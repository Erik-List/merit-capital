#!/usr/bin/env python3
"""Cross-investor alignment, 2026-09-21 (PRO-121 pre-wave; COLLECTION.md §10 rule 10).

Before the 13-book re-ingest, every book was compared with every other on the
merged view with verify's in-flight skip turned off: 63 pairs disagreed on
status or valuation band. Each pair was judged on fetched evidence (five
read-only research passes, the largest claims re-checked by hand): 29 are
namesakes and are ruled `distinct` in data/collection/cross-investor.json;
the rest are one company with a stale side, aligned here. Several namesake
pairs also carried a defect on one side, most often a Wikidata join on a
single-token name that left an unrelated entity's date (1919, 1927, 1945,
1949, 1966, 2003) or status on the row; those rows are corrected too.

The judged values, citations and reasons live in the sibling
2026-09-21-pro121.json. Three rows are HELD there for Erik's ruling (a team
hire the buyer says is not an acquisition: Clockwise, Styra) and are not
emitted.

Usage:
  python3 2026-09-21-pro121.py rulings            append the distinct rulings (idempotent)
  python3 2026-09-21-pro121.py emit <investor>... write each book's record batch to
      investors/<slug>/scratch/queue/cross-align-2026-09-21.jsonl, then
      `run.py record --investor <slug> --jsonl <that file>` and re-export.

Wave books (the 13 in public.companies) are emitted only after PRO-132 has
committed that book, so its graduation pass and this batch never race.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INV = ROOT / "data" / "collection" / "investors"
RULINGS = ROOT / "data" / "collection" / "cross-investor.json"
DATA = json.loads(Path(__file__).with_suffix(".json").read_text())
sys.path.insert(0, str(ROOT / "scripts"))
from run import merge_rows, range_of  # noqa: E402

WHO = "cross-investor-align-2026-09-21"
TAG = "cross-investor alignment 2026-09-21, PRO-121"
STALE_BEFORE = "2024-09"          # a private mark older than 24 months is stale (§6)


def record_for(f: dict, cur: dict) -> dict:
    rec = {"slug": f["slug"], "who": WHO, "status": f["status"],
           "note": f"{f['reason']} [{TAG}]"}
    if f["status"] in ("private", "public") and f.get("valuation_usd"):
        rec.update(valuation_usd=f["valuation_usd"], valuation_asof=f["valuation_asof"],
                   valuation_source="web_verified", valuation_citation=f["citation"],
                   valuation_range=range_of(f["valuation_usd"]), valuation_confidence="high")
        assert rec["valuation_range"] == f["valuation_range"], f
        stale = (f["valuation_asof"] or "")[:7] < STALE_BEFORE
        rec["flags"] = ["stale"] if stale else []
        rec["clear_flags"] = ["needs_web_value", "rule_a_below_1b"] + ([] if stale else ["stale"])
        # rule 4: a $1B+ row needs class-1/2 stage evidence or the debt marker
        cited = bool((cur.get("entry_stage_citation") or "").strip()) \
            or cur.get("entry_stage_source") in ("formd_structural", "formd_band")
        if not cited and cur.get("entry_stage") != "undetermined":
            rec["flags"].append("cite_pending")
    else:
        # No standalone figure: acquired / defunct / unknown, or a private row
        # whose only figure or date belonged to a namesake.
        assert f["valuation_range"] == "below_1b" and not f.get("valuation_usd"), f
        rec.update(valuation_usd=None, valuation_asof=None, valuation_source=None,
                   valuation_citation=None, valuation_range="below_1b", is_public=False)
        rec["clear_flags"] = ["stale", "needs_web_value"]
        if cur.get("status") != f["status"]:
            rec["status_citation"] = f["citation"]
    return rec


def emit(investor: str) -> None:
    fixes = DATA["fixes"].get(investor, [])
    if not fixes:
        print(f"{investor}: no records")
        return
    comp = INV / investor / "companies"
    base = json.loads((comp / "base.json").read_text())
    resolved = json.loads((comp / "resolved.json").read_text())
    cls = json.loads((comp / "classification.json").read_text())
    merged = merge_rows(base, resolved, cls)
    slugs = {r["slug"] for r in base}
    out = []
    for f in fixes:
        assert f["slug"] in slugs, f"{investor}: {f['slug']} not in base"
        out.append(record_for(f, merged.get(f["slug"], {})))
    dest = INV / investor / "scratch" / "queue" / "cross-align-2026-09-21.jsonl"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n")
    print(f"{investor}: {len(out)} records -> {dest.relative_to(ROOT)}")


def add_rulings() -> None:
    rul = json.loads(RULINGS.read_text())
    have = {frozenset(e["rows"]) for k in ("distinct", "same", "accepted")
            for e in rul.get(k, [])}
    new = [dict(e, note=f"{e['note']}; 2026-09-21 PRO-121 pre-wave")
           for e in DATA["rulings"] if frozenset(e["rows"]) not in have]
    rul["distinct"].extend(new)
    RULINGS.write_text(json.dumps(rul, indent=1, ensure_ascii=False) + "\n")
    print(f"distinct rulings: {len(new)} added, "
          f"{len(DATA['rulings']) - len(new)} already present")


if __name__ == "__main__":
    if sys.argv[1:2] == ["rulings"]:
        add_rulings()
    elif sys.argv[1:2] == ["emit"] and sys.argv[2:]:
        for inv in sys.argv[2:]:
            emit(inv)
    else:
        sys.exit(__doc__)
