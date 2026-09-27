#!/usr/bin/env python3
"""Registered-fund positions and the EDGAR company layer (rewritten 2026-09-27).

First version: appended one row per restricted N-PORT issuer to
sources/edgar/edgar-companies.json with forms ["NPORT-P"] and an empty CIK.
That failed verify ("edgar_links missing on rows with forms"): the builder
forms a filing link from the row's own CIK, and an N-PORT is filed under the
FUND's CIK (2044519), so a company row has no CIK to link with. Giving eleven
companies the fund's CIK would make the same-registrant check read them as one.

What this script does now: it REMOVES those rows again, so the EDGAR company
layer holds ownership forms only, as the shared script writes it. The
registered-fund evidence stays in sources/edgar/registered-fund-holdings.json
and reaches the base two ways: a company the firm lists keeps its listing as
membership evidence and cites the N-PORT in its note; a company on no list
(Kalshi) enters as a ledger recall addition citing the N-PORT filing, verdict
evidence class fund_filing. Re-run after every `run.py collect` is NOT needed.
A builder change (a filer-side link for fund filings) is proposed in report.md.
"""
import json
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
EC = INV / "sources/edgar/edgar-companies.json"
rows = json.load(open(EC)); keep = []; dropped = trimmed = 0
for r in rows:
    if "NPORT-P" in (r.get("forms") or []):
        if set(r["forms"]) == {"NPORT-P"}: dropped += 1; print("  dropped", r["name"]); continue
        r["forms"] = [f for f in r["forms"] if f != "NPORT-P"]; r["accessions"] = [a for a in r["accessions"] if not a.startswith("0001410368-")]
        r["filer_ciks"] = [c for c in r.get("filer_ciks", []) if c != "2044519"]; trimmed += 1; print("  trimmed", r["name"])
    keep.append(r)
EC.write_text(json.dumps(keep, indent=1) + "\n")
lp = INV / "companies/membership-ledger.json"; L = json.load(open(lp)); b = L["coatue"]
if not any(a["slug"] == "kalshi" for a in b["recall_additions"]):
    b["recall_additions"].append({"name": "Kalshi", "slug": "kalshi", "first_seen": "2026", "on_site_now": False, "sector": "Fintech", "source": "registered-fund layer (scripts/edgar-registered-fund.py)",
        "citation": "https://www.sec.gov/Archives/edgar/data/2044519/000141036826085820/primary_doc.xml",
        "basis": "The Coatue Innovative Strategies Fund (CIK 2044519) reports a restricted position in Kalshi on its N-PORT for the period ending 2026-06-30: a fund of the firm holding a private company's stock (decisions.md D4). The company is not on the firm's page."})
    lp.write_text(json.dumps(L, indent=1, sort_keys=True) + "\n")
print(f"dropped {dropped}, trimmed {trimmed}; recall additions: {[a['slug'] for a in b['recall_additions']]}")
