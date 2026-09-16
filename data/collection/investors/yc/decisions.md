# Y Combinator — investor-specific decisions

Derived from the standing rule set (COLLECTION.md §1) under the derivation
protocol: one line per category, the facts found, the test applied, the
outcome, the precedent. Derivations need no confirmation; deltas do.
Run-time standing rulings are dated and flagged for review.

Slug `yc`, display name **Y Combinator**. Run PRO-74, opened 2026-09-06.

---

## Part 1 — Derivations

### D1. Firm boundary (T1) — the accelerator and its own funds

**Facts.** Twenty EDGAR filers address-verify to 335 Pioneer Way, Mountain
View CA, YC's own address, and no other address appears among them:

- batch vehicles: `Y Combinator ES20, LLC`, `ES24`, `ES26` (promoted by
  YCBATCH20, LLC / YC Batch24, L.P. / YC Batch26, L.P. respectively)
- main funds: `YC II, L.P.`, `YC III, L.P.`
- affiliates: `YC Affiliates Fund II, L.P.`, `II (QP)`, `IIA`
- principals: `YC Principals Fund II, L.P.`, `III`, `YCP24, L.P.`, `YCP26, L.P.`
- programme/sleeve vehicles: `YC ESP22`, `YC ESP24`, `YC ECO24`, `YCA26`,
  `YCC20`, `YCCG21`
- growth: `Y Combinator Continuity Fund I, L.P.`,
  `Y Combinator Continuity Affiliates Fund I, L.P.`

**Test.** T1 (same adviser / same operation). **Outcome:** all twenty are
IN as one firm; there is no brand-sharing entity with its own fund family
among them, and no desk partition is needed — YC runs one global programme
from one address, so `desks.home` is `us` with an empty partition.
**Precedent.** a16z's vertical families under one adviser; Thrive's
umbrella with its sleeves and lettered LLCs.

### D2. YC Continuity is IN, as YC's own growth fund

**Confirmed by Erik 2026-09-04**, and already recorded in COLLECTION.md §1
under T1's precedent list. Not re-opened here. The consequences this run
carries end to end:

- **The base is not batch-defined.** The directory enumerates batch
  companies; Continuity-only holdings are invisible to it and come from the
  fund's own filings and press.
- `entry_stage` for a Continuity-only row follows the Continuity round
  (Growth by taxonomy), not the batch mode.
- The trap set carries Continuity holdings as known-**trues**, and the
  adjacent noise (companies Continuity was reported to be circling but
  never funded) as traps.

### D3. Alumni-founded is not funded (T2)

A company founded by a YC alumnus that no YC vehicle backed is **not** a
member. **Test.** T2 (fund money). The association is dense enough in press
that this is a class-wide ruling rather than a per-row call.
**Precedent.** COLLECTION.md T2, "companies founded by the firm's alumni
that no fund backed".

### D4. Partner personal positions OUT (T2/T4)

A partner's own angel cheque is not a firm position; ex-partner filings are
dated against the person's firm at filing time; LP stakes are out.
**Precedent.** Kushner (Thrive); Cherry's founder-angel positions (Erik,
2026-09-04). The Form D related-persons sweep over YC's 23-name roster
returned 109 accessions and this ruling is what most of them meet: an
accelerator does not take board seats at a rate that makes the layer a
membership source, so every hit is judged cluster-first (§3) and lands
`not_member` unless a YC **fund** held the position.

### D5. The string trap, resolved by address and never by name (T5/§5)

Two external classes wear the YC name and a name rule pulls in both:

1. **Third-party access and SPV vehicles** selling exposure to a batch —
   Stonks' per-batch Access Funds, `GCW Access - Y Combinator, L.P.`,
   Poolit, `YC Allocate AF26 AI/QP, L.P.` (502 Waverley St., Palo Alto —
   Allocate's address), `YC ALUMS FUND 2021 LLC`, and the
   CGF2021 / Kolysh / A7 Capital / Kepler series SPVs. Every one is an
   LP-side feeder: OUT under T5 (fund-shaped) and T3 (no venture entry by
   a YC fund).
2. **Plain namesakes** with no YC connection: YCG LLC and YCG Mutual Funds
   (a Texas asset manager), YCharts, Yclip, YCurb, the Massachusetts
   YC/YCC/YCH Holdings entities, the New York YCP funds, `YC 1926 (BVI)
   LTD` (Tortola).

**Outcome.** Encoded as `desks.classify[0]` external patterns; resolution is
by filing address against 335 Pioneer Way in every case. Two pattern errors
were caught by that test on 2026-09-06 and are recorded because they are the
rule proving itself: `YC Allocate AF26 AI/QP` were name-matched IN and are
external; `YCP24, L.P.` and `YCP26, L.P.` were name-matched OUT and file
from 335 Pioneer Way, so they are YC's own.

EDGAR full-text is kept entity-qualified for the same reason: bare
"Y Combinator" matches 1,008 filings, almost all of them portfolio
companies naming their accelerator — which is exactly what the exit-side
sweep wants, and useless as an own-entity pattern.

---

## Part 2 — Deltas (Erik's, before verdicts write)

*Recorded here as the run finds them; each is argued, not assumed.*

---

## Part 3 — Run-time standing rulings

### R1 (2026-09-06). The public directory is a floor, not the portfolio

**Finding.** The directory's Algolia index is tag-filtered to `ycdc_public`
and returns 6,203 companies. It is not the whole funded book: the archived
`/companies/` namespace carries slugs that 404 on the live site today, and
the first (alphabetically truncated) pass alone recovered 20 of them —
Accredible, AdmitSee, Affix API, AllCanCode, Metadata and fifteen numeric-id
pages resolving to Convictional, Encellin, Business Score, Gold Fig Labs,
Gmelius, Wallarm, LabGrid, Reach.Live, StudyRoom, Chesscademy, Callisto,
Minimall, Blotout and two more. **Ruling.** A capture-evidenced
`/companies/<slug>` page is `site_listing`-class membership evidence
whatever the live index says, exactly as an archived listing is for every
other investor (§1 evidence sufficiency: "a listing on the investor's own
site (any era)"). The report states the directory's own coverage caveat.

### R2 (2026-09-06). A company name is not an identity here

**Finding.** 89 names in the directory are borne by two different companies
in different batches (Parse S11, the Facebook-acquired backend, vs Parse
F25; Struct W23 vs Struct F24), all with distinct YC ids. **Ruling.** The
row's identity is YC's own company id. Encoded as `site_api.key_field` and
the base build's opt-in `site_id`; both landed as pipeline changes rather
than local fixes.

### R3 (2026-09-06). YC's numeric company-id URLs are the same row

**Finding.** The 2020–21 directory served `/companies/<numeric id>` and the
live site 301s that form to the slug (`/companies/531` → `/companies/doordash`).
The CDX layer therefore built an id-named row beside every directory row it
already had. **Ruling.** Resolved as identity merges (890 rows), not as
members; the redirect is the resolver, and a 404 instead of a 301 is what
separates a delisting (R1) from a duplicate. Slug-history 301s to a
*different* name are renames and merge the same way (1build → Handoff,
Adra → Adravision).

### R4 (2026-09-06). The directory's own fields are evidence, not labels

`status` (Active 4,293 / Inactive 1,072 / Acquired 815 / Public 23) and
`stage` (Early 5,114 / Growth 1,089) are scored on the golden set before
either is trusted (§4). `stage` in particular is a two-value field
describing the company today, not the round YC entered at, so it cannot be
an `entry_stage` label whatever it scores; it is recorded as corroboration.
"Inactive" is **not** identical to `defunct` and the mapping is measured,
not assumed.

### D6. Nonprofits are OUT (T3 and T5, same answer)

**Facts.** YC has run nonprofits through its batches since 2013. They receive
a **grant**, not an equity investment: "Nonprofits get $100k of funding and go
through the standard YC program, participating side by side with for-profits"
(YC blog, 2017-09-29, via the Internet Archive; the live URL 404s). YC's
current nonprofits page states only that it works with 2–4 nonprofits per
batch and "more than 30 companies so far"; the directory's own `nonprofit`
flag marks **42** rows, so YC's two published numbers disagree and the
directory is the higher one. The current grant amount is not published
anywhere and is recorded as unverified.

**Tests.** T3 (venture entry) and T5 (venture-outcome operating company).
**Outcome: OUT, and both tests agree** — a grant is not a round, no equity is
issued, so there is no entry stage, no valuation, no exit and no C2A cohort
membership; and a nonprofit is not a venture-outcome operating company. The
42 flagged rows leave the published base into `excluded.json`.
**Not a delta**: no test is stretched and none collide.

### D7. The directory lists *launched* companies, not funded ones

**Facts.** YC's own directory says so in its result count: filtering to the
current batch renders "Showing 40 of 235 **launched** companies — more will be
added as Summer 2026 launches!" Companies are also removed after the fact
(YC parted ways with Delve in April 2026 and its company page came down).
The directory's prose still reads "over 5,000 companies" while the index
returns 6,203, so the prose is stale rather than contradicted.

**Outcome.** The count is *publicly listed launched companies as of
2026-09-06*. It excludes unlaunched and stealth companies in in-flight
batches and any company whose page has been pulled. This is the evidential
basis for R1 (the directory is a floor) and it is stated in the report as the
layer's coverage caveat, not hidden.

### D8. Adviser registration: one ERA, no RIA, no separate Continuity adviser

**Facts.** `Y COMBINATOR MANAGEMENT, LLC` (business name "Y Combinator"),
**CRD 171730**, SEC file 802-80528, **exempt reporting adviser** — ERA-Active
with the SEC since 2014-10-23 and with California since 2018-04-19; not SEC-
or state-registered as an RIA. Latest annual amendment 2026-03-27, filed from
335 Pioneer Way. An ERA files no Item 5.F, so there is no regulatory AUM;
**Section 7.B reports 19 private funds at $21,962,163,829 gross**, which is
the sworn AUM anchor (§11: for an ERA, 7.B is the substitute and both range
ends are the composite). IAPD returns no "YC Continuity" or "Y Combinator
Continuity" adviser at all, and Continuity Fund I is reported under this same
ADV.

**Test.** T1. **Outcome.** One adviser covers the whole firm, so there is no
brand-sharing entity to exclude and no desk partition — the D1 derivation is
confirmed by registration and not only by address.

**Four vehicles appear in the ADV but nowhere in EDGAR**, so the Form D sweep
alone would have missed them and the profile's fund table takes them from the
ADV: `Y Combinator Fund I, LP` ($672.0M), `Y Combinator Fund II, LP`
($295.9M), `YCVC Fund I, L.P.` ($536.3M), `YCVC W14, LLC` ($22.5M).

---

## Part 4 — Calibration gate results (2026-09-06, before any verdict wrote)

Both sets pre-registered in `golden.json` first. §4 requires scoring every
candidate evidence layer, not only the judge, and the four scores below set
the evidence order the grind uses.

### Layer: the directory's own `stage` field — **REFUSED** (4/29)

Its vocabulary is two values, `Early` (5,114) and `Growth` (1,089), and it
describes the company **today**, not the round YC entered at. Mapped as
generously as possible (`Early`→Seed, `Growth`→Growth) it scores 4 of 29 and
misses in exactly the way that matters: `Growth` for Checkr, DoorDash,
Ginkgo, Razorpay, Podium, Lob, Whatnot, RevenueCat, Zepto, Webflow, Airbnb,
Dropbox and Stripe — every one a batch entry the field reads as a later
round. That is the entry-versus-participation error the golden set was built
to catch, and it is worse in kind than Thrive's job-board stage field (0/10,
refused). **Never an `entry_stage` label; carried as evidence only.**

### Layer: the batch record — **PROMOTED to class 1** (31/31)

`batch present → Seed`, `batch == "ycc_only" → Growth`, cited to YC's own
deal terms for the era (recorded in `golden.json._batch_deal_eras`). Perfect
on all four classes: 2/2 on the two rows where the label itself
discriminates, 11/11 against publicised Continuity distractors, 8/8 against
famous Series A distractors, 10/10 on controls.

**A YC batch entry is `Seed`, never `Pre-Seed`.** First-party basis: YC's own
about page, sustained from at least 2009 to 2020 — "Y Combinator provides
seed funding for startups. Seed funding is the earliest stage of venture
funding." The 2005–2007 cheques ($6,000 per founder, capped near $20,000)
tempt a Pre-Seed answer, but YC's contemporaneous language calls it seed and
the term did not then exist. **`Pre-Seed` and `Series A` are structurally
empty for this investor**: Continuity's mandate was pro rata and later-stage
growth, so it never led a Series A.

**The gate caught a live trap in its own scoring.** The rule first scored
30/31, the single miss being Convoy — because the lookup resolved the name
"Convoy" to the directory's `convoy-2` (Winter 2022, London/Nigeria) rather
than to `convoy` (id 11874, Seattle, the digital-freight company tagged
`ycc_only`). Re-scored with site_id identity it is 31/31. R2's name-collision
problem therefore bites the **judge**, not only the base build: every grind
lookup keys on YC's id, never on the name.

### Layer: the directory's `status` field — **corroboration only** (67.5%)

Scored against the 767 rows already judged in landed bases: 518 agree, 249
disagree. The mapping that fails is the dead-and-exited tail, exactly where
the column matters: `Inactive` lands as `private` 41 times and `unknown` 28
times against only 27 `defunct`, so **"Inactive" is emphatically not
`defunct`** (Phase 0 ruling 5, now measured rather than assumed). `Acquired`
reads `private` 36 times and `defunct` 20; the site is also stale in the
other direction, reading `Active` for 35 acquired and 21 defunct companies.
Only `Active → private` (386) is dependable. **Never a label**; the base
overrides it with the cited event, as §6 requires.

### Layer: `all_locations` — country **class 2**, city **normalize first**

`hq_country` agrees with landed bases on 616/730 (84.4%), and part of the
residue is name-collision noise on the *landed* side rather than directory
error (a French "Angle" against YC's Angle Health, a Czech "RADAR" against
YC's RADAR). `hq_city` agrees on only 273/544 (50.2%), but the largest single
cause is shape, not fact — "New York City" against the §6 rule's bare
municipality "New York". City is normalized to the §6 shape before use and
the judge overrides on conflict; neither field publishes without that check.

---

## Part 3 (continued) — rulings made during the grind and close

### R5 (2026-09-07). Acquired-then-shut-down is `acquired`

My own grind contract had said "Acquired -> acquired unless the company later
shut down", which contradicts §6: `defunct` is reserved for businesses that
ended *without* an acquisition, and an acquirer retiring the product does not
undo the exit (Chariot/Ford, Hipmunk/SAP Concur). Contract corrected; only the
two rows judged here under the wrong clause were flipped. Twenty rows reading
`defunct` against a directory `Acquired` came from landed bases and are bound
by invariant 10, so they were left alone. **Open for Erik**: Coin (Fitbit took
platform and team, card business died) and Cymmetria (Stage Fund bought it,
then wound it down) sit on the same asset-sale-versus-wind-down line as
Airware, which reads `defunct` because no buyer took the business.

### R6 (2026-09-07). The unicorn snapshot never bands a row here (Rule A)

`verify.unicorn_bands: false`. The pipeline banded rows off a unicorn-list
name match on every `prepare`; it had put Cohere's $6.8B on a Summer 2020
company the directory marks Acquired. Every $1B+ row now rests on a priced
event with a citable figure; the six carried in from landed bases on the
snapshot were re-cited from their rounds (Fivetran, Relativity Space,
SmartAsset, Substack, Flutterwave, Astranis).

### R7 (2026-09-07). C2A is withheld, not published at 100%

`verify.c2a_deterministic: false`. Cohort 5,041, deterministically verified
13 (0.26%). See report §4. The column ships uniformly null with
`cohort_unverified` on every cohort row.

### R8 (2026-09-07). Imported values are checked against a date the row knows

An event dated before the company's own batch cannot be the company's. Five
cross-investor imports failed that test (Guild Education's $4.4B on a Summer
2026 row, the identity-verification Alloy's $1.55B on a Winter 2023 row) and
none of them had surfaced as a disagreement, because nothing on the other
side contradicted them. Applied to every `cross_investor_bound` row.

### R9 (2026-09-07). Weak CIK joins are quarantined unless the directory says Public

84 rows had a public float from a same-named registrant (Dover Corp $25B,
Parametric $18.5B, Iliad SA, Lucid, Plexus, Mosaic Co). Every one was already
flagged `cik_weak`. Quarantined under §8 duty 8; only `gitlab` and `oklo`
kept theirs, both `Public` in YC's own directory.

### R10 (2026-09-07). Membership of OpenAI — raised, not decided here

The Internet Archive holds a full YC company page for OpenAI, so under §1 a
site listing in any era suffices and the row is a member; my golden trap set
had said the opposite on the strength of a live 404 and was corrected. Whether
YC's own listing settles it against a 2015 funding round that came from
individuals rather than a YC fund is a boundary question for Erik. At $852B
it is the largest row in the dataset.

### R11 (2026-09-15). Wave alignment is recorded, not accepted away

140 cross-investor pairs are in `cross-rulings.json` under `accepted`, each
reason naming which side is stale and that the entry is to be DELETED at the
wave alignment once the other investor's row is updated. A collection session
may not edit another investor's directory (§12). 96 pairs are ruled
`distinct`, mostly one-word collisions.

### R12 (2026-09-15). The PRO-109 ledger rename

The tooling session renamed the ledger to `membership-ledger.json` while this
run was in flight and YC's file was not migrated; a later `record` created a
fresh, near-empty ledger and one rebuild ran against it. Merged
authoritatively from the orphaned `base-verification.json`, which is retired
in the closing commit. No other investor was affected.

### R10 resolved (Erik, 2026-09-16). OpenAI is OUT. A confirmed delta

Erik: "If OpenAI did not receive investment from a YC entity, keep out." It
did not. The 2015 funders were Altman, Brockman, Musk, Livingston, Thiel, AWS,
Infosys and YC Research (TechCrunch, 2015-12-11), as contributions to a
non-profit; YC Research was a non-profit lab Altman jump-started with $10M of
his own money, "not ... with the goal of helping YC's startups succeed or
adding to our bottom line" (YC's own post), and it is none of YC's 20 fund
vehicles nor any of the 19 funds in the ADV. No YC fund appears in any later
OpenAI round. Verdict `not_member`, `who: erik`.

**The delta to ratchet** (COLLECTION.md 1, T2 precedents, for the tooling
session): *a listing on the firm's own site that reflects affiliation rather
than fund money does not carry membership.* The site-listing sufficiency rule
assumes the listing records an investment; where the firm lists a company it
is affiliated with through a person or a related non-profit, T2 governs and
the row needs fund money to be a member. First instance: YC's archived company
page for OpenAI.
