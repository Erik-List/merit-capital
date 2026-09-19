# Outcome Classification Report — Sequoia Capital

Single-session autonomous run (PRO-6), completed 2026-08-12.
Base: pinned snapshot of the Sequoia Company Base, **1,293 rows** (md5 `63c4bc30`, manifest in `manifest.json`). All figures below are measured from `classification.json` + `resolved.json` merged over the snapshot; nothing is estimated.

## 1. What was classified

Per company (current-state only, per the profile-card copy "current value of companies where {investor} invested in"):

- `status` — private | public | acquired | defunct | unknown
- `valuation_usd` + `valuation_source` + `valuation_confidence` + `valuation_asof`
- `is_public` (IPO by-product bucket)
- `country` / `region`
- `seed_to_a_graduation` (C2A) + `entry_stage` (review-table only) + `graduation_source`
- `flags` + free-text `note` with citations

## 2. Method (first-principles design)

The run was rebuilt around one asymmetry: **a wrong positive (company in a $1B+ bucket) costs far more than a wrong negative**. So positives must be individually sourced, and model knowledge is only allowed to rule out, never to mint figures.

**Hard rule (machine-enforced):** `valuation_usd` may be non-null only when `valuation_source ∈ {sec_public_float, wikidata, unicorn_list, web_verified}`. `validate_record` rejects any batch line violating this; `verify` re-checks the merged set. Result: **0 of the 168 published figures come from parametric memory.**

Layers, in order:

| Layer | Source | What it contributes |
|---|---|---|
| A | SEC XBRL `dei:EntityPublicFloat` (per-CIK, cached) | 78 published figures; staleness >24 months → acquired signal; boundary flag within 20% of a threshold |
| B | Wikidata SPARQL (business-entity constrained) | country/region + cross-check (18 valuation assists, none published solo into buckets) |
| C | Wikipedia unicorn list (621 current + 208 former with exit reasons) | 41 published figures; recall net so bucket membership never depends on model memory |
| D | Form D rescan (74 local EDGAR ZIPs, CIK-driven) | 388 companies, 1,177 round sequences → deterministic C2A for 129 of 142 cohort rows |
| E | Model judgment in 28 batches of ≤45 | status rule-outs, identity checks, duplicate detection, desk assignment; never mints figures |
| F | Web verification pass (~35 searches, 9 rounds) | 49 published figures; corrections listed in §5 |

**Snapshot pinning:** the base CSV was rebuilt by other sessions mid-run once before; `prepare` therefore pins `base-snapshot.csv` and every later command reads the pin. `verify` reports live drift without corrupting the run.

**Crash/compaction safety:** all state on disk (`classification.json`, `queue/batch-NNN.out.jsonl`); `status` is derived from disk; the run rules lived in `RUN-PROTOCOL.md`, re-read after every context compaction (since retired into `../../COLLECTION.md`; the Sequoia-specific residue is in §11).

## 3. Measured quality

- **Calibration** (blind vs filing-grade key, 40 rows): **35/40 status (88%), 34/40 full-record (85%)**; 3 of the 6 misses were defects in the key that the model correctly disputed.
- **Self-consistency** (30 model-judged rows re-judged blind, seed 42): **30/30 status agreement (100%)**; no `unstable` flags needed.
- **verify: clean** on the final merged set (source rule, slug coverage, enum validity, duplicate-group exclusion all pass).

## 4. Results

### Status (all 1,293 rows)

| status | count |
|---|---|
| private | 440 |
| acquired | 439 |
| unknown | 202 |
| public | 119 |
| defunct | 93 |

`unknown` is dominated by Form D name-collisions (surgery-center LLCs, micro-filings) where identity could not be established; these carry explanatory notes.

### Track-record buckets (derivation set: 1,182 rows after excluding 111 flagged duplicate / not_a_company / suspect_base)

| bucket | count | share of counted base |
|---|---|---|
| $1B+ | 128 | 10.8% |
| $10B+ | 46 | 3.9% |
| $100B+ | 12 | 1.0% |
| IPO (currently public) | 133 | 11.3% |

$100B+ roster: Nvidia $4.0T, Apple $3.25T, SpaceX $2.1T, Google $1.9T, Anthropic $965B, OpenAI $852B, Oracle $347B, Cisco $248B, xAI $230B, Uber $188B, Stripe $159B, Palo Alto Networks $120B.

*(Checkpoint roster. In the final data xAI is `acquired` (absorbed into SpaceX, Feb 2026; its value sits inside the SpaceX row) and Waymo joined the bucket at $126B on 2026-09-03; see §12.)*

Buckets are **cumulative** ($100B+ ⊆ $10B+ ⊆ $1B+). The current `merit.tsx` treats them as disjoint (`rest = total − sum`), which double-counts; the fix is scoped in PRO-25. `graduation_rate` shape mismatch ({rate, companies[]} vs {rate_percent, sample_size}) is also in PRO-25.

### Valuation sources (168 published figures)

sec_public_float 78 · web_verified 49 · unicorn_list 41. Confidence over all rows: high 471, medium 802, low 20; **no $1B+ row is low-confidence**.

### Seed-to-A graduation (C2A)

Cohort **142** (Seed entry, ≥24 months since entry or resolved earlier), graduated **40**, rate **28.2%**. Excluding flagged rows: cohort 138, graduated 39, **28.3%**. Sources: Form D deterministic 129, model 13. Censored (<24 months, null by rule): 9. Entry is anchored at the earliest **partner-attributed** accession (fixes the pre-Sequoia-round bug that had inflated the rate to 44%); graduation = later round ≥2× entry amount and ≥$5M.

## 5. Corrections the run caught (would otherwise be published wrong)

- **Electronic Arts — take-private closed 2026-08-04** (four days before this run); was "public" in every prior layer.
- **SpaceX — public since 2026-06-12**, ~$2.1T; base had it private.
- **Wiz — acquisition by Google closed 2026-03-11**.
- **Nubank — public, $67B** (Sequoia seed → graduated; the single best C2A validation row).
- **dbt Labs — merged into Fivetran** (acquired, not private).
- **Rackspace — still listed**; the >24-month float staleness heuristic had mis-signaled acquired (false stale).
- **Ineffable Intelligence = David Silver's lab**, $1.1B seed at $5.1B co-led by Sequoia; identity confirmed by web.
- 23andMe → TTAM (sub-24-month float death), Google→Alphabet reorg (stale-float misfire), generic-name CIK false joins (apollo ↔ Apollo Global, linear ↔ Linear Technology, harmonic ↔ HLIT, paid) — all caught by the standing verification duties.

## 6. Duplicates and artifacts (excluded from derivation, 111 rows)

- **84 duplicate rows**: 18 groups via shared CIK plus ~30 legal-name duplicates found by model knowledge (Counsel AI = Harvey, ZenLeads = Apollo.io, Raintank = Grafana Labs, sp0n = Citizen, TrialSpark = Formation Bio, Refresh Club = The Wing, Standard Nine = Inkling, Qadium = Expanse, Rearden = Deem, VA Linux = SourceForge lineage, Pivotal registrant pair, SpaceX registrant pair, …). One canonical row per group is kept in the derivation set.
- **19 not_a_company**: fund vehicles, persons, filter labels (e.g. Reynolds & Co Venture Partners).
- **9 suspect_base**: Tier C rows with no Wayback evidence and $1B+ claims (e.g. Zai Lab, a Qiming-style China deal).

## 7. What remains for human review (in priority order, matching review.html)

1. **52 unpinned rows** (`needs_web_value`, value = null): deliberately kept **out of all buckets** under the conservative triage policy. Three families:
   - *China/India-desk candidates* (53 China, 49 India flagged overall; e.g. PDD ~$150–200B, Full Truck Alliance, Meesho, Groww, Justdial): whether these belong in the US/Europe Sequoia base is a scoping decision, not a data question.
   - *Stale 2021–22 unicorn marks* (Glossier, Front, Mixpanel, Clipboard Health, LangChain, Hex, …): last-round prices that likely no longer hold; publishing them would overstate current value.
   - *Weak-identity rows* (linear, carbon, maven, magic): name-collision risk.
2. **47 model_disputes_source** rows: the model disagrees with a deterministic layer; each note says why.
3. **35 identity_uncertain** rows.
4. Duplicate-group canonical-row choices (default = strongest evidence tier; override in review.html).

## 8. Limitations

- **Current-value-only systematically understates exited winners**: WhatsApp ($19B exit), Instagram, YouTube, PayPal appear as "acquired, no current value". The card copy defines the metric this way; a separate exit-value metric would need per-deal proceeds data.
- Private valuations are last-round or reported secondary marks, inherently lagged.
- The unicorn list is a floor for recall at $1B, not for $10B/$100B (those all came from float or web).
- Form D coverage starts 2006; earlier entries are `pre-window` (entry/graduation null).
- `unknown` status (202 rows) is honest ignorance, mostly identity collisions on generic names.

## 9. Proposed derivation blocks (PRO-25 input)

`track-record-proposal.json` holds the full block. Shape:

```json
{
  "total_companies_invested": 1182,
  "one_b_companies":     {"amount": 128, "names": ["Nvidia", "..."]},
  "ten_b_companies":     {"amount": 46,  "names": ["..."]},
  "hundred_b_companies": {"amount": 12,  "names": ["..."]},
  "ipo_companies":       {"amount": 133, "names": ["..."]}
}
```

`graduation_rate`: `{"rate_percent": 28.3, "graduated": 39, "sample_size": 138}` (flagged rows excluded, censored rows excluded from cohort).

Derivation policy encoded here: exclude rows flagged duplicate/not_a_company/suspect_base, one canonical row per duplicate group, cumulative buckets, null-value rows never in buckets.

## 10. Artifacts

| File (current name after the PRO-59 move) | What |
|---|---|
| `base.csv` | Per-company deliverable (the one merged surface; was `sequoia-capital-companies.csv` at run time) |
| `review.html` | Review UI (read-only since PRO-56; was interactive at run time) |
| `classification.json` | Merged judgment records with notes + citations |
| `resolved.json`, `layer-a.json`, `layer-b.json` | Deterministic layer outputs |
| `graduation-formd.json`, `sources/edgar/formd-issuer-rounds.json` | C2A evidence (round sequences, accessions) |
| `calibration-*.json`, `consistency-blind.json` | Quality measurements (retired; results recorded in §3) |
| `track-record-proposal.json` | §9 block, consumed by PRO-25, then retired (PRO-24 moved derivation into the DB) |
| `../../COLLECTION.md` | The collection playbook (rules and duties, generalized from this run's protocol docs) |

## 11. Run chronology and Sequoia rulings (residue from the retired protocol docs)

The binding rules generalized into `../../COLLECTION.md`; what follows is what happened on Sequoia specifically, moved here when `RUN-PROTOCOL.md`, `CLASSIFICATION-V2.md` and `ENTRY-STAGE.md` were retired (PRO-58). Sequoia's investor-specific decisions live in `decisions.md`.

### Chronology

- **Run 1 (2026-08-11, sections 1–10 above)**: the original grind over the 1,293-row pinned snapshot. Calibration 35/40 status (88%), 34/40 full (85%) — 3 of 6 misses were key defects the model correctly disputed (23andMe dead-but-recent-float, Google stale→acquired misfire on the Alphabet reorg, apollo false CIK join). Self-consistency 30/30.
- **Run 2 (2026-08-12)**: scope augmentation after Erik's review. Base hygiene moved upstream (`identity-merges.json`, consumed on every rebuild; run-1 had flagged BOTH rows of a dup pair, silently dropping Block $39.4B from derivation — replaced by `duplicate_of` on non-canonical rows only). Added 100%-fill columns: `valuation_range`, `hq_country`, `entry_stage`. 692 rows / 16 batches.
- **Run 3 (2026-08-12)**: `entry_stage` rebuilt from first principles after Erik's finding (Airbnb/Stripe should be Seed, HubSpot Growth). Golden set of 40 documented entries: run-2 column 32/39 (82%); all seven misses were `formd_band` rows, model-judged rows 24/24. Root causes: coverage blindness (Sequoia's entry often predates the first partner-attributed filing — Airbnb seed '09 and Stripe seed '10 never filed), ordinality blindness (HubSpot's $18.8M third round banded "Series A"), band trusted as label. The corrected evidence order is now COLLECTION.md §6.
- **2026-08-13, the CrowdStrike question**: a partner's personal Section 16 filing is not evidence the firm invested (Gandhi filed for Accel's board seat; Goetz is an independent Intel director). Now the person-attribution rule in COLLECTION.md §1.
- **Base v2 (2026-08-13)**: the inversion — publish only rows with sufficient evidence that survive an independent membership judge. Precision pass over 1,055 rows: 869 seeded on sufficient evidence, 186 name-match rows judged individually (~16 web arbitrations) → 184 not_member, 4 recovered members (Avalanche, CloudShare fka IT Structures, Muze, Romotive), 1 uncertain. Recall pass (parametric enumeration, fund 13D/G subject diff, European probe): zero missing members. Base 1,055 → 873; Tier C 201 → 19; C2A 47.1% → 71.7% (33/46) once the fake seed cohort left; Pre-Seed to zero (all collision micro-filings).
- **Classification v2 (2026-08-13)**: adversarial A/B pass over the visible slice, ~60 fresh web arbitrations; every public $1B+ row got a cited market cap. Then `focus` (twelve-value re-judge) and `hq_city` (one parametric pass, 120/batch).

### Classification v2 corrections (the attack pass)

Confluent acquired by IBM ($11B, closed 2026-03-17, delisted); Faire's Nov-2025 tender at $5.2B (59% below the stale $12.6B); Houzz down-bucketed below $1B; Root Insurance out of the bucket ($805M cap); StarkWare corrected to the real $8B/May-2022 primary; Fireblocks asof → Jan 2022; Notion → $11B Jan-2026 tender; Vanta $4.15B, Trade Republic EUR 12.5B, Verkada $5.8B, Commure $7B, Whatnot $20B, Ramp $44B, ElevenLabs $11B, OpenEvidence $12B, Skild $14B, Sierra $15.8B, NinjaOne $12.3B, Cyera $12B, Odoo ~EUR 7B replaced stale marks. Armis flagged for status review (pending ServiceNow $7.75B acquisition, announced 2025-12-23). Float-to-cap moves put Google $4.23T, Cisco $483B, Palo Alto $314B, Western Digital $151B, Snowflake $116B and Airbnb $100B into the $100B+ bucket (15 names). Debt made explicit: 29 sub-$5B private marks and 119 $1B+ stage claims `cite_pending`; all 46 C2A cohort rows `cohort_unverified` (Erik's keep-with-flag ruling). Valuation citation coverage 119/148 $1B+ rows (80%).

### Duplicate groups (CIK-shared, resolved via identity-merges)

17 genuine renames (10Gen→MongoDB, Evenflow→Dropbox, Square→Block, SourceForge/VA lineage, Bit9→Carbon Black, Widgetbox→Flite, Turin→Force10, Rearden→Deem, Arbor→Hyperion, HQC→Health Catalyst, Qadium→Expanse, Network Appliance→NetApp, Service-now.com→ServiceNow, …) plus one false join: base `linear` (the software company) ↔ LINEAR TECHNOLOGY (semiconductor, acq. Analog 2017) via suffix-stripped norm collision — the canonical example for verification duty 3.

### Taxonomy rulings applied (focus, twelve values)

Result: 821/873 classified (94.0%), 52 outside, of which 47 are the permanently unidentifiable floor; real residual ambiguity 5 rows. Rulings behind the precedence rules now in COLLECTION.md §6: Apple/Atari/Jawbone → Consumer (consumer devices, not Industrial despite the `hardware` alias); Cisco/Aruba/Confluent/MongoDB/Cohesity → Data Infrastructure; Wiz/Palo Alto/Okta/Symantec/Verkada/Chainguard → Security; Fireblocks/Phantom/FTX/LayerZero/StarkWare → Crypto & Web3, Robinhood stays Fintech; AdMob/AdBrite/Amobee/Chartboost → Media, Attentive/Hearsay stay SaaS. Distribution in `track-record-proposal.json` under `by_focus` with a $1B+ breakdown. Downstream migration of `investors.investment_scope.focus` (seven → twelve in DB and leaderboard filter) tracked separately.

### hq_city results

664/873 located (76%), 146 distinct cities; 100% of $1B+ rows, 193/195 of the visible slice (gaps `pace` and `two` have unresolved identity). All 209 nulls in the sub-$1B tail with `city_unknown`. Top: San Francisco 176, New York 54, San Jose 30, Mountain View 26, Palo Alto 25, Santa Clara 24, Sunnyvale 20, Tel Aviv 18, Redwood City 16, Los Angeles 11; Bay Area municipalities 384/664 (58%). Entry-time-trap movers caught: Aurora→Pittsburgh, Snowflake→Bozeman, Block→Oakland, Green Dot/Natera→Austin, Omnicell→Fort Worth, Bird/Picsart→Miami, Appirio→Indianapolis, SpaceX→Starbase. Six `city_country_conflict` rows, all country defects: Barracuda (BE), Aquarium (DE), Avanex (CH) are wikidata identity errors; Rappi and Bubble Motion took US from a subsidiary's filing; LayerZero operates from Vancouver under a US incorporation.

## 12. Company Base build residue (from the retired Build & Reconciliation Report)

The generic build method — evidence layers, exclusion filters, tiering, duplicate arbitration — lives in `../../COLLECTION.md` §5 and in the collector scripts. What follows is the Sequoia-specific record from the v0 build report (2026-07-19), retired in PRO-59.

**Build stats (v0, pre-membership-judge).** 1,293 candidate rows: 279 Tier A / 719 Tier B / 295 Tier C. 182 pooled-fund issuers (253 filings) dropped; 22 other-desk rows partitioned out (21 china, 1 india); ~105 ex-partner deals removed; 94 name-variant duplicates merged (6 kept separate). Entity registry: 301 vehicles (151 us-eu, 75 china, 39 india, 11 israel, 25 external). The v2 membership inversion (§11, Base v2) then took the base 1,055 → 873.

**Wayback era yields.** Era A `/company/` 2006–2009: 284/66/87/24 slugs per year, enumerated from the CDX index. Era B `/us/` 2010–2014 via sitemap + homepage: 275–377 paths per year, 2013–14 thin from a site redesign; the old CMS left an un-interpolated Ruby object in category-link alt text (`#<Region:0x..>`), which is what separates the 68 category pages per snapshot from companies and supplies era-B display names. Era C `/companies/` 2015–2021: 188 → 290 companies with sector + partner tags. Era D `/our-companies/` 2021–2026: ~32 server-rendered entries per snapshot only (lazy-loaded page); covered instead by the site API (418 companies via WordPress REST) and Form D.

**Audit findings that shaped the code** (all fixed and re-verified): a person filed as a company (`bill-coughran` slug vs `William Coughran`, fixed by `same_person()` matching); the Josephine/Joseph Chen feminine-variant collision that attributed Renren's fintech deals to Sequoia (fixed by `DISTINCT_DESPITE_PREFIX`); 12 property LLCs under a different Ravi Gupta (fixed by the non-portfolio industry rule — the audit showed all 19 rows previously spared as "ambiguous industry" were noise); spacing duplicates (`Mark Logic`/`MarkLogic`, fixed by the space-insensitive join key); and the regression that key introduced (word-prefix duplicate check broke, fixed by the separate `norm_words` key). HTML entities decoded at every read point (`Alpha &amp; Omega` never joined its Form D row).

**Duplicate arbitration results.** The investor's own publications are the arbiter (two names in one snapshot = two companies): 93 merged, 6 kept separate (`Carbon`/`Carbon Black`, `Linear`/`Linear Technology`, `Magic`/`Magic Eden`, `Parallel`/`Parallel Web Systems`, `Elevate`/`Elevate Credit`, `Nimble Storage`/`Nimble Rx`). Snapshot scoping keys on `snapshot_ts`, not year (a year-keyed check wrongly split `Barracuda`/`Barracuda Networks`). A differing EDGAR CIK proves distinctness only when both rows are independently listed (`Aurora Innovation`/`Aurora Operations` are one company's filing entities).

**Known limitations that still apply.** Era D shallow in the archive (mitigated by the site API and Form D); 2013–14 listing gap; Form D electronic coverage starts 2009, Section 4(a)(2) raises and non-US issuers never file; `first_seen = '?'` on site-listed rows with no archive or filing date (the site API's `published` field is a page-creation date and deliberately not used); pre-2006 history out of window by design, so the foundational era (Apple-as-entry, Cisco, Oracle) is absent from entry-level columns; the partner roster's archived-snapshot span under-reports tenure for rarely-crawled people; EDGAR collection is bounded by the entity registry.

## 12. Cross-investor alignment (2026-09-03)

`run.py verify` now compares every row with the other investors' published
`base.csv` on `status` and `valuation_range` (COLLECTION.md §10 invariant
10; rulings in `data/collection/cross-investor.json`; method and gate
described in the Lightspeed report). First run on Sequoia: 46
disagreements, most of them homonyms (Bird, Linear Technology, Convex,
Tandem, Maven, Avalanche, Handshake, Harmonic) now ruled distinct; after
resolution 0 (4 accepted thin pairs). Recorded with
`who: cross-investor-align-2026-09-03`; reproducible from
`data/collection/shared/cross-align/2026-09-03.py`.

**Rows changed (15):**

| slug | before | after | evidence |
|---|---|---|---|
| waymo | acquired / below_1b | private / 100b_plus $126B | never acquired: Alphabet-controlled subsidiary raising priced external rounds; $16B at $126B post 2026-02-02, co-led by Sequoia. Ruling 6 in decisions.md, Erik to confirm |
| grafana | private / below_1b (dedup remnant) | 1b_plus $9B | GIC-led round reported Feb 2026 (last company-confirmed $6B, Aug 2024); either way $1B+ |
| harvey | private / below_1b (dedup remnant) | 10b_plus $11B | $200M at $11B post 2026-03-25, co-led by GIC and Sequoia |
| ethos | public / below_1b ($352M float) | public / 1b_plus $2.42B | IPO 2026-01-28 (Nasdaq: LIFE); market cap 2026-09-03; the float was never a value |
| reflection-ai | 1b_plus $8B | 10b_plus $25B | 2026 round closed at $25B pre-money (CEO, CNBC 2026-04-23) |
| doordash | 10b_plus $91.9B (Aug) | 10b_plus $96.35B | same-day cap shared with a16z; the two runs had straddled the $100B edge |
| ironclad | $3.2B as-of 2025-06, no citation | $3.2B as-of 2022-01, cited, `stale` | the as-of was an ARR remark, not a round |
| physical-intelligence | $5.6B, no citation | citation added | the ~$11B 2026 round is still in talks |
| census, replicate, stainless, varagesale, iron-fish | private / unknown | acquired | Fivetran (2025), Cloudflare (closed 2025-12-01, $57.4M), Anthropic (announced 2026-05-18), VerticalScope (2017), Coinbase acqui-hire (2025-03) |
| bird | acquired | defunct | Bird Global liquidated in Chapter 11, equity wiped; assets to Third Lane |
| orchid-labs | unknown | private | operating; aligned with a16z |

**Counts.** cumulative $1B+ 148 → **152**, $10B+ 53 → **56**, $100B+ 15
→ **16**; valuation_range 725 / 95 / 38 / 15 → **721 / 96 / 40 / 16**;
status 336 / 349 / 76 / 59 / 53 → **334 private / 352 acquired / 77 defunct
/ 59 public / 51 unknown**. `verify` clean. **Re-ingested 2026-09-03** with Erik's
approval (sample sign-off, zero corrections); the database now derives
152 / 56 / 16 and 59 public on 873 rows. The Waymo ruling (decisions.md
6) went in as proposed; a `who: "erik"` correction and a re-ingest
reverse it if he rules otherwise.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Twenty published rows carried `identity_uncertain` (fourteen further entries
in `classification.json` are stale keys). This book's flagged set is the
opposite of Redpoint's: almost all of it is genuinely unnameable, because the
era-D cards carry a one-word name and a sector tag and nothing else — no url,
no description, no founders.

**Four rows are named and lose the flag.** `clover-newco-llc` is Clover
Health's legal name (Sequoia led the 2017 $160M Series D; CLOV since the 2021
SPAC), `cue-labs` is Greplin renamed, which Apple bought in 2013, `aquarium`
is Aquarium Learning, the SF YC company that wound down around 2023, and
`paid` is Paid.ai, Manny Medina's agent-billing company. Two of them keep a
separate dispute that is not about identity: Aquarium's Wikidata "Germany"
and Paid's $6.8M OTC-shell float are both false joins on a short name.

**One row is identified with a namesake.** `handshake` is the handshake.org
naming protocol, whose 2018 token sale is the only event on the record —
never to be joined with Handshake the university-recruiting company.

**Three rows keep their values without a name**, because their own filings
carry the stage: `cove` ($5M in 2020 with one prior), `indie-technologies-inc`
($60M in 2022, $46M in 2024) and `public-stage` ($65.5M in 2020 with three
priors). This is the carried-through exception, and it is the difference
between "we cannot name the company" and "we know nothing about the round".

**Twelve rows read `undetermined`:** `allegro`, `fin`, `flex`, `glow`,
`mithril`, `monad`, `nevis`, `open`, `origin`, `otter`, `veil` and `x`. Every
one of them published a stage that was the desk's convention applied to a
company nobody could name, and four carried a Wikidata country match that the
judges had already called a collision (Germany, Russia, Romania, India). `x`
is a single letter. `flex` is the instructive one: the note read "likely the
NYC rent-flexibility fintech", and a likely reading is not an identification.

`verify --in-flight` clean. Sequoia is mid-S2A-wave with a live in-flight
marker, so this pass did not close it, did not rebuild the base and did not
re-export; the wave owns the published surface.
