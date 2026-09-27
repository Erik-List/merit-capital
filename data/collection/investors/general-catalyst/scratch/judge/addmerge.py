#!/usr/bin/env python3
"""Add identity merges: addmerge.py canonical dup1[,dup2] "reason" [...]"""
import json, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
p = INV / "companies/identity-merges.json"
d = json.load(open(p))
g = d["general-catalyst"]
B = {r["slug"] for r in json.load(open(INV / "companies/base.json"))}
args = sys.argv[1:]
for i in range(0, len(args), 3):
    can, dups, why = args[i], args[i + 1].split(","), args[i + 2]
    for x in [can] + dups:
        if x not in B:
            sys.exit(f"not in base: {x}")
    ex = next((m for m in g["merges"] if m["canonical"] == can), None)
    if ex:
        ex["duplicates"] = sorted(set(ex["duplicates"]) | set(dups))
        ex["reason"] += "; " + why
    else:
        g["merges"].append({"canonical": can, "duplicates": dups, "reason": why})
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
print(len(g["merges"]), "merge groups")
