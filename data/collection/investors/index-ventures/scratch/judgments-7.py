"""PRO-82 grind, batch-007 (taxfix .. algorx). Same evidence and conventions as batch-001. 7tm, acutus-medical, addex,
algorx and versartis are life sciences desk rows (judgments-life.py)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

u = post("taxfix-the-automated-tax-accountant")
L.append(C("taxfix", country="DE", country_src="wikidata", city="Berlin", stage="Growth", **WV, stage_cite=u, entry_date="2020-04", focus="Fintech & Payments", flags=["stale"],
    note="Mobile tax-return app (Berlin); 'raised a $65 million Series C round' led by Index (the firm's post, 2020-04-16), Neil Rimer on the board; $1B at the April 2022 Series D, stale beyond 24 months",
    rounds=[rnd("2020-04-16", "Series C", 65000000, "Index Ventures", True, u, "firm")]))
L.append(C("teatime-games", status="defunct", city="Reykjavik", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social mobile games with live video (Reykjavik; founded by the QuizUp team); Index led the $7.5M Series A of 2018, Guzman Diaz as director (Form D 2018-Q2; Tech.eu 2018-05-16); closed in 2022, as Atomico's row records"))
u = post("why-were-backing-tebi")
L.append(C("tebi", status="private", country="NL", city="Amsterdam", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-10", rng="below_1b",
    focus="Fintech & Payments", note="Point-of-sale and payments system for restaurants and shops, from Adyen's co-founder Arnout Schuijf (Amsterdam); Index led the EUR 20M round of October 2024, the Series A ('Simplicity with purpose: why we're backing Tebi', the firm's post by Jan Hammer); EUR 30M led by CapitalG in June 2025",
    rounds=[rnd("2024-10-15", "Series A", None, "Index Ventures", True, u, "firm")]))
v = nqurl('"Tekion" valuation $4 billion Dragoneer', "Tekion Corp raises $200 million in funding at valuation of over $4 billion")
L.append(C("tekion", dispute=("usd",), city="Pleasanton", stage="Growth", stage_src="model", stage_conf="high", entry_date="2019-10", usd=4000000000, val_src="web_verified", val_cite=v,
    asof="2024-07-16", rng="1b_plus", focus="SaaS", flags=["cite_pending"],
    note="Cloud dealer-management platform for automotive retail (Pleasanton, California); Index led the $65M Series B of October 2019, Mike Volpi on the board; $1B+ at Advent's Series C in 2020, 'over $4 billion' at Dragoneer's $200M investment of July 2024 (Economic Times)",
    rounds=[rnd("2019-10", "Series B", 65000000, "Index Ventures", True, None, "press")]))
u = post("tema-expands-access")
L.append(C("tema", status="private", country="US", city="New York", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2023-05", rng="below_1b",
    focus="Fintech & Payments", note="Issuer of actively managed thematic ETFs (New York); 'the biggest venture funding round in the ETF space to date, co-led by Index Ventures and Accel' at launch (the firm's post, 2023-05-10), the seed round in Accel's row",
    rounds=[rnd("2023-05-10", "Seed", None, "Index Ventures, Accel", True, u, "firm")]))
u = post("our-investment-in-temporal"); v = news("Temporal", "Temporal Raises $550M in Series E")
L.append(C("temporal", status="private", country="US", city="Seattle", stage="Growth", **WV, stage_cite=u, entry_date="2022-02", rng="10b_plus", usd=12550000000, val_src="web_verified",
    val_cite=v, asof="2026-09-23", focus="DevTools & APIs",
    note="Durable execution platform for distributed applications (Seattle; born at Uber as Cadence); Index led the $103M Series B at $1.5B ('Everything is a Workflow: Our Investment in Temporal', the firm's post, 2022-02-16), Mike Volpi then Sahir Azam; $12.55B at the $550M Series E of September 2026 (425 Business); the a16z, Lightspeed and Sequoia rows still carry the $5B mark of February 2026",
    rounds=[rnd("2022-02-16", "Series B", 103000000, "Index Ventures", True, u, "firm")]))
u = post("when-everyone-speaks-software")
L.append(C("tessl-io", dispute=("stage",), status="private", city="London", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-11",
    focus="AI & Applied AI", note="AI-native software development platform from Snyk's founder Guy Podjarny (London); Index led the $100M Series A of November 2024 at about $750M (the firm's post, 2024-11-14; Form D first sale 2024-11-04 with Carlos Gonzalez-Cadenas as director) after a $25M seed led by GV and boldstart; the band read the size",
    rounds=[rnd("2024-04", "Seed", 25000000, "GV, boldstart", False, None, "filing"), rnd("2024-11-14", "Series A", 100000000, "Index Ventures", True, u, "firm")]))
u = narch("Business of Fashion Announces $2.1m")
L.append(C("the-business-of-fashion", status="private", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2013-02", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Trade publication for the fashion industry (London); 'The Business of Fashion Announces $2.1m, in seed funding' led by Index (the firm's own news item, 2013-02-18), Robin Klein on the board",
    rounds=[rnd("2013-02-18", "Seed", 2100000, "Index Ventures", True, u, "firm")]))
L.append(C("the-climate-corporation", dispute=("stage",), city="San Francisco", rng="below_1b", stage="Series A", stage_src="model", stage_conf="high", entry_date="2007-10",
    focus="Climate & Energy", note="Weather insurance and climate analytics for farmers, founded as WeatherBill (San Francisco); Index and NEA led the $12.6M Series A of October 2007 (the firm's late-2007 list carries Weatherbill), Neil Rimer on the board; the band read the 2011 filing; acq. by Monsanto, 2013 (about $930M; the firm's own news item)",
    rounds=[rnd("2007-10", "Series A", 12600000, "NEA, Index Ventures", True, None, "press")]))
L.append(C("tiney", status="private", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Childminder agency and training platform (London); the firm's list marks it backed at Seed, Hannah Seal; an EUR 8.3M Series A in May 2024 (EU-Startups)"))
u = post("tofu-raises-5m-seed")
L.append(C("tofu", status="private", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2023-10", rng="below_1b", focus="AI & Applied AI",
    note="AI content personalisation for B2B marketing (San Francisco); 'Tofu raises $5M Seed Round' led by Index (the firm's post, 2023-10-19); $12M in April 2026",
    rounds=[rnd("2023-10-19", "Seed", 5000000, "Index Ventures", True, u, "firm")]))
u = post("privacy-will-define")
L.append(C("transcend", dispute=("stage",), status="private", city="San Francisco", rng="below_1b", stage="Series A", **WV, stage_cite=u, entry_date="2020-06", focus="Security",
    note="Data privacy and governance infrastructure (San Francisco); 'we're leading Transcend's $25 million Series A, alongside our friends at Accel' (the firm's post by Mark Goldberg, 2020-06-10); the band read the $40M Series B filing of 2024, the first to carry an Index director",
    rounds=[rnd("2020-06-10", "Series A", 25000000, "Index Ventures", True, u, "firm")]))
u = narch("Trustpilot raises €10 million")
L.append(C("trustpilot", status="public", country="DK", country_src="wikidata", city="Copenhagen", stage="Growth", **WV, stage_cite=u, entry_date="2012-12", rng="1b_plus",
    **sv("trustpilot", "northzone"), focus="Consumer & Marketplaces",
    note="Online review platform (Copenhagen; LSE: TRST, IPO March 2021); 'Trustpilot raises EUR 10 million in a round led by Index Ventures' (the firm's own news item, 2012-12-12), the Series B after Northzone's Series A, Ben Holmes on the board; market cap aligned to Northzone's cited figure",
    rounds=[rnd("2012-12-12", "Series B", None, "Index Ventures", True, u, "firm")]))
L.append(C("tweetup", status="acquired", city="Pasadena", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Twitter search and promotion marketplace from Idealab (Pasadena); $3.5M in April 2010 from Index and others, Danny Rimer on the board (Form D; the firm's own news item of 2010-04-12); renamed PostUp, then UberMedia, the name the firm's 2012 list carries (one company: merged at the rebuild); UberMedia was acq. by Near, 2021"))
L.append(C("twelve-labs", status="private", city="San Francisco", rng="below_1b", focus="AI & Applied AI", flags=["needs_web_value"],
    note="Video-understanding foundation models (San Francisco and Seoul); Index led the $5M seed of March 2022 ('Unlocking the Power of Video with Twelve Labs', the firm's post; its list marks the company backed at Seed); $50M Series A in June 2024, $100M Series B in July 2026 whose valuation is checked in the A/B pass"))
u = news("Typeform", "lands $15M to revolutionize forms")
L.append(C("typeform", status="private", country="ES", city="Barcelona", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2015-09", rng="below_1b",
    focus="SaaS", note="Conversational forms and surveys (Barcelona); Index led the $15M Series A of September 2015 (VentureBeat, 2015-09-17), Neil Rimer on the board; General Atlantic led the $35M Series B of 2017 and Sofina the $135M Series C of 2022 at $935M; Point Nine's row reads acquired, which no source read here confirms",
    rounds=[rnd("2015-09-17", "Series A", 15000000, "Index Ventures", True, u, "press")]))
L.append(C("ubiquity6", status="acquired", city="San Francisco", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Shared augmented-reality platform (San Francisco); 'Ubiquity6 Announced 10.5M in Funding, Led by Index Ventures' (the Series A; the firm's own item, 2018-04-03), then $27M with Benchmark, Mike Volpi on the board; acq. by Discord, 2021"))
u = news("Upollo", "Raise a $2.75 Million Seed Round")
L.append(C("upollo", status="private", country="AU", city="Sydney", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2022-11", rng="below_1b", focus="SaaS",
    note="Detection of repeat trials and account sharing for subscription products (Sydney); the $2.75M seed of November 2022 (Business Insider) with Index, Mike Volpi the partner on the firm's page",
    rounds=[rnd("2022-11-29", "Seed", 2750000, None, True, u, "press")]))
L.append(C("vetted", status="unknown", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="AI product-research and shopping assistant, earlier listed as Lustre (San Francisco); on the firm's 2022 list, Damir Becirovic; $14M in August 2022 led by Insight (TechCrunch); the round Index entered is not named on any surface read, and nothing dated after 2024 was found: last known state not established (Insight's row reads the same)", rounds=[]))
L.append(C("viagogo", dispute=("stage",), status="public", city="New York", rng="1b_plus", **sv("viagogo", "atomico"), stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006",
    focus="Consumer & Marketplaces", flags=["cite_pending"],
    note="Ticket resale marketplace (founded in London in 2006, later Geneva; bought StubHub in 2020 and listed as StubHub Holdings, NYSE: STUB, in September 2025); Index led the 2006 Series A, Danny Rimer on the board (Form Ds 2009-2011 of the Delaware parent Pugnacious Endeavors; the band read the $35M round of 2009); market cap aligned to Atomico's cited figure"))
uv = news("Vouch", "Hiscox to acquire MGA and carrier operations from Vouch")
L.append(C("vouch", status="acquired", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2019", rng="below_1b", focus="Fintech & Payments",
    note="Business insurance for startups (San Francisco); Index co-led the $24.5M Series A of 2019 with Ribbit, Mark Goldberg; Y Combinator Continuity led the Series B; 'Hiscox to acquire MGA and carrier operations from Vouch' (Coverager, 2025-08-05): the business sold as a going concern (COLLECTION.md s6); the First Round and YC rows read defunct and Ribbit's private",
    extra={"status_citation": uv}))
L.append(C("wealthfront", dispute=("usd", "rng"), city="Palo Alto", **sv("wealthfront", "ribbit-capital"), rng="1b_plus", focus="Fintech & Payments",
    note="Automated investing and cash accounts (Palo Alto; Nasdaq: WLTH, IPO December 2025); Index led the $20M round of March 2013 with Ribbit (the firm's own news item) and the $35M round of April 2014, Mike Volpi on the board; the funds filed a 13G after the IPO; market cap aligned to Ribbit's cited figure"))
L.append(C("wetravel", status="private", country="NL", city="Amsterdam", rng="below_1b", focus="SaaS",
    note="Booking and payments platform for multi-day travel operators (Amsterdam and San Francisco); the firm's list marks it backed at Seed; $27M Series B in March 2025 and $92M in September 2025 (FinTech Futures; Tech Funding News)"))
L.append(C("wise", status="public", country="GB", country_src="wikidata", city="London", rng="10b_plus", **sv("wise", "ivp"), focus="Fintech & Payments",
    note="International money transfers and multi-currency accounts, formerly TransferWise (London; LSE: WISE, direct listing July 2021); Index backed the $1.3M seed of 2012, which its list marks, and joined the '$6 million investment round' of May 2013 led by Valar (the firm's own news item); market cap aligned to IVP's cited figure"))
u = post("wiz-the-security-company")
L.append(C("wiz", status="acquired", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2020-12", rng="below_1b", focus="Security",
    note="Cloud security platform (New York; engineering in Tel Aviv); Index co-led the $100M Series A at launch with Sequoia and Insight ('Wiz: The Security Company that Delivers on its Promise', the firm's post by Shardul Shah, 2020-12-09) and every round after; acq. by Google, announced March 2025 ($32B), closed 2026 (the a16z, Greylock and Insight rows)",
    rounds=[rnd("2020-12-09", "Series A", 100000000, "Index Ventures, Sequoia, Insight Partners", True, u, "firm")]))
u = post("wonderful-raises-34m"); g = post("wonderful-secures-100m")
L.append(C("wonderful", dispute=("country",), country="NL", city="Amsterdam", stage="Seed", **WV, stage_cite=u, entry_date="2025-07", grad="graduated", grad_src="first_party", grad_cite=g,
    focus="AI & Applied AI", note="Enterprise AI agents for customer-facing operations (Amsterdam; Israeli founders); Index led the $34M seed (the firm's post, 2025-07-02) and the $100M Series A four months later ('The Series A was driven by fast growth', 2025-11-11); $5B at the $550M Series C of September 2026; the pre-filled country is a broken Wikidata string",
    rounds=[rnd("2025-07-02", "Seed", 34000000, "Index Ventures", True, u, "firm"), rnd("2025-11-11", "Series A", 100000000, "Index Ventures", True, g, "firm")]))
u = post("wordsmith-raises-5-million"); g = post("wordsmith-ai-raises-25m")
L.append(C("wordsmith-ai", status="private", country="GB", city="Edinburgh", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-06", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="AI & Applied AI",
    note="AI workspace for in-house legal teams (Edinburgh); Index led the $5M seed (the firm's post, 2024-06-20) and the '$25m series A' a year later (2025-06-03; Business Wire: 'from Index Ventures'); a Series B in 2026",
    rounds=[rnd("2024-06-20", "Seed", 5000000, "Index Ventures", True, u, "firm"), rnd("2025-06-03", "Series A", 25000000, "Index Ventures", True, g, "firm")]))
u = post("workbounce-raises-2-7-million")
L.append(C("workbounce", status="private", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2022-03", rng="below_1b", focus="SaaS",
    note="Search and collaboration tool for B2B sales teams (London); 'Workbounce raises $2.7 million from Index Ventures' (the firm's post and TechCrunch, 2022-03-09), a seed round the firm's list marks, Hannah Seal",
    rounds=[rnd("2022-03-09", "Seed", 2700000, "Index Ventures", True, u, "firm")]))
u = news("Worldover", "Index Ventures leads £3M seed round")
L.append(C("worldover", status="private", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2023-09", rng="below_1b", focus="SaaS",
    note="Regulatory compliance automation for cosmetics and consumer products (London); 'Index Ventures leads GBP 3M seed round' (Tech.eu and the firm's post, 2023-09-05)",
    rounds=[rnd("2023-09-05", "Seed", None, "Index Ventures", True, u, "press")]))
u = post("doubling-down-on-data")
L.append(C("xata", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2021-09", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="Data Infrastructure",
    note="Serverless Postgres database platform (remote-first, registered in San Francisco); 'We invested in Xata's seed round last summer and are so proud to double down and co-lead their Series A, alongside our good friends at Redpoint' (the firm's post, 2022-03-08; the $5M seed post of 2021-09-20)",
    rounds=[rnd("2021-09-20", "Seed", 5000000, "Index Ventures", True, post("xata-raises-5m"), "firm"), rnd("2022-03-08", "Series A", 30000000, "Index Ventures, Redpoint", True, u, "firm")]))
L.append(C("zuora", city="Redwood City", rng="below_1b", focus="SaaS",
    note="Subscription billing and revenue software (Redwood City; NYSE: ZUO, IPO April 2018); Index led the $36M Series D of 2011, Mike Volpi on the board (Form Ds 2013-2015; the firm's post on the IPO); acq. by Silver Lake and GIC, 2025"))
L.append(C("8tracks", status="defunct", country="US", city="San Francisco", stage="Seed", stage_src="model", stage_conf="low", entry_date="2012-01", rng="below_1b", focus="Media, Gaming & Advertising",
    flags=["stage_uncited"], note="Playlist-based internet radio (San Francisco); the $1.3M seed of January 2012 with Index and Andreessen Horowitz; a Regulation A crowdfunding in 2016 and no venture round after the seed; shut down at the end of 2019 (Digital Music News)"))
L.append(C("abe-s-market", status="acquired", country="US", city="Chicago", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online marketplace for natural products (Chicago; Israeli founders); on the firm's 2010-2015 lists under its Seed stage filter, Saul Klein the partner; acq. by Direct Eats, 2016"))
L.append(C("adallom", city="Palo Alto", stage="Growth", stage_src="model", stage_conf="high", entry_date="2013-12", rng="below_1b", focus="Security",
    note="Cloud access security for SaaS applications (Palo Alto; founded in Tel Aviv); Index led the $15M Series B of December 2013 after Sequoia's Series A, Shardul Shah on the board; acq. by Microsoft, 2015 ($320M)"))
L.append(C("adconion", status="acquired", country="US", city="Santa Monica", stage="Growth", stage_src="model", stage_conf="high", entry_date="2008-02", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Online audience and video advertising network (founded in Munich, run from Santa Monica); Index Growth led the $80M Series C of February 2008, Dominique Vidal and Giuseppe Zocco on the board; the business was sold in parts, the direct unit to Amobee (Singtel) in 2014"))
L.append(C("admarvel", country="US", city="San Mateo", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile ad mediation platform (San Mateo; founded 2006); on the firm's 2010-2013 lists under its Early stage filter; no source read names the round Index entered; acq. by Opera Software, 2010", rounds=[]))
u = post("albert-invent")
L.append(C("albert", dispute=("status", "country"), status="private", country="US", city="Oakland", stage="Seed", **WV, stage_cite=u, entry_date="2023-06", rng="below_1b", focus="SaaS",
    note="R&D data platform for chemistry and materials science (Albert Invent, Oakland); 'it has raised $7.5M in seed funding' led by Index (the firm's post, 2023-06-07); a Series A led by Coatue followed; the pre-filled 'defunct' and BE are a one-word Wikidata join",
    rounds=[rnd("2023-06-07", "Seed", 7500000, "Index Ventures", True, u, "firm")]))
L.append(C("alertme", status="acquired", country="GB", country_src="wikidata", city="Cambridge", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Smart-home energy monitoring and security platform (Cambridge, UK; founded 2006); on the firm's lists from 2009 under its Early stage filter, Saul Klein the partner; the round Index entered is not named on any surface read; acq. by British Gas (Centrica), 2015 (GBP 65M)", rounds=[]))
L.append(C("algolia", dispute=("country",), country="US", city="San Francisco", stage="Seed", stage_src="model", stage_conf="low", entry_date="2013-09", focus="DevTools & APIs",
    flags=["stage_uncited"], note="Hosted search API (founded in Paris, run from San Francisco); Index joined the $1.2M seed of September 2013 with Alven and Point Nine (on the firm's list from 2014, Martin Mignot); Accel led the 2015 Series A; $2.25B at the July 2021 Series D; the pre-filled country is a broken Wikidata string"))
gl.write("batch-007", L)
