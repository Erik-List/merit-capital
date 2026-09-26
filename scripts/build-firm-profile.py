#!/usr/bin/env python3
"""Assemble and validate the firm-level profile for an investor.

The researched values — name, website, history, AUM, the curated fund list,
investment stage/geo/range, notable picks — are per-investor DATA and live in
the investor's `investor/investor.json` (the ingest row) and `investor/sources.json`
(per-field provenance: source URL or evidence path, basis, flags). This script
carries none of them. What it does, keyed only by the slug:

  recompute  the evidence-derived fields from the evidence layers:
             hq_location (the newest Form ADV principal office, unless the
             firm's own site disagrees; scripts/firm-offices.py),
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
import importlib.util
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT, Paths, write_atomic  # noqa: E402
import profile_copy  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "formd_issuer_rounds", Path(__file__).resolve().parent / "formd-issuer-rounds.py")
formd_rounds = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(formd_rounds)

_spec = importlib.util.spec_from_file_location(
    "firm_offices", Path(__file__).resolve().parent / "firm-offices.py")
offices = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(offices)

# Researched fields that must already be present in investor.json, each with a
# provenance entry in investor/sources.json. Field semantics, not values.
RESEARCHED_FIELDS = [
    "name", "website", "icon_url", "founding_year", "history",
    "investment_concept", "investment_stage", "investment_geo",
    "investment_range", "notable_investments", "aum", "funds",
]


def indent_of(path: Path, default: int = 2) -> int:
    """The indentation an existing JSON file uses, so a rewrite diffs by content."""
    if path.exists():
        for line in path.read_text().splitlines():
            if line.startswith(" "):
                return len(line) - len(line.lstrip(" "))
    return default


def own_fund_filings(p: Paths) -> dict:
    """The firm's own fund-vehicle Form D filings, keyed by issuer name:
    {name: {cik, filings: [{form, accession, quarter, offering, sold, first_sale,
    pooled}]}}. Derived at build time from the own-desk CIKs in entities.json
    over the local bulk zips, via the issuer-rounds scanner (COLLECTION.md §11).
    Replaces the hand-built fund-formds.json (PRO-113): the roster-name sweep
    only sees a vehicle's filing when a swept person is a related person on it,
    and an accelerator's vehicles name a management LLC instead (YC).
    """
    entities = json.loads(p.entities.read_text())
    own = {str(int(e["cik"])): e["name"] for e in entities
           if e.get("desk") != "external"
           and e.get("vehicle_role") not in ("person", "outside-cofiler")}
    filings, _ = formd_rounds.scan(own, set())
    out: dict = {}
    for f in sorted(filings.values(), key=formd_rounds.sort_key):
        entry = out.setdefault(f["issuer"] or f["slug"], {"cik": f["cik"], "filings": []})
        entry["filings"].append({
            "form": "D/A" if f.get("is_amendment") else "D",
            "accession": f["accession"], "quarter": f["quarter"],
            "offering": f.get("offering_usd"), "sold": f.get("sold_usd"),
            "first_sale": f.get("sale_date"), "pooled": f.get("is_pooled", False)})
    print(f"own fund filings: {sum(len(v['filings']) for v in out.values())} "
          f"on {len(out)} vehicles ({len(own)} own-desk CIKs scanned)")
    return out


def current_people(roster: list, team: list):
    """The live team CMS is the source of record for membership, roles and
    socials; the Wayback roster is the historical cross-check. Position is the
    CMS title where the CMS has one; members the CMS files under its investing
    tabs but leaves untitled are shown as "Partner", which is how the firm's
    own team page presents them. Operators without a title stay null.
    """
    latest = max(p["last_seen"] for p in roster)
    roster_names = {p["name"].lower() for p in roster if p["last_seen"] == latest}

    INVESTING_BUCKETS = {"investing"}

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
         "socials": {"linkedin_url": m.get("linkedin_url") or None,
                     "x_url": m.get("x_url") or None}}
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
        raise SystemExit(f"Refusing to write: investor/sources.json missing "
                         f"provenance for: {unsourced}")

    fund_formds = own_fund_filings(p)
    roster = json.loads((p.wayback / "partner-roster.json").read_text())
    # Only rows the site pull bucketed publish: an unmapped group is how a
    # site's operations staff stays out of the profile (COLLECTION.md §11).
    team = [m for m in json.loads(p.team.read_text()) if m.get("role_bucket")]
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
    # The two paragraphs a reader sees keep one short shape (PRO-147).
    if copy := profile_copy.problems(row, fields):
        raise SystemExit("Refusing to write: the thesis or history breaks the "
                         "shape rule (COLLECTION.md §11): " + "; ".join(copy))
    verify_funds_against_filings(fields["funds"]["value"], fund_formds,
                                 "the firm's own Form D filings (bulk zips)")

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
        # Matched by slug through the sidecar, so a published name can drop a
        # legal suffix ("Snap", not "Snap Inc") and still be checked (PRO-152).
        members = {r["slug"]: r["name"] for r in base
                   if verdicts.get(r["slug"], {}).get("verdict") == "member"}
        if notable := profile_copy.notable_problems(row, fields, members):
            raise SystemExit("Refusing to write: " + "; ".join(notable))

    # ---- recompute the evidence-derived fields
    # HQ: the newest Form ADV principal office, unless the firm's own site
    # disagrees (Erik 2026-09-24; scripts/firm-offices.py has the rule and
    # why the Form D address vote it replaces was wrong for 8VC, Greylock, YC).
    office_record = offices.refresh(p)
    statement = offices.statement_of(p)
    hq = offices.decide(office_record, statement)
    latest_year, people, departed = current_people(roster, team)

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    row.update({
        "hq_location": hq["value"],
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

    fields["hq_location"] = offices.hq_field(office_record, hq, statement)
    if focus_representative:
        fields["investment_scope"] = field(
            scope, "companies/base.json",
            "focus from the firm's own site sector tags on %d base rows, crosswalked "
            "to data/taxonomy/focus.json (crosswalk in config.json), published above "
            "%d companies. Scope type is the curated judgement carried in "
            "investor.json." % (sum(mapped.values()), cfg["focus_min_companies"]))
    fields["individuals"] = field(
        people, "sources/site/team.json",
        f"Live team CMS: {len(people)} members. Positions are CMS titles "
        f"({sum(1 for q in people if q['position'] and q['position'] != 'Partner')} "
        f"explicit); untitled members under the investing tabs render as "
        f"'Partner', the site's own presentation. {len(departed)} names from the "
        f"{latest_year} Wayback roster are no longer on the live team page. "
        f"Socials from profile pages: "
        f"{sum(1 for q in people if q['socials']['linkedin_url'])} LinkedIn, "
        f"{sum(1 for q in people if q['socials']['x_url'])} X.")
    sources["generated_at"] = now

    # Keep each file's existing indentation: a build must not rewrite every
    # line of a file whose content it changed in four places.
    write_atomic(p.investor, json.dumps(row, indent=indent_of(p.investor)) + "\n")
    write_atomic(p.investor_sources,
                 json.dumps(sources, indent=indent_of(p.investor_sources)) + "\n")

    print(f"hq            {hq['value']}  ({hq['won_by']})")
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
