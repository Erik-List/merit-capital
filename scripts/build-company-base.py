#!/usr/bin/env python3
"""Join the three evidence layers into Company Base v0 for Sequoia Capital.

Inputs:
  data/aggregation/sources/wayback/parsed/<year>.json   (portfolio listings)
  data/aggregation/sources/wayback/partner-roster.json  (people, to exclude from era-B)
  data/aggregation/sources/edgar/edgar-companies.json   (public-market layer)
  data/aggregation/sources/edgar/formd-sweep.json       (private board-seat layer)

Outputs:
  data/aggregation/company-base/sequoia-capital.csv
  data/aggregation/company-base/sequoia-capital.json
"""
import csv
import html
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "data" / "aggregation"
WB = ROOT / "sources" / "wayback"
ED = ROOT / "sources" / "edgar"
OUT = ROOT / "company-base"

# Column order, tuned for review: identity → decision → evidence links →
# attribution → classification, with secondary/audit fields trailing.
COLUMN_ORDER = [
    "name", "status", "first_seen", "site_url", "wayback_first_link", "formd_links",
    "edgar_links", "partners_site", "partners_formd", "partner_match", "sector",
    # secondary
    "tier", "lineage", "slug", "wayback_years", "edgar_forms", "edgar_span",
    "edgar_cik", "formd_roles", "formd_max_round_usd", "formd_span",
    "formd_accessions", "notes",
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

# Irregular nicknames only — regular shortenings (pat/patrick, greg/gregory,
# doug/douglas) are caught by the prefix rule in same_person().
NICKNAMES = {
    "bill": "william", "billy": "william", "will": "william",
    "bob": "robert", "bobby": "robert", "rob": "robert",
    "jim": "james", "jimmy": "james", "jamie": "james",
    "dick": "richard", "rick": "richard", "richie": "richard",
    "tom": "thomas", "tommy": "thomas",
    "jack": "john", "johnny": "john",
    "hank": "henry", "harry": "harold",
    "peggy": "margaret", "meg": "margaret",
    "betty": "elizabeth", "liz": "elizabeth", "beth": "elizabeth",
    "kate": "katherine", "kathy": "katherine",
    "sue": "susan", "nancy": "ann",
    "chuck": "charles", "charlie": "charles",
    "ted": "theodore", "teddy": "theodore",
    "gus": "august", "sandy": "alexander",
    "mike": "michael", "mick": "michael",
    "steve": "stephen", "steven": "stephen",
    "geoff": "jeffrey", "jeff": "jeffrey",
    "larry": "lawrence", "gerry": "gerald", "jerry": "gerald",
}


# Feminine variants are different people despite the prefix relationship.
DISTINCT_DESPITE_PREFIX = {
    ("joseph", "josephine"), ("daniel", "danielle"), ("robert", "roberta"),
    ("paul", "paula"), ("michael", "michaela"), ("michel", "michelle"),
    ("samuel", "samantha"), ("alexander", "alexandra"), ("alexand", "alexandra"),
    ("christopher", "christina"), ("christian", "christina"),
    ("patrick", "patricia"), ("francis", "frances"), ("carl", "carla"),
    ("eric", "erica"), ("gabriel", "gabriella"), ("julian", "juliana"),
    ("martin", "martina"), ("nicholas", "nicola"), ("stephan", "stephanie"),
    ("victor", "victoria"), ("jean", "jeanne"), ("simon", "simone"),
    ("louis", "louise"), ("george", "georgia"), ("john", "johanna"),
    ("adrian", "adriana"), ("brian", "briana"), ("justin", "justine"),
}


def name_parts(name: str) -> tuple[str, str]:
    """('Roelof F. Botha') -> ('roelof', 'botha'); middle names/initials dropped."""
    toks = [t for t in re.split(r"[^A-Za-z]+", name.lower()) if t]
    if not toks:
        return ("", "")
    if len(toks) == 1:
        return ("", toks[0])
    return (toks[0], toks[-1])


def canon_first(first: str) -> str:
    return NICKNAMES.get(first, first)


def same_person(a: str, b: str) -> bool:
    """Match two person names, tolerating nicknames, shortenings and initials.

    Requires equal surnames, so a loose given-name rule stays safe.
    """
    fa, la = name_parts(a)
    fb, lb = name_parts(b)
    if not la or la != lb:
        return False
    if not fa or not fb:          # surname-only record
        return True
    ca, cb = canon_first(fa), canon_first(fb)
    if ca == cb:
        return True
    if len(ca) >= 3 and len(cb) >= 3 and (ca.startswith(cb) or cb.startswith(ca)):
        short, long_ = sorted((ca, cb), key=len)
        return (short, long_) not in DISTINCT_DESPITE_PREFIX
    if len(fa) == 1 or len(fb) == 1:
        return fa[0] == fb[0]     # 'R. Botha' vs 'Roelof Botha'
    return False


def dedupe_people(names) -> list[str]:
    """Collapse name variants of one person, keeping the most complete form."""
    kept: list[str] = []
    for n in sorted(names, key=lambda x: (-len(x), x)):
        if not any(same_person(n, k) for k in kept):
            kept.append(n)
    return sorted(kept)


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
    OUT.mkdir(parents=True, exist_ok=True)
    base: dict[str, dict] = {}  # norm-key -> row
    sector_tags = load_sector_taxonomy()
    roster_slugs = {r["slug"] for r in json.load(open(WB / "partner-roster.json"))}

    def row_for(key: str, display: str) -> dict:
        return base.setdefault(key, {
            "name": display, "slug": slug_of(display),
            "wayback_years": set(), "sectors": set(), "partners_site": set(),
            "wayback_first": None,  # (year, snapshot_ts, path)
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
            row["wayback_years"].add(year)
            if row["wayback_first"] is None or year < row["wayback_first"][0]:
                row["wayback_first"] = (year, r.get("snapshot_ts", ""), r["path"])
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
    site_path = ROOT / "sources" / "site" / "companies.json"
    site_n = 0
    if site_path.exists():
        for c in json.load(open(site_path)):
            key = norm(c["name"])
            if not key:
                continue
            row = row_for(key, c["name"])
            row["site_listed"] = True
            row["site_url"] = c.get("url") or ""
            row["sectors"].update(c.get("sectors") or [])
            site_n += 1
        print(f"site API portfolio: {site_n} companies")

    # ---- layer 2: EDGAR public-market filings
    ent_path = ROOT / "entities" / "sequoia-capital.json"
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
    # This is the legal entity type, not a name-content pattern.
    LP_FORM = re.compile(r",?\s*(L\.\s?P\.?|LP)\s*$", re.I)
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
    fin_dropped = []
    for key, industry in finance_deferred.items():
        r = base.get(key)
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
        # Wayback presence means Sequoia US/EU listed it themselves, which
        # outranks a single foreign-desk filing.
        listed = r["wayback_years"] or r["site_listed"]
        lineage = r["edgar_desk"] if (r["edgar_desk"] and not listed) else "us-eu"
        status = "auto_confirmed" if tier == "A" else "needs_review"
        first = min([str(min(r["wayback_years"]))] if r["wayback_years"] else []
                    + ([r["edgar_first"][:4]] if r["edgar_first"] else [])
                    + ([r["formd_first"]] if r["formd_first"] else []) or ["?"])
        # wayback evidence link: per-company page for eras A/B, listing page for C/D
        wb_link = ""
        if r["wayback_first"]:
            _, ts, path = r["wayback_first"]
            if path.startswith(("/company/", "/us/")):
                target = f"https://www.sequoiacap.com{path}/"
            elif path.startswith("/our-companies"):
                target = "https://www.sequoiacap.com/our-companies/"
            else:
                target = "https://www.sequoiacap.com/companies/"
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
            "lineage": lineage, "first_seen": first,
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

    # ---- human review layer: durable, re-applied on every rebuild
    dec_path = OUT / "review-decisions.json"
    if dec_path.exists():
        decisions = json.load(open(dec_path)).get("sequoia-capital", {})
        applied = 0
        for row in rows_out:
            rec = decisions.get(row["slug"])
            if not rec:
                continue
            d = rec.get("d")
            if d == "confirmed":
                row["status"] = "human_confirmed"
            elif d == "rejected":
                row["status"] = "human_rejected"
            if rec.get("note"):
                row["notes"] = "; ".join(filter(None, [row["notes"], rec["note"]]))
            applied += 1
        print(f"human decisions applied: {applied}")

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
    site_p = ROOT / "sources" / "site" / "companies.json"
    if site_p.exists():
        snapshots["site"] = {norm_words(c["name"]) for c in json.load(open(site_p))}
    for f in (WB / "parsed").glob("*.json"):
        for e in json.load(open(f)):
            disp = e.get("name") or " ".join(
                w.capitalize() for w in e["slug"].replace("_", "-").split("-"))
            snapshots.setdefault(e.get("snapshot_ts", "?"), set()).add(norm_words(disp))

    def better_name(a: str, b: str) -> str:
        """Prefer the investor's own current rendering, then Title Case over CAPS."""
        site_names = snapshots.get("site", set())
        for n in (a, b):
            if norm_words(n) in site_names:
                return n
        a_caps, b_caps = a.isupper(), b.isupper()
        if a_caps != b_caps:
            return b if a_caps else a
        return max((a, b), key=len)

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
                    "formd_span", "formd_max_round_usd"):
            keep[col] = keep[col] or gone[col]
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
    idm_path = OUT / "identity-merges.json"
    if idm_path.exists():
        overlay = json.load(open(idm_path)).get("sequoia-capital", {})
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
            keep["name"] = better_name(r["name"], r2["name"])
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
            union_rows(keep, gone)
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

    # Partition by desk: companies whose only investor evidence is a foreign desk
    # belong to HongShan / Peak XV under the decision-desk attribution rule, so
    # they leave the Sequoia US/EU denominator.
    other = [r for r in rows_out if r["lineage"] in ("china", "india")]
    rows_out = [r for r in rows_out if r["lineage"] not in ("china", "india")]

    def write_csv(path: Path, rows: list[dict]) -> None:
        rows = [{k: r[k] for k in COLUMN_ORDER} for r in rows]
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLUMN_ORDER)
            w.writeheader()
            w.writerows(rows)
        return rows

    if other:
        other.sort(key=lambda x: x["slug"])
        write_csv(OUT / "other-desk-companies.csv", other)
        print(f"other-desk companies moved out: {len(other)} "
              f"({dict(Counter(r['lineage'] for r in other))})")

    if rejected:
        rejected.sort(key=lambda x: x["slug"])
        write_csv(OUT / "rejected-rows.csv", rejected)

    rows_out.sort(key=lambda x: (x["tier"], x["slug"]))
    rows_out = write_csv(OUT / "sequoia-capital.csv", rows_out)
    json.dump(rows_out, open(OUT / "sequoia-capital.json", "w"), indent=1)

    tiers = {}
    for r in rows_out:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    multi = sum(1 for r in rows_out if r["tier"] == "A")
    print(f"total rows: {len(rows_out)}  tiers: {tiers}")
    print(f"auto_confirmed: {sum(1 for r in rows_out if r['status']=='auto_confirmed')}")
    print(f"needs_review:   {sum(1 for r in rows_out if r['status']=='needs_review')}")


if __name__ == "__main__":
    main()
