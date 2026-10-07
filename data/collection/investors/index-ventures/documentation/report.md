# Index Ventures: Build & Reconciliation Report (PRO-82)

**Linear issue** PRO-82 · **slug** `index-ventures` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session, interrupted once and resumed · report written
2026-10-06.

---

## 1. The answer PRO-82 asked for

**The base is 560 companies, plain `verify` is clean, the firm profile is built and the review
surface renders. Ingest status is in section 15. Section 16 holds what changed after the close on
Erik's two instructions of 2026-10-06: the headquarters reads London, and the European registers
were swept (22 status corrections). The numbers in this report are the ones after that sweep.**

PRO-82 asked one question the earlier runs did not have to answer: how a base states its coverage
when the evidence is structurally uneven inside it. The answer this run gives:

- **Every row carries one of two regimes, derived from its own evidence columns, never from where
  the company is based** (`decisions.md` D9). `sec`: the row has an SEC surface of its own, that
  is a Form D by the issuer, an ownership or Section 16 filing by an Index fund, or a third-party
  registrant's filing that names the fund and the company. `firm_record`: the row rests on the
  firm's own listing, its archive, its posts and press.
- **100 rows are SEC-visible and 460 rest on the firm's record.** That is 18% against 82%.
- **The split is not a US against Europe split.** Only 80 of the 302 US rows have an SEC surface
  (26%). 16 of 226 European rows have one (7%), 2 of 16 Israeli rows. A US company that never
  filed a Form D is `firm_record`; Adyen and Criteo, which filed with the SEC, are `sec`.
- **Membership is filing-grade in both regimes.** A listing on the firm's own site suffices alone
  (COLLECTION.md §1), and 532 of 560 rows have one. The published tier column does not track the
  regime: SEC-visible rows are Tier A (91) or C (9), firm-record rows A (208), B (233) or C (19).
- **What differs by regime is recall and the evidence behind the classification**, and section 4
  reports both per regime, never blended. The short version: the SEC side found 9 companies the
  firm's record does not list; the firm's record carries 460 companies the SEC side cannot see;
  the entry stage is unknown for 1% of SEC-visible rows and 13% of firm-record rows.
- **The reporting contract for the mixed-geography firms that follow** is the table in section 4,
  computed by `scratch/regime-report.py` from `base.json` and the merged classification. The
  published CSV carries the columns it is computed from, so a reader can recompute it.

Index is one firm: Index Ventures SA in Geneva (CRD 161175), an exempt reporting adviser to Jersey
and Delaware funds, run from San Francisco, London and New York. Its Form ADV lists 32 private
funds with $25.3B of gross assets.

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean at 560 rows; flagged debt only (section 7) |
| Distributions sanity-checked | Section 2, against eleven other books |
| Coverage per evidence regime, never blended | Section 4 |
| Profile through the taxonomy gate | `build-firm-profile.py` and `profile_copy.py` ok (section 9) |
| `review.html` rendered | 560 of 560 rows, profile panel opens, no console errors |
| `report.md` with method delta, open rulings, prompt count | This file; three rulings (section 10); prompt count 4 (section 14) |
| COLLECTION.md diff proposed | Section 12 |
| Ingest through the §9 gate, stale sibling rows aligned | Live at 560 rows, readback exact; 36 sibling rows in 20 books re-ingested (section 15) |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 560 | all nameable |
| Private | 275 | 49.1% |
| Acquired | 210 | 37.5% |
| Defunct | 41 | 7.3% |
| Public | 26 | 4.6% |
| Unknown | 8 | 1.4% |
| $1B and above | 91 | 16.2% |
| of which $10B and above | 21 | |
| of which $100B and above | 5 | Facebook, Anthropic, Arista Networks, Revolut, Robinhood |

**$1B and above** (last priced round, or market capitalisation for the 20 public rows in the band):

- $100B+: Facebook $1,890B (public), Anthropic $965B, Arista Networks $270B (public), Revolut
  $115B, Robinhood $105B (public).
- $10B+: Datadog $96.3B (public), Pure Storage $42.0B (public), Adyen $31.4B (public), Scale
  $29.0B, Roblox $27.5B (public), Mistral $24.4B, Cohere $20.0B, Fireworks $17.5B, ClickHouse
  $15.0B, Discord $15.0B, Temporal $12.6B, Wise $11.8B (public), Aurora $11.7B (public), Figma
  $11.1B (public), Notion $11.0B, Instinct $10.0B.
- $1B+ (70 rows): Elastic, Personio, Fireblocks, Plaid, OZON.ru, Dropbox, Etsy, Alan,
  ServiceTitan, Physical Intelligence, Collibra, Ineffable, Coalition, Cockroach Labs, Dream
  Games, Wonderful, Gong, Decagon, Patreon, Tekion, Chai Discovery, Goat, Starburst, ApplyBoard,
  Remote, Motive, Garner Health, Linear, Algolia, Sonos, Multiverse, Viagogo, BlaBlaCar, Cowboy
  Space, Iterable, Kong, Kry, Persona, DeepL, Parallel Web Systems, Simile, Ankorstore,
  Capitolis, Nourish, Productboard, SafetyCulture, Pave, Wealthfront, Built, Culture Amp,
  Flapping Airplanes, Granola, Harmonic, Gruppo MutuiOnline, Linktree, Instabase, Pilot, Rohlik,
  Glow, Spendesk, Trustpilot, Beamery, DataSnipper, Expel, Motorway, Swile, Taxfix, LiveKit,
  Revel, Thatch.

By the pipeline's convention an acquired company carries no band, so Skype, Slack, Wiz, King,
Supercell and MySQL read `below_1b` here as they do in every other book.

**Entry stage.** Series A 198, Seed 158, Growth 142. For 62 rows (11%) no source names the round
in which Index entered, so they read `undetermined` (section 7). Of the 498 decided stages, 276
cite a round announcement, 41 the firm's own label or post, 42 rest on the row's own Form D
sequence, and 139 are the judge's reading without a citation.

**Headquarters.** US 302, GB 113, FR 28, DE 20, IL 16, NL 11, then a tail of 24 countries. 553 of
560 rows carry a city (San Francisco 118, London 104, New York 63, Paris 26, Tel Aviv 15).

**Focus.** Consumer & Marketplaces 133, SaaS 98, Fintech & Payments 71, AI & Applied AI 67, Media,
Gaming & Advertising 54, Data Infrastructure 35, Security 34, DevTools & APIs 25, Healthcare & Bio
15, Industrial & Robotics 15, Crypto & Web3 7, Climate & Energy 5. One row (Second Home, a
workspace operator) sits outside the taxonomy.

**Membership evidence.** Site listing 532, press or the firm's own post 21 (recall additions),
Form D adjudicated 6, fund filing 1 (Cyngn).

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 158 | 16 | 142 | 100 | 42 | **70.4%** |

Coverage is 100%. Of 158 seed entries, 16 were too recent to count; of the 142 that remain, 70.4%
raised a later round. Of the 42 that did not, 22 rest on a cited end (a sale or shutdown before any
Series A) and 20 on a dated search of the named surfaces. Seven of the cited ends came from the
register sweep (section 16).

- **By entry period:** to 2011, 3 of 8; 2012-2015, 25 of 37 (68%); 2016-2019, 17 of 17;
  2020-2022, 34 of 47 (72%); 2023 on, 21 of 33 (64%), with all 16 censored rows in that period.
- **Caveat 1, the rate is a ceiling.** The 2016-2019 cohort graduates 17 of 17. That is not a
  result, it is survivorship: the firm's site drops companies that fail, the 2016-2017 captures
  are thin (86 and 30 rows), and a seed that was never announced and then dropped leaves no trace
  on any surface this run read. The recall probe found nine such seeds for 2012-2015 through
  press and sibling books (section 5), and five of those nine did not graduate. The same gap for
  2016-2019 is unprobed.
- **Caveat 2, entry dates.** 40 seed rows are staged by the firm's own "backed at Seed" mark, which
  publishes no year. For 18 of them the entry year is the year the firm first listed the company,
  an upper bound (R1). It never makes a row censored and a no decided on it is conservative.
- **Caveat 3, the 62 undetermined rows are outside the cohort.**

### Calibration

| Book | Rows | Acquired | Defunct | Private | $1B+ | S2A | Stage unknown |
|---|---|---|---|---|---|---|---|
| Index Ventures | 560 | 37% | 6% | 49% | 16.2% | 100/142 = 70% | 11% |
| Accel | 884 | 27% | 4% | 62% | 13.8% | 143/242 = 59% | 3% |
| Lightspeed | 875 | 30% | 7% | 51% | 14.7% | 89/156 = 57% | 24% |
| Redpoint | 413 | 35% | 15% | 41% | 14.8% | 25/39 = 64% | 23% |
| Kleiner Perkins | 890 | 49% | 5% | 26% | 14.4% | 50/60 = 83% | 53% |
| NEA | 1,110 | 50% | 5% | 33% | 8.6% | 102/161 = 63% | 37% |
| Greylock | 553 | 59% | 12% | 22% | 8.0% | 43/51 = 84% | 55% |
| Benchmark | 284 | 51% | 18% | 14% | 8.5% | 7/7 | 66% |
| Atomico | 164 | 29% | 10% | 52% | 19.5% | 6/13 = 46% | 26% |
| Balderton | 281 | 40% | 9% | 46% | 7.5% | 18/36 = 50% | 22% |
| Creandum | 177 | 29% | 5% | 61% | 11.9% | 36/71 = 51% | 2% |
| Northzone | 220 | 28% | 4% | 49% | 5.0% | 12/19 = 63% | 56% |

Index sits with Accel, Lightspeed and Redpoint on status mix and $1B+ share, which is where a
transatlantic multi-stage firm should sit. Before the register sweep its defunct share was 5% and its unknown share 6%: 33 companies had no
trace of an end and no sign of life, 20 of them European. The registers settled 15 of those 20
(section 16) and the check outside Europe 10 more (section 17); 8 rows read unknown now, 3 of them European.
The S2A rate is above the US books for the reason caveat 1 gives.

## 3. The boundary

Ruled once in `documentation/decisions.md`; 84 rows are in `excluded.json` with their evidence.

- **One firm (D1, D2).** Every fund of Index Ventures SA is in: Index Ventures I to XIII, Growth I
  to VII, Origin I to III, the SPVs, the entrepreneur and co-investment vehicles. Yucca, the
  staff co-investment scheme that co-files with the funds, makes no rows of its own.
- **The life sciences desk (D3).** Out: 47 rows of 42 companies (Genmab, Novocure, Micromet,
  Molecular Partners, Addex, Versartis, Minerva and others). Medicxi started in February 2016
  and by its own launch release "comprises all of the legacy portfolio companies, funds and the
  life sciences team of Index Ventures". This follows the Benchmark Europe and Balderton
  precedent. It is the first open ruling (section 10).
- **Pre-fund positions (R2).** Out: 9 rows (Aptix, ArrayComm, Biocom, Calico Commerce, CommQuest,
  NeoVista, Optimer, SCM Microsystems, Virata). The firm's own 1999-2002 portfolio page heads
  them "Prior investments", apart from the group it heads "Index Ventures I, L.P.". That is the
  standing fund-money rule (Erik, 2026-09-26). Evolve Software stays: the 2001 page carries it in
  the fund's group.
- **A partner's earlier deals.** Seven names the 2002 pages mark "* Denotes prior investments of
  Index Partners" never become rows (Infospace, Vignette, Critical Path, Crossgain, Neoteris,
  Signio, Tellme): partner-carried (Erik, 2026-09-17).
- **Person or firm (D5).** The Form D roster sweep read 312 accessions. 15 rows are out because
  the seat is another firm's money (Ilya Fushman's Kleiner Perkins boards after 2018 above all:
  Loom, Zumper, Stord, Cameo; Erin Price-Wright's Andreessen Horowitz boards; Molly Alter's
  Northzone seat) and 9 because the name is a homonym (a Dr Mark A. Goldberg on
  five biotech boards, a US Ben Holmes, a New York Greg Marsh). Six Form D rows are members:
  Fleetsmith, Optimizely, Skyport Systems, Zesty, Imzy and Netomi, each with an Index partner on
  the board inside their time at the firm and a round the firm is on record in.
- **Venture entry and sale consideration (D6).** Out: ASOS (no venture round), Conexant and
  Greenfield Online (stock received for a portfolio company). Facebook stays as a secondary.
- **Fund-shaped (D4).** Seedcamp is out: an LP-class stake in another investor.
- **Identity.** 38 merges (Lithic was Privacy.com, Kong was Mashape, Raisin was SavingGlobal,
  Drivy was Voiturelib, UberMedia was TweetUp, Daydream is Dahlia Labs, Parallel is Kiosk Inc).
  Cue the calendar app and Cue Labs (Greplin) are two companies and two rows.

## 4. Coverage per evidence regime

| | SEC-visible | Firm record | All |
|---|---|---|---|
| Member rows | 100 | 460 | 560 |
| Share of the base | 17.9% | 82.1% | 100% |
| US rows in the regime | 80 of 302 | 222 of 302 | |
| European rows in the regime | 16 of 226 | 210 of 226 | |
| Rows known only through this regime's sources | 9 | 460 | |
| Membership evidence | site listing 91, Form D adjudicated 6, press 2, fund filing 1 | site listing 441, press or own post 19 | |
| Tier | A 91, C 9 | A 208, B 233, C 19 | |
| Entry stage | Series A 48, Growth 39, Seed 12, undetermined 1 | Series A 150, Seed 146, Growth 103, undetermined 61 | |
| Stage undetermined | 1.0% | 13.3% | 11.1% |
| Stage source, decided rows | Form D sequence 42, round announcement 35, uncited 21, firm's label 1 | round announcement 241, uncited 118, firm's label 40 | |
| Status | acquired 41, private 36, public 15, defunct 7, unknown 1 | private 239, acquired 169, defunct 34, public 11, unknown 7 | |
| $1B and above | 22 | 69 | 91 |
| Seed entries / censored / cohort | 12 / 0 / 12 | 146 / 16 / 130 | 158 / 16 / 142 |
| Graduated / not graduated | 10 / 2 | 90 / 40 | 100 / 42 |
| S2A | 83.3% | 69.2% | 70.4% |
| Graduation decided by | firm's post 5, Form D 3, round announcement 3, dated search 1 | round announcement 69, firm's post 35, dated search 26 | |

What the table says, in order of weight:

- **Recall.** The SEC side adds little to membership for this firm: 9 companies (6 Form D
  adjudications, Cyngn from an investors' rights agreement, Familiar and Nauto from third-party
  filings). Index's funds are Jersey partnerships that file 13Gs and Form 4s only on listed
  winners, and those are all on the firm's site already. The firm's record is the base.
- **The stage column is where the regimes differ.** Where a company filed Form Ds, the sequence
  of offerings dates and sizes the entry, so 99% of SEC-visible rows carry a stage. Where it did
  not, the stage needs a dated announcement naming the firm, and 13% of firm-record rows have
  none. The 62 undetermined rows split 32 Europe, 26 US, 4 elsewhere, so this is a regime
  effect before it is a geography effect.
- **Status.** 7 of 8 unknown rows are firm-record rows (31 of 33 before the register sweep and the check of section 17). A
  company that filed nothing with the SEC leaves no SEC trail when it dies; its home register is
  where the end shows.
- **S2A is not comparable across the two columns.** The SEC-visible cohort is 12 rows. The
  firm-record cohort (130) carries the number.
- **The home registers.** At the close they had been read row by row in a handful of cases, not
  swept, although D10 ordered status first from the registers. Erik asked for the sweep the same
  day and it is done (section 16): Companies House for the UK with its register of controlling
  owners, Sirene for France, and the open Swiss, Czech, Estonian, Finnish and Danish registers.
  It is a status layer, not a membership layer: no register here shows a venture fund's holding.

What carries the base, by layer:

- **Live site.** A Wagtail API: 329 companies with deal partner, sector and a "backed at Seed"
  mark; a team page of 49 people; 586 Perspectives posts, all read.
- **Archive, 2008 to 2025.** Common Crawl, 17 annual eras, 30 to 199 rows each. The Internet
  Archive excludes nothing here but refused this machine three times (see section 7).
- **Archive, 1999 to 2002.** 23 Internet Archive pages: the first site's portfolio pages and the
  November 2002 database pages. 38 companies, 7 of them new member rows.
- **SEC.** 48 fund and general-partner filers, the roster Form D sweep (312 accessions), the
  full-text sweep of third-party registrants naming the firm, the Form ADV.

## 5. Recall probe

22 companies entered that no captured list of the firm carries (R3), each on a source that names
the firm in the round:

- Recent rounds not yet on the site: Instinct (the $250M Series B co-led with Benchmark; two
  outlets and the Wall Street Journal), Uncovr (the firm's own post).
- Sold before it was listed: LESS (the firm's own post; bought by BlaBlaCar five months later).
- The 2012-2015 seed programme: Gojimo, Strikingly, Yup, Leap Transit, DJZ, Little Borrowed
  Dress, Lookback, Pets Deli, Familiar. Five of these nine did not graduate.
- Minority participations: Flipagram, bonify, Italic, Sphere, Dazz, Nauto, Snapguide, Cyngn.
- One led Series A (SourceClear) and one unannounced round (Cue Labs).

Sources of the leads: Wikipedia (10), sibling books' notes (5), EDGAR full text (3), the firm's
own posts (2), the press sweep (2). Wikipedia was a lead and never a citation.
Rejected with reasons in `scratch/web-finds.json`: Spot.IM (the release body names other leads
than its URL), Town (talks), Augmeta (a scout cheque).

The tail is not closed. Finding 22 unlisted companies with a probe this shallow means more exist,
most likely small participations before 2016.

## 6. Method deltas

- **Regime by evidence columns, not geography (D9).** Section 1 and 4.
- **One desk (D1).** PRO-82 expected `desks` to partition by domicile. The verified facts are one
  adviser, one fund family and one book run from three offices, so there is one desk, the
  adviser. What the partition was meant to carry, the regime column carries.
- **A successor firm owns a desk's book (D3).** Applied to a desk that invested from the same
  funds as the rest of the firm until 2012, which the Benchmark precedent did not cover.
- **The firm's own stage marks, scored before use (D8).** The live list's "backed at Seed" mark
  was tested against documented entries: 31 of 36 right. It is accepted as `first_party` at
  medium. The 2012-2013 list's "Seed stage" filter alone is accepted at low; a row under both
  its Seed and Early stage filters is refused.
- **Entry dates for label rows (R1).** The seed's own dated announcement, else a sibling's cited
  entry, else the first-listing year as an upper bound.
- **An unnamed later round below the step-up does not graduate (R5).** Atlar, Beryl, Hyperline,
  Gojimo. Yup is the mirror case: an unnamed $16.0M Form D round, above twice the seed money,
  graduates.
- **Stage by sequence.** Where the record shows the firm in the round before a named Series A
  (Crossing Minds) or before a named Series B with one round preceding it (Innovative Silicon),
  the entry takes the stage the sequence gives. This came out of the blind check.
- **EDGAR's entity table for the Form D leg of an absence test.** EDGAR full-text search does not
  index Form D issuers, so an empty result there is a failed lookup. `scratch/formd-lookup.py`
  reads the entity-name table and the submissions index.
- **Form ADV 7.B as the asset figure.** An exempt reporting adviser files no Item 5.F; the sum of
  the 32 funds' gross asset values is the sworn number (the Creandum precedent).
- **The icon.** The site's mask-icon vector, recoloured to the red its own tag declares.

## 7. Flags and debt behind `verify`

Plain `verify` is clean. What it passes over, by count:

| Flag or debt | Rows | What it means |
|---|---|---|
| `model_disputes_source` | 97 | the judge overrode a pre-filled value (a stale float, a one-word name join); each has a note |
| `stale` | 43 | a pre-filled float older than its row's cited value |
| `unicorn_name_match` | 39 | the vendor list matched by name; the band is cited separately |
| `stage_disputes_band` | 25 | the judged stage differs from the Form D band; 18 cite a source, 7 do not |
| `stage_uncited` | 21 | a decided seed row whose stage has no citation; its own evidence decides the graduation |
| `cite_pending` | 18 | a $1B+ row on an uncited stage: Algolia, Ankorstore, Anthropic, Collibra, Criteo, Culture Amp, Dropbox, Etsy, Facebook, Fireblocks, Gruppo MutuiOnline, Motive, Patreon, Physical Intelligence, Sonos, Swile, Tekion, Viagogo |
| `cik_weak` | 16 | a name-only CIK join; each was audited, none carries a float it does not fit |
| `country_prior` | 12 | country inferred, not cited |
| `city_unknown` | 7 | Arca, Dot Product, Dropshop, Flagship, Grupo Xango, Hoop, Quixotic |
| `boundary` | 2 | Arista Networks and Sonos (below) |
| `suspect_base` | 1 | Instinct: a $10B row the firm does not list yet; two outlets name the firm as co-lead |
| Stage undetermined | 62 | 17 first listed before 2006, 17 in 2006-2012, 28 since |
| Stage uncited (`model`) | 139 | the judge's reading with no citation, 25% of rows |

Soft spots a reader should know:

- **Arista Networks, $270B.** On the firm's own list since 2014 with Mike Volpi as partner, so it
  is a member by the listing rule. No source read names a round Index joined, and the company
  was financed by its founders. The stage reads undetermined. It is the largest row whose entry
  is undocumented.
- **Facebook, $1,890B.** A late secondary before the IPO, listed by the firm 2013-2022. Growth,
  uncited.
- **Internet Archive, 2003 to 2007.** Not read. The Archive refused this machine three times
  during the run (the third time after three pages at four seconds' spacing) and the machine-wide
  cooldown held each time. The firm's 2008-2016 lists carry a "past investments" section that
  covers most of what those pages would add, but a company listed only between 2003 and 2007
  and dropped by 2008 is missing. 26 target pages are queued in `scratch/ia-pass2.py`.
- **Home registers.** Swept after the close (section 16). Five European rows still read unknown:
  Tactic, OpenBuildings, Futurelytics, Rad and Webfair. Germany, the Netherlands, Sweden, Spain
  and Belgium have no open register this run could query in bulk; their rows got the news check
  only.
- **The 2016-2019 seed gap** (section 2, caveat 1).
- **Disk.** The machine ran out of disk space on 2026-10-01 at about 15:12 UTC. Nothing was
  lost: raw captures under `data/filings/index-ventures` are gzipped since, and the 12
  Perspectives posts that failed to save were re-read (586 of 586).

## 8. Standing duties and the A/B pass

1. **Every $1B+ claim web-verified.** 91 rows. 88 carry a cited round or a market capitalisation
   read on 2026-09-25 or 2026-10-06; 3 carry the vendor list's mark with a sibling book's
   citation. Changes taken: Cohere $20B (the Aleph Alpha merger), Temporal $12.55B, Capitolis
   $1.9B, Flapping Airplanes $1.5B, Revel $1.0B, Instabase $1.24B (a down round), Criteo below
   $1B, Outbrain (now Teads) $56M, Instinct $10B.
2. **Every no vetted, every censored clock read.** No $1B+ or public row is a no. All 16 censored
   rows are inside 24 months today; /dev/agents (November 2024) runs out next month.
3. **Weak CIK joins.** 16 audited; none carries a float it does not fit.
4. **Stale float to acquired.** Viagogo is StubHub Holdings (public since 2025); Outbrain is
   Teads; SCM Microsystems (now Identiv) left with R2.
5. **Public rows for deaths.** None. Cyngn trades at an $8.8M capitalisation.
6. **Unicorn list re-intersected** with loose normalisation: no alias miss.
7. **Blind re-classification of 5%.** 28 rows drawn with a fixed seed and judged by a second
   agent that could not read the classification. 177 cells compared, 158 agree (89%), 19 differ
   on 11 rows. Six rows corrected from the blind answers: Crossing Minds (Seed, graduated),
   Innovative Silicon (Series A), Frontback (entry a year earlier with a citation; the product
   changed hands, so acquired), NumberFour (insolvent in 2024, remains bought in 2025:
   acquired), Catch (San Francisco; a funding claim in the note belonged to a namesake),
   UberMedia (an uncited Series A reverted to the Form D band, graduated). Kept against the
   blind answer, with the reason in each note: Catch's status and stage, Feathery (the blind
   source is a secondary write-up), King's stage and city, Innovative Silicon's status and
   city, three focus calls. One cell was a convention the blind judge was not told (an acquired
   row carries no band). The blind judge also caught an error in its own brief: the brief
   described the wrong Catch.
8. **Float name collisions.** Familiar, Sphere, Jumbo, Sofar, Scope and Flagship carried one-word
   Wikidata countries of other companies; each was overridden and noted.
9. **A hit is a class.** Two classes swept after duty 7. Undetermined rows where the record
   shows the firm in before a named later round: 62 notes re-read, the two sample rows were the
   only ones. Judged stage against the Form D band: 26 rows, 23 already flagged, 2 flags added,
   1 uncited override reverted.

**Momentum slice.** 140 recent rows in hot sectors got a mechanical news check; it produced the
Cohere, Temporal, Glow and Nourish marks.

## 9. Firm profile

| Field | Value | Source |
|---|---|---|
| HQ | London, United Kingdom | Erik's ruling of 2026-10-06, recorded as a judged override; the rule's own reading was San Francisco, the first office the site lists |
| Founded | 1996 | Wikipedia and the firm's "30 Years In" post |
| Thesis | "We invest in who you are, not just what you do." | the firm's homepage headline, verbatim |
| Stages | Seed, Series A, Growth | the base |
| Geography | core Europe and US, other Israel | the base |
| Focus | SaaS, AI & Applied AI, Fintech & Payments, Media, Gaming & Advertising, Consumer & Marketplaces, Security, Data Infrastructure | the site's own sector tags through a crosswalk, floor 15 companies |
| Round range | $1M to $300M, median $17M | 258 sized entry rounds; a round size, not a cheque size |
| Notables | Skype, Dropbox, Slack, Discord, Roblox | the five best known |
| AUM | $25.32B | Form ADV 7.B, 32 funds, filed 2026-03-31 |
| Funds | 17, Index Ventures V (2009) to XIII (2026) | the firm's own announcements |
| People | 49: 26 on the investor tab, 23 strategists and operators | the team page; 46 LinkedIn links, 8 X links |

- **HQ London.** The rule gave San Francisco because the site lists it first. Erik ruled London
  on 2026-10-06: the team page has 22 people there against 14 in San Francisco and 10 in New
  York. It is `profile.hq_override` in `config.json`, with the flaw and the basis written out.
- **Positions.** The site publishes no titles. The 26 people on its investor tab publish as
  "Partner", the shared build rule; the other 23 publish with no position.
- **AUM includes Life VI** ($212M), whose companies are outside the base, and predates the July
  2026 funds.

## 10. Open rulings for Erik

Three. Everything else was settled by a standing rule or by research.

1. **The life sciences desk (D3): out, 47 rows.** The cost is Genmab, Novocure and the rest of
   the biotech book, which Index funds bought and Index listed for fifteen years. The reason is
   the Medicxi statement and the Benchmark Europe precedent. If in, the rows return on one
   rebuild and need classifying. R4 rides with it: Novocure, Infection Control, Diartis and
   DirectMedica were ruled with the desk on what they are, with no capture showing their desk.
2. **Pre-fund "Prior investments" (R2): out, 9 rows.** Decided by the standing fund-money rule.
   The case for the other reading: these were the same team's deals at the same firm before it
   raised a pooled fund, not a founder's personal angel book, and the firm kept four of them on
   its lists until 2016. If in, they return on one rebuild; all nine are pre-2000 entries with
   the stage undetermined, so no published rate moves.
3. **Arista Networks: in, on the listing alone.** A $270B row with no documented round. The
   listing rule keeps it; the unverified-position rule (2026-09-28) would not apply because the
   firm itself lists it. Erik may know how Index came to hold it.

## 11. Rebuilds and deltas

| Step | Rows | What changed |
|---|---|---|
| First build, 2026-10-01 | 618 | the grind's base |
| Rebuild 1, 2026-10-06 | 571 | 73 rows out on recorded verdicts, the identity merges applied, 22 recall additions and 12 Archive rows in |
| Rebuild 2 | 564 | the delta's 7 exclusions out |
| Rebuild 3 | 560 | 4 name variants of excluded life-desk rows out (below) |

No evidence layer changed between the three rebuilds of 2026-10-06. Rebuilds 2 and 3 only removed
rows already ruled out.

**The re-key trap, again.** Each rebuild's rename step paired an excluded slug with a name
variant that then stood alone (Acutus and Acutus Medical, Addex and Addex Pharma, Ariad twice,
Aegerion twice) and moved the verdict onto it, so the variant was excluded next time and the first
name came back. One move crossed companies (Oxyplus onto Aegerion). Fixed as the BCV note says:
both variants now hold their own verdict in the ledger, and rebuild 3 renamed nothing.

Delta judged after rebuild 1: 36 rows (22 recall additions, 7 Archive members, 5 pre-fund rows
out, Oxyplus and Opentest out).

## 12. Playbook write-backs proposed (not applied: scripts/ and COLLECTION.md belong to the tooling session)

1. **§9 or §10, the per-regime report.** A base with two evidence regimes reports the table of
   section 4. The regime is derived from the row's own evidence columns. Geography is a second
   cut, never the definition.
2. **§5, EDGAR full-text search does not index Form D issuers.** An empty full-text result for a
   company name with `forms=D` is a failed lookup. The Form D leg of an absence test reads the
   entity-name table and the submissions index.
3. **§5, sibling notes as a recall layer.** Grep every landed book's notes for the firm's name.
   Five of this run's 22 recall additions came from a sentence another run had already cited.
4. **§1, two classes of "prior" on a firm's own site.** "Prior investments" of the firm before
   its first fund is the fund-money rule; "prior investments of the partners" is the
   partner-carried rule. Read the page source: this site's HTML comments named the two groups.
5. **§6, entry dates for rows staged by a first-party label that publishes no year** (R1).
6. **§6, stage by sequence.** A round before a named Series A is a seed; a single round before a
   named Series B is the Series A. Not from size, only from the sequence the record gives.
7. **§8, `rekey_overlays` should copy a verdict onto a rename target, not move it,** when the
   departed slug went to `excluded.json`. Third run to hit it (BCV, Insight, Index). Until then:
   after every rebuild, give both name variants of an excluded row their own verdict.
8. **§8, an identity merge whose canonical row is excluded should exclude the duplicate too.**
   Today the group is skipped and the duplicate returns as a member (Oxyplus, Opentest).
9. **§11, Form ADV 7.B parsing.** The PDF repeats each fund's page cumulatively; join the last
   page of each run into linear text, or four funds read the same value.
10. **§11, a mask icon is black by convention.** Take the colour from the tag's own `color`
    attribute.
11. **§6, a press release's body wins over its URL slug.** Spot.IM's slug names Index; the body
    names other leads.
12. **§6, the company's own site as status evidence.** A domain that now serves an unrelated blog
    (Little Borrowed Dress) or a one-line stub (Covariant) is a dated observation worth citing;
    a fetch that returns nothing (Catch) is not.
13. **§8, gzip raw captures as they are written.** The disk filled on 2026-10-01.
14. **§12, a subagent's brief must say which contact address to use for sec.gov,** or forbid the
    request. The blind judge used the user's personal address in three requests (section 13).

## 13. Usage line

**Kickoff, 2026-10-01 14:32 UTC (Fable 5.1):** five-hour window 3%, weekly 73%, Fable 8%. The session stopped that
evening and resumed on 2026-10-06 on Opus 5.5 after the weekly reset. **First reading after the resume (19:25 UTC):**
five-hour window 8%, weekly 8%, Fable 4%. **At close (about 20:00 UTC):** five-hour window 20%, weekly 11%, Fable 4%.
560 published rows, 655 judged. One subagent (the blind judge, 351K tokens).

**One incident to report.** The blind-check subagent sent three requests to sec.gov with the
User-Agent "Erik List list.erik.2005@gmail.com", the personal address, to read three Form D index
pages (CIKs 1607035, 1997387, 2021402). It reported this itself. The project's own scripts use
erik@meritcapit.al for the SEC. Nothing else carried an address. It cannot be undone.

WebSearch: about 96 of the session's 200 calls, 30 of them by the blind judge.

## 14. Prompt count

**4.** The kickoff ("please collect Index Ventures"), "continue" after the interruption of
2026-10-01, one message after the close with two instructions (London as headquarters; sweep
the European registers if it improves accuracy), and a second "continue", read as the go-ahead
for the same status check on the rows outside Europe (section 17). The target is one.

## 15. Ingest

**Index Ventures is live.** The gate, in the order COLLECTION.md §9 gives:

1. Plain `verify` clean at 560 rows; 708 rows shared with other books, all agree, none parked as accepted.
2. `run.py close`, then the closing commit `633f0015`.
3. Icon uploaded (`investors/index-ventures-fe52f4fc5f.png`), then `ingest-investor.ts`: one row upserted.
4. `ingest-companies.ts --dry-run`: "560 row(s) upserted (560 new), 0 removed, from 0 live". Nothing to
   check on the removal list.
5. The write, then the readback: "csv 560, live 560, missing 0, extra 0, differing cells 0". The investor row
   carries the icon, the profile and the derived S2A of 100 of 142 (70.4%).
6. Post-ingest commit `5cfc1fd6` (the bucket URL in `investor.json`).

**Stale sibling rows: 36 rows in 20 books aligned and re-ingested**, one book at a time, each through the
same gate (its own verify clean, readback exact before, dry run with 0 removals, write, readback exact after,
a commit of that book's three company files). Kits and logs are in `scratch/align/`.

| Book | Rows | What changed | Commit |
|---|---|---|---|
| a16z | 1 | Temporal $12.55B | 9cf9af4d |
| Accel | 3 | HouseTrip acquired; OpenX private; Bird acquired | 74861cea |
| Balderton | 1 | Dream Games $5.0B | e1ee0587 |
| Battery | 1 | Expel $1.0B | 438ca896 |
| Benchmark | 1 | Respond.com acquired | 8f9d9fa2 |
| Coatue | 1 | Covariant unknown | 4f6d1e50 |
| Felicis | 1 | Revel $1.0B | 791668d8 |
| First Round | 3 | Persona $2.0B; Rec Room defunct; UberMedia acquired | d5c9e1df |
| GV | 1 | Flapping Airplanes $1.50B | 52b00d50 |
| Khosla | 1 | Parallel Web Systems $2.0B | ac397477 |
| Lightspeed | 2 | Temporal $12.55B; Avarra graduated (repair) | 3f2a24f9 |
| Lux | 1 | Covariant unknown | b0742c4b |
| NEA | 1 | Expel $1.0B | 6ee893a9 |
| Point Nine | 1 | Typeform private | bb33a254 |
| Redpoint | 3 | Glow $1.20B; Revel $1.0B; Sonos $2.15B | 0b09e563 |
| Seedcamp | 2 | Loctax acquired; Property Partner acquired | 495e01ff |
| Sequoia | 6 | Apex acquired; Bird acquired; Flapping Airplanes $1.50B; Parallel Web Systems $2.0B; Rec Room defunct; Temporal $12.55B | 29485385 |
| Thrive | 2 | Revel $1.0B; Stytch acquired | fe973d54 |
| Tiger Global | 1 | Cohere $20.0B | 72215968 |
| Y Combinator | 3 | Humanloop defunct; Nourish $1.75B; Vouch private | d219eab0 |

Each line carries one sentence naming the event and its source, never Index's own site.

Three things the alignment needed beyond the rows:

- **One repair in a sibling's own book.** Lightspeed's verify was failing on its own: the censoring window of
  its seed row Avarra ended on 2026-10-03. A fresh search of the surfaces found a $17M Series A announced on
  2026-10-06 with Lightspeed in it, so the row reads graduated. A recorded no stays a target on every run; so
  does a censored row whose clock has run out.
- **Namesake pairs the alignment surfaced**, ruled distinct in the books' own files: Redpoint's Glow against
  a16z's and USV's; YC's Vouch against First Round's (YC's row had carried the other company's defunct status).
- **A false alarm in the readback.** YC's CSV carries the name " Metadata" with a leading space; the ingest trims
  it, the readback did not, so it reported one missing and one extra row. The alignment script compares after
  trimming. The readback tool itself is unchanged (it is another run's file).

Decisions inside the alignment that Erik may want to see: Bird reads acquired in the Accel and Sequoia books
(it read defunct there since 2026-09-03, before the insolvency rule was written); Covariant reads unknown in
Coatue and Lux (an acqui-hire, and the company's site is a stub); Typeform reads private in Point Nine (the
Bending Spoons bid of October 2025 never closed); Dream Games reads private at $5B in Balderton (CVC took a
minority); Respond.com reads acquired in Benchmark.

**After the alignment every book that is not in flight verifies clean.** Two pairs between other books were
failing before this run and were ruled on their own notes (Insight's LeoLabs against Kleiner Perkins' Leo;
Project A's Q against Kleiner Perkins' q.ai).

**Not aligned: the six books in flight** (Atomico, Bain Capital Ventures, Bessemer, Founders Fund, General
Catalyst, Speedinvest). Five namesake pairs against them are ruled ahead of time (Atomico's Bird, General
Catalyst's Abacus Labs, Double Labs and Thread, Speedinvest's Solvo.ai). No real disagreement with them is
known; Bessemer and Founders Fund are not classified yet, and their own gate will compare against this book.

**Linear:** PRO-82 set to Done with a closing comment.

## 16. After the close: London, and the register sweep (2026-10-06)

Erik's message after the closing report carried two instructions. Both are done and live.

**Headquarters: London.** `profile.hq_override` in `config.json`; `firm-offices.py` and `verify`
accept it; commit `8f6735f0`; the `hq_location` column was written alone and read back.

**The register sweep. It improved accuracy: 22 of the 128 European rows that read private or
unknown changed status (17%).**

| Change | Rows | Companies |
|---|---|---|
| unknown to defunct | 9 | Cord, GroupSpaces, Loveshark, Mindshapes, RjDj, Solvo, The Garden, Sproutl, smarterwork.com |
| unknown to acquired | 4 | Osper, Pulsic, Groupalia, StylistPick |
| unknown to private | 2 | TheFamily, be2 |
| private to acquired | 5 | Workbounce, PeoplePerHour, Teemo, Kayrros, Cowboy |
| private to defunct | 2 | Kano, Second Home |

European rows before and after: private 108 to 103, acquired 80 to 89, defunct 9 to 20, unknown
20 to 5, public 9. The S2A rate did not move (every corrected seed row already read not
graduated), but seven of its nos now rest on a cited end instead of a dated search.

How it was done:

- **UK, Companies House (67 rows).** The public register site, through the helper earlier runs
  built (`scratch/companies_house.py`). 58 rows matched to a legal entity by name, by a legal name
  the judge supplied (Cord is Radical HQ Limited, RjDj is Reality Jockey Limited, Sproutl is The
  Sprout Group Limited, incident.io is Pineapple Technology Ltd), or through the officer register
  (the founders of The Garden and Sproutl). Each entity's status, filing history and controlling
  owners were read. Sixteen corrections came from here.
- **The register of controlling owners is the register's trace of a sale.** Workbounce (ZoomInfo
  UK Ltd from 2024-11-07), Osper (Crunch Payments Limited from 2025-09-12), PeoplePerHour (a
  company controlled by Taso Du Val from 2025-11-12) and Pulsic (Cadence, also in the press) read
  private or unknown with no press headline this run had found.
- **France, Sirene (18 rows).** The state's open company search. It confirmed the operating rows
  and showed Teemo's legal unit under the name Azira, the successor of the Near that bought it
  in 2020.
- **Switzerland, Czechia, Estonia, Finland, Denmark.** Open registers queried by name; all seven
  rows found are active.
- **A dated news check for sales and insolvencies** on all 128 rows, for the countries with no
  open register and as a second look at the rest. It found Kayrros (bought by Energy Aspects,
  completed 2026-05-21) and Cowboy (taken over by ReBirth, December 2025), and re-raised Dream
  Games, which was re-read and stands: CVC is the sole outside shareholder and the five founders
  keep the majority, so the company was not acquired.
- **44 rows confirmed active** now carry their register page as the status citation.

Readings worth knowing:

- **A dormant shell reads defunct.** Smarterwork.com Limited is still on the register 27 years on,
  filing as a dormant company. The business ended; the row says so at medium confidence.
- **An administration with no sale reads defunct** (the standing rule): Second Home, in
  administration since January 2025, and Kano, dissolved on 2026-10-03.
- **Tactic stays unknown.** Its UK company was struck off in February 2026 after buying back
  shares, and its site is still up.
- **Not reached:** Geckoboard, GetHarley, EDITED (no UK entity under the brand name; all three
  read private on other evidence), and the recent seeds whose entity is weeks old.

Files: `sources/registers/companies-house/` (the search results, the matched entities with
their controlling owners, the decisive filing histories), `sources/registers/sirene/`,
`sources/registers/other/`, `scratch/status-news-eu.json`, and the judgments in
`scratch/judgments-registers.py`.

**Sibling alignment.** One pair: Insight's Groupalia read unknown and now reads acquired, through
the same kit and gate. None of the other 21 corrected companies sits in another book.

**Ingest.** Readback before the write showed 22 differing cells, exactly the 22 statuses. Dry run
with 0 removals, write, readback exact. Insight re-ingested the same way.

**The same check on the rows outside Europe followed on 2026-10-07 (section 17).** Delaware
publishes no open status register, so it ran on the buyers' SEC filings, the dated news check
and the companies' own domains.

Two write-backs to add to section 12: a register pass with the controlling-owner read as a
standing duty for UK rows before the close (it costs minutes and moved 16 rows here); and the
sale-and-insolvency news check for every private row, since the momentum slice looks only at
valuations.

## 17. The status check outside Europe (2026-10-06 and 2026-10-07)

Erik's "continue" after section 16. **14 more statuses changed; unknown falls from 18 to 8.**
Live since 2026-10-07, readback exact.

| Change | Rows | Companies |
|---|---|---|
| private to acquired | 4 | Cocoon, Common Room, Monograph, Science Exchange |
| unknown to acquired | 1 | Interana |
| unknown to private | 4 | Vetted, doubleTwist, Storybird, Cue |
| unknown to defunct | 5 | Mobissimo, DJZ, Catch, Rad, OpenBuildings |

Status now: private 275, acquired 210, defunct 41, public 26, unknown 8. The S2A rate did not
move (100 of 142, 70.4%).

What was checked: the 185 rows outside Europe that read private (172) or unknown (13), and
again the five European rows the register sweep had left unknown.

- **The buyers' own SEC filings.** EDGAR full-text search for "acquisition of", "acquired" and
  "acquire" with each company's name. It found Common Room ("On July 17, 2026, we acquired 100%
  of the issued and outstanding share capital of Common Room, Inc." for $266.8 million, Zoom's
  Form 10-Q) and confirmed Cocoon (TriNet).
- **The dated news check for sales and insolvencies** on all 185 rows. 58 rows returned a
  headline in which a company of that name is sold or closed; each was read against the row.
  Four were a completed sale of the Index company (Cocoon, Common Room, Monograph, Science
  Exchange). The rest were namesakes (Beam Benefits, Thatch the travel guide, Pomelo the
  remittance company, Augment CXM, Transcend Packaging) or events that are not a sale of the
  company (Nauto's unclosed merger, store closures at Glossier, Xapo's custody unit).
- **TechCrunch's own search** on the same rows. Nothing the other two had not found.
- **The companies' own domains**, for the rows with no report either way. A live product is an
  observation (Vetted, doubleTwist, Storybird, Cue). A domain that no longer resolves or serves
  only a parking page is one too (Mobissimo, DJZ, Catch, Rad, OpenBuildings). A page that could
  not be read counts as neither.

Readings worth knowing:

- **A signed merger is not a status.** Nexar and Nauto announced a stock merger on 2026-07-01
  and no source reports the close. Nauto stays private, with the lead in its note.
- **The five defunct rows rest on a vanished or parked domain** and nothing on record since, at
  medium confidence. None has a closure report.
- **Interana** became Scuba Analytics, and Scuba is "now part of Behavure AI" by Behavure's own
  site. The business continues under another company: acquired, medium, as Battery's row reads.
- **Cue** reads private at low confidence: the site is up and nothing more is on record.
- **Still unknown (8):** Covariant (its founders and a licence went to Amazon in 2024 and the
  company's own state is not on record; Coatue and Lux read the same), Tactic, Futurelytics,
  Webfair, Grupo Xango, Happylatte, LaserComm and Pulsent.

**Sibling alignment: 12 rows in 9 books, all re-ingested, every readback exact.**

| Company | Now reads | Books aligned |
|---|---|---|
| Cocoon | acquired | First Round, Y Combinator |
| Common Room | acquired | Greylock |
| Science Exchange | acquired | a16z, Union Square Ventures, Y Combinator |
| Interana | acquired | a16z, Y Combinator (listed as Scuba) |
| DJZ | defunct | GV, Kleiner Perkins |
| Vetted | private | Insight Partners |
| doubleTwist | private | Northzone |

Rulings added to `companies/cross-rulings.json`: Index's Catch (pay-by-bank checkout) is not the
Catch of Sequoia and Y Combinator (benefits for independent workers); Interana is the same
company as the Scuba rows of Battery, Y Combinator and General Catalyst. General Catalyst is in
flight and its Scuba row reads unknown; rule 10 will show the pair when that run closes.

**Three gate repairs in books the Founders Fund run (PRO-81) had left red**, done because they
blocked this alignment:

- a16z's Royal read defunct on an uncited "wound down". royal.io is live and lists two products
  the company runs today. The row now reads private, as Founders Fund's does. Re-ingested.
- `cite_pending` was missing on a16z's Lighter and Battery's Porch Group after that run brought
  their $1B+ values in. Raised on both; no database cell changed.
- Y Combinator's Cargo (sales automation, Summer 2023) and Founders Fund's Cargo (in-car
  commerce, 2018) are two companies. Ruled distinct in the YC book's file.

**Left open, not this run's pairs:** The Boring Company reads $9.6B in 8VC and Sequoia and $23B
in Founders Fund, and Coatue's Enter has a country with no citation. Both came from the
Founders Fund run and keep 8VC, Sequoia and Coatue red at `verify`.

**Ingest.** Readback before the write showed 15 differing cells: the 14 statuses and
doubleTwist's city (Austin, from its own site). Dry run with 0 removals, write, readback exact.
Commit `738756ab`; the nine sibling commits are listed in `scratch/align3/results.txt`.

Files: `scratch/status-news-row.json`, `scratch/status-edgar-fts.json`, `scratch/status-tc.json`,
`scratch/judgments-status-row.py`, `scratch/judgments-status-row-2.py`, and the pages read in
`scratch/web-finds.json`.
