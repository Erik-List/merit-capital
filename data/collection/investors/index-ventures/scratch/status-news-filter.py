#!/usr/bin/env python3
"""Reads scratch/status-news-row.json (or -eu) and keeps the headlines in which the company is the one sold, merged or
closed (not the buyer): 'X acquired by', 'acquires X', 'X shuts down', 'X files for bankruptcy'. Leads for the judge."""
import json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
d = json.loads((H / (sys.argv[1] if len(sys.argv) > 1 else "status-news-row.json")).read_text())
n = 0
for s, e in sorted(d.items()):
    nm = re.escape(e["name"])
    pats = [rf"(acquires?|acquiring|buys|to buy|bought|snaps up|scoops up|takes over|acquisition of|takeover of|purchase of|merges with|to acquire)\s+(?:[\w\-\.&']+\s){{0,4}}?{nm}\b",
            rf"\b{nm}\b[^|]{{0,60}}?(acquired by|bought by|to be acquired|sold to|sells to|agrees to be|is being acquired|joins\b|joining\b|shut(s|ting)? down|to shut|closes|closing down|files for bankruptcy|bankrupt|insolven|winds? down|ceas|folds|lays off|to merge|merges)"]
    hits = [h for h in e["hits"] if any(re.search(p, h["title"], re.I) for p in pats)]
    if hits:
        n += 1
        print(f"{s:22s} {e['country']} {e['status']:8s} | " + " || ".join(f"{h['date']} {h['source'][:14]}: {h['title'][:120]}" for h in hits[-3:]))
print(n, "rows with a target-role headline of", len(d))
