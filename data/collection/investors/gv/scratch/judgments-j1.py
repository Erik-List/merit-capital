"""PRO-75 grind, judge j1: queue batch 1 (44 member rows; ahana was the pilot).
Pattern copied from judgments-pilot.py. Every citation below was printed by a tool run in this session (the
TechCrunch/Crunchbase News WordPress search, nq.py through NEWS(), EDGAR, stockanalysis.com, the firm's own CMS
helpers) or read with WebFetch. Rows with no source tying GV to a named round read `undetermined` and keep the
rounds that were found."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
CHECK = "2026-09-28"
WV = {"valuation_range_source": "web_verified"}
# a public row turned acquired: the float the deterministic layer carried no longer describes the company
NO_FLOAT = {"valuation_source": None, "valuation_range_source": None, "valuation_asof": None,
            "valuation_confidence": None}
GRAD_LEFT = " Graduation left for the graduation pass."


def mcap(t):
    return f"https://stockanalysis.com/stocks/{t}/market-cap/"


# ---------------------------------------------------------------- 23andMe
TC_23_2009 = "https://techcrunch.com/2009/12/23/23andme-funding/"
TC_23_GOOG = "https://techcrunch.com/2009/06/18/all-in-the-family-sergey-brin-loans-23andme-10-million-and-google-ponies-up-26-million/"
TC_23_2010 = "https://techcrunch.com/2010/11/09/23andme-funding-2/"
REL_23_2012 = NEWS("23andme", "23andMe Raises More Than $50 Million")
L.append(cls("23andme", status="acquired", rng="below_1b", country="US", city="South San Francisco",
             focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=TC_23_2010,
             entry_date="2009", flags=["model_disputes_source"], extra=NO_FLOAT,
             note="Consumer genetics. Status disputes the prefilled public float: 23andMe filed for Chapter 11 on "
                  "2025-03-23 and TTAM Research Institute completed the purchase of substantially all its assets on "
                  "2025-07-14 (Wikipedia, 23andMe); the listed shell was renamed Chrome Holding Co. and deregistered "
                  "(EDGAR 15-12G, December 2025). Insolvency followed by an asset sale reads acquired with the business "
                  "continuing under TTAM (decisions D8). The Sequoia row still reads public at the 2024-09-30 float; "
                  "this row holds the fresher cited evidence. Entry: Google Ventures was already an existing investor "
                  "at the November 2010 Series C led by J&J Development Corporation (TechCrunch) and at the December "
                  "2012 Series D (the company's release). GV was formed in 2009, after the 2007 Series A that Google "
                  "itself bought (D2: not a GV position), so its first round was the 2009 Series B ($27.8M, of which "
                  "TechCrunch reported $2.6M 'from Google' in June 2009); a Series B reads Growth. City follows the "
                  "Sequoia row (South San Francisco, Oyster Point) as the last operating headquarters.",
             rounds=[rnd("2009-12-23", "Series B", 27800000, None, None, TC_23_2009, "press"),
                     rnd("2010-11-09", "Series C", 22000000, "Johnson & Johnson Development Corporation", True,
                         TC_23_2010, "press"),
                     rnd("2012-12-11", "Series D", 50000000, None, True, REL_23_2012, "company")]))

# ---------------------------------------------------------------- About.me
ABOUT_2013 = "https://techcrunch.com/2013/02/05/tony-conrads-about-me-spins-back-out-from-aol-after-raising-5-7m-capital-led-by-true-ventures/"
ABOUT_2014 = "https://techcrunch.com/2014/06/10/about-me-raises-11m-to-rival-facebook-for-simple-online-identity/"
ABOUT_ACQ = NEWS("about-me", "About.me acquired by mobile-first")
L.append(cls("about-me", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=ABOUT_2013, entry_date="2013-02",
             note="Personal profile pages. AOL bought About.me in 2010 and spun it back out in February 2013 with "
                  "$5.7M led by True Ventures, Google Ventures among the investors (TechCrunch, 2013-02-05). "
                  "TechCrunch's June 2014 report calls the $11M Foundry-led round the Series B and 'its second since "
                  "getting spun out', which names the 2013 round the Series A. Acquired by Broadly in February 2019 "
                  "(TechCrunch; the firm's own exit line).",
             rounds=[rnd("2013-02-05", "unnamed (spin-out financing; the next round is named Series B)", 5700000,
                         "True Ventures", True, ABOUT_2013, "press"),
                     rnd("2014-06-10", "Series B", 11000000, "Foundry Group", None, ABOUT_2014, "press"),
                     rnd("2019-02-21", "acquisition by Broadly", None, None, None, ABOUT_ACQ, "press")]))

# ---------------------------------------------------------------- Abacus (expense management, YC W14)
ABACUS_ACQ = "https://techcrunch.com/2018/07/17/certify-acquires-real-time-expense-management-startup-and-yc-alum-abacus/"
L.append(cls("abacus", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Fintech & Payments", stage="undetermined", flags=["model_disputes_source"],
             note="Real-time expense management (YC W14), acquired by Certify in July 2018 (TechCrunch; the firm's own "
                  "exit line). Country disputes the Wikidata DE claim: that match is a different Abacus; this one is "
                  "US (New York, as the YC row places it). No source read names the round GV entered (its partner M.G. "
                  "Siegler is on the firm's 2014-2015 pages), so the stage is undetermined. The Menlo row named Abacus "
                  "is a different company (a 2025 tax-document startup), a name collision; the YC row is this company "
                  "and still reads private, which the Certify acquisition overrides.",
             rounds=[rnd("2018-07-17", "acquisition by Certify", None, None, None, ABACUS_ACQ, "press")]))

# ---------------------------------------------------------------- Acalvio
ACALVIO_TC = "https://techcrunch.com/2016/07/26/acalvio-emerges-from-stealth-with-17m-to-bring-its-deception-based-cybersecurity-system-to-market/"
ACALVIO_PR = "https://www.prnewswire.com/news-releases/acalvio-technologies-secures-investment-from-gv-300356815.html"
L.append(cls("acalvio", status="private", rng="below_1b", country="US", city="Santa Clara", focus="Security",
             stage="Growth", stage_src="model", stage_conf="medium", stage_cite=ACALVIO_PR, entry_date="2016-11",
             note="Deception-based threat detection (Santa Clara). Accel led the Series A (September 2015) and "
                  "Ignition the Series B (June 2016), $17M combined, with no GV (TechCrunch, 2016-07-26). GV invested "
                  "in November 2016, bringing total funding to $22M (the company's release, 2016-11-03); an unnamed "
                  "investment after a Series B reads Growth.",
             rounds=[rnd("2015-09", "Series A", None, "Accel", False, ACALVIO_TC, "press"),
                     rnd("2016-06", "Series B", None, "Ignition Partners", False, ACALVIO_TC, "press"),
                     rnd("2016-11-03", "unnamed (GV investment; total raised $22M)", None, None, True, ACALVIO_PR,
                         "company")]))

# ---------------------------------------------------------------- Accent Therapeutics
ACCENT_B = "https://accenttx.com/news-events/accent-therapeutics-announces-dollar63-million-series-b-financing-to-advance-novel-precision-cancer-therapies-targeting-rna-modifying-proteins/"
ACCENT_C = "https://www.prnewswire.com/news-releases/accent-therapeutics-announces-75-million-series-c-financing-to-advance-small-molecule-precision-cancer-therapies-302041338.html"
L.append(cls("accent-therapeutics", status="private", rng="below_1b", country="US", city="Lexington",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=ACCENT_B, entry_date="2020-04",
             note="Oncology small molecules targeting RNA-modifying proteins (Lexington, MA). GV joined as a new "
                  "investor in the $63M Series B led by EcoR1 Capital (the company's release, 2020-04-23) and is "
                  "listed among the existing investors in the $75M Series C led by Mirae Asset (2024-01-23). Still "
                  "operating (2026 releases); no priced mark near $1B.",
             rounds=[rnd("2020-04-23", "Series B", 63000000, "EcoR1 Capital", True, ACCENT_B, "company"),
                     rnd("2024-01-23", "Series C", 75000000, "Mirae Asset Capital Life Science", True, ACCENT_C,
                         "company")]))

# ---------------------------------------------------------------- Adagio Therapeutics (now Invivyd)
ADAGIO_S1 = FTS("Adagio", "S-1")
L.append(cls("adagio-therapeutics", rng="below_1b", usd=280020000, val_src="web_verified", val_cite=mcap("ivvd"),
             asof=CHECK, country="US", city="New Haven", city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ADAGIO_S1,
             entry_date="2020-07", extra=WV,
             note="COVID antibodies; renamed Invivyd (NASDAQ: IVVD), whose EDGAR business address is New Haven, CT. "
                  "The S-1's related-party tables show entities affiliated with GV buying Series A preferred in July "
                  "2020 ($5.5M of the $49.9M), then Series B ($20M) and Series C ($7.5M). Market cap $280.02M on "
                  "2026-09-28 (stockanalysis.com), which replaces the 2025-06-30 float.",
             rounds=[rnd("2020-07", "Series A", 49900000, None, True, ADAGIO_S1, "filing"),
                     rnd("2020-10", "Series B", 80000000, None, True, ADAGIO_S1, "filing"),
                     rnd("2021-04", "Series C", 335500000, None, True, ADAGIO_S1, "filing")]))

# ---------------------------------------------------------------- Adapter
ADAPTER = "https://www.upstartsmedia.com/p/deep-dive-adapter-launches-ai-cognition"
L.append(cls("adapter", status="private", rng="below_1b", country="US", city="Austin", city_src="web_verified",
             focus="DevTools & APIs", stage="undetermined", entry_date="2026-07",
             extra={**WV, "valuation_citation": ADAPTER},
             note="A 'cognition API' (persistent memory and knowledge graph for AI agents), founded November 2022 by "
                  "Adam Ghetti and David Bader, based in Austin; it launched from stealth in July 2026 having raised "
                  "$17.8M to date from GV, Bond Partners, Hillspire and others (Upstarts, 2026-07-14). The report "
                  "names no round, so the stage is undetermined; the entry date is the firm's own first Invested "
                  "month (2026-07, decisions D7). Momentum slice check 2026-09-28: no priced round at or near $1B "
                  "on the record; $17.8M raised in total and no valuation disclosed.",
             rounds=[rnd("2026-07-14", "unnamed (cumulative $17.8M to date)", 17800000, None, True, ADAPTER,
                         "press")]))

# ---------------------------------------------------------------- Adelphic Mobile
ADEL_SEED = "https://techcrunch.com/2012/03/13/adelphic-launch/"
ADEL_A = "https://techcrunch.com/2012/12/04/adelphic-google-ventures/"
ADEL_ACQ = "https://techcrunch.com/2017/01/23/vint-acquires-adelphic/"
L.append(cls("adelphic-mobile", status="acquired", rng="below_1b", country="US", city="Boston",
             focus="Media, Gaming & Advertising", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ADEL_A, entry_date="2012-12",
             note="Mobile ad targeting (Boston). Matrix Partners led the $2M seed (TechCrunch, 2012-03-13); Google "
                  "Ventures led the $10M Series A (TechCrunch, 2012-12-04). Acquired by Time Inc.'s Viant in January "
                  "2017 (TechCrunch; the firm's own exit line).",
             rounds=[rnd("2012-03-13", "Seed", 2000000, "Matrix Partners", False, ADEL_SEED, "press"),
                     rnd("2012-12-04", "Series A", 10000000, "Google Ventures", True, ADEL_A, "press"),
                     rnd("2017-01-23", "acquisition by Viant", None, None, None, ADEL_ACQ, "press")]))

# ---------------------------------------------------------------- Adimab (stage prefilled from the Form D band)
L.append(cls("adimab", status="private", rng="below_1b", city="Lebanon", focus="Healthcare & Bio",
             note="Antibody discovery platform in Lebanon, NH (the Form D address). Still operating in 2026 "
                  "(partner GSK's depemokimab approvals, April 2026 release); no priced round or listing at $1B on "
                  "the record. The stage stays the prefilled Form D band."))

# ---------------------------------------------------------------- Aera Therapeutics
AERA = "https://aeratx.com/aera-therapeutics-launches-with-193-million-in-financing-to-enable-and-advance-the-next-generation-of-transformative-genetic-medicines/"
L.append(cls("aera-therapeutics", status="private", rng="below_1b", country="US", city="Cambridge",
             city_src="web_verified", focus="Healthcare & Bio", stage="Series A", stage_src="model",
             stage_conf="medium", stage_cite=AERA, entry_date="2023-02",
             note="Protein nanoparticle delivery for genetic medicines (Feng Zhang). The company's launch release "
                  "(2023-02-16) says it raised '$193 million in combined Series A and B financings led by ARCH Venture "
                  "Partners, GV and Lux Capital'; the firm's own post says the financing was co-led by GV. The release "
                  "does not split the two rounds, so the Series A is read at medium confidence. City: the company's "
                  "site gives Cambridge, MA (read 2026-09-28); the Lux row's Boston follows the release's dateline.",
             rounds=[rnd("2023-02-16", "Series A and Series B (combined)", 193000000,
                         "ARCH Venture Partners, GV, Lux Capital", True, AERA, "company")]))

# ---------------------------------------------------------------- Affinia Therapeutics
AFFINIA_S1 = FTS("Affinia", "S-1")
L.append(cls("affinia-therapeutics", status="private", rng="below_1b", country="US", city="Waltham",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=AFFINIA_S1, entry_date="2021-04",
             note="Rationally designed AAV gene therapies (Waltham, MA). The S-1 lists GV among the investors in the "
                  "$110M Series B of April 2021; the Series A tranches went to the existing Series A investors, and GV "
                  "is named only in the B. The 2022 IPO was not completed; the company announced a Series C in "
                  "October 2025. No mark at $1B.",
             rounds=[rnd("2021-04", "Series B", 110000000, None, True, AFFINIA_S1, "filing")]))

# ---------------------------------------------------------------- Again (Copenhagen)
AGAIN_SEED = "https://techcrunch.com/2023/11/30/again-bios-bacteria-eats-exhaust-and-spits-vinegar-for-the-climate/"
AGAIN_A = NEWS("again", "Cleantech Startup Again Raises $43 Million")
L.append(cls("again", status="private", rng="below_1b", country="DK", country_src="web_verified",
             country_cite=AGAIN_SEED, city="Copenhagen", city_src="web_verified", focus="Climate & Energy",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=AGAIN_SEED, entry_date="2023-02",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=AGAIN_A,
             note="Gas fermentation turning industrial CO2 into chemicals, spun out of DTU and based in Copenhagen. "
                  "It raised a $10M seed in February 2023 from ACME Capital, GV and Atlantic Labs (TechCrunch, "
                  "2023-11-30), then a $43M Series A co-led by HV Capital and GV (ESG Today, 2024-07-18). No mark at "
                  "$1B.",
             rounds=[rnd("2023-02", "Seed", 10000000, None, True, AGAIN_SEED, "press"),
                     rnd("2024-07-18", "Series A", 43000000, "HV Capital, GV", True, AGAIN_A, "press")]))

# ---------------------------------------------------------------- Agtonomy
AGT_SEED = "https://techcrunch.com/2022/01/18/toyota-ventures-agtonomy-tractors-autonomous-vehicles/"
AGT_A = NEWS("agtonomy", "Agtonomy adds $10M to Series A")
L.append(cls("agtonomy", status="private", rng="below_1b", country="US", city="South San Francisco",
             city_src="web_verified", focus="Industrial & Robotics", stage="Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=AGT_SEED, entry_date="2021-09",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=AGT_A,
             note="Autonomy and tele-assist for farm tractors (South San Francisco). It came out of stealth in "
                  "September 2021 with a $4M seed from Grit Ventures, GV and Village Global, then took a $5M seed "
                  "extension (TechCrunch, 2022-01-18). The Series A closed at $32.8M in October 2024, led by Autotech "
                  "Ventures (The Robot Report), which graduates the seed.",
             rounds=[rnd("2021-09", "Seed", 4000000, None, True, AGT_SEED, "press"),
                     rnd("2022-01-18", "Seed extension", 5000000, None, None, AGT_SEED, "press"),
                     rnd("2024-10", "Series A", 32800000, "Autotech Ventures", None, AGT_A, "press")]))

# ---------------------------------------------------------------- Air Protein
AIRP_A = NEWS("air-protein", "Air Protein raises $32m Series A to make")
L.append(cls("air-protein", status="private", rng="below_1b", country="US", city="Pleasanton",
             city_src="web_verified", focus="Climate & Energy", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=AIRP_A, entry_date="2021-01",
             note="Protein made from CO2 by microbes (Pleasanton, CA). The $32M Series A was led by ADM Ventures, "
                  "Barclays and GV (AgFunderNews, 2021-01-07), GV's first appearance on the firm's list the same "
                  "year. No later priced round or mark on the record.",
             rounds=[rnd("2021-01-07", "Series A", 32000000, "ADM Ventures, Barclays, GV", True, AIRP_A, "press")]))

# ---------------------------------------------------------------- Airtime
AIRTIME_TC = "https://techcrunch.com/2012/03/25/sean-parker-and-shawn-fanning-open-new-social-video-startup-airtime-for-business/"
L.append(cls("airtime", status="defunct", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite=AIRTIME_TC, entry_date="2011",
             note="Sean Parker and Shawn Fanning's group video app. Its first round, $8.3M from Founders Fund, Accel, "
                  "Andreessen Horowitz, Google Ventures, SV Angel and others (TechCrunch, 2012-03-25), preceded the "
                  "$25M second round led by Kleiner Perkins (Wikipedia, Airtime.com); a 2011 first round of that size "
                  "is the Series A, as both sibling rows read it. Status aligned with the a16z and Sequoia rows "
                  "(wound down after its relaunches). City follows the a16z row (New York, where the relaunched app "
                  "was run); the Sequoia row says San Francisco, the 2012 base.",
             rounds=[rnd("2011", "unnamed first round (Series A)", 8300000, None, True, AIRTIME_TC, "press"),
                     rnd("2012", "second round", 25000000, "Kleiner Perkins", None, W("Airtime.com"), "press")]))

# ---------------------------------------------------------------- Alector (public)
ALECTOR_EX = FTS("Alector", "S-1")
L.append(cls("alector", rng="below_1b", usd=214380000, val_src="web_verified", val_cite=mcap("alec"), asof=CHECK,
             country="US", city="South San Francisco", city_src="web_verified", focus="Healthcare & Bio",
             stage="undetermined", extra=WV,
             note="Neurodegeneration immunology (NASDAQ: ALEC), EDGAR business address South San Francisco. GV 2014, "
                  "L.P. and GV 2017, L.P. signed the Series E registration rights agreement filed with the S-1, and "
                  "the S-1 lists GV among its investors, but no source read ties GV to the round it entered (the "
                  "firm has listed Alector since 2015), so the stage is undetermined. Market cap $214.38M on "
                  "2026-09-28 (stockanalysis.com), replacing the 2025-06-30 float.",
             rounds=[rnd("2018", "Series E", None, None, True, ALECTOR_EX, "filing")]))

# ---------------------------------------------------------------- 99 Counties
FORMD_99 = "https://www.sec.gov/Archives/edgar/data/1913861/000191386122000001/0001913861-22-000001-index.htm"
L.append(cls("99-counties", status="private", rng="below_1b", country="US", country_src="formd_address",
             city="Keystone", city_src="formd_address", focus="Consumer & Marketplaces", stage="undetermined",
             note="Regenerative-farm meat sold direct to consumers from Iowa, Wisconsin and Minnesota farms; the site "
                  "still sells (read 2026-09-28). 99 Counties, Inc. (incorporated 2021) filed one Form D, first sale "
                  "2022-02-08, $3.72M sold, from Keystone, IA, with no GV person among the related persons. No source "
                  "read ties GV to a round (Andy Wheeler is on the firm's 2022 people page), so the stage is "
                  "undetermined.",
             rounds=[rnd("2022-02-08", "unnamed (Form D, $3.72M sold)", 3724999, None, None, FORMD_99, "filing")]))

# ---------------------------------------------------------------- Aledade
ALEDADE_B1 = NEWS("aledade", "Aledade raises $20M in recent round")
ALEDADE_F = "https://news.crunchbase.com/venture/biggest-funding-rounds-aledade-kobold/"
L.append(cls("aledade", status="private", rng="1b_plus", usd=3500000000, val_src="web_verified", val_cite=ALEDADE_F,
             asof="2023-06", country="US", city="Bethesda", focus="Healthcare & Bio", stage="Growth",
             stage_src="web_verified", stage_conf="high", stage_cite=ALEDADE_B1, entry_date="2017-01",
             flags=["stale"], extra=WV,
             note="Accountable-care network for independent primary care practices (Bethesda, MD). GV joined as a new "
                  "investor in the $20M Series B1 led by Biomatics Capital (Healthcare Dive, 2017-01-10) and returned "
                  "in the $64M Series C (Crunchbase News, 2020-04-20). Mark: the $260M Series F led by Lightspeed, "
                  "which 'values the company at $3.5 billion, Bloomberg reported' (Crunchbase News, 2023-06-23), the "
                  "same mark as the IVP and Lightspeed rows; older than 24 months, so stale. The December 2025 $500M "
                  "was a credit facility, not a priced round.",
             rounds=[rnd("2017-01-10", "Series B1", 20000000, "Biomatics Capital", True, ALEDADE_B1, "press"),
                     rnd("2020-04-20", "Series C", 64000000, "OMERS Growth Equity", True,
                         "https://news.crunchbase.com/venture/health-tech-startup-aledade-raises-64m-series-c-with-an-eye-toward-profitability/",
                         "press"),
                     rnd("2023-06-21", "Series F", 260000000, "Lightspeed Venture Partners", None, ALEDADE_F,
                         "press")]))

# ---------------------------------------------------------------- Alethea
ALETHEA_PR = "https://www.prnewswire.com/news-releases/alethea-sees-more-than-3x-growth-in-2024-following-20m-series-b-funding-round-302291491.html"
L.append(cls("alethea", status="private", rng="below_1b", country="US", city="Washington", city_src="web_verified",
             focus="Security", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ALETHEA_PR,
             entry_date="2023-11", extra={**WV, "valuation_citation": ALETHEA_PR},
             note="AI detection of disinformation and narrative attacks (dateline Washington and New York). Its $20M "
                  "Series B was led by GV with Ballistic Ventures, closed late 2023 (the company's release, "
                  "2024-10-30); the firm's own first Invested month, 2023-11, dates it (decisions D7). Momentum slice "
                  "check 2026-09-28: no priced round at or near $1B on the record; the Series B is the last round "
                  "found and no valuation was disclosed.",
             rounds=[rnd("2023-11", "Series B", 20000000, "GV", True, ALETHEA_PR, "company")]))

# ---------------------------------------------------------------- Alkira
ALKIRA_B = "https://siliconangle.com/2020/10/13/multicloud-networking-startup-alkira-raises-54m-series-b-round/"
ALKIRA_C = "https://techcrunch.com/2024/05/15/alkira-connects-with-100m-for-a-solution-that-connects-your-clouds/"
ALKIRA_ACQ = NEWS("alkira", "Lumen Completes Alkira Acquisition to Expand AI-Ready")
L.append(cls("alkira", status="acquired", rng="below_1b", country="US", city="San Jose",
             focus="Data Infrastructure", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=ALKIRA_B, entry_date="2020-10",
             note="Multi-cloud network as a service (San Jose). It came out of stealth with about $30M from Sequoia "
                  "and Kleiner Perkins in April 2020; Koch Disruptive Technologies led the $54M Series B in October "
                  "2020 'plus a new investor, GV Management Co.' (SiliconANGLE, 2020-10-13); Tiger Global led the "
                  "$100M Series C (TechCrunch, 2024-05-15). Lumen Technologies completed its acquisition on "
                  "2026-07-07 (citybiz; press reports put the price at $475M). The Sequoia row still reads private; "
                  "this row holds the fresher cited evidence.",
             rounds=[rnd("2020-04", "stealth launch round", 30000000, None, False, ALKIRA_B, "press"),
                     rnd("2020-10-13", "Series B", 54000000, "Koch Disruptive Technologies", True, ALKIRA_B, "press"),
                     rnd("2024-05-15", "Series C", 100000000, "Tiger Global Management", None, ALKIRA_C, "press"),
                     rnd("2026-07-07", "acquisition by Lumen Technologies", None, None, None, ALKIRA_ACQ, "press")]))

# ---------------------------------------------------------------- Allara Health
ALLARA_POST = POST("allara-bridging")
ALLARA_B = "https://www.prnewswire.com/news-releases/allara-health-raises-26-million-in-series-b-funding-to-revolutionize-womens-hormonal-healthcare-302359719.html"
L.append(cls("allara-health", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="Healthcare & Bio", stage="Series A", stage_src="first_party", stage_conf="high",
             stage_cite=ALLARA_POST, entry_date="2023-10",
             note="Virtual care for women's chronic hormonal conditions (New York). The firm's own post of 2023-10-18 "
                  "reveals 'our latest investment' and says the company is 'announcing $10 million in Series A "
                  "funding led by GV'. Index Ventures led the $26M Series B with 'existing investor GV' (the company's "
                  "release, 2025-01-24, dateline New York).",
             rounds=[rnd("2023-10-18", "Series A", 10000000, "GV", True, ALLARA_POST, "firm"),
                     rnd("2025-01-24", "Series B", 26000000, "Index Ventures", True, ALLARA_B, "company")]))

# ---------------------------------------------------------------- Altana AI
ALTANA_SEED = "https://techcrunch.com/2020/11/24/altana-raises-7m-to-protect-supply-chains-from-disruptions-child-labor/"
ALTANA_A = NEWS("altana-ai", "Altana AI Raises $15M to Bring")
ALTANA_A2 = NEWS("altana-ai", "Altana AI Raises $15m Series A Investment")
ALTANA_C = "https://news.crunchbase.com/venture/supply-chain-startup-unicorn-altana/"
L.append(cls("altana-ai", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=ALTANA_C,
             asof="2024-07-29", city="New York", focus="AI & Applied AI", stage="Series A",
             stage_src="web_verified", stage_conf="high", stage_cite=ALTANA_A, entry_date="2021-05",
             flags=["stale"], extra=WV,
             note="AI supply-chain and trade intelligence (New York; the Form D address is Brooklyn). After a $7M "
                  "seed (TechCrunch, 2020-11-24), GV led the $15M Series A (AlleyWatch; Amadeus Capital says the round "
                  "closed in May 2021, the firm's own first Invested month). Mark: the $200M Series C led by the US "
                  "Innovative Technology Fund 'values the company at $1 billion', GV an existing investor (Crunchbase "
                  "News, 2024-07-29), exactly at the band edge; older than 24 months, so stale. Momentum slice check "
                  "2026-09-28: no later priced round found (July 2026 news covers Altana buying Cervo).",
             rounds=[rnd("2020-11-24", "Seed", 7000000, None, None, ALTANA_SEED, "press"),
                     rnd("2021-05", "Series A", 15000000, "GV", True, ALTANA_A2, "press"),
                     rnd("2024-07-29", "Series C", 200000000, "US Innovative Technology Fund", True, ALTANA_C,
                         "press")]))

# ---------------------------------------------------------------- AltspaceVR
ALT_POST = POST("back-to-virtual-reality")
ALT_2015A = "https://techcrunch.com/2015/06/12/vr-chat/"
ALT_2015B = "https://techcrunch.com/2015/07/29/pay-per-virtual-reality/"
L.append(cls("altspacevr", city="Redwood City", rng="below_1b", focus="Media, Gaming & Advertising", stage="Seed",
             stage_src="first_party", stage_conf="high", stage_cite=ALT_POST,
             note="Social VR platform, acquired by Microsoft in October 2017 and shut in March 2023 (Wikipedia, "
                  "AltspaceVR). The firm's own post (2022-10-03) calls it 'an early GV seed investment'. By June 2015 "
                  "it had 'absorbed $5.2 million' from investors including Google Ventures (TechCrunch, 2015-06-12), "
                  "then raised an unnamed $10.3M round led by Comcast Ventures (TechCrunch, 2015-07-29). No source read "
                  "dates the seed, so no entry date is given; the $10.3M round falls just short of twice the $5.2M "
                  "and carries no round name, so it does not decide the column. City follows the Lux row." + GRAD_LEFT,
             rounds=[rnd(None, "Seed", 5200000, None, True, ALT_2015A, "press"),
                     rnd("2015-07-29", "unnamed", 10300000, "Comcast Ventures", None, ALT_2015B, "press")]))

# ---------------------------------------------------------------- Ambition
AMBITION_TC = "https://techcrunch.com/2014/02/21/ambition-launch/"
L.append(cls("ambition", status="private", rng="below_1b", country="US", city="Chattanooga", city_src="web_verified",
             focus="SaaS", stage="undetermined", flags=["model_disputes_source"],
             note="Sales-team performance and gamification software (YC W14), founded in Chattanooga, TN (TechCrunch, "
                  "2014-02-21). Country disputes the Wikidata MA claim, a name-match on a one-word name. Its seed came "
                  "from The Lamp Post Group, Y Combinator and YC VC, without GV (TechCrunch); the firm lists Ambition "
                  "from 2016, and no source read names the round GV entered, so the stage is undetermined. A Series B "
                  "from Primus Capital was reported in October 2021 (Business Journals headline).",
             rounds=[rnd("2014-02", "Seed", None, None, False, AMBITION_TC, "press")]))

# ---------------------------------------------------------------- AMP Robotics (stage prefilled from the Form D band)
L.append(cls("amp-robotics", status="private", rng="below_1b", city="Louisville", focus="Industrial & Robotics",
             note="AI sorting robots for recycling, Louisville, Colorado (as the Sequoia row places it). GV joined the "
                  "$55M round with XN and Valor in January 2021 (Business Wire headline); later rounds include the $91M "
                  "Series C (November 2022); no priced round or reported valuation at $1B on the record."))

# ---------------------------------------------------------------- Anchor (podcasting)
ANCHOR_SEED = "https://techcrunch.com/2017/03/07/backed-with-2-8-million-anchors-digital-radio-revolution-gets-new-tools/"
ANCHOR_A = "https://techcrunch.com/2017/09/28/anchor-raises-10-million-for-podcast-platform/"
ANCHOR_ACQ = "https://techcrunch.com/2019/02/06/spotify-doubles-down-on-podcasts/"
L.append(cls("anchor", status="acquired", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="Media, Gaming & Advertising", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ANCHOR_A, entry_date="2017-09", flags=["model_disputes_source"],
             note="Podcast creation and hosting (New York). Country disputes the Wikidata GB claim: Anchor was a New "
                  "York company. Accel led a $2.8M round in March 2017; GV led the $10M Series A (TechCrunch, "
                  "2017-09-28, 'The New York-based team is announcing $10 million in Series A funding, led by GV'). "
                  "Spotify acquired Anchor in February 2019 (TechCrunch). The YC row named Anchor is a different "
                  "company (a Lagos banking API), a name collision.",
             rounds=[rnd("2017-03-07", "unnamed", 2800000, "Accel", None, ANCHOR_SEED, "press"),
                     rnd("2017-09-28", "Series A", 10000000, "GV", True, ANCHOR_A, "press"),
                     rnd("2019-02-06", "acquisition by Spotify", None, None, None, ANCHOR_ACQ, "press")]))

# ---------------------------------------------------------------- Andela
ANDELA_B = NEWS("andela", "Priscilla Chan fund - Techpoint")
ANDELA_C = "https://techcrunch.com/2017/10/10/andela-a-tech-training-and-development-outsourcer-for-african-coders-raises-40m/"
ANDELA_E = NEWS("andela", "Andela becomes a unicorn after SoftBank")
L.append(cls("andela", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified", val_cite=ANDELA_E,
             asof="2021-09-29", country="US", city="New York", focus="Consumer & Marketplaces", stage="Growth",
             stage_src="web_verified", stage_conf="high", stage_cite=ANDELA_B, entry_date="2016-06",
             flags=["stale", "model_disputes_source"], clear=["unicorn_name_match"], extra=WV,
             note="Global engineering talent marketplace, founded in Lagos, headquartered in New York (as the Spark row "
                  "places it). Country disputes the Wikidata LV claim, a name-match. Spark led the $10M Series A "
                  "(2015); the Chan Zuckerberg Initiative led the $24M Series B, and 'Venture firm GV also joined the "
                  "round, alongside existing investors' (Techpoint Africa, June 2016), so GV entered at the B; GV "
                  "returned in the $40M Series C (TechCrunch, 2017-10-10). Mark: the September 2021 Series E led by "
                  "SoftBank 'values the company at $1.5 billion' (Rest of World, 2021-09-29), which replaces the "
                  "unicorn-list source with a cited one and settles the name match; older than 24 months, so stale. Same mark as the Spark row.",
             rounds=[rnd("2015-06-25", "Series A", 10000000, "Spark Capital", False, W("Andela"), "press"),
                     rnd("2016-06", "Series B", 24000000, "Chan Zuckerberg Initiative", True, ANDELA_B, "press"),
                     rnd("2017-10-10", "Series C", 40000000, None, True, ANDELA_C, "press"),
                     rnd("2019-01", "Series D", 100000000, "Generation Investment Management", None, W("Andela"),
                         "press"),
                     rnd("2021-09-29", "Series E", 200000000, "SoftBank", None, ANDELA_E, "press")]))

# ---------------------------------------------------------------- AngelList
ANGEL_2013 = "https://techcrunch.com/2013/09/23/angellist/"
ANGEL_2022 = "https://techcrunch.com/2022/03/12/angellist-tiger-global-money/"
L.append(cls("angellist", status="private", rng="1b_plus", usd=4100000000, val_src="web_verified", val_cite=ANGEL_2022,
             asof="2022-03", country="US", city="San Francisco", focus="Fintech & Payments", stage="Series A",
             stage_src="model", stage_conf="medium", stage_cite=ANGEL_2013, entry_date="2013-09",
             flags=["stale"], extra=WV,
             note="Startup fundraising and fund-administration platform. Google Ventures co-led, with Atlas Venture, "
                  "the $24M round of September 2013 at about $150M (TechCrunch, 2013-09-23; the round was first "
                  "reported nine months earlier). The record names the March 2022 $100M round led by Tiger Global the "
                  "Series B (Wikipedia, AngelList), which makes the 2013 round the Series A (medium confidence). Mark: "
                  "that 2022 round 'valued the business at $4.1 billion' (TechCrunch, 2022-03-12, AngelList Venture, "
                  "the fundraising business the firm's listing describes); older than 24 months, so stale.",
             rounds=[rnd("2013-09-23", "unnamed (the next named round is the Series B)", 24000000,
                         "Google Ventures, Atlas Venture", True, ANGEL_2013, "press"),
                     rnd("2022-03", "Series B", 100000000, "Tiger Global", None, ANGEL_2022, "press")]))

# ---------------------------------------------------------------- Ankyra Therapeutics
ANKYRA_B = "https://ankyratx.com/press-releases/ankyra-therapeutics-announces-45-million-series-b-financing-and-appoints-howard-l-kaufman-m-d-as-chief-medical-officer/"
L.append(cls("ankyra-therapeutics", status="private", rng="below_1b", country="US", city="Cambridge",
             city_src="web_verified", focus="Healthcare & Bio", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=ANKYRA_B, entry_date="2021-11",
             note="Anchored cytokine immunotherapy for cancer (the company's site gives 245 Main St, Cambridge, MA). "
                  "GV was among the new investors in the $45M Series B, alongside existing investors Polaris Partners "
                  "and Mithril Capital (the company's release, 2021-11-12). Still reporting clinical data in 2026; no "
                  "mark near $1B.",
             rounds=[rnd("2021-11-12", "Series B", 45000000, None, True, ANKYRA_B, "company")]))

# ---------------------------------------------------------------- Anomali (formerly ThreatStream)
THREAT_A = "https://techcrunch.com/2014/02/20/threatstream-raises-4m-from-google-ventures-to-add-realtime-cybersecurity-intelligence/"
THREAT_B = "https://techcrunch.com/2014/12/04/threatstream-grabs-22m-to-help-fight-cybersecurity-threats/"
L.append(cls("anomali", status="private", rng="below_1b", city="Redwood City", focus="Security",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=THREAT_A, entry_date="2014-02",
             flags=["stage_disputes_band"],
             note="Threat intelligence platform (Redwood City), founded 2013 as ThreatStream. Stage disputes the "
                  "prefilled Form D band (Growth on the 2018 filing): ThreatStream 'raised $4 million in Series A "
                  "funding from investors led by Google Ventures' (TechCrunch, 2014-02-20), and General Catalyst led "
                  "the $22M Series B in December 2014 (TechCrunch). The 2018 filing is a later round Karim Faris sat "
                  "on as a director. Still private; its rounds price it well under $1B (about $96M raised by 2018 per "
                  "Wikipedia).",
             rounds=[rnd("2014-02-20", "Series A", 4000000, "Google Ventures", True, THREAT_A, "press"),
                     rnd("2014-12-04", "Series B", 22000000, "General Catalyst", None, THREAT_B, "press")]))

# ---------------------------------------------------------------- Antiva Biosciences
ANTIVA_D = "https://www.antivabio.com/news/2021/110221.php"
ANTIVA_E = "https://www.antivabio.com/news/2023/042723.php"
L.append(cls("antiva-biosciences", status="private", rng="below_1b", country="US", city="South San Francisco",
             city_src="web_verified", focus="Healthcare & Bio", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=ANTIVA_D, entry_date="2021-11",
             note="Topical therapies for HPV lesions (South San Francisco). The $31M Series D was led by Adjuvant "
                  "Capital 'and joined by GV, formerly Google Ventures', a new investor (the company's release, "
                  "2021-11-02); GV is an existing investor in the $53M Series E led by MPM-BioImpact (2023-04-27). "
                  "Reporting clinical data in 2026; no mark near $1B.",
             rounds=[rnd("2021-11-02", "Series D", 31000000, "Adjuvant Capital", True, ANTIVA_D, "company"),
                     rnd("2023-04-27", "Series E", 53000000, "MPM-BioImpact Capital", True, ANTIVA_E, "company")]))

# ---------------------------------------------------------------- Apptentive
APPT_SEED = "https://techcrunch.com/2012/12/10/apptentive/"
APPT_A = "https://techcrunch.com/2014/09/25/surveymonkey-makes-its-first-investment-leads-apptentives-5-3m-series-a/"
L.append(cls("apptentive", status="acquired", rng="below_1b", country="US", city="Seattle", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=APPT_SEED, entry_date="2012-12",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=APPT_A,
             note="In-app customer feedback for mobile apps (Seattle). It raised $1.2M 'in seed funding from Founder's "
                  "Co-Op, Google Ventures, Social Leverage, Golden Venture Partners' (TechCrunch, 2012-12-10), then a "
                  "$5.3M Series A led in part by SurveyMonkey (TechCrunch, 2014-09-25), which graduates the seed. "
                  "Acquired by Alchemer in 2023 (the firm's own exit line).",
             rounds=[rnd("2012-12-10", "Seed", 1200000, None, True, APPT_SEED, "press"),
                     rnd("2014-09-25", "Series A", 5300000, "SurveyMonkey", None, APPT_A, "press")]))

# ---------------------------------------------------------------- Apptimize
APTZ_SEED = "https://techcrunch.com/2014/01/22/apptimize-seed-funding-visual-editor/"
APTZ_A = "https://techcrunch.com/2015/02/17/apptimize-series-a/"
APTZ_ACQ = "https://techcrunch.com/2019/08/27/airship-acquires-apptimize/"
L.append(cls("apptimize", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=APTZ_SEED, entry_date="2014-01",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=APTZ_A,
             note="Mobile A/B testing (YC S13, San Francisco). Its $2.1M seed named Merus Capital, Google Ventures, "
                  "Oliver Jung and an AngelList syndicate as the biggest investors (TechCrunch, 2014-01-22); a $4M "
                  "Series A followed (TechCrunch, 2015-02-17), which graduates the seed, as the a16z row records. "
                  "Acquired by Airship in August 2019 (TechCrunch).",
             rounds=[rnd("2014-01-22", "Seed", 2100000, None, True, APTZ_SEED, "press"),
                     rnd("2015-02-17", "Series A", 4000000, None, None, APTZ_A, "press"),
                     rnd("2019-08-27", "acquisition by Airship", None, None, None, APTZ_ACQ, "press")]))

# ---------------------------------------------------------------- Appurify
APPUR_A = "https://techcrunch.com/2013/05/28/appurify-raises-4-5m-series-a-to-automate-mobile-app-testing-on-a-wide-range-of-devices/"
APPUR_VB = NEWS("appurify", "Google acquires Appurify, an app testing")
APPUR_ACQ = "https://techcrunch.com/2014/06/25/google-appurify/"
L.append(cls("appurify", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="DevTools & APIs", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=APPUR_VB, entry_date="2013-05",
             note="Automated mobile app testing on real devices (San Francisco). TechCrunch names the $4.5M round of "
                  "May 2013 a Series A (2013-05-28) and VentureBeat says Appurify 'raised $4.5 million from Google "
                  "Ventures last year' (June 2014); no source read places GV in the 2012 seed the Felicis row enters "
                  "at, so the entry is the Series A (medium confidence). Google acquired Appurify in June 2014 "
                  "(TechCrunch).",
             rounds=[rnd("2013-05-28", "Series A", 4500000, None, True, APPUR_A, "press"),
                     rnd("2014-06-25", "acquisition by Google", None, None, None, APPUR_ACQ, "press")]))

# ---------------------------------------------------------------- Apteligent (formerly Crittercism)
CRIT_B = "https://techcrunch.com/2013/03/12/crittercism-lands-12m-from-google-ventures-more-to-help-mobile-developers-monitor-app-network-performance/"
CRIT_C = "https://techcrunch.com/2014/04/09/crittercism-accenture-30m/"
L.append(cls("apteligent", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="DevTools & APIs", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CRIT_B,
             entry_date="2013-03",
             note="Mobile app performance monitoring, formerly Crittercism (San Francisco, Wikipedia). Crittercism "
                  "raised $12M in Series B financing 'led by Google Ventures, with contributions from existing "
                  "investors, Shasta Ventures and Opus Capital' (TechCrunch, 2013-03-12), so GV entered at the B; a "
                  "$30M round with Accenture followed in April 2014. Acquired by VMware in 2017 (the firm's own exit "
                  "line; SiliconANGLE headline, May 2017).",
             rounds=[rnd("2013-03-12", "Series B", 12000000, "Google Ventures", True, CRIT_B, "press"),
                     rnd("2014-04-09", "unnamed", 30000000, None, None, CRIT_C, "press")]))

# ---------------------------------------------------------------- Arcus Biosciences (public)
ARCUS_S1 = FTS("Arcus Biosciences", "S-1")
L.append(cls("arcus-biosciences", rng="1b_plus", usd=3180000000, val_src="web_verified", val_cite=mcap("rcus"),
             asof=CHECK, country="US", city="Hayward", city_src="web_verified", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ARCUS_S1, entry_date="2016-08",
             flags=["model_disputes_source"], extra=WV,
             note="Immuno-oncology (NYSE: RCUS; EDGAR business address Hayward, CA). Band disputes the prefilled "
                  "float: the market cap is $3.18B on 2026-09-28 (stockanalysis.com), against a $565.9M float of "
                  "2025-06-30. The S-1's certain-transactions tables show GV 2016, L.P. buying $25M of the August 2016 "
                  "Series B and GV 2017, L.P. buying Series C in November 2017; GV holds no Series A.",
             rounds=[rnd("2015-05", "Series A", 49725000, None, False, ARCUS_S1, "filing"),
                     rnd("2016-08", "Series B", 69999993, None, True, ARCUS_S1, "filing"),
                     rnd("2017-11", "Series C", None, None, True, ARCUS_S1, "filing")]))

# ---------------------------------------------------------------- Areteia Therapeutics
ARETEIA_A = NEWS("areteia-therapeutics", "Knopp Biosciences and Population Health Partners Create")
ARETEIA_A2 = NEWS("areteia-therapeutics", "Additional $75MM in Series A")
L.append(cls("areteia-therapeutics", status="defunct", rng="below_1b", country="US", city="Chapel Hill",
             city_src="web_verified", focus="Healthcare & Bio", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=ARETEIA_A, entry_date="2022-07",
             note="Oral dexpramipexole for eosinophilic asthma, created by Knopp Biosciences and Population Health "
                  "Partners. A syndicate 'led by Bain Capital Life Sciences with participation from Access "
                  "Biotechnology, GV, ARCH Venture Partners' and others committed up to $350M in Series A financing "
                  "(Bain Capital release, 2022-07-12); an additional $75M of Series A followed in February 2024. The "
                  "company's own site (read 2026-09-28) describes it as 'formerly based in Chapel Hill, NC' and 'no "
                  "longer operating', so it reads defunct at its last headquarters.",
             rounds=[rnd("2022-07-12", "Series A", 350000000, "Bain Capital Life Sciences", True, ARETEIA_A, "press"),
                     rnd("2024-02-13", "Series A (additional)", 75000000, None, None, ARETEIA_A2, "press")]))

# ---------------------------------------------------------------- Armadin
ARMADIN_PR = "https://www.prnewswire.com/news-releases/armadin-secures-record-breaking-189-9m-in-seed-and-series-a-funding-to-combat-the-era-of-ai-driven-hyperattacks-302709318.html"
ARMADIN_TC = "https://techcrunch.com/2026/03/10/mandiants-founder-just-raised-190m-for-his-autonomous-ai-agent-security-startup/"
L.append(cls("armadin", status="private", rng="below_1b", city="San Francisco", city_src="web_verified",
             focus="Security", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=ARMADIN_PR,
             entry_date="2026-03", extra={**WV, "valuation_citation": ARMADIN_TC},
             note="Autonomous AI offensive-security agents, founded by Kevin Mandia (dateline San Francisco). It "
                  "announced $189.9M 'in Seed and Series A funding', 'Led by Accel, with participation from Google "
                  "Ventures, Kleiner Perkins, Menlo Ventures, In-Q-Tel, and follow-on investment from 8VC and "
                  "Ballistic Ventures' (the company's release, 2026-03-10). The follow-on wording marks 8VC and "
                  "Ballistic as the seed's investors, so GV and the other new names read as Series A investors "
                  "(medium confidence), as the Accel and Menlo rows read their own entries. City follows the release "
                  "and the Menlo row; the Accel row says Menlo Park. Momentum slice check 2026-09-28: no priced round "
                  "at or near $1B on the record; the company is not disclosing its valuation (TechCrunch, "
                  "2026-03-10).",
             rounds=[rnd("2026-03-10", "Seed and Series A (combined)", 189900000, "Accel", True, ARMADIN_PR,
                         "company")]))

# ---------------------------------------------------------------- ARMO BioSciences
ARMO_S1 = FTS("ARMO BioSciences", "S-1")
ARMO_LILLY = "https://investor.lilly.com/news-releases/news-release-details/lilly-announces-agreement-acquire-armo-biosciences"
L.append(cls("armo-biosciences", status="acquired", rng="below_1b", country="US", city="Redwood City",
             city_src="web_verified", focus="Healthcare & Bio", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=ARMO_S1, entry_date="2015-11",
             note="Immuno-oncology (pegilodecakin), Redwood City per its S-1. The S-1's certain-transactions tables "
                  "show GV 2014, L.P. buying 2,860,194 shares of the Series C sold in closings of November 2015 and "
                  "February 2016 ($7.5M of $49.5M), and GV holds no earlier series. IPO January 2018 (NASDAQ: ARMO); "
                  "Eli Lilly agreed to acquire it in May 2018 for about $1.6B (Lilly's release, linked from the firm's "
                  "own listing; the firm's exit line 'Acquired by Eli Lilly, 2018').",
             rounds=[rnd("2014-05", "Series B", 30000000, None, False, ARMO_S1, "filing"),
                     rnd("2015-11", "Series C", 49542620, None, True, ARMO_S1, "filing"),
                     rnd("2017-08", "Series C-1", 67637153, None, None, ARMO_S1, "filing"),
                     rnd("2018-05", "acquisition by Eli Lilly", None, None, None, ARMO_LILLY, "company")]))

# ---------------------------------------------------------------- Arrakis Therapeutics
ARRAKIS_A = "https://arrakistx.com/press-release/arrakis-therapeutics-announces-38-million-series-a-financing-to-target-rna-with-small-molecule-medicines-and-names-michael-gilman-chairman-and-ceo/"
ARRAKIS_B = "https://arrakistx.com/press-release/arrakis-therapeutics-announces-75-million-series-b-financing-to-advance-a-new-class-of-small-molecule-medicines-targeting-rna/"
L.append(cls("arrakis", status="private", rng="below_1b", country="US", city="Waltham", city_src="web_verified",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=ARRAKIS_B, entry_date="2019-04",
             note="Small molecules that target RNA (Waltham, MA). Canaan Partners led the $38M Series A without GV "
                  "(2017-02-27); venBio and Nextech co-led the $75M Series B 'with participation by new investors "
                  "Omega Funds, HBM Healthcare Investments, GV (formerly Google Ventures)' and others (the company's "
                  "release, 2019-04-18). Still operating (CEO change June 2026); no mark near $1B. The Accel row named "
                  "Arrakis is a different company (a London AI-agent startup), a name collision.",
             rounds=[rnd("2017-02-27", "Series A", 38000000, "Canaan Partners", False, ARRAKIS_A, "company"),
                     rnd("2019-04-18", "Series B", 75000000, "venBio Partners, Nextech Invest", True, ARRAKIS_B,
                         "company")]))

# ---------------------------------------------------------------- Arsanis (merged into X4 Pharmaceuticals)
ARSANIS_JOIN = FTS("Arsanis", "DRS")
ARSANIS_S1 = "https://www.sec.gov/Archives/edgar/data/1501697/000119312517315505/d427310ds1.htm"
L.append(cls("arsanis", status="acquired", rng="below_1b", country="US", city="Waltham", city_src="web_verified",
             focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=ARSANIS_JOIN, entry_date="2017-04", flags=["model_disputes_source"], extra=NO_FLOAT,
             note="Antibodies against infectious disease, Waltham, MA per its S-1. Status disputes the prefilled "
                  "public float: Arsanis merged with privately held X4 Pharmaceuticals in 2019 and its listed entity "
                  "(CIK 1501697) now carries the name X4 Pharmaceuticals (EDGAR lists Arsanis, Inc. as its former "
                  "name); the firm's own line reads 'Acquired by X4 Pharmaceuticals, 2019'. Successor-entity "
                  "ambiguity reads acquired with a successor note; the float belongs to X4's business. Entry: GV 2016, "
                  "L.P. signed the investors' rights joinder dated 2017-04-24, the month of the Series D financing, "
                  "and holds 1,540,499 shares from preferred (S-1); the S-1's 5%-holder tables do not list GV among "
                  "the Series D buyers, so the Series D reads at medium confidence.",
             rounds=[rnd("2015-05", "Series B (second closing)", 7000001, None, False, ARSANIS_S1, "filing"),
                     rnd("2016-04", "Series C", 5499979, None, False, ARSANIS_S1, "filing"),
                     rnd("2017-04", "Series D", 35053178, None, True, ARSANIS_JOIN, "filing")]))

# ---------------------------------------------------------------- Artifact (family story interviews)
L.append(cls("artifact", status="defunct", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Recorded family-story interviews (heyartifact.com). The company's own site (read 2026-09-28) "
                  "announces 'Artifact is shutting down', no longer sells new Artifacts and hosts completed interviews "
                  "through 2024, so it reads defunct. City from the site's 415 (San Francisco) phone number. The firm "
                  "lists it from 2023 (M.G. Siegler); no source read names a round, so the stage is undetermined. "
                  "The a16z row named Artifact is a different company (a speedrun fintech in New York), a name "
                  "collision.",
             rounds=[]))

# ---------------------------------------------------------------- Aspen Neuroscience
ASPEN_B = NEWS("aspen-neuroscience", "Aspen Neuroscience Announces $147.5 Million Series B")
L.append(cls("aspen-neuroscience", status="private", rng="below_1b", country="US", city="San Diego",
             city_src="web_verified", focus="Healthcare & Bio", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=ASPEN_B, entry_date="2022-05",
             note="Autologous cell therapy for Parkinson's (San Diego, per the company's site). The $147.5M Series B "
                  "was 'Led by GV, LYFE Capital and Revelation Partners' (the company's release, 2022-05-09); the firm "
                  "lists Aspen from 2022. A $115M Series C followed in November 2025 (Fierce Biotech and Endpoints, "
                  "linked from the company's site). No mark near $1B.",
             rounds=[rnd("2022-05-09", "Series B", 147500000, "GV, LYFE Capital, Revelation Partners", True, ASPEN_B,
                         "company"),
                     rnd("2025-11-20", "Series C", 115000000, None, None, "https://aspenneuroscience.com", "company")]))

# ---------------------------------------------------------------- Arda Therapeutics (stage prefilled from the Form D band)
ARDA_SEED = "https://www.sec.gov/Archives/edgar/data/1903317/000190331722000001/0001903317-22-000001-index.htm"
ARDA_A = NEWS("arda-therapeutics", "Arda Therapeutics Secures $43M Series A")
L.append(cls("arda-therapeutics", status="private", rng="below_1b", city="San Carlos", city_src="web_verified",
             focus="Healthcare & Bio", stage="undetermined", flags=["stage_disputes_band"],
             extra={"entry_stage_source": None, "entry_stage_confidence": None, "entry_date": None},
             note="Targeted cell depletion for chronic disease (San Carlos, per the company's site). Stage disputes "
                  "the prefilled Form D band (Growth on the $43.3M filing of 2024-09-16): that filing is the round the "
                  "company named its $43M Series A (Business Wire, 2024-10-09), and the band's anchor, director "
                  "Vineeta Agarwala, last appears on GV's pages in 2019 and signs as Andreessen Horowitz's partner "
                  "(T4: the seat is not GV's). The seed Form D (first sale 2021-12-17, $7.5M sold) lists only the CEO; "
                  "a16z says it 'first invested in Arda at the Seed' and led the Series A. GV is named in the Series A "
                  "release, but its body could not be read (Business Wire, Morningstar and Endpoints refused), so "
                  "whether GV entered at the seed or the Series A is not established: undetermined. No mark near $1B.",
             rounds=[rnd("2021-12-17", "Seed", 7499998, None, None, ARDA_SEED, "filing"),
                     rnd("2024-10-09", "Series A", 43000000, "Andreessen Horowitz", None, ARDA_A, "company")]))

jl.write("j1", L)
