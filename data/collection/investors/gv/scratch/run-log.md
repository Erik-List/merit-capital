# GV run log (PRO-75)

Kickoff 2026-09-29 00:31 UTC (2026-09-28 20:31 EDT on this machine), prompt 1 ("please collect GV").
Usage line: not readable from this session at kickoff (no usage tool call); record at close if available.

## RESUME HERE (run closed 2026-09-29; only the ingest remains, on Erik's approval)
- Re-read COLLECTION.md, then `python3 scripts/run.py status --investor gv`, then this file.
- Boundary: decisions.md D1 (no ADV; GV vehicles IN; CapitalG, Gradient, Google/Alphabet corporate OUT), D4 (Waymo,
  Isomorphic Labs IN as minority financings), Delta 1 (profile contract for a manager with no ADV, open).
- IA machine-wide cooldown at the 8 h ceiling until ~06:38 UTC 2026-09-29 (`~/Library/Caches/merit-capital/locks/ia.cooldown`).
  Do NOT fire an IA job the instant it ends (BCV re-tripped that way). The archive layer runs on Common Crawl.

## STATE (UTC; times from file mtimes)
- 00:31 kickoff. 00:41 Sanity pull (company 646, aiCompany 112, teamMember 109, newsArticle 153, caseStudy 19)
  -> shape-site.py -> company-list.json (648 rows) -> site-portfolio.py -> companies.json, team.json.
- 00:45 edgar-fts-sweep.py (done 00:51: 12 phrases, 257 registrants, 204 third-party).
- 00:42-01:03 cc-cluster.py: 128 crawls x 2 keys, 10,424 captures; cc-fetch.py (digest-deduped) -> 1,760 bodies.
  cc-parse.py -> sources/wayback/parsed/2012..2026 (markups A-E; E = Nuxt payloads via js/nuxt2-companies.js
  and a __NUXT_DATA__ reviver), 236 captures, none empty. cc-roster.py + build-roster.py -> 68 people.
- 01:04 run.py collect: Form D sweep 500 filings / 255 issuers; entities.json 31 (23 gv, 8 external);
  edgar-companies 22. 01:05-01:12 identity merges, base 862, wikipedia sweep (227 articles, 34 candidates).
- 01:14 prepare: 862 queued in 20 batches. 01:19 judgments-members-1 (96 verdicts) + members-2 (OSE out):
  770 member / 92 not_member. 01:23 pilot (ahana). news-sweep.py running (Google News is the shared bottleneck).
- 01:25-01:35 judges j1-j10 launched on batches 1-10; recall triage agent on 165 candidates.
- 01:35 DEFECT (fixed for the rebuild): the builder's word-prefix variant merge folded five pairs of different
  companies (Secret/Secret Escapes, Astrid/Astrid Health, Bloom/Bloom Institute of Technology, Spruce
  Health/Spruce Finance, and "Sense" = sense.com 2016-19 vs sensehq.com 2020+), because cc-parse gives each
  company its first capture's snapshot_ts per year, so the builder's co-listed test rarely fires. Fix:
  never_merge pairs (6) + cc-parse SAME_NAME_SPLIT; parsed/ rewritten. Re-check after the grind: secret-escapes,
  astrid, bloom-institute-of-technology, spruce-finance, sense (their evidence packs mix two companies).
- 01:40 profile prep: write-profile.py (history, aum null-and-flag, funds = 9 vehicles, icon path);
  firm-offices.py -> San Francisco, CA (site statement). Icon dry run clean. Team published = 34 investing.
  documentation/collection-md-proposal.md drafted (5 items).
- 01:50 recall probe done. Press sweep (recall/gv-leads-sweep.py: 600 headlines, 202 unmatched, nearly all "GV
  Wire"/GV Prakash/GV cinemas noise) -> Roqbot. Triage agent (recall/triage.json, 165 candidates: 111 noise, 33
  aliases, 16 not GV incl. 5 sale-consideration acquirers, 5 candidate members) -> Fulcrum, Lyell, Singular
  Genomics, Fractyl (+ Secret, already restored by the never_merge split). recall/additions.json = 5 additions,
  to be written into the ledger's recall_additions at the rebuild (under the record lock).
  Triage also found: Crittercism = Apteligent, BridgeBio Oncology = BBOT (merges added, 48 groups); Bowery =
  bowery.io 2014-15 + Bowery Farming 2017+ (SAME_NAME_SPLIT); Google Ventures 2012, L.P. (D1, funds);
  Revolution Medicines = sale consideration for EQRx (trap + verdict, judgments-members-3.py; D11).
- 01:25-13:50 grind: judges j1-j17 recorded all 20 batches (reports condensed in judge-reports.md); 17 verdicts
  beyond the membership passes (seedling, curie-bio, revolution-medicines). Disk filled once (~22:55 EDT); cleared.
- 14:05 merges from the reports: redpanda<-vectorized, omni<-omni-analytics, mylaurel<-ready, backplane<-place,
  hired<-developer-auction, djz<-crossfader, beamable<-disruptor-beam (same CIK). Sense split REMOVED from cc-parse
  (one CMS entry re-linked sense.com -> sensehq.com in May 2019; j12). never_merge + bowery/bowery-bowery-io,
  basis/basis-basis-io (the name-variant rule had folded the bracketed splits back).
- 14:10 fixes-1 (upstart, vera caps; cite_pending on dialpad, simply, turo, typeface, viz-ai; doppler stage_uncited).
  Recall additions (5) written to the ledger under the record lock. queue.json copied to queue-pre-rebuild.json.
- 14:13-14:18 REBUILDS 1-3 (base 862 -> 761). Rebuild 1 re-key DEFECT: curie-bio's not_member verdict moved onto the
  new spruce-health row (shared site_url = the listing page) and place's member verdict onto
  oxford-sciences-innovation (shared index-capture link); both moved back by hand. OSI resurfaced after OSE's
  exclusion -> own verdict (members-4). Form D legal-name pairs flip names between builds (culture-amp, expanse/
  qadium, vise) -> each slug has its own verdict (members-5). Rebuild 3 clean: 761 rows, 10 new rows unjudged.
- 14:20 rule 10: companies/cross-rulings.json (rule10-rulings.py over rule10-pairs.json): 60 distinct, 68 accepted
  (GV fresher; siblings to align at ingest with Erik's approval). verify --in-flight: 0 disagree.
- 14:22 graduation-surfaces.py gv (81 rows, 0 failed); prepare delta: 88 items in 2 batches (77 graduation-only,
  11 rows with more needs incl. the 10 new rows). siblings.json + evidence-pack.json rebuilt for 761 rows.
- 14:30 delta judges d1-d5 launched (DELTA-BRIEF.md, gradview.py, judge_lib.GNEWS); the app quit twice; nothing of
  theirs recorded; resumed from their transcripts at 15:36. Meanwhile fixes-2 (apteligent takes Crittercism's 2011
  seed + graduated; mylaurel takes Ready's Series C; beamable, nchroma-bio notes), fixes-3 (wrong-join
  valuation_source/asof cleared on 15 rows; lattice status stated), fixes-4 (airware, cacheflow status stated),
  fixes-5 (focus on spinlaunch, spruce-finance). Stray stage_disputes_band removed from apteligent by hand.
- 15:48 usage (get_usage): 5-hour 34%, weekly all models 61%, weekly Fable 6% (shared with the other sessions;
  the ICONIQ session read weekly 23% at 00:32 UTC, one minute after this run's kickoff). Context 57% of 1M.
- 15:47 PRO-75 milestone comment (base landed, grind complete). A/B: ab-1 (Vir $1.75B, Prime $519M), ab-2
  (Intercom/Fin acquired 2026-09-14; checkr, homelight, scandit, headway, vercel pinned), ab-3 (flags), ab-4
  (inertia, treeline-biosciences: no published valuation, needs_web_value cleared). Duty 6 clean. names.published
  (11) in config.json. decisions.md: D5 roster note, R1-R5. collection-md-proposal.md: items 7-10.
- 16:00-16:25 delta judges done (d1-d5, reports in judge-reports.md); notes repaired (repair-notes.py, 41 rows);
  fixes-6..10 (cities, corduro era band, rockbot<-roqbot answers, voltron note, brandless acquired); merges added
  dailycred<-shopobot, voltron-data<-ursa-computing, rockbot<-roqbot. REBUILD 4 (final): 758 rows, no rename;
  prepare: 0 queued. fixes-9 (is_public cleared on 11 wrong joins). Plain verify CLEAN. Profile built
  (derive-profile.py now merges like run.py). export + review rendered and checked on 8931.
- 16:25 blind 5% (38 rows): 202/228 cells agree; adjudicated (judgments-blind-adjudication.py, 21 rows unstable,
  11 adopted). Duty 9 class sweep launched: 199 rows (undetermined stage or unknown status), judges s1-s4
  (SWEEP-BRIEF.md). City check against EDGAR headers: headers are NOT an HQ source (Ethos, Strella reverted).
- report.md drafted (documentation/report.md); placeholders {{DUTY7}} and {{USAGE_CLOSE}} to fill.
- 17:00-17:25 sweep s1-s4 done (61 settlements, 5 statuses, 9 more renamed pairs); fixes-14..17 (framed defunct,
  AVOS stage to MixBit, Jetify/Crews by Core take the absorbed seeds, Makani/BufferBox notes, Collaborate city).
  REBUILD 5 (final): 749 rows, no rename; prepare 0 queued; plain verify CLEAN; profile rebuilt; export + review.
  report.md final (S2A 103/187 = 55.1%). Usage 17:23 UTC: weekly 70%, five-hour 68%. CLOSED (run.py close).
- WebSearch used by me: 1 (Ahana); triage agent 8.

## NEXT
1. Delta judges d1-d5 (DELTA-BRIEF.md): d1 = the 11 rows with more than graduation; d2-d5 = graduation rows.
2. Post-delta: canonical fixes for merged rows (mylaurel stage from Ready's Series C, beamable note from Disruptor
   Beam 2013 listing, redpanda/omni/backplane/hired/djz notes); asof junk sweep (courier 2014, hustle 2010, lattice).
3. A/B + standing duties on the $1B+/public slice; final rebuild only if the delta made a membership verdict.
4. Profile (derive-profile, write-profile, build-firm-profile), plain verify, export, review, report, close.
