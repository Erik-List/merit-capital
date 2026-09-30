"""Judge c4, batch 7 (queue batch-007): listed NEA members, classification only."""
import judge_lib as jl

W, SITE, POST, NEWS, FTS, rnd = jl.W, jl.SITE, jl.POST, jl.NEWS, jl.FTS, jl.rnd
GP = "Graduation left for the graduation pass."
L = []


def c(slug, **k):
    L.append(jl.cls(slug, **k))


# ---- duolingo: city; the known Series A (Form D band) is disputed by the named Series B NEA led
c("duolingo", city="Pittsburgh", focus="Consumer & Marketplaces",
  stage="Growth", stage_src="web_verified", stage_cite=W("Duolingo"), stage_conf="high", entry_date="2012-09",
  flags=["stage_disputes_band"],
  rounds=[rnd("2011-10", "Series A", 3300000, "Union Square Ventures", False, W("Duolingo"), "press"),
          rnd("2012-09", "Series B", 15000000, "New Enterprise Associates", True, W("Duolingo"), "press")],
  note="NEA led the $15M Series B of September 2012 (USV had led the $3.3M Series A in 2011), so NEA entered at "
       "Growth, not at the Series A the Form D band read; the firm's own 2012 first-invested year agrees. "
       "Headquartered in Pittsburgh.")

# ---- dura-pharmaceuticals
c("dura-pharmaceuticals", status="acquired", rng="below_1b", country="US", city="San Diego",
  focus="Healthcare & Bio", stage="undetermined", entry_date="1993", rounds=[],
  note="San Diego specialty pharma, acquired by Elan in 2000 (the firm's page reads IPO/Public). No record on disk "
       "names the round NEA entered in 1993, so the stage is undetermined; whether Dura was already listed by "
       "1993 was not checked.")

# ---- e-offering
c("e-offering", status="acquired", rng="below_1b", country="US", city="San Francisco",
  focus="Fintech & Payments", stage="undetermined", entry_date="2000", rounds=[],
  note="E*Offering, the online investment bank, was folded into Wit SoundView (the firm's exit line); the Battery "
       "book agrees on acquired and San Francisco. The round NEA entered in 2000 is not named in any record.")

# ---- e2o-communications
c("e2o-communications", status="acquired", rng="below_1b", country="US", city="Calabasas",
  focus="Industrial & Robotics", stage="undetermined", entry_date="2000", rounds=[],
  note="Optical transceiver maker from Calabasas, acquired by JDS Uniphase (the firm's exit line). The round NEA "
       "entered in 2000 is not named in any record.")

# ---- eargo: city + band; entry date corrected from the Form D anchor to the Series B NEA led
c("eargo", city="San Jose", rng="below_1b", focus="Healthcare & Bio",
  stage="Growth", stage_src="web_verified", stage_cite=W("Eargo"), stage_conf="high", entry_date="2015-12",
  rounds=[rnd("2015-06", "Series A", 13600000, None, False, W("Eargo"), "press"),
          rnd("2015-12", "Series B", 25000000, "New Enterprise Associates", True, W("Eargo"), "press"),
          rnd("2017-10", "Series C", 45000000, None, True, W("Eargo"), "press")],
  note="NEA led the $25M Series B of December 2015, its first investment (the firm's own year is 2015), so the "
       "entry date moves from the 2017 Form D anchor to 2015-12; the stage stays Growth. Taken private in 2024 "
       "and merged with hearX into LXE Hearing in 2025; San Jose.")

# ---- earlens
c("earlens", status="private", rng="below_1b", city="Menlo Park", focus="Healthcare & Bio",
  note="Light-driven hearing aid maker, still raising (a $10M Form D in March 2025) and filing from Menlo Park; "
       "no priced round near $1B on record.")

# ---- ebenx
c("ebenx", status="acquired", rng="below_1b", country="US", city="Minneapolis", focus="Healthcare & Bio",
  stage="undetermined", entry_date="1996", rounds=[],
  note="Health benefits outsourcing company; SHPS agreed to buy it in November 2002 and the merger closed in early "
       "2003 (its 8-K and 15-12G on EDGAR). John Nehra joined the board in 1996, but no record names the round.")

# ---- echo-global-logistics: Series D preferred investor per the S-1
c("echo-global-logistics", country="US", city="Chicago", rng="below_1b", focus="Industrial & Robotics",
  stage="Growth", stage_src="web_verified", stage_cite=FTS("Echo Global", "S-1"), stage_conf="high",
  entry_date="2006",
  rounds=[rnd("2006", "Series D", None, None, True, FTS("Echo Global", "S-1"), "filing")],
  note="The S-1's waiver exhibit signs New Enterprise Associates 12 as the Series D preferred investor (the Series B "
       "holders are the founders' vehicles), and the firm's own year and Growth label are 2006; entry at Growth. "
       "Chicago freight brokerage, taken private by The Jordan Company in 2021.")

# ---- echodyne
c("echodyne", status="private", rng="below_1b", city="Kirkland", focus="Industrial & Robotics",
  stage="Growth", stage_src="web_verified", stage_cite=NEWS("echodyne", "$29M from NEA"), stage_conf="high",
  entry_date="2017-05",
  rounds=[rnd("2014-12", "Series A", 15000000, None, False, None, "filing"),
          rnd("2017-05", "Series B", 29000000, "New Enterprise Associates", True,
              NEWS("echodyne", "$29M from NEA"), "press"),
          rnd("2019-09", None, 20000000, None, None, NEWS("echodyne", "raises $20M from Bill Gates"), "press"),
          rnd("2022-06", "Series C", 135000000, "Bill Gates; Baillie Gifford", None,
              NEWS("echodyne", "$135M funding round led by Bill Gates"), "press")],
  note="NEA's first round was the $29M of May 2017 (GeekWire), the round after the $15M 2014 Series A, i.e. the "
       "Series B (the Lux book records it so); the firm's label reads Growth. The $135M 2022 Series C carried no "
       "published valuation. Kirkland, as in the Lux book.")

# ---- echopass-corporation
c("echopass-corporation", status="acquired", rng="below_1b", country="US", city="Salt Lake City",
  focus="SaaS", stage="undetermined", entry_date="2000", rounds=[],
  note="Hosted contact-center software, acquired by Genesys (the firm's exit line). The round NEA entered in 2000 "
       "is not named in any record.")

# ---- eci-acquisition-holdings
c("eci-acquisition-holdings", status="acquired", rng="below_1b", country="US", city="Westlake", focus="SaaS",
  stage="undetermined", entry_date="2006", rounds=[],
  note="ECI Software Solutions, now majority-owned by Leonard Green (2020) with Apax (2025) and based in Westlake, "
       "Texas (2025 press); the firm's page still reads Private. The 2006 transaction NEA joined is not named in "
       "any record, and the holding-company name may mark a control deal (R1), flagged for review.")

# ---- edimer-pharmaceuticals
c("edimer-pharmaceuticals", status="unknown", rng="below_1b", city="Cambridge", focus="Healthcare & Bio",
  stage="undetermined", entry_date="2013-07",
  rounds=[rnd("2013-07", None, 18000000, None, True, None, "filing")],
  note="Cambridge biotech developing EDI200 for XLHED; the $18M 2013 Form D with David Mott as director is NEA's "
       "entry, but no record names the round. No news of the company since the program moved on; its current "
       "state could not be established.")

# ---- edmodo
c("edmodo", status="acquired", rng="below_1b", city="San Mateo", focus="Consumer & Marketplaces",
  stage="undetermined", entry_date="2012", rounds=[],
  note="Acquired by NetDragon in 2018 for $137.5M (Wikipedia) and shut in 2022; San Mateo as in the USV and "
       "Greylock books. NEA's 2012 round is not named in any record on disk.")

# ---- eegeo
c("eegeo", status="unknown", rng="below_1b", city="Dundee", focus="Media, Gaming & Advertising",
  note="Dundee 3D-mapping company (later WRLD); no news of it after 2017 and its current state could not be "
       "established. " + GP)

# ---- eko: the known defunct and PL are a wrong join on a one-word name
c("eko", status="private", country="US", city="New York", rng="below_1b", focus="Media, Gaming & Advertising",
  stage="undetermined", entry_date="2013", rounds=[], flags=["model_disputes_source"],
  note="Eko (formerly Interlude), the New York interactive-video company, is operating: in May 2025 it announced a "
       "capture factory in Bentonville with Walmart (" + NEWS("eko", "Capture Factory") + "). The prefilled "
       "defunct status and Polish country came from a namesake. NEA's 2013 round is not named in any record.")

# ---- elastic
c("elastic", city="Amsterdam", country="NL", country_src="web_verified", country_cite=W("Elastic NV"),
  focus="Data Infrastructure", flags=["model_disputes_source"],
  stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014",
  rounds=[rnd("2012-11", "Series A", 10000000, "Benchmark", False, None, "press"),
          rnd("2013-02", "Series B", 24000000, "Index Ventures", False, None, "press"),
          rnd("2014-06", "Series C", 70000000, "New Enterprise Associates", True, None, "press")],
  note="Elastic N.V. is headquartered in Amsterdam (Wikipedia), as the Benchmark book records, so the prefilled US "
       "is replaced. NEA led the $70M Series C of June 2014 after Benchmark's A and Index's B; the firm's own year "
       "is 2014, so the entry is Growth.")

# ---- element3-health (renamed Grouper)
c("element3-health", status="private", rng="below_1b", country="US", city="Boston", city_src="web_verified",
  focus="Healthcare & Bio", stage="Seed", stage_src="first_party", stage_cite=SITE("element3-health"),
  stage_conf="medium", entry_date="2018",
  note="Renamed Grouper in January 2024 (" + NEWS("element3-health", "Changes Name to Grouper") + ", dateline "
       "Boston). The firm's own listing labels the 2018 entry Seed. " + GP)

# ---- elements-behavioral-health
c("elements-behavioral-health", status="defunct", rng="below_1b", city="Long Beach", focus="Healthcare & Bio",
  note="Addiction-treatment operator that filed for Chapter 11 in May 2018 (" +
       NEWS("elements-behavioral-health", "Files for Bankruptcy") + "); no sale of the business as a going "
       "concern is on record, so it reads defunct.")

# ---- elevenlabs
c("elevenlabs", country="US", city="New York", focus="AI & Applied AI", flags=["model_disputes_source"],
  stage="Growth", stage_src="web_verified", stage_cite=W("ElevenLabs"), stage_conf="high", entry_date="2025-01-30",
  rounds=[rnd("2023-01", "Pre-Seed", 2000000, "Credo Ventures", False, W("ElevenLabs"), "press"),
          rnd("2023-06", "Series A", 19000000, "Andreessen Horowitz", False, W("ElevenLabs"), "press"),
          rnd("2024-01-22", "Series B", 80000000, "Andreessen Horowitz", False, W("ElevenLabs"), "press"),
          rnd("2025-01-30", "Series C", 180000000, "Andreessen Horowitz; ICONIQ Growth", True, W("ElevenLabs"),
              "press"),
          rnd("2026-02-04", "Series D", 500000000, "Sequoia Capital", None, None, "press")],
  note="NEA came in as a new investor in the $180M Series C of January 2025 at $3.3B (the firm's year reads 2024, "
       "a close year). Momentum check 2026-09-30: the $11B Series D of February 2026 is the current mark. The "
       "Polish country was a Wikidata join; New York as in the a16z and ICONIQ books, though Wikipedia calls it "
       "London-based and Sequoia records Warsaw.")

# ---- elion
c("elion", status="private", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
  stage="Seed", stage_src="first_party", stage_cite=POST("elion-the-first"), stage_conf="high",
  entry_date="2022-10",
  rounds=[rnd("2022-10", "Seed", None, None, True, POST("elion-the-first"), "firm"),
          rnd("2025-08", "Seed", 9300000, "NEA", True,
              "https://www.alleywatch.com/2025/08/elion-ai-powered-healthcare-technology-procurement-vendor-marketplace-bobby-guelich/",
              "press")],
  note="The firm's own October 2022 post announces Elion's seed financing and its listing labels it Seed. The "
       "$9.3M NEA-led round of August 2025 was another seed (AlleyWatch; $12.6M raised in total), not a Series A. "
       + GP)

# ---- embrace
c("embrace", status="acquired", rng="below_1b", city="Los Angeles", focus="DevTools & APIs",
  stage="Growth", stage_src="first_party", stage_cite=POST("embracing-the-future"), stage_conf="high",
  entry_date="2021-10",
  rounds=[rnd("2021-10", "Series B", None, "New Enterprise Associates", True, POST("embracing-the-future"),
              "firm")],
  note="The firm's own October 2021 post announces 'our Series B investment in Embrace', its first-invested year "
       "is 2021; entry at Growth. The firm's exit line reads acquired by Palo Alto Networks, and the YC book also "
       "reads acquired; Los Angeles as in the YC book.")

# ---- embrane
c("embrane", status="acquired", rng="below_1b", country="US", city="Santa Clara", focus="Data Infrastructure",
  stage="undetermined", entry_date="2011", rounds=[],
  note="Network-services software, acquired by Cisco in April 2015 (" + NEWS("embrane", "Cisco Acquires") + "). "
       "NEA's 2011 round is not named in any record.")

# ---- enceladus
c("enceladus", status="private", rng="below_1b", country="US", city="Boston", focus="Healthcare & Bio",
  stage="Seed", stage_src="first_party", stage_cite=SITE("enceladus"), stage_conf="medium", entry_date="2022",
  note="Genome-editing biotech founded 2022 with Ali Behbahani on the board; the firm's listing labels the 2022 "
       "entry Seed. No press covers it and its own site is a placeholder; company profiles place it in Boston. " + GP)

# ---- endocardial-solutions
c("endocardial-solutions", status="acquired", rng="below_1b", country="US", city="Saint Paul",
  focus="Healthcare & Bio", stage="undetermined", entry_date="1993", rounds=[],
  note="Cardiac mapping company, listed in 1997 and acquired by St. Jude Medical (agreement September 2004, closed "
       "January 2005 per its EDGAR filings). The 1993 round is not named in any record.")

# ---- endotex
c("endotex", status="acquired", rng="below_1b", country="US", city="Cupertino", focus="Healthcare & Bio",
  stage="undetermined", entry_date="1996", rounds=[],
  note="Endotex Interventional Systems (NexStent carotid stent), acquired by Boston Scientific (the firm's exit "
       "line). The 1996 round is not named in any record.")

# ---- engine-yard
c("engine-yard", status="acquired", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
  stage="Growth", stage_src="model", stage_conf="medium", entry_date="2008-07",
  rounds=[rnd("2008-01", "Series A", 3500000, "Benchmark Capital", False, W("Engine Yard"), "press"),
          rnd("2008-07", "Series B", 15000000, None, True, W("Engine Yard"), "press"),
          rnd("2009-10", None, 19000000, None, True, W("Engine Yard"), "press")],
  note="NEA first appears in the $15M round of July 2008, the second round after Benchmark's $3.5M first round of "
       "January 2008 (Wikipedia), i.e. the Series B; the firm's own year is 2008. Acquired by Crossover in 2017.")

# ---- enigma: formd band Seed disputed by the NEA-led Series B
c("enigma", status="private", rng="below_1b", city="New York", focus="Data Infrastructure",
  stage="Growth", stage_src="web_verified", stage_cite=W("Enigma Technologies"), stage_conf="high",
  entry_date="2015-06", flags=["stage_disputes_band"],
  rounds=[rnd("2013-02", "Seed", 1100000, None, False, W("Enigma Technologies"), "press"),
          rnd("2014", None, 4500000, None, False, W("Enigma Technologies"), "press"),
          rnd("2015-06", "Series B", 28200000, "New Enterprise Associates", True, W("Enigma Technologies"), "press"),
          rnd("2018-09", None, 95000000, "New Enterprise Associates", True, W("Enigma Technologies"), "press")],
  note="NEA led the $28.2M Series B of June 2015 and the firm's own first-invested year is 2015; the 2013-14 seed "
       "and $4.5M rounds had no NEA money (Ben Narasin's Form D seat predates the firm's entry), so the Seed band "
       "is disputed. New York data company, still private. The Ribbit, Insight and Northzone rows named Enigma "
       "are other companies.")

# ---- envisia-therapeutics
c("envisia-therapeutics", status="acquired", rng="below_1b", country="US", city="Durham", focus="Healthcare & Bio",
  stage="undetermined", entry_date="2013", rounds=[],
  note="Liquidia spin-out developing a glaucoma implant, acquired by Aerie Pharmaceuticals in 2017 (" +
       NEWS("envisia-therapeutics", "Aerie beefing") + "). NEA's 2013 round is not named in any record.")

# ---- enzytech
c("enzytech", status="acquired", rng="below_1b", country="US", city="Cambridge", focus="Healthcare & Bio",
  stage="undetermined", entry_date="1987", rounds=[],
  note="Protein drug-delivery company merged into Alkermes (the firm's exit line; the Menlo book agrees). The 1987 "
       "round is not named in any record.")

# ---- epix-therapeutics
c("epix-therapeutics", status="acquired", rng="below_1b", country="US", city="Santa Clara", focus="Healthcare & Bio",
  stage="undetermined", entry_date="2014", rounds=[],
  note="Cardiac ablation company (formerly Advanced Cardiac Therapeutics), bought by Medtronic in 2019 for $316M ("
       + NEWS("epix-therapeutics", "put up $316m") + "); the firm's exit line names Ajax Health. NEA's 2014 round "
       "is not named in any record.")

# ---- epizyme
EPZ = "https://www.sec.gov/Archives/edgar/data/1571498/000119312513160271/d501246ds1.htm"
c("epizyme", country="US", city="Cambridge", rng="below_1b", focus="Healthcare & Bio",
  stage="Growth", stage_src="web_verified", stage_cite=EPZ, stage_conf="high", entry_date="2009-09",
  rounds=[rnd("2008-02", "Series A", None, None, False, FTS("Epizyme", "S-1"), "filing"),
          rnd("2009-09-18", "Series B", None, None, True, FTS("Epizyme", "S-1"), "filing"),
          rnd("2011-09", "Series B", 19000000, None, True, EPZ, "filing"),
          rnd("2012-04", "Series C", 25000000, "Celgene", False, EPZ, "filing")],
  note="The S-1's certain-transactions section lists New Enterprise Associates 13 among the Series B purchasers "
       "(agreement of 2009-09-18, tranche of September 2011) and the firm's own year is 2009, after the February "
       "2008 Series A; entry at Growth. Acquired by Ipsen in 2022.")

# ---- eroom
c("eroom", country="US", city="Cambridge", rng="below_1b", focus="SaaS", stage="undetermined", entry_date="1997",
  rounds=[],
  note="eRoom Technology, Cambridge collaboration software, acquired by Documentum in 2002 (the firm's exit line; "
       "the firm's description of telecom provisioning systems looks borrowed from another company). The 1997 "
       "round is not named in any record.")

# ---- erytech
c("erytech", status="defunct", rng="below_1b", country="FR", country_src="web_verified", country_cite=SITE("erytech"),
  city="Lyon", focus="Healthcare & Bio", stage="undetermined", entry_date="2020", rounds=[],
  note="Lyon biotech listed on Euronext since 2013; it absorbed Pherecydes in 2023 as Phaxiam Therapeutics, which "
       "went into receivership and then judicial liquidation and delisting in June 2025 (" +
       NEWS("erytech", "Judicial Liquidation") + "). The firm labels NEA's 2020 investment Public/PIPES, a "
       "purchase into a listed company, so under X1 the membership itself is in question; no round is staged.")

# ---- escient-pharmaceuticals
c("escient-pharmaceuticals", status="acquired", rng="below_1b", country="US", city="San Diego",
  focus="Healthcare & Bio", stage="undetermined", entry_date="2022", rounds=[],
  note="GPCR drug developer acquired by Incyte in 2024 (the firm's exit line). NEA's 2022 round is not named in "
       "any record on disk.")

# ---- esp-pharma
c("esp-pharma", status="acquired", rng="below_1b", country="US", city="Edison", focus="Healthcare & Bio",
  stage="Growth", stage_src="first_party", stage_cite=SITE("esp-pharma"), stage_conf="medium", entry_date="2002",
  note="Hospital specialty pharma acquired by Protein Design Labs in 2005; the firm's listing labels the 2002 "
       "entry Growth.")

# ---- esprit-pharma
c("esprit-pharma", status="acquired", rng="below_1b", country="US", city="East Brunswick", focus="Healthcare & Bio",
  stage="Growth", stage_src="first_party", stage_cite=SITE("esprit-pharma"), stage_conf="medium", entry_date="2004",
  note="Urology and women's health specialty pharma acquired by Allergan in 2007; the firm's listing labels the 2004 "
       "entry Growth.")

# ---- eucalyptus-systems
c("eucalyptus-systems", status="acquired", rng="below_1b", city="Goleta", city_src="formd_address",
  focus="Data Infrastructure", stage="undetermined", entry_date="2010",
  rounds=[rnd("2009-04", "Series A", 5500000, "Benchmark Capital", False, None, "press"),
          rnd("2010", None, 20200000, None, None, None, "filing"),
          rnd("2012-04", None, 30000000, None, True, None, "filing")],
  note="Open-source private-cloud software acquired by HP in 2014. Its Form D address is Goleta (Headline records "
       "Santa Barbara, the neighbouring city). The firm's year is 2010, the year of the $20.2M round after "
       "Benchmark's Series A, but no record ties NEA to that round by name.")

# ---- euclid-analytics: later $17M round graduates the Seed entry
EUC = "https://www.mediapost.com/publications/article/194024/euclid-raises-17-mil-aims-to-level-onlineofflin.html"
c("euclid-analytics", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
  grad="graduated", grad_src="web_verified", grad_cite=EUC, grad_conf="high",
  rounds=[rnd("2011-01", None, 5800000, None, True, None, "filing"),
          rnd("2013-02", None, 17000000, "Benchmark Capital", True, EUC, "press")],
  note="After the $5.8M round NEA entered (Form D, first sale January 2011), Benchmark led a $17M round in "
       "February 2013 with NEA participating (MediaPost), above twice the entry, so the row graduated. Acquired "
       "by WeWork in 2019.")

# ---- evalve
c("evalve", status="acquired", rng="below_1b", country="US", city="Menlo Park", focus="Healthcare & Bio",
  stage="Seed", stage_src="first_party", stage_cite=SITE("evalve"), stage_conf="medium", entry_date="1999",
  note="MitraClip developer acquired by Abbott in 2009; the firm's listing labels its 1999 entry Seed. " + GP)

# ---- evenly
c("evenly", status="private", rng="below_1b", country="US", city="Washington", city_src="web_verified",
  focus="Healthcare & Bio", stage="undetermined", entry_date="2019", rounds=[],
  note="Outsourced orthodontics for dental offices, founded 2019 in Washington, D.C. (search result profile); NEA "
       "first invested the same year but no record names the round.")

# ---- eventup
c("eventup", status="acquired", rng="below_1b", country="US", city="Los Angeles", focus="Consumer & Marketplaces",
  stage="Seed", stage_src="first_party", stage_cite=SITE("eventup"), stage_conf="medium", entry_date="2012",
  note="Venue-booking marketplace, now part of Tripleseat (its 2023 release: 'Tripleseat's EventUp', " +
       NEWS("eventup", "Tripleseat Introduces") + "). The firm's listing labels the 2012 entry Seed. " + GP)

# ---- everactive (fka PsiKick; base also carries psikick-inc)
c("everactive", status="private", rng="below_1b", city="Santa Clara", focus="Industrial & Robotics",
  note="Battery-free industrial IoT sensors (formerly PsiKick), still raising (a $13.4M Form D in 2024); no priced "
       "round near $1B. The base also carries psikick-inc, the same company.")

# ---- everfi
c("everfi", status="acquired", rng="below_1b", city="Washington", focus="SaaS",
  stage="undetermined", entry_date="2010", rounds=[],
  note="Digital-skills education company acquired by Blackbaud in 2021 (the firm's exit line). NEA's 2010 round is "
       "not named in any record.")

# ---- evernote
c("evernote", status="acquired", rng="below_1b", country="US", city="Redwood City", focus="Consumer & Marketplaces",
  stage="Growth", stage_src="model", stage_conf="medium", entry_date="2012",
  rounds=[rnd("2010-10", None, 20000000, "Sequoia Capital", False, W("Evernote"), "press")],
  note="NEA's first investment is 2012, after Sequoia's 2010 Series B and the 2011 round, so it entered at a later "
       "private round (Growth); the round is not cited. Acquired by Bending Spoons (announced November 2022); "
       "Redwood City as in the Coatue and Sequoia books.")

# ---- evernow: the firm's own post names the Series A it led; the Growth label is disputed
EVN = NEWS("evernow", "lands $28.5M series A")
c("evernow", status="private", rng="below_1b", country="US", focus="Healthcare & Bio", flags=["stage_disputes_band", "city_unknown"],
  stage="Series A", stage_src="first_party", stage_cite=POST("its-time-to-prioritize-menopause"),
  stage_conf="high", entry_date="2022-04",
  rounds=[rnd("2022-04-06", "Series A", 28500000, "New Enterprise Associates", True, EVN, "press")],
  note="The firm's own April 2022 post says NEA was grateful 'to lead Evernow's Series A financing' (the $28.5M "
       "round, Fierce Healthcare), so the listing's Growth label (year 2021, a close year) is disputed. The press "
       "and the company's pages read did not give its home city.")

jl.write("c4a", L)
