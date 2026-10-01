#!/usr/bin/env python3
"""Curate sources/wayback/partner-roster.json: the investing people only.

The archived team pages (2020-2026, scratch/team-archive.json) mix investors
with finance, legal, talent, events, investor relations and the advisory
board. A person enters the sweep roster when any archived position is an
investing title (decisions.md D4). The 2014-2019 site carried no team page,
so partners who left before 2020 come from PRE_2020 with a press or filing
basis; their windows are deliberately wide, because a wide window only adds
candidates the judge then rules on, while a narrow one hides a deal.
"""
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parent.parent
ARCH = INV / "scratch" / "team-archive.json"
OUT = INV / "sources" / "wayback" / "partner-roster.json"

INVESTING = re.compile(
    r"\b(partner|principal|associate|analyst|investment director|founder)\b", re.I)
NOT_INVESTING = re.compile(
    r"investor relations|finance|cfo|counsel|legal|compliance|talent|people|events|"
    r"assistant|engineer|it &|marketing|communications|cco|coo|special projects|"
    r"business development|capital markets|chief of staff|former|ceo|professor|"
    r"journalist|director,|president", re.I)
# one person under two archive slugs -> the slug kept
SAME = {"mika-salmi-2": "mika-salmi"}
# partners and principals not on any archived team page (no team page 2014-2019)
PRE_2020 = [
    ("Dharmash Mistry", 2015, 2019, "Partner; 'A former Partner at Balderton, Lakestar & LGT Lightstone ... investments including Revolut, Glovo, MessageBird, Infarm, Blockchain.com' (LEO Holdings V Corp S-1, 2021-03-15, EDGAR full-text sweep)"),
    ("Mona ElIsa", 2014, 2018, "Partner, New York office (press; the 2018-2019 homepage lists a New York presence)"),
    ("Raj Ramanandi", 2018, 2020, "Partner, London (press)"),
    ("Luis Shemtov", 2017, 2021, "Principal (press)"),
    ("Henrik Persson", 2013, 2016, "Partner, London: designated member of Lakestar Advisors UK LLP from its incorporation on 2014-11-13 to 2016-06-30 (Companies House OC396445, sources/registers/)"),
]
# tenure starts the archive cannot see (the team page first appears in 2020)
EARLIER = {
    "klaus-hommels": (2012, "Founder (the firm's own site: founded 2012)"),
    "nicolas-brand": (2013, "'spent a decade as a Partner at Lakestar' (BSTR Holdings S-4, 2026-05-14); on the 2020-2023 team pages"),
    "manu-gupta": (2013, "Partner from Lakestar I (press); on the 2020 team page"),
    "michael-stuenkel": (2013, "Partner; signatory of Lakestar Advisors GmbH 2017-2020 (Zefix)"),
    "christoph-schuh": (2015, "Partner (press); on the 2020-2026 team pages"),
    "oliver-heimes": (2016, "Partner (press); on the 2020-2026 team pages; signatory of Lakestar Advisors GmbH from 2024 (Zefix)"),
    "stephen-nundy": (2018, "Partner & CTO (press); on the 2020-2025 team pages"),
    "mathias-haniel": (2017, "Principal, then Partner (press); on the 2020-2023 team pages"),
    "georgia-watson": (2018, "joined as an associate (press); Principal 2022, Partner 2024 on the team pages"),
}


def main() -> None:
    ppl = json.loads(ARCH.read_text())
    merged: dict[str, dict] = {}
    for p in ppl:
        slug = SAME.get(p["slug"], p["slug"])
        m = merged.setdefault(slug, {"slug": slug, "name": p["name"], "positions": {}, "years": set(),
                                     "groups": set()})
        m["years"].update(p["years"])
        m["groups"].update(p["groups"])
        for k, v in p["positions"].items():
            m["positions"].setdefault(k, []).extend(v)
    roster = []
    for slug, m in sorted(merged.items()):
        titles = list(m["positions"])
        inv = [t for t in titles if INVESTING.search(t) and not NOT_INVESTING.search(t)]
        if not inv or "advisor" in m["groups"] - {"team"} and "team" not in m["groups"] and slug != "sam-gyimah":
            continue
        years = sorted(m["years"])
        first = years[0]
        basis = "; ".join(f"{t} ({min(d)[:4]}-{max(d)[:4]})" for t, d in m["positions"].items())
        sources = ["lakestar.com/team 2020-2026 (Common Crawl captures; scratch/team-archive.json)"]
        if slug in EARLIER:
            first, why = EARLIER[slug]
            sources.append(why)
        ys = list(range(first, years[-1] + 1))
        roster.append({"slug": slug, "name": m["name"], "years_seen": ys, "first_seen": ys[0],
                       "last_seen": ys[-1], "snapshots": len(years), "sources": sources,
                       "basis": basis})
    for name, a, b, why in PRE_2020:
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        roster.append({"slug": slug, "name": name, "years_seen": list(range(a, b + 1)),
                       "first_seen": a, "last_seen": b, "snapshots": 0, "sources": [why],
                       "basis": "not on an archived team page (the 2014-2019 site had none); window from press, wide on purpose"})
    OUT.write_text(json.dumps(sorted(roster, key=lambda r: r["slug"]), indent=1, ensure_ascii=False) + "\n")
    print(f"{len(roster)} investing people -> {OUT.relative_to(INV)}")
    for r in sorted(roster, key=lambda r: r["slug"]):
        print(f"  {r['name']:26s} {r['first_seen']}-{r['last_seen']}  {r['basis'][:90]}")


if __name__ == "__main__":
    main()
