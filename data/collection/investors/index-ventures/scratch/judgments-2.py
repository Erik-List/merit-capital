"""PRO-82 grind, batch-002 (boulevard .. deepnote). Same evidence and conventions as batch-001."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("boulevard", status="private", city="Los Angeles", stage="Series A", stage_src="model", stage_conf="high", entry_date="2019-11", rng="below_1b", focus="SaaS",
    note="Booking and business software for salons and spas (Los Angeles); Index led the $11M Series A at launch in November 2019 (PR Web, 2019-11-04), then the $27M Series B ('our growing conviction', the firm's post 2020-11-23) and joined the $80M Series D of July 2025",
    rounds=[rnd("2019-11-04", "Series A", 11000000, "Index Ventures", True, nqurl('"Boulevard" Series A Index Ventures salon', "Boulevard Launches With $11M Series A"), "press")]))
L.append(C("brightback", status="acquired", city="San Francisco", rng="below_1b", focus="SaaS",
    note="Customer retention software for subscription businesses (San Francisco); launched with $11M in April 2019, Index leading the Series A (Shardul Shah on the 2018 Form D); acq. by Chargebee, 2021"))
u = post("brightgo-raises-3m")
L.append(C("brightgo", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2023-11", rng="below_1b", focus="SaaS",
    note="Workforce software for commercial cleaning companies; 'we're excited to announce our seed investment in BrightGo' (the firm's post, 2023-11-13; $3M)",
    rounds=[rnd("2023-11-13", "Seed", 3000000, "Index Ventures", True, u, "firm")]))
uz = nqurl('"BrightHire" Zoom', "Zoom acquires BrightHire, adding")
L.append(C("brighthire", status="acquired", country="US", city="New York", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2021-10", rng="below_1b", focus="SaaS",
    note="Interview intelligence platform (New York); Index led the $12.5M Series A announced October 2021 (total $20.5M), Shardul Shah; acq. by Zoom, 2025 (Zoom's release, 2025-11-13)", extra={"status_citation": uz}))
u = post("brincs-blake-resnick")
L.append(C("brinc", status="private", country="US", city="Seattle", stage="Series A", **WV, stage_cite=u, entry_date="2021-10", rng="below_1b", focus="Industrial & Robotics",
    flags=["needs_web_value"], note="Public-safety drones (Seattle); 'Index Ventures, who led the Series A' ($25M, October 2021; the firm's post of 2023-08-15); a $75M round in April 2025 and $125M from Motorola Solutions and Index in July 2026: the valuation of the 2026 round is checked in the A/B pass",
    rounds=[rnd("2021-10-12", "Series A", 25000000, "Index Ventures", True, u, "firm")]))
L.append(C("built", status="private", city="Nashville", rng="1b_plus", **sv("built", "tcv"), focus="Fintech & Payments", flags=["stale"],
    note="Construction lending software (Nashville); Index led the $21M Series A of November 2017 (the firm's post), Mark Goldberg on the board; $125M Series D at $1.5B in September 2021 led by TCV (aligned to TCV's cited mark), stale beyond 24 months"))
u = post("capitolis-secures-29")
L.append(C("capitolis", status="private", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2018-03", rng="1b_plus", **sv("capitolis", "a16z"),
    focus="Fintech & Payments", flags=["stale"],
    note="Capital-markets optimisation platform (New York; founded 2017); 'secures $29 million financing from Index Ventures and Sequoia Capital' (the firm's post, 2018-03-06), the seed and Series A announced together; $110M Series D at $1.6B in March 2022 (aligned to a16z's cited mark), stale",
    rounds=[rnd("2018-03-06", "Series A", 29000000, "Index Ventures, Sequoia", True, u, "firm")]))
u = post("cargo-one-the-world")
L.append(C("cargo-one", status="private", country="DE", city="Berlin", stage="Series A", **WV, stage_cite=u, entry_date="2020-07", rng="below_1b", focus="Consumer & Marketplaces",
    note="Booking platform for air cargo (Berlin); Index led the $18.6M Series A (the firm's post, 2020-07-27), Martin Mignot; $42M Series B in December 2020 led by Bessemer",
    rounds=[rnd("2020-07-27", "Series A", 18600000, "Index Ventures", True, u, "firm")]))
u = post("castle-raises-9-2")
L.append(C("castle", dispute=("status",), status="private", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2019-02", rng="below_1b", focus="Security",
    note="Account-takeover and fake-account protection (castle.io, San Francisco; founded in Sweden); 'raised $9.2M in Series A funding from Index Ventures' (the firm's post, 2019-02-12); the pre-filled 'acquired' is a one-word Wikidata join",
    rounds=[rnd("2019-02-12", "Series A", 9200000, "Index Ventures", True, u, "firm")]))
L.append(C("catch", status="unknown", country="US", city="New York", rng="below_1b", focus="Fintech & Payments",
    note="Pay-by-bank checkout with store-credit rewards for consumer brands (getcatch.com, New York); a seed in 2021 and a $12M Series A in 2022; Khosla's row reads defunct and no source read here confirms a shutdown or a sale (Google News 2026-10-01), so the last known state is not established"))
u = post("causaly-raises-17")
L.append(C("causaly", status="private", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2021-05", rng="below_1b", focus="AI & Applied AI",
    note="AI research platform for biomedical literature (London); Index led the $17M Series A (the firm's post, 2021-05-20; Tech.eu names the round), Carlos Gonzalez-Cadenas on the board; $60M Series B led by ICONIQ in July 2023",
    rounds=[rnd("2021-05-20", "Series A", 17000000, "Index Ventures", True, u, "firm"), rnd("2023-07-13", "Series B", 60000000, "ICONIQ Growth", True, post("causaly-raises-60m"), "firm")]))
L.append(C("chartbeat", dispute=("stage",), status="acquired", city="New York", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2010-08", focus="Media, Gaming & Advertising",
    note="Real-time web analytics for publishers (New York; a betaworks spin-out); Index led the $3M round of 2010 that the press named its Series A, Saul Klein joining the board (Form Ds 2010-2014); the band read the size as a seed; acq. by Cuadrilla Capital, 2022"))
L.append(C("check", status="private", country="US", city="New York", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Embedded payroll infrastructure (checkhq.com, New York); on the firm's list since 2021, Nina Achadjian; Stripe led the $35M Series B of 2021 and Thrive the $75M Series C of 2022 with Index named among the investors; no source read says which round Index entered", rounds=[]))
L.append(C("ciphercloud", status="acquired", city="San Jose", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2011", rng="below_1b", focus="Security",
    note="Cloud encryption and CASB (San Jose); Index and T-Venture backed the company before Andreessen Horowitz led the $30M Series B of December 2012 (the firm's own news item of 2012-12-05 lists the round); acq. by Lookout, 2021"))
L.append(C("citymapper", status="acquired", country="GB", country_src="wikidata", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Urban transit app (London); Balderton led the 2014 Series A with Index, Connect and Greylock; the firm's list marks it backed at Seed, Dominique Vidal the partner; acq. by Via, 2023"))
up = nqurl('"Class Companion" seed Index Ventures', "Panorama Acquires OpenAI-backed AI Tool")
L.append(C("class-companion", status="acquired", country="US", city="San Francisco", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2023-10", rng="below_1b",
    focus="AI & Applied AI", note="AI feedback tool for teachers (San Francisco); the $4M seed of October 2023 led by Index (Nina Achadjian and Cat Wu), OpenAI's startup fund among the investors; acq. by Panorama Education, 2025 (EdWeek Market Brief, 2025-04-25)",
    extra={"status_citation": up}))
u = post("clickhouse-bringing-the-power")
L.append(C("clickhouse", dispute=("usd", "rng"), city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2021-09", rng="10b_plus", **sv("clickhouse", "coatue"),
    focus="Data Infrastructure", note="Open-source OLAP database (ClickHouse, Inc., San Francisco Bay Area and Amsterdam; spun out of Yandex in 2021); Index and Benchmark co-led the $50M Series A at incorporation (the firm's post, 2021-09-20); $15B at the January 2026 round (aligned to Coatue's cited mark; the unicorn list's $2B is the 2021 Series B)",
    rounds=[rnd("2021-09-20", "Series A", 50000000, "Index Ventures, Benchmark", True, u, "firm")]))
u = post("clumio-announces-51m")
L.append(C("clumio", status="acquired", country="US", city="Santa Clara", stage="Growth", **WV, stage_cite=u, entry_date="2019-08", rng="below_1b", focus="Data Infrastructure",
    note="SaaS backup for cloud data (Santa Clara; a Sutter Hill company); Index led the $40M Series B announced with the $11M Series A as '$51M in funding' (the firm's post, 2019-08-14), Mike Volpi; acq. by Commvault, 2024",
    rounds=[rnd("2019-08-14", "Series B", 40000000, "Index Ventures", True, u, "firm")]))
L.append(C("coalition", dispute=("usd",), city="San Francisco", **sv("coalition", "ribbit-capital"), rng="1b_plus", focus="Fintech & Payments", flags=["stale"],
    note="Cyber insurance with active security monitoring (San Francisco); Index led the $90M Series C of May 2020 and the $175M Series D of March 2021, Shardul Shah on the board; $5B at the $250M Series F of July 2022 (aligned to Ribbit's cited mark; the unicorn list's $3.5B is the 2021 Series E), stale beyond 24 months"))
u = post("databases-will-inherit")
L.append(C("cockroach-labs", dispute=("usd",), city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2016-03", **sv("cockroach-labs", "coatue"), rng="1b_plus",
    focus="Data Infrastructure", flags=["stale"], note="Distributed SQL database (New York); 'Index is leading the $20 million Series A1 in Cockroach Labs' (the firm's post, 2016-03-30), Mike Volpi; $5B at the $278M Series F of December 2021 (aligned to Coatue's cited mark; the unicorn list's $2B is the January 2021 round), stale",
    rounds=[rnd("2016-03-30", "Series A", 20000000, "Index Ventures", True, u, "firm")]))
u = post("employee-leave-made-easy")
L.append(C("cocoon", dispute=("country",), status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2021-03", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="SaaS",
    note="Employee leave management (San Francisco); 'excited to lead Cocoon's $20M Series A just a few months after leading their $5M seed round' (the firm's post by Mark Goldberg, 2021-09-29); the pre-filled CZ is a one-word name join",
    rounds=[rnd("2021-03", "Seed", 5000000, "Index Ventures", True, u, "firm"), rnd("2021-09-29", "Series A", 20000000, "Index Ventures", True, u, "firm")]))
u = post("codat-raises-10m")
L.append(C("codat", status="private", country="GB", city="London", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2020-06", rng="below_1b",
    focus="Fintech & Payments", note="API for small-business financial data (London); Index led the $10M round of June 2020 the press named its Series A (the firm's post, 2020-06-11); $40M Series B led by Tiger Global in 2021 'with existing investors Index Ventures and PayPal Ventures', $100M Series C from JPMorgan in 2025",
    rounds=[rnd("2020-06-11", "Series A", 10000000, "Index Ventures", True, u, "firm")]))
u = narch("5 Reasons Why I Fell in Love with Codecademy")
L.append(C("codecademy", status="acquired", city="New York", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2012-06", rng="below_1b",
    focus="Consumer & Marketplaces", note="Online coding education (New York); Index led the $10M Series B of June 2012 (Saul Klein's post of 2012-06-19 on the firm's site) after Union Square Ventures' Series A; acq. by Skillsoft, 2022 (about $525M)",
    rounds=[rnd("2012-06-19", "Series B", 10000000, "Index Ventures", True, u, "firm")]))
u = post("cohere-and-the-ai-hype-cycle")
L.append(C("cohere", dispute=("usd",), country="CA", country_src="wikidata", city="Toronto", stage="Series A", **WV, stage_cite=u, entry_date="2021-09", **sv("cohere", "tiger-global-management"),
    rng="1b_plus", focus="AI & Applied AI", note="Enterprise large language models (Toronto); 'Our first investment in Cohere came in 2021, when we led the company's Series A' (the firm's post, 2023-11-13; $40M), Mike Volpi; $7B at the September 2025 round (aligned to Tiger Global's cited mark)",
    rounds=[rnd("2021-09-07", "Series A", 40000000, "Index Ventures", True, u, "firm")]))
L.append(C("collibra", dispute=("usd",), country="BE", country_src="wikidata", city="Brussels", stage="Growth", stage_src="model", stage_conf="high", entry_date="2015-09",
    **sv("collibra", "iconiq-growth"), rng="1b_plus", focus="Data Infrastructure", flags=["stale", "cite_pending"],
    note="Data governance and catalogue software (founded in Brussels, run from Brussels and New York); Index led the $23M Series B of September 2015, Jan Hammer on the board, and co-led the $112.5M Series F of April 2020 (the firm's post); $5.25B at the $250M round of November 2021 (aligned to ICONIQ's cited mark), stale",
    rounds=[rnd("2015-09", "Series B", 23000000, "Index Ventures", True, None, "press"), rnd("2020-04-02", "Series F", 112500000, "Index Ventures, ICONIQ", True, post("data-not-software"), "firm")]))
L.append(C("common-room", status="private", country="US", city="Seattle", rng="below_1b", focus="SaaS",
    note="Community and go-to-market intelligence platform (Seattle); launched in March 2021 with $52M across a seed led by Index, a Series A led by Greylock and a Series B; the firm's list marks it backed at Seed, Danny Rimer the partner"))
u = post("complyadvantage-raises-30m")
L.append(C("complyadvantage", status="private", country="GB", city="London", stage="Growth", **WV, stage_cite=u, entry_date="2019-01", rng="below_1b", focus="Fintech & Payments",
    note="Financial-crime screening data and software (London); 'Index Ventures ... led the Series B round, and were joined in the round by existing investor Balderton Capital' (the firm's post, 2019-01-30; $30M); $50M Series C in 2020",
    rounds=[rnd("2019-01-30", "Series B", 30000000, "Index Ventures", True, u, "firm")]))
L.append(C("confluent", dispute=("status", "rng", "usd"), status="acquired", country="US", city="Mountain View", stage="Growth", stage_src="model", stage_conf="high", entry_date="2015-07",
    rng="below_1b", focus="Data Infrastructure",
    note="Data streaming platform built on Apache Kafka (Mountain View; Nasdaq: CFLT, IPO June 2021); Index led the $24M Series B of July 2015, Mike Volpi joining the board, and joined the Series C and D (the firm's posts); acq. by IBM, 2026 (about $11B; three sibling books record the closing), so the pre-filled float no longer stands",
    rounds=[rnd("2015-07-08", "Series B", 24000000, "Index Ventures", True, None, "press"), rnd("2017-03-07", "Series C", 50000000, "Sequoia", True, post("confluent-raises-50-million"), "firm")]))
u = post("cord-raises-17-5m")
L.append(C("cord", status="unknown", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2021-10", rng="below_1b", focus="DevTools & APIs",
    note="Collaboration SDK for web apps (Radical HQ Ltd, London); Index led the $17.5M Series A (the firm's post, 2021-10-06; UK Tech Investment News names the lead); the company announced a wind-down in 2024 by the judge's recollection, which no source read here confirms: last known state not established",
    rounds=[rnd("2021-10-06", "Series A", 17500000, "Index Ventures", True, u, "firm")]))
u = post("rebirth-of-robotics")
L.append(C("covariant-ai", status="private", city="Emeryville", stage="Growth", **WV, stage_cite=u, entry_date="2020-05", rng="below_1b", focus="Industrial & Robotics",
    note="AI for warehouse robots (Emeryville); Index led the $40M Series B (the firm's post by Mike Volpi, 2020-05-06) and the $75M Series C extension of 2023; Amazon hired the founders and licensed the models in August 2024 without buying the company, which continues to operate (COLLECTION.md s6: an acqui-hire does not decide the status); the Coatue and Lux rows read acquired",
    rounds=[rnd("2020-05-06", "Series B", 40000000, "Index Ventures", True, u, "firm")]))
L.append(C("cowboy", status="private", country="BE", city="Brussels", rng="below_1b", focus="Consumer & Marketplaces",
    note="Connected electric bikes (Brussels); the EUR 10M Series A of October 2018 was 'led by Tiger Global Management alongside existing investors Index Ventures and Hardware Club' (the firm's post), so Index entered at the 2017 seed, which its list marks; $80M Series C in January 2022"))
u = post("our-investment-in-aetherflux")
L.append(C("cowboy-space", status="private", country="US", city="San Carlos", stage="Series A", **WV, stage_cite=u, entry_date="2025-04", rng="1b_plus", **sv("cowboy-space", "a16z"),
    focus="Industrial & Robotics", note="Orbital power and data-centre infrastructure, formerly Aetherflux (San Carlos; founded by Robinhood's Baiju Bhatt); 'leading Aetherflux's $50M Series A' (the firm's post, 2025-04-02), the first outside round; $275M Series B led by Index in May 2026 at $2B (aligned to a16z's cited mark). The firm's list marks it backed at Seed, which the record does not bear out (D8 score)",
    rounds=[rnd("2025-04-02", "Series A", 50000000, "Index Ventures", True, u, "firm")]))
u = post("by-combining-biotech-with-ai"); g = post("biotech-startup-cradle-raises-24m")
L.append(C("cradle", status="private", country="NL", city="Amsterdam", stage="Seed", **WV, stage_cite=u, entry_date="2022-11", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="Healthcare & Bio",
    note="Generative AI for protein engineering (Amsterdam and Zurich); Index co-led the $5.5M seed (the firm's post, 2022-11-17) and led the $24M Series A a year later (the firm's post, 2023-11-28: 'since its seed funding round in November 2022'); $73M Series B led by IVP in 2024",
    rounds=[rnd("2022-11-17", "Seed", 5500000, "Index Ventures, Kindred", True, u, "firm"), rnd("2023-11-28", "Series A", 24000000, "Index Ventures", True, g, "firm")]))
L.append(C("creative-juice", status="acquired", country="US", city="San Francisco", rng="below_1b", focus="Fintech & Payments",
    note="Banking and financing for online creators (San Francisco); seed in 2021 with Index (Mark Goldberg and Rex Woodbury), a $15M Series A in April 2022 (Tubefilter); merged into Rho in July 2024 (Net Influencer)"))
L.append(C("credit-benchmark", status="private", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013", rng="below_1b", focus="Fintech & Payments",
    note="Consensus credit-risk data pooled from banks (London); Index led the $7M Series A of 2013, Jan Hammer on the board (the firm's 2014 page); Balderton led the $20M Series B of July 2015"))
L.append(C("criteo", country="FR", country_src="wikidata", city="Paris", stage="Growth", stage_src="model", stage_conf="high", entry_date="2008-01", focus="Media, Gaming & Advertising",
    flags=["cite_pending"], note="Performance advertising and retail media (Paris; Nasdaq: CRTO, IPO October 2013); Index led the second round of January 2008 (the Series B), Dominique Vidal on the board until the IPO; the Index funds filed 13Gs from 2013"))
L.append(C("crossing-minds", status="defunct", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="AI & Applied AI",
    note="Recommendation engine for e-commerce (San Francisco); on the firm's 2022 list, Damir Becirovic; a $10M Series A in October 2021; OpenAI hired the team in June 2025 without buying the company, which stopped serving customers (Economic Times, 2025-06-30); the round Index entered is not on record", rounds=[]))
u = post("cue-launches-with-7-3m")
L.append(C("cue", dispute=("status", "stage"), status="unknown", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2018-11", rng="below_1b", focus="SaaS",
    note="Personal calendar app (CueCal, Inc., San Francisco); 'Index Ventures led the Series A investment round, with participation from existing investor, Khosla Ventures' (the firm's post, 2019-10-18; the $5.3M Form D of November 2018 carries Dino Becirovic); no trace after 2020; the pre-filled 'acquired' joins another Cue (the search app Apple bought in 2013)",
    rounds=[rnd("2018-11-09", "Series A", 5300000, "Index Ventures", True, u, "firm")]))
L.append(C("culture-amp", dispute=("country",), country="AU", city="Melbourne", stage="Growth", stage_src="model", stage_conf="high", entry_date="2017-05", focus="SaaS",
    flags=["cite_pending"], note="Employee engagement and performance software (Melbourne); Index led the $20M Series C of 2017 (Form D first sale 2017-05-31, Ilya Fushman as director; Neil Rimer the partner on the firm's page); $1.5B at the 2021 Series F; the Form D address is the San Francisco office",
    rounds=[rnd("2017-05-31", "Series C", 20000000, "Index Ventures", True, None, "filing")]))
u = post("everyone-is-a-seller")
L.append(C("curtsy", status="private", country="US", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2021-01", rng="below_1b", focus="Consumer & Marketplaces",
    note="Clothing resale app for Gen Z women (San Francisco); 'We're thrilled to lead their Series A' (the firm's post by Damir Becirovic, 2021-01-20; $11M)",
    rounds=[rnd("2021-01-20", "Series A", 11000000, "Index Ventures", True, u, "firm")]))
u = post("cutover-raises-17")
L.append(C("cutover", status="private", country="US", city="New York", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2019-11", rng="below_1b", focus="SaaS",
    note="Work orchestration for enterprise IT operations (founded in London, run from New York); Index led the $17M Series A (the firm's post, 2019-11-12); $35M Series B led by Eldridge in March 2021",
    rounds=[rnd("2019-11-12", "Series A", 17000000, "Index Ventures", True, u, "firm")]))
u = narch("Datadog Announces $6.2M Investment")
L.append(C("datadog", dispute=("usd",), city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2012-11", **sv("datadog", "iconiq-growth"), rng="10b_plus",
    focus="Data Infrastructure", note="Cloud monitoring and observability (New York; Nasdaq: DDOG, IPO September 2019); 'Datadog Announces $6.2M Investment from Index Ventures and RTP Ventures' (the firm's own news item, 2012-11-20), 'its Series A round' in the firm's later words, Shardul Shah on the board; market cap aligned to ICONIQ's cited figure, the pre-filled float is stale",
    rounds=[rnd("2012-11-20", "Series A", 6200000, "Index Ventures, RTP Ventures", True, u, "firm")]))
u = post("datasnipper-raises-100m")
L.append(C("datasnipper", status="private", country="NL", city="Amsterdam", stage="Growth", **WV, stage_cite=u, entry_date="2024-02", rng="1b_plus", **sv("datasnipper", "insight-partners"),
    focus="SaaS", flags=["stale"], note="Audit automation inside Excel (Amsterdam); 'a $100 million Series B, led by Index Ventures, at a valuation of $1B' (the firm's post, 2024-02-01; aligned to Insight's cited mark), stale beyond 24 months",
    rounds=[rnd("2024-02-01", "Series B", 100000000, "Index Ventures", True, u, "firm")]))
u = post("our-investment-in-daydream"); g = news("Daydream", "Daydream Secures $50 Million In Seed")
L.append(C("daydream", status="private", country="US", city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=g, entry_date="2024-06", rng="below_1b",
    focus="Consumer & Marketplaces", note="AI shopping search for fashion (Daydream, legal name Dahlia Labs; founded by Julie Bornstein); the $50M seed co-led by Forerunner and Index (PR Newswire and the firm's post, 2024-06-20; Form D first sale 2024-06-04 with Vlad Loktev as director)",
    rounds=[rnd("2024-06-20", "Seed", 50000000, "Forerunner, Index Ventures", True, g, "press")]))
u = post("our-investment-in-deepnote"); g = news("Deepnote", "Deepnote Raises $20 Million Series A, Led by Index")
L.append(C("deepnote", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2020-02", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="DevTools & APIs",
    note="Collaborative data science notebook (founded in Prague, run from San Francisco); 'co-leading Deepnote's Seed round with our good friends at Accel' ($3.8M, February 2020), then the $20M Series A led by Index and Accel (Business Wire and the firm's post, 2022-01-31)",
    rounds=[rnd("2020-02-06", "Seed", 3800000, "Index Ventures, Accel", True, u, "firm"), rnd("2022-01-31", "Series A", 20000000, "Index Ventures, Accel", True, g, "press")]))
gl.write("batch-002", L)
