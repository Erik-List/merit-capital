# Felicis — collection report (PRO-94)

One run, one session: Company Base, outcome classification and firm profile,
under the merged shape of `data/collection/COLLECTION.md`. Archetype A; the
T1–T5 derivation is PRO-87's, carried out against verified Felicis facts in
`decisions.md`.

**Result: `verify` clean in plain mode.** 493 published rows, 92 in
`excluded.json`, 100% fill on `status`, `valuation_range`, `entry_stage` and
`hq_country`, and **zero cross-investor disagreements** across the 208 rows
Felicis shares with other published bases.

**Usage line:** Erik reads Settings > Usage — kickoff percentages were not
given for this session; the line is filled at ingest (weekly %, Fable %, base
rows 493). Web searches used: 18, plus 12 direct page fetches. **Prompt count:
2** — kickoff and the ingest approval, which is §9's target shape. Ingested
2026-09-07; see §14.

---

## 1. What the base looks like

| | |
|---|---|
| Published rows | **493** |
| Excluded (`not_member`) | 92 |
| Tier A / B | 208 / 285 |
| Status | private 291, acquired 135, defunct 47, public 15, unknown 5 |
| Entry stage | Seed 270 (55%), Series A 157 (32%), Growth 65 (13%), Pre-Seed 1 |
| Valuation | below_1b 444, 1b_plus 38, 10b_plus 10, 100b_plus 1 |
| $1B+ / $10B+ / $100B+ | 49 / 11 / 1 |
| hq_country | US 448 (91%); CA 9, GB 6, IL 5, AU 4, BR 3, NL 2, FR 2, + 7 singles |
| C2A cohort | 71, graduated 26, **36.6%** |
| Focus | Consumer 97, SaaS 94, AI 75, Health 54, Media 32, Industrial 29, Fintech 28, Data Infra 25, Security 24, DevTools 11, Climate 6, Crypto 2, outside taxonomy 16 |

The book runs 2007–2026 and covers three distinct firms: Aydin Senkut's angel
era, the $40M-to-$900M fund ladder, and a current AI book led from the front.

## 2. The three deltas PRO-94 asked about — all confirmed, none needed a ruling

Each turned out to be a property of the base that changes how the run
**reports**, not a boundary question that changes what is **in** it.

**Δ1 — non-US rows: confirmed, and smaller than the issue expected.** 45 of
493 rows (9%) are outside the US. Both Creandum constants bind, and Adyen is
the concrete case: Euronext Amsterdam, so no `sec_public_float` exists and the
cap is web-cited ($37.64B). No ECB conversion was needed in the end, because
the aggregator publishes in USD at the as-of date; had it quoted EUR the §6
rule would have converted at that date's reference rate. The constant is
exercised; the machinery was not stressed.

**Δ2 — partial Form D visibility: confirmed, with a second cause the issue did
not name.** Coverage splits four ways:

| regime | rows |
|---|---|
| US, no Form D on file | 362 |
| pre-2011, site-only (no fund vehicle existed yet) | 64 |
| non-US issuer (files no Form D) | 43 |
| US, Form D on file | 24 |

The second cause is the interesting one. Beyond non-US issuers, **the
2006–2009 book predates the firm's own first EDGAR vehicle** — there is no
Felicis Ventures I, the ladder starts at II in 2010 — so those rows have no
fund-side filing either. Only 24 of 493 rows carry a Form D. Reporting one
blended number would badly misdescribe this base.

**Δ3 — multi-stage entries: confirmed.** 55/32/13 across Seed / Series A /
Growth. Broad, as predicted, so no re-check was triggered.

## 3. The site was the story: two independent first-party layers

felicis.com is Next.js over a **publicly queryable Sanity dataset** (project
`ggsokyyr`) — escalation-ladder step 2, no rendering needed. 277 company docs
carry the firm's own stage, status, deal partner, founders and sector tags.

The better find is in the archive. The 2011–2019 WordPress listings render a
`<p class="circles">` block per company naming **every round Felicis joined**,
in order — "Seed a b", "a b c", "c". The first element is the entry, and the
list is a follow-on record. It covers 151 companies, **90 of which the live
site no longer lists**: survivorship correction that carries its own stage
evidence.

Six site eras across two domains were parsed: felicisventures.com
`/portfolio.html` (2006–07) and `/portfolio.aspx` (2008–10), then felicis.com
`/portfolio/` (2011–19), `/portfolio-item/`, `/company/` and `/companies/`.
The pre-2011 domain is the Lightspeed pattern — felicis.com belonged to
someone else until about 2010, and its 2003–04 captures are a different site.

## 4. The calibration gate

**Stage golden set: 18 rows.** Below the playbook's 30–40, and the reason is
the investor rather than the effort: Felicis publishes **no first-party
announcement archive**. Its blog is a curated feed of third-party press
clippings (246 posts, 19 naming a round), so Creandum's class-1 announcement
layer does not exist here, and only 17 company records carry prose stating the
entry round. Rows were added only where a document answers; four more were
attempted and left in `golden.json` under `unresolved` rather than padded with
model opinion.

**Both layers scored blind, taxonomy-mapped first:**

| layer | score |
|---|---|
| archived `circles` ladder | **5/5** |
| live CMS `stage` enum | **17/18 (94%)** |
| the two against each other, over the full 57-row overlap | 54 agree |

The single CMS miss decomposes to the known failure mode, not noise: Ginkgo
Bioworks reads `Seed` because that was its stage *when listed* — the seed was
Y Combinator's S14 — while Felicis entered at the $9M Series A of March 2015.
That is Accel's *socure* class, and the circles layer is immune to it by
construction because it records what the firm actually joined.

Rather than promote one layer on a thin key, the gate adopted **agreement as
the class-1 signal** (`decisions.md` R3): both agree → publish; circles only →
publish; CMS only → publish, but a $1B+ or post-2020 row still goes back
through the judge; **layers disagree → neither labels**, and the row is judged
with a citation attempt. `scratch/build-entry-stage-layer.py` implements that
mechanically and withheld exactly three rows.

**Membership trap set: 30 traps, gate PASSED with zero false members at high
confidence.** 14 scored directly; 16 never reached the base because the
build's own fund-vehicle and non-operating-company filters removed them first
— the right outcome by a different mechanism, and recorded as such rather than
counted as a judge success.

## 5. Membership: 92 exclusions, 16 person clusters

Every one of the 93 membership rows arrived through the roster-name Form D
sweep **alone** — no listing on any Felicis surface, no fund vehicle on the
filing — so §1's evidence rule decided them before any individual row was
considered. The work was 16 people, not 93 companies:

| cluster | rows | class |
|---|---|---|
| John Anderson | 45 | homonym (Vancouver resource shells, Texas food LLCs, Santos Ltd) |
| Danny / Daniel / Dan Lee | 22 | homonym |
| Jack Abraham | 5 | ex-partner next firm (Atomic studio entities) |
| Wesley Chan | 3 | seat dating |
| 12 others | 15 | operator role, homonym |

**Wesley Chan is the textbook §1 case in both directions from one person.**
He was at Google Ventures before Felicis (roster 2015–2022) and left to
co-found FPV Ventures. Transphorm's Form Ds run 2010–2014 with him as Director
— a *prior*-firm seat. YENDO's run 2023 — a *next*-firm seat. Culture Amp,
in tenure, is a genuine member. Same name, three answers, decided by the date.

**Three rows survived the a16z director-of-record test** — a current partner
listed as Director on the filing itself, in tenure — and all three then
resolved to companies the base already held under their trading names:
Atlas Labs, Inc. → Atlas Health (Sundeep Peechu; the $40M Series A Felicis
led), PRM Solutions, Inc. dba Proton.ai → `proton` (Niki Pezeshki), Hippo
Analytics Inc. → Hippo Insurance (Victoria Treyger). Identity merges, not new
members.

## 6. Five defects found and fixed, each a class rather than a row

**a. The Wikidata `hq_country` layer is broken on this book (`decisions.md`
R5).** `prepare` filled the column on 226 rows, 104 from Wikidata, and the
split is stark: **all 14 multi-token labels are right; the 90 single-token
labels are wrong at a rate no layer survives** — Gusto→Netherlands,
Wish→Japan, Guild→Japan, Cedar→Japan, Planet→Greece, Mercor→Latvia,
Alloy→Australia, Chalk→Czech Republic, Proton→Ukraine (that is Proton AG, the
Swiss privacy company), Karma and Milo→"Czechoslovakia" (not an ISO code and
not a state), and Survios→a raw `wikidata.org/.well-known/genid/…` URL. This
is the First Round finding on a book even more exposed to it: Felicis names
its companies Key, Origin, Sphere, Stream, Arena, Feel, Depot, Condor. The
failure is silent in the exact way §8 warns about — the queue asks only about
EMPTY fields, so the row never reaches the judge. 52 rows carry
`model_disputes_source` as a result.

**b. 44 slug artifacts, fixed in the parsed source (`decisions.md` R6).** Two
causes: the 2007–2010 logo eras publish identity as an image filename
(`bumplogocurrent2`, `justintvlogo`, `midomi-small`), and the current CMS
re-creates a company document with a disambiguator that is sometimes a raw
UUID. Left alone the base publishes a row named "Dig 2 7869de28 2b5e 4634
A24a C5a487f3a955". Per §5 the fix belongs in the parsed source rather than
`identity-merges.json`, and here that matters twice over: for most of these
the canonical row does not separately exist, so the correction is a **rename**
that gives the company's only row its real name. Three were left unresolved
and reported rather than guessed.

**c. Site chrome parsed as portfolio companies (`decisions.md` R7).** The 2011
listing renders its social footer — `linkedin.png`, `groupon.png`,
`twitter-small.jpg` — through the same `images/logos/` path as its portfolio
cards, so LinkedIn and Groupon were published as Felicis positions. This is
the First Round "rejects, not members" class in a new form. The discriminator
is exact and now in the era pattern: portfolio cards use a **relative** `src`,
the chrome an absolute `felicisvc.com` host.

**d. The float sweep's name-collision class.** `Arena` carried a $0.08B public
float from a registrant that merely shares the word; `Exa` carried a 2016
as-of date; `Proton`, `Stream` and `Ginkgo Bioworks` carried wrong statuses
(`acquired`, `defunct`, `acquired` — Ginkgo trades as DNA). All disputed with
`model_disputes_source`.

**e. The deterministic C2A layer was computing graduation for the noise.** It
decided 32 issuers, but only 6 survived into the final base and **none** has a
final `entry_stage` of Seed — it had been working on the Canadian mining
shells and Las Vegas casino vehicles of the homonym clusters. On an investor
whose Form D coverage is a name-matched subset, the C2A layer inherits the
sweep's noise wholesale. What replaced it is the circles ladder: a row whose
ladder is `["Seed", "Series A", …]` is a graduation the firm itself recorded.
65 rows decided that way; 161 stay `cohort_unverified` because no ladder
covers them.

## 7. Recall: zero missing members

Three layers, all clean:

- **Exit-side EDGAR full-text sweep** — 145 hits on four entity-qualified
  phrases, 55 registrants, 34 third-party, **zero new members**. The
  third-party set is proxy-statement director bios (AMD, Deluxe, CA, Lam
  Research), fifteen Guardian insurance separate accounts, a Reg A
  crowdfunding pitch deck listing Felicis deals as social proof, and acquirer
  filings for companies already in the base.
- **Wikipedia insource sweep** — 48 articles, 28 already in the base, 4
  company candidates, all four already members under another name. The first
  pass with the bare word "Felicis" returned 202 articles of mostly **Latin**
  — papal bulls (*Dudum felicis*), Roman inscriptions (ANTONINI PII FELICIS
  INVICTI), species binomials (*Cincinnobotrys felicis*) — which is the Cherry
  common-word trap at its most extreme. Entity-qualifying the phrases cost
  nothing and fixed it entirely.
- **Parametric enumeration plus a 2025–26 press sweep** — the three deals the
  press named (Dreambase, BuildForever, Blomma) were all already in the base.

**One rejection recorded.** *Fresh Guide*, named as an Aydin Senkut portfolio
company in a 2015 profile of him, appears on **no** Felicis surface in any
era. `decisions.md` D-T2a decides it: the 2006–2009 book is IN where the FIRM
published it and OUT where the only evidence is Senkut's personal angel
cheque. It is the one row where that second clause bites.

This reproduces §3's measured Sequoia shape exactly — the site layers carry
recall, the noise is precision-side — and six site eras plus a live CMS are why.

## 8. Open rulings for Erik

**R4 (the one that moves rows) — the 2006–2009 angel era.** Felicis was
founded in 2006 but its **first institutional fund closed in 2010**, which the
EDGAR ladder corroborates exactly: no Felicis Ventures I files at all. For
roughly four years the capital behind the book was its founder's own. That
satisfies **two standing tests with opposite outcomes**, which is §1's
definition of a delta rather than a derivation: T2 asks whether a fund of the
firm held the position and the answer is no, while §1's evidence rule says a
listing on the investor's own site in any era suffices alone — and Felicis
published these companies as its portfolio, on its own domain, under its own
name, and still counts them in its public track record.

**This run publishes them as members**, reading a solo-GP firm deploying its
founder's capital through its own branded vehicle as the firm, not as a
partner's personal angel book taken on the side while employed elsewhere
(Kushner; Cherry's founder-angel positions). The nearest precedent cuts the
other way *on its facts* and confirms the distinction: First Round's D-T2a
excluded its founders' pre-firm book **because that firm published it
separately** as "investments made prior to First Round Capital". Felicis makes
no such separation.

It moves **64 rows** (the pre-2011 regime in §2), including Mint, Meraki,
Twitch, Dogster, Freewebs, Powerset and BrightRoll. Reversing it is a
re-export, not a re-run.

**Smaller ones, all recorded and none blocking:**

- **BrightRoll's entry stage.** The live CMS says Series A; the firm's own
  archived listing said Series A in 2012 and then **Seed in 2013, 2014, 2015
  and 2016**. Published Seed on the firm's sustained reading at medium
  confidence; no contemporaneous source names the round.
- **Opendoor's entry stage.** CMS says Series A, the archived ladder says
  Series C, press places Felicis in the Oct-2015 $80M Series C. Two of three
  agree, so the row publishes Growth at medium confidence.
- **Credit Karma's entry stage.** Both first-party layers say Seed; TechCrunch's
  Nov-2009 report names Felicis in the $2.5M Series A. Published Seed on the
  firm's own record, flagged.
- **Vannevar Labs.** Last priced round $75M Series B (2023) at ~$575M; the CEO
  references $1.5B in company materials and vendors quote upward. Rule A holds
  the row at `below_1b`. This is a case where the rule and the likely market
  value may diverge, and it is flagged rather than quietly resolved.

## 9. Debt behind the green verify

| flag | rows | what it means |
|---|---|---|
| `cohort_unverified` | 170 | C2A follow-on leg unverified — no round ladder covers the row |
| `stage_prior` | 73 | entry stage is a flagged low-confidence prior on an unidentifiable row |
| `model_disputes_source` | 52 | a deterministic layer's value was overruled and why is on the row |
| `country_prior` | 18 | US desk prior after a bad Wikidata join, flagged not silent |
| `stale` | 8 | private mark older than 24 months, no collapse evidence |
| `cite_pending` | 8 | $1B+ row whose entry stage has no class-1 citation |
| `duplicate_suspected` | 4 | flagged, never silently merged |
| `stage_uncited` | 3 | citation attempted and failed |
| `parser_artifact` / `weak_cik_join` / `needs_web_value` / `stage_disputes_band` | 6 | as named |

`focus` is 477/493; the 16 nulls are **outside the closed twelve**, almost all
edtech (ClassDojo, Guild Education, Piazza, Pluralsight, Tynker, Top Hat,
Inkling, Civitas Learning). Force-fitting them to SaaS would corrupt the
distribution, so §6's null-over-force-fit applies and they are reported.

`hq_city` is 0/493: the queue never asked for it and it is not an invariant-1
column. Flagged here as a known gap rather than a silent one.

**Self-consistency (duty 7): 100/100 cells agree** on a blind re-classification
of a 25-row (5%) random sample. No `unstable` flags.

## 10. Cross-investor (invariant 10)

Started at **56 disagreements** over 228 shared rows; ended at **0**, with 193
agreeing and 15 accepted with reasons in `cross-rulings.json`.

The invariant did real work. It caught rows this run had **under-called**:
Unconventional AI at below_1b against three siblings holding it at $4.5B; Exa
at below_1b against three holding it at $2.2B; Guardant Health carrying a
stale $6.20B float against siblings at $21.88B and $22.54B; Plaid at a 2021
$13.4B unicorn-snapshot value against three siblings lower and more recent.

It also caught **two genuine name collisions**, both ruled `distinct`:

- **a16z's and Lightspeed's `arena` rows cite an LMArena round.** Felicis's
  Arena is arena.ai. Chasing that citation is what surfaced LMArena's own
  $1.7B mark, which this run then applied to its separate `lm-arena` row.
- **a16z's `luma-ai`** is the video-model company; Felicis's `luma` is the
  mesh-WiFi hardware business acquired in 2018. a16z separately carries its
  own `luma` row that agrees with this base exactly.

Where **this run is the fresher side** — Runway at $5.3B against two siblings
at below_1b, Poolside at $12B against $3B, Assort Health at $1.2B against
three at below_1b, Alloy, Cedar — the rows are accepted and flagged for the
wave-level pass, because a session aligns its own investor and does not edit a
sibling's base.

## 11. Firm profile

- **AUM $6.74B**, both range ends, from ADV Schedule D Section 7.B (22 private
  funds). Felicis Ventures Management Company, LLC is an **exempt reporting
  adviser** (CRD 162301, SEC 802-74738), so no Item 5.F exists. The 7.B table
  also reaches three vehicles the EDGAR name search cannot — **Clover Fund,
  L.P.**, **Clover-M LLC** and **F-LMA L.P.** carry no "Felicis" in their
  names. Clover Fund was a golden-set trap expected out as an unidentifiable
  fund-shaped name; the ADV identifies it as one of the firm's own vehicles —
  same verdict, filing-grade basis. (The name is not a coincidence: the firm's
  mark is a four-leaf clover.)
- **Ten funds, every size filing-grade.** Felicis files a definite offering
  amount and reports it fully sold, so each entry is asserted against its own
  Form D accession at build time — the opposite of Lightspeed's
  "Indefinite"/$0 style. $40M (II, 2010) → $70M → $120M → $200M → $270M →
  $505M → $600M + a $300M Focus Fund → $825M (IX) → **$900M (X, 2025)**.
- **investment_range** $1M / $7M / $350M. The median is a round-size proxy
  from stated entry rounds and is flagged as such; the ceiling is the largest
  round Felicis has led (Mercor's $350M Series C), consistent with a 10–15%
  concentration of Fund X.
- **47 individuals** from the live team CMS, 2 departed against the archived
  roster. HQ **Menlo Park, CA**, filing-grade from 10 of 18 own-vehicle Form Ds.
- **Icon**: the firm's four-leaf clover, chosen by measurement. `--discover`
  offered five assets; the 256px PNG is the only real mark, and it is
  #FF7E00 on transparency, which the rules refuse on a light plate at 2.44:1.
  On a `#141414` plate it measures **7.0:1**, artwork 256px → 189px (0.74x, no
  enlargement), edge ramp 0.93px, inside the keyline. Uploaded at ingest.

## 12. Method notes for the playbook (proposed, not applied)

Written up as a diff proposal in the closing message rather than applied here,
since `COLLECTION.md` belongs to the designated tooling session while a wave is
running (§12).

1. **A logo era can carry the firm's own ROUND LADDER, not just names.**
   §5 treats a logo era as a recall problem to be solved from filenames.
   Felicis's 2011–2019 wall carries a per-company list of the rounds the firm
   joined, which is simultaneously the strongest `entry_stage` layer this run
   had and a **C2A graduation record** — and it covers 90 companies the live
   site has dropped. Worth a sentence in §5 and in §6's C2A section: when the
   deterministic Form D graduation layer is built on a name-matched sweep, it
   inherits that sweep's homonyms wholesale, and a first-party ladder beats it.

2. **Two first-party stage layers should be scored against each other, and
   agreement used as the class-1 signal.** §4 promotes or demotes each layer
   independently. Where a firm publishes two, their *agreement* is stronger
   than either score alone and their *disagreement* is a reliable pointer at
   the socure class — three rows here, and the one the key could settle went
   against the CMS exactly as predicted.

3. **Site chrome is a member-inventing class alongside acquirer marks.** §5's
   First Round paragraph names acquirer logos beside exits. Add the footer:
   social links rendered through the same asset path as portfolio cards.
   Relative-vs-absolute `src` was the exact discriminator here.

4. **Entity-qualify Wikipedia phrases when the firm's name is a common word in
   any language.** The Cherry lesson is stated for English namesakes; "Felicis"
   is Latin and returned papal bulls and species binomials. Same fix, wider
   trigger.

5. **`fields[...]["value"]` and the two required profile inputs.** §11 already
   warns about the dict `_readme` and the mirrored `value`; add that
   `fields["funds"]["value"]` must be the **list**, not investor.json's
   `{"funds": [...]}` wrapper, and that `team-members.json` must be a flat list
   with a **list-valued** `role_bucket` — which conflicts with
   site-portfolio.py's `{"rows": [...]}` requirement, so the same pull needs
   two files.

## 13. Infrastructure notes

**Both capture archives were down at once.** web.archive.org refused
connections intermittently for most of the session, and
`index.commoncrawl.org` was unreachable throughout, so the Common Crawl layer
never ran. Mitigated without losing the layer: the full 27,847-row CDX index
was pulled minutes before the outage and is kept as evidence at
`sources/wayback/raw/`, and the 117 slugs the truncated puller missed were
merged back into the parsed year files. The three listing years the puller
could not fetch (2011–2013) were recovered by a patient background retrier on
the shared IA budget, and 2011 is the year that turned out to contain both the
site-chrome defect and 24 otherwise-unseen companies.

**A self-matching `pgrep` cost two dead waits.** `until ! pgrep -f "wikipedia-insource.py felicis"`
matches its own shell's command line and never exits. Worth knowing for
anyone scripting waits in this repo.

---

## 14. Ingest (2026-09-07, on Erik's approval)

Order per §9: icon upload → `ingest-investor.ts` → `ingest-companies.ts`.

- Icon uploaded: `investors/felicis-b5ca5f2614.png`.
- Investor row live, `id 8008aa85-be07-4037-8ce5-fc71a09bb163`.
- **493 companies** in `public.companies`.
- App verified rendering: the leaderboard row reads "Felicis · 1 in 10
  companies → $1B · US +3 · Seed–Growth · $1M–$350M · Generalist (8)", the icon
  loads through `next/image` from the bucket, and there are no console errors.

**The Lux incident was avoided, not fixed.** `ingest-investor.ts` still ignores
its positional slug and syncs the whole table. Four investors on disk were
carrying pre-ingest placeholder `icon_url`s at ingest time — 8vc,
battery-ventures, benchmark and greylock — and Benchmark's
(`benchmark.svg#glyph-B`) is the exact unconfigured `next/image` host that
white-screened the app during the Lux run. Running it as
`npx tsx scripts/ingest-investor.ts --investors name=felicis` confines the
write to one row, and the DB was checked afterwards: **zero** non-bucket
`icon_url`s across all 15 investor rows, so the crash condition is absent and
four sibling sessions' ingest gates are untouched.

The three fixes PRO-95 proposed remain unmade. #1 is the cheap one — the
`--investors name=<slug>` filter demonstrably works, so only the default and
the silently-ignored positional argument are wrong.

**Prompt count: 2** — kickoff and the ingest approval, which is §9's target.

## Addendum 2026-09-20: S2A with every Seed row decided (PRO-132)

Felicis' graduation column had never been judged under the status contract:
it held the retired booleans and 169 `cohort_unverified` flags until
`migrate-graduation` cleared them. PRO-132 then made the absence of a later
round a finding: a Seed row past the 24-month clock with no evidence of a
later round did not graduate, and every no records the dated search that
found nothing (the firm's archive, the Form D sequence for a US company, at
least two publisher surfaces; COLLECTION.md §6). The seed book was judged in
five batches.

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 203 | 29 | 174 | 85 | 89 | 48.9% | 100% |

Of 203 seed entries, 29 were too recent to count; of the 174 that remain,
48.9% raised a later round. Of the 89 that did not, two rest on the filings,
37 on a cited end and 50 on a dated search of the named surfaces. The
firm's own archived portfolio ladder (2011 to 2019) read Seed then Series A
for several rows and is cited `first_party` where it does.

What moved:

- Rows found by fetching what the surfaces missed: Bump Technologies and
  Granular (real Series A/B rounds before their acquisitions, invisible to
  the short-name searches) and Freewebs (renamed Webs in 2008 before
  Vistaprint bought it in 2011).
- The unknown-seed bar (COLLECTION.md §6) graduates CarWoo ($6M, 2011),
  DriveTime ($11M, 2019) and Gamalon ($20M, 2018); it keeps Meili's ~$8.8M
  raise under the $16M bar for a 2023 entry, and in review it reverses
  Covalent, whose only later round is an unnamed $5M (2024) under the $12M
  bar for a 2021 entry.
- Knox graduates against the Form D layer (a $25M Series A in March 2026 the
  rescan had not caught); LMArena graduates on the $150M Series A Felicis
  led in January 2026.
- In review: Nimble (NimbleRx; the $28M 2017 round led by Sequoia, CNBC) and
  Operant (the $10M Series A of September 2024 co-led by Felicis,
  GlobeNewswire) graduate; both had been left open. Everalbum, a PRO-135
  handoff, is classified: a Series A entry on the firm's own listing,
  continuing as Paravision after its 2020 consumer shutdown.
- Mon Ami and Alma Campus read `undetermined` in the stage (nothing dates the
  entry).
- A local-language re-check of the non-US nos (`googlenews_local`) found no
  later round.

Several entry dates are approximations and are named in their notes: where
no seed announcement exists, the judge used the firm's earliest listing
capture or the company's founding era. For a no that only errs on the safe
side of the clock (a capture date can only be later than the entry), and for
a graduation the date does not decide the verdict.

`verify` passes every graduation check. Two base problems remain,
`everalbum`/`optrip` present while their merge canonicals are absent; the
PRO-121 session folds them with a rebuild after this commit.

For Erik: **Credit Karma** was re-staged to Series A (Wikipedia names Felicis
in the November 2009 $2.5M round it calls a Series A, with no earlier seed
documented) against the firm's own "Seed" tag; **TalkIQ**'s Form D entry
(2017-08-30) sits three weeks before its announced $14M Series A and may be
the same financing; **RapLeaf** (which became LiveRamp) is a no because no
non-vendor source names a priced RapLeaf round.

Correction 2026-09-21: **Aloha** graduates. The First Round judge identified
it as the Bisanz wellness brand refounded in 2017 under Brad Charron, which
took Semcap's $68M growth investment in April 2024 (Food Dive); the earlier
no had not identified the company. The table above reads 85 graduated, 89 not,
48.9%.
