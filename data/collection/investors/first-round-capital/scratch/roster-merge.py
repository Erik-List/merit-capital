#!/usr/bin/env python3
"""Merge the curated roster into the roster partner-roster.py writes.

partner-roster.py rebuilds partner-roster.json wholesale from the capture
archives and the live CMS, so a curated entry does not survive its next run.
First Round needs curation for two reasons: the firm published team pages
only 2005-2015 and the Internet Archive was intermittently offline for this
run, and the fund-side Form D related persons are filing-grade roster
evidence the script has no source for (COLLECTION.md §5, the Thrive recipe).

Run after every partner-roster.py run:
    python3 data/collection/investors/first-round-capital/scratch/roster-merge.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/first-round-capital"
roster_path = INV / "sources/wayback/partner-roster.json"
curated_path = INV / "sources/roster-curated.json"

roster = json.loads(roster_path.read_text())
curated = json.loads(curated_path.read_text())
by_slug = {r["slug"]: r for r in roster}

added, widened = 0, 0
for c in curated:
    r = by_slug.get(c["slug"])
    if r is None:
        e = dict(c)
        # build-company-base.py reads last_seen + snapshots per roster name
        e.setdefault("snapshots", len(c["years_seen"]))
        by_slug[c["slug"]] = e
        added += 1
        continue
    years = sorted(set(r.get("years_seen", [])) | set(c["years_seen"]))
    if years != r.get("years_seen"):
        widened += 1
    r["years_seen"] = years
    r["first_seen"], r["last_seen"] = years[0], years[-1]
    r["snapshots"] = r.get("snapshots", 0) + len(c["years_seen"])
    for s in c["sources"]:
        if s not in r["sources"]:
            r["sources"].append(s)

# Drop the variants the curated file supersedes: a person under two spellings
# splits their tenure window, and build-company-base.py's ex-partner filter
# then reads a partner as departed years before they left.
alias_slugs = set()
for c in curated:
    for a in c.get("aliases", []):
        alias_slugs.add(a.lower().replace(" ", "-").replace("'", ""))
alias_slugs |= {"board-partners", "finance-and-administration", "operating", "investing"}
dropped = [s for s in by_slug if s in alias_slugs]
for s in dropped:
    del by_slug[s]
if dropped:
    print(f"dropped {len(dropped)} name-variant / group-page entries: {sorted(dropped)}")

rows = sorted(by_slug.values(), key=lambda r: r["slug"])
roster_path.write_text(json.dumps(rows, indent=1) + "\n")
print(f"roster: {len(rows)} people ({added} added, {widened} windows widened from the curated file)")
cov = [y for r in rows for y in r["years_seen"]]
print(f"coverage: {min(cov)}–{max(cov)}")
