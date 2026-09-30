# Fix brief F2: boundary cases (R1 control, D8 sale consideration, R3 incubators). PRO-100 NEA

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only
`judgments-f2.py` (via `jl.write("f2", ...)`). Never touch git, scripts/, config, identity-merges, decisions or other
investors. Read `judge_lib.py`, `../documentation/decisions.md` (D3, D5, D8, R1, R3) and COLLECTION.md s1 T3 "Control
positions" and "Sale consideration is not membership" (`../../../COLLECTION.md`). Notes plain prose, no em-dashes.

## Rows and the question each asks
R1, control (T3 control addendum): did NEA, alone or with its co-investor group, acquire control (50%+ or a
change-of-control transaction, a buyout, a carve-out purchase, a company NEA formed to buy a business)? If so
`not_member` with `extra={"exclusion": "control_position"}` in the verdict line; if NEA took a minority in a
financing, `member` (entry Growth unless the record names another round).
- american-pathology-partners (NEA's $75M founding equity commitment), curana-health (NEA formed it by uniting three
  companies), comprehensive-pharmacy-services (2019 deal), trivascular (2008 buyback from Boston Scientific),
  xcel-pharmaceuticals (2001, Elan products), eci-acquisition-holdings, revspring (NEA beside Frazier's 2024 buyout),
  elements-behavioral-health, paladina-health and marathon-health (the NEAPH Acquisitionco purchase from DaVita,
  2018; everside-health is already not_member on it).

D8, sale consideration: is NEA's stake stock received for selling a portfolio company to this company? If so
`not_member` naming the acquired company (which is the member; say whether it is in `../companies/base.json`). A later
investment of NEA's own money in the acquirer is a separate entry (member).
- 3com-corporation (the firm's year 1996, twelve years after 3Com listed; the firm's 2012 post "The Big Score" names
  "the funding of Bob Metcalfe and 3Com": read it, and 3Com's early financing record, to see whether NEA funded 3Com
  itself), the-spectranetics-corporation (stock from Advanced Interventional Systems' 1994 merger?), pharmos (its 2006
  purchase of Vela Pharmaceuticals), websidestory (its 2006 purchase of Visual Sciences from Avivo, whose investor NEA
  was), letgo (NEA's 2016 stake: a round, or consideration from the Wallapop US combination?), grubwithus (does its
  stock carry into GOAT?), caremark-rx.

R3, incubator vehicles: `not_member` unless a source shows the entity is itself an operating company.
- exploramed-iv, exploramed-v, foundry-therapeutics-1, prospex-medical-iii-inc.

## How
`python3 show.py <slugs>` for the evidence. Filings through `python3 secget.py "<sec url>" --grep "..."`; press
through `NQ_TAG=f2 python3 nq.py <slug> '"Company" query'`; WebFetch for company or press pages. WebSearch: at most 6
calls. Every verdict line carries a citation you read. A kept member whose stored classification is wrong gets a
classification line (only the keys that change). Run `NQ_TAG=f2 python3 judgments-f2.py` once when complete.

Report: one line per row (the transaction, the reading, the verdict), and anything that looks like a new class.
