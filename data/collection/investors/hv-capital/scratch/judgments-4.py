"""Batch 4 (PRO-104 grind, pass 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT, firm_cite  # noqa: E402

L = []


def geo(slug, city=None, country=None, src=None):
    c, ci, cite = hq(slug)
    d = dict(country=country or c, country_cite=cite, city=city or ci)
    return d


def old(slug, status, note, focus, stage="undetermined", rounds=None, extra=None, **kw):
    return cls(slug, status=status, rng="below_1b", stage=stage, focus=focus, note=note, rounds=rounds or [],
               extra=extra, **{**geo(slug), **kw})


L.append(old("bol-com", "acquired", "Online retailer bol.com, Utrecht. A corporate-era holding (entry 2003) the unit listed "
             "under 'Exits' from its 2006 site (D2). Sold on (Delta Lloyd 2009, Ahold 2012); the round is not named.",
             "Consumer & Marketplaces", extra={"status_citation": gn("bol-com", "EptbXBvTTA")}))
L.append(cls("bookya", status="unknown", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             country="DE", country_src="model_knowledge", flags=["city_unknown"],
             note="A 2008-10 portfolio company on the old site (index.php?bookya_en), under 'Former Investments' in 2011. Its "
                  "business and later state were not established.", rounds=[]))
L.append(old("brands4friends", "acquired", "Online private-sales club, Berlin (founded 2007). HV entered 2007-07. acq. by eBay, "
             "2010 ($200M, TechCrunch 2010-12-20); sold on to Regent in 2019 and shut in 2023. The round is not named.",
             "Consumer & Marketplaces"))
L.append(verdict("care-com", "not_member",
                 "Sale consideration (decisions.md D4): HV's Care.com stock came from the sale of HV's Betreut.de to Care.com "
                 "in July 2012. Care.com's Sixth Amended and Restated Investors' Rights Agreement, filed with its 2013 IPO "
                 "registration, lists Holtzbrinck Ventures GmbH & Co. KG beside Rocket Internet and Betreut.de's Berlin "
                 "founders and angels; no financing of Care.com naming HV was found. Betreut.de is the member.",
                 ec="fund_filing", conf="high",
                 cite="https://www.sec.gov/Archives/edgar/data/1412270/000141057813000222/filename11.htm"))
L.append(cls("cafepress", status="acquired", rng="below_1b", stage="undetermined",
             focus="Consumer & Marketplaces", **geo("cafepress", city="Louisville", country="US"),
             note="Print-on-demand marketplace (founded 1999; San Mateo, later Louisville). HV entered 2007-02 and was a "
                  "holder in the 2011-12 IPO registration (S-1/A of 2011-10-24 and 2012-02-17); the round HV bought into "
                  "is not named on the surfaces read. IPO 2012; acq. by Snapfish (2018) and sold on again in 2020.",
             rounds=[]))
L.append(old("caremondo", "unknown", "Care-services platform, Munich (founded 2014). HV entered 2015-09; an exit on the 2022-25 "
             "lists. Its later state was not found.", "Healthcare & Bio"))
L.append(old("carmudi", "acquired", "Emerging-markets car classifieds (a Rocket Internet company, Berlin). HV entered 2015-02 "
             "(the same date as Lamudi). Its country units were sold off; CarDekho Group bought Carmudi (Philippines 2019, the "
             "group 2022). The round is not named.", "Consumer & Marketplaces",
             extra={"status_citation": gn("carmudi", "2VQbXoyS3M")}))
L.append(old("carsale24", "unknown", "B2B used-car auctions, Solingen (founded 2010). HV entered 2011 (the firm's 2011 post on "
             "its car family with autoda and meinauto.de); an exit on the 2022-25 lists. Its later state was not found.",
             "Consumer & Marketplaces"))
L.append(old("cember-net", "acquired", "Cember.net, a Turkish professional network (Istanbul, founded 2007). HV entered 2007-09; "
             "its later website points to xing.com: bought by XING. The round is not named.", "Consumer & Marketplaces"))
L.append(old("citydeal", "acquired", "Group-buying deals, Berlin (founded 2009-10). HV's entry is dated 2009-12-31; CityDeal "
             "raised a further EUR 5M in March 2010 (deutsche-startups) before Groupon bought it in May 2010 (OTS). HV's round "
             "is not named. Groupon, where HV's position ended up, is not a member (D4).", "Consumer & Marketplaces",
             rounds=[rnd("2010-03-17", None, None, None, None, gn("citydeal", "MEhPd3dhZg"))],
             extra={"status_citation": gn("citydeal", "a0cyWVk5Zg")}))
L.append(old("classmarkets", "unknown", "Classmarkets GmbH, Berlin (founded 2008), the operator of the property portal "
             "immobilo (the firm's 2015 nav: 'classmarkets/immobilo'). HV entered 2008-05; an exit on the 2022-25 lists. The "
             "old site's 'immobilo' row is this company (merge at the rebuild). Its later state was not found.",
             "Consumer & Marketplaces"))
L.append(old("cogny", "private", "AI document-analysis copilot for Excel, Paris (founded 2023). HV entered 2024 (Fund IX "
             "Ventures); no announcement names the round.", "AI & Applied AI"))
L.append(old("complyance", "private", "AI governance, risk and compliance platform, London (founded 2022). HV entered 2023 (Fund "
             "IX Ventures), before the $20M Series A led by GV of Feb 2026; HV's own round is not named.", "Security",
             rounds=[rnd("2026-02-11", "Series A", 20_000_000, "GV", True, gn("complyance", "k8zanJYMk0"))]))
L.append(cls("cuponation", status="private", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             country="DE", country_src="model_knowledge", city="Berlin", city_src="model_knowledge",
             note="Coupon portal (a Rocket Internet company), Berlin: HV's DropGifts investment of 2012 (the firm's own post of "
                  "2012-07-24) became CupoNation in 2013 ('CupoNation statt DropGifts', deutsche-startups 2013-11-18); the "
                  "old site's 'DropGifts' row is this company (merge at the rebuild). The round is not named.", rounds=[]))
L.append(old("dafiti", "acquired", "Latin American fashion e-commerce (a Rocket Internet company, Sao Paulo, founded 2010). HV "
             "entered 2011-12-30; folded into Global Fashion Group with lamoda, Namshi, Jabong and Zalora in 2014, its "
             "shareholders taking group shares. The round is not named.", "Consumer & Marketplaces"))
L.append(cls("dawanda", status="defunct", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("dawanda"),
             note="Handmade-goods marketplace, Berlin (founded 2006). HV entered 2007-02, the company's first year; the round "
                  "is not named. Closed in 2018 (Ecommerce News Europe, 2018-07-02).", rounds=[],
             extra={"status_citation": gn("dawanda", "VmFXbE5yZQ")}))
L.append(old("deutsche-startups", "private", "deutsche-startups.de, the Berlin startup news site (founded 2007). HV entered "
             "2007-05; still listed as a growth holding 2022-25. The round is not named.", "Media, Gaming & Advertising"))
L.append(cls("doinstruct", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("doinstruct", "YwVDZQRTB3"), entry_date="2025-03", focus="SaaS", **geo("doinstruct"),
             note="Training and compliance software for frontline workers, Berlin (founded 2021). HV entered at the EUR 16.5M "
                  "Series A of March 2025 (EU-Startups, found by the firm-name search; Startbase names the Series A), after "
                  "Creandum's EUR 7.6M seed of July 2024.",
             rounds=[rnd("2025-03-18", "Series A", 17_800_000, None, True, gn("doinstruct", "YwVDZQRTB3"))]))
L.append(old("doorfeed", "private", "Residential real-estate investment platform, Paris (founded 2021). HV entered 2024 (Fund IX "
             "Ventures), after the EUR 12M seed extension of Nov 2023; HV's round is not named.", "Fintech & Payments",
             rounds=[rnd("2023-11-23", "Seed extension", None, None, None, gn("doorfeed", "THBIY2JSTQ"))]))
L.append(old("draxon", "private", "VR training for airport ground operations, Berlin (founded 2025 by Westwing's Stefan Smalla). "
             "HV entered 2025 (Fund IX Ventures); Point Nine's card reads 'Seed 2025', but no announcement names HV's round.",
             "SaaS"))
L.append(old("dreamlines", "private", "Online cruise travel agency, Hamburg (founded 2012). HV entered 2013-10; the round is not "
             "named (EUR 45M Series E, May 2018, with HV, TechCrunch). Listed as a growth holding through 2025.",
             "Consumer & Marketplaces",
             rounds=[rnd("2018-05-08", "Series E", 55_000_000, None, True, gn("dreamlines", "dkphcTc4MQ"))]))
L.append(old("e-fellows-net", "private", "Online scholarship and career network for students, Munich (founded 2000). A "
             "corporate-era holding (entry 2000-09) listed as portfolio 2006-07 and former from 2011 (D2). The company "
             "operates; the round is not named.", "Consumer & Marketplaces"))
L.append(cls("easy-taxi", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             focus="Consumer & Marketplaces", **geo("easy-taxi", city="Rio de Janeiro"),
             note="Taxi-hailing app (a Rocket Internet company, Rio de Janeiro, founded 2012). HV entered in 2014 (Christian "
                  "Saller's deal; the Series D of July 2014, YourStory, the company's fourth round). Merged into Cabify in "
                  "2017; HV's resulting Cabify stake is not a member (D4).",
             rounds=[rnd("2014-07-30", "Series D", 15_000_000, None, None, gn("easy-taxi", "WI5MnV2SWs"))]))
L.append(old("eatfirst", "private", "Office food delivery, London and Berlin (a Rocket Internet company, founded 2014). HV "
             "entered in late 2014 (the firm's own post of 2015-01-30: 'Holtzbrinck Ventures investiert in EatFirst'), before "
             "the $8M Series A of Nov 2015. EatFirst bought Feedr from Compass Group in 2023.", "Consumer & Marketplaces"))
L.append(old("eating-with-the-chefs", "unknown", "Food delivery from chef kitchens, Berlin (founded 2015). HV entered 2015-04; "
             "an exit on the 2022-25 lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("enamora", "unknown", "Lingerie e-commerce, Berlin (founded 2008). HV entered 2008-05; an exit on the 2022-25 "
             "lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("epuls", "unknown", "Polish social network, Krakow (founded 2007). HV entered 2007-02; former portfolio from 2011. "
             "Its later state was not found.", "Consumer & Marketplaces"))
L.append(cls("erdbeerlounge", status="unknown", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             country="DE", country_src="model_knowledge", flags=["city_unknown"],
             note="A teen girls' online community on the 2011 current list (index.php?erdbeerlounge_en). Its later state was "
                  "not established.", rounds=[]))
L.append(old("erento", "acquired", "Rental marketplace, Berlin (founded 2003). HV entered 2006-12. acq. by VM Digital, 2011 (the "
             "firm's own post of 2011-06-22). The round is not named.", "Consumer & Marketplaces"))
L.append(old("everdine", "unknown", "Ready-meal delivery, London (founded 2016). HV entered 2016; an exit on the 2022-25 lists. "
             "Its later state was not found.", "Consumer & Marketplaces"))
L.append(cls("exein", status="private", rng="1b_plus", usd=1_700_000_000, val_src="web_verified",
             val_cite="https://techcrunch.com/2026/09/15/new-italian-unicorn-exein-rides-the-physical-ai-wave/",
             asof="2026-09-15", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("exein", "tqeTUteEF2"), entry_date="2025-12", focus="Security", **geo("exein"),
             note="Embedded cybersecurity for connected devices, Rome (founded 2018). HV entered at the EUR 100M round of Dec "
                  "2025 (tech.eu, found by the firm-name search; export 'growth', Fund IX Growth), after the Series B (2024) "
                  "and the EUR 70M Series C (July 2025). The $270M round of Sept 2026 valued it at $1.7B (TechCrunch, the "
                  "figure Balderton and Headline cite).",
             rounds=[rnd("2025-07-16", "Series C", 75_000_000, None, False, gn("exein", "aV92NkdsVQ")),
                     rnd("2025-12-18", None, 116_000_000, None, True, gn("exein", "tqeTUteEF2"))]))
L.append(old("experteer", "private", "Premium career service, Munich (founded 2005 with Holtzbrinck Ventures' support: "
             "Wikipedia; the firm's 2011 history names it among companies HV itself founded). An incubation, so no round is "
             "named. The company operates.", "Consumer & Marketplaces"))
L.append(cls("exporo", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("exporo", "U2cTlqZHRn"), entry_date="2016-07", focus="Fintech & Payments", **geo("exporo"),
             note="Real-estate crowd-investing platform, Hamburg (founded 2015). HV entered at the EUR 8.2M Series A of July "
                  "2016 (FinSMEs, found by the firm-name search; the firm's own entry date 2016-07-01).",
             rounds=[rnd("2016-07-13", "Series A", None, None, True, gn("exporo", "U2cTlqZHRn"))]))
L.append(old("fashion-for-home", "acquired", "Online furniture shop, Berlin (founded 2009). HV entered 2009-09-11 (the same "
             "date as Home24). acq. by Home24, 2015. The old site's 'fashion4home' rows are this company (merge at the "
             "rebuild). The round is not named.", "Consumer & Marketplaces",
             extra={"status_citation": gn("fashion-for-home", "NLY283aDJn")}))
L.append(cls("fettspielen-de", status="unknown", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             country="DE", country_src="model_knowledge", flags=["city_unknown"],
             note="A casual-games portal on the 2011 current list (index.php?fettspielen_en). Its later state was not "
                  "established.", rounds=[]))
L.append(cls("flinn", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("flinn", "29GaFZtRUU"), entry_date="2025", focus="Healthcare & Bio", **geo("flinn"),
             note="AI for medtech and pharma regulatory and quality workflows, Vienna (founded 2022). HV's entry (HV Entry "
                  "2025, Fund IX Ventures) is the EUR 17M ($20M) Series A announced 2026-02-19 (trendingtopics, found by the "
                  "firm-name search), after a EUR 1.8M pre-seed (2022) and a EUR 6M seed (2024).",
             rounds=[rnd("2022-12-20", "Pre-Seed", None, None, False, gn("flinn", "FNQk5HNTd3")),
                     rnd("2024-09-30", "Seed", None, "Speedinvest", False, gn("flinn", "EtGRkdwNFU")),
                     rnd("2026-02-19", "Series A", 20_000_000, None, True, gn("flinn", "29GaFZtRUU"))]))
L.append(cls("fmc", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("fmc", "NmandaMUVn"), entry_date="2025-11", focus="Industrial & Robotics",
             flags=["model_disputes_source"], **geo("fmc"),
             note="The Ferroelectric Memory Company, memory chips, Dresden (founded 2016). HV entered at the EUR 100M round of "
                  "Nov 2025 (tech.eu, found by the firm-name search; export 'growth', Fund IX Growth). The pre-filled public "
                  "$5.2B mark and Japan belong to a namesake (FMC Corp.) and are disputed; no priced valuation of the "
                  "Dresden company is published.",
             rounds=[rnd("2025-11-13", None, 116_000_000, None, True, gn("fmc", "NmandaMUVn"))]))
L.append(cls("fp-commerce", status="unknown", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             country="DE", country_src="model_knowledge", flags=["city_unknown"],
             note="An e-commerce company on the 2011 current list (index.php?fpcommerce_en). Its later state was not "
                  "established.", rounds=[]))
L.append(cls("framer", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified",
             val_cite="https://www.businesswire.com/news/home/20250828901842/en/Framer-Raises-$100-Million-Series-D-at-a-$2-Billion-Valuation-to-Redefine-How-Businesses-Build-Websites",
             asof="2025-08-28", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("framer", "JFZGJNX09o"), entry_date="2025-08", focus="SaaS", **geo("framer"),
             note="No-code website builder, Amsterdam (founded 2013). HV entered at the $100M Series D of Aug 2025 at a $2B "
                  "valuation (EU-Startups, found by the firm-name search; Business Wire; export 'growth', Fund IX Growth).",
             rounds=[rnd("2025-08-28", "Series D", 100_000_000, None, True, gn("framer", "JFZGJNX09o"))]))
write("batch-004", L)
