import judge_lib as jl
from judge_lib import cls, rnd, SITE, ARCH, POST, FTS, NEWS

GP = "Graduation left for the graduation pass."
SA_MDB = "https://stockanalysis.com/stocks/mdb/market-cap/"
SA_MIRM = "https://stockanalysis.com/stocks/mirm/market-cap/"
SA_GLUE = "https://stockanalysis.com/stocks/glue/market-cap/"
SA_NKTR = "https://stockanalysis.com/stocks/nktr/market-cap/"
WV = {"valuation_range_source": "web_verified"}

L = []

# metabase
cb = NEWS("metabase", "Raises $13M - Crunchbase")
L.append(cls("metabase", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=cb, city="San Francisco", focus="Data Infrastructure",
             rounds=[rnd("2019-02-11", "undisclosed (Form D, $13.0M)", 13045420, "NEA", True, cb),
                     rnd("2019-04-24", "Series A", 8000000, None, None, NEWS("metabase", "Raises $8M in Series A")),
                     rnd("2021-08-19", "Series B", 30000000, "Insight Partners", None,
                         NEWS("metabase", "Raises $30M in Series B"))],
             note="Open-source BI, San Francisco. NEA led the round on the January 2019 Form D (Crunchbase News reads the "
                  "lead from the filing, Julia Schottenstein of NEA as director); FinSMEs reports it as the Series A and "
                  "the August 2021 round is the named Series B, so NEA entered at the Series A. Private, no mark near $1B."))

# metacrine
L.append(cls("metacrine", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=FTS("Metacrine", "S-1/A"), entry_date="2017-11", country="US", city="San Diego",
             focus="Healthcare & Bio",
             rounds=[rnd("2017-11", "Series B", 22000000, None, True, FTS("Metacrine", "S-1/A"), "filing"),
                     rnd("2018-06", "Series C", 65000000, None, True, FTS("Metacrine", "S-1/A"), "filing")],
             note="The S-1/A lists NEA's first purchase as $12.0M of the $22.0M Series B of November 2017 (none in the "
                  "Series A). Status stays acquired: Equillium's 2022 merger was cancelled, Metacrine sold its FXR program "
                  "to Organovo in March 2023 and filed a certificate of dissolution on 2023-03-24 (its 8-Ks)."))

# metromile
L.append(cls("metromile", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
             note="Pay-per-mile car insurer, San Francisco; listed via SPAC in 2021 and acquired by Lemonade in 2022. "
                  "Siblings (Felicis, First Round) agree on status and city."))

# metronome
tc = NEWS("metronome", "finds hit in AI")
L.append(cls("metronome", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=tc, entry_date="2024-01-31", country="US", city="San Francisco",
             focus="Fintech & Payments",
             rounds=[rnd("2024-01-31", "Series B", 43000000, "NEA", True, tc),
                     rnd("2025-02-25", "Series C", 50000000, None, None, NEWS("metronome", "raises $50 million Series C"))],
             note="Usage-based billing, San Francisco. TechCrunch: a $43M Series B led by NEA, Hilarie Koplow-McAdams to "
                  "the board (the firm's listing gives 2023, the close). Stripe completed the acquisition in January 2026 "
                  "(FX News Group); a16z and General Catalyst rows agree on acquired."))

# mighty-ai
L.append(cls("mighty-ai", status="acquired", rng="below_1b", stage="undetermined", entry_date="2014-12",
             country="US", city="Seattle", focus="AI & Applied AI",
             rounds=[rnd("2014-12-07", "undisclosed", 3250000, None, True, NEWS("mighty-ai", "raises $3.25M")),
                     rnd("2015-08-25", "undisclosed", 10000000, None, None, NEWS("mighty-ai", "raises $10M")),
                     rnd("2017-01-10", "undisclosed", 14000000, None, None, NEWS("mighty-ai", "Relaunches with $14M"))],
             note="Spare5, renamed Mighty AI in 2017 (training data for computer vision), Seattle. NEA entered the $3.25M "
                  "December 2014 round with Madrona and Foundry (GeekWire), which no visible source names; Uber acquired "
                  "the company in June 2019 (GeekWire). GV row agrees on acquired."))

# miim
L.append(cls("miim", status="private", rng="below_1b", stage="undetermined", entry_date="2015", country="US",
             city="Salt Lake City", focus="AI & Applied AI",
             note="MiiM (signal processing and AI for safety), aligned with the Balderton row on Salt Lake City. The firm "
                  "lists a 2015 first investment under an Early label; no source names the round."))

# millendo
gen = NEWS("millendo", "AstraZeneca Sells PCOS")
L.append(cls("millendo", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=gen, entry_date="2016-01-05", country="US", city="Ann Arbor",
             focus="Healthcare & Bio", flags=["model_disputes_source"],
             rounds=[rnd("2016-01-05", "Series B", 62000000, "NEA", True, gen)],
             note="GEN: the $62M Series B was led by NEA (a new investor; Carol Gallagher moved to represent NEA). Status "
                  "disputed from public: Millendo listed through its 2018 OvaScience merger, then merged into Tempest "
                  "Therapeutics in 2021, and the listed company is the separate tempest-therapeutics row."))

# millennial-media
mm = FTS("Millennial Media", "S-1/A")
L.append(cls("millennial-media", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=mm, entry_date="2009-11", city="Baltimore", focus="Media, Gaming & Advertising",
             rounds=[rnd("2009-11", "Series C", 16000000, None, True, mm, "filing"),
                     rnd("2010-12", "Series D", 27500000, None, None, mm, "filing")],
             note="The S-1/A: entities affiliated with NEA bought $12.0M of the $16.0M Series C in November 2009, NEA's "
                  "first round (Kerins a director since November 2009). Mobile ad network, Baltimore; acquired by AOL in 2015."))

# mimosa-networks
L.append(cls("mimosa-networks", status="acquired", rng="below_1b", city="Santa Clara", focus="Data Infrastructure",
             note="Wireless networking equipment; acquired by Airspan Networks in 2018 (the firm's exit line), then sold "
                  "by Airspan to Jio's Radisys in 2023."))

# mindtickle
L.append(cls("mindtickle", stage="undetermined", entry_date="2015", country="US", country_src="web_verified",
             country_cite="https://www.mindtickle.com/contact-us/", city="San Francisco", focus="SaaS",
             flags=["model_disputes_source"],
             rounds=[rnd("2017-12-13", "Series B", 27000000, "Canaan Partners", True,
                         NEWS("mindtickle", "Closes $27 Mn Series B"))],
             note="The IN country was a one-word name match: the company's own contact page gives its North America HQ "
                  "in San Francisco (Pune is the APAC HQ). NEA first invested in 2015 and was an existing investor in the "
                  "December 2017 Series B; no source names NEA's entry round. The Accel row carries San Francisco with IN "
                  "and should align."))

# minerva-surgical
L.append(cls("minerva-surgical", rng="below_1b", city="Santa Clara", focus="Healthcare & Bio",
             grad="graduated", grad_src="formd",
             note="Santa Clara per the S-1/A. The Form D sequence graduates the 2010 seed ($3.0M) at the $26.2M round of "
                  "2011. Status acquired: Accelmed took about 80% through 2023 private placements, and the company "
                  "delisted from Nasdaq in December 2023 and deregistered in January 2024 (its 8-Ks)."))

# minimum
bk = NEWS("minimum", "UK-based Minimum")
L.append(cls("minimum", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("minimum"), entry_date="2022", country="GB",
             country_src="web_verified", country_cite=bk, city="London", focus="Climate & Energy",
             note="Carbon accounting software, London (BetaKit: UK-based, the London office stays). The firm's own label "
                  "is Seed, 2022. Novisto acquired it on 2026-03-31, fresher than the YC row's private. " + GP))

# mirna-therapeutics
L.append(cls("mirna-therapeutics", status="acquired", rng="below_1b", city="Austin", focus="Healthcare & Bio",
             flags=["model_disputes_source"],
             note="Status disputed from public: Mirna, Austin, merged with Synlogic in 2017 and the combined listed "
                  "company is the separate synlogic row; the float on this row is Synlogic's."))

# mirum-pharmaceuticals
mi = FTS("Mirum", "S-1/A")
L.append(cls("mirum-pharmaceuticals", rng="1b_plus", usd=5620000000, val_src="web_verified", val_cite=SA_MIRM,
             asof="2026-09-30", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=mi,
             entry_date="2018-11", city="Foster City", focus="Healthcare & Bio", extra=WV,
             rounds=[rnd("2018-11", "Series A", 120000000, None, True, mi, "filing")],
             note="Market cap $5.62B on 2026-09-30 (stockanalysis). The S-1/A: NEA bought $30.0M of the Series A, initial "
                  "closing November 2018, so the entry date moves from the 2020 Form D to 2018-11 (same stage)."))

# mission-critical-software
L.append(cls("mission-critical-software", status="acquired", rng="below_1b", stage="undetermined", entry_date="1996",
             country="US", city="Houston", focus="Data Infrastructure",
             note="Windows NT systems management software, Houston; IPO 1999, merged into NetIQ in 2000 (the firm's exit "
                  "line). NEA's 1996 round is not named in any source on disk."))

# missmalini
vc = NEWS("missmalini", "Cash-strapped Good Glamm")
L.append(cls("missmalini", status="acquired", rng="below_1b", stage="undetermined", entry_date="2017", country="IN",
             country_src="web_verified", country_cite=vc, city="Mumbai", focus="Media, Gaming & Advertising",
             note="Indian digital media network, Mumbai. Good Glamm Group acquired it in late 2021 and sold it to "
                  "Creativefuel in 2025 (VCCircle). NEA's 2017 round is not named."))

# mnectar
L.append(cls("mnectar", status="unknown", rng="below_1b", city="San Francisco", focus="Media, Gaming & Advertising",
             note="Playable-ad streaming, San Francisco. No news after 2016 and the firm's listing dropped after 2021 "
                  "(last shown Current, private); its site does not resolve, so its fate is not established."))

# mobius-management-systems
L.append(cls("mobius-management-systems", status="acquired", rng="below_1b", stage="undetermined", entry_date="1997",
             country="US", city="Rye", focus="SaaS",
             note="Document archiving and content management software, Rye NY; IPO 1998, acquired by Allen Systems "
                  "Group in 2007 (the firm's exit line). NEA's 1997 round is not named."))

# moda-operandi
L.append(cls("moda-operandi", status="private", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             note="Luxury pre-order e-commerce, New York; still raising privately in 2024 (WWD). No priced mark at $1B."))

# modyfi
pr = NEWS("modyfi", "seed funding led by NEA")
L.append(cls("modyfi", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=pr, entry_date="2023-08-23", city="Los Angeles", city_src="formd_address", focus="SaaS",
             rounds=[rnd("2023-08-23", "Seed", 7000000, "NEA", True, pr)],
             note="AI-native design tool. PR Newswire: a $7M seed led by NEA (the firm's listing says Seed, 2022, the "
                  "close; the 2024-04 Form D date on the row was a later filing). Figma acquired Modyfi in May 2025 and "
                  "the service closed in June (Design Compass). " + GP))

# mojo-vision
L.append(cls("mojo-vision", status="private", rng="below_1b", stage="undetermined", entry_date="2016", country="US",
             city="Saratoga", focus="Industrial & Robotics",
             rounds=[rnd("2023-10-12", "Series A (after the pivot)", 43500000, None, None,
                         NEWS("mojo-vision", "Series A hits $43.5M")),
                     rnd("2025-09-04", "Series B Prime", 75000000, None, None, NEWS("mojo-vision", "Series B Prime"))],
             note="Smart contact lens company turned micro-LED display maker, Saratoga CA. NEA first invested in 2016 "
                  "(Greg Papadopoulos on the board); no source names that round. No priced mark at $1B."))

# moneytap
lm = NEWS("moneytap", "raises $12.3 million from Sequoia")
L.append(cls("moneytap", status="private", rng="below_1b", stage="undetermined", entry_date="2016", country="IN",
             country_src="web_verified", country_cite=NEWS("moneytap", "Peak XV-backed MoneyTap"), city="Bangalore",
             focus="Fintech & Payments",
             rounds=[rnd("2017-06-15", "undisclosed", 12300000, "Sequoia Capital India", True, lm)],
             note="App-based credit lines, Bangalore; now operating as Freo (VCCircle 2024). NEA first invested in 2016 "
                  "and is named an existing investor in the June 2017 $12.3M round (Livemint); its entry round is not named."))

# mongodb
L.append(cls("mongodb", rng="10b_plus", usd=28380000000, val_src="web_verified", val_cite=SA_MDB, asof="2026-09-30",
             entry_date="2012", city="New York", focus="Data Infrastructure", extra=WV,
             note="Market cap $28.38B on 2026-09-30 (stockanalysis), fresher than the Sequoia and USV marks. Entry date "
                  "set to the firm's own first-invested year, 2012 (a 10gen round), not the 2013 Form D; Growth either way."))

# monte-rosa-therapeutics
mr = FTS("Monte Rosa", "DRS")
L.append(cls("monte-rosa-therapeutics", rng="1b_plus", usd=1020000000, val_src="web_verified", val_cite=SA_GLUE,
             asof="2026-09-30", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=mr,
             entry_date="2020-04", city="Boston", focus="Healthcare & Bio", flags=["stage_disputes_band"], extra=WV,
             rounds=[rnd("2020-04", "Series A-2", 12500000, "NEA", True, mr, "filing"),
                     ],
             note="The draft S-1: NEA bought the whole $12.5M Series A-2 in April 2020, before the September 2020 Series B "
                  "the Form D band read (and the firm's Growth label). Market cap $1.02B on 2026-09-30 (stockanalysis), "
                  "within 5% of the band edge; the GV row's $999M of 2026-09-28 is two days older."))

# moonpay
cz = NEWS("moonpay", "NEA Joins")
L.append(cls("moonpay", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=cz,
             entry_date="2021-11-22", city="Miami", focus="Crypto & Web3", flags=["stage_disputes_band"],
             rounds=[rnd("2021-11-22", "Series A", 555000000, "Tiger Global; Coatue", True, cz)],
             note="citybiz: NEA joined the $555M Series A at $3.4B, MoonPay's first outside round, so the documented round "
                  "overrides the firm's Growth label. Miami, aligned with the Coatue, Thrive and Tiger rows."))

# more-health
L.append(cls("more-health", status="private", rng="below_1b", city="San Mateo", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Cross-border virtual second opinions, first for Chinese patients (NEA's Xiaodong Jiang on the Form D). "
                  "The firm still lists it as private. " + GP))

# motion-computing
L.append(cls("motion-computing", status="acquired", rng="below_1b", stage="undetermined", entry_date="2003",
             country="US", city="Austin", focus="Industrial & Robotics",
             note="Rugged tablet PCs, Austin; acquired by Xplore Technologies in 2015, as the IVP row has it. NEA's round "
                  "is not named; the entry date is the firm's own year, 2003, not the 2009 Form D."))

# motricity
L.append(cls("motricity", rng="below_1b", stage="undetermined", entry_date="2004", country="US", city="Bellevue",
             focus="Media, Gaming & Advertising",
             note="Mobile content platform, Bellevue WA; IPO 2010, renamed Voltari in 2013 and taken private by Carl Icahn "
                  "in 2019, as the TCV row has it. The S-1 shows NEA 10 as an 8% holder and Suzanne King a director since "
                  "2004 but names no NEA series."))

# motus-therapeutics
L.append(cls("motus-therapeutics", status="acquired", rng="below_1b", stage="undetermined", entry_date="2010",
             country="US", city="Boston", focus="Healthcare & Bio",
             note="The GI subsidiary of Rhythm (relamorelin), acquired by Allergan on its option in October 2016 (GEN). The "
                  "firm's 2010 year is its Rhythm-era entry; no round is named. Not Motus GI Holdings, a different company "
                  "in the full-text hits."))

# movius-interactive-corporation
L.append(cls("movius-interactive-corporation", status="private", rng="below_1b", stage="undetermined",
             entry_date="2006", city="Duluth", city_src="formd_address", focus="SaaS",
             note="Mobile communications software; EDGAR's former name IP Unity Glenayre shows the 2007 combination of "
                  "IP Unity with Glenayre's messaging business (a portfolio company buying a unit, not an NEA acquisition "
                  "vehicle). NEA's 2006 round is not named; the entry date is the firm's year, not the 2013 Form D."))

# moximed
L.append(cls("moximed", status="private", rng="below_1b", stage="undetermined", entry_date="2007", city="Fremont",
             focus="Healthcare & Bio",
             rounds=[rnd("2022-08-16", "undisclosed", 40000000, None, None, NEWS("moximed", "Moximed raises $40M"))],
             note="Implantable knee shock absorber (FDA clearance 2023), Fremont. Spun out with ExploraMed and NEA (the "
                  "firm's own 2021 post); NEA's 2007 round is not named, and the 2009 Form D is not the entry."))

# mulesoft
ms = FTS("MULESOFT", "S-1/A")
L.append(cls("mulesoft", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ms,
             entry_date="2013-02", city="San Francisco", focus="DevTools & APIs",
             rounds=[rnd("2013-02", "Series E", 37000000, "NEA", True, ms, "filing")],
             note="The S-1/A: entities affiliated with NEA bought $25.0M of the $37.0M Series E (February to March 2013), "
                  "the round the firm's April 2013 post announces. IPO 2017, acquired by Salesforce in 2018; siblings agree."))

# myfit
L.append(cls("myfit", status="acquired", rng="below_1b", stage="undetermined", entry_date="2009", country="US",
             focus="Consumer & Marketplaces", flags=["city_unknown"],
             note="College admissions prediction tool, acquired by Naviance (the firm's exit line). No news, filing or site "
                  "places the company; NEA's 2009 round is not named."))

# myogen
my = FTS("MYOGEN", "S-1/A")
L.append(cls("myogen", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=my, entry_date="1999-11", country="US", city="Westminster", focus="Healthcare & Bio",
             rounds=[rnd("1998-05", "Series A", None, None, False, my, "filing"),
                     rnd("1999-11", "Series C", None, None, True, my, "filing"),
                     rnd("2001-08", "Series D", None, None, True, my, "filing")],
             note="The S-1/A's certain-transactions table shows NEA in the Series C (November to December 1999) and D, not "
                  "the Series A; Van Bladel a director since November 1999. Westminster CO; IPO 2003, acquired by Gilead in 2006."))

# mythic
sa = NEWS("mythic", "Compute-in-memory chip startup")
L.append(cls("mythic", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=sa, entry_date="2025-12-17", country="US", city="Austin", focus="Industrial & Robotics",
             rounds=[rnd("2025-12-17", "undisclosed", 125000000, "DCVC", True, sa)],
             note="Analog AI inference chips. SiliconANGLE: NEA joined the $125M round led by DCVC in December 2025, after "
                  "the company's earlier A to C rounds, so a Growth entry. Momentum check 2026-09-30: no valuation "
                  "reported for the round. City aligned with the Lux row."))

# naaptol
L.append(cls("naaptol", status="private", rng="below_1b", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("naaptol"), entry_date="2011", country="IN", country_src="web_verified",
             country_cite=NEWS("naaptol", "Rs136 crore from Japan"), city="Mumbai", focus="Consumer & Marketplaces",
             note="TV and online shopping, Mumbai. The firm's own label is Growth, 2011; Livemint calls the 2015 Mitsui round "
                  "the company's third, with NEA an existing investor, so NEA's 2011 round was the second."))

# namespace
nb = "https://namespace.so/blog/series-a"
L.append(cls("namespace", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
             stage_conf="medium", stage_cite=POST("namespace-cicd"), entry_date="2026-03-23", country="US",
             focus="DevTools & APIs", flags=["city_unknown"],
             rounds=[rnd("2026-03-23", "Seed and Series A (combined $23M)", 23000000, "NEA", True, nb, "company")],
             note="CI and build compute for developers and agents. The firm's post: NEA led the Series A (listing year 2025); "
                  "the company's post totals $23M of Seed and Series A 'led by NEA', which leaves open whether NEA also "
                  "led the seed. Only a Delaware registered-agent address is known. Momentum check 2026-09-30: no $1B+ round."))

# narmi
L.append(cls("narmi", status="private", rng="below_1b", stage="Series A", stage_src="first_party", stage_conf="high",
             stage_cite=POST("announcing-our-investment-in-narmi"), entry_date="2021-02-02", city="New York",
             focus="Fintech & Payments", flags=["stage_disputes_band"],
             note="The firm's own post announcing its investment: 'NEA is thrilled to lead their Series A financing' "
                  "(February 2021), overriding the Form D band's Growth (the 2022 Series B filing) and the firm's Growth label."))

# nefeli-networks
L.append(cls("nefeli-networks", status="acquired", rng="below_1b", city="Berkeley", focus="Data Infrastructure",
             note="Cloud networking (Scott Shenker), Berkeley; Cloudflare acquired it in March 2024 (SiliconANGLE)."))

# nektar-therapeutics
L.append(cls("nektar-therapeutics", rng="1b_plus", usd=2070000000, val_src="web_verified", val_cite=SA_NKTR,
             asof="2026-09-30", stage="undetermined", entry_date="2011", city="San Francisco", focus="Healthcare & Bio",
             extra=WV,
             note="Market cap $2.07B on 2026-09-30 (stockanalysis), replacing the older float. The firm labels the 2011 "
                  "investment Public/PIPES into a long-listed company: the X1 class, and a PIPE names no round."))

# nellcor
L.append(cls("nellcor", status="acquired", rng="below_1b", stage="undetermined", entry_date="1990", country="US",
             city="Pleasanton", focus="Healthcare & Bio",
             note="Pulse oximetry maker; merged with Puritan-Bennett in 1995, later Mallinckrodt, Tyco and Covidien (the "
                  "firm's exit line). The firm labels the 1990 investment Public/PIPES: the X1 class, no round named."))

# neo-cybernetica
nc = NEWS("neo-cybernetica", "Secures $30M Seed")
L.append(cls("neo-cybernetica", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=nc, entry_date="2022-02-09", country="US", focus="AI & Applied AI",
             flags=["city_unknown"], rounds=[rnd("2022-02-09", "Seed", 30000000, "NEA", True, nc)],
             note="Stealth deep tech company of DataRobot founder Jeremy Achin; PR Newswire: a $30M seed led by NEA, Tony "
                  "Florence to the board. No release places it. Momentum check 2026-09-30: no later round reported. " + GP))

# neoteris
L.append(cls("neoteris", status="acquired", rng="below_1b", stage="undetermined", entry_date="2002", country="US",
             city="Sunnyvale", focus="Security",
             note="SSL VPN appliances; NetScreen agreed to buy it for $265M in October 2003 (The Register). NEA's 2002 round "
                  "(Scott Sandell on the board) is not named. City aligned with the Battery row."))

# neotract
L.append(cls("neotract", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=ARCH("neotract"), entry_date="2005", city="Pleasanton", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             note="UroLift maker, Pleasanton; acquired by Teleflex in 2017. The firm's archived listing labels the 2005 "
                  "investment seed (NeoTract was spun out with ExploraMed that year); the band's Growth read the 2009 Form D, "
                  "four years after the entry. " + GP))

# netcitadel
L.append(cls("netcitadel", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011", country="US",
             focus="Security", flags=["city_unknown"],
             note="Automated security incident response; Proofpoint bought the 'Silicon Valley-based' company for about "
                  "$24M in May 2014 (Proofpoint's release). No source gives its city or NEA's 2011 round."))

jl.write("c7a", L)
