"""Membership, the 75 Form D name-match rows, judged by person (COLLECTION.md s3:
cluster-first). Tenures: decisions.md and sources/wayback/partner-roster.json."""
from jl import *
# --- Keith Rabois: angel to 2010, Square COO 2010-13, Khosla 2013 to early 2019, Founders Fund 2019-03 to 2024-01, Khosla after
for s, why in [
 ("chain-inc", "T4: 2014 seat, Rabois at Khosla Ventures, which led Chain's round."),
 ("decorati-inc", "T4: 2010 seat, a personal angel position nine years before his Founders Fund tenure."),
 ("esper-technologies-inc", "T4: 2016 seat, Rabois at Khosla Ventures."),
 ("lightyear-corp", "T4: 2018 seat, Rabois at Khosla Ventures."),
 ("medisas-inc", "T4: 2016 seat, Rabois at Khosla Ventures."),
 ("milo-com-inc", "T4: 2009 seat, a personal angel position before any venture tenure."),
 ("offline-labs-inc", "T4: 2013 seat on Offline Labs (Sosh), Khosla Ventures' round after Rabois joined Khosla in March 2013."),
 ("sportelligence-inc", "T4: 2010 seat, a personal angel position."),
 ("reddit-inc", "T4: Rabois is a director of record on Reddit's 2017 and 2019 filings; the seat begins in his Khosla years and no Founders Fund vehicle is on any Reddit round or on its registration statement."),
 ("square-inc", "T4: an operator's seat (chief operating officer 2010-13); config trap."),
 ("yelp-inc", "T4: board seat and personal investment a decade before the Founders Fund tenure; config trap."),
 ("xoom-corp", "T4: Kevin Hartz co-founded Xoom and Rabois sat its board personally; both seats predate their tenures; config trap."),
]: NM(s, why)
NM("mach-industries-inc", "T4: the two roster names on the 2025 filing are Geoff Lewis (Bedrock, which led the Series A) and Keith Rabois (Khosla Ventures, which led the Series B); both had left Founders Fund, and no Founders Fund vehicle is named in either round.")
NM("homevest-inc", "Director of record in tenure (Series A, 2019-08), but the issuer's identity never resolved: a New York company filed only as Homevest Inc., no announcement, no trade name found (EDGAR, two web searches, three news searches, 2026-10-06). Under the narrowing of the director-of-record pattern (COLLECTION.md s1) an unresolved issuer is the personal-seat class.", cls="knowledge", conf="medium")
NM("spotmap-inc", "Director of record in tenure (2021-05, $15M, industry 'Restaurants'), but the issuer's identity never resolved: no announcement and no trade name found for SpotMap, Inc. (EDGAR, web and news searches, 2026-10-06). Unresolved issuer: the personal-seat class (COLLECTION.md s1).", cls="knowledge", conf="medium")
V("orgio-inc", "member", "web", "high", "Orgio, Inc. is The Org (New York): 'The Org nabs $8.5M led by Founders Fund' (TechCrunch, 2020-02-19), the round and month of the Form D on which Keith Rabois is a director, in tenure.", "https://techcrunch.com/2020/02/19/the-org-nabs-8-5m-led-by-founders-fund-to-build-a-global-database-of-company-org-charts/")
V("all-day-technologies-inc", "member", "web", "high", "All Day Technologies, Inc. (formerly Virtual Kitchen Co., same CIK): the $20M round of September 2020 was led by Founders Fund (CNBC, 2020-09-08), Keith Rabois joining the board, in tenure.", "https://www.cnbc.com/2020/09/08/virtual-kitchen-led-by-ex-uber-execs-raises-20-million-from-founders.html")
V("virtual-kitchen-co", "member", "web", "high", "Same company as all-day-technologies-inc (EDGAR: All Day Technologies, Inc., formerly Virtual Kitchen Co., CIK 1778911); Founders Fund led its $20M round of September 2020 (CNBC). Merged at the next rebuild.", "https://www.cnbc.com/2020/09/08/virtual-kitchen-led-by-ex-uber-execs-raises-20-million-from-founders.html")
V("royal-markets-inc", "member", "web", "high", "Royal Markets, Inc. is Royal, 3LAU's music-rights platform: $16M seed of August 2021 led by Founders Fund and Paradigm (CoinDesk, 2021-08-26); Keith Rabois director, in tenure.", "https://www.coindesk.com/business/2021/08/26/3lau-raises-16m-to-tokenize-music-royalties-for-artists-and-fans")
V("ghost-autonomy-inc", "member", "web", "high", "Rabois's 2018 seat was Khosla's, but Founders Fund itself invested later: TechCrunch's shutdown report names 'Keith Rabois at Founders Fund' in the Series D and in the last $55M round (2024-04-03).", "https://techcrunch.com/2024/04/03/openai-backed-ghost-autonomy-shuts-down/")
V("indie-technologies-inc", "member", "formd_adjudicated", "high", "Indie Technologies, Inc. is the legal name of Found, the banking app for the self-employed, which the firm lists on its live site: the $59.7M filing of January 2022 is Found's $60M Series B led by Founders Fund and the $46M filing of June 2024 its Series C; Keith Rabois director on both. Merged into `found` at the next rebuild.", "https://foundersfund.com/company/found/")
V("miami-labs-inc", "member", "formd_adjudicated", "high", "Miami Labs, Inc. is OpenStore, the Miami company Keith Rabois co-founded in 2021 and the firm lists (/company/openstore): the $30M and $75M filings of 2021 are its Series A and B. Merged into `openstore` at the next rebuild.", "https://web.archive.org/web/2022/https://foundersfund.com/company/openstore/")
# --- Sean Parker: partner 2006-2014
NM("3dna-corp", "T4: 3dna Corp. is NationBuilder; its 2012 Series A was led by Andreessen Horowitz with Sean Parker investing and joining the board personally. No Founders Fund vehicle is named and the firm never listed it.", conf="medium")
NM("arsenal-biosciences-inc", "T4: Parker's seat (2020 on) is through the Parker Institute for Cancer Immunotherapy, six years after he left the firm.")
NM("tmunity-therapeutics-inc", "T4: Parker's seat (2018) is through the Parker Institute, after he left the firm.")
NM("brigade-media-llc", "T4: Brigade is Sean Parker's own company (founder and chairman, 2014), funded by Parker himself.")
NM("philotic-inc", "T4: Philotic is Sean Parker's own entity (Parker and Michael Polansky as executive officers, 2013).")
# --- Kevin Hartz: partner 2016-2018
NM("dotblu-inc", "T4: 2010 seat, a personal angel position six years before Hartz joined the firm.")
NM("eventbrite-inc", "T4: Kevin Hartz is Eventbrite's co-founder; config trap.")
NM("lookout-inc", "T4: Hartz has been a director of Flexilis/Lookout since 2009 as a personal angel investor; Lookout's rounds name Khosla, Accel, Index, Andreessen Horowitz and others, never a Founders Fund vehicle, and the firm never listed it.", conf="medium")
NM("thewordlab-co", "T4: 2024 seat, Hartz at A-Star, six years after leaving the firm.")
# --- Michael Polansky: 2009-2010, then Sean Parker's office
for s in ("elastic-projects-inc", "outer-biosciences-llc", "researchhub-technologies-inc"):
    NM(s, "T4: seat taken years after Polansky left the firm in 2010, through Sean Parker's entities.")
# --- Stephen Oskoui: partner 2015-2017, then Gigafund
for s, why in [("sana-benefits-inc", "2020 seat: Gigafund led Sana's rounds."), ("b-z-homes-inc", "2021 seat, Gigafund era."),
               ("othram-inc", "2021 seat, Gigafund era."), ("bloomtech-inc", "2024 seat on BloomTech (Lambda School), a Gigafund investment.")]:
    NM(s, "D3/T4: " + why + " Gigafund is a separate firm.")
NM("infoaxe-inc", "T4: a $105,000 filing of September 2015 with 'Steve Oskoui' as director; a personal angel position, no Founders Fund vehicle or announcement.", conf="medium")
V("homee-interiors-inc", "member", "web", "high", "'Homee raises $5M from Founders Fund and Tinder CEO' (TechCrunch, 2016-07-05); Stephen Oskoui director on the June 2016 filing, in tenure. The company renamed itself Hutch in 2017.", "https://techcrunch.com/2016/07/05/homee-raises-5m-from-founders-fund-and-tinder-ceo-to-help-you-furnish-your-place/")
V("hutch-interiors-inc", "member", "web", "high", "Same company as homee-interiors-inc: Homee renamed itself Hutch in 2017 (PYMNTS, 2017-06-19). Merged at the next rebuild.", "https://www.pymnts.com/news/retail/2017/how-mobile-app-homee-became-hutch-and-the-importance-of-the-right-pivot-in-the-competitive-landscape-of-interior-design-styles/")
# --- Geoff Lewis: partner 2012-2017, then Bedrock
NM("vercel-inc", "T4: 2021 seat, Bedrock led Vercel's Series C four years after Lewis left the firm.")
V("runtitle-inc", "member", "formd_adjudicated", "medium", "Geoff Lewis is a director of record on RunTitle's $8M filing of September 2015, in tenure (2012-2017); the issuer resolves (RunTitle, Austin, mineral-title data, later part of Enverus). Director-of-record pattern: an unannounced deal, flagged for the A/B pass.")
# --- Scott Nolan: partner 2011 to date
for s, what in [("8i-corp", "8i, the Wellington volumetric-video company ($20.4M, November 2016)"),
                ("plethora-corp", "Plethora, the San Francisco CNC manufacturing company (2018 on)"),
                ("invisibly-inc", "Invisibly, Jim McKelvey's St. Louis company (two filings, 2018)")]:
    V(s, "member", "formd_adjudicated", "medium", f"Scott Nolan, a current partner, is a director of record on the filings of {what}; the issuer resolves to a real operating company. Director-of-record pattern (COLLECTION.md s1), flagged for the A/B pass.")
# --- Napoleon Ta / Peter Thiel
V("zenreach-inc", "member", "formd_adjudicated", "medium", "Two current partners, Peter Thiel and Napoleon Ta, are directors of record on Zenreach's $30M filing of March 2017; the issuer resolves (Zenreach, San Francisco, Wi-Fi marketing). Director-of-record pattern, flagged for the A/B pass.")
# --- Jeffrey / Jeff Lewis: a different person from Geoff Lewis
for s in ("affl-associates-llc", "globaltmail-usa-inc", "i-of-the-tiger-inc", "ekostinger-inc"):
    NM(s, "Homonym: the filing names Jeffrey (Jeff) Lewis, not the firm's Geoff Lewis; nothing ties the issuer to Founders Fund.")
# --- Ryan Petersen: partner late 2022 to September 2023
NM("ocz-technology-group-inc", "Homonym: OCZ's chief executive was a different Ryan Petersen (2010 to 2013 filings), a decade before the Flexport founder's months at the firm.")
NM("blitsy-inc", "Homonym: a Chicago issuer's executive officer named Ryan Petersen in 2013 to 2015; not the Flexport founder, and nine years before his months at the firm.")
NM("rival-warz-llc", "Homonym: an Iowa LLC's executive officer named Ryan Petersen (2024).")
NM("lumen-inc", "Homonym or personal: a Portland issuer filing since 2015 with a $2M round in January 2023; no Founders Fund round is on record and the issuer does not fit the firm.", conf="medium")
# --- Ken Howery: partner 2005-2019
NM("popexpert-inc", "D2/T4: a $500,000 seed filing of 2013 with Howery as director; PopExpert's seed backers were individuals and Learn Capital, Howery among them personally. No Founders Fund vehicle or listing.", conf="medium")
V("careportal-inc", "member", "formd_adjudicated", "high", "Careportal, Inc. is the legal name of Cedar, the New York healthcare-billing company on the firm's live site: the five filings (2016-12 to 2021) are Cedar's Series A to D, Ken Howery director from the first. Merged into `cedar` at the next rebuild.", "https://foundersfund.com/company/cedar/")
# --- Cyan Banister: partner 2016-2020
NM("mimoco-inc", "T4: 2010-11 seat, a personal angel position five years before she joined the firm.")
NM("february-won-inc", "T4: 2010-12 seat, a personal angel position before she joined the firm.")
V("cargo-systems-inc", "member", "web", "high", "Cargo, the in-car commerce company: its $22.5M Series A of September 2018 was led by Founders Fund (Crunchbase News, 2018-09-24), Cyan Banister joining the board, in tenure.", "https://news.crunchbase.com/startups/founders-fund-likely-leads-22-5m-round-for-in-car-commerce-startup-cargo/")
# --- Joey Krug: Pantera Capital until 2023, partner from 2023
for s in ("wyre-inc", "transparent-financial-systems-inc", "coinme-inc", "zeroex-holdings-inc"):
    NM(s, "T4: seat taken while Joey Krug was co-chief investment officer of Pantera Capital (2017 to 2023), before he joined the firm.")
# --- others
V("modumetal-inc", "member", "web", "high", "'Peter Thiel's Founders Fund backs Modumetal' (GeekWire, 2015-06-08): the firm led the $33.5M round, Aaron VanDevender joining the board, in tenure.", "https://www.geekwire.com/2015/peter-thiels-founders-fund-backs-modumetal-a-creator-of-nanolaminated-parts-that-are-stronger-than-steel/")
V("lula-technologies-inc", "member", "web", "high", "Lula, the Miami insurance-infrastructure company: $18M Series A of July 2021 led by Founders Fund and Khosla Ventures (Refresh Miami, 2021-07-08), Delian Asparouhov director.", "https://refreshmiami.com/news/miami-startup-lula-raises-18m-series-a-round-led-by-founders-fund-khosla-ventures/")
V("tribogenics-inc", "member", "formd_adjudicated", "medium", "Bruce Gibney is a director of record on Tribogenics' 2011 and 2012 filings, in tenure; the issuer resolves (Tribogenics, Los Angeles, portable X-ray sources), and Wired's 2012 profile names Founders Fund among its backers.", "https://www.wired.com/2012/09/tribogenics/")
NM("hyperloop-technologies-inc", "T4: Justin Fishner-Wolfson's seat (2015 on) is 137 Ventures', four years after he left the firm.")
NM("teachstreet-inc", "T4: Dave McClure invested in TeachStreet personally in February 2008, before he ran FF Angel; no Founders Fund vehicle is on record.", conf="medium")
NM("better-cooking-co", "T4: 2025 seat, six years after Zachary Hargreaves left the firm.")
NM("vires-aeronautics-inc", "T4: Hargreaves was an executive officer of VIRES in 2013, three years before he joined the firm.")
NM("mom-project-inc", "T4: 2018 seat, Alda Leu Dennis at Initialized Capital, six years after leaving the firm.")
NM("modulo-bio-inc", "T4: 2024 seat, Alda Leu Dennis at Initialized Capital.")
NM("osaro-inc", "T4: Derik Pridmore is Osaro's founder and chief executive (2017 filing), six years after leaving the firm.")
NM("huntress-labs-inc", "T4: 2024 seat, Everett Randle at Kleiner Perkins, which led the round.")
write("m1-membership")
