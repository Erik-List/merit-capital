"""PRO-99 Kleiner Perkins, judge j01, queue batch 1 (3vr .. axion): classification of listed members.
Skipped per the run notes: 3-v-biosciences, atara-bio (duplicates; atara-biotherapeutics is judged with its evidence)."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, POST, W

# URLs printed by tools run in this session (fts listing / secget / EDGAR browse, WebFetch reads, sibling rows)
S1_AMYRIS = "https://www.sec.gov/Archives/edgar/data/1365916/000119312510085595/ds1.htm"
DRS_ATARA = "https://www.sec.gov/Archives/edgar/data/1604464/000095012314003691/filename1.htm"
S1_ARMO = "https://www.sec.gov/Archives/edgar/data/1693664/000119312517383679/d269230ds1.htm"
S1_AMAZON = "https://www.sec.gov/Archives/edgar/data/1018724/0000891618-97-001309.txt"
S1_APPD = "https://www.sec.gov/Archives/edgar/data/1435043/000119312516805559/d209425ds1.htm"
S1_AEYE = "https://www.sec.gov/Archives/edgar/data/1818644/000119312521280715/d196049ds1a.htm"
F3_PROGYNY = "https://www.sec.gov/Archives/edgar/data/1551306/0001209191-19-053998.txt"
SA_AMBQ = "https://stockanalysis.com/stocks/ambq/market-cap/"
SA_AGLX = "https://stockanalysis.com/quote/osl/AGLX/market-cap/"
MC_AMBIENCE = "https://medcitynews.com/2025/07/healthcare-documentation-startup-unicorn/"
AI_SERIES_F = "https://www.appliedintuition.com/press-releases/series-f"
KP_AI_POST = "https://www.kleinerperkins.com/perspectives/applied-intuition-powering-the-next-era-of-vehicle-intelligence/"
ARSENAL_C = ("https://arsenalbio.com/2024/09/04/arsenalbio-announces-325-million-financing-to-advance-programmable-"
             "cell-therapy-programs-through-clinical-development/")
GV_ALKIRA_B = "https://siliconangle.com/2020/10/13/multicloud-networking-startup-alkira-raises-54m-series-b-round/"
TC_ALKIRA_C = "https://techcrunch.com/2024/05/15/alkira-connects-with-100m-for-a-solution-that-connects-your-clouds/"
CB_ALKIRA = ("https://www.citybiz.co/article/870607/lumen-completes-alkira-acquisition-to-expand-ai-ready-network-"
             "platform/")
GL = "Graduation left for the graduation pass."

L = []

# ---- 3VR
L.append(cls("3vr", status="acquired", rng="below_1b", city="San Francisco", stage="undetermined",
             entry_date="2005", focus="Security",
             rounds=[rnd("2009-08", "unnamed (Form D)", 12166720, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1350856/000135085609000004/0001350856-09-000004-index.htm",
                         "filing")],
             note="Video analytics for physical security, San Francisco; Identiv bought it in 2018 (the firm's exit "
                  "line: acquired by Identiv). The firm's own since-year is 2005, so the 2009 Form D (Ted Schlein a "
                  "director) is a later round and the pre-filled 2009 date is replaced by 2005; no source read names "
                  "the 2005 round."))

# ---- 41st Parameter
L.append(cls("41st-parameter", status="acquired", rng="below_1b", city="Scottsdale", stage="undetermined",
             entry_date="2006", focus="Security",
             rounds=[rnd("2009-12", "unnamed (Form D)", 4115676, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1323175/000132317509000003/0001323175-09-000003-index.htm",
                         "filing"),
                     rnd("2012-04", "unnamed (Form D)", 15072796, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1323175/000132317512000001/0001323175-12-000001-index.htm",
                         "filing")],
             note="Device identification and online fraud prevention, Scottsdale (the firm's 2008-11 listing); "
                  "Experian acquired it in 2013. The firm's since-year is 2006, before the 2009 Form D, so the entry "
                  "date is 2006; the 2006 round is not named in any source read (a Google News query returned no "
                  "funding report)."))

# ---- Aerohive Networks
L.append(cls("aerohive-networks", rng="below_1b", city="Milpitas", stage="Growth", stage_src="web_verified",
             stage_cite=W("Aerohive Networks"), stage_conf="medium", entry_date="2007-07", focus="Data Infrastructure",
             rounds=[rnd("2006", "Series A", 4000000, None, None, W("Aerohive Networks"), "press"),
                     rnd("2007-07", "Series B", 20000000, "Kleiner Perkins Caufield & Byers", True,
                         W("Aerohive Networks"), "press")],
             note="Cloud-managed enterprise Wi-Fi, Milpitas. Wikipedia: a $4M Series A in 2006, then the $20M Series B "
                  "of July 2007 led by Kleiner Perkins Caufield & Byers, and the 2013 draft S-1 names the Series B "
                  "purchasers affiliated with KPCB Holdings; no earlier KP round is on record, so the entry is the "
                  "Series B (Growth). Extreme Networks bought the company in 2019."))

# ---- AEye
L.append(cls("aeye", city="Dublin", stage="Series A", stage_src="model", stage_conf="medium", focus="Industrial & Robotics",
             rounds=[rnd("2013", "seed (Form D)", 476250, None, False, None, "filing"),
                     rnd("2016-10", "Series A", 21347900, "Kleiner Perkins", True, None, "filing")],
             note="Lidar for vehicles; corporate headquarters in Dublin, California (the 2021 S-1/A). Model: Kleiner "
                  "Perkins led the Series A announced in 2017, whose offering the Form D of 2016-10-31 records (Wen "
                  "Hsieh a director from 2017); earlier money was a $0.5M 2013 seed. Listed via SPAC in 2021 (LIDR)."))

# ---- Aggregate Knowledge
L.append(cls("aggregate-knowledge", status="acquired", rng="below_1b", city="San Mateo", stage="Growth",
             stage_src="model", stage_conf="medium", entry_date="2007-04", focus="Media, Gaming & Advertising",
             flags=["stage_disputes_band"],
             rounds=[rnd("2005", "seed", None, None, False, None, "press"),
                     rnd("2007-04", "Series B", 20000000, "Kleiner Perkins", True, None, "press"),
                     rnd("2010-01", "Series C", 9000000, None, None, None, "press")],
             note="Content and audience data for publishers and advertisers, San Mateo; Neustar bought it for $119M in "
                  "2013. The firm listed it in its 2008 portfolio, so the 2009-12 Form D band (Series A) cannot be the "
                  "entry; the First Round book records the $20M Series B of April 2007 led by Kleiner Perkins after "
                  "a 2005 seed, so the entry reads Growth (model, medium)."))

# ---- Agilyx
L.append(cls("agilyx", status="public", rng="below_1b", usd=212486355, val_src="web_verified", val_cite=SA_AGLX,
             asof="2026-09-30", city="Tigard", focus="Climate & Energy",
             note="Plastics-to-oil and chemical recycling, Tigard, Oregon. The business now trades as Agilyx ASA on the "
                  "Oslo Stock Exchange (AGLX; the company's own site). Market cap NOK 2.04B on 2026-09-30 "
                  "(stockanalysis): NOK 2.04B @ ECB 2026-09-30 (NOK/EUR 10.9015, EUR/USD 1.1355) = $212.5M."))

# ---- Airbnb
L.append(cls("airbnb", city="San Francisco", stage="Growth", stage_src="web_verified", stage_cite=W("Airbnb"),
             stage_conf="high", entry_date="2015-06", focus="Consumer & Marketplaces",
             rounds=[rnd("2010-11", "Series A", 7200000, "Greylock Partners, Sequoia Capital", False, W("Airbnb"), "press"),
                     rnd("2015-06", "unnamed ($1.5B growth round)", 1500000000, None, True, W("Airbnb"), "press")],
             note="Home-sharing marketplace, San Francisco. Wikipedia: in June 2015 General Atlantic, Hillhouse, "
                  "Tiger, Kleiner Perkins Caufield & Byers and others invested $1.5 billion; the firm's own label "
                  "reads Growth with a 2015 since-year, and KPCB Holdings appears on the 2020 S-1's registration "
                  "rights. No earlier KP round is on record."))

# ---- Airtime
L.append(cls("airtime", status="defunct", rng="below_1b", city="New York", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2012", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2011", "first round", 8300000, None, False,
                         "https://techcrunch.com/2012/03/25/sean-parker-and-shawn-fanning-open-new-social-video-startup-airtime-for-business/",
                         "press"),
                     rnd("2012", "second round", 25000000, "Kleiner Perkins", True, None, "press")],
             note="Group video chat from Sean Parker and Shawn Fanning, wound down after its relaunches (aligned with "
                  "the a16z, GV and Sequoia rows; city New York as a16z and GV read it). Wikipedia's Airtime.com "
                  "article: the $25M second round of 2012 was led by Kleiner Perkins, after an $8.3M first round in "
                  "2011 (the GV row's TechCrunch citation); KP's entry was therefore a second round, Growth, not the "
                  "Form D band's Series A."))

# ---- Akeana
L.append(cls("akeana", status="private", rng="below_1b", country="US", city="Santa Clara", stage="undetermined",
             entry_date="2021", focus="Industrial & Robotics", rounds=[],
             note="RISC-V processor IP and chips, 3131 Jay Street, Santa Clara (the company's own site). It came out of "
                  "stealth in 2024 having raised over $100M from Mayfield, Fidelity and Kleiner Perkins (the "
                  "company's news page, EPDT 2024-11-18); no source read names the round the firm entered in 2021 "
                  "(the firm's since-year). No $1B+ priced round found."))

# ---- AlertEnterprise
L.append(cls("alertenterprise", status="private", rng="below_1b", city="Fremont", focus="Security",
             note="Identity and physical-logical security convergence software, Fremont, California; still operating "
                  "and privately held. Ray Lane was the KP director on the 2011 Form D."))

# ---- AlienVault
L.append(cls("alienvault", status="acquired", rng="below_1b", city="San Mateo", focus="Security",
             note="Unified security management, San Mateo; AT&T bought it in 2018 (the firm's exit line: acquired by "
                  "AT&T), aligned with the IVP row."))

# ---- Alif Semiconductor
L.append(cls("alif", status="private", rng="below_1b", city="Pleasanton", stage="Series A", stage_src="first_party",
             stage_cite=POST("alif-semiconductor-is-joining"), stage_conf="high", entry_date="2019",
             focus="Industrial & Robotics", flags=["stage_disputes_band"],
             rounds=[rnd("2019", "Series A", None, "Kleiner Perkins", True, POST("alif-semiconductor-is-joining"), "firm")],
             note="Edge-AI microcontrollers, Pleasanton (the firm's own description). The firm's post of 2026-09-09 "
                  "says 'We led the Series A that year' (2019) and later co-led the C and D, so the Form D band's "
                  "Growth is replaced by Series A. Analog Devices announced an agreement to acquire Alif on "
                  "2026-09-09 with no price disclosed; the deal has not closed, so the row stays private below $1B."))

# ---- Align Technology
L.append(cls("align-technology", city="Tempe", focus="Healthcare & Bio",
             note="Invisalign clear aligners; headquartered in Tempe, Arizona (Wikipedia)."))

# ---- Alkira
L.append(cls("alkira", status="acquired", rng="below_1b", country="US", city="San Jose", stage="Series A",
             stage_src="first_party", stage_cite=POST("alkira-built-the-network"), stage_conf="high",
             entry_date="2018", focus="Data Infrastructure",
             rounds=[rnd("2018", "Series A", None, "Kleiner Perkins, Sequoia Capital", True,
                         POST("alkira-built-the-network"), "firm"),
                     rnd("2020-10-13", "Series B", 54000000, "Koch Disruptive Technologies", None, GV_ALKIRA_B, "press"),
                     rnd("2024-05-15", "Series C", 100000000, "Tiger Global Management", None, TC_ALKIRA_C, "press"),
                     rnd("2026-07-07", "acquisition by Lumen Technologies", None, None, None, CB_ALKIRA, "press")],
             note="Multi-cloud network as a service, San Jose. The firm's own post: 'We co-led the Series A in 2018' "
                  "(with Sequoia; announced at the stealth exit in April 2020). Lumen completed the acquisition on "
                  "2026-07-07 (citybiz), aligned with the GV and Tiger Global rows."))

# ---- Allium
L.append(cls("allium", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_cite=POST("allium-series-a"), stage_conf="high", entry_date="2022",
             grad="graduated", grad_src="first_party", grad_cite=POST("allium-series-a"), grad_conf="high",
             focus="Crypto & Web3", flags=["model_disputes_source", "city_unknown"],
             rounds=[rnd("2022", "Seed", None, "Kleiner Perkins", True, POST("allium-series-a"), "firm"),
                     rnd("2024-07-18", "Series A", None, None, True, POST("allium-series-a"), "firm")],
             note="Blockchain data platform (allium.so). The firm's post of 2024-07-18: 'having led their Seed round "
                  "in 2022' and 'Today, Allium announced its Series A financing, with participation from Kleiner "
                  "Perkins', so a Seed entry that graduated. The Wikidata country CZ is a one-word name match on "
                  "another Allium and is replaced by US; the company's site names no city."))

# ---- Amazon
L.append(cls("amazon", city="Seattle", stage="Series A", stage_src="web_verified", stage_cite=S1_AMAZON,
             stage_conf="high", entry_date="1996-06", focus="Consumer & Marketplaces",
             rounds=[rnd("1996-06", "Series A Preferred", None, "Kleiner Perkins Caufield & Byers", True, S1_AMAZON,
                         "filing")],
             note="Seattle. The 1997 S-1's certain transactions: Series A Preferred Stock at $14.05 per share to "
                  "Kleiner Perkins Caufield & Byers VIII and KPCB Information Sciences Zaibatsu Fund II, with John "
                  "Doerr a director since June 1996; the firm's own since-year is 1996."))

# ---- Ambience Healthcare
L.append(cls("ambience", status="private", rng="1b_plus", usd=1250000000, val_src="web_verified", val_cite=MC_AMBIENCE,
             asof="2025-07-29", city="San Francisco", stage="Seed", stage_src="first_party",
             stage_cite=POST("ambience-series-b"), stage_conf="high", entry_date="2020",
             grad="graduated", grad_src="first_party", grad_cite=POST("ambience-series-b"), grad_conf="high",
             focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2020", "Seed", None, "Kleiner Perkins (co-lead)", True, POST("ambience-series-b"), "firm"),
                     rnd("2024-02-06", "Series B", 70000000, "Kleiner Perkins", True, POST("ambience-series-b"), "firm"),
                     rnd("2025-07-29", "Series C", 243000000, "Oak HC/FT, Andreessen Horowitz", None, MC_AMBIENCE,
                         "press")],
             note="AI clinical documentation, San Francisco. The firm's post of 2024-02-06: 'When we met Mike and "
                  "Nikhil in 2020 and co-led their seed round' and now leads the Series B, so the entry is the 2020 "
                  "Seed (the Form D band read the 2023 filing) and the named later round graduates it. Momentum check "
                  "2026-09-30: the $243M Series C at a $1.25B valuation (MedCity News, 2025-07-29) bands it 1b_plus."))

# ---- Ambiq Micro
L.append(cls("ambiq-micro", status="public", rng="1b_plus", usd=1650000000, val_src="web_verified", val_cite=SA_AMBQ,
             asof="2026-09-30", city="Austin", stage="undetermined", focus="Industrial & Robotics",
             flags=["model_disputes_source"],
             rounds=[rnd("2025-07", "Series F-1 (pre-IPO)", 29999999.75, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1500412/000119312525155270/d377490ds1.htm", "filing")],
             note="Ultra-low-power chips, Austin (the 2025 S-1 cover). The pre-filled 'acquired' is disputed: Ambiq "
                  "listed on the NYSE in July 2025 (AMBQ; the firm's own exit line reads IPO), market cap $1.65B on "
                  "2026-09-30 (stockanalysis). Wen Hsieh has been a director since November 2014; the S-1 names the "
                  "KPCB entities' Series F-1 purchase but no source read names the round the firm entered."))

# ---- Amonix
L.append(cls("amonix", status="acquired", rng="below_1b", city="Seal Beach", focus="Climate & Energy",
             note="Concentrated photovoltaic systems, headquartered in Seal Beach, California. After closing its Las "
                  "Vegas plant it sold its assets to Arzon Solar, LLC in June 2014 (Wikipedia), which carried the CPV "
                  "business on: acquired, an asset sale with a successor. The Green Growth Fund position sits in the "
                  "$129.4M Series B that closed in April 2010."))

# ---- Amprius
L.append(cls("amprius", city="Fremont", focus="Climate & Energy",
             note="Silicon-anode lithium-ion batteries, Fremont, California (NYSE: AMPX)."))

# ---- Amyris
L.append(cls("amyris", rng="below_1b", city="Emeryville", stage="Series A", stage_src="web_verified",
             stage_cite=S1_AMYRIS, stage_conf="high", entry_date="2007-04", focus="Climate & Energy",
             flags=["stage_disputes_band"],
             rounds=[rnd("2007-04", "Series A", 14100000, None, True, S1_AMYRIS, "filing"),
                     rnd("2007-09", "Series B", None, None, True, S1_AMYRIS, "filing")],
             note="Synthetic biology (fuels, then ingredients), Emeryville. The 2010 S-1's certain transactions list "
                  "3,449,861 Series A preferred shares held by KPCB Holdings, as nominee; the Series A was sold in "
                  "April and May 2007 at $2.174 (John Doerr a director since May 2006, the firm's 2006 year). So the "
                  "entry is the Series A, not the Seed band read off a 2008 Form D. Chapter 11 in 2023; status as "
                  "pre-filled."))

# ---- AOL
L.append(cls("aol", rng="below_1b", city="New York", stage="undetermined", entry_date="1987-09",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("1987-09", "investment (round not named)", None, None, True, POST("aol"), "firm")],
             note="Online services and media; headquartered in New York since 2007, sold by Yahoo to Bending Spoons in "
                  "2026 (Wikipedia). The firm's case study: 'invested in AOL in September 1987' (Frank Caufield "
                  "had earlier led the investment in Control Video Corp., AOL's predecessor); no round is named."))

# ---- Apiiro
L.append(cls("apiiro", status="private", rng="below_1b", country="IL", city="Tel Aviv", stage="Series A",
             stage_src="first_party", stage_cite=POST("apiiro-series-a"), stage_conf="high", entry_date="2020-10",
             focus="Security",
             rounds=[rnd("2020-10-13", "Series A", 35000000, "Greylock, Kleiner Perkins", True, POST("apiiro-series-a"),
                         "firm")],
             note="Application security posture management, Tel Aviv (as the Greylock and General Catalyst rows). The "
                  "firm's post of 2020-10-13: 'We're excited to co-lead apiiro's Series A' with Greylock; it was the "
                  "company's first round at its stealth exit. General Catalyst led the $100M Series B in 2022; no "
                  "$1B+ priced round on record."))

# ---- AppDynamics
L.append(cls("appdynamics", rng="below_1b", city="San Francisco", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2011", focus="Data Infrastructure",
             rounds=[rnd("2011", "Series C", 25000000, "Kleiner Perkins", True, None, "press")],
             note="Application performance monitoring, San Francisco; Cisco bought it for $3.7B in January 2017, days "
                  "before its IPO. The S-1 has KP's shares held by KPCB XIV and the KPCB Digital Growth Fund; model: "
                  "the firm first came in on the 2011 Series C (the firm's since-year 2011, after the 2008 A and "
                  "2010 B by Greylock and Lightspeed), a Growth entry."))

# ---- Applied Intuition
L.append(cls("applied-intuition", rng="10b_plus", usd=15000000000, val_src="web_verified", val_cite=AI_SERIES_F,
             asof="2025-06-17", city="Sunnyvale", stage="Growth", stage_src="first_party", stage_cite=KP_AI_POST,
             stage_conf="high", entry_date="2019", focus="Industrial & Robotics", flags=["model_disputes_source"],
             rounds=[rnd("2019-10", "Series B", 40000000, "Lux Capital", True, KP_AI_POST, "firm"),
                     rnd("2025-06-17", "Series F and tender", 600000000, "BlackRock-managed funds, Kleiner Perkins", True,
                         AI_SERIES_F, "company")],
             note="Vehicle and physical-AI software. The firm's own post of 2025-06-17: 'We first invested six years "
                  "ago at the Series B' (the $40M Lux-led round of 2019), so the site's 2018 year is not the entry. "
                  "The pre-filled $1.25B (2020) mark is stale: the $600M Series F and tender co-led by BlackRock and "
                  "Kleiner Perkins valued it at $15B (the company's release), aligned with the Coatue, General Catalyst "
                  "and Lux rows. The firm's live description places the headquarters in Sunnyvale (the sibling rows "
                  "still read Mountain View)."))

# ---- Aquion Energy
L.append(cls("aquion-energy", status="acquired", rng="below_1b", city="Pittsburgh", stage="undetermined",
             focus="Climate & Energy",
             rounds=[rnd("2011-07", "unnamed (Form D)", 29930000, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1441529/000144152911000005/0001441529-11-000005-index.htm",
                         "filing")],
             note="Saltwater stationary batteries, Pittsburgh. It filed for Chapter 11 in March 2017 and its assets "
                  "were sold at auction (Wikipedia): acquired, an asset sale out of insolvency. Kleiner Perkins is "
                  "named among its investors, but no source read names the round the firm first joined."))

# ---- Arcade
L.append(cls("arcade", status="private", rng="below_1b", city="San Francisco", stage="Series A",
             stage_src="first_party", stage_cite=POST("arcade-ai-series-a"), stage_conf="high", focus="SaaS",
             rounds=[rnd("2021", "unnamed (Form D)", 2500000, None, False, None, "filing"),
                     rnd("2022", "unnamed (Form D)", 5164996, None, False, None, "filing"),
                     rnd("2024-11", "Series A", 14000000, "Kleiner Perkins", True, POST("arcade-ai-series-a"), "firm")],
             note="Interactive product demo software, San Francisco. The firm's post of 2024-11-21: 'We're excited to "
                  "lead Arcade's Series A'; the earlier 2021-22 filings are seed money before the firm. Outside the "
                  "momentum sectors; no $1B+ round on record."))

# ---- ArcSight
L.append(cls("arcsight", status="acquired", rng="below_1b", city="Cupertino", stage="undetermined", entry_date="2002",
             focus="Security",
             note="Security information and event management, Cupertino; IPO 2008, bought by HP in 2010. Ted Schlein "
                  "has been a director since March 2002 (the 2007 S-1) and the firm's since-year is 2002; no source "
                  "read names the round."))

# ---- Area 1 Security
L.append(cls("area-1-security", status="acquired", rng="below_1b", city="Redwood City", focus="Security",
             note="Anti-phishing email security, Redwood City; Cloudflare bought it for $162M in April 2022 "
                  "(Wikipedia)."))

# ---- Argonaut Technologies
L.append(cls("argonaut", status="acquired", rng="below_1b", country="US", city="Foster City", stage="undetermined",
             focus="Healthcare & Bio",
             note="Chemistry instruments and consumables for drug discovery, Foster City; IPO 2000, bought by Biotage "
                  "in 2005 (as the IVP row). Brook Byers chaired it from 1995 (the 2001 10-K) and KP funds filed "
                  "13Gs from 2001; no round is named."))

# ---- ARMO BioSciences
L.append(cls("armo-biosciences", status="acquired", rng="below_1b", country="US", city="Redwood City", stage="Growth",
             stage_src="web_verified", stage_cite=S1_ARMO, stage_conf="medium", entry_date="2014-05",
             focus="Healthcare & Bio",
             rounds=[rnd("2014-05", "Series B", 29910636, None, True, S1_ARMO, "filing"),
                     rnd("2015-10", "Series B-1 (ACIR merger)", None, None, True, S1_ARMO, "filing"),
                     rnd("2015-11", "Series C", 24485110, None, True, S1_ARMO, "filing")],
             note="Immuno-oncology (pegilodecakin), Redwood City; Eli Lilly bought it for about $1.6B in 2018. The "
                  "S-1's certain transactions show entities affiliated with Kleiner Perkins buying $7.9M of the "
                  "Series B (2014), then B-1, C and C-1; no earlier KP preferred series is listed and the firm's "
                  "since-year is 2014, so Growth (medium: Beth Seidenberg sat on the board from December 2012)."))

# ---- Arresto Biosciences
L.append(cls("arresto-biosciences", status="acquired", rng="below_1b", country="US", city="Palo Alto",
             stage="undetermined", entry_date="2007", focus="Healthcare & Bio",
             note="Antibodies against extracellular-matrix targets for cancer and fibrosis, Palo Alto (the firm's "
                  "2008-11 listing); Gilead bought it (the firm's exit line). The firm's since-year is 2007; no source "
                  "read names the round."))

# ---- ArsenalBio
L.append(cls("arsenalbio", status="private", rng="below_1b", country="US", city="South San Francisco",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2019", focus="Healthcare & Bio",
             rounds=[rnd("2019", "Series A", 85000000, None, True, None, "press"),
                     rnd("2024-09-04", "Series C", 325000000, None, True, ARSENAL_C, "company")],
             note="Programmable T-cell therapies, headquartered in South San Francisco (the company's 2024 release, "
                  "which names Kleiner Perkins among existing investors in the $325M Series C, no valuation "
                  "disclosed). Model: the firm co-founded it in the $85M Series A of 2019 (the firm's since-year)."))

# ---- Ascend Communications
L.append(cls("ascend-communications", status="acquired", rng="below_1b", city="Alameda", stage="undetermined",
             entry_date="1989", focus="Data Infrastructure",
             rounds=[rnd("1989", "initial venture funding", None, None, True, W("Ascend Communications"), "press")],
             note="Remote-access networking, Alameda; IPO 1994, bought by Lucent in 1999. Wikipedia names KPCB, "
                  "Greylock and NEA as initial investors without a round name, as the Greylock, Menlo and NEA rows "
                  "read it."))

# ---- Atara Biotherapeutics
L.append(cls("atara-biotherapeutics", country="US", city="Thousand Oaks", stage="Series A", stage_src="web_verified",
             stage_cite=DRS_ATARA, stage_conf="high", entry_date="2012-10", focus="Healthcare & Bio",
             rounds=[rnd("2012-10", "Series A", 20087750, None, True, DRS_ATARA, "filing")],
             note="Allogeneic T-cell immunotherapy (the atara-bio row is the same company). The 2014 draft S-1: "
                  "Series A sold in October 2012, January and March 2013, with entities affiliated with Kleiner "
                  "Perkins Caufield & Byers buying 1,666,666 shares for $5.0M; incorporated August 2012. Headquarters "
                  "now in Thousand Oaks, California."))

# ---- Audible
L.append(cls("audible", status="acquired", rng="below_1b", country="US", city="Newark", stage="undetermined",
             entry_date="1998", focus="Media, Gaming & Advertising",
             note="Audiobooks and spoken audio, headquartered in Newark, New Jersey (Wikipedia); IPO 1999, bought by "
                  "Amazon in 2008. KP funds filed 13Gs in 2000-01 and the firm's since-year is 1998; no round named."))

# ---- Audius
L.append(cls("audius", status="private", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
             entry_date="2018", focus="Crypto & Web3",
             note="Decentralised music streaming, San Francisco. The firm's since-year is 2018, the year of the Series "
                  "A the Lightspeed card names; no source read ties Kleiner Perkins to a named round (the General "
                  "Catalyst row is undetermined too)."))

# ---- Ausra
L.append(cls("ausra", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="undetermined",
             focus="Climate & Energy",
             note="Compact linear Fresnel solar thermal, Mountain View; Areva bought it in 2010 (as the Khosla row). "
                  "The firm listed it in 2008, before the 2009-04 Form D on file, so that date is a later round; no "
                  "source read names the round KP first joined."))

# ---- Autonomic Technologies
L.append(cls("autonomic-technologies-inc", status="acquired", rng="below_1b", city="Redwood City",
             focus="Healthcare & Bio",
             note="Implantable sphenopalatine-ganglion stimulator for cluster headache, Redwood City (the firm's "
                  "2008-11 listing). Its domain ati-spg.com now redirects to Realeve, which markets the same Pulsante "
                  "system (checked 2026-09-30), so the business continues under a successor: acquired, medium "
                  "confidence."))

# ---- AutoTrader.com
L.append(cls("autotrader-com", status="acquired", rng="below_1b", country="US", city="Atlanta", stage="undetermined",
             entry_date="1999", focus="Consumer & Marketplaces",
             note="Online car marketplace, Atlanta; Cox Enterprises took full ownership and it is now part of Cox "
                  "Automotive. Wikipedia names KPCB as an investor; the firm's since-year is 1999; no round named."))

# ---- Auxogyn (now Progyny)
L.append(cls("auxogyn-inc", city="New York", stage="Series A", stage_src="web_verified", stage_cite=F3_PROGYNY,
             stage_conf="medium", focus="Healthcare & Bio",
             rounds=[rnd("2012-05", "Series A", 18000001, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1551306/000155130612000001/0001551306-12-000001-index.htm",
                         "filing")],
             note="Auxogyn merged with Fertility Authority and renamed itself Progyny (Nasdaq: PGNY), headquartered in "
                  "New York; market cap $1.93B on 2026-09-30 (stockanalysis), as pre-filled. KPCB XIII's Form 3 at "
                  "the 2019 IPO reports Series A and Series B preferred; with Beth Seidenberg a director on the $18M "
                  "Form D of 2012, the entry is the Series A (medium)."))

# ---- Awarepoint
L.append(cls("awarepoint", status="unknown", rng="below_1b", city="San Diego", focus="Healthcare & Bio",
             note="Real-time location systems for hospitals, San Diego. Its last Form D is from 2017 and its own "
                  "website no longer serves (expired certificate, checked 2026-09-30); no acquisition or shutdown "
                  "found, so the state is unknown."))

# ---- Axion
L.append(cls("axion", status="acquired", rng="below_1b", stage="undetermined", entry_date="1991",
             focus="Healthcare & Bio", flags=["city_unknown", "model_disputes_source"],
             note="The firm's own card: a biopharmaceutical company, first investment 1991, acquired by BMS. The Form D "
                  "joined to this row is Axion BioSystems, Inc. of Atlanta (CIK 1458565, founded 2008), a different "
                  "company, so its 2009 date is not the entry: the firm's 1991 year stands. No source read places "
                  "the 1991 Axion's city or names its round."))

jl.write("j01a", L)
