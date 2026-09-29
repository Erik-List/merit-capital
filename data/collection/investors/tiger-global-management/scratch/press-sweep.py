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


queries = []   # (query, hl, gl)
spans = [
    (date(2003, 1, 1), date(2013, 1, 1), 91),
    (date(2013, 1, 1), date(2017, 1, 1), 30),
    (date(2017, 1, 1), date(2020, 1, 1), 15),
    (date(2020, 1, 1), date(2022, 7, 1), 7),
    (date(2022, 7, 1), date(2023, 1, 1), 15),
    (date(2023, 1, 1), date(2026, 10, 1), 30),
]
for a, b, n in spans:
    for d, e in windows(a, b, n):
        queries.append((f'"Tiger Global" after:{d.isoformat()} before:{e.isoformat()}', "en-US", "US"))
for y in range(2005, 2027):
    for v in ('"led by Tiger Global"', '"Tiger Global-backed"', '"from Tiger Global"',
              '"Tiger Global Management" funding', '"Tiger Global" invests', '"Tiger Global" stake'):
        queries.append((f'{v} after:{y}-01-01 before:{y + 1}-01-01', "en-US", "US"))
for y in range(2019, 2023):
    for q0, q1 in (("01-01", "04-01"), ("04-01", "07-01"), ("07-01", "10-01"), ("10-01", "12-31")):
        for w in ('"Series A"', '"Series B"', '"Series C"', '"Series D"', 'seed', '"Series E" OR "Series F" OR "Series G"'):
            queries.append((f'"Tiger Global" {w} after:{y}-{q0} before:{y}-{q1}', "en-US", "US"))
# India's press is English and heavy; one extra pass on its edition
for y in range(2008, 2027):
    queries.append((f'"Tiger Global" after:{y}-01-01 before:{y + 1}-01-01', "en-IN", "IN"))
    queries.append((f'"Tiger Global" funding after:{y}-01-01 before:{y + 1}-01-01', "en-IN", "IN"))
LOCAL = [
    ("老虎环球基金", "zh-CN", "CN", range(2008, 2024)),
    ('"Tiger Global" 融资', "zh-CN", "CN", range(2008, 2024)),
    ('"Tiger Global" rodada', "pt-BR", "BR", range(2011, 2025)),
    ('"Tiger Global" investimento', "pt-BR", "BR", range(2011, 2025)),
    ('"Tiger Global" ronda', "es-419", "MX", range(2012, 2025)),
    ('"Tiger Global" раунд', "ru", "RU", range(2008, 2016)),
    ('"Tiger Global" Finanzierungsrunde', "de", "DE", range(2015, 2024)),
    ('"Tiger Global" levée', "fr", "FR", range(2015, 2024)),
    ('"Tiger Global" pendanaan', "id", "ID", range(2014, 2024)),
    ('"Tiger Global" 투자', "ko", "KR", range(2015, 2025)),
    ('"Tiger Global" 資金調達', "ja", "JP", range(2015, 2025)),
    ('"Tiger Global" funding', "en-SG", "SG", range(2012, 2025)),
    ('"Tiger Global" funding', "en-GB", "GB", range(2012, 2025)),
    ('"Tiger Global" funding', "en-IL", "IL", range(2012, 2025)),
    ('"Tiger Global" funding', "en-AU", "AU", range(2014, 2025)),
]
for q, hl, gl, yrs in LOCAL:
    for y in yrs:
        queries.append((f'{q} after:{y}-01-01 before:{y + 1}-01-01', hl, gl))

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
