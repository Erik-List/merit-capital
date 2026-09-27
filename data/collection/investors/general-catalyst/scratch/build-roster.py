#!/usr/bin/env python3
"""Build General Catalyst's roster for the Form D sweep from first-party sources.

Sources, unioned into sources/wayback/partner-roster.json in partner-roster.py's
shape ({slug, name, years_seen, first_seen, last_seen, snapshots, sources}):

  site-team   the live "Investment Team" department of /team (63 people),
              every title: the grid names associates and principals as deal
              investors too, so the title is no filter here. The other
              departments (Wealth Management, GC Institute, HATCo, Percepta,
              Advisors, operations) hold no seat for the funds and are left
              out; an Advisor is an outside executive.
  site-card   every deal investor a portfolio card or company page names (the
              firm's own attribution map), whatever the department, including
              people the live team no longer lists.
  cdx         archived people pages with capture-year windows, when
              scratch/roster-cdx.json exists (partner-roster.py's output). This
              is the only source that dates a departure.
  history     the founders (Joel Cutler and David Fialkow, 2000); the merged
              teams from their combination dates (La Famiglia 2023-10-16,
              Venture Highway 2024-06-19; a seat such a person held BEFORE that
              date is the earlier firm's, T4, and the judge dates it).

One person, one entry: name variants fold onto one slug with the union window.

Usage: python3 data/collection/investors/general-catalyst/scratch/build-roster.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("general-catalyst")
OUT = P.wayback / "partner-roster.json"
CDX = P.scratch / "roster-cdx.json"
THIS_YEAR = 2026

VARIANTS = {
    "nat-levy-westhead": "nat-levy-westhead",
}
FILED_NAME: dict[str, str] = {}
# start year at the firm, where the firm's own history dates it
START = {"joel-cutler": 2000, "david-fialkow": 2000}
MERGED = {"jeannette-zu-furstenberg": 2023, "judith-dada": 2023, "neeraj-arora": 2024, "samir-sood": 2024}


def slug_of(name: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"\(.*?\)", " ", s.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return VARIANTS.get(s, s)


def main() -> None:
    team = json.load(open(P.site / "team-pages.json"))["rows"]
    comps = json.load(open(P.site / "company-pages.json"))["rows"]
    people: dict[str, dict] = {}

    def add(name: str, source: str, years: set[int], basis: str, title: str = "") -> None:
        s = slug_of(name)
        if not s or "-" not in s:
            return
        r = people.setdefault(s, {"slug": s, "name": FILED_NAME.get(s, re.sub(r"\s*\(.*?\)\s*", " ", name).strip()),
                                  "site_name": name, "years": set(), "sources": [], "basis": [], "title": ""})
        r["years"] |= years
        if source not in r["sources"]:
            r["sources"].append(source)
        if basis:
            r["basis"].append(basis)
        r["title"] = r["title"] or title

    live = {slug_of(t.get("name") or ""): t for t in team}
    for t in team:
        if t.get("group") != "Investment Team":
            continue
        s = slug_of(t["name"])
        start = START.get(s) or MERGED.get(s)
        yrs = set(range(start, THIS_YEAR + 1)) if start else {THIS_YEAR}
        add(t["name"], "site-team", yrs, f"{t.get('title') or 'no title'} on the live team (Investment Team)", t.get("title") or "")

    by_person: dict[str, int] = {}
    for c in comps:
        for n in c.get("partners") or []:
            by_person[n] = by_person.get(n, 0) + 1
    for n, k in by_person.items():
        s = slug_of(n)
        t = live.get(s)
        start = START.get(s) or MERGED.get(s)
        yrs = set(range(start, THIS_YEAR + 1)) if start else {THIS_YEAR}
        where = (f"on the live team ({t.get('group') or 'no department'})" if t
                 else "NOT on the live team page (departed or unlisted; departure undated)")
        add(n, "site-card", yrs, f"named as deal investor on {k} portfolio cards; {where}", (t or {}).get("title") or "")

    for s, y in START.items():
        nm = " ".join(w.capitalize() for w in s.split("-"))
        add(nm, "history", set(range(y, THIS_YEAR + 1)), f"co-founded the firm in {y}")
    for s, y in MERGED.items():
        if s in people:
            people[s]["basis"].append(f"joined with the {y} combination; earlier seats are the earlier firm's (T4)")

    if CDX.exists():
        for r in json.load(open(CDX)):
            yrs = set(r.get("years_seen") or [])
            if yrs:
                add(r.get("site_name") or r["name"], "cdx", yrs,
                    f"archived people pages {min(yrs)}-{max(yrs)} ({r.get('snapshots')} capture years)")

    out = []
    for s, r in sorted(people.items()):
        yrs = sorted(r["years"])
        out.append({"slug": s, "name": r["name"], "site_name": r["site_name"], "years_seen": yrs,
                    "first_seen": yrs[0], "last_seen": yrs[-1], "snapshots": len(yrs),
                    "sources": r["sources"], "title": r["title"], "basis": "; ".join(dict.fromkeys(r["basis"]))})
    P.wayback.mkdir(parents=True, exist_ok=True)
    write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"roster: {len(out)} people -> {OUT.relative_to(ROOT)}")
    print("  sources:", {k: sum(1 for r in out if k in r["sources"]) for k in ("site-team", "site-card", "cdx", "history")})
    print("  not on the live team:", [r["name"] for r in out if "site-team" not in r["sources"] and "history" not in r["sources"]])


if __name__ == "__main__":
    main()
