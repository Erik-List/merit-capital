# Tiger Global: investor-specific decisions

Investor-specific rulings for `tiger-global-management`, derived from the standing
rule set in `data/collection/COLLECTION.md` §1 (T1 to T5) rather than re-asking it.
Linear issue **PRO-167** (crossover manager, the second after Coatue, PRO-78, whose
`decisions.md` is the precedent this file follows).

Structure per §1's derivation protocol: **derivations** apply without confirmation
(Erik may veto any); **deltas** are Erik's to confirm; **run-time standing rulings**
are dated, class-wide and flagged for review. Facts marked *(verified 2026-09-29)*
were read from the filing or page named.

---

## Derivations (T1 to T5 applied to verified facts; vetoable)

- **D1: One registered adviser with regional relying advisers, one firm (T1, same
  adviser) → IN in every geography.** *(verified 2026-09-29, IAPD and the ADV)*
  Tiger Global Management, LLC (CRD 160318) is an umbrella registration: relying
  advisers Tiger Global Hong Kong Limited, Tiger Global Singapore Pte. Ltd., Tiger
  Global Australia Pty Ltd and Tiger Global Management Consulting Shanghai Limited
  (IAPD also lists TG India (Consulting) Private Limited among its names). Principal
  office 9 West 57th Street, 35th Floor, New York; one other office, 600 Montgomery
  Street, San Francisco. The 2026-03-27 annual amendment reports RAUM
  **$77,993,959,953** across 33 accounts ($54.2B of it for non-US clients) and 37
  private funds in Section 7.B.(1) (`sources/registers/adv-160318.json`). Schedule A:
  Charles P. Coleman III (member since 03/2001, 75% or more), Gregory Seidell
  (general counsel and CCO), Eric Lane (president and COO since 07/2021), Ira Platt
  (CFO since 03/2024). The India, China, Southeast Asia and Australia desks are the
  one adviser's relying advisers, so T1's default takes them all IN (the Accel desks
  precedent). No brand-sharing firm with its own registration exists: "Tiger
  Management" (Julian Robertson's firm, the mentor's) and the "Tiger Cub" funds are
  separate firms and never rows; the `TGM` real-estate filers on EDGAR are unrelated.

- **D2: Two strategy families under one adviser (T1, strategy desks).** *(verified
  2026-09-29, the funds' own Form Ds, the ADV fund list and tigerglobal.com/ourstrategy)*
  The firm draws the line itself: "Our public equity business includes fundamentally
  oriented long/short, long-focused and crossover strategies, targeting investments
  in high-quality, public growth companies" and "Our private equity business invests
  in early through late-stage companies". The funds' Form Ds agree: the public
  vehicles file as "Hedge Fund", the private investment partnerships as "Venture
  Capital Fund" or "Private Equity Fund".
  - **`public` desk (other_desk):** the long/short fund (master Tiger Global
    Investments, L.P., $30.2B gross assets, with the feeders Tiger Global, L.P. 2001,
    Tiger Global, Ltd. 2002 and Tiger Global II, L.P.; general partner Tiger Global
    Performance, LLC, formerly Tiger Technology Performance; the old Tiger Technology
    II / Ltd. names), the long-focused funds (Long Opportunities master and feeders
    2013; Long Opportunities II / Internet Opportunities 2015 to 2017), the crossover
    funds (Crossover Master Fund, $6.2B, with Crossover, L.P. and (Cayman), 2021), and
    the Tiger Veda affiliate (Manish Chopra's hedge fund at the firm's former 101 Park
    Avenue office, 2005 to 2016, its own 13F filer).
  - **`us` desk (home):** every private-equity vehicle: Tiger Technology Private
    Investment Partners (PIP I, 2003), Tiger Global Private Investment Partners II to
    XVII (XVII's first Form D 2026-03-20; there is no XIII), their GP entities (PIP
    Management / Performance / Partners / Holding), the PIP 1 co-investment series
    (Tiger Global PIP 1 LLC and 1-A to 1-T, 2021 on, under Tiger Global PIP
    Management), the single-deal holdcos Tiger Global FB Partners (2011) and Tiger
    Global LinkedIn Holdings (2011), and the Singapore "Internet Fund" and "Tiger
    Global <n> Holdings" vehicles that carry the Indian and Asian positions.
  - **Where the partition applies.** Per vehicle, by CIK (`config.desks`), exactly as
    the issue asks. The adviser itself files every Schedule 13D/G for all its funds at
    once, so a filing by the adviser alone cannot place a row on either desk: such a
    row is decided by T3 (D3), and it stays on the home desk until the record names a
    public-desk vehicle as its only holder. A private round whose record names no
    vehicle is the home desk's, because the firm's own page says its private-equity
    business is the one that invests in private companies. The one case the two tests
    decide differently is a public-desk vehicle that bought into a private round: that
    is delta X1.
  - **The profile's `aum` is the private-equity desk's floor, never the umbrella
    RAUM** (§1 strategy desks): the sum of the PIP vehicles' Section 7.B gross asset
    values, master funds only, labelled a floor, with the $78.0B RAUM in the basis.

- **D3: A 13F, 13G or 13D line is a public-market holding, not a venture entry
  (T3; Coatue D3 unchanged).** The standing rule decides the crossover boundary: a
  position that first appears as a 13F holding or a post-IPO 13G, never through a
  venture round, is `not_member`. The 13F layer (`sources/edgar/13f-holdings.json`,
  99 filings 2003 to 2026, 1,098 issuers) is used for (a) public-status
  corroboration of a member, (b) the first public quarter, and (c) the recall
  trigger: a 13F issuer that listed after 2003, when the firm began private
  investing, is checked for a pre-IPO round and admitted only on that round's
  citation (an IPO prospectus naming Tiger among the holders, a round naming the
  firm). The largest 13F positions with no venture round are membership traps in
  `config.verify.not_members`. **A 13F-only or 13G-only row leaves the base as
  `not_member`, never as `other_desk`**: the holding vehicle is unknowable from an
  adviser-level filing (D2), and what decides the row is the entry.

- **D4: The firm's "Our Story" list is evidence of a position, not of a venture entry
  (the site-listing rule plus T3).** *(verified 2026-09-29)* The live page names 18
  companies ("Facebook, LinkedIn, JD.com, Flipkart, Spotify, Uber, Nubank, Stripe,
  Palantir, Toast, Snowflake, Mercado Libre, and AI leaders such as OpenAI,
  Databricks, Waymo, ByteDance, Cerebras, and Scale"), and the firm's disclosure page
  says the companies named "represent companies in which Tiger Global has invested"
  and that it "may be long, short, or not currently own" them. A listing suffices for
  a position; for a crossover firm it does not show the position was private, so each
  of the 18 still passes T3, exactly as Coatue's Hut 8 did (Coatue R1). A name whose
  only position was bought on the market (the likely case for Mercado Libre, listed
  2007) is `not_member` with the page cited.

- **D5: Fund money (T2).** Chase Coleman's and the partners' personal holdings and
  family offices are not fund money; Lee Fixel's investments from 2019 on are
  Addition's, John Curtius's from mid-2022 Cedar's, Scott Shleifer's from 2024 his own
  (D7). Third-party feeders are `external` and hold no positions of their own: J.P.
  Morgan's Tiger Global PIP XV Private Investors, the iCapital access funds, the "CC -",
  OCA, PE Premier, Sage-Mtn, PPB, Lido Advisors, BCA Select and HCP series, and EPQ's
  PIP XI PS vehicle. The firm runs no scout programme or accelerator.

- **D6: Venture entry (T3).** The private-equity desk's entries are primaries (from
  seed to pre-IPO, most often leading or joining growth rounds), and secondaries: the
  2009 to 2011 purchases of Facebook and LinkedIn shares through the single-deal
  holdcos are secondaries in private companies, so they are venture entries, Growth by
  the policy constant. A position entered at or after a listing (a PIPE, a convertible
  into a listed company, shares bought in the IPO) is not a venture entry: Coatue R1,
  still open for Erik, is applied the same way here and flagged. The firm makes
  minority investments; a control transaction, if one surfaces, is judged on the
  control-position addendum.

- **D7: Person or firm (T4).** Standard, and dated against the curated roster
  (`sources/wayback/partner-roster.json`): Chase Coleman 2001 on; Scott Shleifer 2002
  to 2023 (stepped down as head of private investing in January 2024, senior adviser
  since); Lee Fixel about 2006 to early 2019 (Addition after); Feroz Dewan 2003 to 2015
  (public desk); John Curtius to June 2022 (Cedar after); Alex Cook about 2017 to July
  2024; Griffin Schroeder, Evan Feinberg and Eric Lane current. The firm seldom takes
  board seats, so the roster-name Form D sweep carries little recall (226 accessions,
  82 issuers, most of them homonyms of common names such as Charles Coleman and Alex
  Cook); every match is judged cluster-first and needs affirmative corroboration.

- **D8: Single-deal and co-investment vehicles are vehicles, not rows (T5, T1).** The
  FB Partners and LinkedIn Holdings holdcos, the PIP 1 series and the Singapore
  holding companies are the firm's own vehicles (IN under T1), and a company they hold
  enters on the evidence that names the company, at the stage of that entry. They are
  never rows.

- **D9: The firm publishes no portfolio list, so the Thrive shape applies (§5, "When
  the investor publishes no list at all").** *(verified 2026-09-29)* tigerglobal.com
  has five pages and a login; Common Crawl holds no capture before late 2020 and none
  with a list before the 2026 redesign; the Internet Archive is in a machine-wide
  cooldown at kickoff and is checked after it. The `site_listing` class is 18 names
  (D4). The base rests on the filings (13D/G subjects, the Form D sweep), the exit-side
  EDGAR full-text sweep (IPO prospectuses name the firm among principal holders), the
  Wikipedia insource sweep, and a Google News press sweep run as a primary layer
  (every press-evidenced row lands as cited `web`), with the recall probe's
  parametric enumeration by year, sector and country load-bearing.

- **D10: The roster is curated, not crawled** (D7's list; config `roster._note`).

- **D11: Operating company (T5).** Standard. Token-only positions, if any surface,
  follow the token rule; the firm's crypto positions found so far are equity in
  operating companies.

- **D12: "Late Stage" is Growth (§6).** The issue's "entries map to the existing
  taxonomy, mostly Growth and Late Stage" reads onto the one taxonomy: Growth means
  Series B and everything later, so a late-stage or pre-IPO entry is Growth; no new
  stage (Erik, 2026-09-26).

---

## Deltas (Erik's to confirm; the run proceeds on them, flagged)

- **X1: A public-equity vehicle's purchase in a private round.** T1's strategy-desk
  rule places the row on the other desk (the vehicle is a public-equity fund); T3 reads
  a private round as a venture entry. The issue asks for the partition per vehicle, so
  the run applies it: where the record (a prospectus footnote, a joint 13D/G, a Form
  3/4) names only public-desk vehicles as the pre-IPO holder, the row is
  `other_desk`; where it names a PIP vehicle, or no vehicle at all, it is the home
  desk's. Each such row is listed in the report.

- **X2: The firm's "notable examples" include names that may never have been private
  positions.** Mercado Libre is the likely case (D4). The run rules each on T3 and
  lists the result; Erik decides whether the firm's own naming should keep such a row
  in regardless.

---

## Run-time standing rulings

(dated, class-wide, flagged for review)
