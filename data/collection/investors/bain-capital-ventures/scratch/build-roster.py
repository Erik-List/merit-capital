#!/usr/bin/env python3
"""Build Bain Capital Ventures' roster for the Form D sweep from first-party sources.

Sources, unioned into sources/wayback/partner-roster.json in partner-roster.py's
shape ({slug, name, years_seen, first_seen, last_seen, snapshots, sources}):

  site-team   the live Investing Team (Sanity `team` docs in that group), every
              title: BCV's investing team is 18 people and all of them sit on
              boards or lead deals. The Hive (platform) and Operating Team
              groups are left out; their "Partner" titles are platform roles.
  site-panel  every person a portfolio doc links as its deal partner (the firm's
              own attribution map), whatever the group.
  fund-formd  the executive officers and directors named on the firm's OWN fund
              Form Ds (Bain Capital Venture Fund 2012 onward, the crypto funds),
              dated by the filing years. Kept only where another BCV source
              names the same person: the fund Form Ds also list Bain Capital-
              wide officers (group CFO, private-equity MDs) with no BCV seat.
  crypto      Bain Capital Crypto's investing partners (Stefan Cohen, Alex Evans,
              both on the crypto funds' Form Ds).
  cdx         archived people pages with capture-year windows
              (scratch/roster-cdx.json, partner-roster.py's output, copied there),
              the only source that dates a departure.
  old-team    names read from the 2002 to 2010 id-based team pages
              (scratch/roster-old.json, when present).

One person, one entry: name variants fold onto one slug with the union window
(the First Round rule), via VARIANTS.

Usage: python3 data/collection/investors/bain-capital-ventures/scratch/build-roster.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("bain-capital-ventures")
OUT = P.wayback / "partner-roster.json"
CDX = P.scratch / "roster-cdx.json"
OLD = P.scratch / "roster-old.json"
# first-capture slugs from the saved domain index: corroboration only (a
# fund-formd name with a BCV people page is kept), never a roster source
PROVISIONAL = P.scratch / "roster-cdx-provisional.json"
FUND = P.scratch / "fund-formd-persons.json"
THIS_YEAR = 2026

VARIANTS = {
    "michael-krupa": "michael-krupka",     # a typo on the 2012 fund Form D
    "mike-krupka": "michael-krupka",
    "matthew-harris": "matt-harris",
    "benjamin-nye": "ben-nye",
    "j-benjamin-nye": "ben-nye",
    "j-benjamin-h-nye": "ben-nye",
    "jeffrey-glass": "jeff-glass",
    "jeffrey-crisan": "jeff-crisan",
    "benjamin-holzman": "ben-holzman",
    "jeffrey-schwartz": "jeff-schwartz",
    "john-m-connolly": "john-connolly",
    "indy-guha": "indranil-guha",
    "andy-cleverdon": "andrew-cleverdon",
    "jeffrey-williams": "jeff-williams",
    "christina-melas": "christina-melas-kyriazi",
    "leslie-kurkjian-crowe": "leslie-crowe",
    "megan-panzer-kageleiry": "megan-kageleiry",
    "caroline-toch": "caroline-toch-docal",
    "todd-maclean": "todd-maclean",
}
# the name the sweep should match on (the filed form), where it differs
FILED_NAME = {
    "ben-nye": "Benjamin Nye",
    "jeff-glass": "Jeffrey Glass",
    "jeff-crisan": "Jeffrey Crisan",
    "jeff-schwartz": "Jeffrey Schwartz",
    "john-connolly": "John Connolly",
    "michael-krupka": "Michael Krupka",
    "indranil-guha": "Indranil Guha",
}
# starts no captured page dates (the archive reaches this site from 2009 on)
KNOWN_START = {"salil-deshpande": (2008, "joined BCV from Bay Partners in 2008 (his own 2013 page: 'Prior to BCV "
                                         "Salil spent seven years as General Partner at Bay Partners')")}
# titles that hold board seats or lead deals; associates and analysts are left out unless a
# company doc names them as deal partner (site-panel), because they sit on no board and a
# common name buys only false matches (the Insight rule)
SEAT = re.compile(r"managing director|^partner$|principal|vice president(?!,? (marketing|human|investor))|"
                  r"^director$|investor$|operating partner|venture partner|senior advisor|executive-in-residence|"
                  r"network investing|strategic investing|data-driven investing|seed fund program", re.I)
NOT_PEOPLE = re.compile(r"fellows$|^n/?a\b|llc$|l\.?p\.?$", re.I)


def slug_of(name: str) -> str:
    s = re.sub(r"\(.*?\)", " ", name.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return VARIANTS.get(s, s)


def main() -> None:
    team = json.load(open(P.site / "team-pages.json"))["rows"]
    comps = json.load(open(P.site / "company-pages.json"))["rows"]
    people: dict[str, dict] = {}

    def add(name: str, source: str, years: set[int], basis: str, title: str = "") -> None:
        name = re.sub(r"\s+", " ", name).strip()
        if not name or NOT_PEOPLE.search(name):
            return
        s = slug_of(name)
        if not s or "-" not in s:
            return
        r = people.setdefault(s, {"slug": s, "name": FILED_NAME.get(s, name.title() if name.isupper() else name),
                                  "site_name": name, "years": set(), "sources": [],
                                  "basis": [], "title": ""})
        r["years"] |= years
        if source not in r["sources"]:
            r["sources"].append(source)
        if basis:
            r["basis"].append(basis)
        r["title"] = r["title"] or title

    live = set()
    for t in team:
        live.add(slug_of(t["name"]))
        if "Investing Team" not in (t.get("group") or ""):
            continue
        add(t["name"], "site-team", {THIS_YEAR},
            f"{t.get('title') or 'no title'} on the live Investing Team (start year from the archive, when captured)",
            t.get("title") or "")

    by_person: dict[str, list[int]] = {}
    for c in comps:
        for n in c.get("partners") or []:
            if n:
                by_person.setdefault(n, []).append(int(c["invest_year"]) if str(c.get("invest_year") or "").isdigit() else 0)
    for n, ys in by_person.items():
        ys = [y for y in ys if y]
        yrs = set(range(min(ys), THIS_YEAR + 1)) if ys else {THIS_YEAR}
        add(n, "site-panel", yrs,
            f"deal partner on {len(ys)} portfolio docs (earliest invest year {min(ys) if ys else 'n/a'}); "
            + ("on the live team" if slug_of(n) in live else "NOT on the live team"))

    if FUND.exists():
        for acc, h in json.load(open(FUND)).items():
            issuer = h["issuer"]
            # anchored: a third-party feeder's name CONTAINS the fund's
            # ("Brown Advisory Investors 2016 - Bain Capital Venture Fund 2016")
            if not re.match(r"bain capital venture|bain capital crypto|bcv (20|21|coinv|crypto|xi|emerge)", issuer, re.I):
                continue
            y = int(h["q"][:4])
            for first, last, rel, clar in h["persons"]:
                add(f"{first} {last}", "fund-formd", {y},
                    f"related person ({rel or 'officer'}) on the firm's own Form D {acc} ({issuer}, {h['q'][:6]})")

    add("Stefan Cohen", "crypto", set(range(2021, THIS_YEAR + 1)),
        "Bain Capital Crypto co-founder and partner (fund launched 2022); on the crypto funds' Form Ds")
    add("Alex Evans", "crypto", set(range(2021, THIS_YEAR + 1)),
        "Bain Capital Crypto co-founder and partner; on the crypto funds' Form Ds")

    CC = P.scratch / "roster-cc.json"
    non_investing_live = {slug_of(t["name"]) for t in team
                          if t.get("group") and "Investing Team" not in t["group"]}
    if CC.exists():
        for r in json.load(open(CC)):
            yrs = set(r.get("years_seen") or [])
            titles = r.get("titles") or ([r["title"]] if r.get("title") else [])
            s = slug_of(r["name"])
            seat = [t for t in titles if SEAT.search(t.strip())]
            if not yrs or (not seat and s not in people) or s in non_investing_live:
                continue
            add(r["name"], "cc-pages", yrs,
                f"archived people pages (Common Crawl) {min(yrs)}-{max(yrs)}, titles {', '.join(titles) or 'none'}"
                + (f", joined per own bio {r['joined_bio']}" if r.get("joined_bio") else ""),
                seat[-1] if seat else "")
    for src, path in (("cdx", CDX), ("old-team", OLD)):
        if path.exists():
            for r in json.load(open(path)):
                yrs = set(r.get("years_seen") or [])
                if not yrs:
                    continue
                add(r.get("site_name") or r["name"], src, yrs,
                    f"archived people pages {min(yrs)}-{max(yrs)} ({r.get('snapshots') or len(yrs)} capture years)")

    for s_, (y, why) in KNOWN_START.items():
        if s_ in people:
            people[s_]["years"] |= set(range(y, min(people[s_]["years"]) + 1))
            people[s_]["basis"].append(why)

    # A fund Form D names the GP's officers, and on BCV's that includes Bain
    # Capital-wide officers (the group CFO, private-equity managing directors)
    # who hold no BCV seat: sweeping them would pull private-equity portfolio
    # companies into this base. A fund-formd name is kept only where a BCV
    # source corroborates it (a people page, a deal attribution, the crypto
    # team); the rest are written to the log with their reason.
    pages = {r["slug"] for r in json.load(open(PROVISIONAL))} if PROVISIONAL.exists() else set()
    alias = {"jeffrey-glass": "jeff-glass", "jeff-crisan": "jeff-crisan", "benjamin-nye": "ben-nye",
             "john-m-connolly": "john-connolly", "jeff-schwartz": "jeffrey-schwartz"}
    pages |= {alias.get(x, x) for x in pages}
    for s_, r in people.items():
        if r["sources"] == ["fund-formd"] and s_ in pages:
            r["sources"].append("people-page")
            r["basis"].append("a BCV people page exists for this slug in the archive (first capture only)")
    dropped = {s: r for s, r in people.items() if r["sources"] == ["fund-formd"]}
    for s in dropped:
        del people[s]
    if dropped:
        print("  fund-formd only, not swept:", ", ".join(r["name"] for r in dropped.values()))
    out = []
    for s, r in sorted(people.items()):
        yrs = sorted(r["years"])
        out.append({
            "slug": s, "name": r["name"], "site_name": r["site_name"],
            "years_seen": yrs, "first_seen": yrs[0], "last_seen": yrs[-1],
            "snapshots": len(yrs), "sources": r["sources"], "title": r["title"],
            "basis": "; ".join(dict.fromkeys(r["basis"])),
        })
    write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"roster: {len(out)} people -> {OUT.relative_to(ROOT)}")
    print("  sources:", {k: sum(1 for r in out if k in r["sources"])
                         for k in ("site-team", "site-panel", "fund-formd", "crypto", "cdx", "old-team")})


if __name__ == "__main__":
    main()
