#!/usr/bin/env python3
"""Lead's fixes, weak-join audit (COLLECTION.md s8 duty 3; PRO-75, 2026-09-29). Where the SEC or Wikidata join
matched a different company and the judge disputed it, the join's valuation_source and valuation_asof still
published (Mill 'as of 1788-01-01', Courier 2014 from another registrant). Those two keys are cleared on every
such row; rows whose status rode the wrong join get the status stated on their own evidence."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

res = json.loads((jl.INV / "companies/resolved.json").read_text())
cls = json.loads((jl.INV / "companies/classification.json").read_text())
# Weak or wrong joins the judges disputed (the row's own note names the other entity), float or dissolution date
# of that other entity still riding on the row.
WRONG = ["airware", "cacheflow", "cosmos", "courier", "lattice", "sense", "upbound", "flux", "glimpse",
         "desmos", "digit", "favor", "hustle", "sidecar", "mill"]
L = []
for s in WRONG:
    r, c = res.get(s, {}), cls.get(s, {})
    if c.get("valuation_usd"):
        continue
    line = {"slug": s, "who": jl.WHO, "valuation_asof": None, "valuation_source": None}
    if s == "lattice":
        line["status"] = "acquired"
    print(s, "| res:", r.get("valuation_source"), r.get("valuation_asof"), r.get("status"), "| cls status:", c.get("status"))
    L.append(line)
jl.write("fixes-3", L)
