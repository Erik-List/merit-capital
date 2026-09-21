# Khosla Ventures — collection run report

**Run:** PRO-98, one session, 2026-09-07. Merged shape (base + outcome
classification + firm profile in one run), `data/collection/COLLECTION.md`.

**Usage line:** the account's weekly and Fable percentages were not read at
kickoff and are filled at ingest. Web searches used: **11**. Base rows: 507.
**Prompt count: 3** at the time of writing — kickoff, the X1 ruling ("Nextdoor
is out unless a fund held it pre-merger; keep going"), and a continue. The
ingest approval will be the fourth.

**Status:** `verify` clean in full mode. Export, review surface and profile
written. **Nothing has been ingested** — that waits on your approval (§9).

---

## 1. What the base looks like

| | |
|---|---|
| Published members | **507** |
| Preserved in `excluded.json` | **165**, all `not_member` |
| Tiers | A 153 · B 290 · C 64 |
| Status | private 251 · acquired 123 · defunct 107 · public 25 · unknown 1 |
| Valuation band | below_1b 454 · 1b_plus 37 · 10b_plus 13 · 100b_plus 3 |
| Entry stage | Series A 221 · Seed 212 · Growth 71 · Pre-Seed 3 |
| Era | 2000s 40 · 2010s 336 · 2020s 68 · undated 63 |
| C2A cohort | 40 rows, 21 graduated, **52.5%** |
| Firm profile | 19 funds, $21.73B AUM, 46 people, icon dry-run passed |

**The $1B+ share is 10.5%** (53 of 507), well under the 20% guard — a book with
a long, old, quiet tail. **`defunct` at 21% is the highest of any landed run**,
and that is a real property of the firm rather than better detection: the
2006–2013 cleantech book is most of it (Range Fuels, Stion, Calera, KiOR,
Coskata, LightSail, Transonic, EcoMotors, Danotek, Alveo, Spatial Photonics).
The usual caveat still applies in the other direction — `defunct` is
undercounted by construction, quiet shutdowns present as `private` or
`unknown`, and no mortality rate should be read off this column.

**The C2A rate carries its selection bias in the sentence**: of the 40 seed
entries where the record could be established, ~53% graduated to a priced
Series A. The establishable set skews toward visible successes, and 172 of the
212 seed rows are censored or undetermined and are null by rule.

---

## 2. The evidence layers, and what each was worth

Khosla is a US-desk firm with a **disclosing but shallow** site, which put an
unusual amount of weight on the archive.

- **The live site** is one Webflow page: 114 curated cards in eight categories,
  each carrying the firm's own fund label (Seed / Early / Growth on 88) and an
  exchange ticker on 17. No per-company pages in the sitemap, no CMS API.
- **The archive carried the real book**: **429 distinct slugs, 2010–2026**
  across five eras. Two shapes mattered. The 2010–2014 portfolio was a
  *positioned scatter chart* whose every company is an absolutely-positioned
  `<span>` naming its own description block —
  `FillCompanyDesc(this, 'comp_<slug>')` — so slug and rendered name come off
  the same element and the era needs no name inference. The 2014–2023
  WordPress site served one page per company.
- **Reading those per-company page BODIES, not just the CDX index, was the
  single most valuable thing this run did.** The index gave 429 slugs and named
  175 of them not at all; the bodies gave the firm's own name for 304, its own
  sector categories, and a `<table class=dates>` carrying **`Founded` and
  `Invested` years** — a first-party dated entry claim for 279 companies that
  no other layer produces.
- **Form D sweep**: 1,601 issuers across a 123-name roster.
- **Negative results, recorded rather than left silent**: Khosla publishes **no
  deal-announcement archive** — its 389 `/posts/` are podcasts, interviews and
  essays, so the class-1 announcement layer Creandum had does not exist here,
  and `entry_stage` had to rest on citation and filing structure instead.
  Common Crawl's index was unreachable for the whole run window.
  `khoslaimpact.com` and `old.khoslaventures.com` are both dead domains and
  neither is in the archive. The Internet Archive refused connections outright
  for roughly twenty minutes; the pulls are idempotent and a second pass
  recovered every era.

---

## 3. The calibration gate: two layers scored, two refused

The gate did what it exists for — it changed the evidence order before the
grind ran, rather than auditing one afterwards.

**`site_fund_label` (the card's Seed / Early / Growth): 7/15 → DEMOTED.**
Every miss is an "Early" row whose true entry was either **earlier** — DoorDash,
Hermeus and Instacart all entered at the *seed* — or **later** — Nutanix, Okta
and Guardant entered at the *Series B*, OpenAI at an unnamed $50M round. Plus
Rocket Lab, where a "Seed" label over-reads a documented Series A. One cause:
the field names the **fund that holds the position**, not the round the firm
entered at, and Khosla's main fund writes from seed through Series B and later.
This is the Accel *socure* class in a new place. Compare: Accel's CMS label
30/31 → class 1; Menlo's milestones 33/34 → class 1; Thrive's job board 0/10 →
refused.

**`site_invest_year` (the archived page's Invested year): 14/16 → PROMOTED for
2011+, DEMOTED to a ceiling before it.** Fourteen land on the documented entry
year exactly, including every row from 2011 on. Both misses are pre-2010
cleantech rows and both are **late by exactly three years** — Amyris 2009
against a documented 2006 Series A, LanzaTech 2010 against 2007. The cause is
not noise: the CMS this field lives in was built in **2015**, so the early book
was entered retrospectively and drifts toward a later round the record-writer
could see. Both misses late and none early is what makes it a ceiling rather
than a spread.

**Wikidata's `hq_country` pre-fill: REFUSED, all 65 fills cleared.** The First
Round one-word-name failure, at a rate no layer survives: Datera→CZ (Santa
Clara), Fundera→IT (New York), Plum→JP, Fresh→IE, Castle→GB, Donna→ZA,
Bold→CL, BRT→IT, Atmos→CA, Forward→GB. Sword Health returned the footnoted
prose `"Portugal /  United States [96]"` and Airwallex `"Australia /  Hong
Kong"` — not country codes at all, which would have failed `verify`'s
vocabulary check at the very end rather than here. Only Blockstream (Victoria
BC) and Bridge International Academies (Nairobi) survived.

**Membership trap set: CLEARED, zero false members at high confidence.** Nine
of the 21 traps never reached the judge because the build's own filters removed
them first. Of the twelve that survived, ten were judged correctly with no help
from the key, and **two key rows were corrected by the evidence** (§4 scores
both directions): Shoes of Prey, written as a Bling Capital trap, is tier A on
Khosla's own 2015 listing with Ben Ling's Form D dated *inside* his Khosla
tenure; and Arista, pre-registered `uncertain` to avoid pre-judging Accel's open
case, sits on Khosla's own all-companies page, which suffices alone. Critically,
Velo3D and DoorDash were **not** rejected for having a roster founder — the
founder-operator class did not overcorrect.

---

## 4. The grind, and what the seat-dating rule actually did

683 rows judged; 224 of them membership calls resolved as **62 clusters**, not
row by row (§3). **163 not_member / 61 member.**

The clusters are the story. **Keith Rabois's site window reads 2012–2026, and
it is a union that hides the Founders Fund years** — he was Square's COO
2010–2013, at Khosla 2013–2019, at **Founders Fund 2019–2024**, and back at
Khosla from 2024. Ten of his 21 filings sit inside the Founders Fund window
(Homevest, Miami Labs, Orgio, Pietra, Royal Markets, SpotMap, Virtual Kitchen,
Workstream, Indie, All Day) and five predate Khosla entirely (Yelp, Xoom,
Decorati, Milo, Sportelligence). Two survive as Khosla positions: Faire and
Forward. This is the Carlo Biggio case, and without the seat-dating rule this
one roster name alone would have added fifteen false members.

**Doug Cameron appears under two spellings** ("Douglas Cameron" and "Doug
Cameron", 19 rows between them) and the whole cluster is **First Green
Partners-shaped** — his next firm, which itself surfaced in the sweep. **Milo
Werner's nine rows are all classic The Engine positions** (Natel, Infinitum,
Treau, Unspun, Foundation Alloy). **Eric Johnson, James Kim / Jim Kim, Daniel /
Dan / Danny Levin, Bryan Gartner, Ian Kennedy and Ian Robinson** are homonym
clusters — the Levin key alone holds three different people, none of them
Khosla's, which is the Accel "Daniel Levine" precedent in a new place.

**The founder-operator class went both ways, as it should.** Out: Ari Zilka's
own Terracotta, Tim Westergren's Pandora, Nessan Bermingham's Intellia, Justin
Kao's Helix — founder seats on their own companies, predating their Khosla
years. In: Shoaib Makani's KeepTruckin, Evan Moore's Juno, Benny Buller's
Velo3D — companies a Khosla fund actually backed. Being on the roster is
neither a qualification nor a disqualification.

---

## 5. Recall probe: 14 additions, every one cited

Three streams diffed against the landed base — the Wikipedia insource sweep
(178 articles, 69 already in base, 32 candidates), the exit-side EDGAR
full-text sweep (700 registrants, 230 third-party) and parametric enumeration.

The misses have exactly the shape COLLECTION.md predicts for a US-desk firm:
**no US Form D and no site listing**. Five non-US issuers (AirHelp, Airwallex,
Even Healthcare, HealthifyMe, Tools for Humanity), an incubation the site never
listed (Modal, "founded out of Khosla Ventures"), five quiet US seeds (Nebula
Genomics, PatientBank, Summon, True Link, Willow Wealth), one 2007 merger-era
position only the exit-side sweep saw (Verenium, out of the Diversa/Celunol
combination) and one the build's own industry filter had removed (Dusty
Robotics).

**Rejections are recorded too**, so the next run does not re-ask: Rappi,
Replit, Cohere and Bloom Energy were kickoff model priors that no layer
supports — Bloom Energy in particular is a Kleiner Perkins position, which is
D3 rather than a Khosla one. Serve Robotics was found, ruled `member`, and then
**corrected to `not_member`**: its only evidence is a post-listing 13G, which
the standing rule makes crossover treasury. Flagging it while publishing it as
a member would have been the Hawthorne Labs mistake.

---

## 6. Four defects found in the pipeline, all fixed

The scheduled rebuild exposed three bugs in the recall-addition path and the
profile build a fourth. Each would silently lose or break rows on **any**
investor, not just this one.

1. **`LP_FORM` matched `LP$` with no separator before it**, so AirHelp was
   deleted as a limited partnership. **Yelp, Gulp and Kelp are the same shape**
   and would vanish on any base where the row carries no listing evidence.
   Fixed to require a comma or whitespace before the suffix.
2. **The non-portfolio-industry rule and the ex-partner rule each dropped a
   recall addition** — Dusty Robotics, twice, once as "Construction" and once
   on Richard Boyle's tenure. A recall addition reaches the base only after a
   session verified it against a citation, which is stronger than either signal.
   Both rules now exempt them. The rules themselves stay: 46 of the 48 rows the
   industry rule removed on this run were genuine homonym noise.
3. **`identity-merges.json` must be nested under the investor slug and use
   `reason`, not `why`.** Written flat, **all 35 merges silently did nothing** —
   the build printed no "identity overlay" line at all, and the only way to
   notice was that duplicates survived a rebuild that claimed to have run.
4. **`build-firm-profile.py` unions two files of different shape.** A newer code
   path merges `formd-sweep.json` (keyed by accession, carrying `issuer`,
   `city`, `state`) with `fund-formds.json` (keyed by issuer name, carrying only
   `{cik, filings}`) and then reads `rec["issuer"]` and `rec["city"]`
   unconditionally. It raises on every entry from the second file. No landed
   investor had exercised it.

The name-variant merge also folded the unrelated **Even** into **Even
Healthcare** on a shared prefix; fixed in data through the `never_merge`
overlay the build already supported, along with four other genuine prefix
collisions.

---

## 7. Open rulings and judgement calls for you

1. **X1 — Nextdoor: ruled and applied.** You ruled it out unless a fund held it
   pre-merger. No such round appears in any layer, so the row stays out. The
   ruling was **ratcheted into COLLECTION.md §1 under T3 the same day** as a
   standing sponsor-promote precedent, so it binds every future run.
2. **Arista Networks — a boundary row, published as a member, flagged.** It sits
   on Khosla's own 2014–2015 all-companies page with the firm's own invest year
   2012, which suffices under D9. But Arista was founded in 2004 and funded
   largely by Bechtolsheim and Cheriton personally, so there is no obvious
   venture round for Khosla to have entered. Accel carries the standing open
   arista case on *different* evidence (13G-only). The two runs may legitimately
   differ on membership; invariant 10 binds status and valuation, not
   membership. **Your call whether the site listing alone carries it.**
3. **At-Bay — a status disagreement I did not copy.** Another landed base carries
   At-Bay as `acquired`; this run could not corroborate a sale. I aligned the
   valuation band and left the status flagged rather than adopting a sibling's
   status on faith.
4. **Commonwealth Fusion and TerraPower read `below_1b`, and that is Rule A
   working.** CFS raised an $863M Series B2 on $4B total and has **never
   disclosed a valuation**; TerraPower's $650M round likewise. The only figures
   in circulation are vendor estimates, which Rule A forbids banding on. Both
   are recorded `below_1b` with the check and its date, exactly as Justworks
   was. If you want these banded on vendor marks, that is a change to Rule A,
   not to these rows.
5. **Impossible Foods stays at the 2021 $7B mark, stale-flagged.** Secondary
   marketplaces quote it near $500M, but §6 keeps secondary estimates in the
   note, and a marketplace quote is not the priced tender the collapse rule
   requires. Flagging rather than re-marking.
6. **The AUM composite may double-count one pair.** Section 7.B lists Khosla
   Ventures VI ($4.72B) and Khosla Ventures VI (AIV) ($4.17B) separately and the
   composite sums them as filed. An AIV usually holds a subset of its main
   fund's positions, so $21.73B is a ceiling on that pair. An exempt reporting
   adviser files no Item 5.F, so the usual cross-check — the 7.B roster summing
   to RAUM to the dollar — is unavailable.
7. **`AI & Applied AI` is only 23 rows, and that is a signal, not an error.**
   The focus pass runs off the firm's own categories, and Khosla's vocabulary
   has **no AI category at all** — its AI companies sit under "Enterprise" and
   "Frontier". This is the §11 signal in its strongest form: a sector absent
   from the firm's own vocabulary despite obvious portfolio evidence (OpenAI,
   Cognition, Sakana, Field AI, Physical Intelligence). Flagged rather than
   corrected by hand.

## 7a. Debt behind the clean verify

| Flag | Rows | What it means |
|---|---|---|
| `stage_uncited` | 352 | entry round not established by a class-1 citation. Structural for this firm: **no announcement archive exists**, so the usual class-1 source is absent and each row needs its own press citation. |
| `status_uncertain` | 77 | "no trace after the last filing" — an absence inference, not a recorded end-state |
| `cite_pending` | 53 | invariants 3 and 4 debt, resumable |
| `formd_adjudicated` / `unannounced_deal` | 49 | the director-of-record members from the cluster pass, medium confidence |
| `identity_uncertain` | 36 | mostly one-word chart-era names that do not resolve (Go, Sup, Vert, Strut, Simpler, Because) |
| `needs_web_value` | 27 | resolved in the A/B pass; the flag records that the check happened |
| `city_unknown` | 23 | null city rather than a prior (§6 forbids city priors) |
| `model_disputes_source` | 20 | deterministic layers overruled with a note |
| `suspected_duplicate` | 18 | flagged in-run, merged at the rebuild |
| `cik_weak` | 9 | weak CIK joins quarantined; no band rests on one |

`hq_city` is filled on 390 of 507. `prepare` never queues it — the column is
authored alongside `hq_country` — and Lux shipped with zero, so this is
coverage, not a regression.

---

## 8. Standing verification duties

1. **$1B+ web-verified** — all 53 rows; five deterministic pre-fills were wrong
   and corrected (below).
2. **C2A `false` vetted** — enforced by invariant 7, no row ends false + $1B+.
3. **Weak CIK joins audited** — 9 quarantined, no band rests on one.
4–5. **Stale-float sweep** — Guardant ($6.20B float → $21.88B cap), Opendoor
   ($0.34B → $3.97B), Nutanix, Okta, Rubrik all re-pinned to cited caps.
6. **Unicorn re-intersection with loose normalisation** — zero unicorn-list rows
   left recorded `below_1b`.
7. **Self-consistency, 25-row blind sample** — no disagreement; the apparent
   nulls are values living in the deterministic store, which `export` merges.
8. **Float name-collision quarantine — five real hits.** **Stripe was recorded
   `acquired`**; **Zebra carried Zebra Technologies' $15.5B** when Khosla's
   Zebra is Zebra Medical Vision, acquired by Nanox; **Cadre** was recorded
   public on a stale float when Yieldstreet bought it in 2023; **Teamshares**
   was disputed to private and then **the dispute was withdrawn** when two
   siblings produced a fresher cited cap; **Box** re-surfaced under a second
   slug after the rebuild and needed its own verdict.
9. **Cross-investor**: 198 shared rows — **189 agree, 9 accepted with reasons,
   0 disagree**, after aligning 17 rows and ruling 8 pairs distinct.

---

## 9. Playbook write-back (proposed)

Already landed during the run:

- **COLLECTION.md §1, T3 — sponsor promotes.** Your X1 ruling, ratcheted the
  same day as a standing precedent binding every investor.

Proposed at close, in `scripts/`:

- the four pipeline fixes in §6 above (`build-company-base.py` ×3,
  `build-firm-profile.py` ×1), all additive and all no-ops for landed bases.

Proposed for COLLECTION.md §5, as new standing lessons:

- **Read the archived per-company page BODY, not only the CDX index.** The
  Common Crawl rule already says the body is the evidence; the same is true of
  the IA replay, and on this run it produced 304 names, 279 first-party
  investment years and the firm's own sector tags that the index could not.
- **A site's own fund label is not an entry-round label.** Where a firm runs
  separate seed / main / growth funds, the card's label names the vehicle
  holding the position, and a main fund that writes from seed to Series B makes
  it unscoreable as a stage. Score it before trusting it; Khosla's went 7/15.
- **A CMS-era boundary makes a first-party date field a ceiling before it and a
  label after it.** Khosla's invest year is exact from 2011 and three years late
  before it, because the CMS was built in 2015 and the early book was entered
  retrospectively. Look for the CMS build year when a dated field misses.
- **A recall addition must be exempt from the build's own removal rules.** It
  enters only after a session verified it against a citation; two separate rules
  removed one anyway.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Thirty-six published rows carried `identity_uncertain`, and unusually for this
sweep, none of them were stale keys — Khosla's flagged set is live.

**Seventeen rows read `undetermined`.** They are the chart-era entries:
`ava`, `because`, `brt`, `dragonfly`, `fresh`, `go`, `ikoa`, `nordic`, `pax`,
`plum`, `psp`, `recapping`, `simpler`, `strut`, `sup`, `supernova`, `vert` —
a one-word or three-letter label in a single capture, with the firm's own
invest year and nothing else. Six of them had a Wikidata country attached by a
join on that bare name (Italy for BRT the parcel courier, Great Britain twice,
Ireland, Japan), which the run had already disputed; `go` is two letters.

`pax` is the one worth reading twice. The row rests on a single 2010 capture,
which predates PAX Labs taking that name — it was founded in 2007 as Ploom and
renamed in 2015 — so the $1.7B mark attached to it is a 2019-era figure for a
company this row may not be. That is precisely the failure the new rule exists
to stop, and the row now asserts nothing.

**Fifteen rows are named and lose the flag**, including three where the flag
was covering a different question entirely: `arista-networks` (a boundary
question — Arista was funded largely by Bechtolsheim and Cheriton personally,
so whether there is a venture ENTRY here is open), `himax-display` (a
membership question — a subsidiary of a listed parent on one capture) and
`yammer` (a membership question — the firm's own invest year is the year of
Microsoft's acquisition). `narrative` is the opposite case: its Swedish
country SURVIVED review because Narrative AB fits the row's own evidence, and
a confirmed identification has no business carrying a doubt flag.

**Four rows are identified with a namesake** and take `identity_homonym`:
`miso` (the social TV app, not Miso Robotics), `ori` (Ori Biotech, not the
robotic-furniture Ori), `vinci` (getvinci.ai, not Vinci SA — and the France
pre-fill came from exactly that collision, so it must not be read as
corroboration) and `evolv-on-demand` (not the public Evolv Technologies).

`verify --in-flight` clean. Khosla is mid-S2A-wave with a live in-flight
marker, so this pass did not rebuild, re-export or close; its 200 Seed rows
still owe a graduation, which is PRO-120's work.

## Addendum 2026-09-21: S2A with every Seed row decided (PRO-132)

§1 published 52.5% on a 40-row cohort of the seeds whose record could be
established. PRO-132 makes the absence of a later round a finding: a Seed row
past the 24-month clock with no evidence of a later round did not graduate,
and every no records the dated search that found nothing (the firm's archive,
the Form D sequence for a US company, at least two publisher surfaces;
COLLECTION.md §6). The 200 open rows were judged in five batches.

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 167 | 6 | 161 | 77 | 84 | 47.8% | 100% |

Of 167 seed entries, 6 were too recent to count; of the 161 that remain,
47.8% raised a later round. Of the 84 that did not, 15 rest on the filings,
22 on a cited end (an acquisition or shutdown with no round between it and
the seed) and 47 on a dated search of the named surfaces. **The stage leg is
thin on this book**: 113 of the 161 decided rows carry `stage_uncited`, the
Seed label resting on the firm's listing year and the model's reading rather
than a page naming the seed (PRO-131 (b); Erik confirmed on 2026-09-20 that a
no may rest on an uncited stage). The rate is the full seed book's, but the
book's edge is soft.

What moved:

- Re-staged out of Seed where a page names Khosla's first money at a later
  round (about 25 rows), among them Varda, Basis, Credit Genie, Cinemagram and
  Cellular Intelligence (Series A), BillGuard, Bunkerhill Health and Emergent
  (Growth), Oratomic, Rhoda, Rubedo, Split, Terra AI and Stylus Medicine
  (Series A), Factory, Loyal, Mariana Minerals and Monumental (Growth).
- In review: Shoes of Prey to Growth (Khosla's December 2015 round was the
  company's third, after a named 2012 Series A), GroupMe to Series A (the
  seed came from other investors; Khosla's money went in with the $10.6M
  round of January 2011), and Even overturned to graduated (Keith Rabois led
  its $1.5M seed for Khosla in January 2015; it raised $40M in July 2018).
- Form D verdicts overturned by named rounds: MemSQL (a $35M Series B, 2014)
  and Lumiata (a $14M Series B, 2021).
- Recognition fixes: Casca is Casca Footwear (Vancouver, acquired 2023) on
  Khosla's own archived page, not the AI-lending Casca; TrueAccord was missed
  by the surfaces as "True Accord"; Twenty is the CRM, not the Khosla-backed
  cyber company of the same name.
- Rows reading `undetermined` in the stage because nothing dates a Khosla
  entry: ten, among them Ultima Genomics, Castle, Everyone Medicines, Outsmart
  College and Pearl Bio.

`c2a_rate_max` stays at the 0.80 default. `verify` is clean.

For Erik: **Everlane** is a no on Shein's 2026 purchase, but no source dates
a priced round after Khosla's 2012 entry and the company raised little
before L Catterton; **True Link** is a no although a vendor page lists
Centana Growth Partners as a later investor (no citable round); **The Hunt**
and **Overture Life** carry Seed on entries of $10M (2014) and $21.6M (2017),
above the era's seed band; **Sakti3** graduates on Dyson's $15M strategic
investment seven months before Dyson bought it.
