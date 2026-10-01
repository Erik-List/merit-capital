"""PRO-82 grind, batch-012 (onefinestay .. spiko). Same evidence and conventions as batch-001. pangenetics,
parallele-bioscience, profibrix, sequenta-inc and sgx-pharma are life sciences desk rows (done). oxyplus-inc waits for the
pre-2008 archive pass. Name variants merged at the rebuild: photoways (into photobox), privacy-com (into lithic),
savingglobal (into raisin). quixotic is left open (no round, place or outcome on any surface read yet).
Label rows (stage left for the label pass): peopleperhour, rjdj."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl, verdict, arch = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl, gl.verdict, gl.arch
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

u = narch("onefinestay raises $12 million")
L.append(C("onefinestay", status="acquired", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2011", rng="below_1b", focus="Consumer & Marketplaces",
    note="Upscale home rentals with hotel service (London); 'onefinestay's Series A funding was led by leading venture capital firm Index Ventures' (the firm's own news item on the $12M Series B, 2012-06-19), Dominique Vidal on the board; acq. by AccorHotels, 2016 ($169M; The New York Times)",
    rounds=[rnd("2012-06-19", "Series B", 12000000, "Canaan Partners", True, u, "firm")], extra={"status_citation": news("onefinestay", "AccorHotels of France Buys Onefinestay")}))
L.append(C("openbuildings", status="unknown", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="low", entry_date="2011", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online community and catalogue of architecture (London; Bulgarian founders); Index and BlueRun funded a $2M round in 2011; on the firm's 2012-2013 lists under its Early stage filter; no outcome on any surface read"))
u = narch("OpTier Raises $63M")
L.append(C("optier", status="defunct", country="US", city="New York", stage="Growth", **WV, stage_cite=u, entry_date="2008-09", rng="below_1b", focus="Data Infrastructure",
    note="Business transaction management software (New York; R&D in Israel); 'an additional $47.5 million in funding from new investors Index Ventures and Morgan Stanley' in its fourth round (the firm's own news item, 2008-09-24); closed in 2014 (aligned to Lightspeed's row)",
    rounds=[rnd("2008-09-24", "Series D", 47500000, None, True, u, "firm")]))
u = news("Oratomic", "Oratomic Raises $300 Million Series A - The Quantum Insider")
L.append(C("oratomic", status="private", city="Pasadena", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-07", rng="below_1b", focus="Industrial & Robotics",
    flags=["needs_web_value"], note="Fault-tolerant neutral-atom quantum computers (Pasadena; Caltech founders); 'Oratomic Raises $300 Million Series A' (The Quantum Insider, 2026-07-07), Martin Mignot and Bastian Hasslinger the partners; no priced valuation is on a surface read yet (checked in the A/B pass)",
    rounds=[rnd("2026-07-07", "Series A", 300000000, None, True, u, "press")]))
u = post("osper-reinvents")
L.append(C("osper", status="unknown", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014-06", rng="below_1b", focus="Fintech & Payments",
    note="Prepaid debit card and banking app for children (London); 'has raised over $10million in pre-launch funding and is backed by Index Ventures' and Horizons (the firm's post, 2014-06-30), Robin Klein the partner; no outcome on any surface read",
    rounds=[rnd("2014-06-30", "undisclosed", 10000000, None, True, u, "firm")]))
u = narch("Panther Express closes")
L.append(C("panther-express", status="acquired", city="New York", stage="Growth", **WV, stage_cite=u, entry_date="2008-02", rng="below_1b", focus="Data Infrastructure",
    note="Content delivery network (New York); 'Panther Express closes $15.75M Series B funding led by Index Ventures' (the firm's own news item, 2008-02-27), after Greylock's Series A; acq. by CDNetworks, 2009",
    rounds=[rnd("2008-02-27", "Series B", 15750000, "Index Ventures", True, u, "firm")]))
u = post("parallel-raises-20m")
L.append(C("parallel", dispute=("country",), status="private", country="FR", city="Paris", stage="Series A", **WV, stage_cite=u, entry_date="2026-03", rng="below_1b", focus="Healthcare & Bio",
    note="AI agents that automate hospital administration (beparallel.com, Paris; legal entity Kiosk, Inc., whose Form D of March 2026 names Julia Andre: one row after the rebuild); 'Index Ventures is leading a $20M Series A' (the firm's post, 2026-03-19); not Parallel Web Systems; the pre-filled AU is a one-word name join",
    rounds=[rnd("2026-03-19", "Series A", 20000000, "Index Ventures", True, u, "firm")]))
u = post("parallels-100m-series-a"); v = news("Parallel Web Systems", "hits $2 billion valuation")
L.append(C("parallel-web-systems", status="private", country="US", city="Palo Alto", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024",
    grad="graduated", grad_src="first_party", grad_cite=u, rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=v, asof="2026-05-01", focus="AI & Applied AI",
    note="Web search and research APIs built for AI agents, founded by Parag Agrawal (Palo Alto); 'We couldn't be more excited to double down on Parallel with a $100 million Series A co-led with Kleiner Perkins' (the firm's post, 2025-11-12): the firm was already in from the seed, which its list marks, and the Series A is the graduation; $2B at the May 2026 Series B (Moneycontrol)",
    rounds=[rnd("2025-11-12", "Series A", 100000000, "Index Ventures, Kleiner Perkins", True, u, "firm")]))
u = narch("Pentaho Secures $23 Million")
L.append(C("pentaho", status="acquired", city="Orlando", stage="Series A", stage_src="model", stage_conf="high", entry_date="2005", rng="below_1b", focus="Data Infrastructure",
    note="Open-source business intelligence and data integration (Orlando); Index and NEA funded the 2005 Series A; 'existing investors Benchmark Capital, Index Ventures and DAG Ventures' in the $23M Series C (the firm's own news item, 2012-10-30); acq. by Hitachi Data Systems, 2015"))
L.append(C("peopleperhour", status="private", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Freelance services marketplace (London; founded 2007); on the firm's 2010-2013 lists under both its Seed and Early stage filters"))
L.append(C("peoplevox", status="acquired", country="GB", city="London", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Warehouse management software for e-commerce (London); on the firm's 2020-2023 pages, Dominique Vidal the partner; acq. by Descartes Systems, 2020; the round is not on record", rounds=[]))
u = post("exponent-private-equity")
L.append(C("photobox", dispute=("country",), status="acquired", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="low", entry_date="2001", rng="below_1b",
    focus="Consumer & Marketplaces", note="Online photo printing and personalised gifts (Photobox Group, London); the firm's position began in Photoways (Paris), which merged with PhotoBox in 2006 (its 2008-2012 lists carry Photoways: one row after the rebuild), Neil Rimer the partner; acq. by Exponent and Electra, 2015-2016 (the firm's post)",
    extra={"status_citation": u}))
L.append(C("physical-intelligence", status="private", country="US", city="San Francisco", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2025-11", rng="1b_plus",
    **sv("physical-intelligence", "general-catalyst"), focus="AI & Applied AI", flags=["needs_web_value"],
    note="General-purpose AI models for robots (San Francisco); Index joined the $600M round of November 2025 at $5.6B (Bloomberg; aligned to General Catalyst's cited mark), Nina Achadjian and Eryk Dobrushkin the partners; a $1B round at about $11B was reported in September 2026 (checked in the A/B pass)"))
L.append(C("playfish", dispute=("country",), country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2008", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social games on Facebook (London); Index and Accel funded the first round and the $17M round of October 2008 (GamesBeat), Ben Holmes on the board; 'Index and Accel Announce Exit of Playfish to Electronic Arts' (the firm's own news item, 2009-11-09)",
    extra={"status_citation": narch("Index and Accel Announce Exit of Playfish")}))
u = post("vente-privee-com-strengthens")
L.append(C("privalia", status="acquired", country="ES", city="Barcelona", stage="Growth", stage_src="model", stage_conf="high", entry_date="2010-10", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online flash sales of fashion brands (Barcelona); Index joined the EUR 70M round of October 2010 with General Atlantic, Giuseppe Zocco the partner; 'Vente-privee.com Strengthens Its Position in Europe by Buying Privalia' (the firm's post, 2016-04-14)",
    extra={"status_citation": u}))
u = post("property-partner-raises-5")
L.append(C("property-partner", status="acquired", country="GB", city="London", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2015-03", rng="below_1b",
    focus="Fintech & Payments", note="Crowdfunded residential property investment platform (London; now London House Exchange); 'The investment, led by Index Ventures' (GBP 5.2M; the firm's post, 2015-03-23), the round after the GBP 1.25M seed led by Octopus in 2014; acq. by Better, 2021 (Orrick)",
    rounds=[rnd("2015-03-23", "Series A", None, "Index Ventures", True, u, "firm")], extra={"status_citation": nqurl('"Property Partner" acquired Better', "Orrick Advises Property Partner on Acquisition by Better")}))
L.append(C("pulsic", status="unknown", country="GB", city="Bristol", stage="undetermined", rng="below_1b", focus="DevTools & APIs",
    note="Custom chip layout automation software (Bristol); on the firm's 2008-2013 lists under its Early stage filter; neither the round nor a later outcome is on any surface read", rounds=[]))
u = post("our-investment-in-quilter")
L.append(C("quilter", status="private", country="US", city="Los Angeles", stage="Growth", **WV, stage_cite=u, entry_date="2025-10", rng="below_1b", focus="AI & Applied AI",
    note="Physics-driven AI that automates circuit-board layout (Los Angeles); 'I'm thrilled to be leading Quilter's $25.5 million Series B and joining the board' (the firm's post, 2025-10-07)",
    rounds=[rnd("2025-10-07", "Series B", 25500000, "Index Ventures", True, u, "firm")]))
L.append(C("rad", status="unknown", country="FR", city="Paris", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online streetwear and fashion retailer (Rad, Paris); on the firm's 2014-2019 pages, Martin Mignot the partner; neither the round nor a later outcome is on any surface read", rounds=[]))
u = nqurl('"Revel" hardware test Series B Index', "Revel Raises $150M Series B")
L.append(C("revel", status="private", country="US", city="Los Angeles", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-02", rng="below_1b",
    focus="DevTools & APIs", flags=["needs_web_value"], note="Software platform for hardware test and control (Los Angeles); 'We couldn't be more excited to partner with Scott and to welcome him and the Revel team to Index' (the firm's post, 2026-02-26), the day of the $150M Series B (Business Wire); a $1B+ valuation is carried only by an aggregator headline so far (Rule A: checked in the A/B pass)",
    rounds=[rnd("2026-02-26", "Series B", 150000000, None, True, post("great-hardware-deserves"), "firm")]))
L.append(C("rightscale", status="acquired", country="US", city="Santa Barbara", stage="Growth", stage_src="model", stage_conf="high", entry_date="2008-12", rng="below_1b", focus="Data Infrastructure",
    note="Cloud management platform (Santa Barbara); Index led the $13M Series B of December 2008 after Benchmark's Series A, Danny Rimer on the board; acq. by Flexera, 2018"))
L.append(C("rjdj", status="unknown", country="GB", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Reactive music apps (Reality Jockey, London); on the firm's 2012-2013 lists under its Seed stage filter; no outcome on any surface read"))
u = post("ryft-raises")
L.append(C("ryft", status="private", country="IL", city="Tel Aviv", stage="Seed", **WV, stage_cite=u, entry_date="2025-07", grad="censored", rng="below_1b", focus="Data Infrastructure",
    note="Automated management of Apache Iceberg data lakes (Tel Aviv); 'Ryft has raised $8 million in seed funding led by Index Ventures and joined by Bessemer Venture Partners' (the firm's post, 2025-07-09); inside the 24-month window; not the UK payments company of the same name",
    rounds=[rnd("2025-07-09", "Seed", 8000000, "Index Ventures", True, u, "firm")]))
L.append(C("scm-microsystems", country="US", city="Santa Ana", stage="undetermined", focus="Security",
    note="Smart-card readers and secure access hardware (SCM Microsystems, founded 1990 in Germany and California; NASDAQ IPO 1997; now Identiv, NASDAQ: INVE, the listed company the pre-fill reads); an Index investment of the 1990s, on its lists as a past investment; the round is not on record", rounds=[]))
u = post("building-the-first-intelligence-layer")
L.append(C("scope", dispute=("country",), status="private", country="GB", city="London", stage="undetermined", rng="below_1b", focus="AI & Applied AI",
    flags=["country_prior"], note="AI for industrial inspection and asset-integrity workflows (getscope.ai; 'UK AI startup Scope' per EU-Startups); 'convinced us to partner with them and lead this $20M funding round' (the firm's post, 2026-05-19), which names no round; not YC's Scope; the pre-filled DK is a one-word name join",
    rounds=[rnd("2026-05-19", "undisclosed", 20000000, "Index Ventures", True, u, "firm")]))
L.append(C("scratch", status="private", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Loan servicing platform for borrowers and lenders (Scratch Services, San Francisco); on the firm's 2020 page, Mark Goldberg the partner; which round the firm joined is not on any surface read", rounds=[]))
L.append(C("securewave", status="acquired", country="LU", city="Luxembourg", stage="undetermined", rng="below_1b", focus="Security",
    note="Endpoint application and device control software (SecureWave S.A., Luxembourg); on the firm's 2008 list tagged Lumension, formed when PatchLink bought it in 2007; the round is not on record", rounds=[]))
u = post("leading-similes-series-a")
L.append(C("simile", city="Palo Alto", stage="Series A", **WV, stage_cite=u, entry_date="2026-02", focus="AI & Applied AI",
    note="Simulations of human behaviour with generative agents (Palo Alto; Stanford founders); 'we're thrilled to lead Simile's $100 million Series A' (the firm's post, 2026-02-12), then 'double down' in the $200M Series B at $2B (2026-07-30)",
    rounds=[rnd("2026-02-12", "Series A", 100000000, "Index Ventures", True, u, "firm"), rnd("2026-07-30", "Series B", 200000000, None, True, post("similes-200m-series-b"), "firm")]))
u = narch("SKYPE Closes")
L.append(C("skype", status="acquired", country="LU", city="Luxembourg", stage="Growth", **WV, stage_cite=u, entry_date="2004-03", rng="below_1b", focus="Consumer & Marketplaces",
    note="Internet voice and video calling (Skype Technologies S.A., Luxembourg; built in Tallinn); 'it has closed its second round of funding. The investment round was led by the venture capital firms, Draper Fisher Jurvetson and Index Ventures' ($18.8M; the firm's own news item 'SKYPE Closes B Round', 2004-03-15), Danny Rimer on the board; acq. by eBay, 2005, and by Microsoft, 2011",
    rounds=[rnd("2004-03-15", "Series B", 18800000, "Draper Fisher Jurvetson, Index Ventures", True, u, "firm")], extra={"status_citation": narch("eBay to Acquire Skype")}))
u = post("slack-raises-160m")
L.append(C("slack", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2015-04", rng="below_1b", focus="SaaS",
    note="Team messaging (San Francisco); 'New investors include Horizons Ventures, Digital Sky Technologies (DST Global), Index Ventures, Spark Capital Growth, and Institutional Venture Partners' in the $160M round at $2.8B (the firm's post, 2015-04-16), Mike Volpi the partner; NYSE listing June 2019; acq. by Salesforce, 2021",
    rounds=[rnd("2015-04-16", "Series E", 160000000, None, True, u, "firm")]))
u = narch("Socialbakers, Global Leaders")
L.append(C("socialbakers", status="acquired", country="CZ", city="Prague", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2012-11", rng="below_1b",
    focus="SaaS", note="Social media analytics for brands (Prague; now part of Emplifi); 'The current round was led by Index Ventures, with additional follow-on funding from first-round investor Earlybird' ($6M; the firm's own news item, 2012-11-19): the company's second round, Jan Hammer on the board; acq. by Astute, 2020",
    rounds=[rnd("2012-11-19", "Series B", 6000000, "Index Ventures", True, u, "firm")]))
L.append(C("sofar", dispute=("country",), status="private", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Intimate live-music events in unusual venues (Sofar Sounds, London); on the firm's 2018-2019 pages; which round the firm joined is not on any surface read; $25M raised in 2019 from Battery and Union Square Ventures; the pre-filled IT is a one-word name join", rounds=[]))
L.append(C("soundcloud", status="private", country="DE", city="Berlin", stage="Growth", stage_src="model", stage_conf="high", entry_date="2011-01", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Audio streaming and sharing platform (Berlin); Index and Union Square Ventures led the $10M Series B of January 2011, Mike Volpi on the board"))
L.append(C("sourcelabs", status="acquired", country="US", city="Seattle", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2004", rng="below_1b", focus="DevTools & APIs",
    note="Support and certified stacks for open-source enterprise software (Seattle); Index and Ignition funded the 2004 Series A; acq. by EMC, 2009 (the firm's list tags it)"))
u = post("spiko-raises-22m")
L.append(C("spiko", status="private", country="FR", city="Paris", stage="Series A", **WV, stage_cite=u, entry_date="2025-07", rng="below_1b", focus="Fintech & Payments",
    note="Tokenised money-market funds for corporate cash management (Paris); 'The Series A funding will accelerate Spiko's go-to-market strategy' ($22M led by Index; the firm's post, 2025-07-17)",
    rounds=[rnd("2025-07-17", "Series A", 22000000, "Index Ventures", True, u, "firm")]))
gl.write("batch-012", L)
