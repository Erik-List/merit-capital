#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 3, chunk c (CarTrade to Classplus, 14 rows).
Evidence: show.py --batch 3, SEC filings in the evidence pack (read), press pages in the caches (read),
Bing/Google News under NQ_TAG=b3, sibling marks read from siblings.json, stockanalysis.com (WebSearch).
Run: NQ_TAG=b3 python3 judgments-3c.py"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PK = json.loads((HERE / "evidence-pack.json").read_text())
SIBS = json.loads((HERE / "siblings.json").read_text())
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


def SIB(slug, investor):
    """A sibling book's valuation citation for the same company, read from siblings.json."""
    for x in SIBS.get(slug, []):
        if x["investor"] == investor and (x.get("val_cite") or "").startswith("http"):
            return x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {investor!r}): no citation")


L = []

# ---------------------------------------------------------------- CarTrade (listed 2021)
CT_14 = URLOF("cartrade", "CarTrade.com raises $30M from Warburg Pincus, Canaan & Tiger Global", "vccircle.com")
CT_CAP = "https://stockanalysis.com/quote/nse/CARTRADE/market-cap/"   # printed by WebSearch, read 2026-09-29
L.append(cls("cartrade", status="public", rng="1b_plus", usd=1_469_500_005, val_src="web_verified", val_cite=CT_CAP,
    asof="2026-09-29", stage="undetermined", country="IN", country_src="web_verified", country_cite=CT_14,
    city="Mumbai", focus="Consumer & Marketplaces",
    note="Mumbai online auto marketplace (CarTrade Tech), listed on the NSE and BSE since August 2021. Tiger Global was "
         "already an existing investor when Warburg Pincus led the Rs 185 crore ($30M) round of October 2014 "
         "(VCCircle; Financial Express); the round in which Tiger first invested could not be found (Bing, Google "
         "News, Wikipedia), so the stage is undetermined. Market cap INR 141.05B on 2026-09-29 (stockanalysis.com): "
         "INR 141.05B @ ECB 2026-09-29 (INR/EUR 108.991, EUR/USD 1.1355) = $1.47B.",
    rounds=[rnd("2014-10", "Unnamed", 30_200_000, "Warburg Pincus", True, CT_14, "press")], extra=WV))

# ---------------------------------------------------------------- CashU (a unit of the Souq Group)
L.append(verdict("cashu", "not_member",
    "The Wikipedia sentence says Naspers took a stake 'alongside Jabbar Internet Group and Tiger Global in CashU and "
    "Souq.com', which sat together in the Souq Group from 2012 to 2015: Tiger's money went into the group (the "
    "souq-com row), and no record names a CashU financing with a Tiger vehicle. A unit of a portfolio company's group "
    "is not its own entry (T5)",
    ec="web", conf="medium", cite=W("CashU")))

# ---------------------------------------------------------------- CertiK
CK_B = NEWS("certik", "Blockchain Security Firm CertiK Announces $24M Series B+")
CK_V = SIB("certik", "coatue")
L.append(cls("certik", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=CK_V,
    asof="2022-04-07", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CK_B,
    entry_date="2021-08", country="US", city="New York", focus="Security", flags=("stale",),
    note="New York blockchain security auditor. Tiger Global led the $24M Series B+ of August 2021 (Business Wire) and "
         "co-led the $88M Series B3 of April 2022 with Insight Partners and Advent at a $2B valuation (Business Wire), "
         "the mark the Coatue, Insight and Lightspeed books carry. Mark $2B as of 2022-04, stale; no later priced "
         "round or documented collapse found.",
    rounds=[rnd("2021-08-17", "Series B+", 24_000_000, "Tiger Global", True, CK_B, "company"),
            rnd("2022-04-07", "Series B3", 88_000_000, "Insight Partners; Tiger Global; Advent International", True,
                CK_V, "company")], extra=WV))

# ---------------------------------------------------------------- Chaayos
CH_A = URLOF("chaayos", "Tea chain Chaayos raises $5M from Tiger Global, Ola founders", "vccircle.com")
CH_C = URLOF("chaayos", "Tiger Global-backed Chaayos secures $45 mn in Series C", "vccircle.com")
L.append(cls("chaayos", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=CH_A, entry_date="2015-05", country="IN", country_src="web_verified",
    country_cite=CH_A, city="Gurugram", focus="Consumer & Marketplaces",
    note="Tea cafe chain (Sunshine Tea House Pvt Ltd), Gurgaon-based (Mint, 2015). Tiger Global led the $5M (Rs 32 "
         "crore) Series A of May 2015 with the Ola founders, after an angel seed from Zishaan Hayath, and its managing "
         "director joined the board (VCCircle); Tiger put in $2M more in 2017 and backed the $45M Series C of 2022. "
         "The Wikidata IN claim is confirmed.",
    rounds=[rnd("2015-05-18", "Series A", 5_000_000, "Tiger Global", True, CH_A, "press"),
            rnd("2022-06", "Series C", 45_000_000, None, True, CH_C, "press")]))

# ---------------------------------------------------------------- Chainalysis (Lee Fixel = Addition)
L.append(verdict("chainalysis-inc", "not_member",
    "Lee Fixel is director on Chainalysis's 2021 Form D as Addition's partner: he left Tiger in early 2019 and D7 "
    "names Chainalysis among Addition's seats; no Chainalysis round names Tiger Global (the Accel, Benchmark, Coatue, "
    "Point Nine and Ribbit books hold the company)",
    ec="formd_adjudicated", conf="high", cite=SEC("chainalysis-inc")))

# ---------------------------------------------------------------- Chargebee
CB_B = NEWS("chargebee", "ChargeBee Raises $5M Series B Led By Tiger Global")
CB_V = SIB("chargebee", "accel")
L.append(cls("chargebee", status="private", rng="1b_plus", usd=3_500_000_000, val_src="web_verified", val_cite=CB_V,
    asof="2022-02", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CB_B, entry_date="2015-03",
    country="US", city="San Francisco", focus="SaaS", flags=("stale",), clear=("needs_web_value",),
    note="Subscription billing software, founded in Chennai; the Accel and Insight books place its headquarters in San "
         "Francisco. Tiger Global led the $5M Series B of March 2015 (TechCrunch), after Accel's Series A, and led "
         "again in 2021 (unicorn round) and in February 2022 with Sequoia ($250M at $3.5B, Business Today). Mark "
         "$3.5B as of 2022-02, stale; no later priced round or documented collapse found.",
    rounds=[rnd("2015-03-10", "Series B", 5_000_000, "Tiger Global", True, CB_B, "press"),
            rnd("2022-02", "Unnamed", 250_000_000, "Tiger Global; Sequoia Capital India", True, CB_V, "press")],
    extra=WV))

# ---------------------------------------------------------------- Checkmate (ItsaCheckmate)
CM_B = NEWS("checkmate", "Checkmate Raises $10 Million in Series B Funding Led by Tiger Global to Scale")
L.append(cls("checkmate", status="private", rng="below_1b", stage="undetermined", country="US", city="New York",
    city_src="web_verified", focus="SaaS",
    note="Checkmate (ItsaCheckmate), New York restaurant ordering and voice-AI software founded by Vishal Agarwal "
         "(RestaurantNews release, New York dateline). Tiger Global's first money was $3M in November 2018 (YourStory), "
         "a round the record does not label, so the stage is undetermined; Inspire Brands invested in 2020 (Restaurant "
         "Business) and Tiger led the $10M Series B of October 2024. The a16z row 'checkmate' (a programme company) is "
         "another company: a name collision, not aligned.",
    rounds=[rnd("2018-11", "Unnamed", 3_000_000, "Tiger Global", True,
                NEWS("checkmate", "CheckMate gets $3 million funding from Tiger Global"), "press"),
            rnd("2024-10-23", "Series B", 10_000_000, "Tiger Global", True, CM_B, "company")]))

# ---------------------------------------------------------------- Checkout.com
CO_T = NEWS("checkout-com", "crowned Europe")
CO_V = SIB("checkout-com", "ribbit-capital")
L.append(cls("checkout-com", status="private", rng="10b_plus", usd=12_000_000_000, val_src="web_verified",
    val_cite=CO_V, asof="2025-09-26", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CO_T,
    entry_date="2021-01", country="GB", country_src="web_verified", country_cite=W("Checkout.com"), city="London",
    focus="Fintech & Payments", clear=("needs_web_value",),
    note="London online payments company. Tiger Global led the $450M round of January 2021 at $15B (CNBC), after the "
         "$150M round of 2020 at $5.5B that did not name it, and joined the $1B Series D of January 2022 (Wikipedia). "
         "Mark: the $12B valuation of September 2025 (TechCrunch), the one the Coatue, Insight and Ribbit books carry.",
    rounds=[rnd("2021-01-12", "Unnamed", 450_000_000, "Tiger Global", True, CO_T, "press"),
            rnd("2025-09-26", "Valuation update", None, None, None, CO_V, "press")], extra=WV))

# ---------------------------------------------------------------- CHEQ
CQ_C = NEWS("cheq", "Tiger Global Backs Go-to-Market Security Leader CHEQ")
CQ_V = NEWS("cheq", "CHEQ enters Unicorn club")
L.append(cls("cheq", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=CQ_V,
    asof="2022-02-22", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CQ_C,
    entry_date="2022-02", country="IL", country_src="web_verified", country_cite=CQ_V, city="Tel Aviv",
    focus="Security", flags=("stale",),
    note="Israeli go-to-market security company (Calcalist), Tel Aviv. Tiger Global led the $150M Series C of February "
         "2022, joined by existing investors Battery, Hanaco and Phoenix (PR Newswire; Calcalist). The company did not "
         "disclose the valuation; Calcalist reported it at $1B, exactly at the band edge. Mark $1B as of 2022-02, "
         "stale. The Battery book reads below $1B with no figure: this row holds a cited mark.",
    rounds=[rnd("2022-02-22", "Series C", 150_000_000, "Tiger Global", True, CQ_C, "company")], extra=WV))

# ---------------------------------------------------------------- Chili Piper
CP_B = NEWS("chili-piper", "pitch deck startup Chili Piper used to land")
L.append(cls("chili-piper", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CP_B, entry_date="2021-04", country="US", city="New York", focus="SaaS",
    note="Scheduling and lead-routing software company. After an $18M Series A in April 2020, Tiger Global led the $33M "
         "Series B announced in April 2021, with Base10 and Gradient (Business Insider).",
    rounds=[rnd("2020-04", "Series A", 18_000_000, None, False, CP_B, "press"),
            rnd("2021-04", "Series B", 33_000_000, "Tiger Global", True, CP_B, "press")]))

# ---------------------------------------------------------------- Chime (X1: public-desk vehicles only)
CHM_IRA = PACK("chime")
CHM_V = SIB("chime", "coatue")
L.append(verdict("chime", "member",
    "Chime's IPO registration files its amended investors' rights agreement, dated at the Series G of 2021-08-06, "
    "signed by Tiger Global Investments, L.P. and Tiger Global Long Opportunities Master Fund, L.P. as investors "
    "while Chime was private. Both named vehicles are public-desk funds and no PIP vehicle is named: delta X1 would "
    "move the row to the other desk (flag boundary)",
    ec="fund_filing", conf="high", cite=CHM_IRA))
L.append(cls("chime", status="public", rng="10b_plus", usd=10_140_000_000, val_src="web_verified", val_cite=CHM_V,
    asof="2026-09-25", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=CHM_IRA,
    entry_date="2021-08", city="San Francisco", focus="Fintech & Payments", flags=("boundary",),
    note="San Francisco consumer fintech, listed on Nasdaq (CHYM) since June 2025. Tiger's two public-desk funds signed "
         "the rights agreement of the $750M Series G (2021-08-06) as investors; the filing does not say whether they "
         "bought in the G or held from the Series F of September 2020, both late-stage rounds, so Growth with the entry "
         "dated no later than 2021-08 (model, medium). X1 row. Market cap $10.14B on 2026-09-25 (stockanalysis.com), "
         "the figure the Coatue and ICONIQ books carry.",
    rounds=[rnd("2021-08-06", "Series G", 750_000_000, None, True, CHM_IRA, "filing")], extra=WV))

# ---------------------------------------------------------------- ChinaEdu (F-1 names PIP II)
CE_F1 = PACK("chinaedu-corp")
L.append(verdict("chinaedu-corp", "member",
    "ChinaEdu's 2007 F-1 records that Tiger Global Private Investment Partners II, L.P. (a PIP vehicle) and Tiger Global "
    "II, L.P. bought its Series B preferred shares in a private placement on 2004-12-13 (PIP II paid $10.99M), with a "
    "Tiger Global Investment Consulting managing director on the board since December 2004",
    ec="fund_filing", conf="high", cite=CE_F1))
L.append(cls("chinaedu-corp", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CE_F1, entry_date="2004-12-13", country="CN", country_src="web_verified",
    country_cite=CE_F1, city="Beijing", focus="SaaS",
    note="Beijing provider of online degree programmes and education services to Chinese universities, listed on "
         "Nasdaq in December 2007. Tiger's PIP II entered in the Series B of December 2004 (F-1). Shareholders "
         "approved the going-private merger on 2014-04-18 (PR Newswire), after which the company was held privately: "
         "acquired. Focus SaaS under the edtech rule (it sells its platform and services to universities).",
    rounds=[rnd("2004-12-13", "Series B", None, None, True, CE_F1, "filing")]))

# ---------------------------------------------------------------- Chiper
CI_B = NEWS("chiper", "14-slide pitch deck Chiper")
L.append(cls("chiper", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=CI_B, entry_date="2021-11", country="CO", country_src="web_verified", country_cite=CI_B, city="Bogotá",
    focus="Consumer & Marketplaces",
    note="Colombian B2B e-commerce platform supplying neighbourhood stores, Bogotá. Tiger Global led the $53M Series B "
         "of November 2021 (Business Insider; Bloomberg Linea names the Series B); no earlier round in the evidence view "
         "names the firm. Last known private; no later round or shutdown found.",
    rounds=[rnd("2021-11-18", "Series B", 53_000_000, "Tiger Global", True, CI_B, "press")]))

# ---------------------------------------------------------------- Classplus
CP_C = NEWS("classplus", "Classplus raises $65 million in a Series C round led by Tiger Global")
L.append(cls("classplus", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CP_C, entry_date="2021-06", country="IN", country_src="web_verified",
    country_cite=CP_C, city="Noida", focus="SaaS",
    note="Noida software platform for tutors and coaching businesses (SaaS under the edtech rule). Tiger Global led the "
         "$65M Series C of June 2021 (Business Line); earlier rounds do not name it. No priced round at $1B or more "
         "found.",
    rounds=[rnd("2021-06-23", "Series C", 65_000_000, "Tiger Global", True, CP_C, "press")]))

if __name__ == "__main__":
    jl.write("batch-003c", L)
