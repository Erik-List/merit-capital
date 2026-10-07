#!/usr/bin/env python3
"""Curate sources/wayback/partner-roster.json for Earlybird.

Three sources, unioned per person (COLLECTION.md s5 layer 2, s8: one entry per
person with the union window and its basis):

1. The Internet Archive's own index of the firm's team pages, 2001-2013
   (scratch/cdx/earlybird-com-urlkeys.json, one CDX query, 2026-10-06): each
   /en|de/team/<office>/persons/<name> and /en/team/tech|health-tech/<name>.html
   page carries its first and last capture year, which is the person's window
   on the site ("capture-year tenure windows are roster evidence").
2. The 2014-2024 site had no per-person URLs; those years come from the
   archived homepage and /team captures (sources/wayback/team-years.json,
   written by scratch/eb_archive.py) where they exist.
3. The live team of both sites (sources/site/team-2026.json,
   team-health-2026.json), investment people only.

Advisory boards (adv_board_*, ab_*, medical_adv_board,
international_advisory_group, advisory-group), operations staff and the
Catalysts are advisers or staff, never deal partners, and are left out so their
names cannot attribute a Form D seat (decisions.md D7). Digital East's partners
are kept, marked lineage 'digital-east' in the basis: a Form D seat of theirs
is a Digital East Fund position (decisions.md D2) and the row it creates is
partitioned, not lost.
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_GROUPS = re.compile(
    r"adv_board|ab_usa|ab_europe|medical_adv|advisory|operations|menlo_park$|"
    r"palo_alto$|paloalto$")
NOT_PEOPLE = {
    "index", "team", "hamburg", "munich", "persons", "berlin", "istanbul",
    "milan", "italy", "germany", "tech", "health-tech", "operations",
    "partners", "header", "nav_pfeil", "nav_sub", "buero_hamburg",
    "buero_paloalto", "buero_ab_usa", "text_advisory_board", "bay-city-capital",
    "function.include", "_on", "_off", "health-tech_232", "health-tech_234",
    "advisory-group", "advisory-gruppe", "adv_board_usa", "medical_adv_board",
    "menlo_park", "palo_alto", "paloalto",
}
# one person, several spellings on the old site
ALIAS = {
    "christian-g-nagel": "christian-nagel", "dr-christian-nagel": "christian-nagel",
    "dr-hendrik-brandis": "hendrik-brandis", "hendrik-brandis2": "hendrik-brandis",
    "rolf-mathies2": "rolf-mathies", "rolf-mathies-46": "rolf-mathies",
    "katrin-haskamp2": "katrin-haskamp", "marc-canabou2": "marc-canabou",
    "ciaran-o-leary": "ciaran-oleary", "jason-d-whitmire": "jason-whitmire",
    "jason-d-withmire": "jason-whitmire", "dr-marion-jung": "marion-jung",
    "steve-j-ciesinski": "steve-ciesinski", "michael-c-schuster": "michael-schuster",
    "elena-wholz": "elena-wholz",
}
NAMES = {
    "christian-nagel": "Christian Nagel", "hendrik-brandis": "Hendrik Brandis",
    "ciaran-oleary": "Ciarán O'Leary", "jason-whitmire": "Jason Whitmire",
    "evren-ucok": "Evren Ucok", "cem-sertoglu": "Cem Sertoglu",
    "maurice-van-riek": "Maurice van Riek", "daniela-von-wedel": "Daniela von Wedel",
    "steve-ciesinski": "Steve Ciesinski", "michael-schuster": "Michael Schuster",
}
DIGITAL_EAST = {"cem-sertoglu", "evren-ucok", "mehmet-atici"}
# operations people who sat under hamburg/persons on the old site
STAFF = {"daniela-von-wedel", "johanna-berghofer", "elena-wholz", "matias-collan"}

# Curated additions for the years with no per-person URL (2014-2024) and for
# the people the firm's own records name as deal partners. Each line is a
# ruling with its basis (COLLECTION.md s5: "one ruling per name").
CURATED = [
    # slug, name, first, last, basis
    ("fabian-heilemann", "Fabian Heilemann", 2016, 2021,
     "Partner 2016-2021; deal partner on the firm's own company pages (Sennder / Everoad 2017, Inkitt 2015, Service Partner One); left to found AENU in 2021"),
    ("ferry-heilemann", "Ferry Heilemann", 2016, 2020,
     "Partner alongside Fabian Heilemann from 2016 (the brothers joined together); left with the founding of AENU"),
    ("tim-rehder", "Tim Rehder", 2016, 2026,
     "General Partner, earlybird.com/members 2026-10-06; deal partner on the firm's company pages from 2017"),
    ("andre-retterath", "Andre Retterath", 2017, 2026,
     "General Partner, earlybird.com/members 2026-10-06; deal partner on the firm's company pages from 2018"),
    ("paul-klemm", "Paul Klemm", 2018, 2026,
     "General Partner, earlybird.com/members 2026-10-06; deal partner on the firm's company pages from 2019"),
    ("moritz-belling", "Moritz Belling", 2021, 2026,
     "Principal, earlybird.com/members 2026-10-06; deal team on the firm's company pages"),
    ("laura-waldenstrom", "Laura Waldenstrom", 2021, 2026,
     "Principal, earlybird.com/members 2026-10-06"),
    ("akash-bajwa", "Akash Bajwa", 2022, 2026,
     "Principal, earlybird.com/members 2026-10-06"),
    ("nina-mayer", "Nina Mayer", 2020, 2026,
     "Principal, earlybird.com/members 2026-10-06 (the site also spells her Nina Meyer)"),
    ("laurin-class", "Laurin Class", 2022, 2025,
     "deal team on the firm's company pages 2022-2025; not on the 2026 team list"),
    ("ferdinand-dansard", "Ferdinand Dansard", 2023, 2025,
     "deal team on the firm's company pages 2023-2025; not on the 2026 team list"),
    ("alina-bassi", "Alina Bassi", 2026, 2026,
     "Principal, earlybird.com/members 2026-10-06 (joined 2026 per the firm's post)"),
    ("stefano-gonelle-ribas", "Stefano Gonelle Ribas", 2025, 2026,
     "Investment Team, earlybird.com/members 2026-10-06"),
    ("umberto-belluzzo", "Umberto Belluzzo", 2026, 2026,
     "Investment Team, earlybird.com/members 2026-10-06"),
    ("paul-christoph-altunay", "Paul-Christoph Altunay", 2026, 2026,
     "Investment Team, earlybird.com/members 2026-10-06"),
    ("frederic-du-bois-reymond", "Frédéric du Bois-Reymond", 2019, 2026,
     "Venture Partner, earlybird.com/members 2026-10-06; Earlybird-X (the university fund, 2019-)"),
    ("philipp-semmer", "Philipp Semmer", 2019, 2024,
     "Earlybird-X partner (the university fund, 2019-); not on the 2026 team list"),
    ("michael-schmitt", "Michael Schmitt", 2019, 2024,
     "Earlybird-X partner (the university fund, 2019-); not on the 2026 team list"),
    ("dan-lupu", "Dan Lupu", 2012, 2026,
     "lineage digital-east 2012-2024 (the firm's own post: 'a Partner with the Earlybird-licensed Digital East Fund'); Venture Partner at Earlybird itself from 2025, earlybird.com/members 2026-10-06"),
    ("cem-sertoglu", "Cem Sertoglu", 2012, 2024,
     "lineage digital-east: Istanbul team page 2012-2013; Digital East Fund partner until the 2024 rebrand to Bek Ventures"),
    ("evren-ucok", "Evren Ucok", 2012, 2024,
     "lineage digital-east: Istanbul team page 2012-2013; Digital East Fund partner"),
    ("ravi-kurani", "Ravi Kurani", 2016, 2019,
     "named on the one-page site from the 2016-12 capture; Principal on the archived /team page 2018-2019"),
    ("mehmet-atici", "Mehmet Atici", 2014, 2024,
     "lineage digital-east: Digital East Fund, now Managing Partner of Bek Ventures (Vestbee 2024-11-13)"),
    # health
    ("thom-rasche", "Thom Rasche", 2003, 2026, "Partner, health.earlybird.com/members 2026-10-06; team pages from 2003"),
    ("john-yianni", "John Yianni", 2011, 2026, "Partner, health.earlybird.com/members 2026-10-06; team pages from 2011"),
    ("lionel-carnot", "Lionel Carnot", 2012, 2026, "Partner, health.earlybird.com/members 2026-10-06; team pages from 2012"),
    ("florent-gros", "Florent Gros", 2021, 2026, "Partner, health.earlybird.com/members 2026-10-06"),
    ("rainer-christine", "Rainer Christine", 2014, 2026, "Partner (Health I Fund and Health Opportunities Fund), health.earlybird.com/members 2026-10-06"),
    ("rabab-nasrallah", "Rabab Nasrallah", 2019, 2026, "Partner, health.earlybird.com/members 2026-10-06"),
    ("christoph-massner", "Christoph Massner", 2017, 2026, "Partner, health.earlybird.com/members 2026-10-06"),
    ("alexander-mueller", "Alexander Müller", 2016, 2026, "Operating Partner, health.earlybird.com/members 2026-10-06"),
    ("fabian-scheugenpflug", "Fabian Scheugenpflug", 2022, 2026, "Principal, health.earlybird.com/members 2026-10-06"),
]
# partners whose window the old pages end in 2013 only because the site lost
# its per-person URLs then; their last year comes from the record named here
EXTEND = {
    # the 2014-2017 one-page site named the team without per-person URLs
    # (Common Crawl captures of earlybird.com/, 2014-07 to 2017-12)
    "ciaran-oleary": (2015, "named on the one-page site through the 2015-07 capture, gone by 2015-11"),
    "jason-whitmire": (2017, "named on the one-page site through the 2017-12 capture"),
    "maximilian-claussen": (2014, "named on the one-page site in the 2014-07 capture, gone by 2014-12"),
    "konstantin-guericke": (2015, "named on the one-page site through the 2015-11 capture, gone by 2016-07"),
    "christian-nagel": (2026, "Co-Founder and General Partner, earlybird.com/members 2026-10-06"),
    "hendrik-brandis": (2026, "Co-Founder and General Partner, earlybird.com/members 2026-10-06"),
    "rolf-mathies": (2023, "Co-Founder; health.earlybird.com/members lists him 'In Memoriam' (2026-10-06)"),
    "roland-manger": (2026, "Co-Founder; home-desk partner to 2012, then a partner of the Digital East Fund (lineage digital-east 2013-2024); quoted as 'Co-Founder of Earlybird' in the firm's E2D release of 2026-06-18"),
}


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def from_cdx() -> dict[str, dict]:
    rows = json.loads((ROOT / "scratch/cdx/earlybird-com-urlkeys.json").read_text())[1:]
    people: dict[str, dict] = defaultdict(lambda: {"years": set(), "n": 0, "groups": set()})
    for original, ts, ets, gc, _sc, _mt in rows:
        p = re.sub(r"^https?://(www\.)?earlybird\.com(:80)?", "", original).split("?")[0].lower()
        if not re.match(r"/(en|de|it)/team", p) or re.search(r"\.(gif|jpg|png|css|js)$", p):
            continue
        parts = [x for x in p.strip("/").split("/") if x]
        if len(parts) < 4:
            continue
        last = re.sub(r"\.html?$", "", parts[-1])
        group = "/".join(parts[2:-1])
        if last in NOT_PEOPLE or SKIP_GROUPS.search(group) or "document." in last:
            continue
        slug = slugify(last.replace("_", "-"))
        slug = ALIAS.get(slug, slug)
        if slug in STAFF:
            continue
        d = people[slug]
        d["years"].update(range(int(ts[:4]), int(ets[:4]) + 1))
        d["n"] += int(gc)
        d["groups"].add(group)
    return people


def main() -> None:
    people = from_cdx()
    out: dict[str, dict] = {}
    for slug, d in people.items():
        name = NAMES.get(slug) or " ".join(w.capitalize() for w in slug.split("-"))
        years = sorted(d["years"])
        out[slug] = {
            "slug": slug, "name": name, "years_seen": years,
            "first_seen": years[0], "last_seen": years[-1], "snapshots": d["n"],
            "sources": ["earlybird.com-team-page"],
            "basis": "team page(s) %s on earlybird.com, first captured %d, last %d (Internet Archive index)" % (
                ", ".join(sorted(d["groups"])), years[0], years[-1]),
        }
    for slug, name, first, last, basis in CURATED:
        r = out.get(slug)
        if r:
            r["first_seen"] = min(r["first_seen"], first)
            r["last_seen"] = max(r["last_seen"], last)
            r["years_seen"] = sorted(set(r["years_seen"]) | {first, last})
            r["sources"].append("curated")
            r["basis"] += "; " + basis
            r["name"] = name
        else:
            out[slug] = {"slug": slug, "name": name, "years_seen": sorted({first, last}),
                         "first_seen": first, "last_seen": last, "snapshots": 0,
                         "sources": ["curated"], "basis": basis}
    for slug, (last, basis) in EXTEND.items():
        r = out[slug]
        r["last_seen"] = max(r["last_seen"], last)
        r["years_seen"] = sorted(set(r["years_seen"]) | {last})
        r["sources"].append("curated")
        r["basis"] += "; " + basis
    # archived 2018-2024 /team captures (eb_archive.py): the site's own Team tag
    # and title decide who is an investing person of the home funds
    ty = ROOT / "sources/wayback/team-years.json"
    if ty.exists():
        t = json.loads(ty.read_text())
        # Only people who held a partner or principal title sit on boards and sign
        # as related persons. Analysts, associates and "Investment Team" members
        # are left off: on the first build two of them (James Bennett, Junkai Zhu
        # read as "Jun Zhu") drew 20 homonym issuers from the Form D sweep.
        invest_title = re.compile(r"(?i)partner|principal")
        staff_title = re.compile(r"(?i)assistant|finance|cfo|account|controller|office|talent|"
                                 r"marketing|communications|engineer|investor relations|risk|people|"
                                 r"event|content|product manager|data strategist|operations|vision lab")
        for raw_name, years in t.get("people", {}).items():
            det = t["detail"][raw_name]
            name = re.sub(r"^(Dr\.|Prof\.)\s+", "", raw_name)
            name = re.sub(r",\s*PhD$|\s*\(In Memoriam\)$", "", name)
            name = {"Mehmed Atici": "Mehmet Atici", "Nina Mayer (Rinke)": "Nina Mayer",
                    "Nina Rinke": "Nina Mayer", "Oguzhan \u00d6zer": "Oguzhan Ozer"}.get(name, name)
            slug = ALIAS.get(slugify(name), slugify(name))
            slug = {"alexander-muller": "alexander-mueller"}.get(slug, slug)
            tags = " ".join(det["team_tags"].values())
            titles = " ".join(det["titles"].values())
            r = out.get(slug)
            if not r:
                if "Digital East" in tags or "Operations" in tags or staff_title.search(titles) \
                        or not invest_title.search(titles):
                    continue
                desk = "Earlybird-X" if ("UNI-X" in tags or "Earlybird-X" in tags) else (
                    "Health" if "Health" in tags else "Earlybird")
                r = out[slug] = {"slug": slug, "name": name, "years_seen": [], "first_seen": min(years),
                                 "last_seen": max(years), "snapshots": 0, "sources": [],
                                 "basis": "%s team, archived earlybird.com/team %d-%d (%s)" % (
                                     desk, min(years), max(years),
                                     ", ".join(sorted(set(det["titles"].values()))))}
            r["years_seen"] = sorted(set(r["years_seen"]) | set(years))
            r["first_seen"] = min(r["first_seen"], min(years))
            r["last_seen"] = max(r["last_seen"], max(years))
            r["snapshots"] += len(years)
            if "archived-team-capture" not in r["sources"]:
                r["sources"].append("archived-team-capture")
    for slug in DIGITAL_EAST:
        if slug in out and "lineage digital-east" not in out[slug]["basis"]:
            out[slug]["basis"] = "lineage digital-east; " + out[slug]["basis"]
    roster = sorted(out.values(), key=lambda r: (r["first_seen"], r["slug"]))
    dst = ROOT / "sources/wayback/partner-roster.json"
    dst.write_text(json.dumps(roster, indent=1, ensure_ascii=True) + "\n")
    print(f"{len(roster)} people -> {dst.relative_to(ROOT)}")
    for r in roster:
        print(f"  {r['first_seen']}-{r['last_seen']}  {r['name']:28s} {r['sources']}")


if __name__ == "__main__":
    main()
