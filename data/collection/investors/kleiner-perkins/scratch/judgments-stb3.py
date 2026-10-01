#!/usr/bin/env python3
"""Stage and R7 pass, tag stb, third block of rows 65-129 of queue/st.json (PRO-99).
Run: NQ_TAG=stb python3 judgments-stb3.py

Stage keys, rounds and flags only.
"""
import json

import judge_lib as jl
from judge_lib import cls, rnd, NEWS, FTS, FORMD_CITE

L = []
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def old(slug, *subs):
    rs = (_CLS.get(slug) or {}).get("funding_rounds") or []
    return [r for r in rs if not subs or any(s.lower() in (r.get("round") or "").lower() for s in subs)]


# URLs read in this pass with curl, found through the TechCrunch and Crunchbase News searches.
TC_WAZE = "https://techcrunch.com/2011/10/18/social-navigation-and-traffic-app-waze-raises-30m-from-kleiner-perkins-and-li-ka-shing/"
CB_UJET_B = "https://news.crunchbase.com/venture/customer-support-startup-ujet-raises-25m-series-b-gv-citi-invest/"
TC_VEEM_17 = "https://techcrunch.com/2017/03/08/align-commerce-veem-24-million/"
CB_MINDBLOOM = "https://www.crunchbase.com/organization/mindbloom-938a"

# 115 true-north-therapeutics: an existing investor at the Series B, so in the Series A.
TN = NEWS("true-north-therapeutics", "What You Need to Know")
L.append(cls("true-north-therapeutics", stage="Series A", stage_src="web_verified", stage_cite=TN, stage_conf="medium",
             entry_date="2013",
             rounds=[rnd("2013", "Series A", 22000000, None, True, TN, "press"),
                     rnd("2014", "Series B", 35000000, "OrbiMed", True, TN, "press"),
                     rnd("2015-12-03", "Series C", 40000000, "New Leaf Venture Partners", True, TN, "press")],
             note="Stage pass: BioSpace (2015-12-02) lists a $22M Series A and a $35M Series B led by OrbiMed 'with "
                  "participation from existing investors Kleiner Perkins Caufield & Byers, MPM Capital, SR One and "
                  "Baxter Ventures', so the firm was in the only earlier round, the Series A, in the site's 2013 "
                  "year (Beth Seidenberg on the archived page). Medium because the article garbles the two rounds' "
                  "dates. No R7 case."))

# 117 twitter: the December 2010 round the firm led.
TW = NEWS("twitter", "$200m fundraising")
TW2 = NEWS("twitter", "Venture Capital investors in line")
L.append(cls("twitter", stage="Growth", stage_src="web_verified", stage_cite=TW, stage_conf="high",
             rounds=[rnd("2010-12", "$200M round at a $3.7B valuation", 200000000,
                         "Kleiner Perkins Caufield & Byers", True, TW2, "press")],
             note="Stage pass: the Guardian (2010-12-16) says the $200M investment 'came mainly from the Silicon "
                  "Valley venture capital house Kleiner Perkins Caufield & Byers', and the Mercury News IPO timeline "
                  "has it leading that round in December 2010, the firm's 2010 year and its Digital Growth Fund; a "
                  "$200M round at $3.7B reads Growth. Cited, no longer model; no R7 case."))

# 118 uber: the June 2014 round at $17B.
UB = NEWS("uber", "Why Uber Might Well")
L.append(cls("uber", stage="Growth", stage_src="web_verified", stage_cite=UB, stage_conf="high",
             rounds=[rnd("2014-06", "$1.2B round at a $17B valuation (Series D)", 1200000000, "Fidelity Investments",
                         True, UB, "press")],
             note="Stage pass: the New York Times (DealBook, 2014-06-09) lists Kleiner Perkins Caufield & Byers "
                  "among the investors who 'plowed $1.2 billion into the company' in June 2014, with Fidelity, "
                  "BlackRock, Google Ventures, Menlo, Wellington and Summit; the firm's 2014 year and its Digital "
                  "Growth Fund. Cited, no longer model."))

# 119 ujet: a Series A investor, per the Series B report.
L.append(cls("ujet", stage="Series A", stage_src="web_verified", stage_cite=CB_UJET_B, stage_conf="high",
             entry_date="2017-05",
             rounds=[rnd("2016-03", "Seed", 6600000, None, False, CB_UJET_B, "press"),
                     rnd("2017-05", "Series A", 13400000, None, True, CB_UJET_B, "press"),
                     rnd("2018-02-13", "Series B", 25000000, "GV", True, CB_UJET_B, "press")],
             note="Stage pass: Crunchbase News (2018-02-13) says 'Two investors from UJET's Series A round, Kleiner "
                  "Perkins and DCM Ventures, followed on' in the $25M Series B, with Ted Schlein on the board, and "
                  "dates the $13.4M Series A to May 2017 after a $6.6M seed from Resolute, DCM and Relay; the "
                  "site's 2017 year. No R7 case."))

# 120 veem: the firm's first deal with Align Commerce, November 2015; the label is not in a page read.
VM = NEWS("veem", "First Bitcoin-Related")
L.append(cls("veem", stage="Series A", stage_src="model", stage_cite=VM, stage_conf="medium",
             entry_date="2015-11-17",
             rounds=[rnd("2015-11-17", "$12.5M round (Series A)", 12500000, "Kleiner Perkins Caufield & Byers", True,
                         NEWS("veem", "raises $12.5 million"), "press"),
                     rnd("2017-03-08", "$24M round", 24000000, "NAB Ventures", True, TC_VEEM_17, "press")],
             note="Stage pass: the Wall Street Journal's headline of 2015-11-17 is 'Kleiner Perkins Makes First "
                  "Bitcoin-Related Deal With Align Commerce' and Finextra the same day reports the $12.5M raise, the "
                  "site's 2015 year; TechCrunch (2017-03-08) names the firm again in the $24M round. Both 2015 pages "
                  "refuse a fetch, so the Series A label is model knowledge of that $12.5M round, not a line read. "
                  "No R7 case."))

# 122 vera-therapeutics: the prospectus has KPCB XVI holding Series A; the Growth band is disputed.
VE = FTS("Vera Therapeutics", "S-1")
L.append(cls("vera-therapeutics", stage="Series A", stage_src="web_verified", stage_cite=VE, stage_conf="high",
             entry_date="2016-06", flags=["stage_disputes_band"],
             rounds=[rnd("2016-06", "Series A", None, None, True, VE, "filing"),
                     rnd(None, "Series B", None, None, True, VE, "filing"),
                     rnd("2020-10-29", "Series C", 80000000, "Abingworth", True, VE, "filing")],
             note="Stage pass: the 2021 prospectus's principal-stockholders note has Kleiner Perkins Caufield & "
                  "Byers XVI holding 4,746,224 shares of Series A preferred, then Series B and Series C, with Beth "
                  "Seidenberg on the board since June 2016, the site's year. The Form D that set the Growth band is "
                  "the 2020 Series C, a follow-on, so the band is disputed: Series A."))

# 123 veracyte: a founding investor; the prospectus shows the position but not the series by holder.
VC = FTS("VERACYTE", "S-1")
L.append(cls("veracyte", stage="Series A", stage_src="model", stage_cite=VC, stage_conf="medium",
             flags=["cite_pending"],
             rounds=[rnd(None, "Series A (22.4M shares at $1.00)", 22400000, None, True, VC, "filing"),
                     rnd("2010-06-04", "Series B (Form D, $28.4M)", 28435000, None, True, FORMD_CITE("veracyte", 0),
                         "filing"),
                     rnd("2012", "Series C", None, None, True, VC, "filing")],
             note="Stage pass: the 2013 prospectus has Brook Byers on the board since January 2007 (the company was "
                  "the incubator Calderome until 2008) and KPCB Holdings buying 4,016,000 Series B and 3,158,385 "
                  "Series C shares, against 12,697,935 shares held by KPCB XII; the only preferred stock before the "
                  "2010 Series B was the Series A at $1.00, so the founding position reads Series A. The filing does "
                  "not print the Series A holders, so the source is model and the citation stays owed."))

# 127 waze: the October 2011 round from the Digital Growth Fund and the iFund.
L.append(cls("waze", stage="Growth", stage_src="web_verified", stage_cite=TC_WAZE, stage_conf="high",
             entry_date="2011-10-18",
             rounds=old("waze", "second round")
                    + [rnd("2011-10-18", "third round, $30M", 30000000, "Horizons Ventures; Kleiner Perkins", True,
                           TC_WAZE, "press")],
             note="Stage pass: TechCrunch (2011-10-18) reports $30M of new funding from Horizons Ventures and 'the "
                  "Kleiner Perkins Caufield & Byers Digital Growth Fund and iFund', bringing the total to over $55M, "
                  "with Mary Meeker a board observer; the company's third round, so Growth. Cited, no longer model; "
                  "no R7 case."))

# 69 mindbloom: vendor profiles only.
L.append(cls("mindbloom", stage="undetermined", entry_date="2021",
             rounds=[rnd("2020-09-10", "Series A", 8000000, None, None, CB_MINDBLOOM, "vendor"),
                     rnd("2021-09-22", "Series B", None, None, None, CB_MINDBLOOM, "vendor")],
             note="Stage pass: only vendor profiles carry Mindbloom's rounds (an $8M Series A in September 2020, a "
                  "Series B in September 2021, the site's year) and they list Kleiner Perkins beside 8VC and Founders "
                  "Fund without tying it to a round; no press or company source read names the round, and none shows "
                  "a partner's previous firm behind the listing, so it stands and the stage stays undetermined."))

# 112, 124, 128: searched, nothing found.
L.append(cls("trace-data",
             note="Stage pass: Google News, TechCrunch and Crunchbase News return no funding report for Trace Data; no "
                  "round is on record and no partner's previous firm explains the 2019 listing, so it stands and "
                  "the stage stays undetermined."))
L.append(cls("visly",
             note="Stage pass: Visly was in Y Combinator's Winter 2019 batch (TechCrunch, 2019-03-19); no funding "
                  "report names a round or Kleiner Perkins, and no partner's previous firm explains the listing, so "
                  "it stands and the stage stays undetermined."))
L.append(cls("willo",
             note="Stage pass: Google News returns product coverage only for Willo, no funding report; no round is on "
                  "record and no partner's previous firm explains the 2017 listing, so it stands and the stage "
                  "stays undetermined."))

jl.write("stb3", L)
