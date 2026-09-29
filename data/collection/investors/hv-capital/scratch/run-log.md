# HV Capital run log (PRO-104)

Kickoff 2026-09-29 ~17:40 UTC on Erik's "please collect HV Capital". One session, one run, slug `hv-capital`.

## Usage line at kickoff (get_usage, 17:48 UTC)
- 5-hour limit 74% (resets 19:00 UTC)
- Weekly, all models: 71% (resets 18:00 UTC 2026-09-29, i.e. within minutes)
- Weekly, Fable: 6%
- Extra usage: disabled, 24% (EUR 12.14 of 50)

## Siblings on this checkout at kickoff
- Live sessions: Northzone (started ~17:47), TCV (~17:47), ICONIQ, GV, Tiger Global.
- In-flight markers present: atomico, bain-capital-ventures, founders-fund, general-catalyst, tiger-global-management (the first three and GC are closed runs whose markers were never removed; not this session's to touch).
- IA cooldown at kickoff: 0 s.

## Prompt count
1. kickoff ("please collect HV Capital")

## In-flight marker
Written at kickoff by hand (same shape as run.py in_flight_mark), before any base build, so no sibling's verify reads this book half-built (Balderton lesson, s12 write-back candidate).

## Layer notes
- Live site: hvcapital.com is Next.js App Router on Storyblok; the company list loads client-side, but the page's own export button calls /api/portfolio-csv?lang=en, which returns the firm's whole list as CSV (154 rows: Founded, Founders, HV Entry year, HQ, Funding fund, current Stage, Stage at Entry, Status, Categories, Website). Saved as sources/site/portfolio-2026.csv, reshaped to sources/site/companies-2026.json.
- Archive: holtzbrinck-ventures.com 2006-2018 (three CMS generations: 2006-2010 phpwcms per-company pages with the whole portfolio/exits list in the subnav; 2011-2015 Dutyfarm CMS with the pf-teaser grid; 2015-2018 WordPress /portfolio/ and /filterportfolio/), hvcapital.com 2020-2021 WordPress Divi /companies, 2022-2025 Next.js /_next/data/<build>/companies.json (223 companies in the 2025-01 build, with entry_date, founded_date, partners, city, country, current_stage).
