#!/usr/bin/env python3
"""Stage and R7 pass, tag stb, second block of rows 65-129 of queue/st.json (PRO-99).
Run: NQ_TAG=stb python3 judgments-stb2.py

Stage keys, rounds and flags only. The ab1 rows the A/B agents had already staged and cited when this block was
written (rebellion-defense, sierra, stord, stripe, transcarent, turo, viz-ai, watershed, xendit) are left as they
stand: this pass read the same rounds and agrees with them.
"""
import json

import judge_lib as jl
from judge_lib import cls, rnd, NEWS, FTS, SITE, W, FORMD_CITE

L = []
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def old(slug, *subs):
    rs = (_CLS.get(slug) or {}).get("funding_rounds") or []
    return [r for r in rs if not subs or any(s.lower() in (r.get("round") or "").lower() for s in subs)]


# URLs read in this pass with curl or secget, found through the TechCrunch search or a web search.
TC_PLEX_18 = "https://techcrunch.com/2018/01/08/podcasts-are-coming-to-plex-followed-by-web-series-and-other-digital-media/"
TC_PLEX_21 = "https://techcrunch.com/2021/04/14/plex-raises-50m-growth-round-to-fuel-ad-supported-streaming-expansions/"
TC_PLEX_24 = "https://techcrunch.com/2024/01/29/streaming-media-company-plex-raises-new-funds-as-it-nears-profitability/"
TC_SEGMENT_B = "https://techcrunch.com/2015/10/09/segment-raises-27-million-for-its-one-api-to-rule-them-all/"
TC_SMAX_E = "https://techcrunch.com/2014/03/04/field-service-software-developer-servicemax-raises-71m-from-kleiner-perkins-meritech-capital/"
TC_SMAX_10 = "https://techcrunch.com/2010/04/13/saas-field-service-software-servicemax-raises-10-million-from-salesforce-and-others/"
TC_SMAX_11 = "https://techcrunch.com/2011/06/08/saas-field-service-software-servicemax-raises-14m-from-mayfield-salesforce-and-others/"
TC_SESSIONM_B = "https://techcrunch.com/2012/05/08/sessionm-series-b/"
TC_SESSIONM_E = "https://techcrunch.com/2018/07/23/sessionm-customer-loyalty-data-aggregator-snags-23-8-m-investment/"
TC_STACKBIT = "https://techcrunch.com/2021/02/01/kleiner-perkins-bucky-moore-will-outline-what-to-think-about-before-raising-a-series-a-at-early-stage-in-april/"
CB_STACKBIT_SEED = "https://www.crunchbase.com/funding_round/stackbit-seed--c8fe516e"
CB_STACKBIT = "https://www.crunchbase.com/organization/stackbit"
QS_S4 = "https://www.sec.gov/Archives/edgar/data/1811414/000119312520249736/d14810ds4.htm"

# 86 plex: TechCrunch names the 2014 round the firm led.
L.append(cls("plex", stage="Series A", stage_src="web_verified", stage_cite=TC_PLEX_18, stage_conf="medium",
             entry_date="2014",
             rounds=[rnd("2014", "Series A", 10000000, "Kleiner Perkins", True, TC_PLEX_18, "press"),
                     rnd("2021-04-14", "Series C (growth round, about $15M of it new capital)", 50000000, "Intercap",
                         True, TC_PLEX_21, "press"),
                     rnd("2024-01-29", "Series C-3", 40000000, "Intercap", True, TC_PLEX_24, "press")],
             note="Stage pass: TechCrunch (2018-01-08) writes of 'its seed and its $10 million Series A led by "
                  "Kleiner Perkins in 2014', the site's year; TechCrunch's reports of the 2021 and 2024 rounds name "
                  "Kleiner Perkins an existing investor. Medium because the 2021 report calls that round 'technically "
                  "Plex's Series C' with no Series B between on record. No R7 case, a Kleiner Perkins fund led the "
                  "round."))

# 92 quantumscape: the merger filings give the board seat and the holding, not the series.
L.append(cls("quantumscape", flags=["cite_pending"],
             note="Stage pass: the 2020 merger prospectus and the S-1 have John Doerr on the board since December "
                  "2010 and KPCB Holdings as a 5% holder, but list no preferred series by holder, and no press "
                  "source read names the 2010 round; the Series A label stays model and the citation stays owed."))

# 98 segment: Kleiner Perkins is an existing investor by the 2015 Series B; the round it entered is not on record.
L.append(cls("segment", stage="undetermined",
             rounds=[rnd("2014", "$15M round from Accel and others (the Series A)", 15000000, "Accel", None,
                         TC_SEGMENT_B, "press"),
                     rnd("2015-10-09", "Series B", 27000000, "Thrive Capital", True, TC_SEGMENT_B, "press")],
             note="Stage pass: TechCrunch (2015-10-09) names Kleiner Perkins Caufield & Byers an existing investor at "
                  "the $27M Series B led by Thrive, and the firm's own page for Ted Schlein lists Segment, so the "
                  "listing is the firm's own money (no R7 case). Whether it entered at the 2013 seed, as the site's "
                  "year suggests, or at the $15M round of 2014 is not on a citable record (vendor profiles put it in "
                  "the 2014 Series A), so the stage stays undetermined."))

# 99 servicemax: the March 2014 Series E the firm co-led.
L.append(cls("servicemax", stage="Growth", stage_src="web_verified", stage_cite=TC_SMAX_E, stage_conf="high",
             entry_date="2014-03-04",
             rounds=[rnd("2010-04-13", "$8M round", 8000000, None, False, TC_SMAX_10, "press"),
                     rnd("2011-06-08", "$14M round", 14000000, "Mayfield", False, TC_SMAX_11, "press"),
                     rnd("2014-03-04", "Series E", 71000000, "Meritech Capital; Kleiner Perkins", True, TC_SMAX_E,
                         "press")],
             note="Stage pass: TechCrunch (2014-03-04) reports the $71M Series E led by Meritech Capital and Kleiner "
                  "Perkins, with the existing investors listed separately; the firm's 2014 year and its Green Growth "
                  "Fund. Cited, no longer model; no R7 case."))

# 100 sessionm: the initial $6.5M round from the iFund and Highland, the round before the 2012 Series B.
L.append(cls("sessionm", stage="Series A", stage_src="web_verified", stage_cite=TC_SESSIONM_B, stage_conf="medium",
             entry_date="2011",
             rounds=[rnd("2011", "initial $6.5M round (the round before the Series B)", 6500000,
                         "Kleiner Perkins iFund; Highland Capital Partners", True, TC_SESSIONM_B, "press"),
                     rnd("2012-05-08", "Series B", 20000000, "Charles River Ventures", True, TC_SESSIONM_B, "press"),
                     rnd("2016", "Series D", 35000000, "Salesforce Ventures", None, TC_SESSIONM_E, "press"),
                     rnd("2018-07-23", "Series E", 23800000, "Salesforce Ventures", True, TC_SESSIONM_E, "press")],
             note="Stage pass: TechCrunch (2012-05-08) says the founder started SessionM 'initially raising a $6.5 "
                  "million round from Kleiner's iFund and Highland' and names both as past investors in the $20M "
                  "Series B; the first round before a Series B reads Series A, medium because the report does not "
                  "print the label. The firm's 2011 year and its iFund. No R7 case."))

# 102 spacex: no round names the firm.
L.append(cls("spacex", flags=["cite_pending"],
             note="Stage pass: no source read names a Kleiner Perkins fund in a SpaceX round or tender; the Growth "
                  "label rests on the site's 2023 year (every 2023 transaction was a tender or late primary at about "
                  "$150B), so the citation stays owed."))

# 103 spotify: the June 2011 round at $1B.
SP = NEWS("spotify", "latest funding values it at $1bn")
L.append(cls("spotify", stage="Growth", stage_src="web_verified", stage_cite=SP, stage_conf="high",
             entry_date="2011-06-17",
             rounds=[rnd("2011-06-17", "$100M round at a $1B valuation", 100000000, "Digital Sky Technologies", True,
                         SP, "press")] + old("spotify"),
             note="Stage pass: the Guardian (2011-06-17) reports the $100M round at a $1B valuation 'with Facebook "
                  "investor Digital Sky Technologies, Twitter backer Kleiner Perkins and Accel', the firm's 2011 year "
                  "and its Digital Growth Fund, after the 2008 to 2010 venture rounds: Growth. Cited, no longer "
                  "model."))

# 104 square: the firm's own page names the round it led.
SQ = SITE("square")
L.append(cls("square", stage="Growth", stage_src="first_party", stage_cite=SQ, stage_conf="high",
             entry_date="2011-06-27",
             rounds=[rnd("2011-01-10", "Series B (Form D, $31.7M)", 31749894, "Sequoia Capital", None,
                         FORMD_CITE("square", 1), "filing"),
                     rnd("2011-06-27", "Series C, the $100M round the firm led", 100000000, "Kleiner Perkins", True, SQ,
                         "firm")],
             note="Stage pass: the firm's own page says 'KP led Square's $100 million funding round in 2011, with a "
                  "KP partner joining the company's board'; the Form D dates that round's first sale 2011-06-27 and "
                  "Wikipedia lists it as the Series C, after Khosla's Series A and Sequoia's Series B. First-party, "
                  "and it agrees with the Growth band."))
W("Block, Inc.")  # the article read for the series names is on disk

# 105 stackbit: the firm's own partner sits on the board; the round is on vendor pages only.
L.append(cls("stackbit", stage="undetermined",
             rounds=[rnd("2019", "Seed", 4150000, None, True, CB_STACKBIT_SEED, "vendor"),
                     rnd("2020-10", "Series A", 10200000, None, True, CB_STACKBIT, "vendor")],
             note="Stage pass: TechCrunch (2021-02-01) has Bucky Moore of Kleiner Perkins on Stackbit's board, so the "
                  "listing is the firm's own deal (no R7 case). Only vendor profiles name the rounds (a $4.15M seed "
                  "in 2019 with Kleiner Perkins, a $10.2M Series A in October 2020); a vendor page never cites, so "
                  "the stage stays undetermined with the rounds on file."))

# 110 teladoc: the prospectus makes the firm's partner the Series D designee.
TD = FTS("Teladoc", "S-1")
L.append(cls("teladoc", stage="Growth", stage_src="web_verified", stage_cite=TD, stage_conf="high",
             entry_date="2011-08-25",
             rounds=[rnd("2011-08-25", "Series D", 18600003, None, True, FORMD_CITE("teladoc", 4), "filing")]
                    + old("teladoc", "Series E")
                    + [rnd("2014-09-09", "Series F", 50250081, None, True, TD, "filing")],
             note="Stage pass: the 2015 prospectus says Dana Mead, a Kleiner Perkins partner, joined the board in "
                  "August 2011 and is 'the designee of our Series D convertible preferred stock', with entities "
                  "associated with Kleiner Perkins party to the investors' rights agreement; the $18.6M Form D of "
                  "2011-08-25 is that round. Its related-party table has KPCB Holdings buying Series F in 2014. "
                  "Series D is the entry: Growth, now cited to the filing."))

# 111 thatgamecompany: the May 2014 Series B.
TG = NEWS("thatgamecompany", "Raises $7 Million")
L.append(cls("thatgamecompany", stage="Growth", stage_src="web_verified", stage_cite=TG, stage_conf="high",
             entry_date="2014-05-27",
             rounds=[rnd("2014-05-27", "Series B", 7000000, "Capital Today", True, TG, "press")]
                    + old("thatgamecompany", "investment"),
             note="Stage pass: Variety (2014-05-27) says Capital Today led 'the Series B round of financing, along "
                  "with venture capital firm Benchmark Capital, and a half-dozen individual investors and investment "
                  "companies, including Kleiner Perkins Caulfield & Byers', the site's 2014 year: Growth. No R7 "
                  "case."))

# 114 transmedics: the band stands; the round is on file.
L.append(cls("transmedics",
             rounds=[rnd("2010-02-17", "preferred round (Form D, $35.4M)", 35414792, None, True,
                         FORMD_CITE("transmedics", 2), "filing")],
             note="Stage pass: the 2019 prospectus names Kleiner Perkins Caufield & Byers XIII as the holder and "
                  "lists a later purchase in its name, but does not date the earlier series; the $35.4M Form D of "
                  "2010-02-17 with Joseph Lacob as a director is the entry, twelve years after the 1998 founding and "
                  "after several earlier preferred rounds, so the Growth band stands on the filing structure."))

jl.write("stb2", L)
