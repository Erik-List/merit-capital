"""PRO-100 NEA, judge c3, queue batch 6 (listed members, classification; three membership rulings)."""
import json
from pathlib import Path

import judge_lib as jl

cls, rnd, verdict, SITE, POST, W, NEWS, ARCH = jl.cls, jl.rnd, jl.verdict, jl.SITE, jl.POST, jl.W, jl.NEWS, jl.ARCH
SIBS = json.loads((Path(__file__).resolve().parent / "siblings.json").read_text())


def FTSU(reg, suffix):
    """A full-text-hit URL on disk: the filing of registrant `reg` whose URL ends with `suffix` (exactly one)."""
    m = sorted({f["url"] for r in jl._FTS if reg.lower() in r["registrant"].lower()
                for f in r.get("filings", []) if f["url"].endswith(suffix)})
    if len(m) != 1:
        raise SystemExit(f"FTSU({reg!r}, {suffix!r}) matched {m}")
    return m[0]


def SIBCITE(slug, investor):
    """The valuation citation a sibling book carries for the same company (rule 10 alignment)."""
    m = [x["val_cite"] for x in SIBS.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIBCITE({slug!r}, {investor!r}) matched {m}")
    return m[0]


WV = {"valuation_range_source": "web_verified"}
LEFT = "Graduation left for the graduation pass."

L = []

# ---- membership rulings (verdict line only)
L.append(verdict("cti-biopharma", "not_member",
                 "X1 (flagged, Erik's open delta): the firm labels the position Public/PIPES from 2018 and NEA's 13D filings "
                 "start in 2018, while CTI BioPharma (formerly Cell Therapeutics, Seattle) had been listed since 1997; no NEA "
                 "private round came first. If PIPEs are ruled venture entries it enters as Growth in 2018; status acquired "
                 "(Sobi, 2023).", ec="fund_filing", conf="high", cite=jl._base()["cti-biopharma"]["edgar_links"].split(";")[0].strip()))
L.append(verdict("dallas-semiconductor", "not_member",
                 "X1 (flagged, Erik's open delta): the firm labels its 1990 position Public/PIPES, a private placement into a "
                 "company already listed since the 1980s, and no record shows an earlier NEA private round. If PIPEs are ruled "
                 "venture entries it enters as Growth in 1990; Dallas, acquired by Maxim Integrated in 2001.",
                 ec="site_listing", conf="medium", cite=SITE("dallas-semiconductor")))
L.append(verdict("dsi-renal", "not_member",
                 "R1 control position: DSI Renal is Dialysis Newco, Inc., 'a portfolio company of Frazier Healthcare VI, L.P. "
                 "and New Enterprise Associates 13', formed to buy the 28 dialysis centers DaVita divested in September 2011 "
                 "(DaVita 10-K); the two sponsors bought the business, a control acquisition rather than a minority financing.",
                 ec="web", conf="medium", cite=FTSU("DAVITA HEALTHCARE", "d465470d10k.htm"),
                 extra={"exclusion": "control_position"}))

# ---- classification
# cuponation
L.append(cls("cuponation", status="private", rng="below_1b", stage="undetermined", entry_date="2012",
             country="DE", country_src="web_verified", country_cite=W("Global Savings Group"), city="Munich",
             focus="Consumer & Marketplaces",
             note="Coupon platform founded in 2012 with Rocket Internet, renamed Global Savings Group in 2016 and Atolls in 2024, "
                  "private and based in Munich (Wikipedia), as in the Headline book; NEA's 2012 round is not named."))

# curalate
L.append(cls("curalate", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011",
             city="Philadelphia", focus="SaaS",
             note="Visual commerce marketing software in Philadelphia, acquired by Bazaarvoice in 2021 (the firm's exit line); NEA's "
                  "first investment is the firm's 2011, earlier than the 2014 Form D, and its round is not named."))

# curana-health
L.append(cls("curana-health", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("curana-health"), stage_conf="medium", entry_date="2021", country="US", city="Austin",
             focus="Healthcare & Bio",
             note="Senior-living primary care and Medicare Advantage company NEA formed in 2021 by uniting Elite Patient Care, "
                  "Provider Health Services and AllyAlign Health (the firm's post of 2022-05-04); the firm's card reads Growth."))

# curisium
L.append(cls("curisium", status="acquired", rng="below_1b", city="Manhattan Beach", city_src="formd_address",
             focus="Healthcare & Bio",
             note=f"Blockchain value-based contracting platform acquired by HealthVerity (the firm's exit line); its Form D gives "
                  f"Manhattan Beach, California. {LEFT}"))

# curzion-pharmaceuticals
L.append(cls("curzion-pharmaceuticals", status="acquired", rng="below_1b", stage="undetermined", entry_date="2019",
             country="US", focus="Healthcare & Bio", flags=["city_unknown"],
             note="Systemic sclerosis drug developer acquired by Horizon Therapeutics in 2019 (the firm's exit line); no record "
                  "found places it in a city or names NEA's round."))

# cuspai
_CUSP = "https://theaiinsider.tech/2025/09/15/cuspai-announces-100m-series-a-to-accelerate-ai-powered-materials-discovery/"  # WebSearch, read with WebFetch
L.append(cls("cuspai", status="private", rng="1b_plus", usd=2.6e9, val_src="web_verified",
             val_cite=SIBCITE("cuspai", "northzone"), asof="2026-07-20", stage="Series A", stage_src="web_verified",
             stage_cite=_CUSP, stage_conf="high", entry_date="2025-09", country="GB", country_src="web_verified",
             country_cite=_CUSP, city="Cambridge", focus="AI & Applied AI", extra=WV,
             rounds=[rnd("2025-09", "Series A", 100_000_000, "New Enterprise Associates; Temasek", True, _CUSP, "press")],
             note="Cambridge, UK materials discovery AI company; NEA co-led the $100M Series A with Temasek in September 2025, its "
                  "first round. Marked at the $2.6B of the $450M Series B of July 2026, as in the Northzone book."))

# cv-ingenuity
_CVI = POST("cv-ingenuity-success")
L.append(cls("cv-ingenuity", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party", stage_cite=_CVI,
             stage_conf="high", entry_date="2011-09", city="Fremont", city_src="formd_address", focus="Healthcare & Bio",
             rounds=[rnd("2011-09", "Series B", None, "New Enterprise Associates", True, _CVI, "firm")],
             note="The firm's post says NEA led the Series B in September 2011 alongside the Series A investors, and Covidien "
                  "agreed to acquire the company at the end of 2012."))

# cvent
_CVENT = ARCH("cvent")
L.append(cls("cvent", rng="below_1b", stage="Growth", stage_src="first_party", stage_cite=_CVENT, stage_conf="medium",
             entry_date="2011-07", city="Tysons", focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2011-07", "growth investment", 136_000_000, "New Enterprise Associates", True, W("Cvent"), "press")],
             note="NEA put $136M into Cvent in July 2011 (Wikipedia) and the firm's archived card labels it growth, so the Pre-Seed "
                  "band read off a $0.9M 2012 filing is wrong. Acquired by Blackstone in 2023, as in the Insight book."))

# cvrx
L.append(cls("cvrx", city="Minneapolis", focus="Healthcare & Bio",
             note="Baroreflex therapy device maker headquartered in Minneapolis."))

# cybermedia
L.append(cls("cybermedia", status="acquired", rng="below_1b", stage="undetermined", entry_date="1995", country="US",
             city="Santa Monica", focus="SaaS",
             note="PC troubleshooting software maker (Nasdaq CYBR) acquired by Network Associates in 1998; the 1995 round is not named."))

# cydan
L.append(cls("cydan", status="unknown", rng="below_1b", city="Cambridge", city_src="formd_address", focus="Healthcare & Bio",
             note="Rare disease accelerator NEA helped form in late 2012 (the firm's post), later Cydan II in Cambridge, "
                  "Massachusetts (Form D); it left the firm's live list after 2023 and its current state is not on record."))

# cyence
L.append(cls("cyence", status="acquired", rng="below_1b", stage="undetermined", entry_date="2014", country="US",
             city="San Mateo", focus="Fintech & Payments",
             note="Cyber risk analytics for insurers acquired by Guidewire in 2017 (the firm's exit line; the IVP book agrees); "
                  "NEA's 2014 round is not named."))

# cyras-systems
L.append(cls("cyras-systems", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999", country="US",
             city="Fremont", focus="Data Infrastructure",
             note="Optical transport equipment maker acquired by Ciena in 2000 (the firm's exit line); the 1999 round is not named."))

# dandelion
L.append(cls("dandelion", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=SITE("dandelion"),
             stage_conf="medium", entry_date="2018", country="US", city="Mount Kisco", focus="Climate & Energy",
             note=f"Residential geothermal company spun out of Alphabet's X; the firm's card reads Seed in 2018. {LEFT}"))

# dasan-zhone-solutions-inc
L.append(cls("dasan-zhone-solutions-inc", rng="below_1b", city="Plano", focus="Data Infrastructure",
             note="Zhone Technologies renamed (DASAN Zhone Solutions, then DZS; base row zhone-technologies is the same company), "
                  "last based in Plano, Texas; it filed Chapter 7 in March 2025 and MSNi bought its assets in June 2025 "
                  f"({NEWS('dasan-zhone-solutions-inc', 'MSNi-owned Zhone Technologies snaps up DZS assets')}), so acquired stands."))

# data-critical-corporation
L.append(cls("data-critical-corporation", status="acquired", rng="below_1b", stage="undetermined", country="US",
             city="Bothell", focus="Healthcare & Bio",
             note="Wireless telemedicine software maker (Nasdaq DCCA) acquired by GE Medical Systems in 2001; the firm's archived "
                  "card gives no investment year or round."))

# data-domain
_DD = POST("vcs-and-angels-take-aim")
L.append(cls("data-domain", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=_DD,
             stage_conf="high", entry_date="2001", city="Santa Clara", focus="Data Infrastructure",
             note=f"The firm's 2013 post names Data Domain among NEA's seed investments and its card reads Seed in 2001; IPO in 2007, "
                  f"acquired by EMC in 2009. {LEFT}"))

# databento
_DB = NEWS("databento", "Databento Raises $97 Million Series B Led by NEA")
L.append(cls("databento", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=_DB,
             stage_conf="high", entry_date="2026-07", city="Salt Lake City", city_src="web_verified",
             focus="Fintech & Payments",
             rounds=[rnd("2026-07-09", "Series B", 97_000_000, "New Enterprise Associates", True, _DB, "company")],
             extra={**WV, "valuation_asof": "2026-09-30", "valuation_citation": _DB},
             note="Market data platform in Salt Lake City; NEA led the $97M Series B of 2026-07-09, its first round, as the Redpoint "
                  "book also cites. Momentum check 2026-09-30 (Google News): no valuation disclosed, no priced mark at or above $1B."))

# databricks
L.append(cls("databricks", city="San Francisco", focus="Data Infrastructure",
             note="Headquartered in San Francisco, as in the eleven sibling books."))

# datafold
_DFS = POST("our-investment-in-datafold")
_DFA = NEWS("datafold", "Datafold Raises $20M Series A")
L.append(cls("datafold", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=_DFS,
             stage_conf="high", entry_date="2020-11", grad="graduated", grad_src="web_verified", grad_cite=_DFA,
             grad_conf="high", city="New York", city_src="formd_address", focus="Data Infrastructure",
             flags=["stage_disputes_band"],
             rounds=[rnd("2020-11-19", "Seed", None, "New Enterprise Associates", True, _DFS, "firm"),
                     rnd("2021-11-09", "Series A", 20_000_000, "New Enterprise Associates", True, _DFA, "company")],
             note="The firm's post of 2020-11-19 says NEA led the seed, so the entry is the seed, not the 2021 filing the band "
                  "read; graduated with the $20M Series A of 2021-11-09 (Business Wire)."))

# datalogix
L.append(cls("datalogix", rng="below_1b", stage="undetermined", entry_date="1992", city="Valhalla", focus="SaaS",
             note="Datalogix International, process manufacturing software in Valhalla, New York, acquired by Oracle in the 1990s; "
                  "the General Catalyst and IVP Datalogix is the later Colorado marketing data company, a name collision."))

# datarobot
L.append(cls("datarobot", city="Boston", focus="AI & Applied AI",
             note="Headquartered in Boston, as in the Sutter Hill and Tiger Global books."))

# datavisor
L.append(cls("datavisor", status="private", rng="below_1b", city="Mountain View", city_src="formd_address",
             focus="Security",
             note="Fraud detection company in Mountain View (Form D address), still private; no priced mark near $1B."))

# datrium
L.append(cls("datrium", status="acquired", rng="below_1b", stage="undetermined", entry_date="2012", country="US",
             city="Sunnyvale", focus="Data Infrastructure",
             note="Converged storage company acquired by VMware in 2020 (the firm's exit line; the Lightspeed book agrees); "
                  "NEA's 2012 round is not named."))

# davita-nephrolife
L.append(cls("davita-nephrolife", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011",
             country="IN", country_src="web_verified", country_cite=SITE("davita-nephrolife"), focus="Healthcare & Bio",
             flags=["city_unknown"],
             note="Indian renal care chain (NephroLife) the firm lists as acquired by DaVita; no record found gives its city or "
                  "NEA's round."))

# decru
L.append(cls("decru", status="acquired", rng="below_1b", stage="undetermined", entry_date="2002", country="US",
             city="Redwood City", focus="Security",
             note="Storage security appliance maker acquired by Network Appliance in 2005, as in the Benchmark and Greylock books; "
                  "the 2002 round is not named."))

# deeya-energy-inc
L.append(cls("deeya-energy-inc", status="defunct", rng="below_1b", country="US", city="Fremont", focus="Climate & Energy",
             note="Flow battery maker in Fremont, renamed Imergy Power Systems in 2014 (base row imergy-power-systems), which "
                  "ceased operations in 2016."))

# deltastream
L.append(cls("deltastream", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("deltastream"), stage_conf="medium", entry_date="2020", country="US", city="Menlo Park",
             focus="Data Infrastructure",
             note=f"Serverless stream processing company; the firm's card reads Seed in 2020 and Aaron Jacobson sits on its board. {LEFT}"))

# denali-medical-ii
L.append(cls("denali-medical-ii", status="unknown", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=ARCH("denali-medical-ii"), stage_conf="medium", grad="graduated", grad_src="formd",
             city="Plymouth", city_src="formd_address", focus="Healthcare & Bio",
             note="Medical device incubator in Plymouth, Minnesota; the firm's archived card reads seed, and its Form D sequence "
                  "shows the $2M 2009 round followed by $15M in 2011, a graduation. It left the firm's list after 2016."))

# dermira
_DERM = FTSU("Dermira", "a2221236zs-1.htm")
L.append(cls("dermira", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=_DERM, stage_conf="high",
             entry_date="2011-08", city="Menlo Park", focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2011-08", "Series A", 34_000_000, None, True, _DERM, "filing")],
             note="The S-1 shows NEA 13 buying $12.2M of the Series A that closed in August 2011 and August 2012, so the entry is "
                  "the A, not a Growth round; acquired by Lilly in 2020."))

# desire2learn
_D2L = W("D2L")
L.append(cls("desire2learn", status="public", rng="below_1b", usd=370_220_239, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/tsx/DTOL/market-cap/", asof="2026-09-30",
             stage="Series A", stage_src="web_verified", stage_cite=_D2L, stage_conf="medium", entry_date="2012-09",
             country="CA", country_src="web_verified", country_cite=_D2L, city="Kitchener", focus="SaaS",
             flags=["stage_disputes_band"], extra=WV,
             rounds=[rnd("2012-09-04", "Series A", 80_000_000, None, True, _D2L, "press")],
             note="D2L's first financing, the $80M of September 2012 that NEA announced, is named a Series A (Wikipedia), over the "
                  "firm's Growth label. Listed on the TSX since 2021: CAD 525.1M @ ECB 2026-09-30 (CAD/EUR 1.6105, EUR/USD 1.1355) = $370.2M."))

# desktop-metal
L.append(cls("desktop-metal", rng="below_1b", city="Burlington", focus="Industrial & Robotics",
             note="Metal 3D printing company in Burlington, Massachusetts, acquired by Nano Dimension in 2025."))

# devices-for-vascular-intervention
L.append(cls("devices-for-vascular-intervention", status="acquired", rng="below_1b", stage="undetermined", entry_date="1986",
             country="US", city="Redwood City", focus="Healthcare & Bio",
             note="Atherectomy catheter maker acquired by Eli Lilly (the firm's exit line); the 1986 round is not named."))

# diatide
L.append(cls("diatide", status="acquired", rng="below_1b", stage="undetermined", entry_date="1993", country="US",
             city="Londonderry", focus="Healthcare & Bio",
             note="Peptide imaging agent developer in Londonderry, New Hampshire, acquired by Schering AG (the firm's exit line); "
                  "the 1993 round is not named."))

# didi-chuxing
_DIDI = W("DiDi")
L.append(cls("didi-chuxing", status="public", rng="10b_plus", usd=16.14e9, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/otc/DIDIY/market-cap/", asof="2026-09-30",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2016",
             country="CN", country_src="web_verified", country_cite=_DIDI, city="Beijing", focus="Consumer & Marketplaces",
             extra=WV,
             note="Beijing ride-hailing company; every Didi financing in 2016 was a late-stage round at a valuation above $20B, so "
                  "NEA's 2016 entry is Growth though its round is not named. Delisted from the NYSE in 2022, its ADSs trade OTC at "
                  "a $16.14B market cap on 2026-09-30 (stockanalysis)."))

# divvy (stage filled below)

# djust (filled below)

# divvy
_DV = NEWS("divvy", "Divvy Raises $200M After Finding")
L.append(cls("divvy", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=_DV,
             stage_conf="high", entry_date="2019-04", country="US", city="Lehi", focus="Fintech & Payments",
             rounds=[rnd("2019-04-30", "Series C", 200_000_000, "New Enterprise Associates", True, _DV, "press")],
             note="NEA led the $200M Series C of April 2019 (Crunchbase News), its first round in the Utah spend management "
                  "company; acquired by Bill.com in 2021, as in the Insight book."))

# djust
_DJ = NEWS("djust", "B2B commerce platform DJUST secures")
L.append(cls("djust", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=_DJ,
             stage_conf="high", entry_date="2023-06", country="FR", country_src="web_verified", country_cite=_DJ,
             city="Paris", focus="SaaS",
             rounds=[rnd("2020", "Seed", 4_310_000, "Elaia", False, _DJ, "press"),
                     rnd("2023-06-12", "Series A", 12_940_000, "New Enterprise Associates; Elaia", True, _DJ, "press")],
             note="France-based B2B commerce software; NEA co-led the EUR 12M Series A of June 2023 with Elaia, after Elaia's 2020 "
                  "seed (Retail Insight Network), as the firm's post of 2023-06-12 describes."))

# docent-health
L.append(cls("docent-health", status="acquired", rng="below_1b", city="Cambridge", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Patient experience platform in Cambridge, Massachusetts (Form D address), acquired by GetWellNetwork (the "
                  "firm's exit line)."))

# dots-technology-corp
L.append(cls("dots-technology-corp", status="private", rng="below_1b", stage="undetermined", entry_date="2015",
             city="Natick", city_src="formd_address", focus="Healthcare & Bio",
             note="Point-of-care allergen and diagnostics detection company in Natick, Massachusetts (Form D), still listed private; "
                  "the firm's 2015 round is not named. The Felicis, Northzone and YC Dots rows are other companies."))

# dreamfactory-software-inc
_DF = W("DreamFactory")
L.append(cls("dreamfactory-software-inc", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=_DF, stage_conf="high", entry_date="2006", city="Campbell", city_src="formd_address",
             focus="DevTools & APIs",
             rounds=[rnd("2006", "Series A", 5_600_000, "New Enterprise Associates", True, _DF, "press")],
             note="API platform company in Campbell, California; Wikipedia records its $5.6M Series A from NEA in 2006, the firm's "
                  "first-investment year, earlier than the 2010 Form D."))

# drobo
L.append(cls("drobo", status="defunct", rng="below_1b", stage="undetermined", entry_date="2008", city="San Jose",
             focus="Data Infrastructure",
             note="Storage device maker (Data Robotics until 2011, base row data-robotics-inc): merged into Connected Data in 2013, "
                  "spun out in 2015, bought by StorCentric in 2018 and shut in 2023 in StorCentric's Chapter 7 (Wikipedia); "
                  "defunct as in the Greylock and Sutter Hill books."))

# drop
_DROP = W("Drop (loyalty program)")
L.append(cls("drop", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=_DROP,
             stage_conf="high", entry_date="2018-02", city="Toronto", focus="Consumer & Marketplaces",
             rounds=[rnd("2018-02", "Series A", 21_000_000, "New Enterprise Associates", True, _DROP, "press")],
             note="Card-linked rewards app based in Toronto (its Form D address); NEA led the $21M Series A announced in February "
                  "2018 (Wikipedia), earlier than the 2021 date on file. The First Round book's country FR looks like a data error."))

jl.write("c3b", L)
