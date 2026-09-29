#!/usr/bin/env python3
"""Find TCV's own posts by keyword: python3 scratch/post.py <word> [word ...] -> slug, first capture, citation URL, and the body's first lines where CC holds it."""
import json, re, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
P = json.load(open(INV / "scratch/tcv-posts.json"))
ws = [w.lower() for w in sys.argv[1:]]
for s, p in sorted(P.items(), key=lambda x: x[1]["ts"]):
    if all(w in s.lower() for w in ws):
        body = INV / "sources/site/news" / (s[:150] + ".txt")
        t = body.read_text() if body.exists() else ""
        m = re.search(r"(?i)(PRNewswire|Business Wire|GLOBE NEWSWIRE|—\s*\(|\d{4}\s*[-–—/]\s*)", t)
        print(p["ts"][:8], s, "\n   ", p["capture"])
        if t:
            i = t.lower().find(ws[0])
            print("   |", t[max(0, i - 100): i + 500].replace("\n", " "))
