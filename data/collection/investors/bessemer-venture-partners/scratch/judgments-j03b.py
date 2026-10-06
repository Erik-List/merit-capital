"""PRO-80 Bessemer Venture Partners, judge j03, queue batch 5 part 2 (gainsight .. hatch): classification of listed
members, and one control position excluded (gts-central-europe)."""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, SITE, ARCH, POST, W, NEWS, FORMD_CITE

GL = "Graduation left for the graduation pass."
# URLs printed by tools run in this session (NEWS decode, WebSearch and WebFetch reads)
GTS_BUYOUT = ("https://developingtelecoms.com/telecom-business/telecom-trends-forecasts/"
              "1083-private-equity-group-to-take-over-gts-central-europe.html")
CT_GANKSTER = NEWS("gankster", "raises $4.25 million for its")
AW_GIGFINESSE = NEWS("gigfinesse", "Raises $3.6M")
BI_GETACCEPT = NEWS("getaccept", "pitch deck")
FT_GLOSS = NEWS("glossgenius", "latest female-founded unicorn")
BM_GLOSS = NEWS("glossgenius", "Closes a $16.4 Million Series A")
BW_GOODSHIP = NEWS("goodship", "Secures $8M Series A")
EI_MYGLAMM = NEWS("good-glamm-group", "raises $6mn")
ET_GLAMM = NEWS("good-glamm-group", "Inside Good Glamm")
EN_GRAPH = NEWS("graph-ai", "seed round from Bessemer")
FS_GRAPH = NEWS("graph-ai", "Raises $13.3M in Series A Funding")
FB_GUILD = NEWS("guild", "Reaches $4.4 Billion")
PR_HABANA = NEWS("habana-labs", "Secures $75M")
MC_HALTER = NEWS("halter", "led by Peter Thiel")
GN_HASHI = NEWS("hashicorp", "Help Enterprises Adopt")
IV_HATCH = NEWS("hatch", "completes $270 million")
YC_GETACCEPT = "https://www.ycombinator.com/companies/getaccept"

L = []

# ---- Gainsight
L.append(cls("gainsight", status="acquired", rng="below_1b", city="San Francisco", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2014-10-06", focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2013-11", "Series B (Form D)", 21386054, "Bain Capital Ventures", False, None, "filing"),
                     rnd("2014-10", "Series C (Form D)", 25584460, "Lightspeed Venture Partners", True, None, "filing"),
                     rnd("2015-11", "Series D (Form D)", 51699993, None, True, None, "filing")],
             note="Customer success software, San Francisco (as in the Bain Capital Ventures and Lightspeed books); "
                  "acq. by Vista Equity Partners, 2020. The firm's own date, 2014-10-06, is the $25.6M round of "
                  "October 2014, which followed a $21.4M round filed a year earlier; model: that is the Series C led "
                  "by Lightspeed (the Lightspeed book cites the same round as Growth), so the Series A band is "
                  "disputed. A Google News query on 2026-10-01 returned no report to cite."))

# ---- Gamefam
L.append(cls("gamefam", status="private", rng="below_1b", country="US", city="Los Angeles", stage="undetermined",
             entry_date="2020", focus="Media, Gaming & Advertising",
             rounds=[rnd("2022-03", "Series A", 25000000, "Konvoy Ventures", True, W("Gamefam"), "press")],
             note="Developer and publisher of Roblox games, Los Angeles. Wikipedia names Bessemer in the $25M Series A "
                  "of March 2022 led by Konvoy, but the firm's own year is 2020 and no report of a 2020 or 2021 round "
                  "was found (Google News, 2026-10-01), so the entry round is not established."))

# ---- Gankster
L.append(cls("gankster", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_cite=CT_GANKSTER, stage_conf="high", entry_date="2022-12", focus="Media, Gaming & Advertising",
             country="IL", country_src="web_verified", country_cite=CT_GANKSTER, flags=["city_unknown"],
             rounds=[rnd("2022-12", "Seed", 4250000, "Bessemer Venture Partners and Hetz Ventures", True, CT_GANKSTER,
                         "press")],
             note="Team finder and tournament platform for competitive gamers (Gankster Ltd). CTech (2022-12-07): a "
                  "$4.25M seed co-led by Bessemer and Hetz Ventures. The country is read from the Israeli co-lead and "
                  "CTech's coverage, at medium confidence; no source read gives a city. " + GL))

# ---- Gerson Lehrman Group (GLG)
L.append(cls("gerson-lehrman-group-glg", status="private", rng="below_1b", city="New York", stage="undetermined",
             entry_date="2004-01-22", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2015-12", "unnamed (Form D)", 211505646, None, True, None, "filing")],
             note="Expert network, New York. The firm's own listing dates its investment 2004-01-22, so the 2015 "
                  "Form D on which Rob Stavis is a director is a later transaction and the pre-filled Growth entry "
                  "of 2015 is withdrawn; no source read names the 2004 round. GLG filed for an IPO in 2021 and did "
                  "not list; no priced mark of $1B or more was found (Google News, 2026-10-01)."))

# ---- GetAccept
L.append(cls("getaccept", status="private", rng="below_1b", country="SE", country_src="web_verified",
             country_cite=YC_GETACCEPT, city="Malmö", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2020-12", focus="SaaS",
             rounds=[rnd("2020-12", "Series B", 20000000, "Bessemer Venture Partners", True, BI_GETACCEPT, "press")],
             note="Digital sales room and e-signature software, Malmö (YC's directory page; as in the YC book). "
                  "Business Insider (2021-01-06) reports the $20M raised from investors including Bessemer; model: "
                  "that round is the Series B Bessemer led in December 2020, the firm's partnered year."))

# ---- GetInsured
L.append(cls("getinsured", status="private", rng="below_1b", country="US", city="Mountain View",
             stage="undetermined", entry_date="2005", focus="Healthcare & Bio", rounds=[],
             note="Health insurance marketplace technology (Vimo, Inc.), Mountain View. The firm's own year is 2005, "
                  "the founding year; no source read names the round (Google News, 2026-10-01, returned no funding "
                  "report)."))

# ---- GigFinesse
L.append(cls("gigfinesse", status="private", rng="below_1b", city="New York", stage="Seed", stage_src="web_verified",
             stage_cite=AW_GIGFINESSE, stage_conf="high", entry_date="2022", focus="Consumer & Marketplaces",
             rounds=[rnd("2022", "Seed", 3600000, None, True, AW_GIGFINESSE, "press")],
             note="Booking marketplace for independent artists and music venues, New York. AlleyWatch (2022-12-07): a "
                  "$3.6M seed closed in 2022 with Bessemer Venture Partners among the investors. " + GL))

# ---- Ginger
L.append(cls("ginger", status="acquired", rng="below_1b", city="San Francisco", focus="Healthcare & Bio",
             note="On-demand mental health care, San Francisco; merged with Headspace in 2021 to form Headspace "
                  "Health (the firm's listing now points at Headspace), so the row reads acquired. The firm's own "
                  "year reads 2011, the founding year, but its archive first lists the company in 2020 and Steve "
                  "Kraus joins the board on the $50M round of August 2020, so the pre-filled Growth entry stands."))

# ---- Glint
L.append(cls("glint", status="acquired", rng="below_1b", country="US", city="Redwood City", stage="Growth",
             stage_src="model", stage_conf="medium", entry_date="2016-08-15", focus="SaaS",
             rounds=[rnd("2016", "Series C", 27000000, "Bessemer Venture Partners", True, None, "press")],
             note="Employee engagement software, Redwood City; acq. by LinkedIn, 2018. Model: Bessemer led the $27M "
                  "Series C of 2016, which matches the firm's own date of 2016-08-15; a Google News query on "
                  "2026-10-01 returned no report to cite."))

# ---- GlossGenius (now Genius)
L.append(cls("glossgenius", status="private", rng="1b_plus", usd=1150000000, val_src="web_verified",
             val_cite=FT_GLOSS, asof="2026-07", city="New York", stage="Series A", stage_src="web_verified",
             stage_cite=BM_GLOSS, stage_conf="high", entry_date="2021-11", focus="SaaS",
             flags=["stage_disputes_band"],
             rounds=[rnd("2021-11", "Series A", 16400000, "Bessemer Venture Partners", True, BM_GLOSS, "press"),
                     rnd("2022-09", "Series B", 25000000, None, None, None, "press"),
                     rnd("2023-07", "Series C", 28000000, None, True, None, "press"),
                     rnd("2026-07", "Series D", 44000000, "Lux Capital", True, FT_GLOSS, "press")],
             extra={"valuation_range_source": "web_verified"},
             note="Booking and payments software for beauty businesses, New York; renamed Genius in July 2026. "
                  "BeautyMatter: Bessemer led the $16.4M Series A (announced November 2021) after $2.8M of angel and "
                  "Techstars money, so the entry is the Series A and the Growth band read off the 2023 Form D is "
                  "disputed; the firm's own year reads 2020. Mark: the $44M Series D of July 2026 led by Lux at "
                  "$1.15B (Fortune, 2026-07-21)."))

# ---- Good Glamm Group (MyGlamm)
L.append(cls("good-glamm-group", status="defunct", rng="below_1b", country="IN", country_src="web_verified",
             country_cite=W("Good Glamm Group"), city="Mumbai", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2019", focus="Consumer & Marketplaces",
             rounds=[rnd("2017-09", "Series A", 6000000, "L'Occitane", False, EI_MYGLAMM, "press"),
                     rnd("2019", "Series B", None, "Bessemer Venture Partners", True, None, "press"),
                     rnd("2021-07", "Series C", 71000000, None, True, W("Good Glamm Group"), "press"),
                     rnd("2021-11", "Series D", 150000000, "Prosus Ventures and Warburg Pincus", None,
                         W("Good Glamm Group"), "press")],
             note="Beauty and personal care brands (MyGlamm), Mumbai. The group collapsed in July 2025: its lenders "
                  "took over and began selling the brands (Economic Times timeline, 2025-07-24), so the row reads "
                  "defunct and below_1b against the $1.2B mark of November 2021, as the Accel book reads its MyGlamm "
                  "row. The September 2017 Series A names L'Occitane, Tano and Brand Capital, not Bessemer "
                  "(Entrepreneur India); model: Bessemer entered leading the 2019 Series B, the year its archive first "
                  "lists MyGlamm, and the firm's own year of 2015 predates every round on record. This row and the "
                  "base row myglamm are one company."))

# ---- GoodShip
L.append(cls("goodship", status="private", rng="below_1b", country="US", city="Seattle", stage="Series A",
             stage_src="web_verified", stage_cite=BW_GOODSHIP, stage_conf="high", entry_date="2024-05",
             focus="SaaS",
             rounds=[rnd("2024-05", "Series A", 8000000, "Bessemer Venture Partners", True, BW_GOODSHIP, "press"),
                     rnd("2025-08", "Series B", 25000000, None, None, None, "press")],
             note="Freight procurement and analytics software, founded by Convoy alumni in the Seattle area. Business "
                  "Wire (2024-05-16): GoodShip secures an $8M Series A led by Bessemer Venture Partners. Momentum "
                  "check 2026-10-01: a $25M Series B in August 2025 with no reported valuation (Google News)."))

# ---- Gracenote
L.append(cls("gracenote", rng="below_1b", city="Emeryville", stage="undetermined", entry_date="2004-02-20",
             focus="Media, Gaming & Advertising", rounds=[],
             note="Music and media metadata, Emeryville (as in the Sequoia book); acq. by Sony, 2008. The firm's own "
                  "listing dates its investment 2004-02-20 and names no round; a Google News query on 2026-10-01 "
                  "returned no funding report."))

# ---- Graph AI
L.append(cls("graph-ai", status="private", rng="below_1b", country="US", city="Pleasanton", city_src="web_verified",
             stage="Seed", stage_src="first_party", stage_cite=POST("graph-ai-is-redefining"), stage_conf="high",
             entry_date="2025-10", grad="graduated", grad_src="web_verified", grad_cite=FS_GRAPH, grad_conf="high",
             focus="Healthcare & Bio",
             rounds=[rnd("2025-10", "Seed", 3000000, "Bessemer Venture Partners", True, EN_GRAPH, "press"),
                     rnd("2026-09", "Series A", 13300000, "Insight Partners", True, FS_GRAPH, "press")],
             note="AI pharmacovigilance software for drug makers, Pleasanton, California (FinSMEs; the firm's India "
                  "desk made the investment). The firm's own post of 2025-10-16: Bessemer leads Graph AI's seed "
                  "round ($3M, Entrackr). Graduated: the $13.3M Series A of September 2026 led by Insight Partners "
                  "with Bessemer participating (FinSMEs, 2026-09-10), a named later round inside the 24-month "
                  "window. Momentum check 2026-10-01: no valuation reported."))

# ---- Groups
L.append(cls("groups", status="private", rng="below_1b", country="US", city="Burlington", stage="Series A",
             stage_src="first_party", stage_cite=POST("our-deep-health-seed-program"), stage_conf="high",
             entry_date="2017-04-11", focus="Healthcare & Bio",
             rounds=[rnd("2017-04", "Series A", None, "Bessemer Venture Partners", True,
                         POST("our-deep-health-seed-program"), "firm")],
             note="Groups Recover Together, outpatient opioid addiction treatment, Burlington, Massachusetts. The "
                  "firm's own post of 2018-06-01: 'We led the Series A of ... Groups'; the listing dates the "
                  "investment 2017-04-11."))

# ---- GTS Central Europe (control position)
L.append(verdict("gts-central-europe", "not_member",
                 "control position: a consortium of funds led by Columbia Capital, M/C Venture Partners and Innova "
                 "Capital, with Bessemer Venture Partners a member, bought the entire shareholding of GTS Central "
                 "Europe in January 2008, the firm's listed 2008 investment; the firm with its co-investor group "
                 "acquired control, so there is no venture round (COLLECTION.md s1 control positions, decisions.md "
                 "D5); Deutsche Telekom bought the company from the consortium in 2014",
                 ec="web", conf="high", cite=GTS_BUYOUT))

# ---- Guild
L.append(cls("guild", status="private", rng="1b_plus", usd=4400000000, val_src="web_verified", val_cite=FB_GUILD,
             asof="2022-06", city="Denver", entry_date="2017", focus="SaaS",
             flags=["stale", "model_disputes_source"],
             rounds=[rnd("2017", "Series B", 21000000, "Bessemer Venture Partners", True, None, "press"),
                     rnd("2019-11", "Series D (Form D)", 157300014, None, True, None, "filing"),
                     rnd("2022-06", "Series F", None, None, None, FB_GUILD, "press")],
             extra={"valuation_range_source": "web_verified"},
             note="Guild (Guild Education), education benefits platform, Denver. The pre-filled acquired status is a "
                  "name collision (the YC and Battery rows named Guild are other companies); Guild is private "
                  "(Wikipedia), valued at $4.4B in June 2022 (Forbes), a mark older than 24 months, as in the "
                  "Felicis, General Catalyst, ICONIQ and Redpoint books. The firm's own year is 2017, when by model "
                  "knowledge Bessemer led the $21M Series B, so the Growth entry stands and its date moves from the "
                  "2019 Form D to 2017."))

# ---- Habana Labs
L.append(cls("habana-labs", status="acquired", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=PR_HABANA, city="Caesarea", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2017-01-04", focus="Industrial & Robotics",
             rounds=[rnd("2017-01", "Series A", None, None, True, None, "press"),
                     rnd("2018-11", "Series B", 75000000, "Intel Capital", True, PR_HABANA, "press")],
             note="AI processor developer, Israel (Caesarea, as in the Battery book; the company's 2018 release says "
                  "Tel Aviv and San Jose); acq. by Intel, 2019. The firm's own date is 2017-01-04, 22 months before "
                  "the $75M Series B of November 2018 in which the release also names Bessemer; model: the earlier "
                  "round is the Series A, in which Bessemer invested beside Avigdor Willenz and Walden."))

# ---- Hadapt
L.append(cls("hadapt", status="acquired", rng="below_1b", city="Cambridge", focus="Data Infrastructure",
             note="SQL analytics on Hadoop, Cambridge, Massachusetts; acq. by Teradata, 2014 (the firm's exit year)."))

# ---- Halter
L.append(cls("halter", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=MC_HALTER,
             asof="2026-03", country="NZ", country_src="web_verified", country_cite=W("Halter (company)"),
             city="Auckland", stage="Growth", stage_src="web_verified", stage_cite=W("Halter (company)"),
             stage_conf="high", entry_date="2023-03", focus="Industrial & Robotics",
             rounds=[rnd("2018", "early round", None, None, False, W("Halter (company)"), "press"),
                     rnd("2021", "Series B", None, "Blackbird Ventures", False, W("Halter (company)"), "press"),
                     rnd("2023-03", "Series C", None, "Bessemer Venture Partners", True, W("Halter (company)"),
                         "press"),
                     rnd("2025-06", "Series D", 100000000, None, None, W("Halter (company)"), "press"),
                     rnd("2026-03", "Series E", 220000000, "Founders Fund", None, MC_HALTER, "press")],
             extra={"valuation_range_source": "web_verified"},
             note="Smart collars and herd management software for cattle, Auckland. Wikipedia: the NZ$85M Series C "
                  "announced in March 2023 was led by Bessemer, and the earlier rounds name other investors, so the "
                  "entry is Growth (the firm's own year reads 2022). Mark: the $220M Series E of March 2026 led by "
                  "Founders Fund at a $2 billion valuation (Moneycontrol headline, 2026-03-22; Wikipedia agrees)."))

# ---- HashiCorp
L.append(cls("hashicorp", rng="below_1b", city="San Francisco", stage="Growth", stage_src="web_verified",
             stage_cite=GN_HASHI, stage_conf="high", entry_date="2018-10-17", focus="Data Infrastructure",
             rounds=[rnd("2018-11", "Series D", 100000000, "IVP", True, GN_HASHI, "company")],
             note="Infrastructure automation software, San Francisco; IPO in 2021, then acq. by IBM, 2025. The "
                  "company's release of 2018-11-01: the $100M Series D at $1.9B was led by new investor IVP 'with "
                  "participation from Bessemer Venture Partners, also a new investor'; the firm's own date is "
                  "2018-10-17."))

# ---- Hatch
L.append(cls("hatch", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2021", focus="SaaS", rounds=[],
             note="Customer messaging and lead management software for home service businesses, San Francisco (as in "
                  "the YC book); acq. by Yelp, 2026 (the $270M purchase of Hatchify Inc. completed in February 2026, "
                  "Investing.com headline). "
                  "No report of the 2021 round Bessemer entered was found (two Google News queries, 2026-10-01)."))

jl.write("j03b", L)
