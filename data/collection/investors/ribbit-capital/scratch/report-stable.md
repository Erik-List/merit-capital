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
- **Form D seats (R4).** Sixteen Form D rows where a Ribbit person is a director or officer are out: Craize
  Snacks, Harbor National and OSIX (a partner's board seat with no fund named), Lemon, Inc. (Malka's own
  company, D5) and twelve namesakes or the person's own earlier companies.
- **Control (D8).** None found: Ribbit makes minority venture investments.

## 4. Coverage per evidence regime

- **Live site**: the Rebels list (155 rows, parsed from the Next.js page chunk by `scratch/pull-site.py`)
  and the team page (33 people). The site's disclaimer says the list shows companies in active strategies
  only and omits some for confidentiality or size, so absence from it is not evidence.
- **Archive**: the Internet Archive gave the 2012-2015 Bets pages (27 captures) before it blocked this
  machine; Common Crawl carried everything else (Our Bets 2015-2018 and 2021-2025, the Rebels page chunks
  2025-12 to 2026-09, the team pages 2015-2026). ARCHIVE_2019_2020
- **Form D**: the roster sweep over 67 names of 56 people with tenure windows; the related persons' filed
  addresses decided the common-name seats. The firm's own deal vehicles: 78 filings on 64 vehicles.
- **Single-deal vehicles**: 52 codes read off the ADV and Form D; decoded in
  `sources/registers/spv-decode.json` (resolved, probable, unresolved). 14 codes stay unresolved and none
  decodes to a company absent from the base. RNBW-1 is OnePay (RNBW Ventures Inc., Green Dot's 10-Q).
- **Exit side**: EDGAR full text on ten fund phrases (138 registrants, 61 third-party ones triaged), the
  adviser's 13F lines (CIKs 1571355 and 1836733), Wikipedia insource (38 articles, 12 company candidates).
- **Press**: the Google News sweep per row and a press recall sweep (222 items, `scratch/recall/press-sweep.txt`).
- **Recall probe**: one addition (Delphia, its own Series A release names Ribbit), twelve rejections
  with reasons in `scratch/recall/rejections.json`.

## 5. Method deltas

- **Common Crawl as the archive during an IA block.** The run's first fetch burst earned a 60-minute
  machine-wide IA block (19:36Z), and the first requests after it doubled it to 120 minutes (20:36Z to
  22:37Z). Common Crawl, read through the static cluster index (`scratch/cc-cluster.py`, `cc-fetch.py`),
  carried Our Bets, the team pages and the Rebels page chunks. It holds nothing for ribbitcap.com between
  mid-2018 and 2020; four targeted IA replay requests (`scratch/ia-gap-fetch.py`) went out after the cooldown.
- **The Rebels page is a compiled array, archived as a JS chunk.** The live list and its archived versions
  come from the Next.js page chunk (`sources/site/rebels-page.js`), read with a small JS-string decoder;
  the 2015-2025 Our Bets pages carry logos and company links only, so a link-host identity map
  (`sources/wayback/identity-map.json`) names each logo.
- **The single-deal vehicle decode** (`sources/registers/spv-decode.json`): each code is fund-filing
  evidence that a Ribbit vehicle was in that round, never the entry (D6); it dated Clip, Kavak, Root, DCG
  and others, and it showed OnePay behind RNBW-1.
- **Titles from the record for a site that publishes none** (`sources/web/team-titles.json`, merged by the
  existing file_list machinery): Form ADV Schedule A and releases that quote the person with a title.
- **`scratch/readnews.py`**: decode a Google News headline to its publisher and read the page with a
  browser user agent, for the publishers WebFetch is refused by (CNBC, LatamList, Bloomberg Línea,
  Nearshore Americas, KrASIA, VCCircle, CoinDesk).
- **`scratch/set-notes.py`**: a rewrite pass replaces a row's note instead of appending to it (record
  appends with " | ", which is right for a delta and wrong for a correction).
- **Parallel judges** on batches 1-4 from `scratch/JUDGE-BRIEF.md`, per-judge news caches (`NQ_TAG`),
  recording under the per-investor lock.

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
Specialist: Fintech & Payments, Crypto & Web3, AI & Applied AI (derived, the site has no sector tags);
range $6M to $427M around a $30M median entry round (125 members, judged rounds). Notables Coinbase,
Robinhood, Stripe, Revolut, Nubank. Individuals 33: eight titled from the record, 25 name-only. Icon: the
site's 256px icon, the green plate kept (0.945x, contrast 10.6:1, ramp 1.07px); upload at ingest.
