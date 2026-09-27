# Coatue: investor-specific decisions

Investor-specific rulings for `coatue`, derived from the standing rule set in
`data/collection/COLLECTION.md` §1 (T1 to T5) rather than re-asking it.
Linear issue **PRO-78** (Phase 2, layer-building: the public-market evidence
family), sibling of the PRO-87 wave.

Structure per §1's derivation protocol: **derivations** apply without
confirmation (Erik may veto any); **deltas** are Erik's to confirm; **run-time
standing rulings** are dated, class-wide and flagged for review. Facts marked
*(verified 2026-09-26)* were read from the filing or page named; anything
marked *provisional* is re-derived from verified facts during the run.

---

## Derivations (T1 to T5 applied to verified facts; vetoable)

- **D1 — One registered adviser, one firm (T1, same adviser) → IN.**
  *(verified 2026-09-26, IAPD and the ADV)* Coatue Management, L.L.C. is the
  one SEC-registered adviser (CRD 157910, SEC 801-73669), principal office
  9 West 57th Street, 25th Floor, New York; other advisory offices in Menlo
  Park (2885 Sand Hill Road, 13 advisory staff), San Francisco (21 South Park
  Street, 13) and Hong Kong (Two IFC, 3). Its 2026-07-29 amendment reports
  RAUM **$92,705,722,582** across 127 accounts and 144 private funds in
  Section 7.B.(1) with **$126.9B** of gross assets (feeders included), all
  under general partners it controls (`sources/registers/adv-157910.json`).
  No relying adviser, no umbrella. IAPD by name returns only this firm.
  EDGAR's 160 "Coatue" CIKs are all the firm's own vehicles or third-party
  feeders into them: no namesake exists.

- **D2 — Two strategy families under one adviser (T1, strategy desks).**
  *(verified 2026-09-26, Form D fund types and the ADV fund list)* The
  adviser runs public-markets strategies (the flagship long/short Coatue
  Qualified Partners / Coatue Offshore Fund and their master, $31.0B; Long
  Only, $11.1B master; Quant; Strategic Maple; Select; Crown; Cardinal; F1;
  SC V) beside a private-markets ladder (Coatue Private Fund I 2013 and II
  2015, Kona III 2017, Growth Fund IV 2019, V 2021, V-B 2023 and VI 2026,
  Early Stage Fund 2018, Ventures II 2021 and III 2022, Opportunity I 2020
  and II 2024, Structured Fund 2022, Tactical Solutions 2022, the thematic
  Climate Tech II, FinTech I, Smart Transportation I and Asia funds, and
  about 130 numbered single-deal co-investment vehicles, Coatue CT nn LLC /
  LP, Coatue US nn LLC and Coatue (Cayman) nn LLC, under Coatue Capital CI).
  Under §1's strategy addendum the public-markets funds are the `public`
  desk and every private-markets vehicle is the home desk `us`
  (`config.desks`). **The partition is applied at the vehicle level only**
  (the profile's AUM and fund table), because at the row level it cannot be:
  the adviser files one Schedule 13G for all its funds at once, so a filing
  never says whether the flagship or a growth fund holds the shares. Rows
  are decided by T3 (D3), and the base's `partition` is empty on purpose.
  The thematic funds (Climate Tech II, FinTech I, Smart Transportation I,
  Asia) file Form D typed "Hedge Fund" although they invest in private
  companies; they sit on the home desk and their public buys are ruled out
  row by row under D3.

  **The profile's `aum` is the venture desk's floor, never the umbrella
  RAUM** (§1 strategy desks): the sum of the private-markets vehicles'
  Section 7.B gross asset values, master funds only, labelled a floor, with
  the $92.7B RAUM in the basis.

- **D3 — A 13F, 13G or N-PORT line is a public-market holding, not a
  venture entry (T3).** This is the ruling PRO-78 asks for up front, re-ruled
  here for a firm where 13F is a primary source rather than noise. It
  **survives contact unchanged**: the standing rule (a position that first
  appears as a 13F holding or a post-IPO 13G, never through a venture round,
  is `not_member`) is exactly the crossover boundary. What changes is the
  *use* of the layer: the 13F is (a) a public-status corroboration for a
  member (a 13F line is by definition an exchange-traded security), (b) a
  first-public-quarter date, and (c) the recall trigger for the crossover
  blind spot: a 13F issuer whose listing postdates 2013 (when Coatue's
  private investing began) is **checked** for a pre-IPO round, and admitted
  only on that round's citation. The largest 13F positions with no venture
  round (Taiwan Semiconductor, Lam Research, Micron, Applied Materials, GE
  Vernova, Amazon, Broadcom, Eaton, Alphabet, Intel, Meta, Equinix, Nvidia,
  Constellation, Microsoft, ASML, Netflix, Qualcomm, AMD, Intuitive Surgical)
  are membership traps in `config.verify.not_members`. **A 13F-only or
  13G-only row leaves the base as `not_member`, never as `other_desk`:** the
  desk of the holding vehicle is unknowable from the filing (D2), and the
  test that decides the row is the entry, not the desk. Where the site lists
  a company the 13F also carries (Spotify, Reddit, Snap, DoorDash, Uber,
  Snowflake), the site listing is the membership evidence and the 13F only
  corroborates `public`.

- **D4 — The registered CTEK fund is a home-desk vehicle; its restricted
  positions are venture entries, its listed positions are not (T1, T3).**
  *(verified 2026-09-26, N-PORT 2026-06-30 and N-CSR 2025-12-31)* Coatue
  Innovative Strategies Fund (CIK 2044519, formerly Coatue Innovation Fund /
  Coatue CTEK Fund; a non-diversified closed-end tender-offer fund that
  began trading 2025-05-12; $9.5B net assets at 2026-06-30) is advised by
  the same adviser and holds both: 19 restricted private positions (Revolut,
  Anthropic, Stripe, OpenAI, Kalshi and others, Level 3, held through
  wholly-owned Coatue US nnn LLC subsidiaries) beside a listed book (Micron,
  Kioxia, Samsung, Amazon, TSMC). A restricted position is a purchase of a
  private company's stock by a fund of the firm (T2 fund money; a primary or
  a secondary, so Growth by the policy constant where the round is not
  named) and is membership evidence of class `fund_filing`, citing the
  N-PORT or N-CSR; a listed position is T3's public purchase and is out.
  **The N-PORT fair value is a mark, not a priced event**: it goes to the
  note under Rule A and never bands a row (X3 asks Erik to confirm).
  *(amended 2026-09-27)* **How the evidence reaches the base.** The builder
  forms a filing link from a row's own CIK, and an N-PORT is filed under the
  fund's CIK, so a company row cannot carry the form without failing
  `verify` (no link) or, given the fund's CIK, reading as one registrant
  eleven times. A company the firm lists keeps its listing as membership
  evidence and cites the N-PORT in its note; a company on no list (Kalshi)
  enters as a ledger recall addition citing the N-PORT, verdict class
  `fund_filing`. A builder change is proposed in the report.

- **D5 — Single-deal co-investment vehicles are vehicles, not rows (T5,
  T1).** *(verified 2026-09-26, Form D)* Coatue CT nn LLC / LP, Coatue US nn
  LLC and Coatue (Cayman) nn LLC are pooled "Private Equity Fund" issuers
  with Coatue Capital CI, LLC / LP as managing member and the adviser as
  investment manager; their Form Ds name no target. T1's lettered-vehicle
  default: IN as the firm's own vehicles, and a company they hold enters
  the base on the evidence that names the company (a 13G naming the LLC as
  a joint filer, an N-CSR footnote "held by Coatue US 119 LLC", a
  prospectus holder table), at the stage of that entry. They are never rows
  and never `first_seen` anchors on their own.

- **D6 — Fund money (T2).** Philippe Laffont's personal vehicles (Green Ox
  Farm Holdings LLC on the ADV; Coatue CT XXIII LLC, whose general partner
  is Laffont personally rather than Coatue Capital CI, is checked in the
  run) are not fund money. Third-party feeders (BBH Wealth Strategies'
  Coatue sub-trust and series, PB Coatue Private Fund Feeders, EPQ LLC /
  Coatue V PS, the iCapital access fund) are `external` and hold no
  positions of their own. Coatue runs no scout programme or accelerator;
  the East Meets West conference and the "Fantastic 40" index are lists of
  companies, not positions (D12).

- **D7 — Venture entry (T3).** Coatue's private-markets entries are
  primaries and secondaries (tenders and structured instruments included);
  secondaries and tenders are Growth entries (policy constant). Coatue makes
  minority investments only, so the control addendum is not expected to
  fire; a row that turns out to be a control transaction is judged on the
  addendum's test. A structured instrument (Tactical Solutions / Structured
  Fund: convertible or preferred with downside protection into a private
  company) is a financing of the company and a venture entry at Growth;
  the same instrument into a listed company is a public purchase, out.

- **D8 — Person or firm (T4).** Standard: person-level Section 16 filings
  locate a person; a seat is dated against the person's firm at filing time.
  Coatue's investing partners take board seats rarely, so the roster-name
  Form D sweep is expected to carry little recall here (PRO-78's own
  framing); what it returns is judged cluster-first as usual.

- **D9 — The archive layer starts on Common Crawl and the Wayback pull
  lands after the cooldown (§5, outage rule).** *(verified 2026-09-26)* The
  Internet Archive was in a four-hour machine-wide cooldown at kickoff
  (`shared_throttle` ia.cooldown, after two blocks earned earlier that day).
  coatue.com was a single page until 2023 (Common Crawl 2014 to 2021 holds
  only `/` and `/privacy.html`); `/portfolio` exists from 2023. The archive
  can therefore date listings 2023 to 2026 only; the pre-2023 book rests on
  the live site's "Exit" rows, the filings and press.

- **D10 — The roster is curated, not crawled.** coatue.com publishes no
  team page. The roster is built the Thrive way: the natural persons on the
  firm's own fund Form Ds 2009 to 2026 (Laffont, Bowring, Woolaver, Sacks,
  Lang), the ADV owners, the CTEK prospectus officers, the firm's own
  welcome and leadership posts (Viswanath 2022, Urquhart 2022, Lai and
  Gerson 2023, Bryant 2023, O'Boyle and von Marcard 2024, the 2024-11
  leadership update, Wallace 2025), and press-dated windows for the
  investing partners, one basis line per person.

- **D11 — The site's "Initial investment" field labels Growth and anchors
  Venture (§5 eligibility, §6 class 1b).** The `/portfolio` grid's own
  filter is headed "Initial investment" (Venture | Growth): it is the firm's
  claim about the round it entered, so it is eligible. `Growth` collapses
  onto one taxonomy stage and labels (confidence medium until scored);
  `Venture` straddles Seed and Series A and is an anchor only. The grid's
  "Active | Exit" is the FIRM's position status, not the company's: an
  "Exit" row may be public, acquired, private (a secondary sale) or defunct,
  and the judge decides `status` from the company's own evidence.

- **D12 — Operating company (T5).** Standard. "Fantastic 40" (the firm's
  index of private companies it follows) and the East Meets West speaker
  lists are not portfolio lists and seed nothing.

---

## Deltas (Erik's to confirm; the run proceeds on them, flagged)

- **X1 — WITHDRAWN 2026-09-27: the shape guard on the $1B+ share no longer
  exists.** Written before the grind as a restated ceiling of 0.60. The
  playbook has since removed the ceiling altogether (COLLECTION.md 8, Erik
  2026-09-26: a growth or crossover book can sit at any share, the share is
  stated in the report and never gated), so `one_b_share_max` is gone from
  this investor's config and nothing is left to confirm. Measured at close:
  the share is in the report. `c2a_rate_max` keeps the 0.80 default.

- **X2 — `entry_stage` needs no crossover vocabulary; the leaderboard needs
  a cohort floor.** PRO-78 asks whether the column needs a crossover ruling
  rather than a shape-guard exception. Answer proposed: **no new stage.**
  Growth already means "Series B and everything later, secondaries and
  tenders included", which is every Coatue entry that is not a Venture one,
  and a Late Stage label would split one fact (a later-round entry) by check
  size, which §6 forbids. What the crossover shape breaks is not the column
  but the comparison: an S2A rate on a cohort of a dozen Seed rows is not
  comparable to Point Nine's on 145, so the leaderboard should display the
  rate only above a cohort floor (or show the cohort beside it), which is a
  display rule for PRO-54's surface, not a collection ruling. Erik decides.

- **X3 — A registered fund's audited fair value never bands a row.**
  Proposed under Rule A: the CTEK N-PORT / N-CSR fair values (Level 3,
  audited) are the strongest marks any run has seen for a private company
  and still estimates, not priced events. They go to the note with the
  filing cited; a $1B+ band still needs a priced round, tender or public
  float. If Erik prefers to admit them, the source gate needs a new
  `valuation_source` value (`registered_fund_fair_value`) and this run will
  add it; until then the rows carry `needs_web_value`.

- **X4 — PRO-78's premise that public rows get a better valuation source
  from this family is not borne out.** Neither a 13F line (a position
  value) nor an N-PORT line (a fair value) carries a market capitalisation.
  Public rows are still pinned by a web-cited market cap with the SEC float
  as corroboration; verify invariant 2 needs no new source. Reported as a
  finding, not a change.

---

## Run-time standing rulings

(dated, class-wide, flagged for review)

- **R1 — A position entered at or after the listing is not a member (T3),
  2026-09-26.** Hut 8 (a convertible investment in a listed company) is out
  on the Omniture precedent although the firm's page lists it; Endeavor is
  kept and flagged `boundary` because the firm's entry predates the 2021
  listing in the record. **Extended 2026-09-27 to PIPE shares bought at a
  SPAC merger** (SoFi, Payoneer, Sunlight Financial, CCC Intelligent
  Solutions; Apex Fintech's PIPE never closed in the filings): the shares
  are bought at the listing, no private round names the firm, so the recall
  probe rejected all five. Erik decides whether a PIPE at a merger counts as
  a venture entry; if it does, four rows enter as Growth.

- **R2 — A director of record on a Form D, with the firm silent, is a
  member flagged `boundary`, 2026-09-26.** Pill Club, Sungage Financial and
  Fire Pit Collective each name a Coatue partner as director inside that
  partner's tenure and appear on no page of the firm. (Nomos AI, first read
  the same way, is the registered name of Norm Ai, which the firm lists;
  merged 2026-09-27.) T4's default reads a
  seat inside the tenure as the firm's; for a golf media company (Fire Pit
  Collective, Thomas Laffont) a personal holding is at least as likely.
  Erik decides per row.

- **R3 — A signed, unclosed acquisition is a mark, not a status,
  2026-09-26.** Airtable ($2.25B) and Hugging Face ($12.93B) stay private
  at the agreed price until the deal closes.

- **R4 — Equity raised is a floor, not a valuation, 2026-09-27.** DayOne
  ($4.5B) and Vantage Data Centers ($9.2B) carry the equity raised in one
  round as a floor under the valuation because no page states the
  valuation itself. Both are flagged `needs_review`; Erik decides whether
  a floor may band a row.

- **R5 — The absence test owes one web search per row and a name scan of
  the Form D data for single-deal vehicles, 2026-09-27.** The four standard
  surfaces missed three later rounds in a cohort of twenty (Meticulous,
  Stability AI, WisdomAI). A vehicle named "Meticulous Sept 2025" in the
  Form D data exposed the first; one web search per row found the other
  two. Every no in this book now carries both lines.

- **R6 — The company's own head office statement wins over the press,
  2026-09-27.** Firmus reads Sydney (its own releases) against Singapore
  and Launceston in the press; Scala reads Barueri (its own contact page)
  against São Paulo. Rapyd reads London on two press pages although the
  company was founded in Tel Aviv and publishes no head office line.

- **R7 — A company that renamed itself keeps its row and its slug,
  2026-09-27.** Tome now trades as Lightfield and raised a Series A under
  the new name; the row stays `tome` until the firm's page changes the
  name, with the new name in the note.
