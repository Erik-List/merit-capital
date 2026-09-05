# PRO-73 run log (scratch, regenerable narrative)

2026-09-04, single session, merged shape (PRO-71): base + classification + profile in one run.
Prompt count so far: 1 (kickoff "Please collect cherry ventures").

## Kickoff facts pinned
- cherry.vc is a Webflow site (2026): /founders list (90 links), /founder-companies/<slug> pages (94 in the
  sitemap, incl. two "<x>-information-missing" placeholders), /team/<slug> (39: 23 staff + 16 network/departed),
  /news/<slug> (118). No CMS API; sitemap + per-page fetch (ladder step 5). Fields per company: description,
  mission, founders, founded (a mixed field: launch year for the old book, announcement date since 2024),
  industry, location, website; the list page carries an "(EXIT)" marker and an industry tag.
- The 2024-03 to 2025 Next.js site's Sanity dataset (project 763y4e9t) is still publicly queryable: 86 company
  docs (name, slug, date, href, founders, tags incl. an "Exit" tag), 108 articles with body text (2019-2024
  migrated posts), 31 personas.
- Archived WordPress site 2016-11 to 2024-01: /portfolio/ listings parsed per year (2016 28, 2017 31, 2018 36,
  2019 42 with data-invested epoch dates and an 'Investment: Seed/Series A' label; 2020-2023 48/61/71/74 with
  sector classes, exit class, website, description and data-chronological = LAUNCH year). Posts 2016-2022 (105
  in the archived wp-sitemap) are title-only in the archive (bodies loaded by script from wp-json, never
  captured); 12 bodies exist in Common Crawl, 4 pages in Wayback. Team pages 2017-2023 parsed (names + roles).
- Getro job board talent.cherry.vc: 98 companies (38 not on the 2026 list).
- EDGAR: ERA Cherry Ventures Management GmbH (AIFM) CRD 301494 (ADV 2024-03-14, 7.B GAV: Fund III KG $534.2M,
  Fund IV KG $342.6M, Decentral I $28.9M); Form D: Fund III (US) L.P. 2019 $200.7M, Fund IV (US) L.P. 2022
  $311.0M, Cherry Decentral I 2022 $34.0M ($17.1M sold); Titanbay feeders (external); FTS "Cherry Ventures" =
  5 own Form Ds, 0 third parties. Roster sweep: 6 accessions, 1 name-match issuer (Intenseye).
- Registers: North Data (Handelsregister) 44 entities with dates, GPs, LPs (entities.json); BaFin DB empty
  (registered AIF manager, not licensed); Companies House / Bolagsverket / RCS via the same pages.
- Unicorn list re-pulled at run start (627 current / 209 former): helsing $14B (not on any Cherry surface ->
  recall probe), forto $1.2B (2021, stale), sennder, personio, celonis, trade republic.

## Layers landed
- site union 183 -> base 153 rows (142 A / 10 B / 1 C), 31 merges, 2 rejects (stealth placeholders).
- wayback parsed years 2016-2023 + 2026 (147 slugs); Common Crawl 100 company slugs + 45 people.
- roster: 34 investing staff 2012-2026 curated from the team pages + posts (ops/network dropped).
- wikipedia insource: 5 articles (Drover, Flink, Light, TourRadar in base; Turian = recall candidate).

## Gate (scratch/gate-blind-pass.json, golden.json registered 16:16 before the build at ~16:20)
- Membership: 34 rows, 0 false members; cazoo/xometry present for not_member verdicts.
- Stage: 46/46 label, 45/46 year (kitchen-stories 2014 vs press 2015). Layers: firm posts class 1; press
  class 1; 2016-2019 site label 4/6 (corroboration); archive dates 11/13; sanity dates 7/7.
- Pre-fill quarantine list: forgent float (Forgent Networks), shift unicorn name-match, Wikidata homonym
  countries (aloha PH, beo JP, curio DZ, elise FR, light JP, save FR, soba GB, sphinx PL, together GB,
  vesper BR, flink SE).

## Close (2026-09-04, late afternoon)

- Three verify problems cleared: nine slug-named Webflow pages renamed at the
  source (names-only rebuild; alicetech→alice-tech and tracespace→trace-space
  migrated in classification, ledger and golden), Flix's Seed entry cited from
  the firm's own "first institutional supporter" post, Legora marked
  `cite_pending`.
- Profile rebuilt after the builder's district strip (HQ "Berlin, Germany") and
  the crosswalk extension (0 unmapped tags).
- Momentum slice recorded on the rows (47 rows, `valuation_range_source:
  web_verified` + citation); Ben web-checked last (Series A Aug 2022, private).
- verify clean (full mode, links skipped); export 148 rows; review.html 207 KB,
  rendered on the static server, profile panel expands.
- report.md written; COLLECTION.md write-back applied (§5, §6, §11); memory saved.
- Ingest NOT run; nothing committed. Prompt count 1.
