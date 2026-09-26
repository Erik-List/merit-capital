# Point Nine run notes (PRO-101), scratch — regenerable

Resume: re-read `data/collection/COLLECTION.md`, then
`python3 scripts/run.py status --investor point-nine`, then continue at the
first pending batch. Rulings live in `documentation/decisions.md` (D1–D13).

Kickoff 2026-09-26 18:54Z. Usage at kickoff: 5-hour 18%, weekly all-models
21%, weekly Fable 4%, extra usage EUR 9.29 of 50 (plan Pro).

## Evidence on disk (durable, under sources/)
- site/webflow-companies.json (193 live cards, P9 INVESTMENT field),
  jobs-board-companies.json (107 Getro), team-webflow.json (14),
  blog-mentions.json (122 companies from 410 posts)
- registers/entities.json (27 North Data entities; Fund I = Team Europe
  Ventures Fund), registers/fund-holdings.json (29 fund->company links)
- edgar/: formd-sweep.json (45 accessions, 32 issuers), fts-hits.json,
  entities.json (8 fund CIKs) at the investor root
- web/: founding-era.json, row-evidence.json (per-row D2 evidence),
  techcrunch-mentions.json (71 companies), visible-slice.json (17 marks),
  recall-candidates.json
- wayback/partner-roster.json (15 curated; to extend from archived team pages)

## Scratchpad helpers (session scratchpad /p9)
pack.py (evidence pack per batch), emit.py (decisions -> two JSONL lines),
pre-verdicts.json (7 D2 rows + Project Europe not_member), draft-site.json,
focus-draft.json, later-rounds.json, techcrunch-p9-full.json, posts/.

## Decided at kickoff
- P9 INVESTMENT label scored 36/40 = 90.0% -> first_party at medium; misses
  are 2011-2013 press-named Series A rounds (Couchsurfing, DocPlanner,
  Humanity/ShiftPlanning, Mambu) -> Series A there.
- Site year is an anchor, not an entry date (Brainly 2012 not 2017; inFakt 2010).
- Rule 10 alignments owed at close: Revolut $115B (a16z, Greylock at $75B),
  Poolside $12B (Redpoint at $3B).
- unicorn_bands false; acquired/defunct rows read below_1b with no figure.

## Next
1. Archive (IA cooldown until ~20:04Z): eras pointninecap.com/portfolio
   (2011-2019), pointnine.com/p9-family (~2019-2023),
   /p9-family-companies/<slug> (~2023-2025), /companies (2024-2025); team
   pages for the roster.
2. Re-run formd-query with the full roster; build base; record
   pre-verdicts; prepare; graduation-surfaces --slugs (site Seed rows).
3. Grind; recall probe; one rebuild; delta; duties; A/B; profile; verify;
   export; review; report; write-back; close.
