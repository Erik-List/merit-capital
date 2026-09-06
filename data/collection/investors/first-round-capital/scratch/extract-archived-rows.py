#!/usr/bin/env python3
"""Extract the WordPress-era company rows out of the archived captures.

COLLECTION.md §5: the capture body is the evidence. The 2016-2025
/companies/ accordion carries, per company, the firm's own name, a
description, the founders, the location and — from ~2020 — its own
"Initial Partnership: <stage>" label, which is a *candidate* entry_stage
layer and must be scored on the stage golden set (§4) before it is trusted.
The wayback parser keeps only slug+name, so this reads the same cached raw
files a second time and writes the rest as an evidence sidecar.

Output: sources/site/archived-rows.json
  {slug: {name, years: {year: {stage, location, founders, desc, status}}}}
"""
import json
import re
from html import unescape
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
RAW = INV / "sources/wayback/raw"
OUT = INV / "sources/site/archived-rows.json"

BLOCK = re.compile(r'<div id="(?P<slug>[^"]+)" class="company company-preview[^"]*">')
NAME = re.compile(r'<p>\s*<(?:strong class="company-name"|b)>([^<]{1,80})</(?:strong|b)>')
STAGE = re.compile(r'<strong>Initial Partnership:</strong>\s*([A-Za-z][A-Za-z /-]{2,24}?)\s*</p>', re.S)
STAGE2 = re.compile(r'<h4>Initial Partnership</h4>\s*<p>\s*([A-Za-z][A-Za-z /-]{2,24}?)\s*</p>', re.S)
LOC = re.compile(r'<h4>Location</h4>\s*<p>\s*([^<]{2,40}?)\s*</p>', re.S)
LOCF = re.compile(r'data-filter-location="([^"]*)"')
CAT = re.compile(r'data-filter-category="([^"]*)"')
FOUNDER = re.compile(r'<li class="founder">([^<]{2,60})</li>')
DESC = re.compile(r'<span class="hide-mobile">([^<]{5,300})</span>')
STATUS = re.compile(r'(?i)\b(acquired by [A-Z][\w .&\'-]{2,40}|acquired|ipo)\b')


def blocks(html: str):
    starts = [(m.start(), m.group("slug")) for m in BLOCK.finditer(html)]
    for i, (pos, slug) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(html)
        yield slug, html[pos:end]


def main() -> None:
    rows: dict[str, dict] = {}
    for f in sorted(RAW.glob("*-companies.html")):
        year = f.name[:4]
        html = f.read_text(encoding="utf-8", errors="replace")
        seen = 0
        for slug, b in blocks(html):
            nm = NAME.search(b)
            st = STAGE.search(b) or STAGE2.search(b)
            lo = LOC.search(b) or LOCF.search(b)
            r = rows.setdefault(slug, {"name": None, "years": {}})
            if nm and not r["name"]:
                r["name"] = unescape(nm.group(1)).strip()
            entry = {
                "stage": st.group(1).strip() if st else None,
                "location": unescape(lo.group(1)).strip() if lo else None,
                "category": (CAT.search(b).group(1) if CAT.search(b) else None),
                "founders": [unescape(x).strip() for x in FOUNDER.findall(b)],
                "desc": unescape(DESC.search(b).group(1)).strip() if DESC.search(b) else None,
                "status_text": STATUS.search(b).group(1) if STATUS.search(b) else None,
            }
            r["years"][year] = {k: v for k, v in entry.items() if v}
            seen += 1
        print(f"  {f.name}: {seen} blocks")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(rows, indent=1, sort_keys=True) + "\n")
    staged = sum(1 for r in rows.values() if any(y.get("stage") for y in r["years"].values()))
    print(f"\nwrote {OUT.relative_to(INV)} — {len(rows)} companies, {staged} with a firm-stated Initial Partnership")

    # Feed the block enumeration back into the wayback per-year files. The era
    # regex in config.json needs a name to emit a row, and ~130 rows per late
    # capture render without one; the block boundaries find them all. Same
    # shape and same merge rule as wayback-pull.py (keyed slug+path, existing
    # rows win), so an Internet Archive re-run converges over this.
    parsed = INV / "sources/wayback/parsed"
    added = 0
    for f in sorted(RAW.glob("*-companies.html")):
        year = f.name[:4]
        html = f.read_text(encoding="utf-8", errors="replace")
        ts = json.loads((RAW / "companies.snapshots.json").read_text()).get(year, ["", ""])[0]
        dest = parsed / f"{year}.json"
        cur = json.loads(dest.read_text()) if dest.exists() else []
        have = {(r["slug"], r.get("path")) for r in cur}
        for slug, _ in blocks(html):
            key = (slug, "/companies/")
            if key in have:
                continue
            cur.append({"slug": slug, "name": rows[slug]["name"], "path": "/companies/",
                        "snapshot_ts": ts})
            have.add(key)
            added += 1
        if cur:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(json.dumps(sorted(cur, key=lambda r: (r["slug"], r.get("path") or "")),
                                       indent=1) + "\n")
    print(f"merged {added} rows the era regex could not name into sources/wayback/parsed/")


main()
