#!/usr/bin/env python3
"""Per-row open needs: the queue's asks against the merged view (resolved.json overlaid
with classification.json, over the live base). Read-only.
Usage: python3 .../scratch/open-needs.py [need ...]"""
import json, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
q = json.load(open(INV / "scratch/queue/queue.json"))
res = json.load(open(INV / "companies/resolved.json"))
cl = json.load(open(INV / "companies/classification.json"))
cl = cl.get("rows", cl) if isinstance(cl, dict) and "rows" in cl else cl
led = json.load(open(INV / "companies/membership-ledger.json"))["iconiq-growth"]["verdicts"]
base = {r["slug"] for r in (lambda b: b if isinstance(b, list) else b.values())(json.load(open(INV / "companies/base.json")))}
want = set(sys.argv[1:])
out = {}
for it in q:
    s = it["slug"]
    if s not in base or (led.get(s) or {}).get("verdict") == "not_member":
        continue
    m = dict(res.get(s) or {}); m.update(cl.get(s) or {})
    open_ = []
    for n in it["need"]:
        if n == "membership":
            if s not in led: open_.append(n)
        elif n == "seed_to_a_graduation":
            if m.get("entry_stage") == "Seed" and not m.get("seed_to_a_graduation"): open_.append(n)
            elif not m.get("entry_stage"): open_.append(n)
        elif n == "hq_city":
            if not m.get("hq_city") and "city_unknown" not in (m.get("flags") or []): open_.append(n)
        elif not m.get(n): open_.append(n)
    if open_ and (not want or want & set(open_)):
        out[s] = open_
for s, n in sorted(out.items()):
    print(f"{s:34s} {','.join(n)}")
print(len(out), "rows with open needs")
