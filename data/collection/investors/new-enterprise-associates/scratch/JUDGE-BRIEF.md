# Judge brief: PRO-100 NEA, membership and classification batches

You judge the queue items you are given for the NEA (New Enterprise Associates) company base: membership where it
is open, then every open classification column for the members. You write a Python judgments file and record it.
Work only inside `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<TAG>.py` (it writes `queue/<TAG>.out.jsonl` through `jl.write`).
- Set `NQ_TAG=<TAG>` in EVERY shell command that runs `nq.py` or your judgments file (e.g.
  `NQ_TAG=j3 python3 nq.py ...`, `NQ_TAG=j3 python3 judgments-j3.py`). Other judges run in parallel; the tag keeps
  your news caches separate.
- WebSearch: at most the number of calls your task names (the session shares one budget of 200). Prefer `nq.py`
  (Google News, uncapped, throttled machine-wide), `wikifetch.py` (Wikipedia plain text) and WebFetch of a company's
  own site, a press page or an SEC filing. `curl` works for stockanalysis.com market caps
  (`https://stockanalysis.com/stocks/<ticker>/market-cap/`) and for SEC filings (send a User-Agent header).
- Never type a citation URL by hand except an SEC URL copied from the row's own `formd_links`/`edgar_links` in
  `../companies/base.json` or a URL printed by a tool you ran. Use the helpers (they refuse a missing or ambiguous
  match). A URL you found with WebFetch/WebSearch may be cited after you read the page and it says what you cite.
- Notes are plain prose, one or two sentences. Never use em-dashes (use commas, semicolons, parentheses). Say
  "inferred", never "prior"; "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. This file.
2. `judge_lib.py` (the whole file: `cls`, `verdict`, `rnd`, `write`, and the citation helpers `SITE`, `ARCH`, `POST`,
   `W`, `FTS`, `NEWS`, `GNEWS`, `FORMD_ROUNDS`, `FORMD_CITE`).
3. `../documentation/decisions.md` (D1 to D8 and X1; the boundary).
4. `../../../COLLECTION.md` section 6 "Classification columns" (from the line `## 6. Classification columns` to
   `## 7.`). Skim; return when a row raises a question.

## Your rows
`python3 show.py --batch <N>` (or `python3 show.py <slug> ...`) prints each item: `need` (the columns still open,
`membership` first when the row is unjudged), `known` (prefilled by the deterministic layers: do not repeat a known
value unless you dispute it with evidence), the live CMS row (`site`: the firm's own first-invested year, its stage
label, status and exit line, NEA deal team and board members), the archived listings (`archive`: years, the
firm's "Year invested", stage, Current/Historic, exit and acquirer, the 2008 report it sat in, e.g. "Public
Purchase"), NEA vehicles' own SEC filings, the firm's posts naming the company, EDGAR full-text hits (S-1 holder
tables naming NEA), Form D partner matches with their filing dates, Wikipedia sentences, and sibling books' rows
(`sib`).

## Membership (items whose `need` starts with `membership`)
The firm's own listing in any era suffices (D1, D2). A filing by an NEA vehicle (13D/G, Form 3/4 by the fund, an S-1
holder table naming "New Enterprise Associates" entities) suffices. A Form D on which a roster person is a related
person is a NAME MATCH and never suffices alone (COLLECTION.md s1): it needs affirmative corroboration (the firm's
listing, an NEA vehicle on a filing, a press or company source naming NEA in a round). Judge name-match rows
cluster-first: resolve the person once (their NEA years in the item's `partners_formd` window, their prior and next
firms), then every row that person explains.
- `member`: `verdict(slug, "member", basis, ec=..., conf=..., cite=...)` with `ec` one of `site_listing`,
  `fund_filing`, `formd_adjudicated`, `web`, `knowledge`. A current or in-tenure NEA partner as Director of record on
  the Form D of a company that RESOLVES to a real operating company is `formd_adjudicated` at medium, flagged for the
  A/B pass (COLLECTION.md s1).
- `not_member`: a homonym, a seat held outside the person's NEA years (prior or next firm, an operator job), a
  personal angel check, a fund or SPV or fund-shaped entity (D5), a PIPE or public purchase into an already listed
  company with no earlier NEA private round (X1, T3), stock received as sale consideration (D8), a company only the
  IndoUS joint venture or NewView held (D1). Missing corroboration on a name match is `not_member`, not `uncertain`.
- `uncertain` only when identification is genuinely open or the evidence conflicts after you tried.
A `not_member` row gets its verdict line and nothing else. A member gets the verdict line AND a classification line
(two separate lines; `record` routes by the presence of `verdict`).

## The classification contract (COLLECTION.md section 6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take
  `rng="below_1b"` and no usd. An asset sale out of insolvency reads acquired with a successor note; a bankruptcy
  with no sale yet reads defunct; a shutdown reads defunct; a merger into another company reads acquired; an
  acqui-hire decides nothing (the company's own fate does). The firm's exit line corroborates but goes stale.
- `valuation_range`: below_1b | 1b_plus | 10b_plus (usd >= $10B) | 100b_plus (>= $100B). Any band from 1b_plus up
  needs `usd`, `val_src="web_verified"`, `val_cite`, `asof` (YYYY-MM or YYYY-MM-DD) and
  `extra={"valuation_range_source": "web_verified"}`. Rule A: vendor estimates (PitchBook, Crunchbase "estimated",
  Tracxn, GetLatka, Sacra, Forge) never band a row; it takes a priced round, tender, listing or signed acquisition
  price with a citable figure. A mark older than 24 months (asof before 2024-09-30) carries the flag `stale`. Public
  companies: market cap with a citation and asof. **Momentum slice**: every private row first seen in 2021 or later
  in AI, fintech, data infrastructure or dev tools gets one mechanical check for a $1B+ priced round (one `nq.py`
  query is enough); write the check's outcome and date in the note either way.
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined. Series B and later read Growth; secondaries,
  tenders and crossover rounds read Growth. Sources, strongest first: `web_verified` (a cited round naming NEA, or
  an S-1's certain-transactions table listing the preferred series NEA bought, via `FTS()`), `first_party` (the
  firm's own post saying which round NEA entered; or the firm's own CMS stage label `Seed` or `Growth`, cited with
  `SITE(slug)`, confidence medium; `Early` is NOT a label, it straddles Seed and Series A), `formd_structural` /
  `formd_band` (prefilled; dispute only with a documented round, adding `stage_disputes_band`), `model` (a
  documented round you can name, confidence medium). **An announcement names the round the firm led, which is
  often a follow-on; it asserts the entry only where it says so.** **A press-named round replaces the firm's own
  label only after the firm's own posts show nothing earlier.** When the round cannot be named,
  `stage="undetermined"` (no source keys). Record the rounds you found as `rounds=[rnd(...)]` (COLLECTION.md s6,
  PRO-143), `source_type` one of firm | company | press | filing | vendor (vendor pages may be listed, never cited).
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided; it may be given with undetermined. Read
  it off the round's own citation; where none dates it more precisely, the firm's own first-invested year
  (`site.invest_year`, the archive's "Year invested") is the entry year. Never off `first_seen`.
- `seed_to_a_graduation` only for Seed entries. Write `graduated` only with a cited later priced round (`grad_src`
  first_party or web_verified, `grad_cite`, `grad_conf`, and the round in `rounds=[rnd(...)]`); a later round the
  record names Series A or later graduates whatever the amounts. Write `censored` when the entry is after
  2024-09-30. Otherwise leave it for the graduation pass (say "Graduation left for the graduation pass." in the
  note). Never write `not_graduated`.
- `hq_country`: ISO alpha-2. A non-US country needs `country_src="web_verified"` and `country_cite`. Prefilled
  countries from Wikidata are often wrong joins on one-word names: dispute with evidence (flag
  `model_disputes_source`). An item carrying `hq_country_claim` asks you to confirm or replace a Wikidata country.
- `hq_city`: the bare municipality ("San Francisco", never "San Francisco, CA"; Brooklyn is New York; Cambridge MA
  is Cambridge); `city_src` is `model_knowledge` (default), `formd_address` or `web_verified`. If no source places
  the company, omit it and add the flag `city_unknown`.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising. Give it on every row you classify. Chips and hardware are Industrial & Robotics;
  enterprise infrastructure and networking are Data Infrastructure; healthcare vertical software is Healthcare & Bio.
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib`, rule 10): the same company in another book must agree on status, band and mark, country and
  city unless you hold fresher cited evidence (then say so in the note). A `sib` line that is plainly a different
  company with the same name is a name collision: do not align, and list it in your report.
- A company that cannot be named at all: flag `identity_unresolved`, and `stage`, `rng` all `undetermined`.

## Finish
1. `NQ_TAG=<TAG> python3 judgments-<TAG>.py` must print `recorded ... ` lines. On `REJECTED`, fix and re-run the
   whole file (record merges idempotently; never record the same file twice after it succeeded, notes would be
   replaced). Read record's whole output.
2. Report back in under 250 words: verdicts by kind, rows classified, name collisions with siblings, rows left
   `unknown`/`undetermined` that a later pass could settle, WebSearch calls used, anything wrong in the base (two
   rows that are one company: name both slugs; a renamed company).
