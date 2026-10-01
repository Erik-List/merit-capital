# Stage and R7 pass brief. PRO-99 Kleiner Perkins

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch/`. Write only
`judgments-<TAG>.py` (via `jl.write("<TAG>", ...)`, recording after every ~20 rows as `<TAG>a`, `<TAG>b`, ...). Never
touch git, scripts/, config, identity-merges, decisions or other investors. Read `judge_lib.py`, `JUDGE-BRIEF.md` (the
classification contract, especially `entry_stage`, and the run notes), `../documentation/decisions.md` (R7 in
particular) and COLLECTION.md s6 `### entry_stage` (`../../../COLLECTION.md`). Set `NQ_TAG=<TAG>`; scratch under
`scratchpad/<TAG>/`. Notes plain prose, no em-dashes.

Your rows are your half of `queue/st.json` (each carries `why`). `python3 show.py <slug>` prints the evidence; the
stored values are in `../companies/classification.json` (over `resolved.json`), including any `funding_rounds` the
first judge found.

For each row:
1. **Find the round Kleiner Perkins FIRST entered, and cite it.** The strongest sources, in order: the firm's own post
   (`POST()`), the company's own announcement, press naming Kleiner Perkins / KPCB in that round, an IPO prospectus
   (principal stockholders / certain transactions tables list the preferred series the KP funds bought: search
   `../sources/edgar/fts-hits.json` via `FTS("<Registrant>", "S-1")` or read the S-1 with `python3 secget.py <url>
   --grep "Kleiner|KPCB|Series"`). Remember: an announcement names the round the firm LED, often a follow-on; the
   entry is the first round the firm was IN. Emit `stage`, `stage_src`, `stage_cite`, `stage_conf`, `entry_date` and
   `rounds=[rnd(...)]` (all rounds you found, `firm_in_round` true where the source names KP). A decided Seed entry
   also needs its graduation per the brief (graduated with a cited later round, censored if after 2024-09-30, else
   say "Graduation left for the graduation pass.").
2. **R7 check** (rows marked "R7 sweep"): if the company's round history is on record and NO round names a Kleiner
   Perkins fund, and a partner who joined the firm AFTER the site's year backed it at a previous firm (Mamoon Hamid:
   Social+Capital, USVP; Ilya Fushman: Index; Leigh Marie Braswell: her previous firm; Josh Coyne, Aditya Naganath,
   Joubin Mirzadegan, Aatish Nayak, Annie Case, Everett Randle, Bucky Moore: check their prior firms), rule it
   `not_member` with basis "partner-carried (R7): <partner> backed it at <firm> in <year>; no round names a Kleiner
   Perkins fund" and the citation you read. Where the record is simply silent, the listing stands: keep the member,
   stage `undetermined`, and record the rounds you found.
3. A $1B+ row ("rule 4") whose entry round you cannot cite keeps its value and gets the flag `cite_pending`.

WebSearch: at most 12 calls per agent. Report: stages cited (count by source), R7 not_members with the partner and
prior firm, rows left cite_pending, anything wrong in the base.
