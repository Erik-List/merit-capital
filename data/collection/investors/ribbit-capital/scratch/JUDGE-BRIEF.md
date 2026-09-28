# Judge brief: PRO-161 Ribbit Capital, classification batches 1-5

You classify the member rows of ONE queue batch of the Ribbit Capital company base, write them as a Python
judgments file, and record it. Work only inside
`/Users/erik/Developer/merit-capital/data/collection/investors/ribbit-capital/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<N>.py` (and let it write its `queue/batch-<N>.out.jsonl` through `jl.write`).
- Set `NQ_TAG=b<N>` in EVERY shell command that runs `nq.py` or your judgments file (e.g.
  `NQ_TAG=b3 python3 nq.py ...`, `NQ_TAG=b3 python3 judgments-3.py`). Other judges run in parallel; the tag keeps
  your news caches separate.
- WebSearch: at most 15 calls in total (the session has one shared budget). Prefer `nq.py` (Google News, uncapped,
  throttled machine-wide), `wikifetch.py` (Wikipedia plain text) and WebFetch of a company's own page or a press page.
- Never type a citation URL by hand except an SEC URL copied from the row's own `formd_links`/`edgar_links` in
  `companies/base.json`, a URL printed by a tool you ran, or a page you fetched and read. Prefer the helpers (they
  refuse a missing or ambiguous match).
- Notes are plain prose. Never use em-dashes (use commas, semicolons, parentheses). Say "inferred", never "prior";
  "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. `JUDGE-BRIEF.md` (this file).
2. `judgments-0.py`: the exact pattern (imports, `cls`, `rnd`, citations, notes).
3. `judge_lib.py` (the helpers: `cls`, `verdict`, `rnd`, `SITE`, `ARCH`, `W`, `NEWS`, `FORMD_CITE`, `SPV`).
4. `../documentation/decisions.md` (D1-D8).
5. `../../../COLLECTION.md` section 6 "Classification columns" (lines 1231-1900). Skim; come back when a row raises
   a question.

## What this firm publishes (and does not)
Ribbit's own surfaces give membership and very little else: the live Rebels list (name, founders, the company's
URL), and the archived lists (2012-2014 "Bets" with a one-line description, 2015-2025 "Our Bets" with the
company's URL and the firm's own COUNTRY label). No year, no stage, no status, no sector, and the site has no posts.
So the entry round comes from the press, the company's own announcements, Wikipedia, Form D sequences and the
firm's single-deal vehicles (`spv` lines).

## Your rows
`python3 show.py --batch <N>` prints each row: its `verdict` (classify only `member` rows; skip `not_member`), its
`need` list (the columns still open), what is already `known` (pre-filled; do not repeat a known value unless you
dispute it with evidence), the live listing (`site (Rebels)`), the archived listing (`archive:` years, link, country
label, 2012-2014 description), the firm's deal vehicles decoded to this company (`spv` lines: code, filing quarter,
dollars sold, the round the code names), the adviser's 13F lines, EDGAR full-text and Wikipedia sentences, the
Google News sweep `"<company>" "Ribbit Capital"` (`news` lines, dated), and sibling investors' rows (`sib`).
Rows already in `../companies/classification.json` from an earlier batch need nothing.

## Tools
- `NQ_TAG=bN python3 nq.py <slug> '"Company" query words' [--all]`: Google News; items land in
  `news-extra-bN.json` under that slug and become citable with `NEWS(slug, "unique title substring")`.
  `NEWS(slug, sub)` also cites any headline of the row's sweep (the `news` lines).
- `python3 wikifetch.py "Title" ... --grep "ribbit|headquart|acquir|series|valuation"`: caches the article so
  `W("Title")` can cite it (an article from the insource sweep is citable already).
- `SITE(slug)`: the live Rebels list (membership only). `ARCH(slug)`: the row's first archived listing capture.
- `SPV("RH-D")`: the Form D index of one of the firm's deal vehicles (fund-filing evidence that a Ribbit vehicle was
  in THAT round; never the entry round by itself, decisions.md D6).
- `FORMD_CITE(slug, i)`: the index URL of round i in the company's own Form D sequence.

## The contract (COLLECTION.md section 6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take
  `rng="below_1b"` and no usd. A merger into another company reads acquired from the CLOSING (a signed, unclosed deal
  is a mark, not a status change); insolvency then an asset sale reads acquired; a shutdown reads defunct; a
  bankruptcy filing with no sale yet reads defunct. `unknown` when no source read gives the fate (say so).
- `valuation_range`: below_1b | 1b_plus | 10b_plus (usd >= $10B) | 100b_plus (>= $100B). Any band from 1b_plus up needs
  `usd`, `val_src="web_verified"`, `val_cite`, `asof` (YYYY-MM or YYYY-MM-DD) and
  `extra={"valuation_range_source": "web_verified"}`. Rule A: vendor estimates (PitchBook, Crunchbase "estimated",
  Tracxn, CB Insights, Forge) never band a row; it takes a priced round, tender, listing or acquisition price with a
  citable figure (a vendor's news arm reporting a priced round is press). A private mark older than 24 months (asof
  before 2024-09-28) carries the flag `stale`. Non-USD figures convert at the ECB rate of their own date
  (`python3 ../../../../../scripts/fx-convert.py`), the note keeps the original. PUBLIC $1B+ rows: leave the cap to
  the A/B pass (write status public and nothing else about the value unless `valuation_range` is asked and the known
  float band is plainly wrong).
- Momentum slice (Erik's rule): every PRIVATE row first seen 2021 or later in fintech, crypto, AI, data or dev tools
  gets one web check for a $1B+ priced round (the news lines usually settle it; `nq.py` otherwise). Write the check's
  outcome in the note either way ("no round at or above $1B found, news sweep 2026-09-28").
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined. Series B and later read Growth (a secondary or a
  tender is Growth). Sources: `web_verified` (a cited round naming Ribbit, or the company's own announcement listing
  Ribbit), `model` (a named deal in the note, e.g. "Ribbit joined the 2016 Series B", confidence medium or high), or
  the prefilled `formd_band` / `formd_structural` (dispute only with a documented round, then flag
  `stage_disputes_band`). An `spv` line proves Ribbit was in THAT round, not that it was the first: use it as the entry
  only when the press says Ribbit first invested there, or no earlier Ribbit round exists and the company was already
  at that stage when Ribbit first listed it. When the round cannot be named, `stage="undetermined"` (no source keys).
  Search for Ribbit's FIRST round in the company: "led the Series A" folklore fails one way on famous rows.
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided; it may be given with undetermined.
- Record the rounds you read (`rounds=[rnd(date, round, amount_usd, lead, firm_in_round, source_url, source_type)]`,
  source_type firm | company | press | filing | vendor) whenever you researched the entry (COLLECTION.md s6).
- `seed_to_a_graduation` only matters for Seed (and Pre-Seed) entries. Write `graduated` only with a cited later
  priced round (`grad_src` web_verified or first_party, `grad_cite`, `grad_conf`, and the round in `rounds`). A later
  round NAMED Series A or later graduates whatever the amounts. Write `censored` when the entry is after 2024-09-28.
  Otherwise leave it for the graduation pass (say "Graduation left for the graduation pass." in the note). Never
  write `not_graduated`.
- `hq_country`: ISO alpha-2. A non-US country needs `country_src="web_verified"` and `country_cite` (the company's
  Wikipedia article, its own site, or a press item that places it). Prefilled countries can be wrong Wikidata joins;
  dispute with evidence (`model_disputes_source`) and say so.
- `hq_city`: the bare municipality in English ("Sao Paulo" is written "São Paulo"; "Mexico City"; "Bengaluru" is
  "Bangalore"), never "City, Country". `city_src` is `model_knowledge` (default), `formd_address` or `web_verified`.
  If no source places the company, omit it and add the flag `city_unknown`.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising. Give it on every row you classify. Crypto & Web3 wins over Fintech for on-chain
  businesses; insurance, lending, banking, payments, wealth and accounting software read Fintech & Payments.
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib` lines, COLLECTION.md rule 10): the same company at another investor must agree on status and
  valuation band, and should agree on country and city, unless you hold fresher cited evidence (then say so). A `sib`
  line that is plainly a different company with the same name is a name collision: do not align, list it in your
  report.
- Token and protocol rows (Solana, Arbitrum, Uniswap, Morpho, M0, Lighter, Ethena, Farcaster, Tempo, Aave, Osmosis,
  Helium, Provenance...; decisions.md D2): the row is the issuing organisation (Solana Labs, Offchain Labs, Uniswap
  Labs...). Where the record shows Ribbit bought tokens and no priced equity round, the stage reads `undetermined` and
  the row takes the flag `token_funded`; where Ribbit joined a priced equity round of the labs company, stage it
  normally.

## Membership problems you may find
Membership is decided, but if a row's evidence shows it is NOT a venture position, emit a `verdict(...)` line
instead of a classification and list it in your report: a public-market purchase of an already-listed company (T3),
a control position (the firm and co-investors took 50% or more), a partner's personal angel position with no fund
behind it (T2), or not a company (a fund, a token with no issuer, a person). A verdict needs cited evidence; a hunch
goes in your report instead.

## Finish
1. `NQ_TAG=bN python3 judgments-N.py` must print `recorded ... classification rows`. On `REJECTED`, fix and re-run
   (a rejected file records nothing).
2. Report back in under 250 words: rows classified, any verdict lines and why, name collisions with siblings,
   rows left `unknown` or `undetermined` that a later pass could settle, the WebSearch calls you used, and anything
   that looked wrong in the base (two rows that are one company: name both slugs).
