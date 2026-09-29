"""PRO-75 grind, judge j3: queue batch 3 (Chronosphere to Curie.Bio), one cls() per member row.
Citations are read from disk or printed by a tool (NEWS decodes, SITE/ARCH/W/FTS helpers); every page cited was read.
Run: NQ_TAG=j3 python3 judgments-j3.py   (J3_DRY=1 writes the .out.jsonl without recording)."""
import importlib.util
import os
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
TODAY = "2026-09-28"
GRAD_LATER = "Graduation left for the graduation pass."

# ---------------------------------------------------------------- chronosphere
C_SERC = NEWS("chronosphere", "Additional Series C")
L.append(cls("chronosphere", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Data Infrastructure",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=C_SERC, entry_date="2023-01-10",
             note="Cloud-native observability platform (New York). GV entered as a new investor in the $115M additional "
                  "Series C at a $1.6B valuation (Chronosphere's release, 2023-01-10: 'New investors include GV (formerly "
                  "Google Ventures) and Geodesic Capital'). Palo Alto Networks announced the acquisition in November 2025 "
                  "($3.35B) and completed it on 2026-01-29 (Palo Alto Networks' own release); the firm's exit line reads "
                  "'Acquired by Palo Alto Networks, 2025'. Status aligned with greylock, lux-capital and spark-capital.",
             rounds=[rnd("2023-01-10", "Series C", 115000000, None, True, C_SERC, "company")]))

# ---------------------------------------------------------------- circleup
CU_A = NEWS("circleup", "CircleUp Raises $7.5M")
CU_ACQ = NEWS("circleup", "CircleUp Acquired by Brightflow")
L.append(cls("circleup", status="acquired", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CU_A, entry_date="2013-05-07",
             note="Investing and credit platform for consumer brands (San Francisco). Forbes, 2013-05-07: CircleUp 'has "
                  "raised $7.5 million in a Series A funding round led by Union Square Ventures and joined by Google "
                  "Ventures, Maveron and Clayton Christensen's Rose Park Advisors' (read on the archived copy); the only "
                  "earlier money was the $1.5M pre-launch round from angels and Maveron (Wikipedia), so the A is GV's "
                  "entry. Canaan led the $14M 2014 round with 'previous investors Google Ventures and Union Square "
                  "Ventures'. Brightflow AI acquired the whole company in June 2023 (PR Newswire, 2023-06-02); the "
                  "union-square-ventures row still reads private, and this later cited sale is why the two differ.",
             rounds=[rnd("2013-05-07", "Series A", 7500000, "Union Square Ventures", True, CU_A, "press"),
                     rnd("2014", "Unnamed", 14000000, "Canaan Partners", True, W("CircleUp"), "press"),
                     rnd("2015-11-11", "Series C", 30000000, "Collaborative Fund", None, W("CircleUp"), "press")]))

# ---------------------------------------------------------------- circuithub
CH_A = NEWS("circuithub", "CircuitHub Raises $28M to Expand PCB")
CH_YC = "https://www.ycombinator.com/companies/circuithub"   # og:url printed by curl of the page, read 2026-09-28
CH_TC = ("https://techcrunch.com/2013/01/24/backed-by-y-combinator-and-google-ventures-circuithub-aims-to-be-a-one-stop-"
         "shop-for-electrical-parts/")   # printed by TechCrunch's own search API, read
L.append(cls("circuithub", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=CH_YC, city="London", city_src="web_verified", focus="Industrial & Robotics",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=CH_TC, entry_date="2013-01",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CH_A,
             note="On-demand electronics manufacturing (YC W12). TechCrunch, 2013-01-24: 'CircuitHub is backed by Y "
                  "Combinator with investments from Google Ventures and notable angel investors' (Buchheit, Cutts, "
                  "Ohanian, Taggar, Tan): the post-YC money from GV and angels is the seed, named from the record (model, "
                  "medium; the article dates it no later than January 2013). Plural led the $28M Series A in May 2026 "
                  "(Ventureburn), which graduates the row. The company's own YC directory page gives 'Location: London, "
                  "United Kingdom' (58 employees 'based in London'); its contact page lists the factory in South "
                  "Deerfield, Massachusetts and a UK office. Country and city follow the directory, as the y-combinator "
                  "row does; the a16z row reads US.",
             rounds=[rnd("2013-01", "Unnamed", None, None, True, CH_TC, "press"),
                     rnd("2026-05-20", "Series A", 28000000, "Plural", None, CH_A, "press")]))

# ---------------------------------------------------------------- clarifai
CL_W14 = NEWS("clarifai", "The AI Startup Google Should Probably")
CL_NEB = NEWS("clarifai", "Nebius snaps up Clarifai")
L.append(cls("clarifai", status="acquired", rng="below_1b", country="US", city="Washington", focus="AI & Applied AI",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=CL_W14, entry_date="2014",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=W("Clarifai"),
             note="Computer-vision and AI platform founded in late 2013 by Matthew Zeiler. WIRED, 2014-07-11, names "
                  "OkCupid co-founder Max Krohn as an angel and adds 'Another investor: Google Ventures', ahead of the "
                  "$10M Series A that Union Square Ventures led in 2015 (Wikipedia): the documented pre-A money is the "
                  "seed, named here from the record (model, medium). Menlo led the $30M Series B (2016), NEA the $60M "
                  "Series C (October 2021, no price disclosed). In May 2026 Nebius took the core team (CEO Zeiler became "
                  "Nebius's SVP Research), bought the patent portfolio and licensed the inference and orchestration "
                  "technology (SiliconANGLE and Nebius's own post, 2026-05-12); the firm's exit line reads 'Acquired by "
                  "Nebius, 2026'. Read as a sale of the business's core (team, patents, product technology), so "
                  "acquired; flagged in the report because the lux-capital, menlo-ventures and union-square-ventures "
                  "rows predate the deal and read private, and because the deal is also described as an acqui-hire. "
                  "City: Washington, as two of the three sibling rows carry (Wikipedia lists a Wilmington, Delaware "
                  "headquarters with offices in Washington, New York and San Francisco).",
             rounds=[rnd("2014", "Unnamed", None, None, True, CL_W14, "press"),
                     rnd("2015", "Series A", 10000000, "Union Square Ventures", None, W("Clarifai"), "press"),
                     rnd("2016", "Series B", 30000000, "Menlo Ventures", None, W("Clarifai"), "press"),
                     rnd("2021-10", "Series C", 60000000, "New Enterprise Associates", None, W("Clarifai"), "press")]))

# ---------------------------------------------------------------- classpass
CP_W = W("ClassPass")
L.append(cls("classpass", status="acquired", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CP_W, entry_date="2015-11",
             note="Fitness-class subscription marketplace (New York). Wikipedia: after the $40M Series B from General "
                  "Catalyst and Thrive (2015), 'Classpass received an additional $30 million of funding in November 2015 "
                  "led by Google Ventures'; a round after the B is Growth whatever its letter. Temasek led the $70M "
                  "Series C (2017) at $470M; the January 2020 round priced it at $1B. Acquired by Mindbody in October "
                  "2021 (Mindbody and ClassPass now sit under the Playlist parent brand, 2025).",
             rounds=[rnd("2014-03", "Seed", 2000000, None, None, CP_W, "press"),
                     rnd("2014-09", "Series A", 12000000, None, None, CP_W, "press"),
                     rnd("2015", "Series B", 40000000, "General Catalyst, Thrive Capital", None, CP_W, "press"),
                     rnd("2015-11", "Unnamed", 30000000, "GV", True, CP_W, "press"),
                     rnd("2017-05", "Series C", 70000000, "Temasek", None, CP_W, "press"),
                     rnd("2020-01", "Unnamed", 285000000, None, None, CP_W, "press")]))

# ---------------------------------------------------------------- clear-labs
CLB_B = NEWS("clear-labs", "Clear Labs Raises $13m Series B")
CLB_B2 = NEWS("clear-labs", "Series B2")
CLB_C = NEWS("clear-labs", "raises $60M to chase")
CLB_D = NEWS("clear-labs", "Clear Labs Secures $30 Million in Series D Financing to Accelerate Development and Adoption of Cutting-Edge Sequencing Solutions - PR")
L.append(cls("clear-labs", status="private", rng="below_1b", city="San Carlos", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CLB_B, entry_date="2016-12",
             note="Automated next-generation-sequencing platform for food safety and pathogen testing (San Carlos, per "
                  "its 2025 release). AgFunderNews, 2016-12-15: Clear Labs 'raised a $13 million Series B from ... GV, "
                  "... Felicis Ventures, Khosla Ventures, and ... Tencent'; the firm has listed it since the 2017 capture, "
                  "so the B is GV's entry. Menlo's $21M round of October 2018 was a Series B2 (Food Safety Magazine); a "
                  "$60M round followed in 2021 and a $30M Series D in January 2025 with GV among the existing investors "
                  "(no price disclosed). No $1B mark on record.",
             rounds=[rnd("2016-12-15", "Series B", 13000000, None, True, CLB_B, "press"),
                     rnd("2018-10-31", "Series B2", 21000000, None, None, CLB_B2, "press"),
                     rnd("2021-05-26", "Unnamed", 60000000, None, None, CLB_C, "press"),
                     rnd("2025-01-13", "Series D", 30000000, None, True, CLB_D, "company")]))

# ---------------------------------------------------------------- clearstory-data
CS_REG = NEWS("clearstory-data", "ClearStory uncloaks")
CS_GVN = NEWS("clearstory-data", "Shona Brown joins ClearStory")
CS_ACQ = NEWS("clearstory-data", "Alteryx Acquires ClearStory Data to Accelerate")
L.append(cls("clearstory-data", status="acquired", rng="below_1b", country="US", city="Menlo Park",
             focus="Data Infrastructure",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CS_GVN, entry_date="2012-03",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CS_GVN,
             note="Data analytics and harmonisation platform. The Register, 2012-03-19: the Palo Alto company 'has just "
                  "signed up Google Ventures, Andreessen Horowitz, and Khosla Ventures for its first round of venture "
                  "capital funding'; Global Venturing, 2013-07-30: Google Ventures 'participated in a $9m series A round "
                  "for ClearStory Data in December 2012, and also contributed to its seed funding'. Seed entry "
                  "(March 2012), graduated at the December 2012 Series A. Alteryx acquired it in April 2019 (PR "
                  "Newswire, 2019-04-04), when it was in Menlo Park.",
             rounds=[rnd("2012-03", "Seed", None, None, True, CS_REG, "press"),
                     rnd("2012-12", "Series A", 9000000, None, True, CS_GVN, "press")]))

# ---------------------------------------------------------------- climate-x
CX_A = NEWS("climate-x", "Climate Risk Assessment Platform Climate X Raises")
L.append(cls("climate-x", status="private", rng="below_1b", country="GB", country_src="web_verified", country_cite=CX_A,
             city="London", focus="Climate & Energy",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CX_A, entry_date="2024-06-27",
             note="Climate-risk analytics for banks, insurers and real-asset owners, UK-headquartered in London with a "
                  "New York office (ESG Today). GV led the $18M Series A (ESG Today, 2024-06-27; GV principal Roni "
                  "Hiranand quoted) with Pale blue dot, CommerzVentures and others; the firm has listed it since the "
                  "2024 capture, so the A is its entry. Google News for 'Climate X raises' (checked 2026-09-28) shows no "
                  "later round.",
             rounds=[rnd("2024-06-27", "Series A", 18000000, "GV", True, CX_A, "press")]))

# ---------------------------------------------------------------- cliqr-technologies
CQ_TC = NEWS("cliqr-technologies", "Cisco is buying CliQr")
CQ_SEED = "https://techcrunch.com/2012/06/25/google-ventures-backed-cliqr-brings-old-school-business-apps-to-the-cloud/"  # TechCrunch search API, read
L.append(cls("cliqr-technologies", status="acquired", rng="below_1b", country="US", city="San Jose",
             focus="Data Infrastructure",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CQ_SEED, entry_date="2012-06",
             note="Hybrid-cloud application management (San Jose, founded 2010). TechCrunch, 2012-06-25: the company 'has "
                  "raised a seed round of just under $1 million from Google Ventures and Foundation Capital, and it's "
                  "raising a Series A now' (the seed dated no later than June 2012). TechCrunch, 2016-03-01: Cisco is "
                  "buying CliQr for $260M; it 'had raised just over $38 million' from Google Ventures, Foundation Capital, "
                  "InstantScale, Polaris and Translink, so later rounds exist but none read here is named or dated. "
                  "Acquired by Cisco in 2016 (the firm's exit line). " + GRAD_LATER,
             rounds=[rnd("2012-06", "Seed", 1000000, None, True, CQ_SEED, "press")]))

# ---------------------------------------------------------------- cloudera
CD_IRA = FTS("Cloudera", "S-1")
CD_REL = ("https://www.cloudera.com/about/news-and-blogs/press-releases/2014-03-18-cloudera-raises-160-million-from-"
          "t-rowe-price-google-ventures-msd-capital-and-several-other-top-tier-institutional-investors.html")  # printed by the Wayback CDX query
L.append(cls("cloudera", rng="below_1b", city="Santa Clara", focus="Data Infrastructure",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CD_IRA, entry_date="2014-03-18",
             note="Hadoop-based data platform. The investor rights agreement filed with the 2017 S-1 (Exhibit 4.02) lists "
                  "'Google Ventures 2014, L.P.' under Schedule F, the Series F purchasers (1,373,626 shares), and in no "
                  "earlier series; Cloudera's release of 2014-03-18 announces the $160M round led by T. Rowe Price that "
                  "'included an investment by Google Ventures and an affiliate of MSD Capital' (read on the archived "
                  "copy). Entry: Series F, March 2014, Growth. IPO on the NYSE in 2017 (CLDR, the firm's exit line); "
                  "taken private by KKR and CD&R in 2021, so acquired and below_1b. City aligned with accel and greylock "
                  "(Santa Clara).",
             rounds=[rnd("2014-03-18", "Series F", 160000000, "T. Rowe Price", True, CD_REL, "company")]))

# ---------------------------------------------------------------- clover-health
CV_CNBC = NEWS("clover-health", "Clover Health got $425 million")
CV_CAP = "https://stockanalysis.com/stocks/clov/market-cap/"   # canonical printed by curl, read 2026-09-28
L.append(cls("clover-health", status="public", rng="1b_plus", usd=2300000000, val_src="web_verified", val_cite=CV_CAP,
             asof="2026-09-28", city="Franklin", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CV_CNBC, entry_date="2017-05",
             note="Medicare Advantage insurer (NASDAQ: CLOV since the January 2021 SPAC listing), headquartered in "
                  "Franklin, Tennessee (Wikipedia). CNBC, 2018-01-03: 'In May, Alphabet's venture arm GV joined a $130 "
                  "million financing round', the Series D led by Greenoaks in its table of rounds (A $100M 2015 First "
                  "Round, B $35M 2015 Sequoia, C $160M 2016 Greenoaks, D $130M May 2017 Greenoaks); Wikipedia names GV "
                  "in the 2017 Series D and in no earlier round. Market cap $2.30B as of 2026-09-28 (stockanalysis.com), "
                  "fresher than the $2.26B of 2026-09-04 that first-round-capital and spark-capital carry.",
             rounds=[rnd("2015-09", "Series A", 100000000, "First Round Capital", None, CV_CNBC, "press"),
                     rnd("2015-12", "Series B", 35000000, "Sequoia Capital", None, CV_CNBC, "press"),
                     rnd("2016-05", "Series C", 160000000, "Greenoaks", None, CV_CNBC, "press"),
                     rnd("2017-05", "Series D", 130000000, "Greenoaks", True, CV_CNBC, "press")],
             extra={"valuation_range_source": "web_verified"}))

# ---------------------------------------------------------------- clutter
CT_B = NEWS("clutter", "raised money for 2nd time in 5 months")
CT_C = NEWS("clutter", "Clutter Raises $64 Million To Move Your Mess")
CT_IM = NEWS("clutter", "Clutter by Iron Mountain")
L.append(cls("clutter", status="acquired", rng="below_1b", country="US", city="Los Angeles",
             focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CT_C, entry_date="2017-06-13",
             note="On-demand storage (Los Angeles). Sequoia led the $9M Series A (October 2015) and the $20M Series B "
                  "(April 2016, Business Insider). Forbes, 2017-06-13: Atomico led 'Clutter's third round' ($64M), and "
                  "Sequoia 'also joined this time, as did Google Ventures and Fifth Wall' (read on the archived copy); "
                  "Business Insider names GV beside 'existing investor Sequoia', so the third round is GV's entry "
                  "(Growth). Clutter absorbed MakeSpace in 2022 and now operates as 'Clutter by Iron Mountain' (Business "
                  "Wire via Yahoo Finance, 2026-08-13), the lender having taken it over, as the atomico row records; "
                  "acquired. City aligned with atomico (sequoia-capital's Culver City is a Form D address).",
             rounds=[rnd("2015-10", "Series A", 9000000, "Sequoia Capital", None, CT_B, "press"),
                     rnd("2016-04", "Series B", 20000000, "Sequoia Capital", None, CT_B, "press"),
                     rnd("2017-06-13", "Series C", 64000000, "Atomico", True, CT_C, "press")]))

# ---------------------------------------------------------------- cmd
CM_B = NEWS("cmd", "Series B led by Google Ventures")
CM_ACQ = NEWS("cmd", "to be acquired by enterprise search firm Elastic")
L.append(cls("cmd", status="acquired", rng="below_1b", country="CA", country_src="web_verified", country_cite=CM_B,
             city="Vancouver", focus="Security",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CM_B, entry_date="2019-02-26",
             note="Linux runtime security for cloud workloads (Vancouver). BetaKit, 2019-02-26: 'Vancouver's Cmd raises $19 "
                  "million CAD Series B led by Google Ventures' (Karim Faris quoted), bringing total funding past C$28M; "
                  "Business in Vancouver reported it as US$15M at the time. The firm has listed it since the 2019 "
                  "capture, so the Series B is its entry. Elastic agreed to acquire Cmd in August 2021 (BetaKit, "
                  "2021-08-27), matching the firm's exit line 'Acquired by Elastic, 2021'.",
             rounds=[rnd("2019-02-26", "Series B", 15000000, "GV", True, CM_B, "press")]))

# ---------------------------------------------------------------- cockroach-labs
CR_SEED = NEWS("cockroach-labs", "Cockroach Labs Raises $6.25M in Seed")
CR_F = NEWS("cockroach-labs", "More Than Doubles Its Valuation to $5B")
L.append(cls("cockroach-labs", rng="1b_plus", usd=5000000000, val_src="web_verified", val_cite=CR_F,
             asof="2021-12-16", city="New York", focus="Data Infrastructure",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CR_SEED, entry_date="2015-06",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CR_F,
             flags=("stale", "model_disputes_source"),
             note="Distributed SQL database (New York). FinSMEs, 2015-06-05: the New York company 'raised $6.25m in seed "
                  "funding. Backers included Benchmark, Google Ventures and Sequoia Capital' (read on the archived "
                  "copy); GV's entry is the seed. Graduated: its release of 2021-12-16 names a $278M Series F led by "
                  "Greenoaks at a $5B valuation, GV among the participants. Mark: the prefilled $2B (the January 2021 "
                  "Series E) is replaced by the later $5B Series F, as the coatue and sequoia-capital rows "
                  "carry; no newer priced round found, so the mark is flagged stale.",
             rounds=[rnd("2015-06-05", "Seed", 6250000, None, True, CR_SEED, "press"),
                     rnd("2021-12-16", "Series F", 278000000, "Greenoaks", True, CR_F, "company")],
             extra={"valuation_range_source": "web_verified"}))

# ---------------------------------------------------------------- cognosys (Ottogrid)
CG_TC = NEWS("cognosys", "AI startup Cohere acquires Ottogrid")
L.append(cls("cognosys", status="acquired", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=CG_TC, city="Vancouver", city_src="web_verified", focus="AI & Applied AI",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=CG_TC, entry_date="2023-05",
             note="AI agent and market-research platform, renamed Ottogrid in October 2024 (Vancouver). TechCrunch, "
                  "2025-05-16: Cohere acquires Ottogrid, formerly Cognosys, which 'raised $2 million in venture capital "
                  "from investors including GV (Google Ventures), Untapped Capital' and angels; the product is being "
                  "sunset. The firm's own /ai list dates its only investment May 2023. The company's one documented "
                  "round, $2M from GV and angels in its first year, is named the seed from the record (model, medium). "
                  "The acquisition decides the row's status (announced as an acquisition; the firm's exit line reads "
                  "'Acquired by Cohere, 2025'). " + GRAD_LATER,
             rounds=[rnd("2023-05", "Unnamed", 2000000, None, True, CG_TC, "press")]))

# ---------------------------------------------------------------- cohesity
CO_B = NEWS("cohesity", "Indian founded Cohesity emerges")
CO_C = "https://www.cohesity.com/newsroom/press/cohesity-raises-90-million-series-c-funding/"  # printed from the accel row; read
CO_H = "https://fintech.global/2024/12/12/data-protection-leader-cohesity-secures-7bn-valuation-following-veritas-merger/"  # printed from sibling rows; read
L.append(cls("cohesity", rng="1b_plus", usd=7000000000, val_src="web_verified", val_cite=CO_H, asof="2024-12",
             city="San Jose", focus="Data Infrastructure",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CO_B, entry_date="2015-06",
             flags=("model_disputes_source",),
             note="Data protection and secondary-storage platform. YourStory, June 2015 (read on the archived copy): after "
                  "the $15M Series A from Sequoia Capital and Wing, 'a massive $55million Series B round led by ARTIS "
                  "Ventures and Qualcomm Ventures along with Accel Partners, Battery Ventures, Google Ventures, and "
                  "Trinity Ventures'; the firm has listed it since the 2015 capture, so the B is GV's entry. GV and "
                  "Sequoia co-led the $90M Series C (Cohesity's release, 2017-04-04). Mark: the prefilled $3.7B is "
                  "replaced by the $7B the December 2024 Veritas combination and Haveli-led Series H put on the company "
                  "(FinTech Global, 2024-12-12), as accel, coatue and sequoia-capital carry. City San Jose, aligned with "
                  "those rows.",
             rounds=[rnd("2013", "Series A", 15000000, "Sequoia Capital, Wing Venture Capital", None, CO_B, "press"),
                     rnd("2015-06", "Series B", 55000000, "ARTIS Ventures, Qualcomm Ventures", True, CO_B, "press"),
                     rnd("2017-04-04", "Series C", 90000000, "GV, Sequoia Capital", True, CO_C, "company"),
                     rnd("2024-12", "Series H", None, "Haveli Investments", None, CO_H, "press")],
             extra={"valuation_range_source": "web_verified"}))

# ---------------------------------------------------------------- compass-therapeutics
CP_FB = NEWS("compass-therapeutics", "launches with $132M")
CP_CAP = "https://stockanalysis.com/stocks/cmpx/market-cap/"   # canonical printed by curl, read 2026-09-28
L.append(cls("compass-therapeutics", status="public", rng="below_1b", usd=199900000, val_src="web_verified",
             val_cite=CP_CAP, asof="2026-09-28", country="US", city="Boston", focus="Healthcare & Bio",
             stage="undetermined",
             note="Antibody therapeutics for oncology (NASDAQ: CMPX; 80 Guest Street, Boston). Founded 2014; Fierce Biotech, "
                  "2018-07-12, reports a $132M Series A assembled since inception from OrbiMed, F-Prime, Cowen Healthcare, "
                  "Thiel Capital and Alexandria, and does not name GV; the 2020 resale S-1 lists no GV holder. The firm "
                  "has listed it since the 2015 capture with Krishna Yeshwant as partner, but no source read ties GV "
                  "to a named round, so the stage is undetermined. Listed through a 2020 reverse merger, before which "
                  "the firm already listed it (not a post-IPO position). Market cap $199.9M as of 2026-09-28 "
                  "(stockanalysis.com), after the September 2026 FDA setback on tovecimig.",
             rounds=[rnd("2018-07-12", "Series A", 132000000, None, None, CP_FB, "press")]))

# ---------------------------------------------------------------- complyance
CY_TC = NEWS("complyance", "Complyance raises $20M to help companies")
CY_CCI = NEWS("complyance", "Complyance Raises $20M Series A Led by Google")
L.append(cls("complyance", status="private", rng="below_1b", country="US", city="New York", focus="Security",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CY_TC, entry_date="2026-02-11",
             note="AI-native governance, risk and compliance platform (New York, per Corporate Compliance Insights). "
                  "TechCrunch, 2026-02-11: GV led the $20M Series A; Corporate Compliance Insights names existing investors "
                  "Creandum, HV Capital, Speedinvest and Everywhere Ventures; the firm's /ai list dates its only investment February "
                  "2026, so the A is GV's entry. Momentum check 2026-09-28 (Google News for the company with valuation "
                  "and funding words): the February 2026 Series A is the latest round; no $1B mark.",
             rounds=[rnd("2026-02-11", "Series A", 20000000, "GV", True, CY_TC, "press")]))

# ---------------------------------------------------------------- context-ai
CX_BW = NEWS("context-ai", "Context.ai Raises $3.5M from GV")
CX_MAG = NEWS("context-ai", "OpenAI Acqui-hires Context.ai")
L.append(cls("context-ai", status="defunct", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=CX_BW, city="London", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CX_MAG, entry_date="2023-08-30",
             note="Product analytics and evaluations for LLM applications (London; Business Wire dateline). Business Wire, "
                  "2023-08-30: '$3.5M in funding co-led by GV (Google Ventures) and Tomasz Tunguz at Theory Ventures'; "
                  "Maginative, 2025-04-15: 'The pair raised $3.5 million in seed funding from GV and Theory Ventures'. "
                  "OpenAI hired the co-founders in April 2025 and Context.ai announced it would wind down its products "
                  "(Maginative). The hire does not decide the status (the 2026-09-20 acqui-hire rule); the wind-down "
                  "does, so defunct, although the firm's exit line reads 'Acquired by OpenAI, 2025'. " + GRAD_LATER,
             rounds=[rnd("2023-08-30", "Seed", 3500000, "GV, Theory Ventures", True, CX_BW, "company")]))

# ---------------------------------------------------------------- continua
CN_TC = NEWS("continua", "Google vet raises $8M for Continua")
CN_BW = NEWS("continua", "Former Google Distinguished Engineer David Petrou")
L.append(cls("continua", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CN_TC, entry_date="2025-08-12",
             grad="censored",
             note="AI agents for group chats, founded by former Google Distinguished Engineer David Petrou (New York, per "
                  "the Business Wire dateline). TechCrunch, 2025-08-12: Continua 'has raised an $8 million seed round. "
                  "The funding was led by GV, with additional participation from Bessemer'; the firm's /ai list dates "
                  "its only investment August 2025. Censored: the seed is inside the 24-month window. Momentum check "
                  "2026-09-28 (Google News for the company with funding and valuation words): no later round.",
             rounds=[rnd("2025-08-12", "Seed", 8000000, "GV", True, CN_TC, "press")]))

# ---------------------------------------------------------------- contraline
CL_A = NEWS("contraline", "Raises $7.2 Million in Series A")
L.append(cls("contraline", status="private", rng="below_1b", country="US", city="Charlottesville",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CL_A, entry_date="2022-11-15",
             note="Non-hormonal male contraceptive (ADAM hydrogel), Charlottesville, Virginia. citybiz, 2022-11-15: "
                  "Contraline 'has raised $7.2 million in Series A funding from investors led by Google's venture arm GV', "
                  "after a $10.7M Series A in 2021 led by MBX Capital; the firm has listed it since the 2023 capture, so "
                  "GV entered in the second Series A close. A $92.5M Series B followed in June 2026 (Business Wire); no "
                  "valuation disclosed.",
             rounds=[rnd("2021", "Series A", 10700000, "MBX Capital", None, CL_A, "press"),
                     rnd("2022-11-15", "Series A", 7200000, "GV", True, CL_A, "press")]))

# ---------------------------------------------------------------- corduro
L.append(cls("corduro", status="private", rng="below_1b", city="Southlake", city_src="formd_address",
             focus="Fintech & Payments",
             note="Payment processing for merchants (Corduro, Inc., Southlake, Texas, incorporated 2010). Its April 2010 "
                  "Form D ($3.3M, Joe Kraus of Google Ventures a director) is the seed on the row. The company's own site "
                  "(corduro.com, the firm's link) still sells terminals, gateway and processing plans, 'a brand of its "
                  "operating companies Corduro Processing, Inc., and Corduro Merchant Services, LLC', so it reads "
                  "private; Google News has no coverage of the company. " + GRAD_LATER))

# ---------------------------------------------------------------- coreos
CRS_A = "https://techcrunch.com/2015/04/06/coreos-raises-12m-funding-round-led-by-google-ventures-to-bring-kubernetes-to-the-enterprise/"  # TechCrunch search API, read
CRS_B = "https://techcrunch.com/2016/05/09/coreos-raises-28m-series-b-round-led-by-gv/"  # TechCrunch search API, read
L.append(cls("coreos", status="acquired", rng="below_1b", city="San Francisco", focus="Data Infrastructure",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CRS_B, entry_date="2015-04-06",
             flags=("stage_disputes_band",),
             note="Container Linux and Kubernetes (Tectonic) company, San Francisco. TechCrunch, 2015-04-06: CoreOS 'has "
                  "raised a $12 million funding round led by Google Ventures' with KPCB, Fuel and Accel (total $20M); "
                  "TechCrunch, 2016-05-09, on the $28M Series B GV also led: 'GV already led CoreOS's add-on to its Series "
                  "A round'. GV's entry is therefore the April 2015 Series A add-on, not the 2016 Series B the Form D "
                  "band anchored (Dave Munichiello a director on the 2016 filing): stage_disputes_band. Red Hat bought "
                  "CoreOS for $250M in January 2018 (TechCrunch, 2018-01-30), the firm's exit line 'Acquired by Red Hat, "
                  "2018'.",
             rounds=[rnd("2015-04-06", "Series A extension", 12000000, "GV", True, CRS_A, "press"),
                     rnd("2016-05-09", "Series B", 28000000, "GV", True, CRS_B, "press")]))

# ---------------------------------------------------------------- counsel-health
CH_A = NEWS("counsel-health", "Counsel Health raises $25M series A")
CH_SEED = NEWS("counsel-health", "Launches with $11M in Seed Funding")
L.append(cls("counsel-health", status="private", rng="below_1b", country="US", city="New York",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CH_A, entry_date="2025-10-17",
             note="Physician-supervised AI medical care (New York, per its launch release). Andreessen Horowitz led the "
                  "$11M seed (PR Newswire, 2024-10-22, no GV); Fierce Healthcare, 2025-10-17: 'a series A round led by "
                  "Andreessen Horowitz and GV', $25M; the firm's /ai list dates its only investment October 2025. "
                  "Momentum check 2026-09-28 (Google News): no later round or $1B mark.",
             rounds=[rnd("2024-10-22", "Seed", 11000000, "Andreessen Horowitz", False, CH_SEED, "company"),
                     rnd("2025-10-17", "Series A", 25000000, "Andreessen Horowitz, GV", True, CH_A, "press")]))

# ---------------------------------------------------------------- crash-override
CO_AW = NEWS("crash-override", "Daily Funding Report: 7/16/2025")
L.append(cls("crash-override", status="private", rng="below_1b", city="New York", city_src="formd_address",
             focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CO_AW, grad="censored",
             note="Engineering visibility platform tying code to cloud deployments (Crash Override, Inc., New York; "
                  "founded 2022 by John Viega and Mark Curphey). AlleyWatch, 2025-07-16: it 'has raised $28M in Seed "
                  "funding led by SYN Ventures and Google Ventures'. The company's Form Ds show the seed in three closes "
                  "($5.75M 2022, $7.55M 2024, $13.25M first sold 2025-02-20); Erik Nordlander of GV appears only on the "
                  "2025 close, which dates GV's entry (the row's entry date). Censored: inside the 24-month window. "
                  "Momentum check 2026-09-28 (Google News): no later round.",
             rounds=[rnd("2022-07-29", "Seed", 5749999, None, None,
                         "https://www.sec.gov/Archives/edgar/data/1941448/000194144822000002/0001941448-22-000002-index.htm",
                         "filing"),
                     rnd("2024-02-07", "Seed", 7549996, None, None,
                         "https://www.sec.gov/Archives/edgar/data/1941448/000194144824000001/0001941448-24-000001-index.htm",
                         "filing"),
                     rnd("2025-02-20", "Seed", 13249999, "SYN Ventures, GV", True, CO_AW, "press")]))

# ---------------------------------------------------------------- cribl
CB_E = NEWS("cribl", "Data infrastructure startup Cribl raises $319M")
L.append(cls("cribl", status="private", rng="1b_plus", usd=3500000000, val_src="web_verified", val_cite=CB_E,
             asof="2024-08-27", city="San Francisco", focus="Data Infrastructure", flags=("stale",),
             note="Telemetry and security data pipelines (San Francisco). TechCrunch, 2024-08-27: a $319M Series E 'led by "
                  "new investor GV' at a $3.5B valuation, GV's entry (the Form D band agrees). The mark is now older than "
                  "24 months (stale). Momentum check 2026-09-28 (Google News for valuation, tender and funding words): "
                  "Axios reported in February 2026 that Cribl 'eyes secondary offering' after passing $300M ARR; no "
                  "completed priced round or tender found, so $3.5B stands, as greylock, ivp, redpoint-ventures and "
                  "sequoia-capital carry.",
             rounds=[rnd("2024-08-27", "Series E", 319000000, "GV", True, CB_E, "press")],
             extra={"valuation_range_source": "web_verified"}))

# ---------------------------------------------------------------- cur8
CU_TC = NEWS("cur8", "Climate startup CUR8 raises")
CU_SEED = NEWS("cur8", "CUR8 Secures Seed Investment Led by Airbus")
L.append(cls("cur8", status="private", rng="below_1b", country="GB", country_src="web_verified", country_cite=CU_TC,
             city="London", focus="Climate & Energy",
             stage="Pre-Seed", stage_src="web_verified", stage_conf="high", stage_cite=CU_TC, entry_date="2023-05-31",
             note="Carbon-removal portfolio and market-making platform, U.K.-based (London). TechCrunch, 2023-05-31: it "
                  "'raised $6.5 million (£5.3 million) in pre-seed funding led by GV (Google Ventures)' with CapitalT "
                  "(GBP 5.3M @ ECB 2023-05-30 = $6.6M; the press figure is used). Airbus Ventures led its seed round in "
                  "September 2025 with 'existing backers GV (Google Ventures) and CapitalT' (Carbon Herald). A Pre-Seed "
                  "entry is outside the seed-to-A cohort.",
             rounds=[rnd("2023-05-31", "Pre-Seed", 6500000, "GV", True, CU_TC, "press"),
                     rnd("2025-09-29", "Seed", None, "Airbus Ventures", True, CU_SEED, "press")]))

# ---------------------------------------------------------------- curie-bio: not a company position (decisions.md D10)
CB_FIERCE = "https://www.fiercebiotech.com/biotech/weinberg-borisy-launch-new-biotech-vc-offer-drug-discovery-copilots"  # WebSearch result, read
L.append(verdict("curie-bio", "not_member",
                 "decisions.md D10 (T5, fund-shaped position): Curie.Bio is a biotech venture firm, not an operating "
                 "company. Fierce Biotech (2023 launch, read): the 'new biotech VC' raised $520 million 'from an "
                 "assortment of investors, including GV, ARCH Venture Partners and a16z' into 'an investing vehicle that "
                 "will provide seed-stage money to startups and a unit that will provide various services'; it has since "
                 "raised a $380M Series A fund (2024) and a $340M seed fund (2025). GV's position is an interest in the "
                 "investing vehicle, the LP-stake class (the Oxford Science Enterprises reading). The a16z row carries "
                 "it as a member; flagged for Erik.",
                 ec="web", conf="medium", cite=CB_FIERCE))

# ---------------------------------------------------------------- clever
CV_SEED = "https://techcrunch.com/2012/10/22/clever-seed/"   # TechCrunch search API, read
CV_A = ("https://techcrunch.com/2014/03/25/18k-schools-and-counting-clever-confirms-10-3m-raise-from-sequoia-paul-graham-"
        "as-it-looks-to-build-the-next-big-learning-platform/")   # TechCrunch search API, read
L.append(cls("clever", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CV_SEED, entry_date="2012-10-22",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CV_A,
             flags=("model_disputes_source",),
             note="Single sign-on and data platform for K-12 schools (YC S12), founded in San Francisco in 2012. "
                  "TechCrunch, 2012-10-22: Clever 'has raised $3 million in seed funding' from SV Angel, Floodgate, "
                  "SoftTech VC, 'Google Ventures (Kevin Rose)', Bessemer and angels. Graduated: Sequoia led the $10.3M "
                  "Series A (TechCrunch, 2014-03-25); Lightspeed led the $30M round of December 2014. Kahoot! acquired "
                  "it in 2021 for about $500M (Wikipedia; the firm's exit line). The prefilled DK comes from a one-word "
                  "name match on the acquirer's country; the company is in San Francisco, as a16z, general-catalyst and "
                  "sequoia-capital record.",
             rounds=[rnd("2012-10-22", "Seed", 3000000, None, True, CV_SEED, "press"),
                     rnd("2014-03-25", "Series A", 10300000, "Sequoia Capital", None, CV_A, "press")]))

# ---------------------------------------------------------------- clever-care
CC_C = NEWS("clever-care", "Closes $42M Series C")
L.append(cls("clever-care", status="private", rng="below_1b", country="US", city="Huntington Beach",
             focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CC_C, entry_date="2023-03-16",
             note="Culturally tailored Medicare Advantage plan for Asian American seniors, Huntington Beach, California "
                  "(citybiz). citybiz, 2023-03-16: Clever Care 'raised $42M in Series C funding. The round was led by "
                  "GV', with new investor Point32Health and existing investors including Norwest; the firm has listed it "
                  "since the 2023 capture, so the C is GV's entry. Operating in 2026 (its February 2026 release reports "
                  "enrollment up nearly 50 percent); no valuation disclosed.",
             rounds=[rnd("2023-03-16", "Series C", 42000000, "GV", True, CC_C, "press")]))

# ---------------------------------------------------------------- collaborate
CB_CISCO = NEWS("collaborate", "Cisco Announces Acquisition of Collaborate.com")
L.append(cls("collaborate", status="acquired", rng="below_1b", country="US", focus="SaaS", stage="undetermined",
             flags=("city_unknown",),
             note="Collaborate.com, a mobile document-sharing, task and team-communication app. Cisco announced its "
                  "acquisition on 2013-12-17 (Cisco's own blog), matching the firm's exit line 'Acquired by Cisco, "
                  "2013'. No source read names GV's round or places the company (the Cisco post gives no location; Google "
                  "News and TechCrunch's own search return only the acquisition), so the stage is undetermined and the "
                  "city unknown; the country is the model's reading of a Cisco tuck-in the firm listed from 2013.",
             rounds=[]))

# ---------------------------------------------------------------- collective-health
CH_C = NEWS("collective-health", "Collective Health Raises $81M")
CH_E = NEWS("collective-health", "raises $205 million in funding round")
CH_F = NEWS("collective-health", "Collective Health Valued at $1.5 Billion")
L.append(cls("collective-health", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified",
             val_cite=CH_F, asof="2021-05-04", country="US", city="San Francisco", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CH_C, entry_date="2015-10-20",
             flags=("stale",),
             note="Employer health-benefits platform (San Francisco). HIT Consultant, 2015-10-20: '$81 million in Series C "
                  "funding led by Google Ventures and returning investors NEA and Founders Fund' (after a $32M Series B "
                  "in March 2015); the firm first appears in the 2015 capture, so the C is GV's entry. MarketWatch on "
                  "the 2019 $205M round (SoftBank Vision Fund led, GV among existing investors): the company 'declined "
                  "to disclose its current valuation'. Mark: Bloomberg's headline of 2021-05-04, 'Collective Health "
                  "Valued at $1.5 Billion After Funding Infusion' (the $280M Series F), read from the headline "
                  "(paywalled); no priced event since, so stale. Aligned with redpoint-ventures' $1.5B.",
             rounds=[rnd("2015-10-20", "Series C", 81000000, "GV", True, CH_C, "press"),
                     rnd("2019-06-17", "Unnamed", 205000000, "SoftBank Vision Fund", True, CH_E, "press"),
                     rnd("2021-05-04", "Series F", 280000000, None, None, NEWS("collective-health", "Collective Health nets hefty $280M"), "press")],
             extra={"valuation_range_source": "web_verified"}))

# ---------------------------------------------------------------- comanche-biopharma
CM_B = NEWS("comanche-biopharma", "Comanche raises $75m")
L.append(cls("comanche-biopharma", status="private", rng="below_1b", city="Concord", city_src="formd_address",
             focus="Healthcare & Bio",
             note="siRNA therapy for preeclampsia (Comanche Biopharma Corp., Concord, Massachusetts, on both Form Ds and "
                  "its 2023 release dateline). Raised a $75M Series B in January 2024 (Pharmaceutical Technology) and is "
                  "still among the preeclampsia drug developers in 2026 coverage; no valuation disclosed. The entry stays on the Form D band "
                  "(Brendan Bulik-Sullivan a director on the round first sold 2021-06-28, $36.1M); since the next round "
                  "is named the Series B, that round is probably the Series A, a band dispute a later pass could settle "
                  "with a source naming it.",
             rounds=[rnd("2024-01-18", "Series B", 75000000, None, None, CM_B, "press")]))

# ---------------------------------------------------------------- comfy (Building Robotics)
CF_SEED = ("https://techcrunch.com/2013/11/08/building-robotics-lands-1-14m-seed-round-from-ccv-google-ventures-and-other-"
           "angel-investors/")   # TechCrunch search API, read
CF_B = "https://techcrunch.com/2016/06/08/comfy-raises-8-million-for-app-to-end-office-thermostat-wars/"  # TechCrunch search API, read
L.append(cls("comfy", status="acquired", rng="below_1b", country="US", city="Oakland", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CF_SEED, entry_date="2013-11-08",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CF_B,
             flags=("model_disputes_source",),
             note="Building Robotics, maker of the Comfy workplace app for office climate and space (Oakland, California). "
                  "TechCrunch, 2013-11-08: '$1.14 million in a seed round led by Claremont Creek Ventures (CCV), Google "
                  "Ventures, Formation 8' and others. Graduated: Emergence Capital led the $12M Series B (TechCrunch, "
                  "2016-06-08). Siemens acquired Building Robotics in 2018 (Siemens' own release; the firm's exit line). "
                  "The prefilled UA comes from a one-word name match; the company is in Oakland.",
             rounds=[rnd("2013-11-08", "Seed", 1140000, "Claremont Creek Ventures, GV", True, CF_SEED, "press"),
                     rnd("2016-06-08", "Series B", 12000000, "Emergence Capital", None, CF_B, "press")]))

# ---------------------------------------------------------------- comstruct
CS_TC = NEWS("comstruct", "Comstruct raises $13M")
CS_BB = NEWS("comstruct", "secures a 12.5 million euros round")
L.append(cls("comstruct", status="private", rng="below_1b", country="DE", country_src="web_verified",
             country_cite=CS_BB, city="Munich", focus="SaaS",
             stage="Series A", stage_src="model", stage_conf="medium", stage_cite=CS_BB, entry_date="2025-02-06",
             note="Procurement platform for construction materials, Munich-headquartered (BeBeez). GV and 20VC led a "
                  "EUR 12.5M round with existing shareholders Booom and Puzzle Ventures, who had joined the 2023 "
                  "pre-seed (BeBeez, 2025-02-10; TechCrunch, 2025-02-06; PropTech Connect names no series). The first "
                  "institutional round after a pre-seed, at a Series A size, is named the Series A from the record "
                  "(model, medium), as the 20vc row reads it. EUR 12.5M @ ECB 2025-02-10 (EUR/USD 1.032) = $12.9M; "
                  "TechCrunch reported $13M at the time. Momentum check 2026-09-28: no later round found.",
             rounds=[rnd("2023", "Pre-Seed", None, None, False, CS_BB, "press"),
                     rnd("2025-02-06", "Unnamed", 13000000, "GV, 20VC", True, CS_TC, "press")]))

# ---------------------------------------------------------------- confide
CFD_SEED = "https://techcrunch.com/2014/02/04/confide-1-9m/"   # TechCrunch search API, read
CFD_EXT = ("https://techcrunch.com/2016/03/10/confide-confidential-messenger-gets-1-6-million-launches-premium-message-"
           "retraction/")   # TechCrunch search API, read
CFD_ACQ = "https://techcrunch.com/2021/01/27/iacs-teltech-acquired-encrypted-mobile-messaging-app-confide/"  # first-round-capital row; read
L.append(cls("confide", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CFD_SEED, entry_date="2014-02-04",
             note="Encrypted, self-destructing messaging app (New York). TechCrunch, 2014-02-04: '$1.9 million in seed "
                  "funding that was led by WGI Group and includes investors such as Google Ventures, First Round "
                  "Capital, SV Angel'; a $1.6M seed extension followed in March 2016 (TechCrunch). IAC's Teltech acquired "
                  "it in January 2021 and kept the apps available (TechCrunch, 2021-01-27), the firm's exit line "
                  "'Acquired by IAC, 2021'. The first-round-capital row reads defunct on a later wind-down; the sale is "
                  "the company's own last event, so acquired here, flagged for alignment. " + GRAD_LATER,
             rounds=[rnd("2014-02-04", "Seed", 1900000, "WGI Group", True, CFD_SEED, "press"),
                     rnd("2016-03-10", "Seed extension", 1600000, None, None, CFD_EXT, "press")]))

# ---------------------------------------------------------------- cool-planet
CPL_D = NEWS("cool-planet", "Raises $100M in Series D")
L.append(cls("cool-planet", status="unknown", rng="below_1b", country="US", city="Greenwood Village",
             focus="Climate & Energy", stage="undetermined",
             note="Cool Planet Energy Systems: biofuels, then engineered biochar (Cool Terra). The firm's link now points to "
                  "coolplanet.io, which is CoolPlanet Ltd, an unrelated energy-software company; the archived listing "
                  "('negative carbon and carbon neutral fuels based on plant photosynthesis') identifies the biochar "
                  "company. AgFunderNews, 2014-04-04: a $100M Series D placed by UBS and Goldman Sachs, 'all previous "
                  "strategic and venture investors added', and 'Previous investors also include Google Ventures' (GV "
                  "listed it from 2012): GV's own entry round is not named in any source read, so undetermined. Coverage "
                  "stops after the 2018 Alexandria, Louisiana plant and a 2021 DeSmog critique; no source read gives "
                  "the company's fate, so status unknown. City is the model's (Greenwood Village, Colorado, where it "
                  "moved from Camarillo).",
             rounds=[rnd("2014-04-04", "Series D", 100000000, "UBS, Goldman Sachs", True, CPL_D, "press")]))

# ---------------------------------------------------------------- copper (ProsperWorks)
CPR_C = "https://techcrunch.com/2017/09/26/prosperworks-raises-53m-for-its-g-suite-centric-crm-service/"  # TechCrunch search API, read
CPR_B = "https://techcrunch.com/2016/09/27/prosperworks-raises-24m-for-its-google-centric-crm-solution/"   # TechCrunch search API, read
L.append(cls("copper", status="private", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CPR_C, entry_date="2017-09-26",
             flags=("model_disputes_source",),
             note="Copper (formerly ProsperWorks), the CRM built into Google Workspace (San Francisco). The $24M Series B "
                  "of September 2016 was led by Next World Capital with no GV (TechCrunch); TechCrunch, 2017-09-26: 'a "
                  "$53 million Series C round led by Norwest Venture Partners, with participation from GV', GV's entry "
                  "(the firm first lists it in 2017). Operating in 2026 ('Copper CRM, Inc. © 2026' on its site); no "
                  "priced mark. The prefilled GB comes from a one-word name match.",
             rounds=[rnd("2016-09-27", "Series B", 24000000, "Next World Capital", False, CPR_B, "press"),
                     rnd("2017-09-26", "Series C", 53000000, "Norwest Venture Partners", True, CPR_C, "press")]))

# ---------------------------------------------------------------- cord (Cord Project)
CRD_SEED = ("https://techcrunch.com/2014/12/15/cord-project-launches-voice-messaging-app-that-borrows-the-good-parts-of-"
            "texting/")   # TechCrunch search API, read
CRD_ACQ = "https://techcrunch.com/2016/01/20/spotify-buys-cord-project-and-soundwave/"   # TechCrunch search API, read
L.append(cls("cord", status="acquired", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CRD_SEED, entry_date="2014-12-15",
             flags=("city_unknown",),
             note="Cord Project, a one-tap voice-messaging app by two former Google Creative Lab staff. TechCrunch, "
                  "2014-12-15: it 'raised $1.8 million in seed funding led by Lerer Hippeau Ventures and Metamorphic "
                  "Ventures, with participation from Google Ventures, Greycroft' and others. Spotify confirmed it had "
                  "acquired Cord Project in January 2016 (TechCrunch, 2016-01-20; five of seven staff joined, the app "
                  "shut), the firm's exit line 'Acquired by Spotify, 2016'. No source read places the company in a "
                  "city. " + GRAD_LATER,
             rounds=[rnd("2014-12-15", "Seed", 1800000, "Lerer Hippeau Ventures, Metamorphic Ventures", True, CRD_SEED,
                         "press")]))

# ---------------------------------------------------------------- cosmos
CSM_A = NEWS("cosmos", "Cosmos: $15 Million Series A")
CSM_BI = NEWS("cosmos", "Meet the founders of 18 startups disrupting")
L.append(cls("cosmos", status="private", rng="below_1b", country="US", country_src="web_verified", country_cite=CSM_BI,
             city="New York", city_src="web_verified", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CSM_BI, entry_date="2023",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CSM_A,
             flags=("model_disputes_source",),
             note="Visual bookmarking and discovery app, a Pinterest alternative (cosmos.so), founded by Andy McCune and "
                  "Luca Marra. Business Insider's founders roundup (early 2024): 'Location: New York ... Funding: $6 "
                  "million, led by GV and Accel, per the company'. Entry date: the firm added Cosmos to its own "
                  "portfolio records in June 2023 (its CMS entry), the listing year. Graduated: Pulse 2.0, 2026-01-21, a "
                  "$15M Series A co-led by Shine Capital and Matrix, with GV and Accel investing again. The prefilled "
                  "status (acquired) and country (MA) come from a one-word name match on another Cosmos; the company "
                  "is private and in New York.",
             rounds=[rnd("2023", "Seed", 6000000, "GV, Accel", True, CSM_BI, "press"),
                     rnd("2026-01-21", "Series A", 15000000, "Shine Capital, Matrix", True, CSM_A, "press")]))

# ---------------------------------------------------------------- courier
CRR_B = NEWS("courier", "Courier lands $35M")
L.append(cls("courier", status="private", rng="below_1b", country="US", city="San Francisco", focus="DevTools & APIs",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CRR_B, entry_date="2022-06-22",
             flags=("model_disputes_source",),
             note="Notification and customer-messaging API (YC S19, San Francisco). TechCrunch, 2022-06-22: Courier 'closed "
                  "a $35 million Series B funding round led by GV', with Bessemer, Matrix, Twilio Ventures, Slack Fund and "
                  "YC; the firm first lists it in 2022, so the B is GV's entry. The prefilled status (acquired) comes "
                  "from a name match on another Courier: the company operates ('© 2026 Courier' on courier.com) and the "
                  "firm shows no exit. Momentum check 2026-09-28 (Google News for the company with funding, valuation "
                  "and acquisition words): no later round or $1B mark.",
             rounds=[rnd("2022-06-22", "Series B", 35000000, "GV", True, CRR_B, "press")]))

# ---------------------------------------------------------------- cozy
CZ_B = "https://techcrunch.com/2016/08/30/cozy-raises-8-5m-series-b-to-simplify-life-for-property-managers-and-renters/"  # TechCrunch search API, read
CZ_A = "https://techcrunch.com/2014/02/11/cozy-credit-reporting/"   # TechCrunch search API, read
L.append(cls("cozy", status="acquired", rng="below_1b", country="US", city="Portland",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Rental management for landlords and tenants; moved its headquarters from San Francisco to Portland, "
                  "Oregon in 2013 (GeekWire, 2015). TechCrunch reports a Series A led by General Catalyst (2014-02-11) "
                  "and an $8.5M Series B led by American Family Ventures with the Series A investors (2016-08-30); "
                  "GeekWire's 2015 $3.4M round names Butterfield, Calacanis, General Catalyst and Seven Peaks. None names "
                  "GV, which listed Cozy from 2013, so the stage is undetermined. CoStar acquired it in 2018 (the firm's "
                  "exit line).",
             rounds=[rnd("2013", "Series A", None, "General Catalyst", None, CZ_A, "press"),
                     rnd("2015-08-31", "Unnamed", 3400000, None, None, NEWS("cozy", "Cozy raises $3.4M from Slack co-founder"),
                         "press"),
                     rnd("2016-08-30", "Series B", 8500000, "American Family Ventures", None, CZ_B, "press")]))

# ---------------------------------------------------------------- creativelive
CL_A1 = "https://techcrunch.com/2012/10/09/creativelive/"   # TechCrunch search API, read
CL_A2 = ("https://techcrunch.com/2013/03/11/caa-william-morris-kevin-rose-more-put-8m-into-hot-online-classroom-creativelive-"
         "flickr-founder-joins-board/")   # TechCrunch search API, read
CL_B = ("https://techcrunch.com/2013/11/14/with-2m-creatives-and-1b-minutes-of-video-served-creativelive-lands-21-5m-"
        "to-bring-free-live-courses-to-the-worlds-creative-entrepreneurs/")   # TechCrunch search API, read
L.append(cls("creativelive", status="acquired", rng="below_1b", country="US", city="Seattle",
             focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CL_A2, entry_date="2013-03-11",
             note="Live online creative classes (Seattle, with a San Francisco studio; GeekWire). Greylock led the $7.5M "
                  "Series A in October 2012 (TechCrunch); TechCrunch, 2013-03-11: CreativeLIVE 'has raised $8 million in "
                  "series A financing from Creative Artists Agency, William Morris Endeavor, CrunchFund and Google "
                  "Ventures', GV's entry in the second close of the A. Social+Capital led the $21.5M Series B in "
                  "November 2013 (TechCrunch; GeekWire). Fiverr acquired it in October 2021 (GeekWire; TechCrunch). Aligned with "
                  "felicis and greylock on status and city.",
             rounds=[rnd("2012-10-09", "Series A", 7500000, "Greylock Partners", None, CL_A1, "press"),
                     rnd("2013-03-11", "Series A", 8000000, None, True, CL_A2, "press"),
                     rnd("2013-11-14", "Series B", 21500000, "Social+Capital", None, CL_B, "press")]))

# ---------------------------------------------------------------- crews-by-core
CBC_BI = NEWS("crews-by-core", "WakeCap Acquires Construction Startup")
L.append(cls("crews-by-core", status="acquired", rng="below_1b", country="US", focus="SaaS", stage="undetermined",
             flags=("city_unknown",),
             note="Scheduling and daily-reporting software for construction foremen, founded by Di-Ann Eisnor (Waze, "
                  "Google). Business Insider, 2024-07-02: it 'had raised $11 million from investors such as Streamlined "
                  "Ventures, NFX, GV, and Caterina Fake's Yes VC', and Saudi Arabia's WakeCap is buying it in an "
                  "all-stock deal, the firm's exit line 'Acquired by WakeCap, 2024'. No source read names GV's round or "
                  "the company's city (the article says only that the founder lives in New York City).",
             rounds=[]))

# ---------------------------------------------------------------- ctrl-labs
CT_B = NEWS("ctrl-labs", "Ctrl-Labs raises $28m")
CT_ACQ = NEWS("ctrl-labs", "Facebook agrees to acquire brain-computing")
L.append(cls("ctrl-labs", rng="below_1b", country="US", city="New York", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CT_B, entry_date="2018",
             note="Neural-interface wristband (New York; Thomas Reardon). MassDevice, 2019-02-25: a $28M round 'joined by "
                  "both Google and Amazon', 'led by Google's venture arm, GV, and joined by the Amazon Alexa Fund, Lux "
                  "Capital, Spark Capital' and others, total raised $67M; Wikipedia (Thomas Reardon) calls it the "
                  "Series B, and TechCrunch reported it closed by November 2018, when the firm first lists the company. "
                  "Entry: Series B, Growth. Facebook bought CTRL-labs in September 2019 for between $500M and $1B "
                  "(CNBC; a Facebook spokesperson said under $1B); status acquired, below_1b.",
             rounds=[rnd("2018", "Series B", 28000000, "GV", True, CT_B, "press")]))


jl.write("j3", L, record=os.environ.get("J3_DRY") != "1")
