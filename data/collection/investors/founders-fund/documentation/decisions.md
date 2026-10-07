# Founders Fund: investor-specific decisions

Run started 2026-09-27. Read COLLECTION.md in full at kickoff. The requested "Founders Funds" is interpreted as Founders Fund, foundersfund.com.

## Verified facts

- The current Form ADV is the 2026-03-30 annual amendment for Founders Fund LLC, CRD 155462, SEC 802-75555, an exempt reporting adviser. It identifies San Francisco as the principal office and Miami as another office. It names the flagship and Growth management entities in Section 7.A. Source: https://reports.adviserinfo.sec.gov/reports/ADV/155462/PDF/155462.pdf, downloaded at kickoff. Search-engine text still showed 2025; the downloaded document is newer.
- The public WordPress API exposes 64 company posts and 30 team posts, each in one page. Source: https://foundersfund.com/wp-json/wp/v2/types and pagination headers of the company/team endpoints. Company posts carry descriptions and industries, but no entry-round or investment-date claim.
- The site's Peter Thiel biography distinguishes his personal first Facebook investment and founder roles at PayPal and Palantir from the firm's investments. https://foundersfund.com/team/peter-thiel/
- Sean Parker joined in 2006 and stopped making new investments for the firm in 2014, retaining seats on existing investments. https://fortune.com/2014/03/06/sean-parker-formally-leaves-founders-fund/
- Luke Nosek and Geoff Lewis left in 2017 for independent firms. https://www.axios.com/2017/12/15/founders-fund-partner-leaves-to-launch-spacex-focused-fund-1513304489 and https://techcrunch.com/2017/08/21/geoff-lewis-left-founders-fund/

## Derivations

- D1, T1: flagship, Alpha, Growth, Entrepreneurs, Principals and co-investment vehicles under Founders Fund LLC are inside the boundary once matched to the adviser roster or its fund filings. Same-adviser precedent: a16z and Thrive. Foreign office location alone does not create a separate firm.
- D2, T2/T4: Thiel's, Nosek's, Howery's and Parker's personal investments, founder positions and pre-firm operating roles are outside unless a Founders Fund vehicle separately invested. Facebook needs the fund's own first check, rather than Thiel's 2004 angel check. Prior- and next-firm seats are dated individually; retained boards cannot date a new fund investment.
- D3, T1/T4: Gigafund, Bedrock, Valar, Mithril, Clarium and other separately operated firms are outside. Shared founders or a Founders Fund LP commitment do not transfer their portfolio membership. A company funded by both stays on its independently evidenced Founders Fund entry.
- D4, T3: minority private financings, secondaries and tenders are inside; first public-market purchases, sale-consideration stock, control acquisitions and sponsor promotes are outside under the standing rules. A secondary or tender entry is Growth.
- D5, T5: fund vehicles and feeder/SPV structures are not company rows. Direct token positions require an operating or issuing organization. No exception to the standing taxonomy is proposed.
- D6, evidence sufficiency: a company listing on the firm's own current or archived site suffices for membership, subject to the standing founder-angel and sale-consideration exceptions. Form D names alone need corroboration and tenure review. The company API's publication date is a CMS date, never an entry date; its industry is corroboration, never an entry-stage label.

## Deltas requiring a new ruling

None identified at kickoff. New evidence is adjudicated under the standing tests; genuinely uncovered boundaries will be reported with the review artifacts.

## Session change, 2026-10-06

The run was started by a Codex session on 2026-09-27 and last written on 2026-10-02 (170-row provisional base, 72 verdicts, 54 classified rows, no process left running). A Claude Code session took it over on 2026-10-06 at Erik's kickoff, re-read COLLECTION.md in full, kept the evidence on disk and the answers already recorded, and completed the layers the first build never had (the archive, the wider roster, the vehicle roster of the ADV). Linear: PRO-81.

## Verified facts added 2026-10-06

- **The firm publishes a list, and always did.** PRO-81's prior ("a firm that publishes little") is wrong: the live site lists 64 companies, and the archive holds three earlier listing generations: thefoundersfund.com/portfolio.html (2006 to 2009), foundersfund.com/portfolio.php (2009 to 2011) and WordPress /company/<slug> pages from 2011 on, 218 distinct slugs in the index. The first archive pull began at 2014 and so missed every slug first captured 2009 to 2013.
- **Section 7.B of the 2026-03-30 ADV lists 48 private funds** (sources/edgar/adv-7b-roster.json): 23 flagship vehicles (funds I to IX with their Entrepreneurs and Principals funds), eight Growth vehicles (Growth I to IV with their Principals funds), FFAV, LLC, and sixteen deal vehicles: Founders AND and AND2 to AND6, Founders ANT, Founders OPEN and OPEN II, Founders SPC, Gopher E, Erebor, Mirian, Miruvor, Lembas II and Lembas II Series F.
- **Only five deal vehicles ever filed a Form D** (sources/edgar/spv-formd.json): Founders Fund SpaceX Fund, LP (2009, $6.7M sold), Lembas III, LP (2010-10, $9.5M, general partner The Founders Fund III Management), Miruvor, LP (2019-02, $84.3M), Erebor, LP (2019-09, $54.9M) and Mirian, LP (2023-03, $64.75M). The AND, ANT, OPEN, SPC and Gopher vehicles have no EDGAR identity at all.
- **FF Angel and FF Science are fund subsidiaries, not a scout programme.** FF Angel, LLC, FF Angel IV, LLC, FF Science V, LLC and FF Science VI, LLC sign investors' rights agreements and hold stock in their own names (Twilio, SendGrid, Credit Karma, Compass, Notable Labs: exit-side SEC filings in sources/edgar/fts-hits.json). The numeral follows the flagship fund.
- **"Founders Fund" is also Kleiner Perkins' name for its partner side funds** ("KPCB XIV Founders Fund, LLC"), which is most of the noise in the exit-side full-text sweep: 139 third-party registrants, 53 naming a vehicle of this firm.
- **Founders Fund Growth files Form 13F** (Founders Fund Growth Management, LLC, 2022 on), and a Growth sub-vehicle, FF Consumer Growth II, LP, filed Schedule 13G on BitMine Immersion and on ETHZilla (formerly 180 Life Sciences) in 2025.

## Derivations added 2026-10-06 (the three questions PRO-81 asks)

- D7, T1/T5, deal vehicles: every deal vehicle on the ADV roster is the firm's own money under the firm's own adviser, so a company held through one is a member like any other, and the vehicle is never a row. Where the vehicle carries the firm's FIRST money into the company the entry is the round the vehicle funded; where the funds were already in, the vehicle is a follow-on and the entry is unchanged (Lightspeed's Project Mercury, Creandum's Select funds and SPV TR). The row does not say which vehicle holds it: the published columns describe the company and the entry round, not the plumbing.
- D8, T1, Growth: the Growth funds are the same adviser's later-stage venture funds, not a second desk. The strategy-desk partition is for non-venture strategies of one adviser (buyout, credit, public equities); a growth-stage venture round is a venture round. No partition; `desks.partition` stays empty.
- D9, T2/T4, partners' own vehicles: Thiel Capital, Rivendell One and the first Lembas, LLC (Thiel's own Facebook holders, named beside the funds in Facebook's S-1), Mithril, Valar, Clarium, the Thiel Foundation and Breakout Labs, Parker's own entities, Gigafund, Howery's own entities, Long Journey, A-Star and Rabois's personal investments are outside. A vehicle is the firm's when it sits on the firm's ADV or is signed by a Founders Fund management company (Lembas II, Lembas III, Lembas V), whatever its name. The unrelated Lembas Capital LP and Lembas Fund, LLC share only the word.
- D10, T2, FF Angel and FF Science: positions of these subsidiaries are fund money and are members (Sequoia Arc, a16z speedrun). They are ordinary negotiated seed rounds, not a standard-terms programme, so the stage follows the round the record names and `program_terms` does not apply.
- D11, T3, public-market and PIPE positions: BitMine Immersion and ETHZilla (13G positions taken in listed companies in 2025) are outside, and so is a position that exists only as a PIPE into a listing (Opendoor: The Founders Fund Growth, LP, 125,000 shares on the December 2020 resale prospectus). A company a fund backed in a private round stays a member after it lists or merges into a shell (Hims & Hers, Strive).
- D12, T5 and sale consideration: LP stakes held by the funds (Revolution Capital, 500 Startups, CrunchFund, TechFellow) are not rows. An acquirer on whose registration statement a fund appears as a selling stockholder is not a row; the company it bought is (Secure Computing for CipherTrust, Identiv for 3VR, Sprinklr for Booshaka, Intuit for Credit Karma, Uber for Postmates, Adobe for Figma).

## Erik's rulings, 2026-10-07

- **E1: Ken Howery's 2025 financial disclosure is used.** It is the OGE Form 278e a presidential nominee files (Howery was nominated ambassador to Denmark); because he still holds interests in the funds he co-founded, its endnotes list what The Founders Fund, LP and the Principals funds of Funds II, III and IV hold, and say the main funds hold the same. The run had set it aside because the Office of Government Ethics restricts commercial use of such reports (5 U.S.C. 13107(c)); Erik ruled it in. It is a sworn list, so a company on it is a member (class `web`, the report as citation). It names 34 operating companies: 24 were already in the book under 23 rows, 6 are new (AppCard, Five Apes, Indigo Technologies, Instapray, Neurotrack, theAudience), and 4 are stock received when a portfolio company was sold and stay out under D12 (Sabse for Jaxtr, Freethink Media for Big Think, NetBase for Quid, Higher Ground Education for AltSchool). The fund-of-fund and LP entries (Revolution Capital, 500 Startups, CrunchFund, TechFellow) are not rows. Limits: it covers Funds I to IV only, and only what was still held at the end of 2024, so exits are absent and it never dates or names a round. Source: sources/web/howery-2025-fund-notes.json.
- **E2: Avalanche is below $1B, in this book and in a16z's.** A token's market value is not a mark on the company; no priced round of Ava Labs carries a citable figure. The AVAX network value stays in the note. This replaces R7's first half.

## Run-time rulings, 2026-10-06 (flagged for review)

- R1, T2: Friendster is out. Peter Thiel's personal 2003 angel round; the firm listed it 2010 to 2012, no fund on any round.
- R2, T5: fbFund (a seed fund run with Facebook and Accel) and Vittana (a non-profit) are out though the firm listed them.
- R3, T4: a director of record in tenure whose issuer never resolves to a known company is out (Homevest Inc., SpotMap, Inc.).
- R4, D3: ownership filings co-filed by Peter Thiel with Mithril or Clarium entities are those firms' positions (Adagio, BlackSky, Fractyl, PEMCO).
- R5: the "FF Angel" group of the 2012-13 site menu is corroboration for a seed entry, never a label; Cherry, filed there, was a Series A entry.
- R6: a legal-name issuer that is a listed company under its trade name is merged, not kept (Careportal/Cedar, Indie Technologies/Found, Miami Labs/OpenStore, Virtual Kitchen/All Day Kitchens, Homee/Hutch, Pharmacofore/Signature Therapeutics).
- R7: Anvil and Avalanche are token positions, stage and graduation undetermined (Avalanche's value: E2).
- R8: the recall additions (64) rest on a sentence or headline naming Founders Fund, cited per row in the ledger.

## Run-time findings

- 2026-09-27: Internet Archive CDX returns HTTP 503 with "Temporarily Offline"; Common Crawl index probe returns HTTP 502. Historical coverage is pending, not absent. The current-site and SEC layers proceed independently.
- 2026-09-27: No Linear connector is available in this task. Milestones and run provenance are retained locally and in task updates. (From 2026-10-06 the run posts to PRO-81.)
