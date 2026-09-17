# First Round Capital — investor-specific decisions

Derived from the standing rule set in `data/collection/COLLECTION.md` §1 under
the derivation protocol: one line per category, each naming the test applied,
the verified facts, the outcome and the precedent. Derivations need no
confirmation; deltas do; run-time standing rulings are dated and flagged.

Linear: PRO-93 (sub-issue of PRO-87, archetype A). Run started 2026-09-06.

## The firm, in verified facts

| Fact | Value | Source |
|---|---|---|
| Adviser | **FR CAPITAL HOLDINGS, LP** — CRD 160848, SEC# 802-75765 | SEC IA firm roster (exempt), 2026-09-01 feed |
| Registration | Exempt reporting adviser since 2012-03-30; ADV annual amendment filed 2026-03-31 | ADV Item 1, CRD 160848 |
| Private funds | 22, **all venture capital funds**, gross assets **$3,843,440,251** | ADV Item 7.B / SEC roster feed |
| Fund names in the ADV | **Anonymised** under rule 204-2(d) ("FUND 006" … "FUND 030", GPs as "GP 004") | ADV Schedule D §7.B(1) |
| GP entities (ADV §7.A related persons) | First Round Capital Management **II, III, IV, V, VI, VII, VIII, VIII-F, IX, X** LP — eleven, and nothing else | ADV Schedule D §7.A |
| Offices | Philadelphia (principal, 2400 Market St Suite 237), New York (165 Mercer St), one further office | ADV Item 1.F |
| Brand | The adviser files under "FR Capital Holdings, LP"; **no adviser named "First Round" exists** in either SEC roster (registered or exempt), which is why IAPD's name search finds nothing | SEC registered + exempt firm rosters, 2026-09-01 |

The eleven GP entities and the 22 funds reconcile: II, II-A, III, III-A,
III Partners, IV, IV Partners, V, V Partners, VI, VI Partners, VII, VII
Partners, VIII, VIII Partners, VIII-F, VIII-F Partners, IX, IX Partners, X,
X Partners, X-F Partners = 22. **The count leaves no room for a fund outside
the First Round ladder**, which is what decides D1 below.

## Derivations

- **D-T1a — the fund ladder is one adviser, one desk.** Facts: every First
  Round vehicle on EDGAR (2005, 2006, 2006 Annex, 2007, 2007 Annex, II, II-A,
  III … X, each with its matching Partners Fund and the -A / -F sleeves)
  files from the firm's own Philadelphia address, and the ADV's §7.A related
  persons are exactly the First Round Capital Management II–X GPs. Test: T1.
  Outcome: **IN** for every fund, sleeve, Partners Fund and office; one desk
  (`us`), no partition. Precedent: a16z's fund families, LSVP's offices under
  one CRD.
- **D-T1b — no brand-sharing entity exists.** Facts: the SEC's own registered
  and exempt adviser rosters (2026-09-01) carry no "First Round" adviser
  besides CRD 160848, and the ADV names no affiliated adviser. Test: T1's
  standing check (PRO-87 requires it per firm rather than assuming it).
  Outcome: no Accel-KKR / Meritech / Lightspeed-India case here. The one
  EDGAR namesake, **First Round CSWR, LLC** (CIK 1600720, Missouri), is
  `external` in `desks.classify`.
- **D-T1c — no non-venture strategy desk.** Facts: all 22 ADV funds are
  reported as venture capital funds; the adviser reports no other strategy.
  Test: T1's strategy-desk addendum (Erik, 2026-09-04). Outcome: not reached;
  no `other_desk` partition.
- **D-T2a — pre-fund investments are OUT.** Facts: the firm's own site
  published `/our_portfolio_prior.html` (2006–2008) under the heading "The
  following investments were made prior to First Round Capital" —
  del.icio.us, Engage.com, Feedster, Flock, IronPort and the rest of Josh
  Kopelman's and Howard Morgan's angel book. Test: T2 (fund money). Outcome:
  **OUT**; the page is an *exclusion* list, not a listing surface, and is
  deliberately not configured as a wayback era. Precedent: Kushner's personal
  angel book (a16z), Cherry's founder-angel positions. Consequence for the
  recall probe: parametric enumeration will offer del.icio.us and IronPort as
  First Round deals — they are rejections with this reason, not misses.
- **D-T2b — programs and community vehicles are OUT unless a fund held the
  position.** Facts: Angel Track is a training programme for angel investors
  who deploy their own money; First Round publishes no fund behind it. Test:
  T2. Outcome: **OUT**, with the scout precedent (Sequoia, a16z, Accel,
  Lightspeed). A company reached only through such a programme is
  `not_member`; a company the firm also lists or a First Round fund also
  funded is a member on that evidence.
- **D-T3 — venture entry, seed-first.** Facts: First Round enters at
  pre-seed, seed and occasionally Series A and follows on inside its funds;
  it runs no buyout practice and files no 13F. Test: T3. Outcome: standard —
  primaries, follow-ons, secondaries and tenders IN; positions first
  appearing as public-market purchases or post-IPO 13Gs OUT. The control
  addendum binds but is not expected to fire.
- **D-T4 — person-level attribution and seat dating** apply unchanged. The
  roster is unusually mobile on the way out (Charlie O'Donnell → Brooklyn
  Bridge Ventures, Kent Goldman → Upside Partnership, Christine Herron →
  Intel Capital, Phin Barnes → Uncork), so the tenure windows carry real
  weight in the Form D sweep.
- **D-T5 — operating company** test applies unchanged; fund-shaped list
  entries, tokens without an issuing organisation, filter labels and scrape
  artifacts are not rows. This investor adds one artifact class of its own:
  the 2010–2011 logo era publishes names only as image filenames
  (`backupifysmall.jpg`, `attribute.jpg`), so slug-only rows from that era are
  identity-resolved in the grind and dropped as artifacts where they cannot
  be resolved.

## Deltas

**D1 — Dorm Room Fund is OUT (external), on T1 rather than on the scout
precedent.** PRO-93 predicted OUT "per the scout ruling already made four
times". The scout ruling is about individuals' cheques with no fund; Dorm
Room Fund IV, LP and Dorm Room Fund V LP are real funds that file Form D
(DRF IV sold $10.375M by 2022). So the prior's *reasoning* does not reach
them and the case is re-derived from verified facts under T1:

- DRF IV/V name **Dorm Room Fund GP, LLC** / **Dorm Room Fund V GP LLC** and
  **Dorm Room Management Company, LLC** as their related persons — not any
  First Round entity, and not Josh Kopelman.
- Neither entity appears anywhere in FR Capital Holdings' ADV: not in §7.A's
  eleven related persons, not in Item 1.B, nowhere in the 119-page filing.
- The adviser's 22 private funds reconcile exactly to the First Round II–X
  ladder, leaving no slot for a Dorm Room vehicle.

Outcome: **OUT**, same verdict as the issue predicted, reached under T1 (own
adviser, own fund family, own operation) with filing-grade evidence rather
than by analogy. A company reached only through a Dorm Room Fund filing is
`not_member`; a company First Round's own funds or listings also carry is a
member on that evidence, and the DRF connection is a note, not a verdict.
Recorded as a delta rather than a derivation because it overturns the
reasoning the issue carried, and because it is the one boundary a reader of
the published base is most likely to question.

**D2 — the base is sliced to venture activity and says so.** Not applicable
in the control-position sense (no buyout practice), but the same disclosure
rule applies to D-T2a: the published track record excludes the founders'
pre-fund angel book, and the report says so, because several of the
best-known names associated with Josh Kopelman personally (del.icio.us,
IronPort) are not First Round positions.

## Run-time standing rulings

_(dated, class-wide, flagged for review)_

- **2026-09-06 — the shape guards fire low on $1B+ share and high on C2A, and
  that is the correct reading.** A seed-only firm with roughly a thousand
  first cheques since 2005 mechanically produces a low unicorn *share* (the
  denominator is every seed cheque) and a high seed-to-A graduation rate among
  the entries whose record can be established. `verify.shape` keeps the 20% /
  80% defaults; a firing guard is restated here against the evidence rather
  than waived, per §8 lesson 5.

- **2026-09-06 — the firm's own `initialPartnership` label is a floor, never a
  label.** Scored 12/18 on the pre-registered stage golden set, with all six
  misses understating by exactly one step and none overstating
  (`scratch/gate.md`). It may not publish a stage on its own; it is affirmative
  evidence the entry was at least what it says; and where an independent source
  names a later round, the record wins with `stage_disputes_band`.
- **2026-09-06 — Wikidata is corroboration for this investor, never a label.**
  89 of the 104 rows it filled have single-token names and the joins are wrong
  at scale (Uber→NL, Square→JP, Clay→NL, Planet→GR). Every Wikidata-sourced
  `hq_country` and `status` was re-judged; 49 rows carry `model_disputes_source`.
- **2026-09-06 — Howard Morgan's First Round tenure ends 2016, not 2012.** His
  last fund Form D is 2012, but the firm's own listings carry Augury (2014) and
  Kentik (2016) as his deals. The seat-dating boundary for his cluster is the
  site captures; rows from 2020 on are post-tenure and excluded.
- **2026-09-06 — the `/team/<First_Last>` namespace is a portfolio-founder
  directory, not the roster.** Excluded from the Form D sweep (it would confirm
  hundreds of false members) and used instead as a recall layer.
- **2026-09-06 — the 2010-2011 logo wall's acquirer marks are not positions.**
  Google, Microsoft, Intuit, Adobe, eBay and Facebook appear on the page beside
  the exits they bought; they are `rejects`, not members.
