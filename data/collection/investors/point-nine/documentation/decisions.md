# Point Nine — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Point Nine (slug
`point-nine`, display name always **Point Nine**; "Point Nine Capital" until
the 2019 move to pointnine.com). The judge cites these rulings per line.
Written at kickoff 2026-09-26 (PRO-101) under the derivation protocol of
COLLECTION.md §1: **derivations** (a standing test applied to verified facts,
no confirmation needed, vetoable), **deltas** (Erik's), and **run-time standing
rulings** (dated, flagged for review). PRO-101's own delta list carried no
ruling question; every fact below was verified at kickoff, and the sources are
on disk under `sources/`.

**The structural fact of this run:** Point Nine is a Berlin seed firm whose
own list mixes three books that the membership definition separates: the
funds' book since late 2009 (Team Europe Ventures Fund, renamed Point Nine
Capital Fund I in 2011, then Funds II to VII and the Annex follow-on funds),
the founders' personal angel investments of 2008 to 2011 that the firm's
site presents as its own ("Since 2008, we've invested in 10–12 early-stage
startups per year"), and, from 2025 on, a few non-seed positions (an LP stake
in Project Europe, a Series G participation in Anthropic). Its SEC footprint
is fund-side and live: two exempt reporting advisers file Form ADV with
Section 7.B, and the fund KGs file Form D for their US investors. Its
portfolio is mixed EU and US, so Form D visibility is per row, not absent.

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1 — The firm (T1, same adviser).** Point Nine = the Berlin firm managed by
  **Point Nine Management GmbH** (HRB 136626 B, Amtsgericht Charlottenburg,
  entered 2011-09-12; SEC exempt reporting adviser, CRD 306640) and **Point
  Nine Management II GmbH** (HRB 235327 B, 2021-11-05; ERA CRD 319531, SEC
  802-126152), both at Torstr. 19, 10119 Berlin, both controlled by Christoph
  Janz and Pawel Chudzinski (ADV Schedule A, annual amendments of 2026-03-25:
  partners since 09/2011 and 09/2021 respectively; Bounce GmbH and RJ
  Beteiligungsgesellschaft mbH as shareholders; Louis Coppey and Ricardo
  Sequerra Amram partners of the second adviser since 09/2021; Point Nine
  Holding GmbH & Co. KG, 2021-09-13, its managing limited partner). The
  verified vehicle set (North Data / Handelsregister, IAPD, EDGAR, read
  2026-09-26; `sources/registers/entities.json`):
  - **Fund I** — Point Nine Capital Fund I GmbH & Co. KG, HRA 43145 B,
    **entered 2009-10-28 as Team Europe Ventures Fund GmbH & Co. KG** (general
    partner Team Europe Ventures Verwaltungs GmbH; 2 individual and 11
    corporate limited partners admitted 2009-12-10), **renamed 2011-09-01**,
    general partner changed to Point Nine Verwaltungs GmbH 2014-11-18; ADV 7.B
    fund 805-3438427883, gross assets $1,257,266 (2026). The firm names it
    itself: "Point Nine, operating as Team Europe Ventures Fund at the time,
    invested in Lieferheld's first financing round" and "Delivery Hero today
    accounts for about 50% of the total portfolio value of Point Nine Fund I"
    (writing.pointnine.com, 2017-06-30); P9 V is "our fifth fund"
    (2020-09-22).
  - **Fund II** (HRA 45915 B, 2011-11-24; 7.B $417,390,961; Form D CIK
    1795226), **Fund III** (HRA 50098 B, 2014-10-09; $540,521,332; CIK
    1650344), **Fund IV** (HRA 52897 B, 2016-11-22; $287,170,418; CIK
    1795228), **Fund V** (HRA 55932 B, 2019-04-09; $217,076,134; CIK 1790315),
    **Fund VI** (HRA 59489 B, 2021-12-10; $202,325,389; CIK 1904258), **Fund
    VII** (HRA 63803 B, 2025-01-09; $246,708,000; CIK 2066605).
  - **Annex** (HRA 51916 B, 2016-02-19; $36,247,234; CIK 1677337) and **Annex
    II** (HRA 59488 B, 2021-12-10; $143,313,107; CIK 1904244): follow-on funds.
  - **Co-Invest I–VII** (team co-investment KGs, one per fund; Co-Invest I
    entered 2009-10-23 as Team Europe Ventures Investment Board GmbH & Co. KG,
    renamed 2012-04-04), **Annex Team** and **Annex II Team** KGs, **Point Nine
    Team VII eGbR** (2025-03-19).
  - Single-company vehicles: **Point Nine VI Project Europe GmbH** (HRB 278314
    B, 2025-08-19) and **Point Nine Annex HappyCo GmbH** (HRB 288501 B,
    2026-06-18).
  - Offices and service entities: Point Nine Verwaltungs GmbH and Verwaltungs
    II GmbH (general partners), Point Nine France SASU, Point Nine Portugal
    Lda (Lisbon, 2022-08-17), Point Nine Inc. (the US entity on the second
    adviser's Item 7.A, no CRD or CIK).

  All under one team and two advisers under common control → **IN**:
  primaries, follow-ons and secondaries from any of these vehicles.
  Precedent: Cherry D1 (Opportunities, Select and Growth sleeves under one
  team), Creandum's Select funds and SPV.

- **D2 — The founders' angel books (T2 fund money, T4 person or firm).**
  Christoph Janz invested as a business angel with his own money from 2008
  until Point Nine formed in 2011, and the firm's own posts say so: "When I did
  my angel investments in 2008–2011 I typically invested $50–150k per company.
  In some cases, I was the only investor (in case of Zendesk…)" and "I was an
  angel investor for about three years before teaming up with Pawel to start
  Point Nine" (2019-04-08); "my investments in Zendesk in 2008, Clio in 2009"
  (2023-01-27); "involved with Westwing as an angel investor from day one"
  (2018-10-22); "first as individual angel investors, then with Point Nine"
  (2020-09-22). The live list carries those rows as Point Nine investments with
  no distinction, dated from 2008. **Derivation: a position a founder took
  personally is OUT unless a firm vehicle held it** (Cherry D2, Erik
  2026-09-04: founder-angel positions out unless a Cherry vehicle held them;
  T2 "partners' personal angel books"; the Menlo partner-carried ruling, Erik
  2026-09-17, for a firm listing a position its money did not make). IN where
  Team Europe Ventures Fund / Fund I or a later Point Nine vehicle held it,
  **entering at the round the fund itself bought into** (a later Point Nine
  follow-on into an angel-backed company enters at that round; the angel check
  does not set the entry). Evidence per row: the register (Fund I's disclosed
  participations: asgoodas.nu and Cibando in the 2011 accounts; the shareholder
  lists of asgoodasnew, DaWanda and Digital Turbine GmbH, i.e. Fyber, name it),
  the firm's own posts naming the fund, press at the time naming Team Europe
  Ventures or, from the June 2011 rebrand, Point Nine Capital. Applies to every
  row whose firm-stated year is 2008 to 2011 (25 rows on the live list, plus any
  archive-only row of that era). A later press line or the firm's own list
  calling a pre-2011 founder check "Point Nine" is a name-match: the firm did
  not exist.

  **What the record says, verified at kickoff** (`sources/web/row-evidence.json`,
  `sources/web/founding-era.json`). TechCrunch separated the two books on the
  day of the rebrand (2011-06-09): "To date, the fund … has invested in over 10
  startups, including inFakt, Lieferheld, Madvertise, MisterSpex, myGengo and
  SponsorPay", while Janz's "investments include Zendesk, FreeAgent Central,
  Clio, and Propertybase". Janz's own blog at the start of 2012: "from now on
  I'm going to make all new investments via Point Nine Capital", listing his
  personal 2011 checks (Lieferheld and Delivery Hero, Server Density, Fundly,
  Westwing, Shiftplanning, FinanceaCar, Vend, ChicChickClub, Unbounce,
  Cibando). Most of those companies ALSO carry a fund position, which is what
  makes them members: Westwing (the fund in the second round, deutsche-startups
  2011-09-04), Unbounce (the December 2011 round with "Christoph Janz & Point
  Nine Capital"), Clio (the fund backed it in 2011 and was a follow-on investor
  in the 2014 Series C), Vend (Point Nine II), Cibando and myGengo (Point Nine
  seeds, TechCrunch), ShiftPlanning (the 2012 Series A led by Point Nine),
  Delivery Hero (the fund in Lieferheld's 2010 seed). Janz's own account of
  the fund (2012-03-21): "In 2009 TEV raised a ~€6M fund, which was managed by
  Pawel and invested in 24 companies. 16 out of these 24 companies were
  co-investments with myself".

  **The firm's own list disclaims six rows in its own words**, which settles
  them under the Menlo rule (Erik 2026-09-17: a listing suffices unless the
  firm itself disclaims the position) as well as under T2: FreeAgent ("one of
  Christoph's first angel investments"), Geckoboard ("a private angel
  investment by Christoph prior to the formation of Point Nine"), Momox ("one
  of Christoph's angel investments before starting P9"), Propertybase ("One of
  Christoph's angel investments before P9"), samedi and Server Density ("one of
  Christoph's angel investments prior to Point Nine"), all read off
  pointnine.com/companies on 2026-09-26. **Zendesk** is the seventh: its card
  is silent, but the firm's blog calls it "one of Christoph's first angel
  investments" (2014-07-10), his $500K check was in June 2008, a year before
  the fund existed, and "at that stage [the 2009 Series A] Janz's involvement
  in the company came to a close". Each of the seven is searched once more for
  a later fund round before its verdict writes; none was found at kickoff
  (Geckoboard's 2012 round names Janz among the individuals).

- **D3 — Team Europe is a separate firm (T1).** Team Europe (the Berlin company
  builder of Lukasz Gadowski and Kolja Hebenstreit) sponsored the 2009 fund:
  Team Europe Holding I GmbH & Co. KG was a partner of Team Europe Ventures
  Fund until 2011-08-31 and Team Europe Ventures Verwaltungs GmbH its general
  partner until 2014-11-18. The positions Team Europe held itself (its
  incubations and its own vehicles, e.g. Team Europe Ventures Limited, a
  selling shareholder of trivago in Expedia's 2012 share purchase agreement)
  are **external**; only the fund's positions count. Kolja Hebenstreit (Team
  Europe and Delivery Hero co-founder) is a Point Nine Venture Partner today:
  his personal and Team Europe seats are not the firm's (T4).

- **D4 — Advisers and board partners (T2).** Board partners and portfolio
  advisers (Renaud Visage and Andreas Bodczek from 2018, Zack Urlocker from
  2019, Michael Wolfe and Kolja Hebenstreit as Venture Partners today) bring
  their own angel books ("an angel investor in around 20 startups (including
  our portfolio companies Algolia and Sqreen)", 2018-07-20): those positions
  are personal, **OUT** unless a Point Nine vehicle held the company. No scout
  or accelerator programme was found on the site, the blog or the archive
  (re-checked in the recall probe).

- **D5 — Instruments (T3).** Standing rules verbatim: primaries, follow-ons,
  secondaries and tenders IN, secondaries and tenders as Growth; post-RIA
  public purchases out; LP stakes out. **Anthropic** is IN as a Growth entry
  on its Series G (February 2026): "we participated in Anthropic's Series G…
  when our portfolio company Vercept was acquired by Anthropic… we got the
  chance to not only roll over our position but double down" (2026-05-26). The
  rolled Vercept shares alone would be sale consideration (§1, Erik
  2026-09-22); the new money in a priced primary round is a separate, citable
  entry. Vercept stays a member on its own round, `acquired` by Anthropic.
  The site's "Later-stage" label collapses onto Growth.

- **D6 — Plumbing vehicles (T5).** The Annex funds are follow-on vehicles and
  the Co-Invest and Team KGs invest beside the flagship funds: a position held
  or added through one is a follow-on, the entry stage stays the first fund
  entry; a new commitment made only through an Annex enters at that stage
  (Growth when the round is B or later). Point Nine Annex HappyCo GmbH is a
  single-company follow-on vehicle into HappyCo, a member already. Precedent:
  Creandum Select and SPV TR, Cherry D6.

- **D7 — Project Europe is a fund, not a company (T5).** The live list shows
  "Project Europe" (London, Pre-seed, 2025). Project Europe is a €10 million
  fund launched in March 2025 by Harry Stebbings with 20VC, Point Nine, Adjacent
  and 120 founders as backers, writing €200k checks to founders under 25
  (tech.eu 2025-03-12; Sifted), and Point Nine's position sits in the
  single-purpose Point Nine VI Project Europe GmbH. An LP stake in a fund is
  **`not_member`** (fund-shaped entries, standing rule under T5); its portfolio
  companies are not Point Nine's unless a Point Nine vehicle holds them
  directly.

- **D8 — Namesakes and LP-side filings (T1, T5).** Verified by entity and
  address, never by name: Point Nine Inc. of 55 Shuman Blvd, Naperville IL (CRD
  333690, inactive), One Point Nine Management, LLC (Philadelphia, CRD 309145,
  inactive), Point Nine Data Trust Ltd (Cyprus), Pointnine Capital Ltd
  (Cannock, UK, 2025), the "Two / Five / Eight Point Nine" UK companies, and
  "point nine" as a number in prose. SAP SE's 20-Fs and 6-Ks (2014–2026) and
  the Rimini Street S-4 exhibit list "Point Nine Capital Fund II / III" among
  SAP's own holdings: SAP is a limited partner of the funds, LP-side, never
  portfolio.

- **D9 — FX and non-US public rows (policy constants).** Every EUR, GBP, PLN,
  SEK or other non-USD figure converts at the ECB reference rate of its own
  date via `scripts/fx-convert.py`, the native figure in the note; Frankfurt
  (Delivery Hero, Mister Spex, Westwing), AIM/LSE and ASX listings take a
  web-cited market cap (`valuation_source: web_verified`); a US-listed row
  keeps the SEC float layer. No entry-date window (PRO-137).

- **D10 — The roster (T4 seat dating).** Investing people over time from the
  live team (2026: partners Janz, Chudzinski, Coppey, Sequerra Amram; research
  analyst Seemann; venture partners Hebenstreit and Wolfe), the ADV Schedule A
  owners with their dates, the funds' Form D related persons (Janz, Chudzinski,
  Zorylo), the archived team pages and the firm's own welcome and hiring posts
  (Nathan Benaich 2017-11; Julia, Andreas and Renaud 2018-07; Tilman Langer
  2018-03; Ricardo Sequerra Amram joined 2019, partner 2020-09; Laura Weritz
  2025-01), each with a dated basis in `sources/wayback/partner-roster.json`.
  The Form D sweep reaches only US-incorporated members; a roster name on a
  filing outside its window, or on an issuer with no Point Nine listing,
  announcement or vehicle, is a homonym or another firm's seat.

- **D11 — The job board is a first-party list surface** (Thrive ruling 8,
  Cherry D11): jobs.pointnine.com (Getro, Point Nine Management GmbH as the
  legal entity) lists 107 companies; a board listing is `site_listing`
  evidence with the Thrive caveats, and its stage field is never a label.
  Three of its eleven off-list cards are the listed company under another name
  or junk (Podcastle is Async, Vital is Junction, "Factorial HR" at
  factorialhr.de carries a Munich restaurant's description).

- **D12 — The blog is a first-party surface** (PRO-101's delta, applied):
  writing.pointnine.com (Substack, carrying the Medium "Point Nine Land"
  archive from 2014; 410 posts) is the firm's own record. A post naming a
  company as a Point Nine investment is `site_listing`-grade membership
  evidence; a "why we invested" post is class 1 for the round it NAMES and
  asserts an entry only where it says so in words (COLLECTION.md §6, the Menlo
  finding).

- **D13 — The site's "P9 INVESTMENT" field.** Each card on the live list
  carries the round the firm says it entered (Pre-seed / Seed / Series A /
  Later-stage) and a year. Eligible by semantics (the firm's claim about its
  own entry round, not the company's current stage); it labels
  (`entry_stage_source: first_party`) only after it is scored against the
  book's documented rounds (≥95% over ≥30 rows for `high`, `medium` below),
  and a documented round overrides it (`stage_disputes_band`). Its year was
  checked against dated deals before it may feed `first_seen`: Revolut 2015
  ("since our investment in Revolut back in 2015", 2019-10-16), Delivery Hero
  2010 (Lieferheld's 2010 seed, 2017-06-30) and Zendesk 2008 (Janz's June 2008
  check) hold, but TechCrunch dates two rows the site gets wrong: Brainly (site
  2017; "Brainly Raises $500K From Point Nine Capital", 2012-09-12) and inFakt
  (site 2012; Team Europe Ventures' investment, 2010-03-16). So the year is an
  anchor the build may use for `first_seen` (the minimum across layers wins),
  never an `entry_date`: the entry date comes from the round's own citation.
  For a pre-2011 row it dates a founder's check, not the fund's (D2). Early
  press already disputes the round word on a few rows (Couchsurfing and
  ShiftPlanning / Humanity: Series A participations the site calls Seed;
  DocPlanner: a "$1M Series A", its first outside money, the site calls Seed),
  and those count against the field when it is scored.

  **Scored 2026-09-26, blind:** 40 rows whose entry round the record names
  (TechCrunch, the firm's own posts), read before the label was looked at:
  **36/40 = 90.0%, promoted at `medium`** (`site_api.entry_stage_confidence`).
  The four misses are one class, 2011–2013 rounds of $1–2M that the press
  named "Series A" and the firm now calls "Seed" (Couchsurfing, DocPlanner,
  ShiftPlanning / Humanity, Mambu); every scored row after 2013 agrees. Where
  the record names the round, the record wins with `stage_disputes_band`.

## Deltas (Erik's)

None raised at kickoff: every fact found falls under a standing test. D2 moves
famous rows (Zendesk, Clio, Westwing) and rests on the firm's own posts rather
than an adjudicated filing, so it is flagged for Erik with the run's results
as the first open ruling, per the Cherry D2 precedent rather than as a new
test.

**String and namesake traps:** "Point Nine" as a number ("zero point nine
percent"); the namesakes in D8; SAP's list of its fund holdings; "Team Europe"
positions that were the incubator's (D3); "backed by Point Nine" on a
founder's personal pre-2011 check (D2); "Point Nine" as a Project Europe
backer (D7).

## Run-time standing rulings (dated, class-wide, flagged for Erik's review)

- **R1 — A holding received in a swap for a portfolio company's shares is sale
  consideration, not a new member** (2026-09-26, agent, applies COLLECTION.md
  s1 and Erik's 2026-09-22 ruling). Team Europe and Point Nine exchanged their
  madvertise shares for shares in its Turkish subsidiary Mobilike when Mobile
  Network Group bought madvertise in 2014 (deutsche-startups 2014-01-09;
  madvertise had bought Mobilike in 2012). The 2015 list and the 2018-2020 CMS
  (PNC I) carry Mobilike as that continuation: `mobilike` is not_member,
  madvertise stays the member. Same class as the kickoff's register
  rejections (acardo group AG, Personio Group SE for Back, Lindentor 226 for
  Lemoncat). Deskbookers' sale to Spacebase for equity (2020) needed no ruling:
  Spacebase was already a member on its own 2015 seed.

- **R2 — Members with no round that ties Point Nine keep their listing verdict
  and read `entry_stage: undetermined`** (2026-09-26, agent, Thrive ruling 8 /
  D11). Six rows: five listed only on the firm's job board (Audigo Labs,
  Blockit, Ditto, Elea, Recast Systems) and EatFirst, on the job board and the
  2021-2023 list. For four of them the round coverage names other investors
  and not Point Nine (Audigo Labs, Blockit, EatFirst, Elea); for Ditto and
  Recast Systems no round is on record at all. Flagged for Erik as the class
  most likely to hold a non-investment.

- **R3 — The firm's card status is evidence, overridden only by a cited
  event** (2026-09-26, agent). The card went stale in both directions: rows it
  calls Active that were sold (Calldesk to Future Look ITC 2022, Typeform to
  Bending Spoons 2025), a row it calls Acquired that was liquidated
  (Kreditech, as Monedo, 2020) or closed (Zenaton, its founder's own post
  "Zenaton is dead, long live Infinitic"), and merXu, which it calls RIP while
  merxu.com still resolves and no shutdown notice was found (kept defunct on
  the card; Accel's row reads private). Each override cites its event; the
  card stands where nothing contradicts it.

- **R4 — Before the record overrides the card, search for the card's own
  round** (2026-09-26, agent, extends D13). After scoring, three live cards
  looked wrong against the round the press names: Findable (card Seed 2024),
  Heygo (card Seed 2021) and Upciti (card Series A 2023). Only Findable held:
  its EUR 2M round of 2022 was before Point Nine, which entered at the named
  EUR 9M Series A it led (ArcticStartup 2024-09), so the record wins with
  `stage_disputes_band`. Heygo's Series A press left out the seed Point Nine
  led (Nordic 9, 2021-12-23), and FrenchWeb names Upciti's 2023 round "Serie
  A" (the company later called its 2025 round a Series A too), so both keep
  the card's label. The four scored misses carry `stage_disputes_band`, as D13
  says. Preply keeps its card label (Series A 2017): the only rounds anyone
  names start at the 2021 Series B, so nothing contradicts the card.

- **R5 — Tier reads below_1b on collapse evidence** (2026-09-26, agent,
  follows the Creandum Pipe precedent). Tier's 2021 round at a EUR 2B valuation is
  superseded by the 2024 merger with Dott at a fraction of it plus a EUR 60M
  top-up at an undisclosed price; the merged company continues (private).
  Flagged for Erik.

- **R6 — Revolut's mark is the company-run secondary of July 2026 at $115B**
  (2026-09-26, agent). The same kind of event a16z and Greylock used for
  their $75B mark (Nov 2025); it moves the band to 100b_plus, so rule 10
  against both needs the wave alignment.
