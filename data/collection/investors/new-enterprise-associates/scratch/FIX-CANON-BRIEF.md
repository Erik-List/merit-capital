# Fix brief F3: canonical-row corrections and the status pass. PRO-100 NEA

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only
`judgments-f3a.py` (corrections, `jl.write("f3a", ...)`) and `judgments-f3b.py` (status pass, `jl.write("f3b", ...)`).
Never touch git, scripts/, config, identity-merges, decisions or other investors. Read `judge_lib.py`,
`JUDGE-BRIEF.md` (the classification contract) and `../documentation/decisions.md` first. Emit classification lines
only (no verdicts), and only the keys that change, each with its citation and a one-sentence note. Notes plain
prose, no em-dashes.

## Part A: corrections other judges found on canonical rows (verify each, then record)
- the-wing: entry NEA's Series A, 2017-04 (not the band's Growth).
- lot18: entry NEA's Series B, 2011-05 (Growth; not the band's Series A).
- fusion-io: entry NEA's Series A, 2008-03 (Wikipedia; the band read Growth 2011).
- willow: country US, city Mountain View (the GB claim is wrong).
- elements-behavioral-health: acquired, not defunct (BlueMountain bought the assets out of the 2018 bankruptcy;
  bhbusiness.com, 2026-08-20) unless F2 rules it out as control (then skip).
- super: the prefilled defunct/US is a wrong join; NEA's Super is the Indonesian social-commerce company (status,
  valuation band, country ID, city).
- snagfilms: ViewLift (the same issuer) was bought by DAZN, 2026-05: acquired.
- erytech: renamed Phaxiam, liquidated 2025-06: defunct (if still a member after the X1 sweep).
- element3-health: renamed Grouper (2024-01): status per the record.
- exent: the prefilled acquired is unconfirmed: confirm or correct.
- grubwithus: defunct kept unless its stock carried into GOAT (then private at GOAT's mark), cite.
- mode: NEA led the 2017 Series A (the firm's year is 2015: check for an earlier NEA round).

## Part B: status pass
Every member whose status is `unknown` (list: `json.load(open('status-unknown.json'))`, 71 slugs). For each, one
bounded attempt (at most 3 tool calls): the company's own site or its archived copy, `NQ_TAG=f3 python3 nq.py <slug>
'"Company" acquired OR shut down OR bankruptcy'`, a state or national register, Wikipedia. Record `acquired` (note:
"acq. by X, YEAR", cite), `defunct` (cite the shutdown, bankruptcy or dissolution), `private` (cite recent evidence
of operation), or leave `unknown` with a note naming what was searched. Acquired, defunct and unknown rows carry
`rng="below_1b"`.

WebSearch: at most 6 calls in total. Run each judgments file once when complete. Report: counts per status, the
corrections applied, and anything that contradicts another judge.
