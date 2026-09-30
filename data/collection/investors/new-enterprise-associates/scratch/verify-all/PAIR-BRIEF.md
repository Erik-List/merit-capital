# Pair brief: rule-10 disputes between two sibling books (verify-all pass after the NEA run, 2026-09-30)

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/verify-all/`.
Rule 10 (COLLECTION.md s10): a company held by two investors reads the same `status` and `valuation_range` in both
books. Each line of your input file is one failing pair: book A's row, book B's row, and which side has the fresher
as-of. Decide every pair. You write ONLY `plan-<TAG>.json`; never touch git, scripts/, any investor's files,
`cross-investor.json` or any `cross-rulings.json`, and never run `run.py record` (the lead applies your plan through
the ingest gate).

Read first: COLLECTION.md s6 `### status` and `### valuation` (`../../../../COLLECTION.md`), and the Aggregator Rule A
there (vendor estimates never band a row). For each pair read both rows in full:
`python3 -c "import json;print(json.dumps(json.load(open('../../../<book>/companies/classification.json')).get('<slug>'),indent=1))"`
and the row's line in `../../../<book>/companies/base.csv` (name, site_url, note, citations), plus
`../../../<book>/companies/resolved.json` for prefilled values. The notes usually say which company the row is.

For each pair, exactly one action:
1. `distinct`: two different companies that share a name (different founders, product, city or years). The note names
   both ("A's Aspect is the 1990s call-centre software company; IVP's is ..."). Most YC pairs are likely this: a YC
   batch company against an older or foreign namesake. Check, do not assume.
2. `stale`: the same company, and one side is out of date. Give the stale side's aligned values:
   `{"book", "slug", "status", "valuation_range", "valuation_usd", "valuation_asof", "valuation_source",
   "valuation_range_source", "valuation_citation", "note"}` (only the keys that change). The citation is a public
   source you read (a press release, a filing, the company's own page, StockAnalysis for a cap, Wikipedia), never
   either investor's own site. The note is one plain sentence naming the event and its source. A band from $1B up
   needs a figure, `valuation_source: web_verified` and `valuation_asof`; a vendor estimate never bands. A signed but
   unclosed deal is a mark, not `acquired`; an acqui-hire decides nothing (the company's own fate does); an asset sale
   out of a failure reads defunct, a business that carried on under a buyer reads acquired.
3. `same_accepted`: the same company, both readings defensible from the record (rare); give the reason.
Where a row's identity is itself wrong (the row describes one company but carries another's status or mark), say so
in the note and give the corrected values as `stale`.

Tools: `python3 ../nq.py <slug> "<query>"` with `NQ_TAG=<TAG>` (Google News, uncapped), `python3 ../wikifetch.py
"<Title>"`, WebFetch of company pages, `python3 ../secget.py "<url>" --grep "..."` for SEC documents, curl for
`https://stockanalysis.com/stocks/<ticker>/market-cap/`. WebSearch: at most the calls your task names (the session's
budget is nearly spent).

`plan-<TAG>.json`: `[{"pair": ["<bookA>:<slug>", "<bookB>:<slug>"], "action": ..., "note": ...,
"align": {...} (stale only)}]`. Report in under 200 words: counts per action, the stale rows by book, WebSearch
calls used, anything wrong you saw beyond the pair (a row describing the wrong company).
