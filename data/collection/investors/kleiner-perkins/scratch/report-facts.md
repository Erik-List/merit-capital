# Facts for report.md (PRO-99 Kleiner Perkins), from the lead session. Everything else is on disk.
- Run: one session, 2026-09-30, about 17:25 to past midnight EDT. Prompt count 1 (the kickoff "please collect Kleiner Perkins").
- Usage line: kickoff reading missed; first reading at ~19:15 EDT: 5-hour 95%, weekly 64%, Fable 7% (the run parked 80 min
  for the 5-hour window); at close: weekly 72%, Fable 8%. Base rows 890. WebSearch about 180 of 200.
- Final numbers (verify-3.txt, plain verify clean): 890 members; 202 excluded (all not_member); 1,159 ledger verdicts, 0 uncertain;
  $1B+ 128 (87 1b_plus, 30 10b_plus, 11 100b_plus); entry_stage Growth 198, Series A 156, Seed 68, undetermined 464 nameable + 4
  unnameable; S2A: 68 seed entries, 8 censored, cohort 60, graduated 50, not graduated 10, 83.3% (guard restated 0.85, R8).
- Layers: live WordPress REST (416 companies, first_investment_stage Early/Growth, since-year, Current/Prior); Common Crawl for
  kpcb.com/kleinerperkins.com 2008-2026 (88,081 index records; eras portfolio-php, china-php, company-page, kp-tiles; parsed by
  scratch/kp-parse.py; 2011 has no capture); Internet Archive in machine-wide cooldown for the WHOLE run (8 h block, re-armed
  at 22:43 when it lifted), so the pre-2008 leg (kpcb.com 1996-2007 listings) is NOT collected: scratch/ia-pre2008.py is ready,
  a follow-up task is spawned; pre-2008 coverage rests on the live site's Prior rows, the funds' ownership filings, the EDGAR
  full-text sweep and the recall probe. Roster 78 (scratch/build-roster.py). Form D sweep 1,375 accessions / 642 issuers.
  edgar-companies 120. FTS 947 registrants (725 third-party; triage recall-fts-0..4.json: 488 triaged). Wikipedia 434 articles.
  Retired Sanity CMS (project ti7si9cx) probed: dataset deleted (negative result). Gatsby page-data not in Common Crawl.
- Rebuilds: build-1 (initial, 1,099 rows), build-2 (the scheduled one: 51 recall additions, 64 merges, 186 excluded), build-3
  and build-4 (final, after the delta's membership verdicts; hippo-analytics-inc variant). Rename trap hit on build-2 and fixed by
  hand (R9). Recall: 51 candidates landed, 44 judged members (e1 36, e2 8), 7+1 not_member.
- Boundary: D2 Bond; X1 KPCB China provisionally IN (flag kpcb_china on those rows; count them from classification.json);
  R7 partner-carried: 15 rows out (box, yammer, wave, neon, chronosphere, persona, pilot, built, cultureamp, front,
  castlight-health, coverwallet, instaedu, netskope, onelogin). T3 outs: applied-materials, dmx-technologies, casi/entremed,
  biocryst, novavax, platinum-software, seec, freemarkets. Sale consideration outs: alcatel, ciena, cardium, palm,
  redback-networks, hyperion-solutions, travelocity, superhuman, windtree, oura. TDF-era outs: alibaba, baidu, china-netcom,
  focus-media, hurray, cgen, p-cube, kanghui.
- Site stage label score: scratch/stage-score.json (Growth 42/43 promoted first_party high; Early 63 A / 27 Seed / 38 Growth,
  anchor only). first-party-stage applied 11 lines.
- A/B: ab1a, ab1b (74 private $1B+), ab2 (32 momentum rows, none at $1B+; duty 6), ab3 (86 public rows, caps.json), sta/stb
  (130 rows; 57 stages cited), d1 graduation pass, duties du (duty7.json: sample 45, 32 field disagreements on 22 rows, 11
  corrected; classes swept: early Form D band on a later round 17 corrected, missing focus 14 filled; 7 namesake floats).
- Cross-investor: cross-plan-cx1/2/3.json; cross-rulings.json 57 distinct, 39 accepted (8 Instacart band edge; 31 sibling
  stale, alignment kits in scratch/align/ for 13 books).
- Profile: write-profile.py; thesis "Make history."; AUM $20,693,034,506 to $21,051,591,900 (7.B composites, exempt reporting
  adviser); 22 funds; notables Google, Amazon, Twitter, Spotify, Airbnb; HQ Menlo Park, CA; icon source sources/site/kp-mark.svg.
- Open rulings for Erik: X1 (KPCB China in or out); R7 class (15 rows incl. Netskope, a $7B public row); R8 (S2A rate 83.3% on
  the cited subset: publish with caveat or decline); flextronics-international (T3 shape like applied-materials); google's 1999
  round (Series A or B, left undetermined, cite_pending); DJI mark ($15B reported 2018 bidding vs $8B priced 2015); discovery-loop
  (talks at $10B unpriced, kept below_1b); OTC-quoted rows (neomagic, rong360) kept public; zambeel/broadband-office/evant/
  portera (R1/R2 not_member, probably true members); medibuy (member on a paywalled sentence); altarock-energy (unknown vs
  private); the Instacart band-edge acceptance; the pre-2008 Archive leg.
- Write-back proposals (COLLECTION.md is edited only by the tooling session): (1) Common Crawl scripts must use
  shared_throttle "ccdata" and back off 60 s on 403 (three sessions earned a 403 block on 2026-09-30); add ccdata to
  DEFAULT_RATES. (2) R7: a live site can list a new partner's prior-firm deals WITH a year and stage; the Menlo signature
  ("no dated milestone") is too narrow. (3) build-company-base takes the firm host from wayback.site_url_base, so a rebranded
  firm's per-company pages are not recognised as stage citations: read site_api.base too. (4) prepare's older-company test
  misses Form Ds that tick "over five years ago" (duty 9 class, 17 rows). (5) ADV 7.B parser: read each fund's value from its
  own block (ivp's pairing misreads this PDF layout). (6) verify's cross-investor listing is capped (79 lines shown of 94): print
  all or say so. (7) A queued IA script should not fire the instant a machine-wide cooldown lifts (several sessions re-armed it).
