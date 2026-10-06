"""Judge j02, part c (PRO-80 Bessemer Venture Partners, batch 4: dashlane .. doppel), 2026-10-01.
Rows are members on the firm's own listing; classification lines only. Run as NQ_TAG=j02 python3 judgments-j02c.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "scratchpad" / "j02"))
import judge_lib as jl
from judge_lib import ARCH, NEWS, POST, SITE, W, cls, rnd
from common import FP, GRAD_LATER, MOM, READ, SIBCLS, SIBVAL, VRS, WV

L = []
BVP = "Bessemer Venture Partners"

# ---- dashlane
L.append(cls("dashlane", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2014-05-16", city="New York", focus="Security",
             rounds=[rnd("2014-05", "Series B", 22000000, BVP, True, None, "press")],
             note="Password manager, New York (founded in Paris). Bessemer led the $22M Series B of May 2014, the Form D round of that quarter and the firm's investment date (model, medium), so Growth. No priced round at $1B or more on record; the Sequoia and Thrive rows read below $1B as well."))

# ---- databand
DB_IBM = NEWS("databand", "IBM buys Israeli data observability")
L.append(cls("databand", status="acquired", rng="below_1b", stage="undetermined", entry_date="2019", country="IL",
             country_src=WV, country_cite=DB_IBM, city="Tel Aviv", focus="Data Infrastructure",
             rounds=[rnd("2020-12", "Series A", 14500000, "Accel", None, None, "press"),
                     rnd("2022-07-06", "Acquisition (IBM)", 150000000, "IBM", None, DB_IBM, "press")],
             note="Data observability, Tel Aviv; acq. by IBM, July 2022 (Globes: 'IBM buys Israeli data observability co Databand.ai for $150m'). The firm's listing dates its entry 2019, before the Series A that Accel led in 2020, and no page read names that round, so the stage is undetermined."))

# ---- databook
L.append(cls("databook", status="private", rng="below_1b", city="Palo Alto", city_src="formd_address", focus="SaaS",
             note="Sales intelligence platform, Palo Alto. The prefilled Growth agrees with the firm's own post (the $50M Series B of February 2022), which Pulse 2.0 put at a $550M valuation; no later priced round in Google News on 2026-10-01, so below $1B."))

# ---- datafy
DATAFY = NEWS("datafy", "Datafy Completes $20M Seed")
L.append(cls("datafy", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=DATAFY, stage_conf="high",
             entry_date="2025-07-10", grad="censored", country="IL", country_src=WV, country_cite=SITE("datafy"),
             city="Tel Aviv", focus="Data Infrastructure",
             rounds=[rnd("2024-04", "Seed", 6000000, "Insight Partners", None,
                         SIBCLS("insight-partners", "datafy", "entry_stage_citation"), "firm"),
                     rnd("2025-07-10", "Seed (completed at $20M)", 20000000, BVP, True, DATAFY, "company")],
             note="The company's release (2025-07-10): Bessemer led the round that completed the $20M seed, with Insight Partners, which led the first $6M in April 2024; the firm's listing reads 2024 and Tel Aviv. Entry after 2024-10-01 on either reading, so censored. "
                  + MOM + "no later round."))

# ---- datahub
DH = POST("bridging-the-ai-data-divide-with-datahub")
L.append(cls("datahub", status="private", rng="below_1b", stage="Growth", stage_src=FP, stage_cite=DH, stage_conf="high",
             entry_date="2025-05-21", country="US", city="San Francisco", focus="Data Infrastructure",
             rounds=[rnd("2023-06-22", "Series A", 21000000, None, False, None, "press"),
                     rnd("2025-05-21", "Series B", 35000000, BVP, True, DH, "firm")],
             note="The firm's own post (2025-05-21): 'Bessemer Venture Partners leads DataHub's $35 million Series B funding', its first round in the company (formerly Acryl Data), so Growth. "
                  + MOM + "no later round, none at $1B or more."))

# ---- datalot
L.append(cls("datalot", status="acquired", rng="below_1b", stage="undetermined", entry_date="2009", country="US",
             city="New York", focus="Media, Gaming & Advertising", rounds=[],
             note="Insurance customer acquisition marketplace, Brooklyn. The firm's listing gives Lightyear Capital as the acquirer, and Centerfield completed its acquisition of the company in August 2021 (GlobeNewswire). The listing dates the entry 2009, the founding year, and names no round; none found in Google News, so undetermined."))

# ---- deepl
DEEPL = POST("how-deepl-is-changing-communication")
DEEPL_V = SIBVAL("deepl", "atomico")
L.append(cls("deepl", status="private", rng="1b_plus", usd=2000000000, val_src=WV, val_cite=DEEPL_V, asof="2024-05-22",
             extra=VRS, flags=["stale"], stage="Growth", stage_src=FP, stage_cite=DEEPL, stage_conf="high",
             entry_date="2023-01-11", country="DE", country_src=WV,
             country_cite=NEWS("deepl", "Cologne AI translator DeepL"), city="Cologne", focus="AI & Applied AI",
             rounds=[rnd("2023-01-11", "Series B", None, None, True, DEEPL, "firm"),
                     rnd("2024-05-22", "round", 300000000, "Index Ventures", None, DEEPL_V, "company")],
             note="The firm's own post (2023-01-11): 'Bessemer's growth practice joins the Series B of DeepL', so Growth. Mark: the $300M round at $2B of May 2024, as the Atomico, ICONIQ and IVP rows carry it; Google News on 2026-10-01 shows staff cuts of a quarter in May 2026 and no new priced round, so stale."))

# ---- defcon-ai
DEFCON = POST("defcon-ai-transforming-military-logistics")
L.append(cls("defcon-ai", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=DEFCON,
             stage_conf="high", entry_date="2024-08-20", country="US", city="McLean", city_src=WV,
             focus="AI & Applied AI",
             rounds=[rnd("2024-08-20", "Seed", 44000000, BVP, True, DEFCON, "firm")],
             note="The firm's own post (2024-08-20): 'Bessemer Venture Partners leads DEFCON AI's $44 million Seed funding'; a McLean, Virginia startup incubated by Red Cell Partners (citybiz). "
                  + MOM + "no later round. " + GRAD_LATER))

# ---- defense-net
DN_W = W("Defense.Net")
L.append(cls("defense-net", status="acquired", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=DN_W,
             stage_conf="high", entry_date="2012-12-24", country="US", city="Belmont", focus="Security",
             rounds=[rnd("2012", "Series A", 9500000, BVP, True, DN_W, "press")],
             note="DDoS mitigation service, Belmont, California; acq. by F5 Networks, May 2014. Wikipedia: 'In 2012 Bessemer Venture Partners lead a Series A round of funding for a total of $9.5 million', the firm's 2012 entry."))

# ---- delivery-agent
L.append(cls("delivery-agent", status="defunct", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             note="Shoppable television commerce, San Francisco. It filed for Chapter 11 in September 2016 (Variety) and no continuing business was found; the firm's exit year is 2017, so defunct. The firm's investment date is 2006-05-11, so the prefilled entry date is a later Form D; the Growth band is left as it stands."))

# ---- demostack
DEMO = POST("perspective-optimizing-software-sales-with-product-demo")
L.append(cls("demostack", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=DEMO,
             stage_conf="high", entry_date="2021-03", country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2021-03", "Series A", None, None, True, DEMO, "firm"),
                     rnd("2022-04-19", "Series B", 34000000, "Tiger Global", None,
                         NEWS("demostack", "Demostack raises $34 million Series B"), "press")],
             note="The firm's own post: 'In March of 2021, we made a Series A investment in Demostack'. Product demo platform with headquarters in San Francisco and R&D in Tel Aviv; the newest round is the $34M Series B of April 2022 (Calcalist), no priced round at $1B or more in Google News on 2026-10-01."))

# ---- devo
DEVO = NEWS("devo", "Raises $60M Series D")
L.append(cls("devo", stage="Growth", stage_src=WV, stage_cite=DEVO, stage_conf="high", entry_date="2020-09-16",
             country="US", city="Cambridge", focus="Security", flags=["model_disputes_source"],
             rounds=[rnd("2017-09", "Series B", 35000000, "Insight Venture Partners", False,
                         SIBCLS("insight-partners", "devo", "entry_stage_citation"), "firm"),
                     rnd("2020-09-16", "Series D", 60000000, "Georgian", True, DEVO, "press"),
                     rnd("2021-10", "Series E", 250000000, "TCV", None, SIBVAL("devo", "tcv"), "press")],
             note="Crunchbase News (2020-09-16): the $60M Series D, led by Georgian, with Bessemer joining beside Insight; the firm's 2020 entry, so Growth. The Cambridge, Massachusetts company (formerly Logtrust, founded in Spain) is US-headquartered, as the Insight and TCV rows have it, so the prefilled ES is replaced."))

# ---- dinii
DINII = NEWS("dinii", "secures $48M in Series B")
L.append(cls("dinii", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=DINII,
             stage_conf="high", entry_date="2024-09-27", country="JP", country_src=WV, country_cite=DINII,
             city="Tokyo", focus="SaaS",
             rounds=[rnd("2024-09-27", "Series B", 48000000, "Bessemer Venture Partners and Hillhouse Investment", True, DINII, "press")],
             note="BRIDGE (2024-09-27): Tokyo-based Dinii's $48M Series B 'was led by U.S.-based Bessemer Venture Partners and Hillhouse Investment Management', the firm's first investment in Japan, so Growth. No later round in Google News on 2026-10-01."))

# ---- disco: the same company as cs-disco-inc
L.append(cls("disco", status="public", rng="below_1b", usd=267470000, val_src=WV, val_cite=READ["law-cap"],
             asof="2026-10-01", extra=VRS, stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2014-11-12", country="US", city="Austin", focus="SaaS",
             rounds=[rnd("2014-11", "Series A", 10000000, BVP, True, None, "press")],
             note="The same company as the row cs-disco-inc (CS Disco, Inc., NYSE: LAW), which carries the filings: two rows, one company. Bessemer led the $10M Series A of November 2014, when Bob Goodman joined the board (model, medium; the Form D band on the other row agrees). Market cap $267.5M on 2026-10-01 (stockanalysis.com); the Felicis and General Catalyst rows named DISCO read as another, private company."))

# ---- discord
L.append(cls("discord", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020",
             city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2020-06", "Series H", 100000000, "Index Ventures", None, None, "press"),
                     rnd("2020-12", "round", 100000000, "Greenoaks Capital", None, None, "press"),
                     rnd("2021-09", "round", 500000000, "Dragoneer", None, SIBVAL("discord", "ivp"), "press")],
             note="The firm's listing dates its entry 2020, when Discord's rounds were the $100M Series H of June and the December round at $7B; either reads Growth (model, medium), and no page read names the firm in one of them. Mark and city as the sibling books; Google News on 2026-10-01 shows an IPO filing and no listing yet."))

# ---- distil-networks
L.append(cls("distil-networks", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2015-06-18", city="San Francisco", focus="Security",
             rounds=[rnd("2015-08", "Series B", 21000000, BVP, True, None, "press")],
             note="Bot detection and mitigation, San Francisco (the Form D's Arlington, Virginia was the earlier address); acq. by Imperva, 2019 (ZDNET). Bessemer led the $21M Series B of 2015, the firm's investment date being 2015-06-18 (model, medium), so Growth; the prefilled 2016 date was a later Form D."))

# ---- dlthub: the 2023 Form D seat was Foundation Capital's (D6); the firm entered at the 2025 seed
DLT = POST("meet-the-founders-of-dlthub")
DLT_TC = NEWS("dlthub", "Can dltHub solve the Python library problem")
L.append(cls("dlthub", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=DLT, stage_conf="high",
             entry_date="2025-11-03", grad="censored", country="DE", country_src=WV, country_cite=DLT_TC,
             city="Berlin", focus="Data Infrastructure", flags=["model_disputes_source"],
             rounds=[rnd("2023-07-20", "Pre-Seed", 1500000, "Dig Ventures", False, DLT_TC, "press"),
                     rnd("2023-12-14", "round (Form D)", 4850000, None, False, None, "filing"),
                     rnd("2025-11-03", "Seed", 8000000, BVP, True, DLT, "firm")],
             note="The firm's own post (2025-11-03): 'Bessemer Venture Partners leads dltHub's $8 million seed round'. The 2023 Form D behind the prefilled date names Lauri Moore while she was at Foundation Capital (the firm's post on her arrival in July 2024 credits dltHub to that firm), so the seat predates Bessemer (decisions.md D6) and the entry is the 2025 round: censored. Berlin-based (TechCrunch, 2023-07-20); the Form D's Delaware address is a registered agent's."))

# ---- docent-health
L.append(cls("docent-health", status="acquired", rng="below_1b", city="Cambridge", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Patient experience platform, Cambridge, Massachusetts; acq. by GetWellNetwork, January 2021 (Fierce Healthcare). The firm's own post says it led the Series A, which agrees with the prefilled band; its investment date is 2015-11-06, before the 2016 Form D."))

# ---- docusign
L.append(cls("docusign", rng="10b_plus", usd=12810000000, val_src=WV, val_cite=SIBVAL("docusign", "kleiner-perkins"),
             asof="2026-10-01", extra=VRS, stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2011-07-01", country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2010-12", "Series D", 27000000, None, None, None, "press"),
                     rnd("2012-07", "Series E", 47500000, "Kleiner Perkins", None, None, "press")],
             note="The firm's listing dates its investment 2011-07-01, between the Series D of December 2010 and the Series E of 2012, and the S-1 holder table shows a small Bessemer position (700,000 shares); an entry at that point reads Growth (model, medium), though no page read names the round. Market cap $12.81B on 2026-10-01 (stockanalysis.com), in line with the sibling books."))

# ---- docutap: the band read a 2014 follow-on; the firm entered at the 2013 round
L.append(cls("docutap", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2013-04-25", city="Sioux Falls", city_src="formd_address", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2012", "round (Form D)", 6250000, None, None, None, "filing"),
                     rnd("2013-04", "round (Form D)", 11900000, None, True, None, "filing"),
                     rnd("2016-05-04", "majority sale (Warburg Pincus)", None, "Warburg Pincus", None,
                         NEWS("docutap", "Global firm acquires majority stake"), "press")],
             note="Urgent care EMR, Sioux Falls; Warburg Pincus bought a majority in 2016 (Argus Leader) and the company merged with Practice Velocity into Experity in 2019, so acquired. The firm's investment date is 2013-04-25, which matches the company's $11.9M Form D round of 2013 Q2, its third filed round after two in 2012; so the entry reads Growth (model, medium), not the Seed the band read off the $3.0M filing of 2014."))

# ---- dome-systems
DOME = POST("dome-systems-the-operational-control-plane")
L.append(cls("dome-systems", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=DOME,
             stage_conf="high", entry_date="2026-04-16", grad="censored", country="US", city="Menlo Park",
             focus="AI & Applied AI",
             rounds=[rnd("2026-04-16", "Seed", None, BVP, True, DOME, "firm")],
             note="The firm's own post (2026-04-16): 'Bessemer Venture Partners co-leads Dome Systems' seed round'; Menlo Park as on the Redpoint row. Entry after 2024-10-01, so censored. "
                  + MOM + "no later round."))

# ---- dominion-dynamics
DOM = POST("dominion-dynamics-forging-the-future")
DOM_A = NEWS("dominion-dynamics", "lands $139-million Series A")
L.append(cls("dominion-dynamics", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=DOM,
             stage_conf="high", entry_date="2026-01-19", grad="graduated", grad_src=WV, grad_cite=DOM_A,
             grad_conf="high", country="CA", country_src=WV, country_cite=DOM_A, city="Ottawa",
             focus="Industrial & Robotics",
             rounds=[rnd("2026-01-19", "Seed", 15200000, "Georgian", True, DOM, "firm"),
                     rnd("2026-06-30", "Series A", 100000000, "Georgian", True, DOM_A, "press")],
             note="The firm's own post (2026-01-19): 'Bessemer Venture Partners co-leads Dominion Dynamics' $20M CAD Seed'. BetaKit (2026-06-30): the Ottawa company 'secured $139 million CAD ($100 million USD) in Series A financing', with Bessemer following on, so graduated inside the window; Resilience Media put that round at a $400M valuation, below $1B."))

# ---- doppel
DOP = POST("backing-doppel-architecting-trust")
DOP2 = POST("doubling-down-on-doppel")
L.append(cls("doppel", status="private", rng="below_1b", stage="Growth", stage_src=FP, stage_cite=DOP, stage_conf="high",
             entry_date="2025-05-02", city="San Francisco", focus="Security",
             rounds=[rnd("2025-05-02", "Series B", 35000000, BVP, True, DOP, "firm"),
                     rnd("2025-11-19", "Series C", 70000000, BVP, True, DOP2, "firm")],
             note="The firm's own posts: it led the $35M Series B (2025-05-02) and the $70M Series C six months later, so the entry is the Series B and the date is corrected from the November Form D; Growth as prefilled. Fortune (2025-11-19) put the Series C at more than $600M, below $1B, and Google News on 2026-10-01 shows no later round."))

jl.write("j02c", L)
