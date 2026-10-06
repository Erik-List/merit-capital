"""PRO-80 Bessemer Venture Partners, judge j03, queue batch 6 part 1 (health-essentials .. instructure):
classification of listed members, and one sale-consideration row excluded (insmed, for Transave)."""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, SITE, ARCH, POST, W, NEWS, FORMD_CITE

GL = "Graduation left for the graduation pass."
# URLs printed by tools run in this session (stockanalysis curl, secget and the EDGAR full-text listing, NEWS
# decode, WebSearch and WebFetch reads)
SA_HOMEFIRST = "https://stockanalysis.com/quote/nse/HOMEFIRST/market-cap/"
SA_IEX = "https://stockanalysis.com/quote/nse/IEX/market-cap/"
S1_INSTRUCTURE = "https://www.sec.gov/Archives/edgar/data/1355754/000119312515341090/d932934ds1.htm"
K8_INSMED = "https://www.sec.gov/Archives/edgar/data/1104506/000110450610000018/iex99-1.htm"
GN_ILLOCA = NEWS("illoca", "Raises $13 Million Seed Led")
BB_HIBOB = NEWS("hibob", "Salesforce Backs HR Software Firm")
PR_HOUSERX = NEWS("house-rx", "Secures $30 Million")
CT_HUNTERS = NEWS("hunters", "taking funding to nearly")
TC_HUNTERS = NEWS("hunters", "Hunters raises $68M Series C")
TB_IMPLY = NEWS("imply", "Imply Announces $100M")
LM_INNOVITI = NEWS("innoviti", "raises Rs120 crore")
ISN_INRISK = NEWS("inrisk", "Ahmedabad-based")
EN_INRISK = NEWS("inrisk", "Series A round led by Bessemer")
ET_HOMEFIRST = NEWS("homefirst", "exits Home First")

L = []

# ---- Health Essentials
L.append(cls("health-essentials", status="unknown", rng="below_1b", city="Irvine", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Post-acute and hospice care for the frail elderly in California, Nevada and Arizona; Santa Ana in "
                  "2012, Irvine on its Form D of March 2019. SV Life Sciences and Bessemer provided growth funding in "
                  "October 2012 (Venture Capital Journal, 2012-10-24), so the Growth entry stands. The firm's "
                  "list dropped the company after 2019 and no later filing or report was found (Google News, "
                  "2026-10-01), so its present state is not established."))

# ---- Hibob
L.append(cls("hibob", status="private", rng="1b_plus", usd=3200000000, val_src="web_verified", val_cite=BB_HIBOB,
             asof="2026-09", country="GB", country_src="web_verified", country_cite=W("HiBob"), city="London",
             stage="Seed", stage_src="first_party", stage_cite=POST("the-rise-of-hibob"), stage_conf="high",
             entry_date="2015-11-16", grad="graduated", grad_src="web_verified", grad_cite=W("HiBob"),
             grad_conf="high", focus="SaaS", flags=["model_disputes_source"],
             rounds=[rnd("2015-11", "Seed", 7000000, "Bessemer Venture Partners", True, POST("the-rise-of-hibob"),
                         "firm"),
                     rnd("2017", "Series A", 17500000, None, True, W("HiBob"), "press"),
                     rnd("2020", "Series B", 70000000, "Seek and Israel Growth Partners", None, W("HiBob"), "press"),
                     rnd("2021-10", "Series C", 150000000, "General Atlantic", True, POST("the-rise-of-hibob"),
                         "firm"),
                     rnd("2026-09", "growth round", 166000000, "Salesforce", None, BB_HIBOB, "press")],
             extra={"valuation_range_source": "web_verified"},
             note="HR platform, founded in Tel Aviv and headquartered in London (Wikipedia; as in the Battery and "
                  "General Catalyst books), replacing the Wikidata string. The firm's own post: Bessemer signed a "
                  "term sheet to lead a $7 million seed round in September 2015 (the listing dates it 2015-11-16). "
                  "Graduated: the $17.5M Series A of 2017 (Wikipedia). Mark: the $166M round of September 2026 led "
                  "by Salesforce at $3.2B (Bloomberg headline, 2026-09-01), fresher than the sibling books' 2021 "
                  "and 2022 marks."))

# ---- Hightower
L.append(cls("hightower", status="acquired", rng="below_1b", city="New York", grad="graduated", grad_src="formd",
             grad_cite=FORMD_CITE("hightower", 1), grad_conf="high", focus="SaaS",
             note="Leasing software for commercial real estate, New York (GeekWire, 2013-12-20: lands $2.12M, moves "
                  "to NYC); merged into VTS in 2016, so acquired, as in the Thrive book. Graduated on the Form D "
                  "layer: the $2.12M seed of 2013-12-04 was followed by a $6.54M round sold 2014-08-20 (the Series "
                  "A), above twice the entry and $5M."))

# ---- Hinge Health
L.append(cls("hinge-health", city="San Francisco", focus="Healthcare & Bio",
             note="Digital musculoskeletal care, San Francisco (as in five sibling books); NYSE: HNGE since May 2025. "
                  "The pre-filled $1.5B figure is older than the listing's current value: the market cap was $7.93B "
                  "on 2026-10-01 (StockAnalysis), the same band."))

# ---- HockeyStack
L.append(cls("hockeystack", status="private", rng="below_1b", country="US", city="San Francisco", stage="Series A",
             stage_src="first_party", stage_cite=POST("hockeystack-raises"), stage_conf="high",
             entry_date="2025-01", focus="SaaS",
             rounds=[rnd("2025-01", "Series A", 20000000, "Bessemer Venture Partners", True,
                         POST("hockeystack-raises"), "firm")],
             note="Revenue attribution and analytics for B2B go-to-market teams, San Francisco (as in the General "
                  "Catalyst and YC books). The firm's own post of 2025-01-28 announces its backing in the $20M Series "
                  "A (partnered year 2024). Momentum check 2026-10-01: no later round or valuation found (Google "
                  "News)."))

# ---- HomeFirst
L.append(cls("homefirst", status="public", rng="1b_plus", usd=1221859931, val_src="web_verified",
             val_cite=SA_HOMEFIRST, asof="2026-10-01", country="IN", country_src="web_verified",
             country_cite=W("Home First Finance"), city="Mumbai", stage="undetermined", entry_date="2010-12-24",
             rounds=[rnd("2011", "minority stake", None, "Bessemer Venture Partners", True, W("Home First Finance"),
                         "press"),
                     rnd("2017-02", "majority stake", None, "True North", False, W("Home First Finance"), "press"),
                     rnd("2020-10", "25% stake", None, "Warburg Pincus", False, W("Home First Finance"), "press")],
             extra={"focus": None, "valuation_range_source": "web_verified"},
             note="Home First Finance Company India, affordable housing lender, Mumbai; a mortgage lender, outside the "
                  "focus taxonomy. Listed on the NSE since February 2021: INR 117.70B @ ECB 2026-10-01 (INR/EUR "
                  "108.832, EUR/USD 1.1298) = $1.22B (StockAnalysis). Wikipedia: Bessemer bought a minority stake in "
                  "2011 for an undisclosed sum, with no round named, so the stage is undetermined and the date is "
                  "the firm's own; Bessemer sold its last 7.75% in March 2023 (ET Realty headline)."))

# ---- House Rx
L.append(cls("house-rx", status="private", rng="below_1b", country="US", city="San Francisco", stage="Series A",
             stage_src="web_verified", stage_cite=PR_HOUSERX, stage_conf="high", entry_date="2022-03",
             focus="Healthcare & Bio",
             rounds=[rnd("2021", "Seed", 5000000, "First Round Capital", False, PR_HOUSERX, "company"),
                     rnd("2022-03", "Series A", 25000000, "Bessemer Venture Partners", True, PR_HOUSERX, "company"),
                     rnd("2025-11", "Series B", 55000000, None, None, None, "press")],
             note="Specialty pharmacy platform for clinics, San Francisco (as in the First Round and NEA books). The "
                  "company's release of 2022-03-14: $25 million in Series A financing led by Bessemer Venture "
                  "Partners after a First Round-led seed; the firm's own year reads 2021."))

# ---- Hunch
L.append(cls("hunch", status="acquired", rng="below_1b", country="US", city="New York", stage="undetermined",
             entry_date="2007-09-13", focus="Consumer & Marketplaces",
             rounds=[rnd("2010-03", "unnamed (Form D)", 12000000, None, True, FORMD_CITE("hunch", 0), "filing")],
             note="Recommendation engine, New York; acq. by eBay, 2011. The firm's own listing dates its investment "
                  "2007-09-13, the founding year, so the 2010 Form D on which Rob Stavis is a director is a later "
                  "round and the pre-filled 2010 date is replaced; no source read names the 2007 round (Google News, "
                  "2026-10-01, returned no funding report)."))

# ---- Hungama
L.append(cls("hungama", status="private", rng="below_1b", country="IN", country_src="web_verified",
             country_cite=W("Hungama Digital Media Entertainment"), city="Mumbai", stage="undetermined",
             entry_date="2014", focus="Media, Gaming & Advertising",
             rounds=[rnd("2016-04", "$25M round", 25000000, "Xiaomi", None, None, "press")],
             note="Hungama Digital Media, music and video streaming, Mumbai (Wikipedia). The firm's own year is 2014; "
                  "no source read names the round Bessemer entered (Google News, 2026-10-01, shows the Xiaomi-led "
                  "$25M round of April 2016 and nothing naming Bessemer's)."))

# ---- Hunters
L.append(cls("hunters", status="private", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=CT_HUNTERS, city="Tel Aviv", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2021-08", focus="Security", flags=["model_disputes_source"],
             rounds=[rnd("2020-06", "Series A", 15000000, None, False, None, "press"),
                     rnd("2021-08", "Series B", 30000000, "Bessemer Venture Partners", True, TC_HUNTERS, "press"),
                     rnd("2022-01", "Series C", 68000000, "Stripes", True, TC_HUNTERS, "press")],
             note="Security operations platform (hunters.ai), Tel Aviv with a US office; CTech describes its R&D "
                  "center in Israel. The pre-filled acquired status and GB country are a name collision with "
                  "another Hunters; no report of a sale was found (Google News, 2026-10-01), so the row reads "
                  "private. TechCrunch (2022-01-25) dates the $30M Series B to August 2021 and names Bessemer an "
                  "existing investor in the Series C; model: Bessemer led that Series B, the firm's partnered year."))

# ---- Hyperscience
L.append(cls("hyperscience", status="private", rng="below_1b", country="US", city="New York", stage="Growth",
             stage_src="first_party", stage_cite=POST("hyperscience-series-c"), stage_conf="high",
             entry_date="2020-06", focus="AI & Applied AI",
             rounds=[rnd("2020-06", "Series C", 60000000, "Bessemer Venture Partners", True,
                         POST("hyperscience-series-c"), "firm")],
             note="Document automation software, New York (as in the Battery, Felicis and Tiger Global books). The "
                  "firm's own post of 2020-06-01: Bessemer leads the $60M Series C, its partnered year. No priced "
                  "mark of $1B or more was found (Google News, 2026-10-01)."))

# ---- IAG Research
L.append(cls("iag-research-inc", status="acquired", rng="below_1b", country="US", city="New York",
             stage="undetermined", entry_date="2006-04-26", focus="Media, Gaming & Advertising", rounds=[],
             note="Television advertising effectiveness research, New York (as in the Insight book); acq. by The "
                  "Nielsen Co., 2008. The firm's own listing dates its investment 2006-04-26 and names no round; a "
                  "Google News query on 2026-10-01 returned no funding report."))

# ---- illoca
L.append(cls("illoca", status="private", rng="below_1b", country="US", city="San Ramon", city_src="web_verified",
             stage="Seed", stage_src="first_party", stage_cite=POST("news/illoca"), stage_conf="high",
             entry_date="2026-05", grad="censored", focus="AI & Applied AI",
             rounds=[rnd("2026-05", "Seed", 13000000, "Bessemer Venture Partners", True, POST("news/illoca"),
                         "firm")],
             note="Generative design tool for architects and engineers, San Ramon, California (the company's release "
                  "of 2026-05-06 on GlobeNewswire). The firm's own post: Bessemer leads Illoca's $13M Seed "
                  "(partnered year 2025), inside the 24-month window. Momentum check 2026-10-01: no later round "
                  "(Google News)."))

# ---- Illusive Networks
L.append(cls("illusive-networks", status="acquired", rng="below_1b", city="Tel Aviv", stage="undetermined",
             entry_date="2015-09-03", focus="Security",
             rounds=[rnd("2015-06", "Series A", 5000000, "Team8", False, W("Illusive Networks"), "press"),
                     rnd("2015-10", "Series B", 22000000, "New Enterprise Associates", None, W("Illusive Networks"),
                         "press"),
                     rnd("2020", "later round", None, None, True, W("Illusive Networks"), "press")],
             note="Deception-based security, Tel Aviv (as in the NEA book); acq. by Proofpoint, 2022. The firm's own "
                  "date, 2015-09-03, falls between the Team8 Series A of June 2015 and the NEA-led Series B announced "
                  "in October 2015; Wikipedia names Bessemer as a backer of Team8 and as an existing investor by "
                  "2020, but no source read names Bessemer in either 2015 round, so the stage is undetermined (the "
                  "Series B is the likely entry)."))

# ---- Imply
L.append(cls("imply", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified", val_cite=TB_IMPLY,
             asof="2022-05", country="US", city="Burlingame", stage="Growth", stage_src="first_party",
             stage_cite=POST("imply-raises"), stage_conf="high", entry_date="2021-06", focus="Data Infrastructure",
             flags=["stale"],
             rounds=[rnd("2021-06", "Series C", 70000000, "Bessemer Venture Partners", True, POST("imply-raises"),
                         "firm"),
                     rnd("2022-05", "Series D", 100000000, "Thoma Bravo", True, TB_IMPLY, "company")],
             extra={"valuation_range_source": "web_verified"},
             note="Real-time analytics database built on Apache Druid, Burlingame. The firm's own post of 2021-06-15: "
                  "Bessemer led the $70M Series C, its partnered year. Mark: the $100M Series D of May 2022 'which "
                  "values the company at $1.1 billion' (the company's release), older than 24 months, as in the a16z "
                  "and Khosla books."))

# ---- Impossible Aerospace
L.append(cls("impossible-aerospace", status="acquired", rng="below_1b", country="US", city="Santa Clara",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2018-07-25",
             focus="Industrial & Robotics",
             rounds=[rnd("2018-09", "Series A", 9400000, "Bessemer Venture Partners", True, None, "press")],
             note="Battery-electric drones, Santa Clara; acq. by Alpine 4 Technologies, 2021 (the firm's listing). "
                  "Model: Bessemer led the $9.4M Series A announced with the US-1 drone in September 2018 (Airbus "
                  "Ventures and Eclipse took part), which matches the firm's own date of 2018-07-25; the pages "
                  "found (Forbes, The Verge, CNBC) could not be read to cite it."))

# ---- Incognia
L.append(cls("incognia", status="private", rng="below_1b", country="US", city="Palo Alto", stage="Growth",
             stage_src="first_party", stage_cite=POST("incognia-the"), stage_conf="high", entry_date="2024-01",
             focus="Security",
             rounds=[rnd("2024-01", "Series B", 31000000, "Bessemer Venture Partners", True, POST("incognia-the"),
                         "firm")],
             note="Location-based fraud prevention for mobile apps, Palo Alto. The firm's own post of 2024-01-31: "
                  "Bessemer leads the $31M Series B, its partnered year. Momentum check 2026-10-01: no later round "
                  "or valuation found (Google News)."))

# ---- Indian Energy Exchange
L.append(cls("indian-energy-exchange", status="public", rng="below_1b", usd=978422247, val_src="web_verified",
             val_cite=SA_IEX, asof="2026-10-01", country="IN", country_src="web_verified",
             country_cite=W("Indian Energy Exchange"), city="New Delhi", stage="undetermined",
             entry_date="2010-09-28", focus="Fintech & Payments",
             rounds=[rnd("2010-09", "minority investment alongside Lightspeed", None, None, True, None, "press")],
             note="Electronic power trading exchange, New Delhi (as in the Lightspeed book); listed on the NSE and "
                  "BSE since October 2017. INR 94.25B @ ECB 2026-10-01 (INR/EUR 108.832, EUR/USD 1.1298) = $978.4M "
                  "(StockAnalysis), within 5% of the $1B band edge and fresher than the Lightspeed book's $1.11B of "
                  "September 2026, which reads 1b_plus. The firm's own listing dates its investment 2010-09-28 and "
                  "names no round; no report naming it was found."))

# ---- Inertia
L.append(cls("inertia", status="private", rng="below_1b", city="Livermore", stage="Series A",
             stage_src="first_party", stage_cite=POST("inertia-enterprises"), stage_conf="high",
             entry_date="2026-02", focus="Climate & Energy",
             rounds=[rnd("2026-02", "Series A", 450000000, "Bessemer Venture Partners", True,
                         POST("inertia-enterprises"), "firm")],
             note="Inertia Enterprises, laser fusion energy, Livermore (as in the GV book). The firm's own post of "
                  "2026-02-11: Bessemer leads the $450M Series A (partnered year 2025). The valuation was not "
                  "disclosed (Google News, 2026-10-01), so the row reads below_1b under Rule A, as the GV row "
                  "does; a likely understatement."))

# ---- Innoviti
L.append(cls("innoviti", status="private", rng="below_1b", country="IN", country_src="web_verified",
             country_cite=LM_INNOVITI, city="Bangalore", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2017-07", focus="Fintech & Payments",
             rounds=[rnd("2017-07", "Series B", 18500000, "SBI-FMO Fund", True, LM_INNOVITI, "press"),
                     rnd("2020-02", "$5M round", 5000000, None, None, None, "press"),
                     rnd("2022-07", "$45M round", 45000000, "Panthera Growth Partners", None, None, "press")],
             note="Payment solutions for merchants, Bangalore. Livemint (2017-07-12, headline): Innoviti raises Rs120 "
                  "crore from the SBI-FMO fund and others, the firm's partnered year; model: that round is the "
                  "Series B, which Bessemer joined as a new investor beside the existing backer Catamaran."))

# ---- InRisk
L.append(cls("inrisk", status="private", rng="below_1b", country="IN", country_src="web_verified",
             country_cite=ISN_INRISK, city="Ahmedabad", city_src="web_verified", stage="Seed",
             stage_src="first_party", stage_cite=POST("why-we-invested-in-inrisk"), stage_conf="high",
             entry_date="2025-01", grad="graduated", grad_src="web_verified", grad_cite=EN_INRISK, grad_conf="high",
             focus="Fintech & Payments",
             rounds=[rnd("2025-01", "Seed", None, "Bessemer Venture Partners", True,
                         POST("why-we-invested-in-inrisk"), "firm"),
                     rnd("2026-08", "Series A", 27000000, "Bessemer Venture Partners and Northpoint Capital", True,
                         EN_INRISK, "press")],
             note="InRisk Labs, parametric climate insurance platform, Ahmedabad (Indian Startup News). The firm's "
                  "own post of 2025-01-14: Bessemer leads Inrisk's Seed fundraise. Graduated: the $27M Series A of "
                  "August 2026 co-led by Bessemer and Northpoint Capital (Entrackr), a named later round inside the "
                  "24-month window. Momentum check 2026-10-01: no valuation reported."))

# ---- Insmed (sale consideration for Transave)
L.append(verdict("insmed", "not_member",
                 "sale consideration: Insmed is the acquirer of the Bessemer portfolio company Transave, Inc. (base "
                 "row transave-inhalation-biopharmaceuticals, the firm's 2007 investment); the Bessemer funds "
                 "received Insmed stock in the business combination of 2010-12-02 and held no Insmed round before "
                 "it, so the acquirer leaves the base (Erik 2026-09-22; decisions.md D5)",
                 ec="web", conf="high", cite=K8_INSMED))

# ---- Instructure
L.append(cls("instructure", rng="below_1b", city="Salt Lake City", stage="Growth", stage_src="web_verified",
             stage_cite=S1_INSTRUCTURE, stage_conf="high", entry_date="2013-05-13", focus="SaaS",
             rounds=[rnd("2012-08", "Series C", 10000000, None, False, S1_INSTRUCTURE, "filing"),
                     rnd("2013-05", "Series D", 30000000, "Bessemer Venture Partners", True, S1_INSTRUCTURE,
                         "filing"),
                     rnd("2014-11", "Series E", 40000000, "Insight Venture Partners", True, S1_INSTRUCTURE,
                         "filing")],
             note="Canvas learning management software, Salt Lake City (as in the Insight book); IPO in 2015, taken "
                  "private by Thoma Bravo in 2020. The S-1's sales of preferred stock: entities affiliated with "
                  "Bessemer bought 3,270,440 shares of the Series D of May 2013 and none of the Series C of August "
                  "2012, so the entry is the Series D (Growth), dated by the firm's listing, and the pre-filled 2012 "
                  "date is replaced."))

jl.write("j03c", L)
