#!/usr/bin/env python3
"""TechCrunch's (or VentureBeat's) own WordPress search through the shared throttle, with a date window:
python3 tc.py "<term>" [filter-regex] [after YYYY-MM-DD] [before YYYY-MM-DD] [site]"""
import importlib.util, sys, re, json, html, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
term = argv[0]
flt = re.compile(argv[1], re.I) if len(argv) > 1 and argv[1] else None
after = argv[2] if len(argv) > 2 else ""
before = argv[3] if len(argv) > 3 else ""
base = argv[4] if len(argv) > 4 else "https://techcrunch.com"
gs.wait("techcrunch", gs.RATES["techcrunch"])
url = f"{base}/wp-json/wp/v2/posts?search={urllib.parse.quote(term)}&per_page=30&_fields=date,link,title,excerpt"
if after: url += f"&after={after}T00:00:00"
if before: url += f"&before={before}T00:00:00"
code, body = gs.curl(url)
print("http", code)
try:
    posts = json.loads(body)
except ValueError:
    posts = []
for p in posts if isinstance(posts, list) else []:
    title = html.unescape(re.sub(r"<[^>]+>", "", (p.get("title") or {}).get("rendered", "")))
    exc = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", (p.get("excerpt") or {}).get("rendered", "")))).strip()
    if flt and not flt.search(title + " " + exc):
        continue
    print(f"  {(p.get('date') or '')[:10]} | {title[:120]} | {p.get('link')}\n      {exc[:260]}")
