# Thrive Capital — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Thrive Capital. The
judge cites these rulings per line. Researched 2026-08-30, confirmed by Erik
2026-08-31 (PRO-64 Phase 0); written in at kickoff 2026-09-03 under the merged
one-run shape (PRO-71). The underlying facts are re-verified at run time, not
the rulings. **The structural fact of this run: thrivecap.com publishes no
portfolio list in any era (config.json `_eras_note`), so the base builds from
EDGAR, the firm's own job board and cited press.**

1. **The firm = Thrive Capital Management, LLC** (CRD 162771, SEC 801-122181,
   RIA; umbrella with relying adviser Mulberry Street Management, L.P.,
   CRD 343413, same office). IN: Thrive Capital Partners I–X, the Growth
   sleeves (VI Growth onward), the Opportunity funds (2024 Opportunity Fund,
   X Opportunity Fund), the lettered co-invest/SPV LLCs and L.P.s (III-A,
   IV-C/D, IV Stripe, IV Supplemental, VI-A…L, VII-B, VIII-B/C/D, VIII
   Growth-A/B/D, IX-A/C, IX Growth-B…G, X-A, X Growth-A/B, "Harry's"),
   Thrive Capital Partners Investments L.P., the **Claremount** entities
   (Claremount IV/V/VI/VII Associates = GP-side vehicles; Claremount TW =
   the 2013 Oscar Health vehicle, confirmed by the IPO-day Form 3 and its
   June-2013 $5M Form D), and the two further private funds the ADV
   Section 7.B roster lists under the same adviser (JSC Capital Partners,
   L.P.; North River Angel Investments IX, L.P.) — all instruments of the
   firm. Re-verified 2026-09-03: the 2026-07-06 ADV amendment reports RAUM
   $50,492,232,840 across 54 pooled vehicles (all discretionary), 80
   employees (33 advisory), one office at 295 Lafayette St, Suite 701.
2. **Thrive Holdings — OUT**: the AI buy-and-build holdco spun out of Thrive
   Capital in 2025 ($2B raise at $12B, 2026; OpenAI a shareholder). Its
   platforms (Current — the accounting roll-up of ~50 firms; Shield
   Technology Partners — the IT-services roll-up, ~20 companies) and every
   business they acquired are not venture entries. Confirmed refinement:
   pre-spin-out incubations press-attributed to "Thrive Capital" are **IN**
   where a Thrive fund held the position (confirmed 2026-08-31).
3. **Thrive Eternal — OUT**: the permanent-capital holding company announced
   2026-04-24 for sports and cultural assets (San Francisco Giants minority
   stake, first partner; the August-2026 Los Angeles Lakers purchase by
   Kushner and Iger belongs to the same class). Sports franchises and
   cultural institutions are not venture-outcome operating companies under
   the membership definition, whichever vehicle holds them.
4. **13F public positions with no venture entry — OUT** (confirmed
   2026-08-31; now COLLECTION.md §1 standing rule): the adviser's 13F-HR
   (CIK 1765681) is crossover treasury. Re-verified 2026-09-03 on the
   2026-06-30 table (five positions): Amazon ($215M bought August 2026) and
   Shopify ($100M bought March 2026) are public-market purchases with no
   venture entry → `not_member`; Oscar Health (incubated 2013), Figma (Series
   F / May-2024 tender participation) and SpaceX (venture-era entry at a
   $38B valuation, IPO June 2026) entered through venture rounds and stay in
   as public rows. Any future 13F name is judged the same way.
5. **Incubations — IN**: Oscar Health (co-founded January 2013; Claremount TW
   + Funds II/III/V per the IPO Form 3), Cadre, Cedar, The Browser Company
   (incubated 2019 by Josh Miller while at Thrive) and any other incubated
   company where fund money is documented; the /incubations page names the
   program but no companies. Companies Kushner co-founded personally
   (Maple, Capsule) are in only where a Thrive fund position is documented,
   else out as personal.
6. **Secondaries and tenders — IN** as entries at scale (standing instrument
   rule; the book is full of them: OpenAI's 2023 share sale led by Thrive,
   the 2024 Figma tender, the SpaceX secondary entry, the Spotify position).
   Entry stage = Growth per taxonomy; the entry year is the first documented
   purchase.
7. **Carried verbatim** from COLLECTION.md §1: ex-partner filings out,
   partners' personal Section 16 out (Kushner's personal positions — the
   Miami Heat stake, the Lakers — are personal or Eternal, never portfolio),
   LP stakes out, evidence sufficiency unchanged, fund-shaped list entries
   and token positions under the standing rules, seats dated against the
   person's firm at filing time.

**Namesake traps**, unusually dense — verify by address (295 Lafayette St,
New York) and CIK, never by name: "Thrive Capital Fund I LP" (Dallas, CIK
1659889), "THRIVE CAPITAL FUND I, LP" + "THRIVE CAPITAL PARTNERS, INC."
(Peoria IL, CIKs 1588330/1588065), "Thrive Capital Management, LLC" (Fort
Washington PA wealth manager, CRD 281347, **its own 13F filer CIK 1845943
under the adviser's exact legal name** — a registry CIK override, no name
pattern can split them), "Thrive Capital LLC" (Rye Brook NY), MOB II Thrive
Partners (Austin real estate, CIK 1742644), "THRIVE VII SPV, a series of
SVG Thrive Accelerator Fund" (Los Gatos, CIK 1852696), Thrive SIMFA AT
Partners (Austin), Thrive Global Holdings (Arianna Huffington's company,
CIK 1724904), Thrivent, and the Mulberry Street namesakes (Mulberry Street
Investment L.P., Newark NJ PE fund, CIK 1532515; Mulberry Street
Commercial Properties; Mulberry Street Films). In config these are the
`external` desk patterns and run as the first classify rule (§5.3).

Standing rulings made during the run land here, dated, each one a class-wide
rule rather than a row fix.

8. **The firm's Getro job board is its one published list surface** (standing
   ruling, agent, 2026-09-03 kickoff; flagged for Erik's review).
   jobs.thrivecap.com ("Thrive Capital Portfolio Careers", legal entity
   Thrive Capital Management, LLC, 295 Lafayette St) lists 106 companies
   (sitemap_companies.xml, enumerated 2026-09-03 into
   `sources/site/jobs-board-companies.json`). It is a listing on the
   investor's own site and enters the base as the `site_listing` layer
   (`seed-evidence` member verdicts). Its two defects are recorded rather
   than hidden: it is a careers tool, so it under-lists (exits, dead
   companies and founders who never joined it are absent — recall runs
   through EDGAR and press) and it can over-list (Thrive Holdings or
   Eternal entities would be `not_member` under rulings 2–3 whatever the
   board says). Every board-only row is corroborated in the grind where
   press or a filing exists and the corroboration is written into the
   verdict basis; a board row with none keeps its listing verdict, cited to
   the board page.
9. **Third-party access and feeder vehicles are not firm instruments**
   (standing ruling, agent, 2026-09-03): Thrive IX Access LLC and Thrive IX
   Access Offshore LP (CIKs 2030178/2030187, "Other Investment Fund", run by
   Flaws/Huff/Ruffer as managers of a third-party managing member) are
   outside feeders into Fund IX, not Thrive vehicles — registry desk
   `external`, never crawled, never a base row. The same applies to any
   bank-platform feeder that names a Thrive fund.
10. **Public-market purchases in 2026 are instances of ruling 4**, listed by
    name so the base carries the ruling explicitly: Shopify ($100M, March
    2026, Bloomberg 2026-05-14) and Amazon ($215M, August 2026, Bloomberg
    2026-08-14) → `not_member`, evidence class `web`, basis "post-RIA public
    purchase, no venture entry". StubHub, reported as a Thrive public
    position, is judged on whether a pre-IPO entry is documented.
11. **Roster tenure is press-dated, not archive-dated** (standing ruling,
    agent, 2026-09-03): with no team page the roster carries the tenure
    windows the record supports — Kushner 2009–, Weinstein 2011–, Gaybrick
    2011–2015 (Stripe CFO after), Paik 2010–2018 (Pace Capital after),
    Grimshaw 2013–2020 (Benchmark Feb 2021–Mar 2024) and 2024–, Zaki 2014–,
    Ahuja 2014–Jan 2025 (Timeless after), Mallick 2015–, Miller 2017–2019
    (The Browser Company after), Hankes 2019–, Clark 2022–, Nohria 2022–,
    Iger Sep–Nov 2022 and 2026– (Disney seats personal). A roster name on a
    filing outside its window is that person's other employer's seat; the
    judge dates every seat against this list (seat-dating principle, §1).
12. **The ADV private-fund roster is membership evidence for named-deal
    vehicles** (standing ruling, agent, 2026-09-03): a Section 7.B.(1) fund
    named after a company (Thrive Capital Partners IV Stripe, LLC; Thrive
    Capital Partners Harry's, LLC) is the firm's sworn statement that it
    holds that company through a fund — `fund_filing`-grade corroboration
    for Stripe and Harry's even though neither files an ownership form.

13. **Base-shape ceilings are restated for this book** (standing ruling,
    agent, 2026-09-03): `verify`'s sanity guards ($1B+ under 20% of the
    base, seed-to-A graduation under 80%) describe a 900-row site-listed
    megafund base. Thrive's 155-row base has no site layer: the job board,
    the fund-vehicle filings and the press/recall layer all surface winners
    first, and a seed entry is visible to the roster sweep mainly when its
    later rounds left filings. 60 of 155 rows ($1B+, 38.7%) and a 96%
    graduation rate are the shape of the evidence, not a defect, so
    `config.json` `verify.shape` restates the ceilings (45% / 100%) with
    this note; the defaults stay for every other investor. The guards still
    fire above the restated values.

14. **Consortium and token positions follow the token rule and the
    a16z precedent** (standing ruling, agent, 2026-09-03): Thrive's 2019
    Libra founding-member position (Libra Investment Tokens) maps to an
    issuing organization with governance, so Diem is a member row, exited
    when Silvergate bought the association's assets (the Jul-2022 S-3 lists
    Thrive Capital Partners VI and Claremount VI Associates as selling
    stockholders); status `defunct`, aligned with a16z's `diem` row. A
    stake that arrives as merger consideration for an existing row is not
    a new entry (Willow Wealth/Yieldstreet for Cadre: `not_member`).
15. **The exit-side EDGAR sweep and the Wikipedia insource sweep are
    standing recall layers for this book** (agent, approved by Erik
    2026-09-03 as a post-close delta with a second rebuild): every
    third-party registrant naming a Thrive fund entity (S-1 rights-agreement
    parties and holder tables, 424B selling stockholders, acquirer S-3s,
    Regulation A holder lists) and every company article whose source
    names the firm is judged; both layers are re-run before any
    re-collection.

Verdicts live in `base-verification.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded
rows are preserved in `excluded.csv`, never deleted.
