# ICONIQ Growth: Build & Reconciliation Report (PRO-168)

**Linear issue** PRO-168 · **slug** `iconiq-growth` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session (paused 02:50 to 14:00 UTC on the usage limit), with Common Crawl
carrying the archive while the Internet Archive was in a machine-wide cooldown · report written 2026-09-29.
**Ingested 2026-09-29 on Erik's approval (section 14).**

---

## 1. The answer PRO-168 asked for

**The base is 169 companies, plain `verify` is clean, and the firm profile is built.** The investor is the
growth desk, not the family office: ICONIQ Capital, LLC (CRD 159198) advises $117.5B, and the growth desk is
the 81 funds whose general partner is an ICONIQ Strategic Partners GP ($32.2B of gross assets). Client money
(the ICQ Investments and ICQ Opportunities vehicles, client accounts, the 13F) never adds a member. Out:
four control positions (BlackLine, Truckstop.com, GoFundMe, and SLS Breeze, BlackLine's 2013 acquisition
vehicle), Tencent Music (bought at the listing), two credit funds the umbrella holds for clients, Blue Owl
(ICONIQ's own shareholder), and 19 Form D rows that matched an ICONIQ person's name outside the person's
ICONIQ tenure or not at all.

| Done-when item | State |
|---|---|
| Plain `verify` green, only flagged debt | Clean (`verify: clean`); debt is flagged (section 6) |
| Desk partition in `decisions.md` with its registrations | D1 to D3: the ADV's general-partner field, 81 growth-desk funds, CRD 159198, IPI Partners (CRD 284694) external |
| Profile through the taxonomy gate, every field populated or null, sourced | `investor.json` + `sources.json` built by `build-firm-profile.py` (15 funds asserted against their Form Ds); `profile_copy.py` ok |
| `review.html` rendered and checked | Served on the review surface (8931): 169/169 rows, profile section present |
| Cross-investor (rule 10) | 309 shared rows: 280 agree, 29 accepted, 0 disagree; 13 namesake pairs ruled distinct |
| The five deltas | X1 to X5 applied as written (section 3); X6 is new and flagged |
| Report, close, commit, Linear, closing message | This report; `run.py close` run; pathspec commit; PRO-168 comment |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 169 | |
| Private | 115 | 68% |
| Public | 27 | 16% |
| Acquired | 25 | 15% |
| Defunct | 2 | 1% (FTX, InVision) |
| $1B and above | 98 | **58.0%** |
| of which $10B and above | 32 | Anthropic $965B, OpenAI $852B, Alibaba $272.8B, CrowdStrike $258.7B, Databricks $190B, Stripe $159B, Uber $142.2B, Snowflake $115.7B, Robinhood $104.7B, Datadog $96.3B, Airbnb $92.8B, Anduril $61B, Ramp $44B, Canva $42B, Adyen $31.4B, Zoom $25.5B, Epic Games $22.5B, Whatnot $20B, Helsing $18B, Sierra $15.8B, Wayfair $13.5B, DocuSign $12.6B, Devoted Health $12.6B, NinjaOne $12.3B, Groww $12.2B, OpenEvidence $12B, Figma $11.1B, ElevenLabs $11B, Notion $11B, Oura $11B, Chime $10.1B, Quince $10.1B |

**The $1B+ share is 58.0%, with no ceiling** (Erik, 2026-09-26). It reads right for this firm: ICONIQ
Growth enters late (154 of 169 entries are Growth rounds, secondaries or tenders), and its book is the
large-company end of software, fintech and AI.

Entry stage: Growth 154, Series A 8, Seed 3 (all three in 2026), round not on record 4 (Ajaib, DX, Incident
IQ, Assured). Headquarters: US 145, UK 6, Canada 3, Germany 2, India 2, and one each in the Netherlands,
Sweden, France, Finland, Indonesia, Singapore, China, Israel, Mexico, Australia and the Bahamas (FTX).
Focus: SaaS 46, Fintech & Payments 26, AI & Applied AI 22, Healthcare & Bio 17, Consumer & Marketplaces 15,
Data Infrastructure 13, Security 11, DevTools & APIs 10, and 9 more across four sectors. Membership rests on
the growth desk's own portfolio grid for all 169 rows.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 3 | 3 | 0 | 0 | 0 | none (empty cohort) |

The three Seed entries (Grotto, Whirl AI, Standard Template Labs) are all 2026 incubations ("a first for
ICONIQ"), younger than 24 months, so censored. No S2A rate publishes for this book.

## 3. The boundary

- **One adviser, two desks (D1, D2).** Every vehicle is advised by ICONIQ Capital, LLC. The ADV's
  general-partner field splits its 351 private funds: 81 under the ICONIQ Strategic Partners GPs are the
  growth desk ($32,172,497,450 of gross assets, the `aum` floor, X4); the other 270 are the client platform.
  IPI Partners (CRD 284694, data centres) is a separate adviser and external.
- **Client money is not fund money (D3, X2).** ICQ Investments and ICQ Opportunities are client deal
  vehicles. They explain ICONIQ names in filings where no growth fund appears: Uber's 2015 convertible
  notes (ICQ Opportunities Funds 4 and 5), Salesforce's 2014 share issue (ICQ Investments 8), and
  addresses "c/o ICONIQ Capital" for clients' own holdings (GrubHub, Asana, Twilio, Celsius, Cerebras,
  Eventbrite and others). A 2012 "ICONIQ Capital" investment predates the first growth fund (June 2013) and
  is client era (Flipkart's 2012 round, Netshoes).
- **The 13F adds no member (D5, X3).** The umbrella's 13F (574 issuers) mixes client and fund holdings;
  it dated public positions and flagged the T3 questions in section 9.
- **Co-invest series count as fund money (D4, X6, flagged).** The growth GPs' own ICONIQ Strategic Partners
  Co-Invest series are fund vehicles even where their limited partners are clients. Six rows rest on a
  co-invest series with no flagship fund documented in the round and carry `boundary` (CrowdStrike, Fastly,
  Figma, Procore, Sprinklr, Uber); they can be reversed as a class.
- **Control positions (R1).** BlackLine and SLS Breeze (Silver Lake and ICONIQ took control in September
  2013), Truckstop.com (majority stake, April 2019) and GoFundMe (June 2015, the investor group took a
  controlling stake) are out as `control_position`. QGenda is in: Francisco Partners kept the majority.
- **Bought at the listing (R2).** Tencent Music: the TME co-invest series filed its Form D two days after
  the listing.
- **Not operating companies (T5).** Diameter Credit Co and the LibreMax fund (client-platform credit
  allocations); Blue Owl (a SPAC-merger PIPE, and the 6% owner of ICONIQ).
- **Form D name matches (T4).** 19 rows: Doug Pepper's InterWest and Shasta seats (Bloomspot, Brand.net,
  Doximity, Flurry, INVIDI, Marketo, NewsCred, Spredfast, Tapjoy), Will Griffith's TCV-era seat
  (Adknowledge), Seth Pierrepont's pre-ICONIQ seat (Xylos), Rob Bernshteyn's personal Medallia directorship,
  and namesakes (a Dallas oil venture, a Maine telephone company, biotech and consumer seeds).

## 4. Coverage per evidence regime

- **Live site**: the growth grid (172 companies, paged server-side on Webflow) and 143 posts (partnership
  announcements, IPO and exit notes, partner welcomes), `scratch/pull-site-iconiq.py`. The growth page's
  logo strip is the same 172 companies.
- **Archive**: Common Crawl's static cluster index (the index server refused connections) gave 1,851
  captures in 42 crawls; the grids parse to 75 companies (2020), 95 (2021), 128 (2022), 119 (2023), 143
  (2024), 142 (2025) and 156 (2026). After the IA cooldown ended, the Wayback CDX was read once: the
  growth desk's earliest portfolio page is iconiqcapital.com/growth of 2020-09-25 (73 logos, "investors in
  over 70 high growth technology companies"), and all 73 are in the base or excluded. Before 2020 the
  parent site was a splash page (captures of 2013 and 2017), so there is no earlier list to read.
- **Form D**: the roster sweep over 17 curated people with tenure windows, and 442 filings of the firm's
  own vehicles (`sources/edgar/formd-own-issuers.json`).
- **Co-invest decode** (`sources/edgar/coinvest-decode.json`): 15 series confirmed by filings, one
  inferred (Pluralsight PS2), 96 unresolved. The decode is corroboration only (D4).
- **Exit side**: EDGAR full text on three phrases (357 registrants; 96 third-party read sentence by
  sentence), registration-statement exhibits naming the growth funds (Airbnb, DocuSign, Warby Parker,
  Wayfair, The Honest Company, Pluralsight), Wikipedia insource (49 articles).
- **Press**: Google News per row (`"<name>" Iconiq`), a year-by-year press sweep with TechCrunch's search
  (`scratch/press-sweep.py`, 736 items).
- **Recall probe**: no addition. Checked and left out: Adaptive ML, Relativity Space, WeLab, ONE
  Championship, Apttus's peers on Wikipedia's list, Builder.ai, Prime Intellect and Enveda (named as
  "Iconiq" in rounds, absent from every capture of the growth desk's own list; the umbrella brand covers
  the client platform), Netshoes (2012, client era), SurveyMonkey, Dropbox, Coinbase and other 13F lines
  (public-market holdings, T3).

## 5. Method deltas

- **Common Crawl as the archive during the IA cooldown**, read through `cluster.idx` on the data host
  (`scratch/cc-cluster.py`, `cc-fetch.py`, one capture per URL per year) and parsed across four site
  generations (WordPress logo grid, per-company pages, DatoCMS `__NEXT_DATA__`, Webflow) by
  `scratch/parse-cc-iconiq.py`.
- **The ADV as the desk partition**: `scratch/parse-adv.py` reads Schedule D 7.B per fund (GP, adviser,
  gross assets) over 1,732 pages; the growth desk is a filter on the GP field.
- **Registration-statement exhibits as entry evidence**: investors' rights agreements and lock-up lists
  that name ICONIQ Strategic Partners date a pre-IPO growth-fund position when no release does
  (`scratch/fts-context.py`).
- **Research agents for the A/B pass**: three agents (pass B on 30 older marks, entry-round citations for
  38 rows, the momentum slice of 17 rows) and a blind judge for duty 7, each capped on web searches.
- **`scratch/emit.py`**: clears settled work flags (`cf`), carries a rule-6 country citation (`hcc`), keeps
  a band on a status-only line, flags marks older than two years `stale`, and adds `city_unknown` only
  where no city is on disk (a status-only fix line had set two public rows below $1B and two stale city
  flags; both fixed).

## 6. Flags and debt behind `verify`

On the 169 published rows: `stale` 46 (a mark older than two years that pass B could not replace),
`unicorn_name_match` 36 (informational, every value web-cited), `stage_uncited` 31 (all below $1B or
carrying another cited leg), `cik_weak` 14 (audited, section 7), `model_disputes_source` 14 (wrong-entity
Wikidata or SEC joins, each disputed with evidence), `cite_pending` 11, `boundary` 6 (X6),
`stage_disputes_band` 5, and `unstable` 3 (duty 7). **Entry citations still pending on 11 $1B+ or public rows**: Alibaba, Anduril,
Bill.com, CrowdStrike, GoodRx, Notion, OpenAI, Physical Intelligence, Stripe, Uber, Zoom (the mega-rounds
and tenders of 2025-2026 name their leads only). Two stale classification keys (Intercom, People.ai)
duplicate their canonical rows (Fin, Backstory) and are harmless. `defunct` is undercounted by construction
(COLLECTION.md 6).

## 7. Standing duties and the A/B pass

- **Pass A, the defence**: every private $1B+ row carries a priced event with a citation (Rule A: no
  vendor or aggregator figure; Forge, Sacra and similar citations on ezCater, Epic Games, Komodo Health
  and 1Password were replaced by the round's own source). Every public row carries a market cap of
  2026-09-25 to 09-28 (StockAnalysis; Adyen's EUR cap at the ECB rate).
- **Pass B, the attack**: 30 marks older than 2025 were attacked. Outcomes: one newer mark (Age of
  Learning, $3B in June 2021), one completed merger (Fivetran with dbt Labs, June 2026: Fivetran survives,
  dbt Labs reads acquired), three replacement citations, two unconfirmed leads (DeepL weighing a US listing,
  Monzo's share-sale plan), 23 with nothing newer (they keep `stale`). The first web pass had already moved
  the 2026 events: Airtable, Miro (Bending Spoons), Altruist (Vanguard) and Fin (Salesforce) are signed
  and not closed, so private at the agreed price; HeadSpin (PartnerOne, 2024) and Highspot (merged into
  Seismic, August 2026) are acquired; Smartling stays private after Vitruvian's majority recap; Oura has
  set IPO terms and is not listed.
- **Momentum slice**: all 17 private hot-sector rows first seen in the last five years that read below $1B
  carry a dated web check. One was a miss: **Backstory is People.ai renamed** (April 2026) and bands $1B+
  at the $1.1B Series D; the two rows were merged.
- **Duty 3, weak joins**: 14 `cik_weak` rows audited; the wrong-entity ones (Lucid Group on Lucid
  Software, a "Guild" and a "Zoom" read as acquired) were already disputed and replaced.
- **Duty 6, unicorn re-intersect**: every unicorn-list match is banded or acquired (Coupa, Flipkart,
  HeadSpin, Highspot, Loom, Panther, Wolt).
- **Duty 7, blind 5%**: 9 rows (seeded sample: CaptivateIQ, Sanity, Miro, Motorway, Dialpad, Fastly, Side,
  DocuSign, DX) re-judged by a second judge with no access to the record: 51 of 54 cells agree. All three
  disagreements are sectors: Fastly moved to DevTools & APIs and Side to SaaS (both on the company's own
  description), Sanity keeps DevTools & APIs; all three carry `unstable`. Status, band, entry stage and
  headquarters agree on every row, including Miro's signed sale and DX's acquisition by Atlassian.
- **Duty 9, the class**: the sector misses were products sold to businesses filed under the end market;
  the sweep of the Consumer & Marketplaces and infrastructure rows found no other row of that kind.
- **Rule 6, countries**: the non-US $1B+ rows carry a citation or a checked Wikidata join; seven one-word
  Wikidata countries were confirmed and eleven corrected to US (R6).

## 8. Firm profile

Thesis "The future is built by extraordinary people." (the growth page's hero headline; the meta
description and the hero's subline are recorded as competing lines). History 74 words: founded in San
Francisco in 2011 by Divesh Makan, Michael Anders and Chad Boeding; growth funds from 2013 under Will
Griffith; Snowflake, Datadog, Airbnb, Adyen and Robinhood before they listed; the seventh fund at $5.75
billion (2024); and the boundary line (the growth funds' minority stakes only, not client accounts). HQ San
Francisco, CA (ADV principal office; the growth page names no office). AUM $32,172,497,450 both ends (the
growth desk's funds, X4; the umbrella's $117.5B stays in the basis). Funds: 15 vehicles from ICONIQ
Strategic Partners (2013) to VIII and VIII-B (2025), nine sworn sizes asserted against their Form Ds and six
$0-sold filings without a size; the firm's $5.75B for Fund VII is in the basis. Stages Seed, Series A,
Growth (the firm's words, reconciled); geography US, then Europe, Canada, India, Southeast Asia (derived);
scope Generalist across six sectors of 12 or more companies (derived). Range $9M to $750M around a $100M
median entry round (a round-size proxy from 102 members' notes, not ICONIQ's cheque). Notables OpenAI,
Airbnb, Uber, Robinhood, Canva. Individuals 15, every title from a dated first-party record
(`sources/site/team-curated.json`; the site has no team page). Icon: the site's 256px webclip (the
wordmark on its own off-white plate), contrast 7.6:1, ramp 1.72px; uploads at ingest.

## 9. Open rulings for Erik

1. **GoFundMe (R1).** Out as a control position, but ICONIQ held a minority inside the investor group
   that took control in June 2015. The rule's words ("with its co-investor group") put it out; the same
   reading reaches Accel's GoFundMe row, which is live.
2. **Bought before or at the listing (T3)?** GoodRx, Bill.com, CrowdStrike and Zoom are on the growth grid,
   but no round, filing or release dates ICONIQ's entry, and the umbrella 13F carries listed shares from each
   company's listing quarter (CrowdStrike also call options). Kept as members with the entry uncited; your
   T3 ruling (no round named and partnered after the IPO) cannot be established either way.
3. **X6, co-invest money.** Six rows rest on a growth co-invest series alone (section 3). Kept and flagged
   `boundary`; they flip as a class if co-invest series are ruled client money.
4. **Red Ventures** reads below $1B: no round with a published valuation exists (Silver Lake's 2015
   investment and ICONIQ's 2018 co-invest carry no price), and aggregator figures cannot band it (Rule A).
   A known understatement.
5. **Unresolved co-invest codes** with large gross assets (KC, BD, ES, N, PR and others, 96 in all) are
   corroboration only; none has been tied to a company outside the base. If one is, it is a recall lead.
6. **Siblings to align at the wave pass** (the accepted pairs in `companies/cross-rulings.json`): a16z
   (Airbnb cap, Backstory = People.ai, which a16z should also check for a double count, Rillet, Robinhood),
   Accel (Miro at Bending Spoons' price, Monte Carlo), Battery (HeadSpin acquired, Reify Health),
   EQT Ventures and Felicis (HeadSpin acquired), Greylock (Airbnb), Lightspeed (K2 Space, Panther acquired,
   Rain), Lux (Aurora Solar), Menlo (Drata), 8VC and Insight (Quince at $10.1B), Sequoia (Airbnb, Houzz's
   2017 band, Rillet, Robinhood), Thrive (Robinhood), First Round (K2 Space, Omni, Rillet), Redpoint (Omni),
   Creandum (Rillet), Y Combinator (Airbnb).

## 10. Rebuilds and deltas

The one scheduled rebuild after the recall probe (172 rows: 27 out, three renamed companies merged:
Nintex's grid panel into Skuid, Intercom into Fin, People.ai into Backstory). It hit the known re-key
defect: BlackLine's and Truckstop's control verdicts moved onto the 2022 per-company pages' variants, and
the TME variant came back because its canonical row was excluded. The verdicts were restored on both
slugs and TME was ruled out (R2), then a second rebuild for that delta (169 rows, 30 excluded, no rename).
Both builds were diffed against snapshots. Ten identity merges hold; the Tencent Music group is skipped by
design (its canonical row is out).

## 11. Playbook write-backs proposed (not applied mid-wave)

1. **The re-key defect has a second face**: when a canonical row is excluded, its name variants (per-company
   archive pages) survive as rows and the rename step moves the canonical's verdict onto them. Proposed:
   exclude by fingerprint as well as by slug, or merge variants before the verification-ledger exclusion.
2. **Registration-statement exhibits** (investors' rights agreements, lock-up lists) as an entry-evidence
   layer for listed members: they name the growth funds where no release does.
3. **A share-class check for T3**: when pre-IPO holders were reclassified into an unlisted class, a
   listed-class 13F line in the listing quarter points to a purchase at the listing.
4. **`emit.py`'s `cf` and `hcc` keys** (clear settled work flags; carry a rule-6 country citation) for the
   shared judge tooling.

## 12. Usage line

Kickoff (2026-09-29 00:32 UTC): weekly all models 23%, Fable 6%, five-hour 2%. Close (about 14:15 UTC):
weekly all models 53%, Fable 6%, five-hour 4% (the weekly figure includes the GV, Tiger Global and Ribbit
sessions that ran alongside). Web searches: about 170 of the 200 cap, subagents included (pass B 34,
entry citations 40, momentum 20, the blind judges about 26, this session's about 48). Base rows 169.

## 13. Prompt count

**1** so far: the kickoff ("please collect ICONIQ"). The session paused once on the usage limit and was
resumed with "continue". Corrections from Erik: none.

## 14. Ingest (run 2026-09-29, on Erik's approval)

Erik's word: "ingest", on the closing message that offered the sibling alignment with it.

1. **Databricks, ICONIQ's own row, corrected first**: the comparison of every shared row (figure and
   as-of, not only status and band) showed the ICONIQ row carrying the $134B of February 2026 under an
   August date; the round Coatue led closed on 2026-08-13 at $190B (CNBC), as the Coatue, Lightspeed and
   Thrive rows read. Verify clean after.
2. **Icon**: `fetch-investor-icon.ts` uploaded `investors/iconiq-growth-c894a87fa8.png` (256px master, the
   wordmark on its own off-white plate, contrast 7.6:1, ramp 1.72px).
3. **Investor row**: `ingest-investor.ts iconiq-growth` upserted 1 row ("Canada" added as a new
   geography label, as four other books already use it).
4. **Companies**: the dry run planned 169 new, 0 removed, from 0 live; the write upserted 169/169 and the
   count check closed at 169. Readback of every column the ingest writes: 169 rows, 0 differing cells.
5. **Siblings aligned** (`scratch/align/align.py`, who `agent-align-pro168`): 61 rows in 21 books took the
   ICONIQ row's cited value. Status: HeadSpin acquired (Battery, EQT Ventures, Felicis), Panther acquired
   (Lightspeed). Band: Airbnb to $92.8B (a16z, Greylock, Sequoia, Y Combinator), Robinhood to $104.7B
   (a16z, Sequoia, Thrive), Aurora Solar $4B (Lux), Drata $2B (Menlo), Houzz $4B (Sequoia), K2 Space $6.8B
   (First Round, Lightspeed, Redpoint), Miro $1.79B at Bending Spoons' price (Accel), Monte Carlo $1.6B
   (Accel), Omni $1.5B (First Round, Redpoint), Quince $10.1B (8VC, Insight), Rain $1.95B (Lightspeed),
   Reify Health $4.8B (Battery), Rillet $1B (a16z, Creandum, First Round, Sequoia). Figure, same band: Ajaib
   $1.3B (IVP, Ribbit, Y Combinator), Anthropic $965B (Greylock, Lightspeed, Menlo), Automattic $7.5B
   (General Catalyst, Insight), ezCater $1.6B and FloQast $1.6B (Insight; FloQast also Redpoint), Hightouch
   $2.75B (Y Combinator), Legora $5.55B, Stripe $159B, Whatnot $20B and Wealthsimple $7.15B (Redpoint; Whatnot
   also a16z, Wealthsimple also Greylock), Ramp $44B (General Catalyst, Greylock, Khosla, Lux, Redpoint),
   Anduril $61B (Lux), OpenAI $852B (Greylock), Komodo Health $3.3B replacing an aggregator's $3.71B (a16z).
   Each book's CSV changed by exactly its rows (`csvdiff.py`); the database read back equal to the
   committed CSV except those cells before the write; each dry run planned 0 new and 0 removed; every book
   read back with 0 differing cells after. Y Combinator's readback shows one name that differs only by a
   leading space (" Metadata"), a readback-script artefact the ingest's own plan does not see.
6. **Not aligned, listed for their owners**: a16z carries both People.ai and Backstory (the same company
   after the April 2026 rename: a double count that needs an identity merge at a16z's next rebuild);
   Founders Fund (in flight), GV (collected, not ingested) and Tiger Global (in flight) were not touched;
   figure-less below-$1B rows (Pinecone, Braintrust) and as-of-only differences (a public cap read on
   another date, Axonius's and Guild's dates in Accel, General Catalyst and Redpoint) were left as they are.
