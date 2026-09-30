"""Judge c12, queue batch 24 (PRO-100 NEA): classification of listed members, plus the D5 / X1 / R1 verdicts the
rows raised (fund-shaped pages, a listed purchase, a control acquisition)."""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, SITE, ARCH, W, NEWS, POST, FTS

GP = "Graduation left for the graduation pass."
L = []

# ---- membership corrections (the seed-evidence pass admitted every listed page)
L.append(verdict("harvard-experiment-fund", "not_member",
                 "D5: the firm's own page describes a seed-stage vehicle founded by NEA and anchored at Harvard SEAS that "
                 "invests in startups; a fund-shaped entry, not an operating company.",
                 ec="site_listing", conf="high", cite=ARCH("harvard-experiment-fund")))
L.append(verdict("indous-ventures-llc", "not_member",
                 "D5 and D1: the page is NEA's stake in IndoUS Ventures, the 2006-07 India joint venture fund with IndoUS "
                 "Venture Partners (later Kalaari Capital); the firm's own page calls it an India-focused venture fund.",
                 ec="site_listing", conf="high", cite=ARCH("indous-ventures-llc")))
L.append(verdict("exploramed-ii-inc", "not_member",
                 "D5: the firm's own page describes a medical device incubator; ExploraMed entities form and spin out "
                 "device companies (Acclarent, NeoTract and Moximed are their own rows), so the page is program-shaped. "
                 "Flagged for review.",
                 ec="site_listing", conf="medium", cite=ARCH("exploramed-ii-inc")))
L.append(verdict("info-edge", "not_member",
                 "X1 (T3): Info Edge (Naukri) listed in India in 2006, before NEA's India team existed; the firm's own "
                 "2014-15 page labels it growth and IPO/Public, and no NEA private round before the listing is on record, "
                 "so the position is a listed purchase.",
                 ec="web", conf="medium", cite=W("Info Edge")))
L.append(verdict("future-retail", "uncertain",
                 "The firm's 2014-15 page lists Future Retail (India's listed retailer, the former Pantaloon Retail) as "
                 "private, stage early; the company was listed long before 2014, so the position is either an X1 listed "
                 "purchase or a stake in an unlisted Future Group entity. No source found resolves which.",
                 ec="site_listing", conf="low", cite=ARCH("future-retail")))
L.append(verdict("everside-health", "not_member",
                 "R1 control addendum: Everside Health is Paladina Health renamed (November 2020); on 2018-06-01 NEA funds "
                 "acquired, through NEAPH Holdings, all of the outstanding equity of Paladina from DaVita for about $60M "
                 "in cash (Everside's 2021 draft S-1, Certain Relationships; Healthcare Dive, 2018-06-07). A control "
                 "purchase, not a venture round. Same company as the row paladina-health.",
                 ec="web", conf="high", cite=FTS("Everside", "DRS"),
                 extra={"exclusion": "control_position"}))

# ---- classification
L.append(cls("captora", status="unknown", rng="below_1b", country="US", city="San Mateo",
             stage="Growth", stage_src="model", stage_conf="low", entry_date="2014-05",
             stage_cite=NEWS("captora", "Captora scores $22M"), focus="SaaS",
             rounds=[rnd("2014-05-21", "second round", 22000000, firm_in_round=None,
                         source=NEWS("captora", "Captora scores $22M"), source_type="press")],
             note="Captora, adaptive marketing software. The firm's 2014 year matches its $22M second round (May 2014, "
                  "Marketing Dive), which followed a Series A, but no page read names NEA in it, hence low confidence. "
                  "State unknown, aligned with the Bain Capital Ventures book (San Mateo)."))

L.append(cls("carewise-inc", status="acquired", rng="below_1b", country="US", city="Seattle", stage="undetermined",
             focus="Healthcare & Bio",
             note="CareWise, Seattle, healthcare demand management; the firm's historical list gives the exit as acquired "
                  "by PhyCor. No round naming NEA was found."))

wc = W("CCP Games")
L.append(cls("ccp-games", status="private", rng="below_1b", country="IS", country_src="web_verified",
             country_cite=wc, city="Reykjavik", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2015", focus="Media, Gaming & Advertising",
             note="CCP Games (EVE Online), Reykjavik. NEA first invested in 2015 (the firm's 2026 post) in an 18-year-old "
                  "studio majority-held by Novator and General Catalyst, so the entry is Growth. Pearl Abyss bought CCP "
                  "in 2018; on 2026-05-01 it was sold back to its management for $120M and renamed Fenris Creations "
                  "(Wikipedia), with NEA backing it again. Private, fresher than the a16z book's acquired. Same company "
                  "as the row fenris-creations."))

L.append(cls("cellgate-inc", status="acquired", rng="below_1b", country="US", city="Redwood City",
             stage="undetermined", focus="Healthcare & Bio",
             note="CellGate, polyamine-analogue cancer drugs; the firm's historical list gives the exit as acquired by "
                  "Progen Pharmaceuticals (Australia). No round naming NEA was found."))

cx = "https://www.caixinglobal.com/2022-02-15/logistics-automation-startup-g7-wins-22-billion-valuation-101842224.html"
L.append(cls("chinaway-technologies-limited", status="private", rng="1b_plus", usd=2200000000,
             val_src="web_verified", val_cite=cx, asof="2022-02-15", val_conf="medium",
             extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             country="CN", country_src="web_verified", country_cite=cx, city="Beijing", city_src="web_verified",
             stage="undetermined", focus="SaaS",
             rounds=[rnd("2018-12", "Series E", 320000000, lead="Hopu Investment Management", firm_in_round=None,
                         source="https://techcrunch.com/2018/12/09/g7-raised-320-million/", source_type="press"),
                     rnd("2022-02-15", "Series E+", 200000000, lead="Trustbridge Partners", firm_in_round=None,
                         source=cx, source_type="press")],
             note="Chinaway (Huitong Tianxia) is the Beijing logistics IoT company that trades as G7 (identification "
                  "from knowledge; the firm's description matches). G7 raised $200M led by Trustbridge at about a $2.2B "
                  "valuation in February 2022 (Caixin Global), stale. The round NEA entered by 2013 is not on record."))

L.append(cls("choosy", status="defunct", rng="below_1b", country="US", city="New York",
             stage="Seed", stage_src="first_party", stage_cite=ARCH("choosy"), stage_conf="medium", entry_date="2018",
             focus="Consumer & Marketplaces",
             note="Choosy, New York social-media-driven fashion; the firm's archived page labels the 2018 investment "
                  "Seed. Defunct, aligned with the Coatue book. " + GP))

L.append(cls("cirtas-systems-inc", status="defunct", rng="below_1b", country="US", city="San Jose",
             stage="undetermined", focus="Data Infrastructure",
             note="Cirtas Systems, San Jose, cloud storage controllers; it pulled its product and wound down around 2011 "
                  "to 2012 (from knowledge). No round naming NEA was found."))

L.append(cls("citic-pharmaceuticals", status="acquired", rng="below_1b", country="CN", country_src="web_verified",
             country_cite=POST("nea-names-frank-torti-and-rick-yang-partners"), city="Beijing", stage="undetermined",
             focus="Healthcare & Bio",
             note="CITIC Pharmaceuticals, China-based pharmaceutical distribution; the firm's own 2013 and 2015 releases "
                  "say it was acquired by Shanghai Pharmaceuticals. No round naming NEA was found."))

cc = NEWS("console", "Console Connect disappears")
L.append(cls("console", status="acquired", rng="below_1b", country="US", stage="undetermined", entry_date="2014",
             focus="Data Infrastructure", flags=["city_unknown"],
             note="Console, an interconnection platform founded in 2011; in October 2017 PCCW Global took its brand, "
                  "platform and team (Console Connect) and IX Reach its network business (Capacity Media), so "
                  "acquired. Not the Thrive book's Console (AI IT support, San Francisco): a name collision. Its city "
                  "and the round NEA entered are not on record."))

L.append(cls("convex-computer-systems", status="acquired", rng="below_1b", country="US", city="Richardson",
             stage="undetermined", focus="Industrial & Robotics",
             note="Convex Computer, Richardson, Texas, minisupercomputers; bought by Hewlett-Packard in 1995 "
                  "(Wikipedia). The 1980s round NEA entered is not on record."))

sa = NEWS("corestory", "CoreStory raises $32M to help")
L.append(cls("corestory", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", stage="undetermined", entry_date="2022", focus="DevTools & APIs",
             extra={"valuation_range_source": "web_verified", "valuation_citation": sa},
             rounds=[rnd("2025-10-28", "Series A", 32000000, lead="Tribeca Venture Partners, NEA, SineWave Ventures",
                         firm_in_round=True, source=sa, source_type="press")],
             note="CoreStory, San Francisco, AI code intelligence for legacy modernization. NEA co-led the $32M Series A "
                  "(SiliconANGLE, 2025-10-28), but the firm gives 2022 as its first year, so the entry is an earlier, "
                  "undisclosed round: undetermined. Momentum check 2026-09-30: no round at $1B or more reported; the "
                  "Series A is the last priced round, below $1B."))

L.append(cls("corvita-corporation", status="acquired", rng="below_1b", country="US", city="Miami",
             stage="undetermined", focus="Healthcare & Bio",
             note="Corvita, Miami, small-diameter synthetic vascular grafts; the firm's historical list gives the exit as "
                  "acquired by Pfizer. No round naming NEA was found."))

L.append(cls("cruisewise", status="acquired", rng="below_1b", country="US", city="Boston",
             stage="Seed", stage_src="first_party", stage_cite=ARCH("cruisewise"), stage_conf="medium",
             entry_date="2011", focus="Consumer & Marketplaces",
             note="CruiseWise, online cruise booking; the firm's archived page labels the 2011 investment seed and gives "
                  "the exit as acquired by TripAdvisor. " + GP))

tb = NEWS("data-tamer", "Samsung Ventures Contributes to Tamr")
L.append(cls("data-tamer", status="private", rng="below_1b", country="US", city="Cambridge",
             stage="Seed", stage_src="first_party", stage_cite=ARCH("data-tamer"), stage_conf="medium",
             entry_date="2013", grad="graduated", grad_src="web_verified", grad_cite=tb, grad_conf="high",
             focus="Data Infrastructure",
             rounds=[rnd("2018-07-11", "Series B1", 18000000, firm_in_round=None, source=tb, source_type="press")],
             note="Data-Tamer was the early name of Tamr (Cambridge, Massachusetts; Stonebraker and Palmer), the same "
                  "company as the row tamr. The firm's archived page labels the 2013 investment seed; the $18M Series "
                  "B1 of 2018 (Boston Business Journal) is a named later round and graduates the row."))

wd = W("Drive.ai")
L.append(cls("drive-ai", status="acquired", rng="below_1b", country="US", city="Mountain View",
             stage="Growth", stage_src="web_verified", stage_cite=wd, stage_conf="high", entry_date="2017-06",
             focus="Industrial & Robotics",
             rounds=[rnd("2016-08", "early funding", 12000000, firm_in_round=False, source=wd, source_type="press"),
                     rnd("2017-06", "Series B", 50000000, lead="New Enterprise Associates", firm_in_round=True,
                         source=wd, source_type="press")],
             note="Drive.ai, Mountain View self-driving software; NEA led its $50M Series B in June 2017, its first round "
                  "(the early $12M came from Northern Light, Oriza and InnoSpring). Apple bought the company in June "
                  "2019 days before it would have shut down (The Verge)."))

L.append(cls("elance-inc", status="acquired", rng="below_1b", country="US", city="Mountain View",
             stage="undetermined", entry_date="2003", focus="Consumer & Marketplaces",
             note="Elance, freelance services marketplace; merged with oDesk in December 2013 as Elance-oDesk, renamed "
                  "Upwork in 2015 (Wikipedia). Under D8 Elance is the member and the Upwork row is not. The round NEA "
                  "entered in 2003 is not on record."))

L.append(cls("enverv", status="acquired", rng="below_1b", country="US", stage="undetermined", entry_date="2010",
             focus="Industrial & Robotics", flags=["city_unknown"],
             note="EnVerv, smart-grid communications system-on-chip; the firm's own page gives the exit as acquired by "
                  "Semtech, fresher than the Benchmark book's unknown. Its city and the round NEA entered are not on "
                  "record."))

fs = "https://find-and-update.company-information.service.gov.uk/company/07453696/insolvency"
L.append(cls("fantasy-shopper", status="defunct", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=fs, city="Exeter", stage="undetermined", focus="Consumer & Marketplaces",
             note="Fantasy Shopper Limited, an Exeter social shopping game; members' voluntary liquidation from "
                  "2014-03-26, dissolved 2015-04-07 (Companies House, liquidators in Exeter). No round naming NEA was "
                  "found."))

aw = NEWS("feather-home", "Feather Raises Another $12M")
L.append(cls("feather-home", status="acquired", rng="below_1b", country="US", city="New York",
             stage="Seed", stage_src="first_party", stage_cite=ARCH("feather-home"), stage_conf="medium",
             entry_date="2017", grad="graduated", grad_src="web_verified", grad_cite=aw, grad_conf="high",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2019-05-15", "Series A", 12000000, lead="Spark Capital", firm_in_round=False, source=aw,
                         source_type="press")],
             note="Feather, New York furniture rental; the firm's archived page labels the 2017 investment seed. Spark "
                  "led its $12M Series A in May 2019 (AlleyWatch), which graduates the row; Vesta bought Feather and "
                  "Fernish in November 2023 (Business of Home)."))

gb = NEWS("fetchr", "Dubai-based delivery app Fetchr closes")
mb = NEWS("fetchr", "Fetchr secures $41 million in Series B")
L.append(cls("fetchr", status="unknown", rng="below_1b", country="AE", country_src="web_verified", country_cite=gb,
             city="Dubai", city_src="web_verified",
             stage="Series A", stage_src="web_verified", stage_cite=mb, stage_conf="medium", entry_date="2015",
             focus="Consumer & Marketplaces",
             rounds=[rnd(None, "Seed", 1300000, firm_in_round=None, source=mb, source_type="press"),
                     rnd("2015", "Series A", 11000000, lead="New Enterprise Associates", firm_in_round=True,
                         source=mb, source_type="press"),
                     rnd("2017-05-16", "Series B", 41000000, lead="New Enterprise Associates", firm_in_round=True,
                         source=mb, source_type="press")],
             note="Fetchr, Dubai delivery; NEA led its $11M Series A in 2015 and the $41M Series B in 2017 (MENAbytes); "
                  "a $1.3M seed came first without NEA named. The firm's 2014 year is read as the close year. Its top "
                  "backer warned of liquidation in October 2021 (Bloomberg); no later outcome was found. Not the Y "
                  "Combinator book's Fetchr (San Francisco): a probable name collision."))

L.append(cls("forhealth-technologies", status="acquired", rng="below_1b", country="US", city="Daytona Beach",
             stage="undetermined", focus="Healthcare & Bio",
             note="ForHealth Technologies, Daytona Beach, IV drug preparation automation; the firm's historical list "
                  "gives the exit as acquired by Baxa. No round naming NEA was found."))

for s, nm in (("gaov", "GaoV"), ("gtel", "Gtel")):
    L.append(cls(s, status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
                 country="CN", country_src="web_verified", country_cite=ARCH(s), focus=None,
                 flags=["identity_unresolved"],
                 note=f"{nm} appears only as a name on the firm's 2008 China portfolio page, with no description. Google "
                      f"News finds no matching company (Gtel results are a Zimbabwe phone brand), so the company cannot "
                      f"be identified."))

wh = W("Hello Alfred")
L.append(cls("hello-alfred", status="private", rng="below_1b", city="New York",
             stage="Series A", stage_src="web_verified", stage_cite=wh, stage_conf="high", entry_date="2015-04",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2014-11", "Seed", 2000000, lead=None, firm_in_round=False, source=wh, source_type="press"),
                     rnd("2015-04", "Series A", 10500000, firm_in_round=True, source=wh, source_type="press"),
                     rnd("2020-10", "investment round", 42000000, lead="166 2nd LLC", firm_in_round=None, source=wh,
                         source_type="press")],
             note="Hello Alfred (now Alfred), New York; Wikipedia names NEA in the April 2015 $10.5M Series A and not in "
                  "the November 2014 seed (Spark, SV Angel, CrunchFund), so the entry is the Series A. Same company as "
                  "the row alfred, aligned with it and with the Spark book."))

L.append(cls("hospital-group-of-america-inc", status="unknown", rng="below_1b", country="US", stage="undetermined",
             focus="Healthcare & Bio", flags=["city_unknown"],
             note="Hospital Group of America, a chain of free-standing psychiatric hospitals on the firm's 2008 "
                  "historical list; its fate, city and the round NEA entered could not be established."))

L.append(cls("hospital-partners-of-america-inc", status="unknown", rng="below_1b", country="US", city="Charlotte",
             stage="undetermined", focus="Healthcare & Bio",
             note="Hospital Partners of America, Charlotte, developer of physician-partnered acute care hospitals; "
                  "current on the firm's 2008 list, later fate not established."))

L.append(cls("huddler", status="unknown", rng="below_1b", country="US", stage="undetermined", entry_date="2009",
             focus="Media, Gaming & Advertising", flags=["city_unknown"],
             note="Huddler, a SaaS platform for enthusiast discussion forums, first invested 2009; Google News carries "
                  "nothing on it, and its fate, city and round could not be established."))

L.append(cls("ibah-inc", status="acquired", rng="below_1b", country="US", city="Blue Bell", stage="undetermined",
             focus="Healthcare & Bio",
             note="IBAH, Blue Bell, Pennsylvania, contract clinical research; acquired by Omnicare in 1998 (from "
                  "knowledge). The round NEA entered is not on record."))

L.append(cls("imergy-power-systems", status="defunct", rng="below_1b", country="US", city="Fremont",
             stage="undetermined", entry_date="2007", focus="Climate & Energy",
             note="Imergy Power Systems (formerly Deeya Energy, the row deeya-energy-inc), Fremont, vanadium flow "
                  "batteries; it entered insolvency and laid off its staff in August 2016 (Energy-Storage.News). The "
                  "round NEA entered in 2007 is not on record."))

L.append(cls("intarvo", status="unknown", rng="below_1b", country="IN", country_src="web_verified",
             country_cite=ARCH("intarvo"), city="Bengaluru",
             stage="Growth", stage_src="first_party", stage_cite=ARCH("intarvo"), stage_conf="medium",
             entry_date="2009", focus="Industrial & Robotics",
             note="inTarvo, Indian technical support and reverse logistics for electronics OEMs; the firm's archived "
                  "page labels the 2009 investment growth. Its later state could not be established."))

wk = W("Konarka Technologies")
L.append(cls("konarka-technologies-inc", status="defunct", rng="below_1b", country="US", city="Lowell",
             stage="undetermined", focus="Climate & Energy",
             rounds=[rnd("2006", "venture funding to date", 60000000, firm_in_round=True, source=wk,
                         source_type="press")],
             note="Konarka, Lowell, Massachusetts, organic photovoltaics; NEA was among its venture investors by 2006, "
                  "but no round is named. It filed Chapter 7 in May 2012, ceased operations and was liquidated "
                  "(Wikipedia)."))

L.append(cls("koozoo", status="unknown", rng="below_1b", country="US", stage="undetermined",
             focus="Media, Gaming & Advertising", flags=["city_unknown"],
             note="Koozoo, crowd-sourced live video of public places from smartphones, on the firm's 2013 list only; "
                  "Google News has nothing on it, and its fate, city and round could not be established."))

L.append(cls("kor-electronics", status="acquired", rng="below_1b", country="US", city="Cypress",
             stage="undetermined", focus="Industrial & Robotics",
             note="KOR Electronics, Cypress, California, DRFM and electronic warfare systems; acquired by Mercury "
                  "Computer Systems in 2011, as the firm's historical list says. No round naming NEA was found."))

L.append(cls("leyden-energy", status="defunct", rng="below_1b", country="US", city="Fremont",
             stage="undetermined", entry_date="2011", focus="Climate & Energy",
             note="Leyden Energy, Fremont, lithium-ion batteries. In June 2014 A123 Systems bought certain intellectual "
                  "property and technical staff (Windpower Engineering), not the company or its business, which "
                  "ended; so defunct under the acqui-hire rule, aligned with the Lightspeed book, although the firm's "
                  "exit line reads acquired by A123."))

L.append(cls("lifemetrix-inc", status="unknown", rng="below_1b", country="US", stage="undetermined",
             focus="Healthcare & Bio", flags=["city_unknown"],
             note="LifeMetrix, cancer treatment programs and information services, on the firm's historical list; its "
                  "fate, city and round could not be established."))

L.append(cls("likelihood", status="unknown", rng="below_1b", country="US", stage="undetermined", entry_date="2012",
             focus="SaaS", flags=["city_unknown"],
             note="Likelihood, real-time retail customer-intent prediction, first invested 2012; Google News returns only "
                  "the common word, and its fate, city and round could not be established."))

wl = W("Lot18")
L.append(cls("lot18", status="defunct", rng="below_1b", city="New York",
             stage="Growth", stage_src="web_verified", stage_cite=wl, stage_conf="high", entry_date="2011-05",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2010-11", "Series A", 3000000, lead="FirstMark Capital", firm_in_round=False, source=wl,
                         source_type="press"),
                     rnd("2011-05", "Series B", 10000000, lead="New Enterprise Associates", firm_in_round=True,
                         source=wl, source_type="press"),
                     rnd("2011-11", "Series C", 30000000, lead="Accel Partners", firm_in_round=True, source=wl,
                         source_type="press")],
             note="Lot18, New York online wine retailer; NEA led its $10M Series B in May 2011 after FirstMark's Series "
                  "A. It laid off staff and closed in 2023 (Wikipedia)."))

L.append(cls("lsf-network", status="unknown", rng="below_1b", country="US", stage="undetermined", entry_date="2004",
             focus="Media, Gaming & Advertising", flags=["city_unknown"],
             note="LSF Network, performance-based online advertising and lead generation, first invested 2004; its "
                  "fate, city and round could not be established."))

L.append(cls("lytmus", status="unknown", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2015", focus="SaaS",
             note="Lytmus, virtual-machine job try-outs for digital skills, San Francisco; aligned with the a16z book "
                  "(unknown). Not the 2026 Indian edtech Lytmus AI. The round NEA entered is not on record."))

jl.write("c12b", L)
