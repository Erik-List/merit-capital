# Stage pass brief: rows whose entry round is not on record. PRO-100 NEA

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only
`judgments-<TAG>a.py` and `judgments-<TAG>b.py` (via `jl.write("<TAG>a", ...)` / `jl.write("<TAG>b", ...)`), one per
half of your rows. Never touch git, scripts/, config, identity-merges, decisions or other investors. Read
`judge_lib.py`, `JUDGE-BRIEF.md` (the classification contract, entry_stage section) and COLLECTION.md s6
`### entry_stage` (`../../../COLLECTION.md`, from that heading to `### seed_to_a_graduation`). Notes plain prose, no
em-dashes. Set `NQ_TAG=<TAG>` on every nq.py and judgments run. Keep scratch files under `scratchpad/<TAG>/` only.

## Your rows
`queue/<TAG>.json` lists them (`slugs`), highest priority first: $1B+ rows, then public rows, then the rest, newest
first. `python3 show.py <slugs>` prints each row's evidence. Every row is a member whose `entry_stage` is
`undetermined` or empty.

## The task (COLLECTION.md s6, PRO-143: research the funding history, and persist it)
For each row, find the round in which an NEA fund FIRST invested, and record what you found:
- `rounds=[jl.rnd(date, round, amount_usd, lead, firm_in_round, source, source_type)]`: every round you found, with
  `firm_in_round` true/false/None, `source_type` firm | company | press | filing | vendor. An empty list means the
  search ran and found none: record it anyway (`rounds=[]`), with a note naming the surfaces searched.
- Where a non-vendor source NAMES the round and ties NEA to it (or the IPO prospectus's certain-transactions or
  principal-stockholder section shows the preferred series NEA bought and its date), write `stage` (Pre-Seed | Seed |
  Series A | Growth; B and later, crossover and secondaries are Growth), `stage_src="web_verified"` (or
  `"first_party"` for the firm's own post, `"model"` at medium for a documented round you can name from several
  sources), `stage_cite`, `stage_conf`, `entry_date`. An announcement names the round NEA led, which may be a
  follow-on: look for an earlier NEA round before calling it the entry. A press-named round replaces the firm's own
  label only once the firm's posts and archive show nothing earlier.
- The firm's own stage word on its pages (`Early`, lowercase `early`/`seed`/`growth` in the archive) and its
  first-invested year are anchors: they bound the entry and date it, they never name the round alone (`Seed` and
  `Growth` from the live CMS may stand at medium, cited with `SITE(slug)`, only where nothing documents the round).
- Where no source gives the round, leave `stage="undetermined"` (no source keys) and still record `rounds`.

Best sources by era: for a company that went public, its IPO prospectus on EDGAR ("Certain Relationships and Related
Transactions", "Principal Stockholders", "Description of Capital Stock": `FTS("<registrant>", "S-1")` or the row's
`edgar_links`, read with `python3 secget.py "<url>" --grep "Series|New Enterprise"`); for 2000s private rounds, press
wire releases via `NQ_TAG=<TAG> python3 nq.py <slug> '"Company" New Enterprise Associates Series'`; for recent rows,
the firm's own posts (`POST()`), the company's release, then press. Seed entries: leave graduation for the graduation
pass unless a cited later round is already in hand (then `graduated` with its citation), or the entry is after
2024-09-30 (`censored`).

Budget: about 3 tool calls per row, at most 4 WebSearch calls in total. Run each judgments file once. Report: rows
staged by source, rows left undetermined, and any row that is not what the base says it is.
