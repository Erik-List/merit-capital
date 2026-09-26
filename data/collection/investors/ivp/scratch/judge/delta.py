from jl import *
L=[]; V=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
def v(slug, verdict, cls, conf, basis, cite=None):
    d={"slug":slug,"verdict":verdict,"evidence_class":cls,"confidence":conf,"who":"agent","basis":basis}
    if cite: d["citation"]=cite
    V.append(d)
NF="https://www.sec.gov/Archives/edgar/data/1065280/000101287002001044/ds1.txt"
row("accompany-health", parts=[city("Bethesda","web_verified","medium")], note="City: Bethesda MD (company profile; teams distributed).")
row("brex", status="acquired", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Brex, corporate cards and spend management, San Francisco. Capital One completed its acquisition of Brex on 2026-04-07 (announced 2026-01-22; about $2.56B in cash plus stock): https://www.capitalone.com/about/newsroom/capital-one-completes-acquisition-of-brex/ , as Y Combinator carries. IVP's page: Partnered 2018, the $125M Series C of October 2018.")
row("curology", parts=[stage("undetermined","model",None,"low")], note="IVP's page: Partnered 2019; the round IVP joined is not named in our sources.")
row("netflix", parts=[stage("Growth","web_verified",NF,"medium")],
    funding_rounds=[rnd("1998-06","board seat (Timothy Haley, IVP managing director)",None,None,True,NF,"filing"),
                    rnd("1999-02","Series C",None,None,True,NF,"filing")],
    note="Entry from Netflix's 2002 S-1: Timothy Haley, 'a Managing Director of Institutional Venture Partners ... since February 1998', has been a director since June 1998, and the Series C of February 1999 carried a letter agreement with Technology Crossover Ventures, Institutional Venture Partners and Foundation Capital; IVP VIII held 14.5% before the IPO. Either round (the 1998 financing or the Series C) is Growth.")
row("sublime-security", parts=[city("Washington","web_verified","medium")], note="City: Washington DC (company profiles; founders ex-DoD).")
row("connectandsell", parts=[city("Los Gatos","web_verified","medium")], note="City: Los Gatos CA (company profiles).")
row("cowboy-space-corporation", parts=[city("San Carlos","web_verified","high"), stage("Growth","web_verified","https://www.businesswire.com/news/home/20260508036993/en/Cowboy-Space-Corporation-Raises-$275M-Series-B-For-Vertically-Integrated-Orbital-Data-Centers-and-Rockets")],
    **value(2000000000,"https://www.businesswire.com/news/home/20260508036993/en/Cowboy-Space-Corporation-Raises-$275M-Series-B-For-Vertically-Integrated-Orbital-Data-Centers-and-Rockets","2026-05","1b_plus"),
    clear_flags=["needs_web_value"],
    funding_rounds=[rnd("2026-05","Series B",275000000,"Index Ventures",True,"https://www.businesswire.com/news/home/20260508036993/en/Cowboy-Space-Corporation-Raises-$275M-Series-B-For-Vertically-Integrated-Orbital-Data-Centers-and-Rockets","company")],
    note="Cowboy Space Corporation (formerly Aetherflux, renamed May 2026), orbital data centers, San Carlos CA. IVP joined the $275M Series B (Index led) at a $2B valuation (company release 2026-05-08). a16z's row predates the round (raised for the wave alignment).")
row("genlogs", parts=[city("Arlington","model_knowledge","medium")], note="City: Arlington VA, as Battery carries.")
row("solace-health", parts=[city("Austin","web_verified","high")],
    **value(1000000000,"https://hlth.com/insights/news/solace-health-raises-130m-in-series-c-led-by-ivp-surpasses-1b-valuation-2026-02-11","2026-02","1b_plus","web_verified","medium"),
    note="Solace Health, Austin TX. The IVP-led $130M Series C (February 2026) valued Solace at over $1 billion (HLTH, Fierce Healthcare); recorded at the $1B floor the reports give.")
row("venice", parts=[country("IL"), city("Tel Aviv","web_verified","medium")], note="Venice (formerly Valkyrie), Israeli company with offices in Tel Aviv and New York; the $25M Series A inside the $33M total was led by IVP (CTech, Index Ventures).")
# ---- recall additions
v("santera-systems","member","fund_filing","high","Institutional Venture Partners VIII, L.P. signs as a Santera stockholder in the agreements Tekelec filed with its 8-K of 2003-05-07 when it bought Santera (recall addition from the exit-side full-text sweep).","https://www.sec.gov/Archives/edgar/data/790705/000095014803001184/v89867exv10w4.txt")
v("mtone-wireless","member","fund_filing","high","mTone Wireless (GWcom)'s 2004 S-1 lists entities affiliated with Institutional Venture Partners VI as a 9.09% holder, and IVP VI signs its investors' rights agreement.","https://www.sec.gov/Archives/edgar/data/1276118/000119312504064659/ds1.htm")
v("applied-medical","member","fund_filing","high","Applied Medical's 2011 S-1: Institutional Venture Partners IV, L.P. holds Class A stock with demand registration rights (a venture-round position) and is compelling the registration.","https://www.sec.gov/Archives/edgar/data/1534727/000119312511311445/d253118ds1.htm")
v("hearme","member","web","medium","HearMe (Mpath Interactive)'s 2001 10-K405 names Ruthann Quindlen, 'General Partner, Institutional Venture Partners', a director since 1995, and CEO Paul Matteucci as a Resident Entrepreneur at IVP just before founding it: incubated at IVP with IVP's board seat from its first round.","https://www.sec.gov/Archives/edgar/data/1078693/000091205701505915/a2041405z10-k405.htm")
v("wellfleet-communications","member","web","medium","Geoff Yang's bio on Redpoint's own site: as a general partner with IVP he was responsible for 'the firm's investments in ... Wellfleet' (IVP-era, before Redpoint existed; decisions.md D4).","https://web.archive.org/web/20040601000000id_/http://www.redpoint.com/?action=view&oid=234")
row("santera-systems", status="acquired", parts=[country("US"), city("Plano","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Santera Systems, softswitch telecom equipment, Plano TX. Acquired by Tekelec in 2003. IVP VIII held the position (Tekelec 8-K); the round is not named.")
row("mtone-wireless", status="unknown", parts=[country("US"), city("Santa Clara","model_knowledge","low"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="mTone Wireless (GWcom), mobile data services in Asia, Santa Clara CA. Filed an S-1 in 2004 and withdrew it; later fate not established. IVP VI held 9.09%; the round is not named.")
row("applied-medical", status="private", parts=[country("US"), city("Rancho Santa Margarita"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Applied Medical, surgical devices, Rancho Santa Margarita CA. Still private (the 2011 IPO the IVP IV demand forced was withdrawn). IVP IV's round (1990s) is not named in our sources.")
row("hearme", status="defunct", parts=[country("US"), city("Mountain View","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="HearMe (Mpath Interactive), internet voice and games, Mountain View CA. IPO 1999; wound down and liquidated in 2001, as Accel carries. IVP's first-round position; the round word is not given.")
row("wellfleet-communications", status="acquired", parts=[country("US"), city("Billerica","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Wellfleet Communications, routers, Billerica MA. IPO 1991; merged with SynOptics in 1994 to form Bay Networks. Geoff Yang's IVP-era investment; the round is not named.")
write("../queue/batch-001.out.jsonl", L+V)
