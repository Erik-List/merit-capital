# Graduation brief: PRO-162 Bain Capital Ventures, the S2A column on the delta

You decide `seed_to_a_graduation` for a list of Seed-entry rows (your list is in `grad-split.json`, key A or B) and record
them. Work only in `/Users/erik/Developer/merit-capital/data/collection/investors/bain-capital-ventures/scratch/`.

## Hard limits
Same as JUDGE-BRIEF.md (read its "Hard limits": no git, no edits outside your own judgments file, NQ_TAG on every nq.py or
judgments run, citations only from helpers or tool output, plain prose, no em-dashes). WebSearch: at most 10 calls.

## Read first
1. `../../../COLLECTION.md` lines 1610-1780 (the S2A contract). It decides; this brief only summarises.
2. `judge_lib.py`: `cls(...)` (grad, grad_src, grad_cite, grad_conf, grad_asof, surfaces, entry_date, rounds), `rnd(...)`,
   and the S2A helpers at the end: `FORMD_ROUNDS(slug)`, `FORMD_CITE(slug, i)`, `GRADLINES(slug, ...)`.
3. `judgments-4.py` for graduated examples (nightfall, orum, relay-financial).

## Per row
Evidence: `python3 show.py <slug>` (the row, its posts, siblings), `graduation-surfaces.json[slug]` (Google News, TechCrunch,
Crunchbase News results), `../companies/resolved.json[slug]["formd_graduation"]` (the Form D layer's verdict, when the
company files in the US) and `FORMD_ROUNDS(slug)`, `../companies/classification.json[slug]` (stage, entry_date, status, note).
Read the firm's posts that mention the company (`../sources/site/insights-text.json`): a post often announces the Series A.

Decide one of:
- `graduated`: (a) the Form D layer says graduated and the later filing is a real later round (sale date more than 90 days
  after the entry's; at least max(2x entry, $5M)): `grad_src="formd"`, `grad_cite=FORMD_CITE(slug, i)` of that later
  round, `grad_conf="high"`; or (b) a cited later round that the record NAMES as a Series A or later (any amount), or an
  unnamed round above the era's threshold ($5M for an entry to 2014, $8M 2015-18, $12M 2019-21, $16M from 2022):
  `grad_src` web_verified (press, SEC) or first_party (the firm's own post), `grad_cite` via NEWS/POST/W, and add the round
  to `rounds=[rnd(date, round, amount, lead, firm_in_round, cite, "press"|"firm")]`.
- `not_graduated`: the absence test, all of: the entry is older than 24 months (read a bare year at its LAST day), or a
  cited acquisition/shutdown ended the company inside the window; `grad_asof="2026-09-27"`; `surfaces=GRADLINES(slug, ...)`
  after you have CHECKED each line (the helper's "none names a later round" is a default: read the posts and headlines and
  pass `firm_note=`/`formd_note=` or `extra=` where the default is wrong or thin; add `extra` lines for a sibling row,
  Wikipedia or the company's site if you used them). `grad_src`: "formd" when the Form D absence decides (entry after
  September 2008, company files in the US, the layer says not_graduated); "web_verified" when a cited acquisition or
  shutdown is the terminal event (then `grad_cite` is that citation); "absence_check" otherwise (entry from 2005 on).
  A pre-2005 entry takes a no only from a cited terminal event.
- `censored`: entry after 2024-09-27 and no later round found.
Always give `entry_date` (keep the row's; correct it only with evidence). Sibling rows (`sib` lines, and
graduation-surfaces siblings) are surfaces too: if a sibling names the later round, that decides the row.
A vendor page (Crunchbase profile, PitchBook, Tracxn, Dealroom, GetLatka) never cites a graduation or carries a no.

Emit only the graduation keys (and entry_date, rounds, a note line starting from the row's existing note if you add to it,
flags). Do not touch status, valuation, stage unless the evidence shows the stage itself is wrong (then say so in your report
instead of changing it).

## Finish
Write `judgments-grad-<A|B>.py` calling `jl.write("grad-<a|b>", L)`, run it with `NQ_TAG=g<a|b>`, fix any REJECTED line.
Report in under 200 words: counts per value, rows where a post or sibling overturned the Form D layer, rows you could not
decide (say why), WebSearch calls used.
