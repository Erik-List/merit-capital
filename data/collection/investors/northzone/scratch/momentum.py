#!/usr/bin/env python3
"""Momentum slice (COLLECTION.md s6): one headline check per private row first seen from 2021 in a hot
sector, for a priced round at $1B+ the judge's knowledge may predate. Output scratch/momentum.json with
the query, the date and what it showed, so every below-$1B claim in the slice carries a dated check."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
rows = [l.split("\t") for l in open(argv[0]).read().splitlines() if l.strip()]
out = json.loads((H / "momentum.json").read_text()) if (H / "momentum.json").exists() else {}
for slug, name in rows:
    if out.get(slug, {}).get("status") == "ok":
        continue
    q = f'"{name.replace(", Inc.", "")}" valuation OR billion OR unicorn OR raises'
    r = gs.googlenews(q, name.replace(", Inc.", ""))
    if r["status"] != "ok":
        out[slug] = {"status": "failed"}; continue
    hits = [i for i in r["items"] if i["names"] and re.search(r"(?i)billion|\$\d(\.\d)?b\b|unicorn|valuation|valued", i["title"])]
    out[slug] = {"status": "ok", "asof": "2026-09-29", "query": q, "n": r["n"],
                 "hits": [{"date": i["date"], "title": i["title"][:200], "gid": i["gid"]} for i in hits[:8]]}
    (H / "momentum.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(slug, len(hits), "|", " ; ".join(f"{h['date']} {h['title'][:90]}" for h in out[slug]["hits"][:3]), flush=True)
