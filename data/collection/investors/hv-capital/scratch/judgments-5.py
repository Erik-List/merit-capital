"""Batch 5 (PRO-104 grind, pass 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT, firm_cite  # noqa: E402

L = []


def geo(slug, city=None, country=None):
    c, ci, cite = hq(slug)
    return dict(country=country or c, country_cite=cite, city=city or ci)


def old(slug, status, note, focus, stage="undetermined", rounds=None, extra=None, **kw):
    g = geo(slug)
    g.update(kw.pop("geo", {}))
    return cls(slug, status=status, rng="below_1b", stage=stage, focus=focus, note=note, rounds=rounds or [],
               extra=extra, **{**g, **kw})


def bare(slug, status, note, focus):
    """An old-list row whose business or seat the record does not give."""
    return cls(slug, status=status, rng="below_1b", stage="undetermined", focus=focus, country="DE",
               country_src="model_knowledge", flags=["city_unknown"], note=note, rounds=[])


L.append(old("funanga", "unknown", "Prepaid payment cards, Berlin (founded 2009). HV entered 2013-10 with Global Savings Group "
             "(the firm's own post of 2013-11-15). Its later state was not found.", "Fintech & Payments"))
L.append(old("gameduell", "acquired", "Skill-games platform, Berlin (founded 2003). 'In 2004, GameDuell raised a funding round "
             "led by Holtzbrinck Ventures and Burda Digital Ventures' (Wikipedia), the round not named. acq. by Mobile Premier "
             "League, 2022 (Economic Times, 2022-02-28).", "Media, Gaming & Advertising",
             rounds=[rnd("2004", None, None, "Holtzbrinck Ventures, Burda Digital Ventures", True, "https://en.wikipedia.org/wiki/GameDuell")],
             extra={"status_citation": gn("gameduell", "VBQNkRoU1U")}))
L.append(old("glossybox", "acquired", "Beauty subscription boxes (a Rocket Internet company), Berlin (founded 2011). HV entered "
             "2011-05; the round is not named. acq. by The Hut Group, 2017 (Cosmetics Business, 2017-08-15).",
             "Consumer & Marketplaces", extra={"status_citation": gn("glossybox", "WUlGdDhIUQ")}))
L.append(old("gratispay", "acquired", "GratisPay, Berlin (founded 2009): the Samwer-backed virtual-currency payments business "
             "renamed SponsorPay and then Fyber (the firm's own record links fyber.com), bought by RNTS Media in 2014. HV "
             "entered 2009; the round is not named.", "Media, Gaming & Advertising"))
L.append(bare("gute-laune-tv", "unknown", "Gute Laune TV, a German pop and folk music TV channel the unit listed as portfolio "
              "2006-15 (entry 2005-09). Its later state was not established.", "Media, Gaming & Advertising"))
L.append(cls("habyt", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             country="DE", country_cite=EXPORT, city="Berlin", city_src="model_knowledge",
             note="Flexible housing and co-living platform, Berlin (founded 2016; the firm's HQ field reads Frankfurt, "
                  "homefully's seat). HV's own entry is 2017 (Fund VI), separate from its homefully position (2018), which "
                  "Habyt bought in June 2021 with its EUR 20M Series B; Common's 2023 merger release lists HV Capital among "
                  "Habyt's investors. HV's 2017 round is not named. Series C EUR 40M (Oct 2023); Mitsubishi Estate bought its "
                  "co-living property portfolio in 2026, not the company.",
             rounds=[rnd("2021-06-17", "Series B", 24_000_000, None, None, gn("habyt", "zNOZW93eHU")),
                     rnd("2023-10-05", "Series C", 42_000_000, None, None, gn("habyt", "Z2h2NG8tUw"))]))
L.append(old("hades", "private", "Laser drilling for critical minerals and geothermal energy, Munich (founded 2025). HV entered "
             "2025 (Fund IX Ventures); no announcement names the round.", "Climate & Energy"))
L.append(old("hitfox-group", "unknown", "Berlin company builder (Jan Beckers, founded 2011; HitFox Game Ventures, AppLift, later "
             "FinLeap and Heartbeat Labs). HV entered 2011-07; its later corporate state was not established.",
             "Media, Gaming & Advertising"))
L.append(cls("holy", status="private", rng="below_1b", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=EXPORT, entry_date="2025", focus="Consumer & Marketplaces", **geo("holy"),
             note="Functional powdered drinks brand, Berlin (founded 2020). HV entered in 2025 (Fund IX Growth; export "
                  "'growth'), after the EUR 10.5M Series A of Aug 2023 (FinSMEs, FoodBev), so a later round.",
             rounds=[rnd("2023-08-24", "Series A", 11_400_000, None, False, gn("holy", "eC1IMkhDbg"))]))
L.append(old("homefully", "acquired", "Serviced flat-share homes, Frankfurt (founded 2016). HV entered 2018 (Fund VI). acq. by "
             "Habyt, 2021 (EU-Startups, 2021-06-17). The round is not named.", "Consumer & Marketplaces",
             extra={"status_citation": gn("homefully", "zNOZW93eHU")}))
L.append(old("imagekind", "acquired", "Custom art-print marketplace, US (founded 2006). HV entered 2007-02, the $2.6M round "
             "announced that month, not named as a series. acq. by CafePress, 2008.", "Consumer & Marketplaces"))
L.append(old("immo", "unknown", "IMMO Investment Technologies, residential property fintech, London (founded 2017). HV "
             "entered 2017-07-28, before the EUR 11M Series A of Nov 2019 (TechCrunch, found by the firm-name search); HV's "
             "round is not named. An exit on the 2022-25 lists; its later state was not found.", "Fintech & Payments",
             rounds=[rnd("2019-11-07", "Series A", 12_000_000, None, True, gn("immo", "c3NVBkMV9o"))]))
L.append(old("immowelt", "acquired", "Property portal immowelt, Nuremberg (founded 1999). A corporate-era holding (entry 2000-06) "
             "listed under 'Exits' from 2006 (D2). Axel Springer took full ownership in 2019. The round is not named.",
             "Consumer & Marketplaces", extra={"status_citation": gn("immowelt", "bUQ0a24tdw")}))
L.append(old("informed", "private", "informed.so, US (the archived list: San Francisco; founded 2020). HV entered 2022-06-24 "
             "(Fund VIII); no announcement names the round.", "Fintech & Payments"))
L.append(cls("infoseek", status="acquired", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
             country="DE", country_src="model_knowledge", flags=["city_unknown", "model_disputes_source"],
             note="Infoseek's German search portal: the unit's 2006 exits page: 'Central to Infoseek was a comprehensive "
                  "information and search portal ... The business was integrated into a shareholder group'. Not the US "
                  "Infoseek Corporation that Battery and Menlo hold (the pre-filled US country is disputed).", rounds=[]))
L.append(old("innofact", "private", "Online market research, Duesseldorf (founded 2000). HV entered 2001-05; listed as portfolio "
             "2006-15, an exit on the 2022-25 lists. The company operates; the round is not named.", "SaaS"))
L.append(old("internations", "acquired", "Expat network, Munich (founded 2007). HV entered 2007-08. acq. by XING, 2017 (Horizont); "
             "sold on to FairCap in 2026. The round is not named.", "Consumer & Marketplaces",
             extra={"status_citation": gn("internations", "Hl4NkVsTVE")}))
L.append(old("jabong", "acquired", "Indian fashion e-commerce (a Rocket Internet company, founded 2012). HV entered 2012-12-31; "
             "via Global Fashion Group, sold to Flipkart's Myntra in 2016 ($70M). The round is not named.",
             "Consumer & Marketplaces", extra={"status_citation": gn("jabong", "Bna3c5YUdn")}))
L.append(old("januus", "private", "Crypto intelligence linking wallets to real-world identities, London (founded 2021). HV "
             "entered 2021 (Fund VIII); no announcement names the round.", "Crypto & Web3"))
L.append(old("jetlore", "acquired", "AI predictive marketing, Sunnyvale (founded 2011). HV entered 2013-07; the round is not named. "
             "acq. by PayPal, 2018.", "AI & Applied AI", extra={"status_citation": gn("jetlore", "STZXaUJ4bw")}))
L.append(old("jobline-de", "acquired", "Career and job portal jobline.de, Hamburg: a corporate-era holding (entry 1999) under "
             "'Exits' on the unit's 2006 site, which says Jobline 'was one of the leading career and job portals'. Sold on; "
             "the round is not named.", "Consumer & Marketplaces"))
L.append(bare("jobmensa", "unknown", "Jobmensa, the student-jobs portal on the 2011 current list; the firm's 2012 post pairs it "
              "with Studitemps ('das Konzept von Jobmensa und Studitemps funktioniert'). Whether it is a separate company or "
              "the Studitemps (jobvalley) portal was not established.", "Consumer & Marketplaces"))
L.append(old("kissnofrog", "unknown", "Video speed-dating, Hamburg (founded 2007). HV entered 2008-02; an exit on the 2022-25 "
             "lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("kiveda", "private", "Online kitchen retailer, Berlin (founded 2012). HV entered 2012-11 (the firm's post of "
             "2014-02-12: 'Kiveda erhaelt Millionenbetrag'); bought Kuechen Quelle in 2014; still a growth holding 2022-25. "
             "The round is not named.", "Consumer & Marketplaces"))
L.append(old("kyte", "unknown", "Kyte (kyte.com, the 2006 mobile video platform, San Francisco): HV entered 2007-03 in the $15M "
             "of strategic investments of Dec 2007 (eleconomista, found by the firm-name search). The old site's "
             "'decentral.tv / kyte' row is this company (merge at the rebuild). Not the 2021 car-rental startup Kyte. Its "
             "later state was not found.", "Media, Gaming & Advertising",
             rounds=[rnd("2007-12-20", None, 15_000_000, None, True, gn("kyte", "1J4dlg4ang"))]))
L.append(bare("l-arcobaleno", "unknown", "L'Arcobaleno, a luxury design marketplace HV joined in 2013 (the firm's own post of "
              "2013-07-31); on the 2015 current list. Its later state was not established.", "Consumer & Marketplaces"))
L.append(old("lamoda-ru", "acquired", "Russian fashion e-commerce (a Rocket Internet company, founded 2011). HV entered 2011-12-31; "
             "folded into Global Fashion Group, which sold Lamoda to Sheldon in 2023. The round is not named.",
             "Consumer & Marketplaces"))
L.append(old("lap-coffee", "private", "Specialty coffee chain, Berlin (founded 2023). HV entered 2024 (Fund IX Ventures); no "
             "announcement names the round.", "Consumer & Marketplaces"))
L.append(old("lendico", "acquired", "Peer-to-peer lending marketplace (a Rocket Internet company), Berlin (founded 2013). HV "
             "entered 2014-03 (Sven Achter). ING bought the German business in 2018. The round is not named.",
             "Fintech & Payments"))
L.append(old("linio", "acquired", "Latin American marketplace (a Rocket Internet company), Mexico City (founded 2012). HV "
             "entered 2012; acq. by Falabella, 2018 ($138M, LatamList). The round is not named.", "Consumer & Marketplaces",
             extra={"status_citation": gn("linio", "Gw5WUppVmg")}, geo={"city": "Mexico City", "country": "MX"}))
L.append(old("locafox", "unknown", "Local-retail stock search, Berlin (founded 2013). HV entered 2013-09; an exit on the 2022-25 "
             "lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("loots", "unknown", "Loots, Berlin (founded 2016). HV entered 2018-04; an exit on the 2022-25 lists. Its business "
             "and later state were not established.", "Consumer & Marketplaces"))
L.append(bare("mamily", "unknown", "Mamily, a family community on the 2008-10 site, under 'Former Investments' in 2011. Its later "
              "state was not established.", "Consumer & Marketplaces"))
L.append(old("meinauto", "acquired", "Online new-car broker meinauto.de, Cologne (founded 2007). HV entered 2007-09; sold on (Hg "
             "owned MeinAuto Group by 2021). The round is not named.", "Consumer & Marketplaces"))
L.append(old("mercavus", "unknown", "Mercavus, Berlin (founded 2018). HV entered 2019-05; an exit on the 2022-25 lists. Its "
             "later state was not found.", "SaaS"))
L.append(old("meshcapade", "acquired", "AI digital humans and motion capture, Tuebingen (founded 2018). HV entered 2025 (Fund IX "
             "Ventures); the round is not named. acq. by Epic Games, 2026 (80 Level, 2026-02-24).", "AI & Applied AI",
             extra={"status_citation": gn("meshcapade", "lRyQ2s5R3c")}))
L.append(cls("midas", status="private", rng="below_1b", stage="undetermined", focus="Crypto & Web3",
             flags=["model_disputes_source"], **geo("midas"),
             note="Tokenised investment products (mTBILL), Berlin (founded 2020). HV entered at the $8.75M round of March 2024 "
                  "(Axios, found by the firm-name search), not named as a series in the headline; RRE and Creandum led the "
                  "$50M Series A of March 2026. Not the Turkish brokerage Midas that Spark Capital holds; the pre-filled "
                  "'acquired' and GB belong to namesakes and are disputed.",
             rounds=[rnd("2024-03-28", None, 8_750_000, None, True, gn("midas", "M1p0cXR5Zw")),
                     rnd("2026-03-30", "Series A", 50_000_000, "RRE, Creandum", True, gn("midas", "BQVkhkMG42"))]))
L.append(old("milleporte", "unknown", "Milleporte, Tokyo (founded 2010). HV entered 2010-02; an exit on the 2022-25 lists. Its "
             "business and later state were not established.", "Consumer & Marketplaces"))
L.append(old("mobileview", "unknown", ":mobileview AG, mobile information software, Hamburg (founded 2001). 'Holtzbrinck "
             "Ventures participated in Mobileview AG from 2001 - October 2006' with Credit Suisse and Techinvest (the unit's "
             "2007 page). Its later state was not found.", "SaaS"))
L.append(cls("mondoo", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2024", focus="Security", **geo("mondoo"),
             note="Exposure and vulnerability management, founded in Berlin 2019 (the firm's HQ field: San Francisco). HV "
                  "entered in 2024 (Fund IX Ventures), after the $12M Series A Atomico led in Oct 2021, so in a later round; "
                  "HV was in the $17.5M round of Sept 2025 (Business Wire, found by the firm-name search).",
             rounds=[rnd("2021-10-05", "Series A", 12_000_000, "Atomico", False, "https://tech.eu/2021/10/05/bringing-devops-and-security-teams-together-mondoo-raises-12-million-in-atomico-led-round/"),
                     rnd("2025-09-30", None, 17_500_000, None, True, gn("mondoo", "kxMEI0TERn"))]))
L.append(old("mopay", "acquired", "mopay AG, carrier billing and mobile payments, Munich: MindMatics (founded 2000) renamed mopay; "
             "HV entered 2001-12 (the same record as the old site's 'MindMatics' rows, merged at the rebuild). acq. by Boku, "
             "2014 (TechCrunch, 2014-10-07; the firm's own post). The round is not named. Boku, where HV's position ended "
             "up, is not a member (D4).", "Fintech & Payments"))
write("batch-005", L)
