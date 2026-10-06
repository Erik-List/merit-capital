# Cross-book brief: PRO-80 Bessemer Venture Partners, rule 10 (COLLECTION.md s10 invariant 10)

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/`.
Rule 10: a company held by two investors reads the same `status` and `valuation_range` in both books. Your input is
`cross-list.txt` (one disagreement per line: Bessemer's row, the sibling's row, which side has the fresher as-of). Decide
every pair. You write ONLY `judgments-<TAG>.py` (Bessemer rows, via `jl.write`) and `cross-plan-<TAG>.json`; never touch
git, scripts/, another investor's files, `cross-investor.json` or `cross-rulings.json` (the lead applies your plan).

Read first: `JUDGE-BRIEF.md` (hard limits, the classification contract), `judge_lib.py`, COLLECTION.md s6 status
and valuation (`../../../COLLECTION.md`). For each pair read both rows: `python3 show.py <bvp-slug>` for Bessemer, and the
sibling's stored row: `python3 -c "import json;print(json.dumps(json.load(open('../../<sib>/companies/classification.json')).get('<sib-slug>'),indent=1))"`
plus its `../../<sib>/companies/base.csv` line (name, site, note). Siblings' notes often hold the citation.

For each pair, exactly one action:
1. `distinct`: two different companies that share a name (different founders, product, city, years). Note names both.
   No Bessemer change.
2. `bvp_stale`: Bessemer's row is wrong or older than the sibling's cited evidence. Emit a classification line for Bessemer
   with only the keys that change, a cited source (never a vendor page for a band), and a one-sentence note.
3. `sibling_stale`: Bessemer holds the fresher cited evidence (a later sale, shutdown, round or cap). Give the sibling's
   aligned values: `{"book", "slug", "status", "valuation_range", "valuation_usd", "valuation_asof",
   "valuation_source", "valuation_citation", "note"}` (only the keys that change), with a citation that is NOT
   bvp.com (a press release, filing, the company's own page or StockAnalysis for a cap; the sibling cannot cite
   another investor's site). The note is one plain sentence saying what changed and why. A band from $1B up needs a
   figure, `valuation_source: web_verified` and `valuation_asof`.
4. `accepted`: the same company, and both readings are defensible from the record (rare). Give the reason.
Rules: freshest cited evidence wins; a signed but unclosed deal is a mark, not `acquired`; a public row's band follows
its current market cap; a row Bessemer has not yet classified (status None) belongs to the delta, skip it and say so.
WebSearch: at most the calls your task names. Prefer `nq.py` (NQ_TAG=<TAG>), `wikifetch.py`, WebFetch of company
pages, StockAnalysis via curl, SEC filings via `secget.py`.

`cross-plan-<TAG>.json`: `[{"pair": ["bessemer-venture-partners:<slug>", "<book>:<slug>"], "action": ...,
"note": ..., "sibling": {...} (sibling_stale only)}]`. Run your judgments file ONCE if it has lines
(`NQ_TAG=<TAG> python3 judgments-<TAG>.py`) and read record's whole output. Report in under 200 words: counts per
action, Bessemer rows changed, WebSearch calls used.


Your input file is `cross-list-<TAG>.txt` (your half of the list). `python3 show.py <slug>` prints Bessemer's row with what is stored now.
The Bessemer book was re-priced today (2026-10-06): its public rows carry StockAnalysis caps of that date and its
private $1B+ rows were re-pinned to cited rounds, so where the pair differs only because the sibling carries an older
cap or mark, the sibling is stale (`sibling_stale`, with Bessemer's stored figure, as-of and citation, read from
`../companies/classification.json`; the citation must not be bvp.com).
A sibling book that carries `scratch/in-flight.json` (atomico, bain-capital-ventures, founders-fund, general-catalyst,
index-ventures, speedinvest) cannot be written now: still decide the pair, and mark the plan entry `"in_flight": true`.

Known namesakes from the grind (verify each, then rule `distinct`): alloy (20vc, 8vc, bain-capital-ventures, menlo-ventures,
y-combinator; lightspeed's alloy is the identity company), august, avalanche-technology (a16z avalanche is Ava Labs),
axion, beyond, brainbase, breaker, current (a16z, general-catalyst, tiger: the neobank Current; Bessemer's is the accounting
firm formerly Crete Professionals Alliance, now ruled out of the Bessemer base), daylight (a16z, bcv, usv), diligent
(speedinvest, yc), disco (felicis, gc), endgame (a16z, eqt), fabric-technologies (six siblings), fandom (redpoint), flock
(a16z: Flock Safety), fulcrum, guild (yc, battery), kindred, jasper, light (atomico, cherry, seedcamp, balderton: the Danish
Light), milo, pana, nym, ramp (balderton, seedcamp: Ramp Network), sentra, rosebud, shift-technology, speakeasy, trigo,
vesta, spruce, sweep, teleport, valence, watershed, zoomin, parametric, abacus, electric, neo, mural-health, verse.
Known stale siblings (verify, then `sibling_stale` with the citation stored on Bessemer's row): see the "Sibling
alignment worklist" lines in `RESUME.md` (grep "worklist" and "Sibling" there).
