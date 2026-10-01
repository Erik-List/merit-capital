#!/usr/bin/env python3
"""Stage and R7 pass, tag sta, rows 22-43 of queue/st.json (PRO-99). Run: NQ_TAG=sta python3 judgments-sta2.py

Stage keys, rounds and flags only (valuation and status belong to the A/B agents). A not_member row gets its verdict
line and nothing else.
"""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, NEWS, POST, W, FTS

L = []

# URLs read with WebFetch or through secget in this pass (each says what is cited).
ALIGN_424B4 = "https://www.sec.gov/Archives/edgar/data/1097149/000089843001000296/0000898430-01-000296.txt"
TC_CP_B = ("https://techcrunch.com/2013/08/13/cloudphysics-raises-10m-from-kleiner-perkins-for-simulating-what-the-"
           "cloud-might-do-in-that-old-fashioned-data-center/")
TC_CP_C = ("https://techcrunch.com/2014/06/23/cloudphysics-grabs-15m-in-series-c-funding-and-announces-new-virtual-"
           "storage-predictive-analytics/")
PRN_COVER = ("https://www.prnewswire.com/news-releases/coverwallet-raises-78-million-and-adds-jim-ermilio-as-president-"
             "of-insurance-300364533.html")
TC_DRAW_A = "https://techcrunch.com/2012/05/10/drawbridge-kleiner-perkins-sequoia/"
TC_DRAW_B = "https://techcrunch.com/2013/02/22/drawbridge-series-b/"
TC_DRAW_C = "https://techcrunch.com/2016/05/05/drawbridge-series-c/"
TC_DROPCAM = ("https://techcrunch.com/2013/07/31/remote-video-startup-dropcam-raises-30m-plans-to-use-the-funding-to-"
              "better-compete-with-itself/")
EXTR_S1A = "https://www.sec.gov/Archives/edgar/data/1078271/000101287099000736/0001012870-99-000736.txt"
TC_FLIP = "https://techcrunch.com/2015/07/15/flip-it-good/"

# correction to sta1: the prospectus dates only the Series C and D closings; the Series B year was not read.
L.append(cls("align-technology",
             rounds=[jl.rnd("1997", "Series A", None, None, True, ALIGN_424B4, "filing"),
                     jl.rnd(None, "Series B", None, None, True, ALIGN_424B4, "filing"),
                     jl.rnd("1999-09-24", "Series C", 20744912, None, True, ALIGN_424B4, "filing"),
                     jl.rnd("2000-05-25", "Series D", None, None, True, ALIGN_424B4, "filing")]))

# 22 cloudphysics: not in the 2012 Series A, led the Series B of August 2013.
CP_A = NEWS("cloudphysics", "Raises $2.5 Million")
L.append(cls("cloudphysics", stage="Growth", stage_src="web_verified", stage_cite=TC_CP_B, stage_conf="medium",
             entry_date="2013-08-13",
             rounds=[rnd("2012-08-23", "Series A", 2500000, "Mayfield Fund", False, CP_A, "press"),
                     rnd("2013-08-13", "Series B", 10000000, "Kleiner Perkins Caufield & Byers", True, TC_CP_B, "press"),
                     rnd("2014-06-23", "Series C", 15000000, None, None, TC_CP_C, "press")],
             note="Stage pass: TechCrunch (2013-08-13): a $10M Series B led by Kleiner Perkins with Mayfield and the "
                  "VMware founders, a year after the $2.5M first round TechCrunch (2012-08-23) reports from Mayfield "
                  "and angels without Kleiner Perkins. The entry is the Series B, Growth, at medium because the firm's "
                  "page gives 2012 (Mike Abbott's deal, no R7 case)."))

# 23 cognition (stage only)
L.append(cls("cognition", flags=["cite_pending"],
             note="Stage pass: no source read names Kleiner Perkins in a Cognition round; undetermined, cite pending."))

# 24 collective-medical: the round Kleiner Perkins led is named Series A.
CM = NEWS("collective-medical", "Raises $47.5M")
L.append(cls("collective-medical", stage="Series A", stage_src="web_verified", stage_cite=CM, stage_conf="high",
             entry_date="2017-11-14",
             rounds=[rnd("2017-11-14", "Series A", 47500000, "Kleiner Perkins", True, CM, "press")],
             note="Stage pass: HIT Consultant (2017-11-14): $47.5M in Series A funding led by Kleiner Perkins with "
                  "Bessemer, Maverick, Kaiser Permanente Ventures and others, the firm's 2017 entry. The record names "
                  "the round Series A, so it reads Series A although the firm's own label is Growth (no R7 case)."))

# 25 coverwallet: R7, Ilya Fushman at Index Ventures.
L.append(verdict("coverwallet", "not_member",
                 "partner-carried (R7): Ilya Fushman backed it at Index Ventures in 2016; no round names a Kleiner "
                 "Perkins fund. Index joined the $7.8M Series A of November 2016 that Union Square Ventures led (the "
                 "company's release); the firm's own page for Fushman lists CoverWallet among his companies and he "
                 "joined Kleiner Perkins from Index in 2018, after the site's 2017 year; the backers listed at the "
                 "Aon sale (AlleyWatch 2019-11-20: Index, Foundation, Highland, Founder Collective, Union Square, Two "
                 "Sigma, Zurich, Starr) do not include Kleiner Perkins; the page first appears on the firm's list in "
                 "2020 (Erik 2026-09-17 partner-carried rule; decisions.md R7).",
                 ec="web", conf="medium", cite=PRN_COVER))

# 26 cultureamp (stage only; a membership question for the A/B agent)
L.append(cls("cultureamp", flags=["cite_pending"],
             note="Stage pass: no round naming Kleiner Perkins was found. The firm's page for Ilya Fushman lists "
                  "CultureAmp among his companies; he was the Index Ventures director on the May 2017 Form D and "
                  "joined Kleiner Perkins in 2018, after the site's 2016 year, and the row is on the live list only: "
                  "the R7 signature, for the membership check."))

# 27 databricks (stage only)
L.append(cls("databricks", flags=["cite_pending"],
             note="Stage pass: no source read names Kleiner Perkins in a Databricks round; the Growth reading rests on "
                  "the firm's 2024 year, cite pending."))

# 28 datastax: Kleiner Perkins led the $106M Series E of September 2014.
DS = NEWS("datastax", "Premji Invest")
L.append(cls("datastax", stage="Growth", stage_src="web_verified", stage_cite=DS, stage_conf="medium",
             entry_date="2014-09",
             rounds=[rnd("2014-09", "Series E", 106000000, "Kleiner Perkins Caufield & Byers", True, DS, "press"),
                     rnd("2022-06-15", "Unnamed round", 115000000, None, None, W("DataStax"), "press"),
                     rnd("2025-05-28", "Acquisition by IBM", None, None, None, W("DataStax"), "press")],
             note="Stage pass: The Economic Times (2014-09-06) headlines Premji Invest joining the '$106 million "
                  "pre-IPO funding led by KPCB', the round Wikipedia names the Series E of September 2014 and the "
                  "firm's 2014 entry: Growth, at medium because only the headline could be read (no R7 case)."))

# 29 diy
L.append(cls("diy",
             note="Stage pass: Google News, Wikipedia (DIY.org) and a web search name no round with Kleiner Perkins; "
                  "the 2011 entry with Bing Gordon rests on the firm's listing (archived from 2013, no R7 case) and "
                  "the stage stays undetermined."))

# 30 dji (stage only)
L.append(cls("dji", flags=["cite_pending"],
             note="Stage pass: the 2015 coverage read (The Verge, the Wall Street Journal) names Accel, not Kleiner "
                  "Perkins; the Growth reading rests on the firm's 2015 year, cite pending."))

# 31 docusign: named in the July 2012 round, the company's fifth financing or later.
DOCU = W("Docusign")
L.append(cls("docusign", stage="Growth", stage_src="web_verified", stage_cite=DOCU, stage_conf="medium",
             entry_date="2012-07",
             rounds=[rnd("2004", "round of $4.6M (Ignition, Frazier)", 4600000, None, False, DOCU, "press"),
                     rnd("2010-12", "round of $27M", 27000000, "Scale Venture Partners", False, DOCU, "press"),
                     rnd("2012-07", "round of $47.5M, later about $56M (series not named)", 47500000, None, True, DOCU,
                         "press"),
                     rnd("2014-03", "round of $85M", 85000000, None, None, DOCU, "press"),
                     rnd("2015-05", "round of $233M", 233000000, None, None, DOCU, "press")],
             note="Stage pass: Wikipedia: 'In July 2012, Docusign raised $47.5 million in venture funding from "
                  "investors including Kleiner Perkins Caufield & Byers', after the 2004, 2006-09 and December 2010 "
                  "financings, with Mary Meeker on the board from July 2012 (the 2018 draft prospectus): a late round, "
                  "Growth, at medium because the series is not named."))

# 32 drawbridge: seed from Kleiner Perkins and Sequoia, then the Series A.
L.append(cls("drawbridge", stage="Seed", stage_src="web_verified", stage_cite=TC_DRAW_A, stage_conf="medium",
             entry_date="2010",
             grad="graduated", grad_src="web_verified", grad_cite=TC_DRAW_A, grad_conf="high", grad_asof="2012-05-10",
             rounds=[rnd("2010", "Seed", None, "Kleiner Perkins; Sequoia Capital", True, TC_DRAW_A, "press"),
                     rnd("2012-05-10", "Series A", 6500000, "Kleiner Perkins Caufield & Byers; Sequoia Capital", True,
                         TC_DRAW_A, "press"),
                     rnd("2013-02-22", "Series B", 14000000, None, None, TC_DRAW_B, "press"),
                     rnd("2016-05-05", "Series C", 25000000, "Sequoia Capital", None, TC_DRAW_C, "press"),
                     rnd("2019", "Acquisition by LinkedIn", None, None, None, W("Drawbridge (company)"), "press")],
             note="Stage pass: TechCrunch (2012-05-10): a $6.5M Series A from Kleiner Perkins and Sequoia, and "
                  "'Drawbridge previously raised a seed round of undisclosed size from Kleiner and Sequoia', the "
                  "firm's 2010 entry (Matt Murphy's deal, no R7 case): Seed, graduated by that Series A. The seed's "
                  "date is the firm's own year."))

# 33 dropcam: a new investor in the Series C.
L.append(cls("dropcam", stage="Growth", stage_src="web_verified", stage_cite=TC_DROPCAM, stage_conf="high",
             entry_date="2013-07-31",
             rounds=[rnd("2012-06", "Series B", 12000000, "Menlo Ventures", False, None, "press"),
                     rnd("2013-07-31", "Series C", 30000000, "Institutional Venture Partners", True, TC_DROPCAM,
                         "press"),
                     rnd("2014-06", "Acquisition by Google (Nest)", 555000000, None, None, W("Dropcam"), "press")],
             note="Stage pass: TechCrunch (2013-07-31): a $30M Series C led by IVP 'with participation by new investor "
                  "Kleiner Perkins Caufield & Byers and existing backers Accel Partners and Menlo Ventures', the "
                  "firm's 2013 Digital Growth Fund entry: Growth (no R7 case)."))

# 34 engine-ml
L.append(cls("engine-ml", stage="undetermined", entry_date="2018", rounds=[],
             note="Stage pass: Google News and the firm's posts return nothing on an Engine ML round; the 2018 entry "
                  "rests on the firm's listing (archived from 2019) and the stage stays undetermined."))

# 35 enphase-energy: the Green Growth Fund bought Series E preferred on 2010-05-21.
ENPH = FTS("Enphase", "424B4")
L.append(cls("enphase-energy", stage="Growth", stage_src="web_verified", stage_cite=ENPH, stage_conf="high",
             entry_date="2010-05-21",
             rounds=[rnd("2009-04-24", "Series D", 24200000, None, False, ENPH, "filing"),
                     rnd("2010-05-21", "Series E", 45700000, None, True, ENPH, "filing")],
             note="Stage pass: the March 2012 prospectus's preferred-stock financings table shows KPCB Holdings buying "
                  "no Series D (2009) and 2,024,488 Series E shares for $12.5M on 2010-05-21, held by the KPCB Green "
                  "Growth Fund: the entry is the Series E, Growth."))

# 36 extreme-networks: no Series A shares, 2,355,073 Series B shares in mid 1997.
L.append(cls("extreme-networks", stage="Growth", stage_src="web_verified", stage_cite=EXTR_S1A, stage_conf="high",
             entry_date="1997-05",
             rounds=[rnd("1996-05-28", "Series A", 4855140, None, False, EXTR_S1A, "filing"),
                     rnd("1997-05-07", "Series B", 12262995, None, True, EXTR_S1A, "filing"),
                     rnd("1998-01-12", "Series C", 20533973, None, True, EXTR_S1A, "filing")],
             note="Stage pass: the 1999 S-1's certain-transactions table shows the entities affiliated with Kleiner "
                  "Perkins buying no Series A (May 1996), 2,355,073 Series B (May and June 1997 at $1.38) and 136,238 "
                  "Series C shares: the 1997 entry is the Series B, which reads Growth by the taxonomy."))

# 37 facebook: the February 2011 purchase.
FB = NEWS("facebook", "Buys $38 Million")
L.append(cls("facebook", stage="Growth", stage_src="web_verified", stage_cite=FB, stage_conf="medium",
             entry_date="2011-02",
             rounds=[rnd("2011-02", "purchase of about $38M of shares (a 0.07% stake)", 38000000, None, True, FB,
                         "press")],
             note="Stage pass: Business Insider (2011-02-14) headlines 'Kleiner Perkins Buys $38 Million, 0.07% Stake "
                  "In Facebook', the Digital Growth Fund's 2011 entry at a valuation above $50B: Growth, at medium "
                  "because only the headline could be read."))

# 38 farmers-edge: the November 2014 Series B, out of the Green Growth Fund.
FE = NEWS("farmers-edge", "Raises $41m")
FE_X = NEWS("farmers-edge", "Kleiner Perkins Exits")
L.append(cls("farmers-edge", stage="Growth", stage_src="web_verified", stage_cite=FE, stage_conf="high",
             entry_date="2014-11",
             rounds=[rnd("2014-11", "Series B", None, "Kleiner Perkins Caufield & Byers", True, FE, "press"),
                     rnd("2015-06", "investment by Mitsui", None, "Mitsui & Co", None, FE, "press"),
                     rnd("2016-01-27", "equity round of C$58M ($41M) from existing investors", 41000000, None, True,
                         FE, "press"),
                     rnd("2016-12-20", "Fairfax buys a stake; Kleiner Perkins exits", None, None, False, FE_X, "press")],
             note="Stage pass: AgFunderNews (2016-01-27) dates 'November 2014's Series B round with Kleiner Perkins', "
                  "and its exit report (2016-12-20) says the firm 'first invested in the company in November 2014 out "
                  "of its Green Growth Fund': Growth (no R7 case)."))

# 39 flextronics-international
L.append(cls("flextronics-international", flags=["cite_pending"],
             note="Stage pass: no Kleiner Perkins round in Flextronics is on record (listed since 1994; on the firm's "
                  "2012 company pages only); undetermined, cite pending."))

# 40 flipagram: named in the $70M B round.
L.append(cls("flipagram", stage="Growth", stage_src="web_verified", stage_cite=TC_FLIP, stage_conf="medium",
             entry_date="2015-07",
             rounds=[rnd("2015-07-15", "Series B", 70000000, "Sequoia Capital", True, TC_FLIP, "press"),
                     rnd("2017", "Acquisition by ByteDance (Toutiao)", None, None, None, None, "press")],
             note="Stage pass: TechCrunch (2015-07-15): 'a $70 million B round of funding led by Sequoia and including "
                  "Kleiner Perkins and Index Ventures', with John Doerr and Michael Moritz joining the board; no source "
                  "read names Kleiner Perkins in an earlier round, so the entry reads Growth at medium (other outlets "
                  "call the same $70M a Series A, and the site's 2010 year predates the company). No R7 case."))

# 41 flock-safety (stage only)
L.append(cls("flock-safety", flags=["cite_pending"],
             note="Stage pass: no source read names Kleiner Perkins in a Flock Safety round; the Growth reading rests "
                  "on the firm's 2023 year, cite pending."))

# 42 front (stage only; a membership question for the A/B agent)
L.append(cls("front", flags=["cite_pending"],
             note="Stage pass: no round naming Kleiner Perkins was found. The firm's page for Mamoon Hamid lists Front "
                  "among his companies; he was at Social Capital until 2017, after the site's 2016 year, and the row "
                  "is on the live list only: the R7 signature, for the membership check."))

# 43 general-radar
L.append(cls("general-radar",
             note="Stage pass: Google News gives only the $22M Series A of June 2022 (FinSMEs, not readable here); no "
                  "source names the round of the firm's 2016 entry or ties a later partner's previous firm to it, so "
                  "the listing stands and the stage stays undetermined."))

jl.write("sta2", L)
