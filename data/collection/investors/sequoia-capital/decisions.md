# Sequoia Capital — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Sequoia. The judge
cites these rulings per line; all confirmed by Erik, 2026-08-13.

1. **Firm boundary**: "Sequoia" means the US/EU venture funds. China/India
   desk deals leave via the desk partition into `excluded.csv` (reason
   `other_desk`).
   Sequoia Heritage is a different entity. Public-market buys by the
   crossover vehicles are not venture outcomes.
2. **Program vehicles**: scout checks are out unless a main fund followed.
   Arc (the seed program) deploys fund money and is in.
3. **Instruments**: primaries, secondaries and tenders by the funds are in —
   a tender entry is an entry at scale (Stripe 2024).
4. **Exclusions applied** (the generic person-attribution rule, with the
   rows that taught it): partners' personal directorships (Intel/Goetz),
   ex-partners filing from their next firm (CrowdStrike via Gandhi/Accel;
   Lamond/Khosla; Huang/Paradigm; Garg/Wing; Lixandru/Accel), partners who
   became founders (Amy Sun/Daylight), founder positions outside the firm
   (Neil Shen's Ctrip, Home Inns, Molecular Data), founder homonyms (Ankur
   Jain/Bilt, Patrick Grady/Rearden+Tetra, Alex Moore=8VC), and LP positions
   (Y Combinator, Polychain).
5. **Window**: the base window opens 2006; earlier entries (Apple, Cisco,
   EA, Atari-era) are pre-window — entry_stage and graduation null, note
   "pre-window".

Verdicts live in `base-verification.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded
rows are preserved in `excluded.csv` (reason `not_member`), never deleted.
