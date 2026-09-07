# Y Combinator — collection run report (PRO-74)

**Run:** 2026-09-06, one session, on the shared `main` checkout.
**Review model:** full grind (Erik, 2026-09-06).
**Grind mode:** bounded-context subagent grind — a §12 deferred item, **switched
on by Erik at kickoff** on the measured directory size. The other deferred
items (model mix, extra credits, second machine) stayed off.

**Usage line:** _to be filled at close._ Note for the record: the usage lines in
the USV, Spark and Benchmark reports were never filled in, so the deferred-item
call this issue specified — "made on the measured usage lines … never invented
by the session" — had no measured basis available. It was made on the row count
instead, and that substitution is recorded rather than hidden.

**Prompt count:** _to be finalised at the ingest decision._

---

## 1. The method delta

The question this run was set: **what does the pipeline do when the investor
publishes everything, and the volume is several times the largest prior base,
under a full-grind bar?**

The short answer is that "publishes everything" was false in three separate
ways, and finding each one was most of the work.

### 1.1 The directory is a floor, not the portfolio

YC's Startup Directory is an Inertia/React app over an Algolia index
(`YCCompany_production`). The app id and search-only key are the ones the public
page ships to every visitor; the key is a *secured* key whose payload pins
`tagFilters=["ycdc_public"]`, so this run reads exactly the rows an anonymous
visitor is served. It answers **6,203 companies**.

It is not the funded portfolio:

- **It lists *launched* companies.** YC says so in its own result count:
  filtering to a live batch renders "Showing 40 of 235 **launched** companies —
  more will be added as Summer 2026 launches!"
- **Companies are removed.** 140 slugs in the archived `/companies/` namespace
  404 on the live site today; 52 were named from Internet Archive captures
  (Convictional, Encellin, Gmelius, Wallarm, Chesscademy, Blotout and others),
  88 remain unidentified.
- **An entire class is excluded by construction** — see 1.2.

Measured undercount: **145 slugs absent from the public index**, of which three
turned out to be YC founder-community pages rather than companies.

### 1.2 `ycc_only` — the class the directory cannot show

YC's data model carries a hidden batch value, **`ycc_only`**, for Continuity
holdings that never went through a batch. Querying the public index for it
returns **zero**; the rows have live company pages that the search index does
not carry.

It contains **exactly two companies**, verified three ways (each page's own
Inertia payload, the yc-oss public mirror's `batches/ycc_only.json`, and the
index query returning zero):

| Company | id | Continuity round |
|---|---|---|
| Convoy | 11874 | Series B, $62M, 2017-07-25, YC Continuity **led** — the first time YC took a stake in a later-stage company it had not previously funded |
| Monzo Bank | 4787 | Series F, £113M, 2019-06-24 at a £2B post, YC Continuity **led** |

This is decisions.md D2's predicted consequence, confirmed mechanically rather
than inferred — and it bounds the class. The issue anticipated an open-ended
Continuity tail; it is two rows.

A trap inside it: the directory's **own** "Convoy" is `convoy-2` (Winter 2022,
London/Nigeria), a different company. The two were never merged.

### 1.3 A company name is not an identity here

The directory carries **89 names borne by two different companies** in different
batches, each with its own YC id — Parse S11 (the Facebook-acquired backend) vs
Parse F25; Struct W23 vs Struct F24; Alex F24 ("The Cursor for Xcode", team 3)
vs Alex W24 ("Your AI recruiter", team 30).

This broke three things, each fixed as a pipeline change rather than a local
patch (§5, *invention may change the pipeline*):

1. The site merge keyed on the normalized name and **collapsed 100 real
   companies into 89 rows**.
2. The base build did the same, and then published a **duplicate slug** for the
   survivors — worse, because every overlay joins on slug, so one row's answers
   land silently on both and `verify`'s drift check cannot see it: all the keys
   are present, they just describe the wrong company.
3. The judge fell for it too. One judging pass reported the two Alex rows as
   "the same company duplicated"; three others independently flagged duplicate
   slugs in their inputs. Slug uniqueness is now enforced as a build invariant
   (94 collisions resolved on this base).

---

## 2. Evidence layers

| Layer | Result |
|---|---|
| Site (Algolia directory) | 6,203 rows with batch, status, stage, industries, subindustry, regions, all_locations, team_size, top_company, nonprofit, launched_at, **former_names** (3,031 rows) |
| Site (unindexed) | 129 rows: live company pages absent from the search index, plus archived pages that 404 today |
| Wayback `/companies/` | 8,202 distinct slugs after CDX paging was added; **2018–2019 UNRESOLVED** (see 6) |
| Common Crawl | 6,708 company slugs, 17 people — an independent capture set |
| EDGAR entity registry | 60 entities, **20 address-verified to 335 Pioneer Way** |
| EDGAR issuer ownership | **structurally empty** — 0 filings |
| Form D roster sweep | 109 accessions over 23 roster names; 16 rows reached membership judgment |
| Form ADV / IAPD | 19 private funds, **$21.96B gross** (see 4) |

**EDGAR's ownership layer being empty is the shape, not a failure.** An
accelerator never crosses 5% and never takes the board seats that trigger
Section 16, exactly as the issue predicted.

---

## 3. The calibration gate

Both sets pre-registered in `golden.json` before any verdict wrote. §4 requires
scoring every candidate *layer*, not only the judge:

| Layer | Score | Ruling |
|---|---|---|
| Directory `stage` field | **4/29** | **Refused** as an entry_stage label |
| Batch record → Seed / `ycc_only` → Growth | **31/31** | **Promoted to class 1** |
| Directory `status` field | 67.5% (518/767) | Corroboration only, never a label |
| `all_locations` → hq_country | 84.4% | Class 2 |
| `all_locations` → hq_city | 50.2% | Normalize to the §6 shape first |

The `stage` field fails precisely as the set was built to catch: it reads
`Growth` for Checkr, DoorDash, Ginkgo, Podium, Whatnot, Webflow, Airbnb,
Dropbox and Stripe — every one a batch entry described by the company's *later*
rounds. Worse in kind than Thrive's job-board field (0/10). The directory looked
clean, which is exactly why §4 makes it be scored.

`status` fails where it matters most: **"Inactive" is not `defunct`** — it lands
as `private` 41 times and `unknown` 28 against only 27 `defunct`. Phase 0 ruling
5 is now measured rather than assumed, and it became the single most important
line in the judging contract.

**A YC batch entry is `Seed`, never `Pre-Seed`**, on YC's own sustained language
("Y Combinator provides seed funding for startups", about page 2009–2020).
`Pre-Seed` and `Series A` are **structurally empty** for this investor:
Continuity's mandate was pro rata and later-stage growth, so it never led a
Series A.

**The gate caught a live trap in its own scoring.** The batch rule first scored
30/31, the miss being Convoy — because the lookup resolved the *name* to
`convoy-2`. Re-scored on site id: 31/31. The name-collision problem bites the
judge, not only the base build, so every grind lookup keys on YC's id.

**Scoring note.** Raw accuracy on the stage set is near meaningless: 29 of 31
rows are `Seed`, so answering "Seed" unconditionally scores 94%. It is scored by
class instead, with the discriminating power in the 2 class-A rows and the 11
class-B rows that dangle a large publicised Continuity round.

---

## 4. The C2A cohort — the column this investor was supposed to answer

This is the most important negative result of the run.

`seed_to_a_graduation` exists because thousands of seed entries should make the
seed→A graduation rate the single most informative number the dataset can
produce, and **YC is the firm the column was designed for**. It is also the
firm where the column cannot be computed from the evidence the pipeline has.

| | |
|---|---|
| Seed entries | 6,391 |
| C2A cohort (entry ≥24 months ago) | **5,041** |
| Censored (entered within 24 months, null by rule) | 1,290 |
| Deterministically verified on both legs | **0 (0.00%)** |

**Why, structurally.** The deterministic graduation path is the Form D issuer
round history: entry round, then a later round ≥2× and ≥$5M. That works for a
venture firm's book because priced rounds file Form D. It does not work here.
YC companies raise on SAFEs under Section 4(a)(2) and overwhelmingly file no
Form D at all, so **there is no filing record of the seed→A transition** for
essentially the entire cohort. The layer that carries C2A for every other
investor resolves 34 companies on this base — and those 34 are drawn from the
Form D partner-name-match rows, which are themselves being ruled `not_member`.

**What is published:** nothing. All 5,041 cohort rows carry `cohort_unverified`
and a null graduation. Publishing a rate off a 0% verified share would be
inventing the dataset's headline number, and §6's own instruction is that the
published rate carries its verified share — here that share is zero.

**What would be needed.** Not a Form D fix. Either a per-company round history
from a source that records unpriced and SAFE rounds, or ~5,000 web checks — a
different order of cost from anything the playbook currently budgets. One
cheaper candidate exists and is deliberately **not** used here: YC's own
`stage` field ({Early, Growth}) marks companies that have raised beyond seed,
which is close to what graduation asks. It was refused as an `entry_stage`
label at 4/29 on the gate, and using it for graduation is a different question
that a future run should **score against a purpose-built graduation golden set
before trusting** — §4's rule is that an unscored layer may corroborate but may
never label, and that rule does not bend because the answer would be
convenient.

---

## 9. Playbook write-back proposed

_(Numbering follows the standing report shape; sections 4–8 and 10 are completed
at close.)_

Candidates for COLLECTION.md, all investor-agnostic:

1. **A failed fetch is never an empty year.** Absence of a capture and absence
   of a response are different claims. Landed in `wayback-pull.py` (12402a7)
   after the Redpoint run lost 10 of 14 era-years to it. A third failure mode
   found here: a **truncated body** that parses as invalid JSON.
2. **A zero-row year on a page that returned bytes is a failed parser
   hypothesis, not an absence** (Menlo's rule, credited to PRO-91) — check the
   raw file exists and has content before believing an empty year, and give each
   distinct page shape in an era its own pattern.
3. **The scheme was never the variable.** The claim that web.archive.org refuses
   plain HTTP is **retracted**; measured http 7/9 vs https 6/9, all failures
   rc=28, and rc=7 subsequently observed on HTTPS by two runs independently.
4. **A name is not an identity at scale.** Where a source publishes its own id,
   key on it — and make slug uniqueness a build invariant, because a duplicate
   slug is invisible to the drift check.
5. **A search index needs its own strategy.** Every hosted index caps deep
   pagination, so a book larger than the cap cannot be read by paging the
   unfiltered query at all; slice on a facet whose buckets sit under the cap.
6. **Two vocabularies answer different questions.** YC's industry vocabulary has
   no AI value at all; its tag vocabulary does. An industry-only focus crosswalk
   would have published an empty AI bucket on the investor with the most AI
   companies.
7. **Don't repartition a work queue while workers hold pieces of it** — and have
   research subagents write to files, not only report, so an interrupted run
   loses nothing.
