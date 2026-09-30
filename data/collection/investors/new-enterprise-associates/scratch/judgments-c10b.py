"""PRO-100 NEA, judge c10, queue batch 20 (techforward .. tripod): classification of listed members, plus three
membership corrections under X1 (tele-atlas, telebit-corp, trillium-therapeutics)."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, NEWS, W

SA = "https://stockanalysis.com/stocks/{}/market-cap/"
S1_TELEGENT = "https://www.sec.gov/Archives/edgar/data/1296612/000119312509240034/ds1.htm"
S1_TRACON = "https://www.sec.gov/Archives/edgar/data/1394319/000104746914010118/a2221572zs-1.htm"
S4_TAE = "https://www.sec.gov/Archives/edgar/data/0001849635/000143774926031534/djt20260922_s4.htm"
TC_WEATHERBILL = "https://techcrunch.com/2007/10/17/an-interesting-bet-weatherbill-takes-125-million-series-b/"
TC_TIMESCALE = "https://techcrunch.com/2018/01/24/timescale-raises-12-4m-to-build-a-new-breed-of-time-series-database-software/"
VC_TERRAJOULE = "https://www.vcpost.com/articles/17427/20131105/terrajoule-raises-usd11-5-million-solar-energy-storage.htm"
PR_TOKENZ = "https://prtimes.jp/main/html/rd/p/000000003.000163361.html"
GL = "Graduation left for the graduation pass."

L = []

# ---- membership corrections (verdict line only)
L.append(verdict("tele-atlas", "not_member",
                 "X1: Tele Atlas was listed in Frankfurt from 2000; the firm's own listing gives a 2004 first "
                 "investment labelled Public/PIPES, a purchase into the listed company, and no earlier NEA private "
                 "round is on record.", ec="site_listing", conf="medium", cite=SITE("tele-atlas")))
L.append(verdict("telebit-corp", "not_member",
                 "X1: Telebit was a Nasdaq-listed modem maker by the late 1980s; the firm's own listing gives a 1990 "
                 "first investment labelled Public/PIPES, a purchase into the listed company, and no earlier NEA "
                 "private round is on record.", ec="site_listing", conf="medium", cite=SITE("telebit-corp")))
L.append(verdict("trillium-therapeutics", "not_member",
                 "X1 and R2: Trillium was listed on the TSX and Nasdaq from 2014; NEA's position came in 2017 through "
                 "Growth Equity Opportunities Fund V (named as a selling holder on the 2018 F-3) and the firm labels "
                 "it Public/PIPES. No earlier NEA private round is on record.",
                 ec="site_listing", conf="high", cite=SITE("trillium-therapeutics")))

L.append(cls("techforward", status="acquired", rng="below_1b", city="Los Angeles", stage="undetermined",
             entry_date="2007", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2009-06", "unnamed", 800000, None, None, None, "filing"),
                     rnd("2009-08-03", "unnamed", 4308369, None, True, None, "filing"),
                     rnd("2010-12", "unnamed", 1300000, None, None, None, "filing")],
             note="Electronics buy-back guarantees, Los Angeles; the business was sold on (aligned with the First "
                  "Round row; the firm now lists it Historic). The Seed band rode the 2009-08-03 Form D, but the "
                  "company was incorporated in 2007 and the firm's own listing gives a 2007 first investment, so NEA "
                  "entered before the filings; that round is not named in any source read."))

L.append(cls("technical-communities", status="private", rng="below_1b", country="US", city="San Mateo",
             city_src="web_verified", stage="undetermined", entry_date="1999", focus="Consumer & Marketplaces",
             note="Technical Communities, Inc. is the company that trades as TestMart (the TCV row: 'Technical "
                  "Communities, Inc. dba TestMart'), so this row and the testmart row are one company. It "
                  "operates: testmart.com carries a 2026 copyright and a San Mateo address (1840 Gateway Drive). "
                  "NEA's 1999 round is not named in any source read."))

L.append(cls("telegent-systems", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
             stage="Series A", stage_src="web_verified", stage_cite=S1_TELEGENT, stage_conf="high",
             entry_date="2004", focus="Industrial & Robotics",
             rounds=[rnd("2004-04", "Series A", None, None, True, S1_TELEGENT, "filing"),
                     rnd("2004-08", "Series B", None, None, True, S1_TELEGENT, "filing"),
                     rnd("2005-11", "Series C", None, None, True, S1_TELEGENT, "filing")],
             note="Mobile TV chips; Cayman holding company operating from Sunnyvale (S-1, 2009); bought by "
                  "Spreadtrum (the firm's exit line). The S-1 shows NEA 11 and NEA Ventures 2004 holding Series A "
                  "preference shares (issued from April 2004), and Scott Sandell on the board since August 2004."))

L.append(cls("tempest-therapeutics", status="public", rng="below_1b", usd=13350000, val_src="web_verified",
             val_cite=SA.format("tpst"), asof="2026-09-30", city="Brisbane", stage="undetermined",
             entry_date="2015", focus="Healthcare & Bio", flags=["stage_disputes_band"],
             note="Oncology small molecules, Brisbane, California; Nasdaq TPST since the 2021 reverse merger into "
                  "Millendo. Market cap $13.4M on 2026-09-30 (stockanalysis). The Growth band is disputed: the Form D "
                  "sequence on file is the listed shell's (OvaScience, then Millendo, 2011-2018), and its director "
                  "match, Michael Raab, left NEA in 2009; the firm's own listing gives 2015, and that round is not "
                  "named in any source read."))

L.append(cls("tempus", status="public", rng="10b_plus", usd=15080000000, val_src="web_verified",
             val_cite=SA.format("tem"), asof="2026-09-30", city="Chicago", focus="Healthcare & Bio",
             flags=["model_disputes_source"], extra={"valuation_range_source": "web_verified"},
             note="Precision-medicine data and diagnostics, Chicago; Tempus AI listed on Nasdaq (TEM) in June 2024 and "
                  "the firm's exit line reads 'NASDAQ: TEM', so the pre-filled acquired status is disputed. Market "
                  "cap $15.08B on 2026-09-30 (stockanalysis)."))

L.append(cls("teneros", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="undetermined",
             entry_date="2003", focus="Data Infrastructure",
             rounds=[rnd("2008-02-04", "Series D", 40000000, None, None,
                         "https://techcrunch.com/2008/02/04/teneros-a-startup-that-cashes-in-every-time-microsoft-exchange-crashes-raises-40-million-in-a-series-d/",
                         "press"),
                     rnd("2009-11-10", "unnamed", 20000000, None, True, None, "filing")],
             note="Failover appliances for Microsoft Exchange, Mountain View (founded 2003 as Nuity Systems). Its "
                  "business went to Ongoing Operations in November 2010 (vendor profiles only, so read with care; "
                  "the firm still lists it Private). NEA first invested in 2003 per the firm; the 2009 Form D date on "
                  "file is a later round, and NEA's 2003 round is not named in any source read."))

L.append(cls("teracent", status="acquired", rng="below_1b", country="US", city="San Mateo", stage="undetermined",
             entry_date="2007", focus="Media, Gaming & Advertising", flags=["stage_disputes_band"],
             note="Display ad optimization network, San Mateo; bought by Google in 2009 (the firm's exit line). The "
                  "Pre-Seed band rode a $550K 2009 Form D, a late small round; the firm's own listing gives a 2007 "
                  "first investment, and that round is not named in any source read."))

L.append(cls("terrajoule", status="unknown", rng="below_1b", city="Redwood City", stage="Seed",
             stage_src="web_verified", stage_cite=VC_TERRAJOULE, stage_conf="medium", entry_date="2009",
             focus="Climate & Energy",
             rounds=[rnd("2009", "Seed", None, None, True, VC_TERRAJOULE, "press"),
                     rnd("2013-11-05", "Seed", 11500000, "Air Liquide", True, VC_TERRAJOULE, "press")],
             note="Solar steam power with storage, Redwood City. VC Post (2013-11-05): Forest Baskett and Arno Penzias "
                  "of NEA provided seed funding in 2009, and Air Liquide led an $11.5M round it also calls seed "
                  "funding. No company news after 2013; vendor profiles say acquired or merged without naming a "
                  "buyer, so the status cannot be established. " + GL))

L.append(cls("tesaro", city="Waltham", rng="below_1b", focus="Healthcare & Bio",
             note="Oncology biopharma, Waltham MA; bought by GlaxoSmithKline in 2019 (the firm's exit line)."))

L.append(cls("testmart", status="private", rng="below_1b", country="US", city="San Mateo", city_src="web_verified",
             stage="undetermined", entry_date="1999", focus="Consumer & Marketplaces",
             note="Government procurement marketplace for test and measurement equipment. Same company as the "
                  "technical-communities row (Technical Communities, Inc. dba TestMart). The TCV row's defunct is "
                  "contradicted by fresher evidence: testmart.com is live with a 2026 copyright and a San Mateo "
                  "address. NEA's 1999 round is not named in any source read."))

L.append(cls("the-climate-corporation", city="San Francisco", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=POST("vcs-and-angels-take-aim"), stage_conf="medium", entry_date="2006",
             grad="graduated", grad_src="web_verified", grad_cite=TC_WEATHERBILL, grad_conf="high",
             focus="Climate & Energy",
             rounds=[rnd("2007-10-17", "Series B", 12500000, "NEA and Index Ventures", True, TC_WEATHERBILL, "press")],
             note="Weather insurance, later farm data science (WeatherBill until 2011), San Francisco; bought by "
                  "Monsanto in 2013. NEA's own 2013 post names The Climate Corporation among its seed investments "
                  "(first invested 2006); TechCrunch (2007-10-17) reports the $12.5M Series B led by NEA and Index, "
                  "a later named round, so the seed graduated."))

L.append(cls("the-players-tribune", status="acquired", rng="below_1b", country="US", city="New York",
             stage="undetermined", entry_date="2015-06-15", focus="Media, Gaming & Advertising",
             rounds=[rnd("2015-06-15", "unnamed", 9500000, "NEA", True, W("The Players' Tribune"), "press"),
                     rnd("2017-01-19", "Series C", 40000000, "IVP", True, None, "press")],
             note="Athlete-written sports media, New York; bought by Minute Media in 2019. Wikipedia: NEA invested "
                  "$9.5M, announced 2015-06-15; NEA was an existing investor in IVP's 2017 Series C (the GV row). "
                  "The 2015 round is not named in any source read. Aligned with the GV and IVP rows."))

L.append(cls("the-well", status="private", rng="below_1b", country="US", city="New York", stage="undetermined",
             entry_date="2020", focus="Consumer & Marketplaces",
             note="Integrative wellness club, products and content, New York; the firm lists it Private and Current. "
                  "NEA's 2020 round is not named in any source read."))

L.append(cls("the-yes", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2018", focus="Consumer & Marketplaces",
             rounds=[rnd("2022-06-02", "Acquisition by Pinterest", None, None, None,
                         NEWS("the-yes", "Pinterest Is Buying"), "press")],
             note="AI fashion shopping app; Pinterest bought it in 2022 (Fashionista). NEA was among the investors in "
                  "the $30M raised before the 2020 launch (the Bain Capital Ventures row), which spans rounds none of "
                  "which is named. Aligned with that row."))

L.append(cls("theorycraft-games", status="private", rng="below_1b", country="US", city="Bellevue",
             stage="undetermined", entry_date="2020", focus="Media, Gaming & Advertising",
             rounds=[rnd("2021", "Series A", 37500000, "a16z", None, None, "press"),
                     rnd("2025-12-17", "Supervive shutdown announced", None, None, None,
                         NEWS("theorycraft-games", "pivots to more focused"), "press")],
             note="Independent game studio (Supervive); the game shuts in February 2026 while the studio pivots to "
                  "new projects (Dot Esports), so the company reads private. NEA first invested in 2020, before "
                  "a16z's 2021 Series A (the a16z row), but that round is not named in any source read. City aligned "
                  "with the a16z row."))

L.append(cls("therachon", status="acquired", rng="below_1b", country="CH", country_src="web_verified",
             country_cite=NEWS("therachon", "Swiss Rare Disease"), city="Basel", stage="undetermined",
             entry_date="2015", focus="Healthcare & Bio",
             rounds=[rnd("2018-08-09", "unnamed", 60000000, "Novo Holdings", None, None, "press"),
                     rnd("2019-05-08", "Acquisition by Pfizer", 340000000, None, None,
                         NEWS("therachon", "Swiss Rare Disease"), "press")],
             note="Rare-disease biologics (achondroplasia), Basel, Switzerland; Pfizer bought it in 2019 for $340M "
                  "upfront (RAPS, 'Swiss rare disease biotech'). NEA's 2015 round is not named in any source read."))

L.append(cls("thirdlove", status="private", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="model", stage_conf="medium", entry_date="2012", grad="graduated", grad_src="web_verified",
             grad_cite=W("ThirdLove"), grad_conf="high", focus="Consumer & Marketplaces",
             rounds=[rnd("2013-11-07", "unnamed", 5600000, None, True, None, "press"),
                     rnd("2016", "Series A", 8000000, None, True, W("ThirdLove"), "press")],
             note="Direct-to-consumer bras and underwear, San Francisco. The firm's year (2012) predates the $8M "
                  "Series A of 2016 that Wikipedia says NEA joined; NEA was in the first outside raise ($5.6M, "
                  "announced November 2013 with a16z, per the Felicis row's TechCrunch reading), read as the seed. "
                  "The named 2016 Series A graduates it."))

L.append(cls("threatquotient", status="acquired", city="Reston", rng="below_1b", focus="Security",
             note="Threat intelligence platform, Reston, Virginia (the Form Ds give nearby Sterling); bought by "
                  "Securonix (the firm's exit line 'Acquired by: Securonix')."))

L.append(cls("tiburio", status="defunct", city="Cambridge", rng="below_1b", stage="Series A",
             stage_src="web_verified", stage_cite=NEWS("tiburio", "Tiburio launches with"), stage_conf="high",
             focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2019-01-03", "Series A", 31000000, None, True, NEWS("tiburio", "Tiburio launches with"),
                         "press")],
             note="Rare endocrine and neuroendocrine drugs, Cambridge MA. Fierce Biotech (2019-01-03): it started with "
                  "a $31M Series A drawn from NEA, Longitude, Lundbeckfond and Alexandria, which the Growth band had "
                  "misread. No news after 2019; the firm dropped it from its live list and vendor profiles mark it "
                  "out of business from 2021, read as defunct."))

L.append(cls("tidal-therapeutics", status="acquired", rng="below_1b", country="US", city="Cambridge",
             stage="undetermined", entry_date="2019", focus="Healthcare & Bio",
             rounds=[rnd("2021-04-12", "Acquisition by Sanofi", 160000000, None, None,
                         NEWS("tidal-therapeutics", "Sanofi pays $160m upfront"), "press")],
             note="In-vivo mRNA immune-cell reprogramming, Cambridge MA; Sanofi bought it in April 2021 for $160M "
                  "upfront (PMLiVE). NEA's 2019 round is not named in any source read."))

L.append(cls("tigera", status="private", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2016", focus="Security",
             rounds=[rnd("2018-01-24", "unnamed", 10000000, None, True,
                         NEWS("tigera", "Tigera Raises $10M from Madrona"), "press"),
                     rnd("2018-12-12", "Series B", 30000000, "Insight Venture Partners", None,
                         NEWS("tigera", "Raises $30M in Series B"), "press")],
             note="Kubernetes network security (Calico), San Francisco. NEA first invested in 2016 (Aaron Jacobson "
                  "and Forest Baskett on the board); a $10M round from Madrona, NEA and Wing came in January 2018 and "
                  "Insight's Series B in December 2018, but NEA's 2016 round is not named. Aligned with the Insight "
                  "row."))

TIMESCALE_NOTE = ("Time-series database on PostgreSQL, New York; Timescale renamed itself TigerData in 2025 (the "
                  "tigerdata and timescale rows are one company). Entry: the firm's year is 2015, the year of the "
                  "company's $3.7M first Form D round (the Benchmark row: 'the $3.7M seed was NEA's'), read as the "
                  "seed; the $12.4M round of January 2018 led by Benchmark with NEA participating (TechCrunch) is "
                  "more than twice it, so the seed graduated. Mark: the $110M Series C of February 2022 valued it at "
                  "over $1B (FinSMEs), recorded at $1B, stale; aligned with the Benchmark, Redpoint and Tiger Global "
                  "rows.")
for slug, extra_flags in (("timescale", ["stage_disputes_band"]), ("tigerdata", [])):
    L.append(cls(slug, status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
                 val_cite=NEWS("timescale", "Valued at Over $1B"), asof="2022-02-22",
                 country=None if slug == "timescale" else "US", city="New York", stage="Seed", stage_src="model",
                 stage_conf="medium", entry_date="2015", grad="graduated", grad_src="web_verified",
                 grad_cite=TC_TIMESCALE, grad_conf="high", focus="Data Infrastructure",
                 flags=["stale"] + extra_flags, extra={"valuation_range_source": "web_verified"},
                 rounds=[rnd("2015", "unnamed", 3712053, None, True, None, "filing"),
                         rnd("2018-01-24", "unnamed", 12400000, "Benchmark", True, TC_TIMESCALE, "press"),
                         rnd("2022-02-22", "Series C", 110000000, "Tiger Global", None,
                             NEWS("timescale", "Valued at Over $1B"), "press")],
                 note=TIMESCALE_NOTE))

L.append(cls("tintri-inc", city="Mountain View", rng="below_1b", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2008", focus="Data Infrastructure",
             note="VM-aware storage, Mountain View; listed 2017, filed Chapter 11 in 2018 and its assets went to DDN. "
                  "Founded in 2008 with NEA and Lightspeed; NEA's Peter Sonsini has sat on the board since 2008 and "
                  "NEA 12 with NEA Ventures 2008 hold the shares (S-1), so NEA entered in the 2008 founding round, "
                  "read as the Series A as in the Lightspeed row. The 2012 Form D date on file is a later round."))

L.append(cls("tivli", status="private", rng="below_1b", city="San Francisco", stage="undetermined", entry_date="2013",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2013-07", "unnamed", 8968187, None, True, None, "filing"),
                     rnd("2013-08-20", "Renamed Philo", None, None, None, NEWS("tivli", "Tivli Rebrands As Philo"),
                         "press")],
             note="Campus TV streaming; Tivli renamed itself Philo in August 2013 (Fast Company), and Philo operates "
                  "today as a live-TV streaming service based in San Francisco, so the Felicis row's acquired is "
                  "contradicted: the company was renamed, not sold. NEA joined the 2013 round (Hugh Panero and Patrick "
                  "Chung on its Form D), which no source names."))

L.append(cls("tivo", country="US", city="San Jose", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("tivo"), stage_conf="medium", entry_date="1997", focus="Consumer & Marketplaces",
             note="Digital video recorders, San Jose (Alviso); listed 1999, merged into Rovi in 2016. The firm labels "
                  "its 1997 entry, the founding year, Seed; the IVP row reads the same first institutional round, "
                  "co-led with NEA, as Series A (model). " + GL))

L.append(cls("together-ai", city="San Francisco", stage="Series A", stage_src="web_verified",
             stage_cite=NEWS("together-ai", "Another generative AI startup"), stage_conf="high",
             entry_date="2023-11-29", focus="AI & Applied AI",
             rounds=[rnd("2023-05-16", "Seed", 20000000, "Lux Capital", False, None, "press"),
                     rnd("2023-11-29", "Series A", 102500000, "Kleiner Perkins", True,
                         NEWS("together-ai", "Another generative AI startup"), "press"),
                     rnd("2024-03-13", "Series A2", 106000000, "Salesforce Ventures", None, None, "press"),
                     rnd("2025-02", "Series B", 305000000, "General Catalyst", None, None, "press"),
                     rnd("2026-07-01", "Series C", 800000000, None, None, None, "press")],
             note="AI cloud for open models, San Francisco. SiliconANGLE (2023-11-29) names NEA among the "
                  "participants in the $102.5M Series A led by Kleiner Perkins; NEA was not in the Lux-led seed. "
                  "Momentum check 2026-09-30: the $800M Series C at $8.3B of July 2026 is the latest priced round, "
                  "matching the pre-filled mark and the sibling rows."))

L.append(cls("tokenz", status="private", rng="below_1b", country="JP", country_src="web_verified",
             country_cite=PR_TOKENZ, city="Tokyo", stage="undetermined", entry_date="2025", focus="Fintech & Payments",
             rounds=[rnd("2026-06-02", "Series A", None, "Headline Asia", True, PR_TOKENZ, "company")],
             note="Merchant-of-record payments for digital content sellers, Tokyo (Chiyoda). The company's release "
                  "for its JPY 1B Series A (June 2026, led by Headline Asia) lists NEA as an existing investor, so NEA "
                  "entered in 2025 in an earlier round no source names. Momentum check 2026-09-30: that Series A is "
                  "the latest round, far below $1B. Aligned with the Headline row."))

L.append(cls("topera", status="acquired", rng="below_1b", country="US", city="Menlo Park", stage="Growth",
             stage_src="web_verified", stage_cite=W("Topera Medical"), stage_conf="high", entry_date="2013-05",
             focus="Healthcare & Bio",
             rounds=[rnd("2013-05", "Series C", 25000000, "NEA", True, W("Topera Medical"), "press"),
                     rnd("2014-10-29", "Acquisition by Abbott", 250000000, None, None, NEWS("topera", "Menlo Park"),
                         "press")],
             note="Cardiac rotor-mapping catheters, Menlo Park; Abbott bought it for $250M upfront in 2014 (Silicon "
                  "Valley Business Journal). Wikipedia: NEA led the $25M Series C of May 2013, the firm's year."))

L.append(cls("topia", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2014", focus="SaaS",
             rounds=[rnd("2025-06-25", "Majority investment by Bow River Capital", None, "Bow River Capital", None,
                         NEWS("topia", "Makes Majority Platform"), "company"),
                     rnd("2026-09-28", "Majority recapitalization completed", None, "Bow River Capital", None,
                         NEWS("topia", "Bow River Capital completes"), "vendor")],
             note="Global mobility and relocation software (formerly MOVE Guides), San Francisco. Bow River Capital "
                  "took a majority stake (announced June 2025, completed September 2026), read as acquired. NEA's "
                  "2014 round is not named in any source read."))

L.append(cls("trackmaven", status="acquired", rng="below_1b", city="Washington", focus="SaaS",
             rounds=[rnd("2014-02-05", "unnamed", 6500000, None, True, NEWS("trackmaven", "raises $6.5M"), "press"),
                     rnd("2018-10-23", "Merger into Skyword", None, None, None,
                         NEWS("trackmaven", "merges with Boston-based Skyword"), "press")],
             note="Competitive intelligence for digital marketers, Washington DC; merged into Skyword in October "
                  "2018 (Technical.ly; the firm's exit line 'Acquired by Skyword'). " + GL))

L.append(cls("tracon-pharmaceuticals", city="San Diego", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=S1_TRACON, stage_conf="medium", entry_date="2014-09", focus="Healthcare & Bio",
             rounds=[rnd("2014-09", "Series B", 25700000, "NEA", True, S1_TRACON, "filing")],
             note="Oncology and ophthalmology antibodies, San Diego. The S-1 (2014) records the September 2014 "
                  "Series B and its investor rights agreement names NEA 14 the Lead Investor; Paul Walker joined the "
                  "board that month. The 2017 Form D date on file is a later round."))

L.append(cls("trading-dynamics", status="acquired", rng="below_1b", country="US", stage="undetermined",
             entry_date="1998", focus="SaaS", flags=["city_unknown"],
             note="Online auction and market-making software; bought by Ariba (the firm's exit line). No source read "
                  "places the company or names NEA's 1998 round."))

L.append(cls("transfix", status="private", city="New York", rng="below_1b", stage="undetermined", entry_date="2016",
             flags=["stage_disputes_band"], focus="Consumer & Marketplaces",
             rounds=[rnd("2023-10-19", "Series F", 40000000, "NEA and G Squared", True,
                         NEWS("transfix", "Series F Funding Round Led by New Enterprise"), "company"),
                     rnd("2024-06-05", "Brokerage unit sold", None, None, None,
                         NEWS("transfix", "Sells Brokerage Unit"), "press")],
             note="Freight marketplace turned freight software, New York; sold its brokerage unit in 2024 and still "
                  "operates. The Growth band rode the 2023 Form D (the Series F NEA co-led), but the firm's own "
                  "listing gives 2016, so NEA entered years earlier in a round no source read names. The 2021 SPAC "
                  "deal at $1.1B was called off; GetLatka's $376M is a vendor figure."))

L.append(cls("transifex", status="acquired", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_cite=SITE("transifex"), stage_conf="medium", entry_date="2014", focus="DevTools & APIs",
             flags=["city_unknown"],
             rounds=[rnd("2022-04-12", "Sale to PARC Partners", None, None, None, NEWS("transifex", "Sold to PARC"),
                         "press"),
                     rnd("2025-01-30", "Acquisition by XTM International", None, None, None,
                         NEWS("transifex", "XTM International Expands"), "company")],
             note="Software localization platform; corporate head office in California with staff mainly in Greece "
                  "(Slator), no city given. Sold to PARC Partners in 2022 and acquired by XTM International in 2025. "
                  "Entry 2014 at Seed on the firm's own label. " + GL))

L.append(cls("translucent", status="private", rng="below_1b", country="US", city="New York", stage="undetermined",
             entry_date="2025", focus="Healthcare & Bio",
             rounds=[rnd("2025-08", "Seed", 7000000, None, None, None, "press"),
                     rnd("2026-03-11", "Series A", 27000000, "GV", True,
                         NEWS("translucent", "Translucent Raises $27M to Replace"), "press")],
             note="Agentic AI for financial planning at health systems; placed in New York on AlleyWatch's NYC "
                  "coverage. NEA took part in the $27M Series A led by GV (AlleyWatch, March 2026); the firm's year is "
                  "2025, which may be the $7M seed of August 2025 or the Series A's close, so the entry round is "
                  "undetermined. Momentum check 2026-09-30: the Series A is the latest round, no $1B mark."))

L.append(cls("transvascular", status="acquired", rng="below_1b", country="US", city="Menlo Park",
             stage="undetermined", entry_date="1996", focus="Healthcare & Bio",
             note="Catheter systems for vascular disease, Menlo Park; bought by Medtronic (the firm's exit line). "
                  "NEA's 1996 round is not named in any source read."))

L.append(cls("travelbank", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2015", focus="Fintech & Payments",
             rounds=[rnd("2016-10-20", "unnamed", 10000000, None, None, NEWS("travelbank", "TravelBank collects"),
                         "press")],
             note="Travel and expense software, San Francisco; bought by U.S. Bancorp in 2021 (the firm's exit line). "
                  "NEA's 2015 round is not named in any source read."))

L.append(cls("trevena", city="Chesterbrook", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=W("Trevena, Inc."), stage_conf="high", entry_date="2008", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2008", "Series A", 25000000, "Alta, Polaris, NEA, HealthCare Ventures", True,
                         W("Trevena, Inc."), "press")],
             note="GPCR biased-ligand drugs, Chesterbrook, Pennsylvania (the Form Ds give nearby King of Prussia). "
                  "Wikipedia: NEA co-led the $25M Series A in 2008, the firm's year; the Growth band rode the 2010 "
                  "Form D, a later round."))

L.append(cls("trevi-therapeutics", city="New Haven", stage="Growth", stage_src="first_party",
             stage_cite=SITE("trevi-therapeutics"), stage_conf="medium", entry_date="2017", focus="Healthcare & Bio",
             note="Nalbuphine ER for chronic cough, New Haven. Entry 2017 at Growth on the firm's own label (the "
                  "$66.7M 2017 Form D round); the 2021 Form D date on file is a later round."))

L.append(cls("tri-alpha-energy", status="private", rng="1b_plus", usd=6000000000, val_src="web_verified",
             val_cite=S4_TAE, asof="2025-12-18", country="US", city="Lake Forest", stage="Growth",
             stage_src="web_verified", stage_cite=S4_TAE, stage_conf="medium", entry_date="2010",
             focus="Climate & Energy", flags=["stage_disputes_band"], extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2025-12-18", "Merger agreement with Trump Media & Technology Group", 6000000000, None, None,
                         S4_TAE, "filing")],
             note="Fusion power (TAE Technologies), Foothill Ranch in Lake Forest, California. Mark: the S-4 of "
                  "September 2026 values TAE at about $6.0B equity ($53.89 per share) under the all-stock merger "
                  "agreement with Trump Media of 2025-12-18; the deal has not closed (expected Q4 2026), so the row "
                  "stays private at the agreed price. Stage: the S-4 shows NEA 10, NEA 11 and NEA Ventures 2006 "
                  "holding Series 4 preferred and later series, none earlier, so NEA entered at a fourth series: "
                  "Growth, which replaces the firm's Seed label."))

L.append(cls("tripod", status="acquired", rng="below_1b", country="US", city="Williamstown", stage="undetermined",
             entry_date="1996", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             note="Web hosting and online community, Williamstown, Massachusetts; bought by Lycos in 1998 (the firm's "
                  "exit line). The pre-filled GB country is a one-word name match and is disputed. NEA's 1996 round "
                  "is not named in any source read."))

jl.write("c10b", L)
