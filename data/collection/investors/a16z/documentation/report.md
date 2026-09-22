# Company Base Report — a16z (PRO-30)

Single-session autonomous run, 2026-08-29. Scope: the membership-verified
Company Base (PRO-30, "autonomous session 1, part 1"). Classification
columns (`status`, `valuation_range`, `entry_stage`, `hq_*`, `focus`, C2A)
are PRO-31, which continues on this base after Erik's sample sign-off.

**Prompt count: 9** — 1 kickoff ("execute the a16z base collection as per
linear issue PRO-30 / work diligently in full autonomy") + 8 review
exchanges on 2026-08-30. Checkpoint approvals requested: 0 (both
checkpoints posted as status and continued, per the kickoff's autonomy
instruction). **Erik rulings recorded: 6** (each class-wide,
`who: "erik"`): (1) `hewlett-packard-co` out — the audit's not_member had
landed on the merged HPE slug and the HP twin survived the split with a
stale fund_filing seed; sole evidence is Andreessen's personal Section 16
stream. (2) Black Forest Labs corrected to Seed entry / $3.25B / 1b_plus
with citations — the band had mislabeled the Nov-2025 $300M Series B
filing as a Growth entry because the a16z-led $31M seed (Aug 2024) never
filed. (3) Decisions ruling #6: fund-shaped investment-list entries
unidentifiable as operating companies are not_member (AMP Fund, Drone
Capital I, Revival Fund Management). (4) Decisions ruling #7, refining
#3: pure protocol-asset holdings with no issuing organization are out
(Bitcoin, Ethereum); DAO/labs-backed token positions stay (Lido). (5)
Essence Ventures confirmed member (operating company despite the name).
(6) Two identity consolidations ratified in review: 21 -> Earn Holdings
and Filecoin -> Protocol Labs. Further review outcomes:
Hawthorne Labs moved uncertain -> not_member by re-applying the
uncorroborated-name-match rule, and `abacus` (firm-listed since 2023 but
unidentifiable) flagged identity_uncertain with a documented note.
Erik's sample sign-off is the open exit criterion.

## 1. Result

**1,798 published rows** — 1,164 Tier A / 623 Tier B / 11 Tier C — every
row an affirmed **member** (0 uncertain after Erik's review rulings),
plus **134 not_member rows** preserved in `excluded.json`. Verdicts by evidence class: 1,792 site_listing,
10 formd_adjudicated, 2 fund_filing, 3 web (recall additions); by author:
1,786 evidence-class seeds, 21 judge verdicts surviving on published rows
(the other ~160 judge verdicts sit on excluded or absorbed rows).

Evidence coverage: 1,691 rows on the firm's own live listings, 1,252 with
Wayback-era corroboration (2010-2018 portfolio pages + 2023/2024/2026
investment-list snapshots), 160 with partner-attributed Form Ds, 23 with
fund 13D/G / Section 16 streams. `first_seen` dated on 1,278 rows.

## 2. Evidence layers (a16z parameters)

- **Site (layer 1b), four surfaces, 1,703-company union**: the /portfolio/
  page embeds `portfolio_companies` as a JS array (854 rows with
  stage/outcome tags, tickers, acquirers, announcement permalinks); the
  /investment-list/ compliance page (1,458 plain names, "investments made
  in vehicles managed by a16z" — the page itself declares two exclusions:
  issuer-refused disclosures and unannounced public digital assets);
  speedrun.a16z.com's paginated JSON API (251 accelerator companies,
  cohorts SR001-007, in per decisions §2); a16zcrypto.com/portfolio
  (126 rows, 27 of them on no other list — Lido, Farcaster, Yuga Labs,
  Anchorage...). a16z's WP REST is closed on both routes, so
  site-portfolio.py gained a generic `scrape` site_api type (js_array,
  li_text_list, paginated_json, regex_list parsers).
- **Wayback (layer 1)**: three portfolio-page markup eras
  (2010-2013 `entry-title` h1s: 23→69 companies; 2014-2015 `<b>Company:</b>`
  meta divs: 136/223; 2016-2018 `<h2>Company:</h2>` lis: 117-141, with
  founders + HQ metadata) + investment-list snapshots (2023: 758, 2024:
  758, 2026: 1,125). The 2019-2024 portfolio pages render logos without
  text names and are deliberately unparsed — the investment-list
  snapshots cover those years. wayback-pull.py gained two generic
  parsers (`listing_regex`, `js_array_listing`) and a degraded-CDX
  fallback (see §7). The wayback diff recovered ~99 published rows absent
  from every current list — Digg, Burbn (pre-Instagram), Airtime,
  Dropbox, Cloudera, Cyanogen, 21/Earn, Keybase, Helium, Handshake, plus
  direct token positions (Bitcoin, Ethereum, Filecoin) that the 2023
  compliance list carried and later scrubbed (in per decisions §3).
- **Roster**: a16z's people pages share the /author/ namespace with 1,064
  guest authors, and 469 of 572 current staff are operations — so the
  sweep roster is the site team filtered to investment-team +
  board-partners (103 people; `roster.site_team_groups` in config), not
  the author universe. partner-roster.py now unions the site CMS team as
  current-year evidence.
- **EDGAR**: 133-entity vehicle registry (Andreessen Horowitz Fund I-IX +
  LSV/Parallel/Bio/Games/Crypto/Growth families, CNK I-IV crypto funds,
  a16z Perennial, AH Equity Partners GP LLCs, a16z Capital Management);
  876 partner-matched Form D accessions across 451 issuers; 31 companies
  with fund 13D/G or Section 16 streams; 182 issuer round histories
  (594 rounds) for the C2A layer.

## 3. Calibration gate (checkpoint 1) — PASS

20-row membership trap key pre-registered in `golden.json` before any
judge verdict wrote, every answer document-anchored: 8 known-trues across
eras (incl. alias traps Maplebear=Instacart, eShares=Carta and hidden
Tier C trues Nicira, Mesosphere, Meteor), 12 designed falses (ex-partner
and prior-firm seats, founder rows, homonym clusters, board-partner
personal ventures, fund vehicles despite site listing). Blind-protocol
pass: **20/20, zero false members at high confidence**. Honesty note:
one session wrote and took the test; six keys were web-anchored
in-session before the pass — the keys are external documents, which is
what keeps the exercise meaningful (recorded in golden.json's _readme).

## 4. The judge grind

425 Tier C name-match rows existed on the provisional (pre-filter) base;
296 of them were matched only to operations-staff names and were removed
structurally by the roster re-sweep rather than judged. The remaining
**129 investment/board-matched rows were judged individually** (~15 web
arbitrations), plus 30 post-rebuild rows from the loosened nickname
matcher and 7 audit-class rows.

**Recovered members hiding under legal names** (each merged upstream into
its site row): EliseAI (Elise A.I. Technologies), Snackpass (Not Just
Snacks!), Valon (GoServiceOne), Current (FinCo Services), OpenSea (Ozone
Networks — its Brian Roberts is OpenSea's own CFO), Navan (TripActions),
Soylent (Rosa Foods), Ready Player Me (Wolfprint 3D), SignalFx
(SignalFuse), Tenfold (Callinize), Kno (Kakai), Tidemark (Proferi),
Material Security (R Software), Replay (Record Replay), Apex Space (Apex
Technology), All Day Kitchens (All Day Technologies + Virtual Kitchen
Co), D2iQ (Mesosphere), Infinite Athlete (Tempus Ex Machina), Anchorage
Digital (Anchor Labs), Lime (Neutron Holdings), Zenefits (YourPeople),
Jawbone (AliphCom), Airware (Unmanned Innovation), Instacart (Maplebear),
Carta (eShares), Foursquare (Foursquare Labs), Cyanogen->Cyngn (fund
13D/G carried through the rename). Unlisted members recovered: Belly,
Meteor, Magnet Systems, picplz (Mixed Media Labs), Setpoint, Nicira.

**A new adjudicated evidence pattern**: current a16z GPs appearing as
Director of record on in-tenure, in-coverage Form Ds with exact
distinctive names — Adelante Financial (Angela Strange, the same seat
pattern as her confirmed Valon board), Aligned Co / Thingy Thing / Somo
Labs (Anish Acharya), Surely Health / True Medicine (Julie Yoo), PM
Technologies (Olivia Moore). Ruled member at medium confidence as
unannounced deals (the compliance list's own permission-exclusion
explains their absence); each flagged for the PRO-31 A/B pass.

**Exclusion classes recorded** (128 rows in excluded.json, after Erik's HP correction): homonym
clusters (Brian Roberts/Comcast-NBCU-ViewRay, Rod-Rodney-Rodger
Johnson/SpringSource-SandRidge-Elastic, James Sullivan biotech cluster,
Timothy Sullivan/Ancestry); Executive-Officer homonyms (pymetrics' own
co-founder is also named Julie Yoo); partner pre-tenure and founder rows
(Ning/Hunch/3dna, Bond Street, OpenDNS, Big Switch, Ubiquity6, Kyruus,
Knome/Syros, SuccessFactors, Atomist, Zillow); prior-firm board seats
(Discord/Elman-at-Greylock, Strapi/Price-Wright-at-Index,
AirMap/Boyle-at-GC, Jebbit + Marlin9/George-at-General-Atlantic);
board-partner personal ventures (Pacaso, Room 77, Hutch, Switchfly,
Rascoff's SPACs; Shana Fisher's High Line portfolio); Andreessen/Horowitz
personal or pre-firm Section 16 streams (eBay, HP/HPE, Loudcloud,
Orbitz, Blue Coat); fund vehicles despite site listing (A.Capital,
Meta4 Capital, BlockTower Capital); and Starco Brands (the funds' STCB
stock is Soylent's acquisition consideration, not an investment).

## 5. Recall probe

Expected-member lists built from four independent sources and diffed:
the 320-URL announcement sitemap, the fund vehicles' 13D/G subjects,
parametric enumeration (eras x verticals x instruments, ~120 names), and
the peer session's independently measured absent-deal list. Findings:
**three genuine additions** (Seidr, Rewind, LMArena — announcement-only
class, recorded as recall_additions with the firm's own announcement as
citation), one variant merge (Tome Bio(sciences)), and zero parametric
misses — every other candidate was already present under a variant
rendering (Flock Safety = "Flock", Mistral = "Mistral AI") or failed
verification (Discord, Wealthfront, OpenDNS, Adept, Observable,
PicnicHealth are NOT a16z deals; the founder-officer or prior-firm
pattern explains each signal). The site layers carry recall, as on
Sequoia; the probe confirmed the shape rather than breaking it.

## 6. Matcher and code fixes (shared, benefit every investor)

- formd-query.py now applies the `DISTINCT_DESPITE_PREFIX` guard
  (Justin/Justine Moore had attributed Axcient — the Sequoia
  Joseph/Josephine class) and nickname canonicalization.
- people_common.py nickname table: katie/kathryn->katherine (Katie Haun
  files as Kathryn — her attributions were silently unmatchable), andy/
  drew->andrew, eddy/ed->edward, zak/zach/zack->zachary, tony->anthony;
  DISTINCT pairs (chris,christina), (chris,christine) added after a
  Christina Dixon false match. Cost: the loosened matcher surfaced ~30
  new homonym rows (James Sullivan cluster), all judged not_member.
- site-portfolio.py: generic `scrape` site_api type (4 parsers).
- wayback-pull.py: `listing_regex` + `js_array_listing` parsers; nbsp
  normalization; degraded-CDX fallback (statuscode-filtered queries
  timed out during the outage while unfiltered ones answered).
- partner-roster.py: site-team union source + `site_team_groups` filter.

## 7. Environment notes

- **The Internet Archive went down mid-run** (~15:15-16:55 CET,
  "Temporarily Offline" 503s), blocking wayback and CDX layers. The run
  proceeded on a provisional current-team sweep, built v1, cleared the
  calibration gate and ground the judge queue during the outage; wayback
  landed post-recovery through a degraded replay (multi-pass idempotent
  pulls). Residual gaps: no invlist snapshot for 2025 (2024 + 2026
  bracket it); the /investment-list/ page has no captures before 2023.
- **A parallel session ran PRO-32** (investor classification) in the same
  directory. Ownership was negotiated by message (team.json/
  team-members.json/fund-formds.json/investor.json theirs; config,
  sources/site/companies.json, sources/edgar sweeps, base + overlays
  mine); their measured false-attribution clusters seeded my trap set;
  build-firm-profile.py was re-run after the base landed so its
  base-bound assertions executed (clean).
- announcement.md, merit-capital.md, project-scope.md showed as deleted
  in the working tree before this run's first write; neither session did
  it; left untouched.

## 8. Limitations and open debts

- **Alumni roster**: the sweep roster is the current investment team +
  board partners. Departed partners (Haun, Balaji, Walden, Li Jin...)
  are not sweep targets, so deals where ONLY an ex-partner sat the board
  and no list ever carried the company would be invisible. Measured
  risk is low — the compliance list carries recall, and the probe found
  no such miss — but Form D entry anchoring for 2018-2022 crypto rows is
  thinner than it could be. A future pass could add archived
  guest-author-sitemap-based tenure evidence.
- The 2019-2024 portfolio pages are unparsed by design (logo-only
  markup); investment-list snapshots (2023+) and the live union cover
  those years.
- 4 `uncertain` rows for sampling: AMP Fund, Drone Capital I, Revival
  Fund Management (fund-shaped, unidentifiable), Hawthorne Labs (Jordan
  Director 2011, two same-named entities, no documented deal).
- Entity-registry nit: Andreessen's person CIK classifies as desk "us"
  via the name pattern before person resolution, so his Section 16
  streams aren't machine-flagged person-only; the judge caught every
  affected row (eBay, HP, Meta, Orbitz, Loudcloud, Blue Coat).
- 19 registrant-sharing groups (weak CIK joins) are flagged for the
  PRO-31 pass; the verify duplicate tripwire tracks them. Known concrete
  case (spotted by the PRO-32 session): slug `dynamic` (dynamic.xyz, a
  genuine crypto member) weak-joins CIK 1999109 and inherits a ~$1.1B
  entry round from Dynamic Offshore Resources in the issuer-rounds layer
  — its entry_stage/graduation must not trust the Form D band
  (verification duty 3).
- Judged-member rows of the Director-class pattern carry medium
  confidence pending the A/B pass.

## 9. Checkpoint 2 (this report)

The membership-verified base is ready for Erik's sampling: `review.html`
(read-only, sample chip = 18 stratified slugs incl. every uncertain row
and each new evidence class), `base.csv` (1,798 rows, classification
columns empty pending PRO-31), `excluded.json` (134), `golden.json` (the
pre-registered key), `membership-ledger.json` (2,007 durable verdicts).
Corrections in chat are recorded class-wide as `who: "erik"` ledger
verdicts. PRO-31 (classification) is unblocked on sign-off.

## 10. Artifacts

| File | What |
|---|---|
| `base.json` / `base.csv` | Evidence layer / merged published surface (1,798 rows) |
| `membership-ledger.json` | Durable verdict ledger (2,007 verdicts + 23 recall additions) |
| `identity-merges.json` | 30 merge groups, 2 never-merge pairs |
| `excluded.json` | 134 not_member rows, preserved |
| `golden.json` | Membership trap set + pre-registered key (stage set: PRO-31) |
| `decisions.md` | Phase 0 rulings (confirmed 2026-08-18) |
| `entities.json` | 133-entity vehicle registry |
| `sources/site/*` | 4-surface site extraction (companies.json 1,703; team.json is PRO-32's) |
| `sources/wayback/*` | Era snapshots (raw/) + per-year parses (parsed/) |
| `sources/edgar/*` | Sweep, companies, issuer rounds |
| `review.html` | Read-only review surface (checkpoint 2) |

---

# Investor Classification Report — a16z (PRO-32)

Autonomous session 2, run base-less in parallel with PRO-30 per the issue's
design, then recomputed once the base landed the same day. Output:
`investor.json` + `investor/sources.json` (every field populated, per-field
provenance, 8 flags), rendered as the investor panel in the merged
`review.html` (1,807 rows + profile). Taxonomy gate: **0 errors,
0 warnings**. Ingest deliberately not run — it follows Erik's sign-off.

**Prompt count: 1** (kickoff). Coordination with the PRO-30 session ran
session-to-session (ownership split, homonym/alias intel exchange, the
base-landed recompute ping); 0 checkpoint approvals requested.

## Evidence chain

- **AUM [$100B, $106.48B]**: IAPD resolved the adviser as A16Z Capital
  Management, L.L.C. (renamed from AH Capital Management; CRD 160489,
  SEC 801-114985); full ADV PDF pulled, Item 5.F (annual amendment
  2026-03-30): RAUM $106,476,153,956, all discretionary, 119 accounts.
  Bottom is the firm's own "over $100B+" about-page claim (2026-04-30).
  a16z Perennial Management (CRD 324429) is separately registered and
  excluded from AUM and funds — the SCGE precedent applied.
- **Funds: 29, vintage 2015-2026** (`sources/edgar/fund-formds.json`, the
  full AH/Andreessen/a16z/CNK filer sweep: EDGAR company search + local
  Form D ZIPs; 133 filing vehicles + 36 no-Form-D entities). 15 entries
  carry Form D amounts asserted against accessions at build time; 14 carry
  press sizes because post-2022 LP capital enters through the AH Annual
  Fund / Fund Multiplexer conduits (conduits excluded to avoid
  double-counting). Funds I-IV (2009-2014) predate the window.
- **People: 103 published** of 572 in the live CMS payload — the site's
  own Investment Team + Board Partners groups; 469 operations staff
  excluded by flagged scope decision. The WR25 site walls off WP REST;
  the team page embeds the full payload in a `data-payload` attribute
  (escalation ladder step 4). Positions are the site's own flat
  presentation ("Partner" for every investing member, cofounders
  included). Socials 69 LinkedIn / 66 X.
- **investment_range $500K / $25M / $2B**: floor from speedrun's $500K
  upfront check; median recomputed on the final base — partner-anchored
  entry-round median $24,734,937 across 182 membership-verified companies
  (594 rounds in `formd-issuer-rounds.json`; pre-base list-confirmed
  corroboration $30.0M, n=93); ceiling from the $2B Thinking Machines
  seed a16z led in July 2025, consistent with Growth Fund V concentration
  capacity.
- **Stage / geo / scope** from the firm's own filters and language:
  portfolio filters Seed/Venture/Growth, the LSV (Late Stage Venture)
  family, speedrun's pre-seed/seed scope; nine-sector about-page
  enumeration crosswalked to the closed focus taxonomy; offices page
  (5 US + Seoul + Tokyo) and named investment-list companies for geo.
- **Icon** via the PRO-53 flow from the firm's own 270px CDN favicon.

## Post-base reconciliation (same day)

1. `build-firm-profile.py` re-ran against the base: all 8
   notable_investments asserted against auto_confirmed rows; 15 fund
   accessions asserted against filings.
2. **Focus recompute guarded off as unrepresentative**: only 251 of 1,807
   base rows carry sector tags (the speedrun surface exclusively), so a
   base-derived focus would describe the accelerator slice, not the firm.
   The build now publishes the recompute only above 25% tag coverage;
   the firm's own nine-sector enumeration stands, and the speedrun-tag
   crosswalk is staged in config.json for whenever coverage improves.
3. **Median moved $30M → $25M** with the base-anchored recompute (182
   companies vs the 93-issuer pre-base subset). A few distribution tails
   ride on weak CIK joins (slug `dynamic` at $1.1B); PRO-31's standing
   weak-CIK audit is the cleanup pass and the median is insensitive to
   them.
4. The departed cross-check stays structurally empty: the roster is the
   current site team by design (Wayback CDX offline all session); the
   alumni limitation is §8 of the PRO-30 report above.

## Script changes

- `build-firm-profile.py`: tolerates a missing base (skips the two
  base-bound checks loudly, re-runs them once the base exists); focus
  recompute guarded by tag-coverage representativeness; investing-bucket
  vocabulary generalized to a16z's "investing".
- `run.py review`: renders the investor panel over an empty company table
  when no base exists, so the profile session ends at the review surface.

## Debt, all flagged in the sidecar

Entry-round median excludes unfiled raises (speedrun SAFEs, 4(a)(2));
four of nine focus values await the investor-side focus migration before
they filter on the frontend; investment_geo "other" is inference from
named deals + offices, to verify or trim in review.

# Company Classification Report — a16z (PRO-31)

Run: 2026-08-30/31, continuing the PRO-30 base on this branch. Columns
delivered on all 1,722 canonical rows: status, valuation_range (+usd/asof/
source/citation where 1B+), entry_stage (+source/citation), hq_country,
hq_city, focus, seed_to_a_graduation, flags, note. `verify` is clean.

## 1. Shape of the result

- 1,722 rows (from 1,796 pre-rebuild): 103 duplicate rows absorbed by the
  identity overlay, 136 excluded total, 1 row restored (nitra).
- valuation_range: 1,557 below_1b / 123 1b_plus / 34 10b_plus / 8 100b_plus.
- entry_stage: 1,057 Seed / 436 Series A / 229 Growth - the Seed weight is
  the seed program + speedrun + TxO + crypto seeds, and matches the firm's
  own accelerator-heavy shape.
- focus: twelve-value taxonomy on 1,327 rows; 395 rows are null-focus
  unidentifiable tail (each carries stage_prior/country_prior conventions).
- C2A cohort: 60 rows, 11 graduated (18.3%), every row leg-verified or
  flagged cohort_unverified.
- hq_city on 1,084 rows (141 cities; SF 444, NYC 151, LA 66).

## 2. Method

1. Judgment grind: 34 queue batches + 3 supplemental (the 22 layer-complete
   famous rows, merge-pair reconciliation, contradiction flags), ~1,540
   model-judged rows recorded through `run.py record` under the source gate.
2. Web pass (5 research agents, 103 unique needs_web_value targets):
   every suspected-1B+ figure pinned with source web_verified + asof +
   citation, or left flagged. 100 pinned; ideogram, planetscale and
   ultima-genomics have no credible public mark and stay flagged.
3. Adversarial A/B agent over the visible slice: 30 claims checked
   (site-acquired buyers, identity collisions). 22 confirmed, 5 refuted
   and corrected, 3 inconclusive (kept flagged).
4. Citation pass (3 agents, 116 lookups): every 1B+ row now has a cited or
   filing-structural entry stage, or carries cite_pending; every public 1B+
   row has a cited market cap. 17 entry stages were corrected by citations
   (e.g. okta B->A, robinhood B-era->seed, dialpad seed->B, decagon A->seed,
   base-power A->B, clickup B->C).

## 3. Findings Erik should know about

- Membership flips (agent verdicts under standing rulings, for review):
  polychain (LP stake in Polychain's funds, ruling #4) and ycvc-w14 (the
  YC W14 batch vehicle a16z backed as an LP, rulings #4/#6) are now
  not_member and sit in excluded.json.
- nitra was restored: the base scrape had glued "NG.CashNitra" into one
  artifact row; Nitra's a16z backing is announcement-corroborated. The
  artifact row stays, flagged, pointing at both real rows.
- The site's acquired-bucket markers were mostly right (metronome->Stripe,
  replicate->Cloudflare, stainless->Anthropic, astral+promptfoo->OpenAI,
  cursor->SpaceX at $60B - real, not a scrape error) but four were wrong
  company matches and got corrected: apollo (GraphQL co is private),
  exa ($2.2B, independent), mercury (Mercury Technologies, $5.2B,
  private), viggle (Viggle AI independent; Perk bought the old TV Viggle).
- Farcaster wound down (Jan 2026, capital returned, protocol to Neynar) -
  status acquired with the $1B 2024 mark retired under the current-value
  convention.
- Six layer identity collisions carry quarantined figures (mosaic,
  seismic-systems, coalition-systems, mara, post, cadre): the classification
  shadows the wrong-entity figure and the dispute flag explains why.
- 98 identity-merge groups now (39 at PRO-30 close): rename chains
  (RigUp->Workrise, TransferWise->Wise, MakerDAO->Sky, Tachyon->Alluxio,
  Firespotter->Dialpad), entity-vs-product twins (Merkle/Farcaster,
  Tlon/Urbit, VHS/Zed Run, Translation/UnitedMasters), typo scrapes
  (BluuStacks, Yield Guide Games, kydio->Skydio flagged), and the EDGAR-
  resolved Thingy Thing -> ALIGNED Co -> Extra chain.

## 4. Debt, all flagged in rows

- needs_web_value x3 (ideogram, planetscale, ultima-genomics): no public
  mark exists; below_1b held conservatively.
- cite_pending: 1B+ rows whose a16z entry round no source documents
  (alation, amplitude, doordash, dropbox, gusto, kailera, openevidence,
  smartasset, twilio, webflow, zapier, cohere-networks + a few more) -
  membership rests on the site listing; the entry stage stays model-judged.
  Notable: webflow's famous $72M Series A was Accel-led - the a16z-round
  assumption was wrong, now corrected.
- identity_uncertain tail (~100 rows, mostly below_1b unidentifiable list
  entries) and the null-focus 395 - conventions applied, nothing asserted.
- Stale-float vintage: public caps sourced from H2-2025 filings were
  re-cited from market data at the citation pass for all 1B+ rows; sub-1B
  public floats keep their filing vintage.
- kydio and the sky/maker read are merge calls flagged identity_uncertain
  for the sample review.

## 5. Artifacts

- base.csv (1,722 rows, full classification columns) - the ingest surface.
- review.html - flat rows, click drawer, flag chips (cite_pending etc.).
- classification.json (1,795 keyed rows incl. 73 orphaned pre-rebuild keys,
  reported by verify as info), membership-ledger.json (2,008 verdicts),
  identity-merges.json (98 groups), scratch/webpass/* (agent evidence).

Exit criterion: Erik's classification sample sign-off via review.html.

## 6. Post-review corrections (Erik, 2026-08-31)

- abacus removed (who:erik not_member, overriding the site-listing seed;
  no independent evidence ever surfaced). arpeggi confirmed member
  (who:erik).
- adelante-financial-holdings-inc and pm-technologies-corp excluded under
  Erik's conditional ruling: their only evidence is a partner as Director
  of record on the Form Ds (Strange 2020-21, Moore 2025) - no a16z fund
  entity on any filing, no announcement, identities never resolved.
  Partner-director-only = personal-seat class.
- Base 1,722 -> 1,719 rows (139 excluded); verify clean; re-exported.
- Process ruling baked into COLLECTION.md par.9: ingestion is gated on
  Erik's explicit approval, never autonomous. The three removed rows
  still sit in public.companies from the pre-ruling ingest - cleanup
  awaits Erik's decision.

## Cross-investor alignment (2026-09-03)

`run.py verify` now compares every row with the other investors' published
`base.csv` on `status` and `valuation_range` (COLLECTION.md §10 invariant
10; rulings in `data/collection/cross-investor.json`; method in the
Lightspeed report). First run on a16z: 59 disagreements, most of them
homonyms and thin unresolved pairs now ruled distinct or accepted; after
resolution 0 (4 accepted). Recorded with
`who: cross-investor-align-2026-09-03`; reproducible from
`data/collection/shared/cross-align/2026-09-03.py`.

**Rows changed (12):**

| slug | before | after | evidence |
|---|---|---|---|
| doordash | public / 100b_plus $102.6B (Aug 28) | public / 10b_plus $96.35B | same-day cap shared with Sequoia; the band edge had been an as-of artifact |
| harvey | 10b_plus $11B (unicorn_list) | 10b_plus $11B (web_verified) | source upgraded to the round: $200M at $11B post 2026-03-25 |
| lookout | 1b_plus $1B (2014) | below_1b, no figure | collapse evidence supersedes the stale primary (§6): consumer business sold to F-Secure 2023, cloud business to Fortra 2025, secondaries ~$296M |
| unconventional-ai | below_1b ("undocumented") | 1b_plus $4.5B | the Dec-2025 $475M seed a16z co-led with Lightspeed |
| groupon | public / below_1b ($618M float) | public / below_1b $769M cap | cap replaces the float (§6); same-day with Accel |
| eon | unknown (MX wikidata match) | private | identity resolved (medium): Endeavor Optical Networks, the 2026 seed a16z co-led; not Eon the cloud-backup company, which has no a16z round |
| airtime | unknown | defunct | wound down (this run's own note) |
| otter, pyn, ciridae | unknown | private | operating: Otter (Sequoia-led A 2021, a16z seed), Pyn (site live), Ciridae ($20M seed May 2026 with Accel) |
| parsable, iron-fish | private | acquired | CAI Software (Sep 2024); Coinbase acqui-hire (2025-03) |

**Counts.** cumulative $1B+ 165 → **165**, $10B+ 42 → **42**, $100B+ 8 →
**7**; valuation_range 1554 / 123 / 34 / 8 → **1554 / 123 / 35 / 7**;
status 1033 / 262 / 108 / 49 / 267 → **1035 private / 264 acquired / 109
defunct / 49 public / 262 unknown**. `verify` clean. **Re-ingested 2026-09-03** with Erik's
approval; the database now derives 165 / 42 / 7 and 49 public on 1,719
rows.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Ninety-nine published rows carried `identity_uncertain`, the largest set in
the sweep, and **eighty-nine of them now read `undetermined`**. a16z's flagged
rows are one-word list entries — `admin`, `blank`, `bold`, `if`, `pure`,
`special`, `uno`, `wave` — where the run wrote "identity unresolved" and then,
because invariant 1 demanded a filled cell, published a Seed anyway.

The second half of that pattern is what makes these rows dangerous rather than
merely thin: a deterministic layer had joined each bare name to SOMETHING and
the note records it as "left standing". `cavia` carries a defunct-JP match to
a Japanese game developer, `paloma` a JP match to a water-heater maker,
`insitu` a match to the drone company Boeing bought in 2008 — before a16z
existed — and `cohere-networks` a $6.8B/CA match to Cohere the AI company.
`concept`, `endra`, `glimpse`, `mirage` and `damora-therapeutics` each carry a
public-float match that reads as a ticker collision. Those are joins on a
name, not identifications, and a row that asserts nothing cannot carry them
into a metric.

**Seven rows are named and lose the flag**: `daylight` (the home-energy
company whose 2024 seed a16z led), `dispatch` (sidewalk-delivery robots, 2016),
`eon` (Endeavor Optical Networks — a later pass resolved it and the "identity
unresolved" wording was never retired), `libra` (the Libra/Diem association,
where the open question is membership rather than identity), `sky` (MakerDAO's
rebrand, already merged with `maker`), `treeline` and `atoms`.

**Three rows are one company under two renderings**: `locomobi` against the
base's `locombi`, `butter-sysems` against `butter-systems` (the list's own
typo), and `ng-cashnitra`, a scrape artifact that glued NG.Cash and Nitra —
two real a16z companies — into one row that names neither correctly. They are
flagged `identity_conflated` and recorded rather than merged: the merge file
and the rebuild that applies it belong to a pass that owns this base.

### One thing worth a decision: the SPEEDRUN rows

Nine of the eighty-nine (`auto`, `cascade`, `coalition-systems`, `darwin`,
`general-magic`, `mara`, `oasis`, `panorama`, `sun`) are live SPEEDRUN
accelerator listings, and they lose something real. The program's $500k terms
DATE and SIZE the entry — that is more than most unnameable rows have — but
the terms describe what a16z offers every speedrun company rather than a round
this one took, which is the same reason YC's batch-deal record cannot carry a
stage on an unnameable row. They are treated the same way here, deliberately.
If the pipeline gained a `program_terms` stage source, ranking with the Form D
sources under the carried-through exception, these nine would keep a Seed that
is genuinely evidenced. That is Erik's call, not this pass's.

`verify --skip-cross` still fails on this book for reasons that predate the
pass — 1,017 problems, all of them the S2A debt: retired booleans,
`cohort_unverified` flags and Seed rows with no graduation status. None of the
reclassified rows appears among them. The seed cohort reads 967 rather than
1,056.

### Addendum 2026-09-19 (later) — SPEEDRUN is Pre-Seed, by Erik's ruling

Erik ruled that a programme entry on standard small-check terms is a
**Pre-Seed** entry, and that it applies to every small-cheque programme
investment rather than to a16z alone. All **250** SPEEDRUN rows — cohorts
SR001 through SR007 — now read `entry_stage: Pre-Seed`, source
`program_terms`, confidence high.

This is the better answer to the question the earlier addendum left open. The
nine unnameable speedrun rows were not losing a Seed, they were losing a
PRE-SEED, and what carries it is the programme's documented $500k terms rather
than anything about the company. `program_terms` now ranks with the Form D
sources as a transaction-level source: it survives a missing company name, so
ten unnameable rows keep a stage while staying `identity_unresolved`.

Two consequences in the numbers. The seed cohort falls **967 → 727**, because
a Pre-Seed entry is not a Seed entry and the seed-to-A column does not apply
to it — 47 of those rows had carried a legacy boolean `False` graduation,
which is 47 model-sourced "no"s removed from a rate they never belonged in.
And `verify`'s problem count falls 1,017 → 777, all of the difference being
speedrun rows that no longer owe a graduation status.

**One rule had to give**, and it gave in the right direction. `undetermined`
was tied symmetrically across `entry_stage` and `valuation_range`: both or
neither. The ten unnameable speedrun rows break that — a programme's terms
give the stage, and a company we cannot name still cannot be valued — so the
tie now runs one way only. An undetermined stage forces an undetermined band
and an undetermined graduation; an undetermined band stands on its own. The
metric basis drops a row with ANY undetermined column, in `verify` and in
`recompute_investor_metrics` alike, so those ten leave every distribution.
Migration `20260919120000_undetermined_propagates_downward.sql` carries the
database half and is NOT pushed.

## Addendum 2026-09-22: S2A with every Seed row decided (PRO-132)

The run published 18.3% on a 60-row cohort. PRO-132 makes the absence of a
later round a finding: a Seed row past the 24-month clock with no evidence of
a later round did not graduate, and every no records the dated search that
found nothing (the firm's archive, the Form D sequence for a US company, at
least two publisher surfaces; COLLECTION.md §6). The 546 open rows were
judged in thirteen batches.

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 246 | 34 | 212 | 88 | 124 | 41.5% | 100% |

Of 246 seed entries, 34 were too recent to count; of the 212 that remain,
41.5% raised a later round. Of the 124 that did not, 37 rest on a cited end
(an acquisition or shutdown with no round between it and the seed) and 87 on
a dated search of the named surfaces. No no rests on the filings: a16z's seed
book barely files, which is why the Form D layer decides one row in the whole
book.

**413 nameable rows read `undetermined` in the stage.** a16z publishes no
round word and no year on its portfolio page, most of its seeds never file a
Form D, and the judge contract refuses an archive capture as an entry date,
so on those rows nothing dates a16z's entry. They leave the S2A cohort, which
is why 212 rows carry the rate for a 1,719-row book. Several are companies
whose later rounds are well documented (Flexport-scale names such as Clay,
Roblox, Refinery29 in the First Round book have their a16z counterparts here:
AppNexus, Homejoy, Aviate, Balanced, FundersClub, Panorama Education).

What moved:

- **The TxO and CSX programme rows are Pre-Seed.** Erik's rule of 2026-09-19
  (COLLECTION.md §6) makes a standard-terms programme cheque a Pre-Seed entry
  citing the terms document; a16z's own first-cohort post gives TxO's standard
  terms ($100K on a SAFE converting to 7%), and the CSX posts give $500K. 25
  rows moved out of the Seed cohort on that rule, most of them nos, which is
  the largest single correction in this book. `documentation/decisions.md` §8
  still carries the older reading (programme cheques as Seed by instrument)
  and should be restated.
- Re-staged out of Seed where a16z's own post or the press names its first
  money at a later round (about 30 rows), among them Product Hunt, Optimizely,
  Canvas Networks, Daylight, Dynamic, Oboe, Octant Bio, Mind Robotics, Netris,
  NextHop, Ollin Bio and Mentari Therapeutics; in review, Tidemark and its
  duplicate Proferi (a16z joined Proferi's first round in October 2010 and the
  next round is called its Series B, so the entry is a Series A) and Rezo
  Therapeutics (FinSMEs names its $78M a Series A).
- Form D verdicts overturned: Optimizely (a16z led the 2014 Series B, three
  years before the filing the layer read), Orbit (a named $15M Series A in May
  2021), Capriza (a $23M re-raise in 2016), App.net (a16z's own money went in
  2013, not at the 2010 filing).
- Erik's Black Forest Labs row now carries the August 2024 seed as its entry
  date and cites the Series B for the graduation; his other values stand.
- Post and Yellow carried public-company flags from weak-CIK matches
  (Post Holdings, and an unrelated registrant); `is_public` is false on both.
- Yuga Labs is a no under the invariant-7 exemption: its $4B mark is the
  seed's own, not evidence of a later round.

`c2a_rate_max` stays at the 0.80 default. `verify` reports no graduation
problem. Four pre-existing rows (honor, loft, odyssey, superhuman) and two
cross-investor pairs (Chute, Forte) are valuation and stage debt for PRO-121,
not S2A's.

For Erik: the **413 undetermined stages** are the number to look at before
publishing this book's rate; the choice that produced them is the one in the
PRO-132 wrap-up comment (whether a firm-listing archive capture may date an
entry). **TxO and CSX** moving to Pre-Seed follows your programme rule, but it
contradicts a16z's own decisions.md §8, so say which one governs.
