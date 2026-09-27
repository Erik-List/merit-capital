#!/usr/bin/env python3
"""Google News headlines per base row, for the judge: `"<company>" "Bain Capital Ventures"`
(`"Bain Capital Crypto"` for the crypto list's rows). Headlines name the rounds BCV led and the
exits, dated by the publisher, so the grind reads the entry round and the current state off one
evidence view instead of spending WebSearch calls (200 per session, COLLECTION.md §8 lesson 4).
Reuses scripts/graduation-surfaces.py's googlenews() (the shared googlenews throttle, 1/s) and
decode() for the publisher URL a citation needs. A failed query is recorded as an error and
retried on the next run, never read as "no news" (the absence-vs-failure class).

Output: scratch/news-sweep.json {slug: {"query", "status", "items": [...]}}
Usage: python3 news-sweep.py [--slugs a,b] [--refresh]
"""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

OUT = HERE / "news-sweep.json"
base = json.loads((HERE.parent / "companies" / "base.json").read_text())
crypto = {r["slug"] for r in json.loads((HERE.parent / "sources" / "site" / "crypto-portfolio.json").read_text())["rows"]}
only = set(argv[argv.index("--slugs") + 1].split(",")) if "--slugs" in argv else None
refresh = "--refresh" in argv
cache = json.loads(OUT.read_text()) if OUT.exists() else {}
todo = [r for r in base if (only is None or r["slug"] in only)
        and (refresh or (cache.get(r["slug"]) or {}).get("status") != "ok")]
print(len(todo), "rows to query", flush=True)
for i, r in enumerate(todo):
    name = gs.clean_name(r["name"])
    firm = '"Bain Capital Crypto"' if r["slug"] in crypto else '"Bain Capital Ventures"'
    q = f'"{name}" {firm}'
    res = gs.googlenews(q, name)
    keep = [{k: it[k] for k in ("date", "title", "source", "gid", "names", "rounds", "amounts")}
            for it in res.get("items", [])]
    cache[r["slug"]] = {"query": q, "status": res["status"], "n": res.get("n", 0), "items": keep[-40:]}
    if i % 25 == 24:
        write_atomic(OUT, json.dumps(cache, indent=1, ensure_ascii=False) + "\n")
        print(i + 1, "done", flush=True)
write_atomic(OUT, json.dumps(cache, indent=1, ensure_ascii=False) + "\n")
print("errors:", sum(1 for v in cache.values() if v["status"] != "ok"), "of", len(cache))
