# Membership constitution

**A row belongs in the base iff a Sequoia representative, acting on behalf of
Sequoia, made an investment in it, and it is a venture-outcome company.**
(Erik, 2026-08-13.)

Direct corollaries, applied by the verification judge:

1. **On behalf of Sequoia** excludes: a partner's personal board seat or
   personal filing (Intel/Goetz), an ex-partner acting for their next firm
   (CrowdStrike/Gandhi), founder positions predating or outside the firm
   (Neil Shen's Ctrip), scout checks with no main-fund follow-on, and LP
   positions in other funds or accelerators (Y Combinator, Polychain).
2. **Sequoia** means the US/EU venture funds. China/India desk deals leave via
   the desk partition (existing rule). Sequoia Heritage is a different entity.
   Public-market buys by the crossover vehicles are not venture outcomes.
3. **An investment** includes primaries, secondaries and tenders by the funds
   (Stripe 2024). It is a firm decision with fund money.
4. **A venture-outcome company** is an operating company. Fund vehicles,
   SPVs, filter labels, scrape artifacts and natural persons are out.
5. **Evidence sufficiency**: a listing on Sequoia's own site (any era), or an
   SEC filing by a fund vehicle, each suffice alone. A Form D related-person
   name-match NEVER suffices alone; it needs affirmative corroboration
   (documented deal, credible identification tying the round to the firm).
   Absence of corroboration on a name-match is a `not_member` verdict, not an
   `uncertain` one: the base asserts membership, and an unsupported assertion
   is the defect class this file exists to kill.

Verdicts live in `base-verification.json` and are re-applied on every rebuild.
Human verdicts (`who: "erik"`) outrank agent verdicts. Excluded rows are
preserved in `verification-excluded.csv`, never deleted.
