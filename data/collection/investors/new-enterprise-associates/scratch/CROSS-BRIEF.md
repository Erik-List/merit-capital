# Cross-book brief: PRO-100 NEA, rule 10 (COLLECTION.md s10 invariant 10)

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`.
Rule 10: a company held by two investors reads the same `status` and `valuation_range` in both books. Your input is
`cross-list.txt` (one disagreement per line: NEA's row, the sibling's row, which side has the fresher as-of). Decide
every pair. You write ONLY `judgments-<TAG>.py` (NEA rows, via `jl.write`) and `cross-plan-<TAG>.json`; never touch
git, scripts/, another investor's files, `cross-investor.json` or `cross-rulings.json` (the lead applies your plan).

Read first: `JUDGE-BRIEF.md` (hard limits, the classification contract), `judge_lib.py`, COLLECTION.md s6 status
and valuation (`../../../COLLECTION.md`). For each pair read both rows: `python3 show.py <nea-slug>` for NEA, and the
sibling's stored row: `python3 -c "import json;print(json.dumps(json.load(open('../../<sib>/companies/classification.json')).get('<sib-slug>'),indent=1))"`
plus its `../../<sib>/companies/base.csv` line (name, site, note). Siblings' notes often hold the citation.

For each pair, exactly one action:
1. `distinct`: two different companies that share a name (different founders, product, city, years). Note names both.
   No NEA change.
2. `nea_stale`: NEA's row is wrong or older than the sibling's cited evidence. Emit a classification line for NEA
   with only the keys that change, a cited source (never a vendor page for a band), and a one-sentence note.
3. `sibling_stale`: NEA holds the fresher cited evidence (a later sale, shutdown, round or cap). Give the sibling's
   aligned values: `{"book", "slug", "status", "valuation_range", "valuation_usd", "valuation_asof",
   "valuation_source", "valuation_citation", "note"}` (only the keys that change), with a citation that is NOT
   nea.com (a press release, filing, the company's own page or StockAnalysis for a cap; the sibling cannot cite
   another investor's site). The note is one plain sentence saying what changed and why. A band from $1B up needs a
   figure, `valuation_source: web_verified` and `valuation_asof`.
4. `accepted`: the same company, and both readings are defensible from the record (rare). Give the reason.
Rules: freshest cited evidence wins; a signed but unclosed deal is a mark, not `acquired`; a public row's band follows
its current market cap; a row NEA has not yet classified (status None) belongs to the delta, skip it and say so.
WebSearch: at most the calls your task names. Prefer `nq.py` (NQ_TAG=<TAG>), `wikifetch.py`, WebFetch of company
pages, StockAnalysis via curl, SEC filings via `secget.py`.

`cross-plan-<TAG>.json`: `[{"pair": ["new-enterprise-associates:<slug>", "<book>:<slug>"], "action": ...,
"note": ..., "sibling": {...} (sibling_stale only)}]`. Run your judgments file ONCE if it has lines
(`NQ_TAG=<TAG> python3 judgments-<TAG>.py`) and read record's whole output. Report in under 200 words: counts per
action, NEA rows changed, WebSearch calls used.
