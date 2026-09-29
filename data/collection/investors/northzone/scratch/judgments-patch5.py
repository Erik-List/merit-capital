"""PRO-105 standing duties (2026-09-29 ~23:20 UTC): duty 3 (Fox Technologies' acquired/public came only from a
weak CIK join), and the momentum-slice record (COLLECTION.md s6): each private row first seen from 2021 in a
hot sector carries the dated check, citing the latest round article it rests on (scratch/momentum.json)."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, page = jl.cls, jl.page
H = Path(__file__).resolve().parent
C = json.load(open(H.parent / "companies" / "classification.json")); C = C.get("northzone", C)
M = json.load(open(H / "momentum.json"))
L = [cls("fox-technologies", status="unknown", flags=["model_disputes_source"], extra={"is_public": False},
         note="The pre-filled acquired and the public float came only from a weak CIK join to another 'Fox Technologies' and are quarantined (COLLECTION.md s8 duties 3 and 8); no trace of FoxT's fate in the status search, so unknown")]
for slug, m in M.items():
    if m.get("status") != "ok" or slug not in C:
        continue
    r = C[slug]
    cite = None
    for rd in reversed(r.get("funding_rounds") or []):
        if rd.get("source"):
            cite = rd["source"]; break
    cite = cite or r.get("entry_stage_citation") or page(slug)
    L.append(cls(slug, extra={"valuation_range_source": "web_verified", "valuation_citation": cite, "valuation_asof": "2026-09-29"},
                 note=f"Momentum check 2026-09-29 (Google News: {m['query'][:80]}): no priced round at $1B or more; latest round on record cited"))
jl.write("batch-patch5", L)
