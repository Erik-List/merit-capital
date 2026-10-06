"""A/B pass, judge ab1 (PRO-80): private rows at $1B or more, second half (livspace to zapier).

Pass A re-pins every mark that rested on the unicorn list to the round's own report (read on 2026-10-06); pass B
searched Google News (nq.py) for a newer round, a sale, a down round or a shutdown. Only the keys that change.

Run once: NQ_TAG=ab1 python3 judgments-ab1b.py
"""
import json

import judge_lib as jl
from judge_lib import cls, rnd, NEWS, POST

WV = "web_verified"
X = {"valuation_range_source": WV}
_CL = json.loads((jl.INV / "companies" / "classification.json").read_text())
_CL = _CL.get("bessemer-venture-partners", _CL)


def R(slug):
    """The funding rounds already on the row (record replaces the list, so a line carries the whole list)."""
    return [dict(x) for x in (_CL.get(slug) or {}).get("funding_rounds") or []]


def BELOW(url, asof):
    """A below_1b band with its dated web check (the form the momentum slice uses)."""
    return {"valuation_source": WV, "valuation_range_source": WV, "valuation_citation": url, "valuation_asof": asof}


L = []

# ---- livspace: the entry gets a press citation in place of Wikipedia
TC_LIV = "https://techcrunch.com/2015/08/11/livspace-lands-8m-to-expand-its-online-home-design-service-in-india/"
L.append(cls("livspace", stage="Series A", stage_src=WV, stage_cite=TC_LIV, stage_conf="high",
             note="A/B 2026-10-06: TechCrunch (2015-08-11, read) confirms the entry: the $4.6 million Series A, extended "
                  "by 'existing investors Helion Venture Partners, Bessemer Ventures Partners and Jungle Ventures'. No "
                  "priced round after February 2022: 1,000 jobs went and a co-founder left in February 2026 (Inc42 "
                  "headline), and a co-founder's secondary share purchase of July 2026 (DealStreetAsia, paywalled) gave "
                  "no readable price, so the mark stays stale."))

# ---- nydig
L.append(cls("nydig", flags=["cite_pending"],
             note="A/B 2026-10-06: BitGo agreed in August 2026 to buy NYDIG's institutional trading unit for $42.5M plus "
                  "an earn-out (TradingView headline), a unit sale and no mark for the company, so the December 2021 "
                  "figure stands, stale. The firm's 2020 post, read again, names no round for the 2017 entry ('initial "
                  "early-stage investment'), so cite_pending."))

# ---- papaya-global
GLOBES_PAP = NEWS("papaya-global", "Papaya Global raises $250m at $3.7b")
L.append(cls("papaya-global", rng="1b_plus", usd=3_700_000_000, val_src=WV, val_cite=GLOBES_PAP, asof="2021-09-11",
             extra=X, flags=["stale"],
             note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the Series D: 'raised $250 million at a "
                  "valuation of $3.7 billion', with Bessemer taking part (Globes, 2021-09-11, read); older than 24 "
                  "months, so stale. CTech (headline, 2026-01-06) reported sale talks at $3.5B to $4.5B; no deal "
                  "followed."))

# ---- perfios
VCC = NEWS("perfios", "Fin-tech firm Perfios raises")
L.append(cls("perfios", stage="Series A", stage_src=WV, stage_cite=VCC, stage_conf="high",
             note="A/B 2026-10-06: VCCircle (2017-04-04, read this time): 'raised $6.1 million (Rs 40 crore) in its "
                  "Series A round from Bessemer Venture Partners, marking its first institutional funding', so the "
                  "entry is cited; no priced round after March 2024 found (Google News), the mark stays stale."))

# ---- productboard
PB_B = "https://www.productboard.com/blog/productboard-raises-a-45-m-series-b-led-by-sequoia-capital/"
PB_D = "https://www.productboard.com/blog/series-d-announcement/"
L.append(cls("productboard", rng="1b_plus", usd=1_725_000_000, val_src=WV, val_cite=PB_D, asof="2022-02-01", extra=X,
             stage="Growth", stage_src=WV, stage_cite=PB_B, stage_conf="high", flags=["stale"],
             rounds=[rnd("2018-07", "Series A", 8_000_000, "Kleiner Perkins", False, None),
                     rnd("2019-02-04", "Series A extension", 10_000_000, "Index Ventures", None,
                         "https://techcrunch.com/2019/02/04/productboard/"),
                     rnd("2020-01-14", "Series B", 45_000_000, "Sequoia Capital", True, PB_B, "company"),
                     rnd("2022-02-01", "Series D", 125_000_000, "Dragoneer and Tiger Global", True, PB_D, "company")],
             note="A/B 2026-10-06: the company's own posts (read) cite both columns: 'a $45M Series B led by Sequoia "
                  "Capital with new investor Bessemer Venture Partners' (2020-01-14; the firm dates the close 2019) and "
                  "the $125M Series D of 2022-02-01 'with a new valuation of $1.725B'. The mark is older than 24 months, "
                  "so stale; no later priced round found (Google News)."))

# ---- render
CNBC_RENDER = NEWS("render", "Cloud startup Render raises funding")
r = R("render") + [rnd("2025-01-21", "Series C", 80_000_000, None, None, None),
                   rnd("2026-02-17", "Series C extension", 100_000_000, None, None, CNBC_RENDER)]
L.append(cls("render", rng="1b_plus", usd=1_500_000_000, val_src=WV, val_cite=CNBC_RENDER, asof="2026-02-17", extra=X,
             rounds=r,
             note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the round's own report: 'raised $100 "
                  "million in funding at a $1.5 billion valuation' on 2026-02-17, Bessemer among the investors (CNBC, "
                  "read); no later round found."))

# ---- shift-technology
TC_SHIFT = "https://techcrunch.com/2021/05/05/shift-technology-raises-220m-at-a-1b-valuation-to-fight-insurance-fraud-with-ai/"
r = R("shift-technology") + [rnd("2021-05-05", "Series D", 220_000_000, "Advent International", True, TC_SHIFT)]
L.append(cls("shift-technology", rng="1b_plus", usd=1_000_000_000, val_src=WV, val_cite=TC_SHIFT, asof="2021-05-05",
             extra=X, flags=["stale"], rounds=r,
             note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the $220M Series D of 2021-05-05 led by "
                  "Advent, 'now valued at over $1 billion', Bessemer taking part (TechCrunch, read); older than 24 "
                  "months, so stale, and no later priced round found (Google News)."))

# ---- sisense
TC_SIS20 = "https://techcrunch.com/2020/01/09/sisense-nabs-another-100m-at-a-1b-valuation-for-its-big-data-business-analytics-solutions/"
TC_SIS18 = "https://techcrunch.com/2018/09/12/sisense-hauls-in-80m-investment-as-data-analytics-business-matures/"
L.append(cls("sisense", rng="1b_plus", usd=1_000_000_000, val_src=WV, val_cite=TC_SIS20, asof="2020-01-09", extra=X,
             entry_date="2015-12-16", flags=["stale"],
             rounds=[rnd("2016-01-07", "$50M round (reported by the WSJ, per Wikipedia)", 50_000_000, None, None, None),
                     rnd("2018-09-12", "Series E", 80_000_000, "Insight Venture Partners", True, TC_SIS18),
                     rnd("2020-01-09", "growth round at over $1B", 100_000_000, "Insight Partners", True, TC_SIS20)],
             note="A/B 2026-10-06: the mark is re-pinned from the unicorn list's $1.1B to the January 2020 round, $100M "
                  "led by Insight that 'catapults Sisense's valuation to over $1 billion' (TechCrunch, 2020-01-09, read; "
                  "Globes: over $1 billion before the money), recorded at $1.0B and stale; layoffs in 2023 and 2024, no "
                  "later priced round. The entry date moves from the 2019 Form D to the firm's own 2015-12-16 (the $50M "
                  "round announced 2016-01-07): TechCrunch (2018-09-12, read) already lists Bessemer among the past "
                  "investors at the Series E, and the stage stays Growth."))

# ---- sorare: collapse evidence, the Pipe reading of COLLECTION.md s6
BGB = NEWS("sorare", "Sorare raises +")
CT_SOR = NEWS("sorare", "Lays Off 35%")  # the layoffs report, decoded so the cache keeps its URL
r = R("sorare") + [rnd("2026-09", "insider round, price undisclosed", None, None, None, BGB)]
L.append(cls("sorare", rng="below_1b", extra=BELOW(BGB, "2026-09-21"), clear=["stale"], rounds=r,
             note="A/B 2026-10-06: the 2021 mark of $4.3B yields to collapse evidence (COLLECTION.md s6, a restructuring "
                  "followed by a small round at an undisclosed price). Revenue fell from EUR 59M in 2023 to EUR 43M in "
                  "2024 with losses above EUR 220M, 35 of about 100 staff were cut and the CTO stepped back in November "
                  "2025 (The Crypto Times, 2025-11-21, read); in September 2026 the existing investors and the "
                  "founders put in 'tens of millions of euros' with no valuation disclosed, after the New York office "
                  "closed and more than EUR 500M of licence commitments were renegotiated or withdrawn "
                  "(BlockchainGamer.biz, read). The row reads below $1B."))

# ---- the-exploration-company: the stored mark was a report of talks; the closed round disclosed no valuation
TNW_C = NEWS("the-exploration-company", "Europe's biggest space round")
r = R("the-exploration-company") + [rnd("2026-09-08", "Series C", 450_000_000,
                                        "Bessemer Venture Partners, Atomico and Scaleup Europe Fund", True, TNW_C)]
L.append(cls("the-exploration-company", rng="below_1b", extra=BELOW(TNW_C, "2026-09-08"), rounds=r,
             note="A/B 2026-10-06: the stored $2.0B came from a report of talks (The Next Web, 2026-07-27, read: 'in talks "
                  "to raise at least $300mn', 'the financing has not been finalised'), which is no priced event. The "
                  "round closed on 2026-09-08 as a $450M Series C co-led by Bessemer, Atomico and the Scaleup Europe "
                  "Fund, and 'nobody disclosed a valuation. Not the company, and not any outlet covering the close' "
                  "(The Next Web, read; Pulse 2.0 and Trending Topics carry none either), so under Rule A the row "
                  "reads below $1B until a figure is published."))

# ---- toss, waymo, zapier: attacked, nothing changes
L.append(cls("toss", note="A/B 2026-10-06: still private: the US listing planned for 2026 was put on hold in July (Seoul "
             "Economic Daily headline, 2026-07-07), and no priced round after the December 2022 Series G was found, so "
             "the mark stays stale."))
L.append(cls("waymo", note="A/B 2026-10-06: no equity round after the February 2026 Series D found (Google News); the $3B "
             "raised in September 2026 was debt (Yahoo Finance headline)."))
L.append(cls("zapier", note="A/B 2026-10-06: no priced event after the March 2021 share sale found (Google News), the "
             "mark stays stale."))

# ---- ual
L.append(cls("ual", flags=["cite_pending"],
             note="A/B 2026-10-06: the mark holds: Tether's $20M investment of July 2026 came at the same $3.2B (The "
                  "Block headline). No round report read names Bessemer (TechCrunch on the 2019 Series C and the 2021 "
                  "round, Business Insider on the 2018 Series B), so the entry stays undetermined with cite_pending."))

# ---- wonderful: the mark gets its citation, and a Seed entry with cited later rounds is graduated, not censored
TC_WON = "https://techcrunch.com/2026/09/02/wonderful-more-than-doubles-its-valuation-to-5b-in-under-6-months/"
GLOBES_WON = NEWS("wonderful", "Israeli AI agents co Wonderful raises")
POST_WON = POST("the-trailblazer-in-enterprise-ai")
L.append(cls("wonderful", rng="1b_plus", usd=5_000_000_000, val_src=WV, val_cite=TC_WON, asof="2026-09-02", extra=X,
             grad="graduated", grad_src="first_party", grad_cite=POST_WON, grad_conf="high",
             rounds=[rnd("2025", "Seed", None, None, True, POST_WON, "firm"),
                     rnd("2025-11", "round", 100_000_000, None, None, GLOBES_WON),
                     rnd("2026-03-12", "Series B", 150_000_000, "Insight Partners", True, GLOBES_WON),
                     rnd("2026-09-02", "Series C", 550_000_000, "Insight Partners", True, POST_WON, "firm")],
             note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to TechCrunch (2026-09-02, read): '$550 "
                  "million in a Series C funding round that gives it a price tag of $5 billion', Bessemer taking part "
                  "again. The censored status is replaced by graduated: the clock guards an absence only, and the "
                  "firm's own post names the Series C it joined after its seed check (Globes, 2026-03-12, read, has the "
                  "Series B at $2B with Bessemer as an existing investor)."))

if __name__ == "__main__":
    jl.write("ab1b", L)
