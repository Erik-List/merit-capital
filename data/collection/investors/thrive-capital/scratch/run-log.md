# PRO-64 run log (scratch, regenerable narrative)

2026-09-03, single session, merged shape (PRO-71): base + classification + profile in one run.
Prompt count so far: 1 (kickoff "Please collect thrive capital").

## Kickoff facts pinned
- thrivecap.com: no portfolio list in any era (Wayback replay 2010-2023 + Common Crawl 2013-2026: splash 2010,
  one-pager 2011-2020, Framer site 2021+ with /info /incubations /contact /disclosure /thrive-x). /incubations
  names no company (browser-rendered). The one list surface: jobs.thrivecap.com (Getro, 106 companies) —
  decisions.md ruling 8, file_list source with the sitemap route.
- IA partial outage: CDX wildcard queries refused (rc 7 / HTTP 000), homepage CDX and replay answered;
  Common Crawl index thin (homepage only until 2021, /inc /info 2021-2023, jobs board 2025+).
- EDGAR: 60-entity registry (49 own: Funds II-X, growth sleeves, lettered LLCs, Claremount, GP LLCs, JSC,
  North River; 11 external incl. the Fort Washington PA namesake under the adviser's exact legal name — CIK
  1845943 confirmed external, 1765681 confirmed us). Ownership filings by the vehicles: 3 subjects only
  (Oscar Health 3/4/13G, Hims & Hers 13G, Vimeo 3/4) — Section 4(a)(2) and sub-5% stakes leave the fund_filing
  layer near-empty, as PRO-64 predicted.
- Roster: curated 20 people (ADV Schedule A + fund Form D related persons + press tenures); sweep 301
  accessions / 161 issuers; clusters: Josh Miller (50 issuers, homonyms), Kushner (53: funds + Oscar/Mulberry,
  Harry's/ADKM/HF Global, Skims, Artsy, Hightower, Kinnek, Zola, Cadre), Zaki (10 healthcare), Weinstein
  (Justworks, Geneva, LeafLink), Gaybrick (Stripe as CFO, Oscar, Omakase=Maple, Justworks), Grimshaw
  (Lattice/Degree, Monzo, Benchling, Supergreat, Doji), Paik (Justin.tv, Grailed, then Pace-era Chrono/
  Trolley/Tiltify/Comfy), Ahuja (LiquidHub homonym, Imprint, then Timeless), Nohria (Rakuten personal, Alsym).
- ADV 2026-07-06: RAUM $50,492,232,840 / 54 funds (Section 7.B roster parsed to the dollar less $1 rounding),
  80 employees / 33 advisory, one office. 13F 2026-06-30: Amazon, Figma, Oscar, Shopify, SpaceX.

## Build 1 (16:5x) and pre-grind rebuild (17:2x, identity-merge fix, nothing recorded)
142 rows: 21 A / 85 B / 36 C; 106 board + 2 fund_filing seeds; 34 unjudged Form D rows; 139 queued in 4 batches.
Dropped by the build: 3 LPs (FLB Partners T, Olam P/T — Kushner-officer vehicles filed 2025-2026, 'Other',
$0 sold: Eternal-class plumbing), 7 non-portfolio-industry Form D-only (incl. Monzo Bank Ltd — the board row
'monzo' carries it), 3 ex-partner-only (Trolley, Comfy, Owen Woods).

## Gate (scratch/gate-blind-pass.json) — PASS
Membership 0 false members; stage layers: Form D band 4/10 -> ceiling; Getro stage -> never a label;
press/vehicle class 1 -> 35/35. Evidence order for the grind recorded there.

## run.py change (PRO-71 learning)
verify --in-flight fired invariants 3/4 on rows the deterministic layers pre-filled (unicorn-list values,
public floats) that no batch had answered: 17 red lines before the first batch. Gated both on `slug in cls`
(judged) in flight; full mode unchanged.

## Post-rebuild (2026-09-03, after the context reset)
Delta batch (37 recall rows) judged and recorded; a16z aligned (honor, plaid, xdof, loft — re-ingest needed);
cross-investor 87/87 agree. A/B pass on the visible slice: web-search budget exhausted at 200 calls after
Cityblock; OpenAI ($852B, Aug-2026 tender flat), Stripe ($159B Feb 2026), Fanatics (no primary since 2022;
~$17B secondary indications) and Mammoth Brands (no primary since 2021) re-checked via the app browser's
DuckDuckGo HTML endpoint; Cedar, Lattice, Benchling, Rightway, Capsule, Airbyte, Stytch keep `stale`.
Standing duties: weak-CIK audit (78 weak joins read, quarantines stand), loose unicorn re-intersection
(patreon + cadence-solutions surfaced as unjudged), self-consistency 8 rows / 40 fields 33 agree (82%),
4 rows flagged `unstable` (all model-sourced fields). Found and fixed: three base rows (oscar-health,
patreon, cadence-solutions) had no classification row — rebuild slug renames left three stale keys and
verify counted keys, not base rows; run.py now counts over the base and fails on unclassified rows.
verify.shape ceilings added (ruling 13). Profile built (17 funds, 13 accession assertions, RAUM $50.49B,
17 people); icon normalized dry-run only (upload is gated with ingest). verify green in full mode.

## Post-close delta (2026-09-03, Erik-approved second rebuild)
New layers: scripts/edgar-fts-sweep.py (phrases 'Thrive Capital Partners' / 'Thrive Capital Management' /
'Claremount': 663 hits, 99 registrants, 31 third-party) and scripts/wikipedia-insource.py (78 articles, 26 in
base, 16 company candidates). Judged: 15 members added (segment, bread, blend-labs, reddit, securitize,
younow, greenhouse-software, tictail, spree-commerce, mapbox, neverware, essential-ai, io, diem, ellis),
2 not_member (willow-wealth = Cadre merger consideration; fifa-forward-enterprise = Thrive Eternal),
noise registrants ignored (Puck Building lease in a 2011 CMBS, 'Claremount' street/place names in PIMCO,
Montpelier Re, RFMS, Wells Fargo and a LendingClub loan listing; Tribe Capital typo; EarthLink = Trive).
