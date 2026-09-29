"""PRO-75 grind, judge j11: queue batch 11 (45 member rows, rani-therapeutics to schr-dinger).

One cls() per row; one verdict() for Revolution Medicines, whose only route into the book is the stock it paid for
GV-backed EQRx (sale consideration, COLLECTION.md s1). Citations come from the helpers (judge_lib) or from pages
read in full during the pass (WebFetch); market caps from stockanalysis.com read 2026-09-28 with curl."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
WV = {"valuation_range_source": "web_verified"}
TODAY = "2026-09-28"


def POSTX(slug):
    """The firm's own post whose slug is exactly `slug` (POST() matches substrings; two posts share this prefix)."""
    m = [p for p in jl._POSTS if p.get("slug") == slug]
    if len(m) != 1:
        raise SystemExit(f"POSTX({slug!r}) matched {len(m)}")
    return m[0]["url"]


def CAP(ticker):
    """stockanalysis.com market-cap page, read with curl on 2026-09-28 (the brief's named source)."""
    return f"https://stockanalysis.com/stocks/{ticker}/market-cap/"


# ---------------------------------------------------------------- pages read in full during the pass
PRWEB_REACTION = ("https://www.prweb.com/releases/reaction_commerce_raises_8_5_million_in_series_a_funding_led_by_gv/"
                  "prweb14834575.htm")
SEQUOIA_ROX = "https://sequoiacap.com/article/partnering-with-rox-every-seller-needs-an-agent-swarm"
TC_ROX = "https://techcrunch.com/2026/03/12/sales-automation-startup-rox-ai-hits-1-2b-valuation-sources-say/"
CB_RIPPLE = "https://news.crunchbase.com/fintech-ecommerce/crypto/unicorn-ripple-500m-raise/"
TC_REPUBLIC_A = "https://techcrunch.com/2012/09/11/republic-project-raise/"
TC_REPUBLIC_DG = "https://techcrunch.com/2013/10/07/dg-acquires-republic-project/"
TC_SCHEMATIC = "https://techcrunch.com/2014/08/04/rhapsody-soundtracking/"
TC_ROCKETRIP = "https://techcrunch.com/2018/04/25/rocketrip-raises-15-million-to-reward-cost-saving-employees/"
TC_ROBINHOOD_SEED = "https://techcrunch.com/2013/12/18/zero-commission-stock-trading-robinhood/"
TC_SCALYR_SEED = "https://techcrunch.com/2015/04/22/scalyr-raises-2-1m-seed-round-for-its-log-monitoring-system/"
TC_SCALYR_A = "https://techcrunch.com/2017/11/20/scalyr-scores-20m-series-a-for-super-fast-log-reading-tool/"
TC_SCALYR_S1 = "https://techcrunch.com/2021/02/09/sentinelone-acquires-high-speed-logging-startup-scalyr-for-155m/"
TC_RESISTANT_A = "https://techcrunch.com/2021/10/20/resistant-ai-scores-16-6m-for-its-anti-fraud-fintech-tools/"
TC_RESOLUTION_B = "https://techcrunch.com/2018/10/23/stockholm-based-resolution-games-nabs-7-5m-to-pioneer-ar-vr-experiences/"
TC_SAVIOKE_SEED = ("https://techcrunch.com/2014/04/09/led-by-ex-ceo-of-willow-garage-savioke-gets-2m-from-ame-google-"
                   "ventures-to-build-a-service-robot/")

# ================================================================ rows

# ---- Rattle: GV came in at the Series A (Insight-led, April 2022)
RATTLE_A = NEWS("rattle", "Rattle raises $26M to revolutionize")
L.append(cls("rattle", status="private", rng="below_1b", country="US", country_src="web_verified",
             country_cite=RATTLE_A, city="San Francisco", city_src="web_verified", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=RATTLE_A,
             entry_date="2022-04-05", flags=("model_disputes_source",),
             note="Revenue-ops workflows that bring Salesforce into Slack. The company's own release (San Francisco "
                  "dateline, 2022-04-05): $26M Series A led by Insight Partners with GV joining existing investors "
                  "Sequoia Capital India and Lightspeed, after a $2.8M seed less than a year earlier (Lightspeed and "
                  "Sequoia India). The prefilled NZ was a name-match on a one-word name; the company is US-based "
                  "(dateline). No later priced round found; below $1B.",
             rounds=[rnd("2021-08-31", "Seed", 2800000, None, False,
                         NEWS("rattle", "to modernize enterprise sales stack"), "press"),
                     rnd("2022-04-05", "Series A", 26000000, "Insight Partners", True, RATTLE_A, "company")]))

# ---- Reaction Commerce: GV led the Series A (October 2017); Mailchimp bought it in 2019
L.append(cls("reaction-commerce", status="acquired", rng="below_1b", country="US", city="Santa Monica",
             city_src="web_verified", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PRWEB_REACTION,
             entry_date="2017-10-31",
             note="Open-source commerce platform (Santa Monica). The company's release (2017-10-31): $8.5M Series A "
                  "led by GV, with CrossCut Ventures, Double M Partners, Joanne Wilson and Female Founders Fund, "
                  "bringing total investment to over $11.7M. Acquired by Mailchimp in 2019 (the firm's own exit line).",
             rounds=[rnd("2017-10-31", "Series A", 8500000, "GV", True, PRWEB_REACTION, "company")]))

# ---- Recursive Superintelligence: GV co-led the company's first, unnamed $650M round at $4.65B (May 2026)
TNW_RECURSIVE = NEWS("recursive-superintelligence", "raises $650m at $4.65bn")
L.append(cls("recursive-superintelligence", status="private", rng="1b_plus", usd=4650000000, val_src="web_verified",
             val_cite=TNW_RECURSIVE, asof="2026-05-13", country="US", city="San Francisco",
             focus="AI & Applied AI", stage="undetermined", entry_date="2026-05", extra=WV,
             note="Self-improving AI lab led by Richard Socher, offices in San Francisco and London. The firm's own post "
                  "(2026-05-13) says GV co-led the 'early $650M funding at a $4.65 billion valuation'; The Next Web: "
                  "led by GV and Greycroft with Nvidia and AMD. Press in April reported the same raise at $500M and a "
                  "$4B valuation. No source gives the round a name (one outlet called it pre-Series A), so the stage is "
                  "undetermined; entry month from the firm's own /ai list (Invested 2026-05). Momentum check "
                  "2026-09-28: the $4.65B mark is the latest priced event found.",
             rounds=[rnd("2026-05-13", "first round (unnamed)", 650000000, "GV and Greycroft", True, TNW_RECURSIVE,
                         "press")]))

# ---- Redpanda (formerly Vectorized): GV entered at the Series A it led; $1B at the April 2025 round GV led
REDPANDA_POST = POSTX("blue-water-autonomy")
REDPANDA_BBG = NEWS("redpanda", "Lifts Redpanda to Unicorn Valuation")
L.append(cls("redpanda", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=REDPANDA_BBG,
             asof="2025-04-03", val_conf="medium", country="US", city="San Francisco", focus="Data Infrastructure",
             stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=REDPANDA_POST,
             entry_date="2020-11", extra=WV,
             note="Kafka-compatible streaming data platform (San Francisco). The firm's own posts: Dave Munichiello "
                  "names Alex Gallego (Redpanda) among the founders he 'backed at the Series A' (2025-08-26), and "
                  "GV's 'continued lead (or co-lead) investment in every round since the Series A' (2025-04-03); "
                  "Vectorized announced the $15M with Redpanda's launch on 2021-01-26 (the firm's post). Lightspeed's "
                  "sibling row holds the earlier 2019 seed. Entry month from the firm's own /ai list (Invested "
                  "2020-11). Mark: the $100M round GV led in April 2025 ('Redpanda Raises $100M Led by GV', the "
                  "company's release headline) 'Lifts Redpanda to Unicorn Valuation' (Bloomberg headline, 2025-04-03; "
                  "both pages refuse scripted reads): $1B as the floor the headline states, medium confidence, aligned "
                  "with the Lightspeed sibling's $1B.",
             rounds=[rnd("2021-01-26", "Series A (announced with the seed as $15M of funding)", None, None, True,
                         POST("vectorized-google"), "firm"),
                     rnd("2025-04-03", "round led by GV ($100M)", 100000000, "GV", True, REDPANDA_BBG, "press")]))

# ---- Relay Therapeutics: GV invested in 2017 (the firm's post), and the only 2017 sale was the Series B
RELAY_POST = POST("relay-therapeutics-ipo")
RELAY_S1 = "https://www.sec.gov/Archives/edgar/data/1812364/000119312520177746/d924757ds1.htm"
L.append(cls("relay-therapeutics", city="Cambridge", focus="Healthcare & Bio",
             stage="Growth", stage_src="model", stage_conf="medium", stage_cite=RELAY_POST, entry_date="2017-12",
             rng="1b_plus", usd=3880000000, val_src="web_verified", val_cite=CAP("rlay"), asof=TODAY, extra=WV,
             flags=("model_disputes_source",),
             note="Motion-based drug discovery (Cambridge MA; NASDAQ: RLAY). Krishna Yeshwant (the firm's post, "
                  "2020-07-16): 'I jumped to invest in the company in 2017 and doubled down on our investment again in "
                  "2018.' The IPO prospectus lists the preferred sales: Series A August 2016 ($56.8M, Third Rock and "
                  "D. E. Shaw), Series B December 2017 ($63.0M), Series C December 2018 ($400M, SoftBank Vision Fund); "
                  "the only 2017 sale is the Series B, so GV's entry is read as the Series B (Growth). Prefilled "
                  "market cap $585.5M was stale: $3.88B on 2026-09-28 (stockanalysis), so the band moves to 1b_plus.",
             rounds=[rnd("2016-08", "Series A", 56824740, "Third Rock Ventures", False, RELAY_S1, "filing"),
                     rnd("2017-12", "Series B", 63000000, None, True, RELAY_S1, "filing"),
                     rnd("2018-12", "Series C", 400000000, "SoftBank Vision Fund", True, RELAY_S1, "filing")]))

# ---- Republic Project: Google Ventures led the $1M Series A (September 2012); DG bought it in October 2013
L.append(cls("republic-project", status="acquired", rng="below_1b", country="US", city="Scottsdale",
             city_src="formd_address", focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_REPUBLIC_A,
             entry_date="2012-09-11",
             note="Cloud ad platform for agencies and brands. TechCrunch (2012-09-11): '$1 million in series A "
                  "financing' led by Google Ventures with 500 Startups, Venture51, Ludlow Ventures and angels. DG "
                  "(Digital Generation) bought it for $1.4M in cash plus earn-outs (TechCrunch, 2013-10-07), the team "
                  "joining DG's Los Angeles office. City from the company's Form D (Republic Project, 21090 North Pima "
                  "Road, Scottsdale AZ, 2011).",
             rounds=[rnd("2012-09-11", "Series A", 1000000, "Google Ventures", True, TC_REPUBLIC_A, "press")]))

# ---- Ripcord: Google Ventures led the December 2017 extension of the Series B (Hayward CA)
TC_RIPCORD_GV = "https://techcrunch.com/2017/12/20/google-ventures-invests-in-ripcords-paper-digitizing-robotics-service/"
TC_RIPCORD_2023 = "https://techcrunch.com/2023/10/13/ripcord-the-steve-wozniak-backed-file-scanning-startup-is-raising-new-cash/"
L.append(cls("ripcord", status="private", rng="below_1b", city="Hayward", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_RIPCORD_GV,
             entry_date="2017-12-20",
             note="Robotic digitisation of paper records (Hayward CA). TechCrunch (2017-12-20): the $40M Series B of "
                  "August 2017 'has just been bumped up to $65 million, courtesy of additional funding led by Google "
                  "Ventures'; the firm entered on that Series B extension (Growth). Still operating: TechCrunch "
                  "(2023-10-13) reports a new round of about $35M at a $110M pre-money valuation, and a May 2026 "
                  "release announces a new California robotics facility. Below $1B.",
             rounds=[rnd("2017-03-23", "Series A", 9500000, None, False, None, "press"),
                     rnd("2017-08-17", "Series B", 40000000, None, False, None, "press"),
                     rnd("2017-12-20", "Series B extension", 25000000, "Google Ventures", True, TC_RIPCORD_GV, "press"),
                     rnd("2023-10-13", "new round (about $35M, $20M closed)", 35000000, None, None, TC_RIPCORD_2023,
                         "press")]))

# ---- Rocketrip: GV led the $15M Series C (April 2018); Mondee bought it in 2020
L.append(cls("rocketrip", status="acquired", rng="below_1b", country="US", city="New York", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_ROCKETRIP,
             entry_date="2018-04-25",
             note="Rewards employees for saving on business travel (New York; YC W14). TechCrunch (2018-04-25): "
                  "'$15 million in Series C funding led by GV (Google Ventures)', with existing investors Bessemer "
                  "Venture Partners and Canaan Partners; earlier rounds of $3M (2014) and $9M (2016) per TechCrunch. "
                  "Acquired by Mondee in 2020 (PhocusWire, 2020-09-09; the firm's own exit line).",
             rounds=[rnd("2014-07-14", "round not named in the headline", 3000000, None, False, None, "press"),
                     rnd("2016-06-20", "round not named in the headline", 9000000, None, False, None, "press"),
                     rnd("2018-04-25", "Series C", 15000000, "GV", True, TC_ROCKETRIP, "press")]))

# ---- Scalyr: Google Ventures in the $2.1M seed (April 2015); $20M Series A (Nov 2017); SentinelOne bought it (2021)
L.append(cls("scalyr", status="acquired", rng="below_1b", country="US", city="San Mateo",
             focus="Data Infrastructure",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SCALYR_SEED,
             entry_date="2015-04-22",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_SCALYR_A,
             note="Log management and observability (San Mateo). TechCrunch (2015-04-22): '$2.1 million seed round led "
                  "by Susa Ventures'; 'other participants in this round include Bloomberg Beta, Google Ventures and "
                  "Sherpalo Ventures'. Graduated: $20M Series A led by Shasta Ventures (TechCrunch, 2017-11-20). "
                  "SentinelOne bought it for $155M (TechCrunch, 2021-02-09).",
             rounds=[rnd("2015-04-22", "Seed", 2100000, "Susa Ventures", True, TC_SCALYR_SEED, "press"),
                     rnd("2017-11-20", "Series A", 20000000, "Shasta Ventures", None, TC_SCALYR_A, "press")]))

# ---- Resistant AI: GV led the $16.6M Series A (Prague); $25M Series B in October 2025
L.append(cls("resistant-ai", status="private", rng="below_1b", country="CZ", country_src="web_verified",
             country_cite=TC_RESISTANT_A, city="Prague", city_src="web_verified", focus="Security",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_RESISTANT_A,
             entry_date="2021-06",
             extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY,
                    "valuation_citation": NEWS("resistant-ai", "Resistant AI raises $25M Series B to fortify")},
             note="AI fraud and financial-crime detection for fintechs (Prague, offices in London and New York). "
                  "TechCrunch (2021-10-20): '$16.6 million in Series A funding', 'GV (formerly Google Ventures) led "
                  "the round' with existing investors Index Ventures, Credo Ventures and Seedcamp, after a $2.75M seed "
                  "led by Index and Credo. Entry month from the firm's own /ai list (Invested 2021-06), matching the "
                  "US entity's Form D (first sale 2021-06-17). Momentum check 2026-09-28: the latest priced event is "
                  "the $25M Series B of October 2025, far below $1B.",
             rounds=[rnd(None, "Seed", 2750000, "Index Ventures and Credo Ventures", False, TC_RESISTANT_A, "press"),
                     rnd("2021-10-20", "Series A", 16600000, "GV", True, TC_RESISTANT_A, "press"),
                     rnd("2025-10-13", "Series B", 25000000, None, None,
                         NEWS("resistant-ai", "Resistant AI raises $25M Series B to fortify"), "press")]))

# ---- SambaNova Systems: GV co-led the 2018 Series A (the firm's own post); $11B at the July 2026 Series F first close
SAMBA_POST = POST("modular-qualcomm")
TC_SAMBA_F = "https://techcrunch.com/2026/07/08/sambanova-draws-1b-at-11b-valuation-in-series-f-first-close/"
L.append(cls("sambanova-systems", status="private", rng="10b_plus", usd=11000000000, val_src="web_verified",
             val_cite=TC_SAMBA_F, asof="2026-07-08", city="Palo Alto", city_src="web_verified",
             focus="Industrial & Robotics",
             stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=SAMBA_POST, entry_date="2018-03",
             extra=WV, flags=("stage_disputes_band", "model_disputes_source"),
             note="AI chips and systems (Palo Alto). The firm's own post (2026-06-25) lists 'SambaNova (Co-led Series "
                  "A, 2018)' and says GV had 'led the Series A rounds of LatticeData, SambaNova, and Determined.ai'; "
                  "the /ai list dates the first investment 2018-03 (the $56M Series A of March 2018), then "
                  "re-investments in 2019, 2020 and 2021. The Form D band read Growth off the 2019 Series B filing, "
                  "where GV's partner first appears; the firm's post names the earlier entry. Mark: TechCrunch "
                  "(2026-07-08) reports $1B raised at an $11B valuation in the first close of the Series F led by "
                  "General Atlantic, after a $350M Vista-led round in February 2026 and failed Intel acquisition "
                  "talks; the prefilled $5.1B (April 2021) was stale.",
             rounds=[rnd("2018-03", "Series A", 56000000, "GV (co-lead)", True, SAMBA_POST, "firm"),
                     rnd("2019-04-01", "Series B", 150000000, None, True, None, "press"),
                     rnd("2021-04-13", "Series D", 676000000, None, True, None, "press"),
                     rnd("2026-07-08", "Series F (first close)", 1000000000, "General Atlantic", None, TC_SAMBA_F,
                         "press")]))

# ---- Rippl: GV in the $32M seed (September 2022); $23M Series A (October 2024); Harbor Health bought it (Feb 2026)
RIPPL_SEED = NEWS("rippl-care", "32 Million Seed Round")
RIPPL_A = NEWS("rippl-care", "Rippl announces $23M series A")
L.append(cls("rippl-care", status="acquired", rng="below_1b", country="US", city="Seattle", focus="Healthcare & Bio",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=RIPPL_SEED, entry_date="2022-09-28",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=RIPPL_A,
             note="Home-based mental health and dementia care for older adults (Seattle). Hospice News (2022-09-28): "
                  "Rippl began operations 'following a $32 million seed funding round' led by ARCH Venture Partners "
                  "and General Catalyst 'with participation from GV, F-Prime Capital, and Mass General Brigham "
                  "Ventures'. Graduated: 'Rippl announces $23M series A' (Fierce Healthcare, 2024-10-02; the page "
                  "refuses scripted reads, the headline names the round). Acquired by Harbor Health in February 2026 "
                  "(GeekWire, 2026-02-10, 'Harbor Health acquires Seattle dementia care startup Rippl'; Orrick, "
                  "2026-02-17), matching the firm's own exit line.",
             rounds=[rnd("2022-09-28", "Seed", 32000000, "ARCH Venture Partners and General Catalyst", True,
                         RIPPL_SEED, "press"),
                     rnd("2024-10-02", "Series A", 23000000, None, None, RIPPL_A, "press")]))

# ---- Scandit: GV led the $30M Series B (July 2018); $1B at the $150M Series D (February 2022)
SCANDIT_B = NEWS("scandit", "Alphabet backs mobile scanning")
L.append(cls("scandit", country="CH", country_src="web_verified", country_cite=POST("scandit-series-c"),
             city="Zurich", city_src="web_verified", focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SCANDIT_B, entry_date="2018-07",
             note="Smart data capture: barcode scanning and computer vision on mobile devices (Zurich). Retail Dive "
                  "(2018-07-27): Scandit, 'a Swiss company', 'raised $30 million in Series B funding led by GV'; "
                  "Tom Hulme (the firm's post, 2020-05-26): 'In July 2018 I invested in Scandit, a Zurich-based "
                  "company'. Atomico's sibling row holds the earlier $7.5M Series A (2017). The prefilled CH is "
                  "confirmed by both. Band and mark stay as prefilled ($1B at the Series D of February 2022, aligned "
                  "with Atomico).",
             rounds=[rnd("2017-01", "Series A", 7500000, "Atomico", False, None, "press"),
                     rnd("2018-07-27", "Series B", 30000000, "GV", True, SCANDIT_B, "press"),
                     rnd("2020-05-26", "Series C", 80000000, None, True, POST("scandit-series-c"), "firm"),
                     rnd("2022-02-09", "Series D", 150000000, None, None, None, "press")]))

# ---- Santa Ana Bio: GV joined the Versant-led Series A, then led the $125M Series B (2024)
SANTA_ANA = NEWS("santa-ana-bio", "Santa Ana Bio Launches With $168M")
L.append(cls("santa-ana-bio", status="private", rng="below_1b", city="Alameda", city_src="web_verified",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=SANTA_ANA,
             flags=("stage_disputes_band",),
             note="Precision immunology for autoimmune and inflammatory disease ('the Alameda, Calif.-based "
                  "biotech', BioSpace; the address on its Form Ds; the a16z sibling row reads South San Francisco). "
                  "BioSpace (2024-06-13): 'Santa Ana's $43 million Series A was led by founding investor Versant "
                  "Ventures' and 'also included TPG's Life Science Innovations fund and GV'; 'the company's $125 "
                  "million Series B was led by GV.' The Form D band read Growth off the February 2023 filing (GV's "
                  "Brendan Bulik-Sullivan first appears as a director there), which is the Series A's second close: "
                  "the two Form D closes sold $8.0M (May 2021) and $35.3M (February 2023), $43.3M together, the $43M "
                  "Series A of the press account. So the stage moves to Series A; entry date kept from that filing. "
                  "No later round found; first subjects dosed in its Phase 1 in September 2026, so still private.",
             rounds=[rnd("2021-05-17", "Series A (first close, Form D)", 8024658, "Versant Ventures", False,
                         jl.FORMD_CITE("santa-ana-bio", 0), "filing"),
                     rnd("2023-02-14", "Series A (second close, Form D)", 35313642, "Versant Ventures", True,
                         jl.FORMD_CITE("santa-ana-bio", 2), "filing"),
                     rnd("2024-06-13", "Series B", 125000000, "GV", True, SANTA_ANA, "press")]))

# ---- Schrodinger: GV 2019 bought Series E preferred in an additional closing (January 2019)
SDGR_EX = FTS("Schrodinger", "DRS")
L.append(cls("schr-dinger", status="public", rng="1b_plus", usd=2210000000, val_src="web_verified",
             val_cite=CAP("sdgr"), asof=TODAY, city="New York", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SDGR_EX, entry_date="2019-01-04",
             extra=WV,
             note="Physics-based computational platform for drug discovery and materials, with its own pipeline (New "
                  "York; NASDAQ: SDGR). The investors' rights agreement filed with the IPO registration: Amendment "
                  "No. 1, effective 2019-01-04, records that GV 2019, L.P. 'intends to purchase 3,354,353 shares of "
                  "Series E Preferred Stock' in an additional closing of the Series E (purchase price $4,999,998.59). "
                  "Series E = Growth. Market cap $2.21B on 2026-09-28 (stockanalysis).",
             rounds=[rnd("2019-01-04", "Series E (additional closing)", 4999999, None, True, SDGR_EX, "filing")]))

# ---- RetailMeNot: stage prefilled (Form D band, Growth); acquired by Harland Clarke in 2017
L.append(cls("retailmenot", rng="below_1b", city="Austin", city_src="formd_address", focus="Consumer & Marketplaces",
             note="Coupon and deal sites (Austin; formerly Whaleshark Media). Acquired by Harland Clarke Holdings in "
                  "2017 for about $630M in equity, later sold on to J2 Global (Wikipedia); acquired, so no mark."))

# ---- ROME Therapeutics: incubated at GV, launched with its Series A (April 2020); wound down, bought by Pretzel (Jan 2026)
ROME_POST = POST("the-road-to-rome")
ROME_A = NEWS("rome-therapeutics", "debuts with $50M")
ROME_END = NEWS("rome-therapeutics", "Pretzel emerges")
L.append(cls("rome-therapeutics", status="acquired", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ROME_A, entry_date="2020-04-27",
             note="Repeatome (dark genome) therapeutics, Boston. Founded inside GV: Rosana Kapeller was GV's first "
                  "life-sciences entrepreneur-in-residence, and the firm's own post 'The Road to ROME's Series A' "
                  "(Krishna Yeshwant, 2020-04-27) marks the launch; Fierce Biotech (same day): 'The company starts life with "
                  "$50 million in series A capital from GV, Arch Venture Partners and Partners Innovation Fund.' "
                  "Later a $77M Series B (2021) and a $72M extension backed by J&J and BMS. Fierce Biotech "
                  "(2026-01-13): Rome had been 'winding down its operations', a process that formally concluded weeks "
                  "earlier, and now operates as a wholly owned subsidiary of Pretzel Therapeutics; a sale after a wind-"
                  "down reads acquired (Business Journals, 2026-01-12, 'After winding down, Rome Therapeutics finds a "
                  "local buyer'). The a16z sibling row still reads private; this is fresher cited evidence.",
             rounds=[rnd("2020-04-27", "Series A", 50000000, None, True, ROME_A, "press"),
                     rnd("2021", "Series B", 77000000, None, None, ROME_END, "press"),
                     rnd("2023-09", "Series B extension", 72000000, None, None, ROME_END, "press")]))

# ---- Rox: GV in the Sequoia-led seed (2024); Series A in November 2024; $1.2B at a General Catalyst-led round
L.append(cls("rox", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=TC_ROX,
             asof="2026-03", country="US", city="San Francisco", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SEQUOIA_ROX, entry_date="2024-04",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=SEQUOIA_ROX,
             extra=WV, flags=("model_disputes_source",),
             note="Agentic CRM for sales teams (San Francisco; CEO Ishan Mukherjee). Sequoia's post (2024-11-19): "
                  "'leading their seed round with participation from GV and General Catalyst and now joining this new "
                  "Series A' -> GV entered at the seed (the firm's /ai list: Invested 2024-04) and the company "
                  "graduated with the November 2024 Series A ($50M across seed and A). TechCrunch (2026-03-12): a new "
                  "round that closed in 2025, led by General Catalyst, 'valuing the company at $1.2 billion' (aligned "
                  "with the General Catalyst sibling). The prefilled HR was a one-word name join (Coatue's 'Rox' row is "
                  "Rox Motor, a different company).",
             rounds=[rnd("2024-04", "Seed", None, "Sequoia", True, SEQUOIA_ROX, "press"),
                     rnd("2024-11-19", "Series A", None, None, True, SEQUOIA_ROX, "press"),
                     rnd("2025", "unnamed round at $1.2B", None, "General Catalyst", None, TC_ROX, "press")]))

# ---- Ripple Foods: status and city; the documented $30M round GV led is a Series B, not the band's Series A
RIPPLE_B = NEWS("ripple-foods", "Fundings-in-Brief: Ripple Foods Raises $30m")
L.append(cls("ripple-foods", status="private", rng="below_1b", city="Berkeley", city_src="formd_address",
             focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=RIPPLE_B,
             flags=("stage_disputes_band",),
             note="Pea-protein dairy alternatives (Berkeley CA; every Form D since 2018 files from 901 Gilman Street). "
                  "AgFunderNews (2016-07-14): a '$30 million Series B round' 'led by GV, Google's venture investment "
                  "arm', with Prelude Ventures, Tao Capital Partners, Khosla Ventures and S2G. GV's Andy Wheeler first "
                  "appears on that round's Form D (June 2016), so the entry is the Series B (Growth), not the band's "
                  "Series A; entry date kept from the filing. Still operating: $17M raised with a new CEO in "
                  "December 2025 (Food Business News). Below $1B.",
             rounds=[rnd("2015-12", "earlier round (Form D, not named)", 13637592, None, False, None, "filing"),
                     rnd("2016-07-14", "Series B", 30000000, "GV", True, RIPPLE_B, "press"),
                     rnd("2021-09-21", "Series E", 60000000, "Rage Capital, Ajax Strategies and S2G Ventures", None,
                         None, "press"),
                     rnd("2025-12-03", "unnamed", 17000000, None, None,
                         NEWS("ripple-foods", "Ripple Foods raises $17 million - Food Business News"), "press")]))

# ---- Revolution Medicines: sale consideration for GV-backed EQRx (verdict, no classification)
L.append(verdict("revolution-medicines", "not_member",
                 "Sale consideration (COLLECTION.md s1; the class of decisions.md D11): GV's Revolution Medicines "
                 "shares are the stock Revolution Medicines paid for GV-backed EQRx in its all-stock acquisition "
                 "(2023). The S-4 of 2023-09-13 lists GV 2019, L.P. as a 9.8% holder of EQRx and converts each EQRx "
                 "share into Revolution Medicines common stock at the exchange ratio. The firm lists Revolution "
                 "Medicines only from 2025, with the exit line 'NASDAQ: RVMD, Acquired EQRx 2023'; Revolution "
                 "Medicines' own IPO prospectus (January 2020) names no GV vehicle, Google or Alphabet, and the EDGAR "
                 "full-text sweep finds GV only in the 2023 merger filings. EQRx (listed 2020-2026) is the member.",
                 ec="fund_filing", conf="high", cite=FTS("Revolution Medicines", "S-4")))

# ---- Recorded Future: Google Ventures invested shortly after founding (2010); Insight bought it (2019), Mastercard (2024)
L.append(cls("recorded-future", status="acquired", rng="below_1b", city="Boston", city_src="web_verified",
             focus="Security", stage="undetermined", entry_date="2010",
             note="Threat intelligence. Wikipedia: 'Google Ventures and In-Q-Tel invested \"under $10 million each\" "
                  "into Recorded Future shortly after the company was founded' (2009), reported in 2010; no source "
                  "read names that round, so the stage is undetermined (the prefilled 2017-10-24 entry date is the "
                  "Form D of a later round, where GV's Rich Miner is a director; the entry is 2010). Later rounds "
                  "per the sibling rows: Series C (2012, Balderton), $60M Series E led by Insight Partners (2017). "
                  "Insight bought it for $780M (2019); Mastercard agreed to buy it for $2.65B in September 2024 "
                  "(Crunchbase News, 2024-09-12) and completed the purchase that year (Wikipedia). Headquarters moved from Somerville to downtown Boston in June 2026 "
                  "(Wikipedia); the Balderton and Insight sibling rows still read Somerville.",
             rounds=[rnd("2010", "unnamed early round (Google Ventures and In-Q-Tel)", None, None, True,
                         W("Recorded Future"), "press"),
                     rnd("2017-10-24", "Form D round (Rich Miner director)", 24999995, None, True,
                         jl.FORMD_CITE("recorded-future", 0) if jl.FORMD_ROUNDS("recorded-future") else None,
                         "filing")]))

# ---- RightHand Robotics: GV joined the Menlo-led $23M Series B (December 2018) as a new investor
RR_B = NEWS("righthand-robotics", "raises $23M; Mick Mountz")
L.append(cls("righthand-robotics", status="private", rng="below_1b", country="US", city="Somerville",
             city_src="web_verified", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=RR_B, entry_date="2018-12-17",
             note="Robotic piece-picking for e-commerce fulfilment (Somerville MA). The Robot Report (2018-12-17): "
                  "'closed a $23 million Series B round' led by Menlo Ventures, 'with participation from GV "
                  "(formerly Google Ventures) and existing investors Dream Incubator, Matrix Partners, and Playground "
                  "Global', after $11.3M across a seed (October 2015) and Series A (March 2017) without GV. Later a "
                  "$66M Series C (2022) and a strategic investment from Rockwell Automation (2025); no priced round "
                  "near $1B found.",
             rounds=[rnd("2015-10", "Seed", None, None, False, RR_B, "press"),
                     rnd("2017-03", "Series A", 8000000, None, False, RR_B, "press"),
                     rnd("2018-12-17", "Series B", 23000000, "Menlo Ventures", True, RR_B, "press"),
                     rnd("2022-02-23", "Series C", 66000000, None, None, None, "press")]))

# ---- National Resilience: joined by 2021; the round is not tied to GV in any source read
L.append(cls("resilience", status="private", rng="below_1b", country="US", city="Blue Ash", city_src="web_verified",
             focus="Healthcare & Bio", stage="undetermined",
             note="National Resilience, biomanufacturing (the firm lists it from 2021, partner David Schenkein). Launched "
                  "in 2020 with $800M (its Form D: $755M sold from 2020-10-23, La Jolla address) and raised more than "
                  "$2B plus $250M in bridge financing; in June 2025 it began winding down six plants to focus on its "
                  "Cincinnati hub and Toronto (BioPharma Dive), and it reported $825M in new funding in October 2025 "
                  "(Endpoints headline). No priced post-money was published, so below $1B under Rule A (aligned with "
                  "the 8VC and Lux rows). The company's own site now lists 'Blue Ash (HQ)' (Ohio), which the Lux "
                  "row carries and the 8VC row's San Diego predates. No source read ties GV to a named round, so the "
                  "stage is undetermined. The General Catalyst and Lightspeed 'Resilience' rows are a different "
                  "company (cyber insurance, San Francisco).",
             rounds=[rnd("2020-10-23", "launch financing (Form D)", 755000062, None, None,
                         "https://www.sec.gov/Archives/edgar/data/1834819/000156761921000473/0001567619-21-000473-index.htm",
                         "filing"),
                     rnd("2025-06", "bridge financing", 250000000, None, None,
                         NEWS("resilience", "to scale back operations"), "press"),
                     rnd("2025-10", "new funding (form not read)", 825000000, None, None,
                         NEWS("resilience", "National Resilience secures $825M"), "press")]))

# ---- Sana Biotechnology: GV 2019 signed the February 2019 rights agreement; A-2 or B not separable
SANA_IRA = FTS("Sana Biotechnology", "DRS")
SANA_S1 = "https://www.sec.gov/Archives/edgar/data/1770121/000119312521007483/d60414ds1.htm"
L.append(cls("sana-biotechnology", city="Seattle", focus="Healthcare & Bio", stage="undetermined",
             rng="below_1b", usd=877130000, val_src="web_verified", val_cite=CAP("sana"), asof=TODAY, extra=WV,
             flags=("model_disputes_source",),
             note="Engineered cells as medicines (Seattle; NASDAQ: SANA). GV is named among the backers of the $700M "
                  "'initial financing' disclosed in June 2020 (BioSpace, 2020-06-23). The IPO registration shows the preferred "
                  "history: Series A-1 (2018), Series A-2 ($216.1M, February 2019, plus $7.9M in October 2019) and "
                  "Series B ($435.6M, June 2020) under one Series A-2/B purchase agreement; GV 2019, L.P. is a party "
                  "to the amended investors' rights agreement dated 2019-02-13 as filed with the IPO registration "
                  "(Exhibit 10.1 of the December 2020 DRS/A), which also carries later joiners, so whether GV entered at the A-2 or only at the B is not established. "
                  "Stage undetermined. Market cap $877.13M on 2026-09-28 (stockanalysis), replacing the stale "
                  "prefilled $295.1M; still below $1B.",
             rounds=[rnd("2019-02", "Series A-2", 216100000, None, None, SANA_S1, "filing"),
                     rnd("2019-10", "Series A-2 (additional closing)", 7900000, None, None, SANA_S1, "filing"),
                     rnd("2020-06", "Series B", 435600000, None, None, SANA_S1, "filing")]))

# ---- Rocket Lawyer: Google Ventures in the $18.5M Series D (July 2011)
L.append(cls("rocket-lawyer", status="private", rng="below_1b", city="San Francisco", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Rocket Lawyer"),
             entry_date="2011-07",
             note="Online legal documents and attorney services for consumers and small businesses (San Francisco). "
                  "Wikipedia: 'In July 2011, the company raised $18.5 million in a Series D round of financing from "
                  "August Capital, Google Ventures and Investor Growth Capital' (Series D = Growth). Still operating "
                  "(2025-26 coverage); its April 2021 raise of $223M (Fortune) published no valuation, so below $1B "
                  "under Rule A.",
             rounds=[rnd("2011-07", "Series D", 18500000, None, True, W("Rocket Lawyer"), "press"),
                     rnd("2021-04-21", "growth financing", 223000000, None, None, None, "press")]))

# ---- Schematic Labs (SoundTracking): Google Ventures among several rounds' investors; the entry round is not named
L.append(cls("schematic-labs", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Maker of SoundTracking, the 'Instagram for songs' app. TechCrunch (2014-08-04): Rhapsody acquired "
                  "Schematic Labs, which had 'raised over $5.7 million dollars from Accel Partners, SoftBank Capital, "
                  "True Ventures and Google Ventures plus angels ... over several rounds'. No source read says which "
                  "round Google Ventures joined, so the stage is undetermined.",
             rounds=[]))

# ---- Roboflow: stage prefilled (Form D band: the GV-led $40M Series B); status, city, band
L.append(cls("roboflow", status="private", rng="below_1b", city="Des Moines", city_src="formd_address",
             focus="DevTools & APIs",
             note="Computer-vision developer platform. Fortune (2024-11-19): 'Roboflow has raised $40 million for its "
                  "Series B', 'led by GV' (the firm's own post says the same). City from its 2024 Form D (500 Locust "
                  "Street, Des Moines), where the YC sibling row carries San Francisco from its directory. Momentum "
                  "check 2026-09-28 (Google News): no round after the Series B; valuation undisclosed; below $1B.",
             extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY,
                    "valuation_citation": NEWS("roboflow", "raises $40 million Series B")}))

# ---- Savioke (now Relay Robotics): Google Ventures in the $2M seed (April 2014); Series B by 2018
SAVIOKE_B = NEWS("savioke", "Savioke Raises $13.4M in Series B")
L.append(cls("savioke", status="acquired", rng="below_1b", city="San Jose", focus="Industrial & Robotics",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SAVIOKE_SEED,
             entry_date="2014-04-09",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=SAVIOKE_B,
             note="Service robots for hotels and hospitals. TechCrunch (2014-04-09): a seed round of '$2 million from "
                  "Jerry Yang's AME Cloud Ventures, Google Ventures, Morado Venture Partners and other individual "
                  "investors' (IEEE Spectrum the same day: led by Morado). Graduated: 'Savioke Raises $13.4M in "
                  "Series B Funding' (FinSMEs, 2018-07-06; the page refuses scripted reads, the headline names the "
                  "round). The business passed to a newly formed company, Relay Robotics, in 2022: The Robot Report "
                  "(2022-05-02, 'Savioke is now Relay Robotics') quotes the company on 'forming a new company over a "
                  "name change' and reports the new company's $10M Series A led by MK Capital, so the row reads "
                  "acquired with Relay Robotics as successor (aligned with the Felicis sibling's status; that row's "
                  "not_graduated sits beside this Series B).",
             rounds=[rnd("2014-04-09", "Seed", 2000000, "Morado Venture Partners", True, TC_SAVIOKE_SEED, "press"),
                     rnd("2018-07-06", "Series B", 13400000, None, None, SAVIOKE_B, "press")]))

# ---- Scan: Google Ventures in the $1.7M seed (February 2012); $7M Series A (October 2013); Snapchat bought it (2014)
TC_SCAN_SEED = ("https://techcrunch.com/2012/02/23/scan-gets-1-7m-from-google-ventures-and-shervin-pishevar-to-make-qr-"
                "codes-actually-useful/")
TC_SCAN_A = "https://techcrunch.com/2013/10/09/thing/"
L.append(cls("scan", status="acquired", rng="below_1b", city="Provo", city_src="web_verified",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SCAN_SEED, entry_date="2012-02-23",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_SCAN_A,
             note="QR-code scanning apps (Provo, Utah). TechCrunch (2012-02-23): the 'Provo, Utah-based' company 'raised "
                  "over $1.7 million in seed funding', Shervin Pishevar of Menlo Ventures leading, with Google Ventures, "
                  "Charles River Ventures, Start Fund, Social+Capital and others. Graduated: a $7M Series A from Entree "
                  "Capital and existing investors including Menlo Ventures (TechCrunch, 2013-10-09). Acquired by "
                  "Snapchat in 2014 for a reported $54M (Wikipedia). The Menlo sibling row for 'Scan' (unresolved, "
                  "San Francisco) is this company.",
             rounds=[rnd("2012-02-23", "Seed", 1700000, "Menlo Ventures (Shervin Pishevar)", True, TC_SCAN_SEED, "press"),
                     rnd("2013-10-09", "Series A", 7000000, "Entree Capital", None, TC_SCAN_A, "press")]))

# ---- Sanas: GV joined the Insight-led $32M Series A (June 2022) as a new investor
SANAS_A = NEWS("sanas", "Sanas Raises $32M for Breakthrough")
L.append(cls("sanas", status="private", rng="below_1b", country="US", city="Palo Alto", city_src="web_verified",
             focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=SANAS_A, entry_date="2022-06-22",
             extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY,
                    "valuation_citation": NEWS("sanas", "Sanas gets $65M in funding")},
             note="Real-time accent translation and speech AI for call centres (Palo Alto). The company's release (Palo "
                  "Alto, 2022-06-22): $32M Series A led by Insight Partners, with new investors GV and Assurant "
                  "Ventures and existing investors General Catalyst, Human Capital, Quiet Capital and DN Capital. "
                  "Momentum check 2026-09-28 (Google News): the latest round is the $65M Series B of February 2025 "
                  "(SiliconANGLE, AI Insider), with no valuation published; no priced round at $1B or more.",
             rounds=[rnd("2022-06-22", "Series A", 32000000, "Insight Partners", True, SANAS_A, "company"),
                     rnd("2025-02-19", "Series B", 65000000, None, None,
                         NEWS("sanas", "Sanas gets $65M in funding"), "press")]))

# ---- Rise: Google Ventures in the Floodgate-led $2.3M seed; One Medical bought it (2016)
TC_RISE = "https://techcrunch.com/2014/02/12/rise/"
L.append(cls("rise", status="acquired", rng="below_1b", country="US", city="San Francisco", city_src="formd_address",
             focus="Healthcare & Bio",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_RISE, entry_date="2014-02",
             note="Mobile nutrition coaching with personal dietitians (Rise Labs, San Francisco; founders Suneel Gupta "
                  "and Stuart Parmenter). TechCrunch (2014-02-12): 'The company had raised $2.3 million in seed "
                  "funding, which was led by Floodgate, along with Cowboy Ventures, Google Ventures, and Greylock' "
                  "(entry dated to that report; the round itself closed earlier). Its only Form D (2015, $0.8M of a "
                  "$1M offering, 180 Capp Street) is a small follow-on, below the era's step-up. Acquired by One Medical "
                  "Group in 2016 (the firm's own exit line). Graduation left for the graduation pass.",
             rounds=[rnd("2014-02", "Seed", 2300000, "Floodgate", True, TC_RISE, "press"),
                     rnd("2015-03-26", "Form D offering (unnamed)", 800000, None, None,
                         "https://www.sec.gov/Archives/edgar/data/1639228/000163922815000001/primary_doc.xml", "filing")]))

# ---- Reserve: listed from 2014 (Kevin Rose); GV is not named in the Series A (2015) or B (2017) reports
TC_RESERVE_A = "https://techcrunch.com/2015/02/11/reserve-series-a/"
TC_RESERVE_B = "https://techcrunch.com/2017/02/01/reserve-series-b/"
L.append(cls("reserve", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Restaurant reservation and payments app from Expa (New York). The firm lists it from 2014 (partner "
                  "Kevin Rose). TechCrunch: a $15M Series A led by Human Ventures and Expa with existing backers First "
                  "Round, Lowercase, Advancit and Sherpa (2015-02-11; $17.3M raised in total, so about $2.3M came "
                  "earlier) and a $10M Series B led by Expa (2017-02-01); neither names GV, and no source read dates "
                  "or names the round GV joined, so the stage is undetermined. Acquired by Resy in November 2018 "
                  "(Eater, NYT and AlleyWatch headlines; the firm's own exit line).",
             rounds=[rnd(None, "earlier funding (unnamed, about $2.3M)", 2300000, None, None, TC_RESERVE_A, "press"),
                     rnd("2015-02-11", "Series A", 15000000, "Human Ventures and Expa", None, TC_RESERVE_A, "press"),
                     rnd("2017-02-01", "Series B", 10000000, "Expa", None, TC_RESERVE_B, "press")]))

# ---- Rockbot: listed from 2013; still operating (Oakland); the round GV joined is not named in any source read
L.append(cls("rockbot", status="private", rng="below_1b", country="US", city="Oakland", city_src="formd_address",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Licensed in-venue music, digital signage and retail media for businesses (Rockbot, Inc., 1308 "
                  "Broadway, Oakland, on its 2015 Form Ds; the site carries a 2026 copyright, so it still operates). "
                  "The firm lists it from 2013 (partner Dave Munichiello 2014-15). TechCrunch (2014-08-27) reports a "
                  "strategic round from Universal Music Group with Detroit Venture Partners, XG Ventures and Susa "
                  "Ventures, without GV; the 2015 Form Ds ($0.3M and $2.7M) name no GV person. No source read names "
                  "the round GV joined: stage undetermined. No priced round near $1B.",
             rounds=[rnd("2014-08-27", "strategic round (UMG, undisclosed)", None, "Universal Music Group", None,
                         "https://techcrunch.com/2014/08/27/rockbot-umg/", "press"),
                     rnd("2015-05-15", "Form D offering", 2711441, None, None, None, "filing")]))

# ---- Rocana (formerly ScalingData): listed from 2014; Google Ventures led the $15M Series B (May 2015)
TC_ROCANA_B = "https://techcrunch.com/2015/05/01/rocana-lands-15m-to-bring-big-data-analysis-to-it-ops/"
L.append(cls("rocana", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Data Infrastructure", stage="undetermined",
             note="IT operations analytics on Hadoop (formerly ScalingData; offices in San Francisco and Boston). "
                  "TechCrunch (2015-05-01): '$15 million in Series B funding' 'led by Google Ventures', with General "
                  "Catalyst and Toba Capital, bringing the total to $19.4M. The firm's archived listing already "
                  "carries ScalingData in 2014, before that round, so GV's money went in with the earlier $4.4M, a "
                  "round no source read names: stage undetermined. Splunk bought its staff and technology assets in "
                  "October 2017 (SiliconANGLE headline; the firm's exit line 'Acquired by Splunk, 2017'), a sale of the "
                  "business, so acquired.",
             rounds=[rnd(None, "earlier funding (unnamed, about $4.4M)", 4400000, None, None, TC_ROCANA_B, "press"),
                     rnd("2015-05-01", "Series B", 15000000, "Google Ventures", True, TC_ROCANA_B, "press")]))

# ---- Rani Therapeutics: listed from 2013; GV an existing investor by 2018; the round GV entered is not named
RANI_S1 = "https://www.sec.gov/Archives/edgar/data/1856725/000119312521211922/d151628ds1.htm"
L.append(cls("rani-therapeutics", country="US", city="San Jose", focus="Healthcare & Bio", stage="undetermined",
             rng="below_1b", usd=108170000, val_src="web_verified", val_cite=CAP("rani"), asof=TODAY, extra=WV,
             flags=("model_disputes_source",),
             note="Robotic pill for oral delivery of biologics (San Jose; NASDAQ: RANI). The firm lists it from its "
                  "2013 page (partner Blake Byers). Drug Delivery Business (2018-02-08): the $53M raise added "
                  "GeneScience and Shire to 'existing investors like Alphabet's GV, Novartis and AstraZeneca'; the "
                  "Q3 2021 10-Q records warrants held by GV 2017, L.P. exercised in July 2021. The IPO prospectus "
                  "(July 2021) lists Series A, B (May 2013), C (Novartis joined, around 2015), C-1, D (Takeda, "
                  "November 2017) and E ($75M, 2020-21) units but no GV holding; with the 2013 listing the entry was "
                  "the Series A or the Series B, and no source read says which: stage undetermined. Market cap "
                  "$108.17M on 2026-09-28 (stockanalysis), replacing the stale prefilled $65M; band unchanged.",
             rounds=[rnd("2013-05", "Series B", None, None, None, RANI_S1, "filing"),
                     rnd("2018-02-08", "financing ($53M; round not named)", 53000000, None, True,
                         NEWS("rani-therapeutics", "nabs $53m"), "press"),
                     rnd("2020", "Series E", 75000000, None, None, RANI_S1, "filing")]))

# ---- RAPT Therapeutics (formerly FLX Bio): GV 2017 and GV 2019 in the Series C/C-2 era; GSK bought it (2026)
RAPT_IRA = FTS("RAPT", "DRS")
L.append(cls("rapt-therapeutics", rng="below_1b", country="US", city="South San Francisco",
             focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=RAPT_IRA,
             note="Immunology and oncology small molecules (South San Francisco; formerly FLX Bio). The amended "
                  "investors' rights agreement of 2018-12-18 (filed with the IPO registration) is signed by GV 2017, "
                  "L.P. and GV 2019, L.P.; its recitals make the parties either holders of the Series A, B and C or "
                  "buyers of the Series C-2. The IPO prospectus dates the preferred sales: Series B April 2016 ($50M), "
                  "Series C December 2017 and June 2018 ($59.9M), Series C-2 December 2018 to June 2019 ($37.1M). "
                  "A GV 2017 vehicle points to a 2017-18 purchase, after the 2016 Series B, so GV entered at the "
                  "Series C or C-2, both Growth. Which close is not established, so no entry date is given. GSK agreed to buy RAPT for "
                  "$2.2B in January 2026 (Pharmaceutical Executive, 2026-01-20); stockanalysis shows the stock no "
                  "longer trades (last cap $1.79B), so acquired, no mark.",
             rounds=[rnd("2016-04", "Series B", 50000000, None, False, "https://www.sec.gov/Archives/edgar/data/1673772/000119312519189775/d723949ds1.htm", "filing"),
                     rnd("2017-12", "Series C (first close)", 29927851, None, None, "https://www.sec.gov/Archives/edgar/data/1673772/000119312519189775/d723949ds1.htm", "filing"),
                     rnd("2018-06", "Series C (second close)", 29900000, None, None, "https://www.sec.gov/Archives/edgar/data/1673772/000119312519189775/d723949ds1.htm", "filing"),
                     rnd("2018-12", "Series C-2", 37100000, None, True, RAPT_IRA, "filing")]))

# ---- Scalus: backed by Google Ventures (with Sherpa); its later fate is not established
L.append(cls("scalus", status="unknown", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="undetermined",
             note="Workflow automation and client-onboarding software spun out of BackOps (San Francisco; founder "
                  "Kristen Koh Goldstein). Launched with $10M in funding (Insightful Accountant headline) from backers "
                  "including Google Ventures and Sherpa (CMSWire, April 2016, on HireAthena, the back-office service "
                  "later spun off from BackOps and Scalus, whose platform runs on Scalus's workflow technology). No "
                  "source read names the round GV joined (stage undetermined) or says what became of Scalus itself "
                  "after 2016 (status unknown: the firm's listing links only a LinkedIn page and carries no exit line).",
             rounds=[rnd(None, "launch funding (not named)", 10000000, None, None,
                         "https://insightfulaccountant.com/accounting-tech/vendor-news/scalus-launches/", "press")]))

# ---- Robinhood: Google Ventures provided the initial funding the $3M seed added to (2013); Series A 2014
RH_SEED = NEWS("robinhood", "Robinhood Closes $3 Million in Seed Funding")
L.append(cls("robinhood", status="public", rng="100b_plus", usd=104710000000, val_src="web_verified",
             val_cite=CAP("hood"), asof=TODAY, city="Menlo Park", focus="Fintech & Payments",
             stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=RH_SEED, entry_date="2013",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=W("Robinhood Markets"),
             extra=WV,
             note="Commission-free brokerage (Menlo Park; NASDAQ: HOOD). The company's release (Redwood City, "
                  "2013-12-18) closed '$3 million in seed funding': 'Index Ventures led the round, with a16z seed, "
                  "Rothenberg Ventures and angel investors ... adding to the initial funding from Google Ventures' "
                  "(TechCrunch the same day: 'it's added to its initial funding from Google Ventures'). GV's money "
                  "is the first cheque of that seed financing; entry dated to 2013 (the company was founded in April "
                  "2013), medium confidence on the label. Graduated: $13M Series A in September 2014 with returning "
                  "investor Index and new investor Ribbit (Wikipedia). Market cap $104.71B on 2026-09-28 (stockanalysis), aligned with the Ribbit sibling "
                  "row of the same day.",
             rounds=[rnd("2013", "initial funding (seed stage)", None, "Google Ventures", True, RH_SEED, "company"),
                     rnd("2013-12-18", "Seed", 3000000, "Index Ventures", True, RH_SEED, "company"),
                     rnd("2014-09", "Series A", 13000000, None, None, W("Robinhood Markets"), "press")]))

# ---- Ripple (OpenCoin): Google Ventures and IDG in the May 2013 angel-stage round; Series A January 2015
COINDESK_RIPPLE = NEWS("ripple-labs", "Google Ventures invests in Bitcoin")
FINOVATE_RIPPLE = NEWS("ripple-labs", "Ripple Labs Raises $30 Million in Series A")
L.append(cls("ripple-labs", rng="10b_plus", usd=40000000000, val_src="web_verified", val_cite=CB_RIPPLE,
             asof="2025-11-05", city="San Francisco", focus="Crypto & Web3",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=COINDESK_RIPPLE, entry_date="2013-05-14",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=FINOVATE_RIPPLE,
             extra=WV, flags=("model_disputes_source",),
             note="Ripple Labs (OpenCoin in 2013), payments and stablecoin infrastructure, San Francisco. CoinDesk "
                  "(2013-05-14): Google Ventures and IDG Capital Partners invested in 'an additional round of "
                  "funding', weeks after the angel round of Andreessen Horowitz, FF Angel, Lightspeed and others; "
                  "Wikipedia's table calls both 2013 rounds angel rounds, and Finovate counts '$9 million in 2013 "
                  "through angel and seed funding rounds'. An angel-stage round is read as Seed (model, medium), as the "
                  "Lightspeed and a16z sibling rows read the April round. Graduated: $30M Series A, January 2015, "
                  "with IDG, Google Ventures and a16z (Finovate, 2015-01-28). Mark: $500M at $40B (Crunchbase News, "
                  "2025-11-05), aligned with the Lightspeed sibling; the prefilled $10B was stale. A September 2026 "
                  "company buyback at a reported $50B is a secondary, noted only.",
             rounds=[rnd("2013-05-14", "angel round (second of 2013)", None, None, True, COINDESK_RIPPLE, "press"),
                     rnd("2015-01-28", "Series A", 30000000, None, True, FINOVATE_RIPPLE, "press"),
                     rnd("2025-11-05", "unnamed round at $40B", 500000000,
                         "Fortress Investment Group and Citadel Securities affiliates", None, CB_RIPPLE, "press")]))

# ---- Sardine: Google Ventures in the a16z-led $51.5M Series B (September 2022); $70M Series C (February 2025)
SARDINE_B = NEWS("sardine", "Sardine raises $51.5M led by a16z")
SARDINE_C = NEWS("sardine", "Wraps Up $70M Series C")
SARDINE_CX = NEWS("sardine", "leads $25 million Series C extension")
L.append(cls("sardine", status="private", rng="below_1b", country="US", city="San Francisco", focus="Security",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SARDINE_B, entry_date="2022-09-20",
             extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY, "valuation_citation": SARDINE_CX},
             note="Fraud and compliance platform for fintechs and banks. TechCrunch (2022-09-20): '$51.5 million in a "
                  "Series B round led by Andreessen Horowitz's (a16z) Growth Fund', participants including Google "
                  "Ventures, after a $19.5M Series A earlier in 2022 that no source read ties to GV; the firm's own "
                  "/ai list dates its first investment 2022-09 and a re-investment 2024-12, matching the Series B and "
                  "the $70M Series C led by Activant (Crunchbase News, 2025-02-11); a $25M Series C extension led by "
                  "National Bank of Canada followed in May 2026 (Finextra, 2026-05-21). No valuation disclosed at any "
                  "of them. Momentum check 2026-09-28 (Google News): no priced round at $1B or more.",
             rounds=[rnd("2022-02-11", "Series A", 19500000, None, None, SARDINE_B, "press"),
                     rnd("2022-09-20", "Series B", 51500000, "Andreessen Horowitz", True, SARDINE_B, "press"),
                     rnd("2025-02-11", "Series C", 70000000, "Activant Capital", True, SARDINE_C, "press"),
                     rnd("2026-05-21", "Series C extension", 25000000, "National Bank of Canada", None, SARDINE_CX,
                         "press")]))

# ---- RhyGaze: GV led the USD 86M Series A (January 2025); Basel
RHYGAZE_A = NEWS("rhygaze", "RhyGaze raises USD 86 million")
L.append(cls("rhygaze", status="private", rng="below_1b", country="CH", country_src="web_verified",
             country_cite=RHYGAZE_A, city="Basel", city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=RHYGAZE_A, entry_date="2025-01-15",
             note="Gene therapy for vision restoration, spun out of the Institute of Molecular and Clinical "
                  "Ophthalmology Basel (based in Basel and Philadelphia). Startupticker (2025-01-15): 'a Series A "
                  "financing of USD 86 million', 'Led by GV (Google Ventures)' alongside ARCH Venture Partners, F-Prime "
                  "Capital and founding investors BioGeneration Ventures and Novartis Venture Fund. No later round "
                  "found; below $1B.",
             rounds=[rnd("2025-01-15", "Series A", 86000000, "GV", True, RHYGAZE_A, "press")]))

# ---- Roger (Sanos Services, Berlin): GV and Partech led the EUR 7M seed (August 2024)
SC_ROGER = "https://siliconcanals.com/german-startup-roger-secures-7m/"
L.append(cls("roger", status="private", rng="below_1b", country="DE", country_src="web_verified",
             country_cite=SC_ROGER, city="Berlin", city_src="web_verified", focus="Healthcare & Bio",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SC_ROGER, entry_date="2024-08-13",
             note="Practice-management and patient-relationship software plus admin services for dental practices "
                  "(Berlin; operating company Sanos Services GmbH per the site's imprint; founded 2021 by Victor "
                  "Charlier and Andreas Wolff). Silicon Canals (2024-08-13): 'Berlin-based Roger ... has secured €7M "
                  "in a seed funding round' 'led by GV (Google Ventures) and Partech'. No later round found; below "
                  "$1B. Graduation left for the graduation pass (the entry passed the 24-month window in August "
                  "2026).",
             rounds=[rnd("2024-08-13", "Seed", None, "GV and Partech", True, SC_ROGER, "press")]))

# ---- Resolution Games: listed from 2015 (Avid Larizadeh Duggan); GV a returning investor in the 2018 Series B
RG_B = NEWS("resolution-games", "Closes $7.5 Million Series B")
L.append(cls("resolution-games", status="private", rng="below_1b", city="Stockholm", city_src="web_verified",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="VR and AR game studio (Stockholm; CEO Tommy Palm). The firm lists it from 2015. The company's release "
                  "(2018-10-23) names GV among the returning investors of the $7.5M Series B led by MizMaa Ventures, "
                  "which brought total funding to $13.5M (TechCrunch the same day: at an $87.5M valuation), so GV's "
                  "money went into the roughly $6M raised before it; no source read names or dates that round (the "
                  "Creandum sibling calls it a seed, uncited), so the stage is undetermined. $25M Series C in July 2021 "
                  "(GamesIndustry.biz); still publishing games (TechCrunch, January 2025). Below $1B.",
             rounds=[rnd(None, "earlier funding (unnamed, about $6M)", 6000000, None, True, RG_B, "company"),
                     rnd("2018-10-23", "Series B", 7500000, "MizMaa Ventures", True, RG_B, "company"),
                     rnd("2021-07-14", "Series C", 25000000, None, None, None, "press")]))

# ---- Rilla: listed from 2025 (Crystal Huang); no source read names or dates GV's round
RILLA_NEWS = NEWS("rilla", "The Home Depot to Advance Customer Experience")
L.append(cls("rilla", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="AI & Applied AI", stage="undetermined",
             extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY, "valuation_citation": RILLA_NEWS},
             note="AI coaching for in-person and field sales teams, recording and analysing reps' conversations "
                  "(founded 2019 by Sebastian Jimenez; Long Island City, New York, per Fortune, 2025-07-11). The firm "
                  "lists it from 2025 (partner Crystal Huang) and names it among its agentic-AI vertical bets (post, "
                  "2026-03-11). No source read names, sizes or dates the round GV joined: stage undetermined. Still "
                  "operating (The Home Depot rollout, PR Newswire, 2026-01-13). Momentum check 2026-09-28 (Google "
                  "News, two queries): no funding report at all, so no priced round at $1B or more.",
             rounds=[]))

# ---- Rodin Therapeutics: listed from 2017 (Ben Robbins); Alkermes bought it (November 2019)
RODIN_ALKS = NEWS("rodin-therapeutics", "Alkermes Buys Rodin")
L.append(cls("rodin-therapeutics", status="acquired", rng="below_1b", country="US", city="Cambridge",
             city_src="formd_address", focus="Healthcare & Bio", stage="undetermined",
             note="Epigenetic (HDAC complex) therapeutics for neurological disorders (300 Technology Square, Cambridge "
                  "MA, on its 2017 Form D; BioSpace calls it Boston-based). The firm lists it from its October 2017 "
                  "page (partner Ben Robbins). Its only Form D (first sale 2017-08-30: $10.8M of a $27.1M offering) "
                  "names Atlas people and no GV person, and no source read names the round GV joined: stage "
                  "undetermined. Alkermes bought it on 2019-11-18 for $100M upfront plus up to $850M in milestones "
                  "(BioSpace).",
             rounds=[rnd("2017-08-30", "Form D offering 0001716694-17-000001 (round not named)", 10826792, None,
                         None, None, "filing")]))

import os  # noqa: E402
jl.write("j11", L, record=os.environ.get("J11_DRY") != "1")
