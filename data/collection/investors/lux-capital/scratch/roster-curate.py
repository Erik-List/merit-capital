#!/usr/bin/env python3
"""Add the pre-2016 roster to sources/wayback/partner-roster.json.

partner-roster.py enumerates the dash-separated people namespaces
(/team/<first>-<last> 2016-2022, /people/ and /advisors/ 2023+), which start
in 2016. Lux's first sixteen years of people live in two eras the pattern
cannot reach: the 2005-2008 PHP site's /team_<lastname>.php pages and the
2010-2015 site, which rendered the team as images (/imteam/<initials>.jpg).
The Form D roster sweep derives its targets from this file, so without these
names the sweep is blind to every deal whose only Lux board seat was held by
someone who left before 2016 -- exactly the recall hole COLLECTION.md §5
names for a current-team roster.

Windows are capture-evidenced: the year range of the captures that name the
person (CDX index of team_*.php, the 2005/2008 team pages and the 2014 /team
listing), never a model prior about when someone joined.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

# slug: (name, first_seen, last_seen, group, evidence)
EARLY = {
    "josh-wolfe": ("Josh Wolfe", 2000, None, "investment",
                   "co-founder; luxcapital.com/team.htm captures from 2000, team_wolfe.php 2005"),
    "peter-hebert": ("Peter Hébert", 2000, None, "investment",
                     "co-founder; team.htm 2000, team_hebert.php 2005"),
    "robert-paull": ("Robert Paull", 2000, None, "investment",
                     "co-founder; team_paull.php 2005; listed under /advisors/ from 2025"),
    "adam-kalish": ("Adam Kalish", 2005, None, "investment", "team_kalish.php 2005"),
    "larry-bock": ("Larry Bock", 2005, 2016, "investment",
                   "team_bock.php 2005; 2014 /team as Special Limited Partner"),
    "sasha-blaug": ("Sasha Blaug", 2006, 2007, "investment",
                    "team_blaug.php 2007 ('associate with Lux Capital')"),
    "shahin-farshchi": ("Shahin Farshchi", 2007, None, "investment", "team_farshchi.php 2007"),
    "nick-wachtel": ("Nick Wachtel", 2007, 2008, "investment",
                     "team_wachtel.php 2007, team_partners.php 2008"),
    "carl-barrelet": ("Carl Barrelet", 2007, 2008, "investment",
                      "team_barrelet.php 2007, team_partners.php 2008"),
    "zack-schildhorn": ("Zack Schildhorn", 2008, None, "investment",
                        "team_schildhorn.php 2008; /advisors/ from 2025"),
    "bilal-zuberi": ("Bilal Zuberi", 2013, None, "investment",
                     "2014 /team listing (Partner); /imteam/b_zuberi_partner_media2.jpg 2014"),
    "adam-goulburn": ("Adam Goulburn", 2013, 2022, "investment",
                      "2014 /team listing (Senior Associate)"),
    "jeff-weinstein": ("Jeff Weinstein", 2013, 2016, "investment",
                       "2014 /team listing (Associate)"),
    "zavain-dar": ("Zavain Dar", 2013, 2022, "investment",
                   "2014-era team captures; /team/zavain-dar 2016"),
    "renata-quintini": ("Renata Quintini", 2015, 2017, "investment",
                        "/team/renata-quintini captures 2017"),
    "tuvia-barak": ("Tuvia Barak", 2005, None, "venture_partner",
                    "2005 team.php Senior Advisors; 2014 /team as Venture Partner"),
    "richard-foster": ("Richard Foster", 2014, None, "venture_partner",
                       "2014 /team listing (Venture Partner)"),
    "jeff-kindler": ("Jeff Kindler", 2014, 2016, "venture_partner",
                     "2014 /team listing (Venture Partner)"),
}
# Named on the early team pages but never investing for the firm: the Senior
# Advisors block (T4 -- a seat these people hold is their own, not Lux's).
ADVISORS_ONLY = {
    "herb-goronkin": "Herb Goronkin (former Motorola Physical Research Labs) — 2005-2016 senior adviser",
    "bob-balk": "Bob Balk (former Boeing Venture Capital) — 2005 senior adviser",
    "hamilton-jordan": "Hamilton Jordan (former White House chief of staff) — 2005 senior adviser",
    "david-sinclair": "David Sinclair (Harvard Medical School) — 2008-2016 senior adviser",
    "r-james-woolsey": "R. James Woolsey (former DCI) — 2014-2016 senior adviser",
}


def main():
    p = Paths("lux-capital")
    f = p.wayback / "partner-roster.json"
    people = json.loads(f.read_text())
    by_slug = {r["slug"]: r for r in people}
    added, extended = 0, 0
    for slug, (name, first, last, group, ev) in EARLY.items():
        r = by_slug.get(slug)
        if r is None:
            r = {"slug": slug, "name": name, "years_seen": [], "first_seen": first,
                 "last_seen": last, "snapshots": 0, "sources": []}
            people.append(r)
            by_slug[slug] = r
            added += 1
        elif first < (r.get("first_seen") or 9999):
            r["first_seen"] = first
            extended += 1
        if last is not None and (r.get("last_seen") or 0) < last:
            r["last_seen"] = last
        r["group"] = group
        r.setdefault("sources", [])
        if "curated-pre-2016" not in r["sources"]:
            r["sources"].append("curated-pre-2016")
        r["curation_evidence"] = ev
    write_atomic(f, json.dumps(sorted(people, key=lambda r: r["slug"]), indent=1))
    write_atomic(p.wayback / "roster-advisors-only.json", json.dumps(
        {"_readme": "Named on Lux's own early team pages under Senior Advisors and "
                    "excluded from the Form D sweep roster: they advise, they do not "
                    "invest the funds, and a board seat one of them holds is their own "
                    "(COLLECTION.md §1 T4).", "people": ADVISORS_ONLY}, indent=1))
    print(f"roster: {len(people)} people ({added} added, {extended} windows extended)")
    print(f"  pre-2016 investment side: "
          f"{sorted(s for s, v in EARLY.items() if v[3] == 'investment')}")


if __name__ == "__main__":
    main()
