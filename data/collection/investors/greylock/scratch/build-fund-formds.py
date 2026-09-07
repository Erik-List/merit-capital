#!/usr/bin/env python3
"""Build sources/edgar/fund-formds.json for build-firm-profile.py.

COLLECTION.md §11 describes this as a mechanical filter of formd-sweep.json by
profile.own_vehicle_pattern.  That works where the roster sweep happens to have
caught the firm's own vehicles as issuers; on Greylock it catches exactly one of
forty, because the sweep matches PARTNER names on other companies' filings and
Greylock's fund L.P.s name no roster partner as a related person.  So the funds
are pulled straight from their own CIKs in entities.json instead — the same
shape, a source the sweep cannot supply.
"""
import json, pathlib, re, subprocess, time

ROOT = pathlib.Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/greylock"
UA = "merit-capital-research/1.0 (erik@meritcapit.al)"


def get(url):
    for _ in range(4):
        p = subprocess.run(["curl", "-sS", "--max-time", "45", "-A", UA, url],
                           capture_output=True)
        if p.returncode == 0 and p.stdout:
            return p.stdout.decode("utf-8", "replace")
        time.sleep(1.0)
    return ""


def field(xml, tag, all_=False):
    m = re.findall(rf"<{tag}>([^<]*)</{tag}>", xml)
    return m if all_ else (m[0] if m else None)


def main():
    cfg = json.loads((INV / "config.json").read_text())
    pat = re.compile(cfg["profile"]["own_vehicle_pattern"], re.I)
    ents = json.loads((INV / "entities.json").read_text())
    own = [e for e in ents if e.get("desk") != "external" and pat.search(e["name"].lower())]
    print(f"own vehicles: {len(own)}")
    out = {}
    for e in own:
        cik = str(int(e["cik"]))
        sub = get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
        if not sub:
            continue
        d = json.loads(sub)
        r = d["filings"]["recent"]
        filings = []
        for form, acc, date in zip(r["form"], r["accessionNumber"], r["filingDate"]):
            if not form.startswith("D"):
                continue
            xml = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/"
                      f"{acc.replace('-', '')}/primary_doc.xml")
            if not xml:
                continue
            offering = field(xml, "totalOfferingAmount")
            sold = field(xml, "totalAmountSold")
            names = field(xml, "entityName", all_=True)
            filings.append({
                "form": form, "accession": acc, "quarter": date[:7],
                "offering": None if offering in (None, "Indefinite") else int(offering),
                "sold": int(sold) if (sold or "").isdigit() else None,
                "indefinite": offering == "Indefinite",
                "first_sale": field(xml, "dateOfFirstSale"),
                "pooled": field(xml, "industryGroupType") == "Pooled Investment Fund",
                "fund_type": field(xml, "investmentFundType"),
                "co_issuers": [n for n in names[1:]] if len(names) > 1 else [],
            })
            time.sleep(0.15)
        out[d["name"]] = {"cik": cik, "filings": filings}
        print(f"  {d['name'][:48]:50} {len(filings)} Form D filings")
        time.sleep(0.15)
    dest = INV / "sources/edgar/fund-formds.json"
    dest.write_text(json.dumps({
        "_readme": {
            "what": ("Every Form D filed by a Greylock home-desk vehicle, keyed by the issuer name "
                     "EDGAR carries, with the offering and sold amounts, the co-issuers and the "
                     "first-sale date per filing."),
            "why_not_the_sweep": ("COLLECTION.md §11 builds this by filtering formd-sweep.json on "
                                  "profile.own_vehicle_pattern. That finds ONE of Greylock's forty "
                                  "vehicles: the roster sweep matches partner names as RELATED "
                                  "PERSONS on portfolio companies' filings, and Greylock's fund "
                                  "L.P.s name none of its partners that way. Pulled from the "
                                  "vehicles' own CIKs in entities.json instead."),
            "built_by": "scratch/build-fund-formds.py, 2026-09-07",
        },
        **out}, indent=1))
    print(f"wrote {dest} — {len(out)} vehicles, "
          f"{sum(len(v['filings']) for v in out.values())} filings")


if __name__ == "__main__":
    main()
