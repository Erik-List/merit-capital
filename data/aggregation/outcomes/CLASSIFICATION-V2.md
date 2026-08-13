# Classification v2 constitution

Adversarial second pass over three published columns: `valuation_usd (+asof)`,
`entry_stage`, `country`. Extends ENTRY-STAGE.md and MEMBERSHIP.md; base-v2
rigor applied column-wise. Erik's rulings, 2026-08-13:

## 1. Valuation

- **Public companies: market capitalization is canonical**, web-cited with an
  as-of date (`valuation_source: web_verified`, `valuation_citation` URL).
  SEC public float remains corroborating evidence only; a public $1B+ row
  without a cited cap FAILS verify.
- **Private companies**: last credible primary-round mark stays canonical
  (run-2 policy), `stale` flag beyond 24 months. Secondary-market estimates
  are recorded in the note, never as `valuation_usd`. The attack pass searches
  stale marks for newer rounds, down rounds, and exits.
- **below_1b rule-outs**: web-checked only on a signal (past unicorn mark,
  mega-raise, hot sector, recent momentum); otherwise validated by a blind
  stratified re-judge sample. Absence claims are not citeable at scale.

## 2. Entry stage

ENTRY-STAGE.md governs. Citation attempted for every row in priority order
($1B+ incl. IPO, then recents, then the tail); `stage_uncited` marks attempted
failures. C2A cohort keeps model-medium rows flagged `cohort_unverified`.

## 3. Country

Entry-time-first hierarchy stands (formd_address > wikidata > model). The
adversarial pass cites country for the visible slice (`country_citation`) and
for every non-US claim (the map's interesting rows); the US mass is validated
by the same blind sample.

## 4. The two-pass structure

Applied to the **visible slice** ($1B+ or currently public): pass A defends
each recorded value (find the confirming source), pass B attacks it (search
for the newer round, the acquisition, the down round, the wrong stage, the
relocated HQ). Agreement with citation closes the row; disagreement is
arbitrated by a targeted search; what survives goes to the sampling sheet.
Elsewhere: one rigorous cited pass, sampling as the default review element.

## 5. Verify invariants (additions)

1. `is_public` and `value_tag >= 1b_plus` implies `valuation_citation` present.
2. Non-US country on a visible row implies `country_citation` or
   `formd_address`/`wikidata` provenance.
3. Standing invariants from runs 1-3 unchanged.
