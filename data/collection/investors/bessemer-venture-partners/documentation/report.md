# Bessemer Venture Partners: Build & Reconciliation Report (PRO-80)

**Linear issue** PRO-80 · **slug** `bessemer-venture-partners` · display name **Bessemer Venture Partners** · one run
under the merged shape of `data/collection/COLLECTION.md`, one session in two sittings (2026-10-01, parked on the
weekly usage limit, resumed 2026-10-06), self-ingesting through the §9 gate · report written 2026-10-06. Every count
below was taken from the run's files (`companies/base.csv`, the ledger, `excluded.json`, `scratch/verify-3.txt`,
the scratch plans); where a number could not be counted from a file, the text says so.

---

## 1. The answers PRO-80 asked for

**The Company Base is 950 companies (950 members, 0 uncertain), plain `verify` is clean, and the firm profile is
built.** Bessemer is one registered adviser (Deer Management Co. LLC, CRD 159279, $20.24B regulatory assets) with
one venture and growth fund family; its buyout strategy, BVP Forge, and the Bessemer namesakes (Bessemer Trust,
Bessemer Securities, Lindsay Goldberg & Bessemer) are outside the portfolio (D2, D3). Out: 226 rows, all
`not_member` (section 3).

The issue asked three things.

**1. How far back can the base honestly reach?** To 1957 for membership, to about 2008 for the round. The firm
published its own list with an investment year for every company (its 2008 to 2012 site), a sentence per exit, a
2002 "successes" page with the month of each investment, and a history page that names the round for the famous
deals. So membership and the entry year are first-party all the way back. What thins out is everything else:

| Entry era | Rows | On the live site | Entry stage decided | Status unknown | No city | $1B+ today |
|---|---|---|---|---|---|---|
| before 1981 | 22 | 0 | 4 (18%) | 1 | 5 | 1 |
| 1981 to 1994 | 54 | 3 | 8 (14%) | 1 | 7 | 6 |
| 1995 to 2001 | 162 | 8 | 41 (25%) | 29 | 23 | 3 |
| 2002 to 2007 | 119 | 30 | 34 (28%) | 20 | 18 | 3 |
| 2008 to 2015 | 194 | 125 | 141 (72%) | 12 | 4 | 24 |
| 2016 to 2026 | 395 | 348 | 340 (86%) | 4 | 12 | 73 |
| no year | 4 | 0 | 0 | 0 | 1 | 0 |

**The era boundary ruled (D8): there is no cut-off year.** The base makes a membership claim wherever the firm's own
list does. A row from before 2008 is allowed to assert membership, the firm's own entry year, and its outcome where a
source gives one; it asserts a round only where a source names it (R9). **What the debt flags should say**, as they
now do: `undetermined` in `entry_stage` means "the record names no round" (382 rows, 270 of them before 2008), never
"unknown company"; `status: unknown` means "no source says how it ended" (67 rows, 49 of them 1995 to 2007, the
dot-com and optical bust); `city_unknown` (70) and `country_prior` (10, a country inferred from the firm's desk) say
where no source places the company; `pre_spinout` (25) marks the positions from before the 1981 spin-out, in under
delta X1's provisional reading.

**2. Precision of the recall layers against the anti-portfolio.** The firm's page of companies it passed on is still
published (7 stories live; 27 names across its versions since 2000, `sources/site/anti-portfolio.json`). Measured
per layer, as candidates surfaced:

| Layer | Candidates | Anti-portfolio names surfaced | Admitted |
|---|---|---|---|
| The firm's own lists (live and archived) | 1,046 names | 0 | 0 |
| Form D sweep on the roster | 636 issuers | 0 | 0 |
| Bessemer vehicles' own filings | 66 companies | 0 | 0 |
| Wikipedia insource sweep | 150 articles | 0 | 0 |
| EDGAR full-text search | 296 third-party registrants | 3 (eBay, Okta, Zoom) | 0 |
| Recall probe (press, parametric) | 67 leads | 0 | 0 |

The three full-text hits are instructive, not noise: eBay and Okta name Bessemer funds as selling holders because
they paid for Skype and Auth0 in stock (sale consideration, R6), and Zoom names an operating partner as a director.
Triage rejected all three on the filing's own text. So the candidate-level false-positive rate of the widest layer
is 1.0% (3 of 296) and the admitted rate of every layer is zero; the layer that surfaces them is the one whose
candidates the playbook already requires a holder-table reading for. The 27 names (45 name keys) are now
`verify.not_members` traps.

**3. Target of one prompt: three were used** (the kickoff, and two "continue" after the park and an interrupt).

| Done-when item | State |
|---|---|
| Plain `verify` green, only flagged debt | `verify: clean` (`scratch/verify-3.txt`); debt flagged (section 6) |
| Era boundary ruled, visible in flags | D8, R9; the table above |
| Profile through the taxonomy gate | `investor.json` + `sources.json` built; `build-firm-profile` and `profile_copy` pass |
| `review.html` rendered and checked | 950 rows, served at localhost:8931 and checked: rows flat, the profile panel expands with every field's source |
| Cross-investor (rule 10) | 561 shared rows: 560 agree, 1 accepted, 0 disagree after the alignment; 76 sibling rows in 22 books aligned and re-ingested; 93 namesake pairs ruled distinct (sections 9 and 16) |
| Report, close, commit, ingest, Linear, closing message | Done: closing commit `605940c5`, 950 companies live with an exact readback, 22 sibling books aligned (section 16) |

## 2. Results

- **Membership evidence**: the firm's own listing 924 (514 on the live site, 410 archive only), a cited round 22
  (the 20 recall additions and 2 press-corroborated Form D rows), a Bessemer vehicle's filing 3, a director of
  record 1 (Strala, medium, for review).
- **Status**: acquired 422, private 352, unknown 67, public 58, defunct 51.
- **Valuation**: below $1B 838; $1B+ 110, of which $10B+ 20 and $100B+ 3 (Anthropic, Shopify, Waymo); 76 private
  and 34 public; 2 rows undetermined (unnameable). Every public row carries a market cap of 2026-10-06.
- **Entry stage**: Growth 239, Series A 208, Seed 118, Pre-Seed 3, undetermined 382. Sources of the 568 decided:
  a cited round 251, the firm's own words 164, a round named from knowledge 91, the Form D band 62.
- **Countries**: US 740, India 61, Israel 57, UK 28, Canada 19, 45 elsewhere.

### S2A block

118 seed entries, 22 censored, **cohort 96, graduated 66, not graduated 30, rate 68.8%**, coverage 100%. The nos
rest on Form D absence 2, a cited end (sale or shutdown) 10, and the absence test of 2026-10-06 on 18. The cohort is
recent by construction: 108 of the 121 Seed and Pre-Seed entries are from 2008 on, because a seed before that is
only labelled where the firm's own text says "seeded". Zapier counts as graduated on its 2021 secondary at $5B
(R10).

## 3. The boundary

Derivations D1 to D10 and delta X1 were posted at kickoff; rulings R1 to R14 were made in the run
(`documentation/decisions.md`). The 226 excluded rows:

| Class | Rows | Rule |
|---|---|---|
| Form D name match with no Bessemer fund (homonyms, operating partners' own seats, seats after the person left, two personal investments) | 166 | §1 evidence rules, D4, D6 |
| Control positions (Netsmart, TeamViewer, LogicNow / GFI, ThreatTrack, GTS, Litify, Medi Assist, WiredScore, Syncsort, Metalogix, CRI, Harman, LiveAuctioneers, Beyond, Current, with their name variants) | 19 | R1 |
| Stock received for a portfolio company (Insmed, Ola, Gentle Dental, VTS, HomeLight, Voyant, Cogent, with variants) | 14 | R6, R13 |
| Bought when already listed (Shriram City, Anant Raj, Ganesh Housing, Riddhi Siddhi, Tulip Telecom, Rico Auto, Centocor, Commercial Federal, Portrait Software, James River) | 11 | T3, R3 |
| The Forge team's prior-firm companies on one 2022 capture | 11 | R4 |
| Funds and company-creation vehicles (KCM Biomedical, New Vernon Capital, Rock Health, Team8, Argnor) | 5 | D7 |

Two corrections to the kickoff derivations, both made before any row depended on them: the Gator Co-Invest
vehicles are BVP Forge's, not the venture funds' (R5; D1 and D7 corrected), and the eleven prior-firm companies
were on the firm's main list, not only on the Forge pages (R4).

## 4. Coverage per evidence layer

- **Live site**: bvp.com is Next.js over Sanity; the dataset's public query API returned every `company` (534),
  team member (315) and post (537, including 19 investment memos). The CMS `stagePartnered` field is a migration
  default ("seed" on 500 of 534) and was never used as a label (D9).
- **Archive, 2008 to 2026**: Common Crawl, 128 crawls, six site generations parsed
  (`scratch/bvp-parse.py`). The 2012 to 2015 generation printed the investment year one year early wherever the
  stored date was a January 1 placeholder; corrected at the parse for 98 companies (301 rows).
- **Archive, 1999 to 2007**: Internet Archive (`scratch/ia-pre2008.py`): the one-page portfolio 2002 to 2007, the
  2002-03 successes page, the anti-portfolio 2000 to 2006, and 26 of the 45 per-practice pages of 1999 to 2001.
  **110 companies the 2008 to 2012 list had dropped** came from here. **Debt: 19 practice pages unfetched** (the
  archive put this machine in cooldown three times; the fetch is still queued). The 2002 page covers every company
  still held in June 2002, so what can be missing is a company that entered and left between 1999 and mid-2002 and
  sat only on those 19 pages.
- **EDGAR**: 152 entities by desk (75 venture, 13 Forge, 64 external namesakes); Form D sweep 1,342 accessions on
  636 issuers; 66 companies on the vehicles' own ownership filings; full-text search 436 registrants.
- **Recall**: full-text triage (195 registrants not in the base: 2 additions, 7 acquisition targets, 6 of which the
  1999 to 2007 archive then listed anyway); the probe (14 additions, all 2020 to 2026, plus the Forge deal list
  and the single-deal vehicle decode); the firm's history page (Measurex, Fotomat, Interdata, R2). 20 recall
  additions landed.
- **Form ADV**: 54 private funds on Schedule D 7.B.(1), $20.26B gross.

## 5. Method deltas

1. The firm's own history narrative and successes page were parsed into a source file and shown to the judge as
   first-party stage evidence (`sources/site/history-narrative.json`).
2. The anti-portfolio was used as a negative control per recall layer (section 1).
3. A second pass re-judged the 285 rows that four Sonnet judges had left without a stage or status, after the
   1999 to 2007 text was in: 121 stages and about 40 statuses decided.
4. The rebuild ran under `record`'s lock while judges were recording (`scratch/rebuild-locked.py`).
5. Single-deal vehicles were assigned to a desk by their Form D related-person list (R5).
6. Entities were assigned to desks by filing address before any name pattern (`scratch/entity-addresses.json`).

## 6. Flags and debt behind `verify`

`stale` 76 (private marks older than 24 months, each kept on its last priced round); `city_unknown` 70;
`model_disputes_source` 52 (a prefilled value the judge overruled with evidence); `stage_disputes_band` 33;
`cik_weak` 30 (audited, section 7); `unicorn_name_match` 28; `pre_spinout` 25; `country_prior` 10; `cite_pending` 5
(abridge, nydig, ual, upside, docusign: a $1B+ row whose entry round no page names); `stage_uncited` 4; `boundary`
3; `identity_unresolved` 2 (Domain, FG Wireless: a bare name on the firm's list). 89 stale classification keys
from earlier base versions are tolerated by `verify`. Known soft spots: 91 stages rest on a round named from
knowledge; about 60 cities are from memory; 16 of the 30 graduation nos and six of the yeses on pre-2005 rows are
at low or medium confidence.

## 7. Standing duties and the A/B pass

- **A/B** (four judges): 76 private rows at $1B or more defended and attacked (about 20 marks re-pinned from the
  unicorn list to the round's own announcement; Devo, Abridge, Axonius, BigID re-priced); 60 public rows priced from
  StockAnalysis on 2026-10-06 (Yelp fell under $1B; Snapdeal listed on 2026-10-05 as AceVector; Flex Pharma and
  Proteon read acquired); the momentum slice of 80 rows carries a dated check on every row (no band changes;
  Intercom acquired by Salesforce on 2026-09-10).
- **Duty 6**: 50 unicorn-list name hits, 44 already banded or exited, the rest namesakes or settled.
- **Duty 3 and 8**: the 30 weak registrant joins read one by one; the judged row overrides the float wherever the
  registrant is a namesake or the company left the market (Rev, Guild, Courier, nCino, Urban Company).
- **Duty 7, the blind 5% sample** (48 rows re-judged without the stored answers): valuation band 48 of 48 agree,
  status 45, country 47, city 39, stage 42. **Duty 9, the class it exposed**: stages read off "first institutional
  round" wording, a convention the playbook retired; 36 stages returned to undetermined across the base (R9).
  Three rows were corrected from the sample itself (Zany Brainy acquired, DataHub Palo Alto, Aivar Coimbatore).

## 8. Corrections taken

None from Erik during the run. The run corrected itself seven times, each recorded: the Gator vehicles (R5), the
eleven prior-firm rows (R4), Sorare (R12, on Erik's earlier ruling), The Exploration Company (R11), the ordinal
stages (R9), the MicroAcquire graduation two judges decided two ways, and three overlays the rebuild's rename
step moved onto the wrong rows (section 12).

## 9. Cross-investor (rule 10)

Three triage passes decided 185 pairs: **93 namesakes ruled distinct**, 9 where this book was stale (corrected
here), 7 accepted (five in the in-flight General Catalyst book with the value owed in the note, one unnameable
Battery row, Exclara), and **76 sibling rows in 22 books stale against this run's cited evidence** (status after
an acquisition or shutdown, a newer priced round, a market cap across the $1B edge, a wrong country or city). The
kits are `scratch/align/<book>.jsonl`; the outcome per book is in section 16. Every column was compared, not only
status and band (COLLECTION.md §9).

## 10. Firm profile

Thesis “Forged in steel. Building what's next.” (the homepage headline). Founded 1981 (the spin-out; the firm also
claims 1911, the family office). HQ Larchmont, NY (the Form ADV principal office, on the firm's own office list).
AUM $20,239,213,324 at both ends (Item 5.F, 2026-05-13; it includes $1.25B of BVP Forge, flagged). 12 funds from VII
(2007) to XIII and Century Fund III (2026), none with an asserted Form D amount. Stage Seed, Series A, Growth; geo
US core, India, Israel, Europe, Canada; Generalist with nine focus sectors; range $1M / $16M / $450M (the ceiling is
a round it led, Inertia Enterprises, not a cheque). Notables LinkedIn, Pinterest, Shopify, Skype, Twitch. 58
investors published, 48 with a link (82.8%; two search-verified). Icon: the header mark as SVG, dry run passed,
uploaded at ingest. Ten reviewer flags are in `investor/sources.json`.

## 11. Open rulings for Erik (three)

1. **Positions from before the 1981 spin-out (X1).** In, provisionally, where the firm's own list carries the
   company (25 rows flagged `pre_spinout`, among them Gartner, Ungermann-Bass, Maxim's predecessors and Measurex).
   The other reading: the family office's money was not a fund of the firm, so all 25 leave.
2. **"Growth buyout" on the firm's own label alone.** LiveAuctioneers, Beyond and Current are out because the
   firm's partner page calls them growth buyouts (R7, R1); no source gives the stake. Litify and CRI are out on
   press that states the majority. The other reading: without a stated majority the listing stands and the three
   return as Growth entries.
3. **Headquarters.** The rule publishes Larchmont, NY, the sworn principal office, which the firm's own office
   list includes. If the page should say where most of the investing team sits (San Francisco and Redwood City),
   that is a `profile.hq_override`, and the rule's text would need a line for firms whose principal office is the
   back office.

Decided in the run and not asked: Ualá's identity (R8), Zapier's graduation (R10), The Exploration Company's mark
(R11), the merger rows (R13), the country and city of 30 shared companies (section 9).

## 12. Rebuilds and deltas

Two rebuilds, as scheduled. The first (1,095 to 969 rows) removed 214 exclusions, merged 51 duplicates and landed
130 new rows (110 from the 1999 to 2007 archive, 20 recall additions). Its rename step moved the overlays of three
unrelated departing rows onto resurfaced name variants of excluded companies; restored from the backups by hand
(R14). The delta grind judged the 130 rows and decided the 44 open graduations. The final rebuild (969 to 950)
removed the 12 rows the delta ruled out and seven more duplicates, with no renames.

## 13. Playbook write-backs proposed

Not applied: `COLLECTION.md` carries another session's uncommitted edit and the scripts belong to the tooling
session. The full text is `scratch/writeback-notes.md`; in brief:

1. §5 archive: a historical list that reads complete still omits the failures; the era's own captures are owed.
2. §5 site: parse a history or successes page as first-party stage evidence.
3. §5 archive: compare the investment year across site generations (the January 1 time-zone shift).
4. §8 rebuild: `rekey_overlays` must not match a departure to an arrival on a listing URL shared by many rows, and
   never when the departure is a merge duplicate or an exclusion; better, the build should carry an exclusion to
   every name variant.
5. §8: a `run.py rebuild` that holds `record`'s lock.
6. §3: a row seen in exactly one capture, with none of the fields its neighbours carry, is checked against the
   firm's team pages for partner-carried companies before it is seeded.
7. §5 recall: where a firm publishes an anti-portfolio, use it as a negative control per layer.
8. §8 budget: the stage research needs the strongest judge; a cheaper judge leaves the column empty.
9. §1: single-deal vehicles take their desk from the Form D related-person list.
10. §12: disk space and the weekly usage limit are run constraints to check before each wave of agents.
11. §3 briefs: forbid bare requests to web.archive.org by name while the archive is in cooldown.
12. §6: say in the entry-stage section that "first institutional round" and ordinals are not round names, next to
    the retired convention, so a brief cannot reintroduce it.

## 14. Usage line

950 base rows. First sitting (2026-10-01, Fable lead and Fable judges, then Sonnet): weekly all-models 73% at
kickoff, 95% at the park; Fable weekly 8% to 46%. Second sitting (2026-10-06, after the weekly reset, Opus lead and
judges): weekly all-models 1% at the resume, 13% at close; Fable weekly 0% to 4%; the five-hour window 27% at
close. So the run cost about 34 points of weekly allowance in all (22 on the Fable sitting for the first 932
judgments, 12 on the Opus sitting for everything after), roughly 0.036 points per company. WebSearch: about 160 of
the session's 200 calls.

## 15. Prompt count

**3** (the kickoff; "continue" after the usage park; "continue" after an interrupt). Target was one.

## 16. Ingest

**Bessemer (first ingest), 2026-10-06, through the §9 gate, no approval prompt.** Preconditions: plain `verify`
clean, `run.py close`, closing commit `605940c5`. Icon uploaded (`fetch-investor-icon.ts`, the header mark as SVG:
contrast 13.0:1, ramp 0.82 px). `ingest-investor.ts`: 1 record upserted (it added "Canada" to the database's
geography labels; eight other books already publish it). `ingest-companies.ts --dry-run`: "950 row(s) upserted
(950 new), 0 removed, from 0 live", so the removal check had nothing to explain. Write: 950 of 950. **Readback:
csv 950, live 950, missing 0, extra 0, differing cells 0.** The icon URL and the ingest logs are commit `35801b89`.

**Sibling alignment, the same day** (`scratch/align/run-align.py`, then two repair passes; results in
`scratch/align/results.txt`, `results2.txt`, `results3.txt`). Every book: its own `verify` clean before, readback
before exact, the kit recorded, `verify` clean after, dry run with 0 removals, write, readback after exact, one
commit of its three company files.

| Pass | Books aligned (rows) |
|---|---|
| 1 | 8vc (3), accel (3), battery-ventures (6), benchmark (2), coatue (1), first-round-capital (1), headline (1), insight-partners (7), lux-capital (1), menlo-ventures (4), new-enterprise-associates (2), redpoint-ventures (3), sequoia-capital (3), tcv (1), thrive-capital (1) |
| 2 | greylock (5), after a country citation was added for Upwind, which the kit lifts to $1B+ |
| 3 | a16z (6), cherry (1), khosla-ventures (6), lightspeed (12), spark-capital (1), y-combinator (6) |

**22 books, 76 rows.** What the repair passes fixed, none of it skipped: a row lifted to $1B+ outside the US needs
its country citation in the same line (Upwind, Sarvam, The Exploration Company); Cherry verifies with
`--skip-links` (no EDGAR link to sample); Y Combinator's readback shows one missing and one extra row that are the
same name after trimming (" Metadata"), which is exact; and five books fail rule 10 against each other until all of
them carry the shared company's new value, so they move together.

Not written: the in-flight books (atomico, bain-capital-ventures, founders-fund, general-catalyst, speedinvest).
Five General Catalyst pairs are parked as `accepted` in `companies/cross-rulings.json` with the value owed (Shift
Technology's country, Visor's status, ClickHouse's city, HiBob's mark, an unidentified Rabbit row). After the
alignment Bessemer's own `verify` reads 561 shared rows, 560 agree, 1 accepted (Exclara), 0 disagree
(`scratch/verify-4.txt`).

**Debt carried out of the run**: the 19 sector pages of 1999 to 2001 still owed by the Internet Archive
(`scratch/ia-owed-pages.json`; `python3 scratch/ia-pre2008.py --people-only`, then `bvp-parse.py`, a rebuild and a
small delta); the three rulings of section 11; the playbook write-backs of section 13.
