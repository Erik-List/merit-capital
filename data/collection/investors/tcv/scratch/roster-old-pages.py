#!/usr/bin/env python3
"""Add TCV's 2002-2013 team pages to the partner roster (PRO-169).

partner-roster.py sweeps profile slugs of the first-last shape; TCV's first
two site generations named profile pages /team/<first_last>.html and
/team/<first_last>.php4 (underscore, extension), which its slug rule cannot
see. This reads the same CDX listing, extracts those pages with their capture
years, and merges them into sources/wayback/partner-roster.json under the
source 'cdx-profile-page-legacy'. Run after partner-roster.py.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402

INV = Path(__file__).resolve().parents[1]
RP = INV / "sources/wayback/partner-roster.json"
PAT = re.compile(r"/team/(?:[a-z]+/)?([a-z]+(?:_[a-z]+)+)\.(?:html?|php4?|asp)$", re.I)
SKIP = {"index", "team_bios", "by_geography", "team_by_geography"}

body, code = ia_fetch.get("https://web.archive.org/cdx/search/cdx?url=tcv.com/team/*&output=text"
                          "&filter=statuscode:200&fl=original,timestamp&limit=20000")
if code != "200":
    sys.exit(f"CDX failed: {code}")
per = defaultdict(set)
for line in body.decode("utf-8", "replace").splitlines():
    parts = line.split()
    if len(parts) != 2:
        continue
    orig, ts = parts
    m = PAT.search(orig.split("?")[0])
    if m and m.group(1).lower() not in SKIP:
        per[m.group(1).lower()].add(int(ts[:4]))
rows = json.load(open(RP)) if RP.exists() else []
by = {r["slug"]: r for r in rows}
added = 0
for s, years in sorted(per.items()):
    slug = s.replace("_", "-")
    name = " ".join(w.capitalize() for w in s.split("_"))
    e = by.get(slug)
    if e is None:
        e = {"slug": slug, "name": name, "years_seen": [], "snapshots": 0, "sources": []}
        by[slug] = e
        added += 1
    e["years_seen"] = sorted(set(e["years_seen"]) | years)
    e["first_seen"], e["last_seen"] = e["years_seen"][0], e["years_seen"][-1]
    e["snapshots"] = e.get("snapshots", 0) + len(years)
    if "cdx-profile-page-legacy" not in e["sources"]:
        e["sources"] = sorted(e["sources"] + ["cdx-profile-page-legacy"])
out = sorted(by.values(), key=lambda r: r["slug"])
RP.write_text(json.dumps(out, indent=1) + "\n")
print(f"legacy pages: {len(per)} people, {added} new; roster now {len(out)}")
for s, years in sorted(per.items()):
    print(f"  {s:28} {min(years)}-{max(years)}")
