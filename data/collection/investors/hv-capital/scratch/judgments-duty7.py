"""Duty 7 (PRO-104): the blind 5% re-judge's disagreements, adjudicated on the blind judge's cited evidence."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, rnd, write, surfaces_lines, ASOF  # noqa: E402

U = ["unstable"]
ND = "https://www.northdata.de/"
L = [
    cls("hyperganic", status="defunct", rng="below_1b", flags=U,
        extra={"status_citation": "https://www.northdata.de/Hyperganic%20Group%20GmbH,%20M%C3%BCnchen/HRB%20262280"},
        note="Algorithmic engineering software for 3D printing, Munich. HV entered 2021-01 (Fund VIII) and co-led the $7.8M "
             "'first venture round' (3DPrint.com), which carries no round word. Wound down: the operating company Hyperganic "
             "Technologies GmbH has been in insolvency since 2025-02-27, the HV-held parent Hyperganic Group GmbH received a "
             "deletion notice on 2026-09-11 (North Data) and Hyperganic Pte. Ltd. is dissolved in a creditors' voluntary "
             "winding up. HV's export still lists it as active (duty 7 found it)."),
    cls("lendis", stage="Seed", stage_src="web_verified", stage_conf="high",
        stage_cite="https://nordic9.com/news/lendis-secures-a-seed-funding-round-from-hv-capital-dn-capital-and-picus-capital/",
        entry_date="2019-03", grad="graduated", grad_src="web_verified",
        grad_cite="https://web.archive.org/web/20221211204455/https://www.eu-startups.com/2022/01/berlin-based-lendis-bags-e80-million-to-scale-up-its-operating-system-for-hybrid-work/",
        flags=U,
        note="Workplace equipment as a service, Berlin (founded 2018). HV's entry is the seed of March/April 2019 with DN "
             "Capital and Picus (nordic9; deutsche-startups dealmonitor 2019-03-28); the EUR 80M Series A of Jan 2022 (EUR 30M "
             "equity, HV as an existing investor; EU-Startups) graduates the row.",
        rounds=[rnd("2019-04-12", "Seed", None, None, True,
                    "https://nordic9.com/news/lendis-secures-a-seed-funding-round-from-hv-capital-dn-capital-and-picus-capital/"),
                rnd("2022-01", "Series A", None, None, True,
                    "https://web.archive.org/web/20221211204455/https://www.eu-startups.com/2022/01/berlin-based-lendis-bags-e80-million-to-scale-up-its-operating-system-for-hybrid-work/")]),
    cls("charles", stage="Seed", stage_src="web_verified", stage_conf="high",
        stage_cite="https://web.archive.org/web/20220817021447/https://www.eu-startups.com/2022/07/berlin-based-charles-picks-up-e19-5-million-to-bring-conversational-commerce-to-europe/",
        entry_date="2021-03", grad="graduated", grad_src="web_verified",
        grad_cite="https://techcrunch.com/2022/07/20/charles-raises-20m-to-bring-conversational-commerce-to-whatsapp-in-europe/",
        flags=U,
        note="Conversational commerce on WhatsApp, Berlin (founded 2019). 'Accel and HV Capital, who led the company's seed "
             "round in 2021' (EU-Startups, 2022-07); the $20M Series A led by Salesforce Ventures (TechCrunch, 2022-07-20) "
             "graduates the row.",
        rounds=[rnd("2021-03", "Seed", 6_500_000, "Accel, HV Capital", True,
                    "https://web.archive.org/web/20220817021447/https://www.eu-startups.com/2022/07/berlin-based-charles-picks-up-e19-5-million-to-bring-conversational-commerce-to-europe/"),
                rnd("2022-07-20", "Series A", 20_000_000, "Salesforce Ventures", True,
                    "https://techcrunch.com/2022/07/20/charles-raises-20m-to-bring-conversational-commerce-to-whatsapp-in-europe/")]),
    cls("eating-with-the-chefs", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified",
        stage_conf="high",
        stage_cite="https://web.archive.org/web/20161021081154/http://www.gruenderszene.de/allgemein/eating-with-the-chefs-founders-fund-holtzbrinck",
        entry_date="2015-11", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
        surfaces=surfaces_lines("eating-with-the-chefs",
                                "the Nov 2015 seed only; the company shut down in Jan 2018 (a cited end)"),
        flags=U, city="Berlin", country="DE",
        extra={"status_citation": "https://www.deutsche-startups.de/2018/01/05/schade-eating-chefs-stellt-die-kueche-ab/"},
        note="Chef-cooked meal delivery (eating.de), Berlin (founded 2015). Founders Fund and Holtzbrinck 'investieren in der "
             "Seed-Runde einen Millionenbetrag' (Gruenderszene, Nov 2015). Shut down in Jan 2018 after failing to raise again "
             "(deutsche-startups, 2018-01-05), so the row did not graduate. The eatingpoint.be link on HV's archived page is "
             "an unrelated Belgian caterer.",
        rounds=[rnd("2015-11", "Seed", None, None, True,
                    "https://web.archive.org/web/20161021081154/http://www.gruenderszene.de/allgemein/eating-with-the-chefs-founders-fund-holtzbrinck")]),
    cls("musicplayr", status="defunct", rng="below_1b", flags=U,
        stage="Seed", stage_src="web_verified", stage_conf="high",
        stage_cite="https://www.ots.at/presseaussendung/OTS_20121022_OTS0123/holtzbrinck-ventures-investiert-500000-euro-in-musicplayrcom",
        extra={"status_citation": "https://www.northdata.de/Musicplayr+24%2F7+GmbH,+K%C3%B6ln/HRB+73292"},
        note="Web music-playlist app, Cologne (founded 2011). Musicplayr 'hat eine Seedfinanzierung von Holtzbrinck Ventures "
             "erhalten', EUR 500K (press release, 2012-10-22). Musicplayr 24/7 GmbH went into liquidation in Jan 2015 and was "
             "deleted in Nov 2016 (North Data); no later round."),
    cls("kyte", status="acquired", rng="below_1b", flags=U,
        extra={"status_citation": "https://www.sec.gov/Archives/edgar/data/1076700/000114420411004916/v209479_ex99-1.htm"},
        note="Kyte (kyte.com), the 2006 mobile and live video platform, San Francisco. Swisscom, Klaus Hommels and Holtzbrinck "
             "Ventures joined in 2007 after a $2.25M first round (GigaOm), with no round word. acq. by KIT digital, Jan 2011 "
             "(~$5.7M; KIT digital's 8-K exhibit). The old site's 'decentral.tv / kyte' row is this company. Not the 2021 "
             "car-rental startup Kyte."),
    cls("hitfox-group", status="private", rng="below_1b", flags=U,
        extra={"status_citation": "https://www.northdata.de/IONIQ%20Group%20GmbH,%20Berlin/Amtsgericht%20Charlottenburg%20(Berlin)%20HRB%20134757%20B"},
        note="Berlin company builder (Jan Beckers, founded 2011; HitFox Game Ventures, AppLift, FinLeap, Heartbeat Labs). "
             "Holtzbrinck Ventures backed it beside founder money (EU-Startups interview, 2013), with no round word. Renamed "
             "IONIQ Group GmbH in May 2019; it still files accounts (2024 accounts filed May 2026) and holds a Finleap stake."),
    cls("fettspielen-de", status="defunct", rng="below_1b", flags=U, country="DE", city="Karlsruhe",
        extra={"status_citation": "https://www.northdata.de/Rumble+Media+GmbH"},
        note="Casual web-games portal fettspielen.de, Karlsruhe, operated by FamilyOne GmbH (later Rumble Media GmbH). "
             "Holtzbrinck Ventures and European Founders Fund backed it (deutsche-startups, 2009-01-07), with no round "
             "word. The operator went into liquidation on 2018-08-16 and was deleted on 2020-08-26 (North Data); the domain "
             "now belongs to an unrelated company."),
    cls("b-cher-de", country="DE", city="Augsburg", flags=U,
        extra={"status_citation": "https://www.spiegel.de/wirtschaft/unternehmen/weltbild-droege-uebernimmt-verlagsgruppe-von-arndt-geiwitz-a-984420.html"},
        note="Online bookshop buecher.de, Augsburg (founded 1999). A corporate-era holding the unit listed under 'Exits' on its "
             "2006 site (D2); entry 1999-09, the round not named. Majority-owned by the Weltbild group by 2014 (Der Spiegel); "
             "the Augsburg KG went into insolvency in July 2024 and liquidation in Oct 2024."),
    cls("kipu-quantum", city="Berlin", flags=U,
        note="Quantum computing software, Berlin (founded in Karlsruhe; the registered seat moved to Berlin in May 2026, "
             "HRB 287200 B, per its imprint). HV's entry 2023-12-19 is the EUR 10.5M seed announced that day, led by HV "
             "Capital and DTCF (The Quantum Insider)."),
]
write("duty7-001", L)
