# ICONIQ Growth: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to ICONIQ Growth
(slug `iconiq-growth`, display name **ICONIQ Growth**, "ICONIQ" in notes).
The judge cites these rulings per line. Written at kickoff 2026-09-29 (PRO-168)
under the derivation protocol of COLLECTION.md §1: **derivations** (a standing
test applied to verified facts; no confirmation needed, vetoable), **deltas**
(Erik's), and **run-time standing rulings** (dated, class-wide, flagged for
review). Facts marked *(verified 2026-09-29)* were read from the filing or page
named.

**The structural fact of this run:** the investor is one strategy desk of a
wealth manager. ICONIQ Capital, LLC advises $117.5B, most of it client money;
the growth desk is the part of that adviser whose funds sit under the ICONIQ
Strategic Partners general partners. The same adviser files the 13F for every
account it manages and runs a second family of deal-by-deal vehicles for its
clients (ICQ Investments, ICQ Opportunities). So the question this book turns
on is not "is this position ICONIQ's" but "did a growth-desk vehicle hold it".

---

## Derivations (T1 to T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: One adviser, umbrella registration (T1).** *(verified 2026-09-29,
  IAPD and the ADV)* Every ICONIQ vehicle is advised by **ICONIQ Capital, LLC**
  (IAPD **CRD 159198**, SEC-registered; principal office 50 Beale St., Ste 2300,
  San Francisco; other advisory office 360 Park Ave South, New York, 48 advisory
  staff; other-than-annual amendment 2026-08-12, `sources/registers/adv-159198.json`).
  Item 5.F RAUM **$117,526,862,202** (discretionary $85.8B over 698 accounts,
  non-discretionary $31.7B over 953; 380 high-net-worth clients hold $10.8B,
  353 pooled vehicles $82.6B). It files as an umbrella: IAPD lists its relying
  advisers as ICQ Opportunities GP, ICQ Management, ICQ Ethos GP, ICQ CS GP,
  ICQ CPE I GP and ICONIQ Strategic Partners II GP and III GP
  (`sources/registers/iapd-search.json`); other business names ICONIQ
  Strategic Partners, ICONIQ Strategic Management, ICONIQ Capital Group.
  Section 7.B lists **351 private funds** with $99.9B of gross assets. IAPD's
  only other "ICONIQ" firm is **IPI Partners, LLC** (CRD 284694, formerly ICONIQ
  DC Management, LLC), the data-centre joint venture, now under its own name:
  **external**. Every EDGAR filer named ICONIQ (204) or ICQ (107) is the firm's
  own vehicle or a feeder into one; no namesake exists.

- **D2: Two strategy families under one adviser (T1, strategy desks) → the
  growth desk only.** *(verified 2026-09-29, the ADV's general-partner field
  per fund)* Where one adviser covers several strategies, the desk runs on
  strategy (COLLECTION.md §1, Erik 2026-09-04), resolved per vehicle. The ADV
  names each fund's general partner, and that field partitions the 351 funds
  exactly:
  - **Growth desk (home, `growth`)**: the **81 funds whose general partner is
    an ICONIQ Strategic Partners GP**, gross assets **$32,172,497,450**, no
    feeders among them: the flagship funds ICONIQ Strategic Partners I (2013)
    to VII with their -B parallels (VIII filed Form D in December 2025 and is
    not yet on the ADV), the numbered co-invest series (D4), the Co-Invest FO /
    FO-B / -C / -T vehicles, and eight **ICQ Holdings** LLCs that the ADV
    places under ICONIQ Strategic Partners II GP despite the ICQ prefix.
  - **Client platform (`platform`, other_desk)**: everything under ICQ BB GP
    (the wealth platform's portfolios: Glide Path Solutions, Absolute Return,
    Fixed Income Plus, Emerging Markets, Real Assets, Secondaries, BB
    Holdings), ICQ Management and ICQ Opportunities GP (the client deal
    vehicles, D3), ICQ CPE I GP and the Co-Investment Portfolio GPs (client
    private-equity programmes), ICONIQ Capital as general partner of the
    **ICONIQ Access** vehicles (client access to outside managers), ICQ CS
    (credit), ICONIQ Residential and ICQ Ethos (real estate) and the ICONIQ DC
    funds (data centres).
  - **Umbrella (`umbrella`)**: ICONIQ Capital, LLC and ICONIQ Capital Group
    file the 13F and Schedule 13D/G for every account at once, so a filing by
    them never says which desk holds the shares; such a row is decided by T3
    and T2 on its own evidence, never by desk (the Coatue D2/D3 shape).
  **Outcome:** the base is the growth desk. Platform rows leave the base as
  `other_desk` (`config.desks.partition: ["platform"]`), preserved in
  `excluded.json`. Precedents: Coatue D2 (one adviser, public and private
  families split by vehicle), the strategy-desk addendum of 2026-09-04.

- **D3: Client deal vehicles are client money (T2).** *(verified 2026-09-29,
  the firm's own Form Ds and the ADV)* **ICQ Investments 1 to 26** (Form Ds
  2012-01 to 2015-04; ICQ Investments 1, 2, 3, 5 and 6 sold $0.3M to $43M to
  10 to 147 investors between January and December 2012, **before ICONIQ
  Strategic Partners, L.P. first sold on 2013-06-07**) and the coded **ICQ
  Investments <code>** and **ICQ Opportunities <code>** vehicles (2014 to 2026)
  sit under ICQ Management and ICQ Opportunities GP, the client platform's
  relying advisers, not under a growth GP. They are how ICONIQ's clients take
  a direct position in one company. **Outcome:** a position held only through
  them, or only in a client's own account, is not a growth-fund position and
  the row is `not_member` (T2: "OUT where the only connection is a person, a
  program listing or an association"; PRO-168's delta 2). Where a growth fund
  came in later, the row is a member and **its entry is the growth fund's
  first check, never the client-era check** (T2's Point Nine precedent: Clio,
  Westwing, Humanity). This is the reading for the 2012 deals the press
  credits to "ICONIQ Capital" before the first growth fund (Flipkart's Series
  D of August 2012 is the named case).

- **D4: The growth desk's co-invest series are growth-desk vehicles (T1, T2,
  T5).** *(verified 2026-09-29, the ADV and Form D)* About 60 single-deal
  vehicles named **ICONIQ Strategic Partners [N] Co-Invest, L.P., Series
  <code>** (codes FK-G, FK-H, U, AB, DD, KC, ST, TS, 1PW, BD, N, NS, RM, DB,
  OR, PR ...) sit under the growth GPs; the ADV reports 1 to 408 beneficial
  owners each, and several are 77% to 100% owned by the adviser's related
  persons (blocker and aggregator series of the funds themselves). T1's
  default admits co-invest and single-name vehicles as the firm's own; T2
  admits a position a fund of the firm held; T5 keeps the vehicle itself out
  of the base. **Outcome:** a company such a series holds is a member on the
  evidence that names the company, at the stage of that entry; the series
  never names a company on its own. **The code decode is corroboration, not a
  label** (the 8VC SPV-decode rule): a code whose letters, round and Form D
  date line up with a documented round dates the growth desk's entry (FK-G
  and FK-H read as Flipkart's Series G and H; U as Uber; 1PW as 1Password),
  and an unresolved code stays unresolved. Precedents: Coatue D5, 8VC's
  decode (`8vc/sources/edgar/spv-decode.json`). The one open reading is X6.

- **D5: A 13F, 13G or 13D line is a public-market holding, not a venture
  entry (T3).** *(verified 2026-09-29, `sources/edgar/13f-holdings.json`: 54
  13F-HRs, 2013-Q1 to 2026-Q2, 574 issuers)* The adviser's 13F mixes the
  growth funds' listed winners (Snowflake at up to $8.5B, Procore, Datadog,
  ServiceTitan, Figma, Netskope, Uber, Robinhood, BlackLine, GitLab) with
  client-account holdings (index ETFs, gold trusts, Nvidia, Alphabet,
  Microsoft, Shopify, DoorDash, Blue Owl, whose 6% stake in ICONIQ itself dates
  from 2020). **Outcome** (Coatue D3, unchanged): the layer never admits a
  member. It corroborates `public`, dates the first public quarter, and
  triggers the recall check for every issuer listed after 2013, admitted only
  on a cited pre-IPO growth-fund round. The largest positions with no venture
  round are membership traps in `config.verify.not_members`.

- **D6: A growth fund's own ownership filing is fund-filing evidence
  (evidence rules).** *(verified 2026-09-29, EDGAR submissions)* ICONIQ
  Strategic Partners, L.P. (CIK 1575779) and its successors (VI: 1864753, VII:
  1924162) file Forms 3 and 4 and Schedule 13G themselves. A filing by a
  growth-desk entity on a company is membership evidence of class
  `fund_filing` (a fund of the firm held the shares); the entry round still
  comes from the round, and the sale-consideration check applies as always
  (COLLECTION.md §1).

- **D7: Venture entry (T3).** ICONIQ Growth's entries are growth rounds,
  secondaries and tenders (Growth by the policy constant) and, since about
  2023, some Series A and B leads (Pinecone, Rillet, TinyFish). Control
  positions leave the base under the control addendum (the CSL Group purchase
  of 2016, "trio of investors acquire CSL", is the named candidate if it
  surfaces). A PIPE at a SPAC merger is judged on Coatue's R1 reading (open
  for Erik there). No sponsor promote is known.

- **D8: Person or firm (T4).** Standard: a seat is dated against the person's
  firm at filing time. Three classes here: the general partners who came from
  operating jobs (Rob Bernshteyn at Coupa, Amit Agarwal at Datadog, Kamran
  Zaki at Adyen, Alex Gorsky at Johnson & Johnson) filed as officers of their
  companies before joining, which are not the firm's seats; the wealth side's
  founders (Divesh Makan, Michael Anders, Chad Boeding until 2018) sit on
  filings as client advisers, so their seat alone is not a growth-fund
  position; and the nine advisory-board members on `/growth/approach`
  (Aditya Agarwal, Eli Collins, Jeff Rothschild, Keith Adams, David Entwistle,
  Chris Degnan, Dennis Lyandres, Robert Alexander, Wafaa Mamilli) are never on
  the roster. A seat alone, with no round, post, listing or fund filing naming
  the firm, is `not_member` (Erik's BCV ruling, 2026-09-28).

- **D9: Operating company (T5).** ICONIQ Impact's Co-Labs are philanthropy
  (grants to nonprofits, `/impact/portfolio`): not investments, no rows. The
  real-estate and data-centre assets (The Newbury Boston, the IPI data
  centres) are platform or external holdings, not rows.

- **D10: The archive is Common Crawl first (COLLECTION.md §5, outage
  rule).** *(verified 2026-09-29)* The Internet Archive is in a machine-wide
  cooldown until 06:38 UTC and index.commoncrawl.org refused connections, so
  the archive layer reads Common Crawl's static cluster.idx
  (`scratch/cc-cluster.py`: 42 crawls 2012 to 2026, 1,851 captures on the three
  hosts). **iconiq.com belonged to an unrelated agency until ICONIQ took the
  domain in 2025** ("our-work", "mind-melt"), so its captures before 2025 are
  skipped. iconiqcapital.com was a one-page site from 2013 to 2019; the growth
  portfolio appears at iconiqgrowth.com/companies/ from late 2020, with a
  per-company page for every holding in the 2022 crawls. The archive can date
  listings from 2020 on; the 2013 to 2019 book rests on the live list, the
  filings and the press, and the Wayback pull runs later in the run.

- **D11: The roster is curated, not crawled.** The live site has no
  investment team page and Common Crawl holds none. The roster is built from
  the firm's own fund Form Ds (Divesh Makan 2012 on, Will Griffith, Kevin
  Foster), its general-partner welcome and interview posts (Roy Luo 2023,
  Kamran Zaki 2024, Rob Bernshteyn 2024, Alex Gorsky 2024, Amit Agarwal and
  Tengbo Li 2025, Murali Joshi 2026, Yoonkee Sull and Caroline Xie 2022),
  Wikipedia (the four founders; Will Griffith from TCV in 2013) and press-dated
  tenures, one basis line per person.

- **D12: The site's "IPO/Acquired" tag is the firm's exit marker, not a
  status.** 53 of 172 grid rows carry it. The judge decides `status` from the
  company's own evidence.

---

## Deltas (PRO-168's five, verified at kickoff; the run proceeds on them)

- **X1 (PRO-168 delta 1): the investor is the growth desk, not the family
  office.** Verified as written: the ADV's general-partner field splits the
  351 funds into the 81 growth-desk funds and the client platform (D2).
- **X2 (delta 2): client money is not fund money.** Verified as written for
  client accounts and for the ICQ Investments and ICQ Opportunities vehicles
  (D3). How the delta reads for the growth desk's own co-invest series is X6.
- **X3 (delta 3): 13F holdings mix client assets and fund positions.**
  Verified (D5). The layer values listed rows and separates entries; it adds
  no member.
- **X4 (delta 4): the profile is sliced to the desk.** The growth desk's own
  funds carry $32,172,497,450 of gross assets (81 funds, 2026-08-12 ADV); that
  sum is the `aum` floor, and the umbrella's $117.5B RAUM stays in the basis.
- **X5 (delta 5): no new stage** (Erik, 2026-09-26). Entries read Growth where
  the round is B or later; the Seed cohort is expected to be thin.
- **X6 (new, for Erik): which co-invest counts as a client co-invest.** Read
  here as: the client platform's deal vehicles (ICQ Investments, ICQ
  Opportunities) are client co-invests and out; the growth desk's own
  co-invest series (under the growth GPs, D4) are fund vehicles and in, even
  where their limited partners are ICONIQ clients, because so are the flagship
  funds' limited partners. A row whose only growth-desk evidence is a
  co-invest series, with no flagship fund documented in the round, is kept and
  flagged `boundary`, and the report counts them, so the reading can be
  reversed as a class.

---

## Run-time standing rulings

(dated, class-wide, flagged for review)

- **R1: control positions are out (COLLECTION.md 1, control positions;
  2026-09-29).** A transaction in which ICONIQ, alone or with its co-investor
  group, took control is not a venture entry; the row leaves as `not_member`
  with exclusion `control_position`. Applied to **BlackLine** and its
  acquisition vehicle **SLS Breeze Holdings** (Silver Lake and ICONIQ
  acquired a controlling interest on 2013-09-03, BlackLine's S-1),
  **Truckstop.com** ("Internet Truckstop Group, LLC's sale to ICONIQ Capital,
  LLC in April 2019", Sagemount's disclosure in Independence Holdings' S-1;
  press: a majority stake) and **GoFundMe** (June 2015: the founders sold a
  controlling stake to the round's investor group, led by Accel and TCV,
  ICONIQ in the group; TechCrunch 2015-06-24). *Flagged for Erik:* on
  GoFundMe ICONIQ's own stake was a minority inside the controlling group;
  the rule's words ("with its co-investor group") put it out, and the same
  reading would reach Accel's GoFundMe row. **Not control:** QGenda (June
  2020: Francisco Partners kept the majority; the Covetrus fairness opinion's
  precedent table lists ICONIQ as the "acquirer" of the stake only).
- **R2: a position bought at or after the listing is not a venture entry
  (T3; 2026-09-29).** **Tencent Music** (and its 2022 per-company page, TME): the III Co-Invest TME series
  filed its Form D on 2018-12-14, two days after the NYSE listing of 2018-12-12.
  *Open for Erik under the same test:* **GoodRx** is on the firm's list of
  2020 new investments and listed on Nasdaq on 2020-09-23; no round, filing
  or release dates ICONIQ's entry, and the umbrella 13F carries Class A shares
  from 2020-09-30 while pre-IPO holders were reclassified into Class B. Kept
  as a member with the entry uncited; the T3 ruling (no round named and
  partnered after the IPO) cannot be established either way.
- **R3: signed sales and pending listings (COLLECTION.md 8 applied;
  2026-09-29).** A definitive agreement that has not closed keeps the row
  private at the agreed price: **Airtable** (Bending Spoons, equity value
  about $2.25B), **Miro** (Bending Spoons, about $1.79B), **Altruist**
  (Vanguard; terms undisclosed, the press figure $4.6B, medium confidence),
  **Fin, formerly Intercom** (Salesforce, about $3.6B). A company that has set
  IPO terms but not listed stays private at its last round: **Oura** ($11B
  Series E, October 2025).
- **R4: a majority recapitalisation by a new sponsor does not end private
  status (2026-09-29).** **Smartling** (Vitruvian Partners' majority growth
  investment of September 2026, buying Battery Ventures' position): the
  company goes on under its own management and reads `private`, as Redpoint's
  Azul Systems does after its Vitruvian recapitalisation.
- **R5: renamed panels and renamed companies (2026-09-29).** The grid's
  **Nintex** panel links to skuid.com: it is the Skuid panel, renamed after
  Nintex bought Skuid in December 2023 (Insight's R10 reads it the same way);
  merged into `skuid`. **Intercom** renamed itself **Fin** in 2026: one row,
  published as Fin with the old name in the note.
- **R6: one-word Wikidata countries (COLLECTION.md 5; 2026-09-29).** Each
  non-US Wikidata country on a one-word name was checked against the
  company's own record. Confirmed and recorded with source `wikidata`: Adyen
  NL, Flipkart IN, Legora SE, Monzo GB, Wolt FI, Helsing DE, Wealthsimple CA.
  Corrected to US (wrong-entity joins or a foreign founding office): Coast,
  Dataiku, Fireblocks, Guild, Hippo, Miro, Nevis, Panther, Recharge, Uber,
  Zoom.


