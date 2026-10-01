"""PRO-82 grind, batch-004 (hutch-games .. nexos-ai). Same evidence and conventions as batch-001. micromet and
minerva-neurosciences are life sciences desk rows (judgments-life.py)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("hutch-games", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile racing games studio (London; founded 2011); the firm's list marks it backed at Seed; a $5.5M round with Mattel in 2017; acq. by Modern Times Group, 2020 (up to $375M; the firm's post of 2020-12-08)"))
ug = nqurl('"Immersive Gamebox" administration OR acquired', "Immersive Gamebox Acquired and Recapitalized")
L.append(C("immersive-gamebox", status="acquired", country="GB", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Group gaming rooms with projection and motion tracking, formerly Electric Playbox and Electric Gamebox (London); the firm's list marks it backed at Seed, Danny Rimer and Georgia Stevenson; venture debt in 2022; 'Acquired and Recapitalized Amid New Leadership' (PR Newswire, 2025-02-11); Project A's row reads acquired",
    extra={"status_citation": ug}))
u = post("incident-io-raises", "4-7"); g = post("incident-io-raises-62m")
L.append(C("incident-io", status="private", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2021-09", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="DevTools & APIs",
    note="Incident management platform (London; founded by former Monzo engineers); the $4.7M seed led by Index and Point Nine (the firm's post, 2021-09-30), a $28.7M Series A led by Index in July 2022, 'a $62 million Series B' at a $400M valuation (the firm's post, 2025-04-10)",
    rounds=[rnd("2021-09-30", "Seed", 4700000, "Index Ventures, Point Nine", True, u, "firm"), rnd("2022-07-13", "Series A", 28700000, "Index Ventures", True, None, "press"), rnd("2025-04-10", "Series B", 62000000, "Insight Partners", True, g, "firm")]))
u = news("Instabase", "Raises Massive $105M Series B")
L.append(C("instabase", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2019-10", focus="AI & Applied AI",
    note="Document-understanding platform for enterprises (San Francisco); Index led the $105M Series B of October 2019 at about $1B, Sarah Cannon on the board (Crunchbase News, 2019-10-21); $2B at the 2023 Series C",
    rounds=[rnd("2019-10-21", "Series B", 105000000, "Index Ventures", True, u, "press")]))
L.append(C("intercom", dispute=("status", "rng", "usd"), status="acquired", city="San Francisco", stage="Growth", stage_src="model", stage_conf="high", entry_date="2016-04", rng="below_1b",
    focus="SaaS", note="Customer messaging and AI support agent, renamed Fin (San Francisco; founded by Irish founders); Index led the $50M round of April 2016, Ilya Fushman then Mark Goldberg the partner, and joined the $125M Series D of March 2018 at $1.275B (the firm's post); acq. by Salesforce, 2026 ($3.6B; Irish Independent, 2026-06-15; GV's row records the closing)",
    rounds=[rnd("2016-04", "Series C extension", 50000000, "Index Ventures", True, None, "press"), rnd("2018-03-27", "Series D", 125000000, "Kleiner Perkins", True, post("intercom-announces-125-million"), "firm")]))
u = post("iterable-raises-23m")
L.append(C("iterable", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2016-12", focus="SaaS",
    note="Cross-channel marketing automation (San Francisco); 'a $23M Series B round of funding led by Index Ventures' (the firm's post, 2016-12-13), Shardul Shah on the board; $2B at the June 2021 Series E",
    rounds=[rnd("2016-12-13", "Series B", 23000000, "Index Ventures", True, u, "firm")]))
u = post("expert-hair-colourist-josh-wood")
L.append(C("josh-wood-colour", status="private", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2019-03", rng="below_1b", focus="Consumer & Marketplaces",
    note="At-home hair colour brand (London); 'Index Ventures ... led the $6.5 million Series A round' with JamJar and Venrex (the firm's post, 2019-03-11)",
    rounds=[rnd("2019-03-11", "Series A", 6500000, "Index Ventures", True, u, "firm")]))
u = post("jump-raises-4-million"); g = post("jump-steps-up-mission")
L.append(C("jump", status="private", country="FR", city="Paris", stage="Seed", **WV, stage_cite=u, entry_date="2021-11", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="Fintech & Payments",
    note="Employment-style contracts and benefits for freelancers (join-jump.com, Paris); 'led us to lead Jump's EUR 4m seed round in 2021 ... we're joining a new EUR 11m Series A round' (the firm's posts, 2021-11-30 and 2024-09-23); the Jump of the Battery, Insight and Menlo books are other companies",
    rounds=[rnd("2021-11-30", "Seed", None, "Index Ventures", True, u, "firm"), rnd("2024-09-23", "Series A", None, None, True, g, "firm")]))
L.append(C("justpark", status="acquired", country="GB", country_src="wikidata", city="London", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Parking marketplace, formerly ParkatmyHouse (London); Index invested in 2014 in a round no source read names (the firm's 2014 page; BMW i Ventures had invested in 2011; an equity crowdfunding followed in 2015); merged with ParkHub in 2024 under FTV Capital and LLR Partners (Business Wire, 2024-03-21)", rounds=[]))
L.append(C("justworks", status="private", country="US", city="New York", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014", rng="below_1b", focus="SaaS",
    note="Payroll, benefits and compliance for small businesses (New York); Index joined the $6M Series A of 2014 led by Thrive (Terrence Rohan, then Danny Rimer the partner on the firm's pages); Redpoint led the $33M Series C of 2016; filed an S-1 in 2021 and withdrew it in 2022; the last disclosed round is undisclosed in price and vendor marks do not band a row (Rule A)"))
L.append(C("kaggle", city="San Francisco", rng="below_1b", focus="AI & Applied AI",
    note="Data science competitions and community (San Francisco; founded in Melbourne); Index and Khosla led the $11M Series A of November 2011, Neil Rimer on the board; acq. by Google, 2017"))
L.append(C("kano", status="private", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Build-it-yourself computer kits for children (London); the $15M Series A of May 2015 led by Breyer Capital with Index (the Guardian, 2015-05-06; Saul Klein and James Higa on the Form D), $28M Series B in 2017 (the firm's post)"))
u = post("kayrros-secures-24m")
L.append(C("kayrros", status="private", country="FR", country_src="wikidata", city="Paris", stage="Series A", **WV, stage_cite=u, entry_date="2017-01", rng="below_1b", focus="Climate & Energy",
    note="Satellite and data analytics for energy and climate markets (Paris); 'raised EUR 9 million in Series A funding in January 2017 led by Index Ventures' (the firm's post on the Series B, 2018-09-18), Dominique Vidal; EUR 40M in 2022",
    rounds=[rnd("2017-01", "Series A", None, "Index Ventures", True, u, "firm"), rnd("2018-09-18", "Series B", None, "Cathay Innovation", True, u, "firm")]))
u = post("resilience-and-adaptability")
L.append(C("kong", dispute=("stage",), status="private", city="San Francisco", rng="1b_plus", **sv("kong", "a16z"), stage="Seed", stage_src="model", stage_conf="medium", entry_date="2011-09",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="DevTools & APIs", flags=["stage_uncited"],
    note="API gateway and service connectivity, founded as Mashape (San Francisco); Index backed the $1.5M seed of 2011 with NEA and CRV (Form D 2011-Q3, $1.7M; the firm's list marks it backed at Seed) and led 'their Series C financing of $43M' (the firm's post, 2019-03-27); the band read the 2018 filing; $2B at the $175M Series E of November 2024 (aligned to a16z's cited mark)",
    extra={"entry_stage_confidence": "low"},
    rounds=[rnd("2011-09", "Seed", 1500000, None, True, None, "filing"), rnd("2019-03-27", "Series C", 43000000, "Index Ventures", True, u, "firm")]))
u = post("kry-the-swedish-video-based-healthcare-provider-raises"); g = post("kry-the-swedish-video-based-healthcare-provider-announces")
L.append(C("kry-livi", status="private", country="SE", city="Stockholm", stage="Seed", **WV, stage_cite=u, entry_date="2016-08", rng="1b_plus",
    usd=2000000000, val_src="web_verified", val_cite="https://www.fiercebiotech.com/medtech/kry-raises-316m-series-d-upping-valuation-to-2b", asof="2021-04-27",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="Healthcare & Bio", flags=["stale"],
    note="Video-based primary care, Kry in the Nordics and Livi elsewhere (Stockholm); the EUR 6.1M seed round of August 2016 with Creandum and Project A, Ben Holmes joining the board, then the EUR 20M Series A of June 2017 led by Index (the firm's posts); $2B at the April 2021 Series D (the mark Accel, Creandum and Project A carry), stale beyond 24 months",
    rounds=[rnd("2016-08-17", "Seed", None, None, True, u, "firm"), rnd("2017-06-28", "Series A", None, "Index Ventures", True, g, "firm")]))
u = narch("first green tech investment in Lehigh")
L.append(C("lehigh-technologies", dispute=("stage",), status="acquired", city="Tucker", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2008-06",
    focus="Climate & Energy", note="Micronized rubber powder from end-of-life tyres (Tucker, Georgia; founded 2003); 'Index makes first green tech investment in Lehigh Technologies' (the firm's own news item, 2008-06-19), the $34.5M round with Kleiner Perkins, Neil Rimer on the board; the band read a $0.1M filing of 2009; acq. by Michelin, 2017",
    rounds=[rnd("2008-06-19", "Growth round", 34500000, "Index Ventures, Kleiner Perkins", True, u, "firm")]))
L.append(C("lever", status="acquired", city="San Francisco", rng="below_1b", focus="SaaS",
    note="Applicant tracking and recruiting software (San Francisco; founded 2012); the firm's list marks it backed at Seed, Terrence Rohan the partner on its 2014 page; Series A led by Redpoint in 2014; acq. by Employ, 2022"))
L.append(C("lightning-ai", status="private", country="US", city="New York", rng="below_1b", focus="AI & Applied AI",
    note="Platform for building and training AI models, from the creators of PyTorch Lightning; founded as Grid.ai (New York); Index led the $18.6M Series A of October 2020 ('Grid.ai: Defying Convention', the firm's post) and its list marks the company backed at Seed; $40M Series B in 2022, $50M in November 2024"))
v = news("Linear", "Completes $99 Million Tender At $2.5 Billion")
L.append(C("linear", status="private", country="US", city="San Francisco", rng="1b_plus", usd=2500000000, val_src="web_verified", val_cite=v, asof="2026-08-28", focus="SaaS",
    note="Issue tracking and product planning for software teams (San Francisco; Finnish founders); the 2019 seed led by Sequoia with Index, which the firm's list marks; $1.25B at the June 2025 Series C, then a $99M tender at $2.5B in August 2026 (Pulse 2.0), a priced event"))
u = post("dolly-parton-linktree")
L.append(C("linktree", status="private", country="AU", city="Melbourne", stage="Growth", **WV, stage_cite=u, entry_date="2021-03", rng="1b_plus", **sv("linktree", "coatue"),
    focus="Consumer & Marketplaces", flags=["stale"], note="Link-in-bio pages for creators and brands (Melbourne); 'Linktree announces $45m investment co-led by Index' (the Series B; the firm's post by Georgia Stevenson, 2021-03-25), then co-led the $110M round of March 2022 at $1.3B (aligned to Coatue's cited mark), stale",
    rounds=[rnd("2021-03-25", "Series B", 45000000, "Index Ventures, Coatue", True, u, "firm")]))
L.append(C("lithic", status="private", country="US", city="New York", rng="below_1b", focus="Fintech & Payments",
    note="Card-issuing API, founded as Privacy.com and renamed in 2021 (New York); the firm's 2020 page lists Privacy.com with Mark Goldberg and its list marks the company backed at Seed; $43M Series B in May 2021, $60M Series C in July 2021"))
u = post("loctax-raises-12m"); ul = news("Loctax", "Tax Systems Acquires Loctax")
L.append(C("loctax", status="acquired", country="BE", city="Leuven", stage="Series A", **WV, stage_cite=u, entry_date="2022-09", rng="below_1b", focus="SaaS",
    note="Tax governance and collaboration platform for in-house tax teams (Belgium); Index led the $12M Series A (the firm's post, 2022-09-21), Hannah Seal and Carlos Gonzalez-Cadenas; acq. by Tax Systems, 2025 (Business Wire, 2025-10-08)",
    rounds=[rnd("2022-09-21", "Series A", 12000000, "Index Ventures", True, u, "firm")], extra={"status_citation": ul}))
L.append(C("lookout", dispute=("usd", "rng"), city="Boston", rng="below_1b", focus="Security",
    note="Mobile and cloud endpoint security (founded in San Francisco, now Boston); Index led the $40M Series D of 2011, Mike Volpi on the board; the 2014 round priced it at $1B, but the consumer business was sold to F-Secure in 2023 and later secondaries priced it near $300M (COLLECTION.md s6: a stale primary mark yields to documented collapse evidence); the a16z, Accel, Greylock and Khosla rows read below $1B"))
L.append(C("loop", status="private", country="US", city="Chicago", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2023-08", rng="below_1b", focus="Fintech & Payments",
    note="Freight audit and payment platform (loop.com; San Francisco and Chicago); Index joined the $35M Series B of August 2023 led by J.P. Morgan Growth Equity Partners, Mark Fiorentino then Nina Achadjian the partner; Founders Fund had led the Series A"))
u = post("matera-raises-10m")
L.append(C("matera", dispute=("country",), status="private", country="FR", city="Paris", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2020-01", rng="below_1b",
    focus="SaaS", note="Self-management platform for co-owned residential buildings, formerly illiCopro (Paris); Index led the EUR 10M Series A (the firm's post, 2020-01-15), then joined the EUR 35M Series B of May 2021; the pre-filled IT is a one-word name join (the Italian city)",
    rounds=[rnd("2020-01-15", "Series A", None, "Index Ventures", True, u, "firm")]))
u = post("smb-payments-are-going-vertical")
L.append(C("mercantile", status="acquired", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2022-10", rng="below_1b", focus="Fintech & Payments",
    note="Branded business credit cards for trade associations and marketplaces (New York); 'we're leading Mercantile's $15M Series A' (the firm's post by Mark Fiorentino, 2022-10-12); the First Round and General Catalyst rows record its sale",
    rounds=[rnd("2022-10-12", "Series A", 15000000, "Index Ventures", True, u, "firm")]))
L.append(C("metromile", city="San Francisco", rng="below_1b", focus="Fintech & Payments",
    note="Pay-per-mile car insurance (San Francisco; Nasdaq: MILE via SPAC, 2021); Index led the 2013 Series A, Neil Rimer on the board (Form D 2013-04, $10.2M); acq. by Lemonade, 2022"))
u = narch("Mimecast secures")
L.append(C("mimecast", country="GB", country_src="wikidata", city="London", stage="Growth", **WV, stage_cite=u, entry_date="2009-09", rng="below_1b", focus="Security",
    note="Cloud email security and archiving (London; Nasdaq: MIME, IPO November 2015); Index led the Series B, 'Mimecast secures GBP 13 million in Series B funding' (the firm's own news item, 2010-01-25); the Index funds filed 13Gs after the IPO; acq. by Permira, 2022 ($5.8B)",
    rounds=[rnd("2010-01-25", "Series B", None, "Index Ventures", True, u, "firm")]))
u = post("mistral-ai-for-tomorrows-enterprise")
L.append(C("mistral", status="private", country="FR", city="Paris", stage="Seed", **WV, stage_cite=u, entry_date="2023-06", rng="10b_plus", **sv("mistral", "headline"),
    grad="graduated", grad_src="first_party", grad_cite=u, focus="AI & Applied AI",
    note="Foundation models and enterprise AI (Mistral AI, Paris); 'after cutting that first seed check for Mistral' in the EUR 105M seed of June 2023 led by Lightspeed, Index joined 'a Series C funding round of EUR 1.7bn at a EUR 11.7bn post-money valuation' (the firm's post, 2025-09-09); mark aligned to Headline's cited figure for the 2026 round",
    rounds=[rnd("2023-06-13", "Seed", 113000000, "Lightspeed", True, u, "firm"), rnd("2025-09-09", "Series C", None, "ASML", True, u, "firm")]))
u = news("Monad", "Index Ventures-led Series A")
L.append(C("monad", status="private", country="US", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2021-08", rng="below_1b", focus="Security",
    note="Security data platform (trymonad.co, San Francisco); emerged from stealth with $17M, the 'Index Ventures-led Series A' (FinTech Global, 2021-08-27), Carlos Gonzalez-Cadenas; not the Monad blockchain",
    rounds=[rnd("2021-08-26", "Series A", 17000000, "Index Ventures", True, u, "press")]))
u = news("Monograph", "Raises $7.4 million in Series A")
L.append(C("monograph", status="private", country="US", city="San Francisco", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2021-06", rng="below_1b",
    focus="SaaS", note="Practice-management software for architects and engineers (San Francisco); the $7.4M Series A of June 2021 led by Index, Nina Achadjian (Architect Magazine, 2021-06-02); $20M Series B in February 2025",
    rounds=[rnd("2021-06-02", "Series A", 7400000, "Index Ventures", True, u, "press")]))
u = post("montonio-raises-11m")
L.append(C("montonio", status="private", country="EE", city="Tallinn", stage="Series A", **WV, stage_cite=u, entry_date="2022-04", rng="below_1b", focus="Fintech & Payments",
    note="Checkout, payments and post-purchase platform for online merchants (Tallinn); the EUR 11M Series A led by Index (the firm's post, 2022-04-12; PYMNTS names the round)",
    rounds=[rnd("2022-04-12", "Series A", None, "Index Ventures", True, u, "firm")]))
L.append(C("moo", dispute=("status", "country"), status="private", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006", rng="below_1b",
    focus="Consumer & Marketplaces", note="Online print and business cards (London; founded 2004); Index and Atlas Venture led the 2006 Series A, Neil Rimer on the board; 'Robin Klein ... who was a seed investor in MOO' did so through The Accelerator Group before he joined Index, not with fund money (T2), which is why the firm's 2012 list also files it under Seed stage; the pre-filled 'acquired' and TW are a one-word Wikidata join"))
L.append(C("motive", dispute=("stage",), status="private", city="San Francisco", rng="1b_plus", **sv("motive", "gv"), stage="Series A", stage_src="model", stage_conf="high", entry_date="2016-01",
    focus="SaaS", flags=["stale", "cite_pending"],
    note="Fleet management and driver safety, founded as KeepTruckin (San Francisco); Index led the $8M Series A announced January 2016 (Form D 2015-Q3, $8.0M), then joined the $50M Series C of 2018 and the $149M Series D of 2019 (the firm's posts); $2.85B at the May 2022 Series F (aligned to GV's cited mark), stale; an S-1 filed in 2025 and the IPO called off in September 2026",
    rounds=[rnd("2016-01", "Series A", 8000000, "Index Ventures", True, None, "filing"), rnd("2018-03-20", "Series C", 50000000, "IVP", True, post("keeptruckin-raises-50-million"), "firm")]))
u = post("motorway-driving-new-business")
L.append(C("motorway", status="private", country="GB", city="London", stage="Growth", **WV, stage_cite=u, entry_date="2021-06", rng="1b_plus", **sv("motorway", "iconiq-growth"),
    focus="Consumer & Marketplaces", flags=["stale"], note="Used-car marketplace selling to dealers by auction (London); 'leading their GBP 48m Series B fundraise' (the firm's post, 2021-06-14); 'unicorn status with $190m Series C' in November 2021 (aligned to ICONIQ's cited mark), stale",
    rounds=[rnd("2021-06-14", "Series B", None, "Index Ventures", True, u, "firm")]))
u = post("whitehat-raises-16m")
L.append(C("multiverse", status="private", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2019-07", rng="1b_plus", **sv("multiverse", "general-catalyst"),
    focus="SaaS", note="Apprenticeships and workforce upskilling, founded as WhiteHat (London); 'WhiteHat Raises $16m Series A Led by Index' (the firm's post, 2019-07-15), Danny Rimer on the board; mark aligned to General Catalyst's cited figure",
    rounds=[rnd("2019-07-15", "Series A", 16000000, "Index Ventures", True, u, "firm")]))
L.append(C("myheritage", status="acquired", city="Or Yehuda", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online genealogy and DNA testing (Or Yehuda, Israel); Index led the $15M round of September 2008 with Accel (the firm's own news item, 2008-09-08), Saul Klein on the board; acq. by Francisco Partners, 2021 (about $600M)"))
L.append(C("nacelle", status="private", country="US", city="Los Angeles", rng="below_1b", focus="SaaS",
    note="Headless commerce platform (Los Angeles); the firm's list marks it backed at Seed, Damir Becirovic the partner; an $18M Series A and a $50M Series B led by Tiger Global in 2021 (PR Newswire, 2021-08-19)"))
L.append(C("nasty-gal", city="Los Angeles", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online fashion retailer for young women (Los Angeles); Index was the only outside investor in 2012 ($9M, then 'Nasty Gal Secures $40 Million', the firm's own news item of 2012-08-28), Danny Rimer on the board; bankrupt in November 2016, the brand bought by Boohoo in 2017"))
un = news("Natoma", "Snowflake buys Natoma for AI agent control")
L.append(C("natoma", status="acquired", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="Security",
    note="Identity and access governance for AI agents and non-human identities (San Francisco; founded 2023); on the firm's list since 2025, Shardul Shah; Greylock led the seed; the round Index entered is not named on any surface read; acq. by Snowflake, 2026 (StartupHub.ai, 2026-05-28)",
    rounds=[], extra={"status_citation": un}))
L.append(C("navabi", status="acquired", country="DE", city="Aachen", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online retailer of plus-size designer fashion (Aachen); Index invested in the early 2010s, Dominique Vidal on the board, in a round no source read names; a EUR 25M round in January 2015; insolvency in 2019 and the brand acq. by City Chic Collective, 2021 (WWD, 2021-07-29)", rounds=[]))
L.append(C("newfront", city="San Francisco", rng="below_1b", focus="Fintech & Payments",
    note="Tech-enabled commercial insurance brokerage (San Francisco; founded 2017); the firm's list marks it backed at Seed; $100M+ raised by October 2020 at a $500M valuation, $2.2B in April 2022; acq. by Willis Towers Watson, announced December 2025 (up to $1.3B; the YC row records the sale)"))
u = post("nexos-ai-emerges-from-stealth"); g = post("nexos-ai-raises", "series-a")
L.append(C("nexos-ai", status="private", country="LT", city="Vilnius", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2025-01", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="AI & Applied AI",
    note="AI orchestration and gateway platform for enterprises (Vilnius; founded by Nord Security's founders); emerged from stealth with $8M 'led by Index Ventures' in January 2025, the seed (the firm's post; Creandum's row), then 'nexos.ai Raises EUR 30M Series A' in October 2025 (the firm's post): a named later round decides the row inside the clock's window",
    rounds=[rnd("2025-01-17", "Seed", 8000000, "Index Ventures", True, u, "firm"), rnd("2025-10-21", "Series A", None, "Index Ventures, Evantic", True, g, "firm")]))
gl.write("batch-004", L)
