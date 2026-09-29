#!/usr/bin/env python3
"""Every rule-10 (cross-investor) disagreement of GV's merged rows, with both sides' notes and citations, for
adjudication (PRO-75). Reproduces run.py's verify_cross_investor pairing; writes scratch/rule10-pairs.json."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("runpy_", ROOT / "scripts" / "run.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)
R.P = R.Paths("gv")
R.CFG = R.P.config()
R.SAMPLE_SLUGS = set()
INV = "gv"
rows = R.load_base(INV)
cls = R.load(R.P.classification, {})
merged = R.merge_rows(rows, R.load(R.P.resolved, {}), cls)
distinct, accepted, ignore, same = R.load_cross_rulings()
by_key, by_cik, sib_cls = {}, {}, {}
for d in sorted(R.INVESTORS.iterdir()):
    if d.name == INV or d.name in ignore or not d.is_dir() or (d / "scratch" / "in-flight.json").exists():
        continue
    for o in R.published_rows(d.name):
        if o["key"]:
            by_key.setdefault(o["key"], []).append(o)
        for c in o["ciks"]:
            by_cik.setdefault(c, []).append(o)
out, seen = [], set()
for row in rows:
    rec = merged.get(row["slug"], {})
    if not rec.get("status") or rec.get("valuation_range") == R.UNDETERMINED:
        continue
    m = {"id": f"{INV}:{row['slug']}", "name": row["name"], "key": R.cross_key(row["name"]),
         "ciks": R.cross_ciks({**row, "flags": ";".join(rec.get("flags") or [])}),
         "status": rec.get("status"), "valuation_range": rec.get("valuation_range"),
         "valuation_usd": rec.get("valuation_usd"), "valuation_asof": rec.get("valuation_asof") or ""}
    cands = list(by_key.get(m["key"], [])) if m["key"] else []
    for c in m["ciks"]:
        cands += by_cik.get(c, [])
    for o in cands:
        pair = frozenset((m["id"], o["id"]))
        if pair in seen or pair in distinct:
            continue
        seen.add(pair)
        if all(m.get(k) == o.get(k) for k in R.TRACK_RECORD_KEYS) or pair in accepted:
            continue
        sib, sslug = o["id"].split(":", 1)
        if sib not in sib_cls:
            p = R.INVESTORS / sib / "companies" / "classification.json"
            sib_cls[sib] = json.loads(p.read_text()) if p.exists() else {}
        sc = sib_cls[sib].get(sslug) or {}
        out.append({"gv": m["id"], "sib": o["id"], "name": m["name"], "sib_name": o["name"],
                    "gv_side": {k: m[k] for k in ("status", "valuation_range", "valuation_usd", "valuation_asof")},
                    "sib_side": {k: o[k] for k in ("status", "valuation_range", "valuation_usd", "valuation_asof")},
                    "gv_val_cite": rec.get("valuation_citation"), "gv_hq": rec.get("hq_city"),
                    "gv_note": rec.get("note") or "", "sib_note": sc.get("note") or "",
                    "sib_val_cite": sc.get("valuation_citation"), "sib_hq": sc.get("hq_city"),
                    "sib_who": sc.get("who")})
(Path(__file__).parent / "rule10-pairs.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(len(out), "disagreeing pairs")
