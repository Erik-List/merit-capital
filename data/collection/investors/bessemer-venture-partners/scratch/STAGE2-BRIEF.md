# Second pass brief: entry stage and status, PRO-80 Bessemer Venture Partners

You re-judge a list of member rows that a first, cheaper pass left with `entry_stage="undetermined"` or
`status="unknown"`. Work only inside
`/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/` (cd there for
every command). Write only `judgments-<TAG><letter>.py`. Never touch git, scripts/, config.json, decisions.md,
identity-merges.json or other investors' directories.

## Read first
1. `JUDGE-BRIEF.md` (complete: the hard limits, the classification contract, the membership boundary).
2. `judge_lib.py` (whole: `cls`, `verdict`, `rnd`, `write`, the citation helpers `SITE`, `ARCH`, `POST`, `W`, `FTS`,
   `NEWS`, `GNEWS`).
3. `../documentation/decisions.md` (D1 to D10, X1, and the rulings R1 to R7 at the end).
4. COLLECTION.md section 6 only (`grep -n "^## 6. Classification columns\|^## 7. " ../../../COLLECTION.md`, read
   that line range).

## Your rows
`python3 show.py --list <your file>` prints each row with what is `stored` now (and the stored note) and all the
evidence. New since the first pass, and the reason for this pass:
- `archive` now reaches back to 1999: the 1999 to 2001 site (eras `html-people`) gives the firm's own investment
  year and deal partner; the 2002 to 2007 site (`asp-onepage`, `asp-success`) gives a description per company that
  often says which round the firm entered ("invested in the first round", "led the Series A", "BVP invested in
  Ciena's Series B round in December 1994", "seeded"), and the month of the investment for the big exits.
- `history page`: the firm's own 2008 history narrative, with round statements for the famous deals.
Cite an archived sentence with `ARCH(slug)` (the first capture carrying the row); cite the history page with the
URL printed on its line.

## What to do, per row
1. **Entry stage.** Decide it wherever a source names the round the firm FIRST entered:
   - the firm's own words (`first_party`, cite `ARCH(slug)`, `POST(...)` or the history-page URL). Read literally:
     "seed", "seeded", "incubated", "co-founded", "founding investor" read Seed; "Series A", "A round", "first
     institutional round" read Series A; "first round" or "initial investor" for a company of the 1970s to 1990s
     reads Series A only where nothing suggests an earlier seed (say so in the note); "Series B" and later, "second
     round", "third round", "later round", "mezzanine", "expansion", "pre-IPO", "growth" read Growth;
   - a cited round naming Bessemer (`web_verified`): press, the company's release, an S-1 (use `FTS()` where the row
     shows full-text hits), Wikipedia's funding sentence (`W()`), found with
     `NQ_TAG=<TAG> python3 nq.py <slug> '"<Company>" Bessemer Series'` or `wikifetch.py`;
   - a round you can name from knowledge without a page in hand (`model`, confidence medium), with the round and
     year in the note.
   Record the round in `rounds=[rnd(...)]`. Still unknown after that: leave `undetermined` and say in the note what
   you searched. Never infer from the year, the check size, the sector or `stage_site`.
   Rows first seen in 2010 or later deserve real research (one or two news queries each); for rows before 1995 the
   firm's own text is usually all there is, so read it closely and move on.
2. **Entry date**: from the round's citation; else the firm's own `invest_date` (not a January 1 placeholder) or
   `invest_year`.
3. **Status** where it is `unknown` or missing: find what became of the company (acquired by whom and when, shut
   down, still private, listed). The archive's "(acq. by X)", exit year and description are the firm's own record.
   One Wikipedia or news lookup per row; if nothing, leave `unknown` with a specific note.
4. **City and country** where the row carries `city_unknown` or no city and a source places the company.
5. **Seed entries**: `graduated` only with a cited later named round; `censored` for entries after 2024-10-01;
   otherwise say "Graduation left for the graduation pass."
6. **Membership**: if the evidence shows the row should not be a member (the firm's own text says the company was
   already public when Bessemer bought in and no earlier private round exists: T3 / R3; a control purchase: R1; stock
   received for a portfolio company: R6; a fund: D7), write a `not_member` verdict with basis and citation instead of
   a classification line, and list it in your report.

Emit a classification line ONLY for rows where you change something, with only the keys that change plus a
one-sentence note (plain prose, no em-dashes). Do not re-emit unchanged rows. Never record the same file twice
after it succeeded (notes would be replaced); split into files of at most 25 rows (`<TAG>a`, `<TAG>b`, ...) and run
each with `NQ_TAG=<TAG> python3 judgments-<TAG>a.py`, reading record's whole output and fixing any REJECTED line.

WebSearch: at most 5 calls. Prefer nq.py (Google News), wikifetch.py, secget.py, WebFetch.

Report in under 250 words: how many stages you decided (by source class), statuses settled, verdicts changed,
rows still undetermined (count only, plus up to ten names a human could settle), anything wrong in the base.
