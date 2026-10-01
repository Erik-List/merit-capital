#!/usr/bin/env python3
"""A/B pass ab1b, part 1 (PRO-99 Kleiner Perkins): the private $1B+ rows k2-space .. profound of queue/ab1.json[37:].
Run as: NQ_TAG=ab1b python3 judgments-ab1b1.py
Rows defended with no change (nothing emitted): k2-space, mind-robotics, mirendil, modern-health, nexthop-ai,
parallel, plaid, profound."""
import json

import judge_lib as jl
from judge_lib import cls, verdict, rnd, POST, W, NEWS

WV = "web_verified"
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def R(slug):
    """The row's funding_rounds as stored (a line's list replaces the stored one, so additions start from it)."""
    return list((_CLS.get(slug) or {}).get("funding_rounds") or [])


L = []

# ---- labelbox: the seed is the entry (TechCrunch names KP as lead), graduated on the Series B
TC_LABELBOX = "https://techcrunch.com/2018/07/30/labelbox/"
LB_SERIES_B = "https://labelbox.com/blog/series-b-announcement/"
FORBES_LB = "https://www.forbes.com/sites/kenrickcai/2022/01/06/data-startup-labelbox-series-d-funding-from-softbank/"
L.append(cls("labelbox", stage="Seed", stage_src=WV, stage_cite=TC_LABELBOX, stage_conf="high",
             entry_date="2018-07-30", grad="graduated", grad_src=WV, grad_cite=LB_SERIES_B, grad_conf="high",
             rounds=[rnd("2018-07-30", "Seed", 3900000, "Kleiner Perkins", True, TC_LABELBOX, "press"),
                     rnd("2020-02-04", "Series B", 25000000, "Andreessen Horowitz", True, LB_SERIES_B, "company"),
                     rnd("2022-01-06", "Series D", 110000000, "SoftBank Vision Fund 2", None, FORBES_LB, "press")],
             note="A/B 2026-09-30: TechCrunch (2018-07-30) reports the $3.9M seed 'led by Kleiner Perkins and joined "
                  "by First Round and Gradient Ventures', the firm's 2018 entry, so Seed; the company's own post "
                  "names Kleiner Perkins among the early investors in the $25M Series B of February 2020, so "
                  "graduated. No round after the January 2022 Series D was found, so the $1B mark stands, stale."))

# ---- magic-leap: the unicorn-list $4.5B (2016) yields to the priced October 2021 round at $2B
CNBC_ML = NEWS("magic-leap", "giving company $2 billion valuation - cnbc")
L.append(cls("magic-leap", rng="1b_plus", usd=2000000000, val_src=WV, val_cite=CNBC_ML, asof="2021-10-11",
             stage="Growth", stage_src=WV, stage_cite=W("Magic Leap"), stage_conf="medium",
             flags=["stale"], clear=["unicorn_name_match"],
             rounds=R("magic-leap") + [rnd("2021-10-11", "funding round ($500M at about $2B post-money)", 500000000,
                                          None, None, CNBC_ML, "press")],
             note="A/B 2026-09-30: the unicorn-list $4.5B of 2016 is replaced by the last priced round, $500M at a "
                  "$2B valuation in October 2021 (CNBC), stale. Saudi Arabia's Public Investment Fund took a "
                  "majority stake in the $450M deal of December 2022 and has funded the company since (2024, 2025) "
                  "at no disclosed price; it still operates under its own name, so private. The a16z row still "
                  "carries the uncited $4.5B."))

# ---- mashgin: the entry round is on a vendor page only
L.append(cls("mashgin", flags=["cite_pending"],
             rounds=[rnd("2015-04", "Seed", 3000000, None, True,
                         "https://crunchbase.com/funding_round/mashgin-seed--ff1cea22", "vendor"),
                     rnd("2022-05-09", "Series B", 62500000, "NEA", None,
                         "https://www.prnewswire.com/news-releases/mashgin-raises-62-5m-series-b-funding-at-a-1-5-billion-valuation-led-by-nea-301542339.html",
                         "company")],
             note="A/B 2026-09-30: one try at the entry round found only a vendor page listing KPCB Edge in the "
                  "$3M seed of April 2015 (Crunchbase), which may not be cited, so the stage stays undetermined "
                  "with cite_pending. No round after the May 2022 Series B was found; the $1.5B mark stands, stale."))

# ---- motive: attack found no priced event after the Series F
TNW_MOTIVE = NEWS("motive", "pulls its IPO")
L.append(cls("motive",
             rounds=R("motive") + [rnd("2026-09-10", "growth financing (General Catalyst Customer Value Fund)",
                                      1300000000, "General Catalyst", None, TNW_MOTIVE, "press")],
             note="A/B 2026-09-30: Motive filed publicly for an IPO in December 2025 and withdrew the filing on "
                  "2026-09-10 after more than $1.3B of growth financing from General Catalyst, at no disclosed "
                  "valuation (The Next Web), so it is still private and the 2022 Series F mark stands, stale."))

# ---- netlify: the mark re-pinned to the round's own report, the stage to the firm's post
TC_NETLIFY = "https://techcrunch.com/2021/11/17/netlify-snags-105m-series-d-to-fuel-jamstack-focused-web-development/"
P_NETLIFY = POST("netlify-modernizing-the-web")
L.append(cls("netlify", rng="1b_plus", usd=2000000000, val_src=WV, val_cite=TC_NETLIFY, asof="2021-11-17",
             stage="Growth", stage_src="first_party", stage_cite=P_NETLIFY, stage_conf="high",
             rounds=[rnd("2018-10-09", "Series B", 30000000, "Kleiner Perkins", True, P_NETLIFY, "firm"),
                     rnd("2020-03-04", "Series C", 53000000, "EQT Ventures", True, W("Netlify"), "press"),
                     rnd("2021-11-17", "Series D", 105000000, "Bessemer Venture Partners", True, TC_NETLIFY, "press")],
             note="A/B 2026-09-30: the firm's post 'Welcome Netlify' (2018-10-09) says the $30M Series B was led by "
                  "Kleiner Perkins, its entry, which agrees with the Form D band (Growth). The $2B mark is re-pinned "
                  "from Wikipedia to TechCrunch's report of the Series D (2021-11-17); no later round or sale found."))

# ---- newlimit: the Series A names Kleiner Perkins
FORTUNE_NL = NEWS("newlimit", "raises $40 million for NewLimit")
_nl = [r for r in R("newlimit") if r.get("round") != "Series A"]
L.append(cls("newlimit", stage="Series A", stage_src=WV, stage_cite=FORTUNE_NL, stage_conf="high",
             entry_date="2023-05-16",
             rounds=[rnd("2023-05-16", "Series A", 40000000, None, True, FORTUNE_NL, "press")] + _nl,
             note="A/B 2026-09-30: Fortune (2023-05-16) reports the $40M Series A 'from Kleiner Perkins and other "
                  "venture firms' (Dimension, Founders Fund), which cites the Series A entry; the $3.1B Series C of "
                  "June 2026 is the latest priced round."))

# ---- newsela: the firm entered at the round the press names Series B
EDSURGE = "https://www.edsurge.com/news/2015-10-06-newsela-makes-more-news-with-15m-round-led-by-kleiner-perkins"
EDWEEK = "https://marketbrief.edweek.org/strategy-operations/k-12-dealmaking-newsela-raises-100-million-series-d-round-reaches-unicorn-status/2021/03"
L.append(cls("newsela", stage="Growth", stage_src=WV, stage_cite=EDSURGE, stage_conf="high",
             flags=["stage_disputes_band"],
             rounds=[rnd("2014-09-12", "Form D offering", 5956174, None, False, None, "filing"),
                     rnd("2015-10-06", "Series B", 15000000, "Kleiner Perkins Caufield & Byers", True, EDSURGE, "press"),
                     rnd("2021-02-26", "Series D", 100000000, None, None, EDWEEK, "press")],
             note="A/B 2026-09-30: EdSurge (2015-10-06) reports '$15 million in a Series B round led by Kleiner "
                  "Perkins Caufield & Byers, which contributed $10 million', the round of the 2015 Form D on which "
                  "Brook Byers joins the board, so the entry is Growth, not the band's Series A. No round after "
                  "the 2021 Series D was found; the $1B mark stands, stale."))

# ---- openevidence: the unicorn-list figure re-pinned to the newest priced round
RM_OE = NEWS("openevidence", "OpenEvidence hits $15B valuation as its ambitions")
L.append(cls("openevidence", rng="10b_plus", usd=15000000000, val_src=WV, val_cite=RM_OE, asof="2026-09-24",
             val_conf="medium", clear=["unicorn_name_match"],
             rounds=R("openevidence") + [rnd("2026-09-24", "funding round ($250M at $15B post-money)", 250000000,
                                            "Andreessen Horowitz and hospital systems", None, RM_OE, "press")],
             note="A/B 2026-09-30: the unicorn-list $12B is replaced by the newest priced round, $250M at a $15B "
                  "post-money valuation led by hospital systems and Andreessen Horowitz, reported by Business "
                  "Insider on 2026-09-24 (Refresh Miami, Axios) and not confirmed by the company, so medium "
                  "confidence. The sibling books still carry the $12B of January 2026."))

# ---- persona: R7, the deal Leigh Marie Braswell led at her previous firm
L.append(verdict("persona", "not_member",
                 "Partner-carried (Erik 2026-09-17 partner-carried rule; decisions.md R7): the firm's own post "
                 "welcoming Leigh Marie Braswell (2023-05-24) credits Persona, with Chronosphere and Neon, to the "
                 "investments she led before joining, at Founders Fund, which led Persona's $150M Series C in "
                 "September 2021, the year the site gives; the listing is first archived in 2023 and reads Prior. "
                 "Persona's round history is on record and no round names a Kleiner Perkins fund: Series A "
                 "(Coatue, First Round), Series B (Index), Series C (Founders Fund, with Meritech, Coatue, Bond, "
                 "Index) and the company's Series D release of 2025-04-30 (Founders Fund and Ribbit, with Bond, "
                 "Coatue, First Round, Index, Chemistry).",
                 ec="web", conf="medium", cite=POST("welcoming-leigh-marie-braswell")))

# ---- pilot: R7, the Index-led Series A Ilya Fushman made before joining
L.append(verdict("pilot", "not_member",
                 "Partner-carried (Erik 2026-09-17 partner-carried rule; decisions.md R7): the one Kleiner Perkins "
                 "trace is Ilya Fushman as a director on Pilot's Form D of the Series A (first sale 2018-02-28), "
                 "when he was a general partner at Index Ventures; Index's own post of 2018-03-14 announces the "
                 "$15M Series A as led by Index, he moved to Kleiner Perkins that month, and he is on none of "
                 "Pilot's later Form Ds. Pilot's round history is on record and no round names a Kleiner Perkins "
                 "fund: Series B (Stripe and Index, TechCrunch 2019-04-18), Series C (Sequoia) and its extension "
                 "(Bezos Expeditions, Whale Rock; TechCrunch 2021-04-14). The site lists it as Prior with the year "
                 "2018 and it never appears in the archived listings.",
                 ec="web", conf="medium",
                 cite="https://www.indexventures.com/perspectives/rebooting-bookkeeping-for-the-modern-business/"))

# ---- productboard: the unicorn-list figure re-pinned to the company's Series D post; the Series A cited
PB_A = "https://www.productboard.com/blog/behind-our-series-a/"
PB_D = "https://www.productboard.com/blog/series-d-announcement/"
PULSE_PB = NEWS("productboard", "Productboard Raises $10 Million")
L.append(cls("productboard", rng="1b_plus", usd=1725000000, val_src=WV, val_cite=PB_D, asof="2022-02-01",
             stage="Series A", stage_src=WV, stage_cite=PB_A, stage_conf="high", entry_date="2018-07-11",
             flags=["stale"], clear=["unicorn_name_match"],
             rounds=[rnd("2018-07-11", "Series A", 8000000, "Kleiner Perkins", True, PB_A, "company"),
                     rnd("2019-02-04", "Series A follow-on", 10000000, "Index Ventures", True, PULSE_PB, "press"),
                     rnd("2022-02-01", "Series D", 125000000, "Dragoneer and Tiger Global", True, PB_D, "company")],
             note="A/B 2026-09-30: the company's own post of 2018-07-11 announces the $8M Series A led by Kleiner "
                  "Perkins, the firm's 2018 entry (Pulse 2.0 names it a previous investor in the Index-led $10M of "
                  "February 2019). The unicorn-list figure is re-pinned to the company's Series D post, $125M at "
                  "$1.725B on 2022-02-01, with Kleiner Perkins participating; no later priced round found, stale."))

jl.write("ab1b1", L)
