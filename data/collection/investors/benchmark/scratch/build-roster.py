#!/usr/bin/env python3
"""Benchmark's roster, CURATED (COLLECTION.md §5, the Thrive/USV path).

partner-roster.py returns zero people here and cannot do better: the firm's
people namespaces are first-name slugs (/about/bill.html, 1997-2001) that no
Form D name sweep can use, full-name pages on three desk sites (2001-2009),
and NOTHING since 2013 — benchmark.com has published no team page for
thirteen years. So the roster is assembled from three dated, checkable
sources and written in partner-roster.py's own shape:

  site      — the firm's own per-person pages, tenure = CDX capture years
              (verified 2026-09-06, per page)
  own_formd — related persons on the firm's OWN fund Form Ds, tenure = filing
              years (sources/edgar/own-formd-persons.json); filing-grade
  press     — named partner arrivals the two above cannot date

Only HOME-DESK investing partners are swept. The Europe and Israel general
partners are recorded in desk-rosters.json and deliberately kept out of the
sweep: their deals are the partitioned desks' (decisions.md D2/D3), and
sweeping their names would pull Balderton's and Benchmark Israel's book back
in through the Form D layer that the desk partition just removed.
"""
import json, sys
sys.path.insert(0, "scripts")
from paths import Paths, write_atomic                                  # noqa: E402

P = Paths("benchmark")
formd = json.loads((P.edgar / "own-formd-persons.json").read_text())

def fy(*names):
    ys = set()
    for n in names:
        ys |= {int(y) for y in formd.get(n, {}).get("years", [])}
    return sorted(ys)

# (name, site years, formd name variants, sources, basis, investing)
R = [
 ("Bob Kagle", [1999,2000,2001,2005,2006,2007,2008,2009,2010], [], ["site","press"],
  "Co-founder 1995. /about/bob.html captured 1999-2001 ('Our Team - Bob Kagle'); "
  "/sv/general_partners/kagle.shtml captured 2005-2010. Absent from the Fund VII "
  "Form D of 2011-01-13, which is the firm's own first electronic roster — so the "
  "tenure closes 2010/2011, consistent with his reported retirement from active "
  "investing.", True),
 ("Bruce Dunlevie", list(range(1999,2027)), ["Bruce W. Dunlevie"],
  ["site","own_formd"],
  "Co-founder 1995. /about/bruce.html 1999-2001, /Silicon_Valley/Bruce_Dunlevie.html, "
  "/sv/general_partners/dunlevie.shtml 2005-2010; related person on Fund VII (2011), "
  "VII AIV (2012) and VII-Annex (2016). Off the Fund VIII roster (2013) and after — "
  "the Annex is a Fund VII vehicle, so 2016 is the vintage he was a GP of, not a "
  "2016 tenure.", True),
 ("Andy Rachleff", [1999,2000,2001], [], ["site","press"],
  "Co-founder 1995. /about/andy.html 1999-2001 ('Our Team - Andy Rachleff'); "
  "/Silicon_Valley/Andy_Rachleff.html in the 2001-2005 era. Left to found Wealthfront; "
  "absent from every era-3 general_partners page (2005-2010).", True),
 ("Kevin Harvey", [1999,2000,2001,2005,2006,2007,2008,2009,2010], ["Kevin R. Harvey"],
  ["site","own_formd"],
  "Co-founder 1995. /about/kevin.html 1999-2001, /sv/general_partners/harvey.shtml "
  "2005-2010; related person on Fund VII (2011), VII AIV (2012), VII-Annex (2016).", True),
 ("Val Vaden", list(range(1995, 1999)), [], ["press"],
  "Co-founder 1995, one of the firm's own founding five. No person page exists for him in any "
  "captured era — the 1999 team page already lists only Kagle, Dunlevie, Rachleff, Harvey, Beirne, "
  "Gurley, Balkanski and Spurlock — so the window is set 1995-1998 from the founding date and that "
  "absence. His only Form D seats (InXpo, 2009-2016) fall a decade past it and are ruled out (R8).", True),
 ("David Beirne", [1999,2000,2001], [], ["site","press"],
  "Joined 1997 from Ramsey Beirne. /about/dave.html 1999-2001 ('Our Team - Dave "
  "Beirne'), /Silicon_Valley/David_Beirne.html in the 2001-2005 era; absent from "
  "every era-3 general_partners page.", True),
 ("Bill Gurley", list(range(1999,2021)), ["J. William Gurley"],
  ["site","own_formd"],
  "Joined 1999. /about/bill.html captured 1999-2007 — the longest-lived era-1 person "
  "page — /Silicon_Valley/Bill_Gurley.html and /sv/general_partners/gurley.shtml; "
  "related person on every fund Form D from VII (2011) to Founders' IX-A and the WS "
  "SPV (2019). Absent from Fund X (2020-05-19), which dates the step back from the "
  "new fund.", True),
 ("Alex Balkanski", [2000,2001,2005,2006,2007,2008,2009,2010], [], ["site"],
  "/about/alex.html captured 2000-2001, /Silicon_Valley/Alex_Balkanski.html, "
  "/sv/general_partners/balkanski.shtml 2005-2010. Absent from the 2011 Fund VII "
  "Form D roster.", True),
 ("Steve Spurlock", [1999,2000,2001,2005,2006,2007,2008,2009,2010], ["Steven M. Spurlock"],
  ["site","own_formd"],
  "/about/steve.html 1999-2001, /Silicon_Valley/Steve_Spurlock.html, "
  "/sv/general_partners/spurlock.shtml 2005-2010; related person on every fund Form D "
  "from VII (2011) through Fund X and Founders' X (2020).", True),
 ("Peter Fenton", [2006,2007,2008,2009,2010], ["Peter H. Fenton"], ["site","own_formd"],
  "Joined 2006 from Accel. /sv/general_partners/fenton.shtml and fenton.html in the "
  "2005-2009 era; related person on all 23 of the firm's own Form D filings from 2011 "
  "to 2026 — the only continuous name across the whole electronic record.", True),
 ("Mitch Lasky", list(range(2007,2024)), ["Mitchell Lasky","Mitchell H. Lasky"],
  ["site","own_formd"],
  "Joined 2007. /sv/general_partners/lasky.shtml captured 2007-2010; related person on "
  "Fund VII (2011) through VII-Annex (2016); off the Fund IX roster (2018).", True),
 ("Matt Cohler", list(range(2008,2021)), ["Matt Cohler","Matthew R. Cohler"], ["site","own_formd"],
  "Joined 2008 from Facebook. /sv/general_partners/cohler.shtml captured 2008-2010; "
  "related person from Fund VII (2011) to VII-Annex (2016); off the Fund IX roster "
  "(2018).", True),
 ("Eric Vishria", [], ["Eric Vishria","Eric H. Vishria"], ["own_formd"],
  "First appears on the Founders' Fund VIII amendment of 2015-02-26 (joined 2014, "
  "after RockMelt sold to Yahoo); related person continuously to the 2026 filings.", True),
 ("Sarah Tavel", list(range(2017,2027)), ["Sarah E. Tavel"], ["own_formd","press"],
  "Related person from Fund IX (2018-10-01) to Benchmark Partners Founders' Fund 1 "
  "(2024-10-17); not on the 2026-02 or 2026-06 filings, consistent with the move to "
  "venture partner.", True),
 ("Chetan Puttagunta", [], ["Chetan Puttagunta"], ["own_formd"],
  "Related person from Fund IX (2018-10-01) through the 2026 filings.", True),
 ("Miles Grimshaw", list(range(2021,2025)), [], ["press"],
  "Joined 2021 from Thrive Capital and departed before the 2024 fund: he appears on "
  "NONE of the firm's own Form D filings, because no fund was raised between Fund X "
  "(2020-05) and Benchmark Partners 1 (2024-07). Swept on the press record alone and "
  "flagged: any row resting on his name only is checked against the firm's own "
  "attribution before it seeds member.", True),
 ("Victor Lazarte", list(range(2022,2027)), ["Victor Lazarte"], ["own_formd"],
  "Related person on Benchmark Partners 1 and the Partners Founders' Fund 1 / 1-A "
  "(2024); not on the 2026 filings.", True),
 ("Everett Randle", [], ["Everett Randle"], ["own_formd"],
  "Related person on the AI Infrastructure Fund and Fund B (2026-02-06) and on "
  "Benchmark Partners 2 / T1 (2026-06-30).", True),
 ("Jack Altman", [], ["Jack Altman"], ["own_formd"],
  "Related person on Benchmark Partners 2 and T1 (2026-06-30), the firm's own dating "
  "of the 2026 hire.", True),
 ("An-Yen Hu", [], ["An-Yen Hu"], ["own_formd"],
  "Related person from Founders' Fund X-A (2020-12) through the 2026 filings. Finance "
  "and operations, not an investing partner: the name is swept like any other but a "
  "Form D seat in her name is not a firm investment attribution.", False),
]

# R3 (2026-09-06). Tenure is a fact about the FIRM, not about fund-vehicle
# membership: a partner drops off the related-person list of the NEXT fund
# years before leaving, and Benchmark raised no fund at all between 2020 and
# 2024. Windows taken from the Form D vehicles alone were filtering real
# members out of the base — Discord (Benchmark led the 2016 Series A, Lasky on
# the board, Form D director filings 2020-2023) was being dropped as
# "ex-partner is the only evidence". Corrected from the press record; where no
# departure is recorded the window stays OPEN and the judge rules the row.
R3 = {
 "Bruce Dunlevie": "R3: window left open to 2026 — no departure is recorded anywhere and he is "
   "not among Wikipedia's prior partners (Gurley, Lasky, Cohler, Lazarte); still filing as a Form D "
   "director in 2025. His post-2016 seats reach the judge instead of being filtered out.",
 "Bill Gurley": "R3: Wikipedia — stepped back 'after serving with the firm for twenty-one years' "
   "(1999+21 = 2020), so the window closes 2020, one year past his last fund Form D.",
 "Mitch Lasky": "R3: Wikipedia lists him among partners who 'stepped back after each spending more "
   "than a decade with the firm' (joined 2007) and its infobox still reads general partner; he filed "
   "as a Form D director of Discord through 2023. Window 2007-2023, not the fund-vehicle 2016 — that "
   "tighter window was dropping the Discord Series A Benchmark led in 2016.",
 "Matt Cohler": "R3: 'more than a decade' from 2008, so the window runs to 2020, not the "
   "fund-vehicle 2016.",
 "Sarah Tavel": "R3: joined 2017 (press); off the 2026 filings on the move to venture partner, "
   "still at the firm, so the window stays open.",
 "Miles Grimshaw": "R3: 2021-2024 from the press record; no fund was raised in those years, which is "
   "why no Form D carries him.",
 "Victor Lazarte": "R3: joined 2022 (press); window left open to 2026 so recent seats reach the judge.",
}

rows = []
for name, site_years, fd_names, sources, basis, investing in R:
    if name in R3:
        basis = basis + " " + R3[name]
    years = sorted(set(site_years) | set(fy(*fd_names)))
    rows.append({
        "slug": name.lower().replace(" ", "-").replace(".", ""),
        "name": name,
        "years_seen": years,
        "first_seen": (years[0] if years else None),
        "last_seen": (years[-1] if years else None),
        "snapshots": len(years),
        "sources": sources,
        "basis": basis,
        "investing": investing,
    })
write_atomic(P.wayback / "partner-roster.json", json.dumps(rows, indent=1) + "\n")

DESK = {
 "europe": [("Barry Maloney","/Europe/Barry_Maloney.html, /europe/general_partners/maloney.shtml"),
            ("Eric Archambeau","/Europe/Eric_Archambeau.html"),
            ("George Coelho","/Europe/George_Coelho.html, /europe/general_partners/coelho.shtml"),
            ("Jerome Misso","/Europe/Jerome_Misso.html, /europe/general_partners/misso.shtml"),
            ("Johan Brenner","/Europe/Johan_Brenner.html, /europe/general_partners/brenner.shtml"),
            ("Mark Evans","/Europe/Mark_Evans.html, /europe/general_partners/evans.shtml"),
            ("Ynon Kreiz","/Europe/Ynon_Kreiz.html, /europe/general_partners/kreiz.shtml"),
            ("Gilles Samoun","/Europe/Gilles_Samoun.html"),
            ("John Newton","/Europe/John_Newton.html"),
            ("Josh Hannah","/Europe/Josh_Hannah.html"),
            ("Peter Malcolm","/about/peter_malcolm.html"),
            ("Robert Wuttke","/Europe/Robert_Wuttke.html"),
            ("Riccardo Zacconi","/Europe/Riccardo_Zacconi.html"),
            ("Tim Barker","/Europe/Tim_Barker.html"),
            ("Eithan Ephrati","/Europe/Eithan_Ephrati.html")],
 "israel": [("Michael Eisenberg","/about/israel/general_partners/eisenberg.shtml, /israel/general_partners/eisenberg.shtml"),
            ("Arad Naveh","/Israel/Arad_Naveh.html, /israel/general_partners/naveh.shtml"),
            ("Mark Kremer","/Israel/Mark_Kremer.html, /israel/general_partners/kremer.shtml"),
            ("Nachman Shelef","/Israel/Nachman_Shelef.html, /israel/general_partners/shelef.shtml"),
            ("Bruce Wurtman","/about/israel/general_partners/wurtman.shtml, /israel/general_partners/wurtman.shtml")],
}
write_atomic(P.wayback / "desk-rosters.json", json.dumps(
    {d: [{"name": n, "pages": p} for n, p in v] for d, v in DESK.items()}, indent=1) + "\n")

print(f"partner-roster.json: {len(rows)} home-desk people "
      f"({sum(1 for r in rows if r['investing'])} investing)")
for r in rows:
    print(f"  {r['name']:20} {r['first_seen']}-{r['last_seen']}  {','.join(r['sources'])}")
print(f"desk-rosters.json: {len(DESK['europe'])} europe, {len(DESK['israel'])} israel "
      f"(recorded, NOT swept)")
