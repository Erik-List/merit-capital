# Recall triage brief: EDGAR full-text candidates, PRO-100 NEA

You triage one shard of EDGAR full-text-search registrants whose filings name New Enterprise Associates (NEA) and
which the NEA company base does not yet carry. Work only in
`/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only your
output file `recall-fts-<SHARD>.json`. Never touch git or any other file.

## Read first
- `../documentation/decisions.md` (the boundary: D1 external entities incl. the IndoUS joint venture, NewView,
  Onset, CMEA; D3 venture entry; D8 sale consideration; X1 PIPEs).
- COLLECTION.md s1 "Evidence rules" (`../../../COLLECTION.md`, the section `### Evidence rules` up to `## 2.`).

## Your candidates
`python3 ftsview.py --shard <SHARD>` prints each registrant: forms, dates, filing URLs, and stored snippets naming
NEA. To read more of a filing: `python3 secget.py "<filing url>" --grep "New Enterprise Associates|NEA "` (throttled
and cached; never curl sec.gov directly). The base's names are in `../companies/base.json` (field `name`); check a
company there before calling it new (it may be listed under its brand or a later name).

## Decide each candidate (one entry per registrant; a registrant may yield extra `target` entries)
- `add`: the registrant ITSELF was an NEA venture position: a filing shows an NEA fund ("entities affiliated with New
  Enterprise Associates", "New Enterprise Associates 1x, L.P.", "NEA Partners") holding it through a PRIVATE round:
  an IPO prospectus principal-stockholder or certain-transactions table, a pre-IPO holder table, a merger proxy
  listing NEA among holders of a private company. Give the company's brand name, the filing URL as `citation`, the
  earliest year the record shows NEA holding it as `first_seen`, and a one-sentence `basis` quoting the filing.
- `target`: the NEA position is ANOTHER, private company named in the filing: an acquisition target whose holders
  are listed in the acquirer's S-4 or merger proxy (Ciena's 2001 S-4 lists NEA holding 9.7% of the target), or a
  company another registrant describes as NEA-funded. Give that company's name, the citation and the quoted basis;
  mark `in_base: true` if `base.json` already has it. The acquirer registrant itself is `reject` (sale
  consideration is not membership, D8).
- `pipe`: NEA bought into the registrant only after it was listed (a post-IPO private placement, a registered direct,
  a 13D reporting a purchase in a PIPE, a shelf resale prospectus listing NEA as a PIPE buyer) with no earlier
  private round in the record. X1 reads these as out; list them separately so the class is counted.
- `reject`: noise. A biography of a person who is or was at NEA with no NEA fund holding in the filing (look in
  the same filing's principal-stockholder table before rejecting: if NEA entities are listed there, it is `add`); a
  former NEA partner now elsewhere; an LP-side or fund-of-funds filing; a namesake (National Education Association,
  "NEA" as an unrelated abbreviation); an acquirer that paid NEA's portfolio company in stock; an entity D1 names
  external (IndoUS, NewView, Onset, CMEA, the feeders). Give the reason in `basis`.
- `uncertain`: the filing names an NEA partner as director and nothing ties an NEA fund to the company. Do not
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
