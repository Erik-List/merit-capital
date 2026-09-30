"""Judge c4, batch 8 (queue batch-008): listed NEA members, classification only."""
import judge_lib as jl

W, SITE, POST, NEWS, FTS, rnd = jl.W, jl.SITE, jl.POST, jl.NEWS, jl.FTS, jl.rnd
GP = "Graduation left for the graduation pass."
L = []


def c(slug, **k):
    L.append(jl.cls(slug, **k))


# ---- evident-id
c("evident-id", status="private", rng="below_1b", city="Atlanta", focus="Security",
  stage="undetermined", entry_date="2017",
  rounds=[rnd("2016", None, 1500000, None, None, None, "filing"),
          rnd("2017", None, 8958933, None, None, None, "filing"),
          rnd("2019", None, 20102416, None, True, None, "filing"),
          rnd("2022-09", None, 14000000, None, None, NEWS("evident-id", "raises $14M"), "press")],
  note="Atlanta identity and credential verification company, still raising ($14M in September 2022). The firm's "
       "own first-invested year is 2017, the year of the $9M Form D round, so the entry date is 2017 rather than the "
       "2019 filing on which Vanessa Larco sits; no record names the round.")

# ---- exent-technologies
EXC = ("https://corporate.comcast.com/news-information/news-feed/comcast-takes-gaming-up-a-level-with-new-games-on-"
       "demand-solution-from-exent-technologies-available-on-comcastnet")
c("exent-technologies", country="IL", country_src="web_verified", country_cite=EXC, city="Petah Tikva",
  rng="below_1b", focus="Media, Gaming & Advertising", flags=["country_conflict"],
  stage="undetermined", entry_date="2000", rounds=[],
  note="Games-on-demand software (GameTanium) developed in Israel; its 2004 Comcast release gives offices in "
       "Bethesda, Maryland and Tel Aviv, and company profiles give Petah Tikva as the headquarters. The prefilled "
       "acquired status was not confirmed by any source read; the firm lists it private. The 2000 round is not named.")

# ---- expanse (fka Qadium; base also carries qadium)
c("expanse", status="acquired", rng="below_1b", city="San Francisco", focus="Security",
  note="Internet attack-surface company (formerly Qadium), acquired by Palo Alto Networks in 2020 (the firm's exit "
       "line; the IVP book agrees). The firm's first-invested year is 2016, earlier than the 2019 Form D anchor. "
       "The base also carries qadium, the same company.")

# ---- expel
c("expel", status="private", rng="below_1b", country="US", city="Herndon", focus="Security",
  stage="Series A", stage_src="model", stage_conf="medium", entry_date="2016-09",
  rounds=[rnd("2016-09", "Series A", 7500000, "Paladin Capital Group", None,
              NEWS("expel", "Raises $20M Series B"), "press"),
          rnd("2018-04", "Series B", 20000000, "Scale Venture Partners", True,
              NEWS("expel", "Raises $20M Series B"), "press"),
          rnd("2021-11", "Series E", 140300000, "CapitalG; Paladin Capital Group", None,
              NEWS("expel", "Series E, cyber firm Expel"), "press")],
  note="The firm's first-invested year 2016 is the year of the $7.5M Series A Paladin led (September 2016); the "
       "Series B coverage names NEA among the backers but not as new. The $140M Series E of November 2021 was "
       "called a unicorn round with no valuation disclosed, so under Rule A the row stays below $1B, as in the "
       "Battery book. Herndon, Virginia.")

# ---- exploramed-iv
c("exploramed-iv", status="unknown", rng="below_1b", city="Mountain View", focus="Healthcare & Bio",
  note="The fourth ExploraMed medical-device incubator entity (2011 Form D, $8M, NEA partners as directors); the "
       "firm listed it only in 2013 and its current state could not be established. An incubator vehicle may be "
       "fund-shaped under D5; flagged for review.")

# ---- exploramed-v
c("exploramed-v", status="private", rng="below_1b", city="Mountain View", focus="Healthcare & Bio",
  note="The fifth ExploraMed medical-device incubator (2017 Form D, $8.8M); the firm lists it as a current private "
       "holding. An incubator vehicle may be fund-shaped under D5; flagged for review.")

# ---- fabfitfun
c("fabfitfun", status="private", rng="below_1b", country="US", city="Los Angeles", focus="Consumer & Marketplaces",
  stage="Seed", stage_src="first_party", stage_cite=SITE("fabfitfun"), stage_conf="medium", entry_date="2015",
  grad="graduated", grad_src="web_verified", grad_cite=NEWS("fabfitfun", "Raised $80 Million"), grad_conf="medium",
  rounds=[rnd("2015", "Seed", None, None, True, SITE("fabfitfun"), "firm"),
          rnd("2019-02", None, 80000000, None, None, NEWS("fabfitfun", "Raised $80 Million"), "press")],
  note="The firm's listing labels its 2015 entry Seed. FabFitFun raised $80M in February 2019 (Forbes headline; "
       "the paywalled body was not read), far above the $8M bar for a 2015 seed, so the row graduated. Los Angeles "
       "subscription-box company, still private and acquiring (Boox, 2025).")

# ---- fabric8labs
c("fabric8labs", status="private", rng="below_1b", city="San Diego", focus="Industrial & Robotics",
  note="Electrochemical metal additive manufacturing, San Diego; still raising (a $56.5M Form D in 2026) with no "
       "published valuation.")

# ---- factory: the EE country is a Wikidata join on a one-word name
c("factory", status="private", country="US", city="San Francisco", focus="AI & Applied AI",
  rng="1b_plus", usd=5000000000, val_src="web_verified",
  val_cite=NEWS("factory", "raises $200M at a $5B valuation for its AI coding"), asof="2026-09-15",
  extra={"valuation_range_source": "web_verified"}, flags=["model_disputes_source"],
  stage="Growth", stage_src="first_party", stage_cite=POST("factory-the-platform"), stage_conf="high",
  entry_date="2025-09",
  rounds=[rnd("2025-09", "Series B", 50000000, "New Enterprise Associates", True, POST("factory-the-platform"),
              "firm"),
          rnd("2026-09-15", None, 200000000, "Blackstone; Khosla Ventures; Sequoia Capital", True,
              NEWS("factory", "raises $200M at a $5B valuation for its AI coding"), "press")],
  note="The firm's own September 2025 post announces the $50M Series B NEA led, its first investment; entry at "
       "Growth. Momentum check 2026-09-30: the $200M round of September 2026 at $5B (The Next Web) is the mark, as "
       "in the 20VC, Khosla, Lux and Sequoia books. The Estonian country was a namesake join; San Francisco.")

# ---- fanhattan
c("fanhattan", status="acquired", rng="below_1b", city="San Mateo", focus="Media, Gaming & Advertising",
  stage="undetermined", rounds=[rnd("2014-03", None, 17997227, None, True, None, "filing")],
  note="Entertainment discovery app and Fan TV box, bought by Rovi in November 2014 (" +
       NEWS("fanhattan", "Rovi Buys Fanhattan") + "). The firm's first-invested year 2007 predates the 2010 "
       "company, and no record names NEA's round.")

# ---- fenris-creations (CCP Games; base also carries ccp-games)
c("fenris-creations", status="private", rng="below_1b", city="Reykjavik", focus="Media, Gaming & Advertising",
  stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015",
  note="Fenris Creations is CCP Games (EVE Online), independent again in 2026 after Pearl Abyss's 2018 purchase; "
       "the firm's own post says it first partnered with CCP in 2015 and backs the new studio. NEA led CCP's $30M "
       "round of 2015, long after the company's early rounds, so Growth. The base also carries ccp-games, the same "
       "company.")

# ---- fibex
c("fibex", status="acquired", rng="below_1b", country="US", city="Petaluma", focus="Data Infrastructure",
  stage="undetermined", entry_date="1997", rounds=[],
  note="Fibex Systems, telecom access equipment from Petaluma, acquired by Cisco in 1999 (the firm's exit line). "
       "The 1997 round is not named in any record.")

# ---- fiftythree
c("fiftythree", status="acquired", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
  note="Maker of the Paper app and Pencil stylus; WeTransfer acquired its assets and patents in August 2018 "
       "(Wikipedia). NEA led the $30M Series B of March 2015. New York, as in the a16z book.")

# ---- fightcamp
c("fightcamp", status="private", rng="below_1b", country="US", city="Newport Beach", focus="Consumer & Marketplaces",
  stage="Growth", stage_src="first_party", stage_cite=SITE("fightcamp"), stage_conf="medium", entry_date="2021",
  rounds=[rnd("2021-06", "Series B", 90000000, "IVP", None, NEWS("fightcamp", "Connected Fitness Boxing Startup"),
              "press")],
  note="The firm's listing labels its 2021 entry Growth, the year of the $90M Series B IVP led. Newport Beach, as in "
       "the IVP book.")

# ---- financial-engines
c("financial-engines", country="US", city="Sunnyvale", rng="below_1b", focus="Fintech & Payments",
  stage="undetermined", entry_date="1997", rounds=[],
  note="Online investment advice, listed in 2010 and taken private by Hellman & Friedman in 2018 (its EDGAR "
       "deregistration). Dick Kramlich joined the board in January 1997, but no record names that round.")

# ---- financial-software-systems
c("financial-software-systems", status="private", rng="below_1b", country="IN", country_src="web_verified",
  country_cite=SITE("financial-software-systems"), city="Chennai", focus="Fintech & Payments",
  stage="Growth", stage_src="first_party", stage_cite=SITE("financial-software-systems"), stage_conf="medium",
  entry_date="2010",
  note="FSS, the Chennai payment-processing company the firm calls India's largest; its listing labels the 2010 "
       "entry Growth.")

# ---- fineground-networks
c("fineground-networks", status="acquired", rng="below_1b", country="US", city="Campbell", focus="Data Infrastructure",
  stage="undetermined", entry_date="2000", rounds=[],
  note="Web application acceleration, acquired by Cisco in 2005 (the firm's exit line). The 2000 round is not "
       "named in any record.")

# ---- fire1
c("fire1", status="private", rng="below_1b", country="IE", country_src="web_verified",
  country_cite=NEWS("fire1", "Irish company Fire1"), city="Dublin", focus="Healthcare & Bio",
  stage="undetermined", entry_date="2013",
  rounds=[rnd("2025-01", None, 120000000, None, None, NEWS("fire1", "Irish company Fire1"), "press")],
  note="Irish heart-failure monitoring implant company, founded 2013 out of The Foundry; raised $120M in January "
       "2025 with no published valuation. The round NEA entered in 2013 is not named.")

# ---- firebase: the prefilled defunct is the acquisition read as a dissolution
c("firebase", status="acquired", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
  flags=["model_disputes_source"],
  stage="Seed", stage_src="web_verified", stage_cite=W("Firebase"), stage_conf="high", entry_date="2012-05",
  grad="graduated", grad_src="web_verified", grad_cite=W("Firebase"), grad_conf="high",
  rounds=[rnd("2012-05", "Seed", 1100000, None, True, W("Firebase"), "press"),
          rnd("2013-06", "Series A", 5600000, "Union Square Ventures", False, W("Firebase"), "press")],
  note="NEA joined the $1.1M seed of May 2012 (the firm's label reads Seed too); the $5.6M Series A of June 2013 "
       "graduates it. Acquired by Google in October 2014, so the prefilled defunct is disputed; the USV book agrees.")

# ---- firestorm
c("firestorm", status="private", rng="below_1b", city="San Diego", focus="Industrial & Robotics",
  note="Firestorm Labs, San Diego maker of 3D-printed military drones; its Form D filings run to a $75M round in "
       "2026 with no published valuation.")

# ---- firstcry
FCM = "https://stockanalysis.com/quote/nse/FIRSTCRY/market-cap/"
c("firstcry", status="public", country="IN", country_src="web_verified", country_cite=W("FirstCry"), city="Pune",
  focus="Consumer & Marketplaces", rng="below_1b", usd=980227714, val_src="web_verified", val_cite=FCM,
  asof="2026-09-30", extra={"valuation_range_source": "web_verified"},
  stage="Growth", stage_src="web_verified", stage_cite=W("FirstCry"), stage_conf="high", entry_date="2015-04",
  rounds=[rnd("2011-04", None, 4000000, "SAIF Partners", False, W("FirstCry"), "press"),
          rnd("2012-02", None, 14000000, None, False, W("FirstCry"), "press"),
          rnd("2015-04", "Series D", 36000000, None, True, W("FirstCry"), "press")],
  note="Brainbees Solutions (FirstCry), Pune, listed on the NSE and BSE in August 2024; NEA came in at the $36M "
       "Series D of April 2015. Market cap INR 93.94B on 2026-09-30 (stockanalysis) @ ECB 2026-09-30 (INR/EUR "
       "108.8205, EUR/USD 1.1355) = $980.2M, within 5% of the $1B edge.")

# ---- fiscalnote
FNM = "https://stockanalysis.com/quote/otc/NOTE/market-cap/"
c("fiscalnote", status="public", city="Washington", focus="SaaS",
  rng="below_1b", usd=910990, val_src="web_verified", val_cite=FNM, asof="2026-09-30",
  extra={"valuation_range_source": "web_verified"},
  stage="Seed", stage_src="web_verified", stage_cite=W("FiscalNote"), stage_conf="high", entry_date="2013",
  grad="graduated", grad_src="web_verified", grad_cite=W("FiscalNote"), grad_conf="high",
  rounds=[rnd("2013", "Seed", 1300000, None, True, W("FiscalNote"), "press"),
          rnd("2014", None, 7000000, None, True, W("FiscalNote"), "press"),
          rnd("2015-02", None, 10000000, None, None, W("FiscalNote"), "press")],
  note="NEA joined the $1.3M 2013 seed after Mark Cuban's first check; the $7M first institutional round of fall "
       "2014 clears the $5M bar, so the row graduated. Delisted from the NYSE in March 2026 and trading OTC; market "
       "cap $0.91M on 2026-09-30 (stockanalysis).")

# ---- fisker-automotive
c("fisker-automotive", status="acquired", rng="below_1b", city="Anaheim", focus="Climate & Energy",
  note="Filed for Chapter 11 in November 2013; its assets were sold at auction in 2014 to Hybrid Technology "
       "(Wanxiang), whose holding company became Karma Automotive (Wikipedia), so it reads acquired out of "
       "insolvency.")

# ---- fizz: the known acquired and GB are namesake joins
c("fizz", status="private", country="US", city="Palo Alto", rng="below_1b", focus="Consumer & Marketplaces",
  flags=["model_disputes_source"], stage="Series A", stage_src="model", stage_conf="medium", entry_date="2022-11",
  rounds=[rnd("2022-11", "Series A", 12000000, None, True, None, "press")],
  note="The anonymous college social app is operating (Saudi launch in April 2026, " +
       NEWS("fizz", "Saudi Arabia Debut") + "), so the prefilled acquired status and British country are "
       "namesake joins. NEA's 2022 entry is the $12M Series A of November 2022 (the Lightspeed book records it; "
       "Rick Yang holds the board seat). The Cherry row named Fizz is the New York card company, another firm.")

# ---- flow
c("flow", city="Hoboken", city_src="formd_address", rng="below_1b", focus="SaaS",
  note="Flow Commerce (flow.io), cross-border e-commerce software, acquired by Global-e (the firm's exit line); "
       "Hoboken is its Form D address. The a16z, Lightspeed and YC rows named Flow are other companies.")

# ---- flox
FLX = NEWS("flox", "Flox raises $27M")
c("flox", status="private", rng="below_1b", country="US", city="New York", focus="DevTools & APIs",
  stage="Series A", stage_src="web_verified", stage_cite=FLX, stage_conf="high", entry_date="2023-02",
  rounds=[rnd("2023-02", "Series A", 16500000, "New Enterprise Associates", True, FLX, "press"),
          rnd("2025-09", "Series B", 25000000, None, None, NEWS("flox", "Series B Raised"), "press")],
  note="NEA led the $16.5M Series A of February 2023 (TechCrunch), the firm's own first-invested year. Momentum "
       "check 2026-09-30: the latest round is the $25M Series B of September 2025, no valuation near $1B.")

# ---- folloze
c("folloze", status="private", rng="below_1b", city="Palo Alto", city_src="formd_address", focus="SaaS",
  stage="undetermined", entry_date="2013",
  rounds=[rnd("2013", None, 3500000, None, None, None, "filing"),
          rnd("2016-09", None, 7300000, None, True, NEWS("folloze", "raises $7.3M"), "press")],
  note="B2B buyer-experience software, still operating (2025 releases). The firm's first-invested year is 2013, "
       "the year of the $3.5M Form D round, not the 2016 filing on which Chetan Puttagunta sits; no record names "
       "the round.")

# ---- forallsecure
c("forallsecure", status="private", rng="below_1b", city="Pittsburgh", focus="Security",
  note="Pittsburgh application-security testing company (Mayhem); raised $21M in 2022 and filed a small round in "
       "2024, no valuation near $1B.")

# ---- force10
c("force10", city="San Jose", rng="below_1b",
  focus="Data Infrastructure",
  note="Force10 Networks, San Jose Ethernet switching, acquired by Dell in 2011. The firm's first-invested year is "
       "1999 and the S-1 shows NEA VIII, 8A and 9 holdings, so the 2009 Form D anchor is a later round.")

# ---- foresight
FSC = "https://finance.yahoo.com/news/foresight-raises-5-5m-seed-110700593.html"
c("foresight", status="private", rng="below_1b", country="US", city="New York", focus="Data Infrastructure",
  stage="Seed", stage_src="web_verified", stage_cite=FSC, stage_conf="high", entry_date="2025-06-26",
  grad="censored",
  rounds=[rnd("2025-06-26", "Seed", 5500000, "New Enterprise Associates", True, FSC, "press")],
  note="NEA led the $5.5M seed of June 2025 (Madison Faulkner to the board); New York. Censored: the entry is "
       "inside 24 months. Momentum check 2026-09-30: no later round found. The Creandum row named Foresight is a "
       "London infrastructure company, and the YC Spring 2026 Foresight is not shown to be this one.")

# ---- forethought: Zendesk bought it in March 2026
c("forethought", status="acquired", rng="below_1b", city="San Francisco", focus="AI & Applied AI",
  note="AI customer-support agents; acquired by Zendesk in March 2026 (" + W("Forethought Technologies") + "; the "
       "firm's exit line agrees), fresher than the 8VC book's private. NEA led the $9M Series A of December 2018.")

# ---- formlabs: the Series A band is disputed by the documented 2018 round
c("formlabs", city="Somerville", focus="Industrial & Robotics",
  stage="Growth", stage_src="web_verified", stage_cite=W("Formlabs"), stage_conf="high", entry_date="2018-08",
  flags=["stage_disputes_band"],
  rounds=[rnd("2013-10", "Series A", 19000000, "DFJ Growth", False, W("Formlabs"), "press"),
          rnd("2016-08", "Series B", 35000000, "Foundry Group", False, W("Formlabs"), "press"),
          rnd("2018-04", "Series C", 30000000, "Tyche Partners", False, W("Formlabs"), "press"),
          rnd("2018-08", None, 15000000, "New Enterprise Associates", True, W("Formlabs"), "press"),
          rnd("2021-05", "Series E", 150000000, "SoftBank Vision Fund 2", None, W("Formlabs"), "press")],
  note="NEA's first money is the $15M of August 2018 that valued Formlabs above $1B, after its Series A, B and C "
       "(Wikipedia), so the entry is Growth, not the Series A the Form D band read. Somerville.")

# ---- forter
c("forter", city="New York", focus="Security",
  stage="Growth", stage_src="first_party", stage_cite=POST("forter-the-new-force"), stage_conf="high",
  entry_date="2014",
  rounds=[rnd("2014", "Series B", None, "New Enterprise Associates", True, POST("forter-the-new-force"), "firm"),
          rnd("2016-04", "Series C", 32000000, None, True, POST("forter-the-new-force"), "firm")],
  note="The firm's own 2016 post: 'We initially partnered with Forter in 2014, leading their Series B financing'; "
       "entry at Growth. New York, as in the Tiger Global book.")

# ---- foundry-therapeutics-1
c("foundry-therapeutics-1", status="private", rng="below_1b", city="Menlo Park", focus="Healthcare & Bio",
  stage="undetermined", entry_date="2018",
  note="A therapeutics vehicle of The Foundry, the Menlo Park medical-device incubator (Form D filings 2019-20 with "
       "Josh Makower and Tak Cheung as directors). No record names the round; an incubator vehicle may be "
       "fund-shaped under D5, flagged for review.")

# ---- fox-hollow-technologies
c("fox-hollow-technologies", status="acquired", rng="below_1b", country="US", city="Redwood City",
  focus="Healthcare & Bio", stage="undetermined", entry_date="1998", rounds=[],
  note="FoxHollow Technologies, atherectomy devices, listed in 2004 and acquired by ev3 in October 2007 (its "
       "delisting on EDGAR). Ryan Drant joined the board in February 1998; the round is not named.")

# ---- framebridge
c("framebridge", status="acquired", rng="below_1b", city="Washington", focus="Consumer & Marketplaces",
  note="Custom framing, Washington, D.C.; acquired by Graham Holdings in May 2020 (Wikipedia).")

# ---- frontier-car-group
FCG = NEWS("frontier-car-group", "OLX Group invests up to $400M")
c("frontier-car-group", status="acquired", rng="below_1b", country="DE", country_src="web_verified",
  country_cite=FCG, city="Berlin", focus="Consumer & Marketplaces", stage="undetermined", entry_date="2016",
  rounds=[rnd("2018-05", None, 58000000, None, None, FCG, "press"),
          rnd("2019-11", None, 400000000, "OLX Group", None, FCG, "press")],
  note="Berlin used-car marketplace group; OLX put up to $400M in at $700M in November 2019 (TechCrunch) and folded "
       "it into OLX Autos in 2020, as the Balderton book reads. NEA's 2016 round is not named.")

# ---- ftx
c("ftx", status="defunct", rng="below_1b", country="BS", country_src="web_verified", country_cite=W("FTX"),
  city="Nassau", focus="Crypto & Web3",
  stage="Growth", stage_src="first_party", stage_cite=SITE("ftx"), stage_conf="medium", entry_date="2021",
  note="The crypto exchange, headquartered in the Bahamas, in Chapter 11 since November 2022 (Wikipedia); aligned "
       "with the seven other books. The firm's listing labels its 2021 entry Growth.")

# ---- ftx-us
c("ftx-us", status="defunct", rng="below_1b", country="US", city="Miami", focus="Crypto & Web3",
  stage="Growth", stage_src="first_party", stage_cite=SITE("ftx-us"), stage_conf="medium", entry_date="2021",
  note="FTX's US exchange (West Realm Shires), in the same November 2022 bankruptcy; it had moved its head office "
       "from Chicago to Miami. The firm labels its 2021 entry Growth; the $400M Series A of January 2022 was the "
       "company's first own fundraise and its published investor lists do not name NEA.")

# ---- fugue
c("fugue", status="acquired", rng="below_1b", city="Frederick", focus="Security",
  note="Cloud security company (formerly Luminal) from Frederick, Maryland, acquired by Snyk in 2022 (the firm's "
       "exit line). The firm's first-invested year is 2014, earlier than the 2016 Form D anchor.")

# ---- fulcrum-microsystems
c("fulcrum-microsystems", status="acquired", rng="below_1b", country="US", city="Calabasas",
  focus="Industrial & Robotics", stage="undetermined", entry_date="2001",
  rounds=[rnd("2010-03", None, 15040000, None, True, None, "filing")],
  note="Ethernet switch chips, acquired by Intel in 2011 (the firm's exit line). The firm's first-invested year is "
       "2001; the 2010 Form D is a later round, and no record names the entry round.")

# ---- functional-finance
FFP = NEWS("functional-finance", "Insurtech Startup Functional Finance")
c("functional-finance", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
  focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_cite=FFP, stage_conf="high",
  entry_date="2023-08",
  rounds=[rnd("2023-08-03", "Seed", 8000000, "New Enterprise Associates", True, FFP, "press")],
  note="NEA led the $8M seed (plus $2M of SAFEs) announced in August 2023 from San Francisco; the firm's listing "
       "gives 2022 and Seed. Momentum check 2026-09-30: no later round found. " + GP)

# ---- fusion-io: the Growth band is disputed by the Series A NEA led
c("fusion-io", city="Salt Lake City", rng="below_1b", focus="Data Infrastructure",
  stage="Series A", stage_src="web_verified", stage_cite=W("Fusion-io"), stage_conf="high", entry_date="2008-03",
  flags=["stage_disputes_band"],
  rounds=[rnd("2008-03", "Series A", 19000000, "New Enterprise Associates", True, W("Fusion-io"), "press"),
          rnd("2009-04", "Series B", 47500000, "Lightspeed Venture Partners", None, W("Fusion-io"), "press"),
          rnd("2010-04", None, 45000000, "Meritech Capital Partners", None, W("Fusion-io"), "press")],
  note="NEA led the $19M Series A of March 2008 (Wikipedia; the firm's own year is 2007), so the entry is Series A, "
       "not the Growth the 2011 Form D anchor read. Acquired by SanDisk in 2014; Salt Lake City as in the Accel and "
       "Lightspeed books (Wikipedia gives Cottonwood Heights).")

# ---- fyusion: the firm's Seed label and the May 2014 seed dispute the Series A band
c("fyusion", status="acquired", rng="below_1b", city="San Francisco", focus="AI & Applied AI",
  stage="Seed", stage_src="first_party", stage_cite=SITE("fyusion"), stage_conf="medium", entry_date="2014-05",
  flags=["stage_disputes_band"],
  rounds=[rnd("2014-05", "Seed", 3350000, None, True, W("Fyusion"), "press"),
          rnd("2015", None, 12999984, None, True, None, "filing")],
  note="The firm's listing labels its 2014 entry Seed, the $3.35M seed of May 2014 (Wikipedia), so the Series A "
       "band on the 2015 filing is disputed. Acquired by Cox Automotive. " + GP)

# ---- gadzoox-networks
c("gadzoox-networks", status="acquired", rng="below_1b", country="US", city="San Jose", focus="Data Infrastructure",
  stage="undetermined", entry_date="1996", rounds=[],
  note="Storage-networking company that filed for bankruptcy in August 2002; Broadcom bought its assets in 2003 ("
       + W("Gadzoox") + "), so it reads acquired out of insolvency. The 1996 round is not named.")

jl.write("c4b", L)
