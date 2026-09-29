"""PRO-75 grind, judge j16: queue batch 16 (45 member rows, all archive-only listings, tier B).
Pattern copied from judgments-pilot.py. Every citation below was printed by a tool run in this session (the
TechCrunch and Crunchbase News WordPress search, nq.py through NEWS(), EDGAR full-text search and Form D
primary documents, stockanalysis.com, company sites fetched with curl, wikifetch.py through W()) or read with
WebFetch. Rows with no source tying GV to a named round read `undetermined` and keep the rounds that were found.

Two pairs of rows are one company each (reported, not merged here): developer-auction and hired (DeveloperAuction
rebranded as Hired.com in September 2013), djz and crossfader (Crossfader was built by Seth Goldstein's DJZ team)."""
import importlib.util
import os
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
CHECK = "2026-09-28"
WV = {"valuation_range_source": "web_verified"}
# a row the float layer pre-filled as public from a same-name registrant: the float describes another company
NO_FLOAT = {"valuation_source": None, "valuation_range_source": None, "valuation_asof": None,
            "valuation_confidence": None}
GRAD_LEFT = " Graduation left for the graduation pass."


def sec(cik, acc):
    """A Form D primary document on EDGAR (the URL printed by the j16 Form D reader)."""
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/primary_doc.xml"


# ---------------------------------------------------------------- Creator (formerly Momentum Machines)
TC_CREATOR = "https://techcrunch.com/2018/06/21/creator-hamburger-robot/"
L.append(cls("creator", status="defunct", rng="below_1b", country="US", city="San Francisco",
             focus="Industrial & Robotics", stage="undetermined",
             note="Robot-made burgers (San Francisco), founded as Momentum Machines (2009, incorporated 2012) and "
                  "renamed Creator in 2017; the base row already absorbed momentum-machines. Backed by GV, Khosla "
                  "Ventures and Root Ventures, and it 'raised at least $18.3 million in 2017' per its filing "
                  "(TechCrunch, 2018-06-21); its Form Ds ($345K from 2013-03-28, $18.4M from 2017-05-26 with Khosla's "
                  "Sven Strohband a director, $13.0M from 2021-06-29 as Creator, Inc.) name no GV director, and no "
                  "source read names the round GV entered, so the stage is undetermined. "
                  "Status follows the Khosla row (closed permanently in 2023); the restaurant reopened in Daly City "
                  "in August 2021 (San Francisco Chronicle) and no later operating trace was found.",
             rounds=[rnd("2013-03-28", "unnamed ($345K sold)", 345368, None, None,
                         sec(1573131, "0001573131-13-000001"), "filing"),
                     rnd("2017-05-26", "unnamed ($18.4M sold)", 18386815, None, None,
                         sec(1573131, "0001573131-17-000004"), "filing"),
                     rnd("2021-06-29", "unnamed ($13.0M sold, as Creator, Inc.)", 13003080, None, None,
                         sec(1573131, "0001573131-21-000002"), "filing")]))

# ---------------------------------------------------------------- Crittercism (Apteligent)
CRIT_SEED = ("https://techcrunch.com/2011/07/13/crittercism-raises-1-2-million-from-kleiner-perkins-and-google-"
             "ventures-for-app-support/")
CRIT_A = "https://techcrunch.com/2012/06/01/crittercism-series-a/"
CRIT_B = ("https://techcrunch.com/2013/03/12/crittercism-lands-12m-from-google-ventures-more-to-help-mobile-"
          "developers-monitor-app-network-performance/")
L.append(cls("crittercism", status="acquired", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CRIT_SEED, entry_date="2011-07",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CRIT_A,
             note="Mobile app performance monitoring (San Francisco), renamed Apteligent; VMware announced its "
                  "acquisition on 2017-05-15 (Wikipedia, Apteligent). Google Ventures was in the seed announced "
                  "2011-07-13 with Kleiner Perkins, Opus, Shasta and AOL Ventures ($1.2M; TechCrunch), re-upped in "
                  "the $5.5M Series A of June 2012 with Opus and Shasta (TechCrunch, 2012-06-01), and led the $12M "
                  "Series B of March 2013 (TechCrunch). The named Series A graduates the seed.",
             rounds=[rnd("2011-07-13", "Seed", 1200000, None, True, CRIT_SEED, "press"),
                     rnd("2012-06-01", "Series A", 5500000, "Opus Capital; Shasta Ventures; Google Ventures", True,
                         CRIT_A, "press"),
                     rnd("2013-03-12", "Series B", 12000000, "Google Ventures", True, CRIT_B, "press")]))

# ---------------------------------------------------------------- DJZ and Crossfader (one company)
TC_DJZ = "https://techcrunch.com/2012/10/31/djz/"
TC_XF = "https://techcrunch.com/2014/06/27/crossfader-app/"
DJZ_ROUNDS = [rnd("2012-10-31", "unnamed ($1M at DJZ's launch)", 1000000, None, True, TC_DJZ, "press"),
              rnd("2014-06-27", "unnamed ($2M for Crossfader)", 2000000, None, None, TC_XF, "press")]
DJZ_NOTE = ("DJZ, Seth Goldstein's electronic dance music media company (launched October 2012), and its mobile "
            "DJ app Crossfader are one company: 'Crossfader was created by Seth Goldstein's DJZ team' (TechCrunch, "
            "2014-06-27); the base carries both rows (djz, crossfader). GV's round: DJZ launched 'with $1 million in "
            "funding' from Kleiner Perkins, Google Ventures, Index, True, Troy Carter and Shari Redstone (TechCrunch, "
            "2012-10-31), its first round and seed-sized for 2012 (model: Seed, medium); Crossfader later took $2M "
            "from Shawn Gruver and Telegraph Hill Capital. No source read gives the company's fate (crossfader.fm no "
            "longer answers), so status is unknown, and none places its office.")
for s in ("djz", "crossfader"):
    L.append(cls(s, status="unknown", rng="below_1b", country="US", focus="Media, Gaming & Advertising",
                 stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TC_DJZ, entry_date="2012-10",
                 flags=["city_unknown"], note=DJZ_NOTE + GRAD_LEFT, rounds=DJZ_ROUNDS))

# ---------------------------------------------------------------- CustomMade
W_CM = W("CustomMade")
BBJ_CM = NEWS("custommade", "co-leads $4M")
WN_CM = NEWS("custommade", "Wayfair Hires")
L.append(cls("custommade", status="acquired", rng="below_1b", country="US", city="Cambridge",
             focus="Consumer & Marketplaces", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=W_CM, entry_date="2011-11",
             note="Marketplace for custom-made goods (Lechmere Square, Cambridge MA). 'In November 2011, CustomMade "
                  "raised $2.1 million in Series A funding from First Round Capital, Google Ventures, and others', and "
                  "Google Ventures co-led the $4M round of April 2012 (Wikipedia; Boston Business Journal headline, "
                  "2012-04-30). Status: Wikipedia says Wayfair acquired the business on 2015-05-21 (Woodworking "
                  "Network's headline frames it as Wayfair hiring its staff while CustomMade retrenched), and in May "
                  "2017 the founder re-purchased the business out of foreclosure with WTI; custommade.com still "
                  "trades as a custom jeweler (read 2026-09-28). A sale with a successor entity reads acquired with "
                  "this note. The First Round row reads defunct ('wound down after 2018', uncited); this row holds "
                  "the cited sale.",
             rounds=[rnd("2011-11", "Series A", 2100000, None, True, W_CM, "press"),
                     rnd("2012-04-30", "unnamed ($4M)", 4000000, "Google Ventures (co-lead)", True, BBJ_CM,
                         "press")]))

# ---------------------------------------------------------------- DailyCred (born Shopobot)
TC_SHOPOBOT = ("https://techcrunch.com/2011/06/16/price-tracking-service-shopobot-raises-funding-from-google-"
               "ventures-aol-and-others/")
DC_SITE = "http://www.dailycred.com/"
L.append(cls("dailycred", status="defunct", rng="below_1b", country="US", focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SHOPOBOT, entry_date="2011-06",
             flags=["city_unknown"],
             note="Authentication as a service, 'born as Shopobot' (an AngelPad price-tracking startup). Shopobot "
                  "'raised an undisclosed amount of seed funding from Google Ventures, AOL Ventures' and others "
                  "(TechCrunch, 2011-06-16); the company's own farewell calls Google Ventures 'our first major "
                  "investor' and says 'DailyCred ended all public APIs and services December 31st, 2020' "
                  "(dailycred.com, read 2026-09-28). No source read places its office." + GRAD_LEFT,
             rounds=[rnd("2011-06-16", "Seed", None, None, True, TC_SHOPOBOT, "press")]))

# ---------------------------------------------------------------- DataPad
TC_DP = "https://techcrunch.com/2014/05/20/data-discovery-technology-nets-datapad-1-7-million/"
VB_DP = NEWS("datapad", "Cloudera acquires business-intelligence")
L.append(cls("datapad", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Data Infrastructure", stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TC_DP,
             entry_date="2014-05",
             note="Collaborative data analysis (San Francisco), founded 2013 by Wes McKinney (pandas) and Chang She. "
                  "It raised '$1.7 million in very early stage funding' from Accel, Google Ventures, a16z's seed fund, "
                  "SV Angel and Ludlow (TechCrunch, 2014-05-20): its only round, unnamed, seed-sized (model: Seed). "
                  "Cloudera acquired its technology assets and team on 2014-09-30 and shut the service "
                  "(VentureBeat), an announced acquisition, so acquired; the a16z row reads defunct, and this row "
                  "holds the cited acquisition." + GRAD_LEFT,
             rounds=[rnd("2014-05-20", "unnamed (very early stage)", 1700000, None, True, TC_DP, "press")]))

# ---------------------------------------------------------------- DeveloperAuction and Hired (one company)
TC_DA = "https://techcrunch.com/2013/03/14/developerauction/"
TC_REBRAND = "https://techcrunch.com/2013/09/17/developer-auction-is-hired-com/"
TC_VETTERY = NEWS("hired", "Vettery acquires Hired")
HIRED_ROUNDS = [rnd("2013-03-14", "unnamed ($2.7M)", 2700000, None, True, TC_DA, "press"),
                rnd("2014-11-25", "unnamed ($14.98M sold)", 14981791, None, None, sec(1570934, "0001570934-14-000005"),
                    "filing")]
HIRED_NOTE = ("Tech-talent marketplace. DeveloperAuction rebranded as Hired.com in September 2013 (TechCrunch, "
              "2013-09-17), so developer-auction and hired are one company. GV's round: DeveloperAuction 'raised $2.7 "
              "million from NEA, Sierra Ventures, Crosslink Capital, Google Ventures' and others in March 2013 "
              "(TechCrunch, 2013-03-14); the round is unnamed and sits above the era's seed ceiling, and the next "
              "filing ($14.98M sold from 2014-11-25, Hired, Inc., San Francisco) names no round either, so the stage "
              "is undetermined. Vettery, part of the Adecco Group, acquired Hired in November 2020 (TechCrunch, "
              "2020-11-23; Wikipedia). City: San Francisco, its Form D address.")
for s in ("developer-auction", "hired"):
    L.append(cls(s, status="acquired", rng="below_1b", country="US", city="San Francisco", city_src="formd_address",
                 focus="Consumer & Marketplaces", stage="undetermined", note=HIRED_NOTE, rounds=HIRED_ROUNDS))

# ---------------------------------------------------------------- Disruptor Beam (Beamable)
TC_DB_B = "https://techcrunch.com/2017/02/02/disruptor-beam-series-b/"
GI_BEAM = NEWS("disruptor-beam", "Disruptor Beam rebrands as Beamable")
WBJ_DB = NEWS("disruptor-beam", "Framingham-company")
W_RADOFF = W("Jon Radoff")
BW_BEAM = NEWS("disruptor-beam", "Skillz Acquires Beamable’s Technology")
L.append(cls("disruptor-beam", status="acquired", rng="below_1b", city="Boston", city_src="formd_address",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Licensed social and mobile games (Game of Thrones Ascent, Star Trek Timelines), Framingham MA "
                  "(Worcester Business Journal, 2016). It sold its games, reorganized and relaunched as Beamable, a "
                  "live-game services platform (GamesIndustry.biz, 2020-04-22). 'Skillz acquired Beamable in January "
                  "2026' (Wikipedia, Jon Radoff); Skillz's own release of 2026-02-04 says it acquired Beamable's "
                  "technology (Business Wire: " + BW_BEAM + "), a purchase of the product, which reads acquired. City: "
                  "Boston, Beamable's address on its 2022 Form D (the "
                  "last before the sale; Framingham through 2021). Rounds: a $3.2M Series A, which its Form D "
                  "tranches of 2013-14 ($771K, $820K, $1.62M) add up to, and an $8.5M Series B led by GrandBanks and "
                  "Romulus (TechCrunch, 2017-02-02; Form D from 2017-01-26); no filing names a GV director and no "
                  "source read names the round GV entered, so the stage is undetermined.",
             rounds=[rnd("2013-03-18", "unnamed ($771K sold)", 771000, None, None,
                         sec(1579283, "0001579283-13-000001"), "filing"),
                     rnd("2013-11-05", "unnamed ($820K sold)", 820000, None, None,
                         sec(1579283, "0001579283-13-000002"), "filing"),
                     rnd("2014-08-11", "unnamed ($1.62M sold)", 1624965, None, None,
                         sec(1579283, "0001579283-14-000001"), "filing"),
                     rnd(None, "Series A ($3.2M in total)", 3200000, None, None, TC_DB_B, "press"),
                     rnd("2017-02-02", "Series B", 8500000, "GrandBanks Capital; Romulus Capital", None, TC_DB_B,
                         "press"),
                     rnd("2021-10-26", "unnamed ($5.27M sold, as Beamable)", 5270181, None, None,
                         sec(1579283, "0001579283-22-000002"), "filing")]))

# ---------------------------------------------------------------- EchoEcho
TC_EE = ("https://techcrunch.com/2012/05/07/google-ventures-backed-location-sharing-service-echoecho-raises-750k-"
         "from-bullpen-profounders/")
RT_EE = NEWS("echoecho", "Echoecho raises $750K")
VS_EE = NEWS("echoecho", "Vancouver company personalizes")
L.append(cls("echoecho", status="unknown", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=VS_EE, city="Vancouver", city_src="web_verified", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TC_EE, entry_date="2011-09",
             note="Friend-finding and meet-up app (CEO Nick Bicanic), a Vancouver BC company ('EchoEcho: Vancouver "
                  "company personalizes location-based service', Vancouver Sun, 2011-03-10). 'Last September, "
                  "EchoEcho raised $750,000 from Google Ventures, UK-based venture firm PROfounders and Don Dodge', "
                  "then another $750K led by Bullpen Capital (TechCrunch, 2012-05-07; Reuters headline, 2011-09-09): "
                  "GV's round is the company's first, unnamed and seed-sized (model: Seed). No source read gives its "
                  "fate; Bicanic ran a dating app, flikdate, by 2014." + GRAD_LEFT,
             rounds=[rnd("2011-09", "unnamed ($750K)", 750000, None, True, RT_EE, "press"),
                     rnd("2012-05-07", "unnamed ($750K)", 750000, "Bullpen Capital", None, TC_EE, "press")]))

# ---------------------------------------------------------------- Envelop VR
UV_ENV = NEWS("envelop", "Envelop VR Has Closed")
FD_ENV = sec(1626289, "0001626289-16-000004")
L.append(cls("envelop", status="defunct", rng="below_1b", country="US", city="Bellevue", city_src="formd_address",
             focus="SaaS", stage="undetermined",
             note="Virtual-reality desktop and productivity software (Bellevue WA, its Form D address). 'Envelop VR has "
                  "closed', announced 2017-01-11 (UploadVR). Its $4M round of October 2015 was led by Madrona "
                  "(UploadVR; the Form D, amended February 2016, reports $5.55M sold with Madrona's Matt McIlwain "
                  "as director); no source read names GV in a round, so the stage is undetermined.",
             rounds=[rnd("2015-10-30", "unnamed ($5.55M sold)", 5550074, "Madrona Venture Group", None, FD_ENV,
                         "filing")]))

# ---------------------------------------------------------------- EventBoard (Teem)
TC_EB = "https://techcrunch.com/2015/11/11/eventboard-a-smart-conference-room-booking-startup-raises-6-5m/"
TC_TEEM = ("https://techcrunch.com/2018/09/12/wework-makes-it-third-biggest-acquisition-to-date-shelling-out-100-"
           "million-for-a-software-startup-called-teem/")
INV_TEEM = NEWS("eventboard", "WeWork Acquires Meeting Room")
L.append(cls("eventboard", status="acquired", rng="below_1b", country="US", city="Salt Lake City",
             city_src="web_verified", focus="SaaS", stage="undetermined",
             note="Meeting-room and workplace software (Salt Lake City), renamed Teem: 'Teem started its operating "
                  "life as Eventboard' (Sixteen:Nine, 2018-09-14). WeWork acquired Teem for $100M in September 2018 "
                  "(TechCrunch, 2018-09-12). GV's round: EventBoard 'was previously backed by investors like Google "
                  "Ventures and Marc Benioff' when Greycroft led its $6.5M round in November 2015 (TechCrunch); no "
                  "source read names the round GV entered, so the stage is undetermined.",
             rounds=[rnd("2015-11-11", "unnamed ($6.5M)", 6500000, "Greycroft Partners", None, TC_EB, "press")]))

# ---------------------------------------------------------------- Fauna
TC_FAUNA = "https://techcrunch.com/2020/07/01/fauna-raises-an-additional-27m-to-turn-databases-into-a-simple-api-call/"
REG_FAUNA = NEWS("fauna", "FaunaDB shuts down")
FD_FAUNA16 = sec(1676363, "0001676363-16-000001")
FD_FAUNA17 = sec(1676363, "0001676363-17-000002")
L.append(cls("fauna", status="defunct", rng="below_1b", country="US", city="San Francisco",
             city_src="formd_address", focus="Data Infrastructure", stage="undetermined",
             flags=["model_disputes_source"],
             note="FaunaDB, a serverless operational database (San Francisco, its Form D address), founded by "
                  "Twitter veterans. FaunaDB shut down in May 2025 (The Register, 2025-03-24). Country disputes the "
                  "prefilled CZ claim, a one-word name match. Rounds: $3.1M sold in May 2016 and $21.75M of a $25M "
                  "round in August 2017 (Form Ds; the 2017 one names Point72's Daniel Gwak as director), then $27M in "
                  "July 2020, 'technically an extension of the company's 2017 Series A', led by Madrona with GV "
                  "participating (TechCrunch, 2020-07-01). GV held the company by October 2017 (the firm's listing), "
                  "and no source read says whether it entered at the 2016 round or the 2017 Series A, so the stage "
                  "is undetermined.",
             rounds=[rnd("2016-05-26", "unnamed ($3.1M sold)", 3109994, None, None, FD_FAUNA16, "filing"),
                     rnd("2017-08-31", "Series A ($21.75M sold of $25M)", 21750017, None, None, FD_FAUNA17, "filing"),
                     rnd("2020-07-01", "Series A extension", 27000000, "Madrona Venture Group", True, TC_FAUNA,
                         "press")]))

# ---------------------------------------------------------------- Favor (The Pill Club)
TC_PC_B = "https://techcrunch.com/2019/01/22/the-pill-club-raises-51m-as-vcs-find-new-opportunities-in-womens-health/"
TC_PC_BX = "https://techcrunch.com/2021/06/14/the-pill-club-takes-on-primary-care-with-41-9m-in-fresh-funding/"
FIERCE_PC = NEWS("favor", "Thirty Madison scoops up assets")
FEM_PC = NEWS("favor", "Favor, Formerly Known as The Pill Club")
BBG_PC = NEWS("favor", "Goes Bankrupt After False Billing")
L.append(cls("favor", status="acquired", rng="below_1b", country="US", city="San Carlos", city_src="web_verified",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=TC_PC_B, entry_date="2019-01", flags=["model_disputes_source"],
             note="Favor is The Pill Club (heyfavor.com; 'Favor, Formerly Known as The Pill Club', Femtech Insider, "
                  "2022-09-06), a birth-control and women's telehealth company in San Carlos CA (TechCrunch, "
                  "2019-01-22). GV came in as a new investor in the $51M Series B led by VMG Partners (TechCrunch, "
                  "2019-01-22) and was an existing investor in the $41.9M Series B extension of June 2021. The company "
                  "filed for bankruptcy in April 2023 (Bloomberg) and Thirty Madison bought its assets in June 2023 "
                  "(Fierce Healthcare); heyfavor.com now serves Nurx, 'a Thirty Madison company' (read 2026-09-28). "
                  "Insolvency followed by an asset sale reads acquired. Status and country dispute the prefilled "
                  "defunct and FR, a one-word name match on another Favor.",
             rounds=[rnd("2019-01-22", "Series B", 51000000, "VMG Partners", True, TC_PC_B, "press"),
                     rnd("2021-06-14", "Series B extension", 41900000, "Base10 Partners", True, TC_PC_BX, "press")]))

# ---------------------------------------------------------------- Florence (Fabric)
FABRIC = "https://www.fabrichealth.com/about"
PR_FLO = ("https://www.prnewswire.com/news-releases/florence-launches-modern-healthcare-experience-with-20m-seed-"
          "round-led-by-thrive-capital-gv-and-salesforce-ventures-301785372.html")
FAB_A = "https://www.fabrichealth.com/blog/60m-series-a-led-by-general-catalyst"
HD_FLO = NEWS("florence", "Florence buys Zipnosis from Bright Health")
L.append(cls("florence", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="Healthcare & Bio", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PR_FLO,
             entry_date="2023-03", grad="graduated", grad_src="first_party", grad_conf="high", grad_cite=FAB_A,
             flags=["model_disputes_source"],
             note="Florence (florenceos.com, which now redirects to fabrichealth.com), founded in 2021 to cut "
                  "emergency-department operating costs, New York. It launched with a '$20M Seed Round Led by Thrive "
                  "Capital, GV, and Salesforce Ventures' (PR Newswire, 2023-03-30), bought Zipnosis from Bright "
                  "Health in May 2023 (Healthcare Dive), and renamed itself Fabric in 2024 (the company's own history "
                  "page). Fabric's $60M Series A of 2024-02-27, led by General Catalyst with GV participating (the "
                  "company's own post), graduates the seed. Operating as Fabric, a care-access platform. Country "
                  "disputes the prefilled MA claim, a one-word name match. The sibling rows are filed under the new "
                  "name (Thrive and General Catalyst, 'fabric': private, New York; aligned); the Redpoint and YC rows "
                  "named Fabric are other companies. No priced mark near $1B is on record.",
             rounds=[rnd("2023-03-30", "Seed", 20000000, "Thrive Capital; GV; Salesforce Ventures", True, PR_FLO,
                         "company"),
                     rnd("2024-02-27", "Series A", 60000000, "General Catalyst", True, FAB_A, "company")]))

# ---------------------------------------------------------------- Flux (Flux Factory)
TC_FLUX_A = ("https://techcrunch.com/2014/05/06/flux-the-first-startup-to-spin-out-of-google-x-nabs-8m-for-its-eco-"
             "home-building-platform/")
TC_FLUX_B = "https://techcrunch.com/2015/12/21/google-x-alum-flux-factory-raises-29m-series-b/"
AN_FLUX = NEWS("flux", "Flux to shut down its data-sharing")
L.append(cls("flux", status="unknown", rng="below_1b", usd=None, country="US", city="San Francisco",
             city_src="web_verified", focus="SaaS", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=TC_FLUX_A, entry_date="2014-05", flags=["model_disputes_source"], extra=NO_FLOAT,
             note="Flux Factory (flux.io), the first Google X spinout, collaborative building-design software, "
                  "San Francisco (TechCrunch, 2015-12-21). Status and figure dispute the prefilled public row and its "
                  "$55.8M float, a same-name registrant; country disputes the CZ claim. The 8VC, Bain Capital "
                  "Ventures and Headline rows named Flux are other companies (flux.ai; a UK receipts fintech). GV's "
                  "round: the $8M led by DFJ with Borealis, a16z, Google Ventures and Ev Williams (TechCrunch, "
                  "2014-05-06), the company's only round before the $29M 'Series B' of December 2015, so the record "
                  "names it the Series A (model). Flux shut its tool suite on 2018-03-31 to pivot to a product for "
                  "real estate professionals (The Architect's Newspaper, 2018-02-26); no source read gives the "
                  "company's later fate and flux.io no longer answers, so status is unknown.",
             rounds=[rnd("2014-05-06", "unnamed ($8M, the Series A by the record)", 8000000, "DFJ", True,
                         TC_FLUX_A, "press"),
                     rnd("2015-12-21", "Series B", 29000000, "Temasek; Surbana Jurong", None, TC_FLUX_B, "press")]))

# ---------------------------------------------------------------- Free
TC_FREE = "https://techcrunch.com/2015/06/11/get-free/"
L.append(cls("free", status="unknown", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="model", stage_conf="medium",
             stage_cite=TC_FREE, entry_date="2015-06", flags=["model_disputes_source"],
             note="Free (ffrree.com), an app to share real-time availability with friends, co-founded by Danny Trinh "
                  "(ex-Path) and Kelvin Kakugawa; it 'raised $1.9 million from top seed funds like Social+Capital, "
                  "Google Ventures, Lowercase, First Round, and SV Angel' (TechCrunch, 2015-06-11): its only round, "
                  "seed-sized and described as a seed (model: Seed). Status and country dispute the prefilled "
                  "acquired and FR: the Wikidata match is Free, the French telecom brand, another company. No source "
                  "read gives this app's fate, so status is unknown; the First Round row (the same company, First "
                  "Round is in the round) carries the same wrong acquired. City San Francisco as in the First Round "
                  "row (model)." + GRAD_LEFT,
             rounds=[rnd("2015-06-11", "unnamed ($1.9M from seed funds)", 1900000, None, True, TC_FREE, "press")]))

# ---------------------------------------------------------------- Glimpse
TNW_GL = "https://thenextweb.com/news/glimpse-completely-overhauls-ios-app-help-meet-relevant-people-instagram"
L.append(cls("glimpse", status="unknown", rng="below_1b", usd=None, country="US", focus="Consumer & Marketplaces",
             stage="undetermined", flags=["model_disputes_source", "city_unknown"], extra=NO_FLOAT,
             note="Glimpse (itsglimpse.com), a 2014 iOS app to meet people through Instagram, backed by 'First Round "
                  "Capital, Google Ventures, Sherpa Ventures, Undercurrent Ventures, William Lauder and various "
                  "angels' (The Next Web, 2014-08-01). Status and figure dispute the prefilled public row and its "
                  "$41M float, which belong to The Glimpse Group (NASDAQ: VRAR). The First Round row is the same "
                  "company (unknown there too); the 8VC row (a CPG company) and the Greylock row (a 2005 shopping "
                  "site) are other companies. No source read names GV's round or gives the company's fate; the "
                  "domain now hosts an unrelated dating site. No source places its office.",
             rounds=[]))

# ---------------------------------------------------------------- Greenwork
L.append(cls("greenwork", status="private", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             stage="undetermined", flags=["city_unknown"],
             note="Greenwork (joingreenwork.com) connects young tradespeople with jobs and training for "
                  "decarbonization work; its site is live (© 2026, read 2026-09-28). No source read names GV's round "
                  "or places its office.",
             rounds=[]))

# ---------------------------------------------------------------- Homejoy
TC_HJ_SEED = "https://techcrunch.com/2013/03/05/homejoy-seed-funding/"
TC_HJ_AB = "https://techcrunch.com/2013/12/05/homejoy-38-m/"
W_HJ = W("Homejoy")
L.append(cls("homejoy", status="defunct", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_HJ_AB, entry_date="2013-12",
             note="On-demand home cleaning (San Francisco, YC 2010); shut down on 2015-07-31 (Wikipedia). GV was not "
                  "in the $1.7M seed of March 2013 (a16z, First Round and angels; TechCrunch). The $38M announced "
                  "2013-12-05 came in 'a Series A led by Google Ventures and a Series B led by Redpoint Ventures' "
                  "(TechCrunch); Wikipedia's line that Google Ventures led the Series B contradicts that contemporary "
                  "report, and the First Round row agrees with TechCrunch.",
             rounds=[rnd("2013-03-05", "Seed", 1700000, None, False, TC_HJ_SEED, "press"),
                     rnd("2013-12-05", "Series A", None, "Google Ventures", True, TC_HJ_AB, "press"),
                     rnd("2013-12-05", "Series B", None, "Redpoint Ventures", True, TC_HJ_AB, "press")]))

# ---------------------------------------------------------------- Humanoid (SpeakerText)
TC_HUM = "https://techcrunch.com/2011/11/02/humanoid-google-ventures/"
TC_CF = ("https://techcrunch.com/2013/03/03/cloudfactory-launches-cloudfactory-2-0-platform-after-acquiring-"
         "speakertext-humanoid/")
L.append(cls("humanoid", status="acquired", rng="below_1b", country="US", focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_HUM, entry_date="2011-11",
             flags=["model_disputes_source", "city_unknown"],
             note="Humanoid, a 'human brainpower API' for crowdsourced tasks, came out of SpeakerText (a New York "
                  "issuer on its 2010 Form D). After SpeakerText's $600K angel round (February 2011), 'Google "
                  "Ventures is putting in a few hundred thousand dollars in another seed round' (TechCrunch, "
                  "2011-11-02). CloudFactory acquired SpeakerText and Humanoid in October 2012 (TechCrunch, "
                  "2013-03-03), which confirms the prefilled acquired. Country disputes the prefilled NL claim, a "
                  "one-word name match; no source read places Humanoid's own office in 2011-12." + GRAD_LEFT,
             rounds=[rnd("2011-02", "angel ($600K, as SpeakerText)", 600000, "Mitch Kapor", False, TC_HUM, "press"),
                     rnd("2011-11-02", "Seed", None, None, True, TC_HUM, "press")]))

# ---------------------------------------------------------------- Jetpack Technologies (Jetify)
TC_JP = "https://techcrunch.com/2023/02/01/jetpack-io-helps-developers-focus-on-applications-instead-of-infrastructure/"
TC_JETIFY = "https://techcrunch.com/2025/01/28/jetify-launches-testpilot-its-ai-qa-engineer/"
LAW_JETIFY = NEWS("jetpack-technologies", "GC AI Acquires Backend Software Company Jetify")
L.append(cls("jetpack-technologies", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="DevTools & APIs", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_JP,
             entry_date="2023-02",
             note="Jetpack.io (Devbox, Testpilot), founded by Daniel Loreto; 'Jetify Inc., formerly Jetpack "
                  "Technologies Inc.' (jetpack.io, read 2026-09-28). Its '$10 million seed' was 'co-led by Coatue and "
                  "GV' (TechCrunch, 2023-02-01); Jetify launched Testpilot in January 2025 (TechCrunch). GC AI, a "
                  "legal-AI company, acquired Jetify in August 2026 (Law.com headline, 2026-08-10: " + LAW_JETIFY +
                  "), which aligns with the Coatue row ('Acq. by GC AI, 2026'). No later priced round was found. City "
                  "San Francisco, as in the Coatue row (model)." + GRAD_LEFT,
             rounds=[rnd("2023-02-01", "Seed", 10000000, "Coatue; GV", True, TC_JP, "press")]))

# ---------------------------------------------------------------- JoyTunes (Simply)
CALC_JT = NEWS("joytunes", "joins unicorn club with $50 million")
GLOBES_JT = NEWS("joytunes", "raising $50m at $1b valuation")
W_JT = W("Simply (software company)")
L.append(cls("joytunes", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=GLOBES_JT,
             asof="2021-06-21", country="IL", country_src="web_verified", country_cite=CALC_JT, city="Tel Aviv",
             focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=CALC_JT, entry_date="2021-06", flags=["stale"], clear=("unicorn_name_match",), extra=WV,
             note="Music-learning apps (Simply Piano), renamed Simply in July 2022 (Wikipedia). GV led a $50M round "
                  "at a $1B valuation in June 2021 with Qualcomm Ventures and Hearst Ventures (Globes and Calcalist, "
                  "2021-06-21), its first investment: the company had raised '$43 million in three funding rounds' "
                  "before it (Calcalist), a $5M Series A in 2014 among them (Wikipedia), so the round reads Growth. "
                  "Mark: $1B exactly, at the band edge, and older than 24 months (stale); Wikipedia's $97M raised to "
                  "date shows no later priced round. Israeli company, all 100 staff in Israel (Calcalist); the "
                  "prefilled IL is confirmed from the company's own record.",
             rounds=[rnd("2014-08", "Series A", 5000000, "Aleph", False, W_JT, "press"),
                     rnd("2019", "unnamed ($25M)", 25000000, "Qumra Capital", False, W_JT, "press"),
                     rnd("2021-06-21", "unnamed ($50M at $1B)", 50000000, "GV", True, CALC_JT, "press")]))

# ---------------------------------------------------------------- Juicero
TC_JU_B = "https://techcrunch.com/2016/03/31/investors-pour-70-million-into-juicero-a-smart-kitchen-appliance-maker/"
W_JU = W("Juicero")
L.append(cls("juicero", status="defunct", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Wi-Fi cold-press juicer (San Francisco); ceased operations in September 2017 (Wikipedia). Artis "
                  "Ventures led the $70M Series B of March 2016, and 'Juicero's Series A and B investors included "
                  "Kleiner Perkins Caufield & Byers, GV (formerly Google Ventures), Thrive Capital' and others "
                  "(TechCrunch, 2016-03-31), which does not say whether GV entered at the A or the B; its Form Ds "
                  "($4M from 2013-09-11, $15.9M from 2014-03-28, filed from New York) name no GV director, and no "
                  "other source read separates the rounds, so the stage is undetermined.",
             rounds=[rnd("2013-09-11", "unnamed ($4M sold, Brooklyn)", 4000000, None, None,
                         sec(1588182, "0001588182-13-000002"), "filing"),
                     rnd("2014-03-28", "unnamed ($15.9M sold of $19.3M)", 15881830, None, None,
                         sec(1588182, "0001588182-14-000002"), "filing"),
                     rnd("2016-03-31", "Series B", 70000000, "Artis Ventures", None, TC_JU_B, "press")]))

# ---------------------------------------------------------------- Just.me
TC_JM_SEED = ("https://techcrunch.com/2011/07/29/stealth-social-mobile-startup-just-me-raises-600k-from-google-"
              "ventures-sv-angel-and-others/")
TC_JM_A = "https://techcrunch.com/2011/12/29/fund-me-mobile-social-network-startup-just-me-raises-2-7-million/"
TC_JM_AUC = "https://techcrunch.com/2013/12/03/just-me-wins-auction/"
FD_JM = sec(1538350, "0001538350-11-000002")
L.append(cls("just-me", status="acquired", rng="below_1b", country="US", city="Palo Alto",
             city_src="formd_address", focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=TC_JM_SEED, entry_date="2011-07", grad="graduated",
             grad_src="web_verified", grad_conf="high", grad_cite=TC_JM_A,
             note="Mobile messaging and social app by Keith Teare (Palo Alto, its Form D address). It 'raised $600,000 "
                  "in seed funding' from Google Ventures, True Ventures, SV Angel, Betaworks and others (TechCrunch, "
                  "2011-07-29), then a $2.7M Series A led by Khosla Ventures (TechCrunch, 2011-12-29), which "
                  "graduates the seed. Out of cash and owing Hercules $1.5M, it auctioned its assets in late 2013 and "
                  "Teare's new entity, Just.me 2014 Inc., won them to keep the service running (TechCrunch, "
                  "2013-12-03): an asset sale out of insolvency reads acquired, with that successor.",
             rounds=[rnd("2011-07-29", "Seed", 600000, None, True, TC_JM_SEED, "press"),
                     rnd("2011-12-29", "Series A", 2700000, "Khosla Ventures", None, TC_JM_A, "press")]))

# ---------------------------------------------------------------- Kibits
TC_KIB = ("https://techcrunch.com/2012/03/29/google-backed-kibits-lets-you-share-with-real-world-micro-networks-"
          "raises-1m/")
BI_KIB = NEWS("kibits", "Truly Innovative Boston Startups")
L.append(cls("kibits", status="unknown", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             focus="SaaS", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_KIB,
             entry_date="2012-03",
             note="Group sharing app turned web and mobile collaboration platform for small and medium businesses, "
                  "founded 2011 by Matt Cutler and David Greenstein, on Business Insider's list of Boston startups "
                  "(2013-04-02). It 'raised a $1 million round of seed funding from Google, CRV, General Catalyst' and "
                  "others (TechCrunch, 2012-03-29; the headline calls it Google Ventures-backed). kibits.com no "
                  "longer serves the product, and no source read gives the company's fate." + GRAD_LEFT,
             rounds=[rnd("2012-03-29", "Seed", 1000000, None, True, TC_KIB, "press")]))

# ---------------------------------------------------------------- Landis
TC_LAN_B = "https://techcrunch.com/2022/10/18/landis-grabs-40m-to-turn-renters-into-homeowners/"
L.append(cls("landis", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=TC_LAN_B, entry_date="2022-10", extra={**WV, "valuation_citation": TC_LAN_B},
             note="Rent-to-own homeownership (New York). GV led the $40M Series B, 'joined by Sequoia Capital' and "
                  "others (TechCrunch, 2022-10-18), after the $165M equity and debt round of July 2021 backed by "
                  "Sequoia, Jay-Z and Will Smith (TechCrunch headline, 2021-07-27); landis.com is live (© 2026 "
                  "Landis Technologies Inc.). Momentum slice check 2026-09-28: no "
                  "priced round at or near $1B on the record; the valuation was not disclosed. Aligned with the "
                  "Sequoia row (private, below $1B, New York).",
             rounds=[rnd("2021-07-27", "unnamed ($165M equity and debt)", 165000000, None, None, TC_LAN_B,
                         "press"),
                     rnd("2022-10-18", "Series B", 40000000, "GV", True, TC_LAN_B, "press")]))

# ---------------------------------------------------------------- Last
L.append(cls("last", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             stage="undetermined", flags=["model_disputes_source", "city_unknown"],
             note="Last (last.co), a stealth mobile product 'that will make it more fun to go out and explore', on the "
                  "firm's 2014-15 listings (partners Kevin Rose, then MG Siegler). Country disputes the prefilled NL "
                  "claim, a one-word name match: nothing ties this company to the Netherlands, and the firm's deal "
                  "partners were Bay Area consumer investors (model: US). A web search found no trace of the company, "
                  "its round, its office or its fate.",
             rounds=[]))

# ---------------------------------------------------------------- Le Tote
TC_LT_SEED = ("https://techcrunch.com/2013/07/31/backed-by-a16z-google-ventures-and-others-le-tote-is-a-"
              "personalized-fashion-stylist-for-everyday-wear/")
TC_LT_A = "https://techcrunch.com/2015/02/05/clothing-rental-startup-le-tote-lands-8-8m-in-series-a-funding/"
W_LT = W("Le Tote")
BLAW_LT = NEWS("le-tote", "Le Tote $12 Million Asset Sale to Saadia Approved")
YF_LT = NEWS("le-tote", "Effectively Defunct Le Tote")
L.append(cls("le-tote", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=TC_LT_SEED, entry_date="2013-07", grad="graduated", grad_src="web_verified",
             grad_conf="high", grad_cite=TC_LT_A,
             note="Clothing-rental subscription (San Francisco, YC S13). Seed from Y Combinator, the YC-VC fund, 500 "
                  "Startups, Andreessen Horowitz, Lerer Ventures and Google Ventures (TechCrunch, 2013-07-31); the "
                  "$8.8M Series A led by Azure (TechCrunch, 2015-02-05) graduates it. Le Tote and Lord & Taylor filed "
                  "for Chapter 11 on 2020-08-02 and the court approved the $12M sale of their intellectual property "
                  "and e-commerce platforms to Saadia Group on 2020-10-20 (Wikipedia; Bloomberg Law); 'Saadia Group "
                  "purchased Le Tote and Lord & Taylor' and ran the rental service until it went offline in spring "
                  "2024 (Yahoo Finance, 2024-04-18). Insolvency followed by an asset sale reads acquired, with that "
                  "successor. The a16z, General Catalyst and YC rows read defunct without the sale; this row holds "
                  "the cited sale. Sources: " + BLAW_LT + " ; " + YF_LT + ".",
             rounds=[rnd("2013-07-31", "Seed", None, None, True, TC_LT_SEED, "press"),
                     rnd("2015-02-05", "Series A", 8800000, "Azure Capital Partners", None, TC_LT_A, "press")]))

# ---------------------------------------------------------------- Light (Light Labs)
W_LIGHT = W("Light (company)")
TC_LIGHT_C = "https://techcrunch.com/2016/07/06/light-raises-money-yay-and-announces-delays-boo/"
TC_LIGHT_D = "https://techcrunch.com/2018/07/18/light-raises-121m-led-by-softbank/"
L.append(cls("light", status="acquired", rng="below_1b", country="US", city="Palo Alto",
             focus="Industrial & Robotics", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=W_LIGHT, entry_date="2016-07", flags=["model_disputes_source"],
             note="Light Labs (Palo Alto), multi-lens computational cameras (the L16), pivoted in 2020 to depth "
                  "perception for vehicles. GV entered at the $30M Series C of July 2016, 'led by GV' (Wikipedia; "
                  "TechCrunch, 2016-07-06), after a $9.7M Series A (2014) and a $25M round led by Formation 8 (2015); "
                  "SoftBank's Vision Fund led the $121M Series D in July 2018 (TechCrunch). 'In May 2022, the tractor "
                  "maker John Deere acquired parts of Light and hired some of the former staff' (Wikipedia): an asset "
                  "sale of the business's technology, read as acquired. Country disputes the prefilled JP claim, a "
                  "one-word name match; the Atomico, Balderton and Cherry rows named Light are a Copenhagen finance "
                  "platform, another company.",
             rounds=[rnd("2014-06", "Series A", 9700000, None, False, W_LIGHT, "press"),
                     rnd("2015-07", "unnamed ($25M)", 25000000, "Formation 8", False, W_LIGHT, "press"),
                     rnd("2016-07-06", "Series C", 30000000, "GV", True, TC_LIGHT_C, "press"),
                     rnd("2018-07-18", "Series D", 121000000, "SoftBank Vision Fund", None, TC_LIGHT_D, "press")]))

# ---------------------------------------------------------------- Locana (Locanabio)
PR_LOC = NEWS("locana", "Locana Raises $55 Million Series A")
FIERCE_LOC = NEWS("locana", "winds down operations")
L.append(cls("locana", status="defunct", rng="below_1b", city="San Diego", city_src="web_verified",
             focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=PR_LOC, entry_date="2019-05",
             note="RNA-targeting gene therapies, 'founded in 2016 and based in San Diego', later Locanabio. ARCH led "
                  "the $55M Series A of 2019-05-22 with existing investors Temasek and Lightstone; 'New investors "
                  "include UCB Ventures and GV' (the company's release). Locanabio said it would 'discontinue "
                  "Locanabio's company operations by the end of 2023' while seeking homes for its programs (Fierce "
                  "Biotech, 2023-11-02); no sale of the company followed on the record, so defunct. Source: "
                  + FIERCE_LOC + ".",
             rounds=[rnd("2019-05-22", "Series A", 55000000, "ARCH Venture Partners", True, PR_LOC, "company")]))

# ---------------------------------------------------------------- LocBox
TC_LB_A = "https://techcrunch.com/2012/10/31/locbox-series-a/"
CBN_LB = "https://news.crunchbase.com/startups/ai-solopreneur-staff-ramakrishnan-rocketship-vc/"
L.append(cls("locbox", status="acquired", rng="below_1b", country="US", focus="SaaS", stage="Series A",
             stage_src="web_verified", stage_conf="high", stage_cite=TC_LB_A, entry_date="2012-10",
             flags=["city_unknown"],
             note="Marketing tools for local businesses (AngelPad-incubated; CEO Saumil Mehta, ex-Kosmix). It 'raised "
                  "$5.1 million in Series A funding' led by InterWest Partners 'with participation from Google "
                  "Ventures, Accel Partners, and 500 Startups' (TechCrunch, 2012-10-31); the firm has no post and no "
                  "earlier round names GV. Its co-founder and CTO's bio reads 'LocBox (acquired by Square)' "
                  "(Crunchbase News, 2024-03-13: " + CBN_LB + "); the date and terms are not on the record. No "
                  "source read places its office.",
             rounds=[rnd("2012-10-31", "Series A", 5100000, "InterWest Partners", True, TC_LB_A, "press")]))

# ---------------------------------------------------------------- Lucid Software
FD_LUCID14 = sec(1604171, "0001604171-14-000001")
FD_LUCID20 = sec(1604171, "0001604171-20-000004")
TC_LUCID_D = "https://techcrunch.com/2020/04/16/lucidchart-raises-52m-series-d-passes-100m-arr/"
CBN_LUCID_C = "https://news.crunchbase.com/startups/lucidchart-draws-72m-in-new-funding-to-scale-visual-collaboration-platform/"
DES_LUCID = NEWS("lucid-software", "Lucid reveals a $1 billion horn")
PR_LUCID = NEWS("lucid-software", "Lucid Receives $500M+ Secondary Investment")
L.append(cls("lucid-software", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified",
             val_cite=PR_LUCID, asof="2021-06-24", country="US", city="South Jordan", city_src="formd_address",
             focus="SaaS", stage="undetermined", flags=["stale", "model_disputes_source"], extra=WV,
             note="Lucidchart and Lucidpress, visual collaboration software, South Jordan UT (its 2020 Form D; Draper "
                  "UT on the 2014 one). Status and figure dispute the prefilled public row and its $2.7B float, a "
                  "same-name registrant joined on the name (cik_weak): Lucid is private. Mark aligned with the ICONIQ "
                  "row (rule 10): in June 2021 Alkeon, Tiger Global and Steadfast bought more than $500M of stock at "
                  "a $3B valuation (the company's release, 2021-06-24), the last priced event on record, though a "
                  "secondary; the last primary, the $52M Series D led by ICONIQ in April 2020, valued it 'north of $1 "
                  "billion' (Deseret News, 2020-04-16). Either way 1b_plus; the mark is older than 24 months "
                  "(stale). Entry: the firm "
                  "listed Lucid in 2014-16 (partner Dave Munichiello); the company's rounds are a $1M angel round in "
                  "2011, $4.36M sold from 2014-03-21 (Form D, Kickstart's Gavin Christensen a director), the $72M "
                  "Series C of October 2018 and the Series D, and no source read names GV in any of them (the 2021 "
                  "release lists Spectrum, ICONIQ, Meritech, Grayhawk and Kickstart as existing investors), so the "
                  "stage is undetermined.",
             rounds=[rnd("2014-03-21", "unnamed ($4.36M sold of $5M)", 4362414, None, None, FD_LUCID14, "filing"),
                     rnd("2018-10-17", "Series C", 72000000, "Meritech Capital; ICONIQ Capital", None, CBN_LUCID_C,
                         "press"),
                     rnd("2020-04-16", "Series D", 52000000, "ICONIQ Capital", None, TC_LUCID_D, "press"),
                     rnd("2021-06-24", "secondary ($500M+ at $3B)", 500000000, None, None, PR_LUCID, "company")]))

# ---------------------------------------------------------------- Luma
TC_LUMA_A = ("https://techcrunch.com/2016/04/07/with-12-5-million-in-funding-including-from-amazon-the-slick-luma-"
             "router-looks-like-fierce-competition/")
TC_LUMA_GV = ("https://techcrunch.com/2016/09/14/luma-nabs-another-9-5-million-in-series-a-funding-from-andreessen-"
              "horowitz-and-gv/")
TC_LUMA_ACQ = ("https://techcrunch.com/2018/01/12/even-the-most-interesting-man-in-the-world-couldnt-make-luma-work-"
               "as-standalone-company/")
L.append(cls("luma", status="acquired", rng="below_1b", country="US", city="Atlanta", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=TC_LUMA_GV, entry_date="2016-09",
             note="Mesh Wi-Fi routers (Atlanta). After a seed from Relay and Felicis and a $12.5M Series A co-led by "
                  "Accel and Amazon in April 2016 without GV (TechCrunch), a16z and GV put in $7M in September 2016, "
                  "which TechCrunch's correction calls 'a convertible note into the Series B' (TechCrunch, "
                  "2016-09-14): GV's entry is the Series B, Growth. First Alert (Newell Brands) acquired Luma in "
                  "January 2018 (TechCrunch, 2018-01-12). Aligned with the a16z and Felicis rows (acquired); the "
                  "Luma AI row in the a16z book is another company.",
             rounds=[rnd("2016-04-07", "Series A", 12500000, "Accel Partners; Amazon", False, TC_LUMA_A, "press"),
                     rnd("2016-09-14", "convertible note into the Series B", 7000000, None, True, TC_LUMA_GV,
                         "press")]))

# ---------------------------------------------------------------- MediaSpike
TC_MS_SEED = "https://techcrunch.com/2012/08/03/mediaspike/"
TC_MS_A = "https://techcrunch.com/2013/11/04/mediaspike-series-a/"
FD_MS = sec(1590179, "0001590179-13-000001")
L.append(cls("mediaspike", status="unknown", rng="below_1b", country="US", city="Mountain View",
             city_src="formd_address", focus="Media, Gaming & Advertising", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=TC_MS_SEED, entry_date="2012-08", grad="graduated",
             grad_src="web_verified", grad_conf="high", grad_cite=TC_MS_A,
             note="In-game product placement. 'MediaSpike has raised a seed round of funding from Raptor Ventures, "
                  "Venture51, Team Downey, Google Ventures, 500 Startups' and others (TechCrunch, 2012-08-03); CMEA "
                  "led the $5.2M Series A with existing investors 500 Startups, Google Ventures and Raptor "
                  "(TechCrunch, 2013-11-04; the Form D reports $5.09M sold from 2013-10-22), which graduates the seed. "
                  "City: Mountain View, the address on its 2013-14 Form Ds (the a16z row says Palo Alto, uncited). "
                  "No source read gives its fate; aligned with the a16z row (unknown).",
             rounds=[rnd("2012-08-03", "Seed", None, None, True, TC_MS_SEED, "press"),
                     rnd("2013-11-04", "Series A", 5200000, "CMEA Capital", True, TC_MS_A, "press")]))

# ---------------------------------------------------------------- Merlin Labs
TC_ML_A = "https://techcrunch.com/2021/05/26/merlin-labs-emerges-from-stealth-to-bring-autonomy-to-55-king-air-fleet/"
TC_ML_B = "https://techcrunch.com/2022/07/13/autonomous-flight-startup-merlin-labs-lands-120m-and-u-s-air-force-partnership/"
MCAP_ML = "https://stockanalysis.com/stocks/mrln/market-cap/"
FTS_ML = FTS("Merlin Labs", "424B3")
GNW_ML = NEWS("merlin-labs", "Announce Closing of Business Combination")
L.append(cls("merlin-labs", status="public", rng="below_1b", usd=176870000, val_src="web_verified",
             val_cite=MCAP_ML, asof=CHECK, country="US", city="Boston", city_src="web_verified",
             focus="Industrial & Robotics", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=TC_ML_A, entry_date="2021-05", extra=WV,
             note="Autonomous flight (Boston, offices in Los Angeles, Denver and New Zealand; TechCrunch, 2022-07-13). "
                  "It raised '$3.5 million in seed funding and $21.5 million in Series A, led by First Round Capital "
                  "and GV (formerly Google Ventures) respectively' (TechCrunch, 2021-05-26), and GV followed in the "
                  "$105M Series B of July 2022. It listed through a merger with Inflection Point Acquisition Corp. IV "
                  "(prospectus 424B3 of 2026-02-12, principal offices 129 South Street, Boston; closing announced "
                  "2026-03-16, GlobeNewswire) and trades on Nasdaq as MRLN: market cap $176.87M on 2026-09-28 "
                  "(stockanalysis.com). The First Round row's $257.75M is a 2025-06-30 float and the General "
                  "Catalyst row reads unknown; this row holds the fresher cap.",
             rounds=[rnd("2021-05-26", "Seed", 3500000, "First Round Capital", None, TC_ML_A, "press"),
                     rnd("2021-05-26", "Series A", 21500000, "GV", True, TC_ML_A, "press"),
                     rnd("2022-07-13", "Series B", 105000000, "Snowpoint Ventures; Baillie Gifford", True, TC_ML_B,
                         "press"),
                     rnd("2026-03-16", "SPAC merger and PIPE (Inflection Point Acquisition Corp. IV)", None, None,
                         None, GNW_ML, "company")]))

# ---------------------------------------------------------------- Miso (social TV)
TC_MISO_SEED = "https://techcrunch.com/2010/05/22/miso-funding/"
TC_MISO_11 = "https://techcrunch.com/2011/01/04/tv-content-check-in-app-miso-lands-1-5m-from-google-ventures-and-hearst/"
TC_MISO_DEC = "https://techcrunch.com/2011/12/01/khosla-google-ventures-and-hearst-put-4m-in-social-tv-platform-miso/"
TC_MISO_ACQ = "https://techcrunch.com/2013/02/01/dijit-buys-miso-really-yes-really/"
L.append(cls("miso", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=TC_MISO_11, entry_date="2010-05",
             note="Miso, the social TV check-in app by Bazaar Labs (San Francisco). 'The startup had previously raised "
                  "seed funding last May from angel investors and from Google Ventures' (TechCrunch, 2011-01-04, on "
                  "the $1.5M round Google Ventures led); Khosla then put in $4M with existing investors Google "
                  "Ventures and Hearst (TechCrunch, 2011-12-01). Dijit bought Miso, 'the tie-up is complete' "
                  "(TechCrunch, 2013-02-01), so acquired; the Khosla row reads defunct although its own note cites "
                  "the Dijit deal. The YC rows named Miso (a Seoul home-services marketplace; Miso Labs) and Miso "
                  "Robotics are other companies." + GRAD_LEFT,
             rounds=[rnd("2010-05-22", "Seed", None, None, True, TC_MISO_11, "press"),
                     rnd("2011-01-04", "unnamed ($1.5M)", 1500000, "Google Ventures", True, TC_MISO_11, "press"),
                     rnd("2011-12-01", "unnamed ($4M)", 4000000, "Khosla Ventures", True, TC_MISO_DEC, "press")]))

# ---------------------------------------------------------------- Miso Media
TC_MM_SEED = ("https://techcrunch.com/2010/12/17/tc-disrupt-peoples-choice-winner-miso-media-raises-funding-from-"
              "google-ventures/")
TC_MM_2 = "https://techcrunch.com/2011/09/14/miso-media-raises-another-2-4-million-to-help-you-learn-guitar/"
MR_MM = NEWS("miso-media", "Now It’s Closed Down")
L.append(cls("miso-media", status="defunct", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_MM_SEED, entry_date="2010-12",
             grad="graduated", grad_src="web_verified", grad_conf="medium", grad_cite=MR_MM,
             flags=["city_unknown"],
             note="Music-learning apps (Miso Music, TechCrunch Disrupt 2010 People's Choice, Shark Tank 2012). It "
                  "'closed a $600K seed funding round led by Google Ventures' (TechCrunch, 2010-12-17), then $2.4M led "
                  "by Mind Fund with Aria Ventures and Detroit Venture Partners, 'the company's second round of "
                  "funding' (TechCrunch, 2011-09-14), which Market Realist names: 'raised $2.4 million in a Series A "
                  "funding round that included Google' (2022-06-30). The named Series A graduates the seed (medium: a "
                  "retrospective names it, the 2011 report does not). The company 'ran out of money, laid off most of "
                  "its staff, and closed down in March 2013' (Market Realist; Inc. headline, 2014-02-28). No source "
                  "read places its office.",
             rounds=[rnd("2010-12-17", "Seed", 600000, "Google Ventures", True, TC_MM_SEED, "press"),
                     rnd("2011-09-14", "Series A ($2.4M)", 2400000, "Mind Fund", True, TC_MM_2, "press")]))

# ---------------------------------------------------------------- MixBit
W_MIX = W("MixBit")
TC_MIX = ("https://techcrunch.com/2014/06/06/youtube-co-founders-break-up-as-chad-hurley-spins-out-his-own-company-"
          "and-steve-chen-joins-google-ventures/")
L.append(cls("mixbit", status="defunct", rng="below_1b", country="US", city="San Mateo", city_src="web_verified",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Collaborative mobile video app from YouTube's co-founders; in 2014 AVOS turned into a single "
                  "company working only on MixBit, with offices in New Zealand and San Mateo (TechCrunch, "
                  "2014-06-06). MixBit ceased operations on 2018-08-21 (Wikipedia). No source read names a round or "
                  "GV's investment beyond the firm's listing, so the stage is undetermined.",
             rounds=[]))

# ---------------------------------------------------------------- MobileDay
MD_SITE = "http://www.mobileday.com/"
FD_MD12 = sec(1538170, "0001538170-12-000002")
FD_MD13 = sec(1538170, "0001538170-13-000002")
FD_MD14 = sec(1538170, "0001538170-14-000001")
L.append(cls("mobileday", status="defunct", rng="below_1b", city="Boulder", city_src="formd_address", focus="SaaS",
             stage="undetermined",
             note="One-touch conference dialing and calendar app (Boulder CO, its Form D address). 'As of 2021, "
                  "MobileDay has shut down' (mobileday.com, read 2026-09-28). Form Ds: $1.03M sold from 2012-11-15 "
                  "(Brad Feld a director), $1.5M from 2013-11-08 and $6.58M from 2014-07-11; the firm listed it from "
                  "May 2013, and no source read ties GV to one of these rounds, so the stage is undetermined.",
             rounds=[rnd("2012-11-15", "unnamed ($1.03M sold)", 1034001, None, None, FD_MD12, "filing"),
                     rnd("2013-11-08", "unnamed ($1.5M sold)", 1500000, None, None, FD_MD13, "filing"),
                     rnd("2014-07-11", "unnamed ($6.58M sold)", 6577064, None, None, FD_MD14, "filing")]))

# ---------------------------------------------------------------- Moonfrye
TC_MF = ("https://techcrunch.com/2013/04/25/punky-brewsters-new-family-focused-interactive-crafting-startup-"
         "moonfrye-raises-2-5m-from-grp-google-ventures-and-others/")
FD_MF = sec(1576174, "0001576174-13-000001")
L.append(cls("moonfrye", status="unknown", rng="below_1b", country="US", city="Los Angeles",
             city_src="formd_address", focus="Consumer & Marketplaces", stage="undetermined",
             note="Family crafting and party-planning apps, co-founded by Soleil Moon Frye and Kara Nortman (Los "
                  "Angeles, its Form D address). It announced '$2.5 million in funding led by GRP Partners with "
                  "participation from Greycroft, Daher Capital, and Google Ventures' (TechCrunch, 2013-04-25; the "
                  "Form D reports $2.72M sold from 2013-04-04): its first round, unnamed and just above the era's "
                  "seed ceiling, so the stage is undetermined. No source read gives its fate.",
             rounds=[rnd("2013-04-04", "unnamed ($2.72M sold)", 2716545, "GRP Partners", True, TC_MF, "press")]))

# ---------------------------------------------------------------- Move Loot
TC_MVL_SEED = ("https://techcrunch.com/2014/06/09/move-loot-raises-2-8m-seed-round-to-expand-its-online-furniture-"
               "consignment-store/")
TC_MVL_9M = "https://techcrunch.com/2015/02/12/move-loot-9m/"
TC_MVL_END = ("https://techcrunch.com/2016/06/29/move-loot-a-yc-backed-furniture-resale-marketplace-shuts-down-"
              "sells-customer-list-to-handy/")
L.append(cls("move-loot", status="defunct", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=TC_MVL_SEED, entry_date="2014-06", grad="graduated", grad_src="web_verified",
             grad_conf="high", grad_cite=TC_MVL_9M,
             note="Used-furniture consignment marketplace (San Francisco, YC W14). Its '$2.8 million seed round' was "
                  "led by First Round and Index 'Other participants include Google Ventures' (TechCrunch, "
                  "2014-06-09). Metamorphic led a $9M round with Google Ventures in February 2015 (TechCrunch, "
                  "2015-02-12), unnamed but above twice the seed and $5M, so the seed graduated. It 'ceased "
                  "operations' in June 2016, selling only its customer list to Handy (TechCrunch, 2016-06-29).",
             rounds=[rnd("2014-06-09", "Seed", 2800000, "First Round Capital; Index Ventures", True, TC_MVL_SEED,
                         "press"),
                     rnd("2015-02-12", "unnamed ($9M)", 9000000, "Metamorphic Ventures", True, TC_MVL_9M, "press")]))

# ---------------------------------------------------------------- mytable
L.append(cls("mytable", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             stage="undetermined", flags=["city_unknown"],
             note="mytable (mytable.org), 'a marketplace and delivery service for locally cooked meals' on the firm's "
                  "2016 listing only. No source read names the company's round, office or fate; the domain serves no "
                  "content.",
             rounds=[]))

# ---------------------------------------------------------------- Nearby
L.append(cls("nearby", status="defunct", rng="below_1b", country="US", city="Oakland",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Nearby (nearbyhq.com), 'the best independent shops in your town, all together', on the firm's "
                  "2021-22 listings. Status and city follow the Redpoint row (defunct, Oakland; its own card dates a "
                  "2021 Series A); no source read names GV's round, so the stage is undetermined.",
             rounds=[]))

if os.environ.get("J16_DRY"):
    jl.write("j16", L, record=False)
else:
    jl.write("j16", L)
