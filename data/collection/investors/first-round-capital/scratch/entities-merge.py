#!/usr/bin/env python3
"""Re-inject curated EDGAR entities after edgar-entities.py rebuilds the registry.

edgar-entities.py seeds from EDGAR's company-name search, whose HTML list
parser sees nothing when a query matches exactly one registrant (EDGAR
redirects to that company's filing page). First Round's ownership-filing
entity, FR Capital Holdings, L.P., is exactly that case and carries the whole
Schedule 13G side of the book, so it is curated here and merged back in.

Run after every edgar-entities.py run, before edgar-companies.py:
    python3 data/collection/investors/first-round-capital/scratch/entities-merge.py
"""
import json
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
entities = INV / "entities.json"
curated = INV / "sources/entities-curated.json"

rows = json.loads(entities.read_text())
have = {r["cik"] for r in rows}
added = 0
for c in json.loads(curated.read_text()):
    if c["cik"] in have:
        continue
    rows.append({k: v for k, v in c.items() if k != "basis"})
    added += 1
rows.sort(key=lambda r: (r["desk"], r["name"].lower()))
entities.write_text(json.dumps(rows, indent=1) + "\n")
print(f"entities: {len(rows)} ({added} re-injected from the curated file)")
