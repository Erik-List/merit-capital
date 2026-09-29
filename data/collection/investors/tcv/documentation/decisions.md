# TCV: investor-specific decisions

Investor-specific rulings for `tcv`, derived from the standing rule set in
`data/collection/COLLECTION.md` §1 (T1 to T5) rather than re-asking it.
Linear issue **PRO-169** (one of the last 9 of the curated 50; growth and
crossover in one fund family). Read beside Coatue's and IVP's decisions files,
as the issue asks: Coatue for the public-market layers (13F, 13D/G), IVP for a
growth book whose history predates the archive.

Structure per §1's derivation protocol: **derivations** apply without
confirmation (Erik may veto any); **deltas** are Erik's to confirm; **run-time
standing rulings** are dated, class-wide and flagged for review. Facts marked
*(verified 2026-09-29)* were read from the filing or page named; anything
marked *provisional* is re-derived from verified facts during the run.

---

## Derivations (T1 to T5 applied to verified facts; vetoable)

- **D1 — One registered adviser and its relying advisers, one firm (T1, same
  adviser) → IN.** *(verified 2026-09-29, IAPD and the ADV)* TCMI, Inc.
  (primary business name **TCV**, CRD 160389) is SEC-registered, principal
  office 250 Middlefield Road, Menlo Park; other offices New York (1045 Sixth
  Avenue, 16 advisory staff) and London. Its 2026-03-27 annual amendment
  reports RAUM **$22,506,060,259** across 34 private funds in Section 7.B.(1),
  and the funds' gross asset values sum to the RAUM to the dollar, which
  proves the parse (`sources/registers/adv-160389.json`). IAPD lists TCV VI,
  VII, VIII and IX Management, L.L.C. and TCV Management 2004, L.L.C. as
  relying advisers. Every fund's general partner is a Technology Crossover
  Management entity (II to XII, VF I; Ltd., L.P. or S.à r.l.). EDGAR's 108
  TCV and Technology Crossover registrants are the firm's own vehicles, bar
  the namesakes and feeders in D2.

- **D2 — No strategy desk to partition (T1, strategy addendum) → partition
  empty; namesakes and third-party feeders external.** *(verified
  2026-09-29)* All 34 funds are the growth funds and their parallels: TCV VII
  to XII with their (A) and (B) parallels and Member Funds, the Luxembourg
  SCSps for XI and XII, TCV Velocity Fund I (2021), and the single-deal "Co"
  vehicles (D3). Every one files Form D typed "Private Equity Fund"; there is
  no public-equity, credit or real-asset fund. **The public and the private
  positions sit in the same funds** (PRO-169's first delta), so, as on
  Coatue (D2/D3), nothing partitions by desk and T3 decides each row (D6).
  External: TCV Trust & Wealth Management, Inc. (Richmond, a trust company
  with its own 13F), TCVI Group Inc., TCV Franchise Fund LP (checked by
  address in the run); the access feeders TCV XI Access LLC / Access
  Offshore SCSp and TCV XII Access LLC / Access Offshore SCSp (filing from
  New York, related persons outside managers, "Other Investment Fund"), TCV
  XII (iCapital), L.P. (general partner iCapital PE GP, LLC), and the TCV
  Global Growth XIII access vehicles: third-party feeders into a fund, the
  Thrive IX Access precedent, which hold no positions of their own. TCV
  Acquisition Corp. (CIK 1845580, the firm's own 2021 blank-check company) is
  a vehicle, never a row (D8).

- **D3 — Sleeves and single-deal vehicles (T1, T2) → IN.** *(verified
  2026-09-29, the ADV and Form D)* The (A)/(B) parallels, the Member Funds
  (the general partners' and employees' own commitments, fund money under
  T2), the Luxembourg SCSps and TCV Velocity Fund I sit under the same
  general partners. The single-deal vehicles (TCV Beat Co 2024, Bus Co 2019,
  Cedar Co 2025, Dev Co 2021, Flare Co 2026, Juniper Co 2025, NB Co 2019, Owl
  Co 2025, Tru Co 2021, Guardian 2020, Sports 2018) are "Private Equity Fund"
  issuers of the XI, XII and X general partners: T1's lettered-vehicle
  default. Their Form Ds name no target; a company they hold enters the base
  on the evidence that names it, and their code names are decoded as
  corroboration only (the 8VC SPV-decode layer), never as a label.

- **D4 — Predecessor book and history before the archive (T3, the policy
  constants).** TCV was founded in 1995 by Jay Hoag and Rick Kimball. TCV I
  to III (1996 to 1999) also bought IPO allocations and open-market stock,
  and the firm's own compliance list says so: it "does not include
  investments that were made solely in IPOs or open market public securities
  in TCV I-III as they represent a different strategy than currently
  employed." Those positions are out under T3 whether or not a filing shows
  them, and a 13F line from TCV I to III with no private round behind it is
  such a position. There is no entry-date window (PRO-137): a 1998 entry is
  judged on the same evidence as a 2024 one, and where the record does not
  give the round the stage reads `undetermined` (PRO-169's third delta).

- **D5 — Fund money (T2).** Standard. Partners' personal angel positions and
  seats are out (T4); the Member Funds are fund money. TCV runs no scout
  programme or accelerator. Venture partners and strategic advisers named on
  the team page do not make a position the firm's.

- **D6 — Venture entry, the public line and control (T3).** *(provisional
  until the 2018-2023 grid is parsed)* Three readings, each the standing
  rule applied to a fact the firm publishes itself:
  - **The firm's own deal type decides the class where the firm states it.**
    The compliance page defines "majority" as deals where "TCV, singly or
    together with a consortium of other investors, owns or controls 50% or
    greater of the portfolio company after the closing of the transaction"
    and "minority" as less than 50%, and the 2018-2023 `/companies/` grid
    labels each featured company `minority`, `majority` or `public`. The
    majority definition is word for word §1's control test (the firm alone
    or with its co-investor group at 50% or more), so a `majority` row is a
    **control position**: out, `excluded.json` reason `control_position`,
    counted in the report (PRO-169's second delta), and the profile says the
    record covers TCV's minority venture and growth activity. A `public` row
    is a position TCV bought as a listed security: out under T3 (the
    Omniture and Coatue R1 precedents) unless one of its funds held the
    company through a private round before the listing, in which case the
    row is a member on that round.
  - **Rows the grid never labelled** (most of the pre-2013 book, and every
    company added after 2023) are judged on their own evidence: the firm's
    own announcement, the company's filings (a prospectus holder table, a
    Form D naming a TCV partner or fund), press. A buyout the firm led with a
    consortium (Travelport 2006, GoDaddy 2011, Genesys 2012, Sitecore 2014,
    Believe 2024 are the model's candidates, each checked) is judged on the
    same control test.
  - **A position that first appears as a 13F line** with no private round
    behind it is not a member (standing rule), and **a 13F line that is an
    acquirer's stock received at the sale of a portfolio company is sale
    consideration** (Erik, 2026-09-22): IAC for Expedia, Amdocs for Solect,
    Nuance for BeVocal, Shutterfly for Tiny Prints, RadiSys for Continuous
    Computing and 8x8 for Fuze are the candidates the 13F layer shows, each
    confirmed against the deal in the run.

- **D7 — Person or firm (T4).** Standard. Person-level Section 16 filings
  locate a person; a seat is dated against the person's firm at filing time.
  TCV partners who moved on (Will Griffith to ICONIQ, among others) carry
  their later seats with them.

- **D8 — Operating company (T5).** Standard. TCV Acquisition Corp. is a
  blank-check shell (T5; a promote would be out under the sponsor-promote
  ruling) and a membership trap. Eladian Partners LP, the one fund-shaped
  name on the compliance list, is judged under the fund-shaped rule: out
  unless identified as an operating company.

- **D9 — The compliance list is complete, so absence from it is evidence (§1
  evidence rules; the Battery precedent).** *(verified 2026-09-29)*
  tcv.com/all-companies lists "All investments (listed alphabetically)" as
  of 2026-07-15, 338 legal names, with one declared exclusion (D4's IPO and
  open-market buys in TCV I to III). Archived copies exist for every year
  from 2017, and the earlier sites carried an alphabetical list in almost
  every year from 2000. A Form D name-match or a 13F issuer absent from every
  version of the list is `not_member` with confidence, because a position
  the firm held would be on it; a company on the partnerships grid but not
  yet on the list (ICEYE, a 2026 deal after the list's date) rests on the
  grid listing. The list's legal names double as a rename detector
  (Maplebear = Instacart, Themis Solutions = Clio, Scinapsis = BenchSci).

- **D10 — The roster is swept and curated.** The team pages are archived
  from 2002 (`/team/<first_last>.html`), 2015-2016 (`/teams/<slug>`) and
  2019-2026 (`/team/<slug>`); the live team carries a role per person, and
  only `Investor` is roster evidence (26 operators and 25 strategic advisers
  are not). The firm's own fund Form Ds name only three people (Jay Hoag, Jon
  Reynolds Jr., Frederic Fenton), so the Section 16 filers who co-file with
  the funds (Hoag, Kimball, Drew, Reynolds, Trudeau, Yuan, McAdam, Marshall
  and others) and the capture spans carry the tenure windows, one basis line
  per person.

---

## Deltas (Erik's to confirm; the run proceeds on them, flagged)

- **X1 — The per-position public line (PRO-169 delta 1).** Resolved by D6
  without a new ruling: the firm's own `public` deal type, else the row's
  own record, decides whether a fund entered before or after the listing.
  One question remains Erik's, the same one Coatue R1 raised: **a PIPE or a
  structured investment into an already listed company** is read as a
  purchase of a listed security and is out; if Erik rules that a negotiated
  PIPE is a venture entry, the affected rows enter as Growth.

- **X2 — Control positions (PRO-169 delta 2).** Resolved by D6 on the firm's
  own `majority` label, whose definition includes consortium control. This
  is the reading ICONIQ's open ruling 1 (GoFundMe) asks Erik to confirm: a
  minority seat inside a consortium that takes control is a control
  position. TCV's own definition answers it for TCV's rows; if Erik rules
  otherwise for ICONIQ, TCV's majority rows are still out by the firm's own
  statement that it, with its consortium, controls them.

- **X3 — No new stage (PRO-169 delta 4, Erik 2026-09-26).** Entries are
  Growth by design; the Seed cohort will be thin or empty and no S2A rate
  may publish.

- **X4 — Non-US share (PRO-169 delta 5).** The fx and non-US-listing
  constants bind; the registers per §5's table are probed for `status` on
  European rows where a quiet shutdown is suspected.

---

## Run-time standing rulings

(dated, class-wide, flagged for review)

- **R1 — A partner's Form D seat the post-filing list does not carry (2026-09-29;
  D9 applied forward).** ViaVia Corp's Form D of 2026-03-25 names Clarey Zhu, a
  current TCV investor, beside Hans Tung; the compliance list dated 2026-07-15
  postdates the filing and does not carry the company. A seat that a later
  complete list omits is not shown to be the firm's: `not_member`, medium,
  amended if the next list names it.

- **R2 — A deal-type label that changes between captures is decided on the
  transaction's facts (2026-09-29).** Sportradar reads 'minority' in 2019 and
  'majority' from 2020: TCV and CPPIB bought EQT's roughly 35% stake in 2018
  and the founder kept his whole position, so the row is a member, flagged
  `boundary`. GoFundMe runs the other way ('majority' 2018-2019, 'minority'
  later): Accel and TCV bought a majority from the founders in 2015, so it is a
  control position. CCC Intelligent Solutions stays in: TCV's 8.9% of August
  2017 was bought after Advent's buyout closed and apart from it.

- **R3 — A legal ban on the core business is collapse evidence for the band
  (2026-09-29).** Dream Sports' last priced event ($8B, 2021) predates India's
  2025 ban on real-money gaming, which ended Dream11's core business; the band
  is `below_1b`, `needs_review`, until a new priced event exists.

- **R4 — A namesake filing does not carry the band (2026-09-29).** TCV's ICON
  is ICON International (Stamford, acquired by Omnicom; the list's 'ICON
  Holding Corp.' from 2024). The Vacaville 'ICON Holding Corp' Form D naming an
  Alex Yu predates TCV's Alex Yu and is another company; its band is disputed.

- **R5 — Status when a company is split or recapitalised (2026-09-29).**
  OneSource Virtual: Cognizant's purchase of select businesses (2022) does not
  decide status; TA Associates' majority growth investment of January 2026
  does, `acquired`, the reading used for other majority purchases.

- **R6 — A partner's personal seat before any fund entry is not the entry
  (T4, 2026-09-29).** Open English's 2009 Form D names Robert Trudeau four
  years before TCV led the 2013 Series D; the fund entry is the entry.

- **R7 — Fund-shaped and incubator lines are out (T5, 2026-09-29).** Eladian
  Partners LP (named like an investment partnership, unidentified) and
  Foundries Holdings, LLC (Atiq Raza's incubator holding company) are
  `not_member`, medium, amended if identification lands.

- **R8 — Listed purchases (T3, D6, delta X1; 2026-09-29).** Out: the PIPEs
  into eLoyalty (Mattersight, 2001) and XATA (XRS, 2009), flagged for Erik
  under X1; Interactive Brokers (bought 2009, listed 2007); OpenText (listed
  before TCV I closed); Rocket Companies (at or after its 2020 listing); Talend
  (ADRs held 2020-2021, listed 2016); the twelve rows the grid labels
  'public'.

- **R9 — A stake carried out of a consortium buyout is a control position
  (D6, X2; 2026-09-29).** Mutant (the list's 'BRL Prime One SCsp') came out of
  Genesys, which Permira and TCV bought together in 2012 (the grid:
  'majority'); Permira's own release says it has backed Mutant 'since 2012
  originally through the Permira Funds' investment in Genesys'. Out, medium,
  flagged. Adevinta (2024 take-private) and Nasuni (Vista-led majority, 2024)
  are out on the same test.

- **R10 — Sale consideration where the list names only the acquired company
  (Erik 2026-09-22, applied).** Teya: the list carries 'RMS Holdco Limited
  acquired by Teya Holdings Ltd', so the Teya shares came from the sale of
  Retail Merchant Services; Teya leaves the base.

- **R11 — A recall claim the company's own release contradicts is not a
  member (2026-09-29).** Wikipedia's Kalshi article credits a 'TCV-led' May
  2026 round; Kalshi's release names Coatue as lead and Sequoia, a16z, IVP,
  Paradigm, Morgan Stanley and ARK as participants, and the complete list does
  not carry Kalshi. Not added.

- **R12 — A round only a shared listing places is not named (2026-09-29).**
  Anthropic (grid from 2026) and Hinge Health (grid from 2022) have no source
  naming the round TCV entered; every round they could be is Growth-sized, but
  the stage reads `undetermined` (COLLECTION.md 1, no date-based default).

