# NEA: Build & Reconciliation Report (PRO-100)

**Linear issue** PRO-100 · **slug** `new-enterprise-associates` · display name **NEA** · one run under the merged
shape of `data/collection/COLLECTION.md`, one session, self-ingesting through the §9 gate · report written
2026-09-30. The Internet Archive's pre-2008 leg was not collected (section 4); Common Crawl carried the archive.

---

## 1. The answer PRO-100 asked for

**The Company Base is 1,110 companies (1,108 members and 2 uncertain), plain `verify` is clean, and the firm
profile is built.** NEA is one registered adviser (New Enterprise Associates, CRD 161004, $35.58B of regulatory
assets) investing from one numbered fund family across technology and healthcare, with a venture-growth sleeve, an
opportunity fund, single-deal SPVs, a secondaries fund (2024) and Connect Ventures I (the CAA partnership, a fund of
the same adviser). The firm's own site lists 917 companies with its first-investment year, a stage label and an exit
line; the archive adds the companies the list has dropped. Out: **74 listed purchases** (X1: PIPEs and positions
bought after a listing), **11 control positions** (17 rows: R1, R5, R6), 62 rows that were a person's seat outside
NEA or a personal check, 56 fund-shaped or incubator rows, 7 rows of sale consideration (D8) and 41 namesakes or
uncorroborated name matches.

| Done-when item | State |
|---|---|
| Plain `verify` green, only flagged debt | `verify: clean`; debt flagged (section 6) |
| control_position rows counted | 17 rows, 11 companies (section 3) |
| Profile through the taxonomy gate | `investor.json` + `sources.json` built by `build-firm-profile.py`; `profile_copy.py` ok |
| `review.html` rendered and checked | Served on the review surface: 1,110/1,110 rows flat, profile panel expands with every field and basis |
| Cross-investor (rule 10) | 541 shared rows: 516 agree, 25 accepted (sibling rows stale, aligned at ingest, section 14), 0 disagree; 49 namesake pairs ruled distinct |
| Report, close, commit, ingest, Linear, closing message | This report; `run.py close`; closing commit; ingest (section 14); PRO-100 comment |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 1,110 | |
| Acquired | 557 | 50% |
| Private | 369 | 33% |
| Public | 71 | 6% |
| Defunct | 57 | 5% |
| Unknown | 56 | 5% (mostly 1990s and 2000s rows with no traceable end) |
| $1B and above | 95 | **8.6%** |
| of which $10B and above | 22 | ByteDance $330B, Databricks $190B, Salesforce $188.7B, Uber $140.6B, Vertex Pharmaceuticals $133.6B, Cloudflare $124.5B, Robinhood $101.2B, SMIC $89.0B, Bloom Energy $82.9B, Workday $45.7B, VAST Data $30B, MongoDB $28.5B, ElevenLabs $22B, Perplexity $20B, SiTime $19.6B, IonQ $17.7B, Didi Chuxing $16.1B, Tempus $15.1B, OpenSea $13.3B, NinjaOne $12.3B, HealthSouth $12.0B, GoodLeap $12.0B |

The $1B+ share is low for a firm of NEA's standing because the book is long: 49 years, more than half of it acquired
or failed 1980s to 2000s companies below $1B by convention.

Entry stage: Growth 283, Series A 237, Seed 174, Pre-Seed 3, round not on record 411 (the old book, whose listings
carry names and years only), 2 unnameable. Headquarters: US 980, China 33, India 24, UK 17, Canada 11, Germany 6,
Switzerland 5, the Netherlands 5, Israel 4 and 25 more across 15 countries. Focus: Healthcare & Bio 342, Data
Infrastructure 137, SaaS 124, Consumer & Marketplaces 121, Industrial & Robotics 101, Media, Gaming & Advertising 61,
AI & Applied AI 57, Fintech & Payments 51, Security 42, Climate & Energy 34, DevTools & APIs 25, Crypto & Web3 12.
Membership rests on the firm's own list for 1,029 rows, an NEA fund's own filing for 45, a cited round naming NEA
for 24 and an adjudicated Form D for 12.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 174 | 13 | 161 | 102 | 59 | **63.4%** |

Coverage is 100% of the cohort. The 59 nos rest on the Form D absence (7), a cited end (9: a sale or shutdown with
the seed as the last round) and the full absence test (43: the firm's own posts, the company's Form D sequence, Google
News twice, TechCrunch and Crunchbase News, and every sibling row). Two graduations rest on an inferred Seed entry with
a cited later round (`stage_uncited`, confidence low: ThirdLove, TigerData).

## 3. The boundary

- **One adviser (D1, D2).** Every numbered fund, sleeve, SPV, the secondaries fund and Connect Ventures I are in (the
  last re-derived from NEA's own ADV Section 7.B). The China and India teams were NEA's own subsidiaries (NEA
  (Beijing) Ltd., NEA (India) Pvt. Ltd.) and are in; the IndoUS joint venture, NewView Capital, the Goldman and
  private-bank feeders, CMEA and Southwest Enterprise Associates are external (R4). Spectra Enterprise Associates,
  listed external at kickoff, re-derived IN on its own 13G (NEA's Baltimore office, NEA's partners as its GPs).
- **X1, listed purchases out (74 rows).** The firm's `Public/PIPES` label and the Growth Equity Opportunities
  vehicles' 13D issuers (R2), per row: where the record shows an NEA private round before the listing, the row stays.
  The label is wrong on several pre-1995 rows (NEA partners on the boards before the IPOs: SGI, Telebit, Vitesse, RF
  Monolithics, Cirrus Logic), so it never decides a row alone. **R7 (new):** a pre-1998 Schedule 13G filed by a
  non-institution dates the holding before the listing; GeneMedicine and Penederm are in on it, Platinum Software and
  Aquila Biopharmaceuticals stay out.
- **Control positions out (11 companies, 17 rows):** AMISYS Managed Care (1994 buyout from AIG with Greylock and ABS),
  American Pathology Partners (R6), Comprehensive Pharmacy Services, DSI Renal, Elements Behavioral Health, RevSpring
  (NEA beside Frazier's buyouts), Paladina Health and its successors Everside and Marathon Health (NEA funds bought all
  of Paladina from DaVita, 2018), Northern Power Systems (NEA Wind Acquisition, 2008), TriVascular and Xcel
  Pharmaceuticals (syndicate carve-outs, R5).
- **Sale consideration out (D8, 7 rows):** Upwork (Elance is the member), Synopsys (Logic Modeling), NetIQ,
  Spectranetics, letgo, Tempest Therapeutics (merger stock) and Visual Sciences (Avivo); Pharmos (Vela) and
  WebSideStory (Avivo) are out on D8 and X1 together.
- **Kept on the transaction's facts:** NeueHealth (NEA's 2016 Series A was a minority; its 2025 take-private by an NEA
  affiliate is the exit, acquired below $1B on the $7.33 common price), Radiology Partners and Curana Health (R6,
  flagged).
- **Uncertain, kept and flagged (2):** Future Retail (a listed Indian company, X1 likely) and ECI Acquisition Holdings
  (R1 control check open).

## 4. Coverage per evidence regime

| Surface | What it gave |
|---|---|
| The firm's Statamic CMS (GraphQL at statamic.nea.com, public) | 917 live companies with first-invested year, stage label, status, exit line, deal team and board members; 108 team rows; 427 posts and press releases |
| Common Crawl, 2008-2026 (ARC crawls 2008-2012 plus WARC) | The 2008 ColdFusion portfolio reports, the 2013 CompanyDetail.aspx pages, 1,018 company pages since 2013 (186 no longer listed), archived team pages (the 178-person roster) |
| Internet Archive, pre-2008 | **Not collected.** The machine-wide IA cooldown held through the run (one of this run's own CDX queries extended it); the leg is a spawned follow-up. It would add descriptions and names of 1990s companies the firm dropped before 2008 |
| EDGAR | 79 entities (58 own-desk CIKs), Form D sweep and issuer rounds, 226 EDGAR companies from NEA filers, full-text search (S-1 holder tables, 13D/13G), the funds' own Form Ds |
| Form ADV (CRD 161004, 2026-08-26) | AUM, fund roster (Section 7.B), offices, Connect Ventures |
| Google News, TechCrunch and Crunchbase News search, Wikipedia | Pass B, the momentum slice, marks, entry rounds, the graduation surfaces |

## 5. Method deltas

- **X1 (PIPEs out)**, the one delta, applied per row (section 3); R2 and R7 extend it.
- **The firm's stage label was scored** (D6): Seed 15/21, Growth 20/25 agree with documented rounds, so both label at
  medium; `Early` straddles Seed and Series B and never labels.
- **New in this run:** the post-rebuild delta ran the graduation pass on every open Seed row (94 decided by the
  delta judges; 1BOG, TiVo, TrackMaven and Cartiva re-staged away from Seed on a documented round or the firm's own
  year); a
  five-row X1 check on filing-only members (Netrix, Lumisys and Sequana in on pre-IPO NEA directors; GeneMedicine and
  Penederm on R7). The 11 run-time rulings are in `decisions.md` (D1 to D8, X1, R1 to R7).

## 6. Flags and debt behind `verify`

`stale` 110 (private marks older than 24 months, each attacked in pass B, and old public or exit marks);
`city_unknown` 98 (mostly 1990s rows); `stage_disputes_band` 71 (a documented round or the firm's own year overrode
the Form D band); `model_disputes_source` 64 (Wikidata countries and prefilled values disputed with evidence);
`cik_weak` 28 (audited); `cite_pending` 11 ($1B+ rows whose entry round no source names: BloomReach, ByteDance,
Chinaway Technologies, Collective Health, Didi Chuxing, Genies, MindTickle, Physical Intelligence, Splashtop,
TigerData, World Labs); `boundary` 9; `stage_uncited` 8; `duplicate` 6; `unicorn_name_match` 2; `identity_unresolved` 2;
`suspect_base` 2. People's links: 43 of 48 carry LinkedIn (90%); six were confirmed by a checked search under
Erik's 2026-09-30 ruling (`site_api.team_social_overrides`).

## 7. Standing duties and the A/B pass

- **Duty 1 ($1B+ claims):** all 95 $1B+ rows carry a web-verified figure; 71 public caps pinned from StockAnalysis on
  2026-09-30 (non-US listings converted at the ECB rate of their date). Signed but unclosed sales stay marks (World
  Labs at AMD's $8.2B, TAE Technologies at $6.0B, Uptake private despite Bosch's March 2026 signing).
- **Momentum slice:** 43 private rows first seen since 2021 in a hot sector, each with a dated check; none newly at
  $1B+. Duty 6 settled 51 unicorn-list name hits (four namesakes).
- **Rule A:** every private $1B+ mark rests on a priced round with a non-vendor citation (55/55).

## 8. Firm profile

NEA, Menlo Park (the ADV's principal office; the site lists Menlo Park, New York, London, Timonium and San
Francisco), founded 1977 by Dick Kramlich, Chuck Newhall and Frank Bonsal. Thesis: "The foundation for new
frontiers." (the homepage headline). AUM $35.58B at both ends (Item 5.F RAUM, 2026-08-26; the firm's "over $25B" of
2022 sits below it and is flagged). Range $3.4M to $500M, median $18M (the entry round over 385 members with Form D
histories, a round-size proxy; floor the p10; ceiling the fund ladder). Funds: NEA 19 (2025, unannounced), NEA
Secondary Opportunity $468.2M (2024), NEA 18 and NEA 18 Venture Growth Equity ($6.2B together, 2023), NEA 17 $3.6B,
NEA 16 $3.3B, NEA 15 $2.8B, NEA 15 Opportunity $350M, NEA 14 $2.6B, NEA 13 $2.5B. Notables: Uber, Robinhood,
Duolingo, Coursera, Databricks (Salesforce left out only for a script mismatch, write-back 6). Stage Seed, Series A,
Growth; geo US core with China, India, Europe, Canada and Israel; scope Generalist, focus recomputed from the site's
tags (Healthcare & Bio, Consumer & Marketplaces, AI & Applied AI, SaaS, Data Infrastructure). 48 current team
members. The icon is the site's vector favicon (contrast 6.0:1, ramp 0.98px), uploaded as
`investors/new-enterprise-associates-bbcae460c3.png`.

## 9. Open rulings for Erik

1. **X1, PIPEs:** 74 rows out as listed purchases. If a negotiated PIPE is a venture entry, they enter at Growth.
2. **R7, the pre-1998 13G route** as evidence of a pre-listing holding (GeneMedicine, Penederm in).
3. **R4, affiliate funds run from their own office** (CMEA, Southwest Enterprise Associates) are external; Dallas
   Semiconductor is out with them.
4. **R5, syndicate carve-outs** (TriVascular, Xcel) out as control positions.
5. **R6, NEA's own formations:** American Pathology Partners out; Radiology Partners and Curana Health in, flagged.
6. **Uncertain rows:** Future Retail (X1 likely) and ECI Acquisition Holdings (control check).
7. **Strongbridge Biopharma** (an OTC-quoted company's placement, X1 at medium) and **Premier Laser Systems** (member
   on NEA IV's 1993 notes; D8 if the notes were part of the ProClosure technology price).
8. **AMISYS across books:** Greylock's book reads it a member on the same 1994 buyout this book rules a control
   position. Membership is not a rule-10 column, so both stand until a ruling.
9. **Data Domain:** Seed on the firm's own post, although the S-1's Series A-1 (November 2001, $1.0M) is the only
   2001 round; the S-1 does not name NEA per holder, so the firm's word stands.
10. **The IA pre-2008 leg:** accept the gap or re-run it when the archive recovers (the spawned task).

## 10. Rebuilds and deltas

Three rebuilds: the scheduled one after the recall probe; a second because the delta made membership verdicts
(Viracta, Glacier Bay's split, Connetics, Aveo, Inventiva, Platinum Software, Aquila); and a third because the
second's rename step moved nine excluded verdicts onto the companies' other renderings ("Sunesis" and "Sunesis
Pharmaceuticals", AMISYS, Genocea, Erytech, TriVascular, Xcel, ExploraMed IV and V, GFI Software). The verdicts were
copied back so both renderings carry them; the third rebuild renamed nothing. The first rebuild's rename step also
moved Serious Materials' answers onto Glacier Bay, which only shares its 2008 index page (removed before prepare),
and exposed two wrong identity merges, now corrected: Cohere Networks is Gainspeed's earlier name (CIK 1556546), not
Cohere Technologies; the firm's 2017-2019 "Blend" is Genies (Blend Systems, CIK 1560253), and Blend Therapeutics
(CIK 1528747) is Tarveda. Ohai and Proof of Learn were merged (one Form D filer).

## 11. Playbook write-backs proposed (not applied; scripts and COLLECTION.md belong to the tooling session)

1. **`rekey_overlays.rename_map` pairs a merged duplicate with an unrelated arrival.** Serious Materials (merged into
   Serious Energy) was mapped to the new Glacier Bay row because both appear only on the 2008 index page. Skip old
   slugs that are duplicates of a surviving merge canonical, and require fingerprint uniqueness across old and new
   rows, not arrivals only.
2. **Excluding one rendering before the name-variant merge flips the survivor.** A not_member verdict on "Sunesis
   Pharmaceuticals" excludes that rendering first, "Sunesis" survives alone, and the re-key moves the verdict onto it,
   so the next build resurfaces the first (nine rows here). Run the exclusion after the name-variant merge, or copy
   the verdict rather than move it (TCV write-back 7).
3. **`run.py prepare` crashes on a pooled Form D cache entry** (`KeyError`, line 962): two live rows whose accessions
   both point at one retired key; the second `formd.pop` finds it gone. Pop only when present, and split a pooled
   entry by CIK.
4. **The Form D rounds cache keys by row slug and pools every CIK a name matched** ("Blend" held Blend Therapeutics
   and Blend Systems). Key the cache by CIK.
5. **The prefix name-variant rule joins different companies that share a first word** when no one snapshot carries
   both (Glacier and Glacier Bay; Blend and Blend Therapeutics). Require a shared CIK, site URL or description before
   the prefix merge.
6. **`build-firm-profile.py` checks notables against `base.json` names, `verify` against `base.csv` published names**:
   a published rename (PRO-146) of a notable fails one or the other (Salesforce.com / Salesforce). Both should read the
   published name.
7. **The firm's `Public/PIPES` label and year are unreliable before 1995** (X1 section): never exclude a pre-1995 row
   on the label alone.
8. **A pre-1998 Schedule 13G by a non-institution is evidence of a pre-listing holding** (R7), for every investor
   whose pre-1996 prospectuses predate EDGAR.
9. **ADV Section 7.B is a boundary source**: a fund of the same adviser under another brand is in (Connect Ventures).
   And the IAPD PDF text reprints earlier 7.B blocks on each page, so a 7.B parser must key on the private fund ID.
10. **A public Statamic GraphQL endpoint** gave the firm's whole CMS (companies, team, posts) without a token; worth
    a probe in `site-portfolio.py` beside the WordPress and Webflow paths.
11. **`edgar-entities.py` single-match seeding** (from the kickoff): a seed query that matches one filer only is
    treated as the firm, which let a person's own filer number in (Heliogen via Krishna Kolluri).
12. **`run.py record` note-join defect** still bites (the stage pass recorded one batch twice; 48 notes restored by
    `scratch/repair-notes.py`): keep the stored note when a line is recorded again.

## 12. Usage line

Close (2026-09-30, about 21:00 UTC): weekly all models 42%, Fable 5%, five-hour 15% (the run crossed a usage-limit
pause mid-run and resumed on "continue"). Web searches: about 159 of the 200 cap, subagents included. Base rows
1,110; excluded 259.

## 13. Prompt count

**2**: the kickoff ("please collect NEA") and "continue" after the usage-limit pause. No corrections.
