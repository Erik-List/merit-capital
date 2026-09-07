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
