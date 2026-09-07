#!/usr/bin/env python3
"""Assemble sources/edgar/fund-formds.json — the firm's OWN fund filings.

COLLECTION.md §11 says build-firm-profile.py refuses to start without this file
and that nothing else writes it. It is NOT a slice of the roster Form D sweep
(that sweep is keyed on portfolio issuers); it is a direct pull of every Form D
filed by an entity in the investor's own registry whose name matches
config.profile.own_vehicle_pattern.

Two traps the playbook names, both handled here: the `_readme` must be a DICT,
because the fund verifier iterates every value in this file; and a fund entry
carrying an accession is asserted against TOTALAMOUNTSOLD at build time, so the
sold figure recorded here has to be the filed one.

Usage: python3 fund-formds-pull.py
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "Merit Capital research erik@meritcapit.al"
P = Paths("8vc")
cfg = json.loads((P.root / "config.json").read_text())
own = re.compile(cfg["profile"]["own_vehicle_pattern"], re.I)
entities = json.loads((P.root / "entities.json").read_text())
rows = entities["entities"] if isinstance(entities, dict) and "entities" in entities else entities


def curl(url: str) -> str:
    for i in range(4):
        shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-sf", "--max-time", "45", "-H", f"User-Agent: {UA}", url],
                           capture_output=True)
        if r.returncode == 0:
            return r.stdout.decode("utf-8", errors="replace")
        time.sleep(1.5 * (i + 1))
    return ""


def field(xml: str, tag: str) -> str | None:
    m = re.search(rf"<{tag}>([^<]*)</{tag}>", xml)
    return m.group(1) if m else None


out: dict = {}
cands = [r for r in rows if r.get("desk") != "external" and own.search(r["name"])]
print(f"own vehicles matching the profile pattern: {len(cands)}")
for i, e in enumerate(sorted(cands, key=lambda x: x["name"]), 1):
    cik = int(e["cik"])
    sub = curl(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
    if not sub:
        print(f"  {e['name']}: submissions unreachable")
        continue
    d = json.loads(sub)
    f = d.get("filings", {}).get("recent", {})
    filings = []
    for j, form in enumerate(f.get("form", [])):
        if form not in ("D", "D/A"):
            continue
        acc = f["accessionNumber"][j]
        doc = f["primaryDocument"][j].split("/")[-1]
        xml = curl(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}")
        offering = field(xml, "totalOfferingAmount")
        filings.append({
            "form": form,
            "accession": acc,
            "quarter": f["filingDate"][j][:4],
            "offering": None if offering in (None, "Indefinite") else offering,
            "sold": field(xml, "totalAmountSold"),
            "indefinite": offering == "Indefinite",
            "first_sale": field(xml, "dateOfFirstSale"),
            "pooled": (field(xml, "isPooledInvestmentFundType") or "").lower() == "true",
            "fund_type": field(xml, "investmentFundType"),
            "co_issuers": re.findall(r"<entityName>([^<]*)</entityName>", xml)[1:],
        })
    if filings:
        out[e["name"]] = {"cik": f"{cik:010d}", "filings": filings}
    if i % 10 == 0:
        print(f"  {i}/{len(cands)}")

out["_readme"] = {
    "what": ("Every Form D filed by an 8VC vehicle in the investor's own EDGAR registry whose name "
             "matches config.profile.own_vehicle_pattern. Written by scratch/fund-formds-pull.py; "
             "COLLECTION.md §11 requires this file and says nothing else writes it."),
    "why_not_the_sweep": ("sources/edgar/formd-sweep.json is the ROSTER sweep — Form Ds carrying an "
                          "8VC person as a related person, i.e. portfolio issuers. The firm's own "
                          "vehicles are a different set and are pulled here by CIK."),
    "filing_style": ("8VC's flagship L.P.s and its SPVs file 'Indefinite' offerings, most of them at "
                     "$0 sold, so the §11 $0-sold cross-check against a total-offering amount does "
                     "NOT apply to this firm: an entry carrying an accession is asserted against the "
                     "filed sold amount, and fund sizes come from press or the ADV Section 7.B."),
    "vehicles": len(out) - 0,
}
write_atomic(P.root / "sources" / "edgar" / "fund-formds.json",
             json.dumps(out, indent=1, ensure_ascii=False))
print(f"wrote fund-formds.json — {len(out) - 1} vehicles with Form D filings")
