# Project A run log (PRO-102)

Kickoff 2026-09-30 ~11:40 local (machine clock EDT) on Erik's "please collect Project A". One session, one run, slug `project-a-ventures`.

## Usage line at kickoff (get_usage)
- 5-hour limit 6% (resets 19:40 UTC)
- Weekly, all models: 14% (resets 2026-10-06 18:00 UTC)
- Weekly, Fable: 1%
- Extra usage: disabled, 24% (EUR 12.14 of 50)

## Siblings on this checkout at kickoff
- Live sessions: NEA collection, Visionaries Club collection (both started ~1 min before this one), Tiger Global collection (idle), Social Profile Coverage (waiting).
- In-flight markers present: atomico, bain-capital-ventures, founders-fund, general-catalyst (closed runs whose markers were never removed; not this session's to touch).
- IA cooldown: a sibling hit the IA firewall about 11:47; machine-wide cooldown 60 min. The project-a.com and project-a.vc CDX enumerations landed before it (scratch/cdx/).

## Prompt count
1. kickoff ("please collect Project A")
2. "continue" (16:03 local, while the run waited out the archive cooldown; no correction)

## In-flight marker
Written at kickoff by hand (run.py in_flight_mark shape), before any base build.

## Layer notes
- Live site: www.project-a.vc is Next.js on Sanity (project nykgtoh6); the public GROQ API serves the whole dataset: 114 portfolioCompany docs (entry year, entry round `projectInvestedAt`, fund, status, HQ, industries, board partner), 25 team personas (department investments / operations), 44 articles, 6 funds. scratch/sanity.py.
- Archive: project-a.com 2012-2025. Common Crawl (static cluster.idx route, scratch/cc-cluster.py + cc-fetch.py, copied from Northzone) holds the listing in 2013 and 2016-2024 plus ~250 per-company pages 2016-2019 and the 2020-2024 team pages. Four site generations parsed by scratch/archive_listings.py: WordPress gallery 2012-2014, Kirby 2015-2018 (portfoliList__item, --former flag, investment themes), LogoTile 2019, Next.js/Contentful 2020-2024 (venture records: status, founded, dateOfInvestment, investment round word, investmentType VC / PE Co-Investment, location, segment).
- The 2020-2024 Contentful dateOfInvestment is real in the earliest captures (Voi 2019-03-01 in 2020) and overwritten with 2021-12-25/26 placeholders from late 2021; the parser reads the earliest capture and drops those placeholders.
- Team 2020-2024: 264 people on the archived pages, types Operations 217, Operational 71, Investment 26, Management 14, Funds 12, Team Leads 15, Lead 8, Partner 6 (scratch/team-archive-2020-2024.json). Roster = 30 investing people (sources/wayback/partner-roster.json).
- EDGAR: 4 fund Form D filers from company search + Project A Opportunity II (folded in by the sweep); Form D roster sweep 108 accessions / 62 issuers, nearly all homonyms (Benno Fischer at AllianzGI, several Jack/John Wangs); real: Pactum AI (Sander), misterb&b and SFO84 Inc. (Waitz). Full-text sweep: one third-party registrant, Demand Media 2014 (S-3 / 424B3: the Saatchi Online sale).
- ADV: PROJECT A VENTURES MANAGEMENT GMBH, CRD 319556, ERA, annual amendment 2026-03-18; 7.B: Ventures II-V, Opportunity II/IIA, Security I, Silver Stone GmbH & Co. KG; $2.756B total (sources/registers/adv-7b.json, hand-read after the generic parser mis-paired values).
