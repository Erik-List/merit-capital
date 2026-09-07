#!/usr/bin/env python3
"""Battery's own fund vehicles' Form D related persons, as a partner roster.

INVENTED LAYER (COLLECTION.md 5, "when the evidence is thin, invent the
layer"). On 2026-09-06 the Internet Archive refused every CDX query AND
Common Crawl's collinfo returned empty replies -- both capture archives down
at once -- so partner-roster.py could enumerate only the 133 people the LIVE
site publishes, every one of them stamped 2026-2026. A current-only roster
has two costs: the Form D sweep never targets a departed partner, and
build-company-base.py's ex-partner tenure rule has no window to test.

What replaces it: the firm's OWN vehicles file Form D, and every Form D
carries a `relatedPersonsList` -- the general partners and managers as of
that filing, with the filing's own date. Across Battery Ventures LP (1983)
through XV, the Side Funds, the Select Funds and their GP LLCs that is a
first-party, dated roster reaching back to the start of electronic Form D,
and it depends on neither archive.

Tenure is the span of filings naming the person, which is a proxy of the
same kind as a CDX snapshot span and is recorded as such: it under-reports
anyone who never sat on a filing vehicle.

Output: sources/edgar/fund-related-persons.json
"""
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
P = Paths("battery-ventures")
OUT = P.edgar / "fund-related-persons.json"


def curl(url: str, tries: int = 4) -> str:
    for i in range(tries):
        shared_throttle.wait("sec")
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", "replace")
        except subprocess.CalledProcessError:
            time.sleep(1.5 * (i + 1))
    return ""


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def titlecase(n: str) -> str:
    """EDGAR renders people as 'TOBIN SCOTT R' or 'Elhafed Morad'."""
    return " ".join(w.capitalize() if w.isupper() or w.islower() else w
                    for w in n.split())


def main() -> None:
    ents = json.load(open(P.entities))
    ciks = [e["cik"] for e in ents
            if e["desk"] == "us" and e.get("vehicle_role") != "person"]
    print(f"{len(ciks)} home-desk vehicles")

    people: dict[str, dict] = {}
    seen_filings = 0
    for n, cik in enumerate(ciks, 1):
        sub = curl(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
        if not sub:
            print(f"  [{n}/{len(ciks)}] {cik}: submissions unavailable")
            continue
        try:
            d = json.loads(sub)
        except json.JSONDecodeError:
            continue
        r = d.get("filings", {}).get("recent", {})
        rows = list(zip(r.get("form", []), r.get("accessionNumber", []),
                        r.get("filingDate", [])))
        ds = [(f, a, fd) for f, a, fd in rows if f.startswith("D")]
        for form, acc, fdate in ds:
            a = acc.replace("-", "")
            xml = curl(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                       f"{a}/primary_doc.xml")
            if not xml:
                continue
            seen_filings += 1
            year = int(fdate[:4])
            for m in re.finditer(r"<relatedPersonInfo>(.*?)</relatedPersonInfo>",
                                 xml, re.S):
                blk = m.group(1)
                first = re.search(r"<firstName>(.*?)</firstName>", blk, re.S)
                last = re.search(r"<lastName>(.*?)</lastName>", blk, re.S)
                mid = re.search(r"<middleName>(.*?)</middleName>", blk, re.S)
                if not (first and last):
                    continue
                nm = " ".join(x.group(1).strip() for x in (first, mid, last) if x
                              and x.group(1).strip())
                nm = titlecase(re.sub(r"\s+", " ", nm)).strip()
                if not nm:
                    continue
                rels = [x.strip() for x in
                        re.findall(r"<relationship>(.*?)</relationship>", blk, re.S)]
                p = people.setdefault(slug_of(nm), {
                    "slug": slug_of(nm), "name": nm, "years": set(),
                    "relationships": set(), "vehicles": set(), "accessions": []})
                p["years"].add(year)
                p["relationships"].update(rels)
                p["vehicles"].add(d.get("name", cik))
                if len(p["accessions"]) < 8:
                    p["accessions"].append(acc)
        print(f"  [{n}/{len(ciks)}] {d.get('name','?')[:44]:44s} "
              f"{len(ds):3d} Form D · {len(people)} people so far")

    rows = []
    for p in people.values():
        ys = sorted(p["years"])
        rows.append({"slug": p["slug"], "name": p["name"],
                     "first_seen": ys[0], "last_seen": ys[-1],
                     "years_seen": ys,
                     "relationships": sorted(p["relationships"]),
                     "vehicles": sorted(p["vehicles"]),
                     "accessions": p["accessions"],
                     "source": "formd_related_persons"})
    rows.sort(key=lambda r: (r["first_seen"], r["name"]))
    write_atomic(OUT, json.dumps({
        "_readme": (
            "Related persons named on Battery's OWN fund vehicles' Form D "
            "filings, aggregated per person with the filing years as a tenure "
            "window. Built 2026-09-06 as a substitute for the Wayback/Common "
            "Crawl people namespaces when BOTH archives were unreachable "
            "(CDX connection-refused, CC collinfo empty). Tenure here is the "
            "span of FILINGS naming the person, a proxy of the same kind as a "
            "snapshot span: it under-reports anyone who never sat on a filing "
            "vehicle, and it starts with electronic Form D (2008), so the "
            "1983-2007 partners are not recoverable this way."),
        "_built": time.strftime("%Y-%m-%d"),
        "_filings_read": seen_filings,
        "rows": rows}, indent=1))
    print(f"\nwrote {OUT}: {len(rows)} people from {seen_filings} Form D filings")
    for r in rows:
        print(f"   {r['first_seen']}-{r['last_seen']}  {r['name'][:32]:32s} "
              f"{','.join(r['relationships'])[:40]}")


if __name__ == "__main__":
    main()
