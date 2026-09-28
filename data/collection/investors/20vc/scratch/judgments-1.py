"""PRO-76 grind, batch-001 (first pass: status, country, city, focus, band, entry
round and funding history; the S2A column is decided in its own pass after
scripts/graduation-surfaces.py). Evidence: scratch/evidence-pack.json (the firm's
2026 card, the podcast site's 2022-2024 pages, press naming 20VC, sibling rows),
scratch/research/*.json and scratch/research/url-checks.json (every citation
below was fetched and its 20VC sentence read before use). Rulings cited:
decisions.md D1-D9, R1."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
L = []
W = "web_verified"
U = "undetermined"

# ---- Bonnet
L.append(cls("bonnet", status="acquired", country="GB", city="London", focus="Climate & Energy", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="medium", entry_date="2022-03",
    stage_cite="https://www.uktech.news/mobility/bonnet-funding-20220302",
    note="EV-charging app (London). 20VC joined the $5.5M (GBP 4M) round led by Lightspeed, March 2022: 'venture capital firms Lightspeed, GV and 20VC also provided funding' (UKTN, 2022-03-02); the round is the seed (Lightspeed's own card: Seed, 2022); the GBP 850K round of 2021 was Ascension's. 20VC's own page for Bonnet dates from 2022. A further GBP 3M from existing investors plus crowdfunding (2023) was unnamed. acq. by OVO Energy (announced Nov 2023; Lightspeed's row: completed 2025-07-23).",
    rounds=[rnd("2021", "pre-seed", None, "Ascension Ventures", None, None),
            rnd("2022-03", "seed", 5500000, "Lightspeed", True, "https://www.uktech.news/mobility/bonnet-funding-20220302"),
            rnd("2023-03", "equity injection from existing investors + crowdfunding", 3600000, None, None, "https://www.automotiveworld.com/news/ev-charging-start-up-bonnet-launches-crowdfunding-as-its-closes-fresh-investment/"),
            rnd("2023-11", "acquisition by OVO Energy", None, "OVO Energy", None, "https://mercomcapital.com/ovo-energy-acquires-ev-charging-app-provider-bonnet/")]))

# ---- CourtCorrect
L.append(cls("courtcorrect", status="private", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2021-11",
    stage_cite="https://www.businessinsider.com/courtcorrect-pitch-deck-legal-tech-seed-funding-investors-vc-2021-12",
    note="AI complaints management for regulated firms (London; founded 2019 by Ludwig Bull). 'CourtCorrect ... snapped up $2.95 million (GBP 2.2 million) in seed round funding in November. Investors included RLC Ventures, Ascension Ventures (UK), and The Twenty Minute VC' (Business Insider, 2021-12-08).",
    rounds=[rnd("2021-11", "seed", 2950000, None, True, "https://www.businessinsider.com/courtcorrect-pitch-deck-legal-tech-seed-funding-investors-vc-2021-12")]))

# ---- CryptoTax Calculator
L.append(cls("cryptotax-calculator", status="private", country="AU", city="Sydney", focus="Crypto & Web3", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2022-03",
    stage_cite="https://techcrunch.com/2022/03/01/australias-cryptotaxcalculator-helps-traders-demystify-the-decentralized/",
    note="Crypto tax reporting software (Sydney; since rebranded Summ). 'The seed round netted the previously-bootstrapped company a total of A$4 million ... AirTree led the financing alongside U.S.-based Coinbase Ventures and United Kingdom-based 20VC' (TechCrunch, 2022-03-01).",
    rounds=[rnd("2022-03", "seed", 2900000, "AirTree Ventures", True, "https://techcrunch.com/2022/03/01/australias-cryptotaxcalculator-helps-traders-demystify-the-decentralized/")]))

# ---- Ellis (immigration law firm; NOT the private-credit Ellis in the Thrive and First Round books)
L.append(cls("ellis", status="private", country="US", city="New York", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2022-04",
    stage_cite="https://techcrunch.com/2022/04/18/ellis-raises-5-6m-to-pave-the-way-for-international-students/",
    flags=["identity_homonym"],
    note="Digital immigration law firm (ellis.com). 'Ellis announced today it has raised a $5.6 million seed round led by Kindred Ventures, with participation from Castle Island Ventures, 20VC, Dreamers VC and V1.VC' (TechCrunch, 2022-04-18). A different company from the Ellis (Ryan Williams' private-credit software, New York, 2026) in the Thrive and First Round books: ruled distinct in companies/cross-rulings.json.",
    rounds=[rnd("2022-04", "seed", 5600000, "Kindred Ventures", True, "https://techcrunch.com/2022/04/18/ellis-raises-5-6m-to-pave-the-way-for-international-students/")]))

# ---- EQL
L.append(cls("eql", status="private", country="AU", city="Melbourne", focus="SaaS", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="medium", entry_date="2022-04",
    stage_cite="https://www.startupdaily.net/topic/funding/insight-partners-backs-hype-commerce-startup-eql-in-25-million-raise/",
    note="Launch platform for high-demand e-commerce drops (Melbourne). The A$25M round of April 2022 led by Insight Partners: 'Other backers include ... Harry Stebbings' investment fund, 20VC' (Startup Daily, 2022-04-12); reported as the Series A (Insight's own row).",
    rounds=[rnd("2022-04", "Series A", 18600000, "Insight Partners", True, "https://www.startupdaily.net/topic/funding/insight-partners-backs-hype-commerce-startup-eql-in-25-million-raise/")]))

# ---- FrankieOne
L.append(cls("frankieone", status="private", country="AU", city="Melbourne", focus="Fintech & Payments", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2021-10",
    stage_cite="https://www.startupdaily.net/topic/funding/anti-financial-fraud-regtech-frankieone-raises-20-million-series-a/",
    note="Identity-verification and fraud-prevention onboarding for fintechs and banks (Melbourne). The A$20M ($16M) Series A of October 2021 'was led by AirTree Ventures and Greycroft, with 20VC, Westpac's Reinventure, Tidal Ventures, APEX Capital Partners, and Mantis VC ... also participating' (Startup Daily, 2021-10-12); the Series A+ of November 2022 (A$23M) again lists 20VC.",
    rounds=[rnd("2021-10", "Series A", 16000000, "AirTree Ventures, Greycroft", True, "https://www.startupdaily.net/topic/funding/anti-financial-fraud-regtech-frankieone-raises-20-million-series-a/"),
            rnd("2022-11", "Series A+", 15400000, "AirTree Ventures, Greycroft", True, "https://fintech.global/2022/11/29/frankieone-nets-15-5m-for-unified-onboarding-system/")]))

# ---- Hofy (Stride.VC's too; 20VC has its own round: D4)
L.append(cls("hofy", status="acquired", country="GB", city="London", focus="SaaS", rng="below_1b",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2022-09",
    stage_cite="https://techcrunch.com/2022/09/28/hofy-lands-15m-to-help-companies-remotely-manage-enterprise-equipment/",
    note="IT equipment management for remote teams (London). 'The company today closed a $15 million Series B round led by CNP with participation from Stride, 20VC, Day One Ventures, Kindred Capital, Activum and TrueSight' (TechCrunch, 2022-09-28); 20VC's own page for Hofy dates from 2022. Stride.VC's earlier position is Stride's (decisions.md D4). acq. by Deel, 2024 (TechCrunch, 2024-07-18).",
    rounds=[rnd("2022-09", "Series B", 15000000, "CNP", True, "https://techcrunch.com/2022/09/28/hofy-lands-15m-to-help-companies-remotely-manage-enterprise-equipment/"),
            rnd("2024-07", "acquisition by Deel", None, "Deel", None, "https://techcrunch.com/2024/07/18/deel-acquires-hofy-to-build-its-own-it-device-management-service/")]))

# ---- Junction (Vital until 2024)
L.append(cls("junction", status="private", country="US", country_src="model_knowledge", city="New York", focus="Healthcare & Bio", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="medium", entry_date="2021",
    stage_cite="https://tryvital.medium.com/announcing-our-2-9m-seed-round-led-by-point-nine-8184556955f1",
    flags=["model_disputes_source"],
    note="Health-data API (Vital, YC W20, renamed Junction in 2024; started in London, now New York, as the Creandum and Point Nine rows read; the Wikidata GB is disputed). 'Today Vital is proud to announce our $2.9m seed funding round ... led by Point Nine, with participation from 20VC, Amino Collective, Adventure Fund and Inflect Health' (the company's post). The post displays a 2023 date on Medium, a re-post: 20VC's own page for Vital is dated 2022-01-24 and Point Nine's card dates the round 2021, so the entry date is 2021.",
    rounds=[rnd("2021", "seed", 2900000, "Point Nine", True, "https://tryvital.medium.com/announcing-our-2-9m-seed-round-led-by-point-nine-8184556955f1", "company"),
            rnd("2025-03", "Series A", 18000000, "Creandum", None, None)]))

# ---- Ledgy
L.append(cls("ledgy", status="private", country="CH", city="Zurich", focus="Fintech & Payments", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="medium", entry_date="2021-09",
    stage_cite="https://www.startupticker.ch/en/news/ledgy-completes-10-million-series-a",
    note="Equity management platform (Zurich). The $10M Series A of September 2021 led by Sequoia: 'further participants in the round are Xavier Niel, Harry Stebbings, Visionaries Club' (Startupticker, 2021-09-07). The line names the founder, not the fund; it dates the entry of a company the firm lists as its own (20VC's pages 2022-2023 and 2026; decisions.md R1).",
    rounds=[rnd("2021-09", "Series A", 10000000, "Sequoia Capital", True, "https://www.startupticker.ch/en/news/ledgy-completes-10-million-series-a")]))

# ---- Linktree ($1B+: visible)
L.append(cls("linktree", status="private", country="AU", country_src=W, country_cite="https://www.insightpartners.com/ideas/linktree-raises-us10-7-million-series-a-led-by-insight-partners-and-airtree-ventures/",
    city="Melbourne", focus="Consumer & Marketplaces", rng="1b_plus", usd=1300000000, val_src=W, asof="2022-03-16",
    val_cite="https://www.insightpartners.com/ideas/linktree-raises-110-million-usd-led-by-index-and-coatue-to-power-next-phase-of-growth-for-creators-consumers-and-brands/",
    stage="Series A", stage_src=W, stage_conf="medium", entry_date="2020-10",
    stage_cite="https://techcrunch.com/2020/10/26/linktree-raises-10-7m-for-its-lightweight-link-centric-user-profiles/",
    flags=["stale"],
    note="Link-in-bio platform (Melbourne). The $10.7M Series A of October 2020 led by Insight Partners and AirTree: 'Strategic investors in the round include Twenty Minute VC's Harry Stebbings' (TechCrunch, 2020-10-26), inside Fund I's life (decisions.md R1: the firm lists Linktree 2022-2024 and 2026). Mark: the $110M Series C at $1.3B (March 2022), the last priced round, older than 24 months, as in the Coatue and Insight rows.",
    rounds=[rnd("2020-10", "Series A", 10700000, "Insight Partners, AirTree Ventures", True, "https://techcrunch.com/2020/10/26/linktree-raises-10-7m-for-its-lightweight-link-centric-user-profiles/"),
            rnd("2022-03", "Series C", 110000000, "Index Ventures, Coatue", None, "https://www.insightpartners.com/ideas/linktree-raises-110-million-usd-led-by-index-and-coatue-to-power-next-phase-of-growth-for-creators-consumers-and-brands/")]))

# ---- Lottielab
L.append(cls("lottielabs", status="private", country="GB", city="London", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2022-04",
    stage_cite="https://businesscloud.co.uk/news/gifs-of-the-future-firm-backed-by-vcs-and-angels/",
    note="Lottie animation editor for product teams (Lottielab, London). 'The seed round was led by early-stage VC firm Point Nine and included participation from podcaster-turned-investor Harry Stebbings's 20VC, Entrepreneur First' (BusinessCloud, 2022-04-27).",
    rounds=[rnd("2022-04", "seed", None, "Point Nine", True, "https://businesscloud.co.uk/news/gifs-of-the-future-firm-backed-by-vcs-and-angels/")]))

# ---- Merge
L.append(cls("merge-dev", status="private", country="US", city="San Francisco", focus="DevTools & APIs", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="Unified API for HR, accounting and CRM integrations (Merge, San Francisco). The firm lists Merge on its 2022-2024 pages and its 2026 card, and its founder names 'Merge API' among his investments (BusinessCloud, 2026-08-12), but no source ties 20VC to a round: the $4.5M seed (May 2021, NEA), the $15M Series A (November 2021) and the $55M Series B (October 2022, Accel) name other investors. Round undetermined.",
    rounds=[rnd("2021-05", "seed", 4500000, "NEA", None, "https://techcrunch.com/2021/05/17/merge-raises-4-5m-to-help-b2b-companies-build-customer-facing-integrations"),
            rnd("2021-11", "Series A", 15000000, None, None, "https://www.merge.dev/blog/announcing-our-15-million-series-a-and-expanded-partnerships", "company"),
            rnd("2022-10", "Series B", 55000000, "Accel", None, "https://techcrunch.com/2022/10/24/merge-raises-55m-series-b-for-its-unified-api/")]))

# ---- Noh (Divy until 2022)
L.append(cls("noh-payments", status="private", country="BR", city="São Paulo", focus="Fintech & Payments", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2021",
    stage_cite="https://oglobo.globo.com/blogs/capital/post/2025/02/fintech-salva-casamentos-noh-alcanca-primeiro-bilhao-em-transacoes.ghtml",
    note="Joint account and card app for couples (Noh, formerly Divy; Sao Paulo). 'uma rodada semente de R$ 17 milhoes captada em 2021 com os fundos Kindred Ventures, Future Positive, Propel e 20VC' (O Globo, 2025-02-21).",
    rounds=[rnd("2021", "seed", 3200000, "Kindred Ventures", True, "https://oglobo.globo.com/blogs/capital/post/2025/02/fintech-salva-casamentos-noh-alcanca-primeiro-bilhao-em-transacoes.ghtml")]))

# ---- Numeral (Paris payments; NOT YC's Numeral)
L.append(cls("numeral", status="acquired", country="FR", city="Paris", focus="Fintech & Payments", rng="below_1b",
    stage=U, flags=["identity_homonym", "stage_uncited"],
    note="Payment operations platform for banks and fintechs (Paris). 20VC lists it from 2022 (the podcast site's page, 2022-01-24) and on its 2026 card, but no source names 20VC in its only round, the EUR 13M seed of December 2021 led by Balderton (the founder's post names Balderton, angels and Kima). acq. by Mambu, December 2024 (PR Newswire); the firm's 2026 card does not flag the exit. A different company from YC's Numeral (sales-tax compliance, San Francisco): ruled distinct.",
    rounds=[rnd("2021-12", "seed", 14700000, "Balderton Capital", None, "https://medium.com/@emandon/announcing-numeral-and-our-13-million-first-round-of-funding-463d4db0678b", "company"),
            rnd("2024-12", "acquisition by Mambu", None, "Mambu", None, "https://www.prnewswire.com/news-releases/mambu-acquires-payment-technology-provider-numeral-bolstering-its-market-position-to-target-new-growth-opportunities-302323958.html")]))

# ---- Pogo
L.append(cls("pogo", status="private", country="US", city="New York", focus="Consumer & Marketplaces", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="App that pays consumers for their data. $14.8M announced in July 2022, 'a $12.3 million seed round led by Josh Buckley and a previously unannounced $2.5 million pre-seed'; 'Other investors in the startup include Slow Ventures, Village Global, Harry Stebbing's 20VC' (TechCrunch, 2022-07-26): 20VC is in one of the two rounds and no source says which, so the round is undetermined.",
    rounds=[rnd("2021", "pre-seed", 2500000, None, None, "https://fintech.global/2022/07/27/pogo-secures-14-8m-to-empower-consumers-to-benefit-from-their-data/"),
            rnd("2022-07", "seed", 12300000, "Josh Buckley", None, "https://techcrunch.com/2022/07/26/pogo-lands-millions-to-become-the-honey-for-the-real-world/")]))

# ---- Rayon
L.append(cls("rayon", status="private", country="FR", city="Paris", focus="SaaS", rng="below_1b",
    stage="Pre-Seed", stage_src=W, stage_conf="high", entry_date="2022-06",
    stage_cite="https://www.rayon.design/blog/announcing-rayon-s-pre-seed",
    note="Collaborative floor-plan design software (Paris). 'We are thrilled to announce Rayon's pre-seed round, led by Seedcamp, alongside Foundamental and 20VC' (the company's post; EUR 1.9M, June 2022); a EUR 4M seed followed in September 2023.",
    rounds=[rnd("2022-06", "pre-seed", 2000000, "Seedcamp", True, "https://www.rayon.design/blog/announcing-rayon-s-pre-seed", "company"),
            rnd("2023-09", "seed", 4300000, None, None, "https://www.eu-startups.com/2023/09/paris-based-rayon-raises-e4-million-to-launch-its-collaborative-architectural-design-tool/")]))

# ---- Rollee
L.append(cls("rollee", status="private", country="FR", city="Paris", focus="Fintech & Payments", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2022-04",
    stage_cite="https://www.getrollee.com/blog/fundraising-4m-in-seed",
    note="Employment and income data API for lenders and insurers (Paris). 'we are delighted to announce our 4M Seed fundraising. We are welcoming our new investors Speedinvest, Seedcamp and 20VC' (the company's post, 2022-04-13).",
    rounds=[rnd("2022-04", "seed", 4400000, None, True, "https://www.getrollee.com/blog/fundraising-4m-in-seed", "company")]))

# ---- Slashwork (Anserine Labs, Inc.)
L.append(cls("slashwork", status="private", country="GB", city="London", focus="SaaS",
    note="Workplace communication platform by ex-Facebook Workplace engineers Jackson Gabbard, David Miller and Josh Watzman (London; issuer Anserine Labs, Inc.). 'Slashwork has emerged from stealth with a $3.5 million round led by 20VC' (Pulse 2.0, 2026-02-03); the Form D of that round (first sale 2025-08-13) names 20VC's Julien Codorniou a director. The stage is the filing's band (Seed).",
    rounds=[rnd("2025-08", "seed", 3500000, "20VC", True, "https://pulse2.com/slashwork-3-5-million-funding/")]))

# ---- Sorare ($1B+: visible)
L.append(cls("sorare", status="private", country="FR", country_src=W, country_cite="https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html",
    city="Paris", focus="Media, Gaming & Advertising", rng="1b_plus", usd=4300000000, val_src=W, asof="2021-09-21", clear=["needs_web_value", "unicorn_name_match"],
    val_cite="https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html",
    stage=U, flags=["stale", "stage_uncited"],
    note="Fantasy football with NFT player cards (Paris). 20VC lists Sorare on its 2022-2024 pages and its 2026 card, and Business Insider (2024-06-13) names it in '20VC's portfolio', but no source ties 20VC to a round (the $4M round of July 2020, the $50M Series A of February 2021 led by Benchmark, the $680M Series B of September 2021 led by SoftBank): round undetermined. Mark: the $680M Series B at $4.3B, the last stated priced round, as in the Accel, Atomico, Headline and IVP rows (Erik's ruling E2, 2026-09-28); stale.",
    rounds=[rnd("2020-07", "seed", 4000000, None, None, None),
            rnd("2021-02", "Series A", 50000000, "Benchmark", None, None),
            rnd("2021-09", "Series B", 680000000, "SoftBank", None, "https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html")]))

# ---- Taxdoo
L.append(cls("taxdoo", status="private", country="DE", city="Hamburg", focus="Fintech & Payments", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2020-12",
    stage_cite="https://techcrunch.com/2020/12/15/taxdoo/",
    note="Tax compliance and accounting for cross-border e-commerce (Hamburg). 'Leading the Series A round is venture capital firm Accel, with participation from Visionaries Club, 20VC and existing investor HTGF' (TechCrunch, 2020-12-15: Fund I, then US-focused, which the article remarks on); 20VC again in the EUR 57M Series B led by Tiger Global (December 2021).",
    rounds=[rnd("2020-12", "Series A", 21000000, "Accel", True, "https://techcrunch.com/2020/12/15/taxdoo/"),
            rnd("2021-12", "Series B", 64000000, "Tiger Global", True, "https://techcrunch.com/2021/12/16/taxdoo-raises-64m-to-expand-from-tax-compliance-to-a-wider-set-of-financial-tools-for-e-commerce-companies/")]))

# ---- This One
L.append(cls("this-one", status="acquired", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="'AI personalisation at scale' (the firm's card). 20VC's page for This One dates from 2022-08-05 and its 2026 card flags an exit; no acquirer, round or press was found (Google News, TechCrunch, Crunchbase News and two web searches, 2026-09-28) and this.one no longer resolves. Status from the firm's own exit flag, acquirer unknown; country and city from the podcast site's London portfolio, low confidence.",
    extra={"hq_country_confidence": "low", "hq_city_confidence": "low"}))

# ---- Xentral
L.append(cls("xentral", status="private", country="DE", city="Augsburg", focus="SaaS", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="ERP for SMEs and e-commerce (Augsburg). 20VC lists Xentral on its page of 2022-01-24 and its 2026 card; its current GP Julien Codorniou was a personal angel in Xentral (TechCrunch, 2024-12-18), but the firm's page predates his 2024 arrival, so the listing is the firm's own position (decisions.md D8). No source names 20VC in a round (the $20M Series A of 2021 led by Sequoia; the $75M Series B of January 2022 led by Tiger Global and Meritech): round undetermined.",
    rounds=[rnd("2021-01", "Series A", 20000000, "Sequoia Capital", None, None),
            rnd("2022-01", "Series B", 75000000, "Tiger Global, Meritech", None, "https://xentral.com/en/blog/investment-tigerglobal-meritech", "company")]))

# ---- AgentSync ($1B+: visible)
L.append(cls("agent-sync", status="private", country="US", city="Denver", focus="SaaS", rng="1b_plus", usd=1200000000, val_src=W,
    asof="2021-12-07", val_cite="https://www.prnewswire.com/news-releases/agentsync-secures-75m-at-a-1-2b-unicorn-valuation-to-power-growth-across-the-insurance-industry-301439043.html",
    stage="Seed", stage_src=W, stage_conf="medium", entry_date="2020-08",
    stage_cite="https://techcrunch.com/2020/08/04/agentsync-raises-4-4m-for-its-insurtech-compliance-service/",
    flags=["stale"],
    note="Insurance producer licensing and compliance (Denver). 'AgentSync announced that it has closed a $4.4 million seed round, co-led by Elad Gil and Caffeinated Capital ... including Affirm's Max Levchin and the podcaster turned VC Harry Stebbings' (TechCrunch, 2020-08-04): Fund I's first months, a company the firm lists 2022-2024 and its founder names among his investments (decisions.md R1). $35M Series A (March 2021, a16z); $75M Series B at $1.2B led by Valor (December 2021, the company's release), the last priced mark; a $50M Series B extension (October 2023) stated no price. Stale.",
    rounds=[rnd("2020-08", "seed", 4400000, "Elad Gil, Caffeinated Capital", True, "https://techcrunch.com/2020/08/04/agentsync-raises-4-4m-for-its-insurtech-compliance-service/"),
            rnd("2021-03", "Series A", 35000000, "Andreessen Horowitz", None, None),
            rnd("2021-12", "Series B", 75000000, "Valor Equity Partners", None, "https://www.prnewswire.com/news-releases/agentsync-secures-75m-at-a-1-2b-unicorn-valuation-to-power-growth-across-the-insurance-industry-301439043.html"),
            rnd("2023-10", "Series B extension", 50000000, None, None, "https://techcrunch.com/2023/10/26/agentsync-raises-50m-more-in-a-massive-series-b-extension/")]))

# ---- Airwallex ($1B+: visible)
L.append(cls("airwallex", status="private", country="SG", country_src=W, country_cite="https://www.businesswire.com/news/home/20251207195682/en/Airwallex-Raises-$330M-Series-G-at-$8B-Valuation-Establishes-San-Francisco-as-Dual-Global-Headquarters",
    city="Singapore", focus="Fintech & Payments", rng="1b_plus", usd=8000000000, val_src=W, asof="2025-12-08",
    val_cite="https://www.businesswire.com/news/home/20251207195682/en/Airwallex-Raises-$330M-Series-G-at-$8B-Valuation-Establishes-San-Francisco-as-Dual-Global-Headquarters",
    stage="Growth", stage_src="model", stage_conf="medium", flags=["cite_pending", "model_disputes_source"], clear=["needs_web_value", "unicorn_name_match"],
    note="Global business payments (founded in Melbourne, headquartered in Singapore, San Francisco a second global HQ from December 2025; the Wikidata AU is its founding country). The firm's card dates from 2026-03 and no source names 20VC's round; every priced Airwallex round since 20VC's first fund (April 2020) is a Series D or later, so the entry is Growth whichever it was (cite_pending for the round). Mark: '$330M Series G at $8B Valuation' led by Addition (Business Wire, 2025-12-07).",
    rounds=[rnd("2025-05", "Series F", 300000000, "Square Peg", None, None),
            rnd("2025-12", "Series G", 330000000, "Addition", None, "https://www.businesswire.com/news/home/20251207195682/en/Airwallex-Raises-$330M-Series-G-at-$8B-Valuation-Establishes-San-Francisco-as-Dual-Global-Headquarters")]))

# ---- allO
L.append(cls("allo", status="private", country="DE", city="Munich", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2024-07",
    stage_cite="https://tech.eu/2024/07/09/restaurant-saas-allo-secures-5m/",
    note="Restaurant operating system and point of sale (Munich). 'Restaurant software provider allO has raised a $5 million Seed funding round ... The round was led by 20VC, with participation from Keen Venture Partners, the NL Startup Fund, 20Product, 20Growth' (Tech.eu, 2024-07-09); $14M Series A led by Zigg Capital (May 2026). Not YC's Allo (a different company).",
    flags=["identity_homonym"],
    rounds=[rnd("2024-07", "seed", 5000000, "20VC", True, "https://tech.eu/2024/07/09/restaurant-saas-allo-secures-5m/"),
            rnd("2026-05", "Series A", 14000000, "Zigg Capital", None, "https://www.hospitalitynet.org/news/4132593/allo-raises-14m-series-a-led-by-zigg-capital-to-scale-the-first-ai-native-operating-system-for-restaurants")]))

# ---- Altertable
L.append(cls("altertable", status="private", country="FR", city="Paris", focus="Data Infrastructure", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2025-06", flags=["stage_uncited"],
    note="AI-native analytics database (Altertable, founded by ex-Algolia CTO Sylvain Utard). Emerged from stealth in June 2025 with a EUR 2.5M seed led by 20VC with Kima Ventures and Drysdale (reported; no fetchable page naming 20VC was found in the run, so the stage is model-sourced at low confidence pending a citation).",
    rounds=[rnd("2025-06", "seed", 2860000, "20VC", True, None)]))

# ---- AMI Labs ($1B+: visible)
L.append(cls("ami-labs", status="private", country="FR", country_src=W, country_cite="https://observer.com/2026/03/yann-lecun-ami-startup-funding-round-fund/",
    city="Paris", focus="AI & Applied AI", rng="1b_plus", usd=4530000000, val_src=W, asof="2026-03-09",
    val_cite="https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/",
    stage="Seed", stage_src=W, stage_conf="medium", entry_date="2026-03",
    stage_cite="https://observer.com/2026/03/yann-lecun-ami-startup-funding-round-fund/",
    note="World-model AI lab of Yann LeCun (Paris). Its only round: $1.03B at a $3.5B pre-money ($4.53B post), March 2026, reported as Europe's largest seed ('AMI Labs Raises Record $1B Seed Round', Observer, 2026-03-10); 20VC was named among the investors in talks (Bloomberg via Mezha, 2026-01-24) and the firm added AMI Labs to its list in March 2026, so its position is this seed. Same mark as the Headline row.",
    rounds=[rnd("2026-03", "seed", 1030000000, "Cathay Innovation, Greycroft, Hiro Capital, HV Capital, Bezos Expeditions", True, "https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/")]))

# ---- Amo
L.append(cls("amo", status="private", country="FR", city="Paris", focus="Consumer & Marketplaces", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="Social app studio of Zenly's founder Antoine Martin (Paris). Its $20M (EUR 18M) round of early 2023 was led by New Wave with Coatue and DST Global Partners and 80 angels (TechCrunch, 2023-11-19); no source names 20VC in it. The firm lists Amo on its 2026 card: round undetermined.",
    rounds=[rnd("2023-03", "seed", 20000000, "New Wave", None, "https://techcrunch.com/2023/11/19/with-amo-the-founder-of-zenly-wants-to-make-social-apps-social-again/")]))

if __name__ == "__main__":
    jl.write("batch-001a", L)
