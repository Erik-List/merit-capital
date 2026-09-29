#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 3, chunk b (BlackBuck to Carrot, 14 rows).
Evidence: show.py --batch 3, SEC filings in the evidence pack (read), press pages in the caches (read),
Bing (bq.py) and Google News (nq.py) under NQ_TAG=b3, stockanalysis.com for the listed cap (WebSearch).
Run: NQ_TAG=b3 python3 judgments-3b.py"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PK = json.loads((HERE / "evidence-pack.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def PACK(slug, kind="sec", i=0):
    line = (PK.get(slug) or {}).get(kind, [])[i]
    u = line.rsplit("| ", 1)[-1].strip()
    if not u.startswith("https://"):
        raise SystemExit(f"PACK({slug!r}, {kind!r}, {i}): no URL on the line")
    return u


def URLOF(slug, title_sub, url_sub):
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    us = list(dict.fromkeys(i["url"] for i in items if i.get("url") and title_sub.lower() in i["title"].lower()
                            and url_sub in i["url"]))
    if len(us) != 1:
        raise SystemExit(f"URLOF({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(us)}")
    return us[0]


L = []

# ---------------------------------------------------------------- BlackBuck (listed 2024)
BB_B = URLOF("blackbuck", "Logistics startup BlackBuck raises $25M from Tiger Global", "vccircle.com")
BB_C = URLOF("blackbuck", "gets $70 mn from Sands Capital", "vccircle.com")
BB_CAP = "https://stockanalysis.com/quote/nse/BLACKBUCK/market-cap/"   # printed by WebSearch, read 2026-09-29
L.append(cls("blackbuck", status="public", rng="1b_plus", usd=1_181_017_515, val_src="web_verified",
    val_cite=BB_CAP, asof="2026-09-29", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BB_B, entry_date="2015-12", country="IN", country_src="web_verified", country_cite=BB_B,
    city="Bangalore", focus="SaaS",
    note="Bangalore trucking platform (Zinka Logistics Solutions, renamed BlackBuck Limited in August 2025), listed "
         "on the NSE since November 2024. Tiger Global entered in the $25M Series B of December 2015, with Apoletto "
         "and the existing investors Accel and Flipkart (VCCircle); the Series C of 2017 was led by Sands Capital. "
         "Market cap INR 113.36B on 2026-09-29 (stockanalysis.com): INR 113.36B @ ECB 2026-09-29 (INR/EUR 108.991, "
         "EUR/USD 1.1355) = $1.18B. The Accel book still reads private and below $1B, which predates the listing: "
         "this row holds the fresher cited evidence.",
    rounds=[rnd("2015-12-09", "Series B", 25_000_000, "Tiger Global", True, BB_B, "press"),
            rnd("2017-03", "Series C", 70_000_000, "Sands Capital", None, BB_C, "press")], extra=WV))

# ---------------------------------------------------------------- Blank Street Coffee
BS_A = NEWS("blank-street-coffee", "General Catalyst, Tiger Global lead $25M")
BS_B = NEWS("blank-street-coffee", "Primary Funding Led By General Atlantic At $650 Million Valuation")
L.append(cls("blank-street-coffee", status="private", rng="below_1b", usd=650_000_000, val_src="web_verified",
    val_cite=BS_B, asof="2026-08", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=BS_A,
    entry_date="2021-10", city="New York", city_src="web_verified", focus="Consumer & Marketplaces",
    note="New York coffee chain founded May 2020 (TechCrunch). General Catalyst and Tiger Global led the $25M Series "
         "A of October 2021; the $7M seed earlier that year does not name the firm (TechCrunch). Latest mark: the $75M "
         "Series B led by General Atlantic in August 2026 at about $650M (Pulse 2.0), below $1B.",
    rounds=[rnd("2021", "Seed", 7_000_000, None, False, BS_A, "press"),
            rnd("2021-10-13", "Series A", 25_000_000, "General Catalyst; Tiger Global", True, BS_A, "press"),
            rnd("2026-08", "Series B", 75_000_000, "General Atlantic", None, BS_B, "press")], extra=WV))

# ---------------------------------------------------------------- Blockdaemon
BD_C = NEWS("blockdaemon", "Blockdaemon Nets $207M")
L.append(cls("blockdaemon", status="private", rng="1b_plus", usd=3_250_000_000, val_src="web_verified",
    val_cite=BD_C, asof="2022-01-26", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=BD_C,
    entry_date="2022-01", country="US", city="Los Angeles", focus="Crypto & Web3", flags=("stale",),
    note="Blockchain node and staking infrastructure company. Sapphire and Tiger Global led the $207M Series C of "
         "January 2022 at a $3.25B post-money valuation (pymnts; Reuters). The $155M Series B of September 2021 "
         "(SoftBank-valued at $1.2B per The Information) does not name Tiger in the evidence view, so the entry is "
         "read as the Series C. Mark $3.25B as of 2022-01, stale; no later priced round or documented collapse found. "
         "City from knowledge (Los Angeles datelines on its releases).",
    rounds=[rnd("2021-09-21", "Series B", 155_000_000, None, None, NEWS("blockdaemon", "Raises $155 Million In Series B"),
                "company"),
            rnd("2022-01-26", "Series C", 207_000_000, "Sapphire Ventures; Tiger Global", True, BD_C, "press")],
    extra=WV))

# ---------------------------------------------------------------- BOX8 / EatClub Brands
BX_T = NEWS("box8", "invests $40 million in BOX8")
BX_C = NEWS("box8", "Raises $15 Mn In Series C Round")
L.append(cls("box8", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BX_T, entry_date="2021-11", country="IN", country_src="web_verified", country_cite=BX_C,
    city="Mumbai", focus="Consumer & Marketplaces",
    note="Mumbai cloud-kitchen company (BOX8, MOJO Pizza), renamed EatClub Brands in November 2021. Tiger Global led "
         "its $40M round of November 2021 (Business Today), after the $15M Series C of March 2019 led by eWTP with "
         "Mayfield and IIFL (Inc42), so the entry is a later-stage round: Growth. Tiger added to its stake in a roughly "
         "$30M secondary in March 2022 (SiliconIndia).",
    rounds=[rnd("2019-03", "Series C", 15_000_000, "eWTP Ecosystem Fund", False, BX_C, "press"),
            rnd("2021-11", "Unnamed", 40_000_000, "Tiger Global", True, BX_T, "press"),
            rnd("2022-03", "Secondary", 30_000_000, None, True, URLOF("box8", "A91 Partners enter into Box8", "siliconindia"), "press")]))

# ---------------------------------------------------------------- Bright Health / NeueHealth
BH_E = PACK("bright-health")
BH_X = NEWS("bright-health", "Announces Closing of Take-Private Transaction")
L.append(cls("bright-health", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BH_E, entry_date="2020-10", country="US", city="Doral", city_src="web_verified",
    focus="Healthcare & Bio",
    note="Bright Health Group, renamed NeueHealth in 2024. The company's SEC correspondence before its 2021 IPO says "
         "Tiger Global Management was a new investor that led the pricing of the Series E preferred issued in October "
         "2020; no earlier round names the firm. NEA's take-private closed on 2025-10-02 (NeueHealth's release, "
         "datelined Doral, Florida, where the company is now based): acquired. The Headline book's Minneapolis is the "
         "pre-2024 headquarters.",
    rounds=[rnd("2020-10", "Series E", None, "Tiger Global", True, BH_E, "filing"),
            rnd("2025-10-02", "Take-private (NEA)", None, "New Enterprise Associates", False, BH_X, "company")]))

# ---------------------------------------------------------------- Built Robotics
BR_C = NEWS("built-robotics", "Built Robotics Raises $64M to Transform")
L.append(cls("built-robotics", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=BR_C, entry_date="2022-04", country="US", city="San Francisco",
    city_src="web_verified", focus="Industrial & Robotics",
    note="San Francisco maker of autonomy kits for construction equipment (release dateline). Tiger Global led the $64M "
         "Series C of 2022-04-07, joined by existing investors NEA, Founders Fund, Fifth Wall and Building Ventures, "
         "bringing total funding to $112M (PR Newswire); no earlier round names Tiger.",
    rounds=[rnd("2022-04-07", "Series C", 64_000_000, "Tiger Global", True, BR_C, "company")]))

# ---------------------------------------------------------------- Built Technologies (Lee Fixel = Addition)
L.append(verdict("built-technologies-inc", "not_member",
    "Lee Fixel is director on Built Technologies' 2022 Form D, after he left Tiger in early 2019 to found Addition "
    "(D7 names Built among Addition's seats); Built's $88M Series C of February 2021 was led by 'VC Lee Fixel's new "
    "fund' (Business Insider), and no round names Tiger Global",
    ec="formd_adjudicated", conf="high", cite=SEC("built-technologies-inc")))

# ---------------------------------------------------------------- Butlr (article evidence)
BUT = URLOF("butlr", "Butlr Closes $20M Investment", "newswire.com/view")
L.append(verdict("butlr", "member",
    "Butlr's release of 2022-07-26 says its $20M Series A was 'led by investors Tiger Global, Ray Stata ... and "
    "Primetime Partners' (newswire); TechCrunch reports the same round",
    ec="web", conf="high", cite=BUT))
L.append(cls("butlr", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=BUT, entry_date="2022-07", country="US", city="Burlingame", city_src="web_verified",
    focus="Industrial & Robotics",
    note="Burlingame, California maker of body-heat occupancy sensors, an MIT Media Lab spinout (release dateline). "
         "Tiger Global, Primetime Partners and Ray Stata led the $20M Series A, which Carrier joined in July 2022.",
    rounds=[rnd("2022-07-26", "Series A", 20_000_000, "Tiger Global; Primetime Partners; Ray Stata", True, BUT,
                "company")]))

# ---------------------------------------------------------------- BVNK
BV_A = NEWS("bvnk", "BVNK Generates $40M in Series A Funding Led by Tiger Global")
BV_M = NEWS("bvnk", "Mastercard to acquire BVNK for up to $1.8 billion")
BV_X = NEWS("bvnk", "after losing BVNK to Mastercard")
L.append(cls("bvnk", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=BV_A, entry_date="2022-05", country="GB", country_src="web_verified",
    country_cite=NEWS("bvnk", "London’s BVNK Enhances Stablecoin Liquidity"), city="London", focus="Crypto & Web3",
    note="London stablecoin payments infrastructure company. Tiger Global led the $40M Series A of May 2022 "
         "(Coinspeaker); a $50M round at about $750M followed in December 2024 (Fortune). Mastercard agreed on "
         "2026-03-17 to buy BVNK for up to $1.8B (Mint) and completed the purchase in August 2026 (Tech Times, "
         "2026-09-15): acquired.",
    rounds=[rnd("2022-05-12", "Series A", 40_000_000, "Tiger Global", True, BV_A, "press"),
            rnd("2024-12-17", "Series B", 50_000_000, None, None, NEWS("bvnk", "raises $50 million at around $750 million"),
                "press"),
            rnd("2026-03-17", "Acquisition (Mastercard)", 1_800_000_000, "Mastercard", False, BV_M, "press")]))

# ---------------------------------------------------------------- Byju's (insolvency)
BY_T = NEWS("byju-s", "Raises US$200M From Tiger Global")
BY_N = NEWS("byju-s", "NCLT orders status quo on Byju’s K3")
L.append(cls("byju-s", status="defunct", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BY_T, entry_date="2020-01", country="IN", country_src="web_verified", country_cite=BY_T,
    city="Bangalore", focus="Consumer & Marketplaces",
    note="Bangalore edtech company (Think & Learn Pvt Ltd). Tiger Global invested about $200M in January 2020 "
         "(AsiaTechDaily), its first position; Byju's had raised many rounds before. Think & Learn was admitted into "
         "corporate insolvency by the NCLT Bengaluru in July 2024 and remains under the tribunal, which in September "
         "2026 was still ruling on the disposal of group assets (Business Line, 2026-09-05): an insolvency with no "
         "sale of the business reads defunct. The Lightspeed book still reads private: this row holds the fresher "
         "cited evidence.",
    rounds=[rnd("2020-01", "Unnamed (primary and secondary)", 200_000_000, "Tiger Global", True, BY_T, "press")]))

# ---------------------------------------------------------------- Captain Fresh
CF_B = NEWS("captain-fresh", "raises $40M Series B led by Tiger Global")
L.append(cls("captain-fresh", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CF_B, entry_date="2021-12", country="IN", country_src="web_verified",
    country_cite=CF_B, city="Bangalore", focus="Consumer & Marketplaces",
    note="Bangalore B2B seafood marketplace. Tiger Global and Prosus led the $40M Series B of December 2021 "
         "(YourStory); the Accel book holds the earlier Series A, which does not name Tiger. The company has been "
         "preparing an IPO (bankers picked October 2024, a pre-IPO round in January 2025, IPO expenses in FY26 per "
         "The Economic Times, 2026-09-22) but is not listed. No priced round at $1B or more found.",
    rounds=[rnd("2021-12-21", "Series B", 40_000_000, "Tiger Global; Prosus Ventures", True, CF_B, "press")]))

# ---------------------------------------------------------------- CaratLane
CL_11 = NEWS("caratlane", "Tiger Global Invests $6M In Diamond Jewellery Portal")
CL_13 = NEWS("caratlane", "CaratLane Raises $15M Series C Funding From Tiger Global: Sources")
CL_15 = NEWS("caratlane", "Caratlane raises $31M in Series D round from Tiger Global")
L.append(cls("caratlane", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
    stage_cite=CL_11, entry_date="2011-06", country="IN", country_src="web_verified", country_cite=CL_11,
    city="Chennai", focus="Consumer & Marketplaces",
    note="Chennai online jewellery retailer founded 2008. Tiger Global invested $6M in June 2011 (VCCircle), the "
         "company's first institutional round, and was its institutional backer through the Series C of 2013 and the "
         "Series D of 2015 (MediaNama; VCCircle; Mint 2016: more than $50M from Tiger since the start). The 2011 round "
         "carries no series label in the press, so Series A is inferred from its place before the named C and D "
         "(model, medium). Titan bought a majority stake in 2016 and the remainder later: acquired.",
    rounds=[rnd("2011-06-22", "Unnamed (first institutional)", 6_000_000, "Tiger Global", True, CL_11, "press"),
            rnd("2013-05", "Series C", 15_000_000, "Tiger Global", True, CL_13, "press"),
            rnd("2015-01", "Series D", 31_000_000, "Tiger Global", True, CL_15, "press")]))

# ---------------------------------------------------------------- Carma (seed entry, listed 2025)
CM_S = URLOF("carma", "comes out of stealth with $20M seed round", "finance.yahoo.com")
CM_A = URLOF("carma", "Carma completes $75m series A raise", "itnews.com.au")
L.append(cls("carma", status="public", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=CM_S, entry_date="2021-12", grad="graduated", grad_src="web_verified", grad_cite=CM_A,
    grad_conf="high", country="AU", country_src="web_verified", country_cite=CM_S, city="Sydney",
    focus="Consumer & Marketplaces", flags=("model_disputes_source",),
    note="Australian online used-car retailer, Sydney. Tiger Global provided the $20M (A$28M) seed with which Carma "
         "came out of stealth in December 2021 (Yahoo Finance) and co-led the $75M Series A of May 2022 with General "
         "Catalyst (iTnews): graduated. Listed on the ASX (CMA) on 2025-11-05 after raising A$100M, a lukewarm debut, "
         "and dropped from the S&P/ASX All Ordinaries in September 2026 (MarketScreener): below $1B. The Wikidata "
         "Ireland claim is a join on another company, disputed. The Y Combinator row 'carma' is another company: a "
         "name collision, not aligned.",
    rounds=[rnd("2021-12", "Seed", 20_000_000, "Tiger Global", True, CM_S, "press"),
            rnd("2022-05-12", "Series A", 75_000_000, "General Catalyst; Tiger Global", True, CM_A, "press")]))

# ---------------------------------------------------------------- Carrot Fertility
CR_C = NEWS("carrot", "Fertility Startup Carrot Raises")
L.append(cls("carrot", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=CR_C, entry_date="2021-08", country="US", city="San Francisco", focus="Healthcare & Bio",
    flags=("model_disputes_source",),
    note="Carrot Fertility, the San Francisco fertility-benefits company. Tiger Global led its $75M Series C of August "
         "2021 (Forbes); no earlier round in the evidence view names the firm. The Wikidata prefill (acquired, Japan) "
         "is a join on another company named Carrot, disputed: Carrot Fertility operates independently. The Khosla "
         "row 'carrot' (acquired) and the Y Combinator row 'carrot' (an AI startup) are other companies: name "
         "collisions, not aligned.",
    rounds=[rnd("2021-08-17", "Series C", 75_000_000, "Tiger Global", True, CR_C, "press")]))

if __name__ == "__main__":
    jl.write("batch-003b", L)
