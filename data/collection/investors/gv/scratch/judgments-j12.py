"""PRO-75 GV, judge j12: queue batch 12 (science-37 .. stamped), 45 member rows.
Every citation is read from disk through the helpers, printed by a tool, or a page read with WebFetch that says
what is cited. Run from scratch/: NQ_TAG=j12 python3 judgments-j12.py"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, CASE, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.CASE, jl.SITE,
                                                            jl.ARCH, jl.W, jl.NEWS, jl.FTS)
WV = {"valuation_range_source": "web_verified"}
L = []

# ---- pages read with WebFetch (URLs printed by a tool: sibling rows, EDGAR listings, decoded headlines)
TC_SNOWBALL = "https://techcrunch.com/2014/10/08/snowball-debuts-a-unified-inbox-for-all-your-messaging-apps/"
TC_STACKBLITZ = "https://techcrunch.com/2022/04/06/stackblitz-raises-7-9m-to-bring-a-better-ide-to-your-browser/"
TC_SIERRA = "https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/"
TC_SIGNPOST = "https://techcrunch.com/2010/10/20/signpost-local-deals/"
TC_STAMPED = "https://techcrunch.com/2011/11/21/stamped-approval/"
CALCALIST_JOYTUNES = "https://www.calcalistech.com/ctech/articles/0,7340,L-3910571,00.html"
FORTUNE_SKYPORT = "https://fortune.com/2016/03/15/gv-cisco-fund-skyport-systems/"
RPM_SKYCATCH = "https://rpmglobal.com/caterpillar-expands-mining-technology-capabilities-with-skycatch-acquisition/"
STACKONE_ABOUT = "https://www.stackone.com/about"
SEISMIC_A = ("https://seismictx.com/seismic-therapeutic-launches-with-101-million-series-a-financing-to-usher-in-a-new-"
             "era-of-immunology-drug-development-integrating-machine-learning/")
SEISMIC_B = ("https://seismictx.com/seismic-therapeutic-closes-121-million-series-b-financing-to-advance-immunology-"
             "pipeline-optimized-by-its-machine-learning-platform/")
ACCEL_SENSE = "https://www.accel.com/companies/sense"
SPERO_S1 = "https://www.sec.gov/Archives/edgar/data/1701108/000119312517305888/d431217ds1.htm"
SQZ_8K = "https://www.sec.gov/Archives/edgar/data/1604477/000119312523302228/d199412d8k.htm"
SQZ_S1 = "https://www.sec.gov/Archives/edgar/data/1604477/000119312520267294/d877186ds1.htm"
SSN_S1 = "https://www.sec.gov/Archives/edgar/data/1180079/000119312511184100/ds1.htm"
GRAD_LEFT = "Graduation left for the graduation pass."

# ---------------------------------------------------------------- rows
# segment: the firm's own post names the Series C (2017) as the round the partner invested in.
L.append(cls("segment", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=POST("segment-twilio"),
             entry_date="2017",
             note="Customer data platform (San Francisco). The firm's own post (Dave Munichiello, 2020-10-12): "
                  "'I was thrilled to invest in the company's Series C in 2017', and GV then co-led the 2019 Series D "
                  "with Meritech. The 2017 Series C was the $64M round that YC Continuity led (Business Journals "
                  "headline, 2017-07-13). Twilio agreed to buy Segment for $3.2B in stock in October 2020; the firm's "
                  "exit line reads 'Acquired by Twilio, 2020'. Aligned with the Accel, Thrive, Headline and YC rows.",
             rounds=[rnd("2017-07-13", "Series C", 64000000, "YC Continuity", True,
                         NEWS("segment", "Y Combinator growth fund chief leads"), "press"),
                     rnd("2019", "Series D", None, "GV, Meritech", True, POST("segment-twilio"), "firm")]))

# skyport-systems: GV led the $30M Series C and is not among the existing investors (Fortune).
L.append(cls("skyport-systems", status="acquired", rng="below_1b", country="US", city="Mountain View",
             focus="Security", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=FORTUNE_SKYPORT, entry_date="2016-03-15",
             note="Secure computing infrastructure for enterprise applications (Mountain View). GV led the $30M "
                  "Series C announced 2016-03-15 (Fortune), with Cisco Investments, Thomvest, Northgate and "
                  "InstantScale new and Index Ventures, Intel Capital and Sutter Hill named as the existing "
                  "investors; GV is not among them, so the Series C is its entry. Cisco bought the company (the "
                  "firm's exit line 'Acquired by Cisco, 2018'). Aligned with Sutter Hill's row.",
             rounds=[rnd("2016-03-15", "Series C", 30000000, "GV", True, FORTUNE_SKYPORT, "press")]))

# sidequest: the firm's post announces the Series A it led as its first VR investment in a while.
SR_SIDEQUEST = NEWS("sidequest", "Google Ventures leads $12m funding for Belfast")
L.append(cls("sidequest", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=SR_SIDEQUEST, city="Belfast", focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="first_party", stage_conf="high",
             stage_cite=POST("back-to-virtual-reality-sidequest"), entry_date="2022-10-03",
             note="VR content store and developer testing platform, Belfast (Silicon Republic: 'Belfast-based VR "
                  "start-up SideQuest'). The firm's own post of 2022-10-03: 'GV making our first VR-related investment "
                  "in quite a while: We are leading a $12 million Series A investment in SideQuest'. The earlier "
                  "rounds carry no GV: a $650K pre-seed in 2020 (Palmer Luckey) and a $3M seed in October 2021 led "
                  "by ProFounders (Silicon Republic). Still operating and independent on the news read; no round at "
                  "$1B or more.",
             rounds=[rnd("2020-09", "Pre-Seed", 650000, "Palmer Luckey", False, SR_SIDEQUEST, "press"),
                     rnd("2021-10", "Seed", 3000000, "ProFounders", False, SR_SIDEQUEST, "press"),
                     rnd("2022-10-03", "Series A", 12000000, "GV", True,
                         POST("back-to-virtual-reality-sidequest"), "firm")]))

# sesame: the firm's case study gives the first round (Series B); the company's release names GV as the lead.
PRN_SESAME = NEWS("sesame", "SESAME SECURES $27 MILLION SERIES B")
L.append(cls("sesame", status="private", rng="below_1b", city="New York", focus="Healthcare & Bio",
             stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=CASE("sesame-care"),
             entry_date="2021",
             note="Sesame (sesamecare.com), a cash-pay marketplace for medical care, New York. The firm's own case "
                  "study reads 'First Round: Series B', 'Date Invested: 2021' (a close year). The company's release "
                  "(New York, 2022-06-14) announced the $27M Series B led by GV, naming General Catalyst, Industry "
                  "Ventures, Coefficient Capital, Giant Ventures and Alumni Ventures as the existing investors. "
                  "Operating and private; no round near $1B found. Name collision: the a16z, Redpoint and Spark rows "
                  "named Sesame are the San Francisco voice-AI company (Brendan Iribe), not this one; General "
                  "Catalyst's row is this company.",
             rounds=[rnd("2022-06-14", "Series B", 27000000, "GV", True, PRN_SESAME, "company")]))

# sierra: the firm's case study gives 'First Round: Series E' (2026); the headline gives the $15.8B mark.
AXIOS_SIERRA = NEWS("sierra", "Sierra locks up $950M at a $15.8B")
L.append(cls("sierra", status="private", rng="10b_plus", usd=15800000000, val_src="web_verified",
             val_cite=AXIOS_SIERRA, asof="2026-05-04", country="US", city="San Francisco",
             focus="AI & Applied AI", stage="Growth", stage_src="first_party", stage_conf="high",
             stage_cite=CASE("sierra"), entry_date="2026-05-04", extra=WV,
             note="Enterprise customer-service AI agents (Bret Taylor, Clay Bavor), San Francisco. The firm's own "
                  "case study reads 'First Round: Series E', invested 2026, and its post of 2026-05-04 says GV is "
                  "co-leading the Series E; the /ai list gives the first investment as 2026-05. TechCrunch "
                  "(2026-05-04): $950M led by Tiger Global and GV at a post-money valuation above $15B; the Axios "
                  "headline gives $15.8B. Mark aligned with the Sequoia and Thrive rows (15.8B, 2026-05-04). "
                  "Momentum slice: the mark itself is the check (priced round, 2026-05-04).",
             rounds=[rnd("2026-05-04", "Series E", 950000000, "Tiger Global, GV", True, TC_SIERRA, "press")]))

# spero-therapeutics: the S-1 shows GV 2015, L.P. holding only Series C preferred, bought in the March 2017 round.
SA_SPRO = "https://stockanalysis.com/stocks/spro/market-cap/"
L.append(cls("spero-therapeutics", country="US", city="Cambridge", focus="Healthcare & Bio",
             rng="below_1b", usd=69300000, val_src="web_verified", val_cite=SA_SPRO, asof="2026-09-28", extra=WV,
             flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SPERO_S1, entry_date="2017-03",
             note="Antibacterial drug developer, Cambridge MA (the S-1's principal office, 675 Massachusetts "
                  "Avenue). The S-1 (2017-10-06): in March 2017 the company sold Class C preferred units at $1.7749 "
                  "for about $43.2M, of which GV 2015, L.P. bought 6,760,944 units for $12.0M, and the principal "
                  "stockholders table lists GV 2015, L.P. holding only Series C preferred, so the Class C round was "
                  "its entry. The Class A and B unit rounds (2015, 2016) carry no GV. Public (NASDAQ: SPRO) since the "
                  "November 2017 IPO; market cap $69.30M as of 2026-09-28 (stockanalysis.com), which replaces the recorded "
                  "$160.3M figure as the canonical public mark; below_1b either way.",
             rounds=[rnd("2017-03", "Series C", 43177052, None, True, SPERO_S1, "filing")]))

# slack: GV 2014, L.P. is the vehicle on the investor rights agreement; GV co-led the October 2014 round.
L.append(cls("slack", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=W("Slack Technologies"),
             entry_date="2014",
             note="Team messaging (San Francisco). The company's 2019 investor rights agreement (S-1/A exhibit 4.2) "
                  "lists GV 2014, L.P. and GV 2017, L.P. as investors and no Google Ventures 2011 vehicle, so GV "
                  "came in during 2014, after the 2010 Series A (Accel, Andreessen Horowitz) and the 2011 Series B. "
                  "Wikipedia: in October 2014 the company raised $120M at a $1.2B valuation led by Kleiner Perkins "
                  "and GV. Whether GV also joined the April 2014 round is not established; either way the entry is "
                  "a Series C or D, so Growth. Direct listing on NYSE in June 2019, bought by Salesforce in July "
                  "2021 (acquired, as the status already reads).",
             rounds=[rnd("2014-10", "Series D", 120000000, "Kleiner Perkins, GV", True, W("Slack Technologies"),
                         "press")]))

# space-monkey: Wikipedia names the 2012 Series A that Google Ventures led, the company's first venture round.
L.append(cls("space-monkey", status="acquired", rng="below_1b", city="Salt Lake City",
             focus="Consumer & Marketplaces", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=W("Space Monkey (company)"), entry_date="2012",
             note="Peer-to-peer cloud storage on a home device (Utah). Wikipedia: founded 2011, won TechCrunch's "
                  "Launch Festival in March 2012, and 'raised $2.7 million of venture capital in a Series A round led "
                  "by Google Ventures that same year'; no earlier venture round is recorded, so the Series A is the "
                  "firm's entry. Vivint bought the company in September 2014 (Wikipedia; Forbes headline "
                  "2014-09-10; the firm's exit line 'Acquired by Vivint, 2014').",
             rounds=[rnd("2012", "Series A", 2700000, "Google Ventures", True, W("Space Monkey (company)"),
                         "press")]))

# simply: the pre-filled 'acquired' belongs to another company; JoyTunes (Simply) is private, Tel Aviv.
L.append(cls("simply", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
             val_cite=CALCALIST_JOYTUNES, asof="2021-06-21", country="IL", country_src="web_verified",
             country_cite=CALCALIST_JOYTUNES, city="Tel Aviv", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-03",
             flags=["model_disputes_source", "stale"], extra=WV,
             note="Simply (formerly JoyTunes), music and hobby learning apps, Israel (Calcalist 2021-06-21: 'The "
                  "Israeli startup', all 100 staff in Israel); IL confirmed. The pre-filled status 'acquired' is a "
                  "name match on another company and is disputed: the firm's live listing carries no exit line, "
                  "Insight's row reads private, and no sale appears in the news read. Entry: the firm's /ai list "
                  "dates GV's first investment 2020-03 (then 2021-04). Wikipedia records a $5M Series A in August "
                  "2014 (Aleph) and a $25M round led by Qumra in 2019, so any 2020 round is at least the third priced "
                  "round: Growth, round not named. Mark: $50M at a $1B valuation led by GV, which put in $25M "
                  "(Calcalist, 2021-06-21); no later priced round found, so stale. Aligned with Insight's row.",
             rounds=[rnd("2014-08", "Series A", 5000000, "Aleph", False, W("Simply (software company)"), "press"),
                     rnd("2019", None, 25000000, "Qumra Capital", None, W("Simply (software company)"), "press"),
                     rnd("2021-06-21", None, 50000000, "GV", True, CALCALIST_JOYTUNES, "press")]))

# sift: Sift Stack (El Segundo); the pre-filled $1B band belongs to Sift Science, the fraud company.
L.append(cls("sift", rng="below_1b", usd=274000000, val_src="web_verified",
             val_cite=NEWS("sift", "With Sift, two ex-SpaceX engineers"), asof="2026-03-25",
             city="El Segundo", city_src="web_verified", focus="Data Infrastructure",
             flags=["model_disputes_source"], extra=WV,
             note="Sift Stack, telemetry and observability software for hardware engineering, founded 2022 by two "
                  "ex-SpaceX engineers, El Segundo (the Series A release dateline, the 2024 Form D address and "
                  "TechCrunch 2026-03-25). GV led the $17.5M Series A of June 2024 (the company's release), which is "
                  "the Series A already recorded. The pre-filled $1B band and figure are a name match on Sift (formerly "
                  "Sift Science, the San Francisco fraud company that the Insight, Spark, First Round and YC rows "
                  "hold) and are disputed: TechCrunch (2026-03-25) reports the $42M Series B led by StepStone, GV "
                  "participating, raised in 2025 at a $274M post-money valuation. Momentum slice checked 2026-09-28: "
                  "no round at $1B or more. Name collision with the four sibling rows named Sift.",
             rounds=[rnd("2023-11-07", "Seed", 7500000, "Riot Ventures", False, W("Sift (company)"), "press"),
                     rnd("2024-06-25", "Series A", 17500000, "GV", True,
                         NEWS("sift", "Sift Raises $17.5M Series A to Propel"), "company"),
                     rnd("2025", "Series B", 42000000, "StepStone", True,
                         NEWS("sift", "With Sift, two ex-SpaceX engineers"), "press")]))

# seismic-therapeutic: the company's launch release names GV in the Lightspeed-led $101M Series A.
L.append(cls("seismic-therapeutic", status="private", rng="below_1b", country="US", city="Watertown",
             focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=SEISMIC_A, entry_date="2021-12",
             note="Machine-learning immunology biologics, Watertown MA (launch release dateline). The company's "
                  "release of 2022-02-09: $101M Series A led by Lightspeed with Timothy Springer, Polaris, GV, Boxer "
                  "and Samsara; the firm's /ai list dates GV's first investment 2021-12, the round's close, so the "
                  "Series A is the entry. GV re-invested in the $121M Series B led by Bessemer (release 2023-12-04, "
                  "GV among the existing investors). Private, no round near $1B. Aligned with Lightspeed's row.",
             rounds=[rnd("2022-02-09", "Series A", 101000000, "Lightspeed", True, SEISMIC_A, "company"),
                     rnd("2023-12-04", "Series B", 121000000, "Bessemer Venture Partners", True, SEISMIC_B,
                         "company")]))

# sensorum-health: no round found; the /ai list dates the firm's investment 2022-07.
L.append(cls("sensorum-health", status="private", rng="below_1b", country="US", city="New York",
             focus="Healthcare & Bio", stage="undetermined", entry_date="2022-07",
             note="Passive-sensor home monitoring and clinical services for older adults with chronic conditions, "
                  "New York (the company's site: 315 W 36th St). The firm's /ai list dates GV's only investment "
                  "2022-07 (an anchor, not a label). The news search found partnership releases (Intermountain "
                  "Health, 2024-03-29 and 2026-03-10) and no funding round, so the round GV entered is not named: "
                  "undetermined. Operating; nothing suggests a valuation near $1B.",
             rounds=[]))

# secret-escapes: Google Ventures led the $60M Series C of July 2015 (Growth Business).
GB_SECRET = NEWS("secret-escapes", "Secret Escapes raises $60m in Series C")
L.append(cls("secret-escapes", status="private", rng="below_1b", city="London", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GB_SECRET, entry_date="2015-07",
             note="Members-only luxury hotel and travel flash sales, London (Growth Business: 'London-based'). Google "
                  "Ventures led the $60M Series C closed by 2015-07-27, with Octopus Ventures (an investor since the "
                  "early stages), Index Ventures and Atlas Venture; GV is not named as an existing investor, so the "
                  "Series C is its entry. Private and operating: Travel Weekly headlines of 2024-09 ('recovers to "
                  "operating profit') and 2026-01 ('enters year debt free after disposal of subsidiary brand'); the "
                  "2019 sale talk was at about GBP 500M (The Telegraph headline), below $1B, and no priced round at "
                  "$1B or more was found. The 2014-2015 archive captures and the M.G. Siegler tag on this row belong "
                  "to Secret, the anonymous-sharing app (secret.ly), which the rebuild splits off.",
             rounds=[rnd("2015-07", "Series C", 60000000, "Google Ventures", True, GB_SECRET, "press")]))

# shape-security: Google Ventures joined the 2012 Series A (the company's own release, GlobeNewswire).
GNW_SHAPE_A = "https://www.globenewswire.com/news-release/2012/07/02/969278/0/en/Google-Ventures-Joins-Shape-Security-Series-A-Funding-Round.html"
L.append(cls("shape-security", status="acquired", rng="below_1b", country="US", city="Mountain View",
             focus="Security", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=GNW_SHAPE_A, entry_date="2012-07-02",
             note="Bot and fraud defence for web applications, Mountain View (the 2012 release: 'Based in Mountain "
                  "View, CA'; VentureBeat 2016: 'Founded out of Mountain View'). The company's release of 2012-07-02, "
                  "'Google Ventures Joins Shape Security Series A Funding Round', alongside Kleiner Perkins, "
                  "TomorrowVentures and Baseline; the company's first Form D (first sale 2012-04-09, $5.58M sold) is "
                  "that Series A, so GV entered at the A. GV stayed in through the 2016 $40M Series D as an existing "
                  "investor (VentureBeat 2016-09-29). F5 agreed in December 2019 to buy Shape for about $1B (GeekWire "
                  "headline; the firm's exit line 'Acquired by F5, 2019'); acquired, so below_1b with no figure.",
             rounds=[rnd("2012-04-09", "Series A", 5584998, "Kleiner Perkins", True, GNW_SHAPE_A, "company"),
                     rnd("2012-12-21", None, 20000001, None, None,
                         "https://www.sec.gov/Archives/edgar/data/1548097/000154809713000001/0001548097-13-000001-index.htm",
                         "filing"),
                     rnd("2014-02-21", None, 40000154, None, None,
                         "https://www.sec.gov/Archives/edgar/data/1548097/000154809714000001/0001548097-14-000001-index.htm",
                         "filing"),
                     rnd("2016-09-29", "Series D", 40000000, None, True,
                         NEWS("shape-security", "Shape Security closes $40 million round"), "press")]))

# sold: Boston seed-stage company; Dropbox bought it in November 2013 and shut the product.
TC_SOLD = ("https://techcrunch.com/2013/11/04/dropbox-snatches-up-sold-the-service-that-simplifies-selling-online-to-"
           "help-it-build-a-new-mystery-ecommerce-product/")
VB_SOLD = "https://venturebeat.com/entrepreneur/dropbox-buys-sold-which-helped-other-people-sell-their-stuff"

# science-37: GV came in new in the $29M Series C of April 2017 (pharmaphorum).
PH_S37 = NEWS("science-37", "Science 37 gets funding to develop")
L.append(cls("science-37", rng="below_1b", country="US", city="Durham", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PH_S37, entry_date="2017-04-27",
             note="Decentralised ('site-less') clinical trials. pharmaphorum (2017-04-27): a $29M Series C led by "
                  "Glynn Capital, with Amgen Ventures and 'Google's investment arm, GV' new to the round, after "
                  "$38M from pharma venture arms; the firm's listing starts in 2017, so the Series C is its entry. "
                  "Listed through the 2021 SPAC merger with LifeSci Acquisition II, then taken private by eMed, whose "
                  "tender offer completed in March 2024 (PR Newswire) for about $38M: acquired, below_1b. City "
                  "aligned with Lux's row (Durham, the Research Triangle base it moved to from Los Angeles).",
             rounds=[rnd("2015", None, 6500000, "Lux Capital, dRx Capital", False, W("Science 37"), "press"),
                     rnd("2016", None, 31000000, None, False, W("Science 37"), "press"),
                     rnd("2017-04-27", "Series C", 29000000, "Glynn Capital", True, PH_S37, "press"),
                     rnd("2020-08", "Series D", 40000000, "Lux Capital, Redmile, PPD", True, W("Science 37"), "press")]))

# soylent: GV led the $50M Series B of May 2017; the existing investors named do not include GV (Food Dive).
FD_SOYLENT = NEWS("soylent", "Soylent gains $50M in series B")
L.append(cls("soylent", status="acquired", rng="below_1b", city="Los Angeles", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=FD_SOYLENT, entry_date="2017-05",
             note="Meal-replacement drinks, Los Angeles. Food Dive (2017-05-08): a $50M Series B led by GV, with Tao "
                  "Capital Partners new and Lerer Hippeau and Andreessen Horowitz as existing investors, bringing the "
                  "total to $74.5M; GV is not among the existing investors, so the Series B is its entry (Wikipedia: "
                  "Andreessen Horowitz led the $20M Series A of January 2015). Starco Brands bought Soylent in 2023 "
                  "(the firm's exit line 'Acquired by Starco Brands, 2023'; decisions D11 keeps Starco out and "
                  "Soylent in). Aligned with the a16z and YC rows.",
             rounds=[rnd("2015-01", "Series A", 20000000, "Andreessen Horowitz", False,
                         W("Soylent (meal replacement)"), "press"),
                     rnd("2017-05-03", "Series B", 50000000, "GV", True, FD_SOYLENT, "press")]))

# signpost: Google Ventures took an undisclosed stake in October 2010, after Spark's $1M seed; round not named.
BW_SIGNPOST = NEWS("signpost", "Hibu, an H.I.G. Portfolio Company, Acquires")
L.append(cls("signpost", status="acquired", rng="below_1b", city="New York", focus="SaaS",
             stage="undetermined", entry_date="2010-10",
             note="Marketing software for local businesses (began as a local-deals site), New York (Wikipedia). "
                  "TechCrunch (2010-10-20): Google Ventures is 'taking a stake' in Signpost, size undisclosed, after "
                  "the '$1 million seed round Signpost raised earlier this year from Spark Capital'; no source names "
                  "the round GV bought into, so the stage is undetermined (it sat between the Spark seed and the "
                  "company's later rounds; Spark's row records the $10.58M offering of 2013-11-12 on the company's "
                  "Form D, CIK 1484639). Status: Hibu, an H.I.G. portfolio company, acquired Signpost's marketing "
                  "technology platform in September 2023 (Business Wire headline 2023-09-11; Carlsquare: 'Signpost "
                  "sold its software business to Hibu'), a sale of the business, so acquired; this is fresher than "
                  "Spark's 'unknown', which should be re-read.",
             rounds=[rnd("2010-02", "Seed", 1000000, "Spark Capital", False, TC_SIGNPOST, "press"),
                     rnd("2010-10", None, None, None, True, TC_SIGNPOST, "press")]))

# silver-spring-networks: the S-1 and the IPO prospectus name no Google entity; the firm's round is not documented.
L.append(cls("silver-spring-networks", rng="below_1b", city="San Jose", focus="Climate & Energy",
             stage="undetermined",
             note="Smart-grid networking for utilities; Redwood City at the 2013 IPO, San Jose from 2016 (Wikipedia). "
                  "Itron bought it in January 2018 for $830M (acquired, as already recorded). The firm lists it (exit "
                  "line 'NYSE: SSNI') from its first 2012 capture, but neither the 2011 S-1 nor the 2013 prospectus "
                  "names Google or Google Ventures, and no press found names GV's round. The S-1's related-party "
                  "section dates the Series C (April 2007 to March 2008, $56.8M), Series D (October 2008 to March 2009, "
                  "$90.0M) and Series E (December 2009, $105.0M); Google Ventures began in March 2009, so any position "
                  "it held is Series D or later, but without a dated source the stage stays undetermined.",
             rounds=[rnd("2007-04", "Series C", 56800000, None, False, SSN_S1, "filing"),
                     rnd("2008-10", "Series D", 90000000, None, None, SSN_S1, "filing"),
                     rnd("2009-12", "Series E", 105000000, None, None, SSN_S1, "filing")]))

# snowball: GV (MG Siegler) was in the $2.3M seed of October 2014; Credit Karma acquired the company in December 2015.
BK_SNOWBALL = NEWS("snowball", "Canadian-founded Snowball acquired by Credit Karma")
L.append(cls("snowball", status="acquired", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SNOWBALL,
             entry_date="2014-10-08", flags=["model_disputes_source", "city_unknown"],
             note="Snowball (trysnowball.com), an Android app that gathered messages from several chat apps into one "
                  "inbox. TechCrunch (2014-10-08): a $2.3M seed led by First Round (Bill Trenchard) with 'Google "
                  "Ventures' MG Siegler', Felicis, Lowercase and others; the firm's listing starts in 2014, so the "
                  "seed is its entry. BetaKit (2015-12-30): 'Canadian-founded Snowball acquired by Credit Karma', "
                  "the app to leave the Play Store and its technology to be integrated into Credit Karma's apps: an "
                  "announced acquisition that took the technology, so acquired (the firm's exit line 'Acquired by "
                  "Credit Karma, 2015'). This disagrees with the Felicis and First Round rows (defunct), which lack "
                  "this citation. The pre-filled CN is a one-word Wikidata match on Snowball (Xueqiu), the Chinese "
                  "investing app, and is disputed; no source read places the company in a city. " + GRAD_LEFT,
             rounds=[rnd("2014-10-08", "Seed", 2300000, "First Round Capital", True, TC_SNOWBALL, "press")]))

# solveai: GV led the $45M Series A (closed November 2025, announced February 2026); Accel led the pre-seed.
UKTN_SOLVE = NEWS("solveai", "Google Ventures leads SolveAI")
FORTUNE_SOLVE = NEWS("solveai", "Exclusive: SolveAI, at eight months old")
L.append(cls("solveai", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=UKTN_SOLVE, city="London", focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FORTUNE_SOLVE,
             entry_date="2025-11",
             extra={"valuation_range_source": "web_verified", "valuation_citation": FORTUNE_SOLVE,
                    "valuation_asof": "2026-02-25"},
             note="AI platform for employees to build compliant enterprise software, London, founded July 2025 by a "
                  "former Palantir engineer. Fortune (2026-02-25): $50M raised, a $5M Accel-led pre-seed in August "
                  "and a $45M Series A led by Google Ventures in November, with Northzone, Mantis and NeverLift; UKTN "
                  "(2026-02-26) gives the same Series A (GBP 33.3M) and calls Accel's round a seed. The firm's /ai "
                  "list dates GV's first investment 2026-02 (the announcement); the Series A is its entry. Momentum "
                  "slice checked 2026-09-28: no valuation disclosed and no later round found, so below_1b. Accel's "
                  "row reads Series A (model) for Accel, which both sources put at the pre-seed or seed.",
             rounds=[rnd("2025-08", "Pre-Seed", 5000000, "Accel", False, FORTUNE_SOLVE, "press"),
                     rnd("2025-11", "Series A", 45000000, "Google Ventures", True, FORTUNE_SOLVE, "press")]))

# smarterer: Google Ventures backed the $1.25M seed of 2011 and followed in the $1.75M Series A of 2012.
GVB_SMARTERER = "https://globalventuring.com/blog/2012/06/06/google-ticks-off-1-75m-for-smarterer/"
TC_SMARTERER = "https://techcrunch.com/2011/06/13/smarterer-raises-1-25m-to-prove-youre-good-at-anything-in-60-seconds-or-less"
L.append(cls("smarterer", status="acquired", rng="below_1b", country="US", city="Boston",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=GVB_SMARTERER, entry_date="2011-06-13",
             grad="graduated", grad_src="web_verified", grad_cite=GVB_SMARTERER, grad_conf="high",
             note="Crowdsourced skills-assessment tests, Boston (TechCrunch 2011: 'The Boston-based team'). "
                  "TechCrunch (2011-06-13): $1.25M from True Ventures and Google Ventures plus angels; Global Venturing "
                  "(2012-06-06): Google Ventures 'also backed Smarterer's $1.25m seed round last year' and joined the "
                  "$1.75M Series A led by True Ventures, so the seed is the entry and the named Series A graduates the "
                  "row. Pluralsight bought Smarterer for $75M in November 2014 (Wikipedia, Pluralsight; the firm's "
                  "exit line 'Acquired by Pluralsight, 2014').",
             rounds=[rnd("2011-06-13", "Seed", 1250000, "True Ventures, Google Ventures", True, TC_SMARTERER,
                         "press"),
                     rnd("2012-06", "Series A", 1750000, "True Ventures", True, GVB_SMARTERER, "press")]))

# singlestore: Google Ventures co-led the 2018 Series D (Wikipedia's funding table); Vector Capital took a majority in 2025.
TT_SINGLESTORE = NEWS("singlestore", "SingleStore agrees to growth buyout")
VECTOR_PORTFOLIO = "https://www.vectorcapital.com/portfolio"
L.append(cls("singlestore", status="acquired", rng="below_1b", city="San Francisco", focus="Data Infrastructure",
             stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=W("SingleStore"),
             entry_date="2018",
             note="Distributed SQL database (formerly MemSQL), San Francisco. Wikipedia's funding table: Series A 2013 "
                  "(DVCA, IA Ventures), B 2014 (Accel), C 2016 (Caffeinated, REV), D 2018 $30M led by Google Ventures "
                  "and Glynn Capital; the firm's listing starts in 2018 and no earlier round names GV, so the Series D "
                  "is taken as its entry (medium). Vector Capital agreed a growth buyout for a majority stake on "
                  "2025-09-10 (TechTarget; Bloomberg put the investment near $500M, terms undisclosed), with GV among "
                  "the holders staying in (Blocks and Files); Vector's portfolio page now lists SingleStore, so the "
                  "sale is read as completed: acquired. Aligned with Insight's row; the Accel, First Round and YC rows "
                  "still read private.",
             rounds=[rnd("2018", "Series D", 30000000, "Google Ventures, Glynn Capital", True, W("SingleStore"),
                         "press"),
                     rnd("2025-09-10", "Buyout (majority)", None, "Vector Capital", None, TT_SINGLESTORE, "press")]))

# snyk: GV came in new in the $22M round of September 2018, which the company's press names the Series B.
GLOBES_SNYK = NEWS("snyk", "Israeli open source security co Snyk raises")
SNYK_BASE = dict(country="US", country_src="web_verified", country_cite=W("Snyk"), city="Boston", focus="Security",
                 stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GLOBES_SNYK,
                 entry_date="2018-09-25")
SNYK_NOTE = ("Developer-first security (founded 2015 in Tel Aviv and London), headquartered in Boston (Wikipedia); the "
             "pre-filled GB is a Wikidata country on a one-word name and is replaced by US (the headquarters), as "
             "Coatue's row has it. Globes (2018-09-25): a $22M Series B led by Accel, with GV and existing investors "
             "Boldstart and Heavybit, after a $7M Series A in March 2018; the firm's /ai list dates GV's first "
             "investment 2018-09, so the September 2018 round is its entry: Growth. The firm's own later posts call "
             "that round Snyk's 2018 'Series A'; the contemporaneous record names it the Series B and a separate "
             "Series A before it, so the label follows the record.")

# stamped: backed by Google Ventures and Bain Capital Ventures at its November 2011 launch; round not named.
TNW_STAMPED = "https://thenextweb.com/news/google-only-funds-1-consumer-project-in-nyc-its-called-stamped"
L.append(cls("stamped", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces", stage="undetermined", entry_date="2011",
             note="Recommendation app from ex-Googlers, New York. At the November 2011 launch TechCrunch wrote 'The "
                  "company is backed by Bain Capital and Google Ventures' and The Next Web called it 'the only NYC "
                  "based consumer project funded by Google Ventures' (both 2011-11-21); neither names the round or "
                  "its size, so the stage is undetermined (Bain's row reads the same launch financing as a seed, "
                  "model). A July 2012 relaunch brought in celebrity investors (Business Insider headline). Yahoo "
                  "bought Stamped in October 2012 (Business Insider headline 2012-10-25; the firm's exit line "
                  "'Acquired by Yahoo!, 2012').",
             rounds=[rnd("2011", None, None, "Bain Capital Ventures, Google Ventures", True, TC_STAMPED, "press")]))

# sold: $1.2M from Google Ventures, Greylock, Matrix and Boston Seed, no round named; Dropbox bought it in November 2013.
L.append(cls("sold", status="acquired", rng="below_1b", country="US", city="Boston", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Sold, a Boston service that priced, listed and shipped items people wanted to sell (VentureBeat: "
                  "'Boston-based Sold launched in April' 2013). TechCrunch (2013-11-04): Sold had raised $1.2M from "
                  "investors including Google Ventures, Greylock, Matrix and Boston Seed, round not named, so the "
                  "stage is undetermined. Dropbox bought Sold in November 2013 ('Dropbox Snatches Up Sold', "
                  "TechCrunch; 'Dropbox buys Sold', VentureBeat): the nine staff joined Dropbox and the service shut. "
                  "The purchase was announced as an acquisition, so acquired (the firm's exit line 'Acquired by "
                  "Dropbox, 2013').",
             rounds=[rnd(None, None, 1200000, None, True, TC_SOLD, "press")]))

# speakeasy: GV led the $7.6M seed (closed May 2023) after a Quiet-led pre-seed; FPV led the $15M Series A (Nov 2024).
YF_SPEAKEASY = NEWS("speakeasy", "Closed $7.6 Million in Seed Funding Led by GV")
FIN_SPEAKEASY = NEWS("speakeasy", "API Platform Speakeasy Raises $15 Million")
L.append(cls("speakeasy", status="private", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=YF_SPEAKEASY, entry_date="2023-05",
             grad="graduated", grad_src="web_verified", grad_cite=FIN_SPEAKEASY, grad_conf="high",
             note="Speakeasy (speakeasyapi.dev), SDK and API tooling, San Francisco (release dateline). The company's "
                  "release (2023-06-29): a $7.6M seed led by GV, closed in May 2023, after a $3.3M pre-seed led by "
                  "Quiet Capital that names no GV, so the seed is the entry. Finovate (2024-11-06): a $15M Series A "
                  "led by FPV Ventures with GV and Quiet, a named later round, so graduated. Momentum slice checked "
                  "2026-09-28: no round at $1B or more found; still operating (adtmag headline 2026-09-18: Google and "
                  "Speakeasy open-source an SDK generator). Name collision: Headline's row named Speakeasy is the "
                  "Seattle internet provider Best Buy bought in 2007, a different company.",
             rounds=[rnd(None, "Pre-Seed", 3300000, "Quiet Capital", False, YF_SPEAKEASY, "company"),
                     rnd("2023-05", "Seed", 7600000, "GV", True, YF_SPEAKEASY, "company"),
                     rnd("2024-11-06", "Series A", 15000000, "FPV Ventures", True, FIN_SPEAKEASY, "press")]))

# speedybrand: GV and Y Combinator led a $2.5M round at a $15M post-money valuation (July 2023); round not named.
TC_SPEEDY = NEWS("speedybrand", "SpeedyBrand uses generative AI")
L.append(cls("speedybrand", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="AI & Applied AI", stage="undetermined", entry_date="2023-07",
             extra={"valuation_range_source": "web_verified", "valuation_citation": TC_SPEEDY,
                    "valuation_asof": "2023-07-07"},
             note="Generative-AI content marketing (blogs, social posts, ads) for small businesses, San Francisco (the "
                  "site's footer: 'Made with love in San Francisco'), a Y Combinator company. TechCrunch (2023-07-07): "
                  "$2.5M 'in a funding round led by GV and Y Combinator that values the company at $15 million "
                  "post-money'; neither TechCrunch nor the company's release names the round, so the stage is "
                  "undetermined. Momentum slice checked 2026-09-28: the $15M post-money mark and no later round "
                  "found, so below_1b; the site still operates.",
             rounds=[rnd("2023-07-07", None, 2500000, "GV, Y Combinator", True, TC_SPEEDY, "press")]))
SNYK_G = NEWS("snyk", "Snyk Closes $196.5 Million Series G")
L.append(cls("snyk", rng="1b_plus", usd=7400000000, val_src="web_verified", val_cite=SNYK_G, asof="2022-12-12",
             flags=["model_disputes_source", "stale"], extra=WV, **SNYK_BASE,
             note=SNYK_NOTE + " Mark: the company's release of 2022-12-12, '$196.5 Million Series G Funding at $7.4 "
                  "Billion Valuation', the last priced round, which replaces the recorded $8.5B of September 2021 "
                  "(aligned with the Accel and Coatue rows, which cite a vendor page for the same figure). Calcalist "
                  "reported secondary deals more than 50% below it (2023-07-10) and Business Insider an employee-stock "
                  "collapse (2026-08-28); neither is a priced event under $1B, so the band stays 1b_plus, stale. "
                  "Private as of July 2026 (Wikipedia).",
             rounds=[rnd("2018-03", "Series A", 7000000, None, False, GLOBES_SNYK, "press"),
                     rnd("2018-09-25", "Series B", 22000000, "Accel", True, GLOBES_SNYK, "press"),
                     rnd("2022-12-12", "Series G", 196500000, None, None, SNYK_G, "company")]))

# sprinter-health: GV was in the a16z-led $33M Series A (October 2021); the $4.6M seed was General Catalyst's.
HHCN_SPRINTER = NEWS("sprinter-health", "Sprinter Health Raises $33M")
L.append(cls("sprinter-health", status="private", rng="below_1b", country="US", city="Menlo Park",
             focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=HHCN_SPRINTER, entry_date="2021-10-13",
             note="In-home clinical visits (blood draws, vitals, testing). Home Health Care News (2021-10-13): a $33M "
                  "Series A led by Andreessen Horowitz with General Catalyst, Accel and Google Ventures, after a $4.6M "
                  "seed in March 2021 led by General Catalyst with angels, so the Series A is GV's entry (the firm's "
                  "listing starts in 2022). General Catalyst's own post describes doubling down in a $55M Series B "
                  "(2025). Private, "
                  "no round near $1B. City aligned with the a16z and General Catalyst rows (Menlo Park); Accel's row "
                  "has San Francisco.",
             rounds=[rnd("2021-03", "Seed", 4600000, "General Catalyst", False, HHCN_SPRINTER, "press"),
                     rnd("2021-10-13", "Series A", 33000000, "Andreessen Horowitz", True, HHCN_SPRINTER, "press"),
                     rnd("2025", "Series B", 55000000, None, None,
                         NEWS("sprinter-health", "Sprinter Health nabs $55M"), "press")]))

# spring: Google Ventures was in the Thrive-led $7.5M Series A of July 2014 (Fortune).
FORTUNE_SPRING = NEWS("spring", "David and Alan Tisch raise $7.5 million")
L.append(cls("spring", status="acquired", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FORTUNE_SPRING,
             entry_date="2014-07-09",
             note="Mobile shopping marketplace from Alan and David Tisch, New York (Wikipedia). Fortune (2014-07-09): "
                  "a $7.5M Series A led by Thrive Capital with Groupe Arnault, Box Group and Google Ventures; the "
                  "company launched under its new name with this round, so the Series A is GV's entry. GV joined the "
                  "$25M Series B led by Box Group in April 2015 (Wikipedia). ShopRunner bought Spring in 2018 (the "
                  "firm's exit line 'Acquired by ShopRunner, 2018'). Aligned with Thrive's row. Name collision: "
                  "General Catalyst's row named Spring is Spring Discovery (San Carlos), a different company.",
             rounds=[rnd("2014-07-09", "Series A", 7500000, "Thrive Capital", True, FORTUNE_SPRING, "press"),
                     rnd("2015-04", "Series B", 25000000, "Box Group", True, W("Spring (application)"), "press"),
                     rnd("2017-05", "Series C", 65000000, "Fidelity", None, W("Spring (application)"), "press")]))

# sqz-biotech: GV's earliest vehicle on the investor rights agreement is GV 2016, L.P.; 2016's only financing was the Series B.
STEMCELL_SQZ = NEWS("sqz-biotech", "STEMCELL Technologies to acquire all assets of SQZ")
L.append(cls("sqz-biotech", status="acquired", rng="below_1b", country="US", city="Watertown",
             focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2016",
             note="Cell-squeezing platform for cell therapies (MIT spinout), Watertown MA (EDGAR business address). "
                  "Entry: the 2019 investor rights agreement filed with the S-1 (exhibit 4.1) lists GV 2016, L.P., GV "
                  "2017, L.P. and GV 2019, L.P. and no earlier GV vehicle, and the S-1's notes date the company's "
                  "preferred rounds: Series Seed (March 2014, $1.0M), Series A (June and July 2015, $5.1M), Series B "
                  "(September and November 2016, $24.1M), Series C (2018), Series D (2019-2020). The firm listed "
                  "SQZ by January 2017, so its 2016 vehicle's entry was the Series B: Growth, the round inferred from "
                  "the filings rather than named with GV (medium). NYSE-listed from the 2020 IPO; after Roche "
                  "dropped its option the company cut staff and on 2023-12-21 agreed to sell substantially all "
                  "assets to STEMCELL Technologies for $11.8M (8-K), approved by stockholders on 2024-02-29 with a "
                  "plan of dissolution (STEMCELL's announcement, 2024-03-01, says it obtained the patents, equipment "
                  "and the MIT licence). The business continues under STEMCELL: acquired, with SQZ dissolved.",
             rounds=[rnd("2014-03", "Seed", 1000000, None, False, SQZ_S1, "filing"),
                     rnd("2015-06", "Series A", 5100000, None, False, SQZ_S1, "filing"),
                     rnd("2016-09", "Series B", 24100000, None, True, SQZ_S1, "filing"),
                     rnd("2018-05", "Series C", 71300000, None, None, SQZ_S1, "filing"),
                     rnd("2019-12", "Series D", 68300000, None, None, SQZ_S1, "filing"),
                     rnd("2023-12-21", "Asset sale", 11800000, "STEMCELL Technologies", None, SQZ_8K, "filing")]))

# snorkel-ai: GV's own post names its seed and Series A investments; the September 2026 round sets a $3.5B mark.
BN_SNORKEL = NEWS("snorkel-ai", "Snorkel AI triples valuation to $3.5 billion")
L.append(cls("snorkel-ai", status="private", rng="1b_plus", usd=3500000000, val_src="web_verified",
             val_cite=BN_SNORKEL, asof="2026-09-23", country="US", city="Redwood City", focus="AI & Applied AI",
             stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=POST("snorkel-machine-learning"),
             entry_date="2019-06", grad="graduated", grad_src="first_party", grad_conf="high",
             grad_cite=POST("snorkel-machine-learning"), extra=WV,
             note="Programmatic data labelling and AI data development, Redwood City (aligned with the Greylock and "
                  "Lightspeed rows). The firm's own post of 2020-07-14: Snorkel 'is emerging from stealth with $15 "
                  "million, including seed and Series A investments from GV along with Greylock and IQT'; its /ai "
                  "list dates GV's first investment 2019-06 (the seed; Greylock's row quotes its own post that it co-led "
                  "the initial seed with GV in spring 2019) and a re-investment 2019-10 (the Series A), so the entry "
                  "is the seed and the named "
                  "Series A graduates it. Mark: a $350M round at $3.5B (BetaNews headline 2026-09-23; Economic Times "
                  "2026-09-22), fresher than the $1.3B Series D of May 2025 that the Accel, Greylock and Lightspeed "
                  "rows carry (same band). Momentum slice: this round is the check.",
             rounds=[rnd("2019-06", "Seed", None, "Greylock, GV", True, POST("snorkel-machine-learning"), "firm"),
                     rnd("2019-10", "Series A", None, "Greylock", True, POST("snorkel-machine-learning"), "firm"),
                     rnd("2026-09-23", None, 350000000, None, None, BN_SNORKEL, "press")]))

# spotlight-therapeutics: shut down in February 2025 (Fierce Biotech, SFGATE headlines).
L.append(cls("spotlight-therapeutics", status="defunct", rng="below_1b", city="Hayward", focus="Healthcare & Bio",
             note="Targeted in vivo gene editing (TAGE platform), Hayward CA (the company's Form D addresses 2019 to "
                  "2022). Shut down in February 2025: Fierce Biotech (2025-02-19), 'It's curtain close for Spotlight: "
                  "Gene editing biotech shutters', and SFGATE (2025-02-20), 'Google-backed Bay Area biotech startup "
                  "shuts down'; no sale of the business was reported, so defunct. The firm's live list no longer "
                  "carries it (last archived 2025), as decisions D9 expects for shutdowns. The recorded Series A "
                  "(Form D band, GV's Blake Byers on the board from the first filing) stands."))

# security-scorecard: GV led the $20M Series B of June 2016, with Sequoia, Evolution and Boldstart as existing investors.
PRN_SSC = ("https://www.prnewswire.com/news-releases/securityscorecard-raises-20-million-series-b-round-led-by-gv-"
           "formerly-google-ventures-300289114.html")
REUTERS_SSC = NEWS("security-scorecard", "SecurityScorecard raises $180 million")
L.append(cls("security-scorecard", status="private", rng="below_1b", city="New York", focus="Security",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PRN_SSC,
             flags=["stale"],
             extra={"valuation_range_source": "web_verified", "valuation_citation": REUTERS_SSC,
                    "valuation_asof": "2021-03-18"},
             note="Security ratings, New York (release dateline; the Form D addresses). The company's release "
                  "(2016-06-23): a $20M Series B led by GV, with Sequoia, Evolution Equity and Boldstart as existing "
                  "investors and Two Sigma new, Karim Faris of GV joining the board; GV is not an existing investor, "
                  "so the Series B is its entry (its Form D, first sale 2016-04-26, already dates it). GV followed in "
                  "the $27.5M Series C led by Nokia Growth Partners (AlleyWatch, 2017-10-12). Band: the $180M round of "
                  "March 2021 was 'at nearly $1 billion valuation' (Reuters headline), the last priced event found, "
                  "so below_1b, stale. Aligned with Sequoia's row.",
             rounds=[rnd("2016-06-23", "Series B", 20000000, "GV", True, PRN_SSC, "company"),
                     rnd("2017-10-12", "Series C", 27500000, "Nokia Growth Partners", True,
                         NEWS("security-scorecard", "This NYC Startup Just Raised $27.5M"), "press"),
                     rnd("2021-03-18", None, 180000000, None, None, REUTERS_SSC, "press")]))

# spybiotech: the company's Series A release calls GV a founding investor; pre-A funding was about $6.5M (seed).
SPY_A = "https://spybiotech.com/spybiotech-raises-32-5m-in-series-a-funding-and-appoints-lutz-b-giebel-as-chairman/"
SPY_CONTACT = "https://www.spybiotech.com/contact-us"
L.append(cls("spybiotech", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=SPY_CONTACT, city="Oxford", focus="Healthcare & Bio",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=SPY_A, entry_date="2017",
             grad="graduated", grad_src="web_verified", grad_cite=SPY_A, grad_conf="high",
             note="Vaccine developer built on Oxford's SpyTag/SpyCatcher technology, Oxford (the company's contact "
                  "page: 7600 Quorum, Oxford Business Park, with a Cambridge MA office); GB confirmed. The company's "
                  "release (Oxford, 2021): a $32.5M Series A led by Braavos, in which 'founding investors' Oxford "
                  "Sciences Innovation and GV also participated, bringing total funding since the 2017 spin-out to "
                  "$39M. So GV entered before the Series A, in the roughly $6.5M of founding money, which is seed "
                  "stage whether it came in 2017 or as a later seed tranche (the firm's listing only shows it from "
                  "2019): Seed, the round inferred rather than named (medium). The named Series A graduates the row.",
             rounds=[rnd("2017", "Seed", None, "Oxford Sciences Innovation", True, SPY_A, "company"),
                     rnd("2021-02-10", "Series A", 32500000, "Braavos Investment Advisers", True, SPY_A,
                         "company")]))

# scope3 (renamed Apostra in September 2026): GV led the $20M Series B of October 2023, the first round naming GV.
BW_SCOPE3_B = NEWS("scope3", "Series B Funding Led by GV")
L.append(cls("scope3", status="private", rng="below_1b", country="US", city="New York", focus="Climate & Energy",
             stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=BW_SCOPE3_B,
             entry_date="2023-10-12",
             note="Emissions measurement for digital advertising, later agentic ad-buying software, New York (Brian "
                  "O'Kelley's company, launched January 2022). The company's release headline (2023-10-12): 'Scope3 "
                  "Raises $20M USD in Series B Funding Led by GV'; the firm's own post of 2024-10-10 says it 'first "
                  "invested' earlier and led the next round ($25M, Business Wire headline 2024-10-10), and no source "
                  "read names GV in the 2022 launch funding, so the Series B is taken as the entry (medium). Two "
                  "rounds of layoffs (Adweek, 2026-02-05) and a rename to Apostra on 2026-09-23 with about 40 staff "
                  "(PPC Land); still private, about $60M raised in total, nothing near $1B.",
             rounds=[rnd("2023-10-12", "Series B", 20000000, "GV", True, BW_SCOPE3_B, "company"),
                     rnd("2024-10-10", None, 25000000, "GV", True, NEWS("scope3", "Scope3 Raises $25M"),
                         "company")]))

# signos: GV co-led the $20M Series B of October 2023, but the firm listed Signos from May 2022; its first round is not named.
TC_SIGNOS = NEWS("signos", "Signos raises $20M to sprinkle")
L.append(cls("signos", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="Healthcare & Bio", stage="undetermined",
             note="Continuous glucose monitor plus AI app for weight management (FDA clearance 2025). TechCrunch "
                  "(2023-10-24): a $20M Series B led by Cheyenne Ventures and GV, with Dexcom Ventures and Samsung. "
                  "The firm's listing already carried Signos in May 2022, seventeen months before that round, so GV "
                  "held an earlier position whose round no source read names: undetermined. A further $20M came in "
                  "May 2026 (Business Wire headline, round unnamed). Private; nothing near $1B.",
             rounds=[rnd("2023-10-24", "Series B", 20000000, "Cheyenne Ventures, GV", True, TC_SIGNOS, "press"),
                     rnd("2026-05-27", None, 20000000, None, None,
                         NEWS("signos", "Signos, Inc., Maker of the First FDA-cleared CGM"), "company")]))

# smol: Google Ventures joined the Eight Roads-led $34M Series B of May 2021 as a new investor (UKTN).
UKTN_SMOL = NEWS("smol", "smol secures £24 million Series B")
L.append(cls("smol", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=UKTN_SMOL, city="London", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=UKTN_SMOL, entry_date="2021-05-10",
             note="Subscription eco laundry and cleaning products, London (EU-Startups headline 2020: 'London-based "
                  "smol'; UKTN: 'the UK's fastest-growing homecare brand'). UK Tech News (2021-05-10): a $34M "
                  "(GBP 24M) Series B led by Eight Roads Ventures 'with participation from Google Ventures, Latitude, "
                  "and existing investors Balderton Capital and Jam Jar', so GV came in new at the Series B; the "
                  "firm's listing starts in June 2021. Balderton led the 2020 Series A. Private and operating (The "
                  "Grocer, 2025-04-08: 'edges closer to profitability'); nothing near $1B. Aligned with Balderton's "
                  "row.",
             rounds=[rnd("2020-07-21", "Series A", None, "Balderton Capital", False,
                         NEWS("smol", "London-based smol raises"), "press"),
                     rnd("2021-05-10", "Series B", 34000000, "Eight Roads Ventures", True, UKTN_SMOL, "press")]))

# spruce-finance: restructured with an HPS Investment Partners investment in 2017; the firm's archived exit line says acquired by HPS.
SPW_SPRUCE = NEWS("spruce-finance", "Spruce Finance acquires two new residential solar portfolios")
L.append(cls("spruce-finance", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             note="Residential solar financing, formed in 2015 when Clean Power Finance merged with Kilowatt "
                  "Financial (Wikipedia); San Francisco on its Form D filings (201 Mission Street, 2013 and 2015). "
                  "Solar Power World (2020-11-17): Spruce 'pivoted from loan origination to asset ownership ... in "
                  "2017 after restructuring and receiving an investment from HPS Investment Partners'; the firm's "
                  "archived listing (2021-2022) reads 'Acquired by HPS Investment Partners, 2018', so a sale out of "
                  "the restructuring: acquired, with the business continuing as the solar-asset owner Spruce Power "
                  "(the live listing now links sprucepower.com). The live exit line 'Acquired by ShopRunner, 2018' "
                  "is a copy of Spring's and is wrong. The base row also carries Spruce Health's archive years, "
                  "partner (Blake Byers) and sector, which the rebuild splits off."))

# skycatch: Google Ventures is named in the 2014 $13.2M Series A (AgFunder's 2014 roundup); Caterpillar bought it in July 2026.
AGF_SKYCATCH = NEWS("skycatch", "2014 Roundup: Top Drone Deals")
L.append(cls("skycatch", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Industrial & Robotics", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=AGF_SKYCATCH, entry_date="2014",
             note="Drone and spatial-data platform for construction and mining, San Francisco (AgFunder). AgFunder's "
                  "2014 drone-deal roundup: Skycatch, founded 2013, '$13.2M, Series A', investors including Google "
                  "Ventures, ff Venture Capital, Ram Shriram and VegasTechFund, $19.7M raised to date; the firm's "
                  "listing starts in September 2014 and no earlier round names GV, so the Series A is taken as its "
                  "entry (medium). Caterpillar 'has acquired Skycatch, Inc.' (Irving, Texas, 2026-07-07; the "
                  "announcement skycatch.com now redirects to): acquired.",
             rounds=[rnd("2014", "Series A", 13200000, None, True, AGF_SKYCATCH, "press"),
                     rnd("2026-07-07", "Acquisition", None, "Caterpillar", None, RPM_SKYCATCH, "company")]))

# stackblitz: the /ai list dates GV's first investment 2020-06, before the Greylock-led seed announced in 2022; round not named.
FORBES_STACKBLITZ = NEWS("stackblitz", "StackBlitz | Company Overview & News")
L.append(cls("stackblitz", status="private", rng="below_1b", usd=700000000, val_src="web_verified",
             val_cite=FORBES_STACKBLITZ, asof="2025-01", country="US", city="San Francisco", focus="DevTools & APIs",
             stage="undetermined", entry_date="2020-06", extra=WV,
             note="Browser-based development environments (WebContainers) and the Bolt.new AI app builder, San "
                  "Francisco (Forbes). The firm's /ai list dates GV's first investment 2020-06 and a re-investment "
                  "2022-04; TechCrunch (2022-04-06) announced a $7.9M seed led by Greylock with GV participating, "
                  "which matches the 2022 re-investment, so GV's 2020 money went into an earlier round that no source "
                  "names: undetermined. Forbes: a Series B in January 2025 from Emergence Capital and GV took total "
                  "funding to $105M at a $700M valuation (Bloomberg reported the talks at $700M, 2025-01-21). "
                  "Momentum slice checked 2026-09-28: no priced round at $1B or more found, so below_1b. Aligned "
                  "with the Greylock and Insight rows.",
             rounds=[rnd("2020-06", None, None, None, True, jl.AI_LISTING, "firm"),
                     rnd("2022-04-06", "Seed", 7900000, "Greylock", True, TC_STACKBLITZ, "press"),
                     rnd("2025-01", "Series B", None, "Emergence Capital, GV", True, FORBES_STACKBLITZ, "press")]))

# stackone: the firm's post announces the Series A it led; the /ai list's first investment is the same month.
PULSE_STACKONE = NEWS("stackone", "StackOne: $20 Million Series A Raised")
L.append(cls("stackone", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=STACKONE_ABOUT, city="Newbury", city_src="web_verified", focus="DevTools & APIs",
             stage="Series A", stage_src="first_party", stage_conf="high",
             stage_cite=POST("stackone-the-next"), entry_date="2025-05-05",
             extra={"valuation_range_source": "web_verified", "valuation_citation": PULSE_STACKONE,
                    "valuation_asof": "2025-05-12"},
             note="Integration layer for SaaS and AI agents. StackOne Technologies Limited is incorporated in England "
                  "and Wales with its registered office in Newbury, Berkshire (the company's about page, which says "
                  "the team works across Europe and the US; EU-Startups calls it a British startup). The firm's own "
                  "post of 2025-05-05: 'we at GV are excited to announce that we are leading the Series A of "
                  "StackOne'; the /ai list gives the first investment as 2025-05, so the Series A is the entry. Pulse "
                  "2.0 (2025-05-12): $20M Series A led by GV with Workday Ventures, XTX, Episode 1 and Playfair, after "
                  "about $4M of seed money. Momentum slice checked 2026-09-28: no later round found, so below_1b.",
             rounds=[rnd("2023", "Seed", 3600000, None, False, STACKONE_ABOUT, "company"),
                     rnd("2025-05-05", "Series A", 20000000, "GV", True, POST("stackone-the-next"), "firm")]))

# sense (SenseHQ): the firm's /ai rounds start with a re-investment in 2017-03; the first round is not named.
L.append(cls("sense", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="SaaS", stage="undetermined", flags=["model_disputes_source"],
             note="Sense (sensehq.com), AI talent-engagement software for staffing firms, San Francisco (Sense Talent "
                  "Labs' 2021 Form D, 225 Bush Street, with GV's Tyson Clark as a director). Status: the pre-filled "
                  "'acquired' is disputed; it rode a weak CIK match (Accel's row says the same), the firm's live "
                  "listing carries no exit line, and the company kept shipping (Business Wire headline 2024-12-18, "
                  "voice AI release): private. Rounds: Accel's page gives Accel's Series A as 2017; a $16M Series C "
                  "led by Avataar (YourStory headline, 2021-06-17) and a $50M Series D led by SoftBank Vision Fund 2 "
                  "(Voicebot, 2021-12-06, about $90M raised in total). The firm's /ai list records only "
                  "re-investments (2017-03, 2018-10, 2020-10), so GV's first money came earlier, in a round no source "
                  "names: undetermined. The 2016-2019 archived 'Sense' entry linked sense.com (the Cambridge MA home "
                  "energy monitor), but sense.com's own investor list has no GV and only one 'Sense' is ever listed, "
                  "so that entry reads as this company mislinked, not a second holding.",
             rounds=[rnd("2017", "Series A", None, "Accel", None, ACCEL_SENSE, "firm"),
                     rnd("2021-06-17", "Series C", 16000000, "Avataar Ventures", True,
                         NEWS("sense", "Talent management startup Sense raises $16M Series C"), "press"),
                     rnd("2021-12-06", "Series D", 50000000, "SoftBank Vision Fund 2", None,
                         NEWS("sense", "Sense Raises $50M for AI-Powered Recruitment"), "press")]))

# scoutrfp: the firm listed Scout RFP by February 2016, before its July 2016 Series A; no source names GV's round.
PRN_SCOUT_C = NEWS("scoutrfp", "Scout RFP Raises $33M")
L.append(cls("scoutrfp", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="undetermined",
             note="Strategic sourcing and procurement software, San Francisco (the company's 2019 release). The firm's "
                  "listing carried ScoutRFP from February 2016, before the $9M Series A of July 2016 (FinSMEs "
                  "headline); the January 2019 $33M Series C release led by Scale names Menlo and NewView as previous "
                  "investors and no GV, and no source read names the round GV bought into: undetermined. Workday "
                  "bought Scout RFP for $540M in late 2019 (Pulse 2.0 headline; the firm's exit line 'Acquired by "
                  "Workday, 2019'). Aligned with Menlo's row. The 2015-2016 archived 'Scout' entry (scoutlauncher.com, "
                  "Rich Miner) is a different company.",
             rounds=[rnd("2016-07-27", "Series A", 9000000, None, None,
                         NEWS("scoutrfp", "Scout RFP Raises $9M"), "press"),
                     rnd("2019-01-15", "Series C", 33000000, "Scale Venture Partners", None, PRN_SCOUT_C, "company"),
                     rnd("2019-11", "Acquisition", 540000000, "Workday", None,
                         NEWS("scoutrfp", "Why Workday Is Buying"), "press")]))

# sonoma-biotherapeutics: the firm listed it from September 2021, after the $265M Series B; GV's round is not named.
L.append(cls("sonoma-biotherapeutics", status="private", rng="below_1b", country="US", city="Seattle",
             focus="Healthcare & Bio", stage="undetermined",
             note="Engineered regulatory T-cell therapies for autoimmune disease, with sites in South San Francisco "
                  "and Seattle (the company's contact page); its November 2025 release is datelined Seattle, as "
                  "8VC's row has it. The firm's listing starts in September 2021, just after the $265M round of "
                  "August 2021 (GeekWire headline), but no source read names GV in that round or an earlier one: "
                  "undetermined. Private and in the clinic (phase 1 data 2025, Cellares manufacturing deal 2026); "
                  "nothing near $1B.",
             rounds=[rnd("2021-08-04", "Series B", 265000000, None, None,
                         NEWS("sonoma-biotherapeutics", "Sonoma Biotherapeutics raises $265M"), "press")]))

# spinlaunch: the recorded Growth stage (Form D band) stands; status, city and band only.
L.append(cls("spinlaunch", status="private", rng="below_1b", city="Long Beach",
             note="Kinetic space-launch and satellite company, Long Beach CA (Wikipedia; the 2022 and later Form D "
                  "addresses). Private: it filed new equity Form Ds in November 2024 ($11.5M sold) and August 2025 "
                  "($15.0M sold), and the last named round was the $71M Series B of September 2022 with GV "
                  "participating (SpaceNews), about $150M raised in total; nothing near $1B. The recorded entry (the "
                  "$35M equity round of March 2018, GV's Shaun Maguire on the board) stands as Growth from the Form D "
                  "band; the 2018 round was announced as $40M from Airbus, Google and others without a series name, "
                  "and the 2022 round being the Series B suggests 2018 was the Series A, left for review.",
             rounds=[rnd("2018-03-28", None, 34749968, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1631845/000163184518000001/0001631845-18-000001-index.htm",
                         "filing"),
                     rnd("2022-09-21", "Series B", 71000000, "ATW Partners", True,
                         NEWS("spinlaunch", "SpinLaunch Closes $71M Series B Funding Round"), "press")]))

jl.write("j12", L)
