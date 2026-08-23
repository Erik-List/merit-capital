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

Verdicts live in `base-verification.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded
rows are preserved in `excluded.csv`, never deleted.
