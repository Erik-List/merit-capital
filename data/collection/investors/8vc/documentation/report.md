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

## 2. The delta — settled by Erik's standing ruling

**Delta A, the Formation 8 legacy book, is closed.** Erik's partner-carried ruling
of 2026-09-17 (a listing that exists because a partner backed the company at a
previous firm is not a member) binds every investor and is Delta A's recommended
reading. `decisions.md` R1 applies it row by row, on evidence, never by era.

*Out:* Palantir, Wish, Oscar (+ Mulberry Health), Guardant Health, Illumio, OpenGov,
Color (+ Color Genomics), RelateIQ (+ SalesforceIQ), Oculus, Hyperloop, Revinate,
and three the close had wrongly kept for lack of evidence: **Radius**, **BuildZoom**
and **Nyansa**, each with a Formation 8-led round on the record (found at ingest
prep, 2026-09-24).

*In:* where an 8VC vehicle demonstrably took a position (Addepar via the ADSF/ADSG
SPVs, Zenreach/Adentro, Joby, Blend), and where nothing shows the position was the
predecessor's (Affinity, Qualia, Blink Health, Kiwi, Progressly, Castle Global).

*The fact behind it:* 8VC's own 2016 team page calls Formation 8 "**the precursor
fund to 8VC**" and lists Lonsdale's board seats as his.

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

Settled since the close: the **two country conflicts** from the city pass, corrected on Erik's instruction 2026-09-24 (Terra Industries → NG, Abuja; Luminate Medical → IE, Galway) and re-ingested; **Delta A** (by the 2026-09-17 partner-carried ruling, see
§2) and **Asana**, which is not the arista class after all: 8VC Fund I and
Entrepreneurs Fund I signed its pre-IPO investors' rights agreement, filed with the
January-2020 DRS (`decisions.md` R2). The stale-marker item is gone too.

Still open:

1. **Rule A publishes Altos Labs at `below_1b`.** $3 billion of committed capital
   and no published post-money. The rule as written; the result is visibly odd.
   Same shape, smaller: Boom Supersonic, Resilience, Cityblock, Sila, BlueVoyant,
   Hive, Quince, Trackonomy, Qualia.
2. **The industry filter is over-broad.** `build-company-base.py` drops Form D
   issuers in "Other Banking and Financial Services"; Erebor is a chartered bank and
   an operating company, recovered here by a recall addition.
3. **The team's X links** all point at the firm's own handle (51 of 51), a fallback
   Lux already publishes. Left as it is.

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

## Addendum 2026-09-21: S2A with every Seed row decided (PRO-132)

The run published S2A on a cohort of ten (20.0%, §1), and the 2026-09-17
re-judge stopped mid-pass. PRO-132 makes the absence of a later round a
finding: a Seed row past the 24-month clock with no evidence of a later round
did not graduate, and every no records the dated search that found nothing
(the firm's archive, the Form D sequence for a US company, at least two
publisher surfaces; COLLECTION.md §6). The 73 open rows were judged in two
batches.

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 69 | 13 | 56 | 33 | 23 | 58.9% | 100% |

Of 69 seed entries, 13 were too recent to count; of the 56 that remain, 58.9%
raised a later round. Of the 23 that did not, five rest on the filings, four
on a cited end and 14 on a dated search of the named surfaces. Twenty-six
decided rows rest on an uncited stage (the firm's listing gives no round
word), flagged `stage_uncited` at low confidence.

What moved:

- Re-staged out of Seed on a page naming 8VC in a later round: Nines
  (the $16.5M Series A of 2019), Rephrase.ai (Series A, 2022), HDVI and
  Socotra (Series A), Indigov (Growth) and Vector (the $10M Series A of
  April 2019 "led by Goldcrest Capital and 8VC", FreightWaves).
- Nineteen rows read `undetermined` in the stage because nothing dates an
  8VC entry, most of them bare-word names whose search results are all
  homonyms (Kiwi, Levee, Neighborly, Shogun, Tome and others), plus Commure,
  Flux, Infra and Software.com, which the batch judges left for review.
- RealScout: the Form D layer read a 2016 $6M filing as the entry; the seed is
  the $1.1M of August 2013 from DCM and Formation 8, followed by a named
  Series A in November 2014, so the row graduates.
- A search gap: the surfaces query the row's name as written, so "Cellino
  Bio" found nothing while the press says "Cellino"; the judge found the
  $80M Series A by hand. Suffix words (Bio, Labs, AI, Health) are worth
  stripping in `graduation-surfaces.py` before the next sweep.

`c2a_rate_max` stays at the 0.80 default. `verify` is clean.

For Erik: **Training All People** is graduated on a 2026-02 release announcing
"a new investment" from 8VC and three other funds with no round name and no
amount, so neither the named-round rule nor the unnamed-round bar decides it;
the judge chose graduated over an absence claim the release contradicts.
**Twingate**'s entry date is the company's founding year (2019), since no
dated seed exists.

## Ingest 2026-09-24 (Erik's approval, this session)

**250 companies live, investor row and icon published, readback exact.**

Before the write, the book was brought up to the rulings made after the close
(commit 41780a8, details in `decisions.md` R1 to R4):

- **Delta A closed** by Erik's partner-carried ruling of 2026-09-17; three more
  Formation 8 rows out on their round evidence (Radius, BuildZoom, Nyansa).
- **Asana stays in**, on `fund_filing`: 8VC Fund I and Entrepreneurs Fund I signed
  its pre-IPO investors' rights agreement (January-2020 DRS), so the T3 post-IPO
  ruling does not reach it.
- **Myeloid Therapeutics = CREATE Medicines** (rebranded 2025-10-06): folded, with
  its decided entry and graduation carried onto `create`.
- **City pass** under the city rule that landed today: 206 of 250 placed, 36
  recorded unknown, 8VC taken off the city-debt ratchet. Two country conflicts
  flagged (Terra Industries, Abuja; Luminate Medical, Galway), then corrected on
  Erik's instruction the same evening: US → NG and US → IE, re-ingested, readback exact.
- Four merge groups pin their names so the rebuild cannot publish legal-suffix
  forms (Nest Health, Adentro, Pango, AMP).

**Order, as §9 sets it for a first ingest:** icon upload
(`investors/8vc-800a6c305d.png`; box 74%, radius 76%, contrast 10.1:1, ramp
0.97px, no enlargement), `ingest-investor.ts 8vc` (the row an earlier Greylock/
Khosla ingest had created by accident at 19:26 UTC, with a placeholder icon, was
overwritten with the real profile), then `ingest-companies.ts 8vc`: dry run 250
new, 0 removed, from 0 live; written to match.

**Readback** (`scratch/8vc-readback.ts`, read-only): 250 live = 250 in
`base.csv`, 0 differing cells across the nine shared columns; the investor row
matches `investor.json` up to JSON key order. Computed figures match `verify`:
23 / 3 / 0 at $1B+ / $10B+ / $100B+, 10 IPOs, S2A **58.9%** on a cohort of 56
(69 seed entries, 13 censored).

**A correction the readback forced, and a second write.** The first readback's
IPO list carried **Cambium**: the float layer had joined 8VC's Cambium (the
private Berkeley materials company) to Cambium Networks Corp, on a join it had
itself marked `cik_weak`, and my close never ran standing duty 3 over it. Auditing
all 110 weak joins found one more that had put a value on a published row:
**Vector**, whose `acquired` status came from Vector Group Ltd, the tobacco
holding company; 8VC's Vector (withvector.com) is private and bought YardView in
January 2026. Both corrected and re-ingested (0 new, 0 removed); the second
readback is the one quoted above. The same Vector Group float sits on
`lightspeed:vector` and `y-combinator:vector` (as-of 2023-06-30); recorded in
8VC's `distinct` rulings as a note for those books' owners, not fixed from here.

**Prompt count: 3, final** (kickoff, continuation, ingest approval).
