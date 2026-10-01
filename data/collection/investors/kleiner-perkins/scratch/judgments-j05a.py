"""PRO-99 Kleiner Perkins, judge j05, queue batch 9 (sportsline .. uipath): classification of listed members.
Superblocks and Truv wait on their momentum-slice news checks and are recorded in judgments-j05b.py."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, W, FTS

GL = "Graduation left for the graduation pass."


def PX(slug):
    """The firm's own post whose URL slug is exactly `slug` (POST() matches substrings)."""
    m = [p["url"] for p in jl._POSTS if p["slug"] == slug]
    assert len(m) == 1, (slug, m)
    return m[0]


# market caps read 2026-09-30 from stockanalysis.com (curl), printed by the tool
SA_SPOT = "https://stockanalysis.com/stocks/spot/market-cap/"
SA_UBER = "https://stockanalysis.com/stocks/uber/market-cap/"
SA_TRUE = "https://stockanalysis.com/quote/sto/TRUE.B/market-cap/"
# SportsLine's 1997 IPO registration (S-1/A, file 333-25259), read through secget.py
S1_SPLN = "https://www.sec.gov/Archives/edgar/data/945688/0000950170-97-001359.txt"
# pages read with WebFetch
SR_SPOTA = "https://www.siliconrepublic.com/start-ups/spotahome-series-b-funding-madrid-proptech"
TC_STORD = "https://techcrunch.com/2026/05/26/amazon-fulfillment-competitor-stord-raises-250m-at-3b-valuation/"
TP_B = "https://goteleport.com/blog/series-b/"
TP_C = "https://goteleport.com/blog/series-c/"
TULIP_PR = "https://www.tulip.com/press/tulip-retail-raises-40-million-led-by-kleiner-perkins/"
BS_TULIP = "https://brainstation.io/magazine/torontos-tulip-secures-40-million-to-bloom-retail-app"
# sibling books' recorded marks (rule 10), printed from siblings.json
STRIPE_MARK = "https://stripe.com/newsroom/news/stripe-2025-update"
TC_SYNTH = "https://techcrunch.com/2026/01/26/synthesia-hits-4b-valuation-lets-employees-cash-in/"
TC_TOSS = "https://techcrunch.com/2022/12/19/south-korean-financial-super-app-toss-closes-405m-series-g-as-valuation-rises-7/"
YH_TURO = "https://finance.yahoo.com/news/turo-becomes-techs-newest-unicorn-with-250m-iac-investment-194729985.html"
# SEC filings
S1_THEROX = FTS("TherOx", "S-1")
S1_TDOC = FTS("Teladoc", "S-1")
FD_TDOC_2011 = "https://www.sec.gov/Archives/edgar/data/1477449/000147744911000002/0001477449-11-000002-index.htm"
FD_TRADESY_2014 = "https://www.sec.gov/Archives/edgar/data/1608924/000160892414000002/0001608924-14-000002-index.htm"
FD_SYNACK_2014 = "https://www.sec.gov/Archives/edgar/data/1582684/000114036114017399/0001140361-14-017399-index.htm"
FD_TRANSPHORM_2010 = "https://www.sec.gov/Archives/edgar/data/1400017/000118143110024469/0001181431-10-024469-index.htm"
FD_TAS_2013 = "https://www.sec.gov/Archives/edgar/data/1491868/000149186813000003/0001491868-13-000003-index.htm"
FD_SUVOLTA_2009 = "https://www.sec.gov/Archives/edgar/data/1356683/000135668309000004/0001356683-09-000004-index.htm"
IRA_TWTR = FTS("TWITTER", "DRS")

VR = {"valuation_range_source": "web_verified"}

L = []

L.append(cls("sportsline", status="acquired", rng="below_1b", country="US", city="Fort Lauderdale",
             stage="Series A", stage_src="web_verified", stage_cite=S1_SPLN, stage_conf="high", entry_date="1995-05",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("1994-08", "Common stock and warrants (private investor)", 2000000, None, False, S1_SPLN, "filing"),
                     rnd("1995-05", "Series A", None, None, True, S1_SPLN, "filing"),
                     rnd("1996-03", "Series B", None, None, None, S1_SPLN, "filing")],
             note="Sports news site, Fort Lauderdale (SportsLine USA). The 1997 IPO registration says that in May 1995 "
                  "the company issued 3,000,000 shares of Series A Preferred to Kleiner Perkins Caufield & Byers VII, "
                  "KPCB Founders Fund and KPCB Information Sciences Zaibatsu Fund II, and Joe Lacob joined the board "
                  "that month; its only earlier financing was common stock sold to a private investor. Listed 1997 "
                  "(SPLN), bought by Viacom's CBS in 2004."))

L.append(cls("spotahome", status="private", rng="below_1b", country="ES", country_src="web_verified",
             country_cite=SR_SPOTA, city="Madrid", stage="Growth", stage_src="web_verified", stage_cite=SR_SPOTA,
             stage_conf="high", entry_date="2018-06-06", focus="Consumer & Marketplaces",
             rounds=[rnd("2018-06-06", "Series B", 40000000, "Kleiner Perkins", True, SR_SPOTA, "press")],
             note="Mid-term rental marketplace, Madrid (the Spain claim is confirmed). Kleiner Perkins led the $40M "
                  "Series B in June 2018, its first investment in a Spanish company (Silicon Republic); the firm's "
                  "listing reads Growth, 2018, Prior. Still operating and independent (a small 2025 strategic round "
                  "after reaching profitability); no priced round near $1B."))

L.append(cls("spotify", status="public", rng="100b_plus", usd=100200000000, val_src="web_verified", val_cite=SA_SPOT,
             asof="2026-09-30", country="SE", country_src="web_verified", country_cite=W("Spotify"), city="Stockholm",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2011",
             focus="Media, Gaming & Advertising", flags=["model_disputes_source"], extra=VR,
             rounds=[rnd("2012-11", "Goldman Sachs-led round at a $3B valuation", 100000000, "Goldman Sachs", None,
                         W("Spotify"), "press")],
             note="Music streaming, headquartered in Stockholm (incorporated in Luxembourg), listed on NYSE (SPOT) by "
                  "direct listing in 2018, so public, not acquired as prefilled. Market cap $100.2B on 2026-09-30 "
                  "(stockanalysis), within 5% of the $100B band edge; the other books read 100b_plus. The firm "
                  "entered in 2011 through its Digital Growth Fund (archived page), years after the 2008-2009 venture "
                  "rounds, so Growth; no source read names the 2011 round, hence model."))

L.append(cls("spruce-finance", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Climate & Energy",
             note="Residential solar financing and ownership, San Francisco (the 2015 Form D address). Status aligned "
                  "with the GV book, which reads acquired (rule 10); no fresher source was found here."))

L.append(cls("spruce-health", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Patient communication software for clinics, San Francisco (the 2015 Form D address). Still "
                  "operating; the firm lists it Prior. Aligned with the GV book (private, below $1B)."))

L.append(cls("square", city="Oakland", focus="Fintech & Payments",
             note="Square, now Block (NYSE: XYZ), with its principal office in Oakland; market cap $44.45B on "
                  "2026-09-30 (stockanalysis), still 10b_plus."))

L.append(cls("stackbit", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2019", focus="DevTools & APIs", rounds=[],
             note="Visual editing platform for headless websites; Netlify announced the acquisition on 2023-06-29 "
                  "(Wikipedia, Netlify), matching the firm's listing (Acquired, Netlify). The firm's listing gives "
                  "2019 and Early; no source read names the round, so the stage is undetermined."))

L.append(cls("stoke", status="acquired", rng="below_1b", city="Santa Clara", focus="Data Infrastructure",
             note="Mobile gateway and LTE security gateway maker, Santa Clara. Mavenir Systems acquired Stoke Inc. in "
                  "November 2014 for about $5.5M (Mavenir's 10-K for 2014), so acquired, not defunct as the Sequoia "
                  "book reads."))

L.append(cls("stord", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified", val_cite=TC_STORD,
             asof="2026-05-26", city="Atlanta", focus="SaaS", extra=VR,
             note="E-commerce fulfillment and supply chain software, Atlanta. Raised a $250M Series F at a $3B "
                  "valuation on 2026-05-26, led by Strike Capital with Kleiner Perkins participating (TechCrunch), "
                  "doubling the $1.5B of its May 2025 Series E. The Lux book's below_1b predates both rounds."))

L.append(cls("stripe", status="private", rng="100b_plus", usd=159000000000, val_src="web_verified",
             val_cite=STRIPE_MARK, asof="2026-02-24", city="South San Francisco", stage="Growth",
             stage_src="model", stage_conf="medium", stage_cite=SITE("stripe"), entry_date="2015",
             focus="Fintech & Payments", flags=["model_disputes_source"], extra=VR,
             note="Payments infrastructure, dual headquarters in South San Francisco and Dublin; private, not acquired "
                  "as prefilled. The February 2026 tender valued it at $159B, as the other books record. The firm's "
                  "page says it backed Stripe in 2015, a company that had already shown remarkable traction, after "
                  "its 2011-2014 seed, Series A, B and C, so Growth; no source read names the 2015 round."))

L.append(cls("sun-microsystems", city="Santa Clara", rng="below_1b", stage="undetermined", entry_date="1982-11",
             focus="Data Infrastructure",
             rounds=[rnd("1982-11", "first venture investment, series not named ($1.7M from Kleiner Perkins)", None,
                         None, True, PX("sun-microsystems"), "firm")],
             note="Workstations and servers, headquartered in Santa Clara at its height; Oracle completed the "
                  "acquisition in January 2010. The firm's own case study says it invested $1.7M in November 1982 "
                  "but names no series, so the stage is undetermined."))

L.append(cls("sybase", city="Dublin", rng="below_1b", stage="undetermined", entry_date="1985",
             focus="Data Infrastructure", rounds=[],
             note="Database software, Dublin, California; SAP completed the acquisition in July 2010 (Wikipedia). The "
                  "firm's listing gives 1985 and Early; no source read names the round."))

L.append(cls("symantec", country="US", city="Tempe", stage="undetermined", entry_date="1983", focus="Security",
             rounds=[],
             note="Security software; the company is now Gen Digital (Nasdaq: GEN), headquartered in Tempe, Arizona, "
                  "as the Sequoia book records; market cap $13.18B on 2026-09-30 (stockanalysis). The firm's listing "
                  "gives 1983 and Early, with John Doerr; no source read names the round."))

L.append(cls("synack", status="private", rng="below_1b", city="Redwood City", stage="Series A",
             stage_src="web_verified", stage_cite=W("Synack"), stage_conf="high", entry_date="2014-04",
             focus="Security", flags=["stage_disputes_band"],
             rounds=[rnd("2013", "Seed (Form D, 2013q3)", 1713427, None, None, None, "filing"),
                     rnd("2014-04", "Series A", 7499995, None, True, FD_SYNACK_2014, "filing"),
                     rnd("2015-02", "Series B", 25000000, None, None, W("Synack"), "press")],
             note="Crowdsourced security testing, Redwood City. The Seed band on the $7.5M April 2014 Form D is "
                  "disputed: Wikipedia records that April 2014 round as the Series A from Kleiner Perkins, Google "
                  "Ventures and Allegis Capital, after a $1.7M 2013 seed; the GV book also reads Series A. Still "
                  "private; the last priced round (2020) was far below $1B."))

L.append(cls("synthesia", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified",
             val_cite=TC_SYNTH, asof="2026-01-26", country="GB", country_src="web_verified",
             country_cite=W("Synthesia (company)"), city="London", stage="Growth", stage_src="web_verified",
             stage_cite=W("Synthesia (company)"), stage_conf="high", entry_date="2021-12",
             focus="AI & Applied AI", flags=["model_disputes_source"], extra=VR,
             rounds=[rnd("2021-04", "Series A", 12500000, None, None, W("Synthesia (company)"), "press"),
                     rnd("2021-12", "Series B", 50000000, "Kleiner Perkins and GV", True, W("Synthesia (company)"), "press"),
                     rnd("2023-06", "Series C", 90000000, "Accel", None, W("Synthesia (company)"), "press"),
                     rnd("2025-01", "Series D", 180000000, "NEA", None, W("Synthesia (company)"), "press"),
                     rnd("2026-01", "Series E", 200000000, "GV", None, TC_SYNTH, "press")],
             note="AI video generation, headquartered in London, so GB, not the prefilled CZ, and private, not "
                  "acquired (it turned down Adobe). Kleiner Perkins co-led the December 2021 Series B with GV (its "
                  "entry; the firm's post is synthesia-series-b); the $4B January 2026 round is the momentum-slice "
                  "check (done 2026-09-30) and matches the Accel, GV and NEA books."))

L.append(cls("tecton", country="US", city="San Francisco", rng="below_1b", stage="Growth",
             stage_src="first_party", stage_cite=PX("tecton-series-c"), stage_conf="high", entry_date="2022-07-12",
             focus="Data Infrastructure",
             rounds=[rnd("2022-07-12", "Series C", 100000000, "Kleiner Perkins", True, PX("tecton-series-c"), "firm")],
             note="Machine learning feature platform, San Francisco; acquired by Databricks. The firm's post "
                  "announces the $100M Series C it led and says it had followed the company for years before, so "
                  "the Series C is the entry."))

L.append(cls("teladoc", city="New York", stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=S1_TDOC, focus="Healthcare & Bio",
             rounds=[rnd("2011-08", "late preferred round (Form D, $18.6M)", 18600003, None, True, FD_TDOC_2011, "filing"),
                     rnd("2013-08-28", "Series E", 15000000, None, None, S1_TDOC, "filing")],
             note="Telehealth, headquartered in New York since 2023. Kleiner Perkins entered at the $18.6M round of "
                  "August 2011 (Dana Mead joined the board that month; Digital Growth Fund on the archived page), "
                  "after earlier preferred rounds from HLM Venture Partners and Cardinal; the S-1 dates the Series E "
                  "to August 2013, so the 2011 round was a Series C or D: Growth."))

L.append(cls("teleport", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified", val_cite=TP_C,
             asof="2022-05-03", country="US", country_src="web_verified", country_cite=TP_C, city="Oakland",
             stage="Series A", stage_src="web_verified", stage_cite=TP_B, stage_conf="high", entry_date="2019",
             focus="Security", flags=["stale", "model_disputes_source"], extra=VR,
             rounds=[rnd("2019", "Series A", None, None, True, TP_B, "company"),
                     rnd("2021-08-18", "Series B", 30000000, "S28 Capital and Kleiner Perkins", True, TP_B, "company"),
                     rnd("2022-05-03", "Series C", 110000000, "Bessemer Venture Partners", None, TP_C, "company")],
             note="Infrastructure access software (Gravitational Inc.), Oakland, so US, not the prefilled AT. The "
                  "company's Series B post quotes Kleiner Perkins' Bucky Moore: since partnering with Teleport at "
                  "Series A (the firm's 2019), and the firm co-led the 2021 Series B. The last priced mark is the "
                  "$1.1B Series C of May 2022, stale."))

L.append(cls("tellme-networks", city="Mountain View", rng="below_1b", stage="undetermined", entry_date="1999",
             focus="Data Infrastructure", rounds=[],
             note="Voice application network, Mountain View; Microsoft bought it in 2007 for about $800M (Wikipedia). "
                  "The firm's listing gives 1999 and Early; no source read names the round."))

L.append(cls("telogis", status="acquired", rng="below_1b", city="Aliso Viejo", stage="Growth",
             stage_src="web_verified", stage_cite=W("Telogis"), stage_conf="high", entry_date="2013-10",
             focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2013-10", "first outside venture capital", 93000000, "Kleiner Perkins", True, W("Telogis"), "press"),
                     rnd("2015-04", "Form D offering", 39999999, None, None, None, "filing")],
             note="Fleet telematics software, Aliso Viejo; Verizon acquired it in 2016. Wikipedia records the "
                  "company's first outside venture capital as $93M from Kleiner Perkins' Green Growth Fund in "
                  "October 2013, a growth-equity round, so the entry date is 2013-10, not the 2015 Form D."))

L.append(cls("tesaro", city="Waltham", rng="below_1b", focus="Healthcare & Bio",
             note="Oncology drug developer, Waltham; GSK completed the acquisition in 2019."))

L.append(cls("therox", status="acquired", rng="below_1b", city="Irvine", stage="undetermined",
             focus="Healthcare & Bio",
             rounds=[rnd("2005-07", "Series I", None, None, True, S1_THEROX, "filing"),
                     rnd("2008-01", "Series J", 29989409, None, True, S1_THEROX, "filing")],
             note="SuperSaturated Oxygen therapy for heart attack patients, Irvine; ZOLL Medical (Asahi Kasei) bought "
                  "it in 2019 (model knowledge). Incorporated in 1994; the 2008 S-1 shows Kleiner Perkins Caufield & "
                  "Byers VII (a 1994 fund) holding shares and designating a director, so the entry was in the 1990s "
                  "and the 2013 Form D date on file is a follow-on; no source read names the first round."))

L.append(cls("thrive", status="private", rng="below_1b", country="US", city="New York", stage="Growth",
             stage_src="first_party", stage_cite=PX("thrive-global"), stage_conf="high", entry_date="2021-07",
             focus="Healthcare & Bio",
             rounds=[rnd("2016", "Series A", 7000000, None, False, W("Thrive Global"), "press"),
                     rnd("2021-07", "Series C", 80000000, "Kleiner Perkins and Owl Ventures", True, W("Thrive Global"), "press")],
             note="Thrive Global, workplace well-being software, New York. The firm's post says it led the Series C "
                  "(July 2021, $80M), matching its listing year 2021; no earlier Kleiner Perkins round is recorded. "
                  "The Thrivent N-PX hit on the row is a homonym."))

L.append(cls("tmunity", status="acquired", rng="below_1b", city="Philadelphia", focus="Healthcare & Bio",
             note="Engineered T-cell therapy, Philadelphia; Kite (Gilead) completed the acquisition in February 2023 "
                  "(Wikipedia, Kite Pharma)."))

L.append(cls("together-ai", city="San Francisco", stage="Series A", stage_src="first_party",
             stage_cite=PX("together-ai"), stage_conf="high", entry_date="2023-11-29", focus="AI & Applied AI",
             rounds=[rnd("2023-11-29", "Series A", None, "Kleiner Perkins", True, PX("together-ai"), "firm")],
             note="AI cloud, San Francisco. The firm's post announces 'our Series A investment and partnership' and "
                  "that it led the Series A; the seed earlier in 2023 was led by Lux Capital, not Kleiner Perkins."))

L.append(cls("toss", status="private", rng="1b_plus", usd=7002897246, val_src="web_verified", val_cite=TC_TOSS,
             asof="2022-12-19", country="KR", country_src="web_verified", country_cite=W("Viva Republica"),
             city="Seoul", stage="Growth", stage_src="web_verified", stage_cite=W("Viva Republica"),
             stage_conf="high", entry_date="2018", focus="Fintech & Payments", flags=["stale"], extra=VR,
             rounds=[rnd("2018", "$80M round that made it a unicorn", 80000000, "Kleiner Perkins and Ribbit Capital",
                         True, W("Viva Republica"), "press"),
                     rnd("2022-12-19", "Series G", 405000000, None, None, TC_TOSS, "press")],
             note="Toss, the finance super-app of Viva Republica, Seoul. Kleiner Perkins co-led the 2018 $80M round "
                  "that made it a unicorn (Wikipedia), matching the firm's 2018 Growth listing. Last priced mark the "
                  "December 2022 Series G, about $7.0B, as the Ribbit book records; stale."))

L.append(cls("trace-data", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2019", focus="Security", rounds=[],
             note="Data observability and security, San Francisco; Netskope acquired it in April 2021 and the founder "
                  "James Donelan joined Netskope, matching the firm's listing (Acquired, Netskope); the Accel book's "
                  "private is stale. The firm's listing gives 2019 and Early; no source read names its round."))

L.append(cls("tradesy", status="acquired", rng="below_1b", city="Santa Monica", stage="Series A",
             stage_src="model", stage_conf="medium", stage_cite=FD_TRADESY_2014, focus="Consumer & Marketplaces",
             rounds=[rnd("2014-05", "priced round (Form D, $15.0M; John Doerr joined the board)", 15028830, None, True,
                         FD_TRADESY_2014, "filing"),
                     rnd("2015-01", "Series B", 30000000, None, True, W("Tradesy"), "press"),
                     rnd("2016-05", "Series C", 30000000, "Wildcat Capital Management", None, W("Tradesy"), "press")],
             note="Resale fashion marketplace, Santa Monica; Vestiaire Collective bought it in 2022. Kleiner Perkins "
                  "entered at the May 2014 round (Form D with John Doerr as director; archived page from 2014); "
                  "Wikipedia names the January 2015 round the Series B, so the 2014 round was the Series A."))

L.append(cls("transmedics", city="Andover", focus="Healthcare & Bio",
             note="Organ care system, Andover, Massachusetts; market cap $2.89B on 2026-09-30 (stockanalysis)."))

L.append(cls("transphorm-inc", status="acquired", rng="below_1b", city="Goleta", stage="undetermined",
             focus="Industrial & Robotics",
             rounds=[rnd("2010-04", "Form D offering", 20200000, None, True, FD_TRANSPHORM_2010, "filing")],
             note="Gallium nitride power semiconductors, Goleta; Renesas acquired it in 2024 (Wikipedia). Kleiner "
                  "Perkins backed it from its early years (Randy Komisar on the board); the 2010 Form D is the first "
                  "filing on record and no source read names the round the firm entered."))

L.append(cls("trius-therapeutics", city="San Diego", rng="below_1b", focus="Healthcare & Bio",
             note="Antibiotics developer, San Diego; Cubist bought it in 2013."))

L.append(cls("true-north-therapeutics", status="acquired", rng="below_1b", country="US",
             city="South San Francisco", stage="undetermined", entry_date="2013", focus="Healthcare & Bio",
             rounds=[],
             note="Complement inhibitor antibodies, South San Francisco; Bioverativ agreed in May 2017 to buy it for "
                  "$825M (Wikipedia, Bioverativ). The firm's listing gives 2013 and Early; no source read names the "
                  "round."))

L.append(cls("truecaller", status="public", rng="below_1b", usd=704489012, val_src="web_verified",
             val_cite=SA_TRUE, asof="2026-09-30", country="SE", country_src="web_verified",
             country_cite=W("Truecaller"), city="Stockholm", stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=W("Truecaller"), entry_date="2014-10", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-02", "venture round", 18800000, "Sequoia Capital", False, W("Truecaller"), "press"),
                     rnd("2014-10", "venture round", 60000000, "Atomico and Kleiner Perkins", True, W("Truecaller"), "press")],
             note="Caller ID app, head office Stockholm, listed on Nasdaq Stockholm (TRUE B). Kleiner Perkins entered "
                  "with Atomico in the $60M round of October 2014, after Sequoia's $18.8M round earlier that year, a "
                  "later-stage round: Growth. Market cap SEK 7.03B on 2026-09-30 (stockanalysis) @ ECB 2026-09-30 "
                  "(SEK/EUR 11.331, EUR/USD 1.1355) = $704.5M, in line with the Atomico and Balderton books."))

L.append(cls("trusona", status="private", rng="below_1b", country="US", city="Scottsdale", stage="Series A",
             stage_src="web_verified", stage_cite=W("Trusona"), stage_conf="high", entry_date="2016-02",
             focus="Security",
             rounds=[rnd("2016-02", "Series A", 8000000, "Kleiner Perkins", True, W("Trusona"), "press"),
                     rnd("2017-06", "venture round", 10000000, "Microsoft Ventures", True, W("Trusona"), "press"),
                     rnd("2020-01", "Series C", 20000000, "Georgian Partners", True, W("Trusona"), "press")],
             note="Passwordless authentication, Scottsdale. Kleiner Perkins led the $8M Series A (February 2016; the "
                  "firm's listing says 2015, the close year) and followed on in 2017 and 2020."))

L.append(cls("tulip", status="private", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=BS_TULIP, city="Toronto", stage="Growth", stage_src="web_verified", stage_cite=TULIP_PR,
             stage_conf="high", entry_date="2017-08-22", focus="SaaS", flags=["model_disputes_source"],
             rounds=[rnd("2017-08-22", "Series B", 40000000, "Kleiner Perkins", True, TULIP_PR, "company")],
             note="Tulip Retail (tulip.com), mobile software for store associates, headquartered in Toronto, so CA, "
                  "not the prefilled JP. Kleiner Perkins led the $40M Series B in August 2017, joining existing "
                  "investors such as Jump Capital; Mood Rowghani joined the board. Not the NEA book's Tulip (Tulip "
                  "Interfaces, Somerville): a different company with the same name."))

L.append(cls("turo", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=YH_TURO,
             asof="2019-07", city="San Francisco", focus="Consumer & Marketplaces",
             flags=["stale", "model_disputes_source"], extra=VR,
             note="Peer-to-peer car sharing, San Francisco (Wikipedia); still operating after it withdrew its IPO "
                  "filing, so private, not defunct as prefilled. The last priced mark is the 2019 IAC-led $250M round "
                  "at over $1B, as the GV book records; stale."))

L.append(cls("twitter", city="San Francisco", rng="below_1b", stage="Growth", stage_src="model",
             stage_conf="medium", stage_cite=IRA_TWTR, entry_date="2010-12", focus="Media, Gaming & Advertising",
             note="Twitter, San Francisco; taken private by Elon Musk in 2022 and folded into xAI (Wikipedia). "
                  "Kleiner Perkins' Digital Growth Fund entered at the roughly $200M round of December 2010 at a "
                  "$3.7B valuation (the firm's year 2010, Growth); KPCB Holdings signs the investors' rights "
                  "agreement in the IPO filing."))

L.append(cls("uber", status="public", rng="100b_plus", usd=139940000000, val_src="web_verified", val_cite=SA_UBER,
             asof="2026-09-30", country="US", city="San Francisco", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2014-06", focus="Consumer & Marketplaces",
             flags=["model_disputes_source"], extra=VR,
             note="Ride hailing and delivery, headquartered in San Francisco (Wikipedia), so US, not the prefilled NL "
                  "(its international holding entity). Kleiner Perkins' Digital Growth Fund joined the June 2014 "
                  "Series D ($1.2B at a $17B valuation), matching the firm's 2014 Growth listing. Market cap $139.94B "
                  "on 2026-09-30 (stockanalysis)."))

L.append(cls("uipath", city="New York", stage="Growth", stage_src="web_verified", stage_cite=W("UiPath"),
             stage_conf="high", entry_date="2018-03-06", focus="SaaS",
             rounds=[rnd("2018-03-06", "venture round ($153M at a $1.1B valuation)", 153000000, None, True,
                         W("UiPath"), "press")],
             note="Robotic process automation, headquartered in New York. Kleiner Perkins entered at the $153M "
                  "March 2018 round (with Accel and CapitalG, at $1.1B; Wikipedia), the day its post 'This is why we "
                  "invested in UiPath' went up."))

jl.write("j05a", L)
