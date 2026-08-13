# Base v2: from filtered union to adjudicated ledger

Proposal, 2026-08-13. IMPLEMENTED same day (simplified per Erik: ledger named base-verification.json, review-decisions.json dropped for human sampling, one-line membership constitution). Results in outcome-report-run2.md section 1h and verification-sample.md. Follows Erik's direction: matching
improvements have hit their asymptote; add an independent adversarial review
loop (parametric memory + web search against the full base, plus a recall
check for missing companies), with budget for search and inference on Max 20x.

## 1. What is actually wrong (detached view)

The current build is **generative**: union three evidence streams, subtract
known-bad patterns. Every rule in the build (WRAPPER_RE, non-portfolio
industries, initial-only matches, unattributed Form D, personal Section 16,
tenure guard, pooled-fund flags) was written after a defect shipped. The three
defects Erik caught personally were of three different kinds:

| Case | Kind | Why no rule could pre-empt it |
|---|---|---|
| Block excluded from buckets | representation | flag semantics, not evidence |
| Intuit via "R Williams" | string matching | fixable by rule, and fixed |
| CrowdStrike via Gandhi | attribution semantics | a Form 4 is true evidence, about the wrong question |

The residue that no matcher can fix:

- **Full-name homonyms.** A genuine person named like a current partner, on a
  genuine filing. String rules are helpless; tenure guards pass them.
- **Attribution semantics.** Evidence that truthfully links a NAME to a
  company while saying nothing about a FIRM position (personal directorships,
  ex-partner filings, scout checks, LP relationships).
- **Membership edge classes.** Scout-fund deals, Sequoia Heritage, SCGE
  crossover positions, secondaries/tenders, accelerator LP stakes. These are
  definitional questions; the pipeline currently has no place to write the
  definition down.

Also a self-critique: the outcome runs repeatedly *classified* symptoms of
non-membership instead of challenging membership. 63 `stage_prior` rows, 49
`country_prior` rows, and thirty "collision near-certain" notes were each a
per-row shrug where the right move was an adversarial membership question. The
surgery-centre cluster should have triggered this proposal months earlier.

## 2. The inversion

**From** "include unless a rule excludes"
**to** "publish only rows that carry a sufficient evidence class AND survive an
independent judge; every exclusion and inclusion is a recorded verdict."

Concretely, a new durable artifact beside the base:

```
data/aggregation/company-base/membership-ledger.json
{
  "<slug>": {
    "verdict": "member" | "not_member" | "uncertain",
    "who": "agent-precision-pass-1" | "agent-recall-pass-1" | "erik",
    "evidence_class": "site_listing" | "fund_filing" | "formd_adjudicated"
                      | "knowledge" | "web",
    "basis": "one sentence with the decisive fact",
    "citation": "url or filing accession, when web/filing based",
    "confidence": "high" | "medium" | "low",
    "decided": "2026-08-13"
  }, ...
}
```

The ledger is the third durable overlay, sitting with `review-decisions.json`
(human) and `identity-merges.json` (identity). The build consumes it exactly
like the other two: re-applied on every rebuild, human verdicts outrank agent
verdicts, nothing silently deleted (excluded rows go to a partition file with
their verdict attached).

`verify-company-base.py` gains the closing invariants:

1. Every published row has a ledger verdict of `member`.
2. Every `member` verdict cites a sufficient evidence class. Sufficient means:
   site listing (any era, artifact-checked), a filing by a FUND vehicle, or a
   Form D partner attribution that the judge affirmed. A bare name-match is
   never sufficient on its own.
3. No `uncertain` verdict older than one rebuild without a review flag.

## 3. The membership constitution (phase 0, needs Erik)

Most remaining errors are definitional. Before any judging, write
`MEMBERSHIP.md` with one ruling per edge class. Proposed defaults:

| Edge class | Default ruling | Rationale |
|---|---|---|
| Scout-fund checks | **out**, unless a main fund followed | site never lists them; not a firm decision |
| Sequoia Heritage | out | endowment vehicle, not the venture firm |
| SCGE (global equities) | out for public-market buys, **in** for pre-IPO privates it led | matches how the site lists |
| Secondaries / tenders by main funds | in | a real position (Stripe 2024) |
| Pure public-market 13G by a fund | out, flagged separately | not venture activity |
| Accelerator/LP stakes (YC, funds-of-funds) | out (already rejected) | LP money is not a portfolio company |
| Partner personal directorships | out (rule shipped 2026-08-13) | person, not firm |
| Pre-split China/India deals on the US site | desk partition (already) | decision-desk rule |

Erik approves or amends each line; the judge cites the constitution by line in
its `basis` when an edge class decides a verdict.

## 4. The two loops

### 4a. Precision loop (adversarial pass over every row)

For each of the ~1,055 published rows plus a 100-row sample of already-filtered
rows (to test the filters themselves, both directions):

1. **Memory first.** The judge answers from parametric knowledge: "Is <name>
   (<sector>, <era>, <evidence summary>) a company the Sequoia US/EU venture
   funds invested in?" Verdict + confidence + one-sentence basis.
2. **Web when it matters.** Mandatory search when: confidence below high, OR
   the row's only evidence is Form D name-matching, OR value_tag >= 1b_plus,
   OR the judge affirms against a filter. Search targets: funding press,
   Sequoia's own memos/site, Crunchbase-shape footprints, the partner's actual
   board history for homonym checks ("is it plausible THIS partner sat on THIS
   board" is answerable: sector fit, era fit, known board load).
3. Verdicts append to the ledger through a validating `record` step (the
   outcome-run pattern: schema-checked at the door, additive, restartable).

Expected volume: ~700 rows resolve from memory at high confidence (famous
companies and clean site-era rows), ~350-400 need one to three searches. Call
it 500-700 searches total. Fine on the stated budget.

### 4b. Recall loop (what is missing)

Build an **expected-member list** from sources independent of the base:

1. Parametric enumeration by era and sector ("Sequoia US investments
   1972-1995, 1995-2005, 2005-2015, 2015-2026", run several framings, union).
2. Sequoia's live site today (already scraped, trivially diffable).
3. The fund vehicles' own 13D/G subjects (already in the EDGAR layer; any
   subject missing from the base is a candidate by construction).
4. Targeted web sweeps: "Sequoia leads/led" press archives per year window,
   Wikipedia's Sequoia category, partner board lists from bios.

Diff against the base. Each missing candidate gets the same judge treatment
(memory, then web), then lands either as a new base row WITH its evidence
attached, or in a `recall-rejected.json` with the reason (China desk, scout,
Heritage, rumor-only). Known blind spots to probe deliberately: European deals
with no Form D and no US filing, 2025-26 deals not yet on the site snapshot,
pre-2006 exits older than the Wayback window, stealth companies.

### 4c. Reconciliation (the actually-adversarial part)

Run the precision judge **twice with opposed priors**: pass A is memory-first
("assume the pipeline was right, look for reasons to doubt"), pass B is
skeptic-first ("assume Tier C rows are noise, look for proof of membership").
Agreement at high confidence closes the row. Disagreement or double-uncertain
routes to a small web-arbitration queue, and what survives THAT goes to Erik
in a review surface (the investor-review keyboard pattern, j/k/confirm/reject,
exporting straight into the ledger as human verdicts).

## 5. Claude workflows (how it runs)

Recommended shape: a **driver script + headless Claude invocations**, same
disk-resident pattern as the outcome runs, because it is restartable,
verifiable at the door, and model-agnostic:

- `scripts/membership-review.py prepare` emits judge batches (50 rows each,
  with evidence summaries and the constitution inlined).
- Each batch runs as a `claude -p` invocation (or Agent SDK task) with
  WebSearch enabled, returning verdict JSONL; `record` validates and appends.
- Passes A and B are just different system prompts over the same batches; they
  can run as parallel subagent fan-outs since each batch is self-contained.
- A `status` command reports coverage; `verify` enforces the §2 invariants.
- Drift: a monthly scheduled run re-judges rows whose evidence changed (new
  filings, site diffs) and re-runs the recall loop quarterly. This is where a
  scheduled cloud agent (routine) fits naturally.

In-session autonomous runs (like runs 1-3) remain the right tool for the
first execution, where judgment calls and protocol amendments are frequent.
The scripted workflow is for repetition, other investors, and drift.

## 6. Measurement before trust

Golden membership set, ~60 rows, before the sweep touches the base:

- ~40 known-true across eras and edge classes (Apple, Tandem era; Google,
  PayPal era; WhatsApp, Stripe era; Klarna, Wiz for non-US; a secondary
  position; an SCGE private).
- ~20 known-false lookalikes: CrowdStrike, Intel, Intuit, Amgen, DocuSign,
  a surgery-centre LLC, a China-desk deal, a scout deal, Y Combinator.

Judge must clear a bar (target: zero false-members at high confidence, recall
above 90% on known-trues) before its verdicts write to the ledger. Same
calibration discipline as the stage rerun, where measuring first (32/39)
correctly indicted the band layer instead of the model layer.

## 7. What this buys per investor going forward

The Sequoia base was built investor-first and generalizes: the constitution,
ledger schema, judge prompts, and driver are investor-agnostic. For the next
investor the sequence is: evidence layers (existing scripts), then the two
loops, then human review of the contested tail. The expensive part (judge
inference and search) scales with base size, not with code.

## 8. Costs and order

| Phase | What | Rough cost |
|---|---|---|
| 0 | MEMBERSHIP.md constitution, Erik approves | one review |
| 1 | Golden set + judge calibration | ~40 searches |
| 2 | Precision pass A+B over 1,055 + filter sample | ~500-700 searches, hours of inference |
| 3 | Recall loop + arbitration | ~150-250 searches |
| 4 | Ledger wired into build + verify invariants | code only |
| 5 | Review surface for the contested tail, Erik adjudicates | UI exists to adapt |
| 6 | Scheduled drift runs | routine setup |

Phases 1-4 are one long autonomous session in the established pattern.
