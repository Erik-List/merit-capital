"""PRO-75 GV grind, judge j4: queue batch 4 (45 member rows, Currencycloud to EpiBiologics).

Every citation below is a URL a tool printed (judge_lib helpers, the news decoder, WebFetch of a tag or listing page,
an EDGAR index) and that was read before it was cited. Market caps: stockanalysis.com, read 2026-09-28.
Disputes of pre-filled values (flagged in the line): Decibel, Denali and Dialpad (the Form D band read a later
filing as the entry), Desktop Metal (entry date), Desmos, Digit and Doppler (one-word Wikidata joins), DocuSign,
Denali and Editas (a public row takes its market cap, not the SEC float), Dapper Labs and Devoted Health (the
unicorn-list figure re-sourced to the priced round).
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
CHECK = "2026-09-28"
GRAD_OPEN = " Graduation left for the graduation pass."
WV = {"valuation_range_source": "web_verified"}


def momentum(cite, asof=CHECK):
    """A below_1b momentum-slice check recorded on the row (COLLECTION.md s6): source, citation and date."""
    return {"valuation_range_source": "web_verified", "valuation_citation": cite, "valuation_asof": asof}


# ---------------------------------------------------------------- Currencycloud
TC_CC = ("https://techcrunch.com/2017/03/08/currencycloud-maker-of-payment-tools-for-fintech-startups-raises-20m-"
         "led-by-gv/")
CBN_CC = NEWS("currencycloud", "Visa, GV And More Invest")
L.append(cls("currencycloud", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=TC_CC, city="London", city_src="web_verified", focus="Fintech & Payments",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_CC, entry_date="2017-03-08",
             note="Cross-border payments APIs, London. GV led the GBP 20M ($25M) Series D in March 2017 as a new "
                  "investor, its first fintech investment in Europe (TechCrunch, 'London-based'); GV was an existing "
                  "backer in the $80M Series E of January 2020 (Crunchbase News). Visa bought it in 2021 (Reuters "
                  "headline, 'at 700 million pounds valuation'; the firm's own exit line 'Acquired by Visa, 2021').",
             rounds=[rnd("2017-03-08", "Series D", 25000000, "GV", True, TC_CC, "press"),
                     rnd("2020-01-27", "Series E", 80000000, None, True, CBN_CC, "press")]))

# ---------------------------------------------------------------- CyberGRX
CS_CG = NEWS("cybergrx", "Investors drop")
SE_CG = NEWS("cybergrx", "December ’18 Startup Funding")
SA_CG = NEWS("cybergrx", "ProcessUnity and CyberGRX unite")
L.append(cls("cybergrx", status="acquired", rng="below_1b", country="US", city="Denver", city_src="web_verified",
             focus="Security", stage="undetermined",
             note="Third-party cyber risk exchange, Denver. Google Ventures is named among the investors when the "
                  "company announced $20M in April 2017 ($29M raised in total; CyberScoop), but no source names that "
                  "round or says whether GV was already in the $9M of 2016, and the next round is a named Series C "
                  "($30M, December 2018, Scale Venture Partners leading, GV an existing investor). Stage undetermined; "
                  "no entry date. ProcessUnity and its investors acquired CyberGRX in July 2023 (SiliconANGLE).",
             rounds=[rnd("2016-07", "unnamed round", 9000000, None, None, NEWS("cybergrx", "Denver cyber-security"),
                         "press"),
                     rnd("2017-04-18", "unnamed round", 20000000, None, True, CS_CG, "press"),
                     rnd("2018-12", "Series C", 30000000, "Scale Venture Partners", True, SE_CG, "press")]))

# ---------------------------------------------------------------- Cymbal
DC_CY = NEWS("cymbal", "Human Readable")
L.append(cls("cymbal", status="defunct", rng="below_1b", country="US", city="San Francisco",
             city_src="model_knowledge", focus="Crypto & Web3", stage="undetermined",
             note="Social Ethereum block explorer founded by Eric Feng (ex-Hulu CTO). Decrypt (July 2023) reports "
                  "$18.5M raised in total with GV among the investors and names no round, so the stage is "
                  "undetermined. cymbal.xyz serves only a logo splash page (read 2026-09-28) and nothing has been "
                  "reported since mid-2023: defunct, aligned with First Round's row (status and city), though the firm "
                  "still lists it.",
             rounds=[rnd("2023-07-19", "total raised to date, no round named", 18500000, None, True, DC_CY,
                         "press")]))

# ---------------------------------------------------------------- Dandelion Energy
PR_DE = NEWS("dandelion-energy", "Series C Funding Round to Expand")
L.append(cls("dandelion-energy", status="private", rng="below_1b", city="Arlington", city_src="web_verified",
             focus="Climate & Energy",
             note="Residential geothermal heating and cooling, spun out of X. GV led the $40M Series C of September "
                  "2024; the release is datelined Arlington, Virginia and gives it as the headquarters (the move is in "
                  "the Washington Business Journal's headline). No valuation disclosed and no later priced round "
                  "found.",
             rounds=[rnd("2024-09-24", "Series C", 40000000, "GV", True, PR_DE, "company")]))

# ---------------------------------------------------------------- Dapper Labs
PR_DL = NEWS("dapper-labs", "Raises $15M in Financing")
CD_DL = "https://www.coindesk.com/business/2021/09/22/dapper-labs-said-to-reach-76b-valuation-in-250m-funding-round"
L.append(cls("dapper-labs", city="Vancouver", city_src="web_verified", focus="Crypto & Web3",
             usd=7600000000, rng="1b_plus", val_src="web_verified", val_cite=CD_DL, asof="2021-09-22",
             stage="undetermined", entry_date="2018-11-01", flags=["stale"], clear=["unicorn_name_match"], extra=WV,
             note="CryptoKitties, NBA Top Shot and Flow, Vancouver. GV joined the $15M round of November 2018 led by "
                  "Venrock (the company's release, datelined Vancouver; $27.85M raised in total, after the $12M "
                  "Series A of March 2018 that a16z and USV led, per their rows); no source names the November round, "
                  "so the stage "
                  "is undetermined with the entry date kept. The last priced mark is the $250M round led by Coatue at "
                  "$7.6B, GV participating (CoinDesk, 2021-09-22), re-sourced from the unicorn list and stale; aligned "
                  "with the Coatue and USV rows. Accel's 'Dapper' row is a different company (Yahoo's 2010 purchase).",
             rounds=[rnd("2018-11-01", "unnamed round", 15000000, "Venrock", True, PR_DL, "company"),
                     rnd("2021-09-22", "unnamed round", 250000000, "Coatue", True, CD_DL, "press")]))

# ---------------------------------------------------------------- Dasient
TC_DA = "https://techcrunch.com/2011/02/07/google-ventures-invests-in-web-security-company-dasient/"
L.append(cls("dasient", status="acquired", rng="below_1b", city="Sunnyvale", city_src="web_verified",
             focus="Security", stage="undetermined", entry_date="2011-02-07",
             note="Anti-malware for websites and ad networks, Sunnyvale (Wikipedia). Google Ventures invested in "
                  "February 2011, amount undisclosed and no round named, after $4M from Benhamou Global Ventures, "
                  "Floodgate, Radar Partners and others (TechCrunch): stage undetermined. Twitter acquired it in "
                  "January 2012 (Wikipedia; the firm's exit line).",
             rounds=[rnd("2011-02-07", "unnamed round", None, None, True, TC_DA, "press")]))

# ---------------------------------------------------------------- DataFox
PR_DF = NEWS("datafox", "Brings Big Data Analytics")
TC_DF14 = NEWS("datafox", "Offers Predictive Intelligence")
TC_DF15 = "https://techcrunch.com/2015/07/22/datafox-hunts-down-5-million-in-fresh-funding/"
TC_DF18 = NEWS("datafox", "Oracle acquires DataFox")
L.append(cls("datafox", status="acquired", rng="below_1b", country="US", city="Palo Alto", city_src="web_verified",
             focus="SaaS", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PR_DF,
             entry_date="2014-02-05",
             note="Private-company intelligence platform. The launch release (Palo Alto, 2014-02-05) names a seed "
                  "round backed by Google Ventures; TechCrunch later put it at $1.78M. The $5M of July 2015 (Goldman "
                  "Sachs and Green Visor) was structured as a seed, 'not a Series A' (TechCrunch, 'Palo Alto-based'), "
                  "so it does not graduate the row by name; DataFox was last valued at $33M in January 2017 and had "
                  "raised just under $19M when Oracle bought it in October 2018 (TechCrunch)." + GRAD_OPEN,
             rounds=[rnd("2014-02", "Seed", 1780000, None, True, TC_DF14, "press"),
                     rnd("2015-07-22", "Seed (structured as seed, not a Series A)", 5000000,
                         "Goldman Sachs and Green Visor Capital", None, TC_DF15, "press")]))

# ---------------------------------------------------------------- dbt Labs
PR_DBT = NEWS("dbt-labs", "raises $222M in Series D funding")
L.append(cls("dbt-labs", status="acquired", rng="below_1b", country="US", city="Philadelphia",
             city_src="web_verified", focus="Data Infrastructure", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=PR_DBT, entry_date="2022-02-24",
             note="Analytics engineering (dbt), Philadelphia. GV came in as a new investor in the $222M Series D of "
                  "February 2022, led by Altimeter at a $4.2B valuation (the company's release, datelined "
                  "Philadelphia). Merged into Fivetran in an all-stock deal completed in 2026 (the firm's own exit "
                  "line 'Acquired by Fivetran, 2026'); acquired, aligned with the a16z, Coatue and Sequoia rows.",
             rounds=[rnd("2022-02-24", "Series D", 222000000, "Altimeter", True, PR_DBT, "company")]))

# ---------------------------------------------------------------- Decibel Therapeutics
S1_DB = FTS("Decibel", "DRS")
L.append(cls("decibel-therapeutics", rng="below_1b", city="Boston", city_src="web_verified",
             focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=S1_DB, entry_date="2017", flags=["stage_disputes_band"],
             note="Inner-ear gene therapies, Boston (the S-1's principal executive offices, 1325 Boylston Street). The "
                  "draft S-1's related-person table lists GV 2016, L.P. buying 5,000,000 shares of Series A preferred "
                  "($5.0M) in the Series A closings of January and May 2017, beside Third Rock and S.R. One. The Form D "
                  "band had read the 2020 Series D filing as a Growth entry; disputed with the filing. Regeneron "
                  "acquired the company in 2023 (status pre-filled).",
             rounds=[rnd("2017", "Series A (January and May 2017 closings)", 35500000, None, True, S1_DB,
                         "filing")]))

# ---------------------------------------------------------------- deepset
TC_DS22 = NEWS("deepset", "Deepset raises $14M")
TC_DS23 = NEWS("deepset", "secures $30M")
L.append(cls("deepset", status="private", rng="below_1b", country="DE", country_src="web_verified",
             country_cite=TC_DS22, city="Berlin", city_src="web_verified", focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_DS22, entry_date="2021-12",
             extra=momentum(TC_DS23),
             note="Haystack, the open-source LLM application framework, Berlin. GV led the $14M Series A, the "
                  "company's first funding round after years bootstrapped (TechCrunch, April 2022; the firm's own post "
                  "calls it GV's first investment in Germany); the round closed in 2021, and the firm's /ai list "
                  "dates GV's first investment December 2021, used as the entry date. Balderton led the $30M round "
                  "of August 2023 with GV following (TechCrunch). Momentum check 2026-09-28 (Google News on the name "
                  "with raises, 2025 and 2026): no later round and no priced mark at or above $1B; aligned with "
                  "Balderton's row.",
             rounds=[rnd("2022-04-28", "Series A", 14000000, "GV", True, TC_DS22, "press"),
                     rnd("2023-08-09", "unnamed round", 30000000, "Balderton Capital", True, TC_DS23, "press")]))

# ---------------------------------------------------------------- Delphia Therapeutics
PR_DT = ("https://www.delphiatx.com/news/delphia-therapeutics-launches-to-pioneer-a-new-field-of-cancer-medicines-"
         "activation-lethality/")
L.append(cls("delphia-therapeutics", status="private", rng="below_1b", country="US", city="Cambridge",
             city_src="web_verified", focus="Healthcare & Bio", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=PR_DT, entry_date="2024-05-02",
             note="Activation-lethality cancer medicines, Cambridge MA (One Kendall Square). The company launched in "
                  "May 2024 with a $67M Series A led by GV, with Nextech, Polaris Innovation Fund and Alexandria "
                  "(the company's release). Endpoints already called it GV-backed in September 2023 (headline), so "
                  "the Series A was likely committed before the launch; the entry date is the release's.",
             rounds=[rnd("2024-05-02", "Series A", 67000000, "GV", True, PR_DT, "company")]))

# ---------------------------------------------------------------- Denali Therapeutics
IRA_DN = FTS("Denali", "DRS")
S1_DN = "https://www.sec.gov/Archives/edgar/data/1714899/000119312517340997/d445892ds1.htm"
SA_DN = "https://stockanalysis.com/stocks/dnli/market-cap/"
L.append(cls("denali-therapeutics", usd=3350000000, rng="1b_plus", val_src="web_verified", val_cite=SA_DN,
             asof=CHECK, city="South San Francisco", city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=IRA_DN, entry_date="2015",
             flags=["stage_disputes_band"], extra=WV,
             note="Neurodegeneration drugs, South San Francisco (the S-1's principal executive offices). The Series "
                  "A-1 investors' rights agreement of 8 May 2015 lists Google Ventures 2015, L.P. among the investors "
                  "after the additional closings of 22 May and 22 July 2015 (the S-1 exhibit), so GV entered at the "
                  "Series A; the Form D band had read the 2024 private placement, years after the 2017 IPO, as the "
                  "entry. Market cap $3.35B on 2026-09-28 (stockanalysis.com) replaces the SEC float.",
             rounds=[rnd("2015-05-08", "Series A-1 (closings to 22 July 2015)", None, None, True, IRA_DN,
                         "filing")]))

# ---------------------------------------------------------------- Desktop Metal
L.append(cls("desktop-metal", rng="below_1b", city="Burlington", city_src="web_verified",
             focus="Industrial & Robotics", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=W("Desktop Metal"), entry_date="2017-02",
             note="Metal 3D printing, Burlington MA (Wikipedia). GV led the $45M Series C announced in February 2017 "
                  "(Wikipedia), after a Series A from NEA, Kleiner Perkins and Lux and further 2016 money; the firm's "
                  "own post says 'I first invested in the company in late 2016'. Same stage as the Form D band, which "
                  "had dated the entry to the 2019 filing; re-sourced and re-dated. Nano Dimension bought it in 2025 "
                  "and it filed for Chapter 11 in July 2025 (Wikipedia): acquired (pre-filled), aligned with Lux.",
             rounds=[rnd("2017-02", "Series C", 45000000, "GV", True, W("Desktop Metal"), "press")]))

# ---------------------------------------------------------------- Desmos
TC_DM = "https://techcrunch.com/2012/09/26/desmos-grabs-funding-from-google-ventures-to-make-math-fun/"
L.append(cls("desmos", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
             city="San Francisco", city_src="model_knowledge", focus="Consumer & Marketplaces",
             stage="undetermined", entry_date="2012-09-26", flags=["model_disputes_source"],
             note="The free online graphing calculator (desmos.com), San Francisco. The pre-filled Greece and "
                  "'defunct' (dissolved 1993) come from a Wikidata join on the one-word name, disputed. Google "
                  "Ventures invested in September 2012, terms undisclosed, bringing total funding past $1M after "
                  "$800K from Kapor, Learn Capital and Kindler; the money was meant to open a Series A that Desmos then "
                  "held off raising (TechCrunch), so no round name holds: stage undetermined. Amplify acquired the "
                  "Desmos curriculum and teacher.desmos.com in May 2022 and the calculator was spun off as Desmos "
                  "Studio PBC (Wikipedia): acquired, with Desmos Studio the successor for the calculator.",
             rounds=[rnd("2011-05", "angel funding before launch", 800000, None, False, TC_DM, "press"),
                     rnd("2012-09-26", "unnamed round (terms undisclosed)", None, None, True, TC_DM, "press")]))

# ---------------------------------------------------------------- Determined AI
PO_DAI = POST("modular-qualcomm-inference")
L.append(cls("determined-ai", status="acquired", rng="below_1b", country="US", city="San Francisco",
             city_src="model_knowledge", focus="AI & Applied AI", stage="Series A", stage_src="first_party",
             stage_conf="high", stage_cite=PO_DAI, entry_date="2018-11",
             note="Deep-learning training platform, San Francisco. The firm's own post lists its early AI "
                  "infrastructure investments as 'Determined AI (Series A, 2018; acquired by HPE)' and says GV led the "
                  "Series A; the /ai list dates GV's first investment November 2018 (entry date, decisions D7) and a "
                  "re-investment April 2020. Hewlett Packard Enterprise acquired it in 2021 (the firm's exit line).",
             rounds=[rnd("2018-11", "Series A", None, "GV", True, PO_DAI, "firm")]))

# ---------------------------------------------------------------- Devoted Health
DV_CO = "https://www.devoted.com/resources/2026-growth/"
MC_DV = "https://medcitynews.com/2021/10/devoted-health-raises-1-1b-sending-valuation-soaring-past-12b/"
L.append(cls("devoted-health", usd=12600000000, rng="10b_plus", val_src="web_verified", val_cite=MC_DV,
             asof="2021-10-08", city="Waltham", city_src="web_verified", focus="Healthcare & Bio", stage="Growth",
             stage_src="web_verified", stage_conf="high", stage_cite=DV_CO, entry_date="2025-11",
             flags=["stale"], clear=["unicorn_name_match"], extra=WV,
             note="Medicare Advantage plan and medical group, Waltham MA. The company's own page names GV among the "
                  "new investors in its $48M Series F (November 2025) and $317M Series F-Prime (January 2026), both "
                  "led by The Space Between and Centricus: a Series F entry, Growth; the entry date is the Series F's "
                  "month (GV may have come in at the F-Prime). No valuation was published for either; the last "
                  "published mark is the $1.15B Series D of October 2021 at $12.6B (MedCity News), re-sourced from the "
                  "unicorn list, stale, and aligned with ICONIQ Growth's row. Press figures for the 2026 rounds "
                  "disagree and the reported talks at $25B are not a priced event.",
             rounds=[rnd("2021-10-08", "Series D", 1150000000, "Uprising and SoftBank Vision Fund 2", False, MC_DV,
                         "press"),
                     rnd("2025-11", "Series F", 48000000, "The Space Between and Centricus", True, DV_CO, "company"),
                     rnd("2026-01", "Series F-Prime", 317000000, "The Space Between and Centricus", True, DV_CO,
                         "company")]))

# ---------------------------------------------------------------- Dialpad
TC_FS = ("https://techcrunch.com/2011/05/04/google-voice-ceo-craig-walker-launches-firespotter-a-google-ventures-"
         "funded-incubator/")
PR_FS = "https://www.prnewswire.com/news-releases/firespotter-labs-raises-15m-series-b-led-by-andreessen-horowitz-163018906.html"
DP_F = "https://www.dialpad.com/press/dialpad-series-f/"
L.append(cls("dialpad", status="private", usd=2200000000, rng="1b_plus", val_src="web_verified", val_cite=DP_F,
             asof="2021-12-16", city="San Ramon", city_src="web_verified", focus="SaaS", stage="Series A",
             stage_src="model", stage_conf="medium", entry_date="2011-05-04",
             flags=["stale", "stage_disputes_band"], extra=WV,
             note="AI business communications, formerly Firespotter Labs and Switch; Dialpad, Inc. gives 2700 Camino "
                  "Ramon, San Ramon as its address (its terms). GV's entry was Firespotter's 'initial $3 million round "
                  "of funding from Google Ventures' (TechCrunch, May 2011); a16z then led the $15M Series B of July "
                  "2012 with Google Ventures an existing and its earliest investor (the company's release), so the "
                  "2011 round is the Series A by position (model, medium). The Form D band had read the 2020 filing as "
                  "a Growth entry; disputed. Last priced mark: the $170M Series F led by ICONIQ at $2.2B, GV "
                  "participating (the company's release, 2021-12-16), stale; aligned with the a16z, Felicis and ICONIQ "
                  "rows.",
             rounds=[rnd("2011-05-04", "initial round (Series A by position)", 3000000, "Google Ventures", True,
                         TC_FS, "press"),
                     rnd("2012-07-19", "Series B", 15000000, "Andreessen Horowitz", True, PR_FS, "company"),
                     rnd("2021-12-16", "Series F", 170000000, "ICONIQ Capital", True, DP_F, "company")]))

# ---------------------------------------------------------------- Digit
TC_DG14 = "https://techcrunch.com/2014/12/16/digit-2-5m-seed/"
TC_DG16 = "https://techcrunch.com/2016/06/02/digit-adds-a-22-5-million-series-b-to-its-savings-account/"
GN_DG = ("https://www.globenewswire.com/news-release/2021/12/22/2357064/0/en/oportun-completes-acquisition-of-digit-"
         "a-neobanking-company-and-platform.html")
L.append(cls("digit", status="acquired", rng="below_1b", country="US", country_src="web_verified",
             country_cite=TC_DG16, city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_DG14, entry_date="2014-12-16",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_DG16,
             flags=["model_disputes_source"],
             note="Automated savings app, San Francisco ('San Francisco-based', TechCrunch 2016). The pre-filled "
                  "Japan and 'defunct' come from a Wikidata join on the one-word name, disputed. Google Ventures was "
                  "in the $2.5M seed led by Baseline Ventures (TechCrunch, December 2014); an $11.3M Series A followed "
                  "about a year before the $22.5M Series B led by Ribbit Capital (TechCrunch, June 2016): graduated. "
                  "Oportun completed its acquisition on 22 December 2021 for about $211.1M (GlobeNewswire); aligned "
                  "with the General Catalyst and Ribbit rows.",
             rounds=[rnd("2014-12-16", "Seed", 2500000, "Baseline Ventures", True, TC_DG14, "press"),
                     rnd("2015", "Series A", 11300000, None, None, TC_DG16, "press"),
                     rnd("2016-06-02", "Series B", 22500000, "Ribbit Capital", None, TC_DG16, "press")]))

# ---------------------------------------------------------------- Digits
TC_DI20 = ("https://techcrunch.com/2020/04/23/digits-launches-a-free-expense-monitoring-dashboard-for-small-"
           "businesses-closes-on-22m-series-b/")
TC_DI22 = ("https://techcrunch.com/2022/03/24/digits-books-65m-on-a-565m-valuation-to-bring-a-more-dynamic-"
           "automated-approach-to-legacy-accounting-tools/")
L.append(cls("digits", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="model_knowledge", focus="Fintech & Payments", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=TC_DI20, entry_date="2020-04-23",
             note="Automated accounting for small businesses (Jeff Seibert). Benchmark led the $10.5M Series A of "
                  "2019 with no GV; GV's Jessica Verrilli led the $22M Series B (TechCrunch, April 2020). SoftBank's "
                  "Vision Fund led the $65M Series C at $565M with GV following (TechCrunch, March 2022). Remote-first; "
                  "city aligned with 20VC's row.",
             rounds=[rnd("2019-11-06", "Series A", 10500000, "Benchmark", False,
                         "https://techcrunch.com/2019/11/06/stealth-fintech-startup-digits-raises-10-5-million-series-a-"
                         "from-benchmark-and-others/", "press"),
                     rnd("2020-04-23", "Series B", 22000000, "GV", True, TC_DI20, "press"),
                     rnd("2022-03-24", "Series C", 65000000, "SoftBank Vision Fund", True, TC_DI22, "press")]))

# ---------------------------------------------------------------- Distance Technologies
DT_SEED = ("https://distance.tech/news/distance-technologies-closes-oversubscribed-eur10m-seed-round-led-by-gv-"
           "google-ventures")
DT_PRE = "https://distance.tech/news/launch_release"
L.append(cls("distance", status="private", rng="below_1b", country="FI", country_src="web_verified",
             country_cite=DT_SEED, city="Helsinki", city_src="web_verified", focus="Industrial & Robotics",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=DT_SEED, entry_date="2024-09-24",
             note="Glasses-free mixed-reality optics and heads-up displays for vehicles and defence, Helsinki. After a "
                  "$2.7M pre-seed led by FOV Ventures and Maki.vc (June 2024), GV led the EUR 10M seed (the company's "
                  "release, Helsinki, 24 September 2024). FORVIA HELLA made an undisclosed strategic investment in "
                  "September 2026 (the company's news page), no round named or amount given." + GRAD_OPEN,
             rounds=[rnd("2024-06-13", "Pre-Seed", 2700000, "FOV Ventures and Maki.vc", False, DT_PRE, "company"),
                     rnd("2024-09-24", "Seed", None, "GV", True, DT_SEED, "company")]))

# ---------------------------------------------------------------- Diverge Health
EP_DH = NEWS("diverge-health", "Medicaid startup Diverge Health")
L.append(cls("diverge-health", status="private", rng="below_1b", city="Chicago", city_src="model_knowledge",
             focus="Healthcare & Bio",
             note="Community health teams embedded in primary care for Medicaid patients (Illinois, Michigan, Ohio "
                  "and New York markets on its careers page). Endpoints' headline reports the GV-backed company "
                  "raising $52M (November 2024), matching the $52.4M sold on its 2024 Form D, where the chief executive "
                  "files from Chicago and the issuer address is a director's in Glencoe, Illinois. No valuation "
                  "disclosed.",
             rounds=[rnd("2024-11-12", "unnamed round", 52000000, None, True, EP_DH, "press")]))

# ---------------------------------------------------------------- Divide (Enterproid)
TC_DV = ("https://techcrunch.com/2011/10/06/enterprise-mobile-computing-platform-enterproid-raises-11m-from-google-"
         "ventures-comcast-and-qualcomm/")
L.append(cls("divide", status="acquired", rng="below_1b", country="US", city="New York", city_src="model_knowledge",
             focus="Security", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_DV,
             entry_date="2011-10-06",
             note="Enterprise mobile 'dual persona' platform, formerly Enterproid, New York. Google Ventures joined the "
                  "$11M Series A led by Comcast Ventures, with Qualcomm Ventures (TechCrunch, October 2011). Google "
                  "bought Divide in May 2014 (CNBC and Forbes headlines; the firm's exit line).",
             rounds=[rnd("2011-10-06", "Series A", 11000000, "Comcast Ventures", True, TC_DV, "press")]))

# ---------------------------------------------------------------- Doctor On Demand
TC_DOD13 = ("https://techcrunch.com/2013/12/10/with-3m-from-andreessen-and-others-doctor-on-demand-launches-to-bring-"
            "a-40-virtual-house-call-to-healthcare/")
TC_DOD14 = "https://techcrunch.com/2014/08/06/doctor-on-demand-raises-21m-series-a-and-adds-comcast-as-a-customer/"
L.append(cls("doctor-on-demand", status="acquired", rng="below_1b", country="US", city="San Francisco",
             city_src="formd_address", focus="Healthcare & Bio", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=TC_DOD13, entry_date="2013-12-10", grad="graduated",
             grad_src="web_verified", grad_conf="high", grad_cite=TC_DOD14,
             note="Video visits with physicians, San Francisco (its Form Ds, 275 Battery Street). Google Ventures was "
                  "in the $3M seed with Venrock, Andreessen Horowitz, Lerer and Shasta at launch (TechCrunch, December "
                  "2013); Venrock and Shasta led the $21M Series A of August 2014 (TechCrunch): graduated. Merged with "
                  "Grand Rounds in May 2021 and rebranded Included Health (PR Newswire and Healthcare Dive headlines): "
                  "acquired, aligned with the a16z row.",
             rounds=[rnd("2013-12-10", "Seed", 3000000, None, True, TC_DOD13, "press"),
                     rnd("2014-08-06", "Series A", 21000000, "Venrock and Shasta Ventures", None, TC_DOD14, "press")]))

# ---------------------------------------------------------------- DocuSign
CAP_DS = "https://www.sec.gov/Archives/edgar/data/1261333/000156459018000747/filename11.htm"
SA_DS = "https://stockanalysis.com/stocks/docu/market-cap/"
L.append(cls("docusign", usd=12520000000, rng="10b_plus", val_src="web_verified", val_cite=SA_DS, asof=CHECK,
             country="US", city="San Francisco", city_src="web_verified", focus="SaaS", stage="Growth",
             stage_src="web_verified", stage_conf="high", stage_cite=CAP_DS, entry_date="2012-08", extra=WV,
             note="E-signature and agreement software, San Francisco (Wikipedia). The capitalization table in the "
                  "draft S-1's credit-agreement exhibit (30 April 2015) shows Google Ventures holding 1,751,781 Series "
                  "D and 102,338 Series E preferred, plus small Series B and common positions; TechCrunch's headline "
                  "of August 2012 has Google Ventures joining the round that grew to $55.7M. Entry at the Series D: "
                  "Growth. Market cap $12.52B on 2026-09-28 (stockanalysis.com) replaces the SEC float; aligned with "
                  "the Accel, Bain Capital Ventures and Insight rows.",
             rounds=[rnd("2012-08", "Series D", 55700000, None, True, CAP_DS, "filing")]))

# ---------------------------------------------------------------- dope.security
L.append(cls("dope-security", status="private", rng="below_1b", city="Mountain View", city_src="formd_address",
             focus="Security",
             note="Endpoint secure web gateway, Mountain View (its 2023 Form D). The firm's own post of March 2023 "
                  "says GV led the $16M Series A, matching the pre-filled stage. No later round or valuation found.",
             rounds=[rnd("2023-03-22", "Series A", 16000000, "GV", True, POST("dope-security-modern-cybersecurity"),
                         "firm")]))

# ---------------------------------------------------------------- Doppler
PO_DP = POST("doppler-modern-developers")
TC_DP22 = "https://techcrunch.com/2022/04/27/doppler-lands-20m-to-help-companies-manage-their-app-secrets/"
YC_DP = "https://www.ycombinator.com/companies/doppler"
L.append(cls("doppler", status="private", rng="below_1b", country="US", country_src="web_verified",
             country_cite=YC_DP, city="Austin", city_src="web_verified", focus="Security", stage="Seed",
             stage_src="model", stage_conf="medium", entry_date="2021-03-04", grad="graduated",
             grad_src="web_verified", grad_conf="high", grad_cite=TC_DP22,
             flags=["model_disputes_source"], extra=momentum(TC_DP22),
             note="Universal secrets manager for developers (YC W19). The pre-filled Austria is a Wikidata join on the "
                  "one-word name, disputed: Y Combinator's directory lists it active in Austin, TX (read 2026-09-28; "
                  "remote-first), aligned with the YC row over Sequoia's San Francisco. GV led the $6.5M round of March "
                  "2021 (the firm's own post; Forbes headline); no source names it, but it falls between the $2.3M seed "
                  "of October 2020 (Sequoia's row) and the $20M Series A that CRV led in April 2022 with GV following "
                  "(TechCrunch): a second seed round (model, medium), graduated by the named Series A. Momentum check "
                  "2026-09-28 (Google News on the name with raises, 2025): no later round, no $1B mark.",
             rounds=[rnd("2021-03-04", "unnamed round (between the seed and the Series A)", 6500000, "GV", True,
                         PO_DP, "firm"),
                     rnd("2022-04-27", "Series A", 20000000, "CRV", True, TC_DP22, "press")]))

# ---------------------------------------------------------------- Driver AI
TF_DR = NEWS("driver", "snaps $8M seed")
FD_DR = "https://www.sec.gov/Archives/edgar/data/2021927/000202192724000002/primary_doc.xml"
L.append(cls("driver", status="private", rng="below_1b", country="US", city="Austin", city_src="formd_address",
             focus="DevTools & APIs", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TF_DR,
             entry_date="2024-04", extra=momentum(TF_DR),
             note="AI-generated technical documentation for codebases (driver.ai), Austin (Driver AI, Inc.'s Form D of "
                  "October 2024, $8.27M sold). GV led the $8M seed with Y Combinator and angels (Tech Funding News, "
                  "October 2024); the firm's /ai list dates GV's investment April 2024, used as the entry date "
                  "(decisions D7). Momentum check 2026-09-28 (Google News on 'Driver AI' raises): no later round, no "
                  "$1B mark." + GRAD_OPEN,
             rounds=[rnd("2024-04", "Seed", 8000000, "GV", True, TF_DR, "press")]))

# ---------------------------------------------------------------- DualEntry
DE_CO = "https://www.dualentry.com/funding-announcement"
L.append(cls("dualentry", status="private", rng="below_1b", city="New York", city_src="web_verified", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=DE_CO, entry_date="2025-10-02",
             extra=momentum(DE_CO),
             note="AI-native ERP, New York (7 World Trade Center, its site). Lightspeed and Khosla led the $90M Series "
                  "A of 2 October 2025 with GV, Contrary and Vesey (the company's announcement); the firm's /ai list "
                  "dates GV's first investment October 2025, so GV was not in the earlier seed. Momentum check "
                  "2026-09-28 (Google News on the name with raises and valuation): no later round; the only figure "
                  "seen is a vendor's $415M (Rule A, not a mark). Aligned with Lightspeed's row.",
             rounds=[rnd("2025-10-02", "Series A", 90000000, "Lightspeed Venture Partners and Khosla Ventures", True,
                         DE_CO, "company")]))

# ---------------------------------------------------------------- Duo Security
TC_DU12 = ("https://techcrunch.com/2012/02/28/google-ventures-and-others-put-5m-in-enterprise-mobile-security-"
           "company-duo/")
TC_DU14 = "https://techcrunch.com/2014/09/22/duo-security-12m-benchmark/"
L.append(cls("duo-security", status="acquired", rng="below_1b", country="US", city="Ann Arbor",
             city_src="web_verified", focus="Security", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=TC_DU14, entry_date="2012-02-28",
             note="Two-factor authentication, Ann Arbor MI (TechCrunch). Google Ventures led the $5M Series A of "
                  "February 2012 with True Ventures and Resonant (TechCrunch 2012; the 2014 piece names it 'a $5 "
                  "million Series A round led by Google Ventures'); Benchmark led the $12M Series B of 2014. Cisco "
                  "bought Duo for $2.35B in 2018 (the firm's exit line): acquired, aligned with the Benchmark and "
                  "Redpoint rows.",
             rounds=[rnd("2012-02-28", "Series A", 5000000, "Google Ventures", True, TC_DU12, "press"),
                     rnd("2014-09-22", "Series B", 12000000, "Benchmark", None, TC_DU14, "press")]))

# ---------------------------------------------------------------- Dyno Therapeutics
SB_DY = NEWS("dyno-therapeutics", "Closes $100 Million Series A")
L.append(cls("dyno-therapeutics", status="private", rng="below_1b", country="US", city="Watertown",
             city_src="web_verified", focus="Healthcare & Bio", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=SB_DY, entry_date="2021-05-06",
             note="AI-designed AAV capsids for gene therapy, Watertown MA (343 Arsenal Street, its site). GV joined "
                  "the $100M Series A led by Andreessen Horowitz in May 2021 (the release on SynBioBeta; the firm's "
                  "/ai list dates GV's investment April 2021); earlier operations ran on a seed from Polaris, CRV and "
                  "KdT. Aligned with the a16z and Lux rows.",
             rounds=[rnd("2021-05-06", "Series A", 100000000, "Andreessen Horowitz", True, SB_DY, "company")]))

# ---------------------------------------------------------------- EasyPost
YF_EP = NEWS("easypost", "UCC Foreclosure Auction")
FD_EP = "https://www.sec.gov/Archives/edgar/data/2058813/000205881325000001/primary_doc.xml"
TC_EP = ("https://techcrunch.com/2013/06/06/easypost-a-stripe-for-shipping-raises-850k-seed-round-sees-transactions-"
         "doubling-every-month/")
L.append(cls("easypost", status="private", usd=1520000000, rng="1b_plus", val_src="web_verified", val_cite=YF_EP,
             asof="2022", city="Lehi", city_src="formd_address", focus="DevTools & APIs", stage="undetermined",
             flags=["stale"], extra=WV,
             note="Multi-carrier shipping API (legal name Simpler Postage, Inc.). Its $850K seed of June 2013 (YC, SV "
                  "Angel and others) did not include Google Ventures (TechCrunch); GV listed it from 2014, and only "
                  "vendor profiles tie GV to a February 2014 seed (Rule A: not citable), so the stage is undetermined. "
                  "A July 2026 auction notice for 2,456,673 pledged common shares says the 2021 and 2022 rounds valued "
                  "it at about $1.52B post-money and that it remains privately held with over $100M of 2025 revenue; "
                  "no auction price is published, so the last primary stands, stale. City: Simpler Postage's March "
                  "2025 Form D files from Lehi, Utah (fresher than the San Francisco on the General Catalyst and YC "
                  "rows).",
             rounds=[rnd("2013-06-06", "Seed", 850000, None, False, TC_EP, "press")]))

# ---------------------------------------------------------------- Editas Medicine
IRA_ED = FTS("Editas", "DRS")
SA_ED = "https://stockanalysis.com/stocks/edit/market-cap/"
L.append(cls("editas-medicine", usd=385490000, rng="below_1b", val_src="web_verified", val_cite=SA_ED, asof=CHECK,
             city="Cambridge", city_src="web_verified", focus="Healthcare & Bio", stage="Growth",
             stage_src="web_verified", stage_conf="medium", stage_cite=IRA_ED, entry_date="2015-08-04", extra=WV,
             note="CRISPR genome-editing medicines, Cambridge MA (the S-1's principal executive offices, 300 Third "
                  "Street). The amended investors' rights agreement of 4 August 2015, signed with the Series B stock "
                  "purchase agreement, adds Google Ventures 2014, L.P. to the Series A-1 and A-2 holders (Flagship, "
                  "Polaris, Third Rock, Partners); the A-2 was a tranche of the 2013 Series A commitments, so GV entered "
                  "at the Series B (the S-1 exhibit). Market cap $385.49M on 2026-09-28 (stockanalysis.com) replaces "
                  "the SEC float; band unchanged.",
             rounds=[rnd("2015-08-04", "Series B", 120000000, None, True, IRA_ED, "filing")]))

# ---------------------------------------------------------------- Egnyte
GB_EG = NEWS("egnyte", "Google Ventures invests in cloud company")
L.append(cls("egnyte", status="acquired", rng="below_1b", city="Mountain View", city_src="web_verified",
             focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GB_EG,
             entry_date="2012-07-17",
             note="Cloud content collaboration and governance, Mountain View (Wikipedia). Google Ventures led the $16M "
                  "Series C of July 2012 with existing investors Kleiner Perkins and Polaris; Karim Faris joined the "
                  "board (Growth Business). In February 2025 GI Partners and TA Associates became majority shareholders "
                  "(Wikipedia; the firm's exit line 'GI Partners and TA Associates, 2025'): a private-equity buyout, "
                  "acquired.",
             rounds=[rnd("2012-07-17", "Series C", 16000000, "Google Ventures", True, GB_EG, "press"),
                     rnd("2013", "unnamed round with existing investors", 29500000, None, True, W("Egnyte"), "press")]))

# ---------------------------------------------------------------- Element Science
L.append(cls("element-science", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Wearable cardioverter-defibrillator patch (Jewel), San Francisco (its Form Ds, 2014 to 2016). The "
                  "$145.6M Series C of March 2020 (Business Wire and FinSMEs headlines) is the last priced round "
                  "found, valuation undisclosed; FDA approval in May 2025 (Fierce Biotech headline), operating. The "
                  "pre-filled stage (Form D band) is left as it stands: no source names the 2014 round."))

# ---------------------------------------------------------------- Emergent VR
RV_EV = NEWS("emergent-vr", "Mobius")
FD_EV = "https://www.sec.gov/Archives/edgar/data/1632809/000163280915000001/primary_doc.xml"
L.append(cls("emergent-vr", status="acquired", rng="below_1b", country="US", city="San Jose",
             city_src="formd_address", focus="Consumer & Marketplaces", stage="Seed", stage_src="model",
             stage_conf="medium", entry_date="2015",
             note="Mobius, a mobile app for capturing and sharing moments in virtual reality. Its only Form D "
                  "(Emergent VR, Inc., San Jose, first sale January 2015) is a $2M convertible-note offering; Road to "
                  "VR reported $2.2M raised from Accel, Google Ventures and Rothenberg Ventures in October 2015, the "
                  "company's first money and no round named: Seed by instrument and size (model, medium). The firm's "
                  "exit line reads 'Acquired by River Studios, 2018'." + GRAD_OPEN,
             rounds=[rnd("2015-01-21", "convertible notes", 2000000, None, None, FD_EV, "filing"),
                     rnd("2015-10-19", "first funding, no round named", 2200000, None, True, RV_EV, "press")]))

# ---------------------------------------------------------------- Encoded Therapeutics
PO_EN = POST("encoded-therapeutics-pediatric-epilepsy")
L.append(cls("encoded-therapeutics", status="private", rng="below_1b", country="US", city="South San Francisco",
             city_src="model_knowledge", focus="Healthcare & Bio", stage="Growth", stage_src="first_party",
             stage_conf="high", stage_cite=PO_EN, entry_date="2020-07-22",
             note="Precision gene therapy for Dravet syndrome (ETX101), South San Francisco. The firm's own post of "
                  "July 2020: David Schenkein and Brendan Bulik-Sullivan 'chose to lead Encoded's Series D funding', "
                  "and the firm lists it from 2020; Menlo had entered at the 2019 Series C. The company raised a "
                  "$275M Series F in September 2026 (Business Wire headline, no valuation found). Aligned with "
                  "Menlo's row.",
             rounds=[rnd("2020-07-22", "Series D", None, "GV", True, PO_EN, "firm")]))

# ---------------------------------------------------------------- EnglishCentral
TC_EC09 = "https://techcrunch.com/2009/12/21/englishcentral-raises-3-5-million-google-ventures/"
TC_EC10 = "https://techcrunch.com/2010/11/09/ntt-ip-englishcentral/"
L.append(cls("english-central", status="private", rng="below_1b", country="US", city="Lexington",
             city_src="formd_address", focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=TC_EC09, entry_date="2009-10", grad="graduated",
             grad_src="web_verified", grad_conf="high", grad_cite=TC_EC09,
             note="Video-based English learning, Lexington MA (its only Form D, 2009; 'based in Massachusetts', "
                  "TechCrunch 2010); the site is live (copyright 2026). Google Ventures led a seed round of "
                  "convertible debt in October 2009 ($1.38M), which converted into a $2.1M Series A in December 2009 "
                  "(TechCrunch: 'the current series A financing', backed by Google Ventures and Atlas Venture): the "
                  "named later round graduates the row, two months after the seed. NTT Investment Partners added $1M "
                  "in November 2010 (TechCrunch). The pre-filled Seed (Form D band) is re-sourced and re-dated to the "
                  "seed itself.",
             rounds=[rnd("2009-10", "Seed (convertible debt)", 1380000, "Google Ventures", True, TC_EC09, "press"),
                     rnd("2009-12", "Series A", 2100000, None, True, TC_EC09, "press"),
                     rnd("2010-11-09", "strategic investment", 1000000, "NTT Investment Partners", None, TC_EC10,
                         "press")]))

# ---------------------------------------------------------------- EpiBiologics
EP_A = ("https://www.epibiologics.com/news-publications/epibiologics-launches-with-50-million-series-a-financing-to-"
        "advance-next-generation-protein-degradation-platform")
EP_X = ("https://www.epibiologics.com/news-publications/epibiologics-appoints-ann-lee-karlon-as-chief-executive-"
        "officer-and-presidentextends-series-a-financing-to-over-70-million")
EP_B = ("https://www.epibiologics.com/news-publications/epibiologics-closes-107m-series-b-to-advance-pipeline-of-"
        "novel-bispecific-antibodies-to-selectively-degrade-extracellular-protein-targets-in-oncology-and-immunology")
L.append(cls("epibiologics", status="private", rng="below_1b", country="US", city="San Mateo",
             city_src="web_verified", focus="Healthcare & Bio", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=EP_A, entry_date="2023-03-22",
             note="Bispecific-antibody protein degraders, San Mateo (the company's releases). GV was in the $50M Series "
                  "A co-led by Mubadala Capital and Polaris Partners (the company's release, 22 March 2023: 'with "
                  "participation from Vivo Capital and GV'); the $23M extension of July 2023 came from Digitalis, "
                  "Taiho and Codon; GV and JJDC co-led the $107M Series B of January 2026 with GV an existing investor "
                  "(the company's release). The firm lists it only from 2026, after the Series B.",
             rounds=[rnd("2023-03-22", "Series A", 50000000, "Mubadala Capital and Polaris Partners", True, EP_A,
                         "company"),
                     rnd("2023-07-20", "Series A extension", 23000000, None, None, EP_X, "company"),
                     rnd("2026-01-08", "Series B", 107000000, "GV and JJDC", True, EP_B, "company")]))

# ---------------------------------------------------------------- DNAnexus
FB_DN = "https://www.fiercebiotech.com/biotech/dnanexus-secures-15-million-funding-led-by-google-ventures-and-tpg-biotech"
BL_DN = "https://blog.dnanexus.com/2011-10-12-expansion"
L.append(cls("dnanexus", status="private", rng="below_1b", city="Mountain View", city_src="web_verified",
             focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=FB_DN,
             entry_date="2011-10-12",
             note="Cloud platform for genomic and biomedical data, Mountain View (Wikipedia; the release). Google "
                  "Ventures and TPG Biotech led the company's $15M 'second-round funding' of 12 October 2011, with "
                  "First Round, SoftTech, K9 and Felicis following (the release on Fierce Biotech); the company's own "
                  "blog calls those four previous investors and Google Ventures and TPG new ones. Felicis, already in "
                  "before October 2011, labels its own entry Series A on its listing (after the $1.55M First Round, K9 "
                  "and SoftTech put in from 2009, Wikipedia), and the $15M of January 2014 was a Series C (Wikipedia), "
                  "so GV's entry is the Series B by position: Growth (model, medium). The "
                  "pre-filled entry date (the 2014 Form D) is replaced. Blackstone Growth led $200M in 2022 (Business "
                  "Wire headline), valuation undisclosed.",
             rounds=[rnd("2009", "first venture funding", 1550000, None, False, W("DNAnexus"),
                         "press"),
                     rnd("2011-10-12", "second round", 15000000, "Google Ventures and TPG Biotech", True, FB_DN,
                         "company"),
                     rnd("2014-01", "Series C", 15000000, None, True, W("DNAnexus"), "press")]))

# ---------------------------------------------------------------- EnduroSat
EN_A = "https://www.endurosat.com/news/endurosat-closes-series-a-investment/"
EN_104 = "https://www.endurosat.com/news/endurosat-secures-104-million-to-scale-espa-class-satellite-production/"
EN_205 = "https://www.endurosat.com/news/endurosat-raises-205m-to-scale-next-generation-space-fleets/"
TR_EN = NEWS("endurosat", "Officially Enters Unicorn League")
L.append(cls("endurosat", status="private", rng="below_1b", country="BG", country_src="web_verified",
             country_cite=EN_205, city="Sofia", city_src="web_verified", focus="Industrial & Robotics",
             stage="Growth", stage_src="model", stage_conf="medium", stage_cite=EN_104, entry_date="2025-10-30",
             extra=momentum(TR_EN),
             note="Satellite manufacturer, Sofia (the company's releases). After a $10M Series A led by CEECAT "
                  "Capital in May 2023 that does not name GV, Google Ventures joined the $104M round of 30 October "
                  "2025 with Riot Ventures, Lux and the EIC Fund (the company's release; the firm lists it from "
                  "2025): an unnamed round after the Series A, Growth (model, medium). GV is also in the $205M round "
                  "of September 2026 led by Riot Ventures and Atreides. Valuation check 2026-09-28: the company's "
                  "CMO told The Recursive the valuation has 'blown past $1B' but will not disclose the figure (BTA "
                  "and Intellinews report the same); with no figure the row reads below $1B under Rule A (the MatX "
                  "precedent), flagged for the web pass.",
             rounds=[rnd("2023-05-10", "Series A", 10000000, "CEECAT Capital", None, EN_A, "company"),
                     rnd("2025-10-30", "unnamed round", 104000000, None, True, EN_104, "company"),
                     rnd("2026-09-16", "unnamed round", 205000000, "Riot Ventures and Atreides Management", True,
                         EN_205, "company")]))

# ---------------------------------------------------------------- Emissary
BI_EM = NEWS("emissary", "powered by")
FD_EM = "https://www.sec.gov/Archives/edgar/data/1688549/000168854924000001/primary_doc.xml"
L.append(cls("emissary", status="defunct", rng="below_1b", country="US", city="New York",
             city_src="formd_address", focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=BI_EM, entry_date="2016", grad="graduated", grad_src="web_verified",
             grad_conf="high", grad_cite=BI_EM,
             note="Marketplace matching B2B salespeople with 'emissaries' who know their target accounts, founded by "
                  "ex-Googler David Hammer, New York (its Form Ds). At its November 2016 launch it announced a $10M "
                  "Series A led by Canaan Partners and G20 Ventures, 'after a $2 million seed round with "
                  "participation from GV' and The New York Times (Business Insider): Seed, graduated. The entry date "
                  "is the year of that report; the seed preceded the launch. Emissary, Inc. kept raising small rounds "
                  "through July 2024 (Form D, $4.5M sold), but emissary.io is now parked for sale (read 2026-09-28) "
                  "and no later news was found: defunct; emissary.ai is an unrelated recruiting company.",
             rounds=[rnd("2016", "Seed", 2000000, None, True, BI_EM, "press"),
                     rnd("2016-11", "Series A", 10000000, "Canaan Partners and G20 Ventures", None, BI_EM, "press"),
                     rnd("2024-07-02", "unnamed equity offering (Form D)", 4526466, None, None, FD_EM, "filing")]))

# ---------------------------------------------------------------- Daydream
PR_DD = NEWS("daydream", "Secures $50 Million In Seed")
KB_DD = NEWS("daydream", "New Retail Platform Daydream")
TC_DD25 = ("https://techcrunch.com/2025/06/25/julie-bornsteins-daydream-is-releasing-an-ai-powered-chatbot-for-"
           "fashion-related-shopping/")
L.append(cls("daydream", status="private", rng="below_1b", country="US", city="Kirkland", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=PR_DD, entry_date="2024-06-20", extra=momentum(TC_DD25),
             note="AI shopping and fashion discovery (daydream.ing), founded by Julie Bornstein; headquarters in "
                  "Kirkland, WA (425 Business; the seed release is datelined New York). GV joined the $50M seed "
                  "co-led by Forerunner and Index with True Ventures (the company's release, 20 June 2024; TechCrunch). "
                  "Momentum check 2026-09-28 (Google News on the name with Julie Bornstein and raises): no later round "
                  "and no $1B mark; TechCrunch's June 2025 launch piece still cites only the seed. The First Round "
                  "row (daydream Labs, an AI SEO agency in San Francisco) and the 8VC row (DayDream, dental AI) are "
                  "different companies." + GRAD_OPEN,
             rounds=[rnd("2024-06-20", "Seed", 50000000, "Forerunner Ventures and Index Ventures", True, PR_DD,
                         "company")]))

# ---------------------------------------------------------------- Datanyze
BI_DZ = "https://www.businessinsider.com/ilya-sermin-used-cold-emails-to-get-datayze-funded-by-mark-cuban-and-google-2015-1"
TC_DZ = "https://techcrunch.com/2014/12/22/datanyze-acquires-leadledger/"
L.append(cls("datanyze", rng="below_1b", city="San Mateo", city_src="web_verified",
             focus="SaaS", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BI_DZ,
             entry_date="2014",
             note="Technographics and sales-prospecting data (which software a website runs). A few months after an "
                  "April 2014 pitch, Mark Cuban 'joined IDG Ventures and Google Ventures in a $2 million seed-round "
                  "investment' (Business Insider, January 2015); TechCrunch dates the $2M seed to 2014. No later "
                  "round found. Zoom Information, Inc. (the legacy ZoomInfo, a Great Hill Partners company that "
                  "DiscoverOrg bought in 2019) acquired it in 2018; its adviser Cascadia Capital gives it as "
                  "'headquartered in San Mateo, California' (the firm's exit line: 'Acquired by ZoomInfo, 2018')."
                  + GRAD_OPEN,
             rounds=[rnd("2014", "Seed", 2000000, None, True, BI_DZ, "press")]))

# ---------------------------------------------------------------- Delighted
TC_DL = "https://techcrunch.com/2014/10/07/delighted-launch-2/"
PR_DLQ = ("https://www.prnewswire.com/news-releases/qualtrics-acquires-delighted-extending-its-market-leadership-in-"
          "customer-experience-300628650.html")
L.append(cls("delighted", status="acquired", rng="below_1b", country="US", flags=["city_unknown"], focus="SaaS",
             stage="Seed", stage_src="model", stage_conf="medium", entry_date="2014-10-07",
             note="Net Promoter customer-feedback surveys, founded in 2013 by Caleb Elston with engineers from Yobongo "
                  "and Mosaic. Its first announced funding, amount undisclosed, came from Google Ventures, Shasta "
                  "Ventures, SV Angel, Designer Fund, Fuel Capital, Relay Ventures and angels a year after launch "
                  "(TechCrunch, October 2014); no round is named, and the syndicate reads as a seed (model, medium). "
                  "Qualtrics acquired it on 12 April 2018 (the release; the firm's exit line). City not placed: the "
                  "release's dateline (Salt Lake City and Seattle) is Qualtrics', and neither TechCrunch's launch "
                  "pieces nor EDGAR give an address; an M&A database's Palo Alto could not be read." + GRAD_OPEN,
             rounds=[rnd("2014-10-07", "first outside funding, no round named", None, None, True, TC_DL, "press")]))

# ---------------------------------------------------------------- Delve Bio
IPM_DB = NEWS("delve-bio", "Launches with $35M Series A")
BS_DB = NEWS("delve-bio", "Delve Bio and UCSF Publish Research")
L.append(cls("delve-bio", status="private", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=IPM_DB, entry_date="2023-06-21",
             note="Metagenomic sequencing diagnostics for infectious disease (Delve Detect), the exclusive licensee of "
                  "UCSF's mNGS test. GV co-invested with Section 32 in the $35M Series A led by Perceptive Xontogeny "
                  "Venture Fund II at the June 2023 launch (Inside Precision Medicine); the company's releases are "
                  "datelined Boston and name PXV Fund II, Section 32 and GV as its backers (BioSpace, November 2024). "
                  "No later round found.",
             rounds=[rnd("2023-06-21", "Series A", 35000000, "Perceptive Xontogeny Venture Fund II", True, IPM_DB,
                         "press")]))

jl.write("j4", L)
