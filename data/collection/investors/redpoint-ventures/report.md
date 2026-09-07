# Redpoint Ventures — collection run report (PRO-90)

**Run:** one session, 2026-09-06, under the merged shape of `../../COLLECTION.md`.
**Result:** `verify` clean in plain mode. **412 members**, 147 rows preserved in
`excluded.csv`, firm profile through the taxonomy gate, review surface rendered
and checked.
**Prompt count: 1** (kickoff). The ingest approval will be prompt 2 — the target.
**Usage line:** kickoff percentages were not supplied to this session; the
weekly and Fable percentages are to be filled at the ingest decision, against
412 base rows. Web-search spend was ~22 calls of the 200-call budget: 6 in
Phase 0 and the golden key, 8 on the public market caps, 8 on the momentum
slice — the rest of the run's evidence came from the firm's own surfaces.

---

## 1. The method delta — a firm whose own site separates its book from its founders'

Redpoint was founded in 1999 by six partners who left two firms at once: Brad
Jones, Jeff Brody and Tim Haley from **Brentwood Venture Capital**, and Geoff
Yang, Tom Dyal and John Walecka from **Institutional Venture Partners**. The
firm's first site rendered the portfolio as **two labelled tables**:

| section | what it is | 2000 capture |
|---|---|---|
| *Current Investments* | the firm's own positions, with description, location and status | 32 rows |
| ***Previous Investments by Redpoint Partners*** | the founding partners' Brentwood and IVP book, displayed as a track record | **57 rows** |

A one-year-old firm cannot have 57 *previous* investments, and Geoff Yang's own
partner page says whose they were: *"Prior to founding Redpoint, Geoff was a
general partner with IVP … He was responsible for **the firm's** investments in
Ask Jeeves, Excite, Foundry Networks, Juniper Networks, MMC Networks, TiVo and
Wellfleet."* The split persists through the 2002–2006 CMS (`oid=152` current,
`oid=157` previous) and the previous list barely moves after 2001 — only two
rows join it in five years, both late-1990s companies.

That is **decisions.md D5**, and it is the largest single judgment of this run:
**60 rows left the base** on it, including 3Com, Ask Jeeves, Avici, Bay
Networks, Documentum, Excite@Home, FileNet, Foundry Networks, Juniper Networks,
Netflix, NextCard, Polycom, SkyStream, Stamps.com, Sybase, TiVo and WebTV. All
are preserved in `excluded.csv` with the citation.

**The rule is evidence-based, not mechanical**: a row is `not_member` only when
it appears *solely* in a previous-by-partners section and carries no Redpoint
fund filing or announcement. Santera, which appears in both sections, stayed a
member on its current-investments listing.

**The trap the two tables set for a generic parser.** A single `listing_regex`
over `/portfolio/default.shtml` matches the *previous* rows and misses the
current ones: the firm's own book is rendered as logo images with descriptions,
the partners' book as plain text links. The first configuration of this run
captured exactly the wrong 57 companies. Both earliest eras are therefore parsed
by `scratch/build-early-eras.py` straight into `sources/wayback/parsed/`, with
the section recorded in the row's `path`.

## 2. Evidence layers — five site eras and one logo-only decade

| era | surface | what it publishes | measured |
|---|---|---|---|
| 2000–2002 | `/portfolio/default.shtml` | two sections; logo `alt` + description, location, status | 32 current / 57 previous |
| 2002–2006 | `index.htm?action=view&oid=152` / `oid=157` | **no names at all** — logos only, plus company URL, description, location, status, acquirer, ticker | 37 → 62 current |
| 2007–2012 | `/portfolio/current-investments/` | logo `alt` names + the same four columns | 69 → 96 |
| 2015–2020 | `/companies/` (WordPress) | `iso-company-name` + the firm's own sector and stage taxonomies, an active_state, **and the deal partner's author slug** | 139 → 173 |
| 2021–2026 | `/companies/` (Gatsby) + the live Sanity CMS | `data-filter-name/-sectors/-stage`; the CMS adds `investmentDate`, `location`, `founders` and an excerpt | 129 → 168; 288 live docs |

**The logo-only decade is the layer this run had to invent.** For five years the
firm rendered every company as an image with no `alt` text. The rows are not
lost, because the era still links each logo to the **company's own domain**, so
`build-early-eras.py` names a row from its own URL host and then corrects it by
joining across eras on that host to whichever surface renders a name. Of 91
rows recovered from 2000–2006, 54 got the firm's own rendering that way and 37
kept a derived name for the judge to correct. On an acquired row the logo link
points at the ACQUIRER, so the parser records that separately and never lets it
name the company.

**The site is also a judge instrument.** Every live company card carries a
one-line entry claim in prose — *"We first partnered for their Series C in
2012"* — and the 2015–2020 cards carry the deal partner's slug, the same slug as
`/author/<slug>`. Those two facts did most of the work of this run's
`entry_stage` column and of its Form D cluster resolution.

**Two recall layers, one negative result.** The Wikipedia insource sweep found
**7 genuine misses** (Deliv, Lever, Path, Secret, Summon, tbh, and Couchbase,
which was then re-judged as a duplicate of Membase under T5). The exit-side
EDGAR full-text sweep returned 283 registrants and **added nothing**: every
operating company in it was already in the base, and the rest were LP-side funds
of funds, acquirers, SPACs and the firm's own vehicles. That negative result is
recorded rather than hidden — for a firm whose own site has listed its portfolio
continuously since 2000, the site layers carry recall and the full-text sweep is
corroboration.

**The site union has no gap:** of 447 companies across all five surfaces, 447
reached the base (the five apparent misses are name variants of rows already in
it).

## 3. The calibration gate

Both sets were assembled and committed before any verdict wrote (`golden.json`,
commit 699c477).

**Membership traps, 20 rows: passed, zero false members at high confidence.**
The dominant trap class here is the homonym: the roster-name Form D sweep
returned **857 accessions across 243 issuers for "Christopher Moore" alone**,
105 for "Jeffrey Miller", 83 for "Greg/Gregory Martin" and 59 for "Michael
Cohen" — four of the commonest names in American business, all real Redpoint
partners. 71 rows entered the base on a name match alone and **63 of them were
ruled out**, each with its cluster reasoning.

**Stage golden set, 34 rows: the CMS field scored 28/28, the excerpt 28/28 —
after four documented key corrections, and the corrections are the finding.**
Against the pre-registered key the card's `stage` field scored 25/28 and the
excerpt 24/28. Every miss was the KEY's, and all four share one cause: the key
row had been anchored on **the earliest item in the firm's own announcement
archive**, and that archive is systematically LATE. LifeSize was listed on the
firm's own site in 2003 and first announced at its 2004 Series B; Auditude was
listed in 2009 and first announced at its 2011 Series B. This is the defect
COLLECTION.md §6 names for the first *filed* round, reproduced for the first
*announced* round.

**Layer verdicts, decided before the grind:**

| layer | score | class |
|---|---|---|
| CMS `stage` reference field | 28/28 | **1** |
| CMS excerpt sentence ("We first partnered for their X in YYYY") | 28/28 | **1, preferred** — it also carries the year and distinguishes first from later |
| the firm's announcement archive (318 dated funding titles) | ceiling only | **2** — cites and dates a round, never labels an entry |
| Form D band | too few key rows to score (9 of 34) | ceiling, unchanged |
| the 2015–2020 card stage class (`seed`/`early`/`growth`) | unscored | corroboration only; 'early' spans Seed, A and B |

Unlike Accel's "socure" class, Redpoint's card does not describe the company's
maturity: it states the DEAL. That is why it scores as it does, and 190 of 417
rows carry a `web_verified` entry stage citing the firm's own company page.

## 4. What the grind found

**581 rows judged in 13 batches, one pass each.** 450 members, 139 not_member
before the rebuild; 417 members after merges and the recall delta.

- **63 homonym and seat-dating rulings.** Alex Bard on Campaign Monitor's Form
  Ds (he was its CEO before joining Redpoint); Erica Brescia on BitRock's (she
  co-founded it, as Bitnami); Andrew Rubin as Illumio's *Executive Officer*
  (Illumio's founder-CEO is a different Andrew Rubin); Pueo Keffer on
  DigitalOcean's 2015 filing (by then he was at Access Industries, which led
  those rounds); "David Yuan" on ExactTarget's — a company backed by Insight and
  Battery that no Redpoint surface has ever listed.
- **5 unannounced deals confirmed** on the adjudicated director-of-record
  pattern, four of them resolving to companies already in the base under their
  brand names: Commerce Fabric = fabric, NoHo Dental = Tend (both Medha Agarwal
  and Annie Kadavy named as directors), Xatabase = Xata, TellAPal = Extole,
  Schooner Information Technology = Schooner. Two genuinely new: **Datagrid
  Systems** and **MayBern Solutions**, both medium confidence and flagged.
- **20 wrong deterministic pre-fills disputed.** The Wikidata and float layers
  returned `status=defunct` for Alchemy (a Czech namesake), `hq_country='Soviet
  Union'` for Tundra, `'United States and  Israel[65]'` for Cyera,
  `status=acquired` for Stripe, Nubank and DraftKings, and a $223M public
  identity for Tactile (that is Tactile Systems Technology, NASDAQ: TCMD).
  **None of those keys was in the row's `need` list**, so the queue never asked
  the judge about them; they were caught only because the evidence view showed
  the pre-fill next to the row's own evidence.
- **45 identity merges**, the largest of any run so far, from three causes: the
  firm renamed the company (Riffsy→Tenor, Heartex→HumanSignal, r2c→Semgrep,
  Idetic→MobiTV, Azureus→Vuze, SocialVibe→True[x]); the logo-only era named a
  row from a domain stem or a logo filename (`longsys`, `procket`, `reflect`,
  `vivace`, `getthere1`); or the Form D sweep found the legal entity behind a
  brand.

## 5. The adversarial A/B pass and the standing duties

**Two corrections that would have published false numbers:**

1. **Pure Storage now trades as EVERPURE, INC. (NYSE: P).** The quote page
   reached by the old PSTG ticker returns Everpure, whose business description
   is Pure Storage's. Market cap $33.16B at the close on 2026-09-04. Standing
   duty 4 exists for exactly this and it fired.
2. **Root, Inc. is no longer a unicorn.** $876.76M at the same close, down 35.5%
   year to date. The deterministic layer carried $1.6B from a stale SEC public
   float; the corrected reading agrees with the Sequoia row's $0.81B.

Every public $1B+ row now carries a cited market cap with an as-of date;
Fortinet moved 10b_plus → 100b_plus ($114.67B), Snowflake to $118.84B, hims down
10b_plus → 1b_plus ($6.47B).

**Momentum slice: 52 rows, 40 newly checked**, each recorded with its date so
the absence claim carries one. Hex at ~$400M, Trunk Tools at ~$326M, Railway,
Databento and Levelpath all undisclosed and unreported at $1B. Nothing crossed.

**Duty 6 (loose unicorn re-intersection):** 5 hits, all correctly handled —
three former unicorns that are acquired rows (HomeAway, Kabam, Duo Security),
one defunct (Essential), and Clara, which was the name collision already
disputed.

**Duty 7 (5% blind re-classification, 21 rows): zero disagreements** — but only
when scored against the EXPORTED surface. Scored against `classification.json`
alone it looked like 11 disagreements, because that file holds only the keys the
judge answered and the deterministic pre-fills live in the base and queue
layers. The finding is about the audit, not the data, and it is proposed as a
playbook write-back.

## 6. Cross-investor alignment (invariant 10)

152 shared rows, 140 agree, **12 accepted, 0 disagree**. One row was stale on
THIS side and was aligned: ClickHouse, from the 2021 Series B mark of $2B to the
$15B the Lightspeed and Thrive rows carry. The other eleven are pairs where this
run's reading is the better-evidenced one and the sibling is stale — Astro
acquired by Slack in 2018 (Accel and Lightspeed both read private), Tact.ai
acquired by Aktana (Accel private), Tidemark/Proferi acquired (a16z unknown),
AMEC listed on the STAR Market (Lightspeed unknown), and five newly-priced $1B+
rows the siblings carry as below_1b. **Those eleven are listed in
`cross-rulings.json` for the wave alignment**; this session owns only its own
directory and did not edit them. Three further pairs are ruled `distinct` (two
Cascades, two Revels, two Simulas).

## 7. Open rulings for Erik

1. **The D5 class — the single ruling that matters most.** 60 rows left the base
   because they appear only in the firm's own *"Previous Investments by Redpoint
   Partners"* table. Three of them — **Netflix, TiVo and LoopNet** — are on the
   firm's LIVE site today, and Netflix's own card dates the relationship to
   "their Series B in 1998", a year before Redpoint existed. Four more —
   **Ask.com (Ask Jeeves), Concur, Juniper Networks and MMC Networks** — are
   the same shape but were KEPT as members because their live cards claim them
   and they were not in the pre-registered trap set; they are flagged
   `identity_uncertain`. If you rule the modern site's claim decisive, those 60
   rows come back; if you rule the firm's own contemporaneous classification
   decisive, the four kept rows should go out with them. This run took the
   second reading and applied it conservatively.
2. **Arista Networks (T3).** The card says only "We partnered in 2014" and names
   no round; Arista IPO'd in June 2014. Either a pre-IPO secondary (in, Growth)
   or a public-market purchase (out). No Redpoint fund filed a 13D/G or Form 3
   on the issuer, and Redpoint Management LLC files 13F-HR from 2022. **This is
   the same question as Accel's open `arista` ruling** and should be settled
   once for both.
3. **Internet Brands (T3).** Same shape: "We first partnered in 2008" in a
   company that had been NASDAQ-listed since 2007.
4. **Redpoint eventures, the Brazil JV (D4).** Nubank, Viajanet and Xango are
   kept as members on the firm's own listing plus a dated entry claim, but the
   JV's funds are not under Redpoint Management LLC and `eVentures Growth, L.P.`
   (CIK 1611943) is e.ventures' own vehicle with no Redpoint person on it.
   9flats and Shoes4You were ruled out on the same reasoning. **Xango raises a
   second question**: it describes itself as a "Consumer Internet Platform
   *investment company*", which is a T5 operating-company question as well.
5. **Project Rover, Inc.** — the one director-of-record row this run could not
   resolve. Geoff Yang named Director on a 2009 Form D by an issuer whose name
   is a codename that resolves to no operating company. Ruled `not_member` under
   your a16z narrowing (identity never resolved, no announcement).
6. **Cyngn and Cyanogen.** CYNGN Inc (NASDAQ: CYN) is the corporate successor of
   Cyanogen Inc, and both are rows. They are guarded against merging and the
   relationship is raised rather than decided.
7. **Redpoint China (D2), for confirmation.** The 29 Chinese rows are all
   pre-2015 home-desk positions the firm still lists; **ACE Redpoint Ventures
   China I–III and ACE Redpoint Opportunity China I–II** were found on EDGAR and
   partitioned `external` by the entity registry, and the 2016 $180M China fund
   is deliberately absent from the profile's fund table.

## 8. Debt behind a clean `verify`

| flag | rows | what it means |
|---|---|---|
| `stage_prior` | 111 | mostly 2000–2006 rows whose entry round no surface names |
| `duplicate_suspected` | 66 | the merge groups, all resolved in `identity-merges.json` |
| `identity_uncertain` | 45 | logo-era derived names and the D5 kept rows |
| `stage_uncited` | 42 | a stage the record supports but no URL names |
| `needs_web_value` | 40 | private rows re-checked in the momentum slice |
| `cohort_unverified` | 30 | seed cohorts whose graduating round is press-documented, not filed |
| `model_disputes_source` | 26 | the deterministic collisions, all corrected |
| `stale` | 19 | private marks older than 24 months |
| `cite_pending` | 11 | Anthropic, OpenAI, Apus, Calix — $1B+ rows whose entry round no source names |

**Structural caveats the numbers carry.** 86 of 417 rows entered before the 2006
window opens, so their `entry_stage` is a convention and their C2A is null.
`defunct` is undercounted by construction (65 rows, 16%) — quiet shutdowns
present as `private` or `unknown`, and 20 rows sit at `unknown` because a
Chinese or dot-com-era company simply went dark. `hq_city` is 241/417: the
2000–2012 table gave a location for its own rows and the modern CMS gives one
for its own, but the eras between them gave neither.

## 9. Proposed playbook write-backs

1. **A replay helper must check curl's return code, not just its body.** Both
   `scripts/wayback-pull.py` and this run's `scratch/build-early-eras.py`
   treated "the probe returned nothing" and "the probe never connected" as one
   outcome, and printed both as `0 entries` / `no capture` — which reads as *the
   archive holds nothing for this year* when it actually means *unknown*. The
   first pull landed 4 of 14 era-years that way, and the early-era builder lost
   3 year-slots.
   **Correction (2026-09-06).** This entry first blamed the scheme: it claimed
   the archive was refusing port 80 while https answered, on my n=3 vs n=3
   sample. That is wrong. The YC session measured it properly — 9 paced
   alternating requests, http 7/9 and https 6/9, and the failures were rc=28
   timeouts on BOTH schemes, not rc=7 refusals. The archive was flaky for
   everyone that hour; the scheme swap was cosmetic and the run-local https
   copies only "fixed" it by retrying. The defect was always the swallowed
   return code. Credit for the measurement is the YC run's.
   The fix (landed upstream by YC as `12402a7`, mirrored here in
   `scratch/build-early-eras.py`): retry a transport failure 3x with backoff,
   and when the probes still never connect, name those years in a loud line as
   UNKNOWN rather than empty. §5 should state the rule directly — **an absence
   may only be read off a year whose probe actually answered.**
   *This was not academic.* Re-running the repaired early-era builder recovered
   3 of the 4 slots this run had recorded as "no capture": `index-oid152 2006`
   (65 companies, a whole year of additions the base never saw), `index-oid157`
   2003 and 2005. Re-running the fixed `scripts/wayback-pull.py` then recovered
   two whole era-years that had been printed as `0 entries` — `/companies/`
   **2021 (128 entries) and 2024 (178)** — neither of which existed in
   `sources/wayback/parsed/` at close. The already-exported and already-ingested
   base moved as a result; see the second addendum.
2. **A firm's own portfolio page can carry two books.** §5 should say that a
   listing surface is read for its SECTION HEADINGS before its rows: a firm that
   spun out of another displays its founders' prior track record beside its own,
   and a single regex takes the wrong one. Generalises beyond Redpoint to any
   spin-out (Versant, Balderton, Foothill).
3. **A logo-only era is named from the company's own domain, not left
   unparsed.** §5 currently allows a logo era to "stay deliberately unparsed
   when snapshots of another list bracket those years". Redpoint's 2002–2006
   decade shows the better move: the logo's own anchor gives the company URL,
   the host names the row, and joining on that host across eras recovers the
   firm's own rendering for most of them. On an acquired row the anchor points
   at the acquirer and must be recorded as such.
4. **An ADV can name no funds at all.** Redpoint identifies every one of its 35
   private funds in Schedule D Section 7.B by a colour or fruit CODE (FUND
   MAGENTA, BLUSH SIDE FUND) under the rule 204-2(d) anonymity option the form
   itself offers. §11's AUM recipe still works — the gross asset values sum to
   $7,964,567,728 — but the sworn roster cannot be mapped onto the named funds,
   and the fund table must come from the vehicles' own Form D filings instead.
5. **"Pre-fill is not judgment" needs a second half.** §8 already says a
   deterministic pre-fill keeps the judge away from its row. This run found that
   the pre-fill can also be WRONG on a key the queue never asks about — 20
   times, from Wikidata and float name collisions. The evidence view should show
   every pre-filled key next to the row's own evidence, and a judge that
   disputes one should be able to say so without the key being in `need`.
6. **Duty 7 must be scored against the exported surface.** Scoring the blind
   re-classification against `classification.json` reports false disagreements
   for every deterministically resolved key.
7. **One rebuild is one rebuild plus a sweep.** §8's own note that excluded
   canonicals resurface their duplicates means the run needs a second, purely
   mechanical rebuild after those slugs get their verdicts. Seven rows did here.
8. **The firm's own announcement archive is a class-2 layer, not class 1.** Add
   it to §6's evidence order explicitly: it cites and dates a round but it is
   systematically late as an ENTRY signal, for the same reason the first filed
   Form D is.

## 10. Ingest — done 2026-09-06 with Erik's approval

In the order COLLECTION.md §9 requires for a first-time investor:

1. **Icon uploaded.** `investors/redpoint-ventures-b569a5e1a9.png`, normalized
   from the site's own 260x260 favicon; provenance in `investor.sources.json`.
2. **`ingest-investor.ts`** — 1 row upserted.
3. **`ingest-companies.ts`** — **412 of 412** rows upserted; the database holds
   412 for the slug and **zero orphans**.

Two payload corrections were needed and are recorded in the sidecar: the row
carried `investor_type: "VC"`, which no investor uses and which made the ingest
silently find nothing (the loader filters on Institutional/Individual); and
`investment_geo.other` carried `"China"`, which is not in `data/taxonomy/geo.json`
— the ingest would have added it to the geography vocabulary, which §11 forbids.
It is published as **Asia**, with the China reading kept in the basis.

**Accel re-ingested** on Erik's ruling: 885 of 885 rows upserted, and the
orphaned `Arista` row (public / 100b_plus / **$246,810,000,000**) was deleted by
id after the upsert. `ingest-companies.ts` upserts and never prunes, so a row
removed from a base survives in the database until it is deleted explicitly —
worth knowing for every future re-ingest that shrinks a base. Accel's investor
row also re-ingested with a pre-existing warning this pass did not introduce:
`investment_geo.other` carries `"Oceania"`, which is likewise not in the geo
taxonomy.

**The wave alignment.** Twelve cross-investor pairs where a sibling is the stale
side are listed in `cross-rulings.json` and belong to the wave-level pass, not
to this session — plus the 38 YC artifact entries, which must be **deleted**
there once YC classifies.

---

## Addendum, 2026-09-06 — Erik's rulings applied; base 417 → 412

Two rulings arrived after the run closed and are recorded in `decisions.md`
Part 2 as confirmed deltas.

**1. T3 — no round named + partnered after IPO is not a member.** Standing from
this run on, binding every investor. It reaches six rows here:
`arista-networks` (card: "We partnered in 2014"; NYSE 2014-06-06),
`internet-brands` ("We first partnered in 2008"; NASDAQ 2007-11), and `juniper`
and `concur` — plus `juniper-networks` and `concur-technologies`, the same two
companies under their full names, which resurfaced once their canonicals were
excluded. Juniper IPO'd four months before Redpoint Ventures I closed and
Concur a year before the firm existed.

Two rows the ruling does **not** reach and which stay members: `ask-com`, whose
card does name a stage ("their Early-stage investment in 1999"), and
`mmc-networks`, whose card carries no partnering claim at all so the second
condition cannot be established. Both remain flagged for the still-open D5
question.

**Applied to Accel in the same pass** on Erik's instruction: `accel:arista` and
`accel:arista-ipo` are `not_member`, which removes a 100b_plus / $246.8B row
from that published track record and closes the open ruling the Accel run left
(`accel/decisions.md`). Accel was re-exported, its profile rebuilt and its
review surface regenerated, and two unrelated defects found in that base were
corrected and recorded rather than shipped: `higgsfield` (below_1b against a
$5.4B figure — web-checked to the 2026-08-17 $400M Series B at $5.4B) and
`modal` (a $1B+ row with an uncited entry stage, now `cite_pending`).

**2. Merge Cyngn and Cyanogen.** One company across one rename. The
`never_merge` guard this run had placed on the pair is removed.

**New shape:** 412 members, 157 rows in `excluded.csv`. $1B+ 60 / $10B+ 15 /
$100B+ 5 (14.6%). Entry stage Series A 239 / Growth 114 / Seed 56 / Pre-Seed 3.
C2A 53.3% on 45 cohort rows. `verify` clean; Arista Networks removed from
`notable_investments`.

**One sibling-state note.** The YC base (7,283 rows) landed today with no
classification at all and no `scratch/in-flight.json`, so every one of its rows
compares as a cross-investor disagreement against every sibling — 38 pairs on
Redpoint and 80 on Accel. These are recorded as `accepted` in both investors'
`cross-rulings.json` with an explicit instruction to **delete the entries at the
wave alignment** once YC classifies; they are a sibling's missing marker, not a
disagreement about a published track record. Reported to the YC session.


## Addendum, 2026-09-06 (second) — a probe bug re-opened the base; 412 → 413

This addendum exists because a **peer session corrected me**, and the
correction changed a base that had already been exported and ingested.

**What I got wrong.** Write-back 1 of §9 originally claimed the Internet
Archive was refusing plain-HTTP (port 80) connections while https answered, and
proposed swapping the scheme in `scripts/wayback-pull.py`. My evidence was three
requests a side. The YC session re-measured it — 9 paced alternating requests,
**http 7/9 and https 6/9, the failures rc=28 timeouts on both schemes** — and
the claim does not survive. The archive was simply flaky that hour. My
run-local https shims "worked" because re-running a request is a retry, not
because of the scheme. §9 write-back 1 is rewritten to say this, and the shims
are deleted (`scratch/README-retired-shims.md`).

**The defect underneath, which was real.** Neither puller checked `curl`'s
return code. A year whose probe never connected was recorded and printed
exactly like a year the archive genuinely holds nothing for: `0 entries`,
`no capture`. **Absence was being read off silence** — and portfolio recall is
built out of exactly those absences. YC fixed it upstream in `12402a7`; this
run's own `scratch/build-early-eras.py` had the identical bug and is fixed the
same way (3 retries with backoff, then a loud line naming the affected years as
UNKNOWN rather than empty).

**Re-running the repaired builder recovered 3 of the 4 slots** this run had
recorded as "no capture": `index-oid152` 2006 (65 companies — a full year of
additions the base never saw), and `index-oid157` 2003 and 2005. Only
`portfolio-default.shtml` 2002 is a true absence; its probe answered.

**What that changed in the published base.** Less than the recovered volume
suggests, because 2006's other 61 rows were already held from adjacent years:

- **+1 company. `amp-d` — Amp'd Mobile**, the Los Angeles MVNO. Defunct
  (Chapter 11, June 2007). Entry recorded as Growth at low confidence: the
  firm's own archive names Redpoint in the round — *"Amp'd Mobile Announces
  $67M in Funding with Investments from Universal Music Group, Highland Capital
  Partners, Columbia Capital and Redpoint Ventures"* (2005-08-08) — and the
  April 2006 release calls the next one the third round, so $67M is a ceiling,
  not a floor. The same archive carries an Amp'd post from **2004-08-25**, a
  year before that round, which hints the true entry is earlier; nothing cites
  it, so the row keeps `stage_uncited` and low confidence.
- **1 `first_seen` correction. `cgen-digital-media-advertising` 2007 → 2006**,
  merged from the logo-only `cgenmedia` row (`identity-merges.json`).
- `soa-software` and `vativ-technologies` also appear in the recovered capture
  and were already members; no change.

**Then the same bug turned up in the late eras, and cost more.** `/companies/`
**2021 and 2024** had failed transport on every retry of the original pull
(`rc=7` three times each, logged in `scratch/wayback-pull2.log`) and were
recorded as `0 entries`. Neither year existed in `sources/wayback/parsed/`.
Re-running the fixed `scripts/wayback-pull.py` landed both — **2021: 128
entries, 2024: 178** — along with every other era-year. That is two full years
of the firm's own listing that the closed run never read.

- It surfaced one more row, `profitboss`, which is **Owner** (owner.com) under
  its former name — the firm's own card says so: *"Redpoint first partnered
  with Owner, previously named Profitboss, during their seed in 2020."* Merged
  to the existing `owner` row, whose `first_seen` stays 2020.
- The wider effect is evidential rather than numerical: two more years of
  listing evidence moved **10 rows from tier B to tier A** (337 → 347
  auto-confirmed, `needs_review` 76 → 66).

**Two parser rules came out of it**, both in `build-early-eras.py`:

1. **Join acquired rows on the logo filename.** When a company is acquired the
   row's anchor is re-pointed at the ACQUIRER, so its acquisition year loses
   both the name and the company URL and reads as a brand-new company. The logo
   image does not change. `ACF783.jpg` is `m7` in 2003–2005 and nameless in
   2006; without the join it comes back as a second row for a company already
   in the base.
2. **Take an anchor as the company's own site only when that host is one the
   firm names elsewhere.** The first cut of this rule guessed instead, by
   testing the anchor host against the acquirer's *name* — and invented a
   company out of every acquirer whose name and domain differ (`amcc`,
   `getthere`, `webtv`, `mmcnet`). Caught by diffing the rebuild against the
   ingested base before export, which is the only reason it is a footnote and
   not seven fabricated rows in the published track record.

**New shape:** 413 members, 153 rows in `excluded.csv`. (The first addendum's
"157" was wrong; the file has held 153 since that rebuild.) $1B+ 60 / $10B+ 15
/ $100B+ 5. Entry stage Series A 238 / Growth 115 / Seed 57 / Pre-Seed 3. C2A
54.3% on 46 cohort rows. Tiers A 347 / B 57 / C 9. `verify` clean, profile
rebuilt.

Net of both recoveries the base is 412 → 413: **+2 companies** (Amp'd Mobile,
and Owner surfacing again under its old name) **−1 merge**. The count moved
barely; what moved is the evidence under it, and the fact that four year-slots
and two whole era-years were being read as "the firm listed nothing" when the
truth was "we never got an answer".

**Cross-investor note.** The 38 `accepted` YC-artifact entries in
`cross-rulings.json` are deleted, and the 86 on Accel with them, now that YC
carries an in-flight marker. Neither changed row is held by another investor,
so nothing was hidden by the comparison being skipped.

### Debt this leaves open

- **`portfolio-default.shtml` 2002** remains the one genuine absence in the
  early eras; its probe answered. No debt.
- The re-pull began while the archive was refusing connections on **both**
  schemes (`rc=7`, `rc=56` — logged in `scratch/wayback-pull3.log`), which is
  the cleanest confirmation available that the scheme was never the variable,
  and the retry loop then rode it out and landed every year. Worth keeping as
  the evidence for write-back 1.
- A **stale `scratch/in-flight.json` for `accel`** (pid 66968, dead) suppressed
  invariant 10 against that sibling. Left in place rather than deleted from
  under another session.
