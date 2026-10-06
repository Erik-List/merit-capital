# Judge brief: PRO-80 Bessemer Venture Partners, membership and classification batches

You judge the queue items you are given for the Bessemer Venture Partners ("BVP") company base: membership where
it is open, then every open classification column for the members. You write a Python judgments file and record
it. Work only inside
`/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<TAG>.py` (it writes `queue/<TAG>.out.jsonl` through `jl.write`).
- **The machine's disk is nearly full.** Do not download large files, do not save pages to disk beyond the helpers'
  own small caches, and never write a file with `open(path, "w")` over an existing shared file.
- Set `NQ_TAG=<TAG>` in EVERY shell command that runs `nq.py` or your judgments file (e.g.
  `NQ_TAG=j3 python3 nq.py ...`, `NQ_TAG=j3 python3 judgments-j3.py`). Other judges run in parallel; the tag keeps
  your news caches separate.
- WebSearch: at most the number of calls your task names (the session shares one budget of 200). Prefer `nq.py`
  (Google News, uncapped, throttled machine-wide), `wikifetch.py` (Wikipedia plain text), `secget.py <sec url>`
  (an SEC document through the shared throttle; never call sec.gov with a bare curl) and WebFetch of a company's
  own site or a press page. `curl` works for stockanalysis.com market caps
  (`https://stockanalysis.com/stocks/<ticker>/market-cap/`, send a browser User-Agent).
- Never type a citation URL by hand except an SEC URL copied from the row's own `formd_links`/`edgar_links` in
  `../companies/base.json` or a URL printed by a tool you ran. Use the helpers (they refuse a missing or ambiguous
  match). A URL you found with WebFetch/WebSearch may be cited after you read the page and it says what you cite.
- Notes are plain prose, one or two sentences. Never use em-dashes (use commas, semicolons, parentheses). Say
  "inferred", never "prior"; "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. This file.
2. `judge_lib.py` (the whole file: `cls`, `verdict`, `rnd`, `write`, and the citation helpers `SITE`, `ARCH`, `POST`,
   `W`, `FTS`, `NEWS`, `GNEWS`, `FORMD_ROUNDS`, `FORMD_CITE`).
3. `../documentation/decisions.md` (D1 to D10, delta X1, and the run-time rulings: the boundary).
4. `../../../COLLECTION.md` section 6 "Classification columns" (from the line `## 6. Classification columns` to
   `## 7.`). Skim; return when a row raises a question.

## Your rows
`python3 show.py --batch <N>` (or `python3 show.py <slug> ...`) prints each item: `need` (the columns still open,
`membership` first when the row is unjudged), `known` (prefilled by the deterministic layers: do not repeat a known
value unless you dispute it with evidence), and the evidence:
- `site`: the live bvp.com row. `invest_year` is the firm's own "Partnered" year, `partners` the Bessemer people on
  the deal, `status_site` the CMS status (active / public / acquired; it is stale for many rows, so check it).
  **`stage_site` is a migration default ("seed" on 500 of 534 rows) and is never a label or a citation** (D9).
- `archive`: the archived bvp.com listings (2008 to 2026): `invest_year` and `invest_date` are the firm's own
  investment year and date (**an `invest_date` of January 1 is a bare year**, not a date), `exit_year`, the deal
  `partners`, `listed as` (the firm's rendering, with "(acq. by X)", "(fka Y)" or a ticker), and `about`,
  `about (older)` and `top exits`: the firm's own descriptions, which often say which round Bessemer entered
  ("BVP led the Series A in 1997", "participated in the seed and subsequent rounds", "invested in the second round
  in April 1988", "first institutional round"). That sentence is first-party evidence for the entry stage: cite it
  with `ARCH(slug)` (the capture that first carried the row).
- `Bessemer vehicle filings` / `edgar`: 13D/G and Forms 3/4 filed by Bessemer funds (filing-grade membership).
- `post`: the firm's own memos (`[memo]`: its investment recommendation at the time, published years later; the
  strongest entry-stage source there is), news and Atlas posts, with round sentences. Cite with `POST("memos/shopify")`
  or `POST("<slug fragment>")`.
- `fts`: EDGAR full-text hits whose registrant is the company (S-1 holder tables naming Bessemer funds).
- `formd partners`: a roster person on the company's Form D, with dates. `wiki`: Wikipedia sentences. `sib`: sibling
  books' rows for the same company.

## Membership (items whose `need` starts with `membership`)
The firm's own listing in any era suffices (COLLECTION.md s1): a row with `site` or `archive` evidence is a member
unless one of the exclusions below applies. A filing by a Bessemer vehicle (Bessemer Venture Partners I to XIII,
Bessec Ventures, Deer <numeral> & Co., 15 Angels, BVP VII Special Opportunity Fund, the Century and India funds)
suffices. A Form D on which a roster person is a related person is a NAME MATCH and never suffices alone: it needs
affirmative corroboration (the firm's listing, a Bessemer vehicle on a filing, a press or company source naming
Bessemer in a round). Judge name-match rows cluster-first: resolve the person once (their Bessemer years are the
window shown; their prior and next firms; their operator jobs), then every row that person explains.

The boundary, from decisions.md (cite the ruling in the basis):
- **D2 BVP Forge.** Forge is the same adviser's buyout strategy (majority or significant-minority deals from 2022).
  A company only a BVP Forge fund holds is `not_member`, basis "BVP Forge position: the adviser's buyout strategy,
  other desk (decisions.md D2)". Forge deals so far include Medisolv, Radformation, Technical Toolboxes, Mortgage
  Automator, Sunwave Health, BetterRx, Nevvon, Parsec, Vector, Givebutter, Supplier.io, StayTerra. A company the
  venture funds backed first stays a member on that entry.
- **D3 namesakes.** Bessemer Trust, Bessemer Securities, Bessemer Investment Management, the Old Westbury funds and
  Lindsay Goldberg & Bessemer are other businesses. A position only they hold is `not_member` (T1, external).
- **D5 control and public purchases.** A position that first appears as a public-market purchase (a 13G on a company
  already listed, a PIPE into a listed company) is `not_member` (T3) unless a Bessemer fund held a venture round
  before the listing. BVP India bought into listed Indian companies in 2006 to 2010 (PIPEs and open-market stakes:
  the archived list shows names such as Motilal Oswal, Shriram EPC, Sunil Hitech, Anant Raj, Ganesh Housing,
  Orient Green Power, IL&FS Transportation): check each for a pre-IPO Bessemer round; a pre-IPO round is a member
  (Growth), a purchase of an already listed company is `not_member` under T3 even though the firm listed it. A
  transaction in which Bessemer (alone or with its group) took control, or financed a management buyout (the firm's
  own Medi Assist memo: "to finance the management buyout"), is `not_member` under the control addendum, cited.
- **Sale consideration.** A listed company known mainly as the ACQUIRER of a portfolio company (a listing rendered
  "X (acq. by Y)" is fine: X is the row; but a row that IS the acquirer, held because it bought a Bessemer company)
  is `not_member`, basis naming the acquired company (Erik 2026-09-22). Name that acquired company in your report.
- **Fund-shaped entries (D7).** Another manager's fund, an accelerator or a holding vehicle on the firm's list
  (e.g. "New Vernon Capital", "KCM Biomedical ... invested in biotech companies") is `not_member` until identified
  as an operating company.
- **Seats travel (D6).** Date every seat against the person's Bessemer window. After they left: Sarah Tavel
  (Pinterest 2012, Greylock 2015, Benchmark 2017), Kristina Shen (a16z 2019), Ethan Kurzweil (Chemistry 2024),
  Sunil Nagaraj (Ubiquity 2017), Trevor Oelschig (General Catalyst 2016), Philippe Botteri (Accel 2011), Justin
  Label (Inovia), Devesh Garg, Rob Chandra (Avid Park 2013), Umesh Padval (Thomvest 2016), Matt Salzberg (Blue
  Apron founder), Peter Lee, Mackey Craven (OpenView), Anna Khan (CRV), Josh Harder (Congress). Common names on the
  roster are homonym traps: **Vishal Gupta, Jeff Epstein, Peter Lee, Scott Smith, Chris Wu, Li Sun, Nitin Gupta,
  Michael Segal, Andrew Walsh, Ben Donald, John Drake, Grace Ma, Sachin Jain, Alyssa Lee, Karen Lee, Sam Bondy**. A
  Form D naming one of them is the firm's only where the issuer is on the firm's own list or deal-partner map, or
  the record ties the round to Bessemer. Operating partners (Jeff Epstein, Chini Krishnan, Nate Fick, Umesh Padval,
  Aran Ron, Scott Smith) hold many seats of their own: without a Bessemer fund in the company, `not_member`.
- **X1 pre-1981 (provisional IN).** A company the firm's own list carries with an investment year before 1981 is a
  member; add the flag `pre_spinout` to its classification line. A holding evidenced only by Bessemer Securities'
  name is `not_member`.
- **Anti-portfolio (D10).** Apple, Apollo Computer, Check Point, StrataCom, eBay, FedEx, Google, Ikanos, Intel,
  Intuit, Lotus, Compaq, PayPal, Facebook, Kayak, Tesla, Yammer, Airbnb, Atlassian, Snapchat, Okta, Zoom, Coinbase,
  Instacart: the firm says it passed on them. If one appears as a row, `not_member`, basis "the firm's own
  anti-portfolio (decisions.md D10)", unless you find a cited Bessemer round (then say so in your report).
- `not_member`: a homonym, a seat held outside the person's Bessemer years, a personal angel check or an operating
  partner's own seat, a fund or SPV, a public-market purchase with no earlier private round (T3), sale
  consideration, a control position, Forge-only. Missing corroboration on a name match is `not_member`, not
  `uncertain`.
- `uncertain` only when identification is genuinely open or the evidence conflicts after you tried.
A `not_member` row gets its verdict line and nothing else. A member gets the verdict line AND a classification line
(two separate lines; `record` routes by the presence of `verdict`). Evidence class for the verdict: `site_listing`
(live or archived listing; cite `SITE(slug)` or `ARCH(slug)`), `fund_filing` (a Bessemer vehicle's filing; cite the
SEC URL from the row), `formd_adjudicated` (a corroborated Form D seat), `web` (a cited press or company source).

## The classification contract (COLLECTION.md section 6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take
  `rng="below_1b"` and no usd. An asset sale out of insolvency reads acquired with a successor note; a bankruptcy
  with no sale yet reads defunct; a shutdown reads defunct; a merger into another company reads acquired; an
  acqui-hire decides nothing (the company's own fate does). The archive's "(acq. by X)" and exit year are the
  firm's own record of an exit: use them (and name the acquirer and year in the note: "acq. by X, YEAR"), but a
  company that went public and was later bought reads acquired. For old exits (1970s to 1990s IPOs) find what
  became of the company: most were later acquired or failed; only a company still listed reads public.
- `valuation_range`: below_1b | 1b_plus | 10b_plus (usd >= $10B) | 100b_plus (>= $100B). Any band from 1b_plus up
  needs `usd`, `val_src="web_verified"`, `val_cite`, `asof` (YYYY-MM or YYYY-MM-DD) and
  `extra={"valuation_range_source": "web_verified"}`. Rule A: vendor estimates (PitchBook, Crunchbase "estimated",
  Tracxn, GetLatka, Sacra, Forge) never band a row; it takes a priced round, tender, listing or signed acquisition
  price with a citable figure. A mark older than 24 months (asof before 2024-10-01) carries the flag `stale`. Public
  companies: market cap with a citation and asof. Non-USD figures convert with
  `python3 ../../../../scripts/fx-convert.py <amount> <CCY> <date>` and the note keeps the helper's line.
  **Momentum slice**: every private row first seen in 2021 or later in AI, fintech, data infrastructure or dev
  tools gets one mechanical check for a $1B+ priced round (one `nq.py` query is enough); write the check's outcome
  and date in the note either way.
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined. Series B and later read Growth; secondaries,
  tenders and crossover rounds read Growth. **Research the round the firm FIRST entered and record what you find
  in `rounds=[rnd(...)]`** (COLLECTION.md s6, PRO-143), `source_type` one of firm | company | press | filing |
  vendor (vendor pages may be listed, never cited). Sources, strongest first:
  - `first_party` with `stage_cite`: the firm's own memo (`POST("memos/<slug>")`), its own news post saying which
    round it entered, or the archived listing's own sentence naming the round (`ARCH(slug)`: "BVP led the Series A
    in 1997", "seeded by BVP's Felda Hardymon", "invested in the company's second round"). Read the sentence
    literally: "first institutional round" or "first round" with no size is Series A for a company of the 1980s to
    2000s only where the sentence or the record calls it that; "seed" and "seeded" read Seed; "second round",
    "Series B", "expansion round", "later-stage" read Growth; "early rounds", "participated in its financing" name
    no round (then `undetermined`, or another source).
  - `web_verified` with `stage_cite`: a cited round naming Bessemer or BVP (press, the company, or an S-1's
    certain-transactions / principal-stockholders table listing the preferred series the Bessemer funds bought,
    via `FTS()`), read by you.
  - `formd_structural` / `formd_band` (prefilled; dispute only with a documented round, adding
    `stage_disputes_band`).
  - `model`: a documented round you can name without a page in hand (confidence medium), e.g. "led the 2011
    Series A"; say which round in the note.
  **An announcement names the round the firm led, which is often a follow-on; it asserts the entry only where it
  says so.** The Century funds (2019 on) enter at Growth unless the venture funds were in earlier. When the round
  cannot be named, `stage="undetermined"` (no source keys) and still record the rounds you found (an empty list
  means you searched and found none). Do not guess from the investment year or the check size.
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided; it may be given with undetermined. Read
  it off the round's own citation; where none dates it more precisely, the firm's own `invest_date` (when it is not
  a January 1 placeholder) or `invest_year` (archive first, then `site.invest_year`) is the entry date. Never off
  `first_seen`.
- `seed_to_a_graduation` only for Seed entries. Write `graduated` only with a cited later priced round (`grad_src`
  first_party or web_verified, `grad_cite`, `grad_conf`, and the round in `rounds=[rnd(...)]`); a later round the
  record names Series A or later graduates whatever the amounts. Write `censored` when the entry is after
  2024-10-01. Otherwise leave it for the graduation pass (say "Graduation left for the graduation pass." in the
  note). Never write `not_graduated`.
- `hq_country`: ISO alpha-2. A non-US country needs `country_src="web_verified"` and `country_cite` (the firm's own
  listing is a fine citation where its geography or description places the company: `ARCH(slug)` or `SITE(slug)`).
  Prefilled countries from Wikidata are often wrong joins on one-word names: dispute with evidence (flag
  `model_disputes_source`). An item carrying `hq_country_claim` asks you to confirm or replace a Wikidata country.
  `site.regions` (us / india / israel / europe) is the desk, a strong hint, not the HQ.
- `hq_city`: the bare municipality ("San Francisco", never "San Francisco, CA"; Brooklyn is New York; Cambridge MA
  is Cambridge; Bengaluru is "Bangalore"); `city_src` is `model_knowledge` (default), `formd_address` or
  `web_verified`. If no source places the company, omit it and add the flag `city_unknown`.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising. Give it on every row you classify; a company that fits none (a retailer is
  Consumer & Marketplaces; a paper mill, a bank, a hotel chain, an insurer, a homebuilder fit none) takes
  `extra={"focus": None}` and the note says "outside the focus taxonomy". Chips and hardware are Industrial &
  Robotics; telecom equipment, networking and enterprise infrastructure are Data Infrastructure; healthcare
  vertical software and biotech are Healthcare & Bio; cleantech is Climate & Energy.
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib`, rule 10): the same company in another book must agree on status, band and mark, country and
  city unless you hold fresher cited evidence (then say so in the note). A `sib` line that is plainly a different
  company with the same name is a name collision: do not align, and list it in your report.
- A company that cannot be named at all: flag `identity_unresolved`, and `stage`, `rng` all `undetermined`.

## Finish
1. `NQ_TAG=<TAG> python3 judgments-<TAG>.py` must print `recorded ... ` lines. On `REJECTED`, fix and re-run the
   whole file (record merges idempotently; never record the same file twice after it succeeded, notes would be
   replaced). Read record's whole output. Split your work into two or three files (`<TAG>a`, `<TAG>b`, ...) of at
   most 25 rows each and record each when it is done, so an interruption loses little.
2. Report back in under 250 words: verdicts by kind, rows classified, name collisions with siblings, rows left
   `unknown`/`undetermined` that a later pass could settle, acquired companies named by sale-consideration rows,
   WebSearch calls used, anything wrong in the base (two rows that are one company: name both slugs; a renamed
   company; an anti-portfolio or Forge company that surfaced).

## Run notes (2026-10-01)
- The alumni's next firms, the Forge deal list and the listed-company names above are leads written from memory,
  not evidence: use them to know where to look, and cite only what you verify.
- The old book is real and well described: the archived list reaches back to 1957 with the firm's own investment
  year and a sentence per company for the exits. Most pre-2000 rows are exits (IPO or sale); many names are
  obscure. Use the archive's own description first, then Wikipedia (`wikifetch.py`), then one `nq.py` query. An
  old company you cannot trace after that reads `status="unknown"` with a specific note, never a guess.
- WebSearch: at most 6 calls per judge (the session shares 200). Tag your files with your TAG
  (judgments-<TAG>.py, queue/<TAG>.out.jsonl) and keep any scratch under `scratchpad/<TAG>/`.
