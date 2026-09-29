#!/usr/bin/env python3
"""PRO-167 Tiger Global, verify-gap fix b (2026-09-29): cited entry stage for the other 10 of the 21 $1B+ rows in
fix-stage.json (waymo .. stoneco-ltd). Corrections: BigID entered on the Series C extension, Meesho in January
2025; Shein and StoneCo carry `cite_pending` (no page names Tiger's round).
Run: NQ_TAG=fx python3 fixb.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402
from judge_lib import cls, rnd  # noqa: E402
from fxlib import SRC, BURL, OLD  # noqa: E402

L = []

# ---------------------------------------------------------------- Waymo: the additional investor of June 2021
u = SRC("waymo-tc")
L.append(cls("waymo", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2021-06-16",
             rounds=[OLD("waymo", "external round")],
             note="Verify fix 2026-09-29: TechCrunch (2021-06-16) lists the $2.5B round's existing investors 'and "
                  "additional investor Tiger Global', so the June 2021 round is Tiger's entry: Growth, web_verified."))

# ---------------------------------------------------------------- Airbnb: a co-lead of the 2015 round
u = SRC("airbnb-vox")
old = OLD("airbnb", "Series E")
old.update(lead="General Atlantic, Hillhouse and Tiger Global", source=u)
L.append(cls("airbnb", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2015-06",
             rounds=[old],
             note="Verify fix 2026-09-29: Vox (2015-12-07, on the SEC filing that confirmed the round): the $1.5B round "
                  "at $25.5B had as lead investors 'reportedly General Atlantic, Hillhouse Capital Group and Tiger "
                  "Global Management'; it closed in mid-2015 (the Series E) and no earlier Airbnb round names Tiger: "
                  "Growth, web_verified."))

# ---------------------------------------------------------------- Ather Energy: Series A, per the DRHP
u = SRC("ather-entrackr")
L.append(cls("ather-energy", stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2015-05",
             rounds=[rnd("2014-12", "Seed", 1_000_000, "Sachin Bansal, Binny Bansal and Raju Venkatraman", False,
                         SRC("ather-mint-2015")),
                     rnd("2015-05", "Series A", 12_000_000, "Tiger Global", True, u)],
             note="Verify fix 2026-09-29: Entrackr (2025-11-07), reading the DRHP: Tiger 'first backed' Ather in 2015 "
                  "'during the Series A round', Rs 75.23 crore for 74,732 Series A preference shares, and joined no "
                  "later round. That is the $12M of May 2015 (Mint), after the founders' $1M seed from the Bansals and "
                  "Raju Venkatraman: Series A, web_verified."))

# ---------------------------------------------------------------- BigID: the Series C extension
u = BURL("bigid", "BigID bags another $50M round", "yahoo")
L.append(cls("bigid", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2020-01-06",
             rounds=[rnd("2019-09-04", "Series C", 50_000_000, "Bessemer Venture Partners", None,
                         BURL("bigid", "BigID Adds $50 Million in Series C", "dbta")),
                     rnd("2020-01-06", "Series C extension", 50_000_000, "Tiger Global", True, u),
                     OLD("bigid", "Series D"),
                     rnd("2021-04-22", "Series D extension", 30_000_000, None, None,
                         BURL("bigid", "With $30M extension, BigID boosts Series D", "yahoo"))],
             note="Verify fix 2026-09-29: correction of the round. TechCrunch via Yahoo (2020-01-06): four months after "
                  "BigID's $50M Series C (September 2019, led by Bessemer), 'The Series C extension came entirely "
                  "from Tiger Global Management'. Tiger's entry is that extension, not the Series C itself: Growth, "
                  "web_verified."))

# ---------------------------------------------------------------- Grab: led GrabTaxi's third round
u = SRC("grab-rappler")
L.append(cls("grab", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2014-10",
             rounds=[rnd("2014-10", "Series C (third round)", None, "Tiger Global", True, u),
                     OLD("grab", "SoftBank round")],
             note="Verify fix 2026-09-29: Rappler (2014-10-23): 'Leading its third round of funding is US-based "
                  "investment firm Tiger Global, with Hillhouse Capital Management joining current investors GGV, "
                  "Qunar, and Vertex Ventures' (CNET 2014-10-21 the same). Tiger was not among the existing "
                  "investors, so GrabTaxi's Series C of October 2014 is its entry: Growth, web_verified."))

# ---------------------------------------------------------------- Innovaccer: Series C, February 2020
u = BURL("innovaccer", "raises $70M in Series C round from Steadview", "yourstory")
L.append(cls("innovaccer", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2020-02-13",
             rounds=[rnd("2020-02-13", "Series C", 70_000_000, None, True, u),
                     OLD("innovaccer", "Series D"), OLD("innovaccer", "Series E"), OLD("innovaccer", "Series F")],
             note="Verify fix 2026-09-29: YourStory (2020-02-13): 'Healthtech startup Innovaccer raises $70M in Series "
                  "C round from Steadview Capital, Tiger Global, others' (Mint and MobiHealthNews the same). Tiger was "
                  "in talks from August 2019 (VCCircle) and no earlier round names it: Growth, web_verified."))

# ---------------------------------------------------------------- Kong: led the Series D
u = SRC("kong-series-d")
old = OLD("kong", "Series D")
old.update(source=u)
L.append(cls("kong", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2021-02-08",
             rounds=[old, OLD("kong", "Series E")],
             note="Verify fix 2026-09-29: Kong's own release (2021-02-08): it 'closed $100 million in Series D funding, "
                  "led by Tiger Global Management with participation from existing investors Index Ventures, CRV, GGV "
                  "Capital and Andreessen Horowitz', at a $1.4B valuation. Tiger is not among the existing investors, "
                  "so the Series D is its entry: Growth, web_verified."))

# ---------------------------------------------------------------- Meesho: correction, joined the cap table Jan 2025
u = SRC("meesho-inc42-2025")
old = OLD("meesho", "techcrunch")
old.update(round="first close of the 2024-25 round", firm_in_round=False)
L.append(cls("meesho", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2025-01",
             rounds=[old,
                     rnd("2025-01", "second close of the same round (mostly secondary shares)", None, None, True, u)],
             note="Verify fix 2026-09-29: correction of the entry date. Inc42 (2025-01-27, citing ET): Meesho 'has "
                  "reportedly closed another $250-270 Mn in a funding with new investors joining the captable, "
                  "including Tiger Global, Think Investments, Mars Growth Capital, majority of which is in secondary', "
                  "the second close of the round that opened with $275M in May 2024. Tiger's March 2024 commitment was "
                  "a report (Moneycontrol); it joined the cap table in January 2025. Growth, web_verified."))

# ---------------------------------------------------------------- Shein: no page names Tiger's round
L.append(cls("shein", flags=("cite_pending",),
             note="Verify fix 2026-09-29: cite pending. Shein's Hong Kong listing papers name entities linked to Tiger "
                  "Global among the pre-IPO investors it compensates for buying in at higher valuations (The Straits "
                  "Times, 2026-08-24), but no page read names the round in which Tiger first invested (Bing News and "
                  "Google News, 2026-09-29). The stage stays Growth from the record (model)."))

# ---------------------------------------------------------------- StoneCo: no page names Tiger's round
L.append(cls("stoneco-ltd", flags=("cite_pending",),
             note="Verify fix 2026-09-29: cite pending. The October 2018 F-1 names 'Tiger Global Investors' (PIP IX and "
                  "an affiliate) as a 5% holder of common shares before the IPO, but neither the F-1 nor the press "
                  "(Google News and one web search, 2026-09-29) names the round or the date of Tiger's purchase. The "
                  "stage stays Growth from the record (model)."))

if __name__ == "__main__":
    jl.write("fix-b", L)
