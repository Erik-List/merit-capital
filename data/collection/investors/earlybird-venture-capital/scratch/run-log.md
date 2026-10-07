# Earlybird run log (PRO-107)

Kickoff 2026-10-06, about 21:10 UTC. Prompt count so far: 1 ("please collect earlybird").
Usage at kickoff: 5-hour 28%, weekly all models 13%, weekly Fable 4%.

## Incidents

- **2026-10-06 21:30 UTC, mine.** While checking how long the Internet Archive cooldown had left I
  called `shared_throttle.cooldown("ia")`, which SETS a cooldown, instead of
  `cooldown_remaining("ia")`, which reads it. That wrote a 4-hour machine-wide stop over a genuine
  2-hour one with about 2 minutes left. I restored the file to its exact previous content
  ("1791322325.118903 7200.000000 1791315125.118903") about 20 seconds later. A check of whether a
  sibling process had read the wrong value in that window was refused by the permission
  classifier, so that is unverified.
- **2026-10-06 21:33 UTC.** The first replay request after the genuine cooldown expired was
  refused; `ia_fetch` set a 4-hour cooldown (doubled from 2 hours, the tooling's rule), expiring
  about 01:33 UTC on 2026-10-07. One CDX query (earlybird.com/*, 6,310 URL keys) had succeeded at
  21:32. Common Crawl became the archive (Erik 2026-09-26, PRO-158); `scratch/ia_pull.py` (198
  targets) is queued behind the cooldown.
- **Google News RSS answered 503** for this machine from about 23:40 UTC. Research uses Bing News
  RSS (`scratch/news.py`), the publishers' own WordPress search endpoints and WebFetch.

## Layers

| Layer | Result |
| -- | -- |
| Live site earlybird.com (Framer) | 120 companies (`scratch/eb_site.py`) |
| Live site health.earlybird.com | 18 companies |
| Job board jobs.earlybird.com (Getro) | 72 companies, 10 names not on the lists |
| Common Crawl, 33 crawls 2008-2026 | 1,161 captures fetched, 3 failed |
| Archive parse (`scratch/eb_archive.py`) | 274 companies 2008-2026, 140 people, 173 press items |
| IA index of team pages 2001-2013 | roster windows (`scratch/eb_roster.py`), 81 people |
| Form D roster sweep | 110 accessions, 48 issuers; 15 rows reached the base, all name-matches, all `not_member` |
| EDGAR entities | 15: earlybird 2, digital-east 2, external 11 |
| EDGAR full-text sweep | 16 third-party registrants |
| North Data (Handelsregister, RCS Luxembourg) | 81 entities, 28 pages read |
| Bek Ventures portfolio | 37 companies (Digital East identification only) |

## Base

- First build: 314 rows. With the overlay (53 merges, 38 Digital East rows partitioned, 1 reject) and
  the roster trimmed to partners and principals: 222 rows (A 124, B 83, C 15).
- `prepare`: 222 rows queued. 15 name-match rows judged `not_member` cluster-first.
- 11 research agents on the 207 listed rows (`scratch/research/`).

## Resume pointer (read this first after a context compaction)

Re-read `data/collection/COLLECTION.md` and `python3 scripts/run.py status --investor earlybird-venture-capital`.
Erik's writing rules: no em-dashes, answer top-down, plain words. Linear issue PRO-107 (In Progress,
kickoff comment posted). Session scratch tools, all under `scratch/`:

- `eb_site.py` (live sites + team), `jobboard-pull.py`, `cc-cluster.py` + `cc-fetch.py` (Common Crawl),
  `ia_pull.py` (Internet Archive, queued behind the cooldown; log `ia-pull.log`), `eb_archive.py`
  (parses every capture into `sources/wayback/parsed/`, `archive-evidence.json`, `team-years.json`,
  `sources/web/press-archive.json`), `eb_roster.py` (partner roster), `eb_overlay.py`
  (identity-merges.json: merges, Digital East desk, rejects), `eb_pack.py` (evidence pack per row),
  `news.py` (Bing + Google news), `judge_lib.py` (`verdict`, `cls`, `rnd`, `write`),
  `judgments-formd.py` (done).
- Research agents write `scratch/research/<group>.json` (groups: old1 old2 mid1 mid2 late1 late2 new1
  new2 x health1 health2; brief in `scratch/research/brief.md`).

Order of the remaining work:

1. When research files land: write `judgments-<group>.py` per group from the research (verdict line +
   classification line per member; `not_member` verdict for pre-fund, sale-consideration, post-IPO
   rows), record them, `verify --in-flight`.
2. Score the live list's stage label against the documented entry rounds (decisions.md D13).
3. When the IA pull has run: `eb_archive.py` again, `eb_overlay.py`, recall probe (press archive
   names, Wikipedia insource, FTS registrants, Bek list check), then the ONE rebuild
   (`build-company-base.py`), `prepare`, delta grind. Copy `scratch/queue/queue.json` to
   `scratch/queue-before-rebuild.json` first.
4. `graduation-surfaces.py` for open Seed rows, absence tests for the nos.
5. Standing duties (s8), A/B pass on the $1B+ and public rows, momentum slice.
6. Registers east of Germany probe (decisions.md D12) -> `sources/registers/cee-turkey-probe.json`.
7. Profile: team sources in config, `firm-offices.py`, ADV 7.B funds, `build-firm-profile.py`, icon
   (`fetch-investor-icon.ts --discover https://earlybird.com`).
8. `names.published` in config, `verify`, `export`, `review`, report.md, `run.py close`, closing
   commit (explicit pathspec of this investor's directory only), ingest gate (s9), sibling
   alignment, Linear comment, memory file, closing message (must report the cooldown incident above).

## 2026-10-07 03:45 UTC: session restarted

- The Claude Code process ended around 00:15 UTC (a network error took two agents first) and the
  session resumed on Erik's "continue". **Prompt count: 2.**
- Research files held 64 of 207 rows at the restart; all 12 agents (11 row groups + profile) were
  resumed from their transcripts.
- Internet Archive: the queued pull fetched 10 pages after the 01:33 expiry, then hit a refusal
  (rc7) and stopped; another refusal set a 4-hour cooldown until about 07:40 UTC. The pull
  (`scratch/ia_pull.py`, 173 targets left) is queued behind it again. If it has not landed by the
  rebuild, the 2001-2007 listing years are debt, named in the report.
- Google News answers again (200).
- Still to do from the resume list above: everything from step 1.

## 2026-10-07 about 05:30 UTC: state (resume here)

Done: all 11 research groups recorded through `scratch/judge_research.py <group>` (rulings in
`scratch/overrides.json`); graduation decisions (`judgments-graduation.py`, absence tests on
`eb-surfaces.json`); wrong public joins fixed (nortech, tilt, versus); momentum slice recorded (24
rows); cross-rulings written (8 distinct, Curio vs Cherry accepted until aligned at ingest); A/B
attack searches run on N26, Aiven, Black Forest Labs, Recursive, Sennder (no change); rulings R1-R8
in decisions.md; stage label scored and refused (`scratch/field-score.json`); REBUILT (two builds
back to back; verdicts the re-key moved were repaired by hand): base 195 rows, 38 other_desk, 35
not_member; `prepare` 2 queued 9 delta rows; Sennder recorded as member. Profile built
(`investor/investor.json`, `sources.json`; copy check ok; icon dry-run fine,
source https://framerusercontent.com/images/wO8t3YzeoaLIe7QfeB1G6Ajm4.png); `names.published` set
(41). WebSearch used so far: about 91 of 200.

Open:
1. Delta research agent (8 rows from the 2001-2007 page index: asyntis, europroteome, internetwork,
   intime, iq, iscribe, music-united, vital-sensors) writes `scratch/research/delta.json`; then
   `python3 scratch/judge_research.py delta` with overrides (unidentified rows: member on the
   firm's page, flagged identity_unresolved, status unknown, all three outcome columns
   undetermined), add published names.
2. IA pull still queued (cooldown to about 07:40 UTC). If it lands: `eb_archive.py`, check new
   names against the base, judge additions, final rebuild. If not: debt in the report.
3. Remaining duties: duty 7 blind 5% re-judge (a subagent), same-company-other-names check
   against siblings, `stale` flag on aiven, Wikipedia insource sweep (`scripts/wikipedia-insource.py`),
   FTS registrants read (Northern Technologies, Alnylam, Tech Data, Kleopatra, Flamel, Openwave).
4. `verify` (plain), `export`, `review`, report.md, write-back proposal, `run.py close`, closing
   commit (pathspec of this directory only), ingest gate, sibling alignment (Cherry Curio defunct;
   General Catalyst Interaction acquired; Creandum Terralayr graduated; YC/others per verify),
   Linear, memory, closing message (report the cooldown incident and prompt count 2).

## 2026-10-07 04:40 UTC: STATE AT CONTEXT COMPACTION (resume from here)

DONE: all 195 base rows judged and classified; plain `verify` CLEAN (`scratch/verify-1.log`);
`export` and `review` written and the review page checked rendered (server `review-surface`, port
8931, 210 table rows, profile panel, no console errors). Delta rows recorded (8 early-2000s
companies identified by research + Sennder). Profile built and copy-checked; icon dry-run fine
(source https://framerusercontent.com/images/wO8t3YzeoaLIe7QfeB1G6Ajm4.png). Recall probe written
(`sources/web/recall-probe.json`, `sources/edgar/fts-reading.json`). Linear PRO-107: kickoff +
milestone comments posted. Prompt count 2. WebSearch about 101 of 200 used.

Numbers (verify): 195 companies; private 99, acquired 60, defunct 32, public 4; $1B+ 6 (Aiven
$3.0B, Black Forest Labs $3.25B, Isar Aerospace $2.31B, N26 $9.0B, Recursive $4.65B, Sennder $1.0B);
entry stage Seed 51, Series A 50, Growth 15, Pre-Seed 15, undetermined 64 (all 131 stages
web_verified); S2A 51 seed entries, 11 censored, cohort 40, graduated 19 (17 web_verified, 2
first_party), not graduated 21 (9 cited end, 12 absence test), rate 47.5%; flags stale 3,
model_disputes_source 6, cik_weak 1, stage_disputes_band 2; countries DE 101, US 24, GB 16, CH 16,
FR 9. Excluded: 38 other_desk (Digital East), 35 not_member, 1 build filter.
Usage: kickoff 5h 28% / weekly 13% / Fable 4%; at 04:40 UTC weekly 24% / Fable 5%.

STILL TO DO, in order:
1. Duty 7: the blind re-check agent writes `scratch/duty7-blind.json` (10 rows: mona-ai,
   madvertise, gmd, yoom, payable, terralayr-ag, alantos-pharmaceuticals, oviva,
   everoad-by-sennder, curio). Compare with classification.json on status / band / city /
   country / stage; adjudicate disagreements; re-export if a row changes.
2. Write `documentation/report.md` (model: hv-capital/documentation/report.md): method, results
   (S2A five numbers and what the nos rest on), coverage per evidence regime, decisions D1-D13 and
   rulings R1-R8, the register probe (CZ and SK usable, TR not), debt (IA 2001-2007 lists unread:
   `scratch/ia_pull.py` queued, cooldown until about 07:40 UTC; 64 undetermined stages; RhodeCode
   Series A only in Wikipedia), incidents (my `cooldown()` slip, restored in 20 s; network restart),
   open rulings (max 3: D2 Digital East out is decided but flagged; Sennder as own row; CrossLend
   defunct at medium confidence), write-back proposals (CZ/SK registers for s5; eb_overlay
   stability lesson: generate overlays from base + excluded + absorbed; record's re-key moved Snyk's
   verdict onto Sennder; Framer search-index parser; Bing News fallback), usage line, prompt count 2.
3. `python3 scripts/run.py close --investor earlybird-venture-capital`; closing commit with explicit
   pathspec `data/collection/investors/earlybird-venture-capital` only (no add -A).
4. Ingest gate (COLLECTION.md s9): `npx tsx scripts/fetch-investor-icon.ts earlybird-venture-capital
   <icon url>`, `npx tsx scripts/ingest-investor.ts earlybird-venture-capital`, `npx tsx
   scripts/ingest-companies.ts earlybird-venture-capital --dry-run`, removal check, write, readback
   (`data/collection/investors/20vc/scratch/align/readback.ts earlybird-venture-capital
   --investor-row`). If the permission classifier refuses the DB write: do not work around; list
   the commands in the report and tell Erik.
5. Sibling alignment (write each book with `run.py record --investor <book>`, export, commit its
   three company files, re-ingest through the gate; skip books with an in-flight marker: atomico,
   bain-capital-ventures, general-catalyst, speedinvest, founders-fund):
   - cherry `curio`: status defunct (creditors' voluntary liquidation 2025-05-30, Companies House
     10145832); then remove the `accepted` pair from `companies/cross-rulings.json`.
   - battery-ventures `Number26`: same company as n26; 1b_plus $9.0B (2021-10, TechCrunch Series E).
   - lakestar + northzone `CrossLend`: defunct (2023 wind-down; medium confidence).
   - creandum `terralayr`: graduated (EUR 77M Oct 2024 and EUR 192M Jan 2026 rounds).
   - general-catalyst Interaction (acquired by Cognition 2026-07) and speedinvest Inkitt city (San
     Francisco): in-flight books, report only.
   - add `distinct` rulings if verify flags Hive (8vc, general-catalyst, y-combinator) after export.
6. Linear PRO-107 closing comment + status Done; memory file `earlybird-run-pro107.md` + MEMORY.md
   line; closing message to Erik (top-down; results, what was ingested, open rulings, the two
   incidents, prompt count 2).

## Duty 7 result (2026-10-07 04:50 UTC)
Blind re-check of 10 rows (`scratch/duty7-blind.json`): 9 agree on status, band, country, stage;
1 status disagreement (yoom: founder bought the assets out of insolvency -> `acquired`), swept as a
class (smoodoos.com, same shape -> `acquired`), both flagged `unstable`; GMD city kept Munich (the
blind pass gave Berlin, the seat after the merger). Recorded in `queue/duty7-adjudication.out.jsonl`.
NEXT: `run.py export` + `review` again, plain `verify`, then steps 2-6 of the list above.
2026-10-07 05:00 UTC: stopped the queued `scratch/ia_pull.py` (pid 64247, still waiting behind the
machine-wide Internet Archive cooldown) so that no file lands in a closed book. The 173 remaining
targets are debt: rerun `python3 scratch/ia_pull.py`, then `scratch/eb_archive.py`, when the archive answers.

## 2026-10-07 05:40 UTC: CLOSED AND INGESTED
`run.py close`; closing commit e3ff87f1; gate corrections c75c53b6 (CrossLend defunct -> private on
the register; yoom and smoodoos.com status citations; two Y Combinator namesakes ruled distinct).
Ingest through the s9 gate: icon uploaded, investor row upserted, 195 companies written, readback
exact. Siblings aligned and re-ingested, each exact: cherry (Curio defunct, d9a3de0f),
battery-ventures (Number26 $9B + cited Series B entry, 82c481f5), creandum (terralayr graduated,
c247a95d). Earlybird rulings: 13 distinct, 1 same, 0 accepted. Report section 16 has the table.
Left: Linear PRO-107 closing comment + Done, memory file, closing message.
