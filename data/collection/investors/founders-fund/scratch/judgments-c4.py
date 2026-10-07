"""Classification of the name-match members, and stemcentrx's status."""
from jl import *
C("stemcentrx", status="acquired", hq_country="US", hq_country_source="model_knowledge", valuation_usd=None)
R("8i-corp", "private", "Los Angeles", MED, dispute=["hq_country"], co="US", flags=["model_disputes_source"],
  note="Volumetric video. Founders Fund's science vehicle joined the $13.5M Series A of October 2015, Scott Nolan on the board; the 2016 filing is the round's later close. Founded in Wellington, run from Los Angeles.")
R("all-day-technologies-inc", "unknown", "San Francisco", CON, note="All Day Kitchens (Virtual Kitchen Co. until 2021). Founders Fund led the $20M Series B of September 2020. Reported to have ceased operating in 2023; no closure report was found to cite.")
R("cargo-systems-inc", "unknown", "New York", CON, note="In-car commerce for ride-hail drivers. Founders Fund led the $22.5M Series A of September 2018. The service stopped during 2020-21; no closure or sale report found.")
R("ghost-autonomy-inc", "defunct", "Mountain View", AI, stage="Growth", conf="high", src="web_verified", dispute=["entry_stage"], edate="2021-07",
  scite="https://techcrunch.com/2024/04/03/openai-backed-ghost-autonomy-shuts-down/",
  note="Founders Fund entered in the $100M Series D of July 2021 (Keith Rabois, by then at the firm, had backed the 2018 Series A from Khosla). Shut down 3 April 2024.")
R("homee-interiors-inc", "unknown", "Los Angeles", CON, note="Homee, renamed Hutch in 2017: interior-design app. 'Homee raises $5M from Founders Fund' (TechCrunch, July 2016). No trace of the app after about 2020.")
R("invisibly-inc", "private", "St. Louis", MED, note="Jim McKelvey's consumer-data company; Scott Nolan a director on the 2018 filings.")
R("lula-technologies-inc", "private", "Miami", FIN, stage="Series A", src="web_verified", conf="high", edate="2021-07",
  scite="https://refreshmiami.com/news/miami-startup-lula-raises-18m-series-a-round-led-by-founders-fund-khosla-ventures/",
  note="Insurance infrastructure. $18M Series A of July 2021 led by Founders Fund and Khosla Ventures.")
R("modumetal-inc", "unknown", "Seattle", IND, stage="Growth", conf="medium", co="US", edate="2015-06",
  note="Nanolaminated metals. Founders Fund led the $33.5M round of June 2015 (GeekWire), the company's third institutional round. No report of its current state was found.")
R("orgio-inc", "private", "New York", SAAS, stage="Series A", src="web_verified", conf="high", edate="2020-02",
  scite="https://techcrunch.com/2020/02/19/the-org-nabs-8-5m-led-by-founders-fund-to-build-a-global-database-of-company-org-charts/",
  note="The Org (Orgio, Inc.), public org charts. $8.5M Series A of February 2020 led by Founders Fund.")
R("plethora-corp", "unknown", "San Francisco", IND, note="On-demand CNC manufacturing; Scott Nolan a director from the 2018 filing. No report of its current state was found.")
R("royal-markets-inc", "private", "Austin", CRY, stage="Seed", src="web_verified", conf="high", dispute=["entry_stage"], edate="2021-08",
  scite="https://www.coindesk.com/business/2021/08/26/3lau-raises-16m-to-tokenize-music-royalties-for-artists-and-fans",
  seed_to_a_graduation="graduated", graduation_source="web_verified", graduation_confidence="high", graduation_citation="https://www.digitalmusicnews.com/2021/11/23/royal-series-a/",
  note="Royal, 3LAU's music-rights platform. $16M seed of August 2021 led by Founders Fund and Paradigm; $55M Series A that November led by Andreessen Horowitz. The band read the seed's size as a Series A.")
R("runtitle-inc", "unknown", "Austin", DATA, stage="undetermined", note="Mineral-title data. Geoff Lewis joined the board at the $8M round of September 2015, which no report names. No report of its current state was found.")
R("tribogenics-inc", "unknown", "Los Angeles", IND, note="Portable X-ray sources; Bruce Gibney on the board for the 2011 and 2012 rounds. No report of its current state was found.")
R("zenreach-inc", "private", "San Francisco", SAAS, note="Wi-Fi marketing (now Adentro). Peter Thiel and Napoleon Ta directors on the $30M round of March 2017.")
write("c4-classification")
