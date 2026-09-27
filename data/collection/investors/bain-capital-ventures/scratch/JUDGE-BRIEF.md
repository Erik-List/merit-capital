# Judge brief: PRO-162 Bain Capital Ventures, classification batches 6-14

You classify the member rows of ONE queue batch of the Bain Capital Ventures (BCV) company base, write them as a
Python judgments file, and record it. Work only inside
`/Users/erik/Developer/merit-capital/data/collection/investors/bain-capital-ventures/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<N>.py` (and let it write its `queue/batch-<N>.out.jsonl` through `jl.write`).
- Set `export NQ_TAG=b<N>` in EVERY shell command that runs `nq.py` or your judgments file (e.g.
  `NQ_TAG=b7 python3 nq.py ...`, `NQ_TAG=b7 python3 judgments-7.py`). Other judges run in parallel; the tag keeps
  your news caches separate.
- WebSearch: at most 12 calls in total. Prefer `nq.py` (Google News, uncapped, throttled machine-wide) and
  `wikifetch.py` (Wikipedia plain text). WebFetch of a company's own site or a press page is fine.
- Never type a citation URL by hand except an SEC URL copied from the row's own `formd_links`/`edgar_links` in
  `companies/base.json` or a URL printed by a tool you ran. Use the helpers (they refuse a missing or ambiguous match).
- Notes are plain prose. Never use em-dashes (use commas, semicolons, parentheses). Say "inferred", never "prior";
  "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. `JUDGE-BRIEF.md` (this file).
2. `judgments-4.py` and `judgments-5.py`: the exact pattern (imports, `site_stage`, `cls`, `verdict`, `rnd`, notes).
3. `judge_lib.py` lines 1-120 and the citation helpers below it (`POST`, `SITE`, `W`, `NEWS`, `CCPAGE`, `ARC`).
4. `../documentation/decisions.md` (D1-D8 and the run-time rulings R1-R3).
5. `../../COLLECTION.md` section 6 "Classification columns" (lines 1231-1900) and section 1 "Control positions"
   (around line 160). Skim; come back when a row raises a question.

## Your rows
`python3 show.py --batch <N>` prints each row: its `need` list (the columns still open), what is already `known`
(prefilled; do not repeat a known value unless you dispute it with evidence), the firm's own listing (`site:`, the
live Sanity CMS), the archived listings (`archive:` years with the old stage bucket, address, outcome text, partners),
the firm's posts, Wikipedia sentences, Form D partners and links, the firm-news sweep (`news`), and sibling
investors' rows for the same company (`sib`). Only classify rows whose ledger verdict is `member`:
```
python3 - <<'EOF'
import json
V=json.load(open('../companies/membership-ledger.json'))['bain-capital-ventures']['verdicts']
b=json.load(open('queue/batch-00N.json')); items=b if isinstance(b,list) else b.get('items',[])
print([i['slug'] for i in items if V.get(i['slug'],{}).get('verdict')=='member'])
EOF
```
Rows already in `../companies/classification.json` from an earlier batch need nothing.

## Tools
- `NQ_TAG=bN python3 nq.py <slug> '"Company" query words' [--all]`: Google News; items land in
  `news-extra-bN.json` under that slug and become citable with `NEWS(slug, "unique title substring")`.
- `python3 wikifetch.py "Title" ... --grep "bain|headquart|acquir|series|valuation"`: caches the article so
  `W("Title")` can cite it (an article from the insource sweep is citable already).
- `SITE(slug)`: the firm's own company page (live list rows). `POST("slug-substring")`: the firm's own post.
- `CCPAGE("/portfolio/company/<slug>")`: the Common Crawl capture of the firm's archived page (archive rows).
- `python3 formd-addr.py <slug>`: related persons with their filed addresses on the row's Form Ds.

## The contract (COLLECTION.md section 6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take
  `rng="below_1b"` and no usd. An asset sale out of a wind-down reads acquired; a shutdown reads defunct; a merger
  into another company reads acquired. `unknown` when no source read gives the fate (say so in the note).
- `valuation_range`: below_1b | 1b_plus | 10b_plus (usd >= $10B) | 100b_plus (>= $100B). Any band from 1b_plus up needs `usd`, `val_src="web_verified"`, `val_cite`, `asof`
  (YYYY-MM or YYYY-MM-DD) and `extra={"valuation_range_source": "web_verified"}`. Rule A: vendor estimates
  (PitchBook, Crunchbase "estimated", GetLatka, Tracxn) never band a row; it takes a priced round, tender, listing
  or acquisition price with a citable figure. A mark older than 24 months (asof before 2024-09-27) carries the
  flag `stale`. Public companies: market cap with a citation and asof. Private rows first seen in 2021 or later
  in hot sectors (AI, crypto, fintech, security, dev tools) get one mechanical web check for a $1B+ priced round
  (Erik's momentum-slice rule); write the check's outcome in the note either way.
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined. Series B and later read Growth.
  Sources: `web_verified` (a cited round naming BCV or dated to BCV's entry), `first_party` (the firm's own post or
  listing), `model` (your reading of a documented but unnamed round, e.g. a first institutional round read as
  Series A; confidence medium), `formd_band` (prefilled; dispute it only with a documented round). Decision R2:
  the live site's `site_stage` tag `Seed` or `Growth` labels at `first_party` medium confidence via
  `**site_stage(slug)` (see the templates); `Early` never mints a stage (it covers Series A and B). A documented
  round that contradicts the tag or the Form D band wins and adds the flag `stage_disputes_band`. When the round
  cannot be named, `stage="undetermined"` (no source keys). Archive stage buckets ("Seed/Early Stage",
  "Expansion/Growth Buyout") are context, not a stage source.
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided; it may be given with undetermined.
- `seed_to_a_graduation` only matters for Seed (and Pre-Seed) entries. Write `graduated` only with a cited later
  priced round (`grad_src` first_party or web_verified, `grad_cite`, `grad_conf`, and the round in `rounds=[rnd(...)]`).
  Write `censored` when the entry is after 2024-09-27. Otherwise leave it for the graduation pass (say
  "Graduation left for the graduation pass." in the note). Never write `not_graduated`.
- `hq_country`: ISO alpha-2. A non-US country needs `country_src="web_verified"` and `country_cite`.
  Prefilled countries are often wrong Wikidata joins (Cameo "IT", Basis "JP", Bench "PH" look wrong): dispute
  with evidence and say so in the note.
- `hq_city`: the bare municipality ("San Francisco", never "San Francisco, CA"); `city_src` is
  `model_knowledge` (default), `formd_address` (from the Form D) or `web_verified`. If no source places the
  company, omit it and add the flag `city_unknown`.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising. Give it on every row you classify.
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib` lines, COLLECTION.md rule 10): the same company at another investor must agree on status,
  valuation band and mark, country and city unless you hold fresher cited evidence (then say so). A `sib` line that
  is plainly a different company with the same name is a name collision: do not align, and list it in your report.
- Crypto rows (Bain Capital Crypto's list, `baincapitalcrypto.com`): a token purchase with no priced equity round
  reads `undetermined` in the stage and adds the flag `token_funded` (COLLECTION.md s6, token-funded positions).

## Membership problems you may find
Membership is decided, but if a row's evidence shows it is NOT a venture position, emit a `verdict(...)` line
instead of a classification (see judgments-5.py `control(...)` and the US LEC line) and list it in your report:
- a control position: the firm with its co-investors bought 50% or more (a buyout, a majority recapitalisation);
  an S-1 or 10-K saying "investors led by Bain Capital ... acquired X% of our stock" is the typical evidence
  (SolarWinds, SurveyMonkey, Zelis were such). `| {"exclusion": "control_position"}`.
- a placement into an already-listed company (T3; decisions D4);
- a Bain Capital generalist-fund position from 1984-1998 (the heritage book, R1: see judgments-heritage.py);
- not a company (a fund, a navigation link, a person).
A verdict needs cited evidence; a hunch goes in your report instead.

## Finish
1. `NQ_TAG=bN python3 judgments-N.py` must print `recorded ... classification rows`. On `REJECTED`, fix and re-run.
2. Report back in under 250 words: rows classified, any verdict lines and why, name collisions with siblings,
   rows left `unknown`/`undetermined` that a later pass could settle, the WebSearch calls you used, anything
   that looked wrong in the base (e.g. two rows that are one company: name both slugs).
