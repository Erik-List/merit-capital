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
