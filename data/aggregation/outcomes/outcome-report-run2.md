# Outcome Classification Report — Run 2 (Sequoia Capital)

Single-session autonomous run, completed 2026-08-12. Supersedes [outcome-report.run1.md](outcome-report.run1.md).
Base: **1,059 published rows** (pinned snapshot; run 1 worked on 1,293). All figures measured from the merged classification; `verify: clean`.

## 1. What run 2 changed (Erik's five orders)

### a. Identity dedup moved into the base itself

Run 1 flagged duplicates but left them in the base, and its derivation bug excluded *both* rows of a pair (Block's $39.4B silently dropped — the defect Erik spotted). Run 2 fixes the class, not the instance:

- **`identity-merges.json`** — a durable overlay next to the base (60 merge groups, 19 rejects, 103 desk moves, 3 proven-distinct pairs) consumed by `build-company-base.py` on every rebuild, exactly like review decisions.
- Rename detection is now **deterministic**: `formd-issuer-evidence.py` sweeps the local Form D ZIPs for `ENTITYNAME` + `ISSUER/EDGAR_PREVIOUSNAME` chains per CIK. That machinery surfaced six renames run 1 never saw (ServiceNow←service-now.com←Glidesoft, MongoDB←10gen, Dropbox←Evenflow, Health Catalyst←HQC, Berkeley Lights←Bruker Cellular, Feihe←American Dairy).
- `verify-company-base.py` gained three invariants (no absorbed/rejected slug published, every canonical present, no unexplained shared CIK). **13/13 pass.**
- Base arithmetic: 1,293 → 1,107 (−63 merged, −19 artifacts/fund vehicles, −103 China/India desk moves to `other-desk-companies.csv`, −1 late merge Indigo Fair→Faire). Every removed row is preserved in its partition file, nothing deleted.

One consequence worth naming: **ServiceNow's $176B float now lands in the buckets** — run 1 had the value stranded on a flagged duplicate row.

### b. value_tag, 100% fill

Every row carries `value_tag ∈ {below_1b, 1b_plus, 10b_plus, 100b_plus}` (highest threshold met). The run-1 hard rule stands: a tag above `below_1b` **requires** a sourced `valuation_usd` (`sec_public_float`, `wikidata`, `unicorn_list`, `web_verified`); the model may only rule *down*. `verify` enforces tag/figure consistency row by row.

### c + d. country and entry_stage, 100% fill, entry-time first

Source hierarchies (all recorded per row as `*_source` + `*_confidence`):

| Field | 1st | 2nd | 3rd |
|---|---|---|---|
| country | `formd_address` — ISSUERS.tsv business address at the **earliest partner-attributed accession** (entry-time, offshore havens skipped) — 355 rows | `wikidata` P17 — 140 | `model_knowledge` — 611 (+1 web) |
| entry_stage | `formd_band` — partner-anchored first-round amount vs STAGE_BANDS — 372 rows | `model` — named-deal knowledge ("Sequoia led the 2011 Series A") — 735 | — |

**Why entry-time first:** the map on the investor page shows *investment* geography. A Form D filed at the moment of the round records where the company sat when the partner wrote the check; Wikidata records today's HQ of whatever entity a name-match found. The cross-check proved the ordering: of 12 formd/wikidata disagreements, **11 were Wikidata name-collisions** (Blues→the NZ rugby franchise, Aurora→Malaysia, Mercury→Japan) and only one was a genuine miss (Klarna's London filing office vs Stockholm HQ — corrected by hand).

**Honest priors, flagged:** 49 unidentifiable rows (2006-09 scrape strays, micro-filings) carry `country_prior` (United States, low confidence) and 63 carry `stage_prior` (Series A, the desk's classic entry, low confidence). They are visible in review.html, not laundered into confident answers.

### f. Post-delivery fix: the initial-only person match (Intuit class)

Erik asked how Intuit came to show a $6.7M Sequoia Seed. It never did: `formd-query.py` matched Form D related persons on surname plus an **unbounded** given-name prefix, so a filed initial matched any partner sharing the letter. Intuit's CFO **R. Neil Williams** matched Sequoia's **Reggie Williams**, and the 2011 filing (a public company's exempt offering, banded "Seed" by amount) pulled Intuit into the base as a portfolio company.

One defect, 48 false rows: `A Moore` → `Alex Moore` produced the entire ~30-row surgery-centre cluster, and `R Williams` / `S Singh` / `J Lee` pulled in Amgen, DocuSign, Concur, Amyris, BitGo and Forum Energy.

Fixed at both sites: the sweep now requires a ≥3-character given-name prefix, and the base build refuses initial-only attributions independently (so a stale `formd-sweep.json` cannot reintroduce them). A second rule follows from it — a Form D filing with **no attributable partner**, no listing and no Sequoia SEC filing is not evidence of a deal, and is dropped. Base 1,107 → 1,059; base verify 13/13.

### e. Scope

The published table now carries `status, value_tag, valuation_usd(+asof/source/confidence), entry_stage(+source/confidence), country(+source/confidence), region, seed_to_a_graduation` — the full shape PRO-25 needs for stage and geography display.

## 2. Results (derivation set: 1,055 rows; 4 excluded as suspect_base)

### Value

| tag | count |
|---|---|
| below_1b | 899 |
| 1b_plus (cumulative 156, **14.8%** of base) | 108 |
| 10b_plus (cumulative 48) | 36 |
| 100b_plus (cumulative 12) | 12 |
| currently public | 108 |

$100B+: Nvidia $4.0T, Apple $3.25T, SpaceX $2.1T (the merged SpaceXAI entity), Google $1.9T, Anthropic $965B, OpenAI $852B, Oracle $347B, Cisco $248B, Uber $188B, **ServiceNow $176B**, Stripe $159B, Palo Alto Networks $120B.

### Geography (region ← country)

North America 925 · Europe 56 · Middle East 55 (Israel-driven) · Asia 8 · Latin America 7 · Africa 2 · Oceania 2. (China/India desk rows left the base under the decision-desk rule; the remaining Asia rows are Japan/Korea/SEA deals booked on the US desk.)

### Entry stage

Series A 542 · Seed 250 · Growth 233 · Pre-Seed 30. Seed-to-A graduation: **41 of 111 = 36.9%** (decided mostly from Form D round sequences, censoring <24 months, entry anchored at the first partner-attributed filing). The rate rose from run 2's first pass (30.3%) because ~32 fake 'Seed' rows — sub-$1M surgery-centre and micro-filings that were never Sequoia deals — left the cohort with the fix in §1f.

## 3. Web pass (37 rows, ~25 searches)

Every remaining open-value row was pinned or ruled out with a citation; `needs_web_value` count is now **zero**.

- **Status corrections:** xAI absorbed into SpaceX (all-stock merger Feb 2026, ceased as a separate company May 2026 -- caught post-run on Erik's question; the row stays as a distinct Sequoia investment, WhatsApp-style, but carries no standalone value since it now lives inside the public SpaceXAI cap); Despegar acquired by Prosus (closed 2025-05-15, $1.7B EV, delisted); Tecton acquired by Databricks (2025-08, ~$900M — run 1's dispute of the acquired signal was itself wrong, now noted); Mercury is private (the "acquired" claim was a Wikidata collision with Mercury Interactive).
- **Fresh pins (selection):** Figma public ~$13.5B (down from $56B at IPO); Mercury $5.2B (May 2026); Valar Atomics $6.0B (Sequoia-led $1B round, Aug 2026); Peregrine $6.8B; STARK ~$4.1B; Eon $4.0B; Chai Discovery $3.8B; Zum $1.7B; Maven $1.7B; SendCutSend $1.01B; Nominal $1.0B; XBOW >$1B; LangChain $1.25B; Linear $1.25B; Framer $2B (and Dutch, country corrected).
- **Evidence-based rule-outs to below_1b:** Glossier (2025 raise sought under $1B), SecurityScorecard (secondary estimate ~$360M), Hex (~$450M 2025 C), Versa Networks (last *disclosed* mark $700M), Cobot and Kriya (no publishable ≥$1B mark despite likely scale — the two most conservative calls, flagged `boundary` for review).
- **Stale-mark policy (new in run 2):** per the 100%-fill order, private companies carry their last credible round mark with `valuation_asof` + a `stale` flag when >24 months old (BigPanda $1.2B '22, Front $1.7B '22, Mixpanel $1.1B '21, Snapdocs $1.5B '21, Pilot $1.2B '21, Carbon $2.4B '19, …), down-tagged only on affirmative decline evidence. Run 1 abstained on these; run 2 publishes them dated and flagged.

## 4. Measured quality

- Run-1 calibration stands (35/40 status, 34/40 full record vs filing-grade key; 30/30 blind self-consistency).
- **New:** the formd/wikidata country cross-check above (11 of 12 disagreements were the *other* source's error).
- Confidence distribution on model-judged fields: country high 400 / medium 88 / low 49; entry stage high 64 / medium 178 / low 317 (the low tail is dominated by pre-window venture entries where "Series A" is an era convention, and by the flagged priors).

## 5. What remains for human review (review.html, priority-ranked)

1. **63 `stage_prior` / 49 `country_prior` rows** — unidentifiable base strays; the real fix is base membership review, not better classification.
2. **23 `stale` marks** carrying 2019-22 valuations (each dated in `valuation_asof`).
3. **14 `boundary` rows** within 20% of a threshold, incl. the Cobot/Kriya conservative calls.
4. **5 suspect_base rows** (Intel, CrowdStrike class — membership doubtful, kept out of derivation).
5. Desk moves are reversible: edit `identity-merges.json`, rebuild.

## 6. Limitations

- Private marks are last-round prices; the `stale` flag and `valuation_asof` make the lag explicit rather than hiding it.
- `entry_stage` for pre-2006 deals has no Form D floor; "Series A" is the recorded convention for classic venture entries, at low confidence.
- Current-value-only still understates exited winners (WhatsApp, YouTube: acquired, below_1b by definition of the metric).
- The amount-banded `formd_band` stage is era-sensitive; a named-deal model override with `stage_disputes_band` was available but rarely needed.

## 7. Artifacts

| File | What |
|---|---|
| [sequoia-capital-companies.csv](sequoia-capital-companies.csv) | 1,107 rows, full run-2 schema |
| [review.html](review.html) | Review UI with the new columns |
| [track-record-proposal.json](track-record-proposal.json) | PRO-25 derivation block: buckets, tags, graduation_rate, by_region, by_entry_stage |
| [../company-base/identity-merges.json](../company-base/identity-merges.json) | Durable identity corrections (the base-hygiene deliverable) |
| [issuer-evidence.json](issuer-evidence.json) | Entry-time addresses + name histories per CIK |
| `*.run1.*` | Complete run-1 archive |

---

# Run 3 addendum — entry_stage rebuilt (2026-08-12)

Erik's spot-checks (Airbnb/Stripe should be Seed, HubSpot Series D) exposed the amount-band
proxy as the column's weak layer. Run 3 rebuilt it from first principles.

## Measured before/after

A golden set of 40 documented Sequoia entries was assembled and web-verified where uncertain
(`golden-entries.json`). The run-2 column scored **32/39 (82%)** on it — and **all seven misses
were `formd_band` rows** (model-judged rows went 24/24). After the rebuild: **39/39 (100%)**,
with one golden label itself corrected by the evidence (23andMe: Sequoia led the $250M 2017
round, not the 2007 A).

## The three failure modes, and the fixes

1. **Coverage blindness** — Sequoia's entry often predates the first partner-attributed Form D
   (Airbnb's '09 and Stripe's '10 seeds never filed). The first filing is now treated as a
   CEILING on entry recency, never a label; zero-prior structural labels are capped at medium
   confidence.
2. **Ordinality blindness** — HubSpot's $18.8M third round had banded "Series A". The new
   `structural_stage()` positions the entry filing within the company's FULL round sequence:
   >=2 prior filings forces Growth at high confidence (the only structurally robust signal).
3. **One fixed band across eras** — Block's $27.5M 2011 Series B sat under a 30M "Series A"
   ceiling. Bands are now era-adjusted (seed ceiling 1.5M in 2010 -> 8M in 2022+) and apply
   only to structurally sound first rounds.

Evidence order inverted: **named-deal knowledge (round + year required in every note) >
structural ordinality > era band > flagged prior.** Every override of a Form D signal carries
`stage_disputes_band` (43 rows); unidentifiable strays keep `stage_prior` (66 rows).

All 1,059 rows were re-judged (22 stage batches, zero coverage gaps). Sources now:
model/named-deal 855 · formd_structural 189 · web_verified 15.

## Headline corrections

Airbnb Growth→**Seed** (led the $585K Apr 2009 seed), Stripe Growth→**Seed** (the ~$2M 2010
seed), HubSpot Series A→**Growth** (led the $32M Series D 2011), Block Series A→**Growth**
(led the $27.5M Series B 2011; run-1's "led Series A 2009" note was wrong — Khosla led that),
MongoDB Series A→**Growth** (third round, late 2010), Salt Security→**Growth** (the 2019 round
was S Capital, the Sequoia Israel spin-out — a different firm; Sequoia's first check was the
Dec 2020 B), Valar Atomics Seed→**Growth** (first confirmed Sequoia check is the $1B 2026 B),
PANW Pre-Seed→**Series A**, 23andMe→**Growth**, plus ~40 more disputes resolved against the band.
Two more base defects fell out in passing: Maplebear Inc. = Instacart (merged in the overlay)
and Indigo Fair = Faire.

## New column shape

Series A 566 · Growth 271 · Seed 198 · Pre-Seed 24. The Series A mass is dominated by
pre-2006 venture entries where "Series A" is the era convention (recorded at low confidence).

## C2A rebuilt on the corrected cohort

Old band-based cohorts mixed fake seeds (micro-filings) with mislabeled entries. The cohort is
now: true Sequoia seed entries with a determinable outcome — **41 of 87 graduated = 47.1%**
(sources: formd 41, model/named-deal 42, web 4). 111 further Seed entries are undetermined:
mostly 2024-26 vintages inside the 24-month censoring window, plus site-only seeds with no
filing trail. Documented graduations that predate Form D coverage now count (Airbnb, Stripe,
Dropbox, Nubank, Lemonade — all graduated), which is why the rate rose from the 36.9% of the
band-based cohort: the old denominator was polluted with never-graduating noise rows and the
old numerator missed the most famous seeds Sequoia ever did.
