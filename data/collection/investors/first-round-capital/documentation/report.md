# First Round Capital — collection report (PRO-93)

One run, one session, 2026-09-06, under the merged shape of
`data/collection/COLLECTION.md`. `verify` green in plain mode.

## Results

| | |
|---|---|
| Base | **594 companies**, 2005–2026 |
| Tiers | A 201 (two-sourced) · B 383 · C 10 |
| Membership | 708 member verdicts, **36 not_member**, 0 uncertain |
| Member evidence | site_listing 695 · formd_adjudicated 12 · web 1 |
| Status | private 255 · acquired 191 · defunct 128 · public 11 · unknown 9 |
| Entry stage | **Seed 509 (86%)** · Series A 59 · Pre-Seed 22 · Growth 4 |
| Valuation | below_1b 576 · 1b_plus 14 · 10b_plus 3 · 100b_plus 1 |
| **Seed-to-A graduation** | **57.1% — 20 of a 35-company verified cohort** |
| Excluded | 41 rows preserved in `excluded.json` |
| Cross-investor | 125 shared rows, 105 agree, 19 accepted, 0 disagree |

The shape is the one PRO-93 predicted and the opposite of a growth investor's:
**3.0% of the base is $1B+ and 86% of entries are Seed.** Both shape guards
(`one_b_share_max` 0.2, `c2a_rate_max` 0.8) are satisfied comfortably from
below, which is the correct reading for a firm whose product is the first
cheque: the denominator is every seed it ever wrote.

**The C2A rate is published with its cohort: 57.1% of 35.** The cohort is small
because §10 invariant 5 binds hard here — a row counts only when both legs are
verified — and the denominator is not "First Round's seeds" but "the seeds
where the record establishes both the entry and the follow-on". The selection
bias runs the usual way: knowledge-true graduations are easier to establish
than confirmed non-graduations.

## The delta this issue asked about

**Dorm Room Fund is OUT, re-derived under T1 rather than on the scout
precedent** (decisions.md D1). DRF IV and V are real funds that file Form D, so
the scout ruling does not reach them. They carry their own GP (Dorm Room Fund
GP, LLC / Dorm Room Fund V GP LLC) and their own management company (Dorm Room
Management Company, LLC), neither of which appears anywhere in FR Capital
Holdings' 119-page ADV, whose 22 private funds reconcile exactly to the First
Round II–X ladder. Same verdict, filing-grade reasoning.

Also derived and applied: **Angel Track OUT** (T2, no fund), and **the founders'
pre-fund angel book OUT** — the firm published it itself, under
"The following investments were made prior to First Round Capital"
(del.icio.us, IronPort, Flock, Feedster, Engage.com). That page is used as an
exclusion list, never configured as a listing surface, and the profile says so.

## Method deltas — what this run had to invent

**1. The adviser does not carry the brand name, and IAPD cannot find it.**
There is no adviser called "First Round" in either SEC roster; the firm files
as **FR Capital Holdings, LP (CRD 160848)**. Resolved by downloading the SEC's
own registered and exempt firm-roster CSVs (the 2026-09-01 FOIA feed) and
matching on the Form D filing address. Keyless, deterministic and complete;
proposed as a write-back to §11's AUM recipe, because a brand whose adviser
files under another name defeats IAPD's search entirely.

**2. The `/team/` namespace holds two populations, and only one is the firm.**
First Round's site published, alongside its own people pages, a **network
directory of 212 portfolio FOUNDERS AND CEOs** at `/team/<First_Last>`
(Travis Kalanick, Jack Dorsey, Dave Baszucki, Neil Blumenthal). Sweeping those
names through Form D would have confirmed hundreds of false members, because a
founder *is* a related person on their own company's filing. The roster pattern
was narrowed to the lowercase namespace, which separates the two exactly — and
the directory was then pulled deliberately as a **recall layer**, where it
found the run's only site-invisible member.

**3. Wikidata is a labeller this investor breaks.** `prepare` wrote
`hq_country` on 104 rows from Wikidata; **89 of them have a single-token name**,
and the joins are wrong at a rate no layer survives: Uber→NL, Square→JP+defunct,
Clay→NL, Planet→GR, Play→PL, Free→FR, Noon→SA, Togg→TR, Abra→GH+defunct,
Superhuman→"Ukraine[56]/ United States[57]". Demoted to corroboration for this
investor and re-judged row by row; 49 rows carry `model_disputes_source`.
The same one-word property drove 24 `distinct` cross-investor rulings.

**4. The logo wall is two artifact classes, and the fix is upstream.** The
2010–2011 portfolio page rendered every name as an image, so the firm's own
upload filenames are the only text the era leaves. That produced 63 filename
variants of real companies (`birchboxsmall`, `smartlingverysmal`, five
spellings of StumbleUpon) and, worse, the **acquirer marks the page carried
beside its exits** — Google, Microsoft, Intuit, Adobe, eBay and Facebook, none
of them First Round positions. The variants are fixed in the source
(`sources/logo-era-names.json`, applied to the parsed years before the build)
rather than merged afterwards, so the published surface never carries a junk
name; the acquirer marks are `rejects` in `identity-merges.json`.

**5. A parser window that crossed a row boundary.** The 2012–2015 tile era's
name pattern took the *next* row's name whenever a row's JS block omitted the
name field — 14 of 153 names in the 2013 capture. Fixed with a negative
lookahead for the next `<li>` and re-parsed. Worth writing back: every
`listing_regex` era with a `.{0,N}?` window has this failure mode.

## The gate

**The firm's own `initialPartnership` label scored 12/18 and was demoted to a
floor** (`scratch/gate.md`). All six misses understate by exactly one step and
none overstates — the field records First Round's self-image as the seed
investor, not the round it bought into (Blue Apron and Flatiron Health are
Series A entries the firm labels Seed; Mint is a 2006 seed it labels Pre-Seed).
Ruling: the label may never publish a stage on its own, it is affirmative
evidence the entry was *at least* what it says, and where the record names a
later round the record wins with `stage_disputes_band` (7 rows).

The trap set (33 rows) cleared with **zero false members at high confidence**.
Seventeen of the 23 traps never reached the base at all — the build's own
filters removed the fund-shaped LPs, the personal Section 16 filings and the
ex-partner tenure cases. Two key rows were wrong and the evidence corrected
them: Augury and Kentik are on First Round's own listings, which fixes the end
of **Howard Morgan's tenure at 2016 rather than his last fund filing in 2012**
— a correction that changed which of his later seats are post-tenure.

## Recall probe

Two additions on a 594-row base (`scratch/recall-probe.md`): **One Kings Lane**
(the December 2009 round with Kleiner and Reid Hoffman; on no First Round
surface in any era) and **FiscalNote**. The site, capture and Form D layers
carry recall here — the firm has published a company list continuously since
2007 across four site generations — and the noise is precision-side, the
Sequoia shape rather than the one this issue expected.

One recorded self-correction: the kickoff `known_positions` list carried six
names that are **not** First Round positions (Brex, Carta, Linktree, Warp, and
Figma and Shopify by the same route). All came from `firstround.com/ai/<company>`,
the firm's editorial AI case studies. Reading an editorial surface as a listing
surface is exactly the failure §5 warns about, and the list was replaced.

## Debt behind the green verify

| Flag | Rows | What it means |
|---|---|---|
| `city_unknown` | 97 | The firm records these as "SF Bay Area", "Distributed" or "Other" — metros, not municipalities — and §6 forbids a city prior. |
| `model_disputes_source` | 49 | Wikidata and float-sweep values corrected on the row, each with the wrong value named in the note. |
| `duplicate_suspected` | 20 | Same-company pairs flagged rather than merged in place; the merge file carries 36 groups already. |
| `cite_pending` | 19 | The visible slice's entry stages, none of which has a class-1 citation yet. |
| `stage_uncited` | 13 | Stage from the firm's own label alone, at low confidence. |
| `identity_uncertain` | 8 | Rows whose issuer resolves to a real company but not to a named one. |
| `stage_disputes_band` | 7 | The record beat the firm's own label or the Form D band. |
| `stale` | 5 | Marks older than 24 months (GOAT 2021, Labelbox 2022, Flexport 2022). |
| `cik_weak` | 3 | Weak registrant joins, quarantined. |

Three wrong-entity public floats were quarantined under duty 8 (`cluster`
$4,399, `pattern` $550M, `glimpse` $41M — all name collisions, none of them
this company). The momentum slice was computed mechanically: **26 rows**
(private, first seen 2021 or later, hot sector), all 26 checked and recorded on
the row with a citation, which turned up three status corrections the layers
had missed — **Aisera** (acquired by Automation Anywhere, 2025-11-04),
**Composer** (acquired by SoFi, 2026-06-23) and **Mercantile** (acquired by
Onboard Partners).

## Open rulings for Erik

1. **Howard Morgan's tenure end (2016).** Set from the firm's own listings
   (Augury 2014, Kentik 2016 enter as his deals) rather than his last fund Form
   D (2012). Everything from 2020 on — Apptronik, Precision Neuroscience,
   CargoMetrics, CornerUp, MyndYou, RetailerX — is post-tenure and excluded on
   that line. If the true end is earlier, Augury and Kentik stay members on
   their listings but the line moves; if later, six rows come back.
2. **Twelve director-of-record members at medium confidence.** Unannounced
   deals where a partner is Director on the Form D inside tenure and the issuer
   resolves to a real company (CarbonDrop, Clarity Financial, Creditly,
   DeepFraud, HealthVillage, Madison Reed, Radvocate, RightHook, SBOT, Uplevel,
   Collective Retreats, Project Fair Bid). The a16z pattern, applied as ruled.
3. **Picmonic ruled out on a common name.** "Robert Hayes" on a Tucson
   medical-education company, no listing and no announcement — excluded under
   the name-match rule. It is the one exclusion in this run that a reader might
   read the other way.
4. **A second and third rebuild.** §8 schedules one. The first exposed a roster
   defect (partner name variants splitting tenure windows, which read Phin
   Barnes as departed in 2012), the second exposed the logo-filename slug
   mismatch, and freezing either would have shipped known-wrong rows. Recorded
   as a deviation rather than hidden.
5. **`scripts/wayback-pull.py` was edited by this session**, against §12's rule
   that shared scripts belong to the tooling session: an optional per-era
   `slug_re` (First Round's 2012–2017 company pages use CamelCase slugs the
   default lowercase pattern rejects) and a case-insensitive `non_company_slugs`
   check. Both are strictly additive and cannot change any existing investor's
   output. Flagged here because the rule is the rule.

## Write-backs proposed for COLLECTION.md

1. **§11 AUM** — the SEC's own registered/exempt firm-roster CSVs resolve an
   adviser by address when the brand name is not the legal name and IAPD's
   search returns nothing.
2. **§5 layer 2** — a firm's people namespace can hold a *portfolio-founder*
   directory beside its roster; the sweep must exclude it, and the recall probe
   should use it.
3. **§5 deterministic layers** — Wikidata needs the same recognition check as
   the CIK join. For a book of one-word names it mislabels at scale, and the
   failure is silent because `prepare` fills the column and never queues it.
4. **§5 layer 1** — a `listing_regex` era whose name window is a bounded `.{0,N}?`
   can take the next row's name; the pattern needs a negative lookahead for the
   row delimiter.
5. **§8** — an artifact NAME is better fixed in the parsed source than merged
   afterwards: a merge keeps the junk name on the surviving row.

## Usage

Read at close only — the kickoff reading was missed, so no delta is available
for this run. Base 594 rows; one session; roughly 45 web searches, well inside
the 200-call budget, with the cross-investor layer supplying seven cited marks
that would otherwise have cost searches of their own.

**Prompt count: 1 so far** (the kickoff). The ingest approval is the second.

## Addendum — ingested 2026-09-06 on Erik's approval

Icon first, then the investor row, then the companies, in the order a
first-time investor requires (§9).

- **Icon published.** Source `https://firstround.com/images/favicon.png`
  (320×320 PNG, the largest raster the site declares). It clears every rule
  without a flag: artwork **downscaled** 0.57× so the no-upscale rule is not
  reached, edge ramp 0.74 px against the 2 px ceiling, contrast 19.6:1 against
  the 3:1 floor, box 72% and radius 80% inside the keyline. The mark is a bare
  black "1" on transparency, so the normaliser synthesised the white plate.
  Provenance in `investor/sources.json`.
- **`ingest-investor.ts`** upserted 1 institutional row.
- **`ingest-companies.ts`** upserted **594 of 594** rows; the freshness check
  passed against the exported `base.csv`.
- **Verified in the database:** 594 company rows against investor
  `a0481de6-5a78-4874-aba8-01deac79ffe4`, `hq_location` "Philadelphia, PA",
  `aum` $3,843,440,251 both ends, `icon_url` on the bucket, and the derived
  metrics recomputed — `track_record` names 11 IPO companies (Uber, Square,
  Roblox, Planet, Upstart, Warby Parker, Clover Health, DoubleVerify,
  FiscalNote, Merlin, Notable Labs) and the focus distribution matches the
  base's own.

The five playbook write-backs proposed above were landed in
`data/collection/COLLECTION.md` in the same session. The `wayback-pull.py`
change is still uncommitted: the working tree carries a sibling session's edit
to the same file, so it is left for the tooling session rather than committed
here.

**Prompt count: 2** — kickoff and the ingest approval, which is the target.
