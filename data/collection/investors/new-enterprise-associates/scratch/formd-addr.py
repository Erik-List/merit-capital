#!/usr/bin/env python3
"""Related persons with their street addresses on the Form Ds of given base rows (SEC primary_doc.xml).
python3 formd-addr.py slug ...  -> scratch/formd-addr.json (cached per accession)"""
import json, re, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
base = {r["slug"]: r for r in json.loads((HERE.parent / "companies/base.json").read_text())}
P = HERE / "formd-addr.json"
cache = json.loads(P.read_text()) if P.exists() else {}
UA = "Merit Capital research erik@meritcapit.al"
for s in sys.argv[1:]:
    r = base[s]
    accs = [a for a in (r.get("formd_accessions") or "").split(";") if a.strip()]
    for a in accs:
        a = a.strip()
        if a not in cache:
            cik = str(int(a.split("-")[0]))
            u = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a.replace('-', '')}/primary_doc.xml"
            x = subprocess.run(["curl", "-s", "-A", UA, u], capture_output=True, text=True).stdout
            time.sleep(0.15)
            if "<relatedPersonInfo>" not in x:
                # fall back to the issuer CIK from the base row's formd link
                m = re.search(r"edgar/data/(\d+)/" + a.replace("-", ""), r.get("formd_links") or "")
                if m:
                    u = f"https://www.sec.gov/Archives/edgar/data/{m.group(1)}/{a.replace('-', '')}/primary_doc.xml"
                    x = subprocess.run(["curl", "-s", "-A", UA, u], capture_output=True, text=True).stdout
                    time.sleep(0.15)
            ppl = []
            for blk in re.findall(r"<relatedPersonInfo>(.*?)</relatedPersonInfo>", x, re.S):
                g = lambda t: (re.search(f"<{t}>(.*?)</{t}>", blk, re.S) or [None, ""])[1].strip()
                ppl.append({"name": f"{g('firstName')} {g('lastName')}", "street": g("street1") + " " + g("street2"),
                            "city": g("city"), "rel": re.findall(r"<relationship>(.*?)</relationship>", blk)})
            iss = (re.search(r"<entityName>(.*?)</entityName>", x) or [None, ""])[1]
            cache[a] = {"url": u, "issuer": iss, "persons": ppl}
        c = cache[a]
        print(f"{s} | {a} | {c['issuer']}")
        for p in c["persons"]:
            print(f"     {p['name']:28} | {p['street'][:60]:60} | {p['city']} | {','.join(p['rel'])}")
P.write_text(json.dumps(cache, indent=1) + "\n")
