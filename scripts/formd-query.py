#!/usr/bin/env python3
"""Sweep SEC Form D bulk datasets for related persons matching the partner roster.

Streams RELATEDPERSONS.tsv + ISSUERS.tsv + OFFERING.tsv directly from the
quarterly ZIPs in data/filings/form-d/ (no extraction, no dependencies).

Targets come from the investor's partner roster
(sources/wayback/partner-roster.json, written by partner-roster.py): each
roster name yields a (surname, given-name) pair, matched case-insensitively
on (last, first-prefix), so "Roelof Botha" matches "Botha Roelof F." style
variants.

Output: sources/edgar/formd-sweep.json  (accession -> issuer + offering + persons)

Usage: python3 scripts/formd-query.py <investor-slug> [--out PATH]
"""
import argparse
import csv
import io
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT, Paths, write_atomic  # noqa: E402
from people_common import DISTINCT_DESPITE_PREFIX, canon_first  # noqa: E402

DATA_DIR = ROOT / "data" / "filings" / "form-d"


def norm(s: str) -> str:
    return " ".join(s.upper().replace(".", " ").split())


def split_initial(first: str) -> tuple[str, str]:
    """(leading initial, given name) of a normalised first-name field. A
    partner who files as an initial and a middle name goes by the middle
    name: Sandy Miller files as "J. SANFORD MILLER", so the name compared is
    SANFORD, not "J SANFORD" (IVP; also R. Thomas Dyal, T. Peter Thomas,
    L. James Strand). Anything else is compared whole, as before."""
    toks = first.split()
    if len(toks) >= 2 and len(toks[0]) == 1:
        return toks[0], " ".join(toks[1:])
    return "", first


def roster_targets(p: Paths) -> list[tuple[str, str, str]]:
    """(surname, given, leading initial) per roster person; single-token
    names carry no surname+given pair and cannot be swept. A roster name that
    leads with an initial ("J. Sanford Miller") is keyed on the name after it."""
    roster_path = p.wayback / "partner-roster.json"
    if not roster_path.exists():
        sys.exit(f"no roster at {roster_path.relative_to(ROOT)} — run "
                 f"scripts/partner-roster.py first")
    targets = []
    for r in json.load(open(roster_path)):
        toks = [norm(t) for t in r["name"].split()]
        toks = [t for t in toks if t]
        if len(toks) >= 3 and len(toks[0]) == 1:
            targets.append((toks[-1], toks[1], toks[0]))
        elif len(toks) >= 2:
            targets.append((toks[-1], toks[0], ""))
    return targets


def is_match(first: str, last: str, target: tuple[str, str, str]) -> bool:
    """Surname equality plus a >=3-char given-name prefix, on the given names
    actually compared.

    An unbounded prefix test made a single filed initial match any partner
    sharing the letter: Intuit's CFO "R. Neil Williams" matched partner
    "Reggie Williams" and pulled Intuit into the base as a portfolio company.
    One initial is not an attribution. The feminine-variant guard mirrors
    people_common: the prefix rule matched Axcient founder "Justin Moore" to
    partner "Justine Moore" (Sequoia's Joseph/Josephine class). When both
    sides lead with an initial, the initials must agree."""
    tl, tf, ti = target
    if last != tl:
        return False
    fi, given = split_initial(first)
    if fi and ti and fi != ti:
        return False
    fa, fb = canon_first(given.lower()), canon_first(tf.lower())
    pair = tuple(sorted((fa, fb), key=len))
    return (len(given) >= 3 and len(tf) >= 3 and (fa.startswith(fb) or fb.startswith(fa))
            and pair not in DISTINCT_DESPITE_PREFIX)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    ap.add_argument("--out", help="write the sweep here instead of sources/edgar/")
    args = ap.parse_args()

    p = Paths(args.investor)
    targets = roster_targets(p)
    print(f"targets: {len(targets)} roster names", file=sys.stderr)

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
                    for target in targets:
                        if is_match(first, last, target):
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

    dest = Path(args.out) if args.out else p.edgar / "formd-sweep.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(dest, json.dumps(results, indent=2) + "\n")
    print(f"wrote {dest}", file=sys.stderr)
    print(f"# accessions matched: {len(matches)}", file=sys.stderr)
    issuers = {r.get("issuer") for r in results.values()}
    print(f"# distinct issuers: {len(issuers)}", file=sys.stderr)


if __name__ == "__main__":
    main()
