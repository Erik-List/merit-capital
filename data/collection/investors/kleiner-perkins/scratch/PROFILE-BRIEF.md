# Profile research brief (COLLECTION.md s11). PRO-99 Kleiner Perkins

Work in `/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch/`. Write only
`profile-research.json` (and scratch under `scratchpad/profile/`). Never touch git, investor/, config, the ledger,
classification, scripts/ or other investors. Read COLLECTION.md s11 (`../../../COLLECTION.md`, from `## 11.` to `## 12.`)
first, and `../documentation/decisions.md` (the boundary: Bond is external from 2018-09; KPCB China provisionally IN).

Already on disk (do not redo): `../sources/adv/adv-7b-funds.json` (every fund's gross asset value on the 2026-03-31 ADVs
of Kleiner Perkins CRD 161035 and KPCB China CRD 161470), `../sources/site/posts.json` and `raw/posts.json` (the firm's
posts, incl. "Our New Funds: KP22 and KP Select IV" 2026-03-24, "Announcing KP21 and Select III" 2024-06-28, "Announcing
KP 20 & KP Select II" 2022-01-11), `../sources/site/team-pages.json` (the live team), `wiki/Kleiner_Perkins.txt`.

## What to research, each with a citation you read
1. **Funds**: every fund the firm raised since about 2006, with size, vintage and a source: KPCB XII (2006), XIII
   (2008), XIV (2010?), XV (2012), XVI (2014), XVII (2016), KP XVIII (2019), XIX (2020), XX, XXI, XXII; KPCB Green Growth
   Fund (2008), Digital Growth Fund I (2010), II, III (2016); Kleiner Perkins Select Fund (I, 2020 or 2021), II, III, IV;
   Kleiner Perkins Flex I; KP Sightglass I and II (what are they?); the iFund (2008, $100M then $200M), sFund (2010,
   $250M), the Pandemic and Bio-Defense Fund (2006); KPCB China Fund (2007, $360M) and Fund II. The firm's own posts and
   announcements first, then press (TechCrunch, WSJ, Reuters, Bloomberg, Fortune). For each fund with a Form D, give
   the fund's CIK (from `../entities.json`) and whether its Form D shows the full size sold (then give the accession and
   the TOTALAMOUNTSOLD) or an indefinite/$0-sold filing (then no accession). Use `python3 secget.py <url> --grep "."` for
   SEC pages, never bare curl to sec.gov.
2. **History facts** (for a 40-80 word, 3-sentence history): founding year, city, founders; the bets that made the firm
   (with a source each); where it stands today (the 2026 raise). Any rename date (KPCB to Kleiner Perkins, 2019).
3. **HQ and offices**: the firm's own site statement of its offices (About page), and the ADV principal office
   (sources/adv/161035.pdf, Item 1.F).
4. **investment_range legs**: the largest round the firm LED in the last five years (a cited figure), the typical early
   check or round size it states anywhere (a post, an interview), and any program floor (KP Fellows is not an
   investment program; say so if nothing exists).
5. **investment_stage / geo / scope** as the firm states them (its own site filters: Early, Growth; sectors AI,
   Consumer, Enterprise, Fintech, Hardtech, Healthcare, ...), with the page you read.
6. **Team**: from `../sources/site/team-pages.json`, which people are investors (role) and which are operations; list
   them with role and LinkedIn/X links exactly as the CMS carries them (never guessed).

## Output
`profile-research.json`: `{"funds": [{"name", "size_usd", "vintage", "cik", "accession", "sold_usd", "source", "note"}],
"history_facts": [{"fact", "source"}], "offices": {...}, "range": {...}, "stage_geo_scope": {...}, "team": [...],
"notes": [...]}`. Write incrementally. WebSearch: at most 10 calls; prefer WebFetch of known pages, `NQ_TAG=pf python3
nq.py pf '<query>'` (Google News) and `python3 wikifetch.py "Title"`. Report in under 200 words.
