# Coatue: collection run report

**Linear issue** PRO-78 (Phase 2, layer-building run) · **slug** `coatue` ·
run closed **2026-09-27** · one session, one run, under the merged shape of
`data/collection/COLLECTION.md`. **Ingested 2026-09-27 on Erik's approval**
(see the addendum at the end).

---

## The answers PRO-78 asked for

**1. Does `entry_stage` need a crossover ruling? No.** Growth already means
"Series B and everything later, secondaries and tenders included", which is
every Coatue entry that is not a Seed or Series A one. The column held on all
379 rows without a new value. What the crossover shape changes is the
comparison, not the column: the Seed cohort is 22 rows, so the S2A rate is a
small-sample number and the leaderboard should show the cohort beside it or
hide the rate under a floor (decisions.md X2, Erik's to decide).

**2. The shape guard needs no exception any more.** The playbook dropped the
ceiling on the $1B+ share on 2026-09-26. The share is stated here instead:
**165 of 379 rows (43.5%)** read $1B or more, against IVP's 23.5% and
Thrive's 39%. The config's restated ceiling was removed and X1 withdrawn.

**3. Hedge-fund desk against growth desk: the split is by vehicle, never by
company.** The ADV lists 144 private funds. 111 private-markets master funds
and about 130 numbered single-deal vehicles form the home desk; the hedge
funds form the public desk. A company never moves between desks: a listed
line on a 13F, 13G or N-PORT is not a member, whatever vehicle holds it
(decisions.md D3). `desks.partition` stays empty on purpose.

**4. Three new evidence layers were built.** What each one is worth:

| Layer | Script and config key | Output | Evidence tier |
|---|---|---|---|
| 13F holdings | `scripts/edgar-13f.py`, `edgar.thirteenf_ciks` | `sources/edgar/13f-holdings.json`: 93 filings from 2000 to 2026, 1,399 issuers | Never membership. It dates when a member listed (33 members appear after their listing), feeds the `verify.not_members` traps (22) and corroborates public status |
| 13D/G positions | the existing `edgar-companies.py` chain | `sources/edgar/edgar-companies.json`: 40 issuers | A listed position on its own is not a member (17 rows ruled out under D3). Beside a private entry it confirms the firm held through the listing |
| N-PORT and N-CSR of the registered fund | `scripts/edgar-registered-fund.py`, `edgar.registered_fund_ciks` | `sources/edgar/registered-fund-holdings.json`: 6 N-PORT and 3 N-CSR filings, 19 restricted lines on 11 private companies at 2026-06-30 | Fund-filing membership for a restricted position. Ten of the eleven were on the firm's page already; Kalshi is the one member only this layer found. Fair values go to the note and never band a row (X3) |

PRO-78 expected this family to give public rows a better valuation source.
It does not (X4): neither a 13F line nor an N-PORT line carries a market
capitalisation, so public rows are still pinned by a cited market cap.

---

## Results

| | |
|---|---|
| Base rows, all members | **379** |
| Ledger verdicts | 443: 383 member (four absorbed by identity merges), 60 not a member |
| Member evidence | site listing 370 · Form D adjudicated 4 · web 4 (recall additions) · fund filing 1 (Kalshi) |
| Status | private 260 · acquired 55 · public 48 · defunct 12 · unknown 4 |
| Valuation band | below $1B 212 · $1B+ 118 · $10B+ 37 · $100B+ 10 · undetermined 2 |
| Entry stage | Growth 246 · Series A 50 · Seed 25 · Pre-Seed 1 · undetermined 57 |
| Entry stage, share of the 322 known | Growth 76.4% · Series A 15.5% · Seed 7.8% · Pre-Seed 0.3% |
| Head office | US 274 · Europe 40 · China 33 · other 32 · 104 cities |
| Public rows | 48, each with a market cap as of 2026-09-25 |
| `verify` | clean in full mode |

The 60 rows ruled out: 28 on a person's seat or past (T4), 17 listed
positions (D3), 15 others (homonyms, the roster error below, vehicles).

## S2A block

| | |
|---|---|
| Seed entries | 25 |
| Censored (entry younger than 24 months) | 3 (OneText, Dirac, SkyPilot) |
| Cohort | 22 |
| Graduated | 10 |
| Not graduated | 12 (9 by the absence test, 3 by a cited end) |
| **Rate** | **45.5%**, coverage 100% |

The rate rests on 22 rows. One row moving changes it by about four and a
half points. Two of the ten graduations were found only after the first
pass: Norm Ai by the blind re-judgment and Distyl by the stage sweep.

**The absence test failed on its standard surfaces and was repaired
(R5).** The four standard surfaces had recorded Meticulous, Stability AI and
WisdomAI as not graduated. All three had raised a named later round
(Meticulous Series A, July 2026; Stability AI Series B, August 2026;
WisdomAI Series A, November 2025). The first miss surfaced through a vehicle
named "Meticulous Sept 2025" in the Form D data; one web search per row
found the other two. Before the repair the rate read 25%. Every no now
carries a web search line and a Form D name scan that says what each hit is.

## Method deltas

- **The site is an API, not a page.** coatue.com serves its list through
  `/api/portfolio` (372 rows, 48 per call) with two fields per company: the
  initial investment (Venture or Growth) and the status (Active or Exit). No
  dates, no sectors, no team page, no company pages.
- **The firm's label decides Growth and only anchors Venture (D11).** Growth
  labels 178 rows as `first_party`. Venture covers Seed and Series A, so
  each Venture row was judged: 131 stages are cited to a round, 59 rest on
  the model, 11 on the Form D band, and 57 stay undetermined because no
  source names the round.
- **Brand names were fixed at the source.** About 45 renderings on the
  firm's page differ from the brand ("Snap Group", "Mei tuan", "Youxinpai").
  The pull script maps them and keeps the page's rendering beside it. The
  rebuild re-keyed 23 slugs by itself and 5 by hand. Four rows were
  merged into the row of the same company: Jetpack.io into Jetify,
  Kanzhun into BOSS Zhipin, Nomos AI into Norm Ai, Teamflow into Lindy.
- **The archive is thin and says so.** Every capture of `/portfolio` carries
  only the first 48 rows, so the archive dates 86 rows and cannot show a
  removal. The 2024 to 2026 captures are Common Crawl's, taken while the
  Internet Archive was in its machine-wide cooldown; the Wayback pull ran
  when the cooldown ended and added the 2023 capture and no new company.
- **The registered fund's rows could not ride the company layer.** The
  builder forms a filing link from the row's own CIK and an N-PORT is filed
  under the fund's CIK. The rows were taken out again; Kalshi entered as a
  recall addition citing the N-PORT (D4, amended).
- **13F values are scaled by an implied price, not by date.** Coatue's five
  filings of 2001 are in dollars and its 2002 to 2022 filings in thousands.
  The script now reads the median value per share of each filing.
- **Market caps on Hong Kong and Indian pages are in local currency.** Six
  rows were converted at the ECB rate of the day (Guming, Keep, Meituan,
  Swiggy, Mech-Mind, Manycore).

## Recall probe

Five additions, each cited on the ledger: **Lunchclub** (Series A co-led
with Lightspeed, 2020), **Wolt** (the $530M round of January 2021),
**Syrn** (press report, medium confidence), **Firmus** (Coatue led the
$505M round of April 2026) and **Kalshi** (the registered fund's N-PORT).
None is on the firm's page.

113 candidates were rejected with reasons in `sources/web/recall-probe.json`.
The EDGAR full-text sweep returned 1,111 registrants; every operating
company among them that shows a fund position was already a row. The rest
are funds holding Coatue funds, biographies of people who once worked at
the firm, listed positions, and a namesake (Coatue Corporation, the memory
company AMD bought in 2003). Of 51 well-known late-stage deals checked by
name, none showed the firm in a round.

**The gap is reported, not hidden.** The firm's page lists 372 companies and
the base holds 379, so recall rests almost wholly on the firm's own list.
What the list leaves out is the class the probe found: recent deals (Firmus,
Kalshi), exits the firm dropped (Wolt) and small positions (Lunchclub).

## The A/B pass and the standing duties

The visible slice is 173 rows: 125 private rows at $1B or more and 48
public rows. Panther left it on its sale; Kikoff joined it through the
blind re-judgment.

**Pass A, the defence.** Every private $1B+ row carries a priced event with
a citation (125 of 125). Every public row carries a market cap as of
2026-09-25 (48 of 48).

**Pass B, the attack.** 71 marks older than 2025 were attacked for a newer
round, a sale, a listing or a shutdown: 20 in the first web pass and 51 by
three research agents.

| Outcome of the 51 | Rows |
|---|---|
| Acquired | 1: Panther (Databricks, closed August 2026) |
| Newer mark found and recorded | 4: Cadence $1.23B (June 2026), Checkr $5.0B (April 2022), Reify Health $4.8B (April 2022), Side $2.5B (June 2021) |
| A lead that no page confirms, row flagged | 5: Attentive, Chainalysis, Cohesity, Postman, Relativity Space |
| The old mark is still the latest priced event, keeps `stale` | 41 |

The first web pass had already moved eight statuses: Mech-Mind and Manycore
listed in Hong Kong, Stytch, Step and Stash acquired, Gantry and Voltron
Data shut down, Dingdong listed. Checked and kept private: Discord (filed
for an IPO in confidence, not listed), Airtable and Hugging Face (sales
signed and not closed, R3), Monzo (sale talks only) and Relativity Space
(control changed hands in 2025, no valuation stated). The 59 marks dated
2025 or 2026 were not attacked a second time.

**Momentum slice.** 39 private rows in AI, fintech, data infrastructure and
developer tools that read below $1B each carry a dated web check.

**Standing duties.**

1. Every $1B+ claim was checked on the web (above).
2. Every "not graduated" was vetted again after the three misses (R5). The
   three censored clocks are OneText (July 2025), Dirac (August 2025) and
   SkyPilot (July 2026).
3. Weak registrant joins: 17 rows carry `cik_weak`. 14 are public rows
   whose cap comes from the exchange page by ticker. Ghost, Slack and
   Workstream were joined to the wrong registrant and are disputed.
4. Pre-filled values were re-judged, not demoted: 57 were overruled, most
   of them single-word Wikidata joins (Stripe, Spotify and Mercury had been
   read as acquired).
5. No float is stale: all 48 caps are dated 2026-09-25.
6. The unicorn list never bands a row here (Rule A). 68 rows match the
   list by name and each $1B+ row among them rests on its own citation.
7. Every citation address an agent reported was fetched again and checked
   for the name or the city it is cited for (about 80 pages, none failed).
   Then every private $1B+ valuation citation was fetched again (125 of
   125 hold) and every momentum-check citation (39): seven of those named
   another company, taken as the newest headline carrying the name (a
   restaurant called Lindy's, ARCH Venture Partners, Titan Australia, a
   drinks platform called Fero, a home tour, the book app Tome, an
   unreadable page for Karat). All seven were replaced.
8. **The blind re-judgment found real errors.** A research agent that
   saw no file of the run classified 20 random rows afresh, five columns
   each. 93 of 100 cells agreed; 7 cells on 5 rows did not:

   | Row | What the blind pass found | Outcome |
   |---|---|---|
   | Nomos AI | It is the registered name of Norm Ai, already a row | the two rows are merged |
   | Norm Ai | Coatue led the seed round, not only the Series A | entry corrected to Seed, graduated |
   | Take Take Take | a named pre-seed round of June 2024 | stage set to Pre-Seed |
   | Kikoff | the Series A names Coatue; a secondary sale of March 2026 at $1.5B | stage and mark recorded, flagged |
   | Lighter, MoonPay | a different head office city | not settled, both flagged `unstable` |

   Each hit was treated as a class. The registered-name class was swept over
   all members that are not on the firm's page: no second case. The
   renamed-company class gave one more: Teamflow and Lindy, which the firm
   lists under both names, are one legal entity in the founder's words, so
   the two rows are one. The
   undetermined-stage class was swept with one news search per row over
   the 58 rows that carried it (three research agents started it and
   stopped on the account's usage limit, so the session finished it by page
   fetch). Five rows gained a cited round: Distyl (Seed, since graduated),
   OneText and Dirac (Seed), Sourceful (Series A) and Figma (a 2024
   secondary, Growth). Saturn turned out to be sold to Snap in June 2025.
   For Lead Bank, Nate, Swarm Aero and Open a release names Coatue as an
   existing investor or in a combined round, so the entry was earlier but
   no page names it; they stay undetermined with the page cited.

## Debt, all flagged and counted

| Flag | Rows | Meaning |
|---|---|---|
| `stale` | 70 | the mark is older than 24 months |
| `undetermined` entry stage | 57 | no source names the round; 5 of them read $1B+ |
| `model_disputes_source` | 57 | a pre-filled value was overruled with a note |
| `needs_review` | 25 | listed under the open rulings |
| `city_unknown` | 9 | no head office city on record |
| `boundary` | 7 | membership rests on a ruling Erik may overturn |
| `unstable` | 2 | Lighter and MoonPay: the blind pass read another city |
| `stage_uncited` | 2 | Amo, Meticulous |
| `needs_web_value` | 2 | Scala, VIPKid |
| `identity_unresolved` | 2 | DecideHQ, Dialect: excluded from every metric |

Entry dates cover 246 of 379 rows. The firm publishes none, so the rest
have no date.

## Firm profile

| Field | Value | Basis |
|---|---|---|
| Head office | New York, NY | Form ADV principal office, filed 2026-07-29 |
| Founded | 1999 | |
| AUM | $40.5B, a floor | gross assets of the 111 private-markets master funds on the ADV; the firm's regulatory total is $92.7B |
| Funds | 17, of which 12 with a sworn size | the funds' own Form D filings |
| Check size | $3M · $100M · $500M | press-based median over 177 cited entry rounds; a round-size proxy |
| Stages | Seed, Series A, Growth | |
| Scope | Generalist, 8 sectors | derived from the focus column |
| Geography | US core; China and Europe | |
| Notable | OpenAI, SpaceX, Uber, Spotify, Snap | |
| People | 16 | each title from a filing or the firm's own post; socials empty, the firm has no team page. Sri Viswanath was removed, having left the firm in the fall of 2025 (TechCrunch, 2026-03-30) |
| Thesis | the firm's own homepage line, quoted | |
| Icon | the wordmark from the page header, vector | dry run only, preview at `investor/icon-preview.png` |

## Open rulings for Erik

1. **X2**: show the S2A rate only above a cohort floor, or beside its cohort.
2. **X3**: a registered fund's fair value never bands a row.
3. **R1**: a PIPE bought at a SPAC merger is not a venture entry. If it is,
   SoFi, Payoneer, Sunlight Financial and CCC enter as Growth. Hut 8 is out
   on the same reading; Endeavor is kept and flagged.
4. **R2**: three members rest on a director's seat alone: Pill Club,
   Sungage Financial and Fire Pit Collective. The last looks personal.
   (Nomos AI, first read the same way, is Norm Ai and is on the firm's page.)
5. **R4**: equity raised as a valuation floor (DayOne $4.5B, Vantage $9.2B).
   Scala and Commonwealth Fusion Systems read below $1B under Rule A because
   no page states a valuation, which is almost certainly too low for both.
   Kikoff's $1.5B comes from a secondary sale reported in a lawsuit story.
6. **Hedged marks**, flagged `needs_review`: Zuoyebang, Manner Coffee,
   Abogen, Fiture, PingPong, Weidian. **Marks with a lead no page
   confirms**: Attentive, Chainalysis, Cohesity, Postman, Relativity Space.
7. **Covariant**: status against the acqui-hire ruling.
8. **Stability AI**: its $101M first round is named a seed and read as Seed.
9. **Braintrust**: funded by a token sale, flagged `token_funded`.
10. **Syrn**: membership rests on one press report.
11. **27 accepted cross-investor pairs** wait for the wave alignment, listed
    in `companies/cross-rulings.json`. One of them is a duplicate inside
    Khosla's book: its Form D row "Nomos AI" is its own Norm Ai row.

## Errors of this run, corrected

- A Khosla partner was on the curated roster. The name was removed and the
  four Form D rows it had attributed were ruled out.
- Three citation addresses were typed from memory and were wrong. They were
  replaced from real headline links; the emitter now drops a figure whose
  headline it cannot match.
- Four market caps were recorded in local currency as dollars, then
  converted. UiPath's cap was dropped at recording and restored.
- The builder merged Tome's registered name into an unrelated company. The
  merge file now separates them.
- Four entry rounds were wrong in the first pass and corrected from cited
  pages: Avail, Choco, Ramp, Weights & Biases. Norm Ai's was wrong too
  (the blind pass found the seed).
- Databricks carried the February 2026 figure ($134B) under an August date,
  copied from a sibling book; it now reads $190B from the round Coatue led.
- Nomos AI was a second row for Norm Ai, and Saturn read private after its
  sale. Both were fixed.
- Sri Viswanath was listed as a current partner after leaving the firm.
- Teamflow and Lindy were two rows for one company, and seven momentum
  citations named another company.

## Playbook write-back proposed

1. **§6, the absence test**: add one web search per no and a Form D name
   scan for single-deal vehicles named after the company (R5). Measured
   miss rate of the four standard surfaces on this book: 3 of 20.
2. **§5, new layers**: the 13F and registered-fund layers with their config
   keys and tiers as in the table above; D3 as a class-wide rule.
3. **Builder**: accept a filer-side link for a fund filing, so an N-PORT
   position can ride a company row.
4. **§6, market caps**: exchange pages outside the US quote local currency
   with no symbol; convert before banding.
5. **Rule 6**: a city found on a page counts only where the sentence ties
   it to the company. A mechanical match produced five false hits here.
6. **§8, renames**: the rename map follows the near-duplicate rule and
   missed five renames; let it take an explicit map from the run.
7. **§3, full-text sweep**: list a firm's namesakes in the config so their
   hits are dropped before reading.
8. **§7, momentum slice**: a headline found by the company's name alone
   is not an identity. Check the entity before a headline becomes a
   citation; on this book 7 of 39 were another company.

## Usage line

| | Weekly, all models | Weekly, Fable |
|---|---|---|
| Before kickoff | 33% | 5% |
| Early morning, 00:47 UTC | 53% | 41% |
| At close, 14:10 UTC | 74% | 80% |

The run paused for about eleven hours on the account's usage limit and was
finished on Opus 5.5. Base rows: 379. Research agents: 14, of which three
stopped on the usage limit. The session's allowance of 200 web
searches was spent before the attack pass ended, and the agents draw on the
same allowance; the last of them worked through news feeds and page fetches.

## Prompt count

**1** at close: the kickoff ("please collect Coatue"). The ingest approval
was the second.

## Addendum 2026-09-27: the ingest

Erik approved with "ingest". Before writing, `verify` ran again against the
books closed since (Insight Partners, EQT Ventures) and found one new name
collision: Coatue's Root is Root Insurance, Insight's is Root, formerly
Slim.AI. It is ruled `distinct` in `companies/cross-rulings.json`.

**First-time order:**

1. Icon: `fetch-investor-icon.ts coatue sources/site/logo-wordmark.svg`
   uploaded `investors/coatue-17004d54b9.png` (256 px master, contrast
   9.3:1, ramp 0.91 px).
2. Investor row: `ingest:investor -- --investors name=coatue`. The script
   noted "China" as a geography label no investor had used before; the
   vocabulary is open by design and 33 companies sit in China.
3. Companies: the dry run planned 379 new rows and no removal; the ingest
   wrote 379 of 379.

**Readback** (`scratch/readback.ts`, read-only): 379 in the file, 379 live,
0 missing, 0 differing cells. The investor row's computed track record
reads 48 listings, 165 companies at $1B+, 47 at $10B+ and 10 at $100B+, and
S2A 45.5% on a cohort of 22.

**Prompt count 2, final:** the kickoff and the ingest approval.
