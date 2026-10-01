#!/usr/bin/env python3
"""Apply the cross-book plans (cross-plan-*.json, CROSS-BRIEF.md) to this investor's own cross-rulings.json:
`distinct` and `accepted` pairs as ruled; `sibling_stale` pairs as `accepted` (the sibling is stale, alignment queued)
until the sibling is aligned and re-ingested at the ingest step, when they are removed (COLLECTION.md s9). Writes one
alignment file per sibling book, scratch/align/<book>.jsonl, a classification line per stale row for
`run.py record --investor <book>`."""
import json, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
plan = [p for f in sorted(HERE.glob("cross-plan-*.json")) for p in json.loads(f.read_text())]
out = {"_doc": "Kleiner Perkins' rule-10 rulings (PRO-99, 2026-09-30); same schema as data/collection/cross-investor.json.",
       "distinct": [], "accepted": [], "same": []}
align = collections.defaultdict(list)
for p in plan:
    rows = p["pair"]
    if p["action"] == "distinct":
        out["distinct"].append({"rows": rows, "note": p["note"]})
    elif p["action"] == "accepted":
        out["accepted"].append({"rows": rows, "note": p["note"]})
    elif p["action"] == "sibling_stale":
        out["accepted"].append({"rows": rows, "note": "Sibling stale, alignment queued in scratch/align (removed once the sibling is aligned and re-ingested): " + p["note"]})
        s = dict(p["sibling"]); book = s.pop("book")
        s["who"] = "agent-judge-pro99"
        if s.get("valuation_usd") is not None:
            s.setdefault("valuation_range_source", s.get("valuation_source"))
        align[book].append(s)
(HERE.parent / "companies" / "cross-rulings.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
(HERE / "align").mkdir(exist_ok=True)
for book, lines in align.items():
    (HERE / "align" / f"{book}.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
print({k: len(v) for k, v in out.items() if isinstance(v, list)}, {b: len(l) for b, l in sorted(align.items())})
