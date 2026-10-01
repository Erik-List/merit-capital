# Judge brief: PRO-99 Kleiner Perkins, membership and classification batches

You judge the queue items you are given for the Kleiner Perkins company base (the firm was Kleiner Perkins
Caufield & Byers, "KPCB", until 2019): membership where it is open, then every open classification column for
the members. You write a Python judgments file and record it. Work only inside
`/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch/`.

## Hard limits
- Never touch git (no add/commit/stash/checkout). Never edit `scripts/`, `COLLECTION.md`, `cross-investor.json`,
  `config.json`, `identity-merges.json`, `decisions.md`, or any other investor's directory. Write only your own
  `judgments-<TAG>.py` (it writes `queue/<TAG>.out.jsonl` through `jl.write`).
- Set `NQ_TAG=<TAG>` in EVERY shell command that runs `nq.py` or your judgments file (e.g.
  `NQ_TAG=j3 python3 nq.py ...`, `NQ_TAG=j3 python3 judgments-j3.py`). Other judges run in parallel; the tag keeps
  your news caches separate.
- WebSearch: at most the number of calls your task names (the session shares one budget of 200). Prefer `nq.py`
  (Google News, uncapped, throttled machine-wide), `wikifetch.py` (Wikipedia plain text) and WebFetch of a company's
  own site, a press page or an SEC filing. `curl` works for stockanalysis.com market caps
  (`https://stockanalysis.com/stocks/<ticker>/market-cap/`) and for SEC filings (send a User-Agent header).
- Never type a citation URL by hand except an SEC URL copied from the row's own `formd_links`/`edgar_links` in
  `../companies/base.json` or a URL printed by a tool you ran. Use the helpers (they refuse a missing or ambiguous
  match). A URL you found with WebFetch/WebSearch may be cited after you read the page and it says what you cite.
- Notes are plain prose, one or two sentences. Never use em-dashes (use commas, semicolons, parentheses). Say
  "inferred", never "prior"; "rule", never "invariant"; "S2A", never "C2A".

## Read first
1. This file.
2. `judge_lib.py` (the whole file: `cls`, `verdict`, `rnd`, `write`, and the citation helpers `SITE`, `ARCH`, `POST`,
   `W`, `FTS`, `NEWS`, `GNEWS`, `FORMD_ROUNDS`, `FORMD_CITE`).
3. `../documentation/decisions.md` (D1 to D7, delta X1, and the run-time rulings: the boundary).
4. `../../../COLLECTION.md` section 6 "Classification columns" (from the line `## 6. Classification columns` to
   `## 7.`). Skim; return when a row raises a question.

## Your rows
`python3 show.py --batch <N>` (or `python3 show.py <slug> ...`) prints each item: `need` (the columns still open,
`membership` first when the row is unjudged), `known` (prefilled by the deterministic layers: do not repeat a known
value unless you dispute it with evidence), the live CMS row (`site`: the firm's own first-investment stage `Early`
or `Growth`, its since-year, `Current` or `Prior`, the company's current stage and the acquirer on exits), the
archived kpcb.com listings (`archive`: years, the 2008-11 list views such as `public` or `china`, the 2012-17
company pages' Teams (China / Digital / Greentech / Life Sciences), Initiative (Digital Growth Fund, sFund, iFund,
Pandemic), the partners named on the deal, the status by year), the firm's vehicles' own SEC filings, the firm's
posts naming the company, EDGAR full-text hits (S-1 holder tables naming Kleiner Perkins entities), Form D partner
matches with their filing dates, Wikipedia sentences, and sibling books' rows (`sib`).

## Membership (items whose `need` starts with `membership`)
The firm's own listing in any era suffices (COLLECTION.md s1). A filing by a Kleiner Perkins vehicle (13D/G, Form
3/4 by the fund, an S-1 holder table naming "Kleiner Perkins Caufield & Byers" or "KPCB" funds) suffices. A Form D
on which a roster person is a related person is a NAME MATCH and never suffices alone: it needs affirmative
corroboration (the firm's listing, a KP vehicle on a filing, a press or company source naming Kleiner Perkins in a
round). Judge name-match rows cluster-first: resolve the person once (their KP years in the item's
`partners_formd` window, their prior and next firms), then every row that person explains.

The boundary, from decisions.md (cite the ruling in the basis):
- **D2 Bond.** A position held by a KPCB Digital Growth Fund is IN whenever taken. A company only Bond's own funds
  (Bond Capital Fund, Bond II, Bond III) backed is `not_member` (T1, external). From September 2018 a Bond partner
  (Mary Meeker, Mood Rowghani, Noah Knauf, Juliet de Baubigny, Daegwon Chae, Paul Vronsky) on a Form D locates
  Bond, not Kleiner Perkins.
- **X1 KPCB China (provisional IN).** A company KPCB China's funds held is a member on the firm's own listing (the
  China listing, the 2012-17 pages under Teams "China", the 2018-24 logo grid): add the flag `kpcb_china` to its
  classification line so the class can be counted (and removed in one step if Erik rules it out). **Except Tina
  Ju's pre-2007 TDF Capital deals** the China listing carried (Alibaba, Baidu, China Netcom, Focus Media, Hurray!,
  CGEN Digital Media, P-Cube): `not_member`, basis "partner-carried: Tina Ju's TDF Capital deal before KPCB China
  (Erik 2026-09-17 partner-carried rule; decisions.md X1)", unless you find a KPCB China fund's own round. China
  Creation Ventures' own later investments are external.
- **Sale consideration.** A listed company known mainly as the ACQUIRER of a portfolio company (archived page
  status "Merged" with an acquirer's name, e.g. "Alcatel", "Citrix", "Oracle") is `not_member`, basis naming the
  acquired company the firm backed (Erik 2026-09-22). Name that acquired company in your report so it can be
  added as its own row.
- **Seats travel (D5).** Vinod Khosla from 2004 is Khosla Ventures; Kevin Compton and Doug Mackenzie from about
  2006 are Radar Partners; Ted Schlein from 2022 also runs Ballistic Ventures; Aileen Lee from 2012 is Cowboy
  Ventures; Chi-Hua Chien from 2014 is Goodwater; Trae Vassallo from 2015 is Defy; Beth Seidenberg from 2018 is
  Westlake Village BioPartners; Joe Lacob and Randy Komisar kept seats from their KP years. Date every seat.
- **Not rows:** SPAC shells and a sponsor promote (Thayer Ventures Acquisition Corp and the like: T3/T5), another
  manager's fund, partners' personal angel checks, KP Fellows companies with no fund check.
- `not_member`: a homonym, a seat held outside the person's KP years, a personal angel check, a fund or SPV, a
  public-market purchase with no earlier private round (T3), sale consideration, Bond-only, KPCB China-only (X1).
  Missing corroboration on a name match is `not_member`, not `uncertain`.
- `uncertain` only when identification is genuinely open or the evidence conflicts after you tried.
A `not_member` row gets its verdict line and nothing else. A member gets the verdict line AND a classification line
(two separate lines; `record` routes by the presence of `verdict`).

## The classification contract (COLLECTION.md section 6 decides; this is the short form)
- `status`: private | public | acquired | defunct | unknown. Acquired, defunct and unknown rows take
  `rng="below_1b"` and no usd. An asset sale out of insolvency reads acquired with a successor note; a bankruptcy
  with no sale yet reads defunct; a shutdown reads defunct; a merger into another company reads acquired; an
  acqui-hire decides nothing (the company's own fate does). The firm's exit fields corroborate but go stale.
- `valuation_range`: below_1b | 1b_plus | 10b_plus (usd >= $10B) | 100b_plus (>= $100B). Any band from 1b_plus up
  needs `usd`, `val_src="web_verified"`, `val_cite`, `asof` (YYYY-MM or YYYY-MM-DD) and
  `extra={"valuation_range_source": "web_verified"}`. Rule A: vendor estimates (PitchBook, Crunchbase "estimated",
  Tracxn, GetLatka, Sacra, Forge) never band a row; it takes a priced round, tender, listing or signed acquisition
  price with a citable figure. A mark older than 24 months (asof before 2024-09-30) carries the flag `stale`. Public
  companies: market cap with a citation and asof. **Momentum slice**: every private row first seen in 2021 or later
  in AI, fintech, data infrastructure or dev tools gets one mechanical check for a $1B+ priced round (one `nq.py`
  query is enough); write the check's outcome and date in the note either way.
- `entry_stage`: Pre-Seed | Seed | Series A | Growth | undetermined. Series B and later read Growth; secondaries,
  tenders and crossover rounds read Growth. **Research the round the firm FIRST entered and record what you find
  in `rounds=[rnd(...)]`** (COLLECTION.md s6, PRO-143), `source_type` one of firm | company | press | filing |
  vendor (vendor pages may be listed, never cited). Sources, strongest first: `web_verified` (a cited round naming
  Kleiner Perkins or KPCB, or an S-1's certain-transactions / principal-stockholders table listing the preferred
  series the KP funds bought, via `FTS()`), `first_party` (the firm's own post saying which round it entered, cited
  with `POST()`), `formd_structural` / `formd_band` (prefilled; dispute only with a documented round, adding
  `stage_disputes_band`), `model` (a documented round you can name, confidence medium). **The site's `stage_site`
  is not a label in this run**: `Early` straddles Seed and Series A (an anchor only), and `Growth` is being scored
  against the rounds you cite; you may mention it in the note, never cite it as the source. **An announcement
  names the round the firm led, which is often a follow-on; it asserts the entry only where it says so.** A
  Digital Growth Fund or Green Growth Fund position (2008-2018 initiative on the archived page) is usually a
  Series B or later entry, but cite the round. When the round cannot be named, `stage="undetermined"` (no source
  keys) and still record the rounds you found (an empty list means you searched and found none).
- `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD) whenever the stage is decided; it may be given with undetermined. Read
  it off the round's own citation; where none dates it more precisely, the firm's own since-year
  (`site.invest_year`) is the entry year. Never off `first_seen`.
- `seed_to_a_graduation` only for Seed entries. Write `graduated` only with a cited later priced round (`grad_src`
  first_party or web_verified, `grad_cite`, `grad_conf`, and the round in `rounds=[rnd(...)]`); a later round the
  record names Series A or later graduates whatever the amounts. Write `censored` when the entry is after
  2024-09-30. Otherwise leave it for the graduation pass (say "Graduation left for the graduation pass." in the
  note). Never write `not_graduated`.
- `hq_country`: ISO alpha-2. A non-US country needs `country_src="web_verified"` and `country_cite`. Prefilled
  countries from Wikidata are often wrong joins on one-word names: dispute with evidence (flag
  `model_disputes_source`). An item carrying `hq_country_claim` asks you to confirm or replace a Wikidata country.
- `hq_city`: the bare municipality ("San Francisco", never "San Francisco, CA"; Brooklyn is New York; Cambridge MA
  is Cambridge); `city_src` is `model_knowledge` (default), `formd_address` or `web_verified`. The 2008-11 listing's
  `location` is the company's city then. If no source places the company, omit it and add the flag `city_unknown`.
- `focus`: one of AI & Applied AI, Data Infrastructure, DevTools & APIs, SaaS, Security, Fintech & Payments,
  Crypto & Web3, Industrial & Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
  Media, Gaming & Advertising. Give it on every row you classify. Chips and hardware are Industrial & Robotics;
  enterprise infrastructure and networking are Data Infrastructure; healthcare vertical software is Healthcare & Bio;
  greentech (solar, fuel cells, biofuels, batteries, efficiency) is Climate & Energy.
- Emit only the keys the row needs, plus deliberate disputes (then add `model_disputes_source` or
  `stage_disputes_band` and explain in the note).
- Siblings (`sib`, rule 10): the same company in another book must agree on status, band and mark, country and
  city unless you hold fresher cited evidence (then say so in the note). A `sib` line that is plainly a different
  company with the same name is a name collision: do not align, and list it in your report.
- A company that cannot be named at all: flag `identity_unresolved`, and `stage`, `rng` all `undetermined`.

## Finish
1. `NQ_TAG=<TAG> python3 judgments-<TAG>.py` must print `recorded ... ` lines. On `REJECTED`, fix and re-run the
   whole file (record merges idempotently; never record the same file twice after it succeeded, notes would be
   replaced). Read record's whole output.
2. Report back in under 250 words: verdicts by kind, rows classified, name collisions with siblings, rows left
   `unknown`/`undetermined` that a later pass could settle, acquired companies named by sale-consideration rows,
   WebSearch calls used, anything wrong in the base (two rows that are one company: name both slugs; a renamed
   company).

## Run notes (2026-09-30)
- **Skip these slugs entirely** (duplicates the one rebuild merges into their canonical; emit nothing for them):
  `atara-bio`, `3-v-biosciences`, `glori-oil`, `at-home-corp`, `entremed-inc`, `360buy`, `alphabet-google`,
  `homestore-com-inc`, `delta-technology-holdings-ltd`. Judge the canonical rows (`atara-biotherapeutics`,
  `sagimet-biosciences`, `glori-energy`, `home-network`, `casi`, `jd-com`, `google`, `move-com`,
  `jiangsu-yangtze-river-delta-fine-chemical`) with the duplicate's evidence in mind. `excite-home` (the firm's
  "Excite@Home" row, website excite.com, 1995) is Excite, a separate investment from @Home Network.
- **Membership traps** (config `verify.not_members`; rule them `not_member` with this basis): `alcatel` (sale
  consideration: the investment was TiMetra Networks, bought by Alcatel in 2003); `alibaba`, `baidu`, `china-netcom`,
  `focus-media`, `hurray`, `cgen-digital-media-acquired-by-focus-media`, `p-cube` (Tina Ju's TDF-era deals,
  partner-carried, X1); `thayer-ventures-acquisition-corp` (a SPAC shell, T5). `casi` is a post-listing purchase
  by KPCB China Fund II into EntreMed/CASI (listed since 1996): `not_member` under T3 unless you find a pre-IPO
  Kleiner Perkins round in EntreMed.
- Rulings R1 to R6 in decisions.md (bios are name matches; a shareholder representative is a person; co-owned
  joint vehicles and partners' family offices are not fund money; the member is the company the fund held; a
  person's Section 16 filing naming a KP fund as holder of record corroborates the fund).
- `site.acquirer` holds the acquirer on exits and the ticker on IPOs (e.g. "TWTR"); `site.timing` Prior means the
  firm no longer holds it; `site.current_stage` is the company's stage now, never the entry.
- WebSearch: at most 6 calls per judge (the session shares 200). Tag your files with your TAG (judgments-<TAG>.py,
  queue/<TAG>.out.jsonl) and keep any scratch under `scratchpad/<TAG>/`.
