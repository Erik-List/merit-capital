# Menlo Ventures — collection run report (PRO-91)

Run date 2026-09-06, one session, one run: Company Base, outcome classification
and firm profile under the merged shape of `../../COLLECTION.md`. Slug
`menlo-ventures`. Ingestion is gated on Erik's explicit approval and has not run.

**Usage line:** kickoff percentages were not read for this session; weekly % and
Fable % to be filled at ingest, against **599 base rows**.

**Prompt count: 1 so far** — the kickoff ("please collect menlo ventures").
The count is final only after the ingest decision.

---

## 1. What this run is

Menlo Ventures was founded on Sand Hill Road in **1976** and is by three decades
the oldest firm this project has collected. Its book runs from Dysan and Eldec in
the late 1970s to Anthropic and Lovable in 2026, and that span is the run's
defining fact: **222 of 599 rows have a first-seen year before 2006**, so the
2006 policy constant nulls `entry_stage` and `seed_to_a_graduation` on
**259 rows — 43% of the base**. That is the delta PRO-91 predicted, and it is
policy rather than debt. Every one of those rows carries an explicit
`pre_window` flag, which is new (§7 below).

---

## 2. The method delta — a site that states its own entry round

**The gate found a class-1 entry-stage layer nobody had scored before.** Menlo's
rendered portfolio cards carry a **Milestones** list in which the firm states its
own entry year and entry round — "2011 – Partnered, Series B" on Uber,
"2018 – Partnered, Series C" on Chime. 214 of the 245 listed rows carry one.

Scored blind against a 36-row key built from external documents (press for the
twelve rows where reputation is most likely wrong, the firm's own dated
announcement posts for the rest): **33 of 34 scored rows correct.** Promoted to
class 1 for the round word.

**The misses decomposed to a date, not a stage.** Five rows the layer labelled
correctly carry a year one earlier than the press announcement (Dropcam 2011 vs
Jun-2012, ConverzAI 2024 vs Feb-2025, Orb 2022 vs Mar-2023, Semgrep 2024 vs
Feb-2025). The field is the year the deal **closed**. So the layer was promoted
for the round and constrained for the date: it may set `first_seen`, it may not
be read as an announcement date, and a year disagreement with press never
overrides the round word. The one genuine miss is **Warby Parker**, where the
site says "Series B" for a 2011 partnering against a documented September-2011
Series A — its own year contradicts its own round word.

**The inversion worth carrying forward: on this firm the announcement archive
scored WORSE than the CMS field**, which is the opposite of the Creandum
finding. Three of the four apparent CMS misses were the announcement layer being
wrong. A Menlo post titled "Our Series A Investment in X" announces the round
Menlo **led**, often months or years after a quieter first cheque — proved four
times inside the run's own sources:

* **eero** — the firm's own words: *"We first invested in eero's seed round two
  years ago"* (2014). The 2016 post announcing a $50M round is the first Special
  Opportunities Fund deal, a follow-on.
* **H1** — *"In April 2020, Menlo led the Series A"*; the December post
  announcing a co-led Series B is the follow-on.
* **Goodfire** and **Numeric** — both entered at the **seed** (Aug 2024 and May
  2024), both announced only at the Series A that Menlo led.

Scoring ran in both directions, as §4 requires: **three key rows were corrected
by the evidence** (Goodfire, Numeric, Squint — the CMS was right and the key was
wrong) and one was **dropped** (Netlify: no citable statement of the entry round
survived checking, so it was judged in the grind like any other row rather than
guessed into a key; the A/B pass later found Menlo named in its 2021 Series D).

**The layer had to be plumbed to the judge.** A class-1 layer the queue item does
not carry is a layer the grind cannot use: `build-company-base.py` folded the
site's invest year into `first_seen` but dropped the round word. It now carries
`site_entry_stage` and `site_invest_year` onto the base row and into
`EVIDENCE_FIELDS`, so every queue item shows the firm's own claim. 210 items did.
Both changes are investor-agnostic and are proposed for write-back (§8).

---

## 3. Results

**`verify` is clean in full (plain) mode.**

**599 rows** — Tier A 357 (two-sourced), B 238, C 4. Evidence class: 595
`site_listing`, 4 `formd_adjudicated`.

| Column | Distribution |
|---|---|
| status | acquired 298 · private 208 · defunct 76 · public 17 |
| entry_stage | null (pre-window) 243 · Series A 193 · Growth 103 · Seed 56 · Pre-Seed 4 |
| valuation_range | below_1b 554 · 1b_plus 31 · 10b_plus 10 · 100b_plus 4 |
| hq_country | US 567 (94.7%) · IL 6 · GB 6 · SE 4 · DE 3 · CA 2 · IN/CN/TR/AU/CZ/FR/CH/HR 1 each |
| focus | Data Infrastructure 107 · Healthcare & Bio 82 · Industrial & Robotics 72 · Consumer & Marketplaces 72 · SaaS 55 · Security 53 · Fintech & Payments 50 · Media/Gaming/Advertising 50 · AI & Applied AI 26 · DevTools & APIs 24 · Crypto & Web3 4 · Climate & Energy 4 |
| C2A | cohort 36, graduated 20, **55.6%** |

**Read the shape before the numbers.** `acquired` at 50% and `defunct` at 13% is
what a fifty-year book looks like once the 1980s and 1990s have fully resolved;
no other base in this project has that much settled history. The focus
distribution has no sector above 18% — the networking, storage and semiconductor
heritage still outweighs the AI wave the firm is now all-in on, because `focus`
records what a company does and not when it was bought. And `defunct` is
undercounted by construction (§6): quiet shutdowns present as `private` or
`unknown`, so no mortality rate may be read off this column.

The **C2A rate of 55.6% on 36 cohort rows** carries its selection bias in the
sentence: of the seed entries where the record could be established, ~56%
graduated, and the establishable set skews toward visible successes. 21 of those
36 rows carry `cohort_unverified` because the follow-on leg is not verified
against a documented round.

**Sources.** Three live surfaces (the WordPress `portfolios` REST collection at
322 companies, the rendered listing's 245 detail cards, and the Getro job board
at 125), **709 distinct slugs across 20 archived years on two domains**
(menloventures.com 1998–2012, menlovc.com 2011–2026, eight configured eras), 28
EDGAR issuers from fund 13D/G and Section 16 filings, 586 Form D accessions
across 41 roster-name clusters, 369 of the firm's own announcement posts, and a
74-person roster covering 1997–2026.

---

## 4. Membership: 73 rows excluded, and why

The trap set's classes all fired. `excluded.json` holds 73 `not_member` rows:

* **Next-firm and prior-firm seats** — the largest class. Christopher Kersey left
  Menlo for Camden Partners in 2002 (Essence Group, Essia Health, LifeNexus,
  Metabolon, Paragon Bioservices, Santa Rosa, Scribes Stat, PatientSafe);
  Matt Murphy was at Kleiner Perkins until 2015 (Booyah, Datameer, GOGII,
  Ocarina, Stoke, textPlus, Cross-Platform); Venky Ganesan was at Globespan until
  2013 (Kaminario, StrongMail, Webaroo, oDesk's own filing); Rama Sekhar was at
  Norwest until 2024 (Agari, InfluxData); Sandeep Bhadra moved to Vertex in 2019
  (Hasura, Forestry.io, Tulip); Shervin Pishevar founded Sherpa in 2013
  (Brandless, Cue, Hyperloop, Social Programming Network).
* **Homonyms.** Two are almost comic and both were caught: **Matt Murphy is
  Marvell's chairman and CEO** (a $2.03B offering by a listed semiconductor
  company), and **Mark Siegel is Patterson-UTI Energy's executive chairman** (a
  Houston drilling contractor). "James Dawson" is a British Columbia mining
  geologist and accounts for Wealth Minerals, Wolverine Minerals, Kivalliq Energy
  and New Dimension Resources.
* **Partners who became founders or operators** — Matthew Kraning co-founded
  Expanse/Qadium, Adam Marchick co-founded Kahuna, Brent Dusing founded Lightside
  Games and Hexify, Jim Dawson was Fusion-io's chief sales officer, Tim Tully was
  Splunk's CTO.
* **Not operating companies.** **Curie.Bio** is described on Menlo's own listing
  as "a seed-stage venture firm and therapeutics accelerator" — an LP stake, not
  a portfolio company. **Menlo Ventures itself** appears on its own job board.
  Six rows are scrape artifacts the era parsers created: three logo filenames
  ('bi', 'chc', 'msi', 'Pro', 'Sol'), the word "Products" from page furniture,
  and a slug that is AVI Networks' own tagline rendered as a company name.

**45 identity merges** landed, in three shapes a fifty-year book produces:
renames (DriveCam→Lytx, Takipi→OverOps, Riffsy→Tenor, AnsibleWorks→Ansible,
Media6Degrees→Dstillery, Abnormal Security→Abnormal AI, SURx→Solarant,
S2io→Neterion), legal names on the filings against trading names on the site
(eShares→Carta, A Place for Rover→Rover, Social Bicycles→JUMP, Lumos
Labs→Lumosity, Vital Labs→Riva Health, Kinetic Automation→Kinetic), and **logo
filenames the 1998 era parser recovered as their own rows** (flexi→
FlexiInternational, redbrick→Red Brick Systems, MTILOGO→MicroTherapeutics).

**Two false merges were pinned apart** in `never_merge`: **Alta** (the 2023
AI style companion Menlo seeded in 2024) had been joined to **Alta Analytics**
(a 1999 listing), and **Eve** (the 2020 legal AI platform) to **eve.com** (the
1999 beauty e-tailer). Both had pulled a 2000 wayback year and a wrong status
onto a modern row. On a book this long the automatic name-variant merge is a
liability, not just a convenience.

---

## 5. Recall probe: zero missing members across four channels

* **Wikipedia insource sweep** — 82 articles, 55 already in the base, **0
  company candidates missing**.
* **Exit-side EDGAR full-text sweep** — 216 registrants, 113 third-party. Every
  apparent miss resolved to a **director biography** in a proxy statement ("Mr X
  was a partner at Menlo Ventures…") rather than a holding: VidaMed, CyOptics,
  LipoScience, Occam Networks and Pet DRx all trace to two such biographies. The
  genuine hits are the acquirers and IPO registrants of companies already in the
  base. **0 additions.**
* **The firm's own announcement archive** (369 posts) — every company named in an
  investment-announcement title is already a base row. **0 additions.**
* **Parametric enumeration by era and sector**, including a targeted sweep of the
  **Anthology Fund**: every company the firm has named from that cohort
  (OpenRouter, Clerk, Goodfire, WisdomAI, Wispr Flow, Ndea, Prime Intellect, Chai
  Discovery, Mercor, All Hands, Abacus, Turing, Accordance, Crosswise, Brellium,
  New Lantern, Alma, Astrix, BeHeard) is in the base. **0 additions.**

**The one quantified coverage gap is the firm's own non-disclosure.** The
Anthology Fund has backed **more than 60 companies** and its own quarterly
updates list roughly twenty by name; the December-2024 cohort post names 18
companies of which **seven are published as "Stealth"**. Those positions exist
and cannot be collected from any surface. This is a disclosure gap, not a
collection gap, and it is the honest ceiling on this base's recall.

---

## 6. The visible slice and the momentum slice

The adversarial A/B pass covered every row that is public or $1B+ — 45 by the close, up from the 30 the deterministic layers had marked, because the pass itself found fifteen more.

**Two catches that change published values:**

* **Clearwater Analytics was taken private and delisted on 2026-06-25** at a
  $7.36B cap. The row read `public` on an SEC float dated 2025-06-30 — exactly
  the stale-float class standing duty 5 exists to catch. Now `acquired`.
* **Anthropic's pre-fill was an aggregator figure with no priced event behind
  it.** The unicorn snapshot carried $965B; the last priced round is the $30B
  Series G that closed 2026-02-12 at a **$380B** post-money valuation. Corrected
  under Rule A, flagged `model_disputes_source`.

**nLIGHT** moved from below_1b to 1b_plus: its SEC float of $953.5M was stale and
below the band edge, and the cited cap is $2.31B.

**The momentum slice was 41 rows and found four unicorns the deterministic
layers had missed** — Dremio ($2B, 2022), Eve ($1B, Sept 2025), Wispr Flow ($2B,
Aug 2026, Menlo-led) and Typeface ($1B, 2023) — plus Netlify ($2B, 2021), where
the press named Menlo in the round and settled the entry question the calibration
key could not. The remaining rows carry a dated absence claim with
`valuation_range_source: web_verified`, so the "no $1B mark" statement carries
its date rather than being silent.

Three rows sit within 10% of a band edge and say so: **Upwork** ($1.10B),
**Typeface** ($1.00B) and **Prime Intellect** ($1.00B).

**Cross-investor (invariant 10):** 183 rows shared with sibling bases, 166 agree and 17 are accepted; **zero disagreements remain**. Before the pass, 48 disagreed.
Of the 48 disagreements, **11 were aligned on this side** (Benchling, Chai
Discovery, Enable, Everlaw, Fireworks, Function Health, Legora, Peregrine,
Signifyd, UUNET, Fab.com), **10 are ruled `distinct`** and **17 `accepted`** in
`cross-rulings.json`. The distinct rulings are the price of a fifty-year book:
Menlo's 1980s and 1990s rows carry names the 2010s and 2020s reused —
**Amplitude** (a 1998 scheduling company against Amplitude Inc), **Alloy**
(alloy.ai against alloy.com), **Axiom** (the AI mathematician against the legal
services company), **Canvas**, **Check**, **Clarify** and **Glide**.

---

## 7. Flags and debt behind a green verify

| Flag | Rows | What it means |
|---|---|---|
| `pre_window` | 259 | Entry predates 2006; `entry_stage` and graduation null **by policy**, asserted on the row rather than left empty |
| `stage_uncited` | 173 | Citation attempted for the entry round and not found |
| `stage_prior` | 122 | No round established on any surface; the firm's modal entry (Series A, 78 of 214 dated cards) applied at **low** confidence |
| `identity_uncertain` | 50 | Thin identification, mostly REST-only rows with no description and 1990s rows named only by a logo file |
| `model_disputes_source` | 42 | A deterministic pre-fill overridden with a reason on the row |
| `stale` | 26 | Private mark older than 24 months |
| `stage_disputes_band` | 23 | The site's stated round overruled a Form D band |
| `cohort_unverified` | 21 | C2A follow-on leg not verified |
| `duplicate_suspect` | 9 | Flagged for the identity file rather than merged silently |

**The honest reading of `stage_prior`:** 122 rows — 20% of the base — carry a
low-confidence prior rather than an established round. They are in-window rows
with no site milestone, no announcement and no partner-anchored Form D, almost
all of them archive-only listings from 2006–2015 that the modern CMS never
re-published. The alternative was to leave the column empty and fail the 100%
fill invariant; a flagged prior is the lesser evil, and the flag is what lets a
reader discount them.

---

## 8. Playbook write-back proposed (§9)

Six changes, all investor-agnostic, all already made in the scripts:

1. **A site that states its own entry round must reach the queue.**
   `build-company-base.py` now carries `site_entry_stage` and `site_invest_year`
   onto the base row and into `COLUMN_ORDER`; `run.py`'s `EVIDENCE_FIELDS`
   carries both into every queue item. Proposed for §5 and §8.
2. **A firm's announcement archive announces the round it LED, which is often a
   follow-on, not the entry.** Class 1 for the round it names; NOT evidence that
   the round is the entry unless the post says so in words. Proposed for §6,
   alongside the Creandum finding it inverts.
3. **A site's per-company year field is a close year, not an announcement date.**
   Proposed for §6.
4. **The pre-window null needs a flag, and `verify` must honour it.** The 2006
   policy constant and the 100%-fill invariant contradict each other on any old
   book: `verify` failed 240 legitimately-null rows. It now accepts a null
   `entry_stage` — and skips invariant 4's stage-evidence requirement — only when
   the row carries `pre_window`. Proposed for §6 and §10. **Benchmark's base
   carries 53 such rows and would fail the same way.**
5. **The one-rebuild schedule cannot land a not_member verdict made in the
   post-rebuild delta.** Two rows ruled `not_member` in the delta had nowhere to
   go; a second, final rebuild before export is needed whenever the delta grind
   produces a membership verdict. Proposed for §8.
6. ~~**CDX over plain HTTP is refused**~~ — **RETRACTED 2026-09-06.** The
   original finding was drawn from a handful of failures during an archive
   outage and misread timeouts as refusals. Re-measured deliberately (two
   8-query runs per scheme): http 14/16, https 13/16, and every single failure
   was a curl rc=28 timeout, never rc=7 connection-refused. The scheme is not
   the variable. `wayback-pull.py` and `partner-roster.py` still use HTTPS, but
   as a convention, not a fix. The real lesson, which the YC session found
   independently in `wayback-pull.py`, is that a **failed fetch must never be
   recorded as an empty year** — absence of a capture and absence of a response
   are different claims. Written to §5 in that corrected form.

7. **One site generation can carry two listing markups, and the second one
   parsed to zero.** Found 2026-09-06, after this run had closed, while checking
   the YC session's warning that a failed fetch was being read as an empty year.
   Menlo's 2002–2003 XHTML site lists companies as bare `<li>Name</li>` on
   `all_alpha` and `prior_investments` but as `<div class="company">` summary
   cards on its four sector pages. The era pattern was written from the former
   and applied to both, so eight captures that fetched cleanly (10–20 KB, correct
   titles, on disk) parsed to **zero rows and read as empty years**. The fix
   recovered **three companies no other layer could see** — Bravanta, Covalent
   Technologies and Lantern Communications, listed only in 2002–2003 and absent
   even from Prior Investments — plus fuller names for 15 existing rows, and the
   firm's own descriptions retired `identity_uncertain` on three rows and proved
   Menlo's Phiar is not YC's. The rule for §5: **a zero-row year on a page that
   returned bytes is a failed parser hypothesis, not an absence**, and it must be
   checked against the fetched page before the year is believed. See R8.

Two smaller mechanics worth recording in §5 and §8:

* **A logo-only era is recoverable from the image filename.** Menlo's 1998 sector
  pages render some companies as logos with no text; an era pattern with both a
  `(?P<slug>...)` branch on `companies/<slug>.gif` and a `(?P<name>...)` branch on
  the text recovered UUNET, FaxSav, SpectraLink, MicroTherapeutics, Latitude,
  Red Brick and a dozen more. This turns the a16z logo-era trap from a recorded
  gap into a solved one.
* **The "emit only the keys for the needs asked" rule needs its exception spelled
  out.** A deliberate dispute is licensed — and on this run 23 rows needed one,
  because a `formd_band` stage the judge overrules is by definition a key the
  queue did not ask for.

---

## 9. Open rulings for Erik

1. **The icon is the firm's campaign mark, not its logo.** The only source that
   clears the resolution and ramp rules is the 512×512 manifest icon, and it
   currently carries Menlo's 50th-anniversary **"ALL IN."** mark on its orange
   plate rather than the Menlo wordmark — because that is what the site ships as
   its own app icon today. It also needs `--allow-low-contrast` (2.58:1 against
   the 3:1 floor), the USV precedent. The site's `favicon.svg` is not a vector: it
   is a RealFaviconGenerator wrapper around a 32×32 PNG and measures a 7.01px
   ramp. **Publish the campaign mark, or wait for the firm to restore its own?**
2. **The director-of-record pattern produced four unannounced members** at medium
   confidence: **Anchore** (Douglas Carlisle, 2016–2020), **Drata** (Houman
   Haghighi, 2021), **Portfolium** (Haghighi, 2015–2017) and **InterModal Data**
   (Sandeep Bhadra, 2015). Each is a Menlo partner as Director of record on a
   Form D inside tenure with an issuer that resolves, and none appears on any
   Menlo surface. The a16z ruling admits exactly this class; these four are the
   rows it produced here.
3. **reThought Insurance is the closest call in the sweep** and was ruled OUT.
   Venky Ganesan is Director of record on the 2018 Form D and he was at Menlo by
   then — but the issuer is a Broomfield, Colorado flood-insurance MGA on no
   Menlo surface, and the firm has no insurance-underwriting position in fifty
   years of listings. Ruled `not_member` on the absence of corroboration.
4. **A second rebuild was run** to land the delta's two `not_member` verdicts,
   against §8's "exactly one rebuild is scheduled". The grind was complete and
   the alternative was publishing two rows the ledger had already excluded. The
   schedule change is proposed in §8 above.
5. **`stage_prior` at 20% of the base.** Flagged, low confidence, and reported
   here rather than hidden — but it is a fifth of the published `entry_stage`
   column and worth a decision on whether the frontend should treat a
   low-confidence prior differently from an established round.

## Addendum, 2026-09-16 — S2A re-judged under the status contract; the pre-window rows labelled

**S2A.** `seed_to_a_graduation` became a judged status (`graduated |
not_graduated | censored | undetermined`, COLLECTION.md §6), superseding the
C2A figures above. `migrate-graduation` dropped 21 legacy values and their
`cohort_unverified` flags; 51 Seed rows were re-judged (49 plus a 2-row delta,
63 web calls) with both legs cited in the same pass.

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|---|
| 45 | 7 | 6 | 32 | 23 | 9 | 71.9% | 84% |

Of 45 seed entries, 7 were too recent to count (entries of 2025–26); of the
38 whose record could be sought, 30 were established (79% coverage) and 70%
of those graduated — the establishable set skews toward visible successes.
Nine "no"s: seven on Form D absence (Handle, Librato, Mr. Number, Skeema,
Sticky, Swantide, Intermodal Data) and two on cited acquisitions with the
absence checked 2026-09-16 (Periscope, Fintool). Six rows left the cohort by
citation: Glympse (the $7.5M 2011 round was the Series B), Mog, Vidyo,
SpeedDate and Jobfox at Growth, ClearBrain at the Series A its own
Milestones name. Undetermined (8): Alcove, Anycart, Brain Jar Games, Lindy
(the A exists only on aggregator pages), Xaira (seed and A inside one launch
financing), Redfast (no round word anywhere), and **Decent and Mimic, named
Series As that fail the 2× step-up on known amounts** ($8M → $10M; $27M →
$50M) — for Erik: a ruling that a named Series A always counts would move
both to graduated. Seven further Seed rows are pre-window and carry no
graduation value by rule.

**Pre-window rows.** The 243 rows previously exported with an empty stage
now carry one (R-S2A): 211 genuinely pre-window rows with `pre_window_entry`
(Series A by the pre-2003 convention at low confidence; five judged or cited
Growth), and 32 rows that were never pre-window, re-labelled in-window with
the flag cleared (6 cited, 26 `stage_uncited`). Entry stages now Series A
408 / Growth 135 / Seed 52 / Pre-Seed 4, **no empty stage left**, so the
database's NOT NULL `entry_stage` no longer blocks this investor's first
companies ingest.

**For Erik, a membership class (T1/T4):** fourteen REST-only historical
listings are partner-carried prior-firm deals by the firm's own team pages —
AppDynamics, Puppet, DocuSign, Egnyte, DataStax, Drawbridge, SessionM,
Upstart, AutoNavi (Matt Murphy, KPCB); Smartsheet, Clearwater Analytics,
Ascentis (JP Sanday, Summit); Upwork, Exeros (Venky Ganesan, Globespan) —
with no Menlo fund named in any round. They stay members, flagged, until
ruled; four $1B+ rows among the re-labelled carry `cite_pending`. Status
notes for a later pass: ClearBrain's Amplitude acquisition closed March
2020, not 2021; Redfast was acquired by Recurly in 2025, not by Pandora in
2017; OpenRouter and Axiom have fresh priced marks above $1B.

`verify` is clean, cross-investor section included.

## Addendum, 2026-09-17 — Erik's ruling on partner-carried listings applied; base 599 → 585

Erik ruled the fourteen partner-carried prior-firm listings out (decisions.md
E1): AppDynamics, Puppet, DocuSign, Egnyte, DataStax, Drawbridge, SessionM,
Upstart, AutoNavi, Smartsheet, Clearwater Analytics, Ascentis, Upwork and
Exeros are `not_member` by human verdict, as are the two variant rows the
rebuild resurfaced (`clearwater`, `odesk-corp`). One rebuild pair later the
base is **585 rows**, 91 rows in `excluded.json`, and the fourteen names are
membership traps in `config.json`. Track record effect: DocuSign, Upstart,
Smartsheet, Clearwater Analytics, AppDynamics and Upwork were $1B+ or public
rows, so the published $1B+ count falls accordingly; the S2A block is
unchanged (none was a Seed entry). Entry stages now Series A 406 / Growth 123
/ Seed 52 / Pre-Seed 4; `cite_pending` remains only on Calix.

The rebuild also exposed a builder rule that renamed six rows by their
longest rendering; merge groups can now pin a display name and the six are
pinned (E1a). `verify` is clean except one cross-investor pair: this base
reads OverOps (formerly Takipi) as acquired, Lightspeed's row still says
private; Lightspeed's own S2A pass aligns it.

**Update, 2026-09-17 (Erik's named-round ruling).** A later round the record
names a Series A or later now graduates a row whatever the amounts, so the
two step-up casualties flagged above are decided: **Decent** graduates on the
$10M Series A led by QED (FinSMEs, 2020-09-11) and **Mimic** on the $50M
Series A co-led by GV and Menlo (SiliconAngle, 2025-02-27; Mimic Networks,
the ransomware-defence company, not the Zurich robotics firm of the same
name). The cohort becomes 32 with 23 graduated, 71.9% at 84% coverage.
Decent's `entry_date` stays the firm's own 2018 Milestones close year under
R1, not the September 2019 launch press.

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Forty-seven published rows carried `identity_uncertain`, all of them live (no
stale keys). Menlo's set splits along a line the other books do not have: the
firm's 1998-2007 pages DESCRIBED what each company did, while its modern REST
listings give a name and nothing else.

**Twenty-four rows are named and lose the flag.** The old pages carry their
own descriptions — Care Visions Corporation is "day and respite care for
children", Charlton Associates is "disk storage media", Tudor is "Tudor
Publishing - Curriculum design software" — and three rows were flagged for
what are plainly rendering defects rather than doubts: `netedge` is a logo
FILENAME for NetEdge Systems, `maven-laboatories-inc` carries the 1998 page's
own misspelling, and `influxda` is a truncated capture of InfluxData. A typo
in a capture is not an unnameable company.

**Five rows are identified with a real namesake** and take `identity_homonym`:
`cibus-pharmaceutical-inc` (not Cibus Inc, the modern CBUS), `crowdcast` (not
the later webinar product), `endgame` (not the security company Elastic
bought), `solace` (Solace Health, not Solace Systems) and `inception` (the
diffusion-LLM company — and its "acquired" pre-fill came from exactly that
collision).

**Eighteen rows read `undetermined`**, and seventeen of them are the modern
REST listings: `atta`, `barnyard-games`, `beheard`, `bluenote`, `crosswise`,
`flapping-airplanes`, `fleet-ai`, `fractal`, `kabata`, `okthx`, `questa`,
`regspot`, `scan`, `skipper`, `trove-ai`, `walden-robotics`, `workup`. Each is
a name plus a menlovc.com URL with no description, milestone or filing, and
each published a Series A that was the desk's convention rather than a round
anyone could point to. Two of them name what they are NOT — `crosswise` is not
the Israeli company Oracle bought, `questa` is not Siemens' verification tool
— and ruling a candidate out is not the same as naming the company.

The eighteenth is `presidio`, a logo filename from the 1998 healthcare page
that the run could not resolve among the Presidio Medical / Presidio
Pharmaceuticals class. It is also the case the precedence question was about:
it carries `pre_window_entry`, whose rule nulls the stage, and
`identity_unresolved`, whose rule writes `undetermined`. `undetermined` wins,
because it is the more specific statement — we do not merely decline to label
this row's stage by policy, we cannot say what company it is.

`verify --skip-cross` clean. The S2A block moves from 52 to 45 seed entries as
the undetermined rows leave the cohort; the rate reads 71.9% over 32 decided
rows.
