#!/usr/bin/env python3
"""Triage view of FTS recall candidates: python3 ftsview.py --shard N  (or: ftsview.py "Registrant substring")
Prints each candidate's forms, dates, filing URLs and the stored snippets that name Kleiner Perkins."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
regs = {r["registrant"]: r for r in json.loads((HERE.parent / "sources/edgar/fts-hits.json").read_text())["registrants"]}
cand = json.loads((HERE / "fts-candidates.json").read_text())["rows"]
a = sys.argv[1:]
if a and a[0] == "--shard":
    names = [c["registrant"] for c in cand if c.get("shard") == int(a[1])]
else:
    names = [n for n in regs if a and a[0].lower() in n.lower()]
for n in names:
    r = regs[n]; c = next((x for x in cand if x["registrant"] == n), {})
    print(f"\n### {n} | cik {r['cik']} | {c.get('cls')} | {r['first_date']}..{r.get('last_date')} | {dict(list(r['forms'].items())[:8])}")
    for f in sorted(r.get("filings", []), key=lambda f: f["date"])[:6]:
        print(f"   {f['date']} {f['form']:10} {f['url']}")
    for s in (r.get("snippets") or [])[:3]:
        if isinstance(s, dict):
            print(f"   > {s.get('form')} {s.get('date')}: " + " | ".join(s.get("context") or [])[:700].replace("\n", " "))
