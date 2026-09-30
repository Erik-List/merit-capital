# Project A: Build & Reconciliation Report (PRO-102)

**Linear issue** PRO-102 · **slug** `project-a-ventures` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session · report written 2026-09-30.
**Closed 2026-09-30. Ingest through the §9 gate: section 15.**

---

## 1. The answer PRO-102 asked for

**The base is 131 companies (130 nameable), plain `verify` is clean, and the firm profile is built.**
Project A is one Berlin firm under one SEC exempt reporting adviser (Project A Ventures Management
GmbH, CRD 319556). Four former Rocket Internet managers founded it in 2012, with the Otto Group as
its first investor. The book runs from the 2012 company-builder years through Fund V (2025). Every
member rests on the firm's own lists, read in four site generations.

The three PRO-102 deltas, all derived from verified facts (`decisions.md`):

- **The roster (D4).** The team pages mix the investment team with the operating-services staff:
  264 people on the 2020-2024 pages, of whom the site's own type field marks 26 "Investment". The
  sweep roster is 30 people: the partners of the 2012-2019 management pages, the ADV general
  partners, the live "investments" department and the archived "Investment" type. Fund-operations
  staff, investor relations and the operating partners of Project A Services are left out.
  `config.json` `roster.site_team_groups` is `["investments"]`; `sources/wayback/partner-roster.json`
  holds the 30 with capture-year tenure windows.
- **The German recipe (D8).** Cherry's conventions apply: an insolvency followed by an asset sale
  reads `acquired` with a successor note, a filing with no sale reads `defunct`, and the home
  register's dissolution or insolvency flag is filing-grade evidence. Non-USD figures convert at the
  ECB rate of their own date.
- **Operating services are not an investment (D5, T2).** Project A Services GmbH & Co. KG and its UK
  company employ the firm's specialists. No row rests on that support. The one surface that lists
  outside companies, the Knowledge Conference speaker and partner directory
  (project-a.com/companies/<slug>, 2022-2024: Google, Mastercard, Deutsche Börse and others), is an
  event directory and never entered the base.

A fourth class the issue did not name decided more rows than any delta: **the private equity
practice (D3, R1).** The firm labels 17 positions private equity. 13 are stakes beside a buyout
sponsor that holds the majority and leave as `control_position`; HomeToGo (a listed company, bought
in 2025) and HelloPrint (held through the Bregal-controlled Onlineprinters group) are out; Yoummday
and Amboss are ordinary minority growth financings and stay as Growth members. The narrow reading of
R1 is Erik's call (section 10).

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean at 131 rows; flagged debt only (section 7) |
| Roster constrained and reported | 264 people to 30 (D4), `roster.site_team_groups` |
| Distributions vs Cherry and Creandum | Section 2, with HV Capital, Balderton and Point Nine |
| Profile through the taxonomy gate | `build-firm-profile.py` and `profile_copy.py` ok; every field populated, with a source |
| `review.html` rendered | Served on the review surface: 131 rows, the profile panel expands, no console errors |
| `report.md` with delta outcome, open rulings, prompt count | This file (sections 1, 10, 14) |
| Archetype-B corrections to PRO-87 | Section 12 and a PRO-87 comment |
| Ingest through the §9 gate, sibling rows aligned | Section 15 |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 131 | 130 nameable, plus the unnameable "Stealth" card |
| Private | 78 | 60% |
| Acquired | 38 | 29% |
| Defunct | 11 | 8% |
| Unknown | 3 | 2% (Scenset, Amazd, Shirtagram) |
| Public | 0 | |
| $1B and above | 6 | 4.6% |
| of which $10B and above | 1 | Trade Republic $14.65B |

**$1B and above** (all private, last priced round):

- Trade Republic $14.65B (a secondary sale, section 10).
- Quantum Systems $8B (the Series D of July 2026).
- Zepz $5B (2021, stale).
- Stark $3.99B (June 2026, a floor).
- Kry $2B (2021, stale).
- Sennder $1B (2021, stale).

**Entry stage.** Seed 73, Series A 23, Pre-Seed 21, Growth 4. For 9 rows the round is not on record:
Evernest, Saatchi Art, Wine in Black, Adtrade, ESV Digital Brazil, Popdust, Priceloop, Shirtagram
and Stark. 84 stages cite a documented round; 37 rest on the firm's own stage field (R2).

**Headquarters.** DE 71, GB 23, US 9, BR 6, DK 5, FR 3, NL 3, SE 3, then a tail. 129 of 131 rows
carry a city (Berlin 46, London 23, Munich 12, São Paulo 6).

**Focus.** Consumer & Marketplaces 37, SaaS 22, Fintech & Payments 13, Media, Gaming & Advertising
12, AI & Applied AI 11, Industrial & Robotics 11, Climate & Energy 8, Healthcare & Bio 6.

**Membership evidence.** Site listing 131: the live CMS and the archived lists.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 73 | 7 | 66 | 31 | 35 | **47.0%** |

Coverage is 100%.

- **Censored (7):** Architect, Atmen, Mimo, Nexcade, Rematiq, Resourcly, Vestigas.
- **Not graduated (35):** 16 have a cited end (a sale, shutdown or insolvency with no later round);
  19 rest on the dated absence test over the named surfaces. Four of those name a later round of
  unstated size (R3).
- **Graduated (31):** by a named later round, or an unnamed round above the step-up bar.
- **By entry period:** 2012-2014 seeds graduate 10 of 19 (53%), 2015-2019 9 of 16 (56%), 2020 and
  later 12 of 31 (39%).

### Calibration

| Book | Rows | Acquired | Defunct | Private | $1B+ | S2A |
|---|---|---|---|---|---|---|
| Project A | 130 | 29% | 8% | 60% | 4.6% | 31/66 = 47% |
| Cherry | 145 | 17% | 7% | 73% | 5.5% | 52/83 = 63% |
| Creandum | 177 | 29% | 5% | 60% | 11.9% | 36/71 = 51% |
| HV Capital | 266 | 39% | 6% | 52% | 6.0% | 28/43 = 65% |
| Balderton | 279 | 40% | 9% | 46% | 7.5% | 18/36 = 50% |
| Point Nine | 199 | 28% | 9% | 61% | 7.0% | 80/145 = 55% |

(Read from each book's published `base.csv`, members only, unnameable rows out; `scratch/calibration.py`.)

Project A's status shares match Creandum's. Its $1B+ share is the lowest of the six, just under
Cherry's. Its S2A rate is the lowest too, near Creandum and Balderton. The rate comes down with the
2020 and later seeds (39%): many of them are past the 24-month clock with no Series A yet. The
2012-2019 seeds graduate at 54%.

## 3. The boundary

- **One firm, one adviser (D1).** Project A Ventures Management GmbH (CRD 319556) advises every
  vehicle: Funds I-V, Opportunity II and IIA, Security I and Silver Stone. All are IN. The feeders
  (IV Feeder, V International Feeder) are plumbing. The London and Munich offices are the same firm.
- **Sale consideration (D2).** The firm's live list files two acquirers in place of companies it
  backed: Modernizing Medicine (which bought Klara) and Navan (which bought Comtravo). Both are
  `not_member`; Klara and Comtravo are the members and read `acquired`. Demand Media, which bought
  Saatchi Online in 2014, appears only on EDGAR's exit side and never became a row.
- **The private equity practice (D3, R1).** Out as `control_position` (13): kfzteile24 (EQT, then
  the 2023 MBO consortium Project A was part of), Onlineprinters (Bregal), LUQOM Group (3i),
  trendtours (Bregal's succession purchase), YDEON Group (3i), Perfect Drive Sports Group and its
  short name PDSG (Bregal), WindStar Medical (Oakley), Inwerk (Triton), Amann Girrbach (Capvis),
  Konges Sløjd (3i), NWT Group (KLAR Partners) and Primutec (Buyout Fund I, Trill Impact). Out on
  other tests: HomeToGo (a public-market purchase, T3) and HelloPrint (T2). Members at Growth:
  Yoummday (EUR 30M round co-led with Armira Growth, 2022) and Amboss (EUR 240M round, 2025).
- **Co-founding and the Studio (D6).** The 2012-2014 company-builder projects (Wine in Black,
  Tirendo, Toroleo, Kochzauber, Amerano, Contorion, Evino, Natue and others) and the 2024 Studio
  companies are IN where a fund held the position. Two joint ventures the firm lists as its own,
  Spryker and ESV Digital Brazil, are judged the same way.
- **Person or firm (D7).** The roster-name Form D sweep is almost all homonyms. Eight issuers are
  `not_member`: Allevion Therapeutics, Digitail, Efficient Drivetrains, Klein Ndoh Acquisitions Fund
  II, VerifyMe, Grande West Transportation, Noodoe and Statics. Partners' personal angel books are
  out.
- **One unnameable row.** The live CMS carries a card titled "Stealth" with no fund, year, round or
  website. It is a member flagged `identity_unresolved` and excluded from every metric.

## 4. Coverage per evidence regime

- **Firm site.** www.project-a.vc runs on Sanity, whose public GROQ API (project `nykgtoh6`) serves
  the whole dataset: 114 portfolio companies, each with the firm's own entry year, entry round, fund,
  status, HQ and board partner; 25 team cards; 44 articles; 6 funds (`scratch/sanity.py`,
  `sources/site/`).
- **Archive, project-a.com 2012-2024.** Four site generations, parsed by
  `scratch/archive_listings.py`: the WordPress gallery of the company-builder years (2012-2014), the
  Kirby and LogoTile listings with per-company pages (2015-2019), and the Next.js and Contentful
  records (2020-2024), which carry the firm's own round word, investment type (VC or PE
  Co-Investment), status, founded year, location and a monthly investment date.
  - **Common Crawl** held the listing in 2013 and 2016-2024, about 250 per-company pages from
    2016-2019 and the 2020-2024 team pages: 776 captures, read through the static `cluster.idx`
    range route while the Internet Archive was in a machine-wide cooldown.
  - **The Internet Archive** was in a machine-wide cooldown set by other sessions for the whole
    run, so the 2012, 2014 and 2015 listings were not read (debt, section 7).
  - **The Contentful migration trap.** A late-2021 migration overwrote every record's
    `dateOfInvestment` with 2021-12-25 or 2021-12-26. The parser reads a date only from captures
    before 2021-11.
- **The firm's own posts.** 175 press posts and blog articles from 2012 to 2025, indexed per company
  (`sources/site/press-archive.json`, `scratch/press_index.py`). They carry most of the cited entry
  rounds and several exits.
- **EDGAR.** The adviser's Form ADV Section 7.B table (eight vehicles, $2.756B gross, read by hand:
  the generic parser mis-paired Fund III's value with IV, V and Silver Stone). Five fund Form D
  filers. The roster Form D sweep read 108 accessions from 62 issuers; the real ones were Pactum
  (Thies Sander) and misterb&b with its SFO84 vehicle (Anton Waitz). The full-text sweep found one
  third-party registrant, Demand Media's 2014 resale prospectus.
- **Registers.** North Data (the Handelsregister mirror) for the firm tree, the operating-services
  entities and the status of German rows; the Receita Federal record for ESV Digital Brazil;
  Companies House for Gigapipe.
- **Press.** Google News per row through `graduation-surfaces` (151 rows, 0 failed surfaces); five
  research agents over the grind groups, one over the PE class and one over the visible slice, each
  re-loading every URL it cited.

## 5. Recall probe and measured recall

**Recall additions: none.** Candidates rejected:

- Bonaverde: a Project A venture partner sat on its board, with no fund position on record (T4).
- HiMate: a refugee-help social business the firm's blog promoted in 2016, with no fund position on
  record (D5).
- Rocket Internet: the founders' former employer.
- The Knowledge Conference companies (D5).

**Measured recall.** The firm's site claims "130+ founding teams". The base holds 131 members; the firm's own count and this
base agree. Both site generations with a full list (the live CMS, 114 companies, and the
2020-2024 records) are inside the base. Form D carried no membership: the roster sweep's real hits
(Pactum, misterb&b) were already listed.

## 6. Method deltas

- **The public CMS API as the site layer.** Sanity's GROQ endpoint returned the firm's full record
  in one query per type, with no HTML parsing.
- **The firm's own stage fields scored and promoted (R2).** Blind against the documented entry
  rounds: the live CMS field 48/53 (90.6%), the 2020-2024 Contentful field 30/38 (78.9%), the
  2015-2019 page line 11/13. Both are promoted at `medium`; the CMS wins where the two disagree, and
  a documented round always overrides the label (the known bias reads a pre-seed as seed).
- **Contentful record ids as identity evidence.** Where one record id carries two names across
  captures, the merge cites the id (15 merges in `companies/identity-merges.json`).
- **A press-archive index.** Every firm post indexed by the companies it names, so the grind read
  the firm's own words before any outside source.
- **Research fan-out.** Five research agents took the grind in groups from one brief
  (`scratch/row-research-brief.md`), each writing one JSON file; the judge scripts cite only what
  the agents re-loaded.
- **Common Crawl as the archive during an Internet Archive cooldown.** The static `cluster.idx`
  route needs no index server.
- **Model mix.** Every judge, research agent and the blind judge ran on the default model (Opus
  5.5).

## 7. Flags and debt behind `verify`

**Flags on the 131 published rows:**

- `model_disputes_source` 16: wrong Wikidata or SEC joins on short names (Q, Relay, Riva, Waypoint
  and others), and firm fields the record overrides (Gabi's CMS seed, Voi's round name), each noted.
- `stale` 4: Kry, Sennder and Zepz (last priced in 2021), and Project Q, where the flag rides the
  quarantined SEC join to a Norwegian namesake (as on HV Capital's Midas).
- `cik_weak` 1: Project Q (the same namesake join, quarantined).
- `unstable` 2 (duty 7): Gabi, ESV Digital Brazil.
- `stage_disputes_band` 1: Pactum.
- `city_unknown` 1: Shirtagram. `country_prior` 2: Shirtagram, Stealth.
- `identity_unresolved` 1: Stealth.

**Debt:**

- **The Internet Archive years 2012, 2014 and 2015 were not read.** The archive was in a
  machine-wide cooldown set by other sessions for the whole run (the last one ends 22:42 local).
  Common Crawl carried 2013 and 2016-2024. The 23 per-company pages the pull targets are all rows
  already in the base, so the risk is a company listed only between the 2013 and 2016 crawls. The
  pull is ready: `scratch/ia_pull.py`, then `scratch/archive_listings.py`.
- 9 rows with the round not on record; 3 `unknown` statuses (Scenset in the Netherlands has no free
  register; Amazd's GmbH still files accounts; Shirtagram left no trace).
- Sibling rows not aligned: YC's Tabula (accepted pair) and Sequoia's Stark city (section 15).

## 8. Standing duties and the A/B pass

- **A/B on the visible slice.** The $1B+ rows, the public-looking joins and the PE class were
  researched by agents that re-loaded every URL they cited (`scratch/visible-research.json`,
  `scratch/pe-research.json`). Every $1B+ figure is a priced round with a citable figure, converted
  at the ECB rate of its date; no mark rests on a vendor (Rule A).
- **Duty 1, $1B+ web check:** all six re-verified for identity and status. Voi reads `below_1b`:
  its lead shareholder VNV Global carries it at $362M-$656M, aligned with the Balderton, Creandum
  and Felicis rows.
- **Duty 2:** no $1B+ row reads `not_graduated`; the seven censored entries all date from 2025-03
  or later.
- **Duties 3, 4, 5 and 8:** the book has no public row and no SEC float. The one weak join (Project
  Q to a Norwegian namesake) is quarantined.
- **Momentum slice:** 18 recent hot-sector private rows got one recorded web check; all stay below
  $1B.
- **Unicorn re-intersect** with loose normalization: only the rows already handled matched.
- **Duty 7, blind 5%.** Seven rows re-judged by a judge with no access to the record: 32 of 35
  cells agree (91%). Adjudicated:
  - ESV Digital Brazil is `defunct`: the Receita Federal record has read INAPTA since 2022-06-07
    (the grind had `unknown`).
  - Gabi keeps Pre-Seed on the firm's own words; the blind judge's Seed reading is open (section
    10).
- **Duty 9, the class.** The status class was swept: of the five `unknown` rows, only ESV had a
  register that settles it. The stage class showed no pattern in the sample.
- **Names under other spellings in sibling books.** Checking this book's merge duplicates and the
  "formerly" and "later" names in its notes against every sibling found five same-company pairs
  the name key had never joined: Tabula (YC), Eduflow (YC), ExpressSteuer (Insight), Saatchi Online
  (Balderton) and ZenMate (HV Capital). They are `same` pairs in `companies/cross-rulings.json`.
  Two sibling sides were stale (section 15). Because this row now publishes as Tabula, four
  pairs with Tabula Inc., the chip maker, are ruled distinct.
- **Cities.** Quantum Systems moved from Munich to Gilching, the registered seat of every group
  entity (the city rule publishes the municipality). Tictail stays Stockholm: at the 2018 sale the
  press called it Sweden-based, with offices in Stockholm and New York.

## 9. Firm profile

- **Thesis:** "From ideas to icons." (the homepage heading, verbatim).
- **History (78 words):** founded in Berlin in 2012 by Florian Heinemann, Uwe Horstmann, Thies
  Sander and Christian Weiss with the Otto Group; WorldRemit, Trade Republic, sennder and Quantum
  Systems; Fund V at EUR 325M in 2025; the track record covers the venture investments, not the
  private equity co-investments.
- **HQ:** Berlin, from the ADV principal office (Julie-Wolfthorn-Strasse 1), with London as the
  other office. `sources/offices.json`.
- **AUM:** $2,755,658,750 at both ends, the sworn Section 7.B gross values of the eight vehicles.
  The firm's own "EUR 1.2 billion" is committed capital, noted.
- **Funds:** V ($377.2M, 2025), IV ($375M, 2022), III ($196.9M, 2019), II ($147.2M, 2017), Fund I
  ($108.5M, 2012), each at the ECB rate of its announcement date.
- **Stages** Pre-Seed, Seed, Series A. **Geography** core Europe, other US. **Scope** Generalist,
  focus from the CMS industry tags through `config.json` `profile.focus_crosswalk` (Health added at
  close; "Work & Education" stays unmapped, its 12 companies spread over four areas): Industrial &
  Robotics, Consumer & Marketplaces, AI & Applied AI, Fintech & Payments, Healthcare & Bio, SaaS,
  Climate & Energy, Security.
- **Range:** $338,550 (the firm's stated EUR 300K floor) to $7,000,000 (the Fund III "initial
  cheques up to $7 million"), median $5M over 68 stated entry rounds (a round size, not the cheque;
  flagged press-based).
- **Notables:** Trade Republic, Voi, Catawiki, Quantum Systems, Zepz. **Individuals:** 14, the
  live "investments" department, each with the LinkedIn link from the firm's own team card (14 of
  14).
- **Icon:** the firm's favicon (1440x1440 PNG, transparent), flattened onto its own light blue
  because the transparent mark measured 2.00:1 against the default plate. The dry run on the
  flattened file passed: contrast 8.6:1, edge ramp 0.77px, keyline OK.

## 10. Open rulings for Erik

1. **R1, the private equity class: the broad reading is applied.** A stake the firm records as a
   "PE Co-Investment" beside a sponsor that holds the majority counts as part of the control group,
   so 13 rows are out. On the narrow reading (only Project A's own stake counts, and it is a
   minority in every case) twelve of them return as Growth members. kfzteile24 is out on either
   reading: Project A was part of the 2023 management buy-out.
2. **R3, an unnamed later round of unstated size does not graduate a seed.** store2be, Toroleo, Kyto
   and Loopline raised a later round the press calls only "seven figures" or "single-digit
   million". They read `not_graduated`, with the unsized round named in their surface lines. The
   alternative is `undetermined`, which takes them out of the cohort.
3. **Trade Republic's band rests on a secondary sale.** The row carries the EUR 12.5B secondary of
   December 2025 ($14.65B, `10b_plus`), aligned with the Accel, Creandum, Sequoia, TCV and Thrive
   books. HV Capital's R6 (n8n) asks whether a secondary may set a mark at all. On primary rounds
   only, Trade Republic reads the EUR 5B of June 2022 (`1b_plus`), and six books change band
   together.
4. **Gabi's entry stage (duty 7).** Kept Pre-Seed on the firm's own exit post ("first invested at
   pre-seed stage five years ago"). The blind judge read the $2.6M seed of August 2017, which
   TechCrunch says Project A was in, and a graduation on the $9.5M Series A of February 2018. On
   that reading Gabi enters the S2A cohort as a graduate. Flagged `unstable`.
5. **ESV Digital Brazil reads `defunct`, from a tax-register flag, not a dissolution.** The Receita
   Federal record has read INAPTA since 2022-06-07 for failing to file returns; the site stopped in
   2018 and its domain is for sale. A second question sits under it: Adtrade merged into the joint
   venture in June 2014, the month before ESV Digital bought Adtrade. The joint venture dates from
   January 2013, so it is read as a position in its own right, not as sale consideration.
6. **Wine in Black stays a member.** In January 2012 Project A planned to take the shop over
   by "takeover, partial sale or share swap" (Deutsche Startups, translated), which would be a control position. The firm's
   2014 post lists Project A as one of five investors, so no control is shown.
7. **Popdust and Shirtagram rest on one listing each**, the firm's May 2013 portfolio page. Popdust
   is a New York publisher whose 2012 Form D names no investor; Shirtagram left no trace beyond the
   page. Both stay members at `undetermined` stage.
8. **Inferred successor sales.** Loopline, Horizn Studios and Kyto read `acquired` because the
   business continued under a successor company after an insolvency or a change of control, read
   from the register and the imprint rather than an announced sale. Amerano reads `acquired`
   (bought by Grünberg in 2013), although the buyer wound it up in 2018.
9. **STARK's entry round is not named.** Press names Project A in the $62M round of August 2025 and
   the EUR 500M Series C of June 2026. The row stays `undetermined` on stage and outside the stage
   distribution; its $3.99B mark is a floor.

## 11. Rebuilds and deltas

The grind judged 161 rows. The one scheduled rebuild removed the 25 `not_member` rows (13 control
positions, HomeToGo, HelloPrint, two acquirers and eight Form D homonyms) and applied the identity
merges. It also brought back two duplicates, GartenHaus and Lampenwelt: their merges into YDEON
Group and LUQOM Group cannot run because those rows are excluded (§8). Each got its own
`control_position` verdict and a second rebuild gave 131 rows.

The rename list was read after each rebuild: no verdict moved onto another company, and the only
new slugs were the two duplicates. `prepare` then found nothing to judge. Ten published names were
set in `config.json` `names.published` under the §8 capitalisation rule: Project Q (the CMS says
"Q"), Tabula (the CMS says "Tabular"; the company is Tabula GmbH), Stark, Pets Deli, Amazd,
Metrigo, Priceloop, Store2be, Yababa and CrossEngage.

## 12. Playbook write-backs proposed (not applied: scripts/ and COLLECTION.md belong to the tooling session)

1. **Look for a public CMS API before parsing HTML.** The site's page source named a Sanity project,
   and its public GROQ endpoint served the firm's whole record (entry year, round, fund, status, HQ,
   board partner) in one query per type. A §3 line: check page source for Sanity, Contentful or
   `__NEXT_DATA__` first.
2. **A date that repeats across many records is a placeholder.** The 2020-2024 Contentful records
   had their investment dates overwritten with 2021-12-25/26 in a late-2021 migration. The
   archive parser should read a date only from captures before a known migration, and flag any
   date shared by more than a handful of records.
3. **The PE co-investment reading (R1) for §1 T3:** a stake the firm records as a PE co-investment
   beside a sponsor that holds the majority is part of the control group, whether it came in at the
   sponsor's closing or months later. If Erik takes the narrow reading instead, T3 should say so.
4. **R3 for §6:** an unnamed later round whose size is not on record is not evidence of graduation;
   the absence test names it and the row reads `not_graduated`.
5. **Index the firm's own posts by company before the grind.** `scratch/press_index.py` built
   `sources/site/press-archive.json` (175 posts), and the grind read the firm's own words first;
   most cited entry rounds came from it.
6. **Parallel research agents need their own scratch folders.** One agent's `merge.py` was
   overwritten by another group's in the shared scratchpad. Generic helper names (`merge.py`,
   `surf.py`, `nd.py`) collide; each agent should work in `scratchpad/<group>/` and write only its
   own output file.
7. **The roster type field.** Where the team pages carry a department or type field, constrain the
   roster with `roster.site_team_groups`; here it cut 264 people to 30. Worth a §4 line for
   operational VCs (archetype B).
8. **The ADV 7.B parser mis-pairs values across fund blocks** when one block's value is long
   (Fund III's $1.378B was paired with IV, V and Silver Stone). The table was read by hand into
   `sources/registers/adv-7b.json`; `scripts/` needs a block-bounded parse.
9. **`graduation-surfaces` has no firm-terms entry for this book.** It falls back to the bare phrase
   "Project A", which matches any project. Proposed `FIRM_TERMS["project-a-ventures"]` =
   `"Project A Ventures" OR "Project A" Berlin`.
10. **Contentful record ids as identity evidence.** One record id carrying two names across captures
    is a rename, and the merge can cite it.
11. **Names the key cannot join.** Five of this book's rows sit in sibling books under other names
    (Tabula, Eduflow, ExpressSteuer, Saatchi Online, ZenMate), and rule 10 had never compared them;
    two siblings were stale. A merge's duplicate names and a note's "formerly" and "later" names,
    matched against every sibling's names, find them; they belong in `same` pairs.

## 13. Usage line

**Kickoff (Opus 5.5):** five-hour window 6%, weekly 14%, Fable 1%. **Close:** five-hour window
6%, weekly 40%, Fable 5% (a new five-hour window began mid-run). Extra usage disabled.

**Web searches:** about 135 of the 200 cap: the PE agent 24, the visible-slice agent 34, the five
research groups 67, the blind judge 9, and a few by hand. Everything else ran on the uncapped Google
News helper.

**Subagents:** five research groups, the PE-class agent, the visible-slice agent and the blind
duty-7 judge.

## 14. Prompt count

**2**: the kickoff ("please collect Project A") and a "continue" while the run waited out the
archive cooldown. No corrections from Erik. The count is final at the closing message.

## 15. Ingest

Pending at the closing commit; recorded after the §9 gate runs.
