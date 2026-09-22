# a16z (Andreessen Horowitz) — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to a16z. The judge
cites these rulings per line; all confirmed by Erik, 2026-08-18.

1. **Firm boundary**: one firm, one decision desk. All fund families are
   in — crypto, bio/health, games, American Dynamism, cultural leaders,
   infrastructure. Unlike HongShan / Peak XV these are not separate desks;
   no desk partition exists for a16z.
2. **Program vehicles**: speedrun (the accelerator) deploys fund money by
   firm decision and is in — same logic as Sequoia's Arc. Scout checks are
   out unless a main fund followed.
3. **Instruments**: primaries, secondaries and tenders by the funds are in.
   Token and protocol positions are in when listed on a16z's own portfolio
   page — the site listing is the sufficient evidence class; a token-only
   position never enters on a name-match.
4. **Carried over verbatim** from the generic rules: ex-partner filings
   out, partners' personal directorships (Section 16) out, LP stakes out,
   evidence-sufficiency rules unchanged.
5. **Window**: founded 2009, so the standard 2006 window covers the firm's
   full history; no pre-window class exists.
6. **Fund-shaped list entries** (ruled 2026-08-30, during base review):
   an investment-list entry whose name is fund-shaped (Capital / Fund /
   Ventures / Management, fund numerals) and that cannot be identified as
   an operating company is `not_member` — the LP-stake class — until
   evidence identifies it otherwise; the verdict is amended and the row
   returns on the next rebuild if identification lands. Applied to
   AMP Fund, Drone Capital I, Revival Fund Management (and consistent
   with the identified cases A.Capital, Meta4 Capital, BlockTower
   Capital). Fund-shaped names identified AS operating companies stay in
   (Capital.xyz, Foundation, Proof Holdings, Essence Ventures — the last
   confirmed by Erik 2026-08-30 as an operating media/commerce company).
7. **Pure protocol-asset positions** (ruled 2026-08-30, refines #3):
   a listed token position stays in when it maps to an operating or
   issuing organization (a DAO with a treasury and governance, a labs
   entity — Lido, Uniswap, Optimism, Yield Guild Games); a pure
   base-layer asset holding with no such entity is a treasury position,
   not a portfolio company, and is `not_member` (Bitcoin, Ethereum —
   both of which a16z itself later removed from the investment list
   under its unannounced-public-digital-assets exclusion). Where the
   token and its company are both listed, they are one row under the
   company (Filecoin -> Protocol Labs).

Verdicts live in `membership-ledger.json` and are re-applied on every
rebuild; human verdicts (`who: "erik"`) outrank agent verdicts; excluded
rows are preserved in `excluded.json`, never deleted.

8. **Program cohorts: entry dates for the C2A clock (2026-09-16)**
   (`who: agent`; an evidence table, not an Erik ruling): the seed-to-A
   graduation rule censors entries younger than 24 months, so a
   program-entry row needs the month its cohort started, failing that
   the month the cohort was announced.

   **Stage superseded (Erik, 2026-09-22): speedrun, TxO and CSX rows are
   `Pre-Seed`, not Seed.** The table below reads the instruments and
   treated every programme row as a Seed entry by instrument; Erik's
   programme rule (2026-09-19, COLLECTION.md: a small-check entry on a
   programme's standard terms is Pre-Seed) governs instead, and this
   note's reading does not survive as an investor-specific exception.
   Applied by PRO-132's a16z pass to 250 speedrun and 26 TxO rows; Erik
   confirmed it on 2026-09-22 ("keep them pre-seed, update a16z's note")
   against this paragraph. Pre-Seed rows leave the seed-to-A cohort, so
   the cohort dates below matter only for rows that are NOT programme
   entries. The instruments stay recorded because they are the evidence
   the programme rule is read against: speedrun invests "$500K for 10% upfront in a
   SAFE and another $500K in your next round within 18 months"
   (speedrun.a16z.com/faq); TxO's first cohort took a "$100K investment
   from the Tides Foundation" via "a SAFE note that converts into a 7%
   percentage ownership stake" (a16z.com/announcing-txos-first-cohort/),
   later TxO cohorts' terms are not on the fetched posts, and
   a16z.com/txo/ now 301-redirects to speedrun.a16z.com (checked
   2026-09-16); CSX invests "a minimum of $500,000 in each company"
   (a16zcrypto.com Fall 2024 and CSX 04 posts; the 2022 relaunch post
   says "$500k in seed funding"), instrument unstated on every fetched
   page. Dates come from a16z's own pages first; press is used only where
   no a16z page states the date, and the row says so. 20 web calls.

   | cohort | start month (YYYY-MM) | basis (URL) | note |
   |---|---|---|---|
   | speedrun SR001 | unknown | https://speedrun.a16z.com/ ("Since launching in 2023"); https://a16z.com/applications-for-sr005-are-officially-open/ ("Since launching speedrun ~2 years ago", posted 2025-03-31) | Year 2023 only. Tried speedrun.a16z.com, /faq, two a16z.com-restricted searches naming SR001, the 2025-03-12 relaunch post; no a16z page states the month. Every 2023 month is more than 24 months before 2026-09, so year precision would leave the row uncensored; whether year precision is acceptable is Erik's call, until then undetermined. |
   | speedrun SR002 | unknown | GamesBeat, press, search snippet only: Demo Day "during GDC" (GDC 2024 = 2024-03), https://gamesbeat.com/a16z-opens-applications-for-75m-speedrun-tech-and-games-accelerator-class/ | No a16z page states a start; the 12-week format implies a ~2024-01 start, inference not a date. Same year-precision remark as SR001 (any 2024-H1 month is more than 24 months before 2026-09). |
   | speedrun SR003 | 2024-07 | GamesBeat, press, search snippet (article not fetched): "ran for 12 weeks beginning on July 29, 2024", Demo Day at SF Tech Week 2024-10, same URL as SR002 | Press used because a16z's own SR003 page (https://sr-cohh.a16z.com/) is a bare application form with no dates. 26 months before 2026-09: not censored. |
   | speedrun SR004 | unknown | https://a16z.com/meet-the-new-a16z-speedrun/ (posted 2025-03-12: "SR004 Demo Day fast approaching"); https://info.a16z.com/register-for-a16z-games-speedrun-sr004-demo-day-2025.html (not fetched) | A ~2025-03 Demo Day implies a ~2025-01 start on the 12-week format, inference only. Any 2025 month is inside the 24-month window as of 2026-09. |
   | speedrun SR005 | 2025-07 | https://a16z.com/applications-for-sr005-are-officially-open/ (posted 2025-03-31): "July 28 – October 10, 2025", Los Angeles | Post states "up to $1M". |
   | speedrun SR006 | 2026-01 | https://a16z.com/a16z-speedrun-application-winter-spring-2026/ (posted 2025-09-02): "late January through April 2026", San Francisco | "$500K for 10% upfront in a SAFE" plus "$500K in your next round within 18 months". |
   | speedrun SR007 | 2026-07 | https://a16z.com/applications-for-a16z-speedrun-sr007-are-now-open/ (posted 2026-04-20): "runs from July 27 through October 11, 2026" | Same terms; "Six cohorts in" confirms SR001 to SR006 as the prior set. |
   | speedrun SR008 | 2027-01 | https://speedrun.a16z.com/faq: "late January through April 2027 in San Francisco" | Not started as of 2026-09-16; no member can carry it yet. |
   | TxO Cohort Alpha (first cohort) | 2020-10 (announcement month) | https://a16z.com/announcing-txos-first-cohort/ (posted 2020-10-30) | Start not stated; "The program will run for 10 months, all online". Seven companies: Oui the People, Breakr, Autumn Adeigbo, Pamper, FutureStream, Coco and Breezy, Elite Sweets. |
   | TxO second cohort ("Meet the next Talent x Opportunity Founders") | unknown | https://a16z.com/meet-the-next-talent-x-opportunity-founders/ (not fetched, budget) | Sits between Cohort Alpha and Spring '23; one fetch would give the announcement month. |
   | TxO Spring '23 | unknown | https://a16z.com/welcoming-the-talent-x-opportunity-spring-23-cohort/ (not fetched, budget) | Season only, from the post title; one fetch would give the announcement month. Any 2023 month is more than 24 months before 2026-09. |
   | TxO Fall '23 | unknown | https://a16z.com/meet-the-talent-x-opportunity-fall-23-cohort/ (not fetched, budget) | Same as Spring '23. |
   | TxO Spring '24 | unknown | https://a16z.com/introducing-talent-x-opportunity-spring-24-cohort/ (not fetched, budget) | Season only; any 2024-H1 month is more than 24 months before 2026-09. |
   | TxO Fall 2024 | 2024-07 (announcement month) | https://a16z.com/meet-the-talent-x-opportunity-fall-2024-cohort/ (posted 2024-07-18) | Start not stated on the post. Five companies: Fashivly, Feedplan, GamerXSociety, Timbucktoo, Virch Merch. Boundary row: the announcement month is 26 months before 2026-09, a literal fall start would be about 24. |
   | TxO Spring 2025 | unknown | https://a16z.com/introducing-the-talent-x-opportunity-spring-2025-cohort/ (not fetched, budget; search snippet: cohort "recently kicked off" in San Francisco, five startups incl. Unisound) | Any 2025 month is inside the 24-month window as of 2026-09. |
   | TxO Fall 2025 and later | unknown | a16z.com/txo/ 301-redirects to speedrun.a16z.com (checked 2026-09-16) | Not searched; the program page is gone, so a TxO row dated after Spring 2025 needs speedrun's pages. |
   | Crypto Startup School 2020 | 2020-02 | https://a16zcrypto.com/posts/article/crypto-startup-school-relaunched/ ("launched ... in February 2020") | No cheque: the 2022 relaunch post says participants "will now receive $500k", so a 2020 school company is not a program entry by instrument and enters only on its own priced round. |
   | CSX 01: Crypto Startup School 2023 (Los Angeles) | 2023-03 | same URL (posted 2022-10-17): "The program will begin on March 6, 2023", "12 weeks", "$500k in seed funding" | Numbering CSX 01 to 03 is inferred from the "CSX 04" name a16z gave the Spring 2025 cohort. |
   | CSX 02: Spring 2024 (London) | 2024-03 | https://a16zcrypto.com/posts/article/crypto-startup-accelerator-csx-spring-2024-cohort/ (posted 2024-03-26: cohort starts "this week", "over 10 weeks") | 25 companies listed on the post (AminoChain through zkPassport). 30 months before 2026-09. |
   | CSX 03: Fall 2024 (New York) | 2024-09 | https://a16zcrypto.com/posts/article/announcing-the-csx-fall-2024-cohort/ (posted 2024-09-09: "this week in New York City", "over the next 8 weeks", "minimum of $500,000 in each company") | 21 companies listed (Anera Labs through zkSpin). Exactly 24 months before 2026-09: the C2A clock's boundary comparison decides censoring. |
   | CSX 04: Spring 2025 (San Francisco) | 2025-04 | https://a16zcrypto.com/posts/article/apply-to-join-the-csx-04-cohort-in-san-francisco-this-spring/ (posted 2025-01-08: April 2025 start, June 2025 Demo Day, "minimum of $500,000") | Planned start from the application post; the cohort-announcement post was not fetched. |
   | CSX 05 and later | unknown | https://a16zcrypto.com/accelerator/ lists no cohorts | Not searched (budget); any such cohort started after 2025-04 and sits inside the 24-month window once dated. |

   A speedrun/TxO/CSX company's entry_date is its cohort's start month;
   the note on the row names the cohort (e.g. 'speedrun SR002'). A
   company whose cohort is unknown (a cohort whose row above reads
   `unknown` counts as unknown) is `undetermined` for graduation, never
   `censored` or `not_graduated`.
