# Graduation brief: PRO-80 Bessemer Venture Partners, the S2A column

You decide `seed_to_a_graduation` for a list of Seed-entry rows and record them. Work only in
`/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/` (cd there for
every command).

## Hard limits
Same as JUDGE-BRIEF.md (read its "Hard limits": no git, no edits outside your own judgments file, NQ_TAG on every
nq.py or judgments run, citations only from helpers or tool output, plain prose, no em-dashes). WebSearch: at most
3 calls.

## Read first
1. `../../../COLLECTION.md` section 6 `### seed_to_a_graduation (S2A)`: find it with
   `grep -n "^### seed_to_a_graduation\|^### hq_country" ../../../COLLECTION.md` and read that line range. It
   decides; this brief only summarises.
2. `judge_lib.py` (whole): `cls(...)` (grad, grad_src, grad_cite, grad_conf, grad_asof, surfaces, entry_date,
   rounds), `rnd(...)`, and the S2A helpers at the end: `FORMD_ROUNDS(slug)`, `FORMD_CITE(slug, i)`,
   `GRADLINES(slug, ...)`.
3. `../documentation/decisions.md` (skim: the boundary rulings).

## Per row
Evidence: `python3 show.py --list <your file>` (the row with what is stored, the firm's posts, the archive, sibling
rows), `graduation-surfaces.json[slug]` (Google News, TechCrunch, Crunchbase News results:
`python3 -c "import json;print(json.dumps(json.load(open('graduation-surfaces.json')).get('<slug>'),indent=1)[:4000])"`),
the queue item's `formd_graduation` and `graduation_evidence` (in `queue/queue.json`, find the item by slug) and
`FORMD_ROUNDS(slug)`.

Decide one of:
- `graduated`: (a) the Form D layer says graduated and the later filing is a real later round (sale date more than
  90 days after the entry's; at least max(2x entry, $5M)): `grad_src="formd"`, `grad_cite=FORMD_CITE(slug, i)` of
  that later round, `grad_conf="high"`; or (b) a cited later round that the record NAMES a Series A or later (any
  amount), or an unnamed round above the era's threshold ($5M for an entry to 2014, $8M 2015-18, $12M 2019-21, $16M
  from 2022): `grad_src` web_verified (press, SEC) or first_party (the firm's own post), `grad_cite` via
  NEWS / GNEWS / POST / W, and add the round to `rounds=[rnd(date, round, amount, lead, firm_in_round, cite,
  "press"|"firm")]`.
- `not_graduated`: the absence test, all of: the entry is older than 24 months (read a bare year at its LAST day),
  or a cited acquisition or shutdown ended the company inside the window; `grad_asof="2026-10-06"`;
  `surfaces=GRADLINES(slug, ...)` after you have CHECKED each line (the helper's "none names a later round" is a
  default: read the posts and headlines and pass `firm_note=` / `formd_note=` or `extra=` where the default is
  wrong or thin; add `extra` lines for a sibling row, Wikipedia or the company's site if you used them).
  `grad_src`: "formd" when the Form D absence decides (entry after September 2008, the company files in the US,
  the layer says not_graduated); "web_verified" when a cited acquisition or shutdown is the terminal event (then
  `grad_cite` is that citation); "absence_check" otherwise (entry from 2005 on). A pre-2005 entry takes a no only
  from a cited terminal event (a sale or shutdown before any Series A).
- `censored`: entry after 2024-10-06 and no later round found.
Always give `entry_date` (keep the row's; correct it only with evidence). Sibling rows are surfaces too: if a
sibling names the later round, that decides the row. A vendor page (a Crunchbase profile, PitchBook, Tracxn,
Dealroom, GetLatka) never cites a graduation or carries a no. A row that is $1B or more, or public, cannot end
`not_graduated` (it raised later rounds: find and cite one).

If the evidence shows the entry stage itself is wrong (the firm entered at the Series A, not the seed), fix the
stage with its citation instead (`stage`, `stage_src`, `stage_cite`, `entry_date`) and say so in your report: a
non-Seed row needs no graduation.

Emit only the graduation keys (and entry_date, rounds, flags, and a note that starts from the row's existing note
and adds one sentence such as "S2A: graduated, the $12M Series A of March 2016 (TechCrunch)." or "S2A: not
graduated; the absence test of 2026-10-06 found no later round."). Do not touch status or valuation.

## Finish
Write `judgments-<TAG>a.py`, `judgments-<TAG>b.py` (at most 15 rows each) ending `jl.write("<TAG>a", lines)`, run
each with `NQ_TAG=<TAG> python3 judgments-<TAG>a.py`, read record's whole output and fix any REJECTED line (record
enforces the contract; a rejected file records nothing). Never record a file twice after it succeeded.
Report in under 200 words: counts per value, rows where a post or sibling overturned the Form D layer, stages you
corrected, rows you could not decide (say why), WebSearch calls used.
