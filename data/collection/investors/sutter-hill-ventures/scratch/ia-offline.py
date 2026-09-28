#!/usr/bin/env python3
"""Parse the Internet Archive pages already cached in sources/wayback/raw/ (no
fetching): the IA blocked this machine a third time (240 min) at 22:40 UTC on
2026-09-28, after scratch/ia-eras.py had cached the 2000 and 2001 software
index pages and three company pages. Same naming rules as ia-eras.py; rows
merged into parsed/<year>.json by (slug, path)."""
import importlib.util, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ia", HERE / "ia-eras.py")
src = (HERE / "ia-eras.py").read_text()
# reuse the helpers only: cut the module before the fetching loops
helpers = src.split("years: dict[int, dict] = {}")[0]
ns = {"__file__": str(HERE / "ia-eras.py")}
exec(compile(helpers, "ia-eras-helpers", "exec"), ns)
P, RAW, slug_of, page_name, CURATED, list_name, write_atomic = (ns[k] for k in (
    "P", "RAW", "slug_of", "page_name", "CURATED", "list_name", "write_atomic"))
years = {}
cached = {}
for f in RAW.glob("*_soft_*_html.html"):
    m = re.search(r"/(\d{14})-www_(?:shv|sutterhillventures)_com_80_soft_([a-z0-9_-]+)_html\.html$", str(f))
    if m:
        cached[m.group(2)] = (m.group(1), f.read_bytes().decode("latin-1", errors="replace"))
for f in list(RAW.glob("*software_html.html")):
    m = re.search(r"/(\d{14})-www_(shv|sutterhillventures)_com(?:_80)?_software_html\.html$", str(f))
    if not m:
        continue
    ts, dom = m.group(1), m.group(2)
    body = f.read_bytes().decode("latin-1", errors="replace")
    cap = f"https://web.archive.org/web/{ts}/http://www.{dom}.com/software.html"
    n = 0
    for slug in sorted(set(re.findall(r'href="soft/([a-z0-9_-]+)\.html?"', body))):
        name, desc = CURATED.get(slug) or list_name(slug), ""
        if slug in cached:
            n2, desc = page_name(cached[slug][1], slug)
            name = name or n2
        row = {"slug": slug_of(name) if name else slug, "path": f"/soft/{slug}.html", "snapshot_ts": ts,
               "era": "sector2000", "site_sector": "Software", "capture_url": cap}
        if name:
            row["name"] = name
        if desc:
            row["description"] = desc
        years.setdefault(int(ts[:4]), {})[(row["slug"], row["path"])] = row
        n += 1
    print(f"  software.html {dom} {ts[:8]}: {n}")
for y, rows in sorted(years.items()):
    f = P.wayback / "parsed" / f"{y}.json"
    old = {(r["slug"], r["path"]): r for r in json.load(open(f))} if f.exists() else {}
    old.update(rows)
    write_atomic(f, json.dumps(sorted(old.values(), key=lambda r: (r["slug"], r["path"])), indent=1,
                               ensure_ascii=False) + "\n")
    print(f"{y}: {len(old)} rows; unnamed: {sorted(r['path'] for r in rows.values() if not r.get('name'))}")
