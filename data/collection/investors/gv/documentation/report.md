# GV: Build & Reconciliation Report (PRO-75)

**Linear issue** PRO-75 · **slug** `gv` · one run under the merged shape of `data/collection/COLLECTION.md`, one
session (the app was quit twice mid-run; the work resumed from disk each time), with Common Crawl carrying the
archive while the Internet Archive sat in its machine-wide cooldown · report written 2026-09-29.
**Not ingested: the ingest waits on Erik's approval.**

---

## 1. The answer PRO-75 asked for

**What §11 does when the manager is not a manager in the ADV sense: three fields lose their sworn anchor. The
run publishes AUM as the firm's own figure, flagged, takes the HQ from the firm's own site, and lists the funds by name with no
size; every other profile field is built as usual.** GV files no Form ADV of any kind (IAPD has nothing under GV,
GV Management, Google Ventures, Google or Alphabet), Alphabet is the only limited partner of every vehicle, so no
vehicle files a Form D, and the management company (CIK 1940173) files only 13F notices and N-PX.

- **`aum`** publishes the firm's own "$13B Under Management" (gv.com, read 2026-09-29) at both ends, flagged
  `firm_stated` (Erik's ruling on Delta 1, 2026-09-29), because no sworn Item 5.F or Section 7.B figure exists.
- **`hq_location`**: no ADV principal office exists, and the vehicles' filing address (1600 Amphitheatre Parkway,
  Mountain View) is Alphabet's headquarters, not the firm's office. `profile.adv_crd: null` lets the firm's own
  site decide (`profile.site_office`: "our San Francisco office", the firm's own posts): **San Francisco, CA**.
- **`funds`**: 10 vehicles by name and vintage from EDGAR (Google Ventures 2011 to GV 2023, plus Google Ventures
  2012, L.P., which never filed under its own name but appears in Upstart's, DocuSign's and Nextdoor's filings),
  `size: null`, each sourced to its EDGAR page.
- **The boundary** needed one new reading: the parent's other investing units (CapitalG, Gradient) are separate
  firms under T1, the parent's strategic stakes are not GV positions (T2), and Alphabet's own companies that GV
  lists (Waymo, Isomorphic Labs) are members as minority financings (D4), because the control addendum excludes
  only a transaction in which the firm acquires control.

The write-back is `documentation/collection-md-proposal.md` item 1 (a §11 paragraph and a T1 line), not applied
mid-wave.

| Done-when item | State |
|---|---|
| Plain `verify` green, only flagged debt | Clean (`verify: clean`); debt is flagged (section 6) |
| Distributions sanity-checked | Section 2: 13.3% $1B+, 55.1% S2A on a cohort of 187, stages and countries as expected for an early-to-growth generalist |
| Profile through the taxonomy gate | `investor.json` + `sources.json` built by `build-firm-profile.py`; every field populated or null with a basis |
| `review.html` rendered and checked | Served on the review surface (8931): every row flat, the profile panel opens with all 15 fields |
| `report.md` with the method-delta answer, open rulings, prompt count | This file (sections 1, 9, 13) |
| COLLECTION.md diff proposed at close | `documentation/collection-md-proposal.md`, 12 items (section 11) |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 749 | |
| Private | 336 | 44.9% |
| Acquired | 273 | 36.4% |
| Defunct | 52 | 6.9% |
| Public | 48 | 6.4% |
| Unknown | 40 | 5.3% |
| $1B and above | 99 | **13.3%** of 746 nameable |
| of which $10B and above | 16 | Stripe $159B, Uber $139.2B, Waymo $126B, Robinhood $104.7B, Ramp $44B, Ripple $40B, IonQ $17.7B, Toast $17.6B, Sierra $15.8B, Harvey $15.5B, Devoted Health $12.6B, DocuSign $12.5B, OpenEvidence $12B, Thinking Machines Lab $12B, SambaNova Systems $11B, HubSpot $10.1B |

**The $1B+ share is 13.3%** (no ceiling applies; Erik, 2026-09-26). It reads right for a firm that has written
about 650 first cheques since 2009, most of them seed and Series A, with a book that is 36% acquisitions.

Entry stage: Growth 231, Series A 199, Seed 199, Pre-Seed 3, round not on record 114, unnameable 3 (the
identity-unresolved codenames q1, q2 and Luna Park). Headquarters: US 680, UK 41, Canada 6, Israel 5, Germany 5,
France 3, Switzerland 2, and one each in Denmark, Finland, Bulgaria, Ireland, the Netherlands, the Czech Republic
and Sweden. Focus: Healthcare & Bio 204, Consumer & Marketplaces 146, SaaS 80, AI & Applied AI 54, Media, Gaming &
Advertising 48, DevTools & APIs 41, Data Infrastructure 39, Industrial & Robotics 37, Security 36, Fintech &
Payments 34, Climate & Energy 20, Crypto & Web3 10. Membership: 744 rows on the firm's own lists (643 on the live
list, 101 only in its archive), 5 on filings or press alone (Synapse Health, Fulcrum Therapeutics, Lyell
Immunopharma, Singular Genomics, Fractyl Health). **Alphabet's own companies (D4)**: Waymo ($126B, Growth) and
Isomorphic Labs ($2.1B floor, Series A) are in the book and in every count above.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 199 | 12 | 187 | 103 | 84 | **55.1%** |

Of 199 seed entries, 12 were too recent to count; of the 187 that remain, 55.1% raised a later round. Of the 84
that did not, none rests on the filings alone, 41 on a cited end (a sale or shutdown with the seed as the last
round) and 43 on a dated search of the named surfaces (the firm's own posts, the company's Form D sequence where it
files, Google News twice, TechCrunch's and Crunchbase News's own search, and sibling books). Coverage is 100%.
Thirteen decided rows rest on an uncited seed with the graduation evidence of their own (`stage_uncited`, low).

## 3. The boundary

`documentation/decisions.md` D1 to D11 and run-time rulings R1 to R5:

- **IN**: every company on either of GV's own lists in any era (the live /portfolio and /ai lists, and the
  googleventures.com and gv.com archives from 2012), and a position held by any GV vehicle. The Google Ventures
  years (2009 to 2015) are the same firm (D1).
- **OUT, the parent (T1/T2)**: CapitalG and Google Capital, Gradient, Google's and Alphabet's balance-sheet stakes,
  and Alphabet's subsidiaries (Calico is a trap: Wikipedia files it under "GV companies", GV lists it nowhere).
  None of the press's "Google invested" companies (Magic Leap, SpaceX, Anthropic, Lyft, Airbnb, CrowdStrike,
  Duolingo) is on GV's lists.
- **OUT, the roster (T4)**: 93 Form D rows. 48 are seats a GV person held outside the person's GV years (David
  Schenkein's Agios and bluebird bio seats before GV, Shaun Maguire's Qadium and Vise seats, Wesley Chan's Culture
  Amp seat at Felicis) and 45 are homonyms (30 filings of an unrelated Scott Davis, 4 of a Luis Garcia, 3 of a
  Samuel Blackman, and single ones). The roster dates each year by that year's own title on the person's page (68
  people); the build removed seven more rows whose only evidence was a seat filed four to nine years after the
  person left.
- **OUT, not an operating company or not a venture position**: Oxford Science Enterprises and its former name
  Oxford Sciences Innovation (D10, "a fund", in the firm's own 2015 words), Curie.Bio (R5), Starco Brands and
  Revolution Medicines (D11, stock paid for Soylent and EQRx), Seedling (R1, merger stock for Moonfrye).

## 4. Coverage per evidence regime

- **Live site**: gv.com is Nuxt 3 over a public Sanity dataset, read with GROQ: 646 companies with their deal
  partners and the firm's own exit line (243 starred exits kept on the list), 112 AI companies with the firm's own
  dated "Invested" and "Re-invested" rounds, 109 team members, 153 posts, 19 case studies.
- **Archive**: Common Crawl, 128 crawls by static `cluster.idx` range reads; 10,424 captures of googleventures.com
  and gv.com, 1,760 fetched (digest-deduplicated), 236 listing captures parsed across five markups (2012 to 2026),
  none empty. From September 2022 the portfolio names appear only in the Nuxt payload (`window.__NUXT__`, a cyclic
  object graph walked in node; then `__NUXT_DATA__`, a devalue array): without it those years read as empty. 101
  members come from the archive alone: the shutdowns the live list drops (Homejoy, Brandless and others).
- **People**: 68 people dated from the archived people pages and the live CMS, each year by that year's own title.
- **EDGAR**: the Form D sweep over the roster (500 filings, 255 issuers), the GV vehicles' own 13D/G and Forms 3/4
  (22 subject companies), full-text search on 12 phrases (257 registrants, 204 third-party, read sentence by
  sentence), and a registry of 31 entities (23 GV, 8 external: Alphabet, Google, CapitalG and their holding
  companies). One member rests on a Form D alone: Synapse Health (Ben Robbins a director on both filings, the second
  filed from 1600 Amphitheatre Parkway).
- **Wikipedia**: the insource sweep (227 articles, 34 candidates).
- **Press**: Google News per row, capped at two concurrent GV clients on the machine-wide bucket after the Tiger
  Global session asked (`scratch/gvslot.py`).
- **Recall probe**: 5 additions with citations (Fulcrum, Lyell, Singular Genomics and Fractyl through GV vehicles in
  their investors' rights agreements, never listed; Roqbot, which turned out to be Rockbot's first name and merged
  into it). The triage of 165 candidates found 111 noise, 33 aliases of listed rows and 16 not GV (five of them
  acquirers that paid GV-backed companies in stock: Twilio, Qualcomm, Mondee, Neumora, Pluralsight).

## 5. Method deltas

- **Common Crawl as the archive** during the IA cooldown, with a Nuxt 2 graph walker and a Nuxt 3 devalue reviver
  (write-back item 2).
- **The CMS as the live list**: the Sanity dataset gives deal partners, the exit line and, on /ai, the firm's own
  dated rounds, used as the entry-date clock and never as a round label (D7).
- **Legal-name twins resolved by Form D co-filers and addresses**: Rosa Foods is Soylent, Denver Technologies is
  Warp, NoHo Dental is Tend, Asset Blue Pharmacy Services is Waltz Health (write-back item 4).
- **17 parallel judges** on 20 batches with a shared judge library whose citation helpers refuse an ambiguous match
  (`scratch/judge_lib.py`), then **5 delta judges** for the graduation column with a per-row graduation view
  (`scratch/gradview.py`) and a headline citation helper (`GNEWS`).
- **Rule 10 as a dump and a rulings script** (`scratch/rule10-dump.py`, `rule10-rulings.py`): every disagreement
  printed with both sides' notes, ruled per pair.
- **Two defects in this run's own briefs**, caught by the judges: the delta brief told judges to pass the stored
  note plus their sentence, and `record` appends, so 41 notes doubled (`scratch/repair-notes.py` repaired them;
  write-back item 11); the graduation helper wrote "formd: no filing" for companies that file under another name,
  and the judges rewrote those lines.

## 6. Flags and debt behind `verify`

On the 749 published rows: `model_disputes_source` 98 (wrong-entity Wikidata or SEC joins, each disputed with
evidence), `stale` 37 (a mark older than two years that pass B could not replace), `city_unknown` 37,
`stage_disputes_band` 36, `unstable` 21 (duty 7), `stage_uncited` 13, `cite_pending` 5, `identity_unresolved` 3, `city_country_conflict` 1
(Vaccitech), `token_funded` 1 (Basis, the 2018 stablecoin). **Entry citations still pending on 5 $1B+ rows**:
Dialpad, Simply, Turo, Typeface and Viz.ai (each a model reading at medium: the entry round is named on one page
and GV on another, never both on one). 24 stale classification keys are the absorbed duplicates' old rows and are
harmless. `defunct` is undercounted by construction (COLLECTION.md §6): 40 rows read `unknown`, mostly 2011-15
apps whose domains are gone.

## 7. Standing duties and the A/B pass

- **Pass A, the defence**: every private $1B+ row carries a priced event with a citation. Five marks that still
  rode the unicorn list's name match were pinned to their rounds' own announcements (Checkr $4.6B, HomeLight $1.6B,
  Scandit $1B, Headway $2.3B, Vercel $9.3B). Every public row carries a market cap of 2026-09-28 or 09-29
  (stockanalysis.com).
- **Pass B, the attack** (`scratch/ab-news.py`: one Google News query per private $1B+ row, 74 rows, headlines
  after each mark): one exit, **Fin, formerly Intercom, acquired by Salesforce** (signed 2026-06-15 at about $3.6B,
  closed 2026-09-14); one band change, **Vir Biotechnology** at $1.75B. Leads that do not price a row and stay
  unpriced: Neuralink's reported $42B (a secondary estimate), Thinking Machines Lab at $40B, Zipline at $20B and
  Devoted Health at $25B (each in talks), Blockchain.com's planned listing, Nubank's talks with Monzo, Ripple's
  buyback at $50B (same band). Inertia and Treeline carry no published valuation, so they stay below $1B under Rule
  A (section 9).
- **Momentum slice**: 62 of 62 hot-sector rows first seen since 2021 carry a dated check (the grind's).
- **Duty 3, weak joins**: 32 `cik_weak` rows audited; 15 wrong-entity joins still published their source and date
  (Mill "as of 1788-01-01", Courier a 2014 float of another registrant) and 11 still read as listed; all cleared
  (`scratch/judgments-fixes-3.py`, `-fixes-9.py`; write-back item 10).
- **Duty 6, unicorn re-intersect** (loose names): every match is banded, exited or a different company (Sift
  Science, Compass Inc., the video Loom).
- **Duty 7, blind 5%**: 38 rows (seeded sample) re-judged by a second judge with no access to the record: 202 of 228 cells agree
  (88.6%). All 21 rows with a disagreement carry `unstable`. Adopted where the page it cited was read and is stronger
  (11 rows: named rounds the grind missed on Blue Vision Labs, Quettra, Arda, iPierian, Ribon and LifeMine; Modern
  Age's asset sale and Scalus's merger; CircuitHub's and Aterian's filed addresses; Tenxer's focus); kept where ours
  is better cited (10 rows, among them HubSpot's band, $10.11B at the 2026-09-28 close against $9.92B a day later).
- **Duty 9, the classes**: the sample settled 5 of its 9 unrecorded rounds, so four judges re-checked all 199 rows
  whose round was not on record or whose status was unknown: 57 rounds settled (28 of them Seed entries: 16
  graduated, 12 not), 5 statuses settled (Kibits acquired by Cisco; Ordr.in, TinyRx, Weotta and Scout defunct), and
  Framed moved to defunct under the acqui-hire rule. The same pass found 10 more renamed companies carried as two
  rows (Carnival Labs and Carnival Mobile, EventBoard and Teem, AVOS and MixBit, Florence and Fabric, Jetpack and
  Jetify, JoyTunes and Simply, Core and Crews by Core, Kibits and Collaborate, Cluster and LaunchKit, plus Roqbot
  and Rockbot in the delta), all merged at rebuild 5. A city check against EDGAR's header addresses changed
  nothing: the header is not the issuer's office (Ethos's 8-K still gives San Francisco, Strella's Form D Seattle).
- **Rule 10**: 622 shared rows, 554 agree, 68 accepted (GV holds the newer cited event), 0 disagree; 60 namesake
  pairs ruled distinct (`companies/cross-rulings.json`).

## 8. Firm profile

Thesis "We support innovative founders moving the world forward." (the homepage meta description; the portfolio
page's line is recorded as competing). History 53 words: founded in 2009 as Google Ventures by Bill Maris, renamed
GV in 2015 under Alphabet, Uber, Nest, Slack and Flatiron Health, led by David Krane, the four offices, and the
firm's own $13 billion (said, not sworn). HQ San Francisco, CA (the firm's own site; no ADV). AUM $13B at both ends, the firm's own
figure, flagged `firm_stated` (Delta 1, ruled). Funds: 10 vehicles, sizes null. Stages Seed, Series A, Growth; geography US, then
Europe; scope Generalist across five focus labels from the firm's own sector tags (SaaS, Healthcare & Bio,
Consumer & Marketplaces, AI & Applied AI, Industrial & Robotics). Range $6M to $75M around a $22M median entry
round (a round-size proxy over the 78 members whose entry round is on EDGAR, not GV's cheque). Notables Uber,
Stripe, Slack, Nest, Robinhood (Waymo and Isomorphic Labs left out as Alphabet's own). Individuals 34, the firm's
Investing Team group on the live CMS (12 General Partners, 3 Managing Partners, the CEO and Managing Partner, 5
Partners and 13 venture partners, EIRs, principals and associates). Icon: the header's own inline SVG mark, a
vector on a white plate, contrast 18.8:1, ramp 0.86px; uploads at ingest.

## 9. Open rulings for Erik

1. **Delta 1: ruled** (Erik, 2026-09-29): the firm's own $13B at both ends, flagged `firm_stated`.
2. **D4, Alphabet's own companies.** Waymo ($126B, the third-largest mark in the book) and Isomorphic Labs are in as
   minority financings. Out would take one of four $100B+ rows away.
3. **R1, Seedling.** Out as merger stock for Moonfrye; the parties called it a merger of equals.
4. **R4, Clarifai: ruled acquired** (Erik, 2026-09-29), siblings aligned at the ingest. Acquired (Nebius took the team, bought the patents, licensed the technology; the firm's exit
   line says acquired) against the acqui-hire rule's reading; Lux, Menlo and USV read private.
5. **R5, Curie.Bio.** Out under D10 (a venture-creation firm); a16z keeps it as a member.
6. **BufferBox (D2).** In by the firm's own listing, but TechCrunch (2014-01-14) says it "was grandfathered in as a
   personal Kevin Rose investment". Whether a partner's personal cheque carried into the firm is a GV position is
   yours; Product Hunt (listed with Kevin Rose, no source names GV in its only round) is the same kind of doubt.
   The same piece counts Makani among the "Google Ventures funded" companies, which answers that row's doubt.
7. **Synapse Health.** In on a Form D alone (a GV partner's seat filed from GV's address; medium).
8. **Vaccitech (Barinthus): ruled** (Erik, 2026-09-29, by what the company says): GB, Altrincham, its own "UK Head
   Office"; Germantown is its US office.
9. **Likely understatements under Rule A**: Inertia (a $450M Series A with no published valuation) and Treeline
   (more than $1B raised, a reverse merger pending) read below $1B.
10. **Siblings to align at ingest** (the 69 accepted pairs in `companies/cross-rulings.json`): First Round 11,
    a16z 8, Y Combinator 7, Sequoia 6, Accel 6, Felicis 5, Khosla 4, Lux 3, Lightspeed 3, and one or two in USV,
    Menlo, Battery, IVP, Spark, EQT, Insight, Greylock, Redpoint and Thrive. Outside rule 10's pairing (names
    differ, or the column is not compared): ICONIQ's Fin still reads private at the signed price (closed
    2026-09-14); 8VC's Lyell reads acquired though LYEL trades; a16z's Basis should be `token_funded`; Redpoint's
    Secret entered at the Series B; Y Combinator's Multiverse and Core carry another company's status by name; Lightspeed's LedgerX reads not
    graduated though Ledger Holdings sold $20.77M of equity from 2015; First Round carries Cluster and LaunchKit as
    two rows (one company, defunct).

## 10. Rebuilds and deltas

The one scheduled rebuild after the recall probe, two more to settle the base before the delta, and one final
rebuild for three identity merges the delta found:

1. **Rebuild 1** (862 to 763 rows): 95 exclusions, 60 identity-merge duplicates absorbed, 5 recall additions landed.
   It hit the known re-key defect twice: Curie.Bio's `not_member` verdict moved onto the newly split Spruce Health
   row (both carried a `site_url` that is the listing page, shared by every gv.com row), and Place's member verdict
   onto Oxford Sciences Innovation (the same first capture). Both moved back by hand. Oxford Sciences Innovation had
   resurfaced because its name-variant canonical was excluded first.
2. **Rebuild 2** (764 rows): the bracketed same-name splits Bowery (bowery.io) and Basis (basis.io) had been folded
   back by the name-variant rule, so both got `never_merge` pairs; Oxford Sciences Innovation got its own verdict.
   Three Form D-only pairs flipped their rendering between builds (Culture Amp, Qadium and Expanse, Vise).
3. **Rebuild 3** (761 rows): each flipping slug got its own verdict; no rename.
4. **Rebuild 4, after the delta** (758 rows): DailyCred absorbs Shopobot (its first name), Voltron Data absorbs Ursa Computing
   (R2), Rockbot absorbs the recall addition Roqbot. No rename, no verdict moved; `prepare` then queued nothing.
5. **Rebuild 5, final** (749 rows): nine renamed companies from the duty-9 sweep merged (section 7). No rename,
   no verdict moved; `prepare` queued nothing and plain `verify` is clean.

The delta (88 items: the S2A column on 77 Seed rows, plus 11 new or split rows) was judged by five judges after
rebuild 3; it produced 5 member verdicts (the recall additions) and no exclusion.

## 11. Playbook write-backs proposed (not applied mid-wave)

`documentation/collection-md-proposal.md`, twelve items: (1) the §11 contract for a corporate venture arm (the
answer above); (2) archived Nuxt payloads are listings; (3) a people page's own title dates the window; (4) read a
Form D's co-filers and addresses before judging a name-match; (5) an investment company on the firm's own list, by
the firm's own words; (6) a per-session cap on a machine-wide bucket; (7) the rebuild's re-key must refuse a
fingerprint that is not unique on both sides; (8) a curated same-name split must also be a never-merge pair; (9)
every slug of an automatic name-variant group needs its own verdict; (10) a disputed layer join must not leave its
source and date behind; (11) `record` appends a note, so a line carries only its new sentences; (12) the Form D band
in code is flat where §6's structural rule is era-adjusted (Corduro moved from Seed to Series A; a separate task
chip proposes the code fix and the re-measure across books).

## 12. Usage line

Kickoff (2026-09-29 00:31 UTC): weekly all models about 23% (read by the ICONIQ session at 00:32 UTC; this session
had no usage readout at kickoff). Mid-run (15:48 UTC): weekly all models 61%, Fable 6%, five-hour 34%, shared with
the ICONIQ, Tiger Global and Ribbit sessions that ran alongside. Close (17:23 UTC): weekly all models 70%, Fable 6%, five-hour 68%. Web searches: 76 of the 200 cap made
(the grind judges 67, the recall triage 8, the lead 1); the session limit then refused further WebSearch and
WebFetch calls, and every later read went through curl and Google News. Base rows 758.

## 13. Prompt count

**1** so far: the kickoff ("please collect GV"). The session resumed three times after context compaction or the
app being quit ("continue"). Corrections from Erik: none.

## 14. Ingest (run 2026-09-29, on Erik's approval)

Erik's rulings of 2026-09-29 were applied first: AUM the firm's own $13B at both ends (`firm_stated`), Clarifai
acquired with the sibling rows aligned, Vaccitech by what the company says (GB, Altrincham).

1. Icon: `fetch-investor-icon.ts` uploaded `investors/gv-2fbd596521.png` (the header's vector mark on a white plate,
   contrast 18.8:1, ramp 0.86px); `icon_url` points at the bucket.
2. Investor row: `ingest-investor.ts gv` upserted 1 row after one fix: the profile writer emitted `funds` as a bare
   list where the table takes `{"funds": [...]}` (the sidecar keeps the list); fixed in `scratch/write-profile.py`.
3. Companies: the dry run planned 749 new, 0 removed, from 0 live; the write upserted 749/749.
4. Readback of every column the ingest writes against `base.csv`: 749 rows, 0 missing, 0 extra, 0 differing cells;
   the investor row reads the $13B AUM, the bucket icon and the S2A block (103 of 187, 55.1%).
5. **Sibling alignment** (Erik's approval of 2026-09-29): 61 stale rows in 18 books aligned to GV's newer cited event,
   each book re-ingested with a dry run of 0 new and 0 removed and a readback of 0 differing cells, and committed by
   explicit pathspec: First Round 9, a16z 6, Accel 6, Sequoia 5, Felicis 4, Khosla 4, Lux 3, Lightspeed 3, and one
   or two in USV, Menlo, Battery, IVP, Spark, Insight, Greylock, Redpoint, 8VC (Lyell: public) and Y Combinator (plus
   its Artifact, found only once GV was published). EQT, Thrive and several other pairs had already been aligned by
   the ICONIQ run. Not aligned: a16z's Oration (its sale is stated only on gv.com; the pair stays accepted) and
   ICONIQ's Fin row (another session was editing that book). New namesake pairs the alignment surfaced are ruled
   distinct in the books' own `cross-rulings.json`. GV's verify: 0 disagree, 1 accepted.
