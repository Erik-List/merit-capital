# Lightspeed — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Lightspeed Venture
Partners. The judge cites these rulings per line. Researched 2026-08-30,
confirmed by Erik 2026-08-31 (PRO-63 Phase 0); written in at kickoff
2026-09-02. The underlying facts are re-verified at run time, not the
rulings. **Ruling 2 is the load-bearing decision of this run.**

1. **LSVP desks — IN**: US, Europe and Israel are offices of the one
   adviser (Lightspeed Management Company, L.L.C., CRD 160187, RIA
   effective 2025-04-28). Fund families IN: flagship IX–XIII, then
   XIV-A/B (Inception/Ignite) and XV-A/B, Select I–VI, Opportunity
   I–III, Co-Investment I, plus the LSVP-managed SPV/SIV trail
   (AI Renaissance, Ascent, Velocity, Platinum, Luminous, M2,
   Affiliates X, SPV-*, *-Holdings LLCs) as instruments of the firm,
   not separate desks.
2. **Lightspeed India (LSIP) — OUT as a separate firm**: the firm's own
   about-page disclosure says LSVP and LSIP "are distinct investment
   advisory entities, are not a unitary enterprise and operate
   independently" (LSIP is its own ERA, CRD 310954, own site lsip.com,
   own funds "Lightspeed India Partners I–V, LLC"). The brand is
   shared: lsvp.com's team page has an LSVP/LSIP firm filter, there is
   a `/companies-india/` page, and ~63 lsip.com company links sit on
   the main companies page. Handling (the HongShan / Peak XV precedent,
   with the firm's own disclosure as basis): **LSIP-only rows out; a
   row on the main list with LSVP participation stays in.** The site's
   own `data-investor` attribute (`lsvp` / `lsip` / `both`, verified at
   kickoff on the rendered cards) is the listing-level attribution:
   `lsvp` and `both` are LSVP site listings; `lsip` rows are not, and
   enter only through independent LSVP evidence.
3. **Lightspeed China Partners — OUT**: independent partnership since
   2011 sharing the brand; own US filers (China I–IV, China Select I).
   Rows evidenced only through China vehicles or China-partner
   attribution are not members.
4. **Lightspeed Faction — OUT**: crypto JV with its own RIA (Faction
   Ventures LLC, CRD 318821), own funds, own site faction.vc. The
   contrast with a16z is deliberate: a16z's crypto funds sit under one
   adviser, Faction does not.
5. **Scouts / Emergence / Summer Fellowship**: out unless a main fund
   followed (standing rule). Extreme Entrepreneurs (LSIP India,
   explicitly no funding/equity): out.
6. **Continuation vehicle ("Project Mercury", ~$600M, reported Aug
   2026)**: fund plumbing, not membership — positions moved (OpenAI,
   Verkada, Rippling, Reflection AI, Glean) remain member rows via
   their original entries; a NEW commitment made through it (Anthropic
   reported) enters as an entry at that stage.
7. **Post-RIA public/secondary purchases** with no venture entry:
   **OUT** of the base — treasury/crossover, not portfolio membership.
   A row entered through a venture round stays in even after it goes
   public.
8. **Carried verbatim** from COLLECTION.md §1: ex-partner filings out,
   partners' personal Section 16 out, LP stakes out, evidence
   sufficiency unchanged, fund-shaped list entries and token positions
   under the standing rules, seats dated against the person's firm at
   filing time.

Known namesake traps for the exclusion classes: Lightspeed Commerce
(Canadian POS, NYSE-listed, formerly Lightspeed POS), Lightspeed
Financial / Lightspeed Trading / Lightspeed Professional Trading
(brokerage), Lightspeed Technologies, Lightspeed Environmental,
Lightspeed Systems (Austin edtech), Lightspeed Genomics (now Rebus
Biosystems), GoSkip; Lightspeed China and LSIP fund families (rulings
2–3), Faction vehicles (ruling 4).

Standing rulings made during the run land here, dated, each one a
class-wide rule rather than a row fix.

9. **China-era rows on the firm's own site** (standing ruling, agent,
   2026-09-02, derived from rulings 1+3 and the seat-dating principle;
   flagged for Erik's review): Lightspeed ran China from its global
   funds 2006–2011 (the Ron Cao Shanghai office) before Lightspeed
   China Partners spun out as an independent partnership in 2011, and
   the global site kept listing China rows through the brand-shared
   eras. The boundary follows the money at entry: a China row first
   backed ≤2011 from the global funds is a member; a row entered 2012+
   through LCP vehicles is not_member even where lsvp.com listed it —
   the listing is a brand-era artifact (the same class as LCP's PPDai
   memo living on lsvp.com's own blog). Unresolvable entry years in
   the LCP cluster default to not_member with the ambiguity noted.

10. **The archived /companies/ era cannot assert LSVP attribution**
   (standing ruling, agent, 2026-09-02, measured at build; flagged for
   Erik's review): the site's lsvp/lsip card attribution
   (`data-investor`, lsip.com link-outs) postdates the January-2026
   archive snapshot, so 2023–2026 /companies/ captures render LSIP
   rows with lsvp.com links and archived listing years from that era
   are not, alone, LSVP site-listing evidence. Membership for
   lsip-attributed slugs follows ruling 2 via today's attribution plus
   independent LSVP evidence; 61 of the 65 lsip-only slugs built base
   rows through those captures and are judged under this ruling.

Verdicts live in `base-verification.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded
rows are preserved in `excluded.csv`, never deleted.
