# EQT Ventures: Build & Reconciliation Report (PRO-163)

**Linear issue** PRO-163 · **slug** `eqt-ventures` · one session, one run, under the merged shape of
`data/collection/COLLECTION.md` · report written 2026-09-27. **Ingested on 2026-09-27 with Erik's approval** (last section), after his ruling on
Docly took the base from 138 to 137 companies.

---

## 1. The answer PRO-163 asked for

**The base is 137 companies, plain `verify` is clean, and the desk partition is ruled: EQT Ventures
is the three EQT Ventures funds, and EQT Growth is another desk.**

| Done-when item | State |
|---|---|
| Plain `verify` green with only flagged debt | Clean on 137 rows; 0 cross-investor disagreements (section 6 lists the flags) |
| Desk partition in `decisions.md` with the registrations it rests on | D1 to D3: CRD 288390 (EQT Fund Management S.à r.l.), the Section 7.B fund records per vehicle, the GP entities in EQT AB's subsidiary list |
| EQT Growth ruled before judging | D2, `other_desk`, written at kickoff; 16 Growth companies moved out; Wolt a member through its 2016 Ventures I entry |
| Sweden gives status only | D8: no Swedish register was used as a membership layer |
| Profile from EQT AB's annual report, the parent's total never in `aum` | Section 8; the recipe is write-back 1 in section 12 |
| fx and non-US-listing constants on every row | Every EUR, SEK and GBP figure converted at the ECB rate of its own date (fund sizes, the check range, the entry rounds, Instabee's mark) |
| Profile through the taxonomy gate | `investor/investor.json`, `profile_copy.py` ok, `build-firm-profile.py` clean |
| `review.html` rendered | Served on the review surface (port 8931) and checked: 137 rows after the Docly ruling (138 at close), profile panel with every field, no console errors |
| report.md | This file |
| Closing message with the ingest request | Sent; approved and ingested 2026-09-27 |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 137 | |
| Private | 104 | 76% |
| Acquired | 26 | 19% |
| Defunct | 6 | 4% |
| Public | 1 | 1% (Einride, Nasdaq ENRD since 2026-06-10) |
| $1B and above | 11 | 8.0% |

The eleven $1B+ rows: Ineffable Intelligence $5.1B (2026-04), Handshake $3.5B (2022-01, stale),
Parloa $3.0B (2026-01), Starcloud $2.3B (2026-08), Netlify $2.0B (2021-11, stale), The Exploration
Company $2.0B (2026-07, low confidence), Instabee $1.6B (2022-09, stale), Odyssey $1.45B (2026-06),
Nothing $1.3B (2025-09), Beamery $1.0B (2022-12, stale), Standard AI $1.0B (2021-02, stale).

Entry stage: Seed 51, Series A 41, Growth 29, Pre-Seed 9, round not on record 7. Headquarters:
Germany 26, Sweden 25, United Kingdom 23, United States 22, France 13, Netherlands 9, Finland 7.
Evidence tiers: A 102, B 34, C 1. Membership rests on the firm's own listing for all 137 (117 on
the live eqtgroup.com pages, 20 on the archived eqtventures.com listings and the stories archive).

Excluded (`excluded.json`, preserved): 16 EQT Growth companies (`other_desk`), 8 `not_member`
rows (BIMobject, a public-market purchase; Docly, a demerger twin, by Erik's ruling; six Form D
name-matches and seat-dating misses), and
1 control position (Banking Circle, EQT VIII's buyout).

### S2A block

51 seed entries, 7 censored; a cohort of 44, of which 23 graduated and 21 did not: **52.3%**, with
100% coverage. The 21 nos rest on: the Form D record 1 (Vectary), a cited end 7 (Calldesk,
Popcore, Reworks, Sonantic, Owwn, Kitemaker, Wonder), and the full absence test 13. Ten decided
rows rest on an uncited entry stage (their own evidence decides them, stage low). Two nos are two
days (Vsim) and ten days (Moonscale) past the 24-month clock; both were searched under every name
they have used.

## 3. Calibration against the European books

| | Rows | $1B+ | S2A |
|---|---|---|---|
| EQT Ventures | 137 | 8.0% | 52.3% (23/44) |
| Creandum | 177 | 10.7% | 50.7% (36/71, after the Kive fix) |
| Balderton | 281 | 7.5% | 50.0% (18/36) |
| Atomico | 164 | 19.5% | 46.2% (6/13) |
| Cherry | 148 | 5.4% | 62.7% (52/83) |

EQT Ventures' $1B+ share sits between Balderton's and Creandum's, and its S2A rate just above both
(Creandum's fell to 50.7% with the Kive fix). Its stage mix (Seed 37%,
Series A 30%, Growth 21%) is earlier than Balderton's and later than Cherry's, which fits a fund
that states a EUR 2M to 50M check and leads most of its entries.

## 4. Coverage per evidence regime

| Regime | Rows | What it gave |
|---|---|---|
| eqtgroup.com portfolio pages (639 pages rendered, Key Facts read) | 117 | Fund, entry year, exit year per company; the desk key for every current and former holding |
| eqtventures.com archive 2017 to 2025 via Common Crawl | 21 | Former holdings the new site dropped; the Internet Archive was on cooldown for most of the run |
| The stories archive (172 posts) and the 2017 to 2020 articles (38) | cited on most rows | Entry rounds named by the firm itself; Bluebook as a recall addition |
| Form D (16 issuers, 30 accessions) | 15 companies | Round histories for US entities; 7 name-matches ruled out |
| EDGAR full text, Wikipedia insource | 25 registrants, 30 articles | No new member; SEEQC's prospectus named a second holding vehicle |
| Google News recall sweep (33 queries, 258 headlines) | 0 new | Crisp, BCB Group, SHL Medical, UserTesting ruled out (`sources/web/recall-probe.json`) |

## 5. Method deltas

1. **The desk key is read per company from the firm's own page.** Every EQT portfolio page names
   the fund that holds the company, so the Ventures/Growth partition is mechanical: 16 rows move by
   their Fund field, none by judgment.
2. **Key Facts are rendered client-side.** The listing is a React Server Components payload; the
   fund, entry and exit fields appear only in the rendered page, and a page with no "Fund" label
   puts the fund names before the first label (the parser now reads them; this recovered Wolt).
3. **Common Crawl's static cluster index** answered for 2016 to 2020 crawls when the index server
   failed (`scratch/cc-cluster.py`), and carried the whole archive layer while the Internet Archive
   was on cooldown.
4. **Entry-round median from the firm's own announcements** (Form D covers only 15 issuers): 114
   rows with a stated round size, each converted at the ECB rate of its entry date
   (`sources/web/entry-rounds.json`).

## 6. Flags and debt behind `verify`

| Flag | Rows | Meaning |
|---|---|---|
| `model_disputes_source` | 17 | The judge disputed a deterministic pre-fill (wrong Wikidata countries, a wrong public float, a unicorn-list name join) and says why in the note |
| `stage_uncited` | 15 | Stage by position or instrument, low confidence; 10 of them are decided S2A rows |
| `city_unknown` | 7 | Moonscale, Vsim, Beside, Colossi Games, Infinit, MarvelX, Meridian: sources disagree or say nothing |
| `stale` | 6 | Beamery, Handshake, Instabee, Netlify, Standard AI (marks older than 24 months, attacked in the A/B pass, no newer price found) |
| `unicorn_name_match` | 4 | Rows the unicorn snapshot joined by name; each verified in the A/B pass |
| `cik_weak` | 2 | Paid and Meridian: the SEC floats belonged to other issuers of the same name; the floats are cleared, the flag stays as the record |
| `stage_disputes_band` | 1 | A Form D band the judge overrode |

Seven rows carry a round the record does not give (`undetermined` stage): Min Doktor, WarDucks,
Watty, Billhop, Infinit, Voilà, Bluebook. `verify` noted that Atomico's book is in flight
and was not compared.

## 7. Standing duties and the A/B pass

1. **$1B+ claims, A/B pass on the visible slice (11 $1B+ rows plus Einride).** Pass A confirmed
   each cited source; pass B searched Google News for a newer round, sale or down round. Starcloud
   moved from $1.1B to **$2.3B** (a $250M Series A extension, 2026-08-21). Instabee's open value was
   pinned at the Sep 2022 merger price (EUR 1.6B), stale, into the $1B+ band. The Exploration
   Company's Series C (2026-09-08) had no disclosed price, so the $2B stays at low confidence. An
   unverified "$3.3B" Starcloud sentence from the grind was removed (Wikipedia on disk says $2.3B).
2. **Nos against reality:** no `not_graduated` row is $1B+ or public.
3. **Weak joins:** Paid (a $6.9M float from another "Paid") and Meridian (a 2012 float from another
   Meridian) had their floats cleared and `is_public` set false.
4. and 5. **Stale floats and public deaths:** no row takes its status from a float; the one public
   row is pinned by a cited market cap.
6. **Unicorn list, loose names:** 6 hits, all reconciled (Einride public at $607M, HeadSpin
   devalued, Wolt sold, the three 2026 rows verified).
7. **Blind 5% re-judgment:** 7 rows (seed 20260927), four columns each: 28 of 28 fields agree, no
   row flagged `unstable` (`scratch/blind-sample.json`).
8. **Momentum slice:** 33 private rows in the hot sectors first seen since 2021; each has a dated
   web check on the row (`valuation_range_source: web_verified`). None reaches $1B. It found
   Billhop's sale to Ramp (2026-03-16), now `acquired`.

Status corrections found on the way: Wonder (wonder.me) shut down in mid-2023, WarDucks closed in
Jan 2024, Willa Pay AB went bankrupt in Feb 2025; all three now `defunct` with citations.

## 8. Firm profile

| Field | Value | Source |
|---|---|---|
| HQ | Stockholm, Sweden | The firm's own page lists its advisers' offices, Stockholm first and without Luxembourg; the ADV's Luxembourg address is the fund manager's seat (`config.json` `profile.site_office`) |
| Founded | 2016 | EQT's 2016-05-26 launch release; EQT AB half-year report 2026 |
| Thesis | "Striving to be the most impactful partner to generation-defining founders." | The page's h1 |
| Stage | Pre-Seed, Seed, Series A, Growth | Entry stages on the base; "As early-stage lead investors" |
| Range | $2.3M / $11M median / $57M | The page's "Investment range 2-50M EUR" at the ECB rate of 2026-09-25; median from 114 entry rounds |
| AUM | $2,964,641,500 (both ends) | Form ADV 7.B of CRD 288390, the six Ventures vehicles only |
| Funds | EQT Ventures III (2022, EUR 1.1B), II (2019, EUR 660M), I (2016, EUR 566M) | The page's "Our Funds", the close releases, 7.B, the annual report |
| Notables | Wolt, Nothing, AnyDesk, Handshake, Netlify | Ledger members |
| Team | 28 people (15 with LinkedIn links from their own pages) | The page's team section |
| Icon | EQT's orange Q on a black plate, contrast 6.6:1, dry run only | Section 15 |

**The annual-report recipe (the issue's delta).** EQT Ventures has no adviser of its own, and the
one adviser that files for it (EQT Fund Management S.à r.l.) manages every EQT strategy, 969 fund
records in all. So:

1. **AUM** is the sum of the Section 7.B gross asset values of the strategy's own vehicles, read
   per private-fund ID: EQT Ventures (No.1)/(No.2), II (No.1)/(No.2), III (No.1)/(No.2) =
   $2,964,641,500. The Growth vehicles ($2.20B) and everything else stay outside.
2. **EQT AB's Annual and Sustainability Report** ("Additional fund information for selected
   funds", p.180 of the 2025 report, as of year end) gives each fund's vintage, committed capital,
   fee-generating AUM and status: EQT Ventures 2016 EUR 0.5bn / 0.3bn Developing, II 2019 EUR
   0.6bn / 0.5bn Developing, III 2022 EUR 1.1bn / 1.1bn Investing. It confirms the fund ladder
   and gives a floor (committed EUR 2.2bn = $2.585B, FAUM EUR 1.9bn = $2.23B at the 2025-12-31
   rate), both below the 7.B total, so they go in the `aum` flag, not the range.
3. **The parent's total AUM (EUR 270bn+) never fills `aum`**; the sidecar says so in the basis.
4. The subsidiary list (p.95 and the group register) names the GP entities and German KGs that
   tie each vehicle to the strategy, and shows a fourth GP (EQT Ventures IV) before any fund is
   announced.

## 9. Delta outcomes

| Delta | Outcome |
|---|---|
| Which desk is the venture desk, from registrations | D1: no EQT Ventures adviser exists; the fund family decides per vehicle; the Ventures funds are three SCSp pairs under their own GPs |
| EQT Growth: same desk or other desk | D2: other desk (EQT's own words at the 2022 Growth close: "two separate business divisions, with separate funds and advisory teams"). 16 rows out: Ardoq, CluePoints, Dwelly, Epidemic Sound, GotPhoto, Harvey, IntegrityNext, Lovable, Mambu, ManyPets, Mews, Mollie, Perk, ReliaQuest, Vinted, Wellhub. Where Ventures entered and Growth followed (Wolt), the row is a member through the Ventures entry |
| Sweden gives status only | Applied (D8) |
| Profile from EQT AB's annual report, never the parent's total | Section 8 |
| fx and non-US-listing constants bind on every row | Applied; Einride's cap is web-cited (StockAnalysis), BIMobject (First North) is out under R1 |

## 10. Open rulings for Erik

1. **D2, EQT Growth as `other_desk`** (the issue's delta, applied as ruled). Flipping it is one
   config line and a rebuild: the 16 rows above would return.
2. **R1, BIMobject** (`not_member`): a EUR 23.4M purchase into a company listed on First North
   since 2012, which the firm listed for seven years.
3. **R2, Docly: ruled by Erik 2026-09-27, `not_member`.** It arrived by demerger from Min Doktor,
   the class of the sale-consideration ruling; Min Doktor keeps its row. Base 138 to 137.
4. **R3, Kive: fixed in Creandum's book 2026-09-27 on Erik's instruction.** Heartcore's Oct 2022
   "$7 million seed round" is a named seed, so not a graduation, in both books now (Creandum's row
   carries the full absence test). Supernormal is read the same way here.
5. **R4, Ineffable Intelligence and Starcloud**: their pages name no fund yet; both are members on
   the Ventures team's own announcements.
6. **"Iris"**: named once in the firm's 2024 list of household names it has backed; no company of
   that name is found on any surface. Not added.
7. **Cross-investor pairs accepted here** (`companies/cross-rulings.json`): Endgame vs Menlo,
   Stacks vs YC, Luko vs Accel, Standard AI vs YC, The Exploration Company vs Cherry (aligned with
   Atomico and Balderton at $2B). Ruled distinct: Handshake vs a16z, Greylock, Sequoia and Point
   Nine; Odyssey vs a16z and USV; Wonder vs Accel and First Round. Vev (Oslo) and Point Nine's Vev
   (Utrecht) are different companies that happen to agree on status and band, so rule 10 counts
   them as agreeing; each note says which Vev it is.
8. **Accel's Airkit: fixed 2026-09-27 on Erik's instruction, now `graduated`.** Accel led the $7M
   seed in late 2017; Airkit raised a named $21M Series A in Jan 2020 (Forbes, 2020-10-06) and the
   $40M Series B EQT Ventures led in May 2021. Rule 10 does not compare the graduation column, so
   nothing had flagged it.
9. **Two disagreements in Accel's book that predate this run** (Accel's `verify` shows them; they
   did not block the re-ingest, which changed one cell): KupiVIP reads `acquired` at Accel and
   `defunct` at Balderton, and SingleStore reads `private` at Accel and `acquired` at Insight
   Partners. Not touched here.

## 11. Rebuilds and deltas

| Step | Rows | What landed |
|---|---|---|
| First build (kickoff) | 154 | Live pages, archive, Form D, stories |
| The one scheduled rebuild | 140 | 14 identity merges, 8 exclusions, Bluebook added |
| Second rebuild (same hour) | 138 | Aifloo and Noomi merged into Nectarine Health (the merge had been written for only one of the three names) |

The delta `prepare` queued the 29 open Seed graduations and nothing else.

## 12. Playbook write-backs proposed (not applied; COLLECTION.md belongs to the tooling session)

1. **§11, a strategy desk of a listed parent**: the annual-report recipe in section 8. Sum the
   strategy's own 7.B records by fund ID; read the parent's per-fund table for vintage, committed
   capital, FAUM and status; never the parent's total.
2. **§11, `hq_location`**: a fund manager's legal seat (a Luxembourg AIFM) is not where the firm
   operates; the site's own office list decides, recorded in `profile.site_office`.
3. **§6, S2A**: a later round the record names a seed is not a graduation, whatever its size
   (R3). Say it in the playbook so Creandum-style step-up readings stop.
4. **§8, `record` and notes**: `record` appends a note unless the old note already contains it,
   so a judge that sends a full rewritten note doubles it (41 rows here, fixed). Either `record`
   replaces a note that starts with the old one, or the playbook says to send only the new text.
5. **§5, portfolio pages rendered client-side**: read Key Facts from the rendered page; lines
   before the first label are the fund names.
6. **§5, Common Crawl's static `cluster.idx` route** as the standard fallback when the index server
   fails (Balderton proposed the same).
7. **§11, `graduation-surfaces.py` needs `investor/investor.json`**: a fresh book must write the
   profile first (Balderton hit the same).

## 13. Usage line

| | 5-hour | Weekly, all models | Weekly, Fable |
|---|---|---|---|
| 2026-09-27 15:55 UTC (close) | 17% | 78% | 82% |

The account is shared with sibling sessions, so the weekly figures are the wave's. Base rows: 138.
Web searches: about 130 of 200; Google News carried the rest.

## 14. Prompt count

**2**, final: the kickoff and the ingest approval (which carried the three fixes).

## 15. Ingest request (not run)

On Erik's approval, in this order: the icon upload, then `scripts/ingest-investor.ts`, then
`scripts/ingest-companies.ts` with a dry run first.

```bash
npx tsx scripts/fetch-investor-icon.ts eqt-ventures https://eqtgroup.com/assets/images/android-v2-chrome-512x512.png --plate "#000000"
```

EQT Ventures is a first-time investor, so the companies ingest removes no rows from the database.

## Ingest 2026-09-27 (Erik's approval, second prompt)

Erik approved with "ingest", and asked for three fixes in the same message: Creandum's Kive, Docly,
and Accel's Airkit. The fixes ran first, then the ingest in the first-time order.

| Step | Result |
|---|---|
| Docly ruling (R2) | `not_member`; base rebuilt, 138 to 137; `verify` clean |
| Creandum's Kive | `not_graduated` with the full absence test; `verify` clean; committed a3ee838 |
| Accel's Airkit | `graduated` on the named Jan 2020 Series A (Forbes); committed a3ee838 |
| Icon upload | `investors/eqt-ventures-fb257d2dc9.png` (the orange Q on a black plate, contrast 6.6:1, ramp 0.92 px) |
| `ingest-investor.ts eqt-ventures` | 1 investor row upserted |
| `ingest-companies.ts eqt-ventures --dry-run` | Plan: 137 upserted (137 new), 0 removed, from 0 live |
| `ingest-companies.ts eqt-ventures` | 137 of 137 upserted |
| Readback (`scratch/readback.ts eqt-ventures`) | csv 137, live 137, missing 0, differing cells 0 |
| Creandum and Accel, compared before the re-ingest | exactly one differing cell each (Kive, AirKit), nothing else |
| `ingest-companies.ts creandum` and `accel` | Plans 177 and 884 upserted (0 new, 0 removed); readback 0 differing cells each |

The database derived from EQT Ventures' rows: 137 companies counted, 11 at $1B and above, 1 public,
S2A 52.3% on a cohort of 44 (51 seed entries, 7 censored). Creandum's S2A is now 50.7% (36 of 71),
Accel's 59.1% (143 of 242).

**Prompt count: 2**, final: the kickoff and the ingest approval.

