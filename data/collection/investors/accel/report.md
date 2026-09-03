# Company Base Report — Accel (PRO-62)

Single-session autonomous run, 2026-08-31. Scope: the membership-verified
Company Base (PRO-62, "autonomous session 1, part 1"). Classification
columns (`status`, `valuation_range`, `entry_stage`, `hq_*`, `focus`, C2A)
are PRO-65, which continues on this base after Erik's sample sign-off; the
review surface already shows the deterministic pre-fills (SEC float,
Wikidata, unicorn list) with their flags, judged by no one yet.

**Prompt count: 4, final** — (1) the kickoff ("execute the accel base
collection as per PRO 62; work diligently in full autonomy", with the
pre-start Atoms ruling), (2) "check whether wayback now works and
complete the base collection" (→ the §5b completion pass), (3) a review
question on capture corroboration, (4) the classification go-ahead that
carried the sample sign-off. Checkpoint approvals requested: 0. **Erik
rulings recorded: 1** (decisions #4); **row corrections at sign-off: 0**.
Sign-off recorded 2026-09-01; PRO-62 marked Done. A parallel
session ran PRO-68 (firm profile) per §11; coordination stayed
session-to-session.

## 1. Result

**886 published rows** — 776 Tier A / 49 Tier B / 61 Tier C — every row
an affirmed **member** (0 uncertain), plus **115 not_member rows**
preserved in `excluded.csv`. Ledger: 1,015 verdicts (14 orphaned keys
from slug canonicalization, expected). Published verdicts by evidence
class: 819 site_listing, 35 formd_adjudicated, 21 fund_filing, 11 web
(recall additions); by author: 840 evidence-class seeds, 46 judge
verdicts on published rows.

Evidence coverage: 803 rows on the firm's own live surfaces, **791 with
capture-archive corroboration** (the Common Crawl layer, §5b — this is
what moved Tier A from 142 to 776), 156 with partner-attributed Form Ds,
64 with fund 13D/G / Section 16 streams, `first_seen` dated on 856,
`partners_site` (the CMS's own per-deal partner attribution) on 731.

*(Checkpoint-2 state before the completion pass: 871 rows at
142 A / 663 B / 66 C, 76 excluded, 947 verdicts — superseded by §5b.)*

## 2. Evidence layers (Accel parameters)

- **Site (layer 1b), Sanity CMS + program surface, 804-row union**: the
  accel.com CMS (project 458oembh, dataset `production`) is publicly
  GROQ-queryable — no XHR-watching needed; `site-portfolio.py` gained a
  generic `json_list` parser (any headless-CMS query API) and the config
  carries the projection. 774 non-archived company docs with per-deal
  partner refs, `firstInvestDate`, `initialInvestmentType` (the firm's
  own entry-stage claim: 299 series-a / 274 seed — PRO-65 evidence),
  `firstExitType/Description`, HQ, founders. 17 `archived==true` docs
  were quarantined (deliberately unpublished — not site-listing
  evidence; four returned as cited recall additions, §5). Person docs
  carry the team incl. an "Emeritus" office (Patterson, Swartz, Golden,
  Comolli, Efrusy) and 94 archived/departed people. atoms.accel.com
  (Webflow, Finsweet JS pagination the CDN defeats for curl) was driven
  in the browser pane — 39 cohort companies with years; the program FAQ
  states Atoms invests $1–2M per selected startup, which is what
  decisions #4 turns on. No marketing-rule compliance list exists —
  recall rides the CMS + news archive instead (implication measured in
  §5: the probe found real scrubbed-deal gaps).
- **Roster**: provisional (CDX blocked by the IA outage) — the 69
  "investing" persons from the CMS (deal-referenced or Emeritus),
  filtered from 207 person docs via a GROQ-computed group. The
  Breyer/Gouw/Wagner/Fenton-era alumni are NOT sweep targets yet; the
  CDX people-page expansion re-runs when the archive recovers (§8).
- **EDGAR**: 181-entity vehicle registry (flagship III–XVI + Accel 17
  (CIK 2137992, from PRO-68's fund sweep), Growth I–VIII, Leaders 1–5,
  London II–9, India III–9, Keiretsu + Internet funds, Investors
  94–2013 side vehicles, Circle Fund 2026 + Core). Namesake filers
  (Accel Investments LLC of Plano, Accel Investor I/II of Akron — PRO-68
  intel), Accel-KKR, Accel Entertainment, "Accel Meritech *" (ruling #8)
  and the Breyer/Gouw/Wagner personal entities all sit desk `external`,
  never crawled. 689 partner-matched Form D accessions across 353
  issuers; 65 companies with fund ownership streams (1997 Farallon 13G
  → 2026 Ethos Section 16); 209 issuer round histories for PRO-65.

## 3. Calibration gate (checkpoint 1) — PASS

21-row membership trap key pre-registered in scratch (commit d0e6808)
BEFORE the base was built, every answer document-anchored: 9 trues
across eras/desks/instruments (1993 UUNET, Facebook, London Supercell,
India Flipkart, Atoms Spendflo, alias traps FreshDesk→Freshworks and
Quidsi→Diapers.com, hidden fund-filing true YuMe) and 12 falses
(Accel-KKR, IDG-Accel, Fenton/Twitter ex-partner, Breyer/Walmart
personal Section 16, pre-tenure officers Sanghvi/Maplebear and
Colyer/GoPivotal, founder-homonym PostEra, Larson and Kumar homonym
clusters, own vehicle, namesake). Blind pass **21/21, zero false
members at high confidence**; all six designed falses verified
structurally absent from the built base. Honesty note: one session
wrote and took the test; the keys are external documents (golden.json).

## 4. The judge grind

109 Tier C name-match rows judged individually (~25 web arbitrations),
all recorded through `run.py record` in one pass. What the grind found:

**Aliases recovered into listed rows** (each a curated identity merge,
24 groups total): FreshDesk→Freshworks, Evenflow→Dropbox,
AgileBits→1Password, Quidsi→Diapers.com, Visual Supply→VSCO,
HasOffers→TUNE, 2tor→2U, Soham→Zenoti, WizRocket→CleverTap,
Good Methods Global→CareStack, InsuranceZebra→The Zebra, 1661→GOAT,
SportsBlogs→Vox Media, Groupay→GoCardless (the original company name),
TherapyMatch→Headway, RSE Markets→Rally, Speakeasy Labs→Speak,
Nino Finance→CoinTracker, Linked Store Cayman→Nuvemshop (identified via
the Form D's own officers: Santiago Sosa + Kaszek's Szekasy),
WC SACD→Aura (the Intersections take-private JV), La Casa→CasaOne,
Enstage→Wibmo, iPolipo→Jifflenow, InVisionApp→InVision. The CMS's own
partner refs validated most merges (the Form D director matches the
listed partner).

**Members judged in on documented deals** (34 on published rows):
Aptana, Alfresco, Amitree, Atomist, BranchOut, Collective Media,
Complex Media, DataGravity, Elo7, Endorse, Exclusively.in, Grovo,
High Gear Media, Icera, Ingenuity, Knewton, Kekanto, Lot18, Metacafe,
MetraTech, Mitra Biotech, Neumob, OpenX, Paxata, PrimaryData,
RGB Networks, Terracotta, Transera, TRUSTe, TUNE, M.Gemi (RCW, Inc.),
ClusterHQ, Point Wild (the May-2024 Aura split-off — never-merged with
aura by rule, the HP/HPE shape), and Autonymy (Director-pattern:
Loughlin in tenure, identity resolved, unannounced — flagged for A/B).

**Exclusion classes recorded (76 rows)**: the John-Larson homonym
complex — at least three distinct non-Accel John Larsons (John M.
Larson/Career Education explains 2tor+2U+Triumph Higher Education; a
mining-cluster John E. Larson explains Nevada Exploration, URZ3,
Vortex, Acapulco Gold; property/insurance Larsons explain Prairie View,
Preneed, Belize LLCs, CAVA, WageWorks, Zipwhip, MBA Polymers, VIA
Pharma, i2H, VIE, Anapanda, Mile High); the Dr.-Amit-Kumar biotech/
mining cluster (Aeolus, CombiMatrix, Actym, NGX Bio, BioCeryx, UberSeq,
Ascent Solar, BlackRock Gold+Silver) plus pre-tenure tech Amit Kumars
(Palaran, Socialscope, Vurve); the Matthew-Robinson founder/exec
homonyms (PostEra's own CTO, MyMedicalShopper, Attributor, Chideo,
Left Hand Robotics, Totum, Rampart, Escape Velocity, Juniper Health,
Method Ventures, NEIC); **prior-firm and employment seats caught live**:
Jonathan Turner's e.ventures-era boards (Cameo/Baron App, Zumper),
Ethan Choi's move to Khosla in early 2024 (Anrok — Khosla led its
Series B with Choi, Outsmart Education), Sagar Sanghvi as Instacart's
CFO pre-Accel (Maplebear) and as Abridge's CFO post-Accel, Adrian
Colyer as Pivotal's own CTO pre-Accel (GoPivotal), Seth Pierrepont
pre-tenure (XYLOS), Carlo Biggio's Hedosophia interlude (CAST AI);
Swartz personal biotech seats (Bullet, GreenLight); Golden uncorroborated
(Trufa); Levine common-name cluster (11 rows, each absent from the
firm's own attribution map); **stock-as-consideration** (Viggle — Accel
IX's shares came from Viggle's $30M acquisition of Accel-backed
Wetpaint; the a16z Starco class); and five unresolved partner-director-
only rows excluded under Erik's a16z narrowing (Osmnez, Enfinio,
Zettata, Galena 2013, Neo on Business, Telescope).

**The twin resurrection caught**: 2u-inc was excluded as not_member
before the identity overlay ran, so its 2tor-inc duplicate resurfaced
unjudged on the next rebuild — the exact HP/HPE class the playbook
warns about, now with its own verdict (COLLECTION.md write-back
proposed: a merge canonical excluded pre-overlay leaves its duplicates
needing their own verdicts).

## 5. Recall probe

Expected-member lists from independent framings, diffed against the
base: parametric enumeration (pre-registered blind in scratch before
the build), the 513-URL news sitemap, the fund vehicles' 13D/G subjects
(in the base by construction), the archived-CMS quarantine, and press
sweeps (recent window + fund-close context). **Eleven recall
additions**, every one from a structural blind spot, each cited:

- Pre-Form-D-window + scrubbed: **XenSource** (2005, acq. Citrix),
  **Glam Media** (2005, Mode Media, wound down), **Wetpaint** (2007 —
  surfaced by the fund-filing audit: Accel IX's Viggle 13G is the sale
  consideration).
- Non-US, scrubbed: **Wonga** (2009 London — collapsed 2018),
  **EduK** (2015 Brazil), **Stoqo** (2018 Indonesia — shut 2020).
- Announcement-only (never on the companies list): **SLAY** (2023),
  **Deviceplane** (2019) — both cited by Accel's own news posts.
- Archived-CMS confirmed: **Pillow** (2022 — shut 2023), **Kubric**
  (2019), **VoiceOps** (2018).

Rejected with reasons (recorded here): Niku, Centillium, Jasmine
Networks, Veoh, Zego, Bux, Prismatic (enumeration candidates with no
supporting evidence); Synopsys, SentinelOne, Amino (archived CMS rows
with no corroborating Accel evidence — likely CMS data errors);
Behtar, Farcast Biosciences, Names & Faces, Cogsy, Youshd, Zopsmart
(archived rows with partner attribution but no external documentation —
left out, sampled for Erik); Folio by Amitree (product of the Amitree
row). The July-2026 press window (Agave, Plazza, Paper, AegisAI) is
fully on the CMS already — the site carries recall, as on Sequoia and
a16z; the probe's real catches were the scrubbed and pre-window
classes, which is exactly the survivorship correction wayback will
deepen when the archive recovers.

## 5b. The completion pass (Common Crawl layer)

The Internet Archive outage outlasted the run (still down at second
close; a publicly reported Wayback outage from ~16:11 CET), so the
capture layer was completed from the **Common Crawl index** instead —
`scripts/commoncrawl-pull.py`, paced+resumable across all 127 CC crawls
back to 2008, writing the exact per-year shape `wayback-pull.py` owns
(IA's deeper pull converges over it idempotently on recovery). Two
hard-won correctness rules live in the script: CC throttles parallel
clients into silent empties (serial pacing + explicit no-captures
markers only), and a **catch-all shell filter** — accel.com 2018 served
one identical body for any `/companies/<slug>` (453 junk captures of
crawler-invented slugs like adobe/amazon, all one digest, dropped).

Yield: 814 clean company-page slugs (2017–2026) and 216 people slugs
with capture-year tenure windows that match known departures exactly
(Breyer 2014–2016, Lixandru 2017–2019, Pierrepont 2018–2021). Effects:

- **Tier promotion 142 → 776 Tier A** (site + capture = two sources).
- **The archived-CMS dilemma resolved by evidence**: archived docs WITH
  years of captures were real listings → members (Snorkel AI, Cogsy,
  Youshd, Names & Faces); archived docs with ZERO captures were never
  published → correctly out (SentinelOne, Synopsys, Amino).
- **New members from removed listings**: Instabug, askSpoke, Clover,
  Mensa Brands, Produze, Nymble, Casual, Tesseract — and **Corsa**, a
  2026 page marked "(ACCEL INVESTMENT) / Seed-Series A / Andrei
  Brasoveanu" served in May 2026, read straight from the CC WARC, now a
  404 and absent from the CMS: an unannounced deal published briefly and
  pulled.
- **Ten more rename-alias merges** from pre-rename page captures:
  CureFit→Cult.fit, MemSQL→SingleStore, MobStac→Beaconstac,
  Bayestree→Sainapse, IndiGG→KGeN, WorldRemit→Zepz, MessageBird→Bird,
  dashdash→Rows, UserLeap→Sprig, EdgeDB(Gel)→edgedb; plus three
  CMS-slug artifacts (brds=Bird Scooters, saltpay=Teya, nova=Nova
  Intelligence).
- **The roster tripled (69 → 217)** with real tenure windows, and the
  re-sweep grew to 1,086 accessions / 465 issuers / 92 matched people.
  The 41-row delta judged: two new members — **Zoomdata** (Accel led
  the 2014 B; Jake Flomenberg, an ex-partner only the capture roster
  could attribute) and **Booyah** (Accel led the $20M 2010 B, Breyer's
  one genuine fund seat in the delta) — against a clean sweep of
  exclusions that exercise the new seat-dating rule: Breyer's parallel
  Breyer-Capital practice (Legendary, Wickr, Datalogix — the press
  itself says "who also remains a partner at Accel", Woven, EDO,
  Paige.AI), Destin's Atlas-era (AdSafe/IAS, Kinvey, Seatwave) and
  Stride-era rows, Conde's personal boards (Digital Reasoning,
  Centripetal, MassMutual separate accounts), Druva (its own CEO is a
  Jaspreet Singh homonym), FullStory (Estevez advisory, no Accel in the
  cap table), and a brian/brianna matcher gap (Triumph Gold) now fixed
  in `people_common.py`.
- Junk namespace slugs (all, see-all, amitree-2) purged and configured
  out; the builder now lets the site's own rendering own name+slug (a
  capture slug that created a row first was naming it — "Assemblyai").

## 6. Matcher and code changes (shared, benefit every investor)

- site-portfolio.py: generic `json_list` parser (headless-CMS query
  APIs — Sanity GROQ here), `file_list` parser (browser-pane extraction
  snapshots with provenance readme), `team_sources` writing team.json
  through the same machinery, string-sector hardening.
- build-company-base.py: site CMS partner refs feed `partners_site`;
  the CMS's own invest-year is a `first_seen` candidate.
- run.py: `verify --base-only` (base + membership + drift + surface
  currency; the classification contract stays PRO-65's), plus the
  landed a16z-session guards (record protects who:erik classification
  keys).
- Registry: explicit `external` desk patterns as the first classify
  rule (namesakes, Accel-KKR, Meritech, personal entities).

## 7. Environment notes

- **The Internet Archive went down before the wayback pull started**
  (~16:40 CET, web.archive.org unreachable while archive.org answers;
  still down at run close). Per the playbook's outage protocol the run
  proceeded on live surfaces with the provisional roster; wayback, the
  CDX-roster expansion (historical partners: Breyer, Gouw, Wagner,
  Fenton, Lixandru...), the Form D re-sweep on that expanded roster,
  and the rebuild land post-recovery, before ingest. A recovery watcher
  ran all session.
- **A parallel session ran PRO-68** (firm profile) in the same
  directory; ownership split declared by message (their four files
  never ride this session's pathspec-scoped commits). Intel exchanged
  both ways: their fund-filer sweep exposed the Plano/Akron namesake
  vehicles my registry had mis-desked (fixed, zero contamination) and
  supplied Accel 17's CIK; my entities registry, team.json and Sanity
  endpoints went the other way. One mis-addressed first contact
  (merit-capital-3e) was corrected; their stale-git warning to Erik was
  retracted after verification.
- SEC throttled twice (503 bursts); retries absorbed it. One verify
  link-check failure was transient throttling, clean on re-run.
- announcement.md, merit-capital.md, project-scope.md remain deleted-
  uncommitted in the working tree (pre-existing, documented in the a16z
  report too); untouched.

## 8. Limitations and open debts

- **IA remains down at close**; the Common Crawl layer (§5b) carries
  capture evidence 2017–2026, but CC never crawled accel.com deeply
  before 2017, so the 1996–2016 site history (including the whole
  /relationships/ era and the Breyer/Gouw/Wagner/Fenton-era people
  pages) is still unparsed — the remaining recall exposure is deals
  from that window never on any later list and without US filings.
  On recovery (monitor armed): `wayback-pull.py accel` (era map to be
  written from CDX inspection), restore `roster.cdx_patterns`,
  `partner-roster.py`, `formd-query.py`, rebuild, judge the delta.
  wayback_first_link URLs on capture-evidenced rows point at
  web.archive.org replay and resolve once IA serves again (verify
  samples only SEC links, so this is cosmetic until then).
- Archived-CMS rows without external documentation (Behtar, Farcast,
  Names & Faces, Cogsy, Youshd, Zopsmart) are out but listed in §5 for
  Erik's sampling — wayback may corroborate some.
- ACCEL FINANCE CO LLC (CIK 1134308, cofiler-closure) stays us/unknown
  role; produced no companies; identity unresolved.
- Director-pattern members at medium confidence (Autonymy, Mitra
  Biotech legs) carry the A/B-pass flag for PRO-65.
- The registry nit from a16z persists in kind: person CIKs surfaced by
  cofiler closure classify by name pattern before roster resolution;
  all four here (Efrusy, Li, Patterson, Swartz) resolved correctly.
- `run.py status` shows 0/19 batches recorded: the queue is shared
  with PRO-65's classification needs; the membership slice is complete
  (871/871 verdicts), the classification slice is untouched by design.

## 9. Checkpoint 2 (this report)

The membership-verified base is ready for Erik's sampling:
`review.html` (verified rendering on the shared review server — 871
flat rows, sample chip = 63 stratified rows incl. every recall
addition, judged Director-pattern members, auto-seeded oddballs
(Amerigroup, Gentle Dental), Atoms and alias rows), `base.csv` (871
rows, classification columns carrying only flagged deterministic
pre-fills pending PRO-65), `excluded.csv` (76), `golden.json` (the
pre-registered key + 21/21 pass), `base-verification.json` (947
verdicts + 11 recall additions). `verify --base-only` is **clean**.
Corrections in chat are recorded class-wide as `who: "erik"` ledger
verdicts. Ingestion stays gated on Erik's explicit approval
(COLLECTION.md §9); PRO-65 is unblocked on sign-off.

## 10. Artifacts

| File | What |
|---|---|
| `base.json` / `base.csv` | Evidence layer / merged published surface (871 rows) |
| `base-verification.json` | Durable verdict ledger (947 verdicts + 11 recall additions) |
| `identity-merges.json` | 24 merge groups, 3 never-merge pairs |
| `excluded.csv` | 76 not_member rows, preserved |
| `golden.json` | Membership trap set + pre-registered key (stage set: PRO-65) |
| `decisions.md` | 9 rulings (7 confirmed at kickoff incl. Erik's Atoms ruling; #8 Meritech + #9 Erasmic agent-standing, flagged for review) |
| `entities.json` | 181-entity vehicle registry |
| `sources/site/*` | Sanity CMS extraction (companies/team), Atoms browser extraction |
| `sources/edgar/*` | Sweep (689 accessions), companies (65), issuer rounds |
| `sources/wayback/` | Provisional roster only — layer pending IA recovery |
| `scratch/` | Trap key draft, gate pass, dossiers, parametric list, sitemap surfaces |
| `review.html` | Read-only review surface (checkpoint 2) |

# Investor Classification Report — Accel (PRO-68)

Autonomous session 2, run base-less in parallel with PRO-62 per §11, then
re-asserted three times the same day as the base landed, rebuilt, and
refreshed. Output: `investor.json` + `investor.sources.json` (every field
populated with per-field provenance, 8 flags), rendered as the investor
panel in the merged `review.html` (886 rows + profile). Taxonomy gate:
**0 errors, 1 warning** (`Oceania`, the site's own region label; geo is
open vocabulary). Ingest deliberately not run — sign-off was recorded
2026-09-01 with zero corrections, but ingest approval was not given, so
the §9 gate stands until Erik explicitly says ingest.

**Prompt count: 1** (kickoff); 0 checkpoint approvals requested.
Coordination with the PRO-62 session ran session-to-session: the
ownership declaration, namesake trap-set intel out (it corrected the
registry desking of Accel Investments LLC and Accel Investor I/II),
membership-complete / rebuild / rescan pings in, and the focus crosswalk
proposed by this session, landed in `config.json` by PRO-62.

## Evidence chain

- **AUM [$38.03B, $46.83B], both ends sworn**: Accel Management Co.
  L.L.C (CRD 331435, SEC 801-131163, RIA since 2024-09, relying adviser
  Accel Management Co. (India)); full ADV PDF pulled, Item 5.F (annual
  amendment 2026-03-30, FY2025): RAUM $38,031,743,340, all
  discretionary, 83 accounts — and the Schedule D 7.B roster parses to
  the same figure to the dollar (83 funds, US + India families, zero
  London). Top adds the London ERAs' Section 7.B gross assets
  ($8,803,015,413; Accel Partners Management LLP CRD 162784 and Accel
  London Management Ltd CRD 171086 report the identical 25-fund roster,
  deduplicated by private-fund ID; zero ID overlap with the US umbrella),
  per the desk-inside boundary ruling. The issue's expected composition
  (bottom = RAUM, top = press ~$36B) inverted at run time — press sat
  below the sworn floor — so both ends are sworn and the press figure is
  recorded in the flag.
- **Funds: 27, vintage 2015–2026** (`sources/edgar/fund-formds.json`:
  the full "Accel *" EDGAR company-search filer sweep, 59 own vehicles,
  62 Form Ds; Accel-KKR and namesakes excluded per decisions #2 and
  filings-based classification). 19 entries carry filed amounts asserted
  against accessions at build time; 8 carry press sizes because the
  L.P. filed sold $0 — and in every such case the filing's
  total-offering amount equals the press figure exactly. Where press and
  filing disagree the filed amount is published (India V $430M, India VI
  $525M, Leaders 3 $2.255B, Growth IV $1.2B). Accel Core is in as the
  Leaders V LP sidecar at its filed $749.575M close; Accel Circle Fund
  2026 ($95M offering, no public trace) is the internal co-invest class,
  out. The sweep surfaced two vehicles beyond the issue inventory:
  Accel Growth Fund 8 (the $1.35B "global expansion" fund) and Accel
  India 9 ($550M).
- **People: the site's own 35 published investors** (Sanity CMS batch
  query; no role labels on cards — 28 profile metaDescriptions state
  "Partner", the other 7 render the site's flat presentation via the
  build fallback; 30 LinkedIn / 23 X; Kevin Comolli sits in the site's
  Emeritus bucket but is published and kept). Departed cross-check
  against the 217-name roster: 96.
- **investment_range $1M / $20M / $2.3B**: floor from Atoms' "up to
  $1 million" program checks (a stated cap, not a floor — flagged);
  median stable across three populations — $22.0M pre-base (63
  site-confirmed sweep issuers), $20.0M on the rebuild (131 verified
  members), $19,597,993 on the refreshed rescan (155 members, 473 priced
  rounds, 55 entries anchored past pre-investor rounds) — published
  $20M; ceiling from the $2.3B Cursor (Anysphere) Series D co-led with
  Coatue (November 2025), consistent with Leaders V's ~$200M average
  checks and 10–15% concentration capacity.
- **Stage / geo / scope from the firm's own dataset**: initial types
  seed / series-a on 567 tagged portfolio rows, Atoms pre-seed (ruling
  #4), the Growth and Leaders fund families → [Pre-Seed, Seed, Series A,
  Growth, Late Stage], Series B deliberately unclaimed (the firm's
  vocabulary never names it). Geo core [US, Europe, India] per PRO-68 —
  exceeds PRO-7's two-label cap, flagged high and left standing at
  sign-off. Focus recomputed from the site's 48-tag sector vocabulary
  via the config crosswalk (86% tag coverage): 9 values, the identical
  set the curated enumeration produced — positioning and portfolio agree
  at this granularity.
- **Icon** via the PRO-53 flow from the firm's own accel.com/icon.png.

## Post-base reconciliation (three rounds, same day)

1. **Membership-complete signal** (947 verdicts): the notable gate
   refused Flipkart, Spotify and Supercell — ledger members whose rows
   sit `needs_review` because the wayback layer was IA-blocked. The gate
   was re-keyed to ledger member verdicts (PRO-62 confirmed this is the
   correct end-state shape, not a transient).
2. **Common Crawl rebuild** (886 members, 1,015 verdicts): all
   re-asserts green; median $20,000,001 over 131 members.
3. **Refreshed issuer-rounds rescan** (155 member histories): median
   $19,597,993, the rename-merge orphan healed. Published $20M stable
   throughout.

## Script changes

- `build-firm-profile.py`: the landed-base signal for the base-bound
  checks is now **full ledger coverage** (§10 invariant 1), not
  base.json existence — the file can land mid-membership, and
  `needs_review` persists even in completed bases (a16z closed with
  563). The notable assertion keys on **ledger member verdicts**, not
  `status == auto_confirmed`. A sparse or empty focus crosswalk can no
  longer publish an empty focus list.

## Debt, all flagged in the sidecar

- Atoms states a cap ("up to $1M"), not a floor; the true smallest check
  may sit below the published lower limit.
- Geo core carries three labels against PRO-7's two-label cap for the
  leaderboard row; accepted at sign-off, revisit if the row overflows.
- Median tails may ride weak CIK joins (PRO-65's standing weak-CIK audit
  is the cleanup; the median is insensitive), and partner-anchored first
  filings are recency ceilings — UiPath anchors at a $230M round though
  Accel led its 2017 Series A.
- The 2026-vintage vehicles (17, Growth 8, London 9, India 9, Circle,
  Core) postdate the FY2025 ADV and sit in neither AUM figure.
- Ingest (investor row + icon_url) awaits Erik's explicit approval.

# Company Classification Report — Accel (PRO-65)

Autonomous session 3 (same session as PRO-62, continued on the "run the
full classification" instruction). All 886 member rows fully classified:
status, valuation (range/usd/asof/source/citation), entry stage
(+source/citation), hq_city, hq_country, focus, seed_to_a_graduation,
flags, note. `verify` (full, with link checks) exits clean; every hold is
a flagged, inspectable debt, not a silent gap.

**Prompt count: 2** (kickoff; approval message). Erik approved companies
+ investor profile 2026-09-02 with zero sample corrections and explicitly
approved ingest; ingested the same day (investor row + 886 companies,
public.companies holds 886 accel rows) and merged to main.

## 1. Shape of the result

- valuation_range: 790 below_1b / 74 1b_plus / 17 10b_plus / 5 100b_plus.
- entry_stage: 305 Seed / 39 Pre-Seed / 399 Series A / 143 Growth — the
  A-weight is the 1996-2014 era when Accel was an A-first firm; Growth is
  dominated by the 2015+ late entries (see §3).
- status: 567 private / 218 acquired / 37 public / 29 defunct / 35 unknown.
- 658 rows carry a cited entry stage (web_verified); 111 rows carry a
  valuation citation; every $1B+ row has a cited value and a cited or
  flagged entry stage; every public $1B+ row has a cited market cap.
- focus: twelve-value taxonomy on 737 rows; 149 null-focus tail (old or
  thin rows, each still carrying stage/country conventions).
- C2A cohort: 91 rows, 72 graduated (79.1%) — but see the §4 caveat.

## 2. Method

1. Generator + judgment tables (`scratch/pro65_generate.py`,
   `scratch/pro65_judgment.py`): layers + CMS + ~450 hand-authored stage
   and status judgments merged into ~20 `run.py record` batches under the
   source gate. Stage calibration gate: 31/33 first run, both misses
   diagnosed as precedence gaps (rules added: label-follows-record on
   at-scale entries; CMS-label discount class), re-run **33/33**. The
   Form-D band was demoted to a ceiling after scoring 5/13 on the gate.
2. Web pass (5 agents, 107 targets): every suspected-$1B+ value pinned
   with source + asof + citation or left flagged.
3. Float sweep over the public slice, which caught the name-collision
   class (§3).
4. Citation pass (2 agents, 63 $1B+ cite_pending rows): 62 resolved with
   citations, 12 entry stages corrected in the process; arista alone
   stays cite_pending (§3).
5. Self-consistency sample (44 rows, 5%) which surfaced the systematic
   city/country incoherence sweep: 27 pairs fixed (ozforex→AU public,
   sky-mavis→Ho Chi Minh City, vinted→Vilnius, synthesia→GB, xero→NZ...)
   plus Bengaluru→Bangalore normalization (32 rows).
6. Close-out audit found 105 non-CMS rows (site-absent members from
   filings/capture/recall layers) with no status at all — the CMS was the
   only status source and covers only site rows. All 105 authored from
   model knowledge (19 public with tickers, 20 acquired with acquirers,
   66 private), 4 missing valuations filled (bumble, comscore, groupon,
   ethos).

## 3. Findings Erik should know about

- **The "Accel led the A" folklore fails on famous rows.** The citation
  pass corrected 12 stages, and the pattern is one-directional: entries
  believed to be Series A were actually B/C growth entries. Personio
  (Northzone led the A; Accel entered at the $75M C, Jan 2020), Netskope
  ($35M C, 2014), PagerDuty ($43.8M C, 2017 — explains the pre-IPO 13G),
  Trade Republic (Creandum led the A; Accel co-led the 2020 B), Sennder
  (B, 2019), BlaBlaCar ($10M B, Jan 2012), Doctolib (€18M B, 2015), G2
  ($30M B, 2017). Two went the other way: Xendit dropped to Seed on
  Accel's own 2015 dating, Mensa Brands to Series A (its launch round).
  New Relic's entry re-read entirely: equity in the 2023 Francisco/TPG
  take-private, not the 2013-14 pre-IPO rounds (which had no Accel).
- **The CMS stage label is class-1 on early rounds but fails on late
  at-scale entries** (the socure class): 17 rows where the CMS said
  "seed"/"Series A" but Accel demonstrably entered at B+ were corrected.
  The gate's label-follows-record rule now encodes this.
- **Name-collision class in the float sweep**: metropcs (T-Mobile,
  $112B), rocket (RKT $14.9B), circle (public CRCL $16.07B, not
  acquired), vinted (wikidata glitch said defunct; private, €8B
  Apr-2026), beam/born/fuse/sense (all wrong-entity floats, quarantined
  with model_disputes_source).
- **arista**: the membership stands on the fund 13G (filing evidence
  suffices under the standing rules), but no source documents any
  pre-IPO Accel round — the company was founder-funded, and the 13G-only
  position reads as a post-IPO fund holding. Stage stays Growth with
  cite_pending + boundary; Erik may want to rule on whether a post-IPO
  public position belongs in the portfolio at all.
- **Anthropic's entry is the Feb 2026 Series G** ($30B at $380B post;
  Accel named in Anthropic's own announcement) — not a 2025 round.
- **defunct is undercounted** (29 rows, 3.3%): quiet shutdowns present
  as private/unknown, acquihires as acquired. The status field answers
  "last known state", not survivorship; don't read a mortality rate off
  it.

## 4. The C2A caveat

The 79.1% graduation rate (91-row cohort, 72 graduated) carries selection
bias and should not be quoted bare: knowledge-true graduations are easier
to author than confirmed non-graduations (nulls hide the undetermined);
only ~20 legs are Form-D-verified, the rest web/model; 76 rows carry
cohort_unverified where a leg is unverified. The honest sentence is:
"of the seed entries where the record could be established, ~79%
graduated — the establishable set skews toward visible successes."

## 5. Debt, all flagged in rows

- cite_pending 3 (arista §3; ethos — $2.7B May-2022 is the last mark;
  groupon — 2010-11 entry uncited).
- stale 43 (valuation >24mo; peak-2021/22 marks the largest class).
- stage_prior 55 / country_prior 124 (era/desk conventions, no direct
  evidence).
- focus null 149; needs_web_value 14 (sub-$1B, not worth a web pass).
- stage_disputes_band 99 (band ceiling disagrees; band scored 5/13, the
  label wins), model_disputes_source 54 (quarantined wrong-entity or
  glitched source figures), cik_weak 4, cohort_unverified 76 (§4).

## 6. Artifacts

- `classification.json` (886 rows, per-key provenance via record who),
  `base.csv` + `review.html` (886 rows, merged with the PRO-68 profile
  panel), `golden.json` (33-row stage set + 21 membership traps,
  `_key_registered`), `scratch/pro65_judgment.py` +
  `scratch/pro65_generate.py` (reproducible judgment).
- Recorded batches: ~20 grind + webpass-A..E + cites-1/2 + fixups +
  collision/pair/city sweeps + status-fill (all through `run.py record`).

Signed off and ingested 2026-09-02 (zero corrections); PRO-62/65/68 all
Done. Post-ingest corrections need fresh ingest approval per §9. Open:
the arista post-IPO-holding ruling, and the IA-recovery wayback pass.

## Cross-investor alignment (2026-09-03)

`run.py verify` now compares every row with the other investors' published
`base.csv` on `status` and `valuation_range` (COLLECTION.md §10 invariant
10; rulings in `data/collection/cross-investor.json`; method in the
Lightspeed report). First run on Accel: 33 disagreements; after resolution
0 (1 accepted). Accel carried the most misses of the four runs: nine
companies another run held at a cited $1B+ primary mark sat at below_1b
here, and eight rows still read "public" for companies acquired or
liquidated years ago. Recorded with `who: cross-investor-align-2026-09-03`;
reproducible from `data/collection/shared/cross-align/2026-09-03.py`.

**Rows changed (23):**

| slug | before | after | evidence |
|---|---|---|---|
| captivateiq, ironclad, falconx, mux | below_1b | 1b_plus, `stale` | last primaries: $1.25B (Jan 2022), $3.2B (Jan 2022), $8B (Jun 2022), $1B+ floor (Apr 2021) |
| decagon, periodic-labs, skydio, snorkel-ai | below_1b | 1b_plus | $4.5B (Jan 2026), $1.3B (Sep 2025), $4.4B (Apr 2026), $1.3B (May 2025) |
| physical-intelligence | below_1b | 1b_plus $5.6B | Series B Nov 2025; membership rests on Accel's own listing (no press names Accel in a round); `cite_pending` on the stage |
| ethos | private / 1b_plus $2.7B (2022) | public / 1b_plus $2.42B | IPO 2026-01-28 (Nasdaq: LIFE); cap 2026-09-03 |
| netskope, groupon | public $6.18B / $1.5B (Aug) | public $5.91B / $769M | same-day caps shared with Lightspeed and a16z; Groupon drops below the band |
| lightspeed | public, no value | public / 1b_plus $1.35B | Lightspeed Commerce (LSPD), cap 2026-09-03 |
| blameless, split, graphite | private | acquired | FireHydrant (2024-08-21), Harness (2024-06-11), Cursor (agreement 2025-12-19; closing evidenced by domain routing) |
| despegar, brightcove-inc, rovio, remedy-corporation, uunet-technologies | public | acquired | Prosus (2025-05-15), Bending Spoons (2025-02-04), Sega (2023-08-17), Peregrine (2001), MFS (1996) |
| bird-scooters | public | defunct | Bird Global liquidated in Chapter 11, equity wiped |
| datagravity-inc | unknown | acquired | assets to HyTrust 2017 |

**Counts.** cumulative $1B+ 96 → **105**, $10B+ 22 → **22**, $100B+ 5 →
**5**; valuation_range 790 / 74 / 17 / 5 → **781 / 83 / 17 / 5**; status
567 / 218 / 29 / 37 / 35 → **563 private / 227 acquired / 30 defunct / 32
public / 34 unknown** (`ipo_companies` 37 → 32). `verify` clean. The live
database still holds the 2026-09-02 values; re-ingest is pending Erik's
approval.
