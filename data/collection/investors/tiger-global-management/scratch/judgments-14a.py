#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 14, chunk a (rows 1-15). Run: NQ_TAG=b14 python3 judgments-14a.py"""
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

# 46 UrbanClap (same company as urban-company, classified identically)
bl = PU("urbanclap", "Business Line")
wuc = W("Urban Company")
L.append(cls("urbanclap", status="public", rng="1b_plus", usd=2_590_091_430, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/nse/URBANCO/market-cap/", asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=bl, stage_conf="high", entry_date="2019-08",
             rounds=[rnd("2019-08", "Series E", 75_000_000, "Tiger Global", True, bl, "press"),
                     rnd("2021-06", "Series F", 255_000_000, "Prosus Ventures, Dragoneer and Wellington", True, wuc, "press")],
             country="IN", country_src="web_verified", country_cite=wuc, city="Gurugram",
             focus="Consumer & Marketplaces",
             note="UrbanClap renamed itself Urban Company in 2020 and listed on the NSE and BSE in September 2025. "
                  "Market cap INR 248.61B @ ECB 2026-09-29 (INR/EUR 108.991, EUR/USD 1.1355) = $2.59B "
                  "(stockanalysis.com). Tiger led the $75M Series E in August 2019 (Business Line), its first "
                  "round. Rows urbanclap and urban-company are one company."))

# 47 UrbanPiper
a = PU("urbanpiper", "Tiger Global, Sequoia lead Series A")
L.append(cls("urbanpiper", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=a, stage_conf="high", entry_date="2019-10",
             rounds=[rnd("2019-10", "Series A", 7_500_000, "Tiger Global and Sequoia", True, a, "press"),
                     rnd("2022-04", "Series B", 24_000_000, "Sequoia and Tiger Global", True,
                         PU("urbanpiper", "Indiatimes"), "press")],
             country="IN", country_src="web_verified", country_cite=a, city="Bangalore", focus="SaaS",
             note="Tiger and Sequoia India co-led the $7.5M Series A of the Bengaluru restaurant-software company "
                  "in October 2019 (VCCircle) and the $24M Series B in April 2022."))

# 48 Uxin
u = PU("uxin-ltd", "IPO DRS", "sec")
L.append(verdict("uxin-ltd", "member",
                 "Uxin's 2018 IPO registration statement: 'Tiger Global Affiliated Entities' hold 8.8% as series D, "
                 "E, F and G preferred shares owned by Tiger Global Private Investment Partners VIII and "
                 "affiliates, and Internet Fund II bought series E in March 2015: PIP positions in private rounds.",
                 ec="fund_filing", conf="high", cite=u))
L.append(cls("uxin-ltd", status="public", rng="below_1b", usd=288_170_000, val_src="web_verified",
             val_cite=SIB("uxin-ltd", "coatue"), asof="2026-09-25", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2014",
             rounds=[rnd("2014", "Series D", None, None, True, u, "filing"),
                     rnd("2015-03-13", "Series E", None, None, True, u, "filing")],
             country="CN", country_src="web_verified", country_cite=u, city="Beijing",
             focus="Consumer & Marketplaces",
             note="Tiger's largest block is 5.79M series D preferred, its earliest series, before Internet Fund II's "
                  "series E purchase of 13 March 2015 (DRS), so the entry is the Series D. Nasdaq-listed since "
                  "2018; market cap $288M as on Coatue's row (stockanalysis.com, 2026-09-25)."))

# 49 Vanta
fr = PU("vanta", "Fundrise", "sec")
L.append(verdict("vanta", "member",
                 "Fundrise Innovation Fund's advertisement filed with the SEC (2023) says it invested in Vanta's "
                 "Series B (November 2021) alongside Craft, Sequoia, Y Combinator, Tiger Global and CrowdStrike. "
                 "A third party's statement of a private round; no press account of the round names Tiger "
                 "(Bing and Google News queries 2026-09-29), hence medium.",
                 ec="fund_filing", conf="medium", cite=fr))
L.append(cls("vanta", status="private", rng="1b_plus", usd=4_150_000_000, val_src="web_verified",
             val_cite=SIB("vanta", "sequoia-capital"), asof="2025-07-23", extra=WV,
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=fr, stage_conf="medium", entry_date="2021-11",
             rounds=[rnd("2021-11", "Series B", None, None, True, fr, "filing"),
                     rnd("2025-07-23", "Series D at $4.15B", 150_000_000, None, None, SIB("vanta", "sequoia-capital"), "press")],
             country="US", city="San Francisco", focus="Security",
             note="Tiger's entry is the Series B of November 2021 per Fundrise's filing; the earlier Series A was "
                  "Sequoia's. Mark: the July 2025 round at $4.15B (CNBC), as on the Sequoia and YC rows. Focus "
                  "Security: Vanta sells security-compliance automation (the siblings read SaaS)."))

# 50 Vecmocon
ev = PU("vecmocon-technologies", "EVreporter")
L.append(cls("vecmocon-technologies", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=ev, stage_conf="medium", entry_date="2022-10",
             rounds=[rnd("2022-10", "Pre-Series A", 5_200_000, "Tiger Global and Blume Ventures", True, ev, "press")],
             country="IN", country_src="web_verified", country_cite=ev, city="New Delhi", focus="Climate & Energy",
             note="Tiger and Blume led Vecmocon's $5.2M Pre-Series A in October 2022 (EVreporter: 'New-Delhi "
                  "headquartered'); a round before the Series A reads Seed. Graduation left for the graduation "
                  "pass."))

# 51 Vecna Robotics
wv = W("Vecna Robotics")
L.append(cls("vecna-robotics", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=wv, stage_conf="high", entry_date="2022-01",
             rounds=[rnd("2022-01", "Series C", 65_000_000, "Tiger Global", True, wv, "press")],
             country="US", city="Waltham", focus="Industrial & Robotics",
             note="Tiger led the Series C of January 2022 (Wikipedia; The Robot Report: $65M). Later raises "
                  "($14.5M in 2024, $31M in 2026) came at no reported $1B mark. Waltham per Wikipedia."))

# 52 Vedantu
wd = W("Vedantu")
L.append(cls("vedantu", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=wd, stage_conf="high", entry_date="2015-05",
             rounds=[rnd("2015-05", "Series A", 5_000_000, None, True, wd, "press"),
                     rnd("2019-08", "Series C", 42_000_000, "Tiger Global and WestBridge", True,
                         PU("vedantu", "inc42"), "press")],
             country="IN", country_src="web_verified", country_cite=PU("vedantu", "Business Line"), city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Accel and Tiger funded Vedantu's Series A (May 2015, $5M; Wikipedia, Business Line); Tiger later "
                  "led the $42M Series C (2019). Below $1B as on the Accel and Coatue rows: after the 2021 $1B "
                  "round Vedantu raised small rounds at lower prices."))

# 53 Veho
nd = PU("veho", "Nasdaq")
L.append(cls("veho", status="private", rng="1b_plus", usd=1_500_000_000, val_src="web_verified", val_cite=nd,
             asof="2022-02-14", extra=WV, flags=["stale", "model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=nd, stage_conf="high", entry_date="2022-02",
             rounds=[rnd("2022-02", "Series B", 170_000_000, "Tiger Global and SoftBank Vision Fund 2", True, nd, "press")],
             country="US", country_src="web_verified", country_cite=W("Veho Tech"), city="New York",
             focus="Consumer & Marketplaces",
             note="Tiger led the $170M Series B at $1.5B in February 2022 (Reuters via Nasdaq), two months after the "
                  "Series A it was not in. Mark stale; 2024 job cuts but no priced down round found. Veho is a US "
                  "delivery company (Wikipedia: based in New York); the LV country came from a Wikidata join on "
                  "the one-word name (disputed)."))

# 54 Veriff
rt = PU("veriff", "Reuters")
L.append(cls("veriff", status="private", rng="1b_plus", usd=1_500_000_000, val_src="web_verified", val_cite=rt,
             asof="2022-01-26", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=rt, stage_conf="high", entry_date="2022-01",
             rounds=[rnd("2022-01", "Series C", 100_000_000, "Tiger Global and Alkeon", True, rt, "press")],
             country="EE", country_src="web_verified", country_cite=rt, city="Tallinn", focus="Security",
             note="Tiger and Alkeon co-led the $100M Series C at $1.5B in January 2022 (Reuters); no earlier round "
                  "names Tiger. Mark stale, as on the Accel and IVP rows."))

# 55 Vestiaire Collective
gq = PU("vestiaire-collective", "Green Queen")
L.append(cls("vestiaire-collective", status="private", rng="1b_plus", usd=1_195_920_000, val_src="web_verified",
             val_cite=SIB("vestiaire-collective", "balderton-capital"), asof="2024-01-23", extra=WV, flags=["stale"],
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=gq, stage_conf="high", entry_date="2021-03",
             rounds=[rnd("2021-03", "funding", 216_000_000, "Kering and Tiger Global", True, gq, "press")],
             country="FR", country_src="web_verified", country_cite=gq, city="Paris",
             focus="Consumer & Marketplaces",
             note="Kering and Tiger Global backed the EUR 178M ($216M) round of March 2021 that made Vestiaire a "
                  "unicorn (Green Queen); Tiger's first round. Mark: the January 2024 community round's valuation "
                  "as on Balderton's row (PYMNTS), stale."))

# 56 Vipshop
L.append(verdict("vipshop-holdings-ltd", "not_member",
                 T3 + ". Vipshop listed on the NYSE in March 2012; Tiger's 13G filings (2015 to 2017) and the 2015 "
                 "20-F holder table show listed ADSs held by the public-desk funds.",
                 ec="fund_filing", conf="high", cite=SEC("vipshop-holdings-ltd", "edgar")))

# 57 Viz.ai
pl = PU("viz-ai", "Pulse 2.0")
L.append(verdict("viz-ai", "member",
                 "Pulse 2.0 (2022-04-11): Viz.ai's $100M Series D 'was led by Tiger Global and Insight Partners', "
                 "with a statement from John Curtius, partner at Tiger Global.",
                 ec="web", conf="high", cite=pl))
L.append(cls("viz-ai", status="private", rng="1b_plus", usd=1_200_000_000, val_src="web_verified", val_cite=pl,
             asof="2022-04-11", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=pl, stage_conf="high", entry_date="2022-04",
             rounds=[rnd("2022-04", "Series D", 100_000_000, "Tiger Global and Insight Partners", True, pl, "press")],
             city="San Francisco", focus="Healthcare & Bio",
             note="Tiger co-led the $100M Series D at $1.2B in April 2022; mark stale, as on Insight's row."))

# 58 Vostu
vb = PU("vostu", "VentureBeat")
L.append(cls("vostu", status="defunct", rng="below_1b", stage="undetermined",
             rounds=[rnd("2010-11", "funding", 30_000_000, "Accel and Tiger Global", True, vb, "press"),
                     rnd("2012-08", "funding", None, None, True, PU("vostu", "thenextweb.com"), "press")],
             country="BR", country_src="web_verified", country_cite=vb, city="São Paulo",
             focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
             note="Accel and Tiger put $30M into the Brazil-focused social game maker in November 2010 "
                  "(VentureBeat); the round is not named, so the stage is undetermined. Tiger returned in the "
                  "August 2012 round with Intel Capital and General Catalyst. Defunct, as on General Catalyst's "
                  "row; São Paulo, BR aligned with that row (GamesIndustry in 2010 called it New York based); the "
                  "AR country from Wikidata is disputed."))

# 59 VTEX
f1 = PU("vtex", "IPO F-1", "sec")
L.append(verdict("vtex", "member",
                 "VTEX's 2021 F-1: common shares held by Tiger Global Private Investment Partners XII and other "
                 "Tiger affiliates before the July 2021 IPO, listed among its 5% shareholders: a PIP vehicle's "
                 "private position.",
                 ec="fund_filing", conf="high", cite=f1))
L.append(cls("vtex", status="public", rng="below_1b", usd=594_370_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/vtex/market-cap/", asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-09",
             rounds=[rnd("2020-09", "funding that made VTEX a unicorn (reported with Tiger)", None, None, True, None, "press"),
                     rnd("2021-06", "pre-IPO common shares", None, None, True, f1, "filing")],
             city="Rio de Janeiro", focus="SaaS",
             note="NYSE-listed since July 2021; market cap $594M (stockanalysis.com, 2026-09-29). Tiger's PIP XII "
                  "held common shares before the IPO; its round is the September 2020 funding that valued VTEX at "
                  "$1.7B (Brazil Journal; the recall lead says co-led with Lone Pine), after the Riverwood and "
                  "SoftBank rounds, so Growth. The parent is a Cayman company; the business is run from Brazil."))

# 60 Walton Enterprises
L.append(verdict("walton-enterprises", "not_member",
                 "Walton Enterprises is the Walton family's holding company; Wikipedia says its trusts held stakes "
                 "in hedge funds run by Tiger Global, an investment in the firm's funds, not a Tiger investment in "
                 "the company (T2, T5).",
                 ec="web", conf="high", cite=W("Walton Enterprises")))

if __name__ == "__main__":
    jl.write("batch-014a", L)
