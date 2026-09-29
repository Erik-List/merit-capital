"""PRO-75 GV grind, queue batch 6 (judge j6): the 45 member rows gravity-sketch .. ionq.

Research order per row: the firm's own sources (posts, case study, /ai dates, archive capture dates), S-1 exhibits and
related-party tables (FTS), Form D ladders, then press (Google News via nq.py, TechCrunch's and Crunchbase News's own
search), Wikipedia, company releases. Where no source read names the round GV entered, the stage is undetermined and
the rounds found are kept. Public marks are stockanalysis.com closes of 2026-09-28."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, CASE, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.CASE, jl.SITE,
                                                           jl.ARCH, jl.W, jl.NEWS, jl.FTS)
L = []
CHECK = "2026-09-28"
VR = {"valuation_range_source": "web_verified"}

# ---------------------------------------------------------------- gravity-sketch
TC22 = NEWS("gravity-sketch", "Gravity Sketch raises $33M")
TC20 = "https://techcrunch.com/2020/09/16/gravity-sketch-scores-3-7m-seed-for-its-vr-based-product-design-and-collaboration-platform/"
L.append(cls("gravity-sketch", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=TC22, city="London", city_src="web_verified", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC22, entry_date="2022-04-19",
             note="3D design and collaboration platform (London). Kindred Capital led the $3.7M seed of September 2020 "
                  "with Point Nine and Forward Partners, and GV is not named in it (TechCrunch 2020-09-16). Accel led the "
                  "$33M Series A of April 2022 with GV, Kindred, Point Nine and others (TechCrunch 2022-04-19): GV's "
                  "entry, matching the firm's first capture in May 2022. No exit and no later priced round found; "
                  "below_1b, aligned with the Accel and Point Nine rows.",
             rounds=[rnd("2020-09-16", "Seed", 3700000, "Kindred Capital", False, TC20, "press"),
                     rnd("2022-04-19", "Series A", 33000000, "Accel", True, TC22, "press")]))

# ---------------------------------------------------------------- gritstone-bio
FB = NEWS("gritstone-bio", "Cancer upstart Gritstone gains major")
GRTS_S1 = "https://www.sec.gov/Archives/edgar/data/1656634/000119312518255669/d565416ds1.htm"
L.append(cls("gritstone-bio", country="US", city="Emeryville", focus="Healthcare & Bio", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=FB, entry_date="2017-09-07",
             note="Cancer immunotherapy developer (Emeryville). GV joined the $92.7M Series B of September 2017 as a new "
                  "investor beside lead Lilly Asia Ventures, with the Series A investors (Versant, The Column Group, "
                  "Clarus, Frazier) following on (Fierce Biotech 2017-09-07); the S-1's investors' rights agreement has "
                  "GV 2017, L.P. as a party (FTS). IPO 2018 (NASDAQ: GRTS). Headlines report a Chapter 11 filing in "
                  "October 2024 and an asset auction for $21.25M in December 2024, so the known acquired status stands "
                  "(a sale out of insolvency); below_1b with no figure.",
             rounds=[rnd("2017-09-07", "Series B", 93000000, "Lilly Asia Ventures", True, FB, "press"),
                     rnd("2018-06-29", "Series C", None, None, None, GRTS_S1, "filing")]))

# ---------------------------------------------------------------- groundswell
L.append(cls("groundswell", status="private", rng="below_1b", city="El Segundo", focus="SaaS", stage="undetermined",
             note="Corporate philanthropy and employee giving platform. Its $15M seed was announced on 2021-11-30 "
                  "(Business Wire headline; the release refuses automated reads, so its investor list was not read); "
                  "the firm's listing begins with a May 2022 capture and no readable source names the round GV entered, "
                  "so the stage is undetermined. Still operating (a February 2023 customer release). City aligned with "
                  "the Felicis row.",
             rounds=[rnd("2021-11-30", "Seed", 15000000, None, None,
                         NEWS("groundswell", "Groundswell Announces A Total of $15M"), "company")]))

# ---------------------------------------------------------------- guide-therapeutics
L.append(cls("guide-therapeutics", status="acquired", rng="below_1b", country="US", city="Atlanta",
             focus="Healthcare & Bio", stage="undetermined",
             note="Nucleic acid delivery (lipid nanoparticles) spun out of Georgia Tech in 2018 by James Dahlman and "
                  "Cory Sago. Beam Therapeutics bought it on 2021-02-23 for $120M upfront in Beam stock plus up to $320M "
                  "in milestones (Beam's release, which names Biomatics Capital, GreatPoint Ventures and GV as its "
                  "backers); the firm's exit line agrees. No source read names the round GV entered, so the stage is "
                  "undetermined; no funding round was found.",
             rounds=[]))

# ---------------------------------------------------------------- guidelight-health
BHB = NEWS("guidelight-health", "GV, Triple Aim Bet Big")
L.append(cls("guidelight-health", status="private", rng="below_1b", city="Denver", city_src="web_verified",
             focus="Healthcare & Bio",
             note="Partial hospitalization and intensive outpatient behavioral health provider with clinics in "
                  "Colorado, Massachusetts, North Carolina and California. Its May 2026 release is datelined Denver "
                  "(GlobeNewswire), where most of its clinics sit, so Denver rather than the Glencoe, Illinois address "
                  "on its 2023 Form Ds (an officer's address outside its markets). GV and Triple Aim led its roughly "
                  "$16.35M round (Behavioral Health Business, 2024-01-29); the Form D band's Series A stands. Operating "
                  "in 2026; below_1b.",
             rounds=[rnd("2024-01-29", "unnamed", 16350000, "GV and Triple Aim", True, BHB, "press")]))

# ---------------------------------------------------------------- guild-ai
POSTG = POST("guild-ai-sharing")
SAG = NEWS("guild-ai", "JetStream Security, Guild.ai and WorkOS")
L.append(cls("guild-ai", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
             focus="DevTools & APIs", stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=POSTG,
             entry_date="2025-11-19", grad="graduated", grad_src="web_verified", grad_conf="medium", grad_cite=SAG,
             note="Control plane for building and running AI agents (San Francisco, per its April 2026 release). GV's "
                  "own post (2025-11-19) says GV partnered with the team from company formation as the lead of the "
                  "Series Seed, matching the firm's first Invested month (2025-11). SiliconANGLE (2026-03-03) reports "
                  "$44M in a combined seed and Series A led by GV Management Co. with Acrew, NFX and Khosla, and the "
                  "company's release calls it Series A funding: a later round the record names Series A, so the seed "
                  "graduated (medium: the two were announced together). Momentum check " + CHECK + ": no valuation "
                  "disclosed and no priced round at $1B or more found; below_1b.",
             rounds=[rnd("2025-11-19", "Seed", None, "GV", True, POSTG, "firm"),
                     rnd("2026-03-03", "Seed and Series A (combined)", 44000000, "GV", True, SAG, "press")],
             extra={"valuation_range_source": "web_verified", "valuation_citation": SAG, "valuation_asof": CHECK}))

# ---------------------------------------------------------------- gusto
GU12 = "https://techcrunch.com/2012/12/11/zenpayroll-launches-cloud-based-payroll-service-with-6-1m-in-seed-funding-from-the-ceos-at-yammer-box-yelp-and-dropbox/"
GU14 = "https://techcrunch.com/2014/02/19/cloud-based-payroll-app-zenpayroll-raises-20m-from-general-catalyst-and-kleiner-at-a-100m-plus-valuation/"
GU15 = NEWS("gusto", "ZenPayroll Receives $60M")
GU25 = "https://fortune.com/2025/06/09/gusto-200-million-plus-tender-offer"
L.append(cls("gusto", rng="1b_plus", usd=9300000000, val_src="web_verified", val_cite=GU25, asof="2025-06-09",
             country="US", city="San Francisco", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=GU12, entry_date="2012-12-11",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=GU14,
             flags=["model_disputes_source"], clear=["unicorn_name_match"],
             note="Payroll, benefits and HR software (San Francisco; ZenPayroll until 2015, a Y Combinator company). "
                  "ZenPayroll launched on 2012-12-11 with $6.1M in seed funding from Google Ventures and others "
                  "(TechCrunch): GV's entry. General Catalyst led the $20M Series A of February 2014 (TechCrunch "
                  "2014-02-19), so the seed graduated; Google Capital led the $60M round of April 2015 with Google "
                  "Ventures as an existing investor (CPA Practice Advisor). Two pre-filled values are disputed: the "
                  "country NL is a one-word Wikidata join, and the 10b_plus band at $10B is the unicorn list's figure, "
                  "not a mark. The freshest priced event is the June 2025 employee tender at $9.3B led by Teachers' "
                  "Venture Growth (Fortune, 2025-06-09), so 1b_plus, aligned with the Ribbit row; the a16z and Felicis "
                  "rows still read 10b_plus.",
             rounds=[rnd("2012-12-11", "Seed", 6100000, None, True, GU12, "press"),
                     rnd("2014-02-19", "Series A", 20000000, "General Catalyst", None, GU14, "press"),
                     rnd("2015-04-06", "unnamed", 60000000, "Google Capital", True, GU15, "press"),
                     rnd("2025-06-09", "Tender", None, "Teachers' Venture Growth", None, GU25, "press")],
             extra=VR))

# ---------------------------------------------------------------- gyft
GYA = "https://techcrunch.com/2013/09/25/digital-gift-card-platform-gyft-raises-5-million-series-a/"
L.append(cls("gyft", status="acquired", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
             focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=GYA,
             entry_date="2012", grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=GYA,
             note="Digital gift card platform (San Francisco). Gyft raised $1.25M in seed funding from Google Ventures, "
                  "Founder Collective and 500 Startups around TechCrunch Disrupt SF 2012 (GV's entry), then a $5M "
                  "Series A led by Karlin Ventures (TechCrunch 2013-09-25), so the seed graduated. First Data bought "
                  "Gyft in July 2014 (TechCrunch 2014-07-30); the firm's exit line agrees.",
             rounds=[rnd("2012", "Seed", 1250000, None, True, GYA, "press"),
                     rnd("2013-09-25", "Series A", 5000000, "Karlin Ventures", None, GYA, "press")]))

# ---------------------------------------------------------------- hags
TCH = NEWS("hags", "GV bets on young team")
L.append(cls("hags", status="acquired", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=TCH, entry_date="2020-09-28",
             note="Social app for high school students that began as a digital yearbook on Snapchat (based in New York "
                  "and remote, per Pulse 2.0). GV led its $1M seed with BoxGroup and angels (TechCrunch 2020-09-28): "
                  "GV's entry. Acquired by Snap in 2022 per the firm's exit line; no press on the sale was found. "
                  "Graduation left for the graduation pass.",
             rounds=[rnd("2020-09-28", "Seed", 1000000, "GV", True, TCH, "press")]))

# ---------------------------------------------------------------- happiest-baby
PUH = NEWS("happiest-baby", "Parenting Solutions Company Happiest Baby Raises $23")
L.append(cls("happiest-baby", status="private", rng="below_1b", country="US", city="Los Angeles",
             focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=PUH, entry_date="2018-12-17",
             note="Maker of the SNOO responsive bassinet (Los Angeles). Greycroft led the $23M Series B of December 2018 "
                  "in which Sallfort Bank and GV also participated (Pulse 2.0, 2018-12-17); the firm's listing first "
                  "appears in a mid-December 2018 capture, so the Series B is GV's entry. Still operating in 2026 (an "
                  "FDA warning letter and a product recall in mid-2026); below_1b, aligned with the Felicis and Lux rows.",
             rounds=[rnd("2018-12-17", "Series B", 23000000, "Greycroft", True, PUH, "press")]))

# ---------------------------------------------------------------- harness
HB = "https://www.harness.io/press-and-news/harness-announces-60m-series-b-financing-from-ivp-gv-and-servicenow"
HE = "https://www.harness.io/press-and-news/harness-announces-240m-financing-round-led-by-goldman-sachs"
L.append(cls("harness", rng="1b_plus", usd=5500000000, val_src="web_verified", val_cite=HE, asof="2025-12-11",
             city="San Francisco", city_src="web_verified", focus="DevTools & APIs",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=HB, entry_date="2019-04-23",
             flags=["model_disputes_source"], clear=["unicorn_name_match"],
             note="Software delivery platform (San Francisco). IVP, GV and ServiceNow Ventures led the $60M Series B of "
                  "April 2019, with Menlo and Unusual as existing investors (the company's release, 2019-04-23): GV's "
                  "entry and the firm's first Invested month (2019-04); GV re-invested in 2020 and 2022. The pre-filled "
                  "$1.7B is the unicorn list's old figure and is replaced: the $240M Series E led by Goldman Sachs "
                  "Alternatives valued Harness at $5.5B (the company's release, 2025-12-11), aligned with the IVP row.",
             rounds=[rnd("2019-04-23", "Series B", 60000000, "IVP, GV and ServiceNow Ventures", True, HB, "company"),
                     rnd("2025-12-11", "Series E", 240000000, "Goldman Sachs Alternatives", None, HE, "company")],
             extra=VR))

# ---------------------------------------------------------------- harvey
HC = NEWS("harvey", "Harvey Raises Series C from Google Ventures")
H11 = "https://www.harvey.ai/blog/harvey-raises-at-dollar11-billion-valuation-to-scale-agents-across-law-firms-and-enterprises"
H155 = "https://www.harvey.ai/blog/harvey-raises-dollar550m-at-a-dollar155b-valuation-to-help-legal-teams-own-their-intelligence"
L.append(cls("harvey", rng="10b_plus", usd=15500000000, val_src="web_verified", val_cite=H155, asof="2026-09-09",
             city="San Francisco", focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=HC, entry_date="2024-07-23",
             clear=["unicorn_name_match"],
             note="Legal AI (San Francisco). GV led the $100M Series C at $1.5B (Harvey's post, 2024-07-23); the firm's "
                  "own case study gives GV's First Round as Series C (2024) and its /ai list the first Invested month "
                  "as 2024-07; GV re-invested in 2025. Harvey's post of 2026-09-09 announces $550M at a $15.5B "
                  "valuation co-led by Diffusion and Lightspeed, which confirms the pre-filled mark with a citation. "
                  "The a16z, Coatue and Sequoia rows still carry the March 2026 round at $11B (Harvey's post, "
                  "2026-03-25) and are the stale side (same band).",
             rounds=[rnd("2024-07-23", "Series C", 100000000, "GV", True, HC, "company"),
                     rnd("2026-03-25", "unnamed", 200000000, "GIC and Sequoia", None, H11, "company"),
                     rnd("2026-09-09", "unnamed", 550000000, "Diffusion and Lightspeed", None, H155, "company")],
             extra=VR))

# ---------------------------------------------------------------- headspin
HS18 = "https://techcrunch.com/2018/10/30/gv-backed-mobile-app-performance-platform-headspin-raises-20m-at-500m-valuation/"
HS24 = "https://techcrunch.com/2024/07/18/pe-firm-partnerone-paid-28m-for-headspin-a-fraction-of-its-1-1b-valuation-set-by-iconiq-and-dell-technologies-capital/"
L.append(cls("headspin", status="acquired", rng="below_1b", city="Palo Alto", focus="DevTools & APIs",
             stage="undetermined", flags=["stage_disputes_band"],
             note="Mobile app testing platform (Palo Alto). GV was already a backer at the $20M Series B of October "
                  "2018, which ICONIQ led and in which the existing backers GV, Telstra Ventures and others did not take "
                  "part (TechCrunch 2018-10-30; the company's release also calls GV existing); the firm lists HeadSpin "
                  "from a December 2016 capture. The Form D band read the December 2020 filing, a round after the "
                  "financial review on which Karim Faris sits as director, as GV's entry: it is a follow-on, so the "
                  "Growth band is disputed. No source read names the round GV entered before the Series B, so the stage "
                  "is undetermined and the band's entry date is cleared. PE firm PartnerOne bought HeadSpin for $28.2M "
                  "in July 2024 (TechCrunch 2024-07-18), a fraction of the $1.1B Series C of 2020, after the founder's "
                  "fraud conviction: acquired. The Battery, EQT Ventures and Felicis rows still read private.",
             rounds=[rnd("2018-10-30", "Series B", 20000000, "ICONIQ Capital", False, HS18, "press"),
                     rnd("2020-02", "Series C", None, None, None, HS24, "press")],
             extra={"entry_stage_source": None, "entry_date": None}))

# ---------------------------------------------------------------- headway
ACC = "https://www.accel.com/news/rewiring-the-mental-healthcare-system-our-seed-and-series-a-investment-in-headway"
MER = NEWS("headway", "Digital Health Mental Health Startup Headway Raises $26")
L.append(cls("headway", city="New York", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ACC, entry_date="2020-11-19",
             note="Mental health care network (New York). Accel led the 2019 seed; the $26M Series A of November 2020 "
                  "was led by Thrive Capital and GV, both welcomed as new investors in Accel's own post, with Accel "
                  "following on (Mercom 2020-11-19 also names Thrive and GV as leads). GV's entry is the Series A, so no "
                  "graduation applies. Andreessen Horowitz led the $70M Series B of May 2021.",
             rounds=[rnd("2019", "Seed", None, "Accel", False, ACC, "press"),
                     rnd("2020-11-19", "Series A", 26000000, "Thrive Capital and GV", True, MER, "press")]))

# ---------------------------------------------------------------- heartthis
HT15 = "https://techcrunch.com/2015/02/05/heartthis-lets-you-shop-all-your-favorite-stores-from-just-one-app/"
L.append(cls("heartthis", status="acquired", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="Consumer & Marketplaces", stage="undetermined",
             note="Shopping app for browsing many stores in one place (San Francisco, TechCrunch 2015-02-05). It had $2M "
                  "in funding led by Freestyle Capital with 500 Startups, Founder Collective, Google Ventures and "
                  "others; no source names the round, so the stage is undetermined. In September 2015 Thumbtack took "
                  "four people including the CEO and said it was not buying the product or technology, but TechCrunch "
                  "reported it as Thumbtack's first acquisition with HeartThis's investors receiving Thumbtack shares, "
                  "and the firm's exit line reads 'Acquired by Thumbtack, 2015': read as a sale of the company under "
                  "the acqui-hire rule (an announcement that calls it an acquisition).",
             rounds=[rnd("2015-02", "unnamed", 2000000, "Freestyle Capital", True, HT15, "press")]))

# ---------------------------------------------------------------- heavy-ai
MAPD = NEWS("heavy-ai", "MapD Launches Lightning Fast GPU Database")
L.append(cls("heavy-ai", status="acquired", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
             focus="Data Infrastructure", stage="undetermined",
             note="GPU-accelerated analytics database (MapD, renamed OmniSci and in 2022 HEAVY.AI; San Francisco per its "
                  "2016 release). GV invested before the $10M Series A of March 2016, which Vanedge Capital led with "
                  "Verizon Ventures and NVIDIA 'joining earlier investor GV' (MapD's release, 2016-03-30); GV's partner "
                  "says it worked with MapD since the MIT spin-out, and the firm lists it from 2014. That earlier round "
                  "is not named in any source read, so the stage is undetermined. Acquired by NVIDIA per the firm's "
                  "exit line ('Acquired by NVIDIA, 2025'); no press on the sale was found.",
             rounds=[rnd("2016-03-30", "Series A", 10000000, "Vanedge Capital", None, MAPD, "company")]))

# ---------------------------------------------------------------- hebbia
HBB = NEWS("hebbia", "Hebbia Raises Series B Led by Andreessen")
HTC = NEWS("hebbia", "AI startup Hebbia raised $130M at a $700M")
L.append(cls("hebbia", status="private", rng="below_1b", usd=700000000, val_src="web_verified", val_cite=HTC,
             asof="2024-07-09", country="US", city="New York", focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=HBB, entry_date="2024-05",
             flags=["stale"],
             note="AI search and document analysis for finance and legal work (New York). Its $130M Series B from "
                  "Andreessen Horowitz, Index Ventures, Google Ventures and Peter Thiel (Hebbia's post, 2024-07-08) is "
                  "GV's entry; the firm's /ai list gives the first Invested month as 2024-05, used as the entry date "
                  "(the post dates the announcement). TechCrunch put the round at a $700M valuation (2024-07-09), older "
                  "than 24 months, so stale. Momentum check " + CHECK + " (Google News for the company's raises): no "
                  "later priced round found, so below_1b, aligned with the a16z row.",
             rounds=[rnd("2024-07-08", "Series B", 130000000, "Andreessen Horowitz", True, HBB, "company")],
             extra=VR))

# ---------------------------------------------------------------- helium
VB16 = "https://venturebeat.com/2016/04/25/helium-raises-20m-for-smart-industrial-sensors"
TC19 = "https://techcrunch.com/2019/06/12/helium-network/"
NOVA = NEWS("helium", "Helium changes name to Nova Labs")
L.append(cls("helium", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=NOVA,
             asof="2022-03-30", city="San Francisco", city_src="web_verified", focus="Crypto & Web3",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=VB16, flags=["stale"],
             note="Helium Systems, developer of the Helium network (renamed Nova Labs in 2022; San Francisco). Khosla "
                  "Ventures led $16M in 2014 without GV; 'The round was led by GV' for the $20M Series B of April 2016, "
                  "Andy Wheeler joining the board (VentureBeat 2016-04-25; the Form D of 2016-04-18 lists him as "
                  "director): GV's entry. A $15M Series C followed in 2019 (TechCrunch 2019-06-12). Nova Labs' $200M "
                  "Series D at $1.2B, with Google Ventures participating (SiliconANGLE 2022-03-30), is the last priced "
                  "round and older than 24 months, so stale; aligned with the Ribbit row. The Y Combinator row named "
                  "Helium is a different company (tryhelium.com), not aligned.",
             rounds=[rnd("2014", "unnamed", 16000000, "Khosla Ventures", False, VB16, "press"),
                     rnd("2016-04-25", "Series B", 20000000, "GV", True, VB16, "press"),
                     rnd("2019-06-12", "Series C", 15000000, "Union Square Ventures and Multicoin Capital", None, TC19,
                         "press"),
                     rnd("2022-03-30", "Series D", 200000000, "Tiger Global and Andreessen Horowitz", True, NOVA,
                         "press")],
             extra=VR))

# ---------------------------------------------------------------- helix
L.append(cls("helix", status="acquired", rng="below_1b", country="US", focus="SaaS", stage="undetermined",
             flags=["model_disputes_source", "city_unknown"],
             note="HELIX RE, digital twins of buildings for space planning (CEO James Roche). Density acquired it in "
                  "November 2021 alongside Density's $125M Series D (Density's release, 2021-11-10), matching the firm's "
                  "exit line 'Acquired by Density, 2021'. The pre-filled GB is a one-word Wikidata join on 'Helix' and "
                  "is disputed: the deal and the acquirer (Density, San Francisco) are American and no source ties the "
                  "company to Britain (US at medium confidence); its own site is gone, so no city is placed. No source "
                  "read names GV's round, so the stage is undetermined. Not the Sutter Hill row (Helix, the San Mateo "
                  "population genomics company) nor the unresolved a16z row, so neither is aligned.",
             rounds=[]))

# ---------------------------------------------------------------- hellosign
HS17 = "https://techcrunch.com/2017/06/12/1502316/"
L.append(cls("hellosign", status="acquired", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="SaaS", stage="undetermined",
             note="E-signature and online fax (HelloFax, a Y Combinator company; San Francisco). The firm lists it from "
                  "2013, with Wesley Chan as partner that year. Its $16M round of June 2017, led by Foundry Group and "
                  "Zach Coelius with Greylock and US Venture Partners, was called a Series B (TechCrunch 2017-06-12) and "
                  "does not name GV, so GV entered earlier; no source read names that round, so the stage is "
                  "undetermined. Dropbox bought HelloSign for $230M in January 2019 (Wikipedia's Dropbox article; CNBC "
                  "headline); the firm's exit line agrees.",
             rounds=[rnd("2017-06-12", "Series B", 16000000, "Foundry Group and Zach Coelius", None, HS17, "press")]))

# ---------------------------------------------------------------- high-fidelity
HF13 = "https://techcrunch.com/2013/04/19/true-ventures-backs-high-fidelity/"
HF15 = "https://techcrunch.com/2015/02/25/high-fidelity-raises-11m-to-build-deployable-virtual-worlds/"
HF18 = "https://techcrunch.com/2018/06/28/vr-blockchain-startup-founded-by-second-life-co-creator-raises-35m/"
L.append(cls("high-fidelity", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=HF13, entry_date="2013-04",
             note="Philip Rosedale's virtual world company, later spatial audio (San Francisco). True Ventures 'led High "
                  "Fidelity's Series A, and ... Google Ventures and various angel investors also participated' "
                  "(TechCrunch 2013-04-19; $2.4M of a $3.4M round per its SEC filing): GV's entry. Later: $11M led by "
                  "Vulcan Capital (2015), $22M (2016) and a $35M Series D led by Galaxy Digital Ventures (2018). In "
                  "January 2022 it moved staff and patents to Linden Lab for Linden Lab stock and continued as a "
                  "separate company selling spatial audio (GamesBeat); no later sale or shutdown found, so private at its "
                  "last known state, below_1b.",
             rounds=[rnd("2013-04", "Series A", 3400000, "True Ventures", True, HF13, "press"),
                     rnd("2015-02-25", "unnamed", 11000000, "Vulcan Capital", None, HF15, "press"),
                     rnd("2016-12", "unnamed", 22000000, "IDG Capital and Breyer Capital", None, W("High Fidelity, Inc."),
                         "press"),
                     rnd("2018-06-28", "Series D", 35000000, "Galaxy Digital Ventures", None, HF18, "press")]))

# ---------------------------------------------------------------- highfive
HI13 = "https://techcrunch.com/2013/10/24/highfive/"
HI15 = "https://techcrunch.com/2015/03/12/highfive-32m/"
HI20 = "https://techcrunch.com/2020/09/01/dialpad-acquires-video-conferencing-service-highfive/"
L.append(cls("highfive", status="acquired", rng="below_1b", country="US", city="Redwood City", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=HI13, entry_date="2013-10-24",
             note="Video conferencing hardware and software (Redwood City). It raised a $4M seed (investors not named) "
                  "and a $9.5M Series A from General Catalyst, Andreessen Horowitz and Google Ventures (TechCrunch "
                  "2013-10-24); the firm lists it from a late-2013 capture. GV is named only in the Series A, so that is "
                  "its entry (medium: the seed's investors are not named). Series B of $32M (2015) and a Series C "
                  "(2018). Dialpad acquired Highfive in September 2020 (TechCrunch 2020-09-01); aligned with the a16z, "
                  "General Catalyst and Lightspeed rows.",
             rounds=[rnd("2013-10-24", "Seed", 4000000, None, None, HI13, "press"),
                     rnd("2013-10-24", "Series A", 9500000, None, True, HI13, "press"),
                     rnd("2015-03-12", "Series B", 32000000, None, None, HI15, "press")]))

# ---------------------------------------------------------------- hipster
HP11 = "https://techcrunch.com/2011/05/16/hipster-raises-1m-from-google-ventures-lightbank-and-500-startups/"
L.append(cls("hipster", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=HP11, entry_date="2011-05-16",
             note="Local Q&A, then location photo-sharing app (San Francisco). It raised $1M in seed funding from Mitch "
                  "Kapor, 500 Startups, Lightbank, Google Ventures, Charles River Ventures and others (TechCrunch "
                  "2011-05-16): GV's entry. AOL bought Hipster, its five-person team and the app, for a low seven-figure "
                  "sum in March 2012 (TechCrunch 2012-03-15, the firm's own link; its exit line agrees) and shut the app "
                  "in February 2013. Graduation left for the graduation pass.",
             rounds=[rnd("2011-05-16", "Seed", 1000000, None, True, HP11, "press")]))

# ---------------------------------------------------------------- home-from-college
HFC = NEWS("home-from-college", "GV invests in Home From College")
L.append(cls("home-from-college", status="private", rng="below_1b", country="US", city="Los Angeles",
             city_src="web_verified", focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=HFC, entry_date="2024-04-03",
             note="Career platform matching Gen Z students and graduates with jobs (Los Angeles). GV led its $5.4M seed "
                  "after an earlier $1.5M from PEAK6 and angels (TechCrunch 2024-04-03): GV's entry. Google News "
                  "searched " + CHECK + " shows no later round. Graduation left for the graduation pass.",
             rounds=[rnd("2024-04-03", "Seed", 5400000, "GV", True, HFC, "press")]))

# ---------------------------------------------------------------- homeaway
AWAY_IRA = FTS("HOMEAWAY", "S-1")
AWAY_S1 = "https://www.sec.gov/Archives/edgar/data/1366684/000119312511064128/ds1.htm"
L.append(cls("homeaway", city="Austin", focus="Consumer & Marketplaces", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=AWAY_IRA, entry_date="2010",
             note="Vacation rental marketplace (Austin). Google Ventures 2010, L.P. signs HomeAway's amended investors' "
                  "rights agreement of 2011-03-10 as an Investor and a Common Holder (S-1 exhibit 4.2); the S-1 shows no "
                  "preferred sold after the $250M Series D of October and November 2008, so GV's 2010 vehicle bought "
                  "existing shares, a secondary position, which reads Growth (medium: the purchase date is not stated; "
                  "the year is the vehicle's). IPO June 2011 (NASDAQ: AWAY); Expedia bought HomeAway in December 2015 "
                  "for $3.9B (Wikipedia), so acquired with no figure.",
             rounds=[rnd("2008-10", "Series D", 250000000, None, False, AWAY_S1, "filing"),
                     rnd("2010", "secondary purchase", None, None, True, AWAY_IRA, "filing")]))

# ---------------------------------------------------------------- homebound
CBH = "https://news.crunchbase.com/venture/homebound-a-tech-enabled-general-contractor-raises-35m-to-rebuild-after-wildfires/"
TCHB = "https://techcrunch.com/2022/02/15/homebound-raises-75m-in-khosla-led-series-c/"
L.append(cls("homebound", status="private", rng="below_1b", country="US", city="Santa Rosa", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=CBH, entry_date="2019-08",
             note="Tech-enabled homebuilder (Santa Rosa, per TechCrunch 2022). Thrive led the $18M Series A of December "
                  "2018; Fifth Wall Ventures led the $35M Series B, closed in August 2019 and disclosed in January 2020, "
                  "with Khosla, Forerunner, Google Ventures, Ashton Kutcher and Thrive (Crunchbase News 2020-01-17): "
                  "GV's entry, consistent with the firm's first capture in March 2020. Khosla led the $75M Series C of "
                  "February 2022 and the company declined to give a valuation. No later priced round found; below_1b, "
                  "aligned with the Thrive row.",
             rounds=[rnd("2018-12", "Series A", 18000000, "Thrive Capital", None, CBH, "press"),
                     rnd("2019-08", "Series B", 35000000, "Fifth Wall Ventures", True, CBH, "press"),
                     rnd("2022-02-15", "Series C", 75000000, "Khosla Ventures", True, TCHB, "press")]))

# ---------------------------------------------------------------- homelight
HL15 = "https://techcrunch.com/2015/02/04/homelight-funding/"
HL17 = "https://menlovc.com/perspective/the-way-home-menlo-leads-series-b-in-homelight/"
HL21 = "https://techcrunch.com/2021/09/02/homelight-closes-on-100m-series-d-at-a-1-6b-valuation-as-revenue-surges/"
L.append(cls("homelight", city="San Francisco", focus="Consumer & Marketplaces", stage="undetermined",
             note="Real estate agent matching and home transaction platform (San Francisco; launched November 2012). "
                  "TechCrunch (2015-02-04) reports a $3M round led by Bullpen Ventures and that Google Ventures had "
                  "participated in the company's earlier funding (about $1.85M), matching the firm's listing from a May "
                  "2013 capture; no source names that earlier round, so the stage is undetermined. Menlo led the Series "
                  "B in 2017; the $100M Series D of September 2021 valued HomeLight at $1.6B (TechCrunch), the "
                  "pre-filled mark.",
             rounds=[rnd("2015-02-04", "unnamed", 3000000, "Bullpen Ventures", None, HL15, "press"),
                     rnd("2017-08-15", "Series B", None, "Menlo Ventures", None, HL17, "press"),
                     rnd("2021-09-02", "Series D", 100000000, "Zeev Ventures", None, HL21, "press")]))

# ---------------------------------------------------------------- hover
TCHV = NEWS("hover", "GV leads $25M investment in Hover")
POSTH = POST("hover-home-improvement")
L.append(cls("hover", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
             focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TCHV,
             entry_date="2018-01-29",
             note="3D property models from smartphone photos for contractors and insurers (San Francisco). GV led the "
                  "$25M Series B with Home Depot and Standard Industries (TechCrunch 2018-01-29): GV's entry; GV's own "
                  "post says its partner first invested and joined the board in 2017 and backed HOVER again in the $60M "
                  "Series D of November 2020. Menlo led the Series C in 2019. No priced round at $1B or more found; "
                  "below_1b, aligned with the Menlo row.",
             rounds=[rnd("2018-01-29", "Series B", 25000000, "GV", True, TCHV, "press"),
                     rnd("2020-11-17", "Series D", 60000000, None, True, POSTH, "firm")]))

# ---------------------------------------------------------------- hubspot
HSB = "https://www.hubspot.com/blog/bid/10491/sequoia-google-ventures-and-salesforce-com-invest-32-million-in-hubspot"
HUBSCAP = "https://stockanalysis.com/stocks/hubs/market-cap/"
L.append(cls("hubspot", rng="10b_plus", usd=10110000000, val_src="web_verified", val_cite=HUBSCAP, asof=CHECK,
             city="Cambridge", focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=HSB, entry_date="2011-03", flags=["model_disputes_source"],
             note="Marketing, sales and service software (Cambridge, Massachusetts). Sequoia, Google Ventures and "
                  "Salesforce invested $32M in HubSpot's Series D in March 2011, with the existing investors General "
                  "Catalyst, Matrix and Scale following on (HubSpot's own post): GV's entry; Google Ventures 2011, L.P. "
                  "signs the 2012 investors' rights agreement (FTS). NYSE: HUBS since 2014. Market cap $10.11B at the "
                  + CHECK + " close (stockanalysis.com), within 5% of the $10B edge, replacing the pre-filled $28.3B "
                  "float-era figure; same band as the General Catalyst and Sequoia rows.",
             rounds=[rnd("2011-03-08", "Series D", 32000000, "Sequoia Capital, Google Ventures and Salesforce", True,
                         HSB, "company")],
             extra=VR))

# ---------------------------------------------------------------- humans
TCHU = NEWS("humans", "Humans&, a 'human-centric' AI startup")
L.append(cls("humans", status="private", rng="1b_plus", usd=4480000000, val_src="web_verified", val_cite=TCHU,
             asof="2026-01-20", country="US", city="San Francisco", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TCHU, entry_date="2026-01-20",
             grad="censored",
             note="Human-centric AI lab founded in September 2025 by Anthropic, xAI and Google alumni. Its $480M seed at "
                  "a $4.48B valuation, led by SV Angel and co-founder Georges Harik with Nvidia, Jeff Bezos, GV and "
                  "Emerson Collective (TechCrunch and Crunchbase News, 2026-01-20), is GV's entry and matches the "
                  "firm's first Invested month (2026-01). The entry round set the mark, so 1b_plus at $4.48B; the "
                  "Felicis row reads below_1b and is the stale side. City aligned with the Felicis row (its terms name "
                  "the courts of San Francisco). Censored: the entry is under 24 months old.",
             rounds=[rnd("2026-01-20", "Seed", 480000000, "SV Angel and Georges Harik", True, TCHU, "press")],
             extra=VR))

# ---------------------------------------------------------------- hustle
HU17 = "https://techcrunch.com/2017/08/02/hustle-texting/"
HU18 = "https://techcrunch.com/2018/05/01/hustle-sms/"
L.append(cls("hustle", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=HU18, entry_date="2018-05-01",
             flags=["model_disputes_source"],
             note="Peer-to-peer texting platform for campaigns and organizations (San Francisco, with New York and DC "
                  "offices). Social Capital led the $8M Series A of August 2017, whose investor list does not include "
                  "GV (TechCrunch 2017-08-02); Insight Venture Partners led the $30M Series B 'joined by Google's GV and "
                  "Salesforce Ventures' (TechCrunch 2018-05-01): GV's entry, matching the firm's first capture in June "
                  "2018. Social Capital bought Hustle outright in August 2020 (TechCrunch 2020-08-18) and its employees "
                  "bought the whole company from Social Capital in May 2026 (Campaigns & Elections): acquired. The "
                  "pre-filled defunct status and JP country come from a one-word Wikidata join on 'Hustle' (dissolved "
                  "2010) and are disputed; the Insight row's defunct status looks inherited from the same join.",
             rounds=[rnd("2017-08-02", "Series A", 8000000, "Social Capital", False, HU17, "press"),
                     rnd("2018-05-01", "Series B", 30000000, "Insight Venture Partners", True, HU18, "press")]))

# ---------------------------------------------------------------- hyperfine-research
DOT = NEWS("hyperfine-research", "Hyperfine raises $90 million in Series D")
HYPRCAP = "https://stockanalysis.com/stocks/hypr/market-cap/"
L.append(cls("hyperfine-research", status="public", rng="below_1b", usd=88650000, val_src="web_verified",
             val_cite=HYPRCAP, asof=CHECK, country="US", city="Guilford", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=DOT, entry_date="2021-02-15",
             note="Portable bedside MRI (Swoop; Guilford, Connecticut), a Jonathan Rothberg company. GV is named among "
                  "the investors of the $90M Series D announced in February 2021 (DOTmed 2021-02-15; the S-1 shows "
                  "Series D closes in 2020 and 2021), and the firm's listing begins in 2021, so the Series D is GV's "
                  "entry (medium: the earlier rounds' investors are not public); the 2022 S-1 names GV among Legacy "
                  "Hyperfine's institutional investors. Listed through the HealthCor Catalio SPAC in December 2021 "
                  "(NASDAQ: HYPR); market cap $88.65M at the " + CHECK + " close (stockanalysis.com), below_1b.",
             rounds=[rnd("2021-02-15", "Series D", 90000000, None, True, DOT, "press")],
             extra=VR))

# ---------------------------------------------------------------- iconovir-bio
FIC = NEWS("iconovir-bio", "IconOVir uncloaks with $77M")
L.append(cls("iconovir-bio", status="private", rng="below_1b", country="US", city="San Diego", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FIC, entry_date="2021-01-05",
             note="Oncolytic virus developer out of the Salk Institute (San Diego). It launched with a $77M Series A led "
                  "by Nextech and Vida Ventures with Polaris, GV, Wellington, Logos and Two River (Fierce Biotech "
                  "2021-01-05): GV's entry and the firm's first listing year. It dosed the first patient in its Phase 1 "
                  "trial in July 2023 (the company's release headline); no later round, sale or shutdown found, and the "
                  "firm still lists it without an exit line, so private, below_1b.",
             rounds=[rnd("2021-01-05", "Series A", 77000000, "Nextech and Vida Ventures", True, FIC, "press")]))

# ---------------------------------------------------------------- ideaya-biosciences
IS1 = FTS("IDEAYA Biosciences", "S-1")
IDCAP = "https://stockanalysis.com/stocks/idya/market-cap/"
L.append(cls("ideaya-biosciences", rng="1b_plus", usd=3690000000, val_src="web_verified", val_cite=IDCAP, asof=CHECK,
             country="US", city="South San Francisco", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=IS1, entry_date="2018-01",
             note="Precision oncology (synthetic lethality) drug developer (South San Francisco). The S-1's "
                  "related-party section shows GV 2017, L.P. buying $10M of the $94M Series B issued in January and "
                  "March 2018 and becoming a 5% holder at the initial closing; all of GV's shares are Series B, so the "
                  "Series B is GV's entry. IPO May 2019 (NASDAQ: IDYA). Market cap $3.69B at the " + CHECK + " close "
                  "(stockanalysis.com), replacing the pre-filled $1.8B float.",
             rounds=[rnd("2018-01", "Series B", 94000000, None, True, IS1, "filing")],
             extra=VR))

# ---------------------------------------------------------------- imagen
L.append(cls("imagen", status="private", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
             stage="undetermined", entry_date="2018-09",
             note="Imagen Technologies, AI software for radiology (FDA de novo clearance for OsteoDetect wrist fracture "
                  "detection in 2018; New York). The firm's /ai list gives its first Invested month as 2018-09 (the "
                  "entry date, decisions D7); no source read names the round GV entered (only vendor pages list its "
                  "rounds), so the stage is undetermined. The firm still lists it without an exit line and no sale or "
                  "shutdown was found: private, below_1b.",
             rounds=[]))

# ---------------------------------------------------------------- impossible-foods
WIF = W("Impossible Foods")
AGF = NEWS("impossible-foods", "Impossible Foods brings total funding to $2bn")
L.append(cls("impossible-foods", status="private", rng="1b_plus", usd=7000000000, val_src="web_verified",
             val_cite=AGF, asof="2021-11-23", city="Redwood City", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=WIF, entry_date="2014",
             flags=["stale"],
             note="Plant-based meat (Redwood City). Wikipedia names Google Ventures among the investors in its $75M and "
                  "$108M rounds. The company's Form Ds (CIK 1580614, filed late in April 2018) show first sales of $6.2M "
                  "in September 2011, $3.0M and $25.0M in 2013, $40.0M in June 2014 and $108.0M in August 2015; the firm "
                  "lists Impossible from a May 2015 capture, before the $108M round opened, so GV entered in the 2014 "
                  "round, the company's fourth filed raise: Growth (medium: no source gives GV's round letter). Mirae "
                  "led the $500M round of November 2021 at a reported $7B valuation (AgFunderNews, 2021-11-23), the "
                  "last primary mark, older than 24 months, so stale; the Coatue and Khosla rows carry the same $7B "
                  "on a CB Insights page, a vendor. A June 2023 Bloomberg headline reports the value of employees' "
                  "shares down 89% since 2021; the article could not be read and is left for the A/B pass, not read "
                  "as a priced event.",
             rounds=[rnd("2014", "unnamed ($75M)", 75000000, None, True, WIF, "press"),
                     rnd("2015-08", "unnamed ($108M)", 108000000, None, None, WIF, "press"),
                     rnd("2021-11-23", "unnamed", 500000000, "Mirae Asset", None, AGF, "press")],
             extra=VR))

# ---------------------------------------------------------------- incorta
TCIN = "https://techcrunch.com/2017/09/19/real-time-data-analytics-startup-incorta-raises-15m-series-b-led-by-kleiner-perkins/"
TCIN19 = "https://techcrunch.com/2019/08/15/incorta-raises-30m-series-c-for-etl-free-data-processing-solution/"
FORTI = NEWS("incorta", "Google and Microsoft's venture capital arms are pouring")
L.append(cls("incorta", status="private", rng="below_1b", city="San Mateo", city_src="web_verified",
             focus="Data Infrastructure", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=TCIN,
             note="Unified data analytics platform built by former Oracle executives (San Mateo). TechCrunch's Series B "
                  "report (2017-09-19) states 'a $10 million Series A led by GV in May 2016' and lists GV as an existing "
                  "investor in the $15M Series B led by Kleiner Perkins; the 2016 round is the Form D of 2016-05-16 with "
                  "Karim Faris as director, and the $1M and $4.2M filings of 2014-15 carry no GV partner. A $30M Series "
                  "C led by Sorenson (2019, with GV) and a $120M round of June 2021 from GV and Microsoft's M12 (Fortune "
                  "headline) followed. No valuation disclosed and no sale or shutdown found; private, below_1b.",
             rounds=[rnd("2016-05", "Series A", 10000000, "GV", True, TCIN, "press"),
                     rnd("2017-09-19", "Series B", 15000000, "Kleiner Perkins", True, TCIN, "press"),
                     rnd("2019-08-15", "Series C", 30000000, "Sorenson Capital", True, TCIN19, "press"),
                     rnd("2021-06-23", "unnamed", 120000000, None, True, FORTI, "press")]))

# ---------------------------------------------------------------- inertia
GNWI = NEWS("inertia", "Inertia raises $450 million to commercialize")
L.append(cls("inertia", status="private", rng="below_1b", city="Livermore", city_src="web_verified",
             focus="Climate & Energy", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=GNWI, entry_date="2026-02-11", flags=["needs_web_value"],
             note="Laser-driven (inertial confinement) fusion developer (Livermore), launched in August 2025. Bessemer "
                  "led the $450M Series A with GV, Threshold, Modern Capital, IQT and others (the company's release, "
                  "2026-02-11; Crunchbase News): GV's entry, with no earlier round naming GV and the firm's listing "
                  "beginning in 2026. The valuation was not disclosed (checked " + CHECK + " in the release, Crunchbase "
                  "News and Google News); a raise of this size may imply $1B or more, so the row is flagged for the web "
                  "pass and reads below_1b until a figure is cited.",
             rounds=[rnd("2026-02-11", "Series A", 450000000, "Bessemer Venture Partners", True, GNWI, "company")]))

# ---------------------------------------------------------------- infinitus
PRNI = NEWS("infinitus", "Infinitus Systems Announces $30M Series B")
PRNC = NEWS("infinitus", "Infinitus Systems raises $51.5 million Series C funding on the strength")
L.append(cls("infinitus", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="Healthcare & Bio", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=PRNI, entry_date="2021-04", flags=["model_disputes_source"],
             note="Voice AI that automates healthcare phone calls (Infinitus Systems, San Francisco). GV led the $30M "
                  "Series B, Krishna Yeshwant joining the board, with Kleiner Perkins and Coatue as existing investors "
                  "(the company's release, 2021-11-10); the firm's /ai list gives the first Invested month as 2021-04, "
                  "used as the entry date, and a re-investment in 2022-05. Andreessen Horowitz led the $51.5M Series C of "
                  "October 2024 with GV following (the company's release), valuation not disclosed. The pre-filled CN "
                  "is a one-word Wikidata join (Infinitus, the Chinese health products group) and is disputed. Momentum "
                  "check " + CHECK + " (Google News): no priced round at $1B or more found; below_1b, aligned with the "
                  "a16z and Coatue rows.",
             rounds=[rnd("2021-11-10", "Series B", 30000000, "GV", True, PRNI, "company"),
                     rnd("2024-10-23", "Series C", 51500000, "Andreessen Horowitz", True, PRNC, "company")],
             extra={"valuation_range_source": "web_verified", "valuation_citation": PRNC, "valuation_asof": CHECK}))

# ---------------------------------------------------------------- insitro
GVI = "https://globalventuring.com/blog/2020/05/27/insitro-inserts-143m-in-series-b-round/"
BWC = NEWS("insitro", "insitro Raises $400 Million in Series C")
L.append(cls("insitro", status="private", rng="1b_plus", usd=1050000000, val_src="web_verified", val_cite=GVI,
             asof="2018-05", country="US", city="South San Francisco", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GVI, entry_date="2018-05",
             flags=["stale"],
             note="Machine learning drug discovery (Daphne Koller; South San Francisco). It launched in May 2018 with a "
                  "$100M Series A whose cash 'came from GV, Andreessen Horowitz, Arch Venture Partners, Foresite Capital "
                  "and Third Rock at a $1.05bn valuation' (Global Venturing, 2020-05-27): GV's entry and the firm's "
                  "first Invested month (2018-05); GV followed in the $143M Series B led by Andreessen Horowitz (2020). "
                  "The $400M Series C of March 2021 disclosed no valuation in the sources read; the $2.4B on the a16z "
                  "row comes from GetLatka, a vendor, which cannot band a row, so the last cited mark is the Series A's "
                  "$1.05B, stale; the band agrees with the a16z row either way.",
             rounds=[rnd("2018-05", "Series A", 100000000, None, True, GVI, "press"),
                     rnd("2020-05-26", "Series B", 143000000, "Andreessen Horowitz", True, GVI, "press"),
                     rnd("2021-03-15", "Series C", 400000000, None, None, BWC, "company")],
             extra=VR))

# ---------------------------------------------------------------- instawork
PRNIW = NEWS("instawork", "Instawork Raises $60Mn in Series C")
L.append(cls("instawork", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Marketplace for hourly and flexible work (a Y Combinator company, San Francisco). GV is an existing "
                  "investor in the $60M Series C of July 2021 led by Craft Ventures (the company's release); the firm "
                  "lists Instawork from a June 2019 capture. No source read names the round GV entered, so the stage is "
                  "undetermined. A $60M round followed in May 2023 (headlines) with no valuation disclosed; below_1b, "
                  "aligned with the Greylock, Spark and Y Combinator rows.",
             rounds=[rnd("2021-07-09", "Series C", 60000000, "Craft Ventures", True, PRNIW, "company")]))

# ---------------------------------------------------------------- intercom
TCIC = NEWS("intercom", "Intercom raises $125 million to take on Salesforce")
L.append(cls("intercom", rng="1b_plus", usd=1275000000, val_src="web_verified", val_cite=TCIC, asof="2018-03-27",
             city="San Francisco", focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=TCIC, entry_date="2018-03-27", flags=["stale", "model_disputes_source"],
             clear=["unicorn_name_match"],
             note="Customer messaging and AI support software (founded in Dublin, headquartered in San Francisco). "
                  "Kleiner Perkins led the $125M Series D at a $1.275B valuation, with Google Ventures participating "
                  "beside the existing investors Bessemer and Index (TechCrunch 2018-03-27): GV's entry, matching the "
                  "firm's first capture in April 2018. No later priced primary round found, so the mark is the Series "
                  "D's $1.275B (replacing the unicorn list's rounded $1.2B), older than 24 months, stale.",
             rounds=[rnd("2018-03-27", "Series D", 125000000, "Kleiner Perkins", True, TCIC, "press")],
             extra=VR))

# ---------------------------------------------------------------- invetx
LW = NEWS("invetx", "Latham Advises Invetx")
L.append(cls("invetx", status="acquired", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LW,
             entry_date="2022-05-10",
             note="Animal health biologics (half-life-extended antibodies for dogs and cats; Boston). F-Prime, Novo "
                  "Holdings, GV and Eight Roads led its $60.5M Series B (Latham & Watkins, 2022-05-10): GV's entry and "
                  "the firm's first listing year. Dechra Pharmaceuticals agreed to buy Invetx in July 2024 (the "
                  "company's release headline); the firm's exit line reads 'Acquired by Dechra Pharmaceuticals, 2024'. "
                  "Acquired, no figure.",
             rounds=[rnd("2022-05-10", "Series B", 60500000, "F-Prime, Novo Holdings, GV and Eight Roads", True, LW,
                         "press")]))

# ---------------------------------------------------------------- ionic-security
IO13 = "https://techcrunch.com/2013/04/19/ionic-security-raises-9-25m-from-kleiner-perkins-to-help-companies-secure-and-control-their-data-in-the-cloud/"
IO14 = "https://techcrunch.com/2014/02/20/ionic-security-raises-25-5-million-for-its-encryption-based-security-tech/"
L.append(cls("ionic-security", status="acquired", rng="below_1b", country="US", city="Atlanta", city_src="web_verified",
             focus="Security", stage="undetermined",
             note="Data protection and encryption platform (Atlanta). Kleiner Perkins led a $9.4M Series A1 in April "
                  "2013 without GV (TechCrunch 2013-04-19); Google Ventures and Jafco co-led a $25.5M investment reported "
                  "in February 2014 (TechCrunch 2014-02-20; Fox Business), which no source names by series (it could be "
                  "an A2 or a B), so the stage is undetermined; the firm lists Ionic from a May 2013 capture. Over $78M "
                  "raised by April 2015 (Fortune). Twilio acquired Ionic in 2021 (the firm's exit line and its Twilio "
                  "link).",
             rounds=[rnd("2013-04-19", "Series A1", 9400000, "Kleiner Perkins", False, IO13, "press"),
                     rnd("2014-02-20", "unnamed", 25500000, "Google Ventures and Jafco Ventures", True, IO14, "press")]))

# ---------------------------------------------------------------- ionq
IQR = NEWS("ionq", "IonQ Raises $20M Series B Round Led By NEA, GV")
IQCAP = "https://stockanalysis.com/stocks/ionq/market-cap/"
IQFD1 = "https://www.sec.gov/Archives/edgar/data/1682477/000168247717000001/0001682477-17-000001-index.htm"
L.append(cls("ionq", rng="10b_plus", usd=17710000000, val_src="web_verified", val_cite=IQCAP, asof=CHECK,
             city="College Park", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=IQR, entry_date="2017-02-24",
             flags=["stage_disputes_band"],
             note="Trapped-ion quantum computers (College Park, Maryland). NEA and GV led the $20M Series B (IonQ's "
                  "release, 2017-07-25), GV's first quantum investment (Wikipedia); its Form D (first sale 2017-02-24, "
                  "filed July 2017) lists Blake Byers as director, and IonQ's S-1 has him on the board since February "
                  "2017. The band read the other July 2017 Form D, a $2M preferred offering whose first sale was "
                  "2016-07-25 (NEA's earlier money), as a GV seed because Byers is listed on it as a sitting director; "
                  "the documented entry is the Series B, so Growth and no graduation applies. Listed through the dMY III "
                  "SPAC in 2021 (NYSE: IONQ); market cap $17.71B at the " + CHECK + " close (stockanalysis.com), "
                  "replacing the pre-filled $11.5B float.",
             rounds=[rnd("2016-07-25", "unnamed (Form D)", 2000000, None, False, IQFD1, "filing"),
                     rnd("2017-07-25", "Series B", 20000000, "NEA and GV", True, IQR, "company")],
             extra=VR))

jl.write("j6", L)
