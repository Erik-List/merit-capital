#!/usr/bin/env python3
"""Build NEA's roster for the Form D sweep from first-party sources, into
sources/wayback/partner-roster.json in partner-roster.py's shape
({slug, name, years_seen, first_seen, last_seen, snapshots, sources}) plus title and basis.

Sources:
  cc          archived people pages (nea.com/team/<slug>, 2013 on; scratch/roster-cc.json from
              cc-roster.py), read per capture year: a year counts only when that year's own title
              on the page is an investing title.
  ia          the Internet Archive people pages (scratch/roster-ia.json, when present): the
              1990s-2012 sites, read the same way.
  site-team   the live CMS team (sources/site/team-pages.json), published rows in the Investors
              or Leadership unit with an investing title, year 2026.
  site-panel  the NEA deal team and board members the live CMS names per company, where the
              person is also on the published team, year 2026.

Left out: LP relations and capital formation, marketing and communications, talent, operations,
finance, legal and compliance, design and business development staff: none sits on a board for the
firm, and a common name among them buys only false Form D matches.
One person, one entry: name variants fold onto one slug with the union window (VARIANTS), and a
filed name replaces a nickname the sweep cannot match (FILED_NAME).
Usage: python3 build-roster.py
"""
from __future__ import annotations

import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("new-enterprise-associates")
OUT = P.wayback / "partner-roster.json"
THIS_YEAR = 2026
INVESTING = re.compile(r"general partner|managing partner|^partner\b|, partner\b|principal|associate|venture partner|"
                       r"special partner|managing director|investor|entrepreneur in residence|\beir\b|co-ceo|"
                       r"chief investment officer|chairman|head of (technology|healthcare|europe|ai)|co-head|"
                       r"venture advisor|analyst$|founder|^director$|^assistant vice president$|^vice president$|venture fellow", re.I)
NOT_INVESTING = re.compile(r"lp relations|limited partner|capital formation|marketing|communications|talent|"
                           r"operations|operating officer|finance|financial|accounting|controller|legal|counsel|"
                           r"compliance|design partner|business development|impact|events|esg|human resources|"
                           r"recruit|administrative|chief of staff|it\b|technology officer|prehistoric", re.I)
VARIANTS: dict[str, str] = {"kittu-kolluri": "krishna-kolluri", "krishna-kittu-kolluri": "krishna-kolluri"}
FILED_NAME = {"krishna-kolluri": "Krishna Kolluri"}
SUFFIX = re.compile(r",?\s*\b(MD|M\.D\.|PhD|Ph\.D\.|MBA|JD|DVM|MPH|PharmD|Jr\.?|Sr\.?|III|II)\b\.?", re.I)


def clean_name(name: str) -> str:
    name = re.sub(r"\s*(\([^)]*\)|['\u2018\u2019\"][^'\u2018\u2019\"]*['\u2018\u2019\"])", "", name or "")  # Krishna 'Kittu' Kolluri
    name = SUFFIX.sub("", name)
    return re.sub(r"\s+", " ", name).strip(" ,")


def slug_of(name: str) -> str:
    folded = unicodedata.normalize("NFKD", clean_name(name)).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", folded.lower().replace(".", "")).strip("-")
    return VARIANTS.get(s, s)


def investing(title: str) -> bool:
    return bool(title) and bool(INVESTING.search(title)) and not NOT_INVESTING.search(title)


def main() -> None:
    people: dict[str, dict] = {}

    def add(name, source, years, basis, title=""):
        name = clean_name(name)
        s = slug_of(name)
        if not s or "-" not in s:
            return
        r = people.setdefault(s, {"slug": s, "name": FILED_NAME.get(s, name), "years": set(), "sources": [],
                                  "basis": [], "titles": {}})
        r["years"] |= set(years)
        if source not in r["sources"]:
            r["sources"].append(source)
        if basis:
            r["basis"].append(basis)
        for y in years:
            if title:
                r["titles"].setdefault(y, title)

    for src, fn in (("cc", "roster-cc.json"), ("ia", "roster-ia.json")):
        f = HERE / fn
        if not f.exists():
            continue
        for s, p in json.loads(f.read_text()).items():
            name = (p.get("names") or [s.replace("-", " ").title()])[0]
            yrs = sorted(int(y) for y, t in (p.get("titles") or {}).items() if investing(t))
            if yrs:
                add(name, src, yrs, f"archived people page ({src}) with an investing title in {yrs[0]}-{yrs[-1]} "
                                    f"({'; '.join(f'{y}: {t}' for y, t in p['titles'].items())})",
                    p["titles"].get(str(yrs[-1]), ""))

    team = json.loads((P.site / "team-pages.json").read_text())["rows"]
    current = set()
    for t in team:
        if not t.get("published"):
            continue
        if set(t.get("units") or []) & {"Investors", "Leadership"} and investing(t.get("title") or ""):
            add(t["name"], "site-team", [THIS_YEAR], f"{t.get('title')} on the live team", t.get("title") or "")
            current.add(slug_of(t["name"]))
    comps = json.loads((P.site / "company-list.json").read_text())["rows"]
    panel = collections.Counter(n for c in comps for n in (c.get("partners") or []))
    for n, k in panel.items():
        if slug_of(n) in current:
            add(n, "site-panel", [THIS_YEAR], f"NEA deal team or board member on {k} live portfolio entries")

    rows = []
    for s, r in sorted(people.items()):
        ys = sorted(r["years"])
        rows.append({"slug": s, "name": r["name"], "years_seen": ys, "first_seen": ys[0], "last_seen": ys[-1],
                     "snapshots": len(ys), "sources": r["sources"], "title": r["titles"].get(ys[-1], ""),
                     "basis": "; ".join(dict.fromkeys(r["basis"]))})
    write_atomic(OUT, json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(len(rows), "people ->", OUT.relative_to(ROOT))
    for r in rows:
        print(f"  {r['name']:28} {r['first_seen']}-{r['last_seen']} ({r['snapshots']}) {','.join(r['sources'])} | {r['title']}")


if __name__ == "__main__":
    main()
