"""PRO-106 grind, batch-001 (aircall .. arive). Evidence: scratch/evidence-pack.json (the live
card, the firm's own posts, the UK officer graph, EDGAR full text, Wikipedia), scratch/siblings.json,
and the web checks named per line. Graduation is judged in its own pass."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
LIST = "https://www.balderton.com/companies/"
NEWS = "https://www.balderton.com/news/"
L = []
def fp(slug, stage, **kw):
    """Stage from the firm's own card (first_party, scored medium: decisions.md D11)."""
    return cls(slug, stage=stage, stage_src="first_party", stage_cite=LIST, stage_conf="medium", **kw)

L.append(cls("aircall", status="private", country="FR", country_src="web_verified", country_cite=LIST, city="Paris",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2016/09/19/aircall-raised-8-million-for-its-cloud-phone-system-for-teams/",
    focus="SaaS", flags=["stage_disputes_band", "model_disputes_source", "needs_web_value"],
    note="Cloud phone system; Balderton led the $8M Series A of Sep 2016 (TechCrunch; the firm's post of 2016-09-15; card 'Series A in 2016'); the Form D band read the 2021 Series D filing as the entry; Paris-founded, the Form D address is the US entity in New York; unicorn mark Jun 2021 pinned in the A/B pass",
    rounds=[rnd("2016-09-19", "Series A", 8000000, "Balderton Capital", True, "https://techcrunch.com/2016/09/19/aircall-raised-8-million-for-its-cloud-phone-system-for-teams/"),
            rnd("2021-06-23", "Series D", 120000000, None, True, NEWS + "aircall-raises-120m-series-d-and-becomes-a-unicorn/", "firm")]))
L.append(cls("azuro", status="acquired", city="Santa Clara", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    flags=["model_disputes_source"],
    note="Chip clock-tree synthesis software (Cambridge UK founders, Santa Clara HQ); listed on the Benchmark Europe desk page from 2004; the entry round is not named on any surface read; acq. by Cadence Design Systems, 2011 (the pre-filled 'defunct' is disputed)"))
L.append(fp("bebo", "Series A", status="acquired", country="US", city="San Francisco", rng="below_1b", focus="Consumer & Marketplaces",
    note="Social network; card 'Series A in 2006' (Benchmark Europe's $15M round, May 2006); acq. by AOL, 2008 ($850M)"))
L.append(fp("betfair", "Growth", status="acquired", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Betting exchange; card 'Series B in 2000' (the desk's position came through Flutter.com, merged into Betfair in 2001-02); LSE IPO 2010; merged with Paddy Power, 2016 (now Flutter Entertainment)"))
L.append(cls("big-fish-games", status="acquired", city="Seattle", stage="Growth", stage_src="model", stage_conf="medium", rng="below_1b",
    focus="Media, Gaming & Advertising",
    note="Casual games; card gives the year 2008 only: the $83.3M round of Sep 2008 (Balderton, General Catalyst, Salmon River), a growth round six years after founding; acq. by Churchill Downs, 2014 ($885M), then Aristocrat, 2018; the card's Cork is the European office"))
L.append(fp("cloud9", "Growth", status="acquired", city="Amsterdam", rng="below_1b", focus="DevTools & APIs",
    note="Cloud IDE; card 'Series B in 2014' (Form D 2014, Chandratillake); acq. by Amazon, 2016"))
L.append(cls("codemasters", city="Southam", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.gamespot.com/articles/vc-firm-buys-out-codemasters/1100-6172485/",
    rng="below_1b", focus="Media, Gaming & Advertising", flags=["stage_disputes_band"],
    note="Games publisher; the desk bought a 40% stake in 2005 (a minority purchase at scale: Growth; the card says 'Series A in 2005'), a further 30% in 2006 and the founders' remainder in 2007 (GameSpot), so the position became a control holding AFTER a minority entry; kept a member on the 2005 entry and raised for Erik (decisions.md R1); later Reliance 50% (2010), AIM IPO 2018, acq. by Electronic Arts, 2021"))
L.append(fp("contentful", "Seed", status="acquired", country="DE", country_src="web_verified", country_cite=LIST, city="Berlin",
    entry_date="2012", rng="below_1b", focus="DevTools & APIs", flags=["stage_disputes_band", "model_disputes_source"],
    note="API-first content platform; card 'Seed in 2012'; the Form D band read the 2021 Series F filing as the entry; Berlin HQ, the Form D address is the US office in Denver; Salesforce agreed to acquire it (the firm's post of 2026-06-02), recorded acquired in the Benchmark and Point Nine books; closing re-checked in the A/B pass"))
L.append(fp("displaylink", "Series A", city="Palo Alto", rng="below_1b", focus="Industrial & Robotics",
    note="USB graphics chips (Newnham Research until 2006); card 'Series A in 2004'; acq. by Synaptics, 2020 ($305M)"))
L.append(cls("frontier-car-group", status="acquired", country="DE", country_src="web_verified", country_cite=LIST, city="Berlin",
    rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Used-car marketplaces in emerging markets; Berlin HQ (the Form D address is counsel's); OLX Group took a $400M controlling position in 2019 (the firm's post of 2019-11-11) and folded it into OLX Autos"))
L.append(cls("hiya", status="private", city="Seattle", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "investment-update-hiya-raises-18m-to-transform-mobile-calling-worldwide/", rng="below_1b", focus="Security",
    note="Caller ID and spam-call protection (Whitepages spin-out); Balderton led the $18M Series A of Oct 2017, its first outside funding; Seattle HQ (the card's London is the European office)",
    rounds=[rnd("2017-10-19", "Series A", 18000000, "Balderton Capital", True, NEWS + "investment-update-hiya-raises-18m-to-transform-mobile-calling-worldwide/", "firm")]))
L.append(fp("icera", "Series A", status="acquired", city="Bristol", rng="below_1b", focus="Industrial & Robotics",
    note="Soft-modem chips; card 'Series A in 2003'; acq. by Nvidia, 2011 ($367M)"))
L.append(fp("lovefilm", "Series A", country="GB", country_src="web_verified", country_cite=LIST, city="London", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="DVD rental and streaming; card 'Series A in 2003' (the desk backed Video Island, merged into Lovefilm in 2006; Coelho director 2006-08); acq. by Amazon, 2011; the Wikidata country DE is wrong"))
L.append(fp("memrise", "Series A", status="private", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["stage_disputes_band"],
    note="Language-learning app; card 'Series A in 2010' (Form D Nov 2012, $5.1M, Evans); the band read the amount as a seed"))
L.append(cls("merama", status="private", country="MX", country_src="web_verified", country_cite=LIST, city="Mexico City",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "merama-secures-160m-as-it-seeks-to-become-the-largest-e-commerce-product-business-in-latin-america/",
    focus="Consumer & Marketplaces", flags=["stage_disputes_band", "model_disputes_source", "needs_web_value"],
    note="Latin American e-commerce brand aggregator; the firm's post of 2021-04-28 announces the $160M Series A (seed and A together); unicorn mark Dec 2021 pinned or killed in the A/B pass; Mexico City HQ, the Form D address is counsel's",
    rounds=[rnd("2021-04-28", "Series A", 160000000, None, True, NEWS + "merama-secures-160m-as-it-seeks-to-become-the-largest-e-commerce-product-business-in-latin-america/", "firm")]))
L.append(cls("mog", status="acquired", city="Berkeley", stage="Growth", stage_src="model", stage_conf="medium", rng="below_1b",
    focus="Media, Gaming & Advertising",
    note="Music streaming; card gives the year 2010 only; the Form D of Feb 2010 ($10M, Mistry) follows two 2009 filings and earlier Menlo and label rounds, so a later round; acq. by Beats Electronics, 2012"))
L.append(cls("mysql", status="acquired", country="SE", city="Uppsala", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2016/05/23/mysql-series-b-round-pitch-deck/", rng="below_1b", focus="Data Infrastructure",
    flags=["stage_disputes_band"],
    note="Open-source database; the card says 'Series A in 2001', but the 2001 Series A came from Scandinavian investors and Benchmark with Index led the Series B of May 2003; acq. by Sun Microsystems, 2008 ($1B); also a member of Benchmark's base (both desks held it)",
    rounds=[rnd("2001", "Series A", 4000000, None, False, "https://en.wikipedia.org/wiki/MySQL_AB"),
            rnd("2003-05", "Series B", 19500000, "Benchmark Capital", True, "https://tech.eu/2016/05/23/mysql-series-b-round-pitch-deck/")]))
L.append({**verdict("nasn", "not_member",
    "North American Sports Network was a joint venture of Benchmark Capital Europe and Setanta Sports, sold by the two to ESPN in Dec 2006 (EUR 70M): the desk and its one partner owned the company outright, a control position (T3, Erik 2026-09-04), not a venture round; raised for Erik (decisions.md R2)",
    ec="web", conf="medium", cite="https://thewaltdisneycompany.com/espn-to-acquire-nasn/"), "exclusion": "control_position"})
L.append(fp("naturalmotion", "Growth", status="acquired", country="GB", city="Oxford", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Animation technology and mobile games; card 'Series B in 2006' (Evans director from 2006-04); acq. by Zynga, 2014 ($527M)"))
L.append(fp("newbay", "Series A", status="acquired", country="IE", city="Dublin", rng="below_1b", focus="SaaS",
    note="White-label content services for mobile operators; card 'Series A in 2003'; acq. by Research In Motion, 2011, then Synchronoss, 2012 (the card's New York is Synchronoss)"))
L.append(fp("openet", "Series A", status="acquired", city="Dublin", rng="below_1b", focus="SaaS",
    note="Telecom charging and policy software; card 'Series A 1999'; acq. by Amdocs, 2020 ($180M)"))
L.append(fp("ory", "Seed", status="private", country="DE", country_src="web_verified", country_cite=LIST, city="Munich", entry_date="2020",
    rng="below_1b", focus="Security", flags=["stage_disputes_band", "model_disputes_source"],
    note="Open-source identity and access platform; card 'Seed in 2020'; the Form D band read the 2021 Series A filing ($20.9M, Hanna) as the entry; Munich HQ, the Form D address is a US agent's"))
L.append(cls("photoroom", status="private", city="Paris", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2022/11/07/after-40-million-app-downloads-photoroom-raises-19-million/", focus="AI & Applied AI",
    note="AI photo editing; Balderton led the $19M Series A of Nov 2022 (TechCrunch; card 'Series A in 2022'); $43M Series B Feb 2024; band set in the momentum check",
    rounds=[rnd("2022-11-07", "Series A", 19000000, "Balderton Capital", True, "https://techcrunch.com/2022/11/07/after-40-million-app-downloads-photoroom-raises-19-million/"),
            rnd("2024-02-27", "Series B", 43000000, None, True, NEWS + "photoroom-secures-43m-in-series-b-funding-launches-next-generation-ai-photo-editing-features-for-businesses/", "firm")]))
L.append(cls("rebtel", status="private", country="SE", city="Stockholm", stage="Series A", stage_src="model", stage_conf="medium", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="International calling for migrant communities; card gives the year 2006 only: the $20M Series A of 2006 (Index Ventures and Benchmark Capital Europe); the card says Exited, the company still operates (2022 press)"))
L.append(cls("sketchfab", city="New York", rng="below_1b", focus="Media, Gaming & Advertising",
    note="3D content platform; Balderton led the $2M round of Dec 2013 (Wikipedia), the seed; the $7M Series A followed in 2015 (the firm's post of 2016-06-16); the card says 'Series A in 2013', the Form D band Seed stands; acq. by Epic Games, 2021"))
L.append(cls("sophia-genetics", status="public", country="CH", country_src="web_verified", country_cite=LIST, city="Rolle",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2017/09/13/balderton-joins-30m-series-d-for-big-data-biotech-platform-play-sophia-genetics/",
    focus="Healthcare & Bio", flags=["model_disputes_source", "needs_web_value"],
    note="Data-driven medicine; Balderton led the $30M round of Sep 2017 (TechCrunch: Series D; card 'Series B in 2017'); Nasdaq IPO Jul 2021 (SOPH), Fund VI files 13Gs; Swiss HQ, the SEC address is the US office; market cap pinned in the A/B pass"))
L.append(fp("sunrise", "Series A", city="New York", rng="below_1b", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
    note="Calendar app; card 'Series A in 2014' (the $6M round, Form D Jul 2014, Liautaud; the 2013 seed of $2.2M came from others); acq. by Microsoft, 2015"))
L.append(cls("supernormal", status="private", city="Stockholm", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "supernormal-raises-10-million-to-transform-worker-productivity-and-transparency-with-ai-generated-meeting-notes/",
    entry_date="2023-01-26", rng="below_1b", focus="AI & Applied AI", flags=["stage_disputes_band"],
    note="AI meeting notes; the firm's post of 2023-01-26 announces the $10M seed Balderton led (card 'Seed in 2023'); the Form D band read the amount as a Series A"))
L.append(cls("talend", city="Redwood City", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2009/01/26/more-validation-for-open-source-software-talend-raises-12-million/", rng="below_1b",
    focus="Data Infrastructure",
    note="Open-source data integration (founded in Suresnes, France); Balderton led the $12M round of Jan 2009 (TechCrunch: Series C; card 'Series D in 2009'); Nasdaq IPO 2016, Fund IV filed 13Gs; acq. by Thoma Bravo, 2021, then Qlik, 2023"))
L.append(fp("thread", "Series A", status="acquired", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Menswear styling service; card 'Series A in 2014' (the firm's post of 2015-08-23: Balderton led the $8M round); administration and sale of the business to Marks & Spencer, Nov 2022 (acquired out of insolvency)"))
L.append(cls("vivino", status="private", city="San Francisco", rng="below_1b",
    note="Wine app and marketplace; Balderton led the $10.3M Series A of Jul 2013 with Creandum (Wikipedia; Creandum's book reads Series A), so the Form D band Series A stands and the card's 'Series C in 2013' is wrong; last round $155M Series D, Feb 2021"))
L.append(cls("yoox-group", status="acquired", country="IT", city="Milan", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online fashion retailer; card gives the year 2000 only and the desk page lists it from 2004; the round the desk entered is not named on any surface read; Milan IPO 2009, merged with Net-a-Porter 2015, acq. by Richemont, 2018"))
L.append(fp("zopa", "Series A", status="private", city="London", focus="Fintech & Payments", flags=["needs_web_value"],
    note="Peer-to-peer lender turned bank; card 'Series A in 2004'; the card says Exited (the firm sold), Zopa Bank remains private; its 2021-23 marks are pinned or killed in the A/B pass"))
L.append(fp("01health", "Seed", status="private", country="GB", city="London", entry_date="2023", rng="below_1b", focus="Healthcare & Bio",
    note="Connects general clinicians with specialists; card 'Seed, 2023'"))
L.append(cls("7digital", status="acquired", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Digital music platform; on the Benchmark Europe desk list from Jan 2006; the entry round is not named on any surface read; reversed into UBC Media (AIM) 2014, acq. by Songtradr, 2023"))
L.append(fp("adludio", "Seed", status="defunct", country="GB", city="London", entry_date="2013", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="Sensory mobile advertising; card 'Seed in 2013' (Bonanzinga director 2013-04, then Chandratillake); the card says Live, Companies House 08227542 shows Adludio Limited in liquidation"))
L.append(cls("agave-games", status="private", country="TR", country_src="web_verified", country_cite=LIST, city="Istanbul",
    stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "agave-games-turkeys-newest-casual-puzzle-game-studio-raises-7m-seed-round/", entry_date="2022-08-11",
    rng="below_1b", focus="Media, Gaming & Advertising",
    note="Casual puzzle games; the firm's post of 2022-08-11 announces the $7M seed Balderton led; $18M Series A Dec 2024",
    rounds=[rnd("2022-08-11", "Seed", 7000000, "Balderton Capital", True, NEWS + "agave-games-turkeys-newest-casual-puzzle-game-studio-raises-7m-seed-round/", "firm"),
            rnd("2024-12-17", "Series A", 18000000, None, True, NEWS + "agave-games-secures-18-million-series-a-to-expand-hit-game-find-the-cat-and-develop-new-titles/", "firm")]))
L.append(cls("almonde", status="acquired", country="FR", city="Paris", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Risk and capital management software for banks; on the Benchmark desk lists 2002-2005; the entry round is not named on any surface read; acq. by Misys, 2006"))
L.append({**verdict("alphyra", "not_member",
    "Benchmark took Alphyra private in the EUR 88.6M management buyout of April 2003 and held 63% of the acquisition vehicle Rendina (Irish Times; Private Equity International 'Benchmark takes Alphyra private'): an acquisition of control, not a venture round (T3, Erik 2026-09-04); raised for Erik (decisions.md R2)",
    ec="web", conf="high", cite="https://www.privateequityinternational.com/benchmark-takes-alphyra-private/"), "exclusion": "control_position"})
L.append(fp("andjaro", "Series A", status="unknown", country="FR", city="Paris", rng="below_1b", focus="SaaS",
    note="Workforce redeployment software; card 'Series A in 2018' (the firm's post of 2018-03-27, EUR 5M); the card says Exited and the event is not on any surface read, so status unknown"))
L.append(fp("anytype", "Seed", status="private", country="DE", city="Berlin", entry_date="2023-08", rng="below_1b", focus="Consumer & Marketplaces",
    note="Local-first, peer-to-peer notes and web builder; card 'Seed 2023' (the firm's post of 2023-08-23, a $13.4M round)"))
L.append(fp("appear-here", "Series A", status="private", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for short-term retail space; card 'Series A in 2014' (the firm's post of 2014-11-26: $7.5M led by Balderton); Series B 2017"))
L.append(cls("arive", status="private", country="DE", city="Munich", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "arive-announces-e6m-seed-round-to-deliver-high-end-consumer-products-to-your-door/", entry_date="2021-09-02",
    rng="below_1b", focus="Consumer & Marketplaces",
    note="On-demand delivery of consumer brands; the firm's post of 2021-09-02 announces the EUR 6M seed; $20M Series A Jan 2022",
    rounds=[rnd("2021-09-02", "Seed", 7100000, None, True, NEWS + "arive-announces-e6m-seed-round-to-deliver-high-end-consumer-products-to-your-door/", "firm"),
            rnd("2022-01-10", "Series A", 20000000, None, True, NEWS + "arive-raises-20m-series-a-to-expand-experience-commerce-across-europe/", "firm")]))
jl.write("batch-001", L)
