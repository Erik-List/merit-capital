"""PRO-82 grind, batch-006 (roli .. taktile). Same evidence and conventions as batch-001. seedcamp is ruled in patch 1."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("roli", dispute=("country",), status="acquired", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Expressive electronic instruments (Seaboard, Blocks; London); the firm's list marks it backed at Seed; $27M Series B led by Foundry Group in May 2016 (the firm's own news item); administration in September 2021, the business bought out of it by the founder's new company Luminary ROLI (MusicTech, 2021-09-02; COLLECTION.md s6); the pre-filled DE is a one-word name join"))
u = news("Rooser", "nets $23 million from GV and Index")
L.append(C("rooser", status="defunct", city="Edinburgh", stage="Series A", **WV, stage_cite=u, entry_date="2022-04", rng="below_1b", focus="Consumer & Marketplaces",
    note="B2B seafood trading platform (Edinburgh); the $23M Series A of April 2022 led by Index with GV (Tech.eu, 2022-04-25; Form D first sale 2022-04-14, Georgia Stevenson as director); wound down, as the GV and Point Nine rows record",
    rounds=[rnd("2022-04-25", "Series A", 23000000, "Index Ventures", True, u, "press")]))
L.append(C("rpx", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2008", rng="below_1b", focus="SaaS",
    note="Defensive patent aggregation by subscription (RPX Corporation, San Francisco; Nasdaq: RPXC, IPO May 2011); founded in 2008 with Series A money from Kleiner Perkins, Charles River and Index, Giuseppe Zocco on the board; the Index funds filed a 13G after the IPO; acq. by HGGC, 2018"))
u = post("safety-first")
L.append(C("safetyculture", country="AU", country_src="wikidata", city="Sydney", stage="Growth", **WV, stage_cite=u, entry_date="2016-10", focus="SaaS",
    note="Workplace inspection and operations app (iAuditor; Sydney, founded in Townsville); 'we are proud to partner with Luke and lead a $23 million funding round in SafetyCulture' (the firm's post by Jan Hammer, 2016-10-18), the Series B; $1.6B at the 2021 round",
    rounds=[rnd("2016-10-18", "Series B", 23000000, "Index Ventures", True, u, "firm")]))
u = post("sanlo-the-financial-hub")
L.append(C("sanlo", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2021-05", rng="below_1b", focus="Fintech & Payments",
    note="Financing and financial tools for game and app developers (San Francisco); 'We're thrilled to be co-leading Sanlo's seed round' (the firm's post, 2021-05-12; $3.5M)",
    rounds=[rnd("2021-05-12", "Seed", 3500000, "Index Ventures", True, u, "firm")]))
g = news("Savvy", "Savvy Wealth Raises $100 Million Series C Led by Halo")
L.append(C("savvy", status="private", country="US", city="New York", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021-10", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="Fintech & Payments", flags=["stage_uncited"],
    note="Technology-led wealth management firm for financial advisors (Savvy Wealth, New York); Index led the $7M seed of 2021, Mark Goldberg; Thrive led the 2022 Series A, a $72M Series B followed in 2025 and a $100M Series C led by Halo Fund in September 2026",
    rounds=[rnd("2021-10", "Seed", 7000000, "Index Ventures", True, None, "press"), rnd("2026-09-21", "Series C", 100000000, "Halo Fund", None, g, "press")]))
u = post("scale-announces-18-million")
L.append(C("scale", status="private", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2018-08", rng="10b_plus", **sv("scale", "accel"),
    focus="AI & Applied AI", note="Training data and evaluation for AI models (Scale AI, San Francisco); '$18 million in Series B funding, led by Index Ventures with participation from existing investors Accel and Y Combinator' (the firm's post, 2018-08-07), Mike Volpi on the board; $29B at Meta's June 2025 investment for 49% (aligned to Accel's cited mark)",
    rounds=[rnd("2018-08-07", "Series B", 18000000, "Index Ventures", True, u, "firm")]))
L.append(C("science-exchange", status="private", city="Palo Alto", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013", rng="below_1b", focus="Healthcare & Bio",
    note="Marketplace for outsourced scientific research services (Palo Alto); Index joined the $3M Series A of 2013 led by Union Square Ventures (the firm's 2014 page names Neil Rimer and Terrence Rohan) and the $25M Series B of March 2016 led by Maverick (the firm's post lists Index among the participants)"))
L.append(C("scoop", status="acquired", country="US", city="San Francisco", rng="below_1b", focus="Consumer & Marketplaces",
    note="Employer carpooling, later hybrid-work planning (Scoop Technologies, San Francisco); the firm's list marks it backed at Seed, Danny Rimer on the board; $36M raised by November 2017 (the firm's own item) and $60M in 2019; the carpool app was bought by Spacer Technologies in 2024 (Yahoo Finance, 2024-07-09)"))
L.append(C("second-home", status="private", country="GB", city="London", rng="below_1b", extra={"focus": None},
    note="Creative workspaces and cultural venues (London, Lisbon, Los Angeles; founded 2014 by Rohan Silva, an Index entrepreneur-in-residence that year); the firm's list marks it backed at Seed; GBP 7.5M in January 2016; a workspace operator sits outside the focus taxonomy"))
u = narch("Why We're Backing Secret")
L.append(C("secret", dispute=("stage",), status="defunct", city="San Francisco", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2014-03",
    focus="Consumer & Marketplaces", note="Anonymous social app (San Francisco); 'The World Needs an Anonymous Social Network: Why We're Backing Secret' (the firm's own post), the $8.6M Series A Index led in March 2014 (Form D 2014-Q1, $10.6M), Danny Rimer on the board; the band read the $25M round of July 2014; shut down in April 2015",
    rounds=[rnd("2014-03", "Series A", 8600000, "Index Ventures", True, u, "firm")]))
u = narch("Secret Escapes wins further funding")
L.append(C("secret-escapes", status="private", city="London", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2012-10", rng="below_1b",
    focus="Consumer & Marketplaces", note="Members-only luxury travel flash sales (London); 'Secret Escapes wins further funding and plans global expansion' (the firm's own news item, 2012-10-15), the GBP 8M Series B Index led after Octopus and Atlas had funded the Series A, Ben Holmes on the board; $60M Series C in 2015, $111M in 2017",
    rounds=[rnd("2012-10-15", "Series B", None, "Index Ventures", True, u, "firm")]))
u = post("seedlegals-uk")
L.append(C("seedlegals", status="private", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2019-05", rng="below_1b", focus="SaaS",
    note="Legal automation for startup fundraising (London); the $4M Series A 'led by venture capital firm Index Ventures' (the firm's post, 2019-05-30)",
    rounds=[rnd("2019-05-30", "Series A", 4000000, "Index Ventures", True, u, "firm")]))
L.append(C("servicetitan", dispute=("usd",), city="Glendale", **sv("servicetitan", "coatue"), rng="1b_plus", focus="SaaS",
    note="Software for home-services contractors (Glendale, California; Nasdaq: TTAN, IPO December 2024); Index led the $165M Series D of November 2018 (the firm's post), Nina Achadjian on the board; market cap aligned to Coatue's cited figure"))
L.append(C("seso", status="private", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2023-01", rng="below_1b", focus="SaaS",
    note="Workforce and visa-compliance software for farm employers (San Francisco); Index led the $25M Series A of January 2023, Nina Achadjian; $26M Series B led by BOND in April 2024"))
L.append(C("shapeways", city="New York", rng="below_1b", focus="Industrial & Robotics",
    note="3D printing marketplace and manufacturing service (New York; founded in Eindhoven); Index entered in 2012 and led the $30M Series C of April 2013 (the firm's own news item), Ben Holmes on the board; public via Galileo Acquisition in 2021 (the funds' 13G); bankrupt in July 2024, the business bought back by its management that autumn"))
L.append(C("shopmonkey", status="private", city="San Jose", rng="below_1b", focus="SaaS",
    note="Shop-management software for auto repair (San Jose); 'leading the company's $10M Series A' (the firm's post, 2019-09-24), Nina Achadjian on the board; $25M Series B in 2020, $75M Series C in 2021"))
L.append(C("signal-sciences", status="acquired", country="US", city="Culver City", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2017-03", rng="below_1b", focus="Security",
    note="Web application firewall and API protection (Culver City, Los Angeles); Index joined the $15M Series B of March 2017 led by CRV, Shardul Shah; the Series C of February 2019 lists Index among the 'existing investors' (the firm's post); acq. by Fastly, 2020 (about $775M)"))
u = post("silverfin-raises-4-5m")
L.append(C("silverfin", status="acquired", country="BE", city="Ghent", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2017-03", rng="below_1b", focus="SaaS",
    note="Cloud accounting and reporting platform for accountancy firms (Ghent); the $4.5M Series A led by Index (the firm's post, 2017-03-14; Irish Tech News names the round); Hg led the 2020 Series B; acq. by Visma, 2023 ('Visma firm Silverfin', Enterprise Times 2026)",
    rounds=[rnd("2017-03-14", "Series A", 4500000, "Index Ventures", True, u, "firm")]))
g = news("Siro", "Siro Raises $50M in Series B")
L.append(C("siro", status="private", country="US", city="New York", stage="Seed", stage_src="model", stage_conf="low", entry_date="2022", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="AI & Applied AI", flags=["stage_uncited"],
    note="AI conversation coaching for in-person field sales (New York); Index led the seed of 2022, Damir Becirovic; a Series A in 2023 and a $50M Series B in May 2025 (FinSMEs)",
    rounds=[rnd("2022", "Seed", None, "Index Ventures", True, None, "press"), rnd("2025-05-23", "Series B", 50000000, None, None, g, "press")]))
u = post("sofia-mexicos-first")
L.append(C("sof-a", status="private", city="Mexico City", stage="Series A", **WV, stage_cite=u, entry_date="2020-11", rng="below_1b", focus="Fintech & Payments",
    note="Digital health insurer (Mexico City); 'their Series A round led by Index' (the firm's post, 2020-11-18; $19M; Form D first sale 2021-04, Neil Rimer as director); the founders' earlier 'angel investments from Index partners Jan Hammer, Neil Rimer and others' were personal and are not the firm's entry (T2); $13.5M in December 2024",
    rounds=[rnd("2020-11-18", "Series A", 19000000, "Index Ventures", True, u, "firm")]))
L.append(C("soluto", status="acquired", city="Tel Aviv", stage="Growth", stage_src="model", stage_conf="high", entry_date="2011-06", rng="below_1b", focus="SaaS",
    note="PC and device troubleshooting software (Tel Aviv); Index led the $10.2M Series B of June 2011, Saul Klein on the board (Form D 2011-Q2); acq. by Asurion, 2013 (up to $130M)"))
u = post("solvo-launches-new-app")
L.append(C("solvo", status="unknown", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2022-09", rng="below_1b", focus="Crypto & Web3",
    note="Consumer crypto investing app founded by former Revolut employees (solvo.finance, London); 'raised $3.5 million in seed funding led by Index Ventures' (the firm's post, 2022-09-29); no trace of the app after 2023 on any surface read, and no shutdown notice either: last known state not established; the Solvo of the cloud-security headlines is another company",
    rounds=[rnd("2022-09-29", "Seed", 3500000, "Index Ventures", True, u, "firm")]))
L.append(C("songkick", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Concert discovery and ticketing (London; a 2007 Y Combinator company); on the firm's list since 2009 under both its Seed stage and Early stage filters, Saul Klein on the board (Form D 2011, $2.0M); $10M Series B led by Sequoia in 2012; merged with CrowdSurge in 2015; acq. by Warner Music Group, 2017"))
L.append(C("sonos", dispute=("usd", "rng"), city="Santa Barbara", stage="Growth", stage_src="model", stage_conf="high", entry_date="2010", **sv("sonos", "headline"), rng="1b_plus",
    focus="Consumer & Marketplaces", flags=["cite_pending"],
    note="Wireless home audio (Santa Barbara; Nasdaq: SONO, IPO August 2018); Index invested in 2010, eight years into the company's life, and joined the $135M round of 2012, Mike Volpi on the board (the firm's post, 2018-08-02); the Index funds filed 13Gs after the IPO; market cap aligned to Headline's cited figure, the pre-filled float is stale"))
u = post("sourceful-raises-12"); g = post("sourceful-secures-20m")
L.append(C("sourceful", status="private", country="GB", city="Manchester", stage="Seed", **WV, stage_cite=u, entry_date="2021-09", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="SaaS",
    note="Sustainable packaging and sourcing platform (Manchester); 'The seed round was led by Index Ventures' ($12.2M; the firm's post, 2021-09-15), then 'a $20 million Series A funding round led by Index Ventures' (2022-03-29)",
    rounds=[rnd("2021-09-15", "Seed", 12200000, "Index Ventures", True, u, "firm"), rnd("2022-03-29", "Series A", 20000000, "Index Ventures", True, g, "firm")]))
u = post("spendesk-raises-8-million")
L.append(C("spendesk", country="FR", country_src="wikidata", city="Paris", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2018-01", focus="Fintech & Payments",
    flags=["stale"], note="Spend management for European businesses (Paris); Index led the EUR 8M Series A (the firm's post, 2018-01-29, quoting Dominique Vidal) and the EUR 35M Series B of September 2019; $1.1B at the January 2022 Series C extension, stale beyond 24 months",
    rounds=[rnd("2018-01-29", "Series A", None, "Index Ventures", True, u, "firm")]))
L.append(C("squarespace", city="New York", rng="below_1b", focus="SaaS",
    note="Website building and hosting (New York; NYSE: SQSP, direct listing May 2021); 'Index and Accel Back Squarespace' (the firm's own news item, 2010-07-14), the $38.5M first outside round, Dominique Vidal on the board; the funds filed 13Gs after the listing; acq. by Permira, 2024 ($7.2B)"))
L.append(C("stack-overflow", status="acquired", city="New York", rng="below_1b", focus="DevTools & APIs",
    note="Developer Q&A network, legal name Stack Exchange (New York); Index led the $12M Series B of early 2011 after Union Square Ventures' Series A, Neil Rimer on the board (Form Ds 2011 and 2015; the band reads the 2011 filing as a Series A by size); acq. by Prosus, 2021 ($1.8B; the firm's post)"))
u = post("starburst-and-presto")
L.append(C("starburst", status="private", country="US", city="Boston", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2019-11", rng="1b_plus", **sv("starburst", "a16z"),
    focus="Data Infrastructure", flags=["stale"], note="Distributed SQL query engine on Trino, formerly Presto (Boston); Index led the $22M Series A ('Starburst and Presto: with Stellar Velocity', the firm's post by Mike Volpi, 2019-11-20); $3.35B at the February 2022 Series D (aligned to a16z's cited mark), stale",
    rounds=[rnd("2019-11-20", "Series A", 22000000, "Index Ventures", True, u, "firm")]))
L.append(C("strapi", status="private", city="Paris", rng="below_1b", focus="DevTools & APIs",
    note="Open-source headless CMS (Paris and San Francisco); Index led the $10M Series A of May 2020 (the firm's post; Form D 2020-Q2 with Ari Helgason as director) after Accel's seed; $31M Series B in June 2022"))
ut = nqurl('"Stytch" Twilio acquire', "Twilio acquires Stytch for $104.1M")
L.append(C("stytch", dispute=("status", "rng", "usd"), status="acquired", city="San Francisco", rng="below_1b", focus="Security",
    note="Authentication APIs for developers (San Francisco); the firm's list marks it backed at Seed (the $6M seed of 2020), Mark Goldberg; Thrive led the 2021 Series A and Coatue the $90M Series B at $1B in November 2021; acq. by Twilio, closed November 2025 (the agreement of 2025-10-29; Coatue's row), so the unicorn-list mark no longer stands",
    extra={"status_citation": ut}))
u = post("achieving-the-sublime")
L.append(C("sublime-security", status="private", country="US", city="Washington", stage="Series A", **WV, stage_cite=u, entry_date="2024-04", rng="below_1b", focus="Security", flags=["needs_web_value"],
    note="Programmable AI email security (Washington, DC); 'Sublime Security Raises $20M Series A Led by Index Ventures' (PR Newswire and the firm's post, 2024-04-24), Shardul Shah on the board; a $150M Series C in October 2025 whose valuation is checked in the A/B pass",
    rounds=[rnd("2024-04-24", "Series A", 20000000, "Index Ventures", True, u, "firm")]))
us = news("Subset", "Rogo Acquires Subset")
L.append(C("subset", status="acquired", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Collaborative spreadsheet on a canvas (San Francisco); on the firm's list since 2023, Shimin Ooi then Nina Achadjian; no source read names the round Index entered; acq. by Rogo, 2025 (Business Wire, 2025-09-03)",
    rounds=[], extra={"status_citation": us}))
u = nqurl('"Super Evil Megacorp" Index Ventures', "Super Evil Megacorp raises $26 million, forges")
L.append(C("super-evil-megacorp", status="private", city="San Mateo", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015-08", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile games studio (Vainglory; San Mateo); Index led the $26M Series B of August 2015 (GamesIndustry.biz, 2015-08-10; Form D first sale 2015-07-29 with Ben Holmes as director) after a $11.6M Series A in 2014; $19M more in August 2017 (the firm's post); rebooted under Kristian Segerstrale in 2024",
    rounds=[rnd("2015-08-10", "Series B", 26000000, "Index Ventures", True, u, "press")]))
u = post("superconductive-expect-great")
L.append(C("superconductive", status="private", city="Cottonwood Heights", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2021-05", rng="below_1b",
    focus="Data Infrastructure", note="Maker of the Great Expectations data-quality framework, later renamed GX (Utah, remote-first); Index led the $21M Series A ('Superconductive: Expect Great Things From Your Data', the firm's post, 2021-05-20; Form D with Bryan Offutt as director), then joined the $40M Series B of February 2022",
    rounds=[rnd("2021-05-20", "Series A", 21000000, "Index Ventures", True, u, "firm")]))
g = post("supersolid-raises-4-million")
L.append(C("supersolid", status="private", country="GB", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile games studio (Home Street; London); the firm's list marks it backed at Seed (on its pages since 2014, Ben Holmes); 'raises $4 million Series A round led by Index' (the firm's post, 2017-10-12)"))
L.append(C("swile", country="FR", country_src="wikidata", city="Montpellier", stage="Growth", stage_src="model", stage_conf="high", entry_date="2019-02", focus="Fintech & Payments",
    flags=["stale", "cite_pending"], note="Employee benefits card and app, formerly Lunchr (Montpellier); Index led the EUR 30M Series B of February 2019 and the EUR 70M Series C of June 2020 (the firm's post), Martin Mignot and Dominique Vidal; $1B at the October 2021 round led by SoftBank, stale beyond 24 months",
    rounds=[rnd("2019-02", "Series B", None, "Index Ventures", True, None, "press"), rnd("2020-06-23", "Series C", None, "Index Ventures", True, post("swile-ex-lunchr"), "firm")]))
u = narch("Swipely to Reinvent")
L.append(C("swipely", dispute=("stage",), status="acquired", city="Providence", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2010-05",
    focus="SaaS", note="Restaurant management and payments software, renamed Upserve in 2016 (Providence); Index led the $7.5M Series A of May 2010 (the firm's own news item, 2010-05-11; Form D 2010-Q2, Danny Rimer as director) after a $1M seed from First Round; acq. by Lightspeed Commerce, 2020",
    rounds=[rnd("2010-05-11", "Series A", 7500000, "Index Ventures", True, u, "firm")]))
u = post("backing-sylvera"); g = post("sylvera-raises-32m")
L.append(C("sylvera", status="private", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2021-05", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="Climate & Energy",
    note="Carbon credit ratings and data (London); 'we are pleased to announce leading their seed investment of $5.8m' (the firm's post, 2021-05-13), then '$32.6M in Series A funding' co-led by Index and Insight (2022-01-25); $57M Series B led by Balderton in 2023",
    rounds=[rnd("2021-05-13", "Seed", 5800000, "Index Ventures", True, u, "firm"), rnd("2022-01-25", "Series A", 32600000, "Index Ventures, Insight Partners", True, g, "firm")]))
L.append(C("tactic", status="private", country="GB", city="London", rng="below_1b", focus="AI & Applied AI",
    note="AI research assistant for sales and market intelligence (tactic.fyi, London); the firm's list marks it backed at Seed, Jan Hammer; a $4.5M seed in 2022"))
L.append(C("tactile-games", status="private", city="Copenhagen", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile puzzle games studio (Lily's Garden; Copenhagen); on the firm's list from 2023, Danny Rimer; no source read names the round or the year Index entered (Google News 2026-10-01: nothing with the firm's name)", rounds=[]))
u = post("tacto-secures-50m")
L.append(C("tacto", status="private", country="DE", city="Munich", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2023-12", rng="below_1b", focus="SaaS",
    note="Procurement and supply-chain software for industrial mid-sized companies (Munich); 'EUR 50 million in new funding led by Index and Sequoia' (the firm's post, 2023-12-12), the Series A (Sequoia's row), after Cherry and Visionaries seeded it",
    rounds=[rnd("2023-12-12", "Series A", None, "Index Ventures, Sequoia", True, u, "firm")]))
u = post("taktile-raises-4-7m"); g = post("taktile-raises-20m")
L.append(C("taktile", status="private", country="US", city="New York", stage="Seed", **WV, stage_cite=u, entry_date="2021-08", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="AI & Applied AI",
    note="Decision-automation platform for lenders and insurers (founded in Berlin, run from New York); 'raised $4.7m in seed financing led by Index Ventures' (the firm's post, 2021-08-26), then '$20 million in Series A funding' led by Index and Tiger Global (2022-11-22); $54M Series B in 2025, $110M Series C led by Goldman Sachs in June 2026",
    rounds=[rnd("2021-08-26", "Seed", 4700000, "Index Ventures", True, u, "firm"), rnd("2022-11-22", "Series A", 20000000, "Index Ventures, Tiger Global", True, g, "firm")]))
gl.write("batch-006", L)
