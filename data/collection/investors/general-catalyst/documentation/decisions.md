# General Catalyst: investor-specific decisions

Investor-specific rulings for `general-catalyst`, derived from the standing
rule set in `data/collection/COLLECTION.md` §1 (T1 to T5) rather than
re-asking it. Linear issue **PRO-166**, Archetype A of PRO-87 (US venture,
SEC nexus on both sides), with the control-position addendum of T3 as one of
the questions this run was written for (§1 names General Catalyst beside
Insight as the case where one vehicle does both).

Structure per §1's derivation protocol: **derivations** apply without
confirmation (Erik may veto any); **deltas** are Erik's text in PRO-166,
applied as written and flagged; **run-time standing rulings** are dated,
class-wide and flagged for review. Facts marked *(verified 2026-09-27)* were
read from the filing or page named.

---

## Derivations (T1 to T5 applied to verified facts; vetoable)

- **D1 — One registered adviser, with two affiliated advisers (T1, same
  adviser) → IN.** *(verified 2026-09-27, IAPD and the Form ADV of
  2026-07-21, `sources/registers/adv-162548.json`)* General Catalyst Group
  Management, LLC (CRD 162548, SEC 801-115155), doing business as General
  Catalyst and General Catalyst Partners, has been SEC-registered since
  2019-04-26 (an exempt reporting adviser before, withdrawn 2019-03-29).
  Principal office 20 University Road, 4th Floor, Cambridge, MA; other
  offices San Francisco (75 Hawthorne Street, 31 advisory staff, the largest),
  London (42 Berners Street) and Berlin (Schönhauser Allee 8). RAUM
  **$45,502,659,880** across 49 accounts, all discretionary; **48 private
  funds** in Section 7.B.(1). Its Section 7.A names two related-person
  advisers: **La Famiglia GmbH** (Berlin, CRD 318343), the European desk since
  the 2023 combination (D8), and **GC Wealth Management RIA, LLC** (CRD
  327269, SEC 801-128318), a wealth-management adviser (D5).

  IN, as the firm's own vehicles (EDGAR, 2026-09-27): the flagship ladder
  General Catalyst Group II to XIII with their supplemental funds and the
  strategy sleeves of X to XII (Early Venture, Growth Venture, Endurance,
  Ignition, Health Assurance, Creation, Community); the GC Entrepreneurs
  Funds II to IX; GC Creation Fund III; the GC Customer Value Fund family
  (D6); the GC Venture single-deal vehicles (GC Venture V, VII, VIII, IX, X,
  XI (S), XII (A)…(T), (VH 2025), XIII (C-I), (D), (P), (LL)); the single-LP
  Bear Coast funds (general partners under the same adviser); the Excelsior
  Fund, the Guadalupe PIV, GC Aggregator I, GC Group XI Holdings, GC Health
  Assurance Holdings, GC VG Ventures, the Alignment Fund and Global Growth
  Capital Opportunities Fund I. OUT as third-party feeders (the Thrive IX
  Access precedent): General Catalyst XII Access LLC and its Offshore SCSp,
  GC Creation III Access LLC, its Offshore L.P. and the Allocate Access L.P.
  Feeders of any kind seed no row (they hold fund interests, not companies).
  Namesakes sharing the initials: Golub Capital's GC Advisors, GCM Grosvenor,
  GCW and GCB wealth firms are `external`.

- **D2 — Strategy desks (T1, strategy addendum).** The adviser runs venture
  and growth funds, a Creation strategy (D3), the Customer Value Fund (D6)
  and, through its affiliate, wealth management (D5). No public-equities
  strategy with its own vehicles was found on the ADV; a position that first
  appears as a public purchase is out by T3 whatever vehicle holds it (D7).

- **D3 — Creation: a hatch is IN, a roll-up or a purchase is a control
  position (T2 incubations; T3 control addendum).** *(verified 2026-09-27,
  the firm's /capital and /transformations pages)* The firm describes its
  Creation strategy as two things: "Hatches and Transformations, helping
  proven founders start new companies in complex or nascent industries, and
  AI-enabled roll-ups, in which we infuse tech rather than just remove costs",
  and says that "through applied AI, we see even more opportunities to buyout
  and transform businesses". The two halves meet different tests:

  1. **A hatch is an incubation and is IN** where a fund of the firm held the
     position (T2, Thrive's incubations as precedent, PRO-166's delta). The
     firm names its hatches (Livongo, Commure, Hippocratic, Homeward,
     Crescendo, Kayak, Demandware: the Fund XII post of 2024-10-24). The
     entry is the founding capital, staged from the record (Thrive's Oscar
     and Browser Company read Seed on their founding evidence).
  2. **A roll-up or transformation company whose business is buying control
     of existing operating companies is a control position and is OUT**
     (PRO-166's delta: "any roll-up or majority deal"). The companies such a
     platform buys are its add-ons and are never rows of their own (Insight
     D3.5). The named case is HATCo, the Health Assurance Transformation
     Company, which the firm calls "a subsidiary of General Catalyst" and
     which bought Summa Health (the firm's post "Our Acquisition of Summa
     Health", 2024-01-17).
  3. The line between the two is what the company does with the money: a
     hatch builds a new business and raises venture rounds from outside
     investors; a roll-up buys businesses that already operate. A Creation
     company that does both (a new product built on acquired operations) is
     decided on its evidence, flagged, and listed in the report.

- **D4 — Control positions are out, per transaction (T3, control addendum;
  Erik 2026-09-04, restated in PRO-166).** Insight's D3 rules apply
  unchanged: control must be evidenced and cited; a consortium counts as one
  buyer; **the entry decides** (a minority round first and a buyout later is a
  member on the earlier round, and the reverse stays out); an add-on bought by
  a controlled platform leaves with its platform; control rows are
  `not_member` with `"exclusion": "control_position"`, leave into
  `excluded.json` and are counted in the report. Buyout vehicle names on the
  firm's own list ("Ulysses Buyer, L.P.", "Fino Topco, L.P.", "Raven TopCo,
  L.P.") are the signature Insight's R1 found on Form D: an acquisition
  vehicle is control evidence on its face, and the company it bought is
  looked up and judged with it.

- **D5 — Wealth management is another desk (T1 strategy addendum).** GC
  Wealth Management RIA, LLC (CRD 327269) advises individuals and families;
  its site offers "private/co-investment opportunities ... limited to
  qualified investors". A row whose only evidence is a GC Wealth vehicle is
  `other_desk` (partition `wealth`). The 40 people of the Wealth Management
  department are not in the Form D roster.

- **D6 — The Customer Value Fund is not a venture entry (T3; PRO-166's
  delta, now verified).** *(verified 2026-09-27, the firm's own post "From La
  Famiglia to GC Famiglia", 2025-11-13)* The firm describes CVF as "an
  innovative capital model that pre-funds sales and marketing like an asset
  rather than equity". A position the firm holds only through CVF is
  therefore not a round: `not_member`, class `site_listing`, basis "Customer
  Value Fund financing, not equity (D6)". The portfolio card's own **CVF**
  flag is the trigger, and it decides nothing alone: a CVF company in which a
  venture fund of the firm also bought equity (a round naming the firm, a
  Form D naming a partner, the firm's post of an equity investment) is a
  member on that equity entry. Where the evidence shows the CVF instrument
  itself carries equity or warrants, the row is flagged for Erik (the delta's
  own instruction), not decided silently.

- **D7 — Venture entry and the public book (T3).** Primaries, follow-ons,
  secondaries and tenders IN, secondaries and tenders as Growth (policy
  constant). A holding that first appears as a public purchase or a post-IPO
  13G with no venture round is `not_member`. **The SPAC is out**: General
  Catalyst Global Resilience Merger Corp. (CIK 2108962) is a blank-check
  company the firm sponsors, a vehicle with no operating business (T5) whose
  promote is not a venture entry (T3, the KVSA precedent); partition `spac`.
  A company it merges with is a member only where a fund held it through an
  earlier venture round.

- **D8 — The merged firms: before the combination, the earlier firm's
  (T4, the partner-carried ruling of 2026-09-17; PRO-166's delta).**
  *(verified 2026-09-27, the firm's own posts)*
  - **La Famiglia**: "Today, we announced that GC is joining forces with La
    Famiglia" (Hemant Taneja, 2023-10-16); "Earlier this year, we joined
    forces with La Famiglia" (2024-06-04). La Famiglia GmbH (CRD 318343) is a
    related-person adviser on GC's ADV.
  - **Venture Highway**: "Venture Highway (VH) is merging with General
    Catalyst" (2024-06-19); Venture Highway Management II (CRD 307427) is
    inactive.

  A company one of those firms backed **before** its combination date, with
  no General Catalyst fund in it before that date, is `not_member`: the money
  behind the seat was the earlier firm's (T4), exactly as Menlo's fourteen
  partner-carried rows. Where a General Catalyst fund later put money in, the
  row is a member and its entry is **that fund's first check**, never the
  earlier firm's (the Point Nine founder-angel rule applied to firms). Deals
  after the combination through the La Famiglia or Venture Highway vehicles
  or the GC Venture (VH 2025) vehicle are the firm's own (T1: an affiliated
  adviser inside the firm, the Accel London precedent). The card's investor
  names (Neeraj Arora, Jeannette zu Fürstenberg) and the card's "Backed
  since" year are the evidence the judge dates it by.

- **D9 — Fund money (T2).** The GC Venture Fellowship (student founders),
  the GC Institute (policy), GC Famiglia (community, events) and the
  Advisors are programmes and people, not positions. Partners' personal
  angel positions are OUT; a founder's angel check stays out even where the
  firm lists it (Erik, 2026-09-26).

- **D10 — Person or firm (T4).** Standard. The roster is the 63-person
  Investment Team plus every deal investor the cards name, dated where the
  firm's history dates them (`scripts/…/build-roster.py`); the merged teams
  are dated from their combination (D8), so a pre-merger seat on a Form D is
  a seat of the earlier firm.

- **D11 — Operating company (T5).** Standard. Fund vehicles, co-investment
  vehicles, feeders and holding companies are never rows (a holding company
  on the list, "Stripe Global Holdings, Inc.", "Aven Holdings, Inc.", is its
  company's row). Token positions follow the standing rule: "Circle Internet
  Group, Inc. (Arc Token)" is one row under Circle.

- **D12 — The site's own fields.** *(verified 2026-09-27)* The portfolio
  grid carries six flags per company (Active, IPO, Acquired, Creation, CVF,
  Seed), a sector, a region and the deal investors; each company page adds
  "Backed since: <year>". **"Backed since" is the firm's own year of first
  backing**: an anchor (it sets `site_invest_year` and bounds the entry), never
  a round word. **The Seed flag** is the firm's claim that it backed the
  company at seed; it is eligible (it describes the firm's entry, not the
  company's stage today). **Scored 2026-09-27 against the firm's own posts**
  that name the round in the company's "Backed since" year: 27 of 29 flagged
  rows agree (Gitpod and PhysicsX are flagged Seed where the firm's post names
  a Series A entry), so it labels at **medium** confidence (§5: under 95%).
  It labels only `Seed`, and only positively: 12 documented seed entries
  carry no flag (Magma, Phare Health, Rippl, Remnote, Pelico among them), so
  a missing flag says nothing. The judge applies it per row as `first_party`
  cited to the company page, and a documented round overrides it with
  `stage_disputes_band` (the socure class). It is re-scored at close against
  the rows the grind cites.
  **The IPO / Acquired / Active flags** describe the company's state as the
  firm last recorded it and are corroboration for `status`, never a
  substitute for the cited event. **The /list page** is the firm's
  marketing-rule list, "investments made by General Catalyst ... as of June
  30th, 2026", with a declared exclusion for confidentiality provisions: a
  listing on it suffices for membership (§1), and absence from it weighs
  against a bare Form D name-match without proving it (the a16z caveat, not
  the Battery one).

---

## Deltas (Erik's text in PRO-166, applied as written; flagged)

PRO-166 states that no new ruling is required. Its deltas are applied as
D3 (hatch in, roll-up out), D4 (control out, per transaction; the profile
says so), D6 (CVF not a venture entry, verified from the firm's own words),
D8 (merged firms dated by their combination), D5 (wealth another desk) and
the budget note (a very large base; the fx and non-US-listing constants
bind). Two questions the facts raise that no test settles cleanly:

- **X1 — A Creation company that is both a hatch and a buyer.** D3.3
  decides these on their evidence. The report lists every Creation row ruled
  either way with its reason, so the line can be moved cheaply.
- **X2 — Positions held for a single client.** The list tags two positions
  "RDV" ("Sweetgreen, Inc. (RDV III)", "Ahma, Inc. - RDV"), and the ADV
  carries single-owner Bear Coast funds under the firm's own general
  partners. A vehicle under the firm's adviser is the firm's (T1); the run
  records which rows rest only on such a vehicle, if any.

---

## Run-time standing rulings

(dated, class-wide, flagged for review)

- **R1 — A stake in a listed acquirer that bought a portfolio company is sale
  consideration (2026-09-27).** COLLECTION.md 1 (the Teladoc ruling) applied
  to the list's public-company entries whose only tie to the firm is an
  acquisition paid in stock: Teladoc (Livongo), Millennial Media (Jumptap; the
  firm's first 13G is dated the month the deal closed), Xero (Melio, 2025),
  WW International (Weilos), Starco Brands (the a16z class). All
  `not_member`, medium confidence where the path is inferred rather than
  filed. Twilio, Snowflake, Slack and similar list-only public names with no
  round naming the firm stay members with an undetermined stage and are
  listed in the report: a post-IPO or consideration stake would move them
  out under T3.
- **R2 — Form D namesakes and pre-GC seats (2026-09-27).** A Form D person
  match is the firm's only when the person sat for the firm: the Louisville
  Mark Crane (Edumedics, ICATS, IKOTECH, EQL Games), the issuers' own
  executives named Tony or Anthony Ho (CRISPR, Land Medicine, Flitch) and
  Shou-Chuan Ho (Prime View) are namesakes; Christopher Bischoff's 2018-2020
  seats (Cedar, VillageMD) are Kinnevik's, Marc Bhargava's Tagomi seat is his
  own company's, Neeraj Arora's Vivino seat and Holly Maloney's erecruit seat
  predate the firm, and Phillip Riese (a Catalyst Advisor) sits on his own
  account (eWise, MPOWER). All `not_member` (T4). Form D rows that ARE the
  firm's (a partner director, the company on the list under another name) are
  folded into the list row through identity-merges.json (21 merges).
- **R3 — The Customer Value Fund, applied (2026-09-27; D6).** From the CVF
  research (scratch/research/cvf-findings.json): ten companies whose only tie
  is CVF money are `not_member` (Beautiful.ai, Chainguard, CookUnity,
  Function Health, IM8, Ladder, Mirage, Quo, Relay, Rylo); where the firm
  also bought equity, the entry is the first equity round, not the CVF date
  (Factorial's 2026 Series D, Iru's 2024 round). Dandy is `uncertain`: a CVF
  flag, two health partners on the card, and no citable round either way.
- **R4 — Creation rows decided (2026-09-27; D3, X1).** From the Creation
  research (scratch/research/creation-findings.json): hatches IN (Commure,
  Hippocratic, Homeward, HealthEx, Maribel, Kayak, Demandware, Datalogix,
  Datto, Livongo and others); roll-ups OUT as control positions (Athletes
  First, Beacon, Dwelly, Long Lake); the X1 rows ruled on the entry: Accrual,
  Crescendo, Eudia and Titan IN (a product company at the firm's entry,
  acquisitions after), Zero RFI OUT (launched on its seed together with three
  acquisitions). Aura is OUT: the firm entered through the consortium that
  took Intersections private (D4, the entry decides), and Intersections is
  out with it. Eleven list entries named as buyout or holding vehicles (Ulysses
  Buyer, Fino Topco, Raven TopCo, Dynamo Topco, Logicbroker TopCo, RW-2023
  HoldCo, Build Holdco I, ReInvent Commerce Holdings, XFIT Holdings, Ponto
  Meridian Rollup, Beacon Acquisition) are control positions on their face.
- **R5 — A stale public float on a weak CIK join says nothing about status
  (2026-09-27).** Duty 3 found the float layer's "acquired" on four rows whose
  registrant is another company (Cicero Technologies, Faro Health, Sprint
  Labs, Shyft); each is disputed with `model_disputes_source`. A company's own
  priced-round announcement is not a vendor mark: Hive's $2B Series D (its
  own blog, 2021) bands the row, where 8VC's book read it as vendor-carried
  (cross-rulings.json).
- **D12 amendment — the Seed flag re-scored at close.** Against the 42
  flagged rows whose stage the run cited from outside the grid, 34 agree
  (81%): three flagged rows were named pre-seed (Afori, Berry Health,
  Stilla) and five entered at a later round (Gitpod, PhysicsX, Thatch,
  Anagram, Stripe). The flag stays a positive, medium-confidence Seed label;
  20 cited seeds carry no flag.
