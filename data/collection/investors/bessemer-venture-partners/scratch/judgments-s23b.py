"""PRO-80 Bessemer, second pass s23, file b: the 2005 and later rows of queue/s2-3.json that change
(flock to zenzap). Run as NQ_TAG=s23 python3 judgments-s23b.py."""
import json

import judge_lib as jl
from judge_lib import NEWS, W, cls, rnd

BVP = "Bessemer Venture Partners"
GRAD = " Graduation left for the graduation pass."
CLS = json.loads((jl.INV / "companies" / "classification.json").read_text())


def STORED(slug):
    rows = CLS if isinstance(CLS, list) else CLS.get("rows", CLS)
    if isinstance(rows, dict):
        return rows[slug]
    return next(r for r in rows if r.get("slug") == slug)


L = []

CBS = NEWS("flock", "Fourth Round")
L.append(cls("flock",
             rounds=[rnd("2008-05-22", "fourth round", 15000000, "Fidelity Ventures", True, CBS, "press")],
             note="CBS News (2008-05-22): the $15M fourth round was led by Fidelity Ventures with 'past backers' Bessemer, Catamount and Shasta taking part, and the three earlier rounds were never announced in detail; no source read names the round Bessemer entered in 2005."))

ZW = W("Z-Wave")
L.append(cls("zensys", stage="Growth", stage_src="web_verified", stage_cite=ZW, stage_conf="medium", entry_date="2005",
             rounds=[rnd("2005", "third round", 16000000, BVP, True, ZW, "press")],
             note="Wikipedia's Z-Wave article: 'In 2005, Bessemer Venture Partners led a $16 million third seed round for Zensys'. A $16M third round of a company founded in 1999 is read as a later round (Growth), not as a seed, whatever the article's wording."))

AVEO = "https://www.sec.gov/Archives/edgar/data/1325879/000119312509253999/ds1.htm"
L.append(cls("aveo-pharmaceuticals", stage="Growth", stage_src="web_verified", stage_cite=AVEO, stage_conf="medium",
             entry_date="2007-04-10",
             rounds=[rnd("2007-04-10", "Series D (closes 2007-03-26, 04-10 and 04-27)", 52913775, None, True, AVEO, "filing")],
             note="AVEO's S-1: 'On March 26, 2007, April 10, 2007 and April 27, 2007, we sold an aggregate of 21,165,510 shares of our series D convertible preferred stock'. The firm's own investment date is 2007-04-10, the second close, and Bessemer Venture Partners VI Institutional signs the investor rights agreement filed with the S-1, so the entry was the Series D (Growth). The S-1's holder table lists only 5% holders and does not name Bessemer."))

TC08 = "https://techcrunch.com/2008/10/03/accel-partners-to-help-bring-you-cheap-eco-friendly-diapers/"
TC10 = "https://techcrunch.com/2010/04/20/diapers-com-on-its-way-to-selling-half-a-billion-diapers-raises-20-million-debt-round/"
L.append(cls("soap-com", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2007-11-07",
             rounds=[rnd("2007", "unnamed $7M round (Series B per a vendor profile)", 7000000, BVP, True, TC08, "press"),
                     rnd("2008-10", "unnamed round led by Accel", None, "Accel Partners", None, TC08, "press"),
                     rnd("2009-10", "Series E", 30000000, None, True, TC10, "press")],
             note="Soap.com is a Quidsi site, so this row is the same company and investment as quidsi-fka-diapers-com and diapers-com. TechCrunch (2008-10-03): Diapers.com 'raised a $7 million round led by Bessemer Venture Partners in 2007', then a larger Accel round; TechCrunch (2010-04-20) calls the October 2009 round the Series E. "
                  "No page read gives the 2007 round its letter; it is taken as the Series B (Growth), which a vendor profile also says, since the company already had venture backers (MentorTech, BEV Capital) by then."))

L.append(cls("enforta", status="acquired",
             note="Bought by the Russian operator ER-Telecom Holding, which completed the purchase in 2016 (from knowledge; a 2015-10-09 Broadband TV News item on the planned deal surfaced under the company's name but could not be read). Telecompaper (2014) describes the operator as Prestige Internet working under the Enforta brand. The round Bessemer entered in January 2008 is not named."))

PRN = NEWS("onestop-internet", "Linens")
L.append(cls("onestop-internet", city="Los Angeles", city_src="web_verified",
             note="A June 2016 release describes 'Los Angeles-based Onestop Internet ... backed by blue-chip investors Bessemer Ventures and Fung Capital USA' (" + PRN + "). Its fate after 2018 and the 2008 round's name were not found (two news queries)."))

QS = W("QuinStreet")
L.append(cls("ziff-davis-enterprise", status="acquired",
             note="Wikipedia: QuinStreet acquired the media assets of Ziff Davis Enterprise, including eWeek, in February 2012 (" + QS + "), so acquired. Insight Venture Partners had bought the division from Ziff Davis Media in July 2007; no source read says whether Bessemer was part of that buying group (a control ruling candidate) or which round its 2008 investment was."))

ITNL = NEWS("il-fs-transportation-networks", "Third Interim Distribution")
L.append(cls("il-fs-transportation-networks", status="public",
             note="Still listed on the NSE and BSE in 2026: share price and shareholding pages are current, and the company announced a third interim distribution to its debenture holders in April 2026 (" + ITNL + ") under the IL&FS group resolution that has run since 2018. No sale or delisting was found, so the row reads public, far below $1B."))

L.append(cls("densbits", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2010-10-20", city="Haifa",
             rounds=[rnd("2010-10-20", "Series B", None, None, True,
                         "https://www.cbinsights.com/company/densbits-technologies/financials", "vendor")],
             note="Entered at the Series B of October 2010 with Sequoia Capital Israel (from knowledge; a vendor profile dates a Series B to 2010-10-20, the firm's own date, and no press page naming the round was found). Haifa, Israel."))

IT = NEWS("palogix-infrastructure", "Insolvency Tracker")
L.append(cls("palogix-infrastructure", status="acquired", city="Kolkata",
             note="An insolvency process against the company (the NCLAT ruling Palogix Infrastructure v. ICICI Bank is its best known trace) ended in a resolution plan under which Sanjay Kumar Mishra (JFC Finance) acquired it, with creditors recovering Rs 56.84 crore of Rs 154.39 crore claimed (" + IT + "): a sale out of insolvency, so acquired. Kolkata from knowledge. The 2010 round is not named."))

TCI = "https://techcrunch.com/2012/05/14/saas-for-smbs-insightsquared-picks-up-4-5m-from-atlas-bessemer-salesforce-and-nextview/"
L.append(cls("insightsquared", stage="Series A", stage_src="web_verified", stage_cite=TCI, stage_conf="high",
             entry_date="2011-12-02",
             rounds=[rnd("2012-05-14", "Series A", 4500000, "Atlas Venture", True, TCI, "press")],
             note="TechCrunch (2012-05-14): 'a Series A round of $4.5 million' led by Atlas Venture with NextView 'and new investors Bessemer Venture Partners and Salesforce.com'. The firm's own date, 2011-12-02, is kept as the entry date. Mediafly announced it would acquire Boston-based InsightSquared in December 2021 (" + NEWS("insightsquared", "Mediafly to Acquire") + ")."))

XT = "https://vcnewsdaily.com/xtime/venture-capital-funding/ygdgvqppxd"
L.append(cls("xtime", stage="Growth", stage_src="web_verified", stage_cite=XT, stage_conf="high", entry_date="2012-10-05",
             rounds=[rnd("2012-11-13", "Series 2", 23000000, BVP, True, XT, "press")],
             note="VC News Daily (2012-11-13): Xtime 'raised $23 million in Series 2 funding ... led by Bessemer Venture Partners with participation from Lumia Capital and existing investors RPM Ventures and Saints Capital'. A second series into a company founded in 1999 with existing venture holders is a later round (Growth). The same page places Xtime in Redwood Shores, which is Redwood City."))

NS = "https://techcrunch.com/2013/04/16/nitrous-io-seed-funding/"
NA = "https://techcrunch.com/2014/03/18/cloud-development-platform-nitrous-io-closes-6-65m-series-a-round-led-by-bessemer/"
NX = "https://techcrunch.com/2016/10/31/cloud-development-platform-nitrous-io-shuts-down/"
L.append(cls("nitrous-io", status="defunct", stage="Seed", stage_src="web_verified", stage_cite=NS, stage_conf="high",
             entry_date="2012-08-09", grad="graduated", grad_src="web_verified", grad_cite=NA, grad_conf="high",
             city="San Francisco",
             rounds=[rnd("2013-04-16", "Seed", 1000000, BVP, True, NS, "press"),
                     rnd("2014-03-18", "Series A", 6650000, BVP, True, NA, "press")],
             note="TechCrunch (2013-04-16): '$1 million in seed funding. The round was led by Bessemer Venture Partners'; the firm's own date for it is 2012-08-09. Graduated: TechCrunch (2014-03-18), 'Nitrous.IO Closes $6.65M Series A Round Led By Bessemer'. "
                  "The company announced on 2016-10-31 that it was shutting the service down on November 14 (" + NX + "), so defunct. San Francisco from knowledge (the founders moved from Singapore)."))

BK = NEWS("vidyard", "Raises $18M")
TCV = "https://techcrunch.com/2015/01/14/video-technology-brings-millennial-marketers-to-vidyard/"
L.append(cls("vidyard", stage="Growth", stage_src="web_verified", stage_cite=BK, stage_conf="high", entry_date="2014-12-03",
             country="CA", country_src="web_verified", country_cite=TCV, clear=("country_unknown",),
             rounds=[rnd("2013-03-21", "Series A", 6000000, "OMERS Ventures", False,
                         "https://techcrunch.com/2013/03/21/vidyard-series-a/", "press"),
                     rnd("2015-01-14", "Series B", 18000000, BVP, True, BK, "press"),
                     rnd("2016-01-26", "Series C", 35000000, "Battery Ventures", True,
                         "https://techcrunch.com/2016/01/26/vidyard-series-c/", "press")],
             note="BetaKit (2015-01-14): the $18M Series B 'is led by Bessemer Venture Partners with participation from existing investors', and Byron Deeter joined the board; the firm's own date is 2014-12-03. Bessemer was not in the 2013 Series A, so the entry is Growth. TechCrunch calls Vidyard 'a Kitchener, Ontario-based company', which confirms Canada."))

L.append(cls("isight-partners", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014",
             rounds=[rnd("2015-01", "Series C", 30000000, BVP, True, None, "press")],
             note="Entered at the $30M Series C that Bessemer led, announced in January 2015 (from knowledge; two news queries returned no page naming the round). The firm's 2014 date is a year-end placeholder for that close."))

L.append(cls("knowme", city="New York",
             note="KnowMe was the New York company of filmmaker Andrew Jarecki (headlines in Inc. and Inverse, early 2016; city from knowledge). What became of it after 2016 and the round Bessemer entered were not found."))

TT = "https://techcrunch.com/2017/02/07/traveltriangle-closes-10-million-series-b/"
L.append(cls("travel-triangle", stage="Series A", stage_src="web_verified", stage_cite=TT, stage_conf="high",
             entry_date="2015-05-08",
             rounds=[rnd("2014-07", "pre-Series A", 1700000, "SAIF Partners", False, TT, "press"),
                     rnd("2015-04", "Series A", 8000000, BVP, True, TT, "press"),
                     rnd("2017-02-07", "Series B", 10000000, "RB Investments", True, TT, "press")],
             note="TechCrunch (2017-02-07): 'SAIF led TravelTriangle's $1.7 million pre-Series A in July 2014, while Bessemer led the $8 million Series A which closed in April 2015'. The firm's own date, 2015-05-08, is kept."))

GL = NEWS("oryx-vision", "raises $50m")
IE = NEWS("oryx-vision", "Oust Lidar")
L.append(cls("oryx-vision", stage="Series A", stage_src="web_verified", stage_cite=GL, stage_conf="medium", entry_date="2016",
             city="Petah Tikva", city_src="web_verified",
             rounds=[rnd("2016-11", "Series A", 17000000, None, True, IE, "press"),
                     rnd("2017-08-08", "Series B", 50000000, "Third Point Ventures; WRV", True, GL, "press")],
             note="Globes (2017-08-08): the $50M Series B included 'existing investors Bessemer Venture Partners, Maniv Mobility and Trucks VC', and 'the Petah Tikva based company raised $17 million, 15 months ago when it came out of stealth'; IEEE Spectrum names that $17M round the Series A. It was the only round before the Series B, so Bessemer entered at the Series A; no page read says who led it."))

GA = NEWS("applitools", "buys control")
L.append(cls("applitools", city="San Mateo", city_src="web_verified",
             note="Globes (2021-03-30): Applitools has 'headquarters in San Mateo, California and development center in Israel' and had raised $46M 'from Magma, Bessemer Venture Partners, iAngels, OpenView and private investors' (" + GA + "); San Mateo replaces San Francisco. No source read names the round of Bessemer's May 2017 entry."))

CAL = NEWS("hysolate", "Raises $18 Million")
L.append(cls("hysolate", stage="Growth", stage_src="web_verified", stage_cite=CAL, stage_conf="high", entry_date="2018-09-05",
             rounds=[rnd("2018-01", "first round", 8000000, "Innovation Endeavors; Team8", False, CAL, "press"),
                     rnd("2018-10-03", "Series B", 18000000, "Bessemer Venture Partners; Innovation Endeavors", True, CAL, "press")],
             note="Calcalist (2018-10-03): Hysolate 'announced ... the completion of an $18 million Series B funding round' led by Bessemer Venture Partners and Innovation Endeavors, after $8M from Innovation Endeavors and Team8 in January 2018. The firm's own date is 2018-09-05."))

EET = NEWS("dune-networks", "Broadcom to acquire Dune")
L.append(cls("dune-networks", country="US", country_src="web_verified", country_cite=EET, city="Sunnyvale",
             city_src="web_verified", clear=("country_unknown",),
             note="EE Times (2009-11-30): Broadcom agreed to buy Dune Networks, 'based in Sunnyvale, California', for about $178M; Globes adds a second office in Yakum, Israel and names Pitango and Evergreen among its backers, not Bessemer. The firm lists it without a year, and no source read ties Bessemer to a round."))

CBN = NEWS("topfreegames", "Newest Unicorn: Wildlife")
WS = STORED("wildlife-studios")
L.append(cls("topfreegames", status="private", rng="1b_plus", usd=WS["valuation_usd"], val_src="web_verified",
             val_cite=WS["valuation_citation"], asof=WS["valuation_asof"], val_conf="high",
             entry_date="2012", country="BR", country_src="web_verified", country_cite=CBN, city="Sao Paulo",
             flags=["stale"], extra={"valuation_range_source": "web_verified"},
             note="Top Free Games (TFG) is the former name of Wildlife Studios: the firm's live page for Wildlife Studios sits at bvp.com/portfolio/topfreegames and says 'formerly TFG'. This row is the same company as wildlife-studios and is aligned to it (Sao Paulo, per Crunchbase News; $3B mark of August 2020, older than 24 months; the firm's 2012 year). The two rows should be merged. The 2012 round is not named."))

TCS = "https://techcrunch.com/2022/02/01/vendorpm-raises-6m-to-scale-its-marketplace-for-property-managers-and-service-vendors/"
VA = NEWS("vendorpm", "Closes $20M Series A")
L.append(cls("vendorpm", stage="Seed", stage_src="web_verified", stage_cite=TCS, stage_conf="high", entry_date="2021",
             grad="graduated", grad_src="web_verified", grad_cite=VA, grad_conf="high",
             rounds=[rnd("2022-02-01", "Seed", 6000000, BVP, True, TCS, "press"),
                     rnd("2022-08-23", "Series A", 20000000, None, None, VA, "company")],
             note="TechCrunch (2022-02-01): VendorPM 'has raised $6 million in seed funding led by Bessemer Venture Partners'; the firm's own year for it is 2021. Graduated: the company's release of 2022-08-23, 'VendorPM Closes $20M Series A'."))

LI = NEWS("makersplace", "ledgerinsights")
NP = NEWS("makersplace", "Immediate Closure")
L.append(cls("makersplace", status="defunct", stage="Series A", stage_src="web_verified", stage_cite=LI, stage_conf="high",
             entry_date="2021-08",
             rounds=[rnd("2021-08-04", "Series A", 30000000, "Bessemer Venture Partners; Pantera Capital", True, LI, "press")],
             note="Ledger Insights (2021-08-05): 'MakersPlace announced a Series A investment of $30 million led by Bessemer Venture Partners and Pantera Capital'. The company announced on 2025-01-16 that it was ceasing operations, with NFT transfers ending in June 2025 (" + NP + "), so defunct."))

ZV = "https://finder.startupnationcentral.org/company_page/zenzap"
L.append(cls("zenzap",
             rounds=[rnd("2024-04", "Seed", None, None, True, ZV, "vendor")],
             note="A vendor database (Start-Up Nation Finder) lists a seed round of April 2024 with Bessemer and The Garage for a company founded in April 2022 in Tel Aviv; no press, company or firm page naming the round was found (web search and two news queries, 2026-10-06), so the stage stays undetermined."))

jl.write("s23b", L)
