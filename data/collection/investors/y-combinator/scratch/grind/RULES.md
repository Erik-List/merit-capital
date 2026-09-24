# YC grind — judging `status` and `valuation_range`

You judge rows of Y Combinator's company base. Two columns only: `status` and
`valuation_range`. Everything else is already filled and you must not emit it.

## Output

One JSON object per line (JSONL), one line per input row, to the output path
you were given. Emit ONLY keys you are answering. Never invent keys.

    {"slug":"<exact slug from the input>","status":"...","valuation_range":"...",
     "valuation_confidence":"high|medium|low","flags":[...],"note":"one line"}

`slug` must be copied exactly from the input row. Do not rename, re-derive or
guess it. **Identity is the slug, never the name** — YC has 89 names borne by
two different companies (Parse S11, the Facebook-acquired backend, is a
different company from Parse F25).

## status — one of: private | public | acquired | defunct | unknown

Current state only. IPO'd-then-acquired is `acquired`.

The input carries `dir_status`, YC's own directory value (Active / Inactive /
Acquired / Public). **It is corroboration, not a label** — measured at 67.5%
against companies already judged in other bases. Use it like this:

- `Public` -> `public`. Reliable.
- `Acquired` -> `acquired`. **A company the acquirer later shut down is still
  `acquired`** — the acquisition is the outcome, and `defunct` is reserved for
  businesses that ended *without* one (SAP Concur buying Hipmunk in 2016 and
  retiring the product in 2020 is `acquired`, with the shutdown in the note;
  Ford buying Chariot and closing the service is `acquired`). Insolvency
  followed by an asset sale is also `acquired`, with a successor note. Use
  `defunct` only where there was no acquisition at all. A bankruptcy filing
  with no sale yet reads `defunct`.
- `Active` -> `private`, unless you positively know it was acquired or died
  (the field is stale in that direction: it reads Active for 35 acquired and
  21 defunct companies in the measured sample).
- **`Inactive` is NOT `defunct`.** Measured: it lands as private 41 times and
  unknown 28 times against only 27 defunct. Use `defunct` only when you
  actually recognise the company as dead or the evidence says so. Otherwise
  `unknown`. This is the single most common way to get this column wrong.

Where you genuinely do not recognise the company (most of this list is
obscure seed-stage startups, and that is expected): a dark row with no recent
trace is `unknown`, not `defunct`. Do not manufacture certainty.

## valuation_range — one of: below_1b | 1b_plus | 10b_plus | 100b_plus

- **`below_1b` is the only band you may assert without a dollar figure.** For
  the overwhelming majority of these rows it is the correct answer: an
  unrecognised seed company with no recent trace is sub-$1B with high
  probability, and that rule-out is legitimate.
- **Any band at or above `1b_plus` REQUIRES a sourced figure in the same
  line.** When you can cite one, emit all four together:

      "valuation_range":"1b_plus","valuation_usd":1600000000,
      "valuation_source":"web_verified","valuation_asof":"2023-08-15",
      "valuation_citation":"https://..."

  `valuation_usd` is a bare number (no commas, no "$"), `valuation_asof` is
  YYYY-MM-DD, and the citation must be a real URL naming that figure. The
  record step REJECTS a band above `below_1b` that has no figure, and a
  rejected line takes the whole batch down with it.
- If you believe a company is worth $1B+ but have **no** citable figure, emit
  `valuation_range: "below_1b"` **plus** `flags: ["needs_web_value"]` and say
  why in the note. A later pass pins or kills it. Never mint a figure, and
  never emit `valuation_usd` on a `below_1b` row.
- `valuation_usd` is allowed **only** when `status` is `private` or `public`.
  An `acquired`, `defunct` or `unknown` row carries no figure.
- A **vendor** valuation (PitchBook, CB Insights, Tracxn, Dealroom, Sacra,
  Forge, Caplight...) never bands a row. A $1B+ band needs a priced round,
  tender or public float with a citable figure from the company, a filing or
  the press.

## Confidence and notes

`valuation_confidence`: `high` for filing-grade or common-knowledge-stable;
`medium` for recognised but possibly moved past your knowledge; `low` for
genuinely uncertain. Notes are one specific line ("acq. by Stripe, 2023"),
never boilerplate.

## Flags to use where they apply

`needs_web_value` (believed $1B+, no citable figure) · `identity_uncertain`
(the row's evidence does not fit the company you are thinking of — era, sector
and round sizes must match before you trust a name) · `stale` (your figure is
older than 24 months).

## Two rows with the same name are NOT a duplicate

This base deliberately contains 89 names borne by two different companies in
different batches, each with its own YC id, and they are separate rows on
purpose. Before you call anything a duplicate, compare the `one_liner`,
`batch` and `team_size` the input gives you — they will usually differ
obviously. A real example that already fooled one judge: `alex` (Fall 2024,
"The Cursor for Xcode", team 3) and `alex-com` (Winter 2024, "Your AI
recruiter...", team 30) are two unrelated companies.

Judge each row on its own evidence. Never write a note claiming two rows are
the same company, and never copy one row's answer onto another because the
names match.

## The one rule that matters most

**Recognition check before trust.** Before using knowledge of a name, confirm
the row's evidence fits it: batch year, sector tag, team size. A mismatch
means a different company with the same name. Treat it as unrecognised and
flag `identity_uncertain`. Being wrong here is worse than answering `unknown`.

## Other columns some rows ask for

A row's `need` list may also contain `hq_country` or `entry_stage`. These
appear only on rows the directory has no record for, so answer them from the
row's own evidence.

- **`hq_country`**: ISO 3166-1 alpha-2 (`US`, `GB`, `IN`, `NG`...). Emit
  `hq_country_source` alongside — one of `model_knowledge` or `web_verified`.
  If you genuinely cannot place the company, omit the key rather than guess.
- **`entry_stage`**: for a YC company this is **`Seed`** — the batch investment
  is the entry, and YC's own sustained language calls it seed funding. Emit
  `entry_stage_source: "web_verified"` with
  `entry_stage_citation: "https://www.ycombinator.com/deal"`. The only
  exceptions in this whole base are the two `ycc_only` rows (Convoy and Monzo
  Bank), which are `Growth` — YC Continuity growth rounds into companies that
  never went through a batch. `Pre-Seed` and `Series A` are structurally empty
  for this investor; never emit them.

---

## Note for the run operator (not the judge)

**Never delete `*.out.jsonl` when regenerating batch inputs.** Regeneration
deletes and renumbers the input files; if an agent is still working, or has
finished and not yet been recorded, its output is destroyed with them. This
happened twice on this run — once orphaning a batch into a renumbered file,
once losing 380 judged rows outright. Regeneration must delete only
`(prio|tail)-NNN.json`, record every existing `.out.jsonl` first, and ideally
name each wave's outputs distinctly so a later wave cannot overwrite them.
