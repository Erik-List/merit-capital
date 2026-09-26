from jl import *
CC="https://index.commoncrawl.org/"
L=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
def old(slug, city_, st="acquired", note="", cc_="US", conf="high", **extra):
    parts=[]
    if cc_: parts.append(country(cc_))
    if city_: parts.append(city(city_,"model_knowledge",conf))
    parts.append(stage("undetermined","model",None,"low"))
    row(slug, status=st, parts=parts, valuation_range="below_1b", note=note, **extra)
row("aerohive-networks", parts=[city("Milpitas"), stage("Growth","web_verified",CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/aerohive-announces--22-5-million-mezzanine-equity-financing-led-by-institutional-venture-partners&output=json")], valuation_range="below_1b",
    funding_rounds=[rnd("2012","mezzanine",22500000,"IVP",True,CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/aerohive-announces--22-5-million-mezzanine-equity-financing-led-by-institutional-venture-partners&output=json")],
    note="Aerohive Networks, cloud Wi-Fi, Milpitas CA. IVP's archived release: '$22.5 Million Mezzanine Equity Financing Led by IVP' (2012, the firm's Year Invested), a pre-IPO round: Growth. IPO 2014 (HIVE); acquired by Extreme Networks in 2019.")
old("agile-software","San Jose",note="Agile Software, product lifecycle management, San Jose. IPO 1999; acquired by Oracle in 2007. On IVP's 2013-2016 list; entry round not on record.")
row("akamai", parts=[country("US"), city("Cambridge"), stage("undetermined","model",None,"low")],
    note="Akamai Technologies, content delivery, Cambridge MA (NASDAQ: AKAM). On IVP's 2013-2016 portfolio list (the firm's own listing); IVP's round is not on record in our sources.")
row("alienvault", status="acquired", parts=[country("US"), city("San Mateo"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="AlienVault, unified security management, San Mateo. IVP's page: Year Invested 2015, the $52M Series D of February 2015 that IVP led. Acquired by AT&T in 2018.")
row("altera", parts=[city("San Jose"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Altera, programmable logic, San Jose. IPO 1988 (ALTR); acquired by Intel in 2015 (Intel sold a 51% stake to Silver Lake in 2025, a new owner of the acquired business). IVP's early round is not named in our sources.")
old("amati-communications","Mountain View",conf="medium",note="Amati Communications, DSL modems, Mountain View CA. Acquired by Texas Instruments in 1997. Entry round not on record.")
row("anthropic", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Anthropic, AI safety and research, San Francisco. IVP's page: Partnered 2026 (first on the site April 2026), so a 2026 round (the $30B Series G of February 2026 or later); to be cited in the A/B pass.")
row("app-annie", status="acquired", parts=[city("San Francisco")], valuation_range="below_1b", flags=["identity_conflated"],
    note="App Annie renamed itself data.ai in 2022; the data-ai row is this company (merge recorded, applies at the rebuild).")
row("appcharge", status="private", parts=[city("Tel Aviv"), stage("Growth","web_verified",post("appcharge-putting-power-back-in-the-hands-of-game-developers"))], valuation_range="below_1b",
    funding_rounds=[rnd("2025-08","Series B",58000000,"IVP",True,post("appcharge-putting-power-back-in-the-hands-of-game-developers"))],
    note="Appcharge, direct-to-consumer payments for games, Tel Aviv. IVP leads the $58M Series B (IVP post 2025-08-13).")
row("archive", parts=[country("US"), city("Costa Mesa","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["model_disputes_source"],
    note="Archive Corporation, tape drives, Costa Mesa CA. IPO (ACHV); acquired by Conner Peripherals in 1993. The Wikidata ZA is a namesake's. Entry round not on record.")
old("artisan-components","Sunnyvale",conf="medium",note="Artisan Components, semiconductor IP, Sunnyvale CA. IPO 1998; acquired by ARM in 2004. Entry round not on record.")
old("ask-jeeves","Oakland",conf="medium",note="Ask Jeeves, search, Oakland CA (Emeryville earlier). IPO 1999 (ASKJ); acquired by IAC in 2005. Geoff Yang's bio names it among IVP's investments (on Redpoint's previous-by-partners list); entry round not on record.")
row("aspect", status="acquired", parts=[country("US"), city("San Jose"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["identity_homonym"],
    note="Aspect Communications (Aspect Telecommunications), call-center systems, San Jose. IPO 1990 (ASPT); acquired by Concerto Software in 2005, as Menlo carries. Not Y Combinator's 'Aspect' rows (different companies). Entry round not on record.")
row("aster-data-systems", parts=[city("San Carlos"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Aster Data Systems, analytic database, San Carlos CA. IVP's page: Year Invested 2009; acquired by Teradata in 2011. Round not named in our sources.")
old("borland-software","Austin",conf="medium",note="Borland Software, developer tools, Austin TX (Scotts Valley CA until 2007). IPO (BORL); acquired by Micro Focus in 2009. Entry round not on record.")
old("bridge-communications","Mountain View",conf="medium",note="Bridge Communications, LAN internetworking, Mountain View CA. IPO (QBCI); merged into 3Com in 1987. Entry round not on record.")
row("business-com", status="acquired", parts=[country("US"), city("Santa Monica"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Business.com, B2B search directory, Santa Monica (New York on IVP's later page). IVP's page: Year Invested 2004; acquired by R.H. Donnelley in 2007. Round not named in our sources.")
row("cape", status="private", parts=[country("US"), city("Washington","model_knowledge","medium"), stage("Growth","web_verified",post("cape-security-at-the-mobile-core"))], valuation_range="below_1b",
    funding_rounds=[rnd("2026-03","Series C",100000000,"IVP (co-lead)",True,post("cape-security-at-the-mobile-core"))],
    note="Cape, privacy-first mobile carrier, Washington DC. IVP is co-leading the $100M Series C (IVP post 2026-03-19).")
old("chemconnect","San Francisco",note="ChemConnect, online chemicals exchange, San Francisco. Acquired by IntercontinentalExchange in 2007. On Redpoint's previous-by-partners list (the founders' IVP/Brentwood book); entry round not on record.")
old("cipher-data-products","San Diego",conf="medium",note="Cipher Data Products, tape drives, San Diego. Acquired by Archive Corporation in 1990. Entry round not on record.")
row("cirrus-logic", parts=[city("Austin"), stage("undetermined","model",None,"low")],
    note="Cirrus Logic, mixed-signal chips, Austin TX (NASDAQ: CRUS). On IVP's 2013-2016 list; IVP's early-1980s round is not named in our sources.")
row("comscore-networks", parts=[country("US"), city("Reston"), stage("undetermined","model",None,"low")],
    note="comScore, digital audience measurement, Reston VA (NASDAQ: SCOR). IVP's page: Year Invested 2000; round not named in our sources.")
row("connectandsell", status="private", parts=[country("US"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="ConnectAndSell, sales dialing service. On IVP's 2013-2014 list; still operating; round not named. City to be placed in the web pass.")
row("constant-contact", parts=[city("Waltham"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Constant Contact, email marketing, Waltham MA. IPO 2007; acquired by Endurance International in 2016. Entry round not on record.")
row("cortina-systems", status="acquired", parts=[city("Sunnyvale"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Cortina Systems, communications chips, Sunnyvale CA. Acquired by Inphi in 2014. Entry round not on record.")
row("cowboy-space-corporation", status="private", parts=[stage("Growth","web_verified",post("the-sun-never-sets"),"medium")], flags=["needs_web_value"],
    funding_rounds=[rnd("2026-05","Series B",None,None,True,post("the-sun-never-sets"))],
    note="Cowboy Space Corporation, orbital compute infrastructure (Baiju Bhatt). IVP's post (2026-05-11) announces its part in the Series B. A hot-sector 2026 raise, so the band is web-checked; city to be placed in the web pass.")
row("danger", status="acquired", parts=[country("US"), city("Palo Alto"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Danger, Hiptop/Sidekick phones, Palo Alto. IVP's page: Year Invested 2004; acquired by Microsoft in 2008. Round not named in our sources.")
row("data-domain", status="acquired", parts=[city("Santa Clara"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Data Domain, deduplication storage, Santa Clara. IPO 2007; acquired by EMC in 2009. Entry round not on record.")
row("digital-river", status="acquired", parts=[city("Minnetonka"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Digital River, e-commerce services, Minnetonka MN. IPO 1998; taken private by Siris Capital in 2015. Entry round not on record.")
row("dropcam", parts=[city("San Francisco"), stage("Growth","web_verified",CC+"CC-MAIN-2013-48-index?url=http://www.ivp.com/news/press-release/dropcam-secures--30-million-in-series-c-funding-led-by-institutional-venture-partners&output=json")], valuation_range="below_1b",
    funding_rounds=[rnd("2013","Series C",30000000,"IVP",True,CC+"CC-MAIN-2013-48-index?url=http://www.ivp.com/news/press-release/dropcam-secures--30-million-in-series-c-funding-led-by-institutional-venture-partners&output=json")],
    note="Dropcam, Wi-Fi video cameras, San Francisco. IVP's archived release: 'Dropcam Secures $30 Million in Series C Funding Led by IVP' (2013). Acquired by Google/Nest in 2014.")
row("dust-networks", status="acquired", parts=[city("Hayward","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Dust Networks, wireless sensor networks, Hayward CA. Acquired by Linear Technology in 2011. Entry round not on record.")
row("ehealth", parts=[country("US"), city("Austin","model_knowledge","medium"), stage("undetermined","model",None,"low")],
    note="eHealth, online health insurance, Austin TX (Santa Clara until its move). IPO 2006 (EHTH); still listed. Entry round not on record.")
row("exabyte", status="acquired", parts=[country("US"), city("Boulder"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["model_disputes_source"],
    note="Exabyte, tape storage, Boulder CO. Its business was sold to Tandberg Data in 2006, which IVP's own page records (the link goes to Tandberg): an asset sale, so acquired, not defunct. Entry round not on record.")
row("ftx", status="defunct", parts=[country("BS"), city("Nassau"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="FTX, crypto exchange, Nassau. On IVP's 2021-2022 pages; IVP's position came in the 2021 growth rounds. Filed for Chapter 11 in November 2022: defunct under the bankruptcy ruling, as Sequoia and Lightspeed carry.")
row("gaia-interactive", status="acquired", parts=[country("US"), city("San Jose","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Gaia Interactive (Gaia Online), anime social network, San Jose. The community was sold on (2015); entry round not on record.")
row("gamma", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending","model_disputes_source"],
    note="Gamma, AI presentations, San Francisco. IVP's page: Partnered 2025, the $68M Series B of November 2025 at $2.1B (Accel's citation); round to be cited. The Wikidata RU belongs to a namesake.")
row("genlogs", status="private", parts=[country("US"), stage("Growth","web_verified",post("genlogs-seeing-the-road-clearly"))], valuation_range="below_1b",
    funding_rounds=[rnd("2026-02","Series B",None,None,True,post("genlogs-seeing-the-road-clearly"))],
    note="GenLogs, truck intelligence, US. IVP's post (2026-02-02): 'partnering with Ryan and the GenLogs team on their Series B'. City to be placed in the web pass.")
row("h5", status="private", parts=[country("US"), city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["model_disputes_source"],
    note="H5, legal search and e-discovery, San Francisco. IVP's page: Year Invested 2005; round not named. The Wikidata FR belongs to a namesake.")
old("hands-on-mobile","San Francisco",conf="medium",note="Hands-On Mobile, mobile games, San Francisco. Acquired by RockYou in 2011. Entry round not on record.")
row("hopin", status="acquired", parts=[country("GB"), city("London"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Hopin, virtual events, London. IVP's page: Partnered 2020, the $125M Series B of November 2020 that IVP and Coatue led. Its events business went to RingCentral (2023) and StreamYard to Bending Spoons (2024): acquired, as a16z and Accel carry.")
old("ic-works","San Jose",conf="medium",note="IC Works, clock chips, San Jose. Acquired by Cypress Semiconductor in 1999. Entry round not on record.")
row("juniper-networks", parts=[city("Sunnyvale"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Juniper Networks, routers, Sunnyvale. IVP's page: Year Invested 1996, the founding year, and Geoff Yang's own bio names it among IVP's investments; the round is not named in our sources. Acquired by HPE in July 2025, as Benchmark carries.")
row("kalshi", parts=[city("New York"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Kalshi, regulated prediction markets, New York. IVP's page: Partnered 2025 (IVP post 2025-12-02), a 2025 growth round; to be cited in the A/B pass.")
row("kayak", parts=[country("US"), city("Stamford"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Kayak, travel search, Stamford CT. IVP's page: Year Invested 2010, two years before the 2012 IPO: a late private position. Acquired by Priceline in 2013.")
write("../queue/batch-005a.out.jsonl", L)
L2=[{"slug":"ivp-silicon-valley","verdict":"not_member","evidence_class":"site_listing","confidence":"high","who":"agent",
     "basis":"T5: 'IVP Silicon Valley' is the firm's own office entry that the 2016 WordPress portfolio page carried beside the company tiles (a scrape artifact of the listing, not a company); it names no business, has no page of its own, and appears on no other surface.",
     "citation":"https://index.commoncrawl.org/CC-MAIN-2016-40-index?url=http://www.ivp.com/portfolio/&output=json"}]
write("../queue/batch-005v.out.jsonl", L2)
