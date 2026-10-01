# Lakestar: investor-specific decisions (PRO-108)

The judge cites these rulings per line. Part 1 derives the boundary from the standing tests of
`data/collection/COLLECTION.md` §1 (T1 to T5) on verified facts. Part 2 holds the deltas PRO-108
names, each ruled once. Part 3 holds the rulings made during the run, dated and flagged for review.

Facts were verified 2026-10-01 unless a line says otherwise. Sources are named per line; the
register pulls are in `sources/registers/`, the EDGAR pulls in `sources/edgar/`.

## Part 1: derivations

### D1. One firm, no brand-sharing entity (T1: IN)

- **Facts.** Lakestar Advisors GmbH, Zurich (UID CHE-114.605.813; Zefix: formerly Brightsquare
  Consulting GmbH, purpose "acquiring, holding and selling participations and advisory services",
  owned by Hommels Holding GmbH of Zug until 2023) operates the site and advises the funds.
  Lakestar Advisors UK LLP (OC396445, FCA firm 778593) and Lakestar Advisors Germany GmbH (Berlin,
  HRB 156549 B) are its London and Berlin arms; the firm's own remuneration policy names both as
  included in Lakestar Advisors GmbH. Lakestar Holding AG (Zurich, CHE-354.733.105, 2022) is the
  holding company. The funds are Guernsey limited partnerships with Guernsey general partners at
  Trafalgar Court, St Peter Port: Lakestar I LP, Lakestar II LP (Form D 2015), Lakestar III LP,
  Lakestar Growth I LP, Lakestar Early IV LP (Form D 2022), Lakestar Growth II LP (Form D 2022),
  Lakestar CF I LP (Form D 2025) and Lakestar Resilience I (2026). Three general partners filed
  Form 13F (Lakestar (G.P.) Ltd, Lakestar II (G.P.) Ltd, Lakestar Growth I (G.P.) Ltd).
- **No SEC adviser registration.** IAPD returns only an unrelated Chicago adviser (NestEgg
  Advisory, formerly Lakestar Advisors LLC, CRD 161067).
- **Outcome.** Every fund family and sleeve (early, growth, the continuation fund, Resilience I)
  and all three offices are IN. No entity shares the brand under its own registration.
- **Namesakes, external:** Lakestar Semi Inc. (Conexant's name from 2013), Lakestar Advisors LLC and
  Lakestar Wealth Management (Chicago).
- **Precedent.** Creandum (four ERAs, one firm), Cherry.

### D2. The founder's personal investments (T2 and T4: OUT unless a Lakestar fund held the position)

- **Facts.** Klaus Hommels invested as a private investor from 2000 and through Hommels Holding
  from 2007 (Skype, Xing, QXL, Facebook, Spotify in 2009, Klarna, King, Airbnb and others), before
  Lakestar's first institutional fund (Lakestar I, 2013). The firm lists those positions as its
  own: the 2011 to 2013 site's portfolio pages, the 2018 to 2019 homepage logo strip ("Lakestar has
  invested in ... Facebook, Spotify and Skype") and the 2026 homepage, which now says in words that
  the platform "spans institutional venture capital funds and personal investments". The 2022 to
  2026 portfolio page, the one list the firm kept as its institutional portfolio (109 companies with
  a stage, a thesis and a deal partner each), never carried Facebook, Skype, Airbnb, Klarna, King,
  Coinbase, SumUp or Helsing.
- **Test.** T2: a founder's angel check stays out even where the firm lists it as its own, unless
  a fund of the firm held the position (Erik, 2026-09-26, binding every investor; Cherry D2, Point
  Nine, Thrive's Kushner). T4: a seat or a stake held by a person locates the person.
- **Outcome.** A row whose only route into the base is one of the brand surfaces (the 2011 to 2013
  site, the 2018 to 2019 logo strip, the 2026 homepage strip) is `not_member` unless evidence shows
  a Lakestar fund held it: an SEC filing naming a Lakestar vehicle, a round announcement naming
  Lakestar as an investor from 2013 on, or the firm's own institutional portfolio page. Where a fund
  later came into a company Hommels had backed personally (Spotify: Hommels 2009, Lakestar I on the
  2018 Form 13F), the row is a member and its entry is the fund's first check, never the angel
  check. Each such row is researched in the grind and its verdict names the evidence.
- **Why this is a derivation.** PRO-108 names it as a T2 and T4 question with the Kushner
  precedent; the facts are verified and the test is standing. It moves visible rows (Facebook,
  Skype, Airbnb), so it is also raised for Erik at close.

### D3. Lakestar SPAC I SE (T5 for the shell, T3 for the target; ruled once)

- **Facts.** Lakestar SPAC I SE, a Luxembourg blank-cheque company sponsored by Lakestar, listed
  in Frankfurt in February 2021 and completed its business combination with HomeToGo GmbH on
  21 September 2021 (the company's own announcement). Lakestar had joined HomeToGo's Series C in
  2018 as a new investor (HomeToGo's release of December 2018; the firm's own site listed HomeToGo
  from October 2018), three years before the merger. No other company came public through a
  Lakestar vehicle.
- **Test.** T5: the shell has no operating business and is not a row. T3, sponsor promotes
  (Erik, 2026-09-07, Khosla's KVSA II): a de-SPAC is not a venture entry unless a fund of the firm
  held the target through a venture round before the merger.
- **Outcome.** The SPAC is not a row and is in `config.verify.not_members`. HomeToGo is a member
  on the 2018 round (Growth); the sponsor shares and the 2021 PIPE add nothing to the row. A
  company whose only Lakestar link were the SPAC would be out; none exists.

### D4. The roster (T4)

- **Facts.** The archived team pages (2020 to 2026) list 95 people: investors, finance, legal,
  talent, events, investor relations and an advisory board. The 2014 to 2019 site had no team page.
- **Outcome.** The sweep roster is the 40 people with an investing title (partner, principal,
  associate, analyst, investment director, venture partner, the founder), plus four partners and
  principals who left before 2020, from press and an SEC filing (`scratch/build_roster.py`,
  `sources/wayback/partner-roster.json`). Advisers, finance, legal and investor relations are out.
  A roster name on a Form D is a name-match and never suffices alone (§1): each is judged per
  person, dated against the person's firm at filing time. Known operator and next-firm seats:
  Mika Salmi (CEO of CreativeLive before Lakestar; Hagerty director), Nicolas Brand (BCP after 2023),
  Dharmash Mistry (Balderton before, LGT Lightstone after).

### D5. Venture entries only (T3)

- **Facts.** The three general partners' Form 13F holdings are Spotify (Lakestar I, 2018 Q4),
  Opendoor and Oscar Health (Lakestar II, 2020 to 2022) and Oscar Health (Growth I, 2021 to 2022).
  Oscar Health's IPO registration lists Lakestar I LP, Lakestar II LP and Lakestar Growth I LP as
  holders under its investors' rights agreement.
- **Outcome.** All three entered through venture rounds and stay members after listing. A 13F line
  never seeds membership. No buyout practice exists, so the control-position rule has no class here.

### D6. The continuation fund and other plumbing (T5)

- **Facts.** Lakestar CF I LP (Form D October 2025; the firm's site: a USD 265 million
  continuation vehicle closed in September 2025) took over existing positions.
- **Outcome.** Positions moved into it stay rows through their original entries; the vehicle is
  not a row and brings no new member.

### D7. Sale consideration and acquirers

- **Outcome.** Stock received for selling a portfolio company is not membership (§1). The
  acquirers of Lakestar exits (Disney for Maker Studios, SAP for Taulia, Bosch for Five, Delivery
  Hero for Glovo, Visma for Holded and others) are not rows.

### D8. Registers per jurisdiction

- **Switzerland (below the pre-build threshold; probed in this run).** Zefix, the federal index
  of the cantonal registers, answers a name search and a per-firm record as JSON with no key:
  status, legal form, seat, purpose, former names, auditors and the full publication history
  (officers, and for a GmbH the quota holders by name). It is filing-grade for `status` and for the
  firm's own entities. It gives no shareholders of an AG, which is the form almost every Swiss
  venture-backed company takes, so it is not a membership layer. Finding: usable for status and
  entity facts; recorded in the report.
- **Germany.** Cherry's recipe: the Handelsregister through North Data for status and successor
  entities; an insolvency followed by an asset sale reads `acquired`, a filing with no sale reads
  `defunct`.
- **UK.** Companies House company status is free and structured.

### D9. Conventions

- Non-USD figures convert at the ECB rate of their own date (`scripts/fx-convert.py`). A listing
  outside SEC registration takes a web-cited market cap (HomeToGo on Frankfurt, Marley Spoon).
- No entry-date window; a round the record does not give reads `undetermined`.

## Part 2: the deltas PRO-108 names

1. **Three jurisdictions.** D8 above. The Swiss probe ran and its verdict is recorded.
2. **The SPAC.** D3 above, ruled once.
3. **The named principal.** D2 above.
4. **Founded 2012.** The fund book starts in 2013. The older rows on the firm's surfaces are the
   founder's own and are decided by D2, not by a date.

## Part 3: run-time rulings (dated, flagged for review)

- **R1 (2026-10-01). The site's stage field: `Growth` labels at medium, `Seed` only with a dated
  seed, `Early` and `Exit/IPO` never.** The 2022 to 2026 portfolio page files each company under
  Seed, Early, Growth or Exit/IPO. Eligibility: before an exit the value is the firm's own bucket
  for its investment (it switches to Exit/IPO when the firm is out: Aleph Alpha, Avrios, Eigen,
  Imburse), so it is the firm's claim about its entry, read at the row's earliest value. Scored
  blind against the 88 rows with a documented entry round (`scratch/judge_research.py`, the table
  in the run log): `Seed` agreed on 28 of 32 (the misses: Modulate and Netspeak, announced as
  Series A; Ravical and Murphy, pre-seeds), `Growth` on 20 of 24 (the misses: Neko Health,
  Colossyan and Reneo, Series A rounds the growth fund led, and Omio), `Early` split 8 Seed, 10
  Series A, 2 Growth. So `Early` straddles two stages and is an anchor; `Exit/IPO` names no round.
  `Growth` is promoted at medium as `first_party` where no round announcement names Lakestar
  (WeLend). `Seed` is not used alone: a Seed row owes a graduation decision and that needs an
  entry date, which the page does not give and a capture never supplies (§6); such rows read
  `undetermined`. A documented round always overrides the label.
- **R2 (2026-10-01). Scout and angel-programme cheques are out (T2).** Vsim names "Lakestar Scout
  Fund" and Zefi.ai names Halo, the firm's angel programme; neither has a main-fund follow-on.
  Both are recorded rejections of the recall probe, never rows.
- **R3 (2026-10-01). Seat-only rows are out.** ShareIQ (Christoph Schuh on the 2016 Form D; only
  vendor profiles list Lakestar) and Modern Meadow (Klaus Hommels on the 2021 Form D; never on a
  Lakestar surface) are `not_member` under Erik's ruling of 2026-09-28 on seat-only rows.
- **R4 (2026-10-01). The firm investing as a firm counts from 2012; the 2011 to 2013 site does
  not.** The 2011 to 2013 lakestar.com ("(c) 2011 Lakestar") listed Hommels' angel book: where a
  round of that period names an investor it names "Klaus Hommels" in person (SumUp, Nutmeg,
  Snappli, 2012). Rows whose only surface is that site are `not_member` under D2. Recall additions
  made in 2026, after the firm said its future investments are "made with own capital", are
  members where the announcement names Lakestar the firm (GeneralMind, Antidote, Pit): the firm
  acting as a firm, not a person's cheque.
- **R5 (2026-10-01). Helsing is out until a round or filing names a Lakestar fund.** No Helsing
  round names Lakestar; the trade press calls Hommels an angel investor in it; the firm never
  listed it on its 2022 to 2026 portfolio page and names it only in the 2026 Resilience material.
  Raised for Erik: on the other reading (the firm's own 2026 listing suffices) Helsing returns as
  a member with an undetermined entry round.
- **R6 (2026-10-01). An unnamed round between two named rounds takes the earlier stage.**
  Marley Spoon (Lakestar's money of March 2015, after the Series A of November 2014 and before
  the Series B) reads Series A; Omio (Lakestar's money of January 2014, after the 2013 seed and
  before the Series A of August 2014) reads Seed. Both at low confidence, flagged for review.
- **R7 (2026-10-01). A signed SPAC merger is a mark, flagged.** Terra Quantum's definitive
  business-combination agreement of 2026-05-26 states a USD 3.5B equity value; the row reads
  private at that figure until the deal closes or fails (§6, a signed but unclosed acquisition is
  a mark). Raised for Erik, because a de-SPAC price is negotiated with a shell, not set by a
  financing.
- **R8 (2026-10-01). A majority takeover reads `acquired`.** Solaris (SBI took the majority in
  the rescue round of February 2025), nebenan.de (Hubert Burda Media, 61%, September 2020) and
  Avrios (Battery Ventures, January 2023) changed control without a full sale; each reads
  `acquired` with the buyer in the note. Raised for Erik: the other reading keeps them `private`.
- **R9 (2026-10-01). Two bands follow the sibling books.** 1047 Games reads below $1B with the
  Lightspeed and Insight books, on the studio's collapse after the 2021 round at $1.5B; by the
  letter of the stale-mark rule the 2021 mark would stand, so it is raised as one ruling for
  three books. OneFootball reads below $1B with the Union Square Ventures book: the EUR 1B figure
  for its 2022 round traces to a vendor list (Rule A).
- **R10 (2026-10-01). Spotify's entry is Growth on structure, flagged `cite_pending`.** Lakestar I
  held 330,440 shares at the end of 2018 (Form 13F). Hommels' own cheque dates from 2009; the
  fund dates from 2013, when Spotify was past its Series F, so the fund's entry is a later round
  or a secondary, both Growth. No announcement names the round.
- **R11 (2026-10-01). Public caps follow the freshest sibling inside ten days.** Spotify takes the
  Kleiner Perkins book's cap of 2026-09-30 ($100.20B), so every book reads the same band at the
  $100B edge.
