# Balderton run log (PRO-106)

Kickoff 2026-09-26 ~22:30 UTC. One session, one run.

## Usage line at kickoff (get_usage)
- 5-hour limit 41% (resets 00:09 UTC 2026-09-27)
- Weekly, all models: 33%
- Weekly, Fable: 5%
- Extra usage: 18% (EUR 9.29 of 50)

## Siblings in flight on this checkout
- atomico (in-flight since 16:47), point-nine (marker since 18:31; PRO-101 reported closed)
- IA cooldown at kickoff: 12,470 s remaining (machine-wide block earned earlier today)

## Prompt count
1. kickoff ("please collect Balderton")

## 2026-09-26 23:1x UTC: in-flight marker written early, on a peer's correction
The Atomico collection session reported that its `verify` compared against this book's unclassified rows (9 None/None pairs: Light, Omio, Peakon, TestGorilla, The Exploration Company, Truecaller and others), because the first base build wrote `base.csv` before `prepare` had written the marker. Marker written the same way `in_flight_mark` does. Credit: Atomico session. Write-back candidate (COLLECTION.md s12): the first base build of a new investor should write the marker, not only `prepare`.

## Rule 10 notes from siblings (for the alignment, not yet applied)
- Atomico reads The Exploration Company at 1b_plus, $2B (FT via The Next Web, Jul 2026, low confidence; the $450M Series C closed Sep 2026 with no price).
- Atomico reads Truecaller public, below_1b ($0.69B cap, 2026-09-25).

## 2026-09-26 23:25 UTC: state for a resume
- Base v1: 271 rows (205 live cards, 52 Benchmark-era rows, Form D / EDGAR rows), `prepare` done: 271 rows queued in 7 batches.
- Judging plan: pass 1 per batch (membership, status, country, city, stage, band, focus), then `graduation-surfaces.py --all-seed`, then the graduation pass on Seed rows, then recall probe, ONE rebuild (archive eras + recall additions), delta grind, A/B pass, profile, verify, export, review, report, write-back, close.
- Pending layers: balderton.com archive eras (IA cooldown ends ~02:05 UTC 2026-09-27; CC index flapping, scratch/cc-index.py retries), Wikipedia candidates (18), recall leads (scratch/recall-leads.md).
- Usage at 23:23 UTC: 5-hour 65%, weekly 39%, Fable 14%.

## 2026-09-26: citation audit (a defect of mine, caught and fixed before any milestone)
The compact batch view truncated the firm's post URLs at 48-70 characters and I completed 17 of them by hand; 17 of the completions were not real URLs. Two TechCrunch links (Coro, Photoroom) were typed from memory and were wrong too. All 19 were replaced with the real URLs (matched by prefix against sources/site/news.json, or through TechCrunch's own API) in batch-citation-fix.out.jsonl. Rule for the rest of the run: a citation is copied from a tool result or a file on disk, never completed or typed from memory; judgments read post URLs from evidence-pack.json by key.

## RESUME POINT, 2026-09-27 00:05 UTC (written before a context compaction)

After a compaction: re-read `data/collection/COLLECTION.md` start to finish, then this section, then
`python3 scripts/run.py status --investor balderton-capital` (note: `prepare` takes the slug positionally,
`record` / `status` / `verify` take `--investor`). Checkpoint commit 7c6b735 (local main, not pushed).

### Done
- Phase 0: decisions.md D1-D12, R1 (Codemasters kept on its minority entry), R2 (Alphyra, NASN out as control
  positions). Kickoff and milestone comments posted on PRO-106 (issue is In Progress).
- Layers on disk: live list 205 cards (`sources/site/companies-facetwp.json`), team 48 cards, news 552 posts
  (`sources/site/news.json`), benchmark.com Europe rows 2001-2009 copied from PRO-88 (`sources/wayback/parsed/`),
  curated roster (43 people), EDGAR entities 19, Form D sweep, issuer filings, full-text sweep, Wikipedia sweep,
  Form ADV CRD 160323 parsed (`sources/registers/adv-160323.json`: 16 funds, $8,511,214,328), Companies House
  LLP register + officer graph (`sources/registers/companies-house/`).
- Base v1 271 rows; grind pass 1, A/B pass, momentum slice (scratch/momentum.json) and graduation pass all recorded
  (judgments-1..8, -ab, -grad, citation fix, rule 6 fix). `verify --in-flight`: only `wonga` missing (recall),
  absorbed duplicates awaiting the rebuild, and the empty profile.
- `companies/identity-merges.json` (9 merges) and `companies/cross-rulings.json` (28 distinct, 10 accepted) written.

### To do, in order
1. **Archive eras for balderton.com** once the Internet Archive cooldown ends (about 02:05 UTC 2026-09-27; check
   `shared_throttle.cooldown_remaining('ia')`). Common Crawl showed the URL history: 2013-2017 `/portfolio`
   (listing) with `/team/<slug>`; 2021-2023 `/companies` listing and `/investments/<slug>` per-company pages;
   2024+ the current site. 2007-2012 unknown. Enumerate CDX, write the eras into config.json, run
   `python3 scripts/wayback-pull.py balderton-capital` and `partner-roster.py` (extend the curated roster, never
   shorten a register-dated window). The Common Crawl index answered only intermittently (scratch/cc-index.py
   retries; every crawl recorded FAILED, not empty).
2. **Recall probe** (scratch/recall-leads.md). Filing-grade additions already evidenced:
   - Touch Local / Scoot: Web.com 10-Q and S-3 2014, Balderton Capital III a seller (Evans director 2006-08).
   - Lemon, Inc. (formerly Bling Nation): LifeLock 8-K/A 2014-02-21, Balderton held Series B preferred, repurchased Feb 2012 -> Growth entry.
   - Wonga: Wikipedia + Liautaud director 2009-2018 (administration Aug 2018, TechCrunch) -> defunct.
   - Leads to check against the archive listings: Achica (ACH Realisations), Lifecake, Tapdaq, Tilt, Banjo, Archify,
     Audium Semiconductor, Clinical Solutions, Cognism, Retro Labs, Hook, Pict Ventures, Entomics, Cherryz, KupiVIP.
   Additions go in as site/file_list rows or recall entries with citations; every rejected candidate gets a not_member verdict.
3. **The one rebuild** (`build-company-base.py`), then `prepare` for the delta, judge the delta, second rebuild only
   if the delta rules a row not_member.
4. **Standing duties** (s8): blind 5% re-judgment, weak CIK join audit (95 rows resolved a CIK in layer A; check any
   float or status riding a weak join), unicorn list re-intersection.
5. **Profile** (step 7). Facts gathered:
   - thesis (title tag, the homepage has no h1): "Europe's leading venture firm focused exclusively on backing
     European-founded tech companies" (read 2026-09-26; meta description is the competing line).
   - founding 2000 as Benchmark Capital Europe (VentureBeat 2007-06-07; the firm's 2014 post); independence June 2007;
     founders Barry Maloney, George Coelho, Mark Evans (LLP founding members 2004-02-12; desk pages 2000).
   - funds (sizes from the firm's own posts): IX $615M and Growth II $685M (2024-08-12); VIII $600M (2021-11-17);
     Growth I $680M (2021-06-10); VII $400M (2019-11-12); Liquidity I $145M (2018-10-03); VI $375M (2017-11-27);
     V $305M (2014-04-01, "fifth European fund", total $2.2B); III $500M (Dec 2006, VentureBeat); IV (2009), II (2004),
     I (2000) sizes not yet sourced.
   - AUM: Form ADV 7.B sum $8,511,214,328 (ERA, no Item 5.F); the site's about page says "$5.7bn" raised.
   - HQ: The Stables, 28 Britannia Street, London (ADV Item 1.F; site footer agrees). Run `firm-offices.py`.
   - notable candidates: Revolut, Wayve, Lovable, Depop, Darktrace (check slugs are members).
   - icon: run `fetch-investor-icon.ts --discover https://www.balderton.com` and `--dry-run`; upload only with the ingest.
   - the kickoff stub `investor/investor.json` must be replaced by the real profile.
6. Plain `verify`, `export`, `review` (serve through the review-surface launch entry, port 8931), `report.md`
   (usage line: kickoff 5h 41% / weekly 33% / Fable 5%; at 00:05 UTC 5h 86% / weekly 44% / Fable 25%), playbook
   write-back proposals, `run.py close`, closing commit with pathspec, closing message with the ingest request.
   Ingest only after Erik's explicit approval.

### Open rulings to raise with Erik at close
D2 (Benchmark Europe book is Balderton's), R1 (Codemasters), R2 (Alphyra, NASN control positions), D6 (Odyssey out,
Rahko in), the four unidentified desk-era rows (Activiti, Cas Services, i-Cue, Visual Media), Feast Kitchen = Simple Feast
merge (medium confidence), The Exploration Company at $2B (low confidence), status calls at medium confidence
(Hubilo, Tempow, Lyst confirmed), Premialab HQ moved to the UAE.

### Write-back candidates for COLLECTION.md (propose at close, do not edit the playbook mid-wave)
- The first base build should write the in-flight marker, not only `prepare` (Atomico's verify compared against
  this book's unclassified rows).
- A successor firm inherits the predecessor desk's archived rows from the sibling run's parsed captures, with
  `capture_url` per row; mixed desk pages are never configured as eras.
- FacetWP sites: the refresh endpoint refuses scripted calls; `?_paged=N` renders server-side.
- A judge never completes a truncated URL: read citations from disk by key (19 wrong citations this run).
- The UK LLP member register gives exact partner tenure; `graduation-surfaces.py` needs `investor/investor.json`
  to exist, which a fresh book does not have (FIRM_TERMS fallback).
- The momentum slice paid: four events after the judge's knowledge on one book.

### Siblings and etiquette
Atomico, Point Nine, Coatue and Insight Partners sessions are active on this checkout. Insight added
`"exclusion": "control_position"` to the builder (6fdf0fc); used on Alphyra and NASN. Never touch their directories.
Prompt count so far: 1.

### 2026-09-27 00:10 UTC: added after the resume point
- Recall additions written to the ledger (`recall_additions`): Wonga, Touch Local, Lemon. They land at the rebuild.
- A background job waits for the Internet Archive cooldown (task bmac9kihp); when it reports, start at to-do item 1.
- Early fund sizes, sourced by web search 2026-09-27 (URLs from the search results, to be cited in `investor/sources.json`):
  - Benchmark Europe I: $750M at the close of May 2000 (Light Reading, https://www.lightreading.com/business-management/benchmark-closes-750m-european-fund), reduced to $500M in 2002.
  - Benchmark Europe II: $375M, Jul 2004 (Buyouts Insider, https://www.buyoutsinsider.com/benchmarks-2nd-euro-fund-oversubscribed/).
  - Benchmark Europe III: EUR 430M, Nov 2006 (TechCrunch, https://techcrunch.com/2006/11/16/benchmark-capital-europe-raises-e430-million-2/); about $550M.
  - Balderton IV: GBP 285M, about $430M, 2009 (TechCrunch, https://techcrunch.com/?p=2814); a vendor page says $485M (not used, Rule A).
  - Non-USD sizes convert with `scripts/fx-convert.py` at the announcement date.
