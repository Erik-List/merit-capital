# Benchmark — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Benchmark (slug
`benchmark`, display name always **Benchmark** — the firm dropped "Capital"
from its own branding; its legal adviser name is Benchmark Capital Holdings
Co. LLC). The judge cites these rulings per line. Written under the
derivation protocol of COLLECTION.md §1: **derivations** (a standing test
applied to verified facts — vetoable by Erik, no confirmation needed),
**deltas** (Erik's to confirm) and **run-time standing rulings** (dated,
flagged for review). Phase 0 was researched and verified at kickoff
2026-09-06 against IAPD, the Form ADV PDF, EDGAR and the archived site;
every fact below was checked in this run, not carried from the issue.

**The structural fact of this run.** Benchmark is a 1995-vintage Silicon
Valley equal partnership that leads first institutional rounds, and it is
the first investor in this project whose own site is **archival only**: the
live benchmark.com is a single page carrying two office addresses and a
Twitter link (`/portfolio`, `/companies/`, `/sitemap.xml`, `/index.xml` and
`jobs.benchmark.com` all 404 or do not resolve, verified 2026-09-06). The
firm published a full portfolio list for sixteen years and none for the
thirteen since. So the base has two halves with different evidence models:

- **1997–2013, list-covered.** Four listing eras on benchmark.com, all
  parsed (`config.json` `wayback.eras`): the alphabetical `/about/p-alpha
  .html` (1999–2001), `/Portfolio/Portfolio_By_Location.html` with its
  sector cuts (2001–2005), `/portfolio/worldwide.shtml` with per-desk pages
  (2005–2009), and the WordPress `/companies/` logo cards with a
  `/company/<slug>/` page each (2010–2013).
- **2013–2026, no list at all.** The Thrive shape (COLLECTION.md §5, "when
  the investor publishes no list at all") without the job board: the
  roster-name Form D sweep is the primary structural layer, the fund
  vehicles' own 13D/G and Section 16 filings are filing-grade membership
  evidence, and the exit-side EDGAR full-text sweep, the Wikipedia insource
  sweep, press sweeps and the recall probe's parametric enumeration carry
  the rest. Expect the recall probe to be load-bearing over this half and
  say so in the report rather than reading a thin decade as a defect.

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1 — The firm (T1, same adviser).** Benchmark = the adviser filing as
  **BENCHMARK CAPITAL HOLDINGS** (full legal name **Benchmark Capital
  Holdings Co. LLC**; also "Benchmark Capital"), **CRD 160352**, SEC
  **exempt reporting adviser** 802-75842, ERA since **2012-03-30** (a
  California state ERA filing since 2024-01-19), annual amendment filed
  **2026-03-24**. Principal office **2965 Woodside Road, Woodside, CA
  94062**; website benchmark.com (ADV Section 1.I). It is **not** an SEC- or
  state-registered investment adviser, so there is no Item 5.F RAUM and the
  AUM anchor is the Section 7.B private-fund gross asset composite
  (COLLECTION.md §11): **34 private funds, $7,582,538,663** on the
  2026-03-24 filing. Founded 1995 (Bob Kagle, Bruce Dunlevie, Andy
  Rachleff, Kevin Harvey, Val Vaden). Filing addresses across the record:
  2480 Sand Hill Road, Menlo Park (1997–2019) → 2965 Woodside Road,
  Woodside (2019–), with 140 New Montgomery Street, San Francisco as the
  city office the live site names.

  **IN under T1**, one adviser, one team: the flagship family **Benchmark
  Capital Partners L.P. (I), II, IV, V, VI, VII (+ VII (AIV), VII – Annex),
  VIII, IX, X** and the renamed successors **Benchmark Partners 1, 2 and
  T1**; the co-invest **Founders' Fund** family (IV, IV-A, IV-B, IV-X, V,
  V-A, V-B, VI, VI-B, VII, VII-B, VIII, VIII-B, IX, IX-A, IX-B, X, X-A and
  Benchmark Partners Founders' Fund 1, 1-A); the **Benchmark Capital
  Management Co.** GP LLCs (II, IV, V, VI, VII, VIII, IX); the single-deal
  **Benchmark WS SPV, L.P.** (2019); and the thematic sleeve **Benchmark AI
  Infrastructure Fund, L.P. + Fund B + Management Co., L.L.C.** (first
  filed 2026-02-06). Every one of them files from Menlo Park or Woodside.
  There is **no Benchmark Capital Partners III on EDGAR** — Fund III (1998)
  predates the electronic Form D and filed on paper; its existence is
  evidenced by the fund ladder and the Management Co. numbering, and its
  absence from EDGAR is a coverage note, not a boundary question.

  This settles the issue's open question, and the answer changed under
  verification during the run (recorded rather than quietly corrected).
  **Yes — Benchmark now runs both a thematic sleeve and, since June 2026,
  a growth fund**, and both are IN under T1's default (the a16z
  vertical-fund precedent), same adviser, same address, same naming
  convention:

  - **Benchmark AI Infrastructure Fund, L.P. + Fund B** ($127,250,000 and
    $96,690,000 sold, both filed 2026-02-06) are **single-company
    vehicles raised to fund one Cerebras round** — TechCrunch, 2026-02-06:
    the two vehicles "were created specifically to fund the Cerebras
    investment", ~$225M into the $1B round at a $23B valuation. They are
    the firm's own SPVs, not a new strategy, and they carry no rows of
    their own beyond Cerebras.
  - **Benchmark Partners T1, L.P.** ($1,250,000,000, filed 2026-06-30) is
    **the firm's first-ever growth fund** (TechCrunch, 2026-06-03: $2B
    across two funds, "five to six large investments in both existing
    portfolio companies and new startups"), raised alongside **Benchmark
    Partners 2, L.P.** ($750,000,000) for seed/A/B. This is a real break
    with the $425M discipline the firm held for two decades and it is a
    T1 fact, not a T3 one: a growth fund of the same adviser making
    venture rounds is inside the boundary, and its late-stage entries are
    `Growth` by taxonomy like any other. No opportunity, select,
    continuation or crossover vehicle exists in the record.
  - **Benchmark WS SPV, L.P.** ($38,127,000, filed 2019-12-18) is a
    single-deal vehicle of the same kind, a decade earlier.

- **D2 — Benchmark Europe / Balderton Capital: OUT, desk `europe`, partitioned
  (T1).** Benchmark Europe was the firm's London desk from **2000** and
  became **fully independent as Balderton Capital in 2007** (Wikipedia,
  citing VentureBeat 2007-06-07 "Benchmark Europe declares independence; now
  'Balderton Capital'"; the transition is visible on benchmark.com itself,
  which served `/about/contact/balderton.shtml`). Its vehicles — Benchmark
  Europe II L.P. (CIK 1301861), Benchmark Europe III L.P. (1380218),
  Benchmark Europe Founders Fund II-A (1316847), Benchmark Europe Founders'
  Fund III (1408864) — filed from Benchmark's own Menlo Park address while
  the desk was inside the firm, so they are *the firm's own desk of that
  era*, not namesakes; the successor firm is nonetheless a separate firm
  with its own fund family today. **Precedent: IDG-Accel China (historical
  JV, independent successor, OUT), Lightspeed China (independent
  partnership since 2011, OUT), HongShan / Peak XV.** In each the split was
  temporal and the rows went out whole rather than being cut at the split
  date, because the successor firm owns that track record. Balderton is a
  separate investor in this same wave (PRO-106) and would otherwise carry
  the same companies twice.

  Mechanically: the Europe vehicles classify to desk `europe`, which is in
  `desks.partition`, so their rows leave the published base into
  `excluded.csv` with reason `other_desk` — **preserved, not deleted**, so
  Balderton's run inherits them (COLLECTION.md §12, cross-investor
  etiquette). This is the ruling PRO-88 asked to be recorded for Balderton
  to read.

- **D3 — Benchmark Israel: OUT, desk `israel`, partitioned (T1).** The
  Israeli desk opened 2001 and is today **BENCHMARK ISRAEL VC 2007 LTD**,
  **CRD 160374**, its **own** SEC exempt reporting adviser (802-75560, ERA
  since 2012-03-29) at **32 Rothschild Blvd, Tel Aviv** — a separate
  adviser, separate office, separate fund family. That is T1's OUT limb
  read literally, and the Lightspeed India precedent exactly (own ERA, own
  site, own funds, brand shared). Benchmark Israel I and II (CIK 1328065)
  filed from Menlo Park in the desk's in-house years, so they classify as
  the `israel` desk rather than as namesakes, and partition out the same
  way as D2.

- **D4 — The desk split is read off the firm's own attribution, not off a
  company's country (D2, D3 applied).** Two positive rules, in order:
  1. **The post-split list decides.** The 2010–2013 `/companies/` cards
     were published *after* both desks became separate firms and are the
     firm's own claim on its own book. A company on that list is a home-desk
     row whatever desk originally sourced it (MySQL and Wix are on it;
     Betfair, Bebo, Yoox and Lovefilm are not).
  2. **Otherwise the desk page decides.** A company whose only listing
     evidence is a desk page (`/Europe/Europe_Portfolio.html`,
     `/portfolio/worldwide/europe.shtml`, `/Israel/Israel_Portfolio.html`,
     `/portfolio/worldwide/israel.shtml`) carries that desk's lineage. A
     company on `/portfolio/worldwide/sv.shtml`, or on the undifferentiated
     union pages only (`p-alpha`, `Portfolio_By_Location`, `worldwide.shtml`,
     the sector cuts), is `us`.

  The build's own rule (`lineage = edgar_desk if edgar_desk and not listed
  else home_desk`) forces every listed row to the home desk, which is
  precisely the trap PRO-88 flagged, so the desk assignment is written as
  explicit `desk` entries in `identity-merges.json` — derived mechanically
  from the parsed era paths by `scratch/derive-desks.py`, reproducible and
  re-runnable, never row by row. A US or worldwide fund's independent
  evidence (a fund 13D/G, a Form D seat, a US-fund-led round) puts a row
  back in regardless of which desk page also listed it, exactly as
  Lightspeed's "a row on the main list with LSVP participation stays in".

- **D5 — Namesakes (T5).** Resolved by CIK and filing address, never by
  name. **Benchmark Capital Advisors** (CIK 1352859), a 13F filer at 100
  Wall Street, New York whose administrator files from Summit, NJ, is
  **not** this firm and is `external` — note that the Wikipedia article
  calls the venture firm "Benchmark Capital Advisors LLC", which the sworn
  record contradicts (IAPD: Benchmark Capital Holdings Co. LLC). Also
  external: the ~120 `BENCHMARK <year>-<series> MORTGAGE TRUST` CMBS
  shells, Benchmark Electronics (NYSE: BHE), Benchmark Bankshares /
  Bancorp, Benchmark Capital Corp /BD, the Benchmark Plus hedge funds
  (Tacoma, WA), Benchmark Equity Group, Benchmark Real Estate / Western
  Real Estate funds, and every other `BENCHMARK *` filer in
  `desks.classify[0]`. **"Benchmark" is the worst common-word trap this
  project has met** (Cherry's was five documents; a bare EDGAR full-text
  "Benchmark" is tens of thousands, since the word is a common noun in
  every rate, index and compensation disclosure), so every phrase layer is
  entity-qualified and every hit is address-checked.

- **D6 — Scouts, angel books, programs (T2).** Benchmark runs no scout
  program, no accelerator and no seed program; it has no community or
  program listing to rule on. The standing rules apply unchanged if one
  surfaces: partners' personal angel positions are OUT (Cherry precedent),
  a program listing is OUT unless a fund held the position. Positions held
  personally by partners — a recurring pattern at a firm this small, where
  general partners are visible angels — are OUT and their Section 16
  filings locate the person, never the firm (T4).

- **D7 — Venture entry (T3).** Standard: primaries, follow-ons, secondaries
  and tenders IN (tenders as Growth); positions first appearing as 13F
  holdings or post-IPO 13Gs OUT under the standing post-RIA rule. Benchmark
  runs no buyout practice and no public-markets vehicle, so the
  control-position addendum and the crossover exclusion have no candidates
  expected; the `Benchmark WS SPV` (2019) is a single-deal vehicle of the
  firm and its position enters at the round it funded.

- **D8 — Pre-window entries (policy constant).** The base window opens
  **2006**. Benchmark's first eleven years (1995–2005) are a large share of
  the archived listings — the 1999 alphabetical list alone carries the
  eBay/Ariba/Juniper/Handspring era — so a large pre-window cohort is
  expected: those rows are members with `entry_stage` and graduation null
  by rule, and the report states what share of the base they are rather
  than letting a null-heavy stage column read as missing work.

## Deltas (Erik's to confirm)

**None.** Every boundary question this investor raises — the Balderton
split, the Israeli desk, the AI Infrastructure sleeve, the namesake wall —
is a standing test applied to facts verified in this run, so under §1's
inverted protocol they are derivations above and not deltas. Nothing is
blocked on a confirmation.

## Run-time standing rulings (dated, class-wide, flagged for review)

- **R1 — Bill Gurley's personal CIK is a home-desk person entity**
  (2026-09-06). `edgar-entities.py`'s co-filer closure left CIK 1190191
  (GURLEY J WILLIAM) as `external` / `outside-cofiler` while every other
  partner's personal CIK resolved to `us`. He is on the roster and a related
  person on eleven of the firm's own Form Ds; his Section 16 filings are the
  densest person-level channel into the 2013-2026 window the site cannot
  reach. Re-desked to `us` / `person` in `entities.json`. This does not make
  his filings membership evidence — the build still drops any row whose only
  evidence is a Section 16 filing by a person entity — it only lets those rows
  be seen and judged.

- **R2 — Benchmark Israel II L.P. added to the registry by hand** (2026-09-06).
  CIK 1328065 never came back from the EDGAR company-search seeds. Recorded as
  desk `israel` so the registry states the desk truthfully; it is partitioned
  (D3), so nothing it filed enters the published base.

- **R3 — Tenure is a fact about the firm, not about fund-vehicle membership**
  (2026-09-06, class-wide). A partner drops off the related-person list of the
  *next* fund years before leaving, and Benchmark raised no fund at all between
  Fund X (2020-05) and Benchmark Partners 1 (2024-07). Windows taken from the
  Form D vehicles alone were filtering real members out of the base: **Discord**
  — Benchmark's 2016 Series A, Lasky on the board, director filings through
  2023 — was being dropped as "ex-partner is the only evidence" because Lasky's
  last fund Form D is 2016. Windows re-dated from the press record (Wikipedia's
  "prior partners" section and the departure reports it cites): Gurley to 2020
  ("twenty-one years"), Lasky to 2023, Cohler to 2020, Dunlevie and Tavel left
  open, Grimshaw 2021-2024, Lazarte from 2022. Where no departure is recorded
  the window stays open and the judge rules the row rather than a filter
  removing it unseen.

- **R4 — The Form D band is a ceiling on this investor, never a label**
  (2026-09-06, from the gate; `scratch/gate.md`). It scored **7/16** against the
  pre-registered stage key. Eight of the nine misses are the band reading a
  later filing as the entry round. No band-only `entry_stage` publishes on a row
  that is $1B+, post-2013, or evidenced only by the Form D sweep.

- **R5 — `first_seen` from the Form D sweep is a ceiling on entry recency, not
  an entry date** (2026-09-06, class-wide, the gate's central finding). The
  sweep sees the first filing on which a roster name appears as a director, and
  Benchmark leads seeds and Series As that routinely never file, so `first_seen`
  runs two to five years late across the 2013-2026 half of the base (Cerebras:
  `first_seen` 2026, entry 2016). It may not feed `entry_stage`, the C2A cohort
  or any "recent" slice unchallenged. The site's own first listing year, by
  contrast, is a sound ceiling: checked on ten key rows, the entry is never
  later than the first listing and at most one year earlier.

- **R9 — A Section 16 filing by a PERSON is seeded as "a filing by a fund
  vehicle", and the seeder never queues the row** (2026-09-06; a layer defect
  the gate caught, not a judgment). `prepare`'s membership seeding writes the
  basis "SEC ownership filing by a fund vehicle (forms 3,4, CIK …)" without
  checking whether the filer is a fund or a natural person, and a row seeded
  `member` that way carries no `membership` need, so the judge never sees it.
  The trap set caught exactly one: **Wealthfront**, seeded member on Forms 3/4
  whose filer is CIK 1190190, RACHLEFF ANDREW S — the founder's own Section 16
  filings, on the company he founded after leaving. A sweep of the whole base
  for the class found one more: **Activision**, whose 1999-2001 Forms 3/4 were
  filed by LASKY MITCHELL as an Activision executive, eight years before he
  joined Benchmark. Both ruled `not_member`. COLLECTION.md §1 already says a
  person-entity Section 16 filing locates a person and never a firm position,
  and `build-company-base.py` drops such rows — the gap is that the SEEDER does
  not, for a row that survived the build on some other evidence. Proposed for
  the playbook and for `run.py`: seed `member` from an ownership filing only
  when at least one filer CIK is a fund vehicle, and queue the row otherwise.

- **R8 — Twenty rows of the Form D sweep are other firms' seats, ruled as five
  clusters** (2026-09-06, class-wide). Benchmark hired four partners out of other
  firms between 2021 and 2026, so the prior-firm class is unusually large for a
  base this size. Ruled cluster-first (§3), never row by row:
  **Puttagunta's NEA book** (Canopy Tax, Folloze, Heap, Logik Systems,
  Placester, Reltio, ScoutRFP, SiteTraker — every seat filed before his first
  Benchmark fund Form D of 2018-10-01); **Altman's Alt Capital book** (Antares
  Nuclear, Verifiable, Copilot Labs — the last one quarter before his first
  Benchmark filing of 2026-06-30) **and his own company** (Degree, Inc. = Lattice);
  **Grimshaw's Thrive seats** (Benchling, filed 2016, five years before he joined
  — and a member of both Thrive's and a16z's landed bases, which corroborates the
  attribution directly) **and his next firm's** (Doji Labs, 2025); **Randle's
  pre-Benchmark Huntress seat** (2024q2); **Beirne's own post-Benchmark venture**
  (Fantex, founded 2012 by a general partner whose tenure ended in 2001 — Dunlevie
  co-files in tenure, but Fantex filed registration statements and the full-text
  sweep on the firm's own fund phrases returns zero Fantex documents, so there is
  no affirmative corroboration and the verdict is not_member, not uncertain);
  **Vaden's post-tenure InXpo seats**; and **Harvey's three personal LLCs**
  (Camrose, Cardston and Fronterra Investors, one $500-600K offering each on the
  same day in 2013q3, fund-shaped names with no operating company).

  The counter-example is deliberate and is in the trap set: **Minerva Project is a
  member on the SAME partner's seat** — Kevin Harvey, first Form D 2012q2, in
  tenure, Benchmark led the $25M seed. A cluster is resolved once per person and
  then decided per row.

- **R7 — The asterisk on the firm's own list is a disclaimer, and it takes 21
  rows out** (2026-09-06, class-wide, high confidence). Every listing era from
  1999 to 2009 carries the legend **"* Investments made by Benchmark Capital
  general partner(s) prior to the formation of Benchmark Capital"** at the foot
  of the page. Twenty-one rows carry the marker — AOL, Approach Software,
  Avant!, C·ATS Software, Chromatic Research, Collabra Software, eShop,
  Geoworks, Ipsilon Networks, Kalpana, Legato Systems, Palm Computing, Pure
  Atria Software, Rambus, S3, SDRC, Synopsys, Viasoft, Vitalink Communications,
  Walker Interactive Systems, XA Systems — and they are the founders' pre-1995
  deals from Merrill Pickard, TVI and their other prior seats. No Benchmark fund
  held any of them (the firm was formed in 1995), so **T2 rules them out**, and
  they are `not_member` as one class rather than row by row.

  This is a **refinement of the evidence-sufficiency rule** and is proposed for
  the playbook: COLLECTION.md §1 says "a listing on the investor's own site (any
  era) … suffices alone" for membership. It does not, when the site's own legend
  disclaims the row. Read the page's footnotes before trusting its rows —
  without this, Synopsys, Rambus, AOL, Palm Computing and Legato Systems would
  have published inside Benchmark's track record, 6% of the base and heavily
  weighted to famous names.

- **R6 — A continuing board seat first taken at a prior firm stays the prior
  firm's** (2026-09-06, class-wide; proposed for the playbook, §1 seat dating).
  COLLECTION.md dates a seat against the person's firm **at filing time**, which
  is right for a seat taken at the new firm and wrong for one carried across a
  move: the later filing is an amendment to a relationship that began elsewhere.
  The test is the seat's FIRST year. Benchmark forces the refinement because it
  hired four partners out of other firms between 2021 and 2026 — Miles
  Grimshaw's Lattice (Degree, Inc.) seat, taken in 2019 at Thrive, files inside
  his Benchmark window and would otherwise read as a Benchmark position.
  Mechanically: `scratch/enrich-queue.py` puts one line per (partner, quarter)
  on every queued row with that partner's roster window and an
  `in_tenure | pre_tenure | post_tenure | boundary` flag, because
  `formd_span` is year-granular and thirteen of Benchmark's rows turn on a
  boundary inside a year.
