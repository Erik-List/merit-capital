#!/usr/bin/env python3
"""Form D related-persons sweep keyed on the FIRM'S OFFICE ADDRESS and the
person's ROLE, not on a roster name (PRO-77's role question).

formd-query.py matches related persons by (surname, given name) against the
partner roster and keeps only RELATIONSHIP_1. Sutter Hill's partners sit on
issuers' filings as directors and, at the firm's incubations, as executive
officers and promoters, and they usually give the firm's own street address
(755 Page Mill Road) as their business address. So this sweep reads EVERY
related person whose street address is one of the firm's offices, with all
three relationship slots and the clarification text, and resolves issuer and
offering per accession.

Output: sources/edgar/formd-address-sweep.json
  accession -> {issuer, cik, city, state, year_of_inc, date_of_first_sale,
                total_offering, total_sold, industry_group, is_pooled, filed,
                persons: [{person, roles[], clarification, street, city}]}

Usage: python3 scratch/formd-address-sweep.py
"""
import csv
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("sutter-hill-ventures")
DATA = ROOT / "data" / "filings" / "form-d"

# The firm's offices over time (ADV Item 1.F; archived contact pages).
ADDRESS_RES = [re.compile(r"\b755\s+PAGE\s+MILL\b", re.I)]


def norm(s):
    return " ".join((s or "").upper().replace(".", " ").split())


def main():
    hits = {}
    for z in sorted(DATA.glob("*.zip")):
        with zipfile.ZipFile(z) as zf:
            rp = next((n for n in zf.namelist() if n.upper().endswith("RELATEDPERSONS.TSV")), None)
            if not rp:
                continue
            with zf.open(rp) as f:
                for row in csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t"):
                    street = f"{row.get('STREET1') or ''} {row.get('STREET2') or ''}"
                    if not any(r.search(street) for r in ADDRESS_RES):
                        continue
                    acc = row["ACCESSIONNUMBER"]
                    roles = [row.get(k) for k in ("RELATIONSHIP_1", "RELATIONSHIP_2", "RELATIONSHIP_3") if row.get(k)]
                    hits.setdefault(acc, {"persons": [], "quarter": z.stem})["persons"].append({
                        "person": norm(f"{row.get('FIRSTNAME')} {row.get('MIDDLENAME') or ''} {row.get('LASTNAME')}"),
                        "last": norm(row.get("LASTNAME")), "first": norm(row.get("FIRSTNAME")),
                        "roles": roles,
                        "clarification": row.get("RELATIONSHIPCLARIFICATION") or "",
                        "street": " ".join(street.split()), "city": row.get("CITY") or "",
                    })
    for z in sorted(DATA.glob("*.zip")):
        with zipfile.ZipFile(z) as zf:
            for kind in ("ISSUERS.TSV", "OFFERING.TSV", "FORMDSUBMISSION.TSV"):
                name = next((n for n in zf.namelist() if n.upper().endswith(kind)), None)
                if not name:
                    continue
                with zf.open(name) as f:
                    for row in csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t"):
                        acc = row.get("ACCESSIONNUMBER")
                        if acc not in hits:
                            continue
                        r = hits[acc]
                        if kind == "ISSUERS.TSV":
                            if row.get("IS_PRIMARYISSUER_FLAG", "YES") in ("YES", "Y", "true", "") or "issuer" not in r:
                                r.setdefault("co_issuers", []).append(row.get("ENTITYNAME"))
                                if "issuer" not in r or row.get("IS_PRIMARYISSUER_FLAG") == "YES":
                                    r["issuer"] = row.get("ENTITYNAME")
                                    r["cik"] = str(int(row.get("CIK") or 0))
                                    r["city"] = row.get("CITY")
                                    r["state"] = row.get("STATEORCOUNTRY")
                                    r["street"] = row.get("STREET1")
                                    r["year_of_inc"] = row.get("YEAROFINC_VALUE_ENTERED") or row.get("YEAROFINC_TIMESPAN_CHOICE")
                                    r["entity_type"] = row.get("ENTITYTYPE")
                        elif kind == "OFFERING.TSV":
                            r["date_of_first_sale"] = row.get("DATEOFFIRSTSALE") or row.get("SALE_DATE")
                            r["total_offering"] = row.get("TOTALOFFERINGAMOUNT")
                            r["total_sold"] = row.get("TOTALAMOUNTSOLD")
                            r["industry_group"] = row.get("INDUSTRYGROUPTYPE")
                            r["is_pooled"] = (row.get("ISPOOLEDINVESTMENTFUNDTYPE") == "true") or bool(row.get("INVESTMENTFUNDTYPE"))
                            r["fund_type"] = row.get("INVESTMENTFUNDTYPE") or None
                            r["equity"] = row.get("ISEQUITYTYPE")
                        else:
                            r["filed"] = row.get("FILING_DATE")
                            r["form"] = row.get("SUBMISSIONTYPE")
    dest = P.edgar / "formd-address-sweep.json"
    write_atomic(dest, json.dumps(hits, indent=1, sort_keys=True) + "\n")
    issuers = {}
    for acc, r in hits.items():
        issuers.setdefault(r.get("cik"), set()).add(r.get("issuer"))
    print(f"accessions: {len(hits)}  issuers (cik): {len(issuers)}", file=sys.stderr)


if __name__ == "__main__":
    main()
