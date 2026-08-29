# Company Base Report — a16z (PRO-30)

Single-session autonomous run, 2026-08-29. Scope: the membership-verified
Company Base (PRO-30, "autonomous session 1, part 1"). Classification
columns (`status`, `valuation_range`, `entry_stage`, `hq_*`, `focus`, C2A)
are PRO-31, which continues on this base after Erik's sample sign-off.

**Prompt count: 1** (the kickoff: "execute the a16z base collection as per
linear issue PRO-30 / work diligently in full autonomy"). Checkpoint
approvals requested: 0 (both checkpoints posted as status and continued,
per the kickoff's autonomy instruction). Corrections: 0 at the time of
writing; Erik's sample sign-off is the open exit criterion.

## 1. Result

**1,807 published rows** — 1,165 Tier A / 629 Tier B / 13 Tier C — every
row carrying a durable membership verdict: **1,803 member, 4 uncertain**
(sampling-marked), plus **127 not_member rows** preserved in
`excluded.csv`. Verdicts by evidence class: 1,792 site_listing,
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

**Exclusion classes recorded** (127 rows in excluded.csv): homonym
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
  PRO-31 pass; the verify duplicate tripwire tracks them.
- Judged-member rows of the Director-class pattern carry medium
  confidence pending the A/B pass.

## 9. Checkpoint 2 (this report)

The membership-verified base is ready for Erik's sampling: `review.html`
(read-only, sample chip = 18 stratified slugs incl. every uncertain row
and each new evidence class), `base.csv` (1,807 rows, classification
columns empty pending PRO-31), `excluded.csv` (127), `golden.json` (the
pre-registered key), `base-verification.json` (2,007 durable verdicts).
Corrections in chat are recorded class-wide as `who: "erik"` ledger
verdicts. PRO-31 (classification) is unblocked on sign-off.

## 10. Artifacts

| File | What |
|---|---|
| `base.json` / `base.csv` | Evidence layer / merged published surface (1,807 rows) |
| `base-verification.json` | Durable verdict ledger (2,007 verdicts + 23 recall additions) |
| `identity-merges.json` | 30 merge groups, 2 never-merge pairs |
| `excluded.csv` | 127 not_member rows, preserved |
| `golden.json` | Membership trap set + pre-registered key (stage set: PRO-31) |
| `decisions.md` | Phase 0 rulings (confirmed 2026-08-18) |
| `entities.json` | 133-entity vehicle registry |
| `sources/site/*` | 4-surface site extraction (companies.json 1,703; team.json is PRO-32's) |
| `sources/wayback/*` | Era snapshots (raw/) + per-year parses (parsed/) |
| `sources/edgar/*` | Sweep, companies, issuer rounds |
| `review.html` | Read-only review surface (checkpoint 2) |
