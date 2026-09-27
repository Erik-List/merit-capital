#!/usr/bin/env python3
"""Print the round sentences of the firm's posts for the given grid slugs (judge aid)."""
import json, re, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
P = json.load(open(INV / "scratch/posts-by-company.json"))
S = {s["url"]: s for s in json.load(open(INV / "sources/site/stories.json"))["rows"]}
R = re.compile(r"[^.]*\b(seed|series [a-h]|round|led |lead |co-led|co-lead|first invest|incubat|creat|hatch|acqui|majority|valuation|billion)[^.]*\.", re.I)
for slug in sys.argv[1:]:
    for n, p in enumerate(P.get(slug, [])[:3], 1):
        t = S[p["url"]]["text"]
        hits = [m.group(0).strip()[:220] for m in R.finditer(t)][:4]
        print(f"{slug} @{n} {p['date']}: " + " || ".join(hits))
