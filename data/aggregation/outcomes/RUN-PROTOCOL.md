# Outcome run protocol — Sequoia Capital

The run reads the live Company Base (`company-base/<investor>.csv`) directly;
there is no pinned snapshot. Standing assumption: the base is not rebuilt for
an investor while that investor's run is in flight. `verify` reports a
violation as drift between `resolved.json` keys and base slugs.

This file is the run's constitution. If context is compacted mid-run, re-read
this file and `python3 scripts/outcome-run.py status`, then continue at the
first pending batch. Do not re-derive rules from memory.

## What is being decided per row

Two judgments, recorded as JSONL (one object per row) in
`queue/batch-NNN.out.jsonl`, then `python3 scripts/outcome-run.py record <file>`:

* **Valuation** (rows with `"valuation"` in `need`): current status and, only via
  an allowed source, a current dollar figure.
* **Graduation** (rows with `"graduation"` in `need`): the investor's entry stage
  and whether a later round followed (C2A).

**Emit only the keys for the needs asked** (plus `flags`, `note`, optional
`hq_country`). Extra keys clobber filing-grade facts at merge time. The one
exception is a deliberate dispute (below).

## Hard rules (enforced by `record`, do not fight them)

1. `status` ∈ private | public | acquired | defunct | unknown. Current-state:
   IPO'd-then-acquired → acquired. Successor-entity ambiguity → acquired + note.
2. `valuation_usd` non-null requires `valuation_source` ∈
   {sec_public_float, wikidata, unicorn_list, web_verified} AND status
   private/public. `model_knowledge` never carries a figure: if I believe a
   company is ≥$1B without a source, I claim status private, leave the figure
   null, flag `needs_web_value`, and the web pass pins it or kills it.
3. `seed_to_a_graduation` non-null requires `entry_stage: "Seed"`.
4. Acquired / defunct / unknown → `valuation_usd` null.

## Judgment rules

* **Recognition check before trust.** Before using knowledge of a name, confirm
  the row's evidence fits it: era (`first_seen`, `wayback_years`), `sector` tag,
  round sizes. A mismatch means it is a different company with the same name →
  treat as unrecognized, flag `identity_uncertain`.
* **Rule-outs are legitimate.** An unrecognized company, absent from the unicorn
  list, with small/old rounds and no recent trace, is sub-$1B with high
  probability. Recognized-dead → defunct; recognized-acquired → acquired + note
  "acq. by X, YEAR"; unrecognized-with-recent-evidence-of-life → private;
  unrecognized-and-dark → unknown + note. Notes must be specific, one line.
* **Pre-2006 legacy holdings** (Apple, Cisco, EA, Atari-era rows): entry precedes
  the base window → `entry_stage` null, graduation null, note "pre-window".
* **Confidence:** high = filing-grade or common-knowledge-stable or strong
  multi-signal rule-out. medium = recognized but facts may have moved post
  May-2026 cutoff; name-matched external list. low = genuinely uncertain → the
  claim must not publish a bucket; prefer status unknown.
* **Disputes.** When knowledge contradicts a deterministic layer (e.g. float
  series says public but the company was acquired after its last filing),
  record a classification row carrying the corrected keys + flag
  `model_disputes_source` + note. Never silently accept a value I know is wrong,
  never silently override either.
* **Layer-A assist.** If a row is recognizably a US-listed company that Layer A
  missed on a name mismatch, resolve its CIK by ticker and fetch the float
  directly (deterministic, manually keyed) rather than claiming from memory.

## Standing verification duties (after the grind, before verify-clean)

1. **Web-verify every $1B+ claim** regardless of source, including the 43
   unicorn_list matches. Confirm identity (is the base row this company?) and
   current status. Update figure + `valuation_asof` with source `web_verified`
   where the search moves it; downgrade to sub-$1B/private where it kills it.
2. **Vet Form D graduation False against reality.** A `seed_to_a_graduation:
   false` on a company that is now ≥$1B, public, or known to have raised an A is
   a Form D blind spot (4(a)(2), foreign). Dispute those to true with
   graduation_source model/web. Cross-check: no row may end
   `false` + (valuation ≥$1B or is_public).
3. **Audit every `cik_weak` row** encountered: does the matched registrant's
   float/company actually fit the row? The known false-join: base `linear` (the
   software company) ↔ LINEAR TECHNOLOGY (semiconductor, acq. Analog 2017) via
   suffix-stripped norm collision.
4. **Self-consistency:** re-classify a random 5% blind at the end; disagreements
   flagged `unstable`, adjudicated, counted in the report.

## Duplicates (18 groups, flagged, do not "fix")

Same SEC registrant under two base rows: 17 genuine renames (10Gen→MongoDB,
Evenflow→Dropbox, Square→Block, SourceForge/VA lineage, Bit9→Carbon Black,
Widgetbox→Flite, Turin→Force10, Rearden→Deem, Arbor→Hyperion, HQC→Health
Catalyst, Qadium→Expanse, Network Appliance→NetApp, Service-now.com→ServiceNow…)
plus one false join (`linear`). Rows stay flagged `duplicate`; membership is the
human's call; derivation excludes flagged rows and says so.

## Batch loop

Read 2 batches → judge every row → Write both `.out.jsonl` → `record` both →
one-line progress in chat → next pair. Progress lives on disk; `status` is the
resume point. Track nothing in context that disk already knows.

## Calibration results (measured 2026-08-11, 40 blind rows vs filing-grade key)

Status 35/40 (88%), full 34/40 (85%). Decomposition: 3 key defects caught by
model knowledge (23andme dead-but-recent-float; google stale->acquired misfire
on the Alphabet reorg; apollo false CIK join, actually Apollo.io private ~$1.6B),
1 threshold boundary (crowdstrike $109B float), 1 humble unknown on a real
micro-cap (positron), 1 open (rackspace re-IPO lineage -> web).

Added vet-pass duties:
5. Sweep every stale->acquired row for holding-co reorgs and re-IPOs (Google ->
   Alphabet CIK 1652044-style successor floats; fetch successor float directly).
6. Sweep public rows with floats 12-24 months old for known deaths (23andme).
7. Re-intersect the unicorn list with loose normalization (strip .io/.ai/.com,
   "HQ", "Labs") to catch Apollo.io-style misses.

---

# RUN 2 — 2026-08-12

Scope augmentation ordered by Erik after run 1 review:

1. **Base hygiene is upstream now.** Identity-level duplicates (renames like Square→Block,
   legal-entity aliases like ZenLeads→Apollo.io) are corrected in the Company Base itself via
   `data/aggregation/company-base/identity-merges.json`, consumed by `build-company-base.py`
   on every rebuild. Run-1 finding: flagging BOTH rows of a dup pair `duplicate` excluded the
   canonical from derivation (Block $39.4B silently dropped). New representation:
   non-canonical rows get `duplicate_of: <canonical-slug>`; canonical carries no exclusion flag.
2. **valuation_range, 100% fill.** Every row gets `valuation_range ∈ {100b_plus, 10b_plus, 1b_plus, below_1b}`
   (highest threshold met). Figures stay source-gated as in run 1; the tag may be a model
   rule-out (below_1b) but a tag ≥ 1b_plus REQUIRES a sourced valuation_usd. verify enforces.
3. **hq_country, 100% fill.** Source hierarchy (entry-time first):
   formd_address (ISSUERS.tsv STATEORCOUNTRYDESCRIPTION at earliest partner accession)
   > wikidata (P17, current HQ) > model_knowledge > web_verified. Conflicts flagged
   `country_conflict`, model may dispute a Form D Delaware-of-convenience address only with
   note. Stored as ISO 3166-1 alpha-2 (`US`, `IL`, ...); answers may say the name in prose,
   record collapses it to the code and bounces names it cannot map.
4. **entry_stage, 100% fill.** Hierarchy: formd_band (partner-anchored first round, STAGE_BANDS)
   > model_knowledge (deal history: "Sequoia led the Series A") > web_verified. Model may
   override a band ONLY with named deal knowledge + `stage_disputes_band` flag; era drift
   (a 2021 $25M "seed") is exactly what the override is for. Pre-window rows (< 2006, no
   Form D): model with confidence, first institutional round ≈ Series A convention noted.
5. **Desk feedback.** Run-1 China/India-desk findings feed the base's existing decision-desk
   rule via the overlay; moved rows land in other-desk-companies.csv, reversible in review.

Hard rules of run 1 stay in force verbatim (source-gated figures, no mid-run base
rebuilds, disk-resident progress, flags union at merge, additive layers,
verification duties 1–7).

## Run-2 batch conventions (grind #2, 692 rows / 16 batches)

- Answers merge per key into existing records; flags union; only clear_flags removes.
- hq_country: model_knowledge with confidence. Unknown-identity rows on the us-eu desk
  with no foreign marker: United States, confidence low, flag `country_prior`.
- entry_stage: named-deal knowledge overrides nothing deterministic (bands already
  resolved those rows); for era companies with no Form D and no deal memory:
  Series A, confidence low (Sequoia's classic entry), flag `stage_prior`.
  Growth for rows that first appear as later-stage positions (public-era entries,
  scaled companies at first listing).
- valuation_range: only `below_1b` may be asserted without a figure. Anything higher
  routes through needs_web_value -> web pass.
- Rename duty stays: any suspected identity duplicate -> flag + note, never silently.

---

# RUN 3 — 2026-08-12: entry_stage rebuilt from first principles

Erik's finding: Airbnb/Stripe should be Seed, HubSpot Growth (Series D 2011). Golden-set
measurement (40 documented entries): run-2 column scored 32/39 = 82%; ALL seven misses were
`formd_band` rows; model-judged rows went 24/24 on that slice. Root causes, in order of harm:

1. **Coverage blindness.** Sequoia's entry often predates the first partner-attributed
   Form D (Airbnb seed '09, Stripe seed '10 never filed). The first filing is a CEILING
   on entry recency, never a label.
2. **Ordinality blindness.** The band labeled by amount alone; HubSpot's $18.8M third
   round banded "Series A"; Block's $27.5M Series B banded "Series A" (fixed 30M cutoff).
3. **Band trusted as label.** It is a proxy, valid only for a structurally-sound first
   round (0 prior filings, company founded >= 2008 so coverage is complete, young at filing).

## New evidence order

  knowledge(high, named round + year required)            e.g. "led the 2011 Series A"
  > structural(high): 0/1/2+ prior filings + era band + age guard, coverage complete
  > knowledge(medium)
  > structural(medium)
  > band fallback (low)  — only young first-filers nobody can identify
  > stage prior (low, flagged) — unidentifiable strays only

Era-adjusted band ceilings (seed / A), by entry year: <=2010: 1.5M/12M · 2011-14: 2.5M/15M ·
2015-18: 4M/20M · 2019-21: 6M/30M · >=2022: 8M/40M. Pre-Seed = below seed/4.
Structural rules: >=2 prior filings -> Growth; 1 prior -> Series A or Growth by band;
0 prior -> band, but ONLY if year_inc >= 2008 and age at entry <= 4y, else confidence drops
and knowledge decides. Every override of a structural answer carries `stage_disputes_band`.

C2A follows the corrected column: cohort = final entry_stage == Seed; graduation for
knowledge-based seeds that predate Form D coverage may be decided by documented follow-on
(source model/web with citation), deterministic path unchanged for the rest.

## Evidence rule added after the CrowdStrike question (2026-08-13)

**A partner's personal Section 16 filing is not evidence that the firm invested.**

Forms 3/4/5 are filed by a natural person about their own holdings. A Sequoia
partner files them from board seats that have nothing to do with a Sequoia
position, in two distinct ways:

- **Ex-partner era.** Sameer Gandhi was a Sequoia partner 1998-2007, joined
  Accel in 2008, and has sat on CrowdStrike's board since 2013 *for Accel*.
  His 2019+ CrowdStrike Forms 3/4 entered our base because the entity registry
  still carries his CIK from his Sequoia years. Sequoia never invested in
  CrowdStrike (Accel, Warburg Pincus and CapitalG did).
- **Personal directorship.** Jim Goetz is a current Sequoia partner and an
  *independent* director of Intel since November 2019. Sequoia holds no Intel
  position.

The genuine signal is a **fund vehicle** on the filing (a 13D/G, or a Form 3/4
filed by the fund itself), which shows the partnership holds shares.

`build-company-base.py` therefore drops any row whose only evidence is a
Section 16 filing by a `vehicle_role == "person"` entity, with no site listing,
no Wayback capture, and no Form D partner attribution. Seven rows left:
CrowdStrike, Intel, Film Department Holdings, SpaceX's registrant duplicate,
and three Neil Shen founder positions (Ctrip, Home Inns, Molecular Data).

This is the EDGAR mirror of the Form D rule above: person-level attribution
locates a *person*, never a firm position.

## Base v2: the verification ledger (2026-08-13)

The inversion Erik ordered: publish only rows that carry sufficient evidence
AND survive an independent membership judge. MEMBERSHIP.md is the constitution;
base-verification.json is the durable ledger (verdict, who, evidence class,
basis, citation); build-company-base.py excludes not_member rows to
verification-excluded.csv; verify-company-base.py enforces full coverage.

Precision pass over 1,055 rows: 869 seeded on sufficient evidence (site
listing / fund filing), 186 name-match rows judged individually with ~16 web
arbitrations. Result: 184 not_member, 4 recovered members (Avalanche,
CloudShare fka IT Structures, Muze, Romotive), 1 uncertain. Recall pass
(parametric enumeration, fund 13D/G subject diff, European probe) found zero
missing members: the site layers carry recall, the noise was all precision.

Defect classes the judge caught that no string rule could: ex-partners filing
from their next firm (Gandhi/Accel: Quidsi, Sonatype, Lot18; Lamond/Khosla:
SeaMicro, Skybox, Seeo, Soladigm; Huang/Paradigm: Gitcoin, Rain; Garg/Wing:
Shape; Lixandru/Accel: Framer), partners who became founders (Amy Sun/
Daylight), founder homonyms (Ankur Jain/Bilt, Patrick Grady/Rearden+Tetra,
Alex Moore=8VC on Saronic/Epirus/Nylas), and Sequoia Heritage (Outside).

Base: 1,055 -> 873. Tier C: 201 -> 19. The derivation set is now the full
published base, no flag-based exclusions left. C2A moved 47.1% -> 71.7%
(33/46) because the fake seed cohort left; Pre-Seed went to zero, all of it
had been collision micro-filings.

## Classification v2 (2026-08-13): the adversarial column pass

Erik's scope: a second, more rigorous adversarial pass over valuation(+asof),
entry_stage, hq_country. Rulings: market cap is canonical for public rows
(web-cited, dated; float demoted to corroboration); below-$1B rule-outs get
signal-triggered checks plus blind sampling; the full A/B defend-attack
structure applies to the visible slice ($1B+ or public).

Executed this session: ~60 fresh web arbitrations over the visible slice.
Every public $1B+ row now carries a cited market cap. Corrections the attack
pass caught: Confluent acquired by IBM ($11B, closed 2026-03-17, delisted);
Faire's Nov-2025 tender at $5.2B, 59% below the stale $12.6B the table held;
Houzz down-bucketed below $1B (2017 mark nine years stale, secondaries sub-$1B);
Root Insurance out of the bucket ($805M cap); StarkWare's mark corrected to
the real $8B/May-2022 primary (recorded figure and date were both wrong);
Fireblocks' asof corrected to Jan 2022; Notion refreshed to the $11B Jan-2026
tender; Vanta $4.15B, Trade Republic EUR 12.5B, Verkada $5.8B, Commure $7B,
Whatnot $20B, Ramp $44B, ElevenLabs $11B, OpenEvidence $12B, Skild $14B,
Sierra $15.8B, NinjaOne $12.3B, Cyera $12B, Odoo ~EUR 7B replaced stale marks.
Armis carries a pending ServiceNow $7.75B acquisition (announced 2025-12-23),
flagged for status review. Float-to-cap moves reshaped the top: Google $4.23T,
Cisco $483B, Palo Alto $314B, Western Digital $151B, Snowflake $116B and
Airbnb $100B entered the $100B+ bucket, which now holds 15 names.

Debt made explicit rather than hidden: 29 sub-$5B private marks and 119
$1B+ stage claims carry `cite_pending` (the resumable citation queue);
all 46 C2A cohort rows carry `cohort_unverified` until their legs get
citations (Erik's keep-with-flag ruling). verify tolerates only flagged debt.
Coverage: 119/148 $1B+ rows valuation-cited (80%).
