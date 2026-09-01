# Company Base Report — Accel (PRO-62)

Single-session autonomous run, 2026-08-31. Scope: the membership-verified
Company Base (PRO-62, "autonomous session 1, part 1"). Classification
columns (`status`, `valuation_range`, `entry_stage`, `hq_*`, `focus`, C2A)
are PRO-65, which continues on this base after Erik's sample sign-off; the
review surface already shows the deterministic pre-fills (SEC float,
Wikidata, unicorn list) with their flags, judged by no one yet.

**Prompt count: 1** — the kickoff ("execute the accel base collection as
per PRO 62; work diligently in full autonomy", with the pre-start ruling
that resolved the Atoms question). Checkpoint approvals requested: 0
(both checkpoints posted-and-continued). **Erik rulings recorded so
far: 1** (decisions #4, Atoms in where Accel money deployed — given at
kickoff). The count is final only after sample sign-off. A parallel
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
