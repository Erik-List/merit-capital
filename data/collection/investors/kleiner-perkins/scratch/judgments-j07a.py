"""PRO-99 Kleiner Perkins, judge j07, batch 13. Run: NQ_TAG=j07 python3 judgments-j07a.py"""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, W, ARCH, SITE, POST

L = []
A = L.append
U = "Graduation left for the graduation pass."


def post_exact(slug):
    m = [p["url"] for p in jl._POSTS if p.get("slug") == slug]
    if len(m) != 1:
        raise SystemExit(f"post_exact({slug!r}) matched {len(m)}")
    return m[0]


# consider (consider.co, a talent-network platform for venture firms' portfolios)
A(cls("consider", status="private", rng="below_1b", stage="undetermined", rounds=[],
      country="US", flags=["city_unknown"], focus="SaaS",
      note="Consider (consider.co, the firm's 2020 enterprise tile link) runs job boards and talent networks for venture "
           "firms; its site was live on 2026-09-30. No round naming Kleiner Perkins was found, and no source placed its "
           "headquarters."))

# cooliris
A(cls("cooliris", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="San Francisco", focus="Consumer & Marketplaces",
      note="Cooliris was acquired by Yahoo on 2014-11-21 (Wikipedia, which lists Kleiner Perkins among its backers). "
           "The archived page ties it to the iFund; the round the firm first entered is not on record."))

# coronet
A(cls("coronet", status="acquired", rng="below_1b", stage="undetermined", rounds=[], entry_date="1994",
      country="US", flags=["city_unknown"], focus="Data Infrastructure",
      note="CoroNet (network management software) was acquired by Compuware per the firm's own exit field; the firm's "
           "since-year is 1994 and no round is named. No source placed its headquarters."))

# cosine-communications (aligned with TCV's row)
A(cls("cosine-communications", status="defunct", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Redwood City", focus="Data Infrastructure",
      note="CoSine Communications (IPO 2000) wound down its operations in the mid-2000s and remained a shell; defunct "
           "and Redwood City as in TCV's row. No round naming Kleiner Perkins is on record."))

# credit-ease (KPCB China; R5: CreditEase is the row, not its listed subsidiary Yirendai)
A(cls("credit-ease", status="private", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite="https://www.creditease.cn/", city="Beijing",
      focus="Fintech & Payments", flags=["kpcb_china"],
      note="CreditEase (Tina Ju, KPCB China) is a Beijing lending and wealth platform whose own site names its Beijing "
           "entity; the member is CreditEase itself, not its listed subsidiary Yirendai (decisions.md R5). No priced round "
           "with a published valuation was found, so below_1b under Rule A; the round KPCB China entered is not on record."))

# crittercism (Apteligent)
A(cls("crittercism", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      city="San Francisco", focus="DevTools & APIs",
      note="Crittercism renamed itself Apteligent and was acquired by VMware (announced 2017-05-15, Wikipedia). The "
           "archived page ties it to the iFund (Ellen Pao); the round the firm first entered is not on record here."))

# crystal (Crystal Semiconductor)
A(cls("crystal", status="acquired", rng="below_1b", stage="undetermined", rounds=[], entry_date="1986",
      country="US", city="Austin", focus="Industrial & Robotics",
      note="Crystal Semiconductor (Austin) was acquired by Cirrus Logic in a stock swap completed in late October 1991 "
           "(Wikipedia). The firm's since-year is 1986; no round is named."))

# crystal-dynamics: seed capital from Technology Partners and KPCB; King World bought 10% for $7.5M in 1993
cd = W("Crystal Dynamics")
A(cls("crystal-dynamics", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=cd, stage_conf="medium",
      entry_date="1992", grad="graduated", grad_src="web_verified", grad_cite=cd, grad_conf="medium",
      city="San Carlos", focus="Media, Gaming & Advertising",
      rounds=[rnd("1992", "Seed", None, None, True, cd, "press"),
              rnd("1993-07", "equity purchase (HBO, 10%)", None, "Home Box Office", None, cd, "press"),
              rnd("1993-09", "equity purchase (King World, 10%)", 7500000, "King World", None, cd, "press")],
      note="Wikipedia: Technology Partners and Kleiner Perkins provided Crystal Dynamics with seed capital (1992, the "
           "firm's since-year). King World then bought 10% for $7.5M in September 1993, an unnamed later priced round "
           "above the $5M step for an entry to 2014, so the seed graduated. Acquired by Eidos in 1998; based in San "
           "Carlos per Wikipedia."))

# csg-systems
A(cls("csg-systems", status="acquired", rng="below_1b", stage="undetermined", rounds=[
          rnd("1994", "acquisition of Cable Services Group by CSG Holdings (Morgan Stanley, Trident)", 137000000,
              "Morgan Stanley", None, W("CSG Systems International"), "press")],
      entry_date="1994", country="US", city="Englewood", focus="SaaS",
      note="CSG Systems (IPO 1996) was acquired by NEC, announced October 2025 and completed May 2026 (Wikipedia). The "
           "firm's since-year 1994 is the year CSG Holdings bought the business from First Data; the record does not "
           "name the firm's round, so the stage is undetermined."))

# cuspai: KP co-led the $450M Series B at $2.6B (2026-07-20)
cu = "https://pulse2.com/cuspai-raises-450-million-series-b-at-2-6-billion-valuation-to-discover-new-materials/"
A(cls("cuspai", status="private", rng="1b_plus", usd=2600000000, val_src="web_verified", val_cite=cu,
      asof="2026-07-20", stage="Growth", stage_src="web_verified", stage_cite=cu, stage_conf="high",
      entry_date="2026-07-20", country="GB", country_src="web_verified", country_cite=cu, city="Cambridge",
      focus="AI & Applied AI", extra={"valuation_range_source": "web_verified"},
      rounds=[rnd("2026-07-20", "Series B", 450000000, "Kleiner Perkins, New Enterprise Associates", True, cu, "press")],
      note="Kleiner Perkins co-led CuspAI's $450M Series B at $2.6B with NEA (Pulse 2.0, 2026-07-20; the firm's own "
           "post of the same day says it co-led the Series B); the site's since-year is 2026, so the B is the entry. "
           "Cambridge, UK. Momentum check 2026-09-30: this round is the $1B+ priced round."))

# cyoptics
A(cls("cyoptics", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Breinigsville", focus="Industrial & Robotics",
      note="CyOptics (InP optical chips, Breinigsville PA) was acquired by Avago Technologies in 2013. Vinod Khosla is "
           "the partner on the archived page, a pre-2004 Kleiner Perkins seat; no round is named."))

# cypress-semiconductor: status disputed (the prefill read defunct; Infineon closed the acquisition 2020-04-17)
A(cls("cypress-semiconductor", status="acquired", rng="below_1b", stage="undetermined", rounds=[
          rnd("1982", "formation financing", None, None, True, W("Cypress Semiconductor"), "press")],
      entry_date="1982", city="San Jose", focus="Industrial & Robotics", flags=["model_disputes_source"],
      note="Status disputed: Infineon completed its acquisition of Cypress on 2020-04-17 (Wikipedia), so acquired, not "
           "defunct. Cypress was formed in 1982 with backing from Sevin Rosen, Kleiner Perkins, Mayfield and Sequoia; the "
           "round is not named."))

# danoo
A(cls("danoo", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="US", flags=["city_unknown"], focus="Media, Gaming & Advertising",
      note="Danoo (place-based digital media screens) appears on the firm's 2008-09 list only and left it by 2010; a "
           "Google News search for the name returned nothing about the company, so its fate and city are not established."))

# dash-navigation
A(cls("dash-navigation", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Mountain View", focus="Consumer & Marketplaces",
      note="Dash Navigation was acquired by Research In Motion (announced June 2009). Mountain View per Wikipedia and the "
           "firm's own 2008-10 listing; Sequoia's row reads Sunnyvale from model knowledge. The firm's entry round "
           "(Matt Murphy) is not on record."))

# datou (KPCB China)
A(cls("datou", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("datou"), city="Beijing",
      focus="Media, Gaming & Advertising", flags=["kpcb_china"],
      note="Datou, a Beijing mobile multimedia software company on the KPCB China list (Beijing per the firm's own "
           "2009-10 China listing); its later fate is not established and no round is named."))

# deosen (KPCB China)
A(cls("deosen", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("deosen"), flags=["kpcb_china", "city_unknown"],
      focus="Industrial & Robotics",
      note="Deosen, a xanthan gum manufacturer on the KPCB China list, located only as 'Shandong, China' (a province) by "
           "the firm's 2009-10 listing; the city and its current state are not established, and no round is named."))

# destineer: status disputed (the prefill's 'defunct' joins the unrelated Minnesota game publisher)
A(cls("destineer", status="acquired", rng="below_1b", stage="undetermined", rounds=[], entry_date="1992",
      flags=["city_unknown", "model_disputes_source"], focus="Data Infrastructure",
      note="Status disputed: the firm's own record gives Destineer (1992, networking for telecom carriers) as acquired "
           "by MCI WorldCom; the prefilled defunct matches the unrelated video game publisher of the same name. No source "
           "placed its headquarters and no round is named."))

# devicescape: two rows for one company (Instant802 Networks renamed Devicescape in 2005)
for s in ("devicescape-formerly-instant-802-networks-inc", "devicescape-software-inc"):
    A(cls(s, status="acquired", rng="below_1b", stage="undetermined", rounds=[],
          country="US", city="San Francisco", focus="Data Infrastructure",
          note="Devicescape (founded 2001 in San Francisco as Instant802 Networks, renamed 2005) was acquired by "
               "Pareteum on 2019-05-08 (Wikipedia). The two base rows devicescape-formerly-instant-802-networks-inc and "
               "devicescape-software-inc are one company. The firm's round (Doug Mackenzie) is not on record."))

# dhgate (KPCB China)
A(cls("dhgate", status="private", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=W("DHgate"), city="Beijing",
      focus="Consumer & Marketplaces", flags=["kpcb_china"],
      note="DHgate, a Beijing cross-border B2B marketplace (Wikipedia), held by KPCB China (Tina Ju, Xin Tang). No priced "
           "round with a published valuation was found, so below_1b under Rule A; KPCB China's round is not on record."))

# diamond-lane
A(cls("diamond-lane", status="acquired", rng="below_1b", stage="undetermined", rounds=[], entry_date="1995",
      country="US", city="Petaluma", focus="Data Infrastructure",
      note="Diamond Lane Communications (DSL equipment, Petaluma) was acquired by Nokia per the firm's own exit field; "
           "since-year 1995, no round named."))

# dichanphone (KPCB China)
A(cls("dichanphone", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("dichanphone"), flags=["kpcb_china", "city_unknown"],
      focus="Consumer & Marketplaces",
      note="Dichanphone (pre-installed real estate phone apps) appears on the firm's 2012-17 pages under Team China "
           "(Xin Tang); no source gives its city, fate or round."))

# digital-chocolate (aligned with Sequoia and Sutter Hill)
A(cls("digital-chocolate", rng="below_1b", stage="undetermined", rounds=[], city="San Mateo",
      focus="Media, Gaming & Advertising",
      note="Digital Chocolate (Trip Hawkins, 2003, San Mateo) sold its games to RockYou and shut its site (Wikipedia); "
           "the firm's round (Russell Siegelman) is not on record."))

# discovery-loop
bi = "https://www.investing.com/news/company-news/ai-startup-discovery-loop-seeks-funding-at-50bn-valuation--business-insider-4898595"
A(cls("discovery-loop", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="medium",
      entry_date="2026", grad="censored", flags=["needs_web_value", "city_unknown"], focus="AI & Applied AI",
      rounds=[rnd("2026-08", "initial round (reported as a seed)", None, "Radical Ventures, Khosla Ventures", True, bi, "press")],
      note="Kleiner Perkins joined Discovery Loop's initial round, led by Radical Ventures and Khosla Ventures (Business "
           "Insider via Investing.com, 2026-09-11); reports call it a seed, and the firm lists it Early 2026. Momentum "
           "check 2026-09-30: the $10B figure was reported as talks and a new round seeks about $50B, neither a closed "
           "priced round, so below_1b with needs_web_value. Censored: entered 2026."))

# djz (aligned with GV)
A(cls("djz", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="US", flags=["city_unknown"], focus="Media, Gaming & Advertising",
      note="DJZ (electronic dance music media, Mike Abbott, 2014); status unknown as in GV's row, city not established, "
           "no round naming Kleiner Perkins found."))

# dmx-technologies (KPCB China; SGX-listed, KDDI subsidiary from 2009)
kd = "https://www.kddi.com/english/corporate/news_release/2009/0910/"
A(cls("dmx-technologies", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="HK", country_src="web_verified", country_cite=kd, city="Hong Kong",
      focus="Data Infrastructure", flags=["kpcb_china"],
      note="DMX Technologies Group, an SGX Main Board company headquartered in Hong Kong, became a consolidated KDDI "
           "subsidiary when KDDI subscribed new shares for 52.56% (KDDI release 2009-09-10). The KPCB China position "
           "was likely taken after the SGX listing (a T3 question raised in the report); no round is named."))

# dollar-shave-club: seed March 2012 incl. KPCB; Series A October 2012 by the same group plus Venrock
ds = W("Dollar Shave Club")
A(cls("dollar-shave-club", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=ds, stage_conf="high",
      entry_date="2012-03", grad="graduated", grad_src="web_verified", grad_cite=ds, grad_conf="high",
      city="Durham", focus="Consumer & Marketplaces",
      rounds=[rnd("2012-03", "Seed", 1000000, None, True, ds, "press"),
              rnd("2012-10", "Series A", 9800000, "Venrock", True, ds, "press"),
              rnd("2013", "Series B", 12000000, "Venrock", None, ds, "press")],
      note="Seed investors including Kleiner Perkins put in $1M in March 2012 and the same group with Venrock the $9.8M "
           "Series A in October 2012 (Wikipedia), so the seed graduated. Acquired by Unilever in 2016. City Durham: "
           "the company opened its new headquarters there in September 2025 (Wikipedia), fresher than the siblings' Los Angeles."))

# doodle-mobile (KPCB China with the iFund's Matt Murphy)
A(cls("doodle-mobile", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("doodle-mobile"), city="Beijing",
      focus="Media, Gaming & Advertising", flags=["kpcb_china"],
      note="Doodle Mobile, a Chinese mobile game developer on the firm's 2013-17 pages under Teams China and Digital "
           "(Wei Zhou, Matt Murphy); Beijing from model knowledge. Its fate and the round are not established."))

# easic
A(cls("easic", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Santa Clara", focus="Industrial & Robotics",
      note="eASIC (founded 1999, Santa Clara) was acquired by Intel in 2018 (Wikipedia). Its 2014 draft S-1 lists KPCB "
           "Holdings among holders exchanging into Series A-2 stock in a recapitalisation; the firm's first round (Vinod "
           "Khosla's KP-era seat) is not named."))

# echelon
A(cls("echelon", rng="below_1b", stage="undetermined", rounds=[], country="US", city="Santa Clara",
      focus="Climate & Energy",
      note="Echelon (founded 1988, IPO 1998) was acquired by Adesto Technologies on 2018-09-14 and was based in Santa "
           "Clara (Wikipedia). The firm's round is not on record."))

# edeniq
A(cls("edeniq", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Visalia", focus="Climate & Energy",
      note="EdeniQ (biofuel process technology, Visalia CA; John Denniston) is on the firm's 2013-18 pages; its current "
           "state is not established and no round is named."))

# effx
A(cls("effx", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="San Francisco", focus="DevTools & APIs",
      note="effx (microservices catalog, 2018-2021) announced on its own site that 'effx is joining the team at Figma' "
           "(read 2026-09-30), and the firm lists it among alumni; Kleiner Perkins' Bucky Moore was an early investor and "
           "EIR, but the round is not named."))

# elance (aligned with NEA)
A(cls("elance", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Mountain View", focus="Consumer & Marketplaces",
      note="Elance merged with oDesk in 2013 to form Elance-oDesk, now Upwork (Wikipedia); acquired and Mountain View as "
           "in NEA's row. The firm's round is not on record."))

# elcomax
A(cls("elcomax", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      flags=["city_unknown"], focus="Climate & Energy",
      note="elcomax (fuel cell combined heat and power, partners Brook Porter and Jan van Dokkum, 2013-18 pages); its "
           "domain elcomax.de no longer resolves and its fate and city are not established; no round named."))

# element-analytics
A(cls("element-analytics", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="US", flags=["city_unknown"], focus="Data Infrastructure",
      note="Element Analytics (industrial data operations) is on the firm's 2017-18 pages with no detail; its round, "
           "current state and city are not established here."))

# emdeon-corporation (the renamed Healtheon/WebMD parent)
A(cls("emdeon-corporation", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Elmwood Park", focus="Healthcare & Bio",
      note="Emdeon Corporation is the 2005 name of Healtheon/WebMD (the firm's 1996 Healtheon investment), renamed HLTH in "
           "2007 and merged into WebMD Health Corp in 2009, itself bought by Internet Brands in 2017; the same company as "
           "the base rows healtheon and webmd-corp-new."))

# endforce
A(cls("endforce", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Columbus", focus="Security",
      note="ENDFORCE, an Ohio network access control company, was acquired by Sophos in 2007 (Wikipedia, Sophos article); "
           "the firm's tile links to sophos.com. No round named."))

# enet (KPCB China; aligned with Redpoint)
A(cls("enet", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("enet"), city="Beijing",
      focus="Media, Gaming & Advertising", flags=["kpcb_china"],
      note="eNet, a Beijing IT-industry portal on the firm's 2009-10 China listing; status unknown as in Redpoint's row, "
           "no round named."))

# engram: KP led the Series A as it emerged with $98M raised; $98M at a $600M valuation
pr = jl.NEWS("engram", "Engram Launches with $98M")
A(cls("engram", status="private", rng="below_1b",
      stage="Series A", stage_src="first_party", stage_cite=POST("engram-giving"), stage_conf="high",
      entry_date="2026-06", country="US", city="San Francisco", city_src="web_verified", focus="AI & Applied AI",
      extra={"valuation_range_source": "web_verified", "valuation_citation": pr, "valuation_asof": "2026-06-23"},
      rounds=[rnd("2026-06-23", "Seed and Series A ($98M total)", 98000000,
                  "General Catalyst, Kleiner Perkins, Sequoia Capital, Factory, Modern, Amplify Partners", True, pr, "company"),
              rnd("2026-06-23", "Series A", None, "Kleiner Perkins", True, POST("engram-giving"), "firm")],
      note="The firm's own post says it led Engram's Series A as the company emerged with $98M across seed and Series A "
           "(company release, San Francisco, 2026-06-23); Sequoia's row holds the earlier seed. Momentum check 2026-09-30: "
           "Calcalist headlines the $98M at a $600M valuation and Google News shows no later round, so below_1b."))

# enlighted
A(cls("enlighted", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Sunnyvale", focus="Climate & Energy",
      note="Enlighted (smart building sensors and controls, Sunnyvale; Trae Vassallo) was acquired by Siemens in 2022; "
           "the firm's round is not on record."))

# eo-computer
A(cls("eo-computer", status="defunct", rng="below_1b", stage="undetermined", rounds=[], entry_date="1991",
      country="US", flags=["city_unknown"], focus="Consumer & Marketplaces",
      note="Eo, Inc., 52 percent owned by AT&T, shut down operations on 1994-07-29 (Wikipedia, EO Personal "
           "Communicator); the site's 'acquired by AT&T' reflects the 1993 majority stake, but the business ended, so "
           "defunct. Since-year 1991, no round named."))

# erecyclingcorps (renamed HYLA Mobile, acquired by Assurant)
A(cls("erecyclingcorps", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Irving", focus="Consumer & Marketplaces",
      note="eRecyclingCorps (device trade-in and resale, Green Growth Fund) renamed itself HYLA Mobile and was acquired by "
           "Assurant in 2020 (model knowledge). The Green Growth Fund round is not cited here."))

# erly
A(cls("erly", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", flags=["city_unknown"], focus="Consumer & Marketplaces",
      note="Erly (a social collections app, sFund, Chi-Hua Chien) shows as Acquired on the firm's 2013-14 pages; the "
           "acquirer, city and the round are not established."))

# esionic
A(cls("esionic", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="US", flags=["city_unknown"], focus="Climate & Energy",
      note="eSionic (molecular systems for energy storage, Mark Allen) is on the firm's 2012-14 pages only; its fate, "
           "city and round are not established."))

jl.write("j07a", L)
