"""c13a: NEA queue batch 25 (listed members, classification only). Run: NQ_TAG=c13 python3 judgments-c13a.py"""
import judge_lib as jl
from judge_lib import cls, rnd

HC, IR, DI, CM, MG, CE, FP, SA, SE, AI = ("Healthcare & Bio", "Industrial & Robotics", "Data Infrastructure",
                                          "Consumer & Marketplaces", "Media, Gaming & Advertising", "Climate & Energy",
                                          "Fintech & Payments", "SaaS", "Security", "AI & Applied AI")

MODE_PR = "https://www.prnewswire.com/news-releases/mode-emerges-from-stealth-with-24-million-in-venture-funding-and-a-new-class-of-private-network-for-enterprise-300660534.html"
REWIND_TC = "https://techcrunch.com/2024/04/17/a16z-backed-rewind-pivots-to-build-ai-powered-pendant-to-record-your-conversations/"
POSITRON_PR = "https://www.prnewswire.com/news-releases/positron-ai-raises-875-million-at-a-5-billion-valuation-to-bring-its-next-generation-inference-silicon-to-market-302874601.html"
POSITRON_PRESS = "https://www.positron.ai/press"
SMIC_CAP = "https://companiesmarketcap.com/smic/marketcap/"
MEDRC_SITE = "https://www.medisysevarsity.com/about-medrc-edutech/"
MEDRC_VENDOR = "https://www.cbinsights.com/company/medrc-edutech-funding"
REZNEXT_SI = "https://www.siliconindia.com/cover-story/reznext-global-solutions-an-intelligent-distribution-platform-to-demystify-distribution-for-hoteliers--nwid-1676.html"
RECCE_TC = "https://techcrunch.com/2012/07/13/recce-a-rich-interactive-map-thats-also-a-gaming-platform-launches-with-4m-from-nea/"
REZNEXT_MN = "https://www.medianama.com/2014/12/223-reznext-raises-5-million-from-nea/"

L = [
    cls("lytro", city="Mountain View", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
        entry_date="2011-06", focus=CM,
        note="NEA led Lytro's $50M Series B announced in June 2011 (the firm's own year 2010 reads as the close), so the "
             "entry is Growth on that named round. Lytro ceased operations in March 2018 with staff moving to Google "
             "(Wikipedia); status stays the prefilled defunct."),
    cls("marathon-health", status="private", rng="below_1b", country="US", city="Indianapolis", stage="Growth",
        stage_src="first_party", stage_cite=jl.SITE("marathon-health"), stage_conf="medium", entry_date="2018",
        focus=HC,
        note="The firm's 2018 Growth year matches its May 2018 purchase of Paladina Health from DaVita; Paladina became "
             "Everside Health, which merged with Marathon Health in February 2024 under the Marathon name (PR Newswire, "
             "2024-02-08), so this page is read as the same NEA position as the paladina-health and everside-health rows. "
             "No priced mark is published."),
    cls("maxiscale-inc", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=DI,
        flags=["city_unknown"],
        note="Infrastructure software for web 2.0 companies, on the firm's 2013 historical list only; no later record "
             "of the company, its location or its fate was found, and no round is named."),
    cls("mayhem", status="acquired", rng="below_1b", country="US", city="Pittsburgh", stage="Series A",
        stage_src="model", stage_conf="medium", entry_date="2018-11", focus=SE,
        rounds=[rnd("2018-11", "Series A", 15000000, "NEA", True, None, "filing"),
                rnd("2022-03-21", "Series B", 21000000, "Koch Disruptive Technologies and NEA", True,
                    jl.NEWS("mayhem", "ForAllSecure Raises"), "company")],
        note="Mayhem Security, formerly ForAllSecure (Pittsburgh; the forallsecure row is the same company), was bought "
             "by Bugcrowd on 2025-11-04. NEA entered at the $15M Series A (Form D first sale 2018-11-20, Aaron Jacobson "
             "director), the only round before the $21M Series B NEA co-led in March 2022, which took total funding to "
             "$36M (the company's release)."),
    cls("mecommerce", status="defunct", rng="below_1b", country="US", stage="undetermined", focus=CM,
        flags=["city_unknown"],
        note="Personalized e-commerce startup the firm listed only in 2013; the Felicis book reads it defunct and no "
             "later record, location or named round was found."),
    cls("medrc-edutech", status="private", rng="below_1b", country="IN", country_src="web_verified",
        country_cite=MEDRC_SITE, city="Hyderabad", city_src="web_verified", stage="undetermined", focus=HC,
        rounds=[rnd("2013-02-09", "Series A", 5000000, None, True, MEDRC_VENDOR, "vendor")],
        note="Hyderabad medical-education company (its own site), now listed by the firm as MediSys EduTech, so the "
             "medisys-edutech row is the same company. Only a vendor dates a $5M Series A with NEA in February 2013, "
             "which cannot cite, so the stage stays undetermined."),
    cls("microwave-technology-inc", status="acquired", rng="below_1b", country="US", city="Fremont",
        stage="undetermined", focus=IR,
        note="Fremont maker of gallium arsenide amplifiers (MwT), bought by IXYS in 2008. No round is named for NEA's "
             "historical entry."),
    cls("mode", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
        focus=DI, flags=["model_disputes_source"],
        rounds=[rnd("2017", "Series A", 8000000, "NEA", True, MODE_PR, "company"),
                rnd("2018-06-07", "Series B", 16000000, "GV", None, MODE_PR, "company")],
        note="Mode (mode.net, cloud private network, San Francisco) closed an $8M Series A led by NEA in 2017 and a $16M "
             "Series B led by GV (company release, 2018-06-07), but the firm's own first-investment year is 2015, so the "
             "entry round is not established; VMware bought it in 2020 (the GV book). The prefilled GB is a one-word "
             "Wikidata join."),
    cls("move-guides", status="acquired", rng="below_1b", country="US", city="Denver", stage="undetermined",
        focus=SA,
        note="MOVE Guides renamed itself Topia (the topia row is the same company); Bow River Capital completed a "
             "majority recapitalization on 2025-06-25 and Topia now runs from its new global headquarters in Denver "
             "(PR Newswire). NEA's October 2014 announcement does not name the round."),
    cls("narrativ", status="private", rng="below_1b", country="US", city="New York", stage="Seed",
        stage_src="first_party", stage_cite=jl.ARCH("narrativ"), stage_conf="medium", entry_date="2015", focus=MG,
        note="Commerce-recommendation platform later renamed Howl (the howl row is the same company); the firm's own "
             "listing labels the 2015 entry Seed. Howl sold its creator business to Taboola's commerce arm in September "
             "2026 (ADWEEK) and otherwise operates; graduation left for the graduation pass."),
    cls("nationwide-remittance-centers", status="acquired", rng="below_1b", country="US", stage="undetermined",
        focus=FP, flags=["city_unknown"],
        note="1986 consumer-payment processing network; the firm's exit line says acquired by Financial Telesis while "
             "its archived page said Cashflex. The nrc row is the same company (the live page is /portfolio/nrc)."),
    cls("nazomi-communications-inc", status="unknown", rng="below_1b", country="US", city="Santa Clara",
        stage="undetermined", focus=IR,
        note="Santa Clara fabless maker of Java and multimedia application processors for handset makers, on the "
             "firm's 2008 historical list; its later fate as an operating company was not established."),
    cls("nephrolife", status="acquired", rng="below_1b", country="IN", country_src="web_verified",
        country_cite=jl.ARCH("nephrolife"), stage="undetermined", focus=HC, flags=["city_unknown"],
        note="Indian renal-care chain that the firm's own page calls India's first holistic renal disease management "
             "centre, with the exit line acquired by DaVita. NEA's 2011 entry round is not named and no source places "
             "its city."),
    cls("nordic-windpower", status="defunct", rng="below_1b", city="Kansas City", stage="undetermined", focus=CE,
        rounds=[rnd("2010-05-18", "Series C", 38000000, "Khosla Ventures", True,
                    jl.NEWS("nordic-windpower", "raises $38"), "press")],
        note="Two-bladed wind turbines; the company moved from Berkeley to Kansas City and filed for liquidation in "
             "October 2012 (Wikipedia). NEA was in the May 2010 Series C led by Khosla, but its first round is not "
             "named."),
    cls("nova-medical-centers", status="acquired", rng="below_1b", country="IN", country_src="web_verified",
        country_cite=jl.ARCH("nova-medical-centers"), stage="undetermined", focus=HC, flags=["city_unknown"],
        note="The day-care surgical chain the firm describes was bought by Apollo Hospitals' Apollo Health and Lifestyle "
             "arm in January 2015 for about $24M (VCCircle) and rebranded Apollo Spectra; the firm's page still read "
             "private in 2023. NEA's 2010 entry round is not named."),
    cls("novatorque", status="acquired", rng="below_1b", country="US", city="Fremont", stage="undetermined",
        focus=IR,
        note="High-efficiency electric motors, Fremont; Regal Beloit bought its assets in 2016 (aligned with the Menlo "
             "book). NEA's 2008 entry round is not named."),
    cls("nrc", country="US", rng="below_1b", stage="undetermined", focus=FP, flags=["city_unknown"],
        note="Same company as the nationwide-remittance-centers row (consumer payment processing, NEA 1986). Its "
             "prefilled data came from a weak EDGAR join to an issuer public since 2017, a different company; the "
             "acquired status stands on the firm's own exit line."),
    cls("nurien-soft-ltd", status="acquired", rng="below_1b", country="KR", country_src="web_verified",
        country_cite=jl.NEWS("nurien-soft-ltd", "raises $15 million"), city="Seoul", stage="Series A",
        stage_src="web_verified", stage_cite=jl.NEWS("nurien-soft-ltd", "raises $15 million"), stage_conf="medium",
        entry_date="2008-04-22", focus=MG,
        rounds=[rnd("2008-04-22", "first venture round", 15000000, None, True,
                    jl.NEWS("nurien-soft-ltd", "raises $15 million"), "press")],
        note="Korean 3D social networking and online game company; GamesBeat (2008-04-22) reports its $15M first round "
             "of venture capital with NEA among four investors, read as the Series A. The firm's exit line says "
             "acquired by Infolink Global."),
    cls("occupational-health-rehab", status="acquired", rng="below_1b", country="US", city="Hingham",
        stage="undetermined", focus=HC,
        note="Occupational Health + Rehabilitation Inc (Nasdaq: OHRI), work-injury clinics run from Hingham, "
             "Massachusetts, bought by Concentra in 2005. NEA's entry round is not named."),
    cls("pacificdental-benefits-inc", status="unknown", rng="below_1b", country="US", stage="undetermined",
        focus=HC, flags=["city_unknown"],
        note="California and Nevada dental HMO on the firm's 2013 historical list; its fate and headquarters could not "
             "be established."),
    cls("paladina-health", status="private", rng="below_1b", country="US", city="Indianapolis", stage="Growth",
        stage_src="web_verified", stage_cite=jl.FTS("Everside Health", "DRS/A"), stage_conf="high",
        entry_date="2018-05-24", focus=HC,
        note="NEAPH Acquisitionco, an NEA vehicle, bought Paladina Health from DaVita under an Equity Purchase Agreement "
             "of 2018-05-24 (Everside Health's 2021 registration, exhibit 10.14), a buyout-scale entry; the control "
             "question (R1) is flagged. Paladina became Everside Health and merged with Marathon Health in February 2024 "
             "under the Marathon name, so it operates privately as Marathon Health (the everside-health and "
             "marathon-health rows)."),
    cls("paysa", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
        stage_cite=jl.ARCH("paysa"), stage_conf="medium", entry_date="2015", focus=CM, flags=["city_unknown"],
        note="Salary-benchmarking platform for employees launched in February 2016; the firm's own listing labels the "
             "2015 entry Seed and still showed it current in 2020, the last record found. Graduation left for the "
             "graduation pass."),
    cls("peptimmune-inc", status="unknown", rng="below_1b", country="US", city="Cambridge", stage="undetermined",
        focus=HC,
        note="Cambridge, Massachusetts clinical-stage autoimmune biotech on the firm's 2013 list; its later fate was "
             "not established from a source, and no round is named."),
    cls("pixelberry", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="undetermined",
        focus=MG,
        note="Mountain View studio behind the story game Choices, bought by Nexon in 2017 and by Series Entertainment "
             "in 2024 (Wikipedia). NEA's entry round is not named."),
    cls("pmc-sierra-inc", country="US", city="Sunnyvale", rng="below_1b", stage="undetermined", focus=IR,
        note="Broadband communications chips; Microsemi completed its acquisition on 2016-01-15 (Wikipedia). City "
             "aligned with the Sequoia book; NEA's round is not named."),
    cls("positron-ai", status="private", rng="1b_plus", usd=5000000000, val_src="web_verified", val_cite=POSITRON_PR,
        asof="2026-09-10", country="US", city="Reno", stage="Growth", stage_src="web_verified",
        stage_cite=POSITRON_PR, stage_conf="high", entry_date="2026-09-10", focus=IR,
        extra={"valuation_range_source": "web_verified"},
        rounds=[rnd("2025-07", "Series A", 51600000, None, False, POSITRON_PRESS, "company"),
                rnd("2026-02", "Series B", 230000000, None, False, POSITRON_PRESS, "company"),
                rnd("2026-09-10", "Series C", 875000000, "NEA, Atreides, Valor, Andra, SemiAnalysis Capital, Jim Clark",
                    True, POSITRON_PR, "company")],
        note="NEA co-led Positron's $875M Series C at a $5B post-money valuation (Reno dateline, 2026-09-10), its first "
             "round in the company per the firm's own post announcing its Series C lead. Momentum check 2026-09-30: the "
             "Series C itself is the $1B+ priced round."),
    cls("primary-health-inc", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=HC,
        flags=["city_unknown"],
        note="Integrated insurer, provider network and administrator on the firm's 2013 list; the company could not be "
             "placed or its fate established."),
    cls("primax-recoveries-inc", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=HC,
        flags=["city_unknown"],
        note="Subrogation and overpayment recovery services for health payers, on the firm's 2008 historical list; its "
             "location and fate were not established."),
    cls("protostar-ltd", status="acquired", rng="below_1b", country="US", city="San Francisco",
        stage="undetermined", focus=DI,
        note="Bermuda-incorporated satellite operator run from San Francisco and Singapore; it filed Chapter 11 on "
             "2009-06-29 and its satellites were auctioned, ProtoStar I to Intelsat for $210M (Wikipedia), so it reads "
             "acquired on the asset-sale rule. The Bermuda incorporation is a haven and falls through to its San "
             "Francisco operations."),
    cls("provation-medical-inc", status="acquired", rng="below_1b", country="US", city="Minneapolis",
        stage="undetermined", focus=HC,
        note="Minneapolis procedure-documentation software company, bought by Wolters Kluwer Health and later sold to "
             "Fortive in 2018. NEA's entry round is not named."),
    cls("qbotix", status="defunct", rng="below_1b", country="US", city="Menlo Park", stage="Seed",
        stage_src="first_party", stage_cite=jl.ARCH("qbotix"), stage_conf="medium", entry_date="2011", focus=CE,
        note="Menlo Park maker of robots that turn solar panels; it shut down in August 2015 after raising about $25M "
             "(Fortune, 2015-09-22), none of it named by series. The firm's own listing labels the 2011 entry Seed; "
             "graduation left for the graduation pass."),
    cls("qpex-bipharma", status="acquired", rng="below_1b", country="US", city="San Diego", stage="Series A",
        stage_src="web_verified", stage_cite=jl.NEWS("qpex-bipharma", "Closing of $33 Million Series A"),
        stage_conf="high", entry_date="2018-10-22", focus=HC,
        rounds=[rnd("2018-10-22", "Series A", 33000000, "NEA", True,
                    jl.NEWS("qpex-bipharma", "Closing of $33 Million Series A"), "company")],
        note="San Diego antibiotics developer that launched with a $33M Series A led by NEA (company release, "
             "2018-10-22); Shionogi bought it for about $140M in June 2023."),
    cls("quantum-medical-systems", status="acquired", rng="below_1b", country="US", city="Issaquah",
        stage="undetermined", focus=HC,
        note="Issaquah, Washington ultrasound maker bought by Siemens in 1989, the root of Siemens' ultrasound "
             "business. NEA's entry round is not named."),
    cls("quicklogic", country="US", city="San Jose", stage="undetermined", focus=IR,
        note="FPGA maker listed on Nasdaq (QUIK), San Jose, aligned with the Sequoia book. The firm's own year is 1995 "
             "with the anchor label early; no round is named."),
    cls("rapid-robotics", status="private", rng="below_1b", country="US", city="San Francisco", stage="Series A",
        stage_src="first_party", stage_cite=jl.POST("rise-of-the-rapid-robots"), stage_conf="high",
        entry_date="2021-04-06", focus=IR,
        rounds=[rnd("2020-11", "Seed", None, None, False, None, "press"),
                rnd("2021-04-06", "Series A", 12000000, None, True, jl.POST("rise-of-the-rapid-robots"), "firm"),
                rnd("2021-08-18", "Series B", None, "Kleiner Perkins and Tiger Global", None, None, "press")],
        note="NEA's own post of 2021-04-06 announces its Series A investment in the $12M round, after a seed NEA was "
             "not named in; Kleiner Perkins and Tiger Global led the Series B in August 2021 and the company still "
             "operates (new CEO July 2024)."),
    cls("reachify", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
        stage_cite=jl.ARCH("reachify"), stage_conf="medium", entry_date="2017", focus=SA, flags=["city_unknown"],
        note="Brand-technology intelligence platform; the firm's own listing labels the 2017 entry Seed and later marks "
             "the holding historic, and a June 2023 release shows the company still hiring. Graduation left for the "
             "graduation pass."),
    cls("realtime-worlds-inc", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
        country_cite=jl.W("Realtime Worlds"), city="Dundee", stage="undetermined", focus=MG,
        rounds=[rnd("2006-12-11", "unnamed", 30000000, "NEA", True, jl.W("Realtime Worlds"), "press"),
                rnd("2008-02-14", "unnamed", 50000000, "Maverick Capital and NEA", True, jl.W("Realtime Worlds"),
                    "press")],
        note="Dundee developer of Crackdown and APB; NEA announced a $30M investment in December 2006 and co-led a $50M "
             "round in February 2008 (Wikipedia), neither named as a series. It entered administration in August 2010 "
             "and APB was sold to Reloaded Productions, so it reads acquired on the asset-sale rule."),
    cls("reshape-inc", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=IR,
        flags=["city_unknown"],
        note="Electronic design automation software on the firm's 2013 historical list; its location and fate were not "
             "established."),
    cls("rewind", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Series A",
        stage_src="web_verified", stage_cite=REWIND_TC, stage_conf="medium", entry_date="2023-05", focus=AI,
        flags=["model_disputes_source"],
        rounds=[rnd("2022-11", "unnamed", 10000000, "a16z", False, REWIND_TC, "press"),
                rnd("2023-05", "Series A", None, "NEA", True, REWIND_TC, "press")],
        note="Rewind AI, renamed Limitless (the limitless row is the same company), bought by Meta in December 2025 "
             "(TechCrunch). NEA led the 2023 investor-pitch round that TechCrunch calls the unusual Series A, after "
             "a16z's $10M of 2022; the prefilled NZ is a one-word Wikidata join."),
    cls("reznext", status="private", rng="below_1b", country="IN", country_src="web_verified", country_cite=REZNEXT_SI,
        city="Bangalore", city_src="web_verified", stage="Seed", stage_src="web_verified", stage_cite=REZNEXT_SI,
        stage_conf="medium", entry_date="2014-12", focus=SA,
        rounds=[rnd("2014-12", "Seed", 5000000, "NEA", True, REZNEXT_SI, "press")],
        note="Bangalore hotel-distribution software company; SiliconIndia names its $5M seed funding from NEA (MediaNama "
             "reported the $5M in December 2014). Graduation left for the graduation pass."),
    cls("runtime", status="private", rng="below_1b", country="US", stage="undetermined", focus=DI,
        flags=["city_unknown"],
        note="IoT device management built on Apache Mynewt, listed by the firm as current and private through 2022; no "
             "round or location was found. The Y Combinator row named Runtime is a 2026 agent-infrastructure startup, "
             "a different company."),
    cls("semiconductor-manufacturing-int-l", status="public", rng="10b_plus", usd=66180000000, val_src="web_verified",
        val_cite=SMIC_CAP, asof="2026-09", country="CN", country_src="web_verified",
        country_cite=jl.W("Semiconductor Manufacturing International Corporation"), city="Shanghai",
        stage="Growth", stage_src="web_verified", stage_cite=jl.FTS("SEMICONDUCTOR MANUFACTURING", "F-1"),
        stage_conf="high", entry_date="2003", focus=IR, extra={"valuation_range_source": "web_verified"},
        rounds=[rnd("2003", "Series C", None, None, True, jl.FTS("SEMICONDUCTOR MANUFACTURING", "F-1"), "filing")],
        note="SMIC, the Shanghai foundry; its 2004 F-1 shows NEA entities holding only Series C preference shares, issued "
             "in the second half of 2003, so NEA entered at Growth. Market cap $66.18B as of September 2026 "
             "(companiesmarketcap); the semiconductor-manufacturing-international-corporation-smic row is the same "
             "company."),
    cls("shenghui-lighting", status="private", rng="below_1b", country="CN", country_src="web_verified",
        country_cite=jl.ARCH("shenghui-lighting"), stage="undetermined", focus=CE, flags=["city_unknown"],
        note="Chinese green-lighting maker the firm listed as current in 2013 (its own page: a leading green lighting "
             "company in China); no later record was found, so it reads private as last known."),
]

# pending rows appended below after research: rapid-mobile-media-limited, recce
PENDING = [
    cls("rapid-mobile-media-limited", status="unknown", rng="below_1b", country="US", stage="undetermined", focus=MG,
        flags=["city_unknown", "country_prior"], extra={"hq_country_confidence": "low"},
        note="Mobile services, content and advertising delivery platform on the firm's 2013 list only; no record of the "
             "company, its location or fate was found, so the country is an inferred US at low confidence although the "
             "Limited suffix suggests a registration outside the US."),
    cls("recce", status="unknown", rng="below_1b", country="GB", country_src="web_verified", country_cite=RECCE_TC,
        city="London", city_src="web_verified", stage="Series A", stage_src="web_verified", stage_cite=RECCE_TC,
        stage_conf="medium", entry_date="2012-07-13", focus=CM,
        rounds=[rnd("2012-07-13", "Series A", 4000000, "NEA", True, RECCE_TC, "press")],
        note="Recce, the 3D interactive city map from London-based eeGeo, launched with a $4M Series A led by NEA on top "
             "of a seed from Initial Capital, Swordfish and others (TechCrunch, 2012-07-13); the firm's own 2010 year "
             "predates it. eeGeo later became WRLD and the Recce app closed; the company's current state was not "
             "established."),
]
L += PENDING
import sys
if "--dry" in sys.argv:
    import json; print(len(L), sorted(x["slug"] for x in L)); sys.exit()
jl.write("c13a", L)
