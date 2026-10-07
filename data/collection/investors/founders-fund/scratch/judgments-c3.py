"""Classification, chunk 3 (ritual .. zinier), and one membership ruling."""
from jl import *
NM("vittana", "T5: Vittana was a non-profit student-microloan organisation (501(c)(3)); the firm's 2012-14 listing reflects support for it, not an equity position a fund could hold. Not a venture-outcome operating company.", conf="medium")
R("ritual", "private", "Los Angeles", CON, stage="Seed", conf="medium", co="US", edate="2015", note="Ritual, subscription vitamins. Founders Fund led the $3.5M seed and the $10.5M Series A of 2017. Not the Toronto food-ordering app.")
R("sendgrid", None, "Denver", DEV, stage="Seed", conf="high", edate="2009", note="FF Angel, LLC bought into the 2009 seed and is a party to the investors' rights agreement filed with the 2017 IPO. Acq. by Twilio, 2019.")
R("sgn", "acquired", "Culver City", MED, stage="Series A", conf="high", co="US", edate="2008-05", note="Social Gaming Network, later Jam City. Founders Fund led the $15M Series A of May 2008. Netmarble bought control in 2015.")
R("signature-therapeutics", "private", "San Carlos", HB, stage="undetermined", co="US", note="Abuse-deterrent opioid chemistry (Pharmacofore until 2012). On the firm's list 2012 to 2014; the round is not named in the sources read.")
R("slide", "acquired", "San Francisco", CON, stage="undetermined", co="US", note="Max Levchin's Slide, on Fund I's first list (2006); Thiel also backed it personally, and the round the fund first joined is not established. Acq. by Google, 2010.")
R("smartdrive", "acquired", "San Diego", IND, stage="undetermined", co="US", note="Fleet video safety, a Fund I position on the list from 2007. Acq. by Omnitracs, 2020. The round is not named in the sources read.")
R("stemcentrx", None, "South San Francisco", HB, stage="undetermined", note="Cancer-stem-cell antibodies; the firm's largest position of the 2011-15 funds. Which series was the first fund entry is not established in a citable source. Acq. by AbbVie, 2016, $5.8B upfront.")
R("stord", "private", "Atlanta", SAAS, stage="Growth", conf="medium", co="US", edate="2020", val_from=("lux-capital", "stord"), flags=["cite_pending"],
  note="Cloud supply chain. Founders Fund joined Kleiner Perkins in the $31M Series B of 2020.")
R("styleseat", "private", "San Francisco", CON, stage="Seed", conf="low", edate="2011", flags=["stage_uncited"], note="Beauty-booking marketplace listed under FF Angel.")
R("taskrabbit", "acquired", "San Francisco", CON, stage="Growth", conf="medium", co="US", edate="2011-12", note="Founders Fund joined the $17.8M Series B of December 2011. Acq. by IKEA, 2017.")
R("top-fans", "unknown", None, None, stage="undetermined", co="US", vr="undetermined", flags=["identity_unresolved", "country_prior"],
  note="Listed as 'Top Fans' on the firm's site in 2010 and 2011, beside Topguest; no company could be tied to the name from the list alone.")
R("topsy", "acquired", "San Francisco", DATA, stage="Series A", conf="low", co="US", edate="2008", flags=["stage_uncited"], note="Topsy Labs, social search. Founders Fund among the early backers with BlueRun and Ignition. Acq. by Apple, 2013.")
R("ubeam", "unknown", "Marina Del Rey", IND, stage="Seed", conf="medium", co="US", edate="2012", note="Ultrasonic wireless charging (later SonicEnergy); FF Angel in the $750K seed of 2012. No sign of operations since about 2021.")
R("unity-biotechnology", "defunct", "South San Francisco", HB, stage="Growth", conf="medium", dispute=["status"], edate="2016-10", vr="below_1b", valuation_usd=None, valuation_source=None,
  flags=["model_disputes_source"], note="Senolytic medicines. Fund V entered in the $116M Series B of October 2016 and signed the investors' rights agreement filed with the 2018 IPO. The company wound down and delisted in 2025.")
R("uservoice", "private", "Raleigh", SAAS, stage="Seed", conf="low", edate="2010", flags=["stage_uncited"], note="Customer-feedback software listed under FF Angel.")
R("vicarious-systems", "acquired", "Union City", AI, stage="Seed", conf="medium", co="US", edate="2011-02", note="Vicarious. Founders Fund led the $1.2M seed of February 2011 and joined the 2012 Series A. Acq. by Alphabet's Intrinsic, 2022.")
R("vise", "private", "New York", FIN, stage="Series A", conf="high", co="US", edate="2019-12", val_from=("ribbit-capital", "vise"), stale=True, flags=["cite_pending"],
  note="AI portfolio management for advisers. Founders Fund led the $14.5M Series A of December 2019. Last priced round May 2021 at $1B.")
R("votizen", "acquired", "San Francisco", CON, stage="Seed", conf="medium", edate="2010", note="Voter network; Founders Fund in the $1.5M seed of 2010 with Sean Parker. Acq. by Causes, 2013.")
R("wallaby", "acquired", "Pasadena", FIN, stage="Seed", conf="medium", co="US", edate="2012", note="Wallaby Financial; FF Angel in the 2012 seed. Acq. by Bankrate, 2014.")
R("wanderjaunt", "defunct", "San Francisco", CON, stage="undetermined", co="US", note="Short-term rental operator; on the firm's list 2021 to 2022. Which round Founders Fund first joined is not established in the sources read. Shut down June 2023.")
R("wildfire", "acquired", "Redwood City", MED, stage="undetermined", note="Wildfire Interactive, an fbFund company. The firm lists it 2012 to 2014 without a group; the round a fund bought is not on record. Acq. by Google, 2012.")
R("withco", "private", None, FIN, stage="Series A", conf="medium", co="US", edate="2022", flags=["country_prior"], note="Lease-to-own real estate for small businesses. Founders Fund led the $32M Series A of 2022.")
R("younoodle", "private", "San Francisco", SAAS, stage="undetermined", note="Startup-competition platform backed by Founders Fund in 2008; the round carries no name in the sources read.")
R("zinier", "private", "San Mateo", SAAS, stage="Growth", conf="medium", co="US", edate="2019-01", note="Field-service automation. Founders Fund led the $22M Series B of January 2019.")
write("c3-classification")
