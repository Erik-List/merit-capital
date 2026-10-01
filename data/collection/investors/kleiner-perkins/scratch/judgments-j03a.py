"""PRO-99 Kleiner Perkins, judge j03, queue batch 5 (inspire-medical-systems .. luvocracy): classification of listed
members. No membership was open in this batch."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, NEWS, ARCH, W, FTS

SA = "https://stockanalysis.com/stocks/{}/market-cap/"
GL = "Graduation left for the graduation pass."
TC_INSTACART = "https://techcrunch.com/2014/12/30/instacart-210m"
S1_LZ = FTS("LEGALZOOM COM", "S-1")
K8_LC = FTS("LendingClub", "8-K")
S1_IRONPLANET = FTS("IronPlanet", "S-1")
S1_INVUITY = FTS("Invuity", "S-1")

L = []

L.append(cls("inspire-medical-systems", city="Golden Valley", focus="Healthcare & Bio",
              note="Implantable nerve stimulation for sleep apnea; the company's EDGAR business address is Golden Valley, "
                   "Minnesota (the firm's 2010-14 listing gave Minneapolis)."))

L.append(cls("instacart", status="public", rng="1b_plus", usd=9980000000, val_src="web_verified",
              val_cite=SA.format("cart"), asof="2026-09-30", extra={"valuation_range_source": "web_verified"},
              stage="Growth", stage_src="web_verified", stage_cite=TC_INSTACART, stage_conf="high",
              entry_date="2014-12", city="San Francisco", focus="Consumer & Marketplaces",
              rounds=[rnd("2013-06", "Series A", 8500000, "Sequoia Capital", False, None, "press"),
                      rnd("2014-06", "Series B", 44000000, "Andreessen Horowitz", False, None, "press"),
                      rnd("2014-12-30", "Series C", 210000000, "Kleiner Perkins", True, TC_INSTACART, "press")],
              note="Listed on Nasdaq (CART, Maplebear Inc.) since 2023; market cap $9.98B on 2026-09-30 (stockanalysis), "
                   "under 1% below the $10B edge, fresher than the siblings' 10b_plus marks of 2026-09-02 to 09-25. "
                   "Kleiner Perkins led the Series C ($210M at over $2B, TechCrunch 2014-12-30, existing investors "
                   "Sequoia, Khosla and Canaan); the firm's page says it backed the seed in 2012, but no seed source "
                   "names the firm and its own stage field reads Growth."))

L.append(cls("internet-security-systems", country="US", city="Atlanta", rng="below_1b", stage="undetermined",
              entry_date="1997", focus="Security",
              rounds=[rnd("1997", "venture round (unnamed)", None, None, True, W("Internet Security Systems"), "press")],
              note="Network security software, Atlanta; bought by IBM in 2006. Wikipedia says Ted Schlein of Kleiner "
                   "Perkins invested in 'the next round' in 1997 without naming it (the site's 1982 year predates the "
                   "1994 founding), so the stage is undetermined."))

L.append(cls("intersect-ent", city="Menlo Park", rng="below_1b",
              stage="Series A", stage_src="model", stage_conf="medium", stage_cite=W("Intersect ENT"),
              entry_date="2006", focus="Healthcare & Bio",
              rounds=[rnd("2006", "Series A", None, None, None, W("Intersect ENT"), "press"),
                      rnd("2013", "Series D", 30000000, "Norwest Venture Partners", True, W("Intersect ENT"), "press")],
              note="ENT drug-device company, Menlo Park (EDGAR address); Medtronic closed its $1.1B purchase in May "
                   "2022. The firm's own since-year is 2006 and Wikipedia dates the company's first venture round, "
                   "its Series A, to 2006, with Kleiner Perkins among the pre-IPO investors."))

L.append(cls("intuit", city="Mountain View", stage="undetermined", entry_date="1990", focus="Fintech & Payments",
              rounds=[rnd("1990", "outside financing (unnamed)", None, None, True, SITE("intuit"), "firm")],
              note="Personal finance and tax software, Mountain View. The firm's case study says Scott Cook raised "
                   "outside money for the first time in 1990 and Kleiner Perkins backed the company that year; no "
                   "source names the round, so the stage is undetermined."))

L.append(cls("invuity", city="San Francisco", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
              rounds=[rnd("2012", "Series D", None, None, True, S1_INVUITY, "filing")],
              note="Surgical illumination devices, San Francisco; Stryker bought it in 2018. The S-1 shows KPCB XII "
                   "and its founders fund holding 11.2% and KPCB Holdings buying Series D in 2012, but the firm listed "
                   "Invuity from 2008, so the 2011-12-27 Form D date is a follow-on; the entry round is not named."))

L.append(cls("ionic-security", status="acquired", rng="below_1b", city="Atlanta", focus="Security",
              note="Data security software, Atlanta (EDGAR address); the firm lists it exited to Twilio."))

L.append(cls("ipierian", status="acquired", rng="below_1b", city="South San Francisco", focus="Healthcare & Bio",
              note="Stem-cell disease-model biotech, South San Francisco; Bristol-Myers Squibb bought it in 2014."))

L.append(cls("ironnet-cybersecurity", rng="below_1b", city="McLean", focus="Security",
              note="Cybersecurity company, McLean, Virginia (EDGAR address of IronNet, Inc.); listed through a SPAC "
                   "in 2021 and went through Chapter 11 in 2023, so no value is carried."))

L.append(cls("ironplanet", status="acquired", rng="below_1b", city="Pleasanton",
              stage="Series A", stage_src="model", stage_conf="medium", stage_cite=S1_IRONPLANET,
              entry_date="1999-11", focus="Consumer & Marketplaces",
              rounds=[rnd("1999", "Series A", None, None, True, S1_IRONPLANET, "filing"),
                      rnd("2014-10-31", "Form D offering", 24999999, None, True, None, "filing")],
              note="Online heavy-equipment marketplace, Pleasanton; Ritchie Bros bought it in 2017. The 2010 S-1 has "
                   "Ted Schlein on the board since November 1999, the year the company was founded, with the stake "
                   "held by KPCB IX (the 1999 fund) and Series A preferred outstanding by April 2000; the 2014 Form D "
                   "date is a follow-on."))

L.append(cls("itc-nexus-dx", status="acquired", rng="below_1b", city="San Diego", focus="Healthcare & Bio",
              note="Point-of-care diagnostics (ITC Nexus Holding, renamed Accriva Diagnostics; EDGAR address San "
                   "Diego), sold to Werfen in 2017. It was formed in 2010 around Nexus Dx (a separate row) and "
                   "International Technidyne."))

L.append(cls("jask", status="acquired", rng="below_1b", city="Austin", focus="Security",
              note="Autonomous security operations platform, Austin (Form D address, as the Battery row); Sumo Logic "
                   "bought it in 2019."))

L.append(cls("jive", rng="below_1b", city="Campbell", focus="SaaS",
              note="Enterprise collaboration software; its last EDGAR business address is Campbell, California "
                   "(earlier Palo Alto). Aurea (ESW Capital) bought it in 2017."))

L.append(cls("juniper-networks", city="Sunnyvale", rng="below_1b", stage="undetermined", entry_date="1996",
              focus="Data Infrastructure",
              rounds=[rnd("1996", "seed", 2000000, None, None, W("Juniper Networks"), "press"),
                      rnd("1996", "first-year funding", 12000000, None, None, W("Juniper Networks"), "press"),
                      rnd("1997", "venture round", 40000000, None, None, W("Juniper Networks"), "press")],
              note="Networking equipment, Sunnyvale; Hewlett Packard Enterprise completed its purchase in 2025. The "
                   "firm's since-year is 1996, but no source read ties Kleiner Perkins to a named round, so the stage "
                   "is undetermined."))

L.append(cls("kenandy", status="acquired", rng="below_1b", city="Redwood City",
              stage="Series A", stage_src="model", stage_conf="medium", stage_cite=W("Kenandy"),
              entry_date="2011-08", focus="SaaS", flags=["stage_disputes_band"],
              rounds=[rnd("2011-08", "first round", 10500000, "Kleiner Perkins", True, W("Kenandy"), "press"),
                      rnd("2013", "Series B (first close)", None, None, True, W("Kenandy"), "press"),
                      rnd("2016-03", "Series B", 11500000, None, True, W("Kenandy"), "press")],
              note="Cloud ERP, Redwood City; Rootstock Software bought it on 2018-01-11. Wikipedia says Kleiner Perkins "
                   "led the company's first round ($10.5M, August 2011) and calls the 2013 round the first close of "
                   "the Series B, so the entry is the Series A, not the Growth band read off the 2013 Form D."))

L.append(cls("ketera", status="acquired", rng="below_1b", country="US", city="Santa Clara", stage="undetermined",
              entry_date="2003", focus="SaaS", rounds=[],
              note="Cloud procurement network (Ketera Technologies, Santa Clara), bought by Rearden Commerce, later "
                   "Deem, as the firm's listing says. No source read names the round of the firm's 2003 entry."))

L.append(cls("kinsa", status="acquired", rng="below_1b", city="San Francisco",
              stage="Series A", stage_src="model", stage_conf="medium", stage_cite=W("Kinsa"), entry_date="2014",
              focus="Healthcare & Bio",
              rounds=[rnd("2014", "first venture round", 9600000, "Kleiner Perkins", True, W("Kinsa"), "press"),
                      rnd("2017-03", "Series B", 17000000, "GSR Ventures", None, W("Kinsa"), "press")],
              note="Smart thermometers, San Francisco; bought by Healthy Together in January 2024. Kleiner Perkins led "
                   "the 2014 $9.6M raise that preceded the March 2017 Series B, so the entry is the Series A (the "
                   "2016-12 Form D date is the Series B)."))

L.append(cls("kovio", status="acquired", rng="below_1b", city="San Jose", focus="Industrial & Robotics",
              note="Printed silicon electronics, San Jose; Thin Film Electronics bought its technology, IP and "
                   "equipment on 2014-01-21 as the company wound down (an asset sale, successor Thinfilm)."))

L.append(cls("legalzoom", status="public", rng="below_1b", usd=960800000, val_src="web_verified",
              val_cite=SA.format("lz"), asof="2026-09-30", city="Glendale",
              stage="Growth", stage_src="model", stage_conf="medium", stage_cite=S1_LZ, entry_date="2011",
              focus="Consumer & Marketplaces",
              rounds=[rnd("2011", "common stock purchase (growth fund)", None, None, True, S1_LZ, "filing")],
              note="Online legal documents, Glendale; Nasdaq LZ, market cap $960.8M on 2026-09-30 (stockanalysis). "
                   "The 2012 S-1 shows the stake held as common stock by KPCB Digital Growth Fund and its founders "
                   "fund, a growth-fund purchase in the firm's 2011 entry year, so the entry reads Growth."))

L.append(cls("lehigh-technologies", status="acquired", rng="below_1b", city="Tucker", focus="Climate & Energy",
              stage="undetermined", flags=["stage_disputes_band"],
              rounds=[rnd("2008", "venture rounds from 2008 (unnamed)", 50000000, None, True, W("Lehigh Technologies"), "press"),
                      rnd("2012-06-01", "Form D offering", 19007643, None, None, None, "filing")],
              note="Recycled rubber powders, Tucker, Georgia (EDGAR address; the 2008-11 listing gave Naples, "
                   "Florida); Michelin bought it in October 2017. The Pre-Seed band read a $120K 2009 filing, but the "
                   "firm held it through the KPCB Green Growth Fund and Wikipedia puts over $50M of venture money in "
                   "from 2008, so no named round supports a stage."))

L.append(cls("lendingclub", country="US", city="San Francisco", stage="Growth", stage_src="web_verified",
              stage_cite=K8_LC, stage_conf="high", entry_date="2012-06-01", focus="Fintech & Payments",
              rounds=[rnd("2007-08", "Series A", 10260000, None, False, None, "press"),
                      rnd("2012-06-01", "Series E", 17500000, "Kleiner Perkins", True, K8_LC, "filing")],
              note="Online lending marketplace, San Francisco. The company's 8-K of June 2012 says Kleiner Perkins was "
                   "the lead investor in its $17.5M Series E of 2012-06-01, the firm's first round."))

L.append(cls("lifelock", city="Tempe", rng="below_1b", stage="Growth", stage_src="web_verified",
              stage_cite=W("LifeLock"), stage_conf="high", entry_date="2007-04", focus="Security",
              rounds=[rnd("2006", "Series A", 5000000, "Bessemer Venture Partners", False, W("LifeLock"), "press"),
                      rnd("2007-04", "Series B", 6000000, "Kleiner Perkins", True, W("LifeLock"), "press"),
                      rnd("2008-01", "Series C", 25000000, "Goldman Sachs", None, W("LifeLock"), "press")],
              note="Identity theft protection, Tempe; Symantec bought it in 2017. Wikipedia: LifeLock raised a $6M "
                   "Series B from Kleiner Perkins in April 2007, after Bessemer's 2006 Series A."))

L.append(cls("lightspan-inc", status="acquired", rng="below_1b", country="US", city="San Diego",
              stage="undetermined", focus="Consumer & Marketplaces", rounds=[],
              note="Educational software (Lightspan Partnership, San Diego), merged into PLATO Learning in 2003, as the "
                   "firm's 2012 page marked it 'Merged'. A 2001 13G by the firm's funds is on file; no source read "
                   "names its entry round."))

L.append(cls("lilliputian-systems", status="defunct", rng="below_1b", city="Wilmington", focus="Climate & Energy",
              note="Miniature fuel cells, Wilmington, Massachusetts; the company shut down in 2014 without a sale."))

L.append(cls("linear-technology", status="acquired", country="US", city="Milpitas", rng="below_1b",
              stage="undetermined", focus="Industrial & Robotics", flags=["model_disputes_source"], rounds=[],
              note="Analog semiconductors, Milpitas; Analog Devices bought it in March 2017, so acquired, not defunct. "
                   "No source read names the firm's early round. The 20VC, Accel and Sequoia 'Linear' rows at $1.25B are "
                   "the software company Linear, a different firm."))

L.append(cls("livongo", city="Mountain View", rng="below_1b", focus="Healthcare & Bio",
              note="Chronic-condition digital health, Mountain View; Teladoc bought it in 2020."))

L.append(cls("lockerz", status="defunct", rng="below_1b", city="Seattle", focus="Consumer & Marketplaces",
              note="Social commerce site, Seattle; renamed Ador (EDGAR name Ador, Inc.), its site shut in 2014 and "
                   "redirected to Ador until 2016, with no sale recorded."))

L.append(cls("looker", status="acquired", rng="below_1b", country="US", city="Santa Cruz",
              stage="Growth", stage_src="web_verified", stage_cite=W("Looker (company)"), stage_conf="high",
              entry_date="2016-01-14", focus="Data Infrastructure",
              rounds=[rnd("2013-08-13", "Series A", 18000000, "Redpoint Ventures", False, W("Looker (company)"), "press"),
                      rnd("2015-03-11", "Series B", 30000000, None, False, W("Looker (company)"), "press"),
                      rnd("2016-01-14", "Series C", 48000000, "Kleiner Perkins", True, W("Looker (company)"), "press")],
              note="BI and analytics, Santa Cruz; Google bought it in 2020. Kleiner Perkins' first round was the $48M "
                   "Series C of 2016-01-14 (Wikipedia; the firm's post of the same day)."))

L.append(cls("loom", status="acquired", rng="below_1b", city="San Francisco",
              stage="Series A", stage_src="first_party", stage_cite=POST("loom-putting"), stage_conf="high",
              entry_date="2019-02", focus="SaaS",
              rounds=[rnd("2016-10", "Seed", 600000, None, False, W("Loom, Inc."), "press"),
                      rnd("2019-02", "Series A", 11000000, "Kleiner Perkins", True, W("Loom, Inc."), "press"),
                      rnd("2019-11", "Series B", 30000000, "Sequoia Capital", True, W("Loom, Inc."), "press"),
                      rnd("2021-05", "Series C", 130000000, "Andreessen Horowitz", True, W("Loom, Inc."), "press")],
              note="Video messaging, San Francisco; Atlassian bought it for $975M in 2023. The firm's post says it led "
                   "Loom's Series A (February 2019 per Wikipedia); the prefilled 2019-10 date is the Series B filing."))

L.append(cls("lotus-development", status="acquired", rng="below_1b", country="US", city="Cambridge",
              stage="undetermined", focus="SaaS", rounds=[],
              note="Spreadsheet and groupware pioneer, Cambridge, Massachusetts; IBM bought it in 1995. Wikipedia "
                   "credits Ben Rosen's 1982 backing; no source read names the firm's round."))

L.append(cls("lsi", country="US", city="San Jose", rng="below_1b", stage="undetermined", entry_date="1981",
              focus="Industrial & Robotics",
              rounds=[rnd("1981", "initial funding", 6000000, None, True, W("LSI Corporation"), "press")],
              note="LSI Logic, later LSI Corporation, San Jose; Avago (now Broadcom) bought it in 2014. Wikipedia says "
                   "its initial $6M came from a consortium including Kleiner Perkins Caufield & Byers II, without "
                   "naming the round."))


SILICON_JUNA = "https://siliconangle.com/2024/11/18/industrial-ai-startup-juna-ai-raises-7-5m-seed-funding/"
COOLEY_INTEROS = "https://www.cooley.com/news/coverage/2021/2021-08-02-interos-reaches-unicorn-status-with-series-c-round"
TC_INTEROS = "https://techcrunch.com/2024/10/24/supply-chain-startup-interos-lands-new-customers-cash/"
FORBES_LABELBOX = "https://www.forbes.com/sites/kenrickcai/2022/01/06/data-startup-labelbox-series-d-funding-from-softbank/"
CB_INWORLD = "https://www.crunchbase.com/funding_round/inworld-ai-seed--3a307fb1"
VB_INWORLD = "https://venturebeat.com/business/inworld-ai-joins-metaverse-innovation-with-ai-driven-virtual-characters"
SA_INWORLD = "https://siliconangle.com/2022/08/23/inworld-ai-raises-50m-ai-powered-no-code-virtual-character-development-studio/"
S1_LUCA = FTS("Luca Technologies", "S-1")

L.append(cls("instaedu", status="acquired", rng="below_1b", city="San Francisco", stage="undetermined",
             entry_date="2012", focus="Consumer & Marketplaces",
             rounds=[rnd("2013-07-02", "Form D offering", 4000000, None, None, jl.FORMD_CITE("instaedu", 0), "filing")],
             note="Online tutoring, San Francisco; Chegg bought it in 2014. The firm lists a 2012 entry; the only "
                  "filing is the $4M Form D of 2013-07-02, whose director Mamoon Hamid was then at Social Capital "
                  "(he joined Kleiner Perkins in 2017), so it locates another firm, and no source read names the "
                  "firm's 2012 round."))

L.append(cls("interos", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
             val_cite=COOLEY_INTEROS, asof="2021-08-02", extra={"valuation_range_source": "web_verified"},
             flags=["stale"], city="Arlington", focus="SaaS",
             note="Supply-chain risk platform, Arlington, Virginia. The $100M Series C of August 2021, led by "
                  "NightDragon with Kleiner Perkins and Venrock, took the valuation to more than $1B (Cooley, "
                  "2021-08-02); the October 2024 $40M Blue Owl round came without a published price (TechCrunch), "
                  "so the 2021 mark stands, stale."))

L.append(cls("inworld", status="private", rng="below_1b", country="US", city="Mountain View",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=VB_INWORLD,
             entry_date="2021-11-09", focus="AI & Applied AI",
             grad="graduated", grad_src="web_verified", grad_cite=SA_INWORLD, grad_conf="high", grad_asof="2022-08-23",
             rounds=[rnd("2021-11-09", "Seed", 7000000, None, True, VB_INWORLD, "press"),
                     rnd("2022-08-23", "Series A", 50000000, "Section 32, Intel Capital", True, SA_INWORLD, "press"),
                     rnd("2023-08", "Series A-1", 80100000, "Lightspeed Venture Partners", None, CB_INWORLD, "vendor")],
             note="AI characters for games (Inworld AI, legally Theai Inc.). Its $7M seed of 2021-11-09 named Kleiner "
                  "Perkins, CRV and Meta as investors (VentureBeat), the firm's 2021 entry; the $50M Series A of "
                  "2022-08-23, led by Section 32 and Intel Capital with Kleiner Perkins, graduates it (SiliconANGLE). "
                  "Momentum check 2026-09-30 (Google News and web search): the last priced round found is the August "
                  "2023 A-1 at about $520M post by vendor figures, no $1B+ round."))

L.append(cls("juna-ai", status="private", country="DE", country_src="web_verified", country_cite=SILICON_JUNA,
             city="Berlin", stage="Seed", stage_src="web_verified", stage_cite=SILICON_JUNA, stage_conf="high",
             entry_date="2024-11-18", grad="censored", rng="below_1b", focus="AI & Applied AI",
             extra={"valuation_range_source": "web_verified", "valuation_citation": SILICON_JUNA,
                    "valuation_asof": "2026-09-30"},
             rounds=[rnd("2024-11-18", "Seed", 7500000, "Kleiner Perkins", True, SILICON_JUNA, "press")],
             note="Industrial AI agents, Juna.ai GmbH of Berlin. Kleiner Perkins led its $7.5M seed (SiliconANGLE, "
                  "2024-11-18), after the censoring date. Momentum check 2026-09-30 (Google News): only the seed "
                  "coverage, no $1B+ round."))

L.append(cls("juvaris-biotherapeutics-inc", status="unknown", rng="below_1b", city="Burlingame",
             focus="Healthcare & Bio",
             note="Adjuvanted vaccines, Burlingame; its last Form D is from 2010 and the firm's listing dropped it "
                  "after 2012, and no source read states a sale or shutdown."))

L.append(cls("karma-science", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2011", focus="Consumer & Marketplaces", rounds=[],
             note="Social gifting app (Karma), bought by Facebook in 2012 as the firm's listing says; the sFund "
                  "entry of 2011 is not tied to a named round in any source read."))

L.append(cls("katango", status="acquired", rng="below_1b", country="US", stage="undetermined", entry_date="2010",
             focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
             note="Automatic friend-grouping app backed from the iFund and sFund, bought by Google in 2011 as the firm "
                  "lists; no source read names its round or places the company in a city."))

L.append(cls("klout", status="acquired", rng="below_1b", city="San Francisco", stage="undetermined",
             entry_date="2010", focus="Media, Gaming & Advertising", rounds=[],
             note="Social influence scores, San Francisco; Lithium Technologies bought it for $200M in March 2014 "
                  "(Wikipedia) and closed the service in 2018. The firm's sFund entry year is 2010; no source read "
                  "names that round."))

L.append(cls("labelbox", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
             val_cite=FORBES_LABELBOX, asof="2022-01-06", extra={"valuation_range_source": "web_verified"},
             flags=["stale"], country="US", city="San Francisco", stage="undetermined", entry_date="2018",
             focus="AI & Applied AI", rounds=[],
             note="Training-data platform, San Francisco; the $110M Series D of January 2022 valued it at $1B "
                  "(Forbes, as the a16z and First Round rows), stale. The firm lists a 2018 entry labelled Early; no "
                  "source read ties it to a named round."))

L.append(cls("lightforce-orthodontics", status="private", rng="below_1b", country="US", city="Burlington",
             stage="Growth", stage_src="first_party", stage_cite=POST("lightforce"), stage_conf="high",
             entry_date="2021-10-05", focus="Healthcare & Bio",
             rounds=[rnd("2021-10-05", "Series C", None, "Kleiner Perkins", True, POST("lightforce"), "firm")],
             note="3D-printed orthodontic brackets, Burlington, Massachusetts. The firm's post of 2021-10-05 says it "
                  "led the Series C, its 2021 entry."))

L.append(cls("luca-technologies", status="unknown", rng="below_1b", city="Golden", focus="Climate & Energy",
             stage="undetermined", flags=["stage_disputes_band"],
             rounds=[rnd("2006", "venture and private equity offerings 2006-2008", 99000000, None, True, S1_LUCA, "filing")],
             note="Microbial coal-bed methane, Golden, Colorado; it filed an S-1 in 2011 but never listed, and no source read states "
                  "its later fate. The Pre-Seed band read a $20,600 filing of 2009, but the S-1 names Kleiner Perkins "
                  "among the backers of about $99M raised in 2006-2008 (the KPCB Green Growth Fund held it), so no "
                  "round supports a stage. The Menlo and YC 'Luca' rows are other companies."))

L.append(cls("lumafield", status="private", rng="below_1b", country="US", city="Boston", stage="undetermined",
             entry_date="2019", focus="Industrial & Robotics", rounds=[],
             note="Industrial CT scanning, Boston (as the IVP and Spark rows). The firm lists a 2019 entry labelled "
                  "Early; no source read names that round."))

L.append(cls("lumeris", status="private", rng="below_1b", country="US", city="St. Louis", stage="undetermined",
             entry_date="2011", focus="Healthcare & Bio", rounds=[],
             note="Value-based care services, St. Louis. The firm lists a 2011 entry; no source read names the round."))

L.append(cls("luvocracy", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2012", focus="Consumer & Marketplaces", rounds=[],
             note="Social product recommendations, San Francisco; @WalmartLabs bought it in 2014 (the firm's listing "
                  "and the GV row). No source read names the firm's 2012 round."))

jl.write("j03a", L)
