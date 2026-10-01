# Index Ventures — investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Index Ventures
(slug `index-ventures`, display name always **Index Ventures**). The judge
cites these rulings per line. Written at kickoff 2026-10-01 (PRO-82) under the
derivation protocol of COLLECTION.md §1: **derivations** (a standing test
applied to verified facts; no confirmation needed, vetoable), **deltas**
(Erik's), and **run-time standing rulings** (dated, class-wide, flagged for
review).

**The structural fact of this run:** Index is one firm with two evidence
regimes inside one base. Its funds are Jersey limited partnerships under a
Geneva adviser, run from London, San Francisco and New York, and its
portfolio is roughly half US companies (which file Form D and, when they
list, S-1s that name the Index funds) and half European and Israeli companies
(which file nothing with the SEC until a US listing). The same deal therefore
arrives with filing-grade paper on one side of the Atlantic and with the
firm's own listing plus press on the other. D9 says how a row states which
regime it sits in, so the base never reads SEC exposure as evidence strength.
What carries the base: (1) the firm's own record read in depth: the live
Wagtail list of 329 companies (deal partner, sector, a "backed at Seed" mark),
the Perspectives archive (586 posts), and four earlier site generations
1999–2019 that listed the companies the live site has since dropped; (2) the
SEC side: 48 fund filers whose 13D/G and Section 16 filings name the listed
winners, the exit-side full-text sweep (185 third-party registrants name
"Index Ventures"), and the roster Form D sweep for the US book; (3) the home
registers for the European rows (status first, COLLECTION.md §5).

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1 — The firm (T1, same adviser).** Index Ventures = the funds advised by
  **Index Ventures SA**, 2 rue de Jargonnant, Geneva (legal name until a
  rename: Index Venture Management SA), an exempt reporting adviser to venture
  capital funds, **CRD 161175**, SEC 802-75760, annual amendment of 2026-03-31
  (`data/filings/index-ventures/adv/161175.pdf`, parsed in
  `sources/registers/adv-7b-funds.json`). It is the only adviser IAPD returns
  for "Index Venture(s)", and its Section 7.B.(1) lists 32 private funds: the
  venture funds III, V–XII with their Parallel Entrepreneur Funds and Delaware
  Entrepreneur Funds, Growth II–VII, Origin I–II, Life VI, and Index SPV I and
  II. EDGAR carries 48 fund and general-partner filers under the firm's name
  (`entities.json`): Index Ventures III–XIII, Growth I–VII, Origin I–III, Life
  VI and VII, the Associates general partners, SPV 1 and 2. The firm was
  founded in Geneva in 1996 by Neil Rimer, David Rimer and Giuseppe Zocco out
  of Index Securities; London from 2002, San Francisco from 2011, New York
  from 2022 (Wikipedia, the firm's own team pages). One investment team
  across the offices, one adviser, one fund family → **IN**: primaries,
  follow-ons and secondaries from any of these funds. Precedent: Lightspeed's
  US, Europe and Israel offices under one registration; Northzone D1.
  The base does **not** partition by office or by the domicile of the
  portfolio company; `desks.home` is the adviser.
- **D2 — Growth, Origin, SPV, entrepreneur and co-investment vehicles (T1,
  T5).** Index Ventures Growth I–VII (2008–2024), Index Origin I–III (the seed
  funds, 2021–), Index SPV I/II, the Parallel Entrepreneur Funds and the
  Delaware Entrepreneur Funds are sleeves of the one adviser → **IN**, and a
  position moved or followed on through one of them keeps its original entry
  (T5: Creandum's Select funds, Thrive's sleeves). **Yucca (Jersey) SLP**,
  Yucca Partners L.P. Jersey Branch and Yucca Associates Ltd co-file every
  ownership filing with the Index funds as the administrator of the Index
  co-investment scheme (the firm's staff and partners investing alongside the
  funds, pro rata): the same positions, no rows of their own. A filing by
  Yucca alone, with no Index fund on it, is not seen in this run; if one
  appears it is read as the fund's position.
- **D4 — Fund-shaped and programme entries (T5, the standing fund-shaped
  rule).** **Seedcamp** sits on the firm's own list from 2008 (and under its
  "Seed stage" filter): Index was a founding backer of the Seedcamp funds, an
  LP-class stake in another investor, not an operating company →
  `not_member`. The same reading for any accelerator, studio fund or
  investment vehicle the list carries (TheFamily is checked on its facts: an
  operating company that ran an accelerator is a company; a fund is not).
  The firm's own vehicles, the Medicxi vehicles and the Associates general
  partners are never rows.
- **D5 — Person or firm (T4).** A seat is dated against the person's firm at
  filing time. The roster (`sources/wayback/partner-roster.json`) is built
  from the firm's own team pages 2008–2026 and its own "Index Team"
  attribution on each company page, the strongest reference graph a run can
  have (COLLECTION.md §5, a CMS that names deal partners). The departures
  that matter for seat dating are verified per person when their Form D
  cluster is judged (COLLECTION.md §3, cluster-first) and recorded under the
  run-time rulings below: the Klein family's own vehicles (The Accelerator
  Group, LocalGlobe) are personal or third-party money unless an Index fund
  held the position; a partner's operator or board seat from before joining
  (Mike Volpi's Cisco years, Dick Costolo, Stephane Kurgan's King years,
  Carlos Gonzalez-Cadenas, Vlad Loktev, Sahir Azam, Zack Urlocker) is not an
  Index position. A founder's or partner's angel check stays out even where
  the firm lists it, unless a fund held the position (T2, Erik 2026-09-26).
- **D6 — Venture entry (T3).** Secondaries and tenders are Growth entries (the
  firm listed Facebook in 2013: a secondary, in if a fund held it). A
  position that first appears on a 13F or a post-IPO 13G with no venture
  round is out; a row that entered through a venture round stays in after its
  IPO. Sale consideration is not membership (Erik, 2026-09-22): where the
  funds hold an acquirer's stock because it bought a portfolio company (eBay
  for Skype, Corgentech for AlgoRx, Adobe for Figma had it closed), the row is
  the company that was bought.
- **D7 — Control positions (T3).** Index takes minority positions; no
  transaction in which an Index fund acquired control is known at kickoff.
  Moleskine (listed 2013; a minority stake beside Syntegra Capital, the
  controlling holder, ahead of the 2013 Milan IPO) is a minority growth
  position → in, Growth. Any row that turns out to be a control acquisition
  leaves under `control_position`.

## Deltas (Erik's to confirm; the run proceeds on the reading below and raises them at close)

- **D3 — The life sciences desk and Medicxi: OUT, the successor firm owns
  that book.** Facts, verified 2026-10-01:
  - From 1996 to 2016 Index ran one firm with two practices. Its own site
    split the portfolio into "Technology" and "Life Sciences" from 2002
    (`/cgi-local/ivw_port_detail.cgi?typ=it|ls`) through 2013
    (`/portfolio/index/industry_id/1|2`) and 2014–2015 ("Tech / Life
    Science" filters), and the team page listed a separate Life Sciences
    group (Francesco De Rubertis, Kevin Johnson, Michèle Ollier, Roman Fleck,
    Mark de Boer, David Grainger and others). Until 2012 both practices
    invested from the same funds (Index Ventures I–V); **Index Ventures Life
    VI (Jersey) L.P.** (CIK 1591199, 2012) was the first dedicated vehicle.
  - **Medicxi Ventures started on 2016-02-01** and, in the words of its
    launch release, "comprises all of the legacy portfolio companies, funds
    and the life sciences team of Index Ventures", with "Index Ventures and
    Medicxi Ventures [operating] independently"
    (https://www.medicxi.com/news/medicxi-formerly-index-ventures-life-sciences-launches-as-an-independent-venture-capital-firm-and-announces-closing-of-a-210m-fund-including-gsk-and-johnson-johnson-innovation).
    Index's own post is https://www.indexventures.com/perspectives/hello-medicxi/.
  - Registration follows the statement. **Medicxi Ventures Management
    (Jersey) Limited** is its own exempt reporting adviser (CRD 283504, ADV
    of 2026-02-26) with its own fund family (Medicxi Ventures I, Growth I,
    III, IV, V, Secondary I; 17 EDGAR filers). Its Section 7.B.(2) lists the
    funds it sub-advises for another adviser: Index Ventures III (three
    vehicles), Index Ventures V (two) and Index Ventures Life VI, that is,
    the life sciences positions of Index's funds. **Index Ventures Life VII
    (Jersey) LP** (CIK 1648676, Form D 2015) is not on Index's ADV: it is the
    fund that closed as Medicxi Ventures I.
  - Index's live site lists no life sciences company; its "Healthcare"
    sector (14 rows) is digital health backed by the technology partners.
  **Two readings collide.** T1 and T2 read at entry say IN: Index fund money,
  under the Index adviser, by Index partners, listed on Index's own site for
  fifteen years; and Life VI is still on Index Ventures SA's ADV. The
  Benchmark Europe / Balderton precedent (Benchmark D2, Balderton D2) says
  OUT: where a desk becomes its own firm and takes its book with it, "the
  successor firm owns that track record" from the desk's first date, and here
  both firms say so in words. **This run takes the second reading**: every
  position the firm's own site classed as Life Sciences, every position of
  Life VI, and every Medicxi vehicle's position is `not_member` (basis D3),
  preserved in `excluded.json` with its evidence, and the Life Sciences team
  is not swept on Form D. Digital health companies backed by the technology
  partners stay in. Reasons for choosing it over T1-at-entry: the firms'
  own statement is the closest thing to a disclaimer a site listing can meet
  (COLLECTION.md §1, a listing suffices unless the firm itself disclaims the
  position); the page a reader sees is Index Ventures the technology
  investor, and a book of Genmab, Addex and Versartis managed by another
  firm since 2016 would misstate it; and the precedent keeps the two
  spin-out cases in the dataset consistent. **It costs Index its early
  biotech wins (Genmab above all) and that is Erik's call**: the rows are
  listed in report.md with their evidence, flagged `life_sciences_desk` in
  the ledger basis, and return on one rebuild if he rules them in.

## Method rulings made at kickoff (flagged for review)

- **D8 — The firm's own stage claims.** Two first-party fields exist and both
  are eligible by semantics (the firm's claim about the round it entered),
  neither labels before it is scored (COLLECTION.md §5):
  (a) the live listing's **"backed at Seed"** filter (`data-backed` carries
  `seed` or `all-seed` on 75 of 329 cards; "Index has a long history of
  investing at the very early stages ... teams we've been fortunate to work
  with since Seed"). It says Seed and nothing else, so it can label a Seed
  and never a later round; a card without it is no claim.
  (b) the 2009–2013 site's **stage filter** (`/portfolio/index/.../
  company_stage/4|1|2` = "Seed stage / Early stage / Growth stage"). A
  company can sit under two of them (doubleTwist, Dimdim and Erply under Seed
  and Early), and Facebook sits under "Early stage", so the field reads as
  the fund programme that holds the position rather than the round: "Seed
  stage" is the firm's seed programme (a Seed claim), "Early stage" straddles
  Seed and Series A (an anchor, like a bare year), and "Growth stage" alone
  is the growth fund (Growth). Scored in the run against documented rounds;
  the score and the verdict are restated in report.md.
  The Perspectives archive is class 1 for the round a post NAMES; it asserts
  an entry only where the post says so in words (the Menlo rule).
- **D9 — How a row states its evidence regime.** Every base row carries one
  of two regimes, derived mechanically from its own evidence columns and
  never from where the company is based:
  **`sec`**, where the row has any SEC surface of its own (an issuer CIK with
  a Form D, an ownership or Section 16 filing by an Index fund, or a
  third-party registrant's filing that names the fund and the company);
  **`firm_record`**, where the row rests on the firm's own listing, its
  archive and press, with no SEC surface. The regime is a statement about
  which sources could have seen the deal, not about confidence: membership
  is filing-grade in both (a listing on the investor's own site suffices
  alone, COLLECTION.md §1), and the tier column is already regime-neutral for
  listed rows (two site eras make a Tier A row with no filing at all). What
  differs by regime is recall and the classification evidence, and the
  report states both per regime, never blended: rows and share; membership
  evidence class; how many rows are known ONLY through that regime's sources
  (the recall each regime contributes); entry-stage source mix and the share
  `undetermined`; graduation decided by filings versus by cited round or
  dated search; status and band sources. `scratch/regime-report.py` computes
  the table from `base.json` and the merged classification. The published
  CSV already carries the columns the split is computed from (`edgar_forms`,
  `formd_links`, `site_url`, `wayback_first_link`), so a reader can recompute
  it. A US company with no filing is `firm_record`; a Swedish company with an
  F-1 is `sec`.
- **D10 — Registers.** UK (Companies House: status, officers, filed
  shareholder documents), Germany (Handelsregister via North Data), France,
  the Nordics: `status` first, as COLLECTION.md §5 orders it. Switzerland and
  Israel sit below the pre-build threshold and are probed in the run.

## Run-time standing rulings

(added during the run, dated)
