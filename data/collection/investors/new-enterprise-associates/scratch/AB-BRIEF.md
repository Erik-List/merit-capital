# A/B pass brief (COLLECTION.md s7, s8 standing duties). PRO-100 NEA

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only
`judgments-<TAG>.py` (via `jl.write("<TAG>", ...)`). Never touch git, scripts/, config, identity-merges, decisions or
other investors. Read `judge_lib.py`, `JUDGE-BRIEF.md` (the classification contract), COLLECTION.md s6 `### valuation`
and s7 (`../../../COLLECTION.md`). Set `NQ_TAG=<TAG>` on nq.py and judgments runs; scratch under `scratchpad/<TAG>/`.
Emit classification lines with only the keys that change (plus flags and a one-sentence note); a membership problem
gets a verdict line with its citation. Notes plain prose, no em-dashes.

`scratch/ab-news.json` holds, per private row, the Google News headlines naming the company dated after its mark
(`items_after_mark`); cite a headline with `NEWS(slug, "unique title words")` after reading it (`nq.py` items are
citable the same way). `python3 show.py <slug>` prints the row, its stored values and sibling rows.

## ab1: the private $1B+ rows (`queue/ab1.json`)
Pass A, defend: every private $1B+ row carries a priced event (round, tender, signed acquisition price) with a
citable non-vendor figure and date (Rule A: vendor estimates never band). Re-pin any mark that rests on the unicorn
list or a vendor to the round's own announcement; a mark older than 2024-09-30 keeps `stale`. Pass B, attack: search
for the newer round, the acquisition (closing flips status to acquired; a signed but unclosed deal is a mark), the
down round or tender, the shutdown. Also, per s8 duty 1, rule 4: every $1B+ row needs class 1 or 2 stage evidence (a
cited round naming NEA, the firm's own post, or the Form D structure); where the stage is `model` or `undetermined`,
try once to cite it; failing that add the flag `cite_pending`. Specific checks: chinaway-technologies-limited (a $2.2B
G7 mark set on a judge's own recollection that Chinaway is G7: cite the identity or revert to below_1b), world-labs
($8.2B AMD agreement, unclosed), tri-alpha-energy ($6.0B signed merger), positron-ai ($5B), koudai (`needs_web_value`:
pin or kill), radiology-partners and strive-health (decisions.md R6: did NEA alone form or control them? if control,
verdict `not_member` with `extra={"exclusion": "control_position"}`).

## ab2: the momentum slice (`queue/ab2.json`)
Every private row first seen since 2021 in AI, fintech, data infrastructure or dev tools gets one mechanical check
for a $1B+ priced round (the ab-news items, one nq.py query if they are thin). Record the outcome on the row either
way: `extra={"valuation_range_source": "web_verified"}` with the citation of the round found, or a note "Checked
2026-09-30 for a priced round at $1B or more: none found (Google News)" with the band kept below_1b. Then duty 6:
re-intersect the unicorn list with loose names (`../../../shared/unicorns/wikipedia.json`, current and former; strip
.io/.ai/.com, "Labs", "HQ", "Technologies") against every member row, and settle each hit (banded, exited, a
different company).

## ab3: the public $1B+ rows (`queue/ab3.json`) and loose ends
Each public $1B+ row already has a 2026-09-30 market cap from stockanalysis.com (the `caps` lines). Check each row is
still listed under that ticker and is the same company (s8 duty 8: a float or cap from a namesake); duty 4: stale
float rows that were acquired or re-listed; duty 5: public rows whose float is older than 12 months for known deaths.
Then the loose ends: boku (LSE AIM: find a citable cap in GBP and convert with `python3 ../../../../scripts/fx-convert.py
<amount> GBP 2026-09-30`), fiscalnote and galera-therapeutics (no longer quoted: status and value per the record),
gst-clinics (identify the listing or correct the status), super (prefilled Wikidata valuation source dated 1985
must not survive: set the band from the record).

WebSearch: at most 8 calls per agent. Run the judgments file once. Report: rows changed and why (one line each), rows
flagged cite_pending or stale, anything that contradicts a sibling book.
