"""PRO-105 grind, batch-001 (berry-street .. funcom). Evidence: scratch/evidence-pack.json (the firm's
company page and posts), scratch/siblings.json, scratch/news-bulk.json (Google News headlines, decoded
on citation), article texts read with scratch/read-articles.py, and the web checks named per line.
Membership of the live rows was seeded by prepare (site_listing). Graduation is judged in its own
pass after graduation-surfaces.py, except rows the clock censors."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, post, art, sib, page, news, wp = jl.cls, jl.rnd, jl.post, jl.art, jl.sib, jl.page, jl.news, jl.wp
L = []
def fp(slug, sub, stage, date, **kw):
    """Stage from the firm's own post naming the round (web_verified, the post is the citation)."""
    u = post(slug, sub)
    kw.setdefault("rounds", [rnd(date, stage if stage != "Growth" else kw.pop("round_word", "Growth round"), None, None, True, u, "firm")])
    return cls(slug, stage=stage, stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date=date, **kw)
def pc(slug):
    return dict(country_src="web_verified", country_cite=page(slug))

L.append(cls("berry-street", status="private", city="New York", stage="undetermined", rng="below_1b", focus="Healthcare & Bio",
    note="Insurance-covered nutrition therapy (New York); the firm lists Partnered 2023 and announced its investment in the $50M raise on 2025-02-05 (Sofina, FJ Labs and angels); no source names Northzone's entry round (Form Ds 2024-Q1 $9.3M, 2025-Q1 $30M; the band is withheld on a four-year-old issuer), so the stage is undetermined",
    rounds=[rnd("2025-02-05", "undisclosed", 50000000, None, True, post("berry-street", "our investment"), "firm")]))
L.append(cls("blitzy", status="private", city="Cambridge", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=news("Blitzy", "Ex-Nvidia"), entry_date="2026-05",
    rng="1b_plus", usd=1400000000, val_src="web_verified", val_cite=news("Blitzy", "Ex-Nvidia"), asof="2026-05-06",
    focus="DevTools & APIs",
    note="Autonomous code generation for enterprises (Cambridge, MA); Northzone led the $200M round at a $1.4B valuation (techfundingnews 2026-05-06; Lowenstein Sandler represented Northzone as lead), its first investment; Battery's row reads below $1B and is stale (aligned at the ingest)",
    rounds=[rnd("2026-05-05", "Growth round", 200000000, "Northzone", True, news("Blitzy", "Ex-Nvidia"), "press")]))
L.append(cls("hero-journey-club", status="private", city="San Mateo", city_src="formd_address", rng="below_1b", focus="Healthcare & Bio",
    note="Community-based mental health support (Form D addresses San Francisco and San Mateo, the later one kept); Series A band from the 2023-Q3 Form D of $14.7M, Wendy Xiao director, the firm lists Partnered 2023"))
L.append(cls("microverse", status="private", city="San Francisco", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=news("Microverse", "technext"), entry_date="2021-07", rng="below_1b", focus="Consumer & Marketplaces",
    note="Remote coding school (San Francisco; the firm lists Spain, the founder's base); Northzone led the $12.5M Series A with General Catalyst and All Iron (technext24, 2021-07-02; Sifted 2021-07-01), Michiel Kotting; an A extension in 2022 (Sifted)",
    rounds=[rnd("2021-07-01", "Series A", 12500000, "Northzone", True, news("Microverse", "technext"), "press")]))
L.append(fp("personio", "announcing our investment", "Series A", "2017-08", city="Munich",
    usd=int(float(sib("personio", "accel", "usd"))), val_src="web_verified", val_cite=sib("personio", "accel", "val_cite"),
    asof=sib("personio", "accel", "asof"), focus="SaaS", flags=["stale"],
    note="HR software for SMEs (Munich); Northzone invested in the $12M (EUR 10.5M) Series A with GFC and Picus (the firm's post, 2017-08-03), Michiel Kotting; last primary mark $8.5B (June 2022 Series E extension; aligned to Accel's and Lightspeed's cited mark), stale beyond 24 months; the 2025 Form D is a later filing, not the entry",
    rounds=[rnd("2017-08-03", "Series A", 12000000, None, True, post("personio", "announcing our investment"), "firm"),
            rnd("2021-10-12", "Series E", 270000000, "Greenoaks", True, post("personio", "6-3-billion"), "firm")]))
L.append(cls("sticky", status="acquired", city="San Francisco", city_src="formd_address", stage="undetermined", rng="below_1b",
    focus="SaaS",
    note="Eye-tracking ad-testing SaaS, founded in Stockholm as EyeTrackShop (the firm's post 'Northzone invests in EyeTrackShop', 2012-05-15), later Sticky Ad, Inc. of San Francisco (Form D 2016, Jeppe Zink director); the firm marks it Acquired, the acquirer is not named on any surface read; the 2012 round is not named (a $3M raise in 2013, MrWeb), so the entry stage is undetermined; Menlo's row reads defunct (rule 10, raised at the alignment)"))
L.append(cls("agon", status="private", **pc("agon"), city="London", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=news("Agon", "Advising Agon"), entry_date="2026-07", grad="censored", rng="below_1b", focus="AI & Applied AI",
    note="AI training and validation infrastructure for defence autonomy (London); the $30M (GBP 22.5M) seed of July 2026 with Lakestar, Lux Capital, Northzone and XYZ (Winston Taylor deal note; UKTN 2026-07-30); inside the 24-month window",
    rounds=[rnd("2026-07-29", "Seed", 30000000, None, True, news("Agon", "Advising Agon"), "press")]))
L.append(fp("aidence", "raises", "Seed", "2017-06", status="acquired", **pc("aidence"), city="Amsterdam", rng="below_1b",
    focus="Healthcare & Bio",
    note="AI for medical image analysis (Veye, Amsterdam); the EUR 2.25M seed with HenQ and the Health Innovation Fund (the firm's post, 2017-06-01); acq. by RadNet, 2022 (the firm's post 2022-01-24; RadNet's 424B7 of 2022-02-02 lists the selling holders)"))
L.append(fp("airforestry", "our investment", "Seed", "2024-10", status="private", **pc("airforestry"), city="Uppsala",
    city_src="web_verified", grad="censored", rng="below_1b", focus="Climate & Energy",
    note="Drone-based tree harvesting (AirForestry AB, Danmarksgatan 26, Uppsala: the company's own site); Northzone led the EUR 10.3M seed (the firm's post, 2024-10-10); a SEK 28M pre-commitment to the Series A in Feb 2026 (Cision) is not yet a round; inside the window read at the latest day of Oct 2024"))
L.append(cls("alphora", status="private", **pc("alphora"), stage="undetermined", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown"],
    note="AI-native IT service provider (the firm lists Germany, Partnered 2026, Wendy Xiao and Dominik Esen); the firm's page links no website and Google News has nothing (2026-09-29): the round and the city are not on record"))
L.append(cls("anyfin", status="private", city="Stockholm", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=news("Anyfin", "Series B to expand"), entry_date="2018-02", rng="below_1b", focus="Fintech & Payments",
    clear=[],
    note="Consumer loan refinancing (Stockholm); Northzone led the EUR 4.8M Series A of Feb 2018 (the firm's archived post 2018-02-21; tech.eu 2020-05-13: 'a Series A in 2018', Northzone tagged), then the EUR 8M A extension (the firm's post 2019-05-14); Wikidata SE confirmed",
    rounds=[rnd("2018-02-21", "Series A", None, "Northzone", True, news("Anyfin", "Series B to expand"), "press"),
            rnd("2019-05-14", "Series A extension", None, None, True, post("anyfin-raises-e8-million-to-help-consumers-refinance-their-loans"), "firm")]))
L.append(fp("asetek", "goes public", "Series A", "2005", status="public", country="DK", country_src="web_verified",
    country_cite=page("asetek"), city="Aalborg", rng="below_1b", focus="Industrial & Robotics", flags=["model_disputes_source"],
    note="Liquid cooling for computers and data centres (Aalborg, Denmark); 'Northzone was the leading institutional investor in Asetek, having invested in the company from its A round' (the firm's post, 2013-03-20); Oslo Børs listing March 2013; the pre-filled US is the San Jose office, disputed"))
L.append(cls("avito", status="acquired", **pc("avito"), city="Moscow", stage="undetermined", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Russia's leading classifieds marketplace; Northzone invested in 2010 (the firm lists Partnered 2010; Wikipedia: 'In 2010, Avito.ru collected a large amount of capital from venture capitalist Northzone Ventures'), round not named; exit when Naspers took a majority in Oct 2015 ($1.2B transaction, tech.eu; the firm's post 2015-10-23)"))
L.append(cls("axon", status="private", **pc("axon"), city="London", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Brain-inspired AI for high-frequency trading (Axon Labs, London; founded 2025); the firm lists Partnered 2025, Jeppe Zink and Naseem Moumene; a16z's row is its speedrun cheque; no press names Northzone's round (Google News 2026-09-29)"))
L.append(cls("bedrock", status="private", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=news("Bedrock", "Seafloor Exploration"), entry_date="2023-07", rng="below_1b", focus="Climate & Energy",
    flags=["city_unknown", "model_disputes_source"],
    note="AUV seafloor data for offshore wind (Bedrock Ocean Exploration); Northzone co-led the $25.5M Series A with Primary (the firm's post 2023-07-12; Ocean News & Technology); the pre-filled 'acquired' is a one-word Wikidata join and is disputed (the firm lists it Active); the city is stated neither on the company's site nor in the article",
    rounds=[rnd("2023-07-12", "Series A", 25500000, "co-led: Northzone, Primary", True, news("Bedrock", "Seafloor Exploration"), "press")]))
L.append(cls("behaviosec", status="acquired", **pc("behaviosec"), city="San Francisco", stage="undetermined", rng="below_1b",
    focus="Security",
    note="Behavioural biometrics (founded in Luleå, Sweden, 2008; later San Francisco HQ); Northzone and Octopus co-led a EUR 5M round in Dec 2014 (the firm's post, round not named; the firm lists Partnered 2013); acq. by LexisNexis Risk Solutions, 2022-05-03 (risk.lexisnexis.com press release); the firm's page still reads Active",
    rounds=[rnd("2014-12-08", "undisclosed", None, "co-led: Octopus, Northzone", True, post("behaviosec", "lands"), "firm")]))
L.append(cls("black-forest-labs", status="private", city="Freiburg", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=post("black-forest-labs", "our investment"), entry_date="2025",
    rng="1b_plus", usd=int(float(sib("black-forest-labs", "cherry", "usd"))), val_src="web_verified",
    val_cite=sib("black-forest-labs", "cherry", "val_cite"), asof=sib("black-forest-labs", "cherry", "asof"),
    focus="AI & Applied AI",
    note="Frontier visual-generation models (FLUX; Freiburg); 'we're proud to have been early believers in Black Forest Labs at Series A' (the firm's post, 2025-12-01), then the $300M Series B led by AMP and Salesforce Ventures at $3.25B (aligned to the siblings' cited mark)",
    rounds=[rnd("2025-12-01", "Series B", 300000000, "AMP, Salesforce Ventures", True, post("black-forest-labs", "our investment"), "firm")]))
L.append(cls("brickanta", status="private", **pc("brickanta"), city="Stockholm", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=news("Brickanta", "Pulse"), entry_date="2026-01", grad="censored", rng="below_1b", focus="AI & Applied AI",
    note="AI operating system for construction (Stockholm, YC); Northzone led the $8M seed (Pulse 2.0, 2026-01-28; Sifted); inside the window",
    rounds=[rnd("2026-01-28", "Seed", 8000000, "Northzone", True, news("Brickanta", "Pulse"), "press")]))
L.append(cls("bunch", status="private", **pc("bunch"), city="San Francisco", stage="undetermined", rng="below_1b",
    focus="Media, Gaming & Advertising",
    note="Social video party app for mobile games (San Francisco); the firm lists Partnered 2018; later the $3.85M round of Nov 2019 (Supercell, Miniclip, Riot) and the $20M Series A of Sep 2020 (Forbes), neither naming Northzone's entry; not Cherry's 'bunch' (a Berlin investment-syndicate fintech)"))
L.append(fp("caronsale", "growth investment", "Growth", "2025-07", status="private", **pc("caronsale"), city="Berlin", rng="below_1b",
    focus="Consumer & Marketplaces", round_word="Series C",
    note="B2B used-car auction platform (Berlin); Northzone led the EUR 70M Series C (the firm's post, 2025-07-07), its first investment; the seed was Creandum's (Aug 2019)"))
L.append(cls("catawiki", status="private", **pc("catawiki"), city="Amsterdam", stage="Growth", stage_src="model", stage_conf="medium",
    entry_date="2016", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online auctions for special objects (Amsterdam); the firm lists Partnered 2016, after the EUR 10M Series B of Sep 2014 (FinSMEs) and the $82M round of July 2015 (TechCrunch): any Northzone entry from 2015 on is a growth round; EUR 150M Permira-led round Dec 2020",
    rounds=[rnd("2014-09-25", "Series B", None, None, None, news("Catawiki", "€10M"), "press")]))
L.append(cls("chord", status="private", **pc("chord"), city="New York", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Headless commerce and customer-data platform (New York), formerly Arfa (renamed 2021); the firm lists Partnered 2020 and Jessica Schultz; the $18M Series A of March 2021 was led by Eclipse (TechCrunch) after about $7M earlier; Northzone's 2020 round is not named on any surface read (the archived Arfa page merges at the rebuild)"))
L.append(fp("clarium", "our investment", "Series A", "2025-05", status="private", **pc("clarium"), city="New York", rng="below_1b",
    focus="Healthcare & Bio",
    note="AI supply-chain software for hospitals; Northzone led the $27M Series A with General Catalyst (the firm's post, 2025-05-09); GC's row reads status unknown (aligned at the ingest)"))
L.append(cls("crosslend", status="private", **pc("crosslend"), city="Berlin", stage="undetermined", rng="below_1b",
    focus="Fintech & Payments",
    note="Cross-border loan securitisation marketplace (Berlin); the firm lists Partnered 2015 and Jeppe Zink; later a Series B (FinTech Global, 2019-10-17) and a EUR 35M Santander-led round (2020); Northzone's 2015 round is not named"))
L.append(cls("cusp-ai", status="private", **pc("cusp-ai"), city="Cambridge", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=post("our-investment-in-cuspai-pioneering-ai-designed-materials-to-combat-climate-change"), entry_date="2024-06", rng="below_1b", focus="AI & Applied AI",
    note="Generative AI for materials design (Cambridge, UK); Northzone participated in the $30M seed with Hoxton, BasisSet, LocalGlobe and Lightspeed (the firm's post, 2024-06-18); a $100M Series A followed in 2025 (the firm's portrait post; Fortune)",
    rounds=[rnd("2024-06-18", "Seed", 30000000, None, True, post("our-investment-in-cuspai-pioneering-ai-designed-materials-to-combat-climate-change"), "firm")]))
L.append(fp("dalma", "our investment", "Series A", "2022-06", status="private", **pc("dalma"), city="Paris", rng="below_1b",
    focus="Fintech & Payments",
    note="Pet health insurance (Paris); Northzone led the $15M (EUR 15M) Series A with Project A and Anterra (the firm's post, 2022-06-02)"))
L.append(fp("defacto", "our investment", "Series A", "2022-06", status="private", **pc("defacto"), city="Paris", rng="below_1b",
    focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Embedded B2B credit (Paris); Northzone led the EUR 15M Series A with Headline and GFC (the firm's post, 2022-06-07); the pre-filled 'acquired' with the parent 'Paris La Défense' is a Wikidata join on the one-word name and is disputed (the firm lists it Active)"))
L.append(cls("disperse", status="private", **pc("disperse"), city="London", stage="undetermined", rng="below_1b",
    focus="AI & Applied AI",
    note="AI progress tracking for construction (founded in London; the company's site now shows a San Francisco address); the firm lists Partnered 2019 and its post of 2019-10-22 on the $15M round (VentureBeat), round not named; $16M more in 2022 (TechCrunch)"))
L.append(cls("distribusion", status="private", **pc("distribusion"), city="Berlin", stage="Series A", stage_src="model", stage_conf="medium",
    entry_date="2016-03", rng="below_1b", focus="Consumer & Marketplaces",
    note="B2B marketplace for intercity bus tickets (Berlin); the EUR 6M round of March 2016 backed by Northzone, Creandum and HR Ventures, with the existing seed investor Frühphasenfonds Brandenburg (TechCrunch, 2016-03-17): the first round after the seed, the Series A by the record's own sequence; EUR 30M 2022, $80M 2024 (PhocusWire)",
    rounds=[rnd("2016-03-17", "undisclosed (after the seed)", None, None, True,
                "https://techcrunch.com/2016/03/17/distribusion-the-startup-that-makes-it-easy-to-sell-intercity-bus-tickets-picks-up-e6-million-funding/", "press")]))
L.append(cls("dots", status="acquired", **pc("dots"), city="New York", stage="undetermined", rng="below_1b",
    focus="Media, Gaming & Advertising",
    note="Mobile puzzle games (Playdots, New York; Paul Murphy was its founder-era executive officer before joining Northzone); the firm lists Partnered 2014 (Form D 2014-Q4 $9.65M), round not named on any surface read; acq. by Take-Two, 2020 (the firm's post 2020-08-18); not Felicis's or YC's Dots"))
L.append(cls("duvo-ai", status="private", **pc("duvo-ai"), city="Prague", stage="undetermined", rng="below_1b", focus="AI & Applied AI",
    note="AI automation for retail operations (Prague; founded 2025); the firm lists Partnered 2025, no press names the round (Google News 2026-09-29)"))
L.append(cls("einride", status="public", city="Stockholm", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-05",
    rng="below_1b", usd=int(float(sib("einride", "eqt-ventures", "usd"))), val_src="web_verified",
    val_cite=sib("einride", "eqt-ventures", "val_cite"), asof=sib("einride", "eqt-ventures", "asof"),
    focus="Industrial & Robotics", flags=["model_disputes_source"],
    note="Electric and autonomous freight (Stockholm); the firm lists Partnered 2021, the year of the $110M Series B (Einride, 2021-05-05; Reuters), which Northzone joined; listed on the NYSE through a 2026 SPAC merger (F-4 April 2026, 6-K June 2026), market cap aligned to EQT's cited figure; the pre-filled private $1.44B unicorn mark is superseded"))
L.append(cls("energy-micro", status="acquired", city="Oslo", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    note="Ultra-low-power 32-bit microcontrollers (Oslo); 'Northzone, together with Investinor, has been an investor in Energy Micro since March 2010' (the firm's post, 2013-06-10), round not named; acq. by Silicon Labs for $170M, 2013 (Silicon Labs 8-K 2013-06-07)"))
L.append(cls("episerver", status="acquired", country="SE", country_src="model_knowledge", city="Stockholm", stage="undetermined",
    rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="Web content management (EPiServer, Stockholm, founded 1994; today Optimizely); the firm lists Partnered 2007, round not named; Northzone sold its stake to IK Investment Partners (the firm's post, 2010-11-10); the firm's 'United States' is today's Optimizely HQ, the row keeps the Stockholm company it held"))
L.append(cls("era", status="private", **pc("era"), city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=news("Era", "Seed Led by Northzone"), entry_date="2023-11", rng="below_1b", focus="Fintech & Payments",
    flags=["model_disputes_source"],
    note="AI wealth management founded by Stripe alumni; the $3.1M seed led by Northzone (Business Wire, 2023-11-09); the pre-filled public / Bulgaria / $817M is a one-word Wikidata join to another company, disputed",
    rounds=[rnd("2023-11-09", "Seed", 3100000, "Northzone", True, news("Era", "Seed Led by Northzone"), "press")]))
L.append(cls("fiberplane", status="private", **pc("fiberplane"), city="Amsterdam", stage="Seed", stage_src="web_verified",
    stage_conf="high", stage_cite="https://techcrunch.com/2021/09/16/fiberplane-nabs-e-7-5m-seed-to-bring-google-docs-like-collaboration-to-incident-response/",
    entry_date="2021-09", rng="below_1b", focus="DevTools & APIs",
    note="Collaborative incident-response notebooks (Amsterdam); the EUR 7.5M seed co-led by Crane and Notion with Northzone participating (TechCrunch, 2021-09-16)",
    rounds=[rnd("2021-09-16", "Seed", None, "co-led: Crane, Notion Capital", True,
                "https://techcrunch.com/2021/09/16/fiberplane-nabs-e-7-5m-seed-to-bring-google-docs-like-collaboration-to-incident-response/", "press")]))
L.append(cls("filed", status="private", **pc("filed"), city="San Francisco", stage="undetermined", rng="below_1b", focus="AI & Applied AI",
    note="AI tax-preparation software; Northzone led the $17.2M round with Day One and Neo (TechCrunch 2025-05-21; the firm's post 2025-05-21), round word not given",
    rounds=[rnd("2025-05-21", "undisclosed", 17200000, "Northzone", True, news("Filed", "tax prep"), "press")]))
L.append(fp("finom", "growth investment", "Growth", "2024-02", status="private", **pc("finom"), city="Amsterdam", rng="below_1b",
    focus="Fintech & Payments", round_word="Series B",
    note="SME neobank (Amsterdam); Northzone co-led the EUR 50M Series B with General Catalyst (the firm's post, 2024-02-13), its first investment; EUR 115M Series C June 2025 (Finextra), valuation not disclosed"))
L.append(cls("fishbrain", status="private", **pc("fishbrain"), city="Stockholm", stage="Seed", stage_src="model", stage_conf="medium",
    entry_date="2014-07", rng="below_1b", focus="Consumer & Marketplaces",
    note="Social network and app for anglers (Stockholm); Northzone and Active Venture Partners led a round in July 2014 (the firm's post 2014-07-08), the round before the $8M Series A that Northzone also led (the firm's post 2015-07-22, 'A-round'): the seed by the record's own sequence; Series B $13.5M 2018 (TechCrunch)",
    rounds=[rnd("2014-07-08", "undisclosed (before the A)", None, "Northzone, Active Venture Partners", True, post("fishbrain", "secures funds"), "firm"),
            rnd("2015-07-22", "Series A", 8000000, "Northzone", True, post("fishbrain", "8m a-round"), "firm")]))
L.append(cls("flink", status="private", city="Berlin", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2021-02",
    usd=int(float(sib("flink", "cherry", "usd"))), val_src="web_verified", val_cite=sib("flink", "cherry", "val_cite"),
    asof=sib("flink", "cherry", "asof"), rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Quick-commerce groceries (Berlin); Flink's first institutional round of Feb 2021 (~$52M seed) was led by Cherry, Northzone and Target Global (Wikipedia, Flink (company)); $240M Series A June 2021; last mark about $900M (aligned to Cherry's cited figure); the pre-filled SE is a one-word Wikidata join, disputed; not Accel's Flink (Mexico)"))
L.append(fp("flower", "our investment", "Series A", "2024-10", status="private", **pc("flower"), city="Stockholm", rng="below_1b",
    focus="Climate & Energy",
    note="Battery-storage and energy optimisation platform (Stockholm); Northzone led the EUR 45M Series A (the firm's post, 2024-10-31); not Felicis's or YC's Flower"))
L.append(cls("footway", status="private", **pc("footway"), city="Stockholm", city_src="web_verified", stage="undetermined", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Online shoe and fashion retailer (Footway, Victoria Tower, Kista, Stockholm: the company's own site); the firm lists Partnered 2014, round not named on any surface read"))
L.append(cls("forto", city="Berlin", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=wp("northzone-leads-20m-series-freighthub"), entry_date="2017-12",
    usd=2100000000, val_src="web_verified", val_cite=news("Forto", "Logistics tech Forto valued at $2.1 billion"), asof="2022-03-07",
    focus="Industrial & Robotics", flags=["stale"],
    note="Digital freight forwarder (Berlin), formerly FreightHub; Northzone led the $20M Series A (the firm's post, 2017-12-13); valued at $2.1B in the $250M round of March 2022 (Reuters), stale beyond 24 months",
    rounds=[rnd("2017-12-13", "Series A", 20000000, "Northzone", True, wp("northzone-leads-20m-series-freighthub"), "firm")]))
L.append(fp("fubotv", "annoucing our investment", "Growth", "2017-06", country="US", country_src="web_verified", country_cite=page("fubotv"),
    city="New York", round_word="Series C",
    usd=992600000, val_src="web_verified", val_cite="https://stockanalysis.com/stocks/fubo/market-cap/", asof="2026-09-29",
    rng="below_1b", focus="Media, Gaming & Advertising", flags=["model_disputes_source"], status="public",
    note="Sports-first live TV streaming (New York); Northzone led the $55M Series C (the firm's post, 2017-06-19; NZ VIII (GP) Ltd's 13D of 2021); NYSE since Oct 2020; Disney took 70% when Hulu + Live TV combined with Fubo in 2025, and Fubo stays listed, so the pre-filled 'acquired' is disputed; market cap $992.6M (StockAnalysis, 2026-09-29), within 5% of the $1B edge"))
L.append(cls("funcom", country="NO", country_src="web_verified", country_cite=page("funcom"), city="Oslo", stage="undetermined",
    rng="below_1b", focus="Media, Gaming & Advertising",
    note="Online game developer (Oslo, founded 1993; Anarchy Online, Age of Conan); the firm lists Partnered 2004, ahead of the 2005 Oslo Børs listing, round not named; Tencent took 29% in 2019 and the whole company in 2020"))

jl.write("batch-001", L)
