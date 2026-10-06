# Index Ventures run log (PRO-82)

Kickoff 2026-10-01 ~14:25 UTC ("please collect Index Ventures"). One session, one run. Slug `index-ventures`.

## Usage line at kickoff (get_usage, 14:32 UTC)
- 5-hour limit 3% (resets 19:20 UTC)
- Weekly, all models: 73% (resets 2026-10-06 18:00 UTC)
- Weekly, Fable: 8%
- Extra usage: disabled

## Prompt count
1. kickoff ("please collect Index Ventures")

## Siblings in flight on this checkout at kickoff
atomico, bain-capital-ventures, founders-fund, general-catalyst (in-flight markers). The working tree carries
uncommitted edits in ~25 other books, scripts/run.py, scripts/graduation-surfaces.py and COLLECTION.md (other
sessions' work); never touched. In-flight marker for index-ventures written at kickoff.

## 2026-10-01 14:30-15:30 UTC: Phase 0
- EDGAR company search: 34 "Index Ventures ..." funds, 11 "Index Venture ... Associates" GPs, 3 Index Origin funds,
  Index SPV 1/2. entities.json: 53 entities (49 home desk, 4 external: Life VII, three Yucca co-filers).
- Adviser: Index Ventures SA, Geneva, ERA, CRD 161175 (SEC 802-75760), ADV 2026-03-31, 7.B.(1) 32 funds.
  Medicxi Ventures Management (Jersey) Ltd, ERA CRD 283504, 7.B.(2) lists Index III (3 vehicles), V (2) and Life VI
  as funds it sub-advises. scratch/parse-adv-7b.py -> sources/registers/adv-7b-funds.json
  (GAV values repeat on some funds: a parse artefact to fix before the profile uses them).
- Medicxi: launched 2016-02-01, "comprises all of the legacy portfolio companies, funds and the life sciences team
  of Index Ventures" (Medicxi's launch release). Life VII (CIK 1648676, Form D 2015) is not on Index's ADV.
- Site: Wagtail, 329 companies (listing = sitemap), 49 team cards (26 investor / 11 strategist / 12 operator).
  No year, no round word per company; the listing's "backed at Seed" filter marks 75 rows. scratch/site-scrape.py,
  sources/site/companies-wagtail.json, companies-list.json, team-cards.json; site-portfolio.py run.
- Archive: CDX enumeration (60,000 keys, capped in /startup-jobs). Five site generations (config wayback._eras_note).
  IA: 503s, then a firewall refusal -> machine-wide cooldown 60 min from ~15:05 UTC. Not our rate (2 requests).
- Common Crawl (static cluster.idx route): 29 crawls 2008-2025 read; /portfolio + /index.php 2008-2013,
  /companies 2014-2025, /team 2008-2025, /news, /news-room, /blog. scratch/cc-cluster.py, cc-fetch.py (6 workers).
- WebSearch used: 1 of 200.

## Decisions taken in Phase 0 (decisions.md)
- D3 life sciences desk: OUT, partitioned (Medicxi owns the legacy book by the firms' own statement; Benchmark
  Europe / Balderton precedent). Open ruling for Erik at close; rows preserved.

## RESUME POINT 1, 2026-10-01 ~15:20 UTC
State on disk:
- Base v1 built (618 rows; build-2.log) from: live site 329, Common Crawl archive 2008-2025 (parsed/<year>.json,
  543 distinct names, archive-facts.json with the firm's own desk / status / stage-filter / Index Team claims),
  Form D sweep (72-name roster from the firm's team pages; 312 accessions, 181 issuers), 25 fund-filing issuers.
  identity-merges.json: 24 merges + never_merge gather/gather-wholesale-inc. prepare run once (14 batches of 45).
- Verdicts recorded: life-desk (37 not_member, D3), formd-clusters (23 not_member, T4/homonyms).
  opentest-inc (absorbed into loom-inc) resurfaces at the rebuild and needs its own not_member verdict then
  (delta verdict -> a second, final rebuild).
- Form D members still to classify (judgments-formd-members.py): fleetsmith-inc (Seed 2016-03, Fushman; Apple 2020),
  optimizely-inc (Series C 2015-09 led by Index), skyport-systems-inc (Volpi; Index led the $30M Series B 2014/15; Cisco 2018),
  zesty-inc (Series A 2015-06; Square 2018), saurus-inc = Imzy (Dan McComas, Saar Gur; $8M 2016-08; shut 2017),
  pomsg-ai-inc = msg.ai / Netomi (Puneet Mehta; 2017-03), kiosk-inc (Paris WhatsApp-marketing AI; Julia Andre 2026-03,
  director of record), dahlia-labs-inc = Daydream (Julie Bornstein; merge into `daydream` at the rebuild).
- Tools: scratch/show.py (judge view), evidence-pack.py, siblings.py (344 of 618 rows shared), judge_lib.py
  (post / page / arch / narch / sib / news / gsurl lookups; citations never typed), news-bulk.py (Google News per
  listed company, running in background, resumable), news-archive.py (the firm's archived news 2002-2019).
- DISK: the machine hit 0 bytes free at ~15:12 UTC (ENOSPC). Raw captures under data/filings are now gzipped
  (readers are gz-aware), cc-index-raw.json trimmed to the namespaces used. 222 Common Crawl captures failed
  (throttling) and are FAILED in cc-manifest.json; a retry is optional.
- IA: machine-wide cooldown until ~15:36 UTC. Still to read from IA: /portfolio.html 1999-2001, /portf_sect.html,
  /cgi-local/ivw_port_detail.cgi 2002-2007 (typ=it / typ=ls), /portfolio/index/industry_id/2 (life list 2008-2013,
  resolves novocure, infection-control, oxyplus-inc, directmedica, diartis), news ids 1999-2007. These land as recall
  additions at the one scheduled rebuild.
Next: grind batches 1-14 (classification of ~560 listed members), graduation pass, recall probe (IA eras, FTS leads,
Wikipedia sweep, parametric), ONE rebuild, delta, A/B + momentum, duties, profile, verify, export, review, report,
write-back, close, commit, ingest gate, siblings.
WebSearch used: 1 of 200.

## RESUME POINT 2, 2026-10-01 ~16:05 UTC
- Grind: batches 1-5 recorded (judgments-1..5.py; 219 rows classified). Method per batch: `scratch/show.py N --from 0 --to 23`
  (judge view), `postgrep.py` / `nq.py` for wording and press checks, then judgments-N.py through gl.C() (drops keys the
  queue did not ask unless `dispute=`). Left open on purpose: rows whose only stage evidence is the site's
  "backed at Seed" mark (label pass after D8 scoring), graduation of Seed rows without a cited later round
  (graduation pass after graduation-surfaces.py), dot-product (no location on record).
- D8 score so far ("backed at Seed" vs documented entry): hits cowboy, hebbia, kong, linear, productboard, remote,
  robinhood, figma, arthurai, cradle, atlar, anrok?(not labelled), nova-credit, resistant-ai, nexos-ai, incident-io,
  kry-livi, jump, okendo?; misses auxmoney (2013 $12M round), cowboy-space (Series A), deliveroo (firm calls it Series A),
  notion (2020 growth round), revolut (Series A 2016). Recount mechanically before the label pass.
- Sibling rows that look stale against this run's cited evidence (align at ingest): sequoia apex (acquired, Tenable),
  balderton dream-games (private $5B, not acquired), coatue+lux covariant (private; acqui-hire), yc humanloop (defunct),
  battery+nea expel ($1B+ 2021), sequoia bird (acquired out of Ch.11), headline peanut?, khosla catch?
- Identity merge to add before the rebuild: lithic <- privacy-com; daydream <- dahlia-labs-inc.
- IA: second firewall refusal at ~15:38 UTC, machine-wide cooldown ~2h (until ~17:40). scratch/ia-pass.py is queued
  (pre-2008 portfolio pages + life lists); two early pages are already cached (1999 /portfolio.html, 2001 /portf_sect.html).
- Google News lookups done for all listed names (news-bulk*.json, 3 workers). WebSearch used: 1 of 200.

## RESUME POINT 3, 2026-10-06 ~18:20 UTC (the session was interrupted on 2026-10-01 ~17:30 UTC and resumed five days later)
- Grind complete: batches 1-14 recorded (judgments-1..14.py), 536 rows classified. Ledger: 616 verdicts.
- Label pass done (judgments-label.py; decisions.md D8 scored: 'backed at Seed' 31/36 -> first_party medium;
  'Seed stage' alone -> first_party low; Seed+Early -> refused). config.site_api.entry_stage_fields = [stage_site].
- Open rows settled by web search (judgments-open.py): the-garden, quixotic, dot-product; v-watch not_member (D3).
- identity-merges.json: 37 merges (13 added from the grind: lithic, daydream, ubermedia, beryl, vetted, mirage, kong,
  glasses-direct, photobox, raisin, trouva, drivy, parallel). They apply at the ONE rebuild.
- Perspectives archive re-read: 586 of 586 posts on disk (the first scrape had 12 failures; scraper is gz-aware now).
- Graduation: scripts/graduation-surfaces.py ran 2026-10-01 for 86 Seed rows (0 lookups failed); prepare re-run
  (queue: 100 rows in 3 batches; the grind's queue is kept in scratch/queue-grind/). scratch/gshow.py and gshow2.py
  are the judge views; scratch/formd-lookup.py gives the `formd:` line of an absence test.
  investor/investor.json is a two-key STUB so graduation-surfaces.py can read the firm's name; the profile build replaces it.
- WebSearch used: 9 of 200.
Next: graduation judgments, IA pre-2008 pass, recall probe, ONE rebuild, delta, A/B + momentum, duties, profile,
verify, export, review, report, write-back, close, commit, ingest gate, siblings.

## RESUME POINT 4, 2026-10-06 ~19:45 UTC (model switched to Opus 5.5 at the second prompt, "continue"; prompt count 2)
- Done since point 3 (commits 6abe0079, 32ad6e41, 399cfea2, 118b4af8): graduation pass (judgments-grad.py), IA
  1999-2002 layer (ia-listings.py, 12 rows), recall probe (22 additions in the ledger, R3), A/B pass on the visible
  slice (judgments-ab.py), momentum slice, public caps of 2026-10-06, cross-rulings (42 distinct, 4 same), profile
  dry build (ADV 7.B: 32 funds, $25.32B; 49 people; hq by the site-list rule).
- People: 26 "Partner" (investor tab) and 23 without a position (strategist + operations tabs). That is the shared
  build rule, the same shape as Accel, a16z and Ribbit; the site publishes no titles.
- Instinct: the $1B Series C at $10B CLOSED on 2026-09-28 (PYMNTS, the company's release). The earlier note
  "talks at $10B are not a mark" is superseded: the row takes $10B, as Kleiner Perkins' row does.
- Ten more source pages read for the recall additions (web-finds.json: nauto, sourceclear, snapguide, sphere-2017,
  gojimo, bonify, less, familiar, dazz-2021, yup-edsurge). Dazz and Italic entry round not established: undetermined.
- Duty 7: seeded sample of 28 members (scratch/duty7-sample.json, seed 82), judged blind by a subagent that may not
  read the classification; its answers land in documentation/duty7-blind.json.
- scratch/regime-report.py written (D9); run it again after the rebuild.
- IA: machine-wide cooldown until ~19:50 UTC; scratch/ia-pass2.py (26 targets, 2002-2007 lists) waits on it in the
  background. If it is refused again, the 2003-2007 pages stay debt and the rebuild goes ahead without them.
- WebSearch used: about 52 of 200 (plus the subagent's, capped at 30).
Next: ia-pass2 -> ia-listings -> ONE rebuild -> read the rename list -> prepare -> judge the delta (22 recall rows,
12 IA rows, merged rows) -> names.published -> profile rebuild -> regime report -> verify -> export -> review ->
report -> write-back -> close -> commit -> ingest gate -> siblings -> Linear -> memory -> closing message.

## RESUME POINT 5, 2026-10-06 ~20:05 UTC (prompt count 2)
- IA refused a third time (3 pages fetched, 120 min machine-wide cooldown): the 2003-2007 pages are debt.
- Rebuilds: 618 -> 571 (the one planned) -> 564 (the delta's exclusions) -> 560 (name variants of excluded
  life-desk rows; the re-key trap: both variants now hold a verdict in the ledger).
- Delta judged (judgments-delta.py, 36 rows). R2 revised: the 1999-2002 "Prior investments" group is OUT (9 rows).
- Blind 5% check: documentation/duty7-blind.json, 19 of 177 cells differ, 6 rows corrected
  (queue/duty7-adjudication.out.jsonl). The subagent sent the personal Gmail to sec.gov in a User-Agent, 3 requests.
- Profile rebuilt with a focus crosswalk (config.profile). names.published: 21 overrides.
- Plain verify: CLEAN at 560 rows, 708 shared rows agree, 0 accepted. Export + review rendered and checked.
- Sibling alignment (scratch/align/): pairs.json 20 books / 35 rows, plus one repair (Lightspeed's Avarra, whose
  censoring window ended 2026-10-03 and which announced a Series A on 2026-10-06). Local phase done for all 20:
  their classification.json / base.csv / review.html are changed and UNCOMMITTED until `align.py ingest` runs.
  If this session dies here: either run `python3 scratch/align/align.py ingest` after the Index ingest, or restore
  the 20 books with `git checkout -- <book>/companies/{classification.json,base.csv,review.html}`.
Next: close -> closing commit -> icon upload -> ingest-investor -> ingest-companies --dry-run -> write -> readback ->
align.py ingest -> report section 15 -> commit -> Linear -> memory -> closing message.

## CLOSED, 2026-10-06 ~20:45 UTC (prompt count 2)
- Index Ventures ingested: icon, investor row, 560 companies; readback "csv 560, live 560, missing 0, extra 0,
  differing cells 0". Commits 633f0015 (closing) and 5cfc1fd6 (post-ingest).
- Siblings: 36 rows in 20 books aligned and re-ingested, every readback exact (scratch/align/results.txt).
  Every book not in flight verifies clean afterwards.
- report.md is final (section 15 = ingest). Linear PRO-82 Done. Memory note index-ventures-run-pro82.
- Open for Erik: D3 (life sciences desk out), R2 (pre-fund "Prior investments" out), Arista (in on the listing).
- Debt: Internet Archive 2003-2007 pages (scratch/ia-pass2.py is queued), home registers for the 20 European
  rows of unknown status, the 2016-2019 seed recall gap, 18 cite_pending rows.
