"""PRO-75 GV, judge j7: queue batch 7 (45 member rows, iPierian to Magenta Therapeutics).

Every citation below is a URL a tool printed (the NEWS/POST/W/FTS/ARCH helpers, TechCrunch tag pages listed by the
judge's own tools, a sibling book's row, the GV CMS row) and whose page the judge read (WebFetch or curl), or a
headline read on its visible surface (the paywall rule). Research ran 2026-09-28.
"""
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
_BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def FD(slug, i=0):
    """The i-th Form D index link on the row's own formd_links (base.json)."""
    links = [x.strip() for x in (_BASE[slug].get("formd_links") or "").split(";") if x.strip()]
    return links[i]


ASOF = "2026-09-28"
L = []

# ---------------------------------------------------------------- iPierian
BMS = "https://news.bms.com/news/details/2014/Bristol-Myers-Squibb-Acquires-iPierian-Inc/default.aspx"
L.append(cls("ipierian", status="acquired", rng="below_1b", stage="undetermined",
             city="South San Francisco", city_src="formd_address", focus="Healthcare & Bio",
             note="Cellular reprogramming drug discovery (South San Francisco; 951 Gateway Boulevard on its Form Ds). "
                  "Bristol-Myers Squibb bought it in April 2014 for $175M upfront plus up to $550M in milestones (BMS "
                  "release, which names Kleiner Perkins, MPM Capital, SR One, Highland Capital and Google Ventures as its "
                  "backers). Google Ventures entered through the $28.97M round on the 2010 Form D, where Krishna Yeshwant "
                  "sits as director; no source names that round (the 2009 Form Ds follow the iZumi Bio merger), and Google "
                  "News and the BMS release give no label, so the stage is undetermined.",
             rounds=[rnd("2009", "unnamed (two 2009 Form D filings, $11.5M and $0.94M)", 12438588, None, False,
                         FD("ipierian", 0), "filing"),
                     rnd("2010-07-01", "unnamed ($28.97M Form D, Krishna Yeshwant director)", 28970000, None, True,
                         FD("ipierian", 1), "filing")]))

# ---------------------------------------------------------------- Isomorphic Labs
ISO_B = NEWS("isomorphic-labs", "announces Series B investment round")
ISO_YF = NEWS("isomorphic-labs", "raises $2.1 billion Series B for AI")
ISO_TC = "https://techcrunch.com/2025/03/31/alphabets-ai-drug-discovery-platform-isomorphic-labs-raises-600m-from-thrive/"
L.append(cls("isomorphic-labs", status="private", rng="1b_plus", usd=2100000000, val_src="web_verified",
             val_cite=ISO_B, asof="2026-05-12",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ISO_YF, entry_date="2025-03-31",
             city="London", focus="Healthcare & Bio", flags=["model_disputes_source"],
             note="AI drug discovery, the DeepMind spin-out (London). Status disputes the Wikidata 'acquired': Alphabet "
                  "controls it, but it sells priced rounds to outside investors, so it reads private at its latest round "
                  "(decisions.md D4, the Waymo reading). GV entered in the $600M first external round of March 2025 led "
                  "by Thrive (TechCrunch: 'participation from GV and existing investor Alphabet'; the firm's /ai list, "
                  "Invested 2025-03); Yahoo Finance names that round 'the 2025 Series A' and GV an existing backer in the "
                  "$2.1B Series B of May 2026. The Series B closed at an undisclosed valuation (the company's post and "
                  "Yahoo), so the $2.1B is the arithmetic floor of the post-money, not a mark, aligned with Thrive's row.",
             rounds=[rnd("2025-03-31", "Series A", 600000000, "Thrive Capital", True, ISO_TC, "press"),
                     rnd("2026-05-12", "Series B", 2100000000, "Thrive Capital", True, ISO_B, "company")]))

# ---------------------------------------------------------------- Iterative Health
ITH = NEWS("iterative-health", "Raises $77 Million Series C to Scale")
L.append(cls("iterative-health", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ITH, entry_date="2026-04-30",
             country="US", city="Cambridge", city_src="web_verified", focus="Healthcare & Bio",
             note="AI-driven clinical research network, formerly Iterative Scopes (Cambridge MA and New York, per the "
                  "release). GV co-led the $77M Series C of April 2026 with Intrepid Growth Partners, named as a lead and "
                  "not among the existing investors (Insight Partners, Obvious Ventures), and the firm first lists the "
                  "company in 2026: a Series C entry, Growth. No valuation was disclosed (checked 2026-09-28).",
             rounds=[rnd("2026-04-30", "Series C", 77000000, "Intrepid Growth Partners, GV", True, ITH, "press")]))

# ---------------------------------------------------------------- Jaunt
JA_VB = NEWS("jaunt", "grabs a real $27.8M")
L.append(cls("jaunt", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=JA_VB, entry_date="2014-08-21",
             country="US", city="San Mateo", city_src="web_verified", focus="Media, Gaming & Advertising",
             note="Cinematic virtual reality capture and content. Google Ventures co-led the $27.8M Series B of August "
                  "2014 with Highland Capital (VentureBeat; about $6M had been raised before it, the Series A Redpoint "
                  "says it joined in 2013), so the entry is Growth. Jaunt wound down its VR products in October 2018 and "
                  "kept its AR capture work in San Mateo (UploadVR); Verizon bought it in 2019 (CNBC headline, the "
                  "firm's exit line 'Acquired by Verizon, 2019').",
             rounds=[rnd("2014-08-21", "Series B", 27800000, "Highland Capital Partners, Google Ventures", True, JA_VB,
                         "press"),
                     rnd("2015-09-21", "unnamed", 65000000, None, None, NEWS("jaunt", "adds $65m"), "press")]))

# ---------------------------------------------------------------- Jet
JET_A = "https://techcrunch.com/2014/09/16/quidsi-co-founder-raises-an-additional-20m-for-a-new-e-commerce-biz/"
JET_B = "https://techcrunch.com/2015/02/11/e-commerce-site-jet-raises-another-140m/"
L.append(cls("jet", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=JET_B, entry_date="2015-02-11",
             city="Hoboken", city_src="web_verified", focus="Consumer & Marketplaces",
             note="Marc Lore's e-commerce company (Hoboken NJ, Wikipedia). Its Series A closed at $80M in September 2014 "
                  "with NEA, Accel, Bain Capital Ventures, MentorTech, Western Technology Investment and SVB, without "
                  "Google Ventures (TechCrunch). Google Ventures is named in the $140M round of February 2015 led by Bain "
                  "Capital Ventures (TechCrunch), the round after the Series A, so the entry is Growth. Walmart bought "
                  "Jet for $3.3B in August 2016 (Wikipedia).",
             rounds=[rnd("2014-09-16", "Series A", 80000000, "NEA", False, JET_A, "press"),
                     rnd("2015-02-11", "unnamed (the round after the Series A)", 140000000, "Bain Capital Ventures",
                         True, JET_B, "press"),
                     rnd("2015-11", "unnamed", 350000000, "Fidelity", None, W("Jet.com"), "press")]))

# ---------------------------------------------------------------- Jetify
JTF = NEWS("jetify", "GC AI Acquires")
L.append(cls("jetify", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="San Francisco", focus="DevTools & APIs",
             note="Developer environments (Devbox, Nixhub) and the Testpilot AI QA agent, formerly Jetpack.io (renamed "
                  "April 2024, the company's blog). GC AI acquired it in June 2026, terms undisclosed (Law.com, "
                  "2026-08-10). GV's listing names Erik Nordlander; no source names the round GV entered (TechCrunch, "
                  "Google News, the company's site and blog), so the stage is undetermined. City aligned with Coatue's "
                  "row.",
             rounds=[]))

# ---------------------------------------------------------------- JumpCam
JC = NEWS("jumpcam", "JumpCam, Backed With")
L.append(cls("jumpcam", status="unknown", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=JC, entry_date="2013-09-26",
             country="US", city="San Francisco", city_src="web_verified", focus="Consumer & Marketplaces",
             note="Collaborative mobile video app (San Francisco). Trinity Ventures and Google Ventures led its $2.7M "
                  "Series A (TechCrunch, September 2013). Status unknown: no source read gives its fate (Google News "
                  "finds nothing after early 2014, EDGAR has no filer by the name, jumpcam.com is a parked domain, and "
                  "the firm's listing carries no exit line).",
             rounds=[rnd("2013-09-26", "Series A", 2700000, "Trinity Ventures, Google Ventures", True, JC, "press")]))

# ---------------------------------------------------------------- Kabam
KB = NEWS("kabam", "Kabam nets extra")
L.append(cls("kabam", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=KB, entry_date="2011-05-26",
             city="San Francisco", focus="Media, Gaming & Advertising",
             note="Mobile and social games publisher (San Francisco until the 2017 break-up). Google Ventures co-led the "
                  "$85M Series D of May 2011 with Pinnacle Ventures, while Canaan, Redpoint and Intel Capital are named "
                  "as the earlier investors (GamesIndustry.biz), so the entry is Growth. Netmarble bought the Kabam "
                  "Vancouver studio and brand in 2017 for about $800M (the firm's exit line 'Acquired by Netmarble, "
                  "2017'); its last private valuation was about $1B (the unicorn snapshot), $700M in a 2013 employee "
                  "sale (Techcircle headline).",
             rounds=[rnd("2011-05-26", "Series D", 85000000, "Google Ventures, Pinnacle Ventures", True, KB, "press")]))

# ---------------------------------------------------------------- Kamcord
KC_SEED = ("https://techcrunch.com/2012/12/19/mobile-game-recording-yc-alum-kamcord-raises-1-5-million-from-andreessen"
           "-horowitz-google-ventures-and-others/")
KC_B = NEWS("kamcord", "GungHo leads")
KC_LYFT = "https://techcrunch.com/2017/11/16/lyft-acquihires-the-kamcord-team-for-engineering-talent/"
L.append(cls("kamcord", status="defunct", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=KC_SEED, entry_date="2012-12-19",
             grad="graduated", grad_src="web_verified", grad_cite=KC_B, grad_conf="high",
             country="US", city="San Francisco", focus="Media, Gaming & Advertising",
             note="Mobile game recording and live streaming (Y Combinator S12, San Francisco). Google Ventures was in the "
                  "$1.5M seed with Andreessen Horowitz and Tencent (TechCrunch, December 2012). A named $15M Series B led "
                  "by GungHo followed in December 2014 (GamesIndustry.biz), which graduates the row, and a $10M Series C "
                  "in 2016. Defunct under the acqui-hire rule: Lyft hired 12 of the team in November 2017 'though not any "
                  "of the broadcast live streaming app's technologies' (TechCrunch), and kamcord.com now serves an "
                  "unrelated blog; the firm's exit line 'Acquired by Lyft, 2017' names the hire. Aligned with the a16z, "
                  "General Catalyst and Y Combinator rows.",
             rounds=[rnd("2012-12-19", "Seed", 1500000, None, True, KC_SEED, "press"),
                     rnd("2014-12-11", "Series B", 15000000, "GungHo Online Entertainment", None, KC_B, "press"),
                     rnd("2016-04", "Series C", 10000000, "Time Warner", None, KC_LYFT, "press")]))

# ---------------------------------------------------------------- Kensho
KS_FIN = NEWS("kensho", "Boosts Total Capital")
L.append(cls("kensho", status="acquired", rng="below_1b", stage="undetermined", entry_date="2013",
             country="US", city="Cambridge", city_src="web_verified", focus="Fintech & Payments",
             note="AI analytics for financial professionals (Cambridge MA, Finovate). The firm's own post says 'we were "
                  "early investors in his first company, Kensho, in 2013' (" + POST("openevidence-ai-doctors") + "), "
                  "which dates the entry but names no round; Finovate (2015) lists Google Ventures among the earlier "
                  "investors and no source names the 2013 round (Kensho's first Form D is dated 2013-11-22 on EDGAR), so "
                  "the stage is undetermined. S&P Global bought it for $550M in 2018 (the firm's exit line; Business "
                  "Insider headline).",
             rounds=[rnd("2013", "unnamed (the firm's own post: early investor in 2013)", None, None, True,
                         POST("openevidence-ai-doctors"), "firm"),
                     rnd("2014-11", "unnamed", 15000000, "Goldman Sachs", None, KS_FIN, "press"),
                     rnd("2015-08", "unnamed (regulatory filings)", 33000000, None, None, KS_FIN, "press")]))

# ---------------------------------------------------------------- Kindbody
KBD_A = NEWS("kindbody", "How Kindbody Is Reinventing")
KBD_B = NEWS("kindbody", "Fertility Care And Testing Company Kindbody Secures")
KBD_F = NEWS("kindbody", "Female founders had a record year")
L.append(cls("kindbody", status="private", rng="below_1b", stage="undetermined",
             country="US", city="New York", city_src="web_verified", focus="Healthcare & Bio",
             extra={"valuation_range_source": "web_verified", "valuation_citation": KBD_F, "valuation_asof": "2026-03-24"},
             note="Fertility and women's health clinics (New York). GV is not among the investors of the $15M Series A of "
                  "April 2019 (led by RRE and Perceptive) nor the earlier angels (Pulse 2.0), yet it is an 'existing "
                  "investor' in the $32M Series B of July 2020 led by Perceptive (Pulse 2.0); totals imply about $10M "
                  "raised between the two, which no source names, so the round GV entered is undetermined. The $100M of "
                  "March 2023 at $1.8B (Axios headline) yields to documented collapse evidence: Fortune (2026-03-24) "
                  "reports the valuation 'had fallen to $400 million as it shuttered clinics', so the row reads below_1b "
                  "with no figure minted. Still operating (new CEO June 2025, platform launch February 2026, PR "
                  "Newswire).",
             rounds=[rnd("2019-04-28", "Series A", 15000000, "RRE Ventures, Perceptive Advisors", False, KBD_A, "press"),
                     rnd("2020-07-14", "Series B", 32000000, "Perceptive Advisors", True, KBD_B, "press"),
                     rnd("2021-06-25", "Series C", 62000000, None, None,
                         NEWS("kindbody", "Raises a $62M Series C"), "press"),
                     rnd("2023-03-02", "unnamed ($1.8B valuation)", 100000000, None, None,
                         NEWS("kindbody", "gets $100M at $1.8B"), "press")]))

# ---------------------------------------------------------------- Kindred
KD_B = "https://betakit.com/kindred-closes-35-4m-series-b-from-tencent-launches-pilot-program-with-major-retailers/"
KD_OC = NEWS("kindred", "Ocado acquires Haddington Dynamics, Kindred")
L.append(cls("kindred", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="San Francisco", city_src="web_verified", focus="Industrial & Robotics",
             note="Kindred Systems, AI robotic piece-picking for warehouses (founded in Vancouver; 'San Francisco-based' "
                  "when Ocado bought it for about $262M in November 2020, The Robot Report). The Tencent-led Series B of "
                  "October 2017 (BetaKit) does not name GV, and no source read ties GV to a round, so the stage is "
                  "undetermined. The a16z 'Kindred' row is a different company (a home-swapping network).",
             rounds=[rnd("2017-10-24", "Series B", 28000000, "Tencent", None, KD_B, "press")]))

# ---------------------------------------------------------------- Kinetic Apps
L.append(cls("kinetic-apps", status="private", rng="below_1b", stage="undetermined",
             country="US", city="New York", city_src="web_verified", focus="AI & Applied AI",
             note="Builds a portfolio of consumer software apps with small AI-native teams ('AI lets 10 people do what "
                  "used to take 100'); office in Brooklyn, New York (kineticapps.ai). Listed by the firm from 2026 (KJ "
                  "Sidberry). No round source found. Momentum slice check 2026-09-28 (Google News on the name, EDGAR): "
                  "no priced round reported at all, so nothing at or above $1B.",
             rounds=[]))

# ---------------------------------------------------------------- Kitchen United
KU_RB = NEWS("kitchen-united", "nets $10M investment")
KU_FSR = NEWS("kitchen-united", "C3 Acquires Remaining Assets")
L.append(cls("kitchen-united", status="acquired", rng="below_1b",
             stage="Series A", stage_src="model", stage_conf="medium", stage_cite=KU_RB, entry_date="2018-10-08",
             country="US", city="Pasadena", city_src="web_verified", focus="Consumer & Marketplaces",
             note="Ghost-kitchen operator (Pasadena). GV led the $10M round of October 2018 (Restaurant Business: 'The "
                  "lead investor ... is GV'), which Wikipedia calls the company's initial funding and follows with a "
                  "'$40-million series B round' GV also joined; the round is unnamed in the press, and with a named "
                  "Series B next it reads as the Series A (model, medium). C3, Sam Nazarian's platform, acquired its IP "
                  "and remaining assets in March 2024 after the kitchens closed (FSR Magazine): an asset sale, so "
                  "acquired, the business continuing under C3.",
             rounds=[rnd("2018-10-08", "unnamed (initial funding)", 10000000, "GV", True, KU_RB, "press"),
                     rnd("2019", "Series B", 40000000, None, True, W("Kitchen United"), "press"),
                     rnd("2022-07", "unnamed", 100000000, None, None, KU_FSR, "press")]))

# ---------------------------------------------------------------- Kobalt
KO_TC = "https://techcrunch.com/2015/02/26/kobalt-tunes-into-60m-led-by-google-ventures-for-its-music-rights-collection-platform/"
KO_MBW = NEWS("kobalt", "Done deal")
L.append(cls("kobalt", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=KO_TC, entry_date="2015-02-26",
             country="US", city="New York", focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
             note="Music publishing and rights-management company. Google Ventures led the $60M Series C of February "
                  "2015 with MSD Capital, an earlier investor, also in (TechCrunch), so the entry is Growth. Francisco "
                  "Partners took a controlling stake in September 2022 (Wikipedia), and Primary Wave's purchase of "
                  "Kobalt from Francisco Partners closed on 2026-07-07 (Music Business Worldwide): acquired. The "
                  "pre-filled IT is a wrong Wikidata join on a one-word name; the company has offices in London and New "
                  "York (TechCrunch, which in 2017 calls it a European startup) and was founded in New York per Wikipedia; "
                  "country and city aligned with Balderton's row (New York). The Y Combinator 'Kobalt' row is a different company.",
             rounds=[rnd("2015-02-26", "Series C", 60000000, "Google Ventures", True, KO_TC, "press"),
                     rnd("2017-05-08", "Series D ($775M post-money)", 75000000, "Hearst Entertainment", None,
                         "https://techcrunch.com/2017/05/08/music-royalty-collector-kobalt-nabs-75m-led-by-hearst-entertainment-at-775m-valuation/",
                         "press")]))

# ---------------------------------------------------------------- Kronos Bio
KR_S1 = FTS("Kronos Bio", "S-1")
L.append(cls("kronos-bio", rng="below_1b", stage="undetermined",
             country="US", city="San Mateo", city_src="web_verified", focus="Healthcare & Bio",
             note="Small-molecule oncology (principal executive offices in San Mateo, per its S-1). GV (formerly Google "
                  "Ventures) is named among its investors in the 2020 DRS and S-1, but below the 5% line, so the "
                  "certain-transactions tables do not say which series it bought: the Series Seed ($11.5M, May 2018) or "
                  "the Series A ($105.0M, July 2019). Stage undetermined. Concentra Biosciences agreed to buy it in May "
                  "2025 (Fierce Biotech headline).",
             rounds=[rnd("2018-05", "Series Seed", 11500000, None, None, KR_S1, "filing"),
                     rnd("2019-07", "Series A", 105000000, None, None, KR_S1, "filing"),
                     rnd("2020-08", "convertible notes (2020 Notes)", 155200000, None, None, KR_S1, "filing")]))

# ---------------------------------------------------------------- Lacework
LW_TC21 = "https://techcrunch.com/2021/01/07/lacework-lands-525m-investment-as-revenue-grows-300/"
LW_TC24 = "https://techcrunch.com/2024/04/18/wiz-is-in-talks-to-buy-lacework-for-150-200m-security-firm-was-last-valued-at-8-3b/"
L.append(cls("lacework", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="San Jose", city_src="web_verified", focus="Security",
             note="Cloud security platform ('based in San Jose', TechCrunch 2024). TechCrunch (April 2024) lists GV "
                  "among its investors, but neither the Series D of January 2021 (TechCrunch) nor the $1.3B round of "
                  "November 2021 at $8.3B (CRN) names GV, and the firm first lists it in 2022, so the round GV entered "
                  "is undetermined. Fortinet bought it in 2024 (the firm's exit line). City aligned with the General "
                  "Catalyst and Sutter Hill rows (Coatue's reads Mountain View).",
             rounds=[rnd("2021-01-07", "Series D", 525000000, "Sutter Hill Ventures, Altimeter Capital", None, LW_TC21,
                         "press"),
                     rnd("2021-11-18", "Series D (CRN), $8.3B valuation", 1300000000,
                         "Sutter Hill Ventures, Altimeter, D1, Tiger Global", None,
                         NEWS("lacework", "Raises $1.3B On $8.3B"), "press")]))

# ---------------------------------------------------------------- Lapse
LP_S = ("https://techcrunch.com/2021/12/20/lapse-an-app-that-lets-you-snap-and-develop-rolls-of-film-with-groups-of-"
        "friends-raises-11m-from-gv-and-others/")
LP_A = "https://techcrunch.com/2024/02/27/lapse-the-app-turning-your-phone-into-an-old-school-camera-snaps-up-30m/"
L.append(cls("lapse", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=LP_S, entry_date="2021-12-20",
             grad="graduated", grad_src="web_verified", grad_cite=LP_A, grad_conf="high",
             country="GB", country_src="web_verified", country_cite=LP_S, city="London", city_src="web_verified",
             focus="Consumer & Marketplaces",
             note="Disposable-camera photo-sharing app (London). Octopus Ventures and GV led the $11M seed of December "
                  "2021, after a pre-seed led by Speedinvest (TechCrunch). Greylock and DST co-led the $30M Series A of "
                  "February 2024 with GV following, at a valuation of about $150M per sources (TechCrunch), which "
                  "graduates the row.",
             rounds=[rnd("2021-12-20", "Seed", 11000000, "Octopus Ventures, GV", True, LP_S, "press"),
                     rnd("2024-02-27", "Series A", 30000000, "Greylock, DST Global", True, LP_A, "press")]))

# ---------------------------------------------------------------- Lattice
L.append(cls("lattice", stage="undetermined", entry_date="2016-04", rng="below_1b", focus="AI & Applied AI",
             flags=["city_unknown"],
             note="Lattice Data, machine learning that turns unstructured data into structured data (from Stanford's "
                  "DeepDive project, co-founded by Chris Re). The firm's /ai list dates GV's investment to April 2016 "
                  "(its first AI investment, per its 2023 post); no source names the round. Apple bought it in May 2017 "
                  "for a reported $175M to $200M (Fortune). No source read places its office, so the city is left open. "
                  "The Thrive and Y Combinator 'Lattice' rows are the HR-software company (lattice.com), a different "
                  "company.",
             rounds=[rnd("2016-04", "unnamed (the firm's /ai list: Invested 2016-04)", None, None, True, jl.AI_LISTING,
                         "firm")]))

# ---------------------------------------------------------------- LaunchKit
LK = "https://techcrunch.com/2016/07/27/launchkit-team-heads-to-google-and-open-sources-its-tools-for-helping-devs-launch-their-apps/"
L.append(cls("launchkit", status="defunct", rng="below_1b", stage="undetermined",
             country="US", city="San Francisco", focus="DevTools & APIs",
             note="Tools for launching mobile apps. Defunct under the acqui-hire rule: in July 2016 the team joined "
                  "Google's Developer Product Group, the products did not move to Google, were open-sourced, and the "
                  "hosted services were discontinued after 12 months (TechCrunch); the firm's exit line reads 'Acquired "
                  "by Google, 2016'. The company raised $2.2M in all ($1.6M for its earlier app Cluster, $600K after the "
                  "pivot) from Baseline, Freestyle, First Round, SV Angel, GV and others (TechCrunch), with no date or "
                  "label per tranche, so GV's round is undetermined. First Round's row reads acquired from before the "
                  "2026-09-20 acqui-hire ruling.",
             rounds=[rnd(None, "unnamed (Cluster era)", 1600000, None, None, LK, "press"),
                     rnd(None, "unnamed (after the pivot to LaunchKit)", 600000, None, None, LK, "press")]))

# ---------------------------------------------------------------- Laurel
LR_F = NEWS("laurel", "Laurel raises $100 million Series C")
L.append(cls("laurel", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LR_F, entry_date="2025-06-10",
             country="US", city="San Francisco", focus="AI & Applied AI", flags=["model_disputes_source"],
             extra={"valuation_range_source": "web_verified", "valuation_citation": LR_F, "valuation_asof": "2025-06-10"},
             note="AI time intelligence and timekeeping for professional-services firms (formerly Time By Ping). IVP led "
                  "the $100M Series C of June 2025, and 'GV and 01 Advisors joined as new investors in the round, which "
                  "values Laurel at $510 million' (Fortune); the firm's /ai list dates GV's investment to 2025-04. "
                  "Momentum slice check 2026-09-28 (Google News on the name with raises and valuation): no later priced "
                  "round, the latest mark $510M, below $1B. The pre-filled JP is a namesake's Wikidata country; San "
                  "Francisco aligned with the IVP row.",
             rounds=[rnd("2025-06-10", "Series C", 100000000, "IVP", True, LR_F, "press")]))

# ---------------------------------------------------------------- Lawhive
LH_TC = NEWS("lawhive", "raises $40M to go after")
LH_LF = NEWS("lawhive", "£9.5m Google funding boost")
LH_F = NEWS("lawhive", "raises $60 million in new funding")
L.append(cls("lawhive", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=LH_TC, entry_date="2024-04-17",
             grad="graduated", grad_src="web_verified", grad_cite=LH_TC, grad_conf="high",
             country="GB", country_src="web_verified", country_cite=LH_TC, city="London", city_src="web_verified",
             focus="AI & Applied AI",
             extra={"valuation_range_source": "web_verified", "valuation_citation": LH_F, "valuation_asof": ASOF},
             note="AI-native consumer law firm and platform (London). GV led the GBP 9.5M round of April 2024 (Legal "
                  "Futures), which TechCrunch calls 'an $11.9 million seed round'; an earlier GBP 1.8M seed of 2022 did "
                  "not include GV. GV then co-led the $40M Series A of December 2024 as an 'existing investor' "
                  "(TechCrunch), which graduates the row, and joined the $60M Series B of February 2026 led by Mitch "
                  "Rales (Fortune). Momentum slice check 2026-09-28 (Google News on the name with valuation): no "
                  "valuation disclosed for the Series B and no priced mark at or above $1B; aligned with Balderton's "
                  "row.",
             rounds=[rnd("2024-04-17", "Seed", 11900000, "GV", True, LH_LF, "press"),
                     rnd("2024-12-04", "Series A", 40000000, "GV, TQ Ventures", True, LH_TC, "press"),
                     rnd("2026-02-05", "Series B", 60000000, "Mitch Rales", True, LH_F, "press")]))

# ---------------------------------------------------------------- LawPivot
LPV_S = "https://techcrunch.com/2011/01/19/google-ventures-leads-600k-investment-in-lawpivot-a-quora-for-startup-legal-advice/"
LPV_S2 = "https://techcrunch.com/2011/12/01/qa-platform-lawpivot-raises-1m-launches-legal-services-marketplace/"
LPV_ACQ = ("https://techcrunch.com/2013/01/14/rocket-lawyer-acquires-lawpivot-to-add-a-quora-like-qa-platform-to-"
           "online-legal-services-site/")
L.append(cls("lawpivot", status="acquired", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=LPV_S, entry_date="2011-01-19",
             grad="not_graduated", grad_src="web_verified", grad_cite=LPV_ACQ, grad_conf="high", grad_asof=ASOF,
             surfaces=["firm: the firm's own listing for LawPivot (on googleventures.com from the 2012 capture) -> exit "
                       "line 'Acquired by Rocket Lawyer, 2013'; no post of the firm names the company",
                       "formd: EDGAR company search 'lawpivot' for Form D filings -> no filer by that name",
                       "techcrunch: TechCrunch's own tag page for LawPivot -> five articles: the $600K seed led by "
                       "Google Ventures (2011-01-19), the $1M 'additional seed funding' (2011-12-01) and the Rocket "
                       "Lawyer acquisition (2013-01-14); no Series A or later round",
                       "googlenews: Google News, 'LawPivot' and 'LawPivot' beside 'Google Ventures' -> two results "
                       "(New York Times 2011, Stanford CodeX 2016), none reporting a later round"],
             country="US", focus="Consumer & Marketplaces", flags=["city_unknown"],
             note="Legal Q&A marketplace connecting startups with lawyers. Google Ventures led its $600K seed in January "
                  "2011 (TechCrunch); a $1M round of 'additional seed funding' followed in December 2011 (TechCrunch). "
                  "Rocket Lawyer bought it in an all-stock deal in January 2013 (TechCrunch) with no priced round after "
                  "the seed: the acquisition ends the row as not graduated. No source read names its city.",
             rounds=[rnd("2011-01-19", "Seed", 600000, "Google Ventures", True, LPV_S, "press"),
                     rnd("2011-12-01", "Seed (additional)", 1000000, None, None, LPV_S2, "press")]))

# ---------------------------------------------------------------- Layer Health
LYH_S = NEWS("layer-health", "launches with $4M from Google Ventures")
LYH_A = NEWS("layer-health", "Raises $21 Million Series A")
L.append(cls("layer-health", status="private", rng="below_1b",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=LYH_S, entry_date="2022-12",
             grad="graduated", grad_src="web_verified", grad_cite=LYH_A, grad_conf="high",
             city="Boston", city_src="formd_address", focus="Healthcare & Bio", flags=["stage_disputes_band"],
             note="AI chart review for health systems (Boston; 141 Tremont Street on its 2025 Form D). Disputes the Form D "
                  "band: the filing the band read is the $21M Series A of 2025, which the firm's own /ai list records as "
                  "a re-investment (Invested 2022-12, Re-invested 2024-12). GV's entry is the $4M launch round with "
                  "General Catalyst (MobiHealthNews headline, November 2023), unnamed in what was read; before a named "
                  "Series A it reads as the seed (model, medium). The Series A, led by Define Ventures with GV "
                  "participating (Healthcare IT Today), graduates the row. Entry date is the firm's own Invested month "
                  "(decisions.md D7). The General Catalyst row's 'unknown' status predates the 2025 round.",
             rounds=[rnd("2022-12", "unnamed launch round (announced 2023-11-22)", 4000000, None, True, LYH_S, "press"),
                     rnd("2025-03-27", "Series A", 21000000, "Define Ventures", True, LYH_A, "press")]))

# ---------------------------------------------------------------- LedgerX
L.append(cls("ledgerx", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="New York", focus="Crypto & Web3",
             note="CFTC-regulated bitcoin options exchange and clearing house (New York). On the firm's listing from its "
                  "November 2014 capture (Blake Byers); no source read names the round GV entered (Google News, "
                  "TechCrunch, EDGAR), so the stage is undetermined. FTX.US bought it in August 2021 (The Block; the "
                  "firm's exit line 'Acquired by FTX, 2021'); FTX's estate sold it on in 2023. Status and city aligned "
                  "with Lightspeed's row.",
             rounds=[]))

# ---------------------------------------------------------------- Lemonade
LM_CM = "https://www.carriermanagement.com/news/2016/12/05/161735.htm"
L.append(cls("lemonade", status="public", rng="1b_plus", usd=3400000000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/lmnd/market-cap/", asof=ASOF,
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LM_CM, entry_date="2016-12-05",
             city="New York", focus="Fintech & Payments",
             note="AI-driven insurance carrier (New York; NYSE: LMND since July 2020). The firm's post says 'When GV "
                  "first invested in Lemonade in 2016' (" + POST("lemonade-ipo") + "); Carrier Management names GV among "
                  "the new participants in the $34M Series B of December 2016 led by General Catalyst, apart from the "
                  "existing investors XL Innovate, Aleph and Sequoia, so the entry is Growth. Market cap $3.4B on "
                  "2026-09-28 (stockanalysis.com).",
             rounds=[rnd("2015-12", "Seed", None, None, False, LM_CM, "press"),
                     rnd("2016-12-05", "Series B", 34000000, "General Catalyst", True, LM_CM, "press"),
                     rnd("2019-04-15", "Series D", 300000000, "SoftBank", True,
                         NEWS("lemonade", "Lemonade closes Series D"), "press")]))

# ---------------------------------------------------------------- LendUp
LU_12 = ("https://techcrunch.com/2012/10/10/lendup-raises-cash-from-kleiner-perkins-andreessen-horowitz-google-ventures-"
         "and-others-to-disrupt-payday-loans/")
LU_13 = "https://techcrunch.com/2013/11/12/lendup-raises-14m-from-google-ventures-data-collective-to-disrupt-payday-lending/"
L.append(cls("lendup", status="defunct", rng="below_1b", stage="undetermined", entry_date="2012-10-10",
             city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
             note="Online lender to low-credit borrowers (Y Combinator, San Francisco). Google Ventures is among the VCs "
                  "and angels funding its October 2012 launch (TechCrunch) and in the $14M round of November 2013 with "
                  "QED and Data Collective (TechCrunch); neither round is named and the launch round's size (about $4M "
                  "by the totals) sits on the seed and Series A band edge, so the stage is undetermined. It ceased "
                  "lending in January 2022 under a CFPB order (Wikipedia; American Banker headline): defunct, aligned "
                  "with the a16z and Y Combinator rows.",
             rounds=[rnd("2012-10-10", "unnamed (launch funding)", None, None, True, LU_12, "press"),
                     rnd("2013-11-12", "unnamed", 14000000, None, True, LU_13, "press")]))

# ---------------------------------------------------------------- LevelUp
LV_09 = "https://techcrunch.com/2009/12/24/scvngr-google/"
LV_11 = "https://techcrunch.com/2011/01/04/scvngr-raises-15-million-at-100mm-valuation/"
LV_GH = "https://www.balderton.com/news/levelup-is-acquired-by-chicago-based-grubhub/"
L.append(cls("levelup", status="acquired", rng="below_1b", stage="undetermined", city="Boston",
             focus="Fintech & Payments", flags=["stage_disputes_band"], extra={"entry_stage_source": None},
             note="Mobile payments and loyalty for restaurants, born as SCVNGR (Boston). Disputes the Form D band's "
                  "Seed: Google Ventures' round is the $4M of December 2009, which it led with Highland Capital as an "
                  "existing investor (TechCrunch), and TechCrunch (2011) lists it after 'some seed funding before that', "
                  "so it was not the seed; Balderton's own card labels its $15M round of the following year 'Series C', "
                  "which would make the 2009 round a Series B, against the reading that it was the Series A. The record "
                  "does not settle the label, so the stage is undetermined. Grubhub bought LevelUp in 2018 (Balderton's "
                  "post). City aligned with Balderton's row.",
             rounds=[rnd("2009-12-24", "unnamed", 4000000, "Google Ventures", True, LV_09, "press"),
                     rnd("2011-01-04", "unnamed (Balderton's card: Series C)", 15000000, "Balderton Capital", True, LV_11,
                         "press"),
                     rnd("2012-06-07", "unnamed", 12000000, None, True,
                         "https://techcrunch.com/2012/06/07/levelup-raises-12m/", "press")]))

# ---------------------------------------------------------------- Leyden Labs
LY_DDT = NEWS("leyden-labs", "closes $140M in Series B")
L.append(cls("leyden-labs", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=LY_DDT, entry_date="2021-03-25",
             country="NL", country_src="web_verified", country_cite="https://leydenlabs.com", city="Leiden",
             city_src="web_verified", focus="Healthcare & Bio",
             note="Intranasal antibodies against respiratory viruses (Leyden Laboratories B.V., Emmy Noetherweg 2, Leiden, "
                  "per its own site). GV led the EUR 40M (about $45M) Series A of March 2021 (Drug Discovery & "
                  "Development) that launched the company, the firm's own post announcing it with '$47 million in "
                  "funding' (" + POST("leyden-labs") + "), then co-led the $140M Series B of January 2022 with Casdin. "
                  "Later money: $70M (January 2025), EUR 30M from the EIC Fund and Invest-NL (October 2025) and EUR 40M "
                  "(June 2026, European Biotechnology); no valuation disclosed.",
             rounds=[rnd("2021-03-25", "Series A", 45000000, "GV", True, LY_DDT, "press"),
                     rnd("2022-01-25", "Series B", 140000000, "Casdin Capital, GV", True, LY_DDT, "press"),
                     rnd("2026-06-25", "unnamed", None, None, None, NEWS("leyden-labs", "adds €40m for intranasal"),
                         "press")]))

# ---------------------------------------------------------------- LifeMine Therapeutics
L.append(cls("lifemine-therapeutics", status="private", rng="below_1b", city="Cambridge", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Genomic drug discovery from fungi (Cambridge MA; 100 Acorn Park on its Form D). Still private: a $75M "
                  "Series D in November 2025 'featuring existing investors like GSK and Google Ventures' and a $188M "
                  "Series E in 2026 ($263M in all) with no valuation disclosed (Fierce Biotech), so below_1b.",
             rounds=[rnd("2026-08-06", "Series E", 188000000, None, None,
                         NEWS("lifemine-therapeutics", "How LifeMine won over Gates"), "press")]))

# ---------------------------------------------------------------- Lightmatter
LT_OP = NEWS("lightmatter", "Google backs Lightmatter again")
LT_SA = NEWS("lightmatter", "raises $80M round backed by GV")
L.append(cls("lightmatter", status="private", rng="1b_plus", usd=4400000000, val_src="web_verified", val_cite=LT_OP,
             asof="2024-10",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=LT_OP, entry_date="2019-02",
             city="Boston", city_src="formd_address", focus="Industrial & Robotics", flags=["stage_disputes_band"],
             note="Photonic computing chips for AI data centers (Boston). Disputes the Form D band's Growth (it read the "
                  "2023 filing): GV 'invested in the firm's $33 million series A round completed in 2019' (Optics.org) "
                  "and the firm's /ai list dates its first investment to 2019-02, with the $22M February 2019 Form D; "
                  "GV then followed in the Viking-led $80M round of 2021 (SiliconANGLE) and later rounds. Latest priced "
                  "mark: the $400M Series D of October 2024 that 'effectively values it at $4.4 billion' (Optics.org), "
                  "aligned with Spark's row. Checked 2026-09-28: the $700M data-center photonics raise of August 2026 "
                  "(WSJ) was Lumilens, not Lightmatter; no newer round.",
             rounds=[rnd("2019", "Series A (completed in 2019; the February 2019 Form D reports $22.2M)", 33000000, None, True, LT_OP, "press"),
                     rnd("2021-05-06", "unnamed", 80000000, "Viking Global Investors", True, LT_SA, "press"),
                     rnd("2024-10-16", "Series D", 400000000, None, True, LT_OP, "press")]))

# ---------------------------------------------------------------- Lime
L.append(cls("lime", status="public", rng="1b_plus", usd=1880000000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/lime/market-cap/", asof=ASOF,
             city="San Francisco", city_src="formd_address", focus="Consumer & Marketplaces",
             note="Shared e-bikes and scooters (Neutron Holdings, San Francisco). Listed on Nasdaq as LIME in July 2026 "
                  "(its 424B4 prospectus, " + FTS("Neutron Holdings", "424B4") + "). Market cap $1.88B on 2026-09-28 "
                  "(stockanalysis.com), aligned in band with the Atomico, BCV, Coatue and IVP rows."))

# ---------------------------------------------------------------- Locker Room
LR_TE = NEWS("locker-room", "acquires LA-based Betty Labs")
LR_DOT = NEWS("locker-room", "How Betty Labs CEO Built")
L.append(cls("locker-room", status="acquired", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=LR_TE, entry_date="2020-10",
             grad="not_graduated", grad_src="web_verified", grad_cite=LR_TE, grad_conf="high", grad_asof=ASOF,
             surfaces=["firm: the firm's own listing for Locker Room (from the 2020 capture) -> exit line 'Acquired by "
                       "Spotify, 2021'; no post of the firm names a later round",
                       "formd: EDGAR company search 'betty labs' for Form D filings -> one filer, 'Betty Labs SPV, a "
                       "series of Lambeth Family Office LLC' (Form D 2020-01-08), an investment vehicle, not the "
                       "company; no Form D by Betty Labs itself",
                       "techeu: Tech.eu's report of the Spotify acquisition (2021-03-31) -> names the $9.3M seed led by "
                       "GV as the company's latest raise; no later round",
                       "googlenews: Google News, 'Betty Labs' funding and 'Locker Room' beside GV -> the October 2020 "
                       "launch and the March 2021 Spotify purchase (Reuters, CNBC, dot.la); no later round"],
             country="US", city="Los Angeles", city_src="web_verified", focus="Media, Gaming & Advertising",
             note="Betty Labs, maker of the Locker Room live sports-audio app (Los Angeles). It 'raised $9.3 million in "
                  "seed funding led GV' (Tech.eu), the round of October 2020 (dot.la), after early backing from "
                  "Lightspeed. Spotify bought Betty Labs in March 2021 (Tech.eu, Reuters) with no round after the seed: "
                  "the acquisition ends the row as not graduated.",
             rounds=[rnd("2020-10", "Seed", 9300000, "GV", True, LR_TE, "press")]))

# ---------------------------------------------------------------- Lola
LO_C = NEWS("lola", "Lola.com Raises $37M to Transform")
LO_BG = NEWS("lola", "startup Lola adds $15m")
L.append(cls("lola", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LO_C,
             country="US", city="Boston", city_src="web_verified", focus="SaaS",
             note="Lola.com, Paul English's travel-booking company, later corporate travel management (Boston). General "
                  "Catalyst and Accel funded its first $19.7M, and CRV led the $15M of January 2017 with those two as the "
                  "earlier investors (Boston Globe); GV is first named in the $37M Series C of March 2019 led by General "
                  "Catalyst and Accel 'with participation from CRV, Tenaya Capital, and GV' (Coverager). The firm lists "
                  "Lola from 2017, so GV likely joined the 2017 round's later close; either way the entry is Series B or "
                  "later, Growth, and its date is left open. Capital One took most of its staff and software in October "
                  "2021, reported as an acquisition (Skift): acquired, aligned with Accel's row. The Spark 'Lola' row is "
                  "a different company (the LOLA tampon brand).",
             rounds=[rnd("2017-01-10", "unnamed", 15000000, "CRV", None, LO_BG, "press"),
                     rnd("2019-03-26", "Series C", 37000000, "General Catalyst, Accel", True, LO_C, "press")]))

# ---------------------------------------------------------------- Loom (the 2013 photo startup)
LOO_ACQ = ("https://techcrunch.com/2014/04/17/dropbox-acquires-cloud-photos-startup-loom-service-to-be-shut-down-as-"
           "users-transferred-to-carousel/")
L.append(cls("loom", status="acquired", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=LOO_ACQ, entry_date="2013",
             grad="not_graduated", grad_src="web_verified", grad_cite=LOO_ACQ, grad_conf="high", grad_asof=ASOF,
             surfaces=["firm: the firm's own listing for Loom (from the 2013 capture) -> exit line 'Acquired by Dropbox, "
                       "2014'; no post of the firm names a later round",
                       "formd: EDGAR company search 'loom' for Form D filings -> 40 filers named Loom, none identifiable "
                       "as the 2013 photo startup; no Form D found for it",
                       "techcrunch: TechCrunch's own tag page for Loom -> the photo startup's 2013 launch articles and the "
                       "Dropbox acquisition (2014-04-17), which names the $1.3M seed as its funding; no later round",
                       "googlenews: Google News, 'Loom' with photo and Dropbox -> seven results (The Verge 2013, "
                       "MacStories 2014 and others), none reporting a later round"],
             country="US", city="San Francisco", city_src="web_verified", focus="Consumer & Marketplaces",
             note="Loom, the cloud photo and video library of 2013 (San Francisco, formerly Popset), not the later Loom "
                  "video company. 'Loom raised $1.3 million in seed funding last fall from Google Ventures, Tencent, "
                  "Great Oaks VC' and others (TechCrunch, April 2014: fall 2013), and Dropbox bought it that month and "
                  "shut the service with no later round: not graduated. The a16z, Coatue, General Catalyst, Point Nine, "
                  "Sequoia, Y Combinator and ICONIQ 'Loom' rows, and the unicorn prefill of $1.53B, are the video company "
                  "Atlassian bought in 2023; GV's live CMS row carries that company's domain and sectors, while its exit "
                  "line and archived description identify the photo startup.",
             rounds=[rnd("2013", "Seed", 1300000, None, True, LOO_ACQ, "press")]))

# ---------------------------------------------------------------- LotusFlare
LF_TC = "https://techcrunch.com/2015/09/01/lotusflare-raises-6-million-to-help-emerging-markets-access-the-mobile-internet/"
L.append(cls("lotusflare", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=LF_TC,
             country="US", city="Santa Clara", city_src="web_verified", focus="SaaS",
             note="Cloud commerce and monetization platform for telecom operators (DNO Cloud) and the Nomad eSIM "
                  "business; its December 2025 release is datelined Santa Clara. Google Ventures was a seed investor in "
                  "the $4M seed (Wikipedia; TechCrunch names 'seed investors Google Ventures and Metamorphic Ventures' in "
                  "the Series A). Social+Capital led the $6M Series A of September 2015 (TechCrunch), which graduates the "
                  "row once the seed's date is on record: the company was founded in June 2014 (Wikipedia) and no source "
                  "dates the seed. Graduation left for the graduation pass. Ericsson bought a minority stake in December "
                  "2025 (PR Newswire).",
             rounds=[rnd(None, "Seed", 4000000, None, True, W("LotusFlare"), "press"),
                     rnd("2015-09-01", "Series A", 6000000, "Social+Capital", True, LF_TC, "press"),
                     rnd("2025-12-03", "minority equity investment", None, "Ericsson", None,
                         NEWS("lotusflare", "Ericsson and LotusFlare Announce"), "company")]))

# ---------------------------------------------------------------- Lovevery
LV_ED = NEWS("lovevery", "Lovevery Raises $20 Million")
L.append(cls("lovevery", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LV_ED, entry_date="2019-10-16",
             country="US", city="Boise", city_src="web_verified", focus="Consumer & Marketplaces",
             note="Montessori-inspired play kits for young children (Boise). Maveron led the $20M Series B of October 2019 "
                  "and 'GV (formerly Google Ventures), Reach Capital, the Chan Zuckerberg Initiative and Collaborative "
                  "Fund participated' (EdSurge); about $6M came before it (the 2018 Form D) and no source ties GV to that "
                  "money (Idaho Statesman headline: the 2019 round brought money from Google and Zuckerberg funds), so "
                  "the entry is Growth. The $100M round of October 2021 led by TCG valued it at $800M (Wikipedia; WSJ "
                  "headline): below_1b.",
             rounds=[rnd("2019-10-16", "Series B", 20000000, "Maveron", True, LV_ED, "press"),
                     rnd("2021-10-28", "unnamed ($800M valuation)", 100000000, "TCG", None, W("Lovevery"), "press")]))

# ---------------------------------------------------------------- Luminate (formerly Pixazza)
LUM_B = "https://techcrunch.com/2010/07/18/google-funded-pixazza-raises-12-million-for-crowdsourced-adsense-for-images/"
LUM_C = "https://techcrunch.com/2012/02/23/nokia-google-ventures-and-others-put-10-7m-in-adsense-for-images-luminate/"
LUM_Y = "https://techcrunch.com/2014/09/05/yahoo-acquires-shuts-down-luminate-an-interactive-image-platform/"
L.append(cls("luminate", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=LUM_B,
             country="US", city="Mountain View", focus="Media, Gaming & Advertising",
             note="Luminate, formerly Pixazza, 'AdSense for images' (interactive in-image ads and apps). Shasta Ventures "
                  "led the $12M Series B of July 2010 'with Series A investors August Capital, CMEA Capital and Google "
                  "Ventures also participating' (TechCrunch), so GV entered at the Series A, whose date no source read "
                  "gives (left open). Nokia Growth Partners led the $10.7M Series C of 2012 with GV following "
                  "(TechCrunch). Yahoo bought it and shut the service in September 2014 (TechCrunch). The 8VC, Sequoia "
                  "and Y Combinator 'Luminate' rows are different companies (Luminate Medical, Luminate Security).",
             rounds=[rnd(None, "Series A", None, None, True, LUM_B, "press"),
                     rnd("2010-07-18", "Series B", 12000000, "Shasta Ventures", True, LUM_B, "press"),
                     rnd("2012-02-23", "Series C", 10700000, "Nokia Growth Partners", True, LUM_C, "press")]))

# ---------------------------------------------------------------- Luminate Wireless
L.append(cls("luminate-wireless", status="unknown", rng="below_1b", stage="undetermined",
             country="US", focus="Data Infrastructure", flags=["city_unknown"],
             note="Cloud-based mobile network infrastructure for enterprises (the firm's 2016 listing; Luminate Wireless, "
                  "Inc. on LinkedIn). Status unknown: no source read gives its fate (Google News and EDGAR find nothing "
                  "under the name, and luminatewireless.com, listed through 2022, now redirects to an unrelated domain). "
                  "No round source, and no source places its office; the US country is model knowledge.",
             rounds=[]))

# ---------------------------------------------------------------- Luna Park
L.append(cls("luna-park", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
             focus="Consumer & Marketplaces", flags=["identity_unresolved", "city_unknown"],
             note="Listed by the firm as 'Luna Park' (Consumer, no partner, CMS record of 2022, first archived in 2026) "
                  "with the link lunapark.com. That domain today serves 'Quinn', a training platform for trades teams, "
                  "with nothing tying it to the name; Google News on the name returns only amusement parks, and EDGAR has "
                  "no filer by it. The company cannot be identified, so stage, band and graduation read undetermined. "
                  "The pre-filled FR is a Wikidata name match on a generic name and is left standing unverified.",
             rounds=[]))

# ---------------------------------------------------------------- Luvocracy
LUV = ("https://techcrunch.com/2014/07/29/walmartlabs-acquires-kleiner-perkins-backed-luvocracy-a-pinterest-like-"
       "marketplace-for-product-recommendations/")
L.append(cls("luvocracy", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="San Francisco", city_src="web_verified", focus="Consumer & Marketplaces",
             note="Social shopping marketplace built on trusted recommendations (San Francisco). WalmartLabs bought it in "
                  "July 2014, 'largely an acqui-hire' of 16 of its 20 staff with the service to be shut (TechCrunch), "
                  "announced as an acquisition and listed by the firm as 'Acquired by WalmartLabs, 2014': acquired (the "
                  "Postmates and Sosh reading). It had raised $11M from Kleiner Perkins, Google Ventures and others "
                  "(TechCrunch); no source names the round GV entered, so the stage is undetermined.",
             rounds=[]))

# ---------------------------------------------------------------- Luxe
LX = "https://techcrunch.com/2015/02/25/luxe-20m-redpoint-venrock/"
L.append(cls("luxe", status="acquired", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=LX,
             country="US", city="San Francisco", city_src="web_verified", focus="Consumer & Marketplaces",
             note="On-demand valet parking (San Francisco). Google Ventures was in the $5.5M seed with Redpoint, Sherpa, "
                  "Lightspeed, Foundation Capital and Data Collective, and Redpoint and Venrock co-led the $20M Series A "
                  "of February 2015 (TechCrunch), which graduates the row once the seed's date is on record: TechCrunch "
                  "says only that the service had run since October 2014. Graduation left for the graduation pass. Hertz "
                  "led a $50M Series B in 2016 (PR Newswire headline); Volvo bought Luxe in September 2017 (TechCrunch "
                  "tag page; Business Insider headline). Lightspeed, also in this seed, reads undetermined in its book.",
             rounds=[rnd(None, "Seed", 5500000, None, True, LX, "press"),
                     rnd("2015-02-25", "Series A", 20000000, "Redpoint Ventures, Venrock", None, LX, "press"),
                     rnd("2016-04-07", "Series B", 50000000, "Hertz", None,
                         NEWS("luxe", "Luxe Raises $50 Million Series B"), "company")]))

# ---------------------------------------------------------------- mabl
MB_A = "https://techcrunch.com/2018/02/21/with-10m-in-funding-mabl-brings-machine-learning-to-software-testing/"
MB_B = "https://techcrunch.com/2018/09/18/mabl-announces-20-million-series-b-to-bring-automated-qa-to-enterprise-customers/"
L.append(cls("mabl", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=MB_B, entry_date="2018-09-18",
             city="Boston", city_src="formd_address", focus="DevTools & APIs",
             note="ML-driven test automation (Boston). The $10M Series A of February 2018 came from CRV and Amplify "
                  "(TechCrunch); GV entered with the $20M Series B of September 2018, where CRV and Amplify are the "
                  "existing investors and GV's Karim Faris joins the board (TechCrunch; QA Financial headline: 'Led by "
                  "Google'). The pre-filled entry date (2020-05-08) is the Form D anchor of a later round, replaced by the "
                  "Series B date. No valuation disclosed.",
             rounds=[rnd("2018-02-21", "Series A", 10000000, None, False, MB_A, "press"),
                     rnd("2018-09-18", "Series B", 20000000, "GV", True, MB_B, "press"),
                     rnd("2020-05-08", "unnamed (Form D)", 8000001, None, None, FD("mabl", 2), "filing"),
                     rnd("2021", "unnamed (Form D)", 39999904, None, None, FD("mabl", 0), "filing")]))

# ---------------------------------------------------------------- Machinify
MF = "https://techcrunch.com/2018/10/08/machinify-raises-10-million-to-help-businesses-use-ai-to-monetize-data/"
L.append(cls("machinify", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=MF, entry_date="2018-10-08",
             country="US", city="Palo Alto", focus="Healthcare & Bio",
             note="AI for health-plan payment integrity. Battery Ventures led the $10M Series A of October 2018 'with "
                  "participation from GV and Matrix Partners' (TechCrunch); the firm's /ai list dates its investment to "
                  "2018-07, the same round. New Mountain Capital agreed to buy it in January 2025 (citybiz headline; the "
                  "firm's exit line 'Acquired by New Mountain Capital, 2025'). City aligned with Battery's row.",
             rounds=[rnd("2018-10-08", "Series A", 10000000, "Battery Ventures", True, MF, "press")]))

# ---------------------------------------------------------------- Magenta Therapeutics
MG = NEWS("magenta-therapeutics", "Magenta agrees to reverse merger with Dianthus")
L.append(cls("magenta-therapeutics", status="acquired", rng="below_1b", city="Cambridge", city_src="web_verified",
             focus="Healthcare & Bio",
             flags=["model_disputes_source"],
             extra={"valuation_source": None, "valuation_range_source": None, "valuation_asof": None,
                    "valuation_citation": None, "valuation_confidence": None},
             note="Stem-cell transplant conditioning (principal offices at 50 Hampshire Street, Cambridge, per its 2018 "
                  "S-1). Disputes the pre-filled public status and float: after halting its lead trial and laying off "
                  "most staff, Magenta merged with the private Dianthus Therapeutics in 2023, Dianthus holders taking "
                  "about 79% and the combined company trading as Dianthus (Nasdaq: DNTH) under Dianthus's CEO (BioPharma "
                  "Dive). The listing on this CIK is now Dianthus's, so the $599.4M float belongs to the successor: "
                  "acquired with a successor note, the General Catalyst OvaScience precedent."))

jl.write("j7", L)
