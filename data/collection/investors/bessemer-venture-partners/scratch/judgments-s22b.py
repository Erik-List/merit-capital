"""Second pass s22, file b: rows first seen 2005 to 2024 (queue/s2-2.json). Entry rounds from press read for this
pass (URLs found through TechCrunch's own search, the row's news items or a web search, each page read), the firm's
own post, or a named round from memory at medium confidence. Only changed keys are emitted; notes append to the
stored note."""
import judge_lib as jl

cls, rnd, NEWS, W, POST = jl.cls, jl.rnd, jl.NEWS, jl.W, jl.POST

TC_WIZE = "https://techcrunch.com/2007/01/21/four-month-old-wize-gets-4-million/"
TC_OPENCANDY = "https://techcrunch.com/2010/04/21/opencandy-raises-5-million-series-b-for-bundled-software-you-might-actually-want/"
TC_CROWDFLOWER = "https://techcrunch.com/2010/01/20/crowdflower-raises-5-million-for-cloud-sourced-labor/"
TC_XTREME = "https://techcrunch.com/2010/07/27/xtreme-power-funding/"
TC_MOJAVE = "https://techcrunch.com/2013/11/24/the-danger-of-laissez-faire-security-attitudes/"
TC_SCRATCH = "https://techcrunch.com/2015/07/14/scratch-an-e-commerce-app-that-lets-you-text-requests-to-expert-shoppers-raises-3-6-million/"
MEDCITY_VERATO = "https://medcitynews.com/2017/02/patient-matching-startup-verato-series-b/"
TC_ZIRX = "https://techcrunch.com/2015/04/22/zirx-30m-bessemer/"
TC_DEEPSCALE = "https://techcrunch.com/2017/03/21/deepscale-raises-3-million-for-perception-ai-to-make-self-driving-cars-safe/"
CALCALIST_ZOOMIN_B = "https://www.calcalistech.com/ctech/articles/0,7340,L-3882230,00.html"
FOLD_BLOG = "https://blog.foldapp.com/fold-raises-13-million-series-ato-bring-bitcoin-rewards-to-mass-market/"
TC_ZENSKAR = "https://techcrunch.com/2022/10/03/saas-billing-platform-zenskar-funding-bessemer-ventures-partners/"
BETAKIT_DAYLIGHT = "https://betakit.com/rebranded-daylight-automation-raises-15-7-million-cad-in-series-a-funding/"
CLEANMAX_CAP = "https://stockanalysis.com/quote/nse/CLEANMAX/market-cap/"

FORBES_NETAMBIT = NEWS("netambit", "Building Business From a Telephone")
CB_RELISH = NEWS("relish", "Relish Secures $5M Series A")
FG_ZENSKAR_A = NEWS("zenskar", "Zenskar raises $15m Series A for agentic")
PRN_MALACHYTE = NEWS("malachyte", "Ex-Spotify Team Raises $10M for Malachyte")
ZOOMIN_POST = POST("zoomin-raises-a-total")
WIKI_DEEPSCALE = W("DeepScale")

lines = [
    cls("oxagen", status="defunct", stage="Growth", stage_src="model", stage_conf="medium",
        rounds=[rnd("2005-05", "later round", None, None, True, None, "press")],
        note="Second pass: Companies House shows Oxagen Limited (03246469) dissolved on 2 February 2024 after "
             "liquidation, so defunct. Bessemer entered in the May 2005 financing of a company venture-funded since "
             "1997, a later round (from memory, medium confidence), read Growth."),
    cls("wize", stage="Series A", stage_src="web_verified", stage_cite=TC_WIZE, stage_conf="medium",
        city="Burlingame", city_src="web_verified",
        rounds=[rnd("2007-01-21", "first round of financing", 4000000, None, True, TC_WIZE, "press")],
        note="Second pass: TechCrunch (2007-01-21) reports the company's first round of financing, $4M from Mayfield "
             "and Bessemer, read Series A as the first institutional round; the firm's own year 2006 stays the entry "
             "date. TechCrunch (2010-07-07) places Wize in Burlingame at the NexTag sale."),
    cls("netambit", status="private", stage="Series A", stage_src="web_verified", stage_cite=FORBES_NETAMBIT,
        stage_conf="medium", city="Noida",
        rounds=[rnd("2007", "first round", None, "Bessemer Venture Partners", True, FORBES_NETAMBIT, "press"),
                rnd("2009", "second round", None, None, True, FORBES_NETAMBIT, "press")],
        note="Second pass: Forbes India (2010-06-17) gives the whole outside funding as Rs 15 crore from Bessemer in "
             "2007 and Rs 50 crore from Bessemer and Helion in 2009, so the firm's September 2007 investment was the "
             "first institutional round, read Series A (the article does not use the label). Still operating as "
             "NetAmbit Group in 2026 (press), so private; Noida from memory."),
    cls("alnara-pharmaceuticals", stage="Series A", stage_src="model", stage_conf="medium",
        rounds=[rnd("2008-10", "Series A", 20000000, None, True, None, "press")],
        note="Second pass: Bessemer joined the $20M Series A of October 2008 with Third Rock, MPM and Frazier (from "
             "memory, medium confidence; the firm's own date is 2008-10-03). Lilly's release of July 2010 names "
             "Bessemer among the investors and places Alnara in Cambridge, Massachusetts."),
    cls("goodmail", status="defunct", stage="Growth", stage_src="model", stage_conf="medium", city="Mountain View",
        rounds=[rnd("2008", "Series D", 20000000, "Bessemer Venture Partners", True, None, "press")],
        note="Second pass: Bessemer led the $20M round of 2008, the company's fourth (Series D), after DCM, Emergence "
             "and Softbank had funded it (from memory, medium confidence), read Growth. Goodmail Systems shut down in "
             "February 2011 after a sale fell through (from memory; the news search returned no page), so defunct; "
             "city corrected to Mountain View."),
    cls("sweetlabs-inc-fmr-opencandy", status="private", stage="Series A", stage_src="web_verified",
        stage_cite=TC_OPENCANDY, stage_conf="medium",
        rounds=[rnd("2008", "Series A", 3500000, None, True, TC_OPENCANDY, "press"),
                rnd("2010-04-21", "Series B", 5000000, "Google Ventures", True, TC_OPENCANDY, "press")],
        note="Second pass: TechCrunch (2010-04-21) reports the $5M Series B led by Google Ventures with existing "
             "investors Bessemer and O'Reilly AlphaTech, after a $3.5M Series A in 2008; the firm's own date of "
             "2008-09-12 is that Series A. The company's site was live on 2026-10-06 and no sale was found, so "
             "private, as in the GV book."),
    cls("crowdflower", stage="Series A", stage_src="web_verified", stage_cite=TC_CROWDFLOWER, stage_conf="high",
        rounds=[rnd("2010-01-20", "Series A", 5000000, "Trinity Ventures and Bessemer Venture Partners", True,
                    TC_CROWDFLOWER, "press")],
        note="Second pass: TechCrunch (2010-01-20) reports $5M in Series A funding led by Trinity Ventures and "
             "Bessemer, after a $1.2M angel round without Bessemer; the firm's own date of 2009-12-08 stays the entry "
             "date. Wikipedia (Figure Eight Inc.) confirms the sale to Appen in March 2019."),
    cls("xtreme-power", stage="Growth", stage_src="web_verified", stage_cite=TC_XTREME, stage_conf="high",
        rounds=[rnd("2010-07-27", "Series C", 29500000,
                    "Bessemer Venture Partners, Dow's venture arm and SAIL Venture Partners", True, TC_XTREME,
                    "press")],
        note="Second pass: TechCrunch (2010-07-27) reports a $29.5M Series C co-led by Bessemer, Dow Chemical's "
             "venture arm and SAIL Venture Partners, read Growth."),
    cls("kroll-bond-ratings",
        rounds=[rnd("2010", "start-up round", 24000000, None, True, W("Kroll Bond Rating Agency"), "press")],
        note="Second pass: Wikipedia (Jules Kroll) says the agency was started with capital from named individuals "
             "and that Bessemer, RRE and New Markets invested $24 million; no source read labels that round, so the "
             "stage stays undetermined."),
    cls("clean-max-energy-solutions", status="public", rng="1b_plus", usd=1697275061, val_src="web_verified",
        val_cite=CLEANMAX_CAP, asof="2026-10-06", val_conf="high", rounds=[],
        note="Second pass: this is Clean Max Enviro Energy Solutions (Mumbai), now a listed renewable power producer "
             "(NSE: CLEANMAX, trading since March 2026); a Venture Intelligence item seen only as a search summary "
             "lists Bessemer first among its investors, from May 2011. Market cap INR 163.66B @ ECB 2026-10-06 "
             "(INR/EUR 108.6615, EUR/USD 1.1269) = $1.70B (stockanalysis.com). The round Bessemer entered in 2011 is "
             "not named by any source read."),
    cls("mojave-networks", city="San Mateo",
        rounds=[rnd("2013-11", "undetermined", 5000000, "Bessemer Venture Partners", True, TC_MOJAVE, "press")],
        note="Second pass: TechCrunch (2013-11-24) says Mojave raised $5M the week before in a round led by Bessemer "
             "with Sequoia, without naming the round, and the firm's own date (2013-03-12) is eight months earlier; "
             "the entry round stays undetermined. City San Mateo, California, from memory."),
    jl.verdict("vts", "not_member",
               "Sale consideration (decisions.md R6, Erik 2026-09-22): Bessemer's holding in VTS is the stock it "
               "received for Hightower, which VTS absorbed in the all-stock merger announced 2016-11-29 (The Real "
               "Deal, 'VTS, Hightower merge in landmark CRE tech deal'; WSJ, 'Real Estate Tech Companies VTS and "
               "Hightower to Merge in $300 Million Deal'; headlines only, both pages are walled). The firm's own "
               "live listing calls the company 'View The Space (Fmr Hightower)' and dates it 2013, the year of the "
               "Hightower seed; Hightower is the row. No VTS round names Bessemer: the $90M Series D of May 2019 "
               "lists Brookfield, GLP, Tishman Speyer and Fifth Wall (Crunchbase News, read). The live-site row "
               "view-the-space-fmr-hightower is the same company and the same reading applies to it.",
               ec="web", conf="medium", cite=NEWS("vts", "VTS, Hightower merge in landmark")),
    cls("helloshopper", stage="Seed", stage_src="web_verified", stage_cite=TC_SCRATCH, stage_conf="high",
        city="Boston", city_src="web_verified",
        rounds=[rnd("2015-07-14", "seed", 3600000, "Bessemer Venture Partners", True, TC_SCRATCH, "press")],
        note="Second pass: TechCrunch (2015-07-14) reports Scratch, the company's earlier name, with $3.6M in seed "
             "funding in a round led by Bessemer and a team in Boston; the firm's own date of 2014-09-11 stays the "
             "entry date. Its later fate is still not found. Graduation left for the graduation pass."),
    cls("verato", stage="Series A", stage_src="web_verified", stage_cite=MEDCITY_VERATO, stage_conf="high",
        rounds=[rnd("2015-01", "Series A", 12500000, None, True, MEDCITY_VERATO, "press"),
                rnd("2017-02", "Series B", 12500000, "Bessemer Venture Partners and Columbia Capital", True,
                    MEDCITY_VERATO, "press")],
        note="Second pass: MedCity News (February 2017) says Bessemer and Columbia Capital, co-leads of the $12.5M "
             "Series B, had both participated in the Series A, a $12.5M round that closed in January 2015; that "
             "matches the firm's own date of 2015-01-14."),
    cls("stratim", stage="Growth", stage_src="web_verified", stage_cite=TC_ZIRX, stage_conf="high",
        rounds=[rnd("2015-04-22", "Series B", 30000000, "Bessemer Venture Partners", True, TC_ZIRX, "press")],
        note="Second pass: TechCrunch (2015-04-22) reports ZIRX, the company's earlier name, raising $30M in Series B "
             "funding led by Bessemer, with Norwest and Trinity as the existing investors, read Growth. Acquired by "
             "KAR Auction Services in February 2018 (TechCrunch, 2018-02-07). The zirx row is the same company and "
             "should be merged into this one."),
    cls("deepscale", stage="Seed", stage_src="web_verified", stage_cite=TC_DEEPSCALE, stage_conf="high",
        grad="graduated", grad_src="web_verified", grad_cite=WIKI_DEEPSCALE, grad_conf="high",
        rounds=[rnd("2017-03-21", "seed", 3000000, None, True, TC_DEEPSCALE, "press"),
                rnd("2018", "Series A", 15000000, None, None, WIKI_DEEPSCALE, "press")],
        note="Second pass: TechCrunch (2017-03-21) reports $3M in seed funding with Bessemer among the seed "
             "investors; the firm's own date of 2016-11-14 stays the entry date. Graduated: Wikipedia records a $15M "
             "Series A in 2018, and Tesla bought the company on 2019-10-01."),
    cls("zoomin", stage="Series A", stage_src="first_party", stage_cite=ZOOMIN_POST, stage_conf="medium",
        entry_date="2018",
        rounds=[rnd("2018", "first round", None, "Bessemer Venture Partners", True, ZOOMIN_POST, "firm"),
                rnd("2020-12-16", "Series B", 14000000, None, True, CALCALIST_ZOOMIN_B, "press")],
        note="Second pass: the firm's own post (2020-12-16) says Bessemer was the first investor in Zoomin, a company "
             "bootstrapped until 2018, and Calcalist (December 2020) calls the next round, $14M with Bessemer taking "
             "part, the Series B; the firm's first round is therefore read Series A. First Round's Zoomin is another "
             "company (a name collision)."),
    cls("relish", stage="Series A", stage_src="web_verified", stage_cite=CB_RELISH, stage_conf="high",
        entry_date="2020-04", city="New York", city_src="web_verified",
        rounds=[rnd("2018-10", "venture round", 2200000, None, None, CB_RELISH, "press"),
                rnd("2020-04-27", "Series A", 5000000, "Bessemer Venture Partners", True, CB_RELISH, "press")],
        note="Second pass: Crunchbase News (2020-04-27) reports a $5M Series A led by Bessemer with previous "
             "investors Trinity Ventures and Bullpen Capital, after a $2.2M round in October 2018 that does not name "
             "Bessemer. AlleyWatch (October 2019) places the company in New York. Its site was still up on 2026-10-06 "
             "with a 2020 copyright line and no later news was found, so the status stays unknown."),
    cls("fold", stage="Series A", stage_src="web_verified", stage_cite=FOLD_BLOG, stage_conf="high",
        entry_date="2021-05",
        rounds=[rnd("2021-05-27", "Series A", 13000000, "Craft Ventures", True, FOLD_BLOG, "company")],
        note="Second pass: Fold's own announcement (2021-05-27) reports a $13M Series A led by Craft Ventures with "
             "M13, Slow Ventures and Bessemer taking part; the firm dates its entry 2021 and no earlier round names "
             "it."),
    cls("zenskar", stage="Seed", stage_src="web_verified", stage_cite=TC_ZENSKAR, stage_conf="high",
        entry_date="2022-10", grad="graduated", grad_src="web_verified", grad_cite=FG_ZENSKAR_A, grad_conf="high",
        rounds=[rnd("2022-10-03", "seed", 3500000, "Bessemer Venture Partners", True, TC_ZENSKAR, "press"),
                rnd("2026-04-20", "Series A", 15000000,
                    "Susquehanna Venture Capital, Bessemer Venture Partners, Shine Capital and Rho", True,
                    FG_ZENSKAR_A, "press")],
        note="Second pass: TechCrunch (2022-10-03) reports a $3.5M seed round led by Bessemer with Shine Capital, "
             "Basecamp Fund and Converge. Graduated: FinTech Global (2026-04-20) reports a $15M Series A led by "
             "Susquehanna, Bessemer, Shine Capital and Rho."),
    cls("daylight", status="acquired", stage="Seed", stage_src="web_verified", stage_cite=BETAKIT_DAYLIGHT,
        stage_conf="medium", entry_date="2020-03", grad="graduated", grad_src="web_verified",
        grad_cite=BETAKIT_DAYLIGHT, grad_conf="high",
        rounds=[rnd("2020-03", "seed", 2260000, None, True, BETAKIT_DAYLIGHT, "press"),
                rnd("2021-09-21", "Series A", 12300000, "RTP Global, Bessemer Venture Partners and Golden Ventures",
                    True, BETAKIT_DAYLIGHT, "press")],
        note="Second pass: BetaKit (2021-09-21) says Bessemer and Golden Ventures invested in the $2.26M round of "
             "March 2020, which the co-founder calls the seed round, and co-led the $12.3M Series A of September "
             "2021, so Seed and graduated. Quadient acquired Daylight Automation in September 2023 (Quadient's "
             "announcement of 2023-09-18, read on MarTech Series), so acquired."),
    cls("malachyte", stage="Seed", stage_src="web_verified", stage_cite=PRN_MALACHYTE, stage_conf="medium",
        grad="censored",
        rounds=[rnd("2026-08-06", "seed", 10000000, "Bessemer Venture Partners and Gradient", True, PRN_MALACHYTE,
                    "company")],
        note="Second pass: the company's release (PR Newswire, 2026-08-06) announces a $10M seed round co-led by "
             "Bessemer and Gradient with Harpoon Ventures; it is the only round on record and the firm dates its "
             "partnership 2024, kept as the entry date. Censored: the entry is inside the 24 month window."),
]

jl.write("s22b", lines)
