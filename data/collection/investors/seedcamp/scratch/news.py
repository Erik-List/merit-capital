#!/usr/bin/env python3
"""Google News headline search for the judge (reuses scripts/graduation-surfaces.py,
paced by the shared throttle). Headlines name rounds, leads and exits; `--decode N`
resolves the first N matching items to the publisher's own URL for citation.

Usage: python3 news.py "query" [--name NAME] [--decode N] [--all]
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
sys.argv, argv = sys.argv[:1], sys.argv[1:]
spec.loader.exec_module(gs)

query = argv[0]
name = argv[argv.index("--name") + 1] if "--name" in argv else query.split('"')[1] if '"' in query else query
n_decode = int(argv[argv.index("--decode") + 1]) if "--decode" in argv else 0
show_all = "--all" in argv
picks = [argv[i + 1].lower() for i, a in enumerate(argv) if a == "--pick"]
res = gs.googlenews(query, name)
if res["status"] != "ok":
    print("ERROR", res)
    sys.exit(1)
items = [i for i in res["items"] if show_all or i["names"]]
print(f"{res['n']} items, {len(items)} naming {name!r}")
done = 0
for i in items[-25:]:
    url = ""
    if any(p in i["title"].lower() for p in picks) or (
            done < n_decode and (i["rounds"] or i["amounts"] or "acqui" in i["title"].lower())):
        url = gs.decode(i["gid"]) or ""
        done += 1
    print(f"  {i['date']} | {i['source']} | {i['title'][:150]} {url}")
