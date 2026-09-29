#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 14, chunk c (rows 31-45). Run: NQ_TAG=b14 python3 judgments-14c.py"""
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


def BING(slug, sub, source):
    """The URL of the one Bing item for this slug whose title contains sub and whose publisher is source."""
    items = []
    for f in sorted(HERE.glob("news-extra-bing*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    m = list(dict.fromkeys(i["url"] for i in items
                           if sub.lower() in i["title"].lower() and (i.get("source") or "") == source))
    if len(m) != 1:
        raise SystemExit(f"BING({slug!r}, {sub!r}, {source!r}) matched {len(m)}")
    return m[0]


L = []
WV = {"valuation_range_source": "web_verified"}
T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"

# 76 Wow! Momo
lm = PU("wow-momo", "Livemint")
L.append(cls("wow-momo", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=lm, stage_conf="medium", entry_date="2019-09",
             rounds=[rnd("2019-09", "funding at $120M", 23_000_000, "Tiger Global", True, lm, "press"),
                     rnd("2021-09", "Series C", 15_000_000, "Tree Line Investment Management", True, None, "press")],
             country="IN", country_src="web_verified", country_cite=lm, city="Kolkata", focus="Consumer & Marketplaces",
             note="Tiger led the $23M round at a $120M valuation in September 2019 (Mint), its first; the next "
                  "round (September 2021, Tree Line) is the Series C, so Tiger's round was the Series B."))

# 77 Xanadu (seed stands)
xs = NEWS("xanadu", "Xanadu secures $120 million CAD")
L.append(cls("xanadu", status="public", rng="1b_plus", usd=1_450_000_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/xndu/market-cap/", asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=xs, stage_conf="medium", entry_date="2021-05",
             rounds=[rnd("2021-05", "Series B (CAD 120M)", None, "Bessemer Venture Partners", True, xs, "company")],
             country="CA", country_src="web_verified", country_cite=NEWS("xanadu", "Quantum's next big bet"),
             city="Toronto", focus="Industrial & Robotics",
             note="Tiger joined Xanadu's CAD 120M Series B led by Bessemer in May 2021 (the company's release, "
                  "surfaced by a Tiger Global query); PIP 14 later signed the coattail agreement. Listed on Nasdaq "
                  "on 27 March 2026 through the Crane Harbor SPAC merger; market cap $1.45B (stockanalysis.com, "
                  "2026-09-29). Quantum hardware reads Industrial & Robotics, as PsiQuantum and IonQ do."))

# 78 Xendit
ac = PU("xendit", "acv.vc")
L.append(cls("xendit", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
             val_cite=SIB("xendit", "accel"), asof="2021-09", extra=WV, flags=["stale"],
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=ac, stage_conf="high", entry_date="2021-09",
             rounds=[rnd("2021-09", "Series C", 150_000_000, "Tiger Global", True, ac, "press"),
                     rnd("2022-05", "Series D", 300_000_000, "Coatue and Insight Partners", None,
                         PU("xendit", "Indonesian Stripe rival"), "press")],
             country="ID", country_src="web_verified", country_cite=ac, city="Jakarta", focus="Fintech & Payments",
             note="Tiger led the $150M Series C of September 2021 that made Xendit a unicorn; the May 2022 Series D "
                  "was reported without a valuation, so the $1B mark stands, stale, as on the Accel, Coatue, "
                  "Insight and YC rows. Momentum check: no later priced round found."))

# 79 Xentral
wx = W("Xentral ERP Software")
L.append(cls("xentral-erp-software", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=wx, stage_conf="high", entry_date="2021-08",
             rounds=[rnd("2021-08", "Series B", 75_000_000, "Tiger Global Management and Meritech Capital", True, wx, "press")],
             country="DE", country_src="web_verified", country_cite=wx, city="Augsburg", focus="SaaS",
             note="Tiger and Meritech led the $75M Series B in August 2021 (Wikipedia); the earlier Series A was "
                  "Sequoia's."))

# 80 Yandex N.V.
yf = PU("yandex-n-v", "IPO F-1", "recall")
L.append(verdict("yandex-n-v", "member",
                 "Yandex's 2011 F-1: Tiger Global Holding Coöperatief U.A. held 70.9% of the Class A shares (20.26% "
                 "of voting power) before the May 2011 IPO, with a registration rights agreement since 2008, and "
                 "bought further Class A shares from existing shareholders in August 2009: a private position, a "
                 "voting minority (not control).",
                 ec="fund_filing", conf="high", cite=yf))
L.append(cls("yandex-n-v", status="acquired", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium",
             rounds=[rnd("2009-08", "purchase of 6,893,982 Class A shares from existing shareholders", None, None, True, yf, "filing")],
             country="RU", country_src="web_verified", country_cite=yf, city="Moscow",
             focus="Media, Gaming & Advertising",
             note="Tiger already held 18.31% of Yandex's voting power before the August 2009 purchase from existing "
                  "holders (F-1); its first purchase is not dated in the passage read, so no entry date. A "
                  "pre-IPO stake in a large private company bought from holders is a secondary, Growth (D6). "
                  "Status: the Russian business was sold to a consortium of Russian investors in July 2024 and "
                  "the Dutch parent became Nebius Group, a different business; read acquired."))

# 81 Yatsen
yd = PU("yatsen-holding-ltd", "IPO DRS", "sec")
L.append(verdict("yatsen-holding-ltd", "member",
                 "Yatsen's 2020 IPO registration statement: an exhibit is an investment agreement with Tiger Global "
                 "as 'Investor', and Tiger Global Hong Kong's managing director Pengfei Wang has sat on the board "
                 "since March 2020, before the November 2020 IPO: a private round naming the firm.",
                 ec="fund_filing", conf="high", cite=yd))
L.append(cls("yatsen-holding-ltd", status="public", rng="below_1b", usd=236_380_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/ysg/market-cap/", asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020",
             rounds=[rnd("2020", "investment agreement (Tiger Global as Investor)", None, None, True, yd, "filing")],
             country="CN", country_src="web_verified", country_cite=yd, city="Guangzhou",
             focus="Consumer & Marketplaces",
             note="Tiger's investment agreement dates to 2020, when the Perfect Diary maker was already a large "
                  "company with earlier rounds, so Growth; the series is not named in the passage read. "
                  "NYSE-listed since November 2020; market cap $236M (stockanalysis.com, 2026-09-29)."))

# 82 Yuno
tc = PU("yuno", "techcrunch.com/2024/03/05")
L.append(cls("yuno", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=tc, stage_conf="high", entry_date="2024-03",
             rounds=[rnd("2022", "Seed", 10_000_000, "Andreessen Horowitz", False, tc, "press"),
                     rnd("2024-03", "Series A", 25_000_000, "DST Global Partners", True, tc, "press"),
                     rnd("2026-08", "Series B", 45_000_000, "Global PayTech Ventures", True,
                         BING("yuno", "Yuno secures $45m Series B", "Yahoo Finance"), "press")],
             country="CO", country_src="web_verified", country_cite=tc, city="Bogotá", focus="Fintech & Payments",
             note="Tiger joined the $25M Series A led by DST Global Partners in March 2024 at a $150M valuation "
                  "(TechCrunch); the 2022 $10M seed is recorded with a16z, not Tiger. TechCrunch calls Yuno 'the "
                  "Colombian payments startup'; a16z's row reads US with no city. Momentum check: the August 2026 "
                  "$45M Series B carried no reported $1B mark."))

# 83 YY (JOYY) (seed stands)
ye = PU("yy", "IPO F-1 exhibits", "sec")
L.append(cls("yy", status="public", rng="1b_plus", usd=3_930_000_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/joyy/market-cap/", asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=ye, stage_conf="medium",
             rounds=[rnd("2011", "purchase of Series A, B, C-1 and C-2 preferred from existing holders", None, None, True, ye, "filing")],
             country="SG", country_src="web_verified", country_cite="https://stockanalysis.com/stocks/joyy/company/",
             city="Singapore", focus="Media, Gaming & Advertising",
             note="Tiger Global Six YY Holdings bought preferred shares from existing holders (Morningside among "
                  "the vendors) under the agreement filed with YY's 2012 F-1, a secondary in a private company, "
                  "Growth (D6); shares were issued to it before the SAFE registration of 6 February 2012 (20-F), "
                  "the exact date not read. JOYY (YY until 2019) is headquartered in Singapore; market cap $3.93B "
                  "(stockanalysis.com, 2026-09-29)."))

# 84 ZAK
nf = PU("zak", "NeoFeed")
L.append(cls("zak", status="private", rng="below_1b", stage="undetermined",
             rounds=[rnd("2021-11", "funding of R$80M (round not named)", None, "Tiger Global", True, None, "press"),
                     rnd("2022-08", "rescue round at a lower valuation", None, "Tiger Global", True, nf, "press")],
             country="BR", country_src="web_verified", country_cite=nf, city="São Paulo", focus="SaaS",
             note="Tiger wrote ZAK's R$80M cheque in November 2021 (Globo) and led a rescue round at a lower "
                  "valuation in August 2022 (NeoFeed); neither names the round, so the stage is undetermined. "
                  "Momentum check: no later round found (Bing News 2026-09-29)."))

# 85 Zaraye
dw = PU("zaraye", "dawn.com/news")
L.append(cls("zaraye", status="private", rng="below_1b",
             stage="Pre-Seed", stage_src="web_verified", stage_cite=dw, stage_conf="high", entry_date="2022-04",
             rounds=[rnd("2022-04", "Pre-Seed", 2_100_000, "Tiger Global and Zayn Capital", True, dw, "press")],
             country="PK", country_src="web_verified", country_cite=dw, city="Karachi", focus="Consumer & Marketplaces",
             note="Tiger and Zayn Capital led the $2.1M pre-seed of the Karachi B2B raw-materials marketplace in "
                  "April 2022 (Dawn), Tiger's first pre-seed in Pakistan."))

# 86 Zenoti
mf = PU("zenoti", "Mena FN")
L.append(cls("zenoti", status="private", rng="1b_plus", usd=1_500_000_000, val_src="web_verified",
             val_cite=SIB("zenoti", "accel"), asof="2021-06", extra=WV, flags=["stale"],
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=mf, stage_conf="high", entry_date="2019-04",
             rounds=[rnd("2019-04", "Series C", 50_000_000, "Tiger Global Management", True, mf, "press"),
                     rnd("2021-06", "funding at about $1.5B", 80_000_000, None, None, SIB("zenoti", "accel"), "press")],
             city="Bellevue", focus="SaaS",
             note="Tiger led the $50M Series C in April 2019 (Mena FN; GeekWire), its first round. Mark: the 2021 "
                  "$80M round at about $1.5B, as on Accel's row, stale."))

# 87 Zepto
L.append(verdict("zepto", "not_member",
                 "The seed headlines report Tiger Global conducting due diligence and 'looking for a stake' in Zepto "
                 "(September 2024); no report of a completed Tiger investment was found (a Bing News query for Zepto "
                 "with Tiger Global, 2026-09-29): no record ties the firm to a round.",
                 ec="web", conf="medium", cite=PU("zepto", "Inc42", "recall")))

# 88 Zhaopin
L.append(verdict("zhaopin-ltd", "not_member",
                 T3 + ". Zhaopin listed on the NYSE in June 2014; Tiger's 13G filings run from 2014 and its 13F "
                 "lines from 2014-06-30.",
                 ec="fund_filing", conf="high", cite=SEC("zhaopin-ltd", "edgar")))

# 89 Zillow
L.append(verdict("zillow-group-inc", "not_member",
                 T3 + ". Zillow listed in July 2011; Tiger's 13F carries it from 2012-12-31 and the 2014 merger "
                 "proxy's holder table cites its 13G on listed Class A shares.",
                 ec="fund_filing", conf="high", cite=SEC("zillow-group-inc", "edgar")))

# 90 Zinier
zv = PU("zinier", "Automation startup Zinier snags Series C")
L.append(cls("zinier", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=zv, stage_conf="high", entry_date="2020-01",
             rounds=[rnd("2020-01", "Series C", 90_000_000, "ICONIQ Capital", True, zv, "press")],
             country="US", city="San Mateo", focus="SaaS",
             note="Tiger joined the $90M Series C led by ICONIQ in January 2020 (VCCircle), its first round. Agrees "
                  "with the Accel and ICONIQ rows."))

if __name__ == "__main__":
    jl.write("batch-014c", L)
