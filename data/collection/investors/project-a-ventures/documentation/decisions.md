# Project A: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Project A (slug
`project-a-ventures`, display name **Project A**; legal names Project A Ventures
GmbH & Co. KG and the adviser Project A Ventures Management GmbH). The judge
cites these rulings per line. Written at kickoff 2026-09-30 (PRO-102, sub-issue
of the PRO-87 wave) under the derivation protocol of COLLECTION.md s1:
**derivations** (a standing test applied to verified facts; no confirmation
needed, vetoable), **deltas** (Erik's), and **run-time standing rulings**
(dated, class-wide, flagged for review). PRO-102 named three deltas; all three
are derived below from verified facts (D4 the roster, D8 the German recipe, D5
the operating services), and the run surfaced a fourth class the issue did not
name, the private equity practice (D3), which two standing tests already decide.

**The structural fact of this run:** Project A is a Berlin operational VC founded
in 2012 whose portfolio is overwhelmingly European and files nothing with the
SEC, while its fund side is visible there (one exempt reporting adviser with a
Section 7.B table, five fund Form D filers). What carries the base is the firm's
own record, read in four site generations: the live Sanity CMS (114 companies
with the firm's own entry year, entry round, fund, status, HQ and board partner),
the 2020-2024 Contentful records (the firm's own round word, investment type VC /
PE Co-Investment, monthly investment date, status, founded year, location), the
2015-2019 Kirby and LogoTile listings with per-company pages (round word, exit
line), and the 2012-2014 WordPress gallery of the company-builder years.

## Derivations (T1-T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm (T1, same adviser).** Project A = the Berlin firm managed
  through one SEC exempt reporting adviser, **Project A Ventures Management
  GmbH** (primary business name PROJECT A, CRD 319556, SEC 802-127292, annual
  amendment 2026-03-18) at Julie-Wolfthorn-Strasse 1, 10115 Berlin. Schedule A:
  Florian Heinemann, Uwe Horstmann and Thies Sander general partners since
  11/2015, Anton Waitz since 11/2016, Jan-Willem Jensen and Anton Grabovski
  managing directors since 09/2023, five partner holding companies as
  shareholders since 10/2016. Section 7.B.(1): Project A Ventures II, III, IV and
  V GmbH & Co. geschlossene Investment KG, Project A Opportunity II and IIA,
  Project A Security I, and Silver Stone GmbH & Co. KG ($2.756B gross, sources/
  registers/adv-7b.json). EDGAR (read 2026-09-30): Form Ds by Project A Ventures
  III (CIK 1769632, 2019-03), IV Feeder (1892828, 2021-11), V (2048216,
  2024-12), V International Feeder SCSp (2048219, Luxembourg, 2024-12) and
  Project A Opportunity II (CIK 1837937, 2021), all but the Luxembourg feeder at the adviser's
  address. The firm's own CMS names the holding fund per company: Fund I (2012,
  "110 Million USD Fund" on the firm's 2016 overview page), Fund II ("our current
  EUR 140m fund", 2018 scope page), Fund III, Fund IV ("$375m fourth fund", the
  firm's 2022-06-15 post), Fund V ("EUR 325 million fund", 2025-06-24 post) and
  "Buyout Fund I". Handelsregister (North Data suggest, read 2026-09-30; sources/registers/northdata-suggest-*.json): Project A Ventures GmbH & Co. KG, Project A Ventures II-V GmbH & Co. geschlossene Investment KG with their Carry KGs and Komplementär GmbHs, Project A Ventures IV Feeder and IV Blocker, Project A Opportunity II, IIa and III, Project A Security Fund I and Security Opportunity I, Project A Ventures Management GmbH, Project A Ventures Trust UG, all in Berlin; no Buyout vehicle is registered there under the Project A name. One firm, one adviser, one investment team -> **IN**:
  primaries, follow-ons and secondaries from Funds I-V, the Opportunity funds and
  the Security funds. Feeders (IV Feeder, V International Feeder) are plumbing (T5). The
  London office (Project A Services UK Ltd., opened 2021) and the Munich office
  are the same firm. Precedent: Northzone D1 (one firm, several offices);
  Creandum's flagship, Select and SPV vehicles.

- **D2: Sale consideration (T3 standing rule, Erik 2026-09-22, and the share-swap
  extension of 2026-09-26).** The firm's own lists carry ACQUIRERS in place of
  companies it backed: Modernizing Medicine (the CMS files it under Fund II,
  2022, no entry round; ModMed bought Project A's Klara, the firm's own
  2022-02-08 post "Exit: Patient collaboration platform Klara is acquired by
  ModMed") and Navan (Fund II, 2022, no entry round; Navan, then TripActions,
  bought Project A's Comtravo in 2022). EDGAR's exit side adds Demand Media
  (its 2014 S-3 / 424B3 resale prospectus lists Project A among the Saatchi
  Online sellers). Each is `not_member` with the acquired company named, which
  is the member and reads `acquired`, unless a fund later put new money into the
  acquirer in a financing (then a separate citable entry). Written into
  `config.verify.not_members`.

- **D3: The private equity practice (T1 strategy desks and T3 control positions;
  a class PRO-102 did not name).** Facts: the live CMS labels 13 companies
  `projectInvestedAt: private_equity` and the 2020-2024 Contentful records label
  about 20 `investmentType: PE Co-Investment`, with the firm's own round words
  "Later Stage Acceleration", "Succession Arrangement" and "Venture Round";
  Christoph Rösler "co-leads the firm's Private Equity practice. He focuses on
  PE growth and buy-out investments" (live CMS bio); the CMS names the holding
  fund as Fund II, III or IV (the venture funds) for 12 of the 13, and "Buyout
  Fund I" for one (Primutec, 2025); the firm's 2016 press release "Project A
  teams up with EQT Mid Market for joint investment in kfzteile24". Two standing
  tests decide it, so it is a derivation and not a delta:
  - **Strategy desks (T1, Erik 2026-09-04)** resolve per vehicle, never by the
    brand. A position held by a venture fund (Fund II-IV) is on the venture
    desk whatever the practice that sourced it, so the partition does not
    remove those rows. **Buyout Fund I** is a buyout-strategy vehicle of the
    same firm: `other_desk`, its rows leave the published base preserved in
    `excluded.json` (Primutec).
  - **Control positions (T3, Erik 2026-09-04)** decide each remaining PE row per
    transaction: where the firm, alone or with its co-investor group, took
    control (50% or more, a buyout, a succession purchase of the founders'
    business, an LBO beside a PE sponsor), the row is OUT with reason
    `control_position`; a minority growth financing or a minority secondary is
    a venture entry at scale, IN as `Growth`. The firm's own words are the first
    evidence ("Succession Arrangement" reads control), then the transaction's
    press or register record. This is the case the addendum names ("where one
    vehicle does both (Insight, General Catalyst)").
  - A purchase of shares in a company already listed (HomeToGo, listed in
    Frankfurt since 2021, CMS `private_equity` 2025) is a public-market purchase:
    OUT under T3's standing rule, whatever the practice that made it.
  - The profile says so: the published track record covers Project A's venture
    and minority growth investments, not its buyouts (COLLECTION.md s1).

- **D4: The roster (PRO-102's first delta, derived).** The people namespace mixes
  the investment team with the operating-services staff: 264 people on the
  2020-2024 team pages, of whom the site's own type field marks 26 "Investment",
  14 "Management" and 6 "Partner", against 217 "Operations", 71 "Operational",
  15 "Team Leads" and 12 "Funds" (fund operations and investor relations);
  the live CMS has 14 "investments" and 11 "operations". The sweep roster is
  the partners of the 2012-2019 management pages, the ADV general partners, the
  live "investments" department and the archived "Investment" type, excluding
  the fund-operations and IR staff and the operating partners of Project A
  Services (Rainer Berak, "Operating Partner | Managing Director Project A
  Services GmbH"): 30 people with capture-year tenure windows
  (sources/wayback/partner-roster.json, config `roster.site_team_groups`).

- **D5: The operating services are not an investment (T2; PRO-102's third delta,
  derived).** Project A Services GmbH & Co. KG (with Project A Services Management GmbH, Berlin; North Data, read 2026-09-30) and Project A Services UK Ltd.
  employ the firm's value-creation specialists ("With our team of nearly one
  hundred specialists in the areas of IT & product, business intelligence,
  online marketing and organization building, we support founders", 2016
  overview). A company that received that support with no fund position is OUT,
  the scout and programme shape. On the evidence so far the firm's own lists
  carry only fund positions (every CMS row names its fund); the one surface that
  lists outside companies is the Knowledge Conference's speaker and partner
  directory (project-a.com/companies/<slug> 2022-2024: Google, Mastercard,
  Lacework, Deutsche Börse, Berlin Partner), an event directory, never the
  portfolio: no row may rest on it.

- **D6: Co-founding and the Studio (T2, the incubation precedent).** "We start our
  own projects and invest in existing teams and startups ... Co-Founding ideas
  ... Check out our portfolio page to see some companies that were co-founded by
  Project A" (2016 investment-approach page). The 2012-2014 company-builder
  projects (Wine in Black, Tirendo, Toroleo, Kochzauber, Amerano, Contorion,
  Evino, Natue and the others the gallery lists) and the 2024 Project A Studio
  companies are IN where a fund of the firm held the position (Thrive
  incubation precedent), which the firm's lists assert by naming the fund. Two
  joint ventures the firm lists as its own (Spryker, spun out in 2014; ESV Digital
  Brazil, "Joint Venture") are judged the same way: IN as the fund's listed
  position, stage from the record or `undetermined`.

- **D7: Person or firm (T4).** Standard seat dating. The roster-name Form D sweep
  is homonym noise on this book (Benno Fischer at the AllianzGI funds, several
  Jack and John Wangs in US real estate and biotech, a 2025 Digitail seat for an
  Andreas Helbig who left the team after 2020): every such row needs affirmative
  corroboration and, lacking it, is `not_member`. Partners' personal angel books
  are out (Cherry D2, standing since 2026-09-26): Christian Weiss's "Business
  Angel in 20+ startups, e.g. eDarling, Zalando" (2016 management page).

- **D8: German recipe (PRO-102's second delta, derived).** Cherry's conventions
  apply: insolvency followed by an asset sale reads `acquired` with a successor
  note; a filing with no sale yet reads `defunct` (Erik, 2026-09-07); the home
  register's dissolution or insolvency flag is filing-grade `defunct` evidence
  (the North Data sweep of HV Capital's write-back 3). Non-USD figures convert at
  the ECB rate of their own date (`fx-convert.py`); a listing outside SEC
  registration takes a web-cited market cap.

- **D9: No entry-date window.** The book starts in 2012; every row is judged on
  the same evidence, and where the record does not give the round the stage
  reads `undetermined` (PRO-137).

- **D10: The firm's own stage fields (COLLECTION.md s5).** Two first-party
  fields claim the round the firm entered: the live CMS `projectInvestedAt`
  (pre_seed / seed / series_a / series_b / private_equity) and the 2020-2024
  Contentful `investment` (Seed / Series A / Series B / Venture Round / Joint
  Venture / Later Stage Acceleration / Succession Arrangement), plus the
  2016-2019 per-company pages' "Investment" line. Eligible by semantics. They
  ride in the queue as evidence and label only after they are scored blind
  against the book's documented entry rounds (s5: `high` at 95% over 30 or more
  rows, `medium` otherwise). `private_equity`, "Venture Round", "Joint Venture"
  and "Succession Arrangement" name no taxonomy round and never label. The
  Contentful `dateOfInvestment` is read only from a company's earliest capture
  (later captures carry 2021-12-25/26 migration placeholders); it and the CMS
  `investedAt` are close-year anchors (Menlo rule), not announcement dates.

## Deltas (Erik's)

None beyond the three PRO-102 named, all derived above and flagged. D3 (the
private equity practice) is new to this run and is derived from two standing
tests; it is flagged for review with the results. Anything the grind finds
outside every test is raised at close (s9).

## Run-time standing rulings

(dated, class-wide, flagged for review)

- **R1 (2026-09-30): the private equity class, as found (D3 applied; flagged for review).**
  Of the 17 rows the firm labels private equity, 13 are stakes beside a buyout
  sponsor that holds the majority, and they leave as `control_position`:
  kfzteile24 (EQT, and in 2023 the MBO consortium Project A was part of),
  Onlineprinters (Bregal), LUQOM/Lampenwelt (3i), trendtours (Bregal's succession
  purchase), YDEON/GartenHaus (3i), Perfect Drive Sports Group and its short name
  PDSG (Bregal), WindStar Medical (Oakley), Inwerk (Triton), Amann Girrbach
  (Capvis), Konges Sløjd (3i), NWT Group (KLAR Partners) and Primutec (Buyout Fund
  I; Trill Impact). The reading: T3 excludes a transaction in which "the firm,
  alone or with its co-investor group, acquires control"; a stake the firm itself
  records as a "PE Co-Investment" beside the controlling sponsor is part of that
  group's position, whether Project A came in at the sponsor's closing (WindStar,
  GartenHaus) or joined the sponsor's structure months later (Lampenwelt seven
  months, Amann Girrbach two years). Project A's own stake is a minority in every
  one of them; **the narrow reading** (only the firm's own stake counts) would bring
  the twelve later-joiner and co-investment rows back in as Growth, and is Erik's
  call. kfzteile24 is control on either reading (the 2023 MBO). HomeToGo (listed
  since 2021, bought in 2025) is out as a public-market purchase; HelloPrint is out
  under T2, its 2017 stake held through the Bregal-controlled Onlineprinters
  holding, not a Project A fund. Two PE-practice positions are ordinary minority
  financings with no controlling sponsor and stay as Growth members: Yoummday
  (EUR 30M growth round co-led with Armira Growth, 2022) and Amboss (EUR 240M
  round, 2025). Sources: scratch/pe-research.json (67 re-loaded citations).

- **R2 (2026-09-30): the firm's stage fields scored and promoted at medium (D10 applied).**
  Blind against the documented entry rounds recorded in the grind: the live CMS
  `projectInvestedAt` 48/53 (90.6%), misses Baobab, Gabi and Spryker (pre-seeds
  read seed) and 42matters and Homeday (Series A read seed); the 2020-2024
  Contentful `investment` 30/38 (78.9%), every miss but two a pre-seed read Seed;
  the 2015-2019 page line 11/13. Both are the firm's own claim about the round it
  entered, so both label at `medium` (COLLECTION.md s5: below 95%), cited to the
  listing (the live CMS) or the archived capture (Contentful, pages); the CMS wins
  where the two disagree. The known bias (pre-seed read as seed) is the reason a
  documented round always overrides the label. Config `site_api.entry_stage_fields`.

- **R3 (2026-09-30): an unnamed later round of unstated size does not graduate a seed
  (COLLECTION.md s6 applied; flagged for review).** Several of the firm's older
  company builds and seeds raised a later round the press reports only as
  'siebenstellig' (seven figures) or 'single-digit million', with no round name and
  no figure: store2be (2018, 2020), Toroleo (Creathor, 2013), Kyto (Müller Medien,
  2015), Loopline (2016, 2018). The step-up test (twice the seed, at least $5M; the
  era's seed ceiling standing in for an unknown seed) cannot be met by a round
  whose size is not on record, so such a round is not evidence of graduation, and
  the absence test records it by name as a later round not shown to qualify. The
  rows read `not_graduated`, their surface lines naming the unsized round. The
  alternative, reading the entry as `undetermined` so the row leaves the cohort,
  was the first call on Kyto and Loopline and was reversed: it drops exactly the
  quiet non-graduations PRO-132 exists to count.
