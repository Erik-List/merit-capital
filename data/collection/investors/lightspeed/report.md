# Lightspeed collection report

## PRO-63 — Company Base

Single-session autonomous run, 2026-09-02, parallel with PRO-69 in the
same directory under the §11 ownership split (agreed session-to-session
after a first-hour collision on config.json — both sessions kicked off
within minutes of each other; the split held from there, intel flowing
both ways). Scope: the membership-verified Company Base. Classification
columns are PRO-66, which continues on this base after Erik's sample
sign-off; the review surface shows the deterministic pre-fills (SEC
float, Wikidata, unicorn list) with their flags, judged by no one yet.

**Prompt count: 2, final** — (1) the kickoff ("please execute
lightspeed base collection"), (2) the sample sign-off carrying the
classification go-ahead. Checkpoint approvals requested: 0; checkpoint
statuses posted-and-continued: 2. **Erik sampled the review with zero
corrections; sign-off recorded 2026-09-03; PRO-63 marked Done.** The
COLLECTION.md write-back landed with the close commit.

### 1. Result

**931 published rows** — 627 Tier A / 294 Tier B / 10 Tier C — every
row an affirmed **member** (0 uncertain), plus **333 not_member rows**
and 1 other_desk row preserved in `excluded.csv`. Ledger: 1,288
verdicts (orphaned keys from merge canonicalization expected). By
author: 968 evidence-class seeds surviving as-is, ~320 judge verdicts
(gate fixes, the LSIP book, the China sweep, the 273-row Tier C grind,
recall). 24 identity-merge groups applied.

Evidence coverage: 600 rows on the firm's own current card list (569
`lsvp` + 31 `both`), 1,057 distinct capture-layer slugs 2001–2026
(lightspeedvp.com listing eras 2001–2011, lsvp.com eras 2012–2026,
Common Crawl per-company pages), 233-person roster with tenure windows,
1,395 partner-matched Form D accessions across 796 issuers, 27
companies with fund ownership streams, 381 issuer round histories.

### 2. The load-bearing boundary (ruling 2) — measured

The site's own `data-investor` attribute (lsvp/lsip/both) is the
listing-level attribution, but it is NEWER than the January-2026
archive snapshot: archived 2023–2026 /companies/ captures render LSIP
rows with lsvp.com links, so **61 of the 65 lsip-only slugs built base
rows through captures alone** (standing ruling 10, written at the
gate). Resolution: 53 clean LSIP-era rows excluded class-wide on the
site's own current attribution; 8 judged individually — Indian Energy
Exchange stays IN (2010 entry, Rs 35 Cr for ~10%, written from the
global funds five years before LSIP's first dedicated fund; the site's
own treatment of siblings ItzCash and OYO agrees), Darwinbox,
Innovaccer, Supabase, Solana, Priority Vendor, Property Share and
Triomics stay OUT (LSIP-era entries, LSIP memos or LSIP-partner
seats — Triomics' Form D names Dev Khare, LSIP's own managing
partner). The 20-person LSIP roster (`?firm=lsip` server-side filter)
is preserved as a judge instrument in `sources/site/lsip-people.json`.

### 3. The China boundary (rulings 3 + 9)

Lightspeed ran China from the global funds 2006–2011 (the Shanghai
office) before Lightspeed China Partners spun out; the shared-brand
site kept listing China rows for years (LCP's own PPDai memo lives on
lsvp.com's blog). Standing ruling 9: the money at entry decides.
Global-era entries stay (99Bill, MediaV, G-Media, IHaveU — still on
the current card list —, Dianping, whose position survives as Meituan
equity after the 2015 merger and is merged accordingly); LCP-window
rows leave (PPDai/FinVolution — including the LCP-vehicle 13Gs the
partition caught —, Rong360, Tujia, FangDD, BTCC, Bitmain, Meilele,
eDaijia, FaceU, Coding and the unresolvable-entry tail, 19 rows in
all). Hesai stays: an LSVP-desk vehicle filed the 13G — the firm's own
money regardless of geography.

### 4. Calibration gate (checkpoint 1) — PASS 22/22

22-row key (10 true / 12 false) pre-registered and committed BEFORE the
base was built (9efb036), every answer document-anchored: the site's
own attribution attribute, Form D accessions from the local bulk zips
(a targeted pre-build related-persons sweep anchored the ex-partner
traps), or press. The first inspection surfaced four era-listing false
members (zolve, ppdai, rong360, finvolution seeded member off archived
brand-era listings) — a LAYER defect fixed as standing rulings 9+10
plus judged verdicts, then a clean re-score: **zero false members at
high confidence**. Structural falses (namesake Form D filers, the own
pooled vehicle, Faction and LSIP designed rows) verified absent from
the built base. Honesty note as Accel: one session wrote and took the
test; the key is external documents, registered pre-build.

### 5. The judge grind (273 Tier C rows, 75 clusters)

All name-match rows judged individually, cluster-first: the roster
identity resolved per person (tenure windows, prior firms, operator
histories), then rows judged against decisions.md.

**Members found in the filings (22)**, most under rename-alias legal
names now merged: Grafana Labs (Raintank — Lightspeed led the 2019
Series A), Carta (eShares — the Kohler seat corroborates the card's
own 2019 Series E entry), Cameo (Baron App), Whisper (WhisperText),
HQ Trivia (Intermedia Labs), Tome (Magical Tome — led the $43M B),
TollBit (Novoscribe), Terminal (Elastic Projects), Yellow.ai (Bitonic
Technology Labs, Bengaluru — LSVP in the $78M C), All Day Kitchens
(All Day Technologies — led the $65M C), Art of Sport (AOS Group),
Orca Bio (Orca Biosystems — led the $192M D), DualBird (Israel — led
seed+A), Composio (Sampark), LivingSocial (Hungry Machine), Fusion-io
(Fusion Multisystems), plus standalone rows NS8 (led the $123M June-
2020 round; collapsed in fraud that September — a member with a
defunct outcome), Heighten (two in-tenure partner directors, 2015,
acq. LinkedIn — unannounced), Zocks (led the 2024 A), AWA, Pie Tech
(led the June-2026 A), Arena Club, and fal.ai at medium confidence
under the a16z Director-pattern (seat on the 2025 filings, rounds led
by others — flagged for the A/B pass, as is TollBit's round).

**Exclusion classes recorded (251)**: the mega-homonym complexes
("Mark Anderson" 34 rows, "John Thompson" 32 — the real John W.
Thompson is a Lightspeed VOP whose Microsoft/Illumio/KoBold seats are
personal, "Paul Murphy" 28 incl. Toronto gold miners and his own
founder-era Dots, "Adam Smith" incl. Xobni's founder, "David Chen",
"Brian Kelly", the Pauline Murphy complex); operator-VOP pre-tenure
paper (Roxanne Oulman's Human Interest/Medallia CFO jobs, Paul Ricci's
Nuance chairmanship, John Borgerding's WorkForce Software); prior-firm
seats caught live (Twohig's Insight-era Udemy, Taussig's Highland-era
Jaunt, Kohler's Prism VentureWorks five, Alcorn's Zetta trio, Bucky
Moore's Kleiner pair, Dev Khare's Venrock-era Appia/Lavante);
ex-partner next-firm deals (Vrionis's Unusual-era Arrikto/Rasgo/Rime,
Caldbeck's pre-tenure Bain-era Oyster); guest-author roster artifacts
(BuzzFeed via its own president, Securrency via WisdomTree's CEO);
LSIP-partner seats (OkCredit's $67M paper as OkTech); documented
syndicates without Lightspeed (Dataiku, MobileIron, Wearable
Intelligence, Rhumbix — each cited); and the identity-unresolved tail
ruled out under Erik's a16z narrowing (67 Ventures, Good Game, Elliot,
Interlace, Livday, Omni Science, R2 Air, Somo — each flagged to
recall if identification ever lands).

### 6. Recall probe

Pre-registered parametric enumeration (committed before the build),
the ruling-6 continuation-vehicle position list, the fund vehicles' 13G
subjects (in by construction), press sweeps, and the site diff.
**Three recall additions, each cited**: OpenAI (ruling 6: its position
is the firm's own reported continuation-fund asset), Reflection AI
(co-led the $105M A and the $2B Oct-2025 round; the current card
renders it "Reflection" and the merge folded them), Discovered
Materials (led the $9M 2026 seed, not yet on the site snapshot).
Rejections recorded with reasons: Netlify, Together AI, Baseten, Alto
Pharmacy (documented syndicates without Lightspeed), SuperLiving
(LSIP's book). Two probe candidates resolved as already-present:
Databricks (the firm's own card lists it) and LivingSocial. The site
layer carries recall, as measured on Sequoia/a16z/Accel — the probe's
catches were the not-yet-listed (announced weeks ago) and the
never-listed (continuation positions) classes.

### 7. Environment and coordination

- IA in partial recovery all session (CDX intermittently refusing;
  replay reliable): the lsvp-era year snapshots were fetched via
  replay redirects into wayback-pull's own raw/parsed shapes; the
  Common Crawl layer (run by the PRO-69 session) covers 2013–2017 +
  2023–2026 per-company pages; `wayback-pull.py` now MERGES per-year
  parsed files so the two capture universes survive each other's
  re-runs.
- lsvp.com was a parked domain until ~2011; the 2000–2012 site lived
  on lightspeedvp.com (per-era cdx_domain override added to
  wayback-pull for exactly this).
- Registry judgments for sampling: LS SPV Management, LLC and Venture
  Investors General Partner LLC (2006!) both file Forms 3/4 from 2200
  Sand Hill Road — re-desked from external to us/confirmed; the 2006
  GP entity carries pre-2012 board-seat evidence the roster window
  misses.
- PRO-69 intel used: the 112-filing Lightspeed*/Faction* Form D
  enumeration (trap-key anchors, namesake inventory incl. Lightspeed
  Microscopy/Coin Ex/Lane and Faction Brewing/Entertainment), the
  2026q3 filing list, cc outputs. Sent back: roster, sweep, boundary
  sidecars, ledger-coverage pings.

### 8. Limitations and open debts

- **Roster tenure coverage starts 2012** (the /team/ era; CC starts
  2013): 2000–2011 partners (Cogan, Showalter, early era) are not
  sweep targets. Mitigations: the firm's own 2001–2011 listings carry
  that era's recall; Venture Investors GP's filings carry 2006+ seats;
  Form D data starts 2008 anyway. Residual exposure: 2008–2012 deals
  never on any list with only a departed-partner Form D trail.
- **The SPV-initials blind spot**: the LSVP SPV/holdco trail (HS, ST 2,
  INF, NH, SU, C, R, M2, W-I, Platinum, Luminous, Velocity, Ascent,
  AI Renaissance) names positions only by initials; pooled Form Ds
  disclose no subjects. Positions held ONLY through unidentified SPVs
  are invisible to every layer. Ruling 7 bounds the damage (post-RIA
  public/secondary-only purchases are out anyway).
- Local Form D zips end 2026q2; 2026q3 filings ride the peer's
  formd-2026q3-recent.json only.
- 2013–2018 lsvp.com listing pages were barely archived (per-company
  WP site); CC's per-company pages carry those years instead; 2018
  removals inside that window could hide.
- The May-2012 ASP and Oct-2012 WP site snapshots share the 2012
  parsed year; era attribution within 2012 rides the row's path.
- `run.py status` shows 0/21 batches recorded: the queue is shared
  with PRO-66's classification needs; the membership slice is complete
  (1,288 verdicts, 0 uncertain), the classification slice untouched by
  design.

### 9. Checkpoint 2 (this report)

The membership-verified base is ready for Erik's sampling:
`review.html` (verified rendered and served — 931 flat rows, Sample
chip = 91 stratified rows incl. every recall addition, every
director-pattern member, the LSIP/China boundary keeps, and every
$10B+ pre-fill), `base.csv` (931 rows, classification columns carrying
only flagged deterministic pre-fills pending PRO-66), `excluded.csv`
(334, preserved), `golden.json` (pre-registered key + 22/22 pass),
`base-verification.json` (1,288 verdicts + 3 recall additions + 7
recorded rejections). `verify --base-only` is **clean**. Corrections
in chat are recorded class-wide as `who: "erik"` ledger verdicts.
Ingestion stays gated on Erik's explicit approval (COLLECTION.md §9);
PRO-66 is unblocked on sign-off.

### 10. Artifacts

| File | What |
|---|---|
| `base.json` / `base.csv` | Evidence layer / merged surface (931 rows) |
| `base-verification.json` | 1,288 verdicts, 3 recall additions, 7 rejections |
| `identity-merges.json` | 25 merge groups |
| `excluded.csv` | 334 rows, preserved (333 not_member, 1 other_desk) |
| `golden.json` | 22-row membership trap set, pre-registered (9efb036) |
| `decisions.md` | 10 rulings (8 Erik-confirmed Phase 0; 9–10 agent-standing, flagged) |
| `entities.json` | 148-entity registry (98 us / 7 china / 5 india / 5 faction / 33 external) |
| `sources/site/*` | 600-row card extraction + LSIP boundary sidecars |
| `sources/wayback/*` | 2001–2026 capture layers (IA + CC merged), 233-person roster |
| `sources/edgar/*` | Sweep (1,395 acc), companies (27), rounds (381) |
| `scratch/` | Trap key draft, gate pass, run log, merge queue, parametric list |
| `review.html` | Read-only review surface (checkpoint 2, verified served) |

## PRO-66 — Company outcome & classification

Continued in the same session on the sign-off'd base (Erik sampled PRO-63
with zero corrections, 2026-09-03). All 875 published member rows fully
classified: status, valuation (range/usd/asof/source/citation), entry
stage (+source/citation), hq_city, hq_country, focus (twelve-value
taxonomy), seed_to_a_graduation, flags, note. `verify` (full, with link
checks) exits clean; every hold is a flagged, inspectable debt.

**Prompt count: 2, final** (the PRO-63/66 shared count — kickoff +
sign-off go-ahead). Erik's classification sample sign-off and ingest
approval are the remaining gates.

### 1. Shape of the result

- **valuation_range: 756 below_1b / 86 1b_plus / 28 10b_plus / 5
  100b_plus** — 119 rows $1B+ (13.6% of the base, within the expected
  <20% band). The five $100B+: OpenAI ($852B), Stripe ($159B), xAI
  ($230B), Databricks ($190B), Anthropic ($380B).
- **entry_stage: 500 Series A / 195 Seed / 179 Growth / 1 Pre-Seed** —
  the A-weight is the firm's enterprise-first history; Growth is the
  2015+ late/at-scale entries.
- **status: 457 private / 248 acquired / 59 defunct / 34 public /
  77 unknown** — the acquired weight is the 2000s enterprise era; do
  not read a mortality rate off `defunct` (quiet shutdowns present as
  unknown, acquihires as acquired).
- focus: twelve-value taxonomy on 812 rows; 63 outside-taxonomy tail
  (heritage/thin rows). Distribution led by Consumer & Marketplaces
  (138), Data Infrastructure (118), SaaS (97), Industrial & Robotics
  (76), Fintech & Payments (69), AI & Applied AI (69).
- **C2A cohort: 102 rows, 63 graduated (61.8%)** — but see §4.

### 2. The Lightspeed advantage: first-party stage evidence, measured

Every lsvp.com company card states Stage Invested + Backed Since — the
firm's own page naming the entry round. The stage golden set (31 rows)
measured whether that field is trustworthy: **31/31 blind**, the card
mapping right on every row including the two card-vs-press tensions
(Orca Bio and Forty Seven, both resolved in the card's favor by
research during key assembly). So the card is **class-1 evidence with
the company page URL as citation**: 553 rows carry a first-party card
stage, the cheapest and highest-coverage stage column of any investor
run to date. The A/B pass then attacked the visible slice as usual, and
the card held up (one documented exception, Seismic — the 2018 round
the card calls "Series A" was Seismic's $100M Series E; disputed with
the round record).

### 3. Method

1. Generator + judgment table (`scratch/pro66_generate.py`,
   `pro66_judgment.py`, ~640 hand-authored rows): the card mapping
   (gate-validated), Form D structure as a ceiling, issuer addresses,
   priors — merged under the source gate into 16 `run.py record`
   batches. Precedence: judgment > card > formd_structural > band (as
   ceiling) > convention/prior (always flagged).
2. Web pass (5 agents, 82 visible-slice rows): every suspected-$1B+ and
   public row pinned with a current market cap / round mark + as-of +
   citation, or ruled below_1b. Then a second pass (2 agents, 45
   unicorn-list-sourced rows) re-verified the name-matched figures.
3. Weak-CIK audit: 299 rows carry a weak CIK join, but only the ones
   that produced a surviving ≥$1B figure matter — every one (Ciena,
   Snap, Zscaler, QuantumScape) went through the web pass for identity
   + current-cap confirmation; the wrong-entity floats (Aurora, Cato,
   Balance, Eve, Exa, Fathom, Paid, Arena, Teads) were quarantined with
   `model_disputes_source`.
4. City/country coherence sweep: 0 issues.

### 4. Findings Erik should know about

- **The second China sweep (a membership change after sign-off).**
  Classification surfaced 41 more Lightspeed-China-window rows that the
  base's first China sweep missed — because their earliest listing year
  is 2019+ (the archived /companies/ + /portfolio/ eras that ruling 10
  says can't assert LSVP attribution). Pinduoduo (PDD, $100B+ public),
  Full Truck Alliance, XPeng, QingCloud, BTCChina, Laiye and a tail of
  brand-era artifacts — all Lightspeed China Partners entries under
  ruling 9, now `not_member`. This is the single biggest correction of
  the classification phase; had it not run, the base would have
  published Pinduoduo as a $100B+ LSVP position it never was.
- **Card-status staleness is systematic on exits.** ~40 rows the card
  still marks "Private" or "IPO" are actually acquired, defunct, or
  re-listed — Wiz (Google closed the $32B acquisition 2026-03-11, the
  peer session's catch), Moveworks (ServiceNow, Dec 2025), Daily
  Harvest (Chobani, 2025), At-Bay (Munich Re, 2026), Normalyze
  (Proofpoint), Brigit (Upbound), DataStax (IBM), and the heritage
  acquired tail. The card's Status field is corroboration, never the
  label (deterministic-layer rule); model knowledge + the web pass
  carried the current state.
- **Unicorn-list glitches on the visible slice**, caught by the
  re-verification pass: Anthropic's list figure was $965B (corrected),
  Skild AI's $14B (corrected to its real ~$4.5B), plus stale 2021-2022
  peaks re-marked to current rounds (Helion up to $15.5B, Saronic down
  to $9.25B, several others).
- **Instrument-typed entries at scale → Growth** (the Epic-Games
  designed row): Epic (common stock 2020), Telegram (the 2018 GRAM
  token pre-sale), Weee! (common 2020) all read Growth, not the card's
  literal instrument label.

### 5. The C2A caveat

The 61.8% graduation rate (102-row cohort, 63 graduated) carries the
same selection bias the Accel run documented and must not be quoted
bare: the deterministic Form-D layer established only 8 legs; the rest
were authored from knowledge where the follow-on outcome was
establishable, and the establishable set skews toward visible
successes. 94 cohort rows carry `cohort_unverified`. The honest
sentence: "of the seed entries where the follow-on could be
established, ~62% graduated — the establishable set skews toward
visible outcomes." Genuinely-undetermined recent seeds were left null
(censored or out of cohort), not counted false.

### 6. Debt, all flagged in rows

- cite_pending 14 (model-sourced entry stages on $1B+
  rows: Databricks, OpenAI, Rippling, Neuralink, Telegram, Meituan,
  Aledade, Hesai, CertiK, Seismic, fal.ai, plus a couple thin rows —
  the stage is a confident model call, the citation owed).
- director_pattern 1 (fal.ai — seat on the 2025 filings, participating
  round unannounced; flagged for the A/B pass as on Accel).
- model_disputes_source 50 (quarantined wrong-entity floats +
  glitched sources).
- cohort_unverified 94 (§5); stage_prior / country_prior / city_unknown
  on the heritage/thin tail (era conventions, no direct evidence).
- boundary 4 (apna-time / pixxel US papers ruled LSIP; pine-labs and a
  couple India rows whose LSVP-vs-LSIP attribution Erik may want to
  confirm).
- focus null 63 (heritage/thin rows outside the taxonomy).

### 7. Artifacts

- `classification.json` (932 rows incl. absorbed-merge keys; per-key
  provenance via record `who`), `base.csv` + `review.html` (875 rows,
  merged with the PRO-69 profile panel), `golden.json` (31-row stage
  set + 22 membership traps, both `_key_registered`),
  `scratch/pro66_generate.py` + `pro66_judgment.py` (reproducible),
  `scratch/pro66-audit.md` (the membership/identity fixes found during
  classification).
- Recorded batches: 16 grind + webpass-1..5 + webpass-6a/6b + the two
  China sweeps + C2A + fixups (all through `run.py record`).

Signed off (base) 2026-09-03; classification sample + ingest approval
pending. Post-approval ingest via `ingest-companies.ts`. Open: the
apna/pixxel/pine-labs LSVP-vs-LSIP boundary calls, the fal.ai and
Seismic A/B items, the ~40 cite_pending stage citations.

## PRO-69 — Investor classification (firm profile)

Autonomous session 2, kicked off 2026-09-02 ("please execute lightspeed
investor classification"), run base-less in parallel with the PRO-63 base
session per COLLECTION.md §11. File ownership was declared by session
message within minutes of detecting the parallel run: profile session owns
`investor.json` + `investor.sources.json`, the team payloads
(`sources/site/team.json`, `team-members.json`) and the fund filer sweep
(`sources/edgar/fund-formds.json`); base session owns `config.json`,
`decisions.md`, site companies extraction, the EDGAR partner sweeps, base +
overlays. Intel exchanged both ways: the profile's 112-filing Lightspeed*/
Faction* Form D enumeration seeded the base session's trap set (China
I–IV + China Select I, India Partners I–V, Faction Fund I/II + feeders +
Principals II, and the namesake filer clusters, all with CIKs); the base
session's roster and config merges flowed back, and its formd-sweep.json
(1,395 accessions over the 233-person roster) fed the profile's median and
hq recompute.

### Method notes, what differed from Accel

- **AUM is one sworn number, both range ends.** The single RIA (CRD 160187,
  effective 2025-04-28) covers the US, Europe and Israel desks per the
  firm's own about-page disclosure, so there is no in-boundary ERA to add a
  second sworn figure (the Accel London shape does not recur); the excluded
  affiliates (Faction CRD 318821, LSIP ERA CRD 310954) match the base
  boundary. FY2025 annual amendment (filed 2026-05-06) re-pulled at run
  time: **RAUM $50,005,412,721** (disc. $47.32B / non-disc. $2.68B, 51
  pooled vehicles). Parse proof: the Schedule D 7.B.(1) roster — 51 funds
  keyed by 805- IDs after de-duplicating the PDF's index stubs and
  page-header echoes — sums to the RAUM **to the dollar**, and the one
  non-discretionary account is exactly LS INVESTMENTS C, L.P.
  ($2,682,626,884). Press ">$40B globally" (Dec 2025) sits below the sworn
  floor and is flagged, not published.
- **The firm's filing style defeats the offering-amount cross-check.**
  Lightspeed L.P.s file Indefinite offerings with $0 sold and amend only at
  close (or never) — unlike Accel, where every $0-sold first filing carried
  a total-offering amount that matched press to the dollar. Consequence:
  six of fifteen curated fund sizes (XIII, Select IV, Opportunity I,
  XIV-A/B, Select V, Opportunity II) rest on press (Debevoise-confirmed
  closes), with filings as existence corroboration only; seven carry
  accessions asserted at build (XI, Select II, the five December 2025
  closes).
- **Co-issued Form Ds are a real trap.** X+Select I (2014), XII+Select III
  (2018/2019) and Luminous VI-A/B (2025) each file ONE Form D as co-issuer
  pairs; a per-accession issuer scan silently keeps the last co-issuer row
  and cross-wires names to CIKs. Caught because the XII "flagship" $2.11B
  looked wrong against an $890M XIII; resolved via the S&P split (XII
  $752.0M + Select III $1,361.8M = the filed $2,113,827,411 exactly).
  fund-formds.json records co_issuers per filing.
- **The site is first-party classification evidence end to end.** Every
  companies-page card carries Founded / Stage Invested / Backed Since /
  Status, and every row a data-investor attribute (lsvp | lsip | both) —
  the LSIP boundary of decisions.md #2 is machine-readable on the firm's
  own surface. The team page's own filters (Investors 46 / Specialists 33
  / Venture and Operating Partners 24; LSVP vs LSIP) set the individuals
  scope: the 46 Investors are published, roles as the cards present them.
- **Wayback degraded again; Common Crawl carried the roster.** IA's CDX
  answered "Temporarily Offline" intermittently at kickoff (third measured
  outage across runs), so commoncrawl-pull.py ran first (~9 min): 229
  people slugs and 811 historical company slugs (2014–2026 eras). CDX
  recovered enough for the base session's roster merge: 233 people,
  2012–2026, all 46 current Investors present.

### Results

- `investor.json` + `investor.sources.json`: every PRO-7 field populated or
  explicitly null with per-field source + basis; 8 flags carried.
- AUM {bottom: $50,005,412,721, top: $50,005,412,721}, sworn, parse-proven.
- Funds: 15 entries, vintages 2016–2025, sorted by size — $3.28B
  Opportunity III down to $500M Select II; 7 accession-asserted by
  build-firm-profile.py. Excluded with treatment flagged: the
  SIV/SPV/access trail (incl. Ascent $1.14B GAV, AI Renaissance + Platinum
  2026q3 filings), $1.25B of 2025 single-investor vehicles, the ~$600M Aug
  2026 continuation vehicle (decisions.md #6), and the China/India/Faction
  families (rulings 2–4).
- investment_range: floor $485K (the sole-investor Snapchat seed, 2012);
  median $17M — recomputed on the membership-verified base after PRO-63's
  checkpoint 2: $17,500,002 over 115 verified members with priced Form D
  histories (32 entries anchored past pre-investor rounds), vs $17.25M on
  the pre-base site-confirmed subset (71 entries) — stable across both
  populations, published value unchanged; ceiling $13B (the Anthropic
  Series F the firm co-led, 2025-09-02; own commitment reported ~$1B).
- notable_investments: 8 of the 9 issue candidates (Nutanix dropped on
  household recognition), all base-less-asserted against the firm's own
  companies dataset with first-party entry fields; Wiz carried as acquired
  (Google $32B, closed 2026-03-11) though the site still says Private.
- Stage [Seed, Series A, Growth, Late Stage] from the site's 553
  stage-tagged rows + "Seed to Series F and beyond"; geo core [US, Europe,
  Israel] per PRO-69 instruction (cap-of-two exceeded, high-severity flag,
  Erik's call at review); focus = the firm's 7-sector filter vocabulary
  crosswalked (Security notably absent from the firm's own vocabulary
  despite Wiz/Netskope/Rubrik/Cato — flagged as positioning-vs-behaviour
  signal for the post-base recompute).
- hq_location recomputed filing-grade: Menlo Park, CA on 34 of 35 own
  Form D filings (the one outlier is the Cayman-organized Affiliates X).
- individuals: 46 (site Investors group), 42 LinkedIn / 24 X socials.
- Icon: favico.svg → 256 PNG master → Icon Images bucket (PRO-53 flow),
  icon_url in the row.
- Taxonomy gate: clean — 0 errors, 0 warnings (run standalone via
  scratch/validate-taxonomy.ts, before and after build).
- build-firm-profile.py: clean; the two base-bound checks (notable ledger
  assertion, focus recompute) skipped loudly, to re-run at first
  post-base build.
- review.html rendered base-less (investor panel over the empty company
  table) and verified served on the review-surface config (localhost:8931):
  the panel expands with every field, its source link and basis.

### Prompt count (PRO-69 session)

1. Kickoff ("please execute lightspeed investor classification").

Corrections during run: none. Count final only after Erik's sample
sign-off.

### Debt

- ~~`investment_range.median` interim until the base lands~~ — CLEARED
  same day: PRO-63 hit full ledger coverage at checkpoint 2 and the §11
  post-base pass ran (median verified over 115 members, notables
  ledger-asserted at build, focus recompute correctly skipped at 0/931
  base sector tags — the curated enumeration stands until PRO-66 lands
  sector tags, when the recompute publishes automatically).
- FY2025 ADV predates the Dec 2025 closes; RAUM refreshes at the next
  annual amendment (~2027-03).
- The XIV-A/XIV-B sleeve split is undisclosed; published as one $1.98B
  entry.
