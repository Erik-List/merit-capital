"""Judge j01, part d (PRO-80 Bessemer Venture Partners, batch 2): rows bold-metrics .. carefull-corporation.

Evidence read on 2026-10-01 as in part a. Run as NQ_TAG=j01 python3 judgments-j01d.py.
"""
import judge_lib as jl
from judge_lib import ARCH, POST, SITE, W, cls, rnd

WV = "web_verified"
FP = "first_party"
BVP = "Bessemer Venture Partners"

CT_BOLD = "https://www.calcalistech.com/ctechnews/article/skcwxqx5bl"
BW_BOLDFIT = "https://www.businessworld.in/article/kl-rahul-backed-boldfit-raises-rs-110-crore-in-series-a-funding-from-bessemer-venture-partners-538491"
BD_BOOM = "https://businessden.com/boom-supersonic-raising-300m-at-a-1-5b-valuation/"
BOOM_PR = "https://boomsupersonic.com/press-release/boom-supersonic-to-power-ai-data-centers"
SEC_BOX_S1 = "https://www.sec.gov/Archives/edgar/data/1372612/000119312514112417/d642425ds1.htm"
FORTUNE_BRAINBASE = "https://fortune.com/2020/05/20/brainbase-funding-automation-legal-work-nate-cavanaugh/"
NEWSWEEK_BRAINBASE = "https://www.newsweek.com/who-nate-cavanaugh-doge-official-now-running-us-institute-peace-2053170"
CFI_BREAD = "https://www.crowdfundinsider.com/2015/11/77352-bread-raises-14-3-million-for-pay-over-time-platform/"
PRN_BREAD_ADS = "https://www.prnewswire.com/news-releases/alliance-data-completes-acquisition-of-bread-301186414.html"
CITYBIZ_BREAKER = "https://www.citybiz.co/article/807143/defense-tech-startup-breaker-raises-6m-seed-led-by-bessemer-venture-partners/"
SA_BFAM = "https://stockanalysis.com/stocks/bfam/market-cap/"
EDSURGE_BB = "https://www.edsurge.com/news/2022-10-11-google-discreetly-acquires-edtech-analytics-company-brightbytes"
PYMNTS_BW = "https://www.pymnts.com/news/investment-tracker/2021/brightwheel-early-education-platform-raises-55m/"
TEAM_FEINSTEIN = "https://www.bvp.com/team/brian-feinstein"
TC_CAMBLY = "https://techcrunch.com/2023/01/24/hear-how-cambly-found-profits-after-failing-to-raise-a-series-a-on-techcrunch-live/"
BI_CANDID = "https://www.businessinsider.com/candid-co-teeth-straightening-orthodontics-startup-raises-15-million-2017-11"
DT_CANDID = "https://www.dentistrytoday.com/candidpro-launches-smile-concierge-for-providers/"
FORBES_CANVA = "https://www.forbes.com/sites/alexkonrad/2019/10/16/canva-3-billion-valuation-after-raise-for-enterprise-push/"
TECHEU_CAPMO = "https://tech.eu/2021/08/24/construction-management-platform-capmo-cements-30-million-round/"
ADM_CAPSULE8 = "https://appdevelopermagazine.com/cloud-security-platform-capsule8-raises-$6m/"
TC_CAPTIVATEIQ = "https://techcrunch.com/2022/01/26/captivateiq-raises-100m-at-a-1-25b-valuation/"
FORBES_CAPTIVATEIQ_A = "https://www.forbes.com/sites/kenrickcai/2020/05/26/captivateiq-series-a-funding-round-sequoia/"
TC_CAREFULL = "https://techcrunch.com/2023/10/11/carefull-lands-16-5m-to-shield-seniors-from-financial-fraud/"
CITYBIZ_CAREFULL = "https://www.citybiz.co/article/477940/carefull-n-y-fintech-to-protect-seniors-closes-on-16-5-million-series-a/"
DEEP_HEALTH = POST("our-deep-health-seed-program")
DEEP_TECH = POST("roadmap-deep-tech")
P_BRIGHTWHEEL = POST("bessemer-s-investment-in-brightwheel")
P_BRISK = POST("our-investment-in-brisk-teaching")
P_CAMBLY = POST("our-investment-in-cambly")
P_CANVA_AU = POST("cloud-100-2021-list-reveal")

L = []

# ---- bold-metrics
L.append(cls("bold-metrics", status="private", rng="below_1b", city="San Francisco", focus="AI & Applied AI",
             note="Bold Metrics, AI body-measurement prediction for apparel brands, San Francisco (the dateline of its Series A release). The $8M Series A of 2022 is the newest round found; no $1B mark (Google News, 2026-10-01)."))

# ---- bold-security
L.append(cls("bold-security", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=CT_BOLD,
             stage_conf="high", entry_date="2024", grad="graduated", grad_src=WV, grad_cite=CT_BOLD, grad_conf="high",
             country="IL", country_src=WV, country_cite=CT_BOLD, city="Tel Aviv", focus="Security",
             rounds=[rnd("2024", "Seed", 12000000, "Bessemer Venture Partners; Picture Capital", True, CT_BOLD, "press"),
                     rnd("2026-03-12", "Series A", 28000000, "Red Dot Capital Partners", True, CT_BOLD, "press")],
             note="Bold Security, AI endpoint data-loss prevention, 'headquartered in Tel Aviv' (CTech). CTech (2026-03-12): the 2024 seed of $12M 'was led by Bessemer Venture Partners and Picture Capital', and the company has now raised a $28 million Series A (Red Dot, Bessemer, Picture), $40M in total. Graduated on that Series A; no valuation published, so below $1B."))

# ---- boldfit
L.append(cls("boldfit", status="private", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=BW_BOLDFIT,
             stage_conf="high", entry_date="2024-11", country="IN", country_src=WV, country_cite=BW_BOLDFIT,
             city="Bangalore", focus="Consumer & Marketplaces",
             rounds=[rnd("2024-11-07", "Series A", 13000000, BVP, True, BW_BOLDFIT, "press")],
             note="Boldfit, fitness gear and apparel brand, Bangalore (model knowledge; the firm's India desk). BW Businessworld (2024-11-07): 'KL Rahul Backed Boldfit Raises Rs 110 Crore in Series-A Funding from Bessemer Venture Partners', its first institutional round, about $13M at a reported $74M valuation (The Arc), so below $1B."))

# ---- boom-supersonic
L.append(cls("boom-supersonic", status="private", rng="1b_plus", usd=1500000000, val_src=WV, val_cite=BD_BOOM,
             asof="2025-12", extra={"valuation_range_source": WV}, stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2021-03", country="US", city="Centennial", city_src=WV, focus="Industrial & Robotics",
             rounds=[rnd("2019-01", "Series B", 100000000, "Emerson Collective", False, None, "press"),
                     rnd("2021-03", "the firm's first investment (round not named)", None, None, True, DEEP_TECH, "firm"),
                     rnd("2025-12-09", "unnamed round at $1.5B post-money", 300000000, "Darsana Capital Partners", True, BD_BOOM, "press")],
             note="Boom Supersonic, supersonic airliner and gas turbine developer, Centennial, Colorado (BusinessDen: 'the Centennial-based company'; the 8VC row reads Denver). The firm's own roadmap: 'in March 2021, Bessemer invested in Boom Supersonic'; the company's Series B dates from January 2019, so a 2021 investment is a later round and Growth, the round itself not named. Mark: the $300M round of December 2025 'gives the Centennial-based company a $1.5 billion post-money valuation', from the chief executive's email to investors as BusinessDen reports it (2025-12-09), with the company's own release confirming the $300M. The 8VC row still reads below $1B."))

# ---- box
L.append(cls("box", city="Redwood City", stage="Growth", stage_src=WV, stage_cite=SEC_BOX_S1, stage_conf="high",
             entry_date="2011-10-05", focus="SaaS",
             rounds=[rnd("2011-10", "Series D-2", 32000000, None, True, SEC_BOX_S1, "filing"),
                     rnd("2011-10", "secondary purchase of Series A, B and C shares from DFJ and USVP", 20000000, None, True, SEC_BOX_S1, "filing")],
             note="Box, cloud content management, Redwood City (as the sibling books read). The S-1: entities affiliated with Bessemer Venture Partners bought 1,654,588 shares of Series D-2 preferred for $15.0M in the Series D-2 financing, and in October 2011 bought $20.0M of Series A, B and C shares from Draper Fisher Jurvetson and U.S. Venture Partners; the firm's own date is 2011-10-05. A Series D-2 entry with a concurrent secondary, so Growth."))

# ---- brainbase
L.append(cls("brainbase", status="acquired", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=FORTUNE_BRAINBASE,
             stage_conf="high", entry_date="2020-05", country="US", city="Los Angeles", focus="SaaS",
             rounds=[rnd("2020-05-20", "Series A", 8000000, BVP, True, FORTUNE_BRAINBASE, "press")],
             note="Brainbase, licensing and intellectual property management software, Los Angeles (Fortune). Fortune (2020-05-20): 'Brainbase announced it has raised $8 million in a Series A funding round led by Bessemer Venture Partners'. Newsweek's 2025 profile of its co-founder says 'The company was acquired in 2022' without naming the buyer (Constellation Software, from knowledge), so acquired; the firm's list still shows it as active. The Y Combinator row named Brainbase Labs is another company."))

# ---- bread-financial
L.append(cls("bread-financial", status="acquired", rng="below_1b", country="US", city="New York", stage="Series A",
             stage_src=WV, stage_cite=CFI_BREAD, stage_conf="high", entry_date="2015-11", focus="Fintech & Payments",
             flags=["model_disputes_source"],
             rounds=[rnd("2015-11", "Series A", 14300000, BVP, True, CFI_BREAD, "press"),
                     rnd("2017-08-02", "Series B (equity and debt)", 126000000, "Menlo Ventures", None, None, "press")],
             note="Bread (getbread.com), pay-over-time financing for retailers, New York; acq. by Alliance Data Systems, 2020 ($450M; the firm's own listing and the buyer's release of 2020-12-04). The pre-filled public status and $2.7B figure belong to the acquirer, which renamed itself Bread Financial in 2022; the firm's position is the startup, so acquired and no figure. Crowdfund Insider (2015-11): 'completion of a Series A funding round last week led by Bessemer Ventures Partners', $14.3M."))

# ---- breaker
L.append(cls("breaker", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=CITYBIZ_BREAKER,
             stage_conf="high", entry_date="2025", grad="censored", country="US", city="Austin", city_src=WV,
             focus="AI & Applied AI",
             rounds=[rnd("2026-02-17", "Seed", 6000000, BVP, True, CITYBIZ_BREAKER, "press")],
             note="Breaker, software that lets operators command teams of robots by voice, for defence; 'Austin-based', with offices in Sydney and Austin (citybiz). citybiz (2026-02-17): '$6 million in seed funding led by Bessemer Venture Partners'; the firm's list dates the partnership to 2025, the close ahead of the announcement. An entry after 2024-10-01, so censored. Momentum check 2026-10-01: the seed is the only round. The Y Combinator row named Breaker is another company."))

# ---- bright-health-group
L.append(cls("bright-health-group", city="Doral", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=DEEP_HEALTH,
             stage_conf="high", entry_date="2016-03-25", focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2016-03-25", "Series A", 80000000, "Bessemer Venture Partners; New Enterprise Associates", True, DEEP_HEALTH, "firm")],
             note="Bright Health Group (NeueHealth from 2024), health insurer and care provider, last head office in Doral, Florida (as the Tiger Global book reads; Minneapolis until 2023); IPO June 2021, taken private by New Enterprise Associates and a consortium, so acquired and no figure. The firm's own post (2018-06-01): 'We led the Series A of ... Bright Health', and the IPO filings name New Enterprise Associates 15 and Bessemer Venture Partners IX as the 'Initial Investors'. The Form D band read Growth from the $81.5M size of that first round, which the record calls the Series A, so the label is re-staged on the same date."))

# ---- bright-horizons-family-solutions
L.append(cls("bright-horizons-family-solutions", status="public", rng="1b_plus", usd=3200000000, val_src=WV,
             val_cite=SA_BFAM, asof="2026-10-01", extra={"valuation_range_source": WV, "focus": None},
             stage="undetermined", entry_date="1986", country="US", city="Newton",
             rounds=[rnd("1986", "first round", None, None, True, ARCH("bright-horizons-family-solutions"), "firm"),
                     rnd("1987", "second round", None, None, True, ARCH("bright-horizons-family-solutions"), "firm")],
             note="Bright Horizons Family Solutions, employer-sponsored child care, Newton, Massachusetts; outside the focus taxonomy. Listed in 1997, taken private by Bain Capital in 2008 and listed again in 2013 (NYSE: BFAM): market cap $3.2B on 2026-10-01 (stockanalysis.com). The firm's archived listing: 'Founded in 1986 ... Bessemer invested in its first two rounds'; the sentence names no round word that maps to one stage, so undetermined on the founding year."))

# ---- brightbytes
L.append(cls("brightbytes", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
             note="BrightBytes, education analytics, San Francisco (the firm's archived list places it in North America - West; the Insight book reads Atlanta, where its Authentica unit sat); acq. by Google, 2022 (EdSurge, 2022-10-11)."))

# ---- brightwheel
L.append(cls("brightwheel", status="private", rng="below_1b", city="San Francisco", stage="Growth", stage_src=FP,
             stage_cite=P_BRIGHTWHEEL, stage_conf="high", entry_date="2018-06-07", focus="SaaS",
             rounds=[rnd("2018-10-02", "Series B", 21000000, BVP, True, P_BRIGHTWHEEL, "firm"),
                     rnd("2021-02-03", "Series C at a valuation above $600M", 55000000, "Addition", None, PYMNTS_BW, "press")],
             note="Brightwheel, software for preschools and childcare providers, San Francisco. The firm's own post (2018-10-02): 'Bessemer is leading the company's $21M Series B financing'; its investment date is 2018-06-07. A Series B entry, so Growth. The newest priced round is the $55M of February 2021 at about $600M (PYMNTS, Bloomberg), so below $1B; no later round found on 2026-10-01."))

# ---- brisk-teaching
L.append(cls("brisk-teaching", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=P_BRISK,
             stage_conf="high", entry_date="2025-03", country="US", city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2024-09-18", "Seed", 5000000, None, False, None, "press"),
                     rnd("2025-03-25", "Series A", 15000000, BVP, True, P_BRISK, "firm")],
             note="Brisk Teaching, AI tools for teachers, San Francisco. The firm's own post (2025-03-25): 'Bessemer Venture Partners leads Brisk Teaching's $15 million Series A financing'; the seed of 2024 names no Bessemer. Momentum check 2026-10-01: no later round, no $1B mark."))

# ---- broadsoft
L.append(cls("broadsoft", city="Gaithersburg", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="1999-04", focus="Data Infrastructure", flags=["stage_disputes_band"],
             rounds=[rnd("1999-04", "Series A", 5000000, None, True, W("BroadSoft"), "press")],
             note="BroadSoft, call-control software for telecom carriers, Gaithersburg, Maryland; IPO June 2010, acq. by Cisco, 2018, so no figure. The S-1: Robert Goodman of Bessemer 'has served as one of our directors since April 1999', months after the 1998 founding, and Bessemer Venture Partners IV signs the investor agreements; Wikipedia: 'BroadSoft then received $5 million in Series A round funding'. The two together place the firm in the Series A of 1999 (no single page says so, hence model, medium). The Form D band read Growth off a 2011 filing of the listed company, which is not the entry."))

# ---- bumble
L.append(cls("bumble", country="US", city="Austin", stage="Growth", stage_src=FP, stage_cite=TEAM_FEINSTEIN,
             stage_conf="medium", entry_date="2020", focus="Consumer & Marketplaces",
             rounds=[rnd("2020-01", "Blackstone's majority purchase of MagicLab closes", None, "Blackstone", None, None, "press"),
                     rnd("2020", "growth investment (the firm's words)", None, None, True, TEAM_FEINSTEIN, "firm")],
             note="Bumble, dating apps, Austin (as the Accel and Headline books read). The firm's own partner page credits Brian Feinstein with 'growth investments in Ramp, Fireworks, Cognition, nCino (IPO) and Bumble (IPO)', and its list dates the partnership to 2020, between Blackstone's purchase of the majority (closed January 2020) and the IPO of February 2021: a private entry before the listing, Growth by the firm's own word. No source read shows whether the position came as a co-investment inside Blackstone's control purchase; that question is raised in the report."))

# ---- cambly
L.append(cls("cambly", status="private", rng="below_1b", stage="undetermined", entry_date="2018", country="US",
             city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd(None, "Series A", 15000000, None, None, TC_CAMBLY, "press"),
                     rnd(None, "Series B", 40000000, "Benchmark", None, TC_CAMBLY, "press")],
             note="Cambly, online English tutoring, San Francisco (as the GV and Y Combinator books read). The firm's own post (2022-06-14) calls itself among the 'early stage backers of the team' and its list dates the partnership to 2018; TechCrunch (2023-01-24) names a $15M Series A and a $40M Series B without dates or Bessemer. 'Early stage' does not map to one stage and no source ties the firm to either round, so undetermined. Profitable and private; no $1B mark."))

# ---- candid-co
L.append(cls("candid-co", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2017-11-21", country="US", city="New York", focus="Healthcare & Bio",
             rounds=[rnd("2017-11-21", "Series A", 15000000, "Greycroft", True, BI_CANDID, "press")],
             note="Candid (Candid Co.), clear aligners, New York (as the Headline book reads). Business Insider reported the $15 million raise on 2017-11-21, the firm's own investment date; the round was the Series A led by Greycroft with Bessemer taking part (named from knowledge, the page could not be opened). The company closed its consumer business in 2022 and operates as CandidPro, selling through dentists, with product news through 2025 (Dentistry Today), so private; the Headline row reads defunct."))

# ---- canva
L.append(cls("canva", country="AU", country_src=WV, country_cite=P_CANVA_AU, city="Sydney", stage="Growth",
             stage_src="model", stage_conf="medium", entry_date="2019-10", focus="SaaS",
             rounds=[rnd("2019-10-16", "unnamed round at a $3.2B valuation", 85000000, None, True, FORBES_CANVA, "press")],
             note="Canva, online design platform, Sydney: the Wikidata country is confirmed by the firm's own post ('spreads across the globe from its Australian roots') and the sibling books. Bessemer joined the $85M round of October 2019 at a $3.2B valuation (Forbes headline of 2019-10-16; its part is named from knowledge, the page could not be opened), six years and several rounds into the company's life, so Growth; the firm's partnered year is 2019."))

# ---- capmo
L.append(cls("capmo", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=TECHEU_CAPMO,
             stage_conf="high", entry_date="2021-08", country="DE", country_src=WV, country_cite=TECHEU_CAPMO,
             city="Munich", focus="SaaS",
             rounds=[rnd("2021-08-24", "Series B", 30000000, BVP, True, TECHEU_CAPMO, "press")],
             note="Capmo, construction management software, Munich (Tech.eu: 'the Munich startup'; the firm's desk tag reads US). Tech.eu (2021-08-24): 'Capmo's $30 million Series B round was led by Bessemer Venture Partners, with existing investors Capnamic Ventures and UVC Partners also following on'. A Series B entry, so Growth. Momentum check 2026-10-01: no later priced round found."))

# ---- capsule8
L.append(cls("capsule8", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="medium",
             entry_date="2016-11-03", grad="graduated", grad_src=WV, grad_cite=ADM_CAPSULE8, grad_conf="high",
             country="US", city="New York", focus="Security",
             rounds=[rnd("2016-11", "Seed", 2500000, BVP, True, None, "press"),
                     rnd("2017-09-28", "Series A", 6000000, None, True, ADM_CAPSULE8, "press")],
             note="Capsule8, attack detection for Linux production systems, New York; acq. by Sophos, 2021 (the firm's own listing). The firm's own date is 2016-11-03, the company's founding year, when Bessemer led the $2.5M seed (named from knowledge). Graduated: App Developer Magazine (2017-09-28) reports a $6 million round that 'brings total funding to more than $8.5 million', with Bessemer's Bob Goodman on the board."))

# ---- captivateiq
L.append(cls("captivateiq", status="private", rng="1b_plus", usd=1250000000, val_src=WV, val_cite=TC_CAPTIVATEIQ,
             asof="2022-01", extra={"valuation_range_source": WV}, stage="undetermined", entry_date="2018",
             country="US", city="San Francisco", focus="SaaS", flags=["stale"],
             rounds=[rnd("2020-05-26", "Series A", 13000000, None, None, FORBES_CAPTIVATEIQ_A, "press"),
                     rnd("2022-01-26", "Series C", 100000000, "ICONIQ Growth; Accel; Sequoia", None, TC_CAPTIVATEIQ, "press")],
             note="CaptivateIQ, sales commission software, San Francisco. Mark: 'CaptivateIQ raises $100M at a $1.25B valuation' (TechCrunch, 2022-01-26), as the Accel, ICONIQ, Sequoia and Y Combinator books carry it; no later priced round found on 2026-10-01, so stale. The firm lists the company from 2018, two years before the Series A of May 2020, and no source read names Bessemer in any round (Google News for the company beside Bessemer found nothing), so the stage is undetermined."))

# ---- carefull-corporation
L.append(cls("carefull-corporation", status="private", rng="below_1b", stage="undetermined", entry_date="2019",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2021-02", "seed (about $3.2M, from the stated total)", 3200000, None, None, None, "press"),
                     rnd("2023-10-11", "Series A", 16500000, "Fin Capital", True, TC_CAREFULL, "press")],
             note="Carefull, financial safety monitoring for older adults, New York (citybiz). The firm lists it from 2019, its founding year; TechCrunch and citybiz (October 2023) name Bessemer in the $16.5M Series A led by Fin Capital, which brought the total to $19.7M over three rounds, and neither says which of the two earlier rounds Bessemer joined. A pre-seed or a seed, two stages, so undetermined. Momentum check 2026-10-01: no later priced round, no $1B mark."))

jl.write("j01d", L)
