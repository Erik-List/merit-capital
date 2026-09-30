# Visionaries Club — investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Visionaries Club
(slug `visionaries-club`, display name **Visionaries Club**; the firm's 2026
site calls itself "Visionaries" with "Visionaries Club" as its alternate name,
and its deep-tech fund trades as **Visionaries Tomorrow**). The judge cites
these rulings per line. Written at kickoff 2026-09-30 (PRO-103) under the
derivation protocol of COLLECTION.md §1: **derivations** (a standing test
applied to verified facts, vetoable, no confirmation needed), **deltas**
(Erik's), and **run-time standing rulings** (dated, flagged for review). The
facts below were verified at kickoff; the sources are on disk under
`sources/`.

**The structural fact of this run:** Visionaries Club is a Berlin/London firm
founded in 2018–2019, with a first seed fund and a first growth fund of about
€40M each (first closings 2020), single-company "Late Growth" vehicles from
2021, a second seed fund (€150M) and early-growth fund (€200M) and a €50M
deep-tech "Tomorrow" fund announced 2022-09-22 (TechCrunch). Its SEC footprint
is fund-side only (three 2021 Form Ds, one ADV); its companies raise in Europe
and file nothing. Membership therefore rests on the firm's own lists (the live
visionaries.vc and tomorrow.vc pages, the 2023–2025 WordPress portfolio in
Common Crawl and the Internet Archive), the German register's shareholder
lists naming the fund KGs, and press.

## Derivations (T1–T5 applied to verified facts; vetoable)

- **D1 — The firm (T1, same adviser).** One adviser: **Visionaries Club GmbH**,
  Brunnenstr. 24, 10119 Berlin, SEC exempt reporting adviser, CRD 317147, SEC
  file 802-122841 (annual amendment 2026-03-24, `sources/registers/adv-317147.txt`).
  Direct owners (Schedule A): Robert Lacher (managing director since 12/2018,
  through Kensington Beteiligungs GmbH, member since 10/2018) and Sebastian
  Pollok (managing director since 03/2019, through Cape Ventures GmbH, member
  since 02/2019). Its Section 7.B lists eleven private funds
  (`sources/registers/adv-7b-funds.json`, $193.1M gross assets in all):
  Seed Fund I, Growth Fund I, Late Growth I, II, III and IV, Seed Fund II and
  its feeder, Growth Fund II and its feeder, and Tomorrow Fund I, all "GmbH &
  Co. KG". The register (North Data over the Handelsregister, Amtsgericht
  Charlottenburg; `sources/registers/northdata-*.html`) carries the same tree:
  Seed Fund I HRA 55972 B, Growth Fund I HRA 55965 B, Late Growth I HRA 58572 B,
  Late Growth IV HRA 59109 B (dissolved) and a second Late Growth IV HRA
  64866 B, Seed Fund II HRA 60069 B, Growth Fund II HRA 60072 B with Growth Fund
  II Access GmbH HRB 265145 B (2024-06-26, managing director Roland
  Geeraedts, the firm's CFO), Tomorrow Fund I HRA 60243 B with its Admin GmbH
  HRB 241654 B, **Visionaries Club AGI I GmbH & Co. KG** HRA 65385 B (the
  newest vehicle, not yet on the 2026 ADV), carry KGs for Funds I and II, and
  Visionaries Club Ltd (London, Companies House 14248209). EDGAR carries three
  2021 Form Ds (Seed Fund I CIK 1861538, Growth Fund I CIK 1861059, Late Growth
  I CIK 1886703), each naming Lacher and Pollok as executive officers.
  All under one adviser and one team → **IN**: primaries, follow-ons and
  secondaries from any of these vehicles. Precedent: Creandum (flagship,
  Select and SPV vehicles), Cherry (Opportunities, Select and Growth sleeves).

- **D2 — Visionaries Tomorrow (T1).** tomorrow.vc is the firm's deep-tech fund:
  Tomorrow Fund I is a private fund on Visionaries Club GmbH's own ADV, the
  site's team is the firm's (Sebastian Pollok, Robert Lacher, Linh Seidel,
  Thong Le Hoang, Iris ten Have) and Lacher's own quote calls it the extension
  of "our Visionaries Club strategy into deep tech". Its ten listed companies
  are **IN** on the same footing as visionaries.vc's.

- **D3 — The Late Growth and AGI vehicles (T1, T3, T5).** Late Growth I–IV and
  AGI I are single-company vehicles run by the same adviser. A position held
  through one is the firm's position (T1; Creandum's SPV TR precedent) and a
  row (T5: the vehicle itself is never a row). The round it bought decides the
  stage: a primary or a secondary into a late round is a `Growth` entry (T3,
  secondaries and tenders are Growth). Where the register names the vehicle
  (Late Growth I on Xentral ERP Software GmbH's shareholder lists of
  2021-11-09 and 2023-10-06) it is `fund_filing` evidence.

- **D4 — The LP network (T2, fund money).** The firm markets itself on its
  backers: "more than 20" founder LPs it has backed before (Hanno Renner of
  Personio, Jenny Podewils of Leapsome, Daniel Khachab of Choco, Christian
  Reber of Pitch and Superlist; TechCrunch 2022-09-22), unicorn founders
  (Daniel Dines of UiPath, Niklas Zennström) and family businesses (tomorrow.vc's
  "Backers": Swarovski, FlixBus's founders, Babor, Heraeus, Haniel, Fiege,
  Conrad and others, each with a page at `tomorrow.vc/<person>`). An LP's own
  company is **never** a row on that association alone (T2: the only
  connection is a person); a backer's company that a fund actually invested in
  is a member on that investment's evidence. Neither the backer pages nor the
  founders' "stories" posts (UiPath, Supercell) seed rows.

- **D5 — Partners' previous firms (T4, seat dating).** Robert Lacher was a
  founding partner of **La Famiglia** before Visionaries (his own bio names
  Deel, Groq and Personio from those years); Judith Dada was a general partner
  at La Famiglia and, after its 2024 merger, a partner at General Catalyst
  before joining Visionaries in 2025 (her bio names Personio, Parloa, Orbem,
  Buynomics, Ethon). A company backed at those firms is **not** a Visionaries
  position unless a Visionaries fund invested (COLLECTION.md §1, the
  partner-carried ruling, Erik 2026-09-17). Personio is on both sides: the
  firm lists it as its own and the press names it among Visionaries'
  investments (TechCrunch 2022-09-22), so it is a member on the Visionaries
  fund's own entry, which the grind must find and date; La Famiglia's earlier
  check is never the entry.

- **D6 — The founders' pre-fund checks (T2).** The adviser's owners date from
  late 2018 and the first funds' first closings from 2020 (Form D first sale
  2020-09-21; Seed Fund I on GetMomo's shareholder list by 2020-07-13). A
  check the founders wrote personally before a fund existed is out (Cherry D2,
  generalised by Erik 2026-09-26); where a fund later came in, the row is a
  member and its entry is the fund's first check.

- **D7 — The domain's previous owner (T5, scrape artifacts).** visionaries.vc
  was a Japanese Toastmasters club's site until 2019 (every capture before
  2020 is that club: meeting minutes, photo galleries). Nothing from those
  captures is read, and no row may cite one.

## Deltas (PRO-103's delta list, answered from the facts)

PRO-103 listed four expectations as priors to verify rather than rulings to
make; none needs Erik before kickoff:

1. *Youngest firm, short archive, small base.* Verified: the firm's own site
   exists from mid-2020, the Internet Archive and Common Crawl carry four site
   generations (see `config.json` `wayback._eras_note`).
2. *The S2A cohort may be too young to publish.* Measured at the end of the
   run; the rate is published with its cohort size and date range, or withheld
   with the reason, in `report.md`.
3. *The LP base is a T2 trap.* D4.
4. *Multiple sleeves under T1.* D1–D3, verified by registration.

## Run-time standing rulings

(dated, each flagged for Erik's review)

- **R1 — Personio is a partner-carried prior-firm deal (T4; COLLECTION.md §1,
  Erik's Menlo ruling of 2026-09-17, which binds every investor).**
  *2026-09-30, flagged for Erik: this moves an $8.5B row.* The firm lists
  Personio and its homepage calls Hanno Renner a "Portfolio founder & LP",
  and TechCrunch's fund article of 2022-09-22 repeats Personio among its
  investments. But Robert Lacher's own bio on the firm's team section credits
  Personio to La Famiglia ("Prior to Visionaries, he was the Founding Partner
  of La Famiglia ... including investments in companies such as Deel, Groq and
  Personio") while listing Lovable, n8n, Pigment, Miro, Tacto and Pave Space as
  his Visionaries deals; Judith Dada's bio also credits it to La Famiglia; no
  Series C, D or E report (2020–2022), no register filing and no Google News
  item names a Visionaries fund in Personio, and the firm's lists carry no
  dates. That is the Menlo signature in full, so the row is `not_member`
  (evidence class `web`, citation the team section). Reversal restores it with
  a Growth entry of unknown round.
- **R2 — Stage by construction from the fund's inception.** *2026-09-30,
  flagged.* Where no source names the round the firm entered but the
  company's Series A closed before the firm existed (the adviser's owners date
  from late 2018, the first funds from 2019–2020), every later round or
  secondary is Growth by the taxonomy, so the row reads `Growth` with source
  `model` at medium confidence and the reasoning in the note: Miro (Series A
  2018, `cite_pending` as a $1B+ row) and Rows (Series A May 2018; the entry is
  Lakestar's March 2020 round in DashDash, Deutsche Startups 2020-03-09). This
  is the opposite direction to the capture-date reading PRO-143 refused (a
  capture only bounds an entry from above; the fund's inception bounds it from
  below and the taxonomy makes the bound decisive after an A). Not applied
  where the firm could have been in the A or an A extension (Causaly,
  incident.io, Pigment stay `undetermined`).
- **R3 — A German shareholder list naming a fund KG is `fund_filing`.**
  *2026-09-30.* North Data's free fund pages name the portfolio GmbHs whose
  Gesellschafterliste lists each Visionaries fund (up to three per year, the
  rest counted). As on Balderton's UK share registers, a register filing that
  names the fund as holder is filing-grade membership evidence; it put Tytan,
  ContextFab and Acapela in the base, and dated GetMomo's and Tacto's entries
  to 2020. The yearly counts are a recall check (Seed Fund I: 14 German
  holdings in 2021, 21 in 2022, 12 in 2023, 8 in 2024).
- **R4 — One company, several names** (identity-merges.json, applied at the
  rebuild): Zigguratum → Ziggiz, Loxo → Pallery, Uify → turian. Recorded in
  notes, no second row: GetHenry → Cycle, Simplo → GetMomo (the founder's
  earlier product on the same GmbH), aiConomix → automaited, DashDash → Rows,
  Gtmhub → Quantive, Tillit → Two.
- **R5 — Recall candidates rejected** *(2026-09-30)*: Causal Labs (its $6M
  seed names Kindred, no Visionaries; the press hit was an unrelated item),
  Roboat (its EUR 550k round came from LUMO Labs and SHIFT Invest), Lightfern
  (the firm's news feed posted its launch; no round, listing or filing ties a
  fund to it). Pausder and the founders' LP commitments reported by Deutsche
  Startups are LP positions in the firm, never rows (D4).
- **R6 — Sustained stays a member on the firm's 2023 listing** (COLLECTION.md
  §1: a listing suffices unless the firm disclaims it), although its UK and
  Estonian cap tables show only the founders (a convertible is the likely
  instrument).
- **R7 — Arculus enters at the December 2019 pre-emptive round** alongside
  Atomico (the firm's own text; Atomico calls it the Series A), before the
  funds' first closings; Growth Fund I is on the company's 2020–2021
  shareholder lists. Robert Lacher's earlier seed check was personal (D6).
- **R8 — Namesakes ruled distinct** (companies/cross-rulings.json): Lux's
  Tactic (US carbon accounting, bought by TaxBit) and 20VC's Cycle (Paris
  product-feedback software).
- **R9 — Sequoia's "Two" is this company** (Tillit, whose seed Sequoia led in
  2021); its `acquired` is a stale prior: Two raised EUR 13M in July 2025
  (tech.eu). Aligned at the ingest where the Sequoia book passes the gate,
  else accepted with this reason.
- **R10 — Miro stays private at Bending Spoons' agreed price** (COLLECTION.md
  §6, a signed but unclosed acquisition is a mark): the agreement of
  2026-09-10 implies an equity value of about $1.79B, closing expected in Q4
  2026.
