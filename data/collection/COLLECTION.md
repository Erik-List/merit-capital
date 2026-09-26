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

**Thin evidence is a design problem, not a stopping condition.** When a
layer returns nothing for this investor, the session invents one, and
changes the pipeline if that is what the invention needs — see §5, *When
the evidence is thin, invent the layer*. Register coverage per country,
for the European runs, is in §5 as well.

Everything lives investor-first under `data/collection/investors/<slug>/`;
every script takes the slug and derives its paths via `scripts/paths.py`, and
every investor-specific constant lives in the investor's `config.json`.
Starting a new investor means creating that directory with `config.json` and
`decisions.md` — nothing outside it changes.

The shape of a collection, in order:

1. Investor-specific decisions derived from the standing rule set, plus
   the confirmed deltas (§1).
2. Evidence layers collected (§5), base built.
3. Membership traps written to `config.verify.not_members` (§10 invariant
   11) before any verdict writes; `verify` enforces them on every run.
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
`data/collection/investors/<slug>/documentation/decisions.md`. The judge cites its rulings
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

  **Strategy desks** (Erik, 2026-09-04). T1 keys on adviser identity,
  which is a good proxy for independence and a poor one for "is this a
  venture desk". Where one adviser covers several investment
  strategies, the default above would pull the parent's non-venture
  funds in. So the desk partition runs on strategy as well as
  geography: non-venture strategies of the same adviser (buyout,
  credit, infrastructure, public equities, real assets) are
  `other_desk`, not `external`, and their rows leave the published base
  preserved in `excluded.json`, exactly as Accel's non-home desks
  already do. Resolve the desk per vehicle by CRD or CIK, never by the
  brand that announced the deal. Reaches Bain Capital Ventures and EQT
  Ventures, where the venture arm may or may not carry its own
  registration; check IAPD first, because where it does, T1 decides the
  case with no partition needed.

  **The profile is sliced to the same boundary as the base.** Where a
  §11 field's only source is the parent's filing (ADV Item 5.F RAUM is
  the usual one), the field is the sum of the venture desk's own
  disclosed funds, labelled as a floor, or null-and-flagged. A parent's
  RAUM never fills a child desk's `aum`: it would contradict the base
  it sits next to by an order of magnitude. Where the parent is
  publicly listed, its annual report segment disclosures are a stronger
  source than an ADV and should be used and written back (first
  candidate: EQT AB).
- **T2 — Fund money.** Did a fund of the firm hold the position? Default
  IN where it did, whatever the program or channel; OUT where the only
  connection is a person, a program listing or an association. IN:
  Sequoia Arc, a16z speedrun, Accel Atoms per cohort company where Accel
  money was deployed, Thrive incubations including pre-spin-out ones
  where a fund held the position. OUT: scout checks with no main-fund
  follow-on (ruled on Sequoia, a16z, Accel and Lightspeed); Lightspeed's
  Extreme Entrepreneurs (no funding); partners' personal angel books
  (Kushner; Cherry's founder-angel positions, Erik 2026-09-04);
  **a founder's angel check stays out even where the firm lists it as its
  own**, unless a fund of the firm held the position (Erik, 2026-09-26,
  binding every investor: "exclude as we did for Cherry"). This is Cherry's
  D2 generalised, and it reverses Point Nine's E1 of the same day, which had
  kept such rows flagged `pre_fund_angel`. Where a fund later came into a
  company the founder had backed personally, the row stays a member and its
  entry is the fund's first check, never the angel check (Point Nine: Clio,
  Westwing, Humanity). **The firm's own "previous" or "Pre <firm>" label is
  the evidence** that a listed position began before the fund (Point Nine's
  2018–2020 CMS filed JoinR under "Pre Point Nine"): read it for every row it
  touches;
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

  **Control positions** (Erik, 2026-09-04). A venture entry is a
  *minority* position taken through a financing of the company. OUT:
  any transaction in which the firm, alone or with its co-investor
  group, acquires control (50% or more of the voting equity
  post-transaction, or a transaction the company itself reports as a
  change of control), including LBOs and majority recapitalisations,
  and including where the company is private and the equity newly
  issued. A control acquisition is not a round, so every column that
  describes a round (`entry_stage`, entry valuation, the C2A cohort)
  is meaningless for it. This is the transaction-level counterpart to
  the vehicle-level exclusion above: Thrive Holdings was ruled out as a
  vehicle that makes no venture rounds, which does not decide the case
  where one vehicle does both (Insight, General Catalyst). Evidence
  proxy: a Form D exists for a financing and not for a purchase of
  existing shares, so a round whose Form D names the firm is a
  financing absent contrary evidence. Control rows leave the published
  base under `excluded.json` reason `control_position`, preserved and
  counted in the report (new reason code; not yet emitted by
  `build-company-base.py`). A base that excludes them **says so on the
  firm profile**: the published track record then covers the firm's
  venture activity rather than the firm, and without that statement it
  reads as the latter.

  **Sponsor promotes** (Erik, 2026-09-07, ruled on Khosla's KVSA II /
  Nextdoor). A firm that sponsors a blank-check company and takes it
  public through a de-SPAC has **not** made a venture entry: the
  sponsor's founder shares are issued by the shell at nominal cost when
  the shell is formed, and the position in the operating business
  arises from a reverse merger into a listing, not from a financing of
  that business. It is not T3's OUT limb either — the shares are not
  bought on the market and the entry is contemporaneous with the
  listing rather than after it — so T3 named no case until this
  ruling. **OUT, unless one of the firm's funds held the target
  through a venture round before the merger**, in which case the row is
  a member on that earlier round and the SPAC is irrelevant to its
  membership. The reasoning is the control-position one: a promote is a
  fee for assembling a listing vehicle, and every column that describes
  a round (`entry_stage`, entry valuation, the C2A cohort) is
  meaningless where there is no round to name. The SPAC shell itself is
  separately out under T5, as a vehicle with no operating business. A
  fund's PIPE into the merger is a different instrument and is judged
  on its own facts.
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
**there is no entry-date window** (Erik, 2026-09-19, PRO-137, retiring the
2006 constant and its `pre_window` / `pre_window_entry` flags: a 1998 entry is
judged on the same evidence as a 2024 one, and where the record does not give
the round the stage reads `undetermined` rather than taking a date-based
default. The old constant nulled graduation and excused the stage-evidence
rule on an unaudited hand-set flag, and it sorted on the wrong axis: what
predicts an unknowable round is whether the source ever carried a description,
not how old it is. A firm's 1998 page with a sentence per company resolves;
a modern REST listing with a name and a URL does not); secondaries and tenders
are Growth entries; a
private mark is `stale` beyond 24 months; the profile's geo core carries
at most two labels; a non-USD figure converts to USD at the ECB reference
rate of its own date, and a listing outside SEC registration takes a
web-cited market cap (both ruled on Creandum, Erik 2026-09-04; mechanics
in §6 valuation).

**Jurisdiction coverage** is a policy constant of the same kind (Erik,
2026-09-04), and it governs only what is built *ahead of* a run. It does
not narrow §5's standing instruction to invent a layer mid-run when the
evidence is thin: that instruction applies in every jurisdiction,
including the ones below the threshold.

A jurisdiction is **pre-built** when at least three investors in the
target list depend on it. Infrastructure only one run will ever use is
better found mid-run and written back than specified in advance. On the
current target list that threshold is met by the US (EDGAR, built),
Germany, the UK and the Nordics. What each register can actually answer
is §5's country table, and that table governs over any summary here: the
registers differ by direction (backtrace versus forward enumeration) and
only Denmark and Norway answer both. Sequence inside a pre-built
jurisdiction follows §5 as well, `status` first, since it is free and
machine-readable in every one of them and repairs the column this
playbook undercounts by construction, and a membership layer only where
that register supports one.

Below the threshold a jurisdiction is **decided in the run, never
degraded in advance**. The run probes its register under a bounded effort
budget, the same way §5 requires the Wayback eras to be
checked before concluding that no list ever existed, and records a
finding: usable (cite it, and propose the layer for write-back), or not
usable (name the obstacle, fall back to the layers that are proven, count
the gap). Switzerland, LatAm and Asia sit below the threshold today. That
fixes what is built before a run starts and nothing about what the run
may conclude or invent.

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

**A capture URL is a valid citation when the live page is gone.** A listing
that existed and was captured is evidence whether or not the firm still serves
it, so a `web.archive.org` or `index.commoncrawl.org` URL properly cites a page
a site migration has since 404'd (Cherry's pre-migration `cherry.vc/2021/...`
announcement posts, four S2A rows). Common Crawl was retired as a sweep layer
in 2026-09 because it surfaced no company the Internet Archive did not already
hold; **that retirement is about where we look, not about what counts, and it
does not invalidate a Common Crawl citation already recorded.** Where the
Internet Archive excludes a site outright (IVP, 2026-09-26: 403 on every
ivp.com capture), Common Crawl is that book's archive layer: its captures
parse into `sources/wayback/parsed/<year>.json` like any other, and a parsed
row's `capture_url` (the `index.commoncrawl.org` form) is used verbatim as
the row's `wayback_first_link`.

**A site listing suffices unless the firm itself disclaims the position**
(Erik, 2026-09-17, on Menlo). A company a firm lists because a partner backed
it at a *previous* firm is not a member. Menlo's live site carried fourteen
such historical rows (AppDynamics, DocuSign, Upstart from a partner's KPCB
years; Smartsheet from Summit; Upwork from Globespan) with no dated milestone,
its own team pages credit them to the prior firm, and no round names a Menlo
fund; T4 decides it, since the money behind the seat was the other firm's.
The signature: a listing with no milestone or date, a company too well known
to have gone unannounced, and a partner bio that claims it elsewhere. Verdict
`not_member` with `who: "erik"` and the team page as citation; every name
variant and every slug of its merge group needs its own verdict, because the
rebuild resurfaces them once the canonical leaves, and any such name in
`verify.known_positions` moves to `verify.not_members`.

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

**Sale consideration is not membership, and the acquirer leaves the base**
(Erik, 2026-09-22, ruled on Greylock's Intel, UnitedHealth, 3Com and
Conexant): where the only route into a base is stock the funds received
because that company BOUGHT a portfolio company, the row is `not_member`
with the acquired company named, whatever the size of the holding and
whichever surface carries it — a fund filing, or the firm's own site or
IPO roster. The investment is the company that was bought (Sonix, Maker
Communications, Share Development, all rows of their own), and the
acquirer's own scale is not the firm's track record. This settles the
"agent, flagged" reading above: the consideration check now decides
membership rather than only raising it. A firm that later backs the
acquirer on its own money is a separate, citable entry. **A share swap at a
sale is sale consideration too** (Point Nine, ruled 2026-09-26, PRO-157):
Point Nine received shares in Mobilike, madvertise's Turkish subsidiary, in
exchange for its madvertise shares when Mobile Network Group bought madvertise
in 2014, so `mobilike` is `not_member` and madvertise stays the member.

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
`membership-ledger.json`: per slug a verdict
(`member | not_member | uncertain`), `who`, an evidence class
(`site_listing | fund_filing | formd_adjudicated | knowledge | web`), a
basis sentence and a citation where one exists. The ledger is re-applied on
every rebuild. Human verdicts (`who: "erik"`) outrank agent verdicts — and
mechanically so on the ledger: `record` refuses to overwrite them.
Classification keys carry the same guard in `record`: an agent record may
add keys to a `who: "erik"` row but never overwrite or unflag the keys the
human set. Belt and braces: never re-emit a key Erik has set.
Two lines for one company in one file are one answer (PRO-156, after IVP
lost Suno's stage citation and Point Nine an Upciti line to the second line
silently replacing the first): `record` folds them key by key before it
validates, and refuses the file when the lines give one key different
values. An explicit `clear_flags` of a work flag (`needs_web_value`,
`model_disputes_source`, `unicorn_name_match`) is kept on the row as
`cleared_flags`, so the prepared layer cannot put the flag back; flags that
record a fact (`duplicate`, `boundary`, `cik_weak`) stay unclearable.
`not_member` rows leave the published base into `excluded.json` (reason
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
  name → treat as unrecognized, and flag it with the case that fits.
- **Three identity flags, and none for a recognised company** (Erik,
  2026-09-18). `identity_unresolved`: the company cannot be named at all.
  `identity_conflated`: one company split across two rows, a rename or a
  spelling drift — fix it in `identity-merges.json`, and where the row turns
  out to be the same investment filed under another legal entity rather than
  a second company, it is `not_member`, because keeping it double-counts one
  investment. `identity_homonym`: two real companies sharing a name — record
  the pair under `never_merge` in `identity-merges.json`, never only as a
  note, so the builder is stopped rather than a future reader warned. A
  company that IS named and described carries **no identity flag**:
  recognition happened, and confidence already records how firmly.
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
- **An unresolvable company is `undetermined`, never inferred** (Erik,
  2026-09-18). Where the company cannot be named, `entry_stage`,
  `valuation_range` and `seed_to_a_graduation` all read `undetermined`, and
  the flag carries the reason. Invariant 1's 100% fill still holds —
  `undetermined` is what satisfies it — and the derived metrics exclude these
  rows rather than counting them, so an unnameable company is not a Seed
  entry, not a below-$1B outcome and not a graduation denominator. The exclusion keys on the VALUE, not the flag, exactly as the
  database's `recompute_investor_metrics` does. This replaces the older rule that such a
  row took the firm's modal stage as an inferred fill: that produced 169
  invented Seed entries which then entered the published graduation cohort.
  **Exception: the filings are evidence even when the name is not.** A row
  whose stage comes out of its own Form D sequence (`formd_structural`,
  `formd_band`) keeps **whatever stage that sequence gives** — `Growth` on a
  first filing of $36M as readily as `Seed` on a small one — and is judged
  from the filings, name or no name: an EDGAR-only row is often a
  partner-signed issuer nobody ever listed, and its dated rounds decide the
  column. Such a row keeps the
  `identity_unresolved` flag and its values, and it stays in the metrics.
  What an unresolvable row may never do is assert a stage from `model` or an
  inferred fill: `record` and `verify` both refuse it.
- **An inferred value is only ever flagged, and a STAGE may no longer be
  inferred at all.** Where an inferred value fills a gap (US for a row on a US
  desk) it is confidence low and carries its flag (`country_prior`); it never
  lands silently. **`stage_prior` is deleted, not renamed** (Erik, 2026-09-19,
  PRO-135: "just rm stage_prior and use the other possible source options").
  So are **`pre_window` and `pre_window_entry`**: PRO-137 retired the window and
  the pre-2003 `Series A` convention, and the flags outlived them on 847 rows —
  while they persisted they went on waiving invariant 4 for rows like Menlo's
  Gilead ($100B+, its stage from the retired convention, no citation). `record`
  refuses all three, so none can return.
  The firm's classic entry round is a fact about the firm, and writing it into
  a company's row said something about that company the record never said — on
  950 rows. There is no honest fill between the evidence and `undetermined`, so
  the flag is refused by `record` and by `verify`, and the rows it marked carry
  one of the surviving sources or read `undetermined`. `country_prior` is
  untouched: the desk prior is all such a row has, the flag is what marks it
  inferred, and invariant 1 still wants a country.
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

## 4. Calibration gate (removed 2026-09-17, PRO-114)

The pre-registered trap set, the stage golden set and the blind pass over them
are gone: the same session wrote and took the test, and the layer scores it
produced are standing rules in §6 (the Form D band is a ceiling; the firm's own
label is class 1 for the round it names; a documented round overrides both).
What survives is the membership trap list, as `config.verify.not_members`
assertions that `verify` enforces on every run (§10 invariant 11), beside the
`known_positions` list. Earlier reports cite this section for their gate
results; those results stand as history.

## 5. Evidence layers

1. **Wayback portfolio listings**, one snapshot per year per site era. The
   investor's own listings captured over time also recover companies later
   removed from the live site (survivorship correction).

   Era parsers live in `scripts/wayback-pull.py`, including two generic
   ones (`listing_regex`, `js_array_listing`) that cover most markup eras
   without new code. A logo-only era (names rendered as images) may stay
   deliberately unparsed when snapshots of another list surface bracket
   those years — record the gap in the report.

   **A logo-only era is often readable after all, through the firm's own
   upload filenames, and it brings two artifact classes with it** (First
   Round, 2026-09-06). The 2010–2011 wall rendered every name as an image with
   no alt text, but the file names are the firm's own
   (`bazaarvoice.jpg`, `aster_data.jpg`, `Gigya_Small.jpg`), so an era pattern
   over `src="…/uploads/(?P<slug>…)"` recovers the roster. What it also
   recovers is junk, and both classes have to be handled before the base is
   published. **Filename variants of one company** ("birchboxsmall",
   "smartlingverysmal", five spellings of StumbleUpon) are best fixed in the
   PARSED SOURCE — a curated map applied to `sources/wayback/parsed/*.json`
   before the build, keyed case- and separator-insensitively because the slugs
   are file names — rather than in `identity-merges.json`, because a merge
   keeps the junk name on the surviving row and the published surface then
   carries it. And **the same page carries the ACQUIRER marks beside its
   exits**: Google, Microsoft, Intuit, Adobe, eBay and Facebook all appeared on
   First Round's wall next to the companies they had bought, and a
   name-matching layer will confidently label them. Those are `rejects`, not
   members. A reject may name a row by its ASCII spelling: the builder slugs
   KäuferPortal as `k-uferportal`, so rejects also match the folded slug, and
   a reject that matches no row is printed rather than skipped (PRO-156).

   **A `listing_regex` era whose name window is a bounded `.{0,N}?` can take
   the NEXT row's name.** Measured on the same run: rows whose per-row JS
   block omitted the name field pulled the following row's, shifting 14 of 153
   names in one capture — silently, because every name in the file is a real
   company name. Bound the window with a negative lookahead for the row
   delimiter (`(?:(?!<li).){0,700}?`), and check the parsed names against the
   slugs before the build: a name that does not normalise to its own slug is
   the tell. If the Internet Archive
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
   checked). **Parsed year files merge rather than replace**
   (keyed slug+path): a retired second capture archive wrote the same
   per-year shape from a different capture set, and those rows are no
   longer reproducible, so a pull that replaced the file would silently
   delete them. **When CDX refuses but replay answers**
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

   **Four rules every capture enumeration pays for** (each one bought on
   Accel):

   - **Catch-all shells are filtered by body digest.** accel.com in 2018
     served one identical body for any `/companies/<slug>`; 453 junk
     captures of crawler-invented slugs (adobe, amazon) shared one digest
     and were dropped. A capture enumeration without this filter invents
     members.
   - **Read the captured body, not only the index row.** A page can be
     served, captured and pulled within weeks (Accel: Corsa, "(ACCEL
     INVESTMENT) / Seed-Series A" in a May-2026 body, a 404 by run time,
     absent from the CMS) — the body is the evidence, the index row only
     says a body exists.
   - **Capture-year tenure windows are roster evidence.** People-page
     captures give per-person first and last years that matched known
     departures exactly (Breyer 2014–2016, Lixandru 2017–2019); Accel's
     roster tripled from 69 to 217 names and the Form D re-sweep grew from
     689 to 1,086 accessions on that alone.
   - **The site's own rendering owns name and slug.** A capture slug never
     names a row (a capture-created row was publishing "Assemblyai");
     namespace junk (`all`, `see-all`, `<slug>-2`) is configured out in
     `wayback.non_company_slugs`. **Where a listing renders the name twice,
     the row's own anchor text wins over the image `alt`** (Lux, 2026-09-06):
     `LOGO_ACCELERGY.gif` carried `alt="Angstrom Publishing"` and
     `LOGO_CIS.gif` carried `alt="Cambrios Technologies Corp."` — the firm's
     own copy-paste errors. An alt-first parser does not merely mislabel
     those rows, it DROPS them, because the wrong name collides with a row
     already seen; the era went from 6 companies to 11 on this fix alone.

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

   **A site that states its own ENTRY ROUND per company is the strongest
   entry_stage layer a run can have — and it must reach the queue.** Menlo's
   portfolio cards carry a Milestones list giving the firm's own entry year and
   round ("2011 - Partnered, Series B" on Uber, "2018 - Partnered, Series C" on
   Chime) for 214 of 245 listed rows; measured against 36 documented rounds it
   went 33/34 and is class 1 for the round word (§6). Two mechanics
   the run had to build, both now standing: `build-company-base.py` carries
   `site_entry_stage` and `site_invest_year` onto the base row and into
   `COLUMN_ORDER`, and `run.py`'s `EVIDENCE_FIELDS` carries both into every
   queue item — a class-1 layer the item does not carry is a layer the grind
   cannot use, which is the Black Forest Labs failure in a new place. Read the
   year as a CLOSE year, not an announcement date (§6).

   **Which of a site's fields may LABEL a row is a semantic question, settled
   once per book and then mechanical** (PRO-135). PRO-131 (a) made the firm's
   own listing class-1 stage evidence where it gives a round word; the field
   that carries it is declared in `config.site_api.entry_stage_fields`, the
   base build resolves it through `stage_words.py` into `site_entry_round` and
   `site_entry_stage_citation`, and every row it reaches is a row nobody has
   to write `undetermined`. Two tests, and they are different questions:
   **eligibility** asks whether the field is the firm's claim about the round
   IT entered — `initialInvestmentType`, the card's "Invested", USV's "FIRST
   INVESTMENT" — and refuses a field that reports the company's CURRENT stage
   or lists every round the firm joined; **the value** must then collapse onto
   one taxonomy stage (§6). Scored blind against each book's own cited rows,
   2026-09-19, eligible fields hold and ineligible ones fail in the same
   direction the semantics predict:

   | Field | Labels | Score | Verdict |
   | -- | -- | -- | -- |
   | Lightspeed `stage_invested` | 525 | 522/522 | promoted |
   | Accel `initial_type` | 567 | 552/553 | promoted |
   | Menlo `site_entry_stage` | 210 | 193/194 | promoted (was already in use) |
   | Felicis `site_entry_stage` / `stage_ladder` | 728 | 66/67 | promoted |
   | Redpoint `site_stage` | 258 | 178/182 | promoted |
   | USV `round_site` | 203 | 132/139 | promoted |
   | Battery `site_entry_stage` | 198 | 19/19 | promoted (`Early` is an anchor) |
   | Spark `stage_site_first` | 62 | 34/37 | promoted at `medium` |
   | Greylock `site_entry_stage` | 155 | 41/50 | promoted at `medium` |
   | Cherry `stage_site` | 46 | 11/14 | promoted at `medium` |
   | a16z `stages` | — | 38/57 | **refused**: a tag list of every round joined, not the entry; thirteen misses read Growth on a Series A entry |
   | Khosla `site_fund_label` | — | unscoreable | **refused** (D9): it names the FUND holding the position, and the firm re-lists follow-ons |
   | Lux `stage_board`, Thrive `stage`, Cherry `stage` | — | 5/14, 16/29, 8/32 | **refused**: Getro job boards, already refused by Lux R2 and Thrive ruling 8 |

   The score sets CONFIDENCE, not admission: `high` at ≥95% over ≥30 scored
   rows, `medium` otherwise, and a documented round still overrides the
   firm's own label with `stage_disputes_band` (§6, the socure and Personio
   classes). The refusals matter as much as the promotions — a job board's
   `stage` field looks exactly like an entry round and is the company's
   current one, which is why eligibility is judged before the score.

   **A logo-only era is recoverable from the image filename.** COLLECTION.md
   used to accept a logo era as a deliberate gap (a16z). It need not be one:
   where the era renders a company as `<img src="companies/<slug>.gif">`, an era
   pattern carrying BOTH a `(?P<slug>...)` branch on the filename and a
   `(?P<name>...)` branch on the text recovers both kinds of row in one pass —
   on Menlo's 1998 sector pages that returned UUNET, FaxSav, SpectraLink,
   MicroTherapeutics, Latitude Communications and Red Brick Systems, every one
   of them a real position that the text-only pattern missed. The slug is the
   company's identity, so the row lands unnamed and the judge names it.

   **A zero-row year on a page that returned bytes is a failed parser
   hypothesis, not an absence.** One site generation can carry two listing
   markups: Menlo's 2002–2003 XHTML site lists companies as bare `<li>Name</li>`
   on `all_alpha` and `prior_investments` and as `<div class="company">` summary
   cards on its four sector pages, so an era pattern written from the first and
   applied to both parsed eight cleanly-fetched captures (10–20 KB, correct
   titles) to zero rows — and the years read as empty. Found post-close, it cost
   three companies no other layer could see. **Before believing an empty year,
   check whether the raw file exists and has content**; if it does, the era
   pattern is the thing that failed, and each distinct page shape in an era needs
   its own pattern. The same check separates this from the fetch-failure case
   below: absence of a capture, absence of a response, and a capture the pattern
   could not read are three different claims.

   **The CDX scheme is not the variable — a failed fetch is.** An earlier
   version of this paragraph claimed plain HTTP was refused; that was wrong,
   and it was retracted on 2026-09-06 after two 8-query measurements per scheme
   (http 14/16, https 13/16) in which every failure was a curl rc=28 timeout.
   *Refinement, same day:* rc=28 is not the only failure mode — the Redpoint
   re-pull logged **seven rc=7 and one rc=56 against HTTPS** in one window
   (`redpoint-ventures/scratch/wayback-pull3.log`), so rc=7 is not a port-80
   signature either; it is what the archive returns to anyone while it is
   refusing connections. Read no scheme diagnosis out of the code at all.
   HTTPS is not more reliable and a scheme swap fixes nothing. `wayback-pull.py` and `partner-roster.py` use HTTPS as a
   convention only. What actually matters is that a failed fetch must never be
   recorded as an empty year: absence of a capture and absence of a response
   are different claims, and only the first is evidence.

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

   **A people namespace can hold a directory of PORTFOLIO FOUNDERS beside the
   firm's own roster, and mixing them poisons the Form D sweep** (First Round,
   2026-09-06). `/team/` carried both: the firm's partners at
   `/team/<initial+lastname>.html`, `/team/profile/<first_last>` and
   `/team/<group>/<first-last>`, and a 212-name network directory at
   `/team/<First_Last>` whose pages read "<Role> at <Company>" — Travis
   Kalanick, Jack Dorsey, Dave Baszucki, Neil Blumenthal. A founder IS a
   related person on their own company's Form D, so sweeping those names
   confirms hundreds of false members with filing-grade-looking evidence, and
   `roster.site_team_groups` does not help because the archived namespace has
   no groups. What separated them exactly was a **case rule** in
   `roster.slug_re`: the firm's own slugs are lowercase, the directory's are
   capitalised. Check what a people namespace actually contains before
   sweeping it, and where a directory like this exists, pull it deliberately —
   read the other way round it is a first-party company list, and on this run
   it was the layer that found the only site-invisible member the recall probe
   turned up.
3. **EDGAR**: the investor's vehicle registry (`scripts/edgar-entities.py`,
   one table serving role resolution, fund exclusion and lineage), issuer
   filings via the submissions API (`scripts/edgar-companies.py`), the
   Form D sweep on the roster (`scripts/formd-query.py <slug>`, targets
   derived from the roster; a partner who files as an initial and a middle
   name is matched on the middle name, IVP's Sandy Miller as "J. SANFORD
   MILLER", and when both sides lead with an initial the initials must agree)
   and issuer round histories
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

   **Wikidata needs the same recognition check as a CIK join, and a book of
   one-word names breaks it outright** (First Round, 2026-09-06). `prepare`
   filled `hq_country` on 104 rows from Wikidata; 89 of those rows have a
   single-token name, and the joins were wrong at a rate no layer survives —
   Uber→NL, Square→JP and defunct, Clay→NL, Planet→GR, Play→PL, Free→FR,
   Noon→SA, Togg→TR, Abra→GH and defunct, and Superhuman→"Ukraine[56]/ United
   States[57]", a footnoted prose string rather than a country code. The
   failure is silent in a way the float sweep's is not: `prepare` fills the
   column, the queue then asks only about EMPTY fields, and the row never
   reaches the judge (§8, the Black Forest Labs class). So **score the layer
   against the base before trusting it**, demote it to corroboration where the
   portfolio is full of common words, and re-judge every value it wrote with
   `model_disputes_source`. The same property is what makes invariant 10 noisy
   for such a firm: one-word names collide across investors (Maven, Whisper,
   Drift, Level, Cover, Haven, Gem, Parallel, Prepared), and each pair needs a
   `distinct` ruling rather than an alignment.

**When the investor publishes no list at all** (measured on Thrive,
2026-09-03, the first merged run): the `site_listing` class is not empty,
it moves. The firm's job board (Getro/Consider: `jobs.<domain>`) is a
first-party company list — enumerate it from its sitemap plus the
per-company pages (`site_api` with one `file_list` source), and never take
its stage field as a label. **That refusal is now standing and needs no
re-scoring**: Thrive's board scored 0/10 and Lux's scored 3/19, and the
misses have the same cause both times — the field describes the company's
CURRENT stage (`ipo`, `acquisition`, `series_f`), not the round the firm
entered, so it reads Recursion as "ipo" and a documented $3.5M seed as
"series_b". Keep it in the evidence pack as an unscored extra. A board is
worth enumerating on a disclosing firm too, not only a silent one: Lux's
carried 190 live companies against 215 on the marketing site, and 312
across the archive. The roster is curated from
the ADV, Form D related persons and press with press-dated tenure windows
(one ruling per name, §1), and the roster-name Form D sweep becomes the
primary structural layer. The ADV Section 7.B fund roster is membership
evidence for named-deal vehicles ("… Partners IV Stripe, LLC"). Press
sweeps run as a primary layer: every press-evidenced row lands as cited
`web`, and the recall probe's parametric enumeration is load-bearing (37
of 155 rows). Expect the base to be small and winner-heavy — the
fund-vehicle and press layers surface the companies that made news — and
say so in the report rather than reading it as a defect (§8, `verify.shape`).
Check the Wayback eras before concluding no list ever
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
next run is a delta. **Full-text search fails deep, not empty**: past about
2,000 hits the index can refuse a page on every retry (IVP, 2026-09-26:
`{"message": "Internal server error"}` from offset 2,100 of 2,196) and it
never serves an offset past 10,000. The sweep retries, then re-reads the
phrase in five-year date windows (halved where one still fails), and
records any window it still cannot read under `coverage` in
`fts-hits.json` as "partial: N of M", never as the absence of those hits.

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

**When the firm is a German seed manager** (measured on Cherry Ventures,
2026-09-04, the second EU run): the "no SEC" assumption fails in a specific
way — a German AIF manager that raises US money files Form ADV as an exempt
reporting adviser (Cherry Ventures Management GmbH (AIFM), CRD 301494) and
its Delaware feeder L.P.s file Form D, so Section 7.B gross asset values
exist and anchor AUM even though the ADV may lag the newest fund by two
vintages (Cherry's 2024 amendment carries Funds III and IV, not V). The
Handelsregister, read through North Data's free entity pages, gives the
whole vehicle tree with incorporation dates, general partners and the
limited partners named in the announcement history (44 entities: fund KGs,
GP GmbHs, Entrepreneurs / Employee / Carry KGs, numbered Opportunities
co-investment KGs, a Growth fund, a Select sleeve, UK and Swedish
branches) — filing-grade for the boundary and the fund ladder, and again
zero portfolio (the KGs' participations sit behind the aggregator's paywall;
handelsregister.de's own shareholder lists were not needed because the
firm's four list surfaces carried recall). BaFin's institution database
returns nothing for a registered (sub-threshold, KAGB §44) manager; the
ADV's Item 1.M records the BaFin registration instead.

**Four list surfaces can coexist for one small firm, and the archive is
still load-bearing.** Cherry's live Webflow site (94 pages, 90 listed, an
"(EXIT)" marker, no dates or stages), the Sanity CMS behind its 2024–2025
Next.js site — still publicly queryable after the migration, with a date
field, founders and sector tags for 86 companies plus 108 dated articles
(the migrated post archive with body text) — the archived WordPress
listings 2016–2023 (seven years, 107 companies, the firm's own investment
dates as `data-invested` epoch seconds, a 2016–2019 "Investment: Seed /
Series A" label, sector classes and exit flags) and a Getro job board
(98 companies, 38 on no other surface). Three rules from it: **a decommissioned
headless CMS is often still readable** — grep the archived RSC payload for
a Sanity or Contentful project id and query it before parsing the render;
**a site's date field carries mixed semantics** (the Webflow FOUNDED field
was the launch year for the old book and the announcement date for
2024+ rows; the 2020–2023 `data-chronological` attribute was the launch
year, not the investment year — verify a date field against three known
deals before it feeds `first_seen`); and **archived WordPress posts can be
title-only** (the bodies loaded by script from a wp-json endpoint the
archive never captured), in which case the URL slug still names the round
and the migrated CMS holds the text.

**The common-word name cost nothing once the phrases were entity-qualified**
(PRO-73's defining trap): "Cherry Ventures" / "Cherry Decentral" returned
five documents on EDGAR full-text search, all the firm's own Form Ds, and
five Wikipedia articles, four already in the base; the namesakes (Cherry
Tree Ventures, the 2007 Cherry Ventures Ltd of London, Cherry AB) were
caught by the entity registry's address check, never by the phrase layers.

**Evidence-pack mechanics that bit** (Cherry): a sentence splitter that
breaks at the decimal point of "$5.1M pre-seed" truncates the round word,
and every reader of the truncated snippet gets the round word wrong the
same way; the splitter must keep decimals. And a page whose rendered title sits below a hero block makes
a name extractor fall back to the URL slug (nine rows published as slugs
until a names-only rebuild) — check the extracted names against the CMS
rendering before the build.

### European registers, country by country

Researched 2026-09-04 at Erik's request, after the Creandum run reached
the EU registers and reported them as an entity-set source only. Two
different questions hide behind "can the register find it", and no
European register answers both the way Form D does: **backtrace** (who
holds this company) and **forward enumeration** (which companies does this
fund entity hold). Forward enumeration is the one that could replace the
roster Form D sweep; backtrace confirms a single row. Only Denmark and
Norway answer both today. Access terms here moved twice in three years and
in both directions, so verify a register's current terms at run time
rather than trusting this table.

| Country | Backtrace: holders of a company | Forward: a fund's holdings | Company status |
|---|---|---|---|
| Germany | **Yes** — GmbH shareholder lists, free, full cap table | Aggregator only (one hop) | Free |
| UK | Partial — inside filed documents, not the API | Officer graph only | **Free and structured** |
| France | Partial — inside filed acts | No | Free |
| Spain | No | No | Free |
| Denmark | **Yes** — legal owners at 5%+, structured | **Yes** — by owner | **Free and structured** |
| Norway | **Yes** — every AS, one national dataset | **Yes** — same dataset | Free |
| Sweden | No | No (the fund's own accounts only) | Free |
| Finland | No | No | Free |

- **Germany — handelsregister.de.** The strongest document source in
  Europe. Every GmbH files a shareholder list (`Gesellschafterliste`) on
  each change, naming every holder including foreign fund vehicles, and
  since DiRUG took effect on 2022-08-01 the register serves those
  documents free, without registration or login. A backtrace of any German
  GmbH gives the cap table with the fund entities on it. The register is
  searchable by company only, so forward enumeration needs an aggregator
  that has already extracted the relations (North Data holds them as a
  network with an API, exportable one hop at a time). An AG files no
  shareholder list, and the beneficial-ownership register
  (`Transparenzregister`) is behind a legitimate-interest wall.
- **UK — Companies House.** The API is free and genuinely structured, but
  not for shareholders: the confirmation statement carries the holder list
  only inside the filed document, and only when shares moved during the
  period, so a backtrace is a document read per company-year. Structured
  ownership stops at persons of significant control, a 25% threshold a
  venture investor rarely crosses. What the API does give is the officer
  register, searchable by person across companies — the direct analogue of
  the Form D related-person seat, with the same seat-dating discipline
  (§1). Share-allotment filings are a lead for dating rounds and have not
  been tested here.
- **France — INPI, data.inpi.fr.** The national business register serves
  company data, filed acts and statutes (since 1993) and non-confidential
  accounts (since 2017) free, through APIs and bulk FTP. Subscribers to a
  capital increase are frequently named in the filed minutes, so backtrace
  works document by document. No structured shareholder table exists, and
  beneficial-owner access is restricted to authorised parties or a
  demonstrated legitimate interest.
- **Spain — Registro Mercantil.** The weakest of the five. An SL's
  shareholder book is an internal company document, not a register filing;
  beneficial ownership is restricted; only incorporation, officers and
  capital events reach the official bulletin. A draft public-integrity law
  would move SL stakes into the register with legitimate-interest access,
  but it is not in force — check whether it has passed before planning a
  Spanish base around it.
- **Denmark — CVR / Det Offentlige Ejerregister on virk.dk.** The best
  structured source in Europe for this pipeline. Legal owners holding 5%
  or more are public, foreign fund vehicles included, and the register is
  searchable *by owner*, so a fund entity's Danish holdings enumerate
  directly. Beneficial-owner data left the public register on 2025-09-01;
  legal owners stayed. This is the one country where a Form-D-shaped
  structural layer can be built as-is.
- **Norway — Skatteetaten's aksjonærregisteret.** Every Norwegian AS and
  every foreign company listed in Oslo, at each year end, ordered as one
  national CSV. It answers both questions for the whole country in a
  single file. Two costs: annual granularity, and publication in May of
  the following year, so the newest holdings are always a year behind.
  Entity data comes separately from Brønnøysund's free registers.
- **Sweden — Bolagsverket.** No shareholder register exists. The share
  book (`aktiebok`) is held by the company, and the beneficial-owner
  search shows only holders at 25% or more, which excludes almost every
  venture position. Board seats are public and carry the officer trace.
  One indirect forward route for a Swedish-domiciled fund: the fund AB's
  own annual accounts may enumerate its holdings — untested, and worth one
  attempt on the next Swedish manager.
- **Finland — PRH.** Same shape as Sweden: the shareholder list
  (`osakasluettelo`) stays with the company under the Companies Act, and
  the beneficial-owner register is restricted to anti-money-laundering
  purposes. The public front end (ytj.fi) gives entities and officers.

Two findings that generalise beyond any one country:

**The registers pay off on `status`, not on membership.** Company status is
free and machine-readable in all eight jurisdictions, while shareholders
are structured in only two. `status` is the column this playbook admits is
undercounted by construction (§6) and worst for European rows, where quiet
shutdowns never reach English-language press. A dissolution, liquidation
or bankruptcy flag in the company's home register is filing-grade evidence
for `defunct` and costs one lookup. Build that before building any
membership layer out of registers.

**Beneficial-ownership registers are not a plan.** The walls in Germany,
France, Spain and Denmark all trace to the same post-2022 EU case law
restricting public access, and the thresholds (25%, or 5% in Denmark) sit
above most venture positions anyway. Treat a BO register as a bonus if the
run happens to have access, never as a layer the base depends on.

### When the evidence is thin, invent the layer

**The layers above are a floor, not a ceiling, and every one of them was
invented mid-run by a session that needed evidence it did not have.**
The exit-side EDGAR full-text sweep and the Wikipedia insource sweep came
out of an investor that published no portfolio page. The Nuxt payload parsers and the CDX-outage
replay path came out of a site and an archive that both refused the
configured route. None of them existed when the run that needed them
started.

So when this investor's evidence is thin — a layer returns nothing, a
whole class of evidence does not exist in this jurisdiction, a row resists
every source in `config.json` — **the executing session is expected to
invent a way in, and to reach for the unconventional channel before
recording a gap.** A gap written into the report without a documented
attempt is the one outcome this playbook does not accept. Scarce evidence
is a design problem, and solving it is the session's job, not Erik's.

**Invention may change the pipeline, not just the config.** New scripts,
new parsers, new source shapes under `sources/`, new config keys, changes
to the build, verify and export scripts, and changes to the run shape
itself are all in scope — the merged one-run shape came from a session
that proposed it, and the momentum slice came from a miss that a session
turned into a rule. Do not wait for permission to build a layer; build it,
score it, and propose it at close.

Think laterally about who else had a reason to write the fact down. A
financing has several parties and they all publish something. Channels
that have paid off, and channels not yet tried, as prompts rather than a
checklist:

- **The counterparty's surfaces, not the investor's**: the portfolio
  company's own investors page, its press kit, its founders' posts, the
  accelerator directory it belongs to — and the archived copies of each,
  which outlive the investor's own listing.
- **The exit side**: acquirers' filings, registration statements,
  insolvency and liquidator reports (which name shareholders precisely
  because an estate must), merger-control notifications published by
  competition authorities.
- **The money's other paperwork**: public grant and subsidy databases
  (CORDIS, Vinnova, Innovate UK, Bpifrance) pairing a company with dated
  funding; trademark and patent assignments, which move when a company is
  sold; the home-register status flags described above.
- **The firm's own non-portfolio surfaces**: annual review posts, LP-facing
  pages, event and podcast archives, newsletters. A partner naming a deal
  in an interview is often the only public record of an unannounced round.

Four rules make an invented layer usable, and they are not optional:

1. **Measure it before you trust it.** Check the new layer's field against
   documented rounds (press, the firm's own posts), exactly as the site's own
   stage field was measured: Accel's CMS label scored 30/31 and was promoted to class 1,
   Thrive's job-board stage scored 0/10 and was refused. An unscored layer
   may corroborate; it may not label.
2. **Class it** (§1 evidence rules). Every row it produces carries an
   evidence class and a citation. A new channel is never a reason to relax
   the source gates, the membership definition or the verify invariants.
3. **Record the negative result.** A channel tried and found empty is a
   finding, not a silence: Creandum's EU register pulls produced the entity
   set and zero membership evidence, and saying so is what makes the next
   EU run cheaper.
4. **Write it back at close** (§9) — into this file if it is
   investor-agnostic, into the scripts if it is mechanical. A layer
   invented and left inside one investor's directory has to be invented
   again by the next run.

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

**A signed but unclosed acquisition is a mark, not a status change** (Lux,
2026-09-06). The agreed price in a definitive agreement is a priced event
with a citable figure, and a better mark than the stale round it supersedes
— NVIDIA's agreement of 2026-09-02 to buy Hugging Face for $12,930,300,000,
disclosed in NVIDIA's own filing, against a 2023 round at $4.5B. But status
turns on the **closing**, so the row stays `private` at the agreed price
until the deal closes and flips to `acquired` then; the note carries the
agreement date and the expected close. The same reading rules out pricing a
row off a deal that is only *reported* or *in talks*.

**Insolvency followed by an asset sale is `acquired` with a successor note,
not `defunct`** (Cherry, 2026-09-04; agent, flagged): where the business
continues under an acquirer (Julienne Bruno out of administration into
Harvey & Brockless, Joblift's assets into Adzuna, Homelike's brand into
Spacest, Infarm's IP into a successor NewCo), the row reads `acquired` and
the note says the sale came out of insolvency; `defunct` is reserved for
businesses that ended (Watchmaster wound up, Weengs, Lesara, Move24). A
German seed book carries many of both, and the register's insolvency
notices are the layer that separates them.

**A bankruptcy filing with no sale yet reads `defunct`** (Erik, 2026-09-07,
ruled on Lux's Carbon Health): a company in Chapter 11 or an equivalent
reorganisation is recorded `defunct`, on the reading that the business goes
defunct afterwards. This closes the gap the vocabulary used to leave — the
row is neither `acquired` (no sale has happened) nor safely `private` at its
pre-filing mark, and `unknown` is for companies whose state cannot be
established, not for one whose state is on a court docket. The rule above
still governs the moment a sale follows: insolvency **followed by an asset
sale** is `acquired` with a successor note, because there the business
continues under an acquirer. The note carries the filing date and court.

**An acqui-hire does not decide the status; the company does** (Erik,
2026-09-20, ruled on Clockwise and Styra). When a buyer hires the team but
does not buy the company or its business, the row reads what happened to
the company: `defunct` if it shut down, `private` (or `public`) if it still
operates. Clockwise (team to Salesforce, which said it was "not acquiring
Clockwise or its technology"; product shut 2026-03-27) and Styra (founders
and most of the team to Apple, "did not acquire the company or its assets";
products open-sourced or shut) are both `defunct`. A buyer that takes the
business itself, the product or unit as a going concern, is still a sale
and reads `acquired` under the asset-sale rule above; an announcement that
calls it an acquisition (Postmates and Sosh) is read the same way. The note
names the hire and cites the shutdown or the evidence the company operates.

**Whichever surface supplies status covers only its own rows.** A site CMS
carries status for listed rows and nothing for members that entered
through filings, captures or recall; the grind authors status for every
layer-only member or the column ships with holes (Accel's close-out audit
found 105 such rows with no status at all). The firm's own status field
also goes stale, and the base overrides it with the cited event
(Lightspeed carried Wiz as `acquired` while the site still said Private).
**`defunct` is undercounted by construction** (Accel 3.3%): quiet
shutdowns present as `private` or `unknown`, and an acqui-hire recorded
before the 2026-09-20 ruling may still read `acquired`. The
column answers "last known state", not survivorship; no mortality rate may
be read off it, and the report says so.

### valuation

- **Figures are source-gated, machine-enforced.** `valuation_usd` non-null
  requires `valuation_source` ∈ {sec_public_float, wikidata, unicorn_list,
  web_verified} AND status private/public. `model_knowledge` never mints a
  figure: a company believed ≥$1B without a source is claimed private,
  figure null, flag `needs_web_value`; the web pass pins it or kills it.
- **`undetermined` accompanies an undetermined stage, and only that.** A
  row whose company could not be identified carries no band and no figure:
  `valuation_range: undetermined`, `valuation_usd` null. The two columns
  move together — the database rejects one without the other — because the
  rule-out that would otherwise produce `below_1b` reasons about a company,
  and here there is no company to reason about.
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
- **Vendor marks never band a row** (Rule A, ruled by Erik 2026-09-06 on
  USV and Spark; binds every investor from this wave on). A valuation
  published by a data vendor — PitchBook, CB Insights, Tracxn, Dealroom,
  Sacra, GetLatka, Contrary, Forge, Caplight, PremierAlts, UpMarket and
  the like — is an estimate unless it transcribes a priced event, and then
  the event is the source to cite. A `1b_plus` or higher band needs a
  priced round, tender or public float with a citable figure from the
  company, a filing or the press (a vendor's news arm reporting a priced
  round is press). Vendor figures go to the note; a company known only
  through vendor marks reads `below_1b` with the check recorded (Justworks:
  an undisclosed 2020 Series E and three vendors at $1.4B–$2.53B; MatX: the
  company's own "several billion" without a figure). The unicorn snapshot
  is itself an aggregator — a coverage floor to verify (§7), never a mark.
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

- **No date excuses an empty stage** (PRO-137). The column is filled from the
  company's own evidence, or it reads `undetermined`; an empty cell is missing
  work whatever the entry year. `undetermined` here says only that the round
  could not be established, so unlike an unnameable row it leaves
  `valuation_range` alone and takes no graduation (the row is not a Seed
  entry). `verify` rule 4's stage-evidence requirement is waived for it,
  because there is nothing to cite.
- Taxonomy: `Pre-Seed | Seed | Series A | Growth | undetermined`. Growth = Series B and
  everything later: C/D, crossover, pre-IPO, secondaries and tenders (a
  tender entry is an entry at scale), buyout-scale positions, recaps,
  consortium structures. SAFEs and seed extensions count as Seed; the label
  follows what the firm and the record call the round, not the check size.
  **Search for the firm's own round label before a named round in the press
  overrides it** (Point Nine, ruled 2026-09-26, PRO-157): Heygo's Series A
  coverage left out the seed Point Nine had led a year earlier, so the press
  name described a later round, not the firm's entry. A press-named round
  replaces the firm's label only once the firm's own posts, listing and
  archive have been read for the entry and show nothing earlier.
  Pre-2003 deals: the modern ladder does not map, and **the old "first
  institutional round is `Series A` by convention" rule is retired** (Erik,
  2026-09-19, PRO-137). It labelled 549 rows from their date alone. Where the
  record names the round, use it; where it does not, the stage is
  `undetermined`. Re-entry after a full exit restarts the clock at the new
  round.
- **Evidence order**, strongest first:

  1. `web_verified` + `entry_stage_citation` (URL naming the round and the
     firm's participation, or the firm's own memo/company page).
  1b. `first_party` + `entry_stage_citation`: **the firm's own listing, where
     it publishes a round word** (Erik, 2026-09-19, PRO-131 a). A company on
     the firm's site with an investment year AND a stage label is class-1
     evidence, the listing URL its citation. Menlo's R1 and Lightspeed's
     per-company round field already were this; it now holds wherever a firm
     publishes one, and it is the cheapest evidence there is, because the
     source is already on disk under `sources/site/`.
     **A bare year is an anchor, not a label.** A listing carrying an
     investment year and no round word may set `first_seen` and may bound
     entry recency; it may not mint a `Seed`. Dozens of rows have been
     re-staged from Series A to Growth for exactly that mistake.
     **The same guard generalises: a label is usable exactly when it collapses
     onto ONE taxonomy stage** (PRO-135). `Late Stage`, `Growth` and `Buyout`
     all collapse onto `Growth`, so they label; `Early`, `Early Stage` and
     `venture` straddle Seed and Series A, so they are anchors like the year.
     `Common`, `Token`, `IPO` and `series_unknown` name no round at all.
     `scripts/stage_words.py` is that vocabulary, shared by the base build and
     by `record`, and a word it does not know is reported rather than dropped.
  2. `formd_structural`: partner-anchored entry position with prior-filing
     count; the accessions are the citation.
  3. `model` with a named deal in the note ("led the 2011 Series A") at
     high/medium confidence.
  4. `model` at low confidence on a company the pass could name. There is no
     rung below this one: the inferred `stage_prior` fill that used to sit
     here is deleted (§3), and a named company whose round the record does not
     give reads `undetermined`. A row whose COMPANY could not be identified
     reads `undetermined` too (below).

  A publication-visible claim wants class 1 or 2. Citation is attempted for
  every row, priority $1B+ (incl. IPO), then recents, then the tail;
  `stage_uncited` marks attempted failures.
- **Research the funding history, and persist it** (Erik, 2026-09-23,
  PRO-143). Whenever a run looks for a row's entry round beyond what the
  deterministic layers give, it records the company's rounds as it found them,
  not only the verdict, under `funding_rounds` on the classification line:
  one entry per round, `{"date", "round", "amount_usd", "lead",
  "firm_in_round", "source", "source_type"}`, with `date` as precise as the
  source gives, `round` as the record names it, and `source_type` one of
  `firm | company | press | filing | vendor`. The stage and `entry_date` are
  then read off the round the firm entered, cited to a non-vendor source that
  names that round and ties the firm to it. Where no round can be tied to the
  firm, the stage stays `undetermined` and the list is kept anyway, with an
  empty list meaning the search ran and found none, so the next run starts
  from it instead of repeating the search. Until 2026-09-23 a run kept only a
  verdict, one citation and note prose; PRO-135 then had nothing to read but
  the prose, and 2,032 of the 2,187 rows it wrote `undetermined` had no round
  on disk at all. The best source depends on the era: for a company that went
  public, its IPO prospectus on EDGAR ("Principal Stockholders", "Certain
  Transactions", "Description of Capital Stock") lists every preferred series
  with dates and holders; for a modern company, the firm's own post, the
  company's release, then press. A vendor profile may guide the search and
  may be listed with `source_type: vendor`, but it never cites (Rule A). A
  history visible only in part is not a single round: a row whose citable
  record shows one round while a vendor shows three stays `undetermined`
  (the iCracked case).
- **An archive capture of the firm's listing never names or dates an entry**
  (Erik, 2026-09-23, PRO-143). The capture proves only that the firm held the
  company by that day. Reading "exactly one round closed before the capture"
  as the entry was measured and refused: on a sample of 20 undetermined rows
  it named a correct stage on 2, misfired wherever the history was only partly
  citable, and admitted companies that stalled while excluding those that
  raised their Series A before the page was first archived, which biases S2A
  downward. Direct research found the real entry round on 12 of the same 20.
- **No staged row without a source, and a `web_verified` citation names THAT
  company's round** (PRO-135, both enforced by `record` and by `verify`).
  Swept across all twenty books 2026-09-19. What the column rests on now:
  `program_terms` 6,705 · `model` 3,791 · `web_verified` 2,584 ·
  **`undetermined` 1,887** · `first_party` 780 · `formd_band` 590 ·
  `formd_structural` 94. Zero rows carry a stage with no source.
  A stage with an empty `entry_stage_source` is a claim with no provenance and
  no rung on the order above; 214 rows carried one. And a citation shared by
  ten rows or more is, by construction, not evidence about any one of them, so
  it may not carry a `web_verified` stage: a reused portfolio index is a
  per-company page pressed into service. **What makes a shared citation legal
  is what the page IS, not how many rows point at it.** A `program_terms` row
  cites a terms document that states what every cohort company got, and a
  `first_party` row cites a listing that states a round for each row on it —
  Felicis and Menlo both publish a per-company stage on the portfolio page, so
  there the evidence was real all along and only the SOURCE was wrong. Both
  stay legal at any number of rows. `undetermined` is exempt from all of it: it
  asserts nothing, so there is nothing to cite.
- **A programme entry on standard small-check terms is `Pre-Seed`** (Erik,
  2026-09-19). Where a firm runs an accelerator or programme that invests a
  standard cheque on standard terms — a16z's SPEEDRUN at $500k, YC's batch
  deal — the stage is the PROGRAMME's, not a round the company negotiated:
  `Pre-Seed`, source `program_terms`, and the note names the cohort. **The
  citation is the TERMS document**, not a per-company round page —
  `speedrun.a16z.com/faq` for a16z's $500k, `ycombinator.com/deal` for YC's
  batch deal — which is exactly what makes it evidence about a company nobody
  has written about. A terms page shared by thousands of rows is therefore
  correct here and must not be swept up with the reused index pages that a
  `web_verified` claim may never rest on. It is a
  fact about a documented transaction, so it survives a missing company name
  the way a Form D sequence does, and `record` accepts it on an
  `identity_unresolved` row. It also leaves the S2A cohort: a Pre-Seed entry
  is not a Seed entry, so `seed_to_a_graduation` is null by the ordinary rule.
  This replaces the older reading that a programme cheque is a Seed by
  instrument, which put whole accelerator cohorts into a seed-to-A rate they
  never belonged in.
- **A company that cannot be identified reads `undetermined`** (Erik,
  2026-09-18). Where the pass cannot say what company the row is — the page
  is gone, the name is one generic word, no filing or publisher matches —
  the stage is not inferred from the firm's modal round. The row is flagged
  `identity_unresolved` and `entry_stage`, `valuation_range` and
  `seed_to_a_graduation` all read `undetermined`; the row stays a member
  (the firm's own listing is the membership evidence), it satisfies
  invariant 1's 100% fill, and every derived metric excludes it. The older
  inferred fill put 169 invented Seed entries into the published graduation
  cohort. A Form D giving a dated seed-band round is evidence even with no
  name attached, so such a row keeps `Seed` and is judged normally.
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
  late at-scale entries.** Check it against documented rounds before trusting
  it; where it holds it is class 1 — but a CMS that says "seed" or "Series A"
  for a company the firm demonstrably entered at B or later is describing
  the company when it was listed, not the deal (Accel: 17 rows, the socure
  class). Precedence: **the label follows the record** — a documented
  entry round at scale overrides the site's label, flagged
  `stage_disputes_band` with the citation.
- **A firm's own announcement archive announces the round the firm LED,
  which is regularly a follow-on and not the entry.** The Creandum finding —
  score the announcement archive as a class-1 entry-stage layer — INVERTS on a
  firm that leads later rounds into companies it seeded quietly. On Menlo the
  archive scored WORSE than the site's CMS field, and four rows proved it inside
  the run's own sources: eero ("we first invested in eero's seed round two years
  ago", 2014, against a 2016 post announcing the $50M round it led), H1 ("in
  April 2020, Menlo led the Series A", against a December post announcing the
  co-led Series B), and Goodfire and Numeric, both entered at the seed and both
  announced only at the Series A the firm led. Class-wide rule: an announcement
  is class 1 for the round it NAMES; it asserts an ENTRY only where the post
  says so in words.
- **A site's per-company year field is a CLOSE year, not an announcement
  date.** Five rows whose round word the Menlo CMS got right carry a year one
  earlier than the press announcement (Dropcam 2011 vs Jun-2012, ConverzAI 2024
  vs Feb-2025, Orb 2022 vs Mar-2023, Semgrep 2024 vs Feb-2025). Such a field may
  set `first_seen`; it may not be read as an announcement date, and a year
  disagreement with press never overrides the round word.
- **"The firm led the A" folklore fails one-directionally on famous
  rows.** Accel's citation pass corrected 12 stages and ten went Series A
  → Growth (Personio: Northzone led the A, Accel entered at the $75M C;
  Netskope, PagerDuty, Trade Republic, Sennder, BlaBlaCar, Doctolib, G2
  likewise). Reputation is not evidence: the entry round of every famous
  row is cited, and the firm's own dated company or relationship pages
  are the first place to look.

### seed_to_a_graduation (S2A)

**A status, never a boolean, and on a Seed entry always decided** (Erik,
2026-09-16 and 2026-09-17; PRO-132). Every Seed entry carries exactly one of
`graduated | not_graduated | censored`, and null is reserved for a non-Seed
entry. **A company past the censoring window with no evidence of a later round
did not graduate**, and the column says so rather than abstaining. The old
fourth value, `undetermined`, left the denominator, so every row we failed to
establish inflated the published rate, and the bias was not random: a company
that raised a big Series A gets written about, one that quietly stalled does
not, so what fell out of the cohort was disproportionately the
non-graduations. Measured before the rework on five books, counting only rows
with a cited seed, an entry past the clock and a dated search that found
nothing: USV 86.8% became 61.1%, Redpoint 82.1% became 60.5%, Spark 73.2%
became 58.8%. Coverage is now 100% of the Seed entries old enough to count,
by construction.

The column is **judged, never pre-filled**: `prepare` queues the
`seed_to_a_graduation` need on every Seed row that still owes it (no decided
status; a `not_graduated` without its absence test; a decided row without its
`entry_date`), the Form D layer's verdict rides in the item as
`formd_graduation`, the publisher surfaces ride as `graduation_evidence`
(below), and only a judged status closes the need.

`undetermined` survives in the column in one place only, **as the cascade of
an undetermined STAGE**, where there is no seed to graduate from: the company
that cannot be named (`identity_unresolved`, Erik 2026-09-18) and the
token-funded position (Erik 2026-09-19, below) read `undetermined` in
`entry_stage` and here. `record` refuses it on any row that has a stage, and
`export` publishes what the row stores: `undetermined` where it is stored,
null on a named row whose round the record does not give, and it refuses to
publish a Seed row with no decided status at all.

Evidence per status, verified by construction (`record` refuses anything
less, so no verified tag exists: the cohort is the verified set):

- `graduated`: a later priced round ≥ max(2× entry, $5M) in the company's
  own Form D sequence (`graduation_source: formd`, the accessions are the
  citation, and the answer must agree with the layer; a filing whose sale
  date is within 90 days of the entry's is a close of the same round, not a
  later one — Boku's $13M round filed its March and June closes separately,
  Benchmark 2026-09-16), or a cited later
  round — the firm's own post or company page, the company's own funding
  page (`first_party`), a press release or SEC filing naming the round
  (`web_verified`) — with `graduation_citation`. **A later round the record NAMES as a Series A
  or later graduates the row whatever the amounts** (Erik, 2026-09-17): the
  round word is the fact the column asks about, and a flat or small A is
  still an A (Menlo's Decent, $8M seed → $10M A; Mimic, $27M → $50M; Spark's
  Panjo, $1.6M → $4.6M). The 2× / $5M step-up decides only rounds with no
  name, which in practice means the Form D layer: it reports amounts and
  never round words, so there the test stands unchanged. **Where the seed's
  amount is not on record, the era's seed-band ceiling stands in for it**
  (the structural rules under entry_stage: $1.5M to 2010, $2.5M 2011-14, $4M
  2015-18, $6M 2019-21, $8M from 2022), so an unnamed later round graduates
  the row at $5M for an entry to 2014, $8M for 2015-18, $12M for 2019-21 and
  $16M from 2022. An unknown seed amount is never a reason for a no: the first
  PRO-132 pass recorded Creandum's Soundtrack Your Brand as not graduated
  beside a $22M round three years after its 2014 seed. **A vendor page never
  cites a graduation either** (Rule A): Crunchbase profiles, PitchBook, Tracxn,
  Dealroom, CB Insights and the like transcribe a round, and the round's own
  announcement is the citation; `record` and `verify` refuse one
  (Crunchbase News, the vendor's press arm, is press and passes).
- `not_graduated`: **the absence test, a positive finding** (PRO-132). Every
  no records the search that found no later round, whatever it rests on, and
  `record` refuses one that is incomplete:
  1. the entry is past the censoring window on the day of the check, read at
     the LATEST day its `entry_date` can mean (a bare `2024` is 2024-12-31),
     because the clock wins inside its window. The clock guards an ABSENCE
     only: a cited acquisition or shutdown ends the chance to raise at all, so
     it decides the row inside the window too (Menlo's fintool, a 2025 seed
     bought by Microsoft in April 2026);
  2. `graduation_asof`, the day the search ran;
  3. `graduation_surfaces`, one line per surface in the form
     `<surface>: <what was searched> -> <what it showed>`, naming the firm's
     own archive (`firm:`), the company's Form D sequence where the company
     files in the US (`formd:`), and **at least two publisher surfaces**:
     places that would have reported a later round had there been one, such
     as a press search (`googlenews:`), a publication's own archive
     (`techcrunch:`, `crunchbase_news:`), the company's own site or newsroom
     (`company:`), its Wikipedia article. A vendor's database (Crunchbase
     profiles, PitchBook, Tracxn, Dealroom and the like) is never one:
     vendor pages never carry a no (Rule A). **A sibling investor's row for
     the same company is a surface too** (`sibling:<slug>`; Point Nine,
     ruled 2026-09-26, PRO-157): its note and citations may already hold the
     later round. Accel's merXu note had the November 2021 Prosus-led round
     that the Point Nine run's English searches missed; a Polish-language
     pass then found it named a Series A (EMEA Startups, 2021-11-16). Read the
     sibling's row before recording a no; where it names a round, that round
     decides the row and the two books are aligned in the same pass;
  4. the entry inside the coverage of what the no rests on.

  What the no rests on is its `graduation_source`. `formd` is the Form D
  absence: the rescan as-of ≥ entry + 24 months **and the entry inside the
  layer's coverage**. Electronic Form D filing opens in September 2008, so on
  an earlier entry the follow-on window sits in years the filings do not cover
  and their silence says nothing; the layer declines such a row
  (`formd_before_coverage`) and the judge decides it from evidence outside the
  filings. An absence verdict requires the entry to sit inside the register's
  coverage; stated that way, any register with a start date carries the same
  rule (Erik, 2026-09-19). `web_verified` or `first_party` is a cited
  terminal event: the acquisition or shutdown in `graduation_citation`, the
  note naming the seed as the last round. `absence_check` is a no whose
  evidence is the search itself. The press surfaces cover startup financings
  systematically from 2005 (TechCrunch launched in June 2005), so an
  `absence_check` needs an entry from 2005 on; an older entry takes a no only
  from a cited terminal event. `scripts/graduation-surfaces.py` runs the
  standard surfaces for every open row (two Google News searches, one with
  round words and one with the firm's name, plus TechCrunch's and Crunchbase
  News's own search) and records each as found, confirmed empty, or failed.
  **A company outside the US is also searched in its own Google News edition
  and language** (`googlenews_local`), because a Nordic or German round
  reported only at home is invisible to the English searches: the first pass
  on Creandum rested a quarter of its nos on English surfaces alone. Recorded
  nos stay targets on every run, so a re-run is a re-check. A
  failed lookup is never an absence and is retried on the next run. General
  web engines were measured and refused for bulk use on 2026-09-20:
  DuckDuckGo serves a captcha to scripts, Brave answers about five queries
  and then refuses for minutes, and Bing serves a scripted client unrelated
  results. The judge's own web search is kept for the rows the surfaces leave
  open.
- `censored`: `entry_date` less than 24 months before today. **The clock
  wins inside the window** (Erik, 2026-09-19): a dated search that finds
  nothing on a row younger than 24 months leaves it `censored`, not
  `not_graduated`. The clock is about opportunity rather than evidence, and a
  six-month-old seed with no Series A is not a failure; reading absence as a
  no there would delete censoring and turn the column into a point-in-time
  snapshot, which is a different metric. The clock is
  re-read on every `verify`; an entry that has aged past it owes a decision.
  A coarse date is read at the LATEST day it can mean, for a no and for
  `censored` alike (PRO-132): a bare `2024` may still be inside the window
  on 2026-09-20, so it is censored and cannot be a no; a bare `2023` cannot
  be young, so it is decided. Every coarse date is therefore decidable, and
  none is decided on a guessed month (Lightspeed's Zo Computer, whose firm
  card gives only the year).
- **A paywall is not a reason to abstain** (Erik, 2026-09-19). Where a round
  is known to exist behind a publisher that blocks us, classify on what is
  visible independent of the paywall: a headline, a snippet or an index entry
  naming a later round graduates the row, cited to that visible surface. What
  the body text would add is detail, not the fact. The same holds in reverse
  — a paywalled page proves nothing about a round it does not name.
- **A token-funded position reads `undetermined` in the stage AND the
  graduation** (Erik, 2026-09-19). Where the money went in as a token
  purchase and no priced round exists to stage — USV's DAO and protocol
  positions are the class — there is no seed to enter and no Series A to
  graduate to, so both columns say so and the row leaves the cohort. It keeps
  its band and its status: the company is named and its scale is often
  knowable, which is why this is not the unnameable case and why the
  stage-to-band cascade does not apply. Flag it `token_funded` so the class
  can be counted rather than inferred from prose.

**A decided row may rest on an uncited stage when its own evidence decides
it** (Erik, 2026-09-19, PRO-131 b; extended to the no by PRO-132). Where the
later round is cited but no page ties the firm to the seed, the row is
DECIDED: the graduation keeps its source and citation, `entry_stage_confidence`
reads `low`, and the row carries `stage_uncited`. The graduation is the
published fact and the stage is context; discarding the row threw away
something the record gives for want of something it does not. A
`not_graduated` has the same standing when ITS evidence is complete (the
filings, a cited end, or the full absence test with the entry date known).
With (b) alone only the graduations on an uncited seed kept their place, and
the non-graduations fell out of the cohort for want of the same citation,
which is the upward bias this column's rework exists to remove. `verify`
counts both on its `stage leg` line, so the softening is visible rather than
silent. It licenses nothing else: a graduation still needs its citation, a no
still needs its absence test, and **a row with no evidence of its entry at
all** (no seed announcement, no Form D, no dated listing, nothing that dates
it) has no Seed entry to decide: its stage reads `undetermined`, because the
record does not give the round. The firm's own listing (evidence class 1b
above) is the cheaper fix and is tried first.

`graduation_source` ∈ `formd | first_party | web_verified | absence_check`;
the model may not decide a graduation. **`entry_date` is required on every
decided row and every censored one** (YYYY, YYYY-MM or YYYY-MM-DD), and it is
read off, in order, the seed's own citation, the Form D entry filing where the
stage comes from the filings, or the firm's own listing year. Never off note
prose, never off the Form D anchor of a later round, and never off
`first_seen`, which dates a capture of the listing rather than the entry: all
three carry a later date more prominently than the entry, and all three fail
on exactly the long-gap rows that matter (USV's buglabs published a 2010 entry
for a 2006 seed until `fb6fa17`). A bare year reads as its first day for
`censored` and its last day for a no, so a recent entry needs month precision
either way. Cross-check (invariant 7): no row ends `not_graduated` +
(valuation ≥$1B or public); that combination is a Form D blind spot
(4(a)(2), foreign), and the round that exists is cited instead. **Except
where the entry round set the mark**: a private row whose $1B+ mark dates
within six months of its entry was valued by its own seed, and implies no
later round (Yuga Labs' $450M seed at $4B, March 2022, never followed).

The published block carries five numbers: seed entries, censored, cohort
(`sample_size`), graduated, rate. Coverage, `sample_size / (seed_entries −
censored)`, is 100% on every judged book, so the sentence now carries what the
nos rest on rather than a selection bias: "of N seed entries, K were too
recent to count; of the M that remain, R% raised a later round. Of the Q that
did not, A rest on the filings, B on a cited end and C on a dated search of
the named surfaces." An investor whose evidence cannot establish the column
at all may decline it in `config.json` (`verify.c2a_deterministic: false`): it
is never asked and its column publishes empty. A **pre-seed investor** is a
different case and publishes nothing at all: YC's whole book enters on the
batch deal, so every row is `Pre-Seed` and the column does not apply (the
transition its cohort makes is pre-seed to seed, which this dataset does not
measure; Erik, 2026-09-19). A classification file from before these rules is
rewritten by `run.py migrate-graduation`: a cited `web_verified` graduation on
a cited stage stays, everything else re-enters the queue, a value left on a
non-Seed row is dropped, and `--reopen` sends every judged `undetermined` on a
row that has a stage back to the judge.

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

**The city is asked and required, like the country** (Erik, 2026-09-24).
The investor page draws its whole Investment Geography bar from `hq_city`
alone, and a company with no city lands in "Other". Until this date
`prepare` never asked for it and `verify` only printed the fill, so a book
could close "clean" with the column empty: Lux (0 of 270) and Felicis (0 of
493) published **100% "Other"**. Now `prepare` asks `hq_city` for every
nameable row that has neither a city nor `city_unknown`, and `verify` fails a
row with neither. `city_unknown` is a claim that the judge LOOKED and could
not place the company; it is never a way to skip the question. A row whose
company cannot be named at all (`identity_unresolved`) is not asked. When a
city lands, `record` drops a leftover `city_unknown` from the row.

Books closed before the rule are held at the count they carried when it
landed (`data/collection/shared/city-debt.json`): `verify` prints the debt
and fails only if it grows, so no book went red and no new row arrives
without a city. A city pass clears a book (re-run `prepare`, judge the
queued cities, then lower or remove its entry). Every new book is strict.

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
queue. The S2A column has no debt value any more (PRO-132): a Seed row is
decided or it is open, `verify --in-flight` counts the open ones, and `export`
refuses to publish a book that still holds one (`cohort_unverified` retired
2026-09-16: an unverified yes or no is not recorded at all). `verify`
tolerates only flagged debt.

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
- **Graduation is judged, never pre-filled** (2026-09-16). Every Seed row
  that still owes the column (no decided status, a `not_graduated` without
  its absence test, a decided row without its `entry_date`; PRO-132), and
  every row whose stage is itself open, carries the `seed_to_a_graduation`
  need; the Form D layer's verdict rides in the item as `formd_graduation`
  (status, entry and step-up amounts, entry date, the rescan's as-of), which
  the judge confirms with `graduation_source: formd` or disputes with a
  citation. The need closes on a decided status with its evidence complete,
  or on a judged non-Seed stage.
  The item carries `entry_date` and `entry_quarter` from the filings and
  `site_invest_year` from the site as the judge's clock for the censor
  rule; where none exists the date comes from the citation or the
  program's cohort table in `decisions.md`. **Run
  `scripts/graduation-surfaces.py <slug>` before `prepare`** on a book with
  open graduations: the next `prepare` carries its result into each item as
  `graduation_evidence` (the headlines that name the company, ranked, with
  per-surface status and what sibling books established for the same
  company), so the judge decides from the item and a no can name its
  surfaces. It exits 3 while any lookup failed; re-run it until clean.
- **One queue, one pass per row.** `prepare` emits every open need for a
  row in one item — `membership` first when the row is unjudged, then
  whichever of `status`, `hq_country`, `entry_stage`, `valuation_range`,
  `seed_to_a_graduation` the deterministic layers left empty — and carries the row's evidence
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
  rebuild is the one step that moves `not_member` rows into `excluded.json`
  and lands recall additions. After it, one `prepare` re-emits the delta
  (new rows, and any need still open) and the grind finishes it.
  Rebuilding at any other point costs a re-prepare and a renumbered queue
  for nothing.
- **A membership verdict made in the post-rebuild delta needs a second,
  final rebuild.** The one-rebuild schedule assumes the delta only fills
  classification, but the delta grind can rule a row `not_member` — Menlo's did,
  twice — and those rows then have nowhere to go: `verify` fails them as
  "published despite not_member" and the schedule offers no landing. Run one
  more rebuild before `export` whenever the delta produced a membership verdict,
  and say so in the report. It is safe there because the grind is complete.
- **`record` routes a line by the presence of `verdict`, so a MEMBER needs TWO
  lines** — the verdict line and a classification line. A single line carrying
  both is recorded as a verdict and every classification key on it is dropped
  silently; a 45-row batch recorded "45 verdicts + 0 classification rows" before
  the split was noticed.
- **"Emit only the keys for the needs asked" has one licensed exception and it
  fires often.** A `formd_band` stage the judge overrules is by definition a key
  the queue did not ask for, because the band already filled it — 23 Menlo rows
  needed exactly that override. A tool that filters emissions against the
  queue's `need` list must let a deliberate dispute through, or the judge's
  corrections are silently discarded.
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
  citation URLs, the §6 graduation contract against the record on disk,
  city shape, country codes) and rejects violations; answers
  merge per key into existing records; flags union; only `clear_flags`
  removes. **Emit only the keys for the needs asked** (plus `flags`, `note`,
  and `funding_rounds` wherever the entry round was researched, §6)
  — extra keys clobber filing-grade facts at merge time; the one exception
  is a deliberate dispute. `record` stores `funding_rounds` as written and
  does not yet check its shape, so the judge keeps to the §6 form.
- **A person under two spellings is two people to the tenure filter** (First
  Round, 2026-09-06). `partner-roster.py` unions its sources by slug, so
  "Josh Kopelman" from the site and "Joshua Kopelman" from the Form D related
  persons land as separate roster rows with separate windows, and
  `build-company-base.py`'s ex-partner rule then reads a partner as departed
  years before they left — it removed rows on a "last on site 2012" for a
  partner who was still filing in 2020. Collapse the variants to one entry per
  person with the union window and its basis before the base is built, and
  re-check the removal list afterwards: the rule is doing exactly what it
  should, on a roster that was wrong.
- **A rebuild that renames a row carries the row's answers with it**
  (PRO-135). The slug is derived from the display name and the builder takes
  the most recent rendering (c8f28f7), so a rebuild can rename a row it has
  not otherwise touched — `MapR Technology` to `MapR`, `Sidecar Technologies,
  Inc.` to `Sidecar` — and every overlay joins on the slug. Left alone the row
  loses its verdict and its classification, comes back unjudged, and `verify`
  reports the old key as merely stale rather than as work thrown away: nine
  Lightspeed rows, two Spark, one Accel, on one rebuild. `rekey_overlays.py`
  now runs inside the build and moves them, matching the two sides on evidence
  a rename does not touch (site id, site URL, CIK, first Form D accession,
  first wayback capture), and only where that evidence is unique to one row.
  Where nothing matches it moves nothing and prints the pair, because from the
  slug alone a departure and an arrival look exactly like a rename. It prints
  every move it makes; read them, because this is the same surface as the
  database rename problem below.
- **Identity duplicates are fixed upstream**, in the investor's
  `identity-merges.json`, consumed by the base build on every
  rebuild; non-canonical rows carry `duplicate_of: <canonical-slug>`, the
  canonical carries no exclusion flag. A merge entry may pin its display name
  with `"name"`; without it the builder takes the better of the two
  renderings (the live site's, then Title Case over CAPS, then the longer),
  which on an old book can publish the acquirer or an archive spelling
  (Menlo, 2026-09-17: Chipcom became "3com" against its own ruling). The
  database upserts on (investor, name) and the name is the whole of a row's
  identity there, so a rename is a new row, not an edit. Since PRO-139
  `ingest-companies.ts` reconciles: it removes every row of the investor
  whose name the CSV no longer carries, however many that is (the 5% refusal
  was removed 2026-09-24 by Erik: a deliberate rebuild under a name rule
  renames more than that, and the reviewed list is the guard). Run it
  `--dry-run` first and read the removal list, because
  from the database a rename, a merge and a real removal look identical;
  only the base's slugs tell them apart. In-run: any suspected duplicate →
  flag + note, never a silent merge. Verdicts key on slugs and merges move
  slugs: after any change to the merge file, re-check that ledger verdicts
  still attach to the intended rows — an un-merge resurrects the twin with
  its stale seed (the a16z HP/HPE case, which shipped a wrong member).
  The build applies ledger exclusions BEFORE the identity overlay, so a
  merge whose canonical is `not_member` never runs — its duplicates
  resurface as their own unjudged rows on the next rebuild (Accel:
  2tor-inc, after 2u-inc was excluded). Every slug of a merge group needs
  its own verdict when the canonical's verdict is `not_member`.
- **A published name is the brand, in normal capitalization, with no legal
  suffix** (Erik, 2026-09-24). Per word, one test: a word read letter by
  letter keeps its capitals (IFTTT, DJI, LTSE, VSCO, AI, U.S.); every other
  word takes normal case, including a brand that styles itself in capitals
  (GOAT → Goat, DFINITY → Dfinity, AKASA → Akasa) and a word the source
  shouted (OPOWER → Opower, JAMF → Jamf). A mixed-case spelling the company
  uses stays as it is (eBay, AdMob, LeetCode). Legal suffixes go (Inc., Corp.,
  Corporation, LLC, Ltd., L.P., PBC, GmbH, AB, AG, S.A., plc): "AIRBYTE, INC."
  publishes as Airbyte, "PROGRESS SOFTWARE CORPORATION" as Progress Software.
  A misspelling carried from the source is corrected in the same edit
  (Menlo's "MAVEN LABOATORIES, INC." is Maven Laboratories). The string alone
  cannot tell `OPOWER` from `IFTTT`, so every single-word capitals name is a
  judgment per row, not a script. Measured 2026-09-24: 400 names publish in
  capitals (legal names from filings and 1990s portfolio pages 120, single
  words 280; 239 of them in books already live), and 501 mixed-case names
  still carry a suffix. Every change is a rename in `public.companies`, so a
  book applies the rule in ONE pass together with its next deliberate
  rebuild, and the ingest's removal list is read against it, never as a
  separate sweep that renames the same row twice.
- **Standing verification duties**, after the grind, before verify-clean:
  1. Web-verify every $1B+ claim regardless of source: identity and current
     status; update or downgrade.
  2. Vet every `not_graduated` against reality (invariant 7: a $1B+ or
     public row cannot be a no) and every `censored` clock (an entry now
     ≥24 months old owes a decision).
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

- **A measurement reads the MERGED view over the live base, or it is wrong**
  (PRO-135, twice in one day, by two sessions independently). A row's answer is
  `resolved.json` overlaid with `classification.json` and filtered to the slugs
  still in `base.json`, and every shortcut off that reads a real number that
  means nothing. Counting `classification.json` alone reported 554 rows with no
  entry stage when the true figure was three, because `prepare` writes the Form
  D band to `resolved.json`; the same shortcut undercounted the $1B+ rows at
  risk from an unapplied migration, because those rows carry the stage in the
  overlay and the band in the deterministic layer. Counting the file instead of
  the base is the same error one level up and is already lesson 1 below.
  Two further rules on top of the join, both learned the expensive way:
  **re-measure after the last pass commits**, not during the sweep (a count of
  seven taken mid-sweep finished at 28); and where a number will be quoted to
  anyone, print the rows, not just the total — the discrepancy between two
  sessions' counts was two named companies, and only the list found them.
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
   every ladder step) — **and only after the invention pass of §5 has been
   tried and its attempts recorded**. A layer missing because nothing was
   built in its place is not a trigger, it is unfinished work.

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
export + review.html + report; `run.py close --investor <slug>` removes the
in-flight marker (§12) as the last act before the closing commit; the
session's closing message carries the results, the open rulings and the
ingest request, and stops. Corrections
that land after an approved ingest are re-ingested only with a fresh
approval. Rows taken out of the base after an ingest are removed from the
database by the next ingest rather than left behind, so the closing message
names them and the approval covers the removals too.

Before the closing message, the review surface is verified rendered —
serve it (`file://` is blocked in the app browser; use a static server)
and check that rows render flat, the profile panel expands, and the
surface is actually reviewable. It is an exit-criterion artifact, not a
byproduct.

Every run ends in the investor's `report.md`: method deltas, results
(the S2A block in its five numbers — seed entries, censored, cohort,
graduated, rate — with what the nos rest on in the sentence, §6),
corrections taken, the flag and debt counts behind `verify`, the open
rulings raised, the usage line (§12), and the session's prompt count — the number this pipeline
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
diff at its mid-run checkpoint and then ran nine more hours, so a whole
evidence layer and every classification-phase rule went unrecorded
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
   vocabulary; every nameable row carries an `hq_city` or `city_unknown`
   (books closed before 2026-09-24 are held at their recorded count, §6
   `hq_city`); every Seed row carries a DECIDED graduation status
   (`graduated`, `not_graduated`, `censored`; PRO-132). `undetermined`
   satisfies the fill: in `valuation_range` only on an `identity_unresolved`
   row, and in `entry_stage` on any row whose round the record does not give
   (PRO-137). **A metric excludes a row only in the column the row declines to
   answer** (PRO-135). An `identity_unresolved` row reads `undetermined` across
   all three outcome columns and leaves every distribution, every rate and the
   `c2a_rate_max` ceiling. A NAMEABLE row whose round is unknown leaves the
   stage distribution and the S2A cohort and **nothing else** — it keeps its
   band, its status, its country and its place in the track record, because an
   unknown round is not an unknown company. `verify` prints the two on separate
   lines (`identity` and `stage unknown`). This was one test while the only
   undetermined row was an unnameable company. PRO-135's 1,887 nameable ones
   break it: **28 rows carry an unknown round and a $1B+ band**, and under the
   old rule every one drops out of the computed track record and all four
   distributions — not deleted from `public.companies`, but absent from every
   published figure. Twelve are in books already in the database (Lux 8 incl.
   Cognition $10B+, Lightspeed 2 incl. Meituan, Sequoia's Western Digital
   $100B+, USV's Polygon) and sixteen are latent in books awaiting their first
   ingest (Greylock 9 incl. Stryker, UnitedHealthcare and Vertex; Menlo 5 incl.
   Gilead; Benchmark 2 incl. Equinix). `recompute_investor_metrics` carries the
   same per-column split from migration `20260919180000`, **applied to
   production 2026-09-21** together with `20260919120000`, which it depends on:
   without that one the schema forced an `undetermined` stage to drag the band
   with it and would have rejected every one of these rows on ingest.
2. Source gate: a dollar figure only from an allowed source; only
   `below_1b` without a figure.
3. Public $1B+ row → cited market cap, else `cite_pending`.
4. $1B+ row → class 1/2 stage evidence (citation or filing structure), else
   `cite_pending`. And at every visibility (PRO-135): a staged row carries an
   `entry_stage_source`; a `web_verified` or `first_party` stage carries its
   citation; and a `web_verified` citation is not one shared by ten rows or
   more, which is a page about no one of them. `program_terms` and
   `first_party` may share a citation — a terms document and a listing do
   state something per row (§6) — and `undetermined` is exempt.
5. Cohort row (`graduated` / `not_graduated`) → both legs verified: a cited
   or structural entry stage, and a graduation source carrying its evidence
   (`formd` agreeing with the layer; `first_party` / `web_verified` with
   `graduation_citation`; `absence_check` only on a no). **Every no carries
   the complete absence test** (§6, PRO-132): `graduation_asof`,
   `graduation_surfaces` naming the firm's archive, the Form D sequence of a
   US company and at least two publisher surfaces, the entry past the window
   at the check and inside the coverage of what the no rests on. **Every
   decided row carries an `entry_date`.** **Exception (PRO-131 b, extended by
   PRO-132): a decided row may carry an uncited stage when its own evidence
   decides it** (a cited graduation; the filings, a cited end or the complete
   absence test for a no), flagged `stage_uncited` at
   `entry_stage_confidence: low`; those rows are counted on the `stage leg`
   line rather than failed. In flight, a no decided before PRO-132 without its
   absence test and a decided row without its date are counted as owed, not
   failed. `cohort_unverified` is not an allowed end state (retired
   2026-09-16).
6. Non-US country on a visible row → citation or formd/wikidata provenance.
   Enforced by `verify` since 2026-09-26 (PRO-156): model knowledge alone
   fails. The 125 rows in 19 books that carried it then are held in
   `shared/country-debt.json`, the city rule's ratchet: printed on every
   verify, allowed to shrink, never to grow.
7. No row ends `not_graduated` + (≥$1B or public), except a private row
   whose $1B+ mark dates within six months of its entry (the entry round set
   the mark, so no later round is implied); no `censored` row whose entry,
   read at the latest day its date can mean, is ≥24 months old.
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
11. Membership traps: no name in `config.verify.not_members` is published
    as a member (absent from the base, or present with a `not_member`
    verdict awaiting the rebuild; matched on slug or normalised name, never
    a substring), and `not_members` and `known_positions` are disjoint.
    Replaced the pre-registered trap set of the former §4 (PRO-114).

Two modes. Plain `verify` is the contract: every invariant above, full
fills, distribution guards, published surfaces current. `verify
--in-flight` runs mid-grind: invariants 2–7, 9 and 10 over every answered
row and drift (8) always, while unjudged rows, unfilled columns (Seed rows
without a graduation status among them), an expired censor clock and
`not_member` rows awaiting the rebuild are counted and reported rather
than failed, and the distribution guards wait for the full mode. A merged
run is green in flight at every milestone and green in full once, at the
end.

## 11. Investor classification (the firm profile)

Every field here answers a question about the firm, not its portfolio,
and the profile is **step 7 of the same run**: built once, after the base
has landed and the grind is complete, by the same session. Output is the
investor's `investor.json` plus `investor/sources.json`, one source entry
per field; every field populated or explicitly null, through the taxonomy
gate, onto the review surface.

**Two of these fields are READER-FACING COPY, and they keep one short shape**
(ruled by Erik, 2026-09-07, after ten of the first eleven profiles carried
provenance into the page; the shape ruled 2026-09-24, PRO-147, after the twenty
profiles ranged from a 16-word to a 301-word history; the thesis became the
firm's own statement on 2026-09-26).
`components/investor/overview.tsx` renders exactly `investment_concept` (the
thesis) and `history`; every other string is a short label or not rendered at
all. The test for both: **a reader who has never heard of Merit Capital
understands every word.**

|  | Thesis | History |
| -- | -- | -- |
| Length | 1–2 sentences, at most 25 words | at most 3 sentences, 40–80 words |
| Says | the firm's own crisp statement, in its own words | founded (year, city, founders), then the bets that made the firm, then where it stands today (latest fund or assets managed) |
| Source | the firm's own site: the homepage headline, else the title-tag tagline, else the meta description's first sentence that says what the firm does | cited facts, third person |

**The thesis is quoted, not written.** Take the line the firm itself leads
with: Sequoia's "We help the daring build legendary companies.", YC's "Make
something people want." (beside the logo), Thrive's "Thrive Capital builds and
invests in internet, software, and technology-enabled companies." (its meta
description; the homepage has no headline). The only edits allowed are
sentence case (Felicis sets "Fortune Favors The Brave", Cherry sets capitals by
CSS), straight quotes and one closing period, and the line is published
inside quotation marks (“…”) so the reader sees it is the firm speaking
(Erik, 2026-09-26). The sidecar's `source` is the
page it was read from and its `basis` says where on the page, the date read,
and any competing line the site also carries. A firm that publishes no
statement at all (Benchmark: a wordmark and two addresses) carries a derived
line, marked `derived: true` on the sidecar field and flagged in its basis,
and never in quotation marks: it is our sentence, not the firm's.

The history is written, and the model is Thrive's: founder and first fund,
the bets that made it (Instagram, GitHub, Oscar Health, Stripe, OpenAI), and
Fund X, in 56 words. The two ways to fail were Sequoia (a 16-word history) and
Khosla (four sentences and 138 words, "its book shows it", em-dashes).

Never in either paragraph:

- **This pipeline's vocabulary:** base, book, filings, member, ledger, verdict,
  "recorded / counted / shown here". Say "the portfolio" or "on this page".
- **Filing vocabulary:** CRD, CIK, EDGAR, Form ADV, Form D, "registered",
  "exempt reporting adviser", "relying adviser". These establish the firm
  boundary and are load-bearing, so they live in `investor/sources.json`
  under the `aum` and boundary bases, where the next session can check them.
- **A dash as punctuation** (em-dash, spaced en-dash or hyphen). Use commas,
  colons, parentheses or a new sentence.
- **The firm's own voice in the history** (we, our). The thesis is the firm's
  voice by design; the history is ours.

**Nothing true is dropped to fit; it moves to the sidecar.** What the page no
longer says (a fund ladder, a desk that became its own firm, entry-round
shares) is appended to the field's `basis`, so the next session can put it
back. A portfolio boundary stays readable where the reader needs it: Battery's
history says "the track record on this page covers its minority stakes only";
boundaries a reader does not need to read the numbers (Benchmark's London and
Israeli desks, Greylock IL, Dorm Room Fund, Thrive Holdings) live in the basis.

**The rule is checked, not remembered.** `scripts/profile_copy.py` holds it
(sentence and word limits, the banned words, dashes, first person in the
history, the thesis sourced from the firm's own site and in quotation marks
unless marked derived,
the sidecar mirror); `build-firm-profile.py`
refuses to write a profile that breaks it and `run.py verify` fails one.
`python3 scripts/profile_copy.py` with no slug checks all investors.

**The sidecar's `value` must mirror `investor.json`, and a placeholder is a
defect.** `"see investor.json"` in a `fields.<name>.value` breaks the field
verifier, which reads the sidecar rather than the profile; two Redpoint fields
shipped that way. A rewrite of a reader-facing field therefore touches both
files.

**`build-firm-profile.py` reads two shared-script outputs and hand-builds
nothing** (PRO-113, 2026-09-16; until then every run hand-built
`team-members.json` and `fund-formds.json` and rediscovered the same traps).
The team is `sources/site/team.json` as `site-portfolio.py` writes it: every
row carries `cms_title`, `role_bucket` (a list from the closed vocabulary
`investing | operations | platform | finance | advisor | emeritus | eir |
founder | other`), `linkedin_url` and `x_url`. The bucket is mechanical where
it can be — `site_api.team_buckets` maps the site's own group label, and a
row with no group falls to the title rules in the script — and
`site_api.team_bucket_overrides` carries the per-person judgement calls by
name. Only rows with a non-empty bucket publish; an unmapped group is the
way to keep a site's operations staff out of the profile. Socials come from
the CMS list where it carries them and from the member's own profile page
otherwise (`--no-fetch-profiles` skips the page fetch). The firm's own Form D
filings are derived at build time from the own-desk CIKs in `entities.json`
over the local bulk zips, so there is no fund file to shape. Two standing
traps: a fund entry carrying an `accession` is asserted against
`TOTALAMOUNTSOLD` on that filing and the build fails on mismatch, so a fund
whose latest Form D reports `$0 sold` must carry no accession; and the
`fields` of `investor/sources.json` each need a `value` mirroring
`investor.json`, which is what the verifier actually reads.

**`hq_location` is where the firm operates, not where it files** (ruled by
Erik, 2026-09-24, after YC's profile read Mountain View while YC runs its
batches from San Francisco). The value is the principal office on the firm's
newest Form ADV (Item 1.F), unless the firm's own site disagrees with that
office; then the site wins. The site disagrees in three cases:

- it labels a different office its headquarters;
- it lists its offices and the principal office is not among them;
- it says in its own words that the firm operates from another city. No scan
  can read that, so it is recorded by hand in `config.json`
  `profile.site_office` (`place`, `url`, `quote`, `basis`). YC's site calls
  Mountain View "the original YC office" and says each batch moves to San
  Francisco.

A site that lists several offices including the principal office agrees with
it, whatever the order: Creandum lists San Francisco first, and its ADV shows
two advisory staff there. A site that names no office leaves the ADV
standing. `scripts/firm-offices.py <slug>` reads both sources into
`sources/offices.json`: the newest ADV's principal and other offices, with
advisory staff per office, and the site's offices in page order with the
quoted text. It then writes the decision into both profile files.
`build-firm-profile.py` runs the same step, and `verify` re-applies the rule
offline to the stored record and fails when the published value differs. A
site that cannot be fetched is recorded as unchecked, never as naming no
office, and the decision refuses. The adviser is `profile.adv_crd`, else the
first CRD the `aum` provenance cites. The Form D address vote this replaces
was wrong three ways: 8VC moved to Austin in 2021 and the vote still said San
Francisco; Greylock's only address on file was a fund administrator's in
Burlington, MA; and YC's filing address outlived the office.
`python3 scripts/firm-offices.py --all --check` compares every published HQ
with a fresh read and writes nothing; it is how a firm that moved is caught.

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
the fund filer sweep in particular feeds the membership traps in
`config.verify.not_members` (§10) and belongs early.

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
  the same CRD).

  **When IAPD's search cannot find the firm, the adviser files under a legal
  name that is not the brand, and the SEC's own roster feed resolves it**
  (First Round, 2026-09-06). IAPD returns nothing for "First Round"; the firm
  reports as **FR Capital Holdings, LP** (CRD 160848). The deterministic route
  is the SEC's FOIA firm-roster CSVs — "Information About Registered
  Investment Advisers and Exempt Reporting Advisers", one zip per month, one
  for RIAs and one for ERAs — which carry CRD, SEC number, firm type, every
  Item 1 address, the 7.B fund count and gross assets, and the VC-fund flag,
  in a file that greps in a second. Match on the **Form D filing address** of
  a fund vehicle rather than on the name: the vehicles and the adviser share
  an office, and that join is exact where a name search is hopeless. Do this
  before concluding a firm has no adviser registration, and record the CRD in
  the sidecar so the next run starts from it. An exempt reporting adviser files no Item 5.F; its
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
  for current people; roles as the site presents them.
- **People's social links: the person's own, from the firm's own site, or
  none** (PRO-154, 2026-09-26). A wrong link is worse than a missing one, and
  the old read, the first X link anywhere on the member's page, put the site
  footer's firm account on 116 people (8VC 51, Lux 35, Khosla 22, Menlo 8) and
  a portfolio company's account on seven Menlo partners. `site-portfolio.py`
  (`read_socials`) now decides each link by four rules:
  - **An account named for the firm is nobody's** (`khoslaventures`,
    `Lux_Capital`, `GreylockVC`, `a16z`: `people_common.firm_handles`, plus
    `site_api.team_social_exclude`).
  - **A link the CMS row itself carries is the person's** (First Round's
    `iconLinks`, Creandum's `websiteLink` and `twitterLink`), unless the CMS
    gives the same account to two or more people (8VC filled `@8vc` for all).
  - **A link read off the member's page must name them**
    (`people_common.handle_score`: 3 first and last name or an initial of one,
    2 the last name, 1 the first name, 0 none), **and goes to nobody when a
    colleague's name matches it better**: a16z's author pages link every
    co-author, Creandum's LinkedIn pages list "people also viewed". A
    hyphenated id is read token by token and scores 0 when its first token is
    someone else's name ("anders-brenner" is not Johan Brenner).
  - A LinkedIn or X address in the row's page slot is the person's link, never
    a page to read.
  Links are cleaned to the profile address (no query string, `@`, trailing
  backslash or LinkedIn sub-path); anything that is not a profile
  (`linkedin.com/profile/view`, `/company/`) is dropped.
  A genuine account that does not match the name (Khosla's Alex Morgan is
  @genomicsdoc) goes into `site_api.team_social_overrides` by name, after a
  look; `null` there forces none. No link is guessed from a search.
  Three traps: the CMS query must ask for the link field (First Round's did
  not, so 19 people had none); a site-relative page path must be resolved
  against the site (YC's `/people/...`, never read); and a page that 404s is
  one request, not four retries. `python3 scripts/site-portfolio.py <slug>
  --socials-only` re-reads the links of the people already recorded, writes
  the per-person candidates to `sources/site/team-socials.json`, and carries
  the links onto `investor.json` and its sidecar without adding or dropping
  anyone. `run.py verify` fails a link that is not a clean profile address,
  the firm's own account, one account on two people, and a page-read link
  that does not name the person (or names a colleague better) and is not an
  override.
- **investment_range.** Three legs: the Form D entry-round distribution
  gives the median (a round-size proxy for check size — fair only for
  high-ownership lead investors, and the flag says so); program floors
  (seed-program check sizes) give the lower limit; the largest verified led
  round, cross-checked against dry powder at a 10–15% single-position
  concentration of the largest fund, gives the ceiling. Strategy
  allocations and unconfirmed aggregator claims are rejected and the
  rejections recorded in the flag.
- **notable_investments: at most five, the best known first** (Erik,
  2026-09-24, PRO-152). The base decides membership; the model decides fame,
  the one licensed use of model memory as a source: the names a general
  reader (not a VC insider) would recognise first among the firm's
  companies, in that order. The page keeps the stored order. Each name reads
  as a reader knows it, with no legal suffix or aside (§8: "Snap", not "Snap
  Inc"; "Instagram", not "Instagram (Burbn)"), and the sidecar's `slugs`
  list ties each one to its portfolio row, so the check matches on the
  company, not the spelling. `profile_copy.notable_problems` refuses more than
  five, a slug that is not a member, a name that does not name its slug, and
  a suffix; `build-firm-profile.py` and `verify` both run it. There was never
  a frontend cap: until 2026-09-26 the page showed every entry, A to Z, up to
  Redpoint's 33.
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
  rasterize at 2× the master before downsampling. Two **resolution rules**
  (Thrive, 2026-09-05: the issue's icon pointer was the site's 32×32
  favicon, the contain-fit resize enlarged it 8× and the published master
  was a blur — and the fetch log said "source 256x256" because it measured
  the canvas, not the file; Accel had hit the same trap in June and was
  fixed by hand): **raster artwork is never enlarged** (`MAX_UPSCALE`
  1.05: the artwork's pixels in the master may not exceed its pixels in
  the source; the fetch refuses and names the enlargement), and **the
  master's edge ramp must stay under 2 px** (`MAX_RAMP`: partial-coverage
  pixels per perimeter pixel — every crisp published icon measures
  0.5–1.1 px, the upscaled Thrive master 5.9 px — which also catches a
  source that arrives pre-blurred). **Choose the source by measurement**:
  `--discover <site-url>` lists every icon-sized asset the site declares
  (`<link rel=icon>`, apple-touch-icon, manifest icons, og:image, logo
  `<img>`s, inline logo SVGs) with intrinsic sizes and a verdict; take the
  vector or the largest raster, never the first favicon. Every publish
  writes **provenance** into `investor/sources.json` (`fields.icon_url.
  provenance`: source URL, format, intrinsic size, artwork pixels in
  source and master, scale, ramp), and `--allow-upscale` is the only way
  past the rules — logged in that provenance. `--plate <colour>` overrides
  the synthesized background, `--dry-run <file>` previews without
  uploading, and **`--audit` replays the current rules against every
  published icon**, reading the ramp off the master and the scale off the
  provenance — run it when a rule changes, so icons that predate it are
  found rather than assumed fine. The DB still only changes on ingest.

- **A site's declared assets may all be unusable while the real mark is
  inline in the page, and it may be more than one element** (Lux,
  2026-09-06). Lux's shortcut icon was 32×32 (would be upscaled) and its
  apple-touch webclip measured a 6.09 px ramp (pre-blurred), so `--discover`
  offered nothing publishable — while the mark itself shipped as inline SVG
  in the markup. It shipped as **two** elements: `.logo_embed` (the angled
  "Lu") and `.logo_embed-x-char` (the red cross standing in for the X, sized
  47.875% and pinned top-right by the site's own CSS). Taking the first alone
  publishes half a logo. So when the declared assets fail, read the page
  source for the logo elements and compose them at the geometry the site's
  CSS gives, keeping the composed file under `sources/site/`.
- **The edge ramp is measured per ink, so a two-colour mark is not read as
  blur** (Lux, 2026-09-06). `MAX_RAMP` normalized every pixel's deviation
  from the plate by a single "full ink", so on a two-ink logo the second
  colour fell inside the partial band and counted as anti-aliasing: the Lux
  mark measured 5.45 px while being pixel-crisp (the same geometry filled
  black measured 0.87 px). The metric now discriminates on **flatness, not
  colour count** — quantize the non-plate pixels, keep bins holding ≥10% of
  them, and treat those as ink only when together they cover ≥60% of the
  artwork. A flat multi-ink mark clears that bar (Lux: 87% of its mass in two
  bins); a blurred or upscaled source does not (the same mark blurred: 20% in
  its largest bin) and falls through to the single-ink path unchanged. Verify
  any change to this metric the way that one was: `--audit` must leave every
  published icon's ramp identical, and a deliberately blurred master plus a
  32 px master enlarged 8× must both still refuse.

- **A non-US office publishes as "City, Country"** ("Berlin, Germany",
  "Stockholm, Sweden"): `firm-offices.py` takes the country from the Form ADV
  address and strips a " - <district>" suffix from the city. This replaces
  the Form D state-slot codes (V7 for Sweden) the old address vote had to
  map (Cherry, Creandum).
- **An ERA whose ADV lags the fund ladder anchors only the bottom.** Cherry's
  2024 Section 7.B ($905.7M across Funds III, IV and the web3 sleeve)
  predates Cherry V ($500M, 2025); the top took the only credible press
  figure ("around $1 billion"), and the sidecar says why the sworn number
  is a floor. Feeders (Fund III (US) / IV (US) L.P.) are described in the
  funds basis, never listed beside their master KGs.
- **Comma-joined site tags** ("Industry, SaaS, AI") are split by the
  profile's focus recompute into single words, so the crosswalk must carry
  the words as well as the phrases, or the recompute reports them unmapped.
- **Focus recompute needs representative tags.** A base-derived focus
  distribution publishes only when sector tags cover ≥25% of base rows;
  below that the tagged slice describes whichever surface carried tags,
  not the firm (a16z: only the accelerator's 251 rows carried tags, and
  the recompute had published an empty focus list). The firm's own sector
  enumeration stands until coverage clears the bar
  (`build-firm-profile.py` enforces this).

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

## 12. Running investors in parallel

Several investors may collect at once on one machine, each in its own
session, all on the shared `main` checkout — the shape every parallel run so
far has used. A worktree per investor is the fallback for a session that
must edit scripts, or if git contention shows. What makes the shared
checkout safe, and the etiquette that keeps it safe:

- **One investor, one session.** `record` is a read-modify-write on the
  ledger and classification files; two sessions on the same investor lose
  updates. A session never touches another investor's directory.
- **The in-flight marker.** `prepare` writes `scratch/in-flight.json` (slug,
  start, pid, branch); `run.py close --investor <slug>` removes it as the
  last act of the run, after export, review and report and before the
  closing commit. `verify`'s cross-investor section does not compare an
  investor whose marker exists, so a half-done sibling never fails another
  run's verify; alignment happens once per wave (below). A forgotten `close`
  is loud: every sibling's verify prints the skip note by name.
- **Shared caches are appended, never rewritten**, and every writer goes
  through `write_atomic` (`scripts/paths.py`): a reader in another session
  sees the old file or the new one, never a torn one. A failed SEC or
  Wikidata fetch is never cached as an empty answer: `prepare` leaves those
  rows open, exits 3 and says to re-run.
- **One budget per external service.** `scripts/shared_throttle.py` paces
  SEC (8 requests per second), the Internet Archive (1) and Wikidata (0.67)
  across every process on the machine through lock files in
  `~/Library/Caches/merit-capital/locks`. No session raises a rate
  (`MERIT_<SERVICE>_RATE` exists for lowering one). Long pulls
  (`wayback-pull.py`, `run.py collect`) start in the background in a
  run's first minutes so the wave's I/O serializes early.
- **Git etiquette on the shared checkout.** A collection session commits
  only with an explicit pathspec of its own investor directory
  (`git commit -- data/collection/investors/<slug>`), never `git add -A` or
  `commit -a`, never `stash`, `checkout`, `rebase` or `pull` (each rewrites
  the tree under the sibling), and retries once on a transient
  `index.lock`. `scripts/`, this playbook, `.claude/launch.json` and
  `data/collection/cross-investor.json` are edited only by the designated
  tooling session; a fix needed mid-wave is requested by session message
  and lands between phases. Main stays linear, so pushes are
  fast-forwards; nothing pushes to origin from another clone during a wave.
- **Cross-investor rulings** go in the investor's own `cross-rulings.json`
  (same schema as the shared file: `distinct`, `accepted`, `same`); `verify`
  merges them at read time. The shared file is written only at alignment.
- **Review surface.** One server, the `review-surface` launch entry on 8931,
  serves every slug at `/<slug>/companies/review.html`.
- **Alignment once per wave**, on main, after every session in the wave has
  closed: the cross-investor invariant over all published bases, the stale
  side aligned and re-exported, the wave's playbook write-backs landed once,
  then the ingest requests.
- **Wave etiquette.** Kickoff order by base size, starts about two hours
  apart. Each report carries a **usage line**: the account's weekly and
  Fable percentages read before kickoff and at close, and the base rows, so
  cost per company is measured rather than assumed. A session that hits the
  five-hour session limit parks in a cheap phase and is nudged when the
  window resets.

Deferred by decision (2026-09-05), so a cold session does not invent them:
the bounded-context grind (judging batches in fresh subagents), a model mix
by phase, extra-usage credits, a second machine, a worktree per investor.
They are revisited on the measured usage lines of the first two-session
wave.
