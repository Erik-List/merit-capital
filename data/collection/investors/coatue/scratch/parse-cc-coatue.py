#!/usr/bin/env python3
"""Parse the Common Crawl captures of coatue.com (scratch/cc-raw, written by
pull-cc-coatue.py) into the archive layer's year files,
sources/wayback/parsed/<year>.json, in wayback-pull.py's row shape plus the
capture that cites the row (COLLECTION.md 1: a Common Crawl capture is a valid
citation; IVP's R1 precedent). One row per company per year per page, from the
earliest capture of that page in the year. The pages read: /portfolio (the
grid's first 48 rows, all any capture carries), /privates-portfolio (the
featured grid) and / (the 2026 featured strip). Merges with what
wayback-pull.py writes for the same years (rows keyed slug+path).
Usage: python3 data/collection/investors/coatue/scratch/parse-cc-coatue.py
"""
import json, re
from pathlib import Path
from html import unescape
ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/coatue"
RAW = INV / "scratch/cc-raw"
OUT = INV / "sources/wayback/parsed"
PAT = re.compile(r'"status":"(?:Active|Exit)","name":"(?P<name>[^"]+)"')
def slug_of(n): return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")
best = {}   # (year, path) -> (ts, meta, html)
for meta_p in sorted(RAW.glob("*/*.json")):
    m = json.load(open(meta_p))
    path = re.sub(r"^https?://(www\.)?coatue\.com", "", m["url"]).split("?")[0] or "/"
    if path not in ("/portfolio", "/privates-portfolio", "/"):
        continue
    ts = m["timestamp"]; y = int(ts[:4])
    k = (y, path)
    if k not in best or ts < best[k][0]:
        best[k] = (ts, m, meta_p.with_suffix(".html").read_text("utf-8", "replace"))
years = {}
for (y, path), (ts, m, html) in sorted(best.items()):
    rows = {}
    for mm in PAT.finditer(html):
        name = unescape(mm.group("name")).replace("\\u0026", "&").strip()
        name = json.loads(f'"{name}"') if "\\u" in name else name
        slug = slug_of(name)
        if not slug: continue
        rows[slug] = {"slug": slug, "name": name, "path": path, "snapshot_ts": ts,
                      "capture_url": f"https://index.commoncrawl.org/{m['crawl']}-index?url={m['url']}&output=json",
                      "surface": f"cc:{path}"}
    years.setdefault(y, []).extend(rows.values())
    print(f"  {y} {path}: {len(rows)} rows from {m['crawl']} {ts}")
OUT.mkdir(parents=True, exist_ok=True)
for y, rows in years.items():
    p = OUT / f"{y}.json"
    existing = json.load(open(p)) if p.exists() else []
    keyed = {(r["slug"], r["path"]): r for r in existing}
    for r in rows:
        keyed.setdefault((r["slug"], r["path"]), r)
    merged = sorted(keyed.values(), key=lambda r: (r["path"], r["slug"]))
    p.write_text(json.dumps(merged, indent=1, ensure_ascii=False))
    print(f"{p.name}: {len(merged)} rows")
