import judge_lib as jl
from judge_lib import cls, rnd, verdict, ARCH, SITE, POST, W, NEWS
L = []
def A(*a, **k): L.append(cls(*a, **k))
NONE = {"focus": None}
B1 = "below_1b"

A("sahara-networks", status="acquired", rng=B1, stage="undetermined", entry_date="1995", country="US", city="Sunnyvale", focus="Data Infrastructure", rounds=[],
  note="Listing says acq. by Cascade, Ascend, and Lucent (Cascade was bought by Ascend in 1997, Ascend by Lucent in 1999). The archive names no round; no stage is stated. City follows the Greylock row.")
A("salto", status="private", rng=B1, stage="Seed", stage_src="model", stage_conf="medium", entry_date="2019", country="IL", country_src="web_verified", country_cite=NEWS("salto", "Israeli SaaS co Salto"), city="Tel Aviv", focus="SaaS", rounds=[],
  note="The firm's own Atlas post says Bessemer made its first investment in Salto in 2019, before the October 2020 $27M round that Accel and Lightspeed read as Series A, so the entry was a pre-A seed round (inferred, round not named by the firm). Cut 50% of staff in June 2025 to refocus on security. Graduation left for the graduation pass.")
A("sarovar-hotels-resorts", status="acquired", rng=B1, stage="undetermined", entry_date="2006-02-07", country="IN", country_src="web_verified", country_cite=ARCH("sarovar-hotels-resorts"), city="New Delhi", focus=None, extra=NONE, rounds=[],
  note="Archive about says Sarovar was acquired by China's Louvre Hotels Group in January 2017. BVP India invested in 2006; no source names the round. Outside the focus taxonomy (hotel chain).")
A("sarvega", status="acquired", rng=B1, stage="undetermined", entry_date="2001-08-07", country="US", city="Downers Grove", focus="Security", rounds=[],
  note="Acq. by Intel, August 2005 (firm's own about; Wikipedia agrees). No round named. City from memory.")
A("scratch", status="unknown", rng=B1, stage="undetermined", entry_date="2014-09-11", country="US", city="New York", focus="Consumer & Marketplaces", rounds=[],
  note="Invite-only shopping-expert app founded August 2014; no news after the 2014 listing found, so its current state is unknown. Region on the firm's list is North America East.")
A("selectminds", status="acquired", rng=B1, stage="undetermined", entry_date="2007-08-21", country="US", city="New York", focus="SaaS", rounds=[],
  note="Acq. by Oracle, October 2012 (firm's own about). No round named.")
A("sent", status="private", rng=B1, stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite="https://www.manilatimes.net/2025/05/27/tmt-newswire/plentisoft/sent-raises-355-million-in-series-seed-funding-to-transform-a2p-business-messaging/2121331",
  entry_date="2025-05", grad="censored", country="US", city="New York", focus="DevTools & APIs",
  rounds=[rnd("2025-05", "Seed", 3550000, "Companyon Ventures", True, "https://www.manilatimes.net/2025/05/27/tmt-newswire/plentisoft/sent-raises-355-million-in-series-seed-funding-to-transform-a2p-business-messaging/2121331", "press")],
  note="$3.55M seed in May 2025 led by Companyon Ventures with Bessemer participating; $12M Series A followed July 2026 (GlobeNewswire). Momentum check 2026-10-01: no $1B+ priced round found. Entry is after 2024-10-01, so graduation is censored.")
A("shriram-epc", status="unknown", rng=B1, stage="undetermined", entry_date="2006-03-27", country="IN", country_src="web_verified", country_cite=ARCH("shriram-epc"), city="Chennai", focus=None, extra=NONE, rounds=[],
  note="BVP India listing of 2006. The company is believed to have listed in 2008 (not verified), so the 2006 entry would be a private round; the round is not named and the current state could not be confirmed. Outside the focus taxonomy (EPC contractor).")
A("siano-mobile-silicon", status="unknown", rng=B1, stage="undetermined", entry_date="2006-03-30", country="IL", country_src="web_verified", country_cite=ARCH("siano-mobile-silicon"), city="Netanya", focus="Industrial & Robotics", rounds=[],
  note="Israeli fabless chip company (firm's region Israel). No exit on the list and no verified later event, so the state is unknown. City from memory.")
A("sirocco-systems", status="acquired", rng=B1, stage="Seed", stage_src="first_party", stage_cite=ARCH("sirocco-systems"), entry_date="1998", grad="graduated", grad_src="first_party", grad_cite=ARCH("sirocco-systems"), grad_conf="high",
  country="US", city="Wallingford", focus="Data Infrastructure",
  rounds=[rnd("1998", "Seed", None, "Bessemer Venture Partners", True, ARCH("sirocco-systems"), "firm"), rnd("1998", "Series A", None, "Bessemer Venture Partners", True, ARCH("sirocco-systems"), "firm")],
  note="Firm's own sentence: Felda Hardymon led the seed and A round investments. Acq. by Sycamore Networks, 2000. The A round is named by the same sentence, so graduated. City follows the Greylock row.")
A("smart-machines", status="acquired", rng=B1, stage="undetermined", entry_date="1997", country="US", focus="Industrial & Robotics", flags=["city_unknown"], rounds=[],
  note="Listing says acq. by Brooks Automation; year and city not verified. No round named.")
A("soap-com", status="acquired", rng=B1, stage="undetermined", entry_date="2007-11-07", country="US", city="Jersey City", focus="Consumer & Marketplaces", rounds=[],
  note="Soap.com is a Quidsi brand; Quidsi was acquired by Amazon in April 2011 (firm's own about; Wikipedia places Quidsi at Exchange Place, Jersey City). No round named.")
A("soleil-securities", status="acquired", rng=B1, stage="undetermined", entry_date="2003-10-28", country="US", city="New York", focus=None, extra=NONE, rounds=[],
  note="Independent research broker, outside the focus taxonomy. Status, country and city follow the Bain Capital Ventures row (acquired, New York); the buyer is not verified here.")
A("sonic-mule", status="private", rng=B1, stage="undetermined", entry_date="2008", country="US", city="San Francisco", focus="Consumer & Marketplaces", rounds=[],
  note="Sonic Mule is Smule (about says so). Smule still operates; Wikipedia now gives its headquarters as Salt Lake City, but the company is long known as San Francisco based, so the city is from memory. No round named.")
A("sonus-networks", status="public", rng=B1, usd=305790000, val_src="web_verified", val_cite="https://stockanalysis.com/stocks/rbbn/market-cap/", asof="2026-10-01", stage="undetermined", entry_date="1997", city="Plano", focus="Data Infrastructure", rounds=[],
  note="Sonus merged with Genband in 2017 to form Ribbon Communications (RBBN), headquartered in Plano since 2019 (Wikipedia); market cap $305.79M. Archive says Felda Hardymon invested in 1997 with no round named.")
A("spanco-power-distribution", status="unknown", rng=B1, stage="undetermined", entry_date="2011-04-29", country="IN", country_src="web_verified", country_cite=ARCH("spanco-power-distribution"), focus="Climate & Energy", flags=["city_unknown"], rounds=[],
  note="Indian power distribution company on the BVP India list; no later news found, so the current state is unknown.")
A("speakeasy", status="unknown", rng=B1, stage="undetermined", entry_date="2014-01-31", country="US", focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
  note="Mobile conference-calling app of 2014. The sibling rows (GV's San Francisco API company, Headline's Seattle company) are different companies with the same name and are not aligned. No later news found.")
A("spot-ai", status="private", rng=B1, stage="undetermined", entry_date="2021", country="US", city="Burlingame", focus="AI & Applied AI", rounds=[],
  note="Listed from the first 2021 capture; no source read names the round Bessemer entered (Redpoint's row reads Series A). Momentum check 2026-10-01: latest priced round is $31M equity in October 2024, no $1B+ round. City follows the Redpoint row.")
A("stackpulse", status="unknown", rng=B1, stage="undetermined", entry_date="2020", country="US", focus="DevTools & APIs", flags=["city_unknown"],
  rounds=[rnd("2021-01", "Series A", 28000000, None, True, POST("out-of-stealth-stackpulse"), "firm")],
  note="Firm's own news post (2021-01-19) says Bessemer made the initial investment a year earlier when the company launched, without naming the round; the $28M announced then is a later raise. Current state not found. Momentum check 2026-10-01: no $1B+ round.")
A("staples", rng=B1, stage="undetermined", entry_date="1986", country="US", city="Framingham", focus="Consumer & Marketplaces", rounds=[],
  note="Archive says Hardymon and Burgin invested in each of the four rounds starting in 1986; the first round is not called Series A. IPO 1989; taken private by Sycamore Partners in 2017.")
A("stayglad", status="acquired", rng=B1, stage="undetermined", entry_date="2015-10-14", country="IN", country_src="web_verified", country_cite=ARCH("stayglad"), focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
  note="Acq. by Quikr, September 2016 (Business Standard headline 2016-09-13). No round named.")
A("stratim", status="acquired", rng=B1, stage="undetermined", entry_date="2015-04-08", country="US", city="San Francisco", focus="Industrial & Robotics", rounds=[],
  note="Same company as zirx: the valet app Zirx shut its consumer business in February 2016 and the firm carries it as Stratim with the same 2015-04-08 date. Firm records an exit in 2018; the buyer is not verified. Duplicate rows (zirx, stratim).")
A("stratoscale", status="defunct", rng=B1, stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013-09-30", country="IL", country_src="web_verified", country_cite=W("Stratoscale"), city="Herzliya", focus="Data Infrastructure", rounds=[rnd("2013-10", "Series A", 10000000, "Battery Ventures", True, None, "press")],
  note="First institutional round reported October 2013 (Haaretz: $10M for the new startup), the round Battery's row also reads Series A. Status follows Battery's row (defunct). Graduation left for the graduation pass is not needed, entry is not Seed.")
jl.write("j10a", L)
