# Row research brief (Project A, PRO-102)

You research a list of Project A portfolio companies for a venture-capital data
pipeline. Project A (Project A Ventures) is a Berlin early-stage VC founded in 2012.
Work from `/Users/erik/Developer/merit-capital`. The only file you may write is the
output JSON your task names. Never edit anything else.

## Start from what is on disk (free)

`python3 data/collection/investors/project-a-ventures/scratch/pack.py <slug> [<slug> ...]` prints the
evidence the pipeline already holds for each row:
- the firm's live CMS fields: invest year, the firm's own round word, fund, status, HQ, founded year;
- the firm's archived fields (2012-2024 pages);
- the firm's own press posts naming the row;
- news headlines found by an automatic search;
- other investor books that hold the same company (SIBLING lines).

The firm's own posts (full text) are in
`data/collection/investors/project-a-ventures/sources/site/press-archive.json`, under `posts`, keyed by
post slug. Each post has its `capture_url`: the citation for that post.

Sibling books hold cited rows: `grep -i "<name>" data/collection/investors/*/companies/base.csv`.

## Search

- **Google News, uncapped, use first:**
  `python3 data/collection/investors/atomico/scratch/news.py "query" --all --decode 5`
  It prints dated headlines and decodes the first 5 round or exit headlines to publisher URLs.
  Add `--pick "<word>"` to decode a specific headline.
  One-word company names collide (Bucket, Butter, Baobab, Q, Twig, Origin). Always qualify the query with
  the product, city or a founder ("Bucket feature flags Copenhagen").
- **WebSearch** only within the budget your task gives. **WebFetch** freely on specific pages.
- **German company status:** North Data's free suggest endpoint,
  `curl -s -A "Mozilla/5.0" "https://www.northdata.com/suggest.json?query=<name>&countries=DE"`,
  then the company page for `in Liquidation`, `gelöscht`, `Insolvenz` or a new owner.
  A dissolution, liquidation or insolvency in the home register is filing-grade evidence.

## What to find per row

1. **Project A's ENTRY round**: the round in which a Project A fund first put money in.
   - Give the date (month if known), the round as the record names it (Pre-Seed, Seed, Series A, Series B...), the amount, the lead, and a citation URL that names that round AND ties Project A to it.
   - Read the firm's own posts first. A firm post announcing a round Project A LED may be a follow-on; it states the entry only where the post says so in words.
   - A press "Series A" can skip a seed the firm led earlier. Check whether Project A was already in an earlier round.
   - The firm's CMS invest year is a close year, not an announcement date.
   - If nothing names Project A's round, say `null`. Never guess.
2. **All funding rounds you can see**, as a list:
   `{"date", "round", "amount_usd", "lead", "firm_in_round", "source", "source_type": "firm|company|press|filing|vendor"}`.
   Convert EUR, GBP or SEK only approximately in `amount_usd`; the pipeline re-converts. Keep the native figure in `amount_native`.
3. **For a Seed or Pre-Seed entry: the next round.**
   - A later round the record NAMES as Series A or later, with date and citation, graduates the row.
   - An unnamed later round counts only with its amount.
   - If you find no later round, say so and list what you searched: the firm posts, Google News queries, the company site.
4. **Status now (2026-09-30)**: `private`, `acquired` (acquirer, date, citation), `public` (exchange, ticker) or `defunct` (shutdown, liquidation or insolvency, with citation).
   - An insolvency followed by an asset sale is `acquired` (note the successor).
   - An insolvency with no sale yet is `defunct`.
   - Project A selling its stake to another investor is NOT the company being acquired.
   - An acqui-hire that does not buy the company leaves the company `defunct` if it shut down.
5. **Valuation**: only a priced round or market cap stating a figure of $1B or more. Otherwise `below_1b`.
   Vendor estimates (PitchBook, Dealroom, Tracxn, CB Insights, GetLatka, Crunchbase profile pages) are never a source.
6. **HQ**: city and ISO country code (current HQ; last known for dead or acquired companies).
7. **Focus**: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
   Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
   Media, Gaming & Advertising; or null if none fits.
   Healthcare SaaS is Healthcare & Bio. Security wins when security is what the company sells.

## Rules

- Re-fetch every URL you cite and confirm the page states what you claim. A citation you did not load is worse than none.
- A vendor page may guide you and may appear in `rounds` with `source_type: vendor`, but is never the citation for a stage, graduation, status or figure.
- A paywalled page proves what its visible headline or snippet names.
- Keep quotes under 25 words, copied from the page.

## Output per row (JSON)

```
"<slug>": {
  "name": "...",
  "entry": {"date": "YYYY-MM", "round": "Seed", "amount": "EUR 1.5M", "lead": "...",
            "citation": "url", "quote": "...", "project_a_named": true, "entry_asserted": "how the source shows this was Project A's FIRST round"},
  "rounds": [...],
  "graduation": {"later_round": "Series A", "date": "YYYY-MM", "citation": "url", "quote": "..."} | {"none_found": true, "searched": ["firm posts ...", "googlenews: <query> -> ...", "company site ..."]},
  "status": "private|acquired|public|defunct", "status_detail": "...", "status_citation": "url",
  "valuation": {"range": "below_1b|1b_plus|10b_plus", "usd": null, "citation": null, "asof": null},
  "hq_city": "...", "hq_country": "DE",
  "focus": "...",
  "confidence": "high|medium|low",
  "notes": "one or two sentences"
}
```
