# Menlo Ventures — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Menlo Ventures (slug
`menlo-ventures`, display name **Menlo Ventures**; the firm has used
"Menlo Ventures" continuously since 1976 and its two advisers both file under
that primary business name). The judge cites these rulings per line. Written
under the derivation protocol of COLLECTION.md §1: **derivations** (a standing
test applied to verified facts — vetoable by Erik, no confirmation needed),
**deltas** (Erik's to confirm) and **run-time standing rulings** (dated,
flagged for review). Phase 0 was researched and verified at kickoff
2026-09-06 against IAPD, both Form ADV PDFs, EDGAR and the archived site;
every fact below was checked in this run, not carried from the issue.

**The structural fact of this run.** Menlo Ventures was founded in **1976** and
has invested continuously for fifty years, which makes it the oldest book this
project has collected and the one with the largest **pre-window** slice: the
2006 policy constant nulls `entry_stage` and `seed_to_a_graduation` for every
row entered before it, and that is the rule rather than debt (PRO-91's delta,
and the Greylock treatment). Two consequences shape the run:

- **The firm's own archive is the pre-window evidence, and it is unusually
  good.** Menlo published a *Prior Investments* page — its own list of exited
  and dead positions — in two consecutive site eras (`/port_prior.html`
  2000–2001, `/portfolio/prior_investments/` 2002–2007). That is the
  survivorship-correction surface for the 1976–1999 book, which no filing
  layer can reach: Form D coverage begins in 2008 and the firm's earliest
  13G is 1997.
- **The live site is a superset of its own rendered listing.** The WordPress
  `portfolios` collection carries **322** companies where `/portfolio/`
  renders **245**; the 77 REST-only rows are the historical exits (UUNET,
  Infoseek, DocuSign, Redfin, Upstart, Upwork, Palo Alto Networks, Shazam,
  AppDynamics, Smartsheet, Clearwater Analytics, HNC Software). A run that
  scraped the rendered page would have dropped the firm's best-known exits.

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1 — The firm (T1, same adviser).** Menlo Ventures is **two exempt
  reporting advisers filing under one primary business name, at one address,
  with one team**, and both are IN:

  - **MV MANAGEMENT XI, LLC**, dba MENLO VENTURES — **CRD 161248**, SEC
    **802-75435**, annual amendment filed **2026-04-01**. Section 7.B carries
    **8 private funds, $967,805,151**: Menlo Ventures X, XI and XII, Menlo
    Entrepreneurs Fund X and XII, and MMEF X, XI and XII.
  - **MENLO VENTURES MANAGEMENT, L.P.**, dba MENLO VENTURES — **CRD 283999**,
    SEC **802-108043**, annual amendment filed **2026-03-31**. Section 7.B
    carries **31 private funds, $10,774,945,953**: Menlo Ventures XIV, XV,
    XVI and XVII; Menlo Inflection, II, III and IV; the Inflection deal
    vehicles (AI Partners and AI Investors I/II, ABN AI Partners, Suno
    Partners); Menlo Labs I, II and the Side Fund; Menlo Olympus Fund I;
    Menlo Bio I; the Entrepreneurs, CxO, Innovators and MM/MMEF/MMSOP
    co-invest vehicles.

  Both file from **1300 El Camino Real, Suite 150, Menlo Park, CA 94025**;
  neither is an SEC- or state-registered investment adviser, so **there is no
  Item 5.F RAUM** and the AUM anchor is the Section 7.B composite
  (COLLECTION.md §11): **39 private funds, $11,742,751,104**, both filings
  within one day of each other, so the composite is coherent as of one
  fiscal year end. Press supplies the range top.

  **IAPD was checked by CRD for a brand-sharing entity with its own
  registration and there is none** (PRO-87 requires this check rather than
  assuming it). A search of every adviser named "Menlo" returns exactly two
  Menlo Ventures records — the pair above — plus namesakes with their own
  unrelated businesses: Menlo Equities (CRD 162139) and Menlo Equities V and
  VI (real estate, Menlo Park), Menlo Advisors LLC (CRD 122721, a Menlo Park
  wealth manager filing 13Fs since 2004), Menlo Group LLC (CRD 308522),
  Menlo Investment Corporation and Menlo Securities. **No Accel-KKR /
  Meritech / Lightspeed-India pattern exists here.**

  Filing addresses across the record, all Menlo Park: 3000 Sand Hill Road
  (1997–2014) → 2884 Sand Hill Road, Suite 100 (2005–2022) → 1300 El Camino
  Real, Suite 150 (2017–present).

- **D2 — Sleeves and vehicles (T1, default IN for every fund family and
  sleeve of the one adviser).** IN: the **flagship ladder** (Menlo Ventures
  IV, VI, VII, IX, X, XI, XII, XIV, XV, XVI, XVII, plus XVII Innovators and
  XVII Private Investors); the **Inflection** family, which is the firm's
  early-stage sleeve (Menlo Inflection I–IV, Inflection IV Innovators,
  Inflection IV Private Investors, and the Entrepreneurs/CxO Inflection
  vehicles); **Menlo Special Opportunities Fund I, II and III**, the
  later-stage sleeve; **Menlo Labs I, II and Side Fund**, the crypto sleeve;
  **Menlo Bio I**, **Menlo AI Leaders Fund and II**, **Menlo Olympus/Olympic
  Fund I**, **Menlo Ventures Select I**; the single-deal Inflection SPVs
  (**AI Partners / AI Investors I and II**, **ABN AI Partners**, **Suno
  Partners I and II**, **Atlas Partners**, **Cybersecurity Partners**,
  **Menlo Ventures Axm Partners**, **Menlo LV Partners**); and the
  **co-invest and employee vehicles** (Menlo Entrepreneurs Fund IX, IX-A, X,
  XII, XIV, XVI and Inflection; Menlo CxO Fund XVI and Inflection III; Menlo
  XV Innovators; MMEF X/XI/XII/XIV/XV; MM Inflection and MM Inflection III;
  MMSOP). Precedent: a16z's crypto / bio / games / American Dynamism
  families under one adviser; Creandum's flagship, Select and SPV vehicles;
  Thrive's lettered LLCs.

  This is a venture book end to end and the **strategy-desk addendum does not
  fire**: there is no buyout, credit, infrastructure, real-assets or
  public-equities practice under either adviser. The one public-market
  artefact is D5.

- **D3 — The Anthology Fund (T2, fund money).** The **$100M Anthology Fund**,
  created with Anthropic and staffed by six Menlo partners (Tim Tully, Matt
  Murphy, Joff Redfern, Amy Wu Martin, Deedy Das, Venky Ganesan) alongside
  Anthropic's Daniela Amodei and Mike Krieger, writes pre-seed, seed and
  Series A cheques from $100,000 up as lead or participant. It is **Menlo
  money deployed by Menlo partners**, so its companies are **IN** on the
  a16z-speedrun and Accel-Atoms precedent: fund money deployed, whatever the
  program or channel. Anthropic's role is a partnership on sourcing and
  credits, not a separate adviser, and creates no boundary question. A
  cohort company where no Menlo vehicle actually deployed is OUT under T2's
  standing rule, exactly as an Atoms cohort company is.

- **D4 — Third-party feeders (T5, plumbing is not a row; and T1, whose
  vehicle).** OUT of the fund list as `external`: **Menlo Special
  Opportunities III Access LLC / Access Offshore LP** and **Menlo
  Opportunities Access LLC / Access Offshore LP**, all four filing from
  **200 West Street, New York** (Goldman Sachs), and **Menlo Ventures 2025 –
  Allocate Access, L.P.**, filing from **502 Waverley St, Palo Alto**
  (Allocate). These are third-party access vehicles feeding Menlo funds, not
  Menlo vehicles — the Thrive IX Access precedent. Their existence is a
  fund-raising fact for the profile, never membership evidence, and the
  positions they reach are already carried by the master funds.

- **D5 — The 13F is venture residue, not a crossover desk (T3, venture
  entry).** Menlo Ventures Management, L.P. (CIK 1911541) began filing
  **13F-HR** in 2026. The August-2026 table holds **three** positions:
  **Chime Financial** ($357.2M), **Senti Biosciences** ($39.3K) and **Braze**
  ($100.1K) — post-IPO residue of venture entries, not a public book. Braze
  is the §1 *sale-consideration* pattern rather than a position: Braze
  acquired Menlo's portfolio company **OfferFit** in 2025, so the shares are
  merger consideration and the investment row is OfferFit. Under T3 the 13F
  therefore seeds nothing on its own; a row whose only evidence is this
  filing is `not_member`, and the two rows it corroborates entered through
  venture rounds and stay in.

- **D6 — Namesakes (T5, is this a row at all).** The firm's name is the town
  its funds file from, which makes "Menlo" the worst possible unqualified
  search term on EDGAR: Menlo Park is the filing address of a large part of
  Sand Hill Road. Every phrase layer is entity-qualified (`config.json`
  `edgar.fts_phrases`, `wikipedia.phrases`). The registered namesakes,
  verified by address: **Menlo Equities / Menlo Realty Partners** (Palo Alto
  real estate, funds I–VI), **Menlo Advisors LLC** (659 Oak Grove Avenue,
  Menlo Park — a 13F wealth manager), **Menlo Asset-Backed Partners LLC / II**
  (490 California Avenue, Palo Alto), **Menlo Park Investors LLC** (254 W
  31st Street, New York), **Menlo Acquisition Corp** (Parsippany, NJ),
  **Menlo Townhomes LLC** (AZ), **Menlo Atherton 71 LLC** and **Menlo BCSP
  405 JV LLC** (real estate JVs), and the two AngelList series funds
  **Menlo-CS-0628** and **Menlo-GI-0307** (Washington State, AngelList's own
  syndicate namespace). **Menlo Microsystems, Inc.** (Irvine, CA) is an
  *issuer*, not a vehicle, and is not a Menlo Ventures position on any
  surface; it is classed external so no layer reads its Form Ds as the
  firm's.

- **D7 — Scouts, angels and programs (T2).** Standard: scout checks with no
  main-fund follow-on OUT, partners' personal angel books OUT, program and
  community listings OUT unless a fund held the position. Ruled on Sequoia,
  a16z, Accel and Lightspeed; nothing in Menlo's facts departs from it.

- **D8 — Person-level attribution and seat dating (T4).** Standard. Menlo's
  roster spans fifty years and its partners predate, postdate and interleave
  with other firms, so the seat-dating discipline is load-bearing: a Form D
  or Section 16 filing by a natural person locates the person, and the seat
  is dated against the person's firm **at filing time**. Named risk cases for
  the cluster pass: **Shervin Pishevar** (Menlo 2011–2013, then Sherpa
  Capital — the Uber-era seats belong to Menlo, the 2013+ ones do not),
  **Sonja Hoel Perkins** (Menlo 1994–2011, then Broadway Angels/The
  Perkins Fund), **Tim Tully** (Splunk CTO before Menlo — an operator job,
  not a firm seat), **Matt Murphy** (Kleiner Perkins before Menlo 2015),
  **Joff Redfern** (Atlassian VP Product before Menlo), **Steve Sloane**,
  **Naomi Pilosof Ionita** (Invoice2go operator years), **Matt Kraning**
  (Expanse founder, then Palo Alto Networks, then Menlo 2025) and
  **Rama Sekhar** (Norwest before Menlo 2024). Each is resolved once as a
  cluster, not row by row.

- **D9 — Venture entry (T3), control positions, and the public-purchase
  exclusion.** Standard, unchanged: primaries, follow-ons, secondaries and
  tenders IN, a tender entry Growth by taxonomy; positions first appearing as
  13F holdings or post-IPO 13Gs OUT; control acquisitions OUT with reason
  `control_position`. Menlo runs no buyout practice, so the control addendum
  is expected to be inert here — if it fires, the row is recorded under it
  rather than argued around.

- **D10 — Fund-shaped entries and tokens (T5).** Standard. The Menlo Labs
  sleeve makes the token rule live: a listed token position is IN when it
  maps to an operating or issuing organization, OUT when it is a bare
  base-layer asset holding, and where a token and its company are both
  listed they are one row under the company.

## Deltas (Erik's to confirm)

**None.** Every category above resolved as a derivation under a named
standing test against facts verified in this run. PRO-91's three delta
candidates all landed as derivations:

1. *"Founded 1976, so a large pre-window slice."* Not a ruling — the 2006
   policy constant already decides it. The run reports the pre-window share
   and does not chase it.
2. *"Sleeves under T1: the flagship plus Inflection and any labs or seed
   sleeve."* Verified by CRD: D1/D2. One adviser family, no separate
   registration, all IN.
3. *"Long site history, check for a pre-rebrand domain."* Verified: the firm
   published on **menloventures.com from 1997 to 2012** and moved to
   **menlovc.com** in 2011–2012, both configured with per-era `cdx_domain`
   overrides on the Lightspeed precedent. No archive gap was recorded before
   the old domain was checked.

## Run-time standing rulings

_(dated, class-wide, flagged for review; appended during the run)_

### R1 — The site's Milestones field is class 1 for the round and a close year for the date (2026-09-06)

Menlo's rendered portfolio cards carry a **Milestones** list stating the firm's
own entry: `2011 – Partnered, Series B` (Uber), `2018 – Partnered, Series C`
(Chime). 214 of the 245 listed rows carry one. Scored blind against the
36-row key in `golden.json`: **33 of 34 scored rows correct** (one row absent
from the rendered listing, one dropped from the key). Promoted to **class 1
for the round word**, alongside a web citation.

The misses decompose to a **date**, not a stage: five correctly-labelled rows
carry a year one earlier than the press announcement (Dropcam 2011 vs
Jun-2012, ConverzAI 2024 vs Feb-2025, Orb 2022 vs Mar-2023, Semgrep 2024 vs
Feb-2025). The field is the year the deal **closed**. So it may set
`first_seen`; it may not be read as an announcement date; and a year
disagreement with press never overrides the round word. The one genuine miss
is **Warby Parker** (site "Series B" for a 2011 partnering against a
documented September-2011 Series A) — its own year contradicts its own round
word, which is what makes it a layer defect rather than a judgement call.

### R2 — On this firm the announcement archive is class 1 for the round it names and is NOT evidence of the entry (2026-09-06)

The Creandum finding — score the firm's announcement archive as a class-1
entry-stage layer — **inverts here**. Three of the four apparent CMS misses
were the announcement layer being wrong. A Menlo post titled "Our Series A
Investment in X" announces the round Menlo **led**, which on this book is
regularly a follow-on to a quieter first cheque. Proven four times inside the
run's own sources: **eero** ("we first invested in eero's seed round two years
ago", 2014, against a 2016 post announcing the $50M round it led),
**H1** ("in April 2020, Menlo led the Series A", against a December post
announcing the co-led Series B), **Goodfire** (in the $7M seed of Aug 2024,
announced only at the $50M Series A of Apr 2025) and **Numeric** (first
cheque in the $10M seed of May 2024, announced at the $28M Series A of
Oct 2024). Class-wide rule for this investor: an announcement dates and names
a round; it asserts an ENTRY only where the post says so in words.

### R3 — Pipeline change: the entry-stage claim now reaches the judge (2026-09-06)

A class-1 layer that the queue item does not carry is a layer the grind
cannot use. `build-company-base.py` already folded the site's `invest_year`
into `first_seen` but dropped the round word; it now carries
`site_entry_stage` onto the base row, and `run.py`'s `EVIDENCE_FIELDS`
carries `site_entry_stage` and `site_invest_year` into every queue item.
Both are investor-agnostic and are proposed for write-back (§9). Applied
before any verdict was written: the base was rebuilt and re-prepared with
one seeded verdict and zero classification keys on the overlays, so the
no-rebuild-mid-run rule is not in play.

### R4 — 3Com is Chipcom (2026-09-06)

The live site lists a company called **3com** carrying Chipcom's own
description ("Chipcom was an early pioneer in the Ethernet hub industry"),
and the 1998 communications page lists **CHIPCOM CORPORATION**. Menlo's
investment was Chipcom; 3Com acquired it in 1995 and the modern CMS row is
filed under the acquirer's name. The two slugs are one row, canonical
**chipcom**, and this is the acquirer-naming pattern COLLECTION.md §1 flags
for the consideration reading — here it is a naming artifact, not a position
in 3Com.

### R5 — The director-of-record pattern produced four unannounced members (2026-09-06)

Applying COLLECTION.md §1's a16z pattern mechanically — a current partner as
Director of record on a Form D, in tenure, with an issuer that resolves to a
real operating company — admitted four rows that appear on no Menlo surface:
**Anchore** (Douglas Carlisle, 2016–2020), **Drata** (Houman Haghighi, 2021),
**Portfolium** (Haghighi, 2015–2017) and **InterModal Data** (Sandeep Bhadra,
2015). All four are recorded `member` at medium confidence as unannounced
deals and raised for Erik. **reThought Insurance** (Venky Ganesan, 2018) meets
the same structural test and was ruled OUT: the issuer is a Broomfield flood-
insurance MGA and the firm has no insurance-underwriting position in fifty
years of listings, so the pattern's "resolves to a real operating company"
clause is satisfied while the corroboration the definition asks for is not.
Recorded so the boundary between the two is visible rather than implied.

### R6 — Menlo's fifty-year book collides with every sibling base on common words (2026-09-06)

Ten cross-investor pairs are `distinct` rather than disagreements, and the
pattern is structural rather than incidental: the firm's 1980s and 1990s rows
carry names the 2010s and 2020s reused. **Amplitude** (a 1998 resource-
scheduling company Critical Path bought, against Amplitude Inc), **Alloy**
(alloy.ai against alloy.com), **Axiom** (the AI mathematician against the legal-
services company), **Canvas** (three companies), **Check** (a 2014 bill-payment
app against a 2019 payroll API), **Clarify** (a 1990s CRM against Clarify
Health) and **Glide** (a video app against a no-code builder). An investor
whose book spans decades should expect invariant 10 to surface these as
disagreements and should rule them `distinct` rather than align them.

### R7 — Two automatic name-variant merges joined companies decades apart (2026-09-06)

`build-company-base.py`'s name-variant merge joined **Alta** (founded 2023,
seeded 2024) to **Alta Analytics** (a 1999–2000 listing) and **Eve** (founded
2020, seeded 2022) to **eve.com** (the 1999 beauty e-tailer), pulling a 2000
wayback year and a wrong status onto each modern row. Both are pinned apart in
`identity-merges.json` under `never_merge`. On a fifty-year book the automatic
merge is a liability as much as a convenience, and the flagged pairs were found
only because the modern rows carried an impossible first-seen year.

### R8 — One site generation, two listing markups: the 2002–2003 sector pages (2026-09-06, post-close)

The 2002–2003 XHTML site renders companies **two different ways on the same
generation**. `all_alpha` and `prior_investments` use a bare `<li>Name</li>`
list; the four sector pages (`communications`, `healthcare`, `internet`,
`services_and_software`) use a `<div class="company">` card whose
`<p class="summary">` holds the name and the firm's own one-line description.
The era pattern was written from the alphabetical pages and applied to all six,
so the eight sector-page captures parsed to **zero rows and read as empty years**
— a silent recall hole, not a fetch failure: every page was fetched, is on disk
at 10–20 KB, and carries the right title.

Corrected by giving the four sector eras their own pattern. It recovered
**Bravanta, Covalent Technologies and Lantern Communications** — three companies
listed only in 2002–2003, absent from every later Menlo surface including Prior
Investments, and therefore invisible to every other layer. It also supplied
fuller names for 15 rows already in the base (`Big Bear` → `Big Bear Networks`,
`vBrick` → `VBrick Systems`, `GoDIGITAL TELECOMMUNICATIONS` → `GoDigital Networks
Corporation`), which re-slugged them; the ledger, classification and inner slug
fields were re-keyed rather than re-judged, since the evidence and verdicts are
unchanged.

Two second-order gains. The firm's own descriptions **retired the
`identity_uncertain` flag on three rows** (Big Bear Networks, Parama Networks,
Phiar Corporation) — including a disputed GB namesake pre-fill on Big Bear that
the description ("opto-electronic modules for high-speed optical networks")
settles as a Sunnyvale optical-components startup. And they proved Menlo's
**Phiar Corporation** ("high-speed photonic switching applications", 2002) is not
YC's **Phiar** (S18, AR navigation); the suffix-stripped cross-investor key joins
them, so the pair is now ruled `distinct` in `cross-investor.json`.

The general lesson, written to §5: **a zero-row year on a page that fetched
successfully is a parser hypothesis that failed, not an absence.** The era
pattern is a claim about markup, and it must be checked against a page that
returned bytes before an empty year is believed.

### R-S2A — Seed-to-A graduation re-judged under the status contract; the pre-window rows labelled; fourteen partner-carried listings surfaced (2026-09-16, agent, class-wide)

**S2A.** Under the 2026-09-16 contract (COLLECTION.md §6) every in-window
Seed row was re-judged with both legs cited: 45 seed entries, 7 censored,
8 undetermined, cohort 30, graduated 21, rate 70.0%, coverage 79%. Six rows
left the cohort because the citation places Menlo's entry later (Glympse,
Mog, Vidyo, SpeedDate and Jobfox at Growth; ClearBrain at the Series A its
own Milestones name). Decent ($8M seed, $10M Series A) and Mimic ($27M seed,
$50M Series A) are named Series As that fail the 2× step-up on known amounts
and stay `undetermined` under the rule Erik kept; a ruling that a named
Series A always counts would move both to graduated. The 0.80 ceiling is
not approached.

**Pre-window rows.** The 243 rows an earlier pass had nulled as pre-window
now carry a label under the 2026-09-07 constant. 211 are genuinely
pre-window (the firm's archive lists them before 2006): `pre_window_entry`,
Series A by the pre-2003 convention at low confidence, except five judged
or cited Growth (Ingrian Networks, PassMark Security, IMVU, USinternetworking,
CinemaNow); graduation null by rule. 32 were never pre-window: historical
listings with no dated milestone. Their `pre_window` flag is cleared and the
label is in-window (6 cited, 26 `stage_uncited` and archive-bracketed).

**Partner-carried listings (ruling needed, T1/T4).** Fourteen of those 32
are deals Menlo's own team pages attribute to a partner's previous firm,
with no Menlo fund named in any round: AppDynamics, Puppet, DocuSign,
Egnyte, DataStax, Drawbridge, SessionM, Upstart, AutoNavi (Matt Murphy,
KPCB); Smartsheet, Clearwater Analytics, Ascentis (JP Sanday, Summit);
Upwork, Exeros (Venky Ganesan, Globespan). T4 asks whose money sat behind
the seat; on the record it was not Menlo's. They stay members until Erik
rules, labelled by the carried round at low confidence with
`PARTNER-CARRIED` in the note; DocuSign, Upstart and Upwork carry
`cite_pending` as $1B+ rows without a cited stage, as does Calix.
