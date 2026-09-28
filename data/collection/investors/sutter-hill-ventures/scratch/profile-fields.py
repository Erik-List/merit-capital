#!/usr/bin/env python3
"""The profile's base-dependent numbers, read off the MERGED view over the live
base (resolved.json overlaid with classification.json, members only; COLLECTION.md
§8): entry-stage mix, HQ countries, focus counts, status mix, $1B+ rows.
Prints them; the profile writer copies what it uses into investor.json and the
sidecar bases. Usage: python3 scratch/profile-fields.py"""
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths  # noqa: E402

P = Paths("sutter-hill-ventures")
base = {r["slug"]: r for r in json.loads(P.base_json.read_text())}
res = json.loads(P.resolved.read_text())
cl = json.loads(P.classification.read_text())
cl = cl.get("sutter-hill-ventures", cl)
led = json.loads(P.ledger.read_text())["sutter-hill-ventures"]["verdicts"]
rows = {}
for s in base:
    if led.get(s, {}).get("verdict") != "member":
        continue
    rows[s] = {**(res.get(s) or {}), **(cl.get(s) or {})}
n = len(rows)
st = Counter(v.get("entry_stage") for v in rows.values())
co = Counter(v.get("hq_country") for v in rows.values())
fo = Counter(v.get("focus") for v in rows.values())
ss = Counter(v.get("status") for v in rows.values())
big = sorted(((v.get("valuation_usd") or 0, s) for s, v in rows.items()
              if v.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus")), reverse=True)
print(f"members {n}")
print("stage", dict(st))
print("country", dict(co.most_common()))
print("focus", dict(fo.most_common()))
print("status", dict(ss))
print(f"$1B+ {len(big)}:", ", ".join(f"{s} {u/1e9:.1f}B" for u, s in big))
for s in ("nvidia", "snowflake-inc", "activision", "palm-inc", "glassdoor", "pure-storage", "netapp"):
    print("notable check", s, s in rows)
