# Seedcamp: Build & Reconciliation Report (PRO-83)

**Linear issue** PRO-83 · **slug** `seedcamp` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session · report written 2026-09-30.
**Ingested 2026-09-30 through the §9 gate: 553 companies live, readback exact; Balderton and Greylock re-ingested for aligned rows, YC skipped at its gate (section 15).**

---

## 1. The answers PRO-83 asked for

**`verify.shape` does not need a pre-seed profile.** The only shape guard left is the S2A ceiling
(80%), and a pre-seed book sits far below it: 40.6% on a cohort of 64. The inversion the issue
expected does not happen, because the playbook already takes programme entries out of the cohort
(a `Pre-Seed` entry is not a Seed entry, D3), so the column measures only the firm's named seed
deals. What a mixed pre-seed and seed book needs is a sentence, not a guard: the cohort is 74 of
553 companies (13%), all from the seed-fund years (2014 on), so the published rate describes
Seedcamp's seed investing, not its programme.

**The recall probe scales at this row count, but only its mechanical half.** Parametric
enumeration (about 60 known Seedcamp names plus a control set of famous European
companies the firm did not back) found **zero** missing members. The firm's own Views archive,
read mechanically (1,337 posts, one pass, no web calls), found **8**: 1.4% of the book, every one a
company on neither the live list nor any archived list (section 5). For YC, an order of magnitude
larger, model enumeration will not scale and is not where the misses are. The probe that works is a
mechanical diff of the firm's own publication streams against the base; keep a short parametric
head (the few hundred famous names) as a sanity check only.

**The programme versus the fund holding (the ruling the issue asked for), D2 and D3:** a team the
firm announced as joining the family, investing its standard cheque, is a member at `Pre-Seed` on
the terms of its era, cited to the terms document; Seedcamp Week attendees, finalists and the 2009
Mini Seedcamp winners are not members; a company the firm announces as a seed investment is a
member at `Seed`, cited to the post. From 2018 there is no standard deal, so every entry takes the
round the record names or reads `undetermined`.

| Done-when item | State |
|---|---|
| Plain `verify` green with flagged debt only | `verify --skip-links` clean (153 shared rows agree). Plain `verify` prints one line, "sampled evidence links failing: none sampled": no published row carries a filing link to sample (section 7) |
| Distributions against the pre-seed shape | Section 2; no guard fired |
| Profile through the taxonomy gate | `build-firm-profile.py` and `profile_copy.py` ok; every field sourced (section 9) |
| `review.html` rendered | Served on the review surface: 553 rows, profile panel, no console errors |
| `report.md` | This file |
| COLLECTION.md diff proposed | Section 12 (not applied: the playbook belongs to the tooling session) |
| Ingest through the §9 gate, sibling rows aligned | Done: 553 live, readback 0 differing cells; Balderton and Greylock re-ingested, each exact; YC skipped at its gate (section 15) |

## 2. Results

**553 companies** (575 member verdicts, 22 of them name variants folded by the rebuild), all
nameable.

| Status | Count | | Valuation | Count |
|---|---|---|---|---|
| Private | 301 | | below $1B | 541 |
| Unknown | 147 | | $1B+ | 9 |
| Acquired | 73 | | $10B+ | 2 (Wise, Fluidstack) |
| Defunct | 30 | | $100B+ | 1 (Revolut) |
| Public | 2 (Wise, UiPath) | | | |

Entry stage: **Pre-Seed 278** (the programme and the named pre-seed rounds), **Seed 74**, Growth 1
(Function Health, via Select), **undetermined 200** (a nameable company whose round no source ties
to the firm; they keep their status and band). Countries: GB 291, FR 50, DE 38, US 38, then 38 more
countries; 528 of 553 rows carry a city.

The shape is the pre-seed prior the issue named: mostly small (98% below $1B), a large quiet
share (147 unknown, 30 defunct), and a long European tail. 27% of the book is `unknown`: companies
from the 2007-2016 programme that left no trace. That is a correct reading, not a coverage gap.

### S2A block

Of **74 seed entries, 10 were too recent to count; of the 64 that remain, 40.6% (26) raised a later
round.** Of the 38 that did not, 0 rest on the filings, 10 on a cited end (an acquisition or
insolvency with no later round before it) and 28 on a dated search of the named surfaces
(`scripts/graduation-surfaces.py`, 2026-09-30: two Google News searches, TechCrunch, Crunchbase
News and the local-language edition, plus the firm's archive and sibling rows). Coverage 100%.

## 3. The boundary

One adviser, Seedcamp Investment Management LLP (SEC ERA CRD 330799, FCA 628313), managing
Seedcamp III to VI, the opportunity vehicles and, since 2026, Fund VII and Select (D1). The
corporate Fund I and II entities, the Select fund and the opportunity vehicles are inside; the
AngelList syndicate SPVs never make a member on their own (D6); LP stakes are out (R5).

## 4. Coverage per evidence regime

- **The firm's own record carries the book.** Live list: 327 companies with the firm's investment
  year. Archived lists 2008-2024 read from **Common Crawl** (1,002 captures, 0 failed): the
  Internet Archive held a machine-wide cooldown for the whole run (re-armed to eight hours), so
  **no Wayback era was pulled**; the CC captures bracket every year the site published a list.
  Views archive: 1,337 posts with text, 211 cohort rows curated from them.
- **EDGAR and Form D are nearly silent** (European companies, board-observer seats only): 26
  Form D rows, all `not_member` (real-estate and mining issuers named after a person, D8), plus
  the fund's own Seedcamp V filing.
- **The UK register** (Companies House, D11) supplied dissolutions for 20+ status calls.
- **Press**: Bing News RSS (the shared Google News budget was saturated by a sibling session in the
  first hours) for the grind, Google News through the graduation surfaces for S2A.

## 5. Recall probe and measured recall

- **Parametric enumeration**: about 60 Seedcamp names from memory, by era and sector, plus a control
  list: 0 missing.
- **The firm's Views posts** (`scratch/views-candidates.json` and the year-in-review "new to the
  Nation" lists): **8 additions**, landed at the one rebuild as recall additions with the post as
  the citation: Arcane (pre-seed, 2023), Kern AI (seed 2023, acquired by Accompio 2025), MindLabs,
  Ourspace (pre-seed 2022), Recurse ML, Salesroom (seed 2022), Specify, Troop. A ninth, Granular
  Energy, turned out to be the live list's "Granular" and was withdrawn.
- **Rejected candidates**: Plum, Lexoo, Finimize, Hassle, Yoyo (named in posts as examples or
  podcast guests, no investment shown); the 2013 and 2015 Seedcamp Week attendee lists (D2).
- **Measured recall of the site layers**: 545 of 553 (98.6%).

## 6. Method deltas

1. **Acquirer pages are a parser trap.** The 2017-2024 `/acquirer/<name>/` template has a footer
   ("Social", "Address") that the first parser read as the sold company's name; two artifact rows
   (`social`, `address`) were ruled `not_member` and the parser now takes only a heading before
   "This company has been acquired".
2. **Renames are the main identity problem on a list this old.** 17 rename pairs were found in the
   grind (R2); the firm keeps the logo slot when a card is renamed, so the same logo-upload month
   plus the same one-line description is a reliable merge signal.
3. **An acquirer can take over a sold company's card** (Taxfix on TaxScouts' card, R1).
4. **The Views archive is a membership layer, not only a citation store** (section 5).
5. **`record` concatenates notes on a re-judged row** ("old | new"). 35 rows re-judged after a
   rename or the A/B pass carried both notes, the old one contradicting the new; the classification
   file was rewritten to keep the latest note (write-back 5).

## 7. Flags and debt behind `verify`

- 200 `undetermined` stages (programme-era rows with no cohort post from 2014 on, and 2018+ rows
  whose post names no round). They leave the stage distribution and the S2A cohort only.
- 25 rows with `city_unknown`, three with `country_prior` (Utopia, Ritually, Wombo: GB inferred
  from the London desk, no source places them).
- 13 weak CIK joins quarantined: the pre-filled SEC floats and public flags cleared on each
  (`model_disputes_source`), UiPath the only genuine registrant.
- No Wayback era (section 4).
- **The link sample has nothing to sample.** `verify` samples the first EDGAR and Form D links of
  the published rows and fails when there are none. Seedcamp is the first book with zero: its
  companies file nothing with the SEC and all 26 Form D rows were `not_member`. The check reads an
  absence as a failure; the fix is one line in `run.py` (write-back 7). The ingest gate was passed
  on `verify --skip-links`, as the sibling gates are.

## 8. Standing duties and the A/B pass

- **A/B pass, every public or $1B+ row**, each cited and dated and aligned with sibling books:
  Revolut $115B, Wise $11.83B (2026-09-25), Fluidstack $18B (Forbes, 2026-09-03), UiPath $6.49B,
  Pleo $4.7B, wefox $4.5B, Sorare $4.3B, Synthesia $4B, Function Health $2.5B, 9fin $1.3B, Viz.ai
  $1.2B, Grover $1B. Dust stays below $1B (no published mark), as in the Sequoia book.
- **Invariant 7**: no `not_graduated` on a $1B+ or public row.
- **Unicorn list re-intersected loosely**: no alias missed.
- **Momentum slice**: every headline naming a sub-$1B row with a billion-dollar figure or
  "unicorn" was read (namesakes only: Hubble Network, Varda, Flow Engineering at $750M).
- **Duty 7, 5% blind**: 28 rows (seed 83) re-classified blind; 6 disagreed, all on status or
  country where the blind pass lacked the row's evidence (the firm's exit flag, a live site, the
  register, a cohort post naming Riga). All six adjudicated for the recorded value; no class to
  sweep.

## 9. Firm profile

Built by a profile subagent under the same run, then rebuilt after the team fixes.
- **Thesis**: "By your side from day one." (the homepage headline, read 2026-09-30).
- **History** (63 words): founded in London in 2007 by Saul Klein and Reshma Sohoni with a EUR 2.5M
  fund; among the first investors in Wise, Revolut, UiPath and Synthesia; raised $320M in 2026 for
  Fund VII and Select, about $1B under management.
- **HQ** London (ADV principal office, the site agrees). **AUM** $934.8M (the ADV 7.B composite over
  eight funds, a floor that predates Fund VII) to $1B (TechCrunch, 2026-06-22).
- **Funds**: Seedcamp I (EUR 2.5M, 2007) to Seedcamp VII ($220M) and Select ($100M, 2026).
- **Range** $350K / $2.7M median (63 entry rounds the firm announced with a size) / $5M.
- **Notables**: Revolut, Wise, UiPath, Synthesia, Hopin.
- **Team**: 17 people, every one with a LinkedIn link; Miguel Pinho bucketed by override.
- Flag for the recompute: the portfolio has 49 Media, Gaming & Advertising companies, a sector the
  firm's own tags do not have.

## 10. Open rulings for Erik

1. **E1, warrant-only positions**: 0 rows identified. The firm's posts never say which of its three
   options a company took, so the delta touched nothing; the derivation stands.
2. **Cymmetria**: bought by Stage Fund (Sep 2019), then liquidation filed (Dec 2019). Ruled
   `defunct` (R7) and the YC row aligned; the alternative is `acquired`.
3. **Try.com** enters on Fund II terms from its logo upload month alone (R4).
4. **Finance Fox / wefox**: one investment (merged), entry round `undetermined` because the firm's
   own post puts a Series A before its cohort listing (R3).
5. **Taxfix** out as the acquirer of TaxScouts (R1).
6. **Lua**: the firm lists it exited; the Lua in the 20VC book (2026 seed) ruled a different company.
7. **Mimo, resolved 2026-10-01 on Erik's instruction, in all three books that hold it** (Seedcamp,
   Northzone, Project A): headquarters **Stockholm, SE**. The UK register shows the parent: Omim
   Technology AB (Stockholm, Bolagsverket 559404-0940) owns 75% or more of the UK company Omim
   Technology Ltd (14546072), whose sole director is resident in Sweden. Seedcamp's 2024 review and
   Project A's own record say Sweden; Northzone's card and the UK press say London, the launch
   market and second office. Latest round on record: $8.5M in March 2025 led by Project A; none
   since. Each book re-ingested through the gate, readback exact.

## 11. Rebuilds and deltas

One scheduled rebuild after the recall probe: 553 rows (597 before: 22 merged name variants, 28
`not_member` rows moved to `excluded.json`, 8 recall additions in). One `prepare` then queued the
additions and the S2A needs, finished in two delta files. No membership verdict was made after the
rebuild, so no second rebuild.

## 12. Playbook write-backs proposed (not applied: scripts/ and COLLECTION.md belong to the tooling session)

1. **§3, the recall probe**: make "the firm's own publication stream, diffed mechanically against
   the base" the probe's first leg, and demote parametric enumeration to a head check; state that
   at YC scale the parametric leg is not expected to find anything. (Seedcamp: 8 of 8 misses came
   from the posts, 0 from memory.)
2. **§5, archived lists**: an `/acquirer/` or exit template can carry footer headings; take only
   the heading before the template's own sentence. And: the same logo-upload month plus the same
   one-line description across two names is a merge candidate for `build-company-base.py`.
3. **§1, consideration**: a live-list card that carries an acquired company's line under the
   acquirer's name is the acquired company's card (Taxfix on TaxScouts); the acquirer is
   `not_member` under the sale-consideration ruling.
4. **§6 S2A, mixed books**: say in the published sentence what share of the book the cohort is
   (74 of 553 here), because a pre-seed programme leaves it by rule.
5. **§8, `record`**: a line that restates a whole row (a rename, an A/B pin) should be able to
   replace the note (`note_replace: true`) instead of appending "old | new".
6. **§9, the Internet Archive**: a run that meets the machine-wide cooldown can close on Common
   Crawl when CC captures bracket every list year; say so in the report instead of waiting.

7. **§10 / `run.py verify`**: the link sample should fail on a dead link, not on an empty sample
   (`if bad:` plus a printed note when no published row carries a filing link). A European
   pre-seed book has none by construction.

## 13. Usage line

**Close (Opus 5.5):** five-hour window 100% (resets 2026-10-01 00:40 UTC), weekly 65%, Fable 7%;
extra usage disabled. **Web searches:** about 70 of the 200 cap (the profile subagent 5). The
grind's press ran on Bing News RSS, S2A on the Google News helper, neither capped.
**Subagents:** one (the firm profile).

## 14. Prompt count

**2**: the kickoff ("please collect Seedcamp") and one "continue", after the plan limit cut the run
between the report and the ingest. One context compaction mid-grind.

## 15. Ingest

Run by the session through the gate of COLLECTION.md §9, 2026-09-30 (evening, US Eastern).

- **Preconditions**: `verify --skip-links` clean (153 shared rows: 151 agree, 2 accepted pending
  YC); plain `verify` carries only the empty link sample (section 7). `run.py close`, closing
  commit `ef8c4a46`.
- **Seedcamp**: icon published from the site's Safari mask SVG on its own #00FFAA plate (contrast
  14.4:1, ramp 0.76 px); investor row upserted; dry run "553 upserted (553 new), 0 removed, from 0
  live"; write; **readback: csv 553, live 553, missing 0, extra 0, differing cells 0**. Icon
  provenance committed in `30f99bc2`.
- **Balderton** (Psykosoft `unknown` to `defunct`, Companies House 07531099 dissolved): readback
  before showed that one cell, dry run 0 removed, readback after 0 differing cells; `78c26dcc`.
- **Greylock** (Revolut $75B to $115B, Bloomberg 2026-07-22, as in eight other books): readback
  before showed the three valuation cells, readback after 0; `945864a3`.
- **Y Combinator: skipped at the gate.** Its readback before the write shows a row this run did
  not touch (the csv name " Metadata" carries a leading space, so the tool reports it missing and
  extra), which is a stop condition. The two lines (CustomerOS `private`, Cymmetria `defunct`) are
  ready in `scratch/align/y-combinator.jsonl`; YC's company files were put back to their committed
  state, and the two pairs sit as `accepted` in `companies/cross-rulings.json` with that reason,
  to be removed once YC is re-ingested.
- **Namesakes ruled from YC's side of rule 10**: Miru Labs against YC's miru and Miru ML, Tilt
  against YC's Tilt (Crowdtilt). 72 distinct pairs in all.
