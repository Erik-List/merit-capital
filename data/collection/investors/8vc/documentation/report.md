# 8VC — collection run report

Run: **PRO-96** (Archetype A, sub-issue of PRO-87). One session, 2026-09-06/07.
Slug `8vc`. `verify` clean in **plain mode**. Ingest **not run** — gated on Erik's
explicit approval (§9).

---

## 1. Results

| | |
|---|---|
| **Published base** | **254 companies** — Tier A 177, B 59, C 18 |
| Membership verdicts | 330 (269 member, 61 `not_member`, 0 uncertain) |
| Evidence classes | site_listing 254 · formd_adjudicated 70 · fund_filing 5 · web 1 |
| Classification | 254/254 rows on `status`, `entry_stage`, `hq_country`, `valuation_range` |
| `entry_stage` | Seed 140 · Growth 81 · Series A 31 · Pre-Seed 2 |
| `valuation_range` | below_1b 233 · 1b_plus 18 · 10b_plus 3 · 100b_plus 0 |
| `focus` | Healthcare & Bio 78 · SaaS 38 · Fintech 28 · AI 26 · Consumer 24 · Industrial 19 · Data Infra 11 · Security 10 · Media 6 · DevTools 5 · Climate 3 · outside taxonomy 6 |
| `hq_country` | US 242 · Israel 3 · UK 2 · Canada 2 · India 2 · Brazil, Colombia, Australia 1 each |
| `hq_city` | 174/254 filled, 51 distinct (San Francisco 56, New York 19) |
| C2A | cohort 10, graduated 2, **20.0%** |
| Cross-investor | 84 shared rows, **76 agree, 8 accepted, 0 disagree** |
| Firm profile | every field populated or explicitly null, each with a source and basis |

**Shape.** A 2015-vintage firm with a curated 176-row live list and 81
survivorship-only rows from the archive. The $1B+ share is **8.3%** (21 of 254),
well under the 20% default guard — the opposite of the pre-run expectation, and
entirely an artefact of Rule A: thirteen rows that vendors and unicorn lists call
unicorns publish `below_1b` because no priced round with a citable figure exists
(§4 below). The C2A rate of 20% on a cohort of ten is not a statistic; the report
says so rather than dressing it up.

---

## 2. The delta — Erik's ruling still open

**Delta A: the Formation 8 legacy book.** Argued in full in `decisions.md` Part 2.
The run proceeded on the recommended reading and flagged every affected row, so a
reversal re-judges one ledger class rather than re-collecting.

*What was decided.* Eleven rows with **positive predecessor evidence** are
`not_member`: **Palantir** (Lonsdale co-founded it in 2003; no 8VC vehicle has ever
held it — 8VC GP I's 13F-HRs report one holding, Joby), **RelateIQ** and
**SalesforceIQ** (Salesforce bought it in July 2014, a year before 8VC existed),
**Oculus** (Facebook, March 2014), **Wish** (8VC's own post: "we co-led the angel
round in 2010"), **Oscar** and its legal entity **Mulberry Health** (2015q2 Form D,
Lonsdale, outside tenure), **Guardant Health** (press puts Formation 8 at the
Feb-2015 Series C), **Illumio**, **OpenGov**, **Color** and **Color Genomics**.
Plus **Hyperloop Technologies** and **Revinate**, ruled the same way on the same
evidence in the grind.

*What was NOT decided that way.* A legacy row where an 8VC vehicle demonstrably
took a position stays a member: **Addepar** (8VC ADSF SPV filed 2021-05-06 and ADSG
SPV 2024-12-31), **Zenreach/Adentro** (Lonsdale on the 2017 and 2018 filings),
**Joby** (the 13F holding), **Blend**, and every 2016-era row with no positive
Formation 8 evidence (Affinity, Qualia, BuildZoom, Blink Health, Nyansa, Kiwi,
Progressly, Radius, Castle Global). The test applied is **fund money, not era**.

*The fact that decides it, found mid-run.* 8VC's own 2016 team page calls Formation
8 "**the precursor fund to 8VC**" and lists Addepar, OpenGov, Oscar, Illumio,
Radius, Hyperloop-One and Wish as **Joe Lonsdale's** board seats — T4's question
answered by the firm itself. That is the Redpoint D5 shape after all, reached
through a different page than the one listing the rows.

**If Erik reverses it**, the class goes back in together and their entry rounds
become the predecessor's; the stages are already recorded on the rows for that case.

---

## 3. Method deltas — what this run invented or found

### 3.1 The SPV name decode (new evidence layer, proposed for write-back)

8VC runs ~30 single-deal SPVs whose Form Ds name **no portfolio company**: every one
files "Indefinite / $0 sold", fund type "Venture Capital Fund", with 8VC SPV GP I,
LLC and Joe Lonsdale as executive officers. What they *do* carry is a name and a
date, and the names are codes: `<company initials> + S + <round letter>`.

**Scored before use** (§5 rule 1), against announced round dates: ADSF → Addepar
Series F (−6 weeks), ANSD → Anduril Series D (−5 wks), PAIC → PathAI Series C
(−4 wks), ANSF → Anduril Series F (−2 wks), EPSD → Epirus Series D (−3 wks);
one outlier, ANSE, formed six months before Anduril's Series E closed. A **sixth**
confirmation landed later in the run when the cross-investor pass dated Saronic's
Series D to March 2026 and `8VC STSD, LLC` turned out to have filed 2026-03-17.

The layer is **corroboration, not a label** — two letters are ambiguous — but a code
whose prefix, round letter and date all line up with a documented round is
affirmative `fund_filing` evidence. It is what puts Addepar, Anduril, PathAI, Epirus
and Saronic in the base on fund money rather than on a site listing, which is
exactly what Delta A turns on. 24 codes are recorded **unresolved** rather than
guessed (`sources/edgar/spv-decode.json`).

### 3.2 The advisor trap, in a new form

8vc.com has **three** people namespaces and the WordPress era put **advisor profiles
under `/team/<slug>`** alongside the partners. First Round's case was separated by a
case rule in the slug; here both sets are lowercase-dash, so the discriminator had to
be the firm's own **card class on its index pages** (`square--team` vs
`square--advisor`), pulled per archived year by `scratch/wp-people-pull.py` (65 team,
76 advisors, 2016–2022).

Left alone it was live: the sweep was seeding on **Scott Cook, Jerry Yang, John Mack,
Ashton Kutcher, Ronnie Lott, Stephen Harper, Arie Belldegrun and Zachary Bookman**.
Excluding 11 advisor-only names dropped the Form D sweep from **548 accessions to
420** — 128 accessions of pure false-lead noise.

And people move **between** the two sets in different years, which the tenure filter
must respect: **Bhaskar Ghosh** was an advisor 2016–2018 (VP Eng, NerdWallet) and a
partner from 2019; **John Tenet** a partner 2019–2020 then an advisor; Zach Rivkin,
Blake Brickman and Brett Cummings likewise. Rule applied: **team wins**, and
advisor-only years are removed from tenure (`scratch/fix-tenure.py`).

### 3.3 A live defect: the round history does not apply the tenure window

The Form D sweep and the issuer round histories attribute a filing to a roster name
**without checking the filing year falls inside that person's tenure**, so the
entry-stage band picks an out-of-tenure filing as the entry — §1 T4 exactly.
**31 of the 106 rows with Form D history** have an out-of-tenure earliest filing.

The clean case is **Ushur**: the band read the 2018q3 $11.8M filing as 8VC's entry
because Bhaskar Ghosh is on it — three years before he joined. The firm's own post
puts its entry at the 2020 Series B. Worked around by `scratch/enrich-queue.py`,
which puts `{person, quarter, tenure, in_tenure}` on every queue item so the grind
can date each seat; **script fix proposed below**.

### 3.4 Recall: five members no list surface carries

The exit-side EDGAR full-text sweep found four companies with **filing-grade fund
evidence** that appear on **no 8VC surface in any archived year** — the structural
blind spot §3 says the probe exists to find:

- **Oklo** (NYSE: OKLO) — 8VC Fund II and Entrepreneurs Fund II on the Investors'
  Rights Agreement filed with AltC's 2023 S-4. The run's largest recall addition.
- **Acutus Medical** — both funds signed the A&R IRA filed with its 2020 DRS.
- **Deep Fission** (NASDAQ: FISN) — SAFE notes of $493K + $7K (Jan 2024) and
  $986K + $14K (May 2024), converting at the merger.
- **Aura Consolidated Group** — 2,003,767 CDIs (1%) in the 2026 S-1 holder table.

Plus **Erebor**, recovered from the build's own dropped-row log: its Form D was
dropped as a "non-portfolio industry" (Other Banking and Financial Services) — a
chartered bank IS an operating company — and the ERSA/ERSB SPVs bracket its rounds.
And **SOFR Academy** from the Wikipedia insource sweep (web-class, medium).

**Recorded negative results:** Common Crawl was unreachable for the whole run
(`index.commoncrawl.org` refused every connection); the Wayback layer covered its
two jobs in full, so the gap cost nothing here. Lineage, Immersed, StepStone and the
CCP feeders were examined and rejected with reasons.

---

## 4. The calibration gate

**Membership trap set (22 rows) — CLEARED, zero false members at high confidence.**
Fifteen never reached the base: the build's pooled-fund filter dropped 108 fund
issuers, taking out the whole *Advanced Technology Select Fund IX–XX* factory (the
KEVIN CHEN homonym, 34 issuers), Bain Capital Partnership Strategies (COLIN
CAMPBELL), the Indus funds (BRIAN GUZMAN) and the TCA/Trinity real-estate LLCs
(PETER CONWAY). The set surfaced a class it had not named: **`smith-raymond`, a
natural person carried as a base row**.

**Three layers scored, two demoted.**

- **Wikidata `hq_country` — DEMOTED, all 44 values stripped and re-judged.** The
  First Round one-word-name trap, worse here: **Color→CZ, Oscar→BE, Esper→DE,
  Honor→CN, Oculus→LV, Baton→RU, Alloy→AU, Luna→RS, Orchestra→FR, Rainbow→PL,
  Create→JP, Flux/Premise→CZ, Pango/Radius→SE** — every one a US company. At least
  15 of 61 single-token rows wrong. `prepare` asks only about empty fields, so none
  would have reached the judge.
- **`formd_band` `entry_stage` — DEMOTED to a ceiling, 2 of 6 scorable rows**
  (Accel's 5/13 in a new place). Misses: Mantra Bio (band *Growth* off one $30.1M
  filing against the firm's own **pre-seed**), Ushur (§3.3), Bobyard (band *Growth*
  against "lead investors in their $35mm **Series A**"), Palantir (a stage for a
  non-member). 61 band rows were re-queued.
- **The site's own Stage field — not a layer.** Populated on **5 of 175** rows.

**Stage golden set: 24 rows**, under §4's 30–40 guidance and deliberately so — every
answer carries a citable document rather than a model opinion. Nine press-anchored
(the subset the announcement archive is scored against, so the score is not
self-referential), fourteen from 8VC's own dated posts where press is silent, one
Form-D-only control. Three are Menlo-inversion traps (Saronic, Subskribe, Twingate)
and four are the Delta A class. Two key rows were **corrected by the evidence**
(§4 scores both directions): Ushur's basis was rewritten around seat dating, and
Epirus was dropped from scoring as genuinely unresolved.

**Self-consistency (duty 7):** 13 rows × 4 fields re-judged blind, **0
disagreements** — with the standing caveat that the blind pass is the same model on
the same evidence pack.

---

## 5. Corrections this run made to itself

1. **D7's facts were wrong.** The first version said 8vc.com carries no Palantir
   page. It does, with 13 archived captures. Re-derived under the same tests (§1: a
   wrong fact re-derives, it does not escalate) to the same verdict on a stronger
   basis — no 8VC vehicle has ever held it.
2. **Blend's 13G is not membership evidence.** An earlier note called the 8VC
   Co-Invest Fund I SC 13G "8VC fund evidence"; it was filed seven months *after*
   Blend's IPO, and T3 puts a post-IPO 13G out as crossover treasury. Blend stays a
   member on its 2016 site listing; the 13G is corroboration only.
3. **Honor was recorded acquired; it is private.** Honor Technology was the
   *acquirer* of Home Instead in 2021. Caught by invariant 10 against a16z and
   Thrive, and aligned to their cited $1.25B.
4. **Wispr Flow was ruled out by the momentum slice and should not have been.**
   Menlo publishes $2B on a TechCrunch citation of 2026-08-17. The rule-out had been
   *recorded on the row*, so the correction was one row — which is the whole point
   of recording rule-outs (the Augustus case on Creandum).
5. **Addepar's entry stage was the founder's round.** The band read Lonsdale's 2011
   filing; the round an 8VC *fund* entered is the 2021 Series F.
6. **`verify.known_positions` was model priors.** Eight names in the kickoff list
   are not in the base (radiology partners, base power, element biosciences, oura,
   chef robotics, vast, atlan, plus a naming slip on oscar). `verify` was right to
   flag them; the list is now verified against the landed base.

---

## 6. Debt behind `verify: clean`

| flag | rows | what it means |
|---|---|---|
| `stage_uncited` | 201 | citation attempted and not found. 8VC publishes an entry round for almost no company and only 106 of 254 rows have any Form D history, so this is the run's dominant debt |
| `momentum_ruled_out` | 41 | hot-sector rows ruled out by §3's rule-out rather than searched; the claim carries its date |
| `stage_prior` | 38 | recent listings with no filing or press trace; the firm's classic entry stage at low confidence |
| `identity_uncertain` | 28 | mostly one-word names and merge candidates recorded rather than merged silently |
| `country_prior` | 20 | unidentifiable rows on a US desk |
| `cite_pending` | 19 | the resumable citation queue: $1B+ rows whose stage rests on model knowledge, plus four public micro-caps without a cited cap |
| `predecessor_era` | 18 | the Delta A class, marked for a one-class re-judgment |
| `model_disputes_source` | 15 | Wikidata countries and four wrong-entity floats overruled |
| `rule_a_below_1b` | 13 | rows a vendor calls a unicorn, published `below_1b` with the check recorded |
| `stale` | 7 | marks older than 24 months |
| `stage_disputes_band` | 5 | deliberate overrides of the band |
| `country_conflict` | 1 | Aura's CDI listing (US filing, ASX instrument) |

---

## 7. Open rulings for Erik

1. **Delta A — the Formation 8 legacy book.** §2 above. The one ruling the run needs.
2. **Asana is the `arista` class.** 8VC first lists it in 2022, after the September
   2020 direct listing, and no venture entry is documented. T3 says a position first
   appearing post-IPO is out; the site listing says in. Shipped as a member, raised
   as a boundary ruling — the same shape as Accel's arista, still open.
3. **Rule A publishes Altos Labs at `below_1b`.** The company launched in 2022 with
   **$3 billion** of committed capital and has never published a post-money. Rule A
   needs a priced round with a citable figure; a commitment is not one. The rule is
   applied as written, and the result is visibly odd. Same shape, smaller: Boom
   Supersonic, Resilience, Cityblock, Sila Nanotechnologies, BlueVoyant, Hive,
   Quince, Trackonomy, Qualia, Flexport, Airbyte, Erebor (before alignment).
4. **`8VC ERSA/ERSB` and the industry filter.** `build-company-base.py` drops Form D
   issuers in "Other Banking and Financial Services"; Erebor is a chartered bank and
   an operating company. Recovered by hand here — the filter is over-broad.
5. **Three siblings carry stale in-flight markers** (`accel`, `redpoint-ventures`,
   `yc`, plus `battery-ventures`, `felicis` and `greylock` which are genuinely
   running). Accel and Redpoint are closed per your notes, so those two are
   forgotten `close` calls, and this run's cross-investor pass skipped two large
   published bases because of them. Not touched (§12).

---

## 8. Proposed write-backs

**To `scripts/` (requested by session message, per §12 — a sibling wave is live):**

1. **Apply the tenure window in the Form D round history.** `formd-issuer-rounds.py`
   / `prepare` should not pick an out-of-tenure filing as the entry. 31 of 106 rows
   here. `scratch/enrich-queue.py` is the shape of the fix.
2. **Collapse roster name variants before the tenure filter.** "Alex Moore" and
   "Alexander Moore", "Drew Oetting" and "Andrew Oetting" are one person each and
   the sweep carries them as two — COLLECTION.md already names this defect; it is
   still live and it cost two membership adjudications here.
3. **`build-firm-profile.py`'s `hq_location` recompute breaks for a firm that
   moved.** The modal Form D address returned San Francisco on 10 of 19 filings
   because 8VC filed from there until 2020; the sworn ADV Item 1.F says Austin.
   Prefer Item 1.F where an ADV exists, or weight the most recent filing year.
4. **Widen the non-portfolio industry filter's exceptions** so a chartered bank is
   not dropped (Erebor).

**To `COLLECTION.md` (§5, a new evidence layer):**

> **A firm that runs single-deal SPVs often encodes the company and the round in the
> vehicle name.** 8VC's ~30 SPVs file "Indefinite / $0 sold" Form Ds naming no
> portfolio company, but their names are `<company initials> + S + <round letter>`
> (ADSF = Addepar Series F, ANSD/ANSE/ANSF = Anduril Series D/E/F, EPSD = Epirus
> Series D, PAIC = PathAI Series C, STSD = Saronic Series D) and the Form D date sits
> within six weeks of the round announcement in six of seven scored cases. Score the
> scheme before trusting it, treat it as corroboration rather than a label — two
> letters are ambiguous — and leave unresolved codes unresolved rather than guessing.
> Where a code's prefix, round letter and date all line up with a documented round it
> is `fund_filing` evidence that the firm's own money entered at that round, which is
> the evidence a predecessor-book question turns on.

**To `COLLECTION.md` (§5, the people-namespace rule):**

> The First Round rule generalises past its case rule: **the discriminator is
> whatever the firm's own rendering uses**, not the slug. On 8vc.com both partners
> and advisors live at `/team/<slug>` in lowercase-dash form, and only the index
> pages' card class (`square--team` vs `square--advisor`) separates them. **And a
> person can be in both sets in different years** — advisor first, partner later, or
> the reverse — so the rule is *team wins for identity, per-year for tenure*: an
> advisor-only year is not tenure, and a seat dated to one is not the firm's.

---

## 9. Usage

- Base rows: **254** published, 61 excluded, 330 verdicts.
- Web searches: **~20**, against a 200-per-session budget. The visible slice was
  carried mostly by **cross-investor alignment**: fourteen $1B+ rows took a cited
  figure from a sibling's published base rather than a fresh search (invariant 10
  paying for itself), and Rule A resolved thirteen more without one.
- Long pulls, all started in the first minutes (§12): wayback (11 yearly captures,
  255 slugs), partner roster (137 → 126 names), `run.py collect` (96 entities, 420
  Form D accessions), the site pull (175 companies, 51 team, 73 advisors, 249
  fellows, 224 posts), the two recall sweeps, the own-vehicle Form D pull (80).
- **Usage percentages not recorded.** §12 asks for the account's weekly and Fable
  percentages at kickoff and at close; this session did not read them at kickoff and
  will not invent them. Next run should read them first.
- **Prompt count: 2 so far** — the kickoff ("please collect 8VC") and one
  continuation. Not final until the ingest decision.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Twenty-eight published rows carried `identity_uncertain` (fourteen further
entries in `classification.json` are stale keys). 8VC's set divides almost
exactly three ways, and the middle group is the interesting one.

**Nine rows are identified AND have a real namesake**, so they take
`identity_homonym` with both named in the note: `galileo` (Galileo Health, not
Galileo Financial Technologies — the pair PRO-136 itself cites), `outset`
(outset.ai, not Outset Medical), `terra-industries` (Africa's defence prime,
not the fertilizer producer CF bought in 2010), `tome` (the presentation tool,
not Tome Biosciences), `kiwi` (the student lender, not Kiwi.com),
`terminal-logistics` (Terminal Industries, against the base's own `terminal`
row — already guarded by a `never_merge` pair), `vector`, `fractal` (Fractal
Software, against three other Fractals) and `luminate`.

**Eleven rows are named and lose the flag.** Six of them describe a twin
"to resolve at the identity step" that the rebuild already resolved:
`senti-bio`, `photys`, `pango`, `software`, `wispr-flow` and `vesta-home` all
absorbed their twins long ago and the notes were never retired. `aimip` is the
clearest case of a flag on a rendering rather than a company: 8VC's own card
maps that slug to AMP at amp.tech with a full description.

`transrisk-inc` is worth its own line. The note called it "possibly the same
position as FreightWaves (same founder, city and year)", and the tempting move
was to merge it — but `identity-merges.json` already rules that pair
`never_merge` on the evidence that they are two issuers with separate filings.
The row is Craig Fuller's Chattanooga freight-futures startup, reported as
such in December 2017, and it stays its own position.

**Eight rows read `undetermined`:** `agentic`, `beacon`, `castle-global`,
`farcast`, `melvi`, `rested`, `tap` and `zeno` — archive-only rows that are
gone from the live site with no filing or press trace. `tap` is the sharpest:
its site url (tap3d.com) does not match 8VC's own "Announcing TAP (Training
All People)" post, so the firm's two surfaces disagree about which company the
row is.

`verify --in-flight` clean. 8VC is mid-S2A-wave with a live in-flight marker,
so this pass did not rebuild, re-export or close.
