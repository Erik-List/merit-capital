# Accel — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Accel. The judge
cites these rulings per line. Proposed 2026-08-30 (PRO-62), confirmed by
Erik 2026-08-31 at kickoff (pre-start decision resolving #4).

1. **Firm boundary — one firm, three desks, all IN**: US (Palo Alto) +
   London/Europe + India are one brand, one site, one portfolio page.
   SEC structure agrees: Accel Management Co. L.L.C. (Palo Alto,
   CRD 331435, RIA since 2024-09) with Accel Management Co. (India) as
   relying adviser; the two London advisers (CRD 162784, 171086) are
   affiliated ERAs. All fund families IN: flagship (Accel XI–XVI, then
   "Accel 17"), Growth I–VII, Leaders 1–5, London IV–9, India III–VIII,
   plus Strategic Partners / Entrepreneurs parallel vehicles. Desk
   lineage is recorded per row (us / london / india) but no desk
   partitions out.
2. **Accel-KKR — OUT**: independently operated software-PE firm, own RIA
   (CRD 156498) and own EDGAR fund family. Its portfolio companies are
   not Accel rows; its vehicles stay out of the entity registry.
3. **IDG-Accel China — OUT**: historical 2000s JV branding; successor
   IDG Capital is independent; Accel has no China desk. Rows evidenced
   only by IDG-Accel attribution are not members; an accel.com listing
   still suffices as ever.
4. **Accel Atoms — IN where Accel money was deployed** (ruled by Erik
   2026-08-31, kickoff): the pre-seed cohort program (India /
   Indian-origin founders; Atoms AI / Atoms X tracks) is in for cohort
   companies where Accel deployed fund money — the speedrun logic. A
   cohort listing with no Accel money deployed is out.
5. **Scouts**: no branded scout program found; if one surfaces, out
   unless a main fund followed.
6. **Unidentified new vehicles** (Accel Circle Fund 2026 L.P.,
   CIK 2118098; Accel Core L.P., CIK 2109720): fund vehicles, not member
   rows; classified during the entities registry.
7. **Carried verbatim** from COLLECTION.md §1: ex-partner filings out,
   partners' personal Section 16 out, LP stakes out, evidence
   sufficiency unchanged, fund-shaped list entries and token positions
   under the standing rules.

Known namesake traps for the exclusion classes: Accel Entertainment
(NYSE: ACEL, gaming terminals), Accel Robotics, "Wealth Accel" / "Accel
Wealth Management" adviser namesakes, Accel-KKR portfolio (ruling 2),
IDG-Accel China deals (ruling 3).

Standing rulings made during the run land here, dated, each one a
class-wide rule rather than a row fix.

8. **Meritech vehicles — external** (standing ruling, agent, 2026-08-31,
   found during the entities registry; flagged for Erik's review):
   Meritech Capital Partners, the late-stage affiliate Accel helped
   launch in 1999, is an independently operated firm. The registry's
   "Accel Meritech Associates III" / "Accel Meritech Investors III"
   vehicles are co-invest or LP conduits into Meritech funds — the
   Accel-KKR logic (ruling #2) applies: desk `external`, never crawled;
   a company evidenced only through them is not a member. Subjects of
   filings that also carry a genuine Accel vehicle enter through that
   vehicle as ever.

9. **Erasmic-era India deals** (standing ruling, agent, 2026-08-31 —
   derived from the membership definition; flagged for Erik's review):
   Accel India was formed in 2008 by absorbing Erasmic Venture Fund.
   Deals made with Erasmic fund money before the merge are members only
   where Accel's own listings carry them (the listing suffices as ever);
   an Erasmic-only attribution with no Accel listing is not_member —
   different fund, different firm at the time.

Verdicts live in `base-verification.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded
rows are preserved in `excluded.csv`, never deleted.
