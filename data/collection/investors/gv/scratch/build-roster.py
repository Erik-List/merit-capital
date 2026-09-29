#!/usr/bin/env python3
"""Build GV's roster for the Form D sweep from first-party sources, into
sources/wayback/partner-roster.json in partner-roster.py's shape
({slug, name, years_seen, first_seen, last_seen, snapshots, sources}) plus title and basis.

Sources:
  cc          archived people pages on googleventures.com and gv.com (scratch/roster-cc.json,
              cc-roster.py), read per capture year: a year counts only when the page's own
              title that year is an investing title (Kevin Rose is General Partner in 2013-14
              and "Advisor to Google Ventures" from 2015; Rich Miner General Partner to 2016,
              "GV Advisor" from 2017), or the 2012 page puts the person on the Investing Team.
  listing     the deal partner the archived listings name per company (2013-15 tooltips,
              2016-19 data-investors): a person named as deal partner in a year was investing
              that year.
  site-team   the live CMS Investing Team (sources/site/team-pages.json), year 2026.
  site-panel  the live /portfolio docs' deal partners (current staff only), year 2026.

Left out: design, UX research, engineering, recruiting and talent, marketing and communications
partners, administrative, finance and legal staff, and the "GV Adviser" / "Advisor to Google
Ventures" group: none of those roles sits on a board for the firm, and a common name among them
buys only false Form D matches. An engineering or legal title in one year does not stop a later
investing title from counting (Adam Ghobarah, Erik Nordlander, Vidu Shanmugarajah).

One person, one entry: name variants fold onto one slug with the union window (VARIANTS).
Usage: python3 build-roster.py
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("gv")
OUT = P.wayback / "partner-roster.json"
CC = P.scratch / "roster-cc.json"
THIS_YEAR = 2026
INVESTING = re.compile(r"managing partner|general partner|^partner$|^partner,? (?!portfolio|startup lab|chief of)"
                       r"|principal|^associate$|venture partner|^president|\bceo\b|investor|entrepreneur in residence"
                       r"|investing", re.I)
NOT_INVESTING = re.compile(r"design|research|engineering|recruit|talent|marketing|communications|administrative|"
                           r"finance|financial|legal|counsel|advis|product partner|portfolio programs|startup lab|"
                           r"data analyst|accounting|controller|operations|business partner", re.I)
VARIANTS = {"m-g-siegler": "mg-siegler", "feng-yuan-xu": "feng-xu", "david-t-lu": "david-lu",
            "avid-larizadeh-duggan": "avid-larizadeh", "nathan-amchan": "nate-amchan",
            "secretary-ray-mabus": "ray-mabus", "salvador-diaz": "sal-diaz"}
# platform staff whose later pages carry a bare "Partner" title: their first archived title says what the
# role was (Laura Melahn "Marketing Partner", Rick Klau "Partner, Startup Lab", Tracie Rotter "Partner,
# Portfolio Programs", Brian Bendett "Data Analyst"), and none sits on a board for the firm
PLATFORM = {"laura-melahn", "rick-klau", "tracie-rotter", "brian-bendett"}
# the name the sweep should match on (the filed form), where the site's display differs
FILED_NAME = {"mg-siegler": "MG Siegler", "avid-larizadeh": "Avid Larizadeh Duggan"}


def slug_of(name: str) -> str:
    import unicodedata
    folded = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", folded.lower().replace(".", "")).strip("-")
    return VARIANTS.get(s, s)


def investing(title: str) -> bool:
    return bool(title) and bool(INVESTING.search(title)) and not NOT_INVESTING.search(title)


def main() -> None:
    people: dict[str, dict] = {}

    def add(name, source, years, basis, title=""):
        name = re.sub(r"\s+", " ", name or "").strip()
        s = slug_of(name)
        if not s or "-" not in s or s in PLATFORM:
            return
        r = people.setdefault(s, {"slug": s, "name": FILED_NAME.get(s, name), "years": set(), "sources": [],
                                  "basis": [], "titles": {}})
        r["years"] |= set(years)
        if source not in r["sources"]:
            r["sources"].append(source)
        if basis:
            r["basis"].append(basis)
        if title:
            for y in years:
                r["titles"].setdefault(y, title)

    # cc: per-year titles from the archived people pages
    cc = json.loads(CC.read_text()) if CC.exists() else {}
    for s, p in cc.items():
        name = (p["names"] or [s.replace("-", " ").title()])[0]
        yrs = []
        for y, t in p["titles"].items():
            if investing(t):
                yrs.append(int(y))
        for y, g in p["groups"].items():
            if g == "Investing Team" and not NOT_INVESTING.search(p["titles"].get(y, "")):
                yrs.append(int(y))
        yrs = sorted(set(yrs) - set(p.get("former_years") or []))
        if yrs:
            add(name, "cc", yrs, f"archived people page with an investing title in {yrs[0]}-{yrs[-1]} "
                                 f"({'; '.join(f'{y}: {t}' for y, t in p['titles'].items())})",
                p["titles"].get(str(yrs[-1]), ""))

    # listing: the deal partner the archived listings name per company, by year
    by_person = collections.defaultdict(set)
    for f in sorted(P.wayback.glob("parsed/*.json")):
        y = int(f.stem)
        for r in json.loads(f.read_text()):
            # the 2022+ CMS listings (era E) keep a departed partner attached to his companies for years (Andy
            # Wheeler and MG Siegler to 2024), so only the 2013-21 eras, whose pages were rebuilt per release, date a window
            if r.get("era") not in ("C", "D"):
                continue
            for field in r.get("partners") or []:
                # a 2013-15 tooltip lists co-partners in one field ("Bill Maris, David Krane")
                for n in re.split(r"\s*(?:,|&|\band\b)\s*", field or ""):
                    if n and len(n) < 40:
                        by_person[n].add(y)
    for n, yrs in by_person.items():
        add(n, "listing", sorted(yrs), f"named deal partner on the archived listing in {min(yrs)}-{max(yrs)}")

    # live CMS: the Investing Team and the /portfolio deal partners
    team = json.loads((P.site / "team-pages.json").read_text())["rows"]
    for t in team:
        # the CMS files a finance partner under the Investing Team (Zach Brauer, "Senior Finance Partner"):
        # the title filter applies to live staff as it does to the archive
        if "Investing Team" in (t.get("group") or "") and not NOT_INVESTING.search(t.get("title") or ""):
            add(t["name"], "site-team", [THIS_YEAR], f"{t.get('title') or 'no title'} on the live Investing Team",
                t.get("title") or "")
    comps = json.loads((P.site / "company-list.json").read_text())["rows"]
    panel = collections.Counter(n for c in comps for n in (c.get("partners") or []))
    for n, k in panel.items():
        add(n, "site-panel", [THIS_YEAR], f"deal partner on {k} live /portfolio docs")

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
