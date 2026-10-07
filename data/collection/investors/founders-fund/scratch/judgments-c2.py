"""Classification, chunk 2 (cdd .. ripple), and two membership rulings on listed rows."""
from jl import *
SA = "https://stockanalysis.com/stocks/%s/market-cap/"
NM("friendster", "D2/T2: Peter Thiel backed Friendster personally in its 2003 angel round, two years before the firm existed; the firm listed it from 2010 to 2012, but no fund of the firm is on any Friendster round. A founder's angel check stays out even where the firm lists it (COLLECTION.md s1, T2).", conf="medium")
NM("fbfund", "T5: fbFund was the seed fund Facebook ran with Accel and Founders Fund; a commitment to a fund is not an operating-company position. Its companies are rows where a fund of the firm invested (Inigral, Life360, Wildfire).")
R("cdd", "private", "Burlingame", HB, stage="undetermined", co="US", note="Collaborative Drug Discovery; on Fund I's first list (2007) and still listed in 2014. The spin-out round the fund backed carries no round name in any source read.")
R("cherry", None, "San Francisco", CON, stage="Seed", conf="medium", dispute=["hq_country"], co="US", edate="2011", flags=["model_disputes_source"],
  note="On-demand car wash by PayPal alumni; FF Angel in the 2011 seed. Acq. by Lyft, 2013. The Wikidata country was a wrong join.")
R("chronosphere", "acquired", "New York", DATA, stage="Growth", conf="medium", co="US", edate="2021-10", note="Observability platform. Founders Fund joined the $200M Series C of October 2021. Acq. by Palo Alto Networks, $3.35B, announced November 2025.")
R("collective-health", "private", "San Francisco", HB, stage="Series A", conf="medium", co="US", edate="2014", val_from=("new-enterprise-associates", "collective-health"), stale=True,
  flags=["cite_pending"], note="Employer health benefits. Founders Fund backed the 2014 Series A and the Series B that October. Last priced round May 2021 at $1.5B.")
R("compass", "public", "New York", CON, stage="Seed", conf="high", dispute=["status", "hq_country"], co="US", edate="2012", usd=7_040_000_000, vcite=SA % "comp", vasof="2026-10-06",
  flags=["model_disputes_source", "cite_pending"], note="Urban Compass until 2015. FF Angel IV, LLC bought into the $8M seed of 2012 and is on the investors' rights agreement filed with the 2021 IPO. NYSE: COMP. The pre-filled 'acquired' and country were a wrong Wikidata join.")
R("coolchip", "unknown", "Somerville", IND, stage="Seed", conf="low", co="US", edate="2012", flags=["stage_uncited"], note="CoolChip Technologies, kinetic cooling for electronics; listed under FF Angel. No recent trace.")
R("counsyl", "acquired", "South San Francisco", HB, stage="undetermined", note="Carrier screening. The funds held from before 2013; the round they first bought is not named in the sources read. Acq. by Myriad Genetics, 2018, $375M.")
R("cover", "private", "Los Angeles", IND, stage="Series A", conf="high", co="US", edate="2019", note="Cover Technologies, factory-built backyard homes. Founders Fund led the $10M Series A of 2019. Not the insurance app of the same name.")
R("crowdflower", "acquired", "San Francisco", AI, stage="Seed", conf="medium", co="US", edate="2009", note="Crowdsourced data labelling (later Figure Eight); FF Angel in the 2009 seed. Acq. by Appen, 2019.")
R("dynamic", "acquired", "San Francisco", CRY, stage="Series A", conf="medium", co="US", edate="2023", note="Dynamic Labs, wallet authentication. Founders Fund and a16z crypto led the $13.5M Series A. Acq. by Fireblocks, 2025.")
R("earable", "private", "Boulder", HB, stage="Series A", conf="medium", co="US", edate="2022", note="Earable Neuroscience, sleep-tech headband. Founders Fund led the $6.6M Series A of 2022.")
R("engage-com", "defunct", None, CON, stage="Series A", conf="low", co="US", edate="2006", flags=["stage_uncited", "country_prior"], note="Online dating site on Fund I's first list (2006); closed by 2009.")
R("estately", "private", "Seattle", CON, stage="Seed", conf="low", co="US", edate="2011", flags=["stage_uncited"], note="Online real-estate brokerage listed under FF Angel; still operating.")
R("fanbridge", "unknown", "New York", MED, stage="undetermined", co="US", note="Fan-relationship tools for musicians, listed under FF Angel; which round the vehicle joined is not on record, and the company has gone quiet.")
R("freeform", "private", "Hawthorne", IND, stage="Series A", conf="medium", co="US", edate="2023", note="AI-driven metal 3D printing by former SpaceX engineers. Founders Fund joined the $45M Series A of 2023.")
R("frogmetrics", "defunct", "San Francisco", SAAS, stage="Seed", conf="medium", co="US", edate="2008", note="Customer-feedback devices (Y Combinator, summer 2008); FF Angel seed. Closed about 2011.")
R("gazillion", "defunct", "San Mateo", MED, stage="undetermined", co="US", note="Gazillion Entertainment (Marvel Heroes). On the firm's list from 2010; the round is not named in the sources read. Shut down November 2017.")
R("geckogo", "unknown", None, CON, stage="Seed", conf="low", co="US", edate="2010", flags=["stage_uncited", "country_prior"], note="Travel-guide site (Y Combinator) on the firm's list 2012 to 2014; no later trace.")
R("geni", None, "Los Angeles", CON, stage="Series A", conf="medium", dispute=["hq_country"], co="US", edate="2007-01", flags=["model_disputes_source"],
  note="David Sacks's genealogy network. Founders Fund led the first $1.5M round of January 2007. Acq. by MyHeritage, 2012. The Wikidata country was a wrong join.")
R("glow", "private", "San Francisco", HB, stage="Series A", conf="high", co="US", edate="2013-08", note="Max Levchin's fertility app (Upward Labs). Founders Fund and Andreessen Horowitz led the $6M Series A of August 2013. Not the 2026 security company of the same name.")
R("gotenna", "private", "New York", IND, stage="Growth", conf="medium", co="US", edate="2019", note="Mesh-network radios. Founders Fund led the $24M Series C of 2019.")
R("halcyon-molecular", "defunct", "Redwood City", HB, stage="undetermined", note="DNA sequencing; Luke Nosek on the board and Founders Fund the lead backer (2009 to 2010). The first fund round carries no name in the sources read. Closed 2012.")
R("hampton-creek", "private", "Alameda", CON, stage="undetermined", co="US", flags=["needs_web_value"], note="Now Eat Just. On the firm's list from 2013; the round the fund first bought is not established. Reported at $1.1B in 2016; to be pinned or dropped in the web pass.")
R("harbor", "acquired", "San Francisco", CRY, stage="Growth", conf="high", co="US", edate="2018-04", note="Tokenised-securities platform. Founders Fund led the $28M Series B of April 2018. Acq. by BitGo, 2020.")
R("hipchat", "acquired", "San Francisco", SAAS, stage="Seed", conf="medium", co="US", edate="2010", note="Team chat; FF Angel in the 2010 angel round. Acq. by Atlassian, March 2012.")
R("hipswap", "defunct", "Los Angeles", CON, stage="Seed", conf="low", co="US", edate="2011", flags=["stage_uncited"], note="Mobile local marketplace listed under FF Angel; closed about 2013.")
R("hubble", "private", "New York", CON, stage="Series A", conf="medium", co="US", edate="2017", note="Hubble Contacts, subscription contact lenses. Founders Fund led the $10M Series A of 2017. Not the London office-space marketplace.")
R("immunepath", "defunct", "Foster City", HB, stage="Seed", conf="medium", co="US", edate="2010", note="Stem-cell immunotherapy; Founders Fund seed of 2010. Wound down in 2012.")
R("instacanvas", "acquired", "Santa Monica", CON, stage="Seed", conf="medium", co="US", edate="2012", note="Instagram print marketplace (later Twenty20); FF Angel in the $1.7M seed of 2012. Acq. by Envato, 2019.")
R("ironport", None, "San Bruno", SEC, stage="undetermined", note="Email security. On Fund I's first list (2006), before Cisco bought it in January 2007 for $830M; the late round the fund joined is not named in the sources read.")
R("isocket", "acquired", "Burlingame", MED, stage="Seed", conf="low", co="US", edate="2010", flags=["stage_uncited"], note="Direct ad-sales platform listed under FF Angel. Acq. by Rubicon Project, 2014.")
R("jawfish-games", "defunct", "Seattle", MED, stage="undetermined", co="US", note="Real-time mobile tournaments. Founders Fund led the $3.55M first round of December 2011, which the reports do not name; listed under FF Angel. Closed about 2016.")
R("jaxtr", "acquired", "Menlo Park", CON, stage="Series A", conf="low", co="US", edate="2006", flags=["stage_uncited"], note="Social voice calling, on Fund I's list from 2007. Acq. by Sabse Technologies, 2009.")
R("knewton", "acquired", "New York", SAAS, stage="Growth", src="first_party", conf="high", edate="2011-10",
  scite="https://web.archive.org/web/20130601000000/http://www.foundersfund.com/company/knewton",
  note="The firm's own company page lists 'Founders Fund Leads $33 Million D Round In Learning Startup Knewton' (14 October 2011). Assets acq. by Wiley, 2019.")
R("koders", "acquired", None, DEV, stage="undetermined", co="US", flags=["country_prior"], note="Source-code search engine on Fund I's first list (2006). Acq. by Black Duck Software, 2008. The round is not named in the sources read.")
R("lava", "unknown", None, None, stage="undetermined", co="US", vr="undetermined", flags=["identity_unresolved", "country_prior"],
  note="A /company/lava page captured in 2025; the page body could not be read during the archive block of 2026-10-06 and several companies carry the name, so the row is not yet identified.")
R("leaflink", "private", "New York", SAAS, stage="Growth", conf="medium", co="US", edate="2020-12", note="Cannabis wholesale marketplace. Founders Fund led the $40M Series C of December 2020.")
R("leap-motion", None, "San Francisco", IND, stage="Seed", conf="medium", dispute=["hq_country"], co="US", edate="2011", flags=["model_disputes_source"],
  note="Hand-tracking sensor. Founders Fund joined the $1.3M seed of 2011 and co-led the $12.75M Series A of May 2012. Acq. by Ultrahaptics, 2019. The Wikidata country was a wrong join.")
R("life360", None, "San Mateo", CON, stage="Seed", conf="low", co="US", edate="2010", val_from=("bessemer-venture-partners", "life360"), flags=["stage_uncited", "cite_pending"],
  note="Family-location app; an fbFund company listed under FF Angel (2010-11 angel rounds). Nasdaq: LIF.")
R("lore", "acquired", "New York", SAAS, stage="Seed", conf="medium", edate="2011-06", note="Coursekit, later Lore. Founders Fund in the $1M seed of June 2011 and lead of the $5M Series A that November. Acq. by Noodle, 2013.")
R("material", "private", "Redwood City", SEC, stage="Growth", conf="medium", co="US", edate="2022-05", flags=["needs_web_value"], note="Material Security, email security. Founders Fund led the $100M Series C of May 2022, reported at $1.1B; to be pinned in the web pass.")
R("mint", "acquired", "Mountain View", FIN, stage="Growth", conf="medium", co="US", edate="2008-03", note="Mint.com. Founders Fund joined the $12M Series B of March 2008. Acq. by Intuit, 2009, $170M.")
R("moat", "acquired", "New York", MED, stage="Seed", conf="medium", co="US", edate="2011", note="Ad analytics. Founders Fund in the 2011 seed. Acq. by Oracle, 2017, about $850M.")
R("modern-animal", "private", "Los Angeles", CON, stage="Series A", conf="medium", co="US", edate="2019", note="Membership veterinary clinics. Founders Fund led the Series A of 2019 and the $75.5M Series B of 2021.")
R("modern-health", "private", "San Francisco", HB, stage="Growth", conf="medium", co="US", edate="2020-01", val_from=("y-combinator", "modern-health"), stale=True, flags=["cite_pending"],
  note="Workplace mental health. Founders Fund led the $31M Series B of January 2020. Last priced round February 2021 at $1.17B.")
R("mosaic", "private", "San Diego", FIN, stage="Growth", conf="high", dispute=["status", "valuation_range"], edate="2022-03", vr="below_1b", flags=["model_disputes_source"],
  note="Finance planning software. 'Mosaic Closes $25 Million Series B, Led by Founders Fund' (Business Wire, 2022-03-30). The pre-filled public float belonged to The Mosaic Company, the fertiliser producer.", valuation_usd=None, valuation_source=None)
R("natera", None, "Austin", HB, stage="undetermined", usd=57_750_000_000, vcite=SA % "ntra", vasof="2026-10-06", flags=["model_disputes_source"],
  note="Gene Security Network until 2012. The Founders Fund II, LP and its side funds signed the investors' rights agreement filed with the 2015 IPO; the series they first bought (2007 to 2010) was not read out of the prospectus. Nasdaq: NTRA.")
R("navia", "unknown", None, None, stage="undetermined", co="US", vr="undetermined", flags=["identity_unresolved", "country_prior"],
  note="Listed as 'Navia' on the firm's site 2010 to 2012; no company could be tied to the name from the list alone, and the profile page was not readable during the archive block.")
R("neon", None, "San Francisco", DATA, stage="Growth", conf="medium", dispute=["hq_country"], co="US", edate="2023-08", flags=["model_disputes_source"],
  note="Serverless Postgres. Founders Fund joined the $46M Series B of August 2023. Acq. by Databricks, 2025.")
R("networkedblogs", "unknown", None, MED, stage="Seed", conf="low", co="US", edate="2010", flags=["stage_uncited", "country_prior"], note="Blog syndication app for Facebook (Ninua), on the firm's list 2012 to 2014; no later trace.")
R("newfront", None, "San Francisco", FIN, stage="Growth", conf="medium", edate="2020", note="Insurance brokerage. Founders Fund co-led the $100M Series C of 2020 with Meritech. Acq. by WTW, 2025.")
R("nextivity", "private", "San Diego", IND, stage="undetermined", co="US", note="Cellular signal boosters (Cel-Fi). A Fund I position on the 2010 list; the round the fund joined is not named in the sources read.")
R("niantic", "acquired", "San Francisco", MED, stage="Growth", conf="medium", dispute=["status", "valuation_range"], edate="2017-11", vr="below_1b", valuation_usd=None, valuation_source=None,
  flags=["model_disputes_source"], note="Founders Fund joined the $200M Series B of November 2017. The games business was sold to Scopely for $3.5B in 2025 and the rest spun out as Niantic Spatial; read as acquired, as the sibling books do.")
R("olx", "acquired", "New York", CON, stage="Growth", conf="medium", co="US", edate="2008", note="Online classifieds. Founders Fund joined the 2008 round with Nexus, Bessemer and General Catalyst. Acq. by Naspers, 2010.")
R("openstore", "private", "Miami", CON, stage="Series A", conf="medium", co="US", edate="2021", note="Keith Rabois's Shopify-brand aggregator (Miami Labs, Inc.); Founders Fund in the $30M Series A of 2021 with Atomic and Khosla.")
R("ostrovok", "private", "Moscow", CON, stage="Seed", conf="low", co="RU", edate="2011", flags=["stage_uncited"], note="Russian online travel agency (Emerging Travel Group), listed under FF Angel.")
R("oyster", "defunct", "New York", MED, stage="Seed", conf="high", co="US", edate="2012-10", note="E-book subscription. Founders Fund led the $3M seed of October 2012. Google hired the team in 2015 and the service closed in 2016: defunct under the acqui-hire rule.")
R("path", "acquired", "San Francisco", CON, stage="Seed", conf="medium", co="US", edate="2010", note="Dave Morin's private social network; FF Angel in the 2010 seed. Acq. by Daum Kakao, 2015.")
R("pathway-genomics", "unknown", "San Diego", HB, stage="undetermined", note="Consumer genetic testing. Founders Fund led its 2009 financing, which the reports do not name. The company stopped operating about 2019; no sale or closure report found.")
R("pharmacofore", "private", "San Carlos", HB, stage="undetermined", co="US", flags=["identity_conflated"], note="Renamed Signature Therapeutics in 2012; the same investment as the row of that name, to be merged at the rebuild.")
R("planet-labs", "public", "San Francisco", IND, stage="Series A", conf="medium", edate="2013", usd=6_760_000_000, vcite=SA % "pl", vasof="2026-10-06", flags=["cite_pending"],
  note="Earth-imaging satellites. Founders Fund joined the $13.1M Series A of 2013. NYSE: PL.")
R("portalarium", "acquired", "Austin", MED, stage="Seed", conf="low", edate="2011", flags=["stage_uncited"], note="Richard Garriott's studio, listed under FF Angel. Its game and assets were sold to Catnip Games in 2019.")
R("powerset", None, "San Francisco", AI, stage="Series A", conf="high", edate="2006-11", note="Natural-language search. Founders Fund and Foundation Capital led the $12.5M Series A of November 2006. Acq. by Microsoft, 2008.")
R("practice-fusion", "acquired", "San Francisco", HB, stage="Growth", conf="high", edate="2011-04", note="Free electronic health records. Founders Fund led the $23M Series B of April 2011. Acq. by Allscripts, 2018, $100M.")
R("quid", "acquired", "San Francisco", AI, stage="undetermined", co="US", note="Text-analytics visualisation. On the firm's list from 2011; the first fund round is not named in the sources read. Merged with NetBase in 2020.")
R("radiant", "private", "El Segundo", CLI, stage="Series A", conf="low", co="US", edate="2022", val_from=("union-square-ventures", "radiant"), flags=["stage_uncited", "cite_pending"],
  note="Portable nuclear microreactors. Founders Fund backed the early rounds (2022) and the later ones.")
R("radius", "acquired", "San Francisco", DATA, stage="Growth", conf="medium", dispute=["status", "hq_country"], co="US", edate="2014-09", flags=["model_disputes_source"],
  note="Radius Intelligence, B2B marketing data. Founders Fund led the $54.7M Series C of September 2014. Acq. by Kabbage, 2019. The pre-filled 'defunct' and country were a wrong Wikidata join.")
R("rapleaf", "acquired", "San Francisco", DATA, stage="Series A", conf="low", edate="2007", flags=["stage_uncited"], note="Consumer data. Thiel backed it personally in 2006 and Founders Fund joined the 2007 Series A. Acq. by TowerData, 2013.")
R("raptr", "defunct", "Mountain View", MED, stage="Series A", conf="medium", co="US", edate="2008", note="Gaming social network. Founders Fund and Accel in the $12M Series A of 2008. Shut down September 2017.")
R("readyforce", "defunct", "San Francisco", SAAS, stage="Seed", conf="low", co="US", edate="2011", flags=["stage_uncited"], note="College recruiting network listed under FF Angel; closed about 2014.")
R("resilience", "private", "San Diego", HB, stage="Growth", conf="low", co="US", edate="2021", flags=["stage_uncited"], note="National Resilience, biomanufacturing. Founders Fund is among the backers of the 2020-21 rounds.")
R("retel-technologies", "defunct", "Chicago", AI, stage="Seed", conf="low", co="US", edate="2011", flags=["stage_uncited"], note="Retail video analytics listed under FF Angel; no trace after about 2015.")
R("ringadoc", "acquired", "San Francisco", HB, stage="Seed", conf="medium", co="US", edate="2011", note="After-hours telemedicine; FF Angel seed. Acq. by Practice Fusion, 2015.")
R("ripple", None, "San Francisco", CRY, stage="Seed", conf="medium", edate="2013-04", dispute=["valuation_range"], val_from=("lightspeed", "ripple"), flags=["cite_pending"],
  note="OpenCoin at the time: FF Angel joined the angel round of April 2013 with Andreessen Horowitz and Lightspeed. $500M round of November 2025 at $40B.")
write("c2-classification")
