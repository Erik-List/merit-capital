# The collection playbook

One playbook for collecting an investor: its Company Base, the outcome
classification of every member, and the firm profile — **one run, one
session, one Linear issue per investor**. It is investor-agnostic:
everything specific to one investor lives in that investor's decisions file
(§1). The session running a collection reads this file start to finish
before the first batch.

**If context is compacted mid-run, re-read this file and
`python3 scripts/run.py status --investor <slug>`, then continue at the
first pending batch. Do not re-derive rules from memory.**

Everything lives investor-first under `data/collection/investors/<slug>/`;
every script takes the slug and derives its paths via `scripts/paths.py`, and
every investor-specific constant lives in the investor's `config.json`.
Starting a new investor means creating that directory with `config.json` and
`decisions.md` — nothing outside it changes.

The shape of a collection, in order:

1. Investor-specific decisions derived from the standing rule set, plus
   the confirmed deltas (§1).
2. Evidence layers collected (§5), base built.
3. **Both** calibration sets — membership traps and stage golden set —
   assembled, pre-registered and cleared (§4), before any verdict writes.
4. One grind (§3, §6, §8): every queued row answered for membership and,
   where it is a member, for every open classification column, in the
   same pass.
5. Recall probe (§3); additions judged; **one** rebuild; one re-prepare
   for the delta.
6. Standing verification duties (§8) and the adversarial A/B pass (§7).
7. Firm profile built once, against the landed base (§11).
8. `verify` green with only flagged debt; `export`; `review`; `report.md`;
   playbook write-back (§9).
9. One message to Erik: results, open rulings, the ingest request (§9).

Until 2026-09-03 a collection was two issues and two sessions — the base,
then classification — separated by a blocking sample sign-off. The
tooling never split (one queue, one `record`, one CSV), both Accel and
Lightspeed reported the resume pointer dead for the whole base run, rows
were judged twice off the same evidence, and Erik reviewed the same rows
twice, the first time with placeholder classification columns. The
merged shape is the fix; the Lightspeed run (PRO-63/66) was the last of
the old shape.

## 1. Investor-specific decisions

Each investor gets one decisions file next to its base:
`data/collection/investors/<slug>/decisions.md`. The judge cites its rulings
per line; once a ruling is written there, no further approval is needed
before verdicts write. The file is not a restatement of the standing rules
below — it is their **derivation** for this investor's facts, plus the
**deltas** those rules do not cover (the derivation protocol, below).

**The membership definition**, common to every investor: a row belongs in the
base iff a firm representative, acting on behalf of the firm, made an
investment with fund money in it, and it is a venture-outcome operating
company. Fund vehicles, SPVs, filter labels, scrape artifacts and natural
persons are out.

### The standing rule set

Read as a corpus, the rulings confirmed across the first five investors
(Sequoia, a16z, Accel, Lightspeed, Thrive) are five tests applied to each
investor's facts. The tests are the standing rules. They bind every
investor, and a new investor's decisions file **derives** its boundary from
them instead of re-asking them. Each test carries its precedents with the
facts that decided them, so a case that does not fit is visible as a delta
rather than stretched to fit. Provenance is marked where a precedent was an
agent's flagged ruling or a generalization made here rather than a
confirmed ruling.

- **T1 — Same adviser.** Is the vehicle under the firm's own adviser
  registration and operation? Default IN for every fund family, sleeve
  (growth, opportunity, continuity, select, co-invest, the lettered and
  single-name vehicles) and office of the one adviser or its relying and
  affiliated advisers; OUT for a brand-sharing entity with its own RIA or
  ERA, its own fund family, or its own disclosure of independent
  operation. IN: a16z's crypto / bio / games / American Dynamism families
  under one adviser; Accel's US, London and India desks (relying adviser
  plus affiliated ERAs); LSVP's US, Europe and Israel offices under CRD
  160187; Thrive's umbrella with its relying adviser, Growth and
  Opportunity sleeves, lettered LLCs and Claremount vehicles; Creandum's
  flagship, Select and SPV vehicles under four ERAs, one of them the
  AIFM; YC Continuity as the firm's own growth fund (Erik, 2026-09-04).
  OUT: HongShan and Peak XV (separate firms since 2023); Accel-KKR (own
  RIA); IDG-Accel China (historical JV, independent successor); Meritech
  (independently operated affiliate; agent, flagged); Lightspeed India
  (own ERA and the firm's own "not a unitary enterprise" disclosure);
  Lightspeed China (independent partnership since 2011); Lightspeed
  Faction (own RIA).
- **T2 — Fund money.** Did a fund of the firm hold the position? Default
  IN where it did, whatever the program or channel; OUT where the only
  connection is a person, a program listing or an association. IN:
  Sequoia Arc, a16z speedrun, Accel Atoms per cohort company where Accel
  money was deployed, Thrive incubations including pre-spin-out ones
  where a fund held the position. OUT: scout checks with no main-fund
  follow-on (ruled on Sequoia, a16z, Accel and Lightspeed); Lightspeed's
  Extreme Entrepreneurs (no funding); partners' personal angel books
  (Kushner; Cherry's founder-angel positions, Erik 2026-09-04);
  Erasmic-era India deals with no Accel listing (agent, flagged);
  companies founded by the firm's alumni that no fund backed
  (generalized here from the definition, unruled).
- **T3 — Venture entry.** Did the position enter through a venture round
  — a primary, a secondary or a tender in a private company? Default IN
  for primaries, follow-ons, secondaries and tenders (a tender entry is an
  entry at scale, Growth by taxonomy: Thrive's Figma, Creandum's Klarna);
  OUT for positions that first appear as public-market purchases, 13F
  holdings or post-IPO 13Gs, and for vehicles that make no venture rounds
  at all. OUT: post-RIA public or secondary purchases (Lightspeed,
  Thrive; generalized 2026-09-03, in full below); Sequoia Heritage and
  the crossover vehicles' public buys; Thrive Holdings (buy-and-build
  holdco) and Thrive Eternal (permanent capital for sports and cultural
  assets). Open: Accel's arista, a 13G-only holding with no documented
  pre-IPO round, awaiting Erik's ruling.
- **T4 — Person or firm.** Whose money sat behind the seat on that date?
  A filing by a natural person locates the person, never a firm position,
  and a seat is dated against the person's firm at filing time. The full
  rules are the evidence rules below: person-level attribution, seat
  dating, the director-of-record pattern and its narrowing.
- **T5 — Operating company.** Is the row a venture-outcome operating
  company at all? Fund vehicles, SPVs, feeders, continuation vehicles,
  fund-shaped list entries, tokens with no issuing organization, filter
  labels, scrape artifacts and natural persons are not rows. Positions
  moved through plumbing stay rows through their original entries, and a
  new commitment made through such a vehicle enters at that stage
  (Lightspeed's Project Mercury; Creandum's Select funds and SPV TR as
  follow-ons, entry stage unchanged); third-party feeders into a fund are
  external (Thrive IX Access; agent, flagged). The fund-shaped and token
  rules below are this test in full.

**Policy constants**, ruled once and changed only by Erik, never derived:
the base window opens 2006 (earlier entries are pre-window, entry_stage
and graduation null); secondaries and tenders are Growth entries; a
private mark is `stale` beyond 24 months; the profile's geo core carries
at most two labels; a non-USD figure converts to USD at the ECB reference
rate of its own date, and a listing outside SEC registration takes a
web-cited market cap (both ruled on Creandum, Erik 2026-09-04; mechanics
in §6 valuation).

### The derivation protocol

Until 2026-09-04 every investor's Phase 0 restated the categories above
and Erik confirmed the whole set each time; of the five Cherry rulings
confirmed that day, none was a decision — all were T1–T3 applied to
facts. The inverted protocol: derive, and confirm only the delta.

A new investor's decisions file has three parts, and only the second
needs Erik before kickoff:

1. **Derivations** — one line per category: the facts found, the test
   applied, the outcome, the precedent. No confirmation is needed. They
   are listed in the Linear issue so Erik sees them and can veto any one
   before kickoff; silence means they apply.
2. **Deltas** — rulings no test covers, facts that satisfy two tests with
   opposite outcomes, or a proposed exception to a standing rule for this
   investor, argued. Erik confirms these, and only these, before kickoff.
3. **Run-time standing rulings** made during the run, dated, each one a
   class-wide rule rather than a row fix, flagged for review — as before.

A derivation needs both a named test and verified facts. Where the facts
are still model priors, the derivation is provisional and is re-derived
at kickoff from the verified facts; where either the test or the facts
are missing, the item is a delta, not a derivation. **A wrong fact
re-derives under the same test**, recorded in the file and reported —
facts flip derivations mechanically, they do not reopen rulings. Only a
re-derivation that is not clean, or facts outside every test, escalates
(§9 trigger 1).

**Confirmed deltas ratchet the same day.** A delta that is
investor-agnostic is written into this section once confirmed — as a
precedent under its test, or as a policy constant — before the run, not
at close (§9's write-back is for method; decisions ratchet earlier
because the next investor's issue is usually written before the previous
run closes). What stays Erik's: new categories, test collisions, argued
exceptions, changes to the policy constants, and the four §9 triggers.

### Standing rules in full

Three standing rules under the membership definition, generalized from
a16z rulings 6–7 and Lightspeed ruling 7; T3 and T5 above index them. They
bind every investor, and an investor's file departs from them only through
a confirmed delta:

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
- **Post-RIA public or secondary purchases with no venture entry** (a
  position that first appears as a 13F holding or a post-IPO 13G, never
  through a venture round) are `not_member` — crossover treasury, not
  portfolio membership. A row that entered through a venture round stays
  in after it goes public. Erik confirmed the Lightspeed and Thrive
  instances 2026-08-31; generalized 2026-09-03. Accel's arista (13G-only,
  no documented pre-IPO round, shipped as a member) is the open case
  under the earlier per-investor treatment and is raised for Erik's
  ruling, not re-judged.

### Evidence rules

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
may itself be a recall addition. The same reading applies to the firm's own site
(Creandum: Elastic listed as a commitment from the month Elastic bought
Creandum-seeded Opbeat, held through the IPO) — a site listing suffices
for membership, but a site-listed acquirer of a portfolio company is
checked for consideration before it seeds member (agent, flagged).

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
Classification keys carry the same guard in `record`: an agent record may
add keys to a `who: "erik"` row but never overwrite or unflag the keys the
human set. Belt and braces: never re-emit a key Erik has set.
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

**Name-match rows are judged cluster-first, not row-first.** A Form D
name-match queue is a list of people, not companies: resolve the person
once — tenure window, prior and next firms, operator jobs, founder-era
paper — then sweep every row that person explains against the decisions
file. Lightspeed judged 273 name-match rows as 75 clusters; three homonyms
alone ("Mark Anderson", "John Thompson", "Paul Murphy") accounted for 94
rows, and each cluster lived or died in one ruling. Where the site names
deal partners (§5), the attribution map is the cluster's reference graph.

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

Two measured sets, both assembled, pre-registered (keys committed before
the base build) and cleared before the grind starts — the single grind
writes verdicts and `entry_stage` in the same pass, so both keys exist
before either column may write:

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

**The gate calibrates layers, not only the judge.** Score every candidate
evidence layer for the guarded column against the key, and promote or
demote it by its score before the grind trusts it. Measured on Accel: the
firm's own CMS entry-stage label scored 30/31 and was promoted to class 1;
the Form D band scored 5/13 and was demoted to a ceiling. A layer that was
never scored is not a label. This is what the stage set is for when it
runs before the grind rather than after the base: it decides the evidence
order the grind will use, instead of auditing one it already used.

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

   Three rules measured on Lightspeed: **the firm's early site may live
   on another domain entirely** — an era entry carries its own
   `cdx_domain` / `site_url_base` (lightspeedvp.com 2000–2012 while
   lsvp.com sat parked on a squatter page; an empty archive under the
   current domain is not a coverage gap until the old domain is
   checked). **Parsed year files merge across capture universes**
   (keyed slug+path): the IA pull and the Common Crawl pull write the
   same per-year shape from different capture sets, and each must
   survive the other's re-runs. **When CDX refuses but replay answers**
   (the 2026-09 partial outage: connection-refused CDX, working
   replay), year-targeted replay redirects fetched into wayback-pull's
   own raw/parsed shapes — true snapshot timestamps recovered from the
   rewritten URLs — keep the layer moving and converge with the
   eventual CDX pull. Measured again on Creandum (2026-09-04, CDX refused every query for
   the whole run): the replay path alone landed 22 years across six eras.
   Three mechanics it needed, now in `wayback-pull.py`: **a per-era
   snapshot memo** (`raw/<era>.snapshots.json`), so a throttled probe
   (429) never re-asks for a year it already resolved and a known capture
   timestamp can be seeded by hand when the probe's nearest capture is
   the wrong era; **gzip-stored captures** (replay serves some captures as
   stored gzip bytes — the puller sniffs the magic and inflates before
   parsing, and JS payloads are written byte-safe); and **0-byte files
   from a throttled probe are deleted, never parsed**.

   **Layer 1a — Common Crawl**, the second capture archive
   (`scripts/commoncrawl-pull.py`, configured by `commoncrawl.company_paths`
   and `people_paths`; omitting the block silently disables the layer). It
   serves the wayback layer's two jobs — survivorship correction and roster
   tenure — from an independent capture set, and it carried Accel through
   a full-run Internet Archive outage (the third measured outage across
   runs). It writes the same per-year parsed shape as `wayback-pull.py`,
   so the IA pull converges over it on recovery. Five rules, each paid for
   on Accel:

   - **Serial pacing only.** CC throttles parallel clients into silent
     empties; the script paces one request at a time and stores explicit
     no-captures markers so a resume skips what was genuinely empty.
   - **Catch-all shells are filtered by body digest.** accel.com in 2018
     served one identical body for any `/companies/<slug>`; 453 junk
     captures of crawler-invented slugs (adobe, amazon) shared one digest
     and were dropped. A capture enumeration without this filter invents
     members.
   - **Read the WARC body, not only the index.** A page can be served,
     captured and pulled within weeks (Accel: Corsa, "(ACCEL INVESTMENT) /
     Seed-Series A" in a May-2026 body, a 404 by run time, absent from
     the CMS) — the body is the evidence.
   - **Capture-year tenure windows are roster evidence.** People-page
     captures give per-person first and last years that matched known
     departures exactly (Breyer 2014–2016, Lixandru 2017–2019); Accel's
     roster tripled from 69 to 217 names and the Form D re-sweep grew from
     689 to 1,086 accessions on that alone.
   - **The site's own rendering owns name and slug.** A capture slug never
     names a row (a capture-created row was publishing "Assemblyai");
     namespace junk (`all`, `see-all`, `<slug>-2`) is configured out in
     `wayback.non_company_slugs`.

   Two things captures decide that no other layer can. **A CMS "archived"
   or "unpublished" flag is not a verdict**: archived docs with years of
   captures were real listings and are members (Accel: Snorkel AI, Cogsy,
   Youshd, Names & Faces); archived docs with zero captures were never
   published and are correctly out (SentinelOne, Synopsys, Amino). And
   **the capture layer is an identity-merge instrument**: pre-rename page
   captures read ten Accel merges directly (CureFit→Cult.fit,
   MemSQL→SingleStore, WorldRemit→Zepz, MessageBird→Bird, UserLeap→Sprig)
   plus three CMS-slug artifacts (brds = Bird Scooters, saltpay = Teya).
   The measurable payoff is tier: capture corroboration is what makes a
   site row two-sourced (Accel: 142 → 776 Tier A).

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

   **A shared-brand site's own attribution can be newer than its
   archives** (Lightspeed: the per-card lsvp/lsip firm attribute
   postdates the January-2026 snapshot, so archived cards render the
   sister firm's rows with home-domain links — 61 of 65 boundary rows
   built base rows on captures alone). Where the live site attributes
   rows to a sister firm, archived listing years from that surface are
   not, alone, home-firm listing evidence; membership resolves by the
   current attribution plus independent vehicle or partner evidence,
   recorded as a standing ruling in the investor's decisions file.

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
   3b. Nuxt full-static (Creandum): `/_nuxt/static/<build>/<route>/
      payload.js`, a `__NUXT_JSONP__` call whose argument is a cyclic
      object graph; the build id comes from `staticAssetsBase` in the
      page source or, failing that, the preload links. `site-portfolio.py`'s
      `nuxt_payload` parser decodes the graph with `$ref` markers and
      walks `list_path` (the rows sit under `data.data.0`), flattening
      Contentful entries; `wayback-pull.py`'s `nuxt_payload_listing` era
      reads the archived builds the same way with build ids pinned per
      year in config. Creandum's payload carried the firm's own investment
      date, lead partner, sector and exit flag per row, and the whole blog
      with related-company links — the richest single surface any run has
      had.
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
   1, 1a, 1b and 2 stay separate invocations: they carry judgment steps.

   Two registry rules. **Explicit `external` desk patterns run as the first
   classify rule** (`desks.classify[0]` in config: namesakes, independently
   operated affiliates such as Accel-KKR and Meritech, partners' personal
   entities), so a namesake that shares the firm's name pattern is caught
   before the home-desk rule can claim it. And **a cofiler-closure entity's
   own filing address can re-desk it, and reach back before the roster
   window**: Lightspeed's LS SPV Management and Venture Investors General
   Partner LLC both surfaced as `external`, and both file Forms 3/4 from
   2200 Sand Hill Road; the GP entity has filed since 2006 and carries the
   pre-2012 board seats the 2012+ roster window structurally misses.
4. **Deterministic classification layers**: SEC XBRL public float, Wikidata,
   unicorn lists, Form D round positions. These are ceilings and
   corroboration, never labels — and the unicorn snapshot is a
   coverage floor, not a census: the Wikipedia list (shared/unicorns,
   pulled 2026-08-23) omitted Augustus a month after its $1B round and
   carries companies under their current names only, so a renamed
   member (Ivy → Augustus) never matches. Re-pull it at run start,
   match on every merged name, and treat its absence as no evidence — the first filing is a ceiling on entry
   recency, not the entry round, and a float is corroboration for a market
   cap, not the cap itself.

**When the investor publishes no list at all** (measured on Thrive,
2026-09-03, the first merged run): the `site_listing` class is not empty,
it moves. The firm's job board (Getro/Consider: `jobs.<domain>`) is a
first-party company list — enumerate it from its sitemap plus the
per-company pages (`site_api` with one `file_list` source), and never take
its stage field as a label (0/10 on the gate). The roster is curated from
the ADV, Form D related persons and press with press-dated tenure windows
(one ruling per name, §1), and the roster-name Form D sweep becomes the
primary structural layer. The ADV Section 7.B fund roster is membership
evidence for named-deal vehicles ("… Partners IV Stripe, LLC"). Press
sweeps run as a primary layer: every press-evidenced row lands as cited
`web`, and the recall probe's parametric enumeration is load-bearing (37
of 155 rows). Expect the base to be small and winner-heavy — the
fund-vehicle and press layers surface the companies that made news — and
say so in the report rather than reading it as a defect (§8, `verify.shape`).
Check the Wayback and Common Crawl eras before concluding no list ever
existed; on Thrive none did (2010–2026), and that is recorded, not assumed.

**Two recall layers run before the recall probe, disclosing site or not**
(built on Thrive's post-close delta, 2026-09-03, which found 15 misses on
a 155-row base): the **exit-side EDGAR sweep** (`scripts/edgar-fts-sweep.py`,
`edgar.fts_phrases`) — full-text search on the fund-entity phrases, hits
aggregated by third-party registrant, own entities / LP-side registered
funds / ownership forms separated, the primary document's sentences kept
as evidence. IPO S-1s file the investors' rights agreement with every fund
signatory, 424B and S-3 resale prospectuses list selling stockholders of
any size, acquirers' S-3/S-4/8-K schedules list target holders, Regulation
A statements list holders; all filing-grade (`fund_filing`). And the
**Wikipedia insource sweep** (`scripts/wikipedia-insource.py`,
`wikipedia.phrases`) — every article whose source names the firm, with the
naming sentences, company articles separated from people and lists; the
judge cites the article and its underlying reference (`web`). Both need
the noise read once per investor (place names, leases, namesake typos)
and a `not_member` verdict for every candidate ruled out, so the layer's
next run is a delta.

**When the investor sits outside the SEC** (measured on Creandum,
2026-09-04, the EU thin-data test): the SEC layer is fund-side only, not
empty. The firm's own vehicles still file Form D (eleven Creandum
vehicles: a Guernsey L.P., Swedish (D)/(E) AB pairs, Select funds, a
single-company SPV) and its exempt reporting advisers file Form ADV, whose
Section 7.B gross asset values are the AUM anchor and the fund list's
existence corroboration; issuer-side ownership filings do not exist, and
the roster-name Form D sweep reaches only the US-incorporated members
(7 of 177) while still removing ex-partner clusters through the tenure
rule. What replaces Form D is the firm's own record read in depth — the
CMS with its dates, partners and exit flags, every archived listing era
(the 2003–2016 book survived only there), and the announcement archive
scored as a class-1 layer on the gate — plus the exit-side EDGAR
full-text sweep, which works for any firm whose winners exit into US
listings. The EU registers (Bolagsverket via allabolag.se, the
Finansinspektionen AIFM register, Companies House) give the entity set
and the manager's authorisation, filing-grade for the boundary ruling
and the profile, and zero membership evidence — record that negative
result rather than hide it (`sources/registers/entities.json`). The
deterministic classification layers shrink to near nothing (2 structural
stages, 6 unicorn pre-fills, one float), so the A/B pass carries the
whole visible slice and the search budget is sized for it (~78 searches
on 177 rows).

## 6. Classification columns

### status

`private | public | acquired | defunct | unknown`, current-state only.
IPO'd-then-acquired → acquired; successor-entity ambiguity → acquired +
note. Acquired / defunct / unknown → `valuation_usd` null.

A merger that folds the company into an acquirer is `acquired` from the
closing even when its last primary mark is fresher than the deal (xAI's
Jan-2026 $230B round, then the Feb-2026 all-stock absorption into SpaceX):
the standalone value no longer exists and survives only inside the
acquirer's own row where that acquirer is held (Sequoia's SpaceX row). The
Lightspeed run kept xAI private at $230B with the merger in its own note;
the other two runs holding xAI had already retired it. A subsidiary that
was never acquired but sells priced primary rounds to outside investors
(Waymo, an Alphabet unit since the 2016 spin-out) is `private` with that
mark: there was no acquisition event to retire the value.

**Whichever surface supplies status covers only its own rows.** A site CMS
carries status for listed rows and nothing for members that entered
through filings, captures or recall; the grind authors status for every
layer-only member or the column ships with holes (Accel's close-out audit
found 105 such rows with no status at all). The firm's own status field
also goes stale, and the base overrides it with the cited event
(Lightspeed carried Wiz as `acquired` while the site still said Private).
**`defunct` is undercounted by construction** (Accel 3.3%): quiet
shutdowns present as `private` or `unknown`, acquihires as `acquired`. The
column answers "last known state", not survivorship; no mortality rate may
be read off it, and the report says so.

### valuation

- **Figures are source-gated, machine-enforced.** `valuation_usd` non-null
  requires `valuation_source` ∈ {sec_public_float, wikidata, unicorn_list,
  web_verified} AND status private/public. `model_knowledge` never mints a
  figure: a company believed ≥$1B without a source is claimed private,
  figure null, flag `needs_web_value`; the web pass pins it or kills it.
- **Public rows: market capitalization is canonical**, web-cited with an
  as-of date. Float is corroboration only; a public $1B+ row without a cited
  cap fails verify.
- **Non-USD figures convert at the ECB reference rate of their own date**
  (ruled on Creandum, Erik 2026-09-04; a §1 policy constant binding every
  investor): a round size, a private mark or a market cap quoted in EUR,
  SEK, DKK, NOK, GBP, CHF or any other ECB reference currency converts at
  the euro reference rate in force on the figure's date — the announcement
  date for a round or mark, the as-of date for a cap — cross-rated through
  EUR, via `scripts/fx-convert.py` (ECB Data Portal, keyless, cached under
  `data/collection/shared/fx/`). The note keeps the original figure,
  currency, rate and rate date in the helper's form ("EUR 1.00B @ ECB
  2025-06-30 (EUR/USD 1.172) = $1.17B"); a weekend or holiday takes the
  last published rate before it and the note names the date used. A press
  USD figure for a non-USD round is accepted only where the press converted
  at the time; an undated figure converts at the month-end of its period.
  Bands are assigned on the converted figure, and a figure within 5% of a
  band edge is noted as such. Conversion does not change
  `valuation_source` — the mark's own source class carries.
- **Listings outside SEC registration take a web-cited market cap** (ruled
  on Creandum, Erik 2026-09-04; binds every investor): `sec_public_float`
  does not exist for Nasdaq Stockholm, First North, Oslo Børs, Euronext,
  LSE or Deutsche Börse listings, so the row carries no float
  corroboration and is pinned by cap like every other public row —
  `valuation_source: web_verified`, the citation from the exchange's own
  quote page or a market-cap aggregator the landed runs already cite
  (companiesmarketcap.com, stockanalysis.com, Google or Yahoo Finance), the
  local-currency cap converted under the rule above at the as-of date and
  recorded in the note. A US-listed foreign private issuer (Spotify's 20-F)
  keeps the shared SEC float layer where it exists.
- **Private rows**: last credible primary-round mark, `stale` flag beyond
  24 months. Secondary-market estimates go in the note, never in
  `valuation_usd`.
- **A stale primary mark yields to documented collapse evidence**: a priced
  tender or secondary far below it, or the sale of the business's core,
  rules the row into the lower band with the evidence cited in the note
  (Faire's Nov-2025 tender 59% under its 2022 mark; Lookout's ~$296M
  secondaries after the consumer-business sale against a 2014 $1B round).
  Without such evidence the last primary stands, `stale`-flagged; a
  figure is still never minted from the evidence itself. Read the
  same way on Creandum (agent, flagged for Erik): a lead investor's
  published fair-value marks a third under the last primary (Voi: VNV
  Global's $611M–$656M in 2025 against the 2021 $1B), and a restructuring
  followed by a small round at an undisclosed price (Pipe: the $16M 2026
  round after founder exits and a CEO change, against the 2021 $2B).
- **A $0 or pre-listing SEC float is not a value.** A public row whose
  float is zero, or measured before its listing (a first 10-K dating the
  float to the pre-IPO quarter end: Netskope, IPO Sep 2025, float "as of"
  Jul 2025 = $0), takes `needs_web_value` and is pinned by market cap. It
  never settles into `below_1b` on the float alone.
- **`valuation_range`** ∈ {100b_plus, 10b_plus, 1b_plus, below_1b}, highest
  threshold met, 100% fill. Only `below_1b` may be asserted without a
  figure; a tag ≥ 1b_plus requires a sourced `valuation_usd`.
- **below_1b rule-outs** are web-checked only on a signal (past unicorn
  mark, mega-raise, hot sector, recent momentum); otherwise validated by
  blind stratified sampling. Absence claims are not citeable at scale. **The signal is computed, not noticed** (Erik's correction on
  Creandum, 2026-09-04): Augustus (ex-Ivy) closed a $180M Series B at
  $1B on 2026-07-21 and the run published it `below_1b` — the raise
  postdated the judge's knowledge, the Wikipedia unicorn snapshot did
  not carry it, the rename defeated any name match, and the row showed
  no trigger in its evidence pack because the firm posted nothing about
  the round. So the **momentum slice** is mechanical: every private row
  with `first_seen` inside the last five years in a hot sector (AI &
  Applied AI, Fintech & Payments, Data Infrastructure, DevTools & APIs)
  gets one web check in the A/B pass, and the check is recorded on the
  row (`valuation_range_source: web_verified` with the citation, even
  for a below_1b result), so an absence claim carries its date. On
  Creandum that slice was 39 rows of which 5 had been checked; size the
  search budget for it up front.

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
- **The firm's own stage label is class 1 on early rounds and fails on
  late at-scale entries.** Score it on the gate (§4) before trusting it;
  where it passes it is class 1 — but a CMS that says "seed" or "Series A"
  for a company the firm demonstrably entered at B or later is describing
  the company when it was listed, not the deal (Accel: 17 rows, the socure
  class). Precedence: **the label follows the record** — a documented
  entry round at scale overrides the site's label, flagged
  `stage_disputes_band` with the citation.
- **"The firm led the A" folklore fails one-directionally on famous
  rows.** Accel's citation pass corrected 12 stages and ten went Series A
  → Growth (Personio: Northzone led the A, Accel entered at the $75M C;
  Netskope, PagerDuty, Trade Republic, Sennder, BlaBlaCar, Doctolib, G2
  likewise). Reputation is not evidence: the entry round of every famous
  row is cited, and the firm's own dated company or relationship pages
  are the first place to look.

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

The published rate carries its selection bias in the sentence, not in a
footnote: knowledge-true graduations are easier to author than confirmed
non-graduations, and nulls hide the undetermined. The honest form (Accel,
79.1% on 91 rows): "of the seed entries where the record could be
established, ~79% graduated — the establishable set skews toward visible
successes."

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
- **One queue, one pass per row.** `prepare` emits every open need for a
  row in one item — `membership` first when the row is unjudged, then
  whichever of `status`, `hq_country`, `entry_stage`, `valuation_range`
  the deterministic layers left empty — and carries the row's evidence
  (`evidence_class`, site, wayback, EDGAR and Form D links, partner
  attribution) so the judge rules membership from the item alone. The
  judge answers membership first: a `not_member` row gets its verdict line
  and nothing else; a member gets the verdict line plus one classification
  line, in the same `.out.jsonl`. `record` routes the two kinds by the
  presence of `verdict`. Rows already ruled `not_member` are retired from
  the queue on the next `prepare` and leave `base.json` at the rebuild.
- **Progress lives on disk, not in context.** Batch loop: read 2 batches →
  judge every row → write both `scratch/queue/batch-NNN.out.jsonl` →
  `record` both → one-line progress in chat → next pair. `status` is the
  resume point and counts **per slug and per need** against
  `scratch/queue/queue.json` (a membership-only item completes on its
  verdict; a `not_member` row completes outright); batch files are a
  chunking that `prepare` regenerates and renumbers freely, so never hold
  a batch number in context that disk already knows.
- **Exactly one rebuild is scheduled**, after the recall probe. The
  standing rule that the base is not rebuilt mid-run still holds; the
  rebuild is the one step that moves `not_member` rows into `excluded.csv`
  and lands recall additions. After it, one `prepare` re-emits the delta
  (new rows, and any need still open) and the grind finishes it.
  Rebuilding at any other point costs a re-prepare and a renumbered queue
  for nothing.
- **`verify --in-flight` is the mid-run check**; plain `verify` is the
  contract at the end (§10). In flight every answered row is held to the
  full consistency, source-gate and citation contract, while unjudged
  rows, unfilled columns and `not_member` rows awaiting the rebuild are
  counted and reported rather than failed. A red `--in-flight` mid-grind
  is a defect in what has been answered, never a reminder of what has not.
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
  8. Quarantine the float sweep's name-collision class: a public-float hit
     is a registrant match, not an identity, and a wrong-entity float is a
     distinct error from a weak CIK join (Accel: metropcs read as T-Mobile
     at $112B, rocket as RKT, circle as public CRCL rather than acquired,
     vinted as defunct on a Wikidata glitch). Quarantine with
     `model_disputes_source` and a note; never accept a float the row's
     own evidence does not fit.
  9. A self-consistency hit is a class, not a row: when duty 7 disagrees
     on a pattern, sweep the whole base for it before adjudicating the
     sample (Accel: a 44-row sample surfaced systematic city/country
     incoherence — 27 pairs fixed plus 32 rows of Bengaluru→Bangalore
     normalization).

- **Lessons of the first merged run** (Thrive, 2026-09-03):
  1. `verify` counts classification over the base, not over the
     classification file: a rebuild that renames a slug leaves the old key
     behind with a status, and counting keys hid three unjudged rows
     behind three stale ones. Full mode now fails on unclassified base rows.
  2. Read `record`'s whole output, never its last line: a rejected batch
     records nothing, and a row the deterministic layers pre-filled
     (public float, unicorn-list value) then reads as classified in every
     count except the citation invariants.
  3. Copy `scratch/queue/queue.json` before the post-rebuild `prepare`:
     it is overwritten with the delta, and duty 7's blind re-judgment
     needs the evidence view of the original rows (rebuildable from
     `base.json` + the layer files, but only by hand).
  4. The web-search budget is a run constraint (200 calls per session):
     the A/B pass on a large visible slice (Thrive: 60 $1B+ rows) must be
     budgeted before the grind spends it. Out of budget, the app browser's
     DuckDuckGo HTML endpoint and direct fetches of known pages still
     answer targeted checks; whatever stays unattacked keeps its `stale`
     flag and is listed in the report.
  5. Base-shape guards are investor properties: `config.json`
     `verify.shape` (`one_b_share_max`, `c2a_rate_max`) restates the
     20% / 80% defaults with a note when the evidence model explains the
     shape (ruling in `decisions.md`); the guards still fire above it.

## 9. Review, escalation, and the end of a run

The review surface (the investor's `review.html`, written by
`run.py review`) is **read-only**: priority-ranked rows, evidence links, no
input widgets. Corrections arrive in chat, and each one is recorded
class-wide — as a ledger verdict or classification correction with
`who: "erik"` — so it binds every row of its class, outranks agent verdicts,
and survives every rebuild.

**The run does not stop for approval** (ruled by Erik 2026-09-03, merging
the base and classification runs). Milestones — gate result, base landed,
classification complete — are posted to the Linear issue as status
comments and the session continues past them. Erik reviews the surface
when he chooses; the run's exit is finished artifacts, not a sign-off.
Corrections that arrive after the run closes land the same way as during
it, and a corrected base is re-exported and re-reviewed before any ingest.

**Escalate only on a defined trigger**, and only for what evidence plus the
decisions file genuinely cannot resolve:

1. A derivation's facts (§1) turn out wrong and the re-derivation under
   the same test is not clean, or the investor's facts fall outside every
   standing test. A clean flip — wrong fact, same test, different outcome
   — is re-derived, recorded and reported, never escalated. A confirmed
   delta contradicted by the run's evidence escalates as before.
2. A firm-boundary question with no ruling that would move a class of rows
   (Accel: arista, a 13G-only post-IPO holding with no documented venture
   entry — in or out is a boundary ruling, not a row fix).
3. A published field would have to breach a taxonomy contract (Accel and
   Lightspeed: a geo core of three labels against the profile's two-label
   cap).
4. Evidence access fails in a way that leaves a layer permanently missing
   rather than delayed (an archive that never recovers, a site that blocks
   every ladder step).

Everything else — layer defects, gate misses, namesake clusters, new
standing rulings — the session resolves, records as a dated ruling in
`decisions.md` flagged for review, and reports. **When a trigger fires,
finish everything it does not block**, then raise it once at the end,
alongside the results; never stop mid-run with work outstanding that the
open question does not touch.

**Ingestion is gated on Erik's explicit approval** (ruled 2026-08-31, after
the a16z run ingested ahead of review; unchanged by the merge):
`ingest-companies.ts` and `ingest-investor.ts` write the shared database,
so they run only after Erik explicitly approves — never as an autonomous
step, even when the issue's Done-when lists ingestion. The run ends at
export + review.html + report; the session's closing message carries the
results, the open rulings and the ingest request, and stops. Corrections
that land after an approved ingest are re-ingested only with a fresh
approval, and rows removed from the base after an ingest are called out so
Erik can decide the database cleanup.

Before the closing message, the review surface is verified rendered —
serve it (`file://` is blocked in the app browser; use a static server)
and check that rows render flat, the profile panel expands, and the
surface is actually reviewable. It is an exit-criterion artifact, not a
byproduct.

Every run ends in the investor's `report.md`: method deltas, results,
corrections taken, the flag and debt counts behind `verify`, the open
rulings raised, and the session's prompt count — the number this pipeline
exists to drive down. **The target is two prompts: kickoff and the ingest
approval.** The count is final only after the ingest decision: review
exchanges count, and a16z went from "1 prompt, 0 corrections" mid-run to
10 prompts and 6 rulings by close. Session recipe: the strongest available
harness, web search enabled, the machine kept awake for the grind.

**Run close includes a playbook write-back, and it happens at close.** A
rule invented during the run that is investor-agnostic belongs in this
file, not only in the investor's `decisions.md` or the report — propose
the COLLECTION.md diff as the last act of the run, after the last
artifact, never at a milestone. The a16z run wrote seven durable lessons
into code and local files and none into the playbook; Accel wrote its
diff at its mid-run checkpoint and then ran nine more hours, so the whole
Common Crawl layer and every classification-phase rule went unrecorded
until the next investor needed them.

The icon is part of the gated step: at profile time
`fetch-investor-icon.ts --dry-run` normalizes the source image to a local
PNG for inspection and `investor.json` carries the source URL; the upload
to the Icon Images bucket runs with the ingest, after the approval, and
`ingest-investor.ts` then carries the bucket URL. **Order for a first-time
investor: icon upload, `ingest-investor.ts`, then `ingest-companies.ts`** —
the companies ingest resolves the investor's database id and refuses to
run before the investor row exists (Thrive, 2026-09-04).

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
10. Cross-investor: a company held by another investor reads the same
    `status` and `valuation_range` in that investor's published `base.csv`
    (identity: a shared strong CIK, or the loose name key, minus the pairs
    ruled distinct in `data/collection/cross-investor.json`). The track
    record consumes exactly these two columns with no status filter, so a
    disagreement is a disagreement about a published track record. It
    fails verify unless the pair is ruled `accepted` with a reason; the fix
    is to align the stale side (freshest as-of by default) in that
    investor's classification and re-export it. Added 2026-09-03 after the
    first four runs were found to disagree on ~20 shared companies
    (xAI private/$230B in one run and acquired in two; Waymo acquired in
    one and private/$126B in another; a dozen $1B+ marks one run had cited
    and another had missed). Runs done months apart will still straddle a
    band edge on as-of date alone for public rows (DoorDash at $92B vs
    $103B in the same month); align to one fresh cap rather than accept.

Two modes. Plain `verify` is the contract: every invariant above, full
fills, distribution guards, published surfaces current. `verify
--in-flight` runs mid-grind: invariants 2–7, 9 and 10 over every answered
row and drift (8) always, while unjudged rows, unfilled columns and
`not_member` rows awaiting the rebuild are counted and reported rather
than failed, and the distribution guards wait for the full mode. A merged
run is green in flight at every milestone and green in full once, at the
end.

## 11. Investor classification (the firm profile)

Every field here answers a question about the firm, not its portfolio,
and the profile is **step 7 of the same run**: built once, after the base
has landed and the grind is complete, by the same session. Output is the
investor's `investor.json` plus `investor.sources.json`, one source entry
per field; every field populated or explicitly null, through the taxonomy
gate, onto the review surface.

Built after the base, `build-firm-profile.py` runs its base-bound checks
once, for real: notable_investments asserted against ledger member
verdicts, the entry-round median over the verified members' Form D
histories, the focus recompute off the grind's sector tags. **The
landed-base signal is full ledger coverage** (§10 invariant 1), never
`base.json` existence — `needs_review` rows persist even in completed
bases (a16z closed with 563), and a single-source famous member
legitimately sits `needs_review` while being a member (Accel:
Flipkart/Spotify/Supercell during the archive outage). The profile's own
evidence work — the ADV pull, the fund filer sweep, the team payloads —
does not depend on the base and may be collected at any point in the run;
the fund filer sweep in particular is a trap-set input (§4) and belongs
early.

Why not in parallel any more: on Accel and Lightspeed the profile ran
base-less in a second session and re-asserted against the landed base
afterwards — three recompute rounds on Accel ($22.0M → $20.0M → $19.6M
median, published $20M throughout), two on Lightspeed ($17.25M → $17.5M,
published $17M throughout) — for zero published deltas, plus a first-hour
file collision on Lightspeed. The parallel start bought parallelism only.
**If a second session genuinely exists**, the a16z split still works:
declare file ownership by session message in the first minutes, not "up
front" — profile session owns `investor.json` + sources sidecar, team
payloads and the fund filer sweep; base session owns `config.json`,
`decisions.md`, site companies, the EDGAR sweeps, base + overlays — and
re-run the profile build once the base lands.

Field recipes, learned on Sequoia and a16z:

- **AUM.** Form ADV via IAPD for any registered adviser: Item 5.F RAUM is
  the firm's own sworn number and anchors the bottom of the range; press
  supplies the top. Resolve the adviser by CRD, not name — adviser names
  drift (AH Capital Management renamed to A16Z Capital Management under
  the same CRD). An exempt reporting adviser files no Item 5.F; its
  Section 7.B private-fund gross assets are the sworn substitute. An
  affiliated but separately registered adviser (a crossover or
  public-equities arm) is excluded from both AUM and the fund list, so
  the row stays internally consistent — but an affiliated ERA advising a
  desk ruled INSIDE the firm adds its 7.B gross assets to the umbrella
  RAUM for the range top (Accel: the London desk). Co-advisers of one
  desk report identical fund rosters, so dedupe by private-fund ID; and
  the umbrella's own 7.B roster should sum to its Item 5.F RAUM to the
  dollar — parse both and let the equality prove the parse. Both range
  ends can be sworn; press "AUM" figures may sit below the sworn floor
  and then belong in the flag, not the range. One RIA can cover several
  geographies (Lightspeed: US, Europe and Israel under CRD 160187 by the
  firm's own disclosure), in which case there is no in-boundary ERA and
  both range ends are one sworn number — test which shape applies rather
  than assuming the Accel London one. An ERA-only firm (Creandum: four exempt
  reporting advisers, no RIA) has no Item 5.F at all; both range ends are
  the 7.B composite, and press "AUM" quotes below it belong in the flag.
  The 7.B tables live in the IAPD PDFs; `pypdf` reads them.
- **Funds.** Sweep every Form D filer matching the firm's name on EDGAR —
  the partner-matched subset structurally misses vehicles. Sizes from
  Form D where the vehicle raised directly, from press where the size is an
  allocation; any entry carrying an accession is asserted against the
  filing at build time, and the build fails on mismatch. Where the main
  L.P. filed sold $0 (first close unfunded at filing), the filing's
  total-offering amount is exact corroboration for the press size
  (Accel: every such case matched to the dollar) — **but only for firms
  that file a total-offering amount**. Lightspeed's L.P.s file
  "Indefinite" offerings at $0 sold and amend at close or never, so six
  of fifteen fund sizes rested on press with the filing as existence
  corroboration only; test which filing style the firm uses before
  leaning on the cross-check. **Co-issued Form Ds cross-wire names to
  CIKs**: two vehicles can file one Form D as co-issuers (Lightspeed:
  X + Select I, XII + Select III, Luminous VI-A/B), and a per-accession
  issuer scan silently keeps the last co-issuer row — a $2.11B "flagship"
  that looked wrong against an $890M successor was two funds. Record
  `co_issuers` per filing and split by the documented close.
  Post-restructure caveat: where LP capital enters through an evergreen
  vehicle, sub-funds' own Form Ds show only principals' money.
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
  positioning and behaviour is signal, not error. A sector absent from the
  firm's own vocabulary despite portfolio evidence is the same signal in
  its strongest form (Lightspeed: no Security filter on a site listing
  Wiz, Netskope, Rubrik and Cato) — flag it for the post-grind recompute
  rather than adding the label by hand.
- **Icons are published under measured rules, not eyeballed.**
  `scripts/fetch-investor-icon.ts <slug> <source-url>` normalizes through
  `scripts/utils/icon-normalize.ts`, which enforces three properties the
  first four investors each broke in a different way: an icon must carry
  its **own opaque background** (a bare glyph on transparency is invisible
  in the app's dark mode — Lightspeed's favicon is one #303030 path with
  `fill="none"`, and its master was 84% transparent); artwork must sit
  inside a **keyline** (box ≤74%, furthest pixel ≤80% of the crop radius,
  because the leaderboard renders `rounded-full object-cover` — Sequoia's
  tree reached 94% and was being shaved); and glyph-to-plate **contrast
  must clear 3:1**, or the publish is refused rather than shipping an
  unreadable plate. A source that already backs itself is left alone,
  including a disc plate whose square corners are empty (Accel), since
  insetting it would shrink a full-bleed logo into a sticker. SVG sources
  rasterize at 2× the master before downsampling, never upscaled from
  their intrinsic size. `--plate <colour>` overrides the synthesized
  background, `--dry-run <file>` previews without uploading, and
  **`--audit` replays the current rules against every published icon** —
  run it when a rule changes, so icons that predate it are found rather
  than assumed fine. The DB still only changes on ingest.

- **Focus recompute needs representative tags.** A base-derived focus
  distribution publishes only when sector tags cover ≥25% of base rows;
  below that the tagged slice describes whichever surface carried tags,
  not the firm (a16z: only the accelerator's 251 rows carried tags, and
  the recompute had published an empty focus list). The firm's own sector
  enumeration stands until coverage clears the bar
  (`build-firm-profile.py` enforces this).

- **EDGAR files a non-US issuer's country in the state slot** as a
  two-character code from its "State or Country" list (Sweden = V7);
  `build-firm-profile.py` maps the codes to country names so an EU firm's
  hq_location reads "Stockholm, Sweden" rather than "Stockholm, V7".
- **People without CMS titles.** Where the team CMS publishes a group
  label but no titles (Creandum: "Investment Team"), titles come from the
  firm's own promotion and welcome posts where stated, and the group label
  stands for the rest; no title is inferred from LinkedIn or memory.
- **investment_range without Form D coverage.** When the Form D issuer
  histories cover only a handful of members, the median comes from the
  firm's own entry announcements that state a round size (Creandum: 47
  rounds since 2003 in the stories and archived press, published $7M),
  flagged press-based; fund sizes quoted in EUR or SEK convert at the ECB
  rate of the announcement date (§6, `scripts/fx-convert.py`) and the
  native figure stays in the fund's note.

**Profile without a site** (Thrive, 2026-09-03): `investment_stage`,
`investment_geo` and `investment_scope` are derived — stage from the fund
architecture (early/growth sleeves, opportunity funds) plus the landed
entry_stage distribution, geo from `hq_country` on the base, scope from the
grind's focus column with `profile.focus_min_companies` scaled to the base
(~4.5% of rows; 25 was the 900-row megafund value) — each flagged derived
in the sidecar. The fund table lists funds and sleeves; lettered co-invest
and SPV vehicles are counted and described in the basis, not listed.
Check the filing style before the $0-sold cross-check: a fund that files
Form D before first close ("Indefinite", $0 sold) carries its press or
firm-stated size, not an accession assertion. The team is the ADV owners
and officers plus the Form D related persons and press-documented
partners — publish what the record supports, null the rest.
