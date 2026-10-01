#!/usr/bin/env python3
"""Append identity merges / never_merge pairs to ../companies/identity-merges.json (read only at the rebuild).
Usage: python3 add-merges.py '[["canonical", ["dup", ...], "reason", "optional name"], ...]'
       python3 add-merges.py --never '[["slug-a", "slug-b", "reason"], ...]'"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
p = HERE.parent / "companies" / "identity-merges.json"
d = json.loads(p.read_text()); K = d["kleiner-perkins"]
base = {r["slug"] for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
if sys.argv[1] == "--never":
    for a, b, why in json.loads(sys.argv[2]):
        K["never_merge"].append({"slugs": [a, b], "reason": why, "decided": "2026-09-30"})
else:
    for e in json.loads(sys.argv[1]):
        c, dups, why = e[0], e[1], e[2]
        miss = [x for x in [c] + dups if x not in base]
        if miss:
            print("not in base (skipped):", miss)
        dups = [x for x in dups if x in base]
        if c not in base or not dups:
            continue
        ex = next((m for m in K["merges"] if m["canonical"] == c), None)
        if ex:
            ex["duplicates"] = sorted(set(ex["duplicates"]) | set(dups)); ex["reason"] += "; " + why
        else:
            m = {"canonical": c, "duplicates": dups, "reason": why}
            if len(e) > 3 and e[3]:
                m["name"] = e[3]
            K["merges"].append(m)
p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
print(len(K["merges"]), "merges,", len(K["never_merge"]), "never_merge")
