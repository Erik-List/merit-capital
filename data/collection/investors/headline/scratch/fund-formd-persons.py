"""Related persons on the firm's own vehicles' Form D filings, dated by filing.

Reads every own-desk CIK in entities.json, lists its Form D / D/A filings via
the SEC submissions API, and extracts each filing's related persons (name,
relationship, clarification, city). Writes sources/edgar/fund-formd-persons.json:
one row per person with the filing dates and vehicles that name them, which is
the kickoff roster's filing-grade leg (config.json roster._note)."""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parents[3] / "scripts"))
import shared_throttle  # noqa: E402

UA = "Merit Capital research erik@meritcapit.al"


def get(url):
    shared_throttle.wait("sec")
    r = subprocess.run(["curl", "-sS", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                       capture_output=True)
    return r.stdout.decode("utf-8", "replace")


ents = [e for e in json.loads((HERE / "entities.json").read_text()) if e["desk"] == "headline"]
people = {}
filings = []
for e in ents:
    cik = int(e["cik"])
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json") or "{}")
    rec = (sub.get("filings") or {}).get("recent") or {}
    for form, date, acc, doc in zip(rec.get("form", []), rec.get("filingDate", []),
                                    rec.get("accessionNumber", []), rec.get("primaryDocument", [])):
        if form not in ("D", "D/A"):
            continue
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/primary_doc.xml"
        x = get(url)
        sold = re.findall(r"<totalAmountSold>(.*?)</totalAmountSold>", x)
        offer = re.findall(r"<totalOfferingAmount>(.*?)</totalOfferingAmount>", x)
        filings.append({"cik": cik, "vehicle": e["name"], "form": form, "date": date, "accession": acc,
                        "total_offering": offer[0] if offer else None, "total_sold": sold[0] if sold else None})
        for m in re.finditer(r"<relatedPersonInfo>(.*?)</relatedPersonInfo>", x, re.S):
            b = m.group(1)
            first = (re.findall(r"<firstName>(.*?)</firstName>", b) or [""])[0].strip()
            last = (re.findall(r"<lastName>(.*?)</lastName>", b) or [""])[0].strip()
            mid = (re.findall(r"<middleName>(.*?)</middleName>", b) or [""])[0].strip()
            if first.upper() in ("N/A", "NA", "") and not mid:
                name = last
            else:
                name = " ".join(x for x in (first, mid, last) if x)
            rel = re.findall(r"<relationship>(.*?)</relationship>", b)
            clar = (re.findall(r"<relationshipClarification>(.*?)</relationshipClarification>", b) or [""])[0]
            city = (re.findall(r"<city>(.*?)</city>", b) or [""])[0]
            p = people.setdefault(name.lower(), {"name": name, "filings": []})
            p["filings"].append({"date": date, "vehicle": e["name"], "accession": acc,
                                 "relationship": rel, "clarification": clar, "city": city})
    print(e["name"], "done", file=sys.stderr)

for p in people.values():
    ds = sorted(f["date"] for f in p["filings"])
    p["first_filing"], p["last_filing"], p["n"] = ds[0], ds[-1], len(ds)
out = {"_readme": __doc__, "filings": sorted(filings, key=lambda f: f["date"]),
       "people": sorted(people.values(), key=lambda p: p["first_filing"])}
(HERE / "sources" / "edgar" / "fund-formd-persons.json").write_text(json.dumps(out, indent=1) + "\n")
for p in out["people"]:
    print(f"{p['first_filing']}..{p['last_filing']} {p['n']:3d} {p['name']} | {p['filings'][0]['clarification'][:60]}")
print(len(filings), "filings")
