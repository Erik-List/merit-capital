# Human sampling sheet, base v2 verification (2026-08-13)

Stratified sample of ledger verdicts for spot-checking. For each row: the
verdict, the decisive fact, and what a 2-minute check looks like. Overrides go
into `base-verification.json` with `"who": "erik"` (they outrank agent verdicts
on every rebuild).

## not_member, high-value ejections (the ones that moved buckets)

| slug | was tagged | basis | 2-min check |
|---|---|---|---|
| bilt-technologies-inc | 10b_plus | rounds are Kairos/Wells Fargo/Left Lane; the "Ankur Jain" match is Bilt's own founder | Bilt press releases list investors |
| saronic-technologies-inc | 1b_plus | 8VC/a16z/Caffeinated/Kleiner rounds; "Alex Moore" is 8VC's partner | Saronic Series B press release |
| framer-inc | 1b_plus | Accel A, Atomico B, Meritech C/D; the Lixandru filing is her Accel-era board seat | TechCrunch Series B article |
| epirus-inc | 1b_plus | 8VC/Bedrock/T. Rowe rounds | Epirus press releases |
| uptake-technologies-inc | 1b_plus | NEA/Revolution/GreatPoint/Baillie; acquired by Bosch 2026-03 | Uptake funding history |
| itrust-capital-inc | 1b_plus | the $125M round was Left Lane's | iTrustCapital press release |

## not_member, defect classes (one specimen each)

| slug | class | basis |
|---|---|---|
| quidsi-inc | ex-partner, next firm | Gandhi's Accel era; Accel/Bessemer backed Diapers.com |
| seamicro-inc | ex-partner, next firm | Lamond's Khosla era |
| shape-security-inc | ex-partner, own fund | Garg's Wing era; backers KP/Venrock/Norwest/GV/WING |
| daylight-labs-inc | partner became founder | Amy Sun founded it after Sequoia; a16z backed it |
| tetrascience-inc | full-name homonym | its CEO is the other Patrick Grady |
| canpotex-japan-ltd | not a venture company | potash export JV subsidiary |
| twin-health-inc | decision desk | Sequoia INDIA's deal (Bhatnagar) |
| outside-interactive-inc | Sequoia Heritage | the $150M was Heritage, out per constitution |

## member, recovered from the noise pile (all four)

| slug | basis | citation |
|---|---|---|
| avalanche-technology-inc | Sequoia in the 2010 B and later rounds | sequoiacap.com/companies/avalanche/ |
| cloudshare-ltd | Sequoia in the 2009 B and 2011 round; fka IT Structures (merged) | techcrunch.com 2011-07-05 |
| muze-collective-inc | Sequoia among the 2019-20 seed backers | techcrunch.com 2020-08-25 |
| romotive-inc | Sequoia led the $5M Series A 2012 (Alfred Lin) | documented deal |

## member, seeded on evidence class (spot-check the seeding logic)

| slug | evidence | check |
|---|---|---|
| youtube | wayback listing 2006 | archived sequoiacap.com page |
| fal | current-site listing | sequoiacap.com/companies |
| webvan-group-inc | fund-vehicle SEC filing | EDGAR 13D/G by a Sequoia fund |

## uncertain (1 row, needs your call)

| slug | question |
|---|---|
| indie-technologies-inc | $60M+$46M filings, related person "Alfred Lin", no identifiable company or documented deal. Real Lin deal under a stealth name, or a common-name homonym? |
