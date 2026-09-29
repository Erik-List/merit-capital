#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 14, chunk b (rows 16-30). Run: NQ_TAG=b14 python3 judgments-14b.py"""
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
_CLS = json.loads((HERE.parent / "companies" / "classification.json").read_text())

# 61 Wasoko
ys = PU("wasoko", "finance.yahoo.com/news/sokowatch")
L.append(cls("wasoko", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=ys, stage_conf="high", entry_date="2022-03",
             rounds=[rnd("2022-03", "Series B", 125_000_000, "Tiger Global", True, ys, "press")],
             country="KE", country_src="web_verified", country_cite=PU("wasoko", "yahoo.com/news/two-africas"),
             city="Nairobi", focus="Consumer & Marketplaces",
             note="Tiger led the $125M Series B in March 2022, when Sokowatch renamed itself Wasoko (TechCrunch). "
                  "Wasoko and Cairo's MaxAB completed an all-stock merger in August 2024 (TechCrunch: "
                  + NEWS("wasoko", "Wasoko and MaxAB complete merger: Interview") + "): read acquired with the successor "
                  "noted; the base also carries a maxab row. The 2024 markdown to $260M preceded the merger."))

# 62 WATI
nq = PU("wati", "Nasdaq")
L.append(cls("wati", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=nq, stage_conf="high", entry_date="2022-10",
             rounds=[rnd("2022-10", "Series B", 23_000_000, "Tiger Global", True, nq, "press")],
             country="HK", country_src="web_verified", country_cite=PU("wati", "scmp.com"), city="Hong Kong",
             focus="SaaS",
             note="Tiger led WATI's $23M Series B in October 2022 (TechCrunch; the company's release via Nasdaq); "
                  "no earlier round names Tiger. SCMP: 'Hong Kong SaaS start-up'."))

# 63 Way
pr = NEWS("way", "Way Takes Brand Activations")
L.append(cls("way", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=pr, stage_conf="high", entry_date="2022-11",
             rounds=[rnd("2022-11", "Series A", 20_000_000, "Tiger Global", True, pr, "company")],
             country="US", city="Austin", city_src="web_verified", focus="SaaS",
             note="Tiger led Way's $20M Series A at a $100M valuation (November 2022; the company's release, "
                  "datelined Austin, Texas and Paris)."))

# 64 Wealthfront
bb = NEWS("wealthfront-corp", "Wealthfront Raises $75 Million Led by Tiger")
L.append(verdict("wealthfront-corp", "member",
                 "Wealthfront's 2025 IPO registration statement: Tiger Global Private Investment Partners X and LFX "
                 "Capital ('Tiger Investors') sign the investors' rights agreement and Tiger affiliates hold more "
                 "than 5% (19.57% before the December 2025 IPO); Bloomberg (2018): 'Wealthfront Raises $75 "
                 "Million Led by Tiger Global Management'.",
                 ec="fund_filing", conf="high", cite=PU("wealthfront-corp", "PIP X and LFX Capital", "sec")))
L.append(cls("wealthfront-corp", rng="1b_plus", usd=1_570_000_000, val_src="web_verified",
             val_cite=SIB("wealthfront-corp", "ribbit-capital"), asof="2026-09-28", extra=WV,
             clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=bb, stage_conf="high", entry_date="2018-01",
             rounds=[rnd("2018-01", "funding", 75_000_000, "Tiger Global Management", True, bb, "press")],
             country="US", city="Palo Alto", focus="Fintech & Payments",
             note="Tiger led the $75M round of January 2018 (Bloomberg), after Wealthfront's lettered rounds of "
                  "2011 to 2014, so Growth. Nasdaq-listed since December 2025; market cap $1.57B as on Ribbit's "
                  "row (stockanalysis.com, 2026-09-28); the $0 pre-listing float is not a value."))

# 65 Weave
wd = PU("weave-communications-inc", "IPO DRS", "recall")
L.append(verdict("weave-communications-inc", "member",
                 "Weave's 2021 IPO registration statement: entities affiliated with Tiger Global Private Investment "
                 "Partners XI bought Series D preferred (about $65M), and PIP XI is an Investor with a board "
                 "observer right in the investors' rights agreement made with the Series D purchase on 18 October "
                 "2019: a PIP vehicle in a private round.",
                 ec="fund_filing", conf="high", cite=wd))
L.append(cls("weave-communications-inc",
             stage="Growth", stage_src="web_verified", stage_cite=wd, stage_conf="high", entry_date="2019-10-18",
             rounds=[rnd("2019-10-18", "Series D", 65_000_000, None, True, wd, "filing")],
             country="US", city="Lehi", focus="Healthcare & Bio",
             note="Tiger entered at the Series D of October 2019 (IPO DRS). Weave sells communications software to "
                  "dental, optometry and veterinary practices: healthcare vertical software. NYSE-listed since "
                  "November 2021, below $1B."))

# 66 Weavr
bi = PU("weavr", "Business Insider")
L.append(cls("weavr", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=bi, stage_conf="high", entry_date="2022-02",
             rounds=[rnd("2022-02", "Series A", 40_000_000, "Tiger Global", True, bi, "press")],
             country="GB", country_src="web_verified", country_cite=PU("weavr", "Business Wire"), city="London",
             focus="Fintech & Payments",
             note="Tiger led the $40M Series A of the London embedded-finance company in February 2022 (Business "
                  "Insider; Business Wire); Headline's row holds the earlier seed. Momentum check: no later "
                  "priced round in the row's press."))

# 67 Webull (seed stands)
L.append(cls("webull", status="public", rng="1b_plus", usd=3_880_000_000, val_src="web_verified",
             val_cite=SIB("webull", "coatue"), asof="2026-09-25", extra=WV, stage="undetermined",
             rounds=[rnd("2024-12", "pre-merger shareholder (round not named)", None, None, True,
                         PU("webull", "De-SPAC F-4", "sec"), "filing")],
             city="St. Petersburg", focus="Fintech & Payments",
             note="Webull's articles filed with the de-SPAC F-4 define the investor 'Tiger Global' as Internet Fund "
                  "VII Pte. Ltd., a shareholder before the April 2025 listing; the round it bought into is not "
                  "named, so the stage is undetermined. Market cap $3.88B as on Coatue's row (2026-09-25)."))

# 68 Weee!
bz = NEWS("weee", "scores $425M in new funding")
pn = PU("weee", "PR Newswire")
L.append(cls("weee", status="private", rng="1b_plus", usd=4_100_000_000, val_src="web_verified", val_cite=bz,
             asof="2022-02-28", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=pn, stage_conf="high", entry_date="2021-03",
             rounds=[rnd("2021-03", "Series D", 315_000_000, "DST Global", True, pn, "company"),
                     rnd("2022-02", "Series E", 425_000_000, None, None, bz, "press")],
             country="US", city="Fremont", focus="Consumer & Marketplaces",
             note="Tiger joined the $315M Series D led by DST Global in March 2021 (PR Newswire), its first round. "
                  "Mark: the February 2022 $425M round at $4.1B (Silicon Valley Business Journal), stale; the "
                  "same figure as Lightspeed's row, which cites a vendor page (Sacra) for it."))

# 69 Wego
ww = W("Wego.com")
L.append(verdict("wego", "member",
                 "Wikipedia (Wego.com): Tiger Global Management put $13M into Wego's Series B in December 2010 and "
                 "joined the Series C (2013) and Series D (2015). The seed cited a HolidayIQ headline, a different "
                 "company; this line replaces that citation.",
                 ec="web", conf="high", cite=ww))
L.append(cls("wego", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=ww, stage_conf="high", entry_date="2010-12",
             rounds=[rnd("2008-01", "Series A", 4_500_000, "News Digital Media", False, ww, "press"),
                     rnd("2010-12", "Series B", 13_000_000, "Tiger Global Management", True, ww, "press"),
                     rnd("2013-06", "Series C", 17_000_000, None, True, ww, "press"),
                     rnd("2015-10", "Series D", 11_000_000, None, True, ww, "press"),
                     rnd("2017-08", "Series E", 12_000_000, "MBC", False, ww, "press")],
             country="AE", country_src="web_verified", country_cite=ww, city="Dubai",
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             note="Travel marketplace headquartered in Singapore and Dubai (Wikipedia); its main market and "
                  "leadership are in Dubai. The JP country came from a Wikidata join on the one-word name "
                  "(disputed)."))

# 70 WIZ.AI
bt = PU("wiz-ai", "The Business Times")
L.append(cls("wiz-ai", status="private", rng="below_1b",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2022-06",
             rounds=[rnd("2022-06", "funding (round not named)", 30_000_000, "Tiger Global", True, bt, "press"),
                     rnd("2025-11", "Series B", None, "SMBC Asia Rising Fund", None,
                         BING("wiz-ai", "Raises Tens of Millions in Series B", "Yahoo Finance"), "company")],
             country="SG", country_src="web_verified", country_cite=bt, city="Singapore", focus="AI & Applied AI",
             note="Tiger led the $30M round of June 2022 (The Business Times); the company's own release names its "
                  "November 2025 round the Series B, so the 2022 round reads Series A. Momentum check: the 2025 "
                  "Series B raised 'tens of millions' with no $1B mark."))

# 71 Wiz Freight
en = PU("wiz-freight", "entrackr.com/2022/03")
L.append(cls("wiz-freight", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=en, stage_conf="high", entry_date="2022-03",
             rounds=[rnd("2022-03", "Series A", 36_000_000, "Tiger Global", True, en, "press"),
                     rnd("2024-01", "Series B (extended)", None, None, None, None, "press")],
             country="IN", country_src="web_verified", country_cite=en, city="Chennai",
             focus="Industrial & Robotics",
             note="Tiger led the $36M Series A in March 2022 (Entrackr; YourStory and STAT Times name the Series A). "
                  "The 2024 extended Series B valued the company at Rs 1,400 crore (New Indian Express), well "
                  "below $1B. Freight forwarding reads Industrial & Robotics, as Flexport does in the a16z and GV "
                  "books."))

# 72 WNS
L.append(verdict("wns-holdings-ltd", "not_member",
                 T3 + ". WNS listed on the NYSE in July 2006; its 2007 20-F holder table cites Tiger's 13G filed "
                 "in September 2006, after the IPO.",
                 ec="fund_filing", conf="high", cite=SEC("wns-holdings-ltd", "edgar")))

# 73 Wolt
wb = NEWS("wolt", "Wolt Gets $530 Million")
L.append(cls("wolt", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=wb, stage_conf="high", entry_date="2021-01",
             rounds=[rnd("2021-01", "funding", 530_000_000, "ICONIQ Capital and Tiger Global", True, wb, "press")],
             country="FI", country_src="web_verified", country_cite=W("Wolt"), city="Helsinki",
             focus="Consumer & Marketplaces",
             note="Tiger's entry is the $530M round of January 2021 (Bloomberg via Yahoo, found by a Tiger Global "
                  "and ICONIQ query; Wikipedia lists Tiger among Wolt's investors). Acquired by DoorDash in 2022 "
                  "(status known)."))

# 74 WordPress (Automattic, the same company as the automattic row)
ph = PU("wordpress", "PE Hub")
L.append(cls("wordpress", status="private", rng="1b_plus", usd=7_500_000_000, val_src="web_verified",
             val_cite=_CLS["automattic"]["valuation_citation"], asof="2021-08-16", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=ph, stage_conf="high", entry_date="2013-05",
             rounds=[rnd("2013-05-24", "share purchase", 50_000_000, "Tiger Global", True, ph, "press")],
             country="US", city="San Francisco", focus="SaaS",
             note="The investment is in Automattic, WordPress.com's parent: Tiger bought $50M of stock in May 2013 "
                  "(PE Hub; Reuters), a secondary in a private company, Growth (D6). Classified as the automattic "
                  "row is ($7.5B, 2021, stale); rows wordpress and automattic are one company."))

# 75 Workvivo
yw = PU("workvivo", "Yahoo News Australia")
L.append(cls("workvivo", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=yw, stage_conf="high", entry_date="2020-05",
             rounds=[rnd("2020-05", "Series A", 16_000_000, "Tiger Global", True, yw, "press"),
                     rnd("2022-06", "Series B", 22_000_000, "Tiger Global", True, PU("workvivo", "businessinsider.com/workvivo-tiger-global-leads"), "press")],
             country="IE", country_src="web_verified", country_cite=PU("workvivo", "Irish Examiner"), city="Cork",
             focus="SaaS",
             note="Tiger led the $16M Series A (May 2020) and the $22M Series B (June 2022) of the Cork employee "
                  "communications company. Acquired by Zoom in April 2023 (Wikipedia)."))

if __name__ == "__main__":
    jl.write("batch-014b", L)
