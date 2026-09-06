#!/usr/bin/env python3
"""Rewrite the 2010-2011 logo-wall artifact slugs and names in the parsed
wayback year files, so the rebuild produces the real company rather than the
firm's own upload filename. Curated map: sources/logo-era-names.json.

Idempotent. Run after any wayback-pull.py run and before a base rebuild:
    python3 data/collection/investors/first-round-capital/scratch/fix-logo-names.py
"""
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
raw = json.loads((INV / "sources/logo-era-names.json").read_text())["fix"]
# The era's slugs are the firm's own upload FILENAMES, so they arrive with the
# original capitalisation and underscores ("Gigya_Small", "path_s", "Uber_Small")
# and the build normalises them only later. Match on a normalised key so one map
# entry covers every spelling of a filename.
def key(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())
fix = {key(k): v for k, v in raw.items()}
parsed = INV / "sources/wayback/parsed"

changed = files = 0
for f in sorted(parsed.glob("*.json")):
    rows = json.loads(f.read_text())
    out, seen, hit = [], set(), False
    for r in rows:
        m = fix.get(key(r["slug"]))
        if m:
            if (r["slug"], r.get("name")) != (m["slug"], m["name"]):
                hit = True
            r = {**r, "slug": m["slug"], "name": m["name"]}
        # Key on the slug alone, not (slug, path): the rewrite maps the logo-era
        # filename onto a company the text list already carried that year under
        # a different path, and two rows of one company in one year make the
        # base build disambiguate them into "gigya" and "gigya-1".
        rowkey = r["slug"]
        if rowkey in seen:          # the rewrite can collide two filename variants
            changed += 1
            continue
        seen.add(rowkey)
        out.append(r)
    if hit or len(out) != len(rows):
        f.write_text(json.dumps(sorted(out, key=lambda r: (r["slug"], r.get("path") or "")),
                                indent=1) + "\n")
        files += 1
print(f"logo-era names: rewrote {files} year files, collapsed {changed} filename-variant rows")
