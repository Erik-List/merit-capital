import judge_lib as jl
from judge_lib import cls, rnd, verdict, SITE, POST, FTS, NEWS, W

GP = "Graduation left for the graduation pass."
WV = {"valuation_range_source": "web_verified"}
SA = "https://stockanalysis.com/stocks/{}/market-cap/"

L = []

# netiq: D8, stock received as sale consideration for Mission Critical Software
L.append(verdict("netiq", "not_member",
                 "D8 (sale consideration): NEA's NetIQ stock came from NetIQ's 2000 all-stock merger with Mission "
                 "Critical Software, NEA's 1996 portfolio company (the member row); the firm lists NetIQ with a 2000 "
                 "first year, the merger year, and NetIQ's 10-K405 says Scott Sandell had been a Mission Critical "
                 "director since September 1996. Mission Critical Software is the member.",
                 ec="web", conf="medium", cite=FTS("NETIQ", "10-K405")))

# netsolve
L.append(cls("netsolve", status="acquired", rng="below_1b", stage="undetermined", entry_date="1988", country="US",
             city="Austin", focus="Data Infrastructure",
             note="Outsourced network management, Austin; IPO 1999, acquired by Cisco in 2004 (the firm's exit line). NEA "
                  "IV held 24.7% (2001 proxy); the 1988 round is not named."))

# neuehealth
L.append(cls("neuehealth", rng="below_1b", stage="undetermined", entry_date="2016", country="US", city="Minneapolis",
             focus="Healthcare & Bio",
             note="Bright Health, renamed NeueHealth; listed 2021. NEA and a consortium took it private, closing in "
                  "October 2025 (Fierce Healthcare), hence acquired. NEA's 2016 entry round is not cited."))

# neural-magic
fs = NEWS("neural-magic", "Raises $30M in Series A")
L.append(cls("neural-magic", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("neural-magic"), entry_date="2018", country="US", city="Somerville",
             focus="AI & Applied AI", grad="graduated", grad_src="web_verified", grad_cite=fs, grad_conf="high",
             rounds=[rnd("2021-10-05", "Series A", 30000000, None, None, fs)],
             note="CPU inference software from MIT CSAIL, Somerville (as the a16z row has it). The firm's own label is "
                  "Seed, 2018; the named $30M Series A of October 2021 (FinSMEs) graduates it. Acquired by Red Hat in "
                  "January 2025 (the firm's exit line)."))

# neuralieve
L.append(cls("neuralieve", status="private", rng="below_1b", stage="undetermined", entry_date="2002", country="US",
             city="Baltimore", city_src="web_verified", focus="Healthcare & Bio",
             note="Renamed eNeura (sTMS migraine device); 'Baltimore-based eNeura' (Baltimore Sun, 2018) and its site still "
                  "sells the therapy. NEA's 2002 round is not named."))

# neuropace
L.append(cls("neuropace", rng="below_1b", usd=472650000, val_src="web_verified", val_cite=SA.format("npce"),
             asof="2026-09-30", stage="undetermined", entry_date="2000", city="Mountain View",
             focus="Healthcare & Bio", flags=["stage_disputes_band"], extra=WV,
             note="Market cap $472.65M on 2026-09-30 (stockanalysis). The band's Growth read a 2011 Form D, eleven "
                  "years after the firm's own 2000 first investment; that round is not named, so undetermined."))

# neutral-tandem
L.append(cls("neutral-tandem", rng="below_1b", stage="undetermined", entry_date="2003", country="US", city="Chicago",
             focus="Data Infrastructure",
             note="Tandem voice interconnection, Chicago; IPO 2007, renamed Inteliquent, taken private by GTCR in 2017 and "
                  "sold to Sinch in 2021. NEA 10 signed the 2004 voting agreement; its 2003 round is not named."))

# nevro
L.append(cls("nevro", rng="below_1b", stage="undetermined", entry_date="2013", country="US", city="Redwood City",
             focus="Healthcare & Bio",
             note="High-frequency spinal cord stimulation, Redwood City; IPO 2014, acquired by Globus Medical in 2025. "
                  "NEA Ventures 2013 signed the March 2013 rights agreement; the round is not named in what was read."))

# new-wave-foods
L.append(cls("new-wave-foods", status="acquired", rng="below_1b", city="Stamford", city_src="formd_address",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-01-07", "Series A", 18000000, None, True,
                         NEWS("new-wave-foods", "Raises $18 Million Series A"))],
             note="Plant-based shrimp. It ceased operations in February 2024 unable to pay its debts (AgFunderNews) and "
                  "Big Idea Ventures' Bayou Best Foods bought its IP in July 2024: read as acquired with a successor, "
                  "the Cherry insolvency-sale rule. The firm's own post calls NEA's investment the Series A."))

# newbrandanalytics
L.append(cls("newbrandanalytics", status="unknown", rng="below_1b", city="Washington", focus="SaaS",
             note="Social-feedback analytics for restaurants and retail, Washington DC. The firm listed it through 2020 "
                  "as private; no later news or filing establishes its fate."))

# newglobe
L.append(cls("newglobe", status="private", rng="below_1b", city="Nairobi", focus="Consumer & Marketplaces",
             note="Bridge International Academies, renamed NewGlobe; runs government school programs in Nigeria and "
                  "Kenya (2024 press). City aligned with the Khosla row."))

# newscale
L.append(cls("newscale", status="acquired", rng="below_1b", stage="undetermined", entry_date="2001", country="US",
             city="San Mateo", focus="SaaS",
             note="IT service catalog software, San Mateo; acquired by Cisco in 2011 (the firm's exit line), as the Menlo "
                  "row has it. NEA's 2001 round is not named; the 2009 Form D is not the entry."))

# nexchem
L.append(cls("nexchem", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("nexchem"), entry_date="2009", country="CN",
             country_src="web_verified", country_cite=SITE("nexchem"), focus="Healthcare & Bio",
             flags=["city_unknown"],
             note="Chinese maker of active pharmaceutical ingredients, per the firm's own listing (Growth, 2009). No news "
                  "or filing places its city."))

# neximmune
L.append(cls("neximmune", status="defunct", rng="below_1b", stage="undetermined", city="Gaithersburg",
             focus="Healthcare & Bio", flags=["model_disputes_source"],
             note="Status disputed from acquired: NexImmune, Gaithersburg, delisted from Nasdaq in July 2024 and moved "
                  "forward with its wind-down and dissolution (Washington Business Journal, 2024-08-30); no buyer. NEA's "
                  "2014 round is not named."))

# nexo
ws = NEWS("nexo", "Wilson Sonsini Advises Versant")
L.append(cls("nexo", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ws, entry_date="2023-07-26", city="Littleton", city_src="formd_address",
             focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2023-07-26", "Series A", 60000000, "Versant Ventures; NEA", True, ws)],
             note="Nexo Therapeutics launched with a $60M Series A from Versant and NEA (Wilson Sonsini, advising both), "
                  "so the band's Growth on the 2022 filing is replaced (the firm's year 2022 is the first close)."))

# nextnav
L.append(cls("nextnav", rng="1b_plus", usd=2460000000, val_src="web_verified", val_cite=SA.format("nn"),
             asof="2026-09-30", city="McLean", focus="Data Infrastructure", extra=WV,
             note="Terrestrial 3D positioning network, McLean VA. Market cap $2.46B on 2026-09-30 (stockanalysis)."))

# ng-cash
cz = NEWS("ng-cash", "NEA Leads $26.5 Million")
L.append(cls("ng-cash", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=cz, entry_date="2025-08-06", country="BR", country_src="web_verified",
             country_cite=cz, city="Rio de Janeiro", focus="Fintech & Payments",
             rounds=[rnd("2025-08-06", "Series B", 26500000, "NEA", True, cz)],
             note="Gen Z financial app in Brazil. citybiz: NEA led the $26.5M Series B (after a 2022 seed and a 2024 "
                  "Series A, per the a16z row). City aligned with the a16z row. Momentum check 2026-09-30: no $1B+ round."))

# nginx
L.append(cls("nginx", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=W("Nginx"), entry_date="2013-10", city="San Francisco", focus="Data Infrastructure",
             flags=["stage_disputes_band"],
             note="Wikipedia: the $10M October 2013 round NEA led was the Series B (NEA's post announces its investment "
                  "that month), so the band's Series A is replaced. Acquired by F5 Networks in 2019."))

# niara
L.append(cls("niara", status="acquired", rng="below_1b", stage="undetermined", entry_date="2013", country="US",
             city="Sunnyvale", focus="Security",
             note="Behavioral security analytics, Sunnyvale; acquired by Hewlett Packard Enterprise (Aruba) in 2017, the "
                  "firm's exit line. NEA's 2013 round is not named."))

# nicira
L.append(cls("nicira", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011", city="Palo Alto",
             focus="Data Infrastructure",
             note="Software-defined networking, Palo Alto; acquired by VMware in 2012. NEA's 2011 round is not named."))

# nightstar
f1 = FTS("Nightstar Therapeutics Ltd", "F-1")
L.append(cls("nightstar", rng="below_1b", stage="undetermined", entry_date="2015", country="GB",
             country_src="web_verified", country_cite=f1, city="London", focus="Healthcare & Bio",
             note="Retinal gene therapy, principal offices in London (F-1); IPO 2017, acquired by Biogen in 2019. David "
                  "Mott of NEA a director since August 2015; the round NEA entered is not named in what was read."))

# nimble-collective
L.append(cls("nimble-collective", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("nimble-collective"), entry_date="2015", city="Mountain View",
             focus="SaaS",
             note="Cloud animation studio platform, Mountain View. The firm's own label is Seed, 2015 (the 2018 Form D is "
                  "a later round); its exit line names Amazon Web Services, which built Nimble Studio on it. " + GP))

# ninjaone
cb = NEWS("ninjaone", "Reaches $12.3 Billion Valuation Following $400")
L.append(cls("ninjaone", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=cb,
             entry_date="2026-06-09", city="Austin", focus="SaaS",
             rounds=[rnd("2026-06-09", "Series C extension", 400000000, None, True, cb)],
             note="citybiz lists NEA among the investors in the $400M Series C extension at $12.3B (June 2026), the "
                  "firm's 2026 entry. Austin, as the Coatue, ICONIQ and Sequoia rows have it."))

# nitra
pr = NEWS("nitra", "Nitra Raises $62 Million")
py = NEWS("nitra", "Nitra Secures $187 Million")
L.append(cls("nitra", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="medium",
             stage_cite=pr, entry_date="2022-08-23", country="US", city="New York", focus="Fintech & Payments",
             grad="graduated", grad_src="web_verified", grad_cite=py, grad_conf="high",
             rounds=[rnd("2022-08-23", "Seed (equity and debt)", 62000000, None, True, pr),
                     rnd("2025-08", "Series A", 22000000, None, None, py),
                     rnd("2026-03-10", "Series B", 50000000, None, None, py)],
             note="Healthcare-practice fintech, New York. NEA joined the August 2022 $62M equity-and-debt raise; the "
                  "a16z row and PYMNTS (a 'previously unannounced $22 million Series A' in August 2025) make it the seed, "
                  "and the named Series A graduates it. Momentum check 2026-09-30: no valuation reported."))

# nkarta-therapeutics
nk = FTS("Nkarta", "S-1/A")
L.append(cls("nkarta-therapeutics", rng="below_1b", usd=186580000, val_src="web_verified", val_cite=SA.format("nktx"),
             asof="2026-09-30", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=nk,
             entry_date="2016", city="South San Francisco", focus="Healthcare & Bio", flags=["stage_disputes_band"],
             extra=WV,
             note="The S-1/A: NEA 15 held Series A through Battersea Biotech (distributed to it in December 2017), and Ali "
                  "Behbahani sat on the board from October 2015, so NEA entered at the Series A, not the 2019 Series B the "
                  "band read. Market cap $186.58M on 2026-09-30 (stockanalysis)."))

# nodar
fn = NEWS("nodar", "Nodar Raises $12M in Series A")
L.append(cls("nodar", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=fn, entry_date="2022-04", city="Somerville", focus="Industrial & Robotics",
             rounds=[rnd("2022-04-13", "Series A", 12000000, None, True, fn)],
             note="Stereo 3D vision for vehicles, Somerville MA. FinSMEs names the $12M Series A of April 2022; its Form D "
                  "carries NEA's Greg Papadopoulos as director and the firm's year is 2022."))

# nordsense
L.append(cls("nordsense", status="private", rng="below_1b", stage="undetermined", entry_date="2017", country="US",
             focus="Industrial & Robotics", flags=["city_unknown"],
             note="Smart waste-bin sensors (San Francisco pilot 2019, Ingram Micro partnership 2024). No source read "
                  "places its headquarters; NEA's 2017 round is not named."))

# nova-fertility
et = NEWS("nova-fertility", "TPG-backed AHH buys Nova")
L.append(cls("nova-fertility", status="acquired", rng="below_1b", stage="undetermined", entry_date="2010",
             country="IN", country_src="web_verified", country_cite=et, focus="Healthcare & Bio",
             flags=["city_unknown"],
             note="Nova IVI Fertility, an Indian fertility chain; TPG-backed Asia Healthcare Holdings acquired it in May "
                  "2019 (Economic Times). Its head-office city is not stated in what was read; NEA's 2010 round is not named."))

# novacept
L.append(cls("novacept", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("novacept"), entry_date="2002", country="US", city="Palo Alto",
             focus="Healthcare & Bio",
             note="Women's health devices (NovaSure), Palo Alto; acquired by Cytyc in 2004. The firm's own label is Growth, "
                  "2002, and its 2004 S-1 shows NEA only in the latest preferred series."))

# novast-holdings-limited
L.append(cls("novast-holdings-limited", status="private", rng="below_1b", stage="undetermined", entry_date="2008",
             country="CN", country_src="web_verified",
             country_cite=NEWS("novast-holdings-limited", "Lilly Expands Strategic Partnership"), city="Nantong",
             focus="Healthcare & Bio",
             note="Chinese specialty generics maker (Novast Laboratories, Nantong). A Dealroom note of 2026-09-25 reports "
                  "an IPO priced to raise about $140M, not confirmed listed as of 2026-09-30: re-check status and cap."))

# novatium
L.append(cls("novatium", status="unknown", rng="below_1b", stage="undetermined", entry_date="2007", country="IN",
             country_src="web_verified", country_cite=NEWS("novatium", "Novatium offers cloud-based"),
             focus="Data Infrastructure", flags=["city_unknown"],
             note="Cloud-hosted netbooks and thin clients for India (Liliputing, 2010); confirms the IN claim. No later news "
                  "establishes its fate or city."))

# nth-round
L.append(cls("nth-round", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_conf="medium", stage_cite=SITE("nth-round"), entry_date="2018", country="US",
             focus="Fintech & Payments", flags=["city_unknown"],
             note="Private-share trading platform. The firm's own label is Seed, 2018; no source read places the "
                  "company. " + GP))

# nuelle
L.append(cls("nuelle", status="acquired", rng="below_1b", city="Mountain View", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Women's sexual wellness device (Fiera); Aytu BioScience acquired Nuelle in May 2017 (PR Newswire)."))

# nuvolo
L.append(cls("nuvolo", status="acquired", rng="below_1b", stage="undetermined", entry_date="2015", country="US",
             city="Wellesley", focus="SaaS",
             note="Enterprise asset and workplace software on ServiceNow; Trane Technologies completed the acquisition in "
                  "November 2023 for about $440M. City aligned with the Insight row; NEA's 2015 round is not named."))

# oanda
L.append(cls("oanda", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("oanda"), entry_date="2007", country="US", city="New York", focus="Fintech & Payments",
             note="Online FX broker, New York. The firm's own label is Growth, 2007; Wikipedia: a group led by NEA invested "
                  "in 2007 after Index in 2005. Sold to CVC in 2018 and to FTMO, closing in 2025."))

# obseva
ob = FTS("ObsEva", "DRS/A")
L.append(cls("obseva", status="defunct", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=ob, entry_date="2015-11", country="CH", country_src="web_verified",
             country_cite=POST("looking-beyond-the-numbers"), city="Geneva", focus="Healthcare & Bio",
             flags=["model_disputes_source"],
             rounds=[rnd("2015-11-19", "Series B", None, None, True, ob, "filing")],
             note="The draft F-1: NEA 15 bought $14.9M of the November 2015 Series B, the 'new investment' of the firm's "
                  "own post on a Swiss company. Status disputed from acquired: ObsEva sold program rights, then wound down "
                  "and laid off all staff in February 2024 (Fierce Biotech) and left the SIX."))

# oculeve
L.append(cls("oculeve", status="acquired", rng="below_1b", city="South San Francisco", focus="Healthcare & Bio",
             note="Dry eye neurostimulation device; acquired by Allergan in 2015 (the firm's exit line)."))

# ohai
L.append(cls("ohai", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("ohai"), entry_date="2021", city="Pembroke", city_src="formd_address",
             focus="AI & Applied AI",
             note="AI household assistant from Care.com founder Sheila Marcelo. The firm's own label is Seed, 2021 (Tony "
                  "Florence); the 2023 Form D date on the row was a later filing. Momentum check 2026-09-30: an August "
                  "2025 strategic round led by Muse Capital, no $1B+ mark. " + GP))

# olio-devices
L.append(cls("olio-devices", status="acquired", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             note="Luxury smartwatch maker, San Francisco; acquired by Flex, per the firm's archived exit line."))

# omada-health
tc = "https://techcrunch.com/2014/04/09/omada-health-raises-23m-series-b-led-by-andreessen-horowitz-for-digital-health-that-actually-works/"
L.append(cls("omada-health", rng="1b_plus", usd=1270000000, val_src="web_verified", val_cite=SA.format("omda"),
             asof="2026-09-30", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=SITE("omada-health"), entry_date="2011", country="US", city="San Francisco",
             focus="Healthcare & Bio", grad="graduated", grad_src="web_verified", grad_cite=tc, grad_conf="high",
             extra=WV, rounds=[rnd("2014-04-09", "Series B", 23000000, "Andreessen Horowitz", None, tc)],
             note="The firm's own label is Seed, 2011; the named $23M Series B of April 2014 (TechCrunch) graduates it. "
                  "Market cap $1.27B on 2026-09-30 (stockanalysis), fresher than the a16z and Lux marks."))

# omio
L.append(cls("omio", status="private", rng="below_1b", stage="undetermined", entry_date="2014",
             country="DE", country_src="web_verified", country_cite=W("Omio"), city="Berlin",
             focus="Consumer & Marketplaces",
             note="GoEuro, renamed Omio in 2019; Wikipedia: headquartered in Berlin, NEA among its investors. NEA's 2014 "
                  "round precedes the December 2015 Series B the Atomico row cites, and is not named."))

# omthera-pharmaceuticals
L.append(cls("omthera-pharmaceuticals", status="acquired", rng="below_1b", city="Princeton", focus="Healthcare & Bio",
             note="Omega-3 dyslipidemia drug; IPO April 2013, acquired by AstraZeneca in 2013 (the firm's exit line)."))

# one-concern
L.append(cls("one-concern", status="private", rng="below_1b", city="Palo Alto", city_src="formd_address",
             focus="AI & Applied AI",
             note="AI disaster and climate resilience modeling; the firm still lists it as private. No priced mark at $1B."))

# onshape
L.append(cls("onshape", status="acquired", rng="below_1b", city="Cambridge", focus="SaaS",
             note="Cloud CAD; acquired by PTC in 2019 (the firm's exit line). City aligned with the a16z row."))

# onstream
L.append(cls("onstream", status="acquired", rng="below_1b", stage="undetermined", entry_date="1991", country="US",
             focus="Data Infrastructure", flags=["city_unknown"],
             note="High-speed networking equipment, acquired by 3Com (the firm's exit line). No source read places it or "
                  "names NEA's 1991 round."))

jl.write("c7b", L)
