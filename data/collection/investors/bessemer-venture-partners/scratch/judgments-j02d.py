"""Judge j02, part d (PRO-80 Bessemer Venture Partners, batch 4: doubleai .. fandom), 2026-10-01.
Rows are members on the firm's own listing; classification lines only. Run as NQ_TAG=j02 python3 judgments-j02d.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "scratchpad" / "j02"))
import judge_lib as jl
from judge_lib import ARCH, NEWS, POST, SITE, W, cls, rnd
from common import FP, GRAD_LATER, MOM, READ, SIBCLS, SIBVAL, VRS, WV

L = []
BVP = "Bessemer Venture Partners"

# ---- doubleai
DAI = READ["doubleai-memo"]
DAI_V = NEWS("doubleai", "From Mobileye to doubleAI")
L.append(cls("doubleai", status="private", rng="1b_plus", usd=1000000000, val_src=WV, val_cite=DAI_V, asof="2026-07-26",
             extra=VRS, stage="Series A", stage_src=WV, stage_cite=DAI, stage_conf="medium", entry_date="2025",
             country="IL", country_src=WV, country_cite=DAI, city="Tel Aviv", focus="AI & Applied AI",
             rounds=[rnd("2025", "Series A", 200000000, "Lightspeed Venture Partners and Bessemer Venture Partners", True, DAI, "press")],
             note="A published memo on the round (Illai Gescheit): 'doubleAI raised its $200 million Series A co-led by Lightspeed Venture Partners and Bessemer Venture Partners', valuing the Tel Aviv company at over $1B; the stage rests on that one secondary source (medium). Calcalist (2026-07-26) reports the money raised 'at a valuation exceeding $1 billion': the figure recorded is that floor, on the band edge, since no exact valuation is published."))

# ---- doubledutch
L.append(cls("doubledutch", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2013-09-09", city="San Francisco", focus="SaaS",
             rounds=[rnd("2013-09", "Series C", 10000000, BVP, True, None, "press"),
                     rnd("2014-08", "Series D", 19000000, "Index Ventures", True, None, "press"),
                     rnd("2015-08", "Series E", 45000000, "KKR", True, None, "press")],
             note="Event app software, San Francisco; acq. by Cvent, June 2019 (Pulse 2.0). The firm's investment date is 2013-09-09: the $10M Series C of September 2013, which preceded the Series D of 2014 and the Series E of 2015 that the Form Ds show (model, medium), so Growth; the prefilled 2014 date was the Series D filing."))

# ---- drivenets
DN = POST("drivenets-the-ai-networking-fabric")
DN_V = NEWS("drivenets", "DriveNets raises $410 million as AI boom")
DN_W = W("DriveNets")
L.append(cls("drivenets", rng="1b_plus", usd=8500000000, val_src=WV, val_cite=DN_V, asof="2026-06-01", extra=VRS,
             stage="Series A", stage_src=FP, stage_cite=DN, stage_conf="high", entry_date="2019",
             country="IL", country_src=WV, country_cite=DN_V, city="Ra'anana", focus="Data Infrastructure",
             rounds=[rnd("2019", "Series A", 110000000, "Bessemer Venture Partners and Pitango Growth", True, DN_W, "press"),
                     rnd("2021", "Series B", 208000000, "D1 Capital Partners", True, DN_W, "press"),
                     rnd("2022-08", "Series C", 262000000, "D2 Investments", True, DN_W, "press"),
                     rnd("2026-06-01", "Series D", 410000000, "Bessemer Venture Partners and Atreides Management", True, DN_V, "press")],
             note="The firm's own post (2026-06-01): it leads the $410M Series D of 'a company we've backed since their Series A', the $110M round of 2019. Calcalist (2026-06-01): the round values the Israeli networking company at $8.5B, which supersedes the prefilled $2.5B; IL confirmed."))

# ---- dronedeploy
DD = NEWS("dronedeploy", "announces $35M Series D led by Bessemer")
L.append(cls("dronedeploy", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=DD,
             stage_conf="high", entry_date="2019-11-13", country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2019-11-13", "Series D", 35000000, BVP, True, DD, "company")],
             note="The company's release (San Francisco, 2019-11-13): 'it closed a $35 million Series D round led by Bessemer Venture Partners', a new investor beside the existing ones, so Growth. No priced round at $1B or more in Google News on 2026-10-01."))

# ---- dropcam
DROP = POST("memos/dropcam")
DROP_W = W("Dropcam")
L.append(cls("dropcam", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=DROP, stage_conf="high",
             entry_date="2009-02-18", grad="graduated", grad_src=WV, grad_cite=DROP_W, grad_conf="high",
             city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2009-02-18", "Seed", None, None, True, DROP, "firm"),
                     rnd("2012-06", "round", 12000000, "Menlo Ventures", None, DROP_W, "press"),
                     rnd("2013", "round", 30000000, "Institutional Venture Partners", None, DROP_W, "press")],
             note="The firm's own memo (2009-01-30): 'We recommend a $200k seed investment in Dropcam'; the investment date is 2009-02-18. Wikipedia: $12M led by Menlo Ventures in June 2012 and $30M led by IVP the following year, later priced rounds many times the seed, so graduated. Acq. by Google, 2014 ($555M)."))

# ---- dynamic-yield
L.append(cls("dynamic-yield", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2013-02-21", city="Tel Aviv", focus="SaaS",
             rounds=[rnd("2013-02", "Series A", 1700000, BVP, True, None, "press"),
                     rnd("2019-03-26", "Acquisition (McDonald's)", 300000000, "McDonald's", None,
                         NEWS("dynamic-yield", "Acquires Dynamic Yield for $300M"), "press")],
             note="Personalization software, Tel Aviv and New York; acq. by McDonald's, 2019 (over $300M), and sold on to Mastercard. Bessemer led the $1.7M Series A of February 2013, the firm's investment date (model, medium)."))

# ---- easebuzz
EB = POST("supercharging-indias-digital-payments")
L.append(cls("easebuzz", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=EB,
             stage_conf="high", entry_date="2025-04-16", country="IN", country_src=WV, country_cite=EB, city="Pune",
             focus="Fintech & Payments",
             rounds=[rnd("2025-04", "Series A", 30000000, BVP, True, EB, "firm")],
             note="The firm's own post (2025-04-16): 'Bessemer Venture Partners leads Easebuzz's $30 million Series A funding', on India's digital payments; Pune (IN confirmed). "
                  + MOM + "talks in March 2026 at a valuation of over $250M (Entrepreneur India), no priced round at $1B or more."))

# ---- eave
L.append(cls("eave", status="acquired", rng="below_1b", city="New York", focus="Fintech & Payments",
             note="Digital mortgage lender, New York (the Form D gives Brooklyn); acq. by HomeLight, July 2019 (HousingWire). The prefilled Series A band is left as it stands; the firm's investment date is 2016-01-20."))

# ---- eeye-digital-security
L.append(cls("eeye-digital-security", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004-05-25",
             country="US", city="Irvine", focus="Security", rounds=[],
             note="Vulnerability management software, Orange County, California (Irvine as on the Insight row); acq. by BeyondTrust, 2012 (the firm's listing). The firm's listing dates its investment 2004-05-25 and names no round; none found in Google News, so undetermined."))

# ---- electric
EL = POST("bessemer-promotes-andrew-hedin-mike-droesch")
EL_V = READ["electric-d1"]
L.append(cls("electric", status="private", rng="1b_plus", usd=1000000000, val_src=WV, val_cite=EL_V, asof="2022-03-29",
             extra=VRS, flags=["stale"], stage="Series A", stage_src=FP, stage_cite=EL, stage_conf="high",
             entry_date="2018-03-30", city="New York", focus="SaaS",
             rounds=[rnd("2018", "Series A", 9300000, BVP, True, EL, "firm"),
                     rnd("2021-10-19", "Series D", 90000000, None, True, EL_V, "company"),
                     rnd("2022-03-29", "Series D-1", 20000000, "Harmonic Growth Partners", None, EL_V, "company")],
             note="The firm's own post (2019-07-16): Mike Droesch 'sourced and championed our Series A investment in automated IT support provider, Electric', announced 2018-03-30; the prefilled 2016 date was an earlier Form D. Mark: the company's own release on the $20M Series D-1 of 2022-03-29 at a $1B valuation, on the band edge; no priced round found since, so stale."))

# ---- eliseai
ELISE = POST("building-the-backbone-of-operational-excellence")
ELISE2 = POST("eliseai-deepens-vertical-operations")
ELISE_V = NEWS("eliseai", "EliseAI Raises $350M at $4B Valuation to Expand AI Automation Platform")
L.append(cls("eliseai", status="private", rng="1b_plus", usd=4000000000, val_src=WV, val_cite=ELISE_V,
             asof="2026-09-29", extra=VRS, stage="Growth", stage_src=FP, stage_cite=ELISE, stage_conf="high",
             entry_date="2025-08-20", city="New York", focus="AI & Applied AI",
             rounds=[rnd("2025-08-20", "Series E", 250000000, "a16z", True, ELISE, "firm"),
                     rnd("2026-09-28", "round", 350000000, "a16z and Bessemer Venture Partners", True, ELISE2, "firm")],
             note="The firm's own post (2025-08-20): 'Bessemer Venture Partners joins EliseAI's $250M Series E', so Growth. Mark: the $350M round the firm co-led in September 2026 at a $4B valuation (citybiz, 2026-09-30), fresher than the $2.2B of August 2025 on the a16z row."))

# ---- eloqua
L.append(cls("eloqua", status="acquired", rng="below_1b", stage="undetermined", entry_date="2007-09-27", country="US",
             city="Vienna", focus="SaaS", rounds=[],
             note="Marketing automation, Vienna, Virginia (founded in Toronto); listed in August 2012 and acq. by Oracle, closed 2013. Byron Deeter joined the board in September 2007 (the S-1), the firm's investment date; no page read names that round, so undetermined."))

# ---- endgame
L.append(cls("endgame", status="acquired", rng="below_1b", city="Arlington", focus="Security",
             note="Endpoint security, Arlington, Virginia; acq. by Elastic, 2019. The prefilled Series A agrees with Wikipedia: the $29M round of October 2010 from Bessemer, Columbia Capital, Kleiner Perkins and TechOperators preceded the named Series B of 2013. The a16z and EQT Ventures rows named Endgame are another company."))

# ---- enjoei: the band read a Seed; the record names no round and it was not the first institutional one
LAVCA = READ["enjoei-lavca"]
L.append(cls("enjoei", status="public", rng="below_1b", stage="undetermined", country="BR", country_src=WV,
             country_cite=LAVCA, city="Sao Paulo", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2013", "round (R$7M)", None, "Monashees", False, LAVCA, "press"),
                     rnd("2014-12-19", "round (R$18M)", 7046246, BVP, True, LAVCA, "press")],
             note="Second-hand fashion marketplace, Sao Paulo; listed on B3 in November 2020 (ENJU3), a small cap on 2026-10-01 (stockanalysis.com), so below $1B. LAVCA (2014-12-19): an investment of R$18M 'liderado pelo fundo de investimentos Bessemer Venture Partners', after Monashees' R$7M of 2013; the record names no round and it was not the first institutional one, so the prefilled Seed band is replaced by undetermined."))

# ---- entropik
ENT = NEWS("entropik", "raises $25 million in Series B funding round led by Bessemer")
L.append(cls("entropik", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=ENT,
             stage_conf="high", entry_date="2023-02-08", country="IN", country_src=WV, country_cite=SITE("entropik"),
             city="Bangalore", focus="AI & Applied AI",
             rounds=[rnd("2023-02-08", "Series B", 25000000, "Bessemer Venture Partners and SIG Venture Capital", True, ENT, "company")],
             note="The company's release (Business Wire, 2023-02-08): Entropik 'raises $25 million in Series B funding round led by Bessemer Venture Partners and SIG Venture Capital', the firm's 2023 entry on its India list, so Growth. "
                  + MOM + "no later round."))

# ---- epix-pharmaceuticals
L.append(cls("epix-pharmaceuticals", status="defunct", rng="below_1b", stage="undetermined", entry_date="1993",
             country="US", city="Lexington", focus="Healthcare & Bio", rounds=[],
             note="MRI imaging agents (EPIX Medical, later EPIX Pharmaceuticals), Lexington, Massachusetts; listed in 1997 and in asset liquidation by July 2009 (Wikipedia), so defunct. The firm's archived listing says only that 'BVP participated in its early rounds' from 1993, which names no round, so undetermined."))

# ---- evenup
EU = POST("evenup-providing-equal-access-to-justice")
EU_V = NEWS("evenup", "EvenUp Raises $150M Series E at $2B+")
L.append(cls("evenup", status="private", rng="1b_plus", usd=2000000000, val_src=WV, val_cite=EU_V, asof="2025-10-07",
             extra=VRS, stage="Growth", stage_src=FP, stage_cite=EU, stage_conf="high", entry_date="2023-06-08",
             country="US", city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2023-06-08", "Series B", 50500000, BVP, True, EU, "firm"),
                     rnd("2025-10-07", "Series E", 150000000, None, None, EU_V, "company")],
             note="The firm's own post (2023-06-08): 'Bessemer Venture Partners' Growth team leads EvenUp's $50.5 million Series B financing', so Growth. Mark: the $150M Series E at $2B of October 2025 (the company's release), as the Bain Capital Ventures and Lightspeed rows carry it; no later priced round in Google News on 2026-10-01."))

# ---- everlance
L.append(cls("everlance", rng="below_1b", stage="undetermined", entry_date="2021", city="San Francisco", focus="SaaS",
             rounds=[],
             note="Mileage and expense tracking, San Francisco; acq. by Motus, February 2025 (Motus's release). The firm's listing dates its entry 2021 and no release names the round; none found in Google News, so undetermined."))

# ---- eye-security
EYE = POST("eye-security-is-safeguarding-european")
L.append(cls("eye-security", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=EYE,
             stage_conf="high", entry_date="2022-11-16", country="NL", country_src=WV, country_cite=EYE,
             city="The Hague", focus="Security",
             rounds=[rnd("2022-11-16", "Series A (EUR 17M)", None, BVP, True, EYE, "firm"),
                     rnd("2024-03-13", "Series B (EUR 36M)", None, None, None, NEWS("eye-security", "Eye Security Raises €36M"), "press"),
                     rnd("2026-06-30", "Series C (EUR 60M)", None, "Sofina", True, NEWS("eye-security", "Eye Security raises €60m Series C"), "press")],
             note="The firm's own post (2022-11-16): 'Bessemer Venture Partners leads the EUR 17 million Series A in Eye Security, the Netherlands-based startup'; The Hague. The EUR 60M Series C of June 2026 led by Sofina (FinTech Global) publishes no valuation, so below $1B."))

# ---- fabric-technologies
FAB = NEWS("fabric-technologies", "Fabric nabs $2.5m")
FAB_A = NEWS("fabric-technologies", "Fabric Raises $10M")
L.append(cls("fabric-technologies", status="acquired", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=FAB,
             stage_conf="high", entry_date="2017-03-23", grad="graduated", grad_src=WV, grad_cite=FAB_A,
             grad_conf="high", country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2017-03-23", "Seed", 2500000, BVP, True, FAB, "press"),
                     rnd("2018-06", "Series A", 10000000, BVP, True, FAB_A, "press"),
                     rnd("2022-01-12", "Acquisition (Western & Southern)", None, "Western & Southern Financial Group", None,
                         NEWS("fabric-technologies", "Sews Up Fabric"), "press")],
             note="FinTech Global (2017-03-23): '$2.5m in a Seed round led by Bessemer Venture Partners' (the firm's listing reads 2016); FinSMEs (June 2018): a $10M Series A led by Bessemer, so graduated. Acq. by Western & Southern Financial Group (ThinkAdvisor, January 2022; the firm's page says 2021); the six sibling rows named Fabric are other companies."))

# ---- fal-ai
FAL = POST("fal-is-powering-the-generative-media")
FAL_V = NEWS("fal-ai", "Fal lands $140M at $4.5B")
L.append(cls("fal-ai", status="private", rng="1b_plus", usd=4500000000, val_src=WV, val_cite=FAL_V, asof="2025-12-09",
             extra=VRS, stage="Growth", stage_src=FP, stage_cite=FAL, stage_conf="high", entry_date="2025-02-12",
             country="US", city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2025-02-12", "Series B", 49000000, None, True, FAL, "firm"),
                     rnd("2025-07-31", "Series C", 125000000, "Meritech", None, None, "press"),
                     rnd("2025-12-09", "Series D", 140000000, "Sequoia", None, FAL_V, "press")],
             note="The firm's own post (2025-02-12): 'Bessemer Venture Partners joins fal's $49 million Series B', so Growth. Mark: the $140M Series D led by Sequoia at $4.5B (Tech Funding News, December 2025); no later priced round in Google News on 2026-10-01."))

# ---- fandom
FAN_W = W("Fandom (website)")
L.append(cls("fandom", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2006", country="US", city="San Francisco", focus="Media, Gaming & Advertising",
             rounds=[rnd("2006", "Series A", 4000000, "Bessemer Venture Partners and First Round Capital", True, FAN_W, "press"),
                     rnd("2006-12", "Series B", 10000000, "Amazon", None, FAN_W, "press"),
                     rnd("2012-11", "Series C", 10800000, "Institutional Venture Partners", True, FAN_W, "press")],
             note="Wikipedia: Wikia 'announced a US$4 million venture capital investment from Bessemer Venture Partners and First Round Capital' in 2006, nine months before Amazon's named Series B, so the firm's entry is the Series A (model, medium, the page does not use the name). Acq. by TPG, 2018; the Redpoint row named Fandom is the 1999 portal, another company."))

jl.write("j02d", L)
