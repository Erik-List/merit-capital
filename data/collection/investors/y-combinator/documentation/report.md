# Y Combinator — collection run report (PRO-74)

**Run:** 2026-09-06, one session, on the shared `main` checkout.
**Review model:** full grind (Erik, 2026-09-06).
**Grind mode:** bounded-context subagent grind — a §12 deferred item, **switched
on by Erik at kickoff** on the measured directory size. The other deferred
items (model mix, extra credits, second machine) stayed off.

**Ingested 2026-09-24 with Erik's approval** ("when done correctly, ingest yc"):
icon published, investor row (hq San Francisco, CA; stage Pre-Seed), then 6,426
companies (6,426 new, 0 removed on the dry-run plan). Readback: 6,426 rows, every
status, band, stage and location matches `base.csv`; the derived stage
distribution is Pre-Seed 6,404 and Growth 2, and the graduation rate is empty, as
the pre-seed ruling requires. Before the ingest: the profile's stage moved from
Seed to Pre-Seed, Monzo's stage citation was corrected, the HQ follows the new
rule (the newest Form ADV principal office, unless the firm's own site
disagrees), 87 shared names publish with their domain in brackets (Erik's choice;
the table is unique on investor and name), Gmelius's numeric-id row was merged,
and the `pickle` row was re-identified as Pickle W21 (pickleai.com). A rebuild
under today's shared scripts drifts (ten slug-named archive rows, two worse
names), so the committed base stands and that rebuild is its own task.

**Usage line:** measured at the ingest from the app's usage card, account-wide:
5-hour window 9%, weekly all models 13%, weekly Fable 3%, extra usage EUR 9.29 of
EUR 50; this session's context 43% of 1M. These are window readings, not this
run's total: the run spanned sessions from 2026-09-06 and no per-run total
exists. The earlier note stands: the USV, Spark and Benchmark usage lines were
never filled in, so the deferred-item call was made on the row count instead.

**Prompt count:** 11. Five before the ingest decision (kickoff; the grind-mode
answer; "keep going"; two "continue" resumes), then the OpenAI ruling, the slug
rename and its three approvals, the stage and HQ question, the HQ rule, and the
ingest approval; the shared-name question was answered in the ingest turn.
Target was 2.

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
| Wayback `/companies/` | 8,202 distinct slugs after CDX paging was added; 2018–19 established as a **genuine absence** (see 2.1) |
| Common Crawl | 6,708 company slugs, 17 people — an independent capture set |
| EDGAR entity registry | 60 entities, **20 address-verified to 335 Pioneer Way** |
| EDGAR issuer ownership | **structurally empty** — 0 filings |
| Form D roster sweep | 109 accessions over 23 roster names; 16 rows reached membership judgment |
| Form ADV / IAPD | 19 private funds, **$21.96B gross** (see 4) |

**EDGAR's ownership layer being empty is the shape, not a failure.** An
accelerator never crosses 5% and never takes the board seats that trigger
Section 16, exactly as the issue predicted.

### 2.1 An empty year, established rather than assumed

The era's 2018 and 2019 years came back with nothing, and a direct probe
showed 2018 *does* have `/companies/*` captures — which under the
zero-rows-is-not-an-absence rule (Menlo, PRO-91) made the years UNKNOWN, not
empty. Resolving it took three attempts across an archive outage that returned
`rc=7` on HTTPS and, once, a **truncated body that parsed as invalid JSON** —
a third transport failure mode neither this run nor the sibling runs had
catalogued.

The answer is that the absence is real. All 150 captures in those two years are
of `/companies/` **itself**, none carries a per-company slug segment, and the
index page is a 3.7 KB JavaScript shell with no server-rendered company list.
YC's per-company URLs begin in 2020. The era now starts there.

Worth recording because the cheap conclusion — "the archive was flaky, so the
years are unknown" — and the expensive one — "the years are genuinely empty" —
look identical from the pull log, and only the second one is true here.

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

---

## 5. Results

| | |
|---|---|
| Published base | **6,427 rows** |
| Excluded | 84 (build_filter 5, not_member 78) |
| Membership | 6,521 member verdicts, 78 not_member, 0 uncertain |
| Evidence class | site_listing on every published row: the directory, the unindexed live pages, or an archived company page |

**Status:** private 4,239 · unknown 1,092 · acquired 889 · defunct 187 · public 20

**Valuation band:** below_1b 6,316 · 1b_plus 94 · 10b_plus 15 · 100b_plus 2 — a $1B+ share of **1.7%**, against a `one_b_share_max` of 6% set for a seed book. Sources on the $1B+ slice: web_verified 112.

**Entry stage:** Seed 6,426 · Growth 2 (Convoy and Monzo, the two `ycc_only` rows). Pre-Seed and Series A are structurally empty, as the gate established.

**Country:** US 4,965, GB 228, IN 216, CA 162, MX 84, FR 77. US is 77.2%; 79 US values are flagged `country_prior` at low confidence and carry no weight beyond the ordering.

**Focus (judged column):** AI & Applied AI 1,386, SaaS 1,202, Fintech & Payments 766, Consumer & Marketplaces 758, DevTools & APIs 564, Healthcare & Bio 498, Industrial & Robotics 412. AI & Applied AI is the largest bucket — the two-layer crosswalk is why; YC's industry vocabulary alone would have published it as zero.

**The $10B+ slice**

| Company | Status | Band | $B | As of |
|---|---|---|---|---|
| Stripe | private | 100b_plus | 159.0 | 2026-02-24 |
| Airbnb | public | 100b_plus | 100.5 | 2026-08-07 |
| DoorDash | public | 10b_plus | 96.3 | 2026-09-03 |
| Coinbase | public | 10b_plus | 48.7 | 2026-09-04 |
| Reddit | public | 10b_plus | 30.0 | 2026-09-03 |
| Scale AI | private | 10b_plus | 29.0 | 2025-06 |
| Kalshi | private | 10b_plus | 22.0 | 2026-05 |
| Whatnot | private | 10b_plus | 20.0 | 2026-08-07 |
| Deel | private | 10b_plus | 17.3 | 2025-10 |
| Rippling | private | 10b_plus | 16.8 | 2025-05-09 |
| Helion Energy | private | 10b_plus | 15.5 | 2026-06-05 |
| Groww | public | 10b_plus | 13.7 | 2026-09-04 |
| Oklo | public | 10b_plus | 13.5 | 2026-09-07 |
| OpenSea | private | 10b_plus | 13.3 | 2022-01-04 |
| Instacart | public | 10b_plus | 11.9 | 2026-09-02 |
| Supabase | private | 10b_plus | 10.5 | 2026-06 |
| Alchemy | private | 10b_plus | 10.2 | 2022-02 |

**Directory status against the judged column** (the measured stale-ness of YC's own field, now over the whole base):

| Directory | Published | n |
|---|---|---|
| Active | private | 3,938 |
| Inactive | unknown | 868 |
| Acquired | acquired | 737 |
| Inactive | defunct | 89 |
| Active | acquired | 75 |
| Active | defunct | 58 |
| Active | unknown | 58 |
| Inactive | private | 51 |
| Inactive | acquired | 48 |
| Acquired | private | 32 |

`Active → private` holds for 3,938 rows; the tail is where the field is stale: 75 Active rows are acquired, 58 are defunct, and `Inactive` split 868 unknown / 89 defunct / 51 still private / 48 acquired. **"Inactive" is not defunct**, and the judges were held to that.

**The bar, per row class.** Every published row carries a judged membership verdict and every classification column authored or pre-filled from a gate-scored layer. `entry_stage` and `focus` come from class-1/class-2 layers the gate promoted; `status` and `valuation_range` were judged per row across 30-odd subagent batches; `hq_country` comes from the directory at class 2 with flagged priors where the row is dark. The unidentified archive rows (10 flagged `identity_uncertain`) meet the bar with flagged priors, which is what §3 prescribes for a row nothing can identify; none of their values is a finding.

**Blind sampling over the un-signalled `below_1b` remainder** was not run as a separate step: the priority slice (top_company, recent hot-sector, team ≥150 — the momentum slice of §6) was judged with web checks, and the tail was judged with recognition-first rule-outs. Reported as such rather than as a sample that did not happen.

---

## 6. Corrections taken during the run

The run corrected itself far more than it corrected the directory. In rough order of consequence:

1. **The prefill imported other companies' valuations** (22 rows: Flow/Neumann, Runway/RunwayML, Avalanche/AVAX, Maven Clinic, cedar.com, clay.com). Cleared and re-judged.
2. **Five more imports failed a date check** (Guild Education's $4.4B on a Summer 2026 row). Cleared.
3. **84 weak-CIK-join public floats quarantined** (Dover Corp, Parametric, Iliad SA, Lucid, Plexus, Mosaic Co); every one was already flagged `cik_weak`.
4. **Nine visible-slice bands rested on another company's citation** (Paribus carrying Ramp's $44B; Quill carrying Circle's cap; LemFi carrying Lemonade's). The check was whether the citation URL contained the company's name.
5. **Identity merges pointed at the wrong company** (`apriora → alex-com` written as canonical `alex`). Regenerated against the published slug.
6. **Duplicate slugs** were reaching the judges (94 collisions). Slug uniqueness is now a build invariant.
7. **74 rename pairs sat in the base twice** (Asayer/OpenReplay, Jumpstart/Novel). Merged on a shared site id; the surviving row adopts YC's current name.
8. **The Continuity Convoy and the webhooks Convoy had swapped evidence** through a slug/site-id collision; both re-judged explicitly.
9. **My grind contract contradicted §6** on acquired-then-shut-down; the two rows judged under it were flipped, and 20 invariant-10-bound rows were deliberately left alone.
10. **My golden trap set was wrong on OpenAI** (see §7).
11. **Y Combinator itself and four founder-community pages** were in the base as companies. Rejected with a T5 reason.
12. **The 42 nonprofits** (plus three archive-slug siblings) were excluded under D6 only at close — the derivation had been written at kickoff and not applied.
13. **PRO-109 renamed the ledger mid-run** and one rebuild ran against a fresh, near-empty file. Merged back from the orphaned original (§R12).

Corrections to the **directory** by the judges, by class: Active rows found acquired (75) or defunct (58); Inactive rows found still trading (51) or acquired (48); Acquired rows found later wound up are left `acquired` by rule.

---

## 7. Flags, debt and open rulings

**Flag counts on published rows:** `site_field_prefill` 6,293, `cohort_unverified` 4,971, `cross_investor_bound` 737, `country_prior` 437, `duplicate` 161, `model_disputes_source` 93, `cik_weak` 90, `stale` 86, `needs_web_value` 68, `identity_uncertain` 56, `unicorn_name_match` 46, `stage_prior` 35, `prefill_identity_error` 27, `band_downgraded_no_figure` 12.

**Debt:** `cohort_unverified` 4,971 (every C2A cohort row, by decision, §4); `needs_web_value` 68 rows for the web pass to pin or kill; `stale` 86 $1B+ marks older than 24 months; `cite_pending` 10; `country_prior` 437; `identity_uncertain` 56; `model_disputes_source` 93.

**Open rulings for Erik**, raised once here under §9:

1. **OpenAI: RESOLVED by Erik, 2026-09-16, OUT.** "If OpenAI did not receive investment from a YC entity, keep out." Verified that it did not: the 2015 funders were individuals, AWS, Infosys and YC Research, a non-profit lab Altman funded personally that is not a YC fund, and no YC vehicle appears in any later round. Recorded `who: erik`; the $852B row left the base. The delta it establishes (an affiliation listing does not carry membership) is ratchet item 13 in §9.
2. **Coin and Cymmetria** versus **Airware**: the asset-sale-versus-wind-down line, resolved `acquired` where a buyer took platform and team and `defunct` where none did. Consistent with the Cherry ruling, but Erik should see the line drawn.
3. **The C2A column** is empty for the investor it was designed for (§4). A decision on whether to build a non-Form-D graduation layer, and whether YC's own `stage` field may be scored for it.
4. **`investor_type`** ships `Institutional`; the enum has no accelerator value (trigger 3 as anticipated by the issue). The accelerator nature is carried in `investment_concept` and `history`.
5. **D6 (nonprofits out)** is a derivation applied without confirmation, per the protocol; it moved 45 rows and is listed for veto.
6. **140 cross-investor pairs pending alignment** in `cross-rulings.json`, each naming the stale side and the action. Two of the adjudications close open questions in other bases: Kinter is a16z's unidentifiable entry (Alloy Automation, rebranded), and Clay settles Thrive's open `Clay, Inc.` identity.
7. **PRO-109's ledger rename** left this in-flight run with an orphaned ledger; worth a rule that a path migration touches in-flight investors explicitly or not at all.

---

## 8. Usage line

_Erik records the account's weekly and Fable percentages here at ingest._ Base rows: 6,428. This run used 10+ subagent judging batches under the §12 bounded-context mode Erik switched on at kickoff; the honest cost-per-company figure this issue asked for needs the account numbers, which no earlier report filled in either.

---

## 10. Close

`verify: clean` (plain mode). `review.html` rendered and checked usable at 6,428 rows (search filters to a single row in under a second). `run.py close` removes the in-flight marker as the last act before the closing commit. Ingest (icon upload, `ingest-investor.ts`, then `ingest-companies.ts`) runs **only after Erik's explicit approval**.

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
7. **Don't repartition a work queue while workers hold pieces of it**, and have
   research subagents write to files, not only report, so an interrupted run
   loses nothing.
8. **Check an imported value against a date the row already knows.** An event
   dated before the company's own entry cannot be the company's; it catches
   collisions no disagreement would surface.
9. **A weak CIK join whose row is not Public in the firm's own source is a
   collision.** Quarantine it; the pipeline already flags `cik_weak`.
10. **Rule A and the C2A rate need switches, not editing of derived files.**
    `verify.unicorn_bands` and `verify.c2a_deterministic` landed as opt-outs;
    promote to defaults once the wave agrees.
11. **The judge sees the evidence you attach.** Two rows sharing a name with
    swapped slug/site-id will be fed each other's batch and one-liner, and a
    name check cannot catch it. Key evidence on the source's own id.
12. **A path migration must touch in-flight investors explicitly** or leave
    them alone; the ledger rename orphaned this run's ledger for one rebuild.
13. **An affiliation listing does not carry membership** (Erik, 2026-09-16,
    OpenAI). The site-listing sufficiency rule assumes the listing records an
    investment; where the firm lists a company it is tied to through a person
    or a related non-profit, T2 governs and the row needs fund money. Ratchet
    into COLLECTION.md 1 as a T2 precedent.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Fifty-six published rows carried `identity_uncertain`. YC's set is unlike any
other book's, because the flag was applied before the directory pull that
recovered most of these companies — twenty-seven of the notes still read
"Unidentified archive row" about rows the directory now carries with a name, a
website and a batch.

**Twenty-seven rows lose the flag.** Eighteen are directory records that
resolve outright (`gmelius`, `candor-security`, `freestyle-ai`, `gpt` → Nexus,
`haystackeditor`, `laminar-com`, `miru-ml`, `orchid-ai`, `rivet-design`,
`struct-ai`, `aalo`, `assembled`, `blotout`, `convictional`, `convoy`,
`hyperbrowser`, `parker`, `sync`). Nine are the Imagine K12 cohort the S2A
pass had already identified from knowledge and description — `remind`,
`schoolmint`, `socrative`, `sown-to-grow`, `stablegains`, `swing-education`,
`teachboost`, `tioki`, `trinket`.

**Five rows are identified with a namesake.** `almond-2` (Spring 2025 robotics
at almond.bot) against the base's own `almond` (Summer 2022 ObGyn telehealth),
`hyper-4` (Spring 2026) against `hyper` (Summer 2021 Discord memberships) and
`hyper-online`, plus `snipd` (the 2008 media row, not the 2021 podcast app),
`benchify` and `bobidi`, whose YC one-liners do not match the companies those
names are known for.

**Twenty rows read `undetermined`**, among them the seven bare numeric ids
(`11963`, `13067`, `1924`, `1991`, `21848`, `22278`, `23631`) whose pages are
gone. Their Seed came from the batch-deal record — which describes what YC
offers EVERY company rather than a round this one took — so on a row that
names no company it is exactly the inferred fill the new rule abolishes. This
is the population PRO-133 counted when it found 33 YC rows citing
`ycombinator.com/deal` as stage evidence.

### Two findings that are not identity, and one that did not work

**The suffixed twins cannot be merged by the current builder.** `cleartax-2`,
`sieveai-2` and `usenarrative-2` are archive renderings of `cleartax` (Clear),
`sieveai` (sieve) and `usenarrative` (Narrative), and `12869`/`12869-2` are
YC's numeric id for Gmelius. A merge entry naming those published slugs does
nothing: the builder mints the `-2` suffix AFTER the identity overlay runs, so
at overlay time both rows carry the same base slug and the duplicate lookup
misses. The rows are flagged `identity_conflated` with the pairing recorded,
and the builder's ordering is raised for Erik rather than worked around.

**`never_merge` made it worse here, which is worth knowing.** Adding pairs for
`almond`/`almond-2` and `hyper`/`hyper-4` did not protect two real companies —
it resurrected archive rows literally named "Almond 2" and "Hyper 4" that the
name-prefix rule had been absorbing, adding junk rows to the base. The pairs
were reverted and the base is byte-identical to before; the namesakes are
recorded on the rows instead.

`verify --skip-cross` still fails on this book for a reason that predates the
pass: 4,971 rows carry `cohort_unverified`, a flag retired on 2026-09-16 and
never swept here. That is PRO-120's work. The twenty new `undetermined` rows
verify cleanly and leave every metric; the seed cohort reads 6,405 rather than
6,425.
