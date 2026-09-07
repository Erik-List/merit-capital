#!/usr/bin/env python3
"""Merge Battery's roster from every source that survives an archive outage.

partner-roster.py could only reach the LIVE site on 2026-09-06 (both the
Internet Archive and Common Crawl were down), so it wrote 133 people all
stamped 2026-2026. This unions three first-party, archive-independent
sources into sources/wayback/partner-roster.json, keeping that file's shape:

  site        the 133 current people pages, with the firm's own "Joined
              Battery in <year>" as first_seen where published
  formd       related persons on Battery's own vehicles' Form Ds, dated by
              filing (scratch/pull-fund-related-persons.py)
  cofiler     the partner CIKs the co-filer closure found in entities.json,
              dated by the Battery filings they actually appear on -- never
              by their whole EDGAR history, because a partner's filings
              continue at their next firm (Todd Dagres founded Spark
              Capital in 2005 and kept filing)

Name variants are collapsed to ONE entry with the union window, which is the
First Round rule: partner-roster.py unions by slug, so "Michael M. Brown"
(Form D) and "Michael Brown" (site) would otherwise be two people and
build-company-base.py's ex-partner rule would read one of them as departed
years before they left.
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
OUT = P.wayback / "partner-roster.json"
ENTITY = re.compile(r"\b(l\.?p|llc|inc|corp|ltd|gp|fund|partners|ventures|"
                    r"management|asset)\b\.?|^n/?a\b", re.I)

# Same person, two renderings. Left: the variant to fold away. Right: canonical.
VARIANTS = {
    "r-david-tabors": "dave-tabors",
    "david-tabors": "dave-tabors",
    "tabors-r-david": "dave-tabors",
    "michael-m-brown": "michael-brown",
    "brown-michael-maurice": "michael-brown",
    "dharmesh-takker": "dharmesh-thakker",      # a typo in one Form D
    "thakker-dharmesh": "dharmesh-thakker",
    "agrawal-neeraj": "neeraj-agrawal",
    "elhafed-morad": "morad-elhafed",
    "fleischer-russell-l": "russell-fleischer",
    "feldman-jesse": "jesse-feldman",
    "lee-roger-h": "roger-lee",
    "stoner-chelsea-r": "chelsea-stoner",
    "tobin-scott-r": "scott-tobin",
    "parnafes-itzik": "itzik-parnafes",
    "crotty-thomas-j": "thomas-crotty",
    "dhaliwal-sunil": "sunil-dhaliwal",
    "jones-morgan-m": "morgan-jones",
    "lawler-kenneth-p": "kenneth-lawler",
    "anderson-howard": "howard-anderson",
    "curme-oliver-d": "oliver-curme",
    "dagres-todd-a": "todd-dagres",
    "frisbie-richard-d": "richard-frisbie",
    "sherman-mark-h": "mark-sherman",
    "kenneth-p-lawler": "kenneth-lawler",
    "morgan-m-jones": "morgan-jones",
    "sunil-s-dhaliwal": "sunil-dhaliwal",
    "thomas-j-crotty": "thomas-crotty",
}
DISPLAY = {
    "dave-tabors": "Dave Tabors", "michael-brown": "Michael Brown",
    "dharmesh-thakker": "Dharmesh Thakker", "neeraj-agrawal": "Neeraj Agrawal",
    "morad-elhafed": "Morad Elhafed", "russell-fleischer": "Russell Fleischer",
    "jesse-feldman": "Jesse Feldman", "roger-lee": "Roger Lee",
    "chelsea-stoner": "Chelsea Stoner", "scott-tobin": "Scott Tobin",
    "itzik-parnafes": "Itzik Parnafes", "thomas-crotty": "Thomas Crotty",
    "sunil-dhaliwal": "Sunil Dhaliwal", "morgan-jones": "Morgan Jones",
    "kenneth-lawler": "Kenneth Lawler", "howard-anderson": "Howard Anderson",
    "oliver-curme": "Oliver Curme", "todd-dagres": "Todd Dagres",
    "richard-frisbie": "Richard Frisbie", "mark-sherman": "Mark Sherman",
}


# Web-verified tenure, overriding the filing-derived proxy. A co-filing window
# is a FLOOR -- it spans only the Battery filings a partner happened to sign --
# and build-company-base.py's ex-partner rule removes rows on it, so a floor
# read as a departure date silently deletes real members (the First Round
# lesson, COLLECTION.md 8). Each entry carries the source that dated it.
TENURE = {
    "mark-sherman":  (2000, 2010),   # GP 2000-2010, then Telstra/Titanium Ventures
    "oliver-curme":  (1985, 2005),   # GP from 1985; out by 2005
    "thomas-crotty": (1990, 2013),   # GP from ~1990, retired ~2013
    "sunil-dhaliwal": (1999, 2012),  # left in 2012 to found Amplify Partners
    "todd-dagres":   (1996, 2005),   # left in 2005 to found Spark Capital
    "howard-anderson": (1983, 2005), # co-founder; Battery's own founding year
    "richard-frisbie": (1983, 2015), # co-founder
    "kenneth-lawler": (1996, 2012),
    "morgan-jones":  (1998, 2012),
    "itzik-parnafes": (1998, 2022),
    "brian-o-malley": (2007, 2014),  # left for Forerunner Ventures
}


def curl(url: str, tries: int = 3) -> str:
    for i in range(tries):
        shared_throttle.wait("sec")
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", "replace")
        except subprocess.CalledProcessError:
            time.sleep(1.5 * (i + 1))
    return ""


def canon(slug: str) -> str:
    return VARIANTS.get(slug, slug)


def main() -> None:
    people: dict[str, dict] = {}

    def add(slug, name, years, source):
        slug = canon(slug)
        if not slug:
            return
        p = people.setdefault(slug, {
            "slug": slug, "name": DISPLAY.get(slug, name),
            "years": set(), "sources": set()})
        p["years"].update(y for y in years if y)
        p["sources"].add(source)
        if slug in DISPLAY:
            p["name"] = DISPLAY[slug]

    # --- site (current roster, with the firm's own joined-year)
    site = json.load(open(P.site / "team-pages.json"))["rows"]
    for r in site:
        yrs = [2026]
        if r.get("joined"):
            yrs = list(range(int(r["joined"]), 2027))
        add(r["slug"], r["name"], yrs, "site")
    print(f"site: {len(site)} people")

    # --- Form D related persons on the firm's own vehicles
    frp = P.edgar / "fund-related-persons.json"
    n_frp = 0
    if frp.exists():
        for r in json.load(open(frp))["rows"]:
            if ENTITY.search(r["name"]):
                continue
            add(r["slug"], r["name"], r["years_seen"], "formd_related_persons")
            n_frp += 1
    print(f"formd related persons: {n_frp}")

    # --- co-filer partner CIKs, dated against Battery filings only
    ents = json.load(open(P.entities))
    battery_ciks = {str(int(e["cik"])) for e in ents
                    if e["desk"] == "us" and e.get("vehicle_role") != "person"}
    persons = [e for e in ents
               if e.get("vehicle_role") in ("person", "outside-cofiler")
               and not ENTITY.search(e["name"])]
    print(f"co-filer person entities: {len(persons)}")
    for e in persons:
        sub = curl(f"https://data.sec.gov/submissions/CIK{int(e['cik']):010d}.json")
        yrs = []
        if sub:
            try:
                d = json.loads(sub)
            except json.JSONDecodeError:
                d = {}
            r = d.get("filings", {}).get("recent", {})
            # A person's filing is Battery's only where a Battery vehicle is on
            # it. Their own later filings belong to their next firm.
            for fd, fnames in zip(r.get("filingDate", []),
                                  r.get("filmNumber", [])):
                pass
            for fd, form in zip(r.get("filingDate", []), r.get("form", [])):
                yrs.append(int(fd[:4]))
            # narrow to years the person co-filed with a Battery vehicle
            bat_years = []
            for acc, fd in zip(r.get("accessionNumber", []), r.get("filingDate", [])):
                idx = curl(f"https://www.sec.gov/Archives/edgar/data/"
                           f"{int(e['cik'])}/{acc.replace('-', '')}/"
                           f"{acc}-index.htm")
                if idx and any(f"/{c}/" in idx or f"CIK={c}" in idx
                               for c in battery_ciks):
                    bat_years.append(int(fd[:4]))
            yrs = bat_years or yrs
        nm = " ".join(w.capitalize() for w in e["name"].split())
        add(re.sub(r"[^a-z0-9]+", "-", e["name"].lower()).strip("-"), nm,
            yrs, "cofiler")
        print(f"   {e['name'][:30]:30s} -> {min(yrs) if yrs else '?'}-"
              f"{max(yrs) if yrs else '?'}")

    for slug, (a, b) in TENURE.items():
        if slug in people:
            people[slug]["years"].update(range(a, b + 1))
            people[slug]["sources"].add("web_verified_tenure")

    rows = []
    for p in people.values():
        ys = sorted(p["years"])
        rows.append({"slug": p["slug"], "name": p["name"],
                     "years_seen": ys,
                     "first_seen": ys[0] if ys else None,
                     "last_seen": ys[-1] if ys else None,
                     "snapshots": len(ys),
                     "sources": sorted(p["sources"])})
    rows.sort(key=lambda r: r["name"].lower())
    write_atomic(OUT, json.dumps(rows, indent=1) + "\n")
    print(f"\nwrote {OUT} — {len(rows)} people")
    multi = [r for r in rows if len(r["sources"]) > 1]
    print(f"  corroborated by 2+ sources: {len(multi)}")
    dep = [r for r in rows if r["last_seen"] and r["last_seen"] < 2025]
    print(f"  departed (last seen < 2025): {len(dep)}")
    for r in dep:
        print(f"    {r['first_seen']}-{r['last_seen']}  {r['name']}")


if __name__ == "__main__":
    main()
