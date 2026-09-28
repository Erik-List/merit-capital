# Ribbit Capital: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Ribbit Capital
(slug `ribbit-capital`, display name always **Ribbit Capital**, "Ribbit" in
notes). The judge cites these rulings per line. Written at kickoff 2026-09-28
(PRO-161) under the derivation protocol of COLLECTION.md §1: **derivations**
(a standing test applied to verified facts; no confirmation needed, vetoable),
**deltas** (Erik's), and **run-time standing rulings** (dated, class-wide,
flagged for review).

**The structural fact of this run:** one registered adviser runs every
vehicle, and most of the firm's growth-stage money went through ~40 single-deal
SPVs whose names encode the company and the round ("RH-E Ribbit Opportunity
II" is a Robinhood Series E vehicle). Most of them file their own Form D (the
build's own-desk scan reads 78 filings on 64 vehicles) and all sit on the
ADV's Section 7.B. The portfolio is fintech and crypto, and two in five of its
companies sit outside the US (Brazil, the UK, India, Mexico, Europe and Asia),
where Form D carries nothing. (Corrected 2026-09-28 at close: the kickoff text
said the SPVs file no Form D and that more than half the portfolio is
non-US; the landed base has 109 US members of 182.)

## Derivations (T1 to T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm and its vehicles (T1).** Every Ribbit fund is advised by
  **Ribbit Management Company, LLC** (IAPD **CRD 165308**, SEC 801-111886,
  primary business name "Ribbit Capital"; principal office 364 University
  Ave, Palo Alto; annual amendment 2026-03-30; Item 5.F RAUM
  $20,775,390,188 over 67 accounts). **Schedule R is empty: no relying
  advisers**, and no other adviser carries the brand. Section 7.B lists 67
  private funds (`sources/registers/adv-165308.pdf`): the flagship **Ribbit
  Capital** funds (I 2012, II 2014, III 2015, IV 2017, V 2018, VI 2020, VII
  2021, X 2022, Y 2025, Z 2026), the growth funds **Bullfrog Capital** and
  **Ribbit Bullfrog II and III**, the **Ribbit Founder Funds** (II to VII, X, Y,
  Z and the Bullfrog Founder Funds), **Ribbit OB1** (master and two feeders),
  **Ribbit BTC Holdings**, and ~40 single-deal vehicles named
  `<code>-<round> Ribbit Opportunity <n>`, `<code> Bullfrog Opportunity <n>`
  or `<code> Ribbit Holdings`. EDGAR carries 28 filers named "Ribbit", every
  one the firm's. **Outcome: IN** for every position any of these vehicles
  held; one adviser, no partition (`config.desks.partition` empty).
  Precedent: Lightspeed's US, Europe and Israel offices under one RIA.
  **External:** Ribbit LEAP, Ltd. and Ribbit LEAP Sponsor, Ltd. (D3).

- **D2: Token and protocol rows (T5, the token rule; Erik's a16z ruling 7).**
  The Rebels list carries **Bitcoin** ("Satoshi Nakamoto", no URL) and
  **Ethereum** ("Vitalik Buterin"). Both are base-layer assets with no
  investable issuing entity; the ADV's **Ribbit BTC Holdings, LP** is the
  treasury vehicle. **Outcome: `not_member`** for both (a16z precedent: Bitcoin
  and Ethereum out, Erik 2026-08-30). Protocol rows that map to an operating or
  issuing organisation are **members under that organisation**: Solana
  (Solana Labs), Arbitrum (Offchain Labs), Uniswap (Uniswap Labs), Morpho
  (Morpho Labs), M0 (M^0 Labs), Farcaster (Merkle Manufactory), Ethena
  (Ethena Labs), Lighter, Tempo; the row keeps the firm's own name. Where the
  money went in as a token purchase and no priced round exists, the stage and
  the graduation read `undetermined` with flag `token_funded` (COLLECTION.md
  §6). **Diem** (the Libra Association, of which Ribbit was a 2019 founding
  member) is a member under the a16z, USV and Thrive precedents (a Libra
  Investment Token position).

- **D3: Ribbit LEAP (T5; the sponsor-promote ruling, Erik 2026-09-07).**
  Ribbit LEAP, Ltd. (CIK 1818346) was the firm's blank-check company (NYSE,
  September 2020), sponsored by Ribbit LEAP Sponsor, Ltd. (CIK 1818380); it
  never completed a merger and was wound up. **Outcome:** the shell is
  `not_member` under T5 (no operating business) and the sponsor's founder
  shares are not a venture entry. No portfolio row arises from it, because
  there was no target. A `config.verify.not_members` trap asserts it.

- **D4: Public positions (T3).** A row that entered through a venture round
  stays a member after listing: Robinhood (2021), Coinbase (2021), Nubank
  (2021), Affirm (2021), Root (2020), Futu? and others are judged on their
  entry round. A position that first appears as a public-market purchase, a
  13F holding or a post-IPO 13G is `not_member`. The listed companies whose
  entry is not yet known to be a venture round (**Mercado Libre**, **Futu**,
  and the archive's **Sea** and **Tinkoff**) are decided in the grind on the
  record: the firm's 13F filings (Ribbit Management Company, CIK 1836733),
  the companies' prospectuses, the firm's own posts.

- **D5: Fund money (T2).** The Founder Funds are the firm's own 7.B vehicles
  and IN. A partner's personal angel check is out, whether or not the firm
  lists the company (Erik, 2026-09-26, Cherry's D2 generalised): Micky
  Malka's pre-2012 positions (his own Banco Lemon and Lemon Wallet, and any
  angel book) enter only where a Ribbit fund held the company.

- **D6: The single-deal SPVs (T1 for the vehicle, T5 for the row).** An SPV
  is plumbing: it is never a row, and the company it holds is a member through
  it (Creandum's SPV TR precedent). The name codes the company and the round
  (RH = Robinhood, RV = Revolut, BX = Brex, ST = Stripe, RZ = Razorpay, KV =
  Kavak, UA = Ualá, BP = BharatPe, FBT = Fenbeitong, TL = Tala, UP = Upgrade,
  RT = Root, GW = Groww, DG = DCG; the rest are decoded in
  `sources/registers/spv-decode.json` or left unresolved). A decoded code is
  `fund_filing`-grade evidence that a Ribbit vehicle entered **that** round; it
  is never read as the entry round, because an Opportunity SPV is usually a
  follow-on into a company a flagship fund entered earlier (the 8VC decode
  layer, COLLECTION.md §5 proposal).

- **D7: Non-US rows (policy constants).** Every non-USD figure converts at the
  ECB reference rate of its own date (`scripts/fx-convert.py`); a listing
  outside SEC registration takes a web-cited market cap. Registers give
  `status`, not membership (§5 country table): Companies House for the UK
  rows (Monzo, Revolut, Funding Circle, Habito, Atlantic Money, Teya), the
  Handelsregister for the German ones (Raisin, bonify).

- **D8: Control positions (T3 addendum).** Ribbit makes minority venture
  investments; no buyout practice appears in the ADV or on the site. A
  holding that the record shows as a controlling stake is out as
  `control_position`, judged per row (none known at kickoff).

## Deltas (Erik's)

None open. The five deltas PRO-161 listed each resolve under a standing
rule and are recorded above as derivations: public positions after the IPO
(D4, T3), token and crypto positions (D2), Ribbit LEAP (D3), the non-US
portfolio (D7), and the quiet firm with a thin site (the site layers turned
out to be three archived eras plus the live list; §5 archive work, not a
ruling).

## Run-time standing rulings (dated, class-wide, flagged for review)

- **R1: Protocol rows with no equity mark band on the token's network cap
  (2026-09-28; OPEN for Erik).** Solana (Solana Labs, SOL $69.94B) and Aave
  (Aave Labs, AAVE $2.28B) carry no priced equity round of the issuing
  organisation, so the judges banded them on the token's market cap
  (CoinGecko, read 2026-09-28), the basis the a16z and Bain Capital Ventures
  books use for Solana, NEAR, Avalanche and World. Rule A asks for a priced
  event with a citable figure; a traded token's market cap is read here as
  the analogue of a listing's market cap. Where the labs company sold priced
  equity (Offchain Labs for Arbitrum, Nova Labs for Helium, Uniswap Labs,
  Tempo, Lighter), that round is the mark instead. If Erik rules token caps
  out, both rows fall to below_1b with the check recorded.

- **R2: Priced units in a listed company's private subsidiary are a venture
  position (2026-09-28; OPEN for Erik).** Caret Ventures LLC is Safehold's
  subsidiary holding the capital-appreciation interest in its ground leases;
  Safehold's 8-K of 2022-02-15 reports a sale of Caret Units to outside
  investors including Ribbit at an implied $1.75 billion. The firm listed
  Caret 2022 to 2024. Read as a priced placement into a private company
  (member, entry Growth, $1.75B stale), the Waymo reading of a subsidiary
  that sells priced units; the alternative is a structured position in a
  listed REIT's economics (T3, out).

- **R3: A listed company the firm lists is out when its shares traded before
  the firm's first money (2026-09-28; D4 applied).** Bank Jago (IDX: ARTO
  from before January 2021; Ribbit's minority stake announced October 2021),
  Futu, Mercado Libre, Sea and Tinkoff: all `not_member` under T3. The
  single-deal vehicle DH-S (Ribbit Cayman IN Opportunity VI, 2021) decodes to
  Dhani Services, a listed Indian company the firm never listed, so it makes
  no row.

- **R4: A Form D seat is not a position (2026-09-28; Erik's 2026-09-28 ruling
  on unverified venture positions applied).** Thirty Form D rows that
  matched a Ribbit person's name are `not_member`: sixteen at the first pass
  (Craize Snacks, Harbor National, OSIX, Lemon Inc. and twelve namesakes or
  the person's own earlier companies) and fourteen from the widened roster
  after the rebuild (a Buffalo-area Brian McGrath on four companies, Valon
  Technologies where a Brian McGrath sits on the board beside a16z, and
  seats held before or after the person's Ribbit tenure). No round, release
  or listing names a Ribbit fund in any of them.
