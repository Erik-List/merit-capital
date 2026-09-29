# Delta brief: PRO-75 GV, the graduation pass and the rows new since the rebuild

You decide the Seed-to-A graduation column (S2A) for the rows you are given and, where a row asks for more, its
other open columns. Work only inside `/Users/erik/Developer/merit-capital/data/collection/investors/gv/scratch/`.

**Read `JUDGE-BRIEF.md` first: its hard limits, tools and contract all hold**, with two changes: this brief replaces
its S2A bullet, and **WebSearch and WebFetch are exhausted for this session: do not call them.** Read pages with
`curl -sL -A "Mozilla/5.0"` and cite a page only after you read it. Google News works through `nq.py`.

## Your rows
Your slugs are in your prompt. For each:
- `python3 gradview.py <slug> ...` prints the row's stage and entry as recorded, its Form D rounds, the Form D
  layer's verdict, every headline the publisher surfaces returned that names the company (Google News with round
  and exit words, Google News with "GV", TechCrunch's own search, Crunchbase News's own search, all dated), and
  what sibling books decided for the same company.
- `python3 show.py <slug>` prints the row's full evidence view (site, archive, posts, filings, news, siblings).
- Cite a surface headline with `jl.GNEWS(slug, "unique title substring")` (TechCrunch and Crunchbase News items
  cite their own link; Google News items are decoded to the publisher URL). `jl.NEWS` still covers `nq.py` results.

## S2A: the contract (COLLECTION.md s6, "seed_to_a_graduation"; read it, lines 1617-1822)
Every row whose entry stage is Seed or Pre-Seed ends with exactly one of `graduated | not_graduated | censored`.
Every decided or censored row carries `entry_date` (YYYY, YYYY-MM or YYYY-MM-DD).

1. **entry_date**, in this order: the seed's own citation (the article or release announcing the round GV was in),
   the Form D entry filing where the stage comes from the filings, or the firm's own dated round on /ai
   (`site.ai_first_invested`, decisions D7). Never `first_seen` (a capture year), never note prose, never a later
   round's filing. Give the month wherever a source gives it.
2. **censored**: the entry is less than 24 months before today (after 2024-09-29). A search that finds nothing
   inside the window leaves the row censored; only a cited acquisition or shutdown decides a young row.
3. **graduated**: a later priced round, cited. `grad_src="web_verified"` (a press report or release naming the
   later round, `grad_cite`) or `"first_party"` (the firm's or the company's own page), `grad_conf`, and the round
   in `rounds=[jl.rnd(...)]`. **A later round the record names Series A or later graduates whatever the amounts.**
   An unnamed later round graduates only at >= max(2x the seed, $5M); where the seed amount is not on record use
   the era ceiling: the later round must reach $5M for an entry up to 2014, $8M for 2015-18, $12M for 2019-21, $16M
   from 2022. A Form D verdict in the item (`formd_graduation`) may be confirmed with `grad_src="formd"` (agree
   with it) or disputed with a citation. Vendor pages (Crunchbase profiles, PitchBook, Tracxn, CB Insights, Dealroom)
   never cite a graduation; Crunchbase News is press and may.
4. **not_graduated**, only on one of two footings:
   a. a cited terminal event: the acquisition or shutdown with no later round before it, `grad_src="web_verified"`
      (or `first_party`), `grad_cite` = the acquisition or shutdown report, the note saying the seed was the last
      round. This decides even inside the 24-month window.
   b. the absence test, `grad_src="absence_check"`: the entry is past the window (read at the LAST day its date can
      mean: a bare "2024" cannot carry this no), the entry year is 2005 or later, `grad_asof="2026-09-29"`, and
      `surfaces=jl.GRADLINES(slug)`, which writes the `firm:`, `formd:`, publisher and `sibling:` lines from the
      evidence on disk. **Read what GRADLINES wrote before you record it**: it lists the newest funding headline
      per surface; if any headline actually reports a later round of THIS company, the row is graduated, not a no.
      Pass `firm_note=` / `formd_note=` / `extra=[...]` when you searched more (e.g. `"company: <site> -> ..."`).
   A $1B+ or public row can never be not_graduated (rule 7): find the round that got it there.
5. **Uncited stage**: if the row's entry stage has no `entry_stage_citation` and is not `formd_structural` /
   `formd_band` (gradview prints `src` and `cite`), a decided row must also carry `flags=["stage_uncited"]` and
   `stage="Seed", stage_src=<its src>, stage_conf="low"`, unless you cite the seed now (then give `stage_cite` and
   `stage_src="web_verified"`). A row with nothing that dates or evidences its seed has no Seed entry to decide:
   set `stage="undetermined"` (no graduation key).
6. **A wrong stage**: if the record shows GV entered later than the seed (the seed without GV, GV in the A or B),
   re-stage the row (`stage=...`, `stage_disputes_band` or `model_disputes_source`, note) and give no graduation.
7. Keep the note: pass `note=` as the row's existing note with your S2A sentence appended ("S2A: ..."), in plain
   prose, no em-dashes. `jl.cls(slug, grad=..., grad_src=..., grad_cite=..., grad_conf=..., grad_asof=...,
   surfaces=..., entry_date=..., note=..., rounds=[...])`. Emit only these keys plus deliberate disputes.

## Rows new since the rebuild (judge d1 only)
Membership first where the item's `need` says `membership`: a `jl.verdict(slug, "member", basis, ec="web",
conf=..., cite=...)` line (the recall additions' evidence is in `../companies/membership-ledger.json` under
`gv.recall_additions`; read the cited page before you rely on it), then one classification line with every open
column. The split rows are different companies from the rows they were split from:
- `spruce-health`: Spruce (sprucehealth.com), the dermatology then care-communication app, listed 2015-17; not
  Spruce Finance.
- `bloom`: Bloom (bloomcloser.com), an elder-care device, listed 2015-17 under Rich Miner; the prefilled BE and the
  "Kyowa" acquirer are name joins to check.
- `secret`: Secret (secret.ly), the 2014 anonymous-sharing app (MG Siegler); shut in 2015.
- `bowery-bowery-io`: Bowery (bowery.io), developer environments, listed 2014-15 under MG Siegler; not Bowery
  Farming.
- `basis-basis-io`: Basis (basis.io, Intangible Labs), the 2018 algorithmic stablecoin that raised $133M and shut in
  December 2018; the a16z and Bain Capital Ventures rows hold the same company.
- `astrid`: Astrid the to-do app (Yahoo bought it in 2013); only its country and S2A are open.

## Finish
`NQ_TAG=<TAG> python3 judgments-<TAG>.py` must print `recorded ...`; on `REJECTED`, fix and re-run; read the whole
output. Report in under 200 words: the counts (graduated / not_graduated by footing / censored / re-staged /
undetermined), any verdict lines, rows where a sibling book disagrees with your S2A, anything wrong in the base.
