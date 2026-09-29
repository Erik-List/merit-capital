#!/usr/bin/env python3
"""Merge the curated roster notes into the swept roster (PRO-169).

sources/wayback/roster-notes.json carries the people the page sweeps cannot
date: TCV partners and officers who file Section 16 forms beside the funds
(the window is their first and last such filing on EDGAR, read from
sources/edgar/fts-hits.json), and the officers named on the firm's own fund
Form Ds. Each note is one person, one basis line. The merge unions their years
into sources/wayback/partner-roster.json under the source 'curated', and
collapses spelling variants of one person onto one slug (COLLECTION.md 8: a
person under two spellings is two people to the tenure filter).
Run last in the roster chain: partner-roster.py, roster-old-pages.py,
parse-cc-tcv.py (team pages), then this.
"""
import json
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
RP = INV / "sources/wayback/partner-roster.json"
NOTES = INV / "sources/wayback/roster-notes.json"

notes = json.load(open(NOTES))["people"]
rows = {r["slug"]: r for r in (json.load(open(RP)) if RP.exists() else [])}
for n in notes:
    slug = n["slug"]
    for alias in n.get("aliases", []):
        if alias in rows and alias != slug:
            a = rows.pop(alias)
            e = rows.setdefault(slug, {"slug": slug, "name": n["name"], "years_seen": [], "snapshots": 0, "sources": []})
            e["years_seen"] = sorted(set(e["years_seen"]) | set(a["years_seen"]))
            e["snapshots"] = e.get("snapshots", 0) + a.get("snapshots", 0)
            e["sources"] = sorted(set(e["sources"]) | set(a["sources"]))
    e = rows.setdefault(slug, {"slug": slug, "name": n["name"], "years_seen": [], "snapshots": 0, "sources": []})
    e["name"] = n["name"]
    e["years_seen"] = sorted(set(e["years_seen"]) | set(range(n["from"], n["to"] + 1)))
    e["first_seen"], e["last_seen"] = e["years_seen"][0], e["years_seen"][-1]
    if "curated" not in e["sources"]:
        e["sources"] = sorted(e["sources"] + ["curated"])
    e["basis"] = n["basis"]
# the live team's investors (site role 'Investor'), as current-year evidence (partner-roster.py
# adds them too when it runs; this keeps the roster complete while the archive is closed)
import time
team = INV / "sources/site/team.json"
if team.exists():
    y = int(time.strftime("%Y"))
    for r in json.load(open(team)):
        if r.get("group") != "Investor":
            continue
        slug = r.get("slug") or r["url"].rstrip("/").rsplit("/", 1)[-1]
        e = rows.setdefault(slug, {"slug": slug, "name": r["name"], "years_seen": [], "snapshots": 0, "sources": []})
        e["name"] = r["name"]
        e["years_seen"] = sorted(set(e["years_seen"]) | {y})
        e["first_seen"], e["last_seen"] = e["years_seen"][0], e["years_seen"][-1]
        if "site-team" not in e["sources"]:
            e["sources"] = sorted(e["sources"] + ["site-team"])
out = sorted(rows.values(), key=lambda r: r["slug"])
RP.parent.mkdir(parents=True, exist_ok=True)
RP.write_text(json.dumps(out, indent=1) + "\n")
print(f"roster: {len(out)} people after merging {len(notes)} curated notes")
