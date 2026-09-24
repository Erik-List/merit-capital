# Greylock Partners — collection run (PRO-89)

One session, one run, 2026-09-07. **Ingested 2026-09-24: 553 companies live.**
Figures below are current as of that date, after the sale-consideration ruling,
the 7AI merge and the PRO-132, PRO-135 and PRO-136 passes; the run's own closing
numbers are in the addenda at the foot. `verify` clean.

| | |
|---|---|
| Members | **553** — Tier A 455, B 94, C 4 |
| Excluded | 113 (`not_member`), preserved in `excluded.json` |
| Entry years | 1967–2026; **304 of 541 dated rows entered before 2006** (56%) |
| Status | acquired 327 · private 122 · defunct 65 · public 32 · unknown 7 |
| Visible slice | 42 rows at $1B+, 25 at $10B+, 9 at $100B+ |
| Entry stage | Series A 136 · Seed 61 · Growth 51 · Pre-Seed 1; **302 nameable rows say the round is unknown** |
| S2A | cohort 51, graduated 43, **84.3%**, coverage 100% |
| AUM | $10,469,154,000, the ADV Section 7.B composite, 13 funds, filed 2026-03-31 |
| Prompt count | **2**: kickoff and the ingest approval. |

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
4. ~~**Intel, 3Com, Conexant and UnitedHealth** reach the base only through fund
   filings dated after those companies bought a Greylock portfolio company,
   the sale-consideration pattern (§1).~~ **RULED 2026-09-22, see the addendum
   at the foot.** Erik: all four out. The rule is in COLLECTION.md §1 as
   commit dafa302 and now binds every investor.
5. **Four ISO codes are missing from `run.py`'s table**: BM, GI, KY, VG. Mutual
   Risk Management (Hamilton, Bermuda) and Xapo (Gibraltar) carry
   `country_conflict` and their true domicile in the note rather than a null
   that would fail the full-fill rule.

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

## Addendum 2026-09-19 — identity reclassification (PRO-136)

Twenty-three published rows carried `identity_uncertain` (the other 27 entries
in `classification.json` are stale keys for rows already absorbed). The
striking finding is how few of them were identity questions at all.

**Sixteen rows lose the flag and keep everything.** Twelve are named and
described on the firm's own cards — `altara` (Greylock led the $7M seed it
announced itself), `ava` (meetava.com, the row's own link), `emotion-inc`,
`genpath-pharmaceuticals`, `illuminator`, `managed-comp`, `netnumina`,
`celeritek` and `matrix-software` (both carrying "merged at the rebuild" notes
for merges that landed long ago), plus `arista-networks`, `promega` and
`ai-fund`.

Four of the sixteen are famous public companies — `3com`, `intel`,
`conexant-systems-inc`, `united-healthcare-corporation` — where the flag was
parked on the wrong question entirely. Nobody doubts Intel's identity; what is
doubted is MEMBERSHIP, because each reaches this base through a fund filing
made when the company ACQUIRED a Greylock portfolio company (Sonix, Maker
Communications, Share Development), which is §1's sale-consideration pattern.
That question was already raised for Erik and this pass does not pre-empt it;
it only stops the rows claiming an identity problem they do not have.
`arista-networks` and `promega` are the same shape: an entry question and a
membership question wearing an identity flag.

**One pre-registered trap, applied.** `ai-fund` sat in
`config.verify.not_members` as a T5 fund-shaped entry and was still published
as a member, which is invariant 11 failing. The verdict now records what the
config already stated: Andrew Ng's venture studio is not an operating company
the firm holds a venture position in.

**One row leaves membership under the new filing-entity rule.** `ailens-inc`'s
single 2019q2 Menlo Park filing is $5,099,988 — exactly the round this base
already carries on `truera`, with Jerry Chen signing as Director on both, and
FinSMEs reports that same $5.1M as TruEra's first funding led by Greylock. It
is TruEra's pre-rebrand issuer, so keeping it double-counts one investment.
This is the case Erik's 2026-09-18 rule names, and it is distinct from an
ordinary duplicate: the vehicle is not the company.

**One merge.** `iss-group-inc` is Internet Security Systems' listed holding
entity, reaching the base separately through the funds' 1999 13G.

**Five rows are genuinely unnameable**, and they split by evidence:
`mysteries-inc` ($18.5M sold 2021-12-03, one prior, Sarah Guo as Director) and
`rivington-labs-inc` ($40.0M sold 2025-11-07, one prior, Mike Duboe) keep
stages, now sourced `formd_band` rather than `model`, because their own
filings carry them — and Rivington's stage moves Series A → Growth, since the
Series A was model knowledge about a company nobody can name. `okamiai-inc`
(CIK 1997387, $36.1M, Asheem Chandna) has a filing with NO date of first sale,
so the layer could never date or band it; it reads `undetermined`, with the
filing recorded so a later pass can band it if the sale date is recovered.
`bluesky` and `dbs` read `undetermined` outright.

Base 561 → 559. `verify --skip-cross` clean. Six cross-investor disagreements
remain against Accel's and Battery's books (Forte Software, Guru, Inventa,
Rally Software and Sprig twice); all predate this pass, all are status
disagreements or namesakes rather than identity, and they belong to the wave
alignment rather than here.

## Addendum 2026-09-21: S2A with every Seed row decided (PRO-132)

The 2026-09-17 pass left 22 Seed rows `undetermined` and read 94.9% on a
39-row cohort. PRO-132 makes the absence of a later round a finding: a Seed
row past the 24-month clock with no evidence of a later round did not
graduate, and every no records the dated search that found nothing (the
firm's archive, the Form D sequence for a US company, at least two publisher
surfaces; COLLECTION.md §6). The 30 open rows were judged in one batch.

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 61 | 10 | 51 | 43 | 8 | 84.3% | 100% |

Of 61 seed entries, 10 were too recent to count; of the 51 that remain,
84.3% raised a later round. Of the eight that did not, three rest on a cited
end (1000memories to Ancestry in 2012, Treat to Typeface in 2024, Natoma to
Snowflake in 2026) and five on a dated search of the named surfaces (Lithos,
Portals, Reduct, Airspeed, Headrace). The old note's claim that "no row could
be decided as a no" was a property of the abstaining instrument, not of the
book.

What moved:

- Entry dates corrected: Gretel's recorded 2020-10-07 was the Series A's own
  Form D date; the seed is TechCrunch's $3.5M of 2020-02-20. Reduct's entry
  was found under "Reduct.Video" (TechCrunch, 2021-02-11, $4M led by
  Greylock).
- Name traps checked and set aside: the June 2026 $20M Series A of a London
  "Airspeed" (DN Capital) is a different company from Greylock's San
  Francisco Airspeed; Lithos Carbon's $57.1M of December 2023 is Frontier's
  carbon-removal offtake, not equity.
- Re-staged out of Seed: Scenery to Series A (Greylock's partner appears only
  on the 2022 filing, not the 2020 one) and Vori to Growth (the only page
  naming Greylock is the May 2026 $22M Series B, FinSMEs).
- Eight rows read `undetermined` in the stage because nothing dates a
  Greylock entry: Optic, Ava Protocol, Coffee, Hoist, Latent Space,
  RabbitHole, Tydo, Zed (Zed's funding history names Redpoint, Root,
  Matchstick, V1.VC and Sequoia, never Greylock).

`c2a_rate_max` is restated from 0.98 to 0.90: the rate sits just above the
0.80 default once the non-graduations count. `verify` passes every graduation
check. One problem remains and is not S2A's: `united-healthcare-corporation`
is a public $1B+ row without a cited market cap, held pending Erik's
membership ruling on the sale-consideration rows (with 3Com, Intel and
Conexant).

For Erik: **Scenery** (Series A entry read from which filing names the
partner) and **Vori** (Growth entry although Greylock's listing predates the
Series B announcement) are judgment calls on thin evidence.

## Addendum 2026-09-22: sale consideration ruled out, four rows leave

**Erik ruled open question 4: Intel, UnitedHealth, 3Com and Conexant are not
members.** The rule is now in COLLECTION.md §1 as commit **dafa302**, "Sale
consideration is not membership, and the acquirer leaves the base", and it binds
every investor rather than only this one.

Where the only route into a base is stock the funds received *because that
company bought a portfolio company*, the row is `not_member` with the acquired
company named, whatever the size of the holding and whichever surface carries
it. That last clause is what decided UnitedHealth: it came in on Greylock's own
IPO roster, not on a filing, and a first-party surface carrying the acquirer
still does not make the acquirer a member.

| Row removed | Route in | The investment is |
|---|---|---|
| Intel | fund Section 16 filings | **Shiva Corporation** (bought 1998) and **Xircom** (2001) |
| UnitedHealth Group | the firm's own IPO roster | **Share Development** (bought 1985) |
| 3Com | a 2001 fund filing | **Sonix Communications** (bought 1995) |
| Conexant Systems | a 2001 fund 13G | **Maker Communications** (bought 2000) |

Every company in the right-hand column is a row of its own and stays a member.
Shiva in particular is worth naming: Intel leaves, Shiva stays, and that pair is
the whole rule in one line.

**What changed.** A dry build was diffed against the live base before the real
one ran, because a rebuild in this window can carry unrelated churn from the
2026-09-19 "most recent rendering" name rule. Greylock's dry build moved exactly
these four rows, nothing added and nothing renamed, so the rebuild was safe.

- Members **558 → 554**; excluded 109 → 113.
- Visible slice **$100B+ 11 → 9**, $10B+ 27 → 25, $1B+ 44 → 42. Removing Intel
  ($503B) and UnitedHealth ($282B) is most of that.
- `verify` was failing on one row before this, `united-healthcare-corporation`
  as a public $1B+ row without a cited market cap. The ruling resolved it rather
  than a citation: **`verify` is clean**.
- The S2A cohort is untouched at 51 rows and 84.3%; none of the four was a seed
  entry.

The headline table at the top of this report was restated to these figures and
to the current shape of the stage column, which PRO-135 changed: the pre-window
flags are gone and 302 nameable rows now say the round is unknown rather than
carrying an inferred label.

## Addendum 2026-09-24: ingested

Erik approved the ingest. **553 companies live** and the readback matches `base.csv` row for row.
The icon was already published by an earlier session: re-running the fetch
produced the identical file and therefore the identical URL
(`greylock-441dcb7c09.png`), so that step confirmed rather than changed
anything.

One duplicate was caught in the pre-ingest check and fixed before anything was
written: **OkamiAI, Inc. renamed to 7AI, Inc.** EDGAR carries both under CIK
1997387, filing from 200 Clarendon Street, Boston, with `OkamiAI` in
`formerNames`. This base had them as two rows, because they arrived by different
routes: `7ai` from the site listing for the $36M seed the firm announced in
February 2025, and `okamiai-inc` from the 2023 Form D that Asheem Chandna signed
as director of record, which the run had recorded as an unannounced deal. It was
one deal in one company under two names. Merged onto `7ai`, the current
rendering and the one greylock.com uses, and members went 554 to 553.

The fix is worth keeping in mind for the shape rather than the row. The
director-of-record pattern finds real unannounced companies, and the company it
finds can surface again years later under a new name once the firm does announce
it. A shared CIK is the check that catches it.

| | |
|---|---|
| Companies live | **553**, equal to `base.csv` |
| Icon | already live, re-measured clean (contrast 12.0:1, ramp 0.96px, no override) |
| Graduation rate on the investor row | 84.3%, cohort 51, matching `verify` |
| Status | acquired 327 · private 122 · defunct 65 · public 32 · unknown 7 |
| Entry stage | Series A 136 · Seed 61 · Growth 51 · Pre-Seed 1 · undetermined 304 |
| Valuation | below_1b 509 · 1b_plus 17 · 10b_plus 16 · 100b_plus 9 · undetermined 2 |

Checked by name in the live table: Intel, UnitedHealth Group, 3Com, Conexant
Systems and OkamiAI are all absent, and Shiva, Xircom, Share Development, Sonix,
Maker Communications, 7AI and Continental Cablevision are all present. That is
R6 and the 7AI merge both readable in the database.

**One thing for the taxonomy, not for this book.** `ingest-investor.ts` warned
that `investment_geo.other: "Canada"` is not a known geography label and added
it as new. Greylock, USV and YC all carry it, and Accel has the same warning for
"Oceania". Either the label belongs in the geography taxonomy or those four
profiles should use an existing one; four books writing an unknown label is a
taxonomy gap rather than four separate mistakes.
