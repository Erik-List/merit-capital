"""PRO-100 NEA, judge c5, queue batch 10 (guideline .. innerworkings): listed members, classification only.
Run: NQ_TAG=c5 python3 judgments-c5b.py"""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, W, FTS, NEWS, FORMD_CITE

HEMO_PR = "https://www.sec.gov/Archives/edgar/data/1127393/000119312506252706/dex991.htm"  # printed by the FTS listing
INHIB_S1 = FTS("INHIBITEX", "S-1")
HYGEIA_CAP = "https://stockanalysis.com/quote/hkg/6078/market-cap/"  # read with WebFetch 2026-09-30
L = []

# ---- X1: NEA's first position was a private placement into an already listed company
L.append(verdict("hemosense", "not_member",
                 "X1: NEA's first position is the December 2006 private placement (about $7.0M of common stock from a "
                 "single institutional investor, NEA 12) into HemoSense, listed on AMEX since 2005; the firm's own label "
                 "is Public/PIPES 2006 and no earlier NEA private round is on record.",
                 ec="fund_filing", conf="medium", cite=HEMO_PR))
L.append(verdict("immunex-corporation", "not_member",
                 "X1: the firm's own listing labels Immunex Public/PIPES with a 1992 first investment, nine years after "
                 "Immunex's 1983 IPO; no earlier NEA private round is on record.",
                 ec="site_listing", conf="medium", cite=SITE("immunex-corporation")))
L.append(verdict("immunomedics", "not_member",
                 "X1: NEA's position was bought in 2017 through Growth Equity Opportunities Fund IV (the 2017 S-3 names it "
                 "a selling stockholder) in Immunomedics, listed since the 1980s; the firm's own label is Public/PIPES 2017 "
                 "and no earlier NEA private round is on record.",
                 ec="fund_filing", conf="medium", cite=FTS("IMMUNOMEDICS", "S-3")))
L.append(verdict("infinity-pharmaceuticals", "not_member",
                 "X1: the firm's own listing labels Infinity Public/PIPES with a 2009 first investment; Infinity was listed "
                 "from its 2006 merger with Discovery Partners, and no earlier NEA private round is on record.",
                 ec="site_listing", conf="medium", cite=SITE("infinity-pharmaceuticals")))

# ---- classification lines
L.append(cls("gynecare", status="acquired", rng="below_1b", stage="undetermined", entry_date="1994", country="US",
             city="Menlo Park", focus="Healthcare & Bio", rounds=[],
             note="Johnson & Johnson acquired Gynecare after its IPO (the firm's exit line); EDGAR files Gynecare Inc. "
                  "(CIK 1002243) at Menlo Park, CA. The round NEA entered in 1994 is not named."))

L.append(cls("healthsouth", country="US", city="Birmingham", stage="undetermined", focus="Healthcare & Bio", rounds=[],
             note="HealthSouth is now Encompass Health (EDGAR, Birmingham, AL). The firm's year 1995 postdates the 1986 IPO, "
                  "while NEA co-founder Charles Newhall sat on the board from the 1980s; the round NEA entered is not named, "
                  "so no entry date is set."))

L.append(cls("heavy-ai", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=W("HEAVY.AI"), stage_conf="high", city="San Francisco", focus="Data Infrastructure",
             rounds=[rnd("2016", "Series A", 10000000, source=W("HEAVY.AI"), source_type="press"),
                     rnd("2017-03-16", "Series B", 25000000, lead="NEA, Nvidia, Verizon", firm_in_round=True,
                         source=W("HEAVY.AI"), source_type="press"),
                     rnd("2018-10", "Series C", 55000000, lead="Tiger Global", firm_in_round=True, source=W("HEAVY.AI"),
                         source_type="press")],
             note="NEA co-led the $25M Series B in 2017 (Wikipedia; the Form D of 2017-03-16), after the 2016 Series A, so "
                  "the entry is Growth. Nvidia acquired HEAVY.AI (formerly MapD, OmniSci) in 2025."))

L.append(cls("heliovolt-corporation", status="defunct", rng="below_1b", city="Austin", stage="Series A",
             stage_src="web_verified", stage_cite=W("HelioVolt"), stage_conf="high", entry_date="2005",
             flags=["stage_disputes_band"],
             rounds=[rnd("2005", "Series A", 8000000, lead="NEA", firm_in_round=True, source=W("HelioVolt"),
                         source_type="press"),
                     rnd("2007-08", "Series B", 101000000, lead="Paladin Capital Group, Masdar Clean Tech Fund",
                         source=W("HelioVolt"), source_type="press")],
             note="HelioVolt suspended operations in 2014 (Wikipedia). NEA put in the $8M Series A in 2005 (Wikipedia), "
                  "so the Growth band read off the 2009 Form D is disputed."))

L.append(cls("hillcrest-laboratories", status="acquired", rng="below_1b", stage="undetermined", entry_date="2003",
             city="Rockville", focus="Industrial & Robotics",
             rounds=[rnd("2011-03-29", "unnamed (Form D)", 5542562, source=FORMD_CITE("hillcrest-laboratories", 0),
                         source_type="filing")],
             note="InterDigital bought Hillcrest in 2016 and sold it to CEVA in 2019 (the firm's exit line names CEVA). "
                  "NEA first invested in 2003; the 2011 Form D is a later round, so the prefilled 2011 date is replaced and "
                  "the entry round is not named."))

L.append(cls("hygeia-medical-services-group", status="public", rng="below_1b", usd=753200000, val_src="web_verified",
             val_cite=HYGEIA_CAP, asof="2026-09-30", val_conf="medium", stage="Growth", stage_src="first_party",
             stage_cite=SITE("hygeia-medical-services-group"), stage_conf="medium", entry_date="2010", country="CN",
             country_src="web_verified", country_cite=SITE("hygeia-medical-services-group"), city="Shanghai",
             focus="Healthcare & Bio",
             note="Hygeia Medical Services Group (hygeiamedical.cn, a Shanghai radiotherapy and oncology hospital chain) is "
                  "read as today's Hygeia Healthcare Holdings, listed in Hong Kong since 2020 (HKG:6078): HKD 5.91B @ ECB "
                  "2026-09-30 (HKD/EUR 8.9095, EUR/USD 1.1355) = $753.2M. Stage from the firm's own label Growth 2010."))

L.append(cls("hyperion-therapeutics", rng="below_1b", focus="Healthcare & Bio", city="Brisbane",
             note="Horizon Pharma bought Hyperion in 2015; EDGAR's last business address is Brisbane, CA (the earlier "
                  "Form D gave South San Francisco)."))

L.append(cls("ifonly", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=W("IfOnly"), stage_conf="high", entry_date="2013-10", country="US", city="San Francisco",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2013-10", "Series A", 12000000, firm_in_round=True, source=W("IfOnly"), source_type="press"),
                     rnd("2016-02", "Series B", 10250000, source=W("IfOnly"), source_type="press"),
                     rnd("2018-04", "Series D", 20000000, lead="Mastercard", firm_in_round=True, source=W("IfOnly"),
                         source_type="press")],
             note="NEA was in the $12M Series A of October 2013 (Wikipedia), IfOnly's first round. Mastercard acquired "
                  "IfOnly in Q4 2019 (Wikipedia; the firm's exit line)."))

L.append(cls("illusive-networks", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=W("Illusive Networks"), stage_conf="high", entry_date="2015-10-20", country="IL",
             country_src="web_verified", country_cite=W("Illusive Networks"), city="Tel Aviv", focus="Security",
             rounds=[rnd("2015-06", "Series A", 5000000, lead="Team8", source=W("Illusive Networks"), source_type="press"),
                     rnd("2015-10-20", "Series B", 22000000, lead="NEA", firm_in_round=True,
                         source=W("Illusive Networks"), source_type="press")],
             note="NEA led the $22M Series B announced 2015-10-20 (Wikipedia; the firm's post of the same day), after "
                  "Team8's Series A, so the entry is Growth. Headquartered in Tel Aviv and New York (Wikipedia); "
                  "Proofpoint acquired it in 2022 (the firm's exit line)."))

L.append(cls("imanage", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998", country="US",
             city="Foster City", focus="SaaS", rounds=[],
             note="iManage listed in 1999 and merged into Interwoven in 2003 (the firm's exit line names Interwoven); "
                  "EDGAR's last business address is Foster City, CA. The round NEA entered in 1998 is not named."))

L.append(cls("imara", status="acquired", rng="below_1b", focus="Healthcare & Bio", city="Boston", flags=["model_disputes_source"],
             note="Imara merged with Enliven Therapeutics in 2023; EDGAR now carries the registrant (CIK 1672619) as "
                  "Enliven, so the Imara business reads acquired, aligned with the Battery book, and the prefilled "
                  "public float (Enliven's) is disputed. Imara was based in Boston."))

L.append(cls("incarey", status="private", rng="below_1b", stage="undetermined", entry_date="2021", country="CN",
             country_src="web_verified", country_cite=SITE("incarey"), focus="Healthcare & Bio",
             flags=["city_unknown"], rounds=[],
             note="The firm's own page describes a chronic-disease management platform based in China; no source on disk "
                  "names its city or the round NEA entered in 2021."))

L.append(cls("infogear-technology", status="acquired", rng="below_1b", stage="undetermined", entry_date="1996",
             country="US", city="Redwood City", focus="Consumer & Marketplaces", rounds=[],
             note="Cisco acquired InfoGear in 2000 (the firm's exit line). The round NEA entered in 1996 is not named."))

L.append(cls("inhibitex", country="US", city="Alpharetta", stage="Growth", stage_src="web_verified",
             stage_cite=INHIB_S1, stage_conf="high", entry_date="2002-02", rng="below_1b", focus="Healthcare & Bio",
             rounds=[rnd("2002-02", "Series D", 44997928, firm_in_round=True, source=INHIB_S1, source_type="filing"),
                     rnd("2003-12", "Series E", 20045690, source=INHIB_S1, source_type="filing")],
             note="The 2004 S-1 lists New Enterprise Associates 10 among the buyers of the Series D sold in February to "
                  "April 2002 (about $45.0M), and NEA's Barrett joined the board in February 2002: a pre-IPO entry at "
                  "Series D, so the firm's Public/PIPES label is not the entry. Bristol-Myers Squibb bought Inhibitex in "
                  "2012; EDGAR's address is Alpharetta, GA."))

L.append(cls("innerworkings", city="Chicago", focus="SaaS", stage="Growth", stage_src="web_verified",
             stage_cite=FTS("INNERWORKINGS", "S-1"), stage_conf="high", entry_date="2006-01", rng="below_1b",
             rounds=[rnd("2006-01", "Series E", None, firm_in_round=True, source=FTS("INNERWORKINGS", "S-1"),
                         source_type="filing")],
             note="The 2006 S-1 says InnerWorkings issued 10.2M Series E preferred (about 25% fully diluted) to New "
                  "Enterprise Associates 11 and NEA Ventures 2005 in January 2006; the firm's own label is Growth. HH "
                  "Global bought InnerWorkings in 2020."))

HIRED_A = "https://techcrunch.com/2014/03/24/hired-raises-15m-series-a/"  # printed in the GV row; read 2026-09-30
INDIO_B = "https://menlovc.com/portfolio/indio/"  # printed in the Menlo row; read 2026-09-30
INFLU_SEED = ("https://techcrunch.com/2012/08/08/influitive-raises-3-75-million-from-11-investors-in-seed-preferred-"
              "round-for-customer-advocate-platform/")  # printed in the First Round row; read 2026-09-30
HOUSERX_B = NEWS("house-rx", "House Rx Raises $55 Million to Scale In-Clinic")  # read 2026-09-30
HABITAT = NEWS("habitat-health", "announces founding leadership team")  # read 2026-09-30
H3_E = NEWS("horizon3-ai", "raises $250M at $2B-plus valuation")  # read 2026-09-30
HOWL = NEWS("howl", "Quietly Sells Creator Business")  # read 2026-09-30
HYPERFAIR = NEWS("hyperfair", "invest $ 1,2 million in hyperfair")  # read 2026-09-30
INKITT_B = NEWS("inkitt", "Data-driven publishing platform Inkitt raises $59 million")  # read 2026-09-30
GUIDESPARK = "https://www.guidespark.com/"  # read 2026-09-30: acquired by Tivian
HIREGUIDE = "https://www.hireguide.com/"  # read 2026-09-30: team and technology acquired by Hirevue
HOS = "https://www.hosinc.co/"  # read 2026-09-30

L.append(cls("guideline", status="acquired", rng="below_1b", stage="undetermined", entry_date="2015", city="Burlingame",
             focus="Fintech & Payments", rounds=[],
             note="Gusto agreed to buy Guideline (announced 2025-08-27), read as acquired and aligned with the Felicis and "
                  "Tiger books; Tiger led the $35M Series C of December 2018. NEA's 2015 round, in the year Guideline was "
                  "founded, is not named in any source on disk."))

L.append(cls("guidespark", status="acquired", rng="below_1b", city="Menlo Park", city_src="formd_address",
             focus="SaaS",
             note="The company's own site says GuideSpark has been acquired by Tivian and its legacy video product "
                  "discontinued. NEA's own 2014 post says Pete Sonsini led an investment in GuideSpark in March 2014, "
                  "a year before the 2015 Form D the prefilled stage rests on."))

L.append(cls("habitat-health", status="private", rng="below_1b", stage="undetermined", entry_date="2023", country="US",
             focus="Healthcare & Bio", flags=["city_unknown"],
             rounds=[rnd("2024-09-10", "unnamed", 50000000, lead="Town Hall Ventures, NEA, Kaiser Permanente",
                         firm_in_round=True, source=HABITAT, source_type="press")],
             note="Kaiser Permanente and Town Hall Ventures launched Habitat Health, a PACE provider opening its first "
                  "center in California in 2025, with more than $50M from Town Hall, NEA and Kaiser (PR Newswire, "
                  "2024-09-10). No round is named and no source gives the company's city."))

L.append(cls("hired", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=HIRED_A,
             stage_conf="high", entry_date="2013", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", grad="graduated", grad_src="web_verified", grad_cite=HIRED_A,
             grad_conf="high",
             rounds=[rnd("2013", "Seed", 2700000, firm_in_round=True, source=HIRED_A, source_type="press"),
                     rnd("2014-03-24", "Series A", 15000000, lead="Crosslink, Sierra Ventures", source=HIRED_A,
                         source_type="press")],
             note="TechCrunch (2014-03-24) names NEA among the backers of Hired's $2.7M seed and reports the $15M Series A "
                  "led by Crosslink and Sierra, which graduates the row. Vettery (Adecco) acquired Hired in November 2020 "
                  "(Wikipedia); aligned with the GV book."))

L.append(cls("hireguide", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("hireguide"), stage_conf="medium", entry_date="2022", country="US", focus="SaaS",
             flags=["city_unknown"], rounds=[],
             note="The company's own site says Hireguide's team and technology have been acquired by Hirevue. Stage from "
                  "the firm's own label Seed, first invested 2022; no source gives its city. Graduation left for the "
                  "graduation pass."))

L.append(cls("horizon3-ai", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=H3_E,
             asof="2026-08-03", city="San Francisco", focus="Security",
             rounds=[rnd("2025-06-10", "Series D", 100000000, lead="NEA", firm_in_round=True, source_type="press"),
                     rnd("2026-08-03", "Series E", 250000000, lead="NightDragon, NEA", firm_in_round=True, source=H3_E,
                         source_type="press")],
             note="Series E of $250M co-led by NightDragon and NEA at a valuation of more than $2B (SiliconANGLE, "
                  "2026-08-03); NEA led the $100M Series D of June 2025 (the firm's own post), its entry."))

L.append(cls("hos", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=SITE("hos"),
             stage_conf="medium", entry_date="2022", country="US", focus="AI & Applied AI", flags=["city_unknown"],
             rounds=[],
             note="Stage from the firm's own label Seed, first invested 2022; the company's own site names NEA, Sequoia, "
                  "B5 Capital, Cortical and IA Ventures and gives no city. Momentum check 2026-09-30 (Google News for hOS "
                  "and Jeremy Achin): no reported round, so no $1B+ mark. Graduation left for the graduation pass."))

L.append(cls("house-rx", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=HOUSERX_B, stage_conf="high", entry_date="2025-11-12", country="US", city="San Francisco",
             focus="Healthcare & Bio",
             rounds=[rnd("2025-11-12", "Series B", 55000000, lead="NEA, Town Hall Ventures", firm_in_round=True,
                         source=HOUSERX_B, source_type="press")],
             note="NEA and Town Hall Ventures led House Rx's $55M Series B equity and debt round (PR Newswire, "
                  "2025-11-12), the firm's 2025 entry; San Francisco dateline, as in the First Round book."))

L.append(cls("houzz", stage="undetermined", entry_date="2012", city="Palo Alto", focus="Consumer & Marketplaces",
             rounds=[rnd("2011", "Series A", 11600000, lead="Sequoia", source_type="press"),
                     rnd("2017-06", "Series E", 400000000, lead="ICONIQ", source_type="press")],
             note="Sequoia led the 2011 Series A and ICONIQ the 2017 Series E at $4B (sibling books); the round NEA "
                  "entered in 2012 is not named in any source on disk. City aligned with the Sequoia and ICONIQ books."))

L.append(cls("howl", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=SITE("howl"),
             stage_conf="medium", entry_date="2015", country="US", city="New York", focus="Media, Gaming & Advertising",
             rounds=[],
             note="Howl (launched as Narrativ) sold its creator business to Taboola's Connexity in 2026 but continues to "
                  "operate, per its founder (Adweek, 2026-09-14). Stage from the firm's own label Seed, first invested 2015. "
                  "Graduation left for the graduation pass."))

L.append(cls("hyperfair", status="unknown", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_cite=HYPERFAIR, stage_conf="high", entry_date="2014-02", country="US", city="San Francisco",
             city_src="web_verified", focus="SaaS",
             rounds=[rnd("2014-02-21", "convertible loan", 1200000, lead="Atlante Ventures, NEA, Como Venture",
                         firm_in_round=True, source=HYPERFAIR, source_type="press")],
             note="Atlante Ventures, NEA and Como Venture put $1.2M into Hyperfair as a convertible loan in February 2014 "
                  "(Intesa Sanpaolo), read as its seed; HQ San Francisco with R&D in Lecco. The firm's company link now "
                  "points to an unrelated domain and no later source shows the company operating. Graduation left for the "
                  "graduation pass."))

L.append(cls("idfy", status="private", rng="below_1b", stage="undetermined", entry_date="2015", country="IN",
             country_src="web_verified", country_cite=W("IDfy"), city="Mumbai", focus="Security",
             rounds=[rnd("2015-08", "unnamed", 3000000, firm_in_round=True, source=W("IDfy"), source_type="press"),
                     rnd("2020-08-27", "unnamed", 2000000, source_type="press")],
             note="IDfy, an identity-verification company headquartered in Mumbai (Wikipedia), had raised up to $3M by "
                  "August 2015 from investors including Blume, Faktory, NEA and Beenos; no source names NEA's round."))

L.append(cls("ifttt", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=SITE("ifttt"),
             stage_conf="medium", entry_date="2011", country="US", city="San Francisco", focus="SaaS", rounds=[],
             note="Stage from the firm's own label Seed, first invested 2011; the a16z book records a16z leading the 2012 "
                  "Series A without a citation. Graduation left for the graduation pass."))

L.append(cls("in-house-health", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("in-house-health"), stage_conf="medium", entry_date="2024", grad="censored", country="US",
             focus="Healthcare & Bio", flags=["city_unknown"],
             rounds=[rnd("2024-05-08", "Seed", 4000000, source_type="press")],
             note="Stage from the firm's own label Seed, first invested 2024; In-House Health announced a $4M seed on "
                  "2024-05-08 (Business Wire, page not readable, so NEA's place in it is unconfirmed). A bare 2024 reads "
                  "inside the window, so censored. Momentum check 2026-09-30 (Google News): no $1B+ round."))

L.append(cls("indio", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=SITE("indio"),
             stage_conf="medium", entry_date="2016", country="US", city="San Francisco", focus="Fintech & Payments",
             grad="graduated", grad_src="web_verified", grad_cite=INDIO_B, grad_conf="high",
             rounds=[rnd("2019-05-02", "Series B", 20000000, source=INDIO_B, source_type="firm")],
             note="Stage from the firm's own label Seed, first invested 2016. Indio raised a $20M Series B in 2019 (Menlo's "
                  "own page; Coverager), which graduates the row, and Applied Systems acquired it in late 2019."))

L.append(cls("influitive", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_cite=INFLU_SEED, stage_conf="high", entry_date="2012-08", country="CA", country_src="web_verified",
             country_cite=INFLU_SEED, city="Toronto", focus="SaaS",
             rounds=[rnd("2012-08-08", "Seed", 3750000, firm_in_round=True, source=INFLU_SEED, source_type="press"),
                     rnd("2016-03-02", "unnamed", 8200000, source_type="press")],
             note="TechCrunch (2012-08-08) names NEA among the investors in Influitive's $3.75M seed preferred round. "
                  "Status follows the Lightspeed book (private; a 2023 asset sale is unconfirmed, and the company bought "
                  "PostBeyond in 2021); the First Round book reads acquired. Graduation left for the graduation pass."))

L.append(cls("inkitt", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=INKITT_B,
             stage_conf="high", entry_date="2021-10", country="US", city="San Francisco", focus="Media, Gaming & Advertising",
             rounds=[rnd("2017-09", "Series A", 3900000, source_type="press"),
                     rnd("2021-10-05", "Series B", 59000000, lead="NEA", firm_in_round=True, source=INKITT_B,
                         source_type="press"),
                     rnd("2024-02-26", "unnamed", 37000000, source_type="press")],
             note="NEA's Scott Sandell led Inkitt's $59M Series B (Tech.eu, 2021-10-05), the firm's 2021 entry. Tech.eu "
                  "then called it Berlin-based; country and city follow the HV Capital and Khosla books (San Francisco)."))

L.append(cls("infoworks", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2018", city="Palo Alto", city_src="formd_address", focus="Data Infrastructure",
             rounds=[rnd("2015-05-11", "unnamed (Form D)", 4710767, source=FORMD_CITE("infoworks", 1), source_type="filing"),
                     rnd("2016-12-20", "unnamed (Form D)", 14999998, source=FORMD_CITE("infoworks", 2), source_type="filing"),
                     rnd("2018-10-22", "unnamed (Form D)", 24999986, firm_in_round=True,
                         source=FORMD_CITE("infoworks", 3), source_type="filing"),
                     rnd("2020-04-28", "unnamed (Form D)", 12999992, source=FORMD_CITE("infoworks", 4), source_type="filing"),
                     rnd("2021-12-17", "unnamed (Form D)", 26215034, source=FORMD_CITE("infoworks", 0), source_type="filing")],
             note="The firm dates its first investment to 2018, which matches the company's third Form D round (October "
                  "2018, $25.0M sold) after rounds in 2015 and 2016, so the entry reads Growth; the prefilled 2021 date "
                  "anchored on a later filing is replaced. Uniphore acquired Infoworks (the firm's exit line)."))

L.append(cls("hdmessaging", status="unknown", rng="below_1b", stage="undetermined", entry_date="2007", country="US",
             focus="Media, Gaming & Advertising", flags=["city_unknown"], rounds=[],
             note="A mobile entertainment company the firm first backed in 2007; its listing links brightkite.com and no "
                  "news, filing or article on disk shows its later fate, city or round, so status is unknown."))

L.append(cls("igneous-systems", status="acquired", rng="below_1b", city="Seattle", focus="Data Infrastructure",
             note="Rubrik acquired Igneous's technology and IP assets in December 2020 (GeekWire, TechTarget), read as an "
                  "asset sale of the business."))

L.append(cls("hydra-biosciences-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2002",
             country="US", city="Cambridge", focus="Healthcare & Bio", rounds=[],
             note="Eli Lilly bought Hydra's pre-clinical pain program in December 2018 (Lilly release), the sale the "
                  "firm's exit line calls an acquisition by Lilly. The round NEA entered in 2002 is not named."))

L.append(cls("heap", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             city="San Francisco", focus="SaaS",
             rounds=[rnd("2015-12-11", "Series A", 9111757, firm_in_round=True, source=FORMD_CITE("heap", 1),
                         source_type="filing"),
                     rnd("2017-04-20", "Series B", 26999994, source=FORMD_CITE("heap", 2), source_type="filing"),
                     rnd("2019-07-23", "Series C", 55000000, source_type="press"),
                     rnd("2021-11-24", "Series D", 112599966, source=FORMD_CITE("heap", 0), source_type="filing")],
             note="Heap's first Form D after its YC seed (December 2015, $9.1M sold) names NEA's Chetan Puttagunta as a "
                  "director, and the Menlo book records Heap's Series A in 2016 from Menlo's own page: read as NEA "
                  "entering at the Series A. Contentsquare acquired Heap in 2023, as in every sibling book."))

L.append(cls("hackerone", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=W("HackerOne"), stage_conf="high", entry_date="2015-06", country="US", city="San Francisco",
             focus="Security",
             rounds=[rnd("2014-05", "Series A", 9000000, lead="Benchmark", source=W("HackerOne"), source_type="press"),
                     rnd("2015-06", "Series B", 25000000, lead="NEA", firm_in_round=True, source=W("HackerOne"),
                         source_type="press"),
                     rnd("2017-02", "Series C", 40000000, lead="Dragoneer", source=W("HackerOne"), source_type="press"),
                     rnd("2019", "Series D", 36000000, lead="Valor Equity Partners", source=W("HackerOne"),
                         source_type="press")],
             note="NEA led HackerOne's $25M Series B (Wikipedia; the firm's own announcement of 2015-06-24), after "
                  "Benchmark's 2014 Series A, so the entry is Growth. No priced round at $1B is on record."))

L.append(cls("illumitex-inc", status="unknown", rng="below_1b", city="Austin", focus="Industrial & Robotics",
             note="Illumitex ended its LED lighting operations in February 2020 to become an AgTech AI company "
                  "(FarmVisionAI); no later source shows it operating, and the firm dropped it from its list after 2020."))

L.append(cls("gumgum", status="private", rng="below_1b", stage="undetermined", entry_date="2011", country="US",
             city="Santa Monica", focus="Media, Gaming & Advertising",
             rounds=[rnd("2009-07-08", "unnamed (second round)", 2600000, source_type="press"),
                     rnd("2021-04-13", "unnamed", 75000000, lead="Goldman Sachs", source_type="press")],
             note="GumGum is private and operating (a $75M Goldman Sachs round in April 2021, expansion news in 2026); "
                  "NEA's stake moved to NewView Capital in the 2018 spinout, which the firm's exit line records. The round "
                  "NEA entered in 2011 is not named in any source on disk. City aligned with the First Round book."))

L.append(cls("hearsay-social", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011", country="US",
             city="San Francisco", focus="SaaS",
             rounds=[rnd("2011-07-28", "unnamed", 18000000, source=NEWS("hearsay-social", "Hearsay Social Raises $18 Million"),
                         source_type="press")],
             note="Yext completed its acquisition of Hearsay Systems on 2024-08-01 (Business Wire; about $125M). Hearsay "
                  "raised $18M in July 2011 (Forbes), NEA's first-invested year, but the page naming the round's investors "
                  "could not be read, so the stage stays undetermined."))
jl.write("c5b", L)
