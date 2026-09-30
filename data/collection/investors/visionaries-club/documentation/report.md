# Visionaries Club: Build & Reconciliation Report (PRO-103)

Run of 2026-09-30, one session, slug `visionaries-club`. **Status: collected, plain `verify` clean; NOT yet closed or ingested** (the session hit its usage limit). Remaining: finish this report, `run.py close`, the closing commit, then the §9 ingest (icon upload from https://www.visionaries.vc/favicon-new.svg, `ingest-investor.ts`, `ingest-companies.ts --dry-run`, write, readback).

## Results
- 76 companies: 59 on the live visionaries.vc, 10 on tomorrow.vc, 4 from the 2023-25 WordPress archive, 6 recall additions (Tytan, ContextFab, Acapela from the German register; Conveo, Fina, Trana from press).
- Status: private 65, acquired 7, defunct 3, unknown 1. $1B+: Lovable ($13.3B), n8n ($5.2B), Black Forest Labs ($3.25B), Proxima Fusion ($2.74B), Miro ($1.79B, Bending Spoons deal unclosed), Choco ($1.2B, stale), Pigment ($1.0B, stale).
- Entry stage: Seed 18, Pre-Seed 12, Growth 11, Series A 10, undetermined 25.
- **S2A: 18 seed entries, 5 censored, cohort 13 (entries 2021-02 to 2025-02), 7 graduated, 6 not graduated, rate 53.8%**; the six nos rest on the absence test. The cohort is young and small; read the rate with that date range.
- Rule 10: 74 shared rows, 71 agree, 3 accepted as stale on the other side (Rows at Accel and Cherry, Two at Sequoia; those books fail their own verify on unrelated pairs, so not aligned).
- Profile built: HQ Berlin, AUM $193.1M (ADV 7.B) to $515.2M (committed), median entry round $10.0M (press-based, 43 rounds).

## Open rulings for Erik (decisions.md R1-R10)
1. **R1 Personio ruled `not_member`** as a partner-carried La Famiglia deal (Menlo rule): Lacher's own bio credits it to La Famiglia; no round names Visionaries. Moves an $8.5B row.
2. R2 stage by construction (Miro, Rows = Growth because their Series A predates the firm).
3. Pallery flagged `unstable` after the blind duty-7 check (3 of 4 agree).

## Method notes (write-back candidates)
See scratch/run-log.md: North Data fund pages as a forward register layer; Deutsche Startups WP search API as a recall layer; the Gatsby 2020-22 site had no portfolio list (links to Crunchbase); the IA blocked this machine three times (60, 120, 480 min); `formd-query.py` misses compound surnames (scratch/formd-query-compound.py found Ziggiz's Form D; a second rebuild landed it); `run.py verify` fails "none sampled" on a book with no SEC links.

## Usage and prompts
Usage at kickoff: weekly 15%, Fable 1%. Prompt count: 1 so far (the kickoff).
