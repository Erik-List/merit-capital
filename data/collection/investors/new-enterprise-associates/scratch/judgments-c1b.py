import judge_lib as jl
from judge_lib import cls, rnd

# Batch 2 (judge c1): listed members, classification only.

AGP = "https://www.sec.gov/Archives/edgar/data/1064863/000095013301500056/y44498a5s-1a.txt"
ANNX = "https://www.sec.gov/Archives/edgar/data/1528115/000095012319008962/filename1.htm"
ARST = "https://www.sec.gov/Archives/edgar/data/1368582/000095013407020122/filename1.htm"
ARDX = "https://www.sec.gov/Archives/edgar/data/1437402/000095012314003746/filename1.htm"
ATHR = "https://www.sec.gov/Archives/edgar/data/1140486/000119312503087125/ds1.htm"
ADNC = "https://www.sec.gov/Archives/edgar/data/1201663/000119312512012183/d229773ds1.htm"
ARDM = "https://www.sec.gov/Archives/edgar/data/1013238/000089161801501793/f75718orex4-3.txt"
AUPH = "https://www.sec.gov/Archives/edgar/data/1600620/000119312514145986/d710955dex991.htm"
AUPH_ADDR = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1600620&type=10-K&dateb=&owner=include&count=10"
AVEO = "https://www.sec.gov/Archives/edgar/data/1325879/000119312516589712/d165021dex103.htm"
AVZ = "https://www.sec.gov/Archives/edgar/data/1739410/000119312526392246/d71655ds4a.htm"
SA = "https://stockanalysis.com/stocks/{}/market-cap/"
ANYS = ("https://www.businesswire.com/news/home/20211208005269/en/Anyscale-Secures-%24100M-Series-C-at-%241B-Valuation-"
        "to-Radically-Simplify-Scaling-and-Productionizing-AI-Applications")
ANTR = "https://venturebeat.com/business/meet-the-startup-using-ai-to-slash-healthcares-trillion-dollar-administrative-burden"
AURL = "https://techcrunch.com/2025/08/27/911-centers-are-so-understaffed-theyre-turning-to-ai-to-answer-calls/"
ASMB = "https://techcrunch.com/2022/05/26/customer-support-management-platform-assembled-lands-51m/"
ARRIS = "https://www.webwire.com/ViewPressRel.asp?aId=257824"
AUG = "https://www.august.law/blog/august-raises-7m-to-deliver-configurable-legal-ai-to-midsize-firms-globally"
AQB_A = "https://www.finsmes.com/2019/06/aquabyte-raises-10m-in-series-a-financing.html"
AQB_S = "https://www.finsmes.com/2018/01/aquabyte-raises-3-5m-in-seed-funding.html"

L = [
    cls("amerigroup-corporation", country="US", city="Virginia Beach", rng="below_1b",
        stage="Series A", stage_src="model", stage_conf="low", stage_cite=AGP, entry_date="1994-12",
        focus="Healthcare & Bio",
        rounds=[rnd(None, "Series A", None, None, None, AGP, "filing"),
                rnd(None, "Series B", None, None, None, AGP, "filing"),
                rnd(None, "Series C", None, None, None, AGP, "filing")],
        note="Medicaid managed-care company in Virginia Beach, acquired by WellPoint in 2012. The 2001 S-1/A has NEA's "
             "Charles Newhall on the board since the company's formation in December 1994 and lists Series A as its first "
             "preferred, but gives no issue date, so the Series A entry is inferred at low confidence."),

    cls("amicus-therapeutics", status="acquired", rng="below_1b", city="Princeton", focus="Healthcare & Bio",
        flags=["model_disputes_source"],
        note="BioMarin completed its $4.8B acquisition of Amicus on 2026-04-27 (PR Newswire) and FOLD was delisted, so the "
             "prefilled public status and float no longer apply. Princeton headquarters (EDGAR)."),

    cls("amisys-managed-care", status="acquired", rng="below_1b", country="US", city="Rockville",
        stage="undetermined", entry_date="1994", focus="Healthcare & Bio", rounds=[],
        note="Managed-care information systems company in Rockville (EDGAR), listed on Nasdaq and acquired by HBO & Company "
             "(later McKesson HBOC), as the Greylock row reads. No source names NEA's 1994 round."),

    cls("amplitude", status="acquired", rng="below_1b", country="US", stage="undetermined", entry_date="1997",
        focus="SaaS", flags=["model_disputes_source", "identity_homonym", "city_unknown"], rounds=[],
        note="NEA's Amplitude is the 1990s web calendaring software company acquired by Critical Path (the firm's page), "
             "not the Nasdaq-listed analytics company Amplitude Inc.; the prefilled public float and the sibling rows belong "
             "to that namesake. No source found places this company's city or names NEA's 1997 round."),

    cls("amplyx-pharmaceuticals", status="acquired", rng="below_1b", city="San Diego", focus="Healthcare & Bio",
        note="Antifungal drug developer in San Diego (Form D address), acquired by Pfizer per the firm's exit line."),

    cls("aneurx", status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined",
        entry_date="1995", focus="Healthcare & Bio", rounds=[],
        note="Endovascular aneurysm stent-graft maker acquired by Medtronic (the firm's exit line). No source names NEA's "
             "1995 round."),

    cls("annexon", country="US", city="Brisbane", stage="Growth", stage_src="web_verified", stage_conf="high",
        stage_cite=ANNX, entry_date="2016-06", focus="Healthcare & Bio",
        rounds=[rnd("2016-06", "Series B", 44600000, None, True, ANNX, "filing"),
                rnd("2018-12", "Series C", None, None, None, ANNX, "filing")],
        note="The 2019 registration statement says entities affiliated with NEA became 5% holders at the June 2016 Series B "
             "($44.6M in two closings) and that NEA 15 designated a director, matching the firm's 2016 entry. Public "
             "(Nasdaq: ANNX, $801M on 2026-09-30); now based in Brisbane, California."),

    cls("antenna-software", status="acquired", rng="below_1b", country="US", city="Jersey City",
        stage="undetermined", entry_date="2009", focus="SaaS", flags=["model_disputes_source"], rounds=[],
        note="Mobile application platform headquartered in Jersey City, New Jersey, acquired by Pegasystems in October 2013 "
             "for $27.7M (Wikipedia); the GB country was a one-word name match. No source names NEA's 2009 round."),

    cls("anterior", status="private", rng="below_1b", country="US", city="New York",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ANTR, entry_date="2024-07",
        focus="Healthcare & Bio",
        rounds=[rnd("2024-07", "Series A", 20000000, "NEA", True, ANTR, "press"),
                rnd("2026-02-12", "unnamed", 40000000, None, None,
                    "https://www.fiercehealthcare.com/ai-and-machine-learning/payer-ai-company-anterior-banks-40m-funding-round",
                    "press")],
        note="NEA led the $20M Series A with Sequoia as an existing investor (VentureBeat, July 2024), so the Sequoia row's "
             "'Sequoia led the A' does not match the press. A $40M round followed in February 2026 (Fierce Healthcare) with "
             "no $1B valuation reported; New York per the firm's post."),

    cls("antimatter", status="acquired", rng="below_1b", country="US",
        stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=jl.POST("antimatter-pioneering"),
        entry_date="2022-03", focus="Security", flags=["city_unknown"],
        rounds=[rnd("2022-03", "Series A", 12000000, "NEA", True, jl.POST("antimatter-pioneering"), "firm")],
        note="NEA led Antimatter's $12M Series A (the firm's March 2022 post; TechCrunch). Databricks acquired the company in "
             "a deal that closed in 2025 and was disclosed in March 2026 (TechCrunch); no source places its city."),

    cls("anulex-technologies-inc", status="defunct", rng="below_1b", country="US", city="Minnetonka",
        stage="undetermined", entry_date="2001", focus="Healthcare & Bio",
        rounds=[rnd("2009-05-05", "unnamed (Form D)", 10644751, None, None, jl.FORMD_CITE("anulex-technologies-inc", 0), "filing"),
                rnd("2010-05-21", "unnamed (Form D)", 20000000, None, None, jl.FORMD_CITE("anulex-technologies-inc", 2), "filing")],
        note="Minnetonka annulus-repair device company; Orthopedics This Week reported in 2018 that Anulex had died. NEA's "
             "2001 entry predates its Form Ds and no source names that round."),

    cls("anyscale", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=ANYS,
        asof="2021-12", city="San Francisco", focus="AI & Applied AI", flags=["stale"],
        extra={"valuation_range_source": "web_verified"},
        note="Ray compute platform, San Francisco. Last priced mark is the December 2021 $100M Series C at a $1B valuation "
             "(Business Wire), as the a16z row reads; older than 24 months, so flagged stale."),

    cls("apnex-medical-inc", status="unknown", rng="below_1b", city="Saint Paul", stage="undetermined",
        focus="Healthcare & Bio",
        rounds=[rnd("2009-11-18", "unnamed (Form D)", 19050000, None, None, jl.FORMD_CITE("apnex-medical-inc", 0), "filing"),
                rnd("2011-09-26", "unnamed (Form D)", 35000000, None, None, jl.FORMD_CITE("apnex-medical-inc", 1), "filing")],
        note="Hypoglossal nerve stimulation company in St. Paul (formerly Prospex Medical II), last traced in 2011 trial "
             "coverage; no source found for its later fate, so status is unknown and NEA's round is not named."),

    cls("appian", status="public", rng="1b_plus", usd=2520000000, val_src="web_verified", val_cite=SA.format("appn"),
        asof="2026-09-30", city="McLean", focus="SaaS", extra={"valuation_range_source": "web_verified"},
        note="Low-code platform listed on Nasdaq (APPN), market cap $2.52B on 2026-09-30 (stockanalysis.com); "
             "headquartered in McLean, Virginia."),

    cls("applied-imaging-corp", status="acquired", rng="below_1b", country="US", city="San Jose",
        stage="undetermined", focus="Healthcare & Bio", rounds=[],
        note="Automated cytogenetics imaging company in San Jose (EDGAR), Nasdaq-listed and later acquired by Genetix. NEA "
             "reported a 16.9% stake from 1997, but no source names the round it entered or its year."),

    cls("applix", status="acquired", rng="below_1b", country="US", city="Westborough", stage="undetermined",
        entry_date="1983", focus="SaaS", rounds=[],
        note="Westborough, Massachusetts software company acquired by Cognos on 2007-10-25 (Wikipedia). No source names "
             "NEA's 1983 round."),

    cls("apprenda-inc", status="defunct", rng="below_1b", city="Troy", stage="undetermined", entry_date="2009",
        focus="DevTools & APIs",
        rounds=[rnd("2013-11", "Series C", 16000000, None, None, jl.FORMD_CITE("apprenda-inc", 0), "filing"),
                rnd("2015-07-10", "unnamed (Form D)", 19999989, None, None, jl.FORMD_CITE("apprenda-inc", 1), "filing")],
        note="Troy, New York private-PaaS company that stopped operating in July 2018 and then tried to sell its assets "
             "(Business Insider, Times Union); no sale reported. NEA's 2009 entry is not named by any source."),

    cls("appriva-medical", status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined",
        entry_date="2000", focus="Healthcare & Bio", rounds=[],
        note="Left atrial appendage occlusion device company acquired by Microvena (ev3), per the firm's exit line. No "
             "source names NEA's 2000 round."),

    cls("appsheet", status="acquired", rng="below_1b", city="Bellevue", city_src="formd_address",
        stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=jl.W("AppSheet"), entry_date="2015",
        focus="SaaS",
        rounds=[rnd("2015", "Seed", None, "NEA", True, jl.W("AppSheet"), "press"),
                rnd("2019-04-10", "unnamed (Form D)", 19335060, None, None,
                    "https://www.sec.gov/Archives/edgar/data/1774214/000177421419000001/0001774214-19-000001-index.htm", "filing")],
        note="Wikipedia and the firm's own Seed label agree NEA provided the 2015 seed; Google acquired the no-code app "
             "platform in January 2020, and its 2019 Form D gave Bellevue. Graduation left for the graduation pass."),

    cls("aquabyte", status="acquired", rng="below_1b", city="San Francisco",
        stage="Seed", stage_src="first_party", stage_conf="medium", stage_cite=jl.SITE("aquabyte"), entry_date="2018-01",
        grad="graduated", grad_src="web_verified", grad_cite=AQB_A, grad_conf="high",
        focus="AI & Applied AI",
        rounds=[rnd("2018-01-30", "Seed", 3500000, None, True, AQB_S, "press"),
                rnd("2019-06-11", "Series A", 10000000, None, None, AQB_A, "press"),
                rnd("2022-07", "unnamed", 25000000, None, None, None, "press")],
        note="The firm labels its entry Seed and announced the investment on 2018-01-30 alongside the $3.5M seed "
             "(FinSMEs); the $10M Series A of June 2019 graduates it. An investment firm bought a majority of the "
             "computer-vision aquaculture company in December 2025 (IntraFish; the firm's page names Vitruvian)."),

    cls("aquantia", city="Milpitas", rng="below_1b", focus="Industrial & Robotics",
        note="Ethernet chip company in Milpitas (Form D address), acquired by Marvell in 2019; the Greylock and Lightspeed rows agree."),

    cls("aradigm-corporation", country="US", city="Hayward", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ARDM, entry_date="2001-08",
        focus="Healthcare & Bio",
        rounds=[rnd("2001-08-21", "PIPE", None, None, True, ARDM, "filing")],
        note="NEA 10 bought common stock and warrants in Aradigm's August 2001 private placement (securities purchase "
             "agreement), five years after its 1996 listing: an X1 row, Growth only if Erik rules a PIPE a venture entry. "
             "Hayward company, acquired after its 2019 bankruptcy as the sibling rows read."),

    cls("arcellx", status="acquired", rng="below_1b", city="Redwood City", focus="Healthcare & Bio",
        flags=["model_disputes_source"],
        note="Gilead completed its $7.8B acquisition of Arcellx on 2026-04-28 and ACLX was delisted (stockanalysis.com, "
             "Stock Titan), so the prefilled public status and mark no longer apply. Redwood City headquarters (EDGAR)."),

    cls("arcsight", status="acquired", rng="below_1b", city="Cupertino",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ARST, entry_date="2005-08-17",
        focus="Security",
        rounds=[rnd("2005-08-17", "secondary (Series A preferred)", None, None, True, ARST, "filing")],
        note="ArcSight's 2007 SEC correspondence says NEA had no prior relationship and on 2005-08-17 bought 4,350,000 "
             "Series A preferred shares from an early investor at about $1.88: a secondary, so Growth. Cupertino security "
             "software company acquired by Hewlett-Packard in 2010."),

    cls("ardelyx", city="Waltham", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=ARDX,
        entry_date="2008", focus="Healthcare & Bio",
        rounds=[rnd(None, "Series A", 28764000, None, True, ARDX, "filing"),
                rnd("2011", "Series B", None, None, True, ARDX, "filing")],
        note="Founded October 2007 as Nteryx; the 2014 registration statement shows NEA 12 holding 52.4M shares against 39.6M "
             "bought in the Series B, so it also holds Series A, the company's first preferred, matching the firm's 2008 "
             "entry. Now headquartered in Waltham; $852M market cap on 2026-09-30 (stockanalysis.com)."),

    cls("argon-networks", status="acquired", rng="below_1b", country="US", city="Littleton", stage="undetermined",
        entry_date="1998", focus="Data Infrastructure", rounds=[],
        note="Littleton, Massachusetts router maker acquired by Siemens in 1999, as the Greylock row reads. No source names "
             "NEA's 1998 round."),

    cls("arkestro", status="private", rng="below_1b", city="San Francisco",
        stage="Series A", stage_src="model", stage_conf="medium",
        stage_cite="https://www.businessinsider.com/arkestro-series-a-pitch-deck-supply-chain-procurement-automation-2022-6",
        focus="SaaS", flags=["stage_disputes_band"],
        rounds=[rnd("2022-06", "Series A", 26000000, None, None,
                    "https://www.businessinsider.com/arkestro-series-a-pitch-deck-supply-chain-procurement-automation-2022-6", "press"),
                rnd("2025-05-14", "strategic", 36000000, "Altira Group, Aramco Ventures", True,
                    "https://www.prnewswire.com/news-releases/arkestro-secures-36m-in-strategic-investment-to-accelerate-predictive-procurement-innovation-302454539.html",
                    "company")],
        note="Procurement software company in San Francisco. NEA's 2022 entry is the May 2022 Form D round with NEA's Jeff "
             "Immelt as director, which the press names the $26M Series A (Business Insider headline, June 2022), so the Form D "
             "band's Growth is disputed; NEA was an existing investor in the May 2025 $36M round, no mark near $1B."),

    cls("aronex-pharmaceuticals-inc", status="acquired", rng="below_1b", country="US", city="The Woodlands",
        stage="undetermined", focus="Healthcare & Bio", rounds=[],
        note="The Woodlands, Texas oncology drug company (EDGAR) that merged into Antigenics in 2001; NEA reported a "
             "stake in 2000, and no source names the round or year it entered."),

    cls("arris", status="private", rng="below_1b", country="US", city="Berkeley",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ARRIS, entry_date="2019-01",
        focus="Industrial & Robotics", flags=["model_disputes_source"],
        rounds=[rnd("2019-01", "Series A", 10000000, "NEA", True, ARRIS, "company"),
                rnd("2020-04", "Series B", 48500000, "Taiwania Capital", True, ARRIS, "company")],
        note="Arris Composites, Berkeley: NEA led its $10M Series A in January 2019 and returned in the $48.5M Series B "
             "(company release, April 2020). Still private; the prefilled acquired status was a name match to ARRIS International."),

    cls("ascend-communications", status="acquired", rng="below_1b", city="Alameda", stage="undetermined",
        entry_date="1990", focus="Data Infrastructure", rounds=[],
        note="Remote-access networking company in Alameda acquired by Lucent in 1999; Wikipedia names NEA among its initial "
             "investors but no round, so the stage stays undetermined as in the Greylock and Menlo rows."),

    cls("aspect-medical", status="acquired", rng="below_1b", country="US", city="Norwood", stage="undetermined",
        entry_date="1989", focus="Healthcare & Bio", rounds=[],
        note="Anesthesia-monitoring (BIS) company founded 1987 and acquired by Covidien in 2009 for $210M (Wikipedia). No "
             "source names NEA's 1989 round."),

    cls("assembled", status="private", rng="below_1b", country="US", city="San Francisco",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ASMB, entry_date="2022-05",
        focus="SaaS", flags=["model_disputes_source"],
        rounds=[rnd("2022-05-26", "Series B", 51000000, "NEA", True, ASMB, "press")],
        note="NEA led the $51M Series B of the San Francisco support-operations software company (TechCrunch, 2022-05-26); "
             "the SG country was a one-word name match. The YC row named Assembled is a different company (W11, TenXList)."),

    cls("astral-point", status="acquired", rng="below_1b", country="US", city="Chelmsford", stage="undetermined",
        entry_date="1998", focus="Data Infrastructure", rounds=[],
        note="Optical (WDM) switching company acquired by Alcatel, per the firm's exit line. No source names NEA's 1998 round."),

    cls("astrowatt", status="unknown", rng="below_1b", city="Round Rock", city_src="formd_address",
        stage="undetermined", entry_date="2009", focus="Climate & Energy",
        rounds=[rnd("2009-03-05", "unnamed (Form D)", 1600000, None, None, jl.FORMD_CITE("astrowatt", 0), "filing"),
                rnd("2010-07-06", "unnamed (Form D)", 5128350, None, None, jl.FORMD_CITE("astrowatt", 1), "filing")],
        note="Thin-silicon solar start-up filing from Round Rock, Texas; incorporated 2006, so the 2009 filing may not be its "
             "first round and the Form D seed band stays withheld. No later trace of the company was found."),

    cls("atheros-communications", country="US", city="San Jose", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ATHR, entry_date="2000-03",
        focus="Industrial & Robotics",
        rounds=[rnd("1998-12", "Series A", 12050000, None, False, ATHR, "filing"),
                rnd("2000-03", "Series B", 25589502, None, True, ATHR, "filing"),
                rnd("2001-04", "Series C", 66670856, None, True, ATHR, "filing")],
        note="The 2003 S-1 shows NEA 9 buying 4,329,292 Series B shares (March 2000, $3.335) and none of the Series A, so "
             "the firm's Growth label holds. Wireless chip company acquired by Qualcomm in 2011, San Jose by then."),

    cls("attest", status="private", rng="below_1b", country="GB", country_src="web_verified",
        country_cite=jl.POST("powering-real-time-insights"), city="London",
        stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=jl.POST("powering-real-time-insights"),
        entry_date="2019-05", focus="SaaS",
        rounds=[rnd("2019-05-06", "Series A", 16000000, "NEA", True, jl.POST("powering-real-time-insights"), "firm")],
        note="The firm's post of 2019-05-06 says NEA led a $16M Series A in London-based Attest, a consumer research platform."),

    cls("audience", country="US", city="Mountain View", rng="below_1b",
        stage="Growth", stage_src="model", stage_conf="medium", stage_cite=ADNC, entry_date="2006-04",
        focus="Industrial & Robotics", flags=["model_disputes_source"],
        rounds=[rnd("2009-02", "Series D", 15020887, None, True, ADNC, "filing"),
                rnd("2010-02", "Series E", 15161075, None, True, ADNC, "filing")],
        note="Voice-processor chip company founded in 2000 in Mountain View (S-1); NEA 11 and NEA Ventures 2006 entered with "
             "Forest Baskett joining the board in April 2006, after the earlier preferred rounds, so a Growth entry; "
             "acquired by Knowles in 2015. The DK country was a one-word name match."),

    cls("august", status="private", rng="below_1b", city="New York", stage="undetermined", entry_date="2025-08",
        focus="AI & Applied AI",
        rounds=[rnd("2025-08", "unnamed", 7000000, "NEA and Pear VC", True, AUG, "company")],
        note="Legal AI for midsize law firms, New York; NEA led a $7M round (company post) that the sources do not name. "
             "Momentum check 2026-09-30: no $1B+ priced round. The a16z row named August is a different company (Tel Aviv fintech)."),

    cls("aurelian", status="private", rng="below_1b", country="US", city="Seattle",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=AURL, entry_date="2025-08-27",
        focus="AI & Applied AI",
        rounds=[rnd("2025-08-27", "Series A", 14000000, "NEA", True, AURL, "press")],
        note="NEA led the $14M Series A of the Seattle 911-call AI company (TechCrunch, 2025-08-27), after its YC S22 start. "
             "Momentum check 2026-09-30: no $1B+ priced round."),

    cls("aurinia-pharmaceuticals", country="CA", country_src="web_verified", country_cite=AUPH_ADDR, city="Edmonton",
        rng="1b_plus", usd=2170000000, val_src="web_verified", val_cite=SA.format("auph"), asof="2026-09-30",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=AUPH, entry_date="2014-02",
        focus="Healthcare & Bio", extra={"valuation_range_source": "web_verified"},
        rounds=[rnd("2014-02-14", "PIPE", 52000000, "venBio, NEA and others", True, AUPH, "filing")],
        note="NEA co-led the $52M private placement Aurinia completed on 2014-02-14 while listed on the TSX: an X1 row, "
             "Growth only if Erik rules a PIPE a venture entry. Market cap $2.17B on 2026-09-30 (stockanalysis.com); "
             "Edmonton principal office (EDGAR)."),

    cls("aurora-biosciences-corporation", status="acquired", rng="below_1b", country="US", city="San Diego",
        stage="undetermined", focus="Healthcare & Bio", rounds=[],
        note="San Diego drug-screening company (EDGAR), merged into Vertex in 2001; NEA reported a stake in 1998-99, and no "
             "source names the round or year it entered."),

    cls("automation-anywhere", city="San Jose", focus="SaaS",
        note="Robotic process automation company headquartered in San Jose (Wikipedia)."),

    cls("availink", status="private", rng="below_1b", country="CN", country_src="web_verified",
        country_cite="http://www.availink.com/", city="Beijing", stage="undetermined", entry_date="2005",
        focus="Industrial & Robotics", rounds=[],
        note="Fabless digital-TV chip company founded in 2005, listed by the firm with its China practice; its own site "
             "gives a Beijing telephone number. No source names NEA's 2005 round."),

    cls("avenzo", status="private", rng="below_1b", country="US", city="San Diego",
        stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=AVZ, entry_date="2024-02",
        focus="Healthcare & Bio", flags=["stage_disputes_band"],
        rounds=[rnd("2024-02", "Series A (second tranche)", 68500000, None, False, AVZ, "filing"),
                rnd("2024-02", "Series A-1", 115300000, None, True, AVZ, "filing"),
                rnd("2025-08", "Series B", 60300000, None, True, AVZ, "filing")],
        note="Rallybio's 2026 S-4/A shows NEA 18 Venture Growth Equity buying $20.0M of Avenzo's Series A-1 in the "
             "February-March 2024 closings, a round named Series A, so the firm's Growth label is overridden. The reverse "
             "merger into Rallybio was still pending in September 2026, so Avenzo reads private."),

    cls("aveo-oncology", status="acquired", rng="below_1b", country="US", city="Boston",
        stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=AVEO, entry_date="2016-05",
        focus="Healthcare & Bio",
        rounds=[rnd("2016-05-13", "PIPE", 17025000, None, True, AVEO, "filing")],
        note="NEA entered through AVEO's May 2016 private placement (registration rights agreement naming NEA's vehicle), "
             "long after its 2010 listing: an X1/R2 row, Growth only if Erik rules a PIPE a venture entry. Boston company "
             "acquired by LG Chem in January 2023."),
]

jl.write("c1b", L)
