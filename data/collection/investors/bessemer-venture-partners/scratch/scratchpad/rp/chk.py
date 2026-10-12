#!/usr/bin/env python3
"""chk.py: names on stdin (one per line or comma separated) -> prints MISSING ones and loose hits."""
import json, sys, re
from pathlib import Path
b = json.load(open(Path(__file__).resolve().parents[3] / "companies" / "base.json"))
def norm(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
idx = [(norm(r["name"]), norm(r["slug"]), r["slug"], r["name"]) for r in b]
names = [n.strip() for n in re.split(r"[\n,;]", sys.stdin.read()) if n.strip()]
miss = []; found = 0
for n in names:
    k = norm(n)
    ex = [s for a, c, s, nm in idx if a == k or c == k]
    if ex: found += 1; continue
    loose = [(s, nm) for a, c, s, nm in idx if (k in a or (len(a) > 4 and a in k))][:5]
    miss.append((n, loose))
print(f"{len(names)} names, {found} exact in base, {len(miss)} not exact:")
for n, l in miss: print("  ", n, "->", l)
