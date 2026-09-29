#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 4, chunk c (Cube26 to Diligent Robotics, 15 rows).
Evidence: show.py --batch 4, SEC filings in the evidence pack (read), press pages in the caches (read), Bing/Google
News under NQ_TAG=b4, Wikipedia, sibling marks from siblings.json, stockanalysis.com (WebSearch).
Run: NQ_TAG=b4 python3 judgments-4c.py"""
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
    for x in SIBS.get(slug, []):
        if x["investor"] == investor and (x.get("val_cite") or "").startswith("http"):
            return x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {investor!r}): no citation")


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []

# ---------------------------------------------------------------- Cube26 (seed entry)
C26_V = URLOF("cube26", "Tiger Global-backed Cube26 shuts down IoT business", "vccircle.com")
C26_P = URLOF("cube26", "Paytm acquires Tiger Global-backed technology firm Cube26", "moneycontrol.com")
L.append(cls("cube26", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_conf="high", stage_cite=C26_V, entry_date="2015-10", country="IN", country_src="web_verified",
    country_cite=C26_V, city="New Delhi", focus="AI & Applied AI",
    note="New Delhi mobile software company known for gesture and camera controls for handset makers (VCCircle). It "
         "received $7.7M (Rs 50 crore) in seed funding from Tiger Global and Flipkart in October 2015 (VCCircle, 2017), "
         "shut its IoT business in 2017 and was bought by Paytm in June 2018, a fire sale (Moneycontrol; Entrackr): "
         "acquired. Graduation left for the graduation pass.",
    rounds=[rnd("2015-10", "Seed", 7_700_000, "Tiger Global; Flipkart", True, C26_V, "press"),
            rnd("2018-06-19", "Acquisition (Paytm)", None, "One97 Communications (Paytm)", False, C26_P, "press")]))

# ---------------------------------------------------------------- Culture Machine
CM_ET = NEWS("culture-machine", "Culture Machine raises $18 million from hedge fund")
CM_B = NEWS("culture-machine", "Culture Machine raises $18 mn in Series B")
L.append(cls("culture-machine", status="unknown", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CM_ET, entry_date="2015-02", country="IN", country_src="web_verified",
    country_cite=CM_ET, city="Mumbai", focus="Media, Gaming & Advertising",
    note="Mumbai multi-channel video network. It raised $18M (Rs 111 crore) in February 2015 from Tiger Global as a new "
         "investor, with existing investors Zodius Capital and Times Internet (The Economic Times, Mumbai dateline); "
         "the round was its Series B (bestmediainfo). No later funding, sale or shutdown was found, so the current "
         "state is unknown.",
    rounds=[rnd("2015-02-05", "Series B", 18_000_000, None, True, CM_B, "press")]))

# ---------------------------------------------------------------- Current
CU_W = NEWS("current", "Current Joins Mobile-Banking Boom With $131 Million Tiger Global-Led Round")
CU_V = SIB("current", "a16z")
L.append(cls("current", status="private", rng="1b_plus", usd=1_500_000_000, val_src="web_verified", val_cite=CU_V,
    asof="2026-06", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CU_W, entry_date="2020-11",
    country="US", city="New York", focus="Fintech & Payments", flags=("model_disputes_source",),
    note="Current, the New York consumer fintech. Tiger Global led the $131M Series C of November 2020 at $750M (WSJ; "
         "HousingWire), after the 2019 Series B that did not include it. Mark: the $80M Series E of June 2026 at $1.5B, "
         "down from the 2021 round at $2.2B (BankingWith; the Business Journals), the figure the a16z and General "
         "Catalyst books carry. The Wikidata JP claim is a join on another company, disputed.",
    rounds=[rnd("2020-11-24", "Series C", 131_000_000, "Tiger Global", True, CU_W, "press"),
            rnd("2026-06", "Series E", 80_000_000, None, None, CU_V, "press")], extra=WV))

# ---------------------------------------------------------------- Dangdang (F-1: all of Series B)
DD_F1 = PACK("dangdang")
L.append(cls("dangdang", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=DD_F1, entry_date="2004-02-25", country="CN", country_src="web_verified",
    country_cite=DD_F1, city="Beijing", focus="Consumer & Marketplaces",
    note="Beijing online retailer (E-Commerce China Dangdang). Its 2010 F-1 shows that the Series B convertible "
         "preferred shares, issued on 2004-02-25 for about $9.5M, are all held by Tiger Global Private Investment "
         "Partners, L.P. and Tiger Technology II, L.P., together 23.9% before the December 2010 NYSE IPO; the Series A "
         "of 2000 predates the firm. The founders took Dangdang private in 2016: acquired.",
    rounds=[rnd("2000-02-28", "Series A", 6_200_000, None, False, DD_F1, "filing"),
            rnd("2004-02-25", "Series B", 9_459_000, "Tiger Global Private Investment Partners", True, DD_F1, "filing"),
            rnd("2006-06-27", "Series C", 27_009_000, "DCM", None, DD_F1, "filing")]))

# ---------------------------------------------------------------- Danke (Phoenix Tree)
DK = PACK("danke-phoenix-tree")
DK_N = NEWS("danke-phoenix-tree", "How China apartment rental giant Danke saw its business crumble")
L.append(cls("danke-phoenix-tree", status="defunct", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=DK, entry_date="2018-05-25", country="CN", country_src="web_verified",
    country_cite=DK, city="Beijing", focus="Consumer & Marketplaces",
    note="Beijing long-term apartment rental platform (Danke Apartment, Phoenix Tree Holdings). Its 2019 DRS shows "
         "Tiger's Internet Fund IV buying $44M of Series B-2 preferred on 2018-05-25 and $250M of Series C on "
         "2018-09-30, with a Tiger Global Hong Kong director on the board. It listed on the NYSE in January 2020; the "
         "business collapsed in late 2020 amid tenant and landlord disputes (Nikkei Asia) and the NYSE delisted it in "
         "April 2021 (SCMP): defunct.",
    rounds=[rnd("2018-05-25", "Series B-2", 44_000_000, None, True, DK, "filing"),
            rnd("2018-09-30", "Series C", 250_000_000, "Internet Fund IV (Tiger Global)", True, DK, "filing")]))

# ---------------------------------------------------------------- Dataiku
DA_W = W("Dataiku")
DA_V = SIB("dataiku", "iconiq-growth")
L.append(cls("dataiku", status="private", rng="1b_plus", usd=3_700_000_000, val_src="web_verified", val_cite=DA_V,
    asof="2022-12", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=DA_W, entry_date="2020-08",
    country="US", city="New York", focus="Data Infrastructure", flags=("stale", "model_disputes_source"),
    clear=("needs_web_value",),
    note="Data science and AI platform, founded in Paris and headquartered in New York (the Battery, ICONIQ and "
         "Insight books). Stripes and Tiger Global co-led the $100M Series D of August 2020, and Tiger led the $400M "
         "Series E of August 2021 at $4.6B (Wikipedia). Mark: the $200M Series F of December 2022 at a reduced $3.7B "
         "(FinTech Futures), the figure the ICONIQ book carries; stale. Momentum check: no later priced round found "
         "(Bing, 2026-09-29). The Wikidata FR claim reflects the founding country, disputed for the current head office.",
    rounds=[rnd("2020-08", "Series D", 100_000_000, "Stripes; Tiger Global", True, DA_W, "press"),
            rnd("2021-08", "Series E", 400_000_000, "Tiger Global", True, DA_W, "press"),
            rnd("2022-12", "Series F", 200_000_000, None, None, DA_V, "press")], extra=WV))

# ---------------------------------------------------------------- DealShare (collapse)
DS_T = NEWS("dealshare", "Tiger Global leads $144 million funding round in DealShare")
DS_ET = NEWS("dealshare", "may sell to Truemeds")
L.append(cls("dealshare", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=DS_T, entry_date="2021-07", country="IN", country_src="web_verified",
    country_cite=DS_T, city="Bangalore", focus="Consumer & Marketplaces",
    note="Indian social e-commerce grocery company. Tiger Global led the $144M Series D of July 2021 at $455M "
         "(Moneycontrol; Entrackr); the May 2021 personal bets by Chase Coleman and Scott Shleifer (Entrackr) were not "
         "fund money (T2). The January 2022 round valued it at about $1.7B, but the mark has collapsed: in August 2026 "
         "DealShare was in advanced talks to sell to Truemeds in a share swap valuing it at a little over its roughly "
         "$90M cash (The Economic Times, 2026-08-30; Inc42, 2026-09-17): below $1B on that documented collapse.",
    rounds=[rnd("2021-07-08", "Series D", 144_000_000, "Tiger Global", True, DS_T, "press"),
            rnd("2022-01", "Series E", 165_000_000, "Tiger Global; Alpha Wave", True, NEWS("dealshare", "Cart Of Woes"), "press")]))

# ---------------------------------------------------------------- Deep Vision
DV_S = NEWS("deep-vision", "Deep Vision raises USD 35 mn from Tiger Global")
L.append(cls("deep-vision", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=DV_S, entry_date="2021-09", country="US", city="Los Altos",
    focus="Industrial & Robotics",
    note="Los Altos AI inference chip company. Tiger Global led its $35M Series B of September 2021 (The Statesman; "
         "FinSMEs names the Series B). Last known private. Momentum check: no later round found (Bing, Google News, "
         "2026-09-29).",
    rounds=[rnd("2021-09-20", "Series B", 35_000_000, "Tiger Global", True, DV_S, "press")]))

# ---------------------------------------------------------------- DeHaat (headline about another company)
L.append(verdict("dehaat", "not_member",
    "The only record is a Forbes India podcast headline listing separate stories ('Tiger Global backs Zolve; DeHaat "
    "raises $115 mln'): the Tiger investment it names is Zolve's. DeHaat's rounds (the $115M of October 2021, the "
    "Series E led by Sofina) do not name Tiger Global, and Bing finds no other item tying the firm to DeHaat",
    ec="web", conf="medium", cite=NEWS("dehaat", "Tiger Global backs Zolve; DeHaat raises")))

# ---------------------------------------------------------------- Delhivery (listed 2022)
DL_D = NEWS("delhivery", "Delhivery Snaps $85 Mn In Series D From Tiger")
DL_C = URLOF("delhivery", "Carlyle, Tiger Global bet $100 mn on logistics startup Delhivery", "vccircle.com")
DL_CAP = "https://stockanalysis.com/quote/nse/DELHIVERY/market-cap/"   # printed by WebSearch, read 2026-09-29
L.append(cls("delhivery", status="public", rng="1b_plus", usd=3_257_382_995, val_src="web_verified",
    val_cite=DL_CAP, asof="2026-09-29", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=DL_D,
    entry_date="2015-05", country="IN", country_src="web_verified", country_cite=DL_C, city="Gurugram",
    focus="Industrial & Robotics",
    note="Gurugram logistics and fulfilment company, listed on the NSE and BSE since May 2022. Tiger Global led the $85M "
         "Series D of May 2015 with existing investors (Inc42; Avendus: 'led by Tiger Global Management and existing "
         "investors'), bought a 10% stake from Multiples later in 2015 (Mint) and joined Carlyle's round in 2017 "
         "(VCCircle). Market cap INR 312.66B on 2026-09-29 (stockanalysis.com): INR 312.66B @ ECB 2026-09-29 "
         "(INR/EUR 108.991, EUR/USD 1.1355) = $3.26B.",
    rounds=[rnd("2015-05-05", "Series D", 85_000_000, "Tiger Global", True, DL_D, "press"),
            rnd("2017-03", "Unnamed", 100_000_000, "Carlyle", True, DL_C, "press")], extra=WV))

# ---------------------------------------------------------------- dELiA*s (13G only)
L.append(verdict("delias-inc", "not_member",
    T3 + ": dELiA*s was Nasdaq-listed from its 2005 spin-off from Alloy; Tiger's 13G filings date from 2014 and 2015",
    ec="fund_filing", conf="high", cite=SEC("delias-inc", "edgar", 0)))

# ---------------------------------------------------------------- Deliverr
DE_C = NEWS("deliverr", "Shopify Snaps Up Logistics Startup Deliverr")
L.append(cls("deliverr", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=DE_C, entry_date="2021-11", country="US", city="San Francisco",
    focus="Consumer & Marketplaces",
    note="San Francisco e-commerce fulfilment company. Tiger Global led the November 2021 Series E at about $2B post "
         "money (Crunchbase News; Bloomberg via Yahoo reported the Tiger-led round in October 2021); no earlier round "
         "names the firm. Shopify bought Deliverr for $2.1B in 2022 (Crunchbase News; Axios): acquired.",
    rounds=[rnd("2021-11", "Series E", 250_000_000, "Tiger Global", True, DE_C, "press")]))

# ---------------------------------------------------------------- Devron
DVN = NEWS("devron", "Devron, an AI fintech launched by a former CIA agent")
L.append(cls("devron", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=DVN, entry_date="2022-02", country="US", city="New York", focus="AI & Applied AI",
    note="New York federated machine-learning company. Tiger Global led its $12M Series A of February 2022 (Business "
         "Insider). Momentum check: no later round found (Bing, 2026-09-29).",
    rounds=[rnd("2022-02-10", "Series A", 12_000_000, "Tiger Global", True, DVN, "press")]))

# ---------------------------------------------------------------- DiDi
DI_X = PACK("didi")
L.append(cls("didi", status="public", rng="10b_plus", usd=16_180_000_000, val_src="web_verified",
    val_cite=SIB("didi", "coatue"), asof="2026-09-25", stage="undetermined", country="CN", country_src="web_verified",
    country_cite=DI_X, city="Beijing", focus="Consumer & Marketplaces",
    note="Beijing ride-hailing company (DiDi Global), listed on the NYSE in June 2021 and traded over the counter since "
         "its 2022 delisting. The F-1's shareholders agreement names Tiger Global Eight Holdings as an investor before "
         "the listing, alongside DiDi's Beijing group companies. The round in which Tiger first invested (in Kuaidi "
         "Dache before its 2015 merger with Didi, or in DiDi later) is not established: undetermined. Market cap "
         "$16.18B on 2026-09-25 (stockanalysis.com), the figure the Coatue book carries.",
    rounds=[], extra=WV))

# ---------------------------------------------------------------- Diligent Robotics
DR_B = NEWS("diligent-robotics", "Diligent Robotics Raises Over $30 Million in Series B")
DR_S = NEWS("diligent-robotics", "a Serve Robotics Company, Begins Rolling Out Moxi")
L.append(cls("diligent-robotics", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=DR_B, entry_date="2022-04", city="Austin", focus="Industrial & Robotics",
    note="Austin maker of the Moxi hospital service robot. Tiger Global led the Series B of more than $30M in April 2022 "
         "(PR Newswire). Serve Robotics agreed to acquire it in January 2026 (Serve's 8-K) and Diligent now operates as "
         "'a Serve Robotics Company' (its release of 2026-08-17): acquired.",
    rounds=[rnd("2022-04-11", "Series B", 30_000_000, "Tiger Global", True, DR_B, "company"),
            rnd("2026-01-21", "Acquisition (Serve Robotics)", None, "Serve Robotics", False, PACK("diligent-robotics"),
                "filing")]))

if __name__ == "__main__":
    jl.write("batch-004c", L)
