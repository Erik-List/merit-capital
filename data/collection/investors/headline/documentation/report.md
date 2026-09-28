# Headline: Build & Reconciliation Report (PRO-164)

Headline (e.ventures 2012 to 2021, BV Capital 2000 to 2012, Bertelsmann
Ventures from 1997), collected 2026-09-27 under `data/collection/COLLECTION.md`
and closed that night at 268 companies. On 2026-09-28 Erik ruled the Asia and
Brazil desks in (E1) and Accel's Sorare row aligned (E2), and approved the
ingest to follow. This report is the state after that delta: 395 companies.

## 1. The answer PRO-164 asked for

**395 companies, plain `verify` clean, profile rebuilt, review surface checked.
Ingest approved by Erik on 2026-09-28 and run after this report (section 14).**

| Done-when item | State |
|---|---|
| Plain `verify` green | `verify: clean` (flagged debt only, section 6) |
| Entity set in `decisions.md` | D1: six exempt reporting advisers (CRDs 304362, 309084, 319198, 323219, 323221, 344374) plus BV Capital Management (160568, last filed 2017); since E1 also the Asia desk (Infinity Ventures, Headline Asia; Infinity Ventures Crypto, CRD 321781) and the Brazil desk (Redpoint eventures, Headline Brazil) |
| Every row judged, classified, cited | 436 verdicts (402 member, 34 not_member) over 395 published + 34 excluded rows; 395/395 classified |
| Coverage per evidence model (D11) | Section 4, never blended |
| Firm profile | `investor/investor.json` + `sources.json`, rebuilt by `build-firm-profile.py`, `profile_copy.py` ok |
| `review.html` rendered | Served on the review surface (port 8931) and checked: 395/395 rows flat, profile panel carries the desks' funds, AUM and geography |
| Cross-investor (rule 10) | 133 shared rows: 125 agree, 8 accepted (sibling side stale, aligned at the wave pass), 0 disagree; 26 namesake pairs ruled distinct, all in Headline's own `companies/cross-rulings.json` |

## 2. Results

| | Count | Share of 386 nameable |
|---|---|---|
| Companies | 395 (9 unnameable, excluded from every metric) | |
| Private | 233 | 60% |
| Acquired | 97 | 25% |
| Unknown | 25 | 6% |
| Defunct | 20 | 5% |
| Public | 11 | 3% |
| $1B and above | 25 | 6.5% |
| of which $10B and above | 1 | Mistral $24.4B (EUR 21B, September 2026) |

The 25: Mistral $24.4B, Gopuff $8.5B, AppFolio $7.2B (public), Rappi $5.25B
(2021, stale), Recursive $4.7B, AMI Labs $4.5B, Sorare $4.3B (2021, stale),
Creditas $3.3B, Black Forest Labs $3.25B, Flutterwave $3.2B, Icertis $2.8B
(2021, stale), Fetch $2.5B (2022, stale), Wellhub $2.4B (2023, stale), Owner
$2.3B, Sonos $2.15B (public), Acorns $1.9B (2022, stale), Lightricks $1.8B
(2021, stale), Exein $1.7B, Olist $1.5B (2021, stale), freee $1.37B (public,
Tokyo), Fundamental $1.2B, Staffbase $1.1B (2022, stale), The RealReal $1.07B
(public), Swile $1.0B (2021, stale, floor), Genki Robotics $1.0B (April 2026).
Every mark is web-verified with a citation; public rows carry the market cap
of 2026-09-25 (2026-09-28 for the desks' listed companies).

Entry stage over the 256 rows whose round is on record: Series A 107, Seed 87,
Growth 59, Pre-Seed 3; 130 nameable rows (34%) stay `undetermined`.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 87 | 16 | 71 | 48 | 23 | **67.6%** |

Coverage 100%. The 23 nos rest on Form D absence (2), a cited end (6: an
acquisition before any Series A) and the absence test (15). By desk: the home
book 76.0% on 50, the Asia desk 5 of 7, the Brazil desk 5 of 14 (seed
extensions and small follow-ons, not Series As). Eleven decided rows rest on
an uncited (model) entry stage and carry `stage_uncited`, confidence low.

## 3. The boundary

- **D1 one firm across three renames**: every Bertelsmann Ventures, BV
  Capital, e.ventures and Headline vehicle.
- **E1 (Erik, 2026-09-28): the Asia and Brazil desks are in**, reversing the
  derived D2/D3. Both operate under the Headline name and claim the firm:
  Infinity Ventures became Headline Asia in May 2021 by Headline's own release,
  and Headline Brazil III was announced as one of Headline's own funds. Applied
  with the D1 lineage test inside each desk, so Infinity Venture Partners' and
  Redpoint eventures' earlier deals come in too (the narrower reading is open,
  section 9). 127 rows returned: 63 Asia, 64 Brazil.
- **D4 partner-carried deals out** (no desk row qualified: Viajanet predates
  Romero Rodrigues; Rappi and ABC da Construcao are desk-fund deals), **D5
  Porsche Ventures II out**, **D6/D7** instruments and sale consideration.
- Run-time rulings, flagged for review: **R1** eVenture Capital Partners was
  the firm's European branch before 2012; **R2** Raisin is sale consideration,
  Deposit Solutions the member; **R3** hidden CMS docs judged on
  corroboration (every hidden desk doc was corroborated by the Brazil desk's
  own portfolio page, rpev.com.br, or press); **R4** the CMS "Growth" label
  sets a stage; **R5** the Moscow and Kiev deals came from the European fund;
  **R6** the e.ventures logo wall is the firm's own listing.

## 4. Coverage per evidence regime (D11)

A row is `sec_visible` when the base carries a Form D or EDGAR issuer record
for it, `non_sec` otherwise.

| | sec_visible | non_sec |
|---|---|---|
| Rows (nameable) | 31 (31) | 364 (355) |
| Membership evidence | site 21, web 8, formd_adjudicated 2 | site 311, web 53 |
| Status | private 16, acquired 7, unknown 4, public 3, defunct 1 | private 217, acquired 90, unknown 21, defunct 19, public 8 |
| Stage decided / undetermined | 27 / 4 (13%) | 229 / 126 (35%) |
| Stage source (decided) | formd_band 12, web_verified 12, model 2, first_party 1 | web_verified 178, model 31, first_party 20 |
| S2A cohort / rate | 8 / 75.0% | 63 / 66.7% (16 censored) |
| $1B+ | 4 (12.9%) | 21 (5.9%) |

The book is 92% `non_sec`. The desk rows are the weakest regime: the round the
desk entered in is undetermined for 55% of Asia rows and 47% of Brazil rows,
because Japanese, Taiwanese, Chinese and Brazilian coverage names amounts and
dates far more often than round letters.

## 5. Method deltas

- **Logo-wall layer (R6)**: one CDX enumeration of eventures.vc before the
  Internet Archive firewalled the machine; the upload filenames list the
  portfolio logos (166 non-people logos, 89 recall additions).
- **E1 desk delta**: config partition emptied, one rebuild with two identity
  merges (Jihua.fm into Classbox, Resultados Digitais into RD Station), four
  research agents (two Asia, two Brazil). Two first-party sources carried the
  desks: the Brazil desk's own portfolio page, rpev.com.br/portfolio (49
  companies with fund number and HQ), and Headline Asia's PR TIMES feed
  (company_id 84461), which gave first-party round names for most Japanese
  rows where Google News returned nothing.
- **Recall press sweep**, **Common Crawl** for bvcapital.com 2008 to 2010,
  **stage pass** by five agents, **two rebuilds** on day one (Verse vs Verse
  Medical fixed with `never_merge`).

## 6. Flags and debt behind `verify`

| Flag | Rows | Meaning |
|---|---|---|
| model_disputes_source | 23 | a pre-fill overruled by the row's evidence, noted |
| stale | 15 | $1B+ mark older than 24 months (section 2) |
| stage_uncited | 11 | decided S2A rows on a model stage, confidence low |
| cik_weak | 10 | float-sweep registrant joins: six right company; Pronto, Flux, Pulse and the desk's Arena quarantined |
| identity_unresolved / country_prior | 9 / 9 | title-only CMS docs (Indigo, Journey, Keeper, Nouri, Root, Tandem) and three Asia-desk rows (Cardmon, Undone, Openhome) |
| unstable | 8 | blind 5% disagreements, adjudicated (section 7) |
| city_unknown | 7 | looked, not placed (ClarityCare and six desk rows) |
| cite_pending | 5 | model stages still owed a citation (Fetch, Sonos, AMI Labs, Sorare, Staffbase) |
| stage_disputes_band | 4 | cited round disagrees with the Form D band |
| valuation_floor | 3 | mark is a floor figure |
| boundary | 2 | AppFolio and Sonos, a fact flag from the deterministic layer |
| formd_adjudicated / unannounced_deal | 2 / 2 | ViaVia and Daily Secret (director of record, medium) |

**Archive debt** (the IA block held both days): headline.com and headline.vc
eras, bvcapital.com 2000 to 2007, per-year snapshot parses of eventures.vc, and
18 logo filenames not identified.

## 7. Standing duties and the A/B pass

- **A/B pass**, home book (23 visible rows): no band moved (Icertis sale talks,
  Bumble exploring a sale, Sorare's unpriced 2026 round). Desk rows (Rappi,
  Wellhub, Olist, Genki Robotics, freee): no band moved; Amazon's 2025 money in
  Rappi was a $25M convertible note with no valuation; Genki's $1B is reported
  by Axios and Crunchbase News.
- **Momentum slice**: 25 recent rows, no new $1B+ mark.
- **Duty 1**: every $1B+ mark web-verified; unicorn-list pre-fill flags cleared.
- **Duties 3 and 8**: ten registrant joins audited; four were other companies
  and carried a listing flag (Pronto, Flux, Pulse; the desk's Arena read as
  Arena Group Holdings): quarantined and the listing cleared.
- **Duty 6**: unicorn list re-matched loosely on both passes: no miss.
- **Duty 7, blind 5%**: home book 14 rows, 7 disagreed; three corrections
  (Flowhub, TVSmiles, All Def Digital), three stand with the blind reading
  noted, one was the blind judge's error. Desk rows 7 rows, 2 corrections
  (Olist's entry is its 2016 Series A, named by Baguete; Smartbreak's head
  office is Osasco). All eight carry `unstable`. **Duty 9 sweep**: the
  Flowhub class ("Growth by sequence" on recall rows) found The Young Turks;
  the Olist class (a named round the research missed) is the desks' 50%
  undetermined share, not swept row by row: reported as debt.

## 8. Firm profile

HQ San Francisco, CA (ADV principal office; the site lists it with Berlin,
Paris, London, Hamburg and Sao Paulo). Founded 1997. Thesis, the title-tag
tagline: “Global venture capital helping founders win, bigger.” History 3
sentences, 76 words, now naming the four regions. Stage Seed, Series A, Growth.
Geo core US and Europe, other Latin America and Asia (US 152, Europe 111, Latin
America 61, Asia 53 of 386). Focus from the site's tags: SaaS, Consumer &
Marketplaces, Fintech & Payments, Data Infrastructure. Range $1.5M / $8M median
(248 entry rounds, press-based) / $110M. AUM $4.04B to $4.57B: the bottom is the
sworn Section 7.B composite of seven exempt reporting advisers (Infinity
Ventures Crypto added); the top adds Porsche Ventures II and the desk funds no
SEC adviser reports (Headline Asia V $145M, Headline Brazil III $169.4M,
Headline Asia IV $100M). 13 funds, Headline Asia V (2025) to eVentures Growth
(2014). Notables: Sonos, Bumble, Mistral, Farfetch, Goop. 83 people. Icon: the
site's vector favicon, dry run clean.

## 9. Open rulings for Erik

1. **E1's reach**: applied with the lineage test, so the desks' pre-rename
   deals are in (Infinity Venture Partners 2010s, Redpoint eventures from
   2012). The narrower reading, only deals made under the Headline name (May
   2021 on), would drop most of the 127 desk rows again.
2. **Desk judgment calls**: Memed reads acquired (DNA Capital's 2021 control
   buyout bought out the desk; the company still operates), the BCV
   BetterCloud precedent; Jmty graduated on its 2020 IPO (no named Series A);
   Delfos graduated on a 2026 "Series A extension" that EU-Startups still calls
   pre-A; "Pre-Series A" read as undetermined (Nudge, Letara) per the
   Balderton ruling; Genki Robotics is a member on two Headline Asia partners'
   team pages with no press naming the firm.
3. **R1, R2, R5, R6** (above), each flagged for review.
4. **Sibling alignment at the wave pass** (ruled `accepted` in Headline's
   `cross-rulings.json`, sibling side stale): Accel BetterCloud, Sequoia Bird,
   a16z All Def Digital, General Catalyst Coya, Battery Fundamental, Khosla K2
   Network, 8VC Plated, Redpoint Sonos, a16z Genki Robotics (below_1b vs the
   $1B Series A). Same band, citation fixes: Redpoint Owner, Y Combinator
   Flutterwave, Spark Clyde, Redpoint Fanhattan. Accel's own verify also
   carries two older disagreements from yesterday's sibling runs (KupiVIP vs
   Balderton, SingleStore vs Insight).

## 10. Rebuilds and deltas

Day one: two rebuilds (recall additions; the Verse fix). Day two (E1): one
rebuild after the research landed, with two identity merges; no existing row
renamed or moved (checked slug by slug); the 127-row delta judged in full.

## 11. Playbook write-backs proposed (not applied mid-wave)

1. **§1, E1 as a standing test**: a desk that carries the firm's brand and
   claims the firm is in, whatever its adviser registrations; the old T1 test
   (own adviser plus own fund family is out) stays for desks that dropped the
   brand (HongShan, Peak XV).
2. **§5, the upload-filename layer** when the archive blocks (R6).
3. **§5, first-party desk sources**: a desk's legacy portfolio site
   (rpev.com.br) and a firm's PR TIMES feed are first-party layers; Google
   News is nearly blind to Japanese and Chinese rounds.
4. **§8 duty 8**: a wrong registrant join sets `is_public` too; clear it, or
   the row counts as an IPO. The duty-3 list must read the exported view.
5. **`stage_words.py`**: add "pre-series a" and "pre-series b" as anchors
   (straddling two stages, per Balderton), so the word is recognised.
6. **`run.py record` note merge**: a new note inside the stored one replaces
   it; keep the old note instead.
7. **`edgar-entities.py`** drops entities whose seed query returns a single
   EDGAR company page.
8. **ADV 7.B parse**: a value on the next page takes the next fund's value.
9. **`build-company-base.py` name-variant merge** joined Verse and Verse Medical.
10. **`profile_copy.notable_problems`** matches the base name, not
    `names.published` ("Mistral AI" vs "Mistral").
11. **`focus_crosswalk` is case-sensitive** and fell back silently.
12. **Uncommitted shared-script hunk for the tooling session**:
    `scripts/graduation-surfaces.py` FIRM_TERMS gained Headline's three names.
13. **Rule-10 rulings belong in the investor's own `cross-rulings.json`**; this
    run first wrote into the shared file and moved them before close.

## 12. Usage line

Day one: weekly all models 80% at kickoff, 96% at close; weekly Fable 82% to
85%. Day two (after the weekly reset): see the closing message. 395 published
rows (429 judged including exclusions). Research agents: five (stage), four
(logo wall), four (desks), two blind re-judges.

## 13. Prompt count

4: the kickoff, two "continue" prompts after context compactions, and Erik's
rulings with the ingest approval.

## 14. Ingest (approved 2026-09-28)

Order for a first-time investor: icon upload, `ingest-investor.ts headline`,
then `ingest-companies.ts headline` (395 companies); then Accel re-ingested for
E2 (one row changed, Sorare). Readback results are in the closing message and
the Linear comment.
