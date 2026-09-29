#!/usr/bin/env python3
"""PRO-75 GV stage sweep, judge s1 (SWEEP-BRIEF.md, duty 9 of COLLECTION.md s8): the undetermined-stage and
unknown-status class on 50 rows. Evidence read 2026-09-29: gradview.py and show.py per row, TechCrunch's own search
(wp-json), Google News (nq.py, NQ_TAG=s1), FinSMEs and GeekWire through their archived copies, the companies' own
EDGAR filings (Form Ds, Silver Spring's 2011 S-1), Wikipedia's Rabb.it article and its references, and the sibling
books' rows. WebSearch and WebFetch were not used.

Settled 11 stages: web_verified 6 (avos-systems, cool-planet, nextdoor, rabbit, the-pill-club, transcriptic), model 5
(boxbee, lendup, parse at medium: a page ties GV to the pre-Series A round and the record names the next round the
Series A; objective-logistics at low with stage_uncited: the label rests on the seed band only; silver-spring-networks
at medium: every round open to GV after its 2009 start is the S-1's Series D or later). The firm's listing dates are
used only as bounds, never to mint a stage (the lead's clarification of 2026-09-29). New Seed rows 6, with S2A:
graduated 5 (boxbee, lendup, parse, objective-logistics, transcriptic), not graduated on a cited end 1 (rabbit). No
status settled: the 13 unknown rows found no fate on any surface read. Rows left open get no line.

Notes carry only the new sentences (record appends them). funding_rounds keep what is stored and add what was found.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

rnd, NEWS = jl.rnd, jl.NEWS
C = json.loads((jl.INV / "companies" / "classification.json").read_text())
ASOF = "2026-09-29"
S = "Stage sweep 2026-09-29: "
L = []


def sec_index(cik, acc):
    """An EDGAR filing's index page, built from the CIK and accession read off EDGAR (as judge_lib.FORMD_CITE)."""
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{acc}-index.htm"


def kept(slug, drop=lambda r: False):
    """The row's stored funding_rounds, less the entries this line restates."""
    return [r for r in (C.get(slug) or {}).get("funding_rounds") or [] if not drop(r)]


# ================================================================ Growth and Series A entries (web_verified)
# ---- avos-systems
AVOS_FIN = NEWS("avos-systems", "AVOS Systems Closes Series A Venture Capital Financing - finsmes")
L.append(jl.cls(
    "avos-systems", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=AVOS_FIN,
    entry_date="2012-04-27",
    rounds=kept("avos-systems", lambda r: r.get("round") == "Series A")
    + [rnd("2012-04-27", "Series A", None, "New Enterprise Associates and Google Ventures", True, AVOS_FIN, "press")],
    note=S + "FinSMEs (2012-04-27, read from its archived copy) names the round: AVOS 'has closed a Series A venture "
             "capital financing', 'led by New Enterprise Associates (NEA) and Google Ventures', with Madrone Capital "
             "and Innovation Works. It is the company's first institutional round and the firm first lists AVOS in "
             "May 2012, so GV entered at the Series A (web_verified)."))

# ---- cool-planet
TC_CP = "https://techcrunch.com/2011/03/17/coolplanetbiofuels-google-ventures-series-b-undisclosed-amt/"
CP_FD = sec_index(1477611, "0001477611-11-000001")
L.append(jl.cls(
    "cool-planet", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_CP,
    entry_date="2011-03-17",
    rounds=kept("cool-planet")
    + [rnd("2011-03-17", "Series B", None, None, True, TC_CP, "press"),
       rnd("2010-08-13", "Series B (Form D, amended 2011-02-22)", 17769846, None, None, CP_FD, "filing")],
    note=S + "TechCrunch (2011-03-17): CoolPlanet 'attracted a series B investment From Google Ventures', the firm's "
             "'first foray into biofuels', joining North Bridge and GE Energy Financial Services in that round; the "
             "company's Form D for it (Cool Planet BioFuels, first sale 2010-08-13) was amended on 2011-02-22 to "
             "$17.8M sold to four investors. GV entered at the Series B: Growth (web_verified). Status stays unknown: "
             "its last Form D is of July 2018 ($20.3M sold), KALB reported the Alexandria facility closing on "
             "2020-06-30, and coolplanet.com now serves a parked lander; no source read gives the company's own end."))

# ---- nextdoor
TC_ND = ("https://techcrunch.com/2013/02/12/nextdoor-closes-21-6-million-in-new-series-b-funding-to-take-its-"
         "neighborhood-focused-social-network-global/")
L.append(jl.cls(
    "nextdoor", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_ND,
    entry_date="2013-02-12",
    rounds=kept("nextdoor") + [rnd("2013-02-12", "Series B", 21600000, "Greylock Partners", True, TC_ND, "press")],
    note=S + "TechCrunch (2013-02-12): the $21.6M round led by Greylock, 'which serves as Nextdoor's Series B', "
             "brought in 'new investors Bezos Expeditions and Google Ventures'; the firm first lists Nextdoor in May "
             "2013. GV entered at the Series B: Growth (web_verified)."))

# ---- the-pill-club
NC_PC = NEWS("the-pill-club", "Online Birth Control Startup The Pill Club Raises")
L.append(jl.cls(
    "the-pill-club", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NC_PC,
    entry_date="2019-01",
    rounds=kept("the-pill-club", lambda r: r.get("amount_usd") == 51000000)
    + [rnd("2019-01", "Series B", 51000000, "VMG Partners", True, NC_PC, "press")],
    note=S + "NewsCenter.io (January 2019): The Pill Club 'secured $51 million in Series B funding', led by VMG 'with "
             "participation from new investors GV (formerly Google Ventures), ACME Capital', beside existing Base10 "
             "and Shasta (Pulse 2.0, 2019-01-24, also names the Series B). GV entered at the Series B: Growth "
             "(web_verified); its Form D shows first sale 2019-01-08."))

# ---- silver-spring-networks (the rounds on disk already cite the S-1's dated series)
L.append(jl.cls(
    "silver-spring-networks", stage="Growth", stage_src="model", stage_conf="medium",
    note=S + "the 2011 S-1 dates the Series D to 'multiple closings between October 2008 and March 2009' and the "
             "Series E to December 2009, after the Series C of 2007-08. Google Ventures began investing in 2009, and "
             "the firm lists Silver Spring from its first 2012 capture, before the March 2013 IPO, so any position GV "
             "held entered at the Series D or later (a later close, the convertible notes the 2013 prospectus "
             "converts, or a secondary): Growth whichever it was (model, medium). No source dates the entry, so no "
             "entry date is written."))

# ================================================================ Seed entries, with S2A
# ---- transcriptic (seed named, later Series A named)
TC_T12 = ("https://techcrunch.com/2012/12/13/biotech-startup-transcriptic-receives-1-2m-in-seed-funding-led-by-google-"
          "ventures-and-ff-angel/")
TC_T15 = ("https://techcrunch.com/2015/02/19/cloud-based-bio-lab-startup-transcriptic-lands-8-5-million-in-series-a-"
          "funding-to-help-it-scale/")
L.append(jl.cls(
    "transcriptic", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_T12,
    entry_date="2012-12-13", grad="graduated", grad_src="web_verified", grad_cite=TC_T15, grad_conf="high",
    rounds=kept("transcriptic")
    + [rnd("2012-12-13", "Seed", 1200000, "Google Ventures and FF Angel", True, TC_T12, "press"),
       rnd("2015-02-19", "Series A", 8500000, "Data Collective", None, TC_T15, "press")],
    note=S + "TechCrunch (2012-12-13): Transcriptic raised '$1.2 million in a seed funding round' 'led by Google "
             "Ventures and FF Angel'; the firm lists it from May 2013. GV entered at the seed (web_verified). S2A: "
             "TechCrunch (2015-02-19) reports '$8.5 million in Series A funding', Data Collective leading; a later "
             "round named Series A graduates the row: graduated."))

# ---- rabbit (seed named; cited end)
SB_R = NEWS("rabbit", "Rabbit is bringing an innovative")
BI_R = NEWS("rabbit", "A Startup Named")
VB_R = ("https://web.archive.org/web/20190801071012/https://venturebeat.com/2019/07/31/kast-acquires-remnants-of-"
        "group-watch-company-rabbit/")
R_FD = sec_index(1634638, "0001634638-15-000001")
L.append(jl.cls(
    "rabbit", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SB_R, entry_date="2013-02",
    grad="not_graduated", grad_src="web_verified", grad_cite=VB_R, grad_conf="medium", grad_asof=ASOF,
    surfaces=[
        "firm: the firm's own listings for Rabbit (2013 to 2019 captures; Kevin Rose 2014, Chris Hutchins 2015) -> no "
        "exit line, and no post of the firm names the company",
        "formd: Rabbit, Inc. (CIK 1634638, Redwood City) -> one Form D, 0001634638-15-000001, equity, first sale "
        "2015-02-09, $3,806,831 sold to 11 investors (below $5M and below twice the $3.3M seed); EDGAR full-text "
        "search finds no other filing naming the company",
        "googlenews: '\"Rabbit\" (\"rabb.it\" OR \"co-watching\" OR \"watch together\")' with round words, '\"Rabbit\" "
        "Temkin', '\"Rabbit\" \"video chat\"' with round words -> the 2013 seed (StartUp Beat), the August 2014 launch "
        "(Business Insider, Fast Company, PR Newswire); no later round",
        "techcrunch: TechCrunch's own search ('rabb.it', 'Rabbit co-watching', 'Rabbit streaming' in 2019) -> no "
        "story on the company's funding",
        "wikipedia: Rabb.it -> a VC round failed in May 2019, the service shut down and Kast acquired its remaining "
        "assets on 2019-07-31; no round after the seed named",
        "venturebeat: VentureBeat's 2018-11-08 profile and its 2019-07-31 report of Kast's purchase (archived copies) "
        "-> no later round named",
        "company: the last CEO's post 'Hitting The Wall' (LinkedIn, 2019, archived) -> the next round fell through at "
        "the term sheet in May 2019; no Series A named",
        "sibling:a16z: its Rabbit row is identity-unresolved (rabb.it or the rabbit r1 maker) -> no round in its note",
    ],
    rounds=kept("rabbit")
    + [rnd("2013-02", "Seed", 3300000, None, True, SB_R, "press"),
       rnd("2015-02-09", "unnamed (Form D, equity)", 3806831, None, None, R_FD, "filing")],
    note=S + "StartUp Beat (2013-03-25): Rabbit 'just closed a $3.3 million Seed funding round in late February. "
             "Investors include Google Ventures'; Business Insider (2014-08-20) adds that it had 'yet to do its "
             "Series A'. GV entered at the seed (web_verified). S2A: the only later round on record is Rabbit, Inc.'s "
             "Form D of February 2015 ($3.8M sold), unnamed and below both $5M and twice the seed; a VC round then "
             "failed in May 2019, the service shut down and Kast bought its remaining assets (VentureBeat, "
             "2019-07-31): not graduated on a cited end."))

# ---- boxbee (GV's round precedes a named Series A)
TC_BOX = "https://techcrunch.com/2014/04/16/boxbee-2-3m-floodgate-gv/"
TECHCO_BOX = NEWS("boxbee", "Boxbee Raises $5M Series A")
L.append(jl.cls(
    "boxbee", stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TC_BOX, entry_date="2014-04-16",
    grad="graduated", grad_src="web_verified", grad_cite=TECHCO_BOX, grad_conf="high",
    rounds=kept("boxbee") + [rnd("2014-12-16", "Series A", 5000000, "Metamorphic Ventures", None, TECHCO_BOX,
                                 "press")],
    note=S + "GV's round is the $2.3M of April 2014 (TechCrunch, 2014-04-16, names Google Ventures among the "
             "investors), the only round reported between the company's 2013 AngelPad start and its next round, "
             "which is named: Boxbee 'raised $5 million in Series A funding led by Metamorphic Ventures' (tech.co, "
             "2014-12-16). The round before the Series A is the seed (model, medium: no page calls it a seed in "
             "words). S2A: that named Series A graduates the row: graduated."))

# ---- lendup (GV in the launch round; the next round named the Series A)
TC_LU12 = ("https://techcrunch.com/2012/10/10/lendup-raises-cash-from-kleiner-perkins-andreessen-horowitz-google-"
           "ventures-and-others-to-disrupt-payday-loans/")
TC_LU13 = ("https://techcrunch.com/2013/11/12/lendup-raises-14m-from-google-ventures-data-collective-to-disrupt-"
           "payday-lending/")
TC_LU16A = "https://techcrunch.com/2016/01/22/the-loan-dolphin/"
TC_LU16B = "https://techcrunch.com/2016/08/22/the-loan-dolphin-swims-again/"
L.append(jl.cls(
    "lendup", stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TC_LU12, entry_date="2012-10-10",
    grad="graduated", grad_src="web_verified", grad_cite=TC_LU16A, grad_conf="high",
    rounds=kept("lendup", lambda r: r.get("amount_usd") == 14000000)
    + [rnd("2013-11-12", "Series A", 14000000, "Google Ventures", True, TC_LU13, "press"),
       rnd("2016-01-22", "Series B", 50000000, None, True, TC_LU16A, "press"),
       rnd("2016-08-22", "Series C", 47500000, "Y Combinator Continuity", True, TC_LU16B, "press")],
    note=S + "GV's first money is the October 2012 launch round (TechCrunch, 2012-10-10, names Google Ventures among "
             "the VC firms and angels), and TechCrunch (2016-01-22) names the next round: 'It was time to raise a "
             "Series A', and 'Google Ventures led a $14 million round' (reported 2013-11-12). The launch round before "
             "that Series A is the seed (model, medium). S2A: the named $14M Series A of November 2013 graduates the "
             "row: graduated. The a16z row, in the same launch round, reads Series A."))

# ---- parse (GV in the pre-Series A money; the next round named the Series A)
TC_P11A = "https://techcrunch.com/2011/08/04/yc-funded-parse-a-heroku-for-mobile-apps/"
TC_P11B = "https://techcrunch.com/2011/11/09/parse-the-heroku-for-mobile-raises-5-5-million-series-a/"
L.append(jl.cls(
    "parse", stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TC_P11A, entry_date="2011-08-04",
    grad="graduated", grad_src="web_verified", grad_cite=TC_P11B, grad_conf="high",
    rounds=[rnd("2011-08-04", "unnamed (pre-Series A: $1.1M by August, $1.5M by November)", 1500000, None, True,
                TC_P11A, "press")]
    + kept("parse", lambda r: r.get("round") == "Seed"),
    note=S + "TechCrunch (2011-08-04): Parse 'has raised $1.1 million so far', with investors including YC, Start Fund, "
             "Google Ventures, Menlo Ventures and SV Angel; TechCrunch (2011-11-09) names the next round, a '$5.5 "
             "million Series A' led by Ignition Partners, after '$1.5 million from Y Combinator and some top angel "
             "investors'. GV's money is the pre-Series A seed (model, medium). S2A: the named Series A graduates the "
             "row: graduated."))

# ---- objective-logistics (GV in the first equity round; seed by its filing and band)
FIN_OL = NEWS("objective-logistics", "Objective Logistics Raises $1.5M")
OL_FD11 = sec_index(1534972, "0000897069-11-000419")
OL_FD12 = sec_index(1534972, "0001534972-12-000001")
OL_FD13 = sec_index(1534972, "0001534972-13-000002")
L.append(jl.cls(
    "objective-logistics", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"],
    entry_date="2011-11", grad="graduated", grad_src="web_verified", grad_cite=OL_FD13, grad_conf="medium",
    rounds=kept("objective-logistics", lambda r: r.get("amount_usd") == 1500000)
    + [rnd("2011-11-30", "unnamed", 1500000, "Atlas Venture and Google Ventures", True, FIN_OL, "press"),
       rnd("2011-11-08", "equity (Form D; the same round)", 1836784, None, None, OL_FD11, "filing"),
       rnd("2012-06-29", "notes (Form D)", 900000, None, None, OL_FD12, "filing"),
       rnd("2013-07-15", "equity (Form D)", 5361059, None, None, OL_FD13, "filing")],
    note=S + "FinSMEs (2011-11-30, read from its archived copy): the $1.5M round 'was led by Atlas Venture and Google "
             "Ventures', with NextView, Canary and individuals. It is Objective Logistics Inc.'s first Form D (CIK "
             "1534972, incorporated 2011; equity, first sale 2011-11-08, $1,836,784 sold), followed by notes in June "
             "2012 ($900K) and equity in July 2013 ($5,361,059 sold). A first equity round of that size in 2011 sits "
             "in the era's seed band ($2.5M): Seed, but no page names the round, so model, low, stage_uncited (as "
             "carnival-mobile). S2A: the July 2013 "
             "equity round is an unnamed later priced round above $5M and above twice the seed: graduated, at medium "
             "confidence because it may include the 2012 notes converting."))

jl.write("s1", L)
