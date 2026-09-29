"""Batch 2 (PRO-104 grind, pass 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT  # noqa: E402

L = []


def geo(slug, city=None, country=None):
    c, ci, cite = hq(slug)
    return dict(country=country or c, country_cite=cite, city=city or ci)


L.append(cls("home24", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("home24"),
             note="Online furniture retailer, Berlin (founded 2009 in the Rocket Internet orbit). HV entered 2009-09-11 "
                  "(Fund III); no announcement names the round. Listed 2018; acq. by XXXLutz, 2023 (merger cleared by the "
                  "European Commission 2023-04), then delisted.",
             rounds=[], extra={"status_citation": gn("home24", "VUtsUXNIbw")}))

L.append(cls("hyperganic", status="private", rng="below_1b", stage="undetermined", focus="Industrial & Robotics",
             **geo("hyperganic"),
             note="Algorithmic engineering software for 3D printing, Munich. HV entered 2021-01 (Fund VIII); the $7.8M round "
                  "of April 2021 (3Druck, found by the firm-name search) is not named in its headline.",
             rounds=[rnd("2021-04-09", None, 7_800_000, None, True, gn("hyperganic", "hQRkhQN1BO"))]))

L.append(cls("i2x", status="acquired", rng="below_1b", stage="undetermined", focus="AI & Applied AI", **geo("i2x"),
             note="Conversation intelligence for sales teams, Berlin (founded 2017). HV entered 2017-02 (Fund VI). The "
                  "firm's export lists it as acquired and exited; the acquirer was not found on the surfaces read.",
             rounds=[]))

L.append(cls("impossible-cloud", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=gn("impossible-cloud", "M1VVVWcxYw"), entry_date="2023-03",
             focus="Data Infrastructure", **geo("impossible-cloud"),
             note="Enterprise cloud object storage, Hamburg. 'HV Capital and 1kx Leading a EUR 7M Seed Round' (Business "
                  "Wire, 2023-03-01; the firm's own entry date 2022-08-08 is the close). The token network's later "
                  "raises belong to Impossible Cloud Network, a separate Swiss entity.",
             rounds=[rnd("2023-03-01", "Seed", 7_600_000, "HV Capital, 1kx", True, gn("impossible-cloud", "M1VVVWcxYw"))]))

L.append(cls("inkitt", status="private", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             **geo("inkitt"),
             note="Reader-driven book and story publishing (founded in Berlin, 2014). HV entered 2019-08 (Fund VII), between "
                  "the $3.9M Series A of Sept 2017 and the $59M Series B of Oct 2021; no announcement names HV's 2019 round.",
             rounds=[rnd("2017-09-25", "Series A", 3_900_000, None, False, None),
                     rnd("2021-10-05", "Series B", 59_000_000, None, True, gn("inkitt", "VnFpdlE4Zw"))]))

L.append(cls("instant-commerce", status="private", rng="below_1b", stage="undetermined", focus="SaaS",
             **geo("instant-commerce"),
             note="Headless storefront builder, Amsterdam (founded 2022). HV entered 2022-07 (Fund VIII); no announcement "
                  "names the round.", rounds=[]))

L.append(cls("jobvalley", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("jobvalley"),
             note="Student and temporary staffing marketplace, Cologne: Studitemps (founded 2008) renamed jobvalley. HV "
                  "entered in 2008 (Fund II, co-founding capital; the firm's 2012 post: Seventure and co raise about EUR "
                  "3M); the founding round is not named. The old site's 'Studitemps' rows are this company (merge at "
                  "the rebuild).", rounds=[]))

L.append(cls("jokr", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=gn("jokr", "JYZGdxNzJR"), entry_date="2021-07", focus="Consumer & Marketplaces",
             **geo("jokr"),
             note="Instant grocery delivery (New York and Latin America; the firm's HQ field says Berlin, the founder's "
                  "base). HV's entry 2021-04-01 closed into the $170M Series A announced 2021-07-20 (Food On Demand, "
                  "found by the firm-name search; Balderton's own post names the round). A $50M Series D of 2023 valued "
                  "it at $800M (TechCrunch).",
             rounds=[rnd("2021-07-20", "Series A", 170_000_000, None, True, gn("jokr", "JYZGdxNzJR")),
                     rnd("2023-09-20", "Series D", 50_000_000, None, None, gn("jokr", "SDR2R2dEUQ"))]))

L.append(cls("kennek", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("kennek", "UDNad1pLMw"), entry_date="2023-10", focus="Fintech & Payments", **geo("kennek"),
             note="Lending operations software, London. HV's entry 2023-10-10 is the GBP 10M seed of Oct 2023 (City AM, "
                  "UKTN, found by the firm-name search).",
             rounds=[rnd("2023-10-09", "Seed", 12_500_000, None, True, gn("kennek", "UDNad1pLMw"))]))

L.append(cls("kipu-quantum", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("kipu-quantum", "1LZWU0S1ZR"), entry_date="2023-12", focus="Data Infrastructure",
             **geo("kipu-quantum"),
             note="Quantum computing software, Karlsruhe. HV's entry 2023-12-19 is the EUR 10.5M seed announced that day "
                  "(The Quantum Insider, found by the firm-name search).",
             rounds=[rnd("2023-12-19", "Seed", None, None, True, gn("kipu-quantum", "1LZWU0S1ZR"))]))

L.append(cls("klima", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("klima", "RGtJcUxUQQ"), entry_date="2020-08", focus="Climate & Energy",
             flags=["model_disputes_source"], **geo("klima"),
             note="Consumer carbon-offsetting app, Berlin (founded 2019). HV's entry 2019-12 closed into the $5.8M seed "
                  "announced 2020-08-12 (Crunchbase News, found by the firm-name search). The Wikidata status 'defunct' "
                  "dated 2004 belongs to a namesake and is disputed.",
             rounds=[rnd("2020-08-12", "Seed", 5_800_000, None, True, gn("klima", "RGtJcUxUQQ")),
                     rnd("2022-04-21", None, None, None, True, gn("klima", "dXI1Tjk1aw"))]))

L.append(cls("koro", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("koro", "eng0RFJCQQ"), entry_date="2022-03", focus="Consumer & Marketplaces", **geo("koro"),
             note="Direct-to-consumer pantry food brand, Berlin (founded 2014). HV entered at the EUR 50M round of March "
                  "2022 (FinSMEs, found by the firm-name search; the firm's own entry date 2022-03-23; export 'growth'), "
                  "extended as the Series B in April 2023 (tech.eu), followed by a EUR 35M Series C in Nov 2024.",
             rounds=[rnd("2022-03-29", "Series B", 50_000_000, None, True, gn("koro", "eng0RFJCQQ")),
                     rnd("2023-04-20", "Series B extension", 20_000_000, None, True, gn("koro", "TdDaXBvVlE")),
                     rnd("2024-11-20", "Series C", 35_000_000, None, True, gn("koro", "bE05NWw4VQ"))]))

L.append(cls("lamudi", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("lamudi"),
             note="Emerging-markets property portal (a Rocket Internet company; Berlin, later Makati). HV entered at the $18M "
                  "round of Feb 2015 (the firm's own news post and the firm-name search), not named as a series. acq. by "
                  "EMPG, 2020 (Lamudi Global); its country units later went to Lifull and Digital Classifieds Group.",
             rounds=[rnd("2015-02-10", None, 18_000_000, None, True, gn("lamudi", "MU40VWhORg"))],
             extra={"status_citation": gn("lamudi", "pmTENUVUFB")}))

L.append(cls("lanch", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite=gn("lanch", "1ZNUdpY1Fn"), entry_date="2023-10",
             grad="graduated", grad_src="web_verified", grad_cite=gn("lanch", "NuNEhUdlp3"),
             focus="Consumer & Marketplaces", **geo("lanch"),
             note="Creator-led delivery food brands, Berlin (founded 2023). HV's entry 2023-04 closed into the $6.9M "
                  "(EUR 6.5M) round announced 2023-10-12 (TechCrunch, tech.eu; the firm-name search), the company's first; "
                  "a EUR 26M round of Feb 2025 named the Series A (Business Insider) graduates the row.",
             rounds=[rnd("2023-10-12", "Seed", 6_900_000, None, True, gn("lanch", "1ZNUdpY1Fn")),
                     rnd("2025-02-12", "Series A", 27_000_000, None, True, gn("lanch", "NuNEhUdlp3"))]))

L.append(cls("lazada", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("lazada"),
             note="South-east Asian e-commerce marketplace (a Rocket Internet company, founded 2012). HV entered 2012-04-16 "
                  "(Fund V) and sold with the other early holders when Alibaba took control in 2016 (Reuters, 2016-04-12); "
                  "the round HV entered is not named.",
             rounds=[], extra={"status_citation": gn("lazada", "Nob1Y1dXct")}))

L.append(cls("lecturio", status="private", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
             **geo("lecturio"),
             note="Online medical and professional education, Leipzig (founded 2008). HV entered 2011-09 (Fund IV, later "
                  "Fund Coco); the entry round is not named. Bought NEJM Healer (2024) and SimTutor (2025).", rounds=[]))

L.append(cls("lendis", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("lendis"),
             note="Workplace equipment management, Berlin (founded 2018). HV entered 2019-03 (Fund VII); no announcement "
                  "names that round. EUR 80M debt and equity in Jan 2022 (EU-Startups).", rounds=[]))

L.append(cls("limehome", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=gn("limehome", "liVUU1bUpj"), entry_date="2019", focus="Consumer & Marketplaces",
             **geo("limehome"),
             note="Tech-run short-stay apartments, Munich (founded 2018). HV entered 2019 (Fund VII) in the Series A that "
                  "Limehome extended by EUR 10M in Oct 2020 (PhocusWire, found by the firm-name search).",
             rounds=[rnd("2020-10-23", "Series A extension", None, None, True, gn("limehome", "liVUU1bUpj"))]))

L.append(cls("linearity", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("linearity"),
             note="Vector design and motion software (Vectornator, renamed Linearity 2022), Berlin. HV entered 2019-10 "
                  "(Fund VII), before the EQT Ventures-led Series A of 2021; HV's round is not named.", rounds=[]))

L.append(cls("lingokids", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("lingokids"),
             note="Early-childhood learning app, Madrid (founded 2014). HV entered at the $4M round of June 2017 (Yahoo, "
                  "Tech in Asia, found by the firm-name search), not named as a series; a $6M Series A followed in Oct 2018 "
                  "and a EUR 33M Series C in June 2021. HV exited in 2025 when Nextalia bought a stake; the company "
                  "continues independently.",
             rounds=[rnd("2017-06-21", None, 4_000_000, None, True, gn("lingokids", "FJdHg3TXZR")),
                     rnd("2018-10-02", "Series A", 6_000_000, None, True, gn("lingokids", "EJ2TDFRQWc"))]))

L.append(cls("loopme", status="private", rng="below_1b", stage="Series A", stage_src="first_party", stage_conf="high",
             stage_cite="https://web.archive.org/web/20140406184303/http://www.holtzbrinck-ventures.com:80/index.php?news_en&newsdetail=20140327-292_loopme-raises-3-million-in-series-a-funding-round-for-mobile-and-games-advertising",
             entry_date="2014-03", focus="Media, Gaming & Advertising", **geo("loopme"),
             note="AI brand-advertising platform, London (founded 2011). The firm's own news post of 2014-03-27, 'LoopMe "
                  "raises $3 million in Series A funding round', is HV's entry (HV Entry 2014-03-18, Fund V), after a "
                  "$500K seed of Jan 2013. HV exited in 2022; LoopMe operates and bought Chartboost in Dec 2024.",
             rounds=[rnd("2013-01-16", "Seed", 500_000, "Russell Buckley", False, None),
                     rnd("2014-03-27", "Series A", 3_000_000, None, True,
                         "https://web.archive.org/web/20140406184303/http://www.holtzbrinck-ventures.com:80/index.php?news_en&newsdetail=20140327-292_loopme-raises-3-million-in-series-a-funding-round-for-mobile-and-games-advertising", "firm")]))

L.append(cls("marvel-fusion", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("marvel-fusion", "nhSZEVLLVU"), entry_date="2024-09", focus="Climate & Energy",
             **geo("marvel-fusion"),
             note="Laser-driven fusion energy, Munich (founded 2019). HV entered at the $70M round of Sept 2024 (TechCrunch, "
                  "found by the firm-name search; export 'growth', Fund IX Growth), the company's Series B, extended by "
                  "EUR 50M in March 2025.",
             rounds=[rnd("2024-09-25", "Series B", 70_000_000, None, True, gn("marvel-fusion", "nhSZEVLLVU")),
                     rnd("2025-03-31", "Series B extension", 54_000_000, None, None, gn("marvel-fusion", "VTN4R1l0aw"))]))

L.append(cls("matterway", status="acquired", rng="below_1b", stage="undetermined", focus="AI & Applied AI",
             **geo("matterway"),
             note="Desktop workflow automation, Berlin (founded 2014). HV entered 2017-12-21 (Fund VI). The firm's export "
                  "gives its current stage as 'acquired'; the acquirer was not found on the surfaces read.", rounds=[]))

L.append(cls("neura-robotics", status="private", rng="1b_plus", usd=7_000_000_000, val_src="web_verified",
             val_cite=gn("neura-robotics", "Mm04LWRSTA"), asof="2026-06", stage="Series A", stage_src="web_verified",
             stage_conf="medium", stage_cite=gn("neura-robotics", "NElsQmRFUQ"), entry_date="2023-07",
             focus="Industrial & Robotics", **geo("neura-robotics"),
             note="Cognitive and humanoid robots, Metzingen (founded 2019). HV entered at the $55M (EUR 50M) round of "
                  "July 2023 'led by Primepulse, Vsquared, Lingotto, and HV Capital' (GP Bullhound; TechCrunch), the "
                  "company's first institutional round; EUR 120M Series B Jan 2025; the Series C of up to $1.4B in June "
                  "2026 valued it at $7B.",
             rounds=[rnd("2023-07-19", "Series A", 55_000_000, "Primepulse, Vsquared, Lingotto, HV Capital", True, gn("neura-robotics", "NElsQmRFUQ")),
                     rnd("2025-01-16", "Series B", 130_000_000, None, True, gn("neura-robotics", "dBRTJiaGlx")),
                     rnd("2026-06-10", "Series C", 1_400_000_000, None, None, gn("neura-robotics", "Mm04LWRSTA"))]))

L.append(cls("one-data", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("one-data", "XzlEd1BfZw"), entry_date="2024-07", focus="Data Infrastructure",
             **geo("one-data"),
             note="Data-product platform, Passau (founded 2021). HV entered at the EUR 32M Series B extension of July 2024 "
                  "(FinSMEs, found by the firm-name search; the firm's entry year 2024).",
             rounds=[rnd("2024-07-17", "Series B extension", None, None, True, gn("one-data", "XzlEd1BfZw"))]))

L.append(cls("ottonova", status="private", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
             country="DE", city="Munich", flags=["model_disputes_source"],
             note="Digital private health insurer, Munich (the firm's HQ field reads Berlin; ottonova's seat is Munich, "
                  "and the archived HV list gave 'Berlin, Germany / Munich'). HV entered 2016 (Fund VI); the entry round "
                  "is not named. A Series F closed in Sept 2022.", rounds=[],
             extra={"hq_country_source": "web_verified", "hq_country_citation": EXPORT, "hq_city_source": "model_knowledge"}))

L.append(cls("outfittery", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("outfittery"),
             note="Curated men's fashion boxes, Berlin (founded 2012). HV entered 2012-06 (Fund V, later Fund Coco); the "
                  "firm's 2012 posts ('Hausbesuch bei Outfittery') do not name the round. Merged with Lookiero into the "
                  "Lookiero Outfittery Group, which raised EUR 17M in Jan 2026.", rounds=[]))

L.append(cls("packmatic", status="private", rng="below_1b", stage="undetermined", focus="Industrial & Robotics",
             **geo("packmatic"),
             note="B2B packaging procurement marketplace, Berlin (founded 2021). HV entered 2021-09-15 (Fund VIII); the round "
                  "is not named. EQT Ventures led the EUR 15M Series A of Jan 2024.", rounds=[]))

L.append(cls("parship", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("parship"),
             note="Online matchmaking, Hamburg. Founded by Holtzbrinck Ventures itself in 2000-01 (Fund I; the firm's 2011 "
                  "history: 'to ourselves found internationally successful companies such as Parship'); an incubation, so "
                  "no round is named. Sold to Oakley Capital in 2015, then to ProSiebenSat.1 as Parship Elite in 2016.",
             rounds=[], extra={"status_citation": gn("parship", "1I5WEFua2c")}))

L.append(cls("plan-a", status="acquired", rng="below_1b", stage="undetermined", focus="Climate & Energy",
             **geo("plan-a"),
             note="Carbon accounting software, Berlin (founded 2017). HV entered 2021-11 (Fund VIII); the round is not named. "
                  "acq. by Diginex, 2026 (EUR 55M cash and shares, closed 2026-01-14).",
             rounds=[], extra={"status_citation": gn("plan-a", "3BrMHdWYjU")}))

L.append(cls("plusdental", status="acquired", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
             **geo("plusdental"),
             note="Clear-aligner orthodontics, Berlin (founded 2017). HV entered 2017 (Fund VI). The firm's export lists it "
                  "as acquired and exited; the acquirer was not found on the surfaces read.", rounds=[]))

L.append(cls("polyteia", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("polyteia"),
             note="Data platform for public administrations, Berlin. HV entered at the EUR 5M round of Feb 2023 (Sifted, "
                  "found by the firm-name search; the firm's own entry date 2023-03-03), not named as a series in the "
                  "headline.", rounds=[rnd("2023-02-28", None, 5_000_000, None, True, gn("polyteia", "3gzb2Etd0Y"))]))

L.append(cls("powerus", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("powerus"),
             note="Hiring marketplace for skilled blue-collar workers, Berlin (YC Summer 2020). HV entered 2021-01 (Fund VIII) "
                  "after the batch; the round is not named. EUR 24M Series B in Sept 2023. Not the US drone maker "
                  "Powerus that merged with Aureus in 2026.", rounds=[]))

L.append(verdict("qonto", "not_member",
                 "Sale consideration (decisions.md D4): HV's Qonto line carries Penta's entry (export: HV Entry 2019, "
                 "Fund VII, the vintage of HV's Penta position; Storyblok entry 2022-08-08, the month Qonto's purchase of "
                 "Penta closed). Qonto agreed to buy Penta in July 2022 (tech.eu, 2022-07-22); no financing of Qonto naming "
                 "HV was found. Penta is the member.", ec="site_listing", conf="medium", cite=gn("qonto", "Y2FMQmNqcA")))

L.append(cls("qualifyze", status="private", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
             **geo("qualifyze"),
             note="Supplier audits and compliance for pharma, Frankfurt (founded 2017). HV entered 2021-11-03 (Fund VIII); no "
                  "announcement names that round. $12M in Aug 2023 and $54M in Sept 2024 (TechCrunch).", rounds=[]))

L.append(cls("quantum-systems", status="private", rng="1b_plus", usd=8_000_000_000, val_src="web_verified",
             val_cite=gn("quantum-systems", "1lX180SXZp"), asof="2026-07", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=gn("quantum-systems", "UzNmxBUFdn"), entry_date="2023-10",
             focus="Industrial & Robotics", **geo("quantum-systems"),
             note="Uncrewed aerial systems for defence and industry, Gilching (founded 2015). HV entered at the EUR 63.6M "
                  "Series B of Oct 2023 (tech.eu, found by the firm-name search; the firm's own entry date 2023-11-08; "
                  "export 'growth'). The $1.2B Series D of July 2026 set a post-money of about $8B (FinSMEs).",
             rounds=[rnd("2023-10-24", "Series B", None, None, True, gn("quantum-systems", "UzNmxBUFdn")),
                     rnd("2026-07-02", "Series D", 1_200_000_000, None, None, gn("quantum-systems", "1lX180SXZp"))]))

L.append(cls("roadsurfer", status="private", rng="below_1b", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=EXPORT, entry_date="2021-03", focus="Consumer & Marketplaces", **geo("roadsurfer"),
             note="Campervan rental and subscription, Munich (founded 2017). The firm's export labels its entry 'growth' "
                  "(Fund VIII, entry 2021-03-01), the Series B that Roadsurfer extended by EUR 4.5M in Aug 2021 (Munich "
                  "Startup).", rounds=[rnd("2021-08-02", "Series B extension", None, None, None, gn("roadsurfer", "b2xXWktRQw"))]))

L.append(verdict("rocket-internet", "not_member",
                 "Sale consideration (decisions.md D4; config trap): the firm's own 2015 page: 'Prior to Rocket's IPO, "
                 "Holtzbrinck Ventures decided to sell its entire shareholding in selected companies to Rocket and thus "
                 "became a direct shareholder.' The investments are the Rocket companies (Dafiti, Lazada, lamoda, Linio, "
                 "Jabong, Namshi, Easy Taxi and the rest), each its own member row.", ec="site_listing", conf="high",
                 cite="https://web.archive.org/web/20150219060148/http://www.holtzbrinck-ventures.com:80/index.php?rocket"))

L.append(cls("sanity", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("sanity", "UVTM0ViQ1U"), entry_date="2020-02", focus="Healthcare & Bio",
             flags=["model_disputes_source"], **geo("sanity"),
             note="Sanity Group, medical and wellness cannabis, Berlin (not Sanity.io). HV's entry (HV Entry 2019, Fund VII) "
                  "closed into the EUR 20.1M Series A announced 2020-02-11 (EU-Startups, found by the firm-name search), "
                  "after Cherry's seed. acq. by Organigram, 2026 (closed 2026-04-15). The Wikidata country AU belongs to a "
                  "namesake and is disputed.",
             rounds=[rnd("2020-02-11", "Series A", None, None, True, gn("sanity", "UVTM0ViQ1U")),
                     rnd("2022-09-27", "Series B", 37_600_000, None, None, gn("sanity", "kZBa2RGYzA"))],
             extra={"status_citation": gn("sanity", "d1NHUzR6aA")}))

L.append(cls("sastrify", status="acquired", rng="below_1b", stage="undetermined", focus="SaaS", **geo("sastrify"),
             note="SaaS procurement and spend optimisation, Cologne (founded 2020). HV entered 2021-09 (Fund VIII); the round "
                  "is not named on the surfaces read ($32M Series B in May 2023). acq. by Deel, 2026 (the firm's export: "
                  "'Exited to Deel in 2026').", rounds=[rnd("2023-05-25", "Series B", 32_000_000, None, True, gn("sastrify", "BVenlCcERn"))],
             extra={"status_citation": gn("sastrify", "015ejhVelU")}))

write("batch-002", L)
