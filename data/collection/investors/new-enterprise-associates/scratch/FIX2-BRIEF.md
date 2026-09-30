# Fix brief F5: membership checks raised by the stage pass. PRO-100 NEA

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only
`judgments-f5.py` (via `jl.write("f5", ...)`), run it ONCE. Never touch git, scripts/, config, identity-merges,
decisions or other investors. Read `judge_lib.py` and `../documentation/decisions.md` (T3/T4 derivations, D8, X1, R1,
R5, R6) first. Verdict lines with citations you read; a kept member whose stored classification is wrong gets a
classification line with only the keys that change. Notes plain prose, no em-dashes. `NQ_TAG=f5`; scratch under
`scratchpad/f5/`. WebSearch: at most 4 calls. `python3 show.py <slug>` for each row's evidence; SEC documents through
`python3 secget.py "<url>" --grep "..."`.

Rows and the question:
- heliogen-inc: its only EDGAR evidence is Forms 3/4 filed by Krishna Kolluri and NeoTribe Ventures, his firm after
  NEA. Is any NEA entity on any filing, or on the firm's own list? If not, `not_member` (T4: a person's seat at his
  next firm).
- satsuma-pharmaceuticals-inc, neurometrix-inc: did NEA's money go only into the listed company (X1)? Satsuma listed
  Sept 2019 (NEA's 2021 private placement); NeuroMetrix listed 2004 (NEA 12's 2009 placement). `not_member` under X1
  unless an earlier private NEA round is shown.
- dura-pharmaceuticals: was NEA's 1993 purchase into the already listed company (X1)?
- premier-laser-systems-inc: the same X1 question.
- pcorder: its IPO prospectus shows no NEA holding and Peter Barris as a director; is the stake NEA's (any NEA entity
  on any pcOrder filing) or its parent Trilogy's? If no NEA fund held pcOrder, `not_member`.
- amisys-managed-care: Greylock, NEA VI and ABS bought it from AIG in 1994. R1: a control acquisition by the
  co-investor group is `not_member` with `extra={"exclusion": "control_position"}`; a minority financing is a member.
- tempest-therapeutics: NEA's Millendo stock carried through the 2021 reverse merger in which private Tempest merged
  into listed Millendo (renamed Tempest). Legacy Tempest's holders include no NEA fund. The Battery reading for such a
  reverse merger: the listed shell is `acquired` (millendo row) and the stock NEA holds afterwards is merger stock, not
  an investment in Tempest: `not_member` (D8). Confirm from the merger filing and write it.

Report one line per row: the facts, the verdict, the citation.
