# Calibration gate — First Round Capital (PRO-93)

Both sets pre-registered in `golden.json` on 2026-09-06, before the base was
built and before any verdict or `entry_stage` was written (COLLECTION.md §4).

## Layer scoring: the firm's own `initialPartnership`

First Round publishes its own entry-stage claim per company — `initialPartnership`
on the live Sanity CMS (195 rows: Seed 168, Pre-Seed 13, Series A 13) and
"Initial Partnership: &lt;stage&gt;" on the 2020-2024 archived WordPress accordion
(302 rows). It is the candidate class-1 layer for this investor, so §4 requires
it to be scored before the grind may treat it as a label.

**Score: 12/18 against the cited key.** The decomposition is the finding:

| Row | Firm label | Key (cited) | Direction |
|---|---|---|---|
| mint | Pre-Seed | Seed | understates by 1 |
| blue-apron | Seed | Series A | understates by 1 |
| flatiron-health | Seed | Series A | understates by 1 |
| bazaarvoice | Seed | Series A | understates by 1 |
| carbon-engineering | Series A | Growth | understates by 1 |
| wikia | Seed | Series A | understates by 1 |

**Every one of the six misses understates by exactly one step, and none
overstates.** That is not noise, it is the field's meaning: it records First
Round's self-description as the seed investor in the company rather than the
name of the round it actually bought into. Accel's CMS label scored 30/31 and
was promoted to class 1; this one scores 67% with a systematic one-directional
bias.

**Ruling (2026-09-06, class-wide, flagged for review): the field is a FLOOR,
not a label.**

1. It may never publish an `entry_stage` on its own. A row whose only stage
   evidence is `initialPartnership` carries the label at **low** confidence
   with `stage_prior`, and goes to the citation queue.
2. Read as a floor, it is sound: no row in the key entered *below* its label.
   So a label of "Series A" is affirmative evidence the entry was at Series A
   **or later**, and a `Growth` verdict over a "Series A" label needs no
   dispute flag.
3. Where the label says Seed or Pre-Seed and an independent source names a
   Series A or later round with First Round in it, **the record wins**, flagged
   `stage_disputes_band` with the citation. This is the Accel "socure class"
   in a new form: the CMS describes the company when it was listed, not the deal.
4. Where an independent source agrees with the label, the label is
   corroboration and the row publishes at the independent source's class.

The practical consequence for the grind: **Seed and Pre-Seed labels on rows
that are $1B+, public, or post-2020 are checked against the announcement
archive before they publish**, exactly as §8's Black Forest Labs rule requires
for band-sourced stages. That is where all six misses live.

## Membership trap set

33 rows: 23 traps and 10 known-true members across eras (`golden.json`).
Gate: zero false members at high confidence before any verdict writes.
Scored in the blind pass at the head of the grind; results appended below.

## Blind pass

Run at the head of the grind, judging the golden rows through the production
protocol from their queue evidence alone. Results appended here.

## Trap set — result

Scored 2026-09-06 against the built base, before any verdict was written.

- **17 of the 23 traps never reached the base.** The build's own structural
  filters removed them: fund-shaped LPs (`argand-partners-fund`,
  `sigma-/brintons-/poseidon-co-investment-holdings`, `chp-v-sd-co-invest`,
  `general-partnership`), personal Section 16 filings (`gsi-commerce`,
  `meet-group`), ex-partner tenure (`minerva-bi`, `layer-9-networks`),
  non-portfolio industry (`first-resource-bancorp`), and the five pre-fund
  angel names, which never entered because `/our_portfolio_prior.html` is
  deliberately not a configured listing surface (decisions.md D-T2a).
  Seventeen passes scored before the judge.

- **Two key rows were wrong and the evidence corrected them** (§4: scoring runs
  both directions). `augury` and `kentik` were written as post-tenure Howard
  Morgan seats. They are on **First Round's own portfolio site** — Augury in
  the 2014–2024 captures, Kentik in 2016–2024 — and a site listing suffices for
  membership on its own (§1 evidence sufficiency). Both are members; the key
  is corrected. The finding behind the correction matters more than the two
  rows: **Howard Morgan's First Round tenure runs past his last fund Form D
  (2012) to at least 2016**, so the seat-dating boundary for his cluster is
  the site captures, not the fund filings. Rows dated 2020 and later
  (`myndyou`, `retailerx`, `cargometrics`, `cornerup`,
  `precision-neuroscience`, `apptronik`) stay post-tenure.

- **Four traps survive into the base unjudged** and go to the blind pass:
  `apptronik-inc`, `precision-neuroscience-corp`, `campus-job-inc`,
  `posit-science-corp`.

- **All ten known-true members** seeded `member` on `site_listing`.

Gate: **zero false members at high confidence.** The two corrections were
key errors, not pipeline errors; no row was seeded `member` on evidence the
membership definition does not support.

The pre-fill also behaved as §8 requires: 669 rows seeded `member` on
`site_listing`, and every `formd_only` row (29) left unjudged for the grind.
That is the whole adjudication set, and every trap class in it —
post-tenure seats, founder-era seats, operator jobs, homonyms — is
represented.

## Layer scoring: Wikidata `hq_country` and `status` — DEMOTED

Found while reading `prepare`'s output before the grind (§8: a deterministic
pre-fill silently keeps the judge away from its row).

`prepare` matched 126 base rows to Wikidata and wrote `hq_country` on 104 of
them (81 more came from `formd_address`). **89 of those 104 rows have a
single-token name**, and First Round's book is full of one-word product names.
The joins are wrong at a rate no layer can survive:

| Row | Wikidata says | Reality |
|---|---|---|
| uber | NL | US |
| square | JP + defunct | US, public (Block) |
| clay | NL | US |
| planet | GR | US, public |
| parallel | AU | US |
| play | PL + acquired | US |
| free | FR + acquired | US |
| milk / medico / laurel / sprout | JP | US |
| noon | SA | US |
| togg | TR | US |
| superb | DK | US |
| snowball | CN | US |
| abra | GH + defunct | US |
| alma | CA + defunct | US, private |
| superhuman | "Ukraine[56]/ United States[57]" | US — and not even a country code |

This is the a16z weak-CIK-join class in a different layer, and it is worse
here because the collisions are with famous same-word entities, so a spot check
that recognises the *name* accepts the *wrong* row.

**Ruling (2026-09-06, class-wide): Wikidata is corroboration for this
investor, never a label.** Every Wikidata-sourced `hq_country` and every
Wikidata-sourced `status` is re-judged in the grind and corrected with
`model_disputes_source` where wrong — §8's sanctioned exception to "emit only
the keys the needs asked". `formd_address` countries (81 rows) stand: they are
filing-grade, with §6's entry-time caveat. The same treatment applies to the 94
`formd_band` entry stages, which §8 already requires to go back through the
judge on $1B+ and post-2020 rows.

Two by-products worth recording: the base carries `google`, `microsoft` and
`intuit` as rows — artifacts of the 2010-2011 logo wall, where the firm's own
upload filenames are the only names (decisions.md D-T5) — and they are exactly
the rows a name-matching layer will confidently mislabel. They are judged as
artifacts in the grind.
