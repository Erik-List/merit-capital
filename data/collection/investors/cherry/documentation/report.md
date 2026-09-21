# Cherry Ventures — Build & Reconciliation Report (PRO-73)

Run date 2026-09-04, one session, one merged run (derivation protocol,
`decisions.md` D1–D12 with 0 deltas, run-time rulings 13–18). Prompt count 1
(kickoff). Ingest not run — gated on Erik's approval. Nothing committed to git.

## 1. The question PRO-73 asked

**Does the Creandum EU method transfer to a smaller, younger German seed firm,
and what does the bare-word name cost?** It transfers, with two additions and
one non-event.

- **Transfers unchanged:** site listing as the membership anchor, the Wayback
  ladder for the archived book, the SEC layers for the US-side vehicles, the
  Wikipedia insource sweep, the ECB-rate FX rule, the momentum-slice web check,
  the cross-investor gate. Cherry raises US money through Delaware feeders, so
  the AIFM files Form ADV (CRD 301494, Section 7.B gross asset values) and the
  feeders file Form D — the SEC layers were not empty, just lagging (the 2024
  ADV carries Funds III and IV, not the 2025 Fund V).
- **Addition 1 — the German register.** North Data's free entity pages gave the
  whole vehicle tree (44 entities: five flagship KGs, GP GmbHs, Entrepreneurs /
  Employee / Carry vehicles, numbered Opportunities co-investment KGs, a Growth
  fund, a Select sleeve, UK and Swedish branches, and the 2007 London namesake)
  with incorporation dates, general partners and named limited partners.
  Filing-grade for the boundary and the fund ladder; zero portfolio, because
  the KGs' participations sit behind the aggregator's paywall. BaFin's database
  is empty for a registered (sub-threshold) manager; the ADV records the BaFin
  registration instead.
- **Addition 2 — four list surfaces for one small firm.** The live Webflow site
  (94 pages, 90 listed, an "(EXIT)" tag, no dates or stages); the Sanity CMS
  behind the replaced 2024–2025 site, still publicly queryable (86 companies
  with a date field and sector tags, 108 dated articles with body text); the
  archived WordPress listings 2016–2023 (107 companies with the firm's own
  investment dates for 2016–2019 and a Seed / Series A label); and the Getro
  job board (98 companies, 38 on no other surface). Union 183 candidates, 148
  members after identity work and the membership grind.
- **The non-event — the common-word name.** Entity-qualified phrases ("Cherry
  Ventures", "Cherry Decentral") returned five EDGAR full-text hits (all the
  firm's own Form Ds) and five Wikipedia articles (four already in the base).
  The namesakes (Cherry Tree Ventures, Cherry Ventures Ltd London 2007, Cherry
  AB) were caught by the entity registry's address check, never by the phrase
  layers. Cost: two model priors flagged, no false members.

## 2. Results

| Surface | Count |
|---|---|
| Base rows | 148 (tier A 138, tier B 10) |
| Excluded | 5 (Cazoo, Xometry as site-listed acquirers under D8; Intenseye as an ex-Principal's Point Nine seat; two "Stealth" placeholders) |
| Identity merges | 33 merged, 2 rejected (Flixbus→Flix, FreightHub→Forto, COSI→Numa, DashDash→Rows, SMACC→Hypatos, QOA→Planet A Foods, ELISE→Synera, cioplenu→Operations1, Cauldron→Those Beyond, …) |
| Membership ledger | 151 verdicts, 0 uncertain |
| Classification | 148/148 |
| Status | private 106, acquired 24, defunct 10, unknown 7, public 1 (AUTO1) |
| Valuation range | below_1b 140, 1b_plus 8, 10b_plus 0 |
| Entry stage | Seed 113, Pre-Seed 22, Series A 11, Growth 2 (66 cited, 82 model) |
| Seed→A cohort | 113 Seed rows, 79 determined, 54 graduated = 68.4 % (24 rows verified on both legs) |
| Momentum slice | 47 rows web-checked, each with a citation on the row |
| Cross-investor | 17 shared rows, 17 agree after 3 alignments and 4 distinct rulings |
| Web budget | about 170 of 200 |

**$1B+ rows (8):** Legora $5.55B (Series D, Mar 2026; Cherry's entry is a late
Growth position, round unnamed — `cite_pending`), AUTO1 Group $5.61B (public
float), Black Forest Labs $3.25B (Series B, Dec 2025), Flix $3.24B (EQT/Kühne,
Jul 2024 — `stale`), Proxima Fusion $2.74B (Series B, Jul 2026), Forto $2.1B
(Series D, 2022 — `stale`), Moss $1.16B (Series C, 2022 → 2026 re-mark), Dash0
$1.0B (Series B, Mar 2026). SellerX and Flink stay below_1b on collapse
evidence (BlackRock auction / 2023 down-round) despite unicorn-list marks.

**Distributions.** Focus: Consumer & Marketplaces 32, SaaS 27, AI & Applied AI
19, Fintech & Payments 18, Healthcare & Bio 10, Media/Gaming 8, Climate &
Energy 7, Industrial & Robotics 7, DevTools & APIs 6, Crypto & Web3 5, Data
Infrastructure 3, Security 2, outside taxonomy 4. Geography: DE 84, GB 19, US
12, SE 8, DK 6, FR 3, then FI/NL/AE/CH 2 each; cities Berlin 56, London 18,
Munich 14, Stockholm 7, Copenhagen 6, New York 6 (143/148 filled). Entry
years: 2012–2019 62 rows, 2020–2026 76 rows (31 in 2026, the Fund V book),
10 undated (job-board-only positions).

## 3. Calibration gate

Both sets were pre-registered before the build (`golden.json`).

- **Membership:** 34 traps (namesakes, portfolio-of-portfolio, founder-angel
  seats, acquirers, placeholders, look-alikes). 0 false members after the grind.
- **Stage:** 46 keyed rows. Blind pass 44/46 after two key corrections (Zaro and
  Forgent: the evidence pack's sentence splitter cut "$5.1M pre-seed" at the
  decimal, so the key and the blind read were wrong the same way — splitter
  fixed, keys corrected, logged in `_corrections`). Entry-year agreement 45/46.
- **Self-consistency:** 40/40 on an eight-row re-judge (`scratch/selfcheck-blind.json`).

## 4. Standing duties and the A/B pass

- Weak-CIK audit: 33 EDGAR name hits, 31 weak; two public floats quarantined
  (Forgent Networks is not Forgent; Xometry is excluded).
- Unicorn-list re-intersection: Forto took the fresher press mark; Shift's
  unicorn entry is Shift Technologies (homonym) and was rejected.
- City/country coherence: 33 distinct cities; the five unresolved rows carry
  `city_unknown`; twelve Wikidata homonym countries disputed and overridden
  from the firm's own pages.
- Momentum slice: 47 rows, each web-checked and cited on the row
  (`valuation_range_source: web_verified`), one unicorn miss avoided (none
  found above the list; Olix-type corrections did not recur).
- A/B pass: the archived listing's Seed / Series A label (2016–2019) agrees
  with the judged stage on 41 of 44 overlapping rows; the three disagreements
  are noted on the rows (`model_disputes_source`).
- Recall probe: Helsing, sennder, Kertos rejected (no Cherry participation in
  any named round); Turian is Uify (identity merge); zero additions.

## 5. Firm profile

HQ Berlin, Germany (3/3 own filings; the builder now strips the "- Mitte"
district from the Form D city). AUM $905.7M (ADV Section 7.B, 2024: Fund III
$534.2M, Fund IV $342.6M, Decentral I $28.9M) to $1.0B (press, after Cherry V
$500M in 2025 — the sworn figure is a floor two vintages old). Five flagship
funds from the register and the filings; feeders (Fund III/IV (US) L.P.) and
sleeves are described in the basis, not listed. 23 individuals (10 investing,
7 operations, 6 strategic; 5 departed partners kept with end dates from the
Wayback roster 2012–2026). Focus: eight labels from the firm's own tags
(crosswalk in `config.json`); the grind ranks AI & Applied AI third while the
site's tags do not surface it — flagged in the sidecar, not overwritten. Check
size: verified median $5.0M at Seed. Icon dry run passed (source web clip,
opaque plate, contrast 3.6:1); upload pending approval.

## 6. Flagged debt

| Flag | Rows | Meaning |
|---|---|---|
| stage_uncited | 82 | stage from model knowledge (mostly the 2012–2019 book, whose rounds pre-date the press archive) |
| cohort_unverified | 78 | Seed rows where one leg of the graduation test is a prior |
| model_disputes_source | 13 | the judge overrode a surface (Wikidata homonyms, listing labels) |
| censored | 12 | 2025–2026 entries too young for the graduation test |
| identity_uncertain | 9 | job-board-only or renamed positions |
| city_unknown / country_prior | 5 / 5 | no firm page names the seat |
| stale | 2 | Flix (26 months), Forto (2022) |
| cite_pending | 1 | Legora's late-entry round |

## 7. Open rulings for Erik

1. **D8 — site-listed acquirers are consideration, not members** (Cazoo took
   Drover, Xometry took Shift): applied on the Creandum precedent, agent-flagged.
2. **Ruling 15 — job-board-only positions** (10 tier-B rows) kept as members at
   low confidence because the board is the firm's own surface.
3. **Ruling 16 — late entries:** Legora (Growth, round unnamed), Black Forest
   Labs (Growth), Proxima Fusion (Series A) enter the book above Seed.
4. **Ruling 17 — collapse evidence over list marks:** SellerX and Flink below_1b.
5. **Ruling 18 — insolvency followed by an asset sale is `acquired`** with a
   successor note (Homelike→Spacest, Julienne Bruno, Joblift→Adzuna, Infarm);
   `defunct` only where the business ended (Watchmaster, Weengs, Lesara, Move24).
6. **AMBOSS** stays below_1b without a figure despite the €240M 2025 round (no
   published post-money).
7. **AUM top** from a single press figure; the sworn 7.B number is the floor.
8. Seven `unknown` status rows and four outside-taxonomy focus rows are listed
   in `review.html`.

## 8. Pipeline contributions

- `scripts/build-firm-profile.py`: German Form D cities carry the district;
  stripped to the municipality.
- `data/collection/COLLECTION.md`: three write-backs (German register recipe
  and the four-surface small-firm pattern in §5; the insolvency/asset-sale
  convention in §6; ERA-lag AUM, district cities and comma-joined tags in §11).
- Scratch recipes reusable for the next EU run: Webflow sitemap + page ladder,
  Sanity dataset query behind a replaced site, WordPress `wp-sitemap` listing
  captures with `data-invested` epochs, Getro board via `__NEXT_DATA__`,
  North Data entity pages, decimal-aware evidence-pack splitter, roster
  curation from the Wayback team pages.
- `data/collection/shared/cross-align/2026-09-04-cherry.py`: aligned Accel
  (legora $5.55B, dash0 $1.0B) and Lightspeed (proxima-fusion $2.74B); their
  `base.csv` files are re-exported and need re-ingest.

## 9. Ingest request (not run)

1. `npx tsx scripts/fetch-investor-icon.ts cherry` (upload the web clip).
2. `npx tsx scripts/ingest-investor.ts cherry`.
3. `npx tsx scripts/ingest-companies.ts cherry`.
4. Re-ingest Accel and Lightspeed for the three aligned rows.
5. Set PRO-73 to Done.

## Addendum 2026-09-17 — S2A re-judged under the status contract

`seed_to_a_graduation` became a judged status (`graduated | not_graduated |
censored | undetermined`, COLLECTION.md §6), superseding the C2A figures
above. `migrate-graduation` dropped 113 legacy values with their 78
`cohort_unverified` flags; all 113 Seed rows were judged in three batches
with both legs cited in the same pass (27 rows gained a stage citation).

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|---|
| 112 | 10 | 50 | 52 | 48 | 4 | 92.3% | 51% |

Of 112 seed entries, 10 were too recent to count; of the 102 whose record
could be sought, 52 were established (51% coverage) and 92.3% of those
graduated — the establishable set skews toward visible successes, and on
this book that bias is the strongest yet measured: Cherry files no Form Ds,
so a row is decidable only if a publisher or the firm itself wrote about the
later round. The four "no"s are all cited acquisitions (Kitchen Stories,
Qura, Shift, Speechly). Of the 50 undetermined, 27 are live companies whose
seed is cited but whose later record is silent, 19 are rows no page ties
Cherry to a seed at all, three are unresolved identities and one is an
ownership change rather than a round. `verify.shape.c2a_rate_max` is
restated from 0.80 to 0.95 (D-S2A), and `spryker` left the cohort on a
first-party listing that contradicts itself — both are written up there.

Coverage of 51% sits just above the leaderboard's ranking floor of 50%, so
this investor's rate is the one most sensitive to a handful of further
citations.

`verify` is clean.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Nine flagged rows, and the firm's own records split them cleanly six-three.

**Six rows are named companies and lose the flag.** `anboto-labs`
(anboto.xyz), `lucent-data` (lucentdata.io), `profitmind` (Netail, Inc. at
netail.ai) and `venmark` (venmark.co.uk) each carry a job-board card with a
url and a product description — that IS the company being named, and under
the 2026-09-18 rule a named and described company carries no identity flag.
`teatox` (the Berlin detox-tea brand, 2013-09 entry) and `vicomi` (Tel Aviv
audience-emotion analytics, 2014-10) are named on the firm's own 2016 listing
and carried to 2019. What those rows are missing is a round, a status or a
graduation, and each of those already has its own flag.

**Three rows are one-word labels on the 2016-2019 portfolio grid** with an
invest year and nothing else: `aloha` (2013), `enfold` (2014), `save` (2015).
No url, no description, no filing, no later trace; `aloha`'s Wikidata
Philippines match was already disputed as a homonym. The firm's own grid
labelled each entry Seed, but the label was applied to a company nobody could
name, so `entry_stage`, `valuation_range` and `seed_to_a_graduation` all read
`undetermined` and the rows leave every metric.

`hq_country` on those three stays the Berlin desk inference with
`country_prior` still on it. An inferred STAGE cannot survive on a row whose
stage reads `undetermined` — the flag would contradict the value — but an
inferred country can: it is all such a row has, the flag is what marks it
inferred, and invariant 1 still wants the cell filled.

`verify` clean. The S2A block moves from 112 to 109 seed entries as the three
leave the cohort; the rate is unchanged at 92.3%, because all three were
`undetermined` there already.

## Addendum 2026-09-20: S2A with every Seed row decided (PRO-132)

PRO-132 made the absence of a later round a finding. A Seed row past the
24-month clock with no evidence of a later round did not graduate, and every
no records the dated search that found nothing: the firm's archive and at
least two publisher surfaces (COLLECTION.md §6). Cherry files no Form Ds, so
every decision rests on a citation or on that search.

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 93 | 10 | 83 | 52 | 31 | 62.7% | 100% |

Of 93 seed entries, 10 were too recent to count (Flinn.ai, Bardo, Trace.Space,
Cortea, Alice.Tech, BEO, Kiku, Sphinx, Alta Ares, INXM); of the 83 that
remain, 62.7% raised a later round. Of the 31 that did not, 7 rest on a cited
end and 24 on a dated search of the named surfaces. 20 decided rows rest on an
uncited seed and carry `stage_uncited`.

Was (D-S2A, 2026-09-17): 112 seed entries, 10 censored, 50 undetermined,
cohort 52 at 92.3% with 51% coverage.

**A German-language re-check backs the nos.** `graduation-surfaces.py` now
adds the company's own Google News edition and language (`googlenews_local`,
de-DE for a German company). Run over every Cherry no on 2026-09-20, it found
no later round; the hits were namesakes (Eastnine the Baltic landlord, Klar
the Mexican neobank, Hadrian the US defence manufacturer) or non-rounds
(Amorelie's 2014 ProSieben media-for-equity stake before its sale).

What moved:

- 19 rows left the Seed cohort. Two were re-staged because the only citable
  Cherry money is a later round (Formel Skin at the Series A, Numa at Growth);
  sixteen now read `undetermined` in the stage because nothing on record dates
  Cherry's entry (among them AdvaSolutions, Anboto Labs, ProfitMind, Uify,
  Buycycle, Ninetailed, Orkestro and Together); Radicle is token-funded
  (Radworks financed through token rounds, no priced ladder), `undetermined`
  in stage and graduation with `token_funded`.
- The four nos from the 2026-09-17 pass (Kitchen Stories, Qura, Shift,
  Speechly) now carry their absence records; Julienne Bruno's pre-pack
  administration into Compleat Food Group (The Grocer, November 2025) is its
  cited end.
- Pemo stays a no: its only later round, $7M in November 2024, is styled
  "pre-Series A" by every outlet, and a round named below a Series A does not
  graduate the row.

`verify.shape.c2a_rate_max` returns from 0.95 to the 0.80 default. `verify` is
clean.

For Erik: **Fizz** and **Mine** are very likely one company (Fizz rebranded as
Mine / MoneyGPT, per Pulse 2.0); an identity question for the merge file, left
as two rows here.
