#!/usr/bin/env python3
"""Rebuild each base company's complete Form D filing history, driven by issuer CIK.

Why this exists separately from `formd-query.py`: that script sweeps the bulk
data for *partner names*, so it only ever sees filings where one of the
investor's partners was a named related person. That is the right driver for
discovering which companies an investor touched, and the wrong one for asking
whether a company raised a later round -- a Series A led by somebody else has no
Sequoia partner on it and is therefore invisible. Used for graduation, the
partner-driven sweep would measure "raised a follow-on the investor also joined".

So this pass inverts the driver. It takes the issuer CIKs already discovered for
base companies and collects *every* filing those issuers ever made, regardless of
who was on it.

The same sweep also extracts issuer-level evidence for the classification run
(formerly scripts/formd-issuer-evidence.py): the entry-time address and
incorporation year at each base accession, plus the full name history of every
base CIK (ENTITYNAME + previous names — the deterministic Square -> Block
rename signal).

Inputs:
  data/aggregation/company-base/<investor>.json     (formd_accessions per row)
  data/aggregation/sources/edgar/formd-sweep.json   (accession -> issuer CIK)
  data/filings/form-d/*.zip                         (74 quarterly bulk datasets)

Outputs:
  data/aggregation/sources/edgar/formd-issuer-rounds.json   (or --out)
  data/aggregation/outcomes/issuer-evidence.json
    {"accessions": {acc: {cik, name, city, state_desc, jurisdiction, year_inc}},
     "ciks": {cik: {"names": [...], "prev_names": [...], "first": ..., "last": ...}}}

Offline: reads only local ZIPs, no network.

Usage:
  python3 scripts/formd-issuer-rounds.py [investor-slug] [--base PATH] [--out PATH]
"""
import argparse
import csv
import io
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORMD_DIR = ROOT / "data" / "filings" / "form-d"
BASE_DIR = ROOT / "data" / "aggregation" / "company-base"
ED = ROOT / "data" / "aggregation" / "sources" / "edgar"
EVIDENCE_OUT = ROOT / "data" / "aggregation" / "outcomes" / "issuer-evidence.json"

# csv defaults to 128 KB; a few RELATEDPERSONS rows carry longer free-text fields.
csv.field_size_limit(10_000_000)


def usd(value: str | None) -> int | None:
    """Form D amounts are free-ish text: '', '0', 'Indefinite', '1,000,000'."""
    if not value:
        return None
    cleaned = re.sub(r"[^0-9]", "", value)
    return int(cleaned) if cleaned else None


def tsv(zf: zipfile.ZipFile, suffix: str):
    """Yield dict rows from the member ending in `suffix`, or nothing if absent."""
    name = next((n for n in zf.namelist() if n.upper().endswith(suffix)), None)
    if not name:
        return
    with zf.open(name) as fh:
        stream = io.TextIOWrapper(fh, encoding="utf-8", errors="replace")
        yield from csv.DictReader(stream, delimiter="\t")


def base_rows(base_path: Path) -> list[dict]:
    """The live Company Base rows. The evidence detail lives in the JSON that
    build-company-base.py writes; the sibling CSV is the merged published
    surface and no longer carries formd_accessions."""
    return json.load(open(base_path))


def target_ciks(rows: list[dict]) -> tuple[dict[str, set[str]], dict[str, str]]:
    """-> (slug -> {cik}, cik -> slug).

    The base stores accessions per company; the sweep maps accession -> CIK. A
    company can legitimately have more than one CIK (re-registration under a new
    entity), so the mapping is kept as a set.
    """
    sweep = json.load(open(ED / "formd-sweep.json"))
    acc_to_cik = {acc: str(int(rec["cik"])) for acc, rec in sweep.items() if rec.get("cik")}

    by_slug: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        for acc in (a.strip() for a in (row.get("formd_accessions") or "").split(";")):
            cik = acc_to_cik.get(acc)
            if cik:
                by_slug[row["slug"]].add(cik)

    cik_to_slug: dict[str, str] = {}
    for slug, ciks in by_slug.items():
        for cik in ciks:
            # A CIK shared by two base rows means the base has a duplicate; the
            # first slug wins and the collision is reported at the end.
            cik_to_slug.setdefault(cik, slug)
    return by_slug, cik_to_slug


def scan(cik_to_slug: dict[str, str],
         wanted_accs: set[str]) -> tuple[dict[str, dict], dict[str, dict]]:
    """One pass over the quarterly ZIPs: every filing by a target CIK (rounds),
    plus the issuer row at each base accession (entry-time evidence)."""
    filings: dict[str, dict] = {}          # accession -> record
    evidence: dict[str, dict] = {}         # accession -> issuer evidence
    collisions: set[str] = set()

    for zpath in sorted(FORMD_DIR.glob("*.zip")):
        quarter = zpath.stem                                  # e.g. "2019q1_d"
        with zipfile.ZipFile(zpath) as zf:
            # ISSUERS first: it decides which accessions in this quarter matter.
            wanted: dict[str, dict] = {}
            for row in tsv(zf, "ISSUERS.TSV"):
                raw = (row.get("CIK") or "").strip()
                if not raw.isdigit():
                    continue
                acc = row["ACCESSIONNUMBER"]
                if acc in wanted_accs and row.get("IS_PRIMARYISSUER_FLAG") != "NO":
                    evidence[acc] = {
                        "cik": raw.lstrip("0"),
                        "name": row.get("ENTITYNAME"),
                        "city": row.get("CITY", ""),
                        "state_desc": row.get("STATEORCOUNTRYDESCRIPTION", ""),
                        "jurisdiction": row.get("JURISDICTIONOFINC", ""),
                        "year_inc": row.get("YEAROFINC_VALUE_ENTERED", ""),
                    }
                cik = str(int(raw))
                slug = cik_to_slug.get(cik)
                if not slug:
                    continue
                prev = wanted.get(acc)
                if prev and prev["slug"] != slug:
                    collisions.add(acc)
                # On a multi-issuer filing prefer the primary issuer's row.
                if prev and prev["is_primary"] and row.get("IS_PRIMARYISSUER_FLAG") != "true":
                    continue
                wanted[acc] = {
                    "slug": slug, "cik": cik,
                    "issuer": row.get("ENTITYNAME"),
                    "city": row.get("CITY"), "state": row.get("STATEORCOUNTRY"),
                    "is_primary": row.get("IS_PRIMARYISSUER_FLAG") == "true",
                }
            if not wanted:
                continue

            for row in tsv(zf, "FORMDSUBMISSION.TSV"):
                rec = wanted.get(row["ACCESSIONNUMBER"])
                if rec is not None:
                    rec["filing_date"] = row.get("FILING_DATE") or None
                    rec["submission_type"] = row.get("SUBMISSIONTYPE") or None

            for row in tsv(zf, "OFFERING.TSV"):
                rec = wanted.get(row["ACCESSIONNUMBER"])
                if rec is None:
                    continue
                rec["sale_date"] = row.get("SALE_DATE") or None
                rec["offering_usd"] = usd(row.get("TOTALOFFERINGAMOUNT"))
                rec["sold_usd"] = usd(row.get("TOTALAMOUNTSOLD"))
                rec["is_amendment"] = row.get("ISAMENDMENT") == "true"
                rec["previous_accession"] = row.get("PREVIOUSACCESSIONNUMBER") or None
                rec["industry"] = row.get("INDUSTRYGROUPTYPE") or None
                rec["is_pooled"] = row.get("ISPOOLEDINVESTMENTFUNDTYPE") == "true"

            for acc, rec in wanted.items():
                rec["quarter"] = quarter
                rec["accession"] = acc
                filings.setdefault(acc, rec)

    if collisions:
        print(f"  note: {len(collisions)} filings name two different base companies "
              f"as issuer (likely base duplicates)")
    return filings, evidence


def name_histories(wanted_ciks: set[str]) -> dict[str, dict]:
    """Second sweep: full name history of every base CIK — ENTITYNAME plus
    ISSUER/EDGAR previous names, the deterministic rename signal
    (Square -> Block class)."""
    ciks: dict[str, dict] = {}
    for zpath in sorted(FORMD_DIR.glob("*.zip")):
        with zipfile.ZipFile(zpath) as zf:
            for row in tsv(zf, "ISSUERS.TSV"):
                cik = (row.get("CIK") or "").lstrip("0")
                if cik not in wanted_ciks:
                    continue
                e = ciks.setdefault(cik, {"names": [], "prev_names": [],
                                          "first": None, "last": None})
                if row["ENTITYNAME"] and row["ENTITYNAME"] not in e["names"]:
                    e["names"].append(row["ENTITYNAME"])
                for k in ("ISSUER_PREVIOUSNAME_1", "ISSUER_PREVIOUSNAME_2",
                          "ISSUER_PREVIOUSNAME_3", "EDGAR_PREVIOUSNAME_1",
                          "EDGAR_PREVIOUSNAME_2", "EDGAR_PREVIOUSNAME_3"):
                    v = (row.get(k) or "").strip()
                    if v and v.upper() != "NONE" and v not in e["prev_names"]:
                        e["prev_names"].append(v)
                acc = row["ACCESSIONNUMBER"]
                e["first"] = min(filter(None, [e["first"], acc]))
                e["last"] = max(filter(None, [e["last"], acc]))
    return ciks


def sort_key(f: dict) -> tuple:
    """Chronological. Filing date is authoritative; quarter is the fallback."""
    return (f.get("filing_date") or "", f.get("quarter") or "", f["accession"])


def collapse_amendments(filings: list[dict]) -> list[dict]:
    """Fold each D/A onto the round it amends, so a round is counted once.

    An amendment revises an existing offering rather than announcing a new one,
    so counting one as a round would inflate both the round count and the
    graduation rate. Amendments frequently revise the offering amount upward, so
    the round keeps the largest figure seen across the original and its
    amendments.
    """
    filings = sorted(filings, key=sort_key)
    rounds: list[dict] = []
    by_accession: dict[str, dict] = {}

    for f in filings:
        parent = None
        if f["is_amendment"]:
            # Prefer the declared parent; fall back to the latest earlier round
            # by the same issuer, since PREVIOUSACCESSIONNUMBER is often blank.
            parent = by_accession.get(f.get("previous_accession") or "")
            if parent is None:
                same_cik = [r for r in rounds if r["cik"] == f["cik"]]
                parent = same_cik[-1] if same_cik else None

        if parent is None:
            rnd = {
                "accession": f["accession"], "cik": f["cik"],
                "quarter": f["quarter"], "filing_date": f.get("filing_date"),
                "sale_date": f.get("sale_date"),
                "offering_usd": f.get("offering_usd"), "sold_usd": f.get("sold_usd"),
                "industry": f.get("industry"), "is_pooled": f.get("is_pooled", False),
                "amendments": 0,
                # every accession folded into this round, original + amendments,
                # so a partner-attributed D/A can still anchor the round
                "accessions": [f["accession"]],
            }
            rounds.append(rnd)
            by_accession[f["accession"]] = rnd
        else:
            parent["amendments"] += 1
            parent["accessions"].append(f["accession"])
            by_accession[f["accession"]] = parent
            for field in ("offering_usd", "sold_usd"):
                new, old = f.get(field), parent.get(field)
                if new is not None and (old is None or new > old):
                    parent[field] = new
            if not parent.get("sale_date") and f.get("sale_date"):
                parent["sale_date"] = f["sale_date"]

    return rounds


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("investor", nargs="?", default="sequoia-capital")
    ap.add_argument("--base", type=Path, help="base JSON (defaults to the live one)")
    ap.add_argument("--out", type=Path, help="output JSON path")
    args = ap.parse_args()

    base_path = args.base or (BASE_DIR / f"{args.investor}.json")
    dest = args.out or (ED / "formd-issuer-rounds.json")

    rows = base_rows(base_path)
    by_slug, cik_to_slug = target_ciks(rows)
    wanted_accs = {a.strip() for r in rows
                   for a in (r.get("formd_accessions") or "").split(";") if a.strip()}
    base_edgar_ciks = {r["edgar_cik"].lstrip("0") for r in rows if r.get("edgar_cik")}
    print(f"base: {base_path.relative_to(ROOT)}")
    print(f"target companies: {len(by_slug)}  distinct issuer CIKs: {len(cik_to_slug)}")
    print(f"scanning {len(list(FORMD_DIR.glob('*.zip')))} quarterly datasets (offline)...")

    filings, ev_accs = scan(cik_to_slug, wanted_accs)
    print(f"filings collected: {len(filings)}")
    print(f"evidence: {len(ev_accs)}/{len(wanted_accs)} base accessions found")

    grouped: dict[str, list[dict]] = defaultdict(list)
    for f in filings.values():
        grouped[f["slug"]].append(f)

    out: dict[str, dict] = {}
    for slug, fs in grouped.items():
        rounds = collapse_amendments(fs)
        out[slug] = {
            "ciks": sorted(by_slug[slug]),
            "round_count": len(rounds),
            "rounds": rounds,
        }

    dest.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(dest, "w"), indent=1)

    # ---- second output: issuer evidence for the classification run
    wanted_ciks = base_edgar_ciks | {v["cik"] for v in ev_accs.values()}
    ciks = name_histories(wanted_ciks)
    renamed = sum(1 for e in ciks.values() if e["prev_names"] or len(e["names"]) > 1)
    json.dump({"accessions": ev_accs, "ciks": ciks}, open(EVIDENCE_OUT, "w"), indent=1)
    print(f"wrote {EVIDENCE_OUT.relative_to(ROOT)} "
          f"({len(ciks)} CIKs, {renamed} with a name history)")

    # ---- what the rescan actually bought, measured rather than asserted
    sweep = json.load(open(ED / "formd-sweep.json"))
    known = set(sweep)
    new_filings = sum(1 for a in filings if a not in known)
    gained = sum(1 for slug, rec in out.items()
                 if any(r["accession"] not in known for r in rec["rounds"]))
    multi = sum(1 for rec in out.values() if rec["round_count"] > 1)
    amended = sum(r["amendments"] for rec in out.values() for r in rec["rounds"])
    dated = sum(1 for rec in out.values() for r in rec["rounds"] if r.get("sale_date"))
    total_rounds = sum(rec["round_count"] for rec in out.values())

    print(f"\nwrote {dest.relative_to(ROOT)}")
    print(f"  companies with Form D history : {len(out)}")
    print(f"  rounds after amendment merge  : {total_rounds} "
          f"({amended} amendments folded in)")
    print(f"  companies with 2+ rounds      : {multi}")
    print(f"  filings the partner sweep never saw: {new_filings}")
    print(f"  companies gaining >=1 such filing  : {gained}")
    print(f"  rounds carrying a sale date   : {dated}/{total_rounds}")


if __name__ == "__main__":
    main()
