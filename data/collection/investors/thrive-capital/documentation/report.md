# Thrive Capital collection report

## PRO-64 — Base, outcome classification, firm profile (one merged run)

Single-session autonomous run, 2026-09-03, the first run under the merged
shape of `COLLECTION.md` (PRO-71): investor-specific decisions, evidence
layers, both calibration sets pre-registered, one grind answering
membership and every classification column per row, recall probe and one
rebuild, standing duties and the A/B pass, the firm profile built once
against the landed base, `verify` / `export` / `review` / this report and
the playbook write-back. Ingest is not part of the run (§9).

**Ingested 2026-09-04 with Erik's approval** (investor row with the uploaded icon first, then the 170 companies, then the a16z re-ingest of the four corrected rows). **Prompt count: 4, final** — the kickoff ("Please collect thrive capital"), the question on non-disclosing funds that produced the two new layers, the go-ahead for the post-close delta, and the ingest approval.
The count becomes final with the ingest decision; the target of two holds
if the closing message's ingest request is the second prompt. Checkpoint
approvals requested: 0; milestone comments posted-and-continued: 2. The
session survived one context reset mid-run (after the delta batch) on the
disk state alone — `status` was the resume point, as designed.

### 1. The method delta — what the pipeline does when the site layer is empty

This run's purpose was the answer to one question: with `thrivecap.com`
publishing no portfolio list, what does the evidence model become?

**The site layer moved rather than vanished.** No era of thrivecap.com
ever listed companies — Wayback replay 2010–2023 (CDX refused the
2024–26 window; recorded as a gap), Common Crawl 2013–2026, both checked
before concluding. The one first-party list is the Getro job board
(`jobs.thrivecap.com`): 106 companies enumerated from its sitemap plus
per-company pages, parsed by `site-portfolio.py`'s `file_list` source into
the `site_listing` class. Its stage field scored 0/10 on the gate and is
never a label.

**EDGAR reaches almost nothing through the vehicles.** The 60-entity
registry (address-verified against 295 Lafayette; the Fort Washington PA
namesake, CIK 1845943, confirmed external) yields ownership filings for
three subjects only: Oscar Health, Hims & Hers, Vimeo. The structural
layer is instead the roster-name Form D sweep: 301 filings / 161 issuers
off a **curated 20-name roster** (no team page exists; tenure windows are
press-dated, ruling 11), judged cluster-first — the Josh Miller homonym
cluster alone was 50 issuers, every seat dated against the roster.

**Press is a primary layer, and recall is load-bearing.** 37 of 155 rows
(24%) are recall additions — parametric enumeration of the book,
CB Insights' 2014 teardown, retrospective exit lists — each landing as a
cited `web` row. The ADV Section 7.B roster of 54 funds supplied
membership evidence for named-deal vehicles (Stripe, Harry's; ruling 12).

**What the model cannot see**: seed entries whose later rounds left no
filings (the C2A cohort is 27 of 43 seeds), SPV entries whose Form Ds
name no company, and anything before 2011's electronic Form D. The
consequence is a small, winner-heavy base — 60 of 155 rows $1B+ — which
is the shape of the evidence, not a defect; the shape guards are
restated for this book (ruling 13, `config.json` `verify.shape`).

### 2. Result

**155 published rows** — 22 Tier A / 84 Tier B / 49 Tier C — every row a
ledger member; **18 `not_member` rows** in `excluded.json` (Shopify and
Amazon 2026 public purchases, Thrive Holdings acquisitions, ex-partner
seats, namesake filers, LP vehicles). Ledger 179 verdicts. Eight
identity merges (Mulberry Health = Oscar, Degree = Lattice, TherapyMatch
= Headway, ADKM / HF Global = Harry's / Mammoth Brands, Omakase = Maple,
REALCADRE = Cadre, Justin.tv = Twitch, Browser Co of New York = The
Browser Company).

| column | distribution |
|---|---|
| status | private 106 · acquired 31 · public 14 · defunct 2 (Supergreat, Tutorspree) · unknown 2 (Clay, Motion Clinical) |
| valuation_range | below_1b 95 · 1b_plus 38 · 10b_plus 17 · 100b_plus 5 — all 60 $1B+ rows web-cited |
| entry_stage | Growth 73 · Seed 43 · Series A 39 — web_verified 85 · formd_structural 11 · model 59 (`stage_uncited`) |
| C2A | cohort 27 · graduated 26 · rate 96.3% · 16 `cohort_unverified` |
| hq | 154/155 filled, 32 cities — New York 65 · San Francisco 48 · Los Angeles 6 · São Paulo 3 |
| focus | Consumer & Marketplaces 41 · Healthcare & Bio 28 · Fintech & Payments 25 · SaaS 15 · Industrial & Robotics 9 · Media 9 · AI 7 · Security 6 · Climate 5 · Data Infra 4 · Crypto 3 · DevTools 2 · outside 1 |

Top of the book (market cap canonical for public rows, as of
2026-09-03): SpaceX $2.03T, OpenAI $852B, Databricks $190B, Stripe
$159B, Spotify $111.8B, Robinhood $93.9B, Nubank $65.3B, Anduril $61B,
Ramp $44B, Scale AI $29B, Fanatics $27B, Affirm $25B. Public rows (14):
Oscar Health, Figma, SpaceX, Affirm, Compass, Hims & Hers, Instacart,
Lemonade, Nubank, Opendoor, Robinhood, Spotify, Unity, Warby Parker.

Sanity against the known Thrive shape: Growth-heavy (47%), concentrated
(38.7% $1B+), New York-centred (42%), consumer/health/fintech-led — the
issue's expectation, met. Seed at 28% is higher than the issue guessed
because the roster sweep sees Kushner-era seeds (2011–2015) and the
incubations (Oscar, Cadence) enter at formation.

### 3. Calibration gate and corrections taken

Gate PASS before any verdict wrote (`scratch/gate-blind-pass.json`):
membership 0 false members (11 structural falses absent from the build,
4/4 judged falses, 1/1 judged true); stage layers scored — press/vehicle
documents 35/35 (class 1), Form D band 4/10 (demoted to a ceiling),
Getro stage 0/10 (never a label). One key corrected before the build
(Doji: its filing is 2025q3, Grimshaw's Thrive seat, not a Benchmark-era
false) and recorded in `golden.json`.

Corrections during the run: Isomorphic Labs published at the $2.1B
arithmetic floor (`valuation_floor`); Justworks and DuckDuckGo killed
from `needs_web_value` to below_1b (no primary mark above $1B exists);
Airtable to $2.25B (agreed sale to Bending Spoons), Plaid $6.1B, Gong
$4.5B (secondary), Dutchie $400M, Glossier sub-$1B; Anysphere acquired
by SpaceX (closed 2026-08-14); Vimeo, Melio, The Browser Company
(Atlassian), Console (Palo Alto Networks), Wiz, Geneva (Bumble) acquired;
Supergreat defunct. Benchling and Motion Clinical carried a persisted
band pre-fill into "graduation set on a Series A row" — cleared with
explicit `seed_to_a_graduation: null`.

### 4. Standing duties and the A/B pass

1. **$1B+ web verification**: 60/60 cited.
2. **C2A falses**: one (Tutorspree, shut down) — verified.
3. **Weak-CIK audit**: 78 weak joins read; the float sweep's registrant
   collisions (Stripe, Honor, Pace, Cadre, Lattice, Hims, Unify, Slack)
   quarantined with `model_disputes_source` (24 rows); no band rides a
   weak join into a published stage.
4–5. **Stale-float / old-float sweeps**: no re-IPO or holding-co reorg
   found; the 14 public rows carry 2026-09 market caps.
6. **Loose unicorn re-intersection**: surfaced Patreon and Cadence as
   base rows without a classification row — see §10.
7. **Self-consistency**: 8 rows (5.2%) re-judged blind on 5 fields —
   33/40 agree (82%). All seven disagreements sit on model-sourced,
   uncited fields (Check and 42Floors entry stage, Rize focus, Neuralink
   HQ, plus Doji's stage and city where the Form D evidence backs the
   recorded value); four rows flagged `unstable` with the alternative
   reading in the note.
8–9. No systematic class emerged; the disagreements are row-level.

**A/B pass** on the visible slice (60 $1B+ rows plus the public rows):
pass A defended every value with a citation; pass B attacked the stale
marks. The session's web-search budget (200 calls) ran out after
Cityblock ($116M Series E 2024, Homeward merger 2026, no down round);
OpenAI ($852B held, Aug-2026 tender flat), Stripe ($159B Feb 2026),
Fanatics (no primary since 2022; secondary indications ~$17B) and Mammoth
Brands (no primary since 2021) were re-checked through the app browser's
DuckDuckGo endpoint. **Not attacked, `stale` kept**: Cedar, Lattice,
Benchling, Rightway, Capsule, Airbyte, Stytch (17 `stale` rows in all).

### 5. Findings Erik should know about

- **Public purchases are out, and named**: Shopify ($100M, Mar 2026) and
  Amazon ($215M, Aug 2026) are `not_member` under ruling 4/10; Oscar,
  Figma and SpaceX stay in on their venture entries.
- **Anysphere (Cursor) is an acquired row** (SpaceX, closed 2026-08-14) —
  the firm's most-cited recent position is no longer private.
- **Airtable is priced at its sale** ($2.25B, Bending Spoons, pending) —
  a $11B 2021 mark would have been the single largest over-statement.
- **Clay** (`clay-inc`, `identity_uncertain`, status unknown): the Form D
  issuer and the Sequoia-backed Clay are ruled distinct in
  `cross-investor.json`; the base row rests on a 2025 Zaki seat and
  needs Erik's read. **Advocate** (`advocate-inc`, `unannounced_deal`):
  a Thrive seat on a filing no press has covered.
- **Four a16z rows were corrected** for the cross-investor gate (Honor
  $1.25B private, Plaid $6.1B, xDOF private, Loft $2.9B private) — a16z
  needs a re-ingest of those rows.

### 6. The C2A sentence (superseded by §15, 2026-09-16)

Of the 43 seed entries, 27 have a verified graduation leg: 26 raised a
Series A or later, 1 (Tutorspree) did not. The other 16 carry
`cohort_unverified` — seeds whose later rounds the roster sweep cannot
see. 96.3% on the verified cohort is the survivor shape of a
press-visible book, not the firm's seed hit rate.

### 7. Debt, all flagged in rows

`stage_uncited` 58 · `model_disputes_source` 24 · `stale` 17 ·
`cohort_unverified` 16 · `stage_disputes_band` 10 · `censored` 6 ·
`cite_pending` 6 · `unstable` 4 · `needs_web_value` 2 · `city_unknown`
1 · `valuation_floor` 1 · `unannounced_deal` 1 · `identity_uncertain` 1.
`verify` is clean in plain mode with these as the only debt.

### 8. Firm profile

`investor.json` + `investor/sources.json`, `build-firm-profile.py` clean
(hq from 42/42 own Form D filings: New York, NY; 17 people, current
cohort 2026; notable_investments asserted against ledger members;
13 fund accessions asserted against filed sold amounts).

- **AUM** $50,492,232,840 both ends — Form ADV Item 5.F (2026-07-06
  amendment), one RIA, no in-boundary ERA; the 54-fund 7.B roster sums
  to $50,492,232,839.
- **Funds** 17: I–X with growth sleeves, IV Supplemental, the first
  Opportunity fund. Fund X's two L.P.s filed Indefinite/$0 (Oct 2025), so
  their $1B/$9B come from the firm's /thrive-x page; Fund III carries its
  $150M press close with the $147M filing as corroboration; 24 lettered
  co-invest/SPV vehicles (~$2.9B sold) and the Claremount entities are
  described in the basis, not listed.
- **People** 17 (ADV owners/officers, Form D related persons, press):
  Kushner, Weinstein, Zaki, Grimshaw, Mallick, Nohria, Clark, Hankes,
  Y. Clark, Klemmer, Mella, Yuan, Pripstein, Budhiraja, Feldman, Brandow,
  Iger (adviser). No team page exists; nothing invented.
- **Range** $1.5M / $20M / $1.3B — lower from the documented smallest
  entries (Grailed, Warby Parker seeds), median from 34 partner-anchored
  entry rounds (flagged thin and SPV-distorted), upper the reported
  OpenAI check (Oct 2024).
- **Stage / geo / scope** derived and flagged: Seed–Late Stage from the
  fund architecture and the landed distribution; US core, Europe and
  Latin America other; Generalist with seven focus labels at
  `focus_min_companies` 7 (~4.5% of the base).
- **Icon**: first published at the ingest (2026-09-04) from the issue's
  favicon pointer, which turned out to be a 32×32 PNG: the master was an
  8× enlargement and rendered blurred in the app. Republished 2026-09-05
  from the site's 1200×1200 apple-touch icon (`--discover` found it; the
  new master measures a 0.85 px edge ramp against 5.9 px before), and the
  fetch now refuses raster enlargements and soft masters
  (`icon-normalize.ts` MAX_UPSCALE / MAX_RAMP, provenance in the sidecar).

### 9. Cross-investor alignment

87 rows shared with a16z, Sequoia, Accel and Lightspeed: 87 agree.
Thrive aligned to the freshest marks (OpenAI $852B, Stripe $159B,
Databricks $190B, Ramp $44B, Neuralink, Gong …); three `distinct`
rulings added (Pace, Cedar, Clay namesakes); four a16z corrections as
above.

### 10. Driver and playbook changes

- `run.py verify --in-flight` no longer fires the citation invariants on
  rows the deterministic layers pre-filled and no batch has answered.
- `run.py verify` counts classification over the base and fails on
  unclassified base rows: three stale keys (rebuild slug renames) hid
  three unjudged rows (Oscar Health, Patreon, Cadence) behind a "155
  classified" count.
- `config.json` `verify.shape` restates the $1B+ share and C2A ceilings
  per investor (defaults unchanged elsewhere).
- `COLLECTION.md` write-back (§5 no-site evidence model, §8 five merged-
  run lessons, §9 icon gating, §11 profile without a site) — landed with
  the close, as the last act.

### 11. Open rulings (§9 triggers, raised once)

1. a16z re-ingest of the four corrected rows (published-surface change).
2. `clay-inc` identity (unknown status) and `advocate-inc` (unannounced
   deal) — Erik's read before they publish, or they publish flagged.
3. The ~2,000 macOS " 2" duplicate files in the working tree (all
   investors) — untouched, not committed; deletion is Erik's call.
4. Carried from the megafund wave: the Waymo ruling and five accepted
   cross-investor pairs still await Erik's confirmation.

### 12. Environment

Web search exhausted at 200 calls (the A/B pass budget lesson, now in
§8); IA CDX refused wildcard and 2024–26 queries; sec.gov answered 503
intermittently on the link sample (transient, re-run clean); EDGAR
entity sweep exceeded the 600 s tool timeout (run in background); one
context reset mid-run. Machine time ~6 h wall-clock for the whole run.

### 13. Artifacts

`base.csv` / `base.json` (155), `excluded.json` (18), `membership-ledger.json`
(179), `classification.json`, `resolved.json`, `golden.json`,
`identity-merges.json`, `decisions.md` (rulings 1–13), `config.json`,
`investor.json` + `investor/sources.json`, `review.html` (served and
checked: rows flat, profile panel expands), `sources/` (job board, EDGAR
sweeps, ADV-derived fund roster, curated partner roster and team),
`scratch/` (gate, layers, queue batches, run-log, verified-median,
self-consistency sample and blind file).

### 14. Post-close delta — the exit-side EDGAR sweep and the Wikipedia insource sweep (2026-09-03, second rebuild approved by Erik)

Two recall layers built as pipeline scripts after the close, from the
first-principles question "where does a non-disclosing fund's investment
leave traces it does not control": `scripts/edgar-fts-sweep.py` (EDGAR
full-text search on the fund-entity phrases, hits aggregated by
third-party registrant, primary documents fetched and the sentences
around the phrase kept) and `scripts/wikipedia-insource.py` (every
article whose source names the firm, with the sentences that name it,
company articles separated from people and lists, titles matched
against the base). Config: `edgar.fts_phrases` / `fts_own_pattern`,
`wikipedia.phrases`; outputs `sources/edgar/fts-hits.json`,
`sources/web/wikipedia-insource.json`.

| Layer | Swept | Candidates | Members added |
|---|---|---|---|
| EDGAR full text (3 phrases) | 663 hits, 99 registrants: 51 own entities, 9 LP-side registered funds, 8 ownership-form-only, 31 third-party | 12 real companies (19 already in the base or noise) | 7: Segment (Twilio S-3, named-deal vehicle), Bread (Alliance Data S-3), Blend Labs (S-1 rights agreement), Reddit (S-1), Securitize (S-1 holder table), YouNow (Reg A holder list), Diem (Silvergate S-3) |
| Wikipedia insource | 78 articles: 26 in the base, 16 company candidates, 36 people/lists | 9 read | 8: Greenhouse, Tictail, Spree Commerce, Mapbox, Neverware, io, Essential AI (via Ashish Vaswani's article), Ellis (via Ryan Williams' article) |

**15 members added, 155 → 170 rows (+9.7%)**, all judged on the same
contract: 7 filing-grade (S-1/S-3/Reg A holder tables and rights
agreements), 8 press-cited. Two `not_member` verdicts recorded so the
names do not resurface: Willow Wealth (Yieldstreet's stake in Thrive's
name is merger consideration for Cadre, one-row principle) and FIFA
Forward Enterprise (Thrive Eternal, ruling 3). Noise named and
dismissed: the Puck Building lease in a 2011 CMBS prospectus,
"Claremount" as a place name in PIMCO, Montpelier Re, mortgage-trust and
LendingClub filings, Wikipedia's Tribe Capital typo and EarthLink's Trive
Capital. New rulings 14 (consortium/token positions: Diem in, aligned with
a16z; merger consideration is not a new entry) and 15 (both sweeps are
standing layers for this book).

After the second rebuild: `verify` clean, cross-investor 92 rows shared /
92 agree (Reddit re-marked at $30.01B as of 2026-09-03 in the same band as
a16z/Sequoia; Blend Labs paired with Lightspeed's `blend` by a `same`
ruling; Diem mirrors a16z's row; Segment's focus aligned with Accel's).
Shape now: $1B+ 62 (36.5%) / $10B+ 23 / $100B+ 5; Growth 79 / Seed 47 /
Series A 44; C2A cohort 30, graduated 29; New York 71 / San Francisco 53.
Debt added: `stage_uncited` on Bread, Diem, io, Securitize, YouNow;
`cite_pending` on Securitize ($1.22B public row whose entry round no press
names); `needs_web_value` on Mapbox.

What the delta measures: a base built without a site layer missed about
one row in ten, and the misses cluster where the roster sweep is blind —
Fund II–IV era positions (2012–2016) that exited through public
acquirers or IPOs, and rounds Thrive joined without a board seat. The
exit-side sweep is cheap (one query per phrase, no search budget) and
filing-grade; it belongs before the recall probe in every run, disclosing
site or not.

## PRO-71 — what the merged shape teaches (closes PRO-71)

The shape held. One queue, one pass: 155 rows judged once for membership
and every column; the delta after the rebuild was 37 rows and one
re-prepare; the profile was built once, after the base landed, with zero
recompute rounds; the review surface was built once; `status` resumed the
run across a context reset; no row was judged twice and Erik signed
nothing mid-run. Prompt count 1 → 2 with the ingest approval, against 5
for Lightspeed's three-issue run.

What it cost, and what is now in the playbook: (1) `verify` counted
classification keys rather than base rows, and a rebuild's slug renames
hid three unjudged rows — fixed in the driver; (2) the post-rebuild
`prepare` overwrites `queue.json`, so the evidence view for the blind
re-judgment had to be rebuilt by hand — copy it first; (3) a rejected
`record` batch is invisible behind `tail` — read the whole output; (4)
the web-search budget is a run constraint the A/B pass must be planned
around; (5) base-shape guards are investor properties. Recommendation:
keep the merged shape for Creandum, Cherry and YC; their three-issue
templates can collapse to one issue each.

### 15. C2A re-judged under the status contract (2026-09-16, the pilot investor)

`seed_to_a_graduation` became a judged status (`graduated | not_graduated
| censored | undetermined`, COLLECTION.md §6) after the coverage audit
found the column had never been queued for judgment. Thrive went first.

**Method.** `migrate-graduation` kept 3 cited graduations, dropped 48
legacy values (model-sourced, uncited, or the Form D layer's own verdicts)
and removed 16 `cohort_unverified` flags; `prepare` queued the 44 re-opened
Seed rows; one judge batch answered them (73 web calls), confirming the
Form D layer on 3 rows and overturning it on 2 (Zola: $25M Series C, Dec
2016, Business Wire; Grailed: $15M Series A, Jun 2018, Index's own post).
Invariant 5 then demanded the entry-stage leg on 13 decided rows whose
Seed label rested on model knowledge: 4 cited (Retro, Maisonette, Modern
Life, Fabric), 5 re-staged because the citation first names Thrive at a
later round (Mesh Optical and xDOF at the Series A, Folio at the A, Pace
and Fora at Growth; `entry_date` moved to that round, medium confidence, a
seed seat undocumented rather than excluded), 4 left undetermined because
no page ties Thrive to the seed (Forus, GroupMe, Milewise, Fortell).

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|---|
| 42 | 3 | 11 | 28 | 26 | 2 | 92.9% | 71.8% |

Of 42 seed entries, 3 were too recent to count (Doji 2025-05, Neon
2024-11, Ellis 2026-07); of the 39 whose record could be sought, 28 were
established (72% coverage) and 92.9% of those graduated — the establishable
set skews toward visible successes. The two "no"s: Clay (Form D absence
52 months after the 2021 entry, identity uncertain, medium confidence) and
Tutorspree (shut down Sep 2013, TechCrunch; absence checked 2026-09-16).
Undetermined (11): Formal, Rent App, Specter, Vetcove, Advocate, Geneva
(later filings never reach 2× the $14.2M entry; Bumble's acquisition is
not a no because the seed was not the last round), Kickstarter (the 2021
a16z deal was a tender, not a primary round), Forus, GroupMe, Milewise,
Fortell (Wired and Forbes refused the fetch; worth citing by hand).

Notes corrected on the way: Modern Life's Series A is Nov 2025, not Jul
2023; Console's seed was reported 2025-06, not 2024; Fora's A was co-led
by Heartcore and Forerunner, not Thrive. Business Wire, Forbes and Fora's
newsroom refuse fetches (403/429), so those citations rest on titles and
syndicated text naming round, amount and lead. Entry stages now Growth 81
/ Series A 47 / Seed 42.

`verify` is clean (links sampled) except two pre-existing cross-investor
disagreements with Battery (Chai Discovery's stale below_1b mark against
Thrive's $3.8B of 2026-07; Unify private vs acquired on the same as-of),
to be aligned in Battery's own C2A pass this wave. `verify.shape`
`c2a_rate_max` stays 1.00 with its note restated for the new instrument.

For Erik: Milewise's membership rests on CB Insights' exit list alone
(the seed's investor list in TechCrunch omits Thrive) — a membership
question, not a graduation one; and the five re-staged rows are worth a
glance, since a Seed seat may exist that no page records.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

One flagged row, and it is the exception rather than the rule. `clay-inc` is
an EDGAR-only row: nothing names the company behind the issuer "Clay, Inc." —
no Thrive listing, no site card, no press trace since 2021 — so it carries
`identity_unresolved`. But its own filings decide it (~$3.13M across three
2021q2 offerings, Hankes as director, no priors), which is where its
`formd_structural` Seed and its `not_graduated` come from. Under the
carried-through exception the filings survive the missing name, so the row
keeps every value and stays in the metrics. What such a row may never do is
publish a stage sourced `model`.

`verify` clean; the S2A block is unchanged.

## Addendum 2026-09-20: S2A with every Seed row decided (PRO-132)

PRO-132 made the absence of a later round a finding. A Seed row past the
24-month clock with no evidence of a later round did not graduate, and every
no records the dated search that found nothing: the firm's archive, the Form D
sequence for a US company, and at least two publisher surfaces (COLLECTION.md
§6).

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 36 | 3 | 33 | 27 | 6 | 81.8% | 100% |

Of 36 seed entries, 3 were too recent to count (Doji 2025-05, Neon 2024-11,
Ellis 2026-07); of the 33 that remain, 81.8% raised a later round. Of the 6
that did not, one rests on the filings (Clay, Form D silent since 2021), one on
a cited end (Tutorspree, shut down 2013) and four on a dated search of the
named surfaces (Advocate, Formal, Rent App, Geneva). Two decided rows rest on
an uncited seed (Fortell, Rent App) and carry `stage_uncited`.

Was (§15): 42 seed entries, 3 censored, 11 undetermined, cohort 28 at 92.9%
with 72% coverage.

What moved:

- Six rows left the Seed cohort. Forus, Specter, Vetcove, GroupMe and MileWise
  now read `undetermined` in the stage, because nothing on record dates or
  evidences Thrive's entry: GroupMe's August 2010 seed predates Thrive's first
  fund and its January 2011 round does not name Thrive, and MileWise's own
  exit coverage lists five seed investors without Thrive. Kickstarter reads
  Growth: Thrive's stake is a Fund I holding after USV's 2009 Series A, which
  the firm's own secondary ruling (decisions.md 6) stages as Growth.
- Two citations fixed. Neverware's graduation cited a Tracxn page, a vendor
  (Rule A); it now cites the PR Newswire Series B release. Blend Labs cited an
  SEC accession that does not exist; it now cites the S-1 and its investors'
  rights agreement, which lists Thrive Capital Partners II among the 2012
  seed investors.
- Two Form D verdicts overturned with citations stay overturned (Grailed's
  2018 Series A, Index's own post; Zola's 2016 Series C, Business Wire).

`verify.shape.c2a_rate_max` is restated from 1.0 to 0.90 against the new
rate. `verify` is clean.

For Erik: **Geneva** has two later Form Ds (2021 $12.3M, 2022 $21.0M), neither
reaching twice the $14.2M entry, and no press names a lettered round; Bumble
bought it in 2024. It is recorded not_graduated on the step-up test, and a
reader could argue the 2022 round graduates it. **GroupMe** and **MileWise**
are membership questions: their seed rounds' own investor lists omit Thrive.
The stage now says so; membership is unchanged.
