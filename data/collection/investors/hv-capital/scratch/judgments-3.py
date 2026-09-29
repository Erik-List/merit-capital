"""Batch 3 (PRO-104 grind, pass 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT, firm_cite  # noqa: E402

L = []


def geo(slug, city=None, country=None):
    c, ci, cite = hq(slug)
    return dict(country=country or c, country_cite=cite, city=city or ci)


L.append(cls("sch-ttflix", status="private", rng="below_1b", stage="undetermined", focus="Industrial & Robotics",
             **geo("sch-ttflix"),
             note="Construction-materials and waste-logistics marketplace, Guetersloh (founded 2019). HV entered 2020-07 "
                  "(Fund VII), before the $50M Series A of Sept 2021 (FinSMEs, found by the firm-name search); HV's own "
                  "round is not named.", rounds=[rnd("2021-09-30", "Series A", 50_000_000, None, True, gn("sch-ttflix", "hqQTk1RXlH"))]))

L.append(cls("scoutbee", status="acquired", rng="below_1b", stage="undetermined", focus="AI & Applied AI",
             city="Würzburg", country="DE", country_cite=EXPORT,
             note="AI supplier discovery, Wuerzburg (founded 2015). HV entered 2018 (Fund VII), before the $60M Series B of "
                  "Jan 2020 (Technical.ly; Atomico's cited entry); HV's round is not named. acq. by Coupa, 2025 (announced "
                  "2025-10-06; the firm's export: 'Exited to Coupa in 2025').",
             rounds=[rnd("2020-01-23", "Series B", 60_000_000, None, True, gn("scoutbee", "pYa0FCd2pR"))],
             extra={"status_citation": gn("scoutbee", "X2puOXNhQQ")}))

L.append(cls("sdui", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("sdui"),
             note="School communication and administration platform, Koblenz (founded 2018). HV entered 2021-02 (Fund VIII); "
                  "no announcement names that round. EUR 25M Series A in Feb 2023 (VC Magazin); a strategic investment led "
                  "by Bain Capital in July 2025.", rounds=[rnd("2023-02-01", "Series A", 25_000_000, None, None, gn("sdui", "hZckdrempn"))]))

L.append(cls("simpleclub", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("simpleclub"),
             note="Learning app for school and vocational training, Munich (founded 2015). HV entered 2020-09 and again "
                  "2021-12 (Fund VII); no announcement names HV's round.", rounds=[]))

L.append(cls("spread", status="private", rng="below_1b", stage="undetermined", focus="AI & Applied AI",
             **geo("spread"),
             note="Engineering-intelligence platform for hardware product data, Berlin (founded 2019). HV entered at the "
                  "EUR 14.6M ($16M) round of May 2023 (EU-Startups, tech.eu, found by the firm-name search; the firm's own "
                  "entry date 2023-05-05), not named as a series in the headlines; a $30M Series B followed in April 2026.",
             rounds=[rnd("2023-05-03", None, 16_000_000, None, True, gn("spread", "hQdGFFMDBv")),
                     rnd("2026-04-29", "Series B", 30_000_000, None, True, gn("spread", "ZWVGaHZVNg"))]))

L.append(cls("storyblok", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("storyblok", "cXBaV2xZag"), entry_date="2022-05", focus="SaaS", flags=["model_disputes_source"],
             **geo("storyblok", city="Linz", country="AT"),
             note="Headless CMS, Linz (founded 2017; hvcapital.com runs on it). HV entered at the $47M round of 2022-05-17 "
                  "(TechCrunch, found by the firm-name search; the firm's own entry date is the same day; export 'growth'), "
                  "the Series B after the $8.5M Series A of Feb 2021; $80M Series C in June 2024. The Wikidata country "
                  "'worldwide' is not a country and is replaced.",
             rounds=[rnd("2021-02-03", "Series A", 8_500_000, "Mubadala Capital", False, None),
                     rnd("2022-05-17", "Series B", 47_000_000, None, True, gn("storyblok", "cXBaV2xZag")),
                     rnd("2024-06-04", "Series C", 80_000_000, "Brighton Park Capital", None, gn("storyblok", "k9WSzNQZGc"))]))

L.append(cls("studivz", status="defunct", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("studivz"),
             note="Student social network, Berlin (founded 2005). HV entered 2006 (Fund II); the round is not named. Bought by "
                  "the publishing group's Holtzbrinck Networks in Jan 2007 (an exit to the parent; D2); the operator filed "
                  "for insolvency in Sept 2017 (Stern, Kleine Zeitung).", rounds=[],
             extra={"status_citation": gn("studivz", "lTaGd4ajJn")}))

L.append(cls("stylight", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("stylight"),
             note="Fashion discovery and shopping platform, Munich (founded 2008). HV entered 2008-11 (Fund III); the round is "
                  "not named. SevenVentures (ProSiebenSat.1) led a Series B in Jan 2013; acq. by 7Commerce (ProSiebenSat.1), "
                  "2016 (TechCrunch, 2016-06-01).", rounds=[], extra={"status_citation": gn("stylight", "YjZlR2RIUQ")}))

L.append(cls("super-ai", status="private", rng="below_1b", stage="undetermined", focus="AI & Applied AI",
             **geo("super-ai"),
             note="Intelligent document processing (super.ai), US (the firm's HQ field San Francisco; the archived list Bellevue, "
                  "Washington). HV entered 2021-06 (Fund VIII); no announcement names the round.", rounds=[]))

L.append(cls("the-naked-market", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=gn("the-naked-market", "OXFNMTQyRg"), entry_date="2020-10",
             grad="graduated", grad_src="web_verified", grad_cite=gn("the-naked-market", "ZWYzZZaUx3"),
             focus="Consumer & Marketplaces", **geo("the-naked-market"),
             note="Food and beverage brand incubator, San Francisco (founded 2018). HV was in the $6M seed closed and "
                  "announced 2020-10-28 (PR Newswire, found by the firm-name search; the firm's own entry date 2018-12 is "
                  "its first cheque into the round); the $27.5M Series A of Nov 2021 graduates the row.",
             rounds=[rnd("2020-10-28", "Seed", 6_000_000, None, True, gn("the-naked-market", "OXFNMTQyRg")),
                     rnd("2021-11-11", "Series A", 27_500_000, None, None, gn("the-naked-market", "ZWYzZZaUx3"))]))

L.append(cls("thermondo", status="private", rng="below_1b", stage="undetermined", focus="Climate & Energy",
             **geo("thermondo"),
             note="Heating and solar installer platform, Berlin (founded 2012). HV entered in the EUR 6M round of 2015 with "
                  "Rocket Internet (the firm's own post of 2015-04-15; HV Entry 2015, Fund VI), not named as a series in the "
                  "post's title. Brookfield took a majority stake in 2021 while thermondo kept raising outside rounds (EUR "
                  "50M in July 2025), so the company reads private.", rounds=[]))

L.append(cls("timberhub", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite=gn("timberhub", "JCUW1CYWFR"), entry_date="2022-09", focus="Industrial & Robotics",
             **geo("timberhub"),
             note="B2B timber trading marketplace, Amsterdam (founded 2022). HV's entry 2022-02 closed into the EUR 5.8M "
                  "round announced Sept 2022 (tech.eu, found by the firm-name search), the company's seed (Creandum's own "
                  "post).", rounds=[rnd("2022-09-27", "Seed", None, None, True, gn("timberhub", "JCUW1CYWFR"))]))

L.append(cls("tourlane", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("tourlane"),
             note="Online tailor-made travel, Berlin (founded 2016). HV entered 2016 (Fund VI), before the EUR 21.1M Series B "
                  "led by Sequoia (Dec 2018); HV's round is not named on the surfaces read. Series C 2019-20, EUR 25M in "
                  "Nov 2024 led by Sequoia.",
             rounds=[rnd("2018-12-06", "Series B", 24_000_000, "Sequoia Capital", True, gn("tourlane", "SGJtSl9fRQ")),
                     rnd("2019-05-07", "Series C", 47_000_000, "Sequoia, Spark Capital", True, gn("tourlane", "YtSmltYkZR"))]))

L.append(cls("ultimate-ai", status="acquired", rng="below_1b", stage="undetermined", focus="AI & Applied AI",
             **geo("ultimate-ai"),
             note="Customer-support automation, Helsinki (founded 2017). HV entered 2018-08 (Fund VII), before the $20M Series "
                  "A of Dec 2020; HV's round is not named. acq. by Zendesk, 2024.", rounds=[]))

L.append(cls("upvest", status="private", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
             **geo("upvest"),
             note="Investment API for fintechs, Berlin (founded 2017). HV entered 2017 (Fund VI); no announcement names HV's "
                  "round. EUR 7M Series A Dec 2019, extended 2020-21; EUR 100M Series C Dec 2024.",
             rounds=[rnd("2019-12-14", "Series A", None, None, None, gn("upvest", "dGozdmF5OA")),
                     rnd("2024-12-12", "Series C", None, None, True, gn("upvest", "F4SVpwV3l3"))]))

L.append(cls("visionai", status="private", rng="below_1b", stage="undetermined", focus="AI & Applied AI",
             **geo("visionai"),
             note="AI search and tagging for e-commerce, Bielefeld (founded 2021). HV entered at the EUR 5M round of Oct 2023 "
                  "(tech.eu, found by the firm-name search; the firm's own entry date 2023-10-10), not named as a series in "
                  "the headline.", rounds=[rnd("2023-10-23", None, 5_300_000, None, True, gn("visionai", "SW4tZXBLOQ"))]))

L.append(cls("warehousing1", status="private", rng="below_1b", stage="undetermined", focus="Industrial & Robotics",
             **geo("warehousing1"),
             note="E-commerce warehousing and fulfilment network, Berlin (founded 2018). HV entered 2019-08 (Fund VII); no "
                  "announcement names the round.", rounds=[]))

L.append(cls("wasp", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("wasp", "WGlWamtlRQ"), entry_date="2021-10", focus="DevTools & APIs", **geo("wasp"),
             note="Full-stack web framework (wasp-lang), Zagreb (YC Winter 2021). HV's entry 2021-07 closed into the $1.5M seed "
                  "announced 2021-10-04 (TechCrunch, found by the firm-name search), after the YC batch.",
             rounds=[rnd("2021-10-04", "Seed", 1_500_000, None, True, gn("wasp", "WGlWamtlRQ"))]))

L.append(cls("wellster", status="private", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
             **geo("wellster"),
             note="Telemedicine and treatment platform, Munich (founded 2018). HV entered 2018 (Fund VII); no announcement "
                  "names that round. EUR 35M in June 2021; Series B completed at $60M in Jan 2022.",
             rounds=[rnd("2022-01-18", "Series B", 60_000_000, None, None, gn("wellster", "p6M0lKcFVN"))]))

L.append(cls("wooga", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2009-05", grad="graduated", grad_src="web_verified",
             grad_cite="https://en.wikipedia.org/wiki/Wooga", flags=["stage_uncited"],
             focus="Media, Gaming & Advertising", **geo("wooga"),
             note="Social and mobile games, Berlin (founded 2009). HV entered 2009-05 (Fund III), the company's first funding "
                  "that spring ('Holtzbrinck Ventures, which had provided funding earlier that year, also participated in "
                  "this round', Wikipedia on Balderton's EUR 5M Series A of Nov 2009, which graduates the row); the spring "
                  "round is not named on any surface. acq. by Playtika, 2018 (tech.eu 2018-12-03).",
             rounds=[rnd("2009-05", None, None, None, True, None),
                     rnd("2009-11", "Series A", 7_300_000, "Balderton Capital", True, "https://en.wikipedia.org/wiki/Wooga")],
             extra={"status_citation": gn("wooga", "ldjYUxwckM")}))

L.append(cls("zencargo", status="private", rng="below_1b", stage="undetermined", focus="Industrial & Robotics",
             **geo("zencargo"),
             note="Digital freight forwarding, London (founded 2017). HV entered 2019-05 (Fund VII), after LocalGlobe's seed-plus "
                  "of Sept 2018 and before the GBP 30M Series B of May 2021; HV's round is not named.",
             rounds=[rnd("2018-09-24", "Seed", 4_000_000, "LocalGlobe", False, gn("zencargo", "FTVm11MDJB")),
                     rnd("2021-05-11", "Series B", None, "Digital+ Partners", True, gn("zencargo", "UE9KWmItWg"))]))

# ---- old-book rows (corporate era and the 2010s exits)
L.append(cls("21diamonds", status="unknown", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("21diamonds"),
             note="Online jewellery, Munich (founded 2011). HV entered 2011-08; listed through 2015, an exit on the 2022-25 "
                  "lists. Its later state was not found.", rounds=[]))

L.append(cls("7trends", status="unknown", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("7trends"),
             note="Fashion e-commerce, Berlin. HV entered 2009-03; an exit on the 2022-25 lists. Its later state was not found.",
             rounds=[]))

L.append(cls("actio", status="unknown", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("actio"),
             note="Nikita Fahrenholz's Berlin app venture (actio.com, founded 2019). HV entered 2020-12 (the firm-name search: "
                  "a 'Millionenrunde' in Dec 2020); the seed reached EUR 10M in Feb 2021 (Startbase). Off HV's live list by "
                  "2026; its current state was not found. Not Actio Biosciences, the US biotech Jazz bought in 2026.",
             rounds=[rnd("2021-02-17", "Seed", None, None, True, gn("actio", "UmdvM2JFZw"))]))

L.append(cls("adscale", status="acquired", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             **geo("adscale"),
             note="Real-time ad exchange, Munich (founded 2007). HV entered 2007-07; listed through 2011, an exit on the "
                  "2022-25 lists (sold to Stroeer, 2011). The round is not named.", rounds=[]))

L.append(cls("ahaoho", status="unknown", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             country="DE", country_src="model_knowledge", flags=["city_unknown"],
             note="A 2008-09 portfolio company on the old site (index.php?ahaoho_en), under 'Former Investments' in 2011. "
                  "Its business and later state were not established.", rounds=[]))

L.append(cls("audible-de", status="acquired", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             country="DE", country_src="model_knowledge", city="Berlin", city_src="model_knowledge",
             note="Audible's German audiobook service, Berlin: a 2004 joint venture of Audible Inc., Random House and the "
                  "publishing group, whose stake the corporate unit held and listed as portfolio 2006-07 (D2, D7; the "
                  "shareholder agreement is an exhibit to Audible Inc.'s 10-Q of 2006-11-09). A formation stake, so no "
                  "round is named. Audible Inc. took the business over and was bought by Amazon in 2008.",
             rounds=[], extra={"status_citation": "https://www.sec.gov/Archives/edgar/data/1077926/000107792606000035/exhibit10_49de.htm"}))

L.append(cls("aurora-health", status="acquired", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
             **geo("aurora-health"),
             note="Moodpath mental-health app, Berlin (founded 2015). HV entered 2017-10-17. acq. by Schoen Klinik, 2019 "
                  "(kma Online, 2019-09-26). The round is not named.", rounds=[],
             extra={"status_citation": gn("aurora-health", "lQZ1FJVVpv")}))

L.append(cls("autoda", status="unknown", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("autoda"),
             note="Used-car trading, Filderstadt (founded 2010). HV entered 2011-01 (the firm's own post of 2011-04-27 on its "
                  "car family with meinauto.de and carsale24). Its later state was not found.", rounds=[]))

L.append(cls("b-cher-de", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("b-cher-de"),
             note="Online bookshop buecher.de, Augsburg (founded 1999). A corporate-era holding the unit listed under 'Exits' "
                  "on its 2006 site (D2); entry 1999-09. Sold on; the round is not named.", rounds=[]))

L.append(cls("betreut-de", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("betreut-de"),
             note="Care marketplace (besser betreut), Berlin (founded 2007). HV entered 2007-09. acq. by Care.com, 2012 "
                  "(deutsche-startups, 2012-07-11; the firm's own post of 2012-07-12). The round is not named.", rounds=[],
             extra={"status_citation": gn("betreut-de", "bzNFQ0FreA")}))

L.append(cls("billpay", status="acquired", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
             country="DE", country_src="model_knowledge", city="Berlin", city_src="model_knowledge",
             note="Invoice and instalment payments, Berlin. HV was invested by 2011 (current portfolio 2011; the firm's post "
                  "of 2012-06-29: Billpay raises from Kinnevik and its existing shareholders). acq. by Wonga, then sold to "
                  "Klarna in 2017 (Business Insider).", rounds=[], extra={"status_citation": gn("billpay", "VN6bFN1WWY")}))

L.append(verdict("boku", "not_member",
                 "Sale consideration (decisions.md D4): Boku bought HV's mopay in Oct 2014 ('Boku Buys Germany's Mopay In "
                 "Carrier Billing Consolidation', TechCrunch 2014-10-07; the firm's own news post of the same date); HV's Boku "
                 "line is dated 2014-12-31, the closing, and no financing of Boku naming HV was found. mopay is the member.",
                 ec="site_listing", conf="high", cite=firm_cite("boku")))

write("batch-003", L)
