"""PRO-105 grind, batch-002 (fyndiq .. openzeppelin). Evidence as in batch 1: the firm's company page and
posts, siblings, Google News headlines (decoded on citation), article texts read with read-articles.py.
Graduation in its own pass, except rows the clock censors."""
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
TC_INFOGRID = "https://techcrunch.com/2020/11/30/infogrid-raises-15-5m-from-northzone-to-retrofit-buildings-with-smart-iot/"
TC_LABSTER = "https://techcrunch.com/2017/09/06/virtual-science-lab-startup-labster-bags-10m/"
BI_HOMA = "https://markets.businessinsider.com/news/stocks/homa-games-gaming-startup-raises-50-million-from-northzone-2021-10"

L.append(fp("fyndiq", "fyndiq", "raises", "Series A", "2014-11", status="private", city="Stockholm", rng="below_1b",
    focus="Consumer & Marketplaces", note="Online bargain marketplace (Stockholm); Northzone led the $20M Series A with Industrifonden (the firm's post, 2014-11-07); Wikidata SE confirmed"))
L.append(fp("gc-ai", "gc ai", "our investment", "Growth", "2025-11", rw="Series B", status="private", city="San Francisco",
    usd=555000000, val_src="web_verified", val_cite=news("GC AI", "Artificial Lawyer"), asof="2025-11-12", rng="below_1b",
    focus="AI & Applied AI", note="AI for in-house legal teams; Northzone co-led the $60M Series B with Scale Venture Partners (the firm's post, 2025-11-12), its first investment; valued at $555M (Artificial Lawyer, 2025-11-12)"))
L.append(cls("genesis-ai", status="private", **pc("genesis-ai"), city="Palo Alto", stage="Seed", stage_src="model", stage_conf="medium",
    entry_date="2025-07", grad="censored", rng="below_1b", focus="AI & Applied AI",
    note="Foundation models for robots; emerged in July 2025 with a $105M seed from Eclipse and Khosla (TechCrunch, 2025-07-01), the only round it raised in the year the firm lists as Partnered 2025, so the entry is the seed; talks in July 2026 about $500M at $3B (Dealroom) are a reported deal, not a mark",
    rounds=[rnd("2025-07-01", "Seed", 105000000, "Eclipse, Khosla", None, news("Genesis AI", "launches with $105M"), "press")]))
L.append(fp("goals", "goals", "our investment", "Seed", "2022-04", status="private", city="Stockholm", **pc("goals"), rng="below_1b",
    focus="Media, Gaming & Advertising", note="Free-to-play football game (Stockholm); Northzone led the $15M seed (the firm's post, 2022-04-05); a $20M Series A in April 2023 with Seven Seven Six, Northzone, Moonfire and Cassius (Wikipedia, Andreas Thorstensson)"))
L.append(fp("govdash", "govdash", "our investment", "Series A", "2024-04", status="private", **pc("govdash"), city="New York", rng="below_1b",
    focus="AI & Applied AI", note="AI for government contractors (New York, YC); Northzone led the $10M Series A (the firm's post, 2024-04-16); $30M Series B Jan 2026 (Pulse 2.0)"))
L.append(fp("happyornot", "happyornot", "leads", "Series A", "2017-10", status="acquired", city="Tampere", rng="below_1b", focus="SaaS",
    note="Smiley-terminal satisfaction feedback (Tampere); Northzone led the $14.5M Series A (the firm's post, 2017-10-12); Verdane took a majority stake in August 2026 (FE International deal note; the firm's shareholders sold alongside), so the row reads acquired; Wikidata FI confirmed"))
L.append(cls("heltia", status="private", **pc("heltia"), city="Istanbul", stage="undetermined", rng="below_1b", focus="Healthcare & Bio",
    note="Preventive health management (Istanbul); the firm lists Partnered 2023 and Michiel Kotting; no press names the round (Google News 2026-09-29)"))
L.append(wv("hidden-door", news("Hidden Door", "pre-seed"), "Pre-Seed", "2022-03", status="private", **pc("hidden-door"), city="New York",
    rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social AI narrative game platform (New York); Northzone led the $2M pre-seed with Makers Fund, Betaworks and Brooklyn Bridge Ventures (GamesIndustry.biz, 2022-03-17); the firm lists Partnered 2021, the close year"))
L.append(cls("holidu", status="private", **pc("holidu"), city="Munich", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2022",
    rng="below_1b", focus="Consumer & Marketplaces",
    note="Vacation-rental search and host software (Munich); the firm lists Partnered 2022 and marks the company Growth, after the EUR 5M Series A of 2016 and the extended Series C of 2020 (UKTN): any 2022 entry is a growth round"))
L.append(wv("homa-games", BI_HOMA, "Series A", "2021-10", status="private", **pc("homa-games"), city="Paris", rng="below_1b",
    focus="Media, Gaming & Advertising",
    note="Mobile game publishing platform (Paris); Northzone led the $50M Series A, seven months after the $15M seed (Business Insider, 2021-10-11); $100M more in Oct 2022 led by Quadrille and Headline at an undisclosed valuation (TechCrunch, tech.eu): the firm's Unicorn tag has no citable priced figure behind it, so the band is below $1B (Rule A)",
    rounds=[rnd("2021-10-11", "Series A", 50000000, "Northzone", True, BI_HOMA, "press"),
            rnd("2022-10-11", "Series B", 100000000, "Quadrille Capital, Headline", True, "https://tech.eu/2022/10/12/homa-hauls-in-100-million-in-quadrille-capital-and-headline-led-round/", "press")]))
L.append(cls("hopin", status="acquired", **pc("hopin"), city="London", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2020-02",
    rng="below_1b", focus="SaaS",
    note="Virtual events platform (London); the firm lists Partnered 2020 and Pär-Jörgen Pärson; its first institutional round was the $6.5M seed of Feb 2020 that Northzone led (PhocusWire 2020-02-21), then the $40M Series A of June 2020; the businesses were sold (events to RingCentral 2023, StreamYard to Bending Spoons 2024), aligned with the siblings' acquired",
    rounds=[rnd("2020-02-21", "Seed", 6500000, "Northzone", True, news("Hopin", "phocuswire"), "press")]))
L.append(cls("iconic", status="private", **pc("iconic"), city="London", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2025-12",
    grad="censored", rng="below_1b", focus="Media, Gaming & Advertising",
    note="On-device AI for voice-driven games (London); the $13M seed of Dec 2025 (tech.eu; EU-Startups) is the round of the year the firm lists as Partnered 2025, so the entry",
    rounds=[rnd("2025-12-15", "Seed", 13000000, None, None, news("Iconic", "raises $13M seed"), "press")]))
L.append(fp("idoven", "idoven", "our investment in idoven", "Series A", "2022-06", status="private", **pc("idoven"), city="Madrid", rng="below_1b",
    focus="Healthcare & Bio", note="AI cardiology service (Madrid); Northzone co-led the $19.8M Series A with Insight Partners (the firm's post, 2022-06-21)"))
L.append(cls("jasper", status="acquired", **pc("jasper"), city="Mountain View", stage="undetermined", rng="below_1b", focus="DevTools & APIs",
    note="Jasper Design Automation, formal verification software for chip design (Mountain View, founded 1999); the firm lists Partnered 2003, round not named; acq. by Cadence for $170M, 2014 (the firm's posts 2014-04-21/22); not Jasper AI (Coatue, IVP, Insight) nor Jasper Wireless (Sequoia); the unicorn-list match is Jasper AI and is rejected"))
L.append(fp("jow", "jow", "", "Series A", "2024-02", rw="Series A extension", status="private", **pc("jow"), city="Paris", rng="below_1b",
    focus="Consumer & Marketplaces", note="Recipe-to-grocery shopping app (Paris); Northzone led the $13M Series A extension with Eurazeo (the firm's post, 2024-02-08)"))
L.append(wv("kahoot", "https://arcticstartup.com/kahoot-raises-10-million-series/", "Series A", "2016", conf="medium", status="acquired", city="Oslo",
    rng="below_1b", focus="SaaS",
    note="Game-based learning (Oslo); Northzone came in with Microsoft Ventures on the $10M second tranche of the Series A that Creandum entered in 2015 (ArcticStartup; Creandum's row); Oslo listing 2021; taken private in 2024 by a Goldman Sachs Asset Management / General Atlantic / Kirkbi consortium; Wikidata NO confirmed"))
L.append(fp("katana", "katana", "our investment", "Growth", "2022-10", rw="Series B", status="private", **pc("katana"), city="Tallinn",
    rng="below_1b", focus="SaaS", note="Manufacturing ERP for SMEs (Tallinn); Northzone led the $35M Series B with Lightrock, Atomico and 42CAP (the firm's post, 2022-10-13), its first investment"))
L.append(wv("klang", "https://80.lv/articles/klang-games-raises-money-to-develop-seed", "Series A", "2018-07", status="private", **pc("klang"),
    city="Berlin", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Game studio building the MMO Seed (Berlin); Northzone led the $8.95M Series A with Makers Fund, Novator and firstminute (80 Level, 2018-07-18; the firm's post); $22.3M Series B led by Novator, Aug 2019 (GamesIndustry.biz)"))
L.append(cls("klarna", status="public", city="Stockholm", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015",
    rng="1b_plus", usd=int(float(sib("klarna", "ivp", "usd"))), val_src="web_verified", val_cite=sib("klarna", "ivp", "val_cite"),
    asof=sib("klarna", "ivp", "asof"), focus="Fintech & Payments",
    note="Buy-now-pay-later and digital bank (Stockholm, founded 2005); the firm lists Partnered 2015, ten years and several rounds after Sequoia's 2010 entry, so any Northzone entry is a growth round (a 2015 round, Business Insider 2015-09-01); NYSE since Sept 2025; market cap aligned to IVP's and Atomico's cited figure of 2026-09-25; Wikidata SE confirmed"))
L.append(cls("kota", status="private", **pc("kota"), city="Dublin", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Employee benefits platform (Dublin; formerly Yonder, not Northzone's London credit-card Yonder); the firm lists Partnered 2022 and Jeppe Zink; EUR 5M seed led by EQT Ventures in Oct 2023 and a $14.5M Series A in 2025 (Silicon Republic, the firm's press link); Northzone's 2022 round is not named"))
L.append(cls("kriya", status="acquired", **pc("kriya"), city="London", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="SME invoice finance and B2B payments (London), formerly MarketInvoice then MarketFinance; Northzone led a $5M round in Dec 2014 (the firm's archived post, round not named); the firm marks it Acquired, acquirer not found on the surfaces read; not Kriya Therapeutics"))
L.append(wv("labster", TC_LABSTER, "Series A", "2017-09", status="private", city="Copenhagen", **pc("labster"), rng="below_1b",
    focus="SaaS", note="Virtual science labs for education (Copenhagen); Northzone joined the $10M Series A (TechCrunch, 2017-09-06; the firm's post 'Why we invested in Labster', Marta Sjögren); Balderton's row enters the same round"))
L.append(cls("lastminute-com", status="acquired", **pc("lastminute-com"), city="London", stage="undetermined", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Online travel (London, founded 1998); the firm lists Partnered 1998 and marks it IPO (LSE, 2000), round not named; acq. by Sabre, 2005; the firm's Unicorn tag is a label, not a mark"))
L.append(cls("livepeer", status="private", **pc("livepeer"), city="New York", stage="Series A", stage_src="model", stage_conf="medium",
    entry_date="2019-06", rng="below_1b", focus="Crypto & Web3",
    note="Decentralised video transcoding network (Livepeer Inc., New York); the firm lists Partnered 2019 and posted the $8M raise of June 2019 (Cointelegraph), the company's Series A; Northzone also joined the $20M Series B led by DCG, July 2021 (CoinDesk)",
    rounds=[rnd("2019-06-19", "Series A", 8000000, None, True, art("livepeer", "8m"), "press"),
            rnd("2021-07-29", "Series B", 20000000, "Digital Currency Group", True, news("Livepeer", "CoinDesk"), "press")]))
L.append(wv("logicstar", news("LogicStar", "Recursive"), "Pre-Seed", "2025-02", status="private", **pc("logicstar"), city="Zurich",
    rng="below_1b", focus="AI & Applied AI",
    note="AI agent that fixes software bugs (Zurich, an INSAIT and ETH spin-off); Northzone led the $3M (EUR 2.9M) pre-seed (the firm's post 2025-02-04; The Recursive)"))
L.append(cls("lorum", status="private", **pc("lorum"), city="Dubai", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Global clearing infrastructure without correspondent banks (formerly Fuse; the firm lists the UAE, Partnered 2025); no press names the round"))
L.append(cls("magic-labs", status="acquired", **pc("magic-labs"), city="San Francisco", stage="undetermined", rng="below_1b",
    focus="Crypto & Web3",
    note="Passwordless login and embedded wallets (magic.link, San Francisco); the firm lists Partnered 2020, round not named; Payward (Kraken) bought the embedded-wallet business in July 2026 and the remaining company renamed itself Newton Labs (The Cryptonomist, 2026-07-27): the business the firm backed was sold, read as acquired; not Sequoia's Magic (the AI coding lab)"))
L.append(cls("mamut", status="acquired", city="Oslo", stage="undetermined", rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="SMB business software (Oslo, founded 1994); the firm lists Partnered 1998 and marks it IPO (Oslo Børs), round not named; acq. by Visma, 2011; the pre-filled 'defunct' is disputed; Wikidata NO confirmed"))
L.append(cls("masmovil", status="acquired", **pc("masmovil"), city="Madrid", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="MásMóvil, Spanish mobile operator; the firm lists Partnered 2007, round not named; taken private by KKR, Cinven and Providence, 2020, merged with Orange Spain 2024"))
L.append(cls("matsmart", status="private", **pc("matsmart"), city="Stockholm", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Surplus-food e-commerce (Stockholm; trades as Motatos abroad); Northzone announced its investment on 2015-12-15 (the firm's post, round not named); EUR 7.5M 2017, EUR 24M 2021, EUR 38M Series D 2022"))
L.append(cls("medwing", status="private", **pc("medwing"), city="Berlin", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2019",
    rng="below_1b", focus="Healthcare & Bio",
    note="Healthcare recruitment marketplace (Berlin); the firm lists Partnered 2019, the round before the EUR 28M Series B of July 2020 (Cathay; Adevinta), after Cherry's seed: the Series A by the record's own sequence; Northzone also in the $47M Series C of 2023 (TechCrunch)"))
L.append(wv("microagi", news("MicroAGI", "AI Insider"), "Seed", "2026-07", status="private", **pc("microagi"), city="Munich", grad="censored",
    rng="below_1b", focus="Industrial & Robotics",
    note="Robotics deployment platform for industry (Munich); the $55M seed led by Hummingbird with Northzone, LocalGlobe, Village Global and redalpine (AI Insider, 2026-07-16)"))
L.append(wv("mimo", news("Mimo", "months after"), "Seed", "2024-04", conf="medium", status="private", **pc("mimo"), city="London", rng="below_1b",
    focus="Fintech & Payments",
    note="B2B payments and credit for SMBs (London); Northzone led the EUR 18M round of April 2024 (the firm's post 2024-04-11), which UKTN calls the company's 'major seed round' (2025-03-12), Jessica Schultz; a GBP 6M follow-on led by Project A in March 2025"))
L.append(cls("monumental", status="private", **pc("monumental"), city="Amsterdam", stage="undetermined", rng="below_1b",
    focus="Industrial & Robotics",
    note="Bricklaying robots (Amsterdam); the firm lists Partnered 2023 and Michiel Kotting; $25M announced Feb 2024 (The Robot Report), round not named"))
L.append(cls("murphy", status="private", **pc("murphy"), stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite=post("murphy", "backing murphy"), entry_date="2025-07", grad="censored", rng="below_1b", focus="AI & Applied AI",
    flags=["city_unknown"],
    note="AI debt collection (the firm lists Spain); Northzone led the $15M of pre-seed and seed funding with ElevenLabs, Lakestar, Seedcamp and Enzo (the firm's post, 2025-07-14): the round Northzone led is the seed; the city is not given on the surfaces read"))
L.append(cls("na-kd", status="private", city="Gothenburg", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2017-01",
    rng="below_1b", focus="Consumer & Marketplaces",
    note="Online fashion brand (Gothenburg); Northzone led the EUR 14M round with eEquity (the firm's post 2017-01-03; tech.eu), the round before the $45M 'B-round' led by Partech (the firm's post 2018-01-15): the Series A by the record's own sequence",
    rounds=[rnd("2017-01-03", "undisclosed (before the B)", None, "Northzone", True, post("na-kd-com-joins-northzone-family"), "firm")]))
L.append(cls("napatech", status="public", **pc("napatech"), city="Copenhagen", stage="undetermined", rng="below_1b", focus="Data Infrastructure",
    note="FPGA SmartNICs (Søborg, Copenhagen); the firm lists Partnered 2004 and marks it IPO (Oslo Børs, 2013), round not named; small cap, below $1B"))
L.append(cls("nested", status="private", **pc("nested"), city="London", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Chain-free estate agency (London); Northzone and Balderton put GBP 20m of equity into the GBP 120m raise of Nov 2018 (the firm's post 2018-11-12), round not named; Balderton had entered earlier"))
L.append(cls("nextgentel", city="Bergen", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Norwegian broadband provider (Bergen); the firm lists Partnered 2000 and marks it IPO (Oslo Børs), round not named; acquired later (TeliaSonera, 2006); Wikidata NO confirmed"))
L.append(cls("nimsoft", status="acquired", country="US", country_src="web_verified", country_cite="https://en.wikipedia.org/wiki/Nimsoft",
    city="Redwood City", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite="https://en.wikipedia.org/wiki/Nimsoft",
    entry_date="2007", rng="below_1b", focus="Data Infrastructure", flags=["model_disputes_source"],
    note="IT monitoring software (founded in Oslo, later Redwood City); 'In 2007 a 10.3 million Series A round of funding from JMI Equity and Northzone Ventures closed' (Wikipedia); the firm lists Partnered 2006; acq. by CA Technologies for $350M, 2010; the pre-filled GB is disputed; Sutter Hill's row holds the same company"))
L.append(fp("nirvana", "nirvana", "our investment in nirvana", "Series A", "2024-09", status="private", **pc("nirvana"), city="San Francisco",
    rng="below_1b", focus="Healthcare & Bio",
    note="Health-insurance benefit verification (meetnirvana.com, San Francisco); Northzone led the $24.2M Series A with Inspired, Eniac and Surface (the firm's post, 2024-09-12); the firm lists Partnered 2022, earlier than the post; not Nirvana Insurance (the $1.5B trucking insurer in General Catalyst's and Lightspeed's books)"))
L.append(fp("nivoda", "nivoda", "growth investment", "Growth", "2024-11", rw="Series C", status="private", **pc("nivoda"), city="London",
    rng="below_1b", focus="Consumer & Marketplaces",
    note="B2B diamond and gemstone marketplace (London); Northzone led the $51M (GBP 41M) Series C with Avenir, Headline, Abstract and Canaan (the firm's post, 2024-11-21), its first investment"))
L.append(wv("noda", TC_INFOGRID, "Series A", "2020-11", status="private", city="London", rng="below_1b", focus="Industrial & Robotics",
    note="IoT building monitoring (London), formerly Infogrid; Northzone led the $15.5M Series A (TechCrunch, 2020-11-30), Jeppe Zink; $90M in 2023 (TechCrunch); Wikidata GB confirmed"))
L.append(cls("openfx", status="private", **pc("openfx"), stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=post("openfx", "partnering"), entry_date="2026-03", rng="below_1b", focus="Fintech & Payments", flags=["city_unknown"],
    note="Stablecoin-based cross-border payments; Northzone co-led the $94M Series A (the firm's post; Business Wire 2026-03-31); the siblings disagree on the city (New York, San Francisco; a Miami outlet covers it) and the company's own pages were not readable, so no city is asserted",
    rounds=[rnd("2026-03-31", "Series A", 94000000, "co-led", True, post("openfx", "partnering"), "firm")]))
L.append(cls("openzeppelin", status="private", **pc("openzeppelin"), city="San Francisco", stage="undetermined", rng="below_1b",
    focus="Crypto & Web3",
    note="Smart-contract security (founded in Buenos Aires; San Francisco entity); the firm lists Partnered 2018, round not named; S&P Global agreed on 2026-09-17 to acquire it (Crypto News), not closed, so the row stays private until the closing"))

jl.write("batch-002", L)
