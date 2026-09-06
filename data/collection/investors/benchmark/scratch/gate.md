# Calibration gate — Benchmark (COLLECTION.md §4)

Both sets pre-registered in `golden.json` **before any verdict or `entry_stage`
was written**. The stage key was assembled from external round announcements
(25 web-verified citations, 2026-09-06) and only then compared with what the
deterministic layers had pre-filled.

## 1. Stage golden set — the Form D band scores 7/16 and is DEMOTED

The band produced an `entry_stage` for 16 of the 25 key rows:

| row | layer said | the record says | |
|---|---|---|---|
| snapchat | Series A | Series A | ok |
| twitter | Growth | Growth (Series C, Feb 2009) | ok |
| new-relic | Series A | Series A ($3.5M, 2008) | ok |
| dotcloud | Series A | Series A ($10M, 2011) | ok |
| contentful | Growth | Growth (Series B, 2016) | ok |
| zuora | Series A | Series A ($6.5M, 2008) | ok |
| airbyte | Series A | Series A ($26M, 2021) | ok |
| discord | Growth | **Series A** (2016, Greylock led) | miss |
| wework | Growth | **Series A** ($17M, 2012) | miss |
| zendesk | Series A | **Growth** (Series B, 2009) | miss |
| chainalysis | Growth | **Series A** ($16M, 2018) | miss |
| hipcamp | Series A | **Growth** (Series B, 2019) | miss |
| mercor | Growth | **Series A** ($32M, 2024) | miss |
| legora | Growth | **Seed** ($10.5M) | miss |
| timescale | Growth | **Series A** ($12.4M, 2018) | miss |
| optimizely | Growth | **Series A** ($28M, 2013) | miss |

**7/16 = 44%.** Worse than Sequoia's pre-rebuild 32/39 and on a par with the
Accel band that was demoted at 5/13. **The band may not label on this
investor.**

**What the misses have in common** — eight of the nine are the band reading a
*later* filing as the entry round. Discord's first swept filing is 2020 and the
entry is 2016; Chainalysis 2021 / 2018; Timescale 2021 / 2018; Mercor 2026 /
2024; Legora 2025 / 2024; WeWork 2015 / 2012. Optimizely is the ninth and a
different failure: a $28M Series A blows through the era ceiling ($15M for
2011-14) and the band calls it Growth. Hipcamp is the mirror image — a Series B
entry the band called Series A.

**The finding generalises past `entry_stage`, and it is the most consequential
thing this gate produced.** For a row whose only evidence is the Form D sweep,
`first_seen` is *the first filing on which a roster name appears*, not the
entry. Benchmark leads seeds and Series As that routinely never file a Form D
(4(a)(2)), and the sweep only sees a filing once a partner is already a listed
director — so `first_seen` runs **two to five years late** across the whole
2013-2026 half of the base. It is a ceiling on entry recency, not an entry
date, and it must not feed `entry_stage`, the C2A cohort or the "recent" slice
unchallenged. Cerebras is the extreme case: `first_seen` 2026, entry 2016.

**Decisions taken before the grind:**
1. The Form D band is a **ceiling only**. No band-only `entry_stage` publishes
   on any row that is $1B+, post-2013, or Form-D-only-evidenced. Every such row
   goes to the judge for a cited stage.
2. **The site listing year is promoted to a ceiling** on entry recency. Checked
   against 10 key rows with a listing: the entry year is never later than the
   first listing year and at most one year earlier (uber 2011/2012, instagram
   2011/2012, grubhub 2010/2011, zuora 2008/2009, zendesk 2009/2010; snapchat,
   twitter, new-relic, dotcloud and optimizely land on the same year). It is a
   bound, never a label.
3. `stage_uncited` is expected to be small: the visible slice is cited by hand.

## 2. Membership trap set — 30/33 blind, and the three misses were one layer defect

33 rows: 18 constructed false rows and 15 known-true members. The false rows are
unusually rich here because Benchmark hired four partners out of other firms
between 2021 and 2026 and two long-tenured partners run personal vehicles:

- **prior-firm seats** — Puttagunta's NEA book (Placester, Reltio, ScoutRFP,
  SiteTraker, Folloze, Canopy Tax, Logik), Randle's Huntress (2024q2, two years
  before he joined), Altman's Alt Capital book (Antares Nuclear, Verifiable,
  Copilot Labs);
- **founder rows** — Rachleff's Wealthfront, Altman's own Degree/Lattice;
- **personal vehicles** — Harvey's Camrose / Cardston / Fronterra Investors
  (2013q3, $500-600K, fund-shaped);
- **next-firm rows** — Beirne's Fantex (founded 2012 by a *former* Benchmark GP,
  verified), Grimshaw's Doji Labs (2025, after he left).

The blind pass, reading only the queue item, ruled 30 of 33 the way the key
does. **All three misses were the same defect**: `formd_span` is year-granular
and the boundary sits inside a year.

- `copilot-labs` — Altman 2026q1, and his first Benchmark fund filing is
  2026-06-30. At year granularity the seat reads in-tenure; at quarter
  granularity it is one quarter early.
- `degree-inc` (Lattice) — Grimshaw's 2021q2 and 2022q1 filings fall inside his
  Benchmark window, so the row reads as a Benchmark position. It is not: he
  joined that board in 2019 at Thrive and the seat travelled with him.
- `fantex-holdings` — Dunlevie's window is open, so his co-filed seat reads
  in-tenure and masks the fact that the company is Beirne's own post-Benchmark
  venture.

**Layer fix applied before the grind** (`scratch/enrich-queue.py`): every queued
row now carries one line per (partner, quarter) with that partner's roster
window and a computed `in_tenure | pre_tenure | post_tenure | boundary` flag. 60
rows enriched; 13 carry a `boundary` seat and 13 a `pre_tenure` seat — a class,
not a curiosity. With the discriminating facts on the item the three misses
resolve, and the gate passes: **zero false members at high confidence.**

**One standing rule came out of it, and it is investor-agnostic** (proposed for
the playbook write-back, §1 seat dating): *a continuing board seat first taken
at a prior firm stays the prior firm's.* COLLECTION.md dates a seat against the
person's firm **at filing time**, which is right for a seat taken at the new
firm and wrong for one carried across a move — the filing is an amendment to a
relationship that began elsewhere. The test is the seat's FIRST year, not the
filing's.

## 3. Layers not scored, and why

No site stage label exists to score: Benchmark's listings never carried a round
or a date in any of the four eras, unlike Accel's CMS (30/31, promoted) or
Thrive's job board (0/10, refused). No status or valuation set is required —
the A/B pass (§7) guarantees those columns.
