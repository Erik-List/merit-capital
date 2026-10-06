"""Judge j02, part a (PRO-80 Bessemer Venture Partners, batch 3: cargo-one .. combocurve), 2026-10-01.
Rows are members on the firm's own listing; classification lines only. Run as NQ_TAG=j02 python3 judgments-j02a.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "scratchpad" / "j02"))
import judge_lib as jl
from judge_lib import ARCH, NEWS, POST, W, cls, rnd
from common import FP, GRAD_LATER, MOM, READ, SIBVAL, VRS, WV

L = []
BVP = "Bessemer Venture Partners"

# ---- cargo-one
L.append(cls("cargo-one", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2021", country="DE", country_src=WV,
             country_cite=NEWS("cargo-one", "German logistics tech firm cargo.one"), city="Berlin",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021", "Series B", 42000000, BVP, True, None, "press")],
             note="Air freight booking marketplace, Berlin. Bessemer led the $42M Series B of 2021, the firm's own year (model, medium); the seed and the 2020 Series A sit in the Point Nine and Creandum books. "
                  + MOM + "no priced round at $1B or more, the newest report being the Cargofive acquisition of March 2026."))

# ---- carwow
CARWOW = NEWS("carwow", "secures new $52m investment")
L.append(cls("carwow", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=CARWOW,
             stage_conf="high", entry_date="2024-07-14", country="GB", country_src=WV, country_cite=CARWOW,
             city="London", focus="Consumer & Marketplaces",
             rounds=[rnd("2024-07-14", "Series E", 52000000, BVP, True, CARWOW, "company")],
             note="Carwow's own release (London, 2024-07-14): the $52M round 'was led by global venture capital firm Bessemer Venture Partners', a new investor beside the existing ones; White & Case, the company's counsel, names it the Series E, so Growth. City AM put the valuation at GBP 250M (2024-07-16), below $1B; the prefilled GB is confirmed."))

# ---- cashify
MN = NEWS("cashify", "Cashify raises Series C")
L.append(cls("cashify", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=MN, stage_conf="high",
             entry_date="2015-04", grad="graduated", grad_src=WV, grad_cite=MN, grad_conf="high",
             country="IN", country_src=WV, country_cite=ARCH("cashify"), city="Gurugram",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2015-04", "Seed", 1000000, None, True, MN, "press"),
                     rnd("2017-07", "Series A", None, None, True, MN, "press"),
                     rnd("2018-06", "Series C", 12000000, None, None, MN, "press"),
                     rnd("2022-06", "Series E", 90000000, "NewQuest Capital Partners and Prosus", None, None, "press")],
             note="MediaNama (2018-06-29): in April 2015 the firm, then ReGlobe, 'received seed funding of $1 million' from Bessemer and Blume, and in July 2017 'it raised Series A funding', so a Seed entry that graduated. Inc42 put the $90M Series E of June 2022 at a $250M valuation, below $1B."))

# ---- cents
CENTS_B = NEWS("cents", "Cents Announces $40M Series B")
L.append(cls("cents", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=READ["cents-seed"],
             stage_conf="high", entry_date="2020", grad="graduated", grad_src=WV, grad_cite=CENTS_B, grad_conf="high",
             country="US", city="New York", focus="SaaS",
             rounds=[rnd("2020", "Seed", 4250000, BVP, True, READ["cents-seed"], "company"),
                     rnd("2022-01", "Series A", 25000000, "Tiger Global", True, None, "press"),
                     rnd("2024-08-08", "Series B", 40000000, "Camber Creek", True, CENTS_B, "company"),
                     rnd("2026-03-26", "Series C", 140000000, "Sumeru Equity Partners", None,
                         NEWS("cents", "Cents raises $140m in Series C"), "press")],
             note="The company's own release names a $4.25M seed round led by Bessemer (undated; the firm's year is 2020). PR Newswire (2024-08-08): the $40M Series B was led by Camber Creek 'with participation from previous investors Bessemer Venture Partners and Tiger Global', so graduated; the $140M Series C of March 2026 publishes no valuation, so below $1B."))

# ---- cerulean-pharma: the prefilled public status is the successor shell
L.append(cls("cerulean-pharma", status="acquired", rng="below_1b", stage="undetermined", entry_date="2007-12-07",
             city="Waltham", focus="Healthcare & Bio", flags=["model_disputes_source"], rounds=[],
             note="Nanopharmaceutical developer, Waltham; listed in April 2014 (NASDAQ: CERU). The prefilled public status and float belong to the successor: Cerulean wound down its pipeline and agreed a reverse merger with Dare Bioscience in March 2017 (Fierce Biotech, BioSpace; the firm's exit year is 2017), so the row reads acquired. The filings name the Series D the Bessemer funds joined later, not the round of the firm's December 2007 entry, so the stage is undetermined."))

# ---- chipagents
CHIP = POST("meet-the-founder-and-ceo-of-chipagents")
L.append(cls("chipagents", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=CHIP,
             stage_conf="high", entry_date="2025-10-21", country="US", city="Santa Barbara", focus="AI & Applied AI",
             rounds=[rnd("2025-10-21", "Series A", 21000000, BVP, True, CHIP, "firm"),
                     rnd("2026-07-29", "Series A extension (Series A total $134M)", 60000000, None, None,
                         NEWS("chipagents", "Expands Series A Funding to $134 Million"), "company")],
             note="The firm's own post (2025-10-21): 'Bessemer Venture Partners leads ChipAgents' $21M Series A', its first round in the company. "
                  + MOM + "the Series A was extended to $134M in July 2026 (Business Wire) with no valuation published, so no priced round at $1B or more."))

# ---- choco
CHOCO_V = NEWS("choco", "Choco Raises $111M in Series B2")
L.append(cls("choco", status="private", rng="1b_plus", usd=1200000000, val_src=WV, val_cite=CHOCO_V, asof="2022-04-12",
             extra=VRS, flags=["stale"], stage="Series A", stage_src="model", stage_conf="medium", entry_date="2019",
             country="DE", country_src=WV, country_cite=NEWS("choco", "Choco Raises $30.2M"), city="Berlin",
             focus="SaaS",
             rounds=[rnd("2019", "Series A", 33500000, BVP, True, None, "press"),
                     rnd("2020-04-16", "Series A2", 30200000, "Coatue", None, NEWS("choco", "Choco Raises $30.2M"), "press"),
                     rnd("2021-07-20", "Series B", 100000000, None, None, NEWS("choco", "Choco raises $100m Series B"), "press"),
                     rnd("2022-04-12", "Series B2", 111000000, None, None, CHOCO_V, "press")],
             note="Restaurant and supplier ordering platform, Berlin. Mark: the $111M Series B2 at $1.2B of April 2022 (FinSMEs), as the Coatue, Insight and Visionaries Club rows carry it; no later priced round in Google News on 2026-10-01, so stale. Bessemer led the 2019 Series A (model, medium; the firm's own year)."))

# ---- ciena
L.append(cls("ciena", rng="10b_plus", usd=52470000000, val_src=WV, val_cite=SIBVAL("ciena", "lightspeed"),
             asof="2026-10-01", extra=VRS, stage="Growth", stage_src=FP, stage_cite=ARCH("ciena"), stage_conf="high",
             entry_date="1994-12", country="US", city="Hanover", focus="Data Infrastructure",
             flags=["model_disputes_source"],
             rounds=[rnd("1994-12", "Series B", None, None, True, ARCH("ciena"), "firm")],
             note="The firm's archived listing: 'David Cowan invested in Ciena's B round in December 1994', so Growth. Ciena is in Hanover, Maryland; the prefilled CA is a name-match error (the Lightspeed row carries the same one). Market cap $52.47B on 2026-10-01 (stockanalysis.com)."))

# ---- clarity
TOI = NEWS("clarity", "Israeli deepfake detection startup raises first")
DEEL = NEWS("clarity", "Deel acquires Israeli deepfake security startup")
L.append(cls("clarity", status="acquired", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=TOI, stage_conf="high",
             entry_date="2024-02-15", country="IL", country_src=WV, country_cite=TOI, city="Tel Aviv", focus="Security",
             rounds=[rnd("2024-02-15", "Seed", 16000000, "Walden Catalyst Ventures and Bessemer Venture Partners", True, TOI, "press"),
                     rnd("2026-08-03", "Acquisition (Deel)", None, "Deel", None, DEEL, "press")],
             note="The Times of Israel (2024-02-15): the $16M seed 'was led by Walden Catalyst Ventures and Bessemer Venture Partners', with R&D headquarters in Tel Aviv. Acq. by Deel, 2026 (Calcalist, 2026-08-03: a $40M to $50M deal). "
                  + GRAD_LATER))

# ---- clarity-money
FST = READ["clarity-money-b"]
L.append(cls("clarity-money", status="acquired", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=FST,
             stage_conf="high", entry_date="2016", country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2016", "Series A", 3500000, None, True, FST, "press"),
                     rnd("2017-03", "Series B", 11000000, "RRE Ventures and Citi Ventures", True, FST, "press")],
             note="FStech on the March 2017 Series B: it came 'eight months after raising $3.5 million in Series A funding', with Bessemer among the existing investors, so the firm's 2016 entry reads Series A (FinSMEs had called the same round a seed in October 2016). Acq. by Goldman Sachs, 2018."))

# ---- claroty
CLAROTY_V = NEWS("claroty", "raises $150 million at a $3 billion")
L.append(cls("claroty", status="private", rng="1b_plus", usd=3000000000, val_src=WV, val_cite=CLAROTY_V,
             asof="2026-01-22", extra=VRS, stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2016-06-16", country="US", city="New York", focus="Security",
             rounds=[rnd("2016", "Series A", None, BVP, True, None, "press"),
                     rnd("2026-01-22", "Series F", 150000000, "Golub Growth", None, CLAROTY_V, "press")],
             note="Industrial cybersecurity, founded in Israel and headquartered in New York. Calcalist (2026-01-22): a $150M Series F led by Golub Growth at a $3B valuation. Bessemer led the 2016 Series A (model, medium; the firm's investment date is 2016-06-16 and its own posts say only 'early')."))

# ---- clearcare
L.append(cls("clearcare", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2014-06-12", country="US", city="San Francisco", focus="Healthcare & Bio",
             rounds=[rnd("2014-06", "Series B", 11000000, BVP, True, None, "press"),
                     rnd("2016-08-25", "growth round", 60000000, "Battery Ventures", None,
                         NEWS("clearcare", "gets $60M from Battery Ventures"), "press")],
             note="Home care software, San Francisco; acq. by WellSky, 2019 (FinSMEs, 2019-10-08; the firm's page says 2017 and its exit year is 2016, the year of Battery's $60M round). Bessemer led the $11M Series B of June 2014 (model, medium)."))

# ---- clearing
CLEARING = NEWS("clearing", "Clearing Targets Chronic Pain")
L.append(cls("clearing", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=CLEARING,
             stage_conf="high", entry_date="2021-05-25", country="US", city="New York", focus="Healthcare & Bio",
             rounds=[rnd("2021-05-25", "Seed", 20000000, "Bessemer Venture Partners and Founders Fund", True, CLEARING, "press")],
             note="Crunchbase News (2021-05-25): 'Bessemer Venture Partners and Founders Fund led' the $20M seed of the New York chronic pain platform; the firm's own year is 2020. No later round in Google News on 2026-10-01 and the company's site still answers. "
                  + GRAD_LATER))

# ---- clickhouse
CH = POST("accelerating-enterprise-transformation-toward")
CH_V = SIBVAL("clickhouse", "coatue")
L.append(cls("clickhouse", rng="10b_plus", usd=15000000000, val_src=WV, val_cite=CH_V, asof="2026-01-16", extra=VRS,
             stage="Growth", stage_src=FP, stage_cite=CH, stage_conf="high", entry_date="2025-05-29",
             city="San Francisco", focus="Data Infrastructure",
             rounds=[rnd("2025-05-29", "Series C", 350000000, "Khosla Ventures", True, CH, "firm"),
                     rnd("2026-01-16", "Series D", None, None, None, CH_V, "press")],
             note="The firm's own post (2025-05-29): 'Bessemer Venture Partners invests in ClickHouse Inc's Series C', so Growth. The prefilled $2B is superseded by the January 2026 round at $15B (TechCrunch, 2026-01-16), the mark the sibling books carry."))

# ---- clio
CLIO_W = W("Clio (software company)")
L.append(cls("clio", rng="1b_plus", usd=5000000000, val_src=WV, val_cite=SIBVAL("clio", "tcv"), asof="2025-11",
             extra=VRS, stage="Growth", stage_src=WV, stage_cite=CLIO_W, stage_conf="high", entry_date="2014-02-27",
             country="CA", country_src=WV, country_cite=CLIO_W, city="Burnaby", focus="SaaS",
             rounds=[rnd("2012", "Series B", 6000000, None, None, CLIO_W, "press"),
                     rnd("2014", "Series C", 20000000, BVP, True, CLIO_W, "press")],
             note="Wikipedia: 'In 2014, Clio received $20 million in Series C funding from Bessemer Venture Partners', after a 2012 Series B, so Growth; headquartered in Burnaby, British Columbia (CA confirmed). The prefilled $1.6B is superseded by the $5B valuation the company announced in November 2025, the mark the NEA, Point Nine and TCV rows carry."))

# ---- cloudinary
CLD_W = W("Cloudinary")
CLD_V = NEWS("cloudinary", "Blackstone invests over")
L.append(cls("cloudinary", status="private", rng="1b_plus", usd=2000000000, val_src=WV, val_cite=CLD_V,
             asof="2022-02-15", extra=VRS, flags=["stale", "model_disputes_source"], stage="Growth", stage_src=WV,
             stage_cite=CLD_W, stage_conf="high", entry_date="2015-08-10", country="US", country_src=WV,
             country_cite=CLD_W, city="San Jose", focus="DevTools & APIs",
             rounds=[rnd("2015", "secondary", None, BVP, True, CLD_W, "press"),
                     rnd("2022-02-15", "secondary", 100000000, "Blackstone", None, CLD_V, "press")],
             note="Bootstrapped image and video API company. Wikipedia: in 2015 'the company received a secondary investment from Bessemer Venture Partners', and a secondary reads Growth; headquartered in San Jose, California, so the prefilled IL (the R&D base) is replaced. Mark: Blackstone's secondary purchase at a $2B valuation (Globes, 2022-02-15), no later priced event found, so stale."))

# ---- cloudlock
L.append(cls("cloudlock", status="acquired", rng="below_1b", city="Waltham", focus="Security",
             note="Cloud security, Waltham; acq. by Cisco, 2016 (Business Insider: $293M). The prefilled Series A band is left as it stands: the company's Form Ds show an $8.7M round in 2012 before the $17.5M round of January 2014 that the firm joined, so the entry may be a later series, and no page read names it."))

# ---- club-w
L.append(cls("club-w", status="acquired", rng="below_1b", city="Santa Monica", focus="Consumer & Marketplaces",
             note="Subscription wine company, renamed Winc in 2016 and listed in November 2021. It filed for Chapter 11 in December 2022 and AMASS Brands bought the operating assets in January 2023 (Retail Dive), so acquired, a sale out of insolvency."))

# ---- coactive-ai
COACT = POST("unleashing-the-full-potential-of-unstructured")
L.append(cls("coactive-ai", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=COACT,
             stage_conf="high", entry_date="2023-03-21", country="US", city="San Jose", focus="AI & Applied AI",
             rounds=[rnd("2023-03-21", "Series A", 10400000, "Bessemer Venture Partners and a16z", True, COACT, "firm"),
                     rnd("2024-05-21", "Series B", 30000000, None, None, NEWS("coactive-ai", "Watkins Advises Coactive"), "press")],
             note="The firm's own post (2023-03-21): 'Bessemer Venture Partners co-leads Coactive AI's Series A', $10.4M with a16z; the firm's listing dates the entry 2022. "
                  + MOM + "the newest round is the $30M Series B of May 2024, no priced round at $1B or more."))

# ---- coiled
COILED = NEWS("coiled", "Coiled Cloud Closes")
L.append(cls("coiled", status="private", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=COILED,
             stage_conf="high", entry_date="2021-05-18", country="US", focus="Data Infrastructure",
             flags=["city_unknown"],
             rounds=[rnd("2020-10-01", "Seed", 5000000, None, None, NEWS("coiled", "Coiled Raises $5M in Seed"), "press"),
                     rnd("2021-05-18", "Series A", 21000000, BVP, True, COILED, "press")],
             note="citybiz (2021-05-18): the $21M Series A was 'led by Bessemer Venture Partners', after a $5M seed in 2020 that does not name the firm. The company is remote-first and no source read gives a headquarters, so the city is left unknown. "
                  + MOM + "no later round reported."))

# ---- collective-medical
CM = NEWS("collective-medical", "Raises $47.5M")
L.append(cls("collective-medical", status="acquired", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=CM,
             stage_conf="high", entry_date="2017-11-14", country="US", city="Salt Lake City", focus="Healthcare & Bio",
             rounds=[rnd("2017-11-14", "Series A", 47500000, "Kleiner Perkins", True, CM, "press"),
                     rnd("2020-12-07", "Acquisition (PointClickCare)", 650000000, "PointClickCare", None,
                         NEWS("collective-medical", "PointClickCare Is Buying"), "press")],
             note="HIT Consultant (2017-11-14): the Utah care-collaboration network raised its Series A 'led by Kleiner Perkins with participation from Bessemer Venture Partners', the firm's 2017 entry and the round the Kleiner Perkins row cites. Acq. by PointClickCare, 2020 ($650M)."))

# ---- columnar
L.append(cls("columnar", status="private", rng="below_1b", grad="censored", city="New York", city_src="formd_address",
             focus="Data Infrastructure",
             note="Data connectivity startup from the Apache Arrow maintainers; the firm's own post (2025-10-29) says it led the $4M seed, the Form D round of May 2025. Entry after 2024-10-01, so censored. "
                  + MOM + "no later round."))

# ---- combocurve
CC = NEWS("combocurve", "ComboCurve Announces $50M")
L.append(cls("combocurve", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=CC,
             stage_conf="high", entry_date="2022-04-12", country="US", city="Houston", focus="SaaS",
             rounds=[rnd("2022-04-12", "Series B", 50000000, "Dragoneer Investment Group and Bessemer Venture Partners", True, CC, "company")],
             note="The company's release (2022-04-12): $50M 'through a Series B funding round led by Dragoneer Investment Group and Bessemer Venture Partners', headquartered in Houston. No later round in Google News on 2026-10-01."))

jl.write("j02a", L)
