# Recall probe brief (COLLECTION.md s3 "The recall probe"). PRO-80 Bessemer Venture Partners

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/`. Write
only `recall-probe.json`. Never touch git, the ledger, classification, config, identity-merges, decisions, scripts/
or other investors. Keep scratch under `scratchpad/rp/`. The machine's disk is nearly full: download nothing large.
Read `../documentation/decisions.md` (the boundary: D1 vehicles, D2 BVP Forge out, D3 the Bessemer namesakes, D4 fund
money, D5 venture entry, D6 seats travel, D10 the anti-portfolio, X1 pre-1981) and COLLECTION.md s1 evidence rules
and s3 "The recall probe" (`../../../COLLECTION.md`).

Question: is every real Bessemer Venture Partners ("BVP") deal a row? The base is `../companies/base.json` (field
`name`; check aliases, former names and acquirer names before calling a company missing). A candidate lands only
with a citation you read that ties a Bessemer FUND to the company (a press release or article naming Bessemer
Venture Partners as investor in a round, an SEC filing listing Bessemer entities as holders, the firm's own page).
A partner's personal check, an operating partner's or advisor's own seat, a BVP Forge buyout, a Bessemer Trust /
Bessemer Securities / Lindsay Goldberg holding, a fund-of-funds position and a namesake are rejections. The firm's
own anti-portfolio (Apple, Apollo Computer, Check Point, StrataCom, eBay, FedEx, Google, Ikanos, Intel, Intuit,
Lotus, Compaq, PayPal, Facebook, Kayak, Tesla, Yammer, Airbnb, Atlassian, Snapchat, Okta, Zoom, Coinbase, Instacart)
are companies it says it passed on: a lead naming one of them is a rejection unless you read a cited Bessemer round.

## Legs
1. **Wikipedia.** The insource sweep's company candidates not in base: list them with
   `python3 -c "import json;d=json.load(open('../sources/web/wikipedia-insource.json'));print([(a['title'],a['url']) for a in d['articles'] if a.get('is_company') and not a.get('in_base')])"`;
   each article carries the sentences naming the firm (`a['sentences']`). Each gets add / reject / in_base with the
   naming sentence.
2. **BVP Forge's own deals** (needed as membership traps, not as rows): from bvpforge.com (WebFetch
   `https://www.bvpforge.com/` and its Insights and news pages) and press ("BVP Forge" acquires / invests / partners
   with), list every company BVP Forge has bought into since 2022 with the announcement URL and date. Write them
   under `"forge"` in the output: `{"company", "date", "citation", "transaction" (majority / minority / unknown)}`.
   The Forge site's "Our Experience" grid mixes Forge deals with the team's earlier work and with Bessemer venture
   companies, so a logo there is not enough: each needs its own announcement.
3. **The firm's single-deal and special vehicles on EDGAR** (CIKs in `../entities.json`): Gator Co-Invest BE, LI, PA,
   TE and VE; Cloud All Star Fund; Bessemer Venture Partners AN I, SG I, VS and PR; GoBlue Ventures LLC and Wahoowa
   Ventures LLC (2021 Forms 3/4 from the firm's office); Bessemer Venture Partners Enforta Cooperatief. Read their
   Form D or filer pages (`python3 secget.py "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<cik>&type=&dateb=&owner=include&count=40" --grep "."`)
   and decode what each holds (the two-letter suffix is usually the company's initials; a Form 3/4 names the issuer).
   A vehicle is never a row; a decoded company missing from base is a candidate only with a citation naming Bessemer.
4. **Press sweep** for recent Bessemer-led rounds the site may not carry yet: Google News, one query per year window
   2019 to 2026 (`NQ_TAG=rp python3 nq.py rp-<year> '"Bessemer Venture Partners" led <year>'` and
   `'"Bessemer Venture Partners" "Series" <year>'`), then keep only companies absent from base. Also the India and
   Israel desks: `'"Bessemer Venture Partners" India led'`, `'"Bessemer" Israel seed led'`.
5. **Parametric enumeration**: list well-known Bessemer investments by era from what you know, as leads only, and
   check each against base; a lead missing from base is a candidate only once a source you read confirms a Bessemer
   fund. Framings: 1970s-80s (Measurex, Fotomat, Interdata, Four-Phase, Ungermann-Bass, Gartner, Businessland,
   Maxim, Staples, Parametric Technology, American Superconductor, Sports Authority, Veritas); 1990s (Ciena, VeriSign,
   PSINet, Cascade, Verio, Keynote, eToys, HotJobs, Blue Nile, Mellanox, Sirocco, Sonus); 2000s (Skype, Postini,
   LinkedIn, Yelp, LifeLock, Wix, Cornerstone OnDemand, Eloqua, OLX, Diapers.com, Playdom, Vertica, Trigo); 2010s
   (Shopify, Twilio, Pinterest, Box, DocuSign, SendGrid, Twitch, Fiverr, Mindbody, Procore, PagerDuty, Auth0, Toast,
   ServiceTitan, Rocket Lab, Blue Apron, Zapier, Intercom, Canva, HashiCorp, nCino, Bright Health, Hinge Health,
   Guild, Discord, Betterment, Shippo, Teladoc, Zoosk, Snapdeal, Swiggy, BigBasket, Urban Company, PharmEasy, Nykaa);
   2020s (Anthropic, Perplexity, Abridge, Wiz, Claroty, Axonius, HiBob, Melio, Papaya Global, Yotpo, Productboard,
   Ada, ManyChat, Imply, Truepill, Spring Health, Hims & Hers, DeepL, EvenUp, Fal, Legora, Supabase, Vapi). Add
   framings of your own: life sciences 1986-2015 (Chris Gabrieli, Steve Kraus), cleantech 2005-2012 (Justin Label),
   India 2006 on (listed-company PIPEs are T3 rejections unless a pre-IPO round exists), Israel, the Century growth
   funds since 2019, space and deep tech (David Cowan, Tess Hatch), consumer (Kent Bennett, Jeremy Levine).

## Output
`recall-probe.json`: `{"rows": [{"name", "decision": "add"|"reject"|"in_base", "in_base_as" (slug), "citation",
"first_seen" (year), "basis" (one sentence quoting the source), "source" (which leg: wikipedia, vehicle, press,
parametric)}], "forge": [...], "vehicle_decode": [{"vehicle", "cik", "form_d_date", "company", "in_base_as",
"confidence", "basis"}]}`. Write incrementally (after each leg). WebSearch: at most 15 calls in total; prefer nq.py
(Google News), WebFetch and EDGAR (`python3 secget.py <url> --grep "..."`, never bare curl to sec.gov).

Report in under 250 words: adds with their citations, rejections by reason, the Forge deal list, the vehicle decode
table, and how many parametric leads were already in base.
