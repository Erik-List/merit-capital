#!/usr/bin/env python3
"""Every Form D filed by a TCV-named issuer (TCV / Technology Crossover / TCMI), with its related persons and
offering facts, read from the local bulk zips (offline). The firm publishes no
team page, so the people named on its own fund filings (general partners,
managing members, executive officers), dated per filing, are the roster's
filing-grade backbone (the Thrive and Coatue shape, COLLECTION.md 5).
Output: sources/edgar/formd-own-issuers.json"""
import csv, glob, io, json, re, sys, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "data/collection/investors/tcv/sources/edgar/formd-own-issuers.json"
PAT = re.compile(r"^(tcv\b|technology crossover|tcmi\b)", re.I)
rows = {}
def tsv(z, suffix):
    for n in z.namelist():
        if n.upper().endswith(suffix):
            with z.open(n) as f:
                yield from csv.DictReader(io.TextIOWrapper(f, "utf-8", errors="replace"), delimiter="\t")
for zp in sorted(glob.glob(str(ROOT / "data/filings/form-d/*.zip"))):
    z = zipfile.ZipFile(zp)
    accs = {}
    for r in tsv(z, "ISSUERS.TSV"):
        if PAT.search(r.get("ENTITYNAME", "")):
            accs[r["ACCESSIONNUMBER"]] = {"accession": r["ACCESSIONNUMBER"], "cik": r.get("CIK"), "issuer": r.get("ENTITYNAME"),
                                          "city": r.get("CITY"), "state": r.get("STATEORCOUNTRY"), "year_inc": r.get("YEAROFINC_VALUE_ENTERED"),
                                          "persons": [], "zip": Path(zp).name}
    if not accs: continue
    for r in tsv(z, "FORMDSUBMISSION.TSV"):
        a = r["ACCESSIONNUMBER"]
        if a in accs:
            accs[a].update({"filed": r.get("FILING_DATE"), "form": r.get("SUBMISSIONTYPE")})
    for r in tsv(z, "OFFERING.TSV"):
        a = r["ACCESSIONNUMBER"]
        if a in accs:
            accs[a].update({"industry": r.get("INDUSTRYGROUPTYPE"), "fund_type": r.get("INVESTMENTFUNDTYPE"), "is40act": r.get("IS40ACT"),
                            "sold": r.get("TOTALAMOUNTSOLD"), "offering": r.get("TOTALOFFERINGAMOUNT"), "investors": r.get("TOTALNUMBERALREADYINVESTED"),
                            "first_sale": r.get("SALE_DATE"), "min_inv": r.get("MINIMUMINVESTMENTACCEPTED")})
    for r in tsv(z, "RELATEDPERSONS.TSV"):
        a = r["ACCESSIONNUMBER"]
        if a in accs:
            accs[a]["persons"].append({"first": r.get("FIRSTNAME"), "last": r.get("LASTNAME"), "roles": r.get("RELATIONSHIP"),
                                       "clar": r.get("RELATIONSHIPCLARIFICATION"), "city": r.get("CITY")})
    rows.update(accs)
    print(zp.split('/')[-1], len(accs), file=sys.stderr)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({"_readme": __doc__, "filings": sorted(rows.values(), key=lambda r: (r.get("filed") or "", r["accession"]))}, indent=1))
print("filings", len(rows))
