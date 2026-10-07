"""Classification, chunk 1 (airtime .. causes). Values the Form D and Wikidata layers pre-filled are left alone unless disputed in the line."""
from jl import *
SA = "https://stockanalysis.com/stocks/%s/market-cap/"
R("airtime", "defunct", "San Francisco", CON, note="Sean Parker's video-chat company; the app was shut down. Entry is the 2011-12 Series A (Founders Fund with Andreessen Horowitz, Accel, Kleiner Perkins, Google Ventures).")
R("altschool", "acquired", "San Francisco", CON, stage="Series A", conf="high", dispute=["entry_stage"], edate="2014-03",
  note="Founders Fund led the $33M Series A of March 2014 with Andreessen Horowitz; the Form D band read the amount as Growth. Became Altitude Learning in 2019; acq. by Higher Ground Education, 2021.")
R("applied-molecular-transport", "acquired", "South San Francisco", HB, stage="undetermined", co="US",
  note="Funds V and VI hold from the preferred rounds before the June 2020 IPO; the IPO filings were not read for the series the funds first bought, so the round stays open. Merged into Cyclo Therapeutics, December 2023.")
R("azumio", "private", "Redwood City", HB, note="Health-app maker; seed of July 2011 ($2.5M) led by Founders Fund.")
R("branch", "private", "Mountain View", DEV, val_from=("new-enterprise-associates", "branch"), stale=True,
  note="Branch Metrics. Founders Fund led the $35M Series B of January 2016 (first sale November 2015). Last priced round February 2022 at $4B, older than 24 months.")
R("clickable", "acquired", "New York", SAAS, stage="Growth", conf="high", edate="2008-07",
  note="Founders Fund led the $14.5M Series B of July 2008 (the firm's own news list links VentureBeat's report). Acq. by Syncapse, 2012.")
R("cloud9", "private", "Santa Monica", MED, note="Esports organisation; Founders Fund led the $25M Series A of 2017. Not the Cloud9 development environment Amazon bought.")
R("compass-pathways", None, "London", HB, stage="Growth", conf="high", edate="2020-04", usd=1_600_000_000, vcite=SA % "cmps", vasof="2026-10-06",
  flags=["model_disputes_source", "cite_pending"], note="Fund VII entered in the Series B of April 2020 (Series B preferred held by The Founders Fund VII, LP per the 2020 draft registration statement); Thiel's earlier stake was personal. Nasdaq: CMPS; market cap replaces the float.")
R("eight-sleep", "private", "New York", CON, stage="Growth", conf="high", edate="2019-11",
  note="Founders Fund led the $40M Series C of November 2019; the 2017 director seat on the filings is Keith Rabois's from Khosla Ventures. $100M round of August 2025 at an undisclosed valuation.")
R("emerald-therapeutics", "private", "Austin", HB, note="Emerald Therapeutics and its spin-out Emerald Cloud Lab (Austin since 2022); the funds backed the first round of September 2010 ($5M).")
R("emulate", "private", "Boston", HB, stage="Growth", conf="high", co="US", edate="2018-06",
  note="Organs-on-chips. Founders Fund led the $36M Series C of June 2018, Aaron VanDevender joining the board.")
R("forward", None, "San Francisco", HB, note="Primary-care clinics; shut down November 2024.")
R("gecko-robotics", "private", "Pittsburgh", IND, stage="Series A", conf="high", dispute=["entry_stage"], edate="2018-06", val_from=("y-combinator", "gecko-robotics"),
  flags=["cite_pending"], note="Founders Fund led the $7M Series A of June 2018 (Trae Stephens on the board); the Form D anchor was the 2025 Series D, which the band read as a Growth entry.")
R("gowalla", "defunct", "Austin", CON, co="US", note="Location check-in app (Alamofire Inc.). Facebook hired the team in December 2011 without buying the service, which shut in March 2012: defunct under the acqui-hire rule.")
R("hq", "defunct", "New York", MED, stage="Series A", conf="high", edate="2018-03",
  note="HQ Trivia (Intermedia Labs). Founders Fund led the $15M Series A of March 2018, Cyan Banister joining the board. Shut down February 2020.")
R("inigral", "acquired", "San Francisco", SAAS, co="US", note="Schools App for colleges (later Uversity); Founders Fund's $3M round of May 2009. Acq. by TargetX, 2015.")
R("long-term-stock-exchange", "private", "San Francisco", FIN, stage="Series A", conf="medium", edate="2016-07",
  note="Founders Fund led the Series A that closed from July 2016 ($24.4M on the filing), Brian Singerman joining the board.")
R("misfit", "acquired", "Burlingame", CON, note="Wearables. Founders Fund and Khosla led the $7.6M Series A of April 2012. Acq. by Fossil, 2015.")
R("newlimit", "private", "South San Francisco", HB, stage="Series A", conf="medium", co="US", edate="2023-05", val_from=("thrive-capital", "newlimit"),
  flags=["cite_pending"], note="Epigenetic reprogramming. Founders Fund joined the $40M Series A of May 2023 with Dimension and Kleiner Perkins.")
R("ooma", None, "Sunnyvale", CON, stage="undetermined", usd=548_140_000, vcite=SA % "ooma", vasof="2026-10-06", flags=["model_disputes_source"],
  note="Fund I position, on the firm's list from 2008; the round the fund entered (2006 to 2008) is not on record here. NYSE: OOMA; market cap replaces the float.")
R("pietra", "private", "New York", CON, stage="Series A", conf="high", edate="2021-09",
  note="Founders Fund led the $15M Series A of September 2021, Keith Rabois joining the board.")
R("prior-knowledge", "acquired", "San Francisco", AI, note="Predictive-database startup; Founders Fund seed of November 2011. Acq. by Salesforce, December 2012.")
R("quantcast", "private", "San Francisco", MED, stage="Series A", conf="medium", edate="2006",
  note="Fund I joined the 2006 Series A with Polaris and Revolution and co-led the $20M Series B of 2008; on the firm's list since 2007.")
R("researchgate", "private", "Berlin", CON, stage="Growth", conf="high", dispute=["entry_stage", "hq_country"], co="DE", edate="2012-02",
  flags=["model_disputes_source"], note="Founders Fund led the Series B of February 2012, Luke Nosek joining the board; the band read the 2013 Series C filing as the entry. Headquartered in Berlin; the Form D address is its US office.")
R("robotex", "unknown", "Sunnyvale", IND, stage="undetermined",
  note="Tactical ground robots (Avatar); Peter Thiel a director on the 2010 filings. No trace of the company after about 2017 and no reported sale; the round the fund entered is not named in any source read.")
R("scale", "private", "San Francisco", AI, stage="Growth", conf="medium", co="US", edate="2019-08", val_from=("index-ventures", "scale"),
  flags=["cite_pending"], note="Scale AI. Founders Fund led the $100M Series C of August 2019. Meta bought 49% in June 2025 at $29B; the company stays independent.")
R("stripe", "private", "San Francisco", FIN, stage="undetermined", dispute=["status"], val_from=("y-combinator", "stripe"), flags=["model_disputes_source"],
  note="Private; the Wikidata join that read 'acquired' is wrong. Funds III and IV hold from 2012 or earlier (the firm's site lists it from 2015); the round the fund first bought was not established in this pass. Tender of February 2026 at $159B.")
R("sword-health", None, "New York", HB, stage="Growth", conf="medium", dispute=["hq_country"], co="US", co_src="model_knowledge", edate="2021",
  flags=["model_disputes_source"], note="Digital musculoskeletal care, founded in Porto, run from New York. Founders Fund first appears in the 2021 rounds (Series C and D). The Wikidata country string was malformed.")
R("synthego", "acquired", "Redwood City", HB, stage="Series A", conf="high", dispute=["entry_stage"], edate="2013",
  note="Founders Fund led the $8.3M Series A of 2013 and the $110M Series C of 2018; the band anchored on the 2016-17 Series B. Chapter 11 in May 2025, assets sold to Perceptive Advisors.")
R("tachyus", "private", "Houston", DATA, note="Oil-and-gas production software; Founders Fund led the $6M seed of 2014, Scott Nolan on the board.")
R("tagomi", "acquired", "Jersey City", CRY, stage="Seed", conf="medium", co="US", edate="2018",
  note="Crypto prime broker; Founders Fund joined the 2018 seed and led the $12M round of March 2019. Acq. by Coinbase, 2020.")
R("the-athletic", "acquired", "San Francisco", MED, note="Founders Fund and Bedrock led the $40M Series C of October 2018. Acq. by The New York Times, February 2022, $550M.")
R("the-climate-corporation", None, "San Francisco", CLI, note="Founders Fund led the $50M Series C of June 2012. Acq. by Monsanto, 2013.")
R("topguest", "acquired", "New York", CON, stage="Seed", conf="low", co="US", edate="2010", flags=["stage_uncited"],
  note="Travel-loyalty check-ins; Founders Fund's 2010 seed round. Acq. by Switchfly, December 2011.")
R("traba", "private", "Miami", CON, stage="Series A", conf="high", co="US", edate="2022",
  note="Light-industrial staffing marketplace. Founders Fund (Keith Rabois) led the Series A of 2022 and the Series B of 2023.")
R("trade-republic", None, "Berlin", FIN, stage="Growth", conf="high", edate="2020-04", dispute=["valuation_range"], val_from=("project-a-ventures", "trade-republic"),
  flags=["cite_pending"], note="Founders Fund co-led the EUR 62M Series B of April 2020 with Accel. Secondary of December 2025 at EUR 12.5B.")
R("until", "private", "San Francisco", HB, stage="Series A", conf="medium", co="US", edate="2025",
  note="Until Labs, reversible cryopreservation. Founders Fund led the $58M Series A of 2025.")
R("wave", "private", "Dakar", FIN, stage="Series A", conf="high", dispute=["status"], co="SN", co_src="web_verified", edate="2021-09", val_from=("y-combinator", "wave"), stale=True,
  flags=["model_disputes_source", "cite_pending"], hq_country_citation="https://www.fintechfutures.com/fintech/african-fintech-wave-hits-unicorn-status-with-200m-series-a-round",
  note="Wave Mobile Money (Senegal). Founders Fund co-led the $200M Series A of September 2021 at $1.7B; no priced round since. The SEC float join was to another registrant named Wave.")
R("wish", "acquired", "San Francisco", CON, stage="Growth", conf="medium", dispute=["hq_country"], co="US", edate="2014",
  flags=["model_disputes_source"], note="ContextLogic. Founders Fund led the $50M Series C of 2014. The Wish business was sold to Qoo10 in April 2024 for $173M; the listed shell is not the investment. The Wikidata country (JP) was a wrong join.")
R("workstream", None, "San Francisco", SAAS, stage="Series A", conf="high", dispute=["entry_stage"], edate="2020-10",
  note="Hourly-hiring software. Founders Fund led the $10M Series A of October 2020; the band anchored on the 2021 Series B.")
R("yammer", "acquired", "San Francisco", SAAS, note="Founders Fund led the $5M Series A of January 2009 with Charles River. Acq. by Microsoft, 2012, $1.2B.")
R("100plus", "acquired", "San Francisco", HB, stage="Seed", conf="medium", co="US", edate="2011",
  note="Health-prediction app; FF Angel led its 2011 seed. Acq. by Practice Fusion, February 2013.")
R("140-proof", "acquired", "San Francisco", MED, stage="undetermined", note="Social advertising network, on the firm's list from 2011; the round was not found. Acq. by AcuityAds, 2016.")
R("abcellera", "public", "Vancouver", HB, stage="Growth", conf="high", co="CA", co_src="web_verified", edate="2020-05", usd=4_260_000_000, vcite=SA % "abcl", vasof="2026-10-06",
  hq_country_citation="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1703057&type=10-K", flags=["cite_pending"],
  note="Antibody discovery. Fund VII entered in the $105M Series B of May 2020 (Series A2 holder on the IPO filing); Peter Thiel joined the board. Nasdaq: ABCL.")
R("affordit", "defunct", "San Francisco", FIN, stage="Seed", conf="low", co="US", edate="2011", flags=["stage_uncited"], note="Layaway-payments startup listed under the firm's FF Angel group; no trace after 2013.")
R("amicus", "defunct", "New York", SAAS, stage="Seed", conf="low", co="US", edate="2013", flags=["stage_uncited"], note="Fundraising software for non-profits (Y Combinator, 2012); on the firm's list 2013 to 2014. Wound down about 2016.")
R("atavist", "acquired", "New York", MED, stage="Seed", conf="medium", edate="2012-05", note="Digital longform publisher; FF Angel joined the $1.5M seed of May 2012. Acq. by Automattic, 2018.")
R("avalanche", "private", "New York", CRY, stage="undetermined", co="US", flags=["token_funded"], vr="below_1b",
  note="Ava Labs. The firm's position came through token sales of the Avalanche Foundation (2021), not a priced equity round, so stage and graduation read undetermined. AVAX's market value is not a mark on the company.")
R("backlight", "unknown", None, MED, stage="undetermined", co="US", flags=["country_prior"], note="On the firm's list in 2013 only; the company behind the name could not be placed.")
R("backplane", "defunct", "Palo Alto", CON, stage="Seed", conf="medium", co="US", edate="2011", note="Lady Gaga's community platform; FF Angel in the 2011 seed. Shut down 2016.")
R("betable", "private", "San Francisco", MED, stage="Seed", conf="medium", co="US", edate="2012", note="Real-money gaming platform (legal entity Rubicon Media); FF Angel in the 2012 seed, Founders Fund in the 2013 Series A.")
R("big-think", "private", "New York", MED, stage="undetermined", co="US", note="Ideas video publisher backed by Peter Thiel from 2007 and listed under FF Angel; the round a fund bought is not on record. Part of Freethink Media since 2022.")
R("billguard", "acquired", "New York", FIN, stage="Seed", conf="medium", dispute=["status"], edate="2011-04", flags=["model_disputes_source"],
  note="Card-fraud alerts; FF Angel in the $3M seed of April 2011, Founders Fund in the Series A that October. Acq. by Prosper, 2015; the pre-filled 'defunct' was the app's later closure.")
R("biofire", "private", "Broomfield", IND, stage="Series A", conf="medium", co="US", edate="2022", note="Biometric smart gun. Founders Fund led the $14M Series A of 2022.")
R("blend", None, "San Francisco", FIN, stage="Growth", conf="medium", edate="2016-01", val_from=("tiger-global-management", "blend"),
  note="Mortgage software. Founders Fund led the $40M Series C of January 2016 (Funds IV and V on the investors' rights agreement). NYSE: BLND.")
R("bolt-threads", "private", "San Leandro", IND, stage="Series A", conf="medium", edate="2015",
  note="Biomaterials. Founders Fund led the Series A (announced with the 2015 Series B). Listed through a SPAC in August 2024 and since delisted; operating privately.")
R("booshaka", "acquired", "San Francisco", MED, stage="Seed", conf="low", co="US", edate="2011", flags=["stage_uncited"], note="Facebook fan-ranking tool listed under FF Angel. Acq. by Sprinklr, 2015 (FF Angel, LLC is on Sprinklr's stockholder schedule).")
R("brit-co", "private", "San Francisco", MED, stage="Seed", conf="medium", co="US", edate="2012", note="Brit Morin's media company; Founders Fund in the $1.25M seed of 2012.")
R("bubble-fusion-labs", "unknown", None, CLI, stage="undetermined", co="US", flags=["country_prior"], note="On the firm's 2010 list only; no company of that name could be traced.")
R("built-robotics", "private", "San Francisco", IND, stage="Series A", conf="high", co="US", edate="2017-10", note="Autonomous construction equipment. Founders Fund led the $15M Series A of October 2017.")
R("business-connect-china", "unknown", "Shanghai", SAAS, stage="undetermined", co="CN", note="On the firm's list 2012 to 2014; no announcement of the round was found and the company has left no later trace.")
R("calibrate", "acquired", "New York", HB, stage="Growth", conf="high", co="US", edate="2021-08", note="Metabolic-health telemedicine. Founders Fund led the $100M Series B of August 2021. Restructured and sold to Madryn Asset Management, October 2023.")
R("carwoo", "acquired", "Burlingame", CON, stage="Seed", conf="low", co="US", edate="2010", flags=["stage_uncited"], note="Car-buying marketplace (Y Combinator) listed under FF Angel. Acq. by TrueCar, 2012.")
R("causes", "acquired", "San Francisco", CON, stage="Series A", conf="medium", co="US", edate="2007",
  note="Sean Parker and Joe Green's company; Founders Fund led the $2.35M Series A of 2007. Merged into Brigade, 2014.")
write("c1-classification")
