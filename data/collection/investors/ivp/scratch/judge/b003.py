from jl import *
CC="https://index.commoncrawl.org/"
L=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
row("lumafield", status="private", parts=[country("US"), city("Boston","model_knowledge","medium"), stage("Growth","web_verified",post("Lumafield-Fixing-Manufacturings-Blind-Spot"))], valuation_range="below_1b",
    funding_rounds=[rnd("2025-03","Series C",75000000,"IVP",True,post("Lumafield-Fixing-Manufacturings-Blind-Spot"))],
    note="Lumafield, industrial CT scanning, Boston. IVP's post (2025-03-13): 'which is why we're leading their $75M Series C', the entry.")
row("lyra-health", status="private", parts=[city("Burlingame")], flags=["needs_web_value"],
    note="Lyra Health, mental-health benefits, Burlingame CA. IVP led the $75M Series C in 2020 (IVP post 2020-03-11). Valued above $1B from 2020 (Series F 2022 reported at $5.6B); the web pass pins the mark.")
row("marketo", parts=[city("San Mateo")], valuation_range="below_1b",
    note="Marketo, marketing automation, San Mateo. IPO 2013 (MKTO); taken private by Vista in 2016 and sold to Adobe in 2018.")
row("masterclass", parts=[city("San Francisco"), stage("Growth","web_verified",post("yoda-was-wrong-who-says-a-master-can-only-have-one-apprentice"))],
    funding_rounds=[rnd("2017-03","Series C",35000000,"IVP",True,post("yoda-was-wrong-who-says-a-master-can-only-have-one-apprentice"))],
    note="MasterClass, online classes, San Francisco. IVP led the $35M Series C (IVP post 2017-03-28), its entry.")
row("microtune", status="acquired", parts=[country("US"), city("Plano"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Microtune, RF tuner chips, Plano TX. IPO 2000 (TUNE); acquired by Zoran in 2010. IVP funds filed 13Gs 2001-2011; entry round not on record.")
row("mindbody", parts=[city("San Luis Obispo")], valuation_range="below_1b",
    note="Mindbody, wellness-business software, San Luis Obispo CA. IPO 2015 (MB); taken private by Vista in 2019.")
row("mmc-networks", status="acquired", parts=[country("US"), city("Sunnyvale","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="MMC Networks, network-processor chips, Sunnyvale CA. IPO 1997 (MMCN); acquired by AMCC in 2000. Geoff Yang's bio names it among IVP's investments (on Redpoint's previous-by-partners list), and IVP funds filed 13Gs 1998-2000; entry round not on record.")
row("monte-carlo", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("the-data-doesnt-lie-monte-carlo-and-the-future-of-data-observability"))],
    **value(1600000000,"https://www.montecarlodata.com/blog-monte-carlo-raises-135m-series-d/","2022-05","1b_plus","web_verified","medium"),
    flags=["model_disputes_source","stale"],
    funding_rounds=[rnd("2022-05","Series D",135000000,"IVP",True,post("the-data-doesnt-lie-monte-carlo-and-the-future-of-data-observability"))],
    note="Monte Carlo, data observability, San Francisco. IVP led the $135M Series D (IVP post 2022-05-24) at $1.6B, as Redpoint carries; mark older than 24 months. The Wikidata RO belongs to a namesake.")
row("motion-computing", status="acquired", parts=[country("US"), city("Austin")], valuation_range="below_1b",
    note="Motion Computing, rugged tablet PCs, Austin TX. Acquired by Xplore Technologies in 2015.")
row("motive", status="private", parts=[city("San Francisco"), stage("Growth","web_verified",post("keep-truckin-reinventing-telematics"))], flags=["needs_web_value"],
    funding_rounds=[rnd("2018-03","Series C",50000000,"IVP",True,post("keep-truckin-reinventing-telematics"))],
    note="Motive (formerly KeepTruckin), fleet management, San Francisco. IVP led KeepTruckin's $50M Series C (IVP post 2018-03-20). Valued above $1B since 2020 (Series E, $2.85B in 2022); the web pass pins the mark. The keeptruckin row is this company (merge recorded).")
row("mulesoft", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="MuleSoft, integration software, San Francisco. IVP's page: Partnered 2016, a late private position ahead of the March 2017 IPO (MULE). Acquired by Salesforce in 2018.")
row("nerdwallet", parts=[city("San Francisco")], note="NerdWallet, personal finance, San Francisco (NASDAQ: NRDS).")
row("netflix", parts=[city("Los Gatos")],
    note="Netflix, streaming, Los Gatos CA (NASDAQ: NFLX). On Redpoint's previous-by-partners list (IVP's 1990s book) and IVP funds filed 13Gs for 2002-2003, so IVP held pre-IPO shares; the round is to be read off the 2002 prospectus in the A/B pass (the site's 'Partnered 2006' postdates the 2002 IPO and is not the entry).")
row("nextdoor", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], flags=["stage_uncited"],
    note="Nextdoor, neighborhood network, San Francisco (NYSE: NXDR). IVP's page: Partnered 2019, the year of the $170M Series H; round not named in IVP's own post.")
row("nextroll", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("big-market-deep-technology-and-a-great-team-thats-how-ivp-adrolls"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2014-04","Series C",70000000,"IVP",True,post("big-market-deep-technology-and-a-great-team-thats-how-ivp-adrolls"))],
    note="NextRoll (formerly AdRoll), marketing technology, San Francisco. IVP's post (2014-04-21) announces its investment in AdRoll's $70M round of April 2014 (the Series C). The adroll row is this company (merge recorded).")
row("ngmoco", parts=[city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="ngmoco, mobile games, San Francisco. IVP's page: Year Invested 2009; acquired by DeNA in 2010 for up to $403M. Round not named in our sources.")
row("niantic", status="acquired", parts=[city("San Francisco"), stage("Growth","web_verified",post("niantic-viewing-the-world-differently"))], valuation_range="below_1b",
    flags=["model_disputes_source"],
    funding_rounds=[rnd("2019-01","Series C",245000000,"IVP",True,post("niantic-viewing-the-world-differently"))],
    note="Niantic, AR games (Pokemon GO), San Francisco. IVP led the $245M Series C (IVP post 2019-01-16). Niantic sold its games business to Scopely in 2025 ($3.5B) and spun the rest out as Niantic Spatial, so acquired, as Battery and Spark carry; the unicorn list's $3.95B is superseded.")
row("numeric", status="private", parts=[country("US"), city("San Francisco"), stage("Series A","web_verified",post("numeric-using-AI-to-create-accounting-magic"))], valuation_range="below_1b",
    funding_rounds=[rnd("2024-10","Series A",28000000,None,True,post("numeric-using-AI-to-create-accounting-magic"))],
    note="Numeric, accounting automation, San Francisco. IVP joins the $28M Series A (IVP post 2024-10-10).")
row("obsidian-security", status="private", parts=[country("US"), city("Newport Beach"), stage("Growth","web_verified",post("obsidian-and-an-industry-shift"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2022-04","Series C",100000000,"IVP",True,post("obsidian-and-an-industry-shift"))],
    note="Obsidian Security, SaaS security, Newport Beach CA. IVP announced its investment 2022-04-14, the $100M Series C.")
row("ondeck-capital", parts=[country("US"), city("New York"), stage("Growth","web_verified",post("congratulations-to-our-friends-at-ondeck"))], valuation_range="below_1b",
    funding_rounds=[rnd("2013-02","Series D",59000000,"IVP",True,post("congratulations-to-our-friends-at-ondeck"))],
    note="OnDeck, small-business lending, New York. 'IVP led OnDeck's $59 million Series D financing in February of 2013' (IVP post 2014-12-17). IPO 2014 (ONDK); acquired by Enova in 2020.")
row("oportun", parts=[city("San Carlos")], note="Oportun (formerly Progreso Financiero), consumer lending, San Carlos CA (NASDAQ: OPRT). The progreso-financiero row is this company (merge recorded).")
row("papaya-global", parts=[country("IL"), city("Tel Aviv"), stage("Growth","model",None,"medium")], flags=["model_disputes_source","stage_uncited","cite_pending"],
    note="Papaya Global, global payroll, Tel Aviv. IVP's page: Partnered 2021 (first captured April 2021), the $100M Series C of March 2021; to be cited in the A/B pass. The Wikidata 'Israel / United States' is not a country code.")
row("paper", status="private", parts=[city("Montreal"), stage("Growth","web_verified",post("paper-the-a-platform-for-transforming-education"))], valuation_range="below_1b",
    funding_rounds=[rnd("2021-06","Series C",100000000,"IVP",True,post("paper-the-a-platform-for-transforming-education"))],
    note="Paper, online tutoring, Montreal. IVP led the $100M Series C (IVP post 2021-06-30).")
row("perplexity", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("perplexity-where-knowledge-begins"))], flags=["needs_web_value"],
    funding_rounds=[rnd("2024-01","Series B",73600000,"IVP",True,post("perplexity-where-knowledge-begins"))],
    note="Perplexity, AI search, San Francisco. 'IVP is leading Perplexity's Series B funding round of $73.6M' (IVP post 2024-01-04), the entry. Valued far above $1B since; the web pass pins the latest mark.")
row("personal-capital", status="acquired", parts=[city("Redwood City")], valuation_range="below_1b",
    note="Personal Capital, digital wealth management, Redwood City CA. Acquired by Empower in 2020 (up to $1B).")
row("pigment", status="private", parts=[country("FR"), city("Paris"), stage("Growth","web_verified",post("pigment-the-true-colors-of-next-gen-business-planning"),"medium")], flags=["needs_web_value"],
    funding_rounds=[rnd("2022-09","Series C",88000000,"ICONIQ Growth and IVP",True,post("pigment-the-true-colors-of-next-gen-business-planning"))],
    note="Pigment, business planning software, Paris. IVP's post (2022-09-29) announces its investment in the $88M Series C. A 2024 $145M Series D is a signal, so the band is checked on the web before a below-$1B rule-out.")
row("pindrop", status="private", parts=[city("Atlanta")], valuation_range="below_1b",
    note="Pindrop, voice fraud prevention, Atlanta. Private; last disclosed marks below $1B.")
row("podium", parts=[city("Lehi"), stage("Growth","web_verified",post("podium-broadcasting-greatness"))],
    **value(3000000000,"https://www.pymnts.com/news/investment-tracker/2021/podium-closes-201m-series-d-funding-deal/","2021-11","1b_plus","web_verified","medium"),
    flags=["stale"],
    funding_rounds=[rnd("2018-06","Series B",60000000,"IVP",True,post("podium-broadcasting-greatness")), rnd("2021-11","Series D",201000000,None,None,"https://www.pymnts.com/news/investment-tracker/2021/podium-closes-201m-series-d-funding-deal/","press")],
    note="Podium, local-business messaging, Lehi UT. IVP led the $60M Series B (IVP post 2018-06-07). Series D (November 2021) at $3B, superseding the unicorn list's $1.5B, as Accel and Y Combinator carry; stale.")
row("polycom", parts=[city("San Jose"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Polycom, conferencing equipment, San Jose. IVP's own page: Year Invested 1991, a year after founding, so an early round, but the round is not named in our sources. IPO 1996; taken private by Siris Capital in 2016.")
row("productiv", status="private", parts=[country("US"), city("Palo Alto"), stage("Growth","web_verified",post("productiv-say-goodbye-to-your-saas-spreadsheet"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2021-03","Series C",45000000,"IVP",True,post("productiv-say-goodbye-to-your-saas-spreadsheet"))],
    note="Productiv, SaaS management, Palo Alto. IVP announced its investment 2021-03-31, the $45M Series C it led.")
row("progreso-financiero", parts=[city("San Carlos")], flags=["identity_conflated"],
    note="Progreso Financiero is Oportun's former name (renamed 2015, one CIK); the oportun row is this company (merge recorded, applies at the rebuild).")
row("prosper", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["model_disputes_source","stage_uncited"],
    note="Prosper, consumer lending marketplace, San Francisco. IVP's page: Partnered 2014 (IVP release 2014-05-05), a late position in a company founded in 2005; the round is not named. The Wikidata PL belongs to a namesake.")
row("pure-storage", parts=[city("Santa Clara"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Pure Storage, flash storage, Santa Clara CA (NYSE: PSTG). IVP's page: Year Invested 2013, the year of the $150M Series E; to be cited in the A/B pass.")
row("retailmenot", parts=[city("Austin")], valuation_range="below_1b",
    note="RetailMeNot, digital coupons, Austin TX. IPO 2013 (SALE); acquired by Harland Clarke in 2017.")
row("roam", status="private", parts=[city("Miami Beach","model_knowledge","medium")], valuation_range="below_1b",
    note="Roam (ro.am), virtual office for distributed teams, Miami Beach (the firm's own Location; the Form D address is Brooklyn). IVP led the $30M Series A (IVP post 2022-11-02).")
row("robinhood", status="public", parts=[city("Menlo Park"), stage("Growth","model",None,"medium")],
    **value(93920000000,"https://stockanalysis.com/stocks/hood/market-cap/","2026-09","10b_plus"),
    flags=["stage_uncited","cite_pending"],
    note="Robinhood, brokerage, Menlo Park (NASDAQ: HOOD). IVP's post (2021-07-29): in 2020 IVP made 'the biggest single investment in the history of our firm' in Robinhood, i.e. the 2020 Series F/G financings; round to be cited in the A/B pass. Cap as Thrive carries.")
row("rubrik", parts=[city("Palo Alto"), stage("Growth","web_verified",post("ten-reasons-why-ivp-invested-in-rubrik"))],
    funding_rounds=[rnd("2017-05","Series D",180000000,"IVP",True,post("ten-reasons-why-ivp-invested-in-rubrik"))],
    note="Rubrik, data security, Palo Alto (NYSE: RBRK). IVP led the $180M Series D (IVP post 2017-05-02), its entry.")
row("sage", status="private", parts=[country("US"), city("New York"), stage("Growth","web_verified",post("sage-bringing-caregiving-into-the-21st-century"))], valuation_range="below_1b", flags=["model_disputes_source"],
    funding_rounds=[rnd("2024-12","Series B",35000000,"IVP",True,post("sage-bringing-caregiving-into-the-21st-century"))],
    note="Sage (hellosage.com), senior-living care tech, New York. IVP leads the $35M Series B (IVP post 2024-12-05). The Wikidata PL belongs to a namesake.")
row("seon", status="private", parts=[country("GB"), city("London"), stage("Growth","web_verified",post("seon-kicking-frauds-butt"))], valuation_range="below_1b",
    funding_rounds=[rnd("2022-04","Series B",94000000,"IVP",True,post("seon-kicking-frauds-butt"))],
    note="SEON, fraud prevention, London (founded in Budapest). IVP led the $94M Series B with Creandum and Portfolion (IVP post 2022-04-19).")
row("skydio", status="private", parts=[city("San Mateo"), stage("Growth","model",None,"medium")],
    **value(4400000000,"https://www.skydio.com/blog/skydio-series-f","2026-04","1b_plus"),
    flags=["stage_uncited","cite_pending"],
    note="Skydio, autonomous drones, San Mateo CA. IVP's pages: Partnered 2017/2018, the $42M Series B of January 2018; to be cited. Series F (2026) at $4.4B, as a16z and Accel carry.")
row("slack", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Slack, team messaging, San Francisco. IVP's page: Partnered 2015, the $160M round of April 2015 (the Series E). IPO 2019 (WORK); acquired by Salesforce in 2021.")
row("snap", parts=[country("US"), city("Santa Monica"), stage("Growth","web_verified",post("ten-reasons-why-ivp-invested-in-snapchat"),"medium")],
    funding_rounds=[rnd("2013-06","Series B",60000000,"IVP",True,post("ten-reasons-why-ivp-invested-in-snapchat"))],
    note="Snap (Snapchat), Santa Monica CA (NYSE: SNAP). IVP's post (2013-06-24): 'Snapchat today announced it recently closed a new round of financing with IVP as the lead investor', the $60M Series B.")
row("sofi", parts=[city("San Francisco"), stage("Growth","web_verified",post("sofi-lighting-a-path-to-financial-success-for-generations-to-come"))],
    funding_rounds=[rnd("2015-02","Series D",200000000,None,True,post("sofi-lighting-a-path-to-financial-success-for-generations-to-come"))],
    note="SoFi, consumer finance, San Francisco (NASDAQ: SOFI). 'IVP first invested in SoFi in February 2015, participating in a $200 million equity financing round' (IVP post 2021-06-14), the Series D.")
row("sorare", parts=[city("Paris"), stage("Growth","web_verified",post("sorare-the-next-generation-of-fantasy-sports"))],
    funding_rounds=[rnd("2021-09","Series B",680000000,"SoftBank",True,post("sorare-the-next-generation-of-fantasy-sports"))],
    note="Sorare, fantasy football, Paris. IVP participated in the $680M Series B (IVP post 2021-09-20). Band left to the A/B pass: Accel reads below $1B on the 2025 contraction.")
row("soundcloud", status="private", parts=[country("DE"), city("Berlin"), stage("Growth","web_verified",post("why-soundcloud-will-rule-the-digital-audio-world"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2014-01","growth round",60000000,"IVP",True,post("why-soundcloud-will-rule-the-digital-audio-world"))],
    note="SoundCloud, audio platform, Berlin. IVP led the round announced January 2014 (IVP post 2014-01-24), a $60M round in a six-year-old company. The 2017 rescue round was priced well below $1B.")
write("../queue/batch-003.out.jsonl", L)
