# Graduation brief: five Seed rows whose censoring window lapsed on 2026-09-30 (verify-all pass)

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/verify-all/`.
Each row was `censored` (a Seed entry in September 2024, less than 24 months old) and today its window closed, so
each needs a decided status: `graduated | not_graduated` (COLLECTION.md s6 `### seed_to_a_graduation (S2A)`, at
`../../../../COLLECTION.md`: read it whole before the first row). Rows: `20vc:zekju`, `a16z:scribenote`,
`cherry:flinn-ai`, `felicis:entalpic`, `felicis:letta`.

Per row read the book's stored row (`../../../<book>/companies/classification.json`, `base.csv`, `resolved.json`)
and its publisher surfaces, just refreshed: `../../../<book>/scratch/graduation-surfaces.json` (key = slug). Also read
every other book's row for the same company (grep the name in `../../../*/companies/base.csv`): a sibling that names
a later round decides it.
- `graduated`: a later priced round named Series A or later (whatever the amounts), or an unnamed round at least
  max(2x entry, $5M) (seed amount unknown: the $16M bar from 2022). Cite the round's own announcement (never a vendor
  page); add the round to `funding_rounds`.
- `not_graduated` on the absence test: `graduation_source: absence_check`, `graduation_asof: 2026-09-30`,
  `graduation_surfaces`: one line per surface, `<surface>: <what was searched> -> <what it showed>`, naming the firm's
  own archive (`firm:`), the Form D sequence (`formd:`, US companies), at least two publisher surfaces from the
  surfaces file, and each sibling row (`sibling:<book>`). Or a cited end (a sale or shutdown with the seed as the last
  round): `graduation_source: web_verified`.
Keep the row's `entry_date`; do not change its stage unless a documented round proves the entry was not a Seed.

Write one JSONL file per book, `grad-<book>.jsonl`, one line per row: `{"slug", "who": "agent-verifyall-pro100",
"seed_to_a_graduation", "graduation_source", "graduation_citation" (graduated or cited end), "graduation_confidence",
"graduation_asof", "graduation_surfaces" (absence test), "funding_rounds" (only when you add a round; the full list
then), "note"}`. The note is one plain sentence starting "S2A:". Never touch git, scripts/ or any investor's files;
never run `run.py record` (the lead records). Tools: `NQ_TAG=gr python3 ../nq.py <slug> "<query>"`, `../wikifetch.py`,
WebFetch of company pages, `../secget.py` for SEC documents. WebSearch: at most 3 calls. Report in under 150 words:
each row's decision and the fact that decided it.
