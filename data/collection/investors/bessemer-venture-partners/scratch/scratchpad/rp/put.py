#!/usr/bin/env python3
"""put.py <section> < json-list : merge items into recall-probe.json (rows keyed by name+source; forge by company; vehicle_decode by vehicle)."""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[2] / "recall-probe.json"
d = json.loads(P.read_text()) if P.exists() else {"rows": [], "forge": [], "vehicle_decode": []}
sec = sys.argv[1]
key = {"rows": lambda r: (r["name"].lower()), "forge": lambda r: r["company"].lower(), "vehicle_decode": lambda r: r["vehicle"].lower()}[sec]
items = json.load(sys.stdin)
have = {key(r): i for i, r in enumerate(d[sec])}
for it in items:
    k = key(it)
    if k in have: d[sec][have[k]] = it
    else: have[k] = len(d[sec]); d[sec].append(it)
P.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
from collections import Counter
print(sec, len(d[sec]), Counter(r.get("decision") for r in d["rows"]))
