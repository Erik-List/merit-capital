# Align brief: sibling rows the GV run (PRO-75) found stale, re-ingested with Erik's approval

**Erik approved on 2026-09-29: "ingest GV and align the stale/misaligned sibling rows".** This is that alignment.
The procedure is the 20VC run's (data/collection/investors/20vc/scratch/align/: align.py, compare.py, csvdiff.py,
readback.ts, reingest.log): read it first and reuse it.

## What to align
1. **The accepted pairs** in `data/collection/investors/gv/companies/cross-rulings.json` (`accepted`, 68 entries):
   each pairs a GV row with a sibling row of the SAME company where GV's row holds the newer cited event. For your
   books, write into the sibling row the status and band GV holds (`status`, `valuation_range`, and for a private or
   public $1B+ row `valuation_usd`, `valuation_source: web_verified`, `valuation_range_source: web_verified`,
   `valuation_asof`, `valuation_citation`; an acquired, defunct or unknown row takes `below_1b` and no figure).
   Take the facts and the citation from the GV row (`data/collection/investors/gv/companies/classification.json`: its
   `valuation_citation`, or a URL in its note that states the event). **Never cite gv.com to another investor's book**,
   and **read every URL you cite with curl before writing it** (it must state the event). Clarifai: Erik ruled it
   `acquired` (Nebius took the team, bought the patents and licensed the technology, May 2026; keep the rule
   consistent), so the Lux, Menlo and USV rows read acquired.
2. **8VC's Lyell** (if your books include 8vc): its row reads acquired, but Lyell Immunopharma (NASDAQ: LYEL) still
   trades: `public`, the market cap from `https://stockanalysis.com/stocks/lyel/market-cap/` on the day you read it.
Nothing else: no stage, S2A, city or country changes in other books (report any you notice).

## How, per book
1. Write `data/collection/investors/gv/scratch/align/<book>.jsonl`, one line per row: `{"slug": <sibling slug>,
   "who": "agent-align-pro75", ...keys..., "note": "Aligned 2026-09-29 from the GV run (PRO-75, rule 10): <one
   sentence with the event and its source>"}`. `record` APPENDS the note, so the note is only that sentence. Emit a
   `clear_flags: ["stale"]`? No: `stale` is not clearable; leave flags alone except adding none.
2. `python3 scripts/run.py record --investor <book> data/collection/investors/gv/scratch/align/<book>.jsonl`; read the
   whole output; fix any REJECTED line (a rejected file records nothing).
3. `python3 scripts/run.py verify --investor <book>`: it must stay as clean as before (compare with a run before
   your record; only fix what you introduced). `python3 scripts/run.py export --investor <book>` and `review`.
4. Diff the re-exported `base.csv` against `git show HEAD:<path>` (20VC's csvdiff.py): only your cells may change.
5. Database: `npx tsx data/collection/investors/20vc/scratch/align/readback.ts <book>` BEFORE writing: it must list
   exactly your changed cells (if it lists other differences, stop that book and report). Then
   `npx tsx scripts/ingest-companies.ts <book> --dry-run` (must plan 0 new, 0 removed), then the write without
   `--dry-run`, then the readback again: 0 differing cells. Append each step's result to
   `data/collection/investors/gv/scratch/align/reingest.log` in 20VC's format.
6. Commit only that book's three company files with an explicit pathspec, never `add -A`/`commit -a`/stash/checkout:
   `git add -- data/collection/investors/<book>/companies/classification.json data/collection/investors/<book>/companies/base.csv data/collection/investors/<book>/companies/review.html`
   then `git commit -m "PRO-75: <book> aligned with the GV run (N rows) and re-ingested" -- <the same three paths>`,
   message ending with the line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Other sessions may hold
   uncommitted edits in these books (config.json); never commit or touch those.

Skip any book whose `scratch/in-flight.json` exists or whose companies files show uncommitted changes before you
start (`git status --short -- data/collection/investors/<book>/companies`); report it instead.
