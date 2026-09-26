from jl import *
CC="https://index.commoncrawl.org/"
L=[]
def row(slug, **k):
    d={"slug":slug}; 
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)

row("abridge", parts=[city("Pittsburgh"), stage("Growth","web_verified",post("abridge-transforming-patient-outcomes-one-conversation-at-a-time"))],
    funding_rounds=[rnd("2024-02","Series C",150000000,None,True,post("abridge-transforming-patient-outcomes-one-conversation-at-a-time"))],
    note="Abridge, generative AI for clinical documentation, Pittsburgh. IVP's own post (2024-02-23) says IVP is participating in the $150M Series C; the site's Partnered 2024 dates it as the entry.")
row("accompany-health", status="private", parts=[country("US"), stage("Series A","web_verified",post("accompany-health-a-return-to-values-based-healthcare"))], valuation_range="below_1b",
    funding_rounds=[rnd("2024-01","Series A",56000000,None,True,post("accompany-health-a-return-to-values-based-healthcare"))],
    note="Accompany Health, primary and behavioral care for low-income patients, launched January 2024. IVP's post (2024-01-30) says IVP participated in the $56M Series A at launch; no later priced round known.")
row("aiven", parts=[city("Helsinki"), stage("Growth","web_verified",post("aiven-the-open-source-data-cloud"))],
    funding_rounds=[rnd("2020-02","Series B",40000000,"IVP",True,post("aiven-the-open-source-data-cloud"))],
    note="Aiven, managed open-source data cloud, Helsinki. IVP led the $40M Series B (IVP post 2020-02-05, Eric Liaw joined the board); Partnered 2020.")
row("ajaib", parts=[city("Jakarta"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Ajaib, Indonesian retail brokerage, Jakarta. IVP's post (2021-10-07) announces the investment without naming the round; it coincides with Ajaib's October 2021 $153M Series B that made it a unicorn, so the entry reads Growth pending a citation that names IVP in that round.")
row("aledade", status="private", parts=[country("US"), city("Bethesda"), stage("Growth","web_verified",post("aledade-improving-data-driven-patient-outcomes"))], flags=["needs_web_value"],
    funding_rounds=[rnd("2021-01","Series D",100000000,None,True,post("aledade-improving-data-driven-patient-outcomes"))],
    note="Aledade, accountable-care organisation for independent practices, Bethesda MD. IVP participated in the $100M Series D (IVP post 2021-01-19). Later rounds put it above $1B (Series F 2022); the web pass pins the mark.")
row("amplitude", parts=[city("San Francisco")], note="Amplitude, product analytics, San Francisco (NASDAQ: AMPL).")
row("anomali", status="private", parts=[city("Redwood City")], valuation_range="below_1b",
    note="Anomali, threat intelligence platform, Redwood City CA (the firm's own Location). Still private; last priced rounds were well below $1B.")
row("appdynamics", parts=[city("San Francisco"), stage("Growth","web_verified",CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/appdynamics-secures--50-million-financing-round--kicks-off-2013-with-300-percent-growth&output=json")], valuation_range="below_1b",
    funding_rounds=[rnd("2013-01","Series D",50000000,"IVP",True,CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/appdynamics-secures--50-million-financing-round--kicks-off-2013-with-300-percent-growth&output=json")],
    note="AppDynamics, application performance monitoring, San Francisco. IVP's archived release: the $50M January 2013 round (the Series D) that IVP led; the firm's Year Invested is 2013. Acquired by Cisco in 2017 for $3.7B, so no standalone mark.")
row("applied-digital-access", status="acquired", parts=[country("US"), city("San Diego","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Applied Digital Access, telco test and monitoring systems, San Diego. IVP's 2013-2014 listing: IPO (ADAX), later acquired by Acterna. IVP funds filed 13Gs in 1997-1998. The round IVP entered is not on record in our sources, so the stage is undetermined.")
row("arcsight", status="acquired", parts=[city("Cupertino"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="ArcSight, security information and event management, Cupertino. IVP's own page: Year Invested 2002; IPO 2008 (ARST), acquired by HP in 2010. The 2002 round IVP entered is not named in any source on disk.")
row("at-road", status="acquired", parts=[country("US"), city("Fremont","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="@Road, mobile resource management, Fremont CA. IVP listing: IPO (ARDI), acquired by Trimble in 2007. IVP funds filed 13Gs 2001-2007. Entry round not on record.")
row("attentive", status="private", parts=[country("US"), city("New York"), stage("Growth","web_verified",post("attentive-getting-the-message-across"))], flags=["needs_web_value"],
    funding_rounds=[rnd("2019-08","Series B",None,None,True,post("attentive-getting-the-message-across")), rnd("2020-01","Series C",70000000,"IVP (co-lead)",True,post("attentive-getting-the-message-across"))],
    note="Attentive, SMS marketing platform, New York. IVP's post (2020-01) says IVP co-led the $70M Series C and 'originally invested in the Series B, completed in August 2019': the entry is the Series B. Later valued above $1B (2021 Series E); the web pass pins the mark.")
row("ayasdi", status="acquired", parts=[city("Menlo Park")], valuation_range="below_1b",
    note="Ayasdi, topological data analysis, Menlo Park CA. Acquired by SymphonyAI in 2019.")
row("baseten", status="private", parts=[city("San Francisco"), stage("Growth","web_verified",post("baseten-engineering-the-foundations-of-ai"))],
    **value(13000000000,"https://www.baseten.co/blog/announcing-our-series-f/","2026-06-22","10b_plus"),
    flags=["stage_disputes_band"],
    funding_rounds=[rnd("2024-03","Series B",40000000,"IVP",True,post("baseten-engineering-the-foundations-of-ai"))],
    note="Baseten, AI model inference, San Francisco. IVP's own post (2024-03-04) says IVP led the Series B, the entry; the Form D layer anchored a 2026 filing instead (a later round), hence stage_disputes_band on the source, not the label. Series F (2026-06-22) at $13B, as Battery, Greylock and Spark carry.")
row("business-insider", status="acquired", parts=[country("US"), city("New York"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Business Insider, digital business news, New York. IVP's own page: Partnered 2011. Acquired by Axel Springer in 2015 (88%, valuing it near $442M). The 2011 round IVP entered is not named in our sources.")
row("buddy-media", status="acquired", parts=[city("New York")], valuation_range="below_1b",
    note="Buddy Media, social media marketing software, New York. Acquired by Salesforce in 2012 (~$689M).")
row("cafepress", status="acquired", parts=[city("Louisville"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["model_disputes_source"],
    note="CafePress, print-on-demand marketplace, Louisville KY. IPO 2012 (PRSS); taken private by Snapfish (District Photo) in 2018, so acquired, not public: the SEC float layer's public reading is stale. IVP's entry round is not on record.")
row("carbonite", status="acquired", parts=[city("Boston"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["model_disputes_source"],
    note="Carbonite, online backup, Boston. IPO 2011 (CARB); acquired by OpenText in December 2019, so the float layer's public reading is stale. Entry round not on record.")
row("care-com", status="acquired", parts=[city("Waltham"), stage("Growth","web_verified",CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/care-com-raises--50-million-in-e-round-financing-led-by-institutional-venture-partners&output=json")], valuation_range="below_1b", flags=["model_disputes_source"],
    funding_rounds=[rnd("2012","Series E",50000000,"IVP",True,CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/care-com-raises--50-million-in-e-round-financing-led-by-institutional-venture-partners&output=json")],
    note="Care.com, online care marketplace, Waltham MA. IVP's archived release: 'Care.com Raises $50 Million in E-Round Financing Led by IVP' (2012, the firm's Year Invested). IPO 2014 (CRCM), acquired by IAC in February 2020, so acquired rather than public.")
row("casper", status="acquired", parts=[country("US"), city("New York"), stage("Growth","web_verified",post("ivp-sleeps-easy-with-investment-in-casper"))], valuation_range="below_1b", flags=["model_disputes_source"],
    funding_rounds=[rnd("2015-06","Series B",55000000,"IVP",True,post("ivp-sleeps-easy-with-investment-in-casper"))],
    note="Casper, direct-to-consumer mattresses, New York. IVP led the $55M 2015 growth round (its post, 2015-06-23: '$30 million investment'). IPO 2020 (CSPR); taken private by Durational Capital in January 2022, so acquired.")
row("chainguard", status="private", parts=[country("US"), city("Kirkland"), stage("Growth","web_verified",post("chainguard-the-solution-to-open-source-security"))],
    **value(3500000000,"https://www.chainguard.dev/unchained/chainguard-raises-356-million-series-d","2025-04","1b_plus"),
    funding_rounds=[rnd("2024","Series C",140000000,None,True,post("chainguard-the-solution-to-open-source-security")), rnd("2025-04","Series D",356000000,None,None,"https://www.chainguard.dev/unchained/chainguard-raises-356-million-series-d","company")],
    note="Chainguard, secure open-source software supply chain, Kirkland WA. IVP's post (2024-07-25): 'We're investing in Chainguard's $140 million Series C'. Series D (April 2025) at $3.5B, as Lightspeed, Redpoint and Spark carry.")
row("checkr", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Checkr, background-check platform, San Francisco. IVP's site: Partnered 2015; Checkr's 2015 rounds were a $9M Series A (Accel) and a $40M Series B (December 2015), so the IVP entry reads Growth pending a citation naming IVP in the B.")
row("chordiant-software", status="acquired", parts=[country("US"), city("Cupertino"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Chordiant Software, CRM software, Cupertino. IPO 2000; acquired by Pegasystems in 2010. IVP funds filed 13Gs in 2004-2007; entry round not on record.")
row("circleci", status="private", parts=[city("San Francisco"), stage("Growth","web_verified",post("circleci-a-virtuous-developer-circle"))], flags=["needs_web_value"],
    funding_rounds=[rnd("2020-04","Series E",100000000,"IVP",True,post("circleci-a-virtuous-developer-circle"))],
    note="CircleCI, CI/CD platform, San Francisco. IVP led the $100M Series E (IVP post 2020-04-07). Series F (2021) was reported at $1.7B; the web pass pins or kills the mark.")
row("clarify", status="acquired", parts=[country("US"), city("San Jose"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["identity_homonym"],
    note="Clarify, the 1990s customer-relationship software company, San Jose. IVP listing: IPO 1995 (CLFY), acquired by Nortel (1999) and later Amdocs. Not Clarify Health (Spark's row): a homonym. Entry round not on record.")
row("clickhouse", parts=[city("San Francisco"), stage("Growth","web_verified",post("clickhouse-the-database-that-lets-you-have-it-all"))],
    **value(15000000000,"https://techcrunch.com/2026/01/16/snowflake-databricks-challenger-clickhouse-hits-15b-valuation/","2026-01-16","10b_plus"),
    flags=["model_disputes_source"],
    funding_rounds=[rnd("2025-05","Series C",350000000,None,True,post("clickhouse-the-database-that-lets-you-have-it-all")), rnd("2026-01","Series D",400000000,"Dragoneer",None,"https://techcrunch.com/2026/01/16/snowflake-databricks-challenger-clickhouse-hits-15b-valuation/","press")],
    note="ClickHouse, analytical database, San Francisco. IVP joined the $350M Series C (IVP post 2025-05-29). The January 2026 Series D priced it at $15B, superseding the unicorn list's $2B, as Battery, Thrive and Lightspeed carry.")
row("clipboard-health", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("clipboard-health-doing-well-by-doing-good"))],
    **value(1300000000,"https://www.businesswire.com/news/home/20220414005913/en/Clipboard-Health-Secures-Total-of-$80M-in-Funding-Reaching-$1.3B-Valuation","2022-02","1b_plus","web_verified","medium"),
    flags=["stale"],
    funding_rounds=[rnd("2021-06","Series B",None,"IVP",True,post("clipboard-health-doing-well-by-doing-good")), rnd("2022-02","Series C",None,"Sequoia",None,post("clipboard-health-doing-well-by-doing-good"))],
    note="Clipboard Health, healthcare staffing marketplace, San Francisco. IVP's post (2022-04-18): IVP's Series B investment in June 2021, then Sequoia's Series C (February 2022) reaching $1.3B. Mark older than 24 months: stale.")
row("coinbase", status="public", parts=[city("San Francisco","model_knowledge","medium"), stage("Growth","web_verified",post("coinbase-unlocking-the-value-of-digital-currencies"))],
    **value(48710000000,"https://companiesmarketcap.com/coinbase/marketcap/","2026-09-04","10b_plus"),
    funding_rounds=[rnd("2017-08","Series D",100000000,"IVP",True,post("coinbase-unlocking-the-value-of-digital-currencies"))],
    note="Coinbase, crypto exchange, remote-first (San Francisco as last office HQ). IVP led the $100M Series D in 2017, its initial investment (IVP posts 2017-08-10 and 2021-04-14). NASDAQ: COIN since 2021; cap as Y Combinator carries.")
row("compass", parts=[city("New York"), stage("Growth","web_verified",post("compass-transforming-the-real-estate-market-with-an-advanced-technology-platform"))],
    **value(9460000000,"https://stockanalysis.com/stocks/comp/","2026-09","1b_plus"),
    flags=["stage_disputes_band","identity_homonym"],
    funding_rounds=[rnd("2015-09","Series C",50000000,"IVP",True,post("compass-transforming-the-real-estate-market-with-an-advanced-technology-platform"))],
    note="Compass, real-estate brokerage platform, New York (NYSE: COMP). IVP's post (2021-04-14): 'we led the $50 million Compass Series C round at a $750 million pre-money valuation in September of 2015', the entry. The 2012 Form D the sweep attached is Compass Labs, Inc. of San Jose (Ajay Vashee, years before he joined IVP), a homonym, so its band says nothing about this row.")
row("concur-technologies", parts=[country("US"), city("Bellevue","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Concur Technologies, travel and expense software, Bellevue WA (Redmond on IVP's page). IPO 1998 (CNQR); acquired by SAP in 2014. IVP funds filed 13Gs and Form 4s 2000-2004 and the company sits on Redpoint's previous-by-partners list (IVP's 1990s book). The firm's page says Year Invested 2003, which reads as a later position; the entry round is not on record.")
row("cortex", status="private", parts=[country("US"), city("San Francisco","model_knowledge","medium"), stage("Growth","web_verified",post("cortex-a-central-brain-for-engineering-services"))], valuation_range="below_1b", flags=["model_disputes_source"],
    funding_rounds=[rnd("2023-05","Series B",35000000,"IVP",True,post("cortex-a-central-brain-for-engineering-services"))],
    note="Cortex (cortex.io), internal developer portal, San Francisco (YC W20). IVP led the $35M Series B (IVP post 2023-05-31). The pre-filled FR country came from a namesake's Wikidata entry and is wrong.")
row("cradle", status="private", parts=[country("NL"), city("Amsterdam"), stage("Growth","web_verified",post("cradle-digital-biology-through-ai"))], valuation_range="below_1b",
    funding_rounds=[rnd("2024-11","Series B",73000000,"IVP",True,post("cradle-digital-biology-through-ai"))],
    note="Cradle (cradle.bio), AI protein engineering, Amsterdam (offices in Zurich). IVP led the $73M Series B (IVP post 2024-11-26). Not the Bangalore YC company of the same name.")
row("cribl", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("cribl-observing-the-right-trend"))],
    **value(3500000000,"https://cribl.io/press/cribl-raises-319-million-series-e/","2024-08","1b_plus"),
    funding_rounds=[rnd("2021-08","Series C",200000000,None,True,post("cribl-observing-the-right-trend")), rnd("2024-08","Series E",319000000,"GV",None,"https://cribl.io/press/cribl-raises-319-million-series-e/","company")],
    note="Cribl, observability data pipelines, San Francisco. IVP's post (2021-08-25) announces its Series C investment. Series E (August 2024) at $3.5B, as Greylock and Redpoint carry.")
row("crowdstrike", parts=[city("Austin"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="CrowdStrike, endpoint security, Austin TX (moved from Sunnyvale in 2021). IVP's site: Partnered 2018; IVP co-led the $200M Series E in June 2018 with General Atlantic and Accel, to be cited in the A/B pass.")
row("curology", status="private", parts=[country("US"), city("San Francisco")], valuation_range="below_1b",
    note="Curology, prescription skincare, San Francisco. Partnered 2019 per IVP's site; still private, no unicorn mark.")
row("cyence", status="acquired", parts=[country("US"), city("San Mateo"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Cyence, cyber-risk analytics for insurers, San Mateo. IVP announced its investment 2016-09-08 (the $30M Series B, per press at the time); acquired by Guidewire in 2017 for ~$275M.")
row("data-ai", status="acquired", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("shining-a-light-on-the-mobile-ecosystemwelcome-appt-annie-to-the-ivp-portfolio"))], valuation_range="below_1b",
    funding_rounds=[rnd("2015-01","Series E",55000000,"IVP",True,post("shining-a-light-on-the-mobile-ecosystemwelcome-appt-annie-to-the-ivp-portfolio"))],
    note="data.ai (formerly App Annie), mobile app intelligence, San Francisco. IVP led the $55M round announced 2015-01-13 (IVP post). Acquired by Sensor Tower in 2024, so acquired although the firm's page still reads Active.")
row("datadog", parts=[city("New York"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Datadog, cloud monitoring, New York (NASDAQ: DDOG). IVP's site: Partnered 2018, after Datadog's last priced primary (Series D, 2016), so the entry was a late private purchase (a secondary, Growth by policy); to be cited in the A/B pass.")
row("datalogix", parts=[city("Denver","model_knowledge","medium"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Datalogix, offline purchase data for digital ads, Westminster/Denver CO. IVP's archived release: 'Datalogix Closes $25 Million Financing Led by IVP' (December 2013), a $25M round for an 11-year-old company, above the era's Series A band; acquired by Oracle in 2015.")
row("dataminr", parts=[city("New York"), stage("Growth","web_verified",CC+"CC-MAIN-2013-48-index?url=http://ivp.com/news/press-release/dataminr-raises--30-million-in-funding-led-by-venrock-and-ivp&output=json","medium")],
    funding_rounds=[rnd("2013-12","Series C",30000000,"Venrock and IVP",True,CC+"CC-MAIN-2013-48-index?url=http://ivp.com/news/press-release/dataminr-raises--30-million-in-funding-led-by-venrock-and-ivp&output=json")],
    note="Dataminr, real-time event detection, New York. IVP's archived release: 'Dataminr Raises $30 Million in Funding Led by Venrock and IVP' (2013), the company's third priced round (the Series C); Year Invested 2013.")
row("deepl", status="private", parts=[country("DE"), city("Cologne"), stage("Growth","web_verified",post("deepl-a-step-change-in-ai-powered-language-translation"))], flags=["needs_web_value"],
    funding_rounds=[rnd("2023-01","Series B",None,"IVP",True,post("deepl-a-step-change-in-ai-powered-language-translation"))],
    note="DeepL, AI translation, Cologne. IVP led the Series B (IVP post 2023-01-11). Valued at $2B in May 2024; the web pass pins the mark.")
row("deputy", parts=[city("Sydney"), stage("Growth","web_verified",post("every-shift-on-deputy-why-ivp-invested-in-deputy"))],
    funding_rounds=[rnd("2018-11","Series B",81000000,"IVP",True,post("every-shift-on-deputy-why-ivp-invested-in-deputy"))],
    note="Deputy, workforce management software, Sydney. IVP led the $81M Series B (IVP post 2018-11-28).")
row("digital-impact", status="acquired", parts=[country("US"), city("San Mateo"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Digital Impact, e-mail marketing, San Mateo. IPO 1999 (DIGI); acquired by Acxiom in 2005. IVP funds filed 13Gs 2000-2004; entry round not on record.")
row("discord", parts=[city("San Francisco"), stage("Growth","web_verified",post("press-play-ivp-invests-in-discord"))],
    funding_rounds=[rnd("2018-04","growth round",None,"IVP",True,post("press-play-ivp-invests-in-discord"))],
    note="Discord, voice and text chat, San Francisco. IVP's post (2018-04-25) says IVP led Discord's new round of growth financing, its entry; 'growth' collapses onto Growth.")
write("../queue/batch-001.out.jsonl", L)
