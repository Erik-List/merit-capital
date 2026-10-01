"""PRO-82 grind, batch-013 (spot-runner .. zend). Same evidence and conventions as batch-001. spinx-technologies and xo1 are
life sciences desk rows (done). Name variants merged at the rebuild: streethub (into trouva), voiturelib (into drivy).
Left open (no round, place or outcome on any surface read yet): the-garden, v-watch. Label row: the-gifts-project."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl, verdict, arch = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl, gl.verdict, gl.arch
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("spot-runner", status="defunct", country="US", city="Los Angeles", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Online platform for buying local TV advertising (Los Angeles); Index and Battery funded the 2006 Series A; 'Spot Runner Receives $51 Million in New Funding' (the firm's own news item, 2008-05-07); wound down in 2010-2011 (aligned to Battery's row)"))
L.append(C("sproutl", status="unknown", country="GB", city="London", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["stage_uncited"], note="Online garden and plant marketplace founded by former Farfetch executives (London; launched July 2021); Index led its seed, Danny Rimer and Georgia Stevenson the partners (the firm's 2022 page); no later round and no outcome on any surface read"))
L.append(C("stardoll", status="defunct", country="SE", city="Stockholm", stage="Series A", stage_src="model", stage_conf="high", entry_date="2006", rng="below_1b", focus="Consumer & Marketplaces",
    note="Dress-up games and social network for teenagers (Stockholm); Index led the 2006 Series A, Sequoia the Series B the same year; 'Stardoll merges with Piczo' (the firm's own news item, 2009-03-09); status aligned to Sequoia's row"))
L.append(C("stepstone", status="acquired", country="NO", city="Oslo", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online job boards across Europe (Oslo; IPO 2000 in Oslo and Frankfurt); an Index investment of the late 1990s, Neil Rimer the partner; acq. by Axel Springer, 2009 (aligned to Northzone's row); the round is not on record", rounds=[]))
u = narch("Microsoft Reaches Agreement to Acquire StorSimple")
L.append(C("storsimple", status="acquired", city="Santa Clara", stage="Series A", stage_src="model", stage_conf="high", entry_date="2009", rng="below_1b", focus="Data Infrastructure",
    note="Hybrid cloud storage appliances (Santa Clara); Index and Redpoint funded the $8.2M Series A of 2009; 'Microsoft Reaches Agreement to Acquire StorSimple' (the firm's own news item, 2012-10-17)",
    extra={"status_citation": u}))
L.append(C("storybird", status="unknown", country="CA", city="Toronto", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["country_prior"], note="Visual storytelling platform pairing illustrators with young writers (Storybird; Toronto founders); on the firm's 2013-2014 lists under its Early stage filter; neither the round nor a later outcome is on any surface read", rounds=[]))
L.append(C("stylistpick", status="unknown", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2011", rng="below_1b", focus="Consumer & Marketplaces",
    note="Subscription fashion e-commerce with celebrity stylists (London); Index and Accel funded its 2011 Series A; on the firm's 2012-2013 lists; no outcome on any surface read"))
u = post("why-we-invested-in-supercell")
L.append(C("supercell", dispute=("country",), country="FI", city="Helsinki", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2013-04", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Mobile games, maker of Clash of Clans (Helsinki); 'my partners and I took the contrary view and decided to lead a EUR 100 million investment in the company' (the firm's post, 2013-04-17), a secondary-led purchase at about $770M (Growth by the taxonomy), Neil Rimer the partner; majority sold to SoftBank in 2013 and to Tencent in 2016",
    rounds=[rnd("2013-04-17", "Growth round", None, "Index Ventures", True, u, "firm")]))
u = news("Superlinked", "Superlinked Raises $9.5 Million Seed From Index Ventures and Theory Ventures")
L.append(C("superlinked", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2024-03", rng="below_1b", focus="Data Infrastructure",
    note="Framework for turning structured and unstructured data into vector embeddings (San Francisco); 'Superlinked Raises $9.5 Million Seed From Index Ventures and Theory Ventures' (PR Web, 2024-03-18)",
    rounds=[rnd("2024-03-18", "Seed", 9500000, "Index Ventures, Theory Ventures", True, post("superlinked-raises"), "firm")]))
L.append(C("swiftkey", dispute=("country",), country="GB", city="London", stage="Growth", stage_src="model", stage_conf="high", entry_date="2013-09", rng="below_1b", focus="AI & Applied AI",
    note="Predictive smartphone keyboard (London); Index led the $17.5M Series B of September 2013 after Octopus and Accel, Martin Mignot the partner; acq. by Microsoft, 2016 ($250M)",
    extra={"status_citation": news("SwiftKey", "Microsoft acquires keyboard app maker SwiftKey")}))
u = post("swoon-editions-makes")
L.append(C("swoon-editions", status="acquired", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2013-05", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="Consumer & Marketplaces",
    note="Online furniture brand selling limited runs direct from makers (London); 'Octopus Investments led the round with additional investment from Index Ventures. The transaction is a follow-on from a seed round of GBP 1.2 million in May 2013 ... our existing investors have decided to support us further' (the firm's post on the GBP 4M round, 2014-07-21); bought out of administration by its founders in a pre-pack, December 2019 (Retail Gazette)",
    rounds=[rnd("2013-05", "Seed", None, None, True, u, "firm"), rnd("2014-07-21", "Series A", None, "Octopus Investments", True, u, "firm")],
    extra={"status_citation": nqurl('"Swoon" furniture acquired', "Swoon bought out of administration by co-founders")}))
L.append(C("tamara-mellon", status="private", country="US", city="Los Angeles", stage="Series A", stage_src="model", stage_conf="low", entry_date="2013", rng="below_1b", focus="Consumer & Marketplaces",
    note="Direct-to-consumer luxury footwear brand of the Jimmy Choo co-founder (now Los Angeles; New York on the firm's 2014 page); Index backed the 2013 launch company, Danny Rimer the partner; it went through Chapter 11 in 2015-2016 and relaunched with NEA; $50M Series C in June 2019"))
u = post("teemo-raises-16m")
L.append(C("teemo", status="private", country="FR", city="Paris", stage="Series A", **WV, stage_cite=u, entry_date="2017-03", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Drive-to-store mobile advertising for retailers (Paris; formerly Databerries); 'is today announcing a $16 million Series A round led by Index Ventures' (the firm's post, 2017-03-21), Dominique Vidal on the board",
    rounds=[rnd("2017-03-21", "Series A", 16000000, "Index Ventures", True, u, "firm")]))
L.append(C("telegent-systems", status="acquired", country="US", city="Sunnyvale", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    note="Single-chip mobile TV receivers (Sunnyvale); on the firm's lists under its Early stage filter, and its 2009 S-1 names the Index funds; acq. by Spreadtrum, 2011; which round the firm entered is not on a surface read", rounds=[]))
u = post("empowering-choice")
L.append(C("thatch", dispute=("country",), country="US", city="San Francisco", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-09", focus="Fintech & Payments",
    note="Health-benefit budgets (ICHRA) that let employees pick their own insurance (San Francisco); 'Empowering Choice: Thatch and a new era of freedom in healthcare' (the firm's post, 2024-09-05), published with the $38M Series B that Index led; $108M Series C at $1B in September 2026 (Fierce Healthcare); the pre-filled GB is a one-word name join",
    rounds=[rnd("2024-09-05", "Series B", 38000000, "Index Ventures", True, u, "firm")]))
L.append(C("the-gifts-project", status="acquired", country="IL", city="Tel Aviv", rng="below_1b", focus="Consumer & Marketplaces",
    note="Group-gifting platform for online retailers (Tel Aviv); on the firm's 2012 list under its Seed stage filter; acq. by eBay, September 2011 (Haaretz)",
    extra={"status_citation": news("The Gifts Project", "eBay Buys The Gifts Project")}))
L.append(C("thefamily", status="unknown", country="FR", city="Paris", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Start-up education and support company that took small equity stakes in its members (TheFamily, Paris; founded 2013); the firm held shares in the operating company itself, Martin Mignot the partner (pages 2014-2020); the round is not on record, and its later history (a 2022 dispute among the founders) is not on a surface read", rounds=[]))
u = post("thread-ai-emerges")
L.append(C("thread-ai", status="private", country="US", city="New York", stage="Seed", **WV, stage_cite=u, entry_date="2024-10", rng="below_1b", focus="AI & Applied AI",
    note="Composable infrastructure for enterprise AI workflows, founded by former Palantir engineers (New York); 'The company has raised $6 million in seed funding, led by Index Ventures' (the firm's post, 2024-10-01); $20M in June 2025 (PYMNTS)",
    rounds=[rnd("2024-10-01", "Seed", 6000000, "Index Ventures", True, u, "firm")]))
L.append(C("toolbx", status="private", country="CA", city="Toronto", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Ordering and delivery software for building-supply dealers (Toronto); on the firm's 2021-2025 pages, Damir Becirovic the partner; which round the firm joined is not on any surface read", rounds=[]))
u = post("topi-raises-15m-series-a")
L.append(C("topi", status="acquired", country="DE", city="Berlin", stage="Seed", **WV, stage_cite=u, entry_date="2021-12", grad="graduated", grad_src="first_party", grad_cite=u, rng="below_1b",
    focus="Fintech & Payments", note="Hardware-as-a-service subscriptions for business equipment (Berlin); 'Index Ventures having led the company's $4.5m seed round', then '$15m is equity led by Index Ventures and Creandum' in the Series A (the firm's post, 2022-08-31); acq. by PEAC Solutions, 2025 (EU-Startups)",
    rounds=[rnd("2022-08-31", "Series A", 15000000, "Index Ventures, Creandum", True, u, "firm")], extra={"status_citation": news("Topi", "topi is acquired by PEAC Solutions")}))
L.append(C("transform", status="acquired", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2021", rng="below_1b", focus="Data Infrastructure",
    note="Metrics store for analytics teams, founded by former Airbnb data engineers (San Francisco); launched in June 2021 with $24.5M across a seed and a Series A (TechCrunch), Index in the Series A with Bryan Offutt, Redpoint from the seed; acq. by dbt Labs, 2023",
    extra={"status_citation": nqurl('"Transform" metrics Series A Index Ventures Redpoint', "Dbt Labs acquires Transform")}))
u = narch("Trello raises $10m Series A")
L.append(C("trello", status="acquired", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2014-07", rng="below_1b", focus="SaaS",
    note="Kanban-style project boards, spun out of Fog Creek (New York); 'Trello raises $10m Series A funding from Index Ventures and Spark Capital' (the firm's own item, 2014), Neil Rimer the partner; acq. by Atlassian, 2017 ($425M; WSJ)",
    rounds=[rnd("2014-07", "Series A", 10000000, "Index Ventures, Spark Capital", True, u, "firm")], extra={"status_citation": news("Trello", "Atlassian to Buy Trello for $425 Million")}))
L.append(C("trialpay", status="acquired", country="US", city="Mountain View", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2007", rng="below_1b", focus="Fintech & Payments",
    note="Transactional advertising and alternative payments (Mountain View); Index led the 2007 Series A, Danny Rimer on the board, then joined the Series B of 2008 with Battery; acq. by Visa, 2015 (TechCrunch)",
    extra={"status_citation": news("Trialpay", "Visa Announces Acquisition Of TrialPay")}))
L.append(C("trolltech", dispute=("status", "country"), status="acquired", country="NO", city="Oslo", stage="undetermined", rng="below_1b", focus="DevTools & APIs",
    note="Qt cross-platform application framework (Oslo; Oslo IPO July 2006); on the firm's lists under its Early stage filter, Neil Rimer the partner; acq. by Nokia, 2008 (the firm's page tags it OMX:NOK1V); which pre-IPO round the firm entered is not on a surface read; the pre-filled 'defunct' is the dissolved entity after that sale", rounds=[]))
u = news("Trouva", "Trouva secures $10m investment in Series A funding round")
L.append(C("trouva", status="acquired", country="GB", city="London", stage="Seed", stage_src="model", stage_conf="low", entry_date="2014", grad="graduated", grad_src="web_verified", grad_cite=u,
    rng="below_1b", focus="Consumer & Marketplaces", flags=["stage_uncited"], extra={"entry_stage_confidence": "low", "status_citation": nqurl('"Trouva" Made.com acquires', "Made.com acquires marketplace Trouva")},
    note="Online marketplace for independent homeware boutiques, founded as StreetHub (London; the firm's 2014 list carries StreetHub: one row after the rebuild); Index was in the 2014 seed and stayed in the $10M Series A of November 2017 led by Octopus and BGF (TheIndustry.fashion; the firm's post), Martin Mignot the partner; acq. by Made.com, May 2022",
    rounds=[rnd("2017-11-13", "Series A", 10000000, "Octopus Ventures, BGF Ventures", True, post("trouva-lands"), "firm")]))
L.append(C("ubermedia", status="acquired", country="US", city="Pasadena", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2010-04", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile advertising and location data from Idealab, founded as TweetUp (Pasadena; the Form D row TweetUp is the same company, merged at the rebuild); $3.5M in April 2010 from Index and others, Danny Rimer on the board; acq. by Near, 2021"))
u = post("valdera-secures")
L.append(C("valdera", status="private", country="US", city="San Francisco", stage="Series A", **WV, stage_cite=u, entry_date="2024-10", rng="below_1b", focus="SaaS",
    note="Sourcing platform for chemicals and raw materials (San Francisco); 'The company's $15 million Series A funding round has been led by Index Ventures' (the firm's post, 2024-10-03)",
    rounds=[rnd("2024-10-03", "Series A", 15000000, "Index Ventures", True, u, "firm")]))
L.append(C("venice", status="private", country="IL", city="Tel Aviv", stage="Seed", stage_src="model", stage_conf="low", entry_date="2024", rng="below_1b", focus="Security",
    flags=["stage_uncited"], note="Privileged access management for cloud and on-premise systems (Tel Aviv); out of stealth in February 2026 with $33M across a seed and a Series A led by IVP (the firm's post: 'following their seed round, the team spent over a year' building), Juriaan Duizendstraal the partner; not Venice AI"))
u = post("vinyl-equity-secures"); g = news("Vinyl Equity", "Vinyl Equity Raises $20 Million Series A to Modernize")
L.append(C("vinyl-equity", status="private", country="US", city="New York", stage="Seed", **WV, stage_cite=u, entry_date="2025-04", grad="graduated", grad_src="web_verified", grad_cite=g, rng="below_1b",
    focus="Fintech & Payments", note="Digital transfer agent for public companies (New York); 'Vinyl Equity Secures $11.5M Seed Round' from Index and Spark (the firm's post, 2025-04-14), then 'Vinyl Equity Raises $20 Million Series A' led by Jump Capital (Pulse 2.0, 2026-06-11)",
    rounds=[rnd("2025-04-14", "Seed", 11500000, "Index Ventures, Spark Capital", True, u, "firm"), rnd("2026-06-11", "Series A", 20000000, "Jump Capital", None, g, "press")]))
L.append(C("virata", status="acquired", country="US", city="Santa Clara", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    note="DSL chipsets and software (founded in Cambridge, UK, as ATM Ltd; Santa Clara from 1998; NASDAQ IPO 1999); an Index investment of the 1990s, Giuseppe Zocco the partner; merged into GlobespanVirata in 2001 and Conexant in 2004 (the firm's page tags it Conexant; aligned to NEA's row); the round is not on record", rounds=[]))
L.append(C("virtuallogix", status="acquired", city="Sunnyvale", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2002", rng="below_1b", focus="DevTools & APIs",
    note="Real-time virtualisation software for embedded and mobile devices (Sunnyvale; founded near Paris as Jaluna); Index funded Jaluna's 2002 first round with Atlas; acq. by Red Bend Software, 2010 (the firm's list tags it)"))
L.append(C("vitaminic", status="acquired", country="IT", city="Turin", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Digital music distribution platform (Turin; Nuovo Mercato IPO October 2000, Milan: BVTA per the firm's tag); an Index investment of 1999-2000; merged with Buongiorno in 2003; the round is not on record", rounds=[]))
u = news("Vizcom", "Vizcom Secures $20M Series A")
L.append(C("vizcom", status="private", country="US", city="San Francisco", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-03", rng="below_1b",
    focus="AI & Applied AI", note="AI rendering and ideation tools for industrial designers (San Francisco); 'Vizcom Secures $20M Series A' (Maginative, 2024-03-29), led by Index ('We're excited to partner with the team', the firm's post of 2024-03-28), Nina Achadjian the partner",
    rounds=[rnd("2024-03-28", "Series A", 20000000, "Index Ventures", True, post("inside-vizcom"), "firm")]))
u = post("vooma-secures")
L.append(C("vooma", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2024", grad="graduated", grad_src="first_party", grad_cite=u, rng="below_1b",
    focus="AI & Applied AI", note="AI agents for freight brokers and carriers (San Francisco); 'The company has announced $3.6 million in seed funding, led by Index Ventures, and a closely followed $13 million Series A round' (the firm's post, 2024-12-04; the Series A led by Craft)",
    rounds=[rnd("2024", "Seed", 3600000, "Index Ventures", True, u, "firm"), rnd("2024-12-04", "Series A", 13000000, "Craft Ventures", True, u, "firm")]))
L.append(C("wool-and-the-gang", status="acquired", country="GB", city="London", stage="Seed", stage_src="model", stage_conf="low", entry_date="2013-07", rng="below_1b",
    focus="Consumer & Marketplaces", flags=["stage_uncited"], note="Knit-kit and yarn fashion brand (London); the $2.8M round of July 2013 from Index, MMC and Wellington (Growth Business), its first venture round, Neil Rimer the partner; acq. by BlueGem (LoveCrafts group), 2018"))
u = narch("Index leads $12.5 million Series B in WooMe")
L.append(C("woome", status="acquired", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2008-06", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online speed-dating and video introductions (London and Los Angeles; aligned to Atomico's row for place); 'Index leads $12.5 million Series B in WooMe' (the firm's own news item, 2008-06-12); acq. by Zoosk, 2011",
    rounds=[rnd("2008-06-12", "Series B", 12500000, "Index Ventures", True, u, "firm")]))
u = narch("WorkLight Secures $12 Million")
L.append(C("worklight", status="acquired", country="IL", city="Tel Aviv", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2008-05", rng="below_1b",
    focus="DevTools & APIs", note="Mobile application platform for enterprises (an Israeli company per Haaretz; US base in New York); 'WorkLight Secures $12 Million in Series B Round' (the firm's own news item, 2008-05-01), the round Index led; 'IBM Advances Mobile Capabilities with Acquisition of Worklight' (2012-01-31)",
    rounds=[rnd("2008-05-01", "Series B", 12000000, "Index Ventures", True, u, "firm")], extra={"status_citation": narch("IBM Advances Mobile Capabilities")}))
L.append(C("xapo", dispute=("country",), status="private", country="GI", city="Gibraltar", stage="Series A", stage_src="model", stage_conf="high", entry_date="2014-07", rng="below_1b",
    focus="Crypto & Web3", note="Bitcoin custody and private bank (Xapo Bank, Gibraltar; Zurich on the firm's 2014 page, founded in Buenos Aires and Palo Alto); Index and Greylock led the $20M round of July 2014 ('The Global Bitcoin Opportunity: Why Index is Backing Xapo'), Mike Volpi on the board; its institutional custody business went to Coinbase in 2019; place aligned to Greylock and Ribbit"))
L.append(C("zend", status="acquired", country="IL", city="Tel Aviv", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2004", rng="below_1b", focus="DevTools & APIs",
    note="The PHP company: runtime, server and tools (founded in Ramat Gan, US base in Cupertino; place aligned to Greylock's row); Index joined the mid-2000s rounds after the first venture round, Danny Rimer on the board; acq. by Rogue Wave Software, 2015"))
gl.write("batch-013", L)
