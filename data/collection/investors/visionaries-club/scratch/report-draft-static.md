## Coverage per evidence regime

| Layer | What it gave | Notes |
| -- | -- | -- |
| Live visionaries.vc (Kirby single page) | 59 companies with the firm's claim, description and thesis; no year, stage or fund | `scratch/site-live.py` |
| Live tomorrow.vc (Visionaries Tomorrow) | 10 companies | `scratch/site-tomorrow.py`; older captures render only the carousel's first slide |
| WordPress /portfolio/ 2023-2025 | 32, 38 and 44 companies per year; 4 names since dropped (Tactic, Uify, Sustained, Loxo) | Common Crawl only; the Internet Archive blocked this machine twice |
| Gatsby site 2020-2022 | see below | the portfolio is hard-coded in the page-component bundle, which only the Internet Archive holds |
| EDGAR | 3 own Form Ds (2021), no portfolio; full-text search: 3 own hits, no exit-side filing | Form D sweep on the roster found only the firm's own vehicles and a La Famiglia fund |
| Form ADV (CRD 317147) | 11 private funds, $193.1M gross assets; owners Lacher and Pollok | AUM floor, fund ladder, T1 |
| German register (North Data) | fund KGs named on 16 portfolio GmbHs' shareholder lists; yearly holding counts per fund | `fund_filing` class (R3); added Tytan, ContextFab, Acapela; dated Tacto and GetMomo to 2020 |
| Deutsche Startups (WordPress search API) | 189 posts, 268 sentences naming the firm, 2019-2026 | recall: Fina, Trana; identities Simplo = GetMomo, aiConomix = automaited, DashDash = Rows |
| Google News sweeps | half-year windows 2019-2026 for "Visionaries Club", "Visionaries Tomorrow" | recall: Conveo, Tytan; rejected Causal Labs, Roboat |
| Wikipedia insource | 6 articles, 3 in the base, no new company | |
| Vendor lists (Tracxn, Startupintros) | leads only, never cited | Conveo came from here and was confirmed in press |

## Method deltas

1. **The domain's previous owner.** visionaries.vc was a Japanese Toastmasters club's site until 2019; every capture before 2020 is that club's and was not read (D7).
2. **Archive route.** The Internet Archive refused this machine at 11:43 (60 minutes) and again at 12:43 after seven requests (120 minutes). Common Crawl carried the 2023-2025 WordPress era (72 crawls from 2019, one index unreadable: CC-MAIN-2023-06) and tomorrow.vc; the Internet Archive was needed only for the Gatsby bundle, so the pass was reordered to fetch that first.
3. **Register as a membership layer.** North Data's free pages list, per fund KG, the portfolio GmbHs whose shareholder lists name it (up to three a year, the rest counted). That is forward enumeration the §5 table calls aggregator-only, and it is filing-grade (R3).
4. **Deutsche Startups' own search API** (`wp-json/wp/v2/posts?search=`) returns every post naming the firm with its full text: a German deal-monitor recall layer that cost two requests.
5. **Stage by construction** (R2): a firm founded after a company's Series A can only have entered at Growth.
