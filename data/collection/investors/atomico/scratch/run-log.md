# Atomico run log (PRO-79)

Resume point after a compaction: re-read COLLECTION.md, this file, and
`python3 scripts/run.py status --investor atomico`.

## 2026-09-26 kickoff (Erik: "please collect Atomico")
- Usage at kickoff: weekly 21%, Fable 4% (5-hour 18%).
- Parallel wave on the shared checkout: "Point Nine collection" and "IVP
  collection" sessions running. §12 etiquette: touch only
  data/collection/investors/atomico/, commit by pathspec, no scripts/ edits
  (new layer code lives in scratch/ until the close write-back).
- IA machine-wide cooldown hit at ~19:10 UTC (another session tripped the
  firewall); clears ~20:03 UTC.
- decisions.md written (D1-D11, no deltas); PRO-79 kickoff comment posted,
  issue In Progress.

## Evidence found at kickoff
- SEC: 9 own fund filers (see decisions D1); ERAs CRD 301113 + 165691; ADVs
  downloaded to data/filings/adv/ (7.B total ~$4.17B).
- FTS sweep done: sources/edgar/fts-hits.json (225 docs). Third-party
  readings: Skype = Atomico LP (S-1); Velti = Seedcamp LP list; Digimarc =
  EVRYTHNG acquirer; Coincheck = Aplo acquirer; Ferrovial / Partners Group /
  FS MVP = LP-side; Hinge Health, Klarna, Lilium, Compass = fund filings;
  GSV 8-K = Knewton round; SPAC director bios = persons.
- Site eras (from CDX): 2008 /ourportfolio/*.xml; 2008-2010 portfolio*.php;
  2011 /portfolios/{atomico-ventures-i,atomico-ii}/<slug>; 2012-2017
  /portfolio/<slug>; 2018-2019 /partnerships/<slug> (+page/2-4); 2020-2021
  /investments/<slug>; 2021-2026 /partners (+?page=, ?stage=, ?status=) and
  /partners/<slug> (Next.js __NEXT_DATA__: investment year, lead, stage
  Venture/Growth, status Current/Exited, location, themes). Live site is
  behind a Vercel checkpoint: use the archive.
- People eras: /ourteam (2008), aboutatomico2.php (2008-10),
  /about/{investment-team,...} (2011-12), /team (2012-15, 2019-26), /people
  (2016-17); /api/teammembers JSON (2025) with role groups.
- Job board careers.atomico.com (Getro): 68 companies ->
  sources/site/jobboard-companies.json (scratch/jobboard-pull.py).
- Companies House layer: scratch/companies_house.py (website reader, cache in
  data/filings/companies-house/cache, gitignored) + scratch/ch_officer_graph.py
  -> sources/registers/companies-house/officer-graph.json. Config
  registers.uk (firm entities, firm office address patterns).

## Next
1. When IA clears: fetch era samples, write wayback eras, run wayback-pull
   (background), partner-roster; pull archived /partners pages + per-company
   pages into sources/site/*.json; team API.
2. Officer graph over the full investing roster.
3. EDGAR chain (run.py collect), base build, traps, prepare, grind.

## 2026-09-26 ~19:50 UTC — UK register layer working (IA still in cooldown)
- Officer graph over 108 archived people: 103 companies with an anchored
  person's seat; ~35 with an Atomico office service address. Nickname-aware
  re-run anchored Ben Blume. sources/registers/companies-house/officer-graph.json
- Backtrace (scratch/ch_backtrace.py): company profile + shareholder
  statements (AR01 to 2016 / CS01 with updates) read by pypdf or macOS Vision
  OCR (scratch/pdf-ocr.swift; compiled binary in data/filings/companies-house/),
  holder lines matching "atomico" -> entry bracket + share class. Works:
  EVRYTHNG, Chemist Direct, Playfire, Quipper, Hailo (HNH), Farmdrop,
  Uniplaces, LendInvest, Graphcore, Rekki, Jobandtalent, Fon (Atomico II entry
  2011-12, so Zennstrom's 2006 Fon seat was pre-Atomico).
  Fixes landed: statements are read from one before the firm's entry year
  (`since` hint) and a statement bounds from below only if it lists >=5
  holdings. RE-RUN all with --refresh + since hints after the base exists.
- Findings for the report: SH01 never names allottees (class/number/date
  only); AR01 full list only every third year; the website's filing-history
  category filter is not applied server-side (read whole history, 25/page).
- uk-companies.json: 29 register numbers identified (+ Kheiron Medical =
  DeepHealth UK Ltd 10184103, renamed after the RadNet/DeepHealth purchase;
  Newco Trading = Chemist Direct's former holding name).
- Telegram has an Atomico /partners page (2021-10 capture): check the CMS
  record; the 2021 instrument was pre-IPO convertible bonds -> possible
  run-time ruling on T3 if the page confirms a position.
- Archive runner queued (scratch/archive-run.sh): cms-pull, team-pull,
  partner-roster, wayback-pull, insights-pull. Then: 2008-2010 listing eras,
  site-portfolio (file_list sources), base build.
