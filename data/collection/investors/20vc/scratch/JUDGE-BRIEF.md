# 20VC grind: judge brief (PRO-76)

Read `data/collection/COLLECTION.md` §1, §3, §6 and `documentation/decisions.md`
first. This brief only restates what bites on this book.

## Membership

- **The live list (20vc.fund, 79 cards) suffices** for membership (site_listing),
  unless the row's own evidence shows the only position is Harry Stebbings'
  personal check from before April 2020 with no 20VC vehicle after (D3), a
  Stride.VC position with no 20VC vehicle (D4), a Project Europe position (D5)
  or a partner's prior-firm deal (D8).
- **20VC's vehicles** (D1): Fund I (April 2020, $8.3M, US-focused, $100k–$300k
  checks alongside tier-1 leads), Fund II ($33M seed) + Explorer Fund II ($107M
  growth, $3M–$5M checks) from June 2021, Fund III ($125M seed) + Explorer
  Fund III ($275M Series A) from late 2024, SPVs S-1..S-5, D-1, SPV1/2. Any of
  them = IN. "20VC Growth" / "20 VC Explorer" = the Explorer growth fund, IN.
  **The 20Growth / 20Sales / 20Product offshoot funds are EXTERNAL** (D1:
  separate vehicles run by their operator partners): a company held only by
  one of them is `not_member`; with 20VC's own fund in the round it is a
  member on 20VC's position.
- **Press evidence** (class `web`): a sentence naming 20VC / "Harry Stebbings'
  20VC" / "The Twenty Minute VC" as an investor in a round. **R1:** a sentence
  naming only Harry Stebbings the person corroborates a row the firm counts as
  its own (its lists, or its own statements in TechCrunch 2020-07-17, Fortune
  2021-06-16, Business Insider 2024-06-13) and dates its entry; alone it is
  `not_member` (T4, person-level attribution). Before 2020-04 it is his angel
  book (D3).
- **Podcast sentences never count** (D7): "told 20VC", "on the 20VC podcast",
  "spoke to Harry Stebbings", "20VC x SaaStr", a founder's interview.
- Vendor lists (startupintros, Tracxn, Crunchbase, Dealroom) are candidates
  only; they cite nothing (Rule A applies to membership here by analogy: a
  vendor's investor list aggregates every investor the company ever had).

## Entry stage (the round 20VC first joined)

- Fund I can only enter from **2020-04**; Fund II from **2021-06**; Fund III
  from **2024**; an S-series SPV at its Form D first-sale date (S-1 2021-11,
  S-2 2025-07, S-3 2026-01, S-4 2026-02, S-5 2026-06).
- The press line naming 20VC in a round names the round: that is class 1
  (`web_verified`, citation = the article). Where 20VC is named only as an
  existing investor in a later round, the entry is earlier: look for the
  earlier round, else `undetermined` (or Growth if every round the funds could
  have joined is Series B or later: say so in the note, `model`, medium; a
  $1B+ row then carries `cite_pending`).
- Record `funding_rounds` for every row whose entry was researched (§6 form).
- Taxonomy: Pre-Seed / Seed / Series A / Growth (B and later, extensions of B,
  secondaries) / undetermined.

## Classification

- status, valuation_range (Rule A: vendor marks never band; a $1B+ band needs a
  priced round with a citable figure), hq_country (non-US on a $1B+/public row
  needs a citation), hq_city (bare municipality), focus (closed twelve).
- **Align with sibling books** (verify rule 10): same status and band as the
  other books holding the company (`scratch/siblings.json`), unless the
  sibling is stale and the fresher mark is cited; a name collision (Numeral,
  Sphere, Papaya, Context, Pearl, allO, District, Entire) is ruled `distinct`
  in `companies/cross-rulings.json`.
- S2A: every Seed entry gets graduated / not_graduated / censored; entries
  after 2024-09-28 are censored unless a later named round already exists.
