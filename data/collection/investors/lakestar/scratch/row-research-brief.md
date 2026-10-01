# Row research brief (Lakestar, PRO-108)

You research a list of Lakestar portfolio companies for a venture-capital data pipeline.
Lakestar is a European venture firm (Zurich, Berlin, London) founded by Klaus Hommels; its first
institutional fund dates from 2013 (Lakestar I), then Lakestar II (2015), Lakestar III and Growth I
(2020), Early IV and Growth II (2022 to 2024), a continuation fund (2025) and Resilience I (2026).
Work from `/Users/erik/Developer/merit-capital`. The only file you may write is the output JSON your
task names (plus scratch files inside the folder your task names). Never edit anything else, never
run git commands, never touch `scripts/`.

## Start from what is on disk (free)

`python3 data/collection/investors/lakestar/scratch/pack.py <slug> [<slug> ...]` prints the evidence
the pipeline already holds for each row:
- the firm's archived site fields: the stage field (Seed / Early / Growth / Exit/IPO: NOT a reliable
  entry round, treat it as a hint only), thesis, deal partners, the firm's sentence about the company;
- LINKED lines: press articles the firm itself attached to the company page (often the round
  announcement Lakestar joined);
- FIRM POST lines: the firm's own posts naming the row (full text in
  `data/collection/investors/lakestar/sources/site/press-archive.json` under `posts`; each post's
  `capture_url` is its citation);
- SIBLING lines: other investor books that hold the same company, with their cited status, valuation
  and notes. A sibling's valuation citation and figure can be reused once you re-load the page. Check
  that the sibling row is the SAME company (one-word names collide: Agora, Trace, Welcome, Loci,
  Tesseract, Symphony, Piggy, minimum, Forward, Public, Rows, Five, Figure, Cedar).

## Search

- **Google News, uncapped, use first:**
  `python3 data/collection/investors/atomico/scratch/news.py "query" --all --decode 5`
  prints dated headlines and decodes the first 5 round or exit headlines to publisher URLs. Add
  `--pick "<word>"` to decode a specific headline. Always qualify one-word names with the product,
  city or a founder ("Rows spreadsheet Berlin", "Welcome hospitality app Stockholm").
- **WebSearch** only within the budget your task gives. **WebFetch** freely on specific pages
  (company newsroom, TechCrunch, Sifted, EU-Startups, Tech.eu, Gründerszene, deutsche-startups.de,
  press releases).
- **Company status in the home register:**
  - Germany: `curl -s -A "Mozilla/5.0" "https://www.northdata.com/suggest.json?query=<name>&countries=DE"`,
    then the company page for `in Liquidation`, `gelöscht`, `Insolvenz` or a new owner.
  - Switzerland: `curl -s -A "Mozilla/5.0" -H 'Content-Type: application/json' -d '{"name":"<name>","languageKey":"en","maxEntries":20,"offset":0}' https://www.zefix.admin.ch/ZefixREST/api/v1/firm/search.json`
    (status `EXISTIEREND`, `AUFGELOEST` (in liquidation) or `GELOESCHT` (deleted)); details at
    `https://www.zefix.admin.ch/ZefixREST/api/v1/firm/<ehraid>.json`.
  - UK: `https://find-and-update.company-information.service.gov.uk/search/companies?q=<name>` and the
    company page (Active, Dissolved, Liquidation, Administration).
  A dissolution, liquidation or insolvency in the home register is filing-grade evidence.

## What to find per row

1. **Lakestar's ENTRY round**: the round in which a Lakestar FUND first put money in.
   - Give the date (month if known), the round as the record names it (Pre-Seed, Seed, Series A,
     Series B ...), the amount, the lead, and a citation URL that names that round AND names Lakestar
     in it.
   - Read the firm's own posts and LINKED articles first. A firm post announcing a round Lakestar LED
     may be a follow-on; it states the entry only where it says so in words or where no earlier round
     with Lakestar exists.
   - A press "Series B led by Lakestar" can hide an earlier Lakestar seed or Series A. Check every
     earlier round's investor list before calling a round the entry.
   - Klaus Hommels also invests personally (before 2013 through Hommels Holding, and since). A round
     that names only "Klaus Hommels" as an angel, with no Lakestar fund, is NOT a Lakestar entry: say
     so in `notes` and set `lakestar_named` false.
   - If nothing names Lakestar's round, say `null`. Never guess.
2. **All funding rounds you can see**, as a list:
   `{"date", "round", "amount_usd", "amount_native", "lead", "firm_in_round", "source", "source_type": "firm|company|press|filing|vendor"}`.
   `firm_in_round` is true, false or null (unknown) for Lakestar. Convert EUR, GBP, SEK or CHF only
   approximately in `amount_usd`; the pipeline re-converts from `amount_native`.
3. **For a Seed or Pre-Seed entry: the next round.**
   - A later round the record NAMES as Series A or later, with date and citation, graduates the row.
   - An unnamed later round counts only with its amount.
   - If you find no later round, say so and list what you searched: the firm posts, each Google News
     query with what it showed, the company site.
4. **Status now (2026-10-01)**: `private`, `acquired` (acquirer, date, citation), `public` (exchange,
   ticker) or `defunct` (shutdown, liquidation or insolvency, with citation).
   - An insolvency followed by an asset sale is `acquired` (note the successor).
   - An insolvency or bankruptcy with no sale yet is `defunct`.
   - An acqui-hire that does not buy the company leaves it `defunct` if it shut down, `private` if it
     still operates.
   - Went public and was later bought: `acquired`.
5. **Valuation**: only a priced round, tender or market cap stating a figure of $1B or more, with the
   figure, its currency, its date and a citation. For a public company give the market cap, as-of
   date and a quote page (companiesmarketcap.com, stockanalysis.com, Yahoo or Google Finance).
   Otherwise `below_1b`. Vendor estimates (PitchBook, Dealroom, Tracxn, CB Insights, GetLatka,
   Crunchbase profile pages) are never a source. For a company founded or funded in the last five
   years in AI, fintech, data infrastructure or developer tools, run one explicit check for a recent
   large round and say what you searched even if the answer stays `below_1b`.
6. **HQ**: city (the municipality, English name, no state or country suffix) and ISO country code;
   current HQ for live companies, last known for dead or acquired ones.
7. **Focus**: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security,
   Fintech & Payments, Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio,
   Consumer & Marketplaces, Media, Gaming & Advertising; or null if none fits.
   Healthcare software is Healthcare & Bio. Security wins when security is what the company sells.
   Defence hardware, drones, space launch and satellites are Industrial & Robotics. Games are Media,
   Gaming & Advertising. Crypto & Web3 wins over Fintech for on-chain businesses.

## Rules

- Re-fetch every URL you cite and confirm the page states what you claim. A citation you did not
  load is worse than none. If a page is paywalled, what its visible headline or snippet names is
  enough, and say `paywalled` in the quote.
- A vendor page may guide you and may appear in `rounds` with `source_type: vendor`, but is never the
  citation for a stage, graduation, status or figure.
- Keep quotes under 25 words, copied from the page.
- Identify the company first. If the name is ambiguous and the pack gives a website, use the website.
  If you cannot tell which company the row is, say so (`"identity": "unresolved"`) and stop on it.

## Output per row (JSON object keyed by slug)

```
"<slug>": {
  "name": "...", "identity": "ok|unresolved", "what": "one line: what the company does, founded when, where",
  "entry": {"date": "YYYY-MM", "round": "Seed", "amount": "EUR 1.5M", "lead": "...",
            "citation": "url", "quote": "...", "lakestar_named": true,
            "entry_asserted": "how the source shows this was Lakestar's FIRST round"} | null,
  "rounds": [...],
  "graduation": {"later_round": "Series A", "date": "YYYY-MM", "amount": "...", "citation": "url", "quote": "..."}
              | {"none_found": true, "searched": ["firm posts ...", "googlenews: <query> -> ...", "company site ..."]}
              | null (entry is not Seed or Pre-Seed),
  "status": "private|acquired|public|defunct", "status_detail": "...", "status_date": "YYYY-MM", "status_citation": "url",
  "valuation": {"range": "below_1b|1b_plus|10b_plus|100b_plus", "usd": null, "native": null, "event": "what set the figure",
                "citation": null, "asof": null, "searched": "what the momentum check ran, if it applied"},
  "hq_city": "...", "hq_country": "DE", "hq_citation": "url or null",
  "focus": "...",
  "confidence": "high|medium|low",
  "notes": "one or two sentences"
}
```
