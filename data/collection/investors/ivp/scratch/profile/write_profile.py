"""Write IVP's researched profile (investor/investor.json + investor/sources.json)
for build-firm-profile.py to assemble around (COLLECTION.md 11). Values are
researched and cited here; hq_location, individuals and investment_scope.focus
are recomputed by the builder. Re-run after changing any value, then re-run
the builder."""
import json
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
REG = json.loads((INV / "sources/registers/adv-7b-funds.json").read_text())
AUM = REG["sum_gross_asset_value_usd"]
ICON = json.loads((INV / "scratch/profile/icon.json").read_text()) if (INV / "scratch/profile/icon.json").exists() else {}
SITE = "https://www.ivp.com"

history = ("IVP was founded in 1980 in Menlo Park by Reid Dennis as Institutional Venture Partners, "
           "and backs technology companies mostly at later stages. Its bets include Netflix, Twitter, "
           "Snap, Dropbox, Slack, CrowdStrike, Datadog, Coinbase and Anthropic. Its latest fund, "
           "IVP XVIII, raised $1.6 billion, and the firm counts more than 135 IPOs among some 400 companies.")
thesis = "“Supercharging growth.”"

def fund(name, size, vintage, note, source, accession=None):
    f = {"name": name, "size": size, "vintage": vintage, "sources": [{"source": source, "note": note}]}
    if accession: f["accession"] = accession
    return f
FD = "sources/edgar (own fund Form Ds, bulk zips)"
funds = [
    fund("Institutional Venture Partners XII, L.P.", 600000000, 2007,
         "Predates mandatory electronic Form D (2009), so no sworn amount exists (CIK 1402289). Size from the firm's own release 'Institutional Venture Partners Closes $600 Million Fund' (closed 2007-05-17, then the largest fund in its history).",
         "https://www.ivp.com/news/press-release/institutional-venture-partners-closes--600-million-fund/"),
    fund("Institutional Venture Partners XIII, L.P.", 750000000, 2010,
         "Form D/A 2010-06-30: amount sold $750,000,000 (the original Form D reported $600M); the oversubscribed $750M close was also reported in the press.", FD, "0001493922-10-000002"),
    fund("Institutional Venture Partners XIV, L.P.", 1000000000, 2012,
         "Form D 2012-06-14: total offering and amount sold both $1,000,000,000.", FD, "0001550180-12-000001"),
    fund("Institutional Venture Partners XV, L.P.", 1400000000, 2015,
         "Form D 2015-04-21: total offering and amount sold both $1,400,000,000.", FD, "0001640274-15-000001"),
    fund("Institutional Venture Partners XV Executive Fund, L.P.", 7600000, 2015,
         "Form D 2015-12-18: amount sold $7,600,000. Parallel executive fund of the same general partner.", FD, "0001661321-15-000001"),
    fund("Institutional Venture Partners XVI, L.P.", 1500000000, 2017,
         "Form D 2017-09-20: total offering and amount sold both $1,500,000,000.", FD, "0001716992-17-000001"),
    fund("IVP Executive Fund XVI, LLC", 20700000, 2017,
         "Form D 2017-09-20: amount sold $20,700,000. Parallel executive fund.", FD, "0001716965-17-000001"),
    fund("Institutional Venture Partners XVII, L.P.", 1800000000, 2020,
         "The 2020 Form D reports $0 sold at first filing and was never amended, so it carries no accession here; size from the close announced 2021-05-17 ('IVP Closes $1.8 Billion Fund to Back Later-Stage Growth Companies'), the largest in the firm's history at the time.",
         "https://www.businesswire.com/news/home/20211216006113/en/IVP-2021-in-Review-Breakout-Performance-with-15-IPOs-and-%241.8-Billion-Fund-to-Serve-Hypergrowth-Companies"),
    fund("IVP Executive Fund XVII, LLC", None, 2020,
         "Form D (2020) reports $0 sold and no amendment; no public size.", FD),
    fund("Institutional Venture Partners XVIII, L.P.", 1600000000, 2022,
         "Form D/A filed 2024 (first sale 2022-10-06): total offering and amount sold both $1,600,000,000.", FD, "0001931085-24-000001"),
    fund("Institutional Venture Partners XVIII-P, L.P.", None, 2023,
         "Form D (2023) reports $0 sold and no amendment; a parallel vehicle of Fund XVIII with no public size.", FD),
    fund("IVP Executive Fund XVIII, LLC", None, 2023,
         "Form D (2023) reports $0 sold and no amendment; no public size.", FD),
]
row = {
    "slug": "ivp",
    "name": "IVP",
    "investor_type": "Institutional",
    "website": SITE,
    "icon_url": ICON.get("icon_url"),
    "hq_location": None,
    "founding_year": 1980,
    "history": history,
    "investment_concept": thesis,
    "investment_stage": ["Series A", "Growth"],
    "investment_geo": {"core": ["US"], "other": ["Europe", "Israel"]},
    "investment_scope": {"type": "Generalist", "focus": ["SaaS", "Data Infrastructure", "Consumer & Marketplaces", "Healthcare & Bio", "AI & Applied AI", "Fintech & Payments"]},
    "investment_range": {"lower_limit": 6000000, "median": 31000000, "upper_limit": 200000000},
    "notable_investments": ["Netflix", "Twitter", "Uber", "Snap", "Dropbox"],
    "aum": {"bottom": AUM, "top": AUM},
    "funds": {"funds": funds},
    "individuals": [],
    "updated_at": None,
}
advisers = "; ".join(f"{a['adviser']} (CRD {c}) {len(a['funds_7b1'])} funds" for c, a in REG["advisers"].items() if a["funds_7b1"])
F = {
 "name": {"value": "IVP", "source": SITE, "basis": "The firm's own brand on its site and title tag ('IVP: Venture capital for the Exceptional'); the legal family name is Institutional Venture Partners, which the funds still carry."},
 "website": {"value": SITE, "source": SITE, "basis": "The firm's own site."},
 "icon_url": {"value": row["icon_url"], "source": "https://www.ivp.com/favicons/android-chrome-512x512.png",
              "basis": ICON.get("basis", "Chosen by --discover: the 512x512 android-chrome PNG is the firm's own mark on its own navy plate; the vector mask icon is a one-colour silhouette. Upload waits for Erik's ingest approval; the URL is the content-hash path the upload will write."),
              **({"provenance": ICON["provenance"]} if ICON.get("provenance") else {})},
 "founding_year": {"value": 1980, "source": "https://en.wikipedia.org/wiki/Institutional_Venture_Partners",
                   "basis": "Founded 1980 by Reid Dennis, out of Institutional Venture Associates (1974, Dennis and Burton McMurtry), which split into IVP and Technology Venture Investors that year (decisions.md D4). The site's 'five decades of experience' counts from 1974."},
 "history": {"value": history, "source": "https://en.wikipedia.org/wiki/Institutional_Venture_Partners",
             "basis": "Founding year, city and founder from the firm's own lineage (decisions.md D4) and its Menlo Park office on every ADV; the bets are portfolio rows on this page (Netflix, Twitter, Snap, Dropbox, Slack, CrowdStrike, Datadog, Coinbase, Anthropic); Fund XVIII's $1.6B is its own Form D/A; '400 companies, 135+ IPOs' is the firm's own homepage text (read 2026-09-26). Moved to the sidecar, not the page: the fund ladder (XII $600M 2007 through XVIII), IVP XVII's $1.8B close (2021), and the 1999 departure of Geoff Yang, Tom Dyal and John Walecka to found Redpoint."},
 "investment_concept": {"value": thesis, "source": SITE,
                        "basis": "The firm's own statement, verbatim from the homepage headline ('Supercharging Growth', read 2026-09-26); sentence case and a closing period are the only edits. Competing lines on the same page: the title tag 'IVP: Venture capital for the Exceptional' and the meta description 'Over four decades, IVP has accelerated 400 breakout companies to breakthrough impact.' The rule takes the homepage headline first (COLLECTION.md 11)."},
 "investment_stage": {"value": row["investment_stage"], "source": "companies/base.csv",
                      "basis": "DERIVED: the firm publishes no stage filter; it calls itself a later-stage venture and growth equity investor ('our work begins at critical stages of inflection'). Landed entry stages over the 168 rows whose round is known: Growth 156 (93%), Series A 12 (7%), most of the Series A entries since 2022 (Jasper, Roam, Numeric, Accompany Health, Wonderful, Venice). 129 older rows carry no named round."},
 "investment_geo": {"value": row["investment_geo"], "source": "companies/base.csv",
                    "basis": "Landed hq_country over 297 rows: US 271 (91%), Europe 20 (UK 5, Finland 3, Germany 3, Netherlands 2, Sweden 2, France 2, Ireland, Estonia, Turkey), Israel 2, and one each in Indonesia, Australia, Canada and the Bahamas (FTX). Core is the US; Europe and Israel are the recurring other markets (IVP runs a London office, Institutional Venture Partners UK LLP)."},
 "investment_range": {"value": row["investment_range"], "source": "sources/edgar/formd-issuer-rounds.json",
                      "basis": "MEDIAN: the Form D entry-round distribution over the 39 portfolio rows whose first IVP round is on EDGAR: median $30.7M, p25 $15.5M, p75 $55.0M, published as $31M. It is a ROUND-SIZE PROXY for check size, fair only in part here: IVP leads many of its rounds but syndicates the large ones, and Form D coverage starts in 2009. LOWER LIMIT: $6M, the tenth percentile of those entry rounds (IVP runs no seed programme). UPPER LIMIT: $200M, an 11% single-position concentration of the largest fund (IVP XVII, $1.8B), cross-checked against rounds IVP led or co-led (Rubrik $180M Series D, CrowdStrike $200M Series E) and its 2020 Robinhood investment, 'the biggest single investment in the history of our firm'. Aggregator 'typical check' figures were rejected."},
 "notable_investments": {"value": row["notable_investments"], "source": "companies/base.csv",
                         "basis": "The five best known of the firm's companies, most recognised first (PRO-152, Erik 2026-09-24). Also considered: Anthropic, Slack, Coinbase, Discord, Robinhood, CrowdStrike and Datadog.",
                         "slugs": ["netflix", "twitter", "uber", "snap", "dropbox"]},
 "aum": {"value": row["aum"], "source": "sources/registers/adv-7b-funds.json",
         "basis": f"IVP is ERA-only: one exempt reporting adviser per fund general partner, no Item 5.F regulatory AUM. The sworn substitute is Schedule D Section 7.B.(1) current gross asset value, summed over the five active advisers' annual amendments filed 2026-03-28 ({advisers}): 17 private funds, deduped by private fund ID (no overlap), ${AUM:,}. Institutional Venture Partners UK LLP (CRD 329558) reports the same funds under 7.B.(2) as a sub-adviser and adds nothing. Both range ends are that number: press and vendor 'AUM' figures ($7B to $8B, 2026) sit below the sworn floor and belong in this flag, and the 2021 release's '$8.7 billion of committed capital' is cumulative commitments, not assets. PDFs: https://reports.adviserinfo.sec.gov/reports/ADV/<CRD>/PDF/<CRD>.pdf."},
 "funds": {"value": funds, "source": "sources/edgar (own fund Form Ds)",
           "basis": "Main funds XII to XVIII and their parallel executive and P vehicles. Counted here, not listed: the single-purpose co-investment vehicles IVP XVII-A to XVII-G (2021 to 2026, $10M to $60M each) and IVP XVIII-A (2026), and Bow Tie Angels - A, L.P. ($2.8M, 2023), all funds of the same advisers (decisions.md D3). Earlier funds IVP I (1980) to XI appear on EDGAR only through Section 16 and 13D/G filings (IVP III onward, CIK 767841 and later) with no sworn or published sizes. External and not IVP's: Goldman Sachs' 'Institutional Venture Partners XVIII Access LLC' and 'XIX Access' feeders (200 West Street), and Insight Venture Partners' 'IVP (Venice)' and 'IVP CIF' vehicles (decisions.md D1). A Fund XIX was reported in 2026 press as being raised ($1.8B target); it has no close on record and is not listed."},
}
(INV / "investor").mkdir(exist_ok=True)
(INV / "investor/investor.json").write_text(json.dumps(row, indent=1, ensure_ascii=False) + "\n")
(INV / "investor/sources.json").write_text(json.dumps({"slug": "ivp", "run": "PRO-92", "generated_at": None, "fields": F}, indent=1, ensure_ascii=False) + "\n")
print("aum", AUM, "funds", len(funds), "icon", row["icon_url"])
