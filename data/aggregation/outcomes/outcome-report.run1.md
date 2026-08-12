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

**Crash/compaction safety:** all state on disk (`classification.json`, `queue/batch-NNN.out.jsonl`); `status` is derived from disk; `RUN-PROTOCOL.md` is the on-disk constitution re-read after every context compaction.

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

| File | What |
|---|---|
| `sequoia-capital-companies.csv` | Per-company deliverable, 1,293 rows |
| `review.html` | Review UI (j/k/c/x/u/n keys, localStorage, priority-ranked, decision export) |
| `classification.json` | Merged judgment records with notes + citations |
| `resolved.json`, `layer-a.json`, `layer-b.json` | Deterministic layer outputs |
| `graduation-formd.json`, `formd-rounds.json` | C2A evidence (round sequences, accessions) |
| `calibration-*.json`, `consistency-blind.json` | Quality measurements |
| `track-record-proposal.json` | §9 block, ready for PRO-25 |
| `RUN-PROTOCOL.md` | Run constitution (rules, duties, batch log) |
