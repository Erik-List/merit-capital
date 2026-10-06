#!/usr/bin/env python3
"""Apply the cross-book plans (cross-plan-*.json, CROSS-BRIEF.md) to this investor's own cross-rulings.json:
`distinct` and `accepted` pairs as ruled; `sibling_stale` (and `mixed`) pairs as `accepted` (the sibling is stale,
alignment queued) until the sibling is aligned and re-ingested at the ingest step, when they are removed
(COLLECTION.md s9). Writes one alignment file per sibling book, scratch/align/<book>.jsonl: ONE classification line
per stale row for `run.py record --investor <book>` (several plan entries for one sibling row fold into one line,
the later plan winning a key both give; notes join). Extra lines the lead decided are in align-extra.json."""
import json, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
plan = [p for f in sorted(HERE.glob("cross-plan-*.json")) for p in json.loads(f.read_text())]
out = {"_doc": "Bessemer's rule-10 rulings (PRO-80, 2026-10-06); same schema as data/collection/cross-investor.json.",
       "distinct": [], "accepted": [], "same": []}
align = collections.defaultdict(dict)
seen = set()
for p in plan:
    rows = p["pair"]
    key = frozenset(rows)
    a = p["action"]
    if a == "distinct":
        if key not in seen:
            out["distinct"].append({"rows": rows, "note": p["note"]})
    elif a == "accepted":
        if key not in seen:
            owed = p.get("sibling") or p.get("owed")
            out["accepted"].append({"rows": rows, "note": p["note"] + (" Owed to the sibling once it can be written: " + json.dumps({k: v for k, v in owed.items() if k not in ("book", "slug", "note")}, ensure_ascii=False) if owed else "")})
    elif a in ("sibling_stale", "mixed"):
        if key not in seen:
            out["accepted"].append({"rows": rows, "note": "Sibling stale, alignment queued in scratch/align (removed once the sibling is aligned and re-ingested): " + p["note"]})
        s = dict(p["sibling"]); book = s.pop("book")
        s["who"] = "agent-judge-pro80"
        if s.get("valuation_usd") is not None:
            s.setdefault("valuation_range_source", s.get("valuation_source"))
        cur = align[book].setdefault(s["slug"], {})
        note = cur.get("note")
        cur.update(s)
        if note and s.get("note") and s["note"] not in note and note not in s["note"]:
            cur["note"] = note + " " + s["note"]
    seen.add(key)
extra = HERE / "align-extra.json"
if extra.exists():
    for book, lines in json.loads(extra.read_text()).items():
        for s in lines:
            cur = align[book].setdefault(s["slug"], {})
            note = cur.get("note")
            cur.update(s)
            if note and s.get("note") and s["note"] not in note:
                cur["note"] = note + " " + s["note"]
(HERE.parent / "companies" / "cross-rulings.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
(HERE / "align").mkdir(exist_ok=True)
for f in (HERE / "align").glob("*.jsonl"):
    f.unlink()
for book, rows in align.items():
    (HERE / "align" / f"{book}.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows.values()) + "\n")
print({k: len(v) for k, v in out.items() if isinstance(v, list)}, {b: len(l) for b, l in sorted(align.items())}, sum(len(l) for l in align.values()), "sibling rows")
