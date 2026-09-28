# Judge brief: PRO-77 Sutter Hill Ventures, queue batches

You judge the rows of ONE queue batch of the Sutter Hill Ventures (SHV) company base: membership where it is
still open, then every open classification column of each member, written as a Python judgments file that
records itself. Work only inside
`/Users/erik/Developer/merit-capital/data/collection/investors/sutter-hill-ventures/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<N>.py` (and let it write its `queue/batch-<N>.out.jsonl` through `jl.write`).
- Set `export NQ_TAG=b<N>` in EVERY shell command that runs `nq.py` or your judgments file (e.g.
  `NQ_TAG=b7 python3 nq.py ...`, `NQ_TAG=b7 python3 judgments-7.py`). Other judges run in parallel; the tag keeps
  your news caches separate. `record` is lock-safe.
- WebSearch: at most 10 calls in total. Prefer `nq.py` (Google News, uncapped, throttled machine-wide) and
  `wikifetch.py` (Wikipedia plain text). WebFetch of a company's own site, an SEC filing or a press page is fine.
- Never type a citation URL by hand except an SEC URL copied from the row's own `formd_links`/`edgar_links` in
  `../companies/base.json` (use `SEC(slug)`), or a URL printed by a tool you ran. Use the helpers (they refuse a
  missing or ambiguous match).
- Notes are plain prose. Never use em-dashes (use commas, semicolons, parentheses). Say "inferred", never "prior";
  "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. This file.
2. `judge_lib.py` (the line builders `verdict`, `cls`, `rnd`, `write`, and the citation helpers `ARCH`, `W`,
   `NEWS`, `SEC`, `FORMD_ROUNDS`, `FORMD_CITE`, `GRADLINES`).
3. `../documentation/decisions.md` (D1 to D9 and any run-time rulings).
4. `../../../COLLECTION.md` section 6 "Classification columns" and section 1 (the tests T1 to T5, evidence rules).
   Skim; come back when a row raises a question.

## Your rows
`python3 show.py --batch <N>` prints each row: its `need` list (the columns still open), what is already `known`
(prefilled by the deterministic layers; do not repeat a known value unless you dispute it with evidence), the
firm's archived listings (`archive:` years, the 1999 table's own OUTCOME line, the company page's description,
the 2013 list's managing director), every related person on the row's Form Ds with roles and whether they filed
from the firm's own address (`FIRM ADDR` = 755 Page Mill Road), SHV's own ownership filings (`edgar:`), EDGAR
full-text sentences (`fts:`), Wikipedia sentences, press headlines naming the company, and sibling investors'
rows for the same company (`sib`).

## Membership (when `membership` is in `need`)
- A listing on the firm's own archived site (any year) suffices alone (`site_listing`, high), unless the listing is
  in the firm's "Investment Partnerships" category or is otherwise a fund (decisions D6: `not_member`, T5).
- An SEC filing by a Sutter Hill vehicle (SHV itself, CIK 879051, the Entrepreneurs Funds, Sutter Hill Associates)
  about the company suffices (`fund_filing`). A partner's own Form 3/4 locates the PERSON (T4), unless its footnote
  puts the shares in the partnership ("Shares held by Sutter Hill Ventures, a California Limited Partnership").
- A Form D name-match NEVER suffices alone. Corroboration: the partner filed from 755 Page Mill Road in tenure and
  the issuer resolves to a real company (director-of-record pattern: `member`, `formd_adjudicated`, medium), a
  documented round naming SHV, or an SHV filing. A partner's seat before joining or after leaving SHV is not
  SHV's (seat dating, D5): Greg Sands at Costanoa from 2012 (160 Forest Avenue), Ron Bernal at Sequel from 2006
  and NEA from 2010, Stefan Dyckerhoff's Juniper years, Jim Gaither's Cooley years. Homonyms (David Anderson,
  James White, David Sweet at unrelated addresses) are `not_member` with the address as the basis.
- Sale consideration (the SHV filing is on the ACQUIRER of an SHV company: Emcore for K2 Optronics, USANA for
  BabyCare/Yaolan, TeleCommunication Systems for Networks In Motion, Uniti for Tower Cloud) is `not_member`, with the
  acquired company named (COLLECTION.md s1).
- A company only a partner's personal vehicle held is out (D2).
- `uncertain` only when identification is genuinely open after corroboration was tried.
A member needs TWO lines: `verdict(...)` and `cls(...)`.

## Prefilled stages on $1B+ and public rows (check them even when `entry_stage` is not in `need`)
`prepare` prefills a Form D band (`formd_band`) from the company's first filing. For every row in your batch that
is public or `1b_plus` and up (see `known`), and for every post-2020 row, check that stage against the record
(the S-1's preferred stock history on EDGAR, the company's or the firm's announcement) and dispute it with
`stage_disputes_band` and a citation when the record names a different round. Sutter Hill's incubations often
file a tiny first Form D (founders' or a first close) that bands as `Pre-Seed`, while the round SHV bought is
named Series A in the S-1 (Snowflake, Pure Storage). `Pre-Seed` from a band is only kept where the record agrees.

## The classification contract (COLLECTION.md s6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take `rng="below_1b"`
  and no usd. An asset sale out of a wind-down reads acquired; a shutdown reads defunct; a merger into another
  company reads acquired (IPO'd then acquired reads acquired). `unknown` when no source gives the fate (say so).
  The 1999 table's outcome line is the firm's own 1999 statement: corroboration, and it names acquirers.
- `valuation_range`: below_1b | 1b_plus | 10b_plus | 100b_plus. A band from 1b_plus up needs `usd`,
  `val_src="web_verified"`, `val_cite`, `asof` and `extra={"valuation_range_source": "web_verified"}`. Rule A:
  vendor estimates never band a row. Public companies: market cap with citation and as-of. A private mark older
  than 24 months (asof before 2024-09-28) carries the flag `stale`. Private rows first seen 2021 or later in hot
  sectors (AI, fintech, data infrastructure, dev tools, security) get one web check for a $1B+ priced round
  (momentum slice); write the outcome in the note either way.
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined (Series B and later read Growth). Sources:
  `web_verified` (a citation naming the round and SHV's part in it, or dated to SHV's entry: an S-1's preferred
  stock history, a press release), `formd_structural` / `formd_band` (prefilled; dispute only with a documented
  round, flag `stage_disputes_band`), `model` (a named deal in the note, high/medium confidence). **Incubations
  (D3):** SHV formed the company and its fund bought the first preferred round; the stage is what the record calls
  that round (Snowflake's S-1: Series A), never Pre-Seed, and the partner's founder shares are not the entry.
  When the round cannot be named, `stage="undetermined"` (no source keys). No date excuses an empty stage.
  Record the funding history you found in `rounds=[rnd(...)]` whenever you research a round (s6 PRO-143).
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided.
- `seed_to_a_graduation` only for Seed entries: `graduated` needs a cited later round (`grad_src` web_verified or
  first_party, `grad_cite`, `entry_date`); `censored` when the entry is after 2024-09-28; otherwise leave it for the
  graduation pass (note "Graduation left for the graduation pass."). Never write `not_graduated` in the grind.
- `hq_country`: ISO alpha-2; non-US needs `country_src="web_verified"` and `country_cite`. Prefilled Wikidata
  countries on one-word names are often wrong joins: dispute with evidence.
- `hq_city`: bare municipality ("Palo Alto", never "Palo Alto, CA"); `city_src` model_knowledge (default),
  formd_address or web_verified. Unplaceable: omit and add flag `city_unknown`. Current HQ for live companies, last
  known for dead or acquired.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising (chips are Industrial & Robotics; networking and storage are Data Infrastructure).
  Give it on every member you classify; null only if it fits none.
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib`, rule 10): the same company at another investor must agree on status, valuation band and mark,
  country and city unless you hold fresher cited evidence (say so). A sibling that is plainly a different company
  with the same name is a collision: do not align, list it in your report.

## Finish
1. `NQ_TAG=bN python3 judgments-N.py` must print `recorded ...`. On `REJECTED`, fix and re-run.
2. Report back in under 250 words: rows judged (members / not_member / uncertain), verdicts worth a second look,
   sibling name collisions, rows left `unknown` or `undetermined` that a later pass could settle, WebSearch calls
   used, and anything that looked wrong in the base (two rows that are one company: name both slugs).

## Delta after the rebuild (read this if your batch is a delta batch)
- **Recall additions** carry a base note "recall addition: <basis> (<citation>)". Each was verified against a page that
  names Sutter Hill. Verdict `member`, `ec="web"`, `conf="high"` (medium for Cipher Data Products, whose only source is
  Wikipedia), `cite=` the URL inside the note. Then classify as usual; the note often names the round SHV entered.
- **New Form D rows from three people added to the roster:** Brian Blond (at SHV about 2021 to 2022; at Human Capital by
  May 2023, so Toolkit, Inc. and Datawizz Inc. (2025) are `not_member`, seat dating), Victor Miller (Neos Therapeutics,
  BlueCava, Orgenesis are his seats from before SHV: `not_member`; Luminary Cloud and Matic Robots are SHV companies),
  Chad Peets (Sigma Computing, already a member).
- **Leibniz Data Systems** (2021 Form D): both founders are executive officers filing from SHV's own suite (Bldg A 200,
  755 Page Mill Road) and Brian Blond (SHV) is a director: the incubation marker of D3 plus a director of record in
  tenure. `member`, `formd_adjudicated`, medium, cite the Form D (a CB Insights page is a vendor and may not cite).
- **IA-era rows** (the firm's 2000 to 2007 pages) are listed members (`site_listing`, seeded); classify them. The row's
  description holds the page's text, often with the firm's own outcome line ("acquired by ...").
