"""PRO-99 Kleiner Perkins, judge j01, queue batch 2 (azarus .. corventis): classification of listed members, plus three
membership corrections (box and chronosphere partner-carried; ciena sale consideration / post-listing)."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, W, FORMD_CITE

# URLs printed by tools run in this session (fts listing / secget, WebFetch and WebSearch reads, sibling rows)
S1_BOX = "https://www.sec.gov/Archives/edgar/data/1372612/000119312514112417/d642425ds1.htm"
Q10_CIENA = "https://www.sec.gov/Archives/edgar/data/936395/000095013303001977/w86951e10vq.htm"
S1_BYND = "https://www.sec.gov/Archives/edgar/data/1655210/000162828018014471/beyondmeats-1.htm"
DRS_BLOOM = "https://www.sec.gov/Archives/edgar/data/1664703/000095012316015543/filename1.htm"
S1_CBLK = "https://www.sec.gov/Archives/edgar/data/1366527/000104746918002643/a2235165zs-1.htm"
PROSP_CARDIMA = "https://www.sec.gov/Archives/edgar/data/1022570/0001012870-97-001126.txt"
S1_CARDIODX = "https://www.sec.gov/Archives/edgar/data/1304909/000104746913009619/a2216950zs-1.htm"
SA_BE = "https://stockanalysis.com/stocks/be/market-cap/"
SA_BETR = "https://stockanalysis.com/stocks/betr/market-cap/"
BUN_BLOG = "https://bun.com/blog/bun-joins-anthropic"
BB_SERIES_B = "https://www.browserbase.com/blog/series-b-and-beyond"
AZ_SEED = ("https://www.blockchaingamer.biz/news/11459/azarus-raises-1-8-million-in-seed-funding-from-galaxy-eos-vc-and-"
           "other-investors/")
AZ_ANIMOCA = "https://bravenewcoin.com/insights/the-future-is-now-azaruss-alex-casassovici-on-leading-the-livestream"
SA_CSB = ("https://siliconangle.com/2024/12/12/together-ai-acquires-codesandbox-adds-code-interpreter-ai-development-"
          "platform/")
GL = "Graduation left for the graduation pass."

L = []

# ---- membership corrections (verdict line only)
L.append(verdict("box", "not_member",
                 "Partner-carried (Erik 2026-09-17 partner-carried rule; decisions.md D3): Box is on the firm's live list "
                 "only, never on the kpcb.com archive, with a 2007 year; the one KP-side trace is Mamoon Hamid as a "
                 "director on Box's 2009-2011 Form Ds, when he was at U.S. Venture Partners (he joined Kleiner Perkins "
                 "in 2017), and Box's 2014 S-1 names no Kleiner Perkins entity among its holders or its financings.",
                 ec="web", conf="medium", cite=S1_BOX))
L.append(verdict("chronosphere", "not_member",
                 "Partner-carried (Erik 2026-09-17 partner-carried rule; decisions.md D3): the firm's card dates a Growth "
                 "entry to 2021, two years before Leigh Marie Braswell joined; the firm's welcome post of 2023-05-24 "
                 "lists Chronosphere among the investments she led 'in her first few years in venture', before Kleiner "
                 "Perkins, and no Kleiner Perkins fund appears in the rounds the Greylock, GV, Lux and Spark rows record.",
                 ec="web", conf="medium", cite=POST("welcoming-leigh-marie-braswell")))
L.append(verdict("ciena", "not_member",
                 "Ciena listed on Nasdaq in February 1997, before the firm's 1998 year, and no pre-IPO Kleiner Perkins round "
                 "is on record (T3). The firm's link is ONI Systems, a KP-backed optical company Ciena bought for stock in "
                 "2002 (Ciena's 2003 10-Q names KPCB as a defendant in the ONI Systems IPO litigation): the Ciena shares "
                 "are sale consideration (Erik 2026-09-22), and ONI Systems is the company to add as its own row.",
                 ec="web", conf="medium", cite=Q10_CIENA))

# ---- Azarus
L.append(cls("azarus", status="acquired", rng="below_1b", country="US", stage="Seed", stage_src="web_verified",
             stage_cite=AZ_SEED, stage_conf="high", entry_date="2019-06", focus="Media, Gaming & Advertising",
             flags=["city_unknown"],
             rounds=[rnd("2019-06", "Seed", 1800000, None, True, AZ_SEED, "press"),
                     rnd("2021", "extended seed", 4000000, "Galaxy Digital, Animoca Brands, Kleiner Perkins", True, None,
                         "press")],
             note="Interactive challenges and rewards for game livestreams. BlockchainGamer: 'Azarus has managed to "
                  "successfully raise more than $1.8m in seed funding' from Galaxy Digital, SVK Crypto, Kleiner Perkins "
                  "and others (June 2019, the firm's own post the same month). Animoca Brands later took majority "
                  "ownership, making it a subsidiary (Brave New Coin interview with the CEO), so acquired; its own "
                  "domain now redirects to a video. No source places its city; country US at low confidence. " + GL))

# ---- Beam Dental (Beam Benefits)
L.append(cls("beam-dental", status="acquired", rng="below_1b", country="US", city="Columbus", stage="undetermined",
             entry_date="2018", focus="Fintech & Payments",
             note="Digital dental and benefits insurance (Beam Benefits), Columbus, Ohio. Its site's footer now names "
                  "its insurance and administration entities 'wholly owned subsidiaries of Principal Financial Group' "
                  "(checked 2026-09-30), so acquired. The firm labels a 2018 Growth entry; no source read names the "
                  "round."))

# ---- Bedrock Systems (now BlueRock Security)
L.append(cls("bedrock-systems", status="private", rng="below_1b", country="US", city="Boston", stage="undetermined",
             entry_date="2020", focus="Security",
             note="Formally verified hypervisor and security platform; bedrocksystems.com now redirects to BlueRock "
                  "Security Inc., which operates under that name (checked 2026-09-30): renamed, still private. City "
                  "Boston from model knowledge, medium. The firm's since-year is 2020; no source read names the round."))

# ---- Better (Better Home & Finance)
L.append(cls("better-mortgage", status="public", rng="below_1b", usd=208980000, val_src="web_verified",
             val_cite=SA_BETR, asof="2026-09-30", country="US", city="New York", stage="undetermined",
             entry_date="2016", focus="Fintech & Payments",
             note="Digital mortgage lender, New York; listed on Nasdaq as Better Home & Finance (BETR) since the 2023 "
                  "SPAC merger, market cap $208.98M on 2026-09-30 (stockanalysis). The firm labels a 2016 Growth "
                  "entry; no source read names the round."))

# ---- BetterWorks
L.append(cls("betterworks", status="private", rng="below_1b", city="Redwood City", stage="undetermined",
             entry_date="2013", focus="SaaS",
             note="OKR and performance management software founded by Kris Duggan, Redwood City, with John Doerr on the "
                  "deal; still private. The firm's since-year is 2013; no source read names the round. Not the "
                  "Santa Monica BetterWorks (employee perks) of the Redpoint book, a different company."))

# ---- Beyond Meat
L.append(cls("beyond-meat", city="El Segundo", stage="Series A", stage_src="web_verified", stage_cite=S1_BYND,
             stage_conf="medium", entry_date="2011", focus="Consumer & Marketplaces",
             rounds=[rnd("2011", "Series A", 2000000, "Kleiner Perkins", True, POST("beyond-meat-the-future"), "firm")],
             note="Plant-based meat, headquartered in El Segundo (Wikipedia). The firm's post of 2019-05-02: 'Kleiner "
                  "Perkins was the only institutional investor in the first financing round in Beyond Meat back in "
                  "2011'; the 2018 S-1 shows that first preferred series was the Series A (5,000,000 shares, $2.0M). "
                  "The pre-filled 2015 date is a later Form D, so the entry date is 2011."))

# ---- Bison Trails
L.append(cls("bison-trails", status="acquired", rng="below_1b", country="US", city="New York", stage="Series A",
             stage_src="first_party", stage_cite=POST("welcome-bison-trails"), stage_conf="high", entry_date="2019-11",
             focus="Crypto & Web3",
             rounds=[rnd("2019-11", "Series A", None, None, True, POST("welcome-bison-trails"), "firm")],
             note="Blockchain node infrastructure, New York; Coinbase bought it in 2021 (the firm's exit line). The "
                  "firm's post of 2019-11-19: 'We're excited to welcome Bison Trails to the Kleiner Perkins family and "
                  "be part of their Series A.'"))

# ---- Bitstrips
L.append(cls("bitstrips", status="acquired", rng="below_1b", country="CA", city="Toronto", stage="undetermined",
             entry_date="2014", focus="Consumer & Marketplaces",
             note="Bitmoji and comic-avatar maker, Toronto (the pre-filled CA is confirmed); Snap bought it in 2016 (the "
                  "firm's exit line). The firm labels a 2014 Growth entry; no source read names the round."))

# ---- Bloom Energy
L.append(cls("bloom-energy", rng="10b_plus", usd=82910000000, val_src="web_verified", val_cite=SA_BE,
             asof="2026-09-30", city="San Jose", stage="undetermined", entry_date="2002", focus="Climate & Energy",
             flags=["model_disputes_source"],
             rounds=[rnd("2002", "first venture round (not named)", None, None, True, DRS_BLOOM, "filing")],
             note="Solid oxide fuel cells, San Jose (NYSE: BE). The 2016 draft S-1: 'In 2002, Kleiner Perkins Caufield "
                  "Byers became our first venture capital investor', without a round name. The pre-filled $3.9B public "
                  "float is stale: market cap $82.91B on 2026-09-30 (stockanalysis), aligned with the NEA row, so "
                  "10b_plus."))

# ---- BlueOak
L.append(cls("blueoak", status="unknown", rng="below_1b", focus="Climate & Energy", flags=["city_unknown"],
             note="Distributed mini-refineries recovering metals from electronic waste (BlueOak Resources; plant in "
                  "Osceola, Arkansas). Its only Form D gives an investor's Sand Hill Road address, so no source read "
                  "places the head office, and no acquisition, shutdown or later round was found. " + GL))

# ---- Booyah
L.append(cls("booyah", status="defunct", rng="below_1b", city="Palo Alto", grad="graduated", grad_src="formd",
             grad_cite=FORMD_CITE("booyah"), grad_conf="high", focus="Media, Gaming & Advertising",
             rounds=[rnd("2009-09", "unnamed (Form D)", 4999999, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1447359/000144735909000002/0001447359-09-000002-index.htm",
                         "filing"),
                     rnd("2010-05", "unnamed (Form D; the Accel row reads it Series B)", 20000000, "Accel", True, FORMD_CITE("booyah"), "filing")],
             note="Mobile location games (MyTown), an iFund company; its first Form D gives the company's address as "
                  "care of Kleiner Perkins. Palo Alto on the firm's 2008-11 listing; wound down, as the Accel row. The "
                  "$20M round of 2010 is four times the 2009 entry and graduates the Form D Seed entry (the layer "
                  "agrees); the Accel row notes Kleiner did the earlier round."))

# ---- Breathe Technologies
L.append(cls("breathe-technologies", status="acquired", rng="below_1b", city="Irvine", stage="undetermined",
             entry_date="2008", focus="Healthcare & Bio",
             note="Wearable ventilation for respiratory patients, Irvine, California (its 2017 Form D); Hillrom bought "
                  "it in 2019 (the firm's exit line). The firm's since-year is 2008 (Fremont on the 2008-11 listing), "
                  "so the 2014 Form D is a later round and the date is replaced by 2008; no round is named."))

# ---- Brex
L.append(cls("brex", status="acquired", rng="below_1b", city="San Francisco", stage="Growth", stage_src="web_verified",
             stage_cite=W("Brex"), stage_conf="high", entry_date="2019-06", focus="Fintech & Payments",
             rounds=[rnd("2017", "Series A", 7000000, "Ribbit Capital", False, W("Brex"), "press"),
                     rnd("2018-06", "Series B", 50000000, None, False, W("Brex"), "press"),
                     rnd("2018-10", "Series C", 125000000, None, False, W("Brex"), "press"),
                     rnd("2019-06", "Series C-2", 100000000, "Kleiner Perkins", True, W("Brex"), "press")],
             note="Corporate cards and spend management, San Francisco. Wikipedia: the $100M Series C-2 of June 2019 at "
                  "$2.6B 'was led by Kleiner Perkins', the firm's 2019 Growth entry. Capital One completed its $5.15B "
                  "acquisition in April 2026, aligned with the IVP, Ribbit, TCV, Tiger and YC rows."))

# ---- Browserbase
L.append(cls("browserbase", status="private", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="first_party", stage_cite=POST("browserbase-ai-seriesa"), stage_conf="high", entry_date="2024",
             grad="graduated", grad_src="first_party", grad_cite=POST("browserbase-ai-seriesa"), grad_conf="high",
             focus="DevTools & APIs",
             rounds=[rnd("2024", "Seed", None, "Kleiner Perkins", True, POST("browserbase-ai-seriesa"), "firm"),
                     rnd("2024-11-01", "Series A", 21000000, "Kleiner Perkins (co-lead)", True,
                         POST("browserbase-ai-seriesa"), "firm"),
                     rnd("2025-06-18", "Series B", 40000000, "Notable Capital", True, BB_SERIES_B, "company")],
             extra={"valuation_range_source": "web_verified", "valuation_citation": BB_SERIES_B},
             note="Headless browsers for AI agents, San Francisco. The firm's post of 2024-11-01: 'Browserbase announced "
                  "its Series A financing, co-led by Kleiner Perkins. This comes after we led their Seed earlier this "
                  "year', a Seed entry that graduated. Momentum check 2026-09-30: the latest priced round is the $40M "
                  "Series B of 2025-06-18 led by Notable Capital with Kleiner Perkins (the company's post; press put "
                  "it at $300M post-money); no $1B+ round found."))

# ---- buddybuild
L.append(cls("buddybuild", status="acquired", rng="below_1b", country="CA", city="Vancouver", stage="undetermined",
             entry_date="2016", focus="DevTools & APIs",
             note="Mobile continuous integration and crash reporting, Vancouver; Apple bought it in January 2018 (the "
                  "firm's exit line), as the First Round row. The firm's since-year is 2016; no source read names the "
                  "round."))

# ---- Bun (Oven)
L.append(cls("bun", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="web_verified", stage_cite=BUN_BLOG, stage_conf="high", entry_date="2022",
             grad="graduated", grad_src="web_verified", grad_cite=BUN_BLOG, grad_conf="high", focus="DevTools & APIs",
             rounds=[rnd("2022", "Seed", 7000000, "Kleiner Perkins", True, BUN_BLOG, "company"),
                     rnd("2023", "Series A", 19000000, "Khosla Ventures", None, BUN_BLOG, "company"),
                     rnd("2025-12-02", "acquisition by Anthropic", None, None, None, BUN_BLOG, "company")],
             note="The Bun JavaScript runtime (company Oven), San Francisco. The company's post of 2025-12-02: 'We raised "
                  "a $7 million seed round led by Kleiner Perkins' and then 'a $19 million Series A led by Khosla "
                  "Ventures'; the same post announces Bun joining Anthropic (the firm's post 'we proudly led Bun (then "
                  "called Oven's) Seed')."))

# ---- Calico Commerce
L.append(cls("calico-commerce", status="acquired", rng="below_1b", country="US", city="San Jose", stage="undetermined",
             focus="SaaS",
             note="E-business configuration software, San Jose; IPO 1999, then Chapter 11 in 2001 with its business "
                  "sold to PeopleSoft: acquired, an asset sale out of insolvency. KPCB held 11.4% in 2001 (its proxy); "
                  "no round is named."))

# ---- Carbon Black
L.append(cls("carbon-black", rng="below_1b", country="US", city="Waltham", stage="undetermined", entry_date="2006",
             focus="Security",
             note="Endpoint security (incorporated 2002 as Bit9, renamed after buying Carbon Black in 2014), Waltham, "
                  "Massachusetts; IPO 2018, bought by VMware in 2019. The 2018 S-1 has KPCB XII (a 2006 fund) holding "
                  "8.8% and buying Series F; the firm's since-year is 2006, and no source read names the round it "
                  "first joined."))

# ---- Cardima
L.append(cls("cardima", status="defunct", rng="below_1b", country="US", city="Fremont", stage="Series A",
             stage_src="web_verified", stage_cite=PROSP_CARDIMA, stage_conf="high", entry_date="1993-05",
             focus="Healthcare & Bio",
             rounds=[rnd("1993-05", "Series A Preferred", None, None, True, PROSP_CARDIMA, "filing")],
             note="Microcatheters for electrophysiology, Fremont. The 1997 prospectus lists Kleiner Perkins Caufield & "
                  "Byers VI buying 285,714 Series A shares (then C, D and E), with Joe Lacob chairman from May 1993. "
                  "Defunct after its 2010 bankruptcy decision, aligned with the NEA row."))

# ---- CardioDx
L.append(cls("cardiodx", status="defunct", rng="below_1b", city="Palo Alto", stage="undetermined", entry_date="2003-07",
             focus="Healthcare & Bio", flags=["stage_disputes_band"],
             note="Gene-expression tests for coronary artery disease, Palo Alto (the 2013 S-1). Incorporated July 2003 "
                  "with Brook Byers a director from July 2003 and its CEO until August 2004, so Kleiner Perkins was "
                  "there at formation and the 2010 Form D band (Growth) is a follow-on; the founding round is not "
                  "named. The IPO was withdrawn, filings stop in 2017 and its domain now serves an unrelated site "
                  "(checked 2026-09-30): defunct, medium confidence."))

# ---- CareDx
L.append(cls("caredx", city="Brisbane", focus="Healthcare & Bio",
             note="Transplant diagnostics (formerly XDx), Brisbane, California (Nasdaq: CDNA)."))

# ---- Cell Design Labs
L.append(cls("cell-design-labs", status="acquired", rng="below_1b", city="San Francisco", focus="Healthcare & Bio",
             note="Synthetic-biology cell therapy from Wendell Lim's UCSF lab; Kite Pharma (Gilead) bought it in "
                  "2017 (the firm's exit line: Gilead Sciences). City San Francisco from knowledge; the 2016 Form D "
                  "gives an officer's Lafayette address."))

# ---- Cerent
L.append(cls("cerent", status="acquired", rng="below_1b", country="US", city="Petaluma", stage="undetermined",
             entry_date="1997", focus="Data Infrastructure",
             rounds=[rnd("1997", "founding round (not named)", None, None, True, W("Cerent Corporation"), "press")],
             note="SONET optical access equipment, Petaluma; Cisco bought it in 1999. Wikipedia: founded in 1997 as "
                  "Fiberlane Communications 'with funding from Kleiner Perkins Caufield & Byers and Vinod Khosla as "
                  "the managing VC'; no round name (the firm's card says 1998)."))

# ---- CesiumAstro
L.append(cls("cesiumastro", status="private", rng="below_1b", city="Austin", focus="Industrial & Robotics",
             note="Phased-array satellite and airborne communications, Austin. Its 2026 Series C ($270M equity plus "
                  "EXIM debt) disclosed no valuation; press cites only an unnamed source that it crossed $1B, which is "
                  "no citable figure (Rule A), so below_1b until a priced mark is published (a Series D was under way "
                  "in August 2026)."))

# ---- ChargePoint
L.append(cls("chargepoint", city="Campbell", focus="Climate & Energy",
             note="EV charging network, Campbell, California (NYSE: CHPT)."))

# ---- Chef Robotics
L.append(cls("chef-robotics", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2019", focus="Industrial & Robotics",
             note="AI food-assembly robots, San Francisco. The firm's since-year is 2019; no source read names the "
                  "round. No $1B+ priced round on record."))

# ---- Chegg
L.append(cls("chegg", city="Santa Clara", focus="Consumer & Marketplaces",
             note="Student learning services, Santa Clara (NYSE: CHGG)."))

# ---- Choose Energy
L.append(cls("choose-energy", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2012", focus="Consumer & Marketplaces",
             note="Online marketplace for retail electricity and gas plans, San Francisco; Red Ventures bought it (the "
                  "firm's exit line). The firm labels a 2012 Growth entry (Greentech team); no source read names the "
                  "round."))

# ---- Citrix
L.append(cls("citrix", rng="below_1b", country="US", city="Fort Lauderdale", stage="undetermined", entry_date="1989",
             focus="Data Infrastructure",
             note="Application and desktop virtualization, Fort Lauderdale; IPO 1995, taken private by Vista and "
                  "Elliott in 2022 and combined with TIBCO. Kevin Compton, a KP general partner from 1990, was a "
                  "director from 1991 (its 2001 proxy); the firm's since-year is 1989 and no round is named."))

# ---- Clean Power Finance
L.append(cls("clean-power-finance", status="acquired", rng="below_1b", city="San Francisco", stage="undetermined",
             focus="Climate & Energy",
             note="Residential solar finance marketplace, San Francisco (222 7th Street on its 2011 Form D); it became "
                  "Spruce Finance and was bought by XL Fleet in 2022 (now Spruce Power): acquired. A Green Growth Fund "
                  "position (Ben Kortlang) whose first round is not named in any source read."))

# ---- CloudHealth Technologies
L.append(cls("cloudhealth-technologies", status="acquired", rng="below_1b", city="Boston", stage="Growth",
             stage_src="web_verified", stage_cite=W("CloudHealth Technologies"), stage_conf="high", entry_date="2017-06",
             focus="SaaS",
             rounds=[rnd("2017-06", "Series D", 46000000, "Kleiner Perkins Caufield & Byers", True,
                         W("CloudHealth Technologies"), "press")],
             note="Cloud cost management, Boston; VMware bought it in 2018. Wikipedia: 'In June 2017, CloudHealth "
                  "Technologies secured $46 million in Series D funding led by Kleiner Perkins Caufield & Byers', the "
                  "firm's 2017 Growth entry."))

# ---- CloudPhysics
L.append(cls("cloudphysics", status="acquired", rng="below_1b", country="US", city="Santa Clara", stage="undetermined",
             entry_date="2012", focus="Data Infrastructure",
             note="Analytics for virtualized data centres, Santa Clara; Hewlett Packard Enterprise bought it in 2018 "
                  "(the firm's exit line: HPE). The firm's since-year is 2012 (Mike Abbott); no source read names the "
                  "round."))

# ---- Coda
L.append(cls("coda", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="Growth",
             stage_src="first_party", stage_cite=POST("welcome-coda"), stage_conf="high", entry_date="2020-08",
             focus="SaaS",
             rounds=[rnd("2020-08-11", "Series C", None, "Kleiner Perkins", True, POST("welcome-coda"), "firm")],
             note="The coda.io all-in-one doc, Mountain View, as the General Catalyst, Greylock and NEA rows; Grammarly "
                  "bought it in December 2024. The firm's post of 2020-08-11: 'We're excited to be part of Coda's "
                  "pursuit of productivity and lead their Series C', its first round in the company (the card's 2014 "
                  "year predates any KP round on record). Not the Coda Payments of Singapore in the Insight book."))

# ---- CodeSandbox
L.append(cls("codesandbox", status="acquired", rng="below_1b", country="NL", country_src="web_verified",
             country_cite=SA_CSB, city="Amsterdam", focus="DevTools & APIs", flags=["model_disputes_source"],
             note="Browser-based development environments, Amsterdam (CodeSandbox, Inc. files its Form D from San "
                  "Francisco as the US entity, hence the pre-filled US); Together AI bought it in December 2024 "
                  "(SiliconANGLE), aligned with the EQT Ventures row."))

# ---- Collective Medical
L.append(cls("collective-medical", status="acquired", rng="below_1b", country="US", city="Salt Lake City",
             stage="undetermined", entry_date="2017", focus="Healthcare & Bio",
             note="Care-coordination network for high-need patients, Salt Lake City; PointClickCare bought it in 2020 "
                  "(the firm's exit line). The firm labels a 2017 Growth entry; no source read names the round."))

# ---- Compaq
L.append(cls("compaq-computer-corporation", status="acquired", rng="below_1b", country="US", city="Houston",
             stage="undetermined", entry_date="1982", focus="Industrial & Robotics",
             note="Personal computers, Houston; IPO 1983, bought by HP in 2002. The firm's own card calls it one of "
                  "its most important bets (1982); no round is named."))

# ---- Convoke
L.append(cls("convoke", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_cite=POST("convoke-seed"), stage_conf="high", entry_date="2024", focus="Healthcare & Bio",
             flags=["city_unknown"],
             rounds=[rnd("2024", "Seed", None, None, True, POST("convoke-seed"), "firm")],
             note="AI software organising biopharma information. The firm's post of 2025-08-19: 'We're thrilled to be "
                  "partnering with Convoke in their seed funding round'; the card's year 2024 is the close year. "
                  "Neither the company's site nor the post places a city. " + GL))

# ---- CoreOS
L.append(cls("coreos", status="acquired", rng="below_1b", city="San Francisco", focus="Data Infrastructure",
             note="Container Linux and Kubernetes (Tectonic), San Francisco; Red Hat bought it for $250M in January "
                  "2018, aligned with the a16z, GV and YC rows."))

# ---- Corio
L.append(cls("corio", status="acquired", rng="below_1b", country="US", city="San Carlos", stage="undetermined",
             entry_date="1998", focus="SaaS",
             note="Application service provider, San Carlos; IPO 2000, bought by IBM in 2005. Ted Schlein a director "
                  "from September 1998 (its 2002 proxy); the firm's since-year is 1998 and no round is named."))

# ---- Corixa
L.append(cls("corixa", status="acquired", rng="below_1b", country="US", city="Seattle", stage="undetermined",
             focus="Healthcare & Bio",
             note="Vaccine adjuvants and immunotherapeutics, Seattle; GlaxoSmithKline bought it in 2005. Joe Lacob was "
                  "a director from 1994 and chairman to 1999 (its 2001 proxy); no round is named."))

# ---- Corthera
L.append(cls("corthera", status="acquired", rng="below_1b", country="US", city="San Mateo", focus="Healthcare & Bio",
             note="Relaxin for acute heart failure, San Mateo (the firm's 2008-11 listing); Novartis bought it in 2010 "
                  "(the archived page reads Acquired from 2012)."))

# ---- Corventis
L.append(cls("corventis", status="acquired", rng="below_1b", country="US", city="San Jose", stage="undetermined",
             entry_date="2005", focus="Healthcare & Bio",
             note="Wireless cardiac monitoring patches, San Jose (the firm's 2008-11 listing); Medtronic bought it in "
                  "2014 (the firm's exit line). Founded in 2005, the firm's since-year; no round is named."))

jl.write("j01b", L)
