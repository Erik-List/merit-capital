# Recall triage brief: EDGAR full-text candidates, PRO-99 Kleiner Perkins

You triage one shard of EDGAR full-text-search registrants whose filings name Kleiner Perkins (Kleiner Perkins Caufield
& Byers, KPCB) and which the Kleiner Perkins company base does not yet carry. Work only in
`/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch/`. Write only your
output file `recall-fts-<SHARD>.json`. Never touch git or any other file.

## Read first
- `../documentation/decisions.md` (the boundary: D1 the vehicles; D2 Bond, external from 2018-09; D4 venture entry;
  D5 seats travel; X1 KPCB China, provisionally IN except Tina Ju's pre-2007 TDF deals).
- COLLECTION.md s1 "Evidence rules" (`../../../COLLECTION.md`, the section `### Evidence rules` up to `## 2.`).

## Your candidates
`python3 ftsview.py --shard <SHARD>` prints each registrant: forms, dates, filing URLs, and stored snippets naming
Kleiner Perkins. To read more of a filing: `python3 secget.py "<filing url>" --grep "Kleiner Perkins|KPCB"`
(throttled and cached; never curl sec.gov directly). The base's names are in `../companies/base.json` (field `name`); check a
company there before calling it new (it may be listed under its brand or a later name).

## Decide each candidate (one entry per registrant; a registrant may yield extra `target` entries)
- `add`: the registrant ITSELF was a Kleiner Perkins venture position: a filing shows a KP fund ("entities affiliated
  with Kleiner Perkins Caufield & Byers", "Kleiner Perkins Caufield & Byers XII, LLC", "KPCB Holdings, Inc., as
  nominee", "KPCB Digital Growth Fund") holding it through a PRIVATE round:
  an IPO prospectus principal-stockholder or certain-transactions table, a pre-IPO holder table, a merger proxy
  listing KP among holders of a private company. Give the company's brand name, the filing URL as `citation`, the
  earliest year the record shows a KP fund holding it as `first_seen`, and a one-sentence `basis` quoting the filing.
- `target`: the KP position is ANOTHER, private company named in the filing: an acquisition target whose holders
  are listed in the acquirer's S-4 or merger proxy, or a company another registrant describes as KP-funded. Give that company's name, the citation and the quoted basis;
  mark `in_base: true` if `base.json` already has it. The acquirer registrant itself is `reject` (sale
  consideration is not membership, Erik 2026-09-22).
- `pipe`: KP bought into the registrant only after it was listed (a post-IPO private placement, a registered direct,
  a PIPE into a de-SPAC merger, a shelf resale prospectus listing KP as a PIPE buyer) with no earlier private round
  in the record. T3 reads these as out; list them separately so the class is counted. A SPAC the firm sponsored
  and its promote are out (T3 sponsor rule), unless a KP fund held the target through a venture round first.
- `reject`: noise. A biography of a person who is or was at Kleiner Perkins with no KP fund holding in the filing
  (look in the same filing's principal-stockholder table before rejecting: if KP entities are listed there, it is
  `add`); a partner's outside directorship at a public company (Ray Lane at HP, John Doerr at Google/Amazon board
  bios are fine only where a KP fund held the company); a former KP partner now elsewhere (Khosla Ventures, Bond,
  Radar Partners); an LP-side or fund-of-funds filing (N-PX, N-CSR); a law firm or accountant that merely names
  KP as a client; an acquirer that paid KP's portfolio company in stock; a Bond-only position. (A KPCB China fund position is IN under X1's provisional reading: `add`, with `"kpcb_china": true` in the row.)
  Give the reason in `basis`.
- `uncertain`: the filing names a KP partner as director and nothing ties a KP fund to the company. Do not
  guess; say what is missing.

Keep each registrant to at most about 4 tool calls. No WebSearch unless a filing is ambiguous and one search settles
it (at most 5 WebSearch calls for the whole shard; the session shares a budget of 200). WebFetch of a company's own
page or a press release is fine.

## Output
`recall-fts-<SHARD>.json`: `{"shard": N, "rows": [{"registrant", "decision": "add"|"target"|"pipe"|"reject"|"uncertain",
"company" (brand name for add/target), "citation", "first_seen", "basis", "in_base" (bool, for target),
"listed_year" (IPO year if known), "confidence": "high"|"medium"|"low"}]}`. Every candidate in your shard gets one
row. Write the file incrementally (after every ~20 registrants) so progress survives.

Report back in under 200 words: counts per decision, the adds and targets by name, and anything that looked like a
boundary question (a class of rows, not one row).
