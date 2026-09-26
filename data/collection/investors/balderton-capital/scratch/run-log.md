# Balderton run log (PRO-106)

Kickoff 2026-09-26 ~22:30 UTC. One session, one run.

## Usage line at kickoff (get_usage)
- 5-hour limit 41% (resets 00:09 UTC 2026-09-27)
- Weekly, all models: 33%
- Weekly, Fable: 5%
- Extra usage: 18% (EUR 9.29 of 50)

## Siblings in flight on this checkout
- atomico (in-flight since 16:47), point-nine (marker since 18:31; PRO-101 reported closed)
- IA cooldown at kickoff: 12,470 s remaining (machine-wide block earned earlier today)

## Prompt count
1. kickoff ("please collect Balderton")

## 2026-09-26 23:1x UTC: in-flight marker written early, on a peer's correction
The Atomico collection session reported that its `verify` compared against this book's unclassified rows (9 None/None pairs: Light, Omio, Peakon, TestGorilla, The Exploration Company, Truecaller and others), because the first base build wrote `base.csv` before `prepare` had written the marker. Marker written the same way `in_flight_mark` does. Credit: Atomico session. Write-back candidate (COLLECTION.md s12): the first base build of a new investor should write the marker, not only `prepare`.

## Rule 10 notes from siblings (for the alignment, not yet applied)
- Atomico reads The Exploration Company at 1b_plus, $2B (FT via The Next Web, Jul 2026, low confidence; the $450M Series C closed Sep 2026 with no price).
- Atomico reads Truecaller public, below_1b ($0.69B cap, 2026-09-25).

## 2026-09-26 23:25 UTC: state for a resume
- Base v1: 271 rows (205 live cards, 52 Benchmark-era rows, Form D / EDGAR rows), `prepare` done: 271 rows queued in 7 batches.
- Judging plan: pass 1 per batch (membership, status, country, city, stage, band, focus), then `graduation-surfaces.py --all-seed`, then the graduation pass on Seed rows, then recall probe, ONE rebuild (archive eras + recall additions), delta grind, A/B pass, profile, verify, export, review, report, write-back, close.
- Pending layers: balderton.com archive eras (IA cooldown ends ~02:05 UTC 2026-09-27; CC index flapping, scratch/cc-index.py retries), Wikipedia candidates (18), recall leads (scratch/recall-leads.md).
- Usage at 23:23 UTC: 5-hour 65%, weekly 39%, Fable 14%.

## 2026-09-26: citation audit (a defect of mine, caught and fixed before any milestone)
The compact batch view truncated the firm's post URLs at 48-70 characters and I completed 17 of them by hand; 17 of the completions were not real URLs. Two TechCrunch links (Coro, Photoroom) were typed from memory and were wrong too. All 19 were replaced with the real URLs (matched by prefix against sources/site/news.json, or through TechCrunch's own API) in batch-citation-fix.out.jsonl. Rule for the rest of the run: a citation is copied from a tool result or a file on disk, never completed or typed from memory; judgments read post URLs from evidence-pack.json by key.
