"""PRO-82 grind, batch-009 (coverwallet .. frengo). Same evidence and conventions as batch-001. cyrenaic, epsilon-3-bio and
ff-pharma are life sciences desk rows (done). diartis and directmedica wait for the pre-2008 archive pass (their desk is not
on a page read yet). Label rows (stage left for the label pass): cruisewise, duna, edited, eisen, erply, fontself."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl, verdict, arch = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl, gl.verdict, gl.arch
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("coverwallet", status="acquired", country="US", city="New York", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2016-08", rng="below_1b",
    focus="Fintech & Payments", note="Online business-insurance broker for small companies (New York); Index co-led the $7.75M Series A of August 2016 with Union Square Ventures (which had seeded it), Mark Goldberg the partner; $18.5M Series B in October 2017 led by Foundation (the firm's post); acq. by Aon, 2020",
    extra={"status_citation": post("aon-to-acquire-coverwallet")}))
u = post("our-investment-in-crosby")
L.append(C("crosby", status="private", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2025-10", rng="below_1b", focus="AI & Applied AI",
    note="AI-native law firm for commercial contracts (New York); 'We couldn't be more thrilled to lead Crosby's Series A' (the firm's post, 2025-10-08); a $60M round followed in April 2026 (The Global Legal Post)",
    rounds=[rnd("2025-10-08", "Series A", None, "Index Ventures", True, u, "firm")]))
L.append(C("crowdrise", status="acquired", country="US", city="Detroit", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014-04", rng="below_1b",
    focus="Consumer & Marketplaces", note="Online charity fundraising platform (Royal Oak, in the Detroit area per the firm's 2014 page); Index joined the $23M Series A of April 2014 with Union Square Ventures, Spark and Bezos Expeditions, Danny Rimer the partner; acq. by GoFundMe, 2017"))
L.append(C("cruisewise", status="acquired", country="US", city="Boston", rng="below_1b", focus="Consumer & Marketplaces",
    note="Cruise search and booking site (Boston); on the firm's 2012 list under its Seed stage filter, with NEA; acq. by TripAdvisor, 2013"))
L.append(C("curbside", status="acquired", country="US", city="Palo Alto", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014", rng="below_1b",
    focus="Consumer & Marketplaces", note="Mobile order-ahead and store pickup (Palo Alto; founded by ex-Apple engineers); launched in 2014 on $9.5M from Index, Sutter Hill, AME and others, then $25M in June 2015 (Business Insider); acq. by Rakuten, 2018"))
u = post("investing-in-decagon")
L.append(C("decagon", status="private", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2026-01", rng="1b_plus", **sv("decagon", "a16z"), focus="AI & Applied AI",
    note="AI customer-support agents for enterprises (San Francisco); 'We are thrilled to co-lead Decagon's $250 million Series D and to welcome Jesse, Ashwin, and their team to Index' (the firm's post, 2026-01-28), at $4.5B (aligned to a16z's cited mark)",
    rounds=[rnd("2026-01-28", "Series D", 250000000, "Index Ventures, Coatue", True, u, "firm")]))
u = post("fluency-is-currency")
L.append(C("deepl", status="private", country="DE", city="Cologne", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-05", rng="1b_plus",
    **sv("deepl", "atomico"), focus="AI & Applied AI",
    note="AI translation and writing tools for business (Cologne); 'Index Partners Danny and Kathi share why Index is leading a $300m round' (the firm's post, 2024-05-22), a late-stage round at $2B (aligned to Atomico's cited mark)",
    rounds=[rnd("2024-05-22", "Growth round", 300000000, "Index Ventures", True, u, "firm")]))
L.append(C("digiquant", status="acquired", country="DK", city="Copenhagen", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Telecom billing and IP-services software (digiquant, formerly Belle Systems; Denmark); on the firm's 2008 list as a past investment tagged Intec Telecom Systems, which bought it in 2004; the round is not on record", rounds=[]))
u = post("dijas-game-changing")
L.append(C("dija", status="acquired", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2020-12", rng="below_1b", focus="Consumer & Marketplaces",
    note="Ten-minute grocery delivery from dark stores (London); 'Dija itself raised $20 million at the end of December - one of Europe's largest ever at seed stage - from Blossom Capital, Creandum, Index Ventures' (the firm's post, 2021-03-05); acq. by Gopuff, August 2021 (Business Wire), before any Series A",
    rounds=[rnd("2020-12", "Seed", 20000000, None, True, u, "firm")],
    extra={"status_citation": news("Dija", "Gopuff Doubles Down on European Expansion With Acquisition of Dija")}))
u = news("Dimdim", "gets $6 million in series B")
L.append(C("dimdim", dispute=("status",), status="acquired", city="Lowell", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2008-07", rng="below_1b",
    focus="SaaS", note="Open-source web conferencing (Lowell, Massachusetts, with engineering in Hyderabad); Index led the $6M Series B of July 2008 (The Next Web; the firm's own news item 'DimDim raises $6 million') after Draper Richards and Nexus had funded the first round; acq. by Salesforce, January 2011 ($31M), which the firm's list tags; the pre-filled 'defunct' is the product's shutdown after that sale",
    rounds=[rnd("2008-07-09", "Series B", 6000000, "Index Ventures", True, u, "press")],
    extra={"status_citation": nqurl('"Dimdim" Salesforce acquires', "Salesforce.com Acquires Dimdim")}))
L.append(C("dorsia", status="private", country="US", city="Miami", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2025-02", rng="below_1b", focus="Consumer & Marketplaces",
    note="Members-only platform for prepaid reservations at in-demand restaurants (Miami); the $50.4M round of February 2025 led by Index (Bloomberg; Refresh Miami), its first institutional round after a 2022 seed from angels, Martin Mignot the partner"))
L.append(C("doubledutch", status="acquired", country="US", city="San Francisco", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014", rng="below_1b", focus="SaaS",
    note="Mobile event apps for conferences (San Francisco); Index led the $19M round of 2014, the company's fourth, and the firm listed it that year; acq. by Cvent, 2019"))
L.append(C("doubletwist", status="unknown", city="San Francisco", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2007", rng="below_1b", focus="Consumer & Marketplaces",
    note="Media sync and player software, co-founded by Jon Lech Johansen (San Francisco); Index and Northzone funded the 2007 Series A; on the firm's lists to 2013; the apps are still published but no source read shows what became of the company (aligned to Northzone's row)"))
u = post("peer-to-peer-car-rental-service-drivy-raises")
L.append(C("drivy", status="acquired", country="FR", city="Paris", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2012", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="Consumer & Marketplaces",
    note="Peer-to-peer car rental (Paris); 'a EUR 6 million series A round, from existing investors Index Ventures and Alven Capital' (the firm's post, 2014-05-05): the firm was already in from the 2012 seed with Alven, and the Series A it funded is the graduation; acq. by Getaround, 2019 (the firm's own news item)",
    rounds=[rnd("2014-05-05", "Series A", None, None, True, u, "firm")], extra={"status_citation": narch("Getaround Acquires")}))
L.append(C("dropbox", country="US", city="San Francisco", stage="Growth", stage_src="model", stage_conf="high", entry_date="2011-10", focus="SaaS",
    note="File sync and collaboration (San Francisco; NASDAQ: DBX, IPO March 2018); Index led the $250M Series B of October 2011, Danny Rimer the partner (the firm's 2012 list is the first to carry it)"))
L.append(C("dropshop", status="defunct", country="DE", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces", flags=["city_unknown"],
    note="On the firm's 2008-2013 lists, marked exited from 2012, under its Early stage filter; no round and no location is on any surface read (status and country aligned to Balderton's row for the same company)", rounds=[]))
L.append(C("duna", dispute=("country",), status="private", country="NL", city="Amsterdam", rng="below_1b", focus="Fintech & Payments",
    note="Business identity and onboarding platform built by Stripe alumni (Amsterdam); EUR 10.7M led by Index in May 2025 (EU-Startups: 'Dutch startup Duna'), then 'thrilled to be backing them again' in the EUR 30M Series A of February 2026 (the firm's post); the pre-filled UA is a one-word name join"))
u = post("duo-security-raises-70-million")
L.append(C("duo", dispute=("country",), status="acquired", country="US", city="Ann Arbor", stage="Growth", **WV, stage_cite=u, entry_date="2017-10", rng="below_1b", focus="Security",
    note="Two-factor authentication and zero-trust access (Duo Security, Ann Arbor); 'The Series D round also included new investors, Geodesic Capital and Index Ventures' (the firm's post, 2017-10-18; $70M at $1.17B); acq. by Cisco, 2018 ($2.35B; the firm's post); the pre-filled JP is a one-word name join",
    rounds=[rnd("2017-10-18", "Series D", 70000000, "Meritech Capital Partners, Lead Edge Capital", True, u, "firm")], extra={"status_citation": post("duo-security-to-be-acquired")}))
u = nqurl('"duvo" Index Ventures', "Index Ventures led seed funding round")
L.append(C("duvo-ai", status="private", city="Prague", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2025-12", grad="censored", rng="below_1b",
    focus="AI & Applied AI", note="AI agents that run retail back-office operations, founded by the Rohlik team (Prague); 'Duvo raises $15 million in Index Ventures led seed funding round' (Retail Technology Innovation Hub, 2025-12-02); inside the 24-month window",
    rounds=[rnd("2025-12-02", "Seed", 15000000, "Index Ventures", True, u, "press")]))
L.append(C("edited", status="private", country="GB", city="London", rng="below_1b", focus="SaaS",
    note="Retail pricing and assortment analytics, founded as EDITD (London); on the firm's 2012 list under its Seed stage filter, Robin Klein the partner; $29M led by Wavecrest Growth in April 2020 (Crunchbase News)"))
L.append(C("edmodo", status="acquired", city="San Mateo", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2012", rng="below_1b", focus="Consumer & Marketplaces",
    note="Social learning network for classrooms (San Mateo); Index joined the later rounds (the $25M round of 2012 and the $30M of 2014; 'Why Index invested in Edmodo' on the firm's 2014 site); acq. by NetDragon, 2018 (aligned to Benchmark, Greylock and NEA); the service shut in 2022"))
L.append(C("eero", status="acquired", city="San Francisco", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2016", rng="below_1b", focus="Consumer & Marketplaces",
    note="Mesh home Wi-Fi systems (San Francisco); Index came in at the later rounds (the firm's 2019 page lists it), after First Round, Menlo and Redpoint; acq. by Amazon, 2019"))
L.append(C("eisen", status="private", country="US", city="New York", rng="below_1b", focus="Fintech & Payments",
    note="Escheatment and account-offboarding operations for financial institutions (New York); marked 'backed at Seed' on the firm's list; $18.5M announced in May 2026 (Business Wire; Fortune)"))
u = narch("Elasticsearch Closes $24M Series B")
L.append(C("elastic", dispute=("country",), status="public", country="NL", city="Amsterdam", stage="Growth", **WV, stage_cite=u, entry_date="2013-02", rng="1b_plus",
    **sv("elastic", "new-enterprise-associates"), focus="Data Infrastructure",
    note="Search and observability software, the company behind Elasticsearch (Elastic N.V., Amsterdam; NYSE: ESTC, IPO October 2018); '$24 million in Series B financing led by Mike Volpi from Index Ventures' (the firm's own news item, 2013-02-19); market cap aligned to NEA's cited read; the pre-filled DE is wrong for a Dutch N.V.",
    rounds=[rnd("2013-02-19", "Series B", 24000000, "Index Ventures", True, u, "firm")]))
u = post("enigma-emerges")
L.append(C("enigma", status="private", country="IL", city="Tel Aviv", stage="Seed", **WV, stage_cite=u, entry_date="2026-07", grad="censored", rng="below_1b", focus="AI & Applied AI",
    flags=["country_prior"], note="Physical AI models that let people steer robots in real time (enigma.inc; an Israeli team per Calcalist); 'we're excited to lead their $71 million seed round' (the firm's post, 2026-07-27, with Ribbit); inside the 24-month window; not the Enigma rows of Insight, NEA or Northzone",
    rounds=[rnd("2026-07-27", "Seed", 71000000, "Index Ventures", True, u, "firm")]))
L.append(C("erply", status="private", country="EE", city="Tallinn", rng="below_1b", focus="SaaS",
    note="Cloud point-of-sale and inventory software (Tallinn; Seedcamp 2009); $2M from Index and Redpoint in 2010; the firm's 2012 list files it under both its Seed and Early stage filters"))
u = post("ethonai-raises")
L.append(C("ethonai", status="private", country="CH", city="Zurich", stage="Series A", **WV, stage_cite=u, entry_date="2024-05", rng="below_1b", focus="AI & Applied AI",
    note="Causal AI analytics for manufacturing quality (Zurich; an ETH spin-off); '$16.5m (CHF 15m) Series A funding - led by Index Ventures' (the firm's post, 2024-05-30)",
    rounds=[rnd("2024-05-30", "Series A", 16500000, "Index Ventures", True, u, "firm")]))
L.append(C("evolven", status="private", country="US", city="Jersey City", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2008", rng="below_1b", focus="DevTools & APIs",
    note="IT configuration and change analytics (Evolven Software; Jersey City and Israel); Index and Pitango funded the Series A of 2008; on the firm's lists to 2013 under its Early stage filter"))
L.append(C("facebook", country="US", city="Menlo Park", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2010", focus="Media, Gaming & Advertising",
    note="Social network (Meta Platforms, Menlo Park; NASDAQ: META, IPO May 2012); the firm bought into the company late, before the IPO, through secondary shares (Growth by the taxonomy), Danny Rimer the partner; on its lists 2013-2022 as an exit"))
L.append(C("faceit", status="acquired", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2016-01", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Competitive gaming and esports tournament platform (London); the $15M Series A of January 2016 with Anthos and United Ventures (Variety), Ben Holmes the partner; acq. by Savvy Gaming Group, 2022, and merged with ESL (the $1.5B deal covered both)",
    extra={"status_citation": news("FACEIT", "Saudi-Backed Group Merging ESL, FACEIT")}))
L.append(C("fantastic", status="defunct", country="CH", city="Zug", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Broadband data-broadcasting software (The Fantastic Corporation, Zug); floated on Frankfurt's Neuer Markt in 1999 (the firm's 2008 list tags it Frankfurt:FAN as a past investment); wound down after the dot-com collapse; the round is not on record", rounds=[]))
L.append(C("fast", status="defunct", country="US", city="San Francisco", stage="Seed", stage_src="model", stage_conf="low", entry_date="2019", rng="below_1b", focus="Fintech & Payments",
    flags=["stage_uncited"], note="One-click checkout for online stores (San Francisco); Index led the 2019 seed, then joined the $20M Series A led by Stripe (March 2020) and the $102M Series B (January 2021), Jan Hammer on the board; shut down in April 2022"))
L.append(C("ferry-health", status="private", country="US", city="New York", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite=nqurl('"Ferry Health" stealth seed', "Ferry Health exits stealth with $9M seed"), entry_date="2026-09", grad="censored", rng="below_1b", focus="Healthcare & Bio",
    flags=["country_prior"], note="AI personal assistant that books and manages healthcare appointments (ferry.health); out of stealth on 2026-09-16 with a $9M seed led by Index (PR Newswire; Wilson Sonsini), Martin Mignot the partner; inside the 24-month window; the city is inferred from its New York launch"))
u = narch("FilesX, Inc. Announces")
L.append(C("filesx", status="acquired", country="US", city="Southborough", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2003-04", rng="below_1b",
    focus="Data Infrastructure", note="Continuous data protection and recovery software (Southborough, Massachusetts; R&D in Israel); 'a $7.5 million round of venture financing from Benchmark Capital, Index Ventures, and Genesis Partners' (the firm's own news item, 2003-04-15), the company's first venture round; acq. by IBM, 2008 (the firm's own news item)",
    rounds=[rnd("2003-04-15", "Series A", 7500000, None, True, u, "firm")], extra={"status_citation": narch("IBM Signs Agreement to Acquire FilesX")}))
u = post("candid-with-index-in-conversation-with-fireworks")
L.append(C("fireworks", status="private", country="US", city="Redwood City", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2025-10", rng="10b_plus",
    **sv("fireworks", "insight-partners"), focus="AI & Applied AI",
    note="Inference cloud for open AI models (Redwood City); 'Since we first invested in Fireworks last October' (the firm's post, 2026-07-16): the $250M Series C at $4B that Index co-led with Lightspeed (WSJ, 2025-10-28); $17.5B at the July 2026 round (aligned to Insight's cited mark)",
    rounds=[rnd("2025-10-28", "Series C", 250000000, "Lightspeed, Index Ventures", True, post("inference-is-the-new-runtime"), "firm")]))
u = post("taking-flight")
L.append(C("flapping-airplanes", status="private", country="US", city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite=nqurl('"Flapping Airplanes" seed valuation', "Research-First AI Lab With $180M Seed Round"), entry_date="2026-01", grad="censored", rng="below_1b", focus="AI & Applied AI",
    flags=["needs_web_value"], note="Foundational AI research lab working on data-efficient learning (San Francisco); 'to co-lead this investment alongside our friends at GV and Sequoia' (the firm's post, 2026-01-28), the $180M seed; reported at a $1.5B valuation, a figure only an aggregator headline carries so far (Rule A: checked in the A/B pass); inside the 24-month window",
    rounds=[rnd("2026-01-28", "Seed", 180000000, "GV, Sequoia, Index Ventures", True, u, "firm")]))
L.append(C("fon", dispute=("country",), status="acquired", country="ES", city="Madrid", stage="Series A", stage_src="model", stage_conf="high", entry_date="2006-02", rng="below_1b",
    focus="Industrial & Robotics", note="Shared Wi-Fi network and routers (Madrid; founded by Martin Varsavsky); the EUR 18M Series A of February 2006 from Index, Sequoia, Google and Skype, Danny Rimer on the board; acquired in 2019 (aligned to Atomico's row); the pre-filled PL is a one-word name join"))
L.append(C("fontself", status="private", country="CH", city="Lausanne", rng="below_1b", focus="DevTools & APIs",
    note="Font-creation tools for designers (Fontself, Lausanne area); on the firm's 2010-2013 lists under its Seed stage filter"))
u = post("solving-the-human-risk")
L.append(C("frame-security", status="private", country="IL", city="Tel Aviv", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-05", grad="censored", rng="below_1b",
    focus="Security", note="Human-risk and security-awareness platform built by early Wiz staff (Tel Aviv); 'We're delighted to have been Tal, Sharon, and the Frame team's first partner, and looking forward to new investor Team8's support' (the firm's post, 2026-05-11): the firm's entry is the first round, announced with $50M in total; inside the 24-month window",
    rounds=[rnd("2026-05-11", "undisclosed", 50000000, "Index Ventures", True, u, "firm")]))
L.append(C("frengo", status="acquired", country="US", city="San Mateo", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Mobile social messaging start-up (San Mateo) that became the mobile ad platform AdMarvel; Index funded it in 2006, Neil Rimer the partner; acq. by Opera Software, 2010 (the firm's page tags it OSE:OPERA)"))
gl.write("batch-009", L)
