#!/usr/bin/env python3
"""Curate sources/wayback/partner-roster.json: union what is on disk (the CDX
first-capture roster, or partner-roster.py's output when the archive answers)
with dated facts from registers, filings and the firm's own posts. A dated
register or filing fact extends a window and is never shortened by a capture
span (decisions.md D9). Re-run after partner-roster.py."""
import json, os
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "sources" / "wayback" / "partner-roster.json"
rows = {r["slug"]: r for r in json.loads(P.read_text())}
FACTS = {
 # slug: (first, last, name, basis)
 "hans-otterling": (2009, 2020, "Hans Otterling", "general partner on the 2009 team page; related person on the Northzone Streaming Opportunity L.P. Form D 2015-05-05; director of Northzone Ventures UK Limited 2014-09-15 to 2016-01-28 and designated member of Northzone UK LLP 2016-06-28 to 2020-04-05 (Companies House)"),
 "tellef-thorleifsson": (2009, 2018, "Tellef Thorleifsson", "founding partner on the 2009 team page; related person on the 2015 Streaming Opportunity Form D; director of Northzone Ventures UK Limited 2012-02-14 to 2018-09-30 (Companies House); 'Northzone founder joins Nordfund' (the firm's post, 2018-06-07)"),
 "bjorn-stray": (2009, 2015, "Bjørn Stray", "2009 team page; related person on the 2015 Streaming Opportunity Form D"),
 "gregers-kronborg": (2009, 2015, "Gregers Kronborg", "2009 team page; related person on the 2015 Streaming Opportunity Form D"),
 "thorleif-ahlsand": (2009, 2015, "Torleif Ahlsand", "2009 team page (slug thorleif-ahlsand); related person 'Torleif Ahlsand' on the 2015 Streaming Opportunity Form D"),
 "par-jorgen-parson": (2009, 2026, "Pär-Jörgen Pärson", "2009 team page; 2015 Streaming Opportunity Form D; live team page 2026 (Partner, Stockholm)"),
 "jeppe-zink": (2011, 2026, "Jeppe Zink", "director of Northzone Ventures UK Limited from its incorporation 2011-12-13; 'Northzone establishes London presence and welcomes Jeppe Zink as general partner' (the firm's post, 2012-01-17); designated member of Northzone UK LLP 2016-06-28 to date; live team page 2026"),
 "michiel-kotting": (2015, 2026, "Michiel Kotting", "'Michiel Kotting joins Northzone as general partner' (the firm's post, 2015-12-23); member of Northzone UK LLP 2016-06-28 to 2018-03-31; live team page 2026 (Partner, Amsterdam)"),
 "paul-murphy": (2018, 2021, "Paul Murphy", "joined February 2018 (the firm's post 'Connecting the dots & partnering up', 2018-02-07); designated member of Northzone UK LLP 2019-04-06 to 2021-08-20; announced his move to Lightspeed 2021-02-26 (TechCrunch). Seats from March 2021 are Lightspeed's (decisions.md D9)"),
 "kilian-pender": (2021, 2023, "Kilian Pender", "'Meet Kilian Pender, our newest partner' (the firm's post, 2021-09-27); designated member of Northzone UK LLP 2021-08-20 to 2023-08-04"),
 "wendy-xiao": (2020, 2026, "Wendy Xiao", "team page slug wendy-xiao-schadeck first captured 2020; 'Wendy Xiao Schadeck becomes Northzone's first New York partner' (the firm's post, 2021-01-19); live team page 2026 (Partner, New York)"),
 "jessica-schultz": (2016, 2026, "Jessica Schultz", "'Jessica Nilsson promoted to Partner' (the firm's post, 2016-09-01; the same person, now Jessica Schultz); live team page 2026 (Partner, Stockholm). Filings may carry either surname."),
 "molly-alter": (2023, 2026, "Molly Alter", "'Molly Alter Joins Northzone New York!' (the firm's post, 2023-07-13); promoted to Partner 2024-08-01 (the firm's post); live team page 2026"),
 "sanjot-malhi": (2023, 2026, "Sanjot Malhi", "member of Northzone UK LLP 2023-04-01 to date; live team page 2026 (Partner, London)"),
 "sam-endacott": (2026, 2026, "Sam Endacott", "member of Northzone UK LLP 2026-07-01; live team page 2026 (Partner, London)"),
}
# Windows and titles read off the Common Crawl captures of the team pages 2010-2025 (scratch/cc-people.json)
import re as _re
CC = json.loads((Path(__file__).resolve().parent / "cc-people.json").read_text())
NON_INVESTING = {"Stine Foss", "Kristin Kulsrud", "Lea Bajc", "Jackson Heddy", "Rachael Rickwood", "Nicola Sibley", "Nick McCaul",
                 "Amit Sanghvi", "Laura Clifford", "Grace Bentley", "Sanna Blomkvist", "Elena Pantazi", "Iby Khan", "Theo Weir",
                 "Phillip Lally", "Marlowe Cameron", "Daniel Ek", "Geir Førre", "Sorosh Tavakoli", "William Jilltoft"}
def _slug(n): return _re.sub(r"[^a-z0-9]+", "-", n.lower().replace("ø", "o").replace("ö", "o").replace("ä", "a").replace("å", "a").replace("é", "e")).strip("-")
ALIAS = {"wendy-xiao-schadeck": "wendy-xiao", "vincent-touati-tomas": "vincent-touati-tomas", "sarah-nockel": "sarah-nockel", "torleif-ahlsand": "thorleif-ahlsand"}
for name, e in CC.items():
    sl = ALIAS.get(_slug(name), _slug(name))
    r = rows.setdefault(sl, {"slug": sl, "name": name, "years_seen": [], "sources": [], "snapshots": 0})
    ys = sorted(set(r.get("years_seen", [])) | set(e["years"]))
    r.update(years_seen=ys, first_seen=min(ys), last_seen=max(ys), snapshots=len(ys))
    r["sources"] = sorted(set(r.get("sources", [])) | {"commoncrawl-team-pages"})
    r["title_cc"] = ", ".join(e["titles"]) or None
    r["investing"] = name not in NON_INVESTING
    r["basis"] = (r.get("basis", "") if "PROVISIONAL" not in r.get("basis", "") else "") + f" | team page captured {min(e['years'])}-{max(e['years'])} (Common Crawl){'; ' + r['title_cc'] if r['title_cc'] else ''}"
for extra, (name, a0, b0, why) in {"jessica-nilsson": ("Jessica Nilsson", 2016, 2026, "Jessica Schultz's earlier surname (the firm's post 'Jessica Nilsson promoted to Partner', 2016-09-01), kept so filings under either surname match"),
                                     "erik-bakkejord": ("Erik Bakkejord", 2013, 2014, "on the 2013-14 people pages (Common Crawl); role not stated on the capture")}.items():
    r = rows.setdefault(extra, {"slug": extra, "name": name, "years_seen": [a0, b0], "sources": ["registers-filings-posts"], "snapshots": 2})
    r.update(first_seen=a0, last_seen=b0, basis=why, investing=True)
for r in rows.values():
    if r.get("name") in NON_INVESTING:
        r["investing"] = False
for slug, (a, b, name, basis) in FACTS.items():
    r = rows.setdefault(slug, {"slug": slug, "name": name, "years_seen": [], "sources": [], "snapshots": 0})
    ys = sorted(set(r.get("years_seen", [])) | {a, b})
    r.update(name=name, years_seen=ys, first_seen=min(ys), last_seen=max(ys),
             basis=basis + (" | " + r["basis"] if r.get("basis") and "PROVISIONAL" not in r["basis"] else ""))
    r["sources"] = sorted(set(r.get("sources", [])) | {"registers-filings-posts"})
staff = sorted((r for r in rows.values() if r.get("investing") is False), key=lambda r: r["slug"])
(Path(__file__).resolve().parent / "staff.json").write_text(json.dumps(staff, indent=1, ensure_ascii=False) + "\n")
out = sorted((r for r in rows.values() if r.get("investing") is not False), key=lambda r: r["slug"])
tmp = str(P) + ".t"; open(tmp, "w").write(json.dumps(out, indent=1, ensure_ascii=False) + "\n"); os.replace(tmp, P)
print(len(out), "people;", sum(1 for r in out if "registers-filings-posts" in r["sources"]), "with dated facts")
