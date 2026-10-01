#!/usr/bin/env python3
"""Stage and R7 pass, tag sta, rows 0-21 of queue/st.json (PRO-99). Run: NQ_TAG=sta python3 judgments-sta1.py

Stage keys, rounds and flags only (valuation and status belong to the A/B agents). A not_member row gets its verdict
line and nothing else.
"""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, NEWS, POST, W, FTS

L = []

# URLs read with WebFetch or through secget in this pass (each says what is cited).
ALIGN_424B4 = "https://www.sec.gov/Archives/edgar/data/1097149/000089843001000296/0000898430-01-000296.txt"
HW_BETTER = "https://www.housingwire.com/articles/39219-better-mortgage-raises-15-million-to-fund-expansion/"
TC_BUDDY = "https://techcrunch.com/2018/01/02/apple-buys-app-development-service-buddybuild/"
GCV_CASTLIGHT = "https://globalventuring.com/blog/2010/06/15/castlight-health-gains-strategic-investors-in-60m-series-c/"
CB_CHOOSE = "https://lb.crunchbase.com/funding_round/choose-energy-series-b--eac97f59"

# 0 akeana: R7 does not apply, the launch coverage names Kleiner Perkins; the 2021 round is not named.
AK = NEWS("akeana", "launches with $100M")
L.append(cls("akeana", stage="undetermined", entry_date="2021",
             rounds=[rnd("2024-08-13", "launch financing, over $100M in total (rounds not named)", 100000000, None,
                         True, AK, "press")],
             note="Stage pass: SiliconANGLE (2024-08-13) names Kleiner Perkins, Mayfield and Fidelity as the investors "
                  "behind the more than $100M raised by launch, so the listing is the firm's own money (no R7 case); "
                  "no source read names the 2021 round, so the stage stays undetermined."))

# 1 align-technology: the IPO prospectus lists the Kleiner entities' Series A.
L.append(cls("align-technology", stage="Series A", stage_src="web_verified", stage_cite=ALIGN_424B4, stage_conf="high",
             entry_date="1997", flags=["stage_disputes_band"],
             rounds=[rnd("1997", "Series A", None, None, True, ALIGN_424B4, "filing"),
                     rnd("1998", "Series B", None, None, True, ALIGN_424B4, "filing"),
                     rnd("1999-09-24", "Series C", 20744912, None, True, ALIGN_424B4, "filing"),
                     rnd("2000-05-25", "Series D", None, None, True, ALIGN_424B4, "filing")],
             note="Stage pass: the January 2001 prospectus's certain-transactions table shows the entities affiliated "
                  "with Kleiner Perkins holding 3,450,000 Series A, 1,620,656 Series B, 1,000,000 Series C and 283,124 "
                  "Series D preferred shares, with Joseph Lacob a director since August 1997: the entry is the Series A "
                  "of 1997. The Form D band (Growth, 2009) read a later filing and is disputed."))

# 2 ambiq-micro: KPCB XVI's earliest series is the Series C.
AMB = FTS("Ambiq", "424B4")
L.append(cls("ambiq-micro", stage="Growth", stage_src="web_verified", stage_cite=AMB, stage_conf="high",
             entry_date="2014",
             rounds=[rnd("2014", "Series C", None, None, True, AMB, "filing"),
                     rnd(None, "Series D", None, None, True, AMB, "filing"),
                     rnd(None, "Series E", None, None, True, AMB, "filing"),
                     rnd(None, "Series F", None, None, True, AMB, "filing"),
                     rnd("2025-07", "Series F-1 (pre-IPO)", 29999999.75, None, True, AMB, "filing")],
             note="Stage pass: the July 2025 prospectus's principal-stockholders note lists KPCB XVI's shares as "
                  "converted Series C, D, E and F preferred (and the Select Fund's Series F-1), so the earliest series "
                  "the firm bought is the Series C; Wen Hsieh joined the board in November 2014, the firm's own year. "
                  "Series C reads Growth."))

# 3 american-superconductor-corporation: pre-EDGAR IPO (1991); nothing names the 1987 round.
L.append(cls("american-superconductor-corporation", flags=["cite_pending"], rounds=[],
             note="Stage pass: the 1991 IPO predates EDGAR and no source read names the round of the firm's 1987 "
                  "entry; undetermined, cite pending."))

# 4 anthropic (stage only; the A/B agent holds the mark).
L.append(cls("anthropic", flags=["cite_pending"],
             note="Stage pass: no source read names Kleiner Perkins in an Anthropic round, so the 2025 entry stays "
                  "undetermined, cite pending."))

# 5 applied-materials
L.append(cls("applied-materials", flags=["cite_pending"], rounds=[],
             note="Stage pass: no private Kleiner Perkins round in Applied Materials is on record (listed since 1972; "
                  "on the firm's logo grid 2021-24 only); undetermined, cite pending, and the membership is worth a "
                  "second look under T3."))

# 6 assured (stage only)
L.append(cls("assured", flags=["cite_pending"],
             note="Stage pass: the firm's page for Ilya Fushman lists Assured and the site dates a Growth entry to "
                  "2024; the only round on record naming the firm is the 2025 one Bloomberg reports without a series, "
                  "so the stage stays undetermined, cite pending."))

# 7 audius: Kleiner Perkins is named in the Series A.
AU = NEWS("audius", "Audius raises $5.5M")
L.append(cls("audius", stage="Series A", stage_src="web_verified", stage_cite=AU, stage_conf="high",
             entry_date="2018-08-08",
             rounds=[rnd("2018-08-08", "Series A", 5500000, "General Catalyst; Lightspeed", True, AU, "press")],
             note="Stage pass: TechCrunch (2018-08-08): a $5.5M Series A led by General Catalyst and Lightspeed with "
                  "participation from Kleiner Perkins, Pantera and others, the firm's 2018 entry (no R7 case)."))

# 8 beam-dental: Kleiner Perkins led the Series C as a new investor.
BD = NEWS("beam-dental", "Series C Led by Kleiner")
L.append(cls("beam-dental", stage="Growth", stage_src="web_verified", stage_cite=BD, stage_conf="high",
             entry_date="2018-05-16",
             rounds=[rnd("2018-05-16", "Series C", 22500000, "Kleiner Perkins", True, BD, "company"),
                     rnd("2019-05-29", "Series D", 55000000, None, None, NEWS("beam-dental", "raises $55M Series D"),
                         "press")],
             note="Stage pass: the company's release of 2018-05-16 announces a $22.5M Series C led by Kleiner Perkins, "
                  "with Lucas Swisher joining the board, the firm's 2018 entry: Growth (no R7 case)."))

# 9 bedrock-systems
L.append(cls("bedrock-systems", stage="undetermined", entry_date="2020", rounds=[],
             note="Stage pass: no readable source names a BedRock Systems round; its October 2020 launch release "
                  "(Business Wire, not readable here) is reported to name Wing VC, Kleiner Perkins and SE Ventures as "
                  "backers, with Ted Schlein the partner, so no R7 case and the stage stays undetermined."))

# 10 better-mortgage: new investor in the Series B of February 2017.
L.append(cls("better-mortgage", stage="Growth", stage_src="web_verified", stage_cite=HW_BETTER, stage_conf="medium",
             entry_date="2017-02",
             rounds=[rnd("2016", "round of $30M (not named)", 30000000, None, False, HW_BETTER, "press"),
                     rnd("2017-02-09", "Series B", 15000000, None, True, HW_BETTER, "press"),
                     rnd("2019-08", "Series C", 160000000, None, None, W("Better.com"), "press")],
             note="Stage pass: HousingWire (February 2017): a $15M Series B from Goldman Sachs, Kleiner Perkins and "
                  "Pine Brook, after a $30M round the year before; the Wall Street Journal's headline of 2017-02-09 "
                  "calls it new Kleiner Perkins funding at a $220M valuation. Series B reads Growth; the firm's page "
                  "gives 2016 for a round announced in February 2017 (no R7 case)."))

# 11 betterworks: the round Kleiner Perkins led is not named.
BW = NEWS("betterworks", "Leaves Stealth")
L.append(cls("betterworks", stage="undetermined", entry_date="2013",
             rounds=[rnd("2014-09-23", "round of $15.5M announced at launch (not named)", 15500000,
                         "Kleiner Perkins Caufield & Byers", True, BW, "press")],
             note="Stage pass: TechCrunch (2014-09-23): $15.5M led by John Doerr and Bing Gordon of Kleiner Perkins "
                  "with Formation 8, announced as the company left stealth and not given a series name; the firm's "
                  "own year is 2013, so an earlier closing is possible and the stage stays undetermined (no R7 case)."))

# 12 bitstrips: a 2014 entry after the late-2013 round is the Series B the press reported the firm leading.
BS = NEWS("bitstrips", "Huge")
L.append(cls("bitstrips", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014",
             rounds=[rnd("2013-11", "round from Horizons Ventures (about $3M, the Series A)", 3000000,
                         "Horizons Ventures", False, W("Bitstrips"), "press"),
                     rnd("2014", "Series B (reported at about $15M, unconfirmed)", None,
                         "Kleiner Perkins Caufield & Byers (reported)", True, BS, "press")],
             note="Stage pass: BetaKit (2014-02-20) reports Bitstrips raising a Series B of about $15M that Kleiner "
                  "Perkins was said to be leading, after the $3M round of late 2013 from Horizons Ventures; neither "
                  "side confirmed it, so the firm's 2014 entry reads Growth from the model at medium (no R7 case)."))

# 13 bloom-energy: Doerr sits for the Series A preferred; first venture investor in 2002.
BE = FTS("Bloom Energy", "424B4")
L.append(cls("bloom-energy", stage="Series A", stage_src="web_verified", stage_cite=BE, stage_conf="high",
             entry_date="2002-05",
             rounds=[rnd("2002", "Series A", None, "Kleiner Perkins Caufield & Byers", True, BE, "filing")],
             note="Stage pass: the July 2018 prospectus says John Doerr, a director since May 2002, 'was designated as "
                  "the representative of our Series A preferred stock', and the shares sit in KPCB IX and X; the 2016 "
                  "draft says the firm became the first venture investor in 2002. The entry is the Series A."))

# 14 boston-scientific
L.append(cls("boston-scientific", flags=["cite_pending"], rounds=[],
             note="Stage pass: the 1992 IPO predates EDGAR and no source read names a 1991 round; undetermined, cite "
                  "pending."))

# 15 buddybuild: Kleiner Perkins led the Series A of May 2016.
L.append(cls("buddybuild", stage="Series A", stage_src="web_verified", stage_cite=TC_BUDDY, stage_conf="high",
             entry_date="2016-05",
             rounds=[rnd("2016-05", "Series A", 7600000, "Kleiner Perkins Caufield & Byers", True, TC_BUDDY, "press"),
                     rnd("2018-01-02", "Acquisition by Apple", None, None, None, TC_BUDDY, "press")],
             note="Stage pass: TechCrunch (2018-01-02): about $8.8M raised in all, including 'a $7.6 million Series A "
                  "led by Kleiner Perkins Caufield back in May of 2016', the firm's 2016 entry (no R7 case)."))

# 16 built (stage only; a membership question for the A/B agent)
L.append(cls("built", flags=["cite_pending"],
             note="Stage pass: no round naming Kleiner Perkins was found. The firm's page for Ilya Fushman lists Built "
                  "among his companies; he joined from Index Ventures in 2018, after the site's 2017 year, and the "
                  "row is on the live list only, so it carries the R7 signature and belongs in the membership check."))

# 17 caredx: the Form D band read a 2016 post-IPO filing; the firm has been in since January 2003.
CDX = "https://www.sec.gov/Archives/edgar/data/1217234/000119312514272185/d690692d424b4.htm"
L.append(cls("caredx", flags=["cite_pending"], entry_date="2003",
             rounds=[rnd("2003", "preferred round (series not named in the prospectus)", None, None, True, CDX,
                         "filing"),
                     rnd(None, "Series G", 2392759, None, True, CDX, "filing")],
             note="Stage pass: the July 2014 prospectus shows the shares in KPCB X-A and X-B with Brook Byers a "
                  "director since January 2003, so the entry is a 2003 round of XDx (founded 1998), not the 2016 "
                  "filing the Form D band read; the prospectus does not tie the funds to a series, so the Growth band "
                  "is kept with cite pending and the entry date corrected to 2003."))

# 18 castlight-health: R7, Mamoon Hamid at U.S. Venture Partners.
L.append(verdict("castlight-health", "not_member",
                 "partner-carried (R7): Mamoon Hamid backed it at U.S. Venture Partners in 2010; no round names a "
                 "Kleiner Perkins fund. U.S. Venture Partners joined the $60M Series C of June 2010 as a new investor "
                 "beside Maverick, Oak and Venrock (Global Corporate Venturing 2010-06-15), the year the site gives; "
                 "the firm's own page for Hamid lists Castlight Health among his companies and he joined Kleiner "
                 "Perkins in 2017; the 2014 IPO prospectus names no Kleiner Perkins entity; the row is on the live "
                 "list only, never on the kpcb.com archive (Erik 2026-09-17 partner-carried rule; decisions.md R7).",
                 ec="web", conf="medium", cite=GCV_CASTLIGHT))

# 19 chef-robotics: an existing backer by 2024; the entry round is not named.
CR = NEWS("chef-robotics", "14.75M")
L.append(cls("chef-robotics", stage="undetermined", entry_date="2019",
             rounds=[rnd("2021", "round of $7.7M (not named)", 7700000, None, None, CR, "press"),
                     rnd("2024-01-26", "equity and debt round of $14.75M", 14750000, None, True, CR, "press")],
             note="Stage pass: TechCrunch (2024-01-26) names Kleiner Perkins among the existing backers (with "
                  "Construct, Promus and Red and Blue) joining the $14.75M round, after a $7.7M raise in 2021; the "
                  "listing is the firm's own money (no R7 case), but the round of its 2019 entry is not named."))

# 20 chineseall
L.append(cls("chineseall", flags=["cite_pending"], rounds=[],
             note="Stage pass: no source read names the KPCB China round in ChineseAll; undetermined, cite pending."))

# 21 choose-energy: only a vendor profile names a round.
L.append(cls("choose-energy", stage="undetermined", entry_date="2012",
             rounds=[rnd("2013", "Series B", 7500000, None, True, CB_CHOOSE, "vendor")],
             note="Stage pass: Google News, TechCrunch and a web search return no report of a Choose Energy round; "
                  "only a vendor profile lists a $7.5M Series B in 2013 with Kleiner Perkins, which cannot cite, so "
                  "the firm's 2012 Growth entry stays undetermined (the Greentech team's deal, no R7 case)."))

jl.write("sta1", L)
