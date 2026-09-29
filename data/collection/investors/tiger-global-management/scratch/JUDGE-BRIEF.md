# Judge brief: PRO-167 Tiger Global, queue batches

You judge the rows of ONE queue batch of the Tiger Global company base: membership where it is still open, then
every open classification column of each member, written as a Python judgments file that records itself. Work only
inside `/Users/erik/Developer/merit-capital/data/collection/investors/tiger-global-management/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<N>.py` (and let it write its `queue/batch-<N>.out.jsonl` through `jl.write`).
- Set `NQ_TAG=b<N>` in EVERY shell command that runs `nq.py` or your judgments file (e.g. `NQ_TAG=b7 python3 nq.py ...`,
  `NQ_TAG=b7 python3 judgments-7.py`). Other judges run in parallel; the tag keeps your news caches separate.
- WebSearch: at most 8 calls in total, only for $1B+ or public rows the other tools leave open. Prefer, in order:
  `bq.py` (Bing News RSS: `NQ_TAG=bN python3 bq.py <slug> '"Company" valuation'`; its own throttle, and every item
  carries the publisher URL, so `NEWS(slug, "<title substring>")` cites it with no decode), `nq.py` (Google News:
  slower, shared machine-wide, capped at two of this run's processes), `wikifetch.py` (Wikipedia plain text), and
  WebFetch of a company's own page, an SEC filing or a press page. Ask each surface only what the row needs.
- Never type a citation URL by hand. Use the helpers in `judge_lib.py` (`NEWS`, `W`, `SEC`), or a URL printed by a tool
  you ran (the row's evidence view prints its citations). A helper refuses a missing or ambiguous match.
- Notes are plain prose. Never use em-dashes (use commas, semicolons, parentheses). Say "inferred", never "prior";
  "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. This file.
2. `judge_lib.py` (line builders `verdict`, `cls`, `rnd`, `write`; citation helpers `NEWS`, `W`, `SEC`, `FORMD_ROUNDS`,
   `FORMD_CITE`, `GRADLINES`).
3. `../documentation/decisions.md` (D1 to D12, X1, X2 and the run-time rulings R1...).
4. `../../../COLLECTION.md` section 6 "Classification columns" and section 1 (tests T1 to T5, evidence rules).
   Skim; come back when a row raises a question.

## Your rows
`python3 show.py --batch <N>` prints each row: its `need` list, what is already `known` (prefilled by the
deterministic layers; do not repeat a known value unless you dispute it with evidence), and the evidence view:
`press` (the recall addition's headline, the publisher page's own sentence naming Tiger, the citation URL, and the
other headlines that name the company with Tiger), `sec` (prospectus or merger-filing sentences naming a Tiger
vehicle, with the vehicle and desk), `edgar` (Tiger's own 13D/G or Form 3/4 on the company), `13f` (the first and
last quarter Tiger's 13F lists it, which dates a listing), `formd` (a roster person on the company's Form D, role and
year), `wiki` (Wikipedia sentences naming Tiger), `param` (a model-memory recall line: a LEAD, never evidence), and
`sib` (sibling investors' rows for the same company).

## Membership (when `membership` is in `need`)
The membership test (COLLECTION.md 1): a fund of the firm put money into the company through a private round.
- **Press** (`ec="web"`): a headline or the publisher's sentence saying Tiger Global led, co-led, participated in,
  invested in or backed a round of the company, or bought into it while private. High when the sentence names the
  round; medium when it says only "backed by" or "investors include". Cite the publisher URL from the evidence view.
- **SEC filing** (`ec="fund_filing"`): a prospectus holder table, investors' rights agreement signatory list or merger
  filing naming a Tiger vehicle as a holder while the company was private. Cite the filing URL shown. Where every named
  vehicle is a public-desk fund (Tiger Global, L.P./Ltd., Tiger Global Investments, Long Opportunities, Crossover,
  Tiger Veda) and none is a PIP vehicle, say so in the basis and add the flag `boundary`: delta X1 moves such a row to
  the other desk.
- **Site** (`ec="site_listing"`): the firm's own "Our Story" page (18 names) is evidence of a position, not of a
  private round (D4). Keep the row a member only where a private round is on record (cite it in the classification
  note as the entry); a company Tiger only ever bought as listed stock (the likely case for Mercado Libre) is
  `not_member` with the page cited, and the basis says "X2" so the report can list it for Erik.
- **13G / 13D / Form 3/4 / 13F only** (`edgar`, `13f`): a listed-company holding is NOT membership (D3, T3). Such a row
  is a member only when a private round naming Tiger is on record (an S-1 holder table, a press round, a pre-IPO
  Form D seat); otherwise `not_member`, `ec="fund_filing"`, basis "13G/13F position in a listed company, no private
  round naming the firm (T3, D3)". A Form 3/4 filed at the IPO by Tiger as a 10% holder is itself strong evidence of a
  pre-IPO position: confirm the private round and cite it.
- **Form D name-match** (`formd`): never enough alone. A roster person as director of the issuer inside their Tiger
  window plus a documented Tiger round, or a resolved company with the director seat and no contrary evidence
  (director-of-record pattern: `member`, `formd_adjudicated`, medium). Seats outside the window are not the firm's
  (D7): Lee Fixel from 2019 on is Addition (Chainalysis, Kaskada, Stedi, Relay Payments, NoHo Dental, Built, Harry's
  seat after 2019 unless Tiger's own round is on record); John Curtius from mid-2022 is Cedar; homonyms (the New York
  Life officer Alexander Cook, Evan Feinberg the Genesis Therapeutics founder, Eric Lane's Goldman funds) are
  `not_member` with the address or role as the basis.
- **Sale consideration** (a Tiger holding in an ACQUIRER received for a portfolio company it bought) is `not_member`,
  naming the acquired company (COLLECTION.md 1). **PIPE shares bought at a SPAC merger or in the IPO** are not a
  venture entry (D6, Coatue R1): `not_member`, flag `boundary`.
- **Control positions** (COLLECTION.md 1, T3 addendum): where Tiger alone or with its co-investors bought control of
  the company (a whole-company purchase, a majority stake, a buyout), the row is `not_member` with
  `exclusion="control_position"` in `verdict(...)`, basis naming the transaction. Tiger made several such purchases in
  2007 to 2012: AlloCiné (owned 2007 to 2013), jobs.ch (sold to Ringier 2012), Cobone.com (bought 2011), Take2 /
  Takealot (bought with Kim Reid 2010), AlexandAlexa.com (controlling stake 2011). Check each against the record; a
  minority round into the same company later is judged on its own facts.
- A `param` line alone is never evidence. Where a row rests only on it and `nq.py` finds no headline tying Tiger to
  the company, it is `not_member` ("no record ties the firm to a round").
- `uncertain` only when identification is genuinely open after corroboration was tried.
A member needs TWO lines: `verdict(...)` and `cls(...)`.

## Recall rows: membership already seeded, confirm it
Most rows entered as recall additions from the press, the SEC full-text and the Wikipedia layers (the row's `RECALL:`
line quotes the evidence and its URL). Where that evidence was verified at selection (a filing naming a PIP vehicle, a
headline naming Tiger Global and the company with an investment word, a Wikipedia sentence), the ledger already holds a
`member` seed (who `seed-recall-pro167`) with that citation, and `membership` is not in `need`. Read the `RECALL:` line
anyway: if it does not show a PRIVATE-round investment by Tiger in THIS company (a listed-stock purchase, a different
company with the same name, a headline about a rival), emit a verdict line that replaces the seed. Rows whose evidence
is only an article sentence ("D") or a public-desk filing (X1) have `membership` in `need` as usual.

## Seeded rows: re-rule membership even when `membership` is not in `need`
`prepare` auto-seeds `member` (who `seed-evidence`) for every row with a site listing (`ec=listed`) or an EDGAR
ownership filing (`ec=filing`). For Tiger neither is enough on its own (D3, D4): the filing is usually the adviser's
13G on a LISTED company, and the "Our Story" page can name public positions. So for EVERY row in your batch whose
`ec` is `listed` or `filing`, emit a verdict line anyway: `member` with the private round's citation (the prospectus
holder table or IRA signatory in `sec`, a press round, a pre-IPO Form D seat) as `ec="fund_filing"` or `"web"`, or
`not_member` under T3 with the basis "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
(`ec="fund_filing"`, cite the filing). A seeded verdict is an agent-level seed, so your verdict replaces it.

## The classification contract (COLLECTION.md 6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take `rng="below_1b"`
  and no usd. IPO then acquired reads acquired; a shutdown reads defunct; an asset sale out of insolvency reads
  acquired; a bankruptcy with no sale yet reads defunct. A signed, unclosed acquisition keeps the row private at the
  agreed price.
- `valuation_range`: below_1b | 1b_plus | 10b_plus | 100b_plus. A band from 1b_plus up needs `usd`,
  `val_src="web_verified"`, `val_cite`, `asof` and `extra={"valuation_range_source": "web_verified"}`. Rule A:
  vendor estimates (PitchBook, CB Insights, Tracxn, Venture Intelligence, Crunchbase profiles) never band a row; a
  headline or release reporting a priced round at a stated valuation does. Public companies: market capitalisation
  with citation and as-of (companiesmarketcap.com or stockanalysis.com pages are fine; a non-USD cap converts at the
  ECB rate of its date with `python3 ../../../../scripts/fx-convert.py`, and the note keeps the native figure). A
  private mark older than 24 months (asof before 2024-09-29) carries the flag `stale`. Tiger's 2021 book is full of
  marks that later collapsed: a documented down round, a tender far below, a fire sale or a shutdown moves the row
  (COLLECTION.md 6, collapse evidence). Private rows first seen 2021 or later in AI, fintech, data infrastructure or
  developer tools get one check for a newer $1B+ priced round (momentum slice); write the outcome in the note.
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined (Series B and later, secondaries and pre-IPO
  rounds read Growth; "Late Stage" is Growth, D12). The round is the one in which Tiger FIRST put fund money in, which
  for Tiger is often the round the headline names ("led the $50M Series C"); check the company's earlier rounds before
  reading a later round as the entry. Sources: `web_verified` (a citation naming the round and Tiger's part in it),
  `formd_structural` / `formd_band` (prefilled; dispute only with a documented round, flag `stage_disputes_band`),
  `model` (a named deal in the note, high/medium). When the round cannot be named, `stage="undetermined"`.
  Record the funding history you found in `rounds=[rnd(...)]` whenever you research a round (COLLECTION.md 6, PRO-143).
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided, read off the entry round's citation.
- `seed_to_a_graduation` only for Seed entries: `graduated` needs a cited later round (`grad_src` web_verified or
  first_party, `grad_cite`, `entry_date`); `censored` when the entry is after 2024-09-29; otherwise leave it for the
  graduation pass (note "Graduation left for the graduation pass."). Never write `not_graduated` in the grind.
- `hq_country`: ISO alpha-2; a non-US country needs `country_src="web_verified"` and `country_cite` (the press page
  that places the company, or its Wikipedia article via `W`). Many rows are Indian, Chinese, Brazilian, Israeli,
  European or Southeast Asian: place the operating company where its head office is (a Delaware or Cayman parent of
  an Indian business is IN, with the note).
- `hq_country_claim` (in an item's need or known): prepare asks the country where a one-word name carries a non-US
  Wikidata country; those joins are often wrong (Square read JP, Uber read NL). Answer from the company's own evidence.
- `hq_city`: bare municipality, spelled as the other books spell it (rule 10 compares them): "Bangalore" (not
  Bengaluru), "Gurugram", "New Delhi", "Mumbai", "Noida", "Tel Aviv", "São Paulo", "Bogotá", "Mexico City", "Beijing",
  "Shanghai", "Singapore", "Jakarta", "Lagos", "Dubai". `city_src` model_knowledge (default), formd_address or
  web_verified. Unplaceable: omit and add flag `city_unknown`. Current HQ for live companies, last known for dead or acquired.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising (edtech is Consumer & Marketplaces unless it sells software to schools, then SaaS;
  chips are Industrial & Robotics; networking and storage are Data Infrastructure). Null only if it fits none.
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib`, rule 10): the same company at another investor must agree on status, valuation band and mark,
  country and city unless you hold fresher cited evidence (say so in the note). A sibling that is plainly a different
  company with the same name is a collision: do not align; list it in your report.

## Finish
1. `NQ_TAG=bN python3 judgments-N.py` must print `recorded ...`. On `REJECTED`, fix and re-run.
2. Report back in under 250 words: rows judged (members / not_member / uncertain), verdicts worth a second look,
   sibling name collisions, rows left `unknown` or `undetermined` that a later pass could settle, X1 rows (public-desk
   vehicle only), WebSearch calls used, and anything that looked wrong in the base (two rows that are one company:
   name both slugs).

## Delta after the rebuild (read this if your batch is a delta batch)
- **Wave-2 recall additions** (about 50 rows: the row's `RECALL:` line) were reviewed one by one by the run lead before they
  were written: their sentence names Tiger Global investing in THIS company. Rule them `member`, `ec="web"`, confidence
  high when the sentence names a round Tiger led or joined, medium when it only lists Tiger among backers; cite the URL in
  the `RECALL:` line. Rule `not_member` only if the row's own evidence shows a listed-stock purchase or another company.
- **elong-inc**: eLong's 2004 F-1 names Tiger Technology Private Investment Partners (PIP I) as an investor and selling
  shareholder: `member`, `ec="fund_filing"`, cite the F-1 (the `sec` line); the entry is Tiger's pre-IPO round.
- **decolar-com-inc, satylca-s-c-a**: Despegar group entities; the group is out as a control position (Tiger held 57.3%
  before the 2017 IPO): `not_member` with `exclusion="control_position"`, same basis.
- **apollo-group-inc, teacher-synergy-llc** already carry not_member verdicts; nothing to do.
- Seed rows needing S2A: decide `graduated` (cited later round), `censored` (entry after 2024-09-29) or `not_graduated`
  with the full absence test (`GRADLINES(slug)` gives the surface lines from graduation-surfaces.json; add a web line
  per COLLECTION.md 6 and Coatue R5: one web search per no).
