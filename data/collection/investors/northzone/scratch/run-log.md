# Northzone run log (PRO-105)

Kickoff 2026-09-29 ~17:45 UTC. One session, one run. Slug `northzone`.

## Usage line at kickoff (get_usage, 17:47 UTC)
- 5-hour limit 74% (resets 19:00 UTC)
- Weekly, all models: 71% (reset 18:00 UTC, twelve minutes after kickoff)
- Weekly, Fable: 6%
- Extra usage: disabled (24% spent, EUR 12.14 of 50)

## Prompt count
1. kickoff ("please collect Northzone"), followed by "continue" mid-turn (same kickoff)

## Siblings in flight on this checkout at kickoff
atomico, bain-capital-ventures, founders-fund, general-catalyst, tiger-global-management (in-flight markers).
The working tree also carries uncommitted edits across ~25 other books (a sibling's sweep); never touched.
In-flight marker for northzone written at kickoff (Balderton lesson: before the first base build).

## 2026-09-29 18:00-18:40 UTC: Phase 0
- Site: Webflow, 142 companies (list pages ?d42057d9_page=1..2 + 142 company pages), 34 team cards,
  689 insights posts (scrape running). scratch/site-scrape.py, scratch/insights-scrape.py.
  Raw pages in data/filings/northzone/ (gitignored).
- Archive: CDX enumeration of northzone.com (20,000 URL keys, capped inside wp-json/oembed; eras below).
  Six generations: 2001-2005 W5 framed site (/portfolio, .W5Doc per company, GUID logos, 17 companies in 2003),
  2005-2008 ASP (/web/folder.asp, Hugin press cws.huginonline.com/N/131881), 2009-2011 /portfolio/active-investments
  + /exits (?investment=N), 2012-2014 /investments + /investments/<id>, 2015-2019 WordPress /investments/<slug>/,
  2020-2025 WordPress /portfolio/<slug>/, 2026 Webflow.
- IA: 503s then a machine-wide firewall cooldown (58 min from ~18:05 UTC). Not our rate: a degraded spell.
- EDGAR: 6 fund filers (entities.json), no ownership filings; Form D sweep 96 accessions / 62 issuers on a
  PROVISIONAL roster (58 names from archived /team/ slugs + the live Investment group); FTS 14 third-party
  registrants; Wikipedia sweep needs base.json (runs after the first build).
- ADV: three Jersey ERAs, 7.B $1,651,159,907 (scratch/parse-adv-7b.py -> sources/registers/adv-7b-funds.json).
- Registers: Companies House OC412539 (LLP members dated), 07880610; Brønnøysund 895407992, Northzone VII L.P. NUF 913585763.
- decisions.md D1-D10 written; kickoff comment on PRO-105; issue In Progress.
- Paul Murphy verified: Northzone Feb 2018 - Feb 2021, Lightspeed from 2021 (TechCrunch 2021-02-26). WebSearch used: 1.

## To do next
1. When IA answers: archive eras (scratch/archive-listings.py) -> sources/wayback/parsed/<year>.json with capture_url;
   partner-roster.py (then curate: titles from archived team pages, register dates win).
2. Insights: company mentions and round words -> evidence pack; recall candidates.
3. First base build, Wikipedia sweep, prepare, grind.

## 2026-09-29 18:45-18:55 UTC: while the IA cooldown runs
- Form D clusters judged by person (sources/edgar/formd-sweep.json): Paul Murphy 50 hits (Del Taco, Sentinel funds,
  gold miners, UCSD surgery center: homonyms; Playdots 2014 = founder-era Executive Officer; Kumospace 2021,
  Good Game 2022, Believer 2023 = Lightspeed era), FOSSA 2020q1 Director = in tenure but the name is common and
  the Series B (Oct 2020) was Bain Capital Ventures / Canvas / Costanoa with no Northzone: a lead, not affirmative.
  Pauline Murphy 30 = prefix match, all out. Real: Sticky Ad, SellersFunding (Zink); Hero Journey Club,
  Berry Street (Xiao); Microverse, Personio (Kotting); Blitzy (Malhi); Realize, Inc. (Molly Alter, 2024q1 +
  2026q1, NY): director-of-record candidate, identity to resolve. Otterling N22 Africa Fund = a fund (T5).
  Lea Bajc / Amit Sanghvi / Aaron Liu hits = homonyms to confirm against titles.
- Dated WordPress posts: 952 (scratch/wp-posts-index.json, from the CDX enumeration); insights slugs are the
  WP slugs, so date_wp joins by slug. Fund ladder from post slugs: VII EUR 150M (2013-12-05) -> $325M
  (2014-12-16), VIII "biggest fund to date" (2016-09-05), IX "$500M" (2019-11-18).
- Overlap: 70 of 142 live companies are in other books (accel 12, creandum 9, YC 8, GC 7, cherry 7, balderton 6).
  Homonym traps visible: Jasper (Northzone's = Jasper Design Automation, Cadence 2014), Dots, Stream, Sticky, Axon.
- Registers for status: Finland avoindata.prh.fi v3 API works (Zervant -> Ageras Oy -> Shine Europe Oy);
  Denmark cvrapi.dk works (owners listed); allabolag.se 403 to curl; brreg search covers live entities only.
- Norway shareholder register: full extract only by request form + emailed one-week link (skatteetaten.no/en/deling/
  aksjonarregisteret). Not run: needs Erik (form with personal data, his inbox). Proposed at close.

## 2026-09-29 ~20:00 UTC: playbook change, ingest now the run's own last step
Peer message from the Ingestion Alignment session (GV run, PRO-75): COLLECTION.md §9 changed. Checked at source,
not taken from the message: commit 449e2085 "COLLECTION.md: the run ingests its own work behind a mechanical gate
(Erik, 2026-09-29)" replaces the 2026-08-31 approval rule; PRO-105's description now says target one prompt and
"ingest through the §9 gate with the stale sibling rows aligned". So the close is: verify clean -> run.py close ->
closing commit -> icon, ingest-investor, ingest-companies --dry-run -> removal check (every removal explained) ->
write -> readback (20vc/scratch/align/readback.ts) 0 differing cells -> stale siblings aligned + re-ingested one
book at a time (skip any with in-flight.json or uncommitted company files; commit only their three company files)
-> stop and report on any stop condition. Re-read §9 in full before closing. Credit: Ingestion Alignment session.

## RESUME POINT 1, 2026-09-29 ~20:15 UTC (written before any compaction)
After a compaction: re-read data/collection/COLLECTION.md (NEW §9: the run ingests itself behind the gate), then
this file, then `python3 scripts/run.py status --investor northzone`. Nothing committed yet.
Done:
- Phase 0 (decisions D1-D10, kickoff comment, issue In Progress); config.json; in-flight marker.
- Site layer: sources/site/companies-list.json (142, file_list) -> companies.json; team-cards.json -> team.json (34);
  insights.json (689, body + date_wp + article_url). scratch/site-scrape.py, insights-scrape.py.
- EDGAR: entities.json (6 funds), formd-sweep (96/62), fts-hits (14 third-party), adv-7b-funds.json ($1.651B).
- Roster: sources/wayback/partner-roster.json = provisional CDX first-capture roster + scratch/roster-curate.py
  (15 people with dated register/filing/post facts). Re-run roster-curate.py after any partner-roster.py run.
- Base v1 built 2026-09-29 ~20:05 UTC: 176 rows (142 site, 34 Form D name-match rows, mostly homonyms).
  identity-merges.json: playdots-inc -> dots, sellersfunding-corp -> sellersfi (apply at the rebuild).
- config.verify.not_members traps written before any verdict.
- scratch/evidence-pack.json + siblings.json built (re-run both after the rebuild).
Running at this point: prepare (scratch/prepare-1.log), cc-fetch of CC captures (scratch/cc-fetch.log),
wikipedia-insource (scratch/wikipedia-insource.log), IA archive-probe (waits out the IA cooldown, ~21:03 UTC).
Next: grind base v1 (membership + classification) from scratch/queue; archive eras from CC (2013-2025) and IA
(2001-2012) into sources/wayback/parsed/<year>.json; recall probe; ONE rebuild; delta grind; duties; A/B;
profile; verify; export; review; report; close; commit; ingest gate; siblings.
Judge helpers: scratch/judge_lib.py (WHO agent-judge-pro105).
Web searches used so far: 3 of 200.

## RESUME POINT 2, 2026-09-29 ~20:45 UTC
After a compaction: re-read COLLECTION.md (NEW §9 gate), this file, `python3 scripts/run.py status --investor northzone`.
Done since resume point 1:
- Base v1 (176) fully judged: judgments-1..4.py + judgments-patch1.py (batch-001..004, batch-patch1 .out.jsonl).
  32 name-match verdicts (31 not_member; Realize member medium, director-of-record, flagged boundary).
- companies/cross-rulings.json: 19 distinct (homonyms), 4 accepted (stale siblings to align at ingest:
  battery-ventures:blitzy, creandum:stockeld-dreamery, first-round-capital:thirty-madison, accel:wallapop).
- verify --in-flight: only the 2 absorbed slugs (playdots-inc, sellersfunding-corp) until the rebuild.
- Tools: scratch/show.py (judge view), news-bulk.py (+ news-bulk.json), read-articles.py, site-city.py,
  nordic_status.py, judge_lib.py (post/art/wp/news/sib/page lookups; citations never typed).
- cdx-enum.json moved to data/filings/northzone/ (regenerable).
- Web searches used: 5 of 200.
Next, in order:
1. Archive eras: CC captures fetched (scratch/cc-fetch.log; data/filings/commoncrawl/northzone; manifest
   sources/wayback/cc-manifest.json) for 2013-2025 -> write scratch/archive-listings.py era parsers -> parsed/<year>.json.
   IA (cooldown until ~21:03 UTC; the probe job scratch/archive-probe.py waits) for 2001-2012 eras + Hugin press.
2. Roster: partner-roster.py when IA answers, then scratch/roster-curate.py.
3. Recall probe: archive names not in base, wp-posts titles (EyeTrackShop->Sticky, Online Backup Company, P1,
   Ocapo, BraveNewTalent, Activate, DoubleTwist, TestFreaks, T-VIPS, Settle/mCash, Arfa->Chord, 3Box->Recall Labs,
   Noquo->Stockeld, Trolltech->Qt, FreightHub->Forto, MarketInvoice->Kriya, Infogrid->Noda, iZettle->Zettle, Wagestream->Stream).
   Merges into identity-merges.json for renames.
4. ONE rebuild, prepare delta, judge delta, graduation-surfaces.py + graduation pass (26 open Seed rows now).
5. Duties, A/B + momentum slice, profile, verify, export, review, report, write-back, close, commit, ingest gate.
