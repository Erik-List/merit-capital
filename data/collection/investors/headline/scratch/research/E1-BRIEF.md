# E1 research brief: Headline's Asia and Brazil desk rows

Erik ruled on 2026-09-28 that Headline's two regional desks count as part of the
firm: the **Asia desk** (Infinity Venture Partners / Infinity Ventures, "IVP",
renamed **Headline Asia** in May 2021; also BV Capital Fund IV (Asia)) and the
**Brazil desk** (**Redpoint eventures** / Redpoint e.ventures / "RPev", 2012 on,
now **Headline Brazil**, incl. Headline XP). You research one packet of their
companies and write one JSON file. You judge from the public web; you do not
edit any project file except your output.

## Tools and limits

- Google News headlines (no search budget): from the repo root
  `cd /Users/erik/Developer/merit-capital/data/collection/investors/headline &&
  python3 scratch/news.py '"Company" funding' --name Company --all --decode 4`
  (`--decode N` resolves the first N round/amount headlines to publisher URLs;
  `--pick "words"` decodes a headline containing those words).
- WebFetch for pages; WebSearch at most **20 calls** for your whole packet.
- Never fetch web.archive.org (the Internet Archive has this machine
  firewalled). If you touch sec.gov, send the header
  `User-Agent: Merit Capital research erik@meritcapit.al`, a few requests a second at most.
- Logo-wall rows (`surface: logo_wall`) were researched once already: read
  `scratch/research/recall-1.json` .. `recall-4.json` for their prior notes first.

## What to decide per row

1. **membership**: `member` | `not_member` | `uncertain`, with `basis`, `url`, `quote`.
   - `surface: portfolio` (on the firm's rendered portfolio grid) and
     `logo_wall` (on e.ventures' own logo wall): member by the firm's own
     listing unless the evidence shows a namesake; just confirm identity.
   - `surface: cms_hidden` (a hidden doc in the firm's CMS) and `team_page`
     (only on one investor's portfolio list): need a corroborating source
     (press, company, the firm's own post, a filing) that names the desk
     (any name above, or e.ventures / Headline) as an investor.
     A company the partner founded, or backed personally or at a previous firm
     before joining the desk, is `not_member` (partner-carried deal).
     No source either way: `uncertain`, and say what you searched.
2. **status** as of September 2026: `private` | `public` | `acquired` |
   `defunct` | `unknown`, with `status_url` and `status_quote`. IPO'd then
   acquired → acquired. Insolvency or shutdown followed by an asset sale →
   acquired. A plain shutdown → defunct. An acqui-hire never decides status
   (defunct if shut down, private if operating). Give `acquirer` and `exit_date`.
3. **valuation**: `below_1b` | `1b_plus` | `10b_plus`. A $1B+ band needs a cited
   priced round or a market cap at that level; vendor estimates (Tracxn,
   PitchBook, CB Insights, Crunchbase) never band a row. Public rows: current
   market cap with as-of date and currency, from a quote page. Acquired,
   defunct, unknown: no figure (band below_1b). Give `valuation_usd`
   (native amount and currency too), `valuation_asof`, `valuation_url`.
4. **entry**: the round in which the desk FIRST invested, as a source names
   it: `round` (as stated, e.g. "Series A", "シリーズA", "rodada seed",
   "Pre-Series A", "Angel"), `date`, `amount`, `currency`, `lead`, `url`,
   `quote`. Then `entry_stage` in the taxonomy: `Pre-Seed` | `Seed` |
   `Series A` | `Growth` (Series B or later) | `undetermined` (no source names
   the round the desk entered in; the CMS "Early 2015" gives a year, not a
   stage). Do not infer a letter from sequence without saying so in `note`.
5. **rounds**: every round you find, as
   `{date, round, amount, currency, lead, firm_in_round (true/false/null), url, quote, source_type (firm|company|press|filing)}`.
6. **graduation** (only when `entry_stage` is Seed or Pre-Seed): did the
   company later raise a named Series A or larger priced round?
   `graduated` (with the round, url, quote) | `none_found` (entry 24+ months
   ago and no later round found; list what you searched) | `censored` (entry
   under 24 months ago).
7. **hq_country** (ISO alpha-2) and **hq_city** (bare municipality in English,
   e.g. "Taipei", "Tokyo", "São Paulo", "Florianópolis"), current HQ for live
   companies, last known for dead or acquired; `hq_url`.
8. **focus**: one of AI & Applied AI, Data Infrastructure, DevTools & APIs,
   SaaS, Security, Fintech & Payments, Crypto & Web3, Industrial & Robotics,
   Climate & Energy, Healthcare & Bio, Consumer & Marketplaces,
   Media, Gaming & Advertising.
9. **note**: one or two plain sentences a reviewer can check (what the company
   is, how the desk came in, the exit). No dashes as punctuation.

## Output

Write a JSON list (one object per packet row, same `slug`) to the output path
you were given, with keys: `slug, name, membership{verdict,basis,url,quote},
status, status_url, status_quote, acquirer, exit_date, valuation_range,
valuation_usd, valuation_native, valuation_currency, valuation_asof,
valuation_url, entry{round,date,amount,currency,lead,url,quote}, entry_stage,
rounds[], graduation{status,round,date,url,quote}, hq_country, hq_city,
hq_url, focus, confidence (high|medium|low), note`. Use null where unknown.
Every URL must be one you actually loaded or decoded. Reply with a short table
(slug, membership, status, band, entry_stage, country/city) and your WebSearch count.
