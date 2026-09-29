# Judge brief: PRO-75 GV, classification batches

You classify the member rows of the queue batches you are given for the GV company base (GV, formerly Google
Ventures, Alphabet's venture arm), write them as a Python judgments file, and record it. Work only inside
`/Users/erik/Developer/merit-capital/data/collection/investors/gv/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<TAG>.py` (it writes `queue/<TAG>.out.jsonl` through `jl.write`).
- Set `NQ_TAG=<TAG>` in EVERY shell command that runs `nq.py` or your judgments file (e.g.
  `NQ_TAG=j3 python3 nq.py ...`, `NQ_TAG=j3 python3 judgments-j3.py`). Other judges run in parallel; the tag keeps
  your news caches separate.
- WebSearch: at most 8 calls in total (the session shares one budget of 200). Prefer `nq.py` (Google News,
  uncapped, throttled machine-wide), `wikifetch.py` (Wikipedia plain text) and WebFetch of a company's own site, a
  press page or an SEC filing. `curl` works for stockanalysis.com market caps
  (`https://stockanalysis.com/stocks/<ticker>/market-cap/`).
- Never type a citation URL by hand except an SEC URL copied from the row's own `formd_links`/`edgar_links` in
  `../companies/base.json` or a URL printed by a tool you ran. Use the helpers (they refuse a missing or ambiguous
  match). A URL you found with WebFetch/WebSearch may be cited after you read the page and it says what you cite.
- Notes are plain prose. Never use em-dashes (use commas, semicolons, parentheses). Say "inferred", never "prior";
  "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. This file.
2. `judge_lib.py` (the whole file: `cls`, `verdict`, `rnd`, `write`, and the citation helpers `SITE`, `ARCH`, `POST`,
   `CASE`, `W`, `FTS`, `NEWS`, `FORMD_ROUNDS`, `FORMD_CITE`).
3. `../documentation/decisions.md` (D1 to D11; the boundary).
4. `../../../COLLECTION.md` section 6 "Classification columns" (lines 1231-1900). Skim; return when a row raises a
   question.

## Your rows
`python3 show.py --batch <N>` prints each row: `need` (the columns still open), `known` (prefilled by the
deterministic layers: do not repeat a known value unless you dispute it with evidence), the live CMS row (`site`:
sector, deal partners, the firm's own exit line, on /ai rows the firm's own dated rounds), the archived listings
(`archive`: years 2012-2026, description, exit line, deal partner by year), the partners' own people pages that
list the company, the GV vehicles' own SEC filings, the firm's posts naming the company (gv.com/news), its case
study, EDGAR full-text hits (S-1 holder tables), Wikipedia sentences, the news sweep (`news`: Google News headlines
for the company beside "GV" or "Google Ventures") and sibling books' rows (`sib`).
Classify only rows whose ledger verdict is `member`:
```
python3 - <<'EOF'
import json
V=json.load(open('../companies/membership-ledger.json'))['gv']['verdicts']
b=json.load(open('queue/batch-00N.json')); items=b if isinstance(b,list) else b.get('items',[])
print([i['slug'] for i in items if V.get(i['slug'],{}).get('verdict')=='member'])
EOF
```
Skip these four member rows: `rosa-foods-inc`, `denver-technologies-inc`, `noho-dental-inc`,
`asset-blue-pharmacy-services-inc` (legal-name twins of Soylent, Warp, Tend and Waltz Health that fold into those
rows at the rebuild). Rows already in `../companies/classification.json` need nothing.

## Tools
- `NQ_TAG=<TAG> python3 nq.py <slug> '"Company" query words' [--all]`: Google News; items land in
  `news-extra-<TAG>.json` under that slug and become citable with `NEWS(slug, "unique title substring")`.
- `python3 wikifetch.py "Title" ... --grep "gv|google ventures|headquart|acquir|series|valuation"`: caches the
  article so `W("Title")` can cite it.
- `SITE(slug)`: the firm's live list the row is on (gv.com/portfolio or gv.com/ai).
  `ARCH(slug)`: the Common Crawl capture of the firm's archived listing that first carried the row.
  `POST("slug-substring")`: the firm's own post. `CASE("slug-substring")`: the firm's case study.
  `FTS("Registrant name", "S-1")`: the first full-text hit of that registrant (an S-1 that names GV as a holder).
- `python3 formd-addr.py <slug>`: related persons with their filed addresses on the row's Form Ds.

## The contract (COLLECTION.md section 6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take
  `rng="below_1b"` and no usd. An asset sale out of insolvency reads acquired with a successor note; a bankruptcy
  with no sale yet reads defunct; a shutdown reads defunct; a merger into another company reads acquired; an
  acqui-hire decides nothing (the company's own fate does). `unknown` when no source read gives the fate (say so in
  the note). The firm's exit line ("Acquired by X, YEAR", "NASDAQ: TICKER") corroborates but goes stale (decisions
  D8: 23andMe's ticker survives its 2025 bankruptcy and asset sale).
- `valuation_range`: below_1b | 1b_plus | 10b_plus (usd >= $10B) | 100b_plus (>= $100B). Any band from 1b_plus up
  needs `usd`, `val_src="web_verified"`, `val_cite`, `asof` (YYYY-MM or YYYY-MM-DD) and
  `extra={"valuation_range_source": "web_verified"}`. Rule A: vendor estimates (PitchBook, Crunchbase "estimated",
  Tracxn, GetLatka, Sacra, Forge) never band a row; it takes a priced round, tender, listing or signed acquisition
  price with a citable figure. A mark older than 24 months (asof before 2024-09-28) carries the flag `stale`. Public
  companies: market cap with a citation and asof. **Momentum slice** (Erik's rule): every private row first seen in
  2021 or later in AI, fintech, data infrastructure or dev tools gets one mechanical check for a $1B+ priced round
  (one `nq.py` query is enough); write the check's outcome and date in the note either way.
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined. Series B and later read Growth; secondaries
  and tenders read Growth. Sources, strongest first: `web_verified` (a cited round naming GV or Google Ventures, or
  an S-1's certain-transactions table listing the preferred series GV bought, via `FTS()`), `first_party` (the
  firm's own post or case study saying which round GV entered), `formd_band` (prefilled; dispute it only with a
  documented round, adding `stage_disputes_band`), `model` (a documented but unnamed round you can name from the
  record, confidence medium). **An announcement names the round the firm led, which is often a follow-on; it
  asserts the entry only where it says so in words.** **A press-named round replaces the firm's own label only after
  the firm's own posts show nothing earlier.** When the round cannot be named, `stage="undetermined"` (no source
  keys). Record the rounds you found as `rounds=[rnd(...)]` (COLLECTION.md s6, PRO-143), `source_type` one of
  firm | company | press | filing | vendor (vendor pages may be listed but never cite).
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided; it may be given with undetermined. Read
  it off the round's own citation; on an /ai row the firm's own first "Invested" month (`site.ai_first_invested`)
  is the entry date where no round source dates it more precisely (decisions D7). Never off `first_seen`.
- `seed_to_a_graduation` only for Seed (and Pre-Seed) entries. Write `graduated` only with a cited later priced
  round (`grad_src` first_party or web_verified, `grad_cite`, `grad_conf`, and the round in `rounds=[rnd(...)]`); a
  later round the record names Series A or later graduates whatever the amounts. Write `censored` when the entry is
  after 2024-09-28. Otherwise leave it for the graduation pass (say "Graduation left for the graduation pass." in the
  note). Never write `not_graduated`.
- `hq_country`: ISO alpha-2. A non-US country needs `country_src="web_verified"` and `country_cite`. Prefilled
  countries from Wikidata are often wrong joins on one-word names: dispute with evidence (flag
  `model_disputes_source`) and say so in the note. An item carrying `hq_country_claim` asks you to confirm or replace
  a Wikidata country: answer it from the company's own evidence.
- `hq_city`: the bare municipality ("San Francisco", never "San Francisco, CA"; Brooklyn is New York; Cambridge MA
  is Cambridge); `city_src` is `model_knowledge` (default), `formd_address` or `web_verified`. If no source places
  the company, omit it and add the flag `city_unknown`.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising. Give it on every row you classify (GV's own sector is a hint, not the answer).
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib`, COLLECTION.md rule 10): the same company in another book must agree on status, band and mark,
  country and city unless you hold fresher cited evidence (then say so). A `sib` line that is plainly a different
  company with the same name is a name collision: do not align, and list it in your report.
- Alphabet's own companies on GV's list (Waymo, Isomorphic Labs; decisions D4) are `private` at their latest
  priced round.

## Membership problems you may find
Membership is decided, but if a row's evidence shows it is NOT a GV venture position, emit a `verdict(...)` line
instead of a classification and list it in your report: a company only Google, Alphabet or CapitalG backed (D2); a
position that first appears after the IPO (D3); stock received for selling a portfolio company (sale consideration);
an investment company or fund (D10); not a company at all. A verdict needs cited evidence; a hunch goes in your
report instead.

## Finish
1. `NQ_TAG=<TAG> python3 judgments-<TAG>.py` must print `recorded ... classification rows`. On `REJECTED`, fix and
   re-run. Read record's whole output.
2. Report back in under 250 words: rows classified, any verdict lines and why, name collisions with siblings,
   rows left `unknown`/`undetermined` that a later pass could settle, the WebSearch calls you used, anything that
   looked wrong in the base (two rows that are one company: name both slugs).
