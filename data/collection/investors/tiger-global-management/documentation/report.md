# Tiger Global: Build & Reconciliation Report (PRO-167)

**Linear issue** PRO-167 · **slug** `tiger-global-management` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session with two usage-limit pauses · report written 2026-09-29.
**Not ingested: the ingest waits on Erik's approval (section 15).**

---

## 1. The answer PRO-167 asked for

**The base is 560 companies, plain `verify` (links checked) is clean, and the firm profile is built.**
Tiger Global runs two strategy families under one adviser (Tiger Global Management, LLC, CRD 160318), so
the book is the private-equity desk only: Private Investment Partners I to XVII, the PIP 1 co-investment
series, the single-company holding vehicles (FB Partners, LinkedIn Holdings), the Singapore "Internet
Fund" and "Tiger Global <n> Holdings" vehicles that hold the Indian and Chinese stakes, and the per-deal
vehicles (for example "Tiger Global PIP XII-6 LLC" in Confluent's IPO filing). The public desk (the hedge
funds Tiger Global, L.P., Ltd. and II, Tiger Global Investments, Long Opportunities, Crossover, and Tiger
Veda) is `other_desk`. The firm has never published a portfolio list, so membership rests on filings and
press, not on a site list.

Out: 124 rows. About 70 are public-market positions (13F, 13G and 13D lines, SPAC and PIPE blocks: T3),
9 are control positions (seven companies; Despegar under three names), 1 is a public-desk row (MELI
Kaszek Pioneer Corp), 12 fall under the person and seat tests (Harry's and TeachersPayTeachers under
Erik's 2026-09-28 board-seat ruling), and the rest are other firms named in Tiger's filings, Form D name
matches and companies with no Tiger money on record.

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean at 560 rows, links sampled; flagged debt only (section 7) |
| Desk partition in `decisions.md` | D1, D2 (home desk `us`, partition `public`), D8, X1; `config.json` `desks` |
| Every row judged, classified, cited | 560 published rows (559 members, 1 `uncertain`: Clobotics, section 10), 124 out, each with a recorded verdict; 560/560 classified |
| Firm profile | `investor/investor.json` + `sources.json` by `build-firm-profile.py`; taxonomy gate and `profile_copy.py` ok; every field populated or null, each with a source |
| `review.html` rendered | Served on a local static server and checked: 560 rows flat, profile panel expands |
| Measured recall | Section 5 |
| Cross-investor (rule 10) | 552 shared rows: 527 agree, 25 accepted, 0 disagree; 28 namesake pairs ruled distinct |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 560 | |
| Private | 357 | 64% |
| Acquired | 100 | 18% |
| Public | 73 | 13% |
| Defunct | 22 | 4% |
| Unknown | 8 | 1% |
| $1B and above | 193 | 34.5% |
| of which $10B and above | 39 | Facebook $1.83T, OpenAI $852B, Palantir $447B, ByteDance $330B, Alibaba $273B, Databricks $190B, Stripe $159B, Uber $142B, Waymo $126B, Snowflake $118B, Revolut $115B, Spotify $101B, Airbnb $92.8B, Mercado Libre $86.5B, Nubank $59.1B, Coinbase $50.6B, Cerebras $49.7B, NSE $46.4B, Everpure $43.4B, JD.com $35.6B, Zomato $31.7B, VAST Data $30B, Roblox $29.8B, Scale AI $29B, Trip.com $24.2B, Samsara $21.9B, Shein $19B, Toast $17.4B, Didi $16.2B, Sierra $15.8B, OpenSea $13.3B (stale, section 10), Grab $12.8B, Temporal $12.6B, Groww $12.2B, Checkout.com $12B, PhonePe $12B, Meesho $10.7B, Chime $10.1B, Instacart $10B |

Bands: below $1B 367, $1B+ 154, $10B+ 27, $100B+ 12. Entry stage: Growth 360, Series A 125, Seed 17,
Pre-Seed 2 (Habi, Zaraye), round not on record 56. The book is a 2021-2022 book: 179 entries are dated
2021 and 116 are dated 2022; 67 rows carry no entry date. Headquarters: US 265, India 114, China 27,
Brazil 24, Israel 14, UK 14, Australia 9, then Canada, Singapore and Germany 8 each, France 7, Colombia
and Indonesia 6 each, and a tail; 551 rows carry a city, 9 are `city_unknown`. Focus: Consumer &
Marketplaces 159, SaaS 103, Fintech & Payments 92, Industrial & Robotics 34, Healthcare & Bio 27, Media,
Gaming & Advertising 25, then Data Infrastructure, AI & Applied AI and Crypto & Web3 22 each.
Membership evidence: web 450, fund filing 104, adjudicated Form D 6.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 17 | 0 | 17 | 5 | 12 | **29.4%** |

Coverage 100%. Graduated: Algorithmiq, Beleza na Web, Carma, FanCraze, Vecmocon. The 12 nos rest on a
cited end for 4 (Cube26, sold to Paytm in 2018; Jit, to Torq in 2026; Magna, to Payward in 2026; Shopflo,
acquired with its 2022 seed as its last round of any size) and the dated absence test over the named
surfaces for 8 (August Schools, Axis, CreditBook, Mayfair, Miferia, Oico, Rebill, Unblocked). Tiger runs
no seed programme: the 17 are its 2021-2022 seed cheques, so the rate describes a small, recent cohort.

## 3. The boundary

- **One adviser, one firm (D1).** Tiger Global Management, LLC (CRD 160318, New York) with relying
  advisers in Hong Kong, Singapore, Australia and Shanghai. The ADV annual amendment of 2026-03-27
  reports $78.0B regulatory AUM over 37 private funds.
- **Two strategy desks (D2).** Home desk `us`: the private-equity funds and their vehicles (section 1).
  Partition `public`: the hedge-fund family. The desk patterns in `config.json` classify every vehicle
  seen in the record, including the per-deal "PIP XII-6 LLC" and "PIP 1-T" vehicles
  (`desks._vehicles_seen_note`). eLong moved to the home desk when its 2004 F-1 named PIP I (then Tiger
  Technology Private Investment Partners).
- **Public-market lines (D3, D4).** A 13F, 13G or 13D line is a public holding (T3): 49 such names sit
  in `verify` as traps. The firm's "Our Story" names are evidence of a position, not of a venture entry;
  each was checked against the private record.
- **X1, a public-desk vehicle in a private round.** Mercado Libre: Tiger Global, L.P. (a hedge fund) is
  the only Tiger entity in the 2007 IPO holder table, a pre-IPO purchase: member, `boundary`. Blend Labs
  and Chime: the IPO filings name only Tiger Global Investments and Long Opportunities (public desk):
  members under X1, `boundary`. Katapult: the de-SPAC block is a public-market purchase: out, `boundary`
  in the record. Pagaya and Procore carry the flag as well, though both entries are private-desk vehicles
  on filings (PIP XIV's Series E purchase agreement; Tiger Global PIP 11 LLC signing Procore's 2019
  investor rights agreement).
- **Control positions (new exclusion `control_position`).** Despegar (57.3% before its IPO; also filed as
  Decolar and Satylca), AlloCiné, AlexandAlexa, Cobone, JobStreet, Takealot, Super73: Tiger owned or
  controlled the company, a buyout rather than a venture position. Wikimart stays a member (about half
  the company after its first cheque, not a control purchase on the record): Erik's call (section 10).
- **Board seats (Erik's ruling of 2026-09-28).** Harry's (with ADKM and HF Global) and TeachersPayTeachers
  (TPT Holdco, TPT Investor, Teacher Synergy) are out: a seat with no Tiger fund named. InVision and Nylas
  stay in, because press names Tiger's investment.
- **Vehicles, not rows (D8).** Single-deal and co-investment vehicles are how Tiger held a company, not
  companies. MatchNet (Spark Networks) stays out: listed in Frankfurt before Tiger bought.

## 4. Coverage per evidence regime

- **Firm site**: five pages, no portfolio and no team page. "Our Story" names 18 companies
  (`sources/site/our-story-2026.json`).
- **Archive**: the Internet Archive holds 468 URL keys for tigerglobal.com
  (`sources/wayback/cdx-tigerglobal.com.json`). 1999-2002 is an unrelated web-hosting business; the firm's
  pages are /investors (2020) and /ourstory, /ourstrategy, /ouredge (2026). No portfolio or team page in
  any era, so the archive adds no members (D9). Common Crawl has nothing before CC-MAIN-2020-50.
- **Form ADV** (`sources/registers/adv-160318.json`): 37 private funds with gross assets, owners and
  related-person shares; the profile's AUM and fund list read from it.
- **EDGAR**: 84 registrants (57 added from the CIK lookup table because the company-name search seeds
  nothing, section 12), 13F since 2003 (1,098 issuers over 99 filings: the trap list), the Form D sweep
  (226 accessions, 82 issuers), full text (4,240 hits, 411 third-party registrants triaged: 90 portfolio,
  40 target, 92 public, 189 noise). A second full-text pass on the former name "Tiger Technology" found 21
  more registrants, among them Ctrip's 2003 and eLong's 2004 filings.
- **Offer documents outside the US** (`sources/registers/probes.json`): SEBI DRHP/RHP and HKEX
  prospectuses name Tiger's Singapore vehicles as holders (Zomato: Internet Fund VI, 6.04%; Meituan 2018:
  Internet Fund IIIA and IV). The company registers are not usable for holders: MCA (403, paid MGT-7),
  gsxt (JS challenge), SIGER (login); Brazil's CNPJ gives status only.
- **Wikipedia**: insource over 238 articles (about 120 real candidates with sentences), and the Tiger
  article's PIP table (vintages and sizes, `sources/web/wikipedia-tiger-global-management.wikitext`).
- **Press**: a Google News sweep of 1,055 queries (5,222 unique headlines, extracted into about 820
  headlines naming Tiger and about 1,900 funding headlines), the per-company query
  '"<name>" "Tiger Global"' (753 companies), a Bing News RSS layer (812 companies) and 413 publisher pages
  read for the sentence naming Tiger.
- **Model-memory lists**: four era lists (2003-2017, 2018-2020, 2021, 2022-2026) used as leads only;
  none is evidence, and a lead with no headline or filing behind it was rejected.

## 5. Recall probe and measured recall

**Recall additions**: 561 rows in the ledger carry their own evidence, graded A (a filing naming a Tiger
vehicle as a holder while the company was private, 62), B (a headline naming Tiger and the company with
an investment word, 371), C (a Wikipedia sentence, 37), D (the article's own sentence naming Tiger, 47 in
wave 1 after 19 of 66 were rejected by hand), plus 48 from the recall-probe wave (25 of 70 D-grade
candidates rejected) and Ola. Verified A to C additions were seeded as member verdicts
(`seed-recall-pro167`), which a judge's verdict replaces; D grades and public-desk-only filings were
never seeded. 44 rejects carry their reasons in `scratch/recall/manual-decisions.json`.

**Measured recall** against three independent model-memory lists of Tiger's best-known private
investments, sorted by confidence: high 43 of 54 in the base (2 more ruled out), medium 41 of 51, low 27
of 32. The genuine misses, **not researched in this run**: Ozon, Seznam.cz, Deliverect, Pocket FM,
Credgenics, Olive AI. Leads from the judges, also not researched: Mono (Nigeria, Series A 2021) and Mono
(Colombia, seed 2022), Matrixport, OkCredit, Mr Yum, Wati, Conta Azul, Daki, Little.

## 6. Method deltas

- **An evidence pipeline for a firm with no list.** Press sweep, headline extraction (about 2,700 lines),
  per-company verification queries, publisher-page sentence checks, full-text triage and Wikipedia,
  merged into `scratch/recall/candidates.json` and graded A to D by `scratch/select-additions.py`. The
  D grade is noisy (about a third rejected by hand: the sentence names Tiger for another company or round)
  and needs the manual pass.
- **Bing News RSS as a second press layer** (`scratch/bing-news.py`, its own 0.5/s bucket; the item
  carries the publisher URL, so no decode). On 55 overlapping candidates Google's title match found 45 and
  Bing 39, both 37, Bing alone 2. It kept the run moving while GV held the shared Google bucket.
- **Former names in the full-text phrases.** "Tiger Technology" found Ctrip's and eLong's filings, which
  "Tiger Global" cannot.
- **Offer documents as a holder backtrace** for India and China (section 4).
- **Chunked recording.** Session restarts killed the background judges twice; judges now record in
  chunks (batch-NNNa, b, c) so a restart loses at most one chunk.
- **Append-only recall writer.** `scratch/write-additions.py` first replaced every addition with the
  current plan and dropped 516; they were restored from the base notes under the record lock, and the
  writer now appends only and holds `exclusive("record-tiger-global-management")`.
- **Model mix**: the headline extraction ran on Sonnet (a mechanical step); every judge ran on the default
  model.

## 7. Flags and debt behind `verify`

On the 560 published rows: `stale` 115, `unicorn_name_match` 58, `model_disputes_source` 44 (mostly wrong
Wikidata or SEC joins on one-word names, each disputed with evidence), `cik_weak` 22, `suspect_base` 17,
`city_unknown` 9, `boundary` 5, `stage_disputes_band` 5, `cite_pending` 4, `unstable` 2 (duty 7),
`token_funded` 2 (Near Protocol, Polygon), `duplicate` 1 (Danke: the flag predates the merge that made it
the canonical row). `cite_pending`: Spotify, Palantir, Shein and StoneCo are $1B+ rows whose Growth stage
comes from the record (model) because no page read names the round in which Tiger entered. Debt: 56 rows
with the round not on record, 67 rows with no entry date, the unresearched recall leads (section 5).

## 8. Standing duties and the A/B pass

- **A/B on the 167 visible rows** ($1B+, public, or notable). Public caps read 2026-09-29 (StockAnalysis;
  INR at the ECB rate): Facebook $1.83T, Palantir $446.97B, Spotify $101.38B, Mercado Libre $86.55B (fell
  about 31% in a year, so 100b_plus to 10b_plus), Cerebras $49.7B, and the rest of the listed set. Allbirds
  is acquired (the business was sold; the listed shell renamed itself Smartbird). New priced marks: TRM
  Labs $2B, Innovaccer $3.45B, Cohere $7B. Weave's take-private is signed, not closed: still public.
- **Rule A**: Commonwealth Fusion Systems, Qualia and SirionLabs read below $1B (no page states a
  valuation; aligned with the sibling books). Snapdocs ($1.5B) and Sendbird ($1.05B) keep their priced
  rounds, stale, although vendor secondary estimates sit 80-90% lower. No $1B+ mark rests on a vendor.
- **Momentum slice**: every 2021-or-later hot-sector private row got one mechanical web check.
- **Weak CIK joins**: 22 `cik_weak` rows; the statuses and floats riding them were read against the
  company and replaced by cited values where wrong.
- **Unicorn re-intersect**: every one of the 58 name matches is banded or carries a reason.
- **Duty 7, blind 5%**: 28 rows re-judged by a second judge with no access to the record; 133 of 140
  cells agree (95%). InVision keeps Series A (Lee Fixel joined the board on the Q4 2013 Form D round);
  clicOH keeps Córdoba. Both carry `unstable`.
- **Duty 9, the class**: the 67 rows with an undetermined stage were swept with the same reading; 12 were
  staged from a cited round, the rest stay undetermined because the entry round is not on record.

## 9. Firm profile

Thesis "Tiger Global is a research-driven investment firm pursuing a long-term approach to partnering
with high-quality, innovative companies across different stages of their lifecycle." (the first sentence
of the homepage H1, verbatim; the competing line is the Our Story H2, "We invest in the defining
companies of the future."). History 74 words: founded in New York in 2001 by Chase Coleman as Tiger
Technology; private investing from 2003; Facebook, LinkedIn, JD.com, Flipkart; private funds hold at least
$31B of the $78B the firm manages, and the page covers the private investments only. HQ New York, NY (ADV
principal office, 9 West 57th Street; the site agrees). **AUM $31,536,376,225 both ends, a floor**: the
gross assets of ten PIP master funds and the 15 PIP 1 co-investment vehicles on the ADV; PIP XI is left
out because its ADV section repeats PIP XII's figures to the dollar. Funds: 16 entries, PIP I ($99M,
2003) to PIP XVII (2026, size not yet filed), sizes from the Form D filings and the Wikipedia table. Stages
Seed, Series A, Growth (derived); geography core US and India, other China, Latin America, Europe
(derived); scope Generalist with six sectors of 25 or more rows; range $12M to $500M around a $53M median
round (471 members, the round in which Tiger is first named: a round size, not a cheque). Notables
Facebook, OpenAI, Uber, Spotify, LinkedIn. Individuals 6 (Chase Coleman, Eric Lane, Evan Feinberg,
Griffin Schroeder, Gregory Seidell, Ira Platt), curated because the site has no team page. Icon: the TG
monogram (`sources/site/icon-tg-monogram.svg`), chosen by measurement after the wordmark and both favicons
failed (enlargement or a soft edge); dry run only, preview `investor/icon-preview.png`, upload at ingest.

## 10. Open rulings for Erik

1. **X1 rows** (section 3): Mercado Libre, Blend Labs and Chime are in on a public-desk vehicle's purchase
   before the listing; Katapult is out as a de-SPAC block. If a public-desk purchase is never venture
   entry, the three leave the base.
2. **Control positions** (`control_position`, 9 rows, seven companies): confirm that a controlling stake
   is out. Wikimart (about half the company after the first cheque) is kept in.
3. **Allbirds as acquired**: the business was sold and the listed shell (Smartbird, about $27M) is a new AI
   infrastructure company; the row reads acquired, below $1B.
4. **Harry's and TeachersPayTeachers out** under the 2026-09-28 seat ruling, while InVision and Nylas stay
   in on press naming Tiger. Confirm the line.
5. **Collapse readings** (marks kept on the last priced round, stale; COLLECTION.md 6 does not let a fund
   mark or an internal price replace them): Avant $1.98B (2015; most of its equity reported gone; Ribbit's
   book reads below $1B), OpenSea $13.3B (Tiger marked its stake down 94% in 2023), Snyk $7.4B (employee
   share price down about 90%), Relativity Space $4.2B (Eric Schmidt took control in 2025 at an undisclosed
   price), Snapdocs and Sendbird (vendor estimates). Ola reads below $1B on Vanguard's $70M mark as collapse
   evidence (the note carries it; no figure minted).
6. **Grafana Labs**: this book keeps $6B (August 2024, the last closed round); the Coatue, Lightspeed and
   Sequoia rows carry $9B from a February 2026 report of a round being raised, with no closing found.
7. **Cedar**: the a16z row is the same company by its own evidence (accepted in `cross-rulings.json`), but
   its values should be aligned; the Y Combinator Cedar is a different company.
8. **The four `cite_pending` rows** (Spotify, Palantir, Shein, StoneCo): the stage stays Growth from the
   record until a page names Tiger's entry round.
9. **The recall leads** in section 5: research them as a delta, or accept the measured recall.
10. **Clobotics stays `uncertain`** (re-checked at close, as COLLECTION.md 2 asks of every uncertain row):
    the company's own release credits its $10M Pre-B+ (January 2020) to "Tiger Management Fund", which is
    Julian Robertson's firm, while KrASIA's article has "tiger-global" in its URL and "Tiger Investment" in
    its text. The investor is named but conflicts between two Tiger firms, so it is not a bare name match.
    If the release is read as Julian Robertson's firm, the row goes out.

## 11. Rebuilds and deltas

Wave 1 built 641 rows. The one scheduled rebuild after the recall probe gave 568 (the first 109 not_member
rows out, 17 identity merges in, the recall-probe additions in) and a 63-row delta over two batches,
judged by two delta judges. The final rebuild for the delta's verdicts gave 561, and two identity fixes
(Craftsy merged into Sympoz, whose published name is Craftsy; Ola split from Ola Electric with a
`never_merge`) left 560. The rebuild's re-key moved two verdicts onto the wrong company (Apollo Global
Management onto Apollo Group, TPT Holdco onto Teacher Synergy); both were restored by hand under the
record lock. 22 identity merges in all (renames such as Freshdesk to Freshworks, UrbanClap to Urban
Company, IndWealth to INDmoney, OctoML to OctoAI, SVMK to SurveyMonkey, Beleza na Web, Colony Labs to
Scribe) and 49 published names (for example Ctrip to Trip.com, Aihuishou to ATRenew, Pure Storage to
Everpure).

## 12. Playbook write-backs proposed (not applied: tooling-session territory)

1. **EDGAR company search is dead for `edgar-entities`**: the name search returns the smart-search
   landing page, so it seeds nothing. Seed from the CIK lookup table or EFTS (what
   `scratch/registry-supplement.py` does).
2. **`run.py prepare` KeyError at line 962** (`formd[row["slug"]] = formd.pop(hit)`): two live rows re-key
   onto one cached rounds entry after a not_member merge. Worked around by dropping 12 non-live entries
   from `formd-issuer-rounds.json`.
3. **Full-text phrases must include the firm's former names** (Tiger Technology found Ctrip and eLong).
4. **The builder's near-duplicate merge folds a distinct prefix name** (Ola into Ola Electric); a
   prefix match needs a same-company check.
5. **The rebuild re-key crosses companies** (Apollo Global Management onto Apollo Group); read the rename
   list after every rebuild, as the Khosla lesson says, and refuse a re-key across different CIKs.
6. **The shared throttle has no per-session fairness**: GV's 15 Google News clients starved every other
   session until GV capped at two slot locks.
7. **Bing News RSS as a press layer** (section 6), with its measured overlap.
8. **The A to D grading for a firm with no list**, with the D grade's noise rate and its manual pass.
9. **SEBI and HKEX offer documents** as a holder backtrace for Indian and Chinese companies.
10. **Record in chunks**: background judges die on a session restart.
11. **A recall-addition writer must append**, never replace (516 additions dropped and restored).

## 13. Usage line

Kickoff (2026-09-29 00:31 UTC, Opus 5.5): five-hour window 7%, weekly 25%, Fable 6%. Close (about 19:00
UTC): five-hour window 79%, weekly 0% (a new week began mid-run). Two usage-limit pauses (about 11 hours
and 1 hour). Web searches: about 100 of the 200 cap, subagents included. Subagents: 8 grind judges, 2
delta judges, 3 A/B judges, 1 blind judge, fix, cross-investor and sweep agents, a profile agent, 4
model-memory lists, 3 headline extractors (Sonnet), full-text triage and register probes.

## 14. Prompt count

**3 so far**: the kickoff ("please collect Tiger Global") and two "continue" messages after the usage
pauses. Corrections from Erik: none. The count is final after the ingest decision.

## 15. Ingest (awaiting Erik's approval)

Order for a first-time investor (COLLECTION.md 9):

1. Icon: `npx tsx scripts/fetch-investor-icon.ts tiger-global-management data/collection/investors/tiger-global-management/sources/site/icon-tg-monogram.svg`
2. Investor row: `npx tsx scripts/ingest-investor.ts tiger-global-management`
3. Companies: `npx tsx scripts/ingest-companies.ts tiger-global-management --dry-run`, then without
   `--dry-run`, then a readback of every written column against `base.csv`.

With the ingest, under Erik's rule of 2026-09-28, the stale rows in other books named by the accepted pairs
in `companies/cross-rulings.json` are aligned and re-ingested (figures compared and read back before
writing): a16z (Airbnb, Cedar, Quora, Revolut, Temporal), Accel (BlackBuck, Koo), Battery (CHEQ,
GrubMarket, HeadSpin), Benchmark (Quora), EQT Ventures (HeadSpin), Felicis (HeadSpin), Greylock (Airbnb,
Redfin, Revolut), Lightspeed (Byju's, Frubana, Temporal), Menlo (Sidecar Health), Redpoint (Scribe),
Ribbit (Avant), Sequoia (Airbnb, Alkira, Eventbrite, Getir, Rogo, Temporal), Spark (Rapyd), Thrive (Rogo),
Y Combinator (Airbnb, Frubana, Meesho).
