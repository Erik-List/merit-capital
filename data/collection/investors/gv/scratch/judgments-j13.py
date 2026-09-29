"""PRO-75 grind, judge j13: queue batch 13 (StatusPRO to TScan Therapeutics), 45 member rows.
Pattern copied from judgments-pilot.py. Citations come from the helpers (NEWS, CASE, POST, SITE, W, FTS) or are pages
read in this pass (WebFetch or curl) and named in the note; sibling books' pages were read before reuse."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS, CASE = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH,
                                                            jl.W, jl.NEWS, jl.FTS, jl.CASE)
L = []
WV = {"valuation_range_source": "web_verified"}
TODAY = "2026-09-28"


def cap(ticker):
    """stockanalysis.com market-cap page (read with curl on 2026-09-28)."""
    return f"https://stockanalysis.com/stocks/{ticker}/market-cap/"


# ---------------------------------------------------------------- StatusPRO
SP_A = NEWS("statuspro", "STATUSPRO ANNOUNCES")
L.append(cls("statuspro", status="private", rng="below_1b", country="US", city="Miami", city_src="web_verified",
             focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=SP_A, entry_date="2024-02-05",
             note="Sports XR game studio (NFL Pro Era), Miami. The company's release (PR Newswire, 2024-02-05) announces "
                  "a $20M Series A led by GV, with Dream Sports, Wise Ventures and Alumni Ventures and existing backers "
                  "(LeBron James, Drake, Maverick Carter), GV not among them; the firm's listing first carries the "
                  "company in 2024. An earlier $5.2M raise (Refresh Miami headline, August 2021) is not tied to GV. "
                  "Private; no priced round near $1B. Not in the momentum slice (gaming).",
             rounds=[rnd("2024-02-05", "Series A", 20000000, "GV", True, SP_A, "company")]))

# ---------------------------------------------------------------- StockX
SX_B = NEWS("stockx", "Co-Led by GV")
SX_VAL = W("StockX")
L.append(cls("stockx", status="private", rng="1b_plus", usd=3800000000, val_src="web_verified", val_cite=SX_VAL,
             asof="2021-04-08", city="Detroit", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SX_B, entry_date="2018-09-13",
             flags=("stale",), clear=("unicorn_name_match",), extra=WV,
             note="Resale marketplace for sneakers and streetwear, Detroit. GV co-led the $44M Series B with Battery "
                  "Ventures (the company's release, PR Newswire, 2018-09-13); the firm's case study also gives 'First "
                  "Round: Series B', invested 2018. Series C $110M at $1B (June 2019, DST Global, General Atlantic, GGV; "
                  "headlines). Mark: the $255M round of April 2021 at more than $3.8B (Reuters as quoted by Wikipedia); "
                  "no later priced round found, so the 2021 mark stands, flagged stale. Pinned from the unicorn "
                  "list's name match to a cited event; aligned with Battery's row (Detroit, Growth).",
             rounds=[rnd("2018-09-13", "Series B", 44000000, "GV; Battery Ventures", True, SX_B, "company"),
                     rnd("2019-06", "venture round at $1B ($110M)", 110000000, None, True, SX_VAL, "press"),
                     rnd("2021-04-08", "late-stage round", 255000000, None, None, SX_VAL, "press")]))

# ---------------------------------------------------------------- Strella Biotechnology
ST_A = NEWS("strella-biotechnology", "Closes $8M Series A")
L.append(cls("strella-biotechnology", status="private", rng="below_1b", country="US", city="Seattle",
             city_src="web_verified", focus="Climate & Energy",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ST_A, entry_date="2022-06-08",
             note="Sensors and software that predict produce ripeness to cut food waste. The $8M Series A (June 2022) "
                  "was led by Millennium New Horizons with Google Ventures, Rich Products Ventures, Mark Cuban, Union "
                  "Labs, Catapult and Yamaha (Global AgInvesting); the $3.3M seed of May 2020 was co-led by Catapult "
                  "and Yamaha with Mark Cuban and Union Labs and names no GV, so GV entered at the Series A (the "
                  "firm's listing first carries it in 2022). Moved from Philadelphia to Seattle in 2022 (Business "
                  "Journals headline); the company's own site gives 119 Pine St, Seattle and is live. General "
                  "Catalyst's row still says Philadelphia: this row holds the fresher cited address.",
             rounds=[rnd("2020-05", "Seed", 3300000, "Catapult Ventures; Yamaha Motor Ventures", False, ST_A, "press"),
                     rnd("2022-06-08", "Series A", 8000000, "Millennium New Horizons", True, ST_A, "press")]))

# ---------------------------------------------------------------- Stripe
STRIPE_VAL = "https://stripe.com/newsroom/news/stripe-2025-update"
L.append(cls("stripe", status="private", rng="100b_plus", usd=159000000000, val_src="web_verified",
             val_cite=STRIPE_VAL, asof="2026-02-24", city="South San Francisco", focus="Fintech & Payments",
             stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=CASE("stripe"), entry_date="2016",
             flags=("model_disputes_source",), extra=WV,
             note="Payments infrastructure, dual-headquartered in South San Francisco and Dublin (Wikipedia). The "
                  "pre-filled 'acquired' is a Wikidata name join and is disputed: Stripe is private and operating. "
                  "Mark: the employee tender at $159B announced 2026-02-24 (Stripe's own newsroom). Entry: the firm's "
                  "case study gives 'First Round: Series D', invested 2016, so Growth. City follows the majority of "
                  "sibling books (South San Francisco; three books say San Francisco). Not in the momentum slice "
                  "(listed since 2016).",
             rounds=[rnd("2016", "Series D", None, None, True, CASE("stripe"), "firm"),
                     rnd("2026-02-24", "tender offer", None, None, None, STRIPE_VAL, "company")]))

# ---------------------------------------------------------------- Synthesia
SY_E = NEWS("synthesia", "Google Ventures-led series E")
L.append(cls("synthesia", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified", val_cite=SY_E,
             asof="2026-01", country="GB", country_src="web_verified", country_cite=W("Synthesia (company)"),
             city="London", focus="AI & Applied AI",
             stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=CASE("synthesia"),
             entry_date="2021-11", flags=("model_disputes_source",), extra=WV,
             note="AI video generation, London (Synthesia Limited, Wikipedia). The pre-filled 'acquired' and CZ are a "
                  "Wikidata join on the one-word name (a Czech namesake) and are disputed. Entry: the firm's case study "
                  "gives 'First Round: Series B' (invested 2021) and its /ai list 'Invested 2021-11'; Wikipedia: the "
                  "$50M Series B of December 2021 was led by Kleiner Perkins and GV. GV re-invested in 2023 and "
                  "December 2024 and led the $200M Series E at $4B in January 2026 (Silicon Republic). Momentum check "
                  "2026-09-28: the January 2026 Series E is the latest priced round found. Aligned with Accel's row "
                  "($4B, 2026-01, London, GB).",
             rounds=[rnd("2021-12", "Series B", 50000000, "Kleiner Perkins; GV", True, W("Synthesia (company)"), "press"),
                     rnd("2023-06", "Series C", 90000000, "Accel", True, W("Synthesia (company)"), "press"),
                     rnd("2025-01", "Series D", 180000000, "NEA", True, W("Synthesia (company)"), "press"),
                     rnd("2026-01", "Series E", 200000000, "GV", True, SY_E, "press")]))

# ---------------------------------------------------------------- Thinking Machines Lab
TML_SEED = "https://techcrunch.com/2025/07/15/mira-muratis-thinking-machines-lab-is-worth-12b-in-seed-round/"
L.append(cls("thinking-machines-lab", status="private", rng="10b_plus", usd=12000000000, val_src="web_verified",
             val_cite=TML_SEED, asof="2025-07-15", city="San Francisco", focus="AI & Applied AI",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TML_SEED, entry_date="2025-07",
             grad="censored", clear=("unicorn_name_match",), extra=WV,
             note="Frontier AI lab founded by Mira Murati, San Francisco (Wikipedia). The firm's /ai list gives one "
                  "round, 'Invested 2025-07', and the only round the company closed that month is the $2B seed at "
                  "$12B led by Andreessen Horowitz (TechCrunch, 2025-07-15), so the entry is named from the record "
                  "(model, medium): TechCrunch's investor list does not name GV. Mark pinned to that round (the "
                  "unicorn list's figure, now cited). Momentum check 2026-09-28: talks at $50B (November 2025) and "
                  "a reported $1B round at $40B led by Accel (September 2026) are not closed rounds, so no later "
                  "mark. Entry 2025-07 is inside 24 months: censored. Aligned with a16z's row (Seed, $12B, "
                  "San Francisco).",
             rounds=[rnd("2025-07-15", "Seed", 2000000000, "Andreessen Horowitz", True, TML_SEED, "press")]))

# ---------------------------------------------------------------- ThousandEyes
TE_W = W("ThousandEyes")
L.append(cls("thousandeyes", rng="below_1b", city="San Francisco", focus="Data Infrastructure",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TE_W, entry_date="2016",
             note="Network intelligence platform, San Francisco. Wikipedia: Sequoia led the 2011 Series A, Sutter Hill "
                  "the 2014 Series B, and 'In 2016, Tenaya Capital and GV joined a Series C round' ($35M); GV then led "
                  "the $50M Series D (February 2019). The firm's own post (2020-05-28) says its partner first met the "
                  "founders in 2015, consistent with a 2016 entry. Acquired by Cisco (announced May 2020, closed "
                  "August 2020, reported near $1B; the firm's exit line 'Acquired by Cisco, 2020'), so below_1b by "
                  "the acquired-row rule. Aligned with Sutter Hill and Sequoia (acquired, San Francisco).",
             rounds=[rnd("2011", "Series A", 5500000, "Sequoia Capital", False, TE_W, "press"),
                     rnd("2014", "Series B", 20000000, "Sutter Hill Ventures", False, TE_W, "press"),
                     rnd("2016", "Series C", 35000000, None, True, TE_W, "press"),
                     rnd("2019-02", "Series D", 50000000, "GV", True, TE_W, "press")]))

# ---------------------------------------------------------------- theSkimm
SK_W = W("The Skimm")
L.append(cls("theskimm", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Media, Gaming & Advertising",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SK_W, entry_date="2018-03-15",
             note="Subscription news newsletter and media company, New York. Wikipedia: an $8M Series B in June 2016, "
                  "then 'On March 15, 2018, theSkimm raised a $12 million funding round led by Google Ventures'; the "
                  "firm's listing first carries the company in 2018, so GV entered after the Series B: Growth. "
                  "Acquired by Everyday Health Group (Ziff Davis) in March 2025 (Wikipedia; Axios and Inc. headlines; "
                  "the firm's exit line 'Acquired by Everyday Health, 2025').",
             rounds=[rnd("2016-06", "Series B", 8000000, None, None, SK_W, "press"),
                     rnd("2018-03-15", "unnamed ($12M, after the Series B)", 12000000, "GV", True, SK_W, "press")]))

# ---------------------------------------------------------------- Translucent AI
TR_POST = POST("translucent-ai-healthcare")
L.append(cls("translucent-ai", status="private", rng="below_1b", country="US", city="New York",
             city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=TR_POST, entry_date="2026-03",
             note="Agentic AI platform for hospital and physician-group finance (healthcare's 'financial operating "
                  "system'). The firm's own post (2026-03-11): 'GV is leading the Series A for Translucent' and "
                  "'welcome them to the GV family', with the team in NYC; the company's site: 'We raised a $27M "
                  "Series A led by GV'. The /ai list gives 'Invested 2026-03'. Healthcare vertical software, so "
                  "Healthcare & Bio. The company's $7M seed of August 2025 (FinSMEs and Business Wire headlines) names "
                  "no GV, and the post presents the Series A as GV's arrival. Momentum check 2026-09-28 (Google News "
                  "for the company): the March 2026 Series A is the latest round.",
             rounds=[rnd("2026-03", "Series A", 27000000, "GV", True, TR_POST, "firm")]))

# ---------------------------------------------------------------- TScan Therapeutics
TS_S1 = FTS("TScan", "S-1")
L.append(cls("tscan-therapeutics", status="public", rng="below_1b", usd=23040000, val_src="web_verified",
             val_cite=cap("tcrx"), asof=TODAY, country="US", city="Waltham", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TS_S1, entry_date="2018",
             extra=WV,
             note="TCR-engineered T cell therapies (NASDAQ: TCRX), Waltham MA. The S-1's related-party table: "
                  "'Entities affiliated with GV' bought 5,263,158 Series A shares for $5.0M in the Series A sold in "
                  "June and December 2018, then Series B (2019) and Series C (January 2021) shares. Market cap $23.04M "
                  "on 2026-09-28 (stockanalysis.com), replacing the June 2025 float.",
             rounds=[rnd("2018", "Series A", 25000000, None, True, TS_S1, "filing"),
                     rnd("2019", "Series B", 35000000, None, True, TS_S1, "filing"),
                     rnd("2021-01", "Series C", 100000000, None, True, TS_S1, "filing")]))

# ---------------------------------------------------------------- Toast
TO_B = "https://www.prnewswire.com/news-releases/toast-the-leading-restaurant-pos-company-raises-30-million-in-series-b-funding-to-fuel-growth-300199296.html"
L.append(cls("toast", status="public", rng="10b_plus", usd=17560000000, val_src="web_verified", val_cite=cap("tost"),
             asof=TODAY, city="Boston", focus="Fintech & Payments",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TO_B, entry_date="2016-01-05",
             extra=WV,
             note="Restaurant point-of-sale and payments platform (NYSE: TOST), Boston. The company's release "
                  "(PR Newswire, 2016-01-05): a $30M Series B 'led by Bessemer Venture Partners with participation from "
                  "GV', and 'Toast looks forward to working with Rich Miner ... general partner at GV, who led the "
                  "investment for the fund', so GV entered at the Series B (the firm's listing first carries Toast in "
                  "2016; the IPO-era agreements name GV 2014 and GV 2017 vehicles, and GV filed 13G holdings in 2022-23). "
                  "Market cap $17.56B on 2026-09-28 (stockanalysis.com), replacing the June 2025 float.",
             rounds=[rnd("2016-01-05", "Series B", 30000000, "Bessemer Venture Partners", True, TO_B, "company")]))

# ---------------------------------------------------------------- Tracelytics
TL_SEED = "https://techcrunch.com/2011/11/03/web-app-performance-solution-tracelytics-raises-600k-from-google-ventures-battery-flybridge/"
L.append(cls("tracelytics", status="acquired", rng="below_1b", country="US", city="Providence",
             city_src="web_verified", focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TL_SEED, entry_date="2011-11-03",
             note="Application performance tracing for distributed web apps, Providence RI. TechCrunch (2011-11-03): a "
                  "$600,000 seed from Battery Ventures, Flybridge Capital Partners, Google Ventures and angels, the "
                  "company's first disclosed funding (founded June 2010). Bain Capital Ventures then invested $5.2M "
                  "in March 2012 (its Form D, per BCV's row), a later priced round above the seed-era $5M bar; "
                  "AppNeta acquired the company in 2012 (the firm's exit line). Graduation left for the graduation "
                  "pass. Aligned with BCV's row (acquired, Providence).",
             rounds=[rnd("2011-11-03", "Seed", 600000, None, True, TL_SEED, "press")]))

# ---------------------------------------------------------------- tenXer
TX_ACQ = "https://techcrunch.com/2015/04/02/confirmed-twitter-buys-tenxer-for-under-50m-to-improve-its-tools-for-engineers/"
L.append(cls("tenxer", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="undetermined",
             note="Engineering productivity analytics, San Francisco. TechCrunch (2015-04-02): Twitter bought tenXer for "
                  "under $50M; 'The company had raised about $5 million with investors including True Ventures, "
                  "Google Ventures and Khosla', with no round named. Google News for the company returned no funding "
                  "announcement. No source ties GV to a named round, so the stage is undetermined (Khosla's row "
                  "reads Seed off the same article). Acquired, aligned with Khosla's row (San Francisco).",
             rounds=[rnd(None, "undisclosed (about $5M raised in total)", 5000000, None, True, TX_ACQ, "press")]))

# ---------------------------------------------------------------- Swell (Concept.io)
SW_A = "https://techcrunch.com/2013/07/18/swell-series-a/"
SW_ACQ = "https://techcrunch.com/2014/07/28/apple-to-buy-swell-for-30-million-per-report/"
L.append(cls("swell", status="acquired", rng="below_1b", country="US", city="Mountain View", city_src="web_verified",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SW_A, entry_date="2012",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=SW_A,
             note="Personalised news and talk radio app by Concept.io. TechCrunch (2013-07-18): 'Swell previously "
                  "raised a $1.8 million seed round from Google Ventures, Charles River Ventures, DFJ, Andreessen "
                  "Horowitz' and others, and a $5.4M Series A 'led by Draper Fisher Jurvetson, with participation from "
                  "Google Ventures', so GV entered at the seed and the named Series A graduates it. TechCrunch "
                  "(2014-07-28): Concept.io was 'founded back in 2012 in Mountain View', its seed 'was led by CRV and "
                  "Andreessen Horowitz in 2012' (the entry date), and Apple bought Swell and its team for about $30M; "
                  "the app shut down (Fast Company headline). Status and stage align with a16z's row; its city (Palo "
                  "Alto) differs from the Mountain View this row cites. First Round's 'Swell' (defunct, New York, "
                  "2017 listing) is a different company of the same name.",
             rounds=[rnd("2012", "Seed", 1800000, "CRV; Andreessen Horowitz", True, SW_ACQ, "press"),
                     rnd("2013-07-18", "Series A", 5400000, "Draper Fisher Jurvetson", True, SW_A, "press")]))

# ---------------------------------------------------------------- Synack
SN_W = W("Synack")
L.append(cls("synack", status="private", rng="below_1b", city="Redwood City", focus="Security",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=SN_W, entry_date="2014-04",
             note="Crowdsourced penetration testing, Redwood City (Wikipedia). Wikipedia: 'In April 2014, the company "
                  "announced it had secured Series A funding from Kleiner Perkins Caufield Byers, Google Ventures, "
                  "Allegis Capital, and Derek Smith'; the Business Journals headline gives the round as $7.5M led by "
                  "Kleiner Perkins (2014-04-24). The firm's listing first carries Synack in 2014 and its /ai list "
                  "records re-investments in March 2017 and March 2020. Later rounds: $25M Series B (February 2015), "
                  "$21M (April 2017, Fortune headline), $52M (May 2020, Business Wire headline); no mark near $1B.",
             rounds=[rnd("2014-04", "Series A", None, None, True, SN_W, "press"),
                     rnd("2015-02", "Series B", 25000000, None, None, SN_W, "press")]))

# ---------------------------------------------------------------- The Climate Corporation
CC_B = "https://techcrunch.com/2007/10/17/an-interesting-bet-weatherbill-takes-125-million-series-b/"
L.append(cls("the-climate-corporation", rng="below_1b", city="San Francisco", focus="Climate & Energy",
             stage="Growth", stage_src="model", stage_conf="medium", stage_cite=CC_B,
             note="Weather insurance, then farm data science (WeatherBill until 2011), San Francisco. TechCrunch "
                  "(2007-10-17): WeatherBill's $12.5M Series B, led by NEA and Index Ventures. Google Ventures was "
                  "founded in 2009 (the firm's own 'EST. 2009'), so any GV entry came in a later round: Growth, "
                  "though no source read names the round or its date (model, medium). Acquired by Monsanto in "
                  "October 2013 for about $1.1B (Wikipedia; the firm's exit line 'Acquired by Monsanto, 2013'), so "
                  "below_1b by the acquired-row rule. Aligned with the sibling books (acquired, San Francisco).",
             rounds=[rnd("2007-10-17", "Series B", 12500000, "NEA; Index Ventures", False, CC_B, "press")]))

# ---------------------------------------------------------------- Tennr
TN_C = NEWS("tennr", "Healthcare referrals are where patients get lost")
L.append(cls("tennr", status="private", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TN_C, entry_date="2025-06-18",
             note="AI that automates patient referral intake (faxes, documents) for specialty providers, New York. The "
                  "company's release (PR Newswire, 2025-06-18): 'a $101 million Series C led by IVP, with participation "
                  "from new and existing investors including Andreessen Horowitz, Lightspeed, GV, ICONIQ'; the firm's "
                  "/ai list gives a single 'Invested 2025-06', so GV entered at the Series C: Growth. Fortune's headline "
                  "puts the round at a $605M valuation. Momentum check 2026-09-28 (Google News for the company): no "
                  "later round, so below_1b. Aligned with a16z, IVP and Lightspeed (private, New York).",
             rounds=[rnd("2025-06-18", "Series C", 101000000, "IVP", True, TN_C, "company")]))

# ---------------------------------------------------------------- Tala (formerly InVenture)
TA_SEED = "https://techcrunch.com/2014/03/14/inventure"
TA_A = "https://globalventuring.com/inventure-accounts-for-10m-series-a/"
L.append(cls("tala", status="private", rng="below_1b", country="US", city="Santa Monica", focus="Fintech & Payments",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TA_SEED, entry_date="2014-03",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TA_A,
             flags=("model_disputes_source",),
             note="Mobile credit scoring and lending in emerging markets (InVenture until its rename to Tala), "
                  "headquartered in Santa Monica (Wikipedia, 'Tala Finance'). The pre-filled DZ is a Wikidata join on "
                  "the one-word name and is disputed. TechCrunch (2014-03-14): 'a $1.2 million seed round led by Chris "
                  "Sacca's Lowercase Capital. Other investors in that round include Google Ventures'; the firm's 2014 "
                  "listing names InVenture. Global Venturing (2015-09-22): a $10M Series A 'from a consortium including "
                  "Google Ventures', so the seed graduated. Later rounds (per Ribbit's row): IVP-led $30M Series B "
                  "(2017), $145M Series E (2021, enterprise value above $800M); no priced round at $1B found. City: "
                  "Ribbit says Santa Monica and IVP Los Angeles; Wikipedia gives Santa Monica. Seed date read off the "
                  "TechCrunch report (March 2014). (Tala Health, the $1.2B AI health startup of 2025, is a different "
                  "company.)",
             rounds=[rnd("2014-03", "Seed", 1200000, "Lowercase Capital", True, TA_SEED, "press"),
                     rnd("2015-09", "Series A", 10000000, None, True, TA_A, "press")]))

# ---------------------------------------------------------------- Tend
TD_CEO = NEWS("tend", "Troy Bage")
TD_B = NEWS("tend", "Tend Raises $37M Series B Led By GV")
L.append(cls("tend", status="private", rng="below_1b", city="Nashville", city_src="formd_address",
             focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TD_B, entry_date="2020-10-01",
             flags=("stage_disputes_band",),
             note="Dental studio chain (25 locations in New York, Washington DC, Boston, Atlanta, Nashville and "
                  "Connecticut). Entry: the company's release (New York, 2020-10-01), 'Tend Raises $37M Series B Led "
                  "By GV': '$37 million in new funding led by GV', with Juxtapose, Redpoint and Zigg named as the "
                  "existing investors, so GV entered at the Series B: Growth. The Form D band had dated the entry to "
                  "the 2024 filing where GV's Ben Robbins sits (a follow-on; the firm listed Tend from 2020), so its "
                  "date is replaced. A $125M Series C followed in April 2021 (Business Insider and Business Journals "
                  "headlines). HQ: the 2024 Form D gives the issuer and officers at 8 City Boulevard, Nashville, and "
                  "the company's release naming Troy Bage CEO is datelined Nashville (PR Newswire, 2023-08-14; 'based "
                  "out of Tend's Nashville hub'); Redpoint's row says New York, this row holds the fresher cited "
                  "address. Operating (the company's site, 2026); no priced round near $1B.",
             rounds=[rnd("2020-10-01", "Series B", 37000000, "GV", True, TD_B, "company")]))

# ---------------------------------------------------------------- Trada
TRD_C = "https://techcrunch.com/2010/07/21/trada-raises-5-75m-from-google-ventures-to-crowdsource-search-engine-marketing/"
L.append(cls("trada", status="defunct", rng="below_1b", city="Boulder", focus="Media, Gaming & Advertising",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TRD_C,
             flags=("stage_disputes_band",),
             note="Crowdsourced search and social advertising marketplace, Boulder. TechCrunch (2010-07-21): 'a $5.75 "
                  "million Series C round of funding led by Google Ventures, with participation from previous investor "
                  "Foundry Group', $7.95M raised in total; GV's Rich Miner sits on the July 2010 Form D. The Form D band "
                  "read that filing as a Seed; the press names it a Series C, so the entry is Growth (band disputed; the "
                  "seed-to-A column does not apply). A further $9M came in 2011 from Google Ventures and Foundry (Search "
                  "Engine Land headline). Daily Camera (2015-03-30): the creditors, who held Trada's assets as "
                  "collateral, 'have forced the provider of paid search advertising services to cease operations'; "
                  "the firm's live list no longer carries it (archived listings 2012-2015 only): defunct.",
             rounds=[rnd("2010-07-21", "Series C", 5750000, "Google Ventures", True, TRD_C, "press")]))

# ---------------------------------------------------------------- Thatch
TH_SEED = NEWS("thatch", "Thatch launches with funding from a16z and GV")
TH_A = "https://www.generalcatalyst.com/stories/our-investment-in-thatch"
TH_C = "https://www.prnewswire.com/news-releases/thatch-raises-108m-at-1b-valuation-as-employers-shift-away-from-traditional-health-plans-302879015.html"
L.append(cls("thatch", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=TH_C,
             asof="2026-09-15", country="US", city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TH_SEED, entry_date="2023-02-15",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TH_A,
             flags=("model_disputes_source",), clear=("unicorn_name_match",), extra=WV,
             note="Health-budget benefits platform (ICHRA) for employers, San Francisco. The firm's listing gives "
                  "thatch.ai, which redirects to thatch.com: the same company as General Catalyst's and Lux's Thatch "
                  "rows. The pre-filled GB is a name join on the one-word name and is disputed (US). Entry: the "
                  "company's launch release (PR Newswire, San Francisco, 2023-02-15): over $6M across a pre-seed and "
                  "a seed, and 'The company's seed round was led by a16z and GV' (GV's Krishna Yeshwant quoted); the "
                  "firm's listing first carries Thatch in 2023. Graduated: General Catalyst's post (2024-09-05) says it is "
                  "'co-leading a Series A investment'. Mark: the $108M Series C at a $1B valuation (the company's "
                  "release, San Francisco, 2026-09-15), led by The General Partnership, Index, General Catalyst and "
                  "a16z; pinned from the unicorn list's name match. Aligned with General Catalyst ($1B, 2026-09) and "
                  "Lux (Seed, graduated).",
             rounds=[rnd("2023-02-15", "Seed", None, "a16z; GV", True, TH_SEED, "company"),
                     rnd("2024-09-05", "Series A", None, "General Catalyst (co-lead)", None, TH_A, "firm"),
                     rnd("2026-09-15", "Series C", 108000000,
                         "The General Partnership; Index Ventures; General Catalyst; Andreessen Horowitz", None, TH_C,
                         "company")]))

# ---------------------------------------------------------------- Tessl
TS_POST = POST("guy-podjarny-interview-tessl")
TS_A = NEWS("tessl", "to build AI Native Software Development")
L.append(cls("tessl", status="private", rng="below_1b", city="London",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TS_A, entry_date="2024-04",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TS_A,
             focus="DevTools & APIs", flags=("stage_disputes_band",),
             note="AI-native software development platform, London (founder Guy Podjarny of Snyk). The company's "
                  "release (London, 2024-11-14): $125M in total, a previously unannounced $25M seed of April 2024 led by "
                  "boldstart ventures and GV, and a $100M Series A led by Index Ventures with Accel, GV and boldstart. "
                  "The firm's own post (2026-03-18) agrees: 'GV was a seed investor in Tessl in 2024'; its case study "
                  "gives 'First Round: Seed' and the /ai list 'Invested 2024-04' (the first Form D, $25.5M, is dated "
                  "2024-04-10 with Tom Hulme and boldstart's Ed Sim as directors). The Form D band read that filing as "
                  "a Series A; the release names it the seed, so the band is disputed. The named Series A graduates "
                  "the seed. Valuation reported at $500M+ (TechCrunch headline) or $750M (Fortune headline): "
                  "below_1b. Momentum check 2026-09-28 (Google News for the company): no later round.",
             rounds=[rnd("2024-04", "Seed", 25000000, "boldstart ventures; GV", True, TS_A, "company"),
                     rnd("2024-11-14", "Series A", 100000000, "Index Ventures", True, TS_A, "company")]))

# ---------------------------------------------------------------- TrueLens
TLN = "https://finance.yahoo.com/news/truelens-introduces-groundbreaking-customer-intelligence-145126832.html"
TLN_TC = "https://techcrunch.com/2012/12/03/truelens-google-ventures/"
L.append(cls("truelens", status="unknown", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             focus="SaaS", stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TLN,
             entry_date="2012-12-03",
             note="Marketing intelligence from social media data (Socialgraphics), founded in Boston. The company's "
                  "release (Marketwire, 2012-12-03) and TechCrunch the same day: a '$1.2 million funding round led by "
                  "Google Ventures' with Charles River Ventures, Common Angels, 500 Startups, Boston Seed and angels. "
                  "Neither names the round; a $1.2M round from seed funds and angels is read as the seed (model, "
                  "medium). Fate: truelens.com now redirects to an unrelated eyewear retailer; vendor profiles list an "
                  "acquisition by MarketingAudit in 2018, which no non-vendor source read confirms, so status is "
                  "unknown. Graduation left for the graduation pass.",
             rounds=[rnd("2012-12-03", "unnamed ($1.2M)", 1200000, "Google Ventures", True, TLN_TC, "press")]))

# ---------------------------------------------------------------- Transphorm
TP_W = W("Transphorm")
TP_FD = "https://www.sec.gov/Archives/edgar/data/1400017/000118143110024469/0001181431-10-024469-index.htm"
L.append(cls("transphorm", status="acquired", rng="below_1b", city="Goleta", focus="Industrial & Robotics",
             stage="undetermined",
             note="Gallium nitride power semiconductors, Goleta CA (a UCSB spin-out, founded 2007). GV's Wesley Chan "
                  "sits on the company's first electronic Form D (April 2010, $20.2M) beside Kleiner Perkins' Randy "
                  "Komisar and Foundation Capital's Richard Redelfs, so GV was in by then; Wikipedia says 'In 2011, "
                  "Google Ventures invested $20 million'. No source read names the round GV entered (earlier 2007-09 "
                  "money is on no electronic filing), so the stage is undetermined. Renesas agreed to buy the company "
                  "for $339M in January 2024 and completed the purchase on 2024-06-20 (Wikipedia): acquired. The "
                  "firm's exit line ('Acuired by Renesas Electronics, 2020') carries a wrong year. Lux's row still "
                  "reads public (listed 2020 to 2024); this row holds the completed acquisition.",
             rounds=[rnd("2010-04-26", "unnamed (Form D, $20.2M)", 20200000, None, True, TP_FD, "filing")]))

# ---------------------------------------------------------------- Treeline Biosciences
TL_A = "https://www.fiercebiotech.com/biotech/treeline-biosciences-reaps-200m-series-extension-picks-first-three-clinical-fruit"
TL_RM = "https://www.fiercebiotech.com/biotech/secretive-cancer-biotech-treeline-steps-out-shadows-reverse-merger"
TL_FD21 = "https://www.sec.gov/Archives/edgar/data/1856619/000185661921000001/0001856619-21-000001-index.htm"
L.append(cls("treeline-biosciences", status="private", rng="below_1b", city="Watertown", city_src="formd_address",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TL_A,
             flags=("stage_disputes_band", "needs_web_value"),
             note="Precision oncology small molecules and degraders, Watertown MA (the 2024-25 Form Ds; Stamford CT on "
                  "the 2021-22 filings). Fierce Biotech (2025-09-03): 'Treeline launched in 2021 with a series A led by "
                  "Arch Venture Partners, GV and OrbiMed', and its later raises were Series A extensions ($261M in 2022 "
                  "per Crunchbase News, $200M in September 2025); GV's David Schenkein sits on every Form D from the "
                  "first ($220M, April 2021). The Form D band read that first filing as Growth by size; the record "
                  "names it the Series A, so the band is disputed. Mark: more than $1B raised but no priced round with "
                  "a published valuation, so below_1b under Rule A, flagged needs_web_value. Pending: a reverse merger "
                  "with Standard BioTools announced 2026-06-08 (combined company to trade as TRLN, Standard holders to "
                  "own 16%, close expected in the second half of 2026; Fierce); Standard BioTools still trades "
                  "separately on 2026-09-28 (stockanalysis.com), so the deal has not closed and the row stays private.",
             rounds=[rnd("2021", "Series A", None, "ARCH Venture Partners; GV; OrbiMed", True, TL_A, "press"),
                     rnd("2021-04-09", "Series A (first Form D close)", 220002897, None, True, TL_FD21, "filing"),
                     rnd("2025-09-03", "Series A extension", 200000000, None, None, TL_A, "press")]))

# ---------------------------------------------------------------- TravelJoy
TJ_A = "https://techcrunch.com/2024/03/01/backed-by-10m-series-a-traveljoy-is-riding-the-post-covid-demand-for-expert-travel-planning/"
L.append(cls("traveljoy", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
             focus="SaaS", stage="undetermined",
             note="CRM, itineraries and payments software for independent travel advisors; its terms of use give 2261 "
                  "Market Street, San Francisco. TechCrunch (2024-03-01): the company raised its seed in 2019 and an "
                  "unannounced $10M Series A about a year earlier, led by Acrew Capital with NFX, Founder Collective, "
                  "Forerunner and Concrete Rose (no GV named). The firm lists it from 2019 but no source read ties GV "
                  "to a named round, so the stage is undetermined (a listing capture does not name the entry). "
                  "Operating (the company's site, 2026).",
             rounds=[rnd("2019", "Seed", None, None, None, TJ_A, "press"),
                     rnd("2023", "Series A", 10000000, "Acrew Capital", False, TJ_A, "press")]))

# ---------------------------------------------------------------- Teem (formerly EventBoard)
TM_IO = NEWS("teem", "iOFFICE Acquires Leading Meeting Space")
L.append(cls("teem", status="acquired", rng="below_1b", country="US", city="Salt Lake City", city_src="web_verified",
             focus="SaaS", stage="undetermined",
             note="Meeting-room and workplace analytics software (EventBoard until its rename), Salt Lake City. "
                  "Crunchbase News (2020-01): Teem raised about $23M with investors including Greycroft and NGP "
                  "Capital, was bought by WeWork in September 2018 (reported $100M; the firm's exit line 'Acquired by "
                  "WeWork, 2018'), and WeWork sold it to iOFFICE (iOFFICE's release, Houston, 2020-01-14, "
                  "'Salt Lake City-based Teem'). No source read names the round GV entered (the firm lists it from "
                  "2016), so the stage is undetermined. Acquired.",
             rounds=[]))

# ---------------------------------------------------------------- StrongDM
SD_B = "https://www.prnewswire.com/news-releases/strongdm-raises-54m-series-b-led-by-tiger-global-to-transform-secure-infrastructure-access-management-301377026.html"
SD_C = "https://www.prnewswire.com/news-releases/strongdm-secures-34-million-series-c-funding-to-expand-into-europe-and-asia-and-establish-zero-trust-pam-for-enterprise-security-302133548.html"
L.append(cls("strongdm", status="acquired", rng="below_1b", country="US", city="Palo Alto", city_src="web_verified",
             focus="Security",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SD_B, entry_date="2021-09-15",
             note="Infrastructure and privileged access management. The company's release (Burlingame, 2021-09-15): a "
                  "$54M Series B 'led by Tiger Global, with participation from new investor GV' (GV's Erik Nordlander "
                  "quoted), so GV entered at the Series B: Growth. The $34M Series C release (Palo Alto, 2024-05-02) "
                  "names GV, Sequoia and True Ventures as existing investors, $96M raised in total. Delinea announced "
                  "the acquisition in January 2026 and completed it in March 2026 (StrongDM's own About page; "
                  "GlobeNewswire via Manila Times): acquired. City from the latest release dateline (Palo Alto); "
                  "Sequoia's row still reads private and San Francisco, this row holds the completed acquisition.",
             rounds=[rnd("2021-09-15", "Series B", 54000000, "Tiger Global", True, SD_B, "company"),
                     rnd("2024-05-02", "Series C", 34000000, "Anchor Capital", True, SD_C, "company")]))

# ---------------------------------------------------------------- Synapticure
SC_SEED = "https://www.synapticure.com/press-release/synapticure-launches-to-transform-standard-of-care-for-people-living-with-als-and-beyond-with-6m-in-seed-funding-led-by-gv"
SC_A = "https://www.prnewswire.com/news-releases/synapticure-raises-25-million-series-a-to-expand-virtual-care-for-patients-and-caregivers-living-with-neurodegenerative-diseases-in-all-50-states-302310288.html"
L.append(cls("synapticure", status="private", rng="below_1b", country="US", city="Chicago", city_src="web_verified",
             focus="Healthcare & Bio",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SC_SEED, entry_date="2022-02-01",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=SC_A,
             note="Virtual specialist care for ALS, Parkinson's and dementia patients, Chicago (2045 W Grand Ave). The "
                  "company's release (Chicago, 2022-02-01): a $6M seed led by GV with LifeForce Capital, Martin "
                  "Ventures, Byers Capital, Y Combinator and angels. Graduated: the $25M Series A (Chicago, 2024-11-19) "
                  "was led by B Capital with existing backers Google Ventures, Optum Ventures and Rock Health Capital. "
                  "Operating (the company's site, 2025-26). Aligned with Y Combinator's row (Chicago).",
             rounds=[rnd("2022-02-01", "Seed", 6000000, "GV", True, SC_SEED, "company"),
                     rnd("2024-11-19", "Series A", 25000000, "B Capital", True, SC_A, "company")]))

# ---------------------------------------------------------------- TMRW Life Sciences
TW_C = "https://www.prnewswire.com/news-releases/tmrw-life-sciences-raises-105-million-to-accelerate-global-rollout-of-worlds-first-automated-platform-for-ivf-egg--embryo-management-301336896.html?tc=eml_cleartime"
TW_B = "https://www.prnewswire.com/news-releases/tmrw-life-sciences-raises-25-million-in-series-b-funding-led-by-5am-ventures-300976046.html"
TW_M = "https://www.prnewswire.com/news-releases/reprotech-and-tmrw-life-sciences-enter-into-business-combination-to-create-the-most-comprehensive-technology-enabled-cryostorage-company-in-fertility-302732746.html"
L.append(cls("tmrw-life-sciences", status="acquired", rng="below_1b", country="US", city="New York",
             city_src="web_verified", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TW_C, entry_date="2021-07-20",
             note="Automated cryostorage and tracking of frozen eggs and embryos for IVF clinics, New York. The "
                  "company's release (New York, 2021-07-20): a $105M Series C of equity and debt whose equity 'was led "
                  "by Transformation Capital and includes participation from GV (formerly Google Ventures)', with 5AM "
                  "Ventures and Life Sciences Innovation Fund named as the existing investors, so GV entered at the "
                  "Series C: Growth. Earlier: $12M Series A (2019) and $25M Series B led by 5AM (December 2019); a "
                  "Series D in July 2024 (the company's newsroom). Reprotech and TMRW announced a business combination "
                  "on 2026-04-02 (Reprotech's release) and Reprotech now sells TMRW's products; the firm's exit line "
                  "reads 'Acquired by Reprotech, 2026': acquired.",
             rounds=[rnd("2019-12", "Series B", 25000000, "5AM Ventures", False, TW_B, "company"),
                     rnd("2021-07-20", "Series C", 105000000, "Transformation Capital", True, TW_C, "company")]))

# ---------------------------------------------------------------- Swing Education
SW_C = NEWS("swing-education", "Swing Education Raises $38M in Series C")
L.append(cls("swing-education", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SW_C, entry_date="2018",
             note="Marketplace matching substitute teachers with schools, San Francisco. citybiz (2023-06-01): Swing "
                  "Education, 'a San Francisco, CA-based online marketplace', raised a $38M Series C co-led by Apax "
                  "Partners and Reach Capital, following 'a 2018 Series B funding co-led by GV (formerly Google "
                  "Ventures) and Owl Ventures and a seed round' from Social Capital, Kapor, Moment, Ulu and others "
                  "(no GV), so GV entered at the Series B: Growth (the firm lists it from 2018). A $20M growth loan "
                  "from Runway Growth followed in August 2025 (PR Newswire headline). Operating (the company's site). "
                  "Y Combinator's row leaves the city empty.",
             rounds=[rnd("2018", "Series B", None, "GV; Owl Ventures", True, SW_C, "press"),
                     rnd("2023-06-01", "Series C", 38000000, "Apax Partners; Reach Capital", None, SW_C, "press")]))

# ---------------------------------------------------------------- Sync Labs (sync.)
SL_SEED = "https://sync.so/blog/sync-announces-5-5m-seed-round-to-make-video-content-creation-less-camera-dependent-using-ai"
L.append(cls("sync-labs", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SL_SEED, entry_date="2024-04",
             note="AI lip-sync and visual dubbing models (sync.so; legal name Synchronicity Labs). The company's own "
                  "post (2024-08-16): a '$5.5M seed round led by Google Ventures' with Y Combinator, Creator Ventures "
                  "and Rebel Fund; the firm's /ai list gives 'Invested 2024-04', read as the entry date (D7: the "
                  "round's post dates the announcement, not the investment). City from knowledge (San Francisco). "
                  "Momentum check 2026-09-28: Google News for the company returned no later round, so below_1b; the "
                  "entry is past 24 months, so not censored. Graduation left for the graduation pass. Y Combinator's "
                  "'sync.' row (Seoul, KR) describes a different company on the same domain (a one-person Seoul "
                  "fund, per its own note): a name collision, not aligned.",
             rounds=[rnd("2024-04", "Seed", 5500000, "Google Ventures", True, SL_SEED, "company")]))

# ---------------------------------------------------------------- Syremis Therapeutics
SY_A = "https://www.fiercebiotech.com/biotech/karuna-head-teva-alums-meet-minds-launch-schizophrenia-focused-biotech-syremis-165m-series"
L.append(cls("syremis-therapeutics", status="private", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=SY_A, city="Tel Aviv", city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=SY_A, entry_date="2025-12-18",
             note="Neuropsychiatry drugs (schizophrenia, depression), spun out of Israel's Clexio Biosciences. Fierce "
                  "Biotech (2025-12-18): a $165M Series A led by Dexcel Pharma and Third Rock Ventures, with 'Bain "
                  "Capital Life Sciences, Google Ventures, QVT and Pictet' participating, at the company's launch; the "
                  "firm lists it from 2026, so GV entered at the Series A. The company 'is based in Tel Aviv and "
                  "Boston' (Fierce); its founders are Teva and Clexio veterans in Israel and Calcalist lists the round "
                  "among Israeli funding rounds, so recorded as Tel Aviv, IL: a judgment call on a two-site company "
                  "(Boston is the other site).",
             rounds=[rnd("2025-12-18", "Series A", 165000000, "Dexcel Pharma; Third Rock Ventures", True, SY_A,
                         "press")]))

# ---------------------------------------------------------------- TenSixteen Bio
T16_A = "https://news.crunchbase.com/business/tensixteen-bio-40m-series-a/"
L.append(cls("tensixteen-bio", status="unknown", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=T16_A, entry_date="2022-01-27",
             note="Therapeutics from somatic mosaicism and clonal hematopoiesis (CHIP). Crunchbase News (2022-01-27): "
                  "the company 'launched Thursday with a $40 million Series A round funded by Foresite Capital and "
                  "GV', San Francisco-based, co-founded by Foresite Labs, CEO Mark Chao: GV entered at the launch "
                  "Series A. Fate unclear: the company's domain (tensixteen.bio) is now a parked page offering it for "
                  "sale, and an Endpoints piece (2025-05-21, unread, paywalled) reports a new spinout led by a Forty "
                  "Seven co-founder in the same field; the firm still lists the company. No source read gives its "
                  "fate, so status is unknown.",
             rounds=[rnd("2022-01-27", "Series A", 40000000, None, True, T16_A, "press")]))

# ---------------------------------------------------------------- The Pill Club
PC_BI = "https://www.businessinsider.com/the-pill-club-raises-51-million-for-direct-to-consumer-birth-control-2019-1"
L.append(cls("the-pill-club", status="acquired", rng="below_1b", country="US", city="San Carlos",
             city_src="web_verified", focus="Healthcare & Bio", stage="undetermined",
             note="Birth-control telehealth and pharmacy delivery. Business Insider (January 2019): 'Investors including "
                  "GV just put another $51 million' into the company, 'San Carlos, California-based The Pill Club has "
                  "now raised $67 million from investors including VMG, GV's consumer team, Base10, Shasta Ventures "
                  "and Acme Capital'; the round is not named and GV's place in the earlier $16M is not given, so the "
                  "stage is undetermined (the firm lists it from 2019). A $42M round followed in June 2021 (Fierce "
                  "Healthcare headline). After an $18.3M Medicaid-fraud settlement with California (February 2023) "
                  "the company filed for bankruptcy (Mercury News headline, April 2023) and Thirty Madison bought its "
                  "assets in June 2023 (MobiHealthNews, Fierce Healthcare and Business Journals headlines): acquired "
                  "out of insolvency, with Thirty Madison (Nurx) the successor; thepillclub.com now redirects to Nurx.",
             rounds=[rnd("2019-01", "unnamed ($51M)", 51000000, None, True, PC_BI, "press")]))

# ---------------------------------------------------------------- Stipple Bio
STP_A = NEWS("stipple-bio", "Backers Include GV")
STP_FD22 = "https://www.sec.gov/Archives/edgar/data/1932776/000193277622000001/0001932776-22-000001-index.htm"
STP_FD24 = "https://www.sec.gov/Archives/edgar/data/1932776/000193277624000001/0001932776-24-000001-index.htm"
L.append(cls("stipple-bio", status="private", rng="below_1b", city="Cambridge", city_src="web_verified",
             focus="Healthcare & Bio", stage="undetermined", flags=("stage_disputes_band",),
             extra={"entry_stage_source": None, "entry_date": None},
             note="Epitope-level target discovery for precision cancer therapies (ADCs), founded 2022. citybiz "
                  "(2026-04-07): 'Cambridge, Mass.-based Stipple Bio has emerged from stealth' with a $100M Series A "
                  "co-led by RA Capital, a16z Bio+Health and Nextech, 'with participation from existing investors "
                  "Emerson Collective ..., GV (Google Ventures), LoLa Capital Partners'. GV was therefore in before the "
                  "Series A, in one of the unnamed earlier rounds (Form Ds: $12M in 2022, $15M in late 2024), but no "
                  "source names which, and no GV person sits on any filing. The Form D band had read the 2022 filing "
                  "(a16z's Vineeta Agarwala its outside director) as GV's Series A entry; the company names the 2026 "
                  "round its Series A, so that label and its date are withdrawn and the stage is undetermined. City: "
                  "Cambridge (the release and the 2026 Form D addresses); a16z's row still gives Milford from the "
                  "2022 filing.",
             rounds=[rnd("2022-05", "unnamed (Form D, $12M)", 12000000, None, None, STP_FD22, "filing"),
                     rnd("2024", "unnamed (Form D, $15M)", 15000000, None, None, STP_FD24, "filing"),
                     rnd("2026-04-07", "Series A", 100000000, "RA Capital; a16z Bio+Health; Nextech Invest", True,
                         STP_A, "press")]))

# ---------------------------------------------------------------- The Players' Tribune
PT_C = "https://variety.com/2017/digital/news/players-tribune-derek-jeter-funding-ivp-google-thomas-tull-1201963840/"
L.append(cls("the-players-tribune", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Media, Gaming & Advertising",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PT_C, entry_date="2017-01-19",
             note="Athlete-written sports media founded by Derek Jeter, New York. Variety (2017-01-19): 'closed $40 "
                  "million in Series C funding, led by venture-capital firm IVP. The latest round includes "
                  "participation from Alphabet's GV (formerly known as Google Ventures), dozens of individual "
                  "athletes, and existing investors including Thomas Tull ..., New Enterprise Associates, and "
                  "GenTrust', so GV entered at the Series C: Growth (the firm lists it from 2017). Acquired by Minute "
                  "Media in November 2019 (Wikipedia; Variety headline; the firm's exit line). Aligned with IVP's row "
                  "(acquired, New York, Growth).",
             rounds=[rnd("2017-01-19", "Series C", 40000000, "IVP", True, PT_C, "press")]))

# ---------------------------------------------------------------- Trace Neuroscience
TRN_A = "https://www.biopharmadive.com/news/trace-neuroscience-als-third-rock-launch-atlas-ra-gv/732666/"
TRN_A2 = "https://alsnewstoday.com/news/trace-neuroscience-launches-develop-unc13a-treatment-als/"
L.append(cls("trace-neuroscience", status="private", rng="below_1b", country="US", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TRN_A, entry_date="2024-11-12",
             flags=("city_unknown",),
             note="Antisense and genetic medicines restoring UNC13A for ALS. BioPharma Dive (2024-11-12): the company "
                  "'launched Tuesday with $101 million from an investment group that includes Atlas Venture, RA "
                  "Capital Management and Alphabet's venture capital arm, GV. Third Rock led the round'; ALS News "
                  "Today and the Business Wire headline name it the Series A. The firm lists it from 2024, so GV "
                  "entered at the launch Series A. Operating (first clinical program, June 2026, Business Wire "
                  "headline). Located only as 'the San Francisco area' (BioPharma Dive); no source read names the "
                  "municipality, so the city is left open.",
             rounds=[rnd("2024-11-12", "Series A", 101000000, "Third Rock Ventures", True, TRN_A2, "press")]))

# ---------------------------------------------------------------- Transcriptic (now Strateos)
L.append(cls("transcriptic", status="acquired", rng="below_1b", country="US", city="Menlo Park", city_src="web_verified",
             focus="Healthcare & Bio", stage="undetermined",
             note="Robotic cloud laboratory for life-science experiments. Transcriptic merged with 3Scan in 2019 to form "
                  "Strateos (Y Combinator's row; Strateos raised a $56M Series B in 2021 and shifted to on-site cloud "
                  "labs in 2023, Business Wire and Fierce headlines); status aligned with Y Combinator's row "
                  "(acquired, by merger). City: Strateos's contact page lists Menlo Park first (3565 Haven Ave), with "
                  "San Diego and South San Francisco sites; Y Combinator's row says San Francisco. No source read names "
                  "the round GV entered (the firm lists the company from 2013, partner Blake Byers), so the stage is "
                  "undetermined; Google News for the company returned no funding report.",
             rounds=[]))

# ---------------------------------------------------------------- SweetLabs
L.append(cls("sweetlabs", status="private", rng="below_1b", country="US", city="San Diego", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Consumer app distribution for Windows PC makers (Pokki, the OpenCandy network), San Diego with a "
                  "Seattle office (Wikipedia). Wikipedia: 'SweetLabs has raised at least $21.5 million in venture "
                  "capital from Bessemer Venture Partners, Google Ventures, Intel Capital, and O'Reilly AlphaTech "
                  "Ventures'; no source read names the round GV entered (the firm lists it from 2012), so the stage is "
                  "undetermined. Operating: its site (privacy policy updated 2023) describes an app developer for "
                  "device makers. No mark near $1B.",
             rounds=[]))

# ---------------------------------------------------------------- Subtext
L.append(cls("subtext", status="acquired", rng="below_1b", country="US", city="Seattle", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Social reading and ebook annotation app used in classrooms, Seattle. Acquired by Renaissance Learning "
                  "in 2013 (the firm's exit line 'Acquired by Renaissance Learning, 2013'). No source read names the "
                  "round GV entered (the firm lists it from 2012); Google News for the company returned no funding "
                  "report, so the stage is undetermined.",
             rounds=[]))

# ---------------------------------------------------------------- ThinkNear
L.append(cls("thinknear", status="acquired", rng="below_1b", country="US", city="Santa Monica",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Location-based mobile advertising and yield management for local merchants (a TechStars company). "
                  "Telenav bought it for $22.5M in October 2012 (Business Insider headline; the firm's exit line "
                  "'Acquired by Telenav, 2012'), and InMarket acquired Thinknear from Telenav in 2019 (Marketing Dive, "
                  "2019-08-09). City from knowledge (Santa Monica). No source read names the round GV entered, so the "
                  "stage is undetermined.",
             rounds=[]))

# ---------------------------------------------------------------- Tenaya Therapeutics
TY_IRA = FTS("Tenaya", "S-1")
TY_B = NEWS("tenaya-therapeutics", "Closes $92 Million Series B")
L.append(cls("tenaya-therapeutics", rng="below_1b", usd=132250000, val_src="web_verified", val_cite=cap("tnya"),
             asof=TODAY, country="US", city="South San Francisco", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TY_B, entry_date="2019-10-03",
             extra=WV,
             note="Heart-disease gene therapies and small molecules (NASDAQ: TNYA), South San Francisco. The company's "
                  "release (South San Francisco, 2019-10-03): the $92M Series B 'was led by Casdin Capital and included "
                  "GV, The Column Group', with GV's Anthony Philippakis joining as board observer. GV's only vehicle "
                  "on the Series C investors' rights agreement (2020-12-17, filed with the S-1) is GV 2019, L.P., so it "
                  "was not in the Series A (sold through December 2018): GV entered at the Series B, Growth. Market cap "
                  "$132.25M on 2026-09-28 (stockanalysis.com), replacing the June 2025 float.",
             rounds=[rnd("2018-12", "Series A (December 2018 tranche)", 19900000, None, False, TY_IRA, "filing"),
                     rnd("2019-10-03", "Series B", 92000000, "Casdin Capital", True, TY_B, "company"),
                     rnd("2020-12-17", "Series C", 106000000, None, True, TY_IRA, "filing")]))

# ---------------------------------------------------------------- Tamr
TAMR_B = "https://www.tamr.com/press-releases/tamr-receives-25-2-million-in-financing-from-hewlett-packard-ventures-thomson-reuters-massmutual-ventures-and-others"
TAMR_18 = "https://www.tamr.com/press-releases/tamr-closes-18-million-investment-to-accelerate-growth-secure-leadership-of-the-enterprise-data-unification-market"
L.append(cls("tamr", status="private", rng="below_1b", city="Cambridge", focus="Data Infrastructure",
             stage="Series A", stage_src="model", stage_conf="medium", stage_cite=TAMR_18,
             note="Enterprise data mastering and unification, Cambridge MA (co-founded by Michael Stonebraker and "
                  "Andy Palmer). The company's own releases: the June 2015 round was its $25.2M Series B, with NEA and "
                  "Google Ventures as existing investors (Cambridge, 2015-06-19), and the $18M round of July 2018 calls "
                  "'NEA and GV' its founding investors. GV was therefore in the founding round that preceded the "
                  "Series B, read as the Series A (model, medium); no source read names that round or dates it (the "
                  "firm lists Tamr from 2014, and its /ai list records re-investments in 2018, 2020 and 2022). "
                  "Private, operating; no priced round near $1B.",
             rounds=[rnd("2015-06-19", "Series B", 25200000, None, True, TAMR_B, "company"),
                     rnd("2018-07-11", "unnamed ($18M)", 18000000, None, True, TAMR_18, "company")]))

# ---------------------------------------------------------------- Taysha Gene Therapies
TSHA_S1 = FTS("Taysha", "S-1")
L.append(cls("taysha-gene-therapies", rng="1b_plus", usd=1630000000, val_src="web_verified", val_cite=cap("tsha"),
             asof=TODAY, country="US", city="Dallas", focus="Healthcare & Bio", stage="undetermined", extra=WV,
             note="AAV gene therapies for CNS diseases (NASDAQ: TSHA), Dallas. The S-1 (2020-09-02) names 'GV "
                  "(formerly Google Ventures)' among the investors in its $126M of preferred stock: a $30M Series A "
                  "(March to July 2020, almost all to PBM Capital and Nolan Capital) and a $96M Series B (July and "
                  "August 2020, Fidelity the largest related-party buyer). The related-party tables do not list GV, "
                  "and no source read says which series it bought, so the stage is undetermined. Market cap $1.63B on "
                  "2026-09-28 (stockanalysis.com), replacing the June 2025 float ($545M), so the band moves to 1b_plus.",
             rounds=[rnd("2020-03", "Series A", 30000000, None, None, TSHA_S1, "filing"),
                     rnd("2020-07", "Series B", 96000000, None, None, TSHA_S1, "filing")]))

import os  # noqa: E402
jl.write("j13", L, record=os.environ.get("J13_DRY") != "1")
