#!/usr/bin/env python3
"""PRO-167 Tiger Global, verify-gap fix a (2026-09-29): cited entry stage for 11 of the 21 $1B+ rows in
fix-stage.json (jd-com .. uber). Each line cites a page naming the round in which Tiger first put money in and
Tiger's part in it, corrects the entry where the record was wrong (Stripe, OpenAI), and records the rounds found;
where no page ties Tiger to a named round the row carries `cite_pending` (Spotify, Palantir).
Citations come from fxlib/judge_lib helpers that read URLs on disk (fx-sources.json holds each fetched page's quote).
Run: NQ_TAG=fx python3 fixa.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402
from judge_lib import cls, rnd  # noqa: E402
from fxlib import SRC, BURL, OLD  # noqa: E402

L = []

# ---------------------------------------------------------------- JD.com: Tiger's early-2010 round, after the B
u = SRC("jd-pedaily")
L.append(cls("jd-com", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2010",
             rounds=[rnd("2007", "first round (Series A)", 10_000_000, "Capital Today", False, u),
                     rnd("2009", "Series B", 21_000_000, "Capital Today, Bull Capital and Liang Bochao's company",
                         False, u),
                     rnd("2010", "third round, at a $250M valuation", None, "Tiger Global", True, u),
                     OLD("jd-com", "private placement")],
             note="Verify fix 2026-09-29: entry round cited. 投资界 (2023-06-07): Capital Today's $10M first round, "
                  "then a $21M Series B from Capital Today, Bull Capital and Liang Bochao's company after the 2008 "
                  "crisis, then, before the 2010 Lunar New Year, Tiger's China head offered to invest at a $250M "
                  "valuation and Richard Liu took Tiger's money. Tiger's entry is that third round of early 2010: "
                  "Growth, web_verified. The F-1's issuance history covers only 2011 on, so it shows the later $75M "
                  "of November 2012, not the first purchase."))

# ---------------------------------------------------------------- Spotify: no page names Tiger's round
L.append(cls("spotify", flags=("cite_pending",), rounds=[],
             note="Verify fix 2026-09-29: cite pending. Tiger held about 7% (12.18M shares) through MH1 LLC and PIP IX "
                  "before the April 2018 direct listing (the DRS; Institutional Investor 2018-03-02; TechCrunch "
                  "2018-05-09), but no page read names the round or the date of its first purchase: the DRS names no "
                  "buyer in its 2015 private placement (3 individuals and 29 entities), and Bing News, Google News and "
                  "one web search (2026-09-29) found none. The stage stays Growth from the record (model)."))

# ---------------------------------------------------------------- ByteDance: secondary purchases from a $37.5B mark
u = SRC("bytedance-caixin")
L.append(cls("bytedance", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium",
             entry_date="2018",
             rounds=[rnd("2018", "secondary share purchases (first at a $37.5B valuation)", None, None, True, u)],
             note="Verify fix 2026-09-29: Caixin (2020-03-31, reporting the FT): Tiger 'began buying ByteDance's "
                  "shares when the Chinese unicorn was valued at $37.5 billion and has since increased its investment "
                  "through share purchases in secondary markets', a 21-month programme, so from about mid-2018. A "
                  "secondary entry into a late private company: Growth, web_verified at medium (the first trade is "
                  "dated only by that count)."))

# ---------------------------------------------------------------- Databricks: Series F, October 2019
u = SRC("databricks-crn")
L.append(cls("databricks", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2019-10-22",
             rounds=[rnd("2019-02", "Series E", 250_000_000, None, None, u),
                     OLD("databricks", "Series F")],
             note="Verify fix 2026-09-29: CRN (2019-10-22) lists Tiger Global Management among the investors of the "
                  "$400M Series F led by a16z's Late Stage Venture Fund; the February 2019 Series E it mentions does "
                  "not name Tiger, and no earlier round in our sources does: Growth, web_verified."))

# ---------------------------------------------------------------- Facebook: secondary purchases via the holdco
u = SRC("fb-s1")
L.append(cls("facebook", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium",
             entry_date="2011",
             rounds=[rnd("2011-02", "secondary purchases of private shares through the single-deal vehicle "
                         "(Tiger Global FB Partners / FB Holdings)", None, None, True, SRC("fb-partners-formd"),
                         "filing")],
             note="Verify fix 2026-09-29: the S-1 lists Tiger Global FB Holdings, LLC among the holders under the "
                  "voting agreement that binds investors' secondary purchases, so Tiger entered by buying private "
                  "shares from holders (D6: Growth), web_verified at medium. The single-deal vehicle Tiger Global FB "
                  "Partners, LLC filed a Form D with a first sale on 2011-02-07 ($60.4M from 16 investors), which "
                  "dates the purchase to 2011; an earlier purchase through another Tiger fund is not on record."))

# ---------------------------------------------------------------- OpenAI: correction, first shares bought in 2021
u = SRC("openai-cnbc-2024")
L.append(cls("openai", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium",
             entry_date="2021",
             rounds=[rnd("2021", "share purchase (round not named)", None, None, True, u),
                     rnd("2023-04", "share sale at $27-29B", 300_000_000, None, False, SRC("openai-tc-2023")),
                     OLD("openai", "growth round")],
             note="Verify fix 2026-09-29: correction. TechCrunch updated its April 2023 share-sale story 'to remove "
                  "Tiger from this story; it did not participate in this share sale but is an investor in OpenAI', "
                  "so the iPhone in Canada copy recorded before is wrong. CNBC (2024-09-13): Tiger 'first bought "
                  "shares in OpenAI in 2021'. The 2021 purchase is not named as a round; any share purchase in OpenAI "
                  "that year was a late-stage one: Growth, web_verified at medium, entry 2021."))

# ---------------------------------------------------------------- Palantir: no page names Tiger's round
L.append(cls("palantir", flags=("cite_pending",), rounds=[],
             note="Verify fix 2026-09-29: cite pending. Wikipedia places Tiger among Palantir's private funders by "
                  "December 2014 and GSV's 2017 8-K lists it as a notable investor, but no page read names the round "
                  "Tiger joined (the Forbes 2013 round reports return 403; Google News, Bing News and one web search, "
                  "2026-09-29). The stage stays Growth from the record (model)."))

# ---------------------------------------------------------------- Scale AI: led the Series D
u = SRC("scale-cnbc")
L.append(cls("scale-ai", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2020-12-01",
             rounds=[OLD("scale-ai", "Series D"), OLD("scale-ai", "Series E")],
             note="Verify fix 2026-09-29: CNBC (2020-12-01): 'Scale announced Tuesday that it has raised $155 million, "
                  "led by Tiger Global, at a valuation over $3.5 billion', the Series D and the earliest Tiger money "
                  "on record: Growth, web_verified. Wikipedia's list of 'initial investors' naming Tiger is not tied "
                  "to any round."))

# ---------------------------------------------------------------- Stripe: correction, entry September 2018
u = SRC("stripe-bi-2018")
L.append(cls("stripe", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2018-09",
             rounds=[rnd("2018-09", "Series E", 245_000_000, "Tiger Global, Sequoia and DST Global", True, u),
                     rnd("2019-01", "Series E add-on", 100_000_000, "Tiger Global", True,
                         BURL("stripe", "Stripe Raises $100 Million At $22.5 Billion", "pulse2"))],
             note="Verify fix 2026-09-29: correction of the entry date. Tiger first came in on the $245M round of "
                  "September 2018 at $20B: 'This new round was led by Tiger Global Management, Sequoia, and DST "
                  "Global' (Business Insider via Yahoo, 2018-09-27; Pulse 2.0 calls it the Series E). The $100M of "
                  "January 2019 at $22.5B was Tiger's add-on to that round. Growth, web_verified."))

# ---------------------------------------------------------------- Toast: new investor in the Series D
u = BURL("toast", "Toast secures $115M in funding", "fastcasual")
L.append(cls("toast", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2018-06",
             rounds=[rnd("2018-06", "Series D", 115_000_000, "T. Rowe Price", True, SRC("toast-s1"), "filing"),
                     rnd("2019-03", "Series E", 250_000_000, "TCV and Tiger Global", True,
                         BURL("toast", "Toast raises $250M in Series E", "fastcasual")),
                     rnd("2020-02", "Series F", 400_000_000, "TPG and Tiger Global among others", True,
                         BURL("toast", "Restaurant software maker Toast valued at $4.9 billion", "reuters.com"))],
             note="Verify fix 2026-09-29: Fast Casual (2018-07-10): the $115M Series D was led by T. Rowe Price 'with "
                  "participation from new investor Tiger Global Management'; the S-1 dates the Series D sale to June "
                  "2018 and shows Tiger Global PIP 10 LLC buying 752,576 Series D, 3,663,043 Series E and 660,071 "
                  "Series F shares ($143.0M), so the Series B and C shares it also held came from other holders. "
                  "Entry June 2018: Growth, web_verified."))

# ---------------------------------------------------------------- Uber: the December 2015 round
u = SRC("uber-mint")
L.append(cls("uber", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2015-12",
             rounds=[rnd("2015-12", "Series G", None, None, True, u)],
             note="Verify fix 2026-09-29: Mint (2015-12-05, citing Bloomberg): 'Uber closed investments from Tiger "
                  "Global and T. Rowe Price as part of a new round of funds that may value the company at $62.5 "
                  "billion', the Series G and Tiger's first Uber money on record: Growth, web_verified."))

if __name__ == "__main__":
    jl.write("fix-a", L)
