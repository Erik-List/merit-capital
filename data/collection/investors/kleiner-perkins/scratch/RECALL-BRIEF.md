# Recall probe brief (COLLECTION.md s3 "The recall probe"). PRO-99 Kleiner Perkins

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch/`. Write only
`recall-probe.json`. Never touch git, the ledger, classification, config, identity-merges, decisions, scripts/ or other
investors. Keep scratch under `scratchpad/rp/`. Read `../documentation/decisions.md` (the boundary: D1 vehicles, D2 Bond,
D3 fund money, D5 seats travel, X1 KPCB China provisionally IN) and COLLECTION.md s1 evidence rules and s3 "The recall
probe" (`../../../COLLECTION.md`).

Question: is every real Kleiner Perkins deal a row? The firm was Kleiner Perkins Caufield & Byers (KPCB) until 2019. The
base is `../companies/base.json` (field `name`; check aliases, former names and acquirer names before calling a company
missing). A candidate lands only with a citation you read that ties a KP FUND to the company (a press release or article
naming Kleiner Perkins / KPCB as investor in a round, an SEC filing listing KP entities as holders, the firm's own page).
A partner's personal check, a Bond-only deal (after 2018-09), a Khosla Ventures deal (Vinod Khosla after 2004), a KP
Fellows placement with no investment, a fund-of-funds position and a namesake are rejections.

## Candidates to verify
1. From Wikipedia's insource sweep (`../sources/web/wikipedia-insource.json`, the `company` candidates not in base; list
   them with `python3 -c "import json;d=json.load(open('../sources/web/wikipedia-insource.json'));print([(a['title'],a['url']) for a in d['articles'] if a.get('is_company') and not a.get('in_base')])"`;
   each article carries the sentences naming the firm). Each gets add / reject / in_base with the naming sentence.
2. The companies behind sale-consideration rows: TiMetra Networks (bought by Alcatel in 2003; Vinod Khosla sat for KP
   before 2004). Check any other listed acquirer the archive shows with status "Merged".
3. The firm's single-deal and special vehicles on EDGAR: KP Sightglass I, LLC and KP Sightglass II, LLC; Kleiner Perkins
   Flex I, LLC; KPCB Java Fund, LP (1996); KPCB Information Sciences Zaibatsu Fund II and KPCB Life Sciences Zaibatsu
   Fund II (1995-96). Read their Form D or filer pages (`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<cik>&type=D`,
   CIKs in `../entities.json`) and decode what each holds or what it was for. A vehicle is never a row; a decoded company
   missing from base is a candidate only with a citation naming KP.
4. Press sweep for recent KP-led rounds the site may not carry yet: Google News, one query per year window 2019 to 2026
   (`NQ_TAG=rp python3 nq.py rp-<year> '"Kleiner Perkins" led <year>'` and `'"Kleiner Perkins" "Series" <year>'`), then
   keep only companies absent from base.
5. Parametric enumeration: list well-known KP investments by era (1970s-80s: Tandem, Genentech, Compaq, Sun, Lotus,
   Electronic Arts, Hybritech, Cypress, Businessland, Vitalink; 1990s: Intuit, Netscape, Macromedia, Amazon, @Home,
   Excite, Juniper, Cerent, Healtheon, Handspring, Google, Symantec, Citrix, Millennium, Idec; 2000s: Tellme, Friendster,
   Bloom Energy, Silver Spring, Amyris, Fisker, Zynga, Flipboard, Path, Square, Twitter, Groupon, Nest, Waze; 2010s:
   Snap, Uber, Airbnb, Spotify, Slack, DoorDash, Robinhood, Plaid, Stripe, Peloton, Ring, Epic Games, Duolingo, Figma,
   Rippling, Loom, Viz.ai, UiPath, Gusto, Coursera, Desktop Metal, Beyond Meat, Proterra, QuantumScape; 2020s: Glean,
   Applied Intuition, Harvey, OpenEvidence, Together AI, Anthropic, Waymo, Stord, Modern Health) from what you know, as
   leads only, and check each against base; a lead missing from base is a candidate only once a source you read
   confirms a KP fund. Add other framings of your own (life sciences 1990s-2010s; greentech 2006-2014; the iFund and
   sFund cohorts; KPCB China).

## Output
`recall-probe.json`: `{"rows": [{"name", "decision": "add"|"reject"|"in_base", "in_base_as" (slug), "citation",
"first_seen" (year), "basis" (one sentence quoting the source), "source" (which leg: wikipedia, sale, vehicle, press,
parametric), "kpcb_china" (bool)}], "vehicle_decode": [{"vehicle", "cik", "form_d_date", "company", "in_base_as",
"confidence", "basis"}]}`. Write incrementally. WebSearch: at most 15 calls in total; prefer nq.py (Google News),
WebFetch and EDGAR (`python3 secget.py <url> --grep "..."`, never bare curl to sec.gov).

Report in under 250 words: adds with their citations, rejections by reason, the vehicle decode table, and how many
parametric leads were already in base.
