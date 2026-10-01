"""PRO-99 Kleiner Perkins, judge j02, queue batch 4 (fisker-automotive .. inspirato), plus enphase-energy from batch 3
(missed in j02a): classification of listed members. Run with NQ_TAG=j02. No membership items in this batch."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, POST, W

WV = "web_verified"
VRS = {"valuation_range_source": WV}
SA = "https://stockanalysis.com/stocks/{}/market-cap/"
ASOF = "2026-09-30"
FLOCK_VAL = "https://www.flocksafety.com/blog/flock-safety-secures-major-funding"
FS_VAL = ("https://www.prnewswire.com/news-releases/fullstory-secures-100-million-investment-at-1-8-billion-valuation-"
          "to-accelerate-global-growth-301347970.html")
FS_FORMD_2015 = "https://www.sec.gov/Archives/edgar/data/1614167/000161416715000002/0001614167-15-000002-index.htm"
GLEAN_VAL = ("https://www.businesswire.com/news/home/20250610090029/en/Glean-Raises-$150M-Series-F-at-$7.2B-Valuation-"
             "to-Accelerate-Enterprise-AI-Agent-Innovation-Globally")
GUSTO_A = ("https://techcrunch.com/2014/02/19/cloud-based-payroll-app-zenpayroll-raises-20m-from-general-catalyst-and-"
           "kleiner-at-a-100m-plus-valuation/")
GUSTO_VAL = "https://fortune.com/2025/06/09/gusto-200-million-plus-tender-offer"
HIPPO_VAL = ("https://www.businesswire.com/news/home/20251103432446/en/Hippocratic-AI-Raises-$126-Million-in-Series-C-at-"
             "$3.5-Billion-Valuation-Led-by-Avenir-Growth-to-Expand-Clinically-Safe-Generative-AI-Agents-Across-Healthcare")
IMPRINT_VAL = ("https://www.businesswire.com/news/home/20251217961518/en/Imprint-Raises-$150-Million-Series-D-to-Transform-"
               "Co-Brand-Cards-into-a-True-Loyalty-Platform")
INCORTA_B = ("https://techcrunch.com/2017/09/19/real-time-data-analytics-startup-incorta-raises-15m-series-b-led-by-"
             "kleiner-perkins/")
INDIEGOGO_B = "https://www.ivp.com/content/ivp-adds-crowdfunding-leader-indiegogo-to-its-portfolio/"
INFINITUS_A = ("https://techcrunch.com/2021/02/04/infinitus-emerges-from-stealth-with-21m-for-voice-rpa-aimed-at-"
               "healthcare-companies/")
INKITT_A = ("https://techcrunch.com/2019/08/28/inkitt-raises-16m-led-by-kleiner-perkins-to-publish-crowdsourced-novels-"
            "in-mini-episodes/")
GL = "Graduation left for the graduation pass."

L = []

# ---- batch 3 row missed in j02a
L.append(cls("enphase-energy", city="Fremont", usd=4360000000, rng="1b_plus", val_src=WV, val_cite=SA.format("enph"),
             asof=ASOF, extra=VRS, focus="Climate & Energy",
             note="Solar microinverters and home batteries, headquartered in Fremont, California (Wikipedia). Market cap "
                  "$4.36B on 2026-09-30 (stockanalysis.com) replaces the older figure; same band."))

# ---- batch 4
L.append(cls("fisker-automotive", status="acquired", rng="below_1b", city="Anaheim", focus="Climate & Energy",
             note="Plug-in hybrid carmaker (Fisker Karma), Anaheim. It filed for Chapter 11 in November 2013 and Wanxiang "
                  "bought its assets at auction in February 2014, relaunching them as Karma Automotive (Wikipedia): an "
                  "asset sale out of insolvency, so acquired with Karma as successor, aligned with the NEA row."))

L.append(cls("five-prime-therapeutics", city="South San Francisco", city_src="formd_address", rng="below_1b",
             stage="undetermined", flags=["stage_disputes_band"], focus="Healthcare & Bio",
             rounds=[rnd("2010-08-03", "Unnamed round (Form D)", 7499999, None, None, None, "filing")],
             note="Protein therapeutics, South San Francisco; Amgen bought it in 2021. The 2013 S-1's principal-stockholders "
                  "table shows the stake held by Kleiner Perkins Caufield & Byers IX-A, IX-B, X-A and X-B, 1999-2001 vintage "
                  "funds, in a company incorporated in December 2001, so the firm entered years before the 2010 Form D the "
                  "band read as a Seed; no source read names that first round, so the stage is undetermined and no "
                  "graduation applies."))

L.append(cls("flexus-biosciences", status="acquired", rng="below_1b", city="San Carlos", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Immuno-oncology biotech, San Carlos (EDGAR address); Bristol-Myers Squibb acquired it in 2015, as the "
                  "firm's exit field says."))

L.append(cls("flipagram", status="acquired", rng="below_1b", country="US", city="Los Angeles", stage="undetermined",
             entry_date="2010", focus="Consumer & Marketplaces",
             rounds=[rnd("2015", "Series A", 70000000, "Sequoia Capital", None, None, "press"),
                     rnd("2017", "Acquisition by ByteDance (Toutiao)", None, None, None, None, "press")],
             note="Short-form video slideshow app, Los Angeles; ByteDance acquired it in 2017 (the firm's exit field and "
                  "the Sequoia row). The firm's since-year 2010 predates the app, and no source read names the round "
                  "Kleiner Perkins entered, so the stage is undetermined."))

L.append(cls("flipboard", status="private", rng="below_1b", city="Palo Alto", focus="Media, Gaming & Advertising",
             note="News aggregator based in Palo Alto (Wikipedia; EDGAR address). JPMorgan put in $50M in July 2015 and a "
                  "$25M round followed in 2022 (Form D); no priced round at $1B or more is on record, aligned with the "
                  "Coatue and Insight rows."))

L.append(cls("flock-safety", status="private", usd=7500000000, rng="1b_plus", val_src=WV, val_cite=FLOCK_VAL,
             asof="2025-03", extra=VRS, country="US", city="Atlanta", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2023", focus="Security",
             rounds=[rnd("2022-02-15", "Series E", 150000000, "Tiger Global", None, None, "company"),
                     rnd("2025-03", "Unnamed round", 275000000, "Andreessen Horowitz", None, FLOCK_VAL, "company")],
             note="Licence-plate cameras and public-safety software, Atlanta. The firm's since-year 2023 is after the "
                  "$150M Series E of February 2022, so any entry then was a late round or secondary: Growth, model at "
                  "medium since no page names the firm's transaction. Mark: $275M led by a16z at $7.5B in March 2025 (the "
                  "company's post), aligned with the Coatue, Spark, Tiger and YC rows."))

L.append(cls("flx-bio", city="South San Francisco", city_src="formd_address", rng="below_1b", focus="Healthcare & Bio",
             note="FLX Bio, renamed RAPT Therapeutics (same EDGAR registrant), South San Francisco; listed in 2019 and "
                  "delisted on 2026-03-03 after GSK's roughly $2.2B acquisition (stockanalysis.com): acquired, no "
                  "standalone figure."))

L.append(cls("fortify-software", status="acquired", rng="below_1b", city="San Mateo", stage="undetermined",
             entry_date="2003", focus="Security",
             note="Static code-analysis security software; Hewlett-Packard acquired it in 2010. Wikipedia says Kleiner "
                  "Perkins founded it in 2003, but no source read names the founding round, so the stage is undetermined. "
                  "San Mateo was its base when HP bought it (the 2008 listing gave Palo Alto)."))

L.append(cls("foundation-medicine", city="Boston", rng="below_1b", focus="Healthcare & Bio",
             note="Cancer genomic profiling; Roche bought the rest of it in 2018, and in 2024 it moved its headquarters from "
                  "Cambridge to Boston's Seaport (Wikipedia), aligned with the GV row."))

L.append(cls("fullstory", status="private", usd=1800000000, rng="1b_plus", val_src=WV, val_cite=FS_VAL,
             asof="2021-08-04", extra=VRS, city="Atlanta", stage="Series A", stage_src="formd_structural",
             stage_cite=FS_FORMD_2015, stage_conf="medium", entry_date="2015-05-04", flags=["stale"], focus="SaaS",
             rounds=[rnd("2014-09", "Seed (Form D)", 1500000, None, None, None, "filing"),
                     rnd("2015-05-04", "Series A", 10697854, None, True, FS_FORMD_2015, "filing"),
                     rnd("2017-05-04", "Series B", 15000000, None, None, None, "filing"),
                     rnd("2021-08-04", "Series D", 103000000, "Permira", None, FS_VAL, "company")],
             note="Digital-experience analytics, Atlanta. Ted Schlein is a director on the $10.7M Form D of May 2015, the "
                  "company's second filing after a $1.5M 2014 round, which Hypepotamus (as cited in the GV row) names the "
                  "$10M Series A; the firm's since-year is 2015: Series A entry. Mark: the $103M Series D at $1.8B "
                  "(company release, 2021-08-04), stale, aligned with GV."))

L.append(cls("future", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             stage="undetermined", focus="Consumer & Marketplaces",
             rounds=[rnd("2020-09-01", "Unnamed round (Form D)", 23813688, None, True, jl.FORMD_CITE("future"), "filing")],
             note="Remote personal-training app (Future Research, Inc.), San Francisco (EDGAR address). The firm's post "
                  "'Welcome Future' (2019-05-23) names no round, and the only filing naming a partner is the $23.8M round "
                  "of 2020 with Mamoon Hamid as director, a later round; the stage is undetermined."))

L.append(cls("genentech", city="South San Francisco", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("genentech"), stage_conf="high", entry_date="1976", focus="Healthcare & Bio",
             rounds=[rnd("1976", "Seed", None, "Kleiner Perkins", True, SITE("genentech"), "firm")],
             note="Biotech pioneer, South San Francisco; Roche took full control in 2009. The firm's own company page says "
                  "Kleiner Perkins would provide seed capital at formation in 1976: Seed entry. " + GL))

L.append(cls("general-radar", status="private", rng="below_1b", country="US", city="Belmont", city_src=WV,
             stage="undetermined", entry_date="2016", focus="Industrial & Robotics",
             rounds=[rnd("2022-06", "Series A", 22000000, None, None, "https://www.genrad.com/", "company")],
             note="Digital pulse-compression radar (General Radar Corp.), Belmont, California, founded 2016 and "
                  "operating (the company's site). Its Series A of $22M came in June 2022, after the firm's 2016 entry, "
                  "whose round no source names, so the stage is undetermined."))

L.append(cls("genomic-health", city="Redwood City", rng="below_1b", stage="undetermined", entry_date="2001",
             focus="Healthcare & Bio",
             note="Cancer genomic tests, Redwood City; merged into Exact Sciences in 2019. Brook Byers joined the board in "
                  "January 2001 and KPCB X funds are 5% holders in the 2005 S-1, but no source read names the series "
                  "they bought, so the stage is undetermined."))

L.append(cls("glean", status="private", usd=7200000000, rng="1b_plus", val_src=WV, val_cite=GLEAN_VAL,
             asof="2025-06-10", extra=VRS, country="US", city="Palo Alto", stage="Series A", stage_src="first_party",
             stage_cite=SITE("glean"), stage_conf="high", entry_date="2019", focus="AI & Applied AI",
             rounds=[rnd("2019", "Series A", None, "Kleiner Perkins", True, SITE("glean"), "firm"),
                     rnd("2021-03", "Series B", 40000000, "General Catalyst", None, None, "press"),
                     rnd("2024-02-27", "Series D", 200000000, "Kleiner Perkins, Lightspeed", True,
                         POST("glean-series-d"), "firm"),
                     rnd("2025-06-10", "Series F", 150000000, "Wellington", None, GLEAN_VAL, "company")],
             note="Enterprise AI search, Palo Alto. The firm's company page says it made the investment on the spot, "
                  "incubated the team in its office, and backed Glean 'from Series A through Series D': Series A entry "
                  "in 2019. Mark: the $150M Series F at $7.2B (2025-06-10), aligned with the six sibling rows."))

L.append(cls("glori-energy", country="US", city="Houston", rng="below_1b", stage="Series A", stage_src=WV,
             stage_cite=jl.FTS("Glori Energy", "S-1"), stage_conf="high", entry_date="2008",
             focus="Climate & Energy",
             rounds=[rnd("2008", "Series A", 4000000, None, True, jl.FTS("Glori Energy", "S-1"), "filing"),
                     rnd("2009-10", "Series B", None, None, None, jl.FTS("Glori Energy", "S-1"), "filing")],
             note="Microbial enhanced oil recovery, Houston (the S-1's principal office). The 2011 S-1 shows KPCB Holdings "
                  "buying $4M of the series A preferred sold between November 2006 and September 2008, with a KPCB "
                  "designee elected by the series A holders: Series A entry, dated to the end of that window."))

L.append(cls("gogii", status="private", rng="below_1b", city="Los Angeles", focus="Media, Gaming & Advertising",
             note="GOGII, renamed textPlus (free texting and calling app); textPlus, Inc. still runs the service (its site, "
                  "2026). Los Angeles per the 2009 listing (the later filings give Marina del Rey). No sale or priced "
                  "round near $1B found."))

L.append(cls("good-technology", city="Santa Clara", rng="below_1b", stage="undetermined", entry_date="2000",
             focus="Security",
             note="The original Good Technology (founded 2000 as SpringThings, Santa Clara per the firm's listing), which "
                  "Motorola bought in 2007, the acquirer the firm names. Visto bought it from Motorola in 2009 and took "
                  "the name (Wikipedia); the NEA row is Visto, a different company, so its Sunnyvale city and the 2015 "
                  "BlackBerry sale are not aligned here. No source names the firm's 2000 round."))

L.append(cls("google", status="public", usd=4210000000000, rng="100b_plus", val_src=WV, val_cite=SA.format("googl"),
             asof=ASOF, extra=VRS, city="Mountain View", stage="undetermined", entry_date="1999-06",
             flags=["model_disputes_source"], focus="Media, Gaming & Advertising",
             rounds=[rnd("1999-06-07", "Unnamed round", 25000000, "Kleiner Perkins, Sequoia Capital", True, W("Google"),
                         "press")],
             note="Google, now Alphabet (public through the 2015 holding-company reorganisation, not acquired), Mountain "
                  "View. Market cap $4.21T on 2026-09-30 (stockanalysis.com), aligned in band with the Sequoia row. The "
                  "firm co-led the $25M round announced 1999-06-07 (Wikipedia; Doerr on the board from May 1999); the S-1 "
                  "shows series B preferred issued in 1999 but no page ties the firm's shares to a series, so the stage "
                  "is undetermined."))

L.append(cls("greenhouse", city="New York", rng="below_1b", stage="undetermined", flags=["stage_disputes_band"],
             focus="SaaS",
             rounds=[rnd("2013-11-14", "Seed", 2700000, "Social+Capital Partnership, Resolute Ventures", None,
                         W("Greenhouse Software"), "press"),
                     rnd("2014-08", "Series A", 7500000, "Social+Capital Partnership", None, W("Greenhouse Software"),
                         "press"),
                     rnd("2015-03", "Series B", 13600000, "Benchmark", None, W("Greenhouse Software"), "press"),
                     rnd("2015-08", "Series C", 35000000, "Thrive Capital", None, W("Greenhouse Software"), "press"),
                     rnd("2018", "Series D", 50000000, None, None, W("Greenhouse Software"), "press"),
                     rnd("2021-01", "TPG majority stake", 47000000, "TPG", None, W("Greenhouse Software"), "press")],
             note="Recruiting software, New York; TPG took a majority stake in 2021. The Form D band's Seed rests on the "
                  "2014 filing that names Mamoon Hamid as director, but that was Social+Capital's Series A (Wikipedia), "
                  "three years before he joined Kleiner Perkins, and no round on record names Kleiner Perkins, so the "
                  "stage is undetermined and no graduation applies."))

L.append(cls("gumroad", status="private", rng="below_1b", city="San Francisco", stage="Series A", stage_src=WV,
             stage_cite=W("Gumroad"), stage_conf="high", entry_date="2012-05", flags=["stage_disputes_band"],
             focus="Consumer & Marketplaces",
             rounds=[rnd("2012-02", "Seed", 1100000, None, None, W("Gumroad"), "press"),
                     rnd("2012-05", "Series A", 7000000, "Kleiner Perkins", True, W("Gumroad"), "press")],
             note="Creator commerce platform, San Francisco (Wikipedia). After a $1.1M seed in February 2012, Kleiner "
                  "Perkins led the $7M Series A three months later (Wikipedia; Mike Abbott on the Form D of 2012-05-07), "
                  "so the entry is the Series A, not a Seed, and no graduation applies."))

L.append(cls("gusto", country="US", city="San Francisco", status="private", usd=9300000000, rng="1b_plus", val_src=WV,
             val_cite=GUSTO_VAL, asof="2025-06-09", extra=VRS, stage="Series A", stage_src=WV, stage_cite=GUSTO_A,
             stage_conf="high", entry_date="2014-02", flags=["model_disputes_source"], focus="SaaS",
             rounds=[rnd("2012-12-11", "Seed", 6100000, None, None, None, "press"),
                     rnd("2014-02-19", "Series A", 20000000, "General Catalyst", True, GUSTO_A, "press"),
                     rnd("2015-04", "Unnamed round", 60000000, "Google Capital", True, None, "press"),
                     rnd("2025-06-09", "Employee tender offer", 200000000, "Teachers' Venture Growth", None, GUSTO_VAL,
                         "press")],
             note="Payroll and HR software (ZenPayroll until 2015), San Francisco; the NL country and the $10B figure were "
                  "wrong joins. The firm's since-year 2014 is the $20M Series A led by General Catalyst with Kleiner "
                  "(TechCrunch, 2014-02-19). Mark: the June 2025 employee tender at $9.3B (Fortune), aligned with the "
                  "a16z, Felicis, GV and Ribbit rows."))

L.append(cls("handshake", status="private", usd=3500000000, rng="1b_plus", val_src=WV, val_cite=W("Handshake (company)"),
             asof="2022-01", extra=VRS, country="US", city="San Francisco", stage="Series A", stage_src="first_party",
             stage_cite=POST("handshake-moving-the-needle-on-inequality"), stage_conf="high", entry_date="2016",
             flags=["stale"], focus="Consumer & Marketplaces",
             rounds=[rnd("2015", "Seed", 3500000, "True Ventures", None,
                         POST("handshake-moving-the-needle-on-inequality"), "firm"),
                     rnd("2016", "Series A", 10500000, "Kleiner Perkins", True,
                         POST("handshake-moving-the-needle-on-inequality"), "firm"),
                     rnd("2022-01", "Series F", 200000000, None, None, W("Handshake (company)"), "press")],
             note="Early-career network (joinhandshake.com), San Francisco. The firm's case study says a year after the "
                  "$3.5M seed led by True Ventures, Kleiner Perkins led Handshake's $10.5M A round: Series A entry, 2016. "
                  "Mark: the $200M Series F at $3.5B (January 2022, Wikipedia), stale, aligned with Coatue, EQT, "
                  "Lightspeed and Spark. The a16z, Greylock and Sequoia rows are the handshake.org naming protocol and "
                  "the Point Nine row the wholesale app, different companies."))

L.append(cls("handspring", city="Mountain View", rng="below_1b", stage="undetermined", entry_date="1998",
             focus="Consumer & Marketplaces",
             note="Palm-OS handheld maker founded in June 1998 by Jeff Hawkins, Donna Dubinsky and Ed Colligan "
                  "(Wikipedia), Mountain View; merged into Palm in 2003. John Doerr joined the board in 1998, but no "
                  "source read names the round, so the stage is undetermined."))

L.append(cls("hara-software", status="acquired", rng="below_1b", country="US", city="Redwood City",
             city_src="formd_address", grad="graduated", grad_src="formd", focus="Climate & Energy",
             note="Environmental and energy management software, Redwood City (EDGAR address; the 2009 listing gave "
                  "Menlo Park); the firm's archived page reads Acquired by 2014. Graduation from the Form D sequence: a "
                  "$15M round in the third quarter of 2009 after the $6M entry filing, as the Form D layer reads."))

L.append(cls("harmonic-lightwaves", country="US", city="San Jose", usd=1150000000, rng="1b_plus", val_src=WV,
             val_cite=SA.format("hlit"), asof=ASOF, extra=VRS, stage="undetermined", entry_date="1989",
             focus="Media, Gaming & Advertising",
             note="Harmonic Inc. (Harmonic Lightwaves until 1995), video delivery infrastructure, San Jose. Market cap "
                  "$1.15B on 2026-09-30 (stockanalysis.com), so the band rises from below_1b to 1b_plus. No source read "
                  "names the firm's 1989 round."))

L.append(cls("harvest", status="defunct", rng="below_1b", city="Waltham", city_src="formd_address",
             focus="Climate & Energy",
             note="Harvest Power, organics recycling, Waltham, Massachusetts; initially funded by Kleiner Perkins and Waste "
                  "Management. Its last operation (Orlando) ceased in August 2020 and the company was dissolved in April "
                  "2021 (Wikipedia); individual facilities were sold, but the business ended: defunct."))

L.append(cls("harvey", city="San Francisco", focus="AI & Applied AI",
             note="Legal AI platform, San Francisco, as the a16z, Coatue, GV and Sequoia rows carry."))

L.append(cls("heartport", status="acquired", rng="below_1b", country="US", city="Redwood City", stage="undetermined",
             entry_date="1992", focus="Healthcare & Bio",
             note="Minimally invasive heart surgery systems, Redwood City; Johnson & Johnson acquired it in 2001 (the 2001 "
                  "8-K voting agreement signed by Kleiner Perkins Caufield & Byers VI). Joe Lacob sat on the board from "
                  "April 1992, but no source read names the round, so the stage is undetermined."))

L.append(cls("helix", status="private", rng="below_1b", city="San Mateo", focus="Healthcare & Bio",
             note="Helix, population genomics formed in 2015 by Illumina with Warburg Pincus and Sutter Hill (Noah Knauf of "
                  "the Digital Growth Fund on the $185M formation filing), San Mateo, aligned with the Sutter Hill row. "
                  "Still private; the 2021 $50M round disclosed no valuation. The GV row (HELIX RE) and the unresolved "
                  "a16z row are different companies."))

L.append(cls("hippocratic-ai", status="private", usd=3500000000, rng="1b_plus", val_src=WV, val_cite=HIPPO_VAL,
             asof="2025-11", extra=VRS, country="US", city="Palo Alto", stage="Growth", stage_src="first_party",
             stage_cite=POST("hippocratic-ai-series-b"), stage_conf="high", entry_date="2025-01",
             focus="Healthcare & Bio",
             rounds=[rnd("2023-05", "Seed", 50000000, "General Catalyst, Andreessen Horowitz", None, None, "press"),
                     rnd("2024-03", "Series A", 53000000, None, None, None, "press"),
                     rnd("2025-01-09", "Series B", 141000000, "Kleiner Perkins", True, POST("hippocratic-ai-series-b"),
                         "firm"),
                     rnd("2025-11", "Series C", 126000000, "Avenir Growth", True, HIPPO_VAL, "company")],
             note="Safety-focused healthcare AI agents, Palo Alto. The firm's post of 2025-01-09 says it leads the Series "
                  "B, and its since-year is 2025, so the entry is the Series B (Growth). Momentum check 2026-09-30 (web "
                  "search): the latest priced round is the $126M Series C at $3.5B of November 2025 (Business Wire, "
                  "Kleiner Perkins participating), the mark, aligned with the a16z and General Catalyst rows."))

L.append(cls("hixme", status="acquired", rng="below_1b", city="Agoura Hills", city_src="formd_address",
             focus="Fintech & Payments",
             note="Health-benefits insurtech (Hixme Insurance Solutions), Agoura Hills per its 2016 Form D. A web check "
                  "of 2026-09-30 found it acquired by SureCo in May 2021 (vendor profile, terms undisclosed); acquired, "
                  "medium."))

L.append(cls("hollar", status="defunct", rng="below_1b", city="Commerce", focus="Consumer & Marketplaces",
             note="Online dollar store; wound down around 2020, aligned with the Lightspeed row, including its later base "
                  "in Commerce, California (the 2017 Form D gave Santa Monica)."))

L.append(cls("home-value-protection", status="acquired", rng="below_1b", city="San Francisco",
             city_src="formd_address", focus="Fintech & Payments",
             note="Home-price protection insurance (formerly Working Equity), San Francisco (EDGAR address). The firm's "
                  "archived page reads Acquired from 2013; the acquirer is not on record."))

L.append(cls("huntress", status="private", usd=1500000000, rng="1b_plus", val_src=WV, val_cite=W("Huntress (company)"),
             asof="2024-06", extra=VRS, city="Columbia", flags=["stale"], focus="Security",
             note="Managed cybersecurity for small businesses, Columbia, Maryland (Wikipedia; EDGAR address). Mark: the "
                  "$150M Series D of June 2024 co-led by Kleiner Perkins and Meritech raised the valuation to over $1.5B "
                  "(Wikipedia), now past 24 months; no later priced round found."))

L.append(cls("hx-diagnostics", status="unknown", rng="below_1b", country="US", city="Emeryville",
             stage="undetermined", focus="Healthcare & Bio",
             note="Rapid infectious-disease diagnostics, Emeryville per the 2008 listing (the 2009 Form D gives Danville). "
                  "The firm listed it in 2008, before its only Form D ($4.65M, 2009), so that filing is a ceiling on the "
                  "entry, not the entry, and no source names the round; nothing on record after 2009 establishes whether "
                  "it operates, was sold or closed."))

L.append(cls("hyla", status="acquired", rng="below_1b", country="US", city="Farmers Branch", stage="undetermined",
             entry_date="2011", focus="Consumer & Marketplaces",
             note="HYLA Mobile, device trade-in and buyback programs, Farmers Branch, Texas; acquired by Assurant through "
                  "its American Bankers Insurance Group unit in 2020, the acquirer the firm names. No source read names "
                  "the firm's 2011 round."))

L.append(cls("icontrol-networks", status="acquired", rng="below_1b", city="Redwood City", focus="Data Infrastructure",
             note="Connected-home platform, Redwood City (Palo Alto on its 2011 filings); Comcast acquired it in 2017, as "
                  "the firm's exit field says."))

L.append(cls("idec-pharmaceuticals", status="public", usd=33370000000, rng="10b_plus", val_src=WV,
             val_cite=SA.format("biib"), asof=ASOF, extra=VRS, country="US", city="Cambridge", stage="undetermined",
             entry_date="1986", focus="Healthcare & Bio",
             note="IDEC Pharmaceuticals merged with Biogen in 2003 as the surviving legal entity, renamed Biogen Idec and "
                  "then Biogen; Biogen Inc. still files under IDEC's EDGAR registration and is based in Cambridge, "
                  "Massachusetts, so the row is public at Biogen's market cap, $33.37B on 2026-09-30 (stockanalysis.com). "
                  "Brook Byers was IDEC's founding president, but no source names the 1986 round."))

L.append(cls("imprint", status="private", usd=1200000000, rng="1b_plus", val_src=WV, val_cite=IMPRINT_VAL,
             asof="2025-12", extra=VRS, country="US", city="New York", stage="Series A", stage_src="first_party",
             stage_cite=POST("imprint-a-modern-approach-to-rewarding-customer-loyalty"), stage_conf="high",
             entry_date="2021-11", focus="Fintech & Payments",
             rounds=[rnd("2021-11-15", "Series A", 38000000, "Kleiner Perkins", True,
                         POST("imprint-a-modern-approach-to-rewarding-customer-loyalty"), "firm"),
                     rnd("2023-11-13", "Series B", 75000000, "Ribbit Capital", True, None, "company"),
                     rnd("2025-12", "Series D", 150000000, None, None, IMPRINT_VAL, "company")],
             note="Co-branded credit-card programs, New York. The firm's post of 2021-11-15 says it leads Imprint's Series "
                  "A (the site's 2023 since-year is later than the post): Series A entry. Momentum check 2026-09-30 (web "
                  "search): the $150M Series D of December 2025 at $1.2B is the latest priced round; the $2B raised since "
                  "April 2026 is debt. Aligned with the Khosla, Ribbit and Thrive rows."))

L.append(cls("incorta", status="private", rng="below_1b", city="San Mateo", stage="Growth", stage_src=WV,
             stage_cite=INCORTA_B, stage_conf="high", entry_date="2017-09", focus="Data Infrastructure",
             rounds=[rnd("2016-05", "Series A", 10000000, "GV", None, INCORTA_B, "press"),
                     rnd("2017-09-19", "Series B", 15000000, "Kleiner Perkins", True, INCORTA_B, "press")],
             note="Unified data analytics, San Mateo. TechCrunch (2017-09-19) reports the $15M Series B led by Kleiner "
                  "Perkins after GV's $10M Series A of 2016; the firm's since-year is 2017: Growth entry. No valuation "
                  "at $1B or more on record, aligned with the GV row."))

L.append(cls("indiegogo", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Growth",
             stage_src=WV, stage_cite=INDIEGOGO_B, stage_conf="high", entry_date="2014-01", focus="Consumer & Marketplaces",
             rounds=[rnd("2012-06", "Series A", 15000000, "Insight Venture Partners, Khosla Ventures", None,
                         W("Indiegogo"), "press"),
                     rnd("2014-01-28", "Series B", 40000000, "Institutional Venture Partners", True, INDIEGOGO_B, "press"),
                     rnd("2025", "Acquisition by Gamefound", None, None, None, W("Indiegogo"), "press")],
             note="Crowdfunding platform, San Francisco. IVP's post of 2014-01-28 says IVP led the $40M Series B along with "
                  "Kleiner Perkins, and the firm's since-year and Digital Growth Fund tag are 2014: Growth entry. "
                  "Gamefound acquired Indiegogo in 2025 (Wikipedia; the firm's exit field)."))

L.append(cls("infinitus", status="private", rng="below_1b", country="US", city="San Francisco", stage="Series A",
             stage_src=WV, stage_cite=INFINITUS_A, stage_conf="high", entry_date="2021-02",
             flags=["model_disputes_source"], focus="Healthcare & Bio",
             rounds=[rnd("2021-02-04", "Series A", 21400000, "Kleiner Perkins, Coatue", True, INFINITUS_A, "press"),
                     rnd("2021-11-10", "Series B", 30000000, "GV", True, None, "company"),
                     rnd("2024-10", "Series C", 51500000, "Andreessen Horowitz", None, None, "company")],
             note="Voice AI for healthcare phone calls (Infinitus Systems), San Francisco; the prefilled CN was a one-word "
                  "Wikidata join to a Chinese health-products group. TechCrunch (2021-02-04) reports the $21.4M Series A "
                  "co-led by Kleiner Perkins and Coatue, announced as the company left stealth (the firm's since-year "
                  "2019 is likely the close). No priced round at $1B or more, aligned with a16z, Coatue and GV."))

L.append(cls("inkitt", status="private", rng="below_1b", country="US", city="San Francisco", stage="Series A",
             stage_src=WV, stage_cite=INKITT_A, stage_conf="high", entry_date="2019-08", focus="Media, Gaming & Advertising",
             rounds=[rnd("2019-08-28", "Series A", 16000000, "Kleiner Perkins", True, INKITT_A, "press"),
                     rnd("2021-10", "Series B", 59000000, "New Enterprise Associates", None, None, "press")],
             note="Reader-driven fiction publishing (Galatea). TechCrunch (2019-08-28) reports the $16M Series A led by "
                  "Kleiner Perkins, the firm's since-year 2019. TechCrunch then called it Berlin-based; country and city "
                  "follow the HV Capital, Khosla and NEA rows (San Francisco). No priced round at $1B or more."))

L.append(cls("inspirato", city="Denver", rng="below_1b", focus="Consumer & Marketplaces",
             note="Luxury travel subscription, Denver; listed through the Thayer SPAC in 2022 and later taken private "
                  "(acquired, pre-filled), aligned with the First Round and IVP rows."))

jl.write("j02b", L)
