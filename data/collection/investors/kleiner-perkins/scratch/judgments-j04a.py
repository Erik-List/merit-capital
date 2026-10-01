"""Judge j04, batch 7 (Kleiner Perkins PRO-99): classification of the listed members, one sale-consideration verdict."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, W, FTS

GP = "Graduation left for the graduation pass."
L = []

# ---- oakley-networks
L.append(cls("oakley-networks", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004",
             country="US", city="Salt Lake City", focus="Security", rounds=[],
             note="Oakley Networks (data-leak prevention, Salt Lake City per the firm's 2008 listing) was bought by "
                  "Raytheon in 2007, the acquirer the firm's own page names. The firm's since-year is 2004; no record "
                  "on disk names the round it entered, so the stage is undetermined."))

# ---- ocarina-networks
w = W("Ocarina Networks")
L.append(cls("ocarina-networks", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=w, stage_conf="high", entry_date="2007", city="San Jose", focus="Data Infrastructure",
             rounds=[rnd("2007", "Series A", 12000000, None, True, w, "press"),
                     rnd("2009", "Series B", 20000000, None, True, w, "press")],
             note="Wikipedia: in 2007 Ocarina secured a $12M Series A from Kleiner Perkins Caufield & Byers and "
                  "Highland Capital, the firm's 2007 since-year; the 2009 Form D is the $20M follow-on, not the entry. "
                  "Dell bought Ocarina in 2010 (the firm's page names Dell)."))

# ---- oculeve
L.append(cls("oculeve", status="acquired", rng="below_1b", city="South San Francisco", focus="Healthcare & Bio",
             note="Oculeve (dry-eye device) was acquired by Allergan in 2015, the acquirer the firm's page names; "
                  "South San Francisco as in the NEA book."))

# ---- offermatic
L.append(cls("offermatic", status="unknown", rng="below_1b", city="Sunnyvale", city_src="formd_address",
             focus="Fintech & Payments",
             note="Offermatic (card-linked offers, 2010-11 Form D filings at 440 N. Wolfe Road, Sunnyvale). The firm "
                  "listed it as Private 2012-14 and then dropped it; no exit or shutdown is on record, so the state is "
                  "unknown. " + GP))

# ---- okay
tc_okay = "https://techcrunch.com/2023/05/31/okay-which-analyzes-engineers-productivity-sells-to-stripe/"
L.append(cls("okay", rng="below_1b", stage="undetermined", entry_date="2021", country="US",
             city="San Francisco", focus="DevTools & APIs", flags=["model_disputes_source"],
             rounds=[rnd("2023-05-31", "total raised before the sale (YC W20, then Sequoia and Kleiner Perkins)",
                         6600000, None, True, tc_okay, "press")],
             note="Okay (okayhq.com, engineering analytics, San Francisco) was bought by Stripe in May 2023 "
                  "(TechCrunch: it raised $6.6M in total from Sequoia and Kleiner Perkins after YC W20). The Wikidata "
                  "country CZ and acquirer 'OKAY Holding' belong to a Czech namesake: country US. The round the firm "
                  "entered in 2021 is not named on record."))

# ---- one-kings-lane
L.append(cls("one-kings-lane", status="acquired", rng="below_1b", city="San Francisco",
             focus="Consumer & Marketplaces",
             note="One Kings Lane (home decor flash sales, San Francisco) was acquired by Bed Bath & Beyond in 2016; "
                  "aligned with Greylock, IVP and Tiger Global."))

# ---- oni-systems
L.append(cls("oni-systems", status="acquired", rng="below_1b", stage="undetermined", country="US",
             city="San Jose", focus="Data Infrastructure", rounds=[],
             note="ONI Systems (optical networking, San Jose) went public in 2000 and was acquired by Ciena in 2002; "
                  "Kleiner Perkins funds filed 13Gs on it in 2001-02. No record gives the round the firm entered."))

# ---- openevidence
w = W("OpenEvidence")
L.append(cls("openevidence", stage="Growth", stage_src="web_verified", stage_cite=w, stage_conf="high",
             entry_date="2025-07", city="Miami", city_src="web_verified", focus="Healthcare & Bio",
             rounds=[rnd("2025-02", "Series A", 75000000, "Sequoia Capital", False, w, "press"),
                     rnd("2025-07", "unnamed (after the Series A)", 210000000, "GV; Kleiner Perkins", True, w, "press")],
             note="Wikipedia: Sequoia led the $75M Series A (Feb 2025) and GV and Kleiner Perkins led the $210M round "
                  "of July 2025, the firm's entry (its own post is dated 2025-07-15), a round after the A, so Growth. "
                  "Headquartered in Miami (Wikipedia), as GV and Coatue carry it."))

# ---- ophthonix-inc
L.append(cls("ophthonix-inc", status="unknown", rng="below_1b", city="Vista", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Ophthonix (iZon vision-correction lenses, 1491 Poinsettia Avenue, Vista per its 2010 Form D). No "
                  "exit or shutdown is on record, so the state is unknown. The Form D seed band is doubtful: the "
                  "company predates the 2008 Form D coverage and Joe Lacob sat on its board for years before 2010. "
                  "The base also carries it as izon-formerly-ophthonix and opthonix. " + GP))

# ---- opstrace
L.append(cls("opstrace", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="DevTools & APIs",
             note="Opstrace (open-source observability, 35 Divisadero Street, San Francisco per its 2020 Form D) was "
                  "acquired by GitLab in December 2021, the acquirer the firm's page names. " + GP))

# ---- optimedica
L.append(cls("optimedica", status="acquired", rng="below_1b", city="Santa Clara", focus="Healthcare & Bio",
             note="OptiMedica (cataract laser systems, Santa Clara per the firm's 2008 listing) was acquired by Abbott "
                  "in 2013. The firm's since-year (2005) predates the 2009 Form D the band reads, so the entry date "
                  "is likely earlier than the band's."))

# ---- optimizely
L.append(cls("optimizely", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
             note="Optimizely was acquired by Episerver in 2020 (the firm's page names Episerver); aligned with every "
                  "sibling book."))

# ---- optoro
w = W("Optoro")
L.append(cls("optoro", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=w,
             stage_conf="high", entry_date="2014-12", city="Washington", focus="SaaS",
             rounds=[rnd("2014-12", "Series C", 50000000, "Kleiner Perkins Caufield & Byers", True, w, "press"),
                     rnd("2016-12", "Series D", 30000000, None, True, w, "press")],
             note="Wikipedia: KPCB led Optoro's $50M Series C in December 2014 from its Green Growth Fund, the firm's "
                  "entry (the band's 2014-11-25 is the same round's Form D). Returns-logistics software, Washington DC, "
                  "still private; no priced round at $1B on record."))

# ---- orexigen
ore = FTS("Orexigen", "S-1")
L.append(cls("orexigen-therapeutics-inc", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=ore, stage_conf="high", entry_date="2004-01", country="US", city="San Diego",
             focus="Healthcare & Bio",
             rounds=[rnd("2004-01", "Series A", 11000000, None, True, ore, "filing"),
                     rnd("2005-04", "Series B", 35000000, None, True, ore, "filing"),
                     rnd("2006-11", "Series C", 30000000, None, True, ore, "filing")],
             note="The 2006 S-1's related-party table shows KPCB Holdings (for KPCB X-A and X-B) buying 3,389,831 "
                  "Series A shares in the January 2004 $11.0M round, when Joe Lacob joined the board. La Jolla (San "
                  "Diego). Bankrupt in 2018 and sold to Nalpropion, so acquired with a successor."))

# ---- osisoft
w = W("OSIsoft")
L.append(cls("osisoft", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=w,
             stage_conf="high", entry_date="2011-01", city="San Leandro", focus="Data Infrastructure",
             flags=["stage_disputes_band"],
             rounds=[rnd("2011-01-05", "minority growth investment", 135000000, "TCV; Kleiner Perkins", True, w, "press")],
             note="Wikipedia: on 2011-01-05 OSIsoft announced a $135M minority investment by TCV and KPCB (the Green "
                  "Growth Fund on the firm's archived page), an at-scale entry into a 1980 company, so Growth, not "
                  "the Form D seed band. AVEVA bought OSIsoft in 2021."))

# ---- pacific-biosciences-of-california
pb = FTS("PACIFIC BIOSCIENCES", "S-1")
L.append(cls("pacific-biosciences-of-california", stage="undetermined", entry_date="2004", city="Menlo Park",
             focus="Healthcare & Bio",
             rounds=[rnd("2008-07", "Series E", 188000000, None, True, pb, "filing"),
                     rnd("2010-06", "Series F", 109000000, None, True, pb, "filing")],
             note="The firm's since-year is 2004, when Brook Byers joined the board and KP entrepreneur-in-residence "
                  "Hugh Martin became CEO; the 2010 S-1 shows KPCB Holdings in the Series E and F but covers only "
                  "rounds from 2007, so the 2004 round is not named. The 2013 Form D date is a later round."))

# ---- palm: sale consideration
L.append(verdict("palm", "not_member",
                 "Sale consideration (Erik 2026-09-22; decisions.md R5): the firm's 'Palm' card (since 1998, founder "
                 "Jeff Hawkins) is its Handspring investment; KPCB held about 10% of Handspring when Palm bought it "
                 "in 2003 (S-4) and KPCB VIII then held palmOne stock (2004 proxy). Palm itself was a 3Com unit in "
                 "1998. Handspring is its own row.", ec="fund_filing", conf="high", cite=FTS("PALM", "S-4")))

# ---- path
w = W("Path (social network)")
L.append(cls("path", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_cite=w,
             stage_conf="medium", entry_date="2011-02", city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2011-02", "second round (after the 2010 seed)", 8500000,
                         "Kleiner Perkins Caufield & Byers; Index Ventures", True, w, "press"),
                     rnd("2014-01-11", "later round", 25000000, None, True, w, "press")],
             note="Wikipedia: in February 2011 Path raised its second round, $8.5M from KPCB (iFund/sFund on the "
                  "archived page) and Index, after the 2010 seed, which reads Series A; the Form D of 2011-01-28 is "
                  "this round. Acquired by Daum Kakao in 2015 (the app shut in 2018)."))

# ---- pattern
L.append(cls("pattern", status="private", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             flags=["model_disputes_source"],
             note="The firm's Pattern is Pattern Brands (patternbrands.com, home-goods brand group of Emmett Shine, "
                  "New York). The prefilled public status and $550M float come from a weak CIK join to Pattern Group, "
                  "an unrelated listed company; Pattern Brands is private with no exit found (web check 2026-09-30). "
                  "First Round's Pattern (a defunct SF SaaS row) looks like another company. " + GP))

# ---- peloton
L.append(cls("peloton", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2017",
             city="New York", focus="Consumer & Marketplaces",
             rounds=[rnd("2017-05", "Series E", 325000000, "TCV", None, None, "press")],
             note="The firm's since-year is 2017, when Peloton (founded 2012) had already raised four rounds; its 2017 "
                  "financing was the $325M Series E led by TCV, and KPCB Holdings signs the pre-IPO investor rights "
                  "agreement (S-1 exhibit). Any 2017 entry is Growth; KP's own round is not cited."))

# ---- permitflow
pf = POST("permitflow-series-a")
L.append(cls("permitflow", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
             stage_cite=pf, stage_conf="high", entry_date="2024-02", country="US", city="New York",
             focus="SaaS",
             rounds=[rnd("2024-02-21", "Series A", None, "Kleiner Perkins", True, pf, "firm"),
                     rnd("2024-12-03", "Series B", None, None, True, POST("permitflow-building-without-barriers"), "firm")],
             note="The firm's post of 2024-02-21 announces it led PermitFlow's Series A (YC W22, New York), matching "
                  "the 2024 since-year; its 2024-12-03 post covers the Series B. Construction-permitting software; no "
                  "priced round at $1B on record."))

# ---- persona
sa = "https://siliconangle.com/2025/04/30/identity-verification-startup-persona-raises-200m-2b-valuation/"
L.append(cls("persona", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=sa,
             asof="2025-04-30", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021",
             country="US", city="San Francisco", focus="Security", flags=["model_disputes_source"],
             extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2020-01", "Series A", 17500000, "Coatue", None, None, "press"),
                     rnd("2021", "Series B and Series C", None, None, None, None, "press"),
                     rnd("2025-04-30", "Series D", 200000000, "Founders Fund; Ribbit Capital", None, sa, "press")],
             note="Persona (identity verification, San Francisco; SiliconANGLE). The prefilled status acquired and "
                  "country RU are Wikidata joins to namesakes. The firm's since-year is 2021, after the January 2020 "
                  "Series A, so its entry is the 2021 Series B or C (Growth); which one is not on record. Mark: the "
                  "$200M Series D at $2B (2025-04-30), as Coatue, Insight and Ribbit carry it."))

# ---- phantom
L.append(cls("phantom", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2016", country="US", city="Palo Alto", focus="Security",
             rounds=[rnd("2016", "Series A", 13500000, "Kleiner Perkins Caufield & Byers", True, None, "press")],
             note="Phantom Cyber (security orchestration, phantom.us, Palo Alto) was bought by Splunk in 2018 for "
                  "about $350M. The firm's since-year 2016 matches the $13.5M Series A KPCB led that year (model, not "
                  "cited). The a16z, Lightspeed and Sequoia 'Phantom' rows are the crypto wallet, a different company."))

# ---- pharmacopeia
L.append(cls("pharmacopeia", rng="below_1b", stage="undetermined", country="US", city="Princeton",
             focus="Healthcare & Bio", rounds=[],
             note="Pharmacopeia (combinatorial chemistry, Princeton NJ as in Greylock and IVP) was acquired by Ligand in "
                  "2008; Kleiner Perkins funds filed 13Gs on it in 1997-98. No record names the round the firm entered."))

# ---- pharmacyclics
L.append(cls("pharmacyclics", rng="below_1b", stage="undetermined", entry_date="1991", city="Sunnyvale",
             focus="Healthcare & Bio", rounds=[],
             note="Pharmacyclics (Sunnyvale) was founded in 1991, the firm's since-year, and bought by AbbVie in 2015. "
                  "No record names the founding round the firm entered."))

# ---- phia
yh = "https://finance.yahoo.com/news/phia-raises-35m-series-build-154600100.html"
ph = POST("phia-the-ai-shopping-agent")
L.append(cls("phia", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=ph,
             stage_conf="high", entry_date="2024", grad="graduated", grad_src="web_verified", grad_cite=yh,
             grad_conf="high", city="New York", city_src="web_verified", focus="AI & Applied AI",
             flags=["stage_disputes_band"],
             extra={"valuation_range_source": "web_verified", "valuation_citation": yh, "valuation_asof": "2026-01-27"},
             rounds=[rnd("2025-09-18", "Seed", None, "Kleiner Perkins", True, ph, "firm"),
                     rnd("2026-01-27", "Series A", 35000000, "Notable Capital", True, yh, "company")],
             note="The firm's post (2025-09-18) says it led Phia's seed round; the firm dates the investment 2024, as "
                  "does the Form D first sale (2024-04-30), so Seed, not the band's Series A. Graduated: the company's "
                  "release of 2026-01-27 (New York) announces a $35M Series A led by Notable Capital with returning "
                  "investor Kleiner Perkins, at $185M. Momentum check 2026-09-30: that Series A at $185M is the last "
                  "priced round, below $1B."))

# ---- photon-dynamics
L.append(cls("photon-dynamics", status="acquired", rng="below_1b", stage="undetermined", country="US",
             city="San Jose", focus="Industrial & Robotics", rounds=[],
             note="Photon Dynamics (flat-panel test equipment, San Jose; KP general partner Floyd Kvamme its chairman) "
                  "was acquired by Orbotech in 2008; Kleiner Perkins funds filed 13Gs in 1998-99. The entry round is "
                  "not on record."))

# ---- pilot
pm = "https://www.pymnts.com/news/investment-tracker/2021/pilot-valuation-soars-in-extended-series-c-round/"
L.append(cls("pilot", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=pm,
             asof="2021-03-26", city="San Francisco", focus="Fintech & Payments", flags=["stale"],
             extra={"valuation_range_source": "web_verified"},
             note="Pilot (pilot.com, startup bookkeeping and tax, San Francisco). Last priced mark: the Series C "
                  "extended to $100M with Whale Rock and Bezos Expeditions at $1.2B (PYMNTS, 2021-03-26), over 24 "
                  "months old. Sequoia's row cites a vendor page for the same figure. Union Square Ventures' Pilot is "
                  "Pilot Fiber, a different company."))

# ---- pinterest
L.append(cls("pinterest", rng="10b_plus", usd=10700000000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/pins/market-cap/", asof="2026-09-30",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015", country="US",
             city="San Francisco", focus="Media, Gaming & Advertising",
             extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2015-05", "Series G", 367000000, None, None, None, "press")],
             note="The firm's since-year is 2015, when Pinterest (founded 2010) raised its $367M Series G at $11B, a "
                  "late round in any case, so Growth; KP's own round is not cited. Market cap $10.7B on 2026-09-30 "
                  "(StockAnalysis), fresher than the prefilled $18.7B and within 7% of the $10B edge."))

# ---- pivotal
pv = FTS("PIVOTAL CORP", "10-K")
L.append(cls("pivotal", status="acquired", rng="below_1b", stage="undetermined", entry_date="1992",
             country="CA", country_src="web_verified", country_cite=pv, city="North Vancouver",
             city_src="web_verified", focus="SaaS", flags=["model_disputes_source"], rounds=[],
             note="The firm's Pivotal is Pivotal Corporation, the CRM software maker whose 2001 10-K gives its head "
                  "office at 224 West Esplanade, North Vancouver, BC and lists KPCB VI at 3.61%; chinadotcom (CDC) "
                  "bought it in February 2004. The Wikidata ES country and the former-unicorn line (Pivotal Software, "
                  "2013) are other companies; the site's current blurb conflates them. Entry round not on record."))

# ---- pixtronix
L.append(cls("pixtronix", status="acquired", rng="below_1b", stage="undetermined", entry_date="2005",
             city="Andover", focus="Industrial & Robotics", rounds=[],
             note="Pixtronix (MEMS displays, Andover MA per the firm's listing) was acquired by Qualcomm in 2012. The "
                  "firm's since-year is 2005; the 2009 Form D filings are later rounds, and no record names the "
                  "round of 2005."))

# ---- plaid
tc18 = "https://techcrunch.com/2018/12/11/fintech-startup-plaid-raises-250m-at-a-2-65b-valuation/"
tc26 = "https://techcrunch.com/2026/02/26/plaid-valued-at-8b-in-employee-share-sale/"
L.append(cls("plaid", rng="1b_plus", usd=8000000000, val_src="web_verified", val_cite=tc26, asof="2026-02-26",
             stage="Growth", stage_src="web_verified", stage_cite=tc18, stage_conf="high", entry_date="2018-12-11",
             city="San Francisco", focus="Fintech & Payments", extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2018-12-11", "Series C", 250000000, "Mary Meeker (Kleiner Perkins growth fund)", True, tc18, "press"),
                     rnd("2026-02-26", "employee share sale", None, None, None, tc26, "press")],
             note="TechCrunch 2018-12-11: the $250M Series C at $2.65B was led by Mary Meeker with capital from "
                  "Kleiner Perkins' growth fund (a Digital Growth Fund position, IN under D2). Mark aligned with the "
                  "sibling books: the $13.4B 2021 unicorn-list figure yields to the $8B employee share sale "
                  "(TechCrunch, 2026-02-26), so the band moves from 10b_plus to 1b_plus."))

# ---- planetscale
pc = POST("planetscale-series-c")
L.append(cls("planetscale", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=pc, stage_conf="high", entry_date="2021-11", country="US", city="San Francisco",
             focus="Data Infrastructure",
             rounds=[rnd("2021-11-16", "Series C", 50000000, "Kleiner Perkins", True, pc, "firm")],
             note="The firm's post of 2021-11-16 announces 'our partnership with PlanetScale' and its lead investment "
                  "in the $50M Series C, its entry (since-year 2021). Momentum check 2026-09-30: the company's blog "
                  "(latest post 2026-09-10) and the firm's posts show no later priced round, none at $1B."))

# ---- plex
L.append(cls("plex", status="private", rng="below_1b", stage="undetermined", entry_date="2014", country="US",
             city="Campbell", city_src="web_verified", focus="Media, Gaming & Advertising", rounds=[],
             note="Plex (media server and free ad-supported streaming) is based in Campbell, California (Wikipedia). "
                  "The firm's since-year is 2014; no record names the round, and no priced round at $1B is known."))

# ---- power-integrations
L.append(cls("power-integrations", stage="undetermined", city="San Jose", focus="Industrial & Robotics",
             rounds=[],
             note="Power Integrations (power-conversion chips, San Jose). KP general partner Floyd Kvamme has sat on "
                  "the board since September 1989 (2001 10-K), which dates the relationship but names no round."))

# ---- practice-fusion
w = W("Practice Fusion")
L.append(cls("practice-fusion", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=w, stage_conf="high", entry_date="2013-09", city="San Francisco", focus="Healthcare & Bio",
             rounds=[rnd("2013-09", "Series D", 70000000, "Kleiner Perkins Caufield & Byers", True, w, "press")],
             note="Wikipedia: KPCB led the $70M Series D in September 2013 (a Digital Growth Fund position on the "
                  "archived page). Allscripts bought Practice Fusion in 2018."))

# ---- prisma
pr = POST("our-investment-in-prisma")
pb2 = "https://www.prisma.io/blog/prisma-raises-series-a-saks1zr7kip6"
te = "https://tech.eu/brief/prisma-series-a/"
L.append(cls("prisma", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=pr,
             stage_conf="high", entry_date="2018-05", grad="graduated", grad_src="first_party", grad_cite=pb2,
             grad_conf="high", country="DE", country_src="web_verified", country_cite=te, city="Berlin",
             focus="DevTools & APIs", flags=["model_disputes_source"],
             rounds=[rnd("2018-05-15", "Seed", 4500000, "Kleiner Perkins", True, pr, "firm"),
                     rnd("2020-06-26", "Series A", 12000000, "Amplify Partners", None, pb2, "company")],
             note="The firm's post (2018-05-15): Kleiner Perkins led a $4.5M seed in Prisma. Graduated: the company's "
                  "blog announces a $12M Series A led by Amplify Partners (2020-06-26). Tech.eu calls it a "
                  "German-American startup with offices in Berlin and San Francisco; Berlin, DE. The Wikidata CH "
                  "country and acquired status are namesakes; Prisma is private."))

# ---- productboard
L.append(cls("productboard", stage="undetermined", entry_date="2018", city="San Francisco",
             focus="SaaS", rounds=[],
             note="Productboard (founded in Prague, headquartered in San Francisco; Wikipedia names offices in both), "
                  "aligned with Tiger Global's San Francisco. The firm's since-year is 2018, before the Index-led Series "
                  "A and Sequoia-led Series B reported in the sibling notes; the round KP entered is not on record."))

# ---- progyny
pg = POST("progyny-helping")
L.append(cls("progyny", stage="undetermined", entry_date="2010-05", city="New York", focus="Healthcare & Bio",
             rounds=[],
             note="The firm's post: 'When we first invested in Progyny in May 2010' (then Auxogyn, incorporated 2008 as "
                  "Auxogen Bioscience); the round word is not given. New York (Wikipedia). The base also carries it "
                  "as auxogyn-inc."))

# ---- propel
L.append(cls("propel", status="private", rng="below_1b", stage="undetermined", entry_date="2018", country="US",
             city="New York", focus="Fintech & Payments", rounds=[],
             note="Propel (Providers app for SNAP/EBT households, Brooklyn, so New York). The firm's since-year is "
                  "2018; the round is not on record, and no priced round at $1B is known."))

# ---- proterra
L.append(cls("proterra", rng="below_1b", city="Burlingame", focus="Climate & Energy",
             note="Proterra (electric buses and batteries, Burlingame) filed Chapter 11 in August 2023 and sold its "
                  "businesses (batteries to Volvo, transit buses to Phoenix Motor), so acquired with successors."))

# ---- pulmonx
L.append(cls("pulmonx", city="Redwood City",
             note="Pulmonx is headquartered in Redwood City, as the firm's 2010 listing also gives."))

# ---- q
cc = "https://www.calcalistech.com/ctechnews/article/bjmwdmkizx"
L.append(cls("q", rng="below_1b", stage="undetermined", entry_date="2023-01", country="IL",
             country_src="web_verified", country_cite=cc, city="Ramat Gan", city_src="web_verified",
             focus="AI & Applied AI", flags=["model_disputes_source"],
             rounds=[rnd("2023-01", "unnamed", 24500000, None, True, cc, "press")],
             note="Q (q.ai, founded 2022 by Aviad Maizels, headquartered in Ramat Gan) raised $24.5M in January 2023 "
                  "from Kleiner Perkins, GV and others (Calcalist), matching the firm's 2023 since-year; the round is "
                  "not named. Apple bought it in January 2026 for about $1.5-2B. The Wikidata NO country is a namesake."))

# ---- quantumscape
L.append(cls("quantumscape", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2010",
             city="San Jose", focus="Climate & Energy",
             rounds=[rnd("2010", "Series A", None, None, None, "https://lsvp.com/company/quantumscape/", "firm")],
             note="QuantumScape was founded in 2010 (Wikipedia); the firm's since-year is 2010 and John Doerr has sat "
                  "on the board since December 2010 (2020 S-1). Lightspeed's own card calls its 2010 entry the Series "
                  "A; KP's participation in that round is inferred, not cited."))

# ---- quirky
w = W("Quirky (company)")
L.append(cls("quirky", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=w,
             stage_conf="high", entry_date="2012-09", city="New York", focus="Consumer & Marketplaces",
             rounds=[rnd("2010-04", "Series A", 6500000, "RRE Ventures", False, w, "press"),
                     rnd("2011-08", "Series B", 16000000, "Norwest Venture Partners", False, w, "press"),
                     rnd("2012-09", "Series C", 68000000, "Andreessen Horowitz; KPCB", True, w, "press"),
                     rnd("2013-11", "Series D", 79000000, "GE", True, w, "press")],
             note="Wikipedia: KPCB co-led the $68M Series C in September 2012 (Digital Growth Fund). Quirky filed "
                  "Chapter 11 on 2015-09-22 and its assets, site and products were bought by Q Holdings for $4.7M, "
                  "which relaunched it: acquired with a successor under the asset-sale rule; the a16z row reads "
                  "defunct."))

jl.write("j04a", L)
