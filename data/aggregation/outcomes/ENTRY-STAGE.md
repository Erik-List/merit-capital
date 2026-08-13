# Entry-stage constitution

**entry_stage is the stage label of the round in which Sequoia first put firm
money into the company** (MEMBERSHIP.md defines "firm money"). It is a fact
about a named historical deal, not about the company's maturity today.

## Taxonomy

`Pre-Seed | Seed | Series A | Growth`

- **Growth** = Series B and everything later: C/D, crossover, pre-IPO,
  secondaries and tenders (a tender entry is an entry at scale: Stripe 2024),
  buyout-scale positions (Aricent), recaps of operating companies
  (First Republic 2010), and consortium structures (EDX).
- **Pre-2003 deals**: the modern ladder does not map; the first institutional
  round is recorded as `Series A` by convention, at low confidence, unless a
  documented seed exists (none known). Stated once here, not re-argued per row.
- **Re-entry** after a full exit would restart the clock at the new round;
  no such row is currently known.
- **SAFEs / seed extensions** count as Seed. A "seed" so large it prices the
  company like an A (Sunday, Ineffable) stays Seed: the label follows what the
  firm and the record call the round, not the check size.

## Evidence classes, strongest first

1. `web_verified` + `entry_stage_citation` (URL naming the round and Sequoia's
   participation, or Sequoia's own memo/company page).
2. `formd_structural` (the pinned filing sequence: partner-anchored entry
   position with prior-filing count; the accessions are the citation).
3. `model` with a **named deal** in the note ("Sequoia led the 2011 Series A")
   at high/medium confidence.
4. `model` at low confidence, or `stage_prior` for unidentifiable rows.

A publication-visible claim wants class 1 or 2. Class 3 is acceptable for the
display aggregate; the run attempts to upgrade every row (Erik, 2026-08-13:
attempt to cite ALL rows, priority $1B+ incl. IPO, then recents, then rest).
A row where the attempt found no source carries `stage_uncited`, visible to
sampling. Class 4 stays flagged.

## C2A cohort rule (Erik's ruling, 2026-08-13)

The graduation rate keeps model-medium rows: a cohort row whose entry or
graduation rests on class 3 evidence stays IN the cohort and carries
`cohort_unverified`. Verified rows carry citations on both legs (entry stage
and the A follow-on). The published rate is therefore accompanied by its
verified share in the report.

## Verify invariants

1. 100% entry_stage fill, valid taxonomy (standing).
2. Every `1b_plus`-and-above row: class 1 or 2, else FAIL (hard).
3. Every cohort row: class 1 or 2 on both legs, else `cohort_unverified` flag
   present (soft, counted).
4. `stage_uncited` only on rows where a citation attempt happened and failed;
   counted in the report per tier.
