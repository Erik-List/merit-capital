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
def dup(slug, canon, city_, st, note):
    row(slug, status=st, parts=[city(city_)] if city_ else [], valuation_range="below_1b", flags=["identity_conflated"], note=note)
old("klout","San Francisco",note="Klout, social influence scores, San Francisco. IVP's page: Year Invested 2011; acquired by Lithium Technologies in 2014. Round not named in our sources.")
row("langchain", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified","https://techcrunch.com/2025/10/21/open-source-agentic-startup-langchain-hits-1-25b-valuation","medium")],
    **value(1250000000,"https://techcrunch.com/2025/10/21/open-source-agentic-startup-langchain-hits-1-25b-valuation","2025-10","1b_plus"),
    funding_rounds=[rnd("2025-10","Series B",125000000,"IVP",True,"https://techcrunch.com/2025/10/21/open-source-agentic-startup-langchain-hits-1-25b-valuation","press")],
    note="LangChain, agent framework, San Francisco. IVP's page: Partnered 2025; IVP led the $125M Series B of October 2025 at $1.25B (TechCrunch 2025-10-21), as Benchmark, Sequoia and Lux carry the mark.")
old("lensvector","Mountain View",st="defunct",conf="medium",note="LensVector, liquid-crystal autofocus optics, Mountain View CA. On IVP's 2014 list; defunct, as Menlo carries. Entry round not on record.")
old("limelight-networks","Tempe",conf="medium",note="Limelight Networks, content delivery, Tempe AZ. IPO 2007; merged with Edgecast in 2022 to form Edgio, which filed for Chapter 11 in 2024 and sold its assets to Akamai: insolvency followed by an asset sale, so acquired. Entry round not on record.")
row("liveops", status="private", parts=[city("Scottsdale","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Liveops, on-demand contact-center agents, Scottsdale AZ (Redwood City earlier). IVP's page: Year Invested 2007. The agent-network company still operates privately (its cloud software was sold to Serenova in 2016), as Menlo carries; Benchmark reads acquired. Round not named in our sources.")
old("livingsocial","Washington",note="LivingSocial, daily deals, Washington DC. Acquired by Groupon in 2016. IVP's round is not named in our sources.")
row("loopnet", parts=[city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="LoopNet, commercial real-estate listings, San Francisco. IPO 2006 (LOOP); acquired by CoStar in 2012. On Redpoint's previous-by-partners list; entry round not on record.")
row("lsi", parts=[country("US"), city("San Jose"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="LSI Logic, custom chips, San Jose. IVP's page: Year Invested 1980; Wikipedia: 'Initial funding of $6 million came from a consortium of venture capitalists, including Kleiner Perkins Caufield & Byers II, Institutional Venture Partners, and Technical Development Capital'. The round word is not given (the pre-2003 Series A convention is retired). Acquired by Avago in 2014.")
old("luminate-software","Redwood City",conf="low",note="Luminate Software, e-application management, Redwood City CA. Acquired (IVP's page names EMC; the business went to Computer Associates). Entry round not on record.")
row("markmonitor", status="acquired", parts=[city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="MarkMonitor, brand protection, San Francisco. IVP's page: Year Invested 2003; acquired by Thomson Reuters in 2012. Round not named in our sources.")
row("mips-technologies", parts=[city("Sunnyvale"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="MIPS Technologies, processor IP, Sunnyvale. IPO 1998; acquired by Imagination Technologies in 2013. Entry round not on record.")
row("mobile-365", status="acquired", parts=[country("US"), city("Chantilly"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Mobile 365 (formerly InphoMatch/Mobileway), mobile messaging, Chantilly VA. IVP's page: Year Invested 2004; acquired by Sybase in 2006. Round not named in our sources.")
row("mobileiron", parts=[city("Mountain View"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="MobileIron, mobile device management, Mountain View. IVP's page: Year Invested 2012; IPO 2014 (MOBL); acquired by Ivanti in 2020. Round not named in our sources.")
old("motosport","Wilsonville",conf="low",note="MotoSport, powersports parts e-commerce, Oregon. Acquired (Liberty Interactive per IVP's page). Entry round not on record.")
row("mysql", status="acquired", parts=[country("SE"), city("Uppsala"), stage("Growth","web_verified","https://en.wikipedia.org/wiki/MySQL_AB","medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2006-02","third round",18500000,"IVP",True,"https://en.wikipedia.org/wiki/MySQL_AB","press")],
    note="MySQL AB, open-source database, Uppsala (US office Cupertino). Wikipedia: 'A third round of about $18.5 million financing led by Institutional Venture Partners ... was disclosed in February 2006' (IVP's Year Invested 2005): the company's third priced round. Acquired by Sun Microsystems in 2008 for $1B.")
old("neocad","Boulder",conf="medium",note="NeoCAD, FPGA design tools, Boulder CO. Acquired by Xilinx in 1995. Entry round not on record.")
row("neophotonics", parts=[country("US"), city("San Jose"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="NeoPhotonics, optical components, San Jose. IPO 2011 (NPTN); acquired by Lumentum in 2022. Entry round not on record.")
row("omniture", status="acquired", parts=[city("Orem"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["needs_review"],
    note="Omniture, web analytics, Orem UT. Acquired by Adobe in 2009. IVP's page says Year Invested 2009, three years after the 2006 IPO, and no IVP fund filed on Omniture: if the position was a public purchase or sale consideration it is out (T3; the 2026-09-22 ruling). Raised for the recall pass; membership stands on the listing meanwhile.")
row("one-kings-lane", status="acquired", parts=[city("San Francisco"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="One Kings Lane, home decor flash sales, San Francisco. IVP's page: Year Invested 2011 (Sandy Miller's deal), a round after the 2010 Series A; acquired by Bed Bath & Beyond in 2016.")
old("onebox","San Mateo",conf="low",note="Onebox.com, unified messaging, San Mateo CA. Acquired by Phone.com in 2000 (later Openwave). On Redpoint's previous-by-partners list; entry round not on record.")
row("platinum-software", status="acquired", parts=[country("US"), city("Irvine","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Platinum Software, financial software, Irvine CA; renamed Epicor Software in 1999, which Apax took private in 2011. Entry round not on record.")
row("popsugar", status="acquired", parts=[country("US"), city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="POPSUGAR, women's media, San Francisco. IVP's page: Year Invested 2011; acquired by Group Nine Media in 2019. Round not named in our sources.")
dup("qadium","expanse","San Francisco","acquired","Qadium renamed itself Expanse in 2019; the expanse row is this company (merge recorded, applies at the rebuild).")
old("quality-semiconductor","Santa Clara",conf="medium",note="Quality Semiconductor, CMOS logic, Santa Clara CA. IPO (QUAL); acquired by IDT in 1999. Entry round not on record.")
row("qubole", status="acquired", parts=[country("US"), city("Santa Clara","model_knowledge","medium"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Qubole, big-data platform, Santa Clara CA (Mountain View on IVP's page). IVP's page: Year Invested 2015, announced on IVP's blog ('Qubole: Doing Big Data Right'); acquired by Idera in 2020.")
row("quigo-technologies", status="acquired", parts=[country("US"), city("New York"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Quigo Technologies, contextual advertising, New York. IVP's page: Year Invested 2006; acquired by AOL in 2007. Round not named in our sources.")
old("red-pepper-software","San Mateo",conf="medium",note="Red Pepper Software, manufacturing scheduling software, San Mateo CA. Acquired by PeopleSoft in 1996. Entry round not on record.")
old("rgb-networks","Sunnyvale",conf="medium",note="RGB Networks, IP video delivery, Sunnyvale CA. Acquired by Imagine Communications in 2014. Entry round not on record.")
row("sauce-labs", status="private", parts=[city("San Francisco"), stage("Growth","web_verified",CC+"CC-MAIN-2017-04-index?url=https://www.ivp.com/news/blog/ivp-invests-in-red-hot-testing-company-sauce-labs/&output=json","medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2016","growth round",None,"IVP",True,CC+"CC-MAIN-2017-04-index?url=https://www.ivp.com/news/blog/ivp-invests-in-red-hot-testing-company-sauce-labs/&output=json")],
    note="Sauce Labs, cloud testing, San Francisco. IVP's archived post 'IVP Invests in Red-Hot Testing Company Sauce Labs' (2016, the firm's Year Invested): a growth round in a company on its fourth year of funding. Still private.")
row("seagate-technology", status="public", parts=[city("Dublin","model_knowledge","medium"), stage("undetermined","model",None,"low")], flags=["needs_web_value"],
    note="Seagate Technology, hard drives, Dublin (Irish-domiciled since 2010; operations in Fremont/Cupertino CA). IVP's page: Year Invested 1980, the year after founding; the round is not named. NASDAQ: STX; the web pass pins the cap.")
row("sequent-computer-systems", parts=[country("US"), city("Beaverton"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Sequent Computer Systems, multiprocessor servers, Beaverton OR. IPO (SQNT); acquired by IBM in 1999. Entry round not on record.")
row("shazam", status="acquired", parts=[city("London"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Shazam, music recognition, London. IVP's page: Year Invested 2011; acquired by Apple in 2018. Round not named in our sources.")
row("skystream-networks", status="acquired", parts=[country("US"), city("Sunnyvale"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="SkyStream Networks, video over IP, Sunnyvale CA. IVP's page: Year Invested 2003; acquired by Tandberg Television in 2006. Round not named in our sources.")
row("solace-health", status="private", parts=[country("US"), stage("Growth","web_verified",post("solace-health-adds-a-healthy-dose-of-humanity-to-healthcare"))], valuation_range="below_1b",
    funding_rounds=[rnd("2026-02","Series C",130000000,"IVP",True,post("solace-health-adds-a-healthy-dose-of-humanity-to-healthcare"))],
    note="Solace Health, patient advocacy, US. IVP leads the $130M Series C (IVP post 2026-02-10). City to be placed in the web pass.")
row("spiceworks", status="acquired", parts=[city("Austin"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Spiceworks, IT professional network, Austin TX. IVP's page: Year Invested 2010; acquired by Ziff Davis in 2019. Round not named in our sources.")
old("stratus-technologies","Marlborough",conf="medium",note="Stratus Computer, fault-tolerant servers, Marlborough MA. IPO; acquired by Ascend Communications in 1998 (later Lucent). Entry round not on record.")
old("successfactors","South San Francisco",note="SuccessFactors, talent management SaaS, South San Francisco. IPO 2007; acquired by SAP in 2012. Entry round not on record.")
row("suno", parts=[city("Cambridge"), stage("Growth","model",None,"medium")],
    **value(5400000000,"https://variety.com/2026/digital/news/ai-music-suno-funding-round-400-million-5-4-billion-valuation-1236765727/","2026-06","1b_plus"),
    flags=["stage_uncited","cite_pending"],
    note="Suno, AI music, Cambridge MA. IVP's page: Partnered 2026 (IVP post 2026-06-03), the $400M round of June 2026 at $5.4B, as Lightspeed and USV carry; the round word to be cited in the A/B pass.")
row("supportsoft", parts=[country("US"), city("Sunnyvale","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="SupportSoft (renamed Support.com), support automation, Sunnyvale CA. IPO 2000; merged into Greenidge Generation in 2021. Entry round not on record.")
old("synoptics-communications","Santa Clara",note="SynOptics Communications, LAN hubs, Santa Clara CA. IPO (SNPX); merged with Wellfleet in 1994 to form Bay Networks. Entry round not on record.")
old("teros","Santa Clara",conf="low",note="Teros, application security gateways, Santa Clara CA. Acquired by Citrix in 2005. Entry round not on record.")
dup("threatstream","anomali","Redwood City","private","ThreatStream renamed itself Anomali in 2016; the anomali row is this company (merge recorded, applies at the rebuild).")
dup("transferwise","wise","London","public","TransferWise renamed itself Wise in 2021; the wise row is this company (merge recorded, applies at the rebuild).")
row("tripwire", status="acquired", parts=[city("Portland"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Tripwire, change auditing and security, Portland OR. IVP's page: Year Invested 2002; acquired by Thoma Bravo (2011), Belden (2015) and Fortra (2022). Round not named in our sources.")
dup("tv-time","whip-media-group","Santa Monica","private","IVP's 2018-2020 pages list Whip Media under its TV Time app (same leader, address and description); the whip-media-group row is this company (merge recorded, applies at the rebuild).")
write("../queue/batch-006.out.jsonl", L)
