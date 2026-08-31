# a16z (Andreessen Horowitz) — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to a16z. The judge
cites these rulings per line; all confirmed by Erik, 2026-08-18.

1. **Firm boundary**: one firm, one decision desk. All fund families are
   in — crypto, bio/health, games, American Dynamism, cultural leaders,
   infrastructure. Unlike HongShan / Peak XV these are not separate desks;
   no desk partition exists for a16z.
2. **Program vehicles**: speedrun (the accelerator) deploys fund money by
   firm decision and is in — same logic as Sequoia's Arc. Scout checks are
   out unless a main fund followed.
3. **Instruments**: primaries, secondaries and tenders by the funds are in.
   Token and protocol positions are in when listed on a16z's own portfolio
   page — the site listing is the sufficient evidence class; a token-only
   position never enters on a name-match.
4. **Carried over verbatim** from the generic rules: ex-partner filings
   out, partners' personal directorships (Section 16) out, LP stakes out,
   evidence-sufficiency rules unchanged.
5. **Window**: founded 2009, so the standard 2006 window covers the firm's
   full history; no pre-window class exists.
6. **Fund-shaped list entries** (ruled 2026-08-30, during base review):
   an investment-list entry whose name is fund-shaped (Capital / Fund /
   Ventures / Management, fund numerals) and that cannot be identified as
   an operating company is `not_member` — the LP-stake class — until
   evidence identifies it otherwise; the verdict is amended and the row
   returns on the next rebuild if identification lands. Applied to
   AMP Fund, Drone Capital I, Revival Fund Management (and consistent
   with the identified cases A.Capital, Meta4 Capital, BlockTower
   Capital). Fund-shaped names identified AS operating companies stay in
   (Capital.xyz, Foundation, Proof Holdings, Essence Ventures — the last
   confirmed by Erik 2026-08-30 as an operating media/commerce company).
7. **Pure protocol-asset positions** (ruled 2026-08-30, refines #3):
   a listed token position stays in when it maps to an operating or
   issuing organization (a DAO with a treasury and governance, a labs
   entity — Lido, Uniswap, Optimism, Yield Guild Games); a pure
   base-layer asset holding with no such entity is a treasury position,
   not a portfolio company, and is `not_member` (Bitcoin, Ethereum —
   both of which a16z itself later removed from the investment list
   under its unannounced-public-digital-assets exclusion). Where the
   token and its company are both listed, they are one row under the
   company (Filecoin -> Protocol Labs).

Verdicts live in `base-verification.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded
rows are preserved in `excluded.csv`, never deleted.
