#!/usr/bin/env python3
"""One more Google News surface per row: '"<company>" (TCV OR "Technology Crossover")'.
(adapted from ICONIQ's and Coatue's emit.py for TCV, PRO-169; no TCV surface carries a stage label, so
"TCV" since; the standard surfaces' firm query carries one spelling only. (Adapted from
ICONIQ's news-iconiq.py, PRO-169.)
Uses graduation-surfaces.py's own googlenews() (paced machine-wide, uncapped,
no WebSearch budget). Writes scratch/news-tcv.json {slug: {query, items}};
emit.py reads it beside graduation-surfaces.json for headline needles.
Usage: python3 .../scratch/news-tcv.py [slug ...]
"""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts/graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
sys.argv_saved = sys.argv
spec.loader.exec_module(gs)
DEST = HERE / "news-tcv.json"


def main():
    base = json.load(open(HERE.parent / "companies/base.json"))
    rows = base if isinstance(base, list) else list(base.values())
    want = set(sys.argv[1:])
    cache = json.loads(DEST.read_text()) if DEST.exists() else {}
    todo = [r for r in rows if (not want or r["slug"] in want) and r["slug"] not in cache and r.get("tier") == "A"]
    print(f"{len(todo)} rows to query", flush=True)
    for i, r in enumerate(todo):
        name = gs.clean_name(r["name"])
        res = gs.googlenews(f'"{name}" (TCV OR "Technology Crossover")', name)
        if res.get("status") != "ok":
            print(f"  {r['slug']}: FAILED {res.get('http')}", flush=True)
            continue
        cache[r["slug"]] = {"query": res["query"], "items": res["items"]}
        if i % 20 == 0:
            DEST.write_text(json.dumps(cache, indent=1))
            print(f"  {i}/{len(todo)}", flush=True)
    DEST.write_text(json.dumps(cache, indent=1))
    print("done", len(cache), flush=True)


if __name__ == "__main__":
    main()
