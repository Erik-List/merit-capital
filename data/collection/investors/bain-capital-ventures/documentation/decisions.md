# Bain Capital Ventures: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Bain Capital
Ventures (slug `bain-capital-ventures`, display name always **Bain Capital
Ventures**, "BCV" in notes). The judge cites these rulings per line. Written at
kickoff 2026-09-27 (PRO-162) under the derivation protocol of COLLECTION.md §1:
**derivations** (a standing test applied to verified facts; no confirmation
needed, vetoable), **deltas** (Erik's), and **run-time standing rulings**
(dated, class-wide, flagged for review).

**The structural fact of this run:** BCV has its own adviser registration, so
T1 draws the boundary by adviser and no strategy partition is needed (the
issue's first delta resolves the simple way). The hard boundary is in time,
not in strategy: the firm's archived site lists Bain Capital's venture-stage
deals from 1984 to 2000, made by the parent's generalist funds before BCV
existed (D2).

## Derivations (T1 to T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm and its vehicles (T1).** BCV's funds are advised by
  **Bain Capital Ventures, LP** (IAPD **CRD 145652**, SEC 801-69071, formerly
  Bain Capital Venture Partners, LLC; principal office 200 Clarendon Street,
  Boston; other offices 799 Broadway New York and 450 Pacific Avenue San
  Francisco; annual amendment signed 2026-03-31 by the "Chief Compliance
  Officer, Ventures & Crypto"; Item 5.F RAUM $9,837,931,000). Its Section 7.B
  lists 20 private funds (`sources/registers/adv-145652.pdf`): the venture
  funds and their private-investor feeders (2005, 2007, 2009, 2012, 2014, 2016,
  2019, 2021, 2022), the co-investment funds I to IV, the 2019-MD primary and
  co-investment sidecars, **BCV 21 Innovators Fund**, and **Bain Capital
  Crypto** (BCV Crypto I and I-A, Bain Capital Crypto II and II-A). EDGAR adds
  the 2001 and 2004 funds (CIK 1135638, 1302453), Bain Capital Venture Fund XI
  and BCV XI Private Investors (2026) and **BCV Emerge Fund V** (2026, Form D
  signed by Enrique Salem and Ajay Agarwal).
  **Outcome: IN** for every position held by any of these vehicles, venture
  and crypto alike: one adviser, one CCO for "Ventures & Crypto", the crypto
  funds' Form Ds signed by BCV's managing partners (Salem, Agarwal) in 2021.
  Precedent: a16z's crypto family under one adviser. **Bain Capital Crypto is
  the same desk**, which answers the issue's fourth delta.
  **External (T1, own advisers):** every other Bain Capital strategy files
  under its own registration: Bain Capital Private Equity, LP (CRD 145653),
  Bain Capital Credit, LP (134852), Bain Capital Public Equity, LP (145650),
  Bain Capital Real Estate, LP (291809), Bain Capital Insurance Solutions
  (305575), Bain Capital Partnership Strategies (297457), and the European,
  Luxembourg and Irish entities. Their positions are not BCV positions, and a
  company they back enters this base only through a BCV vehicle. Life
  Sciences, Tech Opportunities and Double Impact are strategies of those
  advisers, not of CRD 145652 (none appears in its 7.B). **Third-party
  feeders** into BCV funds (Brown Advisory Investors 2016, BGA Horizon Fund's
  BCV 2022 series, MGF Partners II's Bain Capital Crypto Fund II series,
  iCapital) are external (Thrive IX Access precedent). **Namesake:** BCV 55,
  BCV 66, bcv 77 and BCV III Opportunity LLC are Blue Cloud Ventures vehicles
  (Form D related persons Aber Whitcomb, Darin Feinstein, Blue Cloud
  Management LLC), and BCV Asset Management Inc. is unrelated.
  No partition: `config.desks.partition` is empty.

- **D2: Bain Capital's generalist funds are another desk; the venture fund
  family is BCV's from its first vehicle (T1, strategy desks, resolved per
  vehicle; flagged for Erik as R1 below).** Facts: the firm's own 2006
  portfolio page says "Bain Capital's history of investing in early stage
  companies dates back to 1984, having made over 101 venture-stage investments
  since inception ... In 2001, we formed Bain Capital Ventures as a separate
  arm of Bain Capital to focus exclusively on growth investments"
  (web.archive.org capture 2006-06-15 of /portfolio/index.asp). A venture-
  dedicated vehicle predates that: **Bain Capital Venture Fund, L.P.** held
  Recruitsoft from November 1999 (Taleo's S-1, 2004: "17,337,891 shares held
  of record by Bain Capital Venture Fund, L.P.") and Bluestem Brands (its 2011
  S-1), with Bain Capital Investors, LLC, the parent's GP, above it. Every
  later venture vehicle carries the same name family (Bain Capital Venture
  Fund 2001, 2004, 2005, 2007 ...) and today sits under CRD 145652. Before the
  2008 registrations (Bain Capital's advisers CRD 145650 to 145653 were
  registered together) one Bain Capital adviser covered every strategy, so
  adviser identity cannot draw the line for the early years and the vehicle
  does (the strategy-desk addendum, Erik 2026-09-04: "resolve the desk per
  vehicle by CRD or CIK, never by the brand that announced the deal"). The
  2002 to 2010 listings carry positions of Bain Capital's generalist funds
  (Bain Capital Fund I onward, 1984 to 2000, now the private-equity family
  under CRD 145653) beside the venture funds' own: Staples, Bright Horizons,
  Gartner Group (IPO 1993), Experian, Stericycle, DoubleClick, Course
  Technology, Jostens Learning, The Learning Company.
  **Outcome:** a position held by the venture fund family (Bain Capital
  Venture Fund, L.P. from 1999, and every later BCV vehicle) is IN; a position
  only a generalist Bain Capital fund held is another desk and leaves the base
  as `not_member`, basis "other desk (Bain Capital generalist fund, D2)",
  flagged `bain_capital_heritage` (the ledger's only special exclusion is
  `control_position`, so the desk reason rides in the basis). Where the
  record does not name the vehicle, the entry date decides by proxy: before
  1999 no venture vehicle existed, so the generalist funds held it; from 1999
  the row is judged on its own evidence. **Where a venture fund later
  invested**, the row is a member through that fund's first check and its
  entry is that check (the Point Nine precedent, Clio / Westwing).
  Why flagged: the firm lists these companies as its own history, which is a
  listing on its own site (normally sufficient alone), so two readings exist.
  The ruling flips mechanically (re-record the flagged verdicts, rebuild).

- **D3: Fund money (T2).** OUT: partners' personal angel checks; the BCV
  community programmes named on the team page (AI Fellows, Discover Fellows,
  Labs Fellows, Research Fellows) unless a fund held the company; scout
  checks with no main-fund follow-on. IN: companies incubated or seeded in
  BCV's programmes where a BCV fund held the position (the BCV Labs
  incubations), and BCV 21 Innovators Fund positions (a 7.B fund of the
  adviser).

- **D4: Venture entry (T3).** Primaries, follow-ons, secondaries and tenders
  IN, tenders as Growth. The 2006 to 2010 site sorted its portfolio into
  "Early", "Midstage" and "Expansion/Growth Buyout": BCV made growth buyouts
  in that decade, so the **control-position addendum** (Erik 2026-09-04)
  applies per transaction: a transaction in which BCV alone or with its
  co-investor group took control is `not_member` with `exclusion:
  control_position`; a minority growth round is a member. Positions that
  first appear as public-market purchases, 13F holdings or post-IPO 13Gs are
  OUT. The entry decides: a minority round followed by a later buyout stays a
  member (Insight D3.4).

- **D5: Person or firm (T4).** A seat is dated against the person's firm at
  filing time. BCV's people move to and from other Bain Capital strategies
  (the Form D fund filings name Bain Capital-wide officers: the group CFO,
  private-equity managing directors), to other venture firms (Salil
  Deshpande to Uncorrelated Ventures, 2017) and into operating roles. A Form D
  seat of a Bain Capital private-equity partner is that strategy's, never
  BCV's (D1). The roster keeps a fund-Form-D name only where a BCV people
  page or deal attribution corroborates it (`scratch/build-roster.py`).

- **D6: Operating company (T5).** Standard: fund vehicles, SPVs, feeders,
  tokens with no issuing organization and natural persons are not rows.
  Crypto positions follow the token rule: a token with an issuing
  organization (a labs entity, a foundation with treasury and governance) is
  a row under the organization.

- **D7: "Bain Capital" in the press is not BCV (the issue's second delta).**
  A press line naming "Bain Capital" as investor is evidence of a BCV position
  only where the release, the filing or the firm's own list ties it to Bain
  Capital Ventures or a BCV vehicle. A name match on the parent is not
  evidence, and the recall probe searches "Bain Capital Ventures", never the
  bare parent.

- **D8: The profile is sliced to the base (the issue's third delta).** The
  adviser's Item 5.F RAUM is BCV's own (one adviser for venture and crypto
  only), so it is the sworn AUM and matches the base's boundary; no parent
  figure enters any field.

## Deltas (Erik's)

None confirmed before kickoff: the issue asked for none beyond the four it
listed, and each resolved as a derivation (D1, D7, D8). D2 is raised as
run-time ruling R1 for Erik's veto.

## Run-time standing rulings (dated, class-wide, flagged for review)

- **R1 (2026-09-27, flagged): the generalist-fund heritage book is out (D2).**
  The class moves every archived listing whose only Bain Capital holder was a
  generalist fund (entries 1984 to 1998, and later ones the record ties to
  those funds only). Raised under COLLECTION.md §9 trigger 2 at close.
- **R2 (2026-09-27): the site's stage tag labels at medium confidence.** The
  Sanity `stage` tag (Seed / Early / Growth) is the stage BCV entered, not the
  company's current stage: Crusoe Energy, Nightfall and Orum read Seed while
  each has since raised growth rounds, and IPO and Acquired are separate tags.
  Scored against rounds the firm's own posts and Wikipedia name: 25 of 27
  (Seed 10 of 11, Growth 15 of 16). The two misses show where a documented
  round must override: Archive (the firm "first invested in Archive in their
  pre-seed round", tagged Seed) and HYCU ("BCV leads $87.5 million Series A",
  tagged Growth). `Seed` and `Growth` label as `first_party` at medium
  confidence with the company's deep link as citation
  (`baincapitalventures.com/portfolio/<slug>/`, which the site redirects to its
  own listing filtered to the company); `Early` is an anchor (it covers Series
  A and B entries: Ankorstore and Clockwise were Series B entries) and never
  mints a stage. A documented round overrides the tag with
  `stage_disputes_band`.
- **R3 (2026-09-27): the live portfolio is a compliance list with declared
  exclusions.** The firm's own disclosure page reads: "This website shows Bain
  Capital Ventures portfolio company investments from 2007 vintage funds to
  the present. Only portfolio companies where Bain Capital Ventures has 10%
  ownership or higher are listed" (baincapitalventures.com/disclosure, read
  2026-09-27). Two consequences. (a) Absence from the live list is NOT
  evidence against membership: a pre-2007-fund position or a sub-10% stake
  (typical of growth co-investments) is excluded by construction, so the
  archive eras (2002 to 2023), the Form D sweep and the exit-side filings
  carry that recall, and the Battery "complete first-party list" rule does not
  apply. (b) A company on the live list meets a 10% ownership threshold at
  some point, which supports membership but says nothing about control; D4
  still decides per transaction.
