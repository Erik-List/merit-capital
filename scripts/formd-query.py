#!/usr/bin/env python3
"""Query SEC Form D bulk datasets for related persons matching investor partners.

Streams RELATEDPERSONS.tsv + ISSUERS.tsv + OFFERING.tsv directly from the
quarterly ZIPs in data/filings/form-d/ (no extraction, no dependencies).

Usage: python3 scripts/formd-query.py "LAST,FIRST" ["LAST,FIRST" ...]
Names are matched case-insensitively on (last, first-prefix), so
"BOTHA,ROELOF" matches "Botha Roelof F." style variants.
"""
import csv
import io
import json
import sys
import zipfile
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "filings" / "form-d"


def norm(s: str) -> str:
    return " ".join(s.upper().replace(".", " ").split())


def main() -> None:
    targets = []  # (last, first)
    for arg in sys.argv[1:]:
        last, _, first = arg.partition(",")
        targets.append((norm(last), norm(first)))
    if not targets:
        sys.exit("usage: formd-query.py 'LAST,FIRST' ...")

    matches = {}  # accession -> list of matched person rows
    for zpath in sorted(DATA_DIR.glob("*.zip")):
        with zipfile.ZipFile(zpath) as z:
            rp_name = next((n for n in z.namelist() if n.upper().endswith("RELATEDPERSONS.TSV")), None)
            if not rp_name:
                continue
            with z.open(rp_name) as f:
                reader = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
                for row in reader:
                    last = norm(row.get("LASTNAME") or "")
                    first = norm(row.get("FIRSTNAME") or "")
                    for tl, tf in targets:
                        if last == tl and (first.startswith(tf) or tf.startswith(first)):
                            acc = row.get("ACCESSIONNUMBER")
                            matches.setdefault(acc, []).append({
                                "person": f"{first} {last}",
                                "relationship": row.get("RELATIONSHIP_1") or row.get("RELATIONSHIP"),
                                "quarter": zpath.stem,
                            })

    # Second pass: resolve issuer + offering info for matched accessions
    results = {}
    for zpath in sorted(DATA_DIR.glob("*.zip")):
        with zipfile.ZipFile(zpath) as z:
            for kind in ("ISSUERS.TSV", "OFFERING.TSV"):
                name = next((n for n in z.namelist() if n.upper().endswith(kind)), None)
                if not name:
                    continue
                with z.open(name) as f:
                    reader = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
                    for row in reader:
                        acc = row.get("ACCESSIONNUMBER")
                        if acc not in matches:
                            continue
                        r = results.setdefault(acc, {"persons": matches[acc]})
                        if kind == "ISSUERS.TSV":
                            r["issuer"] = row.get("ENTITYNAME")
                            r["cik"] = row.get("CIK")
                            r["city"] = row.get("CITY")
                            r["state"] = row.get("STATEORCOUNTRY")
                        else:
                            r["date_of_first_sale"] = row.get("DATEOFFIRSTSALE")
                            r["total_offering"] = row.get("TOTALOFFERINGAMOUNT")
                            r["total_sold"] = row.get("TOTALAMOUNTSOLD")
                            r["industry_group"] = row.get("INDUSTRYGROUPTYPE")
                            r["fund_type"] = row.get("INVESTMENTFUNDTYPE") or None
                            # separate boolean: set by funds that picked a
                            # different industry category (REITs, Investing, ...)
                            r["is_pooled"] = row.get("ISPOOLEDINVESTMENTFUNDTYPE") == "true"

    print(json.dumps(results, indent=2))
    print(f"\n# accessions matched: {len(matches)}", file=sys.stderr)
    issuers = {r.get("issuer") for r in results.values()}
    print(f"# distinct issuers: {len(issuers)}", file=sys.stderr)


if __name__ == "__main__":
    main()
