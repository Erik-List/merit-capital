"""PRO-100 NEA, judge c5, queue batch 9 (gaikai .. guardent): listed members, classification only.
Run: NQ_TAG=c5 python3 judgments-c5a.py"""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, W, FTS, NEWS, FORMD_CITE

GLU_S1 = "https://www.sec.gov/Archives/edgar/data/1366246/000089161806000520/f25683orsv1.htm"  # printed by FTS listing
L = []

# ---- X1 / R2: NEA's first position was a public purchase into an already listed company
L.append(verdict("geron", "not_member",
                 "X1/R2: NEA first bought Geron in 2020 through its Growth Equity Opportunities vehicle (13D of 2020-06-04), "
                 "a company listed since 1996; the firm labels it Growth 2020 and no earlier NEA private round is on record.",
                 ec="fund_filing", conf="medium",
                 cite="https://www.sec.gov/Archives/edgar/data/886744/000107261320000201/0001072613-20-000201-index.htm"))
L.append(verdict("gossamer-bio", "not_member",
                 "X1/R2: NEA's first position is the July 2022 private placement into Gossamer Bio (listed since its 2019 IPO), "
                 "bought by Growth Equity Opportunities 18 VGE; the firm's own label is Public/PIPES 2022 and no earlier NEA "
                 "private round is on record.",
                 ec="fund_filing", conf="medium", cite=FTS("Gossamer", "8-K")))
L.append(verdict("genocea", "not_member",
                 "X1: NEA first bought Genocea in the January 2018 public offering (the 424B5 names NEA as the investor that "
                 "gets a board seat), four years after the 2014 IPO; the firm's year is 2018 and no earlier NEA private round "
                 "is on record, so the later Form D placements are PIPEs into a listed company.",
                 ec="fund_filing", conf="medium", cite=FTS("GENOCEA", "424B5")))

# ---- classification lines
L.append(cls("gaikai", rng="below_1b", stage="undetermined", entry_date="2011", city="Aliso Viejo",
             focus="Media, Gaming & Advertising", rounds=[],
             note="Sony acquired Gaikai in 2012 (the firm's exit line and its own 2012 post). NEA first invested in 2011 "
                  "(label Early, an anchor only); no source on disk names the round NEA joined, so the stage stays undetermined."))

L.append(cls("gainspeed", status="acquired", rng="below_1b", stage="undetermined", entry_date="2012", city="Sunnyvale",
             focus="Data Infrastructure",
             rounds=[rnd("2012-09-13", "unnamed (Form D)", 23272000, source=FORMD_CITE("gainspeed", 0), source_type="filing"),
                     rnd("2013-10-21", "unnamed (Form D)", 10000000, source=FORMD_CITE("gainspeed", 1), source_type="filing"),
                     rnd("2014-12-23", "unnamed (Form D)", 27499996, firm_in_round=True,
                         source=FORMD_CITE("gainspeed", 2), source_type="filing")],
             note="Nokia acquired Gainspeed in 2016 (the firm's exit line). NEA's first-invested year 2012 matches the "
                  "company's first Form D round ($23.3M sold, September 2012); no source names that round, so the stage "
                  "stays undetermined."))

L.append(cls("galera-therapeutics", city="Malvern", focus="Healthcare & Bio",
             note="Malvern, Pennsylvania: the Form D address and EDGAR's business address agree."))

L.append(cls("geltex-pharmaceuticals", status="acquired", rng="below_1b", stage="undetermined", entry_date="1993",
             country="US", city="Waltham", focus="Healthcare & Bio", rounds=[],
             note="Genzyme acquired GelTex in 2000 (the firm's exit line names Genzyme); EDGAR's business address is Waltham, "
                  "MA. The round NEA entered in 1993 is not named in the record."))

L.append(cls("gen-g", status="private", rng="below_1b", stage="undetermined", entry_date="2019", country="US",
             city="Los Angeles", focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
             rounds=[rnd("2019-04-17", "unnamed", 46000000, source_type="press")],
             note="Gen.G raised $46M in April 2019 (ESPN, Hollywood Reporter), the year of NEA's first investment, but no "
                  "headline names the round, so the stage stays undetermined. The prefilled KR is the Seoul team base: "
                  "Wikipedia lists headquarters in Santa Monica, Seoul and Shanghai and the Battery book places it in Los "
                  "Angeles, US; this row aligns with Battery."))

L.append(cls("genetic-therapy-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="1991",
             country="US", city="Gaithersburg", focus="Healthcare & Bio", rounds=[],
             note="Sandoz acquired Genetic Therapy in 1995 (the firm's exit line). The round NEA entered in 1991 is not named."))

L.append(cls("genies", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
             val_cite=NEWS("genies", "hits $1 billion valuation"), asof="2022-04-12", stage="undetermined",
             entry_date="2014", city="Los Angeles", focus="Media, Gaming & Advertising", flags=["stale"],
             rounds=[rnd("2014-01-30", "unnamed (Form D)", 2400000, source_type="filing"),
                     rnd("2015-04-23", "unnamed (Form D)", 6341383, source_type="filing"),
                     rnd("2021-04-16", "unnamed (Form D)", 64548862, firm_in_round=True, source_type="filing"),
                     rnd("2022-04-12", "Series C", 150000000, lead="Silver Lake",
                         source=NEWS("genies", "hits $1 billion valuation"), source_type="press")],
             note="Series C of $150M led by Silver Lake at a $1B valuation, April 2022 (TechCrunch, PR Newswire); older "
                  "than 24 months, so stale. NEA's first-invested year 2014 predates the Genies name (the Form D issuer "
                  "files from 2012); the round NEA entered is not named, so the stage stays undetermined."))

L.append(cls("genmo", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
             stage_cite=POST("genmos-open"), stage_conf="medium", entry_date="2023", country="US", city="San Francisco",
             focus="AI & Applied AI",
             rounds=[rnd("2024-10-22", "Series A", 30000000, lead="NEA", firm_in_round=True,
                         source=POST("genmos-open"), source_type="firm")],
             note="NEA's own post of 2024-10-22 says Genmo announced a $30M Series A led by NEA; the firm's listing gives "
                  "2023 as its first-invested year, read as the round's close year, and no firm post shows an earlier "
                  "round. Momentum check 2026-09-30 (Google News for Genmo): no $1B+ priced round."))

L.append(cls("geotel-corporation", status="acquired", rng="below_1b", stage="undetermined", entry_date="1994",
             country="US", city="Littleton", focus="SaaS", rounds=[],
             note="Cisco acquired GeoTel Communications in 1999 (the firm's exit line); EDGAR's last business address is "
                  "Littleton, MA. The round NEA entered in 1994 is not named."))

L.append(cls("gilt-groupe", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("gilt-groupe"), stage_conf="medium", entry_date="2011", city="New York",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2009", "Series C", None, lead="General Atlantic", source=W("Gilt Groupe"), source_type="press"),
                     rnd("2011", "unnamed", 138000000, source=W("Gilt Groupe"), source_type="press")],
             note="Hudson's Bay bought Gilt in 2016 (the firm's exit line) for well under its reported $1B 2011 mark. Stage "
                  "from the firm's own label Growth: NEA's 2011 entry follows the 2009 Series C, and the 2011 raise was "
                  "$138M (Wikipedia)."))

L.append(cls("glacier", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=POST("glacier-qa"), stage_conf="high", entry_date="2022-04", country="US", city="San Francisco",
             focus="Industrial & Robotics", grad="graduated", grad_src="first_party", grad_cite=POST("glacier-qa"),
             grad_conf="high",
             rounds=[rnd("2022-04-19", "Seed", 4500000, lead="NEA", firm_in_round=True, source=POST("glacier-qa"),
                         source_type="firm"),
                     rnd("2024-03-06", "unnamed", 7700000, firm_in_round=True, source_type="press"),
                     rnd("2025-04-28", "Series A", 16000000, firm_in_round=True, source=POST("glacier-qa"),
                         source_type="firm")],
             note="NEA's own 2025 post says NEA led Glacier's Seed round in 2022 (the $4.5M round TechCrunch reported on "
                  "2022-04-19) and participated in the Series A ($16M, April 2025), which graduates the row. The prefilled "
                  "2009 entry date comes from a Form D of a different company named Glacier (CIK 1470797) and is replaced."))

L.append(cls("globallogic", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("globallogic"), stage_conf="medium", entry_date="2006", city="San Jose", focus="SaaS",
             note="Apax bought GlobalLogic in 2013 (the firm's exit line) and Hitachi bought it in 2021 (Wikipedia). "
                  "Stage from the firm's own label Growth; city aligned with the Sequoia book."))

L.append(cls("glu-mobile", rng="below_1b", focus="Media, Gaming & Advertising", stage="Series A", stage_src="web_verified",
             stage_cite=FTS("GLU MOBILE", "S-1"), stage_conf="medium", entry_date="2001-12", city="San Francisco",
             rounds=[rnd("2001-12", "Series A", 4275000, firm_in_round=True, source=GLU_S1, source_type="filing"),
                     rnd("2003-04", "Series B", None, source=GLU_S1, source_type="filing")],
             note="Glu (Sorrent until 2005) issued its Series A in December 2001 (S-1 note 10); NEA's Alsop joined the "
                  "board that month and the voting agreement gives NEA 10 a Series A director seat. The 2010 Form D is a "
                  "later round, not the entry. Electronic Arts bought Glu in 2021; EDGAR's last address is San Francisco."))

L.append(cls("glycomimetics", status="acquired", rng="below_1b", stage="undetermined", entry_date="2003", country="US",
             city="Rockville", focus="Healthcare & Bio", flags=["model_disputes_source"], rounds=[],
             note="GlycoMimetics merged with Crescent Biopharma in a 2025 reverse merger; EDGAR now carries the registrant "
                  "(CIK 1253689) as Crescent Biopharma, Waltham, so the GlycoMimetics business reads acquired (the Battery "
                  "book's reading of Imara) and the prefilled public float is disputed. NEA 10 held common and preferred "
                  "at the 2013 S-1 after a 2009 Series A-1 recap; the 2003 round NEA entered is not named."))

L.append(cls("goeuro", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
             stage_cite=POST("goeuro"), stage_conf="high", city="Berlin", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-08-13", "Series A", 27403198, firm_in_round=True, source=POST("goeuro"), source_type="firm"),
                     rnd("2018", "Series C", 150000000, source=W("Omio"), source_type="press"),
                     rnd("2022", "Series E", 80000000, source=W("Omio"), source_type="press")],
             note="NEA's own post of 2014-08-27 announces 'our Series A investment in GoEuro' (Form D of 2014-08-13, "
                  "$27.4M). GoEuro renamed itself Omio in 2019 (Wikipedia); the base also carries the live omio row for the "
                  "same company. No priced round at $1B is on record."))

L.append(cls("golden-analytics", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_cite=NEWS("golden-analytics", "Debuts with $7M Seed Funding"), stage_conf="high",
             entry_date="2026-04", grad="censored", country="US", city="Bellevue", focus="Data Infrastructure",
             rounds=[rnd("2026-04-07", "Seed", 7000000, lead="NEA, Madrona", firm_in_round=True,
                         source=NEWS("golden-analytics", "Debuts with $7M Seed Funding"), source_type="press"),
                     rnd("2026-06-09", "Seed extension", 14000000, source_type="press")],
             note="Debuted with a $7M seed from NEA and Madrona on 2026-04-07 (PR Newswire), then a $14M seed extension in "
                  "June 2026; entry inside the 24-month window, so censored. Momentum check 2026-09-30 (Google News): no "
                  "$1B+ priced round. City aligned with the Insight book."))

L.append(cls("golden-state-medical-supply", status="acquired", rng="below_1b", stage="undetermined", entry_date="2015",
             country="US", city="Camarillo", focus="Healthcare & Bio", rounds=[],
             note="Court Square Capital Partners acquired GSMS (the firm's exit line). NEA's 2015 investment into a company "
                  "founded in the 1990s is not named in the record."))

L.append(cls("good-technology", rng="below_1b", stage="undetermined", entry_date="1998", city="Sunnyvale",
             focus="Security", rounds=[],
             note="BlackBerry bought Good in 2015 for about $425M. Good is Visto (founded 1996), which took the name after "
                  "buying the original Good Technology in 2009 (Wikipedia), so NEA's 1998 entry is into Visto; the 2013 "
                  "DRS holder list names NEA Presidents Fund and NEA Ventures 1998. The round is not named."))

L.append(cls("goodguide", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("goodguide"), stage_conf="medium", entry_date="2007", city="San Francisco",
             city_src="formd_address", focus="Consumer & Marketplaces",
             rounds=[rnd("2011-04-30", "unnamed (Form D)", 4999998, firm_in_round=True,
                         source=FORMD_CITE("goodguide", 0), source_type="filing")],
             note="UL acquired GoodGuide (the firm's exit line). Stage from the firm's own label Seed with first-invested "
                  "year 2007; the 2011 Form D ($5.0M) is a later round, not the entry, and the prefilled 2011 date is "
                  "replaced. Graduation left for the graduation pass."))

L.append(cls("goodleap", stage="Growth", stage_src="first_party", stage_cite=SITE("goodleap"), stage_conf="medium",
             entry_date="2019", city="Roseville", focus="Fintech & Payments",
             rounds=[rnd("2021-01", "unnamed", 800000000, lead="NEA, West Cap Group, Brookfield, Riverstone",
                         firm_in_round=True, source=W("GoodLeap"), source_type="press")],
             note="Stage from the firm's own label Growth (Loanpal, founded 2003, was a scaled lender by 2019); NEA co-led "
                  "the $800M January 2021 round (Wikipedia). City aligned with the Ribbit book."))

L.append(cls("goop", status="private", rng="below_1b", stage="undetermined", entry_date="2015", city="Santa Monica",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2016", "Series B", 15000000, firm_in_round=True, source=W("Goop (company)"), source_type="press"),
                     rnd("2018-03", "Series C", 50000000, firm_in_round=True, source=W("Goop (company)"),
                         source_type="press")],
             note="Wikipedia names NEA in the $15M 2016 Series B and the $50M 2018 Series C (valued at $250M), but the "
                  "firm's first-invested year is 2015, earlier than the Series B, so the entry round is not established "
                  "and the stage stays undetermined."))

L.append(cls("goqii", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=W("GOQii"), stage_conf="high", city="Menlo Park", city_src="formd_address",
             focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2015-11", "Series A", 13400000, lead="NEA, Cheetah Mobile", firm_in_round=True,
                         source=W("GOQii"), source_type="press"),
                     rnd("2018-11", "Series B", None, lead="Mitsui", source_type="press"),
                     rnd("2020", "Series C", 10000000, lead="Animoca Brands", source=W("GOQii"), source_type="press")],
             note="GOQii's $13.4M Series A was led by NEA and Cheetah Mobile (Wikipedia; YourStory 2015-11-26); the "
                  "October 2015 Form D closes are that round, so the seed band is disputed. Wikipedia gives the "
                  "headquarters in California; the Form D address is Menlo Park."))

L.append(cls("grand-junction", status="acquired", rng="below_1b", stage="undetermined", entry_date="1993", country="US",
             city="Fremont", focus="Data Infrastructure", flags=["model_disputes_source"], rounds=[],
             note="Cisco bought Grand Junction Networks in 1995 (the firm's exit line). The prefilled GB is a wrong name "
                  "join; the company was in Fremont, California, as in the Sutter Hill book."))

L.append(cls("granica", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("granica"), stage_conf="medium", entry_date="2020", country="US", city="Mountain View",
             city_src="web_verified", focus="Data Infrastructure",
             rounds=[rnd("2023-06-12", "unnamed", 45000000, lead="NEA, Bain Capital Ventures", firm_in_round=True,
                         source=NEWS("granica", "Bain Capital Ventures Leads"), source_type="press")],
             note="Stage from the firm's own label Seed, first invested 2020. Granica emerged in June 2023 with $45M led by "
                  "NEA and Bain Capital Ventures (citybiz, which places it in Mountain View); the round is not named. "
                  "Google News check 2026-09-30: no $1B+ round. Graduation left for the graduation pass."))

L.append(cls("graphite-systems", rng="below_1b", focus="Data Infrastructure", city="Menlo Park", city_src="formd_address",
             note="EMC acquired Graphite Systems (the firm's exit line). City from the Form D address. Graduation left for "
                  "the graduation pass (the Form D layer shows a $10.4M round in December 2012 after the $2.0M entry)."))

L.append(cls("gravel", status="private", rng="below_1b", country="ID", country_src="web_verified",
             country_cite=SITE("gravel"), city="Jakarta", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             rounds=[rnd("2021-04-12", "unnamed (Form D)", 5000000, firm_in_round=True,
                         source=FORMD_CITE("gravel", 0), source_type="filing"),
                     rnd("2023-12-03", "unnamed", 14000000, lead="NEA", firm_in_round=True, source_type="press")],
             note="The firm's own page places Gravel in Jakarta, Indonesia; the prefilled US is the Form D filer's San "
                  "Francisco address. NEA's Carmen Chang is a director on the April 2021 Form D; in December 2023 Gravel "
                  "raised $14M with NEA (TechCrunch, Jakarta Post). Graduation left for the graduation pass."))

L.append(cls("green-chef", status="acquired", rng="below_1b", focus="Consumer & Marketplaces", city="Denver", city_src="formd_address",
             note="HelloFresh acquired Green Chef in 2018 (the firm's exit line)."))

L.append(cls("greenlight", status="private", rng="1b_plus", usd=2300000000, val_src="web_verified",
             val_cite=NEWS("greenlight", "hits $2.3bn valuation"), asof="2021-04-27", stage="Seed",
             stage_src="first_party", stage_cite=SITE("greenlight"), stage_conf="medium", entry_date="2017",
             grad="graduated", grad_src="web_verified", grad_cite=NEWS("greenlight", "Closes $260M Series D"),
             grad_conf="high", country="US", city="Atlanta", focus="Fintech & Payments",
             flags=["stale", "model_disputes_source"],
             rounds=[rnd("2021-04-27", "Series D", 260000000, lead="Andreessen Horowitz",
                         source=NEWS("greenlight", "Closes $260M Series D"), source_type="press")],
             note="Stage from the firm's own label Seed (first invested 2017; the archive's 2007 is a typo for a company "
                  "founded in 2014). The $260M Series D at $2.3B (April 2021) graduates the row and is the last priced "
                  "mark, stale past 24 months; aligned with the a16z book. The prefilled SK is a wrong name join: "
                  "Greenlight is in Atlanta."))

L.append(cls("gridpoint", status="acquired", rng="below_1b", focus="Climate & Energy", city="Reston",
             note="Twenty First Century Utilities acquired GridPoint (the firm's exit line); the business continues, based "
                  "in Reston, Virginia (Wikipedia)."))

L.append(cls("groupon", city="Chicago", focus="Consumer & Marketplaces", note="Chicago, as in the Form D address and every sibling book."))

L.append(cls("growth-networks", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998",
             country="US", city="Mountain View", focus="Data Infrastructure", rounds=[],
             note="Cisco acquired Growth Networks in 2000 (the firm's exit line); city aligned with the Lightspeed book. The "
                  "round NEA entered in 1998 is not named."))

L.append(cls("guardent", status="acquired", rng="below_1b", stage="undetermined", entry_date="2000", country="US",
             city="Waltham", focus="Security", rounds=[],
             note="VeriSign acquired Guardent in 2003 (the firm's exit line); city aligned with the Sequoia book. The round "
                  "NEA entered in 2000 is not named."))

L.append(cls("glamsquad", status="private", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_cite=NEWS("glamsquad", "$15 Million Series B Funding Led by"),
             stage_conf="high", flags=["stage_disputes_band"],
             rounds=[rnd("2014-10-21", "Series A", 8850000, source=FORMD_CITE("glamsquad", 0), source_type="filing"),
                     rnd("2015-10-09", "Series B", 15000000, lead="NEA", firm_in_round=True,
                         source=NEWS("glamsquad", "$15 Million Series B Funding Led by"), source_type="press"),
                     rnd("2023-01", "minority investment", None, lead="Boathouse Capital", source_type="press")],
             note="NEA led Glamsquad's $15M Series B (PR Newswire, 2015-10-09; the Form D of 2015-07-23), after the 2014 "
                  "round, so the Series A band is disputed. Still operating in 2025-26 after a 2023 minority investment "
                  "from Boathouse Capital."))

GUSHENG_A = "https://news.qq.com/rain/a/20210628A0208400"  # read with WebFetch 2026-09-30
GUSHENG_CAP = "https://stockanalysis.com/quote/hkg/2273/market-cap/"  # read with WebFetch 2026-09-30
GOODY_A = NEWS("goody", "Goody raises $15M led by SoftBank")  # read with WebFetch 2026-09-30
GREYTHR_SITE = "https://www.greythr.com/company/about-us/"  # read with WebFetch 2026-09-30

L.append(cls("geistm", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("geistm"), stage_conf="medium", entry_date="2011", country="US", city="New York",
             focus="SaaS", rounds=[],
             note="Stage from the firm's own label Seed, first invested 2011. GeistM is a New York martech company (Crain's "
                  "New York Fast 50, 2019) still operating. Graduation left for the graduation pass."))

L.append(cls("greythr", status="acquired", rng="below_1b", stage="undetermined", entry_date="2016", country="IN",
             country_src="web_verified", country_cite=GREYTHR_SITE, city="Bangalore", focus="SaaS",
             rounds=[rnd("2024-08", "majority stake (52.1%)", None, lead="Apax Partners",
                         source=NEWS("greythr", "acquires 52.1% stake"), source_type="press")],
             note="An Apax Partners fund bought a 52.1% controlling stake in greytHR in August 2024 (YourStory), read as "
                  "acquired. The company's own page gives its Bengaluru (Koramangala) address. The round NEA entered in "
                  "2016 is not named."))

L.append(cls("goji-solutions", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("goji-solutions"), stage_conf="medium", entry_date="2011", country="IL",
             country_src="web_verified", country_cite=NEWS("goji-solutions", "Israeli Startup Goji"),
             focus="Industrial & Robotics", flags=["city_unknown"], rounds=[],
             note="Stage from the firm's own label Growth, first invested 2011. IEEE Spectrum (2017) calls Goji an Israeli "
                  "startup and visited its R&D subsidiary in Israel without naming a city; the firm still lists it Private."))

L.append(cls("goody", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=GOODY_A, stage_conf="medium", entry_date="2021", country="US", city="Miami",
             city_src="web_verified", focus="Consumer & Marketplaces",
             rounds=[rnd("2020", "Seed", 4000000, lead="Index Ventures", source=GOODY_A, source_type="press"),
                     rnd("2021", "Series A", 13100000, firm_in_round=True, source=GOODY_A, source_type="press"),
                     rnd("2021-11-16", "unnamed", 15000000, lead="SoftBank Latin America Fund", source=GOODY_A,
                         source_type="press")],
             note="Refresh Miami (2021-11-16) says the Miami-based Goody raised 'a $13.1 million Series A earlier this year "
                  "with NEA' after a $4M seed with Index, matching the firm's first-invested year 2021."))

L.append(cls("grubwithus", status="defunct", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("grubwithus"), stage_conf="medium", entry_date="2011", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", rounds=[],
             note="TechCrunch (2016-08-29) calls GrubWithUs 'now shuttered'; its founders pivoted to GOAT, which the firm's "
                  "listing now links, but no source shows NEA's GrubWithUs stock carried into GOAT, so the row stays "
                  "defunct, aligned with the a16z and First Round books. Stage from the firm's own label Seed. "
                  "Graduation left for the graduation pass."))

L.append(cls("gst-clinics", status="public", rng="below_1b", usd=746800000, val_src="web_verified",
             val_cite=GUSHENG_CAP, asof="2026-09-30", stage="Series A", stage_src="web_verified", stage_cite=GUSHENG_A,
             stage_conf="high", entry_date="2014-01", country="CN", country_src="web_verified",
             country_cite=SITE("gst-clinics"), city="Guangzhou", focus="Healthcare & Bio",
             rounds=[rnd("2014-01", "Series A", None, lead="NEA", firm_in_round=True, source=GUSHENG_A, source_type="press"),
                     rnd("2015-04", "Series B", 25000000, lead="NEA, Eight Roads", firm_in_round=True,
                         source=GUSHENG_A, source_type="press"),
                     rnd("2021-03", "Series E", 37700000, firm_in_round=True, source_type="press")],
             note="GST Clinics is Gushengtang, the Guangdong TCM clinic chain: NEA led its multi-million-dollar Series A in "
                  "January 2014 and the $25M Series B in April 2015 (Tencent News). Listed in Hong Kong in December 2021 "
                  "(HKG:2273): HKD 5.86B @ ECB 2026-09-30 (HKD/EUR 8.9095, EUR/USD 1.1355) = $746.8M."))

L.append(cls("grid", status="private", rng="below_1b", stage="Series A", stage_src="first_party", stage_cite=POST("grid"),
             stage_conf="high", entry_date="2020-08", country="IS", country_src="web_verified",
             country_cite=POST("grid"), city="Reykjavik", focus="SaaS", flags=["model_disputes_source"],
             rounds=[rnd("2020-08-26", "Series A", 12000000, lead="NEA", firm_in_round=True, source=POST("grid"),
                         source_type="firm")],
             note="NEA's own post (2020-08-26) says 'We are thrilled to lead GRID's Series A' and calls GRID a Reykjavik, "
                  "Iceland-based company ($12M, TechTarget). The prefilled CZ is a wrong name join, and the YC book's Grid "
                  "row (San Francisco) is a different company with the same name."))

L.append(cls("grey-rhino", status="private", rng="below_1b", stage="undetermined", entry_date="2017", country="US",
             city="Palo Alto", city_src="formd_address", focus="AI & Applied AI", rounds=[],
             note="Grey Rhino carries One Concern's exact description, first-invested year 2017 and NEA board member (Scott "
                  "Sandell): read as One Concern under a new name, which the base also carries as the archived one-concern "
                  "row (Palo Alto Form D). No source on disk names the round NEA entered."))

L.append(cls("gladly", status="private", rng="below_1b", stage="undetermined", entry_date="2016", country="US",
             city="San Francisco", focus="SaaS",
             rounds=[rnd("2024-09-26", "unnamed", 40000000, lead="AXA Venture Partners",
                         source=NEWS("gladly", "Gladly secures $40M"), source_type="press")],
             note="NEA announced its investment in Gladly on 2016-06-21 without naming the round, and the Greylock and "
                  "Point Nine books place earlier rounds (seed, Series A) before it; no source names NEA's round. Gladly "
                  "raised $40M led by AXA Venture Partners in September 2024 (PR Newswire, San Francisco dateline); no $1B "
                  "mark is on record. City aligned with the sibling books."))
jl.write("c5a", L)
