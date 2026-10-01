#!/usr/bin/env python3
"""Stage and R7 pass, tag sta, rows 44-64 of queue/st.json (PRO-99). Run: NQ_TAG=sta python3 judgments-sta3.py

Stage keys, rounds and flags only (valuation and status belong to the A/B agents). A not_member row gets its verdict
line and nothing else. labelbox (row 61) is already Seed, web_verified and graduated on disk: nothing emitted.
"""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, NEWS, POST, W, FTS

L = []

# URLs read with WebFetch in this pass (each says what is cited).
TC_HYLA = "https://techcrunch.com/2011/12/20/erecyclingcorps-raises-35m-from-kleiner-perkins-to-attack-the-e-waste-problem/"
PRN_HYLA_C = "https://www.prnewswire.com/news-releases/erecycling-group-secures-105-million-in-series-c-funding-229536621.html"
TC_INSTAEDU = "https://techcrunch.com/2013/08/14/instaedu-series-a-battery-ventures/"
TC_KARMA = ("https://techcrunch.com/2012/02/27/sequoia-kleiner-perkins-and-obvious-put-4-5m-in-sleek-social-mobile-"
            "gifting-platform-karma/")
TC_KATANGO = "https://techcrunch.com/2011/05/31/under-the-covers-at-katango-kleiner-perkins-first-sfund-investment/"
TC_KLOUT = ("https://techcrunch.com/2011/01/10/klout-lands-8-5-million-from-kleiner-perkins-and-greycroft-to-measure-"
            "social-influence/")
TC_LUV = ("https://techcrunch.com/2013/05/16/luvocracy-raises-11m-from-kleiner-perkins-google-ventures-and-others-to-"
          "master-ecommerce-and-social-recommendations/")

# 44 genscript
L.append(cls("genscript", flags=["cite_pending"],
             note="Stage pass: no source read names the KPCB China round in GenScript; undetermined, cite pending."))

# 45 google: the June 1999 round is on record, its series is not tied to the firm.
GW = W("Google")
G424 = FTS("Google Inc.", "424B4")
L.append(cls("google", flags=["cite_pending"],
             rounds=[rnd("1999-06-07", "equity round of $25M (announced without a series name)", 25000000,
                         "Kleiner Perkins; Sequoia Capital", True, GW, "press"),
                     rnd("2004-08-19", "IPO: the KPCB IX funds hold 21,043,711 shares", None, None, True, G424,
                         "filing")],
             note="Stage pass: the August 2004 prospectus lists 21,043,711 shares held by KPCB IX-A, IX-B and the "
                  "Information Sciences Zaibatsu Fund II, with John Doerr a director since May 1999, but does not say "
                  "which preferred series they bought (its notes show Series B preferred warrants issued in 1999); the "
                  "$25M round of 1999-06-07 was announced without a series name. Undetermined, cite pending: if the "
                  "1999 round is the Series B, the taxonomy reads it Growth."))

# 46 harmonic-lightwaves
L.append(cls("harmonic-lightwaves", flags=["cite_pending"],
             note="Stage pass: EDGAR holds no prospectus of the 1995 IPO (the earliest Harmonic filings are from "
                  "1997) and no source read names the 1989 round; undetermined, cite pending."))

# 47 harvey: the firm's own post, co-leading the Series B.
HV = POST("harvey-ai")
HW = W("Harvey (software)")
L.append(cls("harvey", stage="Growth", stage_src="first_party", stage_cite=HV, stage_conf="medium",
             entry_date="2023-12-19", flags=["stage_disputes_band"],
             rounds=[rnd("2022-11", "seed round of $5M", 5000000, "OpenAI Startup Fund", False, HW, "press"),
                     rnd("2023-04", "round of $23M (the Series A)", 23000000, "Sequoia Capital", False, HW, "press"),
                     rnd("2023-12-19", "Series B", 80000000, "Elad Gil; Kleiner Perkins", True, HV, "firm"),
                     rnd("2024-07", "Series C", 100000000, "GV", True, HW, "press"),
                     rnd("2025-02", "Series D", 300000000, None, None, HW, "press"),
                     rnd("2025-06", "Series E", 300000000, "Kleiner Perkins; Coatue", True, HW, "press"),
                     rnd("2025-12", "Series F", 160000000, "Andreessen Horowitz", True, HW, "press")],
             note="Stage pass: the firm's post of 2023-12-19: 'We couldn't be more thrilled to co-lead their Series B', "
                  "the first round naming Kleiner Perkins; Wikipedia gives the November 2022 seed to the OpenAI "
                  "Startup Fund and the April 2023 round to Sequoia without the firm. Series B reads Growth. The Form "
                  "D band (Series A, 2023-04-10) dates the company's first filing, not the firm's entry (its only "
                  "roster match is from 2026), and is disputed; medium because no source says outright that the firm "
                  "was absent in April 2023."))

# 48 houzz (stage only)
L.append(cls("houzz", flags=["cite_pending"],
             note="Stage pass: no source read names Kleiner Perkins in a Houzz round (the news read covers 2014 and "
                  "2017); undetermined, cite pending."))

# 49 huntress: the firm's own post, co-leading the Series D.
HU = POST("huntress-series-d")
L.append(cls("huntress", stage="Growth", stage_src="first_party", stage_cite=HU, stage_conf="high",
             rounds=[rnd("2024-06-18", "Series D", 150000000, "Kleiner Perkins; Meritech; Sapphire", True, HU, "firm")],
             note="Stage pass: the firm's post of 2024-06-18: 'Kleiner Perkins is co-leading Huntress' Series D "
                  "alongside our friends at Meritech and Sapphire', the 2024 entry the Form D band already read as "
                  "Growth."))

# 50 hyla: the $35M round of December 2011 from the Green Growth Fund, the round before the Series C.
L.append(cls("hyla", stage="Growth", stage_src="web_verified", stage_cite=TC_HYLA, stage_conf="medium",
             entry_date="2011-12-20",
             rounds=[rnd("2009", "founding investments (OpenAir Equity Partners, SJF Ventures)", None, None, False,
                         PRN_HYLA_C, "company"),
                     rnd("2011-12-20", "round of $35M (series not named)", 35000000,
                         "Kleiner Perkins Caufield & Byers", True, TC_HYLA, "press"),
                     rnd("2013", "Series C", 105000000, "Kleiner Perkins Caufield & Byers", True, PRN_HYLA_C,
                         "company")],
             note="Stage pass: TechCrunch (2011-12-20): eRecyclingCorps (HYLA's former name) raised $35M in a round "
                  "led by Kleiner Perkins; the company's Series C release says the firm 'made their initial investment "
                  "in eRC in December 2011' through the Green Growth Fund, after the 2009 founding investments. The "
                  "round between the founding money and the Series C reads Growth, at medium because its series is "
                  "not named (no R7 case)."))

# 51 idec-pharmaceuticals
L.append(cls("idec-pharmaceuticals", flags=["cite_pending"],
             note="Stage pass: the 1991 IPO predates EDGAR and no source read names the 1986 round; undetermined, "
                  "cite pending."))

# 52 inspire-medical-systems: Kleiner Perkins designates a Series A director.
INSP = FTS("Inspire Medical", "424B4")
L.append(cls("inspire-medical-systems", stage="Series A", stage_src="web_verified", stage_cite=INSP,
             stage_conf="medium", entry_date="2008", flags=["stage_disputes_band"],
             rounds=[rnd("2008", "Series A", None, None, True, INSP, "filing"),
                     rnd("2016-07", "bridge notes", 4000000, None, True, INSP, "filing")],
             note="Stage pass: the May 2018 prospectus's voting agreement seats 'a designee of U.S. Venture Partners "
                  "IX, L.P. and a designee of Kleiner Perkins Caufield & Byers as the Series A Directors', and Dana "
                  "Mead has sat on the board since July 2008, soon after the November 2007 spin-out from Medtronic: "
                  "the entry is the Series A. The Form D band (Growth, 2016) read a later filing and is disputed; "
                  "medium because the prospectus does not date the Series A closing."))

# 53 instaedu: R7, Mamoon Hamid at Social+Capital.
L.append(verdict("instaedu", "not_member",
                 "partner-carried (R7): Mamoon Hamid backed it at The Social+Capital Partnership in 2012; no round "
                 "names a Kleiner Perkins fund. Social+Capital led the 2012 seed and joined the $4M Series A that "
                 "Battery Ventures led (TechCrunch 2013-08-14, $5.1M raised in all before the 2014 sale to Chegg); "
                 "Hamid is the director on the July 2013 Form D; the firm's own page for Hamid lists InstaEDU among "
                 "his companies and he joined Kleiner Perkins in 2017; the row is on the live list only, never on "
                 "the kpcb.com archive (Erik 2026-09-17 partner-carried rule; decisions.md R7).",
                 ec="web", conf="medium", cite=TC_INSTAEDU))

# 54 interos: named in the 2019 Series A.
IN = NEWS("interos", "17.5M Series B")
L.append(cls("interos", stage="Series A", stage_src="web_verified", stage_cite=IN, stage_conf="high",
             rounds=[rnd("2019", "Series A", 8350000, None, True, IN, "press"),
                     rnd("2020-03-12", "Series B", 17500000, "Venrock", True, IN, "press")],
             note="Stage pass: Crunchbase News (2020-03-12): the $17.5M Series B was 'led by Venrock with "
                  "participation from Kleiner Perkins, which also invested in the company's $8.35 million Series A "
                  "last year', which the firm's own post of the same day ('for the past year') and the Form D band "
                  "agree with."))

# 55 intuit
L.append(cls("intuit", flags=["cite_pending"],
             note="Stage pass: the 1993 IPO predates EDGAR and no source read names the 1990 round; undetermined, "
                  "cite pending."))

# 56 jd-com
L.append(cls("jd-com", flags=["cite_pending"],
             note="Stage pass: the May 2014 prospectus names the KPCB funds only among the holders who gave their "
                  "voting proxy, without the round they bought; the Growth reading stands on the model, cite pending."))

# 57 karma-science: the 2011 round is on record without a name.
L.append(cls("karma-science", stage="undetermined", entry_date="2011",
             rounds=[rnd("2011", "round of about $4.5M (not named), disclosed in SEC documents", 4500000, None, True,
                         TC_KARMA, "press")],
             note="Stage pass: TechCrunch (2012-02-27): about $4.5M raised in summer 2011 from Kleiner Perkins, "
                  "Sequoia, The Obvious Corporation, Felicis and angels, with no series named; the sFund entry is the "
                  "firm's own money (no R7 case) and the stage stays undetermined."))

# 58 katango: the sFund's Series A.
L.append(cls("katango", stage="Series A", stage_src="web_verified", stage_cite=TC_KATANGO, stage_conf="high",
             entry_date="2010-10",
             rounds=[rnd("2010-10", "Series A", 5000000, "Kleiner Perkins (sFund)", True, TC_KATANGO, "press")],
             note="Stage pass: TechCrunch (2011-05-31): Katango 'received $5 million in series A from Kleiner', the "
                  "sFund's first investment, announced in October 2010, the firm's own year (no R7 case)."))

# 59 kingnet
L.append(cls("kingnet", flags=["cite_pending"],
             note="Stage pass: no source read names the KPCB China round in Kingnet; undetermined, cite pending."))

# 60 klout: the sFund led the $8.5M round, whose series the record does not name.
L.append(cls("klout", stage="undetermined", entry_date="2011-01",
             rounds=[rnd("2011-01-10", "round of $8.5M (series not named; a vendor profile calls it Series B)",
                         8500000, "Kleiner Perkins Caufield & Byers sFund", True, TC_KLOUT, "press")],
             note="Stage pass: TechCrunch and the company's release (2011-01-10): $8.5M 'led by the Kleiner Perkins "
                  "Caufield & Byers recently launched sFund' with Greycroft, Bing Gordon joining the board, bringing "
                  "the total to more than $10M; neither names the series (Series A or B), so the stage stays "
                  "undetermined. The firm's own money, no R7 case."))

# 62 lumafield: co-led the 2019 seed; the 2020 Series A graduates it.
LF = NEWS("lumafield", "Emerges from Stealth")
L.append(cls("lumafield", stage="Seed", stage_src="web_verified", stage_cite=LF, stage_conf="high", entry_date="2019",
             grad="graduated", grad_src="web_verified", grad_cite=LF, grad_conf="high", grad_asof="2022-04-13",
             rounds=[rnd("2019", "Seed", None, "Lux Capital; Kleiner Perkins", True, LF, "company"),
                     rnd("2020", "Series A", None, "DCVC", True, LF, "company"),
                     rnd("2022-09-12", "Series B", 35000000, None, None, NEWS("lumafield", "35M Series B"), "company")],
             note="Stage pass: the company's release of 2022-04-13: 'Lux Capital and Kleiner Perkins led Lumafield's "
                  "2019 seed round' and 'DCVC led Lumafield's 2020 series A funding with additional participation "
                  "from Lux and Kleiner Perkins', $32.5M raised in all: Seed, graduated (no R7 case)."))

# 63 lumeris
L.append(cls("lumeris", stage="undetermined", entry_date="2011",
             rounds=[rnd("2012-02-14", "financing reported by the New York Times Bits blog (not readable here)", None,
                         None, None, NEWS("lumeris", "Doerr"), "press")],
             note="Stage pass: the only report found is a New York Times Bits headline of 2012-02-14 on John Doerr's "
                  "health care start-up, which could not be read; no source names the round of the 2011 entry, so the "
                  "stage stays undetermined (John Doerr's deal, no R7 case)."))

# 64 luvocracy: named in the $11M raised by May 2013, rounds not named.
L.append(cls("luvocracy", stage="undetermined", entry_date="2012",
             rounds=[rnd("2013-05-16", "$11M raised to date (rounds not named)", 11000000, None, True, TC_LUV,
                         "press")],
             note="Stage pass: TechCrunch (2013-05-16): $11M in funding from Kleiner Perkins, Google Ventures, "
                  "CrunchFund and angels, with Bing Gordon joining the board; the article does not split the sum into "
                  "rounds, so the round of the 2012 entry is not named and the stage stays undetermined (no R7 case)."))

jl.write("sta3", L)
