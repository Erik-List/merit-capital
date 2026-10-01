# Kleiner Perkins run (PRO-99): resume notes

Started 2026-09-30 ~17:25 EDT. Playbook read in full. Linear PRO-99 In Progress; two kickoff comments posted
(derivations, then the X1 re-derivation to provisional IN).

## Done
- Site: WordPress REST (scratch/pull-wp.py, shape-site.py) -> sources/site/company-list.json (416), team-pages.json (30),
  posts.json (205, post-index.py). site-portfolio.py run.
- Archive: Internet Archive in machine-wide cooldown until ~22:42 EDT (a queued ia-cdx-map.py waits for it). Common Crawl
  used instead (cc-cluster.py / cc-fetch.py on the shared `ccdata` throttle, 4/s, 60 s backoff on 403); parsed by
  kp-parse.py into sources/wayback/parsed/2008-2026 (no 2011). Eras: portfolio-php 2008-10, china-php 2010,
  company-page 2012-18 (Teams/Initiative/Partners), kp-tiles 2018-26.
- Roster: scratch/build-roster.py -> 78 people. EDGAR: entities.json (85), edgar-companies (120), formd-sweep (1,375
  accessions / 642 issuers), formd-issuer-rounds, fts-hits (947 registrants), wikipedia-insource (434 articles).
- ADV: sources/adv/{161035,161470,304391}.pdf; scratch/parse-adv-7b.py -> KP 7.B(1) $20.69B, KPCB China $0.36B.
- decisions.md: D1-D7, X1 (KPCB China provisionally IN; TDF-era deals out), R1-R6.
- config.json: traps in verify.not_members (alcatel, TDF deals, thayer SPAC).
- identity-merges.json: 9 merges (duplicates listed in JUDGE-BRIEF run notes).
- Base built (build-1.log): 1,099 rows. prepare-1: 25 batches, in-flight marker written.
- FTS recall triage: recall-fts-0..4.json done (5 agents). Recall probe agent running -> recall-probe.json.
- Grind: 13 judge agents j01-j13 (batches 1-25), told to record per batch.

## Next
1. When judges finish: `run.py status`; re-run any batch left open.
2. Consolidate recall: recall-fts-*.json adds/targets not in base + recall-probe.json; verify R1-grade leads
   (GO Corp, Oblix, Portera, Medibuy, Broadband Office, Geocast, Zambeel, Evant, Vividence, FirstLook, Vanguard Solar,
   FreeMarkets IPO-allocation conflict, HomeGrocer, iScribe, Himax Display, Oura); write ledger recall_additions
   (no judge recording at the time).
3. IA pre-2008 leg after ~22:42 (kpcb.com 1996-2007 portfolio listings) -> parsed years -> recall.
4. ONE rebuild (copy scratch/queue/queue.json first), re-prepare delta, delta grind; second rebuild only if the delta
   rules membership.
5. graduation-surfaces.py, S2A pass; A/B pass (caps.py for public rows, $1B+ private, momentum slice); duties s8;
   stage-label score for site `Growth` (entry_stage_fields).
6. Profile (thesis "Make history."; AUM 7.B composite; funds from posts: KP20 $800M + Select II $1B 2022, KP21 $825M +
   Select III $1.2B 2024, KP22 $1B + $2.5B growth 2026), icon, firm-offices.
7. verify, export, review (serve), report.md, write-back, close, commit, ingest gate, sibling alignment, message.
Usage at ~19:35 EDT: 5-hour 53%, weekly 52%, Fable 7% (read late; kickoff reading missed).

## Findings to act on after the grind (collected from judge reports)
- Merges added to identity-merges.json from j12 (legal-name Form D issuers). Collect more from each report.
- Partner-carried class check: live-site rows whose only link is a partner's prior-firm deal (Greenhouse = Mamoon Hamid's
  Social+Capital 2014 seat; Culture Amp = Ilya Fushman's Index 2017 seat). Sweep: site rows first archived only after the
  partner joined (Hamid 2017, Fushman 2018), since-year before that, no KP round in the record.
- Asera, Inc. (KP company; SEEC bought its assets) -> recall addition.
- Stage undetermined on famous rows (Google, Electronic Arts, Excite, Genomic Health, ...) -> A/B stage citation pass.
- Collisions to rule `distinct` in cross-rulings.json: endgame (a16z), fauna (gv), handshake (a16z/greylock/sequoia/
  point-nine), helix (gv), good-technology (nea: Visto), modern-life (thrive), resonate (y-combinator).
- Superhuman hq_country garbage from Wikidata; turo defunct from bad Wikidata join (j12 says private).
- nq.py jammed (KP's 2 Google News slots saturated by 13 judges).
- j09: collisions Pelago (a16z, atomico, eqt, yc), Presto (usv, yc), Optic (yc; greylock same co), Signal (lightspeed),
  Roadrunner (headline), Parallel (sequoia, yc). Stale siblings: Profound (lightspeed, sequoia -> $1.8B), Rogo (sequoia,
  thrive -> $2B), Plum District (general-catalyst: acquired by Coupon Lawn 2020). 26 status unknown (13 KPCB China).
- j02: collisions endgame/fauna/handshake/helix/good-technology (above). Renames: Intercom->Fin, FLX Bio->RAPT,
  FindTheBest->Graphiq, GOGII->textPlus.
- Sale-consideration targets to add (recall): TiMetra (alcatel), ONI Systems (ciena), InnerCool Therapies (cardium),
  Asera (seec). Handspring/Siara already rows (palm, redback out).
- Partner-carried calls made by judges: box (Hamid at USVP), chronosphere (Braswell pre-KP: VERIFY, site dates 2021
  Growth), greenhouse, culture-amp (to sweep). Cognition vs Windsurf sale consideration (check); applied-materials T3?
- Collisions (more): betterworks (redpoint), coda (insight: Coda Payments), adknowledge (tcv), bump (a16z, felicis,
  sequoia, yc: Bump Technologies), assured (first-round, iconiq: withassured.com), chutney (yc), phantom (a16z,
  lightspeed, sequoia), rain (lightspeed, iconiq), pilot (usv), pattern (first-round), pivotal.
- Sibling disagreements: altarock (khosla unknown vs acquired by Ormat 2025), captions (a16z says a16z led B; company
  says KP led), smiledirectclub (spark defunct vs acquired by SmileSet), quirky (a16z defunct vs acquired).
- Unconfirmed merges (check): china-credit-loan-stealth-company = credit-ease?, bump = secured?, emdeon-corporation lineage.
- relayr city_country_conflict (Berlin vs US prefill). axion Form D joined to Axion BioSystems (wrong).
- zume ($2.25B mark; KP membership only via vendor) -> A/B membership check.

## State at ~19:30 EDT (grind done)
- Grind complete: 925 member / 174 not_member; 108 items with leftover needs (mostly hq_city; re-queued at delta).
- 63 merges + never_merge q/q-entertainment in identity-merges.json. R7 (partner-carried) in decisions.md.
- recall-candidates.json: 51 candidates to inject at the rebuild (ledger recall_additions).
- graduation-surfaces.py running (grad-surfaces-1.log). caps.py done (caps.json: 59 priced, 33 unpriced).
- 5-hour usage window hit 95% at ~19:15; resets 20:40 EDT. Parked. Then launch: AB-BRIEF (ab1a, ab1b, ab2, ab3) and
  ST-BRIEF (sta, stb) from queue/ab1.json, ab2.json, ab3.json, st.json (ab-lists.py).
- IA cooldown ends ~22:42 EDT: pre-2008 kpcb.com leg, then consolidate, ONE rebuild, delta prepare + grind.
- PROFILE-BRIEF.md written (launch after the window resets).
- 20:45 EDT: launched ab1a, ab1b, ab2, ab3, sta, stb, profile. Done: profile (profile-research.json), ab3, ab2.
  ab3: applied-materials + dmx-technologies not_member (T3); naukri member (Murugan Capital pre-IPO); aleees no usd (TWD
  not an ECB currency); instacart $9.98B 1b_plus vs nine siblings 10b_plus. ab2: fin acquired (closed 2026-09-14);
  discovery-loop needs_web_value (my call: below_1b unless a priced round is cited); maxima carries a namesake
  sec_public_float source in resolved.json.
- 21:15 EDT: ab1a, ab1b, sta done. R7 not_member now 13 rows: box, yammer, wave, neon, chronosphere, persona, pilot,
  built, cultureamp, front, castlight-health, coverwallet, instaedu. cognition stays member (its Series E post names KP).
  flextronics-international has the applied-materials T3 shape (open). google 1999 round A vs B left undetermined.
- Site label score (scratch/stage-score.json): Growth 42/43 -> promote as first_party HIGH in config
  site_api.entry_stage_fields=["stage_site"] AFTER the profile agent finishes (it may edit config). Early: 63 A / 27 Seed
  / 38 Growth -> anchor only.
- ia-pre2008.py queued (waits on the IA cooldown, ~22:42) -> sources/wayback/ia-manifest.json; then parse + recall.
- Profile writer agent running (write-profile.py, build-firm-profile, icon dry-run).
- stb still running.
- 21:30 EDT: stb done (R7 +netskope, +onelogin = 15 rows). Profile agent done (investor.json + sources.json pass
  build-firm-profile and profile_copy; icon source sources/site/kp-mark.svg, dry run only). config entry_stage_fields
  set to ["stage_site"] (run scripts/first-party-stage.py after the rebuild). prepare-2 re-queued 33 open rows; judge d1
  running (graduation pass, DELTA-BRIEF.md). queue-original.json saved for duty 7.
- Next: when d1 is done and ia-pre2008.py has fetched (after 22:42): parse IA pages into parsed/<year>.json, write
  recall_additions from recall-candidates.json into the ledger, rebuild, first-party-stage, prepare, delta grind,
  final rebuild, duties, cross-investor rulings, verify, export, review, report, close, commit, ingest.
- ~21:50 EDT: d1 done (graduation pass on the 33 open rows: 13 graduated, 5 not, 1 censored; 9 skip duplicates remain
  queued until the rebuild). CROSS-BRIEF.md adapted (run after the final rebuild with cross-list.txt from verify).
  Waiting only on the IA cooldown (~22:42) for ia-pre2008.py.
- ~22:00 EDT: REBUILD #1 done (build-2.log): 51 recall additions injected (ledger recall_additions), 64 merges applied,
  186 not_member excluded; base 906 rows. Rename trap fixed by hand: verdicts restored on box, pilot, wave, p-cube,
  cgen-digital-media-acquired-by-focus-media, novavax-inc (and biocryst-pharmaceuticals given biocryst's verdict).
  config: wayback.site_url_base -> kleinerperkins.com (so stage citations resolve); entry_stage_fields=["stage_site"];
  run `first-party-stage.py kleiner-perkins --apply` AFTER the final rebuild (dry run now finds no citation).
  prepare-3: 54 rows (52 membership). Delta judges e1 (batch 1), e2 (batch 2) running.
- Then: IA leg (ia-pre2008.py, auto after ~22:42) -> parse -> parsed/<year>.json; FINAL rebuild; first-party-stage;
  prepare; judge IA rows; duties 3 and 7; CROSS-BRIEF agent (cross-list.txt from verify); verify; export; review; report.
- 69 stale classification keys (merged duplicates) reported by status: check verify rule 8 after the final rebuild.
- e2 done: 8 member, zambeel not_member (R1; check the IA 2001-03 listing: a listing reverses it). total-entertainment-network: weak CIK join to Total Luxury Group (duty 3).
- e1 done: 36 member, 7 not_member (columbia-care homonym, hippo Bond, freemarkets T3 IPO allocation, oura sale
  consideration for proxy, broadband-office/evant/portera R1-R2). CHECK `drop`: recall source said Dublin kitchen-scale
  Drop, e1 classified it as Massdrop (San Francisco): identity conflict, verify which one KP backed or rule out.
  Weak: medibuy (paywalled sentence), hybritech/ministor/imagic/nftfi graduations, homegrocer Series A (medium).
  Sibling: first-round `drop` Massdrop acquired by Corsair 2023; NEA picaboo acquired 2025.
- ~22:30 EDT: cx1 done; apply-cross.py wrote companies/cross-rulings.json (45 distinct, 33 accepted incl. 8 Instacart
  band-edge + 25 sibling-stale) and scratch/align/<book>.jsonl for 13 books (25 rows). At ingest: record each kit in its
  book (skip in-flight / dirty books), re-export, re-ingest via the s9 gate, then remove the aligned pairs from accepted.
  `drop` identity settled (Massdrop; TechCrunch 2014 names KPCB). entremed-inc verdict recorded (lead1).
  Duties agent (du) running: duty 7 blind 5%, duty 3 weak CIK, duty 8 floats -> duty7.json.
  WebSearch budget: about 180 of 200 used; no more WebSearch for agents.
- du done: duty 7 sample 45, 32 field disagreements on 22 rows, 11 corrected (flag unstable); duty 9 classes: early
  Form D band on a later round (47 reviewed, 17 corrected; cause: prepare's older-company test misses Form Ds ticking
  "over five years ago" -> write-back), missing focus (14 filled); duties 3/8: namesake float provenance removed on 7
  rows. duty7.json holds the detail. graphiq/findthebest merge added.
- ~23:15 EDT: IA cooldown re-armed for another hour at 22:43 (ia-pre2008.py crashed on a non-JSON refusal; killed with
  ia-cdx-map.py). DECISION: close without the pre-2008 IA leg (NEA precedent), record the gap + spawn a follow-up task.
- FINAL rebuilds done (build-3, build-4): base 890 members, 202 excluded, queue empty. first-party-stage applied (11
  lines). verify-1.txt: 17 problems = 16 cross pairs S-Z (cx2 agent running -> cross-plan-cx2.json, then re-run
  apply-cross.py) + C2A 83.3% guard (config shape now 0.85, decisions R8). names.published written (67). R9 added.
- Remaining: apply cx2, verify clean, export, review (serve + check), report.md (agent), write-back proposal, close,
  commit (pathspec kleiner-perkins only), ingest gate (icon upload, ingest-investor, ingest-companies --dry-run, removal
  check, write, readback), sibling alignment from scratch/align/*.jsonl, Linear comment + Done, memory, final message.
