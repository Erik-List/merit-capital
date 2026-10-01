# Cross-book brief: PRO-99 Kleiner Perkins, rule 10 (COLLECTION.md s10 invariant 10)

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch/`.
Rule 10: a company held by two investors reads the same `status` and `valuation_range` in both books. Your input is
`cross-list.txt` (one disagreement per line: Kleiner Perkins' row, the sibling's row, which side has the fresher as-of). Decide
every pair. You write ONLY `judgments-<TAG>.py` (Kleiner Perkins rows, via `jl.write`) and `cross-plan-<TAG>.json`; never touch
git, scripts/, another investor's files, `cross-investor.json` or `cross-rulings.json` (the lead applies your plan).

Read first: `JUDGE-BRIEF.md` (hard limits, the classification contract), `judge_lib.py`, COLLECTION.md s6 status
and valuation (`../../../COLLECTION.md`). For each pair read both rows: `python3 show.py <kp-slug>` for Kleiner Perkins, and the
sibling's stored row: `python3 -c "import json;print(json.dumps(json.load(open('../../<sib>/companies/classification.json')).get('<sib-slug>'),indent=1))"`
plus its `../../<sib>/companies/base.csv` line (name, site, note). Siblings' notes often hold the citation.

For each pair, exactly one action:
1. `distinct`: two different companies that share a name (different founders, product, city, years). Note names both.
   No Kleiner Perkins change.
2. `kp_stale`: Kleiner Perkins' row is wrong or older than the sibling's cited evidence. Emit a classification line for Kleiner Perkins
   with only the keys that change, a cited source (never a vendor page for a band), and a one-sentence note.
3. `sibling_stale`: Kleiner Perkins holds the fresher cited evidence (a later sale, shutdown, round or cap). Give the sibling's
   aligned values: `{"book", "slug", "status", "valuation_range", "valuation_usd", "valuation_asof",
   "valuation_source", "valuation_citation", "note"}` (only the keys that change), with a citation that is NOT
   kleinerperkins.com (a press release, filing, the company's own page or StockAnalysis for a cap; the sibling cannot cite
   another investor's site). The note is one plain sentence saying what changed and why. A band from $1B up needs a
   figure, `valuation_source: web_verified` and `valuation_asof`.
4. `accepted`: the same company, and both readings are defensible from the record (rare). Give the reason.
Rules: freshest cited evidence wins; a signed but unclosed deal is a mark, not `acquired`; a public row's band follows
its current market cap; a row Kleiner Perkins has not yet classified (status None) belongs to the delta, skip it and say so.
WebSearch: at most the calls your task names. Prefer `nq.py` (NQ_TAG=<TAG>), `wikifetch.py`, WebFetch of company
pages, StockAnalysis via curl, SEC filings via `secget.py`.

`cross-plan-<TAG>.json`: `[{"pair": ["kleiner-perkins:<slug>", "<book>:<slug>"], "action": ...,
"note": ..., "sibling": {...} (sibling_stale only)}]`. Run your judgments file ONCE if it has lines
(`NQ_TAG=<TAG> python3 judgments-<TAG>.py`) and read record's whole output. Report in under 200 words: counts per
action, Kleiner Perkins rows changed, WebSearch calls used.

Known namesakes from the grind (verify, then rule `distinct`): endgame (a16z), fauna (gv: FaunaDB), handshake (a16z, greylock, sequoia: the handshake.org protocol; point-nine: a wholesale app), helix (gv), good-technology (nea: Visto), modern-life (thrive), resonate (yc), pelago, presto, optic, signal, roadrunner, parallel, betterworks (redpoint), coda (insight: Coda Payments), adknowledge (tcv), bump (ours is the streetwear marketplace), assured, chutney, phantom, rain, pilot (usv: Pilot Fiber), pattern, linear-technology vs Linear, mine, multiply, luca, motive (accel), tulip, teleport, wave, songbird, summation, level, instinct (yc), mindbloom (8vc), harmonic (lightspeed: Harmonic Inc.), fizz, beam.
Instacart: Kleiner Perkins' cap ($9.98B, 2026-09-30) sits 0.2% under the $10B edge while eight books hold 10b_plus on earlier September caps: rule it `accepted` with that reason rather than re-ingesting eight books.
