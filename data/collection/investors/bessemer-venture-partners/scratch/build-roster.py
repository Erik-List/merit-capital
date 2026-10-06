#!/usr/bin/env python3
"""Build Bessemer's roster for the Form D sweep from first-party sources, into
sources/wayback/partner-roster.json in partner-roster.py's shape
({slug, name, years_seen, first_seen, last_seen, snapshots, sources}) plus title and basis.

Sources (all the firm's own site, archived or live):
  team-page   bvp.com/Team/<Name>.aspx (2008-2012) and bvp.com/team/<slug> (2012 on): the capture years of each
              person's own page, from the Common Crawl index (scratch/cc-index-raw.json) and, where it has been
              read, the Internet Archive index (scratch/cdx-map-bvp.com.json). The role is read off the page: the
              2008-2012 blurb ("is a Partner", "is an Analyst"), the 2017-18 group line ("Investment Team",
              "Operations Team", "Solutions Team", "Portfolio Team"), the 2019+ title line.
  team-list   the 2008 team listing (names only) for people whose own page was never captured.
  site-team   the live Sanity team (2026): role `investor`, and the alumni the CMS still carries with an investing
              title or with deals attributed to them.
  joined      "joined Bessemer in <year>" in the person's own blurb sets the first year where it is earlier than the
              first capture (a first capture dates the archive, not the hire).

Who counts (decisions.md D4, D6): partners, vice presidents, principals, directors and managing directors of the
India office, associates, analysts, investors, venture partners and operating partners (they sit on boards for the
funds). Left out: operations, finance, legal, talent, marketing, IT and platform staff, entrepreneurs- and
executives-in-residence (their companies are their own), operating advisors (70 on the live site: executives with
employers of their own), science advisors, summer staff. A common name among them buys only false Form D matches.
One person, one entry: name variants fold onto one slug with the union window (VARIANTS); tenure between the first
and last year seen is filled, since a missing capture year is an archive gap, not a departure.
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

P = Paths("bessemer-venture-partners")
OUT = P.wayback / "partner-roster.json"
THIS_YEAR = 2026

# slug variants of one person -> canonical slug
VARIANTS = {"robert-p-goodman": "bob-goodman", "robert-goodman": "bob-goodman", "stephen-kraus": "steve-kraus",
            "robert-stavis": "rob-stavis", "ed-colloton": "j-edmund-colloton", "chris-gabrieli": "christopher-gabrieli",
            "mac-cordrey-0": "mac-cordrey", "tali-vogelstein-0": "tali-vogelstein", "vinay-iyengar-0": "vinay-iyengar",
            "douglas-romanoff": "doug-romanoff", "mary-donofrio": "mary-d-onofrio", "ben-mathews": "ben-matthews",
            "derrick-t-l-lee": "derrick-lee", "mohammad-ibrahim-faruqi": "ibrahim-faruqi", "marla-jalbut-m-d": "marla-jalbut",
            "janelle-teng": "janelle-teng-wade", "g-felda-hardymon": "felda-hardymon", "subramanya-s-v": "subramanya-sv",
            "michael-droesch": "mike-droesch", "alexander-ferrara": "alex-ferrara", "kristina-shen-0": "kristina-shen"}
# the name as it is filed (Form D related persons), where the site's rendering would not match
FILED_NAME = {"bob-goodman": "Robert Goodman", "steve-kraus": "Stephen Kraus", "rob-stavis": "Robert Stavis",
              "j-edmund-colloton": "J. Edmund Colloton", "felda-hardymon": "G. Felda Hardymon",
              "christopher-gabrieli": "Christopher Gabrieli", "mary-d-onofrio": "Mary D'Onofrio",
              "derrick-lee": "Derrick Lee", "subramanya-sv": "Subramanya SV", "mac-cordrey": "Mac Cordrey",
              "janelle-teng-wade": "Janelle Teng", "marla-jalbut": "Marla Jalbut", "lance-co-ting-keh": "Lance Co Ting Keh"}

# Archived people who invested (read off their own pages, 2026-10-01; scratch/team-page-titles.json and the
# 2008-2012 blurbs). Operating partners are in: they take board seats for the funds.
INVESTING = set("""aakash-goel abhijeet-muzumdar adam-fisher alex-ferrara aman-kandola ambar-bhattacharyya amit-karp
anant-vidur-puri andrew-hedin andrew-walsh aneesha-raghunathan anna-khan ariel-sterman aviad-ariel ben-donald
ben-matthews bob-goodman brandon-saw brian-feinstein byron-deeter charles-birnbaum chini-krishnan chitresh-modi
christopher-gabrieli connor-watumull david-cowan david-selverian derrick-lee devesh-garg dhruv-jain doug-romanoff
j-edmund-colloton elliott-robinson eric-arnold ethan-kurzweil felda-hardymon hrishikesh-arjun-nair jay-po jeff-epstein
jenny-gao jeremy-levine jordan-windmueller josh-harder jules-schwerin justin-label kashish-gupta kent-bennett
kristen-faulkner kristina-shen li-sun lisa-wu mac-cordrey mackey-craven mark-lurie mary-d-onofrio matan-friedman
matt-salzberg michael-horowitz michael-segal mike-droesch morgan-cheatham naama-schlamm nate-fick nitin-gupta
ophir-reshef peter-lee phil-strazzulla philippe-botteri raghav-bahl rob-chandra rob-stavis sakib-dadi sarah-tavel
sheel-tyle siddharth-nautiyal sridar-iyengar steve-kraus stephen-bluestein subramanya-sv sunil-nagaraj tali-vogelstein
talia-goldberg tess-hatch tomer-diari trevor-neff trevor-oelschig umair-akeel umesh-padval vikul-goyal vinay-iyengar
vishal-gupta scott-smith aran-ron chris-risley william-harts s-balasubramanian daniela-nemerenco
anil-sarin james-cham ron-elwell richa-bansal yagnesh-sanghrajka rahul-jaswa""".split())
# 2008 listing names with no page of their own in the archive read so far: (slug, name, title, years)
LIST_ONLY = [("anil-sarin", "Anil Sarin", "Director, BVP India", [2008, 2009, 2010]),
             ("james-cham", "James Cham", "Vice President", [2005, 2006, 2007, 2008, 2009, 2010]),
             ("ron-elwell", "Ron Elwell", "Operating Partner, then Senior Partner", list(range(2003, 2011))),
             ("richa-bansal", "Richa Bansal", "Analyst, BVP India", [2008, 2009, 2010]),
             ("yagnesh-sanghrajka", "Yagnesh Sanghrajka", "Operating Partner, BVP India", [2008, 2009, 2010]),
             ("rahul-jaswa", "Rahul Jaswa", "Analyst", [2010, 2011, 2012])]
# Hand-set first years where the page states them ("joined Bessemer in 1992") and the archive starts later.
JOINED = {"david-cowan": 1992, "felda-hardymon": 1981, "christopher-gabrieli": 1986, "bob-goodman": 1998,
          "rob-stavis": 2001, "jeremy-levine": 2001, "j-edmund-colloton": 2001, "justin-label": 2001,
          "rob-chandra": 1996, "byron-deeter": 2005, "adam-fisher": 2007, "devesh-garg": 2003, "vishal-gupta": 2006,
          "james-cham": 2005, "ron-elwell": 2003, "sridar-iyengar": 2007, "siddharth-nautiyal": 2006,
          "ophir-reshef": 2007, "matan-friedman": 2008, "brian-feinstein": 2008, "chitresh-modi": 2008,
          "talia-goldberg": 2012, "andrew-walsh": 2013, "charles-birnbaum": 2013, "anant-vidur-puri": 2014,
          "josh-harder": 2014, "jay-po": 2014, "sakib-dadi": 2015, "andrew-hedin": 2015, "ben-matthews": 2015,
          "ben-donald": 2015, "jenny-gao": 2015, "mac-cordrey": 2015, "aneesha-raghunathan": 2015,
          "kristen-faulkner": 2016, "nitin-gupta": 2016, "dhruv-jain": 2016, "li-sun": 2016,
          "abhijeet-muzumdar": 2009, "mackey-craven": 2010, "michael-horowitz": 2010, "anna-khan": 2012,
          "raghav-bahl": 2011, "vikul-goyal": 2011, "aviad-ariel": 2011, "nate-fick": 2011, "william-harts": 2008,
          "daniela-nemerenco": 2008}
# Last years where a lingering page or the CMS alumni flag would overstate the tenure (press-dated, T4):
LAST_YEAR = {"kristina-shen": 2019,      # joined Andreessen Horowitz in 2019
             "sarah-tavel": 2012,        # left for Pinterest in 2012
             "sunil-nagaraj": 2017,      # founded Ubiquity Ventures in 2017
             "philippe-botteri": 2010,   # joined Accel in 2011
             "matt-salzberg": 2012,      # founded Blue Apron in 2012
             "nate-fick": 2012,          # chief executive of Endgame from 2012 (his seat there is the operator's)
             "james-cham": 2010}
NOT_PERSON = {"default", "team", "index"}


def norm_slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\.aspx$", "", s.replace("%20", "-").replace("_", "-"))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return VARIANTS.get(s, s)


def main() -> None:
    people: dict[str, dict] = {}

    def add(slug, name, source, years, title=""):
        slug = VARIANTS.get(slug, slug)
        r = people.setdefault(slug, {"slug": slug, "name": name, "years": set(), "sources": [], "titles": set(),
                                      "basis": collections.defaultdict(set)})
        r["years"] |= set(int(y) for y in years)
        r["basis"][source] |= set(int(y) for y in years)
        if source not in r["sources"]:
            r["sources"].append(source)
        if title:
            r["titles"].add(title)
        if name and (len(name) > len(r["name"] or "") or not r["name"]):
            r["name"] = r["name"] or name

    titles = json.loads((HERE / "team-page-titles.json").read_text()) if (HERE / "team-page-titles.json").exists() else {}
    names = {norm_slug(k): re.sub(r"\s+", " ", v["name"]).strip() for k, v in titles.items()
             if v.get("name") and "BVP" not in v["name"] and "Untitled" not in v["name"]}

    # team-page years from the capture indexes
    page_years = collections.defaultdict(set)
    idx = json.loads((HERE / "cc-index-raw.json").read_text())
    for cid, slots in idx.items():
        for v in slots.values():
            for r in v.get("records", []):
                p = re.sub(r"https?://(www\.)?bvp\.com(:\d+)?", "", r["url"]).split("?")[0].rstrip("/")
                m = re.match(r"^/(?:in/)?[Tt]eam/([A-Za-z][A-Za-z0-9_.%-]+?)(?:\.aspx)?$", p)
                if m and m.group(1).lower() not in NOT_PERSON:
                    page_years[norm_slug(m.group(1))].add(int(r["timestamp"][:4]))
    ia = HERE / "cdx-map-bvp.com.json"
    if ia.exists():
        for row in json.loads(ia.read_text()):
            orig, ts, endts = row[0], row[1], row[2]
            p = re.sub(r"https?://(www\.)?bvp\.com(:\d+)?", "", orig).split("?")[0].rstrip("/")
            m = re.match(r"^/(?:in/)?[Tt]eam/([A-Za-z][A-Za-z0-9_.%-]+?)(?:\.aspx)?$", p)
            if m and m.group(1).lower() not in NOT_PERSON:
                for y in range(int(ts[:4]), int(endts[:4]) + 1):
                    page_years[norm_slug(m.group(1))].add(y)
    # 2019+ pages carry a title line; the last capture's title is the person's last role at the firm
    inv_re = re.compile(r"partner|vice president|investor|principal|associate|analyst", re.I)
    bad_re = re.compile(r"operating advisor|assistant|tax|account|counsel|marketing|talent|business development|chief|"
                        r"relations|people|operations|controller|treasury|monitoring|coordinator|office|community|event|"
                        r"solutions|legal|finance|compliance|platform|content|emerit|program", re.I)
    for k, v in titles.items():
        role = (v.get("role") or "").strip()
        slug = norm_slug(k)
        if role and inv_re.search(role) and not bad_re.search(role) and page_years.get(slug):
            add(slug, names.get(slug) or v["name"], "team-page", page_years[slug], role)
    for slug in ("mike-giampapa",):   # Vice President until 2023; the last capture of his page carries no title
        if page_years.get(slug):
            add(slug, "Mike Giampapa", "team-page", page_years[slug], "Vice President")
    for slug, yrs in page_years.items():
        if slug in INVESTING:
            nm = names.get(slug) or " ".join(w.capitalize() for w in slug.split("-"))
            add(slug, nm, "team-page", yrs)
    for slug, name, title, yrs in LIST_ONLY:
        add(slug, name, "team-list", yrs, title)

    # the live site
    live = json.loads((P.site / "team-pages.json").read_text())
    for t in live:
        slug = norm_slug(t["slug"])
        inv_title = bool(re.search(r"partner|vice president|investor|principal|associate|analyst", t["title"], re.I)) \
            and not re.search(r"chief|counsel|relations|marketing|talent|people|accounting|assistant|operating advisor|"
                              r"infrastructure|monitoring|community|events?|operations", t["title"], re.I)
        if t["group"] == "investor" and "emerit" in t["title"].lower():
            # an emeritus partner is on the live team page but no longer invests: the archive years stand
            if page_years.get(slug):
                add(slug, t["name"], "team-page", page_years[slug], t["title"])
        elif t["group"] == "investor" and (inv_title or t["deals"] or t["is_partner"]):
            add(slug, t["name"], "site-team", [THIS_YEAR], t["title"])
            if page_years.get(slug):
                add(slug, t["name"], "team-page", page_years[slug])
        elif t["group"] == "alumni" and (t["deals"] or inv_title or slug in INVESTING):
            yrs = page_years.get(slug) or set()
            if yrs:
                add(slug, t["name"], "team-page", yrs, t["title"])
                add(slug, t["name"], "site-alumni", [max(yrs)], t["title"])
            elif t["deals"]:
                # an alumnus the CMS still credits with deals but whose page years are not read yet
                add(slug, t["name"], "site-alumni", [2024], t["title"])

    rows = []
    for slug, r in people.items():
        yrs = set(r["years"])
        if slug in JOINED:
            yrs.add(JOINED[slug])
        last = LAST_YEAR.get(slug)
        if last:
            yrs = {y for y in yrs if y <= last} or {last}
        first, lastseen = min(yrs), max(yrs)
        filled = list(range(first, lastseen + 1))
        name = FILED_NAME.get(slug) or re.sub(r",?\s*(M\.?D\.?|Ph\.?D\.?)$", "", r["name"]).strip()
        rows.append({"slug": slug, "name": name, "years_seen": filled, "first_seen": first, "last_seen": lastseen,
                     "snapshots": len(r["years"]), "sources": sorted(r["sources"]), "title": "; ".join(sorted(r["titles"])),
                     "basis": {k: sorted(v) for k, v in r["basis"].items()}})
    rows.sort(key=lambda x: x["slug"])
    P.wayback.mkdir(parents=True, exist_ok=True)
    write_atomic(OUT, json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(len(rows), "people;", sum(1 for r in rows if r["last_seen"] == THIS_YEAR), "current")
    for r in rows:
        print(f"  {r['slug']:28} {r['name']:26} {r['first_seen']}-{r['last_seen']} {','.join(r['sources'])} {r['title'][:40]}")
    missing = sorted(s for s in INVESTING if s not in people)
    print("INVESTING slugs with no evidence years:", missing)


if __name__ == "__main__":
    main()
