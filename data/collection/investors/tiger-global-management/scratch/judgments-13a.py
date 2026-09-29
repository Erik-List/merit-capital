#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 13, chunk a (rows 1-15). Run: NQ_TAG=b13 python3 judgments-13a.py"""
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


L = []
WV = {"valuation_range_source": "web_verified"}
T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"

# 1 StockX
u = PU("stockx", "MilanoFinanza")
v = NEWS("stockx", "UPDATE 1-Sneaker marketplace StockX valued at $3.8 bln")
L.append(verdict("stockx", "member",
                 "MilanoFinanza (2020-12-17) reports StockX's $275M financing with Tiger Global Management; "
                 "PR Newswire titles the round the Series E (December 2020). A private round naming the firm.",
                 ec="web", conf="high", cite=u))
L.append(cls("stockx", status="private", rng="1b_plus", usd=3_800_000_000, val_src="web_verified",
             val_cite=v, asof="2021-04-08", extra=WV, flags=["stale"],
             clear=["needs_web_value", "unicorn_name_match"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2020-12",
             rounds=[rnd("2020-12", "Series E", 275_000_000, None, True, u, "press"),
                     rnd("2021-04", "Series E-1 (primary) with a secondary tender", 60_000_000, None, None, v, "press")],
             country="US", city="Detroit", focus="Consumer & Marketplaces",
             note="Tiger's entry is the December 2020 $275M Series E (MilanoFinanza names Tiger Global with the "
                  "financing; no earlier StockX round names the firm). Mark: the April 2021 Series E-1 primary "
                  "with a tender valued StockX at $3.8B (Reuters); no later priced round or collapse evidence "
                  "found, so the mark stands, stale. Agrees with Battery's row."))

# 2 StoneCo
u = FTS("StoneCo", "DLP Payments")
L.append(verdict("stoneco-ltd", "member",
                 "StoneCo's July 2018 IPO registration statement (filed as DLP Payments Holdings) lists 'Tiger "
                 "Global Investors', common shares held of record by Tiger Global Private Investment Partners IX, "
                 "among its 5% shareholders before the October 2018 IPO: a PIP vehicle's private position, so the "
                 "13G and 13F lines are the same holding after the listing.",
                 ec="fund_filing", conf="high", cite=u))
L.append(cls("stoneco-ltd", status="public", rng="1b_plus", usd=2_130_000_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/stne/market-cap/", asof="2026-09-28", extra=WV,
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2018",
             rounds=[rnd("2018-07", "pre-IPO common shares (round not named)", None, None, True, u, "filing")],
             city="São Paulo", focus="Fintech & Payments",
             note="Public since the October 2018 Nasdaq IPO; market cap $2.13B (stockanalysis.com, read "
                  "2026-09-29). Tiger's PIP IX held common shares before the IPO (DRS, July 2018); the purchase "
                  "round is not named in the record, and a pre-IPO position in a payments processor already at "
                  "scale reads Growth (D12). Entry date is the DRS year, the latest the position can date from."))

# 3 Sumo Logic
u = PU("sumo-logic-inc", "amended investors", "sec")
L.append(verdict("sumo-logic-inc", "member",
                 "Tiger Global Private Investment Partners XI signs Sumo Logic's amended and restated investors' "
                 "rights agreement, made at the Series G closing, as an Investor (exhibit to the 2019 IPO DRS): "
                 "a PIP vehicle in a private round.",
                 ec="fund_filing", conf="high", cite=u))
L.append(cls("sumo-logic-inc", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019",
             rounds=[rnd("2019", "Series G", None, None, True, u, "filing")],
             country="US", city="Redwood City", focus="Data Infrastructure",
             note="The investors' rights agreement is restated 'of even date' with the Series G Preferred Stock "
                  "Purchase Agreement and PIP XI signs it, so Tiger entered at the 2019 Series G. Acquired by "
                  "Francisco Partners in 2022 (status known). Siblings agree on acquired, Redwood City, US."))

# 4 Sunrun
L.append(verdict("sunrun-inc", "not_member",
                 T3 + ". Sunrun listed in August 2015; Tiger's 13F carries it only from 2018-03-31 and its "
                 "13G and Form 3/4 filings run 2018 to 2021, so the holding was bought on the market.",
                 ec="fund_filing", conf="high", cite=SEC("sunrun-inc", "edgar")))

# 5 Super73
L.append(verdict("super73", "not_member",
                 "Two SEC filings carry founder John Kim's director bio: he 'sold his ownership to the investment "
                 "firm Tiger Global' (Volcon FWP, 2021) and Super73 was 'Acquired by Tiger Global in 2019' "
                 "(Empery Digital 8-K exhibit, 2025). That is a purchase of the company, not a minority round "
                 "(COLLECTION.md 1, T3 control positions); no press reports a Tiger round in Super73.",
                 ec="fund_filing", conf="medium", cite=PU("super73", "Volcon director bio", "sec"),
                 exclusion="control_position"))

# 6 SurveyMonkey (seed stands) and 7 SVMK Inc. (the same company)
w = W("SurveyMonkey")
sm_note = ("SurveyMonkey (legal name SVMK Inc., renamed Momentive Global in 2021) was taken private by STG in "
           "2023. Tiger Global Private Investment Partners VI and VII held more than 5% before the 2018 IPO; "
           "Wikipedia names Tiger Global Management in the 2014 $250M equity financing, the earliest round on "
           "record naming the firm (PIP VI's holding may date from an earlier financing). Rows surveymonkey "
           "and svmk-inc are one company.")
sm = dict(rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=w, stage_conf="medium",
          entry_date="2014", rounds=[rnd("2014", "equity financing", 250_000_000, None, True, w, "press")],
          country="US", city="San Mateo", focus="SaaS", note=sm_note)
L.append(cls("surveymonkey", status="acquired", **sm))
L.append(verdict("svmk-inc", "member",
                 "SVMK Inc. (SurveyMonkey) IPO registration statement, 2018: Tiger Global Private Investment "
                 "Partners VI and VII hold more than 5% before the IPO and PIP VII signs the fourth amended "
                 "registration rights agreement: PIP vehicles' private position. Same company as the "
                 "surveymonkey row.",
                 ec="fund_filing", conf="high", cite=PU("surveymonkey", "SVMK IPO DRS", "sec")))
L.append(cls("svmk-inc", **sm))

# 8 Swap (Brazil)
u = PU("swap", "Yahoo Finance")
L.append(cls("swap", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-10",
             rounds=[rnd("2021-10", "Series A", 25_000_000, "Tiger Global", True, u, "press")],
             country="BR", country_src="web_verified", country_cite=u, city="São Paulo",
             focus="Fintech & Payments",
             note="Tiger led the $25M (R$135M) Series A of Swap, the Brazilian banking-as-a-service fintech, in "
                  "October 2021 (TechCrunch via Yahoo; Pequenas Empresas names the Series A). Momentum check: a "
                  "Bing News query for a later Swap round (2026-09-29) found none. Sibling collision: the Cherry "
                  "and ICONIQ rows named Swap are the London company, a different business; not aligned."))

# 9 Swiggy
L.append(verdict("swiggy", "not_member",
                 "The seed headline is about Zomato, a rival ('Zomato raises $103 million from Tiger Global, "
                 "closes in on Swiggy'); the row's other headlines (UrbanPiper's round, a Swiggy vs Zomato "
                 "comparison) name no Tiger investment in Swiggy, and a Bing News query for Swiggy with Tiger "
                 "Global found none: no record ties the firm to a round.",
                 ec="web", conf="medium", cite=PU("swiggy", "HT Tech")))

# 10 Sympoz Inc. (Craftsy)
vox = NEWS("sympoz-inc", "NBCUniversal spent around")
L.append(verdict("sympoz-inc", "member",
                 "Lee Fixel (Tiger partner, in tenure) is director on Sympoz Inc.'s Form D filings of 2012, 2013 "
                 "and 2014 (Craftsy, Denver); Wikipedia names Tiger Global Management among the investors of the "
                 "company's $15M round and Vox (2017) names Tiger Global among Craftsy's early investors.",
                 ec="formd_adjudicated", conf="high", cite=SEC("sympoz-inc")))
L.append(cls("sympoz-inc", status="acquired", rng="below_1b", city="Denver", focus="Consumer & Marketplaces",
             note="Sympoz Inc. is Craftsy. NBCUniversal bought a majority stake in May 2017 for about $230M (Vox: "
                  + vox + "); the business, renamed Bluprint, closed in 2020 and TN Marketing bought its assets. "
                  "The entry stage stays with the Form D band (April 2012 round)."))

# 11 Takealot
L.append(verdict("takealot", "not_member",
                 "Wikipedia (Takealot Group): in October 2010 Kim Reid and Tiger Global Management acquired the "
                 "existing business Take2 and renamed it takealot.com. Tiger with its co-investor bought the whole "
                 "company: a control purchase, not a venture round (COLLECTION.md 1, T3 control positions). "
                 "Naspers took a majority in 2017 and all of it in 2018.",
                 ec="web", conf="high", cite=W("Takealot Group"), exclusion="control_position"))

# 12 Taktile
a = PU("taktile", "Taktile Raises $20 Million Series A")
b = PU("taktile", "Berliner KI-Fintech")
f = NEWS("taktile", "Exclusive: Taktile raises $110 million")
L.append(cls("taktile", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": f, "valuation_asof": "2026-06-24"},
             stage="Series A", stage_src="web_verified", stage_cite=a, stage_conf="high", entry_date="2022-11",
             rounds=[rnd("2022-11", "Series A", 20_000_000, "Index Ventures and Tiger Global", True, a, "press"),
                     rnd("2025-02", "Series B", 54_000_000, None, None, PU("taktile", "Pulse 2.0"), "press"),
                     rnd("2026-06", "Series C", 110_000_000, "Goldman Sachs Alternatives", True, f, "press")],
             country="DE", country_src="web_verified", country_cite=b, city="Berlin", focus="AI & Applied AI",
             note="Tiger co-led the $20M Series A with Index Ventures in November 2022 (Tech.eu, Business Wire). "
                  "Momentum check: the June 2026 $110M Series C led by Goldman Sachs Alternatives, with Tiger, "
                  "was reported without a valuation (Fortune; Bing News 2026-09-29), so below_1b stands. Agrees "
                  "with Balderton's row (Berlin, DE)."))

# 13 TAL Education
u = PU("tal-education-group", "IPO F-1 exhibits", "sec")
L.append(verdict("tal-education-group", "member",
                 "TAL's 2010 F-1 exhibit (the August 2009 share purchase agreement) names Tiger Global Five China "
                 "Holdings, one of Tiger's holding vehicles for Asian positions (D8), among the Existing "
                 "Shareholders before the October 2010 IPO: a private position.",
                 ec="fund_filing", conf="high", cite=u))
L.append(cls("tal-education-group", status="public", rng="1b_plus", usd=6_490_000_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/tal/market-cap/", asof="2026-09-28", extra=WV,
             stage="undetermined",
             rounds=[rnd("2009-08", "share purchase agreement (Tiger already an existing shareholder)", None,
                         None, True, u, "filing")],
             city="Beijing", focus="Consumer & Marketplaces",
             note="NYSE-listed since October 2010; market cap $6.49B (stockanalysis.com, read 2026-09-29). Tiger "
                  "Global Five China Holdings was already a shareholder when the August 2009 agreement was signed; "
                  "the round it entered is not named in the filings read, so the stage is undetermined."))

# 14 Tango (Tango Technology, Inc.)
w = W("Tango (software company)")
L.append(cls("tango", status="private", rng="below_1b",
             extra={"is_public": False, "valuation_source": None, "valuation_range_source": None,
                    "valuation_asof": None},
             flags=["model_disputes_source"],
             stage="Series A", stage_src="web_verified", stage_cite=w, stage_conf="high", entry_date="2022-06",
             rounds=[rnd("2021-08", "Seed", 5_700_000, "Wing Venture Capital", False, w, "press"),
                     rnd("2022-06", "Series A", 14_000_000, "Tiger Global Management", True, w, "press")],
             country="US", city="Los Angeles", city_src="web_verified", focus="SaaS",
             note="Tango Technology, Inc. is a private US software company (Wikipedia); the public status, the "
                  "$58.4B float and NL came from a weak CIK join and a Wikidata name join to other companies "
                  "named Tango, disputed. Tiger led the $14M Series A in June 2022; the August 2021 seed was led "
                  "by Wing. City from the Series A release's dateline (PR Newswire, Los Angeles). General "
                  "Catalyst's 'Tango Technology' row reads unknown; the company still operates (AI service "
                  "launched April 2025)."))

# 15 TaskUs
L.append(verdict("taskus-inc", "not_member",
                 T3 + ". TaskUs listed in June 2021; Tiger's 13G filings (2021 to 2023) and one 13F quarter "
                 "(2021-12-31) show a listed holding only.",
                 ec="fund_filing", conf="high", cite=SEC("taskus-inc", "edgar")))

if __name__ == "__main__":
    jl.write("batch-013a", L)
