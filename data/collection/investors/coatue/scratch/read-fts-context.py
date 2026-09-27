#!/usr/bin/env python3
"""Recall probe helper: print the passage around 'Coatue' in the filings of named full-text registrants."""
import importlib.util, json, re, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]; INV = ROOT / "data/collection/investors/coatue"
spec = importlib.util.spec_from_file_location("fts", ROOT / "scripts/edgar-fts-sweep.py"); m = importlib.util.module_from_spec(spec); sys.argv = [sys.argv[0]] + sys.argv[1:]; spec.loader.exec_module(m)
F = json.load(open(INV / "sources/edgar/fts-hits.json"))["registrants"]
want = [w.lower() for w in sys.argv[1:]]
out = {}
for r in F:
    if not any(w in r["registrant"].lower() for w in want): continue
    seen = set(); shown = 0
    for f in r["filings"]:
        if f["url"] in seen or shown >= int(__import__("os").environ.get("NF","2")): continue
        seen.add(f["url"])
        try: b = m.get(f["url"])
        except Exception as e: print(r["registrant"], f["form"], "fetch failed", e); continue
        t = m.strip_html(b) if not f["url"].endswith(".xml") else re.sub(r"<[^>]+>", " ", b.decode("utf-8", "replace") if isinstance(b, bytes) else b)
        if isinstance(t, bytes): t = t.decode("utf-8", "replace")
        t = re.sub(r"\s+", " ", t)
        hits = [x.start() for x in re.finditer(r"Coatue", t)]
        if not hits: continue
        shown += 1
        print(f"\n### {r['registrant']} | {f['form']} {f['date']} | {len(hits)} mentions | {f['url']}")
        last = -1000
        for h in hits[:int(__import__("os").environ.get("NH","40"))]:
            if h - last < 500: continue
            last = h; print("   >", t[max(0, h - 260):h + 300])
            if sum(1 for _ in [0]) and hits.index(h) > 12: break
        time.sleep(0.3)
