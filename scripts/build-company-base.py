#!/usr/bin/env python3
"""Join the three evidence layers into an investor's Company Base.

Inputs (under data/collection/investors/<slug>/):
  sources/wayback/parsed/<year>.json   (portfolio listings)
  sources/wayback/partner-roster.json  (people, to exclude from listing eras)
  sources/edgar/edgar-companies.json   (public-market layer)
  sources/edgar/formd-sweep.json       (private board-seat layer)

Outputs:
  base.json      (the evidence layer)
  base.csv       (via run.py export: the merged published surface — base +
                  membership verdict + classification)
  excluded.json  (every partitioned row, with a reason field:
                  build_filter | other_desk | not_member)

Usage: python3 scripts/build-company-base.py <investor-slug>
"""
import argparse
import html
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths, write_atomic  # noqa: E402
from people_common import dedupe_people, name_parts, same_person  # noqa: E402
from rekey_overlays import apply_rename, rename_map  # noqa: E402
from stage_words import earliest_round, unknown_round_words  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("investor")
_args = ap.parse_args()
SLUG = _args.investor
P = Paths(SLUG)
CFG = P.config()
WB = P.wayback
ED = P.edgar

# ---- the firm's own entry-round claim (PRO-131 a, harvested PRO-135)
# Which of the site layer's fields carry the firm's claim about the round IT
# entered, in the order they should be tried. Eligibility is a semantic
# judgement recorded per investor, never a guess by field name: a Getro job
# board also publishes a `stage`, and that one describes the company today.
# COLLECTION.md §5 carries the promoted list and what each scored.
_STAGE_FIELDS = tuple(CFG.get("site_api", {}).get("entry_stage_fields") or ())
# The page the claim is read off, for rows whose own `url` points at the
# company's website rather than the firm's. A listing shared by many rows is a
# legitimate citation HERE — unlike a `web_verified` one — because the page
# states a round for each row on it (COLLECTION.md §6).
_STAGE_LISTING = CFG.get("site_api", {}).get("entry_stage_listing_url") or ""
# ...or the firm's per-company page, where the site has one and the site row
# carries the slug that addresses it (Redpoint's 194-of-195 match against the
# pages its own cited rows already point at).
_STAGE_ROW_URL = CFG.get("site_api", {}).get("entry_stage_row_url") or ""
_FIRM_HOST = (urlparse(CFG.get("wayback", {}).get("site_url_base") or "").netloc
              or "").lower().removeprefix("www.")
_unknown_round_words: Counter = Counter()


def stage_citation(c: dict) -> str:
    """The URL that carries this row's round word: the firm's own per-company
    page where the row has one, else the listing the field was read off."""
    u = str(c.get("url") or "")
    host = urlparse(u).netloc.lower().removeprefix("www.")
    if _FIRM_HOST and host and (host == _FIRM_HOST or host.endswith("." + _FIRM_HOST)):
        return u
    if "web.archive.org" in host and _FIRM_HOST and _FIRM_HOST in u:
        return u  # an archived capture of the firm's own listing
    site_slug = str(c.get("slug") or c.get("site_id") or "")
    if _STAGE_ROW_URL and site_slug:
        return _STAGE_ROW_URL.format(slug=site_slug)
    return _STAGE_LISTING

# Column order, tuned for review: identity → decision → evidence links →
# attribution → classification, with secondary/audit fields trailing.
COLUMN_ORDER = [
    "name", "status", "first_seen", "site_url", "wayback_first_link", "formd_links",
    "edgar_links", "partners_site", "partners_formd", "partner_match", "sector",
    # secondary
    "tier", "lineage", "slug", "wayback_years", "edgar_forms", "edgar_span",
    "edgar_cik", "formd_roles", "formd_max_round_usd", "formd_span",
    "formd_accessions", "notes",
    # The firm's own per-company entry claim, where its site publishes one
    # (Menlo's portfolio-card Milestones: "2011 - Partnered, Series B"). It
    # travels to the queue item as evidence for entry_stage and first_seen —
    # never as a label until it is measured against documented rounds (§6).
    "site_entry_stage", "site_invest_year",
    # ...and what that claim resolves to. `site_entry_stage` is the firm's own
    # words ("Early", "Series C Partner"); `site_entry_round` is the taxonomy
    # stage they collapse onto, empty where they name no single round, and
    # `site_entry_stage_citation` is the listing that says it (PRO-131 a).
    "site_entry_round", "site_entry_stage_citation",
]

# Form D industry branches populated by investment vehicles, banks and property
# entities rather than venture-backed operating companies. Deliberately narrow:
# "Other Banking and Financial Services" and "Other Real Estate" are EXCLUDED
# because that is exactly where fintech and proptech startups classify
# themselves (Prosper, SoFi, LendingHome, Yapstone, Fundrise all sit there).
# Applied only to rows with no other corroborating evidence.
NON_PORTFOLIO_INDUSTRIES = {
    "Investing", "Investment Banking", "Commercial Banking",
    "REITS and Finance", "Residential", "Commercial", "Construction",
    # Audited: all 19 rows previously spared here were noise — property LLCs
    # under a different Ravi Gupta, and Renren deals mis-attributed via the
    # Joseph/Josephine Chen name collision. Being a real fintech is not the
    # test; being a Sequoia deal is, and none of them were.
    "Other Banking and Financial Services", "Other Real Estate",
}
AMBIGUOUS_INDUSTRIES: set[str] = set()

# Legal-entity suffixes only. Descriptor words like "Technology", "Systems",
# "Networks" and "Labs" are part of the company name, not boilerplate: stripping
# them silently merged Linear (developer tools, 2021) with Linear Technology
# (semiconductors, 1980s) into a single row carrying both companies' sectors.
STOP_SUFFIX = re.compile(
    r"\b(inc|corp|corporation|co|company|ltd|limited|llc|l\.l\.c|lp|l\.p|plc|"
    r"gmbh|ag|nv|sa|holdings?|group)\b\.?", re.I)

CMS_DUPLICATE = re.compile(r"^(.+)-([2-9])$")


def norm(name: str) -> str:
    """Join key: legal suffixes and all spacing/punctuation removed, so
    'Mark Logic' (Wayback slug) and 'MarkLogic' (Form D) are one company.
    HTML entities are decoded first — archived markup yields 'Alpha &amp;
    Omega', whose raw form normalises to 'alphaampomega' and never joins."""
    n = html.unescape(name).lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP_SUFFIX.sub(" ", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def norm_words(name: str) -> str:
    """Same as norm() but keeps word boundaries, for prefix comparison:
    'aruba' vs 'aruba networks'. norm() itself strips spaces so that
    'Mark Logic' and 'MarkLogic' join, which destroys that signal."""
    n = html.unescape(name).lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP_SUFFIX.sub(" ", n)
    return re.sub(r"\s+", " ", n).strip()


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load_sector_taxonomy() -> set[str]:
    """Union of Sequoia's own category filter tags from era-C listing pages."""
    tags: set[str] = set()
    for f in (WB / "raw").glob("*-companies.html"):
        html = f.read_text(encoding="utf-8", errors="replace")
        for blob in re.findall(r'data-tags="(\[[^"]*\])"', html):
            try:
                tags.update(json.loads(blob.replace("&quot;", '"')))
            except json.JSONDecodeError:
                pass
    return tags


def main() -> None:
    P.root.mkdir(parents=True, exist_ok=True)
    base: dict[str, dict] = {}  # norm-key -> row
    sector_tags = load_sector_taxonomy()
    roster_slugs = {r["slug"] for r in json.load(open(WB / "partner-roster.json"))}

    def row_for(key: str, display: str) -> dict:
        return base.setdefault(key, {
            "name": display, "slug": slug_of(display),
            "wayback_years": set(), "sectors": set(), "partners_site": set(),
            "wayback_first": None,  # (year, snapshot_ts, path, capture_url)
            "site_listed": False, "site_url": "",
            "edgar_forms": set(), "edgar_first": None, "edgar_last": None,
            "edgar_cik": None, "edgar_accessions": [], "edgar_desk": None,
            "edgar_person_only": False,
            "formd_partners": set(), "formd_roles": set(), "formd_filings": [],
            "formd_amount_max": 0, "formd_first": None, "formd_last": None,
            "notes": [],
        })

    # ---- layer 1: wayback listings
    _roster = json.load(open(WB / "partner-roster.json"))
    people_slugs = {r["slug"] for r in _roster}
    people_names = [r["name"] for r in _roster]
    # A CMS mints "<slug>-2" when a page is created under a slug already in
    # use, so a NAMELESS "/companies/drum-2" beside "/companies/drum" is a
    # second page for one company, and its slug-derived display ("Drum 2") is
    # an artifact, never the company's name (Felicis, 2026-09-21: the rebuild
    # published "Drum 2" and "January 2"). Keyed on the stem being a listed
    # slug of the same investor, so a lone "Sand 9" is untouched; and it only
    # ranks the name (better_name), never merges rows. Opt-in per investor
    # (config wayback.cms_duplicate_pages): YC's directory uses the same
    # suffix for different companies that share a name, and its identity
    # decisions are keyed on those slugs, so ranking there unhooks them.
    CMS_DUP_PAGES = bool(CFG["wayback"].get("cms_duplicate_pages"))
    wb_slugs = {r["slug"] for f in (WB / "parsed").glob("*.json")
                for r in json.load(open(f))}
    for f in sorted((WB / "parsed").glob("*.json")):
        year = int(f.stem)
        for r in json.load(open(f)):
            slug = r["slug"]
            if r["path"].startswith("/us/") and (
                    slug in people_slugs or
                    any(same_person(slug.replace("-", " "), p) for p in people_names)):
                continue  # era-B person page, not a company
            display = html.unescape(r.get("name") or "") or " ".join(
                w.capitalize() for w in slug.replace("_", "-").split("-"))
            key = norm(display) or slug
            row = row_for(key, display)
            # A per-company-page capture names the row after its URL slug
            # ("Brisk Io"); a later listing capture that carries the site's
            # own rendering ("Brisk.io") replaces it. Slug-derived displays
            # are provisional until any rendered name arrives.
            if r.get("name"):
                if row.get("_name_from_slug"):
                    row["name"], row["slug"] = display, slug_of(display)
                    row["_name_from_slug"] = False
            elif "_name_from_slug" not in row:
                row["_name_from_slug"] = True
            cms = CMS_DUPLICATE.match(slug) if CMS_DUP_PAGES else None
            if not r.get("name") and cms and cms.group(1) in wb_slugs \
                    and row["name"] == display:
                row["_cms_duplicate"] = True
            row["wayback_years"].add(year)
            if row["wayback_first"] is None or year < row["wayback_first"][0]:
                row["wayback_first"] = (year, r.get("snapshot_ts", ""), r["path"],
                                        r.get("capture_url") or "")
            # An archived per-company page can state the firm's own investment
            # year even where the live site does not (Khosla's 2017-2023 pages
            # carry <table class=dates> with Founded and Invested). That is the
            # same claim the site layer reads below, from the same publisher,
            # so it feeds the same column rather than a second source — folding
            # it in through site_api instead would count one source twice and
            # lift every archived row from tier B to tier A. Optional key: a
            # parsed row without it behaves exactly as before.
            wy = str(r.get("invest_year") or "")[:4]
            if wy.isdigit():
                row["site_invest_year"] = min(wy, row.get("site_invest_year") or wy)
            for tag in (r.get("filters") or "").split(","):
                tag = tag.strip()
                if not tag:
                    continue
                if tag in sector_tags:
                    row["sectors"].add(tag)
                elif tag in roster_slugs:
                    row["partners_site"].add(
                        " ".join(w.capitalize() for w in tag.split("-")))
                # opaque hash tags are dropped from display, kept in parsed/ raw

    # ---- layer 1b: the investor's own site API (current portfolio)
    # Authoritative and current: catches recent private companies that file no
    # Form D (Section 4(a)(2)) and have not IPO'd, which the archive cannot
    # enumerate because the modern page is JS-rendered with no per-company URLs.
    site_path = P.site / "companies.json"
    site_n = 0
    site_keys: dict[str, str] = {}          # name key -> the site id holding it
    if site_path.exists():
        for c in json.load(open(site_path)):
            key = norm(c["name"])
            if not key:
                continue
            # A company name is not an identity at scale. YC's directory
            # carries 89 names borne by two different companies in different
            # batches (Parse S11, the Facebook-acquired backend, vs Parse
            # F25), and name-keying merged 100 real companies into 89 rows.
            # Where the site publishes its own id, the FIRST row to claim a
            # name key keeps it — so the EDGAR, wayback and Form D layers
            # still join on the name as before — and a later row bearing the
            # same name under a different site id takes its own key instead
            # of silently folding into the first. Sites with no id are
            # unaffected: site_id is empty and the key is the name.
            # Strictly opt-in: `site_id` exists only where the investor's
            # config renames the source's own id into it. It must NOT fall
            # back to the row's `slug`, which is derived from the name —
            # "Mark Logic" and "MarkLogic" carry different slugs and the same
            # name key, and norm() merges them on purpose.
            site_id = str(c.get("site_id") or "")
            collided = False
            if site_id:
                held = site_keys.setdefault(key, site_id)
                if held != site_id:
                    key = f"{key}~{norm(site_id)}"
                    collided = True
                    # Both members of a colliding group take their own site id,
                    # not just the later claimant. Otherwise which row keeps the
                    # bare name slug depends on processing order, and the base
                    # slug ends up pointing at the SIBLING's source record: YC's
                    # base `gather` was the directory's `gather-2`, so every
                    # by-slug evidence lookup returned the wrong company's
                    # batch, one-liner and tags — and a name check cannot catch
                    # it, because the names are identical by construction.
                    first = base.get(key.split("~")[0])
                    if first is not None and first.get("_site_id"):
                        first["slug"] = slug_of(first["_site_id"])
            row = row_for(key, c["name"])
            # The firm's own current rendering is canonical for display and
            # slug — a wayback/CC slug that created the row first must not
            # name it ("assemblyai" vs the site's "Assembly AI").
            row["name"] = c["name"]
            # The PUBLISHED slug must be unique too, not just the internal
            # key: every overlay (classification, the ledger, the queue) joins
            # on slug, so two rows sharing one slug means one row's answers
            # land silently on both and verify's drift check cannot see it.
            # Only the colliding row is re-keyed, onto the site's own id, so
            # the 6,100-odd uncollided rows keep the name-derived slug they
            # already carry in the ledger.
            row["slug"] = slug_of(site_id) if collided else slug_of(c["name"])
            if site_id:
                row["_site_id"] = site_id
            row["site_listed"] = True
            row["site_url"] = c.get("url") or ""
            row["sectors"].update(c.get("sectors") or [])
            # A CMS that names the deal partners (Accel) feeds the same
            # partners_site column the wayback filters do on other sites.
            row["partners_site"].update(p for p in (c.get("partners") or []) if p)
            # The firm's own dated invest claim (year granularity) is
            # first-seen evidence like a listing year; min() below keeps
            # the earliest across layers.
            y = str(c.get("invest_year") or "")[:4]
            if y.isdigit():
                row["site_invest_year"] = min(y, row.get("site_invest_year") or y)
            # The firm's own statement of the round it entered at, where the
            # site publishes one (Menlo's portfolio-card "Milestones": "2011 -
            # Partnered, Series B"). It reaches the queue item as evidence,
            # never as a label: COLLECTION.md 6 requires it to be measured against
            # documented rounds first, and the round it names is the ENTRY round
            # only because that is what the field claims.
            if c.get("site_entry_stage"):
                row["site_entry_stage"] = c["site_entry_stage"]
            # The same claim, resolved to a taxonomy stage. The raw words stay
            # in `site_entry_stage` as the firm wrote them; this column is the
            # single round they collapse onto, and it is EMPTY where they do
            # not collapse onto one -- "Early Stage" and "venture" straddle Seed
            # and Series A, so they bound entry recency and may not mint a
            # stage, exactly as a bare year may not (PRO-131 a).
            for f in ("site_entry_stage",) + _STAGE_FIELDS:
                raw = c.get(f)
                if raw in (None, "", [], {}):
                    continue
                _unknown_round_words.update(unknown_round_words(raw))
                lab = earliest_round(raw)
                if not lab:
                    continue
                row["site_entry_round"] = lab
                row["site_entry_stage_citation"] = stage_citation(c)
                if not row.get("site_entry_stage"):
                    row["site_entry_stage"] = raw if isinstance(raw, str) \
                        else " | ".join(str(x) for x in raw)
                break
            site_n += 1
        print(f"site API portfolio: {site_n} companies")
        staged = sum(1 for r in base.values() if r.get("site_entry_round"))
        if staged or _unknown_round_words:
            print(f"  first-party entry round: {staged} rows from "
                  f"{', '.join(('site_entry_stage',) + _STAGE_FIELDS)}")
            if _unknown_round_words:
                # A site that starts publishing a word the vocabulary does not
                # know is a parser question, not a silent refusal.
                print(f"  unrecognised round words: "
                      f"{dict(_unknown_round_words.most_common(8))}")

    # ---- layer 2: EDGAR public-market filings
    ent_path = P.entities
    person_ciks = {e["cik"] for e in json.load(open(ent_path))
                   if e.get("vehicle_role") == "person"} if ent_path.exists() else set()
    # Names, CIKs, roles and desk all come from each filing's SEC header via
    # edgar-companies.py — no name-shape inference here.
    for c in json.load(open(ED / "edgar-companies.json")):
        key = norm(c["name"])
        if not key or len(key) < 3:
            continue
        row = row_for(key, c["name"])
        row["edgar_forms"].update(c["forms"])
        row["edgar_first"] = c["first"]
        row["edgar_last"] = c["last"]
        row["edgar_cik"] = c["cik"]
        row["edgar_accessions"] = c["accessions"]
        row["edgar_desk"] = c["desk"]
        # Section 16 forms are filed by a natural person about their OWN
        # holdings. A partner's personal Form 3/4 is evidence that the partner
        # sits on that board, not that the firm invested: partners take
        # independent public-company directorships (Jim Goetz on Intel since
        # 2019) and keep filing from board seats won at their next firm
        # (Sameer Gandhi on CrowdStrike since 2013, for Accel, a decade after
        # leaving Sequoia). Only a fund vehicle on the filing shows a position.
        row["edgar_person_only"] = bool(c.get("filer_ciks")) and all(
            person_ciks and fc in person_ciks for fc in c["filer_ciks"])

    # ---- layer 2b: recall additions from the verification loop. Companies the
    # evidence streams missed (no site capture, no US filing), each verified
    # with a citation before entering the ledger. Injected into the working
    # set here so tiering, merging and partitioning treat them like any row.
    bv_early = P.ledger
    if bv_early.exists():
        adds = json.load(open(bv_early)).get(
            SLUG, {}).get("recall_additions", [])
        for add in adds:
            # A recall addition normally keys on its name like any other row.
            # But a name is not an identity on a base whose source publishes
            # two companies under one name: YC Continuity's Convoy (the
            # Seattle freight company) and the directory's own Convoy (a
            # Winter 2022 webhooks company) collide, and keying on the name
            # silently folded the addition into the wrong row. Where the
            # addition declares its own slug AND the name key is already held
            # by a row with a different slug, the declared slug is the key.
            # A landed investor's additions are unaffected: with no collision
            # the key is norm(name) exactly as before.
            add_key = norm(add["name"])
            add_slug = add.get("slug") or slug_of(add["name"])
            held = base.get(add_key)
            if add.get("slug") and held is not None and held.get("slug") != add_slug:
                add_key = norm(add["slug"])
            row = row_for(add_key, add["name"])
            row["slug"] = add_slug
            if add.get("first_seen"):
                # ride the formd_first slot so the assembly's min() picks it up
                row["formd_first"] = row["formd_first"] or str(add["first_seen"])
            if add.get("on_site_now"):
                row["site_listed"] = True
            if add.get("sector"):
                row["sectors"].add(add["sector"])
            row["notes"].append(
                f"recall addition: {add['basis']} ({add.get('citation', '')})")
        if adds:
            print(f"recall additions injected: {len(adds)}")

    # ---- layer 3: Form D sweep
    # Fund vehicles are not portfolio companies. Two independent issuer
    # declarations identify them, and a fund may set either one:
    #   INDUSTRYGROUPTYPE == "Pooled Investment Fund"  (industry category)
    #   ISPOOLEDINVESTMENTFUNDTYPE == true             (separate boolean, set by
    #       funds that categorised themselves as REITs / Investing / etc.)
    pooled_dropped, finance_deferred, ambiguous_industry = Counter(), {}, {}
    initial_only_dropped: Counter = Counter()
    for acc, rec in json.load(open(ED / "formd-sweep.json")).items():
        issuer = rec.get("issuer")
        if not issuer:
            continue
        if rec.get("industry_group") == "Pooled Investment Fund" or rec.get("is_pooled"):
            pooled_dropped[issuer] += 1
            continue
        # A fund that ticked neither flag still self-classifies into the
        # financial-services or real-estate branches, where an operating
        # portfolio company never lands. Deferred rather than dropped: only
        # removed below if nothing else in the base corroborates it.
        ig = rec.get("industry_group")
        if ig in NON_PORTFOLIO_INDUSTRIES:
            finance_deferred[norm(issuer)] = ig
        elif ig in AMBIGUOUS_INDUSTRIES:
            ambiguous_industry[norm(issuer)] = ig
        key = norm(issuer)
        if not key:
            continue
        row = row_for(key, issuer)
        cik = rec.get("cik")
        if cik:
            row["formd_filings"].append((acc, cik))
        for p in rec.get("persons", []):
            # A filed given name of one initial matches any partner sharing the
            # letter, so it cannot carry an attribution on its own. Filtered
            # here as well as in the sweep so an older formd-sweep.json cannot
            # reintroduce the rows (Intuit, Amgen, DocuSign and ~30 ASC LLCs
            # all entered on 'R Williams' / 'A Moore' style matches).
            if len(name_parts(p["person"])[0]) == 1:
                initial_only_dropped[issuer] += 1
                continue
            row["formd_partners"].add(p["person"].title())
            if p.get("relationship"):
                row["formd_roles"].add(p["relationship"])
            q = p.get("quarter", "")[:4]
            if q.isdigit():
                row["formd_first"] = min(row["formd_first"] or q, q)
                row["formd_last"] = max(row["formd_last"] or q, q)
        sold = rec.get("total_sold") or "0"
        if sold.isdigit():
            row["formd_amount_max"] = max(row["formd_amount_max"], int(sold))

    print(f"pooled fund vehicles dropped: {len(pooled_dropped)} issuers "
          f"({sum(pooled_dropped.values())} filings)")
    print(f"initial-only person matches ignored: {len(initial_only_dropped)} issuers "
          f"({sum(initial_only_dropped.values())} attributions)")

    # Entity form: a venture-backed operating company is a corporation or an
    # LLC, essentially never a limited partnership. An LP with no listing
    # evidence is a fund, SPV or professional partnership, not an investment.
    # This is the legal entity type, not a name-content pattern — and the
    # pattern must SAY so: without a separator before the suffix, `LP$` matches
    # the last two letters of an ordinary word and silently deletes the row.
    # Measured on Khosla, where the recall probe's AirHelp was dropped as a
    # limited partnership; Yelp, Gulp and Kelp are the same shape, and any of
    # them would vanish on a base where the row carries no listing evidence.
    LP_FORM = re.compile(r"(?:^|[\s,.])\s*(L\.\s?P\.?|LP)\s*$", re.I)
    lp_dropped = []
    for key, r in list(base.items()):
        if (LP_FORM.search(r["name"]) and not r["wayback_years"]
                and not r["edgar_forms"] and not r["site_listed"]):
            lp_dropped.append(r["name"])
            del base[key]
    if lp_dropped:
        print(f"limited partnerships dropped (not operating companies): "
              f"{len(lp_dropped)}")
        for n in sorted(lp_dropped):
            print(f"    - {n}")

    # Apply the deferred financial/real-estate rule now that all layers are in:
    # drop only where Form D is the sole evidence.
    # A RECALL ADDITION is exempt: it reached the base only because a session
    # verified it against a citation, which is stronger evidence than the
    # industry code this rule reads. Khosla's Dusty Robotics was dropped here
    # as "Construction", re-found by the recall probe, and dropped a second
    # time by the same rule — the probe's whole purpose defeated by a
    # self-classification. (The rule itself stays: 46 of the 48 rows it removed
    # on this run were genuine homonym noise.)
    fin_dropped = []
    for key, industry in finance_deferred.items():
        r = base.get(key)
        if r and any(n.startswith("recall addition:") for n in r.get("notes", [])):
            continue
        if r and not r["wayback_years"] and not r["edgar_forms"] and not r["site_listed"]:
            fin_dropped.append(f"{r['name']} [{industry}]")
            del base[key]
    if fin_dropped:
        print(f"non-portfolio industry, Form D-only ({len(fin_dropped)} dropped):")
        for n in sorted(fin_dropped):
            print(f"    - {n}")

    # ---- tenure check: was the matched partner still at the firm when the
    # round was raised? Form D related-persons are the ISSUER's own officers and
    # directors, so an ex-partner on a filing means they took a job there — not
    # that the firm invested. Flagged, never dropped: the archived-snapshot span
    # is a proxy for tenure, and a rarely-crawled profile under-reports it.
    roster = json.load(open(WB / "partner-roster.json"))
    tenure = {r["name"]: (r["last_seen"], r["snapshots"]) for r in roster}
    CURRENT_FROM, GRACE, MIN_SNAPS = 2025, 3, 3
    stale_flagged, ex_partner_only = 0, []
    for key, r in list(base.items()):
        if not r["formd_partners"] or not r["formd_first"]:
            continue
        filed = int(r["formd_first"])
        stale_notes, any_current = [], False
        # A recall addition is exempt from the ex-partner rule for the same
        # reason it is exempt from the industry rule: it entered because a
        # session verified it against a citation, so an ex-partner on its
        # filing is not the ONLY evidence the row has. Khosla's Dusty Robotics
        # was dropped here on Richard Boyle's tenure after surviving the
        # industry filter -- the probe's finding undone by a second rule.
        if any(n.startswith("recall addition:") for n in r.get("notes", [])):
            continue
        for p in r["formd_partners"]:
            hit = next(((ls, ns) for nm, (ls, ns) in tenure.items()
                        if same_person(nm, p)), None)
            if not hit:
                any_current = True            # unknown -> assume attributable
                continue
            last_seen, snaps = hit
            if snaps < MIN_SNAPS or last_seen >= CURRENT_FROM:
                any_current = True
                continue
            gap = filed - last_seen
            if gap > GRACE:
                stale_notes.append(
                    f"{p} last on site {last_seen}, filing {filed} ({gap}y after)")
            else:
                any_current = True
        if not stale_notes:
            continue
        r["notes"].extend(stale_notes)
        stale_flagged += 1
        # Remove only when an ex-partner is the row's SOLE claim to being a deal:
        # no listing on Sequoia's own site, no Sequoia entity on any SEC filing,
        # and no still-serving partner among the Form D related persons. Anything
        # else stays — Cohesity is a genuine Sequoia company via Bill Coughran and
        # merely also carries Gaurav Garg's post-departure (Wing) filing.
        if not any_current and not r["wayback_years"] and not r["edgar_forms"] \
                and not r["site_listed"]:
            ex_partner_only.append(f"{r['name']} — {stale_notes[0]}")
            del base[key]
    # A Form D filing on its own says nothing about who backed the issuer: the
    # related persons are the ISSUER's officers and directors. The filing enters
    # the base only because a partner was named on it. Once initial-only matches
    # are refused, some rows keep the filing but lose the attribution entirely --
    # and a row with no named partner, no listing and no Sequoia SEC filing has
    # no claim to being a deal at all.
    unattributed = [k for k, r in base.items()
                    if not r["formd_partners"] and not r["partners_site"]
                    and not r["wayback_years"] and not r["site_listed"]
                    and not r["edgar_forms"] and r["formd_filings"]]
    for k in unattributed:
        del base[k]
    if unattributed:
        print(f"removed (Form D filing with no attributable partner): {len(unattributed)}")

    # The mirror of the rule above on the EDGAR side: a row whose only evidence
    # is a partner's PERSONAL Section 16 filing has no fund position behind it.
    personal_only = [k for k, r in base.items()
                     if r["edgar_person_only"] and not r["formd_partners"]
                     and not r["partners_site"] and not r["wayback_years"]
                     and not r["site_listed"] and not r["formd_filings"]]
    for k in personal_only:
        print(f"    - {base[k]['name']} (personal Section 16 filing only)")
        del base[k]
    if personal_only:
        print(f"removed (partner's personal board seat, no fund position): "
              f"{len(personal_only)}")

    if stale_flagged:
        print(f"tenure mismatch flagged: {stale_flagged} rows")
    if ex_partner_only:
        print(f"removed (ex-partner is the only evidence): {len(ex_partner_only)}")
        for n in sorted(ex_partner_only)[:12]:
            print(f"    - {n}")
        if len(ex_partner_only) > 12:
            print(f"    … and {len(ex_partner_only)-12} more")

    # Ambiguous branches stay in the base, annotated so review can adjudicate.
    flagged = 0
    for key, industry in ambiguous_industry.items():
        r = base.get(key)
        if r and not r["wayback_years"] and not r["edgar_forms"] and not r["site_listed"]:
            r["notes"].append(f"Form D industry '{industry}' — verify company vs vehicle")
            flagged += 1
    if flagged:
        print(f"ambiguous industry flagged for review (kept): {flagged}")

    # ---- derive tiers / status / lineage
    rows_out = []
    for key, r in base.items():
        n_sources = sum([bool(r["wayback_years"]), bool(r["edgar_forms"]),
                         bool(r["formd_partners"]), r["site_listed"]])
        if r["edgar_forms"] and n_sources >= 2:
            tier = "A"
        elif n_sources >= 2:
            tier = "A"
        elif r["wayback_years"] or r["site_listed"]:
            tier = "B"
        else:
            tier = "C"
        # Lineage from the filing entity's desk (registry lookup), not name shape.
        # Wayback presence means the home desk listed it themselves, which
        # outranks a single foreign-desk filing.
        listed = r["wayback_years"] or r["site_listed"]
        home_desk = CFG["desks"]["home"]
        lineage = r["edgar_desk"] if (r["edgar_desk"] and not listed) else home_desk
        status = "auto_confirmed" if tier == "A" else "needs_review"
        # Every dated layer competes for first_seen. (Until 2026-09-04 the
        # conditional bound tighter than the concatenation, so a row with any
        # wayback year ignored its Form D first filing and the firm's own
        # dated invest claim — Creandum's site dates were being dropped.)
        first = min(([str(min(r["wayback_years"]))] if r["wayback_years"] else [])
                    + ([r["edgar_first"][:4]] if r["edgar_first"] else [])
                    + ([r["formd_first"]] if r["formd_first"] else [])
                    + ([r["site_invest_year"]] if r.get("site_invest_year") else [])
                    or ["?"])
        # wayback evidence link: the company's own page for eras with
        # per-company pages, the era's listing page otherwise (config-driven)
        wb_link = ""
        if r["wayback_first"] and r["wayback_first"][3]:
            # A parsed row may cite its own capture: where the Internet Archive
            # excludes the site (IVP, 403 on every ivp.com capture), the archive
            # layer is Common Crawl and its index URL is the citation. No row
            # carried the key before IVP, so every earlier book builds as before.
            wb_link = r["wayback_first"][3]
        elif r["wayback_first"]:
            _, ts, path, _ = r["wayback_first"]
            site_base = CFG["wayback"]["site_url_base"]
            target = f"{site_base}{path}/"
            for era in CFG["wayback"]["eras"]:
                if path.startswith(era["path"]):
                    base = era.get("site_url_base", site_base)
                    target = f"{base}{path}/" if era.get("per_company_pages") \
                        else f"{base}{era['path']}"
                    break
            wb_link = f"https://web.archive.org/web/{ts}/{target}"

        def sec_link(cik, acc):
            return (f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                    f"{acc.replace('-', '')}/{acc}-index.htm")

        formd_links = "; ".join(sec_link(cik, acc)
                                for acc, cik in sorted(set(r["formd_filings"])))
        edgar_links = "; ".join(sec_link(r["edgar_cik"], a)
                                for a in sorted(r["edgar_accessions"])[:5]
                                ) if r["edgar_cik"] else ""

        site_p = dedupe_people(r["partners_site"])
        formd_p = dedupe_people(r["formd_partners"])
        if site_p and formd_p:
            agreed = any(same_person(s, f) for s in site_p for f in formd_p)
            pm = "both" if agreed else "site+formd_disagree"
        elif site_p:
            pm = "site_only"
        elif formd_p:
            pm = "formd_only"
        else:
            pm = "none"

        rows_out.append({
            "slug": r["slug"], "name": r["name"], "tier": tier, "status": status,
            "_cms_duplicate": bool(r.get("_cms_duplicate") and r.get("_name_from_slug")),
            "lineage": lineage, "first_seen": first,
            "site_entry_stage": r.get("site_entry_stage") or "",
            "site_invest_year": r.get("site_invest_year") or "",
            "site_entry_round": r.get("site_entry_round") or "",
            "site_entry_stage_citation": r.get("site_entry_stage_citation") or "",
            "wayback_years": ",".join(map(str, sorted(r["wayback_years"]))),
            "wayback_first_link": wb_link,
            "site_url": r["site_url"],
            "sector": ",".join(sorted(r["sectors"])),
            "partners_site": "; ".join(site_p),
            "partners_formd": "; ".join(formd_p),
            "partner_match": pm,
            "edgar_forms": ",".join(sorted(r["edgar_forms"])),
            "edgar_span": f"{(r['edgar_first'] or '')[:4]}-{(r['edgar_last'] or '')[:4]}" if r["edgar_first"] else "",
            "formd_roles": ",".join(sorted(r["formd_roles"])),
            "formd_max_round_usd": r["formd_amount_max"] or "",
            "formd_span": f"{r['formd_first']}-{r['formd_last']}" if r["formd_first"] else "",
            "formd_accessions": "; ".join(a for a, _ in sorted(set(r["formd_filings"]))),
            "formd_links": formd_links,
            "edgar_cik": r["edgar_cik"] or "",
            "edgar_links": edgar_links,
            "notes": "; ".join(r["notes"]),
        })

    # ---- membership verification ledger (base v2): durable verdicts under
    # COLLECTION.md plus the investor's decisions file, written by the
    # adversarial review passes and by human sampling.
    # not_member rows leave the published base (preserved in
    # excluded.json, reason not_member); uncertain rows stay, marked for sampling.
    verification_excluded: list[dict] = []
    bv_path = P.ledger
    if bv_path.exists():
        bv_verdicts = json.load(open(bv_path)).get(
            SLUG, {}).get("verdicts", {})
        unc = 0
        for row in list(rows_out):
            rec = bv_verdicts.get(row["slug"])
            if not rec:
                continue
            if rec["verdict"] == "not_member":
                row["status"] = "rejected"
                row["notes"] = "; ".join(filter(None, [
                    row["notes"], f"not_member ({rec['who']}): {rec['basis']}"]))
                rows_out.remove(row)
                verification_excluded.append(row)
            elif rec["verdict"] == "uncertain":
                row["notes"] = "; ".join(filter(None, [
                    row["notes"], f"membership uncertain: {rec['basis']}"]))
                unc += 1
        print(f"verification ledger: {len(verification_excluded)} excluded, "
              f"{unc} uncertain kept")

    # Now that normalization no longer strips descriptor words, the opposite
    # error becomes possible: "Aruba" and "Aruba Networks" as two rows for one
    # company. Flag word-prefix pairs so review can merge them; never merge
    # automatically, since Linear / Linear Technology proves the same shape can
    # be two genuinely different companies.
    # Resolve name-variant duplicates ("Aruba" / "ARUBA NETWORKS, INC.") without
    # human review, using the investor's own publications as the arbiter:
    # if any single snapshot of a listing names BOTH, they are two entries in one
    # published list and therefore two companies (Carbon / Carbon Black, Linear /
    # Linear Technology, Nimble / Nimble Storage). Otherwise they are one company
    # under two renderings and are merged. Differing EDGAR subject CIKs also prove
    # distinctness outright.
    snapshots: dict[str, set] = {}
    site_p = P.site / "companies.json"
    if site_p.exists():
        snapshots["site"] = {norm_words(c["name"]) for c in json.load(open(site_p))}
    for f in (WB / "parsed").glob("*.json"):
        for e in json.load(open(f)):
            disp = e.get("name") or " ".join(
                w.capitalize() for w in e["slug"].replace("_", "-").split("-"))
            snapshots.setdefault(e.get("snapshot_ts", "?"), set()).add(norm_words(disp))

    def last_listed(row: dict) -> int:
        """The most recent year this rendering was seen on the firm's own site."""
        years = [int(y) for y in re.findall(r"(?:19|20)\d\d", row.get("wayback_years") or "")]
        if row.get("first_seen", "").isdigit():
            years.append(int(row["first_seen"]))
        return max(years) if years else 0

    def better_name(a: dict, b: dict) -> str:
        """The company's most RECENT rendering (Erik, 2026-09-19).

        A merge folds two renderings of one company together and has to
        publish one of them. The right one is the latest, because a rename is
        news about the company: Blockstack became Hiro, CyPhy Works became
        Aria Insights. Length is not a proxy for it and points the wrong way
        as often as not -- it reaches back for "Massdrop" over Drop,
        "Remind101" over Remind, "Foxmarks" over Xmarks, and for archive
        spellings like "Trueandco" over True&Co.

        Precedence: the firm's live list, then the rendering seen most
        recently on its site, then Title Case over CAPS, then the longer.
        """
        site_names = snapshots.get("site", set())
        for row in (a, b):
            if norm_words(row["name"]) in site_names:
                return row["name"]
        # A row the live site still links is current whatever the captures say.
        a_live, b_live = bool(a.get("site_url")), bool(b.get("site_url"))
        if a_live != b_live:
            return a["name"] if a_live else b["name"]
        # A CMS duplicate page's slug display loses to any other rendering.
        a_dup, b_dup = bool(a.get("_cms_duplicate")), bool(b.get("_cms_duplicate"))
        if a_dup != b_dup:
            return b["name"] if a_dup else a["name"]
        a_year, b_year = last_listed(a), last_listed(b)
        if a_year != b_year:
            return a["name"] if a_year > b_year else b["name"]
        na, nb = a["name"], b["name"]
        a_caps, b_caps = na.isupper(), nb.isupper()
        if a_caps != b_caps:
            return nb if a_caps else na
        return max((na, nb), key=len)

    def union_rows(keep: dict, gone: dict) -> None:
        """Fold gone's evidence into keep; name/slug/status are the caller's call."""
        for col, sep in (("wayback_years", ","), ("sector", ","),
                         ("edgar_forms", ","), ("formd_roles", ","),
                         ("partners_site", "; "), ("partners_formd", "; "),
                         ("formd_accessions", "; "), ("formd_links", "; "),
                         ("edgar_links", "; ")):
            vals = [v for v in (keep[col].split(sep) + gone[col].split(sep)) if v]
            keep[col] = sep.join(sorted(set(v.strip() for v in vals)))
        for col in ("site_url", "wayback_first_link", "edgar_cik", "edgar_span",
                    "formd_span", "formd_max_round_usd",
                    # The firm's own entry claim travels with the evidence, or a
                    # merge silently deletes the strongest entry_stage layer the
                    # run has. Fifteen Felicis rows lost a published round word
                    # this way -- `Disco Technology` merged into the shorter
                    # `disco` key and arrived with an empty stage, which then
                    # read as "the listing says nothing about this company".
                    "site_entry_stage", "site_entry_round",
                    "site_entry_stage_citation"):
            keep[col] = keep[col] or gone[col]
        # ...and the invest year takes the EARLIER of the two, which is what the
        # site loop's own min() means by it.
        for col in ("site_invest_year",):
            a, b = keep.get(col) or "", gone.get(col) or ""
            keep[col] = min(x for x in (a, b) if x) if (a or b) else ""
        if gone["first_seen"].isdigit() and (not keep["first_seen"].isdigit()
                                             or gone["first_seen"] < keep["first_seen"]):
            keep["first_seen"] = gone["first_seen"]
        if "A" in (keep["tier"], gone["tier"]):
            keep["tier"] = "A"
        keep["notes"] = "; ".join(filter(None, [keep["notes"], gone["notes"]]))

    # Durable identity corrections from the outcome runs (renames like
    # Square -> Block, legal-entity aliases like ZenLeads -> Apollo.io, fund
    # vehicles, decision-desk reassignments). Curated with evidence in
    # identity-merges.json; re-applied on every rebuild like review decisions.
    overlay = {}
    idm_path = P.identity_merges
    if idm_path.exists():
        overlay = json.load(open(idm_path)).get(SLUG, {})
    never_merge = {frozenset(p["slugs"]) for p in overlay.get("never_merge", [])}

    by_key = {norm_words(r["name"]): r for r in rows_out}
    merged, distinct = 0, 0
    drop: set[int] = set()
    for k, r in sorted(by_key.items()):
        if id(r) in drop:
            continue
        for k2, r2 in by_key.items():
            if not k or k is k2 or id(r2) in drop or not k2.startswith(k + " "):
                continue
            co = any(k in names and k2 in names for names in snapshots.values())
            # Differing subject CIKs prove distinctness only when both rows are
            # independently listed. A company files through several legal
            # entities (Aurora Innovation / Aurora Operations), so an
            # EDGAR-only row with its own CIK is usually a filing vehicle of the
            # listed company, not a separate investment.
            both_listed = (r["site_url"] or r["wayback_years"]) and \
                          (r2["site_url"] or r2["wayback_years"])
            ciks_differ = (both_listed and r["edgar_cik"] and r2["edgar_cik"]
                           and r["edgar_cik"] != r2["edgar_cik"])
            if co or ciks_differ or frozenset((r["slug"], r2["slug"])) in never_merge:
                distinct += 1
                continue
            keep, gone = r, r2
            keep["name"] = better_name(r, r2)
            keep["_cms_duplicate"] = (r if keep["name"] == r["name"] else r2).get("_cms_duplicate", False)
            keep["slug"] = slug_of(keep["name"])
            union_rows(keep, gone)
            drop.add(id(gone))
            merged += 1
    rows_out = [r for r in rows_out if id(r) not in drop]
    print(f"duplicate name-variants merged: {merged}; "
          f"kept separate (co-listed or differing CIK): {distinct}")

    # ---- identity overlay: merges, rejects, desk moves
    by_slug = {r["slug"]: r for r in rows_out}
    idm_merged, rejected = 0, []
    for m in overlay.get("merges", []):
        keep = by_slug.get(m["canonical"])
        if keep is None:
            print(f"  overlay: canonical '{m['canonical']}' not in base, group skipped")
            continue
        for ds in m["duplicates"]:
            gone = by_slug.pop(ds, None)
            if gone is None or gone is keep:
                continue
            # Chosen BEFORE the union, which would merge the two rows'
            # listing years together and destroy the recency comparison.
            pinned_name = m.get("name") or better_name(keep, gone)
            dup_flag = False if m.get("name") else \
                (keep if pinned_name == keep["name"] else gone).get("_cms_duplicate", False)
            union_rows(keep, gone)
            # The site's own rendering owns the name (COLLECTION.md 5). An
            # identity merge can absorb the row that carries the CURRENT name
            # into one created from an old archive slug — YC's OpenReplay into
            # a row still called "Asayer" — so the same better_name rule the
            # near-duplicate path uses is applied here too, and the published
            # name follows the firm rather than the archive.
            # ...unless the merge pins its display name: the author of a merge
            # knows which entity the position is (Menlo's Chipcom, absorbed
            # into a CMS row filed under the acquirer 3Com), and the
            # longest-rendering fallback would publish the wrong one.
            keep["name"] = pinned_name
            keep["_cms_duplicate"] = dup_flag
            keep["notes"] = "; ".join(filter(None, [
                keep["notes"], f"absorbed {ds} ({m['reason']})"]))
            rows_out.remove(gone)
            idm_merged += 1
    for rj in overlay.get("rejects", []):
        gone = by_slug.pop(rj["slug"], None)
        if gone is None:
            continue
        gone["status"] = "rejected"
        gone["notes"] = "; ".join(filter(None, [gone["notes"], f"rejected: {rj['reason']}"]))
        rows_out.remove(gone)
        rejected.append(gone)
    desk_moved = 0
    for dk in overlay.get("desk", []):
        r = by_slug.get(dk["slug"])
        if r is not None and r["lineage"] != dk["lineage"]:
            r["lineage"] = dk["lineage"]
            desk_moved += 1
    if overlay:
        print(f"identity overlay: {idm_merged} duplicate rows merged, "
              f"{len(rejected)} rejected, {desk_moved} desk reassignments")

    # Merging unions evidence, so tier must be recomputed: a row that was
    # single-source before may now be corroborated by two.
    for r in rows_out:
        n = sum([bool(r["wayback_years"]), bool(r["edgar_forms"]),
                 bool(r["partners_formd"] or r["formd_links"]), bool(r["site_url"])])
        r["tier"] = "A" if n >= 2 else ("B" if (r["wayback_years"] or r["site_url"]) else "C")
        if r["status"] not in ("human_confirmed", "human_rejected"):
            r["status"] = "auto_confirmed" if r["tier"] == "A" else "needs_review"

    # Partition by desk: companies whose only investor evidence is a split-off
    # desk belong to that desk's firm under the decision-desk attribution rule,
    # so they leave the home-desk denominator.
    partition = set(CFG["desks"]["partition"])
    other = [r for r in rows_out if r["lineage"] in partition]
    rows_out = [r for r in rows_out if r["lineage"] not in partition]
    if other:
        print(f"other-desk companies moved out: {len(other)} "
              f"({dict(Counter(r['lineage'] for r in other))})")

    # One partition surface: every row that leaves the published base lands in
    # excluded.json with the reason it left, preserved and reversible.
    excluded_rows = (
        [("build_filter", r) for r in sorted(rejected, key=lambda x: x["slug"])]
        + [("other_desk", r) for r in sorted(other, key=lambda x: x["slug"])]
        + [("not_member", r) for r in verification_excluded]
    )
    write_atomic(P.excluded, "[" + ",\n".join(          # one row per line
        json.dumps({"reason": reason, **{k: r[k] for k in COLUMN_ORDER}})
        for reason, r in excluded_rows) + "]\n")
    print(f"excluded.json: {len(excluded_rows)} rows "
          f"({dict(Counter(reason for reason, _ in excluded_rows))})")

    # Slug uniqueness is an invariant, not a hope. Every overlay — the
    # classification file, the verdict ledger, the work queue — joins on slug,
    # so two rows sharing one means one row's answers land silently on both and
    # verify's drift check (invariant 8) cannot see it: the keys are all
    # present, they just describe the wrong company. YC is the first base where
    # this can happen at all, because it is the first whose source publishes
    # two different companies under one name (89 such pairs). Enforced here,
    # after every merge and overlay has run, so nothing downstream can
    # reintroduce a collision: the first row keeps the bare slug and each later
    # claimant takes its own site id, falling back to an ordinal.
    seen_slug: dict[str, int] = {}
    reslugged = 0
    for r in rows_out:
        base_slug = r["slug"]
        if base_slug not in seen_slug:
            seen_slug[base_slug] = 1
            continue
        cand = slug_of(r.get("_site_id") or "") or ""
        if not cand or cand in seen_slug:
            seen_slug[base_slug] += 1
            cand = f"{base_slug}-{seen_slug[base_slug]}"
        while cand in seen_slug:
            seen_slug[base_slug] = seen_slug.get(base_slug, 1) + 1
            cand = f"{base_slug}-{seen_slug[base_slug]}"
        r["notes"] = "; ".join(filter(None, [
            r["notes"], f"slug {base_slug} -> {cand}: another company of the "
            f"same name already holds it"]))
        r["slug"] = cand
        seen_slug[cand] = 1
        reslugged += 1
    if reslugged:
        print(f"slug collisions resolved: {reslugged}")

    rows_out.sort(key=lambda x: (x["tier"], x["slug"]))
    rows_out = [{k: r[k] for k in COLUMN_ORDER} for r in rows_out]
    # A rebuild that renames a row must not orphan its verdict and its
    # classification: the overlays all join on the slug, and a rename is
    # indistinguishable from a departure once the old base is gone. Match the
    # two sides on evidence the rename does not touch, and move the answers
    # before the new base lands.
    if P.base_json.exists():
        renames = rename_map(json.loads(P.base_json.read_text()), rows_out)
        if renames:
            print(f"rows renamed by the rebuild: {len(renames)}")
            for old_slug, new_slug in sorted(renames.items()):
                print(f"    {old_slug} -> {new_slug}")
            for line in apply_rename(P, renames):
                print(f"    {line}")
    write_atomic(P.base_json, json.dumps(rows_out, indent=1))

    # Base and classification share one surface: the sibling CSV is the merged
    # export (base + membership verdict + classification overlays), so it is
    # regenerated on every rebuild. A base without a classification run just
    # leaves those fields empty.
    for cmd in ("export", "review"):
        subprocess.run([sys.executable, str(Path(__file__).parent / "run.py"),
                        cmd, "--investor", SLUG], check=True)

    tiers = {}
    for r in rows_out:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    multi = sum(1 for r in rows_out if r["tier"] == "A")
    print(f"total rows: {len(rows_out)}  tiers: {tiers}")
    print(f"auto_confirmed: {sum(1 for r in rows_out if r['status']=='auto_confirmed')}")
    print(f"needs_review:   {sum(1 for r in rows_out if r['status']=='needs_review')}")


if __name__ == "__main__":
    main()
