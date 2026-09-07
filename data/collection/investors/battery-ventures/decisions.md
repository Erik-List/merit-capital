# Battery Ventures — investor-specific decisions

Investor-specific rulings for `battery-ventures`, derived from the standing
rule set in `data/collection/COLLECTION.md` §1 (T1–T5) rather than re-asking
it. Linear issue **PRO-97**, under the wave umbrella **PRO-87**.

Structure per §1's derivation protocol: **derivations** apply without
confirmation (Erik may veto any before kickoff); **deltas** are Erik's to
confirm; **run-time standing rulings** are dated, class-wide and flagged for
review.

---

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1 — The firm (T1, same adviser).** Battery Ventures is **one
  SEC-registered investment adviser with two relying advisers**, and all
  three are IN:

  - **BATTERY MANAGEMENT CORP.**, dba **BATTERY VENTURES** — **CRD 160921**,
    status ACTIVE RIA, Form ADV filed **2026-03-30**. Item **5.F RAUM
    $15,609,095,762** across **60 discretionary accounts**, and Schedule D
    Section 7.B lists exactly **60 private funds** — the count matches the
    account count, which is what proves the parse (§11).
  - **BMC UK SUBADVISOR SUPPORT, LTD. (RELYING ADVISER)** — the London desk.
  - **BATTERY VENTURES ISRAEL LTD (RELYING ADVISER)** — the Tel Aviv desk.

  Relying advisers of the one adviser are IN by T1's default, exactly as
  LSVP's US, Europe and Israel offices are IN under CRD 160187. The site's
  own people surface corroborates the office set: 133 current staff across
  Boston (55), San Francisco (26), New York (22), **London (12)**, Menlo
  Park (7) and **Tel Aviv (5)**.

  The 7.B roster is one continuous fund family — Battery Ventures VIII
  through XIV with their Side Funds, the Select Funds I and II, the
  Cayman and domestic AIVs, and the Battery Investment Partners IX–XIV
  and Select I–II general partners. Battery Ventures XV and XV-EF (CIKs
  1908631/2108633, filing since 2026) postdate the ADV, so the sworn
  number is a **floor** and press supplies the range top (the Cherry
  lag pattern, §11).

  **IAPD was checked by CRD for a brand-sharing entity with its own
  registration, as PRO-87 requires rather than assumes — and unlike Menlo,
  there is one.** A search of every adviser named "Battery" returns:

  - **BATTERY GLOBAL ADVISORS, LLC — CRD 158508, its own ACTIVE RIA. OUT.**
    This is the Accel-KKR / Lightspeed Faction pattern: a brand-sharing
    entity with its own adviser registration and its own fund family. It
    files from **1 Marina Park Drive, Suite 1150**, one floor from Battery
    Ventures' own Suite 1100 in the same Boston tower, and its vehicles —
    Battery Alternative Income Fund LLC and Ltd, Battery Uncorrelated Fund
    LLC, Battery Opportunity Fund LLC and Ltd — are wealth-management and
    fund-of-funds products, not venture vehicles. The shared address is
    why the desk rules resolve by **CIK and filing suite**, never by the
    name pattern alone.
  - **BATTERY PRIVATE, INC. — CRD 284734**, an inactive ERA that appears as
    a d/b/a of Advisory Services Network, a wealth-management aggregator.
    Unrelated. OUT.
  - **BATTERY EAST GROUP, LLC / SCENIC ADVISEMENT — CRD 169716**, a San
    Francisco secondaries advisory firm. Unrelated. OUT.
  - **BATTERY PARK MANAGEMENT** (a Nomura d/b/a, CRD 110411) and **BATTERY
    PARK CAPITAL** (a Kelleher d/b/a, CRD 126021) — CLO and high-yield
    managers. Unrelated. OUT.
  - **BATTERYMARCH** — the Legg Mason quantitative shop. Unrelated. OUT.

  Also OUT, and not by T1 but by the third-party-feeder precedent (Thrive
  IX Access, §1 T5): **Battery Ventures Opportunities Access LLC** and
  **Battery Ventures Opportunities Access Offshore LP**, which file from
  **200 West Street, New York** — Goldman Sachs' address, not Battery's.
  They are a sponsor's feeder into Battery funds, so they are external.

- **D2 — The buyout practice is NOT a separate strategy desk (T1, strategy
  addendum).** This is PRO-97's first consequence, and the facts decide it
  against a desk partition.

  The T1 strategy addendum partitions **per vehicle, by CRD or CIK**. On
  Battery there is no vehicle to partition: the ADV's 60-fund 7.B roster
  and the EDGAR filer set both show **one fund family** — Battery Ventures
  VIII–XV, Side Funds, Select I–II and their AIVs — with **no buyout-only,
  growth-only or credit vehicle anywhere in either set**. Battery's stated
  model is a single fund investing from seed through buyout, and the
  filings bear that out.

  Therefore `desks.partition` stays **empty**, the strategy addendum does
  not fire, and — contrary to the issue's hopeful reading that a desk
  partition "may make the control test rarely needed" — **the whole
  question falls to T3's transaction-level control test**. Battery is
  precisely the case the addendum names as undecided by the vehicle rule:
  "where one vehicle does both (Insight, General Catalyst)".

- **D3 — Control positions (T3, control addendum).** Battery's own company
  pages carry a **STAGE** field with three values, and the live surface
  splits **Early 152 / Growth 127 / Buyout 71** across 351 listed rows.

  That label is the **firm's own strategy label, not a verdict of control**,
  and it is not treated as one. T3's test is control: 50% or more of the
  voting equity post-transaction, or a transaction the company itself
  reports as a change of control. So:

  1. Every row the firm labels **Buyout** is adjudicated on the control
     test in the grind, not excluded on the label.
  2. Rows labelled **Growth** are tested too where the evidence shows a
     majority recapitalisation — the label is Battery's, and a control deal
     can sit under it.
  3. A row that fails the control test (a minority growth position the firm
     happens to file under Buyout) **stays in the base** as a normal
     Growth entry.
  4. A row that meets it leaves the published base, preserved in
     `excluded.csv`, and every round-describing column (`entry_stage`,
     entry valuation, the C2A cohort) is meaningless for it and is not
     authored.

  The firm's own STATUS text is often decisive on its face — Forterro reads
  "Majority stake sold to Partners Group in 2022", which is a control
  position stated by the firm.

- **D4 — Fund money (T2).** Standard. Battery runs no scout programme and no
  accelerator; the site publishes no community or program list. Partners'
  personal angel positions are OUT, and the compliance list is a list of
  **fund** investments by construction ("All investments as of Q1 2026"),
  so T2 does little work on this investor.

- **D5 — Person or firm, and operating company (T4, T5).** Standard.
  Person-level attribution locates a person, seats are dated against the
  person's firm at filing time, and the fund-shaped / token / scrape-artifact
  rules apply unchanged. One scrape artifact is already known and configured
  out: `/company/battery-ventures/`, the firm's own self-referential page.

- **D6 — The profile is sliced to the base's boundary, and says so (T1,
  profile rule).** This is PRO-97's second consequence.

  Where a venture desk is a child of a larger parent, §1 forbids the
  parent's RAUM from filling the child's `aum`. **That shape does not apply
  here**: there is no parent and no child desk. One adviser (CRD 160921)
  manages one fund family, and the same funds hold the early, growth and
  buyout positions, so **no venture-only RAUM exists to report** — the
  $15.609B is the sworn number for the whole of what this base covers the
  minority slice of.

  So `aum` carries the adviser's own Item 5.F figure, and the profile
  states plainly that **the published base covers Battery's minority
  venture activity while the AUM and fund list cover the whole adviser,
  buyout included**. Without that sentence the base reads as the firm's
  entire track record, which it is not. The excluded control rows are
  counted in `report.md` as a number, not a footnote.

- **D7 — Pre-window entries (policy constant).** Battery has invested since
  **1983** and the compliance list carries the 1980s and 1990s book
  (@Stake, Banyan Systems, Concord Data Systems, Fore Systems, Infoseek).
  The window opens **2006**, so pre-2006 entries are pre-window:
  `seed_to_a_graduation` is null by rule, and `entry_stage` carries the
  **best-supported label at low confidence with a `pre_window_entry` flag
  rather than a null** (Erik, 2026-09-07, the ruling that resolved the
  collision with invariant 1's 100% fill). This keeps the column filled,
  which is also what the database's NOT NULL `entry_stage` requires.

---

## Deltas (Erik's to confirm)

**None.** Every question this investor raises — including the one PRO-97
called the wave's hardest — resolved as a derivation under a test Erik has
already confirmed: T1's strategy addendum and T3's control addendum, both
ruled 2026-09-04. Nothing here is a new category, a test collision, an
argued exception or a change to a policy constant.

Two items are **reported, not confirmed**, and are raised in the closing
message rather than blocking the run:

1. **The `control_position` reason code does not exist in the pipeline.**
   `build-company-base.py` hard-codes three exclusion reasons
   (`build_filter`, `other_desk`, `not_member`); COLLECTION.md §1 specifies
   a fourth. PRO-97 anticipated this and named it a §9 escalation to raise
   once rather than a workaround to improvise, and §12 reserves `scripts/`
   for the tooling session while siblings are in flight. So control rows
   land as ledger `not_member` verdicts whose basis sentence names the
   control test, which is lossless for counting and for the report, and
   lossy only in `excluded.csv`'s reason column. See R1.
2. **Whether Battery's buyout book should be excluded at all** is a
   consequence of a rule Erik has already confirmed, applied here for the
   first time. The run applies it and reports the venture and control
   shares as numbers so the call can be reversed cheaply if the published
   result is not what the rule intended.

---

## Run-time standing rulings

### R1 — Control rows land as `not_member` with a control basis (2026-09-06)

Class-wide, and a workaround recorded rather than hidden. A row ruled a
control position is written to the ledger as `not_member`, `who: "agent"`,
with a basis sentence that opens **"control position:"** and states the
evidence (majority stake, change of control, or the firm's own wording).
`excluded.csv` will therefore show it under reason `not_member` rather than
`control_position` until the build emits the fourth code. The prefix makes
the class exactly countable from the ledger for the report, and re-labelling
them later is a one-line filter. Flagged for review.

### R2 — The site's STAGE field is a strategy label, never a control verdict (2026-09-06)

Battery labels every listed company Early, Growth or Buyout. `Buyout` is the
firm's own strategy bucket and is treated as **a trigger for the control
test, not its answer**: it routes the row to adjudication, and a minority
position filed under it stays in the base. Symmetrically, a `Growth` label
does not exempt a row from the test. Scored on the calibration gate before
it is trusted for `entry_stage` at all (§4). Flagged for review.

### R3 — Both capture archives were down, so the roster was rebuilt from filings (2026-09-06)

On 2026-09-06 the Internet Archive refused every CDX query (connection
refused, replay intermittently answering) **and** Common Crawl's
`collinfo.json` returned empty replies. Both capture archives, unavailable at
once — the first time any run has hit that. §5's instruction is to invent the
layer rather than record the gap, and §9's trigger 4 does not fire until the
invention pass has been tried.

Two of the archive's three jobs did not need replacing. **Survivorship
correction was already covered** by a live first-party surface: the compliance
list is a complete enumeration "as of Q1 2026" carrying the 1980s and 1990s
book, which is the rare case where the archive's main job is done elsewhere.
**Corroboration** landed anyway once the replay path recovered (19 years,
1,021 distinct slugs).

The third job — **the historical roster** — had no substitute, and
`partner-roster.py` wrote 133 people all stamped 2026–2026. What replaced it
(`scratch/pull-fund-related-persons.py`, `scratch/build-roster.py`):

1. **Form D related persons on the firm's own vehicles.** Every Form D carries
   a `relatedPersonsList`, so Battery Ventures VIII–XV and their GPs name their
   own partners with the filing's date attached. 25 filings, 21 people, dated
   2010–2026, independent of any archive.
2. **The co-filer person CIKs** already in `entities.json`, dated **only by the
   Battery filings they appear on** — never by their whole EDGAR history, since
   a partner keeps filing at their next firm.
3. **Name-variant collapsing**, the First Round rule: "Michael M. Brown" /
   "Michael Brown", "David Tabors" / "R. David Tabors" and "Dharmesh Thakker" /
   "Dharmesh Takker" (a typo in one filing) are one person each with the union
   window.

Roster: 133 → **144 people, 11 of them departed with windows**, recovering
founders and GPs the live site no longer lists (Howard Anderson, Richard
Frisbie, Todd Dagres, Oliver Curme, Mark Sherman, Thomas Crotty, Kenneth
Lawler, Morgan Jones, Sunil Dhaliwal, Itzik Parnafes, Brian O'Malley). The
Form D sweep grew from 723 accessions on 133 names to **930 accessions across
436 issuers**. Flagged for review; proposed for write-back at close.

### R4 — A co-filing window is a floor, and reading it as a departure date deletes members (2026-09-06)

The first build removed 11 rows as ex-partner evidence, 8 of them on "Mark
Sherman last on site 2008" — a window that came only from the two Battery
filings he happened to co-sign in 2006 and 2008, not from his tenure. Sherman
was a General Partner from **2000 to 2010**; Oliver Curme was one from **1985
to 2005**. A floor read as an end date is precisely the First Round failure
(§8) in a new source.

So the roster carries an explicit **web-verified tenure table** with a source
per partner, applied over the filing-derived proxy, and the removal list is
re-read after every rebuild. With the corrected windows the rule removes
**31** rows instead of 11, and every one is a next-firm seat that the floor
had been hiding: Todd Dagres's post-2005 filings are **Spark Capital** deals
(1stdibs, Freight Farms, Covestor — Spark is already collected, so these would
have been cross-investor contradictions), and Brian O'Malley's post-2014 ones
are **Forerunner** deals (Arrived, Fora Travel). Widening a window is safe —
it keeps rows; narrowing one is what deletes them. Flagged for review.
