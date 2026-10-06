# Bessemer Venture Partners: investor-specific decisions

Applies the membership rules of `../../../COLLECTION.md` to Bessemer Venture
Partners (slug `bessemer-venture-partners`, "BVP"). The judge cites these
rulings per line. Written at kickoff 2026-10-01 (PRO-80) under the derivation
protocol of COLLECTION.md §1: **derivations** (a standing test applied to
verified facts; no confirmation needed, vetoable), **deltas** (Erik's; a
provisional reading is applied and raised at close), and **run-time standing
rulings** (dated, class-wide, flagged for review).

**The structural facts of this run.** Bessemer traces itself to 1911, when
Henry Phipps set up the family office Bessemer Securities; by the firm's own
timeline the venture group inside that office opened in Silicon Valley in 1976
and "formally spins out into an independent venture firm: Bessemer Venture
Partners" in 1981 (bvp.com About page, read 2026-10-01). Today it is one
registered adviser with numbered funds VI to XII, two Century (growth) funds,
two India funds, a handful of single-deal co-invest vehicles and a buyout
strategy, BVP Forge. Its own site is Next.js over a Sanity dataset whose query
API answers without a token: 534 companies, each with a partnered year, the
Bessemer people on the deal, regions, sectors and a status. The archive
(bvp.com, one domain since the 1990s) adds the companies the live list has
dropped.

**The issue's window premise is retired.** PRO-80 was written on 2026-09-04,
when the 2006 entry window was a policy constant, and asks the run to "rule the
era boundary explicitly: the year before which the base makes no membership
claim". COLLECTION.md §1 removed the window on 2026-09-19 (PRO-137): there is
no entry-date window, a 1985 entry is judged on the same evidence as a 2025
one, and where the record does not give the round the stage reads
`undetermined`. So no boundary year is ruled. What the run reports instead is
D8 below: how far back each evidence layer reaches, and therefore from which
year the base can claim to be a list rather than a sample.

## Derivations (T1 to T5 applied to verified facts; vetoable, no confirmation needed)

- **D1: The firm and its vehicles (T1).** Facts, verified 2026-10-01 from IAPD
  and the Form ADV filed 2026-05-13 (`data/filings/adv/159279.pdf`, parsed to
  `sources/adv/adv-7b-funds.json`):
  - **One adviser.** Bessemer Venture Partners (legal name Deer Management Co.
    LLC), **CRD 159279**, SEC 801-125875, a registered investment adviser,
    principal office 1865 Palmer Avenue, Larchmont NY; other offices Redwood
    City, San Francisco, New York, Wellesley and Cambridge MA. No umbrella
    registration and no relying advisers. Item 5.F regulatory assets
    $20,239,213,324.
  - Its Schedule D 7.B.(1) reports 54 private funds ($20.26B gross): Bessemer
    Venture Partners VI to XII with their Institutional, Associates and
    offshore class vehicles; **Century Fund** and **Century Fund II** (the
    growth funds, from 2019); **Bessemer Venture Partners India** and **India
    II**; BVP VII Special Opportunity Fund; Co-Investment L.P.; the single-deal
    vehicles Cloud All Star Fund, AN I and SG I; and **BVP Forge** (three
    vehicles) with its single-deal vehicles Gator Co-Invest BE / LI / PA /
    TE / VE (corrected 2026-10-06, see R5: the kickoff reading listed the
    Gator vehicles with the venture funds).
  - Related persons on the same ADV: the general partners Deer VI to Deer XII
    & Co., Deer India & Co. and Deer India II & Co., Deer Forge & Co., and the
    local advisory subsidiaries BVP India Investors Private Limited, BVP Israel
    Investors Limited, BVP UK & Europe Investors Limited and BVP Hong Kong
    Limited.

  **Outcome: IN** for every numbered fund and its parallel vehicles, the
  Century funds, the India funds, the Special Opportunity fund, the co-invest
  vehicles, and every office (United States, India, Israel, Europe): one
  adviser, one fund family, the local entities are its own subsidiaries (the
  Lightspeed US / Europe / Israel precedent, not the Lightspeed India one).
  Earlier vehicles (Bessemer Venture Partners I to V, Bessec Ventures, the
  Deer II to V general partners) are read off EDGAR's filer list
  (`entities.json`) and are home desk where a Deer general partner manages
  them. **BVP Forge: D2. Namesakes: D3.**

- **D2: BVP Forge (T1 strategy desks, T3 control positions).** Facts: the
  firm's own timeline says "BVP Forge launches as a private equity firm" (2022)
  and bvpforge.com states the transaction type as "majority or significant
  minority, typically for shareholder liquidity", $50M to $500M enterprise
  value, from a $1 billion fund; the three Forge vehicles sit on the same
  adviser's 7.B.(1). Test: one adviser covering several strategies is
  partitioned by strategy; a non-venture strategy of the same adviser is
  `other_desk`, resolved per vehicle. **Outcome:** a position held by a BVP
  Forge vehicle is **out of the published base as `other_desk`** (desk
  `forge`, preserved in `excluded.json`). The Forge companies are not on the
  bvp.com portfolio list, which is the firm drawing the same line. A company
  the venture funds backed first and Forge bought later stays a member on its
  venture entry. The firm profile says the track record covers the venture and
  growth funds, not Forge.

- **D3: The Bessemer namesakes (T1; the collision the issue named).** Facts,
  from IAPD 2026-10-01: **Bessemer Trust** and its adviser Bessemer Investment
  Management LLC (CRD 112215, New York), Bessemer Investor Services, Bessemer
  Group and the Old Westbury funds are the Phipps family's wealth manager, a
  separate business with its own registrations. **Lindsay Goldberg &
  Bessemer** (Goldberg Lindsay & Co. LLC, CRD 141029) is a buyout firm backed
  by Bessemer Securities. **Bessemer Securities** itself is the family office
  the venture firm spun out of in 1981 and remained an investor in its funds.
  **Outcome:** all of them are `external` and are the first classify rule in
  `config.json` `desks.classify`, ahead of the home-desk pattern, so no sweep
  can attribute a Bessemer Trust 13F holding or a Lindsay Goldberg buyout to
  the venture firm. A position held only by Bessemer Securities or Bessemer
  Trust, with no Bessemer Venture Partners fund and no listing by the firm, is
  OUT. X1 below covers the one place this is not clean: the years before 1981.

- **D4: Fund money (T2).** A position is the firm's when a fund of the firm
  held it. **Outcome:** partners' personal angel checks, an operating
  advisor's or executive-in-residence's own board seat, companies founded by
  the firm's alumni that no fund backed, and LP positions in other managers'
  funds are OUT (Sequoia, a16z, Accel, Lightspeed, Cherry, Point Nine
  precedents). The site publishes 70 operating advisors and their employers:
  an advisor's company is not a position. A company incubated inside the firm
  by an executive-in-residence is IN where a fund held the position (the
  Thrive incubation precedent). A company on the firm's own list is IN on the
  listing (§1) unless the firm's own page or the record shows the money was
  not the firm's (the Menlo partner-carried rule): a site row whose partnered
  year predates the named partner's arrival at Bessemer is checked per row.

- **D5: Venture entry (T3).** Primaries, follow-ons, secondaries and tenders
  in a private company are IN, secondaries and tenders as Growth; the Century
  funds are the firm's own growth sleeve (IN, entries at Growth unless the
  venture funds were in earlier). Positions first appearing as public-market
  purchases, 13F holdings or post-IPO 13Gs are OUT. A control transaction is
  OUT under the control addendum whichever vehicle made it (D2 decides the
  Forge vehicles as a class; a control deal out of a numbered fund is decided
  per row with its citation). A blank-check sponsor promote is OUT unless a
  fund held the target through a venture round before the merger.

- **D6: Person or firm (T4).** Standard person-level attribution and seat
  dating. The firm's people travel: the site itself marks 66 alumni, and the
  investing alumni include Ethan Kurzweil and Kristina Shen (Chemistry, from
  2024; Shen was at a16z from 2019), Sarah Tavel (Pinterest, then Greylock and
  Benchmark), Sunil Nagaraj (Ubiquity Ventures, from 2017), Trevor Oelschig,
  Tess Hatch, Mary D'Onofrio, Morgan Cheatham, Hansae Catlett, Rob Soni
  (Matrix, from 2007) and others; partners who arrived from elsewhere include
  Elliott Robinson (2019), Sameer Dholakia (an operator until 2020), Lauri
  Moore and the newer India partners. A seat is dated against the person's
  firm on the filing date; tenure windows come from the archived team pages.
  Common names on the roster (Vishal Gupta, Jeff Epstein, Rob Chandra, Adam
  Fisher, David Cowan, Steve Kraus, Bob Goodman, Chris Wu, Jason Chan) are
  judged cluster-first (§3): a Form D naming one of them is the firm's only
  where the issuer is on the firm's own attribution map (the CMS `investors`
  references) or the record ties the round to Bessemer.

- **D7: Operating company (T5).** Fund-shaped entries on the firm's own list
  (another manager's fund, an accelerator) are `not_member` until identified
  as operating companies; the standing token and plumbing rules apply
  unchanged. The single-deal co-invest vehicles (Cloud All Star Fund, AN I,
  SG I, PR, VS) are plumbing, never rows: the company each one holds is the
  row. The Gator Co-Invest vehicles are BVP Forge's (R5) and fall under D2.

- **D8: How far back the base reaches (the question the issue asked; the
  no-window constant applied).** The base makes a membership claim wherever
  the evidence does, with no cut-off year. What differs by era is what kind of
  claim it is, and the report states it in these terms:
  - **From the first archived listing on** (bvp.com portfolio pages; the first
    capture year is recorded in the report once the archive is read), the base
    is the firm's own list, year by year, and a company the list dropped is
    still a row.
  - **Before the first archived listing**, a row exists only where a later
    surface still carries it: the firm's own historical list (older site
    generations listed exits back to the 1970s and 1980s), an SEC filing by a
    fund vehicle (EDGAR full text from 2001, ownership filings from the
    mid-1990s), or a cited source found by the recall probe. The base is then
    a sample weighted towards companies that went public or were otherwise
    worth listing, and the report says so rather than reading it as coverage.
  - **Entry stage and graduation** follow the standing rules with no date
    exception: a round the record names is used; otherwise the stage reads
    `undetermined` (a nameable company keeps its band and status). No debt
    flag is date-based: `stage_uncited`, `cite_pending` and `undetermined`
    say what is missing, never how old the row is.

- **D9: The site's stage field (§5, PRO-135 eligibility).** The CMS field
  `stagePartnered` reads `seed` on 500 of 534 companies, among them LinkedIn
  (Bessemer entered at the 2007 Series C), HashiCorp, Box and DocuSign. It is
  a default carried through the site's 2026 migration, not the firm's claim
  about the round it entered. **Refused**: it is not in
  `site_api.entry_stage_fields`, it never labels, and it rides in the evidence
  pack as `stage_site`, an unscored extra. Its score against the run's cited
  entry rounds is recorded in `scratch/stage-score.json` for the record. The
  CMS `partneredYear` is a year anchor (it may set `first_seen` and date a
  Seed entry where the round itself is cited), never a round. The CMS `status`
  field is stale for known rows (Skype reads active; HashiCorp reads public)
  and is evidence, not a status.

- **D10: The anti-portfolio (invariant 11; the harness the issue named).**
  The firm publishes the companies it says it passed on (bvp.com About page,
  section "The Anti-Portfolio": Apple, Atlassian, eBay, Facebook, FedEx,
  Google and Tesla on 2026-10-01; earlier versions of the page carried more,
  read from the archive into `sources/site/anti-portfolio.json`). Each is a
  company the firm states it did not invest in, so each is written to
  `config.verify.not_members` before any verdict, and the report counts how
  many of them each recall layer (EDGAR full text, Wikipedia, the roster Form D
  sweep, press) surfaced as a candidate. An anti-portfolio company that a
  layer surfaces is a false candidate by the firm's own statement; one that
  turns out to be a real later position (the firm passing on one round and
  joining another) is decided on its citation and leaves the trap list with a
  note.

## Deltas (Erik's; a provisional reading is applied and raised at close)

- **X1: Positions from before the 1981 spin-out.** Facts: until 1981 the
  venture group was part of Bessemer Securities, the Phipps family office
  (D3), and its investments were the family office's own money, with no fund
  and no outside investors. The firm presents that history as its own (its
  timeline starts in 1911, and its IPO count of "155+" reaches back through
  those years). Two tests meet: the membership definition asks for "fund
  money" from "a fund of the firm" (T2), which a family office's balance sheet
  is not; the site-listing rule (§1) says a listing on the firm's own site
  suffices unless the firm disclaims the position, and the firm claims these.
  **Provisional reading, applied and raised at close: IN where the firm's own
  list (any era) carries the company; OUT where the only evidence is Bessemer
  Securities' name on a holding.** The reasoning: the venture group that made
  those investments is the group that became the firm, with continuous
  people (the precedent closest to it is a16z's and Thrive's incubations held
  before a fund existed, IN where the firm lists them), while a family-office
  holding the venture firm never listed has no tie to the venture group at
  all. Rows this reading admits are flagged `pre_spinout` so the class can be
  counted and reversed in one pass.

## Run-time standing rulings

- **R1: Control positions (2026-10-01, the standing control rule, COLLECTION.md
  s1 T3).** A transaction in which Bessemer, alone or with its co-investor
  group, bought control is `not_member`, whether or not the firm lists the
  company. Ruled so far, each with its citation in the ledger: Netsmart
  Technologies (taken private with Insight, announced 2006-11), TeamViewer and
  LogicNow / GFI Software (the Insight-led buyout vehicle of 2009, per GFI's
  F-1), ThreatTrack Security (spun out of that GFI holding), GTS Central Europe
  (a consortium bought the whole company, 2008-01), Litify (majority stake,
  2023-02), Medi Assist (the firm's own memo: "to finance the management
  buyout"), WiredScore and its legal entity (majority purchase by the investor
  group Bessemer and Fifth Wall led, 2017-10), Syncsort (a group including
  Bessemer bought a majority, 2008-04), Metalogix (bought with Insight, 2008),
  CRI (Centerbridge and Bessemer took a combined 51% voting interest, 2024),
  Harman International (the 1980 investor-group buyout from Beatrice). A
  minority growth round beside a buyout sponsor stays a member (Anaqua, Ziff
  Davis Enterprise, United Capital, checked 2026-10-06).
- **R2: Names in the firm's own history narrative (2026-10-06).** The firm's
  2008 history page (`/port/onepage.asp`, Common Crawl capture of 2008-11-20)
  says "Pete Bancroft joined Bessemer in 1967 to lead the venture practice.
  Some of his signature deals were Measurex, Fotomat, and Interdata." Those
  three are the venture group's deals stated on the firm's own site: IN as
  recall additions, flagged `pre_spinout` (X1). The same page's "early private
  investments" (W.R. Grace, International Paper, Ingersoll Rand, Automatic
  Sprinkler Corporation of America) are the family office's holdings from
  before a venture practice existed and are not rows (X1, second leg).
- **R3: BVP India's purchases of listed companies (2026-10-01, T3).** The
  India desk of 2006 to 2010 bought stakes in companies that were already
  listed (PIPEs and open-market purchases) and the firm listed them beside its
  venture rounds. A row whose first Bessemer money went into an already
  listed company is `not_member` (Shriram City Union Finance: listed 2005,
  stake 2008; Anant Raj Industries; Ganesh Housing; Riddhi Siddhi Gluco
  Biols; Tulip Telecom). The same rule removes three older rows whose first
  Bessemer money went into a listed company: Centocor (public 1982, entry
  1989), Commercial Federal (public 1984, entry 1992) and Portrait Software
  (AIT Group, a listed company rescued in 2002). A pre-IPO placement is a
  member at Growth (OnMobile, Shriram EPC, Motilal Oswal). Each such row is
  decided on its own listing date and entry date.
- **R4: The Forge team's prior-firm companies (2026-10-01, the partner-carried
  rule, Erik 2026-09-17).** The January 2022 capture of bvp.com/companies
  carried eleven companies that appear in no other capture, carry no
  investment year and no Bessemer partner, and are the "Our Experience"
  companies of the BVP Forge team from their earlier firms: 1010data,
  AbsenceSoft, Appriss, Avetta, Cority, Diligent, Galvanize, Supplier.io, The
  Retail Equation, Turnitin, Vector Solutions. All `not_member`, cited to the
  firm's own Forge page for each.
- **R5: The Gator Co-Invest vehicles are BVP Forge's (2026-10-06).** The Form
  D of each Gator vehicle carries the related-person list of BVP Forge II
  (Scott Ring, Sandra Grippo, Rob Arditi, Navid Oreizy, Brian Feinstein,
  Jeremy Levine, Robert Goodman), not a venture fund's, and each was filed
  within weeks of a BVP Forge announcement: PA = Parsec (2023), VE = Vector
  (2025), TE = Technical Toolboxes (2025), BE = BetterRx (2025), LI =
  Lightning Step (2025). They are desk `forge` in `config.json`; D1 and D7 are
  corrected above. None produced a base row.
- **R6: Sale consideration (Erik 2026-09-22), as applied here.** Out: Insmed
  (stock for Transave, 2010), Ola (stock for TaxiForSure, 2015), Gentle Dental
  Service Corp (stock for GMS Dental Group, 1997; GMS Dental Group is the row,
  a recall addition), Mondee (stock for Rocketrip, 2020, never a row). eBay
  (Skype) and Okta (Auth0) surfaced only in the full-text sweep and were
  rejected there; both are also on the firm's anti-portfolio (D10).
- **R7: Companies on both bvp.com and the Forge grid (2026-10-06).** CRI,
  Current (formerly Crete Professionals Alliance) and StayTerra appear on the
  Forge site's company grid without the prior-experience mark and are also
  claimed on bvp.com (the portfolio list, or a firm post naming the deal
  among a venture investor's deals). The public record does not say which
  fund holds them. The site-listing rule decides: IN, unless a source shows
  the transaction was a purchase of control (then R1).
  **Applied 2026-10-06:** the firm's own page for Brian Feinstein says he "led
  growth buyout investments in Litify, LiveAuctioneers (acq), Beyond, Current,
  and CRI". A buyout is a purchase of control in the firm's own words, so all
  five are `not_member` under R1 (Litify and CRI also on press that states the
  majority). StayTerra stays IN: a minority growth investment beside the
  existing sponsor, named by the firm among a venture investor's deals. This
  class is raised at close because three of the five rest on the firm's label
  alone.
- **R8: Ualá is the Latin American digital bank (2026-10-06).** The firm's
  2021 and 2022 listings carried the name "UALA" with the description and
  website of Uala, an Italian beauty booking marketplace; from 2023 the
  website is Ualá's (uala-abc.com.mx) and from 2025 the description is the
  bank's, with founding year 2017, partnered year 2017 and Brian Feinstein as
  the deal partner, all of which fit only the bank (founded by Pierpaolo
  Barbieri in 2017). The early text was the firm's own error, corrected in its
  CMS. The row is Ualá the bank; no Bessemer round is named in any source
  read, so the entry stage stays undetermined and membership rests on the
  firm's listing.
- **R9: A round's place in the sequence is not its name (2026-10-06, the
  blind sample, COLLECTION.md s6).** The second pass read "first institutional
  round", "first round" and "every round from the first" as Series A, and
  "second round" as Growth, on the lead's own brief. The playbook retired
  exactly that convention (Erik, 2026-09-19): the label follows what the
  record calls the round. Swept: 36 stages returned to `undetermined` (30
  Series A, 5 Growth, and Good Technology's Seed, which rested on "incubated");
  entry dates kept. Kept: a stage where a document names the series (HotJobs:
  the S-1's Series A preferred), a later-stage word ("later rounds", "growth
  stage") or the next round's letter fixes it (Zoomin).
- **R10: Zapier graduated (2026-10-06, verify rule 7).** Zapier raised no
  primary round after its 2012 seed; the later priced event is the 2021 sale
  of shares to Sequoia and Steadfast at $5B. A row at $1B or more cannot read
  `not_graduated`, so it reads `graduated` on that event, at medium
  confidence.
- **R11: The Exploration Company reads 1b_plus at $2.0B (2026-10-06, rule
  10).** The figure is the Financial Times' report of the Series C while it
  was being raised (via The Next Web, 2026-07-27); the round closed on
  2026-09-08 with no price disclosed. Atomico, Balderton and EQT Ventures
  carry that mark at low confidence; this book follows them and Cherry's row
  is aligned up.
- **R12: Sorare keeps its 2021 mark** ($4.3B, stale). Erik's ruling E2 of
  2026-09-28 (Headline's decisions.md): layoffs and an unpriced insider round
  do not band a row. The A/B pass's downgrade was reverted the same day.
- **R13: Mergers of two portfolio-adjacent companies (2026-10-06, R6).**
  Hightower merged into VTS in 2016: Hightower is the row (acquired), VTS and
  its legal-name rows are out. Intercom renamed itself Fin in 2026 before
  Salesforce bought it: one row, published as Intercom. Cogent
  Communications replaced PSINet on the firm's 2019 list (it bought PSINet's
  assets in 2002): PSINet is the row, Cogent is out.
- **R14: Resurfaced name variants of excluded companies (2026-10-06).** At
  the first rebuild nine other renderings of excluded companies came back as
  new rows (LogicNow (GFI), LogicNow S.A., GFI Software S.a r.l., GTS, Beyond
  Pricing, VTS formerly Hightower, View The Space Inc., Ola Cabs, Generate
  Capital Inc.). Each takes its company's verdict; all left at the final
  rebuild.

