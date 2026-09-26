#!/usr/bin/env python3
"""Every Companies House appointment of each Balderton partner (the LLP's
designated members), with dates and service addresses: the UK officer graph
(COLLECTION.md s5 country table; Atomico decisions.md D9 precedent). Output:
../sources/registers/companies-house/appointments/<officer_id>.json"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import companies_house as ch
HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "sources" / "registers" / "companies-house" / "appointments"
OUT.mkdir(parents=True, exist_ok=True)
officers = json.load(open(HERE.parent / "sources" / "registers" / "companies-house" / "OC306910-officers.json"))
for o in officers:
    if not o["officer_id"] or o["name"] == "RT146 LIMITED":
        continue
    dest = OUT / f"{o['officer_id']}.json"
    if dest.exists():
        continue
    try:
        d = ch.appointments(o["officer_id"])
    except ch.Unavailable as e:
        print("UNAVAILABLE", o["name"], e); continue
    d["llp_member"] = {"name": o["name"], "appointed": o["appointed"], "resigned": o["resigned"]}
    dest.write_text(json.dumps(d, indent=1, ensure_ascii=False))
    print(o["name"], "|", d.get("total"), "appointments,", len(d["appointments"]), "read")
