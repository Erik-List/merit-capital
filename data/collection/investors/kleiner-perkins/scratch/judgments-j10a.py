import judge_lib as jl
from judge_lib import cls, rnd, verdict

# Judge j10, batch 19 (PRO-99 Kleiner Perkins): listed members, classification; two sale-consideration rulings.

CK = "2026-09-30"
SYNA_S1 = jl.FTS("SYNAPTICS", "S-1")
SOUN_CAP = "https://stockanalysis.com/stocks/soun/market-cap/"
SUNGROW_CAP = "https://stockanalysis.com/quote/she/300274/market-cap/"
TC_STORENVY_SEED = "https://techcrunch.com/2011/01/27/storenvy/"
TC_STORENVY_A = "https://techcrunch.com/2013/02/12/storenvy-goes-from-getting-kicked-out-of-yc-to-raising-a-5m-round/"
TC_TRENDYOL = "https://techcrunch.com/2011/07/22/turkish-private-shopping-site-trendyol-scores-a-big-round-from-kpcb-tiger-global/"
AA_TRENDYOL = "https://www.aa.com.tr/en/economy/e-commerce-giant-trendyol-becomes-turkeys-1st-decacorn/2329244"
PULSE_TRANSCARENT = "https://pulse2.com/transcarent-health-and-care-platform-company-closes-126-million-at-2-2-billion-valuation/"
BCV_TERRA_CITY = "https://www.bizjournals.com/austin/news/2026/04/13/terrafirma-spacex-mars-buda-austin-headquarters.html"
CITYBIZ_TERRA = "https://www.citybiz.co/article/874154/terrafirma-raises-115-million-series-a-to-scale-ai-powered-robotic-construction-platform/"

L = []

# ---- sale consideration (listed rows whose position was stock received for a portfolio company)
L += [
    verdict("superhuman", "not_member",
            "Sale consideration (Erik 2026-09-22; decisions.md R5): the firm's Superhuman tile was created in November 2025, "
            "after Grammarly bought Coda (the firm led Coda's Series C in 2020, its own post) and renamed itself Superhuman; "
            "it carries Coda's 2020 year, so the position is acquirer stock received for Coda, which is its own row (coda).",
            ec="site_listing", conf="medium", cite=jl.SITE("superhuman")),
    verdict("travelocity", "not_member",
            "Sale consideration (Erik 2026-09-22; decisions.md R5): the firm backed Preview Travel (its funds filed 13G on it, "
            "1998-99; row preview-travel-inc), which merged into Travelocity.com in March 2000; the 2012 page lists the "
            "public successor, whose stock was the consideration.",
            ec="site_listing", conf="medium", cite=jl.ARCH("travelocity")),
]

# ---- members, classification
L += [
    cls("soundhound", status="public", rng="1b_plus", usd=2670000000, val_src="web_verified", val_cite=SOUN_CAP, asof=CK,
        city="Santa Clara", stage="Growth", stage_src="web_verified", stage_conf="medium",
        stage_cite=jl.W("SoundHound"), entry_date="2017-01", focus="AI & Applied AI",
        rounds=[rnd("2015-06", "several earlier rounds ($40M in all)", 40000000, None, False, jl.W("SoundHound"), "press"),
                rnd("2017-01", "$75M round", 75000000, None, True, jl.W("SoundHound"), "press"),
                rnd("2018-05", "$100M round", 100000000, "Tencent", None, jl.W("SoundHound"), "press")],
        extra={"valuation_range_source": "web_verified"},
        note="SoundHound AI (Nasdaq: SOUN), Santa Clara; market cap $2.67B on 2026-09-30 (stockanalysis). Kleiner Perkins "
             "is named in the $75M round announced January 2017, after $40M raised across earlier rounds by mid-2015 "
             "(Wikipedia), so Growth; the firm's own since-year is 2015 and its label Growth, consistent."),

    cls("synaptics", city="San Jose", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SYNA_S1,
        entry_date="1987-06", focus="Industrial & Robotics",
        rounds=[rnd("1986-06", "Series A", None, None, False, SYNA_S1, "filing"),
                rnd("1987-06", "Series B", None, None, True, SYNA_S1, "filing"),
                rnd("1989-09", "Series C", None, None, False, SYNA_S1, "filing"),
                rnd("1990-09", "Series D", None, None, True, SYNA_S1, "filing")],
        note="The 2001 S-1's certain-transactions table shows Kleiner, Perkins, Caufield & Byers IV bought no Series A "
             "(June 1986) and first bought Series B preferred (issued June 1987, $1.75 a share), then D, E and F: a Series B "
             "entry, so Growth. Headquarters San Jose since 2013 (Wikipedia)."),

    cls("synteni", status="acquired", rng="below_1b", country="US", city="Fremont", stage="undetermined",
        entry_date="1997", focus="Healthcare & Bio", rounds=[],
        note="DNA microarray maker bought by Incyte in 1998 (the firm's exit line names Incyte). The firm's since-year is "
             "1997; no source found names the round."),

    cls("tandem-computers", status="acquired", rng="below_1b", city="Cupertino", stage="undetermined", entry_date="1975",
        focus="Data Infrastructure", flags=["model_disputes_source"], rounds=[],
        note="Status disputes the prefilled defunct: Compaq acquired Tandem in 1997 (Wikipedia; the firm's own exit line "
             "names Compaq). Jimmy Treybig wrote the plan at Kleiner Perkins and Tom Perkins made the initial venture "
             "investment (Wikipedia), but no source names the round; since-year 1975."),

    cls("thermawave", status="acquired", rng="below_1b", country="US", city="Fremont", stage="undetermined",
        entry_date="1982", focus="Industrial & Robotics", rounds=[],
        note="Therma-Wave, thin-film metrology for semiconductors, Fremont; the firm's exit line names Toray Industries and "
             "Shimadzu, and the later public company was bought by KLA-Tencor in 2007. No source names the 1982 round."),

    cls("tivoli-systems", status="acquired", rng="below_1b", country="US", city="Austin", stage="undetermined",
        focus="Data Infrastructure", rounds=[],
        note="Systems-management software company from Austin, bought by IBM after its 1995 listing and run as IBM's "
             "Tivoli division (Wikipedia). No source names the round the firm entered."),

    cls("triquint-semiconductor", rng="below_1b", city="Hillsboro", stage="undetermined", focus="Industrial & Robotics",
        rounds=[],
        note="GaAs RF chip maker in Hillsboro, Oregon, merged with RF Micro Devices into Qorvo in 2015 (acquired, as the NEA "
             "row reads). No source names the round the firm entered."),

    cls("stipple", status="acquired", rng="below_1b", city="San Francisco", stage="Seed", stage_src="web_verified",
        stage_conf="high", stage_cite=jl.W("Stipple (company)"), entry_date="2010", focus="Media, Gaming & Advertising",
        rounds=[rnd("2010", "Seed ($2M)", 2000000, None, True, jl.W("Stipple (company)"), "press")],
        note="Image-tagging ad platform; its $2M seed came from Kleiner Perkins Caufield & Byers, Floodgate and angels "
             "(Wikipedia, which places it with the August 2010 launch). Bought by an undisclosed firm in a private sale, product later shut. "
             "Graduation left for the graduation pass."),

    cls("storenvy", status="acquired", rng="below_1b", city="San Francisco", stage="Seed", stage_src="web_verified",
        stage_conf="high", stage_cite=TC_STORENVY_SEED, entry_date="2011-01-27",
        grad="graduated", grad_src="web_verified", grad_cite=TC_STORENVY_A, grad_conf="high", grad_asof="2013-02-12",
        focus="Consumer & Marketplaces",
        rounds=[rnd("2011-01-27", "Seed ($1.5M)", 1500000, "Spark Capital and First Round Capital", True, TC_STORENVY_SEED, "press"),
                rnd("2013-02-12", "Series A ($5M)", 5000000, "Intel Capital", None, TC_STORENVY_A, "press")],
        note="TechCrunch (2011-01-27) names Kleiner Perkins in the just-closed $1.5M seed led by Spark and First Round; a named "
             "$5M Series A followed (TechCrunch, 2013-02-12), so it graduated. Bought by The OpenSky Project in 2016 "
             "(Wikipedia), acquired as in the First Round book."),

    cls("the-wing", status="defunct", rng="below_1b", country="US", city="New York", stage="Series A",
        stage_src="web_verified", stage_conf="high", stage_cite=jl.W("The Wing (workspace)"), entry_date="2017-04",
        focus="Consumer & Marketplaces",
        rounds=[rnd("2016-10", "Seed ($2.4M)", 2400000, None, False, jl.W("The Wing (workspace)"), "press"),
                rnd("2017-04", "Series A ($8M)", 8000000, "NEA", True, jl.W("The Wing (workspace)"), "press"),
                rnd("2017-11", "Series B ($32M)", 32000000, "WeWork", None, jl.W("The Wing (workspace)"), "press"),
                rnd("2018-12", "Series C ($75M)", 75000000, "Sequoia Capital", None, jl.W("The Wing (workspace)"), "press")],
        note="Women's coworking clubs, New York. Kleiner Perkins is named in the $8M Series A that NEA led in April 2017 "
             "(Wikipedia; the $2.4M seed was angels). The Wing ceased operations on 2022-08-30, defunct as in the GV, NEA "
             "and Sequoia books."),

    cls("think", status="acquired", rng="below_1b", country="NO", country_src="web_verified",
        country_cite=jl.W("Think Global"), city="Bærum", stage="Growth", stage_src="web_verified", stage_conf="medium",
        stage_cite=jl.W("Think Global"), entry_date="2009-08-27", focus="Climate & Energy",
        rounds=[rnd("2009-08-27", "recapitalisation ($47M)", 47000000, None, True, jl.W("Think Global"), "press")],
        note="Norwegian EV maker (Think Global, Bærum). Kleiner Perkins is named among the investors in the $47M "
             "recapitalisation of August 2009 that took the 1991 company out of court protection (Wikipedia): a recap, so "
             "Growth. Bankrupt 2011-06-22; Electric Mobility Solutions bought its assets in July 2011 (successor), and "
             "production ceased in August 2012."),

    cls("trendyol", status="acquired", rng="below_1b", country="TR", country_src="web_verified",
        country_cite=jl.W("Trendyol"), city="Istanbul", stage="undetermined", entry_date="2011-07",
        focus="Consumer & Marketplaces",
        rounds=[rnd("2010", "first outside investment (not named)", None, "Tiger Global", False, jl.W("Trendyol"), "press"),
                rnd("2011-07", "round of $25M to $30M (not named)", None, "Kleiner Perkins and Tiger Global", True, TC_TRENDYOL, "press"),
                rnd("2018", "Alibaba majority purchase", 728000000, "Alibaba", False, jl.W("Trendyol"), "press"),
                rnd("2021-08", "funding at $16.5B", 1500000000, None, False, AA_TRENDYOL, "press")],
        note="Istanbul e-commerce platform (Wikipedia, confirming the TR claim). The firm entered through its Digital Growth "
             "Fund in the July 2011 round it co-led with Tiger (TechCrunch), which no source names, so undetermined. Alibaba "
             "bought a majority in 2018; read acquired as the Tiger book does, although Trendyol later raised $1.5B at "
             "$16.5B from outside investors (Anadolu Agency, 2021)."),

    cls("sungrow", status="public", rng="10b_plus", usd=25351495468, val_src="web_verified", val_cite=SUNGROW_CAP,
        asof=CK, country="CN", country_src="web_verified", country_cite=jl.W("Sungrow"), city="Hefei",
        stage="undetermined", focus="Climate & Energy", flags=["kpcb_china"], rounds=[],
        extra={"valuation_range_source": "web_verified"},
        note="Sungrow Power Supply, PV inverter maker headquartered in Hefei, Anhui (Wikipedia), listed in Shenzhen "
             "(300274). Market cap CNY 169.97B on 2026-09-30 (stockanalysis): CNY 169.97B @ ECB 2026-09-30 (CNY/EUR 7.613, "
             "EUR/USD 1.1355) = $25.35B. A KPCB China holding on the China listing (X1); no source names its round."),
]


PRWEB_TERMINAL = "https://www.prweb.com/releases/terminal_raises_10m_to_help_build_elite_remote_engineering_teams_appoints_clay_kellogg_as_ceo/prweb15506565.htm"
L += [
    cls("solidia-technologies", status="private", rng="below_1b", country="US", city="Piscataway", stage="undetermined",
        focus="Climate & Energy", rounds=[],
        note="Low-carbon cement and concrete technology from Rutgers, Piscataway, New Jersey; the firm's Greentech team "
             "(Bill Joy) listed it 2012-18. No source found names the round the firm entered or a mark near $1B."),

    cls("songbird", status="private", rng="below_1b", country="US", stage="undetermined", focus="Healthcare & Bio",
        flags=["city_unknown"],
        rounds=[rnd("2022-08", "round of $7.5M (vendor)", 7500000, "Kleiner Perkins (vendor)", None, None, "vendor")],
        note="Songbird Therapy, in-home autism care for children, on the firm's 2022-23 health-care list; vendor profiles "
             "say its last round was led by Kleiner Perkins but no citable page names the round, so undetermined. The "
             "Sequoia row named Songbird is a different company (the open media player that shut in 2013)."),

    cls("soundcloud", status="private", rng="below_1b", country="DE", country_src="web_verified",
        country_cite=jl.W("SoundCloud"), city="Berlin", stage="Growth", stage_src="model", stage_conf="medium",
        entry_date="2012-01", focus="Media, Gaming & Advertising",
        rounds=[rnd("2009-04", "Series A (EUR 2.5M)", None, "Doughty Hanson Technology Ventures", False, jl.W("SoundCloud"), "press"),
                rnd("2011-01", "Series B ($10M)", 10000000, "Union Square Ventures and Index Ventures", False, jl.W("SoundCloud"), "press"),
                rnd("2012-01", "round of about $50M", 50000000, "Kleiner Perkins and GGV", True, None, "press"),
                rnd("2014-01", "round of $60M at $700M", 60000000, "IVP", None, jl.W("SoundCloud"), "press"),
                rnd("2017-08", "rescue round ($169.5M)", 169500000, "The Raine Group and Temasek", None, jl.W("SoundCloud"), "press")],
        note="Berlin audio platform (Wikipedia: a German service). The firm's Digital Growth Fund entered in the January 2012 "
             "round it led with GGV ('Swedish Soundcloud set to expand with new American investment', The Local, "
             "2012-01-04), after the Series A (2009) and Series B (2011) it was not in (Wikipedia), so Growth. Marks stayed "
             "below $1B ($700M in 2014, a 2017 rescue round); private as in the IVP and USV books."),

    cls("spikesource", status="acquired", rng="below_1b", country="US", city="Redwood City", stage="undetermined",
        focus="Data Infrastructure", rounds=[],
        note="Open-source middleware integration and support company, Redwood City (the 2008 listing); the firm's 2012 page "
             "shows it Acquired. No source found names the round the firm entered."),

    cls("spiracur", status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined",
        focus="Healthcare & Bio", rounds=[],
        note="Mechanically powered negative-pressure wound therapy (SNaP), Sunnyvale (the 2010 listing); its SNaP business "
             "went to Acelity (KCI) in 2016 on model knowledge, while the firm's pages show Private to 2014. No source found "
             "names the round the firm entered."),

    cls("spotmixer", status="acquired", rng="below_1b", country="US", stage="undetermined",
        focus="Media, Gaming & Advertising", flags=["city_unknown"], rounds=[],
        note="Online and mobile video creation service (Randy Komisar); the firm's own pages show it Acquired from 2013. "
             "No source places the company or names the round."),

    cls("ss8-networks", status="private", rng="below_1b", country="US", city="Milpitas", stage="undetermined",
        focus="Security", rounds=[],
        note="Lawful-intercept and network intelligence vendor to carriers and agencies (San Jose in the 2008 listing, "
             "Milpitas now), still independent. No source found names the round the firm entered."),

    cls("stance", status="private", rng="below_1b", country="US", city="San Clemente", stage="undetermined",
        focus="Consumer & Marketplaces",
        rounds=[rnd("2015-03", "round of $50M", 50000000, None, None, jl.W("Stance (brand)"), "press"),
                rnd("2016-04", "round of $30M at $400M", 30000000, "Mercato Partners", True, jl.W("Stance (brand)"), "press")],
        note="Sock and apparel brand, San Clemente (Wikipedia). Kleiner Perkins was a returning investor in the April 2016 "
             "$30M round at $400M (Wikipedia), so it entered earlier, likely in the March 2015 $50M round, which no source "
             "names; undetermined. Private as in the Menlo book."),

    cls("studyplaces", status="acquired", rng="below_1b", country="IN", country_src="web_verified",
        country_cite=jl.ARCH("studyplaces"), stage="undetermined", focus="Consumer & Marketplaces",
        flags=["city_unknown"], rounds=[],
        note="StudyPlaces.com, an Indian education search portal (the firm's 2012 page, which also shows it Acquired). "
             "No source places it in a city or names the round."),

    cls("subject", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
        stage_conf="high", stage_cite=jl.POST("subject-seed"), entry_date="2021-05-26", focus="SaaS",
        flags=["city_unknown"],
        rounds=[rnd("2021-05-26", "Seed", None, "Kleiner Perkins", True, jl.POST("subject-seed"), "firm")],
        note="K-12 digital curriculum and virtual courses (Subject Technologies, still operating per its site). The firm's "
             "own post says it led Subject's seed (2021-05-26). Graduation left for the graduation pass."),

    cls("summation", status="private", rng="below_1b", country="US", city="Bellevue", stage="Series A",
        stage_src="first_party", stage_conf="medium", stage_cite=jl.POST("summation-seriesa"), entry_date="2025-10-01",
        focus="AI & Applied AI",
        rounds=[rnd("2025-10-01", "Series A (part of $35M raised)", None, "Kleiner Perkins", True, jl.POST("summation-seriesa"), "firm")],
        extra={"valuation_range_source": "web_verified", "valuation_citation": jl.POST("summation-seriesa"),
               "valuation_asof": CK},
        note="AI analyst for enterprise planning (Ian Wong), Bellevue, Washington (GeekWire and 425 Business, 2025-10-01). "
             "The firm's own post says it led the Series A; the firm's since-year is 2025, so no earlier entry. Momentum "
             "check 2026-09-30 (Google News by name): newest funding report 'Opendoor co-founder brings Seattle-area startup "
             "Summation out of stealth with $35M in funding' (2025-10-01); no priced round at or above $1B. The Battery row "
             "named Summation is a different company (the e-discovery firm sold in 2004)."),

    cls("sundrop-fuels", status="unknown", rng="below_1b", country="US", city="Louisville", stage="undetermined",
        focus="Climate & Energy", rounds=[],
        note="Solar-gasification biofuel developer, Louisville, Colorado (the 2010 listing; Joe Lacob); its planned "
             "Louisiana plant was not built and no source establishes its current state or names the round."),

    cls("supplyframe", status="acquired", rng="below_1b", country="US", city="Pasadena", stage="undetermined",
        entry_date="2007", focus="SaaS", rounds=[],
        note="Electronics design and sourcing network, Pasadena, bought by Siemens (the firm's exit line; closed 2021). The "
             "firm's since-year is 2007; no source found names the round."),

    cls("tajir", status="private", rng="below_1b", country="PK", country_src="web_verified",
        country_cite=jl.POST("tajir-new-funding"), city="Lahore", stage="Series A", stage_src="model", stage_conf="medium",
        entry_date="2021-06-02", focus="Consumer & Marketplaces",
        rounds=[rnd("2021-06-02", "Series A ($17M)", 17000000, "Kleiner Perkins", True, None, "press")],
        note="Lahore B2B marketplace for small stores. The firm's post of 2021-06-02 calls it its first investment in "
             "Pakistan, the day Forbes, menabytes and Profit reported the $17M Series A led by Kleiner Perkins, so a Series A "
             "entry (headline only, hence model). Private as in the YC book."),

    cls("tally", city="San Francisco", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
        rounds=[rnd("2018-07-25", "round of $25M", 25000000, None, None, None, "press"),
                rnd("2022-10-03", "round of $80M at $855M", 80000000, None, None, None, "press")],
        note="Credit-card debt payoff app, San Francisco, shut down in August 2024 after failing to raise (TechCrunch, "
             "Banking Dive). On the firm's 2018-20 consumer list; the press names its $25M 2018 round (a16z's Series B) and "
             "the $80M 2022 round at $855M, neither tied to Kleiner Perkins, so undetermined."),

    cls("tang-energy", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
        country_cite=jl.ARCH("tang-energy"), city="Beijing", stage="undetermined", focus="Climate & Energy",
        flags=["kpcb_china"], rounds=[],
        note="Wind-turbine blade maker listed by KPCB China (Beijing, China listing 2010; Greentech team pages to 2014, "
             "Private). X1 provisional member. No later trace or named round."),

    cls("tangsong", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
        country_cite=jl.ARCH("tangsong"), city="Shanghai", stage="undetermined", focus="Media, Gaming & Advertising",
        flags=["kpcb_china"], rounds=[],
        note="Online interactive 3D platform on the Virtools engine, Shanghai (KPCB China listing 2010; logo grid to 2024). "
             "X1 provisional member. No current state or named round found."),

    cls("teralane", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
        country_cite=jl.ARCH("teralane"), city="Shenzhen", stage="undetermined", focus="Industrial & Robotics",
        flags=["kpcb_china"], rounds=[],
        note="LCD driver IC designer, Shenzhen (KPCB China listing 2010; pages to 2014, Private). X1 provisional member. "
             "No later trace or named round."),

    cls("terminal-io", status="private", rng="below_1b", country="US", city="San Francisco", stage="Series A",
        stage_src="web_verified", stage_conf="medium", stage_cite=PRWEB_TERMINAL, entry_date="2018-05-22", focus="SaaS",
        rounds=[rnd("2017-03", "Seed ($3M)", 3000000, None, None, None, "vendor"),
                rnd("2018-05-22", "Series A ($10M)", 10000000, None, True, PRWEB_TERMINAL, "company"),
                rnd("2019-09-26", "Series B ($17M)", 17000000, "8VC", True, "https://www.terminal.io/blog/announcing-terminals-17-million-series-b-funding", "company")],
        note="Builds remote engineering teams for startups, San Francisco. Its release of 2018-05-22 names Kleiner Perkins "
             "in the $10M Series A; the firm's listing starts that year and no source puts it in the 2017 seed. The firm "
             "rejoined the $17M Series B led by 8VC (company blog)."),

    cls("terrafirma", status="private", rng="below_1b", country="US", city="Buda", stage="Series A",
        stage_src="first_party", stage_conf="high", stage_cite=jl.POST("terrafirma"), entry_date="2026-07-15",
        focus="Industrial & Robotics",
        rounds=[rnd("2024", "Seed", None, "Bain Capital Ventures", False, None, "firm"),
                rnd("2026-07-14", "Series A ($115M)", 115000000, "Kleiner Perkins", True, CITYBIZ_TERRA, "press")],
        note="AI-driven construction robotics, Buda, Texas (as the Bain Capital Ventures book reads). The firm's post of "
             "2026-07-15 says it leads the $115M Series A, and its since-year is 2026; Bain Capital Ventures had the 2024 "
             "seed. No valuation was published."),

    cls("terralliance", status="unknown", rng="below_1b", country="US", city="Newport Beach", stage="undetermined",
        focus="Climate & Energy", rounds=[],
        note="Oil and gas exploration technology company, Newport Beach (the 2008 listing, its only year). No source "
             "establishes its later state or names the round."),

    cls("tethys-bioscience", status="unknown", rng="below_1b", country="US", city="Emeryville", stage="undetermined",
        focus="Healthcare & Bio", rounds=[],
        note="Blood-test diagnostics for chronic-disease risk (PreDx), Emeryville (the 2008 listing; pages to 2013). No "
             "source establishes its later state or names the round."),

    cls("tianren", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
        country_cite=jl.ARCH("tianren"), stage="undetermined", focus="Climate & Energy",
        flags=["kpcb_china", "city_unknown"], rounds=[],
        note="Biological pesticide producer in Jiangxi province (KPCB China listing 2010, Greentech; logo grid to 2024). X1 "
             "provisional member. The listing gives only the province; no named round."),

    cls("tidal-software-formerly-intersperse", status="acquired", rng="below_1b", country="US", city="Palo Alto",
        stage="undetermined", focus="Data Infrastructure", rounds=[],
        note="IT job-scheduling and monitoring software; Intersperse (Pasadena, the 2008 listing) became Tidal Software, "
             "which Cisco bought in 2009. No source found names the round the firm entered."),

    cls("tidal-systems", status="acquired", rng="below_1b", country="US", city="Santa Clara", stage="undetermined",
        focus="Industrial & Robotics", flags=["kpcb_china"], rounds=[],
        note="SSD controller chips with LDPC error correction (Wen Hsieh; the 2013-14 pages under Teams China, so flagged "
             "for X1); bought by Micron in 2015. No source found names the round."),

    cls("transcarent", status="private", rng="1b_plus", usd=2200000000, val_src="web_verified",
        val_cite=PULSE_TRANSCARENT, asof="2024-05", country="US", city="Denver", stage="undetermined",
        focus="Healthcare & Bio", flags=["stale"],
        rounds=[rnd("2020-10", "Series A ($40M)", 40000000, "General Catalyst and 7wireVentures", None, None, "press"),
                rnd("2021-06-10", "Series B ($58M)", 58000000, None, None, "https://www.businesswire.com/news/home/20210610005315/en/Transcarent-Raises-%2458-Million-in-Series-B-Funding-to-Accelerate-Consumer-Directed-Health-and-Care-Experience-for-Self-Insured-Employers", "company"),
                rnd("2024-05", "Series D ($126M at $2.2B)", 126000000, "General Catalyst and 7wireVentures", None, PULSE_TRANSCARENT, "press")],
        extra={"valuation_range_source": "web_verified"},
        note="Health and care platform for self-insured employers (Glen Tullman), Denver as in the General Catalyst book. "
             "The last priced mark is the $2.2B Series D of May 2024 (Pulse 2.0), older than 24 months, so stale. On the "
             "firm's 2022-26 health-care list; no source found ties Kleiner Perkins to a named round (the $58M Series B release of "
             "2021-06-10 could not be read), so undetermined."),
]

YAHOO_TRAVERSAL = "https://finance.yahoo.com/news/traversal-emerges-stealth-48-million-111152897.html"
L += [
    cls("traversal", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=YAHOO_TRAVERSAL,
        entry_date="2025-06-18", focus="AI & Applied AI",
        rounds=[rnd("2025-06-18", "Seed", None, "Sequoia Capital", False, YAHOO_TRAVERSAL, "press"),
                rnd("2025-06-18", "Series A ($48M with the seed)", None, "Kleiner Perkins", True, YAHOO_TRAVERSAL, "press"),
                rnd("2026-03", "strategic investment", None, "Amex Ventures", None, None, "press")],
        extra={"hq_city_citation": "https://www.traversal.com/", "valuation_range_source": "web_verified",
               "valuation_citation": YAHOO_TRAVERSAL, "valuation_asof": CK},
        note="AI site-reliability startup; its site gives a West 26th Street, New York address, which replaces the Sequoia "
             "row's uncited San Francisco. Sequoia led the seed and Kleiner Perkins the Series A, $48M in all, announced "
             "2025-06-18 (Yahoo Finance; the firm's own post the same day). Momentum check 2026-09-30 (web search by name): "
             "newest funding report is Amex Ventures' strategic investment (March 2026); no priced round at or above $1B "
             "(a vendor's $303M estimate is not a mark)."),

    cls("spot", status="private", rng="below_1b", country="US", stage="undetermined", focus="AI & Applied AI",
        flags=["city_unknown", "model_disputes_source"], rounds=[],
        extra={"valuation_range_source": "web_verified", "valuation_citation": "https://www.upcraft.ai/",
               "valuation_asof": CK},
        note="Spot is meetwithspot.com (the firm's 2025 enterprise tile links it), which now redirects to Upcraft, an AI "
             "sales-agent platform: the company renamed itself. The JP country came from a one-word Wikidata join to "
             "another company and is disputed; nothing places it, and US is inferred from the firm's list. No round names "
             "the firm; momentum check 2026-09-30 (Google News and web search) found no priced round at or above $1B."),
]

MOMO_6K = "https://www.sec.gov/Archives/edgar/data/1610601/000119312518055156/d538391dex991.htm"
TC_TRADEHERO = "https://techcrunch.com/2013/09/26/tradehero-series-a/"
LEAP_TRADEHERO = "https://www.leaprate.com/news/ayondo-acquires-singapore-investor-education-app-tradehero-ahead-of-planned-sgx-listing/"
L += [
    cls("tantan", status="acquired", rng="below_1b", country="CN", country_src="web_verified", country_cite=MOMO_6K,
        city="Beijing", stage="undetermined", focus="Consumer & Marketplaces", flags=["kpcb_china"],
        rounds=[rnd("2018-02-23", "acquisition by Momo (5.3M shares and $600.9M cash)", None, "Momo", None, MOMO_6K, "filing")],
        note="Tantan, the Chinese dating app founded in 2015 (Momo's 6-K of 2018-02-23 confirms the CN claim), acquired by "
             "Momo for about 5.3 million Momo shares and $600.9M in cash, closing in 2018. On the firm's 2021-24 logo grid, "
             "the KPCB China class (X1). No source names the round the firm entered."),

    cls("tradehero", status="acquired", rng="below_1b", country="SG", country_src="web_verified",
        country_cite=TC_TRADEHERO, city="Singapore", stage="Series A", stage_src="web_verified", stage_conf="high",
        stage_cite=TC_TRADEHERO, entry_date="2013-09-26", focus="Fintech & Payments", flags=["kpcb_china"],
        rounds=[rnd("2013-09-26", "Series A ($10M)", 10000000, None, True, TC_TRADEHERO, "press"),
                rnd("2016-11-15", "brand acquired by Ayondo", None, "Ayondo", None, LEAP_TRADEHERO, "press")],
        note="Stock-trading game app by the Singapore developer MyHero; its $10M Series A came from the KPCB China fund and "
             "IPV Capital (TechCrunch, 2013-09-26), so a KPCB China holding (X1). Ayondo acquired the TradeHero brand in "
             "November 2016 (LeapRate)."),
]

jl.write("j10a", L)
