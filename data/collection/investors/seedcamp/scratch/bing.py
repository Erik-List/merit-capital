#!/usr/bin/env python3
"""One Bing News RSS query for the judge (Tiger Global's helper, its own shared budget).
Usage: python3 bing.py "query" [name-filter]"""
import importlib.util, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bn", HERE.parents[0] / ".." / "tiger-global-management" / "scratch" / "bing-news.py")
bn = importlib.util.module_from_spec(spec); spec.loader.exec_module(bn)
for q in sys.argv[1:]:
    r = bn.bing(q)
    print("##", q, r.get("status"), r.get("n"))
    for i in sorted(r.get("items", []), key=lambda x: x.get("date") or ""):
        print(" ", (i.get("date") or "")[:10], i["title"][:140], "|", i.get("source"), "|", i["url"][:120])
