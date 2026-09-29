# TCV: Build & Reconciliation Report (PRO-169)

**Linear issue** PRO-169 · **slug** `tcv` · one run under the merged shape of `data/collection/COLLECTION.md`,
one session, self-ingesting through the §9 gate (commit 449e2085) · report written 2026-09-29.
Common Crawl carried the archive; the Internet Archive's pre-2013 leg was not collected (section 4).

---

## 1. The answer PRO-169 asked for

**The base is 296 companies, plain `verify` is clean, and the firm profile is built.** TCV is one adviser,
TCMI, Inc. (CRD 160389, $22.5B of regulatory assets across 34 private funds), with no strategy desk to
partition. Its own compliance page lists every investment, 338 legal names as of 2026-07-15, and labels
each featured deal `minority`, `majority` or `public`; those two facts decide most of the boundary. Out:
**24 control positions** (the firm's `majority` label, which it defines as TCV alone or with a consortium
at 50% or more), **20 listed purchases** (the `public` label, two PIPEs, and positions bought at or after a
listing), 255 Form D rows that matched a TCV person's name on a company the complete list never carries,
6 further namesake or pre-list filings, 3 fund-shaped or incubator lines, and Teya (sale consideration).

| Done-when item | State |
|---|---|
| Plain `verify` green, only flagged debt | Clean (`verify: clean`); debt is flagged (section 6) |
| control_position rows counted | 24, listed in section 3 |
| Profile through the taxonomy gate | `investor.json` + `sources.json` built by `build-firm-profile.py`; `profile_copy.py` ok |
| `review.html` rendered and checked | Served on the review surface: 296/296 rows flat, profile panel expands with every field and basis |
| Cross-investor (rule 10) | 221 shared rows: 209 agree, 9 accepted (stale siblings, aligned at ingest), 0 disagree; 8 namesake pairs ruled distinct |
| Report, close, commit, ingest, Linear, closing message | This report; section 14 records the ingest |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 296 | |
| Acquired | 154 | 52% |
| Private | 78 | 26% |
| Public | 27 | 9% |
| Defunct | 24 | 8% |
| Unknown | 13 | 4% (dot-com rows with no traceable end, plus Adknowledge, Origin, MoneyExpert) |
| $1B and above | 59 | **19.9%** |
| of which $10B and above | 14 | Facebook $1.83T, Anthropic $965B, ByteDance $330B, Netflix $292.8B, Revolut $115B, Spotify $101.4B, Airbnb $92.5B, Nubank $59.1B, Fireworks AI $17.5B, Toast $17.4B, Trade Republic $14.5B, Celonis $13B, ICEYE $12B, Instacart $10B |

**The $1B+ share is 19.9%, with no ceiling** (Erik, 2026-09-26). It reads right for this book: 30 years of
growth investing, more than half of it the 1996-2012 book (acquired or failed dot-com and telecom
companies at below $1B by convention), with the recent book (2018 onward) carrying most of the $1B+ rows.

Entry stage: Growth 132, Series A 6 (Avalor, Legit Security, Nagomi Security, Nourish, tastytrade, Zillow),
round not on record 158 (mostly the 1996-2012 book, whose listings carry names only). Headquarters: US 244,
Canada 8, UK 6, France 5, Germany 5, Israel 4, India 3, Australia 3, the Netherlands 3, and 15 more across
eleven countries. Focus: SaaS 73, Consumer & Marketplaces 60, Fintech & Payments 42, Data Infrastructure 36,
Media, Gaming & Advertising 29, Security 16, Healthcare & Bio 11, AI & Applied AI 9, DevTools & APIs 6,
Industrial & Robotics 4, outside the taxonomy 10. Membership rests on the firm's own list or grid for all
296 rows.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | none (empty cohort) |

TCV enters at Series A or later (delta X3); no row is a Seed entry, so no S2A rate publishes for this book.

## 3. The boundary

- **One adviser (D1, D2).** Every vehicle is advised by TCMI, Inc.; the ADV's 34 private funds sum to its
  Item 5.F regulatory assets exactly. TCV Trust & Wealth, the TCVI Group, the TCV Franchise Fund and the
  access feeders are external (config `desks.external`).
- **Single-deal vehicles are in (D3).** TCV Sports (Sportradar), NB Co (Nubank), Bus Co (Flix), Tru Co
  (Trulioo), Dev Co (Devo), Guardian and the 2024-2026 Beat, Juniper, Owl, Cedar and Flare vehicles; every
  one filed before the 2026-07-15 list, so the company each holds is on that list and already in the base.
- **Control positions, out (D6, X2; 24):** Adevinta, Avetta, Desert Newco (GoDaddy's buyout vehicle),
  EmbaNet-Compass, ETQ, Genesys, Global 360, GoDaddy, GoFundMe, IQMS, Kipu, Mutant, Nasuni, Orbitz
  Worldwide, Oversight Systems, R.J. O'Brien, Rave Mobile Safety, Retail Merchant Services, RiskMetrics,
  Seismic Micro-Technology, Solarc, Travelport, Watermark, Webroot Software.
- **Listed purchases, out (D6, X1; 20):** Electronic Arts, Envestnet, Expedia, GoodRx, Interactive Brokers,
  K12, LinkedIn, MarketAxess, Mattersight (eLoyalty PIPE), OpenText, Redback Networks, Rocket Companies,
  Talend, TheStreet (two renderings), TripAdvisor, Twilio, Xero, XRS (XATA PIPE, two renderings).
- **The complete list as absence evidence (D9):** 255 Form D name-matches out, plus ViaVia (R1), PSW
  Technologies (a TCV I to III public buy) and four common-name namesakes.
- **Fund-shaped and incubator lines (D8, R7):** Eladian Partners LP, Foundries Holdings, and a 2026
  aggregator vehicle naming Greg Greeley. **Sale consideration:** Teya (R10).
- **Kept on the transaction's facts:** Sportradar (a 35% stake with CPPIB, the founder keeping his whole
  position; R2, flagged `boundary`) and CCC Intelligent Solutions (8.9% bought apart from Advent's buyout).

## 4. Coverage per evidence regime

| Surface | What it gave |
|---|---|
| The compliance list, live (2026-07-15) and archived 2017-2026 | 338 legal names, complete by the firm's own statement; the membership spine and the rename detector |
| The partnerships grid (live, 155) and the 2018-2023 `/companies/` grid | Deal types (`minority` / `majority` / `public`), deal teams, sectors |
| Common Crawl, 2008-2026 (ARC crawls 2008-2012 plus WARC) | The 2008-2013 portfolio pages (`index.php4`, `all-portfolio.php4`), 2013-2016 WordPress list, team pages, 459 news posts |
| Internet Archive, pre-2008 pages | **Not collected.** A machine-wide IA cooldown (another session hit the firewall at 21:03 UTC, four hours) held the leg; it was stopped rather than waited out, because the complete list means those pages could add descriptions, not members. The 36 legacy rows they would have described were judged from EDGAR full-text search and period press instead (5 from filings by this session, 31 by a research pass). |
| EDGAR | Form D sweep and the firm's own fund filings, 13F (79 issuers), full-text search (518 registrants), Forms 3/4 and 13D; S-1 holder tables for entry rounds |
| Form ADV (CRD 160389, 2026-03-27) | AUM floor, fund roster, principal office |
| Google News and targeted web search | Pass B, the momentum slice, marks and entry rounds |

## 5. Method deltas

- **X1 (listed purchases):** applied through the firm's own `public` label; the two PIPEs (eLoyalty 2001,
  XATA 2009) are out as listed purchases, flagged for Erik.
- **X2 (control positions):** applied through the firm's own `majority` label, whose definition includes
  consortium control; extended to Mutant, a stake carried out of the Genesys buyout (R9).
- **X3 (no new stage):** held; the Seed cohort is empty.
- **X4 (non-US share):** ECB conversion for the PLN (Grupa Pracuj) and AUD (SiteMinder) caps; rule-6
  citations on every non-US $1B+ or public row.
- **New in this run:** an asset sale out of a failure reads `defunct`, a business that carried on under a
  buyer reads `acquired` (CoreExpress, Clareon, Constellar, Emerald Solutions and OurHouse defunct;
  ZoneTrader, Achieva and CopperCom acquired). The 12 run-time rulings are in `decisions.md` (R1 to R12).

## 6. Flags and debt behind `verify`

`stale` 42 (21 private marks older than 24 months, every one attacked in pass B with no newer priced event
found: Ankorstore, Attentive, Aviatrix, Built, Capsule, Celonis, Devo, Employment Hero, Flix, Klook, Mambu,
Mollie, Newsela, OneTrust, Qonto, Razorpay, Redis, RELEX, Trulioo, Vectra AI, Zepz; the rest old public or
exit marks); `unicorn_name_match` 21 (each confirmed as the same company); `model_disputes_source` 12;
`cik_weak` 12 (audited: every join is the right company, no wrong-entity float); `stage_disputes_band` 9;
`unstable` 6 (duty 7); **`stage_uncited` 6** (eHarmony, Green Dot, HashiCorp, HomeAway, SeatGeek, Splunk:
model Growth readings at medium, the round named nowhere readable); `needs_review` 2 (Darwinbox's $1.0B
floor, Dream Sports under R3); `city_unknown` 2 (NewlineNoosh, ZoneTrader); `entry_anchor_weak` 1 (Open
English); `boundary` 1 (Sportradar). `cite_pending`: 0.

## 7. Standing duties and the A/B pass

- **Duty 1 ($1B+ claims):** all 59 $1B+ rows carry a web-verified figure; public caps pinned from
  StockAnalysis on 2026-09-29.
- **Pass B** found three marks the grind missed: Corgi's Series B extensions ($1.3B to $4B, FinTech Global),
  Upwind's Series C at $3.8B (SiliconANGLE; surfaced by the duty-7 judge) and Trulioo's $1.75B, which the
  row had lost. Signed but unclosed sales stay marks (Cognite to Schneider Electric, Miro to Bending Spoons).
- **Momentum slice:** 19 private rows first listed since 2021 in a hot sector, all recorded with a dated
  check (Arize AI, Cloudsmith and LayerX added; LayerX's entry corrected to the Series B TCV led).
- **Duty 3 (weak joins):** 12 audited, all correct.
- **Duties 4 and 5 (floats):** TechTarget re-read as public (the combined company is listed, Informa 57%),
  Renren read as Moatable, Rent the Runway's cap refreshed.
- **Duty 7, blind 5%:** 15 rows (seed 169) re-judged by a second judge with no access to the record: 79 of
  90 cells agree (87.8%). Adopted: GMI's city (Bellevue, WPP's release) and TechTarget's status. Kept, with
  `unstable`: Evite, Cognite (focus), 2Wire (focus), CoreExpress (defunct, aligned with Benchmark).
- **Duty 9 (a hit is a class):** the missing-country class (7 rows, all US) and the "note states $1B+ but
  the band reads below" class (Trulioo only) were swept book-wide.
- **Citation debt cleared** on the visible slice: ExlService (a 2004 secondary from the founders, exhibit
  10.24), Zillow (Series A, S-1), Klook (Series D, the firm's copy), Nourish (Series A, citybiz); Anthropic
  and Hinge Health read `undetermined` (R12).

## 8. Firm profile

TCV, Menlo Park (the ADV's principal office; the site lists Menlo Park, New York and London), founded 1995
(TCV I closed 1995-06-23). Thesis: "Partners in growth." (the homepage's title-tag tagline; the homepage has
no headline). AUM $22,506,060,259 (ADV) to $23B (the firm's own figure, as of 2026-06-30). Range $10M to
$500M (the firm's own), median $75M (62 stated entry rounds, a round-size proxy). Funds: TCV XII (size
unannounced), Velocity Fund I $460M, XI $4B, X $3B, IX $2.5B, VIII $2.23B, VII. Notables: Netflix, Facebook,
Airbnb, Spotify, ByteDance. Stage Series A and Growth; geo US core, with Europe, Canada, Israel, India,
Australia and China; scope Generalist across five sectors. 34 current investment-team members. The icon is
the inline TCV wordmark on the site's primary blue (dry run: contrast 9.2:1, ramp 0.92px, vector).

## 9. Open rulings for Erik

1. **X1, PIPEs:** eLoyalty (2001) and XATA (2009) are out as listed purchases. If a negotiated PIPE is a
   venture entry, both enter as Growth.
2. **X2 and R9, consortium control:** Mutant is out as a stake carried from the Genesys buyout (medium; the
   list gives no deal type for it); GoFundMe is out on its 2015 majority purchase despite the later
   `minority` label.
3. **R2, Sportradar:** in on the transaction's facts although the grid says `majority` from 2020.
4. **R3, Dream Sports:** below $1B on India's 2025 ban (`needs_review`); **Darwinbox:** $1.0B as a floor.
5. **The IA pre-2008 leg:** accept the gap, or re-run it when the archive recovers (descriptions only).
6. **Asset sales out of a failure read defunct** (section 5): confirm the reading, which binds the
   legacy book.
7. **Miro's country:** US (San Francisco) as ICONIQ records it; Accel's row says the Netherlands.

## 10. Rebuilds and deltas

Two rebuilds: the scheduled one after the recall probe, and a final one because the delta made four
membership verdicts. The first rebuild's rename step moved three excluded verdicts onto name variants
(XRS to its Form D rendering "XATA Corp /MN/", TheStreet.com to TheStreet, Inc., American Halal Company
to its later Form D name), the class BCV and Insight hit. The verdicts were copied back onto the original
slugs under the record lock and each variant was ruled `not_member` as the same company. Desert Newco,
LLC (GoDaddy's operating company, from its 2011 Form D) entered at the rebuild and was ruled a control
position. The final rebuild renamed nothing.

## 11. Playbook write-backs proposed (not applied; scripts and COLLECTION.md belong to the tooling session)

1. **Common Crawl's 2008-2012 ARC crawls** need ARC-record parsing in the shared fetcher (this run's
   `scratch/cc-fetch.py` reads both); they held TCV's only 2008-2013 portfolio pages.
2. **A firm's own deal-type labels are first-party boundary evidence** (§1 evidence rules): a `majority`
   label defined as consortium control is a control position, a `public` label a listed purchase, unless a
   private round before the listing is on record.
3. **Archive name canonicalisation** (legal and suffixed renderings to one company name, with a curated
   map) as a shared step before the base build; `scratch/canon-archive.py` left 0 unmatched of 5,154.
4. **`edgar-entities.py` seed queries containing spaces return nothing** (URL encoding).
5. **Build the roster before `edgar-entities.py`**, or partners are classed external.
6. **`run.py record` writes an empty `note` over the stored note**; it should keep the stored note (seven
   notes were blanked here and restored).
7. **The rebuild's re-key must copy, not move, an excluded verdict**, and `record` needs a sanctioned way
   to restore a verdict on an excluded slug (recurred here on 3 rows after BCV and Insight).
8. **Next.js RSC `T` blocks are byte-counted**, not character-counted (two parsers sliced mid-name).
9. **The momentum slice should include Security**: Upwind's $1.6B to $3.8B raise sat outside it and was
   found only by the blind judge.

## 12. Usage line

Kickoff (2026-09-29): weekly all models 71%, Fable 6%, five-hour 74%. Close (22:30 UTC, after the weekly
reset): weekly all models 10%, Fable 0%, five-hour 32%. Web searches: about 85 of the 200 cap, subagents
included (the legacy-row research 40, the blind judge 9, this session about 36). Base rows 296.

## 13. Prompt count

**2**: the kickoff ("please collect TCV") and a "go ahead" after a mid-run status message. No corrections.

## 14. Ingest

Recorded after the closing commit (below).
