"""A/B pass, judge ab2, file b (PRO-80 Bessemer): private rows at $1B or more, perplexity to yotpo.
Only the keys that change. Every URL below was printed by a tool of this run and the page was read on 2026-10-06
(headlines through NEWS; where only the headline was read the round says so)."""
import judge_lib as jl

cls, rnd, NEWS = jl.cls, jl.rnd, jl.NEWS
WV = {"valuation_range_source": "web_verified"}

R365_PR = "https://www.prnewswire.com/news-releases/restaurant365-receives-88m-in-funding-led-by-iconiq-capital-300875906.html"
R365_OCBJ = "https://www.ocbj.com/oc-homepage/restaurant365-hits-1b-valuation-135m-raised/"
R365_TC = NEWS("restaurant365", "orders in $175M")
SHIPPO_BLOG = "https://goshippo.com/blog/50-million-new-funding"
WIKI_SHIPPO = "https://en.wikipedia.org/wiki/Shippo_%28company%29"
ACE_QUOTE = "https://stockanalysis.com/quote/nse/ACEVECTOR/"
ACE_LISTING = NEWS("snapdeal", "Lists At 11.6% Discount On BSE")
WIKI_SNAPDEAL = "https://en.wikipedia.org/wiki/Snapdeal"
TRM_A = NEWS("trm-labs", "Announcing Our Series A Funding Round")
TRM_C = "https://siliconangle.com/2026/02/04/trm-labs-raises-70m-1b-valuation-demand-surges-blockchain-intelligence/"
TRM_C2 = "https://markets.businessinsider.com/news/stocks/trm-labs-announces-series-c-expansion-at-2-billion-valuation-to-continue-building-crimefighting-ai-1036532101"
TOSS_C = "https://techcrunch.com/2017/03/09/viva-republica-toss-korea-paypal-goodwater-capital-48-million/"
TOSS_2021 = "https://techcrunch.com/2021/06/22/viva-republica-developer-of-korean-financial-super-app-toss-raises-410m-at-a-7-4b-valuation/"
TOSS_G = "https://techcrunch.com/2022/12/19/south-korean-financial-super-app-toss-closes-405m-series-g-as-valuation-rises-7/"
WILD_A = "https://news.crunchbase.com/venture/brazils-newest-unicorn-wildlife-studios-raises-60m-series-a-led-by-benchmark/"
WILD_B = NEWS("wildlife-studios", "raises $120 million for casual mobile games")
YOTPO_C = "https://techcrunch.com/2016/06/14/yotpo-series-c/"
YOTPO_F = NEWS("yotpo", "raises $230m at $1.4b")

lines = [
    cls("perplexity",
        note="A/B 2026-10-06: Nvidia's reported talks at a valuation above $30B (The Information via Reuters, "
             "2026-08-23) are not a closed round; the September 2025 mark of $20B stands."),
    cls("ramp",
        note="A/B 2026-10-06: a round at about $60B is reported as early talks only (Yahoo Finance, 2026-09-08); the "
             "June 2026 mark of $44B stands."),
    cls("restaurant365",
        rounds=[rnd("2018-01", "Series A", None, "Bessemer Venture Partners", True, R365_PR, "company"),
                rnd("2019-01", "Series B", None, "Bessemer Venture Partners", True, R365_PR, "company"),
                rnd("2019-06-27", "Series C", 88_000_000, "ICONIQ Capital", True, R365_PR, "company"),
                rnd("2023-05-19", "venture round", 135_000_000, "KKR and L Catterton", None, R365_OCBJ, "press"),
                rnd("2024-05-15", "venture round (valuation not disclosed, an up round)", 175_000_000, "ICONIQ Growth",
                    None, R365_TC, "press")],
        note="A/B 2026-10-06: a later round exists, $175M led by ICONIQ Growth (TechCrunch, 2024-05-15), but "
             "'Restaurant365 is not disclosing the valuation it received in the round' beyond calling it an up round, so "
             "the last citable figure remains the $1B of May 2023, stale."),
    cls("shippo", usd=1_000_000_000, val_src="web_verified", val_cite=SHIPPO_BLOG, asof="2021-06-02",
        flags=["stale"], extra={**WV, "valuation_confidence": "high"},
        rounds=[rnd("2016-09", "Series A", 7_000_000, "Union Square Ventures", False, WIKI_SHIPPO, "press"),
                rnd("2017-10", "Series B", 20_000_000, "Bessemer Venture Partners", True, WIKI_SHIPPO, "press"),
                rnd("2021-06-02", "round at a $1B valuation (series not named in the post)", 50_000_000,
                    "Bessemer Venture Partners", True, SHIPPO_BLOG, "company")],
        note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the company's own post of 2021-06-02: 'we "
             "are now valued at $1 billion with another $50 million of capital raised', a round led by Bessemer, as the "
             "Union Square Ventures row cites; no priced round since, so stale."),
    cls("snapdeal", status="public", rng="below_1b", usd=147_160_779, val_src="web_verified", val_cite=ACE_QUOTE,
        asof="2026-10-06", val_conf="high", city="Gurugram", city_src="web_verified", extra=WV,
        rounds=[rnd("2011-07", "second round", 45_000_000, None, True, WIKI_SNAPDEAL, "press"),
                rnd("2014-02", "round led by eBay", 133_000_000, "eBay", True, WIKI_SNAPDEAL, "press"),
                rnd("2026-10-05", "IPO (listing on the NSE and BSE as AceVector Limited)", None, None, None,
                    ACE_LISTING, "press")],
        note="A/B 2026-10-06: the company has listed, so the row is public and the unicorn-list $1B is gone. AceVector "
             "Limited, 'formerly known as Snapdeal Limited' until January 2023 and the owner of the Snapdeal marketplace, "
             "began trading on the NSE and BSE on 2026-10-05 below its IPO price of INR 32 (Inc42); market cap INR 14.19B "
             "at the close of 2026-10-06 (stockanalysis.com, NSE: ACEVECTOR, which places the company in Gurugram). "
             "INR 14.19B @ ECB 2026-10-06 (INR/EUR 108.6615, EUR/USD 1.1269) = $147.2M."),
    cls("trm-labs", stage="Series A", stage_src="web_verified", stage_cite=TRM_A, stage_conf="high",
        entry_date="2021-06-16",
        rounds=[rnd("2021-06-16", "Series A", 14_000_000, "Bessemer Venture Partners", True, TRM_A, "company"),
                rnd("2026-02-04", "Series C", 70_000_000, "Blockchain Capital", None, TRM_C, "press"),
                rnd("2026-09-09", "Series C expansion at a $2B valuation", None, None, None, TRM_C2, "company")],
        note="A/B 2026-10-06: the Series A label is now cited to the company's own post of 2021-06-16: 'TRM has closed a "
             "$14M Series A funding round led by Bessemer Venture Partners'. Nothing priced after the September 2026 "
             "expansion at $2B; the Y Combinator row still carries the February 2026 $1B."),
    cls("upside", flags=["cite_pending"],
        note="A/B 2026-10-06: tried once to cite the 2020 entry round; no page read names Bessemer in a round before the "
             "April 2022 Series D, so the Growth label still rests on knowledge and the row carries cite_pending. The "
             "company operates and has priced nothing since 2022."),
    cls("viva-republica-toss", usd=7_002_897_246, val_src="web_verified", val_cite=TOSS_G, asof="2022-12-19",
        stage="Growth", stage_src="web_verified", stage_cite=TOSS_C, stage_conf="high", entry_date="2017-03-09",
        flags=["stale"], extra={**WV, "valuation_confidence": "high"},
        rounds=[rnd("2017-03-09", "Series C", 48_000_000, None, True, TOSS_C, "press"),
                rnd("2021-06-22", "round at a $7.4B valuation (headline only)", 410_000_000, None, None, TOSS_2021, "press"),
                rnd("2022-12-19", "Series G", 405_000_000, "Tonic Private Equity", None, TOSS_G, "press")],
        note="A/B 2026-10-06: stage and mark are now cited. TechCrunch (2017-03-09): 'a $48 million Series C funding "
             "round', in which 'Bessemer Venture Partners, Altos Ventures and Partech Ventures also participated', the "
             "firm's own investment date, so Growth. Mark re-pinned from the unicorn list to the last priced round: the "
             "$405M Series G, 'now valued at 9.1 trillion won ($7 billion)' (TechCrunch, 2022-12-19), as the Kleiner "
             "Perkins and Ribbit rows carry it; KRW 9100.00B @ ECB 2022-12-19 (KRW/EUR 1377.17, EUR/USD 1.0598) = $7.00B. "
             "The US listing planned for 2026 was put on hold in July 2026; stale."),
    cls("wildlife-studios",
        rounds=[rnd("2019-12-06", "Series A", 60_000_000, "Benchmark", True, WILD_A, "press"),
                rnd("2020-08-14", "Series B at a $3B valuation (headline only)", 120_000_000, "Vulcan", None,
                    WILD_B, "press")],
        note="A/B 2026-10-06: tried again to cite the 2012 entry. Crunchbase News (2019-12-06) names Bessemer in the "
             "$60M Series A led by Benchmark without saying whether it already held shares, and no earlier page names "
             "it, so the stage stays undetermined. No priced round since August 2020."),
    cls("yotpo", usd=1_400_000_000, val_src="web_verified", val_cite=YOTPO_F, asof="2021-03-18",
        flags=["stale"], extra={**WV, "valuation_confidence": "high"},
        rounds=[rnd("2016-06-14", "Series C", 22_000_000, "Bessemer Venture Partners", True, YOTPO_C, "press"),
                rnd("2021-03-18", "Series F", 230_000_000, "Bessemer Venture Partners and Tiger Global", True, YOTPO_F, "press")],
        note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the round. Globes (2021-03-18): 'a $230 "
             "million Series F financing round' led by Bessemer and Tiger Global at a $1.4 billion valuation; no priced "
             "round since (200 layoffs in August 2025), so stale."),
]

if __name__ == "__main__":
    for x in lines:
        assert "—" not in (x.get("note") or ""), x["slug"]
    jl.write("ab2b", lines)
