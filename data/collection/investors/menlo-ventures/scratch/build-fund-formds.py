#!/usr/bin/env python3
"""The firm's own fund vehicles' Form D filings -> sources/edgar/fund-formds.json.

One entry per vehicle in the entity registry that matches profile.own_vehicle_pattern
and is not desk=external, with every Form D it filed: accession, date, amount sold,
total offering and the filing's named related persons (executive officers and
directors). This is the evidence the profile's fund table is asserted against at
build time, and the related persons are a dated roster the site cannot give.
"""
import json, re, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "Merit Capital research erik@meritcapit.al"


def curl(url: str) -> str:
    for _ in range(3):
        shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-sf", "--max-time", "45", "-H", f"User-Agent: {UA}", url],
                           capture_output=True)
        if r.returncode == 0:
            return r.stdout.decode("utf-8", "replace")
        time.sleep(1.5)
    return ""


def main() -> None:
    p = Paths("menlo-ventures")
    own = re.compile(p.config()["profile"]["own_vehicle_pattern"], re.I)
    ents = json.loads(p.entities.read_text())
    ents = ents if isinstance(ents, list) else list(ents.values())
    out = {"_readme": {"note": (
        "The firm's own fund-vehicle Form D filings, pulled per-CIK from the EDGAR submissions "
        "API by scratch/build-fund-formds.py. related_persons are the filing's named executive "
        "officers and directors; on Menlo they are the dated partner roster the site's people "
        "pages cannot give before 2012. NOTE the filing style: Menlo files the fund's full "
        "target as `offering` and amends `sold` at close, so `sold` is the close state on the "
        "filing date and not the fund size.")}}
    for e in sorted(ents, key=lambda x: x.get("name") or ""):
        name, cik, desk = e.get("name") or "", str(e.get("cik") or ""), e.get("desk")
        if desk == "external" or not own.search(name) or not cik:
            continue
        subs = curl(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
        if not subs:
            continue
        d = json.loads(subs)
        rec = d.get("filings", {}).get("recent", {})
        rows = []
        for i, form in enumerate(rec.get("form", [])):
            if form not in ("D", "D/A"):
                continue
            acc = rec["accessionNumber"][i]
            raw = curl(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                       f"{acc.replace('-','')}/primary_doc.xml")
            sold = re.search(r"<totalAmountSold>([\d.]+)</totalAmountSold>", raw)
            offer = re.search(r"<totalOfferingAmount>([\d.]+)</totalOfferingAmount>", raw)
            people = []
            for blk in re.findall(r"<relatedPersonInfo>(.*?)</relatedPersonInfo>", raw, re.S):
                first = re.search(r"<firstName>(.*?)</firstName>", blk)
                mid = re.search(r"<middleName>(.*?)</middleName>", blk)
                last = re.search(r"<lastName>(.*?)</lastName>", blk)
                nm = " ".join(x.group(1).strip() for x in (first, mid, last) if x and x.group(1).strip())
                if nm:
                    people.append(nm)
            rows.append({"accession": acc, "form": form, "date": rec["filingDate"][i],
                         "sold": sold.group(1) if sold else None,
                         "offering": offer.group(1) if offer else None,
                         "related_persons": people})
        if rows:
            out[d.get("name") or name] = {"cik": int(cik), "desk": desk,
                                          "filings": sorted(rows, key=lambda r: r["date"])}
    write_atomic(p.edgar / "fund-formds.json", json.dumps(out, indent=1) + "\n")
    n = len(out) - 1
    print(f"vehicles with Form D filings: {n}   filings: "
          f"{sum(len(v['filings']) for k, v in out.items() if k != '_readme')}")


if __name__ == "__main__":
    main()
