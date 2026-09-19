# Benchmark — collection run report (PRO-88)

**Run:** one session, 2026-09-06, under the merged shape of `../../COLLECTION.md`.
**Result:** `verify` clean in plain mode. **284 members**, 131 rows preserved in
`excluded.json` (88 other-desk, 43 not_member), firm profile through the taxonomy
gate, review surface rendered and checked.
**Prompt count: 1** (kickoff). The ingest approval will be prompt 2 — the target.
**Usage line:** kickoff percentages were not given for this session; weekly % and
Fable % to be filled at ingest, against 284 base rows.

---

## 1. The method delta — the first investor whose own site is archival only

Benchmark's live site is **one page**: a wordmark, two addresses and a Twitter
link. `/portfolio`, `/companies/`, `/sitemap.xml`, `/index.xml` and
`jobs.benchmark.com` were all verified 404 or non-resolving at kickoff. It has
been that page since 2013.

But the firm published a full portfolio list for the **sixteen years before
that**, and all four eras parsed:

| era | surface | measured |
|---|---|---|
| 1999–2001 | `/about/p-alpha.html`, the alphabetical list | 64 → 97 names |
| 2001–2005 | `/Portfolio/Portfolio_By_Location.html` + `/Silicon_Valley/Silicon_Valley_Portfolio.html` | 97 → 130; SV cut 84 → 89 |
| 2005–2009 | `/portfolio/worldwide.shtml` + per-desk pages | 135 → 165; SV cut 91 → 132 |
| 2010–2013 | the WordPress `/companies/` logo cards | 138 → 158 |

So the base has two halves with different evidence models, and the report should
be read that way: **1997–2013 is list-covered** (235 of 284 rows are
`site_listing`), **2013–2026 is the Thrive "no list" model minus the job board** —
the roster-name Form D sweep, the fund vehicles' own ownership filings, the
exit-side full-text sweep and the recall probe's press layer. 28 rows have a
`first_seen` in the 2020s and every one of them arrived through a filing or the
probe, never through a list.

**Archetype correction for PRO-87:** Archetype A assumes a live site the
escalation ladder can climb. Benchmark has none, and the ladder returned nothing
at every step. What carried the base instead was the **archive read five eras
deep** plus the firm's own **Form D related persons as a roster substitute**.
Any Archetype A firm that has gone quiet should be planned that way from the
start rather than discovering it at the ladder.

## 2. Phase 0 — derivations, and the one that changed under verification

Eight derivations (D1–D8), **no deltas**, nothing blocked. The full text is in
`decisions.md`; the two that mattered:

**The Balderton trap, ruled (D2).** Benchmark Europe (2000) became Balderton
Capital, fully independent in 2007. Its vehicles filed from Benchmark's own Menlo
Park address, so they are the firm's own desk *of that era* — but the successor
firm owns the track record, exactly as with IDG-Accel China, Lightspeed China and
HongShan/Peak XV, all of which went out whole rather than being cut at the split
date. The Israeli desk resolved the same way and more sharply: it is today
**Benchmark Israel VC 2007 Ltd, CRD 160374, its own SEC exempt reporting adviser
at 32 Rothschild Blvd, Tel Aviv** — T1's OUT limb read literally.

**How the split is actually read (D4)** is the part worth carrying forward. The
firm's own site published *separate portfolio pages per desk* from 2003 to 2009,
so the desk is readable off the path that listed a row, and the 2010–2013 list —
published *after* both separations — is the firm's own post-split claim on its
own book. Two positive rules, mechanically applied by `scratch/derive-desks.py`:
the post-split list decides, otherwise the desk page decides. Result: **50 Europe
rows and 38 Israel rows partitioned**, and the lists read exactly as they should
(Betfair, Bebo, Lovefilm, Yoox, NaturalMotion, Zopa, Codemasters on one; Gigya,
Metacafe, Panaya, Wilocity, Seeking Alpha on the other). MySQL and Wix stay on
the home desk because the post-split list carries them. **PRO-106 inherits all 88
rows in `excluded.json`.**

**D1 changed under verification and the change is recorded rather than quietly
corrected.** The issue asked whether a growth or opportunity vehicle exists. At
Phase 0 the answer looked like "a thematic sleeve only". It is more than that:

- **Benchmark Partners T1, L.P., $1.25B, filed 2026-06-30 — the firm's first-ever
  dedicated growth fund**, raised alongside a $750M early-stage fund (TechCrunch
  2026-06-03: $2B across two funds, "five to six large investments"). A real break
  with the ~$425M discipline the firm held from 2011 to 2024.
- **Benchmark AI Infrastructure Fund + Fund B, $223.94M, filed 2026-02-06** — not
  a thematic strategy but **two single-company vehicles raised to fund one
  Cerebras round** (TechCrunch: "created specifically to fund the Cerebras
  investment").

Both are IN under T1. The growth fund matters beyond the boundary: it changes
what `investment_stage` and the future entry-stage distribution mean.

## 3. The gate — the Form D band scored 7/16 and was demoted

Both calibration sets were pre-registered in `golden.json` before any verdict or
stage was written; scores and the layer decisions are in `scratch/gate.md`.

**Stage golden set, 25 cited rounds.** The band labelled 16 of them and got
**7 right**. Eight of the nine misses are one failure: *the band reads a later
filing as the entry round*. Discord's first swept filing is 2020 and the entry is
2016; Chainalysis 2021/2018; Timescale 2021/2018; Mercor 2026/2024; Legora
2025/2024 (and the entry is the **seed**, not the Series B); WeWork 2015/2012.

**The finding generalises past `entry_stage` and is the most consequential thing
this run produced (R5).** For a Form-D-only row, `first_seen` is *the first
filing on which a roster name appears as a director*. Benchmark leads seeds and
Series As that routinely never file, so **`first_seen` runs two to five years
late across the whole 2013–2026 half of the base**. Cerebras is the extreme case:
`first_seen` 2026, entry 2016. It is a ceiling on entry recency, not an entry
date, and it may not feed stage, the C2A cohort or any "recent" slice unchecked.
The site's own first listing year, by contrast, was checked on ten key rows and is
a sound bound: never later than the entry, at most one year earlier.

**Membership trap set, 33 rows: 30/33 blind, and all three misses were one layer
defect** — `formd_span` is year-granular while the boundary sits inside a year.
Fixed before the grind (`scratch/enrich-queue.py`): every queued row now carries
one line per (partner, quarter) with that partner's roster window and an
`in_tenure | pre_tenure | post_tenure | boundary` flag. 13 rows carry a boundary
seat and 13 a pre-tenure seat — a class, not a curiosity. After the fix the gate
passes **33/33, zero false members**.

## 4. Precision — two classes that would have published a false track record

**R7 — the asterisk is a disclaimer, and it takes 21 rows out.** Every listing
era 1999–2009 carries, at the foot of the page, the firm's own legend:
**"* Investments made by Benchmark Capital general partner(s) prior to the
formation of Benchmark Capital"**. Twenty-one rows carry the marker — **AOL,
Palm Computing, Synopsys, Rambus, Legato Systems, Kalpana, Collabra, eShop,
Ipsilon, Pure Atria, SDRC, S3, Geoworks, Avant!** and seven more. They are the
founders' pre-1995 deals from Merrill Pickard, TVI and their other prior seats;
no Benchmark fund held any of them, so T2 rules them out as one class.

This refines an evidence rule and is proposed for the playbook: §1 says a listing
on the investor's own site "suffices alone" for membership. **It does not, when
the site's own legend disclaims the row.** Without reading the footnote, 6% of
the base would have been false — and heavily weighted to famous names.

**R8 — twenty rows of the Form D sweep are other firms' seats.** Benchmark hired
four partners out of other firms between 2021 and 2026, so this class is large
for a base this size. Ruled cluster-first: Puttagunta's **NEA book** (8 rows,
every seat before his first Benchmark fund filing of 2018-10-01); Altman's **Alt
Capital book** (3, the last one *quarter* early) and **his own company**
(Degree, Inc. = Lattice); Grimshaw's **Thrive seat** (Benchling — a member of
both Thrive's and a16z's landed bases, which corroborates the attribution
directly) and his **next firm's** (Doji Labs); Randle's **pre-Benchmark Huntress
seat**; Beirne's **own post-Benchmark venture** (Fantex, founded 2012 by a
partner whose tenure ended in 2001); Vaden's post-tenure InXpo seats; and
Harvey's **three personal LLCs**. The deliberate counter-example: **Minerva
Project is a member on the same Kevin Harvey seat** — a cluster is resolved once
per person and then decided per row.

**R9 — a seeding defect the trap set caught.** `prepare` writes the basis "SEC
ownership filing by a fund vehicle" without checking whether the filer is a fund
or a natural person, and a row seeded `member` that way carries no `membership`
need, so **the judge never sees it**. Wealthfront was seeded member on Forms 3/4
filed by **RACHLEFF ANDREW S** — the founder's own filings on the company he
founded after leaving. A sweep of the base found one more: **Activision**, whose
1999–2001 Forms 3/4 were filed by **LASKY MITCHELL as an Activision executive**,
eight years before he joined. Both out. Proposed as a `run.py` fix.

## 5. Recall — the site's blind decade

The Form D sweep, the ownership crawl and the exit-side full-text sweep (256
registrants) were exhausted against the base; the EDGAR layer had no unlisted
members left. The **press probe over 2013–2026 found six**, all verified and
added: **Duo Security** (Benchmark led the $12M Series B, 2014; Cisco $2.35B,
2018), **LangChain** ($10M seed, 2023), **HeyGen** ($60M Series A, 2024),
**Decart** ($25M, 2024), **Reducto** ($24.5M Series A, 2025) and **Manus** ($75M
at $500M post, 2025; acquired by Meta that December). Two candidates were probed
and **rejected with reasons**: **Cursor/Anysphere** (an aggregator tags Benchmark;
the round record does not — every round was led by others) and **Sourcegraph**
(a wrong model prior carried in at kickoff, now removed from `known_positions`).

## 6. Duties, the A/B pass and cross-investor alignment

The blind 5% self-consistency pass disagreed on **3 of 14** rows and all three
were the same defect — a band-derived value on a row never queued. Swept
class-wide per duty 9: **WeWork** Growth → Series A, **Zendesk** Series A →
Growth, **Minerva** Series A → Seed, plus **Handspring**, **Mahi Networks** and
**Xignal** defunct → acquired. Four more rows the automatic sweep flagged were
cleared on re-read and the clearance recorded.

Cross-investor alignment corrected **two of my own rows** from sibling evidence:
**Confluent** was acquired by IBM on 2026-03-17 ($11B) while my row carried
public/$7.2B off a stale float, and **Supergreat** shut down rather than being
acquired (Thrive's row: team hired by Whatnot). Marks aligned to the freshest
cited side on Decart ($4.0B), Exa ($2.2B), Legora ($5.55B), LangChain ($1.25B),
Docker ($2.1B) and Snap ($9.45B, dropping my float-derived 10b_plus). Bo.lt was
ruled **distinct** from the Estonian Bolt three siblings hold. **60 of 60 shared
rows now agree.** Contentful turned out to have been acquired by Salesforce in
June 2026, and Cerebras is now public at $49.9B.

**Rule A was applied to four rows** whose band rested on the unicorn snapshot —
an aggregator, never a mark. Discord, Airbyte, Chainalysis and Quora were
re-pinned to their priced events with citations; Chainalysis moved from the
snapshot's $4.2B estimate to the $8.6B Series F.

## 7. Results

284 members. **Evidence:** 235 site_listing, 34 formd_adjudicated, 9 fund_filing,
6 web. **Era:** 43 rows first seen in the 1990s, 157 in the 2000s, 56 in the
2010s, 28 in the 2020s. **Status:** 145 acquired, 50 defunct, 39 private, 28
unknown, 22 public. **Stage:** 243 Series A, 29 Growth, 11 Seed, 1 Pre-Seed —
the most Series-A-concentrated base this project has produced, which is what an
equal partnership that leads first institutional rounds should look like.
**Valuation:** 24 rows at $1B+ (8.5% of the base, well under the 20% guard), 6 at
$10B+, 2 at $100B+ (Equinix $102.2B, Uber $154.7B). **C2A** (superseded by
§11, 2026-09-16): 10 cohort rows, 8 graduated — 80%, and that rate is quoted
with its selection bias, not as a finding: the cohort is tiny because
Benchmark almost never enters at seed, and knowledge-true graduations are
easier to establish than confirmed non-graduations.

**Debt carried, all flagged:** 65 `stage_prior` (dot-com-era rows with no
documented round), 35 `stale`, 12 `stage_uncited`, 10 `cik_weak`, 10
`identity_uncertain`, 9 `model_disputes_source`, 8 `needs_web_value`, 5
`cite_pending`, 4 `unstable`, 3 `cohort_unverified`, 3 `suspect_base`. 144 rows
have no `hq_city`. The 3 `suspect_base` rows record how the value *first*
arrived and are superseded by cited figures.

**Deliberate coverage note:** 65 `stage_prior` flags and 19 rows outside the
focus taxonomy both sit in the 1999–2005 dot-com tail, where the firm's own list
is the only surviving record of companies that left no other trace. That is a
property of a thirty-year book, not unfinished work.

## 8. Firm profile

`investor.json` + `investor/sources.json`, built against the landed base: HQ
Woodside, CA (20/23 own filings; the site lists San Francisco first and the
sidecar records the discrepancy), founded 1995, **AUM $7,582,538,663** (ADV
Section 7.B composite, 34 funds, 2026-03-24 — an ERA with no Item 5.F), 13 funds,
8 people, stage [Seed, Series A, Growth], geo core US, ten focus values, range
{$3.5M, $13.5M, $225M}.

Two profile findings worth carrying:

- **Benchmark names its ADV funds by numeric code** ('1094', '2165', '2645' …)
  under rule 204-2(d), which permits an adviser to preserve a fund client's
  anonymity. The $7.58B composite is sound; **the per-fund attribution is simply
  not available**, so the fund table is built from Form D instead.
- **Its Form D filing style is the opposite of Lightspeed's.** Benchmark files the
  **full fund size as the total-offering amount** at or before first close, so the
  *offering* is the fund size and *sold* is the close state on the filing date —
  Fund VII shows $5M sold against a $425M offering. §11's $0-sold cross-check
  reads backwards for this filer and the sizes are the offering amounts.

**Icon: resolved, and it passes every rule with no override.** The site declares
no favicon, apple-touch-icon, manifest icon or og:image, so `--discover` has
nothing to measure — because the wordmark is rendered as an **icon font**
(`@font-face 'benchmark'`, `.benchmark-icon-benchmark:before {content:"B"}`).
That makes the mark a **vector**, which is what the rules prefer: glyph U+0042 was
extracted from `fonts/benchmark.svg` into `sources/site/benchmark-mark.svg` on the
site's own palette (cream #f6e3c9 on the body navy #1c364e). Dry run: vector at
2×, box 74%, radius 75%, **contrast 6.2:1** against the 3:1 floor, **ramp 1.50px**
against the 2px limit, upscale 1.00. Nothing uploaded — the bucket write is part
of the gated ingest.

## 9. Open rulings for Erik

1. **Galyan's Trading Company** — a 1995 buyout of a sporting-goods retailer out
   of The Limited, led by Freeman Spogli with Benchmark alongside. Kept as a
   member on the firm's own listing, entry Growth. Under the 2026-09-04
   control-position addendum a transaction in which the firm's **co-investor
   group** takes control is out; whether that reaches a minority co-investor in a
   retail LBO is a boundary ruling, not a row fix. One row today, but the rule
   will meet Battery, Khosla and NEA later in the wave.
2. **Twin Health** — member at medium confidence on the a16z director-of-record
   pattern (Dunlevie on every filing from the company's first, all in tenure).
   Against it: no Benchmark fund on any filing, no announcement, and the firm
   published nothing after 2013 so absence proves little. The single weakest
   member in the base.
3. **Broadcom** — appears once, on the 2001 capture, with no other evidence. The
   likeliest reading is the row standing in for Epigram, Broadcom's 1999
   purchase. Kept as a listed row with the identity question recorded.
4. **The pre-window contradiction in the playbook.** §1's policy constants say
   entries before 2006 carry "entry_stage and graduation null", but `verify`
   requires 100% fill and **no landed run has ever nulled them** — Sequoia and USV
   both fill pre-2006 rows at model/low. This run followed the landed practice
   (§6's pre-2003 Series A convention), which matters here more than anywhere:
   200 of 284 rows predate 2006. Either the sentence or the practice should
   change; a session should not have to choose.
5. **Three cross-investor rulings** written in `cross-rulings.json` (Bo.lt vs
   Bolt, three pairs) — the shared file is untouched, per §12.

## 10. Playbook write-back proposed

Five investor-agnostic rules, in `scratch/collection-writeback.md`, nothing
committed to `COLLECTION.md` from this session:

1. **§1 evidence sufficiency** — a site listing suffices *unless the site's own
   legend disclaims it*. Read the footnotes before trusting the rows (R7, 21 rows).
2. **§1 seat dating** — a continuing board seat first taken at a prior firm stays
   the prior firm's. The test is the seat's FIRST year, not the filing's (R6).
3. **§1 / §8** — seed `member` from an ownership filing only when at least one
   filer CIK is a **fund vehicle**, not a natural person; queue the row otherwise
   (R9, a `run.py` fix).
4. **§6 / §8** — `first_seen` on a Form-D-only row is a ceiling on entry recency,
   not an entry date, and must not feed stage, the C2A cohort or any recency
   slice (R5). Generalises §6's existing rule about the first *filed round*.
5. **§11 funds** — test the filer's style before applying the $0-sold
   cross-check: some firms file the full fund size as the offering.

Plus two mechanical fixes made in this run: `wayback-pull.py`'s `listing_regex`
now collapses internal whitespace in extracted names (a listing that wraps a name
across source lines was publishing the newlines), and `scratch/enrich-queue.py`
is offered as the quarter-level seat-dating step.

## 11. S2A re-judged under the status contract (2026-09-16)

`seed_to_a_graduation` became a judged status (`graduated | not_graduated |
censored | undetermined`, COLLECTION.md §6). `migrate-graduation` dropped the 9
legacy values and 3 `cohort_unverified` flags; the 11 Seed rows were re-judged
in one batch (22 web calls) with both legs cited in the same pass.

Four rows left the cohort because the citation places Benchmark's entry at a
later round: Boku (Series A on the $13M June-2009 round, whose two 2009q3
closes the Form D layer had read as entry plus graduation), uShip (Series A,
June 2005, the firm's own release), Blue Hexagon (a quietly led $6M Series A,
2019) and Stitcher (Growth: the $6M was a Series B after a 2008 Series A).
Polyvore's anchor moved to the earlier unlettered $2.5M round, its graduation
being the $5.6M Series B the layer had taken as the entry. LangChain and
Legora kept their seeds with stronger citations (the companies' own seed
posts) and graduate on cited Series As; Minerva's $25M "largest seed to date"
graduates on its $70M Series B.

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|---|
| 7 | 0 | 0 | 7 | 7 | 0 | 100% | 100% |

Of 7 seed entries, none was too recent and all 7 could be established, and
all 7 graduated. A Series-A firm's seed book is a handful of documented
winners; the rate publishes with its seed count, the app ranks no cohort
under 30 rows, and `verify.shape.c2a_rate_max` is restated at 1.0 against
this evidence (R10).

**Pre-window flag applied** (the 2026-09-07 constant): the 145 rows first
seen before 2006 now carry `pre_window_entry`, their model label at low
confidence (143 rows; two cited stages keep theirs) and graduation null by
rule. Rows first seen 2006–07 whose notes claim an earlier entry (Prosper,
Silver Peak, Zillow, Igglo, ManiaTV) stay unflagged: the note is the only
claim. Entry stages now Series A 246 / Growth 30 / Seed 7 / Pre-Seed 1.

**Class finding**: a later filing in the entry round's own quarter is a
second close, not a graduation; the deterministic layer read Boku's that way.
A same-round guard for `graduation_from_formd` is proposed in `run.py`.
`verify` is clean.

## 11. Ingest request (runs only on Erik's approval)

```bash
tsx scripts/fetch-investor-icon.ts benchmark "$PWD/data/collection/investors/benchmark/sources/site/benchmark-mark.svg"
npm run ingest:investor -- --investors name=benchmark
npm run ingest:companies -- benchmark
```

Order matters for a first-time investor: icon, then the investor row, then the
284 companies (the companies ingest refuses to run before the investor row
exists). Wave alignment with the rest of PRO-87 happens once, at the end.

## 12. Files

Top level: `config.json`, `decisions.md` (D1–D8, R1–R9), `golden.json` (33 traps,
25 cited stage rows), `identity-merges.json` (16 merges, 86 desk reassignments,
1 never-merge), `cross-rulings.json`, `entities.json` (62), `base.json` /
`base.csv` (284), `excluded.json` (131), `classification.json`,
`membership-ledger.json` (343 verdicts, 6 recall additions, 2 rejections),
`resolved.json`, `review.html`, `investor.json`, `investor/sources.json`, this
report. `sources/`: site (the 2010–2013 list, team, the extracted mark), wayback
(nine parsed eras, curated roster, desk rosters), edgar (Form D sweep 313
accessions, 62 entities, own fund filings, FTS 256 registrants, issuer rounds),
registers (the ADV PDF). `scratch/`: `gate.md`, `derive-desks.py`,
`build-roster.py`, `own-formd-persons.py`, `enrich-queue.py`, `build-site-list.py`,
`emit.py`, the queue and out files, the run logs, `collection-writeback.md`.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Ten published rows carried `identity_uncertain` (the other twelve flagged
entries in `classification.json` are stale keys for rows the merges already
absorbed). Two were stale wording, eight were real.

**Two flags retired, values kept.** `opsware` and `juniper-bank` both read
"suspected duplicate, flagged for the identity-merge file" — wording written
during the grind and never revisited after the rebuild landed
`loudcloud → opsware` and `juniper-financial → juniper-bank`. Both companies
are named and described, so under the 2026-09-18 rule they carry no identity
flag at all.

**Eight rows publish `undetermined`.** `abaco-international-group`, `arteis`,
`compression`, `conduit`, `encompass`, `ens`, `northstar` and
`telecommunications-labs` are single-name rows from the 1999–2012 archived
listings where the firm's own page is the only surviving trace. Every one of
them published `entry_stage: Series A` sourced `model` — the inferred fill the
new rule abolishes — and five of the eight did not even carry `stage_prior` to
show it, so a sweep keyed on that flag would have missed them. All eight now
read `undetermined` in `entry_stage` and `valuation_range`; the four
pre-window rows keep a null graduation (that rule outranks this one), the
other four read `undetermined` there too.

`conduit`, `encompass` and `northstar` are the sub-case where real namesakes
exist but none was ruled in — for `conduit` the Israeli toolbar business,
which would belong to the partitioned Israel desk. Under PRO-136's own rule
("where the name resolves to nothing, treat as `identity_unresolved`") they
are unresolved rather than homonyms: `identity_homonym` is for a row we HAVE
identified that must never be fused with its namesake. The candidates are
named in each note, so a later pass can pick one up.

`verify` clean; eight rows excluded from every distribution and every metric.
The S2A block is unchanged (7 seed entries, all graduated), because none of
the eight was a Seed row.

### Follow-up the same day: invariant 10 and an unnameable row

Making the eight rows read `undetermined` turned invariant 10 red on
`benchmark:conduit`, which the loose name key joins to YC's own `conduit`.
The Benchmark session put a `distinct` ruling in as a stopgap and handed the
structural fix over; it is now in `run.py` and the stopgap is deleted.

A row flagged `identity_unresolved` has no identity behind its name, so every
cross-investor pair it forms is unsound by construction rather than a
disagreement to adjudicate — ruling each pair `distinct` would be treating a
class as rows. `verify` now leaves such rows out of the comparison on both
sides and says how many it left out. Across the twenty published bases three
pairs were already affected and two had been papered over by hand.

The four pre-window rows also now store `undetermined` rather than null in
the graduation: `undetermined` is not a graduation claim but the absence of
one, so the store and the published CSV say the same thing and the database
takes the same value the base does.
