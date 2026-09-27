# Insight Partners: investor-specific decisions

Investor-specific rulings for `insight-partners`, derived from the standing
rule set in `data/collection/COLLECTION.md` §1 (T1 to T5) rather than
re-asking it. Linear issue **PRO-165**, Archetype A of PRO-87 (US venture,
SEC nexus on both sides), with the control-position addendum of T3 as the
question this run was written for.

Structure per §1's derivation protocol: **derivations** apply without
confirmation (Erik may veto any); **deltas** are Erik's to confirm, and the
run proceeds on them, flagged; **run-time standing rulings** are dated,
class-wide and flagged for review. Facts marked *(verified 2026-09-26)* were
read from the filing or page named; anything marked *provisional* is
re-derived from verified facts during the run.

---

## Derivations (T1 to T5 applied to verified facts; vetoable)

- **D1 — One registered adviser, one firm (T1, same adviser) → IN.**
  *(verified 2026-09-26, IAPD and the Form ADV)* Insight Venture Management,
  LLC, doing business as Insight Venture Partners and Insight Partners, is
  the one SEC-registered adviser (CRD 142994, SEC 801-67560), principal
  office 1114 Avenue of the Americas, 36th Floor, New York; other offices in
  London (91 Wimpole Street) and Burlingame, California (250 California
  Drive). Its amendment of 2026-09-09 reports RAUM **$92,178,934,483** across
  181 accounts, all discretionary, and **175 private funds** in Section
  7.B.(1) with $90.9B of gross assets as parsed
  (`sources/registers/adv-142994.json`). No relying adviser, no umbrella
  registration. IAPD by name returns no second Insight adviser: Insight Wealth
  Partners (Plano, CRD 153635), Capital Insight Partners (Scottsdale) and
  Insight Investment (London) are unrelated namesakes. EDGAR's **Insight
  Equity** family (Insight Equity I to III, Mezzanine I, Holdings; 14
  filers, 1400 Civic Place, Southlake, Texas) is an unrelated private-equity
  firm: `external`, first classify rule. So are Insight Holdings (DE), Inc.
  (55 East 52nd Street) and Insight Holdings Inc (Wellington, Florida).
  **Insight Holdings Group, LLC** (CIK 1305473, the home address) is the
  firm's own holding entity and its Section 13 and 16 filer since 2004.

  IN, as the firm's own vehicles: the flagship ladder Insight Venture
  Partners IV to X and Insight Partners XI to XIII with their Cayman,
  Delaware, EU, Class A and Co-Investors parallels; the Fund X and Fund XI
  Follow-On Funds; the Coinvestment Funds II and III; the Opportunities Funds
  I and II; the Continuation Funds I to IV and their AIP holding vehicles
  (plumbing, D8); the named co-investment vehicles on the ADV with no
  "Insight" in the name (Grandval, Solar Co-Invest, Empire Co-Invest, CT
  Co-Investment Opps, Sail NH), which resolve by their general partner on the
  ADV, never by name. OUT as third-party feeders (the Thrive IX Access and
  IVP Access precedent): Insight Venture Partners X Access and Insight
  Partners XIII Access (both file from 200 West Street, Goldman Sachs'
  address), and the XI and XII (iCapital) vehicles (care of Institutional
  Capital Network).

- **D2 — Strategy desks: public equities partitions, buyout does not (T1,
  strategy addendum).** *(verified 2026-09-26, EDGAR filer names and the ADV
  fund list)* The adviser runs three strategies beside venture and growth:

  1. **Public equities** (Insight Partners Public Equities Master Fund, its
     US and Cayman feeders, the Focus portfolios, IPPE Liquid, the IPPE
     co-invest vehicles; general partner Insight Partners Public Equities GP,
     LLC). A non-venture strategy with its own vehicles: desk `public`,
     partitioned (`desks.partition`). A row whose only evidence is a
     public-equities vehicle leaves as `other_desk`. Rows are still decided by
     T3 first: a listed position is a public purchase whichever vehicle holds
     it (D5).
  2. **Buyout.** Unlike Battery, Insight does have buyout-named vehicles:
     the Growth-Buyout Coinvestment Fund (2015), the XII Buyout Annex Fund
     (2021) and the XIII Growth Buyout Fund (2025). They do **not** partition
     the base, because they are annexes: they invest beside the flagship
     fund in its control deals, and the flagship holds those positions too.
     No filing says which vehicle holds which company, so a vehicle partition
     would move nothing. The buyout vehicles stay on the home desk and **the
     whole question falls to T3's transaction-level control test** (D3),
     exactly as §1 anticipates ("where one vehicle does both (Insight,
     General Catalyst)").
  3. **Fund of funds** (Insight Vision Capital II, Insight Partners Seed
     Managers Fund). Commitments to other managers' funds are LP stakes, not
     portfolio companies (T5, the fund-shaped rule). They seed no row.

- **D3 — Control positions are out, per transaction (T3, control addendum;
  Erik 2026-09-04, restated in PRO-165).** A venture entry is a minority
  position taken through a financing of the company. A transaction in which
  Insight, alone or with its co-investor group, acquires 50% or more of the
  voting equity, or which the company itself reports as a change of control
  (acquisition, take-private, LBO, majority recapitalisation), is not a round.
  The rules the grind applies, each one Battery's D3 applied to Insight's
  facts:

  1. **Control must be evidenced, and the evidence is cited.** The site
     publishes no strategy label (its stage filter is empty), so nothing on
     the listing triggers the test. The triggers are the firm's own
     announcement wording ("to acquire", "majority investment", "take
     private", "recapitalization"), the company's release, a merger proxy or
     tender-offer filing, and press. A row with no evidence of control is a
     minority position: the site listing suffices for membership (§1) and the
     row stays.
  2. **"Strategic growth investment" is not a control verdict.** Insight's
     releases use the phrase for minority and majority deals alike. It routes
     the row to the test and decides nothing.
  3. **A consortium counts as one buyer.** Where Insight is one member of a
     group that takes control (Inovalon with Nordic Capital, 2021; CoreLogic
     with Stone Point, 2021), the row is a control position whatever
     Insight's own share of the group.
  4. **The entry decides, not the later history** (the rule T3 already
     applies to a row that goes public after a venture entry, and to a SPAC
     target held through an earlier round). Where a fund held a minority
     position first and the firm bought control later (Armis: Series C in
     2019, acquisition in 2020), the row is a **member on the earlier
     round**, and the buyout is an event in its note. Where the entry was the
     control transaction and the firm later sold down to a minority, the row
     stays out: there was never a round to name.
  5. **An add-on bought by a controlled platform is part of that control
     position** (Battery's precedent, where the constituent add-ons left with
     their platforms). The site lists some of them as companies of their own.
     They leave as `control_position` with the platform named. A company
     merged into a minority-held portfolio company, with no investment of its
     own by a fund, is `not_member` (T2).
  6. Control rows are recorded as `not_member` with
     `"exclusion": "control_position"` and a citation, leave the published
     base into `excluded.json` under reason `control_position`, and are
     counted in the report. Every round-describing column is meaningless for
     them and is not authored.

  The Form D proxy (§1) is used as written: a Form D names a financing, so a
  round whose Form D names an Insight partner is a financing absent contrary
  evidence. Its absence proves nothing, since most growth rounds of foreign
  companies file none.

- **D4 — Fund money (T2).** Insight runs no scout programme and no
  accelerator that writes cheques. IGNITE (the enterprise-buyer network), the
  CIO Council, the Government Advisory Board and ScaleUp events are
  communities, not positions; an advisor's employer is never a row. Partners'
  personal angel positions are OUT. Founders' angel checks are OUT even where
  listed (Erik, 2026-09-26).

- **D5 — Venture entry and the public book (T3).** Primaries, follow-ons,
  secondaries and tenders IN, secondaries and tenders as Growth (policy
  constant). Positions that first appear as public-market purchases are OUT:
  the adviser and Insight Holdings Group, LLC (CIK 1305473) file 13F notices
  and Section 13 and 16 forms, and a holding known only from those, with no
  venture round, is `not_member`. A structured instrument bought from a
  private company (the Opportunities Funds: preferred or convertible with
  downside protection) is a financing of the company and a Growth entry (the
  Coatue D7 reading, agent, flagged); see X2 for credit.

- **D6 — Person or firm (T4).** Standard. The roster is large (140 people in
  the live Investors department) and turns over at the junior levels, so the
  Form D related-person sweep is judged cluster-first with each person's
  tenure window, and a name that matches a roster person outside their window
  is a prior-firm or next-firm seat. The Investment Team names on the 856
  company panels are the attribution map (§5): a Form D row whose named
  partner the firm itself lists on that company's panel is corroborated; one
  the map does not know is a name-match and needs its own corroboration.

- **D7 — Operating company (T5).** Standard. Fund vehicles, co-investment
  vehicles, continuation vehicles and feeders are never rows. A named-deal
  vehicle (IPPE Co-Invest (Databricks) DE, L.P.) is membership evidence for
  the company it names, judged on the entry it made.

- **D8 — Continuation funds are plumbing (T5).** Insight Partners
  Continuation Funds I to IV moved existing positions between the firm's own
  vehicles. Positions moved through them stay rows through their original
  entries with the entry stage unchanged (Lightspeed's Project Mercury,
  Creandum's Select funds).

- **D9 — The site's "Initial Investment" is a close month, and it dates the
  entry (§5, §6).** *(verified 2026-09-26 against six documented rounds)*
  Monday.com reads March 2017 (Series B announced April 2017), JFrog
  September 2018 (Series D announced October 2018), New Relic January 2013
  (announced February 2013), HelloFresh June 2014, Delivery Hero January
  2014 and Alteryx September 2014 (each the month of the announced round).
  The field is the firm's own date of first investment, at or up to a month
  before the announcement. It sets `site_invest_year` and `first_seen`, and
  it is the `entry_date` source on a decided Seed row. It carries no round
  word, so it is an anchor and never a stage label. About a third of the
  panels carry no date, and **"June 1996" is the CMS's placeholder, not a
  date**: 36 panels carry it, among them LivingSocial (founded 2007),
  Ticketmonster (2010) and Despegar, so the pull keeps it raw and dates
  nothing with it. **"Status" is the FIRM's position** (Current
  Investment / Prior Investment), never the company's state: a Prior
  Investment may be public, acquired, private or defunct, and the judge
  decides `status` from the company's own evidence.

- **D10 — The profile is sliced to the base's boundary, and says so (T1
  profile rule; PRO-165).** The flagship funds hold minority and control
  positions alike, so **no venture-only RAUM exists to report** (the Battery
  D6 shape). `aum` carries the adviser's Item 5.F figure for the whole
  adviser, and the profile history states that the track record on the page
  covers the firm's minority investments only. The public-equities vehicles
  and the fund-of-funds vehicles are left out of the fund table; the buyout
  annex vehicles are described in the funds basis.

---

## Deltas (Erik's to confirm; the run proceeds on them, flagged)

PRO-165 states that no new ruling is required, and its own five deltas
(control positions out per transaction; the profile says so; Growth entries
by design with no new stage; a very large base; a large non-US share) are
Erik's text and are applied as written. Two questions the facts raise that no
test covers:

- **X1 — A control position the firm later listed publicly or sold is still
  out, and its scale is not the firm's venture record.** Several of Insight's
  best-known outcomes began as control transactions. The rule as written
  removes them, and the report lists the largest by name so the effect on the
  published record is visible and the call can be reversed cheaply.

- **X2 — A credit-only position is not a venture entry.** Proposed under T3:
  where an Opportunities Fund position is a loan with no equity or
  convertible instrument, there is no round to name and the row is
  `not_member`. A structured equity instrument stays in as Growth (D5). The
  run records which rows this touches, if any.

---

## Run-time standing rulings

(dated, class-wide, flagged for review)

### R1 — An acquisition vehicle is control evidence on its face (2026-09-26)

The firm buys control through a holding company it forms for the deal, and
that company files Form D when it issues equity: "Revere Parent, Inc."
(Bullhorn), "Diamond Parent Holdings, Corp." (Diligent), "PFK Buyer Inc."
(PSPDFKit, now Nutrient), "KF Parent, Inc." (Keyfactor), "ELK Holdco, LLC"
(ELLKAY), "Whistler Parent Holdings, Inc." (Within3), "Sunsphere Parent,
Inc." renamed "Property Brands Parent, Inc." (Inhabit). The signature is
structural and sits in the filing itself: the issuer's address is the firm's
own (1114 Avenue of the Americas, or "care of Insight Venture Partners"),
**and** the firm's partners appear as the issuer's executive officers, often
beside the firm's general counsel, rather than only as directors. A venture
investor holds a board seat; it does not run the issuer. Where both hold, the
vehicle and the company it holds are a control position, cited to the Form D.
Where the holding company files from the company's own address with the
firm's partners as directors among other owners' directors (PDS Parent for
PDI, Great Dane Holding for Bestpass, Alert Holding for Appriss), the filing
shows a shared or minority position and decides nothing: those rows are
merged onto the company and the company is judged on its own evidence.

### R2 — A holding company is a row only through its company (2026-09-26)

A holding-company issuer is never published under its own name. Where the
company it holds is a member, the holding company is an identity merge onto
that row (`identity-merges.json`). Where the company is a control position,
the holding company takes its own control verdict, because the build applies
exclusions before merges and a merge onto an excluded canonical never runs
(COLLECTION.md §8).

### R3 — Seats that follow a sale are sale consideration (2026-09-26)

Erik's ruling of 2026-09-22 applied to three filings: the funds' 2026 Forms 3
and 4 on **Coursera** (shares received when Coursera combined with Udemy),
their 2001 filings on **eXcelon** (which bought C-bridge Internet Solutions
for stock), and Hilary Gosher's May 2026 seat on **Spring Health** (which
bought Alma). The acquirer is `not_member` with the acquired company named;
Udemy, C-bridge and Alma are the rows.

### R4 — A sale of the whole company by the firm shows its one transaction was control (2026-09-27)

The firm's own announcements call a majority purchase a "growth investment"
as readily as a minority one (EveryAction 2018, Unitrends 2013), so the entry
announcement often decides nothing. Where the record shows the firm later
**selling the company as its owner** ("Apax acquired EveryAction from Insight
Partners"; "Genstar will become the new majority shareholder ... with Insight
retaining a significant minority stake") and the firm made one investment
before that sale, that investment is what gave it the company, and the row is
a control position at medium confidence, cited to the sale. It does not reach
a company the firm held beside other owners (Aptean, Advantive), nor one
where an earlier minority round is on record (D3.4). PDI stood in that list
until the control pass of 2026-09-27 and left it on the entry announcement
itself (R5).

### R5 — The entry decides, in both directions, and the firm's round word does not (2026-09-27)

The control pass read 59 deferred rows against the firm's posts, the companies'
releases, press, the deal notes of the firm's counsel, Form D and SEC filings
(`scratch/control/findings-1.json` to `findings-4.json`). Two things follow
from D3.4.

**A minority round first keeps the row in, whatever came later.** Achieve3000
(a $9M venture investment in 2007, bought through AC HoldCo in 2015),
Illuminate Education (a $26.5M round sold to six investors in 2014, a majority
by 2018), Detectify (Series A 2018, majority 2024), Armis, Recorded Future,
Veeam and Alteryx are members on the earlier round. Marigold (Campaign
Monitor) is kept on the same reading at lower certainty: $250M in April 2014 at
a reported valuation of about $600M is a minority, the firm "declined to say if
the deal gives Insight a control position" (Fortune), and the majority is
documented only from the 2015 reorganisation. **Flagged for Erik.**

**A purchase of control is out even where the firm calls it a round.** The
firm's own words for these entries were "Series B" (Tricentis, $165M, January
2017), "Series A" (Kinnser 2012, CloudBolt 2018), "growth funding" (Keyfactor,
Within3) and "strategic investment" (iLobby, Exclaimer); the press, the
counsel's note, the company's later statement or the acquisition vehicle on
Form D says majority or acquisition. The source that states the stake decides,
and the row's basis quotes both.

PDI is ruled a control position at medium confidence on the entry announcement
("Insight Venture Partners joins Genstar and TA Associates, who will both
retain minority stakes in PDI"), three of seven directors on the holding
company's Form D, and the 2025 reports of the firm weighing the company's sale.

### R6 — What a controlled platform buys, sheds or becomes stays with the platform (2026-09-27)

D3.5 applied. **TeamViewer** was bought in 2010 by GFI Software, which the
firm controlled from 2005; the date on the firm's panel is GFI's. **ThreatTrack
Security** is GFI's security unit, sold in March 2013 to a company "wholly
owned by certain of our shareholders, including Insight" (GFI's registration
statement). **Delinea** is Thycotic, a control position from July 2015, merged
with Centrify under TPG; the firm "remained involved in the combined company as
a minority investor", which is what it kept at the sale and not a new entry.
All three are control positions.

### R7 — Money of the firm's own beside a sale is an entry (2026-09-27)

The sale-consideration ruling ends: "A firm that later backs the acquirer on
its own money is a separate, citable entry." Two rows meet it. **PayScale**:
"Insight Partners will make a new equity investment into the combined company,
rolling 100% of their Payfactors equity" (the firm's post, 2021-03-01). The row
is a member at that round, and Payfactors enters the base as a recall addition.
**SFX Entertainment**: Insight Venture Partners V subscribed for 1,000,000
common shares on 2013-04-02, six months before the IPO and weeks after selling
Beatport to SFX (the company's draft registration statement). The first
verdict, `not_member` as sale consideration, was reversed on that filing.
LivingSocial (for Ticket Monster), Coursera (for Udemy), eXcelon (for
C-bridge) and Spring Health (for Alma) show no money of the firm's own and
stay out.

### R8 — A PIPE at a de-SPAC listing is not a venture entry (2026-09-27, Erik's to confirm)

Insight Partners XII vehicles hold 12,500,000 WeWork shares from the PIPE that
closed with the BowX merger in October 2021, with a board seat (WeWork's S-1 of
November 2021; the 13F shows the position to mid-2023). The standing rules say a
fund's PIPE into a merger "is judged on its own facts". The facts here: the
instrument buys shares of the listed shell at the listing, no private round of
WeWork names the firm, and the firm's own site does not list the company. T3
asks for an entry through a round of a private company, so WeWork is not added
to the base. It is recorded as a rejected recall candidate and raised in the
report.

### R9 — Ownership evidence alone decides at low confidence, and is listed (2026-09-27)

Three control verdicts rest on a statement that the firm owned the company,
with nothing on record about the entry itself: **Digital Room** (the seller's
adviser names it "a portfolio company of Insight Venture Partners" at the 2017
sale, and one of the firm's managing directors ran it), **Academic
Partnerships** ("previously owned by Insight Partners", Wikipedia) and
**VisualLogix** (a group assembled from purchases, no round on record).
**Vertafore** is medium: CNA's filing dates the sale of control of AMS Services
to 30 November 1999, the month before the date on the firm's panel, but names
no buyer. All four are in the report's list for Erik.
