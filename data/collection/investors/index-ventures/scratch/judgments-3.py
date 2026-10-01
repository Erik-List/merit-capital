"""PRO-82 grind, batch-003 (deepscribe .. humu). Same evidence and conventions as batch-001. egalet is a life
sciences desk row (judgments-life.py); dot-product is left open for the hard-rows pass."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("deepscribe", status="private", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2022-01", rng="below_1b",
    focus="Healthcare & Bio", note="AI medical scribe (San Francisco); Index led the $30M Series A of January 2022, Nina Achadjian (Voicebot.ai, 2022-01-13); a $5.2M seed in May 2021 from others",
    rounds=[rnd("2021-05-14", "Seed", 5200000, None, False, None, "press"), rnd("2022-01-13", "Series A", 30000000, "Index Ventures", True, news("DeepScribe", "Medical AI Transcription Startup DeepScribe Raises"), "press")]))
u = post("deliveroo-raises-2-75m")
L.append(C("deliveroo", status="acquired", country="GB", country_src="wikidata", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2014-06", rng="below_1b",
    focus="Consumer & Marketplaces", note="Restaurant food delivery (London; LSE: ROO, IPO March 2021); 'a GBP 2.75m Series A funding round, led by Index Ventures' (the firm's post, 2014-06-26), then the $25M Series B it led in January 2015; acq. by DoorDash, 2025 (about GBP 2.9B). The firm's list marks it 'backed at Seed'; its own announcement names the round a Series A (D8 score)",
    rounds=[rnd("2014-06-26", "Series A", None, "Index Ventures", True, u, "firm"), rnd("2015-01-29", "Series B", 25000000, "Index Ventures", True, post("deliveroo-raises-25m"), "firm")]))
u = news("/dev/agents", "commanded a massive $56M seed round")
L.append(C("dev-agents", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2024-11", grad="censored", rng="below_1b",
    focus="AI & Applied AI", note="Operating system for AI agents (San Francisco; founded by David Singleton, Hugo Barra and other Google and Stripe veterans); the $56M seed co-led by Index and CapitalG at a $500M valuation (TechCrunch, 2024-11-28; the firm's post of 2024-11-26); inside the 24-month window",
    rounds=[rnd("2024-11-26", "Seed", 56000000, "Index Ventures, CapitalG", True, u, "press")]))
L.append(C("discord", city="San Francisco", focus="Consumer & Marketplaces",
    note="Voice, video and text communities (San Francisco); Index entered in the 2018 growth rounds and led the $100M round of June 2020 at $3.5B (Danny Rimer's post, 2020-06-30); $15B at the September 2021 round"))
L.append(C("double", status="private", country="US", city="New York", rng="below_1b", focus="SaaS",
    note="Remote executive assistants with delegation software (withdouble.com, New York; founded 2018 by French founders); Index led the $6M seed of 2019, Nina Achadjian ('Supercharging Humans', the firm's post of 2019-09-10); the firm's list marks it backed at Seed; the Double of the General Catalyst and YC books is another company"))
u = post("draftwise-raises-20m")
L.append(C("draftwise", status="private", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2024-03", rng="below_1b", focus="AI & Applied AI",
    note="AI contract drafting and negotiation for law firms (New York); '$20 million in Series A financing led by Index Ventures' (the firm's post, 2024-03-14)",
    rounds=[rnd("2024-03-14", "Series A", 20000000, "Index Ventures", True, u, "firm")]))
u = post("dream-games-entertaining-the-world"); v = news("Dream Games", "valued at $5 billion in landmark exit")
L.append(C("dream-games", dispute=("usd",), city="Istanbul", stage="Series A", **WV, stage_cite=u, entry_date="2021-03", usd=5000000000, val_src="web_verified", val_cite=v,
    asof="2025-05-02", rng="1b_plus", focus="Media, Gaming & Advertising",
    note="Mobile puzzle games (Royal Match; Istanbul); 'leading the pre-launch Series A investment in Dream Games in March 2021' (the firm's post, 2022-01-18; $50M); $2.75B at the January 2022 Series C; the May 2025 CVC-led financing that bought out early backers valued it at $5B (MENAbytes, 2025-05-02), the company staying independent under its founders; Balderton's row reads acquired",
    rounds=[rnd("2021-03-01", "Series A", 50000000, "Index Ventures", True, u, "firm")]))
u = news("Dubsmash", "raises $5.5 million from Index")
L.append(C("dubsmash", dispute=("stage",), status="acquired", city="New York", rng="below_1b", stage="Series A", **WV, stage_cite=u, entry_date="2015-08", focus="Media, Gaming & Advertising",
    note="Short-form lip-sync video app (founded in Berlin, later Brooklyn); the $5.5M Series A of August 2015 led by Index (Tech.eu, 2015-08-31), Danny Rimer on the board; the Form D band read a 2019 filing; acq. by Reddit, 2020",
    rounds=[rnd("2015-08-31", "Series A", 5500000, "Index Ventures", True, u, "press")]))
L.append(C("duffel", status="private", country="GB", city="London", rng="below_1b", focus="DevTools & APIs",
    note="Flight-booking API for travel sellers (London); a 2018 seed with Blossom and Index, a $21.5M Series A led by Benchmark in June 2019 and a $30M Series B led by Index in October 2019 (the firm's posts); the firm's list marks it backed at Seed"))
L.append(C("elementl", status="private", country="US", city="San Francisco", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2021-11", rng="below_1b",
    focus="Data Infrastructure", note="Maker of the Dagster data orchestrator, now Dagster Labs (San Francisco); Index (Mike Volpi) co-led the $14M Series A announced November 2021 with Sequoia and Amplify; $33M Series B led by Georgian in May 2023"))
u = post("empathy-raises-47m")
L.append(C("empathy", dispute=("country",), status="private", country="US", city="New York", stage="Growth", **WV, stage_cite=u, entry_date="2024-03", rng="below_1b", focus="SaaS",
    note="Bereavement and estate-settlement support sold through insurers and employers (New York and Tel Aviv); Index led the $47M Series B (the firm's post, 2024-03-12), then joined the $72M Series C of May 2025; the pre-filled JP is a one-word name join",
    rounds=[rnd("2024-03-12", "Series B", 47000000, "Index Ventures", True, u, "firm")]))
L.append(C("etsy", dispute=("usd",), country="US", city="New York", stage="Growth", stage_src="model", stage_conf="high", entry_date="2008-01", **sv("etsy", "tiger-global-management"), rng="1b_plus",
    focus="Consumer & Marketplaces", flags=["cite_pending"],
    note="Marketplace for handmade and vintage goods (Brooklyn, New York; Nasdaq: ETSY, IPO April 2015); Index and Accel led the $27M Series D of January 2008, Danny Rimer on the board; the Index funds filed a 13G at the IPO; market cap aligned to Tiger Global's cited figure, the pre-filled float is stale"))
L.append(C("evervault", status="private", city="Dublin", rng="below_1b", focus="Security",
    note="Encryption infrastructure for developers (Dublin); 'Round led by Index Ventures and joined by existing partners Sequoia, Kleiner Perkins and Frontline' (the firm's post on the $16M Series A, 2020-05-21); $25M Series B in March 2026"))
v = news("Expel", "is now a unicorn")
L.append(C("expel", status="private", city="Herndon", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=v, asof="2021-11-22", focus="Security", flags=["stale"],
    note="Managed detection and response (Herndon, Virginia); Index led the $40M Series C of June 2019 (the firm's post), Shardul Shah on the board; the $140M Series E of November 2021 valued it at over $1B (Technical.ly, 2021-11-22), stale beyond 24 months; the Battery and NEA rows read below $1B"))
L.append(C("factual", status="acquired", city="Los Angeles", stage="Series A", stage_src="model", stage_conf="high", entry_date="2010-12", rng="below_1b", focus="Data Infrastructure",
    note="Location data platform (Los Angeles); the $25M Series A of December 2010 led by Andreessen Horowitz and Index (Form D first sale 2010-12-06, Danny Rimer as director); merged into Foursquare in 2020"))
L.append(C("farfetch", status="acquired", country="GB", country_src="wikidata", city="London", stage="Growth", stage_src="model", stage_conf="high", entry_date="2012-01", rng="below_1b",
    focus="Consumer & Marketplaces", note="Luxury fashion marketplace (London; founded in Portugal; NYSE: FTCH, IPO September 2018); Index led the $18M Series B of January 2012, Danny Rimer on the board; the firm's own news item of 2013-03-04 is the $20M Series C; the funds filed 13Gs after the IPO; acq. by Coupang, 2024 (out of a pre-pack administration)",
    rounds=[rnd("2012-01", "Series B", 18000000, "Index Ventures", True, None, "press"), rnd("2013-03-04", "Series C", 20000000, "Conde Nast", True, narch("Farfetch raises $20m"), "firm")]))
L.append(C("feathery", status="private", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Form and workflow builder for financial-services onboarding (San Francisco); on the firm's list since 2024 with no partner named; a Series A in July 2026 brought the total to $30M (FinSMEs); no source read names the round Index entered", rounds=[]))
u = post("figma-setting-the-new-standard")
L.append(C("figma", dispute=("stage", "usd", "rng"), city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2013-12", grad="graduated", grad_src="first_party", grad_cite=u,
    rng="10b_plus", **sv("figma", "coatue"), focus="SaaS",
    note="Collaborative interface design (San Francisco; NYSE: FIG, IPO July 2025); 'This follows our initial investment in Figma in December 2013', the $3.8M seed Index led (Form D 2013, $4.0M), in the firm's post on the $40M Series C of February 2019; Danny Rimer on the board; the band read the 2019 filing; market cap aligned to Coatue's cited figure",
    rounds=[rnd("2013-12", "Seed", 3800000, "Index Ventures", True, u, "firm"), rnd("2015-12", "Series A", 14000000, "Greylock", True, None, "filing"), rnd("2019-02-14", "Series C", 40000000, "Sequoia", True, u, "firm")]))
L.append(C("fireblocks", dispute=("country",), status="private", country="US", city="New York", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2022-01",
    rng="1b_plus", **sv("fireblocks", "coatue"), focus="Crypto & Web3", flags=["stale", "cite_pending"],
    note="Digital-asset custody and transfer infrastructure (New York; engineering in Tel Aviv); Index joined the $550M Series E of January 2022 at $8B (aligned to Coatue's cited mark), Shardul Shah the partner; stale beyond 24 months; the pre-filled IL is the founders' base"))
L.append(C("flagship", dispute=("status", "country"), status="private", country="US", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces", flags=["city_unknown"],
    note="Storefronts for creators to sell brands' products (flagship.shop); a $2M seed in September 2023 and $6M in April 2025; shut its marketplace in July 2025 and pivoted to a creator search engine (ADWEEK, 2025-07-11); on the firm's list since 2025 with no partner named; the pre-filled 'defunct' and JP are a one-word Wikidata join; its city is not on any surface read", rounds=[]))
u = news("flatfair", "raises $11M led by Index Ventures")
L.append(C("flatfair", status="private", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2019-08", rng="below_1b", focus="Fintech & Payments",
    note="Deposit-free renting (London); 'raises $11M led by Index Ventures' (TechCrunch, 2019-08-14), the Series A, Hannah Seal and Martin Mignot",
    rounds=[rnd("2019-08-14", "Series A", 11000000, "Index Ventures", True, u, "press")]))
u = narch("Flipboard launches world")
L.append(C("flipboard", status="private", country="US", city="Palo Alto", stage="Series A", **WV, stage_cite=u, entry_date="2010-07", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social magazine app (Palo Alto); 'raised $10.5 million in a Series A venture capital round' at launch, from Kleiner Perkins and Index (the firm's own news item, 2010-07-21), Danny Rimer on the board; $50M in 2013; last priced at about $800M in 2015",
    rounds=[rnd("2010-07-21", "Series A", 10500000, "Kleiner Perkins, Index Ventures", True, u, "firm")]))
L.append(C("fomo", dispute=("status",), status="private", city="New York", rng="below_1b", focus="Crypto & Web3",
    note="Consumer on-chain trading app (New York); 'We're thrilled to lead fomo's $75 million Series B' (the firm's post, 2026-06-22) at a $550M valuation (Fortune), Julia Andre on the board; the pre-filled 'acquired' is a one-word name join"))
u = post("fonoa-raises-60m")
L.append(C("fonoa", status="private", country="IE", city="Dublin", stage="Seed", **WV, stage_cite=u, entry_date="2020-12", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="Fintech & Payments",
    note="Tax automation APIs for internet businesses (Dublin; Croatian founders); 'Since the company's Index-led seed round at the end of 2020 ... raised $20.5m Series A funding at the start of this year' (the firm's post on the $60M Series B, 2022-07-21); $110M Series C in June 2026",
    rounds=[rnd("2020-12", "Seed", None, "Index Ventures", True, u, "firm"), rnd("2021-11-22", "Series A", 20500000, None, True, post("fonoa-raises-25-million"), "firm")]))
L.append(C("foodily", status="acquired", city="San Mateo", rng="below_1b", focus="Consumer & Marketplaces",
    note="Recipe search engine (San Mateo); Index led the 2010 Series A, Mike Volpi on the board (Form Ds 2010 and 2013); acq. by IAC (Ask.com), 2015"))
u = post("footprint-emerges-from-stealth"); g = news("Footprint", "bags $25m Series B")
L.append(C("footprint", status="private", country="US", city="New York", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2022-08", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="Fintech & Payments",
    note="Identity verification and compliance onboarding (onefootprint.com, New York); the $6M seed at launch, 'led by Index Ventures with participation from a group of angel investors and seed funds' (the firm's post, 2022-08-03); Series A led by QED in 2024, $25M Series B in September 2026 (FinTech Futures)",
    rounds=[rnd("2022-08-03", "Seed", 6000000, "Index Ventures", True, u, "firm"), rnd("2026-09-24", "Series B", 25000000, None, None, g, "press")]))
u = news("Funding Circle", "raises £2.5 million")
L.append(C("funding-circle", dispute=("country",), status="public", country="GB", city="London", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2011-04",
    rng="below_1b", **sv("funding-circle", "ribbit-capital"), focus="Fintech & Payments",
    note="Small-business lending platform (London; LSE: FCH, IPO September 2018); Index led the GBP 2.5M Series A of April 2011 (Finextra, 2011-04-21), Neil Rimer on the board; market cap aligned to Ribbit's cited figure; the pre-filled US is the American subsidiary's filing address",
    rounds=[rnd("2011-04-21", "Series A", None, "Index Ventures", True, u, "press")]))
L.append(C("fuze", status="acquired", city="Boston", rng="below_1b", focus="SaaS",
    note="Video conferencing as FuzeBox (San Francisco), in which Index led the $20M Series A of 2012 (the firm's own news item); merged into ThinkingPhones of Boston in 2015, which took the Fuze name; acq. by 8x8, 2022"))
u = post("building-a-better-metaverse")
L.append(C("gather", dispute=("country",), status="private", country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2021-11", rng="below_1b", focus="SaaS",
    note="Virtual spaces for remote teams (gather.town, San Francisco); 'co-leading Gather's $50 million Series B with Sequoia' (the firm's post, 2021-11-03); the pre-filled JP is a one-word name join",
    rounds=[rnd("2021-11-03", "Series B", 50000000, "Index Ventures, Sequoia", True, u, "firm")]))
L.append(C("gatsby", dispute=("stage",), status="acquired", city="San Francisco", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-05",
    focus="DevTools & APIs", note="Open-source framework for fast websites (San Francisco area); Index led the $28M Series B of May 2020, Shardul Shah joining the board (the three Form Ds refiled in 2020 name him on every earlier round, which the band read as a 2018 seed entry; the firm's post of 2020-05-27); acq. by Netlify, 2023"))
L.append(C("glossier", status="private", country="US", city="New York", stage="Growth", stage_src="model", stage_conf="high", entry_date="2016-11", rng="below_1b",
    focus="Consumer & Marketplaces", note="Direct-to-consumer beauty brand (New York); Index entered in the $24M Series B of November 2016 and led the $52M Series C of February 2018 (the firm's post); last priced at $1.8B in July 2021, more than 24 months stale; the IVP, Sequoia and Spark rows read below $1B and this row follows them (rule 10)",
    rounds=[rnd("2016-11", "Series B", 24000000, "IVP", True, post("how-glossier-raised"), "firm"), rnd("2018-02-22", "Series C", 52000000, "Index Ventures, IVP", True, post("glossier-inc-raises-52-million"), "firm")]))
L.append(C("goat", status="private", city="Culver City", rng="1b_plus", **sv("goat", "a16z"), focus="Consumer & Marketplaces", flags=["stale"],
    note="Sneaker and apparel resale marketplace (GOAT Group, legal name 1661, Inc.; Culver City); Index led the $60M Series C of February 2018 at the Flight Club merger, Danny Rimer on the board; $3.7B at the June 2021 Series F (aligned to a16z's cited mark), stale"))
u = post("finally-voice-ai-tech-work")
L.append(C("gong", dispute=("country",), country="US", city="San Francisco", stage="Growth", **WV, stage_cite=u, entry_date="2020-08", focus="SaaS",
    note="Revenue intelligence from recorded sales calls (San Francisco; founded in Israel); 'I'm incredibly excited to announce our investment in Gong!' (the firm's post by Nina Achadjian, 2020-08-12, on the $200M Series D led by Coatue at $2.2B); the pre-filled country is a broken Wikidata string",
    rounds=[rnd("2020-08-12", "Series D", 200000000, "Coatue", True, u, "firm")]))
u = post("good-eggs-and-the-importance")
L.append(C("good-eggs", dispute=("stage",), status="acquired", city="Oakland", rng="below_1b", stage="Growth", **WV, stage_cite=u, entry_date="2014-09", focus="Consumer & Marketplaces",
    note="Online grocer for local produce (San Francisco, later Oakland); 'When Index first invested in Good Eggs in 2014' (Danny Rimer's post, 2018-05-15), the $21M Series B Index led in September 2014; the band read the 2016 filing; acq. by GrubMarket, 2024",
    rounds=[rnd("2014-09-08", "Series B", 21000000, "Index Ventures", True, u, "firm")]))
L.append(C("goody", status="private", country="US", city="Miami", rng="below_1b", focus="Consumer & Marketplaces",
    note="Gifting by text message, for consumers and businesses (Miami); a seed with Index in 2020-21 and a $15M Series A led by SoftBank in November 2021 (Refresh Miami); the firm's list marks it backed at Seed, Damir Becirovic the partner"))
u = post("grailed-raises-15-million")
L.append(C("grailed", status="acquired", country="US", city="New York", stage="Series A", **WV, stage_cite=u, entry_date="2018-06", rng="below_1b", focus="Consumer & Marketplaces",
    note="Menswear resale marketplace (New York); Index led the $15M Series A (the firm's post, 2018-06-21), Danny Rimer; acq. by GOAT Group, 2022",
    rounds=[rnd("2018-06-21", "Series A", 15000000, "Index Ventures", True, u, "firm")]))
u = post("shining-a-light-into-the-living-world")
L.append(C("greg", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2021-05", rng="below_1b", focus="Consumer & Marketplaces",
    note="Plant-care app (Gregarious, Inc., San Francisco); 'their seed financing, a $5m round led by Index Ventures with participation from First Round Capital' (the firm's post, 2021-05-27)",
    rounds=[rnd("2021-05-27", "Seed", 5000000, "Index Ventures", True, u, "firm")]))
u = post("gremlin-announces-failure")
L.append(C("gremlin", status="private", country="US", city="San Jose", stage="Series A", **WV, stage_cite=u, entry_date="2017-12", rng="below_1b", focus="DevTools & APIs",
    note="Chaos engineering platform (San Jose); 'announcing Series A funding from Index Ventures and Amplify Partners' (the firm's post, 2017-12-12; $7.5M), Mike Volpi; $18M Series B led by Redpoint in 2018",
    rounds=[rnd("2017-12-12", "Series A", 7500000, "Index Ventures", True, u, "firm")]))
u = post("hebbia-empowering-the-knowledge-worker"); g = news("Hebbia", "raises nearly $100M Series B")
L.append(C("hebbia", status="private", country="US", city="New York", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2020", rng="below_1b",
    grad="graduated", grad_src="first_party", grad_cite=u, focus="AI & Applied AI",
    note="AI research and document analysis for finance and law (New York); 'We were lucky enough to meet George and his team early in their journey and invest in the seed round ... we're leading the $30M Series A round in Hebbia' (the firm's post by Mike Volpi, 2022-09-07); $130M Series B led by Andreessen Horowitz in 2024 at about $700M",
    rounds=[rnd("2020", "Seed", None, None, True, u, "firm"), rnd("2022-09-07", "Series A", 30000000, "Index Ventures", True, u, "firm"), rnd("2024-07-09", "Series B", 130000000, "Andreessen Horowitz", True, g, "press")]))
L.append(C("hollar", status="defunct", city="Commerce", rng="below_1b", grad="graduated", grad_src="formd", focus="Consumer & Marketplaces",
    note="Online dollar store (Los Angeles area); Index joined the $5.5M seed of July 2015 led by Lightspeed, Danny Rimer on the board (Form Ds 2015-2017: $12M Series A in late 2015, $30M Series B in 2016); the store closed and Five Below bought its e-commerce technology in 2020"))
L.append(C("hortonworks", city="Santa Clara", stage="Growth", stage_src="model", stage_conf="high", entry_date="2011-11", rng="below_1b", focus="Data Infrastructure",
    note="Enterprise Hadoop distribution (Santa Clara; Nasdaq: HDP, IPO December 2014); Index led the $25M Series B of November 2011, Mike Volpi on the board; the Index funds filed 13Gs after the IPO; merged with Cloudera in January 2019",
    rounds=[rnd("2011-11", "Series B", 25000000, "Index Ventures", True, None, "press")]))
L.append(C("humanloop", status="defunct", country="GB", city="London", rng="below_1b", focus="AI & Applied AI",
    note="Prompt management and evaluation tools for LLM applications (London; a University College London spin-out); seed with Index in 2020-21; Anthropic hired the team in August 2025 without buying the company (Silicon Republic, 2025-08-14) and the product was shut down that September (COLLECTION.md s6: an acqui-hire does not decide the status); the YC row reads acquired"))
L.append(C("humu", status="acquired", city="Mountain View", rng="below_1b", focus="SaaS",
    note="Behavioural 'nudge' software for HR, founded by Google's former people chief Laszlo Bock (Mountain View); Index led the 2018 Series A and B, Danny Rimer on the board (the firm's post, 2018-05-01); acq. by Perceptyx, 2023"))
gl.write("batch-003", L)
