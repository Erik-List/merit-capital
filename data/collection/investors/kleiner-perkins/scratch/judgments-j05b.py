"""PRO-99 Kleiner Perkins, judge j05, queue batch 10 (ujet .. acuson-acn), plus four batch-9 rows missed in
judgments-j05a.py (suvolta, tas-energy, textplus, thatgamecompany). Membership corrections: wave and yammer
(partner-carried, Mamoon Hamid's earlier firms), windtree-therapeutics-inc-de (sale consideration, R5), aac (T3 / X1).
Skipped per the run notes: 360buy (merges into jd-com)."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, W, FTS, ARCH

GL = "Graduation left for the graduation pass."


def PX(slug):
    m = [p["url"] for p in jl._POSTS if p["slug"] == slug]
    assert len(m) == 1, (slug, m)
    return m[0]


VR = {"valuation_range_source": "web_verified"}
SA_VRSN = "https://stockanalysis.com/stocks/vrsn/market-cap/"
SA_ZLAB_CO = "https://stockanalysis.com/stocks/zlab/company/"
# IPO registrations on EDGAR, read through secget.py
S1_VRSN = "https://www.sec.gov/Archives/edgar/data/1014473/0000898430-98-000012.txt"
S1_VIANT = "https://www.sec.gov/Archives/edgar/data/1028122/0001047469-99-021297.txt"
S1_VLTR = "https://www.sec.gov/Archives/edgar/data/1050550/000089161804001015/f99063orsv1.htm"
S1_VCYT = "https://www.sec.gov/Archives/edgar/data/1384101/000104746913009208/a2216719zs-1.htm"
F1_ZLAB = "https://www.sec.gov/Archives/edgar/data/1704292/000119312517258641/d358845df1.htm"
F20_360 = "https://www.sec.gov/Archives/edgar/data/1084587/000091205701517196/a2036999z20-f.txt"
S1_ZNGA = FTS("ZYNGA", "S-1")
K8_WINT = FTS("WINDTREE", "8-K")
# pages read with WebFetch
WAYMO_BLOG = "https://waymo.com/blog/2026/02/waymo-raises-usd16-billion-investment-round/"
WS_B = "https://watershed.com/blog/series-b"
WS_C = "https://watershed.com/blog/series-c"
# sibling books' recorded citations (rule 10), printed from siblings.json
INSIGHT_VIZ = ("https://www.insightpartners.com/ideas/viz-ai-raises-100-million-in-series-d-funding-led-by-tiger-"
               "global-and-insight-partners-at-1-2-billion-valuation/")
FORBES_XENDIT = "https://www.forbes.com/sites/yessarrosendar/2022/05/19/indonesian-unicorn-xendit-bags-300-million-in-series-d-funding/"
# Form D filings from the rows' own formd_links
FD = {
    "upwind": "https://www.sec.gov/Archives/edgar/data/1420663/000142066310000002/0001420663-10-000002-index.htm",
    "verdiem": "https://www.sec.gov/Archives/edgar/data/1257512/000125751210000001/0001257512-10-000001-index.htm",
    "veracyte": "https://www.sec.gov/Archives/edgar/data/1384101/000138410110000004/0001384101-10-000004-index.htm",
    "xcellerex": "https://www.sec.gov/Archives/edgar/data/1512166/000151216611000001/0001512166-11-000001-index.htm",
    "xdx": "https://www.sec.gov/Archives/edgar/data/1217234/000121723410000002/0001217234-10-000002-index.htm",
    "zephyr": "https://www.sec.gov/Archives/edgar/data/1650467/000165046715000001/0001650467-15-000001-index.htm",
    "zumper": "https://www.sec.gov/Archives/edgar/data/1600984/000160098414000001/0001600984-14-000001-index.htm",
    "suvolta": "https://www.sec.gov/Archives/edgar/data/1356683/000135668309000004/0001356683-09-000004-index.htm",
    "suvolta2": "https://www.sec.gov/Archives/edgar/data/1356683/000135668310000001/0001356683-10-000001-index.htm",
    "tas": "https://www.sec.gov/Archives/edgar/data/1491868/000149186813000003/0001491868-13-000003-index.htm",
    "textplus": "https://www.sec.gov/Archives/edgar/data/1423630/000114036115014479/0001140361-15-014479-index.htm",
}

L = []

# ---- batch-9 rows missed in judgments-j05a.py
L.append(cls("suvolta", status="acquired", rng="below_1b", city="Los Gatos", stage="undetermined",
             focus="Industrial & Robotics",
             rounds=[rnd("2009-10-30", "Form D offering", 3000300, None, True, FD["suvolta"], "filing"),
                     rnd("2010-04", "Form D offering", 22174998, None, True, FD["suvolta2"], "filing")],
             note="Low-power transistor technology, Los Gatos; its technology went to Mie Fujitsu Semiconductor in "
                  "2015 and the NEA book reads acquired (aligned, rule 10). Incorporated in 2006 with Bill Joy on the "
                  "board; the 2009 Form D is the first filing on record, not necessarily the entry, and no source "
                  "read names the round."))

L.append(cls("tas-energy", status="acquired", rng="below_1b", city="Houston", city_src="formd_address",
             stage="undetermined", entry_date="2011", focus="Climate & Energy",
             rounds=[rnd("2013-09", "Form D offering", 19904386, None, True, FD["tas"], "filing")],
             note="Modular cooling and power plants for data centers, Houston (Form D address); the firm lists it "
                  "acquired by Comfort Systems. A Green Growth Fund position the firm dates to 2011 (the 2013 Form D "
                  "with John Denniston is a follow-on); no source read names the round."))

L.append(cls("textplus", status="private", rng="below_1b", city="Marina del Rey", city_src="formd_address",
             stage="undetermined", focus="Consumer & Marketplaces",
             rounds=[rnd("2015-06", "Form D offering", 6904009, None, True, FD["textplus"], "filing")],
             note="Free texting and calling app (formerly Gogii), Marina del Rey (Form D address); an iFund position "
                  "on the firm's 2013-18 pages, the app still operates. The 2015 Form D with Matt Murphy is the only "
                  "filing on record; no source read names the round the firm entered."))

L.append(cls("thatgamecompany", status="private", rng="below_1b", country="US", city="Los Angeles",
             stage="undetermined", entry_date="2014", focus="Media, Gaming & Advertising",
             rounds=[rnd("2014-05-27", "venture round", 7000000, "Capital Today", None, W("Thatgamecompany"), "press"),
                     rnd("2022-03", "investment", 160000000, None, None, W("Thatgamecompany"), "press")],
             note="Game studio (Journey, Sky), Los Angeles. The firm dates its investment to 2014, the year of the $7M "
                  "round led by Capital Today 'and a team of other investors' (Wikipedia), which names no series and "
                  "does not name Kleiner Perkins; stage undetermined."))

# ---- batch 10
L.append(cls("ujet", status="private", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2017", focus="SaaS", rounds=[],
             note="Cloud contact center software, San Francisco; still private. The firm's listing gives 2017 and "
                  "Early; no source read names the round."))

L.append(cls("untuckit", status="private", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             note="Men's apparel brand, headquartered in New York (Wikipedia); private, small Form D rounds in 2024 "
                  "and 2025."))

L.append(cls("upstart", country="US", city="San Mateo", stage="Seed", stage_src="web_verified",
             stage_cite=W("Upstart (company)"), stage_conf="high", entry_date="2012", grad="graduated",
             grad_src="web_verified", grad_cite=W("Upstart (company)"), grad_conf="high", focus="Fintech & Payments",
             rounds=[rnd("2012", "Seed", 1750000, None, True, W("Upstart (company)"), "press"),
                     rnd(None, "Series A", 5900000, None, None, W("Upstart (company)"), "press"),
                     rnd("2015-06", "Series C", 35000000, "Third Point", None, W("Upstart (company)"), "press")],
             note="AI lending platform, San Mateo (Nasdaq: UPST). Wikipedia lists Kleiner Perkins among the investors "
                  "in the $1.75M seed, the firm's 2012 entry, followed by a named $5.9M Series A, so the seed "
                  "graduated; the First Round, GV and NEA books also read Seed. Market cap $2.24B on 2026-09-30 "
                  "(stockanalysis)."))

L.append(cls("upwind-solutions", status="acquired", rng="below_1b", city="Medford", stage="undetermined",
             entry_date="2010", focus="Climate & Energy",
             rounds=[rnd("2010-03", "Form D offering", 28849999, None, True, FD["upwind"], "filing")],
             note="Wind turbine operations and maintenance services, Medford, Oregon (the firm's 2010 listing); "
                  "Vestas bought it (the firm's acquirer field). A Green Growth Fund position entered in 2010 at the "
                  "$28.8M round with David Mount and Michael Linse as directors; the company was already an operating "
                  "business, but no source read names the round."))

L.append(cls("uship", status="private", rng="below_1b", city="Austin", focus="Consumer & Marketplaces",
             note="Online marketplace for shipping, Austin (Wikipedia); still private. Aligned with the Benchmark book."))

L.append(cls("veem", status="private", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2015", focus="Fintech & Payments", rounds=[],
             note="Business payments network (formerly Align Commerce, the firm's page slug), San Francisco "
                  "(Wikipedia, which lists Kleiner Perkins among the investors). The firm's listing gives 2015 and "
                  "Early; no source read names the round."))

L.append(cls("vera-therapeutics", city="Brisbane", focus="Healthcare & Bio",
             note="Immunology biotech, Brisbane, California; market cap $2.33B on 2026-09-30 (stockanalysis)."))

L.append(cls("veracyte", city="South San Francisco", stage="undetermined", entry_date="2007",
             focus="Healthcare & Bio",
             rounds=[rnd("2010-06", "Form D offering", 28435000, None, True, FD["veracyte"], "filing")],
             note="Genomic diagnostics, South San Francisco. The S-1 says the company was incorporated as the "
                  "incubator Calderome in August 2006 and renamed Veracyte in 2008, with Brook Byers on the board from "
                  "January 2007, so the firm was a founding investor (its year 2007) and the 2010 Form D date on file "
                  "is a follow-on; no source read names the first round."))

L.append(cls("verdiem", status="acquired", rng="below_1b", city="Seattle", stage="undetermined",
             flags=["stage_disputes_band"], focus="Climate & Energy",
             rounds=[rnd("2009-12", "Form D offering", 5930000, None, True, FD["verdiem"], "filing")],
             note="PC power management software, Seattle; Aptean bought it on 2015-01-12 (Wikipedia). The Seed band "
                  "on the December 2009 Form D is disputed: the firm's own listing carried Verdiem from 2008 and the "
                  "company dates from 2002, so that filing is a follow-on, and no source read names the entry round."))

L.append(cls("verisign", status="public", rng="10b_plus", usd=25470000000, val_src="web_verified",
             val_cite=SA_VRSN, asof="2026-09-30", city="Reston", stage="Growth", stage_src="web_verified",
             stage_cite=S1_VRSN, stage_conf="high", entry_date="1996-02-20", focus="Data Infrastructure", extra=VR,
             rounds=[rnd("1995-04-18", "Series A", 5168260, None, False, S1_VRSN, "filing"),
                     rnd("1996-02-20", "Series B", 5142851, None, True, S1_VRSN, "filing"),
                     rnd("1996-11-15", "Series C", None, None, None, S1_VRSN, "filing")],
             note="Domain registry and internet infrastructure, Reston, Virginia (Nasdaq: VRSN). The 1998 IPO "
                  "registration lists the April 1995 Series A buyers (Bessemer, Visa, Intel, Security Dynamics) "
                  "without the firm, and Kleiner Perkins Caufield & Byers VII, its founders fund and the Zaibatsu "
                  "Fund II buying the February 1996 Series B; Kevin Compton joined the board that month. Market cap "
                  "$25.47B on 2026-09-30 (stockanalysis)."))

L.append(cls("vertica", city="Billerica", rng="below_1b", stage="undetermined", entry_date="2007",
             focus="Data Infrastructure", rounds=[],
             note="Columnar analytics database founded in 2005, Billerica, Massachusetts; HP bought it in March 2011 "
                  "(Wikipedia). The firm's listing gives 2007 with Ray Lane; no source read names the round."))

L.append(cls("viant", status="acquired", rng="below_1b", country="US", city="Boston", stage="undetermined",
             entry_date="1996", focus="SaaS", flags=["model_disputes_source"],
             rounds=[rnd("1996-05-16", "Series A", 3064998, None, None, S1_VIANT, "filing"),
                     rnd("1996-06-19", "Series B", 1000000, None, None, S1_VIANT, "filing"),
                     rnd("1997-06-04", "Series C", 8001434, None, None, S1_VIANT, "filing"),
                     rnd("1998-11", "Series D", 20125000, None, None, S1_VIANT, "filing")],
             note="Viant Corp, the Boston internet consultancy (founded 1996 as Silicon Valley Internet Partners; IPO "
                  "1999), which merged into divine, inc. in 2002, so acquired, as the TCV book reads, not defunct. The "
                  "firm's live page mixes in Viant Technology (ticker DSP), a different company. The 1999 S-1 shows "
                  "KPCB VIII, KPCB Java Fund and related funds holding shares from the 1996 Series A or B, but does "
                  "not say which."))

L.append(cls("virsa-systems", status="acquired", rng="below_1b", city="Fremont", stage="undetermined",
             entry_date="2004", focus="Security", rounds=[],
             note="Access control and compliance software for SAP systems, Fremont; SAP announced the acquisition on "
                  "2006-04-03. The firm's listing gives 2004 and Early; no source read names the round."))

L.append(cls("visio", status="acquired", rng="below_1b", country="US", city="Seattle", stage="undetermined",
             entry_date="1992", focus="SaaS", rounds=[],
             note="Diagramming software, Seattle; listed in 1995 and bought by Microsoft in 2000 (Wikipedia, Microsoft "
                  "Visio). The firm's listing gives 1992 and Early; no source read names the round."))

L.append(cls("visly", status="acquired", rng="below_1b", country="US", stage="undetermined", entry_date="2018",
             focus="DevTools & APIs", flags=["city_unknown"], rounds=[],
             note="Design-to-code tool for front-end engineers (a Y Combinator company); the firm lists it acquired by "
                  "Figma and visly.app now redirects to figma.com. No source read places its office or names the "
                  "firm's 2018 round."))

L.append(cls("viz-ai", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified",
             val_cite=INSIGHT_VIZ, asof="2022-04", city="San Francisco", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2018", focus="Healthcare & Bio", flags=["stale"], extra=VR,
             note="AI stroke and care coordination software, San Francisco. Kleiner Perkins co-led the 2018 $21M "
                  "Series A with GV (the firm's year 2018, Early). Last priced mark the $1.2B Series D of April 2022, "
                  "as the GV, Insight and Tiger books record; stale."))

L.append(cls("voloagri", status="private", rng="below_1b", city="South San Francisco", city_src="formd_address",
             focus="Climate & Energy",
             note="Vegetable seed breeding and genetics, South San Francisco (Form D address); Form D rounds through "
                  "2020 and no exit found."))

L.append(cls("volterra-semiconductor-corporation", country="US", city="Fremont", rng="below_1b",
             stage="undetermined", focus="Industrial & Robotics",
             rounds=[rnd("2002-01", "Series E", None, None, True, S1_VLTR, "filing")],
             note="Power management semiconductors, Fremont; Maxim acquired it in October 2013. Incorporated in August "
                  "1996; the 2004 S-1 shows Kleiner Perkins Caufield & Byers VIII (a 1996 fund) and related funds as "
                  "the largest holder and buying Series E, but the first series the firm bought is not named."))

L.append(cls("watershed", status="private", rng="1b_plus", usd=1800000000, val_src="web_verified", val_cite=WS_C,
             asof="2024-02-01", city="San Francisco", stage="undetermined", entry_date="2020",
             focus="Climate & Energy", flags=["stale", "stage_disputes_band"], extra=VR,
             rounds=[rnd("2022-02-08", "Series B", 70000000, "Sequoia and Kleiner Perkins", True, WS_B, "company"),
                     rnd("2024-02-01", "Series C", 100000000, "Greenoaks", True, WS_C, "company")],
             note="Carbon accounting software, San Francisco. $1.8B Series C of February 2024 led by Greenoaks with "
                  "Kleiner Perkins (company post), stale. The Growth band read off the 2024 Form D is disputed: the "
                  "firm co-led the 2022 Series B and lists 2020 as its first year, so it entered before, at a round "
                  "no source read names."))

L.append(verdict("wave", "not_member",
                 "Partner-carried (Erik 2026-09-17 partner-carried rule; D3, D5): the firm's page lists Wave (Toronto) "
                 "with a 2012 first year, the year of its May 2012 Series B led by The Social+Capital Partnership "
                 "(Wikipedia), where Mamoon Hamid was a partner; every Form D from 2012 to 2016 names Hamid, who joined "
                 "Kleiner Perkins in 2017, and no source names a Kleiner Perkins fund in any Wave round. The listing "
                 "appears only in the 2023-24 logo grid.", ec="site_listing", conf="medium", cite=W("Wave Financial")))

L.append(cls("waymo", status="private", rng="100b_plus", usd=126000000000, val_src="web_verified",
             val_cite=WAYMO_BLOG, asof="2026-02-02", country="US", city="Mountain View", stage="Growth",
             stage_src="web_verified", stage_cite=WAYMO_BLOG, stage_conf="high", entry_date="2026-02-02",
             focus="Industrial & Robotics", extra=VR,
             rounds=[rnd("2026-02-02", "investment round ($16B at $126B post-money)", 16000000000,
                         "Dragoneer, DST Global and Sequoia Capital", True, WAYMO_BLOG, "company")],
             note="Autonomous driving, Mountain View. Waymo's own post names Kleiner Perkins among the investors in "
                  "the $16B round of February 2026 at $126B post-money, the firm's 2026 entry; that round is also the "
                  "momentum-slice check (done 2026-09-30)."))

L.append(cls("waze", status="acquired", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=W("Waze"), city="Ra'anana", stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=W("Waze"), entry_date="2011", focus="Consumer & Marketplaces",
             rounds=[rnd("2010", "second round", 25000000, None, False, W("Waze"), "press"),
                     rnd("2011", "third round", 30000000, None, None, W("Waze"), "press")],
             note="Crowd-sourced navigation, Waze Mobile, most staff in Ra'anana, Israel; Google bought it in June "
                  "2013 for about $1.1-1.3B. Kleiner Perkins' Digital Growth Fund entered in 2011, the year of the $30M "
                  "third round (Wikipedia; the firm co-led it with Horizons Ventures, model knowledge), after the "
                  "$25M second round of 2010: Growth."))

L.append(cls("webmethods", status="acquired", rng="below_1b", country="US", city="Fairfax", stage="undetermined",
             entry_date="1996", focus="Data Infrastructure", rounds=[],
             note="Enterprise application integration software, Fairfax, Virginia; listed in 2000, bought by Software "
                  "AG in 2007 for $546M (Wikipedia). The firm's listing gives 1996 and Early; no source read names "
                  "the round."))

L.append(cls("willo", status="private", rng="below_1b", country="US", stage="undetermined", entry_date="2017",
             focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
             note="Automated toothbrush maker; its store still sells (willo.com, 2026-09-30) and the firm lists it "
                  "Current. No source read places its office or names the firm's 2017 round."))

L.append(cls("windsurf", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="Growth",
             stage_src="first_party", stage_cite=PX("codeium-series-b"), stage_conf="high", entry_date="2024-01-30",
             focus="AI & Applied AI",
             rounds=[rnd("2024-01-30", "Series B", None, "Kleiner Perkins", True, PX("codeium-series-b"), "firm")],
             note="AI coding tools (Codeium, renamed Windsurf), Mountain View. The firm's post says it led the Series "
                  "B, after the company's Series A. In July 2025 Google licensed the technology and hired the CEO and "
                  "some staff, which decides nothing (acqui-hire rule); Cognition then signed to buy the company "
                  "itself (Wikipedia, Cognition AI), so acquired."))

L.append(verdict("windtree-therapeutics-inc-de", "not_member",
                 "Sale consideration (Erik 2026-09-22; decisions.md R5): KPCB China Fund II's Windtree shares (its Form "
                 "3 of 2018-12-31) came from Windtree's December 2018 acquisition of CVie Therapeutics, which the fund "
                 "held (8-K of 2018-12-21, James Huang a former CVie director); Windtree was listed long before, and "
                 "the 2019 Form D is a private placement into the listed company (T3). CVie Therapeutics is the member.",
                 ec="fund_filing", conf="high", cite=K8_WINT))

L.append(cls("xcellerex", status="acquired", rng="below_1b", city="Marlborough", stage="undetermined",
             entry_date="2006", focus="Healthcare & Bio",
             rounds=[rnd("2011-01", "Form D offering", 5400000, None, True, FD["xcellerex"], "filing")],
             note="Single-use bioreactor systems, Marlborough, Massachusetts; GE Healthcare bought it in 2012. The "
                  "firm dates its investment to 2006, so the 2011 Form D (Thomas Monath) is a follow-on and the entry "
                  "year is the firm's 2006; no source read names the round."))

L.append(cls("xdx-inc", city="Brisbane", stage="undetermined", focus="Healthcare & Bio",
             rounds=[rnd("2010", "Form D offering", None, None, True, FD["xdx"], "filing")],
             note="XDx renamed itself CareDx (Nasdaq: CDNA), transplant diagnostics, Brisbane, California "
                  "(stockanalysis profile); market cap $3.36B on 2026-09-30. Brook Byers' position predates the 2010 "
                  "Form D on file (listed from 2008); no source read names the round."))

L.append(cls("xendit", country="ID", country_src="web_verified", country_cite=FORBES_XENDIT, city="Jakarta",
             stage="undetermined", entry_date="2018", focus="Fintech & Payments", rounds=[],
             note="Payments infrastructure for Southeast Asia, Jakarta (the Indonesia claim is confirmed, as the Accel, "
                  "Coatue, Tiger and YC books record). The firm's listing gives 2018 and Early; no source read names "
                  "its round."))

L.append(cls("xilinx", city="San Jose", rng="below_1b", stage="undetermined", entry_date="1984",
             focus="Industrial & Robotics", rounds=[],
             note="Programmable logic chips, San Jose (Wikipedia); AMD completed the acquisition in 2022. The firm's "
                  "page says it backed the company in its founding year 1984 but names no round."))

L.append(verdict("yammer", "not_member",
                 "Partner-carried (Erik 2026-09-17 partner-carried rule; D3, D5): the live site lists Yammer (Prior, "
                 "2010) but no kpcb.com page carried it in any era, even as an alumnus after the 2012 Microsoft sale; "
                 "the only filing is the 2010 Form D naming Mamoon Hamid, then a partner at US Venture Partners (he "
                 "joined Kleiner Perkins in 2017), and no source names a Kleiner Perkins fund in any Yammer round.",
                 ec="site_listing", conf="medium", cite=SITE("yammer")))

L.append(cls("zai-lab", country="CN", country_src="web_verified", country_cite=SA_ZLAB_CO, city="Shanghai",
             stage="Series A", stage_src="web_verified", stage_cite=F1_ZLAB, stage_conf="high",
             entry_date="2014-03-27", focus="Healthcare & Bio", flags=["kpcb_china"],
             rounds=[rnd("2014-03-27", "convertible loan, converted into Series A-1 on 2014-08-20", 500000, None, True,
                         F1_ZLAB, "filing"),
                     rnd("2014-08-20", "Series A-1", None, None, True, F1_ZLAB, "filing"),
                     rnd("2016-01-20", "Series B-1", None, None, None, F1_ZLAB, "filing")],
             note="Biopharma, Shanghai (principal office in Pudong; Nasdaq ZLAB). The F-1 shows KPCB China Fund II "
                  "lending $0.5M on 2014-03-27 as a loan converted into Series A-1 preferred at the August 2014 "
                  "closing, and buying Series A-1 and A-2; it held 9.3% at the IPO. A KPCB China position (X1)."))

L.append(cls("zazzle", status="private", rng="below_1b", city="Redwood City", stage="undetermined",
             entry_date="2004", focus="Consumer & Marketplaces", rounds=[],
             note="Custom products marketplace, Redwood City (Wikipedia); still private. The firm's listing gives 2004 "
                  "and Early (Bing Gordon on the archived page); no source read names the round."))

L.append(cls("zephyr-health", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             stage="undetermined", focus="Healthcare & Bio",
             rounds=[rnd("2015-07", "Form D offering", 19999995, None, True, FD["zephyr"], "filing")],
             note="Life sciences data and analytics, San Francisco (Form D address). Status aligned with the GV book "
                  "(acquired). The firm's archived page carries it from 2014, before the 2015 Form D with Brook Byers, "
                  "so that filing is not the entry; no source read names the round."))

L.append(cls("zumper", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             stage="undetermined", entry_date="2012", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-02", "Form D offering", 8333257, None, True, FD["zumper"], "filing")],
             note="Apartment rental marketplace, San Francisco; still private. The firm dates its investment to 2012, "
                  "before the first Form D (February 2014, Chi-Hua Chien as director), and no source read names the "
                  "2012 round."))

L.append(cls("zynga", city="San Francisco", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=S1_ZNGA, stage_conf="high", entry_date="2008-07", focus="Media, Gaming & Advertising",
             rounds=[rnd("2008-01", "Series A", None, None, False, S1_ZNGA, "filing"),
                     rnd("2008-02", "Series A-1", None, None, False, S1_ZNGA, "filing"),
                     rnd("2008-07", "Series B", None, "Kleiner Perkins", True, S1_ZNGA, "filing"),
                     rnd("2011-02", "Series C", None, None, True, S1_ZNGA, "filing")],
             note="Social games, San Francisco until the 2022 Take-Two acquisition (then San Mateo). The S-1 records "
                  "KPCB XIII buying Series B in July 2008 (Bing Gordon's seat), after the January and February 2008 "
                  "Series A rounds, and the Digital Growth Fund buying Series C in February 2011: Growth."))

L.append(cls("360networks", status="acquired", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=F20_360, city="Vancouver", stage="undetermined", focus="Data Infrastructure", rounds=[],
             note="Fiber network operator, Vancouver (principal office on its 2001 20-F, which Kleiner Perkins Caufield "
                  "& Byers signed as an investor party); Kevin Compton was a director from May 2000. Bankrupt in 2001, "
                  "reorganised in 2002 and bought by Zayo in December 2011 (Wikipedia), so acquired. No source read "
                  "names the round."))

L.append(cls("3dv-systems", status="acquired", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=W("3DV Systems"), city="Yokneam", stage="undetermined", focus="Industrial & Robotics",
             rounds=[],
             note="Israeli time-of-flight 3D camera maker (ZCam), Yokneam; sold its assets to Microsoft in 2009, the "
                  "technology behind Kinect (Wikipedia), so acquired. No source read names the round."))

L.append(cls("9-diamond", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
             country_cite=ARCH("9-diamond"), city="Shanghai", stage="undetermined", focus="Consumer & Marketplaces",
             flags=["kpcb_china"], rounds=[],
             note="Online diamond retailer, Shanghai, on the firm's 2010 KPCB China portfolio page (X1). No later "
                  "record of the company was found, so its state is unknown; no source read names the round."))

L.append(cls("a8-com", status="acquired", rng="below_1b", country="CN", country_src="web_verified",
             country_cite=ARCH("a8-com"), city="Shenzhen", stage="undetermined", focus="Media, Gaming & Advertising",
             flags=["kpcb_china"], rounds=[],
             note="A8 New Media Group, digital music, Shenzhen; listed in Hong Kong in June 2008 and taken private in "
                  "2024 by its controlling shareholder's vehicle Lux Origo at HK$0.36 a share (scheme of "
                  "arrangement, HKEX filings), so acquired. A KPCB China position (X1); no source read names the "
                  "round."))

L.append(verdict("aac", "not_member",
                 "T3 and X1: AAC Technologies (acoustic components, Shenzhen) has been listed in Hong Kong since 2005 and "
                 "appears only on the firm's KPCB China portfolio page (2010 on); KPCB China was formed in April 2007, "
                 "so its position was a purchase in the listed company, or else a pre-2007 TDF-era deal the China "
                 "listing carried (partner-carried). No Kleiner Perkins private round in AAC is recorded.",
                 ec="site_listing", conf="medium", cite=ARCH("aac")))

L.append(cls("abundant-robotics", status="acquired", rng="below_1b", country="US", city="Hayward",
             stage="undetermined", focus="Industrial & Robotics", rounds=[],
             note="Apple-harvesting robots, Hayward; shut down in 2021 and its assets were sold, so acquired as the GV "
                  "book reads (asset sale out of shutdown). On the firm's pages only in 2017-18; no source read names "
                  "the round."))

L.append(cls("accept", status="acquired", rng="below_1b", country="US", stage="undetermined",
             focus="Fintech & Payments", flags=["city_unknown"], rounds=[],
             note="The firm's page lists 'Accept', 1996, acquired by Amazon: that is Accept.com, the online payments "
                  "company Amazon bought in 1999. The page's year and its 'enterprise sales productivity software' "
                  "description do not fit that company and may mix in another; no source read places its office or "
                  "names the round."))

L.append(cls("acuson-acn", status="acquired", rng="below_1b", country="US", city="Mountain View",
             stage="undetermined", focus="Healthcare & Bio", rounds=[],
             note="Ultrasound equipment, Mountain View (the firm's 2010 listing); listed in the 1980s (ticker ACN) and "
                  "bought by Siemens in 2000. No source read names the round."))

jl.write("j05b", L)
