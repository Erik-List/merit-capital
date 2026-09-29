"""PRO-105 grind, batch-003 (outfittery .. wallapop). Evidence as in batches 1-2. Graduation in its own
pass, except rows the clock censors."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, post, art, sib, page, news, wp = jl.cls, jl.rnd, jl.post, jl.art, jl.sib, jl.page, jl.news, jl.wp
L = []
def pc(slug):
    return dict(country_src="web_verified", country_cite=page(slug))
def fp(slug, key, sub, stage, date, rw=None, **kw):
    u = post(key, sub)
    kw.setdefault("rounds", [rnd(date, rw or stage, None, None, True, u, "firm")])
    return cls(slug, stage=stage, stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date=date, **kw)
def wv(slug, url, stage, date, rw=None, conf="high", **kw):
    kw.setdefault("rounds", [rnd(date, rw or stage, None, None, True, url, "press")])
    return cls(slug, stage=stage, stage_src="web_verified", stage_conf=conf, stage_cite=url, entry_date=date, **kw)
def und(slug, note, **kw):
    kw.setdefault("rng", "below_1b")
    return cls(slug, stage="undetermined", note=note, **kw)
WIKI_TP = "https://en.wikipedia.org/wiki/Trustpilot"

L.append(und("outfittery", "Online personal styling for men (Berlin); Northzone put $20M into the company in March 2015 (the firm's post 'Outfittery receives 20 million dollars from Northzone'), round not named",
    status="private", **pc("outfittery"), city="Berlin", focus="Consumer & Marketplaces"))
L.append(und("predoc", "AI-native medical record retrieval; the firm lists Partnered 2023 and Wendy Xiao; a $30M raise in Sept 2025 (Fortune) is later than the entry, whose round is not named; the city is not given on the surfaces read",
    status="private", **pc("predoc"), focus="Healthcare & Bio", flags=["city_unknown"]))
L.append(und("pricerunner", "Price comparison (Stockholm); the firm lists Partnered 2003, round not named; acq. by ValueClick, 2004 (ValueClick 10-K of 2005), later owned by Klarna (2022)",
    **pc("pricerunner"), city="Stockholm", focus="Consumer & Marketplaces"))
L.append(und("qt", "Trolltech, the company behind the Qt framework (Oslo, founded 1994); the firm lists Partnered 2000 and marks it IPO (Oslo Børs, 2006), round not named; Trolltech was acq. by Nokia, 2008 (Qt later passed to Digia and today's listed Qt Group, a different entity from the one Northzone held)",
    status="acquired", **pc("qt"), city="Oslo", focus="DevTools & APIs"))
L.append(fp("ravio", "ravio", "our investment", "Seed", "2022-04", status="private", **pc("ravio"), city="London", rng="below_1b", focus="SaaS",
    note="Compensation benchmarking (London); Northzone led the $10M seed with Cherry and Spark (the firm's post, 2022-04-27); $12M Series A May 2025 (Business Wire)"))
L.append(fp("rayon", "rayon", "our investment", "Seed", "2023-09", status="private", **pc("rayon"), city="Paris", rng="below_1b", focus="SaaS",
    note="Collaborative floor-plan design (Paris); Northzone co-led the EUR 4M seed with Foundamental (the firm's post, 2023-09-27); EUR 10M Series A in Sept 2026 (tech.eu)"))
L.append(cls("recall-labs", status="private", **pc("recall-labs"), stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite=art("3box", "seed"), entry_date="2019-06", rng="below_1b", focus="Crypto & Web3", flags=["city_unknown"],
    note="Decentralised identity and data network; the company the firm backed as 3Box Labs (the firm's press post 'Web3 platform 3Box raises seed', 2019-06-26; the archived 3box pages merge at the rebuild), today Recall Labs; USV's row holds the same company at its Series A; the city is not given on the surfaces read",
    rounds=[rnd("2019-06-26", "Seed", None, None, True, art("3box", "seed"), "press")]))
L.append(fp("red-points", "red points", "leads", "Growth", "2018-01", rw="Series B", status="private", **pc("red-points"), city="Barcelona",
    rng="below_1b", focus="Security", note="Anti-counterfeiting and piracy protection for brands (Barcelona); Northzone led the $12M Series B with Mangrove and Sabadell (the firm's post, 2018-01-09), its first investment"))
L.append(fp("reonic", "reonic", "our investment", "Series A", "2024-09", status="private", **pc("reonic"), city="Berlin", rng="below_1b",
    focus="Climate & Energy", note="Software for renewable-energy installers (Berlin); Northzone led the EUR 13M Series A with Point Nine and Puzzle (the firm's post, 2024-09-05; Osborne Clarke deal note)"))
L.append(fp("riff", "riff", "our investment", "Series A", "2025-10", status="private", **pc("riff"), city="Oslo", rng="below_1b",
    focus="AI & Applied AI", note="Enterprise AI app building (Oslo); Northzone led the $16M Series A (the firm's post, 2025-10-23; tech.eu; techfundingnews 'Oslo's Riff')"))
L.append(und("safello", "Bitcoin exchange (Stockholm); the firm lists Partnered 2014, round not named; listed on Nasdaq First North (Safello Group), small cap; Wikidata SE confirmed",
    status="public", city="Stockholm", focus="Crypto & Web3"))
L.append(und("salesape", "AI sales agent for SMBs (London); the firm lists Partnered 2024, no press names the round (Google News 2026-09-29)",
    status="private", **pc("salesape"), city="London", focus="AI & Applied AI"))
L.append(wv("seamflow", news("Seamflow", "Tech.eu"), "Seed", "2026-02", conf="medium", status="private", **pc("seamflow"), city="London",
    grad="censored", rng="below_1b", focus="AI & Applied AI",
    note="AI software for testing, inspection and certification (London); the $4.5M seed of Feb 2026 (tech.eu; FinSMEs), the round of the firm's Partnered 2025 (close year)"))
L.append(und("sellersfi", "Revenue-based financing for e-commerce sellers (Weston, FL), formerly SellersFunding; Northzone led the $166.5M round of Sept 2021 (the firm's press post; Form Ds 2021 and 2025 with Jeppe Zink as director), a mix of equity and debt facility whose equity round is not named",
    status="private", **pc("sellersfi"), city="Weston", focus="Fintech & Payments",
    rounds=[rnd("2021-09-15", "undisclosed (equity and debt)", 166500000, "Northzone", True, art("sellersfunding", "166"), "press")]))
L.append(fp("seriously", "seriously", "raises", "Series A", "2015-08", status="acquired", city="Helsinki", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Mobile games (Best Fiends; Helsinki and Venice, CA); Northzone led the $18M Series A (the firm's post, 2015-08-04); acq. by Playtika, 2019; Wikidata FI confirmed"))
L.append(und("solveai", "Enterprise apps from natural language (London, founded 2025); the firm lists Partnered 2025; the GBP 33m ($50M) Series A of Feb 2026 was led by GV (UKTN; GV's row), and the earlier round Northzone entered is not named",
    status="private", **pc("solveai"), city="London", focus="AI & Applied AI"))
L.append(fp("solvimon", "solvimon", "our investment", "Seed", "2023-11", status="private", **pc("solvimon"), city="Amsterdam", rng="below_1b",
    focus="Fintech & Payments", note="Billing and pricing infrastructure (Amsterdam); Northzone led the EUR 9M seed (the firm's post, 2023-11-13; Business Insider)"))
L.append(fp("sona", "sona", "our investment in sona", "Series A", "2024-05", status="private", country="GB", country_src="web_verified",
    country_cite=page("sona"), city="London", rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="Workforce management for frontline staff (London); 'we're taking part in their $27.5m Series A, alongside Felicis' (the firm's post, 2024-05-14; UKTN: led by Felicis); $45M Series B 2026; the pre-filled acquired / IT is a one-word Wikidata join, disputed"))
L.append(und("soundtrack-your-brand", "B2B music streaming, Spotify's joint venture (Stockholm); the firm lists Partnered 2013, the year of the company's first round, not named; Creandum's and Balderton's rows enter the same company",
    status="private", **pc("soundtrack-your-brand"), city="Stockholm", focus="Media, Gaming & Advertising"))
L.append(fp("sourcepoint", "sourcepoint", "leads", "Growth", "2017-01", rw="Series B", status="private", **pc("sourcepoint"), city="New York",
    rng="below_1b", focus="Media, Gaming & Advertising", note="Privacy compliance and content compensation for publishers (New York); Northzone led the $16M Series B, Pär-Jörgen Pärson joining the board (the firm's post, 2017-01-25), its first investment; Spark's row enters at the $10M Series A of 2015"))
L.append(und("soveren", "Sensitive-data discovery and security (London); the firm lists Partnered 2021, round not named; acq. by SecureSky, Sept 2026 (Pulse 2.0, 2026-09-20)",
    status="acquired", **pc("soveren"), city="London", focus="Security"))
L.append(cls("spaceape", status="acquired", **pc("spaceape"), city="London", stage="Series A", stage_src="model", stage_conf="medium",
    entry_date="2013", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile games (London); 'Jeppe Zink, who led Northzone's investment in the company since its initial round in 2013' (the firm's post on Supercell's 62%, 2017-05-23); the 2013 round is the one Accel's row cites as the Series A; Supercell took full control later"))
L.append(fp("spacemaker", "spacemaker", "welcome", "Series A", "2019-06", status="acquired", **pc("spacemaker"), city="Oslo", rng="below_1b",
    focus="AI & Applied AI", note="AI for urban development (Oslo); Northzone invested in the $25M Series A with Atomico (the firm's post, 2019-06-10); acq. by Autodesk for $240M, 2020"))
L.append(fp("spektr", "spektr", "our investment", "Seed", "2024-02", status="private", **pc("spektr"), city="Copenhagen", rng="below_1b",
    focus="Fintech & Payments", note="KYC workflow automation (Copenhagen); Northzone led the EUR 5M seed with Seedcamp and PreSeed Ventures (the firm's post, 2024-02-21); $20M Series A April 2026 (Business Wire)"))
L.append(cls("spotify", country="SE", country_src="web_verified", country_cite=sib("spotify", "creandum", "val_cite") and page("spotify"),
    city="Stockholm", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=post("spotify", "impossible success"),
    entry_date="2008", status="public", rng="100b_plus", usd=int(float(sib("spotify", "tiger-global-management", "usd"))),
    val_src="web_verified", val_cite=sib("spotify", "tiger-global-management", "val_cite"), asof=sib("spotify", "tiger-global-management", "asof"),
    focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="Music and audio streaming (Stockholm; the firm lists the US office); Pär-Jörgen Pärson 'leading the first financing round in 2008 ... the A-round' (the firm's post 'Spotify - The Impossible Success Story', 2018-03-15), co-led with Creandum; NYSE since April 2018; market cap aligned to Tiger's freshest cited figure; the pre-filled 'acquired' (a Wikidata parent join) is disputed",
    rounds=[rnd("2008", "Series A", None, "Northzone, Creandum", True, post("spotify", "impossible success"), "firm")]))
L.append(cls("spring-health", status="private", city="New York", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=post("announcing-our-22m-series-a", ""), entry_date="2020-01",
    rng="1b_plus", usd=int(float(sib("spring-health", "tiger-global-management", "usd"))), val_src="web_verified",
    val_cite=sib("spring-health", "tiger-global-management", "val_cite"), asof=sib("spring-health", "tiger-global-management", "asof"),
    focus="Healthcare & Bio", flags=["stale"],
    note="Precision mental health benefits (New York); the $22M Series A of Jan 2020 (the company's announcement, republished on the firm's site 2020-01-27; the firm lists Partnered 2020, Pär-Jörgen Pärson and Wendy Xiao); $3.3B in the $100M Series E of July 2024 (aligned to the siblings' cited mark), stale beyond 24 months",
    rounds=[rnd("2020-01-27", "Series A", 22000000, None, True, post("announcing-our-22m-series-a", ""), "firm")]))
L.append(und("stepstone", "Online job boards (founded in Oslo 1996); the firm lists Partnered 1997, round not named; StepStone ASA listed on Oslo Børs 2000 and was acq. by Axel Springer, 2009 (later HQ Düsseldorf)",
    status="acquired", **pc("stepstone"), city="Oslo", focus="Consumer & Marketplaces"))
L.append(wv("stockeld-dreamery", "https://www.eu-startups.com/2020/01/stockholm-based-noquo-foods-raises-e3-25-million-to-reinvent-vegan-cheese/",
    "Seed", "2020-01", status="acquired", **pc("stockeld-dreamery"), city="Stockholm", rng="below_1b", focus="Consumer & Marketplaces",
    note="Plant-based cheese (Stockholm), Noquo Foods until 2021; the EUR 3.25M seed with Northzone and Creandum (EU-Startups, 2020-01); $20M Series A Sept 2021 (AgFunderNews); acq. by Bettani Farms, Dec 2025 (Green Queen), after the business had stalled; Creandum's row reads defunct (aligned at the ingest)"))
L.append(fp("stonly", "stonly", "our investment", "Series A", "2022-01", status="private", **pc("stonly"), city="Paris", rng="below_1b",
    focus="SaaS", note="Interactive customer-support guides (Paris); Northzone led the $22M Series A with Accel (the firm's post, 2022-01-27); Accel led the EUR 3.2M seed of 2020"))
L.append(fp("stream", "stream", "building a consumer champion", "Series A", "2019-05", country="GB", country_src="web_verified",
    country_cite=page("stream"), city="London", rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Earned-wage access and workplace finance (London), Wagestream until 2025; Northzone co-led the GBP 15m Series A with Balderton (the firm's post, 2019-05-20; TechRound); the pre-filled defunct / IT is a one-word Wikidata join and is disputed; not Felicis's, YC's or Battery's Stream",
    rounds=[rnd("2019-05-20", "Series A", None, "co-led: Northzone, Balderton", True, post("stream", "building a consumer champion"), "firm")]))
L.append(und("sunscreen", "Privacy engineering tools (sunscreen.tech); the firm lists Partnered 2022 and Wendy Xiao, round not named; the city is not given on the surfaces read",
    status="private", **pc("sunscreen"), focus="Security", flags=["city_unknown"]))
L.append(und("supponor", "Digital billboard replacement for live sports broadcasts (founded in Finland; the firm lists the UK); the firm lists Partnered 2008 and marks it Acquired, round and acquirer not named on the surfaces read",
    status="acquired", **pc("supponor"), city="London", focus="Media, Gaming & Advertising"))
L.append(und("tana", "Notes-to-actions workspace (Oslo); the firm lists Partnered 2021 and Jeppe Zink, round not named; Lightspeed's row enters a later round",
    status="private", **pc("tana"), city="Oslo", focus="SaaS"))
L.append(fp("tandem-health", "tandem health", "our investment", "Seed", "2024-06", status="private", **pc("tandem-health"), city="Stockholm",
    rng="below_1b", focus="Healthcare & Bio", note="AI clinical scribe (Stockholm); Northzone led the $9.5M seed with Amino Collective (the firm's post, 2024-06-19); $50M Series A July 2025 (tech.eu), $100M Series B Sept 2026 led by EQT's Scaleup Europe fund"))
L.append(wv("thirty-madison", art("thirty madison", "series a"), "Series A", "2018-10", status="acquired", **pc("thirty-madison"), city="New York",
    rng="below_1b", focus="Healthcare & Bio",
    note="Consumer healthcare brands (Keeps; New York); the $15.25M Series A of Oct 2018 (Business Wire, linked from the firm's post 'Our investment in Thirty Madison', Paul Murphy); valued above $1B in the $140M Series C of June 2021; acq. by Remedy Meds, Sept 2025 ($500M deal, MobiHealthNews); First Round's row enters the same company"))
L.append(cls("tier", status="private", city="Berlin", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2018",
    rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Shared e-scooters (Berlin); the firm lists Partnered 2018, the year of Tier's Series A after Point Nine's seed; Tier merged with Dott in 2024 and the combined company operates as Dott (the firm's page links ridedott.com and marks it Acquired): the business continues in the merged private company, aligned with Point Nine's private; the pre-filled 'acquired 2012' is a one-word Wikidata join, disputed"))
L.append(und("tobii", "Eye-tracking technology (Stockholm, founded 2001); the firm lists Partnered 2009, round not named; Nasdaq Stockholm since 2015, small cap",
    status="public", **pc("tobii"), city="Stockholm", focus="Industrial & Robotics"))
L.append(fp("topline-pro", "topline pro", "our investment", "Growth", "2025-08", rw="Series B", status="private", **pc("topline-pro"), city="New York",
    rng="below_1b", focus="AI & Applied AI", note="Done-for-you marketing for home-service SMBs (New York, YC); Northzone led the $27M Series B (the firm's post, 2025-08-14), its first investment"))
L.append(fp("troop", "troop", "our investment", "Seed", "2022-11", status="private", **pc("troop"), city="New York", rng="below_1b",
    focus="Fintech & Payments", note="Collective shareholder activism for everyday investors (founded in Brooklyn); Northzone co-led the $4.3M seed with BlockTower and Seedcamp (the firm's post, 2022-11-02)"))
L.append(fp("truelayer", "truelayer", "our investment in truelayer", "Series A", "2018-07", city="London", clear=[],
    rng="below_1b", usd=None, focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Open-banking payments network (London); the firm's post 'Our investment in TrueLayer' (2018-07-19) announces its first investment, the company's Series A after Connect Ventures' 2017 seed; the 2021 $1B unicorn mark is superseded by the 2024 down round (aligned to Tiger's cited reading below $1B)",
    extra={"valuation_range_source": "web_verified", "valuation_citation": sib("truelayer", "tiger-global-management", "val_cite")}))
L.append(cls("trustpilot", status="public", city="Copenhagen", stage="Series A", stage_src="web_verified", stage_conf="medium",
    stage_cite=WIKI_TP, entry_date="2011-11", rng="1b_plus", usd=1055329604, val_src="web_verified",
    val_cite="https://stockanalysis.com/quote/lon/TRST/market-cap/", asof="2026-09-29", focus="Consumer & Marketplaces",
    note="Consumer review platform (founded in Copenhagen; LSE-listed, London HQ since the 2021 IPO); Northzone's first money was the 'initial capital injection from SEED Capital Denmark and Northzone in November 2011', the round before the $13M Series B of 2012 (Wikipedia, Trustpilot): the Series A by the record's own sequence; market cap GBP 796.7M @ ECB 2026-09-29 (GBP/EUR 0.85718, EUR/USD 1.1355) = $1.06B (StockAnalysis), within 6% of the $1B edge",
    rounds=[rnd("2011-11", "initial capital injection (before the B)", None, None, True, WIKI_TP, "press"),
            rnd("2012", "Series B", 13000000, None, True, WIKI_TP, "press")]))
L.append(und("tuza", "Card-payment provider comparison for SMBs (London); the firm lists Partnered 2023; a GBP 4M seed of May 2024 (FinSMEs) is later than the firm's year, and Northzone's round is not named",
    status="private", **pc("tuza"), city="London", focus="Fintech & Payments"))
L.append(fp("unobravo", "unobravo", "growth investment", "Growth", "2023-12", status="private", **pc("unobravo"), city="Naples",
    rng="below_1b", focus="Healthcare & Bio", note="Online psychotherapy (Naples); Northzone co-led the growth round with Insight Partners and H14 (the firm's post, 2023-12-13; Startupbusiness: CDP VC out, Northzone and H14 in), its first investment"))
L.append(cls("videoplaza", status="acquired", country="SE", country_src="model_knowledge", city="Stockholm", stage="Series A", stage_src="model",
    stage_conf="medium", entry_date="2010", rng="below_1b", focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="Video ad serving (founded in Stockholm; London office); the EUR 5M round of 2010 led by Creandum and Northzone, the round after Creandum's 2008 seed (Creandum's row and posts; 'Videoplaza secures five million in funding', the firm's archived post 2010-03-18): the Series A by sequence; acq. by Ooyala, Oct 2014"))
L.append(und("wallapop", "Second-hand marketplace (Barcelona); the firm lists Partnered 2015, round not named (Wikipedia: investors include Mangrove, Northzone and Eight Roads); Naver took 100% in Aug 2025 at a EUR 600M valuation (bebeez), so acquired; Accel's row still reads private (aligned at the ingest); Wikidata ES confirmed",
    status="acquired", city="Barcelona", focus="Consumer & Marketplaces"))

jl.write("batch-003", L)
