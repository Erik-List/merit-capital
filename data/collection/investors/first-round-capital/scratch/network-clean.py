#!/usr/bin/env python3
"""Trim the company strings the network-directory pull captured.

The profile pages run "<Name> <Role> at <Company> Twitter LinkedIn <bio>",
and the first pass' regex kept the trailing social links and bio. This cuts
each company at the first stop word, in place and idempotently.
"""
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
p = INV / "sources/web/network-directory.json"
d = json.loads(p.read_text())
STOP = re.compile(r"\s+(Twitter|LinkedIn|Previous|Facebook|Website|Blog|Github|Angellist)\b|\.\s|\s+(is|was|has|leads|led|joined|serves|co-founded|founded)\s+", re.I)
n = 0
for k, v in d.items():
    c = v.get("company")
    if not c:
        continue
    m = STOP.search(c)
    if m:
        c = c[:m.start()]
    c = c.strip(" ,.;:-—")
    if c != v["company"]:
        v["company"] = c or None
        n += 1
p.write_text(json.dumps(d, indent=1, sort_keys=True) + "\n")
print(f"cleaned {n} company strings of {len(d)} profiles")
