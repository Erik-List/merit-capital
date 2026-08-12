#!/usr/bin/env python3
"""Extract issuer-level evidence from the local Form D ZIPs for the outcome run.

Two passes over data/filings/form-d/*.zip ISSUERS.tsv:
  1. rows whose ACCESSIONNUMBER appears in the base's formd_accessions
     -> entry-time address (STATEORCOUNTRYDESCRIPTION), incorporation year
  2. every filing by any CIK seen in pass 1 or carried by the base
     -> full name history (ENTITYNAME + ISSUER/EDGAR_PREVIOUSNAME_*),
        the deterministic rename signal (Square -> Block class)

Output: data/aggregation/outcomes/issuer-evidence.json
  {"accessions": {acc: {cik, name, city, state_desc, jurisdiction, year_inc}},
   "ciks": {cik: {"names": [...], "prev_names": [...], "first": "acc", "last": "acc"}}}
"""
import csv
import io
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIPS = sorted((ROOT / "data" / "filings" / "form-d").glob("*_d*.zip"))
OUT = ROOT / "data" / "aggregation" / "outcomes" / "issuer-evidence.json"
BASE = ROOT / "data" / "aggregation" / "company-base" / "sequoia-capital.csv"


def issuer_rows(zp):
    with zipfile.ZipFile(zp) as z:
        name = next((n for n in z.namelist() if n.endswith("ISSUERS.tsv")), None)
        if not name:
            return
        with z.open(name) as f:
            text = io.TextIOWrapper(f, encoding="utf-8", errors="replace")
            for row in csv.DictReader(text, delimiter="\t"):
                yield row


def main():
    base_path = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE
    wanted_accs, base_ciks = set(), set()
    for r in csv.DictReader(open(base_path)):
        for a in (r.get("formd_accessions") or "").split(";"):
            if a.strip():
                wanted_accs.add(a.strip())
        if r.get("edgar_cik"):
            base_ciks.add(r["edgar_cik"].lstrip("0"))

    accs, ciks = {}, {}
    hits = 0
    for zp in ZIPS:
        for row in issuer_rows(zp):
            acc = row["ACCESSIONNUMBER"]
            if acc in wanted_accs and row.get("IS_PRIMARYISSUER_FLAG") != "NO":
                accs[acc] = {
                    "cik": row["CIK"].lstrip("0"),
                    "name": row["ENTITYNAME"],
                    "city": row.get("CITY", ""),
                    "state_desc": row.get("STATEORCOUNTRYDESCRIPTION", ""),
                    "jurisdiction": row.get("JURISDICTIONOFINC", ""),
                    "year_inc": row.get("YEAROFINC_VALUE_ENTERED", ""),
                }
                hits += 1
    print(f"pass 1: {len(accs)}/{len(wanted_accs)} accessions found ({hits} rows)")

    wanted_ciks = base_ciks | {v["cik"] for v in accs.values()}
    for zp in ZIPS:
        for row in issuer_rows(zp):
            cik = row["CIK"].lstrip("0")
            if cik not in wanted_ciks:
                continue
            e = ciks.setdefault(cik, {"names": [], "prev_names": [], "first": None, "last": None})
            if row["ENTITYNAME"] and row["ENTITYNAME"] not in e["names"]:
                e["names"].append(row["ENTITYNAME"])
            for k in ("ISSUER_PREVIOUSNAME_1", "ISSUER_PREVIOUSNAME_2", "ISSUER_PREVIOUSNAME_3",
                      "EDGAR_PREVIOUSNAME_1", "EDGAR_PREVIOUSNAME_2", "EDGAR_PREVIOUSNAME_3"):
                v = (row.get(k) or "").strip()
                if v and v.upper() != "NONE" and v not in e["prev_names"]:
                    e["prev_names"].append(v)
            acc = row["ACCESSIONNUMBER"]
            e["first"] = min(filter(None, [e["first"], acc]))
            e["last"] = max(filter(None, [e["last"], acc]))
    renamed = sum(1 for e in ciks.values() if e["prev_names"] or len(e["names"]) > 1)
    print(f"pass 2: {len(ciks)} CIKs, {renamed} with a name history")

    json.dump({"accessions": accs, "ciks": ciks}, open(OUT, "w"), indent=1)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
