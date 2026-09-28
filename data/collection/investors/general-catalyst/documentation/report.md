# General Catalyst: Build & Reconciliation Report (PRO-166)

**Linear issue** PRO-166 · **slug** `general-catalyst` · one run under the merged shape of
`data/collection/COLLECTION.md`, in two sessions (a context restart mid-grind) · report written
2026-09-27; rulings applied and ingested 2026-09-28 on Erik's approval (section 16).

---

## 1. The answer PRO-166 asked for

**The base is 1,933 companies and plain `verify` is clean.** All are members: Erik ruled
the 3 `uncertain` rows out and folded two same-company pairs (E1, E2, section 9). Every control transaction is out (21 excluded rows, about 19 companies), and so are
the Customer Value Fund's revenue-share-only companies, the SPACs and La Famiglia's deals from
before the combination. The page's track record covers the firm's venture investments; the profile's history says so. Ingested 2026-09-28 on Erik's approval (section 16).

| Done-when item | State |
|---|---|
| Plain `verify` green with only flagged debt | Clean on 1,933 rows, cross-investor 0 disagree (section 6 lists the flags) |
| Boundary rows counted | 21 control-position rows, 120 not_member rows in `excluded.json` (section 3) |
| Profile fields populated or null, sourced | `investor/investor.json` and `investor/sources.json`, built by `build-firm-profile.py` |
| `review.html` rendered | Served on the review surface and checked: rows flat, 1,933 shown, profile panel expands (re-checked after the rulings) |
| `report.md` with delta outcomes, open rulings, prompt count | This file |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 1,933 | |
| Unknown | 876 | 45% |
| Private | 733 | 38% |
| Acquired | 242 | 12% |
| Defunct | 53 | 3% |
| Public | 29 | 1% |
| $1B and above | 143 | 7.4% |
| of which $10B and above | 34 | Anthropic, Databricks, Stripe, Snowflake, Airbnb, DoorDash, Anduril, Coinbase, Twilio, Canva, Ramp, Telegram, Reddit, Samsara, Kalshi, Helsing, Deel, Circle, Devoted, Applied Intuition, Discord, Polymarket, ClickHouse, Mistral AI, Skild AI, Superhuman, Iceye, Figma, Bilt Rewards, HubSpot, Cognition, Whoop, Instacart, Mercor |
| of which $100B and above | 4 | Anthropic $965B, Databricks $190B, Stripe $159B, Snowflake $118B |

**Why 45% unknown.** The firm's /list page gives 1,896 legal names; 1,321 rows rest on that list
alone, with nothing else to identify the company behind a legal name, and 846 of them carry
`status: unknown` and `city_unknown` rather than a guess. The rows the firm shows on its grid (578) are identified and classified in full. There is no ceiling on the $1B+ share (Erik,
2026-09-26); 7.4% of a base this long-tailed reads as expected for a multi-stage firm.

Entry stage: Seed 184, Growth 129, Series A 82, Pre-Seed 4, round not on record 1,534.
Headquarters: US 1,661, UK 65, India 56, Germany 36, France 13, Netherlands 10, Israel 9, Mexico
8, Sweden 7, Canada 6, Singapore 6 (686 of the US rows are `country_prior`: the firm's pattern,
not an address). Evidence tiers: A 765, B 1,162, C 6. Membership rests on the firm's own listing
for 1,927 rows (grid 578, list 1,319, archived pages 30), on press for 4 recall additions and on a
Form D ruled by the judge for 2 (Healing Humanity Productions, nToggle).

### S2A block

Of 184 seed entries, 62 were too recent to count. Of the 122 that remain, **67.2%** raised a later
round (82). Of the 40 that did not, 4 rest on a cited end (a sale or a closure) and 36 on the
dated absence test over the named surfaces; none on the Form D filings alone.

| Seed entries | Censored | Cohort | Graduated | Rate |
|---|---|---|---|---|
| 184 | 62 | 122 | 82 | 67.2% |

The rate rose from 61.5% at the in-flight pass: the delta decided 20 more Seed rows (18
graduated, 1 no, 1 censored; Locu restaged to Series A), and two absence-test nos turned out to
have missed later rounds (section 11, item 1).

## 3. The boundary: control positions, Creation, the Customer Value Fund

The firm runs venture and growth funds, a Creation strategy (hatches and AI-enabled roll-ups),
the Customer Value Fund (revenue-sharing growth financing), GC Wealth and a SPAC. The page's
track record covers the venture investments only (decisions.md D3 to D8, R1 to R4):

- **Control positions out** (D4, R4): Athletes First (the MASTRY and GC majority purchase, 2023),
  the roll-ups Beacon, Dwelly, Long Lake and Zero RFI, Aura and Intersections (the consortium
  take-private of 2018/19 is the entry), BBN (the 2004 purchase from Verizon), and eleven list
  entries named as buyout or holding vehicles (Ulysses Buyer, Fino Topco, Raven TopCo, Dynamo
  Topco, Logicbroker TopCo, RW-2023 HoldCo, Build Holdco I, ReInvent Commerce Holdings, XFIT
  Holdings, Ponto Meridian Rollup, Beacon Acquisition). HATCo's Summa Health purchase is not a
  row. **Count: 21 excluded rows, about 19 companies** (BBN appears twice, as BBN and BBN
Technologies; Point Wild is Aura's split-off).
- **Creation hatches in** (D3.1): Commure, Hippocratic AI, Homeward, HealthEx, Maribel, Kayak,
  Demandware, Datalogix, Datto, Livongo, Transcarent, Tendo, Paradigm, Pacific Fusion and others,
  each entered on its founding capital. **X1, the Creation companies that build and buy**, were
  ruled on the entry: Accrual, Crescendo, Eudia and Titan are IN (a product company when the firm
  came in, acquisitions after); Zero RFI is OUT (it launched on its seed with three acquisitions).
  These five are the ones to move if the line should sit elsewhere.
- **Customer Value Fund** (D6, R3): ten companies whose only tie is CVF money are out
  (Beautiful.ai, Chainguard, CookUnity, Function Health, IM8, Ladder, Mirage, Quo, Relay, Rylo).
  Where a venture fund also bought equity the company stays, entered on the first equity round
  (Factorial's 2026 Series D; Iru's 2024 round). Dandy is `uncertain`.
- **La Famiglia and Venture Highway** (D8): 41 La Famiglia companies backed before the October
  2023 combination are out as the earlier firm's deals (Personio, Forto, SoSafe, Y42, Vay, Stoke
  and others); Mistral AI stays, entered on the firm's own December 2023 Series A.
- **Sale consideration** (R1): Teladoc (Livongo), Millennial Media (Jumptap), Xero (Melio),
  WW International (Weilos) and Starco Brands are out.
- **The SPACs** (D7) and the firm's own fund-shaped list entries are out.

## 4. Coverage per evidence regime

| Surface | What it gave |
|---|---|
| The firm's live site (grid of 607 cards, company pages, flags, partners) | 579 members with first-investment year, partners, Seed/Creation/CVF/IPO/acquired flags |
| The firm's /list (1,896 legal names, "as of June 30th, 2026") | 1,321 further members, most otherwise unidentified; the join to the grid (486 pairs incl. 12 judged) |
| The firm's posts (360) | Entry-round citations, Creation hatches, S2A graduations |
| Internet Archive | /portfolio and /companies eras 2007 to 2026 (912 slugs); 32 archive-only members, 31 folds onto existing rows; the partner roster (29 departed investors with windows). A new machine-wide block began mid-run (about 470 minutes) |
| EDGAR (Form D, full text, 13D/G) | 177 rows with Form D links; entry rounds and the S2A Form D sequence; Intersections' 13D (a control position) |
| Form ADV (CRD 162548) | AUM $45.50B to $45.59B, 48 private funds, HQ |
| Wikipedia insource sweep | 7 recall additions (Cadre, Flok, GroupMe, Summon, PatientBank, Article One Partners, Quill) |
| Google News and web search | S2A surfaces, momentum checks, valuation pins; 90 of 200 web searches used |

## 5. Method deltas

- **The firm's /list page is the recall layer.** 1,896 legal names "as of June 30th, 2026", joined
  to the 607-company grid by name, reverse prefix and 12 judged pairs (Maplebear to Instacart,
  Exafunction to Windsurf, Blockratize to Polymarket and others). About 1,300 list rows name
  companies no other source identifies; they carry `status: unknown` and `city_unknown` rather
  than a guess.
- **Form D rows are adjudicated by who sat, not by the name.** 21 Form D registrants are the list's
  companies under a legal or former name and were folded in (JAND is Warby Parker, Mulberry Health
  is Oscar, Coopkanics is Wildcard, Unlimited Labs is B12, Emerging Travel is Ostrovok, DC Devices
  is Corvia, ParElastic is Tesora); the rest were namesakes or pre-GC seats (R2).
- **The research that did not fit the grind ran as three agents**: the CVF equity check, the
  Creation hatch-or-buy check and the valuation pins, each writing one findings file under
  `scratch/research/` that the judge applied row by row.
- **S2A from a converter**: `scratch/judge/s2a.py` turns one line per row into the record and
  builds the absence test from `scratch/graduation-surfaces.json`, the firm's own posts and the
  Form D sequence, so every no names its surfaces.

## 6. Flags and debt behind `verify`

On the 1,933 published rows: `city_unknown` 977, `country_prior` 686 (both the /list
rows), `model_disputes_source` 89, `stage_uncited` 79 (a model stage under $1B; allowed),
`unicorn_name_match` 57, `cik_weak` 31, `stale` 24, `stage_disputes_band` 22, `cite_pending` 12
($1B+ rows whose entry round no source names: Cognition, Color, Devoted, Figma, GitLab, NotCo,
Oscar, Physical Intelligence, Spinny, Sword, Vercel, Telegram), `boundary` 6, `needs_web_value` 4
(ArriVent, Eikon, Maze, Parabilis Medicines: believed $1B+ with no citable figure, so they sit
below $1B), `entry_anchor_weak` 2.
33 of the 143 $1B+ rows carry the unicorn list's figure rather than a cited one. Cross-investor:
1,054 rows shared, 1,014 agree, 40 accepted, 0 disagree; 124 namesake pairs ruled distinct in
`companies/cross-rulings.json`.

## 7. Standing duties and the A/B pass

- **Duty 1** ($1B+ claims): all 143 $1B+ rows checked for identity and status; 110 carry a cited figure and 33 the
unicorn list's; Anthropic, Commure and Webflow were re-cited, and Stripe's status, which the
Wikidata layer read as acquired after the last prepare, was put back to private (a name
collision).
- **Duty 2**: every `not_graduated` is below $1B and private or dead; every `censored` entry is
  inside 24 months at the check.
- **Duties 3 and 4** (weak CIK joins, stale floats): the float layer's "acquired" on four rows
  whose registrant is another company is disputed (Cicero Technologies, Faro Health, Sprint Labs,
  Shyft; R5). The other stale-float rows are genuinely acquired.
- **Duty 5**: OvaScience's float belongs to its successor (merged into Millendo, 2018): acquired.
- **Duty 6**: a loose re-intersection of the unicorn list finds only name collisions, and Thatch,
  which the Wikipedia list showed at $1B with no citable round at the time; the momentum slice then
  found the citable round (PR Newswire, 15 September 2026), so Thatch is now $1B+.
- **Duty 7**: a blind 5% re-classification (88 rows, seed 20260927) disagreed on 12; three were
  errors and are fixed (autone Series A, Mainspring Growth, Landbase private).
- **Duty 9**: the India-team region pattern was swept as a class and holds.
- **Momentum slice**: 93 private hot-sector rows first seen from 2021 got one web check each. Found: three new
unicorns (Serval $1B, Reuters, December 2025; Rox $1.2B, TechCrunch, March 2026; Thatch $1B, PR
Newswire, 15 September 2026, which moves Thatch above $1B and supersedes duty 6's reading), three
exits (Stilla to Meta, Rossum to Coupa, Loci to Epic) and one graduation the S2A absence test
missed (Greenboard). 27 generic names matched other companies and carry a note only.

## 8. Firm profile

- **Thesis**: the site's own line, quoted: "General Catalyst is a global investment and
  transformation company that partners with the world's most ambitious entrepreneurs to drive
  resilience and applied AI."
- **History** (64 words): founded in Cambridge MA in 2000 by Joel Cutler and David Fialkow; Kayak
  and HubSpot, then Airbnb, Stripe, Snap and Anduril; $8B for Fund XII in 2024; the page covers
  the venture investments, with buyouts and revenue-sharing financing left out.
- **HQ** Cambridge, MA (Form ADV principal office). **Founded** 2000. **Stages** Seed, Series A,
  Growth. **Geography** US core; Europe and India.
- **AUM** $45.50B to $45.59B (ADV RAUM plus La Famiglia's). **Funds** XII $8.0B (2024), XI $4.6B
  (2022), X $2.3B (2020), IX $1.375B (2018).
- **Investment range** $5M / $22M median / $900M (entry rounds of 121 members).
- **Notables** Airbnb, Snap, Stripe, Anthropic, Discord. **Individuals** 65 (5 departed).
- **Icon**: the site's GC.svg vector; dry-run render clean at `sources/site/icon-256.png`.

## 9. Open rulings for Erik

**Erik's answers (2026-09-28), applied before the ingest** (decisions.md E1 to E4): items 1 and
2 as asked (the three uncertain rows out; Ponto and Trellis one company each), item 3 approved,
item 4 both kept. Items 5 to 8 stand as reported.

1. **Three `uncertain` rows.** Dandy (CVF money and a vendor-reported equity round; no
   citable equity round found). Domestic Bank and Federal One: 2010 archived company pages that
   could not be read (Internet Archive block) and names on no other surface. Keep, or rule out?
2. **Ponto / Ponto Software and Trellis / Trellis Technologies**: each pair shares an SEC
   registrant and both rows are flagged `duplicate`. Ponto Software, Inc. is probably the grid's
   Ponto (the list carries no other legal name for it); Trellis is unsettled. Same companies?
3. **X1, the Creation companies that build and buy**: Accrual, Crescendo, Eudia and Titan IN,
   Zero RFI OUT (section 3). Is that the line?
4. **nToggle** is in on two of the firm's partners of the time (George Bell, John Simon) sitting
   together on its 2015 Form D, with no press naming the firm. **Healing Humanity Productions** is
   in on Hemant Taneja and Alexa Liautaud as directors on a $15M 2023 Form D; the company is not
   identified.
5. **Eleven archive-only rows are unidentified** (GIRC, MedCatalyst, Arc Energy, Push Computing,
   Axium, Workflow, Hyper, Kiwi, Merlin, Curbflow's details, and the two above). They are members
   by the listing rule with `status: unknown`; re-read the captures when the block lifts.
6. **VisaNow**: my first ruling put it out as a bare Form D name-match; the firm's own 2014
   company page (archived) puts it in, and it is in. Flagged here because it reversed.
7. **Beacon's evidence link**: the row is Beacon Biosignals (a member, classified correctly) but
   its site link points at Beacon Software's card (section 11, item 4). Harmless to the numbers;
   wrong on the review surface.
8. Standing: R5's four disputed "acquired" floats (Cicero, Faro, Sprint Labs, Shyft) read
   unknown or private; Medely is a rule-bound no (vendor totals only); New Travelco is folded into
   Trover on the directors' overlap.

## 10. Rebuilds and deltas

- **Rebuild 1** (after the recall probe and the archive layer): 2,012 rows; 112 excluded; the
  ex-partner rule removed 29 rows and 8 personal board seats. Its rekey renamed Form D slugs and
  disarmed 11 identity merges (the merge file was updated) and fused the two Beacons.
- **Delta 1**: 129 rows. 45 renamed or earlier-name rows folded (Anaconda, Codeium, Kandji,
  Snapchat, DECA and Kin Community, ScanScout, Sand 9, OGSystems and others), BBN Technologies a
  control position, 3 non-company paths and 22 departed-partner or namesake Form D rows out, 2
  unidentifiable paths `uncertain`, nToggle and 4 Wikipedia additions in, 20 Seed rows decided
  for S2A (Locu restaged to Series A on TechCrunch's "Series A").
- **Rebuild 2** (needed because the delta ruled membership): 1,940 rows. Tagomi came back under a
  second legal name, and VisaNow flipped slug, so it escaped exclusion.
- **Rebuilds 3 and 4**: Tagomi out; VisaNow found to be two rows (the Form D issuer and an archived
  2014 company page); the listing makes it a member and the two folded.
- **Rebuild 5**: Ethos AI restored (the build had fused the grid's two "Ethos" cards), Health
  Insight folded into Humedica and GoodsCloud into NewStore (each the same SEC registrant under an
  earlier name). 1,938 rows, no renames. Four rebuilds past the schedule; each was needed for a
  membership change, and none moved a judged answer.
- **At close**: the two Almanac rows were found to carry each other's answers (Almanac Health is a
  Pre-Seed entry of 2025 or earlier, almanac.io a 2019 row) and were corrected; Stripe's status was
  put back to private; the three stale classification keys (castle-global, fragment-technologies,
  point-wild-holdings) and two merged ones were removed (kept in `scratch/stale-classification-keys.json`).
- **Rebuild 6** (Erik's rulings, 2026-09-28): Dandy, Domestic Bank and Federal One out; Ponto
  Software folded into Ponto and Trellis Technologies into Trellis. 1,933 rows, no renames.

## 11. Playbook write-backs proposed (not applied mid-wave)

1. **S2A card truncation.** `s2a-cards.py` showed two items per surface; two absence-test nos
   (Greenboard, Chamber Cardio) had later rounds further down. The absence test must read every
   item, not a sample.
2. **Momentum slice pays**: three unicorns, three exits and one missed graduation on 93 rows.
3. **Partner-roster overwrite.** A second chained run wrote over the 413-person sweep when a new
   IA block began; write the roster to a new file per run and never over a larger one.
4. **Same-name grid cards fuse in the build** (Beacon, Ethos): the site layer keys cards by name.
   Key them by the card slug; the Ethos fusion dropped a member silently.
5. **The rebuild rekey flip-flops** a not_member slug between two renderings (VisaNow), so the row
   escapes exclusion on alternate rebuilds, and it disarms identity merges keyed on the old slug.
6. **`record` appends notes with " | "**: re-recorded rows carried repeated segments (281 cleaned
   at close by dropping any segment that a later one extends). Replace a note that extends the old
   one instead of appending it.
7. **A re-run `prepare` can change pre-filled statuses** (Stripe read acquired from Wikidata after
   the last prepare): verify should compare a row's deterministic status across prepares.
8. **The list-to-grid join can cross two same-stem rows** (the two Almanacs swapped answers).
9. **Agent prompts must forbid personal identifiers in request headers** (section 15).

## 12. Usage line

Kickoff (2026-09-27 19:10 UTC): not read. Close (2026-09-27 23:05 UTC, on Opus 5.5): weekly all
models 94%, Fable 85%, 5-hour 60%, extra usage EUR 12.14 of 50 (disabled). Other sessions ran in
the same window (BCV, the pipeline session), so the week's movement is not this run's alone. Web
searches: 90 of 200 (judge 24, research agents 66). Base rows: 1,933.

## 13. Prompt count

**3, final**: the kickoff ("please collect general catalyst"), "continue" after a restart, and
the review answer that carried four rulings and the ingest approval ("keep 1. considerations
out, mark as same companies on 2., approve on 3., keep both 4., ingest afterwards"). Corrections
from Erik: none to judged rows; four rulings on the open questions.

## 14. Ingest request (not run)

First-time investor, so in this order, each only on Erik's approval:

1. `npx tsx scripts/fetch-investor-icon.ts general-catalyst https://cdn.prod.website-files.com/69df4e62ff62d7b5568fc58b/6a16ee532ff7f5b53d83064a_GC.svg`
2. `npx tsx scripts/ingest-investor.ts general-catalyst`
3. `npx tsx scripts/ingest-companies.ts general-catalyst --dry-run`, read the list (a first
   ingest removes nothing), then the same without `--dry-run`: 1,933 companies.

## 15. Incident: a personal address in a request header

One research subagent (the Creation check) sent one EDGAR full-text-search request with Erik's
personal Gmail address in its User-Agent header, contrary to the rule that the address is used
only to identify him. The repo's own scripts send the Merit Capital research address
(`scripts/edgar_common.py`); every later agent prompt in this run forbade personal identifiers
in requests, and no other request carried it.
