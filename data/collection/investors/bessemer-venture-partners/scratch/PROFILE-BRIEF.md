# Profile research brief (COLLECTION.md s11). PRO-80 Bessemer Venture Partners

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/`. Write
only `profile-research.json` (and scratch under `scratchpad/profile/`). Never touch git, investor/, config, the
ledger, classification, scripts/ or other investors. The machine's disk is nearly full: download nothing large.
Read COLLECTION.md s11 (`../../../COLLECTION.md`, from `## 11.` to `## 12.`: find the lines with
`grep -n "^## 11. \|^## 12. " ../../../COLLECTION.md`) first, and `../documentation/decisions.md` (the boundary: BVP
Forge is the buyout strategy and is out of the portfolio; the Bessemer Trust / Bessemer Securities namesakes).

Already on disk (do not redo):
- `../sources/adv/adv-7b-funds.json`: every private fund's gross asset value on the Form ADV of 2026-05-13 (Bessemer
  Venture Partners = Deer Management Co. LLC, CRD 159279; Item 5.F regulatory assets $20,239,213,324; principal
  office 1865 Palmer Avenue, Larchmont NY; other offices Redwood City, San Francisco, New York, Wellesley, Cambridge).
- `../entities.json` and `entity-addresses.json`: the firm's SEC filers (funds, general partners) with CIKs.
- `../sources/site/posts.json`: the firm's own posts (news, Atlas, memos), incl. "$5.75 billion to back the founders
  building what's next" (2026), "Introducing Our India Fund" (2021-11-30), "Why we launched Bessemer's Growth
  practice" (2019-10-08). Search it: `python3 -c "import json;[print(r['date'],r['title'],r['url']) for r in json.load(open('../sources/site/posts.json'))['rows'] if 'fund' in (r['title']+' '+r.get('subtitle','')).lower() or 'billion' in r['title'].lower()]"`.
- `../sources/site/sanity/aboutPage.json`: the About page (timeline 1911, 1976, 1981, 2006 India, 2007 Tel Aviv, 2019
  growth fund, 2021 London, 2022 BVP Forge, 2023 the $1 billion AI commitment; the eight offices with addresses;
  hero stats "AUM $20B", "IPOs / deSPACs 155+", "Active Portfolio Companies 450+").
- `../sources/site/team-pages.json`: the live team (315 people: role investor / operatingAdvisor /
  firmInfrastructure, titles, LinkedIn and X links as the CMS carries them, alumni flagged).

## What to research, each with a citation you read
1. **Funds**: every fund the firm raised since about 2004, with size, vintage and a source: Bessemer Venture
   Partners VI (2004-05), VII (2007, $1B?), VIII (2011, $1.6B), IX (2015, $1.6B), X (2018, $1.85B), XI and Century
   Fund II (2021, $3.3B together: $2.475B + $825M), XII and BVP Forge (2022: $3.85B + $780M), XIII and Century
   Fund III (2026: the firm's "$5.75 billion" post; Form Ds filed 2026-09-14), the Century Fund (2019, $525M?), the
   India fund (2021, $220M) and India II (2025, $350M), BVP VII Special Opportunity Fund (2009). The numbers in this
   list are leads from memory: confirm each from the firm's own post or press (TechCrunch, WSJ, Reuters, Bloomberg,
   Fortune, PE Hub, Business Wire) or reject it. For each fund with a Form D, give the fund's CIK (from
   `../entities.json`) and whether its newest Form D shows the full size sold (then give the accession and the
   total amount sold) or an indefinite / $0-sold / partial filing (then no accession). Read SEC pages with
   `python3 secget.py "<url>" --grep "."` (never bare curl to sec.gov); a fund's filing list is
   `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<cik>&type=D&dateb=&owner=include&count=40`.
   Forge funds are listed separately and marked `"forge": true` (they are outside the portfolio boundary).
2. **History facts** (for a 40 to 80 word, 3-sentence history): the founding (Henry Phipps, Bessemer Securities,
   1911, New York; the 1981 spin-out as Bessemer Venture Partners), the bets that made the firm (with a source
   each: e.g. Staples, Ciena, VeriSign, Skype, LinkedIn, Yelp, Shopify, Twilio, Pinterest, Toast), where it stands
   today (the 2026 raise or the assets it manages).
3. **investment_range legs**: the smallest check or round size the firm states anywhere (its site, the "Seed
   investor's guide to Bessemer" Atlas post, an interview), the largest round it LED in the last five years (a
   cited figure), any program floor.
4. **investment_stage / geo / scope** as the firm states them (its homepage: "dedicated early and growth
   practices"; its roadmaps / sector pages; "Where we invest"), with the page you read.
5. **Notable investments**: the five companies a general reader would recognise first among Bessemer's portfolio
   (check each is in `../companies/base.json`), in order of fame, with the base slug.
6. **Icon**: run `cd /Users/erik/Developer/merit-capital && npx tsx scripts/fetch-investor-icon.ts --discover https://www.bvp.com`
   and report what it lists (do not publish or upload anything).

## Output
`profile-research.json`: `{"funds": [{"name", "size_usd", "vintage", "cik", "accession", "sold_usd", "source",
"note", "forge"}], "history_facts": [{"fact", "source"}], "range": {...}, "stage_geo_scope": {...},
"notable": [{"name", "slug", "why"}], "icon_discover": "...", "notes": [...]}`. Write incrementally. WebSearch: at
most 10 calls; prefer WebFetch of known pages, `NQ_TAG=pf python3 nq.py pf '<query>'` (Google News) and
`python3 wikifetch.py "Bessemer Venture Partners"`. Report in under 200 words.
