#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 13, chunk c (rows 31-45). Run: NQ_TAG=b13 python3 judgments-13c.py"""
import json
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

_PK = json.loads((HERE / "evidence-pack.json").read_text())
_FTS = json.loads((HERE / "recall" / "fts-triage.json").read_text())


def PU(slug, sub, kind="press"):
    """The URL printed on the row's evidence line (press '|| URL', sec '| https', recall '(https')."""
    p = _PK.get(slug) or {}
    lines = [p.get("recall_basis") or ""] if kind == "recall" else (p.get(kind) or [])
    hits = []
    for ln in lines:
        if sub.lower() not in ln.lower():
            continue
        m = re.search(r"\|\| URL (\S+)", ln) or re.search(r"\| (https?://\S+)", ln) \
            or re.search(r"\((https?://[^)\s]+)\)", ln)
        if m:
            hits.append(m.group(1))
    hits = list(dict.fromkeys(hits))
    if len(hits) != 1:
        raise SystemExit(f"PU({slug!r}, {sub!r}, {kind!r}) matched {len(hits)}")
    return hits[0]


def FTS(company, registrant_sub):
    """The filing URL of the FTS triage entry for this company and registrant (read from disk)."""
    m = [x for x in _FTS if isinstance(x, dict) and x.get("company") == company
         and registrant_sub in (x.get("registrant") or "")]
    if len(m) != 1:
        raise SystemExit(f"FTS({company!r}, {registrant_sub!r}) matched {len(m)}")
    return m[0]["url"]



_SIB = json.loads((HERE / "siblings.json").read_text())


def SIB(slug, investor):
    """(usd, asof, val_cite) of a sibling book's row for the same company, read from siblings.json."""
    m = [x for x in _SIB.get(slug, []) if x["investor"] == investor]
    if len(m) != 1 or not m[0].get("val_cite"):
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)} or has no citation")
    return m[0]["val_cite"]


L = []
WV = {"valuation_range_source": "web_verified"}
T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"

# 31 Trendyol
wt = W("Trendyol")
tc = PU("trendyol", "techcrunch.com/2011/07/22")
L.append(cls("trendyol", status="acquired", rng="below_1b", stage="undetermined",
             rounds=[rnd("2010", "first outside investment, six months after founding (round not named)", None,
                         "Tiger Global", True, wt, "press"),
                     rnd("2011-07", "round of $25M to $30M", None, "Kleiner Perkins and Tiger Global", True, tc, "press"),
                     rnd("2018", "Alibaba majority purchase", 728_000_000, "Alibaba", False, wt, "press"),
                     rnd("2021-08", "funding at $16.5B", 1_500_000_000, None, False,
                         NEWS("trendyol", "Trendyol becomes Turkey's 1st"), "press")],
             city="Istanbul", focus="Consumer & Marketplaces",
             note="Tiger invested six months after the 2010 founding (Wikipedia) and again beside Kleiner Perkins "
                  "in July 2011 (TechCrunch; Webrazzi put Tiger's stake at 45%); neither round is named, so the "
                  "stage is undetermined. Alibaba bought a majority in 2018 (Tiger exited then); read acquired, "
                  "as Accel's book reads Flipkart after Walmart's majority purchase, although Trendyol later "
                  "raised $1.5B at $16.5B from outside investors (Anadolu Agency, August 2021)."))

# 32 TRM Labs
bw = PU("trm-labs", "Series B Led by Tiger Global")
L.append(cls("trm-labs", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
             val_cite=SIB("trm-labs", "y-combinator"), asof="2026-02-04", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=bw, stage_conf="high", entry_date="2021-12",
             rounds=[rnd("2021-12", "Series B", 60_000_000, "Tiger Global", True, bw, "press"),
                     rnd("2022-11", "Series B extension", 70_000_000, "Thoma Bravo", None, None, "press"),
                     rnd("2026-02-04", "funding at $1B", 70_000_000, None, None, SIB("trm-labs", "y-combinator"), "press")],
             country="US", city="San Francisco", focus="Fintech & Payments",
             note="Tiger led the $60M Series B in December 2021 (Business Wire); the earlier seed and Series A "
                  "are not recorded with Tiger. Mark: the February 2026 $70M round at $1B (SiliconANGLE), as on "
                  "YC's row; that round is the momentum check's newer priced round."))

# 33 TrueLayer
ca = PU("truelayer", "City A.M.")
toi = PU("truelayer", "Indiatimes")
dn = PU("truelayer", "Tiger-Backed TrueLayer")
L.append(cls("truelayer", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": dn, "valuation_asof": "2024-10-04"},
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=ca, stage_conf="high", entry_date="2021-09",
             rounds=[rnd("2021-09", "Series E", 130_000_000, "Tiger Global Management", True, ca, "press"),
                     rnd("2024-10", "down round below $1B", None, None, None, dn, "press")],
             country="GB", country_src="web_verified", country_cite=toi, city="London", focus="Fintech & Payments",
             note="Tiger led the $130M Series E of September 2021 that valued TrueLayer above $1B (City A.M.; "
                  "Reuters). Collapse evidence: the October 2024 round cost TrueLayer its unicorn status "
                  "(Bloomberg via Yahoo), so the band is below_1b."))

# 34 TSMC
L.append(verdict("tsmc", "not_member",
                 "The seed headline reports Tiger raising its 13F stake in TSMC, listed in Taiwan since 1994 and as "
                 "NYSE ADRs since 1997: a public-market holding, no private round names the firm (T3, D3).",
                 ec="web", conf="high", cite=PU("tsmc", "Raises Share Stake", "recall")))

# 35 Tuniu
L.append(verdict("tuniu-corp", "not_member",
                 T3 + ". Tuniu listed on Nasdaq in May 2014; Tiger's 13G filings (2014) and its one 13F quarter "
                 "(2014-06-30) follow the listing.",
                 ec="fund_filing", conf="high", cite=SEC("tuniu-corp", "edgar")))

# 36 TVF (same company as the-viral-fever, classified identically)
bs = PU("the-viral-fever", "Business Standard")
L.append(cls("tvf", status="private", rng="below_1b", stage="undetermined",
             rounds=[rnd("2016-02", "first institutional investment (round not named)", 10_000_000, "Tiger Global", True, bs, "press"),
                     rnd("2018-07", "down round", 6_000_000, "Tiger Global", True, PU("tvf", "pumps $6 mn more"), "press"),
                     rnd("2019-05", "funding (inc42's URL calls it Series D)", 5_000_000, "Tiger Global", True,
                         PU("tvf", "TVF valuation doubles"), "press")],
             country="IN", country_src="web_verified", country_cite=bs, city="Mumbai",
             focus="Media, Gaming & Advertising",
             note="The Viral Fever (TVF, Contagious Online Media Network) took $10M from Tiger in February 2016 for "
                  "about a fifth of the company, its first institutional money, with no round label in the "
                  "record (Business Standard cites the RoC filing), so the stage is undetermined. Tiger added $6M "
                  "in a 2018 down round and about $5M in 2019 at an $80M valuation (Mint). Rows the-viral-fever "
                  "and tvf are one company."))

# 37 UiPath (seed stands)
ae = NEWS("uipath", "UiPath Raises $225M Series E")
kf = NEWS("uipath", "UiPath closes $750 million in series F")
L.append(cls("uipath", rng="1b_plus", usd=6_490_000_000, val_src="web_verified", val_cite=SIB("uipath", "coatue"),
             asof="2026-09-25", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=ae, stage_conf="medium", entry_date="2020-07",
             rounds=[rnd("2020-07", "Series E", 225_000_000, "Alkeon Capital", True, ae, "press"),
                     rnd("2021-02", "Series F", 750_000_000, "Alkeon Capital and Coatue", True, kf, "press")],
             city="New York", focus="SaaS",
             note="Tiger is in the July 2020 $225M Series E (analyticsindiamag, surfaced by a Tiger Global query) "
                  "and a 'returning investor' in the February 2021 Series F (KMWorld); no record puts it in the "
                  "2019 Series D or earlier. Market cap $6.49B (stockanalysis.com, 2026-09-25), as on the Coatue "
                  "and IVP rows; the float figure is superseded."))

# 38 Ula
p = NEWS("ula", "Ula Closes Series B Round with Additional")
L.append(cls("ula", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=p, stage_conf="high", entry_date="2021-11",
             rounds=[rnd("2021-10", "Series B", 87_000_000, "Prosus Ventures, Tencent and B Capital", False,
                         NEWS("ula", "raises US$87m in round co-led by Tencent"), "press"),
                     rnd("2021-11", "Series B extension", 23_100_000, "Tiger Global and Binny Bansal", True, p, "press")],
             country="ID", country_src="web_verified", country_cite=PU("ula", "ACV Capital"), city="Jakarta",
             focus="Consumer & Marketplaces",
             note="Tiger led the $23.1M addition that closed Ula's Series B in November 2021 (PYMNTS), its first "
                  "round in the company. Status defunct as on Lightspeed's row (the B2B marketplace wound down)."))

# 39 Unacademy
y = PU("unacademy", "Yahoo Finance")
L.append(cls("unacademy", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=y, stage_conf="high", entry_date="2020-11",
             rounds=[rnd("2020-02", "funding", 110_000_000, None, False, None, "press"),
                     rnd("2020-11", "funding at $2B", None, "Tiger Global and Dragoneer", True, y, "press")],
             country="IN", country_src="web_verified", country_cite=y, city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Tiger's first Unacademy investment is the November 2020 round at $2B (Reuters via Yahoo), after "
                  "the company's earlier lettered rounds, so Growth. Acquired: upGrad completed the purchase in "
                  "September 2026 for about $200M (Business Standard: "
                  + NEWS("unacademy", "Unacademy completes deal") + ")."))

# 40 Unblocked
fb = PU("unblocked", "Forbes")
L.append(cls("unblocked", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=fb, stage_conf="high", entry_date="2022-01",
             rounds=[rnd("2022-01", "Seed", 10_000_000, None, True, fb, "press")],
             country="CA", city="Vancouver", focus="DevTools & APIs",
             note="Tiger, Dapper Labs and Marcy Venture Partners backed Unblocked's seed at a $90M valuation in "
                  "January 2022 (Forbes). The startup then built NFT platforms; First Round's Vancouver "
                  "developer-tools Unblocked is very likely the same company after a pivot (not confirmed from one "
                  "source), and its city and country are used. Graduation left for the graduation pass."))

# 41 Unicommerce
wu = W("Unicommerce")
L.append(cls("unicommerce", status="public", rng="below_1b", stage="undetermined",
             rounds=[rnd("2013", "undisclosed funding", None, "Nexus Venture Partners", False, wu, "press"),
                     rnd("2014-11", "funding", 10_000_000, "Tiger Global", True, PU("unicommerce", "inc42.com | Unicommerce Raises"), "press")],
             country="IN", country_src="web_verified", country_cite=wu, city="Gurugram", focus="SaaS",
             note="Tiger put $10M into Unicommerce in November 2014 after Nexus's undisclosed 2013 funding; "
                  "neither source names the round, so the stage is undetermined. Snapdeal bought the company in "
                  "2015 and Tiger's stake was settled in a share allotment; Unicommerce listed on the Indian "
                  "exchanges in August 2024, market cap well below $1B."))

# 42 Unit21
y = PU("unit21", "finance.yahoo.com/news/tiger-global-leads-34m")
L.append(cls("unit21", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=y, stage_conf="high", entry_date="2021-07",
             rounds=[rnd("2021-07", "Series B", 34_000_000, "Tiger Global", True, y, "press"),
                     rnd("2022", "Series C", 45_000_000, "Tiger Global and South Park Commons", True,
                         PU("unit21", "crowdfundinsider.com/2023/07"), "press")],
             country="US", city="San Francisco", focus="Fintech & Payments",
             note="Tiger led the $34M Series B in July 2021 (TechCrunch via Yahoo) and co-led the $45M Series C "
                  "of 2022, announced June 2023. Momentum check (Bing News 2026-09-29): no later priced round. "
                  "Agrees with ICONIQ's row."))

# 43 Upscale AI
ya = PU("upscale-ai", "finance.yahoo.com/news/100m-seed")
rv = PU("upscale-ai", "Institutional Investor", "recall")
L.append(cls("upscale-ai", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified",
             val_cite=rv, asof="2026-06-22", extra=WV,
             stage="Series A", stage_src="web_verified", stage_cite=ya, stage_conf="high", entry_date="2026-01-21",
             rounds=[rnd("2025", "Seed", 100_000_000, None, None, ya, "company"),
                     rnd("2026-01-21", "Series A", 200_000_000, "Tiger Global, Premji Invest and Xora Innovation", True, ya, "company"),
                     rnd("2026-06-22", "Series A-1", 190_000_000, None, True, rv, "press")],
             country="US", city="Santa Clara", focus="Data Infrastructure",
             note="Tiger co-led the $200M Series A of January 2026 (the company's release, Santa Clara); the $100M "
                  "seed before it is not recorded with Tiger. Mark: the June 2026 $190M Series A-1 extension at "
                  "$2B, which Tiger backed (Institutional Investor; Reuters reported the same figure)."))

# 44 Upstox
i42 = PU("upstox", "inc42.com")
vc = PU("upstox", "Upstox raises $25 mn from Tiger Global affiliate")
L.append(cls("upstox", status="private", rng="1b_plus", usd=3_390_000_000, val_src="web_verified", val_cite=vc,
             asof="2021-11-25", extra=WV, flags=["stale"], clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=i42, stage_conf="medium", entry_date="2019-09",
             rounds=[rnd("2019-09", "funding", 25_000_000, "Tiger Global", True, i42, "press"),
                     rnd("2021-11", "funding at $3.39B", 25_000_000, "Tiger Global", True, vc, "press")],
             country="IN", country_src="web_verified", country_cite=i42, city="Mumbai", focus="Fintech & Payments",
             note="Tiger's first Upstox (RKSV) investment is the $25M of September 2019 (inc42), after the "
                  "broker's earlier institutional round, so Growth. Mark: Tiger's November 2021 top-up at $3.39B "
                  "(VCCircle), stale; no later priced round or collapse evidence found."))

# 45 Urban Company (UrbanClap)
bl = PU("urbanclap", "Business Line")
wuc = W("Urban Company")
L.append(cls("urban-company", status="public", rng="1b_plus", usd=2_590_091_430, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/nse/URBANCO/market-cap/", asof="2026-09-29", extra=WV,
             flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=bl, stage_conf="high", entry_date="2019-08",
             rounds=[rnd("2019-08", "Series E", 75_000_000, "Tiger Global", True, bl, "press"),
                     rnd("2021-06", "Series F", 255_000_000, "Prosus Ventures, Dragoneer and Wellington", True, wuc, "press")],
             country="IN", country_src="web_verified", country_cite=wuc, city="Gurugram",
             focus="Consumer & Marketplaces",
             note="Urban Company (UrbanClap until 2020) listed on the NSE and BSE in September 2025; the known "
                  "'acquired' was wrong. Market cap INR 248.61B @ ECB 2026-09-29 (INR/EUR 108.991, EUR/USD "
                  "1.1355) = $2.59B (stockanalysis.com). Tiger led the $75M Series E in August 2019 (Business "
                  "Line), its first round. Rows urban-company and urbanclap are one company. Accel's row "
                  "(private, below_1b, 'Gurgaon') predates the listing."))

if __name__ == "__main__":
    jl.write("batch-013c", L)
