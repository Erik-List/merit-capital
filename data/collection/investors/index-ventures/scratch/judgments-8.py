"""PRO-82 grind, batch-008 (alkemics .. conexant). Same evidence and conventions as batch-001. bioxell, cellzome and
comentis are life sciences desk rows. blaze and captions are name variants merged at the rebuild (into beryl and mirage)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl, verdict, arch = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl, gl.verdict, gl.arch
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("alkemics", status="acquired", country="FR", city="Paris", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014", rng="below_1b", focus="SaaS",
    note="Product-data collaboration platform between brands and retailers (Paris); Index led the 2014 Series A, Dominique Vidal on the board; the $22M Series B of September 2016 was led by Cathay Innovation and Serena with the existing investors (the firm's post); acq. by Salsify, 2021"))
L.append(C("amen", status="acquired", country="DE", city="Berlin", stage="Seed", stage_src="model", stage_conf="low", entry_date="2011-09", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["stage_uncited"], note="Opinion-sharing app (Berlin); the $1.9M seed of 2011 with Index, Sunstone and A-Grade (on the firm's 2012 list under its Early stage filter); acq. by tape.tv, 2013"))
u = post("ando-building-the-interface")
L.append(C("ando", dispute=("country",), status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2026-09", grad="censored", rng="below_1b",
    focus="SaaS", note="Team messaging for people and AI agents (San Francisco); 'we're very excited to be leading her Seed' (the firm's post, 2026-09-24; $20M with Emergence); inside the 24-month window; the pre-filled JP is a one-word name join",
    rounds=[rnd("2026-09-24", "Seed", 20000000, "Index Ventures", True, u, "firm")]))
u = nqurl('"Ankar" patent AI seed Index Ventures', "Ankar raises £3M Seed to protect intellectual property"); g = post("ankar-raises-20m-series-a")
L.append(C("ankar-ai", status="private", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2025-05", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=g, focus="AI & Applied AI",
    note="AI platform for patent drafting and prosecution (London); the GBP 3M seed of May 2025 led by Index (Tech.eu, 2025-05-28), then 'Ankar Raises $20M Series A' (the firm's post, 2025-12-17: 'This Series A brings Ankar's total funding to $24 million'): a named later round decides the row inside the clock's window",
    rounds=[rnd("2025-05-28", "Seed", None, "Index Ventures", True, u, "press"), rnd("2025-12-17", "Series A", 20000000, None, True, g, "firm")]))
L.append(C("anthropic", city="San Francisco", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2026", focus="AI & Applied AI", flags=["cite_pending"],
    note="Frontier AI models and the Claude assistant (San Francisco); newly on the firm's list in 2026 with Nina Achadjian, Martin Mignot and Vlad Loktev: a late-stage entry in the 2026 financings (the round is confirmed in the A/B pass); $965B at the May 2026 round",
    rounds=[]))
u = news("Arca", "Wilson Sonsini Advises Arca on $64 Million Series A")
L.append(C("arca", dispute=("status", "country"), status="private", country="US", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-07", rng="below_1b",
    focus="Fintech & Payments", flags=["city_unknown", "country_prior"],
    note="AI-native wealth management pairing clients with human advisors (arcawealth.com); out of stealth with a $64M Series A in July 2026 (Wilson Sonsini; the firm's post of 2026-06-25 by Jahanvi Sardana); its city is on no surface read and the US is inferred from the New York partner and US advisers; the pre-filled 'defunct' and MX are a one-word Wikidata join",
    rounds=[rnd("2026-07-08", "Series A", 64000000, None, True, u, "press")]))
L.append(C("arista-networks", city="Santa Clara", stage="undetermined", focus="Data Infrastructure",
    note="Cloud networking switches (Santa Clara; NYSE: ANET, IPO June 2014); on the firm's own list from 2014 as an exited investment with Mike Volpi as its partner; the company was financed by its founders and no source read names a round Index joined, so the round is not on record; the market cap is re-read in the A/B pass", rounds=[]))
L.append(C("armada-interactive", status="defunct", country="FI", city="Helsinki", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile strategy games studio (Helsinki); on the firm's 2018-2023 pages, Ben Holmes; Creandum seeded it and no source read names the round Index entered; bankrupt in September 2020 (GamesIndustry.biz)", rounds=[]))
u = post("arondite-raises-12m")
L.append(C("arondite", status="private", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2025-05", grad="censored", rng="below_1b",
    focus="AI & Applied AI", note="Software connecting autonomous defence systems to human operators (London); the $12M seed of May 2025 led by Index (the firm's post, 2025-05-01; Calibre Defence names the round); inside the 24-month window",
    rounds=[rnd("2025-05-01", "Seed", 12000000, "Index Ventures", True, u, "firm")]))
L.append(C("artimi", status="acquired", country="GB", city="Cambridge", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2005", rng="below_1b", focus="Industrial & Robotics",
    note="Ultra-wideband wireless chips (Cambridge, UK); the $14M Series A of 2005 with Accel, Index, Amadeus and Oak; merged into Staccato Communications in 2008 (the firm's list marks it exited)"))
L.append(verdict("asos", "not_member", "T3 (venture entry; Erik's post-IPO ruling of 2026-09-06): ASOS has been listed on AIM since October 2001, so the position the firm's 2010-2023 pages list (Dominique Vidal) can only have been bought in a public company; no venture round is named on any surface",
                 ec="site_listing", conf="medium", cite=arch("asos", "list_tag")))
L.append(C("assistly", status="acquired", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2010", rng="below_1b", focus="SaaS",
    note="Customer support SaaS for small businesses (San Francisco); Index backed the 2010 Series A with True Ventures, Bernard Dalle the partner; acq. by Salesforce, 2011 ($50M; the firm's own news item), becoming Desk.com"))
u = post("astelia-raises-35m")
L.append(C("astelia", status="private", country="IL", city="Tel Aviv", stage="Series A", **WV, stage_cite=u, entry_date="2026-02", rng="below_1b", focus="Security",
    note="Exposure management by reachability analysis (Tel Aviv); 'I first met Alon ... just after their Seed round and immediately knew ... we'd be backing him at Series A' (the firm's post by Juriaan Duizendstraal, 2026-02-24; $35M)",
    rounds=[rnd("2026-02-24", "Series A", 35000000, "Index Ventures", True, u, "firm")]))
u = narch("AstleyClarke.com secures")
L.append(C("astleyclarke", status="acquired", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2008-06", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online fine-jewellery retailer (Astley Clarke, London); 'AstleyClarke.com secures GBP 2.75 million in series A financing' from Index (the firm's own news item, 2008-06-30); now owned by Aeternum Holding (Retail Jeweller, 2024-08-28)",
    rounds=[rnd("2008-06-30", "Series A", None, "Index Ventures", True, u, "firm")]))
L.append(C("autobutler", status="acquired", country="DK", city="Copenhagen", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for car repair quotes (Copenhagen); 'This marks another investment for our firm in a Danish company' (the firm's post, 2014-07-15), with Creandum; the post names no round; acq. by PSA Group, 2016",
    rounds=[rnd("2014-07-15", "undisclosed", None, "Index Ventures", True, post("autobutler-and-the-six"), "firm")]))
L.append(C("b-hive", status="acquired", country="US", city="San Carlos", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006", rng="below_1b", focus="Data Infrastructure",
    note="Application performance management for virtual machines (B-hive Networks; San Carlos and Herzliya); Index backed the 2006 Series A, Bernard Dalle the partner; acq. by VMware, 2008 (the firm's own news item)"))
L.append(C("base", status="acquired", city="Mountain View", stage="Growth", stage_src="model", stage_conf="high", entry_date="2013", rng="below_1b", focus="SaaS",
    note="Sales CRM (Base, later Mountain View; founded in Krakow and Chicago); Index led the $15M Series B of 2013, Bernard Dalle on the board; acq. by Zendesk, 2018"))
L.append(C("be2", status="unknown", country="LU", city="Luxembourg", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2008", rng="below_1b",
    focus="Consumer & Marketplaces", flags=["stage_uncited"], extra={"entry_stage_confidence": "medium"},
    note="Online matchmaking service (be2 S.a r.l., Luxembourg; founded 2004); on the firm's 2008-2013 lists from the year its growth fund invested in an already large site; no source read establishes what became of the company after 2013"))
L.append(C("beamexpress", status="acquired", country="CH", city="Lausanne", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    note="Long-wavelength VCSEL lasers for optical networks (an EPFL spin-off, Lausanne); on the firm's 2008 list as a past investment tagged Neophotonics, which bought it; the round is not on record", rounds=[]))
L.append(C("beryl", status="private", country="GB", country_src="wikidata", city="London", stage="Seed", stage_src="model", stage_conf="low", entry_date="2014", rng="below_1b",
    focus="Consumer & Marketplaces", flags=["stage_uncited"], note="Bike lights and shared bike schemes, founded as Blaze (London; the firm's 2014-2016 pages carry it as Blaze: one company, merged at the rebuild); the 2014 seed with Index and the Branson family; a GBP 2M raise in February 2023 to open a factory in Poole"))
u = post("beside")
L.append(C("beside", dispute=("country",), status="private", country="FR", city="Paris", stage="Seed", **WV, stage_cite=u, entry_date="2025", grad="graduated", grad_src="first_party",
    grad_cite=u, rng="below_1b", focus="AI & Applied AI",
    note="AI receptionist and operating system for local businesses (Paris and San Francisco); 'Index was proud to lead Beside's seed round, and now we're thrilled to partner with Max and the team again as they emerge from stealth with $32 million in Series A funding' (the firm's post, 2025-11-11); the partner's personal pre-seed cheque is not the firm's entry (T2); the pre-filled JP is a one-word name join",
    rounds=[rnd("2025", "Seed", None, "Index Ventures", True, u, "firm"), rnd("2025-11-11", "Series A", 32000000, None, True, u, "firm")]))
u = narch("BestofMedia attracts")
L.append(C("bestofmedia-group", status="acquired", country="FR", city="Paris", stage="Growth", **WV, stage_cite=u, entry_date="2008-07", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Technology media network, publisher of Tom's Hardware (Paris); 'BestofMedia attracts EUR 22.5 million in Growth Funding from Index Ventures' (the firm's own news item, 2008-07-10); acq. by TechMediaNetwork (Purch), 2013",
    rounds=[rnd("2008-07-10", "Growth round", None, "Index Ventures", True, u, "firm")]))
L.append(C("betfair", status="acquired", country="GB", city="London", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2005", rng="below_1b", focus="Consumer & Marketplaces",
    note="Betting exchange (London; founded 2000); Index bought into the company in the mid-2000s when it was already large, a secondary-led position (Growth by the taxonomy), Neil and Danny Rimer the partners; LSE IPO in October 2010; merged with Paddy Power in 2016 (now Flutter)"))
L.append(C("boku", status="public", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2009-06", rng="below_1b", focus="Fintech & Payments",
    note="Mobile carrier billing and payments (San Francisco and London; AIM: BOKU, IPO November 2017); launched in June 2009 with a $13M Series A from Benchmark, Index and Khosla, Danny Rimer on the board; $25M Series C in January 2010 (the firm's own news item); the market cap is read in the A/B pass"))
L.append(C("brit-co", status="private", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Lifestyle media and e-learning for women (San Francisco); Index joined the $6.3M Series A of 2013 led by Oak (the firm's 2013 list, Early stage filter); $15M Series C in May 2017"))
L.append(C("build", status="private", country="GB", city="London", stage="Seed", stage_src="model", stage_conf="low", entry_date="2026-06", grad="censored", rng="below_1b", focus="AI & Applied AI",
    flags=["stage_uncited"], note="AI software for planning and delivering infrastructure projects (build.inc, London); 'Build Raises $8.5 Million From Index Ventures' (PropTech Connect and UKTN, 2026-06-30), its first announced round, Martin Mignot; inside the 24-month window",
    rounds=[rnd("2026-06-30", "Seed", 8500000, "Index Ventures", True, nqurl('"Build" infrastructure AI-native raises $8.5 million Index Ventures', "Build Raises $8.5 Million From Index Ventures"), "press")]))
L.append(C("call9", status="defunct", country="US", city="New York", stage="Series A", stage_src="model", stage_conf="high", entry_date="2017", rng="below_1b", focus="Healthcare & Bio",
    note="Emergency telemedicine for nursing homes (Brooklyn, New York); Index led the $24M Series A of 2017, Neil Rimer on the board; shut down in June 2019 (Fierce Healthcare)"))
u = news("Cambridge Satchel", "raises $21 million from Index Ventures")
L.append(C("cambridge-satchel", status="acquired", country="GB", city="Cambridge", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2014-01", rng="below_1b",
    focus="Consumer & Marketplaces", note="Leather satchel maker (Cambridge, UK); 'Cambridge Satchel Company raises $21 million from Index Ventures' (FashionNetwork, 2014-01-27), its first institutional round, Giuseppe Zocco on the board; now owned by Chargeurs",
    rounds=[rnd("2014-01-27", "Series A", 21000000, "Index Ventures", True, u, "press")]))
u = post("captain-train-joins-trainline")
L.append(C("captain-train", status="acquired", country="FR", city="Paris", stage="Seed", **WV, stage_cite=u, entry_date="2012-06", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online rail ticketing, founded as Capitaine Train (Paris); 'we decided to lead Captain Train's Seed round alongside CM-CIC in June 2012' (the firm's post, 2016-03-15), Martin Mignot and Neil Rimer; acq. by Trainline, 2016 (up to $189M)",
    rounds=[rnd("2012-06", "Seed", None, "Index Ventures", True, u, "firm")]))
L.append(C("cartesia", status="private", country="US", city="San Francisco", rng="below_1b", focus="AI & Applied AI",
    note="Real-time voice and multimodal AI models (San Francisco; Stanford AI Lab founders); '$22 million in new funding led by Index Ventures, bringing total capital raised to $27 million' (the firm's post, 2024-12-12), the round its list marks as backed at Seed; $64M Series A led by Kleiner Perkins in March 2025"))
L.append(C("centrify", status="acquired", city="Santa Clara", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2007", rng="below_1b", focus="Security",
    note="Identity and privileged-access management (Santa Clara; founded 2004); Index joined the later rounds from 2007, Mike Volpi the partner on the firm's pages; Thoma Bravo acquired a majority in 2018 (the firm's own news item)"))
L.append(C("certess", status="acquired", country="FR", city="Grenoble", stage="Series A", stage_src="model", stage_conf="low", entry_date="2005", rng="below_1b", focus="DevTools & APIs",
    note="Functional qualification software for chip design (Grenoble and Campbell, California); backed by Index and Sofinnova in the mid-2000s; acq. by SpringSoft, 2009 (the firm's own news item)"))
u = post("our-investment-in-chai")
L.append(C("chai-discovery", status="private", country="US", city="San Francisco", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-07", rng="1b_plus",
    **sv("chai-discovery", "bain-capital-ventures"), focus="Healthcare & Bio",
    note="AI foundation models for molecular design (San Francisco); 'Our Investment in Chai Discovery' (the firm's post, 2026-07-14), published with the $400M Series C at $3.8B (aligned to Bain Capital Ventures' cited mark), after a $70M Series A in August 2025 from others",
    rounds=[rnd("2026-07-14", "Series C", 400000000, None, True, u, "firm")]))
L.append(C("ciao", country="DE", city="Munich", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Consumer review and price-comparison site (Munich; founded 1999); an Index investment of the dot-com years, Giuseppe Zocco the partner on the firm's 2014 page; the round is not on record; acq. by Greenfield Online, 2005, then Microsoft, 2008 (the page tags it MSFT)", rounds=[]))
u = post("regtech-company-clausematch")
L.append(C("clausematch", status="acquired", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2018-04", rng="below_1b", focus="SaaS",
    note="Policy and compliance document management for banks (London); 'raises $5m in a Series A round led by Index Ventures' (the firm's post, 2018-04-23); acq. by Corlytics, 2023 (Finextra)",
    rounds=[rnd("2018-04-23", "Series A", 5000000, "Index Ventures", True, u, "firm")]))
u = narch("Cloud.com Launches")
L.append(C("cloud-com", status="acquired", country="US", city="Cupertino", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2010-05", rng="below_1b",
    focus="Data Infrastructure", note="Open-source cloud orchestration, CloudStack (Cupertino; founded as VMOps); Index led the $11M Series B announced at the rename (the firm's own news item, 2010-05-05) after Redpoint and Nexus had funded the Series A; acq. by Citrix, 2011",
    rounds=[rnd("2010-05-05", "Series B", 11000000, "Index Ventures", True, u, "firm")]))
u = post("announcing-our-50m-series-c-in-codesignal")
L.append(C("codesignal-inc", status="private", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2021-09", rng="below_1b", focus="SaaS",
    note="Technical skills assessment for hiring (San Francisco); 'We are thrilled to lead the $50M Series C funding round' (the firm's post by Nina Achadjian, 2021-09-16)",
    rounds=[rnd("2021-09-16", "Series C", 50000000, "Index Ventures", True, u, "firm")]))
L.append(C("commquest", status="acquired", country="US", city="Encinitas", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    note="Wireless chipsets (CommQuest Technologies, Encinitas, California); an Index investment of the 1990s, already 'Acquired by IBM' on the firm's 1999 portfolio page (IBM bought it in 1998); the round is not on record", rounds=[]))
u = post("conduct-a-world")
L.append(C("conduct", status="private", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2026-06", rng="below_1b", focus="AI & Applied AI",
    note="AI agents for modernising enterprise ERP systems (London); 'We're thrilled to be co-leading their $60 million Series A along with ICONIQ' (the firm's post, 2026-06-17); Creandum had led the seed",
    rounds=[rnd("2026-06-17", "Series A", 60000000, "Index Ventures, ICONIQ", True, u, "firm")]))
L.append(verdict("conexant", "not_member", "sale consideration and the same investment under the acquirer's name (decisions.md D6; COLLECTION.md s3 identity_conflated): the firm's position was Virata (Cambridge, UK; its own row, tagged Conexant on the firm's 2014 page), which merged into GlobespanVirata in 2001 and into Conexant in 2004; the 2008-2013 lists carry the acquirer's name and ticker",
                 ec="site_listing", conf="high", cite=arch("conexant", "list_tag")))
gl.write("batch-008", L)
