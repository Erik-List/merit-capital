#!/usr/bin/env python3
"""Curated partner roster for Tiger Global (PRO-167): tigerglobal.com publishes no team
page, so partner-roster.py has nothing to enumerate (config roster._note). The roster is
the Thrive / Coatue shape: the natural persons on the firm's own fund Form Ds (2009-2026,
read from the Form D bulk data), the ADV Schedule A officers (2026-03-27) and press-dated
tenures for the private-equity partners, one basis line per person. The windows are the
seat-dating windows of COLLECTION.md 1 (T4): a seat outside a person's window is not the
firm's. Where a join year is not documented the window opens at the earliest dated
record and says so.

Two spellings of one person are two roster rows to formd-query (it matches the filed
given name), so Chase Coleman carries both his filed name (Charles) and his used name,
with the same window.

Output: sources/wayback/partner-roster.json
"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("tiger-global-management")
PEOPLE = [
    ("Charles Coleman", 2001, 2026, ["adv-schedule-a", "formd-own-fund"],
     "Founder and managing member (ADV Schedule A: member since 03/2001, 75% or more); director and executive officer on the firm's own fund Form Ds 2009-2026 as Charles Coleman III (the filed spelling)."),
    ("Chase Coleman", 2001, 2026, ["adv-schedule-a", "press"],
     "The name Charles P. Coleman III uses (tigerglobal.com/ourstory: 'founded by Chase Coleman at age 25'); same person and window as the filed spelling."),
    ("Scott Shleifer", 2002, 2023, ["formd-own-fund", "press"],
     "Founded and ran the private-equity business; executive officer on the firm's own fund Form Ds 2013-2023; stepped down as head of private investing in January 2024 and became a senior adviser (Axios and TechCrunch, 2023-11-21). Seats after 2023 are not the firm's."),
    ("Lee Fixel", 2006, 2019, ["formd-own-fund", "press"],
     "Private-equity partner; executive officer on the firm's own fund Form Ds 2014-2018; left in early 2019 and founded Addition, so a seat from 2019 on is Addition's (T4). Join year approximate (press: at Tiger from the mid-2000s, led Flipkart in 2009-2010)."),
    ("Feroz Dewan", 2003, 2015, ["formd-own-fund", "press"],
     "Head of public equities; director and executive officer on the firm's own fund Form Ds 2013-2015; left in 2015 and founded Arena Holdings. Public desk; no private seats expected."),
    ("John Curtius", 2012, 2022, ["press"],
     "Private-equity partner who led the software investments; left in June 2022 to found Cedar Investment Management (Fortune 2022-10-05; TechCrunch 2023-11-21). Join year approximate (earliest dated record), so a seat before 2012 is checked against the record before it counts."),
    ("Griffin Schroeder", 2014, 2026, ["press"],
     "Private-equity partner; on the private-equity investment committee formed in January 2024 (Axios 2023-11-21). Join year approximate."),
    ("Evan Feinberg", 2008, 2026, ["press"],
     "Partner (public equities); on the private-equity investment committee formed in January 2024 (Axios 2023-11-21). Join year approximate."),
    ("Alex Cook", 2017, 2024, ["press"],
     "Private-equity partner who oversaw fintech and India deals; left in July 2024 after nearly seven years (TechCrunch 2024-07-30). A common name: every Form D match is judged against the firm's own record, never on the name."),
    ("Eric Lane", 2021, 2026, ["adv-schedule-a", "press"],
     "President and chief operating officer since 07/2021 (ADV Schedule A); on the private-equity investment committee from January 2024 (Axios 2023-11-21)."),
]


def slug(n):
    return n.lower().replace(" ", "-")


rows = []
for name, a, b, src, basis in PEOPLE:
    yrs = list(range(a, b + 1))
    rows.append({"slug": slug(name), "name": name, "site_name": name, "years_seen": yrs,
                 "first_seen": a, "last_seen": b, "snapshots": len(yrs), "sources": src, "basis": basis})
write_atomic(P.wayback / "partner-roster.json", json.dumps(rows, indent=1) + "\n")
print(f"{len(rows)} roster rows -> {P.rel(P.wayback / 'partner-roster.json')}")
