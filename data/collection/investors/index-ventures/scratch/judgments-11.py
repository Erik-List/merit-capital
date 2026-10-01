"""PRO-82 grind, batch-011 (last-fm .. ofoto). Same evidence and conventions as batch-001. levicept, linguaflex, medicentrix,
mind-nrg, molecular-partners, normoxys and oncoethix are life sciences desk rows (done). novocure waits for the pre-2008
archive pass (its desk). Name variants merged at the rebuild: lustre (into vetted), mashape (into kong), myoptique (into
glasses-direct). Label rows (stage left for the label pass): mind-candy, mobissimo, netvibes, nuvo."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl, verdict, arch = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl, gl.verdict, gl.arch
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

u = narch("LAST.FM Secures Series A")
L.append(C("last-fm", status="acquired", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2006-05", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Music recommendation and scrobbling service (London); 'LAST.FM Secures Series A Funding From Index Ventures' (the firm's own news item, 2006-05-08), Neil and Danny Rimer the partners; acq. by CBS, 2007 ($280M)",
    rounds=[rnd("2006-05-08", "Series A", None, "Index Ventures", True, u, "firm")]))
u = nqurl('"Linx Security" Series A', "Linx nets $27M Series A from Index, Cyberstarts")
L.append(C("linx-security", status="private", country="US", city="New York", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2024-07", rng="below_1b",
    focus="Security", note="Identity security and governance platform (New York, with R&D in Tel Aviv); 'emerges from stealth, announcing $33 million in funding led by Index Ventures and Cyberstarts' (the firm's post, 2024-07-22): a Cyberstarts seed and the $27M Series A that Index led (Calcalist); $50M Series B in 2026",
    rounds=[rnd("2024-07-22", "Series A", 27000000, "Index Ventures", True, u, "press")]))
L.append(C("liquido", status="private", country="US", city="Mountain View", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2023-05", rng="below_1b", focus="Fintech & Payments",
    note="Unified payments platform for Latin America (Mountain View, with teams in Mexico and Brazil); $26M announced in May 2023 (TechCrunch; citybiz), the Series A led by Index, Mark Fiorentino the partner"))
L.append(C("listen-com", status="acquired", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Online music subscription service, maker of Rhapsody (San Francisco); an Index investment of 1999-2000, Neil Rimer the partner; acq. by RealNetworks, 2003 (the firm's page tags it NASDAQ:RNWK); the round is not on record", rounds=[]))
u = post("see-hear-speak"); v = nqurl('"LiveKit" $1 billion valuation Series C', "LiveKit hits $1B valuation")
L.append(C("livekit", status="private", country="US", city="San Jose", stage="Growth", **WV, stage_cite=u, entry_date="2026-01", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=v,
    asof="2026-01-22", focus="AI & Applied AI", note="Open-source infrastructure for real-time voice and video AI applications (San Jose); 'I'm thrilled to lead LiveKit's Series C, to join the board' (the firm's post, 2026-01-22); $100M at a $1B valuation (TechCrunch)",
    rounds=[rnd("2026-01-22", "Series C", 100000000, "Index Ventures", True, u, "firm")]))
L.append(C("lovefilm", status="acquired", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2005", rng="below_1b", focus="Media, Gaming & Advertising",
    note="DVD rental by post and streaming (London); Index backed Video Island, one of the companies merged into Lovefilm, and stayed through the mergers, Danny Rimer on the board; acq. by Amazon, 2011 (aligned to Balderton's row)"))
L.append(C("loveshark", status="unknown", country="GB", city="London", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021", rng="below_1b", focus="Media, Gaming & Advertising",
    flags=["stage_uncited"], note="Social mobile games studio (London); on the firm's 2021-2022 pages, Danny Rimer and Sofia Dolfe the partners, a seed-stage entry; no later round and no outcome on any surface read"))
u = post("writing-friction-with-marker")
L.append(C("marker", dispute=("country",), status="private", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2026-07", grad="censored", rng="below_1b", focus="AI & Applied AI",
    flags=["country_prior"], note="AI-native word processor from a former DeepMind creative lead (marker.page); 'we couldn't be more excited to lead Marker's seed round' ($13M; the firm's post, 2026-07-09); inside the 24-month window; London is inferred from the founder's DeepMind base and uktech.news coverage; not YC's Marker; the pre-filled DE is a one-word name join",
    rounds=[rnd("2026-07-09", "Seed", 13000000, "Index Ventures", True, u, "firm")]))
L.append(C("marvel", status="private", country="GB", city="London", stage="Seed", stage_src="model", stage_conf="low", entry_date="2015", rng="below_1b", focus="DevTools & APIs",
    flags=["stage_uncited"], note="Design prototyping and handoff tool (Marvel App, London); Index came in at the seed stage and stayed in the GBP 4M Series A led by BGF Ventures in 2016; on the firm's 2018-2019 pages"))
L.append(C("mediasurface", status="acquired", country="GB", city="London", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Web content management software (London; AIM: MSR from 2004); an Index investment of the dot-com years, on its lists as a past investment; acq. by Alterian, 2008; the round is not on record", rounds=[]))
u = narch("MetaPack strengthens its board")
L.append(C("metapack", status="acquired", country="GB", city="London", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2013-11", rng="below_1b", focus="SaaS",
    note="Delivery management software for online retailers (London; founded 1999); 'MetaPack strengthens its board and accelerates growth following GBP 20m investment' (the firm's own news item, 2013-11-28), a growth-stage entry into a fourteen-year-old company, Dominique Vidal on the board; acq. by Stamps.com, 2018",
    rounds=[rnd("2013-11-28", "Growth round", None, "Index Ventures", True, u, "firm")]))
u = narch("Milestone Systems Receives $27 Million")
L.append(C("milestone", dispute=("status", "country"), status="acquired", country="DK", city="Copenhagen", stage="Growth", **WV, stage_cite=u, entry_date="2008-07", rng="below_1b", focus="SaaS",
    note="Open-platform video management software (Milestone Systems, Brondby near Copenhagen); 'Milestone Systems Receives $27 Million in Growth Stage Funding from Index' (the firm's own news item, 2008-07-10), Giuseppe Zocco on the board; acq. by Canon, 2014; the pre-filled 'defunct' and JP are a one-word name join",
    rounds=[rnd("2008-07-10", "Growth round", 27000000, "Index Ventures", True, u, "firm")]))
L.append(C("mind-candy", status="private", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Children's games and entertainment, maker of Moshi Monsters (London); on the firm's lists 2008-2014 under both its Seed and Early stage filters; $12M raised in April 2020 (Pulse 2.0)"))
u = news("Mindshapes", "Mindshapes receives $5 million in series A funding")
L.append(C("mindshapes", status="unknown", country="GB", city="London", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2011-11", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Educational games and apps for children (London); 'Mindshapes receives $5 million in series A funding' (Pocket Gamer.biz, 2011-11-01; GBP 3.1M per The Guardian), from Index and Richmond Park; on the firm's 2013 list; no outcome on any surface read",
    rounds=[rnd("2011-11-01", "Series A", 5000000, None, True, u, "press")]))
u = post("mirage-raises-60m")
L.append(C("mirage", dispute=("status", "rng", "usd"), status="private", country="US", city="New York", stage="Growth", **WV, stage_cite=u, entry_date="2024-07", rng="below_1b", focus="AI & Applied AI",
    note="AI video creation, maker of the Captions app (New York; the company was called Captions until 2025, one row after the rebuild); 'The Series C round led by Index Ventures brings the total capital raised by Mirage to $100 million and values the company at $500 million' (the firm's post, 2024-07-09); the pre-filled 'public' and $26M belong to a listed namesake",
    rounds=[rnd("2024-07-09", "Series C", 60000000, "Index Ventures", True, u, "firm")]))
u = news("Mirelo", "Berlin startup Mirelo raises $41m in seed funding")
L.append(C("mirelo", status="private", country="DE", city="Berlin", stage="Seed", **WV, stage_cite=u, entry_date="2025-12", grad="censored", rng="below_1b", focus="AI & Applied AI",
    note="AI models that generate synchronised sound for video (Berlin); 'Berlin startup Mirelo raises $41m in seed funding' (Music Business Worldwide, 2025-12-16), co-led by Index and a16z (the firm's post, 2025-12-15); inside the 24-month window",
    rounds=[rnd("2025-12-15", "Seed", 41000000, "Index Ventures, a16z", True, post("musicians-turned-ai-researchers"), "firm")]))
L.append(C("mobissimo", status="unknown", city="San Francisco", rng="below_1b", focus="Consumer & Marketplaces",
    note="Travel metasearch engine (San Francisco); on the firm's 2008-2013 lists under both its Seed and Early stage filters; no outcome on any surface read"))
L.append(C("moleskine", status="acquired", country="IT", city="Milan", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2011", rng="below_1b", focus="Consumer & Marketplaces",
    note="Notebooks and stationery brand (Milan); Index's growth fund bought a minority stake beside Syntegra Capital in 2011, Giuseppe Zocco on the board; Milan IPO in March 2013 (the firm's own news item); taken over by D'Ieteren in 2016-2017 (Financial Times)",
    extra={"status_citation": news("Moleskine", "Belgian auto group buys 41% stake in Moleskine")}))
u = nqurl('"Moment" fixed income Series B Index Ventures', "Moment raises $36m Series B")
L.append(C("moment", status="private", country="US", city="New York", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2025-07", rng="below_1b",
    focus="Fintech & Payments", note="Fixed-income trading and portfolio infrastructure for brokerages and wealth platforms (New York); 'Fixed income fintech Moment raises $36m Series B' (FinTech Futures, 2025-07-10), the round Index led, Jan Hammer the partner; a16z and Lightspeed had funded the earlier rounds",
    rounds=[rnd("2025-07-09", "Series B", 36000000, "Index Ventures", True, u, "press")]))
L.append(C("move-loot", status="defunct", country="US", city="San Francisco", stage="Seed", stage_src="model", stage_conf="low", entry_date="2014-06", rng="below_1b",
    focus="Consumer & Marketplaces", flags=["stage_uncited"], note="Online consignment marketplace for used furniture (San Francisco; YC S14); Index was in the $2.8M seed of June 2014 (StartUp Beat) and led the $9M Series A of February 2015, Danny Rimer the partner; closed in 2016 (aligned to First Round, GV and YC)"))
u = narch("Sun Microsystems Announces Agreement to Acquire MySQL")
L.append(C("mysql", status="acquired", country="SE", city="Uppsala", stage="Growth", stage_src="model", stage_conf="high", entry_date="2003-06", rng="below_1b", focus="Data Infrastructure",
    note="Open-source relational database (MySQL AB, Uppsala; US base in Cupertino); Index co-led the $19.5M Series B of June 2003 with Benchmark, Danny Rimer on the board; acq. by Sun Microsystems, 2008 ($1B; the firm's own news item)",
    extra={"status_citation": u}))
L.append(C("neovista", status="acquired", country="US", city="Cupertino", stage="undetermined", rng="below_1b", focus="Data Infrastructure",
    note="Data-mining software for retailers (NeoVista Software, Cupertino); on the firm's 2008 list as a past investment tagged Accrue, which bought it in 1999-2000; the round is not on record", rounds=[]))
u = narch("Richemont offers to acquire shares in Net-A-Porter")
L.append(C("net-a-porter", status="acquired", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online luxury fashion retailer (London; founded 2000); Danny Rimer the Index partner; the firm's holding dates from the mid-2000s and no source read names the round; 'Richemont offers to acquire shares in Net-A-Porter' (the firm's own news item, 2010-04-01)",
    rounds=[], extra={"status_citation": u}))
L.append(C("netlog", status="acquired", country="BE", city="Ghent", stage="Series A", stage_src="model", stage_conf="high", entry_date="2007", rng="below_1b", focus="Media, Gaming & Advertising",
    note="European youth social network (Ghent; later Massive Media, maker of Twoo); Index led the EUR 5M Series A of 2007 with Atomico, Ben Holmes on the board; acq. by Meetic, 2012 (the firm's page tags it)"))
L.append(C("netvibes", status="acquired", country="FR", city="Paris", rng="below_1b", focus="Consumer & Marketplaces",
    note="Personalised start pages and dashboards (Paris); on the firm's lists under both its Seed and Early stage filters, Neil Rimer the partner (2006 financings with Accel); acq. by Dassault Systemes, 2012"))
u = nqurl('"NewCore" identity seed Series A Index Ventures', "after closing $66M seed funding round")
L.append(C("newcore", status="private", country="IL", city="Tel Aviv", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-06", grad="censored", rng="below_1b",
    focus="Security", note="Identity platform for employees and AI agents (an Israeli company per Globes); 'NewCore launches ... after closing $66M seed funding round' (SiliconANGLE, 2026-06-15), with 'Rebuilding Identity for the Agentic Era: Our Investment in NewCore' the same day (the firm's post); inside the 24-month window",
    rounds=[rnd("2026-06-15", "Seed", 66000000, None, True, post("our-investment-in-newcore"), "firm")]))
L.append(C("nginx", status="acquired", country="US", city="San Francisco", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2013-10", rng="below_1b", focus="Data Infrastructure",
    note="Web server and application delivery software (San Francisco; founded in Moscow); Index joined the $10M Series B of October 2013 led by NEA and listed it in 2014; acq. by F5 Networks, 2019 ($670M)",
    extra={"status_citation": news("Nginx", "F5 Networks reports")}))
u = post("our-investment-in-nomos")
L.append(C("nomos", dispute=("country",), status="private", country="DE", city="Berlin", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2026-09", rng="below_1b",
    focus="Climate & Energy", note="Power supplier that connects household batteries, heat pumps and solar to the electricity market (Berlin); 'Building A New Energy Model For Europe: Our Investment In Nomos' (the firm's post, 2026-09-15), published with the EUR 20M round, its first large round after a 2024 pre-seed (EU-Startups: 'Berlin-based Nomos'); the pre-filled BR is a one-word name join",
    rounds=[rnd("2026-09-15", "Series A", None, None, True, u, "firm")]))
u = post("nourish-raises-35m")
L.append(C("nourish", status="private", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2024-03", rng="1b_plus", **sv("nourish", "atomico"), focus="Healthcare & Bio",
    note="Insurance-covered telehealth with registered dietitians (New York); 'With its $35 million in Series A funding led by Index Ventures' (the firm's post, 2024-03-27); $70M Series B in April 2025; $1.75B at the May 2026 round (aligned to Atomico's cited mark)",
    rounds=[rnd("2024-03-27", "Series A", 35000000, "Index Ventures", True, u, "firm"), rnd("2025-04-23", "Series B", 70000000, None, True, post("nourish-raises-70m"), "firm")]))
u = narch("NumberFour AG Announces")
L.append(C("numberfour", status="private", country="DE", city="Berlin", stage="Series A", **WV, stage_cite=u, entry_date="2013-06", rng="below_1b", focus="SaaS",
    note="Business platform for small merchants (Berlin; renamed enfore in 2017); 'NumberFour AG Announces $38M Series A Financing' (the firm's own news item, 2013-06-27), with Index among the investors",
    rounds=[rnd("2013-06-27", "Series A", 38000000, None, True, u, "firm")]))
L.append(C("numerical-technologies", status="acquired", country="US", city="San Jose", stage="undetermined", rng="below_1b", focus="DevTools & APIs",
    note="Sub-wavelength chip design and mask software (San Jose; NASDAQ IPO April 2000); an Index investment of the late 1990s on its lists as a past investment; acq. by Synopsys, 2003; the round is not on record", rounds=[]))
L.append(C("nuvo", status="private", country="US", city="New York", rng="below_1b", focus="Fintech & Payments",
    note="Credit and onboarding network for B2B trade (nuvo.com); marked 'backed at Seed' on the firm's list; $45M announced in April 2025 across its seed and the $34M Series A led by Sequoia and Spark (TechCrunch; the firm's post)"))
L.append(C("oanda", status="acquired", country="US", city="New York", stage="Growth", stage_src="model", stage_conf="high", entry_date="2007", rng="below_1b", focus="Fintech & Payments",
    note="Online foreign-exchange trading and currency data (founded in Toronto, headquartered in New York); Index joined the $100M round of 2007 with NEA, the company's first outside capital after eleven years, Danny Rimer and Jan Hammer the partners; acq. by CVC, 2018 (the firm's post), then by FTMO, 2025",
    extra={"status_citation": post("cvc-capital-partners-agrees-to-acquire")}))
L.append(C("ofoto", status="acquired", country="US", city="Emeryville", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online photo printing and sharing (Emeryville; the firm's page says Berkeley, where it began); an Index investment of 1999-2000, Neil Rimer the partner; acq. by Kodak, 2001; the round is not on record", rounds=[]))
gl.write("batch-011", L)
