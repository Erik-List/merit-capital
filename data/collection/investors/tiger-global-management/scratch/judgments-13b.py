#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 13, chunk b (rows 16-30). Run: NQ_TAG=b13 python3 judgments-13b.py"""
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

# 16 TaxBit (seed stands)
u = PU("taxbit", "Crowdfund Insider")
L.append(cls("taxbit", status="private", rng="1b_plus", usd=1_330_000_000, val_src="web_verified",
             val_cite=SIB("taxbit", "insight-partners"), asof="2021-08", extra=WV, flags=["stale"],
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-03",
             rounds=[rnd("2021-03", "Series A", 100_000_000, "Paradigm and Tiger Global", True, u, "press"),
                     rnd("2021-08", "Series B", 130_000_000, None, None, SIB("taxbit", "insight-partners"), "press")],
             country="US", city="Draper", focus="Fintech & Payments",
             note="Paradigm and Tiger Global co-led the $100M Series A in March 2021 (Crowdfund Insider; PayPal "
                  "Ventures' release names the round the Series A). Mark: the August 2021 $130M Series B at "
                  "$1.33B (PR Newswire), stale; momentum check found no later priced round. Agrees with the "
                  "Insight, IVP and Ribbit rows."))

# 17 Taxdoo
y = PU("taxdoo", "Yahoo News UK")
d = PU("taxdoo", "Taxdoo ist mit Millionen")
L.append(verdict("taxdoo", "member",
                 "TechCrunch via Yahoo (2021-12-16): Taxdoo's $64M round 'is being led by Tiger Global', with a "
                 "statement from John Curtius, partner at Tiger Global; Deutsche Startups names it the Series B.",
                 ec="web", conf="high", cite=y))
L.append(cls("taxdoo", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=d, stage_conf="high", entry_date="2021-12",
             rounds=[rnd("2020-12", "Series A", None, "Accel", False, None, "press"),
                     rnd("2021-12", "Series B", 64_000_000, "Tiger Global", True, y, "press")],
             country="DE", country_src="web_verified", country_cite=d, city="Hamburg", focus="Fintech & Payments",
             note="Tiger led the EUR 57M ($64M) Series B in December 2021; the 2020 Series A (EUR 17M, Accel and "
                  "Visionaries Club) did not include it. Momentum check (Bing News 2026-09-29): no later round "
                  "reported. Agrees with the 20VC and Accel rows (Hamburg, DE)."))

# 18 TCV Acquisition Corp.
L.append(verdict("tcv-acquisition-corp", "not_member",
                 "A listed blank-check company (SPAC) with no operating business (T5); Tiger's 13G filings "
                 "(2021 to 2023) and 13F lines are a public-market holding, no private round (T3, D3).",
                 ec="fund_filing", conf="high", cite=SEC("tcv-acquisition-corp", "edgar")))

# 19 Teladoc
L.append(verdict("teladoc-inc", "not_member",
                 T3 + ". Teladoc listed in July 2015; Tiger's 13G filings (2017 to 2018) and 13F lines "
                 "(2017) come after the listing.",
                 ec="fund_filing", conf="high", cite=SEC("teladoc-inc", "edgar")))

# 20 Telio (Vietnam)
k = NEWS("telio", "Telio raises USD 25 million Series A")
L.append(verdict("telio", "member",
                 "VietNamNet (2021-11-12): Telio's pre-Series B round names Tiger Global among its investors, "
                 "and KrASIA (2019-12-18) reports the $25M Series A 'led by Tiger Global'.",
                 ec="web", conf="high", cite=PU("telio", "VietNamNet")))
L.append(cls("telio", status="defunct", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=k, stage_conf="high", entry_date="2019-12-18",
             rounds=[rnd("2019-12-18", "Series A", 25_000_000, "Tiger Global", True, k, "press"),
                     rnd("2021-11", "pre-Series B", None, "VNG", True, PU("telio", "VietNamNet"), "press")],
             country="VN", country_src="web_verified", country_cite=k, city="Ho Chi Minh City",
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             note="The Vietnamese B2B e-commerce platform Telio (founded 2018), not the Norwegian VoIP company "
                  "of the same name that the Wikidata join supplied (NO, disputed). Tiger led the $25M Series A "
                  "in December 2019 (KrASIA). Defunct: Telio was dissolved in early 2025 (24h: "
                  + PU("telio", "Startup Telio") + ")."))

# 21 Temporal
g25 = PU("temporal", "Tiger Global leads $146M round")
s26 = PU("temporal", "SiliconANGLE")
gw = NEWS("temporal", "Temporal raises $550M, hits $12.55B valuation")
L.append(cls("temporal", status="private", rng="10b_plus", usd=12_550_000_000, val_src="web_verified",
             val_cite=s26, asof="2026-09-14", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=g25, stage_conf="high", entry_date="2025-03",
             rounds=[rnd("2025-03", "Series C (flat valuation)", 146_000_000, "Tiger Global", True, g25, "press"),
                     rnd("2026-02", "Series D", 300_000_000, None, None, SIB("temporal", "a16z"), "press"),
                     rnd("2026-09-14", "Series E", 550_000_000, "Lightspeed", None, s26, "press")],
             country="US", city="Bellevue", city_src="web_verified", focus="DevTools & APIs",
             note="Tiger led the $146M round of March 2025 (GeekWire); no record found puts it in the 2022 "
                  "Series B (the recall lead said so; not evidence). Mark: the September 2026 $550M Series E at "
                  "$12.55B (SiliconANGLE), fresher than the $5B February 2026 mark the a16z, Lightspeed and "
                  "Sequoia rows carry. City: GeekWire's September 2026 report calls it 'Bellevue-based' ("
                  + gw + "); the sibling rows say Seattle."))

# 22 The Viral Fever and 36 TVF: one company (Contagious Online Media Network)
bs = PU("the-viral-fever", "Business Standard")
tv = dict(status="private", rng="below_1b", stage="undetermined",
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
               "and tvf are one company.")
L.append(cls("the-viral-fever", **tv))

# 23 Thumbtack
w = W("Thumbtack (company)")
L.append(cls("thumbtack", status="private", rng="1b_plus", usd=3_200_000_000, val_src="web_verified",
             val_cite=SIB("thumbtack", "sequoia-capital"), asof="2021-06", extra=WV, flags=["stale"],
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=w, stage_conf="high", entry_date="2014-05",
             rounds=[rnd("2014-05", "Series C", 30_000_000, "Sequoia Capital", True, w, "press"),
                     rnd("2021-06", "funding at $3.2B", 275_000_000, None, None, SIB("thumbtack", "sequoia-capital"), "company")],
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             note="Thumbtack raised a $30M Series C from Sequoia and Tiger Global in May 2014 (Wikipedia; Business "
                  "Wire), Tiger's first round in the company. Mark: the company's own release of the $275M "
                  "investment at $3.2B (2021), stale, as on Sequoia's row."))

# 24 Tiendanube (Nuvemshop)
n = NEWS("tiendanube", "Brazil's Nuvemshop raises $500M")
L.append(verdict("tiendanube", "member",
                 "Milenio (2021-08-17): the round was co-led by Insight Partners and Tiger Global Management; "
                 "TechCrunch via Yahoo: 'raised $500 million in a round co-led by Insight Partners and Tiger "
                 "Global Management'.",
                 ec="web", conf="high", cite=PU("tiendanube", "Milenio")))
L.append(cls("tiendanube", status="private", rng="1b_plus", usd=3_100_000_000, val_src="web_verified",
             val_cite=n, asof="2021-08-17", extra=WV, flags=["stale"],
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=n, stage_conf="high", entry_date="2021-08",
             rounds=[rnd("2021-03", "funding", 90_000_000, None, None, n, "press"),
                     rnd("2021-08", "Series E", 500_000_000, "Insight Partners and Tiger Global Management", True, n, "press")],
             country="BR", country_src="web_verified", country_cite=n, city="São Paulo", focus="SaaS",
             note="Tiendanube (Nuvemshop in Brazil) raised $500M at $3.1B in August 2021, co-led by Insight "
                  "Partners and Tiger Global (TechCrunch; Pulse 2.0 names it the Series E); the March 2021 $90M "
                  "round is not recorded with Tiger. Mark stale, no later priced round found. Founded in Buenos "
                  "Aires, the operating company is run from Brazil, its main market (TechCrunch: 'Brazil's "
                  "Nuvemshop')."))

# 25 Tiger Global Management (the firm itself)
L.append(verdict("tiger-global-management", "not_member",
                 "The row is the firm itself, the investment adviser, not a portfolio company (T5); its seed "
                 "headline reports Tiger's own investment in Cerebras Systems, a different company.",
                 ec="web", conf="high", cite=PU("tiger-global-management", "Cerebras", "recall")))

# 26 Toplyne
t = PU("toplyne", "The Free Press Journal")
L.append(cls("toplyne", status="defunct", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=t, stage_conf="high", entry_date="2022-05",
             rounds=[rnd("2022-05", "Series A", 15_000_000, "Tiger Global and Sequoia Capital India", True, t, "press")],
             country="IN", country_src="web_verified", country_cite=PU("toplyne", "Mint |"), city="Bangalore",
             focus="SaaS",
             note="Tiger and Sequoia India co-led the $15M Series A in May 2022. Toplyne shut down in October "
                  "2024 (Entrackr: " + NEWS("toplyne", "shuts down operations") + ")."))

# 27 Torii
bw = PU("torii", "businesswire.com/news/home/20220202005242")
L.append(cls("torii", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=bw, stage_conf="high", entry_date="2022-02",
             rounds=[rnd("2022-02", "Series B", 50_000_000, "Tiger Global", True, bw, "press")],
             country="US", country_src="web_verified", country_cite=bw, city="New York", focus="SaaS",
             flags=["model_disputes_source"],
             note="Tiger led the $50M Series B in February 2022 (Business Wire); no earlier Torii round names the "
                  "firm. Torii is a SaaS-management company run from New York with engineering in Israel; the "
                  "JP country came from a Wikidata join on the one-word name (disputed)."))

# 28 TeachersPayTeachers (TPT Holdco)
L.append(verdict("tpt-holdco-llc", "not_member",
                 "Lee Fixel (Tiger, in tenure) is director on the 2014 Form D filings of TPT Holdco, TPT Investor "
                 "and Teacher Synergy (TeachersPayTeachers), a holding-company structure whose ownership split "
                 "the record does not state; no press, filing or announced round names Tiger Global (a Google "
                 "News query returned only vendor profiles). A board seat and a holdco of unknown split are not a "
                 "verified venture entry (Erik's ruling on BCV, 2026-09-28).",
                 ec="formd_adjudicated", conf="medium", cite=SEC("tpt-holdco-llc")))

# 29 TradingView
fx = PU("tradingview", "FX News Group")
L.append(cls("tradingview", status="private", rng="1b_plus", usd=3_000_000_000, val_src="web_verified",
             val_cite=fx, asof="2021-10-14", extra=WV, flags=["stale", "model_disputes_source"],
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=fx, stage_conf="high", entry_date="2021-10",
             rounds=[rnd("2021-10", "funding", 298_000_000, "Tiger Global", True, fx, "press")],
             country="US", country_src="web_verified", country_cite=W("TradingView"), city="New York",
             focus="Fintech & Payments",
             note="Tiger led the $298M round at $3B in October 2021 (FX News Group), after the 2019 round led by "
                  "DST and Insight; mark stale, no later priced round found. Wikipedia: 'headquartered in New "
                  "York', with its European headquarters in London; the JP country came from a Wikidata join "
                  "(disputed). Insight's row reads London, GB."))

# 30 TransDigm
L.append(verdict("transdigm-group-inc", "not_member",
                 T3 + ". TransDigm listed in March 2006; Tiger's 13G filings (2007 to 2019) and 13F lines "
                 "(2007 to 2021) are a listed holding.",
                 ec="fund_filing", conf="high", cite=SEC("transdigm-group-inc", "edgar")))

if __name__ == "__main__":
    jl.write("batch-013b", L)
