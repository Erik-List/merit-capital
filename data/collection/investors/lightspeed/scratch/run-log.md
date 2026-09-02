# PRO-63 run log (scratch, regenerable narrative)

2026-09-02, single session (merit-capital-02), parallel with PRO-69
(merit-capital-92) under the §11 ownership split agreed by message.

## Session-to-session split (agreed ~10:50)
- This session: config.json, decisions.md, sources/site/companies.json +
  lsip sidecars, wayback/roster/EDGAR sweeps, base + overlays, ledger,
  entities, excluded, review renders at checkpoints, report.md top.
- PRO-69 session: investor.json + sources sidecar, team.json +
  team-members.json, sources/edgar/fund-formds.json, report.md "## PRO-69"
  section. Their intel used here: scratch/lightspeed-formd-issuer-filings.json
  (112-filing Lightspeed*/Faction* enumeration → trap key + desk patterns),
  scratch/formd-2026q3-recent.json (2026q3 filings past the local zips:
  Platinum, AI Renaissance, HS Holdings, ST Holdings 2), cc outputs.

## Environment
- IA in partial recovery all session: CDX queries intermittently refuse
  (rc 6/7/22/28) or serve "Temporarily Offline"; replay fetches reliable.
  Worked around by replay-driven year fetches into wayback-pull's own
  raw/parsed shapes (idempotent convergence; .ts sidecars carry true
  snapshot timestamps).
- Common Crawl layer run by the PRO-69 session (their background):
  cc-people.json 229 slugs, parsed/ per-company years 2013–2017 +
  2023–2026. wayback-pull.py now MERGES parsed year files (keyed
  slug+path) so the two capture universes survive each other's re-runs.

## Site facts pinned at kickoff
- lsvp.com/companies: 666 cards, data-investor lsvp 570 / both 31 /
  lsip 65 (identical on /companies-india/). The attribute is NEW
  (absent from the 2026-01 archive snapshot): archived eras filter by
  card link target (lsvp.com vs lsip.com) instead.
- Team page: 103 profiles (46 Investors / 24 VOP / 33 Specialists),
  server-side ?firm=lsip variant → 20 LSIP people (2 overlap).
- /legal/: no marketing-rule investment list exists (coverage caveat, as
  Accel). Per-company pages carry no deal-partner attribution.
- lsvp.com was PARKED until ~2011 (domainsponsor); the firm's
  2000–2012 site was lightspeedvp.com (portfolio: pal.asp 2000–01,
  current.asp+history.asp 2002–06, /Portfolio/Default.aspx 2007–11).

## Registry judgments (agent, document-anchored, for Erik's sampling)
- LS SPV Management, LLC (CIK 1978139) and Venture Investors General
  Partner LLC (CIK 1366017): cofiler-closure entities initially desked
  external; both file Forms 3/4 from 2200 Sand Hill Road, Menlo Park
  (submissions API) → own management vehicles, desk us, confirmed:true.
  Venture Investors GP filed since 2006-09 — it carries pre-2012
  board-seat evidence the roster window (2012+) misses.
- COGAN GILL (CIK 1116231): founding partner (2000–~2005, later Opus
  Capital), not roster-resolvable (roster coverage starts 2012) → desk
  external stands; his post-departure seats are Opus's, pre-2005 deals
  ride the lightspeedvp.com listings.
- Dasilva Dax = Lightspeed Commerce founder; institutional co-filers
  (BlackRock, FMR, FIL, CDPQ, Capital International) external as usual.

## Sweep shape (233-name roster, 75 zips 2008q1–2026q2)
1,395 accessions / 796 issuers / 429 pooled. Big homonym clusters to
grind: "Mark Anderson" (172), "John Thompson" (125 — John W. Thompson
IS a Lightspeed venture-partner-era figure: genuine Rubrik-class seats
mixed with personal ones), Brian Kelly (61), David Chen (46),
Paul/Pauline Murphy (50/30), Adam Smith (23), Gaurav Gupta (20),
Jack Thompson (18). Bejul Somaia (27) is LSIP-boundary evidence.

## Known debts (to report.md if unresolved at close)
- Roster tenure coverage starts 2012 (/team/ era); 2000–2011 partners
  (Cogan, Showalter, early-era) are not sweep targets — era covered by
  the firm's own listings + Venture Investors GP filings; Form D zips
  start 2008 anyway.
- Local Form D zips end 2026q2; 2026q3 filings only via the peer's
  formd-2026q3-recent.json (recall-probe input).
- 2013–2018 lsvp.com listing pages barely archived (site was
  per-company-page WP; CC carries 2013–2017 /company/ pages instead).
