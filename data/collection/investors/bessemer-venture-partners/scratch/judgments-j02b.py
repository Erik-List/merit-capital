"""Judge j02, part b (PRO-80 Bessemer Venture Partners, batch 3: clear-ballot .. dashbot), 2026-10-01.
Rows are members on the firm's own listing; classification lines only. Run as NQ_TAG=j02 python3 judgments-j02b.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "scratchpad" / "j02"))
import judge_lib as jl
from judge_lib import ARCH, NEWS, POST, W, cls, rnd
from common import FP, GRAD_LATER, MOM, READ, SIBCLS, VRS, WV

L = []
BVP = "Bessemer Venture Partners"

# ---- clear-ballot
L.append(cls("clear-ballot", status="private", rng="below_1b", stage="undetermined", entry_date="2017-05-25",
             country="US", city="Boston", focus="SaaS", rounds=[],
             note="Voting system software (ClearVote), Boston; the company's site still answers. The firm's listing dates its investment 2017-05-25 and names no round, and Google News carries no report of it, so the stage is undetermined."))

# ---- coder
L.append(cls("coder", status="private", rng="below_1b", stage="undetermined", entry_date="2019", country="US",
             city="Austin", focus="DevTools & APIs",
             rounds=[rnd("2026-04-01", "Series C", 90000000, "KKR", None,
                         NEWS("coder", "Coder Raises $90M Series C Led by KKR"), "press")],
             note="Cloud development environments, Austin. The firm's listing dates its entry 2019 and no release read names Bessemer in a round (the Redpoint row cites the 2019 seed), so the stage is undetermined. The $90M Series C of April 2026 led by KKR publishes no valuation, so below $1B."))

# ---- contractbook: the band read a Seed; the documented entry is the Series A the firm led
AL = NEWS("contractbook", "Contractbook Bags")
L.append(cls("contractbook", status="acquired", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=AL,
             stage_conf="high", entry_date="2020-12-09", city="Copenhagen", focus="SaaS",
             flags=["stage_disputes_band"],
             rounds=[rnd("2019", "Seed", 3900000, "Gradient Ventures", False, AL, "press"),
                     rnd("2020-12-09", "Series A", 9400000, BVP, True, AL, "press"),
                     rnd("2021-05-11", "Series B", 30000000, "Tiger Global", None,
                         NEWS("contractbook", "Contractbook raises $30m Series B"), "press"),
                     rnd("2025-06", "Acquisition (Scrive)", None, "Scrive", None,
                         SIBCLS("tiger-global-management", "contractbook", "hq_country_citation"), "press")],
             note="Artificial Lawyer (2020-12-09): 'a $9.4m Series A investment round, led by Bessemer Venture Partners' with existing investors including Gradient Ventures, which led the earlier $3.9M seed; so the entry is the Series A, not the Seed the Form D band read. Acq. by Scrive, 2025 (Borsen, as the Tiger Global row cites it)."))

# ---- converge-bio
L.append(cls("converge-bio", status="private", rng="below_1b", city="Boston", focus="Healthcare & Bio",
             note="Generative AI for drug discovery, Boston and Tel Aviv; the Form D's Delaware address is a registered agent's. The prefilled Series A agrees with the press: Bessemer led the $25M Series A of January 2026 (Tech in Asia, TechCrunch), after a $5.5M seed in November 2024. No priced round at $1B or more in Google News on 2026-10-01."))

# ---- convertro-inc
L.append(cls("convertro-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2009-09-25",
             country="US", city="Santa Monica", focus="SaaS", rounds=[],
             note="Marketing attribution software, Santa Monica; acq. by AOL, 2014 (AdExchanger: $101M). The firm's listing dates its investment 2009-09-25, the company's founding year, and names no round; none found in Google News, so undetermined."))

# ---- copilotiq
L.append(cls("copilotiq", status="private", rng="below_1b", stage="undetermined", entry_date="2022", country="US",
             city="Nashville", city_src=WV, focus="Healthcare & Bio", rounds=[],
             note="In-home chronic care for Medicare members. It merged with Biofourmis in October 2024 (Business Wire, Fierce Healthcare) and still operates as CopilotIQ, Inc., Nashville (its own site, read 2026-10-01). No release read names the round the firm joined in 2022, so the stage is undetermined; no priced round at $1B or more for the combined company."))

# ---- cornerstone-ondemand
L.append(cls("cornerstone-ondemand", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2007-05-10", city="Santa Monica", focus="SaaS",
             rounds=[rnd("2007-05", "Series D", 32000000, None, True, None, "press")],
             note="Talent management software, Santa Monica; listed in March 2011, acq. by Clearlake Capital, 2021 ($5.2B, TechTarget). The firm's investment date is 2007-05-10, the month Byron Deeter joined the board (the S-1): the $32M Series D of 2007 (model, medium), so Growth. The prefilled 2010 date was a later Form D."))

# ---- courier: the prefilled status is a name match on another Courier
COURIER = POST("courier-a-single-api-for-managing")
L.append(cls("courier", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=COURIER,
             stage_conf="high", entry_date="2020-09-14", country="US", city="San Francisco", focus="DevTools & APIs",
             flags=["model_disputes_source"],
             rounds=[rnd("2020-09-14", "Series A", 10000000, BVP, True, COURIER, "firm"),
                     rnd("2022-06-22", "Series B", 35000000, "GV", True, NEWS("courier", "Courier lands $35M"), "press")],
             note="The firm's own post (2020-09-14): 'we're excited to lead the $10 million Series A investment in Courier', having hesitated when it first met the company in 2019. The prefilled acquired status is a name match on another Courier: the company operates (its site answers) and the GV and Y Combinator rows read private; no priced round at $1B or more."))

# ---- cpower-inc
L.append(cls("cpower-inc", status="acquired", rng="below_1b", country="US", city="New York", focus="Climate & Energy",
             note="Demand response provider, New York at the time; acq. by Constellation Energy, 2010 (the firm's listing), and sold on since (NRG bought it from LS Power in 2025). The firm's investment date is 2007-09-24, so the prefilled band and entry date rest on a 2009 Form D, a later round; no page read names the 2007 round."))

# ---- crash-override
L.append(cls("crash-override", status="private", rng="below_1b", city="New York", city_src="formd_address",
             focus="Security",
             note="Software supply chain security, New York. The Form D layer reads the 2025 filing as a later round, but AlleyWatch (2025-07-16, cited on the GV row) reports $28M of seed funding raised in closes, so the later filings may be closes of the seed. "
                  + GRAD_LATER))

# ---- cri
IPA_CRI = NEWS("cri", "CRI Secures Strategic Growth Investment")
L.append(cls("cri", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=IPA_CRI,
             stage_conf="medium", entry_date="2024-11-18", country="US", city="Enterprise",
             extra={"focus": None},
             rounds=[rnd("2024-11-18", "strategic growth investment", None, "Centerbridge Partners", True, IPA_CRI, "press")],
             note="Carr, Riggs & Ingram, an accounting firm in Enterprise, Alabama: outside the focus taxonomy. Inside Public Accounting (2024-11-18): a strategic growth investment from Centerbridge Partners with Bessemer as co-investor, under an alternative practice structure; no source read says the investors took control, so the row stays a member and reads Growth."))

# ---- criteo
CRITEO_W = W("Criteo")
L.append(cls("criteo", rng="below_1b", usd=810910000, val_src=WV, val_cite=READ["criteo-cap"], asof="2026-10-01",
             extra=VRS, flags=["model_disputes_source"], stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2010-04-26", country="FR", country_src=WV, country_cite=CRITEO_W, city="Paris",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2010-05", "Series C", 7000000, BVP, True, CRITEO_W, "press")],
             note="Wikipedia: 'In May 2010, Criteo raised a further $7 million of funding from Bessemer Venture Partners', the third institutional round after 2006 and 2008: the Series C (model, medium), so Growth; headquartered in Paris (FR confirmed). Market cap $810.9M on 2026-10-01 (stockanalysis.com), so the prefilled $1.25B band drops to below $1B."))

# ---- crosschq
XQ = READ["crosschq-seed"]
L.append(cls("crosschq", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=XQ, stage_conf="high",
             entry_date="2019-08-07", country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2019-08-07", "Seed", 4100000, "GGV Capital", True, XQ, "company")],
             note="The company's release (San Francisco, 2019-08-07): 'its seed round led by GGV Capital, with participation from Bessemer Venture Partners', $4.1M. The company renamed itself Brilliant AI in September 2026 (Dealroom). "
                  + GRAD_LATER))

# ---- cs-disco-inc
L.append(cls("cs-disco-inc", city="Austin",
             note="Legal technology, Austin (the Form D's Houston was the 2014 address). The row disco is the same company (NYSE: LAW) under the name the firm's site uses."))

# ---- ctera
L.append(cls("ctera", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2014", country="IL", country_src=WV,
             country_cite=NEWS("ctera", "CTERA Networks raises $25m"), city="Petah Tikva", focus="Data Infrastructure",
             rounds=[rnd("2014-07", "Series C", 25000000, BVP, True, None, "press"),
                     rnd("2016-09-13", "round", 25000000, None, None, NEWS("ctera", "CTERA Networks raises $25m"), "press"),
                     rnd("2024-07-17", "round, mostly secondary", 80000000, None, None, NEWS("ctera", "CTERA bags $80 million"), "press")],
             note="Hybrid cloud file storage, Petah Tikva and New York (Globes: 'Israeli cloud storage co'). Bessemer led the $25M Series C of July 2014, the firm's own year (model, medium), so Growth. The $80M round of July 2024 was mostly secondary (Calcalist) and publishes no $1B valuation."))

# ---- current: Crete Professionals Alliance, renamed
IPA_CRETE = NEWS("current", "Crete Professionals Alliance Raises Capital")
L.append(cls("current", status="private", rng="below_1b", stage="undetermined", entry_date="2024-05-02", country="US",
             city="Tampa", flags=["model_disputes_source"], extra={"focus": None},
             rounds=[rnd("2024-05-02", "strategic capital round (unnamed)", None, "Thrive Capital and Bessemer Venture Partners", True, IPA_CRETE, "press")],
             note="Accounting firm platform, Tampa, founded as Crete Professionals Alliance and renamed Current in June 2026 (Business Wire): outside the focus taxonomy. Inside Public Accounting (2024-05-02): 'strategic capital in a round led by Thrive Capital and Bessemer Venture Partners', which names no round, so the stage is undetermined. The prefilled JP and the sibling rows named Current (the New York neobank) are name collisions."))

# ---- curri
CURRI = NEWS("curri", "Curri nabs $42M")
L.append(cls("curri", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=CURRI,
             stage_conf="medium", entry_date="2023-06-06", country="US", city="Los Angeles",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-04-02", "Series A", 6000000, "Brick & Mortar Ventures", False, NEWS("curri", "lands $6M funding round"), "press"),
                     rnd("2023-06-06", "Series B", 42000000, BVP, True, CURRI, "press")],
             note="TechCrunch (2023-06-06): the $42M Series B, 'Bessemer Venture Partners led'. The $6M Series A of April 2021 (FreightWaves) names Brick & Mortar, Initialized and Rainfall and not the firm, and the two rounds make up the $48.2M raised, so the entry reads Series B although the firm's listing says 2021 (medium). Los Angeles as on the Y Combinator row; the company also gives Ventura."))

# ---- cybergrx
L.append(cls("cybergrx", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2017-04-04", city="Denver", focus="Security",
             rounds=[rnd("2017-04", "Series B", 20000000, BVP, True, None, "press"),
                     rnd("2018-12", "Series C", 30000000, "Scale Venture Partners", True, None, "press"),
                     rnd("2023-07-12", "Merger (ProcessUnity)", None, "ProcessUnity", None,
                         NEWS("cybergrx", "ProcessUnity and CyberGRX unite"), "press")],
             note="Third-party cyber risk exchange, Denver; merged into ProcessUnity in July 2023 (SiliconANGLE), so acquired. The firm's investment date is 2017-04-04: Bessemer led the $20M Series B of April 2017 (model, medium; the next round was the named Series C of December 2018), so Growth, and the prefilled 2018 date was a later Form D."))

# ---- cyota-inc
L.append(cls("cyota-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004-12-22",
             country="US", city="New York", focus="Security", rounds=[],
             note="Online banking anti-fraud company, headquartered in New York with R&D in Israel; acq. by RSA Security, December 2005 (The Jerusalem Post: $145M). The firm's listing dates its investment 2004-12-22 and names no round; none found in Google News, so undetermined."))

# ---- cyphy
CYPHY = NEWS("cyphy", "CyPhy Works to harness")
L.append(cls("cyphy", status="defunct", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=CYPHY,
             stage_conf="high", entry_date="2015-09-25", city="Danvers", focus="Industrial & Robotics",
             rounds=[rnd("2015-10", "Series B", 22000000, None, True, CYPHY, "press")],
             note="Fortune (2015-10-13): 'CyPhy recently raised $22 million in Series B venture funding', naming Bessemer among the investors, the firm's 2015 entry (investment date 2015-09-25), so Growth; the prefilled 2018 date was a later Form D. Renamed Aria Insights in January 2019 and shut down in March 2019 (The Robot Report); FLIR bought the assets afterwards, so defunct."))

# ---- cypress-io
CYP = POST("bessemer-promotes-andrew-hedin-mike-droesch")
L.append(cls("cypress-io", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=CYP,
             stage_conf="high", entry_date="2018-06-11", grad="graduated", grad_src=FP, grad_cite=CYP, grad_conf="high",
             city="Atlanta", focus="DevTools & APIs",
             rounds=[rnd("2018-06", "Seed", 4000000, BVP, True, CYP, "firm"),
                     rnd("2019-06", "Series A", 9300000, BVP, True, CYP, "firm")],
             note="The firm's own post (2019-07-16): Mike Droesch championed 'our seed investment in front-end test automation platform, Cypress.io', and 'in June 2019, Mike and partner Bob Goodman led Cypress' Series A'. So a Seed entry (investment date 2018-06-11) that graduated; the prefilled 2019 date was the Series A filing."))

# ---- dashbot
L.append(cls("dashbot", status="private", rng="below_1b", entry_date="2016-11-18", city="San Francisco",
             city_src="formd_address", focus="DevTools & APIs",
             note="Conversational analytics, San Francisco, now trading as Dimension Labs (dashbot.io redirects there). The firm's investment date is 2016-11-18, the $2.0M Form D round of late 2016, so the entry date is corrected from the 2018 filing the band read; the stage stays Seed. "
                  + GRAD_LATER))

jl.write("j02b", L)
