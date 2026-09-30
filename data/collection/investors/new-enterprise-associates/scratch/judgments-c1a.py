import judge_lib as jl
from judge_lib import cls, rnd

# Batch 1 (judge c1): listed members, classification only. 42floors re-judged for its stage only (the pilot
# recorded status, city and focus); its note carries the pilot's sentence forward.

W23 = jl.W("23andMe")
S1_23 = "https://www.sec.gov/Archives/edgar/data/1804591/000119312521210858/d154309ds1.htm"
ACCL = "https://www.sec.gov/Archives/edgar/data/1346937/000119312508128918/ds1.htm"
ADV = "https://www.sec.gov/Archives/edgar/data/1091238/000119312504056353/ds1.htm"
ACRV = "https://www.sec.gov/Archives/edgar/data/1781174/000095012322008876/filename1.htm"
ACTS_F1 = "https://www.sec.gov/Archives/edgar/data/1342068/000119312505206886/df1.htm"
ACTS_SPA = "https://www.sec.gov/Archives/edgar/data/1342068/000119312505206886/dex101.htm"
ADAP = "https://www.sec.gov/Archives/edgar/data/1621227/000091205715000017/filename1.htm"
ADXN = "https://www.sec.gov/Archives/edgar/data/1574232/000091205719000390/filename4.htm"
ACAD = "https://www.sec.gov/Archives/edgar/data/1070494/000119312511006698/dex991.htm"
AFMD_20F = "https://www.sec.gov/Archives/edgar/data/1608390/000095010317002899/dp74167_20f.htm"
AFNA = "https://www.sec.gov/Archives/edgar/data/1792694/000095012321012167/filename1.htm"
AKTX = "https://www.sec.gov/Archives/edgar/data/1541157/000114420415055704/v420593_ex99-1.htm"
AKUS = "https://www.sec.gov/Archives/edgar/data/1722271/000091205720000111/filename1.htm"
ALXA = "https://www.sec.gov/Archives/edgar/data/1344413/000089161805000914/f15073orexv4w2.htm"
ALIM = "https://www.sec.gov/Archives/edgar/data/1267602/000119312512305561/d382118dex991.htm"
AFOP = "https://www.sec.gov/Archives/edgar/data/1122342/000089161800005195/0000891618-00-005195-index.htm"
ATON = "https://www.sec.gov/Archives/edgar/data/1089925/000101287099003357/0001012870-99-003357-index.htm"
TC42 = "https://techcrunch.com/2013/01/31/yc-alum-42floors-raises-12-3m-led-by-nea-to-take-its-office-rental-search-engine-us-wide-and-beyond"

L = [
    cls("1bog", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="Climate & Energy",
        note="One Block Off the Grid, a solar group-purchase company in San Francisco (its 2010 Form D address), "
             "acquired by Pure Energies per the firm's own exit line. Graduation left for the graduation pass."),

    cls("23andme", status="acquired", rng="below_1b", city="South San Francisco",
        stage="Series A", stage_src="model", stage_conf="medium", stage_cite=W23, entry_date="2007",
        focus="Healthcare & Bio", flags=["model_disputes_source"],
        rounds=[rnd("2007", "Series A", 8953000, None, True, W23, "press"),
                rnd("2009", "Series B", 27779000, None, None, S1_23, "filing"),
                rnd("2010-11-09", "Series C", 22000000, "Johnson & Johnson Development Corporation", None,
                    "https://techcrunch.com/2010/11/09/23andme-funding-2/", "press"),
                rnd("2012-12-11", "Series D", 50000000, None, None,
                    "https://www.23andme.org/media-center/press-releases/23andme-raises-more-than-50-million-in-new-financing/",
                    "company")],
        note="Status disputes the prefilled public float: after its March 2025 Chapter 11 filing TTAM Research Institute "
             "bought substantially all of 23andMe's assets, closing 2025-07-14 (Wikipedia), which reads acquired as the GV and "
             "Sequoia rows do. NEA entered in 2007 beside Google, Genentech and Mohr Davidow (Wikipedia), the round the 2021 "
             "S-1 carries as the $8.95M Series A, the company's first preferred; the entry date replaces the 2009 Form D anchor."),

    cls("3-v-biosciences-inc", city="San Mateo", focus="Healthcare & Bio",
        note="3-V Biosciences renamed itself Sagimet Biosciences (Nasdaq: SGMT, listed 2023), headquartered in San Mateo; "
             "its 2019 Form D gave Campbell."),

    cls("3com-corporation", status="acquired", rng="below_1b", country="US", city="Marlborough",
        stage="undetermined", entry_date="1996", focus="Data Infrastructure", rounds=[],
        note="Networking company acquired by Hewlett-Packard in 2010, Marlborough by then (as the Sequoia row reads). The firm's "
             "first-invested year 1996 is twelve years after 3Com's 1984 listing, so no venture round can be named; the row is "
             "a candidate for D8 (stock received for a company sold to 3Com) or X1 review."),

    cls("3ware", status="acquired", rng="below_1b", city="Mountain View", stage="undetermined", entry_date="1998",
        focus="Data Infrastructure", rounds=[],
        note="Storage (RAID) controller maker acquired by Applied Micro Circuits in 2004 (the firm's exit line). NEA first "
             "invested in 1998 (Scott Sandell); no source found names that round."),

    cls("42floors", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC42,
        entry_date="2013-01-31", flags=["stage_disputes_band"],
        rounds=[rnd("2012-11", "Series A", 5000000, None, False,
                    "https://techcrunch.com/2012/11/16/42floors-raises-5m-from-dave-mcclure-alexis-ohanian-others-expands-office-search-site-to-new-york/",
                    "press"),
                rnd("2013-01-31", "Series B", 12300000, "NEA", True, TC42, "press")],
        note="Acquired by Knotel in 2019; the firm's own exit line and the a16z book agree. NEA entered as a new investor "
             "leading the $12.3M Series B (TechCrunch, 2013-01-31), so the Form D band's Series A is overridden to Growth."),

    cls("51offer", status="private", rng="below_1b", country="CN", country_src="web_verified",
        country_cite="https://www.51offer.com/", city="Shanghai", stage="undetermined", entry_date="2014",
        focus="Consumer & Marketplaces", rounds=[],
        note="Chinese study-abroad services platform; its own site gives a Xuhui District, Shanghai address and cites a $50M "
             "investment from an international consortium without naming rounds. No source names NEA's 2014 round."),

    cls("858-therapeutics", status="private", rng="below_1b", city="San Diego", focus="Healthcare & Bio",
        note="Private oncology biotech in San Diego (2024 Form D address), no priced mark near $1B; the Insight row agrees."),

    cls("abcuro", status="private", rng="below_1b", city="Newton", focus="Healthcare & Bio",
        note="Private clinical-stage antibody company in Newton, Massachusetts (2025 Form D address); no disclosed valuation near $1B."),

    cls("acadia-pharmaceuticals", city="San Diego", stage="Growth", stage_src="web_verified", stage_conf="high",
        stage_cite=ACAD, entry_date="2011-01", focus="Healthcare & Bio",
        rounds=[rnd("2011-01", "PIPE", 6000001, None, True, ACAD, "filing")],
        note="NEA's Growth Equity Opportunities Fund II bought $6.0M in Acadia's January 2011 private placement (securities "
             "purchase agreement, 8-K exhibit), seven years after the 2004 listing: an X1 row, Growth only if Erik rules a PIPE "
             "a venture entry."),

    cls("acclarent", status="acquired", rng="below_1b", country="US", city="Menlo Park",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ACCL, entry_date="2005-01",
        focus="Healthcare & Bio", flags=["stage_disputes_band"],
        rounds=[rnd("2005-01", "Series A", 13100000, None, True, ACCL, "filing"),
                rnd("2005-11", "Series B", 25100000, None, True, ACCL, "filing"),
                rnd("2007-02", "Series C", None, None, True, ACCL, "filing")],
        note="The 2008 S-1 shows entities affiliated with NEA holding 6,730,769 Series A shares from the January 2005 Series A "
             "at $1.04, plus Series B and C, so the documented round overrides the firm's Seed label. Acquired by Ethicon "
             "(Johnson & Johnson) in January 2010; Menlo Park was its headquarters."),

    cls("aciex", status="acquired", rng="below_1b", city="Boston", stage="undetermined", entry_date="2007",
        focus="Healthcare & Bio",
        rounds=[rnd("2011-08-01", "unnamed (Form D)", 8000000, None, None, jl.FORMD_CITE("aciex", 0), "filing"),
                rnd("2014-04-17", "unnamed (Form D)", 3199720, None, None, jl.FORMD_CITE("aciex", 1), "filing")],
        note="Ophthalmic drug developer acquired by Nicox in 2014 (the firm's exit line), last filing from Boston. NEA's 2007 "
             "entry predates the company's Form Ds and no source names that round."),

    cls("acquia", status="acquired", rng="below_1b", city="Boston", focus="SaaS",
        note="Drupal-based digital experience platform, Boston; acquired by Vista Equity Partners in 2019 (the firm's exit line)."),

    cls("acrivon-therapeutics", country="US", city="Watertown",
        stage="Seed", stage_src="first_party", stage_conf="medium", stage_cite=jl.SITE("acrivon-therapeutics"),
        entry_date="2018", grad="graduated", grad_src="web_verified", grad_cite=ACRV, grad_conf="high",
        focus="Healthcare & Bio",
        rounds=[rnd("2019-06", "convertible notes", 3000000, None, None, ACRV, "filing"),
                rnd("2020-10", "Series A-1", 3000000, None, None, ACRV, "filing"),
                rnd("2021-01", "Series A-1", 12500000, None, True, ACRV, "filing")],
        note="The firm labels its 2018 entry Seed; the 2022 registration statement shows New Enterprise Associates 16 buying "
             "Series A-1 preferred in the January 2021 closing, a later round named Series A, and gives Watertown, "
             "Massachusetts as the principal office."),

    cls("actions-semiconductor", status="acquired", rng="below_1b", country="CN", country_src="web_verified",
        country_cite=ACTS_F1, city="Zhuhai", stage="Growth", stage_src="web_verified", stage_conf="medium",
        stage_cite=ACTS_SPA, entry_date="2005", focus="Industrial & Robotics",
        rounds=[rnd("2005", "pre-IPO share purchase", None, "Intel Capital, NEA and others", True, ACTS_SPA, "filing")],
        note="Zhuhai fabless chip company (F-1 principal office); NEA Ventures 2005 and NEA 11 were lead investors in a 2005 "
             "pre-IPO share purchase from existing shareholders, Growth. Listed on Nasdaq in November 2005 and taken private "
             "by merger with Starman Limited, completed 2016-12-09 (Wikipedia)."),

    cls("adaptimmune", city="Abingdon", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ADAP, entry_date="2014-09-23",
        focus="Healthcare & Bio", flags=["stage_disputes_band"],
        rounds=[rnd("2014-09-23", "Series A", 103809789, None, True, ADAP, "filing")],
        note="The 2015 registration statement names the September 2014 $103.8M round a Series A, with NEA buying $35.0M; the "
             "Form D band's Growth is overridden. Principal office Milton Park, Abingdon; its assets were sold to US WorldMeds in 2025."),

    cls("addex-therapeutics", status="public", rng="below_1b", city="Geneva",
        stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=ADXN, entry_date="2018-02",
        focus="Healthcare & Bio",
        rounds=[rnd("2018-02", "PIPE (capital increase)", None, None, True, ADXN, "filing")],
        note="Listed on SIX (and Nasdaq ADSs), Geneva principal office, market value far below $1B. NEA's Growth Equity "
             "Opportunities Fund IV entered through the February 2018 capital increase of the already listed company: an "
             "X1/R2 row, Growth only if Erik rules a PIPE a venture entry."),

    cls("addthis", status="acquired", rng="below_1b", city="McLean", stage="undetermined", entry_date="2008",
        focus="Media, Gaming & Advertising", rounds=[],
        note="Clearspring Technologies (renamed AddThis in 2012), acquired by Oracle on 2016-01-05 (Wikipedia); McLean as the "
             "IVP row reads. No source names NEA's 2008 round."),

    cls("advanced-cardiac-therapeutics-inc", status="acquired", rng="below_1b", city="Santa Clara",
        focus="Healthcare & Bio",
        note="Advanced Cardiac Therapeutics (Santa Clara, per its 2017 Form D) became EPIX Therapeutics, which Medtronic "
             "acquired in 2019 for $316M (MassDevice)."),

    cls("advanced-cardiovascular", status="acquired", rng="below_1b", country="US", city="Santa Clara",
        stage="undetermined", focus="Healthcare & Bio", rounds=[],
        note="Advanced Cardiovascular Systems, the balloon angioplasty catheter maker Eli Lilly acquired in 1984; the live "
             "page's 2018 invest year and its description (copied from Actions Semiconductor) are errors, so no entry date is given."),

    cls("advertising-com", country="US", city="Baltimore",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ADV, entry_date="1999-09",
        rng="below_1b", focus="Media, Gaming & Advertising",
        rounds=[rnd("1999-09", "Series C", 9100000, None, True, ADV, "filing")],
        note="The 2004 S-1 shows NEA VIII, 8A, Presidents Fund and Ventures holding Series C (sold about September 1999, $8.6M "
             "net) and Series E preferred, matching the firm's 1999 entry. Baltimore company acquired by America Online in 2004."),

    cls("aeluros", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="undetermined",
        entry_date="2001", focus="Industrial & Robotics", rounds=[],
        note="10 Gigabit Ethernet physical-layer chip company founded 2001, merged into NetLogic Microsystems in October 2007 "
             "(Wikipedia). No source names NEA's 2001 round."),

    cls("aera", status="private", rng="below_1b", country="US", city="Mountain View", stage="undetermined",
        entry_date="2014", focus="AI & Applied AI",
        rounds=[rnd("2017-06", "unnamed", 50000000, None, None, jl.NEWS("aera", "rebrands as Aera"), "press")],
        note="FusionOps, renamed Aera Technology in June 2017 after a $50M raise (DC Velocity); no priced mark near $1B. No "
             "source names NEA's 2014 round."),

    cls("aerohive-networks", city="Milpitas", rng="below_1b",
        stage="Growth", stage_src="first_party", stage_conf="medium", stage_cite=jl.SITE("aerohive-networks"),
        focus="Data Infrastructure", flags=["stage_disputes_band"],
        rounds=[rnd("2006", "Series A", 4000000, None, None, jl.W("Aerohive Networks"), "press"),
                rnd("2007-07", "Series B", 20000000, "Kleiner Perkins", None, jl.W("Aerohive Networks"), "press"),
                rnd("2010-03", "Series C", 23500000, None, None, jl.W("Aerohive Networks"), "press"),
                rnd("2012-09", "Series E", 22500000, None, None, jl.W("Aerohive Networks"), "press")],
        note="The firm labels its 2011 entry Growth, and Wikipedia's round history puts Series A to C before it (2006-2010), "
             "so NEA's 2011 round was the Series D and the Form D band's Series A is overridden. Acquired by Extreme Networks, "
             "closed 2019-08-09."),

    cls("aerospike", status="private", rng="below_1b", city="Mountain View", stage="undetermined", entry_date="2012",
        focus="Data Infrastructure",
        rounds=[rnd("2014-06", "Series C", 20000000, None, None, jl.W("Aerospike (company)"), "press"),
                rnd("2019-11-18", "unnamed", 32000000, "Triangle Peak Partners", None, jl.W("Aerospike (company)"), "press"),
                rnd("2024-04-04", "unnamed", 109000000, None, None, jl.NEWS("aerospike", "raises $109M"), "press")],
        note="Real-time NoSQL database, Mountain View; Wikipedia names NEA among its backers by the August 2012 rebrand from "
             "Citrusleaf, but no source names NEA's 2012 round. No priced mark near $1B."),

    cls("aetion", status="acquired", rng="below_1b", country="US", city="New York",
        stage="Growth", stage_src="model", stage_conf="medium",
        stage_cite=jl.NEWS("aetion", "nabs Amgen-backed"), entry_date="2018-04",
        focus="Healthcare & Bio",
        rounds=[rnd("2018-04", "Series B", 36000000, None, None, jl.NEWS("aetion", "nabs Amgen-backed"), "press"),
                rnd("2021-05-11", "Series C", 110000000, "Warburg Pincus", None, jl.NEWS("aetion", "Closes $110M Series C"), "press")],
        note="NEA's 2018 entry matches the April 2018 $36M Series B (Fierce Biotech; the article was not readable, so NEA's "
             "place in it is not cited). Datavant agreed to acquire Aetion in May 2025 (Fierce Healthcare) and aetion.com now "
             "redirects to datavant.com."),

    cls("affimed", status="defunct", rng="below_1b", country="DE", country_src="web_verified", country_cite=AFMD_20F,
        city="Mannheim", stage="undetermined", entry_date="2017-01-25", focus="Healthcare & Bio", rounds=[],
        note="German immuno-oncology company (EDGAR business address Mannheim) that filed for insolvency proceedings in "
             "May 2025 and was delisted (GlobeNewswire), no sale reported. NEA's Growth Equity Opportunities Fund IV bought "
             "in Affimed's January 2017 underwritten public offering (13D), a listed purchase: an X1/R2 row with no venture round."),

    cls("affinia-therapeutics", status="private", rng="below_1b", city="Waltham",
        stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=AFNA, entry_date="2019-10",
        grad="graduated", grad_src="web_verified", grad_cite=AFNA, grad_conf="high",
        focus="Healthcare & Bio", flags=["stage_disputes_band"],
        rounds=[rnd("2019-10", "convertible notes", 8350000, None, True, AFNA, "filing"),
                rnd("2020-03", "Series A", 30400000, None, True, AFNA, "filing"),
                rnd("2021-04", "Series B", 110000000, None, True, AFNA, "filing")],
        note="The 2021 registration statement shows NEA 17 buying $2.0M of the October 2019 convertible notes that preceded "
             "the March 2020 Series A (the firm's archived page labels the 2019 entry Seed), so the Form D band's Growth is "
             "overridden; the Series A graduates it."),

    cls("aigen", status="private", rng="below_1b", city="Redmond", grad="graduated", grad_src="formd",
        grad_cite=jl.FORMD_CITE("aigen", 0), grad_conf="high", focus="Industrial & Robotics",
        note="Solar-powered weeding robots, Redmond (Form D address). After the $4.0M December 2021 seed the company filed a "
             "$15.0M round in September 2023, above twice the entry, which graduates it as the Form D layer reads."),

    cls("ai-squared", status="private", rng="below_1b", country="US", city="Washington",
        stage="Seed", stage_src="first_party", stage_conf="medium", stage_cite=jl.SITE("ai-squared"), entry_date="2021",
        grad="graduated", grad_src="web_verified", grad_conf="high",
        grad_cite="https://www.prnewswire.com/news-releases/ai-squared-raises-13-8m-to-accelerate-widespread-ai-adoption-within-organizations-302118803.html",
        focus="AI & Applied AI",
        rounds=[rnd("2024-04-17", "Series A", 13800000, "Ansa Capital", True,
                    "https://www.prnewswire.com/news-releases/ai-squared-raises-13-8m-to-accelerate-widespread-ai-adoption-within-organizations-302118803.html",
                    "company")],
        note="The firm labels its 2021 entry Seed; the April 2024 $13.8M Series A led by Ansa Capital lists NEA as an existing "
             "investor (PR Newswire, Washington dateline). Momentum check 2026-09-30 (Google News): no $1B+ priced round, below_1b."),

    cls("air-works", status="acquired", rng="below_1b", country="IN", country_src="web_verified",
        country_cite="https://airworks.aero", city="Gurugram", stage="undetermined", entry_date="2011",
        focus="Industrial & Robotics", rounds=[],
        note="Indian aviation MRO group headquartered in Gurgaon (its own site); Adani Defence Systems and Technologies bought "
             "control in 2025 and raised its stake to 99.98% in March 2026 (ET Infra). No source names NEA's 2011 round."),

    cls("ajax-vascular", status="unknown", rng="below_1b", country="US",
        stage="Seed", stage_src="first_party", stage_conf="medium", stage_cite=jl.SITE("ajax-vascular"), entry_date="2013",
        focus="Healthcare & Bio", flags=["city_unknown"],
        note="The firm lists a 2013 Seed in this cardiovascular device company and its archived pages mark it Historic; no "
             "press, filing or company site was found, so status and city are unknown. Graduation left for the graduation pass."),

    cls("akari-therapeutics", country="US", city="Tampa",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=AKTX, entry_date="2015-09",
        focus="Healthcare & Bio",
        rounds=[rnd("2015-09", "PIPE", 75000000, "Deerfield", True, AKTX, "filing")],
        note="NEA joined the $75M private placement led by Deerfield that closed with Celsus Therapeutics' September 2015 "
             "acquisition of Akari, a Nasdaq-listed company: an X1 row, Growth only if Erik rules a PIPE a venture entry. "
             "EDGAR's current business address is Tampa, Florida."),

    cls("akouos", country="US", city="Boston", rng="below_1b",
        stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=AKUS, entry_date="2017-10",
        grad="graduated", grad_src="web_verified", grad_cite=AKUS, grad_conf="high", focus="Healthcare & Bio",
        rounds=[rnd("2017-10", "Series Seed", 7100000, None, True, AKUS, "filing"),
                rnd("2018-07-17", "Series A", 50100000, None, True, AKUS, "filing"),
                rnd("2020-02", "Series B", 105065001, None, None, AKUS, "filing")],
        note="The 2020 registration statement shows NEA 16 buying $3.0M of the October 2017 Series Seed and then Series A "
             "in July 2018, which graduates it. Boston gene-therapy company acquired by Eli Lilly in December 2022."),

    cls("alexza-pharmaceuticals", country="US", city="Mountain View", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=ALXA, entry_date="2002",
        focus="Healthcare & Bio",
        rounds=[rnd("2002-09", "Series C", None, None, None, ALXA, "filing"),
                rnd("2004-11", "Series D", None, None, None, ALXA, "filing")],
        note="NEA 10 is an investor party to the November 2004 (Series D) rights agreement, which superseded the September "
             "2002 (Series C) one; the firm's 2002 year points to the Series C, and either round reads Growth. The Public/PIPES "
             "label is wrong for this pre-IPO position; acquired by Ferrer in 2016."),

    cls("alfred", status="private", rng="below_1b", country="US", city="New York",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=jl.W("Hello Alfred"), entry_date="2015-04",
        focus="Consumer & Marketplaces", flags=["model_disputes_source"],
        rounds=[rnd("2014-11", "Seed", 2000000, None, False, jl.W("Hello Alfred"), "press"),
                rnd("2015-04", "Series A", 10500000, None, True, jl.W("Hello Alfred"), "press"),
                rnd("2018-05", "Series B", 40000000, "Invesco, DivcoWest", None, jl.NEWS("alfred", "Invesco, DivcoWest"), "press"),
                rnd("2020-10", "unnamed", 42000000, "166 2nd LLC", None, jl.W("Hello Alfred"), "press")],
        note="Hello Alfred, New York; the GB country was a one-word Wikidata match. Wikipedia names NEA in the April 2015 "
             "$10.5M Series A and not in the November 2014 seed, so the entry is the Series A."),

    cls("alien-technology-corporation", status="private", rng="below_1b", city="San Jose", stage="undetermined",
        entry_date="1999", focus="Industrial & Robotics", rounds=[],
        note="RFID maker headquartered in San Jose (Wikipedia), still operating. NEA VIII and NEA Ventures 1999 entered in "
             "1999, but the 2006 S-1 lists Series A to H without dates for the early series, so NEA's round cannot be named."),

    cls("alimera-sciences", city="Alpharetta", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ALIM, entry_date="2012-07",
        focus="Healthcare & Bio",
        rounds=[rnd("2012-07", "PIPE", None, "Palo Alto Investors", True, ALIM, "filing")],
        note="NEA participated in the July 2012 private placement led by Palo Alto Investors, two years after the 2010 listing: "
             "an X1 row, Growth only if Erik rules a PIPE a venture entry. Alpharetta company acquired by ANI Pharmaceuticals in 2024."),

    cls("allakos", city="San Carlos", rng="below_1b", focus="Healthcare & Bio",
        note="San Carlos antibody company acquired by Concentra Biosciences in 2025 (EDGAR now shows the buyer's San Diego address)."),

    cls("allay-therapeutics", status="private", rng="below_1b", city="San Jose", stage="undetermined", entry_date="2019",
        focus="Healthcare & Bio",
        rounds=[rnd("2019-01-31", "unnamed (Form D)", 28752807, None, None, jl.FORMD_CITE("allay-therapeutics", 3), "filing"),
                rnd("2020-04-17", "unnamed (Form D)", 15000000, None, None, jl.FORMD_CITE("allay-therapeutics", 4), "filing"),
                rnd("2021-09-09", "unnamed (Form D)", 86890346, None, None, jl.FORMD_CITE("allay-therapeutics", 2), "filing"),
                rnd("2025-06-05", "Series D", 57500000, "Lightstone Ventures, ClavystBio", None,
                    jl.NEWS("allay-therapeutics", "Announces $57.5M Series D"), "company")],
        note="Post-surgical pain company in San Jose (Form D address), formerly Foundry Therapeutics 1. NEA's first year 2019 "
             "matches the January 2019 filing, but no source names that round."),

    cls("alliance-fiber-optic-products-inc", country="US", city="Sunnyvale", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=AFOP, entry_date="2000-07",
        focus="Industrial & Robotics",
        rounds=[rnd("1998-01", "Series A", 3276000, None, False, AFOP, "filing"),
                rnd("2000-01", "Series B", 4000000, None, False, AFOP, "filing"),
                rnd("2000-07", "Series C", 27500000, None, True, AFOP, "filing")],
        note="The November 2000 IPO prospectus shows NEA buying 2,000,000 Series C shares at $5.50 in July and August 2000, "
             "the round before the listing. Sunnyvale optical components maker acquired by Corning in 2016."),

    cls("alteon-websystems", status="acquired", rng="below_1b", country="US", city="San Jose",
        stage="Growth", stage_src="model", stage_conf="low", entry_date="1997", focus="Data Infrastructure",
        flags=["model_disputes_source"],
        rounds=[rnd("1996-05", "Series A", None, None, None, ATON, "filing"),
                rnd("1997-05", "Series B", None, None, None, ATON, "filing"),
                rnd("1998-06", "Series C", None, None, None, ATON, "filing"),
                rnd("1999-06", "Series D", None, None, None, ATON, "filing")],
        note="Acquired by Nortel Networks on 2000-10-04 (Wikipedia), not defunct, as the Sutter Hill and TCV rows read. NEA "
             "is not named in the 1999 prospectus; its 1997 first-invested year matches only the May 1997 Series B."),

    cls("amber-therapeutics", status="private", rng="below_1b", country="GB", country_src="web_verified",
        country_cite="https://www.amber-tx.com/", city="Didcot",
        stage="Series A", stage_src="first_party", stage_conf="high",
        stage_cite=jl.POST("amber-therapeutics-series-a"), entry_date="2024-06", focus="Healthcare & Bio",
        rounds=[rnd("2024-06-10", "Series A", 100000000, "NEA", True,
                    jl.NEWS("amber-therapeutics", "Closes $100 Million Series A"), "company")],
        note="NEA led the $100M Series A (the firm's post; the company's release, 2024-06-10, lists NEA among the new "
             "investors). The company's site gives its headquarters at Harwell Campus, Didcot, UK."),

    cls("american-pathology-partners", status="acquired", rng="below_1b", city="Brentwood", stage="undetermined",
        entry_date="2008-04", focus="Healthcare & Bio",
        rounds=[rnd("2008-04", "equity commitment", 75000000, "NEA", True, jl.W("American Pathology Partners"), "press"),
                rnd("2012-07-05", "unnamed (Form D)", 12000000, None, None, jl.FORMD_CITE("american-pathology-partners", 0), "filing")],
        note="Pathology lab platform in Brentwood, Tennessee (2012 Form D; Wikipedia says Nashville) that NEA backed with a "
             "$75M equity commitment in April 2008, a commitment that names no round; acquired by LabCorp per the firm's exit line."),
]

jl.write("c1a", L)
