"""PRO-162 grind, batch-006 (actively .. chai-discovery). Evidence as in judgments-1.py, plus Wikipedia extracts
cached under scratch/wiki/ (wikifetch.py), Google News (nq.py, news-extra-b6.json), the firm's own Common Crawl
captures (CCPAGE), and press pages read 2026-09-27 (WebFetch; WebSearch for Cameo, Alice, Ario, Celestia and the
Bain Capital Private Equity portfolio list).

Three archive rows leave as another desk: Ameritrade, AMR Interactive and CameraWorld.com appear only on the firm's
2006 page (the page that also carried Bain Capital's generalist history) and all three sit on Bain Capital Private
Equity's own portfolio list, which carries the heritage names (Staples, Bright Horizons, DoubleClick, Stericycle,
Gartner, Babbage's, Calumet Coach, ABRY, Blue Ridge) and none of the venture fund's own positions of the same era
(Taleo, Brontes, Vonage, Tengion, Rapid7, Archer, Ameritox, CentrePath, Alibre, aPriori).

Base defects found: 'adaptive' merges two live-site entries named Adaptive (Adaptive Security, /portfolio/adaptive/,
and Adaptive Innovations, /portfolio/adaptive-health/); this line classifies Adaptive Security. 'basecoin' is 'basis'
under its first name and 'apparent-networks' is 'appneta-broadcom-software' under its old name; both pairs are
classified alike here and wait for an identity merge."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []

# URLs printed by WebSearch (2026-09-27), not typed.
PE_LIST = "https://www.baincapitalprivateequity.com/portfolio/current-and-former-portfolio-companies"
CAMEO_B = "https://www.prnewswire.com/news-releases/cameo-closes-50-million-series-b-round-led-by-kleiner-perkins-300874358.html"
CELESTIA_HQ = "https://tracxn.com/d/companies/celestia/__e9lFtoe2JngZ2Ws_0uK2xeTpXSMEiWtTAKGnUkbpcCc"
ALICE_2018 = "https://technical.ly/startups/alice-fintech-startup-payroll-benefits/"
TAG = "[bain_capital_heritage] "


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


def other_desk(slug, why, conf="medium"):
    L.append(verdict(slug, "not_member",
        TAG + "Another desk (decisions.md D1, D2, R1): " + why + " Bain Capital Private Equity's own portfolio list carries "
        "it beside the generalist-fund names (Staples, Bright Horizons, DoubleClick, Stericycle, Gartner, Babbage's), while "
        "the venture fund's own positions of the same era (Taleo, Brontes, Vonage, Tengion, Alibre, aPriori) are absent "
        "from that list; no record names a Bain Capital venture vehicle as a holder. The firm listed it only on its 2006 "
        "page, which files the generalist deals under 'Bain Capital's history of investing ... since 1984'.",
        ec="site_listing", conf=conf, cite=PE_LIST))


# ---- current site (live Sanity list) ----
L.append(cls("actively", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="AI & Applied AI", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("actively", "Actively AI raises $22.5M to offer"), entry_date="2024",
    note="AI agents for enterprise sales (New York). 'Raised $17.5 million in Series A funding from Bain Capital Ventures' beside "
         "'a previously unannounced $5 million seed round from First Round Capital' (TechCrunch, 2025-04-02); the firm's listing "
         "dates its check to 2024. A $45M Series B led by TCV followed in April 2026. Momentum check (AI, 2024): no priced round "
         "at $1B or more was found. Aligned with First Round (New York)."))
L.append(cls("adaptive", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Security", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("adaptive", "Adaptive Security Raises $81 Million Series B"), entry_date="2025-12",
    flags=["model_disputes_source"],
    note="Adaptive Security, defence against AI-driven social engineering (New York). BCV led the $81M Series B (PR Newswire, "
         "2025-12-16, dateline New York; Enrique Salem quoted); the Series A was led by the OpenAI Startup Fund and a16z. The "
         "prefilled LV is a wrong join on the bare name; a16z's row is the same company, left unresolved there. Momentum check "
         "(security, 2025): no priced round at $1B or more was found. BASE DEFECT: this row merges the firm's two 'Adaptive' "
         "entries; the other, Adaptive Innovations (/portfolio/adaptive-health/, home health, Seed), needs its own row."))
L.append(cls("akkio", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Cambridge",
    focus="AI & Applied AI", stage="Seed", **site_stage("akkio"), entry_date="2019",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("akkio", "Akkio secures $15M"),
    note="No-code AI analytics for businesses (Cambridge, MA in the firm's listing). BCV's listing: 2019, Seed; BCV and Pandome then "
         "led the $15M Series A ('Massachusetts-headquartered Akkio', VentureBeat, 2023-08-01), which graduates it.",
    rounds=[rnd("2023-08", "Series A", 15000000, "Bain Capital Ventures and Pandome", True, NEWS("akkio", "Akkio secures $15M"), "press")]))
L.append(cls("andera", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="AI & Applied AI", stage="undetermined", entry_date="2026",
    note="AI platform for internal audit ('The San Francisco startup', The Next Web, 2026-06-19). Lightspeed led the $37M Series A of "
         "June 2026; no source read names BCV's round (the firm's listing: 2026, Early, which mints no stage). Momentum check "
         "(AI, 2026): no priced round at $1B or more."))
L.append(cls("ansa", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("ansa", "Founded by Adyen and Affirm"), entry_date="2022",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("ansa", "Wallet-as-a-service"),
    note="Branded stored-value wallets for merchants (San Francisco). 'Bain Capital Ventures led Ansa's $5.4 million seed round last "
         "year' (TechCrunch, 2023-04-26); a $14M Series A led by Renegade Partners followed (TechCrunch, 2024-04-30). Rain bought "
         "Ansa in August 2026 (" + NEWS("ansa", "Rain Buys Merchant Wallet") + "); the firm's listing reads Acquired.",
    rounds=[rnd("2024-04", "Series A", 14000000, "Renegade Partners", None, NEWS("ansa", "Wallet-as-a-service"), "press")]))
L.append(cls("apollo-io", status="private", rng="1b_plus", usd=1600000000, val_src="web_verified", asof="2023-08-29",
    val_cite=NEWS("apollo-io", "Apollo.io Secures $100 Million Series D"), extra={"valuation_range_source": "web_verified"},
    city="San Francisco", focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=POST("how-apollo-io"), entry_date="2023-08", flags=["stale"],
    note="Sales intelligence and engagement platform (San Francisco). 'That vision drew Bain Capital Ventures to lead Apollo's $100 "
         "million Series D round' (the firm's post, 2023-08-29), at $1.6B (PR Newswire); aligned with Y Combinator's mark. No later "
         "priced round was found; stale beyond 24 months."))
L.append(cls("aqueduct", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Bellevue",
    focus="Fintech & Payments", stage="Seed", **site_stage("aqueduct"), entry_date="2021",
    note="Billing, invoicing, quoting and accounting for B2B companies (Bellevue, WA in the firm's listing). BCV's listing: 2021, "
         "Seed (Kevin Zhang), outcome Acquired; no source read names the buyer. Graduation left for the graduation pass."))
L.append(cls("ario", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Palo Alto",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("ario", "Ario Raises $16 Million to Tackle Invisible Labor with AI - Business Wire"), entry_date="2024-06",
    flags=["model_disputes_source"],
    note="AI household assistant for parents (Palo Alto). '$16 million in seed funding from top-tier investors, including Wing Venture "
         "Capital, Floodgate, Bain Capital Ventures, Moxxie' (Business Wire, 2024-06-26; Floodgate led). The prefilled NZ is a "
         "wrong join on the bare name. Momentum check (AI, 2024): no later priced round found. Graduation left for the graduation pass."))
L.append(cls("astronomer", status="private", rng="below_1b", city="Cincinnati", focus="Data Infrastructure",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("astronomer", "Astronomer Raises $5.7 Million"),
    entry_date="2019-09", flags=["stage_disputes_band"],
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("astronomer", "Astronomer Secures $93 Million Series D"),
    note="Data orchestration on Apache Airflow (Cincinnati, also New York). 'We first invested in Astronomer back in 2019' (the firm's "
         "post, 2025-05-01): the $5.7M seed led by Sierra Ventures with BCV (PR Newswire, 2019-09-25). The listing's 2025 Growth tag is "
         "BCV's follow-on in the $93M Series D; the documented first check overrides it. Later priced rounds through the Series D "
         "graduate it. Momentum check: no priced round at $1B or more; aligned with Insight (Cincinnati, below_1b).",
    rounds=[rnd("2025-05", "Series D", 93000000, None, True, NEWS("astronomer", "Astronomer Secures $93 Million Series D"), "press")]))
L.append(cls("atoms", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Los Angeles",
    focus="Industrial & Robotics", stage="Growth", **site_stage("atoms"), entry_date="2026-07",
    note="Travis Kalanick's physical-automation company, which folds in CloudKitchens (Los Angeles). BCV's listing: 2026, Growth "
         "(Merritt Hummer); 'Bain Capital' is named in the $1.7B equity round led by a16z (" + NEWS("atoms", "Kalanick raises $1.7B for Atoms, and Uber")
         + ", 2026-07-23). 'The company did not disclose a valuation', so no mark can be recorded and the row stays below_1b "
         "(COLLECTION.md s6 Rule A; the ShipBob reading). Momentum check done: no published figure. a16z's 'atoms' row is Atoms "
         "the New York footwear company, a name collision."))
L.append(cls("auxilius", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Healthcare & Bio", stage="undetermined", entry_date="2022",
    note="Clinical-trial financial management for biotechs (New York; 'backed by ... Bain Capital Ventures, Renegade Partners, and XYZ "
         "Venture Capital', PR Newswire 2022-09-13). BCV's listing: 2022, Early; the $10M round of June 2022 is not named in any "
         "source read. SignalFire led a further $10M in 2024. Momentum check: no priced round at $1B or more."))
L.append(cls("black-forest-labs", status="private", rng="1b_plus", usd=3250000000, val_src="web_verified", asof="2025-12-01",
    val_cite=NEWS("black-forest-labs", "Announces Series B Investment"), extra={"valuation_range_source": "web_verified"},
    city="Freiburg", focus="AI & Applied AI", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("black-forest-labs", "Announces Series B Investment"), entry_date="2025-12",
    note="Frontier image-generation models, FLUX (Freiburg, Germany). BCV joined the $300M Series B led by AMP and Salesforce Ventures "
         "at $3.25B post-money (GlobeNewswire release, 2025-12-01; dateline Freiburg); a Series B entry reads Growth. Aligned with "
         "a16z, Cherry and Creandum."))
L.append(cls("cape", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Washington",
    focus="Security", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("cape-getting-to-the-core"),
    entry_date="2026-03",
    note="Privacy-first mobile carrier (Washington, DC area). 'That's why we invested in Cape - and are excited to be leading their "
         "$100M Series C' (the firm's post, 2026-03-18). Momentum check (security, 2026): no valuation was published. Aligned with "
         "a16z and IVP (Washington, below_1b)."))
L.append(cls("celestia", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", asof="2022-10-19",
    val_cite=NEWS("celestia", "hits unicorn status"), extra={"valuation_range_source": "web_verified"},
    city="Vaduz", city_src="web_verified",
    focus="Crypto & Web3", stage="Series A", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("celestia", "Celestia Labs Raises $55M"), entry_date="2022-10", flags=["stale"],
    note="Celestia Labs, the modular data-availability blockchain, on Bain Capital Crypto's list (Vaduz, Liechtenstein per its company "
         "profile). Bain Capital Crypto and Polychain led the $55M raised in 'two quietly conducted rounds, a Series A and B', which "
         "'valued Celestia at $1 billion' (The Block, 2022-10-19): a priced equity round, so not token-funded; the entry is read at "
         "the first of the two (medium). Bain Capital Crypto also led the Celestia Foundation's $100M token round of September 2024. "
         "Mark: the 2022 round; stale beyond 24 months. The TIA token trades separately and is not the company's mark. "
         "Country OPEN: the headquarters is Vaduz, Liechtenstein (LI, " + CELESTIA_HQ + "), but run.py's ISO table has no "
         "Liechtenstein, so record refuses 'LI'; the country is left empty until the table carries it."))
L.append(cls("chai-discovery", status="private", rng="1b_plus", usd=3800000000, val_src="web_verified", asof="2026-07",
    val_cite=NEWS("chai-discovery", "Chai Discovery nabs $400M"), extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="San Francisco", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("chai-discovery", "Chai Discovery nabs $400M"),
    entry_date="2026-07",
    note="AI-designed antibodies and molecules (San Francisco). 'New investors joining the investment included Bain Capital Ventures' "
         "in the $400M Series C led by Index Ventures, which 'brought the company's valuation to $3.8 billion' (SiliconANGLE, "
         "2026-07-14). Aligned with Battery, Menlo, Sequoia and Thrive."))

# ---- archive-era rows ----
L.append(cls("adentro", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="SaaS", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2015",
    note="Adentro, formerly Zenreach (renamed 2021), WiFi-based marketing for physical businesses (San Francisco; zenreach folds into "
         "this row). Before it emerged from stealth, Adentro 'had raised $20 million in two funding rounds led by investors like "
         "Formation 8, Bain Capital Ventures, First Round Capital' (" + W("Zenreach") + "), before the $30M Series B led by Founders "
         "Fund; BCV's 2015 check (Ajay Agarwal) in the second of those rounds, the one before the B, reads as the Series A. Aligned "
         "with 8VC and Felicis (San Francisco, private)."))
L.append(cls("alibre", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Richardson",
    focus="SaaS", stage="undetermined",
    note="Web-collaborative 3D CAD (Alibre, Richardson, TX; founded 1997, per " + W("Alibre Design") + "). 3D Systems acquired it in "
         "July 2011 (" + NEWS("alibre", "3D Systems acquires Alibre") + ") and divested it again in 2016-17 as Alibre, LLC. BCV "
         "listed it in 2003; the round is not named."))
L.append(cls("alice", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="undetermined", flags=["model_disputes_source"],
    note="Alice (thisisalice.com), automated pre-tax spending benefits (New York in the firm's page, " + CCPAGE("/portfolio/alice/")
         + "; 'a Brooklyn-based HR-tech startup' that had raised a seed round, " + ALICE_2018 + "). The firm listed it 2019-2022 "
         "(Matt Harris, Seed/Early Stage); the round BCV entered is not named. The prefilled 'acquired' by TIM Group and NZ belong to "
         "another Alice; its site still operates and no sale was found."))
L.append(cls("allyo", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Mountain View",
    focus="AI & Applied AI", stage="Series A", stage_src="model", stage_conf="medium",
    entry_date="2018-03",
    note="AI recruiting assistant (Sunnyvale, later Mountain View). BCV led the $14M round announced 2018-03-20 (PR Newswire, '"
         + "$14M in Funding from Bain Capital Ventures'); the $45M Series B of June 2019 brought the total to $64M (GlobeNewswire), "
         "so the $14M round sits between a small seed and the B and reads as the Series A. HireVue bought AllyO in 2020 ("
         + NEWS("allyo", "Carlyle-backed HireVue") + ")."))
L.append(cls("ameritox", status="acquired", rng="below_1b", city="Baltimore", focus="Healthcare & Bio", stage="undetermined",
    note="Pain-medication monitoring laboratory (Baltimore; lab in Greensboro, NC). 'In 2018 Ameritox sold its book of business, "
         "auctioned equipment and other assets, and ceased to operate' (" + W("Ameritox") + "): an asset sale out of a wind-down, so "
         "acquired (COLLECTION.md s6); PitchBook names Aegis Sciences as the buyer. Sibling Sequoia still reads private; this "
         "cited 2018 sale is fresher. The firm listed it from 2010 (Growth, 'Expansion/Growth Buyout'); the round is not named."))
L.append(cls("apimetrics", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Seattle",
    focus="DevTools & APIs", stage="undetermined",
    note="API monitoring (Seattle). 'It has raised $2.6 million from investors including Bain Capital Ventures' (GeekWire, 2023-09-14, "
         + NEWS("apimetrics", "Seattle startup APImetrics merges") + "), when Contxt merged into it and its staff joined APImetrics, "
         "which continues. The firm listed it 2015-2016; the round is not named."))
L.append(cls("apparent-networks", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="Data Infrastructure", stage="undetermined",
    note="Apparent Networks is AppNeta under its old name (the firm's 2010 listing at Wellesley Hills, MA; " + W("AppNeta") + ": "
         "Boston headquarters from 2008, Broadcom acquisition announced 2021-12-07). Classified as the 'appneta-broadcom-software' "
         "row is; the two rows are one company and should merge."))
L.append(cls("apriori", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Concord",
    focus="SaaS", stage="undetermined",
    note="Manufacturing cost and product-cost software (aPriori Technologies, Concord, MA in the firm's 2006 listing); still "
         "operating (Business Wire product launch, 2026-08-19). BCV held it by 2006 (Early bucket, context only); the round is not named."))
L.append(cls("arc", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("arc", "Arc wants to build the de facto"), entry_date="2022-01",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("arc", "Fintech start-up Arc lands"),
    note="Arc Technologies, finance platform for software startups (arc.tech, San Francisco in the firm's 2022 page, "
         + CCPAGE("/portfolio/arc/") + "). The $11M seed led by NFX with Bain Capital (TechCrunch, 2022-01-13), alongside $150M of "
         "debt; the firm's page (Seed/Early, Sarah Smith) ties it to BCV. A $20M Series A followed in 2025. Axos signed to buy it on "
         "2026-07-06 and 'closed the Arc Technology transaction a few weeks ago' (Axos earnings call, "
         + NEWS("arc", "Earnings call transcript: Axos beats") + "), fresher than a16z's 'private'. Menlo's 'Arc' (Torrance, "
         "electric boats) is a name collision.",
    rounds=[rnd("2025-06", "Series A", 20000000, None, None, NEWS("arc", "Fintech start-up Arc lands"), "press")]))
L.append(cls("archer-technologies", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Overland Park", focus="Security", stage="Growth", stage_src="first_party", stage_conf="medium",
    stage_cite=CCPAGE("/portfolio/company/archer-technologies/"), entry_date="2008",
    note="Governance, risk and compliance software (Overland Park, KS). 'Bain Capital Ventures provided primary and secondary growth "
         "capital' to a bootstrapped company, and 'Archer Technologies was acquired by EMC 15 months after the initial investment' "
         "(the firm's 2012 page; EMC bought it in January 2010), so the entry is late 2008. Board seat and an acting CFO role; no "
         "source read gives the stake size. Y Combinator's 'Archer' (San Francisco AI) is a name collision."))
L.append(cls("aria-systems", status="private", rng="below_1b", city="San Francisco", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Aria Systems"), entry_date="2013",
    note="Cloud billing for recurring revenue (San Francisco; founded in Media, PA). In 2013 'Aria opened its first international office "
         "in London and raised a $40 million Series D round led by Bain Capital Ventures' (Wikipedia); a Series D entry reads Growth. "
         "A $90M growth round led by Goldman Sachs followed in 2021."))
L.append(cls("basecoin", status="defunct", rng="below_1b", country="US", country_src="model_knowledge", city="Hoboken",
    focus="Crypto & Web3", stage="undetermined",
    note="Basecoin is Basis under its first name (the firm's January 2018 page, getbasecoin.com, 'a robust, price-stable cryptocurrency "
         "with an algorithmic central bank', " + CCPAGE("/portfolio/basecoin/") + "); classified as the 'basis' row is. The two rows "
         "are one company and should merge."))
L.append(cls("basis", status="defunct", rng="below_1b", country="US", country_src="model_knowledge", city="Hoboken", focus="Crypto & Web3", stage="undetermined",
    flags=["model_disputes_source"],
    note="Basis (formerly Basecoin), an algorithmic stablecoin. 'Salil Deshpande, an investor at Bain Capital Ventures who led the "
         "investment round in Basis' (Fortune, 2018-12-13, " + NEWS("basis", "Here's What Its Lead Investor") + "): $133M raised in "
         "2018; the project shut down in December 2018 and returned the remaining funds. The instrument and round name are not "
         "given, so the stage is undetermined. The prefilled JP belongs to another Basis; aligned with a16z (defunct, Hoboken). "
         "Accel's and Khosla's 'Basis' rows are the New York AI accounting company, a name collision."))
L.append(cls("bench", status="acquired", rng="below_1b", country="CA", country_src="web_verified", country_cite=W("Bench Accounting"),
    city="Vancouver", focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=W("Bench Accounting"), entry_date="2016-05", flags=["model_disputes_source"],
    note="Online bookkeeping for small businesses (Vancouver). 'In 2016, the company raised $16 million in Series B funding, led by Bain "
         "Capital Ventures' (Wikipedia); a Series B entry reads Growth. Bench shut down on 2024-12-27 and Employer.com acquired it days "
         "later, resuming operations in January 2025 (Wikipedia; TechCrunch, " + NEWS("bench", "Inside the wild fall") + "): a "
         "sale out of a shutdown, so acquired. The prefilled PH was a wrong join."))
L.append(cls("blip-me", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Consumer & Marketplaces", stage="undetermined",
    note="blip.me, asynchronous voice messaging (Walkie Talkie) and audio broadcasts (San Francisco, the firm's 2013 page, "
         + CCPAGE("/portfolio/company/blip.me") + "; Ajay Agarwal, Sahil Gupta). The firm listed it 2013-2015; no source read gives "
         "the round or its fate. Not the same company as blip.tv."))
L.append(cls("blockfi", status="defunct", rng="below_1b", country="US", country_src="model_knowledge", city="Jersey City",
    focus="Crypto & Web3", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("blockfi", "BlockFi confirms $350 million Series D"), entry_date="2021-03",
    note="Crypto lender (Jersey City). BCV joined the $350M Series D at $3B with Tiger Global (The Block, 2021-03-11); the firm listed "
         "it 2021-2022 (Growth, Stefan Cohen). Chapter 11 on 2022-11-28 (" + NEWS("blockfi", "BlockFi files for Chapter 11 bankruptcy")
         + ") and a wind-down of all operations from October 2023, with no sale: defunct."))
L.append(cls("brontes-technologies", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Woburn",
    focus="Healthcare & Bio", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2004",
    note="3D dental imaging (Woburn, MA in the firm's 2006 listing). 'The company was funded in 2004 by David Frankel, Flybridge Capital, "
         "Charles River Ventures, and Bain Capital Ventures' (" + W("Brontes Technologies") + "): its first institutional round, read "
         "as its Series A. 3M acquired it in October 2006 for $95M (Wikipedia; the firm's 2012 page, "
         + CCPAGE("/portfolio/company/brontes-technologies/") + ")."))
L.append(cls("cameo", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Chicago",
    focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CAMEO_B,
    entry_date="2019-06", flags=["model_disputes_source"],
    note="Personalised celebrity video messages (Chicago). 'Cameo Closes $50 Million Series B Round Led by Kleiner Perkins' with Bain "
         "Capital participating (PR Newswire, June 2019); the firm listed it from July 2019 (Jamison Hill). The 2021 $1B figure is "
         "a SoftBank estimate and later collapsed (" + W("Cameo (website)") + "), so below_1b, aligned with Lightspeed and Spark. The "
         "prefilled IT belongs to another Cameo."))
L.append(cls("captora", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", city="San Mateo",
    focus="SaaS", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013",
    note="Digital marketing acceleration software (San Mateo, the firm's page, " + CCPAGE("/portfolio/captora/") + "; Ajay Agarwal). "
         "BCV listed it from October 2013, before 'Captora scores $22M in second round of funding' (Marketing Dive, 2014-05), so BCV "
         "was in its first institutional round, read as its Series A. The firm still showed it Active in 2022; captora.com no longer "
         "resolves and no source read gives its fate."))
L.append(cls("centrepath", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Waltham",
    focus="Data Infrastructure", stage="undetermined",
    note="Optical and storage network management (Waltham, MA). 'CentrePath was acquired by Capital Growth Systems in January 2007' "
         "(the firm's page, " + CCPAGE("/portfolio/company/centrepath/") + "; Ben Nye). Greylock's note names Terremark in 2005; "
         "the status agrees. The round is not named."))

# ---- not venture positions of the firm (other desk) ----
other_desk("ameritrade",
    "Ameritrade has been listed since its March 1997 IPO (" + W("TD Ameritrade") + "); no Bain Capital venture vehicle existed before "
    "1999, so a pre-IPO position was a generalist fund's, and a later one is a public-company holding (T3, D4). The firm's 2006 page "
    "files it under 'Expansion/Growth Buyout' with no IPO date.", conf="high")
other_desk("amr-interactive",
    "AMR Interactive, an online market-research firm in Sydney, Australia (the firm's 2006 page, Midstage).")
other_desk("cameraworld-com",
    "CameraWorld.com, a photography e-commerce retailer funded in 1999 and bought by Ritz Camera (the firm's 2006 page, Irvine, CA, "
    "'Expansion/Growth Buyout').")

if __name__ == "__main__":
    jl.write("batch-006", L)
