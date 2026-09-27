"""PRO-163 grind, batch-001 (1x .. lenus). Evidence: scratch/evidence-pack.json (the eqtgroup.com
Key Facts, the eqtventures.com archive, the firm's own posts 2016-2026), scratch/siblings-full.json,
Wikipedia raw text (data/filings/eqt-ventures/wikipedia/) and the web checks named per line (URLs copied
from the search results of 2026-09-27). Seed graduations that need the absence test are judged in their
own pass after graduation-surfaces.py; yeses and censored rows are decided here."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, S, A, W, SITE = jl.cls, jl.verdict, jl.rnd, jl.S, jl.A, jl.W, jl.SITE
L = []

def site_c(slug, code, **kw):
    """Country from the firm's own Key Facts (the eqtgroup.com page states Country per company)."""
    return dict(country=code, country_src="web_verified", country_cite=SITE(slug), **kw)

# ---------------------------------------------------------------- membership
L.append(verdict("banking-circle", "not_member",
    "EQT Ventures I entered Banking Circle through EQT VIII's acquisition of Saxo Payments Banking Circle in July 2018: "
    "'This was a different kind of deal for the EQT Ventures fund as it joined forces with EQT VIII, which will have majority "
    "ownership' (the firm's post, 2018-07-13). The transaction is a control acquisition by the co-investor group, not a "
    "venture round (COLLECTION.md s1, T3 control positions; decisions.md D5); the site lists both funds on the company.",
    ec="site_listing", conf="high", cite=S("on-eqt-s-acquisition-of-banking-circle")) | {"exclusion": "control_position"})

# ---------------------------------------------------------------- classification
L.append(cls("1x", status="private", rng="below_1b", val_src="web_verified",
    extra={"valuation_range_source": "web_verified",
           "valuation_citation": "https://www.theinformation.com/articles/humanoid-robot-developer-1x-targets-1-billion-new-funding",
           "valuation_asof": "2026-09-27"},
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2024/01/11/openai-backed-1x-raises-another-100m-for-the-race-to-humanoid-robots/",
    entry_date="2024-01", country="US", country_src="web_verified", country_cite=W("1X_Technologies"),
    city="Palo Alto", city_src="web_verified", focus="Industrial & Robotics", flags=["model_disputes_source"],
    note="Humanoid robots (formerly Halodi Robotics, Moss, Norway; now headquartered in Palo Alto per its Wikipedia infobox, the Wikidata NO is its founding country). "
         "EQT Ventures led the $100M Series B of Jan 2024, the fund's entry (site: EQT Ventures III, 2024). Momentum check 2026-09-27: the Series C of up to $1B at a $10B+ target "
         "reported in Sep 2025 is not confirmed closed; no priced round with a citable $1B+ figure, so below_1b (Rule A: vendor estimates of the Series B post-money are not marks).",
    rounds=[rnd("2023-03", "Series A2", 23500000, "OpenAI Startup Fund", False, W("1X_Technologies"), "press"),
            rnd("2024-01", "Series B", 100000000, "EQT Ventures", True,
                "https://techcrunch.com/2024/01/11/openai-backed-1x-raises-another-100m-for-the-race-to-humanoid-robots/", "press")]))

L.append(cls("acerta-analytics", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://betakit.com/kitchener-autotech-startup-acerta-omers-series-a/", entry_date="2018",
    grad="graduated", grad_src="web_verified", grad_cite="https://betakit.com/kitchener-autotech-startup-acerta-omers-series-a/",
    **site_c("acerta-analytics", "CA"), city="Kitchener", focus="AI & Applied AI",
    note="Machine-learning quality analytics for automotive manufacturing (Kitchener, Ontario). EQT Ventures' 2018 entry (site: EQT Ventures I, 2018) was the $2M convertible note "
         "from the Female Founders Competition 'launched by M12 in partnership with EQT Ventures and SVB Financial Group' (BetaKit, 2020-09-01): a note before any priced round, "
         "Seed by instrument. The notes converted into the named $7M Series A led by OMERS Ventures (Sep 2020), which graduates the row; $8M Series B (BDC, Nov 2022).",
    rounds=[rnd("2018", "convertible note (Female Founders Competition)", 2000000, "M12", True, "https://betakit.com/kitchener-autotech-startup-acerta-omers-series-a/", "press"),
            rnd("2020-09", "Series A", 7000000, "OMERS Ventures", None, "https://betakit.com/kitchener-autotech-startup-acerta-omers-series-a/", "press")]))

L.append(cls("airkit", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=W("Stephen Ehikian"), entry_date="2021-05", country="US", country_src="web_verified", country_cite=SITE("airkit"),
    city="Redwood City", focus="SaaS",
    note="Low-code customer-experience platform. EQT Ventures led the $40M Series B of May 2021 (Wikipedia; site: EQT Ventures II, entry 2021, exit 2023). "
         "acq. by Salesforce, 2023 (the firm's Exit 2023; Accel's row agrees)."))

L.append(cls("anydesk", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=W("AnyDesk"), entry_date="2018-05", **site_c("anydesk", "DE"), city="Stuttgart", focus="SaaS",
    note="Remote desktop software. 'In May 2018, AnyDesk secured 6.5 million euros of funding in a Series A round led by EQT Ventures' (Wikipedia; the firm's post 2018-05-15). "
         "Insight led the Jan 2020 round, General Atlantic 2021; no disclosed $1B mark."))

L.append(cls("anyfin", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-anyfin"), entry_date="2020-05", city="Stockholm", focus="Fintech & Payments",
    note="Consumer refinancing app. 'The $30 million Series B round was led by EQT Ventures' (the firm's post, 2020-05-14); $30M Series C 2023."))

L.append(cls("argil", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.vestbee.com/insights/articles/argil-secures-4-9-m", entry_date="2024-11",
    grad="censored", **site_c("argil", "FR"), city="Paris", focus="AI & Applied AI",
    note="AI video avatars (YC). EQT Ventures led the seed of a EUR 4.9M pre-seed and seed raise (Vestbee; the firm's archive date 2024-11-27); inside the 24-month window."))

L.append(cls("baffin-bay-networks", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-baffin-bay-networks"), entry_date="2018-06", **site_c("baffin-bay-networks", "SE"),
    city="Stockholm", focus="Security",
    note="Cloud security. '$6.4m Series A, led by EQT Ventures' (the firm's post, 2018-07-16; 'EQT Ventures' first investment in the cyber security space'). acq. by Mastercard, 2022 (the firm's post 2022-03-20)."))

L.append(cls("baller-league", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("baller-league-why-we-believe"), entry_date="2024-12", **site_c("baller-league", "DE"), city="Berlin",
    focus="Media, Gaming & Advertising",
    note="Six-a-side football league and media company. 'We're Proud to Lead the $25M Series A' (the firm's post, 2024-12-10)."))

L.append(cls("beamery", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
    val_cite="https://beamery.com/resources/news/beamery-raises-50-million-in-series-d-funding", asof="2022-12-13",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=S("revolutionising-talent-acquisition"), entry_date="2018-06", **site_c("beamery", "GB"), city="London", focus="SaaS",
    flags=["stale"],
    note="Talent CRM. EQT Ventures led the $28M Series B (Jun 2018; the firm's post names the round and the lead; Wikipedia); $138M Series C 2021 (OTPP); "
         "$50M Series D at a $1B valuation (Dec 2022, the company's release) is the last priced mark, older than 24 months; 2023 layoffs are not collapse evidence with a figure.",
    rounds=[rnd("2017-04", "Series A", 5000000, "Index Ventures", False, W("Beamery"), "press"),
            rnd("2018-06", "Series B", 28000000, "EQT Ventures", True, S("revolutionising-talent-acquisition"), "firm"),
            rnd("2021-06", "Series C", 138000000, "Ontario Teachers' Pension Plan", True, W("Beamery"), "press"),
            rnd("2022-12", "Series D", 50000000, "Ontario Teachers' Pension Plan", None,
                "https://beamery.com/resources/news/beamery-raises-50-million-in-series-d-funding", "company")]))

L.append(cls("beat81", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2019/09/26/berlin-based-beat81-scores-e6-4-million-to-strengthen-fitness-communities/",
    entry_date="2019-09", city="Berlin", focus="Consumer & Marketplaces",
    note="Group fitness classes with heart-rate tracking. EQT Ventures led the EUR 6.4M Series A (Sep 2019, Tech.eu; site: EQT Ventures II, entry 2019); "
         "the firm's Exit 2022 is its own sale of the stake; the company still operates."))

L.append(cls("biolevate", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("announcing-our-investment-in-biolevate"), entry_date="2024-11", grad="censored",
    **site_c("biolevate", "FR"), city="Paris", focus="Healthcare & Bio",
    note="AI for medical writing and regulatory documents. 'we're proud to be leading their EUR 6 million seed funding round' (the firm's post, 2024-11-26); inside the window."))

L.append(cls("buena", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2017-08",
    grad="graduated", grad_src="web_verified",
    grad_cite="https://www.eu-startups.com/2025/07/berlin-based-buena-raises-e49-million-to-digitise-property-management/",
    **site_c("buena", "DE"), city="Berlin", focus="SaaS", flags=["stage_uncited"],
    note="Property management (Berlin), called Home until its rebrand as Buena: the firm's 2017 cards list 'Home' with Signing/Closing Date Aug. 23 2017, the "
         "same date the eqtventures.com archive carries for Buena. 'EQT Ventures is happy to join Home's EUR 3 million round as a lead investor, along with ... Redalpine' "
         "(the firm's post, 2017-08-22). No source names that round; it precedes the company's first named Series A (EUR 49M led by GV, Jul 2025), so the stage is Seed by "
         "position at low confidence and the named Series A graduates the row.",
    rounds=[rnd("2017-08", "round (unnamed)", 3500000, "EQT Ventures", True, A("home-raises-3-million"), "firm"),
            rnd("2025-07", "Series A", 57000000, "GV", None,
                "https://www.eu-startups.com/2025/07/berlin-based-buena-raises-e49-million-to-digitise-property-management/", "press")]))

L.append(cls("calldesk", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=A("calldesk-raises"), entry_date="2017-09", **site_c("calldesk", "FR"), city="Paris", focus="AI & Applied AI",
    note="AI voice agents for call centres. 'has now raised a EUR 2.1 million seed round. The investors in the round were Point Nine Capital and the EQT Ventures fund' "
         "(the firm's post, 2017-09-28). acq. by Future Look ITC, 2022 (Point Nine's row; the firm's Exit 2022). Graduation judged in the surfaces pass."))

L.append(cls("candela", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("eqt-ventures-leads-24m-series-a-in-candela"), entry_date="2021-12", **site_c("candela", "SE"), city="Stockholm",
    focus="Climate & Energy",
    note="Electric hydrofoil boats. 'EQT Ventures is now joining this mission by leading a EUR 24m Series A' (the firm's post, 2021-12-08); EUR 30M raise 2026 (the firm's post)."))

L.append(cls("cleo", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-cleo"), entry_date="2020-12", **site_c("cleo", "GB"), city="London",
    focus="Fintech & Payments", flags=["model_disputes_source"],
    note="AI money assistant. 'raised $44 million Series B funding led by EQT Ventures' (the firm's post, 2020-12-10); $80M Series C at ~$500M (Jun 2022). "
         "London-founded with its users mostly in the US; the Wikidata CA is a wrong join (Balderton's row found the same). Balderton's momentum check of 2026-09-26 found no $1B+ mark."))

L.append(cls("codacy", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=A("leads-codacys-series-a"), entry_date="2017-08", **site_c("codacy", "PT"), city="Lisbon", focus="DevTools & APIs",
    note="Automated code review. 'Lead investor in the A round was EQT Ventures' ($5.1M; the firm's post, 2017-08-17; Tom Mendoza to the board)."))

L.append(cls("codesandbox", status="acquired", rng="below_1b", country="NL", country_src="web_verified", country_cite="https://siliconangle.com/2024/12/12/together-ai-acquires-codesandbox-adds-code-interpreter-ai-development-platform/",
    city="Amsterdam", focus="DevTools & APIs", flags=["model_disputes_source"],
    note="Browser-based development environments (Amsterdam; CodeSandbox, Inc. files Form D from San Francisco, the US entity). EQT Ventures led the $12.7M round of Oct 2020 "
         "(the firm's post, 2020-10-29; the Form D band reads Series A). acq. by Together AI, 2024-12-12 (Together AI's announcement; SiliconANGLE)."))

L.append(cls("cytora", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2019/04/16/cytora/", entry_date="2019-04", **site_c("cytora", "GB"), city="London",
    focus="SaaS",
    note="AI risk-digitisation for commercial insurers. EQT Ventures led the GBP 25M Series B (Apr 2019, TechCrunch); after the GBP 4.4M Series A of Dec 2017. "
         "acq. by Applied Systems, 2025 (Insurance Journal 2025-09-09; the firm's Exit 2025)."))

L.append(cls("depict-ai", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://arcticstartup.com/depictai-has-raised-17m-series-a/", entry_date="2021",
    grad="graduated", grad_src="web_verified", grad_cite="https://www.businesswire.com/news/home/20220224005148/en",
    **site_c("depict-ai", "SE"), city="Stockholm", focus="AI & Applied AI",
    note="Product recommendations for e-commerce (YC). EQT Ventures joined the $2.8M seed led by Initialized Capital (2021); the named $17M Series A led by Tiger Global "
         "followed in Feb 2022 with EQT participating (Business Wire), which graduates the row.",
    rounds=[rnd("2021", "Seed", 2800000, "Initialized Capital", True, "https://arcticstartup.com/depictai-has-raised-17m-series-a/", "press"),
            rnd("2022-02-24", "Series A", 17000000, "Tiger Global", True, "https://www.businesswire.com/news/home/20220224005148/en", "press")]))

L.append(cls("dottxt", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2024/10/18/dottxt-raises-11-m-to-enhance-llm-interaction-capabilities/", entry_date="2024-08",
    country="FR", country_src="web_verified", country_cite="https://siliconcanals.com/dottxt-raises-e10-9m-to-improve-llms/",
    city="Paris", focus="AI & Applied AI", flags=["stage_disputes_band", "model_disputes_source"],
    note="Structured outputs for LLMs (the Outlines library). $11.9M across a $3.2M pre-seed led by Elaia (Dec 2023) and an $8.7M seed led by EQT Ventures (Aug 2024), "
         "Tech.eu and the firm's post 2024-10-18; the Form D band's Series A reads the combined size. Paris-based (Silicon Canals; the firm's Key Facts: France); "
         "the Form D's Jersey City address is the US entity. Graduation judged in the surfaces pass (entry just past 24 months).",
    rounds=[rnd("2023-12", "Pre-Seed", 3200000, "Elaia", False, "https://tech.eu/2024/10/18/dottxt-raises-11-m-to-enhance-llm-interaction-capabilities/", "press"),
            rnd("2024-08", "Seed", 8700000, "EQT Ventures", True, "https://tech.eu/2024/10/18/dottxt-raises-11-m-to-enhance-llm-interaction-capabilities/", "press")]))

L.append(cls("einride", status="public", rng="below_1b", usd=607290000, val_src="web_verified",
    val_cite="https://stockanalysis.com/stocks/enrd/market-cap/", asof="2026-09-25",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=S("on-einride-s-200m-series-c"), entry_date="2019-10",
    city="Stockholm", focus="Industrial & Robotics",
    note="Autonomous electric freight. EQT Ventures co-led the $25M Series A with NordicNinja in 2019 ('only 3 years after we co-led their Series A together with Nordic Ninja "
         "in 2019', the firm's post 2022-12-07), co-led the $110M Series B (2021) and the $200M Series C (2022). Listed on Nasdaq (ENRD) 2026-06-10 after the merger with "
         "Legato Merger Corp. III closed 2026-06-09 at $1.35B pre-money; market cap $607.29M on 2026-09-25 (StockAnalysis)."))

L.append(cls("endgame", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2022-02",
    country="US", country_src="web_verified", country_cite=SITE("endgame"), city="Los Angeles", focus="SaaS",
    note="Product-led sales platform (endgame.io, Los Angeles). The fund's entry (site: EQT Ventures III, 2022; the archive's announcement date 2022-02-08) coincides with "
         "the $30M Series B of Feb 2022; the round's participants were not read on a page, so model at medium. Still operating 2026 (site and blog live); "
         "Menlo's 'acquired' reading is raised at alignment (it may carry the Endgame Inc sold to Elastic in 2019)."))

L.append(cls("evroc", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-evroc"), entry_date="2023-06", **site_c("evroc", "SE"), city="Stockholm",
    focus="Data Infrastructure",
    note="European sovereign hyperscale cloud. 'Today we are happy to welcome evroc to the EQT Ventures family through what is probably our largest seed investment to date' "
         "(the firm's post, 2023-06-06). Graduation judged in the surfaces pass."))

L.append(cls("flow-engineering", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("celebrating-flow-engineerings-85m-seed"), entry_date="2022-12", **site_c("flow-engineering", "GB"), city="London",
    focus="SaaS",
    note="Collaboration platform for hardware engineering. '$8.5m in Seed funding from Backed VC ... alongside EQT Ventures' (the firm's post, 2022-12-06). "
         "Graduation judged in the surfaces pass."))

L.append(cls("fly-io", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2023/06/fly-io-raises-70m-in-series-c-funding.html", entry_date="2023-06",
    city="Chicago", focus="Data Infrastructure",
    note="Developer public cloud. EQT Ventures led the $70M Series C of Jun 2023 at a reported $467M valuation (FinSMEs; Bloomberg)."))

L.append(cls("formo", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://agfundernews.com/formo-nets-50m-for-animal-free-cheese-fermented-from-microbes", entry_date="2021-09",
    **site_c("formo", "DE"), city="Berlin", focus="Healthcare & Bio",
    note="Animal-free cheese by fermentation. $50M Series A led by EQT Ventures with Elevat3 and Lowercarbon as co-leads (Sep 2021, AgFunderNews); $61M Series B 2024."))

L.append(cls("frontify", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-frontify"), entry_date="2020-01", **site_c("frontify", "CH"), city="St. Gallen",
    focus="SaaS",
    note="Brand management platform. 'their $22.3m Series B-round today, led by EQT Ventures' (the firm's post, 2020-01-28)."))

L.append(cls("generative-engineering", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techfundingnews.com/london-based-generative-engineering-nets-e4m-to-make-physical-engineering-more-efficient/",
    entry_date="2023-11", **site_c("generative-engineering", "GB"), city="London", focus="SaaS",
    note="Engineering design-exploration software. 'has netted EUR 4m in pre-seed funding. The round was led by EQT Ventures' (Tech Funding News, 2023-11-22); "
         "FinSMEs calls it a seed, the round's own coverage a pre-seed."))

L.append(cls("griffin", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2020-11",
    grad="graduated", grad_src="web_verified",
    grad_cite="https://griffin.com/blog/griffin-raises-13-5-million-in-series-a-funding-round-led-by-massmutual-ventures",
    **site_c("griffin", "GB"), city="London", focus="Fintech & Payments", flags=["stage_uncited", "model_disputes_source"],
    note="Banking-as-a-service bank (UK licence 2024). EQT Ventures led a GBP 6.5M round in Nov 2020 (Griffin's blog: 'Griffin secures GBP 6.5m round led by EQT Ventures'), "
         "after a GBP 3M seed; no source names that round, and the company's first named Series A is the $13.5M round led by MassMutual Ventures, so Seed by position at low "
         "confidence and the named Series A graduates the row. The Wikidata IT is a wrong join.",
    rounds=[rnd("2020", "Seed", 3900000, None, False, "https://www.privateequitywire.co.uk/2020/11/16/292209/griffin-secures-gbp65m-funding-round-led-eqt-ventures", "press"),
            rnd("2020-11", "round (unnamed)", 8400000, "EQT Ventures", True,
                "https://griffin.com/blog/griffin-secures-6-5m-round-led-by-eqt-ventures-to-build-banking-as-a-service-platform-and-seek-full-bank-license", "company"),
            rnd(None, "Series A", 13500000, "MassMutual Ventures", None,
                "https://griffin.com/blog/griffin-raises-13-5-million-in-series-a-funding-round-led-by-massmutual-ventures", "company")]))

L.append(cls("hackerone", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=W("HackerOne"), entry_date="2017-04", country="US", country_src="web_verified", country_cite=W("HackerOne"),
    city="San Francisco", focus="Security",
    note="Bug bounty and vulnerability disclosure. 'In April 2017, European-based venture capital fund EQT Ventures invested in the $40 million Series C funding round' "
         "(Wikipedia; the firm's post 2017-04-10); $36M Series D 2019 (Valor); no disclosed $1B mark."))

L.append(cls("handshake", status="private", rng="1b_plus", usd=3500000000, val_src="web_verified",
    val_cite="https://www.prnewswire.com/news-releases/no-network-required-handshake-raises-200m-to-help-gen-z-launch-careers-301463445.html",
    asof="2022-01", city="San Francisco", focus="Consumer & Marketplaces", flags=["stale"],
    note="Early-career network (joinhandshake.com; Form D issuer Stryder Corp.). 'Handshake Raises $40 Million in Series C Funding Led By EQT Ventures' (PR Newswire, 2018-10-31), "
         "the fund's entry; the Form D band agrees (Growth). $3.5B at the $200M Series F of Jan 2022, the last priced round, older than 24 months; the same mark and citation as "
         "the Coatue, Lightspeed and Spark rows."))

L.append(cls("headspin", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2018/10/30/gv-backed-mobile-app-performance-platform-headspin-raises-20m-at-500m-valuation/",
    entry_date="2018-10", country="US", country_src="web_verified", country_cite=SITE("headspin"), city="Palo Alto",
    focus="DevTools & APIs",
    note="Mobile app performance testing. EQT Ventures joined the $20M Series B at $500M (Oct 2018, TechCrunch). The 2020 $1.16B mark did not survive the founder's fraud "
         "conviction and the recapitalisation (the Battery and Felicis rows); the firm's Exit 2020."))

L.append(cls("heart-aerospace", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=W("Heart_Aerospace"), entry_date="2019", grad="graduated", grad_src="web_verified", grad_cite=W("Heart_Aerospace"),
    city="Los Angeles", focus="Industrial & Robotics",
    note="Electric and hybrid-electric regional aircraft (founded Gothenburg 2018, headquartered in Los Angeles since 2024). 'raised US$2.1 million in seed funding led by EQT "
         "Ventures, the Norrsken Foundation, and ... Lowercarbon Capital' (spring 2019, Wikipedia); the named $35M Series A (Jul 2021, Breakthrough Energy Ventures) graduates it; "
         "$107M Series B Feb 2024."))

L.append(cls("holidu", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.unquote.com/dach/official-record/67183/eqt-ventures-makes-first-investment-with-eur5m-holidu-series-a",
    entry_date="2015-10", **site_c("holidu", "DE"), city="Munich", focus="Consumer & Marketplaces",
    note="Vacation rental search and management. 'EQT Ventures makes first investment with EUR 5m Holidu series-A' (Unquote; the firm's archive date 2015-10-26; site Entry 2015, "
         "before the fund's May 2016 close); Series C-E since, no disclosed $1B mark."))

L.append(cls("hubs", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=A("leads-3d-hubs-series-b"), entry_date="2016-07", country="NL", country_src="web_verified", country_cite=SITE("hubs"),
    city="Amsterdam", focus="Industrial & Robotics", flags=["model_disputes_source"],
    note="On-demand manufacturing network (3D Hubs, renamed Hubs 2020). 'EQT Ventures leads 3D Hubs' series B financing' (the firm's post, 2016-08-02); Balderton led the "
         "Series A (2014). acq. by Protolabs, 2021 (Protolabs 8-K). Amsterdam-founded; the Form D's New York address is its US entity."))

L.append(cls("hume-ai", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2024/03/hume-ai-raises-50m-in-series-b-funding.html", entry_date="2024-03",
    country="US", country_src="web_verified", country_cite=SITE("hume-ai"), city="New York", focus="AI & Applied AI",
    note="Empathic voice AI. $50M Series B led by EQT Ventures (Mar 2024; USV's row: at $219M). In Jan 2026 Google DeepMind hired the founder and engineers under a licence; "
         "the company still operates (acqui-hire rule: the company decides the status; USV's row agrees)."))

L.append(cls("insempra", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://medium.com/eqtventures/on-eqt-ventures-investment-in-origin-bio-5a749e7c6645", entry_date="2021-05",
    **site_c("insempra", "DE"), city="Munich", focus="Healthcare & Bio",
    note="Synthetic biology for chemicals and materials (Origin.Bio until 2022). EQT Ventures led the $15M series seed of May 2021 (the firm's Medium post; Nordic9). "
         "Graduation judged in the surfaces pass."))

L.append(cls("instabee", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2021/02/10/instabox-series-b/", entry_date="2021-02", **site_c("instabee", "SE"), city="Stockholm",
    focus=None, flags=["needs_web_value"],
    note="Last-mile parcel delivery (Instabox; merged with Budbee as Instabee in 2022). EQT Ventures led Instabox's $90M Series B (Feb 2021, Tech.eu). The 2022 combination "
         "was announced at EUR 1.6B (the firm's post 2022-12-20); a SEK 216M round from EQT vehicles in Jun 2024 carried no public price: the band is pinned in the A/B pass. "
         "Logistics is outside the focus taxonomy."))

L.append(cls("juni", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("52m-series-a-follow-on-investment-in-juni"), entry_date="2021-10", **site_c("juni", "SE"), city="Gothenburg",
    focus="Fintech & Payments",
    note="Financial platform for e-commerce. EQT Ventures entered at the $52M Series A follow-on (the firm's post, 2021-10-14), after the $21.5M Series A of Jul 2021; "
         "EUR 100M Series B 2022 (the firm's post 2022-12-20)."))

L.append(cls("kaiber", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://www.businesswire.com/news/home/20241016279399/en/Kaiber-Launches-Superstudio-a-New-Creative-AI-Platform-for-Seamless-Image-and-Video-Generation",
    entry_date="2024-10", grad="censored", country="US", country_src="web_verified", country_cite=SITE("kaiber"),
    city="Los Angeles", focus="AI & Applied AI",
    note="Generative AI video for artists. A seed round led by EQT Ventures and Crush Ventures, announced with the Superstudio launch (Business Wire, 2024-10-16); inside the window."))

L.append(cls("kive", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-kive"), entry_date="2020-12", **site_c("kive", "SE"), city="Stockholm", focus="SaaS",
    note="AI asset management for creative teams. The firm's post of 2020-12-16 announces its Series Seed. Graduation judged in the surfaces pass."))

L.append(cls("knoetic", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2022/09/21/knoetic-lands-36m-to-unify-diverse-sources-of-hr-data/", entry_date="2022-09",
    country="US", country_src="web_verified", country_cite=SITE("knoetic"), city="New York", focus="SaaS",
    note="Analytics platform for chief people officers. EQT Ventures led the $36M Series B (Sep 2022, TechCrunch), after Accel's $18M Series A (2021)."))

L.append(cls("kota", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.kota.io/blog/kota-raise-5m-seed", entry_date="2023-10",
    grad="graduated", grad_src="web_verified", grad_cite="https://sifted.eu/articles/eqt-ventures-northzone-kota-funding-round-employee-benefits",
    **site_c("kota", "IE"), city="Dublin", focus="Fintech & Payments",
    note="Employee benefits infrastructure (formerly Yonder). 'Kota raise EUR 5M Seed led by EQT Ventures' (the company's blog, Oct 2023); the named $14.5M Series A with "
         "Eurazeo, EQT Ventures and Northzone (Sifted) graduates it."))

L.append(cls("lenus", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2021/06/09/copenhagens-coaching-platform-for-health-and-fitness-professionals-lenus-raises-e50-million-in-series-a-round/",
    entry_date="2021-06", **site_c("lenus", "DK"), city="Copenhagen", focus="Healthcare & Bio",
    note="Coaching platform for health and fitness professionals. EQT Ventures led the EUR 50M Series A, the company's first institutional money (Jun 2021, Tech.eu; "
         "the firm's post 'EQT Ventures invests EUR 50m in Lenus')."))

jl.write("batch-001", L)
