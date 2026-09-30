# Research brief: Visionaries Club portfolio (PRO-103)

You are researching portfolio companies of **Visionaries Club** (Berlin/London
VC, founded 2019 by Robert Lacher and Sebastian Pollok; brands "Visionaries
Club", "Visionaries" (2026 rebrand) and "Visionaries Tomorrow" / "TOMORROW"
(its deep-tech fund, tomorrow.vc)). Its vehicles, all under one adviser
(Visionaries Club GmbH): Seed Fund I (2020), Growth Fund I (2020, Series B
onwards), Late Growth I–IV (single-company SPVs, 2021–), Seed Fund II and
Growth Fund II (2022), Tomorrow Fund I (2022–), AGI I (2025/26).

Work only from the company list you are given. For each company write ONE
JSON file `data/collection/investors/visionaries-club/scratch/research/<slug>.json`
(absolute root: /Users/erik/Developer/merit-capital). Write nothing else
anywhere in the repository.

## What to establish per company

1. **Identity**: legal/brand name, website, founded year, what it does in one
   line. Flag a homonym if a sibling row (below) is a different company.
2. **Membership**: did a Visionaries fund invest? For companies from the live
   visionaries.vc or tomorrow.vc lists this is already established; for
   `archive-wordpress-*` and `recall-candidate` rows you must find evidence
   that Visionaries Club / Visionaries Tomorrow invested (a round announcement
   naming it, the firm's own post, a register entry given in the row).
   A founder's or partner's PERSONAL angel check is not a fund position.
3. **Visionaries entry round**: the round in which Visionaries FIRST invested:
   date (as precise as the source gives), round name as the record names it
   (pre-seed, seed, Series A, B, ...), amount, lead, and a citation URL that
   names the round AND ties Visionaries to it (press release, the company's own
   post, a news article, visionaries.vc editorial, medium.com/@tomorrow.vc).
   A firm's announcement of a round it LED can be a follow-on: look for an
   earlier Visionaries check before accepting it as the entry. If no source
   ties Visionaries to a specific round, say so (entry = "undetermined") and
   still list the rounds you found.
4. **funding_rounds**: every round you find, one object each:
   `{"date","round","amount","currency","lead","firm_in_round","source","source_type"}`
   with `firm_in_round` true/false/null (null = unknown) and `source_type` one
   of `firm | company | press | filing | vendor`. An empty list means you
   searched and found none.
5. **Status now** (as of 2026-09-30): `private | public | acquired | defunct |
   unknown`, with the event, date and citation for anything other than
   private. An acqui-hire where the company shut down is `defunct`; a sale of
   the business is `acquired`; insolvency followed by an asset sale is
   `acquired` (note it); a bankruptcy/insolvency with no sale is `defunct`.
6. **Latest valuation**: ONLY a priced event with a citable figure: a primary
   round's post-money stated by the company, a filing or the press (a vendor's
   news arm reporting a priced round counts as press), a tender price, or a
   market cap for a listed company. **Never** a vendor estimate (PitchBook,
   Tracxn, Dealroom, Crunchbase profile, CB Insights, Sacra, GetLatka, Forge,
   etc.): put those under `vendor_marks` only. Give figure, currency, date,
   citation. If nothing priced exists, say so.
7. **HQ**: current headquarters city (bare municipality in English, e.g.
   "Munich", "Zurich", "Cologne"; never "Munich, Germany") and ISO 3166-1
   alpha-2 country, with a citation (company imprint/contact page or press).
8. **Focus**: one of exactly: AI & Applied AI, Data Infrastructure, DevTools &
   APIs, SaaS, Security, Fintech & Payments, Crypto & Web3, Industrial &
   Robotics, Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
   Media, Gaming & Advertising. "AI & Applied AI" only when AI is the product.
   Security wins over SaaS when security is what it sells; healthcare vertical
   SaaS is Healthcare & Bio; chips are Industrial & Robotics.
9. **Graduation** (only if the Visionaries entry was pre-seed or seed): the
   first LATER round named Series A or later (or an unnamed later round of at
   least 2x the seed and $5M), with date and a non-vendor citation; or, if none
   found, list what you searched (e.g. "googlenews: <query> -> nothing after
   2023-05") in `graduation_surfaces`.

## Sources and tools

- **Google News (uncapped, use it first)**: from the directory
  `/Users/erik/Developer/merit-capital/data/collection/investors/visionaries-club/scratch`
  run `python3 news.py '"<Company>" Visionaries' --all --decode 4` (also
  try `'"<Company>" raises'`, `'"<Company>" seed'`, `'"<Company>" Series A'`).
  `--decode N` resolves the first N round/amount headlines to the publisher's
  URL; `--pick <substring>` decodes a specific headline.
- **WebFetch** (uncapped) on known pages: eu-startups.com, tech.eu,
  techcrunch.com, sifted.eu, the company's own newsroom/blog, visionaries.vc
  editorial pages, medium.com/@tomorrow.vc, finsmes.com.
- **WebSearch is capped: at most 20 calls for your whole assignment.** Use it
  only when Google News and WebFetch fail.
- Every sibling investor's published row for the same company is given in
  `sibling_rows` (other books this project has already collected). Their
  citations are reusable when they name the round you need; their values must
  agree with yours unless you have a newer or better-cited fact (say which).
- Re-fetch every URL you cite and check that it loads and contains the claim;
  put a short quote (under 15 words) in `quote`.
- Paywalled pages: a headline or snippet naming a round is usable, cite the
  visible surface.

## Output shape

```json
{
  "slug": "...", "name": "...", "website": "...", "founded": 2020,
  "what": "one line",
  "homonym_note": "",
  "membership": {"verdict": "member|not_member|uncertain", "basis": "...", "citation": "...", "quote": "..."},
  "entry": {"date": "2021-03", "round": "Seed", "amount": 5000000, "currency": "EUR",
            "lead": "...", "vehicle_hint": "Seed Fund I|Growth Fund I|Tomorrow|...|unknown",
            "citation": "...", "quote": "...", "confidence": "high|medium|low"},
  "funding_rounds": [ ... ],
  "status": {"value": "private", "event": "", "date": "", "citation": ""},
  "valuation": {"figure": null, "currency": "", "date": "", "kind": "post-money primary|tender|market cap", "citation": "", "quote": ""},
  "vendor_marks": [],
  "hq": {"city": "Berlin", "country": "DE", "citation": "..."},
  "focus": "SaaS",
  "graduation": {"status": "graduated|not_graduated|n/a|open", "round": "", "date": "", "citation": "", "quote": ""},
  "graduation_surfaces": [],
  "notes": "anything the judge must know (renames, acquisitions, partner angel checks, disputes with sibling rows)"
}
```

Be exact and conservative: a claim you cannot cite is left empty with a note,
never guessed. Finish every company on your list; report in your final message
a table of slug -> entry round/date, status, valuation figure, and anything
surprising.
