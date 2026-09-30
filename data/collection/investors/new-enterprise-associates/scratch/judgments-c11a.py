"""PRO-100 NEA, judge c11, queue batch 21 (triValence .. VistaGen): classification of listed members."""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, SITE, POST, W, FTS, NEWS, FORMD_CITE

WV = {"valuation_range_source": "web_verified"}
TODAY = "2026-09-30"

# URLs printed by tools run in this session (ftsview/secget, stockanalysis curl, WebFetch reads)
TRIV_S1 = "https://www.sec.gov/Archives/edgar/data/1432732/000119312514091651/d638780ds1.htm"
ULTH_S1 = "https://www.sec.gov/Archives/edgar/data/1345889/000119312514150988/d662886ds1.htm"
TUYA_F1 = "https://www.sec.gov/Archives/edgar/data/1829118/000119312521058848/d75491df1.htm"
VRNA_F1 = "https://www.sec.gov/Archives/edgar/data/1657312/000104746917002313/a2231519zf-1.htm"
VRNA_DRSA = "https://www.sec.gov/Archives/edgar/data/1657312/000091205717000022/filename1.htm"
VTGN_8K = "https://www.sec.gov/Archives/edgar/data/1411685/000165495420013839/ex99-1.htm"
VIRATA_10K = "https://www.sec.gov/Archives/edgar/data/1094371/000101287001501348/d10k.txt"
SA = "https://stockanalysis.com/stocks/{}/market-cap/"
ULINK_SITE = "http://m.vipwifi.com"

L = []

# ---- triValence
L.append(cls("trivalence", status="private", country="US", stage="undetermined", entry_date="2021", rng="below_1b",
             focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
             note="Healthcare supply-chain payments platform the firm lists as a 2021 Early investment, still private. "
                  "Google News on 2026-09-30 (the name beside NEA) showed a 2022 Axios profile and a 2025 CEO appointment "
                  "but no priced round, so neither the entry round nor a $1B+ mark is on record; the company's own site gives "
                  "no location."))

# ---- TriVascular
L.append(cls("trivascular", city="Santa Rosa", city_src="formd_address", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2008-03", rng="below_1b", focus="Healthcare & Bio",
             rounds=[rnd("2008-03", "Series A", None, None, True, TRIV_S1, "filing"),
                     rnd("2010-06", "Series C", None, None, None, TRIV_S1, "filing"),
                     rnd("2012-06", "Series D", None, None, None, TRIV_S1, "filing")],
             note="The S-1 says TV2 Holding bought the business back from Boston Scientific in March 2008 and NEA's Jake Nunn "
                  "has sat on the board since March 2008, so NEA entered in the spin-off financing, TV2's first preferred "
                  "(Series A); the pre-filled 2013 entry date is a later Form D. Acquired by Endologix in 2016."))

# ---- Tulip
TULIP_A = NEWS("tulip", "Tulip Announces $13 Million Series A")
TULIP_D = "https://news.crunchbase.com/venture/ai-leads-unicorn-board-count-january-2026/"
L.append(cls("tulip", status="private", city="Somerville", city_src="formd_address", stage="Series A",
             stage_src="web_verified", stage_cite=TULIP_A, stage_conf="high", entry_date="2017-06-06",
             rng="1b_plus", usd=1300000000, val_src="web_verified", val_cite=TULIP_D, asof="2026-01", extra=WV,
             focus="SaaS",
             rounds=[rnd("2017-06-06", "Series A", 13000000, "NEA", True, TULIP_A, "company"),
                     rnd("2021-08-10", "Series C", 100000000, None, None, NEWS("tulip", "Tulip Raises $100 Million"), "press"),
                     rnd("2026-01", "Series D", 120000000, "Mitsubishi Electric", None, TULIP_D, "press")],
             note="NEA led the $13M Series A (company release, 2017-06-06), matching the firm's 2017 listing. Crunchbase News "
                  "reports the January 2026 $120M Series D led by Mitsubishi Electric at a $1.3B valuation, which bands the "
                  "row 1b_plus; checked 2026-09-30."))

# ---- Tune Therapeutics (stage left as pre-filled; see note)
L.append(cls("tune-therapeutics", status="private", city="Seattle", city_src="formd_address", rng="below_1b",
             focus="Healthcare & Bio",
             rounds=[rnd("2021-12-02", "launch financing", 40000000, None, None,
                         NEWS("tune-therapeutics", "launches with $40M"), "press"),
                     rnd("2025-01-12", "Series B", 175000000, None, None,
                         NEWS("tune-therapeutics", "Completes Over $175M in Series B"), "company")],
             note="Epigenome-editing biotech with Durham and Seattle sites; its 2025 Form D gives Seattle. Last round the "
                  "$175M Series B of January 2025 with no disclosed valuation. The pre-filled Growth band reads that "
                  "filing, while the firm lists a 2020 first investment and the company launched with $40M in December 2021; "
                  "no readable page tied NEA to the launch round, so the stage was not disputed here."))

# ---- Turi (GraphLab, Dato)
GL = W("GraphLab")
L.append(cls("turi", country="US", city="Seattle", stage="Series A", stage_src="web_verified", stage_cite=GL,
             stage_conf="high", entry_date="2013-05", rng="below_1b", focus="AI & Applied AI",
             flags=["model_disputes_source"],
             rounds=[rnd("2013-05-14", "Series A", 6750000, None, True, GL, "press"),
                     rnd(None, "Series B", 18500000, "Vulcan Capital", True, GL, "press")],
             note="Turi was GraphLab (later Dato) of Seattle; Wikipedia names the $6.75M Series A from Madrona and NEA "
                  "(GeekWire, 2013-05-14), matching the firm's 2013 listing, and Apple bought it in August 2016. The "
                  "pre-filled IT country was a one-word-name join."))

# ---- Tuya
L.append(cls("tuya", status="public", country="CN", country_src="web_verified", country_cite=TUYA_F1,
             city="Hangzhou", stage="Series A", stage_src="web_verified", stage_cite=TUYA_F1, stage_conf="high",
             entry_date="2014", rng="1b_plus", usd=1060000000, val_src="web_verified", val_cite=SA.format("tuya"),
             asof=TODAY, extra=WV, focus="Industrial & Robotics",
             rounds=[rnd("2014", "Series A", None, "NEA", True, TUYA_F1, "filing"),
                     rnd("2018-04-16", "Series C", None, None, True, TUYA_F1, "filing")],
             note="The F-1 shows New Enterprise Associates 14 holding 58.0M of the 65.3M Series A preferred shares and "
                  "designating the Series A directors, so NEA's 2014 entry was the Series A; NEA 14 and NEA 15-OF added "
                  "Series C in April 2018. Principal office in Hangzhou (F-1). Market cap $1.06B on 2026-09-30 "
                  "(stockanalysis.com), 6% above the band edge."))

# ---- TwelveLabs (disputes the Form D band)
TL_B = NEWS("twelvelabs", "TwelveLabs Raises $100 Million")
L.append(cls("twelvelabs", status="private", city="San Francisco", city_src="formd_address", stage="Series A",
             stage_src="first_party", stage_cite=POST("twelve-labs-multimodal"), stage_conf="high",
             entry_date="2024-06-04", rng="below_1b", focus="AI & Applied AI", flags=["stage_disputes_band"],
             extra={"valuation_range_source": "web_verified", "valuation_citation": TL_B, "valuation_asof": TODAY},
             rounds=[rnd("2024-06-04", "Series A", 50000000, "NEA, NVentures", True, POST("twelve-labs-multimodal"), "firm"),
                     rnd("2026-07-01", "Series B", 100000000, "NEA, NAVER Ventures", True, TL_B, "company")],
             note="The firm's own post (2024-06-04) says NEA co-led the Series A with NVentures; the Growth band read the "
                  "$50M filing after two earlier Form Ds. Momentum check 2026-09-30: the July 2026 $100M Series B "
                  "(co-led by NEA and NAVER Ventures, HQ San Francisco) discloses no valuation, so no $1B+ mark."))

# ---- U.S. Renal Care
USRC = NEWS("u-s-renal-care", "to be Acquired by Investor Group")
L.append(cls("u-s-renal-care", status="acquired", country="US", city="Plano", stage="Growth", stage_src="first_party",
             stage_cite=SITE("u-s-renal-care"), stage_conf="medium", entry_date="2015", rng="below_1b",
             focus="Healthcare & Bio",
             note="Dialysis operator headquartered in Plano; the firm labels its 2015 entry Growth. Sold in February 2019 by "
                  "Leonard Green, Frazier, NEA and Cressey to a group led by management with Bain Capital, Summit and "
                  "Revelstoke (Bain Capital's release)."))

# ---- Uber
L.append(cls("uber", status="public", country="US", city="San Francisco", stage="Growth", stage_src="first_party",
             stage_cite=SITE("uber"), stage_conf="medium", entry_date="2014", rng="100b_plus", usd=140830000000,
             val_src="web_verified", val_cite=SA.format("uber"), asof=TODAY, extra=WV,
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             note="The firm labels its 2014 entry Growth. Market cap $140.83B on 2026-09-30 (stockanalysis.com). The "
                  "pre-filled NL country is Uber's Dutch holding entity; the company is headquartered in San Francisco, as "
                  "most sibling books have it."))

# ---- Uhana
L.append(cls("uhana", status="acquired", country="US", city="Palo Alto", stage="undetermined", rng="below_1b",
             focus="Data Infrastructure", rounds=[],
             note="Mobile network (radio access) analytics startup acquired by VMware, as the firm's exit line says. Google "
                  "News on 2026-09-30 returned only namesakes, so NEA's entry round is not on record; the firm's 2020 "
                  "year sits oddly beside a 2017 first capture and was not used."))

# ---- Ulink
L.append(cls("ulink", status="private", country="CN", country_src="web_verified", country_cite=ULINK_SITE,
             stage="undetermined", entry_date="2014", rng="below_1b", focus="Consumer & Marketplaces",
             flags=["city_unknown"], rounds=[],
             note="Travel SIM and portable WiFi reseller for Chinese outbound travellers; its own site (vipwifi.com, in "
                  "Chinese) gives no address. The firm still lists it Private; no round or later event found."))

# ---- Ulthera
UL_VA = FTS("ULTHERA", "DRS")
L.append(cls("ulthera", status="acquired", city="Mesa", city_src="formd_address", stage="Growth",
             stage_src="web_verified", stage_cite=UL_VA, stage_conf="high", entry_date="2007-12", rng="below_1b",
             focus="Healthcare & Bio",
             rounds=[rnd("2007-12", "Series B", None, "NEA", True, UL_VA, "filing"),
                     rnd(None, "Series C", None, None, True, ULTH_S1, "filing")],
             note="The firm's own post dates its initial investment to late 2007, and the voting agreement filed with the "
                  "IPO registration gives New Enterprise Associates 12 the Series B director seat (the rights agreement it "
                  "amends is dated 2007-12-27), so NEA entered at the Series B. The pre-filled 2010 date is a later Form D. "
                  "Merz bought Ulthera for about $600M in 2014."))

# ---- UltraDNS
L.append(cls("ultradns", status="acquired", country="US", city="Brisbane", stage="undetermined", entry_date="2000",
             rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="Managed DNS provider acquired by Neustar in 2006, per the firm's exit line; the 2000 round NEA joined "
                  "is not named in any source found."))

# ---- UnifyID
L.append(cls("unifyid", status="acquired", country="US", city="San Francisco", stage="undetermined", entry_date="2017",
             rng="below_1b", focus="Security", rounds=[],
             note="Implicit-authentication startup acquired by Prove, per the firm's exit line; city and status agree with "
                  "the a16z book. Two Google News searches on 2026-09-30 found no page naming the round NEA entered in "
                  "2017."))

# ---- Union (fka TabbedOut)
L.append(cls("union", status="private", country="US", city="Austin", stage="undetermined", entry_date="2010",
             rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"], rounds=[],
             note="Union is the renamed TabbedOut, the Austin restaurant payments and POS company the firm has held since "
                  "2010; the pre-filled NL country was a one-word-name join. No page names NEA's entry round."))

# ---- Union.ai
UAI_S = NEWS("union-ai", "Raises $10M in Seed Funding")
UAI_A = NEWS("union-ai", "Union AI raises $19.1M Series A")
L.append(cls("union-ai", status="private", country="US", city="Bellevue", stage="Seed", stage_src="web_verified",
             stage_cite=UAI_S, stage_conf="high", entry_date="2022-04-12", grad="graduated",
             grad_src="web_verified", grad_cite=UAI_A, grad_conf="high", rng="below_1b", focus="Data Infrastructure",
             rounds=[rnd("2022-04-12", "Seed", 10000000, "NEA", True, UAI_S, "company"),
                     rnd("2023-05-17", "Series A", 19100000, "NEA, Nava Ventures", True, UAI_A, "press")],
             note="The firm labels its entry Seed, and the company's release (2022-04-12, Bellevue) says NEA led the $10M "
                  "seed; TechCrunch reports the $19.1M Series A from NEA and Nava Ventures in May 2023, which graduates the "
                  "row. The firm's 2020 year is read as a close year."))

# ---- Uniphore (valuation)
UNI_E = NEWS("uniphore", "Uniphore raises $400M in Series E led by NEA")
L.append(cls("uniphore", status="private", city="Palo Alto", city_src="formd_address", rng="1b_plus", usd=2500000000,
             val_src="web_verified", val_cite=UNI_E, asof="2022-02-16", extra=WV, focus="AI & Applied AI",
             flags=["stale"],
             rounds=[rnd("2022-02-16", "Series E", 400000000, "NEA", True, UNI_E, "press"),
                     rnd("2025-10-22", "Series F", 260000000, None, True,
                         NEWS("uniphore", "AI startup Uniphore raises $260 million in Series F"), "press")],
             note="NEA led the $400M Series E at a $2.5B valuation (YourStory, 2022-02-16; the firm's own post confirms the "
                  "lead). Momentum check 2026-09-30: the October 2025 $260M Series F (NVIDIA, AMD, Snowflake, Databricks, "
                  "NEA) disclosed no valuation, so the 2022 mark stands, flagged stale."))

# ---- Upskill (APX Labs)
L.append(cls("upskill", status="acquired", city="Vienna", city_src="formd_address", stage="undetermined",
             entry_date="2014", rng="below_1b", focus="SaaS", rounds=[],
             note="Enterprise wearables software company (formerly APX Labs) acquired by TeamViewer, per the firm's exit "
                  "line. The firm lists a 2014 first investment; the 2019 Form D is a later round and no page names the "
                  "round NEA entered."))

# ---- Upstart
UP_W = W("Upstart Holdings")
L.append(cls("upstart", country="US", city="Burlingame", stage="Seed", stage_src="web_verified", stage_cite=UP_W,
             stage_conf="high", entry_date="2012-04", grad="graduated", grad_src="web_verified", grad_cite=UP_W,
             grad_conf="high", rng="1b_plus", usd=2240000000, val_src="web_verified", val_cite=SA.format("upst"),
             asof=TODAY, extra=WV, focus="Fintech & Payments",
             rounds=[rnd("2012-04", "Seed", 1750000, None, True, UP_W, "press"),
                     rnd(None, "Series A", 5900000, None, None, UP_W, "press")],
             note="Wikipedia names NEA in the $1.75M seed that came with the April 2012 launch (the firm also labels it "
                  "Seed) and the $5.9M Series A that followed, which graduates the row. City aligned with the GV book, "
                  "which read Burlingame off the 2026 10-Q. Market cap $2.24B on 2026-09-30 (stockanalysis.com), replacing "
                  "the 2025 float."))

# ---- Upwork (formerly oDesk): D8, the Elance position is the member (elance-inc)
L.append(verdict("upwork-formerly-odesk", "not_member",
                 "D8: NEA's Upwork stock came from oDesk's 2013 all-stock combination with Elance, the company NEA 10 "
                 "backed from 2003 (the S-1 shows NEA 10 holding Elance-oDesk preferred); this listing carries Elance's 2003 "
                 "year and services-procurement description. Elance is the member (row elance-inc); the acquirer's stock "
                 "is sale consideration.", ec="site_listing", conf="high",
                 cite=FTS("Upwork", "DRS")))

# ---- Upworthy
UPW_R = NEWS("upworthy", "closes $8M round")
L.append(cls("upworthy", status="acquired", city="New York", stage="Seed", stage_src="first_party",
             stage_cite=SITE("upworthy"), stage_conf="medium", entry_date="2012", grad="graduated",
             grad_src="web_verified", grad_cite=UPW_R, grad_conf="medium", rng="below_1b",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2012", "Seed", None, None, True, SITE("upworthy"), "firm"),
                     rnd("2013-09-16", "unnamed", 8000000, None, None, UPW_R, "press")],
             note="The firm labels its 2012 entry Seed. Reuters reports the $8M round of September 2013 (the Spark book reads "
                  "it as Spark's Series A); with the seed amount not on record the 2011-14 seed ceiling ($2.5M) stands in, "
                  "and $8M clears the step-up, so the row graduated. Merged into GOOD Worldwide in January 2017."))

# ---- Ursa Space Systems (a documented round overrides the Seed label)
URSA_A = NEWS("ursa", "Secures $7 Million Series A")
L.append(cls("ursa", status="private", country="US", city="Ithaca", stage="Series A", stage_src="web_verified",
             stage_cite=URSA_A, stage_conf="medium", entry_date="2017-10-25", rng="below_1b",
             focus="Data Infrastructure", flags=["model_disputes_source", "stage_disputes_band"],
             rounds=[rnd("2017-10-25", "Series A", 7000000, "Paladin Capital Group", True, URSA_A, "press"),
                     rnd("2019-11-07", "Series B", 15000000, None, None,
                         NEWS("ursa", "Ursa Secures $15 Million in Series B"), "press")],
             note="Ursa Space Systems of Ithaca, NY (the pre-filled ES country was a one-word-name join). The firm labels its "
                  "2017 entry Seed, but the only 2017 round on record is the $7M Series A of October 2017 led by Paladin with "
                  "NEA participating (Via Satellite), and no earlier NEA round or post exists, so the named round is used. "
                  "Sumitomo invested in 2025; no $1B mark."))

# ---- UUNET
UU = W("UUNET")
L.append(cls("uunet", status="acquired", country="US", city="Fairfax", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="1993", rng="below_1b", focus="Data Infrastructure",
             rounds=[rnd("1993", "Series A", 6000000, None, True, UU, "press"),
                     rnd("1996", "unnamed", 8200000, None, None, UU, "press")],
             note="Wikipedia names the $6M 1993 round from Accel, Menlo and NEA, UUNET's first venture round, which the "
                  "Accel book (from its own listing) calls the Series A. Acquired by MFS Communications in 1996; city aligned "
                  "with the Accel book."))

# ---- Valarian
VAL_P = POST("our-investment-in-valarian")
L.append(cls("valarian", status="private", country="GB", country_src="web_verified", country_cite=VAL_P,
             city="London", stage="Series A", stage_src="first_party", stage_cite=VAL_P, stage_conf="high",
             entry_date="2026-07-14", rng="below_1b", focus="Data Infrastructure",
             rounds=[rnd("2026-07-14", "Series A", 50000000, "NEA", True, VAL_P, "firm")],
             note="The firm's own post (2026-07-14) says NEA leads Valarian's $50M Series A and that the company is based in "
                  "London. Momentum check 2026-09-30 (Google News): the Series A is the only round reported and no "
                  "valuation was disclosed."))

# ---- Valley Steer
L.append(cls("valley-steer", status="private", country="US", stage="Seed", stage_src="first_party",
             stage_cite=SITE("valley-steer"), stage_conf="medium", entry_date="2024", grad="censored",
             rng="below_1b", focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
             note="AI-native revenue-cycle outsourcing for providers; the firm labels its 2024 entry Seed. A bare 2024 entry "
                  "is still inside the 24-month window, so censored. Google News found no coverage and the company's site "
                  "gives no location."))

# ---- ValueFirst
VF_T = NEWS("valuefirst", "Twilio acquires India")
L.append(cls("valuefirst", status="acquired", country="IN", country_src="web_verified", country_cite=VF_T,
             city="Gurugram", stage="undetermined", entry_date="2008", rng="below_1b", focus="DevTools & APIs",
             rounds=[],
             note="Indian messaging and mobile-marketing platform; Twilio bought it in 2021 (India New England News) and "
                  "sold it to Tanla Platforms in 2023 (ET Telecom). The firm's listing still says Private. No page names "
                  "the 2008 round NEA entered."))

# ---- Vantage Oncology
L.append(cls("vantage-oncology", status="acquired", country="US", city="Manhattan Beach", stage="undetermined",
             entry_date="2004", rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Radiation oncology center operator acquired by McKesson, per the firm's exit line; the 2004 round is not "
                  "named in any source found."))

# ---- VAST Data
L.append(cls("vast-data", city="New York", stage="Growth", stage_src="first_party", stage_cite=SITE("vast-data"),
             stage_conf="medium", entry_date="2023",
             focus="Data Infrastructure",
             note="The firm labels its 2023 entry Growth; the Tiger Global book also has a Growth entry and the $30B mark. "
                  "City aligned with that book."))

# ---- VeloCloud
L.append(cls("velocloud", status="acquired", country="US", city="Mountain View", stage="undetermined",
             entry_date="2013", rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="SD-WAN company acquired by VMware in 2017 (Broadcom later sold the unit to Arista in 2025); the firm's "
                  "listing still says Private. Google News found no page naming NEA's 2013 round."))

# ---- Veriflow
VF0, VF1 = FORMD_CITE("veriflow", 0), FORMD_CITE("veriflow")
L.append(cls("veriflow", status="acquired", city="San Jose", grad="graduated", grad_src="formd", grad_cite=VF1,
             grad_conf="high", rng="below_1b", focus="Security",
             rounds=[rnd("2014-10-02", "Seed", 2900151, None, True, VF0, "filing"),
                     rnd("2016-06-21", "unnamed", 8181002, None, True, VF1, "filing")],
             note="The firm labels its 2014 entry Seed and the Form D sequence shows the $2.9M seed, then an $8.2M round in "
                  "June 2016 (the round Menlo entered), which graduates the row. Acquired by VMware; city aligned with the "
                  "Menlo book (the Form Ds carry the earlier Champaign address)."))

# ---- Verona Pharma (X1 case)
L.append(cls("verona-pharma", city="London", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2016-07", rng="below_1b", focus="Healthcare & Bio",
             rounds=[rnd("2016-07", "private placement (AIM-listed)", None, None, True, VRNA_DRSA, "filing")],
             note="X1 case: Verona has traded on AIM since 2006 and NEA's Growth Equity Opportunities Fund IV bought in the "
                  "July 2016 placement (the F-1 and the holder table), a PIPE into a listed company; membership under X1 "
                  "is left to that pass and the stage is the Growth X1 assigns if a PIPE is ruled an entry. Acquired by "
                  "Merck in 2025."))

# ---- Vertex Pharmaceuticals
L.append(cls("vertex-pharmaceuticals", status="public", city="Boston", stage="undetermined", entry_date="1989",
             rng="100b_plus", usd=133440000000, val_src="web_verified", val_cite=SA.format("vrtx"), asof=TODAY,
             extra=WV, focus="Healthcare & Bio", rounds=[],
             note="Market cap $133.44B on 2026-09-30 (stockanalysis.com). NEA's 1989 founding-year round is not named in any "
                  "source on EDGAR's electronic record, which starts after the 1991 IPO."))

# ---- Vertica
L.append(cls("vertica", city="Billerica", stage="undetermined", entry_date="2006", rng="below_1b",
             focus="Data Infrastructure", rounds=[],
             note="Column-store database company acquired by HP in March 2011 (Wikipedia); last headquartered in Billerica, "
                  "MA. No page names the 2006 round NEA entered."))

# ---- Vertiflex
L.append(cls("vertiflex", status="acquired", country="US", city="Carlsbad", stage="undetermined", entry_date="2008",
             rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Spine device company acquired by Boston Scientific in 2019, per the firm's exit line; the 2008 round is "
                  "not named in any source found."))

# ---- Vesper Medical
L.append(cls("vesper-medical", status="acquired", city="Wayne", city_src="formd_address", rng="below_1b",
             focus="Healthcare & Bio",
             note="Venous stent company acquired by Royal Philips, per the firm's exit line."))

# ---- Veza
L.append(cls("veza", status="acquired", country="US", city="Palo Alto", stage="Growth", stage_src="first_party",
             stage_cite=SITE("veza"), stage_conf="medium", entry_date="2025", rng="below_1b", focus="Security",
             note="The firm labels its 2025 entry Growth. Acquired by ServiceNow, per the firm's exit line; status and city "
                  "aligned with the Accel, BCV and GV books."))

# ---- Vibrynt
L.append(cls("vibrynt-inc", status="unknown", city="Redwood City", city_src="formd_address", stage="undetermined",
             rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Obesity implant company the firm listed only in 2013; its Form Ds (2011-12, NEA's Nehra, Makower and Drant "
                  "as directors) give Redwood City. Google News found nothing on its fate, and the 2011 filing is a later "
                  "round of a 2006 company, so the entry round is not on record."))

# ---- Viddy
L.append(cls("viddy", status="acquired", city="Los Angeles", rng="below_1b",
             focus="Consumer & Marketplaces",
             note="Wikipedia: founded in Los Angeles in 2011, a $6M Series A in February 2012, then the $30M round with NEA "
                  "(the Growth entry already on the row); acquired by Fullscreen as Supernova in January 2014. The Form D "
                  "and sibling books say Venice, which is a Los Angeles neighbourhood, not a municipality."))

# ---- Videology
L.append(cls("videology", status="acquired", city="New York", stage="undetermined", entry_date="2008",
             rng="below_1b", focus="Media, Gaming & Advertising", rounds=[],
             note="Founded in Baltimore in 2007 as Tidal TV and moved to New York in 2016; filed Chapter 11 in May 2018 and its "
                  "assets were bought by Singtel's Amobee (Wikipedia), an asset sale out of insolvency. The firm's year is "
                  "2008; the pre-filled 2012 date is a later Form D, and no page names NEA's entry round."))

# ---- Vimaan Robotics
L.append(cls("vimaan-robotics", status="private", country="US", city="San Jose", city_src="web_verified",
             stage="undetermined", entry_date="2020", rng="below_1b", focus="Industrial & Robotics", rounds=[],
             note="Warehouse computer-vision and robotics company, San Jose-based (San Jose Inside, 2025). Google News found "
                  "no round naming NEA."))

# ---- Virata
L.append(cls("virata", status="acquired", country="US", city="Santa Clara", stage="undetermined", entry_date="1995",
             rng="below_1b", focus="Industrial & Robotics", rounds=[],
             note="DSL chip company founded in Cambridge, England, headquartered in Santa Clara by its 2001 10-K; merged with "
                  "Globespan into GlobespanVirata in December 2001. NEA's Peter Morris joined the board in May 1995; the "
                  "round is not named."))

# ---- Virtela
L.append(cls("virtela", status="acquired", city="Greenwood Village", city_src="formd_address", stage="undetermined",
             entry_date="2001", rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="Managed network services company acquired by NTT Communications, per the firm's exit line. The firm dates "
                  "its entry to 2001; the pre-filled 2010 date is a later Form D, and the 2001 round is not named."))

# ---- Virtru
VW = W("Virtru")
L.append(cls("virtru", status="private", city="Washington", stage="undetermined", entry_date="2014",
             rng="below_1b", focus="Security",
             rounds=[rnd("2016-08-22", "Series A", 29000000, "Bessemer Venture Partners", True, VW, "press"),
                     rnd("2018-05-31", "Series B", 37000000, "ICONIQ Capital", True, VW, "press")],
             note="Wikipedia names NEA in the $29M Series A of August 2016 and the 2018 Series B, but the firm dates its first "
                  "investment to 2014, so the 2016 round may be a follow-on and the entry round is left undetermined. Band "
                  "aligned with the ICONIQ book's $500M Series D mark of July 2025."))

# ---- Vishwa
L.append(cls("vishwa", status="private", country="IN", country_src="web_verified", country_cite=SITE("vishwa"),
             city="Hyderabad", stage="Growth", stage_src="first_party", stage_cite=SITE("vishwa"), stage_conf="medium",
             entry_date="2011", rng="below_1b", focus="Climate & Energy",
             note="Hyderabad-based water and waste-water infrastructure services company (the firm's own page), which the "
                  "firm labels a 2011 Growth investment."))

# ---- VistaGen (X1 / R2 case)
L.append(cls("vistagen-therapeutics", country="US", city="South San Francisco", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2020-12", focus="Healthcare & Bio",
             rounds=[rnd("2020-12-22", "public offering (Series D preferred)", None, None, True, VTGN_8K, "filing")],
             note="X1 and R2 case: VistaGen was already listed when NEA led its December 2020 public offering of Series D "
                  "preferred (the company's 8-K), a purchase by the Growth Equity Opportunities vehicle; membership under "
                  "X1 is left to that pass and the stage is the Growth X1 assigns if a PIPE is ruled an entry."))

jl.write("c11a", L)
