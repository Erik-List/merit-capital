#!/usr/bin/env python3
"""The report's numbers from the MERGED view over the live base (COLLECTION.md s8: resolved overlaid with
classification, filtered to base slugs), printed as rows, not only totals (PRO-75)."""
import collections
import json
from pathlib import Path

INV = Path(__file__).resolve().parent.parent
base = json.loads((INV / "companies/base.json").read_text())
cls = json.loads((INV / "companies/classification.json").read_text())
res = json.loads((INV / "companies/resolved.json").read_text())
led = json.loads((INV / "companies/membership-ledger.json").read_text())["gv"]["verdicts"]
cfg = json.loads((INV / "config.json").read_text())
pub = (cfg.get("names") or {}).get("published") or {}
M = {}
for r in base:
    s = r["slug"]
    if (led.get(s) or {}).get("verdict") != "member":
        continue
    m = {**res.get(s, {}), **cls.get(s, {})}
    m["name"] = pub.get(s, r["name"])
    M[s] = m
n = len(M)
print("members", n)
st = collections.Counter(m.get("status") for m in M.values())
print("status", dict(st))
vr = collections.Counter(m.get("valuation_range") for m in M.values())
print("band", dict(vr))
nameable = [m for m in M.values() if m.get("valuation_range") not in (None, "undetermined")]
b1 = [m for m in nameable if m.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus")]
print(f"$1B+ {len(b1)} of {len(nameable)} nameable = {100*len(b1)/len(nameable):.1f}%")
big = sorted([m for m in b1 if (m.get("valuation_usd") or 0) >= 1e10], key=lambda m: -(m.get("valuation_usd") or 0))
print("$10B+:", ", ".join(f"{m['name']} ${m['valuation_usd']/1e9:.1f}B" for m in big))
es = collections.Counter(m.get("entry_stage") for m in M.values())
print("stage", dict(es))
cc = collections.Counter(m.get("hq_country") for m in M.values())
print("country", cc.most_common(25))
fc = collections.Counter(m.get("focus") for m in M.values())
print("focus", fc.most_common())
seed = [m for m in M.values() if m.get("entry_stage") == "Seed"]
g = collections.Counter(m.get("seed_to_a_graduation") for m in seed)
cohort = g.get("graduated", 0) + g.get("not_graduated", 0)
print("S2A seed", len(seed), dict(g), "cohort", cohort,
      f"rate {100*g.get('graduated',0)/cohort:.1f}%" if cohort else "")
nos = collections.Counter(m.get("graduation_source") for m in seed if m.get("seed_to_a_graduation") == "not_graduated")
print("nos rest on", dict(nos))
fl = collections.Counter(f for m in M.values() for f in (m.get("flags") or []))
print("flags", fl.most_common())
cp = [m["name"] for m in M.values() if "cite_pending" in (m.get("flags") or [])]
print("cite_pending:", cp)
city_unknown = sum(1 for m in M.values() if "city_unknown" in (m.get("flags") or []))
print("city filled", sum(1 for m in M.values() if m.get("hq_city")), "unknown flagged", city_unknown)
