#!/usr/bin/env python3
"""edidx.py <cik> [form-substr ...]: list a registrant's filings (form, date, primary doc URL) from data.sec.gov."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import secget
cik = int(sys.argv[1]); forms = sys.argv[2:] or ["S-1", "424B", "F-1", "SB-2"]
d = json.loads(secget.get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
print(d.get("name"))
sets = [d["filings"]["recent"]]
for f in d["filings"].get("files", []):
    sets.append(json.loads(secget.get("https://data.sec.gov/submissions/" + f["name"])))
for r in sets:
    for form, date, acc, doc in zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"]):
        if any(x in form for x in forms):
            print(form, date, f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc or acc + '.txt'}")
