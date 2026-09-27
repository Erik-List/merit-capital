# Headline: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Headline (slug
`headline`, display name always **Headline**; **e.ventures** 2012–2021, **BV
Capital** 2000–2012, **Bertelsmann Ventures** 1997–2000). The judge cites these
rulings per line. Written at kickoff 2026-09-27 (PRO-164) under the derivation
protocol of COLLECTION.md §1: **derivations** (a standing test applied to
verified facts; no confirmation needed, vetoable), **deltas** (Erik's), and
**run-time standing rulings** (dated, class-wide, flagged for review). PRO-164
named five deltas; each is derived or raised below and listed again in
`report.md`.

**The structural fact of this run:** one firm under four successive names, with
its US, Europe and growth funds under six SEC exempt reporting advisers that
share owners and officers, and two regional desks (Asia, Brazil) that joined
the brand in 2021 with their own fund families. The firm's own site is a public
Sanity dataset (293 company docs, each with the fund pages that list it and the
firm's own dated entries per fund, 83 team docs with per-investor portfolio
lists). US rows arrive with Form D and EDGAR evidence; European rows with the
site, the archive, registers and press (D11).

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm (T1, same adviser).** Headline = the firm advised by six SEC
  exempt reporting advisers, all annual amendments of 2026-03-31 unless noted
  (IAPD PDFs in `data/filings/headline/adv/`, Section 7.B parsed to
  `sources/registers/adv-7b-funds.json`):
  **e.ventures Management, LLC** (CRD 304362, SEC 802-116979, CIK 1611940; 101
  Montgomery Street, Ste 200, The Presidio of San Francisco), **e.ventures
  Management VI, LLC** (CRD 309084), **Headline Management VII, LLC** (CRD
  323221), **Headline Growth Management, LLC** (CRD 323219), all four at the
  Presidio office; **Headline Management GmbH** (CRD 319198, Friedrichstraße 206,
  Berlin; Hamburg office) and **Headline Management Lux S.à r.l.** (CRD 344374,
  19 Rue Aldringen, Luxembourg; SEC ERA report 2026-09-04). One firm, not a
  family of firms: **Christian Leybold** (Berlin) is a Schedule A owner of the
  two US advisers 304362 and 309084; Headline Europe VII's owner of record is
  **Headline EU VII Holding, LLC**, a US company; the US CFO **Patrick Reilly**
  is a manager of the Lux general partner. The predecessor adviser **BV Capital
  Management, LLC** (CRD 160568, inactive, last ADV 2017-07-25, 600 Montgomery
  Street) advised BV Capital Fund II, II-A and BV Capital GmbH & Co.
  Beteiligungs KG No. 1. Verified vehicles (7.B and EDGAR, `entities.json`):
  BV Capital Fund II / II-A (CIK 1533898/1533899; Angie's List Form 3 2011) and
  the KG No. 1 (1533897); **BV Capital Fund IV (Asia), L.P.** (CIK 1510113, Form
  D 2011-01-12: Delaware, general partner BV Capital GP IV, LLC, Mathias
  Schilling managing director, San Francisco); BV eVenture Fund II L.P.;
  eVentures Growth, L.P. (1611943, 2014); e.ventures US V / V-A (1629997 /
  1660790), US VI (1780856), Growth II (1695813), Growth III (1809367); the
  co-invest LLCs III, IV, V and EVGC Growth I / II Co-Invest (1810732 / 1810727,
  co-managed with Greycroft LP, which the 2020 Form D names "a Manager of the
  Issuer"); Headline US VI and VII (1931045), Headline Growth III / III AIV /
  III Escalar GmbH & Co. KG, Headline Global Growth IV L.P. (1931106) and Lux IV
  SCSP (2002335), Headline Europe VII GmbH & Co. KG, Headline EU VIII SCSP, and
  the single-deal SPVs Headline Homa SPV GmbH & Co. KG, Headline Lion SPV (2040786)
  and Headline Wombat SPV (2036016). The lineage is one team under successive
  names: Bertelsmann Ventures (1997, Santa Barbara, the Bertelsmann-backed
  internet fund) became BV Capital in 2000 with outside LPs, Schilling and
  Gieselmann among its founders ("Thomas co-founded Headline in 1997", the
  firm's own bio); BV Capital became e.ventures in 2012 "adopting the same name
  for all its international branches" (TechCrunch 2012-07-15); e.ventures became
  Headline in May 2021. → **IN** for every vehicle above: early funds, growth
  funds, co-invest sleeves and SPVs alike. Precedent: Thrive's sleeves;
  Balderton D2 (a rename of one manager is one firm across the rename).

- **D2: The Asia desk (T1) → `other_desk`, partitioned; a row stays where a
  home vehicle held it.** Infinity Venture Partners / Infinity Ventures (Tokyo,
  Taipei, Beijing; founding partner Akio Tanaka, with Joseph Huang in Taipei)
  "helped one another on a deal-by-deal basis" with e.ventures for ten years and
  in May 2021 its offices "will be known as Headline Asia" (Headline's own
  release, Media OutReach 2021-05-10); "Headline Asia (formerly known as
  Infinity Ventures) ... close their fourth fund at over $100 Million"
  (2021-08-03). Its funds are its own family under its own managers: none is on
  any Headline adviser's 7.B roster, none is a related person in any Headline
  ADV Section 7.A, and no Headline Asia manager is registered with the SEC (IAPD
  search 2026-09-27; the only Infinity-named ERAs are Infinity Ventures Crypto,
  CRD 321781, Taipei, its own crypto fund, and an unrelated Infinity Investment
  Management Holdings). **Test T1:** a brand-sharing entity with its own fund
  family and no adviser link is OUT. **T2 on the row:** the firm had its own
  Asia vehicle, BV Capital Fund IV (Asia), L.P. (D1), and its US, EU and growth
  funds co-invested; a row the CMS lists under the Asia fund page is a member
  where a home vehicle held it (a home fund reference on the CMS doc, a home
  vehicle on a filing, or a dated e.ventures / BV Capital listing of that era),
  and `other_desk` otherwise. Precedent: Sequoia's HongShan and Peak XV, own
  fund families under the shared brand, OUT; Lightspeed China. **Counter-fact,
  raised for Erik (report X1):** the firm itself calls the 2021 result "a
  single firm, Headline, to invest together globally" (2021-08-03). The issue's
  test is "own adviser plus own statement of independence is out; a relying or
  affiliated adviser of the same firm is in"; Asia has its own adviser, no
  statement of independence, and no registered affiliation, so neither limb
  fits cleanly. Applied as derived; the rows are preserved in `excluded.json`
  as `other_desk` so a reversal is a config change plus a delta grind.

- **D3: The Brazil desk (T1) → `other_desk`, partitioned; a row stays where a
  home vehicle held it.** Redpoint e.ventures was formed in 2012 as a joint
  venture with Redpoint Ventures ("Redpoint e.ventures Closes On $130M For
  Brazil-Focused VC Fund", TechCrunch 2012-07-23); its partners (Anderson
  Thees, Manoel Lemos, Romero Rodrigues from 2016) did not raise a third fund
  together, and Rodrigues formed a new Brazilian management firm under the
  Headline name with XP Inc. as partner (NeoFeed; projetodraft). The firm's own
  blog: "We launched our first fund in Brazil in 2012 in partnership with our
  friends at Redpoint under our previous name as 'Redpoint eventures' (RPev).
  Headline Brazil is currently deploying from its third Early Stage fund,
  Headline Brazil III, now under the Headline global brand and umbrella." No RPev
  or Headline Brazil vehicle is on any Headline adviser's 7.B roster or Section
  7.A, and the Redpoint run ruled the JV vehicle external to Redpoint from the
  other side (PRO-90 decisions.md D4: "the JV as a vehicle is external"; a
  listed row judged on whether a home fund held it). **Test T1:** own fund
  family, own managers, a JV with a third firm → OUT. **T2 on the row:** as D2.
  Counter-fact raised with D2 (report X1): "our first fund in Brazil ... under
  our previous name". Consequence named rather than hidden: RPev's companies
  (Rappi, Creditas, Gympass/Wellhub, Olist, Pismo, Viajanet) belong to neither
  Headline's nor Redpoint's base unless a home fund of either held them.

- **D4: Partner-carried deals (T4; Erik 2026-09-17, and its reverse).** A
  company listed on an investor's team page is the firm's own listing unless
  the firm disclaims it; a company the partner backed at a previous firm, with
  no Headline, e.ventures or BV Capital vehicle behind it, is `not_member` with
  the team page and the prior firm cited (Menlo precedent). The team pages list
  38 companies that the portfolio grid does not (`surface: team_page`), among
  them Schilling's eGroups, Maker Studios, Shopping.com, BlueKai, GoToMeeting,
  HiMedia and Yume Networks (the BV Capital era, judged on fund evidence), and
  Rodrigues's Rappi, Viajanet and ABC da Construção (Redpoint eventures, D3).
  **The reverse** (PRO-164): deals an e.ventures partner later carried to
  another firm stay here when an e.ventures fund held them (Jonathan Turner,
  e.ventures Growth III managing director 2020, at Accel from 2022: Accel's
  roster already reads his e.ventures-era Cameo and Zumper seats as e.ventures').

- **D5: Mandates and programmes (T2, fund money).** **Porsche Ventures II
  SCSP** is on Headline Management Lux's 7.B roster ($118,074,793): a vehicle of
  Porsche's own corporate venture programme for which the Lux entity is the
  registered adviser. Its positions are Porsche's, not a Headline fund's;
  **OUT** under T2 (precedent: third-party feeders external, Thrive IX Access;
  a service mandate is the same shape from the other side). No row enters the
  base through it: the site lists none. Advisors and specialists on the team
  (six Advisory Board members, 31 specialists) carry personal books: OUT unless
  a Headline vehicle held the company. No scout programme was found (re-checked
  in the recall probe).

- **D6: Instruments (T3).** Standing rules verbatim: primaries and follow-ons
  IN; secondaries and tenders IN as Growth entries; post-IPO or public-market
  purchases with no venture entry OUT; control positions and sponsor promotes
  OUT (none expected: the growth funds write minority cheques). A company that
  first appears under the Global Growth fund after an early fund already held
  it enters at the early fund's round.

- **D7: Plumbing and consideration (T5; §1, Erik 2026-09-22).** Parallel
  vehicles (US V-A, Growth III AIV, the Lux feeders), co-invest LLCs and the
  single-deal SPVs invest beside a flagship: no separate entries. **Homa SPV**
  holds Homa Games; Lion and Wombat are code names read in the grind. A holding
  received as consideration for a portfolio company's shares is `not_member`
  and the acquired company is the member: Groupon (the firm's CityDeal, sold to
  Groupon in 2010 for Groupon stock) and Ozon.ru (Sapato, sold to Ozon) are
  checked for this reading before they seed member.

- **D8: Namesakes (T1, T5).** Verified by entity and address, never by name:
  "Headline" is a common word (Headline Media, Headline Entertainment, many
  small issuers), "eVentures" a common company name (eVentures Group Inc., a
  1999 Dallas internet holding company), "BV Capital" a Dutch legal form
  suffix. The EDGAR phrases are entity-qualified (`config.json`
  `edgar.fts_phrases`); `desks.classify[0]` sends the namesakes to `external`.

- **D9: FX and non-US public rows (policy constants).** Every EUR / GBP / SEK
  / JPY / BRL figure converts at the ECB reference rate of its own date via
  `scripts/fx-convert.py`, the native figure in the note; a listing outside SEC
  registration (Tokyo, Hong Kong, Frankfurt, Euronext) takes a web-cited market
  cap; a US-listed row keeps the SEC float layer.

- **D10: The site's own stage list (§5 eligibility).** Each company doc
  carries the firm's dated entries per fund (`stages`: "Early 2019; Growth
  2021"). The earliest entry is the firm's claim about its own first round, so
  the field is eligible in kind; `Early` straddles Seed and Series A and is an
  anchor like a bare year; `Growth` names the growth fund's entry and collapses
  onto Growth; `Seed` labels. It labels only after it is scored blind against
  the book's documented rounds; the score is recorded in `config.json`
  `site_api._entry_stage_score` and restated in `report.md`.

- **D11: Two evidence models in one base (PRO-164; the reporting format this
  run proposes, since Index, PRO-82, has not run).** Each row carries its
  evidence regime, `sec_visible` (the company files with the SEC: a Form D, an
  EDGAR issuer record or an exit-side filing) or `non_sec` (site, archive,
  register and press only). `report.md` states coverage per regime, never
  blended: rows, membership evidence class, stage source and the `undetermined`
  share, the S2A cohort and rate, the $1B+ share and the status mix.

## Deltas

PRO-164's deltas are derived above (D1 rename lineage, D2/D3 regional desks,
D4 partner-carried deals, D11 two evidence models; Germany's backtrace is a
layer, used on German GmbH rows where status or membership needs it). The one
point no test settles cleanly, the regional desks against the firm's own "single
firm" statement, is applied as derived and raised as **X1** at the close.

## Run-time standing rulings

(dated as they are made)

- **R1: eVenture Capital Partners is the firm's European branch before 2012**
  (2026-09-27, agent, flagged for review). kaufDA (2009), Vicampo (2011) and
  Friendsurance (2011) were financed through eVenture Capital Partners, the
  Berlin firm Christian Leybold and Andreas Haug ran from 2006 with the Otto
  Group behind it (TechCrunch 2009 on kaufDA; deutsche-startups 2012 on
  Friendsurance), which took the e.ventures name in 2012 when BV Capital
  adopted "the same name for all its international branches" (TechCrunch
  2012-07-15). The firm's own CMS lists all three as its companies, and a site
  listing suffices unless the firm disclaims it (COLLECTION.md s1). Applied as
  D1 (one firm under successive names; Balderton D2 precedent), with the
  counter-fact named: before 2012 eVCP was a separately branded manager with
  its own backer, so a reader could call its book a merged predecessor rather
  than a branch. A reversal moves those rows to `other_desk` with a
  `lineage: evcp` desk entry.

- **R5: the Moscow and Kiev deals came from the European fund → IN** (2026-09-27,
  agent, flagged for review). BV Capital's own about page (February 2012, Common
  Crawl capture): "With eVenture Fonds I we cover investments throughout the
  whole of Europe, including the emerging markets Russia and the Ukraine"; the
  Moscow and Kiev analysts are listed as eVenture Capital Partners staff, and the
  Sapato (2010) and Mapia (2009) deals name that Hamburg manager, as tech.eu does
  CarPrice's 2014 seed. No Russia-only vehicle, manager or filing was found.
  Test T1 (same fund) → members, as R1. Counter-facts named: TechCrunch
  (2012-07-15) says the firm had run "five different funds", the Eastern Europe
  one to be called "e.ventures Russia", and the firm's 2013 boilerplate lists
  "e.ventures Russland" among "dedicated funds"; if a separate Russia vehicle
  existed after 2012, the post-2012 Moscow rows (Onlinetours, Teamo, AdMoment)
  move to `other_desk` with a `lineage: russia` desk entry. The Asia desk is
  confirmed as its own family by its own release ("Infnity e.ventures Asia III,
  L.P.", PR TIMES 2014) and BV Capital's 2012 page ("via our affiliated Asian
  fund: Infinity Venture Partners"), so D2 stands.

- **R6: the e.ventures logo wall is the firm's own listing** (2026-09-27, agent,
  flagged for review). The Internet Archive was blocked for the rest of the run
  after one enumeration (eventures.vc, 1,758 URLs), so the 2012-2021 portfolio
  eras were read through the firm's own upload filenames (COLLECTION.md s5,
  First Round precedent), `sources/wayback/eventures-uploads.json`, each logo
  cited by its capture. A logo becomes a row only when the company is
  identified (research agents, `scratch/research/recall-*.json`); it is a member
  on a home desk (US, Europe including the Moscow and Kiev deals, Growth) and
  `other_desk` on the Asia and Brazil desks (D2, D3, R5). Not rows: acquirers' logos shown beside exits
  (Ozon, DeNA), platforms (Mobage, the Asia desk's Beijing co-working space),
  investment firms and incubators (betaworks, Fast Lane Ventures, TheFamily:
  T5), and filenames no source ties to a company (kept in the source file,
  reported as debt; two had their own portfolio pages, which resolve once the
  archive answers).

- **R2: Raisin is sale consideration; Deposit Solutions is the member**
  (2026-09-27, agent, flagged for review). Every round the firm was in went
  into Deposit Solutions (Hamburg, founded 2011: the EUR 15M round of July 2016,
  the $100M round of August 2018), which merged into Raisin in June 2021 by
  share swap (Finextra); Raisin's own rounds carry no e.ventures money. The CMS
  lists the merged "Raisin" (Early 2012; Growth 2016), with Deposit Solutions'
  founder among its founders. Erik's sale-consideration ruling (2026-09-22) and
  its share-swap extension (Point Nine, 2026-09-26) decide it: `raisin` is
  `not_member` and `deposit-solutions` a recall addition, acquired by Raisin in
  2021. The published track record loses Raisin's $1.6B mark.

- **R3: hidden CMS docs are judged on corroboration** (2026-09-27, agent).
  The site dataset carries 44 hidden company docs; the seed step counted the
  five in the base as site listings. Each was re-judged on a round naming the
  firm: Thrive Market, Flutterwave, Friendsurance and Roadrunner are members
  on press or company releases; Wawa (title only, several unrelated companies
  of that name) is `not_member` until a round is announced.

- **R4: the CMS "Growth" label sets a stage; "Early" does not** (2026-09-27,
  agent; D10 applied). Scored against the entries documented independently in
  the first pass (firm posts, press, filings): "Growth" 3 of 3 agree (Grüns,
  Owner, Fonoa), "Early" split Seed 3 / Series A 12 / Growth 1 of 16. So a row
  whose first home entry is "Growth YEAR" reads Growth, `first_party`, the CMS
  doc as citation (20 rows); "Early" stays an anchor and every such row was
  researched (five agents, `scratch/research/stage-*.json`).

