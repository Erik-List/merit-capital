#!/usr/bin/env python3
"""BCV fund vehicles' Form D totals (latest D or D/A per vehicle) -> scratch/fund-formds.json, for the profile's fund list."""
import json, re, subprocess, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ents = json.loads((HERE.parent / "entities.json").read_text())
UA = "Merit Capital research erik@meritcapit.al"
def get(u):
    time.sleep(0.15)
    return subprocess.run(["curl", "-s", "-A", UA, u], capture_output=True, text=True).stdout
out = []
for e in ents:
    if e.get("vehicle_role") != "fund" or e.get("desk") != "bcv":
        continue
    cik = e["cik"]
    try:
        s = json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
    except Exception:
        continue
    r = s.get("filings", {}).get("recent", {})
    ds = [(r["filingDate"][i], r["accessionNumber"][i], r["form"][i], r["primaryDocument"][i])
          for i in range(len(r.get("form", []))) if r["form"][i] in ("D", "D/A")]
    if not ds:
        out.append({"cik": cik, "name": e["name"], "formd": None}); continue
    ds.sort()
    first = ds[0]; last = ds[-1]
    x = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{last[1].replace('-', '')}/primary_doc.xml")
    g = lambda t: (re.search(f"<{t}>(.*?)</{t}>", x, re.S) or [None, None])[1]
    out.append({"cik": cik, "name": s.get("name"), "first_filed": first[0], "last_filed": last[0], "accession": last[1],
                "total_offering": g("totalOfferingAmount"), "total_sold": g("totalAmountSold"),
                "first_sale": g("dateOfFirstSale") or (re.search(r"<dateOfFirstSale>\s*<value>(.*?)</value>", x) or [None, None])[1],
                "investors": g("totalNumberAlreadyInvested")})
    print(json.dumps(out[-1]))
(HERE / "fund-formds.json").write_text(json.dumps(out, indent=1) + "\n")
