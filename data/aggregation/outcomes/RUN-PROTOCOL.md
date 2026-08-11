# Outcome run protocol — Sequoia Capital, pinned base 63c4bc30

This file is the run's constitution. If context is compacted mid-run, re-read
this file and `python3 scripts/outcome-run.py status`, then continue at the
first pending batch. Do not re-derive rules from memory.

## What is being decided per row

Two judgments, recorded as JSONL (one object per row) in
`queue/batch-NNN.out.jsonl`, then `python3 scripts/outcome-run.py record <file>`:

* **Valuation** (rows with `"valuation"` in `need`): current status and, only via
  an allowed source, a current dollar figure.
* **Graduation** (rows with `"graduation"` in `need`): the investor's entry stage
  and whether a later round followed (C2A).

**Emit only the keys for the needs asked** (plus `flags`, `note`, optional
`country`). Extra keys clobber filing-grade facts at merge time. The one
exception is a deliberate dispute (below).

## Hard rules (enforced by `record`, do not fight them)

1. `status` ∈ private | public | acquired | defunct | unknown. Current-state:
   IPO'd-then-acquired → acquired. Successor-entity ambiguity → acquired + note.
2. `valuation_usd` non-null requires `valuation_source` ∈
   {sec_public_float, wikidata, unicorn_list, web_verified} AND status
   private/public. `model_knowledge` never carries a figure: if I believe a
   company is ≥$1B without a source, I claim status private, leave the figure
   null, flag `needs_web_value`, and the web pass pins it or kills it.
3. `seed_to_a_graduation` non-null requires `entry_stage: "Seed"`.
4. Acquired / defunct / unknown → `valuation_usd` null.

## Judgment rules

* **Recognition check before trust.** Before using knowledge of a name, confirm
  the row's evidence fits it: era (`first_seen`, `wayback_years`), `sector` tag,
  round sizes. A mismatch means it is a different company with the same name →
  treat as unrecognized, flag `identity_uncertain`.
* **Rule-outs are legitimate.** An unrecognized company, absent from the unicorn
  list, with small/old rounds and no recent trace, is sub-$1B with high
  probability. Recognized-dead → defunct; recognized-acquired → acquired + note
  "acq. by X, YEAR"; unrecognized-with-recent-evidence-of-life → private;
  unrecognized-and-dark → unknown + note. Notes must be specific, one line.
* **Pre-2006 legacy holdings** (Apple, Cisco, EA, Atari-era rows): entry precedes
  the base window → `entry_stage` null, graduation null, note "pre-window".
* **Confidence:** high = filing-grade or common-knowledge-stable or strong
  multi-signal rule-out. medium = recognized but facts may have moved post
  May-2026 cutoff; name-matched external list. low = genuinely uncertain → the
  claim must not publish a bucket; prefer status unknown.
* **Disputes.** When knowledge contradicts a deterministic layer (e.g. float
  series says public but the company was acquired after its last filing),
  record a classification row carrying the corrected keys + flag
  `model_disputes_source` + note. Never silently accept a value I know is wrong,
  never silently override either.
* **Layer-A assist.** If a row is recognizably a US-listed company that Layer A
  missed on a name mismatch, resolve its CIK by ticker and fetch the float
  directly (deterministic, manually keyed) rather than claiming from memory.

## Standing verification duties (after the grind, before verify-clean)

1. **Web-verify every $1B+ claim** regardless of source, including the 43
   unicorn_list matches. Confirm identity (is the base row this company?) and
   current status. Update figure + `valuation_asof` with source `web_verified`
   where the search moves it; downgrade to sub-$1B/private where it kills it.
2. **Vet Form D graduation False against reality.** A `seed_to_a_graduation:
   false` on a company that is now ≥$1B, public, or known to have raised an A is
   a Form D blind spot (4(a)(2), foreign). Dispute those to true with
   graduation_source model/web. Cross-check: no row may end
   `false` + (valuation ≥$1B or is_public).
3. **Audit every `cik_weak` row** encountered: does the matched registrant's
   float/company actually fit the row? The known false-join: base `linear` (the
   software company) ↔ LINEAR TECHNOLOGY (semiconductor, acq. Analog 2017) via
   suffix-stripped norm collision.
4. **Self-consistency:** re-classify a random 5% blind at the end; disagreements
   flagged `unstable`, adjudicated, counted in the report.

## Duplicates (18 groups, flagged, do not "fix")

Same SEC registrant under two base rows: 17 genuine renames (10Gen→MongoDB,
Evenflow→Dropbox, Square→Block, SourceForge/VA lineage, Bit9→Carbon Black,
Widgetbox→Flite, Turin→Force10, Rearden→Deem, Arbor→Hyperion, HQC→Health
Catalyst, Qadium→Expanse, Network Appliance→NetApp, Service-now.com→ServiceNow…)
plus one false join (`linear`). Rows stay flagged `duplicate`; membership is the
human's call; derivation excludes flagged rows and says so.

## Batch loop

Read 2 batches → judge every row → Write both `.out.jsonl` → `record` both →
one-line progress in chat → next pair. Progress lives on disk; `status` is the
resume point. Track nothing in context that disk already knows.

## Calibration results (measured 2026-08-11, 40 blind rows vs filing-grade key)

Status 35/40 (88%), full 34/40 (85%). Decomposition: 3 key defects caught by
model knowledge (23andme dead-but-recent-float; google stale->acquired misfire
on the Alphabet reorg; apollo false CIK join, actually Apollo.io private ~$1.6B),
1 threshold boundary (crowdstrike $109B float), 1 humble unknown on a real
micro-cap (positron), 1 open (rackspace re-IPO lineage -> web).

Added vet-pass duties:
5. Sweep every stale->acquired row for holding-co reorgs and re-IPOs (Google ->
   Alphabet CIK 1652044-style successor floats; fetch successor float directly).
6. Sweep public rows with floats 12-24 months old for known deaths (23andme).
7. Re-intersect the unicorn list with loose normalization (strip .io/.ai/.com,
   "HQ", "Labs") to catch Apollo.io-style misses.
