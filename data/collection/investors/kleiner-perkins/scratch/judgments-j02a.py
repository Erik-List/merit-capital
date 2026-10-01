"""PRO-99 Kleiner Perkins, judge j02, queue batch 3 (coursera .. findthebest): classification of listed members.
Run with NQ_TAG=j02. No membership items in this batch; every row is on the firm's own list."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, POST, W

WV = "web_verified"
VRS = {"valuation_range_source": WV}
SA = "https://stockanalysis.com/stocks/{}/market-cap/"
NEA_COURSERA = "https://www.nea.com/blog/charting-a-new-course-in-online-education"
SF_FIN = "https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/"
DEX_VAL = "https://www.therobotreport.com/dexterity-picks-up-95m-funding-container-unloading-robots/"
FBN_VAL = "https://www.reuters.com/markets/us/farmers-business-network-valued-39-bln-after-adm-takes-stake-2021-11-18/"
FBN_A = "https://agfundernews.com/farmers-business-network-seals-15m-funding-deal-with-google-ventures"
DBX_J = "https://www.databricks.com/company/newsroom/press-releases/databricks-raising-10b-series-j-investment-62b-valuation"
EHEALTH_IRA = "https://www.sec.gov/Archives/edgar/data/1333493/000119312506087959/dex106.htm"
EPIZYME_S1 = "https://www.sec.gov/Archives/edgar/data/1571498/000119312513160271/d501246ds1.htm"
ASOF = "2026-09-30"

L = []

L.append(cls("coursera", city="Mountain View", usd=1310000000, rng="1b_plus", val_src=WV, val_cite=SA.format("cour"),
             asof=ASOF, extra=VRS,
             stage="Series A", stage_src=WV, stage_cite=NEA_COURSERA, stage_conf="high", entry_date="2012-04",
             flags=["stage_disputes_band"], focus="Consumer & Marketplaces",
             rounds=[rnd("2012-04-18", "Series A", 16000000, None, True, NEA_COURSERA, "press"),
                     rnd("2021-03-31", "IPO", None, None, None, jl.FTS("Coursera", "424B4"), "filing")],
             note="Online education, Mountain View. The firm entered at Coursera's first institutional round, the $16M "
                  "Series A of April 2012 backed by Kleiner Perkins and NEA (NEA's post of 2012-04-18; John Doerr on the "
                  "board since December 2011 per the S-1), not at the 2015 filing the Form D band read. Market cap $1.31B "
                  "on 2026-09-30 (stockanalysis.com), aligned with the NEA row."))

L.append(cls("coverwallet", status="acquired", rng="below_1b", country="US", city="New York", stage="undetermined",
             entry_date="2017", focus="Fintech & Payments",
             rounds=[rnd("2016-03", "Seed extension", None, None, None, None, "firm"),
                     rnd("2016-11-17", "Series A", 7800000, "Union Square Ventures", None, None, "company"),
                     rnd("2020-01", "Acquisition by Aon", None, None, None, None, "firm")],
             note="Small-business insurance platform, New York; acquired by Aon in January 2020 (the firm's exit field; "
                  "the USV book cites USV's own post). The firm's since-year is 2017, after the $7.8M Series A of "
                  "November 2016, and no source read names the round Kleiner Perkins entered, so the stage is undetermined."))

L.append(cls("crescendo-bioscience", status="acquired", rng="below_1b", city="South San Francisco",
             city_src="formd_address", focus="Healthcare & Bio",
             note="Rheumatoid-arthritis molecular diagnostics, South San Francisco (EDGAR business address and the "
                  "2009 listing); acquired by Myriad Genetics in 2014, as the firm's exit field and archived status say."))

L.append(cls("crossbar", status="private", rng="below_1b", city="Santa Clara", stage="undetermined", entry_date="2012",
             focus="Industrial & Robotics",
             rounds=[rnd("2012", "Unnamed round", 25000000, None, True, W("Crossbar, Inc."), "press")],
             note="ReRAM memory chips, Santa Clara (Wikipedia; EDGAR address); still operating (company site, DARIC chip "
                  "and security products). Wikipedia names Kleiner Perkins among the 2012 investors of $25M; the firm's "
                  "since-year 2008 predates the 2010 founding Wikipedia gives, and no source names the round, so the stage "
                  "is undetermined. Filings run to a $5.2M round in 2024; no priced round near $1B."))

L.append(cls("cultureamp", status="private", rng="1b_plus", usd=1500000000, val_src=WV, val_cite=W("Culture Amp"),
             asof="2021-07", extra=VRS, country="AU", country_src=WV, country_cite=W("Culture Amp"), city="Melbourne",
             stage="undetermined", entry_date="2016", flags=["stale", "model_disputes_source"], focus="SaaS",
             rounds=[rnd("2015", "Series A", 6300000, None, None, W("Culture Amp"), "press"),
                     rnd("2017-05-31", "Unnamed round (Form D)", 20000009, None, None, None, "filing"),
                     rnd("2021-07", "Series F", 150000000, "Sequoia Capital China, TDM Growth Partners", None,
                         W("Culture Amp"), "press")],
             note="Employee-experience software, based in Melbourne, Australia (Wikipedia), so the prefilled US is "
                  "replaced; the US Form D address is its San Francisco office. Mark: the July 2021 Series F valued it at "
                  "$1.5B (Wikipedia), stale past 24 months, aligned with the Felicis row; no later priced round found. The "
                  "only filing tying a roster name to it is the May 2017 Form D naming Ilya Fushman as director while he "
                  "was still at Index Ventures, so no source names a Kleiner Perkins round and the stage is undetermined."))

L.append(cls("databricks", city="San Francisco", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2024", focus="Data Infrastructure",
             rounds=[rnd("2024-12", "Series J", 10000000000, "Thrive Capital", None, DBX_J, "company")],
             note="Data and AI platform, San Francisco, as in the eleven sibling books. The firm's since-year is 2024, a "
                  "decade after founding; the round Databricks sold that year was the $10B Series J at $62B (the "
                  "company's release, led by Thrive), so any 2024 entry is Growth. No source names Kleiner Perkins in the "
                  "round, hence model at medium; the firm's own Growth label agrees."))

L.append(cls("datameer", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Data Infrastructure",
             note="Hadoop-era analytics platform, San Francisco (EDGAR address). After a 2021 recapitalisation the "
                  "business was sold in 2024, as the Redpoint row records; acquired, below $1B on every reported mark."))

L.append(cls("datastax", status="acquired", rng="below_1b", city="Santa Clara", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2014-09", focus="Data Infrastructure",
             rounds=[rnd("2014-09", "Series E", 106000000, None, None, W("DataStax"), "press"),
                     rnd("2022-06-15", "Unnamed round", 115000000, None, None, W("DataStax"), "press"),
                     rnd("2025-05-28", "Acquisition by IBM", None, None, None, W("DataStax"), "press")],
             note="Cassandra database company, Santa Clara; IBM completed its acquisition on 2025-05-28 (Wikipedia). The "
                  "firm's since-year 2014 falls on the $106M Series E of September 2014 (Wikipedia), the company's only "
                  "round that year, which the firm's Growth label matches; no page read names Kleiner Perkins in it, so "
                  "model at medium."))

L.append(cls("density", status="private", rng="below_1b", country="US", city="San Francisco", city_src=WV,
             stage="Growth", stage_src="first_party", stage_conf="high",
             stage_cite=POST("making-the-most-out-of-physical-space-is-a-matter-of-density"), entry_date="2020-07",
             focus="SaaS",
             rounds=[rnd("2020-07-27", "Series C", None, "Kleiner Perkins", True,
                         POST("making-the-most-out-of-physical-space-is-a-matter-of-density"), "firm")],
             note="Workplace occupancy sensing and analytics; the company's site gives 33 New Montgomery St, San "
                  "Francisco, and shows it operating. The firm's post of 2020-07-27 announces that it leads Density's "
                  "Series C, and its since-year is 2020, so the Series C is the entry (Growth). No priced round at $1B "
                  "or more found."))

L.append(cls("desktop-metal", city="Burlington", rng="below_1b", stage="Series A", stage_src=WV,
             stage_cite=W("Desktop Metal"), stage_conf="high", entry_date="2015", flags=["stage_disputes_band"],
             focus="Industrial & Robotics",
             rounds=[rnd("2015", "Series A", 14000000, None, True, W("Desktop Metal"), "press"),
                     rnd("2017-02", "Series C", 45000000, "GV", None, W("Desktop Metal"), "press"),
                     rnd("2024-07", "Acquisition by Nano Dimension", None, None, None, W("Desktop Metal"), "press")],
             note="Metal 3D printing, Burlington, Massachusetts. Wikipedia names Kleiner Perkins among the leading "
                  "funders of the roughly $14M Series A (the firm's since-year 2015, the 2015 Form D), so the entry is "
                  "the Series A rather than the 2016 filing the band read. Nano Dimension bought it in 2025 and it filed "
                  "for Chapter 11 in July 2025 (Wikipedia): acquired, no standalone figure, aligned with GV, Lux and NEA."))

L.append(cls("dexterity", status="private", rng="1b_plus", usd=1650000000, val_src=WV, val_cite=DEX_VAL, asof="2025-03",
             extra=VRS, city="Redwood City", stage="Series A", stage_src="first_party", stage_conf="high",
             stage_cite=POST("robots-with-human-like-dexterity"), entry_date="2020-07", flags=["stage_disputes_band"],
             focus="Industrial & Robotics",
             rounds=[rnd("2020-07-21", "Series A", None, "Kleiner Perkins", True,
                         POST("robots-with-human-like-dexterity"), "firm"),
                     rnd("2025-03", "Unnamed round", 95000000, None, None, DEX_VAL, "press"),
                     rnd("2026-05-21", "Unnamed round (Form D)", 50000000, None, None, jl.FORMD_CITE("dexterity"),
                         "filing")],
             note="Warehouse robotics, Redwood City. The firm's post of 2020-07-21 says it is leading Dexterity's Series "
                  "A (Lightspeed had seeded it in 2017), so the entry is the Series A, not the 2026 Form D the band read. "
                  "Mark: the $95M round of March 2025 at $1.65B (The Robot Report), aligned with the Lightspeed row; the "
                  "$50M 2026 filing disclosed no valuation."))

L.append(cls("diy", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2011", focus="Consumer & Marketplaces",
             rounds=[rnd("2015", "Unnamed round", 4000000, "Learn Capital", None, None, "press"),
                     rnd("2018-08", "Acquisition by littleBits", None, None, None, None, "press")],
             note="Kids' maker community (DIY.org, relaunched as JAM), San Francisco; littleBits acquired DIY Co in "
                  "August 2018, as the firm's exit field and the Spark row record. Bing Gordon's 2011 entry is not named "
                  "in any source read, so the stage is undetermined."))

L.append(cls("dji", country="CN", country_src=WV, country_cite=W("DJI"), city="Shenzhen", stage="Growth",
             stage_src="model", stage_conf="medium", entry_date="2015", focus="Consumer & Marketplaces",
             rounds=[rnd("2015-05", "Unnamed round", 75000000, "Accel", None, None, "company")],
             note="Drone maker headquartered in Shenzhen (Wikipedia), so the CN claim is confirmed. The firm's since-year "
                  "2015 is the year of DJI's late private rounds at a valuation of about $8B and up (Accel's $75M in May "
                  "2015), so the entry is Growth; no page read names Kleiner Perkins' round, hence model at medium."))

L.append(cls("docusign", city="San Francisco", usd=12550000000, rng="10b_plus", val_src=WV, val_cite=SA.format("docu"),
             asof=ASOF, extra=VRS, focus="SaaS",
             note="E-signature software headquartered in San Francisco (Wikipedia). Market cap $12.55B on 2026-09-30 "
                  "(stockanalysis.com), replacing the older figure, aligned with the Accel, GV, ICONIQ and Insight rows."))

L.append(cls("doordash", city="San Francisco", usd=79530000000, rng="10b_plus", val_src=WV, val_cite=SA.format("dash"),
             asof=ASOF, extra=VRS, stage="Growth", stage_src="first_party", stage_cite=SITE("doordash"),
             stage_conf="high", entry_date="2015-03", focus="Consumer & Marketplaces",
             rounds=[rnd("2015-03", "Series B", 40000000, "Kleiner Perkins", True, SITE("doordash"), "firm")],
             note="Food delivery, San Francisco. The firm's own company page says Kleiner Perkins entered in 2015 "
                  "leading DoorDash's Series B (its 2020 post repeats it; John Doerr on the board since March 2015 per the "
                  "S-1): Growth. Market cap $79.53B on 2026-09-30 (stockanalysis.com)."))

L.append(cls("drawbridge", status="acquired", rng="below_1b", city="San Mateo", stage="undetermined", entry_date="2010",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2011", "Series A", None, "Sequoia Capital", None, None, "press"),
                     rnd("2016", "Series C", 25000000, "Sequoia Capital", None, W("Drawbridge (company)"), "press"),
                     rnd("2019", "Acquisition by LinkedIn", None, None, None, W("Drawbridge (company)"), "press")],
             note="Cross-device advertising identity, San Mateo; LinkedIn acquired it in 2019 (Wikipedia). Wikipedia "
                  "names Kleiner Perkins among its funders without a round; the firm's since-year 2010 precedes the 2011 "
                  "Series A Sequoia led, and no source names Kleiner Perkins' round, so the stage is undetermined."))

L.append(cls("dropcam", city="San Francisco", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2013-06", focus="Consumer & Marketplaces",
             rounds=[rnd("2012-06", "Series B", 12000000, "Menlo Ventures", None, None, "press"),
                     rnd("2013-06", "Series C", 30000000, "Institutional Venture Partners", None, None, "press"),
                     rnd("2014-06", "Acquisition by Google (Nest)", 555000000, None, None, W("Dropcam"), "press")],
             note="Wi-Fi home cameras, San Francisco; Google bought it for $555M in June 2014 (Wikipedia). The firm's "
                  "since-year 2013 and its Digital Growth Fund tag fall on the $30M Series C of June 2013 that IVP led "
                  "(IVP's release, per the IVP row), Dropcam's only round that year: Growth, model at medium since no page "
                  "read names Kleiner Perkins in the round."))

L.append(cls("drugstore-com", status="acquired", rng="below_1b", country="US", city="Bellevue", stage="undetermined",
             entry_date="1998", focus="Consumer & Marketplaces",
             note="Online pharmacy, Bellevue, Washington; listed in 1999 and bought by Walgreens in 2011. Brook Byers "
                  "sat on the board from May 1998 (proxy of 2001) and KPCB funds filed 13Gs to 2010, but no source read "
                  "names the round the firm entered in 1998, so the stage is undetermined."))

L.append(cls("duolingo", city="Pittsburgh", usd=6660000000, rng="1b_plus", val_src=WV, val_cite=SA.format("duol"),
             asof=ASOF, extra=VRS, stage="Growth", stage_src=WV, stage_cite=W("Duolingo"), stage_conf="high",
             entry_date="2014-02", focus="Consumer & Marketplaces",
             rounds=[rnd("2011-10", "Series A", 3300000, "Union Square Ventures", None, None, "press"),
                     rnd("2012-09", "Series B", 15000000, "New Enterprise Associates", None, None, "press"),
                     rnd("2014-02", "Series C", 20000000, "Kleiner Perkins", True, W("Duolingo"), "press")],
             note="Language learning, Pittsburgh. Wikipedia names Kleiner Perkins as lead of the $20M Series C of 2014 "
                  "(the firm's page says it first invested in 2014): Growth, and the 2019 entry date the filings gave is "
                  "replaced. Market cap $6.66B on 2026-09-30 (stockanalysis.com), so the band falls from 10b_plus to "
                  "1b_plus, aligned with the NEA and USV rows."))

L.append(cls("dust-identity", status="private", rng="below_1b", city="Needham", city_src="formd_address",
             focus="Security",
             note="Diamond-based supply-chain identity tags; the 2019 Form D gives Needham, Massachusetts. No sale, "
                  "shutdown or priced round near $1B found."))

L.append(cls("edgespring", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="undetermined",
             entry_date="2011", focus="Data Infrastructure",
             rounds=[rnd("2013-05", "Unnamed round", 11000000, "Kleiner Perkins", True, None, "press"),
                     rnd("2013-06", "Acquisition by Salesforce", None, None, None, None, "press")],
             note="Business-intelligence platform, Mountain View; Salesforce acquired it in June 2013 (the firm's exit "
                  "field; the Lightspeed row cites TechCrunch for an $11M Kleiner Perkins round weeks earlier). Ted "
                  "Schlein's 2011 entry is not named in any source read, so the stage is undetermined."))

L.append(cls("egnyte", status="acquired", rng="below_1b", city="Mountain View", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2011", focus="SaaS",
             rounds=[rnd("2007", "Seed", 1000000, None, None, W("Egnyte"), "press"),
                     rnd("2009-07", "Unnamed round", 6000000, None, None, W("Egnyte"), "press"),
                     rnd("2011", "Unnamed round", 10000000, None, True, W("Egnyte"), "press"),
                     rnd("2012-07", "Series C", 16000000, "Google Ventures", None, None, "press"),
                     rnd("2025-02", "Majority buyout by GI Partners and TA Associates", None, None, None, None, "press")],
             note="Cloud content governance, Mountain View (Wikipedia). The firm's since-year 2011 falls on the $10M "
                  "round of 2011, the round before the $16M Series C of July 2012 that GV led with existing investors "
                  "Kleiner Perkins and Polaris, so it reads as the Series B: Growth, model at medium. GI Partners and TA "
                  "Associates took majority control in February 2025 (the GV row): acquired, aligned with GV."))

L.append(cls("ehealth-inc", country="US", city="Austin", usd=22740000, rng="below_1b", val_src=WV,
             val_cite=SA.format("ehth"), asof=ASOF, extra=VRS, stage="Series A", stage_src=WV, stage_cite=EHEALTH_IRA,
             stage_conf="medium", entry_date="1999", focus="Fintech & Payments",
             rounds=[rnd("1999", "Series A", None, None, True, EHEALTH_IRA, "filing"),
                     rnd("2006-10", "IPO", None, None, None, None, "filing")],
             note="Online health-insurance marketplace, now headquartered in Austin, aligned with the IVP row. The "
                  "investors' rights agreement filed with the 2006 S-1 lists the Series A investors as KPCB Holding (as "
                  "nominee) and the Weiss Peck & Greer funds; Joe Lacob joined the board in April 1999, the entry year "
                  "used. Market cap $22.7M on 2026-09-30 (stockanalysis.com)."))

L.append(cls("elcelyx-therapeutics", status="defunct", rng="below_1b", city="San Diego", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Metabolic-disease biotech, San Diego (EDGAR address). Its last Form D was a $1M round in 2018; in "
                  "2019 Anji acquired the rights to its lead diabetes compound (ANJ900, formerly NewMet), and the company "
                  "has filed and announced nothing since, so it reads defunct (medium; a web check of 2026-09-30 found no "
                  "sale of the company itself)."))

L.append(cls("electronic-arts", status="acquired", rng="below_1b", city="Redwood City", stage="undetermined",
             entry_date="1982", focus="Media, Gaming & Advertising",
             rounds=[rnd("1982", "Founding venture round", None, None, True, SITE("electronic-arts"), "firm"),
                     rnd("2026-08-04", "Take-private by PIF, Silver Lake and Affinity Partners", 55000000000, None, None,
                         None, "press")],
             note="Video games, Redwood City (Wikipedia). The $55B take-private by PIF, Silver Lake and Affinity closed "
                  "on 2026-08-04 and the stock was delisted, as the Sequoia row records, so the row reads acquired with "
                  "no standalone figure, replacing the prefilled public cap. The firm's page says Brook Byers met EA in "
                  "1982 while it was raising venture capital, but names no round, so the stage is undetermined."))

L.append(cls("endgame", status="acquired", rng="below_1b", country="US", city="Arlington", stage="Series A",
             stage_src="model", stage_conf="medium", entry_date="2010-10", focus="Security",
             rounds=[rnd("2010-10", "Unnamed round", 29000000, None, True, W("Endgame, Inc."), "press"),
                     rnd("2013-03", "Series B", 23000000, "Paladin Capital Group", True, W("Endgame, Inc."), "press"),
                     rnd("2019", "Acquisition by Elastic", None, None, None, None, "press")],
             note="Endpoint security company (Endgame, Inc., Arlington, Virginia); Elastic acquired it in 2019. Wikipedia "
                  "names Kleiner Perkins in the $29M investment of October 2010 (the firm's since-year) and calls the "
                  "March 2013 round the Series B, so the 2010 round reads as the Series A (model, medium). The Menlo and "
                  "EQT Ventures rows named Endgame are the product-led sales company, a different firm."))

L.append(cls("engine-ml", status="acquired", rng="below_1b", country="US", stage="undetermined", entry_date="2018",
             flags=["city_unknown"], focus="Data Infrastructure",
             note="Deep-learning infrastructure startup founded by Alex Fielding; the firm's exit field says Ripcord "
                  "acquired it. No filing or article read places the company in a city or names the firm's 2018 round."))

L.append(cls("enjoy-inc", status="defunct", rng="below_1b", city="Palo Alto", focus="Consumer & Marketplaces",
             note="Ron Johnson's in-home tech delivery company, Palo Alto; listed through a SPAC in October 2021 (KPCB "
                  "XVI Founders Fund among the selling holders in the resale S-1) and filed for Chapter 11 in June 2022. "
                  "Read defunct, aligned with the a16z row; no sale of the business as a going concern was established."))

L.append(cls("enterpret", status="private", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="first_party", stage_cite=POST("enterpret-series-a"), stage_conf="high", entry_date="2021",
             grad="graduated", grad_src="first_party", grad_cite=POST("enterpret-series-a"), grad_conf="high",
             focus="AI & Applied AI",
             extra={"valuation_range_source": WV, "valuation_citation": POST("enterpret-series-a")},
             rounds=[rnd("2021", "Seed", None, "Kleiner Perkins", True, POST("enterpret-series-a"), "firm"),
                     rnd("2024-12-04", "Series A", 20800000, "Canaan Partners", True, POST("enterpret-series-a"), "firm")],
             note="Customer-feedback AI, San Francisco. The firm's post of 2024-12-04 says it has been in business with "
                  "the founders since leading their seed round in 2021 and is investing again in the Series A ($20.8M, "
                  "Canaan-led): Seed entry, graduated. Momentum check 2026-09-30 (web search): the Series A disclosed no "
                  "valuation and no priced round at $1B or more exists, so below_1b."))

L.append(cls("epic-games", city="Cary", stage="Growth", stage_src=WV, stage_cite=W("Epic Games"), stage_conf="high",
             entry_date="2018-10", focus="Media, Gaming & Advertising",
             rounds=[rnd("2018-10", "Unnamed round", 1250000000, "KKR", True, W("Epic Games"), "press")],
             note="Games and engine maker, Cary, North Carolina. Wikipedia names Kleiner Perkins among the seven firms "
                  "in the $1.25B investment of October 2018 (the firm's since-year 2018): Growth."))

L.append(cls("epiphany-inc", status="acquired", rng="below_1b", city="San Mateo", stage="undetermined", entry_date="1998",
             focus="SaaS",
             note="E.piphany, marketing and CRM software, San Mateo; SSA Global acquired it in September 2005 "
                  "(Wikipedia). Doug Mackenzie joined the board in January 1998 (2001 proxy), but no source read names the "
                  "round, so the stage is undetermined."))

L.append(cls("epizyme", country="US", city="Cambridge", rng="below_1b", stage="Series A", stage_src=WV,
             stage_cite=EPIZYME_S1, stage_conf="high", entry_date="2008", focus="Healthcare & Bio",
             rounds=[rnd("2008-02", "Series A", None, None, True, EPIZYME_S1, "filing"),
                     rnd("2009-09-18", "Series B", None, None, True, EPIZYME_S1, "filing")],
             note="Epigenetic cancer drugs, Cambridge, Massachusetts; acquired by Ipsen in 2022. The 2013 S-1's "
                  "principal-stockholders table shows Kleiner Perkins Caufield & Byers XIII holding series A as well as "
                  "series B preferred, and the firm's since-year is 2008, the year of the Series A: Series A entry."))

L.append(cls("essence-healthcare", status="private", rng="below_1b", city="Maryland Heights", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Medicare Advantage plan, still enrolling members for 2026 (its site). The holding company files as "
                  "Lumeris Group Holdings (formerly Essence Group Holdings) from Maryland Heights, Missouri, and sold $50M "
                  "and $100M rounds in 2023-24 with no valuation disclosed; below_1b."))

L.append(cls("excite-home", status="acquired", rng="below_1b", country="US", city="Redwood City", stage="undetermined",
             entry_date="1995-01", focus="Media, Gaming & Advertising",
             rounds=[rnd("1995-01", "First round", 250000, None, True, W("Excite (web portal)"), "press"),
                     rnd("1999", "Merger into @Home Network", None, None, None, W("Excite (web portal)"), "press")],
             note="Excite, the web portal (excite.com), a separate investment from @Home Network. In January 1995 Vinod "
                  "Khosla of Kleiner Perkins arranged a $250,000 'first round' (Wikipedia), a description, not a round "
                  "name, so the stage is undetermined. Excite merged into @Home in 1999: acquired."))

L.append(cls("extensity", status="acquired", rng="below_1b", country="US", city="Emeryville", stage="undetermined",
             entry_date="1997", focus="SaaS",
             note="Expense and time-management software, Emeryville; Geac acquired it in 2003. Ted Schlein joined the "
                  "board in May 1997 (2001 proxy), but no source read names the round, so the stage is undetermined."))

L.append(cls("extreme-networks", status="public", usd=2800000000, rng="1b_plus", val_src=WV, val_cite=SA.format("extr"),
             asof=ASOF, extra=VRS, city="Morrisville", stage="undetermined", entry_date="1997",
             focus="Data Infrastructure",
             note="Networking equipment, based in Morrisville, North Carolina (Wikipedia). Market cap $2.80B on "
                  "2026-09-30 (stockanalysis.com). Wikipedia lists Kleiner Perkins among early investors without a round, "
                  "so the stage is undetermined."))

L.append(cls("fabfitfun", status="private", rng="below_1b", city="Los Angeles", focus="Consumer & Marketplaces",
             note="Subscription-box company, Los Angeles; still private and acquiring (the NEA row). The $100M 2019 round "
                  "disclosed no valuation; no priced round at $1B or more found."))

L.append(cls("facebook", country="US", city="Menlo Park", usd=1850000000000, rng="100b_plus", val_src=WV,
             val_cite=SA.format("meta"), asof=ASOF, extra=VRS, stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2011", focus="Media, Gaming & Advertising",
             rounds=[rnd("2011", "Secondary purchase", None, None, True, None, "press")],
             note="Meta Platforms, Menlo Park. The firm's Digital Growth Fund bought into Facebook in 2011 (its since-year "
                  "and initiative tag), a pre-IPO purchase in a company valued above $50B, and KPCB Holdings signed the "
                  "sixth amended investors' rights agreement filed with the 2012 S-1/A: Growth, model at medium since no "
                  "page names the transaction. Market cap $1.85T on 2026-09-30 (stockanalysis.com)."))

L.append(cls("farmers-business-network", status="private", usd=3900000000, rng="1b_plus", val_src=WV, val_cite=FBN_VAL,
             asof="2021-11-18", extra=VRS, city="San Carlos", stage="Series A", stage_src=WV, stage_cite=FBN_A,
             stage_conf="high", flags=["stale", "stage_disputes_band"], focus="Fintech & Payments",
             rounds=[rnd("2014-03-26", "Series A", 6000000, "Kleiner Perkins", True, FBN_A, "press"),
                     rnd("2014", "Series A-1", 3000000, "DBL", None, FBN_A, "press"),
                     rnd("2015-05", "Series B", 15000000, "Google Ventures", None, FBN_A, "press"),
                     rnd("2021-11-18", "Series G", None, "Fidelity", None, FBN_VAL, "press")],
             note="Farmer network, input marketplace and farm finance, San Carlos (Wikipedia, the GV row). AgFunderNews "
                  "(2015-05-20) says FBN raised almost $6M in Series A funding from Kleiner Perkins before the GV-led "
                  "Series B; KP partner Amol Deshpande co-founded it, and the $6M Form D of 2014 is that round, so the "
                  "entry is the Series A, not a Seed, and no graduation applies. Mark: $3.9B at the November 2021 round "
                  "(Reuters), stale; the July 2025 raise disclosed no valuation."))

L.append(cls("farmers-edge", status="acquired", rng="below_1b", city="Winnipeg", city_src="formd_address",
             stage="undetermined", entry_date="2014", focus="SaaS",
             note="Precision-agriculture data platform, Winnipeg (EDGAR address); listed in Toronto in 2021 and taken "
                  "private by Fairfax in 2023 (the firm's exit field). The firm's 2014 entry is not named in any source "
                  "read (the only Form D naming its partners is an $825K 2015 filing), so the stage is undetermined."))

L.append(cls("fauna", status="acquired", rng="below_1b", city="New York", city_src="formd_address",
             focus="Industrial & Robotics",
             note="Fauna Robotics, home robots, New York (EDGAR address). The firm's post of 2026-03-24 announces Fauna "
                  "joining Amazon and its exit field names Amazon: acquired. The GV row named Fauna is FaunaDB, the "
                  "shut database company, a different firm."))

L.append(cls("figma", city="San Francisco", usd=11200000000, rng="10b_plus", val_src=WV, val_cite=SA.format("fig"),
             asof=ASOF, extra=VRS, stage="Growth", stage_src="first_party",
             stage_cite=POST("figma-made-design-collaborative-today-it-makes-history"), stage_conf="high",
             entry_date="2017", focus="SaaS",
             rounds=[rnd("2015-12", "Series A", 14000000, "Greylock Partners", None, None, "press"),
                     rnd("2017", "Series B", 25000000, "Kleiner Perkins", True,
                         POST("figma-made-design-collaborative-today-it-makes-history"), "firm"),
                     rnd("2019-02", "Series C", 40000000, "Sequoia Capital", True, None, "press")],
             note="Collaborative design software, San Francisco; NYSE FIG since July 2025. The firm's post of 2025-07-31 "
                  "says 'In 2017 we led Figma's Series B round' (Wikipedia dates the $25M announcement to February 2018; "
                  "Mamoon Hamid on the board from December 2017), so the Growth entry is re-dated from the 2019 filing to "
                  "2017. Market cap $11.20B on 2026-09-30 (stockanalysis.com); the prefilled $0 was a pre-listing float."))

L.append(cls("fin", status="private", usd=3600000000, rng="1b_plus", val_src=WV, val_cite=SF_FIN, asof="2026-06-15",
             extra=VRS, city="San Francisco", stage="Growth", stage_src=WV, stage_cite=W("Fin (company)"),
             stage_conf="high", entry_date="2018", focus="AI & Applied AI",
             rounds=[rnd("2013-03", "Series A", 6000000, "Social Capital", None, W("Fin (company)"), "press"),
                     rnd("2014-01", "Series B", 23000000, "Bessemer Venture Partners", None, W("Fin (company)"), "press"),
                     rnd("2018", "Series D", 125000000, "Kleiner Perkins", True, W("Fin (company)"), "press"),
                     rnd("2026-06-15", "Definitive agreement, sale to Salesforce", 3600000000, None, None, SF_FIN,
                         "company")],
             note="Intercom, renamed Fin in 2026 (AI customer service), San Francisco. Wikipedia: Kleiner Perkins led the "
                  "$125M Series D of 2018, the firm's first round (the site's 2013 since-year is Mamoon Hamid's Social "
                  "Capital Series A, before he joined). Salesforce signed a definitive agreement on 2026-06-15 to buy Fin "
                  "for about $3.6B, closing expected in its fiscal Q4 2027; signed but not closed, so private at the "
                  "agreed price, aligned with the ICONIQ row, although the firm's page already says Acquired."))

L.append(cls("findthebest", status="acquired", rng="below_1b", city="Santa Barbara", grad="graduated", grad_src=WV,
             grad_cite=W("Graphiq"), grad_conf="high", focus="Consumer & Marketplaces",
             rounds=[rnd("2010-12", "Unnamed round", 2000000, "Kleiner Perkins", True, W("Graphiq"), "press"),
                     rnd("2011", "Unnamed round", 4000000, "Kleiner Perkins", True, W("Graphiq"), "press"),
                     rnd("2013", "Series B", 11000000, "New World Ventures", True, W("Graphiq"), "press"),
                     rnd("2017-05", "Acquisition by Amazon", 50000000, None, None, W("Graphiq"), "press")],
             note="FindTheBest, renamed Graphiq, Santa Barbara; Amazon bought it in May 2017 for an estimated $50M "
                  "(Wikipedia). After Kleiner Perkins' $2M of December 2010 (the entry) and $4M in 2011, the company "
                  "raised an $11M Series B from New World, Kleiner Perkins and others (Wikipedia): a later round named "
                  "Series B graduates the seed, although the Form D layer, reading amounts only, did not."))

jl.write("j02a", L)
