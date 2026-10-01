# A/B pass brief (COLLECTION.md s7, s8 standing duties). PRO-99 Kleiner Perkins

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch/`. Write only
`judgments-<TAG>.py` (via `jl.write("<TAG>", ...)`, recording after every ~20 rows as `<TAG>a`, `<TAG>b`, ...). Never
touch git, scripts/, config, identity-merges, decisions or other investors. Read `judge_lib.py`, `JUDGE-BRIEF.md` (the
classification contract and the run notes), `../documentation/decisions.md` (D1-D7, X1, R1-R7) and COLLECTION.md s6
`### valuation` and s7 (`../../../COLLECTION.md`). Set `NQ_TAG=<TAG>` on nq.py and judgments runs; scratch under
`scratchpad/<TAG>/`. Emit classification lines with only the keys that change (plus flags and a one-sentence note); a
membership problem gets a verdict line with its citation. Notes plain prose, no em-dashes. `python3 show.py <slug>`
prints the row, its evidence and sibling rows; the merged stored values are in `../companies/classification.json`
(over `../companies/resolved.json`).

Google News (`nq.py`) is shared by the agents of this pass; use it for targeted queries, and prefer WebFetch of a
company's own newsroom, TechCrunch (`https://techcrunch.com/?s=<name>`), Crunchbase News, or an SEC filing.
Market caps: `curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
https://stockanalysis.com/stocks/<ticker>/market-cap/` carries the sentence "... has a market cap or net worth of $X
billion as of <date>"; non-US listings: `https://stockanalysis.com/quote/<exchange>/<ticker>/market-cap/` or
companiesmarketcap.com, converted with `python3 ../../../../scripts/fx-convert.py <amount> <CCY> <date>` (the note
keeps the helper's line). Public $1B+ rows: `valuation_source="web_verified"`, the cap URL as citation, asof the date
on the page.

## ab1a / ab1b: the private $1B+ rows (`queue/ab1.json`, first half / second half)
Pass A, defend: every private $1B+ row carries a priced event (round, tender, signed acquisition price) with a
citable non-vendor figure and date (Rule A: vendor estimates never band). Re-pin any mark resting on the unicorn list
or a vendor to the round's own announcement; a mark before 2024-09-30 keeps `stale`. Pass B, attack: search for the
newer round, the acquisition (closing flips status to acquired; a signed but unclosed deal is a mark), the down round
or tender, the shutdown. Rule 4 (s8 duty 1): every $1B+ row needs class 1 or 2 stage evidence (a cited round naming
Kleiner Perkins, the firm's own post, the Form D structure); try once to cite the round the firm ENTERED (record
`rounds=[rnd(...)]`); failing that add the flag `cite_pending`. Membership checks while there: `zume` (only a vendor
lists KP in the 2017 round; Bing Gordon on the board while at KP: find a citable source or rule not_member),
`cognition` (the firm's 2026 Growth entry: its own round, or stock from Cognition's 2025 purchase of Windsurf,
which KP backed as Codeium? If sale consideration only, not_member with Windsurf named), `persona` (R7: Braswell's
prior-firm deal? find whether a KP fund is in any round), `spacex` (status: private or listed? cite).

## ab2: the momentum slice (`queue/ab2.json`) and duty 6
Every private row first seen since 2021 in AI, fintech, data infrastructure or dev tools gets one mechanical check
for a $1B+ priced round. Record the outcome on the row either way: `extra={"valuation_range_source": "web_verified"}`
with the citation of the round found, or a note "Checked 2026-09-30 for a priced round at $1B or more: none found
(<surface>)" with the band kept below_1b. Then duty 6: re-intersect the unicorn list with loose names
(`../../../shared/unicorns/wikipedia.json`, current and former; strip .io/.ai/.com, "Labs", "HQ", "Technologies")
against every member row of this base (all members, not only your list), and settle each hit (banded, exited, a
different company).

## ab3: the public rows (`queue/ab3.json`)
`caps.json` holds a 2026-09-30 cap for 59 of them (from stockanalysis). Emit the cap line for each priced public row
whose stored value differs (usd, `val_src="web_verified"`, `val_cite`=the caps.json url, `asof`, the band from the
cap). For the 33 unpriced in `caps.json` (skip the skip-list duplicates and `xdx-inc`): find the ticker (Square is
XYZ, IDEC is Biogen BIIB, Symantec is Gen Digital GEN, Flextronics FLEX, Microchip MCHP, Synaptics SYNA, Quantum QMCO,
ChargePoint CHPT, NeuroPace NPCE, Applied Materials AMAT, JD.com JD, Groupon GRPN, Rong360 is Jianpu JT) or the
non-US listing (Kingnet, Sungrow, Venustech, ChineseAll on Shenzhen/Shanghai; GenScript, Arrail Dental, Kindstar on
HKEX; Aleees on TPEx; MapmyIndia and Info Edge (Naukri) on NSE; Truecaller on Nasdaq Stockholm) and price it. A
company no longer listed gets its real status (acquired, delisted and operating = private, defunct) with a citation.
Membership checks: `applied-materials` (listed since 1972: a KP venture round before the IPO, or T3 not_member),
`naukri` (Info Edge: a pre-IPO KP round, or a post-IPO purchase or joint vehicle: T3/R3), `dmx-technologies` (listed
in Singapore before KPCB China bought in? T3). Duties 4, 5 and 8: a stale float that was acquired or re-listed; a float
older than 12 months on a company that has since died; a cap or float from a namesake.

WebSearch: at most 12 calls per agent. Report: rows changed and why (one line each), rows flagged cite_pending or
stale, membership changes, anything that contradicts a sibling book.
