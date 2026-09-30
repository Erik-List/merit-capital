# Verify-all pass after the NEA run (PRO-100), 2026-09-30

**Every investor book not in flight now passes plain `run.py verify`, and each changed book was re-ingested through
the §9 gate with its readback exact.** Atomico, Bain Capital Ventures, Founders Fund and General Catalyst carry
another session's in-flight marker and were not touched.

## What failed and why (12 books, 48 problems, measured before any change)

| Kind | Rows | Resolution |
|---|---|---|
| Rule-10 disputes between two sibling books | 36 pairs (YC 28, Sequoia 3, Lightspeed 2, Accel, Battery, Spark) | 2 judges: 6 stale sides aligned, 46 namesake pairs ruled distinct (plus 6 the alignments surfaced) |
| Censoring window lapsed today (Seed entry September 2024) | 5 (20VC Zekju, a16z Scribenote, Cherry Flinn, Felicis Entalpic and Letta) | 1 graduated (Flinn, its EUR 17M Series A), 4 not graduated on the absence test |
| $1B+ row with an uncited stage and no `cite_pending` | 3 (Lux Aurora Solar, Sequoia Houzz and Rillet, all lifted by the ICONIQ alignment) | marker added |
| Review stale-check false alarm | Khosla | one-line fix in `scripts/run.py` (below) |

Plus the 12 stale rows the NEA gate had skipped (a16z, Accel, Felicis, Lightspeed, YC), now aligned.

## Books written (each: record once, export, review, plain verify clean, cell diff of only the intended rows, dry run 0 removals, readback before of only intended cells, write, readback after 0, three company files committed by pathspec)

| Book | Rows | Commit |
|---|---|---|
| Khosla | Faire $5.2B (November 2025 tender), focus corrected from a substring match; Castle unknown | c4b4f129, 227e6c40 |
| Greylock | Banyan Systems acquired (its businesses sold to Unisys and InfoSpace, 2004) | 0065d7f7 |
| Spark | Plume (Plume Design) $2.6B; YC's Plume ruled distinct | e743b520 |
| Lux | Aurora Solar `cite_pending` | afd1dbc7 |
| Accel | Chaos $4.5B, Sentry $3B, Wallapop acquired (NEA run); KupiVIP defunct | 3e1ade06 |
| Lightspeed | CuspAI $2.6B, Influitive acquired (NEA run); Yubi $1.3B; Faire's citation moved off a vendor page; two countries cited (rule 6) | 875e385c |
| Y Combinator | Minimum acquired, Super private (NEA run); nine rows that carried another company's status or mark corrected (Aspect x2, Castle x2, Magic, Origin x2, Tempo x2, Tilt); 45 namesake pairs distinct; 3 wrong "alignment pending" pairs removed | 5a4188ab |
| First Round | Castle (castle.io) private | 56389c10 |
| Sequoia | Houzz and Rillet `cite_pending`; Root, Versatile, Magic, Origin namesakes distinct | b884cac8 |
| 20VC | ZeKju not graduated | c34d7a4f |
| Cherry | Flinn graduated; headquarters Vienna, AT | 00ef600c |
| a16z | Cowboy Space $2B, Belly acquired, Grubwithus private $3.7B (NEA run); Scribenote not graduated | a6938f6b |
| Felicis | Cleo and Plusmo acquired (NEA run); Entalpic and Letta not graduated; Cleo AI namesakes distinct | 300067c7 |

Battery became clean without a change of its own (Greylock's Banyan alignment settled its pair). NEA's accepted
pairs were all removed, since both sides now agree.

## Left for Erik

1. **`scripts/run.py` fix is uncommitted.** The review stale-check now accepts the published name as well as the
   base name (Khosla's "Academia Inc." publishes as "Academia"). The edit is in the working tree beside another
   session's uncommitted edit to the same file (removing the $1B+ share ceiling); staging only this hunk was refused
   by the auto-mode classifier, so it needs committing by hand or with that session's edit.
2. **YC's readback shows " Metadata" (CSV) against "Metadata" (live).** Ingest trims names, the readback tool does
   not, so the two are the same row (0 differing cells, 0 new, 0 removed). The durable fix is
   `names.published {"metadata": "Metadata"}` in YC's `config.json`, which also carries the other session's
   uncommitted edit.
3. Found beside the pairs, not fixed (each a membership or identity call):
   - Sequoia's `root-inc` rests on a Form D naming Olsen after he left Sequoia (2012): membership doubtful.
   - Greylock holds Banyan twice (a `banyan-systems-incorporated` row and an `epresence` row), and Greylock's and
     Sequoia's `epresence` rows still read defunct.
   - Tiger Global's note mentions a $6M seed in the Colombian Mono, which has no row in its book.
   - Insight's Yubi ($1.5B from a secondary sale) and Plume ($1.35B) marks are off-rule or old; their bands are
     unaffected.
   - Greylock's Cleo carries London, GB; its own card says San Francisco.
