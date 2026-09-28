#!/usr/bin/env python3
"""The Form D sweep roster for Ribbit (sources/wayback/partner-roster.json).

Ribbit publishes one team page, names and LinkedIn links only: no titles, no
groups, no per-person pages, so partner-roster.py has nothing to enumerate.
Each person's window is read off the team page itself, one capture per year:
2012-2015 /about/ ("Our Team"), 2015-2024 /team/ (<span class="member-name">),
2025-2026 the live Next.js /team (sources/site/team-pages.json). A person is
seen in a year when a capture of that year names them.

Everyone on the page is a sweep target: the site does not say who invests, and
a seat on a portfolio company's Form D is what the sweep looks for. What a
title the record does give (ADV Schedule A, the firm's own fund Form Ds) is
kept in `basis`. Formal first names are added where a filing would carry them
(Form Ds file "Nicholas Shalek", "Cynthia McAdam", "Jessica Brooks"), as
separate entries with the SAME window, so the ex-partner rule never reads a
split person (COLLECTION.md s8, the First Round Kopelman lesson).

Usage: python3 scratch/build-roster.py
"""
import json
import re
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("ribbit-capital")
RAW = P.wayback / "raw"

# What the record says about a person's role (never from LinkedIn or memory).
ROLES = {
    "meyer malka": "Managing Director and 75%+ owner of the adviser since 03/2012 (ADV Schedule A); "
                   "related person on every Ribbit fund Form D",
    "nick shalek": "related person (executive officer) on the Ribbit OB1 feeders' Form Ds, 2022-2025",
    "cindy mcadam": "Chief Operating Officer of the adviser since 12/2016 (ADV Schedule A)",
    "jessi brooks": "Chief Compliance Officer of the adviser since 10/2021 (ADV Schedule A)",
}
# Formal names a filing would carry: (site name -> extra roster names)
ALIASES = {
    "meyer malka": ["Micky Malka"],
    "nick shalek": ["Nicholas Shalek"],
    "cindy mcadam": ["Cynthia McAdam"],
    "jessi brooks": ["Jessica Brooks"],
    "gabe mennesson": ["Gabriel Mennesson"],
    "alli london": ["Allison London"],
    "nick huber": ["Nicholas Huber"],
    "amy hawkins-leong": ["Amy Hawkins"],
    "rebekah murphy": ["Rebekah Rogers"],
    "meghan stevenson-krausz": ["Meghan Stevenson"],
    "katie suskind": ["Katie Neal"],
}
# One person under two page renderings (a married name, a quoted nickname).
SAME = {"rebekah rogers": "rebekah murphy", "amy hawkins": "amy hawkins-leong",
        "meyer micky malka": "meyer malka"}


NOT_PEOPLE = {"our jedi"}   # the page's frog mascot, rendered in the member-name slot 2015-2016


def clean(name: str) -> str:
    n = unescape(name).replace("“", '"').replace("”", '"')
    n = re.sub(r'"[^"]*"\s*', "", n)          # Meyer "Micky" Malka -> Meyer Malka
    n = re.sub(r"\([^)]*\)\s*", "", n)         # Katie (Neal) Suskind -> Katie Suskind
    return re.sub(r"\s+", " ", n).strip()


def key(name: str) -> str:
    k = clean(name).lower()
    return SAME.get(k, k)


def names_in(path: Path) -> list[str]:
    s = path.read_bytes().decode("utf-8", errors="replace")
    found = re.findall(r'<span class="member-name">([^<]+)</span>', s)
    if not found:   # the 2012-2015 /about/ page: one heading per person
        found = re.findall(r'<h3[^>]*>\s*(?:<a[^>]*>)?([A-Z][^<]{3,40}?)(?:</a>)?\s*</h3>', s)
    return [clean(n) for n in found if clean(n) and clean(n).lower() not in NOT_PEOPLE]


def main() -> None:
    seen: dict[str, dict] = {}
    for f in sorted(RAW.glob("*.html")):
        m = re.match(r"(team|about)-(\d{14})\.html$", f.name)
        if not m:
            continue
        ts = m.group(2)
        for n in names_in(f):
            e = seen.setdefault(key(n), {"name": n, "years": set(), "sources": set()})
            e["years"].add(int(ts[:4]))
            e["sources"].add(f"https://web.archive.org/web/{ts}/{'http://ribbitcap.com/' + m.group(1) + '/'}")
    live = json.loads((P.site / "team-pages.json").read_text())["rows"]
    for r in live:
        n = clean(r["name"])
        e = seen.setdefault(key(n), {"name": n, "years": set(), "sources": set()})
        e["name"] = n                      # the live rendering wins
        e["years"].add(2026)
        e["sources"].add("https://ribbitcap.com/team")
    roster = []
    for k, e in sorted(seen.items()):
        years = sorted(e["years"])
        basis = ROLES.get(k, "On the firm's team page; the site publishes no title.")
        entry = {"years_seen": years, "first_seen": years[0], "last_seen": years[-1],
                 "snapshots": len(years), "sources": sorted(e["sources"]),
                 "basis": basis + f" Seen on the team page in {', '.join(map(str, years))}."}
        for n in [e["name"]] + ALIASES.get(k, []):
            roster.append({"slug": re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-"),
                           "name": n, **entry})
    roster.sort(key=lambda r: r["slug"])
    write_atomic(P.wayback / "partner-roster.json", json.dumps(roster, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(seen)} people, {len(roster)} sweep names")
    for r in roster:
        print(f"  {r['name']:28} {r['first_seen']}-{r['last_seen']} ({r['snapshots']})")


if __name__ == "__main__":
    main()
