# 20VC: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to 20VC (slug `20vc`,
display name always **20VC**; the fund of Harry Stebbings, London, investing
since April 2020 alongside the Twenty Minute VC podcast). The judge cites these
rulings per line. Written at kickoff 2026-09-28 (PRO-76) under the derivation
protocol of COLLECTION.md §1: **derivations** (a standing test applied to
verified facts; no confirmation needed, vetoable), **deltas** (Erik's), and
**run-time standing rulings** (dated, class-wide, flagged for review). PRO-76
asked for three rulings: the media business against the fund, podcast
relationships, and syndicate and SPV participations. All three derive from the
standing tests (D2, D6, D7) and are applied from kickoff, flagged. No delta
remains open at kickoff.

**The structural fact of this run:** 20VC is a young London seed and Series A
firm whose vehicles are Delaware partnerships and platform-administered series
funds, whose portfolio is mostly European, and whose partners sit on almost no
boards. Its SEC footprint is fund-side only: an exempt reporting adviser with a
Section 7.B table, and the funds' own Form Ds. Nothing names a portfolio company
there. What carries the base: (1) the firm's own list (20vc.fund, 79 cards on
2026-09-28, with an Exit flag and sectors but no round and no date; its 2020–2024
generations from the archive), (2) the press, which names 20VC in round
announcements more often than it names most seed funds, because of the podcast
(the recall layer, `scratch/press-sweep.py`), (3) the UK and German share
registers for backtrace, where a row needs a filing, and (4) the recall probe.

**The vehicle-registry finding PRO-76 predicted is real.** The EDGAR company
search is a name-prefix search, so `company=20vc` finds twelve filers and can
never find the five platform series funds, whose names begin with the
administrator's pattern ("Fund I, a series of 20VC, LP"). They are not
co-filers of anything the seed finds, and their Form Ds name AngelList's
Belltower Fund Group, not a partner, so the partner-matched Form D route misses
them too. The adviser is not named after the brand either (Twenty VC LLP), and
IAPD's firm search returns nothing for "20VC". Every route in the registry
returned a clean-looking table with five funds missing, the firm's first fund
among them. D1 resolves them from the adviser's own sworn fund list (Form ADV
7.B) and EDGAR full-text search; the report proposes the config shape and the
verify signal.

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm and its vehicles (T1, same adviser).** 20VC = the funds
  managed by **Twenty VC LLP** (Companies House OC435791, incorporated
  2021-03-02, 16 Berkeley Mews, London W1H 7AY; FCA-registered, Form ADV Item
  1.M; SEC exempt reporting adviser **CRD 316359**, SEC 802-122639, active
  since 2021-10-06, Item 2.B(1) adviser solely to venture capital funds;
  Schedule A: Harry Stebbings, Managing Director, 75% or more, CRD 7242842;
  annual amendment 2025-06-17 per the SEC roster of 2026-09-01, the newest on file, read from
  `data/filings/adv/316359.pdf`). LLP members (Companies House, exact dates):
  Harry Stebbings and The Twenty Minute VC Ltd (designated, 2021-03-02),
  William Goodwin (designated, 2021-03-30 to 2025-04-04), Kieran Hill
  (2021-09-13), Paul Bonnet (2024-08-19), Julien Codorniou (2025-03-24).
  Verified vehicle set (ADV 7.B read 2026-09-28; EDGAR submissions and Form D
  primary documents, `sources/edgar/`):
  - **Fund I, a series of 20VC, LP** (CIK 1808687; Form D 2020-04-07, first
    sale 2020-04-01, $2,080,000 from 28 investors, minimum $5,000; general
    partner "Fund GP, LLC" and manager Belltower Fund Group, i.e. an
    AngelList-administered series fund). The firm's own name for it is
    "20VC Fund I" ($8M and 31 companies, Harry Stebbings on LinkedIn; $8.3M in
    2020, TechCrunch 2020-07-17). Not on the 2025 ADV: it predates the LLP and
    its adviser of record is AngelList Advisors. **IN**: the vehicle bears the
    firm's name, was raised and invested by its founder for the firm, and pools
    28 investors' money; T1's question is whether a vehicle is the firm's or a
    brand-sharer's with its own operation, and a platform acting as adviser of
    record is the arrangement the firm's own ADV reports for its later series
    funds (7.B(2), below). Flagged for Erik because no ADV lists it.
  - **20VC Fund II, L.P.** (CIK 1852410; $33,000,000) and its parallel
    **20VC Explorer Fund II, L.P.** (1852406; $107,000,000), both first sale
    2021-06-14 from 62 investors, general partner 20VC GP II, L.P. (GP of the
    GP: 20VC GP II, LLC; Harry Stebbings managing director): the $140M second
    fund of 2021. 7.B gross assets $37,068,827 and $97,197,156.
  - **20VC Fund III, L.P.** (1921168) and **20VC Explorer Fund III, L.P.**
    (1921021): one co-issued Form D of 2024-04-18 for $400,000,000 (sold $0
    at filing; general partner 20VC GP III, L.P.). The $400M third fund,
    $125M seed and $275M Series A (Sifted, TechCrunch, October 2024). 7.B
    $125,501,224 and $276,103,289.
  - **20VC Fund D-1, L.P.** (1857965; $7,500,000 from one investor, first sale
    2021-06-07; GP 20VC GP II; 7.B $2,868,962) and the AngelList-platform
    **DO Fund I, a series of 20VC FUND D-2, LP** (1868708, first sale
    2021-05-11, $559,406 from 3 investors), renamed **20VC SPV2, a series of
    SAX Capital Series Fund III, LP**, with **20VC SPV1** (1898359, Form D
    2021-12): single-purpose vehicles (D6).
  - **20VC Fund S-1, L.P.** (1886396; $55,722,000 from 5, first sale
    2021-11-22; 7.B $63,971,663), **S-2** (2077933; $12,200,000 from 7,
    2025-07-01), **S-3** (2108553; $10,060,000 from 7, 2026-01-30), **S-4**
    (2108560; $6,485,188 from 14, 2026-02-02), **S-5** (2107393;
    $10,050,000 from 8, 2026-06-29), all under 20VC GP II: single-purpose
    vehicles (D6).
  - **Fund I, a series of 20Growth, LP** (1994833, first sale 2023-10-03,
    $4,960,000 from 9), **Fund I, a series of 20Product, LP** (2010909,
    2024-04, $4,950,000 from 15), **Fund I, a series of 20Sales, LP** (1984365,
    2023-06, $5,000,000 from 14) and **Fund II, a series of 20Sales, LP**
    (2140140, 2026-06, $3,500,000 from 3, minimum $500,000): AngelList-
    administered offshoot funds of the 20Growth, 20Sales and 20Product shows.
    **External** (re-derived at kickoff under T1, same day; flagged). The first
    three are on Twenty VC LLP's ADV under Section 7.B(2), "private funds that
    you advise" reported by AngelList Advisors (802-78135), which first read
    as the firm's own. The funds' own launch disclosures settle it the other
    way: 20SALES "is an offshoot of venture firm 20VC ... but it is a separate
    vehicle entirely", its eight founding partners are its fund managers, and
    "Stebbings, as a limited partner and advisor to the fund, managed its
    fundraising" (TechCrunch 2023-06-21); for 20GROWTH (2023-11-06) and
    20PRODUCT (2024-02-09) "Stebbings is a limited partner and advisor to this
    fund as well", and the partners "will be staying at their current jobs and
    participating in the fund on a part-time basis". Investment decisions sit
    with operators who are not the firm's representatives, which is T1's
    "its own disclosure of independent operation", so a company held ONLY by
    an offshoot fund is not a 20VC member; where 20VC's own funds are in the
    same round (Fyxer's Series A: "led by 20VC, with participation from ...
    20Growth, 20Product"), the row is a member on 20VC's own position. Read
    "20VC Growth" (two words) as 20VC's own growth vehicle, the Explorer fund
    (Digits' Series C of March 2022 names "Harry Stebbings' 20VC Growth"
    twenty months before 20GROWTH existed), and "20Growth"/"20GROWTH" (one
    word) as the offshoot.
  One firm, one investment team, one adviser (and, before it, one founder
  on a platform) → **IN**: primaries, follow-ons and secondaries from any of
  these vehicles. Precedent: Thrive's umbrella with lettered LLCs; Creandum's
  flagship, Select and SPV vehicles under four ERAs.

- **D2: The media business is not the fund (T2, fund money; PRO-76's first
  ruling).** **The Twenty Minute VC Limited** (Companies House 09951526,
  2016-01-14, SIC 59200 sound recording; Harry Stebbings sole director) is the
  podcast business, and is a corporate designated member of the LLP. A
  position it or the podcast holds (equity for sponsorship, advisory equity, a
  media partnership) is not a fund's position → **OUT**. The brand is shared;
  the money is not. **20VC Property Limited** (14169715, 2022, letting) is a
  property company, not a vehicle. Precedent: T2's "OUT where the only
  connection is a person, a program listing or an association".

- **D3: The founder's angel book stays out, even where the site lists it (T2).**
  Harry Stebbings invested personally before the first fund (April 2020) and
  beside it. A company whose only 20VC connection is his personal check is
  **`not_member`**, even on 20vc.fund, unless a 20VC vehicle later held it, in
  which case the row is a member and its entry is the vehicle's first check,
  never the angel check. The listing still suffices for membership by default
  (COLLECTION.md §1): the evidence that turns a listed row out is a dated
  personal check (press or the company naming "Harry Stebbings" as an angel
  before 2020-04 with no fund round after). Precedent: Cherry's D2, Point
  Nine's E1 reversal (Erik, 2026-09-26: "exclude as we did for Cherry"),
  First Round's pre-fund book.

- **D4: Stride.VC is another firm (T1, T4).** Harry Stebbings co-founded
  Stride.VC with Fred Destin and is named an executive officer on both of its
  fund Form Ds (Stride Capital Fund I SCSp, Luxembourg, 2018-06; Stride Capital
  II LP, London, 2021-04, $141,095,150 from 50; promoter Stride.VC LLP,
  Companies House OC417818, FCA FRN 927462, 4 Grotto Passage W1U 4JX). Its own
  funds, adviser and brand. He was a Stride partner when he launched 20VC Fund I
  ("He's also a partner at Stride.vc", TechCrunch 2020-07-17, which gives Fund I
  a US focus and Stride the UK and France) and announced his departure in February 2021
  (TechCrunch 2021-02-07); Companies House dates his Stride.VC LLP membership
  2017-06-19 to 2021-07-08, and his Stride-era directorships (Forward Clinical
  2018-09 to 2021-10, Sedna Communications 2021-06 to 2021-07) are Stride's
  seats (`sources/registers/officer-graph.json`). Earlier still he spent six months at Atomico
  (2016-12 to 2017-05; Wired, Business Insider), whose deals are Atomico's.
  → **external**, and a company Stride backed is not a
  20VC member unless a 20VC vehicle invested in it itself (the Menlo
  partner-carried ruling, Erik 2026-09-17, read from the other side: the money
  behind the seat was Stride's). Two companies sit on both firms' live lists
  (Hofy, TechWolf) and are judged on that question. Both Stride funds are
  `external` in `entities.json`.

- **D5: Project Europe is its own fund (T1, T2, T5).** Project Europe (launched
  2025-03: €200k for 6.66% in founders under 25, from a €10M fund backed by
  20VC, Point Nine, Adjacent and 100+ founders; tech.eu 2025-03-12) is managed
  by **Project Europe Ltd** (16679576, 2025-08-28, SIC 66300 fund management,
  directors Harry Stebbings and Kitty Mayo, 16 Berkeley Mews) through its own
  Scottish partnerships (Project Europe Carry GP Limited SC873561, Project
  Europe Founder Partner LP SL037877 and II SL038085). It is not on Twenty VC
  LLP's ADV. 20VC is one of its backers, i.e. an investor in another fund, so
  a Project Europe company is **not a 20VC member** unless a 20VC vehicle
  holds it directly. Consistent with Point Nine's D7 ruling on the same
  vehicle (2026-09-26: an LP stake in a fund is `not_member`, and its
  portfolio is not the LP's). Flagged: Harry Stebbings directs Project Europe
  Ltd and its CEO appears on 20VC's team page, so a reader may expect the
  cohort on 20VC's page.

- **D6: SPVs and syndicates (T1, T5; PRO-76's third ruling).** The firm's
  single-purpose vehicles are the firm's vehicles: 20VC Fund S-1 to S-5 and
  D-1 (general partner 20VC GP II, the GP of Fund II) and the platform
  vehicles 20VC SPV1 / SPV2 / DO Fund I (named for the firm, run on
  AngelList). **IN**: a company held only through one of them is a member,
  entering at the round that vehicle bought (usually Growth), and a vehicle
  that follows on into a company the funds already hold changes nothing about
  its entry (T5: plumbing). Precedent: Creandum's SPV TR and Select funds,
  Thrive's lettered LLCs, Point Nine's single-company follow-on vehicle. A
  deal-by-deal syndicate led by Harry Stebbings personally before the first
  fund would be his angel book (D3); EDGAR full-text search finds no such
  syndicate under his name, so the class is empty unless a row surfaces one.

- **D7: Podcast relationships are not holdings (T2).** A guest, a sponsor, a
  "friend of the show", a company whose founder Harry Stebbings interviewed, a
  company the podcast or its newsletter recommended: none is a position.
  **OUT** unless a vehicle of D1 invested. The press layer is read with this
  rule, because 20VC is named in far more articles as a podcast than as an
  investor ("told 20VC", "on the 20VC podcast"): a sentence naming 20VC as a
  platform is never membership evidence.

- **D8: Partners' seats are dated against their firm at the time (T4).**
  Julien Codorniou (Felix Capital 2015–2024, founding advisor then partner;
  20VC from the 2024-12-18 announcement, LLP member 2025-03-24), Paul Bonnet
  (DST Global until 2024; LLP member 2024-08-19), Alexandre Dewez (Eurazeo until
  2024), Kieran Hill (LLP member 2021-09-13; before that a partner at the London
  fund Ascension, Business Insider 2024-06-13, and designated member of Ascension
  Media Group LLP since 2014 per Companies House). A deal or board seat of theirs
  from before their 20VC start is their former firm's, whatever the live list
  shows (Julien Codorniou's Agave Games directorship of 2024-11-28 falls inside
  his Felix Capital LLP membership, 2021-12-06 to 2025-03-21; Menlo's
  partner-carried ruling, Erik 2026-09-17). Three live-list cards are named
  in exactly that way: TechCrunch (2024-12-18) says Codorniou "participated
  in funding rounds in Pigment, Omada, TechWolf, and Prediko and Agave" as
  part of Felix Capital and invested "his own money in Bloom & Wild, Xentral,
  Homesome, Olio, Peanut, Nabla, Curio, Bits, and Sunday". **Omada, TechWolf
  and Xentral** therefore need a 20VC vehicle of their own to stay (TechWolf
  has one: 20VC is named a participant in its 2024 Series B, beside Felix's
  lead); without one they are `not_member`, partner-carried. The operator
  partners of the 20Growth / 20Sales / 20Product funds (Elena Verna, Stevie
  Case, Hugo Barra, Gustav Söderström and 22 more) are shown on the team page
  with their own employers; they are not the firm's roster, their personal
  investments are not the firm's, and their employers are not portfolio
  companies by that fact.

- **D9: Fund-shaped and non-company entries (T5).** Fund vehicles, the
  firm's own entities, Project Europe's entities and platform umbrellas (SAX
  Capital Series Fund III, Belltower Fund Group) are never rows. A Form D
  related-person hit on a roster name that is a pooled fund or a homonym is
  dropped or `not_member` (the sweep's three: Crosstown Brewing Co LLC,
  Memphis 2016, "Will Goodwin"; EEM / ECP Ursa I Aggregator, Houston 2023,
  Energy Capital Partners' William Goodwin: homonyms of the LLP member).

## Deltas

None open at kickoff. PRO-76's three named rulings derive under T1, T2 and T5
(D2, D6, D7) and are applied, flagged for Erik in the report.

## Run-time standing rulings

(dated, class-wide, flagged for review)

- **R1 (2026-09-28): a press line naming only Harry Stebbings, the person,
  locates the person (T4), never a fund.** The press names him personally in
  many rounds after April 2020 ("Harry Stebbings (Founder/Host of 20minVC)",
  "angels ... including Harry Stebbings"). Where the firm itself counts the
  company as a fund investment (its own list of 2022-2024 or 2026, or its own
  statement quoted in the press: NexHealth and Spiketrap in TechCrunch
  2020-07-17, Hopin, Clubhouse and RevenueCat in Fortune 2021-06-16), the line
  corroborates the fund's round and dates the entry. Where nothing else names a
  20VC vehicle, the row is `not_member`: the same reading §1 gives a Form D
  related-person name-match, and D3's angel book is exactly what such a line
  cannot rule out (Macro 2020-07, Opal 2021-01, the.com 2022-01; BukuWarung
  2020-09, whose 'partners of DST Global, Soma Capital and 20VC' names people,
  not the fund). Polywork was first read this way on Business Insider's angel
  line and then admitted on Silicon Republic's 'Bungalow Capital and 20VC were
  among the other participants' (2021-08-06). A line naming "20VC", "Harry Stebbings' 20VC", "20VC Growth",
  "20 VC Explorer" or "The Twenty Minute VC" as the investor names the firm.
  Flagged for Erik: it keeps out rows a reader could expect in, if Harry's
  post-2020 checks were in fact the fund's.

- **R2 (2026-09-28): the firm speaking about its own holding on its podcast is
  first-party evidence of the position; D7 excludes the podcast's guests and
  sponsors, not the firm's word about itself.** On the 20VC x SaaStr episode of
  August 2026 'Harry, a Poolside shareholder, said the outcome is roughly a 15x
  for them as a seed investor' (SaaStr's write-up, 2026-08-27): Poolside's
  entry is the August 2023 seed, cited to that write-up at medium confidence.
  The same episode has him speak as a Mercor investor; Mercor is on the firm's
  own list already and its round stays undetermined. A guest founder's remark
  about 20VC, or the podcast naming a company, still proves nothing (D7).
  Flagged for Erik.
