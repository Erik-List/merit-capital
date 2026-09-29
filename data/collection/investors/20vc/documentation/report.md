# 20VC: Build & Reconciliation Report (PRO-76)

20VC (Twenty VC LLP, London), collected 2026-09-28 under
`data/collection/COLLECTION.md` in one session. This report is the state at
close, updated after Erik's approval the same night: 123 companies live, and the
eight stale rows this run found in other books aligned and re-ingested
(section 15).

## 1. The answer PRO-76 asked for

**123 companies live (ingested 2026-09-28 with Erik's approval, readback
exact), plain `verify` clean, profile built, review surface checked. The
other books' stale sides were aligned and re-ingested first (section 15).**

| Done-when item | State |
|---|---|
| Plain `verify` green | `verify: clean` (flagged debt only, section 6) |
| Entity set in `decisions.md` | D1: one exempt reporting adviser, Twenty VC LLP (CRD 316359); Fund I to III, Explorer II and III, D-1, S-1 to S-5, SPV1 and SPV2 in; the 20Growth, 20Product and 20Sales offshoot funds, Stride.VC, Project Europe and the media business out (D1 to D5) |
| Silent-empty vehicle registry made loud | Section 3: five of seventeen vehicles were invisible to every registry route; a config shape and a verify signal are proposed (section 11, write-back 1) |
| COLLECTION.md diff proposed | `documentation/collection-md-proposal.md` (five hunks, not applied: the playbook is the tooling session's) |
| Rulings asked for | Media business vs fund (D2: out), podcast relationships (D7: out), SPVs and syndicates (D6: in); two run-time rulings R1 and R2 (section 9) |
| Every row judged, classified, cited | 125 verdicts (123 member, 2 `not_member`), 123/123 classified |
| Firm profile | `investor/investor.json` + `sources.json`, built by `build-firm-profile.py`, `profile_copy.py` ok |
| `review.html` rendered | Served on the review surface (port 8931) and checked: 123/123 rows, profile panel with every field's source |
| Cross-investor (rule 10) | 89 shared rows: 89 agree, 0 accepted, 0 disagree after the alignment (section 15); 16 namesake pairs ruled distinct in `companies/cross-rulings.json` |

## 2. Results

| | Count | Share of 122 nameable |
|---|---|---|
| Companies | 123 (1 unnameable, Random Walk, excluded from every metric) | |
| Private | 103 | 84% |
| Acquired | 14 | 11% |
| Defunct | 4 | 3% |
| Unknown | 2 | Alloy, and Random Walk (the unnameable row) |
| $1B and above | 18 | 15% |
| of which $10B and above | 5 | Cognition, Perplexity, Lovable, Poolside, Mercor |

The 18: Cognition $48B (2026-09), Perplexity $20B (2025-09), Lovable $13.3B
(2026-08), Poolside $12B (2026-08), Mercor $10B (2025-10), Airwallex $8B
(2025-12), Fuse Energy $5B (2025-12), Factory $5B (2026-09), AMI Labs $4.53B (2026-03), Sorare $4.3B
(2021, stale), Clubhouse $4B (2021, stale), Remote $3B (2022, stale),
Tripledot $2B (2025-05), WorkOS $2B (2026-03),
Linktree $1.3B (2022, stale), Linear $1.25B (2025-06), AgentSync $1.2B (2021,
stale), NexHealth $1B (2022, stale). Every mark is a cited priced round;
rounds only in talks (Mercor at $20B) are not marks. Factory's mark is its
September 2026 round ($200M at $5B), found at the alignment (section 15).

Entry stage over the 83 rows whose round is on record: Seed 46, Series A 19,
Growth 10, Pre-Seed 8; 39 nameable rows (32%) stay `undetermined`, mostly
live-list companies whose round no source ties to 20VC.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 46 | 21 | 25 | 11 | 14 | **44.0%** |

Coverage 100%. The 14 nos rest on a cited end (4: Spiketrap, ShoppingGives,
Atlantic Money, Bonnet, each bought before any Series A) and the absence test
(10). Five decided rows rest on an uncited (model) entry stage and carry
`stage_uncited` at low confidence (Spiketrap, Roam Research, Payflows,
Firmable, Papaya). The book is young: 21 of 46 seed entries are inside the
24-month window, so the rate stands on 25 rows.

## 3. The boundary

- **D1, the firm and its vehicles.** One adviser, Twenty VC LLP. Its newest
  Form ADV (2025-06-17) swears to six funds, $602,711,121 (Section 7.B(1)).
  In: Fund I (2020, $8.3M), Fund II and Explorer Fund II (2021, $33M and
  $107M), Fund III and Explorer Fund III (2024, $125M and $275M), D-1, the
  S-1 to S-5 single-deal vehicles and SPV1/SPV2. "20VC Growth" and "20 VC
  Explorer" in the press are the Explorer funds.
- **The 20Growth, 20Product and 20Sales offshoot funds are external**
  (separate vehicles run by their operator partners; the ADV lists them under
  7.B(2), reported by AngelList Advisors). Every company they back here also
  has 20VC's own fund in the round (Fyxer, 11x, allO, Flare), so the ruling
  moved no row. Flagged for Erik.
- **D2** the media business (The Twenty Minute VC Ltd) and 20VC Property out;
  **D3** Harry Stebbings' angel book before April 2020 out; **D4** Stride.VC is
  another firm (Hofy, TechWolf and Handly carry 20VC rounds of their own);
  **D5** Project Europe is its own fund; **D6** SPVs and syndicates in; **D7**
  podcast relationships out; **D8** partners' seats dated to their firm at the
  time (Omada and TechWolf have 20VC's own participation beside Felix's);
  **D9** Form D homonyms out (Crosstown Brewing).
- **R1** a press line naming only Harry Stebbings corroborates a row the firm
  itself lists and dates its entry; alone it admits nothing. It kept out
  Macro, Opal, the.com and BukuWarung.

**The vehicle registry (PRO-76's first ask).** Five of the firm's seventeen
vehicles, Fund I among them, were invisible to every route the registry had,
and it said nothing: EDGAR's company search matches name prefixes and stops at
"Fund I, a series of 20VC, LP"; the platform funds' Form Ds name AngelList's
Belltower Fund Group, never a partner; and IAPD's search finds nothing for
"20VC" because the adviser files as Twenty VC LLP. What found them was the
adviser's own sworn fund list (ADV 7.B) resolved through EDGAR full-text
search on each name's tail. Proposal in section 11.

## 4. Coverage per evidence regime

| Regime | Rows | How membership rests |
|---|---|---|
| The firm's live list (20vc.fund, Framer CMS, 79 cards) | 79 | site listing |
| The podcast site's archived portfolio pages (2022-2024, Common Crawl) | 15 | site listing (Vital merged into Junction) |
| Press naming 20VC's fund in a round | 26 | `web`, one citation each |
| The firm's own "About 20VC" boilerplate (2025 releases) | 2 | `web` (Perplexity, Captions) |
| Press on Factory's 2026 Series C | 1 | `web` |
| Ruled out | 2 | BukuWarung (R1), Crosstown Brewing (D9) |

The Internet Archive was down for this machine most of the day (a two-hour
cooldown), so the 2022-2024 archive came from Common Crawl. The archive
answered once at the end: it holds a partial copy of the firm's list from
2026-06-12 (50 cards, all in the base), which resolved Alloy's identity.

## 5. Method deltas

- **Framer site.** The live list ships as a Framer CMS data chunk behind a
  client-side "Load More"; `scratch/framercms.py` decodes it
  (`sources/site/companies-framer.json`). The June 2026 archived copy uses a
  newer dictionary-chunk format; its strings were read directly
  (`sources/wayback/framer-cms-2026-06-12.json`).
- **Common Crawl** replaced the Wayback Machine for the podcast site's
  2022-2024 portfolio pages (`scratch/cc-*.py`).
- **Press layer.** 20VC is named in far more articles as a podcast than as an
  investor, so every press sentence was read against D7 and R1 before it
  counted.
- **Targeted news reads.** Where the standard graduation query used a wrong
  spelling ("LottieLabs", "Noh Payments") or drowned in namesakes (Roam, Ellis,
  Papaya, Junction), the absence test carries an extra, named query.

## 6. Flags and debt behind `verify`

`stage_uncited` 24, `city_unknown` 12, `model_disputes_source` 11 (Wikidata
namesakes: Mercor LV, Grand SE, Pearl SR, Sphere JP, Slay US, Roam GB and
more), `identity_homonym` 10, `stale` 6, `cite_pending` 2 (Airwallex and
Lovable: $1B+ rows whose entry round is model-read), `country_prior` 2,
`identity_unresolved` 1 (Random Walk).

## 7. Standing duties and the A/B pass

- **Pass A/B over the visible slice** (every $1B+ row) and the **momentum
  slice** (every private row with an entry or round since 2024): one Google
  News read per row for valuation, unicorn, acquisition and shutdown words
  (`scratch/research/momentum.json`, 2026-09-28). No mark changed: the newest
  priced round is the recorded one on every $1B+ row, and no recent
  below-$1B company crossed $1B (Peec AI's June 2026 round reads $200M). One
  miss: Factory joined the book in the post-rebuild delta, after this scan, and
  its September 2026 round ($200M at $5B) was found only at the alignment
  (section 15). The scan belongs after the delta.
- **Alignment with sibling books**: at the close, eight shared rows were
  accepted differences where the other book was stale:
  Kevin (defunct, insolvency 2024; Accel reads private), Nxyz (acquired by
  Snowflake 2023; Sequoia reads private), WorkOS ($2B, 2026; Lightspeed below
  $1B), Fuse Energy ($5B; Creandum below $1B), Poolside ($12B; Redpoint $3B),
  Factory (Khosla, Lux and Sequoia below $1B). All eight were aligned and
  re-ingested with Erik's approval (section 15); every shared row now agrees.
  Also Pachama is now
  acquired (Carbon Direct, 2025-11), as YC's row already reads.
- **Wikipedia insource sweep**: 52 articles, nothing new (Suno's mention is a
  podcast appearance).

## 8. Firm profile

HQ London, United Kingdom (the ADV principal office, 16 Berkeley Mews; the
site names no office). Founded 2020. Thesis, quoted from the homepage
headline: "20VC operates at the intersection of venture capital and media."
AUM $602.7M at both ends (the sworn 7.B composite; an exempt reporting adviser
files no Item 5.F; press "about $650M" not used). Funds: Explorer III $275M
and III $125M (2024), Explorer II $107M and II $33M (2021), I $8.3M (2020);
the single-deal vehicles are counted in the basis. Team: Harry Stebbings,
Kieran Hill, Julien Codorniou, Paul Bonnet, Alexandre Dewez (the operator
partners are advisers to the offshoot funds, D8). Range $250K / $9M median
entry round / $116M (the largest round it led, Tripledot). Stage Pre-Seed to
Growth; geography core Europe, other US and Australia. Notables: Perplexity,
Lovable, Clubhouse, BeReal, Hopin. The icon is the site's own stacked
"20VC / FUND" mark redrawn from its vector wordmark (dry run passed:
contrast 16.8:1, ramp 0.8px); it uploads with the ingest.

## 9. Open rulings for Erik

1. **D1 offshoot funds external** (20Growth, 20Product, 20Sales), although the
   ADV lists them under 7.B(2). No row moves either way today.
2. **PRO-76's three rulings as derived**: media business out (D2), podcast
   relationships out (D7), SPVs and syndicates in (D6).
3. **R1** (Harry-only press lines admit nothing alone): keeps out Macro, Opal,
   the.com and BukuWarung, which a reader might expect in if Harry's
   post-2020 checks were the fund's.
4. **R2** (new): the firm speaking about its own holding on its podcast is
   first-party evidence of the position. Used once: Poolside's entry is the
   2023 seed ("roughly a 15x for them as a seed investor", SaaStr's write-up).
5. **Roam is Roam Research**, not ro.am (the IVP row), on timing and a vendor
   listing; low confidence, published as "Roam Research".
6. **Alloy** is alloy.capital by the firm's own June 2026 card; its domain has
   lapsed, status unknown.
7. **Random Walk** stays unnameable: the card says "Stealth..." and links a
   domain that now belongs to an enterprise AI services firm.
8. **Done** (Erik, 2026-09-28): the other books' stale sides were aligned and
   re-ingested (section 15).
9. **Published names** changed to the companies' own spellings via
   `config.json names.published`: Roam Research, Remote, Kevin, AgentSync,
   AMI Labs, NexHealth, Lottielab, TechWolf, Noh, RoadFlex, Allo, Merge,
   DataLane.
10. **General Catalyst's Flare Technologies and Sphere** read status unknown
    against 20VC's Flare and Sphere (both private). General Catalyst's rows are
    names from its compliance list with no website, so neither sameness nor
    difference can be shown; they need an identity ruling. General Catalyst's
    own verify lists both pairs; 20VC's skips General Catalyst, whose in-flight
    marker is committed.
11. **Sequoia's Factory entry stage** stays model-read ("Series A") and now
    carries `cite_pending`, which a $1B+ row requires. Khosla's row notes the
    November 2023 $5M seed was co-led by Sequoia and Lux, which would make the
    entry Seed in both books; that stage change is left for Erik.
12. **Older disagreements** found while re-verifying the corrected books, none
    from this run and none touched: Khosla's Faire below $1B against Sequoia's
    and Lightspeed's $5.2B; Accel's SingleStore private against Insight's
    acquired; Accel's KupiVIP acquired against Balderton's defunct;
    Lightspeed's Yubi below $1B against Insight's $1.5B; Sequoia's Root and
    Versatile against Insight's rows (likely namesakes); General Catalyst's
    Hiro, Stitch, Tempo, Tempo Labs and Tomo against Ribbit's rows.
13. **A verify false alarm.** Since PRO-146, `review` renders published names,
    but verify's "review.html stale" check still looks for the first row's
    base name. Khosla's re-rendered page fails it ("Academia Inc." publishes
    as "Academia"). The fix is one line in `run.py` (accept the published
    name); not made here because another session has uncommitted edits in
    `run.py`.

## 10. Rebuilds and deltas

One scheduled rebuild after the recall probe: 3 rows added (Perplexity,
Captions, Factory), 2 moved to `excluded.json` (the two `not_member` rows), no
renames. The delta produced three membership verdicts (all member), so one
more rebuild ran before export, as the playbook asks: no change.

## 11. Playbook write-backs proposed (not applied mid-wave)

The exact text is in `documentation/collection-md-proposal.md`.

1. **Vehicle registry completeness** (PRO-76's ask). Config shape:

   ```json
   "edgar": {
     "seed_queries": ["20vc"],
     "adviser_crds": [316359],
     "vehicle_phrases": ["a series of 20VC", "a series of 20Growth", "a series of 20Product", "a series of 20Sales"],
     "gp_entities": ["20VC GP II", "20VC GP III"]
   }
   ```

   `adviser_crds`: resolve every ADV 7.B(1) and 7.B(2) fund name (source
   `adv-7b`); find the adviser by Form D filing address in the SEC's monthly
   roster CSV when IAPD's search fails. `vehicle_phrases`: EDGAR full-text
   phrases whose hits are the firm's vehicles (catches funds no ADV lists
   yet: Fund I predates the 2021 registration, 20Sales Fund II postdates the
   2025 amendment). `gp_entities`: a vehicle whose Form D names the firm's GP
   entity is the firm's (every S-series SPV names 20VC GP II).
   **Verify signal**: the registry resolves at least as many own vehicles as
   the adviser's sworn 7.B count (from the monthly roster). ADV count N > 0
   and fewer resolved: fail ("missed K of N sworn funds"). ADV count 0 and an
   empty registry: clean, printed as "no private funds reported", the only
   state in which an empty registry is clean. No adviser resolved at all:
   fail unless `edgar.no_adviser` states why. The sworn count is what tells
   "no vehicles" apart from "the pattern missed".
2. **Framer CMS as a site layer**: promote `scratch/framercms.py` to
   `scripts/`, and add the project's `/modules/` prefix on
   framerusercontent.com as an archive surface (the June 2026 dictionary
   chunk carries every card's name, one-liner and website).
3. **Graduation surfaces should search the published name**:
   `graduation-surfaces.py` queried "LottieLabs", "Noh Payments" and "Roam",
   so three absence tests needed a hand-run query. Reading
   `names.published` (or a `names.search` alias) would fix it at source.
4. **Media-brand firms**: D7's reading (a podcast mention is never
   membership) generalises to any firm whose name is also a media brand.

## 12. Usage line

Weekly all models 22% at close, weekly Fable 6%, 5-hour window 70%, extra
usage EUR 12.14 of 50 (disabled). The kickoff reading was not taken (the
weekly window reset during the day). 123 published rows (125 judged including
the 2 exclusions). Web searches: about 54 of 200. No research agents.
After the alignment and ingest: weekly all models 25%, weekly Fable 6%, the
new 5-hour window 9%. Web searches for the alignment: 1 more.

## 13. Prompt count

2, final: the kickoff ("please collect 20VC") and the approval ("fix the
valuation or status revealed in 20VCs collection run for other investors,
afterwards ingest").

## 14. Ingest

Approved by Erik on 2026-09-28, after the alignment (section 15):

1. Icon uploaded: `investors/20vc-897665fe54.png` (the stacked "20VC / FUND"
   mark, 256x256, contrast 16.8:1, ramp 0.80px).
2. `ingest-investor.ts 20vc`: 1 investor record upserted ("Australia" added as
   a new geography label; the vocabulary is open).
3. `ingest-companies.ts 20vc --dry-run`: 123 new, 0 removed, from 0 live;
   then 123/123 upserted, and `public.companies` holds 123 rows for 20VC.
4. Readback (`scratch/align/readback.ts`, read-only): 123 in the CSV, 123
   live, 0 missing, 0 extra, 0 differing cells. The investor row carries 18
   companies at $1B+ and 5 at $10B+, and S2A 44% on a cohort of 25.

## 15. Alignment of the other books (approved 2026-09-28)

`scratch/align/compare.py` compared every shared row on status, band, figure
and as-of date. `scratch/align/align.py` recorded one line per stale row into
that book with `run.py record` (`who: agent-align-pro76`, the citation on the
row, the note appended). Each book was then exported, its review re-rendered
and its CSV diffed against HEAD: every book changed by exactly the rows below.

| Book | Row | Before | After | Source |
|---|---|---|---|---|
| Accel | Kevin | private | defunct | insolvency, Vilnius court (The Paypers, 2024-09); licence revoked (Bank of Lithuania, 2024-10) |
| Sequoia | Nxyz | private | acquired | Snowflake's definitive agreement (MarketScreener, 2023-07-26) |
| Lightspeed | WorkOS | below $1B | $2B (2026-03) | SiliconANGLE, 2026-03-03 |
| Creandum | Fuse Energy | below $1B | $5B (2025-12) | Balderton's post, 2025-12-18 |
| Redpoint | Poolside | $3B | $12B (2026-08) | Forbes, 2026-08-24 |
| Khosla, Lux, Sequoia | Factory | below $1B | $5B (2026-09) | Tech Funding News, 2026-09-16 |
| 8VC, General Catalyst, Khosla, Lux | Cognition | $10.2B | $48B (2026-09) | TechCrunch, 2026-09-08 |
| 20VC | Factory | $1.5B (2026-04) | $5B (2026-09) | Tech Funding News, 2026-09-16 |

Factory's September round was new to this run: Khosla's own note mentioned
it, and a news read confirmed it ("has raised $200 million at a $5 billion
valuation", after The Wall Street Journal and Reuters of 2026-09-15), so
20VC's own row moved with the others. Cognition's four rows were already in
the same band; the figure is what a reader sees, so they were aligned too.

Before any write, a readback showed every book's database rows equal to its
committed CSV except the cells above. Each book was then re-ingested with a
dry run first (0 new, 0 removed in all nine) and read back with 0 differing
cells: Accel 884, Sequoia 873, Lightspeed 875, Creandum 177, Redpoint 413,
Khosla 506, Lux 270, 8VC 250, General Catalyst 1,933 rows
(`scratch/align/reingest.log`). The investor track records recomputed:
WorkOS is in Lightspeed's $1B+ list, Fuse Energy in Creandum's, Poolside in
Redpoint's $10B+ list, Factory in Khosla's, Lux's and Sequoia's.

Plain verify after the alignment: 20VC, Creandum, Redpoint, Lux and 8VC
clean; Khosla fails only on the false alarm of section 9, item 13; Accel,
Sequoia, Lightspeed and General Catalyst fail only on the older disagreements
of section 9, item 12, none of them on a row changed here. The eight accepted
pairs were removed from `companies/cross-rulings.json`, since they now agree.
The same pairs in other books' rulings files (Balderton and Ribbit on
Creandum's Fuse Energy; Bain Capital Ventures, Felicis and Point Nine on
Redpoint's Poolside) are now inert and were left in place.
