#!/usr/bin/env python3
"""A/B pass ab1b, part 2 (PRO-99 Kleiner Perkins): the private $1B+ rows qumulo .. xendit of queue/ab1.json[37:].
Run as: NQ_TAG=ab1b python3 judgments-ab1b2.py
Rows defended with no change (nothing emitted): rogo, saronic-technologies, synthesia, teleport, toss, waymo."""
import json

import judge_lib as jl
from judge_lib import cls, rnd, W, NEWS

WV = "web_verified"
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def R(slug):
    """The row's funding_rounds as stored (a line's list replaces the stored one, so additions start from it)."""
    return list((_CLS.get(slug) or {}).get("funding_rounds") or [])


L = []

# ---- qumulo: the mark re-pinned from Wikipedia to the round's own report
ST_QUMULO = NEWS("qumulo", "valuation hits $1.2 billion")
L.append(cls("qumulo", rng="1b_plus", usd=1200000000, val_src=WV, val_cite=ST_QUMULO, asof="2020-07-16",
             note="A/B 2026-09-30: the $1.2B mark is re-pinned from Wikipedia to The Seattle Times' report of the "
                  "$125M Series E (2020-07-16); layoffs in 2022 and 2023 and a new chief executive in 2024 followed, "
                  "but no later round, sale or tender was found, so it stands, stale."))

# ---- rebellion-defense: the 2019 entry round is on vendor pages only
L.append(cls("rebellion-defense", flags=["cite_pending"],
             rounds=[rnd("2019-04", "Seed", 11360000, "Venrock", None, None, "vendor")] + R("rebellion-defense"),
             note="A/B 2026-09-30: one try at the firm's 2019 entry found only vendor pages (a seed of about $11M in "
                  "April 2019 led by Venrock; none names Kleiner Perkins in it), so the stage stays undetermined "
                  "with cite_pending. Forbes (2023-12-22) reported the company in a nosedive and a new chief "
                  "executive was named that month, but no down round, tender or sale with a figure was found, so "
                  "the 2021 mark stands, stale."))

# ---- rippling: the unicorn-list figure re-pinned to the round's own report
CNBC_RIP = "https://www.cnbc.com/2025/05/09/rippling-valued-at-16point8-billion-in-450-million-funding-round.html"
L.append(cls("rippling", rng="10b_plus", usd=16800000000, val_src=WV, val_cite=CNBC_RIP, asof="2025-05-09",
             clear=["unicorn_name_match"],
             rounds=R("rippling") + [rnd("2025-05-09", "Series G", 450000000, None, None, CNBC_RIP, "press")],
             note="A/B 2026-09-30: the unicorn-list figure is re-pinned to the round itself, the $450M Series G at "
                  "$16.8B (CNBC, 2025-05-09, with a $200M buyback of employee shares), as the Coatue, "
                  "Lightspeed and Y Combinator rows cite it; no later priced round was found."))

# ---- sierra: no source names Kleiner Perkins in a round
L.append(cls("sierra", flags=["cite_pending"],
             note="A/B 2026-09-30: one try at the 2025 entry found no round naming Kleiner Perkins (TechCrunch on "
                  "the September 2025 $350M round names Greenoaks, Sequoia, Benchmark, ICONIQ and Thrive), so the "
                  "Growth stage rests on the firm's listing and its since-year alone and carries cite_pending."))

# ---- stord: the Series A the firm led, cited
HYPE_STORD = NEWS("stord", "Kleiner Perkins-Led Series A")
TC_STORD21 = NEWS("stord", "raises $90M in Kleiner Perkins-led round")
TC_STORD26 = "https://techcrunch.com/2026/05/26/amazon-fulfillment-competitor-stord-raises-250m-at-3b-valuation/"
L.append(cls("stord", stage="Series A", stage_src=WV, stage_cite=HYPE_STORD, stage_conf="high",
             rounds=[rnd("2019-04-18", "Series A", 12300000, "Kleiner Perkins", True, HYPE_STORD, "press"),
                     rnd("2021-09-14", "round led by Kleiner Perkins (unicorn round)", 90000000, "Kleiner Perkins", True,
                         TC_STORD21, "press"),
                     rnd("2026-05-26", "Series F", 250000000, "Strike Capital", True, TC_STORD26, "press")],
             note="A/B 2026-09-30: Hypepotamus (2019-04-18) reports the $12.3M Series A 'led by Silicon Valley "
                  "venture firm Kleiner Perkins', with Ilya Fushman joining the board, which cites the Form D "
                  "band's Series A; the $3B Series F of May 2026 is the latest priced round."))

# ---- stripe: the 2015 round named
VOX_STRIPE = NEWS("stripe", "Visa Invests in Stripe at $5 Billion")
L.append(cls("stripe", stage="Growth", stage_src=WV, stage_cite=VOX_STRIPE, stage_conf="high",
             entry_date="2015-07-27",
             rounds=[rnd("2015-07-27", "round at a $5B valuation with Visa (unnamed)", None, None, True,
                         VOX_STRIPE, "press"),
                     rnd("2026-02-24", "tender offer at $159B", None, None, None,
                         "https://stripe.com/newsroom/news/stripe-2025-update", "company")],
             note="A/B 2026-09-30: Re/code (Vox, 2015-07-27) reports Visa's investment at a $5B valuation as part "
                  "of a larger round that 'also includes new investor Kleiner Perkins Caufield & Byers', the "
                  "firm's 2015 entry, after the Series A to C, so Growth, now cited. The February 2026 tender at "
                  "$159B is the latest priced event; the July 2026 bid for PayPal changes nothing here."))

# ---- together-ai: the unicorn-list figure re-pinned to the round's own report
QZ_TOGETHER = NEWS("together-ai", "Together AI raises $800 million Series C at $8.3 billion valuation")
L.append(cls("together-ai", rng="1b_plus", usd=8300000000, val_src=WV, val_cite=QZ_TOGETHER, asof="2026-07-01",
             clear=["unicorn_name_match"],
             rounds=R("together-ai") + [rnd("2026-07-01", "Series C", 800000000, "Aramco", None, QZ_TOGETHER,
                                           "press")],
             note="A/B 2026-09-30: the unicorn-list figure is re-pinned to the round itself, the $800M Series C at "
                  "$8.3B announced on 2026-07-01 (Quartz), the figure the Coatue, General Catalyst and NEA rows "
                  "carry; no later priced round was found."))

# ---- transcarent: the Series B names the firm among the new investors
WSGR_TC = NEWS("transcarent", "Wilson Sonsini Advises Transcarent on $58 Million")
_tr = [r for r in R("transcarent") if not str(r.get("round", "")).startswith("Series B")]
L.append(cls("transcarent", stage="Growth", stage_src=WV, stage_cite=WSGR_TC, stage_conf="medium",
             entry_date="2021-06-10",
             rounds=sorted(_tr + [rnd("2021-06-10", "Series B", 58000000, "General Catalyst and 7wireVentures",
                                      True, WSGR_TC, "press")], key=lambda r: str(r.get("date"))),
             note="A/B 2026-09-30: the company counsel's note on the $58M Series B (2021-06-10) lists Kleiner "
                  "Perkins among the participants apart from the existing investors (Alta Partners, Jove Equity), "
                  "and the Series C report of January 2022 does not name it, so the Series B is the entry: Growth. "
                  "Transcarent bought Accolade for $621M in April 2025 at no disclosed valuation of its own, so "
                  "the $2.2B Series D of May 2024 stands, stale."))

# ---- turo: the 2015 Series C the firm led
PRN_TURO = NEWS("turo", "rebrands as Turo - PR Newswire")
L.append(cls("turo", stage="Growth", stage_src=WV, stage_cite=PRN_TURO, stage_conf="high", entry_date="2015-08-18",
             rounds=[rnd("2015-11-03", "Series C", 47000000, "Kleiner Perkins Caufield & Byers", True, PRN_TURO,
                         "company"),
                     rnd("2019-07-17", "Series E", 250000000, "IAC", None,
                         "https://finance.yahoo.com/news/turo-becomes-techs-newest-unicorn-with-250m-iac-investment-194729985.html",
                         "press")],
             note="A/B 2026-09-30: the company's release of 2015-11-03 announces the $47M Series C 'led by Kleiner "
                  "Perkins Caufield & Byers (KPCB) and its affiliates' with the existing investors, the round of "
                  "the Form D first sold on 2015-08-18, when Brook Porter joined the board; that is the entry "
                  "(Growth), not the band's 2014 date. Turo withdrew its IPO filing in February 2025 and stays "
                  "private; no priced round after IAC's 2019 investment was found, stale."))

# ---- viz-ai: the Series A the firm led, cited
CTECH_VIZ = "https://www.calcalistech.com/ctech/articles/0,7340,L-3742616,00.html"
L.append(cls("viz-ai", stage="Series A", stage_src=WV, stage_cite=CTECH_VIZ, stage_conf="high",
             entry_date="2018-07-18",
             rounds=[rnd("2018-07-18", "Series A", 21000000, "Kleiner Perkins", True, CTECH_VIZ, "press"),
                     rnd("2022-04-07", "Series D", 100000000, "Tiger Global and Insight Partners", None,
                         "https://www.insightpartners.com/ideas/viz-ai-raises-100-million-in-series-d-funding-led-by-tiger-global-and-insight-partners-at-1-2-billion-valuation/",
                         "press")],
             note="A/B 2026-09-30: CTech (2018-07-18) reports '$21 million in a Series A funding led by' Kleiner "
                  "Perkins Caufield & Byers with GV, which cites the Series A entry. No priced round after the "
                  "April 2022 Series D was found (the $40M growth capital financing of March 2023 carried no "
                  "valuation), so the mark stands, stale."))

# ---- watershed: the first round, named
CTVC_WS = "https://www.ctvc.co/watershed-taylor-francis/"
L.append(cls("watershed", stage="Series A", stage_src=WV, stage_cite=CTVC_WS, stage_conf="medium",
             rounds=[rnd("2021-02", "Series A", None, "Sequoia and Kleiner Perkins", True, CTVC_WS, "press")]
                    + R("watershed"),
             note="A/B 2026-09-30: CTVC (2021-03-07) says Watershed 'raised a much hyped Series A round which "
                  "brought together Sequoia's Michael Moritz and Kleiner's John Doerr as co-leads', the company's "
                  "first round, announced in February 2021 and dated 2020 by the firm, so the entry is Series A. "
                  "No round after the February 2024 Series C was found; the mark stands, stale."))

# ---- xendit: the unicorn-list figure re-pinned to the Series C; the Series A cited
TC_XENDIT = "https://techcrunch.com/2021/09/14/indonesian-fintech-xendit-is-now-a-unicorn-with-150m-in-fresh-funding-led-by-tiger-global/"
CBN_XENDIT = "https://news.crunchbase.com/business/xendit-indonesia-fintech-payments-tiger-global/"
L.append(cls("xendit", rng="1b_plus", usd=1000000000, val_src=WV, val_cite=TC_XENDIT, asof="2021-09-14",
             stage="Series A", stage_src=WV, stage_cite=CBN_XENDIT, stage_conf="medium", entry_date="2018",
             flags=["stale"], clear=["unicorn_name_match"],
             rounds=[rnd("2018", "Series A", None, "Kleiner Perkins", True, CBN_XENDIT, "press"),
                     rnd("2021-03-02", "Series B", 64600000, "Accel", None,
                         "https://techcrunch.com/2021/03/02/indonesia-payments-infra-startup-xendit-raises-64-6m/",
                         "press"),
                     rnd("2021-09-14", "Series C", 150000000, "Tiger Global", None, TC_XENDIT, "press"),
                     rnd("2022-05-19", "Series D", 300000000, "Coatue and Insight Partners", True, CBN_XENDIT,
                         "press")],
             note="A/B 2026-09-30: Crunchbase News (2022-05-19) names 'Kleiner Perkins (who led the Series A)' "
                  "among the Series D participants, and the firm dates its entry 2018, so Series A. The "
                  "unicorn-list figure is re-pinned to the last round with a disclosed price, the $150M Series C "
                  "'bumping its valuation to $1 billion' (TechCrunch, 2021-09-14); the $300M Series D of May 2022 "
                  "disclosed none, and nothing priced was found since, so stale."))

jl.write("ab1b2", L)
