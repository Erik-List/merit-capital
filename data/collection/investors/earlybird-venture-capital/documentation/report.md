# Earlybird: Build & Reconciliation Report (PRO-107)

**Linear issue** PRO-107 · **slug** `earlybird-venture-capital` · one run under the merged shape of
`data/collection/COLLECTION.md`, one session · report written 2026-10-07.
**Ingested 2026-10-07 through the §9 gate: 195 companies live, readback exact; Cherry, Battery Ventures and Creandum aligned and re-ingested (section 16).**

---

## 1. The answer PRO-107 asked for

**The base is 195 companies, plain `verify` is clean, the firm profile is built, and the book is
live: ingested through the §9 gate with an exact readback (section 16).** Earlybird is the firm run from Berlin and Munich under the exempt reporting adviser
Earlybird GmbH & Co. KG (CRD 341941), founded in Hamburg in 1997. The book runs from the 1998 fund
through Fund VIII (2026) and includes Earlybird Health and the Earlybird-X (UNI-X) seed fund.

The PRO-107 deltas, all derived from verified facts (`decisions.md`):

- **The Digital East boundary (D2).** Digital East is OUT and partitioned as its own desk:
  38 rows, including UiPath, Payhawk, Hazelcast and Trendyol. Three
  facts decide it: the firm's own disclaimer on each of those company pages ("The investment
  decision for this company was made by the separate company Digital East Fund which was operating
  under the licensed 'Earlybird' brand"), the fund's own Luxembourg registration and manager, and
  its rebrand to Bek Ventures in 2024. The partition is one config line (`desks.partition`) and
  can be reversed without a rebuild of the evidence. Flagged for Erik (section 10).
- **Earlybird Health (D3) and Earlybird-X (D4)** are IN: same brand, same site, the firm counts
  both in its own figures, and the Health team sits on the firm's team page.
- **The German recipe (D10)**: insolvency followed by an asset sale reads `acquired`; a filing
  with no sale reads `defunct`; listings outside SEC registration take a web-cited market cap.
- **No entry-date window (D11).** The issue expected a pre-2006 slice; that constant was removed
  on 2026-09-19. A 1998 entry is judged on the same evidence as a 2024 one.
- **Registers east of Germany (D12).** The probe ran: the Czech and Slovak registers are usable
  and name the investing entity per round; Turkey's is not (section 4).

Out: 35 rows ruled `not_member`, 38 partitioned with Digital East, 1 dropped by the build filter.

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean at 195 rows; flagged debt only (section 7) |
| Boundary ruled and dated | D1 to D9, R1 to R4; Digital East flagged |
| Outcome classification | 195 of 195 rows, every column filled or `undetermined` with a reason |
| Profile through the taxonomy gate | `build-firm-profile.py` and the copy check ok; every field populated or null, with a source |
| `review.html` rendered | Served on the local static server: rows flat, profile panel expands, no console errors |
| `report.md` | This file |
| Playbook write-back | Section 13 (proposed, not applied) |
| Ingest through the §9 gate, sibling rows aligned | Done: 195 live, readback 0 differing cells; Cherry, Battery Ventures and Creandum re-ingested, each exact (section 16) |

## 2. Results

| Status | Rows | Share |
|---|---|---|
| Private | 100 | 51% |
| Acquired | 62 | 32% |
| Defunct | 29 | 15% |
| Public | 4 | 2% |

Public: NFON, Oculis, Tipp24 (Zeal Network) and Wilex (Heidelberg Pharma).

**$1B+ (6 rows, 3.1%), each on a cited priced event:**

| Company | Figure | Event |
|---|---|---|
| N26 | $9.0B | Series E, October 2021 (flagged `stale`) |
| Recursive | $4.65B | cited round |
| Black Forest Labs | $3.25B | cited round |
| Aiven | $3.0B | Series D extension, 2022 (flagged `stale`) |
| Isar Aerospace | $2.31B | cited round, converted at the ECB rate of its date |
| Sennder | $1.0B | Series D, January 2021 (flagged `stale`) |

OneFootball reads below $1B (R8), as in the Lakestar and USV books.

**Entry stage:** Seed 51, Series A 50, Growth 15, Pre-Seed 15, undetermined 64. All 131 named
stages are `web_verified` (a cited round naming Earlybird). The firm's own "Stage" label was
scored and refused (R6: 66 of 92 right overall, Pre-Seed 11 of 29).

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 51 | 11 | 40 | 19 | 21 | **47.5%** |

- **Censored (11):** Arago, Bayshore, Brandback, Briefcase, eyva, Gemma Biotherapeutics, Mona AI,
  Pillar, Sintra, SpAItial, TopK. All entered after October 2024.
- **Not graduated (21):** nine rest on a cited end (Ctrl, DeepCode, The Interaction Company and
  ThingsThinking were bought; Ducktrain, Everstores, Moped, MyDataModels and Payable shut down).
  Twelve rest on the dated absence test over the firm's own pages and at least two publisher
  surfaces each (TechCrunch, Crunchbase News, deutsche-startups, Bing News; section 6).
- **Graduated (19):** 17 on a cited later round (`web_verified`), 2 on the firm's own record
  (Interhyp, BridgeCo). Unnamed later rounds graduate on their amount (R7).

### Calibration

| Book | Rows | Acquired | Defunct | Private | $1B+ | S2A | Stage unknown |
|---|---|---|---|---|---|---|---|
| Earlybird | 195 | 32% | 15% | 51% | 3.1% | 19/40 = 48% | 33% |
| HV Capital | 266 | 39% | 6% | 52% | 5.6% | 28/43 = 65% | 58% |
| Cherry | 148 | 18% | 7% | 70% | 6.1% | 53/84 = 63% | 11% |
| Creandum | 177 | 29% | 5% | 60% | 10.2% | 37/72 = 51% | 2% |
| Lakestar | 154 | 19% | 5% | 70% | 14.9% | 17/35 = 49% | 31% |
| Northzone | 220 | 26% | 4% | 48% | 3.6% | 12/19 = 63% | 55% |

Two things stand out. The defunct share (15%) is two to three times the peer books'. It comes from
the 1998 to 2008 funds: 47 rows date from before 2010, and the firm's own archived lists and
releases name the failures of the dot-com and biotech years, which most firms' pages drop. The
$1B+ share is the lowest of the German peers because the largest outcomes under the Earlybird
name (UiPath, Hazelcast, Payhawk) sit with Digital East (D2).

## 3. The boundary

- **D1, the firm.** Earlybird GmbH & Co. KG, CRD 341941; the technology funds I to VIII, the
  Growth Opportunity funds, Earlybird Health, Earlybird-X.
- **D2, Digital East out** (38 rows, `other_desk`). See section 1 and section 10.
- **D5, E2D** (the defence growth fund announced with AVP): no investment on record yet; a future
  run rules on it when it has a portfolio.
- **D6, Vision Lab out**: a grant programme, no fund money.
- **R1, "Pre-Fund Investments" out (13 rows plus Vitraum).** The firm's 2018 to 2023 list had this
  status beside Current and Exited. No round names an Earlybird fund for any of them: they are
  partners' positions from before they joined (Biocompatibles, Thermocore, Reverse Medical,
  CryoTherapeutics, Ayoxxa, Arthrokinetics, Topsfield Medical, DailyDeal, Forto / FreightHub,
  JustBook, McMakler, test IO, Eyeota). Inkitt and CrossEngage began the same way but an
  Earlybird fund is named in later rounds: they stay, with the entry stage `undetermined`.
- **R2, sale consideration out (3 rows):** BioValve (for Redeon), NoemaLife (for GMD), Snyk (for
  DeepCode). **Sennder stays** on the new money Earlybird put into its June 2020 round; Everoad
  and Sennder are two rows.
- **R3, Lilium out:** Earlybird led the PIPE of July 2023, 22 months after the listing (the
  post-IPO rule of 2026-09-06).
- **R4, Form D name matches out (15 rows):** the related person shares a name with an Earlybird
  partner but sat on the board for a previous employer, in person, or is someone else.

## 4. Coverage per evidence regime

- **Firm site.** earlybird.com and health.earlybird.com are Framer builds with no API. The list
  pages and Framer's own search index were parsed (`scratch/eb_site.py`): 120 companies on the
  main list, 18 on the Health list, each with the firm's "Invested" year, founders, deal team and
  the Digital East marker; 48 and 14 team cards. The job board adds 72 names. Together 159 names,
  all in the base or partitioned.
- **Archive, Common Crawl.** Used as the archive because the Internet Archive was in a machine-wide
  cooldown for the whole run. Captures of 2008 to 2026 were fetched and parsed
  (`scratch/eb_archive.py`): the 2008 to 2010 A to Z, recent and exits pages, the 2010 to 2013
  pages, the 2014 to 2017 one-pager, the 2018 to 2024 lists with their status and fund tags, and
  173 of the firm's press releases (1999 to 2010).
- **Archive, Internet Archive.** 10 pages were fetched before the cooldown. The page-address index
  of earlybird.com (fetched earlier, `scratch/cdx/`) names every per-company page of 2001 to 2013;
  eight companies known only from their page address were identified by research and added.
  **Debt:** the 2001 to 2007 A to Z lists themselves are unread (173 targets in
  `scratch/ia_pull.py`).
- **EDGAR.** Form ADV of the adviser with its Section 7.B fund table
  (`sources/registers/adv-341941.txt`); the full-text sweep (16 third-party registrants, each
  read, none a new company); the Form D related-person sweep (15 name matches, all out, R4).
- **Registers.** North Data for the German entities and for statuses. The probe east of Germany
  (`sources/registers/cee-turkey-probe.json`): the Czech register (ARES) and the Slovak one (RPO)
  are free, machine-readable, and name the investing entity per round (Socialbakers: Earlybird
  Verwaltungs GmbH; Photoneo: Digital East Fund 2013 SCA SICAR), which is exactly the evidence
  the Digital East boundary needs. Poland answers by register number only, Romania gives status
  only, Bulgaria was not established, Turkey sits behind a login.
- **Press.** One research pass per row by era (13 groups, `scratch/research/`), each cited
  sentence read on the publisher's page; the firm's own releases for 1999 to 2010.
- **Wikipedia.** The insource sweep returned 14 articles; nothing outside the base except Digital
  East positions.

## 5. Recall probe and measured recall

`sources/web/recall-probe.json` lists what was diffed against the base and what each source added.

- **Additions (9):** eight companies of 2001 to 2007 from the archive's page-address index
  (asyntis, EuroProteome, interNetwork, InTime, IQ Labs, iScribe, Music United, Vital Sensors) and
  Sennder (R2).
- **Rejected (1):** Yoggie Security Systems. The Wikipedia article means EarlyBirdCapital, Inc.,
  the New York namesake.
- **Parametric enumeration by era and sector** found no company missing apart from Digital East
  deals.

**Measured against the firm's own claims.** The homepage says "41 trade sales"; the base holds 62
`acquired` rows, which includes insolvency asset sales and the pre-2010 exits the live list no
longer shows. The IPO counter on the homepage is animated and could not be read from the page
source. The 2025 year-in-review post mentions two investments "under wraps"; they are not in the
base and cannot be.

## 6. Method deltas

- **Framer search index as the site source.** A Framer site ships one JSON with the text of every
  page; joined to the list-page anchors it gives the full company record without a browser.
- **Common Crawl's static index as the archive route.** The CDX host was not needed: the cluster
  index on the data host resolves a domain's captures, and WARC range requests fetch them.
- **Absence-test surfaces without Google News.** Google News answered 503 all run. The surfaces
  used are each publisher's own post search plus Bing News (`scratch/eb_surfaces.py`); a failed
  lookup is stored as an error and never as an empty answer.
- **Desk partition by the firm's own marker.** The Digital East rows were identified from the
  marker on the firm's pages, then checked against the archived lists' fund tags.
- **Class sweep after duty 7.** One blind disagreement (an asset sale out of insolvency read as
  `defunct`) was swept across every `defunct` row with an insolvency: one more row changed.
- **Model mix.** The judge and every research pass ran on the default model (Opus 5.5).

## 7. Flags and debt behind `verify`

| Flag | Rows | What it means here |
|---|---|---|
| `model_disputes_source` | 6 | EBS, IQ Labs, Nortech, Ripe, TILT, Versus: a mechanical join named a different company of the same name; the judged value stands |
| `stale` | 3 | Aiven, N26, Sennder: the $1B+ figure is from 2021 or 2022 |
| `stage_disputes_band` | 2 | Shape Memory Medical, Zonare: a Growth entry into a company that ended below $1B |
| `unstable` | 2 | yoom, smoodoos.com: `acquired` on an asset sale out of insolvency to the founder |
| `cik_weak` | 1 | IQ Labs: the SEC name join is wrong and carries no value |

**Debt:**

1. **The 2001 to 2007 archived lists are unread.** The Internet Archive was in cooldown for the
   whole run. The companies of those years are in the base from the page-address index and the
   press archive, so the risk is a handful of early rows without a press release. To pay it:
   `python3 scratch/ia_pull.py`, then `scratch/eb_archive.py`, then judge any addition.
2. **64 rows carry an `undetermined` entry stage (33%).** 33 of them date from before 2010, where
   the firm's releases say "first financing round" and name no stage (R5).
3. **RhodeCode's Series A** is named only by Wikipedia; the row keeps its stage `undetermined`.
4. **CrossLend reads `private` on the register, against a 2023 trade headline** (section 8).
5. **`hq_city`** is filled on all 195 rows; the source label is the model's on every row, checked
   against the firm's page where it gives one.

## 8. Standing duties and the A/B pass

- **Duty 7, blind re-check.** A second agent judged 10 rows without the recorded values
  (`scratch/duty7-blind.json`). 9 of 10 agreed on status, band, country and stage. One status
  differed (yoom: the founder bought the platform, brand and user data out of the insolvency, so
  `acquired` under D10). The class sweep found the same shape at smoodoos.com. One city differed
  (GMD: the blind pass gave Berlin, the seat after the 2002 merger; Munich, the seat while
  Earlybird held it, is kept).
- **Correction at the ingest gate (CrossLend).** The first pass read `defunct` on a paywalled 2023
  headline ("implodiert") and a dead domain. Before writing that value into the Lakestar and
  Northzone books I re-read the home register: CrossLend GmbH is active, with no liquidation or
  insolvency entry, a state aid notice for R&D tax credits in December 2024 and an address change
  registered in January 2026. No source gives a shutdown or a sale, so the row reads `private`,
  as both sibling books already had it. The yoom and smoodoos.com status citations were moved to
  the article that reports each asset sale.
- **A/B attack searches** on the boundary rows (Digital East, Sennder, Lilium, the pre-fund class)
  changed nothing.
- **Field score for the firm's stage label:** refused (R6, `scratch/field-score.json`).
- **Traps in `config.verify.not_members`:** UiPath, Payhawk, Hazelcast, Trendyol, Yemeksepeti,
  Lilium, AuthenTec, Digital River, Zynga, Standard Microsystems, Amgen, EarlyBirdCapital.
- **Cross-investor rule 10:** 54 rows shared with other books, all agree. 13 pairs ruled `distinct`
  (same name, different company; two of them, Tilt and Pillar in the Y Combinator book, showed
  only in that book's `verify`; three Hive pairs are ruled ahead of General Catalyst landing),
  1 pair ruled `same` (N26 and Battery's Number26). The Curio pair parked as `accepted` was
  removed once the Cherry book was aligned (section 16).

## 9. Firm profile

| Field | Value | Source |
|---|---|---|
| Name | Earlybird | Imprint (Earlybird GmbH & Co. KG, Berlin) |
| HQ | Berlin, Germany | Newest Form ADV principal office; the site agrees |
| Founded | 1997 | The firm's 1999 release and its site |
| Thesis | "Your partners from before the breakthrough." | The firm's own line |
| Stage | Pre-Seed, Seed, Series A, Growth | The firm's words, plus the Growth Opportunity funds |
| Geography | Europe core, US other | The firm's words and the portfolio's headquarters |
| Scope | Generalist, six focus areas | Derived from the portfolio, kept by hand (`focus_crosswalk` empty on purpose) |
| Cheque range | $3.0M to $13.5M, median $8.0M | Upper: the firm's "initial ticket sizes up to €12m". Median and lower: the 15 entry rounds announced March 2024 to July 2026. Press-based, flagged |
| AUM | $1.42B to $2.87B | Bottom: Form ADV 7.B gross assets. Top: the firm's "€2.5 billion" of 2026-06-18 |
| Funds | 9, from Fund IV (2008) to Fund VIII (2026, $421M) | ADV, the firm's releases, press |
| Notables | N26, Black Forest Labs, Isar Aerospace, Aleph Alpha, Interhyp | The five best known |
| People | 33, 27 with LinkedIn (82%) | Live team pages |
| Icon | Red plate, white wordmark | The site's own image, dry run inspected |

The history line says in plain words that the track record leaves out the former Digital East
fund, so a reader who knows UiPath as an Earlybird deal finds the reason on the page.

## 10. Open rulings for Erik

1. **Digital East is out (D2).** Decided on the firm's own disclaimer and the fund's separate
   registration, and reversible with one config line. It moves 38 rows, among them UiPath
   (public, $1B+), Hazelcast and Payhawk. If you want them in, the answer is to remove
   `digital-east` from `desks.partition`, rebuild and judge the 38 rows.
2. **Sennder is its own member row beside Everoad (R2).** Earlybird received Sennder shares for
   Everoad and also put new money into Sennder's June 2020 round. The new money makes it a member
   under the sale-consideration ruling; without it the row would leave and the book would lose a
   $1B+ company.
3. **"Pre-Fund Investments" are out (R1).** 13 rows the firm's 2018 to 2023 list showed under that
   label, plus Vitraum: partners' positions from before they joined, with no Earlybird fund named
   in any round. This follows the partner-carried ruling, but it removes names the firm itself
   listed (Forto, McMakler, DailyDeal), so it is worth your eye.

Settled without asking, by a standing rule or by research: Lilium (post-IPO), the three
consideration rows, OneFootball's band, yoom and smoodoos.com (asset sale), CrossLend (register).

## 11. Incidents

- **Internet Archive cooldown file (my error).** At the start of the archive leg I called
  `shared_throttle.cooldown("ia")`, which sets a cooldown, when I meant
  `cooldown_remaining("ia")`, which reads it. That wrote a four-hour machine-wide stop over a
  genuine two-hour one that had about two minutes left. I restored the file's exact previous
  content about 20 seconds later. A follow-up check of the throttle was refused by the permission
  check, so I left it there and did not touch the file again. The archive then refused requests
  on its own and the cooldown doubled, which is why the archive leg ran on Common Crawl. Any
  sibling session that read the file in those 20 seconds saw four hours where two minutes were
  true.
- **Session restart.** A network failure at about 00:15 UTC stopped the session and its research
  agents. Erik's "continue" resumed them; no work was lost, and it cost the second prompt.
- **Linear figure.** A milestone comment on PRO-107 gave S2A figures from memory (21 of 43). It
  was corrected to `verify`'s figures with an edit note.

## 12. Rebuilds and deltas

- The base was rebuilt three times: after the desk partition, after the eight archive additions
  and Sennder, and after the ledger repair below.
- **The rename step moved verdicts between companies** on the second rebuild: Snyk's `not_member`
  landed on Sennder and NoemaLife's on a name variant. Repaired by hand: both variants carry a
  verdict, Snyk was restored, Sennder judged afresh, FreightHub given Forto's verdict.
- `scratch/eb_overlay.py` first ran against the already partitioned base and emitted no desk rows.
  It now builds its universe from base, excluded rows and absorbed duplicates.
- A wording glitch in 168 verdict texts ("on its archived lists , to 9") was fixed in the ledger
  and in the converter.

## 13. Playbook write-backs proposed (not applied: COLLECTION.md and `scripts/` belong to the tooling session)

1. **§5, registers:** add the Czech (ARES) and Slovak (RPO) registers as free, machine-readable
   layers that name the investing entity per round. Poland by register number only; Romania status
   only; Turkey not usable. This is the layer that separates a licensed-brand fund from the firm.
2. **§5, site ladder:** a Framer site has no API but ships `framer-search-index`, one JSON with
   every page's text. Read it before reaching for a browser.
3. **§5, overlays:** a script that writes `identity-merges.json` must build its universe from
   base + excluded + absorbed rows, or a second run against a shaped base silently drops the desk
   list and the merges.
4. **§8, rebuild:** the rename step can move a `not_member` verdict onto a different company that
   shares a merge target (third and fourth cases: Snyk to Sennder, NoemaLife). Proposed: `record`
   refuses a re-key whose target slug has its own base row, and prints the pair.
5. **§6, absence test:** `graduation-surfaces.py` exits while Google News fails. Proposed: accept
   Bing News and the publishers' own post searches as named surfaces, as `eb_surfaces.py` does.
6. **§12, throttle:** `shared_throttle.cooldown()` sets and `cooldown_remaining()` reads; the two
   names are one slip apart (section 11). Proposed: rename the setter to `set_cooldown()` and make
   it refuse to shorten or lengthen an existing cooldown without a reason argument.
7. **§2, licensed-brand desks:** where the firm's own pages disclaim the investment decision for a
   set of rows, that disclaimer is the T1 answer and the rows partition as a desk.

## 14. Usage line

| | 5-hour | Weekly, all models | Weekly, Fable |
|---|---|---|---|
| Kickoff | 28% | 13% | 4% |
| Close (2026-10-07) | 30% | 25% | 5% |

195 base rows (233 membership verdicts, 38 further rows partitioned): 12 weekly points, about 0.06 points per
published company. WebSearch: about 107 of the 200 per session.

## 15. Prompt count

**2.** The kickoff ("please collect earlybird") and one "continue" after the session restart. No
correction and no approval prompt.

## 16. Ingest

**Earlybird is live.** The gate ran in order on 2026-10-07:

| Step | Result |
|---|---|
| Preconditions | Plain `verify` clean; `run.py close`; closing commit e3ff87f1, gate corrections c75c53b6 |
| Every landed sibling's `verify`, read for Earlybird rows | 41 books run; three showed Earlybird rows (Lakestar and Northzone: CrossLend; Y Combinator: two namesakes). All settled before the write (section 8) |
| Icon | Uploaded to the Icon Images bucket; `investor.json` carries the bucket URL |
| `ingest-investor.ts` | 1 investor row upserted |
| `ingest-companies.ts --dry-run` | 195 upserted (195 new), 0 removed, from 0 live |
| Removal check | Nothing to remove (first ingest) |
| Write | 195 of 195 upserted |
| Readback | csv 195, live 195, missing 0, extra 0, differing cells 0 |

The investor row reads: S2A 19 of 40 (47.5%), 11 censored, 51 seed entries; 6 companies at $1B+
(Aiven, Black Forest Labs, Isar Aerospace, N26, Recursive, Sennder); 4 public (Nfon, Oculis,
Tipp24, Wilex); 195 companies; investing since 1997.

**Sibling rows aligned and re-ingested, one book at a time** (readback before the write showed only
the cells this run changed; dry run 0 removed; readback after 0 differing cells):

| Book | Row | Change | Evidence | Commit |
|---|---|---|---|---|
| Cherry | Curio | `acquired` to `defunct` | Curio Labs Limited (10145832) in creditors' voluntary liquidation since 2025-05-30 (Companies House). The "acquired by Wasabi" was Curio AI from GrayMeta, a different company | d9a3de0f |
| Battery Ventures | Number26 | below $1B to $9.0B (2021-10, `stale`); entry stage Series A (uncited) to Growth, cited | TechCrunch 2021-10-18 for the Series E; Global Venturing 2016-06-22 names Battery in the Series B. The stage and country citations were the gate repair a $1B+ row needs | 82c481f5 |
| Creandum | terralayr | Seed `censored` to `graduated`; entry stage cited | EUR 192M round of January 2026 led by Eurazeo with Creandum (deutsche-startups 2026-01-20); TechCrunch 2024-10-17 for the seed | c247a95d |

Cherry's `verify` needed `--skip-links` (the book has no EDGAR link to sample, a known mechanical
case). Creandum's S2A moves from 36 of 71 to 37 of 72.

**Not written, reported for the owning run:**

- **General Catalyst (in flight):** The Interaction Company of California reads `private`; Cognition
  bought it in July 2026 (`acquired` in this book).
- **Speedinvest (in flight):** Inkitt reads Berlin; the company's headquarters moved to San
  Francisco (this book).
- **Battery Ventures, published name:** the row still publishes as "Number26". The name lives in
  that book's `config.json`, which has another session's uncommitted changes, so it was left.
- **CrossLend in Lakestar and Northzone:** no change needed after the correction in section 8.
- **Founders Fund pairs:** 8VC, Sequoia (The Boring Company) and Lux (Impulse Space) fail rule 10
  against the Founders Fund book, and Coatue fails rule 6 on one row. None involves an Earlybird
  row; they belong to those runs.

Nothing was pushed.
