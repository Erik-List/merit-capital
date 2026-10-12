import json, sys, re
from pathlib import Path
INV = Path("/Users/erik/Developer/merit-capital/data/collection/investors")
pk = json.load(open("evidence-pack.json"))
cache = {}
def load(inv):
    if inv not in cache:
        c = {}
        for fn in ("classification.json",):
            p = INV / inv / "companies" / fn
            if p.exists():
                d = json.load(open(p))
                c.update(d if isinstance(d, dict) else {})
        b = {}
        p = INV / inv / "companies" / "base.json"
        if p.exists():
            for r in json.load(open(p)):
                b[r["slug"]] = r.get("name")
        cache[inv] = (c, b)
    return cache[inv]
for s in sys.argv[1:]:
    for sb in pk.get(s, {}).get("siblings", []):
        c, b = load(sb["investor"])
        slugs = [k for k, n in b.items() if (n or "").lower() == sb["name"].lower()]
        for k in slugs:
            r = c.get(k, {})
            keep = {kk: v for kk, v in r.items() if any(kk.startswith(p) for p in ("status", "valuation", "hq_", "entry", "note", "funding"))}
            print(f"== {s} <- {sb['investor']}/{k}: {json.dumps(keep)[:1800]}")
