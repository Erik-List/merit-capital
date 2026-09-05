#!/usr/bin/env python3
"""Cross-investor alignment, 2026-09-04 (Cherry run; COLLECTION.md §10 invariant 10).

Three rows in the landed Accel and Lightspeed bases sat below_1b with no as-of
while the Cherry run pinned fresher, cited $1B+ marks on the same companies.
The stale side is aligned (freshest cited mark wins). Homonym pairs (Hadrian,
Shift, Integral, Flink) are ruled `distinct` in data/collection/cross-investor.json.
Emits one record batch per investor into investors/<slug>/scratch/queue/
cross-align-2026-09-04-cherry.jsonl; each is recorded with `run.py record`
(the validating gate) and the investor's base.csv re-exported. Rows raised into
a $1B+ band whose entry stage has no class-1/2 evidence get `cite_pending`.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
INV = ROOT / "data" / "collection" / "investors"
WHO = "cross-investor-align-2026-09-04-cherry"
TAG = "Cross-investor alignment 2026-09-04 (Cherry run)"
ROWS = {
 "accel": [
  ("legora", 5550000000, "2026-03-20", "1b_plus", "https://tech.eu/2026/04/23/legora-makes-second-acquisition-in-two-months/", "$550M Series D (Mar 2026) at $5.55B post-money (Tech.eu; Legora newsroom); Cherry's row pins the same mark"),
  ("dash0", 1000000000, "2026-03-25", "1b_plus", "https://www.dash0.com/blog/dash0-raises-usd110m-series-b", "$110M Series B at $1B (Mar 2026, Balderton; Accel and Cherry participating) per Dash0's release"),
 ],
 "lightspeed": [
  ("proxima-fusion", 2743920000, "2026-07-07", "1b_plus", "https://www.proximafusion.com/press-news/proxima-fusion-raises-eu411-million-to-build-europes-commercial-fusion-champion", "EUR 411M round at EUR 2.4B (Jul 2026; Lightspeed among the returning investors) = EUR 2.40B @ ECB 2026-07-07 (EUR/USD 1.1433) = $2.74B"),
 ],
}
for inv, rows in ROWS.items():
    cls = json.loads((INV / inv / "classification.json").read_text())
    lines = []
    for slug, usd, asof, rng, cite, note in rows:
        prev = cls.get(slug, {})
        cited = bool((prev.get("entry_stage_citation") or "").strip()) or prev.get("entry_stage_source") in ("web_verified", "formd_structural")
        rec = {"slug": slug, "who": WHO, "status": "private", "valuation_usd": usd, "valuation_asof": asof,
               "valuation_source": "web_verified", "valuation_range": rng, "valuation_range_source": "web_verified",
               "valuation_citation": cite, "valuation_confidence": "high", "is_public": False,
               "note": " | ".join(filter(None, [prev.get("note"), f"{TAG}: {note}"])), "flags": ([] if cited else ["cite_pending"])}
        rec["clear_flags"] = ["stale", "needs_web_value"]
        lines.append(rec)
    out = INV / inv / "scratch" / "queue" / "cross-align-2026-09-04-cherry.jsonl"
    out.write_text("\n".join(json.dumps(l, ensure_ascii=False) for l in lines) + "\n")
    print(f"{inv}: {len(lines)} alignment records -> {out.relative_to(ROOT)}")
