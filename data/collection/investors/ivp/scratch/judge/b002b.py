from jl import *
CC="https://index.commoncrawl.org/"
L=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
row("harness", parts=[city("San Francisco"), stage("Growth","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Harness, software delivery platform, San Francisco (Jyoti Bansal, whom IVP backed at AppDynamics). IVP's post (2019-04-23) announces its initial investment, the $60M Series B IVP led in April 2019, without naming the round; to be cited in the A/B pass. Harness bought Traceable in 2025.")
row("hashicorp", parts=[city("San Francisco"), stage("Growth","web_verified",post("hashicorp-provisioning-the-future-of-the-cloud"))], valuation_range="below_1b",
    funding_rounds=[rnd("2018-11","Series D",100000000,"IVP",True,post("hashicorp-provisioning-the-future-of-the-cloud"))],
    note="HashiCorp, cloud infrastructure automation, San Francisco. IVP led the $100M Series D (IVP post 2018-11-01), its entry. IPO 2021 (HCP); acquired by IBM in February 2025, so no standalone mark.")
row("hello-heart", status="private", parts=[city("Menlo Park")], valuation_range="below_1b",
    note="Hello Heart, heart-health digital therapeutics, Menlo Park CA (the firm's own Location). IVP entered in 2021 (post 2021-05-26); no mark at or above $1B.")
row("hims-hers", parts=[country("US"), city("San Francisco"), stage("Series A","model",None,"medium")], flags=["stage_uncited","cite_pending"],
    note="Hims & Hers, telehealth, San Francisco (NYSE: HIMS). IVP's post (2021-01-21): 'IVP first invested in Hims in January 2018, less than three months after its public launch, and then led a $50 million Series B in June of 2018', so the entry precedes the B: the January 2018 Series A. The post names only the B, hence uncited.")
row("hipmunk", status="acquired", parts=[city("San Francisco"), stage("Growth","web_verified",CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/travel-innovator-hipmunk-raises--15m-from-ivp-and-existing-investors&output=json","medium")], valuation_range="below_1b",
    flags=["stage_disputes_band"],
    funding_rounds=[rnd("2012","Series B",15000000,"IVP",True,CC+"CC-MAIN-2013-20-index?url=http://www.ivp.com/news/press-release/travel-innovator-hipmunk-raises--15m-from-ivp-and-existing-investors&output=json")],
    note="Hipmunk, travel search, San Francisco. IVP's archived release: 'Travel Innovator Hipmunk Raises $15M from IVP and Existing Investors' (2012, the firm's Year Invested), the company's Series B after a $4.2M A; the band read Todd Chaffee's 2014 filing as a Series A entry. Acquired by Concur (SAP) in 2016.")
row("homeaway", parts=[city("Austin"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_disputes_band","stage_uncited"],
    note="HomeAway, vacation rentals, Austin TX. IVP's page: Partnered 2006, the $160M round of November 2006 that IVP led (the company's second institutional round), not the 2010 filing the band anchored on. IPO 2011 (AWAY), acquired by Expedia in 2015.")
row("humu", status="acquired", parts=[city("Mountain View")], valuation_range="below_1b",
    note="Humu, workplace nudge software, Mountain View CA. Acquired by Perceptyx in 2023.")
row("iex", status="private", parts=[country("US"), city("New York"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="IEX Group, stock exchange operator, New York. IVP's page: Partnered 2016; which of IEX's rounds IVP joined is not named in our sources. Private, no mark at or above $1B.")
row("indiegogo", status="acquired", parts=[country("US"), city("San Francisco"), stage("Growth","web_verified",post("ivp-adds-crowdfunding-leader-indiegogo-to-its-portfolio"))], valuation_range="below_1b",
    funding_rounds=[rnd("2014-01","Series B",40000000,"IVP",True,post("ivp-adds-crowdfunding-leader-indiegogo-to-its-portfolio"))],
    note="Indiegogo, crowdfunding, San Francisco. IVP led the $40M Series B with Kleiner Perkins (IVP post 2014-01-28). Acquired by Gamefound in January 2025, so acquired although the firm's page reads Active.")
row("inspirato", parts=[city("Denver"), stage("Growth","web_verified",post("inspirato-reimagining-luxury-travel"))], flags=["stage_disputes_band"],
    funding_rounds=[rnd("2012-01","Series B",None,"IVP",True,post("inspirato-reimagining-luxury-travel"))],
    note="Inspirato, luxury travel club, Denver. IVP's post: 'we led Inspirato's Series B and joined the Board in January 2012', the entry; the band read Todd Chaffee's 2012 filing as a Series A.")
row("jasper", status="private", parts=[country("US"), city("Austin"), stage("Series A","web_verified",post("jasper-this-blog-post-mostly-wrote-itself"))], flags=["needs_web_value","identity_homonym"],
    funding_rounds=[rnd("2022-10","Series A",125000000,"Insight Partners",True,post("jasper-this-blog-post-mostly-wrote-itself"))],
    note="Jasper (jasper.ai), AI marketing content, Austin TX. IVP participated in the $125M Series A (IVP post 2022-10-18), priced near $1.5B; the web pass pins the mark or rules it down. Not Jasper Technologies, the IoT company Cisco bought in 2016 (Sequoia's row): a homonym.")
row("keeptruckin", parts=[city("San Francisco")], flags=["identity_conflated"],
    note="KeepTruckin, fleet telematics, San Francisco: the company renamed itself Motive in 2022, and the motive row is the same company (merge recorded in identity-merges.json, applies at the rebuild).")
row("kittl", status="private", parts=[city("Berlin"), stage("Growth","web_verified",post("kittl-empowering-creativity"))], valuation_range="below_1b",
    funding_rounds=[rnd("2024-01","Series B",36000000,"IVP",True,post("kittl-empowering-creativity"))],
    note="Kittl, design platform, Berlin. IVP led the $36M Series B (IVP post 2024-01-23).")
row("klarna", status="public", parts=[city("Stockholm"), stage("Growth","model",None,"medium")],
    **value(7520000000,"https://companiesmarketcap.com/klarna/marketcap/","2026-08","1b_plus"),
    flags=["stage_uncited","cite_pending"],
    note="Klarna, payments and BNPL, Stockholm (NYSE: KLAR since September 2025). IVP's page: Partnered 2014, a growth-stage position in a company then already at scale; the round is to be cited in the A/B pass. Cap as Sequoia and Creandum carry.")
row("laurel", status="private", parts=[country("US"), city("San Francisco","model_knowledge","medium"), stage("Growth","web_verified",post("laurel-returning-time-to-the-world"))], valuation_range="below_1b",
    flags=["model_disputes_source"],
    funding_rounds=[rnd("2025-06","Series C",100000000,"IVP",True,post("laurel-returning-time-to-the-world"))],
    note="Laurel (laurel.ai), AI timekeeping for professional services, San Francisco. IVP leads the Series C (IVP post 2025-06-10; $100M per press). The Wikidata JP is a namesake's.")
row("legalzoom", parts=[city("Glendale"), stage("Growth","web_verified",post("legalzoom-democratizing-law-through-innovation-and-perserverance"),"medium")],
    funding_rounds=[rnd("2011","secondary",None,None,True,post("legalzoom-democratizing-law-through-innovation-and-perserverance"))],
    note="LegalZoom, online legal services, Glendale CA (NASDAQ: LZ). IVP's post: 'IVP invested in LegalZoom in 2011', and 'the vast majority of the incremental investment in LegalZoom came in the form of secondary shares' bought from existing holders: a secondary entry, Growth by policy.")
row("lifelock", parts=[city("Tempe"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="LifeLock, identity-theft protection, Tempe AZ. IVP's page: Year Invested 2012, the year of the October IPO, so a late pre-IPO round; round not named in our sources. Acquired by Symantec in 2017.")
row("lime", status="public", parts=[city("San Francisco"), stage("Growth","model",None,"medium")],
    **value(2750000000,"https://www.stocktitan.net/overview/LIME/","2026-08","1b_plus","web_verified","medium"),
    flags=["stage_uncited","cite_pending"],
    note="Lime (Neutron Holdings), micromobility, San Francisco. IPO 2026 ($LIME on IVP's page). IVP's page: Partnered 2018, the year of Lime's Series C and D; round to be cited and cap refreshed in the A/B pass (a16z's figure carried meanwhile).")
row("looker", status="acquired", parts=[country("US"), city("Santa Cruz"), stage("Growth","model",None,"medium")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Looker, business intelligence, Santa Cruz CA. IVP's page: Partnered 2017, a late round (the $103M Series E of December 2017). Acquired by Google in 2020 for $2.6B.")
row("lulu-s", parts=[country("US"), city("Chico"), stage("Series A","web_verified",post("from-lovelulus-to-lvlu-lulus-goes-public"))], flags=["model_disputes_source"],
    funding_rounds=[rnd("2018-04","Series A",120000000,"IVP",True,post("from-lovelulus-to-lvlu-lulus-goes-public"))],
    note="Lulu's, women's apparel, Chico CA (NASDAQ: LVLU). IVP's post: 'In April 2018, IVP led Lulus' $120 million Series A, the company's first outside fundraising since H.I.G. Growth's majority investment in 2014': the record names it a Series A, and the label follows the record. The Wikidata GB is a namesake's; the float figure ($2.9M) is implausible and the A/B pass pins the cap.")
write("../queue/batch-002b.out.jsonl", L)
