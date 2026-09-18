# Greylock Partners — collection run (PRO-89)

One session, one run, 2026-09-07. **561 members, `verify` clean in full mode**,
107 rows in `excluded.json`, profile built, review surface rendered.

| | |
|---|---|
| Members | **561** — Tier A 457, B 96, C 8 |
| Excluded | 107 (`not_member`), preserved in `excluded.json` |
| Entry years | 1967–2026; **309 of 548 dated rows are pre-window** (56%) |
| Status | acquired 330 · private 126 · defunct 65 · public 34 · unknown 6 |
| Visible slice | 43 rows at $1B+, 26 at $10B+, 11 at $100B+ |
| Entry stage | Series A 421 · Seed 79 · Growth 60 · Pre-Seed 1 |
| C2A | 34 in cohort, 33 graduated, 97.1% |
| AUM | $10,469,154,000 — ADV Section 7.B composite, 13 funds, filed 2026-03-31 |
| Prompt count | **1** so far (kickoff). The ingest decision is the second. |

## Phase 0: no delta reached Erik

All three of PRO-89's delta candidates resolved under a standing test against
verified facts, so each is a derivation. The issue's Israel question is the
Lightspeed India pattern exactly: **GREYLOCK ISRAEL GLOBAL MANAGEMENT LTD. holds
its own exempt-reporting registration (CRD 162176, SEC file 802-75092)**,
separate from the home adviser's CRD 161537, and 83North holds two more. The
firm's legal name is **Greylock Management Corporation**; it is an ERA, not an
RIA, so Section 7.B is the sworn AUM rather than Item 5.F.

## What this run had to invent

**Both capture archives were down at once.** The Internet Archive flapped
between connection-refused and answering for the run's whole first half, and
`index.commoncrawl.org` never answered at all — so the archive layer, which on a
1965 firm carries the entire book, had nothing behind it.

`data.commoncrawl.org` stayed up. The query API is only a front end over files
that live there, so `scratch/cc-direct.py` binary-searches `cluster.idx` by HTTP
byte range and inflates the `cdx-000NN.gz` blocks directly: the same index,
without the API. 126 crawls, ~19,000 captures, about two dozen range requests
per crawl.

What that bought, none of it reachable otherwise at the time:

- the **2013 and 2014 list pages** (253 and 258 rows) — two years the Internet
  Archive gave nothing for;
- the **2015 listing**, recovered as an id enumeration joined to the Rails name
  map;
- the **2018–2021 logo wall**, read through the firm's own upload filenames;
- and the largest single win, the **2011–2014 Rails per-company partials** —
  270 of them, each a ~600-byte fragment carrying the name, the sector, the
  website, the OUTCOME LINE ("Merged with Creative BioMolecules in 2000") and
  the **Greylock partner on the deal**.

## What the partner attributions then fixed

`partner-roster.py` builds tenure from the years a person's profile page was
captured. On this firm that is wrong by decades in **both** directions: Greylock
publishes its founders as "Emeritus", so Bill Elfers — who co-founded the firm
in 1965 and died in 2016 — read `first_seen 2022`, while partners who left years
ago read `last_seen 2026` because an alumni page is still crawled.

The firm publishes a better witness. Its own listings name the partner on each
company and the year it funded, so a window is bounded below by the earliest
deal the firm attributes to a person and above by the latest capture that still
does: **Dan Gregory from 1967, Charlie Waite 1968, Henry McCance 1973, Howard
Cox 1974, David Strohm 1981, Bill Kaiser 1986, Bill Helman 1987, Roger Evans
1989**. That is evidence, not memory.

With real windows the ex-partner rule fires correctly for the first time on this
run: **15 rows removed**, and every one of them is right — David Aronoff's
Flybridge book (BetterCloud, BitSight, Calxeda, NSONE, NetBox Labs, ValiMail),
Tom Bogan's post-Greylock board seats (Catapult, Reltio) and two Erez Ofer rows
that belong to 83North. The union also recovered nine partners the current site
no longer lists — Charles Chi, David Aronoff, Tom Bogan, Adam Nash, Erez Ofer,
Moshe Mor, Yoram Snir, Simon Rothman, Donald Sullivan.

## The calibration gate refused the firm's own entry-round field

Greylock publishes `firstPartnered` per company — apparently the round it
entered at, for 157 of 158 live rows. Scored blind on the pre-registered stage
key it is **12/17**, and the misses are one class:

| The site claims | Score |
|---|---|
| Series B or later | **6/6** |
| Series A | **4/4** |
| **Seed** | **2/7** |

Where Greylock was the first institutional money the field reads "Seed" whatever
the record calls the round — AppDynamics' $5.5M Series A (2008), Sumo Logic's
$5.8M Series A (2010), TellApart's $4.75M first round (2010), Abnormal's $24M
Series A (2019, and the issuer's *first* Form D is that Series A, so no earlier
priced round exists to rescue the label). It fails by two buckets in the other
direction on **Cribl**, which Greylock entered at the **$200M Series C** in
2021, four years and three leads after CRV's actual seed.

So the field is not a round name; it is the firm's own sense of how early it
felt, and it is safe only in the direction where feeling early is not the claim.
Ruled class 1 for a Series-B-or-later claim, corroboration only otherwise
(decisions.md **R2**) — which put 116 of 158 live rows through the record
instead.

Two further layers scored:

- **The announcement archive is refused outright.** Creandum's finding was that
  a firm's own announcements are a class-1 entry-stage layer; Menlo's was that
  this inverts where the firm leads later rounds into companies it seeded
  quietly. Greylock is a third case: the posts name **no round and no amount**.
  "Our Investment in Rubrik", "…in Discord", "…in Coinbase" were read in full;
  all are thesis pieces. Only ~14 of 207 posts are announcements and the archive
  begins in 2015. It stays as dated membership evidence and a `first_seen`
  ceiling (**R3**).
- **The archived year-funded column is class 1 for `first_seen`** — 456
  companies carry the firm's own investment year, back to 1967.

One honest correction to the gate itself: the `handshake` key row was written
against Joinhandshake, the campus-recruiting company, while Greylock's Handshake
is handshake.org, the naming protocol. Caught and corrected in `golden.json`
before the grind, under §4's rule that a golden label can itself be wrong.

## Two traps that would have published false members

**The acquirer-mark trap arrived through a COLUMN ORDER.** Era 1's
`/company/mergers_page1.htm` runs `logo | company | YEAR | ACQUIRER`, while every
other page in that era runs `logo | YEAR | company | product | status`. The era
pattern takes the cell after the year — so on this one page it harvested **45
buyers as portfolio rows**: ADP, Cisco, IBM, Lotus, Lucent, Pfizer, Siemens, Sun
Microsystems, Westinghouse, US West. That is COLLECTION.md §5's First Round
acquirer-mark class arriving through a column order rather than a logo wall.
Fixed in the pattern — and the fix **recovers Continental Cablevision**, the
firm's most famous early position and the one name `verify`'s known-positions
list flagged as missing.

**The people namespace mixes investors with an EIR directory.** Greylock's
`/team/` carries twelve Executives in Residence who are operators at other
companies — Nir Zuk of Palo Alto Networks, Jeff Weiner of LinkedIn, Glenn Kelman
of Redfin, David McJannet of HashiCorp — plus five ungrouped operations names
the site's own `category` field leaves empty, which `roster.site_team_groups`
therefore cannot see. Left in the sweep, John Delaney confirmed Alliance
Partners LLC and Julie Smith confirmed Carbon Health and e-Scape Bio, each on a
common-name match with filing-grade-looking evidence. Excluded by name.

## Nine rows never reached the judge at all

The deterministic layers filled every column at the first `prepare`, and the
queue asks only about empty fields — COLLECTION.md §8's Black Forest Labs class,
found here by a `focus` audit rather than by the stage check. The nine were
**Palo Alto Networks, Workday, Discord, Nextdoor, Aurora, Cresta, Pure Storage,
SiTime and Instabase**, and two of them were rows the golden key had already
answered:

- **Palo Alto Networks** published `Growth` off the 2008 $37M band, against a
  **$250K seed check in 2005**;
- **Workday** the same, against Greylock leading its first institutional round
  in 2005;
- **Aurora** and **Cresta** published `Growth` against **Series A** entries the
  firm itself announced (Feb 2018 and Feb 2020).

All corrected with `stage_disputes_band`.

## Recall probe

The probe settled a boundary rather than finding rows. Every European and
Israeli name the Wikipedia insource sweep surfaced — Wonga, Socialpoint, Wanova,
Celonis, hybris, MySupermarket, Betable — belongs to **Greylock IL**, the 2011
"$160M fund for Europe and Israel" that cut its ties in January 2015 to become
83North. That is R5 confirmed from outside the firm's own filings. Ten further
candidates are recorded rejections with reasons in
`sources/web/recall-probe.json`; one addition, Continental Cablevision, landed
mechanically at the rebuild.

The exit-side EDGAR full-text sweep returned 268 registrants (158 with
issuer-type forms) and the Form D roster sweep 389 accessions across 185
issuers; both fed the base rather than the probe.

## Cross-investor alignment

194 shared rows, **187 agree, 7 accepted, 0 disagree**. Ten were aligned on this
side because the sibling was better evidenced — including **Chronosphere to
`acquired`**, which Lux and Spark both carry and Greylock's own current field
also says, against my knowledge cutoff. Twenty are name collisions ruled
`distinct`, and one of those had already cost this run a figure: **a16z's
Clubhouse is the audio app; Greylock's is the project tracker that became
Shortcut**, and the aggregator had put a $4B mark on the wrong row until the A/B
pass caught it. Seven pairs where this run's reading is the better one are
listed in `cross-rulings.json` for the wave alignment (Lytro, T-Networks,
Remotion, Redfin, Abnormal, Gowalla, Tidemark).

## Debt behind the clean verify

| Flag | Rows | What it means |
|---|---|---|
| `pre_window_entry` | 301 | pre-2006 entry: stage at low confidence, graduation null (§1) |
| `cite_pending` | 38 | stage or market-cap citation queued |
| `cohort_unverified` | 33 | C2A graduation not verified on both legs |
| `identity_uncertain` | 23 | company not resolved on the record |
| `needs_web_value` | 17 | private row believed sub-$1B, check recorded |
| `model_disputes_source` | 6 | a deterministic value overruled with a note |
| `stage_disputes_band` | 6 | the Form D band overruled by the record |
| `country_conflict` | 5 | includes the two rows below |
| `stage_uncited` | 2 | citation attempted and failed |

**The pre-window share is the rule working, not a gap.** 309 of 548 dated rows
entered before 2006. Their `entry_stage` carries the best-supported label at low
confidence behind `pre_window_entry` rather than a null — the constant Erik set
on 2026-09-07, which supersedes the "entry_stage and graduation null" text in
PRO-89 itself. No row in this base fails invariant 1 on that account.

**`defunct` is undercounted, as §6 says it must be.** 65 of 561 rows read
defunct (12%), which is high for this pipeline precisely because the firm's own
1999–2014 listings state outcomes; but quiet shutdowns in the 1990s book still
present as `acquired` or `unknown`, and no mortality rate may be read off the
column.

**The C2A rate of 97.1% is restated, not waived.** 79 rows entered at Seed and
only 34 are in the cohort — the rest are censored, under 24 months from entry
with no resolution. What survives that filter on a book whose seed entries are
dominated by 2020–2025 AI companies that all raised an A within a year is almost
entirely graduations. `verify.shape.c2a_rate_max` is set to 0.98 with that
reasoning in `config.json`. Published honestly: *of the seed entries where the
record could be established, ~97% graduated; the establishable set skews toward
visible successes, and more than half the seed book is too young to be in it.*

## Open rulings for Erik

1. **AI Fund** is listed on greylock.com/portfolio with no entry round. It is
   Andrew Ng's venture studio and fund — fund-shaped under T5. Published as a
   member with `identity_uncertain` and raised here; confirm and it leaves the
   base.
2. **Arista and ServiceNow** are recorded by the firm as **"Common Stock"**
   entries, not rounds. This run reads a pre-IPO purchase of existing shares as
   a venture entry at scale (T3), so both publish as Growth with no nameable
   round and `stage_uncited`. Same shape as Accel's open `arista` ruling.
3. **Superhuman Platform Inc.** — a 2026 filing reporting **$1,022,429,310
   sold** with Reid Hoffman as Director of record. The issuer does not resolve
   and no Greylock announcement carries it, so the narrowing of the
   director-of-record pattern makes it `not_member`. Flagged because of the size.
4. **Intel, 3Com, Conexant and UnitedHealth** reach the base only through fund
   filings dated after those companies bought a Greylock portfolio company —
   the sale-consideration pattern (§1). Each is flagged `identity_uncertain`
   with the acquired company named; they should probably leave the base.
5. **Four ISO codes are missing from `run.py`'s table**: BM, GI, KY, VG. Mutual
   Risk Management (Hamilton, Bermuda) and Xapo (Gibraltar) carry
   `country_conflict` and their true domicile in the note rather than a null
   that would fail invariant 1.

## Method deltas proposed for COLLECTION.md

1. **When both capture archives refuse, read the Common Crawl index off its data
   host.** `index.commoncrawl.org` is a front end over `cluster.idx` and the
   `cdx-000NN.gz` shards on `data.commoncrawl.org`; a binary search over byte
   ranges answers the same query. Add to §5 beside the CDX-outage replay path.
2. **A firm's own listings are a roster instrument, not only a company list.**
   Where the listings name the partner per company and the year funded, tenure
   windows come from the deals the firm attributes, which beats the
   capture-window proxy by decades on an old firm — and an "Emeritus" section
   breaks that proxy in the opposite direction from First Round's. Add to §8
   beside the two-spellings rule.
3. **The acquirer-mark class has a second shape: a column-order inversion inside
   one era.** Add to §5's First Round paragraph.
4. **A site's stated entry round can fail in ONE bucket only.** Greylock's is
   6/6 at Series B or later and 2/7 at Seed. The gate should score a stage layer
   *per claimed value*, not once overall — a single accuracy number would have
   published this layer at 71% and taken the Cribl error with it. Add to §4.
5. **The Black Forest Labs class needs a `focus` audit too.** Nine rows here
   were fully pre-filled and never queued; the stage check in §8 would not have
   caught them because their stage was pre-filled as well. A cheap standing
   check is "any base row with no judged key at all".
6. **A firm may CODE its funds in Form ADV.** Greylock's Section 7.B names every
   fund "9.1", "FUND 3.2" — rule 204-2(d), which Part 1A expressly permits. 7.B
   still anchors AUM but contributes nothing to the fund table. Add to §11's AUM
   recipe.
7. **`build-firm-profile.py` derives `hq_location` from whichever fund Form D
   carries an address**, which on a firm whose only recent filing is an
   administered SPV gives the administrator's town (Burlington, MA here). It
   should prefer the ADV Item 1.F principal office.

## Usage line

Not recorded. §12 asks for the account's weekly and Fable percentages read
before kickoff and at close; this session did not read them at kickoff and will
not invent them. The measurable costs it can report: **~30 web searches** of the
200-call budget, ~19,000 Common Crawl index entries read over ~3,000 HTTP range
requests, and roughly nine hours wall-clock, of which the first two were spent
working around two simultaneous archive outages.

## Addendum 2026-09-17 — S2A re-judged under the status contract

`seed_to_a_graduation` became a judged status (`graduated | not_graduated |
censored | undetermined`, COLLECTION.md §6), superseding the C2A figures
above. `migrate-graduation` dropped 45 legacy values with their 34
`cohort_unverified` flags; the 79 re-opened Seed rows were judged in two
batches with both legs cited in the same pass.

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|---|
| 71 | 10 | 22 | 39 | 37 | 0 | 94.9% | 64% |

Of 71 seed entries, 10 were too recent to count; of the 61 whose record could
be sought, 39 were established (64% coverage) and 94.9% of those graduated.
**No row could be decided as a "no"** — on a book whose seed cohort is
dominated by 2020–2025 AI companies, a company that has not raised again is
usually still operating rather than dead, and the contract will not call that
a failure without a cited terminal event. That is the honest shape: this rate
measures which seeds are known to have graduated, not what share of the book
succeeded. The 22 undetermined are mostly companies with no round on the
public record at all.

Two rows left the cohort (Upwind re-staged to Series A, Workday flagged
pre-window) and Wisetack's entry date moved to its 2019 seed; three identity
questions and two citation traps are written up in D-S2A. `verify` is clean
apart from the pre-existing `ai-fund` membership trap, which is Erik's to
rule.
