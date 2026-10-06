# A/B pass brief (COLLECTION.md s7, s8 standing duties). PRO-80 Bessemer Venture Partners

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/` (cd there
for every command). Write only `judgments-<TAG><letter>.py` (via `jl.write("<TAG>a", ...)`, recording after every
~20 rows as `<TAG>a`, `<TAG>b`, ...). Never touch git, scripts/, config, identity-merges, decisions or other
investors. Read `judge_lib.py` (whole), `JUDGE-BRIEF.md` (the hard limits, the classification contract, the run
notes), `../documentation/decisions.md` (D1 to D10, X1, R1 to R8) and COLLECTION.md s6 `### valuation`,
`### status` and `### entry_stage`, and s7 (`grep -n "^### status\|^### valuation\|^### entry_stage\|^### seed_to_a\|^## 7. \|^## 8. " ../../../COLLECTION.md`
gives the line ranges). Set `NQ_TAG=<TAG>` on every nq.py and judgments run; scratch under `scratchpad/<TAG>/`.
Emit classification lines with only the keys that change (plus flags and a one-sentence note); a membership problem
gets a verdict line with its citation. Notes are plain prose, no em-dashes. `python3 show.py --list <your queue
file>` prints each row with what is stored now, its evidence and its sibling rows. Never record the same file twice
after it succeeded.

Sources: Google News through `nq.py` is shared by the agents of this pass; use it for targeted queries, and prefer
WebFetch of a company's own newsroom, TechCrunch (`https://techcrunch.com/?s=<name>`), Crunchbase News, or an SEC
filing (`python3 secget.py <url>`). Market caps: `curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
AppleWebKit/537.36 Chrome/128.0 Safari/537.36" https://stockanalysis.com/stocks/<ticker>/market-cap/` carries the
sentence "... has a market cap or net worth of $X billion as of <date>"; non-US listings:
`https://stockanalysis.com/quote/<exchange>/<ticker>/market-cap/` or companiesmarketcap.com, converted with
`python3 ../../../../scripts/fx-convert.py <amount> <CCY> <date>` (the note keeps the helper's line). Public $1B+
rows: `val_src="web_verified"`, the cap URL as `val_cite`, `asof` the date on the page.

## Private rows at $1B or more (`queue/ab-priv-1.json`, `queue/ab-priv-2.json`)
Pass A, defend: every private $1B+ row carries a priced event (round, tender, signed acquisition price) with a
citable non-vendor figure and date (Rule A: vendor estimates and the unicorn list never band a row). Re-pin any
mark resting on `unicorn_list`, a sibling book or a vendor to the round's own announcement (`val_src="web_verified"`,
`val_cite`, `asof`, `extra={"valuation_range_source": "web_verified"}`); a mark before 2024-10-01 keeps or gains
the flag `stale`. Pass B, attack: search for the newer round, the acquisition (closing flips status to acquired and
the band to below_1b; a signed but unclosed deal is a mark), the down round or tender, the shutdown. Rule 4 (s8
duty 1): every $1B+ row needs class 1 or 2 stage evidence (a cited round naming Bessemer, the firm's own post or
memo, the Form D structure); try once to cite the round the firm ENTERED (record `rounds=[rnd(...)]`, and
`stage`, `stage_src`, `stage_cite`, `entry_date` where it decides the stage); failing that add the flag
`cite_pending`. Where a sibling book holds a different mark for the same company, settle on the freshest cited
figure and say in the note what the sibling should read (the lead aligns the sibling).

## The public rows (`queue/ab-public.json`)
Price every row: the ticker, the cap, the date (emit usd, `val_src="web_verified"`, `val_cite`, `asof`, the band
from the cap, also for rows under $1B). A company no longer listed gets its real status (acquired with acquirer
and year in the note, delisted and operating = private, bankrupt = defunct) with a citation and band below_1b.
Duties 4, 5 and 8: a stale float on a company since acquired or re-listed; a float older than 12 months on a
company that has since died; a cap or float taken from a namesake (the prefilled `valuation_usd` comes from an SEC
public-float join on the name: check that the registrant is this company). Membership checks while there: a row
that was already listed when Bessemer first bought in, with no private round before the listing, is `not_member`
(T3 / R3) with the listing date and the entry date cited.

## The momentum slice (`queue/ab-momentum.json`) and duty 6
Every private row first seen since 2021 in AI, fintech, data infrastructure or dev tools gets one mechanical check
for a $1B+ priced round. Record the outcome on the row either way: the band with its citation, or a note "Checked
2026-10-06 for a priced round at $1B or more: none found (<surface>)" with the band kept below_1b. Skip rows whose
stored note already records such a check with a date. Then duty 6: re-intersect the unicorn list with loose names
(`../../../shared/unicorns/wikipedia.json`, current and former; strip .io/.ai/.com, "Labs", "HQ", "Technologies")
against every member row of this base (members are the slugs with verdict `member` in
`../companies/membership-ledger.json` under "bessemer-venture-partners" -> "verdicts"), and settle each hit (banded,
exited, or a different company).

WebSearch: at most the number of calls your task names. Report in under 250 words: rows changed and why (one line
each for the important ones), rows flagged cite_pending or stale, membership changes, sibling books that need
aligning (book, slug, what it should read, the citation), anything that contradicts the base.
