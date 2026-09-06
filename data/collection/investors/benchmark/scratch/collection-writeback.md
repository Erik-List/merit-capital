# Proposed COLLECTION.md edits from the Benchmark run (PRO-88)

Nothing here is committed to `COLLECTION.md` by this session — §12 reserves the
playbook for the designated tooling session. Five investor-agnostic rules and
two mechanical fixes, each with the evidence that paid for it.

## 1. §1, Evidence rules — a site listing suffices *unless the site disclaims it*

Current text: "a listing on the investor's own site (any era) … suffice[s] alone".

Proposed addition:

> **Read the page's own footnotes before trusting its rows.** A firm's list may
> carry a legend that disclaims part of it, and the legend outranks the listing:
> Benchmark's portfolio pages, every era from 1999 to 2009, footnote
> "\* Investments made by Benchmark Capital general partner(s) prior to the
> formation of Benchmark Capital" against 21 rows — AOL, Palm Computing,
> Synopsys, Rambus, Legato Systems and sixteen more, the founders' pre-1995
> deals from their prior firms. No fund of the firm held any of them, so T2 rules
> them out as one class. Taken as plain site listings they would have published
> 6% of the base as a false track record, weighted to the most famous names on it.

## 2. §1, seat dating — a carried seat stays the prior firm's

Current text: "A seat is dated against the person's firm at filing time, not
against the roster."

That is right for a seat taken at the new firm and wrong for one carried across a
move. Proposed refinement:

> **A continuing board seat first taken at a prior firm stays the prior firm's.**
> The later filing is an amendment to a relationship that began elsewhere, so the
> test is the seat's FIRST year, not the filing's. Miles Grimshaw joined
> Lattice's board in 2019 at Thrive; his 2021 and 2022 Form D filings on it fall
> inside his Benchmark window and would otherwise read as a Benchmark position.
> The rule matters most at firms that hire laterally — Benchmark took four
> partners out of other firms between 2021 and 2026.
>
> Mechanically, `formd_span` is YEAR-granular and the boundary often sits inside
> a year: Jack Altman's Copilot Labs seat is 2026q1 and his first Benchmark fund
> filing is 2026-06-30. Carry one line per (partner, quarter) on every queued row
> with that partner's roster window and an
> `in_tenure | pre_tenure | post_tenure | boundary` flag — 26 of Benchmark's 60
> Form-D-evidenced rows carry a boundary or pre-tenure seat.

Reference implementation: `investors/benchmark/scratch/enrich-queue.py`.

## 3. §8 / `run.py` — do not seed `member` from a person's Section 16 filing

`prepare`'s membership seeding writes the basis "SEC ownership filing by a fund
vehicle (forms 3,4, CIK …)" **without checking whether the filer is a fund or a
natural person**, and a row seeded `member` that way carries no `membership` need,
so the judge never sees it. §1 already says a person-entity Section 16 filing
locates a person and never a firm position, and `build-company-base.py` drops such
rows — the gap is that the SEEDER does not, for a row that survived the build on
other evidence.

> Proposed: seed `member` from an ownership filing only when at least one filer
> CIK resolves to a fund vehicle in `entities.json`; otherwise queue the row for
> membership.

Caught by the trap set on Wealthfront (Forms 3/4 filed by RACHLEFF ANDREW S on
the company he founded after leaving) and by the class sweep on Activision (Forms
3/4 filed by LASKY MITCHELL as an Activision executive, eight years pre-tenure).

## 4. §6 / §8 — `first_seen` on a Form-D-only row is a ceiling, not a date

§6 already says "The first filed round is a ceiling on entry recency, not the
entry." The same is true one level up, of the row's `first_seen`, and it is not
said anywhere:

> **For a row whose only evidence is the Form D sweep, `first_seen` is the first
> filing on which a roster name appears as a director — not the entry.** A firm
> that leads seeds and Series As which never file (SAFEs, 4(a)(2)) will see
> `first_seen` run years late across its whole recent book: on Benchmark it runs
> two to five years late over 2013–2026, and Cerebras carries `first_seen` 2026
> against a 2016 entry. It must not feed `entry_stage`, the C2A cohort or any
> "recent" or momentum slice unchallenged. The firm's own first LISTING year is a
> sound ceiling by contrast — checked on ten cited rows it is never later than the
> entry and at most one year earlier.

This is what made Benchmark's Form D band score **7/16** on the pre-registered
stage key, against Sequoia's 32/39 and Accel's demoted 5/13.

## 5. §11, funds — test the filer's style before the $0-sold cross-check

§11 says the total-offering amount corroborates the press size "only for firms
that file a total-offering amount", and warns about Lightspeed's "Indefinite"
style. Benchmark is a third style and the cross-check reads backwards for it:

> **Some firms file the full fund size as the total-offering amount at or before
> first close**, so the offering IS the fund size and the sold amount is merely
> the close state on the filing date. Benchmark's Fund VII shows $5M sold against
> a $425M offering and Fund IX $0 against $425M, on funds the firm held at $425M
> for a decade. Establish which of the three styles a filer uses before asserting
> a size against an accession — `build-firm-profile.py` asserts against the SOLD
> amount and will refuse an offering-based size.

Related, worth a line in §11's AUM recipe:

> An adviser may name its Section 7.B funds by **numeric code** under rule
> 204-2(d) to preserve a fund client's anonymity (Benchmark: '1094', '2165',
> '2645' …). The gross-asset composite is still sound and still anchors AUM; the
> per-fund attribution simply does not exist, and the fund table has to come from
> Form D instead.

## 6. Two mechanical fixes

- **`wayback-pull.py`, `listing_regex`** — collapse internal whitespace in the
  extracted name. A listing that wraps a company name across source lines
  ("Approach\n      Software") was publishing the newlines and the indentation as
  part of the name. One-line change, already made in this run.
- **`scratch/enrich-queue.py`** — offered as the quarter-level seat-dating step of
  item 2 above; it is investor-agnostic apart from its paths.

## 7. One contradiction for Erik, not a proposal

§1's policy constants say the base window opens 2006 and "earlier entries are
pre-window, entry_stage and graduation null". **No landed run has ever done
this** — `verify` requires 100% `entry_stage` fill and Sequoia, USV and every
other base fill pre-2006 rows at model/low confidence, following §6's pre-2003
"Series A by convention" rule. The two statements cannot both hold. It matters
disproportionately here: **200 of Benchmark's 284 rows predate 2006**. This run
followed the landed practice and flagged it rather than silently choosing.
