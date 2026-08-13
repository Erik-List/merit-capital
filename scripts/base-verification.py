#!/usr/bin/env python3
"""Adversarial membership verification for the Company Base (base v2).

The base build unions evidence streams; this layer decides, row by row,
whether each candidate is actually a portfolio company under MEMBERSHIP.md.
Verdicts are durable data in base-verification.json, consumed by
build-company-base.py on every rebuild.

Commands:
  seed     auto-verdict rows whose evidence class is sufficient on its own
           (site listing, fund filing); leave name-match rows for the judge
  prepare  emit judge batches for unverdicted rows (evidence + prior notes)
  record   validate a verdict JSONL and append it to the ledger
  status   coverage counts
  verify   every base row verdicted; no not_member published
"""
import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CB = ROOT / "data" / "aggregation" / "company-base"
OUT = ROOT / "data" / "aggregation" / "outcomes"
LEDGER = CB / "base-verification.json"
QUEUE = OUT / "queue"

VERDICTS = {"member", "not_member", "uncertain"}
EVIDENCE = {"site_listing", "fund_filing", "formd_adjudicated", "knowledge", "web"}
CONF = {"high", "medium", "low"}
BATCH = 50


def load_ledger() -> dict:
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {"sequoia-capital": {"verdicts": {}, "recall_additions": []}}


def save_ledger(led: dict) -> None:
    LEDGER.write_text(json.dumps(led, indent=1, sort_keys=True) + "\n")


def base_rows() -> list[dict]:
    return list(csv.DictReader(open(CB / "sequoia-capital.csv")))


def evidence_class(r: dict) -> str:
    listed = bool(r["site_url"]) or bool(r["wayback_years"])
    filing = bool(r["edgar_forms"])
    formd = bool(r["formd_accessions"]) or bool(r["partners_formd"])
    if listed:
        return "listed"
    if filing:
        return "filing"
    if formd:
        return "formd_only"
    return "none"


def cmd_seed(_a) -> None:
    led = load_ledger()
    v = led["sequoia-capital"]["verdicts"]
    today = date.today().isoformat()
    n = {"listed": 0, "filing": 0, "skipped": 0}
    for r in base_rows():
        if r["slug"] in v:
            continue
        ec = evidence_class(r)
        if ec == "listed":
            v[r["slug"]] = {
                "verdict": "member", "who": "seed-evidence",
                "evidence_class": "site_listing",
                "basis": "Listed on Sequoia's own portfolio site "
                         f"({r['wayback_years'] or 'current site'}).",
                "confidence": "high", "decided": today}
            n["listed"] += 1
        elif ec == "filing":
            v[r["slug"]] = {
                "verdict": "member", "who": "seed-evidence",
                "evidence_class": "fund_filing",
                "basis": f"SEC ownership filing by a fund vehicle "
                         f"(forms {r['edgar_forms']}, CIK {r['edgar_cik']}).",
                "confidence": "high", "decided": today}
            n["filing"] += 1
        else:
            n["skipped"] += 1
    save_ledger(led)
    print(f"seeded: {n['listed']} site_listing, {n['filing']} fund_filing; "
          f"left for the judge: {n['skipped']}")


def cmd_prepare(_a) -> None:
    led = load_ledger()
    v = led["sequoia-capital"]["verdicts"]
    cls = json.loads((OUT / "classification.json").read_text()) \
        if (OUT / "classification.json").exists() else {}
    res = json.loads((OUT / "resolved.json").read_text()) \
        if (OUT / "resolved.json").exists() else {}
    queue = []
    for r in base_rows():
        if r["slug"] in v:
            continue
        m = dict(res.get(r["slug"], {}))
        m.update({k: x for k, x in cls.get(r["slug"], {}).items() if x is not None})
        queue.append({
            "slug": r["slug"], "name": r["name"], "tier": r["tier"],
            "first_seen": r["first_seen"], "sector": r["sector"],
            "partners_formd": r["partners_formd"],
            "formd_span": r["formd_span"],
            "formd_max_round_usd": r["formd_max_round_usd"],
            "outcome_note": (m.get("note") or "")[:220],
            "status": m.get("status"), "value_tag": m.get("value_tag"),
        })
    for f in QUEUE.glob("bv-*.json"):
        f.unlink()
    for i in range(0, len(queue), BATCH):
        (QUEUE / f"bv-{i // BATCH + 1:03d}.json").write_text(
            json.dumps(queue[i:i + BATCH], indent=1))
    print(f"queued {len(queue)} rows in {(len(queue) + BATCH - 1) // BATCH} batches")


def validate(rec: dict, slugs: set[str]) -> list[str]:
    errs = []
    s = rec.get("slug")
    if not s or s not in slugs:
        return [f"slug {s!r} not in base"]
    if rec.get("verdict") not in VERDICTS:
        errs.append(f"{s}: verdict {rec.get('verdict')!r}")
    if rec.get("evidence_class") not in EVIDENCE:
        errs.append(f"{s}: evidence_class {rec.get('evidence_class')!r}")
    if rec.get("confidence") not in CONF:
        errs.append(f"{s}: confidence {rec.get('confidence')!r}")
    if not (rec.get("basis") or "").strip():
        errs.append(f"{s}: empty basis")
    # a member verdict resting on a name-match must say what corroborates it
    if rec.get("verdict") == "member" and rec.get("evidence_class") == "formd_adjudicated" \
            and not rec.get("citation") and rec.get("confidence") == "low":
        errs.append(f"{s}: low-confidence member on a name-match needs a citation")
    return errs


def cmd_record(a) -> None:
    led = load_ledger()
    v = led["sequoia-capital"]["verdicts"]
    slugs = {r["slug"] for r in base_rows()}
    today = date.today().isoformat()
    incoming, errs = {}, []
    for n, line in enumerate(Path(a.jsonl).read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"line {n}: {e}")
            continue
        errs.extend(validate(rec, slugs))
        incoming[rec["slug"]] = rec
    if errs:
        print(f"REJECTED, {len(errs)} problem(s):")
        for e in errs[:20]:
            print("  -", e)
        sys.exit(1)
    for s, rec in incoming.items():
        prev = v.get(s)
        if prev and prev.get("who") == "erik":
            print(f"  kept human verdict on {s}")
            continue
        rec.setdefault("who", "agent-precision-pass")
        rec["decided"] = today
        v[s] = rec
    save_ledger(led)
    print(f"recorded {len(incoming)}; ledger holds {len(v)}")


def cmd_status(_a) -> None:
    led = load_ledger()
    v = led["sequoia-capital"]["verdicts"]
    rows = base_rows()
    from collections import Counter
    c = Counter(v[r["slug"]]["verdict"] if r["slug"] in v else "UNJUDGED"
                for r in rows)
    print(f"base rows {len(rows)}; verdicts {dict(c.most_common())}")
    print(f"recall additions staged: "
          f"{len(led['sequoia-capital'].get('recall_additions', []))}")


def cmd_verify(_a) -> None:
    led = load_ledger()
    v = led["sequoia-capital"]["verdicts"]
    rows = base_rows()
    problems = []
    for r in rows:
        rec = v.get(r["slug"])
        if not rec:
            problems.append(f"{r['slug']}: no verdict")
        elif rec["verdict"] == "not_member":
            problems.append(f"{r['slug']}: published despite not_member")
    unc = [s for s, rec in v.items() if rec["verdict"] == "uncertain"]
    print(f"rows {len(rows)}, verdicts {len(v)}, uncertain {len(unc)}")
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems[:20]:
            print("  -", p)
        sys.exit(1)
    print("base-verification: clean")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("seed", cmd_seed), ("prepare", cmd_prepare),
                     ("status", cmd_status), ("verify", cmd_verify)):
        sub.add_parser(name).set_defaults(fn=fn)
    p = sub.add_parser("record")
    p.add_argument("jsonl")
    p.set_defaults(fn=cmd_record)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
