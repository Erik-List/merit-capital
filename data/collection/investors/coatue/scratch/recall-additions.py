#!/usr/bin/env python3
"""Recall probe outcome (2026-09-27): four additions into the ledger, every other candidate rejected with its reason in sources/web/recall-probe.json."""
import json
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
ADDS = [
 {"name": "Lunchclub", "slug": "lunchclub", "first_seen": "2020", "on_site_now": False, "sector": "Consumer", "source": "recall probe: Wikipedia insource sweep, read against the press",
  "citation": "https://www.cnbc.com/2020/09/01/lunchclub-tops-100-million-valuation-amid-quarantine-usage-spike.html",
  "basis": "Coatue co-led Lunchclub's $24.2M Series A with Lightspeed in 2020 (CNBC, 2020-09-01). The company is on no capture of the firm's portfolio page and files no Form D with a Coatue person, so no list layer could see it."},
 {"name": "Wolt", "slug": "wolt", "first_seen": "2021", "on_site_now": False, "sector": "Marketplaces", "source": "recall probe: Wikipedia insource sweep, read against the company's own release",
  "citation": "https://press.wolt.com/en-WW/196005-wolt-closes-530-million-financing-round-to-continue-expanding-beyond-the-restaurant/",
  "basis": "Wolt's own release of January 2021 names Coatue as a new investor in its $530M round led by ICONIQ Growth. A Finnish issuer with no US filing, sold to DoorDash in 2022 and absent from the firm's page."},
 {"name": "Syrn", "slug": "syrn", "first_seen": "2025", "on_site_now": False, "sector": "Consumer", "source": "recall probe: Wikipedia insource sweep, read against the press",
  "citation": "https://www.marieclaire.com/fashion/sydney-sweeney-syrn-lingerie-brand-launch/",
  "basis": "Press reports Coatue's backing of Syrn, the lingerie brand launched in January 2026 (Marie Claire, citing Puck's report of July 2025). No round or amount is named; the company is absent from the firm's page."},
 {"name": "Firmus", "slug": "firmus", "first_seen": "2026", "on_site_now": False, "sector": "AI Infrastructure", "source": "recall probe: EDGAR full-text sweep (Nomura 6-K of 2026-08-03 names the raise), read against the company's own release",
  "citation": "https://firmus.co/newsroom/firmus-raises-usdusd505-million-in-strategic-equity-investment-led-by-coatue",
  "basis": "Coatue led Firmus's USD 505M equity round of April 2026 at a USD 5.5B post-money valuation (the company's own release). An Australian issuer with no US filing; the deal is newer than the firm's page."},
]
lp = INV / "companies/membership-ledger.json"; L = json.load(open(lp)); b = L["coatue"]
have = {a["slug"] for a in b.get("recall_additions", [])}
b.setdefault("recall_additions", []).extend(a for a in ADDS if a["slug"] not in have)
lp.write_text(json.dumps(L, indent=1, sort_keys=True) + "\n")
PROBE = {
 "_readme": "Coatue recall probe (COLLECTION.md 3), 2026-09-27. Sources independent of the base: the EDGAR full-text sweep (sources/edgar/fts-hits.json, 1,111 registrants), the Wikipedia insource sweep (97 articles, 18 company candidates), a parametric list of about 55 well-known late-stage deals by era and sector, and press searches for rounds led by the firm in 2026. Each candidate is added as a ledger recall addition with its citation, or rejected here with its reason. 'Not found' means no page that could be opened names the firm in a round; most candidates had one or two round announcements opened, not every round.",
 "asof": "2026-09-27",
 "added": [a["name"] for a in ADDS],
 "already_rows": "Of the full-text registrants that are operating companies, every one that shows a fund position was already a base row under its brand name (for example Iambic, Singular Genomics, Anaplan, Kalshi, Grab, Nextdoor, Webull, DiDi, Rivian, Chime, Blend, Root, Dingdong, BOSS Zhipin, Uplight, Valsoft). Lightfield, which raised a Series A on 2026-09-09 with Coatue taking part, is the base row Tome under its new name.",
 "full_text_families": {"registered funds that hold a Coatue fund or name the firm": 162, "own vehicles and related persons, exemptive applications and other forms": 743, "Schedule 13D/G only": 53, "offering documents": 80, "periodic reports and proxies": 73},
 "rejected": {
  "PIPE bought at a SPAC merger: the position is entered at the listing, so it fails T3 (the class is an open ruling, R1)": [
   "SoFi (Coatue US 35 LLC, 5,000,000 shares registered for resale; PIPE signed 2021-01-07)", "Payoneer (Coatue FinTech Fund I, 1,200,000 shares; the table does not label them, the PIPE reading is inferred)",
   "Sunlight Financial (Coatue US 37 LLC, 3,000,000 shares, listed under 'PIPE Investors')", "CCC Intelligent Solutions (Coatue FinTech Fund I, 500,000 shares 'acquired in the PIPE Financing')",
   "Apex Fintech Solutions (PIPE commitment announced 2021-02-22 with Northern Star II; no closing found in the filings)"],
  "Listed position of the hedge fund vehicles (decisions.md D3)": [
   "SK hynix (non-binding indication of interest in the 2026 ADS offering)", "Forgent Power Solutions (Schedule 13G, 7.5% at 2026-06-30)", "Hut 8 (convertible investment in a listed company; already a base row, not_member)",
   "Liberty Broadband / Charter / Time Warner Cable (Coatue Offshore Master Fund in the 2015 investment agreements)", "Virgin Media (5% holder table, 2013)", "Bankrate (public holder objecting to the 2010 settlement)",
   "Lawson Software and Sohu (Schedule 13G)", "Autobytel and Loudeye (selling holders in registered resales of listed shares, 2003-2004)", "Peapod (holder list in the 2001 tender offer)"],
  "Director, officer or employee biography: a person's past or present post, no fund position (T4)": [
   "King Digital", "Missfresh", "PureCycle / Roth CH Acquisition I", "Aeva", "Vertical Aerospace", "Digimarc / Deschutes Parent", "Soho House", "Elastic", "Zendesk", "Impinj", "One Liberty Properties", "Hertz", "DigitalBridge",
   "Stonepeak-Plus Infrastructure Fund", "Michaels / Magic MergeCo", "JA Solar", "Daqo New Energy", "Longhai Steel", "Jeneration Acquisition", "Stillwater Growth", "Cano Health (names OneTrust, a base row, as Coatue-backed)"],
  "A different Coatue: Coatue Corporation, the memory company AMD bought in 2003": ["Zafgen", "Coskata", "Spansion", "Surfect Holdings", "NVE", "Advanced Micro Devices"],
  "The firm named with no position in the registrant": [
   "Walmart (TikTok Global education initiative)", "Applied Digital (chart source credit)", "Sonendo (Coatue Structured Fund AIV is on the purchaser side, Valsoft, a base row)", "AES (the round is Uplight's, a base row)",
   "GDS Holdings (the round is DayOne's, a base row)", "Core Scientific (names the firm's CoreWeave lock-up; CoreWeave is a base row)", "Gryphon Digital Mining (interview about Hut 8)", "Enlivex (names the Kalshi round; Kalshi is a base row)",
   "Nomura (league-table credit for the Firmus raise; Firmus added)", "HealthCor Catalio Acquisition (names the firm as a partner in Catalio's general partner, not a holder of Hyperfine)", "Target Global Acquisition I (names the Rapyd round; Rapyd is a base row)",
   "GSV Capital / Sutter Rock (name the Lyft and Lime rounds; both base rows)", "SK Growth Opportunities (names the firm as a Webull holder; Webull is a base row)", "Khosla Ventures Acquisition II (Nextdoor's 2014 management rights letter; Nextdoor is a base row)",
   "Altimeter Growth (Grab's holders; Grab is a base row)", "Tata Motors and ICICI Bank (investor-meeting lists)", "Sculptor Capital (peer list)", "commercial mortgage trusts (the firm is a tenant at 9 West 57th Street)"],
  "Own vehicles the name scan could not see, recorded for the vehicle layer": ["Green Deer Holdings LLC (Form D 2017)", "Green Ox Holdings II LLC (Form D 2025)"],
  "Sale consideration, not a purchase": ["Getir (Coatue received Getir stock as a Gorillas holder in 2022; Gorillas is the base row)"],
  "No page that could be opened names the firm in a round (well-known deals checked by name)": [
   "commercetools (the Wikipedia mention is the title of an article about Commerce Layer, a base row)", "Bolt", "Kavak", "Rappi", "Clubhouse", "Meesho", "Pipe", "Hopper", "Airwallex", "Character.AI", "Perplexity", "Lambda", "Crusoe", "Helion", "Waymo", "Wiz",
   "Snorkel AI", "Byju's (one search summary claims a 2019 round; no page confirms it)", "Unacademy", "Cityblock Health", "Ro", "Noom", "Affirm", "Datadog", "Li Auto", "RLX Technology", "Flink", "Zepto", "Glovo", "Bird",
   "Instabase (a partner's board seat from her time at Index)", "Benchling", "Articulate", "Paystack", "Flutterwave", "Razorpay (talks reported in 2021, no round)", "Groww (talks only)", "Urban Company", "Pony.ai", "WeRide", "Horizon Robotics",
   "Black Sesame", "Momenta", "Hesai", "Mistral AI", "Physical Intelligence", "World Labs", "Sierra (the firm lists Sierra Space, a different company)", "Abnormal Security", "Vanta", "Verkada"]},
 "notes": ["The research agent's web search allowance ran out in its second pass, so about half of the well-known deals had one search pass and Li Auto and RLX had only the EDGAR check.",
           "Glean was skipped in the press check because it is already a base row."]
}
(INV / "sources/web/recall-probe.json").write_text(json.dumps(PROBE, indent=1, ensure_ascii=False) + "\n")
print("recall additions:", [a["slug"] for a in b["recall_additions"]], "| rejected:", sum(len(v) for v in PROBE["rejected"].values()))
