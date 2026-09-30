# Delta brief: PRO-100 NEA, the post-rebuild delta (graduation pass, recall rows, leftovers)

Read `JUDGE-BRIEF.md` first: its hard limits, membership rules and classification contract all apply. This file adds
the graduation pass and says what differs. Work only in
`/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`.

Skip these rows, the lead handles them: `glacier-bay-inc`, `viracta-therapeutics-formerly-sunesis`.

## 1. The graduation pass (every item whose `need` has `seed_to_a_graduation`)
Read COLLECTION.md section 6 `### seed_to_a_graduation (S2A)` (from that heading to `### ` after it) before the first
row. Every Seed entry leaves with exactly one of `graduated | not_graduated | censored`; this pass MAY write
`not_graduated` (the old "never write not_graduated" line in JUDGE-BRIEF is lifted here), but only with a complete
absence test. The per-row order:
1. Confirm the Seed entry and its `entry_date` (required on every decided and censored row). `show.py` prints the
   Form D layer's verdict as `grad:`. A no or yes from that layer is `grad_src="formd"`, citation the accessions
   (`grad_cite=FORMD_CITE(slug, i)` for the later round, or the entry filing for a no), and your answer must agree
   with the layer. A filing whose sale date is within 90 days of the entry's is a close of the same round.
2. `graduated`: a later priced round NAMED Series A or later graduates whatever the amounts; an unnamed round must
   be at least max(2x entry, $5M), where an unknown seed amount takes the era ceiling ($5M for an entry to 2014, $8M
   2015-18, $12M 2019-21, $16M from 2022). Cite it (`first_party` or `web_verified`, never a vendor page) and put the
   round in `rounds=[rnd(...)]`.
3. `censored`: `entry_date` less than 24 months before 2026-09-30, read at the LATEST day it can mean (a bare 2024
   is 2024-12-31, so censored). A cited acquisition or shutdown decides a row inside the window.
4. `not_graduated`: either a cited terminal event (acquisition or shutdown) with the seed as the last round
   (`grad_src="web_verified"`, `grad_cite` the event), or the absence test: `grad_src="absence_check"`,
   `grad_asof="2026-09-30"`, `surfaces=jl.GRADLINES(slug, ...)` (firm, formd, the publisher surfaces from
   `graduation-surfaces.json`, and sibling rows; READ what it returns and add `extra=[...]` lines for anything you
   searched yourself). An absence_check needs an entry from 2005 on. Read every sibling row first: a sibling that
   names a later round decides the row (and tell me, so the books are aligned). Before any no, read the surfaces'
   own headlines for the company (`python3 -c "import json;print(json.dumps(json.load(open('graduation-surfaces.json'))['<slug>'],indent=1))"`):
   a headline naming a later round graduates the row, cited to that headline (`GNEWS(slug, "title words")`).
5. A pre-2005 Seed entry with no later round and no terminal event you can cite: do not write it; list it in your
   report.
6. The graduation keys go on the row's ONE classification line together with any other open column; add a short note
   sentence ("S2A: graduated, the $12M Series A in March 2016 (TechCrunch)." or "S2A: not graduated; the absence
   test found no later round (surfaces listed).").

## 2. Membership rows (recall additions)
Each carries its recall basis in the row's `notes` (with a citation). Re-read the cited source; a member needs the
verdict line AND a full classification line (status, band, stage with rounds, entry_date, country, city, focus,
graduation if Seed). The Connect Ventures rows (Deep Voodoo, Music AI, Jomboy Media, TMRW Sports, Blacktag, Boisson,
Camp, Mojito, Sekai, Royal, Spire Animation, OpenSea...) are in under decisions.md's Connect Ventures re-derivation:
confirm each company from Connect Ventures' own list or a round naming NEA/Connect, and judge it like any member.

## 3. Leftovers
Rows needing only status, country, city, band or stage: the JUDGE-BRIEF contract. Rule 10: align with siblings
unless you hold fresher cited evidence.

## Finish
Run your judgments file ONCE (`NQ_TAG=<TAG> python3 judgments-<TAG>.py`); read record's whole output; if REJECTED,
fix and re-run (a rejected file records nothing). Report in under 250 words: counts by S2A status and by source,
verdicts, rows you left (with why), sibling rows that disagree, WebSearch calls used, anything wrong in the base.
