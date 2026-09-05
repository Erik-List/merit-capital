#!/usr/bin/env python3
"""The firm's own fund-vehicle Form D filings (COLLECTION.md §11 funds recipe) from the local
quarterly bulk zips: every accession whose primary issuer CIK is an own-desk entity in
entities.json (funds, principals fund, GP/management LLCs), with offering/sold amounts,
indefinite flag, first-sale date, fund type and co-issuers -> sources/edgar/fund-formds.json
(the shape build-firm-profile.py asserts fund sizes against), plus the related persons named on
those filings -> sources/edgar/fund-related-persons.json (executive officers per vintage: the
filing-grade roster corroboration)."""
import csv, io, json, zipfile, sys
from pathlib import Path
from collections import defaultdict
ROOT = Path("/Users/erik/Developer/merit-capital")
I = ROOT / "data/collection/investors/union-square-ventures"
ents = {e["cik"]: e for e in json.load(open(I / "entities.json")) if e["desk"] == "us"}
own = set(ents)
print("own CIKs", len(own), file=sys.stderr)
acc_iss, acc_all_iss = {}, defaultdict(list)
for zp in sorted((ROOT / "data/filings/form-d").glob("*.zip")):
    with zipfile.ZipFile(zp) as z:
        n = next((x for x in z.namelist() if x.upper().endswith("ISSUERS.TSV")), None)
        if not n: continue
        with z.open(n) as f:
            for row in csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t"):
                cik = str(int(row["CIK"])) if (row.get("CIK") or "").strip().isdigit() else None
                acc = row["ACCESSIONNUMBER"]
                if cik in own:
                    acc_all_iss[acc].append({"cik": cik, "name": row["ENTITYNAME"], "primary": row.get("IS_PRIMARYISSUER_FLAG") == "Y", "city": row.get("CITY"), "state": row.get("STATEORCOUNTRY"), "street": row.get("STREET1"), "year_inc": row.get("YEAROFINC_VALUE_ENTERED"), "quarter": zp.stem})
print("accessions with an own issuer", len(acc_all_iss), file=sys.stderr)
accs = set(acc_all_iss)
sub, off, rel = {}, {}, defaultdict(list)
for zp in sorted((ROOT / "data/filings/form-d").glob("*.zip")):
    with zipfile.ZipFile(zp) as z:
        for kind in ("FORMDSUBMISSION.TSV", "OFFERING.TSV", "RELATEDPERSONS.TSV"):
            n = next((x for x in z.namelist() if x.upper().endswith(kind)), None)
            if not n: continue
            with z.open(n) as f:
                for row in csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t"):
                    acc = row["ACCESSIONNUMBER"]
                    if acc not in accs: continue
                    if kind.startswith("FORMD"): sub[acc] = {"form": row.get("SUBMISSIONTYPE"), "filing_date": row.get("FILING_DATE")}
                    elif kind.startswith("OFFERING"): off[acc] = row
                    else: rel[acc].append({"name": " ".join(x for x in (row.get("FIRSTNAME"), row.get("MIDDLENAME"), row.get("LASTNAME")) if x), "relationships": [r for r in (row.get("RELATIONSHIP_1"), row.get("RELATIONSHIP_2"), row.get("RELATIONSHIP_3")) if r], "city": row.get("CITY"), "street": row.get("STREET1")})
funds = {}
for acc, issuers in acc_all_iss.items():
    prim = next((i for i in issuers if i["primary"]), issuers[0])
    o = off.get(acc, {})
    entry = {"form": sub.get(acc, {}).get("form"), "filing_date": sub.get(acc, {}).get("filing_date"), "accession": acc, "quarter": prim["quarter"],
             "offering": o.get("TOTALOFFERINGAMOUNT"), "sold": o.get("TOTALAMOUNTSOLD"), "indefinite": (o.get("TOTALOFFERINGAMOUNT") or "").lower() == "indefinite",
             "first_sale": o.get("SALE_DATE"), "pooled": o.get("ISPOOLEDINVESTMENTFUNDTYPE") == "true", "fund_type": o.get("INVESTMENTFUNDTYPE") or None,
             "industry_group": o.get("INDUSTRYGROUPTYPE"), "min_investment": o.get("MINIMUMINVESTMENTACCEPTED"), "investors": o.get("TOTALNUMBERALREADYINVESTED"),
             "co_issuers": [i["name"] for i in issuers if not i["primary"]], "issuer_address": f"{prim['street']}, {prim['city']}, {prim['state']}", "related_persons": rel.get(acc, [])}
    funds.setdefault(prim["name"], {"cik": prim["cik"], "filings": []})["filings"].append(entry)
for v in funds.values(): v["filings"].sort(key=lambda e: (e["filing_date"] or "", e["accession"]))
out = {"_readme": {"note": "The firm's own fund-vehicle Form D filings from the local quarterly bulk zips (data/filings/form-d/, 2008q1-2026q2), every accession whose issuer CIK is an own-desk entity of entities.json (funds, Investors parallel vehicles, GP LLCs, Union Square Principals 2004). Built 2026-09-05 by scratch/fund-formds.py. related_persons are the filing's named executive officers/directors/promoters — the filing-grade roster corroboration per vintage.", "built": "2026-09-05"}}
out.update(dict(sorted(funds.items())))
(I / "sources/edgar/fund-formds.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
persons = defaultdict(lambda: {"filings": 0, "funds": set(), "first": "9999", "last": "0000", "relationships": set()})
for name, v in funds.items():
    for e in v["filings"]:
        for p in e["related_persons"]:
            k = p["name"].upper(); q = persons[k]; q["filings"] += 1; q["funds"].add(name); q["relationships"].update(p["relationships"])
            d = e["filing_date"] or ""; q["first"] = min(q["first"], d or "9999"); q["last"] = max(q["last"], d or "0000")
pp = {k: {"filings": v["filings"], "funds": sorted(v["funds"]), "first_filing": v["first"], "last_filing": v["last"], "relationships": sorted(v["relationships"])} for k, v in sorted(persons.items())}
(I / "sources/edgar/fund-related-persons.json").write_text(json.dumps({"_readme": "Related persons named on the firm's own fund Form Ds (from fund-formds.json), aggregated per person: the sworn officer roster by vintage.", "persons": pp}, indent=1, ensure_ascii=False))
print("funds", len(funds), "filings", sum(len(v["filings"]) for v in funds.values()), "persons", len(pp), file=sys.stderr)
for k, v in pp.items(): print(f"  {k:<28} {v['filings']:>3} filings {v['first_filing']}..{v['last_filing']} {v['relationships']}", file=sys.stderr)
for name, v in sorted(funds.items()):
    e = v["filings"][0]
    print(f"  {name:<46} cik {v['cik']:<8} {len(v['filings'])} filings; first {e['filing_date']} offering {e['offering']} sold {e['sold']} indef={e['indefinite']} type={e['fund_type']} co={e['co_issuers']}", file=sys.stderr)
