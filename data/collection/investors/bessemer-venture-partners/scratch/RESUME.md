# Bessemer run (PRO-80): resume notes

Started 2026-10-01 ~10:30 EDT. Playbook read in full. Linear PRO-80 In Progress; kickoff comment posted
(derivations D1-D10, delta X1). Usage at kickoff: 5-hour 3%, weekly 73%, Fable 8%.

## Environment traps (read first)
- **Disk nearly full** (228 GB disk, ~2 GB free; swap grows under memory pressure and eats it). At 11:07 it hit
  100% and writes failed (ENOSPC). I cleared the npm and pip caches (+1.8 GB) and told Erik by notification. Keep
  subagent concurrency at about 4; never write shared files non-atomically; a background watcher alerts under 500 MB.
- Internet Archive: machine-wide cooldown 10:36-11:36 EDT; scratch/cdx-map.py (bvp.com URL map) waits behind it.
  Common Crawl carried 2008-2026. Only ONE cc-fetch / cc-plan process at a time (two overwrote the manifest once;
  scratch/cc-manifest-repair.py restores entries from disk).
- run.py subcommands take the slug positionally for collect/prepare (`run.py prepare bessemer-venture-partners`),
  `--investor` for record/status/verify/export/review/close.

## Done
- Site: Sanity dataset (project 2e9xvz8g) -> scratch/pull-sanity.py, shape-site.py -> sources/site/company-list.json
  (534), team-pages.json (315), posts.json (537: 19 memos, news, atlas; post-index.py), anti-portfolio.json (24 names).
- ADV: data/filings/adv/159279.pdf; sources/adv/adv-7b-funds.json (54 funds, $20.26B; RAUM $20,239,213,324).
- Archive (Common Crawl): scratch/cc-cluster.py (index, 128 crawls), cc-plan.py (fetch), bvp-parse.py ->
  sources/wayback/parsed/2010,2012-2026 (929 companies; eras aspx-list 2008-12 with the firm's own investment year
  back to 1957, aspx-exits, drupal-list, drupal2-list with investment DATE, site2019-list, wp-list). Name variants
  folded in the parsed source (scratch/name-groups.json).
- Roster: scratch/build-roster.py -> sources/wayback/partner-roster.json (166 people).
- EDGAR: entities.json (152; desks bvp / forge / external by filing address, scratch/entity-addresses.json),
  formd-sweep.json (1,342 accessions, 636 issuers), edgar-companies.json (66), fts-hits.json (436 registrants, 296
  third-party), wikipedia-insource.json (150 articles).
- config.json: desks, traps (verify.not_members = the anti-portfolio, 41 name keys). decisions.md: D1-D10, X1.
- Base built (scratch/build-0.log): 1,095 rows (A 590, B 309, C 196). prepare-1 started 11:28 (membership seed: 898
  site_listing, 7 fund_filing, 190 for the judge).
- Tooling ported from Kleiner Perkins: judge_lib.py, show.py, evidence-pack.py, siblings.py, nq.py, bvpslot.py,
  wikifetch.py, secget.py, ftsview.py, fts-triage-prep.py; briefs JUDGE-BRIEF.md, RECALL-FTS-BRIEF.md, RECALL-BRIEF.md.
- Anti-portfolio harness (D10), measured 11:30: base 0 hits, Form D sweep 0, fund filings 0, Wikipedia 0, EDGAR
  full text 3 of 296 third-party registrants (eBay: stock received for Skype, 2005 S-3; Okta: stock received for
  Auth0, 2021 424B7; Zoom 2026: to triage).
- Launched 11:32: recall agents fts shard 0, fts shard 1 (sonnet), recall probe (recall-fts-0/1.json,
  recall-probe.json).

## Next
1. When prepare-1 finishes: re-run evidence-pack.py; launch judges (4 at a time; JUDGE-BRIEF.md; tags j01..).
2. IA pre-2008 leg after the cooldown: cdx-map -> fetch bvp.com portfolio listings 1997-2007 -> parsed years -> recall.
3. Consolidate recall (recall-fts-*.json, recall-probe.json, IA leg) into ledger recall_additions; Forge deals into
   config verify.not_members; ONE rebuild (copy scratch/queue/queue.json first); re-prepare delta; delta grind;
   second rebuild only if the delta rules membership.
4. graduation-surfaces.py, S2A pass; A/B pass (public caps, private $1B+, momentum slice); section 8 duties;
   score stage_site for the record (scratch/stage-score.json).
5. Profile (thesis quoted from the site; AUM = ADV RAUM; funds; team from team-pages.json; icon; firm-offices).
6. verify, export, review (serve and check), report.md (incl. the anti-portfolio measurement, how far back the base
   reaches), playbook write-back, close, commit (pathspec only), ingest gate, sibling alignment, closing message.

## State at 12:00 EDT
- **Usage is the binding constraint**: at 11:55 the 5-hour window read 49%, weekly all-models 85% (73% at kickoff),
  Fable weekly 28%. Do NOT exhaust the weekly limit (it blocks Erik's other work until 2026-10-06): park and report
  if weekly reaches about 95%. From here on subagents run on `model: sonnet`; no more Fable judges.
- Disk recovered to 18 GB free at 11:44. IA cooldown doubled at 11:38 (another session), until about 13:38.
- Agents: recall-fts-0/1.json DONE (adds not in base: Triton Network Systems, Knology; targets not in base: Genoa
  Corporation, K2 Optronics, NanoOpto, Trellix, THINQ Learning Solutions, Grow Mobile, LiveVideo (low); Mondee is
  stock received for Rocketrip, already a row; eBay / Okta / Zoom rejected). profile-research.json DONE (funds, range,
  notables Anthropic, LinkedIn, Pinterest, Shopify, Twilio; icon: only inline SVGs usable).
  Running: recall probe (recall-probe.json), jm (batches 21-25, membership), j01 (1-2), j02 (3-4), j03 (5-6),
  j04 (7-8), j05 (9-10), j06 (11-12) on Fable; j07 (13-14), j08 (15-16) on sonnet. NOT yet launched: j09 (17-18),
  j10 (19-20).
- Rulings to write into decisions.md: R1 Netsmart (2007 take-private with Insight: control position, not_member);
  R2 the history narrative's names: Measurex, Fotomat, Interdata (Pete Bancroft's venture practice, 1967 on) are
  recall additions flagged pre_spinout; W.R. Grace, International Paper, Ingersoll Rand, Automatic Sprinkler are the
  family office's early holdings, not rows (X1).
- Thesis (homepage headline): "Forged in steel. Building what's next."

## Judge findings to act on after the grind (collected from reports)
- j08 (15-16, DONE): duplicates dick-s-clothing-sporting-goods = dick-s-sporting-goods; cloudius-systems = scylladb.
  Collisions (rule `distinct`): diligent (speedinvest, yc), daylight (a16z, bcv, usv), flock (a16z). T3 candidates
  kept as members, to sweep: centocor, commercial-federal, ganesh-housing. Nearly every stage undetermined (Sonnet):
  a first-party stage harvest from the archive sentences is owed.
- jm (21-25, DONE): 168 not_member, 22 member. Merges for identity-merges.json (duplicate -> canonical):
  2tor-inc -> 2u; adaptive-planning-inc -> adaptive-insights; hyper-labs-inc -> hyperscience; justin-tv-inc -> twitch;
  dolores-labs-inc -> crowdflower; pinpt-inc -> pinpoint; shop-my-shelf-inc -> shopmy; tinz-optics-inc -> light;
  recover-together-inc -> groups; k2-global-consulting-inc -> k2-intelligence (+ k2-integrity?);
  reputationdefender-inc -> reputation; hellorelish-inc -> relish; tiz-inc -> provi; make-cents-technologies-inc ->
  cents; dyn365-inc -> restaurant365; evolve-bits-inc -> zenskar; t3c-inc -> retail-solutions;
  every-neighbor-deserves-kindness-inc -> mural-health; birch-solutions-inc -> fern; directv-broadband-inc ->
  telocity; learmonth-burchett-... -> lbms; cotinga-pharmaceuticals-inc = critical-outcome-technologies-inc (both out).
  (Check each slug in base.json before writing; the canonical is the site-listed row.)
  New members not on the firm's list: flexcorp-inc (FlexFactor), cozykin-inc; strala-group-inc (director of record,
  medium, for review).
  Control class: ws-holdco-pbc (WiredScore 2017 majority purchase with Fifth Wall) and gfi-software-s-a (Insight
  control 2009, Bessemer via TeamViewer Holdings) ruled not_member; the LISTED twins wiredscore, logicnow, teamviewer
  need the same ruling (and netsmart-technologies: 2007 take-private with Insight). Verify each with a citation.
  Sale consideration: gentle-dental-service-corp out; the investment was GMS Dental Group (missing: recall addition).
- recall probe (DONE, recall-probe.json: 67 rows, 14 forge, 12 vehicles): 14 adds 2020-26 (Moxie Beauty, ShopDeck,
  PrismTPO, Zingage, Perceptron, StayTerra (also on the Forge grid: check), Rain, Sifflet, OFF/BEAT, Harmoni, DualBird,
  Furientis, Fuel Me, Earthly). Measurex / Fotomat / Interdata: no citation beyond the firm's history narrative (the
  2008-12 history page captures name them: cite that capture, R2). Forge deals: Medisolv, Radformation, Parsec,
  Givebutter, Mortgage Automator, Vector, Technical Toolboxes, BetterRx, Sunwave / Lightning Step, Nevvon; control-style
  deals already in base: Litify (majority 2023), CRI, Current. **The bvp.com/forge captures leaked into the parsed
  listings**: nine base rows are the Forge team's prior-firm logos (1010data, appriss, avetta, cority, diligent,
  supplier-io, the-retail-equation, turnitin, vector-solutions) -> fix bvp-parse.py (skip /forge paths), rule them
  not_member, and list every base row whose only archive evidence is a /forge capture.
  **Gator Co-Invest PA/VE/TE/BE/LI are FORGE vehicles** (Parsec, Vector, Technical Toolboxes, BetterRx, Lightning
  Step): move `^gator co-invest` to the forge desk in config and correct decisions D1/D7. Cloud All Star =
  ServiceTitan; PR = Procore; VS = StubHub/viagogo; GoBlue/Wahoowa = Winc; Enforta = Criteo; AN I = Anthropic.
  Duplicates: winc = club-w, stubhub = viagogo, raft = vector-ai.
- j07 (13-14, DONE): anant-raj-industries not_member (T3). Forge-page leak also: absensesoft, boxed? (2022-only rows
  with no year or partner: check). Sibling disagreements to settle: wonderful (IL/Tel Aviv vs insight, ivp
  Amsterdam), zopper (Gurugram vs tiger Noida), zyg (IL vs accel, lightspeed US). Collision: watershed (kp, sequoia are
  the climate-software Watershed). wikia = fandom? Unknown status left: way-systems, watershed, access-360-media,
  activ-financial, applied-solar-technologies, argnor, ba-systems, billshrink, cecure-gaming. Waymo is a row: check
  its membership evidence (first_party stage).
- j02 (3-4, DONE; Fable quality: 76 of 90 stages decided): duplicate disco = cs-disco-inc. Renames: current (was Crete
  Professionals Alliance; check control: Forge-style?), crosschq -> Brilliant AI, dashbot -> Dimension Labs. Collisions:
  current (a16z, gc, tiger), fabric-technologies (six siblings), endgame (a16z, eqt), fandom (redpoint), disco
  (felicis, gc). Lightspeed's Ciena carries country CA (stale sibling). doubleai banded on "exceeding $1 billion"
  (needs a figure, A/B); electric $1B 2022 stale; cri kept Growth (Centerbridge-led: control check). scratch/wiki has
  wrong redirect texts for Cyota, CloudLock, Convertro.
- j09 (17-18, DONE, sonnet: 8 stages named): not_member kcm-biomedical, new-vernon-capital, rock-health (D7 funds),
  medi-assist (management buyout, D5). Duplicate remedinet = remidinet. Flag listed_purchase_check (kept members, T3
  sweep): portrait-software, riddhi-siddhi-gluco-biols, onmobile. Collisions: light (atomico, cherry, seedcamp,
  balderton: the Danish Light), james-river (prefill was the insurer). Sibling disagreements: rabbit (gv acquired),
  myglamm (accel defunct), qwilt (redpoint IL). About 20 status unknown.
- j10 (19-20, DONE, sonnet: about 10 stages named, 70 undetermined): 10tales-inc not_member. Duplicate zirx = stratim.
  Collisions: speakeasy (gv, headline), trigo (menlo, yc), vesta (a16z?). Control checks: syncsort (2008 consortium
  majority purchase with Insight: control position), supplier-io and vector-solutions (Forge-page leak, kept members:
  must go). T3 checks: shriram-epc, tulip-telecom. unipalm note starts with a stray "JP-free:" (fix). "first
  institutional" was read as Series A for ungermann-bass and vmx: the brief says only where the record calls it that;
  re-check in the stage pass.
- j03 (5-6, DONE): not_member gts-central-europe (control, consortium bought the whole company, 2008-01), insmed (sale
  consideration for Transave, which is a row). Duplicates: fin = intercom, fuze = thinking-phone-networks,
  good-glamm-group = myglamm, isis-pharmaceuticals = ionis-pharmaceuticals. Rename: GlossGenius -> Genius (2026-07).
  Sibling alignment: farther (here 1b_plus on a "$1-billion-plus" headline floor: needs a figure; lightspeed below_1b),
  indian-energy-exchange (here below_1b $978M 2026-10-01; lightspeed 1b_plus). Collisions: fulcrum (gc, yc), guild (yc,
  battery), kindred (first-round, gv), jasper (northzone, sequoia). flex-pharma: public via successor shell, check.
  Wrong wiki redirect caches: Flarion, Habana_Labs, Kandou, Kroll_Bond_Rating_Agency.
- j06 (11-12, DONE): not_member teamviewer (control: Insight-led buyout vehicle 2009), threattrack-security (spin-off
  of the GFI holding), team8 (D7 fund-shaped). Duplicates: skybox-imaging = terra-bella-fka-skybox-imaging;
  thinking-phone-networks = fuze; stubhub = viagogo; urban-company = urbanclap; torq = stackpulse; twitch =
  justin-tv-inc. OPEN FOR ERIK: `ual` read as Uala the Argentine bank ($3.2B) but the first archived listing describes
  Uala the Italian beauty marketplace: resolve identity before publishing a $1B+ mark. Collisions: spruce (a16z), sweep
  (balderton, coatue, yc), teleport (a16z, seedcamp), valence (yc). Stale siblings to align: upwind (greylock below_1b;
  now $3.8B), trm-labs (yc $1B; now $2B), urban-company (accel private; now public), truebill, sisense, triana, valence
  cities. us-health-partners-llc, teleradiology-solutions: sponsor-style? check.
- j05 (9-10, DONE): not_member shriram-city (T3: listed 2005, BVP India stake 2008). Duplicates: quidsi-fka-diapers-com
  = diapers-com; scylladb = cloudius-systems; sign-in-enterprise = traction-guest; raft = vector-ai; reputation =
  reputationdefender-inc. Stale siblings: sarvam ($1.5B; lightspeed below_1b), quantopian (defunct by the acqui-hire
  rule; a16z, khosla, spark acquired), city differences (playdom, second-measure, rundoo, qventus). Collisions: ramp
  (balderton, seedcamp: Ramp Network), sentra and rosebud (a16z speedrun), shift-technology (cherry, yc). scopely:
  no source ties Bessemer to a round (membership rests on the listing). quidsi, sila: Form D stage misdated.
- j04 (7-8, DONE): not_member litify (majority purchase 2023-02), netsmart-technologies (2006 take-private with
  Insight), ola (sale consideration: TaxiForSure; check TaxiForSure is a row, else recall addition), logicnow (GFI stock
  from the 2010 TeamViewer merger). Duplicates: matrimony-com = bharat-matrimony; neuehealth = bright-health-group;
  medibuddy-fka-docsapp = docsapp (and it carries Medi Assist's archive: check the name grouping); logicnow =
  gfi-software-s-a. Possible control positions kept as members (rule them): liveauctioneers ("growth buyout"),
  metalogix (with Insight, 2008). Collisions: milo, pana (yc), nym (a16z, lightspeed). Sibling conflicts: mealpal (menlo
  defunct; live), netography (a16z private; acquired by Vectra), onaroll (lux private; acquired), neuehealth city,
  lightspeed nym-health not_graduated vs a named Series A.

## PARKED 2026-10-01 12:35 EDT (usage)
Weekly all-models limit read 95% (73% at kickoff), 5-hour window 85%, Fable weekly 45%. Parked as planned so the
weekly allowance is not exhausted. Nothing committed yet; the in-flight marker stays (siblings skip this book).
State: 932 of 1,095 items answered; membership 911 member / 184 not_member; j01 (batches 1-2, Fable) was still
running at the park and records per file, so re-check `run.py status --investor bessemer-venture-partners` first and
re-run whatever of batches 1-2 is still open (use `model: sonnet`).
Resume order (each step is in "Next" above, with the findings list as the worklist):
 1. Finish batches 1-2 if open. 2. Fix bvp-parse.py to skip /forge paths; move `^gator co-invest` to the forge desk;
 correct decisions D1/D7; write R1 (control: netsmart, teamviewer, logicnow / gfi, wiredscore, litify, gts, syncsort,
 metalogix?, liveauctioneers?), R2 (history-narrative names), R3 (India listed-company purchases, T3), Forge traps in
 config. 3. identity-merges.json from the duplicate pairs. 4. recall_additions in the ledger (FTS adds and targets,
 recall-probe adds, GMS Dental, TaxiForSure if missing, Measurex / Fotomat / Interdata). 5. IA pre-2008 leg if the
 archive answers. 6. Copy queue/queue.json, ONE rebuild, prepare, delta grind. 7. First-party stage harvest for the
 Sonnet batches (13-20: most stages undetermined although the archive sentences name rounds). 8. graduation-surfaces,
 S2A, A/B, duties, profile (profile-research.json is ready), verify, export, review, report, write-back, close,
 commit, ingest gate, sibling alignment.
- j01 (1-2, DONE after the park): all 90 recorded, no not_member. Control questions kept as members: beyond ("growth
  buyout" on the firm's page), bumble (2020 entry inside Blackstone's control purchase?). altair-semiconductor read
  private after its 2026-04 spin-out from Sony. Stale siblings: betterment $1.3B (menlo below), boom-supersonic $1.5B
  (8vc below), astrix acquired (menlo private), candid-co private (headline defunct). Collisions: alloy (20vc, 8vc, bcv,
  menlo, yc), august, avalanche-technology, axion, beyond, brainbase, breaker. 21 stages undetermined; 16 on model.
  THE FIRST GRIND IS COMPLETE: every batch 1-25 has been judged. Next is step 2 of the resume order.

## STOPPED BY ERIK 2026-10-01 ~12:45 EDT (interrupt after "continue")
Done between the resume and the stop: judgments-lead1.py recorded (11 Forge-team prior-firm rows not_member: 1010data,
absensesoft, appriss, avetta, cority, diligent, galvanize, supplier-io, the-retail-equation, turnitin,
vector-solutions; they were on bvp.com/companies in the January 2022 capture only, NOT a /forge-path leak, so
bvp-parse.py needs no change); companies/identity-merges.json written (42 merges). The boundary agent `bd` (control
positions list A, listed-company purchases list B) was stopped before it wrote anything: its lists are in the
session transcript and in the findings above. No agents are running. Stage coverage measured: 911 members, 418
undetermined, 12 of them with a round word in first-party text (queue/stage-harvest.json).
Still to do, in order: gator -> forge desk in config and D1/D7 correction; rulings R1-R4 in decisions.md; Forge and
control traps in config; boundary checks; recall_additions; rebuild; delta; S2A; A/B; profile; verify; export;
review; report; close; commit; ingest.

## RESUMED 2026-10-06 14:16 EDT (Erik: "continue"; session model now Opus 5.5; weekly usage reset to 1%)
Done since the resume:
- config.json: `^gator co-invest` moved to the forge desk; `run.py collect` re-run (entities.json: bvp 75, forge 13,
  external 64; edgar-companies 66, unchanged). decisions.md: D1/D7 corrected; rulings R1-R7 written.
- sources/site/history-narrative.json: the firm's 2008 history page (42 paragraphs, round statements for the famous
  deals); evidence-pack.py and show.py carry it (`history`); show.py also prints the stored answers and takes
  `--list <queue file>`.
- **Internet Archive pre-2008 leg** (scratch/ia-pre2008.py -> sources/wayback/ia-manifest.json, bodies under
  data/filings/wayback/bessemer-venture-partners/): /port/onepage.asp 2002-2007 (110 to 232 companies a year, the
  2005+ captures carry the old book with a sentence each), /port/success.asp 2002-03 (investment month, round
  sentences), /people/** 1999-2001 (26 of 45 sector pages; investment year and partner per company), the
  anti-portfolio 2000-2006. bvp-parse.py has the handlers (asp-onepage, asp-success, html-people), TICKER_NAMES and
  ALIASES (old rendering -> later name). Parsed years now 2000-2007 too. **113 companies the base lacks** (mostly
  dot-com and optical-era failures the 2008-12 list dropped). IA cooldown hit again at ~15:40 for 50 min; the fetch
  process keeps waiting and will finish the 19 missing sector pages, then 250 redundant /port/investor.asp pages
  (kill it once the sector pages are in: `pkill -f ia-pre2008.py`).
- Anti-portfolio now 27 names (added Exodus, ROLM, USWeb from the 2000 page); 45 trap keys in config.
- scratch/recall-additions.json: 20 additions ready for the ledger (14 probe, Triton Network Systems, Grow Mobile, GMS
  Dental Group, Measurex, Fotomat, Interdata). Genoa, K2 Optronics, Knology, NanoOpto, Trellix, THINQ are now on the
  firm's own archived list, so they need no recall addition.
- Agents running (Opus): `bd` (control positions and listed-company purchases; judgments-bd*.py), `s21`-`s24` (second
  pass on 285 rows of batches 13-20 left undetermined or unknown; STAGE2-BRIEF.md; queue/s2-<n>.json).
Next: when bd and s2x are done and the sector pages are in -> re-parse, write recall_additions into the ledger, copy
queue/queue.json, ONE rebuild (read the rename list), prepare, delta grind (about 135 new rows; Voyant Technologies
is sale consideration by the firm's own sentence: "Voyant acquired BVP's portfolio company Octave"), then S2A, A/B,
profile, verify, export, review, report, close, commit, ingest, sibling alignment.
- 15:20: bd DONE (14 out: R1 syncsort, wiredscore, metalogix, cri, liveauctioneers, beyond, current, harman; R3
  centocor, commercial-federal, ganesh-housing, portrait-software, riddhi-siddhi-gluco-biols, tulip-telecom; unsettled,
  kept: bumble, intego, us-health-partners-llc, teleradiology-solutions, car-wash-partners, vision-express-group,
  cogent-communications). decisions.md R1/R3/R7 updated, R8 (Ualá = the bank) added.
- Profile agent DONE: scratch/write-profile.py (re-runnable), investor/investor.json + sources.json written once
  (886 members). Thesis "Forged in steel. Building what's next."; founding 1981; AUM RAUM both ends; 12 funds; HQ
  Larchmont NY by the rule; icon dry run ok (sources/site/bvp-mark.svg; upload at ingest with
  `npx tsx scripts/fetch-investor-icon.ts bessemer-venture-partners data/collection/investors/bessemer-venture-partners/sources/site/bvp-mark.svg`).
  config: team_buckets now only {"investor": "investing"} (58 people; 46 linked = 79.3%, socials_gap recorded; two
  checked searches would lift it over 80%). RE-RUN the five profile commands after the base is final.
- s23 DONE (27 stages, 10 statuses). Merges added: topfreegames -> wildlife-studios, soap-com -> quidsi (44 merges).
  Stale sibling: greylock sahara-networks city (Wallingford CT, not Sunnyvale). ziff-davis-enterprise: R1 candidate
  (Insight bought it 2007; Bessemer's role not found; bd kept it on a 2008 $20M raise).
- bvp-parse.py: the 2012-2015 site (drupal-list) printed the investment year one year EARLY for January 1 placeholder
  dates (98 companies, 301 rows): corrected in regroup(), printed year kept as invest_year_as_printed. The base's
  first_seen picks this up at the rebuild.
- s21, s22, s24 still running at 15:20. IA cooldown ends about 15:32.
- 15:30: s21, s22, s24 DONE too (second pass total: 121 stages decided, about 40 statuses settled; verdict changes:
  james-river, portrait-software, tulip-telecom, commercial-federal, centocor, argnor (D7), homelight (R6, Eave is
  the row), vts (R6: stock for Hightower; `hightower` is the member row; view-the-space-fmr-hightower also out)).
  Merges now 49 (added sonic-mule->smule, vimo->getinsured, tribe->bettermode, billshrink->truaxis,
  innovati->innoviti, flat-world-knowledge->sagence, topfreegames->wildlife-studios, soap-com->quidsi; intercom is
  canonical over fin). AFTER THE REBUILD: copy a decided stage from a merged duplicate onto its canonical where the
  canonical reads undetermined (fin -> intercom Growth 2014-01; sonic-mule -> smule Seed graduated; etc.).
- A/B pass launched 15:20 on existing rows (AB-BRIEF.md): ab1, ab2 (76 private $1B+), ab3 (60 public), ab4 (momentum
  80 + duty 6). ab4 DONE (no band-ups; intercom acquired 2026-09-10). ab2 DONE (snapdeal public as AceVector since
  2026-10-05, $147M; devo $2.0B; 6 re-pins; stale flags).
  **Sibling alignment worklist so far** (book, slug, what it should read, citation):
  insight-partners vts $1.7B@2022-09-06 stale (finledger); index-ventures intercom acquired, Salesforce release
  2026-09-10 (in flight: skip); gv intercom asof 2026-09-10; insight-partners + tcv devo $2.0B@2022-06-02
  (venturebeat); accel ada-support $1.2B@2021-05-07 (betakit); tcv klook asof 2018-08 (techcrunch 2019-04-08);
  menlo-ventures betterment $1.3B@2021-09; 8vc boom-supersonic $1.5B@2025-12; 8vc sila-nanotechnologies $2B@2024-06;
  lightspeed farther $1B@2026-05; lightspeed sarvam $1.5B@2026-06; y-combinator trm-labs $2B@2026-09-09;
  sequoia-capital captivateiq (cites a vendor); greylock sahara-networks city Wallingford CT; plus the earlier list
  in this file (upwind greylock, urban-company accel, netography a16z, onaroll lux, mealpal menlo, astrix menlo,
  candid headline, quantopian a16z/khosla/spark, dysan sequoia, rabbit a16z/gc).
- rebuild-locked.py holds record's lock, lands recall-additions.json, runs the build. 88 cross-investor
  disagreements at the in-flight verify (verify-inflight-1.log): a triage agent is owed (Kleiner's CROSS-BRIEF.md and
  apply-cross.py are the template).
- 15:45 REBUILD DONE (build-1.log; rebuild-locked.py): base 1,095 -> 969 rows; 214 excluded; 51 duplicates merged;
  recall additions 20 landed; 110 pre-2008 rows arrived. Backups: base-before-rebuild.json,
  classification-before-rebuild.json, ledger-before-rebuild.json, queue/queue-before-rebuild.json.
  **The rename step mis-moved overlays** (7 "renames", 3 wrong: flat-world-knowledge -> logicnow-gfi, homelight ->
  beyond-pricing, innovati -> vts-formerly-hightower): excluded companies' other name renderings resurfaced as new
  rows (logicnow-gfi, logicnow-s-a, gfi-software-s-a-r-l, gts, beyond-pricing, vts-formerly-hightower,
  view-the-space-inc, ola-cabs, generate-capital-inc) and the rekey matched departures to them. Repaired by hand
  under the record lock: the 7 old slugs' verdicts and 4 classification rows restored from the backups, the 9
  variants given their company's not_member verdict. They leave at the FINAL rebuild (owed; read its rename list).
- lead2 recorded: stages carried from merged duplicates (intercom <- fin, matrimony-com <- bharat-matrimony, smule <-
  sonic-mule, reputation <- reputationdefender-inc).
- graduation-surfaces run (44 open Seed rows, 0 failed lookups); prepare-2 started 15:50.
- A/B DONE: ab1 (sorare and the-exploration-company to below_1b; 12 re-pins; cite_pending abridge, nydig, ual),
  ab3 (57 caps priced 2026-10-06; yelp below_1b $984M; flex-pharma-inc, proteon-therapeutics acquired;
  cogent-communications not_member: it is the PSINet position; signed unclosed deals ACV, Weave, PTC stay public).
  Sibling worklist additions: sorare below_1b (20vc, accel, atomico, headline, ivp, seedcamp); the-exploration-company
  below_1b (atomico, balderton-capital, eqt-ventures); abridge $5.3B@2025-06-24 TechCrunch (a16z, khosla-ventures,
  redpoint-ventures; date only ivp, lightspeed, spark-capital, union-square-ventures); sisense $1.0B@2020-01-09
  (battery-ventures, insight-partners); hibob $3.2B@2026-09-01 Bloomberg (battery-ventures, general-catalyst hi-bob);
  eliseai $4B (a16z); upwind $3.8B (greylock); shopmy $1.5B (menlo-ventures); benchmark yelp below_1b $984.07M;
  lightspeed indian-energy-exchange below_1b $961.9M; accel urbancompany public 1b_plus $2.55B; lightspeed ciena
  country US; lightspeed alloy country US; general-catalyst shift country FR; khosla-ventures rocket-lab stale float.
- IA cooldown extended to ~17:30 (another session); ia-pre2008.py --people-only waits in the background for the 19
  missing sector pages. If they arrive before the final rebuild, re-parse and fold in; else report as debt.
- 15:55: prepare-2 done (181 queued: 130 new rows, 44 graduation, 7 country leftovers). Launched: d1, d2, d3 (delta,
  DELTA-BRIEF.md, queue/d<n>.json), g1, g2 (graduation, GRAD-BRIEF.md, queue/g<n>.json), cx1, cx2 (rule 10 triage of
  73 pairs, CROSS-BRIEF.md, cross-list-cx<n>.txt -> cross-plan-cx<n>.json). scratch/names-published.json: draft of 31
  published-name overrides for config names.published (apply after the final rebuild).
  Port for the end: ../../kleiner-perkins/scratch/apply-cross.py and align/run-align.sh (+ run-align2.py).
- After these: FINAL rebuild (delta verdicts + the 9 resurfaced variants + any late sector pages; read the rename
  list; repair as before), prepare, close any open needs, duties 2/7, profile re-run (5 commands), names.published,
  verify, export, review (serve + check), report.md, write-back, close, commit, ingest gate, sibling alignment.
- cx2 DONE (cross-plan-cx2.json: 24 distinct, 8 sibling_stale, 3 bvp_stale, 1 skip). **Sorare stays 1b_plus $4.3B
  (2021-09-21, stale)**: Erik's ruling E2 of 2026-09-28 in headline/documentation/decisions.md (layoffs do not band
  a row); cx2 reverted ab1's change. REMOVE sorare from the sibling worklist. Sibling rows to write from cx2:
  menlo-ventures astrix acquired + shopmy $1.5B; khosla-ventures moonvalley-ai-inc acquired + quantopian defunct;
  8vc boom-supersonic $1.5B; a16z netography acquired; first-round-capital rupa-health acquired; lightspeed sarvam
  $1.5B.
- The Exploration Company: balderton-capital, eqt-ventures and atomico hold 1b_plus $2.0B @ 2026-07-27 (the FT report
  of the Series C in talks, via The Next Web; the round closed 2026-09 with no price disclosed); ab1 set ours to
  below_1b. Decide with cx1's plan: align OURS back to 1b_plus $2.0B (three books already ruled so) and cherry up.
- 16:20: cx1, cx2 DONE and applied (apply-cross.py -> companies/cross-rulings.json: 45 distinct, 22 accepted; kits
  in scratch/align/<book>.jsonl for 8vc, a16z, first-round-capital, headline, khosla-ventures, lightspeed,
  lux-capital, menlo-ventures, sequoia-capital, spark-capital, y-combinator, cherry). lead3: the-exploration-company
  back to 1b_plus $2.0B (matches atomico, balderton, eqt; cherry kit aligns cherry up). cross-diff-all.json: every
  difference vs siblings by loose name (171, most namesakes): input for the final cross triage (cx3), which must
  also cover figure / country / city differences (abridge, eliseai, hibob, devo, trm-labs, upwind, urbancompany,
  yelp, vts, wonderful, zyg, legora, papaya-global, productboard, sisense, qwilt, ciena, alloy) and the delta rows
  (greylock e-steel / newview-technologies / tiburon-networks, sequoia elemental-security, sutter-hill measurex).
- g1, g2 DONE: all 44 Seed rows decided (14 graduated, 29 not_graduated, salto corrected to Series A). Zapier
  graduated on the 2021 secondary at $5B (rule 7: a $1B+ row cannot be a no): decided, not asked. lead4: visor
  acquired (Usercentrics). acquire-com-fka-microacquire set not_graduated by the lead (two judges disagreed).
- d1, d2 DONE (87 new rows classified; voyant-technologies not_member R6). Merges now 56 (added microacquire,
  natpal -> yodle, scratch -> helloshopper, tsm -> team-solomid-tsm, e-steel -> newview-technologies, optigrab-com ->
  endeca, informationview-solutions -> vibrant-solutions). d3 still running.
- wikifetch redirect traps (do not cite W()): Circline, Trellix_Corporation, Pacific_Microsonics, Harmoni, Cyota,
  CloudLock, Convertro, Flarion, Habana_Labs, Kandou, Kroll_Bond_Rating_Agency.
- 17:10: FINAL REBUILD DONE (build-2.log): 950 rows, all members; no renames. lead5/lead6 closed the last needs
  (earthly, synergy-computer-graphics not_graduated; m4-financial, utmost-technologies country inferred; flags
  stage_uncited on capsule8, plenful, abacus; cite_pending docusign; domain, fg-wireless S2A undetermined).
  names.published (31) in config. Profile chain re-run (write-profile.py now counts search-verified links: 48/58).
  review.html served and checked (950 rows flat, profile panel expands). verify-1.txt: only 22 cross-investor
  problems. cx3 (final cross triage, 110 loose pairs, all columns) RUNNING -> cross-plan-cx3.json.
- Blind 5% sample (48 rows, scratchpad/blind/blind-answers.json): band 0 disagreements, status 3, country 1, city 9,
  stage 6. Class found (duty 9): my second-pass brief let "first institutional round" read Series A, a convention
  COLLECTION.md s6 retired (Erik 2026-09-19). Swept: 36 stages reverted to undetermined by the lead (30 Series A,
  good-technology Seed, 5 Growth on "second round" / turn-around / unnamed). zany-brainy -> acquired (asset sale out
  of Chapter 11) still to record; city differences to settle (rosebud, pipedrive, datahub, travcorps, inrisk, aivar).
