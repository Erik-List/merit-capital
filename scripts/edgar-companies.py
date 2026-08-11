#!/usr/bin/env python3
"""Collect public-market filing evidence per company, with authoritative roles.

Replaces the full-text-search collector. FTS matched the string "Sequoia Capital"
anywhere in a document, so half its hits were filings that merely mentioned the
firm, and roles had to be guessed from name shape. Here the filing set comes from
the investor's own entity CIKs (submissions API, zero text-mention false
positives) and roles come from each filing's SEC header.

Note the name: this is evidence that a company reached public markets, NOT an
outcome classification. It misses private winners and includes failed IPOs.

Input : data/aggregation/entities/sequoia-capital.json
Output: data/aggregation/sources/edgar/edgar-companies.json
"""
import json
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from edgar_common import fetch_header, parse_header_roles, parse_header_meta  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ENT = ROOT / "data" / "aggregation" / "entities"
OUT = ROOT / "data" / "aggregation" / "sources" / "edgar"
UA = "Merit Capital research erik@meritcapit.al"

OWNERSHIP_FORMS = {"3", "4", "5", "3/A", "4/A", "5/A",
                   "SC 13D", "SC 13G", "SC 13D/A", "SC 13G/A"}

DESK_RANK = ["us-eu", "israel", "india", "china", "unknown"]


def submissions(cik: str) -> dict:
    url = f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"
    for attempt in range(3):
        try:
            out = subprocess.run(
                ["curl", "-sf", "--max-time", "45", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout
            return json.loads(out)
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            time.sleep(1.0 * (attempt + 1))
    return {}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    all_entities = json.load(open(ENT / "sequoia-capital.json"))
    desk_of = {e["cik"]: e["desk"] for e in all_entities}
    # `external` entities are unrelated institutions picked up by co-filer
    # closure. Crawling them would import their whole portfolio as ours.
    entities = [e for e in all_entities if e["desk"] != "external"]
    print(f"registry: {len(all_entities)} entities · {dict(Counter(desk_of.values()))}")
    print(f"crawling {len(entities)} (external excluded)")

    # 1) filer-side filing set, deduped across co-filers
    acc_owner: dict[str, str] = {}   # accession -> a CIK that can serve the archive path
    for i, e in enumerate(entities, 1):
        data = submissions(e["cik"])
        recent = (data.get("filings") or {}).get("recent") or {}
        for acc, form in zip(recent.get("accessionNumber", []), recent.get("form", [])):
            if form in OWNERSHIP_FORMS:
                acc_owner.setdefault(acc, e["cik"])
        if i % 25 == 0:
            print(f"  {i}/{len(entities)} entities · {len(acc_owner)} unique accessions")
        time.sleep(0.11)
    print(f"unique ownership filings: {len(acc_owner)}")

    # 2) resolve roles from each filing's header
    companies: dict[str, dict] = {}
    skipped_no_subject = 0
    for n, (acc, cik) in enumerate(acc_owner.items(), 1):
        hdr = fetch_header(cik, acc)
        if not hdr:
            continue
        subject, filers = parse_header_roles(hdr)
        if not subject:
            skipped_no_subject += 1
            continue
        form, date = parse_header_meta(hdr)
        name, scik = subject
        # a filing where the "subject" is one of our own vehicles is not a holding
        if scik in desk_of:
            continue
        c = companies.setdefault(scik, {
            "name": name, "cik": scik, "forms": set(), "first": date, "last": date,
            "accessions": [], "filer_ciks": set(),
        })
        if len(name) > len(c["name"]):
            c["name"] = name
        c["forms"].add(form)
        c["accessions"].append(acc)
        c["filer_ciks"].update(fc for _, fc in filers)
        if date:
            c["first"] = min(c["first"] or date, date)
            c["last"] = max(c["last"] or date, date)
        if n % 250 == 0:
            print(f"  headers {n}/{len(acc_owner)} · {len(companies)} companies")
        time.sleep(0.02)

    # 3) desk per company: best (most senior) desk among its filing entities
    rows = []
    for c in companies.values():
        desks = {desk_of.get(fc, "unknown") for fc in c["filer_ciks"] if fc in desk_of}
        desk = next((d for d in DESK_RANK if d in desks), "unknown")
        rows.append({
            "name": c["name"], "cik": c["cik"], "desk": desk,
            "forms": sorted(c["forms"]), "first": c["first"], "last": c["last"],
            "accessions": sorted(set(c["accessions"])),
            "filer_ciks": sorted(c["filer_ciks"]),
        })
    rows.sort(key=lambda r: r["name"].lower())
    (OUT / "edgar-companies.json").write_text(json.dumps(rows, indent=1) + "\n")

    print(f"\nwrote edgar-companies.json — {len(rows)} companies")
    print("  by desk:", dict(Counter(r["desk"] for r in rows)))
    if skipped_no_subject:
        print(f"  filings with no parseable subject: {skipped_no_subject}")


if __name__ == "__main__":
    main()
