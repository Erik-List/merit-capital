# The collection playbook

One playbook for collecting an investor's Company Base and classifying its
outcomes. It is investor-agnostic: everything specific to one investor lives
in that investor's decisions file (§1). The session running a collection
reads this file start to finish before the first batch.

**If context is compacted mid-run, re-read this file and
`python3 scripts/run.py status --investor <slug>`, then continue at the
first pending batch. Do not re-derive rules from memory.**

Everything lives investor-first under `data/collection/investors/<slug>/`;
every script takes the slug and derives its paths via `scripts/paths.py`, and
every investor-specific constant lives in the investor's `config.json`.
Starting a new investor means creating that directory with `config.json` and
`decisions.md` — nothing outside it changes.

The shape of a collection, in order:

1. Investor-specific decisions confirmed by Erik (§1), before anything runs.
2. Evidence layers collected (§5), base built.
3. Calibration gate cleared (§4), before any verdict writes.
4. Membership judged into the ledger (§2, §3); recall probe.
5. Classification grind in batches (§6, §8).
6. Adversarial A/B pass on the visible slice (§7).
7. `verify` green with only flagged debt; `export`; `review` (§9).
8. Investor classification — the firm profile (§11); independent of the
   base, runs in parallel as its own session.

## 1. Investor-specific decisions

Each investor gets one decisions file next to its base:
`data/collection/investors/<slug>/decisions.md`. The judge cites its rulings
per line; once a ruling is written there, no further approval is needed
before verdicts write. The file records:

- **Firm boundary**: which entity is "the firm" — decision desks, split-offs
  (HongShan / Peak XV), wealth or heritage arms, crossover vehicles, and
  whether the investor's fund families are one desk or several.
- **Program vehicles**: scouts, accelerator or seed programs, in or out.
- **Instruments**: primaries, secondaries, tenders, token positions.
- **Standing rulings** made during the run, dated, each one a class-wide rule
  rather than a row fix.

**The membership definition**, common to every investor: a row belongs in the
base iff a firm representative, acting on behalf of the firm, made an
investment with fund money in it, and it is a venture-outcome operating
company. Fund vehicles, SPVs, filter labels, scrape artifacts and natural
persons are out.

Two standing rules under that definition, generalized from a16z rulings
6–7 (they bind every investor unless its decisions file overrides):

- **Fund-shaped list entries**: an entry on the investor's own list whose
  name is fund-shaped (Capital / Fund / Ventures / Management, fund
  numerals) and that cannot be identified as an operating company is
  `not_member` — the LP-stake class — until evidence identifies it
  otherwise; the verdict is amended and the row returns on the next
  rebuild if identification lands. Fund-shaped names identified AS
  operating companies stay in.
- **Token positions**: a listed token position is in when it maps to an
  operating or issuing organization (a labs entity, a DAO with treasury
  and governance); a pure base-layer asset holding with no such entity is
  a treasury position, not a portfolio company, and is out. Where the
  token and its company are both listed, they are one row under the
  company.

**Evidence sufficiency**, common to every investor: a listing on the
investor's own site (any era), or an SEC filing by a fund vehicle, each
suffice alone. A Form D related-person name-match NEVER suffices alone; it
needs affirmative corroboration (documented deal, credible identification
tying the round to the firm). Absence of corroboration on a name-match is a
`not_member` verdict, not an `uncertain` one: the base asserts membership,
and an unsupported assertion is the defect class the judge exists to kill.

One adjudicated pattern above a bare name-match (a16z, 2026-08-29): a
**current partner as Director of record** on a Form D — the filing itself
lists the seat, in tenure, inside the coverage window, exact distinctive
name — is affirmative corroboration. Verdict `member` at medium confidence
as an unannounced deal (compliance lists' own permission-exclusions explain
the absence from the site), flagged for the A/B pass. The corroboration is
the seat on the filing, not the name similarity. Erik's narrowing (a16z
review, 2026-08-31; applied class-wide on Accel): the pattern holds only
when the issuer's identity RESOLVES to a real operating company —
director-only with identity never resolved and no announcement is the
personal-seat class, `not_member`.

**A seat is dated against the person's firm at filing time, not against
the roster.** Partners arrive from other firms and leave for others, and
their board seats travel with them: a roster name on a filing can be a
prior-firm deal (Accel: Jonathan Turner's e.ventures-era Cameo and Zumper
boards), a next-firm deal (Ethan Choi leading Anrok at Khosla months
after leaving), an operator job on either side of the tenure (Sagar
Sanghvi as Instacart's CFO before joining, as Abridge's CFO after), or an
interlude at another firm entirely (Carlo Biggio's Hedosophia year
between two Accel stints). The judge's question is never "is this person
ours" but "whose money was behind this seat on this date".

**A fund ownership filing can be sale consideration, not an investment**
(generalizes a16z's Starco ruling; Accel: the funds' Viggle 13G was
consideration from Viggle's acquisition of Accel-backed Wetpaint). When a
fund_filing row's company is known mainly as the ACQUIRER of a portfolio
company near the first-filing date, check the consideration reading
before seeding member — the investment row is the acquired company, which
may itself be a recall addition.

**Person-level attribution locates a person, never a firm position.** Forms
3/4/5 are filed by a natural person about their own holdings; partners file
them from personal board seats, from ex-partner years, and from their next
firm. The genuine EDGAR signal is a fund vehicle on the filing (a 13D/G, or
a Form 3/4 filed by the fund itself). The build drops any row whose only
evidence is a Section 16 filing by a person entity, with no site listing, no
Wayback capture and no Form D partner attribution. The recurring exclusion
classes: ex-partners filing from their next firm, partners' personal
directorships, partners who became founders, founder homonyms, scout checks
with no main-fund follow-on, LP positions in other funds or accelerators.

## 2. The verdict ledger

Membership verdicts are durable, in the investor's
`base-verification.json`: per slug a verdict
(`member | not_member | uncertain`), `who`, an evidence class
(`site_listing | fund_filing | formd_adjudicated | knowledge | web`), a
basis sentence and a citation where one exists. The ledger is re-applied on
every rebuild. Human verdicts (`who: "erik"`) outrank agent verdicts — and
mechanically so on the ledger: `record` refuses to overwrite them.
Classification keys carry no such guard yet (the merge is
last-writer-per-key), so a human classification correction is protected
procedurally: never re-emit a key Erik has set.
`not_member` rows leave the published base into `excluded.csv` (reason
`not_member`), preserved, never deleted; `uncertain` rows stay in the base,
marked for sampling.

`uncertain` is a narrow verdict: identification genuinely open, or evidence
in conflict, after corroboration was attempted. Missing corroboration on a
name-match is `not_member` (§1), not `uncertain` — the a16z run itself got
this wrong once (Hawthorne Labs) and only recovered under review, so before
the base is declared complete, re-sweep every `uncertain` row against this
distinction.

## 3. Judge protocol

- **Parametric memory first.** The judge decides from what it knows; web
  search is triggered, not default. Triggers: confidence below high, evidence
  is a name-match only, or the claim is $1B+ or public.
- **Recognition check before trust.** Before using knowledge of a name,
  confirm the row's evidence fits it: era (`first_seen`, filing years),
  sector tag, round sizes. A mismatch means a different company with the same
  name → treat as unrecognized, flag `identity_uncertain`.
- **Rule-outs are legitimate.** An unrecognized company, absent from the
  unicorn list, with small old rounds and no recent trace, is sub-$1B with
  high probability. Recognized-dead → defunct; recognized-acquired →
  acquired + note "acq. by X, YEAR"; unrecognized with recent evidence of
  life → private; unrecognized and dark → unknown + note. Notes specific,
  one line.
- **Null over force-fit.** Closed taxonomies report misfits as outside, not
  as the nearest bucket; an unlocatable city is null, not the investor's
  home town; a low-confidence claim must not publish a bucket, prefer status
  unknown.
- **Priors only ever flagged.** Where a prior fills a gap (US for an
  unidentifiable row on a US desk, the firm's classic entry stage for an
  unidentifiable stray) it is confidence low and carries its flag
  (`country_prior`, `stage_prior`). A prior never lands silently.
- **Disputes.** When knowledge contradicts a deterministic layer, record the
  corrected keys + flag `model_disputes_source` + note. Never silently accept
  a value known to be wrong, never silently override either.
- **Confidence:** high = filing-grade, common-knowledge-stable, or strong
  multi-signal rule-out. medium = recognized but facts may have moved past
  the knowledge cutoff; name-matched external list. low = genuinely
  uncertain.

**The recall probe.** Precision asks "is every row real"; recall asks "is
every real deal a row". After the membership pass, build an expected-member
list from sources independent of the base — parametric enumeration by era
and sector (several framings, unioned), the live site, the fund vehicles'
own 13D/G subjects, press sweeps ("<firm> leads/led" per year window) — and
diff it against the base. Every missing candidate gets the same judge
treatment (memory, then web) and lands either as a new base row with its
evidence attached, or as a recorded rejection with its reason. Probe the
structural blind spots deliberately: deals with no US filing, recent deals
not yet on the site snapshot, exits older than the archive window, stealth
rounds. Measured on Sequoia: the site layers carry recall and the probe
found zero missing members — the noise is precision-side. Expect that
shape, but run the probe anyway; it is the only check that catches it when
the shape breaks.

## 4. Calibration gate

Two measured sets, both cleared before the columns they guard may write:

- **Membership trap set** (~20 rows): ex-partner next-firm deals, homonym
  partners and founders, scout checks, LP stakes, mixed with known-true
  members across eras. Gate: zero false members at high confidence before
  any verdict writes.
- **Stage golden set** (~30–40 documented entries with named rounds and
  years). Measured blind before `entry_stage` publishes; misses are
  diagnosed and the evidence order rebuilt until the set passes. This is the
  column that fails silently when a filing band is trusted as a label
  (Sequoia: 32/39 banded, 39/39 after the rebuild in §6).

No status/valuation calibration set is required: the A/B citation pass (§7)
is what guarantees those columns.

The gate's loop, in order: **assemble the answer key first**, every answer
anchored to a citation and web-verified where uncertain — the key is
external documents, not model opinion, which is what keeps the test honest
when the same model writes and takes it. Then a **blind pass**: the golden
rows are judged through the exact production protocol, key out of context.
Then **score and decompose** — the question is not "how many right" but
"what do the misses have in common": a miss indicts a layer, and the fix is
the layer, never the instance (Sequoia: all seven stage misses were band
rows, so the band lost its authority). Scoring runs both directions — a
golden label can itself be wrong and gets corrected by the evidence. The
sets persist in the investor's `golden.json` and replay as a regression
test after any protocol change.

## 5. Evidence layers

1. **Wayback portfolio listings**, one snapshot per year per site era. The
   investor's own listings captured over time also recover companies later
   removed from the live site (survivorship correction).

   Era parsers live in `scripts/wayback-pull.py`, including two generic
   ones (`listing_regex`, `js_array_listing`) that cover most markup eras
   without new code. A logo-only era (names rendered as images) may stay
   deliberately unparsed when snapshots of another list surface bracket
   those years — record the gap in the report. If the Internet Archive
   goes down mid-run (measured on a16z: ~100 min), continue on the live
   surfaces and a provisional roster; the pulls are idempotent and
   multi-pass, so wayback lands after recovery. `wayback-pull.py` carries
   a degraded-CDX fallback (statuscode-filtered queries time out during
   outages while unfiltered ones answer).

   **Layer 1b — the site's own surfaces**, for the current portfolio that
   archives and SEC both structurally miss (JS-rendered pages defeat CDX
   enumeration; Section 4(a)(2) raises file no Form D).

   **Enumerate every list surface the firm publishes, not just the
   flagship portfolio page**: marketing-rule compliance / "investment
   list" pages (highest recall — and they declare their own exclusions;
   record those as coverage caveats), accelerator or program sites with
   their own company lists, vertical-fund sites (crypto, bio) whose rows
   appear on no other list. The base is the union (a16z: four surfaces,
   1,703-company union; 27 rows lived only on the crypto site).

   Escalation ladder per surface, in order:

   1. WordPress REST: `/wp-json/wp/v2/types` → find the post type →
      paginate it (`scripts/site-portfolio.py`).
   2. Headless-CMS query API: identify the CMS and try its public read
      endpoint before touching the rendered page — a Sanity project id
      in the page source means `<project>.api.sanity.io/.../data/query/
      production?query=<GROQ>` may serve the whole dataset (Accel: 791
      company docs with per-deal partner refs, entry-stage claims and
      exit fields; the person docs carried the team, the emeriti and the
      departed). `site-portfolio.py`'s `json_list` parser takes any such
      endpoint with a dot-path to the rows; the projection lives in the
      config URL.
   3. Next.js: the `__NEXT_DATA__` script tag, or
      `/_next/data/<build>/*.json`.
   4. Any SPA: watch XHR in the browser pane, then call that endpoint
      directly. When the pagination is client-side and the CDN strips
      the page param for direct fetches (Accel's Atoms surface:
      Finsweet cmsload on Webflow), drive the page in the browser pane,
      read the DOM, and save the rows as a `file_list` source — a local
      JSON whose `_readme` records how it was made, so the union stays
      reproducible from config.
   5. Last resort: parse what the page ships — `site-portfolio.py` has a
      generic `scrape` site_api type (parsers: `js_array`, `li_text_list`,
      `paginated_json`, `regex_list`); an embedded JS array or a
      `data-payload` attribute counts as this step, no headless render
      needed so far.

   **A CMS that names deal partners is a judge instrument, not just a
   listing.** Accel's per-company partner refs fed `partners_site` at
   build (the wayback filter path other sites use), validated identity
   merges (the Form D director matches the listed partner), and — as a
   reference graph queried per person — resolved whole common-name
   clusters at once: every "Daniel Levine" Form D row absent from the
   firm's own attribution map died in one query.

2. **Partner roster** via CDX people pages with tenure windows
   (`scripts/partner-roster.py`). When the site's people namespace mixes
   non-investors (guest authors, operations staff — a16z: 469 of 572),
   constrain the sweep roster to the site's own investing groups via
   `roster.site_team_groups` in config, and union the live CMS team in as
   current-year evidence. Known limitation, accepted and reported: a
   current-team roster cannot see deals where only a departed partner sat
   the board and no list ever carried the company; the compliance list
   carries that recall in practice.
3. **EDGAR**: the investor's vehicle registry (`scripts/edgar-entities.py`,
   one table serving role resolution, fund exclusion and lineage), issuer
   filings via the submissions API (`scripts/edgar-companies.py`), the
   Form D sweep on the roster (`scripts/formd-query.py <slug>`, targets
   derived from the roster) and issuer round histories
   (`scripts/formd-issuer-rounds.py`). One entry point runs the whole chain
   in dependency order: `python3 scripts/run.py collect <slug>` (sweep →
   entities → companies, plus the round rescan once a base exists). Layers
   1, 1b and 2 stay separate invocations: they carry judgment steps.
4. **Deterministic classification layers**: SEC XBRL public float, Wikidata,
   unicorn lists, Form D round positions. These are ceilings and
   corroboration, never labels — the first filing is a ceiling on entry
   recency, not the entry round, and a float is corroboration for a market
   cap, not the cap itself.

## 6. Classification columns

### status

`private | public | acquired | defunct | unknown`, current-state only.
IPO'd-then-acquired → acquired; successor-entity ambiguity → acquired +
note. Acquired / defunct / unknown → `valuation_usd` null.

### valuation

- **Figures are source-gated, machine-enforced.** `valuation_usd` non-null
  requires `valuation_source` ∈ {sec_public_float, wikidata, unicorn_list,
  web_verified} AND status private/public. `model_knowledge` never mints a
  figure: a company believed ≥$1B without a source is claimed private,
  figure null, flag `needs_web_value`; the web pass pins it or kills it.
- **Public rows: market capitalization is canonical**, web-cited with an
  as-of date. Float is corroboration only; a public $1B+ row without a cited
  cap fails verify.
- **Private rows**: last credible primary-round mark, `stale` flag beyond
  24 months. Secondary-market estimates go in the note, never in
  `valuation_usd`.
- **`valuation_range`** ∈ {100b_plus, 10b_plus, 1b_plus, below_1b}, highest
  threshold met, 100% fill. Only `below_1b` may be asserted without a
  figure; a tag ≥ 1b_plus requires a sourced `valuation_usd`.
- **below_1b rule-outs** are web-checked only on a signal (past unicorn
  mark, mega-raise, hot sector, recent momentum); otherwise validated by
  blind stratified sampling. Absence claims are not citeable at scale.

### entry_stage

**The stage label of the round in which the firm first put fund money into
the company.** A fact about a named historical deal, not about the company's
maturity today. 100% fill.

- Taxonomy: `Pre-Seed | Seed | Series A | Growth`. Growth = Series B and
  everything later: C/D, crossover, pre-IPO, secondaries and tenders (a
  tender entry is an entry at scale), buyout-scale positions, recaps,
  consortium structures. SAFEs and seed extensions count as Seed; the label
  follows what the firm and the record call the round, not the check size.
  Pre-2003 deals: the modern ladder does not map; the first institutional
  round is `Series A` by convention, low confidence, unless a documented
  seed exists. Re-entry after a full exit restarts the clock at the new
  round.
- **Evidence order**, strongest first:

  1. `web_verified` + `entry_stage_citation` (URL naming the round and the
     firm's participation, or the firm's own memo/company page).
  2. `formd_structural`: partner-anchored entry position with prior-filing
     count; the accessions are the citation.
  3. `model` with a named deal in the note ("led the 2011 Series A") at
     high/medium confidence.
  4. `model` at low confidence, or `stage_prior` for unidentifiable strays.

  A publication-visible claim wants class 1 or 2. Citation is attempted for
  every row, priority $1B+ (incl. IPO), then recents, then the tail;
  `stage_uncited` marks attempted failures.
- **Structural rules**: ≥2 prior filings → Growth; 1 prior → Series A or
  Growth by band; 0 prior → band, but only if the company was founded inside
  the Form D coverage window (≥2008) and was ≤4 years old at filing, else
  confidence drops and knowledge decides. Era-adjusted band ceilings
  (seed / A) by entry year: ≤2010: 1.5M/12M · 2011–14: 2.5M/15M ·
  2015–18: 4M/20M · 2019–21: 6M/30M · ≥2022: 8M/40M. Pre-Seed = below
  seed/4. Every override of a structural answer carries
  `stage_disputes_band`.
- **The first filed round is a ceiling on entry recency, not the entry.**
  Modern seeds often never file (SAFEs, 4(a)(2)), so the partner-anchored
  first filing can be a later round and the band mislabels the entry as
  Growth (a16z: Black Forest Labs — the led $31M seed never filed; the
  band read the Series B filing as a Growth entry). Before a band verdict
  publishes on a $1B+ or post-2020 row, check the firm's own announcement
  archive for a named earlier round; a found announcement is class 1 and
  overrides with `stage_disputes_band`.

### seed_to_a_graduation (C2A)

Cohort = final `entry_stage` == Seed, ≥24 months since entry or resolved
earlier (censored rows null by rule). Graduation on the deterministic path =
a later round ≥2× entry amount and ≥$5M; for knowledge-based seeds that
predate Form D coverage, a documented follow-on with citation. Cohort rows
are verified on both legs (entry stage and the A follow-on) or carry
`cohort_unverified`; the published rate is accompanied by its verified
share. Cross-check: no row may end `false` + (valuation ≥$1B or public) —
that combination is a Form D blind spot (4(a)(2), foreign), disputed to true
with source model/web.

### hq_country

ISO 3166-1 alpha-2, 100% fill. Source hierarchy, entry-time first:
`formd_address` > `wikidata` > `model_knowledge` > `web_verified`. Offshore
filing havens fall through to the next source. Conflicts flagged
`country_conflict`; a Form D Delaware-of-convenience address may be disputed
only with a note. Non-US claims on visible rows carry a citation or
formd/wikidata provenance.

### hq_city

Publishes only as the pair `hq_city` + `hq_country`; the pair must be
consistent. Current HQ for live companies, last known for dead and acquired.
Free text, but the shape is enforced: bare municipality in title case, no
state or country suffix ("Palo Alto", never "Palo Alto, CA"). Municipality,
not borough or metro (Brooklyn → New York; Mountain View is not San
Francisco); metro rollups are derived downstream and cannot be recovered
from pre-collapsed cities. Common English exonym where standard.

Evidence order: `model_knowledge` > `formd_address` > `web_verified`.
Knowledge leads, unlike `hq_country`, because the filing address is
entry-time and the column is current-HQ; the Form D address is the answer
only when the company is unrecognizable, corroboration otherwise. Its three
known defects, each a reason to override: it is entry-time (companies
move); it is sometimes counsel's, an investor's or a parent's; foreign
issuers file US offices. No city priors: an unlocatable company carries
null + `city_unknown`. Where city and country cannot both be true, flag
`city_country_conflict` + note and record the city truthfully; the country
correction stays Erik's call.

### focus

A **single primary value from the closed twelve** in
`data/taxonomy/focus.json` (the vocabulary the frontend and DB use), so the
distribution sums cleanly. A company fitting none carries `focus: null`,
reported as "outside taxonomy"; force-fitting would corrupt the
distribution. One parametric pass, web search only for unidentifiable rows;
no adversarial second pass, because a sector label publishes no number.

Judgment over the alias table where they disagree. Standing precedence
rules: **Security** wins over SaaS/DevTools/Industrial whenever security is
what the company sells (including security for developers); **Crypto &
Web3** wins over Fintech for on-chain businesses (not for companies where
crypto is a product line); consumer devices are **Consumer & Marketplaces**
even though `hardware` aliases to Industrial; healthcare vertical SaaS is
**Healthcare & Bio**, not SaaS; ad networks and audience monetization are
**Media, Gaming & Advertising** while martech sold as software stays SaaS;
**AI & Applied AI** means AI is the product, not that the company uses ML;
enterprise infrastructure and networking is **Data Infrastructure**, chips
are **Industrial & Robotics**.

## 7. Adversarial A/B pass

Applied to the **visible slice** — every row that is $1B+ or currently
public. Pass A defends each recorded value (find the confirming source);
pass B attacks it (search for the newer round, the acquisition, the down
round, the wrong stage, the relocated HQ). Agreement with citation closes
the row; disagreement is arbitrated by a targeted search; what survives goes
to the sampling sheet. Elsewhere: one rigorous cited pass, blind sampling as
the review element.

Debt is explicit, never hidden: `cite_pending` is the resumable citation
queue, `cohort_unverified` the C2A leg debt. `verify` tolerates only flagged
debt.

## 8. Run mechanics (`scripts/run.py`)

One driver: `collect` (the deterministic EDGAR chain, §5.3), `prepare` (seed
verdicts, run deterministic layers, emit the one work queue), `record`
(validate + merge a batch), `status` (coverage from disk), `verify`
(assertion suite, non-zero exit with the failing rows), `export` (the one
merged CSV, the investor's `base.csv`), `review` (the read-only review.html).
Every subcommand takes the investor slug.

- **The base is read live** from the investor's `base.json`. No pinned
  snapshot; the standing rule is that the base is not rebuilt for an
  investor while that investor's run is in flight. Overlays join on slug, so
  `verify` catches a violation as drift between overlay keys and base slugs.
- **Pre-fill is not judgment.** `prepare` does three jobs at once: seeds
  membership verdicts from evidence classes, runs the deterministic layers
  (which pre-fill `status`, stage bands, `hq_country`), and emits the work
  queue. The queue asks only about empty fields, so a deterministic
  pre-fill silently keeps the judge away from its row — the Black Forest
  Labs class: a band-labeled entry stage that was never queued for
  judgment. A `formd_band`-sourced stage on a $1B+ or post-2020 row goes
  back through the judge (with the §6 announcement check), never past it.
- **Progress lives on disk, not in context.** Batch loop: read 2 batches →
  judge every row → write both `scratch/queue/batch-NNN.out.jsonl` →
  `record` both → one-line progress in chat → next pair. `status` is the
  resume point; track nothing in context that disk already knows.
- **Run scratch lives under the investor's `scratch/`** (the queue, the
  deterministic layer files): everything there regenerates; everything at the
  investor's top level is curated or published and is never deleted by a run.
- **`record` is the gate**: it validates every line (enums, source gates,
  citation URLs, city shape, country codes) and rejects violations; answers
  merge per key into existing records; flags union; only `clear_flags`
  removes. **Emit only the keys for the needs asked** (plus `flags`, `note`)
  — extra keys clobber filing-grade facts at merge time; the one exception
  is a deliberate dispute.
- **Identity duplicates are fixed upstream**, in the investor's
  `identity-merges.json`, consumed by the base build on every
  rebuild; non-canonical rows carry `duplicate_of: <canonical-slug>`, the
  canonical carries no exclusion flag. In-run: any suspected duplicate →
  flag + note, never a silent merge. Verdicts key on slugs and merges move
  slugs: after any change to the merge file, re-check that ledger verdicts
  still attach to the intended rows — an un-merge resurrects the twin with
  its stale seed (the a16z HP/HPE case, which shipped a wrong member).
  The build applies ledger exclusions BEFORE the identity overlay, so a
  merge whose canonical is `not_member` never runs — its duplicates
  resurface as their own unjudged rows on the next rebuild (Accel:
  2tor-inc, after 2u-inc was excluded). Every slug of a merge group needs
  its own verdict when the canonical's verdict is `not_member`.
- **Standing verification duties**, after the grind, before verify-clean:
  1. Web-verify every $1B+ claim regardless of source: identity and current
     status; update or downgrade.
  2. Vet every `seed_to_a_graduation: false` against reality (the C2A
     cross-check above).
  3. Audit every weak CIK join encountered: does the registrant actually
     fit the row, or is it a suffix-stripped name collision? A weak join
     poisons downstream layers — the issuer-rounds history inherits the
     collision, so `entry_stage` and graduation must not trust a Form D
     band riding one (a16z: crypto member `dynamic` weak-joined Dynamic
     Offshore Resources and inherited a ~$1.1B "entry round").
  4. Sweep stale-float → acquired rows for holding-co reorgs and re-IPOs;
     fetch the successor float directly.
  5. Sweep public rows with floats 12–24 months old for known deaths.
  6. Re-intersect the unicorn list with loose normalization (strip
     .io/.ai/.com, "HQ", "Labs") to catch alias misses.
  7. Self-consistency: re-classify a random 5% blind at the end;
     disagreements flagged `unstable`, adjudicated, counted in the report.

## 9. Review by sampling

The review surface (the investor's `review.html`, written by
`run.py review`) is **read-only**: priority-ranked rows, evidence links, no
input widgets. Corrections arrive in chat, and each one is recorded
class-wide — as a ledger verdict or classification correction with
`who: "erik"` — so it binds every row of its class, outranks agent verdicts,
and survives every rebuild. Erik's sample sign-off is the exit criterion of
a run.

**Ingestion is gated on that sign-off** (ruled by Erik 2026-08-31, after
the a16z run ingested ahead of review): `ingest-companies.ts` and
`ingest-investor.ts` write the shared database, so they run only after
Erik explicitly approves — never as an autonomous step, even when the
issue's Done-when lists ingestion. The run ends at export + review.html +
report; the session asks for the ingest go-ahead and stops. Corrections
that land after an approved ingest are re-ingested only with a fresh
approval, and rows removed from the base after an ingest are called out
so Erik can decide the database cleanup.

Two checkpoints pace a run: the calibration gate's result, and the
membership-verified base before classification begins. At each, the session
posts a one-paragraph status and continues or waits per the issue's scope.

Before checkpoint 2 posts, the review surface is verified rendered — serve
it (`file://` is blocked in the app browser; use a static server) and check
that rows render flat and the surface is actually reviewable. It is an
exit-criterion artifact, not a byproduct.

Every run ends in the investor's `report.md`: method deltas, results,
corrections taken, the flag and debt counts behind `verify`, and the
session's prompt count (kickoff, checkpoint approvals, corrections) — the
number this pipeline exists to drive down. The prompt count is final only
after Erik's sample sign-off: review exchanges count, and a16z went from
"1 prompt, 0 corrections" at checkpoint 2 to 10 prompts and 6 rulings by
sign-off. Session recipe: the strongest available harness, web search
enabled, the machine kept awake for the grind.

**Run close includes a playbook write-back.** A rule invented during the
run that is investor-agnostic belongs in this file, not only in the
investor's `decisions.md` or the report — propose the COLLECTION.md diff
as part of closing the run. The a16z run wrote seven durable lessons into
code and local files and none into the playbook; the next investor would
have re-derived them.

## 10. Verify invariants

1. Coverage: every base slug carries a membership verdict; `status`,
   `valuation_range`, `entry_stage`, `hq_country` at 100% fill with valid
   vocabulary.
2. Source gate: a dollar figure only from an allowed source; only
   `below_1b` without a figure.
3. Public $1B+ row → cited market cap, else `cite_pending`.
4. $1B+ row → class 1/2 stage evidence (citation or filing structure), else
   `cite_pending`.
5. Cohort row → both legs verified, else `cohort_unverified`.
6. Non-US country on a visible row → citation or formd/wikidata provenance.
7. No row ends graduation `false` + (≥$1B or public).
8. Drift: overlay keys ⊆ live base slugs (the no-rebuild-mid-run rule).
9. Debt only where flagged; the flags are counted in the report.

## 11. Investor classification (the firm profile)

Independent of the base — every field here answers a question about the
firm, not its portfolio — so it runs in parallel as its own session. Output
is the investor's `investor.json` plus `investor.sources.json`, one source
entry per field; every field populated or explicitly null, through the
taxonomy gate, onto the review surface.

**Running in parallel with the base session, same investor directory**
(the a16z shape, worked): declare file ownership up front by session
message — profile session owns `investor.json` + sources sidecar, team
payloads and the fund filer sweep; base session owns `config.json`, site
companies, the EDGAR sweeps, base + overlays. Exchange intel both ways
(the profile session's measured false-attribution clusters seed the base
session's trap set). The profile may build base-less:
`build-firm-profile.py` skips its base-bound checks loudly and re-runs
them on the first post-base build — re-run it once the base lands so
notable_investments and the entry-round median recompute against the
verified base, interim assertions flagged until then.

Field recipes, learned on Sequoia and a16z:

- **AUM.** Form ADV via IAPD for any registered adviser: Item 5.F RAUM is
  the firm's own sworn number and anchors the bottom of the range; press
  supplies the top. Resolve the adviser by CRD, not name — adviser names
  drift (AH Capital Management renamed to A16Z Capital Management under
  the same CRD). An exempt reporting adviser files no Item 5.F; its
  Section 7.B private-fund gross assets are the sworn substitute. An
  affiliated but separately registered adviser (a crossover or
  public-equities arm) is excluded from both AUM and the fund list, so
  the row stays internally consistent.
- **Funds.** Sweep every Form D filer matching the firm's name on EDGAR —
  the partner-matched subset structurally misses vehicles. Sizes from
  Form D where the vehicle raised directly, from press where the size is an
  allocation; any entry carrying an accession is asserted against the
  filing at build time, and the build fails on mismatch. Post-restructure
  caveat: where LP capital enters through an evergreen vehicle, sub-funds'
  own Form Ds show only principals' money.
- **People.** The live site CMS (team post type) over the archived roster
  for current people; roles as the site presents them; socials where
  extractable from the profiles.
- **investment_range.** Three legs: the Form D entry-round distribution
  gives the median (a round-size proxy for check size — fair only for
  high-ownership lead investors, and the flag says so); program floors
  (seed-program check sizes) give the lower limit; the largest verified led
  round, cross-checked against dry powder at a 10–15% single-position
  concentration of the largest fund, gives the ceiling. Strategy
  allocations and unconfirmed aggregator claims are rejected and the
  rejections recorded in the flag.
- **notable_investments.** Recognition over the confirmed base only: the
  base decides membership, the model decides fame, the frontend cap decides
  count. The one licensed use of model memory as a source.
- **Firm-level stage, geo, scope.** From the firm's own listing filters,
  crosswalked into the taxonomies. When the portfolio distribution lands,
  reconcile: flag disagreements, never silently overwrite — a gap between
  positioning and behaviour is signal, not error.
- **Focus recompute needs representative tags.** A base-derived focus
  distribution publishes only when sector tags cover ≥25% of base rows;
  below that the tagged slice describes whichever surface carried tags,
  not the firm (a16z: only the accelerator's 251 rows carried tags, and
  the recompute had published an empty focus list). The firm's own sector
  enumeration stands until coverage clears the bar
  (`build-firm-profile.py` enforces this).
