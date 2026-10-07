# Row research brief (Earlybird, PRO-107)

You research a list of Earlybird portfolio companies for a venture-capital data
pipeline. Earlybird (Earlybird Venture Capital) is a Berlin and Munich early-stage
VC founded in Hamburg in 1997: Funds I to VIII, the Growth Opportunities funds,
Earlybird Health (life sciences and medtech) and Earlybird-X (university spin-outs).
Work from `/Users/erik/Developer/merit-capital`. **The only file you may write is the
output JSON your task names.** Never edit anything else, never run git, never run
`scripts/run.py`.

Today is 2026-10-06.

## Start from what is on disk (free)

`python3 data/collection/investors/earlybird-venture-capital/scratch/eb_pack.py <slug> [<slug> ...]`
prints the evidence the pipeline already holds for each row:
- LIVE: the firm's live page (its own "Invested" year, deal team, HQ, status, description).
  The list's stage label ("Pre-Seed", "Seed", "Series A") is **unverified**: several are
  wrong (Aiven reads Pre-Seed and was a Series A entry). Never take it as the answer; check it.
- ARCHIVE: the firm's archived pages 2002 to 2026: years listed, the fund tag (Digital West,
  Health, Earlybird-X), "Current" / "Exit" / "Pre-Fund Investments" by year, exit route and date.
- TEAM: which partner listed the company on the archived team page.
- POST / PRESS: the firm's own posts (2024 to 2026) and press releases (2001 to 2010) that name
  the row, each with its capture URL. These are first-party and citable.
- EDGAR-FTS: SEC filings that name an Earlybird fund next to the company.
- SIBLING: other investor books that hold the same company, with their cited stage, status,
  valuation and note. Reuse their citations after re-fetching them.

Full text of the old press releases: `data/collection/investors/earlybird-venture-capital/sources/web/press-archive.json`.
Full text of the firm's recent posts: `.../sources/site/raw/searchIndex.json` (keys `/perspectives/...`, field `p`);
the public URL is `https://earlybird.com` + the key.

## Search

- **News headlines, uncapped, use first:**
  `python3 data/collection/investors/earlybird-venture-capital/scratch/news.py '"Name" query words' [--all] [--lang de]`
  queries Bing News (every item carries the publisher's own URL, citable after you load it) and
  Google News when it answers (it returned 503 for this machine today; add `--decode 5` to turn
  Google headlines into publisher URLs when it works). Put the company name in double quotes.
  One-word names collide (Hive, Keel, Deed, Curio, Ripe, Tilt, Ctrl, Versus, Moped): always
  qualify with the product, city or a founder. For a German, Swiss, Austrian, French or Nordic
  company also search in the home language ("Finanzierungsrunde", "Series A", "übernimmt",
  "Insolvenz", "levée de fonds") with `--lang de` / `fr`.
- **Publisher search endpoints, uncapped (curl, JSON):**
  - `https://www.deutsche-startups.de/wp-json/wp/v2/posts?search=<name>&per_page=20&_fields=date,link,title`
    (German startups; its DealMonitor posts name every round with its investors);
  - `https://techcrunch.com/wp-json/wp/v2/posts?search=<name>&per_page=20&_fields=date,link,title`;
  - `https://news.crunchbase.com/wp-json/wp/v2/posts?search=<name>&per_page=20&_fields=date,link,title`;
  - `https://tech.eu/?s=<name>` (HTML); the company's own newsroom or blog; Wikipedia
    (`https://en.wikipedia.org/w/index.php?title=<Title>&action=raw`, also `de.`).
- **WebSearch: at most 10 calls in total for your whole task.** Spend them on the rows the free
  surfaces cannot settle. **WebFetch** freely on specific pages.
- **German company status:** North Data's free suggest endpoint,
  `curl -s -A "Mozilla/5.0" "https://www.northdata.com/suggest.json?query=<name>&countries=DE"`,
  then the company page for `in Liquidation`, `gelöscht`, `Insolvenz` or a new owner.
  A dissolution, liquidation or insolvency in the home register is filing-grade evidence.
  (Same endpoint with `countries=AT`, `CH`, `GB`, `FR`.)
- **sec.gov:** if you fetch from sec.gov use the User-Agent `Merit Capital Research erik@meritcapit.al`
  and at most 5 requests per second. Never put any other e-mail address or personal detail in a
  request header, URL or form, on any site.
- Do not fetch from web.archive.org (it is rate-limited machine-wide today). Use the capture URLs
  the pack prints as citations without loading them.

## What to find per row

1. **Earlybird's ENTRY round**: the round in which an Earlybird fund first put money in.
   - Give the date (month if known), the round as the record names it (Pre-Seed, Seed, Series A,
     Series B...), the amount, the lead, and a citation URL that names that round AND ties
     Earlybird to it.
   - Read the firm's own posts and press releases first. A firm post announcing a round Earlybird
     LED may be a follow-on; it states the entry only where the post says so in words.
   - A press "Series A" can skip a seed the firm led earlier. Check whether Earlybird was already
     in an earlier round.
   - The firm's "Invested" year is a close year, not an announcement date.
   - For a company that went public, the IPO prospectus (EDGAR S-1 / F-1, or the home exchange)
     lists every preferred series with dates and holders.
   - For the 1999 to 2008 companies the round is often only in the firm's own press release, the
     company's history page, German press (Handelsblatt, manager magazin, heise, golem,
     deutsche-startups.de, VentureCapital Magazin) or Wikipedia. If nothing names it, say `null`.
   - If nothing names Earlybird's round, say `null`. Never guess, never infer from the amount.
2. **All funding rounds you can see**, as a list:
   `{"date", "round", "amount_usd", "amount_native", "lead", "firm_in_round", "source", "source_type": "firm|company|press|filing|vendor"}`.
   Convert EUR, GBP, CHF or SEK only approximately in `amount_usd`; the pipeline re-converts.
3. **For a Seed or Pre-Seed entry: the next round.**
   - A later round the record NAMES as Series A or later, with date and citation, graduates the row.
   - An unnamed later round counts only with its amount.
   - If you find no later round, say so and list what you searched: the firm posts, the exact
     Google News queries, the company site.
4. **Status now**: `private`, `acquired` (acquirer, date, citation), `public` (exchange, ticker)
   or `defunct` (shutdown, liquidation or insolvency, with citation).
   - An insolvency followed by an asset sale is `acquired` (note the successor).
   - An insolvency with no sale yet is `defunct`.
   - Earlybird selling its stake to another investor is NOT the company being acquired.
   - An acqui-hire that does not buy the company leaves the company `defunct` if it shut down.
   - IPO'd and later acquired is `acquired`.
5. **Valuation**: only a priced round, a signed acquisition price or a market cap stating a figure
   of $1B or more. Otherwise `below_1b`. Vendor estimates (PitchBook, Dealroom, Tracxn,
   CB Insights, GetLatka, Crunchbase profile pages) are never a source. For a public company give
   the market cap, its date and the page you read it from (stockanalysis.com,
   companiesmarketcap.com, the exchange).
6. **HQ**: city (the municipality, English name, no state or country suffix) and ISO country
   code. Current HQ; last known for dead or acquired companies.
7. **Focus**: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security,
   Fintech & Payments, Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio,
   Consumer & Marketplaces, Media, Gaming & Advertising; or null if none fits.
   Healthcare SaaS is Healthcare & Bio. Security wins when security is what the company sells.
   AI & Applied AI means AI is the product. Chips and hardware are Industrial & Robotics.
8. **Membership red flags.** Say so in `membership_flag` when you find any of these:
   - `sale_consideration`: Earlybird holds (or held) the company only because it bought or merged
     with a company Earlybird had backed (name both, with the citation);
   - `pre_fund`: the position was a partner's own or previous-firm investment and no Earlybird
     fund is named in any round (the archive's "Pre-Fund Investments" label);
   - `digital_east`: the investing entity was Earlybird Digital East (the Istanbul and CEE fund,
     now Bek Ventures) and not an Earlybird fund of the Berlin and Munich firm;
   - `post_ipo`: the position first appears after the company listed;
   - `not_found`: you cannot find any record that Earlybird invested at all.
   Otherwise `null`.

## Rules

- Re-fetch every URL you cite and confirm the page states what you claim. A citation you did not
  load is worse than none. (Exception: the capture URLs the pack prints.)
- A vendor page may guide you and may appear in `rounds` with `source_type: vendor`, but is never
  the citation for a stage, graduation, status or figure. Crunchbase News and TechCrunch articles
  are press and are fine.
- A paywalled page proves what its visible headline or snippet names.
- Keep quotes under 25 words, copied from the page.
- Work row by row and write the output file after every few rows, so nothing is lost.

## Output: one JSON object keyed by slug

```
"<slug>": {
  "name": "...",
  "entry": {"date": "YYYY-MM", "round": "Seed", "amount": "EUR 1.5M", "lead": "...",
            "citation": "url", "quote": "...", "earlybird_named": true,
            "entry_asserted": "how the source shows this was Earlybird's FIRST round"} | null,
  "rounds": [...],
  "graduation": {"later_round": "Series A", "date": "YYYY-MM", "amount": "...", "citation": "url", "quote": "..."}
              | {"none_found": true, "searched": ["firm: ...", "googlenews: <query> -> <what it showed>", "company: <url> -> ..."]}
              | null (not a Seed or Pre-Seed entry, or the entry is unknown),
  "status": "private|acquired|public|defunct", "status_detail": "...", "status_citation": "url", "status_date": "YYYY-MM",
  "valuation": {"range": "below_1b|1b_plus|10b_plus|100b_plus", "usd": null, "native": null, "citation": null, "asof": null, "basis": "..."},
  "hq_city": "...", "hq_country": "DE",
  "focus": "...",
  "membership_flag": null, "membership_detail": null,
  "confidence": "high|medium|low",
  "notes": "one or two sentences: what the company does and anything the judge must know"
}
```

End your final message with one line per row: slug, entry round and year, status, and any membership flag.
