"""PRO-162 grind, batch-007 (charta-health .. eschelon-telecom). Evidence as in judgments-1.py, plus Google News
(nq.py, news-extra-b7.json), Wikipedia extracts (wikifetch.py), the firm's archived pages (Common Crawl captures under
data/filings/commoncrawl/), EDGAR filings read 2026-09-27 (URLs quoted per line) and seven WebSearch checks.

Two rows leave as verdicts: Eschelon Telecom (its 2005 IPO prospectus names Bain Capital Fund VI, a generalist fund, as
the Bain holder; decisions.md D2, R1) and CTC Communications (Bain Capital Fund VI bought preferred stock of the
NASDAQ-listed company in May 2000; T3). EData Resources merges into environmental-data-resources-inc at the rebuild
(identity-merges.json), so it is not classified here.

Rows that are one company with another row (for Erik's merge list): datica = sansoro-health (the firm's 2020-2022 page
/portfolio/sansoro-health carries the name Datica); davinci-payments = swift-prepaid-solutions = onbe (the firm's
2020-2021 page /portfolio/swift-prepaid-solutions carries the name DaVinci Payments; Onbe is the 2021 rebrand);
digital-compliance = venminder-digital-comply (Venminder's former name); driven = concurrent (Concurrent, Inc.
rebranded Driven)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []
MOM = "Momentum check (Google News, 2026-09-27): no $1B+ priced round found."


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


# ---- live-site rows
L.append(cls("charta-health", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Healthcare & Bio", stage="Seed", **site_stage("charta-health"), entry_date="2025",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("charta-health", "Investing in Charta Health"),
    note="AI pre-bill chart review for provider groups (San Francisco). BCV's listing: 2025, Seed (Aaref Hilaly, Alysaa Co); the firm "
         "'met at pre-seed in 2023' and led the partnership 'from inception' (its posts). Charta's $8.1M seed was reported in "
         "February 2025, then the '$22m Series A round led by Bain Capital Ventures' (Madrona's post, 2025-07-22) graduates it. " + MOM,
    rounds=[rnd("2025-07", "Series A", 22000000, "Bain Capital Ventures", True, NEWS("charta-health", "Investing in Charta Health"), "press")]))
L.append(cls("cleanlab", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Data Infrastructure", stage="Seed", **site_stage("cleanlab"), entry_date="2022",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("cleanlab", "Raises $25M Series A to Automatically"),
    note="Data curation for AI and LLMs (San Francisco). BCV's listing: 2022, Seed (Aaref Hilaly); the $5M seed was announced in July 2023 "
         "and the $25M Series A led by Menlo followed in October 2023 (businesswire). 'AI data labeler Handshake buys Cleanlab' "
         "(TechCrunch, 2026-01-28, " + NEWS("cleanlab", "Handshake buys Cleanlab") + "): mostly a team hire, but announced as a purchase of "
         "the company, so acquired (COLLECTION.md s6 acqui-hire rule; the firm's listing and sibling Menlo read the same).",
    rounds=[rnd("2023-10", "Series A", 25000000, "Menlo Ventures", True, NEWS("cleanlab", "Raises $25M Series A to Automatically"), "press")]))
L.append(cls("cogent", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco", focus="Security",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("cogent", "Cogent Security Raises $42 Million for AI-Driven"), entry_date="2026-02",
    note="AI agents for vulnerability management (Cogent Security, San Francisco). 'The funding was led by Bain Capital Ventures' "
         "(SecurityWeek, 2026-02-18, the $42M Series A); the firm's post says it is 'partnering with them on their Series A financing'. "
         "Greylock led the 2025 seed (sibling row). " + MOM))
L.append(cls("cognition", status="private", rng="10b_plus", country="US", country_src="model_knowledge", city="San Francisco",
    focus="AI & Applied AI", stage="Growth", **site_stage("cognition"), entry_date="2025",
    usd=48000000000, val_src="web_verified", asof="2026-09-08", val_cite=NEWS("cognition", "Cognition hits $48B valuation"),
    extra={"valuation_range_source": "web_verified"},
    note="AI software engineer Devin (Cognition AI, San Francisco; Wikipedia). BCV's listing: 2025, Growth (Aaref Hilaly). Mark: the $2B "
         "Series E at $48B (TechCrunch, 2026-09-08), fresher than the $10.2B of September 2025 the 8VC, Khosla and Lux rows carry; "
         "the $26B round of May 2026 came between."))
L.append(cls("command-e-dropbox", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="SaaS", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("command-e-dropbox", "Command E raises $4.3 million"), entry_date="2019",
    note="Cross-app search (San Francisco). '$4.3 million in seed funding to date from investors including Bain Capital Ventures, Craft "
         "Ventures, Amplify Partners' (TechCrunch, 2020-05-19); the firm's post of 2019-12-11 already names Command E among its "
         "investments, so the entry dates to 2019 (the listing says 2020). Dropbox acquired it (the firm's listing links Dropbox's "
         "'Welcome Command E to Dropbox' post). Graduation left for the graduation pass."))
L.append(cls("compound", status="private", rng="below_1b", city="San Francisco", focus="Crypto & Web3",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("compound", "back Compound's $25M Series A"), entry_date="2018",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("compound", "back Compound's $25M Series A"),
    note="DeFi lending protocol (Compound Labs, San Francisco; the firm's 2018 page, Salil Deshpande). 'Compound raised an $8.2 million "
         "seed round in 2018 led by Andreessen Horowitz, Bain Capital Ventures, and Polychain Capital' and the $25M Series A led by "
         "Andreessen Horowitz followed with BCV participating (The Block, 2019-11-14). Sibling a16z reads the 2018 round as its Series A; "
         "The Block names it the seed.",
    rounds=[rnd("2019-11", "Series A", 25000000, "Andreessen Horowitz", True, NEWS("compound", "back Compound's $25M Series A"), "press")]))
L.append(cls("contextual-ai", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Mountain View",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=W("Contextual AI"), entry_date="2023-06",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=W("Contextual AI"),
    note="Enterprise RAG agents (Mountain View), a BCV Labs incubation. 'BCV is leading its seed round of $20 million' (the firm's post, "
         "2023-06-07; Wikipedia); the $80M Series A led by Greycroft followed in August 2024. In May 2026 Google DeepMind hired staff "
         "and licensed its technology (" + NEWS("contextual-ai", "Silicon UK") + "), a hire, not a purchase of the company; contextual.ai "
         "still sells its product (read 2026-09-27), so private under the acqui-hire rule although the firm's listing tags it Acquired. "
         + MOM,
    rounds=[rnd("2024-08", "Series A", 80000000, "Greycroft", True, W("Contextual AI"), "press")]))
L.append(cls("corridor", status="private", rng="below_1b", city="New York", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("protecting-the-american-dream"), entry_date="2026-09",
    grad="censored",
    note="AI-native health benefits brokerage for small businesses (New York, per Health Tech World). 'We are thrilled to partner with "
         "Corridor on this mission and lead their $25m seed financing' (the firm's post, 2026-09-22; TechCrunch "
         + NEWS("corridor", "Corridor raises $25M seed to build") + "); inside 24 months, so censored. Sibling Felicis's 'corridor' is a "
         "different company (a software-security platform), so its city is not aligned. " + MOM))
L.append(cls("crosby", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("crosby", "Raises $5.8m Seed"),
    entry_date="2025-06",
    grad="graduated", grad_src="first_party", grad_conf="high", grad_cite=POST("crosby-is-redefining"),
    note="Hybrid AI law firm for contract review (New York: 'We work in-person in New York City', Artificial Lawyer). Its founder was "
         "BCV's entrepreneur in residence; the $5.8M seed was 'led by the giant Sequoia Capital, and is also backed by Bain Capital "
         "Ventures' (Artificial Lawyer, 2025-06-19), then BCV was 'excited to lead their Series A' (the firm's post, 2025-10-08, the $20M "
         "round), which graduates it; a $60M round followed in April 2026. Sibling Sequoia's San Francisco and censored reading look "
         "wrong; Lux reads New York. " + MOM,
    rounds=[rnd("2025-10", "Series A", 20000000, "Bain Capital Ventures", True, POST("crosby-is-redefining"), "firm")]))
L.append(cls("daylight", status="private", rng="below_1b", country="IL", country_src="web_verified",
    country_cite=NEWS("daylight", "raises $33 million just three months"), city="Tel Aviv", focus="Security",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("daylight", "Daylight Security raises $7M seed led by BCV"),
    entry_date="2025-07",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("daylight", "raises $33 million just three months"),
    note="AI-driven managed detection and response (Daylight Security, Tel Aviv). 'Daylight Security raises $7M seed led by BCV' (Axios, "
         "2025-07-22); 'Israeli cybersecurity startup Daylight has raised $33 million in Series A funding, led by Craft Ventures with "
         "participation from Bain Capital Ventures' (Calcalist, 2025-11-04). Sibling rows 'daylight' at a16z and USV are other "
         "companies (a home-energy network and an onchain recommendation engine), so nothing is aligned. " + MOM,
    rounds=[rnd("2025-11", "Series A", 33000000, "Craft Ventures", True, NEWS("daylight", "raises $33 million just three months"), "press")]))
L.append(cls("disclo", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Austin", focus="SaaS",
    stage="Seed", **site_stage("disclo"), entry_date="2023",
    note="Workplace accommodations and leave management (Austin, aligned with the YC row). BCV's listing: 2023, Seed; the $5M seed led by "
         "General Catalyst closed in February 2023 (" + NEWS("disclo", "Led By General Catalyst") + "). Graduation left for the graduation "
         "pass. " + MOM))
L.append(cls("dream", status="private", rng="1b_plus", country="IL", country_src="web_verified",
    country_cite=NEWS("dream", "Israeli co Dream Security raises $100m"), city="Tel Aviv", focus="Security",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("dream", "(Series B) Raised At $1.1 Billion"),
    entry_date="2025-02",
    usd=3000000000, val_src="web_verified", asof="2026-06-18", val_cite=NEWS("dream", "SecurityWeek"),
    extra={"valuation_range_source": "web_verified"}, flags=["model_disputes_source"],
    note="AI cyber defence for governments (Dream Security, Tel Aviv; founders Shalev Hulio, Sebastian Kurz, Gil Dolev). BCV led the "
         "$100M Series B at $1.1B in February 2025 ('Bain Backs Israeli AI Cybersecurity Startup Dream', Bloomberg; the firm's post "
         "2025-02-17); a Series B entry reads Growth. Mark: the $260M round at $3B (SecurityWeek, 2026-06-18). The prefilled 'defunct' "
         "and Japan came from a wrong join; the a16z and YC 'dream' rows are other companies."))
L.append(cls("echelon-ai", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("echelon-ai", "Echelon AI raises $4.75M"), entry_date="2025-10", grad="censored",
    note="AI agents for ServiceNow implementations (San Francisco). '$4.75 million in seed funding led by Bain Capital Ventures' "
         "(VentureBeat, 2025-10-09); inside 24 months, so censored. " + MOM))

# ---- crypto list (baincapitalcrypto.com)
L.append(cls("community-labs", status="private", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("community-labs", "Teenage Founder"), entry_date="2022-09",
    note="Developer tools for the Arweave ecosystem. 'Teenage Founder Raises $30 Million for Crypto Startup Community Labs' (Bloomberg, "
         "2022-09-08); Bain Capital Crypto published it on 2022-09-21, the round it joined, read as the seed with sibling Lightspeed. "
         "No source read places the company. Graduation left for the graduation pass. " + MOM))
L.append(cls("curio", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite="https://chainwire.org/2024/08/06/curio-announces-5-7-million-funding-round-to-launch-duper-season-one-co-led-by-bain-capital-crypto-and-sevenx-ventures/",
    city="San Francisco", focus="Media, Gaming & Advertising", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("curio", "Bain Capital Crypto backs gaming"), entry_date="2023-02", flags=["model_disputes_source"],
    note="Onchain games and game infrastructure (San Francisco, per its 2024 release dateline). Bain Capital Crypto led the $2.9M seed "
         "(The Block, 2023-02-21) and co-led a further $5.7M seed with SevenX in August 2024. The prefilled Algeria came from a wrong "
         "join. Sibling Cherry's 'curio' is a London audio-journalism app, a name collision. Graduation left for the graduation pass. "
         + MOM))
L.append(cls("duality", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Crypto & Web3", stage="undetermined", entry_date="2022",
    note="Duality Labs, an order-book DEX in the Cosmos ecosystem, incubated by BCV (Ron Miasnik 'helped incubate and acted as CEO of our "
         "portfolio company Duality Labs', the firm's post 2023-12-14). Neutron's DAO approved the Duality protocol merger, bringing the "
         "team and the DEX into Neutron (https://forum.neutron.org/t/approved-proposal-12-duality-protocol-merger/154), a merger into "
         "another project, so acquired; Neutron sunset the DEX in April 2026. The incubation money is not a named round."))

# ---- archive rows, 2010s
L.append(cls("china-pnr", status="public", rng="below_1b", country="CN", country_src="web_verified",
    country_cite="https://www.scmp.com/business/article/2151874/bain-capital-keeps-cool-head-takes-long-view-china-fintech-and-education",
    city="Shanghai", focus="Fintech & Payments", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015",
    note="Payments infrastructure (ChinaPnR / Huifu, Shanghai, founded 2006). The firm listed it 2015-2022 (Growth, Matt Harris); Bain "
         "Capital bought a 22.45% stake around 2015 and partly exited in the June 2018 Hong Kong IPO of Huifu Payment (HKEX: 1806; SCMP). "
         "A 2015 stake in a nine-year-old company is a late private round, read as Growth. Still listed and operating in 2025; the "
         "market cap (well under $1B) is not pinned here."))
L.append(cls("collectable", status="defunct", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.prnewswire.com/news-releases/sports-memorabilia-platform-collectable-announces-additional-5-5-million-in-funding-as-part-of-series-a-round-to-expand-user-base-and-support-product-expansion-301300300.html",
    entry_date="2021-05",
    note="Fractional investing in sports memorabilia (New York, the firm's 2022 page). BCV joined the $5.5M addition to the Series A led by "
         "Amplo (PR Newswire, May 2021; 'Fractional Cards Broker Collectable Snags Amplo, Bain VC Funds', Sportico). The business stopped: "
         "'A Sports Memorabilia Startup Let Fans Own a Piece of History. Then the Business Vanished' (Inc., 2026-09-17, "
         + NEWS("collectable", "Then the Business Vanished") + "), with investor suits in 2025-2026."))
L.append(cls("datica", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Madison",
    focus="Healthcare & Bio", stage="undetermined",
    note="Healthcare cloud and integration platform (Madison, WI). This is BCV's Sansoro Health position after the June 2019 merger: the "
         "firm's 2020-2022 page /portfolio/sansoro-health carries the name Datica, so the row is one company with sansoro-health. "
         "'Lyniate Acquires Datica Integration Business' (Business Wire, 2021-04-27, " + NEWS("datica", "Lyniate Acquires Datica") + "), "
         "the Sansoro product line, an asset sale, so acquired. The entry round (Sansoro, 2017) is not named."))
L.append(cls("davinci-payments", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Chicago",
    focus="Fintech & Payments", stage="undetermined",
    note="Prepaid and digital payouts (daVinci Payments, formerly Swift Prepaid Solutions, bought in 2019 by Syncapay, which BCV backs "
         "with Silversmith, MissionOG and Nyca; PaymentsJournal). The firm's 2020-2021 page /portfolio/swift-prepaid-solutions carries "
         "the name DaVinci Payments, so the row is one company with swift-prepaid-solutions and onbe (the 2021 rebrand, Chicago). In "
         "December 2020 daVinci merged with North Lane Technologies and 'Centerbridge's majority equity investment' joined the existing "
         "investors (https://www.silversmith.com/news/davinci-payments-completes-merger-with-north-lane-technologies-creating-high-growth-payment-company): "
         "a change of control, so acquired. BCV's 2019 round is not named."))
L.append(cls("digital-compliance", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Elizabethtown",
    focus="Fintech & Payments", stage="undetermined",
    note="Venminder under its former name (company registers file Venminder, Inc. as Digital Comply, "
         "https://system.privco.com/company/digital-comply_private_stock_annual_report_financials; the firm's live list reads "
         "'Venminder (Digital Comply)', 2012, Michael Krupka, and the 2013 page was /portfolio/company/digital-compliance), so the row "
         "is one company with "
         "venminder-digital-comply and aligns with it: third-party risk management (Elizabethtown, KY), acquired by Ncontracts in "
         "September 2024. BCV's first round is not named (BCV led a later $4M Series B, January 2016)."))
L.append(cls("dna-games", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Bruno",
    focus="Media, Gaming & Advertising", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://techcrunch.com/2011/05/18/zynga-continues-shopping-spree-buys-social-game-studio-dna-games/", entry_date="2010",
    note="Social casino games on Facebook (Casino City, Bar World). 'The startup has raised $2 million in new funding from Battery Ventures "
         "and Bain Capital Ventures' (TechCrunch, 2011-05-18), its only reported round, read as the seed with sibling Battery; 'DNA Games "
         "was acquired by Zynga in May 2011' (the firm's 2012 page, Adam Marchick). City from the firm's 2010 listing (1111 Bayhill "
         "Street, San Bruno, CA); sibling Battery reads Austin without a source. Graduation left for the graduation pass."))
L.append(cls("driven", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Data Infrastructure", stage="undetermined",
    note="Concurrent, Inc. (San Francisco, the company behind Cascading) rebranded as Driven, which the firm listed in 2016-2017; the row "
         "is one company with 'concurrent' (BCV's 2014 Form D, Salil Deshpande). Xplenty acquired Concurrent/Driven in 2017 "
         "(https://www.cascading.org/2017/03/22/driven-to-xplenty-what-does-this-mean-for-cascading/). BCV's round is not named."))

# ---- archive rows, 2003-2013 listings
L.append(cls("closings-ltd", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Fintech & Payments", stage="undetermined",
    note="Closings, Ltd., listed by the firm in 2006 ('Early', Acquired). No source read gives its business in detail, its location or "
         "the acquirer; the focus reads the name (real-estate closing services)."))
L.append(cls("cmc", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown", "model_disputes_source"],
    focus="SaaS", stage="undetermined",
    note="CMC, listed by the firm in 2006 ('Early') with the outcome Acquired, which replaces the prefilled 'defunct' from an unrelated "
         "join. No source read identifies the business or its location; the focus is a placeholder reading."))
L.append(cls("cogency-software", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="SaaS", stage="undetermined",
    note="Cogency Software, Inc., on the firm's 2003 listing only. Still operating in 2003-2004 (a customer in Oryx Technology's 10-KSB; "
         "Kate Mitchell of BA Ventures on its board per Acusphere's 2004 S-1). No source read gives its later fate or its location."))
L.append(cls("convey-software", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="SaaS", stage="undetermined",
    note="Enterprise software (611 Mission Street, San Francisco, the firm's 2006 listing, 'Early', Acquired; its CFO in 2002-2003 per "
         "Agile Software's 2005 proxy). The acquirer and BCV's round are not named."))
L.append(cls("datachannel", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Bellevue",
    focus="SaaS", stage="undetermined",
    note="XML and enterprise portal software (DataChannel, Inc., a Washington corporation, Bellevue). 'On December 14, 2001 ... Netegrity, "
         "Inc. completed its acquisition of DataChannel' (Netegrity 8-K, https://www.sec.gov/Archives/edgar/data/840824/000095013501503975/b414648ke8-k.txt). "
         "The firm listed it in 2003; BCV's round is not named."))
L.append(cls("datasynapse", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Data Infrastructure", stage="undetermined",
    note="Grid and application virtualization software (632 Broadway, New York, the firm's 2006 listing, 'Midstage', Michael Krupka). "
         "'DataSynapse was acquired by Tibco in August 2009' (the firm's 2012 page); Bain Capital Venture Fund 2001, L.P. was the "
         "stockholder representative in the merger agreement (TIBCO 8-K, 2009-08-24). BCV held it by 2003; the round is not named."))
L.append(cls("definity-health", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Minneapolis",
    focus="Healthcare & Bio", stage="undetermined",
    note="Consumer-directed health plans (Minneapolis). UnitedHealth Group 'completed its acquisition of Definity Health Corporation' in "
         "the fourth quarter of 2004 (its 8-K exhibit of 2005-01-20). The firm listed it in 2006 and 2010 ('Early'); the round is not named."))
L.append(cls("dexterus", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="SaaS", stage="undetermined",
    note="DexterUs (dexterus.com), listed by the firm in 2006 ('Early', Acquired). Bain Capital managing director Stephen Pagliuca sat on "
         "its board around 2000-2001 (Gartner's and IOS Brands' 2001 proxies). No source read gives its business in detail, location or "
         "acquirer; the focus is a placeholder reading."))
L.append(cls("e5-systems", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", city="Reston",
    focus="SaaS", stage="undetermined",
    note="Web-based modernization of legacy applications (Reston, VA; Sterling, VA in 2010). Listed by the firm from 2003 to 2013 (Michael "
         "Krupka) without an exit; no source read gives its later fate. The round is not named."))
L.append(cls("ecredit-com", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Dedham",
    focus="Fintech & Payments", stage="undetermined",
    note="Credit decisioning software (eCredit.com, Dedham, MA). Internet Capital Group held 32% in 2004 (its 8-K exhibit of 2005-02-17); "
         "Bain Capital managing director Mark Nunnelly sat on its board (CTC Communications' 2001 proxy). The firm's 2006 listing marks "
         "it Acquired; the acquirer and BCV's round are not named."))
L.append(cls("el-dorado-marketing", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", city="Wellesley",
    focus="Media, Gaming & Advertising", stage="undetermined",
    note="Marketing services (El Dorado Marketing Group, Wellesley, MA), listed by the firm in 2006 and 2010 ('Early') without an exit. "
         "Bain Capital Partners managing director Michael Ward sat on its board (Houghton Mifflin's 2005 10-K). No source read gives its "
         "later fate."))
L.append(cls("environmental-data-resources-inc", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Milford", focus="SaaS", stage="undetermined",
    note="Environmental risk information for property transactions (EDR, Milford, CT), listed by the firm in 2003 (as 'EData Resources', "
         "which merges here), 2006 and 2010 ('Early', Acquired). The acquirer and BCV's round are not named."))
L.append(cls("epoch", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Waltham",
    focus="Healthcare & Bio", stage="undetermined", flags=["model_disputes_source"],
    note="EPOCH Senior Living (epochsl.com; Brewster, MA in the firm's 2006 listing, 'Expansion/Growth Buyout'), still operating: "
         "'Waltham, Massachusetts-based EPOCH Senior Living' (Westfair, 2026-08-12, " + NEWS("epoch", "branches out into Brookfield") + "). "
         "The prefilled 'acquired' and Japan came from wrong joins (Epoch Holding Corp; a Japanese Epoch). Bain Capital managing "
         "directors Stephen Pagliuca and John Connaughton sat on its board (DDI's 2001 and Stericycle's 2003 proxies); the round and "
         "the vehicle are not named."))
L.append(cls("eprise-corporation", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Framingham",
    focus="SaaS", stage="undetermined",
    note="Web content management (Eprise Corporation, Framingham, MA). IPO March 2000 (NASDAQ: EPRS); divine, inc. acquired it in 2001 "
         "(Interland's 2003 S-4 lists 'divine Inc. - Eprise Corp.'). The firm listed it in 2003; its IPO prospectus and 2001 proxy name "
         "no Bain holder among 5% owners, so the round is not named."))

# ---- verdicts
L.append(verdict("eschelon-telecom", "not_member",
    "[bain_capital_heritage] Another desk (decisions.md D2, R1): Eschelon Telecom's IPO prospectus (424B1, 2005-08-04) names Bain Capital "
    "Fund VI, L.P. (general partner Bain Capital Partners VI under Bain Capital Investors, LLC) and its BCIP co-investment entities as "
    "the Bain holder, bought in rounds from 1999 (Mark Nunnelly on the board from September 1999, Ian Loring from 2001, both private-"
    "equity managing directors), with no venture vehicle. Fund VI, Wind Point and Stolberg together held 88% before the IPO. A "
    "generalist-fund position, not BCV's, although the firm listed it in 2006-2013.",
    ec="site_listing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1110507/000104746905020767/a2161812z424b1.htm"))
L.append(verdict("ctc-communications", "not_member",
    "CTC Communications Group was listed on NASDAQ when Bain Capital Fund VI, L.P. bought 75,000 shares of its convertible preferred "
    "stock (Schedule 13D of 2000-05-26, beside Thomas H. Lee Equity Fund IV), with Mark Nunnelly joining the board in June 2000 "
    "(CTC's 2001 proxy). A placement into a listed company is not a venture round (COLLECTION.md s1 T3; decisions.md D4), and the "
    "holder was a generalist fund, not a BCV vehicle (D2).",
    ec="site_listing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1092319/000105611401500004/proxy.txt"))

if __name__ == "__main__":
    jl.write("batch-007", L)
