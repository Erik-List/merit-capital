from jl import *
CC="https://index.commoncrawl.org/"
L=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
row("domo", parts=[country("US"), city("American Fork"), stage("undetermined","model",None,"low")],
    note="Domo, business intelligence cloud, American Fork UT (NASDAQ: DOMO since 2018). IVP's own page: Partnered 2011, the year of Domo's first institutional round; which round IVP joined is not named in our sources.")
row("doubleverify", parts=[city("New York")], note="DoubleVerify, ad verification, New York (NYSE: DV).")
row("dream-games", parts=[city("Istanbul"), stage("Growth","web_verified",post("dreaming-the-dream-games"))],
    funding_rounds=[rnd("2021-06","Series B",155000000,None,True,post("dreaming-the-dream-games"))],
    note="Dream Games, mobile games (Royal Match), Istanbul. IVP's post (2021-06-30): IVP is participating in the $155M Series B alongside Index, Makers Fund, Balderton and Kora.")
row("dropbox", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Dropbox, file sync and storage, San Francisco (NASDAQ: DBX). IVP's page: Partnered 2011, the year of the $250M Series B (October 2011, Index led, a large syndicate including IVP); to be cited in the A/B pass.")
row("eightfold", status="private", parts=[country("US"), city("Santa Clara","model_knowledge","medium"), stage("Growth","model",None,"medium")],
    **value(2100000000,"https://techcrunch.com/2021/06/10/ai-startup-eightfold-valued-at-2-1b-in-softbank-led-220m-funding/","2021-06","1b_plus","web_verified","medium"),
    flags=["stage_uncited","cite_pending","stale"],
    note="Eightfold AI, talent intelligence, Santa Clara CA (Mountain View on IVP's older pages). IVP's page: Partnered 2019, the year of the $28M Series C IVP led; SoftBank's $220M round (June 2021) valued it at $2.1B, as Lightspeed carries; mark older than 24 months.")
row("eucalyptus", status="acquired", parts=[city("Goleta","model_knowledge","medium"), stage("Growth","web_verified",CC+"CC-MAIN-2013-20-index?url=http://ivp.com/news/press-release/eycalyptus-announces--30-million-series-c-funding-round&output=json")], valuation_range="below_1b",
    flags=["stage_disputes_band"],
    funding_rounds=[rnd("2012-04","Series C",30000000,"IVP",True,CC+"CC-MAIN-2013-20-index?url=http://ivp.com/news/press-release/eycalyptus-announces--30-million-series-c-funding-round&output=json")],
    note="Eucalyptus Systems, private-cloud software, Goleta CA. IVP's archived release: 'Eucalyptus Announces $30 Million Series C Funding Round' (2012), the round Steve Harrick's Form D seat dates; the band read that filing as a Series A. Acquired by HP in 2014.")
row("excite", status="acquired", parts=[country("US"), city("Redwood City","model_knowledge","medium"), stage("Series A","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Excite (Architext Software), web portal, Redwood City CA. Kleiner Perkins and IVP (Geoff Yang, per his own bio) funded Architext's first venture round in 1994; IPO 1996 (XCIT), merged into @Home Network in 1999, so acquired. On Redpoint's previous-by-partners list: IVP's own position, not Redpoint's.")
row("expanse", status="acquired", parts=[country("US"), city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Expanse (formerly Qadium), internet attack-surface management, San Francisco. IVP's page: Partnered 2017; acquired by Palo Alto Networks in 2020 (~$800M). The 2017 round IVP entered is not named in our sources.")
row("fandom-wikia", status="acquired", parts=[city("San Francisco")], valuation_range="below_1b",
    note="Fandom (formerly Wikia), fan wiki platform, San Francisco. TPG Growth acquired a majority stake in 2018; the company operates privately under that owner, so acquired. Redpoint's row reads defunct, which the company's continued operation contradicts; raised for the wave alignment.")
row("fightcamp", status="private", parts=[country("US"), city("Newport Beach","model_knowledge","medium"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="FightCamp (Hykso), connected boxing fitness, Newport Beach CA. IVP's post (2021-06-30) announces IVP's part in 'the latest funding round', the $90M Series B that IVP led in June 2021.")
row("figma", parts=[country("US"), city("San Francisco"), stage("Growth","model",None,"medium")],
    **value(14490000000,"https://stockanalysis.com/stocks/fig/market-cap/","2026-09-03","10b_plus"),
    flags=["stage_uncited","cite_pending"],
    note="Figma, collaborative design, San Francisco (NYSE: FIG since July 2025; the float layer's $0 is a pre-listing float, not a value). IVP's post (2021-06-24) marks its entry in the $200M Series E of June 2021 (Durable led, $10B), without naming the round; cap as Thrive carries.")
row("fleetmatics", parts=[country("IE"), city("Dublin"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited","model_disputes_source"],
    note="Fleetmatics, SaaS fleet tracking, Dublin (Irish plc; US office Waltham MA), so IE, not the Wikidata US. IVP's page: Partnered 2010, the $70M growth investment IVP made that year. IPO 2012 (FLTX), acquired by Verizon in 2016.")
row("formfactor", status="public", parts=[country("US"), city("Livermore"), stage("undetermined","model",None,"low")], flags=["model_disputes_source","needs_web_value"],
    note="FormFactor, semiconductor probe cards, Livermore CA. Still listed (NASDAQ: FORM), so public, not the float layer's stale acquired; the web pass pins the cap. IVP funds filed 13Gs after the 2003 IPO; the pre-IPO round IVP held is not named in our sources.")
row("found", status="private", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("found-its-not-just-about-what-you-lose-its-about-what-you-find"),"medium")], valuation_range="below_1b",
    funding_rounds=[rnd("2021-12","Series B",100000000,"WestCap",True,post("found-its-not-just-about-what-you-lose-its-about-what-you-find"))],
    note="Found, obesity care platform, San Francisco. IVP's post (2021-12-16) links 'Found raises $100M in Series B funding led by WestCap' as 'our investment in Found'.")
row("foundry-networks", status="acquired", parts=[city("Santa Clara"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["model_disputes_source"],
    note="Foundry Networks, Ethernet switching, Santa Clara CA. IPO 1999; acquired by Brocade in December 2008, so acquired, not the Wikidata-sourced defunct. IVP's position (Geoff Yang's bio names it among 'the firm's investments') predates Redpoint; the round is not on record.")
row("g2", parts=[city("Chicago"), stage("Growth","web_verified",post("bringing-intelligence-to-b2b-purchasing-why-ivp-invested-in-g2-crowd"))],
    funding_rounds=[rnd("2018-10","Series C",55000000,"IVP",True,post("bringing-intelligence-to-b2b-purchasing-why-ivp-invested-in-g2-crowd"))],
    note="G2 (G2 Crowd), software reviews marketplace, Chicago. IVP's post (2018-10-11): IVP's Series C investment, the $55M round Jules Maltz's Form D seat dates.")
row("general-assembly", status="acquired", parts=[city("New York")], valuation_range="below_1b",
    note="General Assembly, tech skills education, New York. Acquired by Adecco in 2018 (~$413M).")
row("giphy", status="acquired", parts=[country("US"), city("New York"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Giphy, GIF search, New York. IVP's page: Partnered 2016, the $72M round of February 2016 that IVP and CRV led. Acquired by Facebook in 2020 and sold on to Shutterstock in 2023.")
row("github", status="acquired", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="GitHub, code hosting, San Francisco. IVP's page: Partnered 2015, the $250M Series B of July 2015 (Sequoia led, IVP and Thrive in). Acquired by Microsoft in 2018 for $7.5B.")
row("glean", status="private", parts=[country("US"), city("Palo Alto"), stage("Growth","web_verified",post("glean-unlocking-enterprise-information-with-AI"),"medium")],
    **value(7200000000,"https://www.glean.com/press/glean-raises-150m-series-f-at-7-2b-valuation-to-accelerate-enterprise-ai-agent-innovation-globally","2025-06","1b_plus"),
    funding_rounds=[rnd("2024-02","Series D",200000000,"Kleiner Perkins and Lightspeed",True,post("glean-unlocking-enterprise-information-with-AI")), rnd("2025-06","Series F",150000000,"Wellington",None,"https://www.glean.com/press/glean-raises-150m-series-f-at-7-2b-valuation-to-accelerate-enterprise-ai-agent-innovation-globally","company")],
    note="Glean, enterprise AI search, Palo Alto. IVP's post (2024-02-27) announces its investment in the February 2024 round (the $200M Series D at $2.2B); Series F (June 2025) at $7.2B, as Sequoia and Lightspeed carry.")
row("glossier", status="private", parts=[city("New York"), stage("Growth","web_verified",post("ivp-just-got-glossier"))], valuation_range="below_1b",
    funding_rounds=[rnd("2016-11","Series B",24000000,"IVP",True,post("ivp-just-got-glossier"))],
    note="Glossier, beauty brand, New York. IVP led the $24M Series B (IVP post 2016-11-30), the entry; the band anchored on Eric Liaw's 2019 seat (the $100M Series D). Below $1B, aligned with Sequoia, Thrive and Spark: the 2021 $1.8B mark did not hold, and the 2025 raise was sought at under $1B (Forbes, 2025-04-11).")
row("grammarly", status="private", parts=[city("San Francisco"), stage("Growth","model",None,"medium")],
    **value(13000000000,"https://en.wikipedia.org/wiki/Grammarly","2021-11","10b_plus","web_verified","medium"),
    flags=["stage_uncited","cite_pending","stale"],
    note="Grammarly (renamed Superhuman in 2025 after buying Superhuman Labs), AI writing assistant, San Francisco. IVP joined the $110M round of May 2017 led by General Catalyst with Spark, the company's first outside capital, Growth by scale (as Spark reads it). Last priced mark $13B (November 2021); stale.")
row("groundtruth", status="private", parts=[country("US"), city("New York"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="GroundTruth (formerly xAd), location-based advertising, New York. IVP's page: Partnered 2014, the $50M round IVP led in xAd that year. The xad row is the same company under its old name (merge recorded, applies at the rebuild).")
row("group-nine-media", status="acquired", parts=[city("New York"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Group Nine Media (Thrillist, NowThis, The Dodo, Seeker), New York. Acquired by Vox Media in 2022. IVP's page: Partnered 2011, which predates the 2016 combination, so IVP's position came through a predecessor (Thrillist); the round is not named in our sources.")
row("h1", status="private", parts=[city("New York"), stage("Growth","web_verified",post("hi-connecting-life-sciences"))], valuation_range="below_1b",
    funding_rounds=[rnd("2020-12","Series B",58000000,"IVP and Menlo Ventures",True,post("hi-connecting-life-sciences"))],
    note="H1, healthcare data platform, New York. IVP co-led the $58M Series B with Menlo Ventures (IVP post 2020-12-17), its entry. No priced mark at or above $1B.")
write("../queue/batch-002a.out.jsonl", L)
