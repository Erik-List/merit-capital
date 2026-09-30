"""c13b: NEA queue batch 26, the 32 listed rows in queue/c26.json (classification only).
Run: NQ_TAG=c13 python3 judgments-c13b.py"""
import sys
import judge_lib as jl
from judge_lib import cls, rnd

HC, IR, DI, CM, MG, CE, FP, SA, SE, AI = ("Healthcare & Bio", "Industrial & Robotics", "Data Infrastructure",
                                          "Consumer & Marketplaces", "Media, Gaming & Advertising", "Climate & Energy",
                                          "Fintech & Payments", "SaaS", "Security", "AI & Applied AI")

SILK_TC = "https://techcrunch.com/2012/08/01/content-crunching-app-silk-raises-1-6-million-seed-round/"
SILK_TNW = "https://thenextweb.com/news/the-tnw-startup-rally-winner-silk-gets-funded-by-atomico"
UMAMI_TC = "https://techcrunch.com/2011/08/16/battery-ventures-and-nea-back-social-tv-app-umami/"
WEDDING_FI = "https://fi.co/insight/silicon-valley-grads-raise-1mm-seed-round-for-their-latest-venture-wedding-party"
TECTORA_Y = "https://finance.yahoo.com/healthcare/articles/schrodinger-establishes-tectora-therapeutics-ra-113301342.html"
WING = jl.W("The Wing (workspace)")
TARG = jl.FTS("Targacept", "S-1")
ACH = jl.FTS("Achaogen", "8-K")

L = [
    cls("sibeam-inc", status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined",
        focus=IR,
        note="Sunnyvale millimetre-wave chip company backed by USVP, NEA, Foundation Capital and Lux from 2004; Silicon "
             "Image bought it in April 2011 for $25.5M (Wikipedia). NEA's entry round is not named."),
    cls("silk", status="defunct", rng="below_1b", country="NL", country_src="web_verified", country_cite=SILK_TNW,
        city="Amsterdam", city_src="web_verified", stage="Seed", stage_src="web_verified", stage_cite=SILK_TC,
        stage_conf="high", entry_date="2012-08-01", focus=SA,
        rounds=[rnd("2011-05-18", "Seed", 475000, "Atomico", False, SILK_TNW, "press"),
                rnd("2012-08-01", "Seed", 1600000, "NEA", True, SILK_TC, "press")],
        note="Amsterdam structured-data publishing startup (silk.co, per The Next Web); NEA led its $1.6M seed round "
             "(TechCrunch, 2012-08-01). Palantir's 2016 deal was an acqui-hire with silk.co frozen, so it reads defunct "
             "as in the Atomico book; graduation left for the graduation pass."),
    cls("skyline-solar-inc", status="unknown", rng="below_1b", country="US", city="Mountain View",
        stage="undetermined", focus=CE,
        note="High-gain solar PV systems from Mountain View; the last record found is a US Department of Defense "
             "contract in January 2012 (PV Tech), so its later fate is not established. NEA's round is not named."),
    cls("snaptell-inc", status="acquired", rng="below_1b", country="US", city="Palo Alto", stage="undetermined",
        focus=AI,
        note="Image-recognition mobile product search from Palo Alto; Amazon's A9 unit bought it in 2009 (the firm's "
             "exit line: acquired by Amazon). NEA's 2006 entry round is not named."),
    cls("spinmedia", status="acquired", rng="below_1b", country="US", city="Los Angeles", stage="undetermined",
        focus=MG,
        note="BuzzMedia, renamed SpinMedia in 2013 (Los Angeles); after a 2014 assignment for the benefit of creditors "
             "its sites were sold off in 2016, so it reads acquired as in the Sutter Hill book. NEA's 2007 entry round is "
             "not named."),
    cls("storvisor", status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined",
        focus=DI,
        note="Storvisor renamed itself Springpath (the springpath row is the same company) and Cisco bought it in 2017, "
             "aligned with the Redpoint and Sequoia books. NEA's 2012 entry round is not named."),
    cls("svaya-nanotechnologies", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=IR,
        flags=["city_unknown"],
        note="Multifunction polymer films; the firm listed it as current and private through 2015 and no later record "
             "or location was found. NEA's 2009 entry round is not named."),
    cls("t-ram-semiconductor-inc", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=IR,
        flags=["city_unknown"],
        note="Fabless memory developer (thyristor RAM) on the firm's 2013 list; no record of its later fate or a "
             "sourced location was found, and no round is named."),
    cls("tabbedout", status="private", rng="below_1b", country="US", city="Austin", stage="undetermined", focus=FP,
        note="Austin mobile bar-tab payments company, since renamed Union, a point-of-sale business; the firm's union "
             "row ('Union (fka TabbedOut)') is the same company and still private. NEA's 2010 entry round is not named."),
    cls("tabula-inc", status="defunct", rng="below_1b", country="US", city="Santa Clara", stage="undetermined",
        focus=IR,
        note="Santa Clara 3-D FPGA maker that raised $215M and officially shut down on 2015-03-24 (Wikipedia), as in "
             "the Balderton, Benchmark and Greylock books; the Y Combinator row named Tabula (Berlin) is a different "
             "company."),
    cls("targacept", country="US", city="Winston-Salem", stage="Growth", stage_src="web_verified", stage_cite=TARG,
        stage_conf="high", entry_date="2002-11-26", focus=HC,
        rounds=[rnd("2002-11-26", "Series C", 59500000, None, True, TARG, "filing")],
        note="Targacept's 2004 S-1 shows New Enterprise Associates 10 buying $15M of the Series C convertible preferred "
             "sold from 2002-11-26, NEA's first round, so the entry is Growth. It merged with Catalyst Biosciences in "
             "2015 (now Gyre Therapeutics), and the catalyst-biosciences row is the same NEA position."),
    cls("targetrx-inc", status="acquired", rng="below_1b", country="US", city="Horsham", stage="undetermined",
        focus=HC,
        note="Pharmaceutical marketing-information company in Horsham, Pennsylvania; the firm's exit line says acquired "
             "by ImpactRx. NEA's entry round is not named."),
    cls("tectora-therapeutics", status="private", rng="below_1b", country="US", stage="Series A",
        stage_src="web_verified", stage_cite=TECTORA_Y, stage_conf="high", entry_date="2026-09-09", focus=HC,
        flags=["city_unknown"],
        rounds=[rnd("2026-09-09", "Series A", 55000000, "NEA and RA Capital", True, TECTORA_Y, "press")],
        note="Immunology biotech co-founded by Schrodinger with NEA and RA Capital, which co-led its $55M Series A "
             "(2026-09-09); it operates in stealth and no source gives its city."),
    cls("telsima-corporation", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
        stage="undetermined", focus=DI,
        note="WiMAX metro-access systems for the Indian telecom market, run from Sunnyvale with engineering in "
             "Bangalore; Airspan Networks bought it in 2009. NEA's entry round is not named."),
    cls("the-spectranetics-corporation", status="acquired", rng="below_1b", country="US", city="Colorado Springs",
        stage="undetermined", focus=HC,
        note="Excimer-laser catheter maker in Colorado Springs, bought by Philips in 2017. NEA's holding appears to "
             "come from Advanced Interventional Systems, which merged into Spectranetics in 1994 with NEA's Cornelius "
             "Bond on its board (2001 proxy), so the sale-consideration question (D8) is flagged."),
    cls("the-wing", status="defunct", rng="below_1b", country="US", city="New York", stage="Series A",
        stage_src="web_verified", stage_cite=WING, stage_conf="high", entry_date="2017-04", focus=CM,
        rounds=[rnd("2017-04", "Series A", 8000000, "NEA", True, WING, "press"),
                rnd("2017-11", "Series B", 32000000, "WeWork", None, WING, "press"),
                rnd("2018-12", "Series C", 75000000, "Sequoia Capital", True, WING, "press")],
        note="Women's coworking clubs in New York; NEA led the April 2017 Series A (Wikipedia) and joined Sequoia's $75M "
             "Series C in December 2018. IWG bought a majority in 2021 and the clubs closed in 2022, so it reads defunct "
             "as in the GV and Sequoia books."),
    cls("think3-inc", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=SA,
        flags=["city_unknown"],
        note="Mechanical design and product data management software on the firm's 2013 list; its later owner or fate "
             "was not established from a source, and no round is named."),
    cls("tract", status="private", rng="below_1b", country="US", stage="Seed", stage_src="web_verified",
        stage_cite=jl.NEWS("tract", "Tract Raises $7 Million"), stage_conf="high", entry_date="2022-09-15", focus=CM,
        flags=["city_unknown"],
        rounds=[rnd("2020", "unnamed", 2000000, None, False, jl.NEWS("tract", "Tract Raises $7 Million"), "press"),
                rnd("2022-09-15", "Seed", 7000000, "NEA", True, jl.NEWS("tract", "Tract Raises $7 Million"), "press")],
        note="Kids-teach-kids learning community co-founded by Esther Wojcicki; NEA led its $7M seed round (citybiz, "
             "2022-09-15), after $2M raised in 2020, matching the firm's own Seed label. No source gives its city; "
             "graduation left for the graduation pass."),
    cls("triquint-semiconductor-inc", country="US", city="Hillsboro", rng="below_1b", stage="undetermined",
        focus=IR,
        note="Gallium arsenide chip maker in Hillsboro, Oregon; it merged with RF Micro Devices into Qorvo on "
             "2015-01-01 (Wikipedia). NEA's historical round is not named."),
    cls("trishe", status="private", rng="below_1b", country="IN", country_src="web_verified",
        country_cite=jl.ARCH("trishe"), stage="Growth", stage_src="first_party", stage_cite=jl.ARCH("trishe"),
        stage_conf="medium", entry_date="2012", focus=CE, flags=["city_unknown"],
        note="Wind-energy developer that the firm's own page calls India's leading independent renewable energy "
             "developer; the firm labels the 2012 entry growth and listed the holding as current through 2020, the last "
             "record found."),
    cls("umami", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Seed",
        stage_src="web_verified", stage_cite=UMAMI_TC, stage_conf="high", entry_date="2011-08-16", focus=CM,
        rounds=[rnd("2011-08-16", "Seed", 1650000, None, True, UMAMI_TC, "press")],
        note="Social-TV companion app; it raised $1.65M in seed funding from Battery Ventures, NEA and angels "
             "(TechCrunch, 2011-08-16), and FOX bought it in 2013 as in the Battery book. Graduation left for the "
             "graduation pass."),
    cls("uni-power-group", status="private", rng="below_1b", country="CN", country_src="web_verified",
        country_cite=jl.ARCH("uni-power-group"), stage="undetermined", focus=FP, flags=["city_unknown"],
        note="Financial services for Chinese small and medium enterprises (the firm's own page), named in NEA's 2013 "
             "release on its China portfolio and listed as current and private through 2020, the last record found. "
             "NEA's 2008 entry round is not named."),
    cls("united-medical-plan", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=HC,
        flags=["city_unknown"],
        note="Independent practice association HMOs on the firm's 2013 historical list; the company could not be "
             "placed or its fate established."),
    cls("viavia", status="private", rng="below_1b", country="US", city="West Hollywood", stage="Seed",
        stage_src="first_party", stage_cite=jl.ARCH("viavia"), stage_conf="medium", entry_date="2021", focus=CM,
        note="Video social-commerce platform for Made in Italy fashion, run from West Hollywood as in the Headline "
             "book; the firm's own listing labels the 2021 entry Seed. Graduation left for the graduation pass."),
    cls("visual-edge-technology-inc", status="unknown", rng="below_1b", country="US", stage="undetermined",
        focus=IR, flags=["city_unknown"],
        note="Large-format copying systems sales and service on the firm's 2013 historical list; its location and "
             "fate were not established."),
    cls("waterbit", status="private", rng="below_1b", country="US", stage="Series A", stage_src="web_verified",
        stage_cite=jl.NEWS("waterbit", "WaterBit Raises $11.4m Series A"), stage_conf="high", entry_date="2018-06-26",
        focus=IR, flags=["city_unknown"],
        rounds=[rnd("2018-06-26", "Series A", 11400000, "NEA", True,
                    jl.NEWS("waterbit", "WaterBit Raises $11.4m Series A"), "press")],
        note="California autonomous-irrigation startup; NEA led its $11.4M Series A (AgFunderNews, 2018-06-26) and it "
             "named a new CEO in August 2021, the last record found. No source gives its city."),
    cls("wedding-party", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Seed",
        stage_src="web_verified", stage_cite=WEDDING_FI, stage_conf="high", entry_date="2013-02-21", focus=CM,
        rounds=[rnd("2013-02-21", "Seed", 1000000, "NEA and Felicis Ventures", True, WEDDING_FI, "press")],
        note="Wedding photo-sharing app; NEA and Felicis led its $1M seed round (Founder Institute, 2013-02-21), and it "
             "reads acquired as in the Felicis book. Graduation left for the graduation pass."),
    cls("wibidata", status="defunct", rng="below_1b", country="US", city="San Francisco", stage="Growth",
        stage_src="model", stage_conf="medium", entry_date="2012", focus=DI,
        note="Hadoop application company founded as Odiago in San Francisco; NEA led its $15M Series B in 2012, the "
             "firm's own first year. Wikipedia describes it in the past tense after 2014 layoffs and no later activity "
             "was found, so it reads defunct."),
    cls("ym-biosciences-inc", status="acquired", rng="below_1b", country="CA", country_src="web_verified",
        country_cite=jl.W("YM BioSciences"), city="Mississauga", stage="undetermined", focus=HC,
        note="Canadian drug developer listed in Toronto and New York; Gilead completed its acquisition in February 2013 "
             "for $510M (Wikipedia). NEA's round is not named."),
    cls("accelerated-networks-inc", status="acquired", rng="below_1b", country="US", city="Moorpark",
        stage="undetermined", focus=DI,
        note="Broadband access equipment maker in Moorpark, California (its 2000 annual report), with NEA's Peter "
             "Morris a director from May 1997; it merged with Occam Networks in 2002 under the Occam name, which Calix "
             "bought in 2011, so the occam-networks-inc row is the same line."),
    cls("achaogen-inc", country="US", city="South San Francisco", rng="below_1b", stage="Growth",
        stage_src="web_verified", stage_cite=ACH, stage_conf="high", entry_date="2016-06-01", focus=HC,
        note="NEA's first position is the June 2016 private placement into the already listed company (IPO 2014) "
             "through Growth Equity Opportunities Fund IV, with no earlier NEA private round found, so under X1 the row "
             "should be out; flagged. Achaogen filed Chapter 11 in April 2019 and sold its assets."),
    cls("advanced-switching-communications-inc", status="defunct", rng="below_1b", country="US", city="Vienna",
        stage="undetermined", focus=DI,
        note="Optical access equipment from Vienna, Virginia (its 2001 proxy), with NEA's Arthur Marks a director from "
             "September 1999; it listed in October 2000 and was wound down and dissolved in 2002, as in the TCV book. "
             "No round is named."),
]

if "--dry" in sys.argv:
    import json
    want = sorted(json.load(open("queue/c26.json"))["slugs"])
    got = sorted(x["slug"] for x in L)
    print(len(L), got == want, set(want) ^ set(got))
    sys.exit()
jl.write("c13b", L)
