"""PRO-80 Bessemer Venture Partners, judge j03, queue batch 6 part 2 (intacct .. leaner-technologies):
classification of listed members. None is excluded in this file."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, ARCH, POST, W, NEWS, FORMD_CITE

GL = "Graduation left for the graduation pass."
# URLs printed by tools run in this session (secget and the EDGAR full-text listing, NEWS decode, WebFetch reads)
S1_KYMERA = "https://www.sec.gov/Archives/edgar/data/1815442/000119312520206645/d940105ds1.htm"
LEANER_SITE = "https://leaner.co.jp/"
NC_INTIGUA = NEWS("intigua", "NoCamels")
PR_IRIS = NEWS("iris-automation", "Closes $13 Million")
P2_JINGLE = NEWS("jingle", "$2.9 Million")
FS_KANDOU = NEWS("kandou", "Raises $92.3M")
TNW_KANDOU = NEWS("kandou", "The Next Web")
PY_KENNA = NEWS("kenna-security", "PYMNTS")
TC_KINDRED = NEWS("kindred", "Opendoor alums")
FS_KINDRED = NEWS("kindred", "Kindred Raises $15M Series A Funding")
TFN_KINDRED = NEWS("kindred", "Tech Funding News")
FB_LD = NEWS("launchdarkly", "Hits $3 Billion")
HZ_LEABA = NEWS("leaba-semiconductor", "Haaretz")

L = []

# ---- Intacct
L.append(cls("intacct", status="acquired", rng="below_1b", city="San Jose", stage="Growth",
             stage_src="web_verified", stage_cite=W("Sage Intacct"), stage_conf="medium", entry_date="2008-03-31",
             focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2000", "Series A", 10000000, "HWVP", False, W("Sage Intacct"), "press"),
                     rnd("2008-03", "later round", None, "Bessemer Venture Partners", True, W("Sage Intacct"),
                         "press"),
                     rnd("2010-06", "unnamed (Form D)", 3000000, None, True, FORMD_CITE("intacct", 0), "filing"),
                     rnd("2014-02", "unnamed (Form D)", 30000000, None, True, FORMD_CITE("intacct", 3), "filing")],
             note="Cloud accounting software, San Jose (as in the Battery and Sutter Hill books); acq. by The Sage "
                  "Group, 2017. Wikipedia: the Series A was raised in 2000 from HWVP, and the rounds from 2001 to "
                  "2014 were led by Battery, BVP, Sigma and Emergence; the firm's own listing dates its investment "
                  "2008-03-31, eight years after the Series A, so the entry is a later round (Growth) and the Seed "
                  "band read off the $3M Form D of 2010 is disputed. Not a Seed entry, so no graduation."))

# ---- Intego
L.append(cls("intego", status="acquired", rng="below_1b", city="Seattle", stage="undetermined",
             entry_date="2007-06-06", focus="Security", rounds=[],
             note="Mac security software, founded in Paris in 1997 and run from Seattle and Austin (Wikipedia); acq. "
                  "by Kape Technologies, 2018. The firm's own listing dates its investment 2007-06-06 and names no "
                  "round; a Google News query on 2026-10-01 returned no funding report."))

# ---- Intigua
L.append(cls("intigua", status="unknown", rng="below_1b", city="Newton", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2012-11-29", focus="Data Infrastructure",
             rounds=[rnd("2013-01", "Series A", 8600000, "Bessemer Venture Partners", True, NC_INTIGUA, "press"),
                     rnd("2014-05", "unnamed (Form D)", 12000000, None, True, None, "filing")],
             note="Virtualized IT management layer, Newton, Massachusetts, with development in Israel (NoCamels). "
                  "NoCamels (2013-01-21) reports the $8.6M Series A without naming its investors; model: Bessemer "
                  "led it, which matches the firm's own date of 2012-11-29, so the pre-filled 2014 date (the Form D "
                  "of the next round) is replaced. The last trace is a small Form D in late 2018 and the firm's list "
                  "dropped the company after 2019, so its present state is not established."))

# ---- Intucell
L.append(cls("intucell", status="acquired", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=ARCH("intucell"), city="Ra'anana", stage="undetermined", entry_date="2011-01-12",
             focus="Data Infrastructure",
             rounds=[rnd("2011-01", "only venture round, Bessemer the sole investor", None,
                         "Bessemer Venture Partners", True, POST("drivenets-the-ai-networking"), "firm")],
             note="Self-optimizing network software for mobile operators, Ra'anana, Israel; acq. by Cisco, 2013. The "
                  "firm's own post of 2026-06-01 says it backed Intucell 'as a sole investor' and the listing dates "
                  "the investment 2011-01-12; neither names the round, so the stage is undetermined."))

# ---- IPC The Hospitalist
L.append(cls("ipc-the-hospitalist", rng="below_1b", country="US", city="Los Angeles", stage="undetermined",
             entry_date="1997", focus="Healthcare & Bio", rounds=[],
             note="Hospitalist physician group, North Hollywood (Los Angeles); IPO in January 2008, acq. by "
                  "TeamHealth, 2015. The firm's own list gives 1997 and 1998 and names no round; the 2007 S-1 shows "
                  "Bessemer Venture Partners IV and Bessec Ventures IV holding preferred stock without saying which "
                  "series they bought first."))

# ---- Iris Automation
L.append(cls("iris-automation", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2017-12-22",
             focus="Industrial & Robotics",
             rounds=[rnd("2018-01", "Series A", 8000000, "Bessemer Venture Partners", True, None, "press"),
                     rnd("2020-12", "Series B", 13000000, None, True, PR_IRIS, "company")],
             note="Detect-and-avoid systems for drones, San Francisco (the company's 2020 release; as in the YC "
                  "book); acq. by uAvionix, 2023 (the firm's listing). The Series B release of 2020-12-15 names "
                  "Bessemer a follow-on investor; model: Bessemer led the $8M Series A announced in January 2018, "
                  "which matches the firm's own date of 2017-12-22."))

# ---- iSIGHT Security
L.append(cls("isight-security", status="acquired", rng="below_1b", country="US", city="Dallas", stage="Growth",
             stage_src="model", stage_conf="medium", entry_date="2014", focus="Security",
             rounds=[rnd("2015-01", "Series C", 30000000, "Bessemer Venture Partners", True, None, "press")],
             note="iSIGHT Partners, cyber threat intelligence, Dallas; acq. by FireEye, 2016. Model: Bessemer made "
                  "the $30M Series C investment announced in January 2015 (the firm's own year reads 2014); two "
                  "Google News queries on 2026-10-01 returned no report to cite."))

# ---- ISIS Pharmaceuticals (Ionis)
L.append(cls("isis-pharmaceuticals", country="US", city="Carlsbad", stage="undetermined", entry_date="1989",
             focus="Healthcare & Bio", rounds=[],
             note="Antisense drug developer, Carlsbad, renamed Ionis Pharmaceuticals in 2015 (NASDAQ: IONS, market "
                  "cap $7.41B on 2026-10-01, StockAnalysis, the same band as the pre-filled figure). The firm's own "
                  "list: Chris Gabrieli 'invested in and served as Chairman of Isis', and the 2001 proxy calls him "
                  "a founder and a director from January 1989; no round is named, so the stage is undetermined. "
                  "This row and the base row ionis-pharmaceuticals are one company."))

# ---- Jasper
L.append(cls("jasper", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified",
             val_cite=POST("how-jasper"), asof="2022-10", country="US", city="Austin", stage="Series A",
             stage_src="first_party", stage_cite=POST("how-jasper"), stage_conf="high", entry_date="2022-10",
             focus="AI & Applied AI", flags=["stale"],
             rounds=[rnd("2022-10", "Series A", 125000000, "Insight Partners", True, POST("how-jasper"), "firm")],
             extra={"valuation_range_source": "web_verified"},
             note="AI content platform for marketing teams, Austin (as in the Coatue, Insight and IVP books). The "
                  "firm's own post of 2022-10-18: Bessemer's growth practice joins the $125 million Series A at a "
                  "$1.5 billion valuation; the mark is older than 24 months, and the 2023 report of a lower "
                  "internal valuation was not a priced event. The former-unicorn record on the row and the "
                  "Northzone and Sequoia rows are another Jasper (Jasper Technologies, bought by Cisco in 2016)."))

# ---- Jingle
L.append(cls("jingle", status="private", rng="below_1b", country="US", stage="Seed", stage_src="web_verified",
             stage_cite=P2_JINGLE, stage_conf="high", entry_date="2023-10", focus="Consumer & Marketplaces",
             flags=["city_unknown"],
             rounds=[rnd("2023-10", "Seed", 2900000, "Bessemer Venture Partners", True, P2_JINGLE, "press")],
             note="Mobile stores that bring local vendors' goods to neighborhoods. Pulse 2.0 (2023-10-11): a $2.9M "
                  "seed led by Bessemer Venture Partners; it places the company in the San Francisco Bay Area "
                  "without naming the city. " + GL))

# ---- K2 Integrity
L.append(cls("k2-integrity", status="private", rng="below_1b", country="US", city="New York", stage="undetermined",
             entry_date="2010", focus="Security", rounds=[],
             note="Risk, investigations and compliance advisory firm founded by Jules Kroll as K2 Intelligence, New "
                  "York (Wikipedia). The firm's own year is 2010 and it names no round; a Google News query on "
                  "2026-10-01 returned no funding report."))

# ---- Kandou
L.append(cls("kandou", status="private", rng="below_1b", country="CH", country_src="web_verified",
             country_cite=FS_KANDOU, city="Lausanne", stage="undetermined", entry_date="2016-06-15",
             focus="Industrial & Robotics",
             rounds=[rnd("2020-11", "Series C", 92300000, "Bessemer Venture Partners", True,
                         FS_KANDOU, "press"),
                     rnd("2021-12", "Series D", 75000000, None, None, None, "press"),
                     rnd("2026-03", "$225M round at a $400M valuation", 225000000, "Maverick Silicon", False,
                         TNW_KANDOU, "press")],
             note="Chip-to-chip interconnect technology, Lausanne (FinSMEs). The firm's own listing dates its "
                  "investment 2016-06-15; FinSMEs (2020-11-17) has Bessemer leading the existing investors in the "
                  "Series C, but no source read names the 2016 round. Value check 2026-10-01: the $225M round of "
                  "March 2026 valued Kandou AI at $400M (The Next Web), below $1B."))

# ---- Kenna Security
L.append(cls("kenna-security", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="Growth", stage_src="web_verified", stage_cite=PY_KENNA, stage_conf="high", entry_date="2018-03",
             focus="Security",
             rounds=[rnd("2018-03", "Series C", 25000000, "Bessemer Venture Partners", True, PY_KENNA, "press"),
                     rnd("2019-09", "$48M round", 48000000, None, None, None, "press")],
             note="Risk-based vulnerability management, San Francisco; acq. by Cisco, 2021. PYMNTS (2018-03-30): "
                  "$25 million in Series C funding, Bessemer Venture Partners leading; the firm's own date is "
                  "2018-03-09."))

# ---- Keynote
L.append(cls("keynote", rng="below_1b", country="US", city="San Mateo", stage="Series A", stage_src="first_party",
             stage_cite=ARCH("keynote"), stage_conf="high", entry_date="1997", focus="Data Infrastructure",
             rounds=[rnd("1997", "Series A", None, "Bessemer Venture Partners", True, ARCH("keynote"), "firm")],
             note="Keynote Systems, internet performance measurement, San Mateo. The firm's own listing: in 1997 "
                  "BVP's David Cowan led the Series A round in Keynote; IPO in 1999 (NASDAQ: KEYN), then acq. by "
                  "Thoma Bravo, 2013, and merged with Dynatrace in 2015."))

# ---- Kindred
L.append(cls("kindred", status="private", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="web_verified", stage_cite=TC_KINDRED, stage_conf="high", entry_date="2022-04",
             grad="graduated", grad_src="web_verified", grad_cite=FS_KINDRED, grad_conf="high",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2022-04", "Seed", 7750000, "Andreessen Horowitz", True, TC_KINDRED, "press"),
                     rnd("2023-04", "Series A", 15000000, "New Enterprise Associates", True, FS_KINDRED, "press"),
                     rnd("2026-02", "Series B and Series C, announced together", 125000000,
                         "NEA and Dylan Field; Index Ventures", None, TFN_KINDRED, "press")],
             note="Home swapping network (livekindred.com), San Francisco (as in the a16z and NEA books). TechCrunch "
                  "(2022-04-21): a $7.75M seed led by Andreessen Horowitz with Bessemer Venture Partners "
                  "participating. Graduated: the $15M Series A of April 2023 led by NEA, Bessemer among the "
                  "existing backers (FinSMEs). Value check 2026-10-01: the $125M Series B and C announced in "
                  "February 2026 carried no disclosed valuation (Tech Funding News), so below_1b under Rule A. The "
                  "First Round and GV rows named Kindred are another company (Kindred AI, robotics)."))

# ---- Klook
L.append(cls("klook", country="HK", country_src="web_verified", country_cite=W("Klook (company)"),
             city="Hong Kong", stage="Growth", stage_src="web_verified", stage_cite=W("Klook (company)"),
             stage_conf="high", entry_date="2023-12", focus="Consumer & Marketplaces",
             flags=["model_disputes_source"],
             rounds=[rnd("2023-12", "Series E+", 210000000, "Bessemer Venture Partners", True, W("Klook (company)"),
                         "press")],
             note="Travel experiences booking platform based in Hong Kong (Wikipedia; as in the TCV book), not "
                  "mainland China as the pre-filled name match read. Wikipedia: the US$210 million Series E+ of "
                  "December 2023 was led by Bessemer Venture Partners, the firm's partnered year. Klook filed for a "
                  "US listing in November 2025 and delayed it into 2026 (Business Times, 2025-12-02); it had not "
                  "listed by 2026-10-01, so the private status stands."))

# ---- Knewton
L.append(cls("knewton", status="acquired", rng="below_1b", city="New York", stage="Growth",
             stage_src="web_verified", stage_cite=W("Knewton"), stage_conf="medium", entry_date="2009-03-30",
             focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2008", "first round", 2500000, "Accel Partners", False, W("Knewton"), "press"),
                     rnd("2009-04", "second round", 6000000, "Bessemer Venture Partners", True, W("Knewton"),
                         "press"),
                     rnd("2010-04", "third round", 12500000, "FirstMark Capital", True, W("Knewton"), "press")],
             note="Adaptive learning technology, New York; Wiley bought its assets in 2019. Wikipedia: after a $2.5M "
                  "first round from Accel and others, the $6 million round of April 2009 was led by Bessemer Venture "
                  "Partners with returning investors, which matches the firm's own date of 2009-03-30; a second "
                  "round, so Growth, and the Series A band read off the 2010 Form D is disputed."))

# ---- Kroll Bond Rating Agency
L.append(cls("kroll-bond-rating-agency", status="acquired", rng="below_1b", city="New York",
             focus="Fintech & Payments",
             note="Credit rating agency (KBRA), New York. The firm's own listing: acq. by Wharf Street Ratings, 2015 "
                  "(its exit year); the agency continues to operate under later owners."))

# ---- Kymera Therapeutics
L.append(cls("kymera-therapeutics", country="US", city="Watertown", stage="Growth", stage_src="web_verified",
             stage_cite=S1_KYMERA, stage_conf="high", entry_date="2018-11", focus="Healthcare & Bio",
             rounds=[rnd("2017", "Series A", None, "Atlas Venture", False, S1_KYMERA, "filing"),
                     rnd("2018-11", "Series B", 65000000, None, True, S1_KYMERA, "filing"),
                     rnd("2020-03", "Series C", None, None, None, S1_KYMERA, "filing")],
             note="Targeted protein degradation biotech, Watertown, Massachusetts; NASDAQ: KYMR since 2020 (market "
                  "cap $9.5B on 2026-10-01, StockAnalysis, the same band as the pre-filled figure). The S-1: the "
                  "Bessemer funds bought $10.0M of the Series B convertible preferred stock sold in November 2018, "
                  "when Andrew Hedin joined the board, and its related-party tables name them in no earlier financing "
                  "(the 2017 seed and Series A units went to Atlas Venture), so the entry is Growth."))

# ---- LaunchDarkly
L.append(cls("launchdarkly", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified",
             val_cite=FB_LD, asof="2021-08", city="Oakland", stage="Growth", stage_src="first_party",
             stage_cite=POST("bessemer-series-c-investment-launchdarkly"), stage_conf="high", entry_date="2019-03",
             focus="DevTools & APIs", flags=["stale"],
             rounds=[rnd("2019-03", "Series C", 44000000, "Bessemer Venture Partners", True,
                         POST("bessemer-series-c-investment-launchdarkly"), "firm"),
                     rnd("2021-08", "Series D", 200000000, None, None, FB_LD, "press")],
             extra={"valuation_range_source": "web_verified"},
             note="Feature management platform, Oakland (as in the Insight book). The firm's own post of 2019-03-13: "
                  "Bessemer leads the $44 million Series C, its partnered year. Mark: the $200M round of August "
                  "2021 at $3 billion (Forbes headline), older than 24 months; no later priced round found (Google "
                  "News, 2026-10-01)."))

# ---- Leaba Semiconductor
L.append(cls("leaba-semiconductor", status="acquired", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=HZ_LEABA, city="Caesarea", stage="undetermined", entry_date="2014-08-12",
             focus="Industrial & Robotics", rounds=[],
             note="Networking semiconductor developer, Caesarea, Israel; acq. by Cisco, 2016 (Haaretz headline: Cisco "
                  "acquires Israel's Leaba Semiconductor for $320 million). The firm's own listing dates its "
                  "investment 2014-08-12, the founding year, and names no round; the company announced no funding "
                  "before the sale."))

# ---- Leaner Technologies
L.append(cls("leaner-technologies", status="private", rng="below_1b", country="JP", country_src="web_verified",
             country_cite=LEANER_SITE, city="Tokyo", stage="undetermined", entry_date="2024", focus="SaaS",
             rounds=[],
             note="Procurement and cost management software for Japanese enterprises (leaner.co.jp, the company's "
                  "own Japanese site), Tokyo. The firm's own year is 2024 and it names no round; two Google News "
                  "queries on 2026-10-01 returned no funding report in English."))

jl.write("j03d", L)
