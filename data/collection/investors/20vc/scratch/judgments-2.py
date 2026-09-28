"""PRO-76 grind, batch-002 (first pass: status, country, city, focus, band, entry
round and funding history; the S2A column is decided in its own pass after
scripts/graduation-surfaces.py). Evidence: scratch/evidence-pack.json,
scratch/research/*.json (rounds, gap, url-checks); every citation below was
fetched and its sentence read before use (MarketScreener's Nxyz brief through
WebFetch, the rest with verify-url.py). Rulings cited: decisions.md D1-D9, R1.
Also re-records Cognition's entry stage (batch-001b): undetermined, not Growth."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd = jl.cls, jl.rnd
L = []
W = "web_verified"
U = "undetermined"
NOSTAGE = {"entry_stage_source": None, "entry_stage_confidence": None, "entry_stage_citation": None}

# ---- Entire
L.append(cls("entire", status="private", country="US", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="medium", entry_date="2026-02",
    stage_cite="https://techcrunch.com/2026/02/10/former-github-ceo-raises-record-60m-dev-tool-seed-round-at-300m-valuation/",
    flags=["city_unknown"],
    note="Developer platform for AI coding agents (entire.io) of former GitHub CEO Thomas Dohmke. 'The startup, Entire, has raised $60 million at a $300 million valuation' in a seed led by Felicis; 'Other investors in the seed round include Madrona, M12, Basis Set, Harry Stebbings, Jerry Yang' (TechCrunch, 2026-02-10). The line names the founder, not the fund; it dates the entry of a company the firm lists on its 2026 card (decisions.md R1). Same company as the Felicis row. No source read gives an HQ city.",
    rounds=[rnd("2026-02", "seed", 60000000, "Felicis", True, "https://techcrunch.com/2026/02/10/former-github-ceo-raises-record-60m-dev-tool-seed-round-at-300m-valuation/")]))

# ---- Firmable
L.append(cls("firmable", status="private", country="AU", city="Melbourne", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2023", flags=["stage_uncited"],
    note="AI sales-intelligence platform (Melbourne; founded by Leigh Jasper after Aconex). The firm listed Firmable by September 2024 (its card, created 2024-09-12); the only round before then: 'Firmable raised $9 million in a 2023 seed funding round led by AirTree' (SmartCompany, 2025-12-02). No report names 20VC in it, so Seed is inferred from the listing date (model, low). The $14M Series A of March 2026 led by AirTree 'with participation from existing investors' (PR Newswire, 2026-03-02) follows.",
    rounds=[rnd("2023", "seed", None, "AirTree Ventures", None, "https://www.smartcompany.com.au/business-advice/aconex-firmable-founder-leigh-jasper-headline-growth-summit-melbourne/"),
            rnd("2026-03", "Series A", None, "AirTree Ventures", None, "https://www.prnewswire.com/news-releases/firmable-raises-14m-series-a-to-take-ai-native-sales-platform-global-302700754.html")]))

# ---- Flare
L.append(cls("flare", status="private", country="DK", city="Copenhagen", focus="AI & Applied AI", rng="below_1b",
    stage="Pre-Seed", stage_src=W, stage_conf="high", entry_date="2026-04",
    stage_cite="https://arcticstartup.com/flare-raises-e3-6m-pre-seed/",
    note="Community-notes style verification layer for AI-era knowledge (flare.co, Copenhagen). 'Copenhagen-based Flare has raised EUR 3.6 million in pre-seed funding ... The round was led by 20VC and 20Growth, with participation from byFounders' (ArcticStartup, 2026-05-01; EU-Startups reported it 2026-04-16). 20VC's own fund leads beside the 20Growth offshoot (decisions.md D1).",
    rounds=[rnd("2026-04", "pre-seed", None, "20VC, 20Growth", True, "https://arcticstartup.com/flare-raises-e3-6m-pre-seed/")]))

# ---- Fuse Energy ($1B+: visible)
L.append(cls("fuse-energy", status="private", country="GB", country_src=W,
    country_cite="https://techfundingnews.com/fuse-energy-hits-profitability-with-550m-revenue-run-rate-as-it-challenges-britains-energy-giants/",
    city="London", focus="Climate & Energy", rng="1b_plus", usd=5000000000, val_src=W, asof="2025-12-18",
    val_cite="https://www.balderton.com/news/fuse-energy-hits-5bn-valuation-in-its-third-year/",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2026-06",
    stage_cite="https://techfundingnews.com/fuse-energy-hits-profitability-with-550m-revenue-run-rate-as-it-challenges-britains-energy-giants/",
    note="Vertically integrated renewable energy supplier and developer (London; Tesseract until 2023). 'Fuse Energy has closed an extension to its Series B round, securing an additional $30 million from 20VC and Collaborative Fund. The new investors join existing backers Balderton Capital and Lowercarbon Capital' (Tech Funding News, 2026-06-05): 20VC enters in a Series B extension, so Growth. Mark: 'Fuse Energy hits $5bn valuation' on the $70M Series B (Balderton's post, 2025-12-18), as in the Balderton row; the Creandum row still reads below_1b, the stale side.",
    rounds=[rnd("2022-09", "seed", 78000000, "Balderton Capital, Lakestar", None, None),
            rnd("2025-12", "Series B", 70000000, "Balderton Capital, Lowercarbon Capital", None, "https://www.balderton.com/news/fuse-energy-hits-5bn-valuation-in-its-third-year/"),
            rnd("2026-06", "Series B extension", 30000000, "20VC, Collaborative Fund", True, "https://techfundingnews.com/fuse-energy-hits-profitability-with-550m-revenue-run-rate-as-it-challenges-britains-energy-giants/")]))

# ---- Fyxer
L.append(cls("fyxer", status="private", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2025-03",
    stage_cite="https://www.uktechnews.info/2025/03/17/fyxer-ai-secures-7-7-million-investment-led-by-20vc/",
    note="AI assistant for email and meetings (London). '$10M Series A funding is led by Harry Stebbings' 20VC'; 'The round was led by 20VC, with participation from Marc Benioff (Salesforce), Christian Reber (Pitch) ... 20Growth, 20Product' (UK Tech Investment News, 2025-03-17). $30M Series B led by Madrona (Tech Funding News, 2025-09-09).",
    rounds=[rnd("2025-03", "Series A", 10000000, "20VC", True, "https://www.uktechnews.info/2025/03/17/fyxer-ai-secures-7-7-million-investment-led-by-20vc/"),
            rnd("2025-09", "Series B", 30000000, "Madrona", None, "https://techfundingnews.com/startup-in-spotlight-fyxer-ai-raises-30m-to-bring-ai-productivity-assistants-to-everyday-professionals/")]))

# ---- General Index
L.append(cls("general-index", status="private", country="GB", city="London", focus="Fintech & Payments", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2024-02",
    stage_cite="https://businesscloud.co.uk/news/gx-investment-to-accelerate-renewable-energy-transition/",
    note="Energy and commodity price benchmarks (General Index, GX; London). 'General Index has completed a GBP 9.5 million Series A funding round ... Investment firm 20VC - chaired by Harry Stebbings - led the funding round, with follow-on investment from Chalfen Ventures' (BusinessCloud, 2024-02-01); the previous round (2021) names no 20VC.",
    rounds=[rnd("2021", "earlier round", None, None, None, None),
            rnd("2024-02", "Series A", None, "20VC", True, "https://businesscloud.co.uk/news/gx-investment-to-accelerate-renewable-energy-transition/")]))

# ---- Grand (not the Wikidata join)
L.append(cls("grand", status="private", country="IE", city="Dublin", focus="Fintech & Payments", rng="below_1b",
    stage="Pre-Seed", stage_src=W, stage_conf="high", entry_date="2026-03",
    stage_cite="https://www.siliconrepublic.com/start-ups/dublins-grand-raises-5m-pre-seed-for-real-world-payment-network-fintech",
    flags=["model_disputes_source"], extra={"valuation_source": None, "valuation_range_source": None},
    note="AI payment and trust network for construction, manufacturing and trade supply (heygrand.com, Dublin). 'Dublin's Grand has raised $5m in a pre-seed funding round led by 20VC, with participation from NAP and Firedrop' (Silicon Republic, 2026-03-26; FinTech Global the same day). The Wikidata pre-fill (a Swedish Grand acquired by Svenska Bio) is a different company: disputed.",
    rounds=[rnd("2026-03", "pre-seed", 5000000, "20VC", True, "https://www.siliconrepublic.com/start-ups/dublins-grand-raises-5m-pre-seed-for-real-world-payment-network-fintech")]))

# ---- Handly (co-led with Stride.VC; 20VC's own position: D4)
L.append(cls("handly", status="private", country="DE", city="Berlin", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2024",
    stage_cite="https://www.businessinsider.de/gruenderszene/business/pitchdeck-handly/",
    note="Operating software and payments for trades and service businesses (Berlin). 'in der Seed-Runde 3,75 Millionen Euro einsammeln. Angefuehrt wurde die Runde von Stride VC und 20VC aus Grossbritannien' (Gruenderszene); deutsche-startups' Dealmonitor of 2025-02-19 lists Stride.VC, 20VC, Base10 Partners and The Delta in the EUR 3.75M. The firm's card existed by 2024-09-12, so the seed closed in 2024, before its February 2025 announcement. The pre-seed of September 2022 (EUR 1.5M, led by The Delta; Tech.eu, 2022-09-13) names no 20VC. Stride.VC is another firm (decisions.md D4); 20VC co-led in its own name.",
    rounds=[rnd("2022-09", "pre-seed", None, "The Delta", None, "https://tech.eu/2022/09/13/berlin-based-handly-scores-eur15-million-to-bring-payments-solutions-to-5-trillion-home-improvement-market/"),
            rnd("2025-02", "seed", None, "Stride.VC, 20VC", True, "https://www.businessinsider.de/gruenderszene/business/pitchdeck-handly/")]))

# ---- Hopin
L.append(cls("hopin", status="acquired", country="GB", city="London", focus="SaaS", rng="below_1b",
    stage=U, extra=NOSTAGE,
    note="Virtual events platform (London). Fund I, the $8.3M micro fund begun in April 2020, 'has made investments in several companies ... including Hopin and social media app Clubhouse' (Fortune, 2021-06-16), so the position is 20VC's own, not Harry Stebbings' personal book (decisions.md D3). Every round from April 2020 (the $40M Series A of June 2020, the Series B to D of 2020-21) could have been Fund I's and no source names it: undetermined. The events business went to RingCentral (2023) and StreamYard to Bending Spoons: acquired, as in the a16z, Accel, Coatue, General Catalyst and IVP rows."))

# ---- kevin. (defunct; the Accel row is the stale side)
L.append(cls("kevin", status="defunct", country="LT", city="Vilnius", focus="Fintech & Payments", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="medium", entry_date="2022-05",
    stage_cite="https://arcticstartup.com/kevin-raised-65m-series-a/",
    note="Account-to-account payments infrastructure (Vilnius). The $65M Series A of May 2022 led by Accel: 'Additional investors in the round include Harry Stebbings, Founder of 20VC, Ilkka Paananen ... and other angel investors' (ArcticStartup and TechRound, 2022-05-04). The line names the founder, not the fund; it dates the entry of a company the firm listed as its own (its site, 2022-08; decisions.md R1). 'Fintech kevin declared insolvent by Vilnius court': the court initiated bankruptcy proceedings and appointed an insolvency administrator (The Paypers, September 2024), and the Bank of Lithuania revoked the payment-institution licence of Kevin EU (October 2024): defunct. The Accel row still reads private, the stale side.",
    rounds=[rnd("2022-05", "Series A", 65000000, "Accel", True, "https://arcticstartup.com/kevin-raised-65m-series-a/"),
            rnd("2024-09", "insolvency proceedings", None, None, None, "https://thepaypers.com/fintech/news/fintech-kevin-declared-insolvent-by-vilnius-court")]))

# ---- La Fraise
L.append(cls("la-fraise", status="private", country="FR", city="Paris", focus="Healthcare & Bio", rng="below_1b",
    stage=U, extra=NOSTAGE, entry_date="2025-11",
    note="AI agents for dental practices (lafraise.pro, Paris; founded 2025 by former Doctolib staff). 'La societe annonce aujourd'hui une premiere levee de fonds de 3,2 millions d'euros aupres de 20VC, Seedcamp, Kima Ventures et Bpifrance' (Maddyness, 2025-11-17; Seedcamp's post the same day). Its first round, but no report names it pre-seed or seed: undetermined.",
    rounds=[rnd("2025-11", "first round", None, "20VC", True, "https://www.maddyness.com/2025/11/17/des-anciens-de-doctolib-misent-sur-lia-pour-ameliorer-lacces-aux-soins-dentaires/")]))

# ---- Linear ($1B+: visible)
L.append(cls("linear", status="private", country="US", city="San Francisco", focus="SaaS", rng="1b_plus", usd=1250000000, val_src=W,
    asof="2025-06-10", val_cite="https://techcrunch.com/2025/06/10/atlassian-rival-linear-raises-82m-at-1-25b-valuation/",
    stage=U, extra=NOSTAGE,
    note="Issue tracking and product development (San Francisco). 20VC names Linear among its backed companies in its own boilerplate ('20VC has backed companies such as Perplexity, Linear, 11x, Deblock and Captions', UK Tech Investment News, 2025-03-17) and lists it on its card; no source names the round. The seed (Sequoia, November 2019) predates the funds; the Series A (Sequoia), the $35M Series B (Accel, 2023) and the $82M Series C (Accel, June 2025) fall inside their life: undetermined. Mark: '$82M at $1.25B valuation' (TechCrunch, 2025-06-10), as in the Accel and Sequoia rows.",
    rounds=[rnd("2019-11", "seed", 4200000, "Sequoia Capital", None, None),
            rnd("2023-09", "Series B", 35000000, "Accel", None, None),
            rnd("2025-06", "Series C", 82000000, "Accel", None, "https://techcrunch.com/2025/06/10/atlassian-rival-linear-raises-82m-at-1-25b-valuation/")]))

# ---- Lovable ($10B+: visible)
L.append(cls("lovable", status="private", country="SE", country_src=W,
    country_cite="https://techcrunch.com/2025/07/17/lovable-becomes-a-unicorn-with-200m-series-a-just-8-months-after-launch/",
    city="Stockholm", focus="AI & Applied AI", rng="10b_plus", usd=13300000000, val_src=W, asof="2026-08-12",
    val_cite="https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/",
    stage="Pre-Seed", stage_src="model", stage_conf="low", entry_date="2024-10",
    flags=["stage_uncited"], clear=["needs_web_value", "unicorn_name_match"],
    note="AI app builder (Stockholm). 'The Series A saw participation from existing investors, which include 20VC, byFounders, Creandum, Hummingbird, and Visionaries Club' (TechCrunch, 2025-07-17), so 20VC entered before July 2025: at the EUR 6.8M pre-seed of October 2024 led by Hummingbird and byFounders, or the $15M pre-Series A of February 2025 led by Creandum, whose report names Visionaries Club and angels but not 20VC (TechCrunch, 2025-02-25). By that elimination Pre-Seed (model, low). Mark: '$13.3B valuation' on the $400M Series C (TechCrunch, 2026-08-12), as in the Accel, Balderton, Creandum, Khosla and Menlo rows.",
    rounds=[rnd("2024-10", "pre-seed", None, "Hummingbird Ventures, byFounders", None, None),
            rnd("2025-02", "pre-Series A", 15000000, "Creandum", None, "https://techcrunch.com/2025/02/25/swedens-lovable-an-app-building-ai-platform-rakes-in-16m-after-spectacular-growth"),
            rnd("2025-07", "Series A", 200000000, "Accel", True, "https://techcrunch.com/2025/07/17/lovable-becomes-a-unicorn-with-200m-series-a-just-8-months-after-launch/"),
            rnd("2025-12", "Series B", 330000000, "Menlo Ventures, CapitalG", None, None),
            rnd("2026-08", "Series C", 400000000, "Menlo Ventures", None, "https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/")]))

# ---- Lupin & Holmes
L.append(cls("lupin-holmes", status="private", country="FR", city="Paris", focus="Security", rng="below_1b",
    stage="Pre-Seed", stage_src=W, stage_conf="high", entry_date="2026-03",
    stage_cite="https://tech.eu/2026/03/17/young-bug-bounty-hunter-bags-6m-pre-seed-round-for-security-startup/",
    note="AI for software supply-chain security (landh.tech, Paris). The $6M pre-seed: Lupin & Holmes 'has captured lead investment from Harry Stebbings' 20VC and Seedcamp' (Tech.eu, 2026-03-17); co-led by 20VC and Seedcamp with Purple Fund and Kima Ventures (Silicon.fr, EUR 5.9M).",
    rounds=[rnd("2026-03", "pre-seed", 6000000, "20VC, Seedcamp", True, "https://tech.eu/2026/03/17/young-bug-bounty-hunter-bags-6m-pre-seed-round-for-security-startup/")]))

# ---- Mercor ($10B+: visible)
L.append(cls("mercor", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="10b_plus", usd=10000000000, val_src=W,
    asof="2025-10-27", val_cite="https://techcrunch.com/2025/10/27/mercor-quintuples-valuation-to-10b-with-350m-series-c/",
    stage=U, extra=NOSTAGE, flags=["model_disputes_source"], clear=["needs_web_value", "unicorn_name_match"],
    note="Expert marketplace supplying AI labs (San Francisco; the Wikidata join to a Latvian entity is a namesake, disputed as in the Felicis and Menlo rows). The firm lists Mercor on its 2026 card and Harry Stebbings speaks as an investor on the 20VC x SaaStr episode of August 2026; the press otherwise pairs Mercor with 20VC through the podcast (decisions.md D7), and no source names the round: undetermined. Mark: 'Mercor quintuples valuation to $10B with $350M Series C' (TechCrunch, 2025-10-27), as in the Benchmark, Felicis, General Catalyst and Menlo rows; a round at $20B was only in talks in August 2026.",
    rounds=[rnd("2023", "seed", None, "General Catalyst", None, None),
            rnd("2024-09", "Series A", 32000000, "Benchmark", None, None),
            rnd("2025-02", "Series B", 100000000, "Felicis", None, None),
            rnd("2025-10", "Series C", 350000000, "Felicis", None, "https://techcrunch.com/2025/10/27/mercor-quintuples-valuation-to-10b-with-350m-series-c/")]))

# ---- Nex Health ($1B+: visible)
L.append(cls("nex-health", status="private", country="US", city="San Francisco", focus="Healthcare & Bio", rng="1b_plus", usd=1000000000, val_src=W,
    asof="2022-04-21", val_cite="https://www.nexhealth.com/resources/series-c",
    stage=U, extra=NOSTAGE, entry_date="2020", flags=["stale"],
    note="Patient-experience platform and healthcare API (NexHealth, San Francisco). 'Backing the company is a collection of super angels, including ... Harry Stebbings, from The Twenty Minute VC' (TechCrunch, 2020-06-30), on $12 million raised by then: a founder-level line for a company the firm listed as its own (its site, 2022-2023; decisions.md R1), dated in Fund I's first months. The article names no round and nothing says whether the check was in the September 2019 seed Point Nine led or the 2020 round: undetermined. Mark: 'NexHealth Raises $125M Series C at $1B Valuation' (the company, 2022-04-21), as in the Point Nine row; older than 24 months (stale).",
    rounds=[rnd("2019-09", "seed", 3300000, "Point Nine", None, None),
            rnd("2020", "round (Form D, 2020 Q3)", 15000000, None, None, None),
            rnd("2022-04", "Series C", 125000000, "Buckley Ventures", None, "https://www.nexhealth.com/resources/series-c")]))

# ---- Nxyz (acquired; the Sequoia row is the stale side)
L.append(cls("nxyz", status="acquired", country="US", focus="Crypto & Web3", rng="below_1b",
    stage=U, extra=NOSTAGE, flags=["city_unknown"],
    note="Blockchain indexing and data API (nxyz). Its one disclosed round, $40M led by Paradigm (October 2022, with Coinbase Ventures, Greylock and Sequoia; DailyCoin), names no 20VC in the reports read, and the firm's 2026 card lists it with an exit flag: undetermined. 'Snowflake Inc. entered into a definitive agreement to acquire NXYZ, Inc.' (MarketScreener, 2023-07-26; the nxyz API was retired on 2023-08-23): acquired. The Sequoia row still reads private, the stale side. Split London/US team; no single city.",
    rounds=[rnd("2022-10", "Series A", 40000000, "Paradigm", None, "https://dailycoin.com/nxyz-raises-40m-to-unlock-faster-blockchain-indexing/"),
            rnd("2023-07", "acquisition by Snowflake", None, "Snowflake", None, "https://www.marketscreener.com/quote/stock/SNOWFLAKE-INC-112440376/news/Snowflake-Inc-entered-into-a-definitive-agreement-to-acquire-NXYZ-Inc-44572045/")]))

# ---- Omada (not Omada Health)
L.append(cls("omada", status="private", country="FR", city="Bordeaux", focus="Media, Gaming & Advertising", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2023-09",
    stage_cite="https://gamesbeat.com/omada-raises-7-5m-for-social-prediction-game-for-sports-fans/",
    note="Free social sports-prediction game (omadagame.com; 'a French company that Miniatti founded in Bordeaux in 2021'). The $7.5M seed: 'London-based Felix Capital led the round, with participation from investors including 20VC, Play Ventures, F4, Motier Ventures' (GamesBeat, 2023-09-27), quoting Harry Stebbings as 20VC's founder. 20VC's own position in the round, not Julien Codorniou's (then at Felix; decisions.md D8).",
    rounds=[rnd("2023-09", "seed", 7500000, "Felix Capital", True, "https://gamesbeat.com/omada-raises-7-5m-for-social-prediction-game-for-sports-fans/")]))

# ---- Ostrich (shut down 2026)
L.append(cls("ostrich", status="defunct", country="GB", city="London", focus="Consumer & Marketplaces", rng="below_1b",
    stage=U, extra=NOSTAGE,
    note="Off-market property marketplace (ostrich.co.uk, London; founded 2021 by the VoucherCodes founders). 'The startup raised $3.98m in early-stage funding, with investment coming from Stebbings' 20VC and proptech Era Ventures, according to PitchBook'; 'A London-based proptech startup ... has shut down' (Tech.eu, 2026-09-09): defunct. No report names the round 20VC joined: undetermined.",
    rounds=[rnd("2026-09", "shut down", None, None, None, "https://tech.eu/2026/09/09/harry-stebbings-backed-proptech-ostrich-shuts")]))

# ---- Pachama (acquired 2025)
L.append(cls("pachama", status="acquired", country="US", city="San Francisco", focus="Climate & Energy", rng="below_1b",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2022-05",
    stage_cite="https://agfundernews.com/pachama-nets-55m-series-b-to-boost-accountability-in-forest-carbon-markets",
    note="Forest-carbon measurement, reporting and verification (San Francisco). The $55M Series B: 'New investors include ... Harry Stebbings' 20VC, and Reddit founder Alexis Ohanian' (AgFunderNews, 2022-05-05): 20VC enters at the B, so Growth. 'Carbon Direct is acquiring Pachama' (Carbon Direct's post, November 2025): acquired, as in the YC row.",
    rounds=[rnd("2022-05", "Series B", 55000000, None, True, "https://agfundernews.com/pachama-nets-55m-series-b-to-boost-accountability-in-forest-carbon-markets"),
            rnd("2025-11", "acquisition by Carbon Direct", None, "Carbon Direct", None, "https://www.carbon-direct.com/insights/carbon-direct-acquires-pachama")]))

# ---- Payflows
L.append(cls("payflows", status="private", country="FR", city="Paris", focus="Fintech & Payments", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2022-10", flags=["stage_uncited"],
    note="Finance-operations platform (Paris). At the EUR 25M Series A led by Balderton (April 2024) 20VC is an existing investor: 'participation from existing investors including Ribbit Capital, Headline, 20VC and the family offices of Plaid's founder and Galeries Lafayette' (Tech.eu, 2024-04-22). The only earlier round is the $5.5M first round of October 2022 co-led by Headline and Ribbit (the Headline row), so Seed (model, low; no report of that round naming 20VC was found).",
    rounds=[rnd("2022-10", "seed", 5500000, "Headline, Ribbit Capital", None, None),
            rnd("2024-04", "Series A", None, "Balderton Capital", True, "https://tech.eu/2024/04/22/saas-payflows-raises-25m-series-a/")]))

# ---- Pearl (heypearl.ai; not YC's Pearl)
L.append(cls("pearl", status="private", country="FR", city="Paris", focus="AI & Applied AI", rng="below_1b",
    stage=U, extra=NOSTAGE, flags=["identity_homonym", "model_disputes_source"],
    note="AI workspace for sales teams (heypearl.ai), founded in Paris by former Pigment sales leaders. Its own site quotes 'we're proud at 20VC to be backing them. Julien Codorniou, 20VC' and signs 'With love from Paris'. A first round of about $1.4M led by 20VC with Sunrise and Kima Ventures is reported, but no page read in this run names the round: undetermined. Not YC's Pearl (a W17 industrial company; ruled distinct in companies/cross-rulings.json) and not the Wikidata join (Suriname, disputed)."))

# ---- Peec AI
L.append(cls("peec-ai", status="private", country="DE", city="Berlin", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2025-07",
    stage_cite="https://tech.eu/2025/07/02/peec-ai-raises-eur7m-to-empower-companies-to-improve-their-visibility-through-ai-search/",
    note="AI-search visibility analytics for marketing teams (Berlin). 'The seed round was led by early-stage venture firm 20VC, with participation from Antler' (Tech.eu, 2025-07-02; EUR 5.2M, weeks after a EUR 1.8M pre-seed in April). 'Just four months after its seed round led by 20VC, the Berlin-based startup has raised a $21 million Series A led by ... Singular' (TechCrunch, 2025-11-17).",
    rounds=[rnd("2025-04", "pre-seed", None, None, None, None),
            rnd("2025-07", "seed", None, "20VC", True, "https://tech.eu/2025/07/02/peec-ai-raises-eur7m-to-empower-companies-to-improve-their-visibility-through-ai-search/"),
            rnd("2025-11", "Series A", 21000000, "Singular", None, "https://techcrunch.com/2025/11/17/as-consumers-ditch-google-for-chatgpt-peec-ai-raises-21m-to-help-brands-adapt/")]))

# ---- Poolside ($10B+: visible)
L.append(cls("poolside", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="10b_plus", usd=12000000000, val_src=W,
    asof="2026-08-24", val_cite="https://www.saastr.com/20vc-x-saastr-nvidia-pays-6b-for-poolsides-model-factory-openai-has-to-go-public-in-2027-and-why-9b-no-longer-clears-the-bar-for-seed/",
    stage="Seed", stage_src=W, stage_conf="medium", entry_date="2023-08",
    stage_cite="https://www.saastr.com/20vc-x-saastr-nvidia-pays-6b-for-poolsides-model-factory-openai-has-to-go-public-in-2027-and-why-9b-no-longer-clears-the-bar-for-seed/",
    note="AI for software development (Poolside, San Francisco with a Paris branch). The firm states its own position: 'Harry, a Poolside shareholder, said the outcome is roughly a 15x for them as a seed investor' (SaaStr's write-up of the 20VC x SaaStr episode, 2026-08-27), the $126M seed Redpoint led in August 2023 (the Redpoint and Bain Capital Ventures rows). This is the firm describing its holding, not a guest or sponsor relationship (decisions.md D7). Mark: Nvidia 'separately investing $1B at a $12B pre-money valuation' beside a $6B licence of the Model Factory, 'not an acquisition and not an acquihire' (same write-up; Forbes, 2026-08-24), as in the Bain Capital Ventures, Felicis and Point Nine rows.",
    rounds=[rnd("2023-08", "seed", 126000000, "Redpoint Ventures", True, None),
            rnd("2024-10", "Series B", 500000000, "Bain Capital Ventures", None, None),
            rnd("2026-08", "Nvidia investment at $12B pre-money", 1000000000, "Nvidia", None, "https://www.saastr.com/20vc-x-saastr-nvidia-pays-6b-for-poolsides-model-factory-openai-has-to-go-public-in-2027-and-why-9b-no-longer-clears-the-bar-for-seed/")]))

# ---- Popup
L.append(cls("popup", status="private", country="US", focus="SaaS", rng="below_1b",
    stage="Pre-Seed", stage_src=W, stage_conf="high", entry_date="2022",
    stage_cite="https://techcrunch.com/2022/11/22/popup-merchants-no-code-storefront/",
    flags=["city_unknown"],
    note="No-code storefront personalization for online merchants (Popup; founders Holmes and Grassi). 'Popup raised $3.5 million in a pre-seed round ... The round was led by Accel and included Seedcamp, 20VC and a group of angels' (TechCrunch, 2022-11-22). 20VC's page for Popup was posted on 2022-01-24, so the round closed before its announcement: entry 2022. No source read gives an operating city (the Accel row's Claymont, Delaware reads as a filing address).",
    rounds=[rnd("2022", "pre-seed", 3500000, "Accel", True, "https://techcrunch.com/2022/11/22/popup-merchants-no-code-storefront/")]))

# ---- Qogita
L.append(cls("qogita", status="private", country="GB", city="London", focus="Consumer & Marketplaces", rng="below_1b",
    stage=U, extra=NOSTAGE,
    note="Wholesale procurement marketplace (London and Amsterdam). The firm listed Qogita on its site from 2022-08-03. Qogita built in stealth from 2021 on a seed co-led by LocalGlobe and Bessemer and a Series A led by Accel, then raised a EUR 80M Series B led by Dawn Capital ('Qogita secures GBP 69 million Series B', UK Tech Investment News, 2023-12-14); no source names 20VC's round: undetermined.",
    rounds=[rnd("2023-12", "Series B", None, "Dawn Capital", None, "https://www.uktechnews.info/2023/12/14/qogita-secures-69-million-series-b-investment-led-by-dawn-capital/")]))

# ---- Random Walk (identity unresolved)
L.append(cls("random-walk", status="unknown", country="GB", country_src="model_knowledge", rng=U, stage=U, grad=U, focus=None,
    flags=["identity_unresolved", "country_prior", "city_unknown"],
    extra={"hq_country_confidence": "low"},
    note="The firm's card reads 'Stealth...' (sectors AI and Consumer, created 2024-09-12) and links randomwalk.ai. The company at that domain today sells enterprise AI solutions ('Advanced AI Solutions for Modern Enterprises', read 2026-09-28), not a stealth consumer product, and its pages name no investor; a vendor profile of it lists 20VC, most likely matched from the card's domain. No source ties 20VC to a named Random Walk: every outcome column undetermined; country is the firm's desk prior (London)."))

# ---- Remote ($1B+: visible)
L.append(cls("remote-com", status="private", country="US", city="San Francisco", focus="SaaS", rng="1b_plus", usd=3000000000, val_src=W,
    asof="2022-04-05", val_cite="https://techcrunch.com/2022/04/05/remote-payroll-hr-workforce-3-billion/",
    stage=U, extra=NOSTAGE, flags=["stale"],
    note="Global employment and payroll platform (Remote, remote.com; US-incorporated and fully distributed, San Francisco as in the Accel, General Catalyst and Sequoia rows). The firm listed it on its site in 2022; no source names 20VC's round, and the $35M Series A (November 2020), the $150M Series B (July 2021) and the Series C (April 2022) all fall inside the funds' life: undetermined. Mark: 'This Series C values Remote at over $3 billion' (TechCrunch, 2022-04-05), older than 24 months (stale). Published as 'Remote'.",
    rounds=[rnd("2020-11", "Series A", 35000000, None, None, None),
            rnd("2021-07", "Series B", 150000000, "Accel", None, None),
            rnd("2022-04", "Series C", 300000000, None, None, "https://techcrunch.com/2022/04/05/remote-payroll-hr-workforce-3-billion/")]))

# ---- Requesty
L.append(cls("requesty", status="private", country="GB", city="London", focus="DevTools & APIs", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2025-09",
    stage_cite="https://www.businessinsider.com/pitch-deck-ai-startup-requesty-seed-2025-9",
    note="Unified LLM gateway for developers (London; pivoted from data analytics in 2025). 'Requesty announced on Friday that it had raised a $3 million seed investment round, led by 20VC and with participation from venture capital firms Tapestry VC, Insiders Ventures, and Tiny Supercomputer' (Business Insider, 2025-09-26).",
    rounds=[rnd("2025-09", "seed", 3000000, "20VC", True, "https://www.businessinsider.com/pitch-deck-ai-startup-requesty-seed-2025-9")]))

# ---- Rivan
L.append(cls("rivan", status="private", country="GB", city="London", focus="Climate & Energy", rng="below_1b",
    stage=U, extra=NOSTAGE, entry_date="2025-05",
    note="Solar-powered synthetic fuel plants (London; factory in Bermondsey). 'London-based climatetech Rivan has raised GBP 10 million in a funding round led by Plural, with participation from 20VC, Nat Friedman and Daniel Gross (NFDG), and angel investors Patrick and John Collison' (Tech.eu, 2025-05-21; UKTN and BusinessCloud the same day). No report names the round: undetermined.",
    rounds=[rnd("2025-05", "unnamed round", None, "Plural", True, "https://tech.eu/2025/05/21/uk-based-rivan-raises-ps10m-to-scale-solar-powered-synthetic-fuel-plants-for-heavy-industry/")]))

# ---- Roadflex (formerly Fygo)
L.append(cls("roadflex", status="private", country="US", city="San Francisco", focus="Fintech & Payments", rng="below_1b",
    stage=U, extra=NOSTAGE,
    note="Fuel card and expense platform for trucking fleets (RoadFlex, formerly Fygo; San Francisco). 20VC's page 'Roadflex' (at /portfolio/fygo/, posted 2022-01-24) lists it; vendor profiles date an October 2021 round with 20VC among about $4M raised, but no report names 20VC or the round: undetermined."))

# ---- Roam = Roam Research (not ro.am, the IVP row)
L.append(cls("roam", status="private", country="US", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2020-09",
    flags=["identity_homonym", "city_unknown", "model_disputes_source", "stage_uncited"],
    note="Networked note-taking (Roam Research, roamresearch.com). The firm's page 'Roam' was posted on 2022-08-03 beside Fund I's US companies. It is not Howard Lerman's virtual office Roam (ro.am, the IVP row): that company emerged from stealth in November 2022, its first outside money was the IVP Series A (IVP's row dates it 2022-09) and 'He also contributed $10.6 million of his own money' (CNBC, 2022-11-02). Roam Research's only round is the $9M seed at a $200M valuation of September 2020, inside Fund I's life, and vendor profiles list 20VC among its investors (not a citation): Seed at low confidence. Wikidata's GB is a namesake, disputed. Published as 'Roam Research'; ruled distinct from the IVP row in companies/cross-rulings.json.",
    rounds=[rnd("2020-09", "seed", 9000000, None, None, None)]))

# ---- ScorePlay
L.append(cls("scoreplay", status="private", country="US", city="New York", focus="SaaS", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2025-02",
    stage_cite="https://www.sportico.com/business/finance/2025/giannis-antetokounmpo-scoreplay-investment-1234827333/",
    note="AI media asset management for sports organisations (ScorePlay; founded 2021 by Victorien Tixier and Xavier Green; its Series A release is datelined New York City, Lisbon-based at its 2023 seed). 'The Series A funding round just closed is led by 20VC' (Sportico, 2025-02-11; $13M; the company's release: 'Led by Harry Stebbings' 20VC'). The $5M seed of 2023 named Seven Seven Six, 35V and athletes, not 20VC, so the entry is the Series A.",
    rounds=[rnd("2023", "seed", 5000000, None, None, None),
            rnd("2025-02", "Series A", 13000000, "20VC", True, "https://www.scoreplay.io/blog/scoreplay-raises-13-million-series-a-funding")]))

# ---- Slay (renamed Born)
L.append(cls("slay", status="private", country="DE", city="Berlin", focus="Media, Gaming & Advertising", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2023-01",
    stage_cite="https://www.deutsche-startups.de/2025/09/11/dealmonitor-born-gcs-hive-robotics/",
    flags=["model_disputes_source"],
    note="Social app studio (Slay, renamed Born in 2025; Berlin). 'Accel, 20VC, Ilkka Paananen, Scott Belsky ... investieren 2,63 Millionen US-Dollar in Slay' (deutsche-startups, 2023-01-19), the round Accel calls its seed: 'Accel unterstuetzt die Jungfirma bereits seit der Seed-Investmentrunde im Jahre 2023. Zu den weiteren Investoren gehoeren unter anderem 20VC' (deutsche-startups, 2025-09-11, on Born's $15M round with Tencent and Laton Ventures). Berlin, not the Wikidata US (disputed).",
    rounds=[rnd("2023-01", "seed", 2630000, "Accel", True, "https://www.deutsche-startups.de/2023/01/19/dealmonitor-awork/"),
            rnd("2025-09", "round", 15000000, "Accel, Tencent, Laton Ventures", None, "https://www.deutsche-startups.de/2025/09/11/dealmonitor-born-gcs-hive-robotics/")]))

# ---- Solve Intelligence
L.append(cls("solve-intelligence", status="private", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2025-04",
    stage_cite="https://techcrunch.com/2025/04/09/microsoft-backs-solve-intelligence-in-12m-series-a-funding/",
    note="AI for patent drafting and prosecution (London; YC S23). 'The startup has raised $12 million in a Series A funding round, led by 20VC' (TechCrunch, 2025-04-09), with Microsoft's M12, Thomson Reuters Ventures and existing investor Y Combinator; 20VC's first round in the company.",
    rounds=[rnd("2025-04", "Series A", 12000000, "20VC", True, "https://techcrunch.com/2025/04/09/microsoft-backs-solve-intelligence-in-12m-series-a-funding/")]))

# ---- Sphere (the tax-compliance Sphere)
L.append(cls("sphere", status="private", country="US", city="San Francisco", focus="Fintech & Payments", rng="below_1b",
    stage=U, extra=NOSTAGE, flags=["model_disputes_source"],
    note="AI-native global tax compliance (Sphere, YC W22; San Francisco), the company of the firm's card ('Global tax compliance'); it began as an ed-tech marketplace. Its $21M Series A led by a16z (TechCrunch, 2025-11-18) names Y Combinator and Felicis; no source names 20VC's round: undetermined. Same company as the Felicis and YC rows; the General Catalyst row names no company (status unknown) and the a16z row is unresolved. Wikidata's JP is a namesake, disputed.",
    rounds=[rnd("2022", "seed", 4300000, None, None, None),
            rnd("2025-11", "Series A", 21000000, "a16z", None, "https://techcrunch.com/2025/11/18/a16z-leads-21m-series-a-into-tax-compliance-platform-sphere/")]))

# ---- SuperMe
L.append(cls("superme", status="private", country="US", city="San Francisco", focus="Consumer & Marketplaces", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2025-11", flags=["stage_uncited"],
    note="AI-native professional network of expert AI profiles (SuperMe; Casey Winters and Ludo Antonov). Its one disclosed round is the $6.8M seed led by Greylock ('we're excited to share our Seed investment in SuperMe', Greylock, 2025-11-11; Upstarts Media the same day), whose reports name no 20VC; the firm listed SuperMe by March 2026 with no later round known: Seed at low confidence.",
    rounds=[rnd("2025-11", "seed", 6800000, "Greylock", None, "https://greylock.com/blog/introducing-superme-the-ai-native-professional-network/")]))

# ---- TechWolf (Stride.VC's and Felix's positions are theirs: D4, D8)
L.append(cls("techwolf", status="private", country="BE", city="Ghent", focus="AI & Applied AI", rng="below_1b",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2024-06",
    stage_cite="https://techcrunch.com/2024/06/24/techwolf-raises-43m-to-take-an-ai-sized-bite-out-of-the-internal-recruiting-game/",
    note="Skills-inference AI for enterprise HR (Ghent). The $42.75M Series B led by Felix Capital: 'Other backers include Acadian Ventures, Fortino Capital Partners, Notion Capital, SemperVirens and 20VC' (TechCrunch, 2024-06-24). Julien Codorniou led it for Felix (decisions.md D8) and Stride.VC's earlier position is Stride's (D4); 20VC's own position is in this round, so Growth.",
    rounds=[rnd("2024-06", "Series B", 42750000, "Felix Capital", True, "https://techcrunch.com/2024/06/24/techwolf-raises-43m-to-take-an-ai-sized-bite-out-of-the-internal-recruiting-game/")]))

# ---- TheyDo
L.append(cls("theydo", status="private", country="NL", city="Amsterdam", focus="SaaS", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2022-12",
    stage_cite="https://tech.eu/2022/12/13/theydo-raises-12-million/",
    note="Customer journey management platform (Amsterdam). 'The EUR 12 million Series A round was led by Blossom Capital, with 20VC and a host of angel investors including Des Traynor' (Tech.eu, 2022-12-13).",
    rounds=[rnd("2022-12", "Series A", None, "Blossom Capital", True, "https://tech.eu/2022/12/13/theydo-raises-12-million/")]))

# ---- Trig (formerly Pavlov)
L.append(cls("trig", status="private", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2025-10",
    stage_cite="https://www.thesaasnews.com/news/trig-raises-6-million-in-seed-funding/",
    note="AI agent platform for account management (Trig, formerly Pavlov; London). '$6 million (GBP 4.5M) in a Seed funding round ... The oversubscribed round was led by 20VC, with participation from Frontline Ventures, Marc Benioff' (The SaaS News; Silicon Canals the same week, early October 2025), after a $2M pre-seed led by Frontline.",
    rounds=[rnd("2025", "pre-seed", 2000000, "Frontline Ventures", None, "https://siliconcanals.com/uks-trig-secures-5-1m/"),
            rnd("2025-10", "seed", 6000000, "20VC", True, "https://www.thesaasnews.com/news/trig-raises-6-million-in-seed-funding/")]))

# ---- Tripledot ($1B+: visible)
L.append(cls("tripledot", status="private", country="GB", country_src=W,
    country_cite="https://techcrunch.com/2022/02/14/tripledot-snaps-up-116m-at-a-1-4b-valuation-as-casual-mobile-games-become-serious-business/",
    city="London", focus="Media, Gaming & Advertising", rng="1b_plus", usd=2000000000, val_src=W, asof="2025-05-07",
    val_cite="https://mobilegamer.biz/its-official-tripledot-has-acquired-all-of-applovins-studios/",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2022-02",
    stage_cite="https://techcrunch.com/2022/02/14/tripledot-snaps-up-116m-at-a-1-4b-valuation-as-casual-mobile-games-become-serious-business/",
    note="Casual mobile games studio (London). The $116M Series B at a $1.4B valuation: 'The round is being led by 20VC' with Access Industries, Lightspeed and Eldridge, following 'a $78 million Series A in April 2021' (TechCrunch, 2022-02-14): 20VC enters at the B, so Growth. Mark: buying AppLovin's studios for $400M in cash and a 20% stake 'worth $400m ... It means Tripledot is now valued at $2bn' (Mobilegamer.biz, 2025-05-07, after the FT), as in the Lightspeed row.",
    rounds=[rnd("2021-04", "Series A", 78000000, None, None, None),
            rnd("2022-02", "Series B", 116000000, "20VC", True, "https://techcrunch.com/2022/02/14/tripledot-snaps-up-116m-at-a-1-4b-valuation-as-casual-mobile-games-become-serious-business/")]))

# ---- Turnkey
L.append(cls("turnkey", status="private", country="US", city="New York", focus="Crypto & Web3", rng="below_1b",
    stage=U, extra=NOSTAGE,
    note="Wallet and key-management infrastructure (New York; ex-Coinbase founders). The firm listed Turnkey by September 2024; its rounds then were a $7.5M seed (2022) and a $15M Series A led by Lightspeed Faction and Galaxy Ventures (closed October 2023, announced April 2024), later a $30M Series B led by Bain Capital Crypto (June 2025) and $12.5M from Circle Ventures and Sequoia (May 2026). No report names 20VC in any: undetermined.",
    rounds=[rnd("2022", "seed", 7500000, None, None, None),
            rnd("2023-10", "Series A", 15000000, "Lightspeed Faction, Galaxy Ventures", None, None),
            rnd("2025-06", "Series B", 30000000, "Bain Capital Crypto", None, None)]))

# ---- Vesence
L.append(cls("vesence", status="private", country="SE", city="Stockholm", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2025-10",
    stage_cite="https://techfundingnews.com/vesence-raises-9m-to-deliver-precision-ai-for-legal-workflows/",
    note="AI document review for law firms (Stockholm; YC). 'The startup just secured $9 million in a seed round led by Emergence Capital, with participation from Creandum, 20VC, Y Combinator' (Tech Funding News, 2025-10-28; Law.com the same day).",
    rounds=[rnd("2025-10", "seed", 9000000, "Emergence Capital", True, "https://techfundingnews.com/vesence-raises-9m-to-deliver-precision-ai-for-legal-workflows/")]))

# ---- Waitroom (later Rumi; acquired by Decidr 2026)
L.append(cls("waitroom", status="acquired", country="US", focus="SaaS", rng="below_1b",
    stage=U, extra=NOSTAGE, entry_date="2022", flags=["city_unknown"],
    note="Live video conversation platform of Vinny Lingham (Waitroom, later Rumi, rumi.ai). 'Character, 20VC, Social Leverage, Valor Equity Partners, Signia and Possible Ventures are also backers' (TechCentral, 2022-03-23, at launch); 20VC's page for Waitroom was posted on 2022-01-24. No report names the round: undetermined. waitroom.com now forwards to rumi.ai, whose notice reads 'Rumi has been acquired by Decidr', service ended 24 July 2026 (read 2026-09-28): acquired.",
    rounds=[rnd("2026-07", "acquisition by Decidr", None, "Decidr", None, "https://rumi.ai/", "company")]))

# ---- WorkOS ($1B+: visible; the Lightspeed row is the stale side)
L.append(cls("workos", status="private", country="US", city="San Francisco", focus="DevTools & APIs", rng="1b_plus", usd=2000000000, val_src=W,
    asof="2026-03-03", val_cite="https://siliconangle.com/2026/03/03/jetstream-security-guild-ai-workos-land-fresh-funding-amid-growing-agentic-ai-infrastructure-push/",
    stage=U, extra=NOSTAGE,
    note="Enterprise-readiness APIs (SSO, directory sync) for developers (San Francisco). The firm added WorkOS to its card in March 2026; no report names 20VC's round, and rounds from the 2020 seed era through the $80M Series B (June 2022) and the Series C fall inside the funds' life: undetermined. Mark: 'WorkOS's $100 million Series C round was raised at a valuation of $2 billion and was led by Meritech Capital Partners LP and Sapphire Ventures' (SiliconANGLE, 2026-03-03). The Lightspeed row still reads below_1b, the stale side.",
    rounds=[rnd("2022-06", "Series B", 80000000, "Greenoaks", None, "https://techcrunch.com/2022/06/01/workos-raises-80m-to-add-enterprise-features-like-sso-to-apps/"),
            rnd("2026-03", "Series C", 100000000, "Meritech Capital, Sapphire Ventures", None, "https://siliconangle.com/2026/03/03/jetstream-security-guild-ai-workos-land-fresh-funding-amid-growing-agentic-ai-infrastructure-push/")]))

# ---- Cognition (re-record, batch-001b): the Series A of 2024 is inside the funds' life
L.append(cls("cognition", stage=U, extra=NOSTAGE, clear=["cite_pending"],
    note="AI software engineer Devin (Cognition AI, San Francisco). The firm added Cognition in March 2026; no source names 20VC's round. Cognition's $21M Series A (Founders Fund, early 2024) falls inside the funds' life as well as every later growth round, so the entry is undetermined (re-recorded from Growth). Mark: the Series E at $48B (TechCrunch, 2026-09-08), the Bain Capital Ventures row's; the 8VC, General Catalyst, Khosla and Lux rows carry the older $10.2B, same band."))

if __name__ == "__main__":
    jl.write("batch-002", L)
