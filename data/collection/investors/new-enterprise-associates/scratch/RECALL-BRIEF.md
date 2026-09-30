# Recall probe brief (COLLECTION.md s3 "The recall probe"). PRO-100 NEA

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/new-enterprise-associates/scratch/`. Write only
`recall-probe.json`. Never touch git, the ledger, classification, config, identity-merges, decisions, scripts/ or other
investors. Keep scratch under `scratchpad/rp/`. Read `../documentation/decisions.md` (the boundary) and COLLECTION.md s1
evidence rules and s3 "The recall probe" (`../../../COLLECTION.md`).

Question: is every real NEA deal a row? The base is `../companies/base.json` (field `name`; check aliases and former
names before calling a company missing). A candidate lands only with a citation you read that ties an NEA FUND to the
company (a press release or article naming New Enterprise Associates / NEA as investor in a round, an SEC filing, the
firm's own page). A partner's personal check (Grovo's seed from Kittu Kolluri personally), a Connect Ventures deal (the
CAA-NEA partnership, its own vehicle), a fund-of-funds position and a namesake are rejections.

## Candidates to verify
1. From Wikipedia's insource sweep (`../sources/web/wikipedia-insource.json`): Compiere, P-CAD (Personal CAD Systems),
   Scalix, Uptake, Vuze (formerly Azureus). Also Deep Voodoo and Grovo (expected rejections; say why).
2. The companies behind sale-consideration rows (D8): Logic Modeling (NEA got Synopsys stock by selling it to
   Synopsys, 1994: the firm's archived Synopsys page says so; its capture is the `wayback_first_link` of the
   `synopsys` row in base.json), Vela Pharmaceuticals (bought by Pharmos, 2006), Avivo Corporation (sold Visual
   Sciences to WebSideStory, 2006; `https://www.sec.gov/Archives/edgar/data/1357525/000095013408003738/v37326exv2w4.txt`
   has NEA 10 as an "AVIVO INVESTOR").
3. Niroda (an unpublished 2026 entry in NEA's CMS; find the round).
4. NEA's single-deal SPVs (EDGAR Form D filers, all at 1954 Greenspring Drive, Timonium): NEA BH SPV (2019) and BH SPV
   II (2020), SH SPV (2023) and SH 2025 SPV, RP SPV (2024), TS 2024 and TS 2025 SPV, CH SPV (2024), CH 2026 and CH 2026 II
   SPV, PLA 2025 SPV, 1F 2025 SPV, 1M 2025 SPV. Decode each: the initials plus the filing date plus press about an NEA
   round at that date (read the Form D: `python3 secget.py "<filing url>" --grep "."`; EDGAR filer pages at
   `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<cik>&type=D`). Record the company each SPV most
   likely holds and whether it is already in base. An SPV is never a row; a decoded company missing from base is a
   candidate only with a citation naming NEA.
5. Press sweep for recent NEA-led rounds the site may not carry yet: Google News, one query per year window 2019 to
   2026 (`NQ_TAG=rp python3 nq.py rp-<year> '"New Enterprise Associates" led <year>'` and '"NEA" "led by" Series
   <year>'), then keep only companies absent from base.
6. Parametric enumeration: list well-known NEA investments by era (1980s-90s: networking, semiconductors, biotech;
   2000s; 2010s; 2020s) from what you know, as leads only, and check each against base; a lead missing from base is a
   candidate only once a source you read confirms an NEA fund.

## Output
`recall-probe.json`: `{"rows": [{"name", "decision": "add"|"reject"|"in_base", "in_base_as" (slug), "citation",
"first_seen" (year), "basis" (one sentence quoting the source), "source" (which leg: wikipedia, d8, draft, spv,
press, parametric)}], "spv_decode": [{"spv", "cik", "form_d_date", "company", "in_base_as", "confidence", "basis"}]}`.
Write incrementally. WebSearch: at most 15 calls in total; prefer nq.py (Google News), WebFetch and EDGAR.

Report in under 250 words: adds with their citations, rejections by reason, the SPV decode table, and how many
parametric leads were already in base.
