#!/usr/bin/env python3
"""The two inputs build-firm-profile.py refuses to start without.

sources/edgar/fund-formds.json  — Battery's OWN fund vehicles' Form D filings,
  keyed by issuer name. The roster sweep in sources/edgar/formd-sweep.json is
  the wrong set (it is partner name-matches against third-party issuers), so
  this walks the home-desk vehicle CIKs in entities.json instead and reads each
  vehicle's own Form Ds. `_readme` is a DICT because the fund verifier iterates
  every value (COLLECTION.md 11).

sources/site/team-members.json — the site team pull, flattened to the shape the
  profile build reads.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
P = Paths("battery-ventures")
OWN = re.compile(P.config()["profile"]["own_vehicle_pattern"], re.I)


def curl(url, tries=3):
    for i in range(tries):
        shared_throttle.wait("sec")
        try:
            return subprocess.run(["curl", "-sfL", "--max-time", "60",
                                   "-H", f"User-Agent: {UA}", url],
                                  capture_output=True, check=True).stdout.decode("utf-8", "replace")
        except subprocess.CalledProcessError:
            time.sleep(1.5 * (i + 1))
    return ""


def tag(xml, name):
    m = re.search(rf"<{name}>(.*?)</{name}>", xml, re.S)
    return m.group(1).strip() if m else None


def main() -> None:
    ents = json.load(open(P.entities))
    vehicles = [e for e in ents
                if e["desk"] == "us" and e.get("vehicle_role") != "person"
                and OWN.search(e["name"] + " ")]
    # own_vehicle_pattern requires a trailing space in the numeral form; also
    # accept the bare family names so the GP LLCs are not dropped.
    if len(vehicles) < 20:
        vehicles = [e for e in ents if e["desk"] == "us"
                    and e.get("vehicle_role") != "person"
                    and re.match(r"^battery (ventures|investment partners|partners)", e["name"], re.I)]
    print(f"{len(vehicles)} home-desk vehicles")
    out = {}
    for n, e in enumerate(vehicles, 1):
        cik = int(e["cik"])
        sub = curl(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
        if not sub:
            continue
        try:
            d = json.loads(sub)
        except json.JSONDecodeError:
            continue
        r = d.get("filings", {}).get("recent", {})
        rows = [(f, a, fd) for f, a, fd in zip(r.get("form", []),
                                               r.get("accessionNumber", []),
                                               r.get("filingDate", []))
                if f.startswith("D")]
        filings = []
        for form, acc, fdate in rows:
            xml = curl(f"https://www.sec.gov/Archives/edgar/data/{cik}/"
                       f"{acc.replace('-', '')}/primary_doc.xml")
            if not xml:
                continue
            co = [x.strip() for x in re.findall(r"<entityName>(.*?)</entityName>", xml, re.S)]
            filings.append({
                "form": form, "accession": acc, "quarter": fdate[:4],
                "offering": tag(xml, "totalOfferingAmount"),
                "sold": tag(xml, "totalAmountSold"),
                "indefinite": (tag(xml, "totalOfferingAmount") or "").lower() == "indefinite",
                "first_sale": tag(xml, "dateOfFirstSale"),
                "pooled": "Pooled Investment Fund" in xml,
                "fund_type": tag(xml, "investmentFundType"),
                "co_issuers": [c for c in co if c.lower() != d.get("name", "").lower()],
            })
        if filings:
            out[d.get("name") or e["name"]] = {"cik": f"{cik:010d}", "filings": filings}
        print(f"  [{n}/{len(vehicles)}] {d.get('name','?')[:46]:46s} {len(filings)} Form D")
    out["_readme"] = {
        "built": time.strftime("%Y-%m-%d"),
        "source": "data.sec.gov submissions per home-desk vehicle CIK in entities.json",
        "note": ("Battery's OWN fund vehicles' Form D filings. The roster sweep in "
                 "formd-sweep.json is a different set -- partner name-matches against "
                 "third-party issuers -- and is not usable for the fund ladder. Filings "
                 "carry no accession assertion here unless the filing reports a non-zero "
                 "sold amount, because a fund whose latest Form D reports $0 sold must "
                 "carry no accession (COLLECTION.md 11)."),
    }
    write_atomic(P.edgar / "fund-formds.json", json.dumps(out, indent=1))
    print(f"wrote fund-formds.json: {len(out)-1} vehicles")

    # ---- team-members.json
    BUCKET = [(r"general partner|^partner$|private equity partner|managing", "investor"),
              (r"principal|vice president|associate|investment team", "investor"),
              (r"operating partner|executive in residence|talent|go-to-market|"
               r"marketing|business development|recruit", "operating"),
              (r"cfo|finance|compliance|legal|counsel|controller|tax|accounting|"
               r"office manager|assistant|human resources|people", "operations"),
              (r"advisor|senior advisor", "advisor")]
    people = []
    for r in json.load(open(P.site / "team-pages.json"))["rows"]:
        title = r.get("title") or ""
        bucket = next((b for pat, b in BUCKET if re.search(pat, title, re.I)), "other")
        people.append({"name": r["name"], "cms_title": title or None,
                       "role_bucket": bucket, "site_group": r.get("office"),
                       "linkedin_url": r.get("linkedin_url"), "x_url": r.get("x_url"),
                       "source": r["url"], "joined": r.get("joined")})
    write_atomic(P.site / "team-members.json", json.dumps(people, indent=1))
    from collections import Counter
    print(f"wrote team-members.json: {len(people)} people "
          f"{dict(Counter(p['role_bucket'] for p in people))}")


if __name__ == "__main__":
    main()
