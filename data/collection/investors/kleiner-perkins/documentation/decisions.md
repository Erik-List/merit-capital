# Kleiner Perkins: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Kleiner Perkins
(slug `kleiner-perkins`; Kleiner Perkins Caufield & Byers, "KPCB", until the
2019 rebrand). The judge cites these rulings per line. Written at kickoff
2026-09-30 (PRO-99) under the derivation protocol of COLLECTION.md §1:
**derivations** (a standing test applied to verified facts; no confirmation
needed, vetoable), **deltas** (Erik's), and **run-time standing rulings**
(dated, class-wide, flagged for review).

**The structural facts of this run.** Kleiner Perkins was founded in 1972 in
Menlo Park by Eugene Kleiner and Tom Perkins. It invests from one numbered fund
family (KPCB I to XIX, then Kleiner Perkins XX to XXII), with growth sleeves
that changed shape three times: the KPCB Digital Growth Funds I to III
(2010-2016) and the KPCB Green Growth Fund (2008), then, after the growth team
left in 2018, Kleiner Perkins Select Funds I to IV (2020 on). Its own site is a
WordPress install whose REST API answers without a token and lists 416
companies with the firm's own first-investment stage (Early or Growth), a
since-year, Current or Prior, the company's current stage and the acquirer on
exits. The archive (kpcb.com to 2019) adds the companies the live list has
dropped.

**The issue's window premise is retired.** PRO-99 was written when the 2006
entry window was a policy constant. COLLECTION.md §1 removed it on 2026-09-19
(PRO-137): a 1985 entry is judged on the same evidence as a 2025 one, and where
the record does not give the round the stage reads `undetermined`. The report
states the pre-2006 share as a fact about the book, not as a window.

## Derivations (T1 to T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm and its vehicles (T1).** Facts, verified 2026-09-30 from IAPD
  and the Form ADV signed 2026-03-31 (`data/filings/adv/161035.pdf`):
  - **One adviser.** Kleiner Perkins (legal name Kleiner Perkins Caufield &
    Byers, LLC), **CRD 161035**, SEC 802-75571, an exempt reporting adviser.
    Its Schedule D 7.B.(1) reports 42 private funds: KPCB XII to XIX and
    Kleiner Perkins XX, XXI and XXII with their founders and friends funds;
    Kleiner Perkins Select Fund I to IV (and Select Founders / Friends funds);
    Kleiner Perkins Flex I; KP Sightglass I and II; **KPCB Digital Growth Fund
    I, II and III** (and their founders funds); **KPCB Green Growth Fund**;
    and **KPCB China Fund II, L.P.** (Cayman; general partner KPCB China
    Associates II, L.P.).
  - The earlier vehicles (KPCB I to XI, the iFund and sFund programmes, the
    Pandemic and Bio-Defense Fund, KPCB Edge) predate or sit outside the
    current 7.B.(1) and are read off EDGAR's own filer list
    (`entities.json`).

  **Outcome: IN** for every numbered fund, founders and friends fund, Select
  fund, Flex and Sightglass vehicle, the Digital Growth Funds I to III, the
  Green Growth Fund and the programme funds (iFund, sFund, Pandemic and
  Bio-Defense, Edge), and for every company on the firm's own list in any
  era. **External**: Bond (D2 below). KPCB China: delta X1 below (provisionally IN).

- **D2: The growth-team separation (T1; the question the issue named).**
  Facts: Mary Meeker's growth team (Mood Rowghani, Noah Knauf, Juliet de
  Baubigny, Daegwon Chae, Paul Vronsky) announced its departure in September
  2018 and launched **Bond** (Bond Capital Management, LP, **CRD 304391**, its
  own registration) with a $1.25B first fund closed in April 2019
  (TechCrunch, 2019-04-24; FinSMEs, 2019-01). Bond's ADV reports Bond Capital
  Fund, Bond II and Bond III in its own 7.B.(1), and reports the four KPCB
  Digital Growth Funds only in **7.B.(2)**, naming **Kleiner Perkins** as the
  adviser that reports them: the Digital Growth Funds stayed Kleiner Perkins
  vehicles, and Bond's people went on managing Digital Growth Fund III to its
  wind-down. Test: T1 resolves per vehicle by CRD or CIK, never by the brand
  or by who staffed it. **Outcome:** a position held by a KPCB Digital Growth
  Fund is **IN** whenever it was taken (the vehicle is under CRD 161035); a
  position held only by a Bond fund is **OUT** (`external`, the Accel-KKR and
  HongShan shape); **the separation date is September 2018**, used only to
  date seats (T4): a Bond partner on a Form D after 2018-09 locates Bond, not
  Kleiner Perkins. The Select funds from 2020 are Kleiner Perkins' own growth
  sleeve (IN).

- **D3: Fund money (T2).** A position is the firm's when a fund of the firm
  held it. **Outcome:** partners' personal angel checks, a venture or
  operating partner's own board seat, the KP Fellows programme (a student
  internship, no investment) and LP positions in other managers' funds are
  OUT (Sequoia, a16z, Accel, Lightspeed, Cherry, Point Nine precedents). A
  company on the firm's own site is IN on the listing (§1) unless the firm's
  own page or the record shows the money was not the firm's (the Menlo
  partner-carried rule): the site's "Prior" rows credited to a partner's
  earlier firm are checked per row. The iFund and sFund were Kleiner Perkins
  funds with strategic LPs (Apple-platform and Facebook / Zynga / Amazon),
  not co-investor programmes: IN.

- **D4: Venture entry (T3).** Primaries, follow-ons, secondaries and tenders
  in a private company are IN, secondaries and tenders as Growth. Positions
  first appearing as public-market purchases, 13F holdings or post-IPO 13Gs
  are OUT. Kleiner Perkins runs no buyout practice; a control transaction, if
  one surfaces, is OUT under the control addendum.

- **D5: Person or firm (T4).** Standard person-level attribution and seat
  dating. Kleiner Perkins' alumni built many firms and their seats travel:
  Vinod Khosla (Khosla Ventures from 2004), the Bond partners (from 2018-09),
  Ted Schlein (Ballistic Ventures from 2022, while still named Partner and
  Advisor on the site), Randy Komisar, Aileen Lee (Cowboy Ventures), Chi-Hua
  Chien (Goodwater), Trae Vassallo (Defy), Beth Seidenberg (Westlake Village
  BioPartners), Joe Lacob, Russ Siegelman, and the partners who later joined
  Menlo, Greylock and others. A seat is dated against the person's firm on
  the filing date; an advisor's seat counts only where a firm fund held the
  position.

- **D6: Operating company (T5).** Fund-shaped entries on the firm's own list
  (another manager's fund, an accelerator) are `not_member` until identified
  as operating companies; the standing token and plumbing rules apply
  unchanged.

- **D7: The site's stage field (§5, PRO-135 eligibility).** The CMS field
  `first_investment_stage` is the firm's own label for the round it entered
  (a separate `current_stage` field carries the company's stage now), so it
  is **eligible**. Its values: `Early` straddles Seed and Series A and is an
  **anchor, never a label**; `Growth` collapses onto Growth and labels once
  scored against documented entry rounds (score and confidence recorded in
  `config.json` `site_api._entry_stage_note` before it is promoted).

## Deltas (Erik's; a provisional reading is applied and raised at close)

- **X1: KPCB China.** Facts: Kleiner Perkins opened KPCB China in 2007 with a
  $360M fund (VentureBeat, 2007-04-23), team from TDF Capital (Tina Ju, David
  Su, Forrest Zhong, Joe Zhou). KPCB China Management, Ltd. is **its own
  exempt reporting adviser** (CRD 161470, SEC 802-75570), owned by Tina Ju,
  Howardstong Group and Kleiner Perkins Caufield & Byers (a shareholder since
  2007-04; the ADV lists it as a related person of Kleiner Perkins), reporting
  KPCB China Fund, L.P. and KPCB China Founders Fund. **KPCB China Fund II,
  L.P. is reported on Kleiner Perkins' own 7.B.(1), and KPCB China Fund, L.P. and
  KPCB China Founders Fund are on Kleiner Perkins' own 7.B.(2)** (funds the filer advises that another adviser
  reports; `sources/adv/adv-7b-funds.json`): Kleiner Perkins advises every KPCB China fund. The investment team later
  formed its own firm, China Creation Ventures, and Tina Ju manages the
  remaining portfolio. **The firm's own site listed the KPCB China companies as
  its own**: the kpcb.com China listing (2008-10), the 2012-17 company pages
  under "Teams: China", and the kleinerperkins.com logo grid through 2024; the
  live 2026 list carries none of them. Two limbs of T1 meet: an affiliated
  adviser of the one firm is IN (Accel's India desk, relying adviser plus
  affiliated ERAs), a brand-sharing entity with its own ERA and fund family is
  OUT (HongShan, Lightspeed India, which also carried the firm's own
  "not a unitary enterprise" disclosure; no such disclosure exists here).

  **Provisional reading, applied and raised at close: IN**, re-derived
  2026-09-30 from the kickoff's provisional OUT once the archive showed the
  firm listing these companies as its own for twelve years (§1: a site listing
  suffices unless the firm disclaims the position; nothing disclaims it). A
  company KPCB China's funds held is a member on the firm's own listing.
  **Except Tina Ju's pre-2007 TDF Capital deals**, which the China listing
  carried because she had backed them before joining (Alibaba, Baidu, China
  Netcom, Focus Media, Hurray!, CGEN Digital Media, P-Cube): `not_member` under
  the partner-carried rule (Erik 2026-09-17, Menlo) unless a KPCB China fund's
  own round is documented. China Creation Ventures' own investments (after the
  team left) are external. If Erik rules KPCB China OUT, 78 rows leave the
  base at the next re-ingest; the class is flagged `kpcb_china` so it can be
  counted and removed in one step.

## Run-time standing rulings (dated, class-wide, flagged for review)

All 2026-09-30, from the EDGAR full-text recall triage; each binds its class, not one row.

- **R1: A "backed by Kleiner Perkins" line in a third party's biography or filing is a name match.** A director
  bio or a narrative mention in someone else's filing (Zambeel, Geocast, Medibuy, FirstLook, Vanguard Solar) needs
  the same corroboration as a Form D name match (§1): a KP fund named on a filing, the firm's own listing, or a
  press or company source naming Kleiner Perkins in a round. Without it the candidate is not added.
- **R2: A partner named as shareholder representative in a merger agreement is a person, not a fund.** Evant,
  AesThera: the representative locates the person (T4); the row needs a fund named elsewhere.
- **R3: Money through a vehicle Kleiner Perkins co-owns with others is not fund money** (T2). eVolution (Finacity),
  the ServiceMaster joint venture (WeServeHomes.com): not a member unless a KP fund itself held the company.
- **R4: A partner's family office is not the firm** (T2). Foris Ventures (John Doerr's) and the like: out.
- **R5: The member is the company the firm's fund held.** KPCB China held CreditEase, not its listed subsidiary
  Yirendai: CreditEase is the row. A holding that later shows up only as merger stock (CVie Therapeutics into
  Windtree) is the private company, and the acquirer's stock is sale consideration (Erik 2026-09-22).
- **R6: A Section 16 filing by a person that names a Kleiner Perkins fund as the holder of record corroborates the
  fund's position.** Beth Seidenberg's Forms 3 footnote the pre-IPO preferred held by KPCB XIV and its founders
  fund (TESARO, Epizyme, Atara, ARMO, Progyny, Vera, Sagimet): the footnote names the fund, which is the §1 fund
  signal, not the person's own holding. A person's filing with no fund named stays person-level.
- **R7: The live site lists some deals new partners made at their previous firms** (the Menlo partner-carried rule,
  Erik 2026-09-17, applied). Found in the grind: the firm's own post welcoming Leigh Marie Braswell credits Neon,
  Chronosphere and Persona to her previous firm, and all three carry a 2021 year on the site while first archived
  only from 2023; Mamoon Hamid (joined 2017 from Social+Capital, before that USVP) is the only link to Box, Yammer and
  Wave; Ilya Fushman (joined 2018 from Index) to Culture Amp and possibly Front. The signature here differs from
  Menlo's: the site DOES give a year and a stage, but the year predates the partner's arrival, the page first appears
  after it, and no round names Kleiner Perkins. Verdict `not_member` where a round history is on record and none of
  its rounds names a Kleiner Perkins fund and the partner's prior firm led or held it; where the record is silent the
  listing stands (§1). Rows ruled: box, yammer, wave, neon, chronosphere (judges, 2026-09-30); the rest are swept in the
  stage pass.
- **R8: The seed-to-A rate rests on the cited subset, and the shape guard is restated for it** (flagged for Erik).
  The firm's own site labels an entry only Early or Growth, and Early covers Seed, Series A and some Series B, so a Seed
  entry exists in this base only where a round is cited (a post, press, a prospectus, a Form D sequence). 464 of the 890
  rows read `undetermined`; the Seed cohort is 60 decided rows of 68, at 83.3%. Companies whose seed was written about
  are the ones that went on to raise, so the rate is biased upward by construction. `verify.shape.c2a_rate_max` is
  restated at 0.85 with this reason. Erik's call: publish the rate with that caveat, or decline the column for this
  firm (`verify.c2a_deterministic: false`).
- **R9: A legal-name variant of an excluded company is excluded with it.** The rebuild resurfaces Form D legal names
  (Box.net Inc, Pilot.com Inc, Wave Accounting Inc, Hippo Analytics Inc, EntreMed) once the listed row leaves; each
  variant carries the canonical's verdict and basis (COLLECTION.md s8).
