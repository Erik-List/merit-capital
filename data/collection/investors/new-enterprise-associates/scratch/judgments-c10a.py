"""PRO-100 NEA, judge c10, queue batch 19 (spring-mobile-solutions .. teal): classification of listed members,
plus three membership corrections under D8 and X1 (synopsys, sunesis, supergen)."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, NEWS, ARCH

SA = "https://stockanalysis.com/stocks/{}/market-cap/"
S1_TABLEAU = "https://www.sec.gov/Archives/edgar/data/1303652/000119312513138700/d469057ds1.htm"
S1_SURFACE = "https://www.sec.gov/Archives/edgar/data/1718108/000119312518094098/d471930ds1.htm"
S1_SUPERNUS = "https://www.sec.gov/Archives/edgar/data/1356576/000104746910010575/a2201368zs-1.htm"
S1_SPYGLASS = "https://www.sec.gov/Archives/edgar/data/1778922/000162828026002356/spyglass-sx1.htm"
EX_SYNLOGIC = "https://www.sec.gov/Archives/edgar/data/1527599/000119312517270395/d431294dex991.htm"
K8_SUNESIS = "https://www.sec.gov/Archives/edgar/data/1061027/000114420409018324/v145069_8k.htm"
TC_SUBTEXT = "https://techcrunch.com/2011/10/25/subtext-raises-3-million-from-google-ventures-more-to-make-ebook-reading-social/"
NW_SUNDECK = "https://www.newswire.com/news/sundeck-announces-the-public-availability-of-its-query-engineering-22049696"
GL = "Graduation left for the graduation pass."

L = []

# ---- membership corrections (verdict line only)
L.append(verdict("synopsys", "not_member",
                 "D8, sale consideration: Synopsys was listed from 1992; the firm's own archived page gives 1994 as the "
                 "year and notes 'Acquired Logic Modeling for stock 3/94' and 'Acquired Everest Design for stock 10/98', "
                 "so NEA's Synopsys stock came from selling Logic Modeling (and Everest Design) to it. Logic Modeling is "
                 "the member; Synopsys leaves the base.", ec="site_listing", conf="high", cite=ARCH("synopsys")))
L.append(verdict("sunesis", "not_member",
                 "X1: Sunesis listed on Nasdaq in 2005; NEA's first position is the April 2009 private placement of "
                 "Series A preferred units into the listed company (8-K of 2009-04-01 naming NEA among the "
                 "participants), which the firm labels Public/PIPES. No earlier NEA private round is on record.",
                 ec="fund_filing", conf="high", cite=K8_SUNESIS))
L.append(verdict("supergen", "not_member",
                 "X1: SuperGen was listed on Nasdaq from 1996; the firm lists a 2008 first investment labelled "
                 "Public/PIPES, a purchase into the listed company. No earlier NEA private round is on record.",
                 ec="site_listing", conf="medium", cite=SITE("supergen")))

# ---- Spring Wireless / Spring Mobile Solutions (one company, CIK 1440096)
L.append(cls("spring-mobile-solutions", status="private", rng="below_1b", city="Reston",
             stage="Growth", stage_src="first_party", stage_cite=SITE("spring-mobile-solutions"), stage_conf="medium",
             entry_date="2008", focus="SaaS",
             note="Mobile enterprise application software (Spring Wireless renamed Spring Mobile Solutions; same "
                  "EDGAR CIK 1440096 as the spring-wireless row, which is the same company). The firm lists it "
                  "Private and Current with a 2008 first investment labelled Growth; the 2013 Form D date on file "
                  "is a follow-on (the company filed from 2009), so the entry year is the firm's 2008. Reston is "
                  "the address on the 2013-2021 Form Ds."))
L.append(cls("spring-wireless", status="private", rng="below_1b", country="US", city="Reston",
             stage="Growth", stage_src="first_party", stage_cite=SITE("spring-mobile-solutions"), stage_conf="medium",
             entry_date="2008", focus="SaaS", flags=["model_disputes_source"],
             note="Same company as spring-mobile-solutions (same EDGAR CIK 1440096; Spring Wireless renamed Spring "
                  "Mobile Solutions), so the two rows should merge. Classified as that row: the firm's own listing "
                  "reads Growth, first invested 2008. Country disputed: the 2009 Form D gave Sao Paulo, the "
                  "company's filings from 2013 give Reston, Virginia, the current head office."))

L.append(cls("springpath", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
             stage="undetermined", entry_date="2012", focus="Data Infrastructure",
             rounds=[rnd("2013", "Series B", None, "Redpoint Ventures", None, None, "firm"),
                     rnd("2017-08", "Acquisition by Cisco", 320000000, None, None,
                         NEWS("springpath", "Cisco acquires"), "press")],
             note="Hyperconverged storage software, Sunnyvale; Cisco bought it for $320M in 2017 (VCCircle). NEA "
                  "first invested in 2012, before Redpoint's 2013 Series B, but no source read names NEA's 2012 "
                  "round (the firm's label is Early), so the stage is undetermined."))

L.append(cls("sprout-social", city="Chicago", focus="SaaS",
             note="Social media management software, Chicago (the Form D address)."))

L.append(cls("spyglass-ophthalmics", rng="below_1b", usd=868730000, val_src="web_verified", val_cite=SA.format("sgp"),
             asof="2026-09-30", city="Aliso Viejo", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=S1_SPYGLASS, flags=["stage_disputes_band"], focus="Healthcare & Bio",
             rounds=[rnd("2019", "Seed", 700000, None, None, S1_SPYGLASS, "filing"),
                     rnd("2019-05-22", "Series A", 6000000, None, True, S1_SPYGLASS, "filing"),
                     rnd("2020-11", "Series B", 27500000, None, None, S1_SPYGLASS, "filing")],
             note="Same company as spyglass-pharma (EDGAR CIK 1778922; renamed SpyGlass Pharma, Nasdaq SGP since "
                  "the February 2026 IPO), so the two rows should merge. The S-1 lists a $0.7M seed, then $6.0M of "
                  "Series A preferred (valued May 2019), $27.5M Series B, C-1, C-2 and D; the $6.03M Form D of "
                  "2019-05-22 with Ali Behbahani as director is that Series A, so the Seed band is disputed. Market "
                  "cap $868.7M on 2026-09-30 (stockanalysis), 13% under the band edge."))
L.append(cls("spyglass-pharma", rng="below_1b", usd=868730000, val_src="web_verified", val_cite=SA.format("sgp"),
             asof="2026-09-30", city="Aliso Viejo", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=S1_SPYGLASS, entry_date="2019-05-22", focus="Healthcare & Bio",
             note="Same company as spyglass-ophthalmics (EDGAR CIK 1778922), classified alike: the S-1 names a "
                  "$6.0M Series A as the first priced round after a $0.7M seed, and the 2019-05-22 Form D with NEA's "
                  "Ali Behbahani as director is that round. Principal office Aliso Viejo (S-1). Market cap $868.7M "
                  "on 2026-09-30 (stockanalysis)."))

L.append(cls("stablix", status="private", rng="below_1b", country="US", city="New York",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=NEWS("stablix", "Stablix lands on stable"), entry_date="2021-06-03", focus="Healthcare & Bio",
             rounds=[rnd("2021-06-03", "Series A", 63000000, "Versant Ventures", True,
                         NEWS("stablix", "Stablix lands on stable"), "press")],
             note="Targeted protein stabilization biotech, New York. Launched with a $63M Series A led by Versant "
                  "and joined by NEA (Fierce Biotech, 2021-06-03); Vertex collaboration 2023, no later round found."))

L.append(cls("stash", status="acquired", rng="below_1b", city="New York", stage="Growth", stage_src="first_party",
             stage_cite=SITE("stash"), stage_conf="medium", entry_date="2022", focus="Fintech & Payments",
             flags=["model_disputes_source"],
             rounds=[rnd("2026-07-01", "Acquisition by Grab", 425000000, None, None,
                         NEWS("stash", "Grab completes US$425 million"), "press")],
             note="Investing app, New York. The pre-filled private status and $1.4B mark (the 2021 unicorn figure) "
                  "are disputed: Grab completed its $425M acquisition in July 2026 (Business Times), and the firm's "
                  "own exit line reads 'Acquired by: Grab'. Aligned with the Coatue and USV rows. Entry 2022 at "
                  "Growth on the firm's own label."))

L.append(cls("stitcher", status="acquired", rng="below_1b", city="San Francisco", stage="Growth", stage_src="model",
             stage_conf="medium", focus="Media, Gaming & Advertising", flags=["stage_disputes_band"],
             rounds=[rnd("2008", "Series A", 2700000, None, False, None, "press"),
                     rnd("2010-03-24", "Series B", 6000000, "Benchmark", False, None, "press"),
                     rnd("2011-08-16", "unnamed", 9999990, None, True, None, "filing")],
             note="Podcast app, San Francisco (Form D address); sold to Deezer in 2014, later Scripps and SiriusXM. "
                  "NEA entered on the $10.0M round of 2011-08-16 (Ravi Viswanathan director of record), which "
                  "followed the 2008 Series A and Benchmark's 2010 Series B (the Benchmark row's TechCrunch "
                  "citation), so NEA's entry was a third priced round: Growth, not the Series A band."))

L.append(cls("stormpath", status="acquired", rng="below_1b", country="US", city="San Mateo", stage="undetermined",
             entry_date="2012", focus="Security",
             rounds=[rnd("2017-03-06", "Acquisition by Okta", None, None, None, NEWS("stormpath", "Okta acquihires"),
                         "press")],
             note="User identity and authentication API, San Mateo. Okta bought the company in March 2017 and "
                  "retired the product (TechCrunch calls it an acqui-hire; Okta's announcement and the firm's exit "
                  "line call it an acquisition, read acquired). NEA invested in 2012 (the firm's own 2012 post); "
                  "no source read names that round."))

L.append(cls("streamsets", status="acquired", rng="below_1b", city="San Francisco", stage="Series A",
             stage_src="model", stage_conf="medium",
             stage_cite=POST("data-performance-management-unlocking"), entry_date="2015-09-23",
             focus="Data Infrastructure", flags=["stage_disputes_band"],
             note="Data pipeline software, San Francisco; bought by Software AG in 2022 (the firm's exit line; IBM "
                  "later bought it from Software AG). The Growth band rode the 2018 Form D, a follow-on: NEA's own "
                  "post of 2015-09-23 announces its investment that day, the Battery-led $12.5M Series A of "
                  "September 2015 (Battery's row cites its own case study for that round)."))

L.append(cls("stride-health", status="acquired", rng="below_1b", city="San Francisco", stage="Seed",
             stage_src="first_party", stage_cite=SITE("stride-health"), stage_conf="medium", entry_date="2014",
             grad="graduated", grad_src="web_verified", grad_cite=NEWS("stride-health", "Series B Funding"),
             grad_conf="high", focus="Fintech & Payments",
             rounds=[rnd("2017-08-22", "Series B", 23500000, None, None, NEWS("stride-health", "Series B Funding"),
                         "company"),
                     rnd("2026-07-08", "Acquisition by Integrity Marketing Group", None, None, None,
                         NEWS("stride-health", "Integrity acquires Allstate"), "press")],
             note="Health insurance recommendation and benefits platform for independent workers, San Francisco. "
                  "The firm labels its 2014 entry Seed; the company's $23.5M Series B of August 2017 (its own "
                  "release) is a later named round, so the seed graduated. Integrity bought it in July 2026 "
                  "(Coverager)."))

L.append(cls("strive-health", status="private", rng="below_1b", country="US", city="Denver", stage="undetermined",
             entry_date="2018", focus="Healthcare & Bio",
             rounds=[rnd("2021-03-16", "Series B", 140000000, "CapitalG and NEA", True,
                         POST("compassionate-kidney-care"), "firm"),
                     rnd("2023-05-31", "Series C", 166000000, "CVS Health Ventures", True,
                         NEWS("strive-health", "clinches $166M"), "press"),
                     rnd("2025-09-09", "Series D", 300000000, "NEA", True,
                         NEWS("strive-health", "Strive Health: $550 Million Raised"), "press")],
             note="Value-based kidney care, Denver; born in 2018 out of NEA's company-creation practice (the firm's "
                  "2021 post). The round NEA entered in 2018-19 is not named in any source read, so the stage is "
                  "undetermined. Mega-raise check 2026-09-30: the $550M of September 2025 ($300M Series D equity "
                  "led by NEA plus $250M debt) states no valuation (Pulse 2.0), so no $1B mark; aligned with "
                  "Redpoint's below_1b."))

L.append(cls("strongbridge-biopharma", country="US", city="Trevose", rng="below_1b", stage="undetermined",
             entry_date="2015", focus="Healthcare & Bio",
             note="Rare-disease biopharma (Cortendo AB redomiciled as Strongbridge Biopharma plc), principal "
                  "office Trevose, Pennsylvania (F-1); bought by Xeris in 2021. NEA came in through the private "
                  "placements from December 2014 while Cortendo's shares were quoted on the Norwegian OTC list, "
                  "before the October 2015 Nasdaq IPO; the firm labels it Public/PIPES and no round word is on "
                  "record. Whether an NOTC-quoted issuer counts as listed under X1 is left open."))

L.append(cls("subtext", status="acquired", rng="below_1b", country="US", city="Seattle", stage="Seed",
             stage_src="web_verified", stage_cite=TC_SUBTEXT, stage_conf="high", entry_date="2011-10-25",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2011-10-25", "Seed", 3000000, None, True, TC_SUBTEXT, "press")],
             note="Social e-book reading for classrooms, Seattle; bought by Renaissance Learning in 2013 (the firm's "
                  "exit line). TechCrunch (2011-10-25) names NEA among the investors in the $3M seed; the firm's "
                  "own label also reads Seed. Aligned with the GV row. " + GL))

L.append(cls("sugarcrm", status="acquired", rng="below_1b", city="Cupertino", stage="undetermined",
             entry_date="2005", focus="SaaS",
             rounds=[rnd("2018-08", "Majority investment by Accel-KKR", None, "Accel-KKR", None,
                         NEWS("sugarcrm", "Accel-KKR buys majority"), "press")],
             note="Open-source CRM software, Cupertino (Form D address). Accel-KKR took a majority stake in August "
                  "2018 (the firm's exit line: acquired by Accel-KKR). NEA first invested in 2005 after DFJ and "
                  "Walden's 2004 rounds, but no source read names NEA's round; the 2011 Form D date on file is a "
                  "later filing, so the entry year is the firm's 2005."))

L.append(cls("sun-edison", status="acquired", rng="below_1b", country="US", city="Beltsville", stage="Growth",
             stage_src="first_party", stage_cite=SITE("sun-edison"), stage_conf="medium", entry_date="2008",
             focus="Climate & Energy",
             note="Commercial solar developer and operator, Beltsville, Maryland; bought by MEMC Electronic "
                  "Materials in 2009 (the firm's exit line). Entry 2008 at Growth on the firm's own label."))

L.append(cls("sundeck", status="private", rng="below_1b", country="US", city="Santa Clara", stage="Seed",
             stage_src="web_verified", stage_cite=NW_SUNDECK, stage_conf="high", entry_date="2023-05-31",
             focus="Data Infrastructure",
             rounds=[rnd("2023-05-31", "Seed", 20000000, None, True, NW_SUNDECK, "company")],
             note="SQL query engineering for Snowflake, Santa Clara. The company's release of 2023-05-31 announces a "
                  "$20M seed from NEA, Coatue and Factory (the firm's year field reads 2022, the close). Momentum "
                  "check 2026-09-30 (Google News for the name): no later round and no $1B mark. Aligned with the "
                  "Coatue row. " + GL))

L.append(cls("suniva-inc", status="acquired", rng="below_1b", city="Norcross", stage="undetermined",
             entry_date="2007", focus="Climate & Energy", flags=["stage_disputes_band"],
             rounds=[rnd("2011-03-31", "unnamed", 115000000, None, True, None, "filing"),
                     rnd("2015-08-13", "Majority stake bought by Shunfeng", None, None, None,
                         NEWS("suniva-inc", "Shunfeng buys majority"), "press")],
             note="Silicon solar cell maker, Norcross, Georgia. Shunfeng International bought a majority stake in "
                  "2015 (Fortune); Chapter 11 followed in 2017, and the business now operates again (an $835M raise "
                  "and a signed, unclosed reverse merger with SUNation Energy in 2026). The Growth band rode the "
                  "2011 $115M Form D, but the firm's own listing gives 2007, the founding year, so 2011 was a "
                  "follow-on; NEA's 2007 round is not named in any source read."))

L.append(cls("super", status="private", rng="below_1b", country="ID", country_src="web_verified",
             country_cite=POST("super-serving-260m"), city="Surabaya", stage="Growth", stage_src="web_verified",
             stage_cite=NEWS("super", "Super gets $70M led by NEA"), stage_conf="high", entry_date="2022-06-01",
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             rounds=[rnd("2021-04-28", "Series B", 28000000, "SoftBank Ventures Asia", False,
                         NEWS("super", "raises $28M led by SoftBank"), "press"),
                     rnd("2022-06-01", "Series C", 70000000, "NEA", True,
                         NEWS("super", "Super gets $70M led by NEA"), "press")],
             note="Social commerce app for Indonesia's smaller cities, head office Surabaya (the firm's own 2022 "
                  "post). NEA led the $70M Series C (TechCrunch 2022-06-01; Forbes names the series). The pre-filled "
                  "US country and defunct status are disputed: the defunct status came through the YC row, which "
                  "carried it from the Lux and Spark rows for a different San Francisco company named Super; no "
                  "shutdown of this company was found, and the firm lists it Private and Current."))

L.append(cls("supernus-pharmaceuticals", country="US", city="Rockville", stage="Series A", stage_src="web_verified",
             stage_cite=S1_SUPERNUS, stage_conf="medium", entry_date="2005-12", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2005-12", "Series A", 45000000, None, True, S1_SUPERNUS, "filing")],
             note="Specialty CNS pharma, Rockville, Maryland. The S-1 (2010) says the company began operating in "
                  "December 2005 by buying Shire Laboratories' assets and raised about $45M of Series A preferred "
                  "in December 2005 and February 2006; NEA 11 is a party to its investor rights agreement and NEA's "
                  "Barrett and Newhall have sat on the board since 2005. The record names the round, so it replaces "
                  "the firm's Growth label."))

L.append(cls("supplybase", status="acquired", rng="below_1b", country="US", stage="undetermined", entry_date="1999",
             focus="SaaS", flags=["city_unknown"],
             note="Online supply-chain parts sourcing software; bought by i2 Technologies (the firm's exit line). "
                  "No source read places the company or names NEA's 1999 round."))

L.append(cls("surf-air", status="public", rng="below_1b", usd=148370000, val_src="web_verified",
             val_cite=SA.format("srfm"), asof="2026-09-30", city="Hawthorne", stage="Seed", stage_src="first_party",
             stage_cite=SITE("surf-air"), stage_conf="medium", entry_date="2012", focus="Consumer & Marketplaces",
             note="All-you-can-fly membership airline, now Surf Air Mobility (NYSE SRFM, listed July 2023), "
                  "Hawthorne, California. Market cap $148.4M on 2026-09-30 (stockanalysis). Entry 2012 at Seed on "
                  "the firm's own label. " + GL))

L.append(cls("surface-oncology", country="US", city="Cambridge", rng="below_1b", stage="Series A",
             stage_src="web_verified", stage_cite=S1_SURFACE, stage_conf="high", entry_date="2014-11",
             focus="Healthcare & Bio",
             rounds=[rnd("2014-11", "Series A", 35100000, None, True, S1_SURFACE, "filing"),
                     rnd("2016-01", "Series A-1", 13500000, None, None, S1_SURFACE, "filing")],
             note="Immuno-oncology antibodies, Cambridge MA; bought by Coherus in 2023. The S-1 shows NEA 14 holding "
                  "Series A preferred, sold in closings from November 2014 to January 2016, the company's first "
                  "round."))

L.append(cls("surgical-health", status="acquired", rng="below_1b", country="US", stage="undetermined",
             entry_date="1991", focus="Healthcare & Bio", flags=["city_unknown"],
             note="Ambulatory surgery centre operator; bought by HealthSouth in the 1990s (the firm's exit line). "
                  "No source read places the company or names NEA's 1991 round."))

L.append(cls("surgrx", status="acquired", rng="below_1b", country="US", city="Redwood City", stage="undetermined",
             entry_date="2005", focus="Healthcare & Bio",
             note="Vessel-sealing surgical devices, Redwood City; bought by Ethicon Endo-Surgery (Johnson & Johnson) "
                  "(the firm's archived exit line). No source read names NEA's 2005 round."))

L.append(cls("suvolta", status="acquired", rng="below_1b", city="Los Gatos", stage="undetermined",
             focus="Industrial & Robotics",
             rounds=[rnd("2009-12", "unnamed", 3000300, None, None, None, "filing"),
                     rnd("2010-04-22", "unnamed", 22174998, None, True, None, "filing"),
                     rnd("2012-01", "unnamed", 17592954, None, None, None, "filing"),
                     rnd("2014-01", "unnamed", 30334420, None, None, None, "filing")],
             note="Low-power CMOS transistor technology, Los Gatos (Form D address); Fujitsu took its process to "
                  "production in 2013 and the technology went to Mie Fujitsu Semiconductor in 2015, read as an "
                  "asset sale (acquired). NEA entered on the $22.2M round of 2010-04-22 (Forest Baskett director), "
                  "one filing after a $3.0M 2009 round; the round is not named, so the stage is undetermined."))

L.append(cls("swift-navigation", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2015", focus="Industrial & Robotics",
             rounds=[rnd("2017-07-13", "Series B", 34000000, None, None,
                         NEWS("swift-navigation", "$34 Million Series B"), "press"),
                     rnd("2025-07", "unnamed", 50000000, None, None, None, "press")],
             note="Precise GNSS positioning, San Francisco. NEA first invested in 2015 (Greg Papadopoulos on the "
                  "board); Felicis's own ladder shows a seed then a Series A, and the $34M Series B came in 2017, "
                  "but no source read says which round NEA entered. Aligned with the Felicis row on status, band "
                  "and city."))

L.append(cls("swiftype", city="San Francisco", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=POST("swiftype-making"), stage_conf="medium", entry_date="2013",
             grad="graduated", grad_src="first_party", grad_cite=POST("swiftype-making"), grad_conf="high",
             focus="DevTools & APIs", flags=["stage_disputes_band"],
             rounds=[rnd("2013-09-30", "Series A", 9244075, "NEA", True, POST("swiftype-making"), "firm")],
             note="Site search as a service, San Francisco; bought by Elastic in 2017. NEA's own post of 2013-09-30 "
                  "announces its Series A investment and says 'As an early seed investor', so NEA entered at the "
                  "seed and the Series A band is disputed; the Series A graduates the seed. The seed is not dated "
                  "in any source read, so the entry year is the firm's own 2013."))

L.append(cls("swirlds", status="private", rng="below_1b", country="US", city="Richardson", stage="Seed",
             stage_src="first_party", stage_cite=SITE("swirlds"), stage_conf="medium", entry_date="2016",
             focus="Crypto & Web3",
             note="Hashgraph distributed-ledger developer (Hedera's originator); sold the hashgraph IP to the Hedera "
                  "Council in 2022 and moved its teams to Swirlds Labs, and the firm still lists it Private. City "
                  "from the shared Hedera head office in Richardson, Texas (2019 move, Dallas Innovates). Entry 2016 "
                  "at Seed on the firm's own label. " + GL))

L.append(cls("switchon-networks", status="acquired", rng="below_1b", country="US", city="Milpitas",
             stage="undetermined", entry_date="1999", focus="Industrial & Robotics",
             note="Packet-classification chips and software, Milpitas; bought by PMC-Sierra in 2000 (the firm's exit "
                  "line). No source read names NEA's 1999 round."))

L.append(cls("syllable", status="private", rng="below_1b", country="US", city="Mountain View", stage="Seed",
             stage_src="first_party", stage_cite=SITE("syllable"), stage_conf="medium", entry_date="2017",
             grad="graduated", grad_src="web_verified",
             grad_cite=NEWS("syllable", "Syllable Raises $40 Million Series C"), grad_conf="high",
             focus="Healthcare & Bio",
             rounds=[rnd("2022-06-09", "Series C", 40000000, "TCV", None,
                         NEWS("syllable", "Syllable Raises $40 Million Series C"), "press")],
             note="Voice AI for health-system call centres, Mountain View. Entry 2017 at Seed on the firm's own "
                  "label; the $40M Series C led by TCV (2022) is a later named round, so the seed graduated. "
                  "Aligned with the TCV row."))

L.append(cls("synchr", status="acquired", rng="below_1b", city="Denver", focus="SaaS",
             rounds=[rnd("2021-04-30", "Acquisition by PrimePay", None, None, None,
                         NEWS("synchr", "PrimePay Announces Acquisition"), "press")],
             note="Cloud HR and payroll software for mid-market companies, Denver; PrimePay announced its "
                  "acquisition on 2021-04-30 (citybiz, datelined West Chester and Denver) and folded it into the "
                  "PrimePay brand in 2023."))

L.append(cls("synlogic", city="Cambridge", stage="Seed", stage_src="first_party", stage_cite=SITE("synlogic"),
             stage_conf="medium", entry_date="2014", grad="graduated", grad_src="web_verified", grad_cite=EX_SYNLOGIC,
             grad_conf="high", focus="Healthcare & Bio",
             rounds=[rnd("2017", "Series C", 42000000, None, True, EX_SYNLOGIC, "filing")],
             note="Synthetic-biology therapeutics, Cambridge MA; listed through the 2017 Mirna merger, ceased most "
                  "operations in 2024, and signed a reverse merger with Caldera in July 2026. Entry 2014 at Seed on "
                  "the firm's own label; the company's 2017 release (8-K exhibit) names a $42M Series C in which NEA "
                  "took part, a later named round, so the seed graduated."))

L.append(cls("synthesia", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified",
             val_cite=NEWS("synthesia", "Synthesia hits $4B valuation, lets"), asof="2026-01",
             country="GB", country_src="web_verified",
             country_cite=NEWS("synthesia", "Synthesia snaps up"), city="London", stage="Growth",
             stage_src="web_verified", stage_cite=NEWS("synthesia", "Synthesia snaps up"), stage_conf="high",
             entry_date="2025-01-14", focus="AI & Applied AI", flags=["model_disputes_source"],
             extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2025-01-14", "Series D", 180000000, "NEA", True, NEWS("synthesia", "Synthesia snaps up"),
                         "press"),
                     rnd("2026-01-26", "Series E", 200000000, "GV", None,
                         NEWS("synthesia", "Synthesia hits $4B valuation, lets"), "press")],
             note="AI video platform, London. The pre-filled acquired status and CZ country are a Wikidata join on a "
                  "Czech namesake and are disputed. NEA led the $180M Series D at $2.1B (TechCrunch 2025-01-14; the "
                  "firm's year field reads 2024, the close). Mark: the $200M Series E at $4B led by GV (TechCrunch "
                  "2026-01-26). Momentum check 2026-09-30: the Series E is the latest priced round found. Aligned "
                  "with the Accel and GV rows."))

L.append(cls("tableau-software", city="Seattle", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=S1_TABLEAU, stage_conf="medium", entry_date="2004-08", focus="Data Infrastructure",
             rounds=[rnd("2004-08", "Series A", None, None, True, S1_TABLEAU, "filing")],
             note="Visual analytics software, Seattle; listed 2013, bought by Salesforce in 2019. The S-1 shows one "
                  "preferred series, Series A, and NEA's Scott Sandell on the board since August 2004, the year the "
                  "firm gives; NEA 11 is the holder. The 2011 Form D date on file is a later filing, so the entry "
                  "is the 2004 Series A."))

L.append(cls("tagkast", status="private", rng="below_1b", country="US", stage="undetermined", entry_date="2011",
             focus="SaaS", flags=["city_unknown"],
             note="Photo marketing and augmented-reality platform for live events; its site is live and the firm "
                  "lists it Private. No press item, filing or page read places the company or names NEA's 2011 "
                  "round."))

L.append(cls("tagworks", status="private", rng="below_1b", country="NL", country_src="web_verified",
             country_cite=NEWS("tagworks", "Startup Tagworks raises"), city="Nijmegen", stage="Series A",
             stage_src="web_verified", stage_cite=NEWS("tagworks", "Startup Tagworks raises"), stage_conf="high",
             entry_date="2023-06-22", focus="Healthcare & Bio",
             rounds=[rnd("2023-06-22", "Series A", 65000000, None, True, NEWS("tagworks", "Startup Tagworks raises"),
                         "press")],
             note="Click-to-release cancer therapeutics, Nijmegen, Netherlands, with a Boston site (BioPharma Dive "
                  "2023-06-22, which names NEA in the $65M Series A syndicate with Novartis's venture arm and "
                  "Lightstone)."))

L.append(cls("tamara-mellon", status="private", rng="below_1b", city="Los Angeles", focus="Consumer & Marketplaces",
             rounds=[rnd("2019-06-18", "Series C", 50000000, None, None,
                         NEWS("tamara-mellon", "Raises $50M Series C"), "press")],
             note="Direct-to-consumer luxury footwear brand, Los Angeles (the 2016 Form D gave New York). NEA "
                  "funded it out of its 2015-16 Chapter 11 (WWD), then the 2017 round and the $50M Series C of 2019 "
                  "(Crunchbase News); still operating (licensing partnership 2023)."))

L.append(cls("tamr", status="private", rng="below_1b", city="Cambridge", stage="Seed", stage_src="first_party",
             stage_cite=SITE("tamr"), stage_conf="medium", entry_date="2013", grad="graduated",
             grad_src="web_verified", grad_cite=NEWS("tamr", "Series B1"), grad_conf="high",
             focus="Data Infrastructure",
             rounds=[rnd("2015-06", "Series B", 25200000, None, True, None, "company"),
                     rnd("2018-07-11", "Series B1", 18000000, None, None, NEWS("tamr", "Series B1"), "press")],
             note="Enterprise data mastering, Cambridge MA. Entry 2013 at Seed on the firm's own label; the company's "
                  "own releases (per the GV row) call NEA and GV founding investors and name a 2015 Series B, and "
                  "the $18M Series B1 of 2018 (Boston Business Journal) is a later named round, so the seed "
                  "graduated. The GV row reads the founding round as Series A (model)."))

L.append(cls("tarveda-therapeutics", status="private", rng="below_1b", city="Watertown", stage="undetermined",
             entry_date="2011", focus="Healthcare & Bio",
             rounds=[rnd("2017-02-03", "Series D", 30000000, None, None,
                         NEWS("tarveda-therapeutics", "Series D Financing"), "press"),
                     rnd("2026-02-02", "unnamed", 30000000, "Versant Ventures", None,
                         NEWS("tarveda-therapeutics", "rebooted Tarveda"), "press")],
             note="Miniaturized drug conjugates (Pentarins), Watertown MA, formerly Blend Therapeutics. A merger with "
                  "Organovo was blocked by shareholders in January 2026 and Versant backed a rebooted Tarveda with "
                  "$30M in February 2026 (Endpoints), so it operates. NEA first invested in 2011; that round is not "
                  "named in any source read."))

L.append(cls("teal", status="acquired", rng="below_1b", country="US", city="Salt Lake City", stage="Seed",
             stage_src="first_party", stage_cite=SITE("teal"), stage_conf="medium", entry_date="2015",
             focus="Industrial & Robotics",
             rounds=[rnd("2021-07-19", "Acquisition by Red Cat Holdings", None, None, None,
                         NEWS("teal", "Teal Drones Acquired by Red Cat"), "press")],
             note="Drone maker (now military small drones), Salt Lake City; Red Cat Holdings bought it in 2021 "
                  "(Dronelife). Entry 2015 at Seed on the firm's own label. " + GL))

jl.write("c10a", L)
