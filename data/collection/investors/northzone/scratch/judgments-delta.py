"""PRO-105 delta grind after the rebuild (2026-09-29 ~23:00 UTC): the archive-era rows. Evidence: the firm's
own company pages of 2003 (Internet Archive capture read before the block) and 2010-2025 (Common Crawl
captures; the 2010-12 pages state HQ, co-investors and exits: scratch/archive-facts.json), the firm's
posts (live insights and the archived WordPress index), Google News status checks (scratch/status-bulk.json)
and siblings. Most old rounds are not named anywhere read: the stage is then undetermined. A company that
is recognised but has no trace of its fate reads status unknown with the search noted."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, verdict, post, wp, page = jl.cls, jl.rnd, jl.verdict, jl.post, jl.wp, jl.page
L = []
FIRM10 = "the firm's 2010 company page (Common Crawl CC-MAIN-2009-2010)"
DARK = "no trace of its fate in the status search (Google News, 2026-09-29) or on the firm's later pages, so the status is unknown"
def A(slug, status, cc, city=None, focus=None, note="", stage="undetermined", cc_src="model_knowledge", flags=(), **kw):
    fl = list(flags)
    if city is None:
        fl.append("city_unknown")
    return cls(slug, status=status, country=cc, country_src=cc_src, city=city, stage=stage, rng=kw.pop("rng", "below_1b"),
               focus=focus, flags=fl, note=note, **kw)
def wv(url, stage, date, **kw):
    return dict(stage=stage, stage_src="web_verified", stage_conf=kw.pop("conf", "high"), stage_cite=url, entry_date=date, **kw)

# ---- membership verdicts
L.append(verdict("nevion", "not_member",
    "sale consideration (COLLECTION.md s1, Erik 2026-09-22): Nevion is 'the combined entity of two industry-leading companies - Nevion and T-VIPS' (the firm's own 2017 page); Northzone held T-VIPS (the firm's 2010-12 pages, Gregers Kronborg) and its Nevion shares came from that merger; T-VIPS is the member",
    ec="site_listing", conf="high", cite="https://en.wikipedia.org/wiki/T-VIPS"))
L.append(verdict("summit-street-medical-llc", "not_member",
    "a prefix match: the filing's related person is Pauline Murphy, a Connecticut director, not Paul Murphy (the same cluster ruled out before the rebuild)",
    ec="formd_adjudicated", conf="high"))
L.append(verdict("mojn", "member", "Northzone led the $4M Series A of Feb 2014 (EU-Startups; ArcticStartup; the firm's own post 'Mojn secures 4 million funding to accelerate growth', 2014-02-03)",
    ec="web", conf="high", cite="https://www.eu-startups.com/2014/02/mojn-secures-4m-funding-in-a-series-a-round-led-by-northzone/"))
L.append(verdict("ocapo", "member", "Northzone led a GBP 9.5m investment in Ocapo Limited, July 2013 (FinSMEs; the firm's own post 'Northzone leads a GBP 9.5 million investment in Ocapo', 2013-07-04)",
    ec="web", conf="high", cite="https://www.finsmes.com/2013/07/ocapo-raises-9-5m-funding.html"))

# ---- 2003 page (the W5 site) and the 2010-12 pages
L.append(A("colibria", "unknown", "GB", "London", "SaaS", "Mobile instant messaging and presence platforms for operators (the firm's 2003 and 2010 pages: HQ London; co-investors Verdane Capital, Ferd Venture; Torleif Ahlsand); " + DARK))
L.append(A("cryptico", "unknown", "DK", "Copenhagen", "Security", "Chaos-based encryption (the firm's 2003 page); the firm 'sold back to founders in Q4-2006' (its 2010 page); " + DARK))
L.append(A("edvantage-group", "unknown", "NO", "Oslo", "SaaS", "E-learning software and outsourcing (the firm's 2003 and 2010 pages: HQ Oslo; co-investors Alliance Venture, Reitan, Altaria; Jörgen Bladh); " + DARK))
L.append(A("envox", "acquired", "SE", "Stockholm", "SaaS", "Voice and CTI application platform (the firm's 2003 page); 'acquired by Canada-based Enghouse Systems Inc. in Q3 2008' (the firm's 2010 page)"))
L.append(A("global-name-registry", "acquired", "GB", "London", "Data Infrastructure", "Registry for the .name top-level domain (the firm's 2003 and 2010 pages); acq. by VeriSign, 2008"))
L.append(A("hugin", "acquired", "NO", "Oslo", "Media, Gaming & Advertising", "Distributor of listed companies' financial information (the firm's 2003 page); 'Acquired in Q4-2006 by Euronext SA' (the firm's 2010 page)"))
L.append(A("ibistic", "acquired", "NO", "Oslo", "SaaS", "Purchasing and process-automation software (the firm's 2003 page); 'Acquired in Q1-2005 by Visma ASA' (the firm's 2010 page)"))
L.append(A("intility", "private", "NO", "Oslo", "Data Infrastructure", "Managed IT infrastructure for businesses (Oslo; the firm's 2003 page); the firm 'sold in Q2-2006 to financial investors' (its 2010 page); the company operates today"))
L.append(A("photonyx", "acquired", "NO", None, "Industrial & Robotics", "Optical components on a patented light-modulator technology (the firm's 2003 page); 'merged with Ignis ASA and was listed on the Oslo Stock Exchange in Q4-2003' (the firm's 2010 page)"))
L.append(A("port-it", "acquired", "NO", None, "Data Infrastructure", "Number portability and switching services for operators (the firm's 2003 page); 'Acquired in Q4-2003 by Labs2 ... Later sold to the Ventelo Group' (the firm's 2010 page)"))
L.append(A("skiinfo", "acquired", "NO", None, "Consumer & Marketplaces", "Ski and online booking site (the firm's 2003 page); 'Sold back to founders in Q3-2003' (the firm's 2010 page); later merged into OnTheSnow (Mountain News), 2010 (medium)", val_conf="medium"))
L.append(A("tinde", "acquired", "NO", "Oslo", "Consumer & Marketplaces", "Norwegian property marketplace (the firm's 2003 and 2010 pages); 'Sold in Q4-2004 to Orkla Media' (the firm's 2010 page)"))
L.append(A("appear-networks", "unknown", "SE", "Stockholm", "SaaS", "Context-aware mobile field-force software (the firm's 2010 page: HQ Stockholm); " + DARK))
L.append(A("beakon", "unknown", "SE", "Lund", "Industrial & Robotics", "Thermoelectric cooling (formerly NanoFreeze; the firm's 2010 page: HQ Lund/Malmö; co-investor TeknoSeed; Gregers Kronborg); " + DARK))
L.append(A("bilguiden", "acquired", "SE", None, "Consumer & Marketplaces", "Scandinavian online car classifieds; 'Acquired in Q2-2001 by Eniro AB (Scandinavia Online - SOL)' (the firm's 2010 page)"))
L.append(A("billiant-connova-labs2", "acquired", "SE", None, "Data Infrastructure", "IP billing systems for operators; 'Merged in Q4-2001 with Connova (which later merged with and renamed to Labs2)' (the firm's 2010 page)"))
L.append(A("chapdrive", "unknown", "NO", "Trondheim", "Climate & Energy", "Hydraulic transmission for wind turbines (the firm's 2010 page: HQ Trondheim; co-investors Statoil New Energy, Hafslund; Tellef Thorleifsson); the firm's archived post on the NOK 52M ($6M) round, 2009-02-11; " + DARK))
L.append(A("climatewell", "unknown", "SE", "Stockholm", "Climate & Energy", "Solar-driven air conditioning (the firm's 2010 page: HQ Stockholm; co-investors Utilsun, Industrifonden, Skirner; Hans Otterling); " + DARK))
L.append(A("doubletwist", "unknown", "US", None, "Consumer & Marketplaces", "Media sync app (the firm's 2010 page: HQ 'US, Norway'; co-investors Index Ventures, Horizon; Bjørn Stray; Wikipedia: backed by Index and Northzone); " + DARK))
L.append(A("enigma", "unknown", "US", "Santa Clara", "Industrial & Robotics", "Switch-fabric silicon (Enigma Semiconductor; the firm's 2010 page: HQ Santa Clara; co-investors TVM, InnovationsKapital, Sunstone; Arve J. Andresen); " + DARK + "; not Insight's or Ribbit's Enigma"))
L.append(A("fotango", "acquired", "GB", "London", "Consumer & Marketplaces", "Online photo portal founded in London in 2000; 'Acquired in Q3-2001 by Canon, Inc.' (the firm's 2010 page)"))
L.append(cls("fox-technologies", country="US", country_src="model_knowledge", city="Mountain View", stage="undetermined", rng="below_1b", focus="Security",
             note="Access-control security software (FoxT; the firm's 2010 page: HQ Mountain View; co-investors IT-Provider, Eqvitec; Pär-Jörgen Pärson); the pre-filled acquired stands"))
L.append(A("haburi", "acquired", "SE", None, "Consumer & Marketplaces", "Online outlet for apparel brands; 'Acquired in Q1-2003 by FortuneGlobe GmbH' (the firm's 2010 page)"))
L.append(A("imbera", "unknown", "FI", "Helsinki", "Industrial & Robotics", "Embedded-component PCB technology (the firm's 2010 page: HQ Helsinki; co-investors Conor, Index Ventures, Daeduck; Bjørn Stray); " + DARK))
L.append(A("innotech-solar", "unknown", "SE", None, "Climate & Energy", "Repowering off-spec solar cells (the firm's 2010-19 pages; Tellef Thorleifsson; the firm's posts 2010-2014); " + DARK))
L.append(A("interse", "unknown", "DK", "Copenhagen", "Data Infrastructure", "Automated classification and search of digital information (the firm's 2010 page: HQ Copenhagen; co-investor Nordic Venture Partners; Arve J. Andresen); " + DARK))
L.append(A("massmarket", "acquired", "NO", None, "Consumer & Marketplaces", "Internet purchasing service for SMEs; 'Acquired by Spray in Q3-2000, and later sold to Lycos Europe' (the firm's 2010 page)"))
L.append(A("mcp", "acquired", "NO", None, "Data Infrastructure", "GSM coverage on ships (Maritime Communications Partner); 'Aquired in Q3-2006 by Telenor ASA' (the firm's 2010 page)"))
L.append(A("norstel", "acquired", "SE", "Norrköping", "Industrial & Robotics", "Silicon carbide wafers (the firm's 2010 page: HQ Linköping; co-investors Eqvitec, Creandum; Jörgen Bladh); acq. by STMicroelectronics, 2019, aligned with Creandum's row"))
L.append(A("orecon", "unknown", "GB", "Plymouth", "Climate & Energy", "Wave-energy devices (the firm's 2010 page: HQ Plymouth; co-investors Advent, Venrock, Wellington; Torleif Ahlsand); " + DARK))
L.append(A("owera", "unknown", "NO", "Oslo", "Data Infrastructure", "VoIP device provisioning (the firm's 2010 page: HQ Oslo; co-investor Vikerud Ventures); " + DARK))
L.append(A("playdo", "unknown", "EE", "Tallinn", "Media, Gaming & Advertising", "Casual games and the Spineworld virtual world (the firm's 2010 page: HQ Tallinn; co-investors Miniclip, GP Bullhound; Torleif Ahlsand); " + DARK))
L.append(A("reisefeber", "acquired", "NO", None, "Consumer & Marketplaces", "Scandinavian travel site; 'Acquired in Q2-2002 by Travelocity, Inc.' (the firm's 2010 page)"))
L.append(A("replisaurus", "unknown", "SE", "Stockholm", "Industrial & Robotics", "Metal micro- and nanostructure fabrication (the firm's 2010 page: HQ Stockholm; co-investors Wellington, the 6th AP Fund; Bjørn Stray); " + DARK))
L.append(A("revolt-technology", "unknown", "NO", None, "Climate & Energy", "Rechargeable zinc-air batteries (the firm's 2010 page: HQ 'Norway/Switzerland'; co-investors Sofinova, TVM, Viking Venture, RWE; the firm's posts on the ARPA-E award, 2010); " + DARK))
L.append(A("seven-mountains", "unknown", "NO", None, "SaaS", "Java desktop and collaboration software: 'Northzone invested in Seven Mountains Software in 1997' (the firm's 2010 page), later funded by Holland Venture and 3i; " + DARK, flags=["country_prior"]))
L.append(A("silex", "acquired", "SE", "Stockholm", "Industrial & Robotics", "MEMS foundry (Silex Microsystems; the firm's 2010 page: HQ Stockholm; co-investors Priveq, CapMan; Tellef Thorleifsson); the firm's post 'Northzone exits Silex Microsystems AB' (2015-07-14); owned since by Sai MicroElectronics"))
L.append(A("speakanet", "unknown", "DK", "Copenhagen", "Data Infrastructure", "Mobile PBX replacement (GoHello; the firm's 2010 page: HQ Copenhagen; co-investors Eqvitec, Via Venture Partners; Arve J. Andresen); " + DARK))
L.append(A("t-vips", "acquired", "NO", "Oslo", "Data Infrastructure", "IP video transmission for broadcasters (the firm's 2010 page: HQ Oslo; Gregers Kronborg); merged into Nevion in 2012 (Wikipedia; the firm's 2017 Nevion page), so acquired; Nevion itself is sale consideration and not a row"))
L.append(A("testfreaks", "unknown", "SE", "Stockholm", "Consumer & Marketplaces", "Product-review aggregator by PriceRunner's founders (the firm's 2010 page: HQ Stockholm; Pär-Jörgen Pärson; Wikipedia: Northzone also invested in TestFreaks); " + DARK))
L.append(A("the-bizmo", "unknown", "NO", "Oslo", "Consumer & Marketplaces", "Digital-content storefronts (UGC Ltd; the firm's 2010 page: HQ Oslo; co-investors East Coast Angels, Burda; Pär-Jörgen Pärson); " + DARK))
L.append(A("xcerion", "private", "SE", "Linköping", "Data Infrastructure", "Web desktop and cloud storage, founded 2001 (the firm's 2010 page: HQ Linköping; Jörgen Bladh), operating as CloudMe (medium)", val_conf="medium"))

# ---- 2013-2025 pages
L.append(A("activate", "unknown", "US", "New York", "Media, Gaming & Advertising", "Influencer marketing platform; 'Activate started life as Bloglovin'' and rebranded in 2018 (the firm's 2018 page); Northzone led Bloglovin's $7M Series A (the firm's archived post, 2014-04-03); " + DARK,
    **wv(wp("bloglovin-raises-7-million-in-series-a-financing-led-by-northzone"), "Series A", "2014-04"), flags=["model_disputes_source"]))
L.append(A("aevy", "unknown", "SE", None, "SaaS", "Automated candidate sourcing (the firm's 2017-25 pages); the country is the firm's Nordic desk (no HQ on the surfaces read); " + DARK, flags=["country_prior"]))
L.append(A("allunite", "unknown", "DK", "Copenhagen", "Media, Gaming & Advertising", "Wi-fi advertising for shops, founded 2013 by Kasper Gevaldig and Esben Elmoe (the firm's 2017 page, Danish-language posts); " + DARK))
L.append(A("artfinder", "unknown", "GB", "London", "Consumer & Marketplaces", "Online art marketplace (London); the firm's archived post 'Art discovery service Artfinder draws new funding' (2012-02-09); " + DARK))
L.append(A("auka", "unknown", "NO", "Oslo", "Fintech & Payments", "White-label mobile payments for banks (the firm's 2017 page); " + DARK))
L.append(A("bnt", "unknown", "US", None, "SaaS", "A company the firm listed as 'BNT' on its 2017-19 pages (the page shows only its tweets on B2B customer communities); the company cannot be named from any surface read",
    stage="undetermined", rng="undetermined", flags=["identity_unresolved", "country_prior"], grad="undetermined"))
L.append(A("boomlagoon", "acquired", "FI", "Helsinki", "Media, Gaming & Advertising", "Mobile games (Helsinki); the firm's archived post welcoming Boomlagoon (2014-05-12); joined Wargaming as Wargaming Helsinki, Dec 2016 (the company's own post on the firm's 2017 page)"))
L.append(A("bravenewtalent", "unknown", "GB", "London", "SaaS", "Social recruiting (London); the firm's archived post 'Social recruiting company BraveNewTalent.com secures venture investment' (2011-02-02); " + DARK))
L.append(A("cachecash", "unknown", "US", None, "Crypto & Web3", "Decentralised CDN with a resource-backed token (the firm's 2019 page); " + DARK))
L.append(A("cornerjob", "unknown", "ES", "Barcelona", "Consumer & Marketplaces", "Mobile job ads for blue-collar work, founded by Wallapop's founders (the firm's 2017 page: HQ Barcelona); " + DARK,
    **wv(wp("cornerjob-raises-series-b"), "Growth", "2016-07", conf="medium"),
    rounds=[rnd("2016-07-11", "Series B", None, None, True, wp("cornerjob-raises-series-b"), "firm")]))
L.append(A("eprospects", "unknown", "GB", None, "Fintech & Payments", "Digital performance marketing for consumer finance (the firm's 2013-19 pages); " + DARK))
L.append(A("fusetools", "unknown", "NO", "Oslo", "DevTools & APIs", "Fuse app-development tools by Outracks Technologies (Oslo): the firm's archived posts 'Outracks raises 3.5 million from Northzone and Alliance Venture' (2014-06-12), 'Fuse emerges from stealth ... secures $2.8M' (2015) and the $12M Series A (2017-01-24); the 2014 round is not named; " + DARK))
L.append(A("heygo", "defunct", "GB", "London", "Consumer & Marketplaces", "Live virtual travel tours (London); the firm's archived post 'Our investment in Heygo' (2022-02-15), round not named; wound down, aligned with Lightspeed's and Point Nine's defunct"))
L.append(cls("kitab-sawti", status="acquired", country="AE", country_src="model_knowledge", city=None, rng="below_1b", focus="Media, Gaming & Advertising",
    flags=["city_unknown"], note="Arabic audiobooks; the $6M Series A of May 2019 (the firm's archived post); acq. by Storytel, July 2020 (MENAbytes, SME10X)",
    **wv(wp("kitab-sawti-an-arabic-audiobook-platform-raises-6-million-series-a-from-international-and-regional-investors-including-careems-abdulla-elyas"), "Series A", "2019-05")))
L.append(A("lemoncat", "acquired", "DE", "Berlin", "Consumer & Marketplaces", "Business catering marketplace (Berlin); the firm's post 'Announcing investment: Lemoncat' (2017-04-24), round not named; acq. by Rocket Internet's Caterwings, 2019 (the firm's post 2019-08-13); aligned with Point Nine"))
L.append(A("lesara", "defunct", "DE", "Berlin", "Consumer & Marketplaces", "Fast-fashion e-commerce (Berlin); the EUR 15M Series B from Northzone and Vorwerk (the firm's archived post, 2015-09-10); insolvency, Nov 2018 (EU-Startups), aligned with Cherry",
    **wv(wp("lesara-announces-e-15-m-series-b-investment-from-northzone-and-vorwerk-venture"), "Growth", "2015-09"),
    rounds=[rnd("2015-09-10", "Series B", None, None, True, wp("lesara-announces-e-15-m-series-b-investment-from-northzone-and-vorwerk-venture"), "firm")]))
L.append(A("letgo", "acquired", "US", "New York", "Consumer & Marketplaces", "Second-hand marketplace app (New York and Barcelona); the firm listed it 2017-19, round not named; acq. by OfferUp, 2020 (Retail TouchPoints), aligned with Insight"))
L.append(cls("mcash", status="private", country="NO", country_src="web_verified", country_cite="https://en.wikipedia.org/wiki/Settle_Group", city="Oslo",
    rng="below_1b", focus="Fintech & Payments",
    note="Mobile payments (Oslo), today Settle Group; Northzone and Entrée invested NOK 43M (the firm's archived post 2014-02-19), 'a $6.87m Series A round led by Northzone Ventures' (Wikipedia, Settle Group); SpareBank 1 bought the Norwegian entity in 2015 (the firm's post), the company continues as Settle",
    **wv("https://en.wikipedia.org/wiki/Settle_Group", "Series A", "2014-02", conf="medium")))
L.append(cls("mojn", status="unknown", country="DK", country_src="web_verified",
    country_cite="https://www.eu-startups.com/2014/02/mojn-secures-4m-funding-in-a-series-a-round-led-by-northzone/", city="Copenhagen",
    rng="below_1b", focus="Media, Gaming & Advertising",
    note="Real-time retargeted email for e-commerce (Copenhagen, founded 2009 as RealTime Targeting); Northzone led the $4M Series A with Notion Capital and Zoar Invest, Feb 2014 (EU-Startups); " + DARK,
    **wv("https://www.eu-startups.com/2014/02/mojn-secures-4m-funding-in-a-series-a-round-led-by-northzone/", "Series A", "2014-02")))
L.append(A("nyx-security", "unknown", "SE", None, "Security", "Security technology (Sweden; the firm's archived posts 2012-13 in Swedish on NYX Revolution and new CEOs); " + DARK + "; not the Israeli Nyx Security Upwind bought in 2025"))
L.append(A("obc", "unknown", "SE", None, None, "A company the firm listed as 'OBC' on its 2017-19 pages (the captured page carries no text); the company cannot be named from any surface read",
    rng="undetermined", flags=["identity_unresolved", "country_prior"], grad="undetermined"))
L.append(cls("ocapo", status="unknown", country="GB", country_src="web_verified", country_cite="https://www.finsmes.com/2013/07/ocapo-raises-9-5m-funding.html",
    city="London", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Online performance marketing and lead generation (London, Dubai, Hong Kong); Northzone led a GBP 9.5m investment with BOOST&Co, July 2013 (FinSMEs; the firm's post), round not named; " + DARK))
L.append(A("one2-1two", "unknown", "GB", None, "Media, Gaming & Advertising", "Hip-hop creator app, formerly 8 Bars (the firm's 2024 page); " + DARK))
L.append(A("p1", "unknown", "CN", "Beijing", "Consumer & Marketplaces", "Private social network for urban Chinese youth (the firm's post 'Northzone invests in P1', 2012-10-02; the 2013-19 pages); " + DARK, flags=["model_disputes_source"]))
L.append(A("pollen", "defunct", "GB", "London", "Consumer & Marketplaces", "Invite-only experiences platform, formerly Verve (London); Northzone led the $60M round of Oct 2019 (the firm's post 'Pollen closes $60m in financing led by Northzone'; WSJ), round not named; the company collapsed into administration in 2022; not YC's Pollen"))
L.append(A("qapital", "private", "US", "New York", "Fintech & Payments", "Savings and banking app (founded in Stockholm, New York HQ); the firm's archived post on the $12M round (2017-03-06; Finovate), round word not given"))
L.append(cls("salus", status="private", country="TR", country_src="web_verified", country_cite=post("our-investment-in-salus-delivering-mental-health-support-for-all"),
    city="Istanbul", rng="below_1b", focus="Healthcare & Bio",
    note="Mental-health support platform (Istanbul, founded 2022); Northzone led the $4.7M seed with 500 Emerging Europe, Wamda and İş Bank's CVC (the firm's post, 2023-11-20); the pre-filled DE is a one-word Wikidata join, disputed; not YC's Salus",
    flags=["model_disputes_source"], **wv(post("our-investment-in-salus-delivering-mental-health-support-for-all"), "Seed", "2023-11")))
L.append(A("soundrop", "acquired", "NO", "Oslo", "Media, Gaming & Advertising", "Spotify app for music rooms (Oslo); Northzone invested $3M (the firm's post, 2012-06-12); the dormant product was taken over by Show.co and revived under CD Baby, 2016 (Music Business Worldwide), read as acquired (medium)", val_conf="medium"))
L.append(A("sqore", "unknown", "SE", "Stockholm", "SaaS", "Recruitment competitions for students, founded 2010 (the firm's 2017 page: HQ Stockholm); $3.5M from Northzone (the firm's archived post, 2015-03-01), round not named; " + DARK))
L.append(A("the-online-backup-company", "unknown", "NO", None, "Data Infrastructure", "Online backup (Norway); 'Northzone invests in The Online Backup Company' (the firm's archived posts 2010-01-11 and 2012-01-02; $5M, StorageNewsletter 2012-01-09); " + DARK))
L.append(A("universal-avenue", "unknown", "SE", "Stockholm", "SaaS", "On-demand brand-ambassador sales force (the firm's 2017 page); $5M in 2015 (FinSMEs; the firm's post), round not named; " + DARK))
L.append(A("visualdna", "acquired", "GB", "London", "Media, Gaming & Advertising", "Personality profiling for advertising (London; Imagini until 2011; the firm's 2010 page: co-investors Horizon, Atomico); acq. by Nielsen, 2019, aligned with Atomico"))
L.append(A("widespace", "unknown", "SE", "Stockholm", "Media, Gaming & Advertising", "Mobile ad network, founded 2007 (the firm's 2017 page); 'Widespace lands EUR 3m from Spotify investor Northzone and Industrifonden' (the firm's archived post, 2012-06-09), round not named; " + DARK))
L.append(A("x5-music-group", "acquired", "SE", "Stockholm", "Media, Gaming & Advertising", "Digital music catalogue company (Stockholm and New York; the firm's 2013-19 pages); acq. by Warner Music Group, June 2016 (The Music Network)"))
L.append(A("jukely", "unknown", "US", "New York", "Consumer & Marketplaces", "Unlimited-concerts subscription (the firm's 2017-19 pages); " + DARK))
L.append(A("playraven", "acquired", "FI", "Helsinki", "Media, Gaming & Advertising", "Mobile strategy games (Helsinki; the firm's 2017-19 pages), round not named; acq. by Rovio, aligned with Creandum's acquired"))
jl.write("batch-delta-1", L)
