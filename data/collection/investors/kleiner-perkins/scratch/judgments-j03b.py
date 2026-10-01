"""PRO-99 Kleiner Perkins, judge j03, queue batch 6 (luxcreo .. nuvasive-inc): classification of listed members,
plus two membership corrections (neon: partner-carried; novavax-inc: a purchase into a listed company, T3).
The rows mirage, maxima, nooks, mine and multiply are superseded by judgments-j03c.py (their momentum checks and
the rounds those searches found); record j03c again after any re-run of this file."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, NEWS, ARCH, W, FTS

GL = "Graduation left for the graduation pass."
TODAY = "2026-09-30"
K8_NOVAVAX = FTS("NOVAVAX", "8-K")
K8_MOVELLA = FTS("Movella", "8-K")
RP_MAXIMA = "https://www.redpoint.com/companies/maxima/"
KP_MAXIMA_A = [p["url"] for p in jl._POSTS
               if p["slug"] == "maxima-bringing-ai-agents-to-the-heart-of-enterprise-accounting"][0]
GNW_MODERN = ("https://www.globenewswire.com/news-release/2021/02/11/2174026/0/en/Modern-Health-Gains-Unicorn-Status-"
              "After-74-Million-Series-D-at-1-17-Billion-Valuation.html")
QZ_NEWLIMIT = "https://qz.com/newlimit-series-c-fundraise-aging-liver-trial-060326"
EW_NEWSELA = ("https://marketbrief.edweek.org/strategy-operations/k-12-dealmaking-newsela-raises-100-million-series-d-"
              "round-reaches-unicorn-status/2021/03")
MOM_MIRAGE = "Momentum check 2026-09-30: queued on Google News, outcome recorded in a follow-up line."
MOM_MAXIMA = "Momentum check 2026-09-30: queued on Google News, outcome recorded in a follow-up line."
MOM_NOOKS = "Momentum check 2026-09-30: queued on Google News, outcome recorded in a follow-up line."
MOM_MINE = "Momentum check 2026-09-30: queued on Google News, outcome recorded in a follow-up line."
MOM_MULTIPLY = "Momentum check 2026-09-30: queued on Google News, outcome recorded in a follow-up line."

L = []

# ---- batch 5 correction: inworld (the seed and Series A citations were decoded after batch 5 was recorded)
VB_INWORLD = "https://venturebeat.com/business/inworld-ai-joins-metaverse-innovation-with-ai-driven-virtual-characters"
SA_INWORLD = "https://siliconangle.com/2022/08/23/inworld-ai-raises-50m-ai-powered-no-code-virtual-character-development-studio/"
CB_INWORLD = "https://www.crunchbase.com/funding_round/inworld-ai-seed--3a307fb1"
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


# ---- membership corrections (verdict line only)
L.append(verdict("neon", "not_member",
                 "Partner-carried (Erik 2026-09-17 partner-carried rule; D3): the firm's own post welcoming Leigh Marie "
                 "Braswell in May 2023 credits Neon, with Chronosphere and Persona, to her first years in venture at "
                 "her previous firm; the site lists all three with a 2021 year and as Prior, and the archive shows Neon "
                 "only from 2023, after she joined. No Kleiner Perkins fund round in Neon is on record.",
                 ec="site_listing", conf="medium", cite=POST("welcoming-leigh-marie-braswell")))
L.append(verdict("novavax-inc", "not_member",
                 "D4 (T3): Novavax was listed on Nasdaq from 1995; the firm's position is the $20M common stock "
                 "offering of February 2006 to Kleiner Perkins Caufield & Byers and Prospect Venture Partners "
                 "(Novavax 8-K), a purchase into the listed company with no earlier private round.",
                 ec="fund_filing", conf="high", cite=K8_NOVAVAX))

L.append(cls("luxcreo", status="private", rng="below_1b", country="US", city="Belmont", stage="undetermined",
             entry_date="2019", focus="Industrial & Robotics", rounds=[],
             note="Additive manufacturing resins and printers, Belmont, California. The firm lists a 2019 entry "
                  "labelled Early; no source read names that round."))

L.append(cls("luxvue-technology", status="acquired", rng="below_1b", city="Santa Clara",
             stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=jl.FORMD_CITE("luxvue-technology", 0), entry_date="2011-08-16", focus="Industrial & Robotics",
             rounds=[rnd("2011-08-16", "Form D offering", 7500000, None, True, jl.FORMD_CITE("luxvue-technology", 0), "filing"),
                     rnd("2012-11-20", "Form D offering", 11075000, None, True, jl.FORMD_CITE("luxvue-technology", 1), "filing"),
                     rnd("2013-12-09", "Form D offering", 25500000, None, True, jl.FORMD_CITE("luxvue-technology", 2), "filing")],
             note="Micro-LED displays, Santa Clara; Apple bought it in 2014. The firm's 2011 entry matches the company's "
                  "first Form D, a $7.5M offering of 2011-08-16 two years after incorporation (Series A size); the "
                  "prefilled 2012-11-20 date is the second offering."))

L.append(cls("macromedia", status="acquired", city="San Francisco", rng="below_1b", stage="undetermined",
             entry_date="1989", focus="SaaS", flags=["model_disputes_source"], rounds=[],
             note="Multimedia and web software, San Francisco; Adobe bought it in December 2005, so acquired, not "
                  "defunct. The firm's 1989 year predates the 1992 merger that formed Macromedia; no source read "
                  "names the round."))

L.append(cls("magic-leap", city="Plantation", stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=W("Magic Leap"), entry_date="2014-10", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-10", "Series B", 542000000, "Google", True, W("Magic Leap"), "press"),
                     rnd("2015-12", "Series C", 827000000, None, None, W("Magic Leap"), "press"),
                     rnd("2018-03-07", "Series D", 461000000, "Public Investment Fund", None, W("Magic Leap"), "press")],
             note="Augmented reality headsets, Plantation, Florida. Wikipedia names Kleiner Perkins among the backers "
                  "of the $540M+ October 2014 round led by Google, the round after the company's $50M Series A of "
                  "early 2014, which matches the firm's 2014 Growth entry."))

L.append(cls("mandiant", city="Alexandria", rng="below_1b", focus="Security",
             note="Incident response, Alexandria, Virginia (EDGAR address); FireEye bought it in 2013."))

L.append(cls("marimba", status="acquired", rng="below_1b", country="US", city="Mountain View",
             stage="undetermined", entry_date="1996", focus="SaaS", rounds=[],
             note="Software distribution and configuration management, Mountain View; BMC Software bought it in 2004. "
                  "The firm's funds filed 13Gs from 2000; no source read names the 1996 round."))

L.append(cls("materialize", status="private", rng="below_1b", country="US", city="New York",
             stage="Growth", stage_src="model", stage_conf="medium", stage_cite=POST("materialize-series-b"),
             entry_date="2020-11-30", focus="Data Infrastructure",
             rounds=[rnd("2020-11-30", "Series B", None, "Kleiner Perkins", True, POST("materialize-series-b"), "firm")],
             note="Streaming SQL database, New York. The firm's first post on the company (2020-11-30, published as "
                  "'materialize-series-b') announces the Series B, after Lightspeed's Series A, in the firm's 2020 "
                  "entry year."))

L.append(cls("maxima", status="private", country="US", city="San Mateo", flags=["model_disputes_source"],
             stage="Seed", stage_src="first_party", stage_cite=KP_MAXIMA_A, stage_conf="high", entry_date="2024",
             grad="graduated", grad_src="first_party", grad_cite=KP_MAXIMA_A, grad_conf="high", grad_asof="2025-12-04",
             rng="below_1b", focus="AI & Applied AI",
             rounds=[rnd("2024", "Seed", None, "Kleiner Perkins", True, KP_MAXIMA_A, "firm"),
                     rnd("2025-12-04", "Series A", None, "Redpoint Ventures", True, RP_MAXIMA, "firm")],
             note="AI agents for enterprise accounting (maxima.ai), San Mateo per Redpoint's page; still private, so "
                  "the acquired status and the Israeli country from a one-word name match are wrong. The firm's post "
                  "of 2025-12-04 says it led the Seed and now joins the Series A. " + MOM_MAXIMA))

L.append(cls("medarrive", status="private", rng="below_1b", city="New York",
             stage="Seed", stage_src="first_party", stage_cite=POST("medarrive-seed"), stage_conf="high",
             entry_date="2020-12-03", flags=["stage_disputes_band"], focus="Healthcare & Bio",
             rounds=[rnd("2020-12-03", "Seed", None, "Kleiner Perkins (co-lead)", True, POST("medarrive-seed"), "firm"),
                     rnd("2022-01-28", "Form D offering", 32846769, None, True, None, "filing")],
             note="In-home care via EMS professionals, New York (Form D address). The firm's post of 2020-12-03 says it "
                  "co-led the Seed, so the Growth band read off the 2022 Form D is a follow-on. " + GL))

L.append(cls("microcide", status="defunct", rng="below_1b", country="US", city="Waltham", stage="undetermined",
             focus="Healthcare & Bio", rounds=[],
             note="Antibacterial drug developer, founded in Mountain View; it merged with Maret and Althexis and was "
                  "renamed Essential Therapeutics (Waltham, the last EDGAR address), which went into Chapter 11 in "
                  "2003. The firm's funds filed 13Gs in 1997-99; no source read names its round."))

L.append(cls("millennium-pharmaceuticals", status="acquired", rng="below_1b", country="US", city="Cambridge",
             stage="undetermined", entry_date="1993", focus="Healthcare & Bio", rounds=[],
             note="Oncology biopharma, Cambridge, Massachusetts; Takeda bought it in 2008 (now Takeda Oncology). The "
                  "firm lists a 1993 entry, the founding year; no source read names the round."))

L.append(cls("mine", status="private", rng="below_1b", country="US", city="New York", stage="undetermined",
             entry_date="2021", focus="Fintech & Payments", rounds=[],
             note="Credit-building debit card for college students (formerly Fizz, joinfizz.com), New York as the "
                  "Cherry and YC rows. The firm lists a 2021 entry; no source read names that round. The Battery and "
                  "Headline 'Mine' rows are MineOS of Tel Aviv, a different company. " + MOM_MINE))

L.append(cls("mirage", status="private", rng="below_1b", country="US", city="New York",
             flags=["model_disputes_source"], stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=POST("captions-series-b"), entry_date="2023-06-22", focus="AI & Applied AI",
             rounds=[rnd("2023-06-22", "Series B", None, "Kleiner Perkins", True, POST("captions-series-b"), "firm")],
             note="AI video creation app Captions, renamed Mirage, New York; private, so the public status and $26M "
                  "value came from a different listed company of the same name. The firm's first post on it "
                  "(2023-06-22, 'captions-series-b') marks the Series B, its 2023 entry. " + MOM_MIRAGE))

L.append(cls("mist-systems", status="acquired", rng="below_1b", country="US", city="Cupertino",
             stage="undetermined", entry_date="2017", focus="Data Infrastructure", rounds=[],
             note="AI-driven Wi-Fi, Cupertino; Juniper Networks bought it in April 2019. The firm lists a 2017 entry "
                  "labelled Growth; no source read names that round."))

L.append(cls("mobcrush", status="acquired", rng="below_1b", country="US", city="Los Angeles",
             stage="undetermined", entry_date="2015", focus="Media, Gaming & Advertising", rounds=[],
             note="Live-streaming platform, Los Angeles; it merged into Super League Gaming in 2021. The firm lists a "
                  "2015 entry; no source read names that round."))

L.append(cls("modern-health", status="private", rng="1b_plus", usd=1170000000, val_src="web_verified",
             val_cite=GNW_MODERN, asof="2021-02-11", extra={"valuation_range_source": "web_verified"},
             flags=["stale"], country="US", city="San Francisco",
             stage="Series A", stage_src="first_party", stage_cite=POST("welcome-modern-health"), stage_conf="high",
             entry_date="2019-05-23", focus="Healthcare & Bio",
             rounds=[rnd("2019-05-23", "Series A", None, "Kleiner Perkins", True, POST("welcome-modern-health"), "firm"),
                     rnd("2021-02-11", "Series D", 74000000, None, None, GNW_MODERN, "company")],
             note="Workplace mental health, San Francisco. The firm's post of 2019-05-23 says it led the Series A; the "
                  "$74M Series D of February 2021 valued the company at $1.17B (company release), stale."))

L.append(cls("motiv", status="unknown", rng="below_1b", city="San Francisco",
             stage="Growth", stage_src="formd_structural", stage_conf="medium",
             stage_cite=jl.FORMD_CITE("motiv", 3), focus="Consumer & Marketplaces",
             rounds=[rnd("2014-02-27", "Form D offering", 1500000, None, False, jl.FORMD_CITE("motiv", 0), "filing"),
                     rnd("2014-10-13", "Form D offering", 2000000, None, False, jl.FORMD_CITE("motiv", 1), "filing"),
                     rnd("2015-09-01", "Form D offering", 9269640, None, False, jl.FORMD_CITE("motiv", 2), "filing"),
                     rnd("2016-02-16", "Form D offering", 6693300, None, True, jl.FORMD_CITE("motiv", 3), "filing")],
             note="Smart ring maker (Motiv Inc., formerly Mechio), San Francisco. Randy Komisar and Wen Hsieh first "
                  "sign the company's 2016-02-16 Form D, its fourth offering after three earlier ones, so the entry "
                  "reads Growth by the filing count; no source read states its fate after 2018."))

L.append(cls("motive", status="private", rng="1b_plus", usd=2850000000, val_src="web_verified",
             val_cite=W("Motive (company)"), asof="2022-05", extra={"valuation_range_source": "web_verified"},
             flags=["stale"], city="San Francisco",
             stage="Growth", stage_src="first_party", stage_cite=POST("motive-series-f"), stage_conf="high",
             entry_date="2022-05-25", focus="SaaS",
             rounds=[rnd("2015", "Series A", 8000000, "Index Ventures", False, W("Motive (company)"), "press"),
                     rnd("2022-05-25", "Series F", 150000000, "Insight Partners, Kleiner Perkins", True,
                         POST("motive-series-f"), "firm"),
                     rnd("2025-05-20", "Form D offering", 150000000, None, True, None, "filing")],
             note="Fleet management platform (formerly KeepTruckin), San Francisco. The firm's post of 2022-05-25 says "
                  "it co-led the Series F (Ilya Fushman had led the 2015 Series A at his previous firm), so the entry "
                  "is 2022, not the 2025 Form D; the $2.85B Series F mark (Wikipedia) stands, stale, as the GV, "
                  "Insight and IVP rows."))

L.append(cls("movella", country="US", city="Henderson", rng="below_1b", stage="undetermined", entry_date="2013",
             focus="Industrial & Robotics", rounds=[rnd("2023-02", "SPAC merger (KPCB Holdings 10.2%)", None, None,
                                                        True, K8_MOVELLA, "filing")],
             note="Motion sensors and software (formerly mCube, which bought Xsens), Henderson, Nevada (EDGAR address "
                  "of Movella Holdings). The firm lists a 2013 entry labelled Growth; no source read names that "
                  "round."))

L.append(cls("moveworks", status="acquired", rng="below_1b", city="Mountain View",
             stage="Growth", stage_src="first_party", stage_cite=POST("moveworks-a-new"), stage_conf="high",
             entry_date="2019-11-14", focus="AI & Applied AI",
             rounds=[rnd("2019-04", "Series A", 30000000, "Lightspeed Venture Partners, Bain Capital", False,
                         W("Moveworks"), "press"),
                     rnd("2019-11-14", "Series B", 75000000, "Kleiner Perkins", True, POST("moveworks-a-new"), "firm")],
             note="Enterprise AI assistant, Mountain View; ServiceNow completed its purchase in December 2025 "
                  "(Wikipedia). The firm's post of 2019-11-14 says it led the Series B, and its 2025 post says it "
                  "backed the company since that round."))

L.append(cls("multiply", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2022", focus="Fintech & Payments", rounds=[],
             note="Mortgage and homeownership platform (multiplymortgage.com). The firm lists a 2022 entry; no source "
                  "read names that round. The Lux and YC 'Multiply' rows are Multiply Labs, a robotics company. "
                  + MOM_MULTIPLY))

L.append(cls("myfitnesspal", city="San Francisco", rng="below_1b",
             stage="Series A", stage_src="model", stage_conf="medium", stage_cite=W("MyFitnessPal"),
             entry_date="2013-08-02", focus="Consumer & Marketplaces",
             rounds=[rnd("2013-08-02", "first institutional round", 18000000, "Kleiner Perkins", True,
                         W("MyFitnessPal"), "press")],
             note="Diet and fitness tracking app, San Francisco; Under Armour bought it for $475M in 2015. Wikipedia: "
                  "its first institutional round, $18M in 2013, was led by Kleiner Perkins with Accel (the Accel row "
                  "reads Series A)."))

L.append(cls("nanogen", status="acquired", rng="below_1b", country="US", city="San Diego", stage="undetermined",
             entry_date="1994", focus="Healthcare & Bio", rounds=[],
             note="Molecular diagnostics, San Diego; it filed Chapter 11 in 2009 and sold its assets to ELITech out of "
                  "the bankruptcy (successor ELITech). The firm lists a 1994 entry; no source read names the round."))

L.append(cls("nav", status="private", rng="below_1b", city="Draper", stage="undetermined", entry_date="2014",
             focus="Fintech & Payments",
             rounds=[rnd("2013-05", "Form D offering", 1000000, None, None, None, "filing"),
                     rnd("2016-08-19", "Form D offering", 25000000, None, True, None, "filing")],
             note="Small-business credit and financing platform (formerly Creditera), Draper, Utah (EDGAR address). "
                  "The firm lists a 2014 entry, before the 2016 Form D that Randy Komisar signs; no source read names "
                  "the 2014 round."))

L.append(cls("nebula", status="defunct", rng="below_1b", city="Mountain View", flags=["model_disputes_source"],
             stage="Series A", stage_src="web_verified", stage_cite=W("Nebula (company)"), stage_conf="high",
             entry_date="2011-05", focus="Data Infrastructure",
             rounds=[rnd("2011-05", "Series A", None, "Kleiner Perkins, Highland Capital Partners", True,
                         W("Nebula (company)"), "press"),
                     rnd("2012", "Series B", 25000000, "Comcast Ventures, Highland Capital", None,
                         W("Nebula (company)"), "press")],
             note="OpenStack private-cloud appliances, Mountain View. It announced it was ceasing operations on "
                  "2015-04-01 (Wikipedia), so defunct, not acquired (staff hired elsewhere decide nothing). Kleiner "
                  "Perkins co-led the May 2011 Series A; the 2012 Form D date is the Series B."))

L.append(cls("nest", status="acquired", rng="below_1b", country="US", city="Palo Alto",
             flags=["model_disputes_source"], stage="Series A", stage_src="first_party", stage_cite=SITE("nest"),
             stage_conf="high", entry_date="2010", focus="Consumer & Marketplaces",
             rounds=[rnd("2010", "Series A", None, "Kleiner Perkins", True, SITE("nest"), "firm")],
             note="Nest Labs, smart thermostats, Palo Alto; Google bought it for $3.2B in 2014. The German country "
                  "came from a one-word name match. The firm's page says it led Nest's Series A and put $20M in "
                  "across the A and B."))

L.append(cls("netlify", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified",
             val_cite=W("Netlify"), asof="2021-11-17", extra={"valuation_range_source": "web_verified"},
             flags=["stale"], city="San Francisco", focus="DevTools & APIs",
             note="Web development platform, San Francisco. The $105M Series D of 2021-11-17, led by Bessemer with "
                  "Kleiner Perkins, valued it at $2B (Wikipedia), stale, as the sibling rows."))

L.append(cls("netscape", city="Mountain View", rng="below_1b", stage="undetermined", entry_date="1994-09",
             focus="Consumer & Marketplaces",
             rounds=[rnd("1994-09", "venture round (unnamed)", None, None, True, POST("netscape"), "firm")],
             note="Web browser pioneer (Mosaic Communications), Mountain View; AOL bought it in 1999. The firm's case "
                  "study says it invested in September 1994 without naming the round."))

L.append(cls("neurocrine-biosciences", city="San Diego", stage="undetermined", focus="Healthcare & Bio", rounds=[],
             note="Neurology and endocrine drugs, San Diego. The firm's funds filed 13Gs in 1997-98; no source read "
                  "names the round it entered."))

L.append(cls("neuron23", status="private", rng="below_1b", country="US", city="South San Francisco",
             stage="undetermined", entry_date="2018", focus="Healthcare & Bio", rounds=[],
             note="Precision neurology biotech, South San Francisco. The firm lists a 2018 entry (now Prior); no "
                  "source read names that round."))

L.append(cls("neuropace", city="Mountain View", focus="Healthcare & Bio",
             note="Responsive neurostimulation for epilepsy, Mountain View (EDGAR address)."))

L.append(cls("newlimit", status="private", rng="1b_plus", usd=3100000000, val_src="web_verified",
             val_cite=QZ_NEWLIMIT, asof="2026-06", extra={"valuation_range_source": "web_verified"},
             country="US", city="South San Francisco", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=POST("new-limit-series-b"), entry_date="2023", focus="Healthcare & Bio",
             rounds=[rnd("2023", "Series A", None, None, True, POST("new-limit-series-b"), "firm"),
                     rnd("2025-05-06", "Series B", None, "Kleiner Perkins", True, POST("new-limit-series-b"), "firm"),
                     rnd("2026-06", "Series C", None, None, None, QZ_NEWLIMIT, "press")],
             note="Epigenetic reprogramming for aging, South San Francisco (the Thrive row gives San Francisco). The "
                  "firm's 2025 post leads the Series B and 'doubles down' after knowing the company at the Series "
                  "A, its 2023 entry year. The June 2026 Series C at $3.1B (Quartz, as the Thrive and 8VC rows) is "
                  "the mark."))

L.append(cls("newsela", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
             val_cite=EW_NEWSELA, asof="2021-02-26", extra={"valuation_range_source": "web_verified"},
             flags=["stale"], city="New York", focus="SaaS",
             note="K-12 reading content platform, New York; the $100M Series D of February 2021 valued it at $1B "
                  "(EdWeek Market Brief, as the TCV row), stale."))

L.append(cls("nexprise", status="acquired", rng="below_1b", country="US", city="Carlsbad", stage="undetermined",
             focus="SaaS", rounds=[rnd("1998", "venture funding (unnamed, $45M total)", 45000000, None, True,
                                       W("Chemdex"), "press")],
             note="Chemdex, renamed Ventro and then NexPrise (Carlsbad); it filed for bankruptcy on 2011-01-18 and "
                  "Trubiquity bought all its assets in April 2011 (successor Trubiquity). Wikipedia names Kleiner "
                  "Perkins among the backers of $45M before the 1999 IPO without naming the round."))

L.append(cls("nextdoor", city="San Francisco", focus="Consumer & Marketplaces",
             note="Neighborhood social network, San Francisco."))

L.append(cls("nexus-dx", status="acquired", rng="below_1b", country="US", city="San Diego",
             focus="Healthcare & Bio",
             note="Point-of-care diagnostics, San Diego; it became part of ITC Nexus Holding (the itc-nexus-dx row, "
                  "later Accriva, sold to Werfen) in 2010. " + GL))

L.append(cls("ngmoco", city="San Francisco", rng="below_1b", stage="undetermined", entry_date="2008",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2010-02", "Series C", 25000000, "Institutional Venture Partners", True, W("Ngmoco"), "press")],
             note="iPhone game publisher, San Francisco; DeNA bought it in 2010. Wikipedia says the iFund backed it at "
                  "launch in 2008 and Kleiner Perkins was an existing investor in the February 2010 Series C; the "
                  "2008 round is not named."))

L.append(cls("nodality", status="unknown", rng="below_1b", city="South San Francisco", focus="Healthcare & Bio",
             note="Single-cell diagnostics, South San Francisco (EDGAR address); the last Form D is from 2011 and no "
                  "source read states a sale or shutdown."))

L.append(cls("nooks", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="Growth", stage_src="first_party", stage_cite=POST("nooks-bringing"), stage_conf="high",
             entry_date="2024-10-23", focus="AI & Applied AI",
             rounds=[rnd("2024-10-23", "Series B", None, "Kleiner Perkins", True, POST("nooks-bringing"), "firm")],
             note="AI sales dialer, San Francisco. The firm's post of 2024-10-23 says it leads the Series B, its 2024 "
                  "entry. " + MOM_NOOKS))

L.append(cls("nova-credit", status="private", rng="below_1b", country="US", city="New York",
             stage="Growth", stage_src="first_party", stage_cite=POST("nova-credit-series-b"), stage_conf="high",
             entry_date="2020-02-12", focus="Fintech & Payments",
             rounds=[rnd("2020-02-12", "Series B", None, "Kleiner Perkins", True, POST("nova-credit-series-b"), "firm")],
             note="Cross-border credit data, New York (as the General Catalyst and YC rows). The firm's post of "
                  "2020-02-12 says it leads the Series B, closed in its 2019 entry year."))

L.append(cls("nuna", status="private", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2014", focus="Healthcare & Bio", rounds=[],
             note="Healthcare data platform, San Francisco. The firm lists a 2014 entry; no source read names that "
                  "round."))

L.append(cls("nurx", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2017", focus="Healthcare & Bio", rounds=[],
             note="Telehealth prescriptions, San Francisco (as the USV row); it merged into Thirty Madison in 2022. The "
                  "firm lists a 2017 entry labelled Growth; no source read names that round."))

L.append(cls("nuvasive-inc", country="US", city="San Diego", rng="below_1b", stage="undetermined",
             focus="Healthcare & Bio", rounds=[],
             note="Spine surgery devices, San Diego; it merged into Globus Medical in 2023. The 2004 S-1 exhibits show "
                  "Kleiner Perkins Caufield & Byers VIII as a signatory investor; no source read names its round."))

jl.write("j03b", L)
