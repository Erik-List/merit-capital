# Sweep brief: PRO-75 GV, the undetermined-stage and unknown-status class (duty 9)

The blind 5% check re-judged 38 rows and settled the entry round on 5 of the 9 rows the grind had left
`undetermined` (Blue Vision Labs, Quettra, Arda, iPierian, Ribon) and the fate of 2 rows (Scalus, Modern Age).
COLLECTION.md s8 duty 9: a self-consistency hit is a class, not a row. You re-check your share of the class.
Work only inside `/Users/erik/Developer/merit-capital/data/collection/investors/gv/scratch/`.

**Read first: `JUDGE-BRIEF.md` (hard limits, tools, contract) and `DELTA-BRIEF.md` (the S2A contract), both still in
force, with these changes: WebSearch and WebFetch are exhausted, do not call them; `record` APPENDS your note to the
stored one, so `note=` carries ONLY your new sentences, starting "Stage sweep 2026-09-29: ".**

## Your rows
Your slugs are in your prompt. `python3 show.py <slug>` prints the evidence view (the queue is empty now, so `need`
is blank; read the row's current record with `python3 gradview.py <slug>`, which prints stage, status, note and
Form D rounds). For each row the question is one or both of:
1. **Entry stage** (rows reading `undetermined`): the stage of the round in which GV (Google Ventures) FIRST put
   money in. Techniques that worked on the sample, strongest first:
   - TechCrunch's own search: `curl -s -A "Mozilla/5.0" "https://techcrunch.com/wp-json/wp/v2/posts?search=<name>&per_page=20&_fields=link,date,title"`
     (add `&after=2013-01-01T00:00:00&before=2014-12-31T00:00:00` to narrow), then read the funding story; a later
     story (an acquisition) often links the funding story, so follow its links. A page that names the round and GV
     is `web_verified` with `stage_cite`.
   - Google News: `NQ_TAG=<TAG> python3 nq.py <slug> '"Name" (raises OR funding OR "Series A" OR seed) "Google Ventures"'`.
   - The firm's listing date against the company's round sequence: the row's `first_seen` / `wayback_first_link`
     dates the firm's first capture listing the company. If exactly one financing precedes that capture, GV
     entered in it (model; `stage_conf="low"` unless a page ties GV to it). Arda: listed May 2022, one round before
     (the December 2021 seed): Seed.
   - The company's own later naming: a round the company calls "Series B" makes the round before it the Series A.
   - Form D structure (COLLECTION.md s6 "Structural rules"), from the first filing that lists a GV person as director
     or related person: 2 or more prior filings reads Growth; 1 prior, Series A or Growth by band; 0 prior, the
     band, if the company was founded 2008 or later and was 4 years old or less. **Use the era-adjusted band, not
     the code's flat one**: seed / Series A ceilings of $1.5M / $12M up to 2010, $2.5M / $15M 2011-14, $4M / $20M
     2015-18, $6M / $30M 2019-21, $8M / $40M from 2022; Pre-Seed below a quarter of the seed ceiling. Filings
     within 90 days of each other are one round. Source `formd_structural`, `stage_cite` the entry accession's
     index URL (copy it from the row's `formd_links`, or from EDGAR for the company's own CIK).
   Where nothing names or clearly places GV's first round, leave `undetermined` and emit nothing for the stage.
   **A row that becomes Seed must also be decided for S2A** exactly as DELTA-BRIEF says (graduated with a cited later
   round; not_graduated on a cited end or on the full absence test with `grad_asof="2026-09-29"` and surfaces; or
   censored), with `entry_date`; a decided row on an uncited stage carries `stage_uncited` and `stage_conf="low"`.
2. **Status** (rows reading `unknown`): the company's fate. Acquired (a sale, a merger into another company, or an
   asset sale where the business continues), defunct (shut down; a bankruptcy with no sale yet), private or public
   (still operating: its own site current, recent news). Cite what you read in the note. If no source settles it,
   leave `unknown` and emit nothing.

Emit one `jl.cls(...)` line per row you change, with only the keys you settle (`stage=`, `stage_src=`,
`stage_conf=`, `stage_cite=`, `entry_date=`, the S2A keys, `status=`), plus `flags=["stage_disputes_band"]` where
you override a Form D band. Rows you cannot settle get no line. Never guess.

## Finish
`NQ_TAG=<TAG> python3 judgments-<TAG>.py` must print `recorded ...` with nothing rejected. Report in under 200
words: rows settled for stage (by source: web_verified / first_party / formd_structural / model), new Seed rows
and their S2A, statuses settled, rows left open, anything wrong in the base.
