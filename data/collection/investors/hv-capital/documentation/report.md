# HV Capital: Build & Reconciliation Report (PRO-104)

**Linear issue** PRO-104 · **slug** `hv-capital` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session · report written 2026-09-29.
Ingested through the COLLECTION.md §9 gate (section 15).

---

## 1. The answer PRO-104 asked for

**The base is 266 companies, plain `verify` is clean, the firm profile is built, and the book was
ingested through the §9 gate.** HV Capital is one firm under two SEC exempt reporting advisers of
one manager (HV Capital Manager GmbH, CRD 301966; HV Capital Adviser GmbH, CRD 163955), founded in
Munich in 2000 as Holtzbrinck Ventures. The book runs from its corporate era (1999-2010, Funds I-III)
through the independent partnership (Funds IV-IX, 2010-2026).

The four PRO-104 deltas, all derived from verified facts (`decisions.md`):

- **The corporate-publisher lineage (D2).** The corporate era is IN: the same team made those
  investments, the holding companies became limited partnerships at the firm's address in December
  2010, and the firm itself claims that book as its Funds I-III. What stayed with the parent is OUT:
  Holtzbrinck Networks, Digital and eLab, and the publishing group. Flagged for Erik, as asked.
- **The rename (D3).** Both domains are configured (holtzbrinck-ventures.com for 2006-2018,
  hvcapital.com for 2020-2026) and parsed by `scratch/hv_archive.py`. Company renames are 16 merges
  in `companies/identity-merges.json`.
- **The German recipe (D9)**, including the insolvency and asset-sale convention for `status`.
- **The pre-window slice (D10).** 14 rows date from before 2006.

Out: 14 rows.

- **10 sale-consideration rows (D4, R1).** HV holds these companies' shares only because each
  bought a company HV had backed: Groupon, Rocket Internet, Care.com, Boku, Cabify, Qonto, Deel,
  Wellhub, Zopa and SumUp. The company HV backed is the member in each case.
- **4 Form D name matches (D8):** the related person on the filing shares a name with an HV partner
  but is someone else.

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean at 266 rows; flagged debt only (section 7) |
| Rename in config, merges recorded | `config.json` `wayback._eras_note`, `scratch/hv_archive.py`; 16 merges |
| Corporate-lineage boundary ruled and dated | D2 (Handelsregister conversion 2010-12-22), flagged |
| Distributions vs Cherry and Creandum | Section 2 |
| Profile through the taxonomy gate | `build-firm-profile.py` and `profile_copy.py` ok; every field populated or null, with a source |
| `review.html` rendered | Served on a local static server: 266 rows flat, profile panel expands |
| `report.md` | This file |
| Archetype-B corrections to PRO-87 | Section 12 and a PRO-87 comment |
| Ingest through the §9 gate, sibling rows aligned | Section 15 |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 266 | |
| Private | 139 | 52% |
| Acquired | 104 | 39% |
| Defunct | 17 | 6% |
| Public | 5 | 2% (Delivery Hero, Zalando, Ozon, HelloFresh, Westwing) |
| Unknown | 1 | Tingles |
| $1B and above | 16 | 6.0% |
| of which $10B and above | 1 | Delivery Hero $12.6B |

**$1B and above:**

- **Public, by market cap on 2026-09-29:** Delivery Hero $12.6B, Ozon $7.59B, Zalando $5.97B.
- **Private, last priced round:** Quantum Systems $8B, Neura Robotics $7B, AMI Labs $4.53B,
  Flix $3.24B, n8n $2.5B, Enpal $2.41B, Isar Aerospace $2.31B, Verbit $2B (stale), Framer $2B,
  Scalable Capital $1.71B, Exein $1.7B, Finn $1.13B, Sennder $1B (stale).

**Entry stage.** Seed 47, Series A 32, Growth 28, Pre-Seed 4. For 155 rows the round is not on
record: it is undetermined for most of the corporate-era and 2000s rows, where the press named no
round.

**Headquarters.** DE 196, GB 17, US 15, NL 8, FR 4, CH 3, RU 3, then a tail. 264 of 266 rows carry
a city.

**Focus.** Consumer & Marketplaces 106, SaaS 29, Media, Gaming & Advertising 25, Fintech & Payments
23, AI & Applied AI 22, Healthcare & Bio 19, Climate & Energy 14, Industrial & Robotics 14.

**Membership evidence.** Site listing 263 (the firm's own lists in six site generations), press 3
(the recall additions).

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 47 | 4 | 43 | 28 | 15 | **65.1%** |

Coverage is 100%.

- **Censored (4):** AMI Labs, Hades, PraxiPal, iGent.
- **Not graduated (15):** all 15 rest on the dated absence test over the named surfaces. Five of
  them also have a cited end:
  - Actio: insolvent in 2023.
  - Eating with the Chefs: shut in 2018.
  - Musicplayr: liquidated in 2015.
  - Rvvup: sold to Zopa in 2025.
  - Impossible Cloud: see R5.
- **Graduated:** by a named later round, or by an unnamed round above the step-up bar (Lieferheld,
  i2x, Delli, Flank).

### Calibration

| Book | Rows | Acquired | Defunct | Private | $1B+ | S2A |
|---|---|---|---|---|---|---|
| HV Capital | 266 | 39% | 6% | 52% | 6.0% | 28/43 = 65% |
| Cherry | 148 | 16% | 7% | 72% | 5.4% | 52/83 = 63% |
| Creandum | 177 | 28% | 6% | 60% | 11.9% | 36/71 = 51% |
| Balderton | 281 | 40% | 9% | 46% | 7.5% | 18/36 = 50% |
| Point Nine | 199 | 28% | 9% | 61% | 7.0% | 80/145 = 55% |

HV's acquired share matches Balderton's, and both are long-history books. The $1B+ share sits
between Cherry and Point Nine. The S2A rate is in Cherry's range, on a cohort half its size.

## 3. The boundary

- **One firm, two advisers of one manager (D1).** Every vehicle is IN, the Ventures and Growth
  sleeves alike. Co-investment and continuation vehicles (COIF, Coco, Founders/Co-Founders KGs) are
  plumbing (D5). A position moved into the Coco continuation fund keeps its original entry.
- **The corporate era 1999-2010 (D2).** Rows the unit itself listed are IN. The parent's arms are
  OUT. StudiVZ (bought by Holtzbrinck Networks in 2007) and Tutoria (bought by Holtzbrinck Digital
  in 2010) read `acquired`.
- **Sale consideration (D4, R1).** The firm's own export files an acquirer in place of the company
  it backed, carrying that company's entry year, fund and description. Ten acquirers are out:
  - Groupon (CityDeal), Rocket Internet (the Rocket companies), Care.com (Betreut.de), Boku
    (mopay), Cabify (Easy Taxi), Qonto (Penta), Deel (Zeitgold), Wellhub (Urban Sports Club),
    Zopa (Rvvup).
  - **SumUp (payleven), which is new at this run.** payleven merged into SumUp in April 2016 and
    its investors took SumUp shares, and no SumUp round names HV.

  Two acquirers stay as members because HV later put its own new money into them:
  - Bioniq: HV co-led its Series B in 2024.
  - Delivery Hero: the ~EUR 25M round of April 2012. **The merge that folded Lieferheld into
    Delivery Hero is removed.** Lieferheld is its own row: seed 2010, acquired 2012.
- **Programmes and people (D6), incubations and the Audible.de joint venture (D7), Form D homonyms
  (D8).**

## 4. Coverage per evidence regime

- **Firm site.** The portfolio export API behind the site's export button (154 companies, each with
  entry year, fund, entry stage and status; `sources/site/companies-2026.json`), and the team CMS
  (66 cards: 27 investing, 4 advisory, 3 platform).
- **Archive, hvcapital.com.** The 2022-2025 Storyblok lists (223 companies including exits back to
  1999, each with an entry date and deal partners) and the 2020-2021 Divi page.
- **Archive, holtzbrinck-ventures.com.** Parsed years 2006, 2007, 2011, 2015 and 2017 (the whole
  current and former portfolio in each page's navigation), plus 22 of the firm's 2010-2011 news
  posts.
  - The CDX enumeration of the old domain (10,880 captures) named 263 companies. All 21 names not
    in the base turned out to be spellings of rows already in it (PlusDental, Schüttflix, MyHammer
    and others), so no company is missing.
  - **Debt (delayed, not permanent):** the 338 per-company pages of the old domain were not
    fetched. The first machine-wide Internet Archive cooldown (27 minutes) ended at 17:03 local
    time. The first request after it was refused at the firewall, and the shared throttle then set
    a 240-minute cooldown. Those pages add text and invest dates for the 2006-2010 generation, not
    companies. The targeted fetch script is ready (`scratch/hv_archive_targeted.py`).
- **Common Crawl.** The index host refused connections all run (`index.commoncrawl.org:443`). The
  attempt is recorded here.
- **EDGAR.** Both advisers' Form ADV Section 7.B tables (`sources/registers/adv-7b.json`); six fund
  Form D filers; one fund 13G filer (Holtzbrinck Ventures NM on Spark Networks SE); the Form D
  sweep. The portfolio side files nothing with the SEC; the sweep's only hits were four homonym
  traps.
- **Registers.** North Data (the Handelsregister mirror) for the lineage (D2) and for the status of
  every row the grind had left `unknown` (section 8).
- **Press.** Google News per row (`graduation-surfaces`: 292 rows, 0 failed), the recall sweep
  ('"HV Capital" leads', '"Holtzbrinck Ventures"'), and publisher pages read for each cited
  sentence.

## 5. Recall probe and measured recall

**Recall additions (4):**

- Ore Energy: $43M Series A co-led by HV, August 2026.
- Fifth Dimension: $26M Series A led by HV, May 2026.
- peaq: token round, March 2024.
- Lieferheld: separated from Delivery Hero, sourced to the firm's own 2011 post.

The first two postdate the firm's 2026 export, which is the recent-deal blind spot. MarqVision was
rejected: HV's participation is unconfirmed and the article is paywalled.

**Measured recall.** HV's homepage claims "290 portfolio companies" and "12 IPOs".

- The base holds 266 members plus 14 rows ruled out. Most of the 10 consideration rows appear on
  HV's own list and so count in its 290.
- The export (154) and the 2022-2025 lists (223) are both inside the base.
- The 12 IPOs are Zalando, Delivery Hero, HelloFresh, Westwing, Home24, Ozon, Spark Networks (as
  eDarling), Dialogue, CafePress and Care.com (out, D4), plus Groupon and Rocket Internet (out, D4).

## 6. Method deltas

- **The firm's own portfolio export as a stage source.** Its `stage_at_entry` label was scored
  against documented rounds: 16 of 17 'growth' rows were Growth entries. It is promoted at medium
  confidence (R2, D11); the 'early' label stays an anchor.
- **Consideration detection from the export.** An acquirer row carries the acquired company's year,
  fund and description. Reading every acquirer on the list against that pattern found ten.
- **The German register as the status layer.** A North Data sweep (its `suggest.json` endpoint and
  company pages) settled 41 of the 47 rows the grind had left `unknown`.
- **A targeted old-domain fetch.** One capture per distinct page rather than per year: 338 fetches
  in place of 1,774, the same companies at a fifth of the archive exposure.
- **Class sweeps after duty 7 (duty 9).** The blind sample found three undetermined rows with
  citable round names, so every undetermined row was swept: 38 of 196 were labelled (19%).
- **Model mix.** Every judge and sweep ran on the default model (Opus 5.5).

## 7. Flags and debt behind `verify`

**Flags on the 266 published rows:**

- `unstable` 10 (duty 7).
- `model_disputes_source` 10: wrong Wikidata or SEC joins on one-word names, each disputed with
  evidence.
- `stale` 5: Sennder, Verbit, Spark Networks, CafePress, Midas.
- `cik_weak` 3: CafePress (the right company), FMC and Midas (quarantined; the float belongs to a
  namesake).
- `stage_uncited` 1: Wooga.
- `city_unknown` 2: Infoseek, MyHammer.
- `ruling_open` 1: Impossible Cloud.
- `unicorn_name_match` 1, `token_funded` 1: peaq.

**Debt:**

- 155 rows with the round not on record.
- The old-domain per-company pages (section 4).
- One `unknown` status (Tingles; the YC book reads it the same way).

## 8. Standing duties and the A/B pass

- **A/B on the visible slice** (27 companies researched: the 20 rows now at $1B+ or public,
  plus the consideration acquirers), with a cited source per value.
  - Public caps were read 2026-09-29 from StockAnalysis, with EUR at the ECB rate of that day
    (1.1355). Ozon's cap is companiesmarketcap's USD figure: the ECB has published no RUB rate since
    March 2022.
  - n8n moved from $5.2B to $2.5B: SAP's May 2026 purchase was a secondary share sale (R6).
  - NEURA's and Quantum Systems' figures are now cited to CNBC and the company release, replacing
    aggregator pages.
  - Solaris is acquired: SBI took the majority in 2025.
  - Klima is acquired: Wren bought it in 2025. HV's export still says active.
- **Rule A.** No $1B+ mark rests on a vendor. Sennder ($1B, 2021) and Verbit ($2B, 2021) keep their
  last priced rounds, flagged stale.
- **Momentum slice.** All 18 recent hot-sector private rows got one recorded web check
  (`valuation_check`); all stay below $1B.
- **Weak joins.** Groupon (out), CafePress (right company), FMC and Midas (a namesake's float,
  quarantined).
- **Unicorn re-intersect** with loose normalization: 7 matches, each banded or out (FlixMobility is
  Flix; Solarisbank is Solaris, now acquired).
- **Duty 7, blind 5%.** 14 rows re-judged by a judge with no access to the record: 68 of 84 cells
  agree (81%). The 16 disagreements (10 rows) all fell on questions the grind had left open, and
  every one was adjudicated to the blind judge's cited evidence:
  - Hyperganic is defunct (insolvency and register deletion), although HV lists it active.
  - Lendis and Charles have cited seeds and graduated.
  - Eating with the Chefs, fettspielen.de and Musicplayr are defunct.
  - Kyte is acquired (KIT digital, 2011); HitFox is private as IONIQ Group.
  - Kipu Quantum moved to Berlin; buecher.de is in Augsburg.
- **Duty 9, the class.**
  - **Status:** 47 `unknown` rows swept. 41 settled plus the 5 duty-7 rows; Tingles stays unknown.
    Three no-sale insolvencies read `defunct` under D9: Loots, Virtual Nights, and mercavus, whose
    Faire deal was a team-and-asset buy that the acqui-hire rule reads as defunct.
  - **Stage:** 196 undetermined rows swept by three agents. 38 were labelled from a source naming
    HV's round.
  - **Two merges came out of the sweep:** Rumble Media into fettspielen.de, and jobmensa into
    jobvalley.

## 9. Firm profile

- **Thesis:** "Backing the bold. Building the future." (the firm's own line, verbatim).
- **History (68 words):** founded in Munich in 2000 as the venture arm of the Georg von Holtzbrinck
  publishing group; independent in 2010; renamed in 2020; Zalando, Delivery Hero, HelloFresh, Flix
  and Scalable Capital; Fund IX of EUR 710M in 2023.
- **HQ:** Munich, from the ADV principal office (Kaiserstrasse 14b), with Berlin as the other
  office. `sources/offices.json`.
- **AUM:** $4,000,968,225 at both ends, the sworn Section 7.B gross values of the ten master funds.
  Feeders are excluded to avoid double counting. The firm's own "2.8 billion euros AUM" is
  committed capital, noted.
- **Funds:** IX ($786.3M, 2023), Coco Growth ($489M, 2022), VIII ($625M, 2020), VI ($330.3M,
  2015), IV ($229.2M, 2011), each at the ECB rate of its announcement date.
- **Stages** Seed, Series A, Growth. **Geography** core Europe, other US. **Scope** Generalist,
  focus from the export's category tags through a new crosswalk (`config.json`
  `profile.focus_crosswalk`): Consumer & Marketplaces, SaaS, Industrial & Robotics, Healthcare & Bio,
  Climate & Energy, Fintech & Payments.
- **Range:** $553,700 to $66,444,000 (the firm's stated EUR 500K to EUR 60M ticket), median $12M.
  The median is taken over the 73 entry rounds whose size the record states; it is a round size,
  not the cheque, and flagged press-based.
- **Notables:** Zalando, Delivery Hero, HelloFresh, Flix, Depop. **Individuals:** 34.
- **Icon:** the firm's own logo file (2380x2380, self-backed plate). It was chosen with
  `--discover` over the 512px manifest icon, and the dry run passed: contrast 3.9:1, edge ramp
  1.01px.

## 10. Open rulings for Erik

1. **D2, the corporate era** (PRO-104's lineage delta): IN, with the parent's arms OUT. Flagged as
   the issue asked.
2. **SumUp out (R1).** This reads the 2016 SumUp and payleven "merger" as a share swap at a sale:
   SumUp's name survived and payleven's investors took SumUp shares. If a merger of equals is read
   as a new position, SumUp ($8.6B, a floor) comes in.
3. **Delivery Hero on its April 2012 entry, with Lieferheld separate (R1).** The alternative is one
   row entered at Lieferheld's 2010 seed, which would add Delivery Hero to the S2A cohort as a $10B+
   graduated seed.
4. **Impossible Cloud (R5).** The founders' Swiss sister entity, Impossible Cloud Network, raised
   EUR 28.8M at $470M with HV. Read as two companies, the row did not graduate. Read as one, it
   graduates.
5. **n8n's figure (R6).** $2.5B here; Sequoia's and Felicis's books carry SAP's $5.2B secondary.
   Same band, different figure: align the siblings to the primary, or accept secondaries as marks.
6. **Acquired rows at a $1B+ exit read `below_1b`.** Depop was sold for $1.6B in 2021 and resold
   for $1.2B in 2026. This is the convention across every book (5,696 acquired rows, none banded
   higher) because `valuation_usd` needs a private or public status. It is not written as a rule
   in §7.
7. **Status calls under D9 made at this run:**
   - Loots, Virtual Nights and mercavus read `defunct`: none has a documented sale, and mercavus's
     deal was a team-and-asset buy.
   - Caremondo reads `acquired`: the assets were sold out of insolvency to FairmedOnline.
   - Tutoria reads `acquired`: it was sold to the parent's Holtzbrinck Digital in 2010, the same
     reading as StudiVZ.
   - Platinnetz stays a member: HV took control of it in 2009, after its 2007 venture entry.
8. **Hyperganic reads `defunct`** from the register: the operating company went insolvent in 2025,
   and the parent received a deletion notice on 2026-09-11. HV's export still lists it as active.
9. **Tingles stays `unknown`.** YC marks it inactive, which the YC book ruled is not the same as
   defunct.

## 11. Rebuilds and deltas

The grind judged 292 rows. The one scheduled rebuild after the recall probe gave 266. It removed
the 14 `not_member` rows, applied 16 merges (19 duplicate rows folded, including jobmensa and
Rumble Media from the sweeps), added the 4 recall additions, and dropped the Delivery Hero merge.

The rename list was read after the rebuild: no verdict moved onto another company.
- The only new slugs are the 4 additions.
- The 11 archive-only names are all spellings of existing rows.

The delta grind judged the 4 additions and filled 4 HQ countries whose Wikidata answer had been
deferred. No second rebuild was needed. 23 published names were set in `config.json`
`names.published` under the §8 capitalisation rule, among them Verbit, Neura Robotics, Wind
Mobility, Ozon and Sennder (aligned with Accel's book).

## 12. Playbook write-backs proposed (not applied: COLLECTION.md has other sessions' uncommitted hunks)

1. **An identity merge never joins an acquired company into its acquirer**, even when the firm's
   own list later files the position under the acquirer. Lieferheld into Delivery Hero was merged
   at kickoff and had to be undone once D4 was applied. The merge check should ask "one company or
   a sale?" before "one name or two?".
2. **A press "merger" in which one name survives and the other side's investors take its shares is
   a sale by share swap** (SumUp and payleven). This extends the 2026-09-26 share-swap ruling in §1.
3. **The German register sweep belongs in the German recipe.** North Data's `suggest.json` and its
   company pages settled 41 of 47 `unknown` rows and found defunct companies that the firm still
   lists as active (Hyperganic). It is cheap and uses no web-search budget.
4. **Archive fetches take one capture per distinct page, not per year** (338 against 1,774 on the
   old domain). The throughput rule should also say: **probe before resuming after a cooldown.**
   The first bulk request after the 27-minute cooldown hit a firewall block that was still active,
   and it escalated to 240 minutes for every session.
5. **FX gap:** the ECB has published no RUB reference rate since 2022-03-01. For a ruble listing,
   the aggregator's own USD cap stands, noted (Ozon).
6. **The momentum check on a row with no press at all** records its dated finding in
   `valuation_check`, cited to the firm's listing (Cogny, Comet, Informed, Reiner.ai).
7. **German round words for `scripts/stage_words.py`:** "Startkapital", "Seedfinanzierung",
   "Seed-Runde" and "Serie A" were all read by hand this run.
8. **Archetype-B lesson (also posted to PRO-87):** a European early-stage book leaves most
   pre-2015 entry rounds unnamed (155 of 266 undetermined here). A class sweep of the undetermined
   rows in the grind itself, not only after duty 7, found names for about one row in five.

## 13. Usage line

**Kickoff (Opus 5.5):** five-hour window 74%, weekly 71%, Fable 6%. **Close:** five-hour window
24%, weekly 8% (a new week began mid-run), Fable 0%.

**Web searches:** well under the 200 cap. Four sweep agents were capped at 10 each, the blind judge
at 12 and the visible-slice agent at 40 (it used 18); everything else ran on the uncapped Google
News helper.

**Subagents:** the visible-slice research agent (which ran three sub-groups), the blind duty-7
judge, a status sweep and three stage sweeps.

## 14. Prompt count

**1**: the kickoff ("please collect HV Capital"). No corrections from Erik. The count is final at
the closing message.

## 15. Ingest

Filled in at the ingest (below).
