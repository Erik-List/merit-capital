# Speedinvest: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Speedinvest (slug
`speedinvest`, display name **Speedinvest**; the adviser and management company
Speedinvest GmbH, Vienna). The judge cites these rulings per line. Written at
kickoff 2026-09-30 (PRO-84) under the derivation protocol of COLLECTION.md s1:
**derivations** (a standing test applied to verified facts; no confirmation
needed, vetoable), **deltas** (Erik's), and **run-time standing rulings**
(dated, class-wide, flagged for review). PRO-84 asked for rulings on the
vertical funds and on any network or scout programme; both are derived below
from verified facts (D1, D3), so the run starts with no open delta.

**The structural fact of this run:** Speedinvest is a Vienna firm founded in
2011 as a EUR 10M "super angel fund" of 30 private investors, now a
multi-team European seed platform with growth and emerging-markets sleeves. Its
portfolio is overwhelmingly European and outside the SEC; its fund side is
visible there only as one exempt reporting adviser and three 2023 Form D
filings. What carries the base is the firm's own record (the live Webflow CMS,
the 2017-2019 WordPress portfolio captured by Common Crawl, the 2012-2016 site
through the Internet Archive, the Getro job board, the firm's own posts) and,
new to this run, **the Austrian company register read through North Data's
free publication stream**, which names the shareholders of an Austrian GmbH at
each change (D8).

## Derivations (T1-T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm (T1, same adviser; the vertical funds).** Speedinvest = the
  Vienna firm managed through **Speedinvest GmbH** (Firmenbuch FN 363581d,
  founded 2011-05-26, formerly "Speed Invest GmbH" and "Speed Invest Management
  GmbH"; SEC exempt reporting adviser CRD 316774, SEC 802-126139, annual
  amendment 2026-04-01; Schedule A: Oliver Holle and Daniel Keiper-Knorr,
  founding partners since 05/2011), principal office Nordbergstrasse 1/1/71,
  1090 Vienna, with offices in Berlin (Speedinvest Deutschland GmbH), London
  (Speedinvest Limited), Munich, Paris (Speedinvest France Sarl) and Abu Dhabi;
  from 2011 to about 2017 a Silicon Valley office (Santa Cruz, then San
  Francisco; the firm's 2012 and 2016 home pages). Every fund vehicle is a
  Vienna GmbH & Co KG under Speedinvest GmbH or **Speedinvest GP GmbH** (FN
  495024b, founded 2018-07-04, formerly Speedinvest Scouts GmbH) as general
  partner (North Data entity pages, read 2026-09-30,
  `sources/registers/northdata-speedinvest-entities.json`):
  - Flagships: Initial Factor Speed Invest GmbH & Co KG (Fund I, 2011, FN
    365424p), Speedinvest II EuVECA (FN 430189g) with II Co-Invest EuVECA,
    III EuVECA (FN 510598f), IV EuVECA (FN 572350t, Form D CIK 1958034) with IV
    GPC, V EuVECA (FN 664308z, 2025).
  - Vertical and regional funds: Speedinvest F EuVECA (fintech, FN 484860f)
    and f II; Speedinvest Industry EuVECA (FN 492953g); Speedinvest X and x II
    EuVECA (the Network Effects fund, "Speedinvest x", launched January 2018,
    second fund 2020); Speedinvest Emerging Markets (FN 563772b, the Middle
    East, Africa & Beyond team).
  - Growth and opportunity vehicles: Opportunity I EuVECA (Form D CIK
    1958033), Industry & Climate Opportunity EuVECA (CIK 1958031), Growth II
    EuVECA (registered 2025-11-05 as Speedinvest Growth EMEA), AI Opportunities
    I (registered 2026-09-29, Speedinvest GmbH as limited partner).
  - Sixteen Co-Invest GmbH & Co KGs named by two or three letters (AC, AM, BT,
    BT II, CH, CH II, FC, I, IK, MA, OT, PH, SF, TM, UVG, WF): single-company
    co-investment vehicles.
  - Continuation I and II GmbH & Co KG (2024-2025): continuation vehicles
    (Adverity's shareholder list moved from Speedinvest II to Continuation I
    and II in 2025).
  One firm, one adviser, one investment team -> **IN**: primaries, follow-ons
  and secondaries from every fund, vertical, regional, opportunity and growth
  vehicle, and every co-investment vehicle (Creandum's flagship, Select and SPV
  precedent; a16z's vertical families under one adviser). The co-investment,
  continuation and GPC vehicles are plumbing (T5): a position moved through
  them stays a row through its original entry, and a new commitment made
  through one enters at that stage. The ADV's Section 7.B lists ten of these
  vehicles ($1.411B gross); a non-US exempt reporting adviser lists the funds
  it reports to the SEC, so the register is the complete fund tree.

- **D2: Feeders and LP-access structures are external (T5; Thrive IX Access
  precedent).** Kalodion Fonds XX (Speedinvest) GmbH & Co KG (Berlin, HRA
  58441 B) is a third-party private-client feeder into a Speedinvest fund, and
  the 2026 joint venture with SBI Ventures Europe gives Japanese institutions
  "streamlined access to invest in European startups" (the firm's own post,
  2026-03-25): both are LP-side structures. No row rests on either. The firm's
  MicroGP programme, which backs emerging fund managers, is an LP position in
  other funds (the standing exclusion class) and is never a row.

- **D3: The Scouts vehicle and the operating joint ventures (T2; PRO-84's
  scout question; re-derived 2026-09-30 from the register, a clean flip under
  the same test).** At kickoff the facts were: Speedinvest Scouts GmbH & Co KG
  (FN 438506m, founded 2015-08-18) held shareholdings in 23 companies, and
  Speedinvest Scouts International GmbH (FN 443403p, formerly "Pioneers Ventures
  Digital International GmbH") passed to Speedinvest II in 2022; the derivation
  was provisional on whether the vehicle was a scout programme or the firm's own
  small-ticket vehicle. The Austrian register answers it
  (`sources/registers/status-at-de.json`): the Scouts KG is the renamed
  **Pioneers Ventures Digital GmbH & Co KG** (Pikd's register entry: "SH:
  Pioneers Ventures Digital GmbH & Co. KG nun Speedinvest Scouts GmbH & Co.
  KG"), a fund vehicle Speedinvest took over in 2015, and its stakes moved into
  Speedinvest II EuVECA in 2021-2023 (GoStudent, Prewave, Refurbed, Timeular,
  Tripmakery, Zerolens: "Shareholder: Speedinvest II EuVECA ... No longer
  Shareholder: Speedinvest Scouts"). It is the firm's own early-stage vehicle,
  not a scout programme, so T2 reads **IN**: a fund of the firm held the
  position. What the flip does not settle is the entry of a position the
  Pioneers vehicle held before Speedinvest took it over; such a row's entry is
  the round Speedinvest's money first went into, else `undetermined`.
  **Speedinvest Heroes Consulting GmbH** (FN 465427b, HR and recruiting) and
  **Speedinvest Pirates GmbH** (FN 483385k, growth marketing) are the "two
  joint ventures that offer HR and growth services" of the firm's 2022 post:
  operating services, not investments. A company that received their support
  with no fund position is OUT (Project A D5 precedent).

- **D4: The growth desk (T1, T3), and the seven listings without a year (T3,
  sale consideration; re-derived at kickoff from the firm's own words).** The
  live site's Growth team ("Since 2019, we've made 20+ growth investments ...
  Writing EUR 5-30M checks from Series B to pre-IPO", with NEA as strategic
  partner) invests from the Opportunity, Growth and co-investment vehicles of
  D1, so its rows are IN, and a secondary or tender in a private company is a
  Growth entry (policy constant). The seven live listings with no "Year
  Invested" were first read as possible growth secondaries; the firm's own card
  for each says otherwise, in the same words every time: "Speedinvest became a
  shareholder in Dialpad following its acquisition of Surfboard in 2024", and
  likewise Mews (Flexkeeping, 2025), Mistral (Emmi AI, 2026), MoonPay (Iron,
  2025), OpenAI (Ona, 2026), Perk (Yokoy, 2025) and Taxfix (TaxScouts, 2024).
  The Austrian register confirms one of them independently: Emmi AI GmbH (FN
  643484a, Linz, Speedinvest IV a shareholder) became Mistral AI Austria GmbH on
  2026-07-17 with Mistral AI SAS its sole shareholder. The standing rule (Erik,
  2026-09-22) decides all seven: **`not_member`**, the acquirer out and the
  acquired company the member, reading `acquired`. Written into
  `config.verify.not_members`. A clean re-derivation under the same test,
  recorded, not escalated.

- **D5: Sale consideration (T3 standing rule, Erik 2026-09-22, and the
  share-swap extension of 2026-09-26).** A company the firm lists only because
  it bought a portfolio company is `not_member` with the acquired company
  named. Checked per site-listed acquirer before it seeds member; written into
  `config.verify.not_members` as found.

- **D6: The roster (T4).** The sweep roster is the investing people only: the
  live team page's investment teams (AI & Infra, Climate Tech & Industrial
  Tech, Deep Tech, Fintech & DeFi, Growth, Health & Bio, Marketplaces &
  Consumer, Middle East, Africa & Beyond, the Management Team), the Form D
  related persons of the three 2023 filings (Holle, Keiper-Knorr, Ockenfels,
  Zahnt, Sieghart, Flock, Ametsreiter, Zitna, Shikhantsova, Arts, Lang,
  Schwarzenbrunner, Hao), the ADV Schedule A, and the archived 2017-2019 team
  pages with capture-year tenure windows. Operations, legal, finance, people,
  communications and portfolio-success staff are left out.

- **D7: Person or firm (T4).** Standard seat dating. The roster-name Form D
  sweep reaches only US-incorporated members of a European book and is expected
  to be homonym noise; every name-match needs affirmative corroboration and,
  lacking it, is `not_member`. Partners' personal angel books are out (Cherry
  D2, standing since 2026-09-26), including the founders' pre-2011 angel
  positions.

- **D8: The Austrian and German recipe.** Cherry's conventions apply: an
  insolvency followed by an asset sale reads `acquired` with a successor note;
  a filing with no sale yet reads `defunct` (Erik, 2026-09-07); the home
  register's dissolution, liquidation or insolvency entry is filing-grade
  `defunct` evidence. For Austrian companies the register is the Firmenbuch:
  North Data's free entity page carries its publication stream, including
  shareholder changes with the holders named when few ("Shareholder: Speedinvest
  Continuation II GmbH & Co. KG, Speedinvest II EuVECA GmbH & Co. KG"), which is
  filing-grade membership corroboration (a fund of the firm on the company's
  shareholder register) and, for a register-only company, filing-grade
  membership evidence (class `fund_filing`). The Ediktsdatei
  (edikte.justiz.gv.at) is the free insolvency layer. Non-USD figures convert at
  the ECB rate of their own date (`fx-convert.py`); a listing outside SEC
  registration takes a web-cited market cap.

- **D9: No entry-date window.** The book starts in 2011; every row is judged
  on the same evidence, and where the record does not give the round the stage
  reads `undetermined` (PRO-137).

- **D10: The firm's own stage fields (COLLECTION.md s5).** The live site
  publishes no round word per company; its "Year Invested" is a close-year
  anchor (Menlo rule), never a label. Archived surfaces are checked for a round
  field; any found rides in the queue as evidence and labels only after it is
  scored blind against the book's documented entry rounds. The Getro board's
  `stage` describes the company today and is refused without re-scoring
  (standing since Thrive and Lux).

- **D11: Speedinvest Digital East (T1; provisional on its vehicle).**
  Facts: a 2017-2018 division for Russia, the CIS and Eastern Europe, planned
  at EUR 25M, led by partner Michael Breidenbruecker; the firm's 2018 team page
  titles Breidenbruecker, Ilia Dubinsky and Lena Krauzova "Partner/Associate,
  Speedinvest Digital East"; a UK company Speedinvest Digital East Limited
  (Companies House 11253525, incorporated 2018-03-13, since dissolved). T1's
  default is IN for every office and sleeve of the one adviser, OUT only for a
  brand-sharing entity with its own adviser, fund family or disclosure of
  independent operation. On the facts found the desk is the firm's own team
  under its own brand and partners, so its positions are **IN** where the firm
  lists them; the dissolved UK company is a vehicle name, not a separate
  adviser. Provisional: if the run finds Digital East raised and managed its own
  fund outside Speedinvest GmbH, its rows re-derive OUT under T1 and the flip
  is reported. **Found (recall probe, 2026-09-30):** the firm's January 2019
  portfolio page carried a 'Digital East' filter counting one company, Scalarr
  (invested 2018, Investment Manager Ilia Dubinsky); it is on the firm's live
  list, so the derivation stands and moves no row.

## Deltas (Erik's)

None. PRO-84's two named questions (the vertical funds; network or scout
programmes) are derived above (D1, D3). Anything the grind finds outside every
test is raised at close (s9).

## Run-time standing rulings

(dated, class-wide, flagged for review)

- **R1 (2026-09-30; WITHDRAWN 2026-10-01, see the last section): a cited, unnamed entry round with a stated amount is banded
  by the era ceilings (COLLECTION.md s6 applied; flagged for review).** The firm
  publishes no round word, and the Austrian and German press often report a
  first round by its amount alone ("Speedinvest leads EUR 1.5 million round").
  An electronic Form D round has the same shape (an amount, never a name) and
  s6 bands it by era: below a quarter of the seed ceiling Pre-Seed, up to the
  ceiling Seed, up to the Series A ceiling Series A. The same band is applied
  where the round Speedinvest first joined is cited on a non-vendor page that
  names Speedinvest and states the amount, with the older-company guard of
  PRO-157 (no early band on a company three or more years old at the round,
  and none where no founding year is on record). Source `model` (rung 3, the
  deal named in the note); a Seed band carries `stage_uncited` at low
  confidence and its graduation is decided on its own evidence (PRO-131 b).
  16 rows (scratch/band_unnamed.py): Seed 10, Pre-Seed 4, Series A 2. A round
  with no amount stays `undetermined`. The alternative, leaving all of them
  `undetermined`, is Erik's call.

- **R2 (2026-09-30): the firm's 2018-2020 Pre-Seed filter tag labels at medium
  (D10 applied).** The archived listing's `pre_seed` filter marks the firm's own
  Pre-Seed Program (Markus Lang, "Head of Pre-Seed Program" on the 2018 team
  page): the firm's claim about the round IT entered, so eligible. Scored blind
  against independently documented entry rounds it agrees on 3 of 3
  (scratch/preseed-score.json); the sample is far below the 30 rows `high`
  needs, so every row it labels is `first_party` at `medium`, cited to the
  archived listing, and a documented round overrides it.

- **R3 (2026-09-30): a merger successor the firm lists beside the original is
  the same position (D5 applied).** Invesdor (bought Finnest, 2019), SILQ
  (formed by merging ShopUp with Sary, 2025) and Dott (TIER merged into it,
  2024) are `not_member`; Finnest, ShopUp and TIER are the members. Finnest and
  ShopUp read `acquired` with a successor note; TIER's status follows the A/B
  pass.


## Settled on 2026-10-01 (Erik: at most three open rulings; settle by rule or by research)

Erik's instruction after the first closing message: align wefox in both books,
cross-investor alignments need no approval, and open rulings are reduced "by
either following rules or investing in research". The fourteen items the report
first listed as open were each settled by a standing rule or a lookup.

- **R1 is withdrawn.** COLLECTION.md s6 already speaks: the stage label
  "follows what the firm and the record call the round, not the check size",
  and a round the record does not name reads `undetermined`. The amount band
  belongs to Form D filings only. The 19 rows it had labelled (Seed 11,
  Pre-Seed 6, Series A 2) read `undetermined`; their cited rounds stay in
  `funding_rounds`. Billie keeps `Seed` on the playbook's lowest rung (`model`
  at low confidence, `stage_uncited`): vendor profiles call its 2017 round a
  seed and no citable page names it.
- **R2 and R3 are rule applications, not rulings.** The Pre-Seed tag labels at
  the confidence its score earns (s5). A merger successor is the same position
  (s1, sale consideration and share swaps): ShopUp reads `acquired` because the
  merged group SILQ is a new parent; TIER reads `private` because Tier Mobility
  SE is the surviving parent of the combined company.
- **R4 (2026-10-01): Spiko is a member, high confidence.** The firm's own list
  of its portfolio (Crypto 50 EMEA post, 2026-08-18) names it with ten others;
  nine of those are positions on the firm's own site and the tenth (Request
  Finance) is a real holding received as sale consideration, so the list is
  accurate wherever it can be checked. A firm's own listing suffices (s1), and
  Spiko bought no portfolio company. Its round is not public: stage
  `undetermined`.
- **R5 (2026-10-01): Heroes Jobs is `not_member`.** The only tie is a partner's
  board seat on the company's two Form Ds. Researched: TechCrunch's sale story
  names no investor, the firm's 2020 post lists the company in a market map
  without calling it a portfolio company, no archived listing or team page
  carries it, and the filing gives the company's own address for the director.
  Only vendor profiles name Speedinvest, and a vendor profile does not cite.
  Erik's ruling of 2026-09-28 (a row stays only if verified to be a venture
  investment; a board seat alone is out) decides it. The row left the base at
  the third rebuild.
- **R6 (2026-10-01): Trending Topics stays rejected.** The company's own 2017
  post names Speedinvest in a consortium that bought 16.7% for EUR 170K; the
  Firmenbuch page (FN 480593f) records five persons and seven companies as
  holders without naming them, and no Speedinvest fund appears in any later
  change. T2 asks whether a fund held the position; nothing shows one did, and
  the firm has never listed it.
- **R7 (2026-10-01): wefox's headquarters is Zurich.** The group's imprint
  names wefox Holding AG, Zurich, and its About page gives Austria, the
  Netherlands and Switzerland as its markets, Germany no longer among them.
  Seedcamp's row was aligned to the same city.
- **Rule-decided, no ruling needed:** the rows that rest on the firm's job
  board are members (a job board is a first-party list, s5); entries first
  held by the Pioneers Ventures vehicle read `undetermined` because that round
  is unnamed (D3, s6); Polaron and Playbrush likewise; GoStudent, TIER and
  wefox read below $1B on documented collapse (s6: a lead investor's published
  write-down, a priced merger, a sale backed by the last round's lead); the
  eight acquirers the firm lists are out (D5).
- **Flagged debt, not a ruling:** Criad, Originator, Obey and Bleep carry the
  home-desk country with `country_prior`; their own sites give no location.
- **Other books.** a16z's June cannot be tied to a company (june.so's own
  funding post names no a16z fund; neither does the June oven's record), so it
  reads as a16z's unnameable row. YC's Diligent and June were aligned once the
  cause of YC's readback difference was found (a leading space in one name).
