#!/usr/bin/env python3
"""Write the researched fields of the firm profile (COLLECTION.md s11) into investor/investor.json and
investor/sources.json. scripts/build-firm-profile.py then recomputes hq_location, individuals and the focus list and
validates the rest. Every URL is read from a file on disk (the firm's posts, the archived news, scratch/web-finds.json).
Run after the base has landed: the notable picks are asserted against the ledger here too."""
import json, statistics
from datetime import datetime, timezone
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent
P = json.loads((R / "sources/site/perspectives.json").read_text())["rows"]
def post(sub):
    h = [r["url"] for r in P if sub in r["slug"]]; assert len(h) == 1, (sub, h); return h[0]
NA = json.loads((R / "sources/wayback/news-archive.json").read_text()); NA = NA["rows"] if isinstance(NA, dict) else NA
def narch(sub):
    h = [r["capture_url"] for r in NA if sub in (r.get("title") or "")]; assert len(set(h)) == 1, (sub, h); return h[0]
W = json.loads((H / "web-finds.json").read_text()); web = lambda k: W[k]["url"]
ADV = json.loads((R / "sources/registers/adv-7b-funds.json").read_text())
own = [f for f in ADV["funds"] if f["reported_by"] == "161175"]
aum = sum(f["gav"] for f in own); assert all(f["gav"] for f in own) and len(own) == 32, len(own)
led = json.loads((R / "companies/membership-ledger.json").read_text())["index-ventures"]["verdicts"]
cl = json.loads((R / "companies/classification.json").read_text())
base = json.loads((R / "companies/base.json").read_text()); base = base["companies"] if isinstance(base, dict) else base
live = {b["slug"] for b in base}

NOTABLE = [("Skype", "skype"), ("Dropbox", "dropbox"), ("Slack", "slack"), ("Discord", "discord"), ("Roblox", "roblox")]
for n, s in NOTABLE: assert s in live and led[s]["verdict"] == "member", s

# entry rounds the firm announced or was reported in, with a size: the earliest sized round each company's record ties the firm to
sizes = {}
for s, v in cl.items():
    if s not in live or (led.get(s) or {}).get("verdict") != "member": continue
    fr = sorted([r for r in (v.get("funding_rounds") or []) if r.get("firm_in_round") and r.get("amount_usd")], key=lambda r: str(r.get("date") or ""))
    if fr and v.get("entry_stage") in ("Seed", "Pre-Seed", "Series A", "Growth"): sizes[s] = (v["entry_stage"], fr[0]["amount_usd"], fr[0]["date"])
med = statistics.median(x[1] for x in sizes.values())
by = {st: statistics.median([x[1] for x in sizes.values() if x[0] == st]) for st in ("Seed", "Series A", "Growth")}
n_by = {st: sum(1 for x in sizes.values() if x[0] == st) for st in by}
(H / "entry-round-sizes.json").write_text(json.dumps({"_readme": "The earliest sized round each member's funding_rounds ties the firm to (firm_in_round), by entry stage; the median is the profile's investment_range.median. Written by scratch/profile-data.py.",
    "median_usd": med, "by_stage": by, "n_by_stage": n_by, "rows": {s: {"entry_stage": a, "amount_usd": b, "date": c} for s, (a, b, c) in sorted(sizes.items())}}, indent=1) + "\n")
median = int(round(med / 1e6) * 1e6)

THESIS = "“We invest in who you are, not just what you do.”"
HISTORY = ("Index Ventures was founded in Geneva in 1996 by Neil Rimer, David Rimer and Giuseppe Zocco, out of a family bond trading firm. "
           "It became known for early bets on Skype, MySQL, Dropbox, Adyen, Figma, Revolut and Wiz, and opened offices in London in 2002, San Francisco in 2011 and New York in 2022. "
           "In July 2026 it announced new seed, venture and growth funds that bring its investing capital to $3.5 billion.")
FUNDS = [("Index Ventures XIII", 900000000, 2026), ("Index Origin III", 400000000, 2026), ("Index Ventures Growth VII", 2200000000, 2024),
         ("Index Ventures XII", 800000000, 2024), ("Index Origin II", 300000000, 2022), ("Index Ventures Growth VI", 2000000000, 2021),
         ("Index Ventures XI", 900000000, 2021), ("Index Origin I", 200000000, 2021), ("Index Ventures Growth V", 1200000000, 2020),
         ("Index Ventures X", 800000000, 2020), ("Index Ventures Growth IV", 1000000000, 2018), ("Index Ventures IX", 650000000, 2018),
         ("Index Ventures VIII", 550000000, 2016), ("Index Ventures Growth III", 700000000, 2015), ("Index Ventures VII", 541880000, 2014),
         ("Index Ventures VI", 441630000, 2012), ("Index Ventures V", 441525000, 2009)]
funds = [{"name": n, "size": s, "vintage": y} for n, s, y in FUNDS]
p30 = post("30-years-in-perfecting-our-craft"); p24 = post("index-launches-23bn-in-new-funds"); p21 = post("index-raises-31-billion")
p16 = post("new-partners-and-125b"); p20 = post("announces-2bn-new-funds"); po2 = post("announcing-index-origin-ii"); pny = post("index-ny-announcing-our-new-office")
inv = {
 "slug": "index-ventures", "name": "Index Ventures", "investor_type": "Institutional", "website": "https://www.indexventures.com",
 "icon_url": "data/collection/investors/index-ventures/sources/site/icon-mark.svg", "hq_location": None, "founding_year": 1996,
 "history": HISTORY, "investment_concept": THESIS, "investment_stage": ["Seed", "Series A", "Growth"],
 "investment_geo": {"core": ["Europe", "US"], "other": ["Israel"]}, "investment_scope": {"type": "Generalist", "focus": []},
 "investment_range": {"lower_limit": 1000000, "median": median, "upper_limit": 300000000},
 "notable_investments": [n for n, _ in NOTABLE], "aum": {"bottom": aum, "top": aum}, "funds": {"funds": funds}, "individuals": [],
 "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat()}
F = {
 "name": {"value": inv["name"], "source": "https://www.indexventures.com/", "basis": "the firm's site. Adviser: Index Ventures SA, Geneva, an SEC exempt reporting adviser (CRD 161175); the funds are Jersey and Delaware limited partnerships (decisions.md D1, D2). The life sciences practice became Medicxi in February 2016 and its companies are outside the portfolio on this page (decisions.md D3)."},
 "website": {"value": inv["website"], "source": "https://www.indexventures.com/", "basis": "firm site (Wagtail; portfolio at /companies, posts at /perspectives, team at /team)"},
 "icon_url": {"value": inv["icon_url"], "source": "https://www.indexventures.com/static/images/safari-pinned-tab.394df958a54e.svg", "basis": "the site's own vector mark (the hand; <link rel=mask-icon>, 256x256 intrinsic), chosen by --discover on 2026-10-06 over the 180x180 touch icon (would be enlarged) and the 32x32 favicons. A mask icon is black by convention; the file kept at sources/site/icon-mark.svg carries the colour the same tag declares (color=\"#e1251b\"), which is the red of the site's touch icon. White plate synthesized by the normalizer; dry run: contrast 4.4:1, ramp 0.48 px, artwork inside the keyline. The bucket URL replaces this value at the ingest."},
 "founding_year": {"value": 1996, "source": web("wikipedia-index"), "basis": "'Index Ventures was officially founded in Geneva in 1996 by Neil Rimer, David Rimer and Giuseppe Zocco' (Wikipedia, read 2026-10-06); the firm's own post of 2026-07-31 is titled '30 Years In'. Its roots are older: Index Securities, a Geneva bond trading firm founded by Gerald Rimer in 1976, and the investments its team made before the first fund (decisions.md R2)."},
 "history": {"value": HISTORY, "source": web("wikipedia-index"), "basis": f"founding, founders and the bond trading firm: Wikipedia (read 2026-10-06) and the firm's post '30 Years In' ({p30}); offices: 'Danny Rimer, who opened Index's London office in 2002 and its San Francisco base in 2011' (the firm's post of 2016-02-03, {p16}) and the New York announcement of 2022-05-05 ({pny}); the named bets are portfolio companies on this page; 2026 funds: 'bringing our total investing capital to $3.5 billion across all stages', a $400 million seed fund, a $900 million venture fund and a growth fund raised to $2.2 billion ({p30}). Moved here from the page: the fund ladder; the life sciences practice that became Medicxi in 2016 and is not part of the portfolio shown; the firm's own count of 2024, '108 Index-backed startups ... reach a $1 billion valuation, 23 have surpassed a $10 billion valuation, and 57 went on to be publicly traded' ({p24})."},
 "investment_concept": {"value": THESIS, "source": "https://www.indexventures.com/", "basis": "The firm's own statement, verbatim from the homepage headline (h1), read 2026-10-06. A closing period is already there; straight quotes are the only edit. The competing line is the meta description ('Partnering with exceptional entrepreneurs from SF to NY, London to Tel Aviv, from Seed to IPO.'), not used. Published inside quotation marks, as the firm's own words (Erik, 2026-09-26)."},
 "investment_stage": {"value": inv["investment_stage"], "source": "https://www.indexventures.com/", "basis": "the firm's own words: 'from Seed to IPO' (homepage meta description) and 'seed, venture, and growth' funds (post of 2026-07-31); the landed entry-stage distribution is restated in report.md"},
 "investment_geo": {"value": inv["investment_geo"], "source": "https://www.indexventures.com/", "basis": "the firm's own words: 'from SF to NY, London to Tel Aviv' (homepage meta description) and 'offices in San Francisco, London, and New York, plus partners on the ground in Berlin and Tel Aviv' (post of 2024-07-10); the list's own region filter is Europe and North America. Core Europe and US (two-label cap), other Israel; the landed country distribution is restated in report.md"},
 "investment_scope": {"value": inv["investment_scope"], "source": "companies/classification.json", "basis": "type: the firm's own homepage lists eight sectors it backs; focus: recomputed by build-firm-profile.py"},
 "investment_range": {"value": inv["investment_range"], "source": "scratch/entry-round-sizes.json", "basis": f"median: ${med/1e6:.1f}M, the median of the earliest sized round that each of {len(sizes)} portfolio companies' records tie the firm to (the firm's own posts and archived news, company releases and press; rows in scratch/entry-round-sizes.json; by stage Seed ${by['Seed']/1e6:.1f}M over {n_by['Seed']}, Series A ${by['Series A']/1e6:.1f}M over {n_by['Series A']}, Growth ${by['Growth']/1e6:.1f}M over {n_by['Growth']}). It is a round size, not a cheque size. lower: documented seed entries of $1.3M to $1.5M (GroupSpaces 2010, Productboard 2016, Geckoboard 2012); upper: the $300M round the firm led in DeepL (its post of 2024-05-22)", "flags": ["median_press_based"]},
 "notable_investments": {"value": inv["notable_investments"], "source": "companies/base.csv", "basis": "The five best known of the firm's own companies, most recognised first (PRO-152, Erik 2026-09-24). Considered next: Revolut, Robinhood, Figma, Facebook (a late secondary purchase), Etsy, Deliveroo, Anthropic.", "slugs": [s for _, s in NOTABLE]},
 "aum": {"value": inv["aum"], "source": "https://adviserinfo.sec.gov/firm/summary/161175", "basis": f"both ends: the sworn Form ADV Section 7.B(1) gross asset values of the firm's exempt reporting adviser, Index Ventures SA, CRD 161175, annual amendment of 2026-03-31 (IAPD PDF parsed with pypdf, sources/registers/adv-7b-funds.json): 32 private funds, ${aum:,} in all. An exempt reporting adviser files no Item 5.F, so the 7.B composite is the sworn figure (Creandum precedent). It includes Index Ventures Life VI ($211,570,819), whose companies are outside the portfolio on this page (decisions.md D3), and predates the funds of July 2026. Medicxi's adviser (CRD 283504) is a separate firm and is not counted. Wikipedia gives EUR 11.7 billion (2025); the firm's posts state capital raised, not assets. Both belong here, not in the range.", "flags": ["era_7b_composite"]},
 "funds": {"value": funds, "source": p30, "basis": f"sizes from the firm's own announcements: XIII $900M, Origin III $400M and Growth VII raised from $1.5B to $2.2B ({p30}); XII $800M and Growth VII $1.5B ({p24}); XI $900M, Growth VI $2bn and Origin I $200M ({p21}); Origin II $300M ({po2}); VIII $550M and Growth III $700M ({p16}); the $2bn of 2020 ({p20}) splits into X $800M and Growth V $1.2B, and the $1.65B of 2018 into IX $650M and Growth IV $1B (TechCrunch, {web('funds-2020')} and {web('funds-2018')}); VII EUR 400M in June 2014 (Globes, 'Index Ventures raises $550m fund'; EUR 400.0M @ ECB 2014-06-11 = $541.9M); VI EUR 350M (the firm's own news item of 2012-06-18, {narch('350m fund to invest in early stage')}; @ ECB 2012-06-18 = $441.6M); V EUR 350M (the firm's own news item of 2009-03-03, {narch('Index Closes')}; @ ECB 2009-03-03 = $441.5M). No entry carries an accession: the funds file Form D at first close. Not listed, because no size was confirmed in this run: Index Ventures I to IV (1996 to 2007), Growth I (2008) and Growth II (2011). Counted here, not listed: the parallel and entrepreneur funds beside each main fund, Index SPV I and II, the Yucca co-investment vehicles, and Index Ventures Life VI (2012), the life sciences fund now sub-advised by Medicxi."},
}
src = {"slug": "index-ventures", "generated_at": inv["updated_at"], "run": "PRO-82", "fields": F}
(R / "investor").mkdir(exist_ok=True)
(R / "investor/investor.json").write_text(json.dumps(inv, indent=2, ensure_ascii=False) + "\n")
(R / "investor/sources.json").write_text(json.dumps(src, indent=2, ensure_ascii=False) + "\n")
print("history words", len(HISTORY.split()), "| thesis words", len(THESIS.split()), "| aum", f"{aum:,}", "| median", median, by, n_by)
