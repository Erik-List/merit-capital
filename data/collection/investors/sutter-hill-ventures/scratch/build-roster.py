#!/usr/bin/env python3
"""Build Sutter Hill Ventures' roster for the Form D sweep from first-party sources.

Sources, unioned into sources/wayback/partner-roster.json in partner-roster.py's
shape ({slug, name, years_seen, first_seen, last_seen, snapshots, sources}):

  team-pages   the archived people pages of both domains (shv.com and
               sutterhillventures.com): 2000 to 2003 /<surname>.html,
               2004 to 2012 /team/<surname>.html, 2013 to 2016 /<first-last>.
               Years come from scratch/roster-captures.json (one CDX row per
               page per year) when present, else from the first-capture index
               in scratch/cdx-*.json.
  adv          the owners on Schedule A of the newest Form ADV (CRD 162959,
               2026-03-27), dated from the "date title acquired" to 2026.
  formd-addr   related persons on issuers' Form Ds who give the firm's own
               street address (sources/edgar/formd-address-sweep.json), dated
               by filing year. Kept only for a person another first-party
               source already names as the firm's: 755 Page Mill Road is an
               office park, and Otter Capital's John Pasquesi, Costanoa's
               vehicles and the incubated companies' own founders file from it
               too.

One person, one entry: the page slugs and filing spellings fold onto one name
through PEOPLE (the First Round rule: two spellings are two people to the
tenure filter).

Usage: python3 data/collection/investors/sutter-hill-ventures/scratch/build-roster.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
from people_common import same_person  # noqa: E402

P = Paths("sutter-hill-ventures")
OUT = P.wayback / "partner-roster.json"
THIS_YEAR = 2026

# page slug(s) -> the person's name as the firm's own pages give it. The page
# slugs are surnames (2000 to 2012) or first-last (2013 to 2016).
PEOPLE = {
    "David L. Anderson": ["anderson", "david-anderson"],
    "G. Leonard Baker Jr.": ["baker", "len-baker"],
    "Ronald Bernal": ["bernal"],
    "Jeffrey W. Bird": ["bird", "jeff-bird"],
    "Tench Coxe": ["coxe", "tench-coxe"],
    "Lynn Ebringer": ["ebringer"],
    "James C. Gaither": ["gaither"],
    "Gregory P. Sands": ["sands"],
    "David E. Sweet": ["sweet"],
    "James N. White": ["white", "jim-white"],
    "Paul M. Wythes": ["wythes", "paulw"],
    "William H. Younger Jr.": ["younger"],
    "Andrew T. Sheehan": ["sheehan", "andy-sheehan"],
    "Michael L. Speiser": ["speiser", "mike-speiser"],
    "Stefan A. Dyckerhoff": ["dyckerhoff", "stefan-dyckerhoff"],
    "Samuel J. Pullara III": ["pullara", "sam-pullara"],
}

# Schedule A owners who are investment professionals; the CFO and the
# owners' spouses (trust co-trustees) are not deal people.
ADV_PEOPLE = {
    "SPEISER, MICHAEL": "Michael L. Speiser",
    "PULLARA III, SAMUEL": "Samuel J. Pullara III",
    "DYCKERHOFF, STEFAN": "Stefan A. Dyckerhoff",
    "LOEBNER, KEITH": "Keith Loebner",
    "RAMPELL, PAUL": "Palmer Rampell",
    "WROBLEWSKI, LUKASZ": "Luke Wroblewski",
    "SCHLAMPP, PETER": "Peter Schlampp",
}


# People the archive and the ADV do not carry, each placed at the firm by a
# filing on a Sutter Hill company (found by the recall probe, 2026-09-28):
# the Form D is the date evidence, the basis says what ties the person to SHV.
MANUAL = {
    "Brian Blond": ([2021, 2025], "director of Leibniz Data Systems on its 2021 Form D, filing from the firm's own suite "
                    "(Bldg A 200, 755 Page Mill Road)"),
    "Victor Miller": ([2025], "director of Luminary Cloud and Matic Robots, both Sutter Hill companies, on their 2025 Form Ds"),
    "Chad Peets": ([2024, 2025], "director of Sigma Computing, a Sutter Hill incubation, on its 2024 and 2025 Form Ds"),
}


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def team_years() -> dict[str, set[int]]:
    """page slug -> capture years of that person's page, either domain."""
    years: dict[str, set[int]] = {}
    per_year = P.scratch / "roster-captures.json"
    rows = []
    if per_year.exists():
        rows = [(r[0], r[1]) for r in json.load(open(per_year))]
    for dom in ("shv.com", "sutterhillventures.com"):
        f = P.scratch / f"cdx-{dom}.json"
        if f.exists():
            rows += [(r[0], r[1]) for r in json.load(open(f))[1:] if r[2] == "200"]
    all_slugs = {s for v in PEOPLE.values() for s in v}
    for ts, orig in rows:
        path = re.sub(r"^https?://[^/]+", "", orig).replace(":80", "").split("?")[0]
        m = re.match(r"^/(?:team/)?([a-z-]+?)(?:\.html?)?/?$", path)
        if not m or m.group(1) not in all_slugs:
            continue
        years.setdefault(m.group(1), set()).add(int(ts[:4]))
    return years


def adv_owners() -> dict[str, int]:
    text = (P.scratch / "adv-clean.txt").read_text()
    out = {}
    for key, name in ADV_PEOPLE.items():
        m = re.search(re.escape(key) + r".{0,300}?(\d\d)/(\d{4})", text, re.S)
        if m:
            out[name] = int(m.group(2))
    return out


def formd_years(names: list[str]) -> dict[str, set[int]]:
    f = P.edgar / "formd-address-sweep.json"
    out: dict[str, set[int]] = {}
    if not f.exists():
        return out
    for acc, r in json.load(open(f)).items():
        filed = str(r.get("filed") or "")
        ym = re.search(r"(19|20)\d\d", filed)
        if not ym:
            continue
        y = int(ym.group(0))
        for p in r["persons"]:
            first, last = p["first"].title(), p["last"].title()
            for n in names:
                if same_person(n, f"{first} {last}"):
                    out.setdefault(n, set()).add(y)
    return out


def main() -> None:
    ty = team_years()
    adv = adv_owners()
    names = list(PEOPLE) + [n for n in ADV_PEOPLE.values() if n not in PEOPLE] + list(MANUAL)
    fd = formd_years(names)
    roster = []
    for name in names:
        years: set[int] = set()
        sources = []
        basis = []
        page_years = set()
        for s in PEOPLE.get(name, []):
            page_years |= ty.get(s, set())
        if page_years:
            years |= page_years
            sources.append("team-pages")
            basis.append(f"archived people pages {min(page_years)}-{max(page_years)}")
        if name in adv:
            years |= set(range(adv[name], THIS_YEAR + 1))
            sources.append("adv")
            basis.append(f"Form ADV Schedule A owner since {adv[name]} (CRD 162959, 2026-03-27)")
        if fd.get(name):
            years |= fd[name]
            sources.append("formd-addr")
            basis.append(f"files from 755 Page Mill Road on issuers' Form Ds {min(fd[name])}-{max(fd[name])}")
        if name in MANUAL:
            years |= set(MANUAL[name][0])
            sources.append("formd-portfolio")
            basis.append(MANUAL[name][1])
        if not years:
            continue
        roster.append({
            "slug": slug_of(name), "name": name,
            "years_seen": sorted(years), "first_seen": min(years),
            "last_seen": max(years), "snapshots": len(years),
            "sources": sources, "basis": "; ".join(basis),
        })
    roster.sort(key=lambda r: r["slug"])
    write_atomic(OUT, json.dumps(roster, indent=1) + "\n")
    for r in roster:
        print(f"  {r['name']:26s} {r['first_seen']}-{r['last_seen']} n={r['snapshots']:2d} {','.join(r['sources'])}")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(roster)} people", file=sys.stderr)


if __name__ == "__main__":
    main()
