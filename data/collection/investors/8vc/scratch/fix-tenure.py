#!/usr/bin/env python3
"""Correct the roster's tenure windows with the site's own team/advisor rendering.

`partner-roster.py` derives each person's window from CDX captures of
/team/<slug>. On 8vc.com that namespace held BOTH the firm's partners and its
Advisor Upside network (decisions.md D5), and several people appear in both sets
in DIFFERENT years — Bhaskar Ghosh was an advisor 2016-2018 (VP Eng at NerdWallet)
and a partner 2019-2022; John Tenet a partner 2019-2020 and an advisor 2021-2022;
Zach Rivkin, Blake Brickman and Brett Cummings likewise. A window that unions the
two roles dates a seat to the wrong firm, which is exactly what §1's T4 forbids.

Measured cost of leaving it: Ushur's 2018q3 Form D carries BHASKAR GHOSH, three
years before he joined 8VC, and the entry-stage band read that filing as 8VC's
entry (Series A) when the firm's own post puts its entry at the 2020 Series B.

Rule: a year in which the site rendered the person ONLY as an advisor is not
tenure. Team years always win. Applied to sources/wayback/partner-roster.json,
which the base build reads.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("8vc")
roster = json.loads((P.root / "sources" / "wayback" / "partner-roster.json").read_text())
wp = json.loads((P.root / "sources" / "site" / "wp-people.json").read_text())["people"]

team_years, adv_years = {}, {}
for r in wp:
    d = team_years if r["kind"] == "team" else adv_years
    d.setdefault(r["name"], set()).update(r["years"])

changed = []
for p in roster:
    n = p["name"]
    adv_only = adv_years.get(n, set()) - team_years.get(n, set())
    if not adv_only:
        continue
    ys = [y for y in p.get("years_seen", []) if y not in adv_only]
    if not ys or ys == p.get("years_seen"):
        continue
    before = (p["first_seen"], p["last_seen"])
    p["years_seen"] = ys
    p["first_seen"], p["last_seen"] = min(ys), max(ys)
    p.setdefault("notes", []).append(
        f"advisor-only years removed from tenure ({sorted(adv_only)}); the site rendered "
        f"this person under square--advisor, not square--team, in those years")
    changed.append((n, before, (p["first_seen"], p["last_seen"]), sorted(adv_only)))

write_atomic(P.root / "sources" / "wayback" / "partner-roster.json",
             json.dumps(roster, indent=1, ensure_ascii=False))
print(f"roster rows: {len(roster)}; tenure windows corrected: {len(changed)}")
for n, b, a, adv in changed:
    print(f"   {n:22} {b[0]}-{b[1]} -> {a[0]}-{a[1]}   (advisor-only {adv})")
