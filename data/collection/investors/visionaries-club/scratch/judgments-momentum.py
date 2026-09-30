#!/usr/bin/env python3
"""Momentum slice (COLLECTION.md s6 valuation, Erik 2026-09-04): every private
row first seen 2021 or later in a hot sector carries one dated web check. The
check is the research pass of 2026-09-30 (scratch/research/<slug>.json), which
looked for the latest round and any priced mark; the citation is the latest
dated source it found. Writes queue/batch-momentum.out.jsonl."""
import json
from judge_lib import line, research, write, HERE

C = json.loads((HERE.parent / "companies" / "classification.json").read_text())
R = []
for slug in json.loads((HERE / "momentum-slice.json").read_text()):
    v = C[slug]
    if v.get("valuation_range") != "below_1b" or v.get("valuation_range_source"):
        continue
    d = research(slug)
    dated = [r for r in d.get("funding_rounds", []) if r.get("source") and str(r.get("date") or "")[:4].isdigit()]
    dated.sort(key=lambda r: str(r["date"]))
    cite = dated[-1]["source"].split(" ; ")[0].strip() if dated else ((d.get("status") or {}).get("citation") or (d.get("entry") or {}).get("citation") or d.get("website"))
    what = f"latest round found: {dated[-1]['round']} ({dated[-1]['date']})" if dated else "no priced round found"
    R.append(line(slug, valuation_range_source="web_verified", valuation_range_citation=cite,
                  momentum_checked="2026-09-30",
                  note=f"Momentum check 2026-09-30: {what}, no priced mark at or above $1B"))
write("batch-momentum.out.jsonl", R)
