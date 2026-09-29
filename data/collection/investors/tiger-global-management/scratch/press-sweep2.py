#!/usr/bin/env python3
"""Press sweep (PRO-167): every Google News headline naming Tiger Global, 2003 to 2026.

The firm publishes no portfolio list (decisions.md D9), so the press is a primary
layer here, as on Thrive: each company a headline ties to the firm becomes a candidate
row, cited to the publisher's page. The RSS answers at most ~100 items per query, so
the windows narrow where the firm was busiest (weekly through 2020 to mid-2022, when it
made several hundred investments a year). Variant queries catch headlines the plain
phrase ranks out of a window ("led by Tiger Global", "Tiger Global-backed"), and local
editions catch rounds reported only at home (China, Brazil, Latin America, Russia,
Germany, France, Indonesia, Korea, Japan).

Output: sources/web/press-sweep.json  {query: {status, n, items[], hl, gl}}
Exit 3 while any query failed (re-run: done queries are kept).
"""
import importlib.util, json, sys
from datetime import date, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
sys.argv = sys.argv[:1]
spec.loader.exec_module(gs)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("tiger-global-management")
OUT = P.web / "press-sweep.json"
done = json.loads(OUT.read_text()) if OUT.exists() else {}


def windows(a: date, b: date, days: int):
    d = a
    while d < b:
        e = min(d + timedelta(days=days), b)
        yield d, e
        d = e


queries = []   # (query, hl, gl): SECOND PASS, the windows the first pass found capped at 100
def months(y0, m0, y1, m1):
    y, m = y0, m0
    while (y, m) <= (y1, m1):
        ny, nm = (y + 1, 1) if m == 12 else (y, m + 1)
        yield date(y, m, 1), date(ny, nm, 1)
        y, m = ny, nm
for a, b in months(2020, 7, 2022, 12):
    queries.append((f'"led by Tiger Global" after:{a} before:{b}', "en-US", "US"))
for a, b in months(2021, 1, 2022, 12):
    queries.append((f'"Tiger Global" invests after:{a} before:{b}', "en-US", "US"))
for a, b in months(2026, 1, 2026, 9):
    queries.append((f'"Tiger Global" invests after:{a} before:{b}', "en-US", "US"))
for a, b in months(2014, 1, 2026, 9):
    queries.append((f'"Tiger Global" after:{a} before:{b}', "en-IN", "IN"))
for a, b in months(2020, 1, 2022, 12):
    queries.append((f'"Tiger Global" funding after:{a} before:{b}', "en-IN", "IN"))
for d0, e0 in windows(date(2026, 1, 15), date(2026, 2, 14), 7):
    queries.append((f'"Tiger Global" after:{d0.isoformat()} before:{e0.isoformat()}', "en-US", "US"))

failed = 0
todo = [x for x in queries if done.get(f"{x[0]} | {x[1]}", {}).get("status") != "ok"]
print(f"{len(queries)} queries, {len(todo)} to run", flush=True)
for i, (q, hl, gl) in enumerate(todo):
    key = f"{q} | {hl}"
    r = gs.googlenews(q, "Tiger Global", hl=hl, gl=gl)
    r["hl"], r["gl"] = hl, gl
    done[key] = r
    if r["status"] != "ok":
        failed += 1
    elif i % 20 == 0 or r["n"] >= 95:
        print(f"{i:4d} {r['n']:3d}  {key}", flush=True)
    if i % 10 == 0 or i == len(todo) - 1:
        write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
print(f"{len(done)} queries stored, {failed} failed this pass", file=sys.stderr)
sys.exit(3 if failed else 0)
