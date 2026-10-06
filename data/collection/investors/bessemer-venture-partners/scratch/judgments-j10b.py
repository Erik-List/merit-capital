import judge_lib as jl
from judge_lib import cls, rnd, verdict, ARCH, SITE, POST, W, NEWS
L = []
def A(*a, **k): L.append(cls(*a, **k))
NONE = {"focus": None}
B1 = "below_1b"
U = "undetermined"

A("stream-machine", status="acquired", rng=B1, stage=U, entry_date="1998", country="US", city="Fremont", focus="Industrial & Robotics", rounds=[],
  note="Listing says acq. by Cirrus Logic. No round named. City from memory.")
A("sulconam", status="unknown", rng=B1, stage=U, entry_date="1957", country="US", focus="Climate & Energy", flags=["pre_spinout", "city_unknown"], rounds=[],
  note="Firm's own archive: BVP invested in 1957 and structured an exit in 1997 when the dividend exceeded cost. What became of the company could not be traced. Pre-1981 entry (X1).")
A("supplier-io", status="private", rng=B1, stage=U, country="US", focus="SaaS", flags=["city_unknown"], rounds=[],
  note="On the firm's own 2022 listing, which predates the first Forge buyouts; the brief names Supplier.io as a Forge deal, so the report asks the lead to confirm no venture fund held it first. No round named.")
A("sweetlabs-inc-fmr-opencandy", status="unknown", rng=B1, stage=U, entry_date="2008-09-12", country="US", city="San Diego", city_src="web_verified", focus="Media, Gaming & Advertising", rounds=[],
  note="Wikipedia: SweetLabs is based in San Diego and Seattle and raised at least $21.5M from Bessemer, GV, Intel Capital and O'Reilly AlphaTech; no exit on the list, current state not verified. Round Bessemer entered not named.")
A("syncsort", status="acquired", rng=B1, stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=W("Precisely (company)"), entry_date="2008-03-31", country="US", city="Burlington", focus="Data Infrastructure",
  rounds=[rnd("2008-04", "Growth", None, None, True, W("Precisely (company)"), "press")],
  note="Wikipedia: in April 2008 Insight, Bessemer, Georgian, Goldman Sachs and others bought a majority interest. A majority purchase by a consortium is a growth buyout, not Bessemer control alone, so the row stays a member at Growth; flagged for the lead. Clearlake bought Syncsort in 2015; the company is now Precisely, in Burlington.")
A("syntrex", status="unknown", rng=B1, stage=U, entry_date="1979", city="Eatontown", focus="SaaS", flags=["pre_spinout"], rounds=[],
  note="Fault-tolerant legal information systems; firm records an exit in 1982 but the fate of the company is not traced. City from memory. Pre-1981 entry (X1).")
A("system-management-arts", status="acquired", rng=B1, stage=U, entry_date="2000-12-07", country="US", city="White Plains", focus="Data Infrastructure", rounds=[],
  note="Acq. by EMC, 2005 (listing and exit year). No round named.")
A("systemsoft", status="acquired", rng=B1, stage=U, entry_date="1992", country="US", country_src="model_knowledge", city="Natick", focus="SaaS", flags=["model_disputes_source"], rounds=[],
  note="The prefilled JP is a one-word name match; SystemSoft was a Natick, Massachusetts PC software company (firm region North America East). Its software business went to Phoenix Technologies in 1999 (from memory), so read acquired.")
A("taqua", status="acquired", rng=B1, stage=U, entry_date="1999", country="US", city="Plano", focus="Data Infrastructure", rounds=[],
  note="Acq. by Tekelec, 2004 (listing and exit year). No round named.")
A("team-solomid-tsm", status="private", rng=B1, stage=U, entry_date="2018-02-12", country="US", city="Los Angeles", focus="Media, Gaming & Advertising", rounds=[],
  note="Esports franchise; 2018 funding reports ($25M in January, $37M in July) do not say which round carried Bessemer. Current state taken as operating, last known.")
A("telenet", status="acquired", rng=B1, stage=U, entry_date="1975", country="US", focus="Data Infrastructure", flags=["pre_spinout", "city_unknown"], rounds=[],
  note="Listing says acq. by GTE. Packet network operator; pre-1981 entry (X1). No round named.")
A("telica", status="acquired", rng=B1, stage=U, entry_date="2000", country="US", city="Marlborough", focus="Data Infrastructure", rounds=[],
  note="Listing says acq. by Lucent Technologies. No round named.")
A("telocity", status="acquired", rng=B1, stage=U, entry_date="1998", country="US", city="Cupertino", focus="Data Infrastructure", rounds=[],
  note="Listing says acq. by Hughes (2001 tender offer, SC 14D9 on EDGAR). No round named.")
A("terabeam", status="acquired", rng=B1, stage=U, entry_date="1998", country="US", city="Seattle", focus="Data Infrastructure", rounds=[],
  note="Listing says acq. by YDI (which took the Terabeam name). No round named.")
A("terawave-communications", status="acquired", rng=B1, stage=U, entry_date="1999", country="US", city="Fremont", focus="Data Infrastructure", rounds=[],
  note="Status follows Lightspeed's row (acquired); buyer not verified. City from memory. No round named.")
A("the-retail-equation", status="acquired", rng=B1, stage=U, country="US", city="Irvine", focus="SaaS", rounds=[],
  note="Listed from the 2022 capture. Believed part of Appriss Retail (from memory, not verified). No round named.")
A("the-sports-authority", status="defunct", rng=B1, stage=U, entry_date="1987", country="US", city="Englewood", focus="Consumer & Marketplaces", rounds=[],
  note="Archive: Hardymon and Burgin participated in the 1987 and 1988 rounds (no round named). Bought by Kmart 1990, IPO 1994, Chapter 11 and liquidation in 2016 (from memory).")
A("thomas-weisel-partners-group", status="acquired", rng=B1, stage=U, entry_date="1997", country="US", city="San Francisco", focus=None, extra=NONE, rounds=[],
  note="Investment bank, outside the focus taxonomy; S-1 of 2005 lists Bessemer among investors in the firm. Bought by Stifel in 2010 (from memory).")
A("timothy-s-coffees-of-the-world", status="acquired", rng=B1, stage=U, entry_date="1997", country="CA", country_src="web_verified", country_cite=ARCH("timothy-s-coffees-of-the-world"), city="Toronto", focus="Consumer & Marketplaces", rounds=[],
  note="Archive: Canada-based coffee retail chain. Wikipedia: Green Mountain bought the wholesale business in November 2009 and the retail operations went to another buyer. No round named.")
A("topfreegames", status="unknown", rng=B1, stage=U, focus="Media, Gaming & Advertising", flags=["city_unknown"], rounds=[],
  note="Mobile games developer on the 2019 listing; neither location nor later news could be found.")
A("traction-guest", status="acquired", rng=B1, stage=U, country="CA", country_src="web_verified", country_cite=NEWS("traction-guest", "Traction on Demand Incubated Traction Guest Acquired"), city="Vancouver", focus="SaaS", rounds=[],
  note="Incubated by Traction on Demand and acquired in December 2021 (BetaKit reports PSG). City from memory. No round named.")
A("traffic-com", status="acquired", rng=B1, stage=U, entry_date="1999", city="Wayne", focus="Consumer & Marketplaces", rounds=[],
  note="Traffic.com (fka Mobility Technologies) was bought by Navteq in 2007 and Nokia took Navteq in 2008 (Wikipedia). No round named. City from memory.")
jl.write("j10b", L)
