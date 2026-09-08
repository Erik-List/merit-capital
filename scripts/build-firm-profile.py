#!/usr/bin/env python3
"""Assemble and validate the firm-level profile for an investor.

The researched values — name, website, history, AUM, the curated fund list,
investment stage/geo/range, notable picks — are per-investor DATA and live in
the investor's `investor.json` (the ingest row) and `investor.sources.json`
(per-field provenance: source URL or evidence path, basis, flags). This script
carries none of them. What it does, keyed only by the slug:

  recompute  the evidence-derived fields from the evidence layers:
             hq_location (issuer address on the firm's own Form D filings),
             individuals (live team CMS + Wayback roster cross-check),
             investment_scope.focus (site sector tags crosswalked to the
             closed taxonomy, thresholds and crosswalk in config.json)
  validate   the curated claims against the evidence: every fund entry naming
             a Form D accession must match the filed amount, and every
             notable pick must be a ledger-verified member of the base
  refresh    updated_at, and the provenance entries of the recomputed fields

A field with no evidence stays null with its recorded reason. Nothing here may
mint a researched value; a missing one is a hard error, fixed by editing the
investor's data files, not this script.

Usage: python3 scripts/build-firm-profile.py <investor-slug>
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT, Paths, write_atomic  # noqa: E402

# Researched fields that must already be present in investor.json, each with a
# provenance entry in investor.sources.json. Field semantics, not values.
RESEARCHED_FIELDS = [
    "name", "website", "icon_url", "founding_year", "history",
    "investment_concept", "investment_stage", "investment_geo",
    "investment_range", "notable_investments", "aum", "funds",
]


def own_formd_filings(sweep: dict, own_re: re.Pattern) -> dict:
    """The firm's own fund filings, split from the portfolio companies."""
    out = defaultdict(list)
    for accession, rec in sweep.items():
        if own_re.search(rec["issuer"]):
            out[rec["issuer"]].append((accession, rec))
    return out


# EDGAR files a non-US issuer's country in the "state" slot, as a two-character
# code from its "State or Country" list (a US fund reads "CA", a Swedish AB
# fund reads "V7"); a German issuer files its city with the district ("BERLIN - MITTE"),
# which is stripped to the municipality (Cherry, 2026-09-04). The profile publishes the country name for those, so an EU
# fund's hq_location reads "Stockholm, Sweden" rather than "Stockholm, V7"
# (Creandum, PRO-72). Codes outside the table fall through unchanged.
EDGAR_COUNTRY_CODES = {
    "2M": "Germany", "C4": "Austria", "C9": "Belgium", "E9": "Cayman Islands",
    "G7": "Denmark", "H9": "Finland", "I0": "France", "L2": "Ireland",
    "L3": "Israel", "L6": "Italy", "N4": "Luxembourg", "P7": "Netherlands",
    "Q8": "Norway", "U3": "Spain", "V7": "Sweden", "V8": "Switzerland",
    "X0": "United Kingdom", "Y7": "Guernsey", "Y9": "Jersey", "1J": "Estonia",
}


def hq_from_filings(own: dict):
    """Issuer address on the firm's own filings. Filing-grade."""
    places = Counter(
        f'{re.sub(r"\s+-\s+.*$", "", r["city"]).title()}, {EDGAR_COUNTRY_CODES.get(r["state"], r["state"])}'
        for items in own.values() for _, r in items
    )
    return places.most_common(1)[0], places


def current_people(roster: list, team: list):
    """The live team CMS is the source of record for membership, roles and
    socials; the Wayback roster is the historical cross-check. Position is the
    CMS title where the CMS has one; members the CMS files under its investing
    tabs but leaves untitled are shown as "Partner", which is how the firm's
    own team page presents them. Operators without a title stay null.
    """
    latest = max(p["last_seen"] for p in roster)
    roster_names = {p["name"].lower() for p in roster if p["last_seen"] == latest}

    INVESTING_BUCKETS = {"seed-early", "growth", "investing"}

    def position(m):
        if m.get("cms_title"):
            return m["cms_title"]
        if set(m.get("role_bucket", [])) & INVESTING_BUCKETS:
            return "Partner"
        return None

    def sort_key(m):
        investing = bool(set(m.get("role_bucket", [])) & INVESTING_BUCKETS)
        return (0 if investing else 1, m["name"])

    people = [
        {"name": m["name"], "position": position(m),
         "socials": {"linkedin_url": m.get("linkedin_url"), "x_url": m.get("x_url")}}
        for m in sorted(team, key=sort_key)
    ]
    departed = sorted(n for n in roster_names
                      if n not in {m["name"].lower() for m in team})
    return latest, people, departed


def focus_from_site_tags(base: list, crosswalk: dict, min_companies: int):
    tags = Counter()
    for row in base:
        for tag in filter(None, (row.get("sector") or "").split(",")):
            tags[tag.strip()] += 1
    mapped, unmapped = Counter(), Counter()
    for tag, count in tags.items():
        target = crosswalk.get(tag)
        (mapped if target else unmapped)[target or tag] += count
    published = [f for f, c in mapped.most_common() if c >= min_companies]
    return published, mapped, unmapped


def verify_funds_against_filings(funds: list, fund_formds: dict, formds_path: str):
    """Every curated entry naming an accession must match the filed amount."""
    by_accession = {}
    for name, v in fund_formds.items():
        for f in v.get("filings", []):
            by_accession[f["accession"]] = (name, f.get("sold"))
    for fund in funds:
        acc = fund.get("accession")
        if not acc:
            continue
        if acc not in by_accession:
            raise SystemExit(f"Refusing to write: accession {acc} not in {formds_path}")
        _, sold = by_accession[acc]
        if int(sold or 0) != fund["size"]:
            raise SystemExit(
                f"Refusing to write: {fund['name']} size {fund['size']:,} does not "
                f"match filed amount {int(sold or 0):,} on {acc}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    args = ap.parse_args()

    p = Paths(args.investor)
    cfg = p.config()["profile"]
    own_re = re.compile(cfg["own_vehicle_pattern"], re.I)

    if not p.investor.exists() or not p.investor_sources.exists():
        raise SystemExit(
            f"Refusing to write: {p.rel(p.investor)} and {p.rel(p.investor_sources)} "
            f"must exist — they hold the researched profile data this script "
            f"assembles around")
    row = json.loads(p.investor.read_text())
    sources = json.loads(p.investor_sources.read_text())
    fields = sources.setdefault("fields", {})

    missing = [k for k in RESEARCHED_FIELDS if row.get(k) is None]
    if missing:
        raise SystemExit(f"Refusing to write: investor.json missing researched "
                         f"field(s): {missing}")
    unsourced = [k for k in RESEARCHED_FIELDS if k not in fields]
    if unsourced:
        raise SystemExit(f"Refusing to write: investor.sources.json missing "
                         f"provenance for: {unsourced}")

    sweep = json.loads((p.edgar / "formd-sweep.json").read_text())
    fund_formds = json.loads((p.edgar / "fund-formds.json").read_text())
    roster = json.loads((p.wayback / "partner-roster.json").read_text())
    team = json.loads((p.site / "team-members.json").read_text())
    # The profile session runs in parallel with the base collection
    # (COLLECTION.md §11), so the base may not exist yet — or may exist
    # mid-membership (the accel run built base.json before its judge pass).
    # The landed signal is ledger coverage, not file existence: a completed
    # run has a membership verdict for every base slug (§10 invariant 1),
    # while needs_review rows persist even then (a16z closed with 563).
    # Until coverage is full, the two checks that need a settled base are
    # skipped loudly and re-run on a later build; nothing else here reads it.
    base = json.loads(p.base_json.read_text()) if p.base_json.exists() else None
    if base is not None:
        verdicts = (json.loads(p.ledger.read_text()).get(p.slug, {})
                    .get("verdicts", {}) if p.ledger.exists() else {})
        unjudged = sum(1 for r in base if r["slug"] not in verdicts)
        if unjudged:
            print(f"base.json is mid-membership ({unjudged} of {len(base)} "
                  f"slugs carry no ledger verdict) — treating the base as "
                  f"not yet landed")
            base = None

    # ---- validate the curated claims against the evidence layers
    verify_funds_against_filings(fields["funds"]["value"], fund_formds,
                                 "sources/edgar/fund-formds.json")

    if base is None:
        print("no base.json yet — notable_investments NOT asserted against the "
              "base and investment_scope.focus NOT recomputed from site tags; "
              "re-run after build-company-base.py")
    else:
        # Membership is the ledger's call (COLLECTION.md §2): build status
        # (auto_confirmed) tracks evidence multiplicity, not membership, and a
        # famous single-source row legitimately sits needs_review while its
        # ledger verdict is member (accel: wayback pending IA recovery left
        # Flipkart/Spotify/Supercell at needs_review-but-member).
        # Case-insensitive: the base carries the site's own casing ("Paypal",
        # "Youtube"), which is not how the names should be published.
        member_names = {r["name"].lower() for r in base
                        if verdicts.get(r["slug"], {}).get("verdict") == "member"}
        not_member = [n for n in row["notable_investments"]
                      if n.lower() not in member_names]
        if not_member:
            raise SystemExit(f"Refusing to write: not ledger-verified members "
                             f"of the base: {not_member}")

    # ---- recompute the evidence-derived fields
    # The roster sweep finds a firm's own vehicles only when a ROSTER HUMAN is
    # named on the filing. That holds for a venture firm, whose fund Form Ds
    # list partners as related persons, and fails for an accelerator: every YC
    # vehicle names a management LLC ("YC Continuity Management I, LLC")
    # instead, so none of its 31 own filings appear in the roster sweep at all.
    # The dedicated fund-filer sweep already has them, so union the two before
    # splitting. Additive: where a filing is in both, it is the same record
    # under the same accession, so this is a no-op for every landed investor.
    own = own_formd_filings(
        {**sweep, **{k: v for k, v in fund_formds.items() if k != "_readme"}},
        own_re)
    (hq, hq_count), hq_places = hq_from_filings(own)
    latest_year, people, departed = current_people(roster, team)

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    row.update({
        "hq_location": hq,
        "individuals": people,
        "updated_at": now,
    })
    # The recompute publishes only when the site tags actually describe the
    # portfolio: a base where few rows carry a sector (a16z: only the
    # accelerator slice, 251/1,807) would derive the firm's focus from an
    # unrepresentative sliver, so the curated enumeration stands instead.
    tagged = sum(1 for r in (base or []) if (r.get("sector") or "").strip())
    focus_representative = base is not None and tagged >= 0.25 * len(base)
    if focus_representative:
        focus, mapped, unmapped = focus_from_site_tags(
            base, cfg["focus_crosswalk"], cfg["focus_min_companies"])
        if not focus:
            # An empty or too-sparse crosswalk must never publish an empty
            # focus list (the a16z near-miss, second form): keep the curated
            # enumeration and say so.
            focus_representative = False
            print("focus recompute produced no values above threshold — "
                  "curated focus kept; check profile.focus_crosswalk in "
                  "config.json")
        else:
            scope = {"type": row["investment_scope"]["type"], "focus": focus}
            row["investment_scope"] = scope
    elif base is not None:
        print(f"focus recompute skipped: only {tagged}/{len(base)} base rows "
              f"carry a sector tag — curated focus kept")

    def field(value, source, basis):
        return {"value": value, "source": source, "basis": basis}

    total = sum(hq_places.values())
    fields["hq_location"] = field(
        hq, "sources/edgar/formd-sweep.json",
        f"issuer address on {hq_count} of {total} of the firm's own Form D "
        f"filings{'; unanimous' if hq_count == total else ''}. Filing-grade.")
    if focus_representative:
        fields["investment_scope"] = field(
            scope, "base.json",
            "focus from the firm's own site sector tags on %d base rows, crosswalked "
            "to data/taxonomy/focus.json (crosswalk in config.json), published above "
            "%d companies. Scope type is the curated judgement carried in "
            "investor.json." % (sum(mapped.values()), cfg["focus_min_companies"]))
    fields["individuals"] = field(
        people, "sources/site/team-members.json",
        f"Live team CMS: {len(people)} members. Positions are CMS titles "
        f"({sum(1 for q in people if q['position'] and q['position'] != 'Partner')} "
        f"explicit); untitled members under the investing tabs render as "
        f"'Partner', the site's own presentation. {len(departed)} names from the "
        f"{latest_year} Wayback roster are no longer on the live team page. "
        f"Socials from profile pages: "
        f"{sum(1 for q in people if q['socials']['linkedin_url'])} LinkedIn, "
        f"{sum(1 for q in people if q['socials']['x_url'])} X.")
    sources["generated_at"] = now

    write_atomic(p.investor, json.dumps(row, indent=2) + "\n")
    write_atomic(p.investor_sources, json.dumps(sources, indent=2) + "\n")

    print(f"hq            {hq}  ({hq_count}/{total} filings)")
    print(f"funds         {len(fields['funds']['value'])}  aum {row['aum']}")
    print(f"individuals   {len(people)}  (current cohort {latest_year}, "
          f"{len(departed)} departed)")
    if focus_representative:
        print(f"focus         {focus}")
        print(f"unmapped tags {[t for t, _ in unmapped.most_common(6)]}")
    else:
        print("focus         kept as researched")
    print(f"\nwrote {p.rel(p.investor)}")
    print(f"wrote {p.rel(p.investor_sources)}")


if __name__ == "__main__":
    main()
