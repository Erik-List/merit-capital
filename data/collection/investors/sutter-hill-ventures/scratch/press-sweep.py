#!/usr/bin/env python3
"""Press sweep: every Google News headline naming Sutter Hill Ventures, in
half-year windows 2004 to 2026 (the RSS answers at most ~100 items a query,
so a window per half year keeps each under the cap), plus round-word queries.

Recall layer for the years the firm's site listed nothing (2017 on) and for
rounds it never posted. Headlines only; the judge decodes the ones it cites.

Output: sources/web/press-sweep.json  {query: {status, n, items[]}}
Exit 3 while any query failed (re-run: done queries are kept).
"""
import importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
sys.argv = sys.argv[:1]
spec.loader.exec_module(gs)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
P = Paths("sutter-hill-ventures")
OUT = P.web / "press-sweep.json"
done = json.loads(OUT.read_text()) if OUT.exists() else {}
queries = []
for y in range(2004, 2027):
    for a, b in (("01-01", "07-01"), ("07-01", "12-31")):
        queries.append(f'"Sutter Hill Ventures" after:{y}-{a} before:{y}-{b}')
queries += ['"Sutter Hill Ventures" led', '"Sutter Hill Ventures" seed', '"Sutter Hill Ventures" "Series A"',
            '"Sutter Hill Ventures" incubated', '"Sutter Hill" incubation', '"Sutter Hill Ventures" backed',
            '"Sutter Hill Ventures" stealth', '"Sutter Hill" Speiser', '"Sutter Hill" Dyckerhoff',
            '"Sutter Hill" Pullara', '"Sutter Hill" "Jeff Bird"', '"Sutter Hill" Rampell',
            '"Sutter Hill" Loebner', '"Sutter Hill" Wroblewski', '"Sutter Hill" Schlampp']
failed = 0
for q in queries:
    if done.get(q, {}).get("status") == "ok":
        continue
    r = gs.googlenews(q, "Sutter Hill")
    done[q] = r
    if r["status"] != "ok":
        failed += 1
    else:
        print(f"{r['n']:3d}  {q}", flush=True)
    write_atomic(OUT, json.dumps(done, indent=1) + "\n")
print(f"{len(done)} queries, {failed} failed", file=sys.stderr)
sys.exit(3 if failed else 0)
