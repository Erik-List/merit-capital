"""Form D filings of the firm's own deal vehicles, from the local bulk zips.
Writes sources/edgar/spv-formd.json."""
import csv, io, json, sys, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic
CIKS = {"1789009": "Erebor, LP", "1503830": "Lembas III, LP", "1967240": "Mirian, LP",
        "1767476": "Miruvor, LP", "1464202": "Founders Fund SpaceX Fund, LP"}
csv.field_size_limit(10**9)
out = []
for z in sorted((ROOT / "data/filings/form-d").glob("*.zip")):
    with zipfile.ZipFile(z) as zf:
        names = {n.split("/")[-1].upper(): n for n in zf.namelist()}
        def rows(key):
            with zf.open(names[key]) as f:
                yield from csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        acc = {}
        for r in rows("ISSUERS.TSV"):
            c = (r.get("CIK") or "").lstrip("0")
            if c in CIKS:
                acc[r["ACCESSIONNUMBER"]] = {"cik": c, "issuer": r.get("ENTITYNAME"), "quarter": z.stem,
                                             "state": r.get("STATEORCOUNTRY"), "city": r.get("CITY"), "street": r.get("STREET1")}
        if not acc: continue
        for r in rows("FORMDSUBMISSION.TSV"):
            if r["ACCESSIONNUMBER"] in acc:
                acc[r["ACCESSIONNUMBER"]].update(filed=r.get("FILING_DATE"), form=r.get("SUBMISSIONTYPE"))
        for r in rows("OFFERING.TSV"):
            if r["ACCESSIONNUMBER"] in acc:
                acc[r["ACCESSIONNUMBER"]].update(first_sale=r.get("SALE_DATE"), offered=r.get("TOTALOFFERINGAMOUNT"),
                    sold=r.get("TOTALAMOUNTSOLD"), investors=r.get("TOTALNUMBERALREADYINVESTED"),
                    year_inc=r.get("YEAROFINC_VALUE_ENTERED"), fund_type=r.get("INVESTMENTFUNDTYPE"))
        for r in rows("RELATEDPERSONS.TSV"):
            if r["ACCESSIONNUMBER"] in acc:
                acc[r["ACCESSIONNUMBER"]].setdefault("related", []).append(
                    f"{r.get('FIRSTNAME','')} {r.get('LASTNAME','')}".strip())
        for a, v in acc.items():
            out.append({"accession": a, **v})
out.sort(key=lambda r: (r["cik"], r.get("filed") or ""))
dest = ROOT / "data/collection/investors/founders-fund/sources/edgar/spv-formd.json"
write_atomic(dest, json.dumps(out, indent=1) + "\n")
for r in out:
    print(r["issuer"], "|", r.get("form"), r.get("filed"), "| first sale", r.get("first_sale"), "| sold", r.get("sold"), "of", r.get("offered"),
          "| investors", r.get("investors"), "|", "; ".join(r.get("related", [])[:6]))
