# Sutter Hill Ventures: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Sutter Hill
Ventures (slug `sutter-hill-ventures`, display name always **Sutter Hill
Ventures**, "SHV" in notes). The judge cites these rulings per line. Written at
kickoff 2026-09-28 (PRO-77) under the derivation protocol of COLLECTION.md §1:
**derivations** (a standing test applied to verified facts; no confirmation
needed, vetoable), **deltas** (Erik's), and **run-time standing rulings**
(dated, class-wide, flagged for review).

**The structural facts of this run.** Sutter Hill is one evergreen
partnership, not a ladder of numbered funds: the adviser reports two private
funds, and the older of them has held every position since the 1960s. The
firm's live site is a wordmark and an address, so the published portfolio is
entirely archival: the firm listed its investments on shv.com and
sutterhillventures.com from 1999 to 2016, starting with a 1999 table of every
investment since 1970 with the firm's own outcome line per company. Its
incubations show up on issuers' Form Ds as a firm managing director serving as
the new company's executive officer, filing from the firm's own address.

## Derivations (T1 to T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm and its vehicles (T1).** The adviser is **SUTTER HILL
  VENTURES, L.L.C.** (IAPD **CRD 162959**, exempt reporting adviser SEC
  802-75145; principal office 755 Page Mill Road, Suite A-200, Palo Alto; no
  other office; annual amendment 2026-03-27, `data/filings/adv/162959.pdf`).
  Its Section 7.B reports two private funds: **Sutter Hill Ventures, A
  California Limited Partnership** (805-7813429138, gross assets
  $2,940,423,000, 53 beneficial owners, 37% held by the firm's related
  persons) and **1962 Opportunity Fund L.P.** (805-5830529833, general
  partner 1962 Opportunity Fund I GP, LLC, gross assets $750,032,000, 15
  owners; Form D as 1962 Opportunity Fund I, L.P., CIK 2034518, 2024, with the
  adviser as a related person). EDGAR adds the partnership's own ownership
  filings (CIK 879051, Forms 3/4 and 13D/G, 1997 to 2024) and the co-filers
  at the same address: **Sutter Hill Entrepreneurs Fund (AI), L.P.** and
  **(QP), L.P.** (CIK 1228875, 1228877; Forms 3/4 2006 to 2014), **Sutter
  Hill Associates, L.P.** and **LLC** (the general partner entities) and
  **Sutter Hill Management Company, L.L.C.**
  **Outcome: IN** for a position held by any of these: one adviser, one
  office, one partnership. **External:** Costanoa Venture Capital (Greg
  Sands's own firm from 2012; its first fund's Form D gives 755 Page Mill Road
  because it started in SHV's office), Bluebird Ventures I, L.P. (2019, Jeff
  Bird's own vehicle, not in the adviser's 7.B), 1870 Embarcadero LP (a
  property partnership filing from the same address), John Pasquesi's Otter
  Capital deals (same office park), and every "Sutter" namesake.

- **D2: Partners' personal vehicles (T2; the issue's second question).**
  Sutter Hill's prospectus footnotes list the partnership beside its partners'
  trusts, retirement plans and family partnerships, which co-invest with it:
  "securities owned by Sutter Hill Ventures, a California Limited Partnership,
  managing directors and a director of the general partner of Sutter Hill,
  retirement trusts of some of such managing directors, family partnerships
  associated with such managing directors, Sutter Hill Entrepreneurs Fund
  (AI), ..." (Amerigroup S-1/A, 2001-03-02, sec.gov/Archives/edgar/data/1064863/
  000095013301500056); a 2002 Clarus proxy splits one managing director's
  28,478 shares held individually from the partnership's 46,929 and the
  Entrepreneurs Funds' 5,596 and 14,171.
  **Outcome:** membership needs a position of the partnership, the 1962 fund
  or the Entrepreneurs Funds. A company only a partner's personal vehicle
  held is out (partners' personal angel books, T2; the Cherry and Kushner
  precedents), and the personal co-investment beside the partnership changes
  nothing about a row that is in. A Form 3/4 a partner files about personal
  holdings locates the person (T4), not the partnership; a Form 3/4 or
  13D/G whose reporting owner is Sutter Hill Ventures, or whose footnote puts
  the shares in the partnership, is `fund_filing`.

- **D3: Incubations are members, and the entry is the fund's first round
  (T2 and T3; the issue's first question).** Facts: Sutter Hill forms
  companies around one of its managing directors as the founding executive
  (Os76, Inc., later Pure Storage, 2009: Mike Speiser and John Colgrove both
  director and executive officer on the first Form D; Bitmoon Computing, later
  Sigma Computing, 2014; Laserlike 2015; Augment Computing 2022; each filing
  from 755 Page Mill Road). The partnership funds the company's first
  preferred round. **Outcome: IN** wherever a fund position is shown (a
  listing, a fund filing or a documented round), because fund money went in
  through a primary financing. The entry is that first round, labelled as the
  record names it. The managing director's own founder shares as acting CEO
  are the person's (T4) and are never the entry. **The taxonomy admits the
  entry, so no §9 trigger-3 question arises:** COLLECTION.md §6 already says
  the label follows what the firm and the record call the round. An
  incubation whose first round the record names a seed is a Seed entry and
  joins the S2A cohort; one named Series A (most of Sutter Hill's) is not a
  Seed entry; one the record does not name reads `undetermined`. `Pre-Seed`
  stays reserved for programme terms (Erik, 2026-09-19).
  **The Form D role marks the incubation, not the money.** A firm person as
  "Executive Officer" or "Promoter" on the issuer's first Form D is evidence
  that the firm formed the company; fund money still needs one of the three
  sources above, and a director seat alone is a name-match that needs
  corroboration (§1 evidence rules).

- **D4: Venture entry (T3).** Primaries, follow-ons, secondaries and tenders
  IN, tenders as Growth. A position that first appears as a post-IPO 13G or
  13D with no documented pre-IPO round is out (the Lightspeed and Thrive
  rule). Sutter Hill runs no buyout practice, so the control-position
  addendum is not expected to fire; any control transaction found is judged
  under it.

- **D5: Person or firm (T4).** A seat is dated against the person's firm at
  filing time. Known moves: Greg Sands to Costanoa Ventures (2012), Jim
  Gaither from Cooley (a lawyer's board seats before he joined), Stefan
  Dyckerhoff from Juniper Networks (2012), Sam Pullara from Yahoo and Twitter
  (2012), Mike Speiser's own founder years before 2008, and the incubated
  companies' founders who file from the firm's address while employed by the
  new company. The roster (`scratch/build-roster.py`) dates each person from
  the archived people pages, the ADV Schedule A and the address sweep.

- **D6: The firm's "Investment Partnerships" are fund positions (T5,
  fund-shaped list entries).** The 1999 table and the 2004 to 2016 listings
  carry a category the firm itself calls investment partnerships: Acacia
  Venture Partners ("health services investment partnership"), Biovest
  Partners ("medical investment partnership", "Distributed"), Chengwei
  Capital, Costanoa Venture Capital, Golden Gate Capital, Helion Venture
  Partners, Indus, Makena Capital Management and Venture TDF China.
  **Outcome:** `not_member` (the LP-stake class), because the firm's own
  label says the position is a partnership interest. A row identified as
  equity in an operating company stays in: Artisan Partners, which the 2004
  site filed under Business & Financial Services and which listed as Artisan
  Partners Asset Management in 2013, and Indus International (an enterprise
  software company, merged with MDSI into Ventyx in 2007), which the 2008
  directory filed in the same category, are judged on that evidence. Biovest
  is the 1999 table's "Biovest Partners, medical investment partnership,
  Distributed"; the 2008 page's text describing Biovest International, a
  cell-culture company, is the firm's own copy error and does not make the
  row an operating company.

- **D7: The firm's history before its first archived page (T1).** The 1999
  table lists investments back to 1970 (Measurex, Hybritech, Apollo
  Computer, Prime Computer, Tellabs), and the 2000 to 2016 pages add older
  positions the table left out (LSI Logic and Linear Technology, whose
  pages say the firm provided start-up funding). The firm
  is one continuous partnership under one name and lists them as its own
  with no disclaimer, so its own listing suffices (§1). **Outcome: IN**, and
  every classification column is judged on the same evidence as a modern row:
  no date window (PRO-137), and a round the record does not name reads
  `undetermined`.

- **D8: The site's outcome lines are dated evidence, not status.** The 1999
  table gives the firm's own outcome per company ("Acquired by Teradyne",
  "Merged into Intersolv", "Public company"). It names acquirers and dates the
  state to 1999, and it is corroboration for `status`; the column itself is
  current state and is judged per row (§6).

- **D9: The profile is sliced to the base.** The adviser is an exempt
  reporting adviser, so there is no Item 5.F; the two funds' Section 7.B
  gross assets ($3,690,455,000 together) are the sworn figure, and they cover
  exactly the vehicles this base draws on.

## Deltas (Erik's)

None confirmed before kickoff. The issue asked for three rulings; each
resolved as a derivation (incubations D3, partners' personal vehicles D2,
the from-inception entry D3). D6 is raised at close for Erik's veto because it
moves a class of the firm's own listings.

## Run-time standing rulings (dated, class-wide, flagged for review)

- **R1 (2026-09-28): the firm's address is the suite, not the building.**
  Sutter Hill is 755 Page Mill Road, Suite A-200 (filed also as "Bldg A 200"
  and, once, "775 Page Mill Road Sutie A-200"). Morrison & Foerster's Palo Alto
  office shares the street number with no suite, and its lawyers file from it
  on client Form Ds (Viz.ai and Primal Therapies, 2016). A related person
  filing from 755 Page Mill Road is a firm person only where the suite, or a
  first-party source, says so; the incubation marker of D3 reads the same way.
- **R2 (2026-09-28): the archive layer runs on Common Crawl while the
  Internet Archive blocks the machine** (Erik, 2026-09-26: Common Crawl on for
  an IA cooldown). Its captures (2008 to 2017) cite in the
  index.commoncrawl.org form; the years only the Internet Archive holds
  (2000 to 2007) land at the one scheduled rebuild (scratch/ia-eras.py).
- **R3 (2026-09-28): the 2013 to 2016 site's "Managing Director | <name>" is
  the firm's own deal attribution.** It feeds `partners_site` and is the
  reference graph for resolving a Form D name-match cluster (§5, the Accel
  rule), dated by the capture.
- **R4 (2026-09-28, Erik): Pure Storage publishes as Everpure.** Pure Storage, Inc. renamed itself Everpure,
  Inc. in January 2026 (SEC name change on CIK 1474432, ticker P). Erik, answering the open ruling at close:
  "rename pure Storage". The row keeps its slug `pure-storage`; `config.names.published` carries the brand.
