"""PRO-82 grind, batch-005 (nexthink .. rohlik). Same evidence and conventions as batch-001."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

u = post("nexthink-raises-85m"); uv = nqurl('"Nexthink" Vista Equity $3 billion', "Vista Equity Partners takes majority stake in Nexthink")
L.append(C("nexthink", dispute=("status", "rng", "usd"), status="acquired", country="CH", country_src="wikidata", city="Lausanne", stage="Growth", **WV, stage_cite=u, entry_date="2018-12",
    rng="below_1b", focus="SaaS", note="Digital employee experience software (Lausanne and Boston; an EPFL spin-out); Index led the $85M round of December 2018 (the firm's post), Neil Rimer on the board; $1.1B at the 2021 Series D; Vista Equity Partners took a majority stake at about $3B in October 2025 (Alternatives Watch, 2025-10-27; the firm's post of the same day): a change of control, so the row reads acquired",
    rounds=[rnd("2018-12-12", "Growth round", 85000000, "Index Ventures", True, u, "firm")], extra={"status_citation": uv}))
u = news("Notion", "Why Index Ventures Invested in $2 Billion")
L.append(C("notion", dispute=("usd",), city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2020-04", **sv("notion", "coatue"), rng="10b_plus", focus="SaaS",
    note="Workspace for notes, documents and projects (San Francisco); Index led the $50M round of April 2020 at $2B, its first investment, Sarah Cannon then Danny Rimer the partner (Business Insider, 2020-04-06); mark aligned to Coatue's cited figure. The firm's list marks it 'backed at Seed', which the record does not bear out (D8 score)",
    rounds=[rnd("2020-04-01", "Growth round", 50000000, "Index Ventures", True, u, "press")]))
u = narch("Notonthehighstreet.com secures")
L.append(C("notonthehighstreet", status="acquired", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Curated marketplace for small creative businesses (Richmond, London; founded 2006); 'secures GBP 7.5 million investment from Index Ventures and Greylock Partners' (the firm's own news item, 2010-08-02), Ben Holmes on the board; the item names no round and earlier money had come from Spark Ventures; acq. by Great Hill Partners, 2021",
    rounds=[rnd("2010-08-02", "undisclosed", None, "Index Ventures, Greylock", True, u, "firm")]))
u = post("nova-credit-helping-immigrants")
L.append(C("nova-credit", status="private", country="US", city="New York", stage="Seed", **WV, stage_cite=u, entry_date="2016", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="Fintech & Payments",
    note="Cross-border credit reporting (founded in San Francisco, now New York); 'We made our first investment in Nova Credit when they came out of Y-Combinator in 2016' and led the $16M Series A the post announces (the firm's post by Mark Goldberg, 2018-05-30); $50M Series B led by Kleiner Perkins in 2020",
    rounds=[rnd("2016", "Seed", None, None, True, u, "firm"), rnd("2018-05-30", "Series A", 16000000, "Index Ventures", True, u, "firm")]))
u = narch("Bain Capital Ventures and Index Ventures Invest in Novus")
L.append(C("novus", dispute=("country",), status="acquired", country="US", city="New York", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013-06", rng="below_1b",
    focus="Fintech & Payments", note="Portfolio analytics for institutional investors (New York; founded 2007 and self-funded until then); 'Bain Capital Ventures and Index Ventures Invest in Novus' (the firm's own news item, 2013-06-10), its first institutional round, Jan Hammer on the board; acq. by SEI, 2020; the pre-filled UA is a one-word name join",
    rounds=[rnd("2013-06-10", "Series A", None, "Bain Capital Ventures, Index Ventures", True, u, "firm")]))
u = news("Okendo", "Raises $5.3M Series Seed Investment, Led by Index"); g = news("Okendo", "Raises $26M in Series A")
L.append(C("okendo", status="private", country="AU", city="Sydney", stage="Seed", **WV, stage_cite=u, entry_date="2021-07", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="SaaS",
    note="Customer reviews and loyalty for Shopify merchants (Sydney); 'Okendo Raises $5.3M Series Seed Investment, Led by Index Ventures' (Business Wire, 2021-07-21), Damir Becirovic; $26M Series A in July 2022 (FinSMEs)",
    rounds=[rnd("2021-07-21", "Seed", 5300000, "Index Ventures", True, u, "press"), rnd("2022-07-15", "Series A", 26000000, None, None, g, "press")]))
L.append(C("openx", status="private", city="Pasadena", stage="Series A", stage_src="model", stage_conf="high", entry_date="2007-06", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Programmatic advertising exchange, founded in the UK as Openads (Pasadena); Index led the $5M Series A of 2007 (the firm's late-2007 list carries it as OpenAds), then joined the Series B led by Accel and the $10M Series C of May 2009 (the firm's own news item)"))
u = post("otrium-raises-7-million")
L.append(C("otrium", status="private", country="NL", city="Amsterdam", stage="Series A", **WV, stage_cite=u, entry_date="2019-05", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online outlet for fashion brands' unsold stock (Amsterdam); the EUR 7M Series A led by Index (the firm's post, 2019-05-02; FinSMEs names the round), then the EUR 24M Series B of May 2020",
    rounds=[rnd("2019-05-02", "Series A", None, "Index Ventures", True, u, "firm")]))
u = post("otterize-launches-game-changing"); uo = news("Otterize", "Cyera acquires Otterize")
L.append(C("otterize", status="acquired", country="IL", city="Tel Aviv", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2023-04", rng="below_1b", focus="Security",
    note="Intent-based access control for service-to-service connections (Tel Aviv); the $11.5M seed led by Index at launch (the firm's post and TechCrunch, 2023-04-13), Carlos Gonzalez-Cadenas; acq. by Cyera, 2025 (Calcalist, 2025-06-26)",
    rounds=[rnd("2023-04-13", "Seed", 11500000, "Index Ventures", True, u, "firm")], extra={"status_citation": uo}))
L.append(C("outbrain", status="public", city="New York", rng="below_1b", **sv("outbrain", "lightspeed"), focus="Media, Gaming & Advertising",
    note="Content recommendation network (New York; Nasdaq: OB, IPO July 2021; renamed Teads Holding after buying Teads in 2025); 'Outbrain Raises $35 Million USD in Series D Funding; Led by Index Ventures' (the firm's own news item, 2011-12-14), Dominique Vidal on the board; market cap from Lightspeed's cited figure, re-read in the A/B pass"))
u = narch("$18 Million Investment to OZON.ru Led by Index")
L.append(C("ozon-ru", status="public", country="RU", city="Moscow", stage="Growth", **WV, stage_cite=u, entry_date="2007-04", focus="Consumer & Marketplaces", flags=["needs_web_value"],
    note="Russian e-commerce marketplace (Moscow; founded 1998; Nasdaq IPO November 2020, delisted in 2023, shares trade on the Moscow Exchange); '$18 Million Investment to OZON.ru Led by Index Ventures' (the firm's own news item, 2007-04-03), Giuseppe Zocco on the board; the market cap is read in the A/B pass (rouble quote; the ECB has published no RUB reference rate since March 2022)",
    rounds=[rnd("2007-04-03", "Growth round", 18000000, "Index Ventures", True, u, "firm")]))
L.append(C("path", status="acquired", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2011-02", rng="below_1b", focus="Consumer & Marketplaces",
    note="Private social network app (San Francisco); the $8.5M Series A of February 2011 led by Kleiner Perkins and Index, Mike Volpi on the board (Form Ds 2011-2014); acq. by Daum Kakao, 2015"))
L.append(C("patreon", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2014-06", focus="Media, Gaming & Advertising", flags=["cite_pending"],
    note="Membership platform for creators (San Francisco); Index led the $15M Series A of June 2014, Danny Rimer on the board (the firm's 2014 page names him and Terrence Rohan); $4B at the April 2021 Series F",
    rounds=[rnd("2014-06", "Series A", 15000000, "Index Ventures", True, None, "press")]))
u = news("Pave", "Compensation Startup Raises $100m at $1.6bn Valuation From Index")
L.append(C("pave", status="private", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2022-06", rng="1b_plus", **sv("pave", "a16z"), focus="SaaS", flags=["stale"],
    note="Compensation benchmarking and planning (San Francisco); Index led the $100M Series C at $1.6B (Business Insider, 2022-06-28; aligned to a16z's cited mark), Mark Goldberg then Martin Mignot the partner; stale beyond 24 months",
    rounds=[rnd("2022-06-28", "Series C", 100000000, "Index Ventures", True, u, "press")]))
L.append(C("peanut", status="private", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Social network for women through fertility, motherhood and menopause (London); the firm's list marks it backed at Seed, Danny Rimer and Hannah Seal; EQT Ventures led the $5M Series A of November 2019 (the firm's post); a $12M Series A extension in 2020; no source read confirms the sale Headline's row records"))
u = post("next-step-of-the-restaurant")
L.append(C("pepper", status="private", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2021-11", rng="below_1b", focus="SaaS",
    note="E-commerce and ordering software for food distributors (New York); 'announcing the company's $16M Series A financing. Index led the investment round' (the firm's post, 2021-11-30); $30M Series B led by ICONIQ in 2024",
    rounds=[rnd("2021-11-30", "Series A", 16000000, "Index Ventures", True, u, "firm")]))
u = post("identity-layer-of-the-internet")
L.append(C("persona", dispute=("status", "country"), status="private", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2021-05", rng="1b_plus", **sv("persona", "coatue"),
    focus="Security", note="Identity verification infrastructure (San Francisco); 'our lead role in Persona's $50M Series B' (the firm's post, 2021-05-04), then the $150M Series C with Founders Fund; $2B at the April 2025 Series D (aligned to Coatue's cited mark); the pre-filled 'acquired' and RU are a one-word Wikidata join",
    rounds=[rnd("2021-05-04", "Series B", 50000000, "Index Ventures", True, u, "firm")]))
u = post("personio-raised-40m")
L.append(C("personio", dispute=("usd",), city="Munich", stage="Growth", **WV, stage_cite=u, entry_date="2019-01", **sv("personio", "accel"), rng="1b_plus", focus="SaaS", flags=["stale"],
    note="HR software for small and mid-sized companies (Munich); 'Personio raised $40M in Series B investment led by Index Ventures' (the firm's post, 2019-01-17), Martin Mignot on the board; $8.5B at the June 2022 Series E extension (aligned to Accel's cited mark; the unicorn list's $6.3B is the October 2021 round), stale",
    rounds=[rnd("2019-01-17", "Series B", 40000000, "Index Ventures", True, u, "firm")]))
u = post("our-investment-in-phaidra")
L.append(C("phaidra", status="private", country="US", city="Seattle", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-07", rng="below_1b",
    focus="AI & Applied AI", note="AI control agents for data-centre cooling and industrial plants (Seattle; founded by former DeepMind engineers); Index led the $12M Series A ('Compute is king: Our investment in Phaidra', the firm's post, 2024-07-02; the post does not print the round word, the press named it); $50M Series B in October 2025",
    rounds=[rnd("2024-07-02", "Series A", 12000000, "Index Ventures", True, u, "firm")]))
u = nqurl('"Piñata Farms" Index Ventures', "meme-maker Piñata Farms landed a $100 million valuation")
L.append(C("pi-ata-farms", status="private", country="US", city="Los Angeles", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2021-07", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Meme and AI video creation app (Los Angeles); 'landed a $100 million valuation in a deal led by Index' months after launch, its Series A (Business Insider, 2021-07-23); still shipping products in August 2025 (PR Newswire)",
    rounds=[rnd("2021-07-23", "Series A", None, "Index Ventures", True, u, "press")]))
L.append(C("pilot", status="private", city="San Francisco", rng="1b_plus", **sv("pilot", "sequoia-capital"), focus="SaaS", flags=["stale"],
    note="Bookkeeping, tax and CFO services for startups (San Francisco); the $15M Series A of March 2018 led by Index (FinTech Global, 2018-03-16) and the $40M Series B it led in April 2019 (the firm's post), Mark Goldberg on the board; $1.2B at the March 2021 Series C (aligned to Sequoia's cited mark), stale"))
u = post("pitch-raises-19m")
L.append(C("pitch", status="private", country="DE", city="Berlin", stage="Series A", **WV, stage_cite=u, entry_date="2018-10", rng="below_1b", focus="SaaS",
    note="Collaborative presentation software (Berlin; founded by the Wunderlist team); 'a $19 million Series A funding round led by Index Ventures and its existing investor BlueYard' (the firm's post, 2018-10-09), Neil Rimer on the board; $85M at $600M in May 2021; restructured in 2024",
    rounds=[rnd("2018-10-09", "Series A", 19000000, "Index Ventures, BlueYard", True, u, "firm")]))
u = post("hidden-power-of-plaid")
L.append(C("plaid", dispute=("usd", "rng"), city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2018-12", **sv("plaid", "coatue"), rng="1b_plus", focus="Fintech & Payments",
    note="Bank-account connectivity APIs (San Francisco); 'we're delighted to be co-leading their $250 million Series C' (the firm's post, 2018-12-11), with Kleiner Perkins; $13.4B in April 2021, $6.1B at the April 2025 round and $8B in the February 2026 share sale (aligned to Coatue's cited mark, the freshest priced event)",
    rounds=[rnd("2018-12-11", "Series C", 250000000, "Index Ventures, Kleiner Perkins", True, u, "firm")]))
u = post("plain-raises-6m"); g = post("plain-raises-15m-series-a")
L.append(C("plain", dispute=("country",), status="private", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2022-11", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="SaaS",
    note="API-first customer support platform for B2B software companies (London; founded by former Deliveroo staff); the $6M seed 'co-led by Index Ventures and Connect Ventures' (the firm's post, 2022-11-09), then 'Plain Raises $15M Series A' (the firm's post, 2025-02-06); the pre-filled NL is a one-word name join",
    rounds=[rnd("2022-11-09", "Seed", 6000000, "Index Ventures, Connect Ventures", True, u, "firm"), rnd("2025-02-06", "Series A", 15000000, None, True, g, "firm")]))
u = post("pointfive-raises-16m"); g = post("pointfive-secures-20m")
L.append(C("pointfive", status="private", country="IL", city="Tel Aviv", stage="Seed", **WV, stage_cite=u, entry_date="2024-06", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="SaaS",
    note="Cloud cost optimisation platform (Tel Aviv); 'PointFive Raises $16M in Seed Funding' led by Index (the firm's post, 2024-06-19), then the $20M Series A 'led by Salesforce Ventures, with participation from all existing investors, including Index Ventures' (2024-11-12); $60M in 2026",
    rounds=[rnd("2024-06-19", "Seed", 16000000, "Index Ventures", True, u, "firm"), rnd("2024-11-12", "Series A", 20000000, "Salesforce Ventures", True, g, "firm")]))
g = news("Pomelo", "secures $55m Series C")
L.append(C("pomelo", status="private", country="AR", city="Buenos Aires", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021-05", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="Fintech & Payments", flags=["stage_uncited"],
    note="Card-issuing and payments infrastructure for Latin America (Buenos Aires); Index joined the $9M seed of May 2021 (Mark Fiorentino, then Carlos Gonzalez-Cadenas the partner), a $35M Series A led by Tiger Global followed that October, and a $55M Series C in January 2026 (FinTech Futures)",
    rounds=[rnd("2021-05", "Seed", 9000000, None, True, None, "press"), rnd("2026-01-23", "Series C", 55000000, "Kaszek, Insight Partners", None, g, "press")]))
u = nqurl('"Printify" Series A Index Ventures $45', "Printify Raises $45M in Series A")
L.append(C("printify", dispute=("stage", "country"), status="acquired", country="LV", city="Riga", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2021-09",
    focus="SaaS", note="Print-on-demand platform for online merchants (Riga; a Delaware parent files the Form Ds, Dino Becirovic as director); 'Printify Raises $45M in Series A Funding', led by Index (ArcticStartup, 2021-09-09); merged with Printful in November 2024 (the firm's post), the successor trading under both brands",
    rounds=[rnd("2021-09-09", "Series A", 45000000, "Index Ventures", True, u, "press")]))
u = post("prodigy-finance-raises-240m")
L.append(C("prodigy-finance", status="private", country="GB", city="London", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2017-08", rng="below_1b",
    focus="Fintech & Payments", note="Loans for international postgraduate students (London); Index led the $40M equity round inside the $240M financing of August 2017 (the firm's post), Neil Rimer on the board; Balderton had led the earlier round",
    rounds=[rnd("2017-08-21", "Series C", 40000000, "Index Ventures", True, u, "firm")]))
u = news("Productboard", "Raises $1.3M in Seed"); g = post("productboard-raises-8-million")
L.append(C("productboard", city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2016-10",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="SaaS",
    note="Product management software (San Francisco; founded in Prague); Index led the $1.3M seed of October 2016 (FinSMEs), which its list marks; '$8 million in Series A financing led by Kleiner Perkins' with Index participating (the firm's post, 2018-07-12); $1.725B at the 2022 Series D",
    rounds=[rnd("2016-10-19", "Seed", 1300000, "Index Ventures", True, u, "press"), rnd("2018-07-12", "Series A", 8000000, "Kleiner Perkins", True, g, "firm")]))
L.append(C("pure-storage", dispute=("usd",), city="Santa Clara", **sv("pure-storage", "ivp"), rng="10b_plus", focus="Data Infrastructure",
    note="All-flash enterprise storage (Santa Clara; NYSE: PSTG, IPO October 2015); Index led the $40M Series D of August 2012 (the firm's own news item), Mike Volpi on the board until 2023; market cap aligned to IVP's cited figure, the pre-filled float is stale"))
L.append(C("qapa", status="acquired", country="FR", city="Paris", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2016-12", rng="below_1b", focus="Consumer & Marketplaces",
    note="Digital temp-staffing marketplace (Paris); Index led the EUR 11M Series B of December 2016 with Partech, Dominique Vidal on the board; acq. by Adecco, 2021 (the firm's list tags it Adecco)"))
L.append(C("quantive", status="acquired", city="Denver", rng="below_1b", focus="SaaS",
    note="OKR and strategy-execution software, founded as Gtmhub in Sofia (Denver); 'Gtmhub Raises $120 Million Series C' led by Index (the firm's post, 2021-12-16), Martin Mignot on the board; acq. by WorkBoard, 2025"))
L.append(C("quill", status="acquired", city="San Francisco", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2020", rng="below_1b", focus="SaaS",
    note="Team messaging app (San Francisco); Index led the $12.5M Series A, Sarah Cannon on the board (the firm's 2020 page); acq. by Twitter, 2021 (the firm's list tags it Twitter)"))
L.append(C("raisin", status="private", country="DE", city="Berlin", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015", rng="below_1b", focus="Fintech & Payments",
    note="Deposit and savings marketplace, WeltSparen in Germany (Berlin); Index led the EUR 20M Series B of 2015, Neil Rimer on the board; the EUR 30M Series C of January 2017 was led by Thrive 'with participation of Raisin's existing investors ... Ribbit Capital and Index Ventures' (the firm's post); merged with Deposit Solutions in 2021; Ribbit's row reads below $1B"))
u = post("our-investment-in-readyset")
L.append(C("readyset", status="private", country="US", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2022-04", rng="below_1b", focus="Data Infrastructure",
    note="SQL caching engine for Postgres and MySQL (San Francisco; an MIT spin-out); 'leading ReadySets Series A' (the firm's post, 2022-04-05; $24M)",
    rounds=[rnd("2022-04-05", "Series A", 24000000, "Index Ventures", True, u, "firm")]))
L.append(C("rebtel", status="private", country="SE", city="Stockholm", stage="Series A", stage_src="model", stage_conf="high", entry_date="2006", rng="below_1b", focus="Consumer & Marketplaces",
    note="International calling and mobile top-up service (Stockholm); Index and Benchmark Europe led the $20M Series A of 2006, Ben Holmes on the board (the firm's lists from 2007)"))
u = post("a-place-to-create-memories"); ur = news("Rec Room", "Rec Room shutting down: Once valued")
L.append(C("rec-room", dispute=("status", "rng", "usd"), status="defunct", city="Seattle", stage="Growth", **WV, stage_cite=u, entry_date="2019-06", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social gaming platform, founded as Against Gravity (Seattle); 'our Series B investment in the company' (the firm's post, 2019-06-12; $24M with Sequoia), Damir Becirovic; $3.5B at the December 2021 round; the company shut the platform down in 2026 (tech-insider, 2026-06-23; Coatue's row reads defunct), so the pre-filled 2021 mark no longer stands",
    rounds=[rnd("2019-06-12", "Series B", 24000000, "Index Ventures, Sequoia", True, u, "firm")], extra={"status_citation": ur}))
L.append(C("redwood-systems", status="acquired", city="Fremont", rng="below_1b", focus="Industrial & Robotics",
    note="Networked LED lighting and building sensors (Fremont); Index joined from the 2009-10 Series A, Neil Rimer on the board (Form Ds 2010-2012); acq. by CommScope, 2013"))
u = post("location-location-whatever")
L.append(C("remote", dispute=("country", "usd"), country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2020-04", grad="graduated", grad_src="first_party", grad_cite=u,
    **sv("remote", "accel"), rng="1b_plus", focus="SaaS", flags=["stale"],
    note="Global employment and payroll platform (remote-first, registered in San Francisco); 'Index led the latest $35m round of funding ... which follows Index's Seed investment a year prior' (the firm's post, 2020-11-10; Tech.eu names the $35M round a Series A); $3B at the April 2022 Series C (aligned to Accel's cited mark; the unicorn list's $1.5B is the 2021 Series B), stale; the pre-filled country is a broken Wikidata string",
    rounds=[rnd("2020-04", "Seed", 11000000, "Index Ventures", True, u, "firm"), rnd("2020-11-10", "Series A", 35000000, "Index Ventures", True, u, "firm")]))
g = post("resistant-ai-announces-16-6m")
L.append(C("resistant-ai", dispute=("stage", "country"), status="private", country="CZ", city="Prague", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021-01",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="Security", flags=["stage_uncited"],
    note="AI defences against document forgery and financial fraud (Prague; a Delaware parent files the Form D); Index led the $2.75M seed of January 2021, which its list marks, then joined the $16.6M Series A led by GV that October (the firm's post; the Form D of June 2021 carrying Jan Hammer is that round, which the band read as the entry); $25M Series B in October 2025",
    rounds=[rnd("2021-01", "Seed", 2750000, "Index Ventures", True, None, "press"), rnd("2021-10-20", "Series A", 16600000, "GV", True, g, "firm")]))
u = post("announcing-our-15m-series-a-in-revenuecat")
L.append(C("revenuecat", status="private", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2020-08", rng="below_1b", focus="DevTools & APIs",
    note="In-app subscription infrastructure for mobile apps (San Francisco); 'we're leading RevenueCat's $15M Series A' (the firm's post by Mark Fiorentino, 2020-08-11); $50M Series C in June 2025",
    rounds=[rnd("2020-08-11", "Series A", 15000000, "Index Ventures", True, u, "firm")]))
u = post("revolut-raises-up-to-further")
L.append(C("revolut", dispute=("country", "usd", "rng"), country="GB", city="London", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2016-07",
    **sv("revolut", "a16z"), rng="100b_plus", focus="Fintech & Payments",
    note="Global financial app (London); Index entered in the Series A of July 2016 led by Balderton (the firm's post of 2016-07-11 lists 'Revolut's institutional investors (including Balderton Capital, Ribbit Capital, Index Ventures, Point Nine ...)') and led the $66M Series B of July 2017 ('The investment round was led by Index Ventures'), Martin Mignot on the board; $115B in July 2026 (aligned to a16z's cited mark). The firm's list marks it 'backed at Seed'; the record names the entry a Series A (D8 score)",
    rounds=[rnd("2016-07-11", "Series A", None, "Balderton", True, u, "firm"), rnd("2017-07-12", "Series B", 66000000, "Index Ventures", True, post("global-banking-alternative-revolut"), "firm")]))
u = post("from-seed-to-a")
L.append(C("robinhood", dispute=("stage", "usd", "rng"), city="Menlo Park", stage="Seed", **WV, stage_cite=u, entry_date="2013-12", grad="graduated", grad_src="first_party", grad_cite=u,
    **sv("robinhood", "a16z"), rng="100b_plus", focus="Fintech & Payments",
    note="Commission-free brokerage (Menlo Park; Nasdaq: HOOD, IPO July 2021); 'as Robinhood announces its Series A, where we had strong enough conviction to double-down on our seed investment to lead the $13M round' (the firm's post by Jan Hammer, 2014-09-23; the $3M seed of December 2013); the band read the 2019 filing; market cap aligned to a16z's cited figure",
    rounds=[rnd("2013-12-18", "Seed", 3000000, "Index Ventures", True, post("mobile-focused-commission-free"), "firm"), rnd("2014-09-23", "Series A", 13000000, "Index Ventures", True, u, "firm")]))
u = post("generation-of-creators")
L.append(C("roblox", dispute=("usd",), country="US", city="San Mateo", stage="Growth", **WV, stage_cite=u, entry_date="2017-03", **sv("roblox", "a16z"), rng="10b_plus",
    focus="Media, Gaming & Advertising", note="User-generated games platform (San Mateo; NYSE: RBLX, direct listing March 2021); 'we have co-led a $92m investment in Roblox' with Meritech, 'the first equity financing in over five years' (the firm's posts, 2017-03-14), Neil Rimer on the board; market cap aligned to a16z's cited figure",
    rounds=[rnd("2017-03-14", "Growth round", 92000000, "Meritech, Index Ventures", True, u, "firm")]))
u = post("rohlik-raises-190-million")
L.append(C("rohlik", country="CZ", country_src="wikidata", city="Prague", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2021-03", focus="Consumer & Marketplaces",
    flags=["stale"], note="Online grocery delivery in central Europe (Prague); Index entered in the EUR 190M Series C of March 2021 led by Partech (the firm's post), Jan Hammer and Sofia Dolfe; the EUR 100M round of July 2021 valued it at EUR 1B ($1.2B), the last priced mark, stale beyond 24 months",
    rounds=[rnd("2021-03-02", "Series C", None, "Partech", True, u, "firm")]))
gl.write("batch-005", L)
