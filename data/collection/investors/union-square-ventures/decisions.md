# Union Square Ventures — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Union Square Ventures
(slug `union-square-ventures`, display name always **Union Square Ventures**;
the slug spells the name out so the `USV` acronym never keys a cross-investor
match). The judge cites these rulings per line. Phase 0 (PRO-86) was researched
2026-09-05 and **confirmed by Erik 2026-09-05** ("phase 0 confirmed") as seven
items; the facts under them were re-verified at kickoff the same day and this
file records the verified facts. Written under the derivation protocol of
COLLECTION.md §1: **derivations** (a standing test applied to verified facts,
vetoable, no confirmation needed), **deltas** (Erik's), and **run-time standing
rulings** (dated, flagged for review).

**The structural fact of this run:** the firm publishes one live list surface,
`usv.com/companies/`, a server-rendered table of 216 rows whose "FIRST
INVESTMENT" column states the firm's own entry round and year per company
("Series A, 2026"; 13 rows carry a bare year), an exit-detail column ("Acquired
by Yahoo!", "NYSE: NET"), a per-company Sector / Status / Entry Point taxonomy
(read off the filtered pages) and a "Read the Post" link into a 3,807-post
writing archive that announces most investments back to 2004. Five archived
listing eras (2005–2009 unionsquareventures.com/portfolio.html, 2010–2012
usv.com/investments, 2013–2015 and 2016–2019 usv.com/portfolio, 2019– /companies/)
carry the survivorship correction and, in 2013–2019, the firm's own entry-round
labels as they stood then. The firm is an **exempt reporting adviser** (not an
RIA, as Phase 0 assumed): Form ADV 802-75126, CRD 162375, so there is no Item
5.F regulatory AUM and the 26 Section 7.B private funds ($3.24B gross asset
value, 2026-03-27 amendment) anchor the profile instead.

## Facts re-verified at kickoff (2026-09-05)

- **Adviser.** UNION SQUARE VENTURES, LLC, CRD 162375, SEC file **802-75126**
  (exempt reporting adviser, Item 2.B venture capital fund adviser exemption;
  annual amendment filed 2026-03-27, IAPD). Principal office **817 Broadway,
  14th Floor, New York, NY 10003** (Item 1.F). Phase 0 carried 915 Broadway,
  19th Floor: that is the address the fund vehicles filed from on EDGAR before
  the move; the EDGAR business addresses are re-read when the issuer filings
  land and both addresses are treated as the firm's.
- **Vehicles (EDGAR registry, 38 own entities; ADV 7.B, 26 funds).** Core
  funds: Union Square Ventures 2004 LP (CIK 1309626), 2008 LP (1430207), 2012
  Fund, L.P. (1532179), USV 2014 (1597790), 2016 (1668248), 2019 (1762444),
  2021 (1833921), 2022 (1918666), 2024 (2027326) and **USV 2026, LP
  (2144844)**, filed after the ADV. Opportunity: Union Square Ventures
  Opportunity Fund LP (1508427, the 2010/2011 fund), USV Opportunity 2014
  (1597793), 2019 (1762450), 2022 (1918672), **2026 (2144843)**. Climate: USV
  Climate 2021 (1833778), 2022 (1936843). Bundled: USV Bundled 2021 (1833676),
  2022 (1924245). Parallel "Investors" vehicles beside each (USV Investors 2012
  Fund, 2014, 2016, 2019, 2021, 2024, 2026; Opportunity Investors 2014, 2019,
  2026; Bundled Investors 2022; Climate Investors 2021). GP and principals
  entities: Union Square GP 2004 / GP 2008 / 2012 GP / Opportunity Fund GP /
  Opportunity GP, USV Opportunity 2014 GP, Union Square Principals 2004 (a
  Delaware multiple series LLC). ADV 7.B gross asset values by fund are in
  `scratch/adv-7b-funds.json` (sum $3,235,446,464; the largest: USV 2016
  $514M, USV Opportunity 2022 $388M, USV 2014 $323M, USV 2024 $282M).
- **Partners with personal SEC CIKs** (Forms 3/4 as directors of public
  portfolio companies): Burnham (1640018), Buttrick (1640011), Weissman
  (1640012), Wenger (1640014); the registry desks them `external` /
  `outside-cofiler` so their personal filings are never crawled as firm
  positions (person-level attribution rule, §1). Wilson's personal filings, if
  any, are treated the same way.
- **Site.** WordPress; the `company` post type has no REST route; the list is
  parsed from the rendered table (`sources/site/live-companies.json`, 216
  rows, 203 with sectors; status terms current 148 / acquired 37 / inactive
  15 / public 15 / exited 1; entry-point terms mirror the labels exactly:
  Series A 102, Seed 64, Series B 20, Series C 5, Series D 5, Series E 2,
  Common 3, Token 2, none 13).

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1 — The firm (T1, same adviser).** Every vehicle above is under the one
  adviser (CRD 162375) and the one partnership: core, Opportunity, Climate,
  Bundled and every parallel "Investors" vehicle are instruments of one firm →
  **IN**. The 2004 and 2008 funds predate electronic Form D and their deals
  enter through the site list, the archived listings and the firm's posts.
  Precedent: a16z's families under one adviser, Thrive's lettered vehicles,
  Creandum's Select funds. (Phase 0 item 1, confirmed.)
- **D2 — One desk (T1 strategy partition).** Core, Opportunity and Climate
  share adviser, partners and office; none is a non-venture strategy, so no
  `other_desk` partition applies. A row's `entry_stage` is the round the firm
  first entered, never the vehicle that held it: the Opportunity funds' rows
  (Lending Club's Series D, Stash's Series D, Suno's Series D) are Growth
  entries because the rounds were, and a Climate-fund seed is Seed. (Phase 0
  item 2, confirmed.)
- **D3 — Namesakes (T1, T5).** Verified by CIK and address, never by name:
  Union Square Advisors LLC (CIK 1368453, M&A boutique), Union Square Park
  Capital Management / Park GP / Park Partners LP and Offshore (1666231,
  1919051, 1636137, 1666228; a hedge fund), Union Square Partners L P (1394193,
  the PE firm formerly Capital Z Partners III), Union Square Capital Partners
  LLC (PA), Union Square Hospitality Group / Union Square Cafe Corp (1634044),
  Union Square CDO Ltd, Union Square Apartments (CO), Union Square Food
  Concepts (OK), Union Square Investment Co (1056463), Union Square Special
  Purpose Vehicle 1 LP (CA), NNN Union Square LLC — `external` in
  `config.json` `desks.classify[0]`. The letters USV inside an unrelated
  issuer name, and Square/Block itself, are portfolio-side questions for the
  judge, not registry entities. (Phase 0 item 3, confirmed.)
- **D4 — Programs and scouts (T2).** Verified on the live site, the five
  archived eras and the writing archive: the firm runs no scout, angel or
  accelerator program. The two-year analyst program is staff, not capital.
  Scout-class rows, if any surface, are out unless a main fund followed
  (standing rule). (Phase 0 item 4, confirmed.)
- **D5 — Instruments (T3).** Primaries IN; secondaries and tenders IN as
  Growth entries; the site's three **"Common"** rows are read as the firm
  itself labels them, purchases of common stock: **Stripe ("Common, 2014")**
  is a secondary purchase in a private company → a venture entry at scale,
  Growth, member (this overrides Phase 0's "do not seed Stripe": the firm's
  own listing is sufficient evidence, and the label names the instrument);
  **Tucows ("Common, 2017", NASDAQ-listed since the 1990s)** and **Marley
  Spoon ("Common, 2019", ASX-listed since 2018)** are purchases of a listed
  company's stock with no venture entry → `not_member` under the standing
  post-RIA public-purchase rule (D6), flagged for Erik's review because the
  firm lists them as portfolio. (Phase 0 items 5 and 6, confirmed; the
  Tucows/Marley Spoon reading is the derivation, raised in the report.)
- **D6 — Post-RIA public or secondary purchases with no venture entry — OUT**
  (standing rule since 2026-09-03; Phase 0 item 6, confirmed). A row that
  entered through a venture round stays in after it goes public: Twitter,
  Etsy, Zynga, Lending Club, Twilio, MongoDB, Cloudflare, Coinbase, Duolingo,
  Funding Circle, Wattpad (Naver), Shapeways (SPAC) are members whatever
  their later listing.
- **D7 — Token positions and crypto funds (T5, standing token and
  fund-shaped rules).** A listed token maps to its issuing organization or
  is out: **Polygon ("Token, 2022")** → Polygon Labs; **Glow ("Token,
  2024")** → the Glow organization, judged in the grind; Algorand, Arweave,
  Helium (Nova Labs), Dapper Labs, Matter Labs, Ceramic/3Box Labs, Blackbird
  Labs are operating companies. The six site-listed **crypto funds** the firm
  backed as a limited partner (the 2018 post "Investing in Token-Focused
  Funds": Autonomous Partners, Multicoin Capital, BlockTower Capital,
  MetaStable Capital, Polychain Capital, Placeholder) are LP stakes in other
  funds, not venture-outcome operating companies → `not_member` (T5;
  fund-shaped list entries; a16z ruling 6 precedent), preserved in
  `excluded.csv` and counted in the report. **Numerai** is a member: the firm
  led the Series A of Numerai's management company (2016 post), an operating
  company that runs a fund. **Bright Moments DAO** is judged under the token
  rule (a DAO with treasury and governance maps to an organization).
- **D8 — Person or firm (T4).** Carried verbatim from §1: ex-partner filings
  out, partners' personal Section 16 filings out, LP stakes out, evidence
  sufficiency unchanged, seats dated against the person's firm at filing
  time. The roster windows in `sources/wayback/partner-roster.json` are the
  dating instrument: Andrew Parker (2006–2010, then Spark), Charlie O'Donnell
  (2004–2006, then First Round / Brooklyn Bridge), Eric Friedman (2008–2010,
  then Foursquare as an operator), Christina Cacioppo (2010–2012; **Vanta**,
  her 2018 company, is not a USV position), Joel Monegro (2014–2017; then
  **Placeholder**), Rebecca Kaden (Maveron seats before 2017-10 are
  Maveron's), Gillian Munson (2019–2021; XO Group before, Vimeo after),
  Jared Hecht (Venture Partner 2024–; **GroupMe** and **Fundera**, his own
  companies, are founder filings), Michael Mignano (GP 2026–; **Anchor**,
  which the firm's own welcome post says USV did not invest in, and his
  Lightspeed-era seats are not USV seats). (Phase 0 item 7, confirmed.)
- **D9 — Fact flips recorded (same tests, verified facts).** (a) The adviser
  is an ERA, not an RIA (Phase 0 said "adviser CRD 162375" without the
  distinction): T1 unchanged, profile mechanics change (no Item 5.F; 7.B
  gross assets anchor AUM). (b) Address 817 Broadway per the 2026 ADV, 915
  Broadway per the funds' filings: both the firm's. (c) A 2026 vintage (USV
  2026, LP; USV Opportunity 2026, LP; their Investors vehicles) filed on
  EDGAR after the ADV: IN under D1. (d) Stripe is site-listed ("Common,
  2014"): D5 applies and the Phase 0 "do not seed" note is superseded by
  the firm's own listing.

## Deltas confirmed by Erik (2026-09-05, PRO-86 Phase 0)

Items 1–7 of the issue as written; the derivations above restate them
against the verified facts. No delta beyond the standing rule set was needed:
every Phase 0 item is T1–T5 applied to this firm.

## Evidence rules specific to this run

- **The site's "FIRST INVESTMENT" label is a claim scored on the gate before
  it is class 1** (§4, §6): the Lightspeed precedent. Where the label
  disagrees with a documented round — the firm's own contemporaneous post or
  press naming the round — the label follows the record, flagged
  `stage_disputes_band` with the citation (Etsy: site "Seed, 2007", the
  firm's June-2006 post and press place the entry in the June-2006 friends
  round → Seed, 2006; Zemanta: site "Series A, 2008", the firm's own
  September-2008 post calls itself a seed investor → judged on the gate).
  Thirteen rows carry a bare year and no round: the round comes from the
  post or press, or the row keeps `stage_uncited`.
- **The site's exit column and Status term are status evidence, not labels**:
  "Acquired by X" seeds `acquired` with the acquirer; a stock ticker seeds
  `public`; `inactive` (15 rows) is checked case by case (Wesabe, Tasty
  Labs, Brewster, Canvas, Turntable, Kitchensurfing, OB1, Recount Media,
  RealtyShares, Brilliant Planet, AMEE, Buglabs, Oddcast, Assembly, Props are
  candidates for `defunct` or `acquired`, never assumed); `exited` (Rupa
  Health) means the firm sold, the company continues.
- **Archived listings are the survivorship layer**: companies on the
  2005–2019 listings and absent from the live list (Code Climate,
  CoverWallet, PayJoy, Shippo, Pilot Fiber, Yieldmo, InfoNgen, Flurry,
  Hashable, GetGlue and others) are members by listing and are classified
  like every other row.
- **The firm's writing archive is the primary citation source** for
  `entry_stage` (class 1: the firm's own post naming the round), with press
  as the cross-check on the visible slice.

## Run-time standing rulings

Dated, class-wide, flagged for Erik's review; added during the run.

- **R1 — Unlisted in-tenure director seats are the personal-seat class** (agent,
  2026-09-05). USV's own list is exhaustive: it carries LP fund stakes and
  public-stock purchases, and every announced deal has a post. So a Form D
  that names a current partner as director on an issuer the firm never listed
  in any era, with no announcement, is a personal or other-firm seat, not an
  unannounced fund position — `not_member` under the a16z narrowing (identity
  never resolved, no announcement). Applied to Creators Collective, DNA Media
  Technologies, Uneven Labs, Gabeau Corp., UPCOMPANY, Smart Balloon, Zerion,
  Thirty Madison's 2017 seed (Weissman's angel seat). Where the issuer DID
  resolve to a listed company under its legal name, the row merged instead
  (Adelante = ADDI, Digicash = alt.bank, Nvest = SigFig, Pollen = C2FO, Ryzac =
  Codecademy, Narvii = Amino, Distributed Creation = Splice, WP Technology =
  Wattpad, Helium Systems = Nova Labs, Leapfrog Power = Leap, iShopShops =
  ShopShops, GIC Technologies = The General Intelligence Company).
- **R2 — Public-stock purchases the firm lists as portfolio** (agent,
  2026-09-05; D5/D6 applied). Tucows ("Common, 2017": the firm's own post says
  "we have never before invested in a public company") and Marley Spoon
  ("Common, 2019": an ASX-listed company, an Opportunity Fund placement) are
  `not_member` under the standing post-RIA public-purchase rule even though
  the firm lists them. Raised for Erik as the one derivation that removes
  site-listed rows on a rule the firm itself does not apply.
- **R3 — Site-listed LP stakes in crypto funds are not rows** (agent,
  2026-09-05; T5 applied): Autonomous Partners, Multicoin Capital, BlockTower
  Capital, MetaStable Capital, Polychain Capital, Placeholder — the firm's
  2018 "Investing in Token Focused Funds" post describes them as fund
  commitments. `not_member`, preserved in `excluded.csv`. Numerai (the firm
  led the Series A of the management company) and the DAO position (Bright
  Moments, a token purchase into a governed treasury) stay in.
- **R4 — The site's entry-round label is class 1, and the record beats it**
  (agent, 2026-09-05; gate result). Scored 51/52 on the live list and 87/89 on
  the 2013–2019 archives, the label is `web_verified` (cited to the list
  page, medium confidence) wherever the firm's post or press names no round.
  Where the firm's own contemporaneous post contradicts the label the record
  wins with `stage_disputes_band`: Zemanta (post: "as seed investors"; press:
  a $650K seed → Seed, not Series A), Wesabe (post: "we did lead the Series A"
  → Series A, not Series B), CoverWallet (post: "a follow-on to CoverWallet's
  seed round" → Seed, not Series A), Reservoir (post: "co-leading Reservoir's
  pre-seed financing in 2021" → Pre-Seed 2021, not Seed 2022). The Form D
  band scored 8/25 and labels nothing.
- **R5 — Bare-year rows take the round from the record or stay
  `stage_uncited`** (agent, 2026-09-05). Thirteen live rows carry only a year:
  Numerai (post names the Series A), Protocol Labs (equity round unnamed →
  Series A, low, `stage_uncited`), Human Dx / Casetext / Clarifai (the
  2013–2019 archived labels supply the round), Anon (press: seed), Bright
  Moments DAO (a token purchase, Seed low), the six LP fund stakes (out).
- **R6 — Merger successors and renames are one row under the firm's current
  rendering** (agent, 2026-09-05; identity-merges.json): Hailo → mytaxi →
  FREE NOW, Pinch Media → Flurry, Onename → Blockstack → Stacks, YouNow →
  Props, Instant Information → InfoNgen, Patch Homes → Noah, SilviaTerra →
  NCX, THE Football App → Onefootball, DroneBase → Zeitview, Flip →
  Caretaker, Sift Science → Sift (the build keeps the archived rendering),
  AdaptiveBlue → GetGlue, 10gen → MongoDB, eShares → Carta, REVOS → BOLT.
- **R7 — Sale consideration is not an entry** (standing §1 rule applied):
  the 2022 Thirty Madison Form D naming Weissman and Kaden is the Nurx merger
  consideration; Nurx carries the exit. Viggle (GetGlue), Vimeo (VHX),
  Skillsoft (Codecademy), WeWork (Meetup), Patch/AOL (Outside.in), Yahoo
  (Tumblr, Flurry, Delicious), Google (FeedBurner, Firebase) are acquirers,
  never rows.

Verdicts live in `base-verification.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded rows
are preserved in `excluded.csv`, never deleted.

## Run-time rulings, A/B pass and close (2026-09-05, session 1, continued)

- **R8 — Acquired rows carry no figure and band `below_1b`.** The convention every
  landed run follows (a16z: Twitter's $44B take-private and Zynga's $12.7B sale
  both `acquired/below_1b`; Sequoia and Spark: Tumblr's $1.1B sale likewise); the
  exit price lives in the note. Applied to Stash (Grab, $425M enterprise value,
  announced 2026-02-11), Farcaster (Neynar, January 2026, Merkle Manufactory
  returning the full $180M raised: an acquisition with capital returned at cost)
  and Veniam (Nexar, 2022-08-03, undisclosed). `record` enforces the first half
  ("acquired carries a valuation" rejects the line).
- **R9 — Token positions band on the issuing organization's own valuation
  statement, never on a token market cap.** Polygon ("Token, 2022") reads
  `1b_plus` at the $2B the company itself told CNBC on 2022-02-07 (the $10B–$20B
  range circulated only in secondary reports); Matter Labs and Protocol Labs stay
  `below_1b` with no equity mark, aligned with a16z's rows, which use the ZK and
  FIL network caps only as proxies for the figure. Diem (Libra Association) is the
  token rule's consortium case: member, `defunct`, `Growth`, as a16z and Thrive
  carry it.
- **R10 — The site's `inactive` label is class-1 status evidence for `defunct`
  unless the record shows the company operating.** Fifteen live rows carry it;
  twelve are `defunct` or `acquired` on the record. Three stay `private` with
  `model_disputes_source`: Props (the YouNow app is live and last updated June
  2026), Brilliant Planet (Watershed deal, WSP and Mott MacDonald facility work
  in Morocco 2024–2025, no wind-down found) and Oddcast (SitePal and Voki still
  sold). `exited` (Rupa Health) reads `acquired`.
- **R11 — Aggregator valuations never band a row** (ruled by Erik 2026-09-06 as Rule A, the standing rule for every investor; COLLECTION.md §7). PitchBook, CB Insights,
  Tracxn, Contrary, Sacra and Forge marks go to the note; a `1b_plus` band needs
  a priced round, tender or public float with a citable figure. Applied to
  Justworks (`below_1b` with Thrive; Spark's $2.53B PitchBook mark is an accepted
  cross-ruling for the wave), OneFootball (the CB Insights $1.1B of April 2021 and
  the "unicorn" press of the 2022 round carry no primary figure — `below_1b`,
  unicorn-list entry disputed) and Hume AI (Contrary's $219M moves to the note).
  Every one of the 23 `$1B+` figures cites a primary or a market-cap page.
- **R12 — Recall additions are named so that `norm_words` is not a prefix of an
  existing row.** The base build's name-variant rule merges prefix pairs unless a
  single listing snapshot names both; "Brilliant" (Brilliant.org, the learning
  company) was folded into Brilliant Planet and silently lost on the first
  rebuild. Renamed to "Brilliant.org" (`brilliant-org`) and rebuilt once more —
  the run's only deviation from the one-rebuild rule, corrective and cost-free
  (the delta queue was seven rows).
- **R13 — Cross-investor slug variants stand as the site renders them.** The
  invariant compares rows by CIK and name key, so Matter Labs (`matter-labs-zksync`
  here, `matter-labs` at a16z), Sift (`sift-science` / Spark `sift`), Dapper Labs
  (`dapper-labs` / Accel `dapper`), Foursquare (`four-square` at a16z), Granola,
  Zerion, Sidecar, Koko, Dia&Co and Stacks are compared correctly but would be
  separate `slug` rows in the companies table; listed in report.md for the wave
  alignment rather than merged unilaterally.
- **Phase 0 items 1–7 confirmed by Erik before kickoff** ("please collect USV;
  phase 0 confirmed"); re-verified facts are in the section above. Two
  deviations from the Phase 0 text, both ruled during the run and raised in
  report.md §7: Stripe is a member (D5: the site's own "Common, 2014" row is a
  documented secondary entry, `Growth`) although Phase 0 said not to seed it on
  the gate (it was not seeded); the firm's office is 817 Broadway (site, ADV
  Item 1.F) while the Form Ds still say 915 Broadway (`hq_location` reads
  "New York, NY" from 25/25 own filings either way).
