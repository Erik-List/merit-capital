#!/usr/bin/env python3
"""TechCrunch own-search (WordPress API) through the shared throttle: tc.py "<query>" [more queries]"""
import importlib.util, sys
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("gs", HERE.parents[4] / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
for q in argv:
    svc = ("crunchbase_news", "https://news.crunchbase.com") if q.startswith("cb:") else ("techcrunch", "https://techcrunch.com"); q = q[3:] if q.startswith("cb:") else q; res = gs.wordpress(svc[0], svc[1], q)
    print("==", q, res.get("status"), res.get("n"))
    for i in res.get("items", []):
        print(f"  {i['date']} | {i['title'][:110]} | {i['link']}\n      {i['excerpt'][:230]}")
