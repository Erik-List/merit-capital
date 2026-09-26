"""PRO-106 grind, batch-003 (figleaves .. lifesum). Same evidence as batch-001."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
LIST = "https://www.balderton.com/companies/"
NEWS = "https://www.balderton.com/news/"
L = []
def fp(slug, stage, **kw):
    return cls(slug, stage=stage, stage_src="first_party", stage_cite=LIST, stage_conf="medium", **kw)
def wv(slug, stage, cite, **kw):
    return cls(slug, stage=stage, stage_src="web_verified", stage_cite=cite, stage_conf="high", **kw)

L.append(cls("figleaves", status="acquired", country="GB", city="London", stage="Growth", stage_src="model", stage_conf="medium", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Online lingerie retailer (founded 1998); the desk bought an almost 40% stake in 2005 (Wikipedia; Evans director 2006-10), a minority purchase in a seven-year-old company; acq. by N Brown Group, 2010 (GBP 11.5M)"))
L.append(wv("finoa", "Series A", NEWS + "finoa-the-digital-asset-platform-for-institutional-investors-and-corporations-raises-22m-series-a-led-by-balderton-capital/",
    status="private", country="DE", city="Berlin", rng="below_1b", focus="Crypto & Web3",
    note="Digital asset custody for institutions; the firm's post of 2021-04-29 announces the $22M Series A Balderton led"))
L.append(fp("flywire", "Growth", city="Boston", focus="Fintech & Payments",
    note="Cross-border payments; card 'Secondary in 2020' (Liquidity I; Flywire's 2021 draft registration names Balderton); Nasdaq IPO May 2021; cap pinned in the A/B pass"))
L.append(wv("forecast", "Series A", NEWS + "forecast-raises-19m-series-a-to-reimagine-project-based-work-using-ai-native-technology/", status="acquired", country="DK",
    city="Copenhagen", rng="below_1b", focus="SaaS", note="Project and resource management; the firm's post of 2021-05-19 announces the $19M Series A; acq. by Accelo, 2025"))
L.append(wv("funnel", "Series A", NEWS + "investment-update-funnel-raises-10m-to-expand-its-platform-for-fully-automated-marketing-reporting/", status="private",
    city="Stockholm", rng="below_1b", focus="SaaS", note="Marketing data platform; Balderton led the $10M Series A of Sep 2017; $47M Series B 2020, $66M pre-IPO round 2021"))
L.append(wv("furhat-robotics", "Seed", NEWS + "investment-update-furhat-robotics-raises-2-5m/", status="private", country="SE", city="Stockholm",
    entry_date="2017-09-14", rng="below_1b", focus="Industrial & Robotics", flags=["stage_disputes_band"],
    note="Social robots; the firm's post of 2017-09-14 announces $2.5M of seed funding from Balderton and LocalGlobe (Wikipedia agrees); the card says 'Series A in 2017'"))
L.append(cls("fuse-energy", status="private", city="London", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "tesseract-raises-78-million-to-fix-the-broken-energy-sector/", entry_date="2022-09-07",
    rng="1b_plus", usd=5000000000, val_src="web_verified", asof="2025-12-18", val_cite=NEWS + "fuse-energy-hits-5bn-valuation-in-its-third-year/",
    focus="Climate & Energy",
    note="Renewable energy supplier and developer (Tesseract until 2023); the $78M seed of Sep 2022 led by Balderton and Lakestar (the firm's post; Wikipedia); the firm's post of 2025-12-18 reports the round at a $5B valuation; Creandum's book still reads below_1b, the stale side for the wave alignment"))
L.append(fp("gcl", "Series A", status="acquired", country="HK", country_src="web_verified", country_cite=LIST, city="Hong Kong", rng="below_1b",
    focus="Climate & Energy", flags=["model_disputes_source"],
    note="Polysilicon maker (GCL Silicon Technology Holdings); card 'Series A in 2007' (its 2008 F-1 files the preferred share agreements naming the Balderton funds); acq. by GCL-Poly Energy, 2009; the pre-filled country SG is a wrong join"))
L.append(fp("geordie-ai", "Series A", status="private", country="GB", city="London", rng="below_1b", focus="Security",
    note="Security and governance for AI agents; card 'Series A in 2026'; band re-checked in the momentum pass"))
L.append(wv("gitguardian", "Series A", NEWS + "gitguardian-raises-12-million-to-find-sensitive-data-hidden-in-online-code/", status="private", country="FR",
    city="Paris", rng="below_1b", focus="Security", note="Secrets detection in code; the firm's post of 2019-12-04 announces the $12M Series A Balderton led; $44M Series B 2021, $50M Series C Feb 2026"))
L.append(cls("globoforce", status="private", city="Framingham", focus="SaaS", flags=["needs_web_value"],
    note="Employee recognition software (Workhuman since 2019; Dublin and Framingham); on the Benchmark desk lists from 2003 and named with the Balderton funds in its 2013-14 S-1; entry round and mark pinned in the A/B pass"))
L.append(wv("gocardless", "Growth", NEWS + "gocardless-raises-7m-from-balderton-capital-to-expand-development-team/", status="private", country="GB", city="London",
    focus="Fintech & Payments", flags=["needs_web_value"],
    note="Bank payments network; Balderton led the $7M Series B of Jan 2014 (the firm's post; Bunting director 2014-23); unicorn round Feb 2022; Mollie signed to acquire it (the firm's post of 2025-12-11); closing and mark checked in the A/B pass",
    rounds=[rnd("2014-01-28", "Series B", 7000000, "Balderton Capital", True, NEWS + "gocardless-raises-7m-from-balderton-capital-to-expand-development-team/", "firm"),
            rnd("2022-02-08", "Series G", 312000000, None, True, NEWS + "gocardless-joins-tech-unicorns-as-it-secures-312m-to-accelerate-growth-in-open-banking/", "firm")]))
L.append(cls("gourmondo", status="unknown", country="DE", city="Munich", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="German online delicatessen; on Benchmark's worldwide list 2006-08 (Europe lineage); neither the entry round nor the company's fate is on any surface read"))
L.append(wv("grand-games", "Series A", NEWS + "grand-games-raises-30m-series-a-to-build-genre-defining-mobile-games/", status="private", country="TR", city="Istanbul",
    rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile games studio; the firm's post of 2025-01-09 announces the $30M Series A Balderton led (Chandratillake director); $70M Series B May 2026; band re-checked in the momentum pass"))
L.append(fp("graphcore", "Growth", status="acquired", country="GB", city="Bristol", rng="below_1b", focus="Industrial & Robotics",
    note="AI processors; card 'Secondary in 2020' (Liquidity I; D5); acq. by SoftBank, 2024"))
L.append(fp("grasp", "Seed", status="private", country="GB", city="London", entry_date="2023", rng="below_1b", focus="AI & Applied AI",
    note="AI learning tools; card 'Seed 2023'; Point Nine's book carries the same seed"))
L.append(wv("healx", "Series A", NEWS + "healx-raises-10m-for-ai-technology-that-finds-treatments-for-rare-disease-faster/", status="private", country="GB",
    city="Cambridge", rng="below_1b", focus="Healthcare & Bio",
    note="AI drug discovery for rare diseases; the firm's post of 2018-07-26 announces the $10M Series A Balderton led (Chandratillake director from 2018-06); $47M Series C 2024"))
L.append(fp("housecall-pro", "Growth", status="private", country="US", city="San Diego", focus="SaaS", flags=["needs_web_value"],
    note="Software for home-service businesses; card 'Secondary in 2020' (Liquidity I; D5); mark checked in the A/B pass"))
L.append(fp("housetrip", "Growth", status="acquired", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Holiday rental marketplace; card 'Series B in 2011' (Bunting director 2012-16); acq. by TripAdvisor, 2016; Accel's book still reads private, the stale side for the wave alignment"))
L.append(wv("hubilo", "Series A", NEWS + "hubilo-raises-17m-series-a-to-redefine-the-future-of-events/", status="acquired", country="US", city="San Francisco",
    rng="below_1b", focus="SaaS", note="Virtual and hybrid events platform (founded in Ahmedabad, HQ San Francisco); the firm's post of 2021-02-24 announces the Series A; acq. by Brandlive, 2024 (status medium confidence; the card says Exited)"))
L.append(wv("hubs", "Series A", NEWS + "news-3d-hubs-raises-4-5m-series-a-funding-led-by-balderton-capital-to-bring-local-3d-printing-to-your-doorstep/", status="acquired",
    country="NL", city="Amsterdam", rng="below_1b", focus="Industrial & Robotics",
    note="Online manufacturing network (3D Hubs); Balderton led the $4.5M Series A of Sep 2014; acq. by Protolabs, 2021"))
L.append(fp("huspy", "Series A", status="private", country="AE", city="Dubai", rng="below_1b", focus="Consumer & Marketplaces",
    note="Home-buying and mortgage platform (Dubai HQ, the card's Madrid is the European base); card 'Series A in 2024' (the firm's post of 2024-05-22); $59M Series B Jul 2025"))
L.append(wv("infarm", "Series A", "https://techcrunch.com/2018/02/05/balderton-backs-infarm/", status="acquired", country="DE", city="Berlin",
    rng="below_1b", focus="Climate & Energy",
    note="Vertical farming; Balderton led the $25M Series A of Feb 2018 (TechCrunch); the 2021 unicorn mark collapsed, the European business went through insolvency in 2023 and the assets continue in a successor company (acquired out of insolvency, as in the Atomico and Cherry books)"))
L.append(cls("innerworkings", city="Chicago", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Print procurement; on Benchmark's worldwide list 2005-08, in the Europe desk's section (PRO-88 lineage); Nasdaq IPO 2006, acq. by HH Global, 2020; the entry round is not named on any surface read"))
L.append(fp("instabridge", "Series A", status="acquired", country="SE", city="Stockholm", rng="below_1b", focus="Consumer & Marketplaces",
    note="Wi-fi sharing app; card 'Series A in 2015' (the firm's post of 2015-09-02: $3M led by Moor and Balderton); acquired, as in Creandum's book"))
L.append(cls("instranet", status="acquired", country="FR", city="Paris", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Knowledge management for customer service; on the Benchmark desk lists 2001-08; the entry round is not named on any surface read; acq. by Salesforce, 2008"))
L.append(wv("itoflow", "Pre-Seed", NEWS + "itoflow-raises-2-5-million-to-bring-institutional-grade-portfolio-management-to-every-investor/", status="private",
    country="GB", city="London", rng="below_1b", focus="AI & Applied AI", note="AI agents for portfolio management; the firm's post of 2026-08-25 announces the $2.5M pre-seed"))
L.append(wv("jokr", "Series A", NEWS + "next-generation-instant-delivery-platform-jokr-announces-170m-series-a/", status="private", country="US", city="New York",
    focus="Consumer & Marketplaces", flags=["needs_web_value"],
    note="Instant grocery delivery; the firm's post of 2021-07-20 announces the $170M Series A; $260M Series B at $1.2B Dec 2021; the company left the US and Europe in 2022; mark pinned or killed in the A/B pass"))
L.append(wv("jolt", "Series A", NEWS + "jolt-raises-14m-to-disrupt-higher-education-with-its-pay-monthly-business-school/", status="unknown", city="Tel Aviv",
    rng="below_1b", focus="Consumer & Marketplaces", note="Pay-monthly business school; the firm's post of 2020-01-13 announces the $14M Series A Balderton led; the card says Exited and the event is not on any surface read"))
L.append(wv("jumbo-privacy", "Series A", NEWS + "jumbo-privacy-raises-8m-series-a-and-launches-jumbo-2-0-to-fight-for-consumers-privacy/", status="unknown", country="US",
    city="New York", rng="below_1b", focus="Security", note="Consumer privacy app; the firm's post of 2020-06-24 announces the $8M Series A Balderton led; the card says Exited and the event is not on any surface read"))
L.append(wv("kaia-health", "Series A", NEWS + "kaia-health-raises-10m-to-transform-treatment-of-chronic-pain-conditions/", status="private", country="DE", city="Munich",
    rng="below_1b", focus="Healthcare & Bio", note="Digital therapeutics for back pain and COPD; the firm's post of 2019-01-21 announces the $10M Series A Balderton led (card 'Series A in 2018', the close year); $75M Series C 2021"))
L.append(cls("kalido", status="acquired", city="London", stage="undetermined", rng="below_1b", focus="Data Infrastructure",
    note="Data warehouse software spun out of Shell; on the Benchmark Europe desk page from 2004; the entry round is not named on any surface read; acq. by Silverback Enterprise Group, 2014"))
L.append(cls("kbox-global", status="defunct", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["model_disputes_source"],
    note="Host-kitchen platform for delivery brands; the card says 'Pre-Series A in 2020', which straddles two stages, and the firm's post of 2020-09-17 (GBP 12M) names no round; the card says Live, Companies House 09556537 shows Kbox Global Limited dissolved (Waterhouse director from 2020-09)"))
L.append(wv("kili-technology", "Series A", NEWS + "kili-technology-raises-25m-to-speed-up-ai-adoption/", status="private", country="FR", city="Paris",
    rng="below_1b", focus="AI & Applied AI", note="Training-data platform; the firm's post of 2021-07-27 announces the $25M Series A Balderton led"))
L.append(cls("kobalt", status="acquired", country="US", country_src="model_knowledge", city="New York", stage="undetermined", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="Music publishing and royalties technology (founded by a Swede in London, HQ New York); the card says 'Initial investment in 2008', which names no round (Bunting director of Kobalt Music Group 2008-22); Francisco Partners took a controlling stake in 2022; the pre-filled country IT is a wrong join"))
L.append(cls("kong", status="private", country="US", country_src="web_verified", country_cite=LIST, city="San Francisco",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "kong-secures-175m-new-financing-at-2bn-valuation-to-power-the-api-world/",
    rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2024-11-19",
    val_cite=NEWS + "kong-secures-175m-new-financing-at-2bn-valuation-to-power-the-api-world/", focus="DevTools & APIs", flags=["model_disputes_source"],
    note="API platform; the firm's post of 2024-11-19 announces the $175M Series E at a $2B valuation, Balderton's entry (card 'Series E in 2024'); the same mark as a16z's book; the pre-filled country IT is a wrong join"))
L.append(wv("labster", "Series A", "https://techcrunch.com/2017/09/06/virtual-science-lab-startup-labster-bags-10m/", status="private", country="DK",
    city="Copenhagen", rng="below_1b", focus="SaaS", note="Virtual science labs; Balderton led the $10M Series A of Sep 2017 (TechCrunch); $60M Series C 2021"))
L.append(wv("lassie", "Growth", "https://techcrunch.com/2023/11/28/as-pet-owners-turn-to-mobile-insurance-apps-lassie-raises-25m-series-b-led-by-balderton/",
    status="private", country="SE", city="Stockholm", rng="below_1b", focus="Fintech & Payments",
    note="Preventive pet insurance; Balderton led the $25M Series B of Nov 2023 (TechCrunch; card 'Series B 2023'); $75M Series C Feb 2026; band re-checked in the momentum pass"))
L.append(fp("latana", "Series A", status="private", country="DE", city="Berlin", rng="below_1b", focus="SaaS",
    note="Brand tracking (Dalia Research until 2019); card 'Series A in 2016' (the firm's post of 2017-01-26: Balderton led the $7M round in Dalia Research); EUR 36M Series B 2022"))
L.append(wv("lawhive", "Series A", NEWS + "lawhive-raises-40m-to-expand-its-legal-ai-platform-in-the-us/", status="private", country="GB", city="London",
    rng="below_1b", focus="AI & Applied AI", note="AI-native consumer law firm; the firm's post of 2024-12-05 announces the $40M Series A; band re-checked in the momentum pass"))
L.append(fp("lendable", "Growth", status="private", country="GB", city="London", focus="Fintech & Payments", flags=["needs_web_value"],
    note="Consumer lending; card 'Secondary in 2019' (Liquidity I; D5); the GBP 210M round of Mar 2022 is pinned in the A/B pass"))
L.append(fp("levelup", "Growth", status="acquired", country="US", city="Boston", rng="below_1b", focus="Fintech & Payments",
    note="Mobile payments and ordering for restaurants (SCVNGR until 2011; Maloney on its Form Ds 2011-17); card 'Series C in 2010'; acq. by Grubhub, 2018 ($390M)"))
L.append(wv("levity", "Seed", NEWS + "levity-raises-8-3m-to-bring-the-power-of-ai-to-businesses-of-all-sizes/", status="private", country="DE", city="Berlin",
    entry_date="2022-10-12", rng="below_1b", focus="AI & Applied AI", note="No-code AI automation for freight email; the firm's post of 2022-10-12 announces the $8.3M seed"))
L.append(fp("lifesum", "Growth", status="private", country="SE", city="Stockholm", rng="below_1b", focus="Consumer & Marketplaces",
    note="Nutrition app; card 'Secondary in 2018' (Liquidity I; D5)"))
jl.write("batch-003", L)
