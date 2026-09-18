# Battery Ventures — collection run report

**Linear issue** PRO-97 (sub-issue of the PRO-87 wave umbrella) · **slug**
`battery-ventures` · run closed **2026-09-07** · one session, one run, under
the merged shape of `data/collection/COLLECTION.md`.

---

## Results

| | |
|---|---|
| **Published base** | **658 companies** |
| Tiers | A 599 (91%) · B 56 · C 3 |
| Excluded, preserved in `excluded.json` | **336** |
| Membership verdicts on the ledger | 1,081 · 0 uncertain |
| `entry_stage` | Growth 320 · Series A 227 · Seed 105 · Pre-Seed 6 — 100% fill |
| `status` | acquired 371 · private 181 · defunct 72 · public 26 · unknown 8 |
| `hq_country` | US 555 (84%) · Israel 52 (8%) · UK 14 · Canada 12 · Germany 5 · France 4 · India 4 |
| `hq_city` | 522/658 filled, 171 distinct |
| `focus` | 100% fill: SaaS 184 · Data Infrastructure 164 · Consumer & Marketplaces 81 · Industrial & Robotics 51 · Fintech & Payments 50 · Security 34 · AI & Applied AI 32 · DevTools & APIs 25 · Healthcare & Bio 18 · Media/Gaming/Advertising 10 · Climate & Energy 6 · Crypto & Web3 3 |
| Visible slice | 36 rows at $1B+, of which 10 at $10B+ and 1 at $100B+ |
| C2A cohort | 22 rows, 10 graduated, 45.5% |
| Era span | 1997 (the earliest archived listing) back to founding-era positions; 182 rows are pre-window |

`verify` is **green in plain mode** with only flagged debt. The only
outstanding assertions are the wave-level cross-investor invariant (below).

## The delta this run was written for: control positions

PRO-97 called this "the wave's hardest Phase 0 question", and it resolved as a
**derivation, not a delta** — both addenda it turns on (T1's strategy-desk
partition and T3's control test) are standing rules Erik confirmed on
2026-09-04, so applying them to Battery's facts needed no new ruling.

**T1 does not partition Battery.** The strategy addendum resolves the desk
*per vehicle, by CRD or CIK*. Battery has one adviser — **Battery Management
Corp., CRD 160921**, an active RIA d/b/a Battery Ventures, with BMC UK
Subadvisor Support Ltd and Battery Ventures Israel Ltd as **relying**
advisers — and its Form ADV's Schedule D lists **60 private funds** with no
buyout-only, growth-only or credit vehicle among them. One flagship family
(Ventures VIII–XV, the paired Side Funds, Select I–II) writes seed cheques,
growth rounds and control buyouts alike. So `desks.partition` is empty and,
contrary to the issue's hopeful reading, the control test was **not** made
rare by a desk partition — it carried the whole question.

**T3 removed 124 rows.** They are: Battery's Buyout-labelled platforms and
their constituent add-ons (AnalytiChem, Alogent, AdaCore, Forterro, Vero,
CAMBRIO, Rogue Wave, DomainTools, LightBox, PPT Group, Nova Instruments and
Metrix, Process Sensing, SPT Labtech, ORTEC, PageUp, Qognify, Learnosity,
Newforma, LI-COR, MadCap, Signiant, Smartling, Syndigo, TrueContext, Xplor,
Clubessential, CrunchTime, Craftview, Cenevo, Velaris, Vercore, Vetspire,
Shiftmove, StoneEagle, ResourceWise, RetailNext, Tech Soft 3D, Plixer,
Reliability Won, conrizon and the rest); the **Freescale** and **Sabre**
consortium LBOs; the **Internet Brands**, **EASY SOFTWARE**, **TrueContext**
and **Quovadx** take-privates; **Made2Manage**, which Battery's own Forterro
case study calls "the firm's first-ever buyout transaction in 2003"; and two
rows the firm's own site labels **Growth** —

> **WebPT**: "In 2014, Battery partnered with the company, acquiring a portion
> of the founders' shares for a **majority stake** in the business."
> **Brightree**: "Battery partnered with the management team and **acquired
> the founder's shares for a majority stake** in the company."

Those two are the reason the control test could not be confined to the 71
Buyout-labelled rows, and they were caught on the calibration gate before the
grind rather than in it (R2, R5).

**Venture and control shares, as the issue asked for them.** Of the 351
companies Battery lists on its portfolio surface, the firm labels **Early 152,
Growth 127, Buyout 71**. After adjudication the published base keeps **two**
Buyout-labelled rows — Cortera and Axiometrix — because the evidence shows a
minority financing rather than a control acquisition, and loses two
Growth-labelled ones. The base is **658 venture rows against 124 control
rows**: the firm's venture activity is roughly **84%** of what it publishes,
and the excluded 16% is preserved and reversible.

**The profile says so.** `investor/sources.json` carries a `base_boundary`
field stating in plain words that the published base covers Battery's
minority venture activity while `aum` and `funds` cover the whole adviser.
That asymmetry is unavoidable here and is not the §1 shape it resembles:
there is no parent and no child desk, one adviser manages one fund family, and
**no venture-only RAUM exists to report**. Without the sentence the base would
read as the firm's entire track record, which it is not.

## Escalation raised (PRO-97 named it in advance)

**`control_position` is still not emitted by `build-company-base.py`.** The
build hard-codes three exclusion reasons — `build_filter`, `other_desk`,
`not_member`. COLLECTION.md §1 specifies a fourth. PRO-97 said that if it were
still absent this is a §9 escalation to raise once rather than a workaround to
improvise, and §12 reserves `scripts/` for the tooling session while siblings
are in flight, so the run did not add it.

What it did instead (R1): every control row is a ledger `not_member` whose
basis sentence opens **"control position:"**. That is lossless for counting
and for this report — the 124 rows are exactly recoverable with one filter —
and lossy only in `excluded.json`'s reason column, which reads `not_member`
for all 336 excluded rows. Re-labelling them once the build emits the code is
a one-line change.

## Method deltas and what they cost

**Both capture archives were down at once (R3).** On 2026-09-06 the Internet
Archive refused every CDX query and Common Crawl's `collinfo.json` returned
empty replies. This is the first run to lose both. Two of the archive's three
jobs did not need replacing — survivorship correction was already covered by a
live first-party surface, and corroboration landed once the replay path
recovered (19 years, 1,021 slugs). The third, the historical roster, had no
substitute, so the run **invented one**: Battery's own fund vehicles' Form D
`relatedPersonsList` entries, dated by filing, plus the co-filer partner CIKs
in `entities.json` dated **only** by the Battery filings they appear on. The
roster went 133 → **144 people with 11 dated departures**, recovering
founders and GPs the live site no longer lists, and the Form D sweep grew from
723 accessions on 133 names to **930 across 436 issuers**.

**A co-filing window is a floor, and reading it as a departure date deletes
members (R4).** The first build removed 11 rows on ex-partner evidence, 8 of
them on "Mark Sherman last on site 2008" — a window that came from the two
Battery filings he happened to co-sign. Sherman was a GP from **2000 to
2010**; Oliver Curme from **1985 to 2005**. With web-verified windows the rule
removes **31** rows instead, and every one is a next-firm seat the floor had
been hiding: Todd Dagres's post-2005 filings are **Spark Capital** deals
(1stdibs, Freight Farms, Covestor — Spark is already collected, so these would
have been cross-investor contradictions), and Brian O'Malley's post-2014 ones
are **Forerunner** deals.

**Wikidata is wrong 28% of the time on this book (R6).** `prepare` filled
`hq_country` on 98 rows from Wikidata; 73 of them have single-token names.
Front→JP, Olo→FI, Marco Polo→MA, Cask→GB, Coram→NL, Cube→DE, Plain→NL,
Taster→JP, Terminal→EE, Trip.com→CN, Cross River Bank→IL, Carta→NL, Sage→PL,
N.E.T.→CZ — plus three rows carrying the footnoted prose string
`"Israel /  United States"`, which is not a country code. The failure is
silent by construction: the queue asks only about EMPTY fields. Battery
publishes its own Location per company, so that layer was **promoted to class
1** and re-judged **330 rows** (23 overriding a wrong pre-fill); `hq_city`
went from 51 to 370 filled on that one pass.

**Two classification lines for one slug do not merge (R7).** `record` reads a
file into a dict keyed by slug, so the second line replaces the first before
any per-key merge. Seven rows lost their `status` and `valuation_range` that
way — every one a row where a band dispute was written as its own line.
COLLECTION.md §8 currently reads as if splitting were safe, because it is safe
for the neighbouring case (a member needs a verdict line *and* a
classification line).

**A Black-Forest-Labs-class defect, caught before it bit.** `rename` creates
`site_entry_stage` on the raw row, but only keys listed in `extras` reach the
merged row — so the firm's own stage label was reaching neither the base nor
the queue. Fixed before the grind; it now carries on 328 queue items.

## The calibration gate (R5)

Scored against a 34-row key anchored to Battery's own case-study posts, before
any `entry_stage` wrote. **The gate's finding is that one field is three
layers:**

| Layer | Score | Verdict |
|---|---|---|
| `INVESTED` year | **34/34 exact** | class 1 for the entry YEAR (a close year) |
| STAGE = `Buyout` | **8/8 control** | class 1 **control trigger**, not a stage label |
| STAGE = `Growth` | **15/17** (both misses control) | class 1 for "Growth **or** control"; never Seed/Series A |
| STAGE = `Early` | **0/8** | **refused as a label**; corroboration only |

`Early` is the result that mattered. Behind those eight rows the key holds
Seed (HotelTonight), Series A (StreamSets, Guardicore, Gainsight) **and
Growth** — Coupa's Series B, BlueKai's Series B, Glassdoor's Series C, Habana
Labs' Series B. It is Battery's strategy bucket describing the company when it
was listed, not the round the firm entered: the Accel *socure* class exactly.
Every `Early` row therefore reached the judge with the round unresolved.

The membership trap set (22 rows) behaved as designed: 12 of the 15
`not_member` traps never became base rows at all, removed structurally by the
ex-partner tenure rule and the personal-Section-16 rule, and all 7 known-true
members were present at tier A.

**Honesty note.** The layer scoring is the load-bearing result and is anchored
to external first-party documents. The judge-side **blind** pass is not
claimed: this session wrote the key and cannot take the test blind in the same
context. What the gate delivered here is §4's other and larger job — deciding
the evidence order the grind would use, rather than auditing one it had used.

## Evidence layers

- **The marketing-rule compliance list** (`/list-of-all-companies/`) is the
  find of the run: **679 entries headed "All investments as of Q1 2026" with
  no declared exclusions**, roughly double the 351-row portfolio surface, and
  the only surface carrying the 1980s–90s book (@Stake, Concord Data Systems,
  CONXUS, Fore Systems, Cullinet). Its legend defines a trailing `*` as
  "Denotes an exited investment", which is first-party exit status on 473
  rows. It publishes **registered** names, which is how a couple of dozen
  renames surfaced for free (eShares→Carta, APIHub→Clearbit, Appboy→Braze,
  Continuuity→Cask, Smooth-Stone→Calxeda, SmarterRemarketer→SmarterHQ,
  Blockscore→Cognito, JRSK→Away, Rizio→Voicera, Buildscale→Vidyard).
- **Per-company detail pages** (351), carrying the firm's own sector tags,
  **INVESTED** year, free-text status, location, Early/Growth/Buyout stage and
  the per-deal Battery Team. Neither the WordPress REST API nor the `/company/`
  index exposes them — the Yoast `company-sitemap.xml` does.
- **52 case studies**, which supplied the calibration key at zero search cost
  and are the reason the stage layer could be scored against first-party
  documents rather than model opinion.
- **Wayback**, 19 years across five site generations: the 1997 FrontPage
  sector page, the 2004–2012 alphabetical view whose second column is the
  *prior*-holdings list, the 2013–2020 logo wall, and the compliance list
  2021–2026 in **three different markups** (`<br/>` runs, a `<tr><td>` table,
  and `<p><span>`).
- **EDGAR**: 85 entities, 930 Form D accessions across 436 issuers, 42
  ownership-filing companies, and an exit-side full-text sweep returning 666
  registrants.
- **Wikipedia insource**: 107 articles, 24 company candidates.

## Recall probe: zero missing members

The Wikipedia sweep's 24 candidates are all either already in the base or are
acquirer, parent, ranking-list or personal-investment noise — MV Agusta is
Oliver Curme's own money and is out under T2; ThousandEyes appears only
because Battery *ranked* it. A parametric enumeration of **463 names across
six eras** found 13 apparent gaps, every one the same company under a longer
rendering (HNC/HNC Software, Akamai/Akamai Technologies, cVidya/cVidya
Networks, Cbeyond/Cbeyond Com).

That result is a property of this investor rather than a triumph of method:
Battery publishes a complete first-party investment list, so the site layers
carry recall almost entirely. It also decided the membership sweep — all 156
Form D name-match rows carried **no Battery surface of any kind**, and on a
firm that publishes everything, that absence is decisive.

## The A/B pass

Corrections found on the visible slice, each cited:

- **Confluent is `acquired`, not public** — IBM bought it and it delisted
  2026-03-17. The row read public on a $0 float.
- **Coinbase** read `below_1b` on a $0 SEC float; market cap **$48.09B**.
- **Guidewire** read `below_1b` on a $0 float; **$13.52B**.
- **Databricks**: the $190B pre-fill was not a priced event. The last
  **closed** round is the $5B Series L at **$134B** (Feb 2026); the $188B
  strategic round is being raised, which §6 refuses to price a row from.
- **ClickHouse** $2B → **$15B** on the January-2026 Series D.
- **Wayfair**, **JFrog** and **MaxLinear** each moved up a band on stale floats.
- Two float **name-collisions** struck (duty 8): RADNET Ltd. (Israeli, 1990s)
  carried RadNet Inc.'s $4.1B; Imara carried the Boston biotech's $836M.

## Debt, all flagged and counted

| Flag | Rows | What it means |
|---|---|---|
| `stage_uncited` | 539 | entry stage from knowledge, no URL. Heavy by construction: 182 rows are pre-window and most of the rest are 1990s–2000s companies with no surviving announcement. |
| `pre_window` | 182 | entries before the 2006 window; stage carried at low confidence, graduation null |
| `city_unknown` | 93 | no municipality could be established; the pair is left null rather than guessed |
| `identity_uncertain` | 53 | compliance-list-only rows whose identity is genuinely open |
| `country_prior` / `stage_prior` | 47 / 46 | prior-filled and flagged, never silent |
| `model_disputes_source` | 33 | a deterministic value overruled with a reason |
| `possible_duplicate` | 31 | flagged, not silently merged |
| `needs_web_value` | 24 | believed above $1B without a priced event (Rule A) |
| `cite_pending` | 18 | the resumable citation queue |
| `stage_disputes_band` | 13 | a Form D band overruled by the record |

## Open rulings for Erik

1. **The control boundary itself.** 124 rows leave the base on a rule Erik has
   already confirmed, applied here for the first time. The numbers are above
   so the call is cheap to reverse. Two specific rows are the ones worth a
   second look, and both are argued in the ledger rather than assumed:
   **Zayo Group** (labelled Buyout, but a 2007 company *formation* Battery
   helped fund and grow by acquisition, not a control acquisition of an
   existing business — kept **in**) and **RAE Systems** (a 2011 take-private
   in which Battery was the minority partner to Vector Capital's control
   position — kept **in**).
2. **`control_position` reason code** — the §9 escalation above.
3. **The `unify` row conflates two companies.** first_seen 1997 is Unify
   Corporation, the 1990s database vendor on Battery's own portfolio page;
   INVESTED 2025 with Dharmesh Thakker's Form D is Unify, the 2023-founded AI
   go-to-market company. The identity overlay merges, it does not split, so
   the row is flagged rather than fixed.
4. **The scope gap.** The profile publishes four focus labels because the
   recompute reads the firm's own tags (280 of 658 rows) at the 30-company
   threshold. **Security** (34 rows) and **AI & Applied AI** (32) clear it on
   the graded focus column and Battery demonstrably invests in both. §11 says
   to leave that gap as signal rather than close it by hand, so it is flagged
   in the sidecar.
5. **Cross-investor invariant 10**: 183 shared rows, 140 agree, **43
   disagree**, and three siblings (accel, greylock, yc) were in flight and not
   compared. Several were resolved in the A/B pass by taking a fresh figure
   (ClickHouse, JFrog, Wayfair now match their siblings). The rest belong to
   the wave-level alignment pass, which §12 runs once after every session in
   the wave closes — not to this run.

## Playbook write-back proposed

Diffs to `COLLECTION.md`, offered as the last act of the run:

1. **§8** — one classification line per slug per file (R7). The section
   currently reads as if splitting were safe.
2. **§5** — the *compliance investment list* deserves its own entry beside the
   a16z one: where a firm publishes a complete dated list with no declared
   exclusions, it is the highest-recall surface **and** it settles the
   membership question for uncorroborated name-matches, because absence from
   it is evidence. Also: such a list publishes REGISTERED names, which is a
   free rename-detector, and it may share markup with the page's cookie-consent
   table — 51 rows of this base were cookie names and descriptions before they
   were ruled out.
3. **§5** — the fund-vehicle Form D `relatedPersonsList` as a roster layer for
   an archive outage (R3), and the rule that a co-filing window is a floor
   (R4).
4. **§1 / PRO-87** — the control-position experience: the T1 strategy addendum
   only bites where a separate VEHICLE exists, so on a one-fund firm the whole
   question falls to T3; and a firm's own strategy label is a trigger for the
   control test, never its answer, in both directions.

## Usage line

Not recorded. §12 asks for the account's weekly and Fable percentages read
before kickoff and at close; this session did not take the kickoff reading, so
no cost-per-company figure can be given for this run. Flagged so the next
session in the wave takes it.

## Prompt count

**2** at close — the kickoff and one "continue". The ingest approval will make
it 3.

## Addendum 2026-09-17 — S2A re-judged under the status contract

`seed_to_a_graduation` became a judged status (COLLECTION.md §6). All 105
in-window Seed rows were judged with both legs cited.

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|---|
| 86 | 2 | 47 | 37 | 15 | 22 | 40.5% | 44% |

Of 86 seed entries, 2 were too recent to count; of the 84 whose record could
be sought, 37 were established (44% coverage) and 40.5% of those graduated.
**This is the only book in the wave where "no" is the majority verdict** —
22 of 37 decided rows did not raise again — and it is the clearest evidence
that the old instrument was measuring visibility rather than outcome: the
same base previously published a far higher figure on an unverified cohort.

Nineteen rows left the cohort (fifteen to Series A, four to Growth under R5),
and one Form D verdict was overturned under the named-round ruling. The 47
undetermined are largely a membership problem wearing an S2A label:
seventeen are compliance-list names with no identifiable company and twenty
are small dead companies with neither a citable round nor a citable terminal
event.

Eight cross-investor pairs were resolved in the same pass, three by
correcting this base and three by correcting the sibling, with two ruled
distinct; details in D-S2A. A backlog of 32 further pairs against Greylock,
Menlo and others remains, surfaced as those siblings closed their runs, and
is a valuation/status job rather than an S2A one.
