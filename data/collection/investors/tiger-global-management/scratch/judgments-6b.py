#!/usr/bin/env python3
"""PRO-167 grind, queue batch 6, chunk b (rows 16-30). Judge b6.

Evidence: the judge view (show.py --batch 5), the evidence pack, the Bing and Google candidate caches, Bing
lookups run with NQ_TAG=b6 (bq.py), sibling books' records, and pages fetched and read in this pass (the
literal URLs below). Every citation is read from disk by a helper or is a page fetched and read here."""
import json
import os
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PKD = json.loads((HERE / "evidence-pack.json").read_text())
BND = json.loads((HERE / "bing-news.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def PK(slug, sub, kind="press"):
    """A URL from the row's evidence-pack lines (press '|| URL', sec line tail, wiki or recall parentheses)."""
    p = PKD.get(slug, {})
    if kind == "recall":
        m = re.findall(r"\((https?://[^)\s]+)\)", p.get("recall_basis") or "")
        if not m:
            raise SystemExit(f"PK recall {slug}")
        return m[-1]
    urls = []
    for x in p.get(kind) or []:
        if sub.lower() not in x.lower():
            continue
        if kind == "press":
            m = re.search(r"\|\| URL (\S+)", x)
        elif kind == "sec":
            m = re.search(r"\| (https?://\S+)\s*$", x)
        else:
            m = re.search(r"\((https?://[^)\s]+)\)", x)
        if m:
            urls.append(m.group(1))
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {sub!r}, {kind}) -> {urls}")
    return urls[0]


def BN(key, sub):
    """A publisher URL from the Bing candidate cache (bing-news.json[key]) whose title contains sub."""
    urls = list(dict.fromkeys(i["url"] for i in (BND.get(key) or {}).get("items", [])
                              if sub.lower() in i["title"].lower()))
    if len(urls) != 1:
        raise SystemExit(f"BN({key!r}, {sub!r}) -> {urls}")
    return urls[0]


def SIB(slug, inv):
    """(usd, asof, citation) of a sibling book's mark for the same company, from the evidence pack."""
    for x in PKD.get(slug, {}).get("sib", []):
        if x["investor"] == inv and x.get("val_cite"):
            return int(float(x["usd"])), x["asof"], x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {inv!r}) missing")
def SIBREC(inv, slug, key):
    """A key of a sibling book's own classification record (data/collection/investors/<inv>), read from disk."""
    d = HERE.parents[1] / inv / "companies"
    rec = {**json.loads((d / "resolved.json").read_text()).get(slug, {}),
           **json.loads((d / "classification.json").read_text()).get(slug, {})}
    if not rec.get(key):
        raise SystemExit(f"SIBREC({inv!r}, {slug!r}, {key!r}) missing")
    return rec[key]


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []
CHECK = "2026-09-29"

# ---------------------------------------------------------------- goguardian (recall seed confirmed)
GG_BW = PK("goguardian", "", "recall")
GG_V = NEWS("goguardian", "GoGuardian Reaches $1 Billion Valuation")
L.append(cls("goguardian", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
             val_cite=GG_V, asof="2021-08-09", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=GG_BW, stage_conf="high", entry_date="2021-08-05",
             city="El Segundo", city_src="web_verified", focus="SaaS",
             note="K-12 classroom and device management software sold to schools, El Segundo (Los Angeles Business "
                  "Journal). Tiger's $200M strategic investment of August 2021 (the company's release), a minority "
                  "growth investment in a company then backed by Sumeru Equity Partners: Growth. The Business Journal "
                  "says the deal values the company 'at well over $1 billion'; the figure is recorded at that stated "
                  "$1B floor, at the band edge, and is older than 24 months, so stale.",
             rounds=[rnd("2021-08-05", "strategic investment ($200M)", 200_000_000, "Tiger Global Management", True,
                         GG_BW, "company")]))

# ---------------------------------------------------------------- gomechanic (recall seed confirmed)
GO_C = PK("gomechanic", "", "recall")
GO_SALE = NEWS("gomechanic", "LifeLong-led consortium acquires GoMechanic in slump sale")
L.append(cls("gomechanic", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GO_C, stage_conf="high", entry_date="2021-06-23",
             country="IN", country_src="web_verified", country_cite=GO_SALE, city="Gurugram",
             focus="Consumer & Marketplaces",
             note="Car servicing network, Gurugram. Tiger led the $42M Series C of June 2021 (ET Auto), after a "
                  "Sequoia-led Series B: Growth. After it admitted misreporting its financials, a consortium led by "
                  "Lifelong Group bought the business in a slump sale in March 2023 with no return to equity holders "
                  "(VCCircle; inc42): acquired out of distress.",
             rounds=[rnd("2021-06-23", "Series C", 42_000_000, "Tiger Global", True, GO_C, "press"),
                     rnd("2023-03-29", "slump sale to Lifelong-led consortium", None, None, None, GO_SALE, "press")]))

# ---------------------------------------------------------------- grab (recall seed confirmed)
GR_GMA = NEWS("grab", "SoftBank invests $250 million in Southeast Asian taxi-hailing app GrabTaxi")
gr_usd, gr_asof, gr_cite = SIB("grab", "coatue")
L.append(cls("grab", status="public", rng="10b_plus", usd=gr_usd, val_src="web_verified", val_cite=gr_cite,
             asof=gr_asof, extra=WV,
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014",
             country="SG", country_src="web_verified", country_cite=GR_GMA, city="Singapore",
             focus="Consumer & Marketplaces",
             note="Ride-hailing, delivery and payments, Singapore (Nasdaq: GRAB since the December 2021 SPAC merger). "
                  "Tiger was already an investor when SoftBank put in $250M in December 2014 (GMA News names 'US "
                  "investor Tiger Global Management' among the earlier backers of the then $90M-funded GrabTaxi); the "
                  "entry is Tiger's 2014 GrabTaxi Series C, a Growth round, named from knowledge (model, medium). "
                  "Market cap $12.77B on 2026-09-25 (StockAnalysis), aligned with the Coatue row.",
             rounds=[rnd("2014-12-04", "SoftBank round ($250M); Tiger an existing investor", 250_000_000, "SoftBank",
                         None, GR_GMA, "press")]))

# ---------------------------------------------------------------- grafana-labs (membership open)
GF_Y = PK("grafana-labs", "Yahoo Finance | Grafana Labs Surpasses")
L.append(verdict("grafana-labs", "member",
                 "Grafana Labs' release of 2025-09-30 (via Yahoo Finance) announces a secondary transaction led by "
                 "Ontario Teachers' Pension Plan 'with participation from Sapphire Ventures and Tiger Global': a "
                 "purchase of shares in the private company, a venture entry under T3 (secondaries are Growth)",
                 ec="web", conf="high", cite=GF_Y))
L.append(cls("grafana-labs", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=GF_Y, stage_conf="high", entry_date="2025-09-30",
             country="US", city="New York", focus="Data Infrastructure",
             note="Open-source observability (Grafana, Loki, Mimir), New York, as the Coatue, Lightspeed and Sequoia "
                  "rows read. Tiger bought in through the September 2025 secondary led by Ontario Teachers' (the "
                  "company's release, no valuation stated): Growth. The sibling rows carry $9B from a February 2026 "
                  "report of a round being raised (SiliconANGLE); the band is left for the web pass to pin with a "
                  "closed round.",
             rounds=[rnd("2025-09-30", "secondary", None, "Ontario Teachers' Pension Plan", True, GF_Y, "company")]))

# ---------------------------------------------------------------- grain (recall seed confirmed)
GN_TC = PK("grain", "", "recall")
L.append(cls("grain", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=GN_TC, stage_conf="high", entry_date="2022-04-12",
             country="US", focus="SaaS", flags=["city_unknown"],
             note="Grain, meeting recording and highlights software (now an AI note-taker), a fully remote company "
                  "(TechCrunch). Tiger led the $16M round of April 2022, which Business Insider calls the Series A: "
                  "Tiger's entry. City not placed (remote, no head office stated). The Bain Capital Ventures (Tel "
                  "Aviv fintech) and Y Combinator (fintech) rows named Grain are other companies.",
             rounds=[rnd("2022-04-12", "Series A", 16_000_000, "Tiger Global", True, GN_TC, "press")]))

# ---------------------------------------------------------------- green-bits (recall seed confirmed)
GB_BI = PK("green-bits", "", "recall")
GB_SALE = PK("dutchie", "Tiger Global-Led Group")
L.append(cls("green-bits", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GB_BI, stage_conf="medium", entry_date="2018-04",
             country="US", city="San Jose", focus="SaaS",
             note="Point-of-sale and compliance software for cannabis retailers, San Jose. Tiger led the $17M round of "
                  "April 2018 (Business Insider; CNBC), the company's Series B after an earlier round from Casa Verde: "
                  "Growth. Dutchie bought Greenbits in March 2021, in the same announcement as its Tiger-led Series C "
                  "(Yahoo Finance, 2021-03-16): acquired.",
             rounds=[rnd("2018-04-21", "Series B ($17M)", 17_000_000, "Tiger Global", True, GB_BI, "press"),
                     rnd("2021-03-16", "acquired by Dutchie", None, None, None, GB_SALE, "press")]))

# ---------------------------------------------------------------- greyorange (recall seed confirmed)
GO_A = NEWS("greyorange", "Grey Orange raises Series A funding from Tiger Global")
GO_HQ = NEWS("greyorange", "GreyOrange Locating Global Headquarters In Georgia")
L.append(cls("greyorange", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=GO_A, stage_conf="high", entry_date="2014-04-29",
             country="US", country_src="web_verified", country_cite=GO_HQ, city="Roswell",
             focus="Industrial & Robotics",
             note="Warehouse robotics and fulfilment software, founded in Gurgaon, global headquarters moved to "
                  "Roswell, Georgia, in metro Atlanta in 2021 (Yahoo and Business Facilities, 2021). Tiger and Blume Ventures funded the Series A of "
                  "April 2014 (YourStory) and the $30M Series B of August 2015: Tiger's entry is the Series A. "
                  "Mithril led the $140M round of 2018.",
             rounds=[rnd("2014-04-29", "Series A", None, "Tiger Global, Blume Ventures", True, GO_A, "press"),
                     rnd("2015-08-10", "Series B", 30_000_000, "Tiger Global", True,
                         PK("greyorange", "", "recall"), "press")]))

# ---------------------------------------------------------------- gridware (membership open)
GW_Y = PK("gridware", "Yahoo Finance | Gridware Raises $55 Million Growth Round")
L.append(verdict("gridware", "member",
                 "Gridware's release (2025-11-17, via Yahoo Finance): 'Gridware announced a $55 million Series B "
                 "strategic growth round led by Tiger Global and Generation Investment Management', a private round",
                 ec="web", conf="high", cite=GW_Y))
L.append(cls("gridware", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GW_Y, stage_conf="high", entry_date="2025-11-17",
             country="US", city="San Francisco", focus="Climate & Energy",
             note="Continuous power-grid monitoring sensors, San Francisco (the release's dateline). Tiger and "
                  "Generation co-led the $55M Series B of November 2025, after a Sequoia-backed Series A: Growth.",
             rounds=[rnd("2025-11-17", "Series B", 55_000_000, "Tiger Global, Generation Investment Management", True,
                         GW_Y, "company")]))

# ---------------------------------------------------------------- grofers (recall seed confirmed)
GF_A = PK("grofers", "", "recall")
GF_Z = NEWS("grofers", "Loss Up 35% QoQ To INR 251 Cr On Blinkit Acquisition")
L.append(cls("grofers", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=GF_A, stage_conf="medium", entry_date="2015-02-27",
             country="IN", country_src="web_verified", country_cite=W("Blinkit"), city="Gurugram",
             focus="Consumer & Marketplaces",
             note="Grocery delivery, Gurugram (Grofers, renamed Blinkit in 2021). Sequoia and Tiger provided the $10M "
                  "round of February 2015 (YourStory; inc42), the company's first institutional round: Tiger's entry, "
                  "the Series A. Tiger led the $35M Series B of April 2015. Zomato completed its all-stock acquisition "
                  "of Blinkit on 2022-08-10 (inc42): acquired; the Zomato shares Tiger received are sale "
                  "consideration, not a Zomato entry.",
             rounds=[rnd("2015-02-27", "Series A", 10_000_000, "Sequoia Capital", True, GF_A, "press"),
                     rnd("2022-08-10", "acquired by Zomato", None, None, None, GF_Z, "press")]))

# ---------------------------------------------------------------- groq (recall seed confirmed)
GQ_C = PK("groq", "", "recall")
GQ_V = NEWS("groq", "Groq raises $350M to fuel its pivot")
L.append(cls("groq", status="private", rng="1b_plus", usd=3_500_000_000, val_src="web_verified", val_cite=GQ_V,
             asof="2026-08-17", extra=WV, clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=GQ_C, stage_conf="high", entry_date="2021-04-14",
             city="Mountain View", focus="AI & Applied AI",
             note="AI inference chips, now an AI inference cloud, Mountain View. Tiger and D1 led the $300M Series C "
                  "of April 2021 (Yahoo Finance; Wikipedia): Growth. Nvidia's $20B licensing deal of December 2025 "
                  "took the founder and core team but not the company, which kept operating and raised $650M in June "
                  "2026 and $350M at $3.5B in August 2026, led by Disruptive (TechCrunch; the round halved the $6.9B "
                  "of September 2025): private under the acqui-hire rule, marked at the latest priced round.",
             rounds=[rnd("2021-04-14", "Series C", 300_000_000, "Tiger Global, D1 Capital", True, GQ_C, "press"),
                     rnd("2026-08-17", "unnamed ($350M at $3.5B)", 350_000_000, "Disruptive", None, GQ_V, "press")]))

L.append(verdict("groupon-inc", "not_member",
                 T3 + ": Groupon listed on Nasdaq in November 2011; Tiger's 13F lists it 2012-2013 and its 13G dates "
                      "from 2012-2014; no prospectus names a Tiger vehicle", ec="fund_filing", conf="high",
                 cite=SEC("groupon-inc", "edgar")))

# ---------------------------------------------------------------- groww (recall seed confirmed)
GW_D = NEWS("groww", "raises $83 million in Series D from Tiger Global")
gw_usd, gw_asof, gw_cite = SIB("groww", "ribbit-capital")
L.append(cls("groww", status="public", rng="10b_plus", usd=gw_usd, val_src="web_verified", val_cite=gw_cite,
             asof=gw_asof, extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=GW_D, stage_conf="high", entry_date="2021-04-07",
             country="IN", country_src="web_verified",
             country_cite=SIBREC("ribbit-capital", "groww", "hq_country_citation"), city="Bangalore",
             focus="Fintech & Payments",
             note="Retail investing platform, Bengaluru; listed on the NSE in November 2025 (Billionbrains Garage "
                  "Ventures), with Tiger selling part of its stake in the offer. Tiger led the $83M Series D of April "
                  "2021 that made the company a unicorn (CNBC TV18), after Ribbit's Series B and YC Continuity's "
                  "Series C: Growth. Market cap $12.19B on 2026-09-28 (StockAnalysis; INR 1170.00B @ ECB 2026-09-28 "
                  "(INR/EUR 109.2095, EUR/USD 1.1378) = $12.19B), aligned with the ICONIQ and Ribbit rows.",
             rounds=[rnd("2021-04-07", "Series D", 83_000_000, "Tiger Global", True, GW_D, "press")]))

# ---------------------------------------------------------------- groyyo (recall seed confirmed)
GY_A = PK("groyyo", "", "recall")
GY_BL = PK("groyyo", "Business Line | B2B manufacturing start-up Groyyo")
L.append(cls("groyyo", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=GY_A, stage_conf="high", entry_date="2022-06-13",
             country="IN", country_src="web_verified", country_cite=GY_BL, city="Mumbai",
             focus="Consumer & Marketplaces",
             note="B2B apparel manufacturing and supply-chain platform, Mumbai (Business Line). Tiger led the $40M "
                  "Series A of June 2022, equity and debt (VCCircle; PTI), after a $4.6M seed led by Alpha Wave "
                  "Incubation in January 2022: Tiger's entry. Cornerstone Ventures led a Series B in 2026.",
             rounds=[rnd("2022-06-13", "Series A", 40_000_000, "Tiger Global", True, GY_A, "press")]))

# ---------------------------------------------------------------- grubmarket (membership open)
GM_Y = PK("grubmarket", "Yahoo Finance | General Mills Backs GrubMarket")
GM_H = NEWS("grubmarket", "$50 Million Series H At $4.5 Billion")
L.append(verdict("grubmarket", "member",
                 "Bloomberg via Yahoo Finance (2022-09-28), on the General Mills-backed round at over $2B: 'Existing "
                 "investors including Tiger Global, Liberty Street Funds, Walleye Capital, Celtic House Asia Partners "
                 "and Apeira Capital also participated', a private round in which the firm put in money as an "
                 "existing holder", ec="web", conf="high", cite=GM_Y))
L.append(cls("grubmarket", status="private", rng="1b_plus", usd=4_500_000_000, val_src="web_verified",
             val_cite=GM_H, asof="2026-02-02", extra=WV, stage="undetermined",
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             note="Food supply-chain software and wholesale distribution, San Francisco. Tiger was an existing "
                  "investor that joined the September 2022 round at over $2B (Bloomberg); the round in which it first "
                  "entered is not on record, so the stage is undetermined. Mark: the $50M Series H of February 2026 "
                  "at a $4.5B pre-money valuation (Pulse 2.0, 2026-02-03), as the Y Combinator row reads; a "
                  "confidential IPO filing followed in July 2026, and a September 2026 report of the company being "
                  "down 48% reads secondary prices, not a priced round (same band either way).",
             rounds=[rnd("2022-09-28", "unnamed (General Mills-backed, over $2B)", None, None, True, GM_Y, "press"),
                     rnd("2026-02-02", "Series H", 50_000_000, None, None, GM_H, "company")]))

# ---------------------------------------------------------------- guardio (recall seed confirmed)
GU_TC = PK("guardio", "", "recall")
L.append(cls("guardio", status="private", rng="below_1b", stage="undetermined",
             country="IL", country_src="web_verified", country_cite=GU_TC, city="Tel Aviv", focus="Security",
             note="Consumer security browser extension and app, Tel Aviv (TechCrunch). Tiger led the company's first "
                  "outside funding, $47M in December 2021 (TechCrunch), which no source names as a seed or a Series "
                  "A, so the stage is undetermined although the entry is dated. ION Crossover Partners put in $80M in "
                  "November 2025.",
             rounds=[rnd("2021-12-14", "first outside round (unnamed, $47M)", 47_000_000, "Tiger Global", True, GU_TC,
                         "press")]))

if __name__ == "__main__":
    jl.write("batch-006b", L, record=os.environ.get("DRY") != "1")
