"""PRO-100 NEA grind, queue batch 3 (judge c2): 45 listed members, classification only.
Each row read from the firm's own listing and posts first, then SEC filings, then press and Wikipedia.
Run: NQ_TAG=c2 python3 judgments-c2a.py"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, rnd, POST, SITE, W, NEWS, FTS = jl.cls, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.FTS
L = []
VW = {"valuation_range_source": "web_verified"}
GRAD_LEFT = "Graduation left for the graduation pass."
ASOF = "2026-09-30"

# ---------------------------------------------------------------- old book, acquired, round not on record
L.append(cls("bay-networks-wellfleet", status="acquired", rng="below_1b", country="US", city="Santa Clara",
             stage="undetermined", entry_date="1990", focus="Data Infrastructure",
             note="Wellfleet Communications (Bedford, later Billerica MA), routers; merged with SynOptics in October 1994 "
                  "to form Bay Networks (Santa Clara), which Nortel bought in June 1998 for $9.1B (Wikipedia). City is "
                  "Bay Networks' last headquarters. NEA's first investment is 1990 (the firm's own year); no source read "
                  "names the round.",
             rounds=[]))

L.append(cls("berkeley-networks", status="acquired", rng="below_1b", country="US", city="Milpitas",
             city_src="web_verified", stage="undetermined", entry_date="1996", focus="Data Infrastructure",
             note="Berkeley Networks, enterprise IP switches, headquartered in Milpitas CA (Wikipedia infobox); FORE "
                  "Systems bought it in 1998 for about $250M. NEA's first investment is 1996 (the firm's own year); no "
                  "source read names the round.",
             rounds=[]))

L.append(cls("bethesda-research-labs", status="acquired", rng="below_1b", country="US", city="Gaithersburg",
             stage="undetermined", entry_date="1980", focus="Healthcare & Bio",
             note="Bethesda Research Laboratories (Gaithersburg MD), molecular biology enzymes; merged with GIBCO in 1983 "
                  "to form Life Technologies (Wikipedia, Life Technologies), the firm's exit line. NEA's first investment "
                  "is 1980 (the firm's own year); no source read names the round.",
             rounds=[]))

BCD_IRA = "https://www.sec.gov/Archives/edgar/data/1289814/000119312508013327/dex44.htm"
BCD_F1 = "https://www.sec.gov/Archives/edgar/data/1289814/000119312508013327/df1.htm"
L.append(cls("bcd-semiconductor", status="acquired", rng="below_1b", country="CN", country_src="web_verified",
             country_cite=BCD_F1, city="Shanghai", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=BCD_IRA, entry_date="2004-04-27", focus="Industrial & Robotics",
             note="BCD Semiconductor Manufacturing, analog and power ICs; principal executive offices in Minhang "
                  "District, Shanghai (its 2008 F-1). The F-1's investors' rights agreement lists New Enterprise "
                  "Associates 11 and NEA Ventures 2004 among the Series C Holders under the Series C Preference Shares "
                  "Purchase Agreement of 2004-04-27, the firm's first-investment year; Series A and B preceded it, so the "
                  "entry is Growth, as in the Redpoint row. Listed on Nasdaq (BCDS) in 2011, acquired by Diodes in 2013.",
             rounds=[rnd("2004-04-27", "Series C", None, None, True, BCD_IRA, "filing")]))

# ---------------------------------------------------------------- public rows
BE_CAP = "https://stockanalysis.com/stocks/be/market-cap/"
L.append(cls("bloom-energy", rng="10b_plus", usd=82480000000, val_src="web_verified", val_cite=BE_CAP, asof=ASOF,
             extra=VW, city="San Jose", stage="undetermined", entry_date="2003", focus="Climate & Energy",
             flags=["model_disputes_source"],
             note="Bloom Energy (founded 2001 as Ion America), solid oxide fuel cells, headquartered in San Jose "
                  "(Wikipedia). Market cap $82.48B as of 2026-09-30 (stockanalysis.com), which replaces the 2025-06-30 "
                  "public float of $3.9B on file (the stock rose about 379% in a year): band 10b_plus. NEA 10 and NEA "
                  "Ventures 2003 sign its registration rights agreement and the firm's first-investment year is 2003; "
                  "no source read names the round NEA entered.",
             rounds=[]))

L.append(cls("black-diamond-therapeutics", city="Cambridge", focus="Healthcare & Bio",
             note="Black Diamond Therapeutics, precision oncology, headquartered in Cambridge MA (Nasdaq: BDTX); the Form "
                  "D address in Stony Brook NY is its founding lab's."))

L.append(cls("box", city="Redwood City", stage="undetermined", entry_date="2008", focus="SaaS",
             note="Box, cloud content management, headquartered in Redwood City. The firm's first-investment year is "
                  "2008; its S-1 names New Enterprise Associates only among the holders its credit agreement permits, "
                  "and no source read names the round NEA entered.",
             rounds=[]))

# ---------------------------------------------------------------- acquired rows, stage from the filings (known)
L.append(cls("bitglass", status="acquired", rng="below_1b", city="Campbell", focus="Security",
             note="Bitglass, cloud access security broker (Campbell CA); acquired by Forcepoint in 2021, the firm's exit "
                  "line. The Form D address is an earlier Palo Alto office."))

L.append(cls("blue-cheetah", status="acquired", rng="below_1b", city="Sunnyvale", city_src="formd_address",
             focus="Industrial & Robotics",
             note="Blue Cheetah Analog Design, die-to-die chiplet interconnect IP (Sunnyvale, the Form D address); "
                  "acquired by Tenstorrent in 2025, the firm's exit line."))

L.append(cls("brandless", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="Brandless, direct-to-consumer essentials (San Francisco). It closed in February 2020 and its brand "
                  "was bought and relaunched by new owners, read acquired under the asset-sale rule, aligned with the GV "
                  "and Redpoint rows. The Form D band's Growth entry agrees with TechCrunch (2017-07-11, cited in the GV "
                  "row): NEA and GV closed the $35M Series B."))

# ---------------------------------------------------------------- Wikipedia names NEA's round
BELLY_W = W("Belly (loyalty program)")
L.append(cls("belly", status="acquired", rng="below_1b", city="Chicago", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=BELLY_W, entry_date="2013-08", focus="SaaS",
             note="Belly, merchant loyalty platform (Chicago). Wikipedia: in August 2013 Belly received a $12.1M Series "
                  "B-1 round led by New Enterprise Associates, the firm's first-investment year; Lightbank's ~$3M seed "
                  "and a16z's 2012 Series B came first, so the entry is Growth. In November 2018 the Belly product line "
                  "assets were acquired from Hatch Loyalty by Mobivity Holdings (Wikipedia; the firm's exit line), so "
                  "the row reads acquired under the asset-sale rule; the a16z row reads defunct and should align.",
             rounds=[rnd("2011", "Seed", 3000000, "Lightbank", False, BELLY_W, "press"),
                     rnd("2013-08", "Series B-1", 12100000, "New Enterprise Associates", True, BELLY_W, "press")]))

BOINGO_W = W("Boingo Wireless")
L.append(cls("boingo-wireless", city="Frisco", city_src="web_verified", stage="undetermined", entry_date="2001",
             rng="below_1b", focus="Data Infrastructure",
             note="Boingo Wireless, Wi-Fi and DAS networks, founded in 2001 by Sky Dayton; taken private by Digital "
                  "Colony (DigitalBridge) in 2021 for about $854M, and it moved its headquarters from Los Angeles to "
                  "Frisco TX in December 2022 (Wikipedia). NEA 10 and NEA Ventures 2001 held 22.5% at the 2011 IPO "
                  "(S-1); the S-1 shows Series A, A-2 and B preferred but does not tie NEA to a series, so the round is "
                  "not on record.",
             rounds=[]))

BLUE_OCEAN_PR = ("https://www.prnewswire.com/news-releases/blue-ocean-smart-system-to-introduce-chiplet-based-high-"
                 "performance-low-power-ai-chips-301331342.html")
L.append(cls("blue-ocean", status="private", rng="below_1b", country="TW", country_src="web_verified",
             country_cite=BLUE_OCEAN_PR, city="Hsinchu", city_src="web_verified", stage="Series A",
             stage_src="web_verified", stage_conf="medium", stage_cite=BLUE_OCEAN_PR, entry_date="2021",
             focus="Industrial & Robotics",
             note="Blue Ocean Smart System, chiplet-based AI chips for cloud and edge (the firm's description), founded "
                  "2019 and headquartered in Hsinchu, Taiwan, with R&D in Nanjing and Shanghai (its own release, "
                  "2021-07-12). The release says the A round was led by IDG Capital and ARM China and the A+ round by "
                  "'NEA Capital' and Henderson Capital in early 2021; NEA lists it with Carmen Chang on the board and a "
                  "2020 first investment, so the entry is the A+ extension, Series A. The General Catalyst and Insight "
                  "rows named Blue Ocean are a different company (a San Francisco SaaS).",
             rounds=[rnd(None, "Series A", None, "IDG Capital; ARM China", False, BLUE_OCEAN_PR, "company"),
                     rnd("2021", "Series A+", None, "NEA; Henderson Capital", True, BLUE_OCEAN_PR, "company")]))

# ---------------------------------------------------------------- recent rows, press names the round
BASALT_A = NEWS("basalt", "Series A Led by NEA to Speed")
L.append(cls("basalt", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("basalt"), entry_date="2025", grad="graduated",
             grad_src="web_verified", grad_conf="high", grad_cite=BASALT_A, focus="Healthcare & Bio",
             flags=["city_unknown"],
             note="Basalt Health (basalt.health), EMR-integrated admissions software for post-acute care. The firm's own "
                  "listing labels NEA's 2025 first investment Seed; the company then raised a $20M Series A led by NEA "
                  "(Business Wire headline, 2026-09-24), a later round named Series A, so the row graduated. No "
                  "valuation disclosed. The company's site and the headline give no city. The Y Combinator and General "
                  "Catalyst rows named Basalt are a different company (satellite constellation software).",
             rounds=[rnd("2025", "Seed", None, None, True, SITE("basalt"), "firm"),
                     rnd("2026-09-24", "Series A", 20000000, "NEA", True, BASALT_A, "company")]))

BACKFLIP_A = NEWS("backflip-ai", "turn text into AI-generated designs")
L.append(cls("backflip-ai", status="private", rng="below_1b", country="US", stage="Series A",
             stage_src="web_verified", stage_conf="high", stage_cite=BACKFLIP_A, entry_date="2024-12-19",
             focus="AI & Applied AI", flags=["city_unknown"],
             note="Backflip AI, generative AI for 3D design and CAD, founded December 2022 by Markforged's founders. "
                  "TechCrunch (2024-12-19): a16z and NEA co-led the $30M Series A; an earlier seed is undisclosed and not "
                  "tied to NEA, and the firm's first-investment year is 2024, so the entry is the Series A (the a16z row "
                  "agrees). No valuation disclosed. Momentum slice checked 2026-09-30 (Google News, 'Backflip AI'): no "
                  "later priced round, below $1B. City: neither the article nor the site states a headquarters (the "
                  "careers page lists one San Francisco role).",
             rounds=[rnd(None, "Seed", None, None, None, BACKFLIP_A, "press"),
                     rnd("2024-12-19", "Series A", 30000000, "a16z; NEA", True, BACKFLIP_A, "press")]))

BELONG_A = NEWS("belong-health", "Closes $40 Million Series A")
L.append(cls("belong-health", status="private", rng="below_1b", city="Philadelphia", city_src="web_verified",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=BELONG_A,
             entry_date="2021-12-15", focus="Healthcare & Bio",
             note="Belong Health, Medicare Advantage and special-needs plans built with regional health plans, "
                  "headquartered in Philadelphia (its release; the Form D address is Radnor PA). NEA led the $40M Series "
                  "A (PR Newswire, 2021-12-15) with seed investor Maverick Ventures, the firm's first-investment year; "
                  "Mohamad Makhzoumi joined the board. The entry date on file (2025-11-13) was read off a later Form D "
                  "and is replaced by the Series A's. A 2025 Form D reports a further $58.3M offering; no valuation "
                  "disclosed.",
             rounds=[rnd(None, "Seed", None, "Maverick Ventures", False, BELONG_A, "company"),
                     rnd("2021-12-15", "Series A", 40000000, "NEA", True, BELONG_A, "company")]))

AVIADO_A = NEWS("aviadobio", "Pioneering company launches to advance")
L.append(cls("aviadobio", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=AVIADO_A, city="London", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=AVIADO_A, entry_date="2021-12-01", focus="Healthcare & Bio",
             note="AviadoBio, gene therapies for frontotemporal dementia and ALS, spun out of the UK DRI at King's "
                  "College London. At launch (UK DRI, 2021-12-01) it announced an $80M (GBP 58.6M) Series A led by NEA and "
                  "co-led by Monograph Capital, after a $16.5M seed from Advent, the Dementia Discovery Fund, F-Prime and "
                  "others; NEA's first-investment year is 2021, so the entry is the Series A. Astellas paid $50M in 2024 "
                  "for an option on its lead program (Fierce Biotech), a licensing deal, not a mark; below $1B.",
             rounds=[rnd(None, "Seed", 16500000, None, False, AVIADO_A, "press"),
                     rnd("2021-12-01", "Series A", 80000000, "NEA", True, AVIADO_A, "press")]))

BESTOW_A = NEWS("bestow", "Bestow Raises $15 Million in Series A")
BESTOW_D = NEWS("bestow", "lands $120M Series D")
L.append(cls("bestow", status="private", rng="below_1b", country="US", city="Dallas", stage="Seed", stage_src="model",
             stage_conf="low", entry_date="2018", grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite=BESTOW_A, focus="Fintech & Payments", flags=["stage_uncited", "stage_disputes_band"],
             note="Bestow, term life insurance technology (Dallas). The firm's own listing labels its 2018 entry Growth, "
                  "but the company's release (PR Newswire, 2018-05-21) says Valar Ventures led the $15M Series A 'with "
                  "participation from existing investors New Enterprise Associates (NEA)', bringing total financing to "
                  "just over $18M: NEA held a position from the roughly $3M raised before the Series A, a seed-sized "
                  "round no page names (stage uncited, low). The Series A is a later round named Series A, so the row "
                  "graduated. Series C $70M (December 2020); Series D $120M co-led by Goldman Sachs Alternatives and "
                  "Smith Point Capital (TechCrunch, 2025-05-13), valuation undisclosed ('approximately doubled' since "
                  "the Series C), so no figure bands the row: below $1B.",
             rounds=[rnd(None, "pre-Series A (unnamed)", None, None, True, BESTOW_A, "company"),
                     rnd("2018-05-21", "Series A", 15000000, "Valar Ventures", True, BESTOW_A, "company"),
                     rnd("2020-12", "Series C", 70000000, None, None, BESTOW_D, "press"),
                     rnd("2025-05-13", "Series D", 120000000, "Goldman Sachs Alternatives; Smith Point Capital", True,
                         BESTOW_D, "press")]))

BD_Q = NEWS("betterdoctor", "Quest Analytics takes on network")
L.append(cls("betterdoctor", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             stage="undetermined", focus="Healthcare & Bio",
             note="BetterDoctor, provider directory data (San Francisco, the Form D address). Quest Analytics acquired it "
                  "for an undisclosed amount (Healthcare Dive, 2018-06-19). NEA's first investment is 2014, the year of "
                  "the company's one Form D ($10.4M, Mohamad Makhzoumi a director); no source read names that round, and "
                  "the Form D band declined it (company incorporated 2011).",
             rounds=[]))

BLISS = "https://globalventuring.com/corporate/investment/fraud-debt-andlicensing-healthcare-startup-insolvencies/"
L.append(cls("blend", status="defunct", rng="below_1b", city="Watertown", city_src="formd_address",
             focus="Healthcare & Bio", flags=["model_disputes_source"],
             extra={"valuation_source": None, "valuation_asof": None, "valuation_range_source": None,
                    "is_public": False, "public_since": None},
             note="This row is Blend Therapeutics (Watertown MA, the Form D address; drug conjugates), NEA's 2011 "
                  "biotech with James Barrett and Sheel Tyle as directors, not Blend Labs: the public status and the "
                  "$696.5M float on file came from a join to the mortgage-software company and are removed. Blend "
                  "Therapeutics was rebooted as Tarveda Therapeutics in 2016 (Endpoints, 2017-02-02) and Tarveda was "
                  "liquidated in April 2022 after raising nearly $130M (Global Venturing, 2024-07-03, " + BLISS + "): "
                  "defunct. The base also carries four Form D filings of Blend Systems, Inc. (CIK 1560253, Los Altos), "
                  "another company. " + GRAD_LEFT))

BLIQ_A = NEWS("bliq", "raises $13.5M to boost earnings")
BLIQ_IMP = "https://bliq.ai/impressum"
L.append(cls("bliq", status="private", rng="below_1b", country="DE", country_src="web_verified",
             country_cite=BLIQ_IMP, city="Berlin", city_src="web_verified", stage="Series A",
             stage_src="web_verified", stage_conf="high", stage_cite=BLIQ_A, entry_date="2022-05-11",
             focus="Consumer & Marketplaces",
             note="Bliq GmbH, Berlin (its imprint, Lohmuehlenstrasse 65), an app that aggregates ride and delivery jobs "
                  "for gig drivers; bliq.app now redirects to bliq.ai, which offers a driverless car subscription. NEA "
                  "led the $13.5M Series A (Tech Funding News, 2022-05-11) with Speedinvest and others, after a EUR 2M "
                  "seed in late 2020 (EU-Startups); NEA's first-investment year is 2022, so the entry is the Series A. "
                  "No valuation disclosed.",
             rounds=[rnd("2020", "Seed", None, None, False, BLIQ_A, "press"),
                     rnd("2022-05-11", "Series A", 13500000, "NEA", True, BLIQ_A, "press")]))

BLOCK_B = NEWS("block-renovation", "Raises Another $40M to Modernize")
L.append(cls("block-renovation", status="private", rng="below_1b", country="US", city="New York",
             stage="Seed", stage_src="first_party", stage_conf="medium", stage_cite=SITE("block-renovation"),
             entry_date="2018", grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=BLOCK_B,
             focus="Consumer & Marketplaces",
             note="Block Renovation, kitchen and bath renovation platform (New York). The firm's own listing labels its "
                  "2018 first investment Seed (the company launched in December 2018, The Real Deal). AlleyWatch "
                  "(2021-07-26): a $40M Series B from NEA, Giant Ventures, Lerer Hippeau, Morningside and Obvious, $54M "
                  "raised in total; a later round named Series B, so the row graduated. No valuation disclosed; a new "
                  "CEO was appointed in January 2025 (PR Newswire).",
             rounds=[rnd("2018", "Seed", None, None, True, SITE("block-renovation"), "firm"),
                     rnd("2021-07", "Series B", 40000000, None, True, BLOCK_B, "press")]))

L.append(cls("benchprep", status="private", rng="below_1b", country="US", city="Chicago", stage="undetermined",
             entry_date="2012-07", focus="SaaS",
             note="BenchPrep, online learning platform for credentialing bodies and publishers (Chicago), founded 2009 as "
                  "Watermelon Express. Wikipedia: in July 2012 it announced a $6M round from New Enterprise Associates and "
                  "Revolution, the firm's first-investment year; no source read names that round. Built In Chicago "
                  "(2019-01-15): a $20M Series C led by Jump Capital and Owl Ventures, $28.2M raised in total. Still "
                  "operating (CEO interview, December 2024).",
             rounds=[rnd("2012-07", None, 6000000, "NEA; Revolution", True, None, "press"),
                     rnd("2019-01-15", "Series C", 20000000, "Jump Capital; Owl Ventures", False,
                         NEWS("benchprep", "raises $20M Series C to double"), "press")]))

L.append(cls("beachmint", status="acquired", rng="below_1b", city="Santa Monica", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="BeachMint, celebrity-curated subscription e-commerce (JewelMint, StyleMint; Santa Monica, the Form D "
                  "address). After its board ousted the founders and returned $20M to investors (Business of Fashion, "
                  "2013-07-03), BeachMint combined with Conde Nast's Lucky magazine in August 2014 (New York Times, "
                  "'Lucky Magazine Gets an E-Partner to Shop With'), the firm's exit line 'Acquired by Conde Nast': a "
                  "merger into another company, acquired. " + GRAD_LEFT))

L.append(cls("beehiiv", status="private", rng="below_1b", city="New York", city_src="formd_address", focus="SaaS",
             note="beehiiv, newsletter platform (New York). NEA's entry is the $33M Series B of April 2024 (Business Wire "
                  "headline), which agrees with the Form D band; no valuation disclosed (a GetLatka estimate of $225M "
                  "stays out, Rule A), and Google News on 2026-09-30 shows no later priced round: below $1B, as in the "
                  "Lightspeed row."))

L.append(cls("big-data-federation", status="private", rng="below_1b", country="US", city="San Jose",
             city_src="web_verified", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("big-data-federation"), entry_date="2019", focus="AI & Applied AI",
             note="Big Data Federation, Inc., machine-learning predictions of financial and economic fundamentals, "
                  "incorporated 2015 and headquartered in San Jose (theorg.com; directory pages give 1735 Technology "
                  "Drive), with an office in Moldova. The firm's own listing labels its 2019 entry Growth; Google News "
                  "carries no round of the company, and no valuation is on record: below $1B."))

L.append(cls("blue-jeans-network", status="acquired", rng="below_1b", country="US", city="San Jose",
             city_src="web_verified", stage="undetermined", entry_date="2011", focus="SaaS",
             note="BlueJeans Network, cloud video conferencing, headquartered at Santana Row, San Jose (Wikipedia), as "
                  "in the Accel row; acquired by Verizon in 2020, which shut the service in 2023-24. Wikipedia: it had "
                  "$23.5M from Accel, NEA and Norwest before its June 2011 launch, and NEA's first-investment year is "
                  "2011; no source read ties NEA to a named round.",
             rounds=[rnd("2011", None, 23500000, None, True, W("BlueJeans"), "press")]))

BLUEFISH_POST = POST("bluefish-the-ai-marketing-platform-for-the-agentic-era")
BLUEFISH_B = NEWS("bluefish-ai", "Bluefish Raises $43 Million Series B to Power")
L.append(cls("bluefish-ai", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=BLUEFISH_POST,
             entry_date="2025-08-20", focus="SaaS",
             note="Bluefish, marketing platform that measures and shapes how brands appear in AI answer engines (New "
                  "York, its release dateline). The firm's own post (2025-08-20) announces 'our Series A investment in "
                  "Bluefish' ($20M, AdExchanger), the firm's first-investment year. Threshold Ventures and NEA co-led the "
                  "$43M Series B (PR Newswire, 2026-04-14), $68M raised in total; no valuation disclosed. Momentum check "
                  "2026-09-30 (Google News, 'Bluefish AI raises'): no $1B+ round, below $1B.",
             rounds=[rnd("2025-08-20", "Series A", 20000000, None, True, BLUEFISH_POST, "firm"),
                     rnd("2026-04-14", "Series B", 43000000, "Threshold Ventures; NEA", True, BLUEFISH_B, "company")]))

BLUESHIFT_C = "https://venturebeat.com/business/blueshift-raises-30-million-to-manage-and-analyze-customer-data"
L.append(cls("blueshift", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("blueshift"), entry_date="2014", grad="graduated", grad_src="web_verified",
             grad_conf="high", grad_cite=BLUESHIFT_C, focus="SaaS",
             note="Blueshift, AI-driven customer data and marketing automation platform (San Francisco). The firm's own "
                  "listing labels its 2014 first investment Seed. VentureBeat (2021-02-24): a $30M Series C led by Fort "
                  "Ross Ventures and Avatar Growth Capital, $65M raised in total; a later round named Series C, so the "
                  "row graduated. A $40M debt facility from Runway Growth followed in January 2024 (TechCrunch); no "
                  "valuation on record, below $1B.",
             rounds=[rnd("2014", "Seed", None, None, True, SITE("blueshift"), "firm"),
                     rnd("2021-02-24", "Series C", 30000000, "Fort Ross Ventures; Avatar Growth Capital", False,
                         BLUESHIFT_C, "press")]))

BOKU_W = W("Boku, Inc.")
L.append(cls("boku", status="public", rng="below_1b", country="GB", country_src="web_verified", country_cite=BOKU_W,
             city="London", city_src="web_verified", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=BOKU_W, entry_date="2011", focus="Fintech & Payments",
             note="Boku, carrier billing and mobile payment methods, listed on London's AIM (BOKU). Wikipedia: Boku is "
                  "headquartered in London, and its releases now carry London datelines; the a16z, Benchmark and Khosla "
                  "rows read San Francisco, US (its home before the listing), so they should align. Wikipedia: after a "
                  "$13M Series A (Khosla, Index, Benchmark) and DAG's $25M round in 2010, Boku raised $35M 'led by NEA "
                  "and existing venture capital investors' (reported for 2012); the firm's own listing labels its 2011 "
                  "entry Growth, which agrees, and the firm's year stands as the entry year. AIM market cap in the "
                  "GBP 450-700M range per the Benchmark row's check: below $1B.",
             rounds=[rnd("2009", "Series A", 13000000, None, False, BOKU_W, "press"),
                     rnd("2010", "Series C", 25000000, "DAG Ventures", False, BOKU_W, "press"),
                     rnd("2012", "Series C", 35000000, "NEA", True, BOKU_W, "press")]))

BONSAI_A = NEWS("bonsai", "Bonsai AI raises $7.6m")
BONSAI_MS = NEWS("bonsai", "Microsoft just bought a startup it invested in")
L.append(cls("bonsai", status="acquired", rng="below_1b", country="US", city="Berkeley", city_src="web_verified",
             stage="undetermined", entry_date="2014", focus="AI & Applied AI",
             note="Bonsai, a platform for building and training industrial AI models (Berkeley CA, Electronics Weekly). "
                  "Microsoft, an investor, bought it in June 2018 (Business Insider headline). Electronics Weekly "
                  "(2017-05): a $7.6M round with Microsoft Ventures, NEA, ABB, Samsung NEXT and Siemens, $13.6M raised in "
                  "total; NEA's first-investment year is 2014 and no source read names the earlier $6M or ties NEA to "
                  "it. The Y Combinator row named Bonsai is a different company (freelancer software).",
             rounds=[rnd(None, None, 6000000, None, None, BONSAI_A, "press"),
                     rnd("2017-05", None, 7600000, "Microsoft Ventures", True, BONSAI_A, "press")]))

LSVP_BRALE = "https://lsvp.com/company/brale/"
L.append(cls("brale", status="private", rng="below_1b", country="US", city="Des Moines", stage="Seed",
             stage_src="first_party", stage_conf="medium", stage_cite=SITE("brale"), entry_date="2022",
             grad="graduated", grad_src="web_verified", grad_conf="medium", grad_cite=LSVP_BRALE,
             focus="Crypto & Web3",
             note="Brale, regulated fiat-backed stablecoin issuance platform (Des Moines, as in the Lightspeed row). The "
                  "firm's own listing labels its 2022 first investment Seed, with Scott Sandell on the board. "
                  "Lightspeed's own company page records its entry in Brale's Series A in 2025, a later round named "
                  "Series A, so the row graduated. No valuation on record; below $1B.",
             rounds=[rnd("2022", "Seed", None, None, True, SITE("brale"), "firm"),
                     rnd("2025", "Series A", None, None, None, LSVP_BRALE, "firm")]))

BNTO_A = NEWS("bnto", "Secures $15 Million in Series A Funding")
L.append(cls("bnto", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("bnto"), entry_date="2021", grad="graduated",
             grad_src="web_verified", grad_conf="medium", grad_cite=BNTO_A, focus="Consumer & Marketplaces",
             flags=["city_unknown"],
             note="BNTO, AI-driven fashion subscription across rental, resale and new (bnto.com). The firm's own listing "
                  "labels its 2021 first investment Seed (Carmen Chang). WWD headline (2025-10-13): 'BNTO Launches AI "
                  "Styling Agent and Secures $15 Million in Series A Funding', a later round named Series A (body "
                  "paywalled), so the row graduated. No valuation disclosed. Neither the site nor the visible coverage "
                  "states a headquarters city.",
             rounds=[rnd("2021", "Seed", None, None, True, SITE("bnto"), "firm"),
                     rnd("2025-10-13", "Series A", 15000000, None, None, BNTO_A, "press")]))

L.append(cls("boxc", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("boxc"), entry_date="2014", focus="SaaS",
             flags=["city_unknown"],
             note="BoxC, API-first cross-border e-commerce logistics platform (boxc.com, still live). The firm's own "
                  "listing labels its 2014 first investment Seed. Google News carries no round of the company and its "
                  "site states no headquarters city. " + GRAD_LEFT))

BR_F = ("https://www.prnewswire.com/news-releases/bloomreach-valuation-soars-to-2-2-billion-following-175-million-"
        "investment-led-by-goldman-sachs-asset-management-301488094.html")
L.append(cls("bloomreach", status="private", rng="1b_plus", usd=2200000000, val_src="web_verified", val_cite=BR_F,
             asof="2022-02-23", extra=VW, country="US", city="Mountain View", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2012", focus="SaaS", flags=["stale"],
             note="Bloomreach, commerce search and marketing platform (Mountain View). Mark: the $175M round led by "
                  "Goldman Sachs Asset Management at a $2.2B valuation (its release, 2022-02-23), stale beyond 24 months; "
                  "no newer priced round found, as in the Bain Capital Ventures and Lightspeed rows. Stage: Lightspeed's "
                  "own page records its entry at the Series B in 2010, and NEA's first investment is 2012, so NEA came in "
                  "at a later round, Growth; no source read names it (the firm's 2012 post on 'SaaS 3.0' features the "
                  "company).",
             rounds=[rnd("2022-02-23", "Series F", 175000000, "Goldman Sachs Asset Management", None, BR_F, "company")]))

BRANCH_F = NEWS("branch", "BRANCH RAISES $300 MILLION AT $4 BILLION")
BRANCH_W = W("Branch (company)")
L.append(cls("branch", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified", val_cite=BRANCH_F,
             asof="2022-02-10", extra=VW, city="Mountain View", city_src="web_verified", stage="Seed",
             stage_src="web_verified", stage_conf="high", stage_cite=BRANCH_F, entry_date="2014-09",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=BRANCH_W,
             focus="SaaS", flags=["stale", "stage_disputes_band"],
             note="Branch Metrics, mobile deep linking and attribution (Mountain View per Wikipedia; its 2022 release and "
                  "Form D give Palo Alto). NEA's Scott Sandell in the company's release (2022-02-10): 'Since the day I "
                  "met Alex, Mike, Mada and Dmitri during the seed investment'; Wikipedia dates that round, a $3M round "
                  "led by NEA, to September 2014, the firm's first-investment year. The Form D band's Series A entry "
                  "(2015) read the next round, disputed. Wikipedia: a $15M Series A in February 2015 followed, so the "
                  "row graduated. Mark: the $300M Series F led by NEA at a $4B valuation (2022-02-10), stale beyond 24 "
                  "months. The 8VC and a16z rows named Branch are Branch International, a different company (emerging-"
                  "market lending).",
             rounds=[rnd("2014-09", "Seed", 3000000, "NEA", True, BRANCH_F, "company"),
                     rnd("2015-02", "Series A", 15000000, None, True, BRANCH_W, "press"),
                     rnd("2022-02-10", "Series F", 300000000, "NEA", True, BRANCH_F, "company")]))

BAIHE_FOSUN = NEWS("baihe", "Fosun Group Owner Plans $631 Million")
L.append(cls("baihe", status="acquired", rng="below_1b", country="CN", country_src="web_verified",
             country_cite=BAIHE_FOSUN, city="Beijing", stage="undetermined", entry_date="2006",
             focus="Consumer & Marketplaces",
             note="Baihe (baihe.com), Chinese online dating and matchmaking, Beijing; it absorbed Jiayuan in 2015 and "
                  "traded on China's New Third Board. In May 2018 Fosun chairman Guo Guangchang agreed to take about 70% "
                  "of it through Yuanhong Investment (Global Dating Insights, 2018-05-04), a change of control read with "
                  "the firm's exit line ('Acquired by Shanghai Huanzhuo') as acquired. NEA's first investment is 2006; "
                  "no source read names the round.",
             rounds=[]))

L.append(cls("barkly", status="acquired", rng="below_1b", city="Boston", city_src="formd_address", focus="Security",
             note="Barkly, endpoint protection (Boston, the Form D address). Alert Logic acquired it in 2019; barkly.com "
                  "now redirects to LevelBlue's 'Alert Logic is now LevelBlue' page. The Form D band's Series A entry "
                  "(2015, Harry Weller a director) stands."))

L.append(cls("braincells-inc", status="unknown", rng="below_1b", city="San Diego", city_src="formd_address",
             focus="Healthcare & Bio",
             note="BrainCells Inc., San Diego (Form D address), repositioning compounds for central nervous system "
                  "diseases; the firm listed it only in its 2013 archive. Its last Form D is dated 2011-12-29 ($4.1M "
                  "sold of $9M); Google News carries nothing on the company, so its fate is not established. The Pre-Seed "
                  "entry on file rests on a $135K 2009 filing of a company that was already venture-backed; a later "
                  "pass should check its round history."))

L.append(cls("berkshire-grey", country="US", city="Bedford", stage="undetermined", entry_date="2016",
             rng="below_1b", focus="Industrial & Robotics",
             note="Berkshire Grey, AI robotic fulfillment (Bedford MA, Boston Globe 2023-03-24). Listed through the RAAC "
                  "SPAC in July 2021, then taken private by SoftBank, which completed the purchase of the shares it did "
                  "not own in July 2023. NEA 15 and NEA Ventures 2016 held 17.2% at the merger (8-K, 2021-07-27) and the "
                  "firm's first-investment year is 2016; no source read names the round NEA entered (Khosla seeded it "
                  "in 2013).",
             rounds=[]))

BT_WSJ = NEWS("braintree", "Braintree Raises $35 Million to Tackle")
L.append(cls("braintree", status="acquired", rng="below_1b", city="Chicago", stage="Growth", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("braintree"), entry_date="2012", focus="Fintech & Payments",
             note="Braintree, online and mobile payments (Chicago). The firm's own listing labels its 2012 entry Growth, "
                  "which agrees with the record: Accel led the $34M first round in 2011 (the Accel row) and Braintree "
                  "raised $35M in October 2012 (WSJ, 2012-10-17), NEA's round (Rick Yang). eBay's PayPal bought it for "
                  "$800M in September 2013 (the firm's own post, 2013-09-26).",
             rounds=[rnd("2012-10-17", None, 35000000, None, True, BT_WSJ, "press")]))

BWP_END = NEWS("boulder-wind-power", "Boulder Wind Power winds down operations")
L.append(cls("boulder-wind-power", status="defunct", rng="below_1b", city="Boulder", city_src="formd_address",
             focus="Climate & Energy",
             note="Boulder Wind Power, direct-drive wind turbine generators (Boulder, the Form D address); it wound down "
                  "operations in October 2014 (Wind Power Monthly, 2014-10-30). The Form D band's Series A entry (2009, "
                  "Harry Weller and Ravi Viswanathan directors) stands."))

BI_C = "https://www.securityweek.com/beyond-identity-becomes-unicorn-100-million-series-c-funding-round/"
L.append(cls("beyond-identity", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified", val_cite=BI_C,
             asof="2022-02-22", extra=VW, city="New York", city_src="formd_address", focus="Security",
             flags=["stale"],
             note="Beyond Identity, passwordless phishing-resistant authentication (New York, the Form D address). Mark: "
                  "the $100M Series C led by Evolution Equity Partners at a $1.1B valuation (SecurityWeek, 2022-02-22), "
                  "stale beyond 24 months; no later priced round found. The Form D band's Series A entry agrees with the "
                  "firm's own post (2020-04-14): NEA led the Series A with co-lead KDT.",
             rounds=[rnd("2020-04-14", "Series A", 30000000, "NEA; KDT", True, POST("beyond-identity-the-end"), "firm"),
                     rnd("2022-02-22", "Series C", 100000000, "Evolution Equity Partners", None, BI_C, "press")]))

L.append(cls("blockcypher", status="private", rng="below_1b", country="US", city="Redwood City", stage="Seed",
             stage_src="first_party", stage_conf="medium", stage_cite=SITE("blockcypher"), entry_date="2014",
             focus="Crypto & Web3",
             note="BlockCypher, blockchain web services and developer APIs (Redwood City). The firm's own listing labels "
                  "its 2014 first investment Seed. Google News shows the company operating (2015, 2018) but no later "
                  "round. " + GRAD_LEFT))

L.append(cls("bedrocket-media-sportsrocket", status="unknown", rng="below_1b", city="New York",
             city_src="formd_address", focus="Media, Gaming & Advertising",
             note="BedRocket Media, later SportsRocket, digital sports video networks and an OTT platform (New York, the "
                  "Form D address). Coverage runs to 2017 (Sportsrocket Turbine, Sports Video Group and Forbes) and its "
                  "last Form D is from 2018; sportsrocket.com now serves an empty page and the firm lists the investment "
                  "as Past, so its fate is not established. The Form D band's Series A entry (2012, Patrick Kerins a "
                  "director) stands."))

import os
if not os.environ.get("C2_DRY"):
    jl.write("c2a", L)
