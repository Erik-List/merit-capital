# Balderton Capital: Build & Reconciliation Report (PRO-106)

**Linear issue** PRO-106 (sub-issue of the PRO-87 wave umbrella) · **slug** `balderton-capital` ·
one session, one run, under the merged shape of `data/collection/COLLECTION.md` · report written
2026-09-27. **Nothing is ingested.** Ingest waits for Erik's explicit approval (order for a
first-time investor: icon upload, `ingest-investor.ts`, `ingest-companies.ts`).

---

## 1. The answer PRO-106 asked for

**The base is 281 companies, plain `verify` is clean, and the Benchmark Europe boundary is ruled:
the London desk's book of 2000 to 2007 is Balderton's.**

| Done-when item | State |
|---|---|
| Plain `verify` green with only flagged debt | Clean on 281 rows (section 6 lists the flags) |
| Benchmark Europe boundary ruled, dated, recorded | `decisions.md` D2 (2026-09-26), 46 rows on the desk pages, merges in `identity-merges.json` |
| Coordination with PRO-88 (Benchmark) | Rows copied from PRO-88's parsed captures with their capture URLs; dual-held rows agree under rule 10 (0 disagreements) |
| Distributions checked against Cherry and Creandum | Section 3 |
| Profile through the taxonomy gate | `investor/investor.json`, `profile_copy.py` ok |
| `review.html` rendered | Served and checked, rows flat, profile panel expands |
| Archetype-B corrections proposed to PRO-87 | Section 9 |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 281 | |
| Private | 129 | 46% |
| Acquired | 112 | 40% |
| Defunct | 24 | 9% |
| Unknown | 12 | 4% |
| Public | 4 | 1% |
| $1B and above | 21 | 7.5% |
| of which $10B and above | 2 | Revolut $115B, Lovable $13.3B |

Entry stage: Series A 100, Growth 77, Seed 38, Pre-Seed 5, round not on record 59, company not
nameable 2. Headquarters: United Kingdom 111, United States 52, Germany 34, France 23, Sweden 14,
Ireland 7. Evidence tiers: A 175, B 92, C 14. Membership rests on the firm's own listing for 265
rows, on a fund in a filing for 7 and on press for 9.

`defunct` is undercounted by construction (COLLECTION.md §6): the column is the last known state,
not a mortality rate.

### S2A block

Of 38 seed entries, 2 were too recent to count (Cino, Mozart). Of the 36 that remain, **50.0%**
raised a later round (18). Of the 18 that did not, 7 rest on a cited end (a sale or a closure) and
11 on a dated search of the named surfaces. None rests on the Form D filings.

| Seed entries | Censored | Cohort | Graduated | Rate |
|---|---|---|---|---|
| 38 | 2 | 36 | 18 | 50.0% |

The cohort is small because Balderton enters at Series A and later: 80% of the staged rows are
Series A or Growth.

## 3. Calibration against Cherry and Creandum

| | Balderton | Creandum | Cherry | Atomico | Point Nine |
|---|---|---|---|---|---|
| Rows | 281 | 177 | 148 | 164 | 199 |
| $1B and above | 7.5% | 10.7% | 5.4% | 19.5% | 7.0% |
| Acquired | 40% | 28% | 16% | 29% | 28% |
| Defunct | 9% | 6% | 7% | 10% | 9% |
| Seed and Pre-Seed entries | 15% | 48% | 78% | 11% | 87% |
| Round not on record | 22% | 2% | 11% | 26% | 3% |
| S2A rate | 50.0% | 52.1% | 62.7% | 46.2% | 55.2% |

Three readings. The acquired share is the highest of the five because the book reaches back to
2000 and the desk-era companies have had 20 years to be sold. The stage mix matches Atomico, the
other Series A and growth firm, and not the two seed firms. The share of rounds not on record is
high for the same reason as Atomico's: 68 rows were first seen before 2010, on pages that carry a
name and a link and nothing else.

## 4. Coverage per evidence regime

| Layer | Rows it reaches | Note |
|---|---|---|
| Live list (balderton.com/companies, 205 cards) | 203 | Hidden post type; read through `?_paged=N` |
| Archived balderton.com listings 2012, 2013, 2015 to 2023 | 215 | Common Crawl, eleven listing years, 251 names |
| benchmark.com Europe desk pages 2001 to 2009 | 46 | Copied from PRO-88's captures |
| The firm's news archive 2014 to 2026 (552 posts) | entry citations for 82 rows | 116 rows carry a cited entry round in all |
| The firm's pre-2014 news archive (497 posts, 2012 and 2013 captures) | 4 new rows, 3 entry stages, 9 entry dates | Posts from 2000 to May 2013 |
| Form D roster sweep | 30 | 18 name-match rows ruled out (namesakes, seats from a prior or a next firm) |
| EDGAR full-text sweep | 3 recall rows, 7 sale-consideration traps | |
| UK share register | 24 companies read, 17 with a fund of the firm on a list | New layer, R3 |
| UK officer graph | 291 appointments, 21 partners | Extended from 211, R4 |
| Wikipedia insource sweep | 225 articles, 3 recall rows | |
| Recall additions | 23 (22 rows after one merge) | |

**78 of the 281 companies are not on the firm's live list.** They came from the archive, the
registers and the recall probe. The live list of a 25-year-old firm carries its survivors and its
famous exits and drops most of what failed.

**The Internet Archive was not used.** It was under the machine-wide cooldown for the whole run
(to about 02:05 UTC on 2026-09-27). Common Crawl stood in: its crawls of 2012 to 2024 carry the
listing pages, and its 2012 and 2013 crawls carry the firm's news archive back to 2000. One gap
remains. The 2009 and 2010 portfolio page loaded its companies by script, and no capture holds
the list. The desk pages to 2009, the 2012 listing and the news archive bracket those years, so
the blind spot is a company added after 2009, removed before February 2012 and never named in a
post. A later Internet Archive pull can test that; it is listed as debt, not as a finding.

## 5. Method deltas

1. **The boundary (D2).** Balderton Capital (UK) LLP is Benchmark Management (UK) LLP renamed on
   2007-06-11 (Companies House OC306910). Same partnership, same funds (Benchmark Europe I to III
   became Balderton Capital I to III), so the desk's book is inherited, with its rows cited to the
   benchmark.com captures.
2. **The hidden list.** The `company` post type is excluded from REST and sitemaps, and the
   FacetWP endpoint refuses scripted calls. `GET /companies/?_paged=1..9` renders server-side.
3. **The card's round label** ("Series A in 2019") scored 88 of 95 against documented rounds
   (92.6%) and is used at `medium` (D11). Known misses are overridden with `stage_disputes_band`
   (MySQL, Sketchfab, Vivino, Ramp, Deepset, Curious AI Company, Banjo).
4. **The UK share register as a membership layer (R3).** A confirmation statement or annual
   return lists every shareholder. Where it lists a fund of the firm, the position is proven at
   filing grade and the share class is on record. `scratch/ch-shareholders.py` reads the filings,
   scanned ones through the system's text recognition. It found four current holdings the firm
   does not list (Hook, Cognism, Cherryz, Tilt) and proved eleven dropped ones. It also separates
   a firm seat from a personal one: no fund on the list means a personal seat (Oxford
   Nanoimaging, Grind, Player X, Goldjobs).
5. **Officer records (R4).** One person has several officer records on the register. The first
   graph followed one per partner and missed 80 appointments.
6. **Common Crawl without its index server.** The server answered nothing all evening. The index
   is also a set of static files: a binary search over `cluster.idx` with range requests finds the
   block, one more request returns the index lines (`scratch/cc-cluster.py`, about 30 small
   requests per crawl).
7. **The pre-2014 news archive.** The 2012 and 2013 captures of `/news/archive/<company>` list
   the firm's posts back to 2000 with date and excerpt (497 posts). They named Igglo, Whisher,
   Power Challenge and Zubka, which no list carries, and gave the entry round of Sulake, Gemvara
   and InnerWorkings.
8. **Register status.** Thirteen rows that read `unknown` were settled from the UK register and
   from the companies' own posts (section 7).
9. **Ordinal round words (R5).** A third round or later reads Growth. A first or a second round
   straddles two stages and stays an anchor.

## 6. Flags and debt behind `verify`

| Flag | Rows | Meaning |
|---|---|---|
| `model_disputes_source` | 29 | A deterministic pre-fill was wrong and is overridden with a note |
| `stage_disputes_band` | 20 | A documented round overrides the card or the Form D band |
| `stale` | 12 | A private mark older than 24 months, or a float of a company since sold |
| `cik_weak` | 5 | A registrant join on the name alone; nothing is taken from it |
| `city_unknown` | 5 | Looked for and not found |
| `country_prior` | 4 | Country inferred, low confidence |
| `stage_uncited` | 4 | Stage at low or medium confidence without a citation |
| `identity_unresolved` | 2 | Activiti, Visual Media |
| `unstable` | 1 | Curious AI Company (the blind re-judgment disagreed) |

No `cite_pending`. Two stale classification keys (`cas-services`, `globoforce`) belong to rows
that left the base. Rows excluded and preserved in `excluded.json`: 24 (20 `not_member`, 3
`control_position`, 1 `build_filter`).

## 7. Standing duties and the A/B pass

- **A/B pass** on the visible slice (24 rows that are $1B and above or public): every mark and cap
  carries a citation and an as-of date.
- **Momentum slice**: 53 recent rows in hot sectors, one web check each. It caught four events
  after the judge's knowledge: GoCardless (Mollie, closed 2026-09-01), Contentful (Salesforce,
  closed 2026-09-01), Prior Labs (SAP, 2026-07-17), Exein ($1.7B, 2026-09-15).
- **Blind 5% re-judgment**: 14 rows, 75 values, 3 disagreements, all on one row (Curious AI
  Company). The class behind it, status `unknown`, was then swept: 17 rows, 13 settled.
- **Weak-join audit**: 13 rows where a deterministic layer wrote a status or a figure. Sunrise,
  Tilt, Hook and Lemon were joined to other entities and are quarantined.
- **Unicorn list re-intersection** with loose names: 16 matches, none missed.
- **Citation audit**: 19 citations I had completed or typed from memory were wrong and were
  replaced from disk. Every citation since is read from a tool result or a file by key.
- **Cross-investor (rule 10)**: 81 shared rows, 71 agree, 10 accepted (Balderton's side is
  fresher), 0 disagree. 32 homonym pairs ruled distinct.

## 8. Firm profile

| Field | Value | Basis |
|---|---|---|
| Thesis | “Europe's leading venture firm focused exclusively on backing European-founded tech companies.” | The site's title tag, read 2026-09-26 |
| Founded | 2000 | As Benchmark Capital Europe; independent June 2007 |
| Headquarters | London, United Kingdom | Form ADV principal office; the site agrees |
| Assets | $8,511,214,328 | Sum of 16 private funds' gross assets, Form ADV Section 7.B (exempt reporting adviser, no Item 5.F). The site says "$5.7bn" raised |
| Funds | 12 | Benchmark Europe I (2000) to Balderton IX and Growth II (2024) |
| Entry round | median $14.0M, range $1M to $50M | 77 entries announced by the firm with a stated size |
| Stages | Pre-Seed, Seed, Series A, Growth | |
| Geography | core Europe, other US | |
| Scope | Generalist | Focus recomputed: Consumer, SaaS, Fintech, AI, Healthcare |
| Notable | Revolut, Depop, Betfair, Lovable, Wayve | All five are members |
| People | 48 | The site's team cards |
| Icon | Footer mark (vector) | Dry run passes: contrast 12.4:1, ramp 1.60 px. Upload runs with the ingest |

## 9. Archetype B: what held and what did not (for PRO-87)

Held: the firm's own lists as the anchor; the announcement archive as a class-1 entry layer;
`fx-convert` on ECB rates; the market-cap rule for listings outside the SEC; Form ADV Section 7.B
as the AUM anchor; the exit-side EDGAR sweep for sale-consideration traps.

Did not hold, or needs a correction:

1. **"UK: officer graph only" undersells the register.** The share register is a backtrace that
   works per company and names the fund and the share class. It should be a standard layer for
   every firm with UK companies, run on every officer-graph seat the lists do not explain.
2. **A live list is not the book for an old firm.** 28% of this base is not on it. The archive
   and the register carry the recall, and the recall probe was load-bearing, not a formality.
3. **The officer graph needs the union of a person's records**, or it misses a quarter of the
   seats.
4. **Common Crawl is usable when its index server is not**, through the static index files.
5. **The Form D layer is thin but not empty** for a European firm: 30 rows, and its name-matches
   need the tenure filter (31 ex-partner rows removed by the build).

## 10. Open rulings for Erik

1. **D2**: the Benchmark Europe book of 2000 to 2007 counts as Balderton's (46 rows).
2. **R2, control positions out**: Alphyra (63% of the 2003 buyout vehicle), NASN (joint venture
   with Setanta) and CAS Services, which is Clinical Solutions (consortium buyout of 2005 with
   Bridgepoint and Allco). The firm lists all three as portfolio companies.
3. **R1**: Codemasters stays a member on its 2005 minority entry, although control followed.
4. **RTT out** under the ruling of 2026-09-06: Balderton entered through the December 2007
   capital increase of an already listed company and the firm's page names no round. The firm
   lists it with a $250M exit.
5. **R5**: a "third round" reads Growth; "first round" and "second round" name no stage.
   Applied to Sulake; Kobalt, Ricall, 3V, Igglo and Audium stay open.
6. **R3**: a fund on the share register is membership. It adds four holdings the firm does not
   publish (Hook, Cognism, Cherryz, Tilt). A share class labels a stage only where it names a
   series.
7. **US companies on the firm's own 2013 page stay members** (Ingenio, Tabula, Terrapass, Next
   New Networks, Friend.ly, Matrix Semiconductor), also where Benchmark's book lists them.
8. **D6**: Odyssey Therapeutics out as sale consideration, Rahko in.
9. **Two desk-era rows cannot be named** (Activiti, Visual Media) and read `undetermined`.
10. **Stages at medium confidence without a citation**: Wonga and WorldStores read Series A from
    model knowledge of the deal (flag `stage_uncited`). The register's "A" share class only
    supports it and is not the label.
11. **Status calls at medium confidence**: Curious AI Company (reported bought by Apple), Hubilo,
    Tempow, Lyst; Jolt stays `unknown`.
12. **Published names**: Jokr, Roli, Arive, Riff, Smol, Dash0, Trawa, Archify, KupiVIP,
    My-Wardrobe (`config.json` `names.published`).
13. **Feast Kitchen is Simple Feast** (merge at medium confidence); **The Exploration Company** at
    $2B (low confidence); **Premialab** moved its headquarters to the UAE.
14. **Repository**: commits cfc7985 and 7a99878 carry about 30 MB of raw register documents and
    captures. They were moved out of the tree in 437b61a. Dropping them from history before the
    next push is Erik's call.

## 11. Rebuilds and deltas

| Step | Rows | What landed |
|---|---|---|
| First build (kickoff) | 271 | Live list, desk pages, Form D, EDGAR |
| The one scheduled rebuild (01:03 UTC) | 279 | 19 recall additions, archived listings, 31 merges, 23 exclusions; delta of 39 rows judged |
| Second rebuild (01:13 UTC) | 281 | RTT out, 3DHubs merged into Hubs, four rows from the archived news |
| Third rebuild (01:21 UTC) | 281 | The 2012 listing year; Habbo merged into Sulake, SCVNGR into LevelUp; no new row |

The second rebuild follows §8 (a membership verdict in the delta needs a final rebuild). The third
landed an archive year that arrived late and changed no row count. Three rebuilds is two more than
the playbook schedules; the cause was the archive outage, which split the archive layer into three
arrivals.

**Defect found in the rebuild.** `rekey_overlays` paired the departing row `lemonade-inc` (a
`not_member` name-match) with the arriving recall addition `lemon` (Lemon, Inc., a different
company) and moved the verdict. Lemon would have been excluded on the next build. Restored by hand
and guarded with a `never_merge` pair.

## 12. Playbook write-backs proposed (not applied mid-wave)

1. §5 UK row: the share register reader as a standard layer (R3), with the rule that a list that
   cannot be read is recorded as failed.
2. §5: a person's officer records are unioned on name and birth month (R4).
3. §5: Common Crawl's static index route, for when the index server does not answer, and the
   ARC format of its 2008 to 2012 crawls. This also corrects memory: Common Crawl reaches back
   to 2009 for some sites, not only to 2013.
4. §5: a successor firm inherits the predecessor desk's rows from the sibling run's parsed
   captures, with the capture URL per row; mixed desk pages are never configured as eras.
5. §5: FacetWP sites render server-side under `?_paged=N`.
6. §8: `rekey_overlays` must not pair a departing `not_member` row with an arriving recall
   addition; at least it should refuse where the two names differ after normalisation.
7. §8: the first base build should write the in-flight marker (credited to the Atomico session,
   whose `verify` compared against this book's unclassified rows).
8. §8: `record` refuses a verdict for a slug the next rebuild will create. Either it accepts one,
   or the playbook says that such rows go through `rejects` and the parsed-source name map.
9. §3: a judge never completes a truncated URL; citations are read from disk by key.
10. §6 and `stage_words.py`: ordinal round words (R5).
11. §11: `graduation-surfaces.py` needs `investor/investor.json` to exist, which a fresh book does
    not have.
12. data/README.md: raw register documents and raw captures belong under `data/filings/`.

## 13. Usage line

| | 5-hour | Weekly, all models | Weekly, Fable |
|---|---|---|---|
| Kickoff | 41% | 33% | 5% |
| 2026-09-27 00:05 UTC | 86% | 44% | 25% |
| 2026-09-27 01:16 UTC (new 5-hour window) | 47% | 58% | 50% |

The account is shared with four sibling sessions (Atomico, Point Nine, Coatue, Insight Partners),
so the figures are the wave's, not this run's alone. Base rows: 281. Web searches: about 115 of
200.

## 14. Prompt count

**1** (the kickoff). The count is final only after the ingest decision.

## 15. Ingest request (not run)

On Erik's approval, in this order: the icon upload, then `scripts/ingest-investor.ts`, then
`scripts/ingest-companies.ts` with a dry run first.

```bash
npx tsx scripts/fetch-investor-icon.ts balderton-capital https://www.balderton.com/wp-content/uploads/2023/10/logo-footer.svg
```

Balderton is a first-time investor, so the companies ingest removes no rows from the database.
