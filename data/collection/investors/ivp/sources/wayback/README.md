# IVP archive layer: Common Crawl, not the Wayback Machine

The Internet Archive excludes ivp.com: web.archive.org answers 403 for every
ivp.com and www.ivp.com capture (decisions.md D8). This directory keeps the
layout the pipeline reads, but its contents come from Common Crawl:

- `parsed/<year>.json` is written by `scratch/parse-cc-ivp.py` from the CC
  captures `scratch/pull-cc-ivp.py` fetched (index pass over every CC crawl
  since 2013, then one capture per URL per year). One row per company per
  capture year, with `snapshot_ts`, the page `path` that named it, the
  `surface` (Gen A listing card, Gen B company page, portfolio slider or
  listing), the firm's own `invest_year` where the page states one, and
  `capture_url`, the `index.commoncrawl.org` record of that capture, which
  `build-company-base.py` (458fcc7) uses as the row's archive citation.
- `partner-roster.json` is curated, not crawled (decisions.md D9): the live
  team, the managing directors on IVP's own fund Form Ds, the CC team pages
  and press-dated windows, one `basis` line per person.

The firm's fields that the build does not read (the Gen A outcome line, the
Gen B Status, Location and Leadership) are kept in
`sources/site/cc-listings.json` for the judge.
