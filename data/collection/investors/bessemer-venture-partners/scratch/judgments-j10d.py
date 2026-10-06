import judge_lib as jl
from judge_lib import cls, rnd, verdict, ARCH, SITE, POST, W, NEWS
L = []
def A(*a, **k): L.append(cls(*a, **k))
NONE = {"focus": None}
B1 = "below_1b"
U = "undetermined"
STUB = "https://stockanalysis.com/stocks/stub/market-cap/"
TOSS = NEWS("viva-republica-toss", "Closes $48M Series C")
ZP = NEWS("zirx", "ZIRX Raises $30 Million Led By Bessemer")

A("vesta", status="private", rng=B1, stage=U, entry_date="2000", country="US", city="Lake Oswego", focus="Fintech & Payments", flags=["model_disputes_source"], rounds=[],
  note="The prefilled BY is a one-word name match. Read as Vesta Corporation, the payment-guarantee company (Lake Oswego, Oregon, founded 1995); identification is from search, low confidence. The a16z row (San Francisco, Seed) may be another company and is not aligned.")
A("via-net-works", status="unknown", rng=B1, stage=U, entry_date="1998", country="US", city="Reston", focus="Data Infrastructure", rounds=[],
  note="European ISP group (IPO 2000). Its later fate was not verified; US headquarters city from memory.")
A("viagogo", status="public", rng="1b_plus", usd=2110000000, val_src="web_verified", val_cite=STUB, asof="2026-10-01", stage=U, city="New York", focus="Consumer & Marketplaces", extra={"valuation_range_source": "web_verified"}, rounds=[],
  note="Now StubHub Holdings (STUB), listed September 2025; market cap $2.11B, consistent with Atomico's row ($2.08B on 2026-09-25). The firm's capture says Viagogo closes the StubHub deal in 2020; no source names the round Bessemer entered.")
A("viddy", status="acquired", rng=B1, stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=POST("memos/twitch"), entry_date="2011", grad="graduated", grad_src="web_verified", grad_cite=W("Viddy (app)"), grad_conf="high",
  country="US", city="Los Angeles", focus="Consumer & Marketplaces",
  rounds=[rnd("2011", "Seed", None, None, True, POST("memos/twitch"), "firm"), rnd("2012-02", "Series A", 6000000, None, True, W("Viddy (app)"), "press")],
  note="The firm's own Twitch memo calls Viddy a BVP seed investment. Wikipedia: a $6M Series A in February 2012 with Bessemer among investors. Renamed Supernova in 2013 and acquired by Fullscreen, January 2014. Siblings place it in Venice (a Los Angeles district).")
A("vimo", status="unknown", rng=B1, stage=U, entry_date="2005", country="US", focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
  note="Vimo (fka Healthia), health-care cost comparison; fate not traced. No round named.")
A("vision-express-group", status="unknown", rng=B1, stage=U, entry_date="1994", country="GB", country_src="web_verified", country_cite=ARCH("vision-express-group"), focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
  note="Archive: operates optical superstores in Europe, region Europe; read as the UK chain. The firm records an exit in 1997 without a buyer, so the status is unknown.")
A("visor", status="private", rng=B1, stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite="https://www.visor.us/blog/visor-announces-5-million-of-seed-funding-and-the-launch-of-the-worlds-most-connected-spreadsheet-to-democratize-internal-application-building/",
  entry_date="2021-09-29", country="US", focus="SaaS", flags=["model_disputes_source", "city_unknown"],
  rounds=[rnd("2021-09-29", "Seed", 5000000, "General Catalyst", True, "https://www.visor.us/blog/visor-announces-5-million-of-seed-funding-and-the-launch-of-the-worlds-most-connected-spreadsheet-to-democratize-internal-application-building/", "company")],
  note="Company's own post: $5M seed on 2021-09-29 led by General Catalyst with Bessemer (Cowan and D'Onofrio). The prefilled ES is a one-word match; no source places the company outside the US (investors are US). Momentum check 2026-10-01: no $1B+ round found. Graduation left for the graduation pass.")
A("vitelic", status="acquired", rng=B1, stage=U, entry_date="1984", country="US", city="San Jose", focus="Industrial & Robotics", rounds=[],
  note="Memory chip maker; merged into Mosel Vitelic (Wikipedia), listing says acq. by Mosel. No round named.")
A("viva-republica-toss", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2017-03-09", city="Seoul", focus="Fintech & Payments",
  rounds=[rnd("2017-03-10", "Series C", 48000000, None, None, TOSS, "press")],
  note="Entry date matches the $48M Series C announced 2017-03-10 (the headline does not name Bessemer), so read as Series C, Growth. Seoul from memory.")
A("vmx", status="acquired", rng=B1, stage="Series A", stage_src="first_party", stage_conf="medium", stage_cite=ARCH("vmx"), entry_date="1978", country="US", focus="Data Infrastructure", flags=["pre_spinout", "city_unknown"],
  rounds=[rnd("1978", "Series A", None, "Bessemer Venture Partners", True, ARCH("vmx"), "firm")],
  note="Firm's own sentence: BVP invested in the first institutional round in 1978, read as the Series A; IPO 1983. Later bought by Octel (from memory). Pre-1981 entry (X1).")
A("vts", city="New York", stage=U, entry_date="2013", focus="SaaS", rounds=[],
  note="Entry year is the firm's own partnered year; no source read names the round Bessemer entered. Mark and status are the prefilled values (stale Insight 2019 mark).")
A("wavesmith-networks", status="acquired", rng=B1, stage=U, entry_date="2000-04-13", country="US", city="Acton", focus="Data Infrastructure", rounds=[],
  note="Listing says acq. by Ciena. City from memory. No round named.")
A("webspective", status="acquired", rng=B1, stage=U, entry_date="1997", country="US", focus="Data Infrastructure", flags=["city_unknown"], rounds=[],
  note="Listing says acq. by Inktomi. No round named.")
A("wize", status="acquired", rng=B1, stage=U, entry_date="2006", country="US", focus="Consumer & Marketplaces", flags=["model_disputes_source", "city_unknown"], rounds=[],
  note="Listing says acq. by NexTag. The prefilled JP is a one-word name match; Wize Rank was a US shopping-review site.")
A("workmetro", status="acquired", rng=B1, stage=U, entry_date="2005", country="US", focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
  note="Listing says acq. by Jobing.com. No round named.")
A("wydr", status="defunct", rng=B1, stage=U, entry_date="2016-12-19", country="IN", country_src="web_verified", country_cite=ARCH("wydr"), focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
  note="Entrackr and Techcircle reported in November 2018 that the Bessemer and Stellaris backed marketplace shut down. No round named.")
A("zany-brainy", country="US", city="King of Prussia", stage=U, entry_date="1995", focus="Consumer & Marketplaces", rounds=[],
  note="Toy retailer; Chapter 11 on 2001-05-15 (Wikipedia). No round named.")
A("zensys", status="acquired", rng=B1, stage=U, entry_date="2005", country="DK", country_src="web_verified", country_cite=W("Z-Wave"), city="Copenhagen", focus="Industrial & Robotics", rounds=[],
  note="Wikipedia: Zensys, a Danish company in Copenhagen, built Z-Wave; acquired by Sigma Designs in December 2008. No round named.")
A("ziff-davis-enterprise", status="unknown", rng=B1, stage=U, entry_date="2008", country="US", city="New York", focus="Media, Gaming & Advertising", rounds=[],
  note="Technology media publisher (eWeek); fate after the 2012 capture not verified. No round named.")
A("zirx", status="acquired", rng=B1, stage=U, entry_date="2015-04", country="US", city="San Francisco", focus="Consumer & Marketplaces",
  rounds=[rnd("2015-04", "undetermined", 30000000, "Bessemer Venture Partners", True, ZP, "press")],
  note="PR Newswire (2015-04-22): $30M led by Bessemer, series not stated and earlier rounds existed. Consumer valet business shut February 2016; same company as stratim, carried under that name by the firm with an exit in 2018. Duplicate rows (zirx, stratim).")
A("zones", status="acquired", rng=B1, stage=U, entry_date="1995", country="US", city="Auburn", focus="Consumer & Marketplaces", rounds=[],
  note="IT reseller; taken private by its majority holder in 2008 (from memory, not verified). No round named.")
L.append(verdict("10tales-inc", "not_member", "Name match only: Jeremy Levine appears as a director on 10Tales' 2015 Form D, with no Bessemer fund on any filing and no listing or press naming Bessemer in a round (decisions.md D6, COLLECTION.md s1 name-match rule).",
  ec="formd_adjudicated", conf="medium", cite="https://www.sec.gov/Archives/edgar/data/1654462/000114036115037511/0001140361-15-037511-index.htm"))
jl.write("j10d", L)
