# Recall triage brief: EDGAR full-text candidates, PRO-80 Bessemer Venture Partners

You triage one shard of EDGAR full-text-search registrants whose filings name Bessemer Venture Partners (its funds
"Bessemer Venture Partners <numeral> L.P.", "Bessec Ventures", "BVP VII Special Opportunity Fund", the Century funds,
"15 Angels", the general partners "Deer <numeral> & Co.") and which the Bessemer company base does not yet carry.
Work only in `/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/`.
Write only your output file `recall-fts-<SHARD>.json`. Never touch git or any other file. The machine's disk is
nearly full: download nothing large.

## Read first
- `../documentation/decisions.md` (the boundary: D1 the vehicles; D2 BVP Forge, the buyout strategy, out; D3 the
  Bessemer namesakes: Bessemer Trust, Bessemer Securities, Bessemer Investment Management, Old Westbury, Lindsay
  Goldberg & Bessemer are OTHER businesses; D5 venture entry; D6 seats travel; D10 the anti-portfolio).
- COLLECTION.md s1 "Evidence rules" (`../../../COLLECTION.md`, the section `### Evidence rules` up to `## 2.`).

## Your candidates
`python3 ftsview.py --shard <SHARD>` prints each registrant: forms, dates, filing URLs, and stored snippets naming
Bessemer. To read more of a filing: `python3 secget.py "<filing url>" --grep "Bessemer|BVP|Bessec|Deer [IVX]+ & Co"`
(throttled and cached; never curl sec.gov directly). The base's names are in `../companies/base.json` (field `name`);
check a company there before calling it new (it may be listed under its brand or a later name).

## Decide each candidate (one entry per registrant; a registrant may yield extra `target` entries)
- `add`: the registrant ITSELF was a Bessemer venture position: a filing shows a Bessemer fund ("entities affiliated
  with Bessemer Venture Partners", "Bessemer Venture Partners VII L.P.", "Bessec Ventures V L.P.", "Deer VII & Co.
  L.P.", "15 Angels II LLC") holding it through a PRIVATE round:
  an IPO prospectus principal-stockholder or certain-transactions table, a pre-IPO holder table, a merger proxy
  listing Bessemer among holders of a private company. Give the company's brand name, the filing URL as `citation`, the
  earliest year the record shows a Bessemer fund holding it as `first_seen`, and a one-sentence `basis` quoting the filing.
- `target`: the Bessemer position is ANOTHER, private company named in the filing: an acquisition target whose holders
  are listed in the acquirer's S-4 or merger proxy, or a company another registrant describes as Bessemer-funded. Give that company's name, the citation and the quoted basis;
  mark `in_base: true` if `base.json` already has it. The acquirer registrant itself is `reject` (sale
  consideration is not membership, Erik 2026-09-22).
- `pipe`: Bessemer bought into the registrant only after it was listed (a post-IPO private placement, a registered direct,
  a PIPE into a de-SPAC merger, a shelf resale prospectus listing Bessemer as a PIPE buyer) with no earlier private round
  in the record. T3 reads these as out; list them separately so the class is counted. A SPAC the firm sponsored
  and its promote are out (T3 sponsor rule), unless a Bessemer fund held the target through a venture round first.
- `reject`: noise. A biography of a person who is or was at Bessemer with no Bessemer fund holding in the filing
  (look in the same filing's principal-stockholder table before rejecting: if Bessemer entities are listed there, it is
  `add`); a partner's outside directorship at a public company (Jeff Epstein at Booking, Kaiser, Twilio, Shutterstock, Poshmark or Okta; David Cowan, Byron Deeter or Jeremy
  Levine board bios are fine only where a Bessemer fund held the company); a former Bessemer person now elsewhere; an LP-side or fund-of-funds filing (N-PX, N-CSR); a law firm or accountant that merely names
  Bessemer as a client; an acquirer that paid Bessemer's portfolio company in stock (eBay for Skype, Okta for Auth0: name the acquired
  company as a `target`); a BVP Forge buyout (D2). (A position held only by Bessemer Trust, Bessemer Securities or an Old Westbury fund is `reject`: a namesake, D3.)
  Give the reason in `basis`.
- `uncertain`: the filing names a Bessemer partner as director and nothing ties a Bessemer fund to the company. Do not
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
