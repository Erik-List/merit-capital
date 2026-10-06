import judge_lib as jl
from judge_lib import cls, rnd, verdict, ARCH, SITE, POST, W, NEWS
L = []
def A(*a, **k): L.append(cls(*a, **k))
NONE = {"focus": None}
B1 = "below_1b"
U = "undetermined"
FS = "https://www.finsmes.com/2026/05/trajectory-raises-15m-in-seed-funding.html"
UC = "https://stockanalysis.com/quote/nse/URBANCO/market-cap/"

A("trajectory", status="private", rng=B1, stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=FS, entry_date="2026-05", grad="censored", country="US", city="San Francisco", focus="AI & Applied AI",
  rounds=[rnd("2026-05", "Seed", 15000000, "Conviction", True, FS, "press")],
  note="$15M seed in May 2026 led by Conviction with Bessemer participating (FinSMEs, found by search). Series A of $40M at $300M followed in August 2026, so below $1B (momentum check 2026-10-01). Entry after 2024-10-01, graduation censored.")
A("transvascular", status="acquired", rng=B1, stage=U, entry_date="1999", country="US", city="Menlo Park", focus="Healthcare & Bio", rounds=[],
  note="Listing says acq. by Medtronic. City and status follow the NEA row. No round named.")
A("travcorps", status="acquired", rng=B1, stage=U, entry_date="1995", country="US", city="Woburn", focus="Healthcare & Bio", rounds=[],
  note="Status and city follow the Greylock row; the firm records an exit in 1999 without a buyer. No round named.")
A("travel-triangle", status="private", rng=B1, stage=U, entry_date="2015-05-08", country="IN", country_src="web_verified", country_cite=ARCH("travel-triangle"), city="Gurugram", focus="Consumer & Marketplaces", rounds=[],
  note="Indian holiday marketplace (firm's own about). Later rounds were Series B in February 2017 led by RB Investments and Series C in 2018, so the May 2015 round was earlier, but no source names it or Bessemer in it.")
A("trenwick", status="defunct", rng=B1, stage=U, entry_date="1979", country="US", city="Stamford", focus=None, extra=NONE, flags=["pre_spinout"], rounds=[],
  note="Reinsurer, outside the focus taxonomy; went into Chapter 11 in 2003 (from memory). Pre-1981 entry (X1). No round named.")
A("tribe", status="unknown", rng=B1, stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=POST("truebill-saving-consumers"), entry_date="2020-11", country="CA", country_src="web_verified", country_cite=NEWS("tribe", "Tribe Technologies announces November seed"), focus="SaaS", flags=["city_unknown"],
  rounds=[rnd("2020-11", "Seed", 7500000, "Bessemer Venture Partners", True, POST("truebill-saving-consumers"), "firm")],
  note="Firm's own news item (indexed under a Truebill URL, title Tribe Technologies) says Bessemer co-led the $7.5M seed round; BetaKit places the seed in November (2020) and the company in Canada. Current state not found. Graduation left for the graduation pass.")
A("trigo", status="acquired", rng=B1, stage=U, entry_date="2000-08-08", country="US", focus="SaaS", flags=["city_unknown"], rounds=[],
  note="Firm's own about: Cowan participated in all institutional rounds from the 1999 founding by a team including Byron Deeter; acq. by IBM, 2004. No single round named. The Menlo (Tel Aviv) and Y Combinator (New York) Trigo rows are different companies and are not aligned.")
A("trinet", country="US", city="Dublin", stage=U, focus="SaaS", rounds=[],
  note="Public PEO (Dublin, California per Wikipedia). The firm's archive carries it as a top exit with exit year 2004 and no investment year or round, so entry stays undetermined.")
A("truaxis", status="acquired", rng=B1, stage=U, entry_date="2007-07-09", country="US", city="San Francisco", focus="Fintech & Payments", rounds=[],
  note="Truaxis (formerly BillShrink) was acquired by MasterCard, September 2012 (firm's own about). No round named.")
A("tulip-telecom", status="unknown", rng=B1, stage=U, entry_date="2007", country="IN", country_src="web_verified", country_cite=ARCH("tulip-telecom"), city="Gurugram", focus="Data Infrastructure", rounds=[],
  note="BVP India listing of 2007; the company is believed to have been private or just listing then and later in difficulty, none verified, so its state is unknown.")
A("tumbleweed", country="US", city="Redwood City", stage=U, entry_date="1997", focus="Security", rounds=[],
  note="Archive gives no round. IPO 1999; Axway bought it in 2008 (Wikipedia).")
A("turnitin", status="acquired", rng=B1, stage=U, city="Oakland", focus="SaaS", rounds=[],
  note="Listed only on the 2022 capture, no year or round. Advance Publications bought Turnitin from Insight Partners in 2019 (from memory); Bessemer's link to it is not documented on any page read.")
A("u-s-behavioral-health", status="acquired", rng=B1, stage=U, entry_date="1987", country="US", city="San Francisco", focus="Healthcare & Bio", rounds=[],
  note="Listing says acq. by The Travelers Group. Status and city follow the Menlo row. No round named.")
A("ungermann-bass", status="acquired", rng=B1, stage="Series A", stage_src="first_party", stage_conf="medium", stage_cite=ARCH("ungermann-bass"), entry_date="1980", country="US", city="Santa Clara", focus="Data Infrastructure", flags=["pre_spinout"],
  rounds=[rnd("1980", "Series A", None, "Bessemer Venture Partners", True, ARCH("ungermann-bass"), "firm")],
  note="Firm's own sentence: Neill Brownstein led the first institutional financing in 1980, read as the Series A. IPO 1983; later bought by Tandem and then Newbridge (Wikipedia names Newbridge). Pre-1981 entry (X1).")
A("unipalm", status="acquired", rng=B1, stage=U, entry_date="1995", country="GB", country_src="web_verified", country_cite=ARCH("unipalm"), city="Cambridge", focus="Data Infrastructure", rounds=[],
  note="JP-free: the prefilled GB is confirmed, the firm's own about calls it the largest independent ISP in the United Kingdom. Listing says acq. by UUnet; Wikipedia adds Computerlinks bought it in 2000.")
A("urbanclap", status="public", rng="1b_plus", usd=2521163151, val_src="web_verified", val_cite=UC, asof="2026-10-01", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("urbanclap", "Urbanclap Raises $25 Mn In Series B"), entry_date="2015-11-18",
  country="IN", country_src="web_verified", country_cite=ARCH("urbanclap"), city="Gurugram", focus="Consumer & Marketplaces", extra={"valuation_range_source": "web_verified"},
  rounds=[rnd("2015-11-18", "Series B", 25000000, "Bessemer Venture Partners", True, NEWS("urbanclap", "Urbanclap Raises $25 Mn In Series B"), "press")],
  note="Now Urban Company, listed 2025. Market cap INR 242.86B = $2.52B (INR/EUR 108.832, EUR/USD 1.1298, ECB 2026-10-01; fx-convert helper). Bessemer led the $25M Series B of November 2015 with Accel and SAIF already in.")
A("valicert", status="acquired", rng=B1, stage=U, entry_date="1998-05-04", country="US", city="Mountain View", focus="Security", rounds=[],
  note="IPO 2000, then bought by Tumbleweed in 2003 (firm's own about). No round named.")
A("vector-ai", status="private", rng=B1, stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("vector-ai", "Vector AI secures"), entry_date="2021-09-14", country="GB", country_src="web_verified", country_cite=NEWS("vector-ai", "Vector AI secures"), city="London", focus="SaaS",
  rounds=[rnd("2021-09-14", "Series A", None, "Bessemer Venture Partners", True, NEWS("vector-ai", "Vector AI secures"), "press")],
  note="Bessemer led the GBP 10.8M Series A in September 2021; no earlier round naming Bessemer was found. The company later renamed to Raft (Series B of $30M in 2023, Bessemer in it). Momentum check 2026-10-01: no $1B+ round.")
A("vector-solutions", status="private", rng=B1, stage=U, country="US", city="Tampa", focus="SaaS", rounds=[],
  note="Listed on the 2022 capture only. Genstar bought a majority in July 2021; the brief names a Forge deal called Vector, which is a different logistics company, so this row stays a member. No round named.")
A("verio", status="acquired", rng=B1, stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=ARCH("verio"), entry_date="1996", country="US", city="Englewood", focus="Data Infrastructure",
  rounds=[rnd("1996", "Growth", None, None, True, ARCH("verio"), "firm")],
  note="Firm's own sentence: BVP participated in an expansion round of Verio in 1996; IPO 1998; acq. by NTT, 2000.")
A("veritas", status="acquired", rng=B1, stage=U, entry_date="1991", country="US", city="Mountain View", focus="Data Infrastructure", flags=["model_disputes_source"], rounds=[],
  note="The prefilled GB is a one-word name match (acquirer Audentes is a different Veritas); this is Veritas Software, formerly Tolerant Computing, a California company that merged into Symantec. Firm's sentence says Brownstein led the turn-around financing, which names no round.")
A("versant-object-technology", country="US", city="Fremont", stage=U, entry_date="1990", focus="Data Infrastructure", rounds=[],
  note="No round named. Bought by Actian in 2012 (from memory).")
A("vertica-systems", status="acquired", rng=B1, stage=U, entry_date="2005-03-31", country="US", city="Cambridge", focus="Data Infrastructure", rounds=[],
  note="Acq. by Hewlett Packard, March 2011 (firm's own about; Wikipedia says Rocket Software took Vertica from OpenText in May 2026). No round named.")
jl.write("j10c", L)
