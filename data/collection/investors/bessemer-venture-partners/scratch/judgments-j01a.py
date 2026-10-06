"""Judge j01, part a (PRO-80 Bessemer Venture Partners, batches 1 and 2): rows 2u .. altair-semiconductor.

Every row is on the firm's own listing (membership seeded), so each gets one classification line. Evidence read on
2026-10-01: the firm's posts and memos (POST), the archived listing (ARCH), Google News under NQ_TAG=j01
(scratchpad/j01/q*.out, news-extra-j01.json), publisher pages through WebFetch, sibling books' citations
(scratchpad/j01/sib.py). Run as NQ_TAG=j01 python3 judgments-j01a.py.
"""
import judge_lib as jl
from judge_lib import ARCH, POST, SITE, W, cls, rnd

WV = "web_verified"
FP = "first_party"
BVP = "Bessemer Venture Partners"

# URLs printed by the tools run for this pass (news decode, sibling rows, WebFetch reads)
TC_42F = "https://techcrunch.com/2012/11/16/42floors-raises-5m-from-dave-mcclure-alexis-ohanian-others-expands-office-search-site-to-new-york/"
CBN_ABRIDGE = "https://news.crunchbase.com/startups/abridge-debuts-with-15m-round-to-provide-medical-plans-of-action/"
FINSMES_ACT = "https://www.finsmes.com/2026/07/act-security-raises-60m-in-total-funding.html"
BK_ADA = "https://betakit.com/ada-closes-19-million-series-a-to-tackle-travel-and-financial-customer-support/"
TELE_ADAP = "https://www.telecompaper.com/news/adap-tv-secures-usd-10-million-in-series-a-funding--563499"
SA_AIMON = "https://siliconangle.com/2024/12/11/aimon-raises-2-3m-combat-ai-hallucinations-llm-judges/"
TC_AIWYN = "https://techcrunch.com/2024/12/19/a-bad-experience-with-an-accounting-firm-spurred-this-founder-to-start-aiwyn/"
GLOBE_ALCRESTA = "https://www.bostonglobe.com/business/2013/07/21/newton-company-raises-million-for-supplement-that-packs-calories/vrCi74PJuFtcstZrG1BELK/story.html"
FINSMES_ALGOX2 = "https://www.finsmes.com/2026/10/algox2-raises-10m-in-seed-extension-funding.html"
TC_ALLOY = "https://techcrunch.com/2022/09/01/fintech-alloy-fight-fraud/"
SA_ALTAIR = "https://siliconangle.com/2026/04/27/altair-semiconductor-raises-50m-completing-spinoff-sony/"
BW_ACTIV = "https://www.businesswire.com/news/home/20211018005547/en/Options-Technology-Announces-Acquisition-of-ACTIV-Financial"
ACV_ATLAS = POST("acv-from-used-car-dealerships")
DEEP_HEALTH = POST("our-deep-health-seed-program")
P_30S = POST("30-sundays-ai-powered")
P_MICRO = POST("microacquire-helps-startups")
P_ACT = POST("act-proactive-cloud-security")
P_AIVAR = POST("realizing-ai-for-global-enterprises-with-aivar")
P_ALGOX2 = POST("revolutionizing-data-streaming")
P_ALLOY = POST("bessemer-series-a-investment-alloy")

L = []

# ---- 2u
L.append(cls("2u", rng="below_1b", city="Arlington", focus="SaaS", entry_date="2011-03-04",
             note="2U (fka 2tor), online degree programmes run for universities. Listed in March 2014, went through Chapter 11 in 2024 and left the market under its lenders, so the row carries no figure. The firm's own investment date is 2011-03-04 (the $32.5M round of early 2011, a later round by the Form D sequence), a year before the Form D seat the entry was dated from; the Growth label stands. Head office moved from Lanham to Arlington, Virginia."))

# ---- 30-sundays
L.append(cls("30-sundays", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=P_30S,
             stage_conf="high", entry_date="2026-07", country="IN", country_src=WV, country_cite=SITE("30-sundays"),
             city="Gurugram", focus="Consumer & Marketplaces",
             rounds=[rnd("2026-07-20", "Series A", 6700000, BVP, True, P_30S, "firm")],
             note="30 Sundays, AI-planned holidays for Indian couples (the firm's India desk; Gurugram from model knowledge). The firm's own post: 'Bessemer Venture Partners leads 30 Sundays' $6.7M Series A' (2026-07-20), and it names no earlier Bessemer round. A $6.7M Series A carries no $1B mark."))

# ---- 42floors
L.append(cls("42floors", status="acquired", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=TC_42F,
             stage_conf="high", entry_date="2012-05-11", city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2012", "Seed", 400000, None, False, TC_42F, "press"),
                     rnd("2012-05", "Series A", 5000000, None, True, TC_42F, "press"),
                     rnd("2013-01-31", "Series B", 12300000, "New Enterprise Associates", None,
                         "https://techcrunch.com/2013/01/31/yc-alum-42floors-raises-12-3m-led-by-nea-to-take-its-office-rental-search-engine-us-wide-and-beyond", "press")],
             note="42Floors, commercial office search; acq. by Knotel, 2018 (the firm's own exit line). TechCrunch (2012-11-16): the company 'raised a $5 million series A round earlier this year' with Bessemer among the investors and Jeremy Levine joining the board; the firm's own investment date is 2012-05-11. The Form D seat of January 2013 is the NEA-led Series B, a follow-on, so the label stays Series A and the date moves to the firm's own."))

# ---- abridge
L.append(cls("abridge", city="Pittsburgh", stage="undetermined", focus="Healthcare & Bio",
             rounds=[rnd("2020-10-06", "Seed ($5M) and Series A ($10M), announced together", 15000000,
                         "Union Square Ventures; UPMC", True, CBN_ABRIDGE, "press"),
                     rnd("2023-10-26", "Series B", 30000000, "Spark Capital", None, None, "press")],
             note="Abridge, clinical documentation AI, Pittsburgh (as the sibling books read). Crunchbase News (2020-10-06) names Bessemer among the investors in a $15M financing that combined a $5M seed and a $10M Series A led by Union Square Ventures and UPMC, without saying which of the two Bessemer bought; the firm's own list dates the partnership to 2021 (its archived 2011 predates the company). The round the firm entered cannot be named from the sources read, so undetermined. The sibling books disagree on the mark ($2.75B and $5.3B); this row's mark was not in the queue."))

# ---- acceleron
L.append(cls("acceleron", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2007", country="US", city="Cambridge", focus="Healthcare & Bio",
             rounds=[rnd("2003-12", "Series A", 25000000, None, False, W("Acceleron Pharma"), "press"),
                     rnd("2007", "Series C", None, BVP, True, None, "press")],
             note="Acceleron Pharma, protein therapeutics; IPO September 2013, acq. by Merck, 2021 (the firm's own listing), so acquired and no figure. Wikipedia dates the $25M Series A to 2003; the firm partnered in 2007 (its own year), at the Series C it led that year (named from knowledge, no page in hand), a round after the Series A and so Growth."))

# ---- accuvein
L.append(cls("accuvein", status="private", rng="below_1b", city="Medford", focus="Healthcare & Bio",
             note="AccuVein, handheld vein illumination devices, Medford, New York; still operating and filing Form D rounds through 2023 ($5.4M), none near a $1B mark. No sale or listing found (Google News, 2026-10-01)."))

# ---- acquire-com-fka-microacquire
L.append(cls("acquire-com-fka-microacquire", status="private", rng="below_1b", stage="Seed", stage_src=FP,
             stage_cite=P_MICRO, stage_conf="high", entry_date="2021-07", country="US", city="San Francisco",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-07-06", "Seed", 2800000, BVP, True, P_MICRO, "firm")],
             note="Acquire.com (fka MicroAcquire), a marketplace for buying and selling startups. The firm's own post (2021-07-06): 'Bessemer leads the $2.8 million seed round of MicroAcquire'. No later priced round found in Google News on 2026-10-01. Graduation left for the graduation pass."))

# ---- act-security
L.append(cls("act-security", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=P_ACT,
             stage_conf="high", entry_date="2025", grad="graduated", grad_src=FP, grad_cite=P_ACT, grad_conf="high",
             country="IL", country_src=WV, country_cite=FINSMES_ACT, city="Tel Aviv", focus="Security",
             rounds=[rnd("2025", "Seed", 20000000, "Team8; Bessemer Venture Partners", True, P_ACT, "firm"),
                     rnd("2026-07-28", "Series A", 40000000, "Notable Capital", True, FINSMES_ACT, "press")],
             note="Act Security, cloud access guardrails, Tel Aviv (FinSMEs). The firm's own post (2026-07-28): 'we've backed Act at its $20 million seed round and now in its Series A'; the seed is dated by the firm's partnered year, 2025. Graduated on the $40M Series A led by Notable Capital, announced with the seed at $60M in total; no valuation published, so below $1B."))

# ---- activ-financial-systems
L.append(cls("activ-financial-systems", status="acquired", rng="below_1b", stage="undetermined", entry_date="2009",
             country="US", city="Wheaton", focus="Fintech & Payments", rounds=[],
             note="ACTIV Financial Systems, market data feeds for electronic trading, Wheaton, Illinois; acq. by Options Technology, 2021 (the firm's own listing; Business Wire, 2021-10-18). The firm partnered in 2009, seven years after the company was founded; no source read names the round (Google News for the company beside Bessemer, 2026-10-01, found none), so undetermined."))

# ---- acv-auctions
L.append(cls("acv-auctions", city="Buffalo", stage="Series A", stage_src=FP, stage_cite=ACV_ATLAS, stage_conf="high",
             entry_date="2016-08-12", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2016-08", "Series A", 5000000, None, True, ACV_ATLAS, "firm"),
                     rnd("2017-03", "Series B", 15000000, BVP, True, ACV_ATLAS, "firm"),
                     rnd("2018-01", "Series C", 31000000, BVP, True, ACV_ATLAS, "firm")],
             note="ACV Auctions, wholesale used-car auctions, Buffalo. The firm's own account (2021-03-24): 'the traction was enough for us to invest $100,000 as part of the company's Series A', and 'We led ACV's Series B and C'; its investment date is 2016-08-12, the month of the $5M Form D. The Form D band read Growth off the 2018 seat, which is the Series C follow-on, so the entry is re-staged to Series A."))

# ---- ada
L.append(cls("ada", country="CA", country_src=WV, country_cite=BK_ADA, city="Toronto", stage="Seed", stage_src=WV,
             stage_cite=BK_ADA, stage_conf="high", entry_date="2016-11-28", grad="graduated", grad_src=WV,
             grad_cite=BK_ADA, grad_conf="high", focus="AI & Applied AI",
             rounds=[rnd("2016-11", "Seed", 2500000, None, True, BK_ADA, "press"),
                     rnd("2018-12-18", "Series A", 19000000, "FirstMark Capital", True, BK_ADA, "press")],
             note="Ada (Ada Support), customer service automation, Toronto: the Wikidata country is confirmed by BetaKit ('Toronto-based'). BetaKit (2018-12-18): Bessemer Venture Partners, Version One and Barney Pell 'all returned to follow-on from Ada's $2.5 million seed round'; the firm's own investment date is 2016-11-28. Graduated on the $19M Series A led by FirstMark in December 2018."))

# ---- adap-tv
L.append(cls("adap-tv", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2011-03-15", city="San Mateo", focus="Media, Gaming & Advertising",
             rounds=[rnd("2007-08", "Series A", 10000000, "Gemini Israel Funds; Redpoint Ventures", False, TELE_ADAP, "press"),
                     rnd("2011-03-14", "later round (unnamed in the filing)", 20000000, BVP, True,
                         jl.FORMD_CITE("adap-tv", 1), "filing")],
             note="Adap.tv, video advertising exchange, San Mateo; acq. by AOL, 2013 ($405M). The company closed its $10M Series A in August 2007 (Telecompaper, as the Redpoint book cites) and a Series B in 2008; Bessemer led the $20M round of March 2011 (the firm's date 2011-03-15; Form D of 2011-03-14 with Byron Deeter as director), a round after the A and B and so Growth. The series letter of the 2011 round is from knowledge."))

# ---- adaptive-insights
L.append(cls("adaptive-insights", status="acquired", rng="below_1b", city="Palo Alto", focus="SaaS",
             entry_date="2013-05-15",
             note="Adaptive Insights (fka Adaptive Planning), cloud corporate performance management, Palo Alto; acq. by Workday, 2018. The firm's own date is 2013-05-15 and its post says 'when we invested in Adaptive Insights in 2013'; Byron Deeter joined the board in May 2013 (the S-1 draft), at the $45M round, so the entry date moves from the 2015 Form D seat to 2013 and the Growth label stands."))

# ---- affirmed-networks
L.append(cls("affirmed-networks", status="acquired", rng="below_1b", city="Acton", focus="Data Infrastructure",
             note="Affirmed Networks, virtualised mobile core software, Acton, Massachusetts (as the Lightspeed book reads); acq. by Microsoft, 2020."))

# ---- aimon
L.append(cls("aimon", status="private", rng="below_1b", stage="Pre-Seed", stage_src=WV, stage_cite=SA_AIMON,
             stage_conf="high", entry_date="2024-12", country="US", focus="AI & Applied AI", flags=["city_unknown"],
             rounds=[rnd("2024-12-11", "Pre-Seed", 2300000, "Bessemer Venture Partners; Tidal Ventures", True, SA_AIMON, "press")],
             note="AIMon (Aimon Labs), hallucination detection for generative AI applications. SiliconANGLE (2024-12-11): a $2.3 million preseed round co-led by Bessemer Venture Partners and Tidal Ventures. Neither the company's site nor the coverage states a head office, so the city is left open. Momentum check 2026-10-01 (Google News): no later round found, no $1B mark."))

# ---- aivar
L.append(cls("aivar", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=P_AIVAR,
             stage_conf="high", entry_date="2025", grad="censored", country="IN", country_src=WV,
             country_cite=SITE("aivar"), focus="AI & Applied AI", flags=["city_unknown"],
             rounds=[rnd("2026-01-08", "Seed", 4600000, "Sorin Investments", True, P_AIVAR, "firm")],
             note="Aivar (Aivar Innovations), AI services for large enterprises, on the firm's India desk. The firm's own post (2026-01-08): 'Bessemer Venture Partners invests in Aivar's $4.6M seed round' (Sorin Investments led, Entrackr); the live list dates the partnership to 2025, the archived 2021 predates the company (founded 2024). An entry after 2024-10-01, so censored. No source read states the city. Momentum check 2026-10-01: the seed is the only round."))

# ---- aiwyn
L.append(cls("aiwyn", status="private", rng="below_1b", stage="undetermined", entry_date="2024-12", country="US",
             city="Charlotte", focus="SaaS",
             rounds=[rnd("2021-06", "Seed", 14000000, "Revolution Ventures", False, None, "vendor"),
                     rnd("2024-12-19", "unnamed round", 113000000, "KKR; Bessemer Venture Partners", True, TC_AIWYN, "press")],
             note="Aiwyn, billing and practice software for accounting firms, Charlotte (TechCrunch). Bessemer co-led the $113M round of December 2024 with KKR's Next Generation Technology fund (TechCrunch, SiliconANGLE); the total raised is $127M, so about $14M came before it. No source read gives the round a series name, and it follows what vendor pages call a seed, so the stage is undetermined; a later pass could settle it from the company's release. Momentum check 2026-10-01: no valuation published, no later round."))

# ---- alcresta-therapeutics
L.append(cls("alcresta-therapeutics", status="acquired", rng="below_1b", city="Waltham", stage="Series A", stage_src=FP,
             stage_cite=DEEP_HEALTH, stage_conf="high", entry_date="2011", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2011", "Series A", None, BVP, True, DEEP_HEALTH, "firm"),
                     rnd("2013-07-22", "Series B", 10000000, "Third Rock Ventures; Frazier Healthcare; Bessemer Venture Partners", True, GLOBE_ALCRESTA, "press")],
             note="Alcresta Therapeutics, enzyme-based products for digestive disorders (Newton at the 2013 round, now Waltham, Massachusetts); acq. by Linden Capital Partners, 2024 (the firm's own listing). The firm's own post (2018-06-01): 'We led the Series A of Allena Pharmaceuticals, Alcresta Therapeutics ...', and its year is 2011; the Boston Globe (2013-07-22) reports the $10M Series B with Bessemer among the lead investors. The Form D band read Growth off the 2017 seat, a follow-on, so the entry is re-staged to Series A."))

# ---- algox2
L.append(cls("algox2", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=P_ALGOX2,
             stage_conf="high", entry_date="2025-10", grad="censored", country="US", city="New York",
             city_src=WV, focus="Data Infrastructure",
             rounds=[rnd("2025-10-08", "Seed", 3500000, BVP, True, P_ALGOX2, "firm"),
                     rnd("2026-09-30", "Seed extension", 10000000, "Bessemer Venture Partners; Fin Capital", True, FINSMES_ALGOX2, "press")],
             note="AlgoX2, a low-latency data streaming platform, New York (FinSMEs: 'a NYC-based provider'). The firm's own post (2025-10-08): 'Bessemer Venture Partners leads seed investment in AlgoX2'. An entry after 2024-10-01, so censored. Momentum check 2026-10-01: the newest round is the $10M seed extension of 2026-09-30, no valuation published."))

# ---- allena-pharmaceuticals
L.append(cls("allena-pharmaceuticals", rng="below_1b", city="Newton", stage="Series A", stage_src=FP,
             stage_cite=DEEP_HEALTH, stage_conf="high", entry_date="2011-09-09", focus="Healthcare & Bio",
             rounds=[rnd("2011-09", "Series A", None, BVP, True, DEEP_HEALTH, "firm"),
                     rnd("2014-10-29", "later round", 27000000, None, True, jl.FORMD_CITE("allena-pharmaceuticals", 1), "filing")],
             note="Allena Pharmaceuticals, oral enzyme therapeutics, Newton, Massachusetts; IPO November 2017, Chapter 11 and asset sale in 2022, so no figure. The firm's own post (2018-06-01): 'We led the Series A of Allena Pharmaceuticals', and its investment date is 2011-09-09, which agrees with the withheld Form D band; the 2014 Form D seat is a follow-on. Not a Seed entry, so no graduation."))

# ---- alloy
L.append(cls("alloy", status="private", rng="1b_plus", usd=1550000000, val_src=WV, val_cite=TC_ALLOY, asof="2022-09",
             extra={"valuation_range_source": WV}, city="New York", stage="Series A", stage_src=FP, stage_cite=P_ALLOY,
             stage_conf="high", entry_date="2019-09", focus="Fintech & Payments", flags=["stale", "stage_disputes_band"],
             rounds=[rnd("2019-09-17", "Series A", 12000000, BVP, True, P_ALLOY, "firm"),
                     rnd("2022-09-01", "Series C extension", 52000000, "Lightspeed; Avenir", None, TC_ALLOY, "press")],
             note="Alloy (alloy.com), identity and fraud decisioning for banks and fintechs, New York. The firm's own post (2019-09-17): 'Bessemer is leading this company's $12 million Series A financing'. The Form D rounds and seat on the row (2010, $33M and $53M, a director named Nitin Gupta) belong to another issuer of the same name, a homonym on a common roster name, so the Growth band and the 2010 date are disputed. Mark: 'an additional $52 million at a $1.55 billion valuation' (TechCrunch, 2022-09-01), as the Felicis and Lightspeed books carry it; no later priced round found on 2026-10-01, so stale. The 20VC, 8VC, Bain Capital Ventures, Menlo and Y Combinator rows named Alloy are other companies."))

# ---- allscripts
L.append(cls("allscripts", city="Chicago", stage="undetermined", entry_date="1987", focus="Healthcare & Bio", rounds=[],
             note="Allscripts (now Veradigm), healthcare IT, Chicago; IPO July 1999. The firm's list gives the partnered year 1987 and no sentence about the round; no source read names it (Google News for the company beside Bessemer found only a fund item), so undetermined."))

# ---- altair-semiconductor
L.append(cls("altair-semiconductor", status="private", rng="below_1b", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2007-05-29", city="Hod Hasharon", focus="Industrial & Robotics",
             rounds=[rnd("2007-05", "Series B", 18000000, BVP, True, None, "press"),
                     rnd("2026-04-27", "round at the spin-out from Sony", 50000000, "Pitango", False, SA_ALTAIR, "press")],
             note="Altair Semiconductor, LTE chipsets, Hod Hasharon. Bessemer led the $18M Series B of mid 2007 (named from knowledge; the firm's own date is 2007-05-29, two years after the 2005 founding round), so Growth. The firm exited when Sony bought the company in January 2016; in April 2026 the company completed a spin-out from Sony as an independent company again with $50M from Pitango (SiliconANGLE, 2026-04-27; Reuters put its value near $300M), so the current state reads private and below $1B. If the 2016 sale should hold the status, this is the line to reverse."))

jl.write("j01a", L)
