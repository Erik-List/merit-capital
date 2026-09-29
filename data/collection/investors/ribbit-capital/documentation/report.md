# Ribbit Capital: Build & Reconciliation Report (PRO-161)

**Linear issue** PRO-161 · **slug** `ribbit-capital` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session, with Common Crawl carrying the archive while the Internet
Archive blocked this machine · report written 2026-09-28. **Not ingested: the ingest waits on Erik's
approval (section 14).**

---

## 1. The answer PRO-161 asked for

**The base is 181 companies, plain `verify` (links checked) is clean, and the firm profile is built.**
One adviser runs every Ribbit vehicle (Ribbit Management Company, LLC, CRD 165308), so there is no desk
partition. Out: Bitcoin and Ethereum (no issuer), the 2020 SPAC Ribbit LEAP, five listed companies the
firm bought after they were public (Mercado Libre, Sea, Futu, Tinkoff, Bank Jago), and 30 Form D rows
that matched a Ribbit person's name: namesakes, roles outside the person's Ribbit tenure, or a board seat
with no Ribbit fund named.

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean, links sampled; no flagged debt blocks it |
| Every row judged, classified, cited | 222 verdicts: 181 published members, 37 excluded (not_member); 181/181 classified |
| Firm profile | `investor/investor.json` + `sources.json`, built by `build-firm-profile.py`; `profile_copy.py` ok |
| `review.html` rendered | Served on the review surface and checked: 181/181 rows, profile section present |
| Cross-investor (rule 10) | 193 shared rows: 174 agree, 19 accepted, 0 disagree; 22 namesake pairs ruled distinct |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 181 | |
| Private | 137 | 76% |
| Acquired | 23 | 13% |
| Public | 11 | 6% |
| Defunct | 6 | 3% |
| Unknown | 4 | 2% |
| $1B and above | 68 | 37.6% |
| of which $10B and above | 17 | Stripe $159B, Revolut $115B, Robinhood $104.7B, Solana $69.9B (token cap, section 9), Nubank $59.1B, Coinbase $50.6B, Cognition $48B, Crusoe $30.9B, Affirm $22.7B, Etched $21B, Deel $17.3B, Base Power $13B, Groww $12.2B, Checkout.com $12B, GoodLeap $12B, PhonePe $12B, DCG $10B |

Entry stage: Growth 71, Series A 45, Seed 25, Pre-Seed 1, round not on record 39 (mostly companies where
Ribbit is first named as an existing investor, so its own entry round is earlier and unnamed).
Headquarters: US 108, Brazil 14, UK 13, India 11, then France, China, Israel, Mexico and Germany 3 each, and
18 more countries with one or two (Gibraltar since the country fix, section 9). Focus: Fintech & Payments 103, Crypto & Web3 38, AI & Applied AI 10.
Membership rests on the firm's own listing for 179 rows and on the company's own release for 2 (Delphia,
ForUsAll).

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 25 | 3 | 22 | 15 | 7 | **68.2%** |

Coverage 100%. The 7 nos rest on a cited end for 3 (Atlantic Money, bought by Deel; Meso, by MoonPay;
Sealance, by Forte) and the dated absence test over the named surfaces for 4 (Alpen Labs, Alude, Ballet,
Redefine). Censored: CoPlane, Enigma, Tako.

## 3. The boundary

- **One adviser, no partition (D1).** Every Ribbit vehicle is advised by Ribbit Management Company, LLC
  (CRD 165308, Palo Alto; no relying advisers). All 67 private funds on its Form ADV are in: the flagship
  funds, the Bullfrog growth funds, the founder side funds and about 40 single-deal vehicles.
- **Tokens (D2).** Bitcoin and Ethereum, which the Rebels list carries, are out (no issuing organisation;
  Erik's a16z ruling 7). Protocol rows are members under their issuing organisation (Solana Labs, Offchain
  Labs, Uniswap Labs, Morpho Labs, the M0 Foundation, Merkle Manufactory, Ethena Labs, Elliot Technologies
  for Lighter, Tempo). Diem is in under the a16z, USV and Thrive precedents.
- **Ribbit LEAP (D3).** The firm's 2020 SPAC never merged and was wound up: out under T5, and no row arises.
- **Public-market positions (D4, R3).** Mercado Libre, Sea, Futu, Tinkoff and Bank Jago are listed by the
  firm but traded before its first money: out under T3. DH-S (Ribbit Cayman IN Opportunity VI, 2021) decodes
  to Dhani Services, a listed Indian company the firm never listed: no row.
- **Form D seats (R4 and the delta).** 30 Form D rows that matched a Ribbit person's name are out: Craize Snacks, Harbor National, OSIX and Valon Technologies (a board seat with no Ribbit fund named;
  Erik's ruling of 2026-09-28), Lemon, Inc. (Malka's own company, D5), and 25 namesakes or roles outside
  the person's Ribbit tenure (a Buffalo-area Brian McGrath on four companies, Carlotta Siniscalco's later
  board seats at Federato, Forward Lending and Whistic, and others).
- **Control (D8).** None found: Ribbit makes minority venture investments.

## 4. Coverage per evidence regime

- **Live site**: the Rebels list (155 rows, parsed from the Next.js page chunk by `scratch/pull-site.py`)
  and the team page (33 people). The site's disclaimer says the list shows companies in active strategies
  only and omits some for confidentiality or size, so absence from it is not evidence.
- **Archive**: the Internet Archive gave the 2012-2015 Bets pages (27 captures) before it blocked this
  machine; Common Crawl carried the rest (Our Bets 2015-2018 and 2021-2025, the Rebels page chunks 2025-12
  to 2026-09, the team pages 2015-2026). **Debt: 2019-2020 is unread.** Common Crawl holds no ribbitcap.com
  capture between January 2018 and January 2021, and the four IA requests that would cover it were
  withheld (section 5). A company listed only in 2019-2020 and gone by 2021 may be missing; the one known
  candidate, ForUsAll (its logo sat on the firm's server), was decided on the company's own release.
- **Form D**: the roster sweep over 67 names of 56 people with tenure windows; the related persons' filed
  addresses decided the common-name seats. The firm's own vehicles: 78 filings on 64 vehicles.
- **Single-deal vehicles**: 52 codes read off the ADV and Form D, decoded in
  `sources/registers/spv-decode.json` (resolved, probable, unresolved). 14 codes stay unresolved and none
  decodes to a company absent from the base. RNBW-1 is OnePay (RNBW Ventures Inc., Green Dot's 10-Q).
- **Exit side**: EDGAR full text on ten fund phrases (138 registrants, 61 third-party ones triaged), the
  adviser's 13F lines (CIKs 1571355 and 1836733), Wikipedia insource (38 articles, 12 company candidates).
- **Press**: the Google News sweep per row and a press recall sweep (222 items, `scratch/recall/press-sweep.txt`).
- **Recall probe**: one addition (Delphia: its own Series A release names Ribbit), twelve rejections with
  reasons in `scratch/recall/rejections.json`.

## 5. Method deltas

- **Common Crawl as the archive during an IA block.** The run's first fetch burst earned a 60-minute
  machine-wide IA block (19:36Z), and the first requests after it doubled the cooldown to 120 minutes (to
  22:37Z). Common Crawl, read through the static cluster index (`scratch/cc-cluster.py`, `cc-fetch.py`),
  carried Our Bets, the team pages and the Rebels page chunks. **The 2019-2020 IA fetch was stopped before
  it fired**: BCV's run found that the first request after a cooldown ends is refused and doubles the
  machine-wide block, and the Sutter Hill and 20VC runs were active. `scratch/ia-gap-fetch.py` (four replay
  requests, no CDX) is ready for a quiet window.
- **The Rebels page is a compiled array, archived as a JS chunk.** The live list and its archived versions
  come from the Next.js page chunk, read with a small JS-string decoder; the 2015-2025 Our Bets pages carry
  logos and company links only, so a link-host identity map (`sources/wayback/identity-map.json`) names
  each logo.
- **The single-deal vehicle decode** (`sources/registers/spv-decode.json`): a code is fund-filing evidence
  that a Ribbit vehicle was in that round, never the entry (D6). It dated Clip, Kavak, Root and DCG, and it
  showed OnePay behind RNBW-1.
- **Titles from the record for a site that publishes none** (`sources/web/team-titles.json`, merged by the
  existing file_list machinery): Form ADV Schedule A and releases that quote the person with a title.
- **`scratch/readnews.py`**: decodes a Google News headline to its publisher and reads the page with a
  browser user agent, for publishers that refuse WebFetch (CNBC, LatamList, Bloomberg Línea, Nearshore
  Americas, KrASIA, VCCircle, CoinDesk, Sifted, BetaKit).
- **`scratch/set-notes.py`**: a rewrite pass replaces a row's note instead of appending to it (record
  appends with " | ", which is right for a delta and wrong for a correction).
- **Parallel judges** on batches 1-4 from `scratch/JUDGE-BRIEF.md`, per-judge news caches (`NQ_TAG`),
  recording under the per-investor lock; a blind second judge for duty 7.

## 6. Flags and debt behind `verify`

On the 181 published rows: `model_disputes_source` 41 (mostly wrong Wikidata or SEC joins on common
words, each disputed with evidence), `stale` 26, `unicorn_name_match` 17, `city_unknown` 13, `cik_weak` 8,
`stage_disputes_band` 5, `token_funded` 2, `unstable` 2 (duty 7), `country_conflict` 1 (Morse Money:
London company, US parent). Archive debt: 2019-2020. Three
stale classification keys (aside, capital-float, sling-money) duplicate their canonical rows (Daffy, Axio,
Morse Money) exactly and are harmless.

## 7. Standing duties and the A/B pass

- **Public caps** read 2026-09-28 (StockAnalysis; INR and GBP at the ECB rate): Robinhood $104.71B,
  Nubank $59.06B, Coinbase $50.57B, Affirm $22.68B, Groww $12.19B, Figure $6.58B, Policybazaar $5.55B,
  Wealthfront $1.57B, Hippo $811M, Root $723M, Funding Circle $701M.
- **Rule A**: eleven $1B+ marks that rested on the unicorn snapshot were replaced by the priced round's own
  citation (Ajaib, BharatPe, Chainalysis, Clip, Coalition, Cred, Etched, PsiQuantum, Razorpay, Slash, and
  Kavak's March 2025 round at $2.2B superseding its $8.7B), and Avant's $1.98B, which had no priced figure,
  fell to below $1B. Primary citations replaced secondary ones for Parafin ($750M, Bloomberg), Gusto ($9.3B
  tender, Fortune), Revolut ($115B, Bloomberg) and Teya ($1bn+, Sifted). No $1B+ mark rests on a vendor.
- **Momentum slice**: the judges checked every 2021-or-later hot-sector private row with one web search.
- **Weak CIK joins**: five wrong-entity statuses or floats (Balance, Solana, Wave, Castle, Harmonic) were
  already replaced by cited values; the Form D bands riding weak joins match their companies.
- **Unicorn re-intersect** (loose names): every match is banded or has a documented reason (Avant; the
  Figure hit is Figure AI, a different company).
- **Duty 7, blind 5%**: 9 rows re-judged by a second judge with no access to the record; 52 of 54 cells
  agree. Privy's stage moved to Growth (an unnamed round after a documented seed and Series A); Teya keeps
  its $1B floor on Sifted's report (the blind judge had found no priced figure). Both carry `unstable`.
- **Duty 9, the class**: the same reading applied to the one other row in Privy's position (Lighter, a $68M
  unnamed round after one earlier round, above the $40M Series A ceiling for 2022 on: Growth). NYDIG,
  Futureswap, RHI Group and OnePay stay undetermined because the entry itself or the instrument is unknown.

## 8. Firm profile

Thesis “The future belongs to the rebels.” (the homepage hero, also on the firm's coin; the competing
line, the meta description, runs 34 words). History 56 words: founded in Palo Alto in 2012 by Micky
Malka with a $100M first fund (LAVCA); Coinbase, Robinhood, Credit Karma, Nubank, Revolut; about $21
billion; Ribbit Capital Z, $562M in 2026. HQ Palo Alto, CA (Form ADV principal office; the ADV also lists
New York; the site names no office). AUM $20,775,390,188 both ends (ADV 2026-03-30, Item 5.F). Funds: 14
entries, Ribbit Capital, L.P. $100M (2012) to Ribbit Capital Z $561.9M (2026), with the Bullfrog growth
line and Leapfrog; six sizes asserted against their filings, seven are offering amounts from filings that
report $0 sold (press corroborates VI and Y). Two hedge-fund-type evergreen vehicles (RBT, Ribbit OB1), the
founder side funds, holding vehicles and the single-deal vehicles are described in the basis, not listed.
Stages Seed, Series A, Growth (derived); geography US, then Europe and Latin America (derived); scope
Specialist: Fintech & Payments, Crypto & Web3, AI & Applied AI (derived; the site has no sector tags);
range $6M to $427M around a $30M median entry round (126 members, judged rounds; a round size, not a
cheque). Notables Coinbase, Robinhood, Stripe, Revolut, Nubank. Individuals 33: eight titled from the
record, 25 name-only. Icon: the site's 256px icon on the brand's own green plate (0.945x, contrast 10.6:1,
ramp 1.07px); upload at ingest.

## 9. Open rulings for Erik

1. **Token caps as marks (decisions.md R1).** Solana ($69.9B, SOL) and Aave ($2.28B, AAVE) are banded on
   the token's market cap, as the a16z and BCV books do, because neither labs company has a priced equity
   round. The blind judge banded Solana the same way on its own. If token caps are out, both fall to below
   $1B.
2. **Caret (decisions.md R2).** Priced units in Safehold's private subsidiary at an implied $1.75B (the 8-K
   of 2022-02-15 names Ribbit): kept as a venture position; the alternative reads it as a structured
   position in a listed REIT (out).
3. **Country table: fixed 2026-09-29** (Erik: "fix the country issue to resolve to the correct country
   now and in the future"). The vocabulary moved to `scripts/countries.py`: all 249 ISO 3166-1 codes plus
   XK, every name the inputs use, and no signal from filing havens (Mauritius, Gibraltar, Monaco, the
   Caribbean IBC jurisdictions), mis-picked dropdown entries (North Korea for Seoul filers) or former
   states (Czechoslovakia). Tested against 1,293 strings: nothing that resolved before changed. Rows fixed:
   Xapo GI here and in Greylock, Mutual Risk Management BM (Greylock), Celestia LI (BCV). `prepare` now
   asks the judge about a non-US Wikidata country on a one-word name; here it asked 10 (Ajaib, BharatPe,
   Clip, Cred, Kavak, Monzo, Nubank, PhonePe, Razorpay, Borro), all the right company and confirmed.
   Greylock and BCV were re-ingested with those rows on Erik's approval (2026-09-29): dry runs 0 new /
   0 removed, readback exact (553 and 414 rows, 0 mismatches).
4. **Published-name calls** under the all-caps rule: CAN Capital, NYDIG and TOP (The Open Platform) read as
   words (Can Capital, Nydig, Top Group); dv01 reads letter by letter (DV01); the firm's "ReDeFine" is
   published as the company writes it (Redefine).
5. **The 2019-2020 archive** (section 4): run `scratch/ia-gap-fetch.py` in a quiet window and add any
   2019-2020-only company as a delta.
6. **Siblings to align at the wave pass** (the accepted pairs in `companies/cross-rulings.json`): a16z
   (Cowboy Space, Gusto, Lighter, Point, Revolut, Robinhood), Felicis (Gusto), Greylock (Revolut), Sequoia
   (Enter, Robinhood), Thrive (Robinhood), Creandum (Fuse Energy), First Round (Farcaster, Gauntlet, Health
   IQ, Kiavi, Persona), Redpoint (Parafin: its $1.5B has no source; the Series C was $750M), Y Combinator
   (Vouch: YC's Vouch is Vouch Insurance, and its "defunct" came from First Round's namesake). Also seen in
   passing: Lux publishes "Ftx" (a letter-read name, FTX), Coatue "CRED", and a16z's Point row describes a
   different Point (a debit-card company) under the home-equity company's slug.
7. **Individuals**: 25 people publish without a title because the site gives none and no release quotes
   them with one; Jordan Angelos is "General Partner" only on aggregators.

## 10. Rebuilds and deltas

The one scheduled rebuild after the recall probe (195 rows: the 23 not_member rows out, four duplicates
merged, Delphia and 14 Form D rows from the widened roster in), then a second rebuild for the delta's 14
not_member verdicts (181 rows). Both builds were diffed against snapshots: no verdict or classification
re-keyed, no name changed. Delta: 15 items (14 Form D rows, all out; Delphia). ForUsAll was judged before
the rebuild on its own release. 15 identity merges (renames such as ZenPayroll to Gusto, Activehours to
EarnIn, LendingHome to Kiavi, SaltPay to Teya, Sling Money to Morse Money, IBOD Company to Root).

## 11. Playbook write-backs proposed (not applied mid-wave)

1. **IA cooldown**: never queue a fetch to fire when a cooldown ends (BCV's lesson, applied here); schedule
   the few gap requests for a quiet window with no sibling run using the archive.
2. **The structural stage rule for press-documented sequences**: an unnamed priced round after documented
   rounds is staged by the prior-round count and the era band, at medium (duty 9 here).
3. **Titles from the record** for a site that publishes none: the file_list overlay
   (`sources/web/team-titles.json` as a second `team_sources` entry); worth a line in section 11.
4. **Rule 10's name key** misses "X" against "X.com" (Checkout against Checkout.com, same company, same
   value); strip a trailing ".com" in `cross_key`.
5. **Co-issued fund Form Ds** in `own_fund_filings`: Ribbit OB1's feeders file one co-issued offering,
   and the per-accession scan gave its 2025 amendment to the Cayman feeder.
6. **`record --replace-note`** for rewrite passes (what `scratch/set-notes.py` does).
7. **Build order**: the industry filter drops Form D rows before the identity merge (Nave Holdings, Nave
   Bank's holding company, dropped as Commercial Banking).
8. **Country table**: done in `scripts/countries.py` (section 9, item 3).

## 12. Usage line

Close (2026-09-28, ~22:15 UTC, Opus 5.5): the weekly and five-hour percentages are not readable from this
session. Web searches: about 75 of the 200 cap, subagents included (the four batch judges, the blind judge's
12 and this session's). Subagents: 4 classification judges, 1 blind judge.

## 13. Prompt count

**3**: the kickoff ("please collect ribbit capital"), "fix the country issue to resolve to the correct
country now and in the future, afterwards ingest" (2026-09-29), and "please reingest greylock & BCV". Corrections from Erik: none.

## 14. Ingest (run 2026-09-29, on Erik's approval)

1. Icon: `fetch-investor-icon.ts` uploaded `investors/ribbit-capital-c067140720.png` (256px master, the
   brand's green plate, contrast 10.6:1, ramp 1.07px); `icon_url` points at the bucket.
2. Investor row: `ingest-investor.ts ribbit-capital` upserted 1 row.
3. Companies: the dry run planned 181 new, 0 removed, from 0 live; the write upserted 181/181 and the
   script's own count check closed at 181.
4. Readback, every column the ingest writes against `base.csv`: 181 rows, 0 cell mismatches, `icon_url`
   matching `investor.json`.
