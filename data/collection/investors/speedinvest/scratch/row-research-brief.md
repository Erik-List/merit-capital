# Row research brief (Speedinvest, PRO-84)

You research a list of Speedinvest portfolio companies for a venture-capital data
pipeline. Speedinvest is a Vienna early-stage VC founded in 2011 (EUR 10M first fund),
now a multi-team European seed firm with growth and Middle East & Africa teams.
Work from `/Users/erik/Developer/merit-capital`. The only file you may write is the
output JSON your task names, plus scratch files inside your own folder
`data/collection/investors/speedinvest/scratch/research/<group>-work/`. Never edit
anything else, never run `scripts/run.py`, never git.

## Start from what is on disk (free)

`python3 data/collection/investors/speedinvest/scratch/pack.py <slug> [<slug> ...]` prints what the
pipeline already holds for each row:
- SITE: the firm's live card: "Year Invested" (a close-year anchor, never a round), sector and team
  tags (Growth = the growth team; Middle East, Africa & Beyond = the MEA team), status (`exited` = the
  site's Exits tag), country, website, and the card's own description. **The description often states the
  exit in the firm's own words** ("Amodo (acquired by Cambridge Mobile Telematics in 2023)"): that sentence,
  on the card's URL, is a first-party citation for status.
- BOARD: the firm's Getro job board record (its `stage` describes the company TODAY; never use it as a round).
- ARCHIVE: the firm's archived 2017-2025 listings and pages: the deal partner ("Investment Manager"), the
  firm's invest year, filter tags (`pre_seed` = the firm tagged it in its 2018-2020 Pre-Seed filter;
  `acquired`/`active`), and the first capture URL (a valid citation for the firm's listing).
- POST: the firm's own posts naming the row (URL = citation). Speedinvest's "Our investment in X" posts
  usually announce the round Speedinvest LED or joined; read whether it was the FIRST round.
- REGISTER: the Austrian or German register reading (North Data) where one exists: terminated, liquidation,
  insolvency, and shareholder events naming Speedinvest vehicles.
- NEWS: headlines an automatic search found. SIBLING: other investor books that hold the same company.

The firm's posts in full: `data/collection/investors/speedinvest/sources/site/press-archive.json`
(`posts`, each with `capture_url`, `text`). Grep it for one-word names the index skips.
Sibling books: `grep -i "<name>" data/collection/investors/*/companies/base.csv`.

## Search

- **Google News, uncapped, use first:**
  `python3 data/collection/investors/atomico/scratch/news.py "query" --all --decode 5`
  prints dated headlines and decodes the first 5 round or exit headlines to publisher URLs.
  Add `--pick "<word>"` to decode a specific headline. For Austrian, German or French companies, query in
  German or French too ("Finanzierungsrunde", "Millionen", "levée").
  One-word names collide (Open, Due, Well, Ray, Drop, Genie): always qualify with the product, city or a
  founder ("Open business banking India").
- **WebSearch** only within the budget your task gives. **WebFetch** freely on specific pages.
- **Austrian and German company status:** North Data's free suggest endpoint,
  `curl -s -A "Mozilla/5.0" "https://www.northdata.com/suggest.json?query=<name>&countries=AT,DE"`,
  then the company page: a cross after the name, `Liquidation`, `Insolvenz`, `gelöscht` or a new sole
  shareholder. A dissolution, liquidation or insolvency in the home register is filing-grade evidence, and
  the page URL is the citation. The Austrian insolvency register is edikte.justiz.gv.at.
- UK companies: Companies House (`https://find-and-update.company-information.service.gov.uk/search?q=<name>`)
  shows dissolved / liquidation status.

## What to find per row

0. **Identity** (archive-only rows especially): which company this is (website, city, what it does). If the
   row is not an operating company (a fund, a programme, a studio, a page title), say so. If you cannot tell
   what company it is, say `identity_unresolved`.
1. **Speedinvest's ENTRY round**: the round in which a Speedinvest fund first put money in.
   - Give the date (month if known), the round as the record names it (Pre-Seed, Seed, Series A, Series B...),
     the amount, the lead, and a citation URL that names that round AND ties Speedinvest to it.
   - Read the firm's own posts first. A post announcing a round Speedinvest LED may be a follow-on; it states
     the entry only where the post says so in words ("we first invested in ... in 2016").
   - A press "Series A" can skip a seed Speedinvest led earlier. Check whether Speedinvest was already in.
   - Growth-tagged rows were often entered at Series B or later by the growth team: find that round.
   - If nothing names Speedinvest's round, say `null`. Never guess.
2. **All funding rounds you can see**, as a list:
   `{"date", "round", "amount_usd", "amount_native", "lead", "firm_in_round", "source", "source_type": "firm|company|press|filing|vendor"}`.
   Convert EUR, GBP or other currencies only approximately in `amount_usd`; the pipeline re-converts.
3. **For a Seed or Pre-Seed entry: the next round.**
   - A later round the record NAMES as Series A or later, with date and citation, graduates the row.
   - An unnamed later round counts only with its amount.
   - If you find no later round, say so and list what you searched: the firm posts, the Google News queries
     (English and home language), the company site.
4. **Status now (2026-09-30)**: `private`, `acquired` (acquirer, date, citation), `public` (exchange, ticker)
   or `defunct` (shutdown, liquidation or insolvency, with citation).
   - An insolvency followed by an asset sale is `acquired` (note the successor).
   - An insolvency with no sale yet is `defunct`.
   - Speedinvest selling its stake to another investor is NOT the company being acquired.
   - An acqui-hire that does not buy the company leaves the company `defunct` if it shut down.
5. **Valuation**: only a priced round or market cap stating a figure of $1B or more. Otherwise `below_1b`.
   Vendor estimates (PitchBook, Dealroom, Tracxn, CB Insights, GetLatka, Crunchbase profile pages) are never
   a source. For a recent (2021+) AI, fintech, data or developer-tools company, check once for a 2025-2026
   round at $1B+ and record what you found.
6. **HQ**: city and ISO country code (current HQ; last known for dead or acquired companies). Municipality,
   not metro; English exonym (Vienna, Munich).
7. **Focus**: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
   Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
   Media, Gaming & Advertising; or null if none fits.
   Healthcare SaaS is Healthcare & Bio. Security wins when security is what the company sells.
   AI & Applied AI means AI is the product.

## Rules

- Re-fetch every URL you cite and confirm the page states what you claim. A citation you did not load is worse than none.
- A vendor page may guide you and may appear in `rounds` with `source_type: vendor`, but is never the citation
  for a stage, graduation, status or figure.
- A paywalled page proves what its visible headline or snippet names.
- Keep quotes under 25 words, copied from the page.
- Write your output file incrementally (after every few rows), so an interruption loses little.

## Output per row (JSON object keyed by slug)

```
"<slug>": {
  "name": "...",
  "identity": {"website": "...", "what": "one line", "operating_company": true, "unresolved": false},
  "entry": {"date": "YYYY-MM", "round": "Seed", "amount": "EUR 1.5M", "lead": "...",
            "citation": "url", "quote": "...", "speedinvest_named": true,
            "entry_asserted": "how the source shows this was Speedinvest's FIRST round"} | null,
  "rounds": [...],
  "graduation": {"later_round": "Series A", "date": "YYYY-MM", "citation": "url", "quote": "..."}
              | {"none_found": true, "searched": ["firm posts ...", "googlenews: <query> -> ...", "company site ..."]}
              | null (entry not Seed/Pre-Seed),
  "status": "private|acquired|public|defunct|unknown", "status_detail": "...", "status_citation": "url",
  "valuation": {"range": "below_1b|1b_plus|10b_plus|100b_plus", "usd": null, "citation": null, "asof": null},
  "hq_city": "...", "hq_country": "AT", "hq_citation": "url or null",
  "focus": "...",
  "confidence": "high|medium|low",
  "notes": "one or two sentences"
}
```
