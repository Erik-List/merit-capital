#!/usr/bin/env python3
"""The firm's own fund-vehicle Form D filings, per CIK, for the profile build.

build-firm-profile.py asserts every curated fund entry that carries an accession
against the filed amounts in sources/edgar/fund-formds.json. Nothing writes that
file for a first-time investor, so this pulls it from the EDGAR submissions API
over the home-desk CIKs in entities.json and parses each primary_doc.xml.
"""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import shared_throttle
from paths import Paths, write_atomic
UA = "Merit Capital research erik@meritcapit.al"
P = Paths("redpoint-ventures")

def curl(url):
    shared_throttle.wait("sec")
    r = subprocess.run(["curl", "-sS", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                       capture_output=True, text=True)
    return r.stdout

def field(xml, tag):
    m = re.search(rf"<{tag}>([^<]*)</{tag}>", xml)
    return m.group(1) if m else None

ents = json.load(open(P.root / "entities.json"))
out = {"_readme": {
    "note": ("The firm's own fund-vehicle Form D filings, pulled per-CIK from the EDGAR submissions API by "
             "scratch/own-fund-formds.py over the home-desk (desk == 'us') CIKs in entities.json. "
             "related_persons are the filing's named executive officers and directors — for Redpoint they "
             "are the general partners, and they corroborate the roster. FILING STYLE: Redpoint files a "
             "definite total-offering amount and amends at close, so `total_offering` is the fund's target "
             "size and `sold` is the close state on the filing date."),
    "pulled": "2026-09-06"}}
for e in ents:
    if e.get("desk") != "us":
        continue
    cik = e["cik"].lstrip("0")
    sub = curl(f"https://data.sec.gov/submissions/CIK{e['cik'].zfill(10)}.json")
    try:
        d = json.loads(sub)
    except Exception:
        continue
    rec = d["filings"]["recent"]
    fils = []
    for i, form in enumerate(rec["form"]):
        if form not in ("D", "D/A"):
            continue
        acc = rec["accessionNumber"][i]
        xml = curl(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/primary_doc.xml")
        persons = []
        for blk in re.findall(r"<relatedPersonInfo>(.*?)</relatedPersonInfo>", xml, re.S):
            fn, ln = field(blk, "firstName"), field(blk, "lastName")
            rel = ",".join(re.findall(r"<relationship>([^<]*)</relationship>", blk))
            if ln:
                persons.append({"name": " ".join(filter(None, [fn, ln])).strip(), "relationship": rel})
        fils.append({"form": form, "date": rec["filingDate"][i], "accession": acc,
                     "total_offering": field(xml, "totalOfferingAmount"),
                     "sold": field(xml, "totalAmountSold"),
                     "first_sale": field(xml, "dateOfFirstSale"),
                     "related_persons": persons})
    if fils:
        out[d["name"]] = {"cik": e["cik"], "filings": sorted(fils, key=lambda f: f["date"])}
        print(f"{d['name']}: {len(fils)} Form D filings", flush=True)
write_atomic(P.edgar / "fund-formds.json", json.dumps(out, indent=1) + "\n")
print(f"\nwrote fund-formds.json — {len(out)-1} vehicles")
