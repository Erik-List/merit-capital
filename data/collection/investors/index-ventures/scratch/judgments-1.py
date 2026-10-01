"""PRO-82 grind, batch-001 (1stdibs .. blue-bottle-coffee). Evidence: scratch/evidence-pack.json (the firm's live page,
its archived claims, Perspectives posts, archived news), scratch/siblings.json, Google News headlines
(news-bulk*.json, nq-cache.json; decoded on citation). Membership of listed rows was seeded by prepare
(site_listing). Rows carrying only the site's "backed at Seed" mark get their stage in the label pass (D8),
graduation of the remaining Seed rows in the graduation pass."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    """Valuation aligned to a sibling book's cited mark (rule 10: one company, one mark)."""
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

u = narch("Growth in online luxury marketplace")
L.append(C("1stdibs", dispute=("stage",), status="public", city="New York", rng="below_1b", **sv("1stdibs", "insight-partners"),
    stage="Growth", **WV, stage_cite=u, entry_date="2012-12", focus="Consumer & Marketplaces",
    note="Luxury design marketplace (New York; NASDAQ: DIBS, IPO June 2021); Index entered in the $42M Series B of December 2012 with Spark and Benchmark (the firm's own news item of 2012-12-03), not the 2013-14 round the Form D band read; market cap aligned to Insight's cited figure",
    rounds=[rnd("2012-12-03", "Series B", 42000000, "Index Ventures", True, u, "firm")]))
u = post("our-investment-in-7ai")
L.append(C("7ai", dispute=("stage",), status="private", city="Boston", rng="below_1b", stage="Series A", **WV, stage_cite=u, entry_date="2025-12",
    focus="Security", note="Agentic security operations (Boston; founded 2024 by Cybereason's founders); Index led the $130M Series A (the firm's post, 2025-12-04) after a $36M seed from Greylock and others (Feb 2025); the Form D band read the size, the record names the round",
    rounds=[rnd("2025-02-06", "Seed", 36000000, None, False, None, "press"), rnd("2025-12-04", "Series A", 130000000, "Index Ventures", True, u, "firm")]))
u = post("bringing-ai-businesses-everywhere")
L.append(C("abacus-ai", status="private", country="US", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2020-07", rng="below_1b",
    focus="AI & Applied AI", note="AI platform for enterprises, ex RealityEngines.AI (San Francisco); 'we are proud to announce our Series A investment in Abacus.ai' (the firm's post, 2020-07-14; $13M); Series B Nov 2020, Series C 2021",
    rounds=[rnd("2020-07-14", "Series A", 13000000, "Index Ventures", True, u, "firm")]))
ua = nqurl('"Adaptive ML" Datadog', "Datadog Acquires Adaptive ML to Accelerate")
L.append(C("adaptive-ml", status="acquired", country="FR", city="Paris", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2023-10", rng="below_1b",
    focus="AI & Applied AI", flags=["stage_uncited"],
    note="Model-tuning platform for enterprises (Paris and New York); Index led the $20M seed with ICONIQ (announced 2024-03-11; the firm's post names no round word); acq. by Datadog, 2026 (Datadog's release, 2026-06-30)",
    rounds=[rnd("2024-03-11", "Seed", 20000000, "Index Ventures", True, post("how-adaptive-is-bringing"), "firm")],
    extra={"status_citation": ua}))
u = post("adfin-deploys-decades"); g = news("Adfin", "Adfin Raises $18M Series A from Index")
L.append(C("adfin", status="private", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2024-07", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="Fintech & Payments",
    note="Billing and payments for small businesses (London); Index co-led the $4.9M seed with Visionaries (the firm's post, 2024-07-05), an EUR 8M seed extension in Feb 2025, then led the $18M Series A (FF News, 2026-05-12)",
    rounds=[rnd("2024-07-05", "Seed", 4900000, "Index Ventures", True, u, "firm"), rnd("2026-05-12", "Series A", 18000000, "Index Ventures", True, g, "press")]))
u = news("Adyen", "received $16 million")
L.append(C("adyen", status="public", country="NL", country_src="wikidata", city="Amsterdam", stage="Series A", stage_src="web_verified", stage_conf="medium",
    stage_cite=u, entry_date="2011", rng="10b_plus", **sv("adyen", "iconiq-growth"), focus="Fintech & Payments",
    note="Global payments platform (Amsterdam; Euronext: ADYEN, IPO June 2018); Index led the $16M Series A of 2011 with Felicis (S&P Capital IQ's transaction record names both), then joined the $250M round of December 2014; market cap aligned to ICONIQ's cited figure",
    rounds=[rnd("2011", "Series A", 16000000, "Index Ventures", True, u, "press"), rnd("2014-12-16", "Growth round", 250000000, "General Atlantic", True, post("adyen-raises-250m"), "firm")]))
L.append(C("adzuna", status="private", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Job search engine (London; founded 2011); on the firm's list since 2012 under its Seed stage filter, Robin Klein the partner; an GBP 8M round in 2018"))
u = post("alan-the-digital-health-insurance-company-announces")
L.append(C("alan", dispute=("status",), status="private", country="FR", city="Paris", stage="Series A", **WV, stage_cite=u, entry_date="2018-04",
    rng="1b_plus", **sv("alan", "coatue"), focus="Fintech & Payments",
    note="Digital health insurer (Paris); Index led the EUR 23M Series A (the firm's post, 2018-04-10: 'investors in the company since their Series A in 2018') and led the 2026 round at about $6B; the pre-filled 'defunct' is a one-word Wikidata join; mark aligned to Coatue's cited figure",
    rounds=[rnd("2018-04-10", "Series A", None, "Index Ventures", True, u, "firm")]))
u = post("how-allara-is-bridging")
L.append(C("allara", status="private", country="US", city="New York", stage="Growth", **WV, stage_cite=u, entry_date="2025-01", rng="below_1b",
    focus="Healthcare & Bio", note="Virtual specialty care for women's hormonal conditions (New York); Index led the $26M Series B (the firm's post by Susana Rojas and Martin Mignot, 2025-01-23) after a $10M Series A in Oct 2023",
    rounds=[rnd("2023-10-18", "Series A", 10000000, None, False, None, "press"), rnd("2025-01-23", "Series B", 26000000, "Index Ventures", True, u, "firm")]))
u = post("anine-bing-closes")
L.append(C("anine-bing", status="private", city="Los Angeles", stage="Series A", **WV, stage_cite=u, entry_date="2018-09", rng="below_1b",
    focus="Consumer & Marketplaces", note="Fashion brand (Los Angeles); the $15M Series A led by Index, Greycroft and Felix Capital (the firm's post, 2018-09-06); Form Ds 2018 and 2019 carry Danny Rimer as director",
    rounds=[rnd("2018-09-06", "Series A", 15000000, "Index Ventures", True, u, "firm")]))
L.append(C("anki", status="defunct", city="San Francisco", rng="below_1b", focus="Consumer & Marketplaces",
    note="Consumer robotics (Anki Drive, Cozmo, Vector; San Francisco); Index joined the $50M round of June 2013 led by Andreessen Horowitz; shut down in April 2019, assets bought by Digital Dream Labs"))
L.append(C("ankorstore", country="FR", country_src="wikidata", city="Paris", stage="Series A", stage_src="model", stage_conf="high", entry_date="2020-12",
    focus="Consumer & Marketplaces", flags=["cite_pending"],
    note="Wholesale marketplace for independent retailers (Paris); Index led the EUR 25M Series A of December 2020; the EUR 250M Series C of January 2022 valued it at EUR 1.75B, 'all existing investors: Index Ventures, Bain Capital Ventures, GFC, Alven and Aglae' (the firm's post, 2022-01-10)",
    rounds=[rnd("2020-12-08", "Series A", None, "Index Ventures", True, None, "press"), rnd("2022-01-10", "Series C", None, "BOND, Tiger Global", True, post("ankorstore-the-fastest"), "firm")]))
u = post("50-year-old-tax-code"); g = news("Anrok", "Series B participation")
L.append(C("anrok", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2021-06", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="Fintech & Payments",
    note="Sales tax compliance for software companies (San Francisco); 'I'm thrilled to co-lead Anrok's $4.3M seed round alongside Bryan Schreier at Sequoia' (the firm's post by Mark Goldberg, 2021-06-14); Series A 2022, $30M Series B 2024 led by Khosla (Business Wire, 2024-05-29)",
    rounds=[rnd("2021-06-14", "Seed", 4300000, "Index Ventures, Sequoia", True, u, "firm"), rnd("2024-04-10", "Series B", 30000000, "Khosla Ventures", None, g, "press")]))
u = post("apex-emerges-from-stealth"); ua = nqurl('"Apex Security" Tenable', "Tenable acquires Sam Altman-backed Apex")
L.append(C("apex", dispute=("country",), status="acquired", country="IL", city="Tel Aviv", stage="Seed", **WV, stage_cite=u, entry_date="2024-05", rng="below_1b",
    focus="Security", extra={"status_citation": ua},
    note="AI security platform (Apex Security, Tel Aviv); the $7M seed co-led by Index and Sequoia (the firm's post, 2024-05-13), the last round before the sale; acq. by Tenable, 2025 (about $105M, Calcalist 2025-05-29); the pre-filled JP is a one-word name join",
    rounds=[rnd("2024-05-13", "Seed", 7000000, "Index Ventures, Sequoia", True, u, "firm")]))
u = post("accessing-international-education")
L.append(C("applyboard-inc", city="Kitchener", stage="Growth", **WV, stage_cite=u, entry_date="2020-09", focus="Consumer & Marketplaces",
    note="International student recruitment platform (Kitchener, Ontario); Index entered in the US $55M Series C extension it co-led with ETS (the firm's post, 2020-09-16); $3.2B at the 2021 Series D",
    rounds=[rnd("2020-09-16", "Series C extension", 55000000, "Index Ventures, ETS", True, u, "firm")]))
u = post("apron-raises-15m")
L.append(C("apron", status="private", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2023-09", rng="below_1b",
    focus="Fintech & Payments", note="Invoice payments for small businesses and accountants (London); 'raised $15 million in Series A funding led by Index Ventures' (the firm's post, 2023-09-28)",
    rounds=[rnd("2023-09-28", "Series A", 15000000, "Index Ventures", True, u, "firm")]))
L.append(C("argent", status="private", country="GB", city="London", rng="below_1b", focus="Crypto & Web3",
    note="Smart-contract crypto wallet (London); a $4M seed in Nov 2018 (TechCrunch: 'from Euro VCs'), a $12M Series A led by Paradigm in March 2020, a $40M Series B in April 2022; the firm's list marks it backed at Seed, Martin Mignot the partner"))
L.append(C("artbinder", status="acquired", city="New York", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014-04", rng="below_1b",
    focus="SaaS", note="Inventory software for art galleries (New York); Index led the $3.2M round of April 2014 that the press named a Series A, Neil Rimer joining the board (Form Ds 2014 and 2015); merged into Artlogic in 2020"))
u = post("arthurai-missing-piece")
L.append(C("arthurai", dispute=("stage",), status="private", city="New York", rng="below_1b", stage="Seed", **WV, stage_cite=u, entry_date="2019",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="AI & Applied AI",
    note="AI model monitoring (Arthur, New York); 'we enthusiastically invested in his seed round two years ago ... Index Ventures will be leading the Series A round for Arthur' (the firm's post, 2020-12-09); the Form D band read the Series A filing, the first carrying Mike Volpi, as the entry",
    rounds=[rnd("2019", "Seed", 3300000, "Index Ventures", True, u, "firm"), rnd("2020-12-09", "Series A", 15000000, "Index Ventures", True, u, "firm")]))
L.append(C("ascend", dispute=("country",), status="private", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2022-01",
    rng="below_1b", focus="Fintech & Payments",
    note="Insurance payments and premium financing (San Francisco); Index led the $30M Series A of January 2022 (PR Newswire, 2022-01-27), First Round had led the seed; the pre-filled CZ is a one-word name join",
    rounds=[rnd("2022-01-27", "Series A", 30000000, "Index Ventures", True, nqurl('"Ascend" insurance payments Series A Index', "Ascend Raises $30M Series A"), "press")]))
L.append(C("atlantic-money", status="acquired", country="GB", city="London", rng="below_1b", focus="Fintech & Payments",
    note="Flat-fee international money transfers (London); a $4.5M seed in 2022 from Amplo, Ribbit, Index and Kleiner Perkins; acq. by Deel, 2024 (Finovate, 2024-12-02)"))
u = post("atlar-launches-to-build")
L.append(C("atlar", status="private", country="SE", city="Stockholm", stage="Seed", **WV, stage_cite=u, entry_date="2022-11", rng="below_1b",
    focus="Fintech & Payments", note="Treasury and payment operations platform (Stockholm; founded by former Tink employees); 'Led by Index Ventures, the seed round of EUR 5 million' (the firm's post, 2022-11-08)",
    rounds=[rnd("2022-11-08", "Seed", None, "Index Ventures", True, u, "firm")]))
L.append(C("attackiq", status="private", city="Los Altos", rng="below_1b", focus="Security",
    note="Breach-and-attack simulation platform (founded in San Diego, now Los Altos); Index led the 2016 Series A (Shardul Shah on the Form Ds from 2016), a $17.6M Series B in 2019 led by Khosla, a $44M Series C in 2021"))
L.append(C("augment", status="private", city="Palo Alto", rng="below_1b", focus="AI & Applied AI",
    note="AI coding assistant (Augment Code, Palo Alto); the $227M Series B of April 2024 at a $977M post-money valuation with Sutter Hill, Index, Innovation Endeavors, Lightspeed and Meritech: within 5% of the $1B edge, below it"))
u = post("aurora-self-driving-and-beyond")
L.append(C("aurora", dispute=("stage", "usd", "rng"), city="Pittsburgh", stage="Series A", **WV, stage_cite=u, entry_date="2018-02",
    rng="10b_plus", **sv("aurora", "lightspeed"), focus="Industrial & Robotics",
    note="Self-driving technology (Aurora Innovation, Pittsburgh; Nasdaq: AUR via Reinvent Technology Partners Y, 2021); 'Aurora raises Series A in a round co-led by Greylock Partners and Index Ventures' (the firm's post, 2018-02-28), Mike Volpi on the board; the band read the 2019 Series B filing; the pre-filled float is stale, market cap aligned to Lightspeed's cited figure",
    rounds=[rnd("2018-02-28", "Series A", 90000000, "Greylock, Index Ventures", True, u, "firm")]))
u = narch("auxmoney raises $12 million")
L.append(C("auxmoney", country="DE", country_src="wikidata", city="Düsseldorf", stage="Growth", **WV, stage_cite=u, entry_date="2013-03", rng="below_1b",
    focus="Fintech & Payments", note="Consumer lending marketplace (Düsseldorf; founded 2007); Index and Union Square Ventures entered in the $12M round of March 2013 (the firm's own news item), a later-stage round of a six-year-old company; Centerbridge took a majority in 2020. The firm's list marks it 'backed at Seed', which the record does not bear out (D8 score)",
    rounds=[rnd("2013-03-12", "Growth round", 12000000, "Index Ventures, Union Square Ventures", True, u, "firm")]))
u = post("a-transformational-moment-in-gaming")
L.append(C("backbone", dispute=("status", "country"), status="private", country="US", city="Vancouver", stage="Series A", **WV, stage_cite=u, entry_date="2022-02",
    rng="below_1b", focus="Consumer & Marketplaces",
    note="Mobile gaming controller and app (Backbone Labs, Vancouver, Washington); 'leading their $40M Series A' (the firm's post, 2022-02-23); the pre-filled 'acquired' and CZ are a one-word Wikidata join",
    rounds=[rnd("2022-02-23", "Series A", 40000000, "Index Ventures", True, u, "firm")]))
L.append(C("ballertv", status="private", country="US", city="Pasadena", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Live streaming of youth and amateur sports (Pasadena, California); on the firm's list since 2019, Danny Rimer and Dino Becirovic; no source read names the round Index entered (Google News 2026-10-01: nothing with the firm's name)", rounds=[]))
L.append(C("beam", dispute=("status",), status="private", city="New York", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2022-04", rng="below_1b",
    focus="SaaS", note="Charitable-giving loyalty software for consumer brands (Beam Impact, New York); the $13.3M Series A of April 2022 led by Index (TechCrunch, 2022-04-14), Damir Becirovic; the pre-filled 'acquired' is a one-word Wikidata join",
    rounds=[rnd("2022-04-14", "Series A", 13300000, "Index Ventures", True, nqurl('"Beam Impact" raises', "Beam Impact raises $13.3M to turn"), "press")]))
u = post("helping-facebook-win")
L.append(C("beamery", status="private", country="GB", city="London", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2017-04",
    rng="1b_plus", **sv("beamery", "eqt-ventures"), focus="SaaS", flags=["stale"],
    note="Talent lifecycle management software (London); 'raised $5 million funding from Index Ventures' (the firm's post, 2017-04-11), the round the press named its Series A; Series B $28M 2018, $138M Series C 2021, $50M Series D at $1B in December 2022 (aligned to EQT Ventures' cited mark), stale beyond 24 months",
    rounds=[rnd("2017-04-11", "Series A", 5000000, "Index Ventures", True, u, "firm")]))
u = post("beauty-pie-raises-100m")
L.append(C("beauty-pie", status="private", city="London", stage="Growth", **WV, stage_cite=u, entry_date="2021-09", rng="below_1b",
    focus="Consumer & Marketplaces", note="Members' club for luxury beauty products (London); Index led the $100M Series B (the firm's post, 2021-09-08), Danny Rimer",
    rounds=[rnd("2021-09-08", "Series B", 100000000, "Index Ventures", True, u, "firm")]))
L.append(C("because", status="private", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Personal care brand for older adults (Because Market, San Francisco); on the firm's list since 2019, Mike Volpi; no source read names the round Index entered", rounds=[]))
L.append(C("behavox", status="private", city="New York", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2017", rng="below_1b",
    focus="Fintech & Payments", note="Compliance and conduct surveillance for financial firms (founded in London, run from New York and Montreal); Index led the $20M Series B of 2017, Jan Hammer; $100M from SoftBank Vision Fund 2 in Feb 2020, $175M of structured capital from HPS in June 2026 with no priced valuation"))
u = post("big-health-raises-12m")
L.append(C("big-health", status="private", city="San Francisco", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2014", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="Healthcare & Bio", flags=["stage_uncited"],
    note="Digital therapeutics for insomnia and anxiety (Sleepio, Daylight; founded in London, now San Francisco); Index led the $3.3M seed of 2014 (the firm's 2014 page names Neil Rimer and Ophelia Brown); the $12M round of July 2016 led by Octopus names Index a 'returning investor' (the firm's post), a step-up past twice the seed",
    rounds=[rnd("2014", "Seed", 3300000, "Index Ventures", True, None, "press"), rnd("2016-07-27", "Series A", 12000000, "Octopus Ventures", True, u, "firm")]))
L.append(C("big-switch", status="acquired", city="Santa Clara", rng="below_1b", focus="Data Infrastructure",
    note="Software-defined networking (Big Switch Networks, Santa Clara); Index co-led the 2011 Series A with Khosla, Mike Volpi on the board (Form Ds 2011-2017); acq. by Arista Networks, 2020"))
u = news("Bigger Games", "scores $6 million seed round from Index")
L.append(C("bigger-games", status="private", country="TR", city="Istanbul", stage="Seed", **WV, stage_cite=u, entry_date="2020-12", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Mobile puzzle games studio (Istanbul; founded by former Peak Games staff); the $6M seed led by Index (Tech.eu, 2020-12-02); sold its Mergedom title to Original Games in Feb 2023",
    rounds=[rnd("2020-12-02", "Seed", 6000000, "Index Ventures", True, u, "press")]))
u = post("birds-the-first-mass-adopted")
L.append(C("bird", status="acquired", city="Miami", stage="Series A", **WV, stage_cite=u, entry_date="2018-02", rng="below_1b",
    focus="Consumer & Marketplaces", note="Shared electric scooters (founded in Santa Monica, later Miami; NYSE: BRDS via SPAC, 2021); 'our original investment in Bird back in February' 2018, the $15M Series A, then co-led the $100M Series B in March (the firm's posts); Chapter 11 in December 2023, the business sold out of bankruptcy to Third Lane Mobility in April 2024 (COLLECTION.md s6: insolvency followed by an asset sale is acquired)",
    rounds=[rnd("2018-02-13", "Series A", 15000000, "Craft Ventures", True, u, "firm"), rnd("2018-03-09", "Series B", 100000000, "Valor, Index Ventures", True, post("bird-announces-100-million"), "firm")]))
L.append(C("birdie", status="private", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2021-05", rng="below_1b",
    focus="Healthcare & Bio", note="Home care management software (birdie.care, London); Index led the $11.5M Series A of May 2021 (Business Insider, 2021-05-11), then joined the $30M Series B led by Sofina in June 2022",
    rounds=[rnd("2021-05-11", "Series A", 11500000, "Index Ventures", True, nqurl('"Birdie" home care Index Ventures', "Raises $11.5m in Fresh VC Funding"), "press")]))
u = post("bit-odd-raises")
L.append(C("bit-odd", status="private", country="FI", city="Helsinki", stage="Seed", **WV, stage_cite=u, entry_date="2022-06", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="Media, Gaming & Advertising",
    note="Mobile games studio founded by Supercell veterans (Helsinki); 'BIT ODD's initial EUR 5M seed round led by Index ... Since we invested at seed in 2022'; the EUR 17M round of November 2024 led by Griffin Gaming Partners, a step-up past twice the seed (the firm's post, 2024-11-14)",
    rounds=[rnd("2022-06-28", "Seed", None, "Index Ventures", True, u, "firm"), rnd("2024-11-14", "Series A", None, "Griffin Gaming Partners", True, u, "firm")]))
u = narch("Why we’re backing BitPay")
L.append(C("bitpay", status="private", city="Atlanta", stage="Series A", **WV, stage_cite=u, entry_date="2014-05", rng="below_1b", focus="Crypto & Web3",
    note="Bitcoin payment processor (Atlanta); 'we are leading a $30m (EUR 22m) Series A investment round in BitPay' (the firm's own post, 2014-05-13)",
    rounds=[rnd("2014-05-13", "Series A", 30000000, "Index Ventures", True, u, "firm")]))
u = post("blablacar-secures-a-100-million")
L.append(C("blablacar", country="FR", country_src="wikidata", city="Paris", stage="Growth", **WV, stage_cite=u, entry_date="2014-07", focus="Consumer & Marketplaces",
    note="Long-distance carpooling and bus marketplace (Paris); 'a $100 million Series C investment round led by Index Ventures' (the firm's post, 2014-07-02), Index's entry; Accel had led the Series B",
    rounds=[rnd("2014-07-02", "Series C", 100000000, "Index Ventures", True, u, "firm")]))
u = post("bloom-wild-secures")
L.append(C("bloom-wild", status="private", city="London", stage="Growth", **WV, stage_cite=u, entry_date="2021-01", rng="below_1b",
    focus="Consumer & Marketplaces", note="Online flower delivery (London); Index entered in the GBP 75M Series D of January 2021 led by General Catalyst (the firm's post, 2021-01-18)",
    rounds=[rnd("2021-01-18", "Series D", None, "General Catalyst", True, u, "firm")]))
L.append(C("blue-bottle-coffee", status="acquired", city="Oakland", rng="below_1b", focus="Consumer & Marketplaces",
    note="Specialty coffee roaster and cafes (Oakland); Index joined the $20M round of October 2012 led by True Ventures, Mike Volpi on the board (Form Ds 2012-2015); Nestle bought a 68% stake in September 2017 at about a $700M valuation"))
gl.write("batch-001", L)
