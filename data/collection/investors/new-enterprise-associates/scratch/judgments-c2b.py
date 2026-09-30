"""PRO-100 NEA grind, queue batch 4 (judge c2): 45 listed members, classification only.
Each row read from the firm's own listing and posts first, then SEC filings, then press and Wikipedia.
Run: NQ_TAG=c2 python3 judgments-c2b.py"""
import importlib.util
import os
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, rnd, POST, SITE, W, NEWS, FTS = jl.cls, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.FTS
L = []
VW = {"valuation_range_source": "web_verified"}
GRAD_LEFT = "Graduation left for the graduation pass."
ASOF = "2026-09-30"
X1 = ("The firm labels this entry Public/PIPES: a private placement into an already listed company, which decisions "
      "X1 reads as out unless an NEA private round came first; no earlier NEA round is on record, so the membership "
      "should be re-judged under X1.")

# ---------------------------------------------------------------- old book, acquired, round not on record
L.append(cls("bravo-health", status="acquired", rng="below_1b", country="US", city="Baltimore", stage="undetermined",
             entry_date="1994", focus="Healthcare & Bio",
             note="Bravo Health (formerly Elder Health), Medicare Advantage plans, Baltimore; acquired by HealthSpring in "
                  "2010, the firm's exit line (HealthSpring later became part of Cigna). NEA's first investment is 1994; "
                  "no source read names the round.",
             rounds=[]))

L.append(cls("careerbuilder", status="acquired", rng="below_1b", country="US", city="Reston", stage="undetermined",
             entry_date="1996", focus="Consumer & Marketplaces",
             note="CareerBuilder Inc., online recruiting (Reston VA), listed on Nasdaq in 1999 and bought in 2000 by "
                  "Tribune and Knight Ridder, which merged it with CareerPath (the firm's exit line; the business later "
                  "moved to Chicago). NEA's first investment is 1996; no source read names the round.",
             rounds=[]))

L.append(cls("cardiothoracic-systems", status="acquired", rng="below_1b", country="US", city="Cupertino",
             stage="undetermined", entry_date="1995", focus="Healthcare & Bio",
             note="CardioThoracic Systems, instruments for beating-heart bypass surgery (Cupertino CA); listed on Nasdaq "
                  "(CTSI) in 1996 and acquired by Guidant in 1999, the firm's exit line. NEA's first investment is 1995; "
                  "no source read names the round.",
             rounds=[]))

L.append(cls("cardiovascular-imaging-systems", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
             stage="undetermined", entry_date="1987", focus="Healthcare & Bio",
             note="Cardiovascular Imaging Systems, intravascular ultrasound catheters (Sunnyvale CA); listed on Nasdaq "
                  "(CVIS) and acquired by Boston Scientific in 1995, the firm's exit line. NEA's first investment is "
                  "1987; no source read names the round.",
             rounds=[]))

L.append(cls("carrier-access-corporation", status="acquired", rng="below_1b", country="US", city="Boulder",
             stage="undetermined", entry_date="1997", focus="Data Infrastructure",
             note="Carrier Access, telecom access equipment (Boulder CO), listed on Nasdaq in 1998 and acquired by Turin "
                  "Networks in 2008 (Turin later went to Force10, the firm's exit line), as in the Menlo row. NEA's first "
                  "investment is 1997; no source read names the round.",
             rounds=[]))

L.append(cls("broadview-network-holdings", status="acquired", rng="below_1b", country="US", city="Rye Brook",
             stage="undetermined", entry_date="2005", focus="Data Infrastructure",
             note="Broadview Networks, integrated communications for businesses (Rye Brook NY), founded 1996; Windstream "
                  "agreed to buy it in April 2017 for $227.5M in cash (Wikipedia). Wikipedia lists NEA among its "
                  "shareholders with Baker Capital, MCG and others; NEA's first investment is 2005 and no source read "
                  "names the round.",
             rounds=[]))

L.append(cls("bridgepoint-medical", status="acquired", rng="below_1b", city="Plymouth", city_src="formd_address",
             stage="undetermined", entry_date="2002", focus="Healthcare & Bio",
             note="BridgePoint Medical, catheter systems for chronic total occlusions (Plymouth MN, the Form D address); "
                  "acquired by Boston Scientific, the firm's exit line. NEA's first investment is 2002 (the firm's own "
                  "year), which replaces the 2009 entry date on file read off a later Form D; no source read names the "
                  "round.",
             rounds=[]))

L.append(cls("carticept-medical", status="acquired", rng="below_1b", city="Alpharetta", city_src="formd_address",
             stage="undetermined", entry_date="2005", focus="Healthcare & Bio",
             note="Carticept Medical, osteoarthritis and cartilage devices (Alpharetta GA, the Form D address); it went "
                  "to Cartiva, itself bought by Wright Medical Group (the firm's exit line). NEA's first investment is "
                  "2005 (the firm's own year), which replaces the 2010 entry date on file read off a later Form D; no "
                  "source read names the round.",
             rounds=[]))

L.append(cls("cartiva", status="acquired", rng="below_1b", city="Alpharetta", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Cartiva, synthetic cartilage implants (Alpharetta GA, the Form D address); acquired by Wright Medical "
                  "Group in 2018, the firm's exit line. " + GRAD_LEFT))

L.append(cls("brightkite", status="defunct", rng="below_1b", country="US", city="Burlingame",
             city_src="formd_address", stage="undetermined", focus="Consumer & Marketplaces",
             note="Brightkite, location-based social network; the mobile network Limbo acquired it in April 2009 and the "
                  "combined company filed as Brightkite, Inc. from Burlingame CA (Form D, 2009, Peter Sonsini a "
                  "director). By December 2011 its apps were pulled and by April 2012 the site was gone (Wikipedia): "
                  "defunct. No source read names NEA's round.",
             rounds=[]))

L.append(cls("carezone", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Healthcare & Bio",
             note="CareZone, medication and care-management app (San Francisco, the Form D address); Walmart acquired it "
                  "in 2020, the firm's exit line. The Form D band's Series A entry (2012, Greg Papadopoulos a director) "
                  "stands."))

L.append(cls("burrow", status="acquired", rng="below_1b", city="New York", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="Burrow, modular furniture sold direct (New York); acquired by Havenly, the firm's exit line, as in the "
                  "General Catalyst and Y Combinator rows."))

CASPER_W = W("Casper Sleep")
L.append(cls("casper", status="acquired", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             note="Casper Sleep, mattresses (New York). Listed on the NYSE in 2020, taken private by Durational Capital "
                  "in 2022 (the firm's exit line) and acquired by Carpenter Co. in October 2024 (Wikipedia). The Form D "
                  "band's Series A entry agrees with Wikipedia: a $13.1M Series A in 2014 with NEA among the investors, "
                  "after a $1.85M seed.",
             rounds=[rnd("2014", "Seed", 1850000, None, None, CASPER_W, "press"),
                     rnd("2014", "Series A", 13100000, None, True, CASPER_W, "press")]))

# ---------------------------------------------------------------- public or once-public rows
CARE_S1 = "https://www.sec.gov/Archives/edgar/data/1412270/000141057813000222/filename1.htm"
CARE_W = W("Care.com")
L.append(cls("care-com", city="Dallas", city_src="web_verified", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=CARE_S1, rng="below_1b", focus="Consumer & Marketplaces",
             note="Care.com, marketplace for family care (Wikipedia: headquartered in Dallas, bought by IAC in February "
                  "2020); the IVP row reads Waltham, its home through the IPO, and should align. Its draft S-1 "
                  "(2013-09-13) lists New Enterprise Associates 13 buying $13.5M of Series C preferred, then Series D "
                  "and E; Matrix had led the $3.5M Series A in 2007 (Wikipedia). The Series C is the October 2010 Form D "
                  "round, the firm's first-investment year: Growth.",
             rounds=[rnd("2007", "Series A", 3500000, "Matrix Partners", False, CARE_W, "press"),
                     rnd("2010-10", "Series C", None, None, True, CARE_S1, "filing")]))

CA_IRA = "https://www.sec.gov/Archives/edgar/data/1169652/000095012312013832/filename13.htm"
CA_S1 = "https://www.sec.gov/Archives/edgar/data/1169652/000095012312013832/filename1.htm"
L.append(cls("channeladvisor", city="Morrisville", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=CA_IRA, entry_date="2007-04", rng="below_1b", focus="SaaS",
             note="ChannelAdvisor, e-commerce channel software (Morrisville NC); listed on the NYSE in 2013, acquired by "
                  "CommerceHub in 2022. Its draft S-1 dates Series A to December 2003, Series B to April 2005, Series B-1 "
                  "to April 2006 and Series C to April 2007; the investors' rights agreement entered with the Series C "
                  "purchase defines NEA as New Enterprise Associates 12 and NEA Ventures 2007, and Patrick Kerins joined "
                  "the board in 2007, the firm's first-investment year: Growth.",
             rounds=[rnd("2003-12", "Series A", None, None, False, CA_S1, "filing"),
                     rnd("2005-04", "Series B", 18000000, None, False, CA_S1, "filing"),
                     rnd("2006-04", "Series B-1", 3000000, None, False, CA_S1, "filing"),
                     rnd("2007-04", "Series C", None, None, True, CA_IRA, "filing")]))

GYRE_CAP = "https://stockanalysis.com/stocks/gyre/market-cap/"
L.append(cls("catalyst-biosciences", rng="below_1b", usd=767680000, val_src="web_verified", val_cite=GYRE_CAP,
             asof=ASOF, extra=VW, country="US", city="San Diego", stage="Growth", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("catalyst-biosciences"), entry_date="2002",
             focus="Healthcare & Bio", flags=["model_disputes_source"],
             note="The firm's description (nicotinic-receptor drugs for CNS disorders) is Targacept, NEA's 2002 "
                  "investment, which merged with Catalyst Biosciences in 2015; Catalyst in turn combined with Gyre "
                  "Therapeutics in 2023 (Nasdaq: GYRE, San Diego, its listing profile). The firm's own listing labels "
                  "the 2002 entry Growth. Market cap $767.68M as of 2026-09-30 (stockanalysis.com) replaces the $72.6M "
                  "float on file; still below $1B."))

CELC_CAP = "https://stockanalysis.com/stocks/celc/market-cap/"
L.append(cls("celcuity", rng="1b_plus", usd=3830000000, val_src="web_verified", val_cite=CELC_CAP, asof=ASOF,
             extra=VW, country="US", city="Minneapolis", stage="undetermined", entry_date="2022",
             focus="Healthcare & Bio", flags=["model_disputes_source"],
             note="Celcuity, targeted cancer drugs (Minneapolis). NEA joined the May 2022 private placement led by "
                  "Venrock Healthcare Capital Partners (8-K, 2022-05-16), years after the 2017 listing. Market cap "
                  "$3.83B as of 2026-09-30 (stockanalysis.com) replaces the $457M float on file: band 1b_plus. " + X1))

CSBR_PROFILE = "https://stockanalysis.com/stocks/csbr/company/"
L.append(cls("champions-oncology", city="Hackensack", city_src="web_verified", stage="undetermined",
             entry_date="2015", focus="Healthcare & Bio",
             note="Champions Oncology, preclinical and translational oncology research services; its listing profile "
                  "gives One University Plaza, Hackensack NJ (" + CSBR_PROFILE + "), with labs in Maryland; the Battery "
                  "row reads Baltimore and should align. NEA 14 bought in through the March 2015 securities purchase "
                  "agreement with Battery (8-K, 2015-03-12), when the company already traded. " + X1))

L.append(cls("cadence-pharmaceuticals", country="US", city="San Diego", stage="undetermined", entry_date="2009",
             rng="below_1b", focus="Healthcare & Bio",
             note="Cadence Pharmaceuticals, hospital products (San Diego); listed on Nasdaq in 2006, acquired by "
                  "Mallinckrodt in 2014. NEA joined the February 2009 private placement led by Venrock (8-K, "
                  "2009-02-20). " + X1))

L.append(cls("cascadian-therapeutics", country="US", city="Seattle", stage="undetermined", entry_date="2016",
             rng="below_1b", focus="Healthcare & Bio",
             note="Cascadian Therapeutics (formerly Oncothyreon, Seattle), cancer drugs; acquired by Seattle Genetics in "
                  "2018. NEA held 7.9% by October 2016 (proxy), bought as a listed company in 2016, one of the Growth "
                  "Equity Opportunities 13D issuers (decisions R2). " + X1))

L.append(cls("cerecor", city="Wayne", city_src="web_verified", focus="Healthcare & Bio",
             note="Cerecor was renamed Avalo Therapeutics (Nasdaq: AVTX) and is now headquartered at 1500 Liberty Ridge "
                  "Drive, Wayne PA (its listing profile, stockanalysis.com); the Form D address was Baltimore."))

L.append(cls("bright-health", city="Doral", city_src="web_verified", rng="below_1b", focus="Healthcare & Bio",
             note="Bright Health Group renamed itself NeueHealth and moved its headquarters to Doral FL, as in the Tiger "
                  "Global row (the Headline row reads Minneapolis, its original home, and should align); in December 2024 "
                  "NEA agreed to take NeueHealth private, the acquisition on file. Below $1B."))

CHELSIO_W = W("Chelsio Communications")
L.append(cls("chelsio-communications", status="private", rng="below_1b", city="Sunnyvale", city_src="web_verified",
             stage="undetermined", entry_date="2002", focus="Industrial & Robotics",
             note="Chelsio Communications, fabless semiconductor company for high-speed Ethernet adapters, privately "
                  "held and headquartered in Sunnyvale (Wikipedia). Wikipedia lists NEA among its early venture "
                  "investors, with a Series D in 2006 and a $25M Series E by January 2008, and it still ships products "
                  "(T7 DPU sampling, 2025); NEA's first investment is "
                  "2002 (the firm's own year), which replaces the 2009 entry date on file, and no source read names "
                  "the round.",
             rounds=[rnd("2006", "Series D", None, None, None, CHELSIO_W, "press"),
                     rnd("2008-01", "Series E", 25000000, None, None, CHELSIO_W, "press")]))

L.append(cls("caremark-rx-inc", status="acquired", rng="below_1b", country="US", city="Nashville",
             stage="undetermined", focus="Healthcare & Bio",
             note="Caremark Rx (formerly MedPartners), pharmacy benefit manager, moved from Birmingham to Nashville in "
                  "2003 and merged with CVS in 2007 (Wikipedia, CVS Caremark). The firm listed it only in its 2008 and "
                  "2013 archive with no investment year, and NEA's one filing is a 13G of 2000-02-11, when MedPartners "
                  "had been listed since 1995: the stake reads as a listed holding or sale consideration from a "
                  "portfolio company MedPartners bought (decisions D8, X1), so the membership should be re-judged.",
             rounds=[]))

BD_W = W("ByteDance")
BD_BUY = NEWS("bytedance-toutiao", "sets valuation at over US$330 billion")
L.append(cls("bytedance-toutiao", status="private", rng="100b_plus", usd=330000000000, val_src="web_verified",
             val_cite=BD_BUY, asof="2025-08-27", extra=VW, country="CN", country_src="web_verified",
             country_cite=BD_W, city="Beijing", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2018", focus="Media, Gaming & Advertising",
             note="ByteDance (Toutiao, Douyin, TikTok), based in Haidian, Beijing (Wikipedia). Mark: the company's own "
                  "employee share buyback at $200.41 a share, valuing it at over $330B (The Business Times, from "
                  "Reuters, 2025-08-27), a priced repurchase by the company; later secondary reports ($480B in a "
                  "November 2025 share auction, $550B in General Atlantic's proposed 2026 sale) stay out of the figure. "
                  "Stage: NEA's first investment is 2018, when ByteDance had already raised Series A to E and a "
                  "pre-IPO round (SoftBank-led, 2018), so any NEA entry, primary or secondary, is Growth; no source "
                  "read names NEA's round.",
             rounds=[]))

BZ_W = W("BuzzFeed")
L.append(cls("buzzfeed", city="New York", stage="Growth", stage_src="model", stage_conf="medium",
             focus="Media, Gaming & Advertising",
             note="BuzzFeed, digital media (New York), listed on Nasdaq (BZFD) through a SPAC in December 2021. NEA's "
                  "entry is the $15.5M round announced in January 2012 (Wikipedia; Form D first sale 2011-12-23, Patrick "
                  "Kerins a director), which followed the company's 2008 round and an $8M round filed in 2010: a third "
                  "institutional round above the era's $15M Series A ceiling, Growth. NEA also led the $19.3M round of "
                  "January 2013 (Wikipedia).",
             rounds=[rnd("2010", None, 8000000, None, False, None, "filing"),
                     rnd("2012-01", None, 15500000, "NEA", True, BZ_W, "press"),
                     rnd("2013-01", None, 19300000, "NEA", True, BZ_W, "press")]))

L.append(cls("change-io", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("change-io"), entry_date="2022", focus="Fintech & Payments",
             flags=["city_unknown"],
             note="Change (GetChange Corp., getchange.io), donation APIs linking companies to charities. The firm's own "
                  "listing labels its 2022 first investment Seed. Momentum check 2026-09-30 (Google News, the company's "
                  "name with donation API and raise words): no round found, below $1B. Its site gives no headquarters "
                  "city. " + GRAD_LEFT))

CHAOS_C = NEWS("chaos", "Defense Tech Startup Chaos Industries Hits $2B Valuation")
CHAOS_D = NEWS("chaos", "CHAOS Industries Raises $510M at a $4.5B Valuation")
L.append(cls("chaos", status="private", rng="1b_plus", usd=4500000000, val_src="web_verified", val_cite=CHAOS_D,
             asof="2025-11-14", extra=VW, country="US", city="Los Angeles", city_src="web_verified",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CHAOS_C, entry_date="2025-05-02",
             focus="Industrial & Robotics",
             note="CHAOS Industries, radar and sensing for drone and missile detection and defense networking (Los "
                  "Angeles, Crunchbase News). Crunchbase News (2025-05-02): Accel and NEA co-led the $275M Series C at a "
                  "$2B valuation, after a $145M Series B; NEA's first-investment year is 2025, so the entry is the Series "
                  "C, Growth. Mark: the $510M round led by Valor Equity Partners at a $4.5B valuation (Tectonic, "
                  "2025-11-14). The 8VC and Accel rows read below $1B and should align; the General Catalyst and "
                  "Lightspeed rows named Chaos are a different company (a New York crypto firm).",
             rounds=[rnd("2024-11-12", "Series B", 145000000, None, None, CHAOS_C, "press"),
                     rnd("2025-05-02", "Series C", 275000000, "Accel; NEA", True, CHAOS_C, "press"),
                     rnd("2025-11-14", "Series D", 510000000, "Valor Equity Partners", None, CHAOS_D, "press")]))

CANDY_A = NEWS("candy", "brings in $100m through Series A funding")
L.append(cls("candy", country="US", city="New York", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=CANDY_A, entry_date="2021-10-22", rng="below_1b", focus="Crypto & Web3",
             flags=["model_disputes_source"],
             note="Candy Digital, licensed sports and entertainment NFTs, founded in 2021 by Fanatics with Galaxy Digital "
                  "and VaynerMedia (New York); the Italian country on file came from a one-word name match (the "
                  "appliance maker Candy) and is replaced. Sportcal (2021-10-22): a $100M Series A at a $1.5B valuation "
                  "led by Insight Partners and SoftBank Vision Fund 2, with NEA participating, the firm's first-"
                  "investment year. Futureverse acquired it in April 2025 (Axios) and the Tad Smith family bought it in "
                  "2026 (National Law Review): acquired, below $1B.",
             rounds=[rnd("2021-10-22", "Series A", 100000000, "Insight Partners; SoftBank Vision Fund 2", True, CANDY_A,
                         "press")]))

CERAMIC_S = NEWS("ceramic", "Former Google VP of Engineering and Gradient Ventures founder raises $12M")
L.append(cls("ceramic", status="private", rng="below_1b", country="US", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=CERAMIC_S, entry_date="2025-03-05", grad="censored",
             focus="AI & Applied AI", flags=["city_unknown"],
             note="Ceramic.ai, infrastructure to train and deploy AI models faster, founded by former Google VP Anna "
                  "Patterson. Tech Funding News (2025-03-05): a $12M seed led by NEA with IBM, Samsung Next and "
                  "Earthshot; the firm's listing labels it Seed with a 2024 first investment. The entry is inside 24 "
                  "months, censored. Momentum check 2026-09-30 (Google News, 'Ceramic AI raises'): no later round, below "
                  "$1B. No source read states a headquarters city.",
             rounds=[rnd("2025-03-05", "Seed", 12000000, "NEA", True, CERAMIC_S, "press")]))

L.append(cls("built-robotics", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Industrial & Robotics",
             note="Built Robotics, autonomy kits for construction equipment, now solar pile-driving robots (San "
                  "Francisco). A $33M Series B in 2019 and a $64M Series C in April 2022 (TechCrunch) with no valuation "
                  "disclosed; below $1B, as in the Tiger Global row. The Form D band's Series A entry (2017, Forest "
                  "Baskett a director) stands."))

L.append(cls("cardioxyl-pharmaceuticals", status="acquired", rng="below_1b", city="Chapel Hill",
             city_src="formd_address", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("cardioxyl-pharmaceuticals"), entry_date="2006", focus="Healthcare & Bio",
             note="Cardioxyl Pharmaceuticals, nitroxyl donors for heart failure (Chapel Hill NC, the Form D address); "
                  "acquired by Bristol Myers Squibb in 2015, the firm's exit line. The firm's own listing labels its "
                  "2006 first investment Seed, which replaces the 2009 entry date on file read off a later Form D; later "
                  "offerings of $9M (2009), $15M (2010) and $28M (2012) are unnamed. " + GRAD_LEFT))

L.append(cls("canopy", status="private", rng="below_1b", city="Lehi", city_src="formd_address", focus="SaaS",
             note="Canopy, practice management and tax resolution software for accounting firms (Lehi UT, the Form D "
                  "address), still operating (CPA Practice Advisor, 2025-2026) and raising (a $36.5M Form D offering in "
                  "2025); no valuation on record, below $1B. The a16z, General Catalyst and Y Combinator rows named "
                  "Canopy are different companies. The Form D band's Series A entry (2015, Chetan Puttagunta a "
                  "director) stands."))

L.append(cls("catalog", status="acquired", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             stage="undetermined", entry_date="2017", focus="Data Infrastructure",
             note="Catalog Technologies, DNA-based data storage (Boston). Its domain now redirects to Biomemory, whose "
                  "site says 'Biomemory acquires key assets from Catalog', adding a production and R&D footprint in "
                  "Boston: an asset sale, acquired with Biomemory (Paris) as successor. NEA's first investment is 2017; "
                  "no source read names the round.",
             rounds=[]))

L.append(cls("broadly", status="private", rng="below_1b", country="US", city="Boca Raton", city_src="web_verified",
             stage="undetermined", entry_date="2015", focus="SaaS",
             note="Broadly, reviews and customer messaging software for local businesses. Its site (Broadly Inc.) is live "
                  "and gives 951 Yamato Road, Boca Raton FL as its address; the company began in the San Francisco Bay "
                  "Area. NEA's first investment is 2015; Google News carries no round of the company under its generic "
                  "name, so the round is not on record.",
             rounds=[]))

BRENIG_A = NEWS("brenig", "Neurology-Focused Drug Development Company Secures")
L.append(cls("brenig", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=BRENIG_A, focus="Healthcare & Bio", flags=["city_unknown",
                                                                                        "stage_disputes_band"],
             note="Brenig Therapeutics, brain-penetrant small molecules for Parkinson's disease (LRRK2) and "
                  "neuroinflammation (NLRP3). Pulse 2.0 (2024-07-25): a $65M Series A led by NEA with existing backers "
                  "OrbiMed, Torrey Pines Investment and BioGeneration Ventures; NEA's first-investment year is 2024, so "
                  "the entry is the Series A, and the Form D band's Growth (read from the $65M size) is disputed; the "
                  "entry date stays the Form D first sale. The Form D and site give only a Dover DE registered-agent "
                  "address, so no city is placed. No valuation disclosed.",
             rounds=[rnd("2024-07-16", "Series A", 65000000, "NEA", True, BRENIG_A, "press")]))

CENT_A = NEWS("centralize", "Former Meta And Slack Engineers Raise $15M")
L.append(cls("centralize", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=CENT_A, entry_date="2026-07-29", focus="AI & Applied AI",
             note="Centralize, AI relationship intelligence for enterprise sales (San Francisco), Y Combinator Winter "
                  "2024. Crunchbase News (2026-07-29): a $15M Series A led by NEA with Salesforce Ventures and Y "
                  "Combinator, after a $4M seed, $19M in total; NEA's first-investment year is 2026, so the entry is the "
                  "Series A. No valuation disclosed; momentum check 2026-09-30 (Google News): no later round, below "
                  "$1B. The Y Combinator row is the same company and agrees.",
             rounds=[rnd("2024", "Seed", 4000000, None, False, CENT_A, "press"),
                     rnd("2026-07-29", "Series A", 15000000, "NEA", True, CENT_A, "press")]))

L.append(cls("cardurion", status="private", rng="below_1b", city="Burlington", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Cardurion Pharmaceuticals, cardiovascular drugs (Burlington MA, the Form D address). NEA's entry is "
                  "the $260M Series B of July 2024 (Fierce Biotech, BioPharma Dive), which agrees with the Form D band's "
                  "Growth; Edward Mathers joined the board. No valuation disclosed, below $1B."))

CATHAY_CAP = "https://stockanalysis.com/quote/sha/688065/market-cap/"
CATHAY_F1 = "https://www.sec.gov/Archives/edgar/data/1517546/000104746911006440/a2204377zf-1.htm"
L.append(cls("cathay-industrial-biotech", status="public", rng="1b_plus", usd=4153904505, val_src="web_verified",
             val_cite=CATHAY_CAP, asof=ASOF, extra=VW, country="CN", country_src="web_verified",
             country_cite=CATHAY_CAP, city="Shanghai", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("cathay-industrial-biotech"), entry_date="2007", focus="Industrial & Robotics",
             note="Cathay Industrial Biotech, bio-based long-chain dicarboxylic acids and polyamides (Shanghai). Its "
                  "2011 F-1 (withdrawn) lists New Enterprise Associates 12 among the preferred investors; the company "
                  "listed on the Shanghai STAR Market in 2020 as Cathay Biotech (688065). Market cap CNY 27.85B as of "
                  "2026-09-30 (stockanalysis.com): CNY 27.85B @ ECB 2026-09-30 (CNY/EUR 7.613, EUR/USD 1.1355) = "
                  "$4.15B, band 1b_plus. The firm's own listing labels its 2007 entry Growth.",
             rounds=[rnd("2007", None, None, None, True, CATHAY_F1, "filing")]))

CAUSES_W = W("Causes (company)")
L.append(cls("causes", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2010", focus="Consumer & Marketplaces",
             note="Causes, online activism platform co-founded by Sean Parker (San Francisco); it became part of Brigade "
                  "Media (the firm's exit line), and Countable Corporation acquired Causes and Brigade in 2019 "
                  "(Wikipedia). Wikipedia names NEA among its investors with Founders Fund and the Case Foundation; "
                  "NEA's first investment is 2010 and no source read names the round.",
             rounds=[]))

L.append(cls("catalytic", status="acquired", rng="below_1b", city="Chicago", city_src="formd_address", focus="SaaS",
             note="Catalytic, no-code workflow automation (Chicago, the Form D address); acquired by PagerDuty in 2022, "
                  "the firm's exit line and Built In Chicago's list of 2022 acquisitions. " + GRAD_LEFT))

L.append(cls("centerbeam", status="acquired", rng="below_1b", city="Sunnyvale", city_src="formd_address",
             stage="undetermined", entry_date="1999", focus="Data Infrastructure",
             note="CenterBeam, outsourced IT management for mid-sized enterprises (Sunnyvale, the Form D address); "
                  "EarthLink bought it for $22M in June 2013 (Data Center Dynamics), the firm's archived exit line. "
                  "NEA's first investment is 1999 (the firm's own year), which replaces the 2013 entry date on file "
                  "read off a late Form D; no source read names the round.",
             rounds=[]))

L.append(cls("centrexion-therapeutics", status="private", rng="below_1b", city="Boston", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Centrexion Therapeutics, non-opioid pain drugs (Boston, the Form D address). It withdrew its IPO in "
                  "May 2021 and its knee pain drug failed two Phase III studies in 2022 (Endpoints), but it kept "
                  "raising privately (Form D offerings of $30M in 2022 and $12.9M in 2024): private, below $1B. The Form "
                  "D band's Growth entry (2017, Sara Nayeem a director) agrees with the $67M round of January 2018 "
                  "(Fierce Biotech)."))

L.append(cls("charm-therapeutics", status="private", rng="below_1b", city="London", city_src="web_verified",
             focus="Healthcare & Bio",
             note="CHARM Therapeutics, AI-designed small molecules, lead program a next-generation menin inhibitor for "
                  "AML (London, EU-Startups 2025-09-02). NEA's entry is the $80M Series B of September 2025, co-led with "
                  "SR One (Snell & Wilmer; Pulse 2.0), which agrees with the Form D band's Growth; a $50M Series A came "
                  "in 2022 (TechCrunch) and NVIDIA's NVentures invested in 2023. No valuation disclosed, below $1B. The "
                  "General Catalyst row reads unknown and US; this London company is private."))

L.append(cls("cardionomic", status="private", rng="below_1b", city="Forest Lake", city_src="formd_address",
             stage="undetermined", entry_date="2010", focus="Healthcare & Bio",
             note="Cardionomic, catheter-based neuromodulation for acute decompensated heart failure (Forest Lake MN, "
                  "the Form D address), Ali Behbahani on the board. NEA's first investment is 2010 (the firm's own "
                  "year), which replaces the 2015 entry date on file read off the company's first Form D ($21.8M, 2015); "
                  "later offerings of $9.6M (2018), $16.8M (2020) and $11.5M (2021) are unnamed, and no source read names "
                  "NEA's round.",
             rounds=[]))

if not os.environ.get("C2_DRY"):
    jl.write("c2b", L)
