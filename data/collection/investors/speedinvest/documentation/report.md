# Speedinvest: Build & Reconciliation Report (PRO-84)

**Linear issue** PRO-84 · **slug** `speedinvest` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session · report written 2026-09-30.

---

## 1. The answer PRO-84 asked for

**The base is 386 companies (385 nameable), plain `verify` is clean, the firm profile is built, and
the registry coverage matrix is section 3.** It is ingested: 386 companies and the investor row are live, and the readback shows 0 differing cells (section 15).

Speedinvest is one Vienna firm under one adviser (Speedinvest GmbH, SEC exempt reporting adviser
CRD 316774), founded in 2011 with a EUR 10M fund and now a multi-team seed firm with growth and
Middle East & Africa teams. The Austrian register shows 45 vehicles under it.

The two questions the issue named, both derived from verified facts (`decisions.md`):

- **The vertical funds (D1).** Speedinvest F (fintech), Industry, x (Network Effects), Emerging
  Markets, the Opportunity and Growth vehicles and 16 single-company co-investment vehicles all sit
  under Speedinvest GmbH or Speedinvest GP GmbH. All are IN.
- **The scout programme (D3).** There is none. "Speedinvest Scouts GmbH & Co KG" is the renamed
  Pioneers Ventures Digital fund, the firm's own early vehicle; its stakes (GoStudent, Refurbed,
  Prewave and others) moved into Speedinvest II in 2021-2023. Its positions are IN. Speedinvest
  Heroes (recruiting) and Pirates (growth marketing) are service companies and are not investments.

One class the issue did not name decided more rows than either: **sale consideration (D4, D5).**
The firm lists eight acquirers in place of the companies they bought, in its own words
("Speedinvest became a shareholder in OpenAI following its acquisition of Ona in 2026"): OpenAI,
Mistral, MoonPay, Perk, Mews, Dialpad, Taxfix and OneTrust. All eight are out; Ona, Emmi AI,
Ultimate (Iron), Yokoy, Flexkeeping, Surfboard, TaxScouts and Planetly are the members.

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean at 386 rows; flagged debt only (section 7) |
| Distributions sanity-checked | Section 2 |
| Profile through the taxonomy gate | `build-firm-profile.py` and `profile_copy.py` ok; every field populated, with a source |
| `review.html` rendered | Served and checked: 386 of 386 rows render flat, the profile panel expands, no console error |
| Registry coverage matrix | Section 3 |
| Method delta, open rulings, prompt count | Sections 6, 10, 14 |
| COLLECTION.md diff proposed | Section 12 (not applied: `scripts/` and the playbook belong to the tooling session) |
| Ingest through the §9 gate, siblings aligned | Done: Speedinvest live; Accel and Seedcamp aligned and re-ingested; Y Combinator and a16z not aligned, with reasons (section 15) |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 386 | 385 nameable, plus Bleep (a 2020 listing with a logo and no other trace) |
| Private | 264 | 68% |
| Acquired | 70 | 18% |
| Defunct | 37 | 10% |
| Unknown | 15 | 4% |
| Public | 0 | |
| $1B and above | 7 | 1.8% |

**$1B and above** (all private, last priced round): Bitpanda $4.1B (August 2021, stale; an IPO was
reported and delayed in 2026), Moove $2.1B (August 2026), Wayflyer $1.6B (February 2022, stale),
Tide $1.5B (September 2025), Open $1B (May 2022, stale), Fasset $1B (August 2026), Kraken Technology
Group $1B (July 2026). Three former unicorns read below $1B on documented collapse: GoStudent
(Prosus's write-down to about $969M, 2024), TIER (the Dott merger at about EUR 150M, 2024) and wefox
(a sale backed by its Series D lead at an enterprise value of at most EUR 550M, 2024).

**Entry stage.** Seed 161, Pre-Seed 77, Series A 25, Growth 7. For 115 nameable rows the round is not
on record (30%). The firm publishes no round word, so every stage is the round a page names:
202 rest on press or company pages, 48 on the firm's own posts and its 2018-2020 Pre-Seed tag (R2),
19 on the amount band of R1 and one (Billie) on an inferred seed.

**Headquarters.** GB 88, DE 81, AT 54, FR 36, US 31, NL 12, ES 9, CH 9, then a tail of 30 countries.
371 of 386 rows carry a city (London 75, Berlin 54, Vienna 40, Paris 29, Munich 12).

**Focus.** Fintech & Payments 82, Consumer & Marketplaces 62, AI & Applied AI 41, SaaS 39, Healthcare
& Bio 37, Climate & Energy 27, DevTools & APIs 22, then five smaller areas.

**Membership evidence.** 385 rows rest on the firm's own listings, pages or posts; one (Heroes Jobs)
on a partner's board seat on the company's own Form D.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 161 | 24 | 137 | 61 | 76 | **44.5%** |

Coverage is 100%. Of the 76 that did not graduate, none rests on the filings, 28 on a cited end (a
sale, shutdown or insolvency with no later round) and 48 on a dated search of the named surfaces.

- **By entry period:** 2011-2016 seeds graduate 6 of 14 (43%), 2017-2020 27 of 46 (59%), 2021 and
  later 28 of 77 (36%), with 24 more too recent to count.
- **What the rate does not cover:** 115 rows with no named entry round are outside the cohort. Many
  are quiet early bets, so the cohort leans toward companies that were written about.
- 12 seed entries rest on an uncited stage (11 banded under R1, and Billie). One is too recent to
  count; of the 11 in the cohort, 4 graduated and 7 did not. `verify`'s stage-leg line
  reads 10.

### Calibration

| Book | Rows | Acquired | Defunct | $1B+ | S2A |
|---|---|---|---|---|---|
| Speedinvest | 386 | 18% | 10% | 1.8% | 61/137 = 44.5% |
| Seedcamp | 553 | 13% | 5% | 2.2% | 26/64 = 41% |
| Project A | 131 | 29% | 8% | 4.6% | 31/66 = 47% |
| Cherry | 148 | 16% | 7% | 5.4% | 53/84 = 63% |
| Point Nine | 199 | 28% | 9% | 7.0% | 80/145 = 55% |
| HV Capital | 266 | 39% | 6% | 6.0% | 28/43 = 65% |
| Creandum | 177 | 29% | 5% | 11.9% | 36/71 = 51% |

(The other books' figures are read from their current `base.csv`.) Speedinvest sits beside
Seedcamp, the other large pre-seed and seed book: the two lowest $1B+ shares and the two lowest
graduation rates of the seven. Three of its best-known companies lost their $1B marks in 2024.


## 3. The registry coverage matrix (the deliverable PRO-84 asked for)

**The answer to the issue's question: no, the European path does not depend on a good registry.**
Membership came from the firm's own record in every jurisdiction: the live site, the job board, the
archived listings and the firm's posts. Not one row entered the base on a register. What the
registers gave is status (dissolution, liquidation, insolvency, a new sole shareholder), identity
(renames and legal names) and corroboration (a Speedinvest vehicle on the shareholder list). Where
no usable register exists, the cost is not a missing company: it is a quiet shutdown read as
`private` or `unknown`.

The issue's prior was also wrong on geography. The book is not spread across DACH and Central and
Eastern Europe: 88 rows are in the UK, 81 in Germany, 54 in Austria, 36 in France and 31 in the US; those five countries hold 75% of the base. CEE is 22 rows.

| Jurisdiction | Register and route | Rows it touched | Filing-grade evidence | Cost | Language | Verdict |
|---|---|---|---|---|---|---|
| Austria | Firmenbuch through North Data's free entity pages (publication stream) | 49 rows cited; 38 of the 204 swept targets matched an Austrian entity | **Yes, three kinds.** Status events (liquidation, Konkurs). Shareholder changes with the holders named when few: 29 rows carry a Speedinvest vehicle by name ("Shareholder: Speedinvest II EuVECA GmbH & Co. KG"). The fund tree itself (45 vehicles, founding dates, name history) | Free; 3 s pacing | German source, English page | **Works for backtrace and status.** Forward enumeration (a fund's holdings) is a count on the free page ("44 known active shareholdings") and a list only on the paid tier; the free page still named 37 holdings across the 45 vehicles |
| Austria | Firmenbuch extract (Justiz, through a Verrechnungsstelle) | Not used | Would give the full shareholder list per GmbH | Paid per extract | German | Not needed: the free stream answered every question asked |
| Austria | Ediktsdatei (insolvency notices) | 1 row (Mikme) | Yes, for insolvency | Free | German | Works; the North Data stream carried the same events |
| Germany | Handelsregister through North Data | 65 rows cited; 63 swept targets matched | **Yes.** Liquidation and insolvency events (Fraugster, Doctorly, JimDrive, datapath.io, Aircloak); renames (PYLOT to FERNRIDE); shareholder-list filings | Free | German source, English page | Works for status and identity (the recipe of the Cherry, HV Capital and Project A runs) |
| United Kingdom | Companies House (web) | 51 rows | **Yes.** Dissolution, strike-off and liquidation (Vitt, Impala, Unweave, Fleksy, Gig.fm); previous names (Our Path to Second Nature, Lark Optics to Allfocal Optics); persons with significant control (Vira Health over The Lowdown) | Free | English | Works for status and identity; no venture-size shareholder is visible without reading filed documents |
| Estonia | e-Business Register through North Data | 3 rows | **Yes.** Shareholders named: Investly lists Speedinvest; Modular Technologies OÜ (Tuum) lists Speedinvest Opportunity I | Free | English page | Works for backtrace; the only CEE register that did |
| France | INPI / RNE (through Pappers, societe.com, the state search API) | 5 rows | Status only (Flaneer ceased 2024-12-31) | Free | French | Status only |
| Netherlands | KVK (through aggregators) | 5 rows | Status only (Secret City Trails struck off) | Free for status | Dutch | Status only |
| Switzerland | Zefix | 2 rows | Status only | Free | German / English | Status only |
| Denmark, Norway | CVR; Brønnøysund | 1 row; 1 row (Skyfri's Norwegian subsidiary, bankrupt November 2025) | Status only in this run | Free | Danish / Norwegian | Not exercised for ownership: too few rows |
| Bulgaria, Croatia, Czech Republic, Greece, Lithuania, Poland, Slovakia | National registers through North Data (bounded probe, `sources/registers/cee-probe.json`) | 13 rows probed, 11 entities found | **Thin.** The entity and a shareholder count; no holder names, almost no status events (kevin.'s Lithuanian entity shows none although the company failed) | Free | English page | **Negative for this pipeline**: finds the legal entity, proves nothing about status or holders |
| Hungary, Slovenia, Turkey, Ukraine | National registers | 9 rows, none read | None: North Data does not carry them, and the national sites were not read (Hungarian and Turkish registers are in the local language behind a captcha or a login) | Not established | Hungarian, Slovene, Turkish, Ukrainian | **Not covered.** These rows rest on the company's own pages and press (two Hungarian shutdowns were read off the companies' own farewell pages) |
| United States | EDGAR | Fund side: 3 Form D filings, one Form ADV (10 funds). Issuer side: 36 roster name-matches, 2 members | Yes, for the fund side and for two unannounced rows (Blloc, Heroes Jobs) | Free | English | As on every non-US firm: fund-side only; the full-text sweep found no third-party mention of Speedinvest at all |

**The coverage rule this gives the remaining European firms** (proposed for COLLECTION.md §5):

1. Sequence a European firm by whether it **publishes its own record** (a portfolio CMS, an archive,
   a post archive), not by its home register. That decides whether the base can be built.
2. A free register adds status and identity in Austria, Germany, the UK and Estonia, and backtrace
   (a named fund on the shareholder list) in Austria, Germany and Estonia. Budget one sweep per run.
3. In the rest of CEE the free route finds the entity and nothing else. Expect `unknown` and
   `private` to hide shutdowns there, and say so. On this book that is 22 rows, 6% of the base.

## 4. Coverage per evidence regime

- **Live site.** www.speedinvest.com is a Webflow site: 292 companies on a paginated list, each with
  the firm's "Year Invested", sector and team tags, an Exits tag, a country tag and a description
  that often states the exit in the firm's own words (54 cards). It publishes no round word.
- **Job board.** careers.speedinvest.com (Getro): 251 companies, 40 of them on no other live
  surface. Its stage field describes the company today and labels nothing.
- **Archive, Common Crawl 2012-2026.** 126 crawls read through the static index while the Internet
  Archive was in a machine-wide cooldown. The 2017-2020 WordPress listings carry the deal partner
  ("Investment Manager"), the firm's invest year, a Pre-Seed filter tag and an Acquired / Active
  filter; the 2017 team page lists each partner's own portfolio; the current site's per-company
  pages were captured from 2023 on and recover companies since removed. 345 companies; 82 on
  neither live list.
- **Archive, Internet Archive 2012-2016.** **Not read (debt, section 7).** Common Crawl crawled only the home page before 2017, and the Internet Archive was in a machine-wide cooldown for the whole run (re-armed by another session at 22:43). The pull is ready (`scratch/ia_pull.py`).
- **The firm's posts.** 719 posts from 2012 to 2026 (the old WordPress blog, the 2021-2023 blog, the
  live knowledge section), indexed per company.
- **EDGAR.** One exempt reporting adviser (Speedinvest GmbH, CRD 316774), whose Section 7.B table
  lists ten vehicles ($1.411B gross); three fund Form D filers; a roster sweep of 50 names that
  matched 36 issuers, two of them members; a full-text sweep with no third-party registrant
  (the one hit, Sea Containers 2002-2008, is a namesake).
- **Registers.** Section 3.
- **Press.** Google News, TechCrunch and Crunchbase News per row (419 rows, no failed lookup);
  twelve research agents over the grind, two over the A/B pass, two over a second stage pass, two
  over recall and one blind re-judge, each re-loading every URL it cited.

## 5. Recall probe and measured recall

**Recall additions: five, all from the firm's own words.** Kianava (the firm's 2020 post, "our lead
investment"), OBEY (the firm's own 2022-2023 portfolio page, which the archive parser had missed),
Flaneer and Prologue (called portfolio companies in the firm's posts) and Spiko (named "inside our
portfolio" in the firm's August 2026 crypto post; medium confidence, section 10).

**Rejected:** Trending Topics (section 10); Request Finance (the acquirer of a portfolio company,
sale consideration); Smint.io (held by Speedinvest Pirates, the service company, not a fund); and 54
more candidates the two recall agents opened: press headlines where Speedinvest is only a
related-story link or the named investor is Pirates, and names from memory that no page ties to
Speedinvest (Archify, Qriously, Wappwolf, Socialspiel and others).

**Measured recall.** A parametric enumeration listed 373 Speedinvest investments from memory; 334
were already rows, and none of the rest survived verification. The Google News sweep (409 headlines,
half-year windows 2011-2026, English, German and French) and the register's 37 named fund holdings
produced no company the firm's own surfaces lacked. Thirteen candidates were existing rows under a
legal or former name (1BillionLives GmbH is Flinn, Allfocal Optics is Lark Optics). The firm claims "400+ investments"; the base holds 386
companies plus the eight acquirers it lists.

## 6. Method deltas

- **The Austrian register as a backtrace layer** (`scratch/register_status.py`,
  `scratch/nd_vehicles.py`). North Data's free pages carry the Firmenbuch's publication stream,
  which names an Austrian GmbH's shareholders at each change. It settled the Scouts question,
  confirmed the Emmi AI sale to Mistral, and found four merges.
- **The firm's own exit sentences as status evidence.** 54 live cards state the exit ("acquired by
  PayU in 2019"); they are first-party citations (`sources/site/exit-statements.json`).
- **Merge detection from research.** The grind found 18 rename and successor groups
  (`companies/identity-merges.json`), among them three-name chains (Parkbob, Ubiq, Necture; Zerolens,
  Colorful, Mokker AI).
- **R1: banding a cited, unnamed first round.** 19 stages (11 Seed, 6 Pre-Seed, 2 Series A).
- **A second, narrower stage pass** on the 87 rows where the firm is provably in a round but the
  first round is unnamed: 23 named on a citation. With R1 and the tag (R2), rows with no round on
  record fell from 154 to 116.
- **Common Crawl through the shared throttle.** The Kleiner Perkins session reported the data host
  refusing the machine; both scripts now use `shared_throttle.wait("ccdata", rate=4.0)` with a
  60-second backoff on 403 and 503.
- **Model mix.** Every judge and research agent ran on the default model (Opus 5.5).

## 7. Flags and debt behind `verify`

**Flags on the 386 published rows:** `model_disputes_source` 15 (wrong Wikidata or SEC joins on
short names such as Grace, Well, Sona, Fuse, Tower, each noted), `city_unknown` 14, `stage_uncited`
12, `stale` 6 (Bitpanda, Wayflyer, Open, and TIER, Diligent and Tower from quarantined joins), `unstable` 4
(duty 7: Raus, wefox, Billie, Hitbox), `cik_weak` 4 (namesake registrants, quarantined),
`country_prior` 4 (Criad, Originator, Obey and Bleep: no location on record), `identity_unresolved`
1 (Bleep).

**Debt:**

- **The 2012-2016 /portfolio listing was not read.** The risk is a company listed only before 2017
  and removed since. What covers that era: the 2017 listing with its Exits section, the partners'
  own "Portfolio:" lines on the 2017 team page, the firm's 2012-2016 posts, and the parametric
  recall, which found no early miss. Run `scratch/ia_pull.py`, then `scratch/archive_listings.py`.
- 115 rows with the round not on record; 15 `unknown` statuses (sites dark, no register entry).
- About 20 rows rest only on the firm's job board (section 10).
- Google News answered 503 for the last third of the run, so the second stage pass and the blind
  re-judge worked from publisher site searches.

## 8. Standing duties and the A/B pass

- **A/B on the visible slice.** Ten rows attacked by two agents that re-loaded every URL they cited
  (`scratch/research/ab.json`, `ab2.json`). Three marks fell (GoStudent, TIER, wefox); seven stand.
- **Duty 2:** no $1B+ row reads `not_graduated`; no censored entry is past its clock.
- **Duties 3 and 8:** four weak SEC joins (Fuse, TIER, Diligent, Tower) are namesake registrants,
  quarantined.
- **Momentum slice:** 79 recent private rows in AI, fintech, data and developer tools carry a
  recorded web check; all stay below $1B. Six checks that had picked up unrelated news (a water well
  for Well) were corrected to the company's own site.
- **Duty 7, blind 5%.** 19 rows re-judged with no access to the record: 112 of 124 cells agree
  (90%; `documentation/duty7-blind.json`). Adjudicated: Raus is Seed on the contemporaneous
  announcement; wefox's HQ is Zurich; Billie's seed is a band, not a citation; Hitbox keeps the
  firm's own label.
- **Duty 9, the class.** The Billie pattern (a seed inferred from "existing investor" at the
  Series A) was not swept row by row; it is the softest part of the stage column.
- **Cross-investor:** 131 shared rows, 123 agree; 20 namesake pairs ruled distinct; 8 pairs accepted
  as stale sibling rows (section 15).

## 9. Firm profile

- **Thesis:** "The power of more." (the homepage headline).
- **History (71 words):** founded in Vienna in 2011 by Oliver Holle and former founders with a
  EUR 10M fund; Shpock, Bitpanda, GoStudent, TIER and Wayflyer; Speedinvest 4 at EUR 350M in 2024
  and more than EUR 1.2B managed.
- **HQ:** Vienna, from the ADV principal office (the site lists Vienna among six offices).
- **AUM:** $1,411,496,014 at both ends, the sworn Section 7.B gross values of ten vehicles; a floor,
  since the filing lists ten of 45 vehicles. The firm's own "over EUR 1.2 billion" ($1.39B) is noted.
- **Funds:** IV ($379.3M, 2022 vintage, final close 2024), III ($206.0M, 2020), II ($98.5M, 2015),
  I ($14.2M, 2011), each at the ECB rate of its announcement date.
- **Stages** Pre-Seed, Seed, Series A, Growth. **Geography** core Europe; other Middle East, Africa.
  **Scope** Generalist; focus from the site's sector tags.
- **Range:** $283,875 (the stated EUR 250K floor) to $34.1M (the EUR 30M growth cheque), median $3.5M
  over 194 stated entry rounds (a round size, not the cheque; press-based).
- **Notables:** Bitpanda, Tide, GoStudent, wefox, TIER. **Individuals:** 33, each with the LinkedIn
  link from the firm's own page.
- **Icon:** the firm's 512px favicon ("Si" on orange): contrast 3.0:1, edge ramp 1.25px.

## 10. Open rulings for Erik

1. **R1, banding a cited but unnamed first round** by the era ceilings (19 stages, 11 of them
   seeds that enter the S2A cohort on an uncited stage). The alternative is `undetermined` for all of them.
2. **R3, merger successors.** Invesdor, SILQ and Dott are out as successors of Finnest, ShopUp and
   TIER. ShopUp reads `acquired` (the merged group is a new parent); TIER reads `private` (Tier
   Mobility SE is the surviving parent). If both should read alike, say which way.
3. **Job-board-only rows stay members** (about 20: Rogue Cortex, Leap Labs, Tangram Data, Ray, Well,
   Criad, Originator, Infinite Games, CareerOS, OpenQ, Ralph and others). The board is the firm's own
   list, but no round names Speedinvest for them.
4. **Spiko is a member on one sentence** ("inside our portfolio"), which also names Request Finance,
   a sale-consideration holding. No round names Speedinvest.
5. **Trending Topics is rejected.** The company's own 2017 post names Speedinvest in a EUR 170K
   consortium; neither the post nor the register says which entity held it, and the firm never
   lists it.
6. **Heroes Jobs is a member on the director-of-record pattern** (Mathias Ockenfels on both Form
   Ds); no page names Speedinvest.
7. **Positions first held by the Pioneers Ventures vehicle** (byrd, Necture and others): the entry
   reads `undetermined`, since that round is unnamed. If a pre-takeover Pioneers position should not
   count as the firm's entry, the entry is the later round.
8. **GoStudent, TIER and wefox below $1B.** Each rests on collapse evidence, not a priced round
   (a write-down, a merger valuation in the press, a proposed sale price).
9. **Criad, Originator, Obey and Bleep carry the home-desk country (AT)** with `country_prior`; no
   location is on record.
10. **Polaron and Playbrush stay `undetermined`**, each with a named round that is not the entry.
11. **R2, the firm's 2018-2020 Pre-Seed filter tag labels 25 rows at medium.** It scored 3 of 3 on
    rows with an independently documented round, too few for `high`.
12. **wefox reads Zurich** (the holding's seat), not Berlin (the operating base), after the blind
    re-judge disagreed. Seedcamp's row for the same company reads Berlin, so the two books differ
    on the city until this is ruled.
13. **The eight acquirers the firm lists are out** (OpenAI, Mistral, MoonPay, Perk, Mews, Dialpad,
    Taxfix, OneTrust), under the sale-consideration ruling. Listed here because OpenAI and Mistral
    are names a reader will look for.
14. **a16z's June.** If it is june.so, a16z's row should read `defunct` like Point Nine's and this
    book's; if it is the June oven, `acquired` is right and the pair is a namesake. a16z's book does
    not say which.

## 11. Rebuilds and deltas

The grind judged 419 rows. The scheduled rebuild removed 23 `not_member` rows and merged 12
duplicates (384 rows). A second, final rebuild landed five recall additions and three more merged
duplicates (386 rows); it was needed because the recall probe finished after the first rebuild, the
case §8 allows. The rename list was read after each: no verdict moved onto another company. 48
published names are set in `config.json` `names.published`.

## 12. Playbook write-backs proposed (not applied)

1. **The coverage rule of section 3** for §5: sequence European firms by their own record, not their
   register; the free-register table per jurisdiction, with Austria and Estonia added.
2. **Austria in the §5 country table:** Firmenbuch, backtrace yes (free through North Data's
   publication stream, holders named when few), forward by paid tier only, status free.
3. **Read the firm's card text for sale consideration before seeding a member.** A card that says
   "became a shareholder in X following its acquisition of Y" is the firm disclaiming the position.
4. **R1** for §6, if Erik keeps it: a cited unnamed first round with an amount bands like a Form D
   round, with the PRO-157 older-company guard.
5. **Merger successors** for §1 T3: a successor the firm lists beside the original is the same
   position.
6. **`graduation-surfaces` local editions** for PL, CZ, HU, RO, BG, HR, SI, EE, LT, TR; and the
   momentum fallback must not take a news item for a common-word name (Well, Ray, Dream).
7. **A shared register-status script.** `register_status.py` (suggest endpoint, exact-name match,
   events, named holders) is the third per-run copy; it belongs in `scripts/`.
8. **Research agents must not touch the Internet Archive during a machine-wide cooldown;** the
   brief should say so, and `pkill -f news.py` by one agent can kill a sibling's query.
9. **The archive parser needs a per-page fallback to the URL slug** where a page title is generic
   (the OBEY miss).
10. **`verify`'s link sample should pass when the base holds no SEC link** (Seedcamp reads "none
    sampled" and fails plain `verify` forever; every European book without Form D rows will).
11. **Before its ingest, a run should run every landed sibling's `verify` and look for its own
    rows.** Rule 10 is not symmetric where a sibling publishes "Name (domain)" pairs: the Fuse
    disagreement appeared only on YC's side.
12. **Research agents' fetched pages belong in `data/filings/site-raw/<slug>/`** (untracked), not in
    `scratch/`: this run's scratch reached 206 MB before the close moved them.

## 13. Usage line

**Kickoff (Opus 5.5):** five-hour window 18%, weekly 43%, Fable 5%. **Close:** five-hour window 26% (a later window), weekly 72%, Fable 8%. The weekly figure is the whole account's: other collection sessions ran on this machine at the same time, so the 29 points are not this run's alone.
The run paused once at the usage limit. 386 rows.

**Web searches:** about 165 of the 200 cap, nearly all by the research agents (8 each for the twelve
grind groups, the A/B, recall and stage passes, the blind judge). **Subagents:** 19.

## 14. Prompt count

**3**: the kickoff, "continue", and "continue" after the session paused at the usage limit. No correction and no ruling was given during the run. The target is one.

## 15. Ingest

**Speedinvest is live.** Closing commit `f7800fd4`, then the gate of COLLECTION.md §9 in order:

| Step | Result |
|---|---|
| Plain `verify` | clean |
| Icon upload | `investors/speedinvest-39dadf6ebf.png` (512px source, contrast 3.0:1, ramp 1.25px) |
| `ingest-investor.ts` | 1 investor row upserted |
| `ingest-companies.ts --dry-run` | 386 new, 0 removed, from 0 live (nothing to explain) |
| The write | 386 of 386 upserted |
| Readback (`--investor-row`) | csv 386, live 386, missing 0, extra 0, differing cells 0 |

**Stale sibling rows, one book at a time** (kit: `scratch/align/`, each line cites the underlying
evidence):

| Book | Rows | Result |
|---|---|---|
| Accel | Luko `private` to `acquired` (Allianz Direct, January 2024, TechCrunch) | Aligned and re-ingested, readback exact (`c7acb7ac`) |
| Seedcamp | Fleksy and Fraugster `unknown` to `defunct`, Stowga `unknown` to `acquired`, wefox `1b_plus` to `below_1b` | Aligned and re-ingested, readback exact (`ea8c2c42`) |
| Y Combinator | Diligent (`acquired`, should be `private`), June (`acquired`, should be `defunct`) | **Skipped at the gate.** The readback before any write shows one row missing and one extra, both named Metadata: drift this run did not make. Both pairs stay accepted in `cross-rulings.json` and are owed at YC's next clean ingest |
| a16z | June (`acquired`) | **Not aligned, on purpose.** a16z's row is a bare name on its investment list; nothing in its book says whether it is june.so or the June oven that Weber bought in 2021, for which `acquired` is right. Section 10, ruling 14 |

Two things the alignment surfaced:

- **A namesake this run's ingest would have broken in YC's book.** YC publishes two Fuses; the name
  key joined Speedinvest's Fuse (fuseinsight.com, London) to YC's other one (letsfuse.com, New
  York) through a weak CIK, and YC's `verify` failed on it although Speedinvest's did not. Ruled
  `distinct`, with a `same` pair for the right row, in this book's `cross-rulings.json`; YC's
  `verify` is clean again. Every other landed book's `verify` was checked for Speedinvest rows: none.
- **Seedcamp's plain `verify` fails on a check that cannot pass**: the link sample reads "none
  sampled" because the base holds no EDGAR or Form D link. The alignment ran its gate with
  `--skip-links` for that book and nothing else differs. Write-back 10.

Five books were in flight and not compared (Atomico, Bain Capital Ventures, Founders Fund, General
Catalyst, Kleiner Perkins); the Fleksy pair with Kleiner Perkins (Fleksy Inc. of San Francisco, a
different company from ThingThing Ltd) is already ruled `distinct` for that run.

