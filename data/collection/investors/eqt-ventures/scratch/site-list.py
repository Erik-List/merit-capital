#!/usr/bin/env python3
"""The site layer's file_list source (COLLECTION.md s5 ladder step 5 over the
pages' rendered Key Facts, read by crawl-portfolio.py).

A row per eqtgroup.com portfolio page that belongs on this run's desk map
(decisions.md D1-D3):
  desk "ventures"       any EQT Ventures fund in Key Facts (I, II, III; the
                        page renders III as "V3" on one row, Filament)
  desk "growth"         EQT Growth only (D2: partitioned, preserved)
  desk "unassigned"     no fund named, a 2026 technology entry written up by
                        the Ventures partners (Ineffable Intelligence) or named
                        by them (Starcloud): the judge rules the desk
Every other strategy's page (private equity, infrastructure, BPEA, EQT Life
Sciences, EQT Future, the EQT Foundation, credit) is not a candidate for this
base and stays in eqtgroup-portfolio-pages.json as reference only (D3).

Output: ../sources/site/companies-eqtgroup.json
"""
import json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
SRC = HERE.parent / "sources/site/eqtgroup-portfolio-pages.json"
OUT = HERE.parent / "sources/site/companies-eqtgroup.json"
VENT = {"EQT Ventures I": "EQT Ventures", "EQT Ventures II": "EQT Ventures II",
        "EQT Ventures III": "EQT Ventures III", "V3": "EQT Ventures III", "Ventures III": "EQT Ventures III"}
UNASSIGNED = {"ineffable-intelligence", "starcloud"}
rows = []
for r in json.loads(SRC.read_text())["rows"]:
    funds = r["funds"]
    vent = [VENT[f] for f in funds if f in VENT]
    if vent:
        desk = "ventures"
    elif "EQT Growth" in funds:
        desk = "growth"
    elif r["slug"] in UNASSIGNED:
        desk = "unassigned"
    else:
        continue
    rows.append({
        "name": r["name"], "url": r["url"], "site_id": r["slug"], "desk": desk,
        "funds": funds, "ventures_funds": vent, "invest_year": r["entry_year"],
        "exit_year": r["exit_year"], "status_site": "exited" if (r["exit_year"] or r["page_kind"] == "former") else "current",
        "country_site": r["country"], "sectors": [r["sector"]] if r["sector"] else [],
        "website": r["website"], "tagline": r["tagline"], "description": r["description"],
        "advisors": r["advisors"],
    })
write_atomic(OUT, json.dumps({"_readme": __doc__, "read": json.loads(SRC.read_text())["read"], "rows": rows},
                             indent=1, ensure_ascii=False))
from collections import Counter
print(len(rows), Counter(x["desk"] for x in rows))
