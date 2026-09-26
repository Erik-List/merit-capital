from jl import *
CC="https://index.commoncrawl.org/"
L=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
ccp=lambda crawl,path: CC+crawl+"-index?url="+path+"&output=json"
row("steelbrick", status="acquired", parts=[country("US"), city("San Mateo"), stage("Growth","web_verified",post("the-abcs-of-qtc-why-ivp-invested-in-steelbrick"))], valuation_range="below_1b",
    funding_rounds=[rnd("2015-03","Series C",None,None,True,post("the-abcs-of-qtc-why-ivp-invested-in-steelbrick"))],
    note="SteelBrick, quote-to-cash software, San Mateo. IVP's Series C investment (IVP post 2015-03-15). Acquired by Salesforce in December 2015 (~$360M).")
row("sublime-security", status="private", parts=[country("US"), stage("Growth","web_verified",post("theres-a-new-standard-in-ai-powered-email-security-and-its-sublime"))], valuation_range="below_1b",
    funding_rounds=[rnd("2024-12","Series B",60000000,"IVP",True,post("theres-a-new-standard-in-ai-powered-email-security-and-its-sublime"))],
    note="Sublime Security, email security. IVP leads the $60M Series B (IVP post 2024-12-12). City to be placed in the web pass.")
row("sumo-logic", parts=[city("Redwood City"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Sumo Logic, log analytics, Redwood City CA. IVP's page: Partnered 2015, the $80M Series F of June 2015. IPO 2020 (SUMO); taken private by Francisco Partners in 2023.")
row("supercell", parts=[city("Helsinki"), stage("Growth","web_verified",ccp("CC-MAIN-2016-07","http://ivp.com/news/press-release/ivp-co-leads--130-million-financing-in-supercell"))], valuation_range="below_1b",
    funding_rounds=[rnd("2012-12","Series B",130000000,"Index Ventures, IVP (co-leads)",True,ccp("CC-MAIN-2016-07","http://ivp.com/news/press-release/ivp-co-leads--130-million-financing-in-supercell"))],
    note="Supercell, mobile games, Helsinki. IVP's archived release: 'IVP co-leads $130 million financing in Supercell' (the Series B of December 2012; the firm's Year Invested is 2013, when it closed). Acquired by SoftBank in 2013 and by Tencent in 2016.")
row("superhuman", status="acquired", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], valuation_range="below_1b",
    valuation_usd=None, valuation_source=None, valuation_asof=None, flags=["stage_uncited","model_disputes_source"],
    note="Superhuman (Superhuman Labs), email client, San Francisco. IVP led the $75M Series C in September 2021 (Partnered 2021). Acquired by Grammarly in July 2025 (Grammarly then took the Superhuman name), so acquired, as a16z and First Round carry; the unicorn list's $13B and the Wikidata country belong to Grammarly.")
row("supermetrics", status="private", parts=[country("FI"), city("Helsinki"), stage("Growth","web_verified",post("supermetrics-a-data-superhero"))], valuation_range="below_1b", flags=["model_disputes_source"],
    funding_rounds=[rnd("2020-08","Series B",None,None,True,post("supermetrics-a-data-superhero"))],
    note="Supermetrics, marketing data integration, Helsinki. IVP participated in the EUR 40M Series B (IVP post 2020-08-24). The Wikidata SG belongs to a namesake.")
row("symyx-technologies", status="acquired", parts=[city("Santa Clara"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Symyx Technologies, materials discovery, Santa Clara CA. IPO 1999 (SMMX); merged into Accelrys in 2010. IVP funds filed 13Gs 2000-2001; entry round not on record.")
row("synchronoss", parts=[country("US"), city("Bridgewater"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Synchronoss Technologies, carrier cloud software, Bridgewater NJ. IVP's page: Year Invested 2005, a year before the June 2006 IPO (SNCR); the pre-IPO round is not named in our sources.")
row("tala", status="private", parts=[country("US"), city("Los Angeles"), stage("Growth","web_verified",post("the-future-of-finance-announcing-ivps-investment-in-tala"),"medium")], valuation_range="below_1b", flags=["model_disputes_source"],
    funding_rounds=[rnd("2017-02","Series B",30000000,"IVP",True,post("the-future-of-finance-announcing-ivps-investment-in-tala"))],
    note="Tala, mobile credit in emerging markets, Los Angeles. IVP announced its investment 2017-02-22, the $30M Series B it led. The Wikidata DZ belongs to a namesake.")
row("tanium", parts=[city("Kirkland"), stage("Growth","web_verified",post("tanium-starting-from-the-end-point"),"medium")],
    funding_rounds=[rnd("2015-09","growth round",120000000,None,True,post("tanium-starting-from-the-end-point"))],
    note="Tanium, endpoint management and security, Kirkland WA (Emeryville until 2020). IVP's post (2015-09-02) announces its investment in the $120M round of September 2015. Unicorn-list $9B (2020) to be cited in the A/B pass.")
row("taxbit", status="private", parts=[city("Draper","formd_address","medium"), stage("Growth","web_verified",post("taxbit-the-most-fun-weve-ever-had-talking-about-taxes"))], flags=["stage_disputes_band","needs_web_value"],
    funding_rounds=[rnd("2021-08","Series B",130000000,"IVP (co-lead)",True,post("taxbit-the-most-fun-weve-ever-had-talking-about-taxes"))],
    note="TaxBit, crypto tax and accounting software, Draper UT (Salt Lake City on IVP's page). IVP co-led the $130M Series B (IVP post 2021-08-12), its entry; the band read Tom Loverro's 2023 filing as a Series A. The Series B was reported at $1.33B, so the web pass pins or kills the mark.")
row("telcom-semiconductor", status="acquired", parts=[country("US"), city("Mountain View","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="TelCom Semiconductor, analog chips, Mountain View CA. IPO 1995 (TLCM); acquired by Microchip in 2000. IVP funds filed 13Gs 1996-1998; entry round not on record.")
row("tennr", status="private", parts=[country("US"), city("New York"), stage("Growth","web_verified",post("tennr-a-cure-for-healthcare-paperwork"))], valuation_range="below_1b",
    funding_rounds=[rnd("2025-06","Series C",101000000,"IVP",True,post("tennr-a-cure-for-healthcare-paperwork"))],
    note="Tennr, healthcare referral automation, New York. IVP leads the $101M Series C (IVP post 2025-06-18), reported at about $605M.")
row("the-honest-company", parts=[city("Los Angeles")], note="The Honest Company, consumer goods, Los Angeles (Playa Vista; Santa Monica on older pages; NASDAQ: HNST).")
row("the-players-tribune", status="acquired", parts=[country("US"), city("New York"), stage("Growth","web_verified",post("ivp-steps-up-to-the-plate-with-the-players-tribune"))], valuation_range="below_1b",
    funding_rounds=[rnd("2017-01","Series C",40000000,"IVP",True,post("ivp-steps-up-to-the-plate-with-the-players-tribune"))],
    note="The Players' Tribune, athlete media, New York. IVP led the $40M Series C (IVP post 2017-01-19). Acquired by Minute Media in 2019.")
row("thrive-global", status="private", parts=[country("US"), city("New York"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Thrive Global, behavior-change platform, New York (Arianna Huffington). IVP's page: Partnered 2017, a growth round that year; round not named in our sources.")
row("tivo", parts=[country("US"), city("San Jose"), stage("Series A","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="TiVo, digital video recorders, San Jose (Alviso). IVP's page: Year Invested 1997, the company's founding year, and Geoff Yang's own bio names TiVo among IVP's investments: IVP co-led the first institutional round with NEA. Acquired by Rovi in 2016.")
row("traceable", status="acquired", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("traceable-ai-a-revolutionary-approach-to-api-security"))], valuation_range="below_1b",
    funding_rounds=[rnd("2022-05","Series B",60000000,"IVP",True,post("traceable-ai-a-revolutionary-approach-to-api-security"))],
    note="Traceable, API security, San Francisco (Jyoti Bansal). IVP led the Series B (IVP post 2022-05-03). Merged into Harness in 2025 ('Acquired by Harness 2025' on IVP's page).")
row("transmeta", status="acquired", parts=[country("US"), city("Santa Clara"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Transmeta, low-power processors, Santa Clara. IPO 2000 (TMTA); acquired by Novafora in 2009. IVP funds filed 13Gs 2001-2009; entry round not on record.")
row("tunein", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",ccp("CC-MAIN-2013-48","http://www.ivp.com/news/press-release/tunein-raises--25-million-and-surpasses-one-billion-listening-hours-in-2013"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2013-12","Series C",25000000,"IVP",True,ccp("CC-MAIN-2013-48","http://www.ivp.com/news/press-release/tunein-raises--25-million-and-surpasses-one-billion-listening-hours-in-2013"))],
    note="TuneIn, internet radio, San Francisco. IVP's archived release: 'TuneIn Raises $25 Million and Surpasses One Billion Listening Hours in 2013', the December 2013 round IVP led (the firm's Year Invested 2013). Still private.")
row("twitter", parts=[city("San Francisco"), stage("Growth","web_verified",post("ten-reasons-why-ivp-invested-in-snapchat"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2009-02","Series C",35000000,"Benchmark and IVP",True,post("ten-reasons-why-ivp-invested-in-snapchat"))],
    note="Twitter, San Francisco. IVP's own post (2013-06-24): 'IVP co-invested in Twitter along side Benchmark in February 2009', the $35M Series C. IPO 2013; taken private by Elon Musk in 2022, so acquired.")
row("uber", status="public", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"low")],
    **value(144000000000,"https://stockanalysis.com/stocks/uber/market-cap/","2026-08-06","100b_plus"),
    flags=["stage_uncited","cite_pending","model_disputes_source"],
    note="Uber, San Francisco (NYSE: UBER). IVP's page: Partnered 2015, a late private position (the 2015 rounds or a secondary); to be cited in the A/B pass. The Wikidata NL is Uber's Dutch holding entity, not its HQ. Cap as Sequoia carries.")
row("uipath", parts=[city("New York"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="UiPath, robotic process automation, New York (NYSE: PATH). IVP's page: Partnered 2018 (IVP post 2018-11-14), the $225M Series C of September 2018; to be cited in the A/B pass.")
row("vercel", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Vercel, frontend cloud, San Francisco. IVP's page: Partnered 2024, the $250M Series E of May 2024; to be cited. Series F (2025) at $9.3B per the siblings' citation.")
row("veriff", status="private", parts=[city("Tallinn"), stage("Growth","web_verified",post("veriff-powering-trust-online"))], flags=["needs_web_value"],
    funding_rounds=[rnd("2021-04","Series B",69000000,"IVP",True,post("veriff-powering-trust-online"))],
    note="Veriff, identity verification, Tallinn. IVP led the $69M Series B with Accel (IVP post 2021-04-12). The January 2022 Series C was reported at $1.5B; the web pass pins or kills the mark.")
row("volt", status="private", parts=[country("GB"), city("London"), stage("Growth","web_verified",post("volt-connecting-real-time-payments-everywhere"))], valuation_range="below_1b", flags=["model_disputes_source"],
    funding_rounds=[rnd("2023-06","Series B",60000000,"IVP",True,post("volt-connecting-real-time-payments-everywhere"))],
    note="Volt (volt.io), real-time payments, London. IVP leads the $60M Series B (IVP post 2023-06-21). The Wikidata NO belongs to a namesake.")
row("vonage", parts=[city("Holmdel"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Vonage, VoIP, Holmdel NJ. IVP funds filed Forms 3 and 4 at the May 2006 IPO, so IVP held pre-IPO shares; the round is not named in our sources. Acquired by Ericsson in 2022.")
row("voxer", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Voxer, push-to-talk messaging, San Francisco. Wikipedia: 'In April 2012, the company raised $30 million in venture financing from Institutional Venture Partners (IVP)', a $30M round in a five-year-old company; the round word is not given.")
row("whip-media-group", status="private", parts=[city("Santa Monica"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Whip Media Group (formerly Whip Networks / Whipclip), entertainment data, Santa Monica. IVP's page: Founded and Partnered 2014; the round is not named in our sources. whip-networks and whipclip are this company (merged pre-prepare).")
row("whoop", parts=[city("Boston")], note="WHOOP, wearable fitness, Boston. IVP led the $100M Series E (IVP post 2020-10-28).")
row("wise", status="public", parts=[city("London"), stage("Growth","web_verified","https://en.wikipedia.org/wiki/Wise_(company)","medium")],
    **value(12600000000,"https://stockanalysis.com/stocks/wse/market-cap/","2026-08","10b_plus"),
    funding_rounds=[rnd("2017-11","Series E",280000000,"Old Mutual Global Investors and IVP",True,"https://en.wikipedia.org/wiki/Wise_(company)","press")],
    note="Wise (formerly TransferWise), cross-border payments, London (LSE: WISE, direct listing 2021). 'In November 2017, the company raised a $280 million Series E led by Old Mutual Global Investors and Institutional Venture Partners' (Wikipedia), which IVP announced 2017-11-01. Cap as a16z carries.")
row("woven", status="acquired", parts=[city("Culver City")], valuation_range="below_1b",
    note="Woven Digital, pop-culture publisher, Culver City CA. No longer independent (acquired, as Felicis carries).")
row("xad", status="private", parts=[city("New York")], valuation_range="below_1b", flags=["identity_conflated"],
    note="xAd is GroundTruth's former name (renamed 2017); the groundtruth row is this company (merge recorded, applies at the rebuild).")
row("yellowbrick-data", status="private", parts=[country("US"), city("Mountain View"), stage("Growth","web_verified",post("yellowbrick-the-ultimate-data-warehouse"))], valuation_range="below_1b",
    funding_rounds=[rnd("2019-06","Series C",81000000,None,True,post("yellowbrick-the-ultimate-data-warehouse"))],
    note="Yellowbrick Data, data warehousing, Mountain View CA. IVP's Series C investment (IVP post 2019-06-05).")
row("yext", parts=[city("New York")], note="Yext, digital presence software, New York (NYSE: YEXT). IVP pushed to lead the Series B in 2009 (IVP post 2017-05-09).")
row("yodlee", parts=[city("Redwood City")], valuation_range="below_1b",
    note="Yodlee, financial data aggregation, Redwood City CA. IPO 2014 (YDLE); acquired by Envestnet in 2015 and by STG in 2022.")
row("zefr", status="private", parts=[city("Los Angeles")], valuation_range="below_1b",
    note="ZEFR, brand-safety and video rights software, Los Angeles (Venice). IVP led the $30M growth round of February 2014 (IVP release).")
row("zendesk", parts=[city("San Francisco"), stage("Growth","web_verified",post("a-month-of-zen"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2014-02","late-stage investment",None,None,True,post("a-month-of-zen"))],
    note="Zendesk, customer service software, San Francisco. IVP's post (2014-03-06) announces its February 2014 investment 'as a late-stage investor', three months before the May 2014 IPO: Growth. Taken private by Hellman & Friedman and Permira in 2022.")
row("zenefits", status="acquired", parts=[city("San Francisco"), stage("Growth","web_verified",ccp("CC-MAIN-2014-23","http://ivp.com/news/press-release/zenefits-raises--66-5-million-in-series-b-funding-led-by-andreessen-horowitz"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2014-06","Series B",66500000,"Andreessen Horowitz",True,ccp("CC-MAIN-2014-23","http://ivp.com/news/press-release/zenefits-raises--66-5-million-in-series-b-funding-led-by-andreessen-horowitz"))],
    note="Zenefits, HR software, San Francisco. IVP's archived release on its own site: 'Zenefits Raises $66.5 Million In Series B Funding Led By Andreessen Horowitz' (2014, IVP in the round). Acquired by TriNet in 2022.")
row("zerto", parts=[city("Boston"), stage("Growth","web_verified",post("the-importance-of-getting-your-zzzs-ivp-adds-zerto-to-the-portfolio"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2016-01","Series E",50000000,"IVP",True,post("the-importance-of-getting-your-zzzs-ivp-adds-zerto-to-the-portfolio"))],
    note="Zerto, disaster recovery software, Boston (R&D in Herzliya). IVP announced its investment 2016-01-13, the $50M Series E it led. Acquired by HPE in 2021.")
row("ziprecruiter", parts=[city("Santa Monica")], note="ZipRecruiter, online hiring, Santa Monica (NYSE: ZIP). IVP's $63M investment in 2014 (IVP release).")
row("zynga", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Zynga, social games, San Francisco. IVP's page: Partnered 2008, the $29M Series B of July 2008 (Kleiner Perkins led, IVP in). IPO 2011; acquired by Take-Two in 2022.")
row("addthis", status="acquired", parts=[city("McLean"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="AddThis (Clearspring), web sharing tools, McLean VA. IVP's page: Year Invested 2011; acquired by Oracle in 2016. Round not named in our sources.")
row("adroll", status="private", parts=[city("San Francisco")], valuation_range="below_1b", flags=["identity_conflated"],
    note="AdRoll became NextRoll in 2018; the nextroll row is this company (merge recorded, applies at the rebuild).")
row("advent-software", status="acquired", parts=[country("US"), city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Advent Software, investment-management software, San Francisco. IPO 1995; acquired by SS&C in 2015. On IVP's 2013-2016 list; entry round not on record.")
write("../queue/batch-004.out.jsonl", L)
