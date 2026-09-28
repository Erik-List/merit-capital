# 20VC: Build & Reconciliation Report (PRO-76)

20VC (Twenty VC LLP, London), collected 2026-09-28 under
`data/collection/COLLECTION.md` in one session. This report is the state at
close: 123 companies, plain `verify` clean, not ingested.

## 1. The answer PRO-76 asked for

**123 companies, plain `verify` clean, profile built, review surface checked.
Ingest waits for Erik's approval (section 14).**

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
| Cross-investor (rule 10) | 89 shared rows: 81 agree, 8 accepted (the sibling side is stale), 0 disagree; 16 namesake pairs ruled distinct in `companies/cross-rulings.json` |

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
(2025-12), Fuse Energy $5B (2025-12), AMI Labs $4.53B (2026-03), Sorare $4.3B
(2021, stale), Clubhouse $4B (2021, stale), Remote $3B (2022, stale),
Tripledot $2B (2025-05), WorkOS $2B (2026-03), Factory $1.5B (2026-04),
Linktree $1.3B (2022, stale), Linear $1.25B (2025-06), AgentSync $1.2B (2021,
stale), NexHealth $1B (2022, stale). Every mark is a cited priced round;
rounds only in talks (Mercor at $20B, Factory at $3.5B) are not marks.

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
  below-$1B company crossed $1B (Peec AI's June 2026 round reads $200M).
- **Alignment with sibling books**: every shared row agrees or is an accepted
  stale pair (section 1). Rows with a fresher cited mark than the sibling:
  Kevin (defunct, insolvency 2024; Accel reads private), Nxyz (acquired by
  Snowflake 2023; Sequoia reads private), WorkOS ($2B, 2026; Lightspeed below
  $1B), Fuse Energy ($5B; Creandum below $1B), Poolside ($12B; Redpoint $3B),
  Factory ($1.5B; Khosla, Lux and Sequoia below $1B). Also Pachama is now
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
8. **Eight accepted pairs** (section 7) are the other books' stale sides, for
   the next alignment pass.
9. **Published names** changed to the companies' own spellings via
   `config.json names.published`: Roam Research, Remote, Kevin, AgentSync,
   AMI Labs, NexHealth, Lottielab, TechWolf, Noh, RoadFlex, Allo, Merge,
   DataLane.

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

## 13. Prompt count

1 so far (the kickoff, "please collect 20VC"). The ingest decision is the
second.

## 14. Ingest

Not run. Order when approved: icon upload, `ingest-investor.ts`, then
`ingest-companies.ts` (123 companies; first ingest for 20VC, so nothing to
remove).
