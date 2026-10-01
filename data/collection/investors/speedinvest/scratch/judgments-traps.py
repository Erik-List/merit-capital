"""Membership verdicts for the rows the grind groups do not take: the sale-
consideration acquirers (decisions.md D4/D5), the firm's own board row, and the
twelve Form D-only issuers of the roster sweep (D7)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J

L = []
c = json.load(open(J.INV / "config.json"))
for t in c["verify"]["not_members"]:
    if t["slug"] == "speedinvest":
        L.append(J.verdict("speedinvest", "not_member", "The firm itself, listed as a company on its own Getro job board (careers.speedinvest.com); not a portfolio company (decisions.md D1).",
                           cite="https://careers.speedinvest.com/companies"))
        continue
    lv = J.live(t["slug"])
    L.append(J.verdict(t["slug"], "not_member", t["why"], cite=lv["url"] if lv else None))

FD = "https://www.sec.gov/Archives/edgar/data/"
L += [
 J.verdict("blloc-inc", "member", "The firm's own post of 2021-12-09 on the SoftBank-Speedinvest Emerge cohort: 'Speedinvest invested a total of $5m into three startups: Adham Badr and Berlin-based Blloc, a homescreen app...'. Blloc Inc. filed a Form D in 2021 naming Michael Schuster. Not on the firm's current list.",
           cite="https://www.speedinvest.com/knowledge/millions-in-funding-for-the-first-ever-european-emerge-cohort-of-startups"),
 J.verdict("heroes-jobs-inc", "member", "Director-of-record pattern (COLLECTION.md s1): Mathias Ockenfels, partner of Speedinvest x (the Network Effects fund, 2018-2023), is a director on both Form Ds of Heroes Jobs Inc. (Nov 2019 and Jan 2020, $4.0M sold), inside his tenure; the issuer resolves to a real company (Heroes, the San Francisco Gen Z job app founded 2019 by Tristan Petit, Adrien Dewulf and Cyriac Lefort, bought by JobGet in May 2023). Unannounced by the firm; flagged for the A/B pass.",
           ec="formd_adjudicated", conf="medium", cite=FD + "1770758/000177075820000001/0001770758-20-000001-index.htm"),
 J.verdict("acadia-pharmaceuticals-inc", "not_member", "Form D name-match only: 'William Wells' on ACADIA Pharmaceuticals' 2013 filing is a pharmaceutical director, not Will Wells of Speedinvest's growth team (on the firm's team page from 2026); ACADIA has been Nasdaq-listed since 2004. No corroboration (D7).", ec="formd_adjudicated"),
 J.verdict("hls-therapeutics-inc", "not_member", "Form D name-match only: 'Bill Wells' on a 2015 filing of a Canadian pharmaceutical company; not Speedinvest's Will Wells. No corroboration (D7).", ec="formd_adjudicated"),
 J.verdict("risktek-solutions-llc", "not_member", "Form D name-match only: 'William Wells' on a 2013 Birmingham, Alabama business-services filing; homonym. No corroboration (D7).", ec="formd_adjudicated"),
 J.verdict("trafficland-inc", "not_member", "Form D name-match only: 'Bill Wells' on TrafficLand's 2010-2011 filings (Virginia); homonym, a decade before Will Wells joined Speedinvest. No corroboration (D7).", ec="formd_adjudicated"),
 J.verdict("couchsurfing-international-inc", "not_member", "Daniel Hoffer co-founded CouchSurfing (2004) and sits on its 2012 Form D as a founder; he was a part-time Speedinvest partner only from 2018 (Wikipedia). A founder's own company, not a Speedinvest position (T4).", ec="formd_adjudicated"),
 J.verdict("triplingo-inc", "not_member", "Daniel Hoffer on TripLingo's 2014 Form D, four years before his part-time Speedinvest role (2018); a personal seat (T4). No corroboration.", ec="formd_adjudicated"),
 J.verdict("kodabow-inc", "not_member", "Form D name-match only: 'Mark Lang' on KodaBow's 2012 filing (West Chester, PA); not Markus Lang of Speedinvest (on the firm's pages from 2018). Homonym (D7).", ec="formd_adjudicated"),
 J.verdict("madrinas-brands-llc", "not_member", "Form D name-match only: 'Alex Davis' on a 2019 Missouri consumer-brand filing; Speedinvest's Alex Davis appears only on the 2026 team page. Homonym (D7).", ec="formd_adjudicated"),
 J.verdict("naima-health-llc", "not_member", "Form D name-match only: 'Alexander Davis' on a 2022 Pittsburgh filing ($100K); homonym (D7).", ec="formd_adjudicated"),
 J.verdict("playback-health-inc", "not_member", "Form D name-match only: 'Sam Singh' (director) on Playback Health's 2024 filing (Long Island City, NY); Sameer Singh is a Speedinvest venture partner, but nothing ties this seat or any fund to the company. No corroboration (D7).", ec="formd_adjudicated"),
]
J.write("traps-and-formd", L)
