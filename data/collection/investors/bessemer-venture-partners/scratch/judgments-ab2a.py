"""A/B pass, judge ab2, file a (PRO-80 Bessemer): private rows at $1B or more, ada to mambu.
Only the keys that change. Every URL below was printed by a tool of this run and the page was read on 2026-10-06
(the firm's posts through POST, headlines through NEWS)."""
import judge_lib as jl

cls, rnd, NEWS, POST = jl.cls, jl.rnd, jl.NEWS, jl.POST
WV = {"valuation_range_source": "web_verified"}

BETAKIT_ADA_A = "https://betakit.com/ada-closes-19-million-series-a-to-tackle-travel-and-financial-customer-support/"
BETAKIT_ADA_C = NEWS("ada", "claims $1.2 billion")
ANTH_H = "https://www.anthropic.com/news/series-h"
ANTH_C = "https://www.anthropic.com/news/anthropic-series-c"
TC_BETTERMENT = "https://techcrunch.com/2010/12/01/bessemer-betterment-3-million/"
BOOM_B = NEWS("boom-supersonic", "Closes $100 Million Series B to Develop Overture")
BOOM_MARK = "https://businessden.com/boom-supersonic-raising-300m-at-a-1-5b-valuation/"
GLOBES_CLAROTY_B = "https://en.globes.co.il/en/article-israeli-cybersecurity-co-claroty-raises-60m-1001240893"
GV_CLAROTY = "https://globalventuring.com/claroty-finds-series-b-clarity"
CALCALIST_CLAROTY_F = "https://www.calcalistech.com/ctechnews/article/syuo0xklwe"
VB_DEVO_F = NEWS("devo", "announces $100M in funding")
CB_DEVO_D = "https://news.crunchbase.com/startups/devo-technology-raises-60m-series-d/"
CB_DEVO_E = NEWS("devo", "Whips Up $250M Series E")
DR_DEVO = NEWS("devo", "Adds $60 Million in Growth Funding")
TC_KLOOK = "https://techcrunch.com/2019/04/08/klook-raises-225m"
WIKI_KLOOK = "https://en.wikipedia.org/wiki/Klook_%28company%29"
FINOVATE_MAMBU = NEWS("mambu", "Scores $34 Million")
TC_MAMBU_A = "https://techcrunch.com/2013/02/14/mambu/"
BW_MAMBU_D = NEWS("mambu", "Raises €110 Million in Funding Round Led by TCV")
MAMBU_E = "https://mambu.com/en/insights/press/mambu-raises-eur235-million-at-eur4-9-billion-valuation-in-eqt-growth-led-series-e"

lines = [
    cls("ada", usd=1_200_000_000, val_src="web_verified", val_cite=BETAKIT_ADA_C, asof="2021-05-07",
        flags=["stale"], extra={**WV, "valuation_confidence": "high"},
        rounds=[rnd("2016-11", "Seed", 2_500_000, None, True, BETAKIT_ADA_A, "press"),
                rnd("2018-12-18", "Series A", 19_000_000, "FirstMark Capital", True, BETAKIT_ADA_A, "press"),
                rnd("2021-05-07", "Series C", 130_000_000, "Spark Capital", True, BETAKIT_ADA_C, "press")],
        note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the round itself. BetaKit (2021-05-07): "
             "'$130 million USD in Series C financing' led by Spark Capital at a $1.2 billion valuation, Bessemer among "
             "the returning investors; no priced round since, so stale. The Accel row (ada-support) still reads below $1B."),
    cls("anthropic", usd=965_000_000_000, val_src="web_verified", val_cite=ANTH_H, asof="2026-05-28",
        stage="Growth", stage_src="first_party", stage_cite=POST("why-we-invested-in-anthropic"), stage_conf="medium",
        extra={**WV, "valuation_confidence": "high"},
        rounds=[rnd("2023-05-23", "Series C", 450_000_000, "Spark Capital", False, ANTH_C, "company"),
                rnd("2024", "the firm's first investment (round not named by the firm)", None, None, True,
                    POST("why-we-invested-in-anthropic"), "firm"),
                rnd("2025-03-03", "Series E", 3_500_000_000, "Lightspeed", True,
                    POST("3-5-billion-more-for-anthropic"), "firm"),
                rnd("2026-05-28", "Series H", 65_000_000_000,
                    "Altimeter Capital, Dragoneer, Greenoaks and Sequoia Capital", None, ANTH_H, "company")],
        note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the company's own announcement of "
             "2026-05-28, '$65 billion in Series H funding', 'valuing the company at $965 billion post-money'; the "
             "secondary trades near $1.2 trillion and the IPO filed in June 2026 are not priced primary events. Stage: "
             "the firm's post of 2024-10-22 dates its first investment after the company's Series C of 2023-05-23, so "
             "the entry is a later round, Growth, the round itself still not named."),
    cls("betterment", stage="Series A", stage_src="web_verified", stage_cite=TC_BETTERMENT, stage_conf="high",
        rounds=[rnd("2010-12-01", "Series A", 3_000_000, "Bessemer Venture Partners", True, TC_BETTERMENT, "press"),
                rnd("2012-10-03", "Series B", 10_000_000, "Menlo Ventures", True,
                    "https://www.cnbc.com/2012/10/03/betterment-raises-10-million-series-b-financing-from-menlo-ventures-bessemer-venture-partners-anthemis-group.html", "press"),
                rnd("2021-09-29", "Series F", 60_000_000, "Treasury", None,
                    "https://www.bloomberg.com/news/articles/2021-09-29/betterment-valuation-rises-to-1-3-billion-on-new-funding-round", "press")],
        note="A/B 2026-10-06: the Series A label is now cited. TechCrunch (2010-12-01): 'raised $3 million in a series A "
             "financing led by Bessemer Venture Partners'. No priced round since the 2021 Series F was found; the Menlo "
             "row still reads below $1B and should carry the $1.3B mark."),
    cls("boom-supersonic", stage="Growth", stage_src="first_party", stage_cite=POST("roadmap-deep-tech"),
        stage_conf="medium",
        rounds=[rnd("2019-01-04", "Series B", 100_000_000, "Emerson Collective", False, BOOM_B, "company"),
                rnd("2021-03", "the firm's first investment (round not named)", None, None, True,
                    POST("roadmap-deep-tech"), "firm"),
                rnd("2025-12-09", "unnamed round at $1.5B post-money", 300_000_000, "Darsana Capital Partners", True,
                    BOOM_MARK, "press")],
        note="A/B 2026-10-06: the stage now rests on the firm's own post ('in March 2021, Bessemer invested in Boom "
             "Supersonic') read against the company's release of 2019-01-04 on its $100 million Series B led by Emerson "
             "Collective: the entry is a later round, Growth, its name not published. Crusoe ended its turbine order in "
             "September 2026 (The Business Journals) and no round has priced since December 2025, so the $1.5B mark stands."),
    cls("claroty", stage="Series A", stage_src="web_verified", stage_cite=GLOBES_CLAROTY_B, stage_conf="medium",
        rounds=[rnd("2016-09-13", "funding disclosed at launch (the round before the Series B, not named in the sources read)",
                    32_000_000, None, True, GV_CLAROTY, "press"),
                rnd("2018-06-11", "Series B", 60_000_000, "Temasek", True, GLOBES_CLAROTY_B, "press"),
                rnd("2026-01-22", "Series F", 150_000_000, "Golub Growth", None, CALCALIST_CLAROTY_F, "press")],
        note="A/B 2026-10-06: the stage is now cited. Globes (2018-06-11) calls the $60 million round led by Temasek the "
             "Series B and Bessemer one of the 'original Claroty investors'; GlobalVenturing (2018-06-12) names BVP in "
             "the $32 million disclosed at the 2016 launch, the round before that Series B, so the entry reads Series A "
             "(medium: neither page prints the words Series A or names a lead). No priced event after January 2026."),
    cls("devo", usd=2_000_000_000, val_src="web_verified", val_cite=VB_DEVO_F, asof="2022-06-02",
        flags=["stale"], extra={**WV, "valuation_confidence": "high"},
        rounds=[rnd("2017-09", "Series B", 35_000_000, "Insight Venture Partners", False,
                    "https://www.insightpartners.com/ideas/logtrust-closes-a-35-million-series-b-round-from-insight-venture-partners/", "firm"),
                rnd("2020-09-16", "Series D", 60_000_000, "Georgian", True, CB_DEVO_D, "press"),
                rnd("2021-10-26", "Series E", 250_000_000, "TCV", None, CB_DEVO_E, "press"),
                rnd("2022-06-02", "Series F", 100_000_000, "Eurazeo", None, VB_DEVO_F, "press"),
                rnd("2023-11-29", "growth funding (headline only, no valuation)", 60_000_000, None, None, DR_DEVO, "press")],
        note="A/B 2026-10-06: the mark moves from the unicorn list's $1.5B (the October 2021 Series E) to the later "
             "priced round. VentureBeat (2022-06-02): '$100 million as part of a series F funding round' led by Eurazeo, "
             "'achieved a valuation of $2 billion'; nothing priced since, so stale. The Insight and TCV rows still read $1.5B."),
    cls("electric",
        note="A/B 2026-10-06: the 'Electric' that Databricks bought in August 2026 is the Postgres sync company, a "
             "namesake; this Electric still sells IT support (HRTech Series, 2026-08-26) and has priced no round since "
             "March 2022, so the mark stands, stale."),
    cls("klook", usd=1_000_000_000, val_src="web_verified", val_cite=TC_KLOOK, asof="2018-08",
        flags=["stale"], extra={**WV, "valuation_confidence": "medium"},
        rounds=[rnd("2018-08-07", "Series D", 200_000_000, None, False, TC_KLOOK, "press"),
                rnd("2019-04-08", "Series D+", 225_000_000, "SoftBank Vision Fund", False, TC_KLOOK, "press"),
                rnd("2023-12", "Series E+", 210_000_000, "Bessemer Venture Partners", True, WIKI_KLOOK, "press")],
        note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the round. TechCrunch (2019-04-08) puts the "
             "$200 million Series D of August 2018 at a valuation of 'over $1 billion' and says the $225 million Series "
             "D+ led by SoftBank Vision Fund raised it without giving a figure; the figure recorded is that floor, at "
             "the band edge, stale. The rounds of December 2023 and February 2025 disclosed no valuation, and the US "
             "listing filed in November 2025 was delayed and had not priced by 2026-10-06. The TCV row cites a page "
             "that carries no figure."),
    cls("legora",
        note="A/B 2026-10-06: a new round is reported as talks only (Financial Times, 2026-08-12, above $10B; Bloomberg "
             "via Investing.com, 2026-09-22, $300M at $8.5B); nothing has closed, so the March 2026 mark of $5.55B stands."),
    cls("mambu", stage="Growth", stage_src="web_verified", stage_cite=FINOVATE_MAMBU, stage_conf="high",
        rounds=[rnd("2013-02-14", "Series A", 2_000_000, "Point Nine Capital and Runa Capital", False, TC_MAMBU_A, "press"),
                rnd("2019-02-20", "funding round (series not named in the source)", 34_000_000,
                    "Bessemer Venture Partners", True, FINOVATE_MAMBU, "press"),
                rnd("2021-01-07", "funding round led by TCV (EUR 110M, as the release is headed)", None, "TCV", None, BW_MAMBU_D, "company"),
                rnd("2021-12-09", "Series E", 266_000_000, "EQT Growth", None, MAMBU_E, "company")],
        note="A/B 2026-10-06: the stage is now cited. Finovate (2019-02-20): '$34 million (EUR 30 million) in its latest "
             "funding round led by US-based Bessemer Venture Partners', beside existing investors Acton, CommerzVentures, "
             "Point Nine and Runa, six years after the $2M Series A (TechCrunch, 2013-02-14): a later round, Growth, the "
             "series not named. No priced round since December 2021."),
]

if __name__ == "__main__":
    for x in lines:
        assert "—" not in (x.get("note") or ""), x["slug"]
    jl.write("ab2a", lines)
