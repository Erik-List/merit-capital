#!/usr/bin/env python3
"""Write Ribbit Capital's firm profile (COLLECTION.md s11): investor/investor.json and investor/sources.json, one
provenance entry per field. The distributions behind stage, geo, scope and range are computed from the landed base
at run time (scratch/entry-rounds.py first), so a re-run after a rebuild restates them. hq_location and individuals
are then written by scripts/firm-offices.py and scripts/build-firm-profile.py; scratch/patch-profile.py adds the
titles note to the individuals basis the build writes.

Usage: python3 scratch/entry-rounds.py && python3 scratch/write-profile.py
"""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
ADV = "https://reports.adviserinfo.sec.gov/reports/ADV/165308/PDF/165308.pdf"
IAPD = "https://adviserinfo.sec.gov/firm/summary/165308"
LAVCA = "https://www.lavca.org/ribbit-capital-debuts-with-100m-early-stage-fund/"
EDGAR = "https://www.sec.gov/Archives/edgar/data/{}/{}/{}-index.htm"


def formd(cik, acc):
    return EDGAR.format(cik, acc.replace("-", ""), acc)


# ---- the landed base: members and their distributions
cls = json.loads((INV / "companies/classification.json").read_text())
res = json.loads((INV / "companies/resolved.json").read_text())
led = json.loads((INV / "companies/membership-ledger.json").read_text())
base = json.loads((INV / "companies/base.json").read_text())
verd = (led.get("ribbit-capital") or led).get("verdicts", {})
members = [r["slug"] for r in base if verd.get(r["slug"], {}).get("verdict") == "member"
           or (r.get("status") == "auto_confirmed" and r["slug"] not in verd)]
members = [s for s in members if s != "ibod-company-inc"]
M = len(members)


def col(s, k):
    return cls.get(s, {}).get(k) or res.get(s, {}).get(k)


geo = Counter(col(s, "hq_country") or "?" for s in members)
stage = Counter(col(s, "entry_stage") or "undetermined" for s in members)
focus = Counter(cls.get(s, {}).get("focus") or "?" for s in members)
REGION = {"Europe": ["GB", "FR", "DE", "PT", "IE", "ES", "IT", "NL", "SE", "CH", "PL", "EE", "LT", "DK", "FI", "NO", "BE", "AT"],
          "Latin America": ["BR", "MX", "CL", "AR", "CO", "PE", "UY"],
          "Asia": ["CN", "ID", "SG", "PH", "HK", "KR", "JP", "VN", "MY", "TH"]}
reg = {k: sum(geo[c] for c in v) for k, v in REGION.items()}
er = json.loads((INV / "scratch/entry-rounds.json").read_text())["summary"]
rng = {"lower_limit": round(er["p10"] / 1e6) * 1_000_000, "median": round(er["median"] / 1e6) * 1_000_000,
       "upper_limit": round(er["p90"] / 1e6) * 1_000_000}
FOCUS_MIN = json.loads((INV / "config.json").read_text())["profile"]["focus_min_companies"]
focus_pub = [f for f, c in focus.most_common() if f != "?" and c >= FOCUS_MIN]
fintech_share = (focus["Fintech & Payments"] + focus["Crypto & Web3"]) / M


def fmt(c, keys):
    return ", ".join(f"{k} {c[k]}" for k in keys if c.get(k))


# ---- the reader-facing copy (COLLECTION.md s11 shape: thesis quoted, history 40-80 words, 3 sentences)
thesis = "“The future belongs to the rebels.”"
history = ("Ribbit Capital was founded in Palo Alto in 2012 by Micky Malka, an entrepreneur who had started five "
           "financial companies, with a $100 million first fund. It became known for bets on Coinbase, Robinhood, "
           "Credit Karma, Nubank and Revolut. It manages about $21 billion, and its latest fund, Ribbit Capital Z, "
           "raised $562 million in 2026.")

# ---- funds: flagship and growth lines, newest first. An entry with an accession is asserted against that
# filing's sold amount by build-firm-profile.py; funds whose Form D reports $0 sold carry the offering amount
# (or the press size) and no accession.
funds = [
    {"name": "Ribbit Capital Z, L.P.", "size": 561860000, "vintage": 2026, "accession": "0001315863-26-000403",
     "sources": [{"source": formd(2107959, "0001315863-26-000403"),
                  "note": "Form D/A 2026 Q2: $561,860,000 sold of a $565,000,000 offering, first sale 2026-02-12 (the first "
                          "filing, 0001315863-26-000144, offered $500,000,000 with $0 sold)."}]},
    {"name": "Leapfrog Capital, L.P.", "size": 331535070, "vintage": 2025, "accession": "0002063407-25-000034",
     "sources": [{"source": formd(2072275, "0002063407-25-000034"),
                  "note": "Form D/A 2025 Q3: $331,535,070 sold, equal to the offering, first sale 2025-07-01; a Cayman venture "
                          "fund at the firm's Palo Alto office (364 University Avenue) with Meyer Malka its related person. "
                          "The first filing (0002063407-25-000012) offered $300,000,000."},
                 {"source": "https://pitchbook.com/news/articles/fintech-vc-firm-ribbit-capital-raising-300m-opportunistic-fund-leapfrog",
                  "note": "PitchBook: 'Fintech VC firm Ribbit Capital is raising a new $300M opportunistic fund' (Leapfrog)."}]},
    {"name": "Ribbit Bullfrog III, L.P.", "size": 650000000, "vintage": 2025,
     "sources": [{"source": formd(2059489, "0001315863-25-000242"),
                  "note": "Form D 2025 Q1: total offering $650,000,000, $0 sold at filing, no amendment on EDGAR through 2026 "
                          "Q2; the offering amount is published (no accession asserted). The Form ADV of 2026-03-30 lists the "
                          "fund; its gross asset value there is a current value, not a size."}]},
    {"name": "Ribbit Capital Y, L.P.", "size": 500000000, "vintage": 2025,
     "sources": [{"source": formd(2059488, "0001315863-25-000241"),
                  "note": "Form D 2025 Q1: total offering $500,000,000, $0 sold at filing."},
                 {"source": "https://techcrunch.com/2025/03/19/in-another-good-sign-for-fintech-ribbit-capital-is-raising-a-new-500m-fund/",
                  "note": "TechCrunch 2025-03-19: Ribbit Capital 'is raising a new $500M fund', from the filing."}]},
    {"name": "Ribbit Capital X, L.P.", "size": 798800000, "vintage": 2022, "accession": "0001937574-23-000001",
     "sources": [{"source": formd(1937574, "0001937574-23-000001"),
                  "note": "Form D/A 2023 Q3: $798,800,000 sold of an $800,000,000 offering, first sale 2022-07-14."}]},
    {"name": "Ribbit Capital VII, L.P.", "size": 1155000000, "vintage": 2021, "accession": "0001851162-22-000001",
     "sources": [{"source": formd(1851162, "0001851162-22-000001"),
                  "note": "Form D/A 2022 Q1: $1,155,000,000 sold, first sale 2021-03-25 (the first filing offered $750,000,000)."},
                 {"source": "https://techcrunch.com/2022/01/03/fintech-focused-ribbit-capital-raises-1-15b-in-seventh-fund-according-to-sec-filing",
                  "note": "TechCrunch 2022-01-03: 'Ribbit Capital raises $1.15B in seventh fund, according to SEC filing'."}]},
    {"name": "Ribbit Bullfrog II, L.P.", "size": 1150000000, "vintage": 2021, "accession": "0001851163-22-000001",
     "sources": [{"source": formd(1851163, "0001851163-22-000001"),
                  "note": "Form D/A 2022 Q1: $1,150,000,000 sold, first sale 2021-03-25; the growth line beside Fund VII."}]},
    {"name": "Ribbit Capital VI, L.P.", "size": 420000000, "vintage": 2020,
     "sources": [{"source": formd(1800884, "0001800884-20-000001"),
                  "note": "Form D 2020 Q1: total offering $420,000,000, $0 sold at filing."},
                 {"source": "https://news.crunchbase.com/venture/ribbit-capital-targets-420m-for-its-sixth-flagship-venture-fund",
                  "note": "Crunchbase News: 'Ribbit Capital targets $420M for its sixth flagship venture fund'."}]},
    {"name": "Bullfrog Capital, L.P.", "size": 500000000, "vintage": 2020,
     "sources": [{"source": formd(1801181, "0001801181-20-000001"),
                  "note": "Form D 2020 Q1: total offering $500,000,000, $0 sold at filing; the first growth fund."}]},
    {"name": "Ribbit Capital V, L.P.", "size": 420000000, "vintage": 2018,
     "sources": [{"source": formd(1751613, "0001751613-18-000001"),
                  "note": "Form D 2018 Q3: total offering $420,000,000, $0 sold at filing."}]},
    {"name": "Ribbit Capital IV, L.P.", "size": 300000000, "vintage": 2017,
     "sources": [{"source": formd(1697450, "0001697450-17-000001"),
                  "note": "Form D 2017 Q1: total offering $300,000,000, $0 sold at filing."}]},
    {"name": "Ribbit Capital III, L.P.", "size": 220000000, "vintage": 2015,
     "sources": [{"source": formd(1637438, "0001637438-15-000001"),
                  "note": "Form D 2015 Q1: total offering $220,000,000, $0 sold at filing."}]},
    {"name": "Ribbit Capital II, L.P.", "size": 124725000, "vintage": 2014, "accession": "0001603636-14-000002",
     "sources": [{"source": formd(1603636, "0001603636-14-000002"),
                  "note": "Form D/A 2014 Q3: $124,725,000 sold of a $125,000,000 offering, first sale 2014-03-27."}]},
    {"name": "Ribbit Capital, L.P.", "size": 100000000, "vintage": 2012,
     "sources": [{"source": LAVCA, "note": "LAVCA: 'Ribbit Capital Debuts With $100M Early-Stage Fund'."},
                 {"source": formd(1553005, "0001553005-12-000001"),
                  "note": "Form D 2012 Q2: total offering $90,000,000, $0 sold at filing; the press size is published."}]},
]
funds_row = [{k: f[k] for k in ("name", "size", "vintage")} for f in funds]

inv = {
    "slug": "ribbit-capital",
    "name": "Ribbit Capital",
    "investor_type": "Institutional",
    "website": "https://ribbitcap.com",
    "icon_url": "https://ribbitcap.com/icon.ico?7f47e9c8855b75ce",
    "hq_location": None,
    "founding_year": 2012,
    "history": history,
    "investment_concept": thesis,
    "investment_stage": ["Seed", "Series A", "Growth"],
    "investment_geo": {"core": ["US"], "other": ["Europe", "Latin America"]},
    "investment_scope": {"type": "Specialist", "focus": focus_pub},
    "investment_range": rng,
    "notable_investments": ["Coinbase", "Robinhood", "Stripe", "Revolut", "Nubank"],
    "aum": {"bottom": 20775390188, "top": 20775390188},
    "funds": {"funds": funds_row},
    "individuals": [],
    "updated_at": now,
}

fields = {
    "name": {"value": inv["name"], "source": "https://ribbitcap.com/",
             "basis": "The firm's own name on its site (the Rebels, team and perspective pages) and its adviser's primary "
                      "business name on Form ADV: Ribbit Management Company, LLC, primary business name RIBBIT CAPITAL, "
                      "CRD 165308 (decisions.md D1)."},
    "website": {"value": inv["website"], "source": "https://ribbitcap.com/",
                "basis": "The firm's site: Next.js (App Router) with no CMS API; the Rebels list (/rebels) and the team "
                         "(/team) are arrays compiled into the page chunks, read by scratch/pull-site.py "
                         "(sources/site/rebels.json, team-pages.json). The perspective letters are DocSend links."},
    "icon_url": {"value": inv["icon_url"], "source": "https://ribbitcap.com/",
                 "basis": "The site's only declared icon, <link rel=icon href=/icon.ico sizes=256x256>: an ICO holding one "
                          "256x256 PNG, extracted to sources/site/icon-256.png, which is the upload source. Dry run "
                          "(fetch-investor-icon.ts, 2026-09-28): the reversed R in a ring on the brand's own opaque green "
                          "plate (self-backing, kept), artwork 200px in the source, 189px in the master (0.945x, never "
                          "enlarged), keyline box and radius 74%, contrast 10.6:1, ramp 1.07px. The upload to the Icon "
                          "Images bucket runs with the ingest, after Erik's approval (COLLECTION.md s9).",
                 "provenance": {"source_url": "data/collection/investors/ribbit-capital/sources/site/icon-256.png",
                                "format": "png", "width": 256, "height": 256, "vector": False,
                                "artwork_source_px": 200, "artwork_master_px": 189, "upscale": 0.945,
                                "ramp_px": 1.07, "master_size": 256, "fetched": "2026-09-28",
                                "allow_upscale": False, "allow_low_contrast": False, "dry_run_only": True}},
    "founding_year": {"value": 2012, "source": ADV,
                      "basis": "Form ADV Schedule A: MALKA, MEYER, Managing Director of the adviser since 03/2012; the first "
                               "fund, Ribbit Capital, L.P., filed its Form D in 2012 Q2 (0001553005-12-000001); LAVCA's report "
                               "of the $100M debut fund (" + LAVCA + "); Wikipedia's infobox gives 2012 "
                               "(https://en.wikipedia.org/wiki/Ribbit_Capital)."},
    "history": {"value": history, "source": LAVCA,
                "basis": "Founding: Palo Alto, 2012, Meyer 'Micky' Malka, 'a serial entrepreneur and financial-services "
                         "veteran' who had 'started five financial-services companies ... in Latin America, Europe and the "
                         "U.S.', with a $100 million debut fund and Malka the sole general partner (LAVCA). Bets: Coinbase, "
                         "Robinhood (Series A, 2014), Credit Karma, Nubank and Revolut (Series A, 2016), all members on "
                         "this page. Assets: $20,775,390,188 regulatory assets under management, Form ADV annual amendment "
                         "of 2026-03-30 (CRD 165308, Item 5.F), 'about $21 billion'. Latest fund: Ribbit Capital Z, L.P., "
                         "$561,860,000 sold (Form D/A 2026 Q2, first sale 2026-02-12). Dropped to fit: the fund ladder "
                         "(see funds), the growth line (Bullfrog, Bullfrog II and III), the opportunistic Leapfrog fund "
                         "(2025), the firm's 2020 SPAC, Ribbit LEAP (liquidated without a merger, out of the portfolio "
                         "under decisions.md D3), and the partners (see individuals). BOUNDARY: one adviser, no relying "
                         "advisers (decisions.md D1); Bitcoin and Ethereum, which the firm lists, are treasury or protocol "
                         "assets and are out (D2); public-market purchases (Mercado Libre, Sea, Futu, Tinkoff) are out "
                         "(D4); the single-deal vehicles decode to rounds, never entries (D6)."},
    "investment_concept": {"value": thesis, "source": "https://ribbitcap.com/",
                           "basis": "The firm's own statement, read off the homepage on 2026-09-28 (sources/site/home.html): "
                                    "the hero reads 'the future belongs to the rebels', set letter by letter in lower case and "
                                    "repeated as a ticker; the same line is on the firm's coin (sources/site/ribbit-coin.png). "
                                    "Published in sentence case with one closing period, inside quotation marks (Erik, "
                                    "2026-09-26). Competing lines on the page: the title tag 'RIBBIT' and the meta "
                                    "description 'The world doesn't change because incumbents decide it should. It changes "
                                    "because someone, somewhere, decides the system is broken and has the conviction to build "
                                    "something better.' (two sentences, 34 words, over the 25-word limit)."},
    "investment_stage": {"value": inv["investment_stage"], "source": "companies/base.json", "flags": ["derived"],
                         "basis": f"Derived: the firm publishes no stage vocabulary (its site lists company names only). "
                                  f"The landed entry distribution over the {M} members: "
                                  f"{fmt(stage, ['Growth', 'Series A', 'Seed', 'Pre-Seed'])}; {stage['undetermined']} rows "
                                  f"whose entry round the record does not give are left out. Three stages carry weight. "
                                  f"The fund architecture agrees: flagship venture funds (Ribbit Capital I to VII, X, Y, Z) "
                                  f"beside growth funds (Bullfrog Capital, Ribbit Bullfrog II and III) and an opportunistic "
                                  f"fund (Leapfrog Capital, 2025)."},
    "investment_geo": {"value": inv["investment_geo"], "source": "companies/base.json", "flags": ["derived"],
                       "basis": f"From the members' headquarters on the landed base: US {geo['US']} of {M}, Europe "
                                f"{reg['Europe']} ({fmt(geo, REGION['Europe'])}), Latin America {reg['Latin America']} "
                                f"({fmt(geo, REGION['Latin America'])}), India {geo['IN']}, the rest of Asia {reg['Asia']} "
                                f"({fmt(geo, REGION['Asia'])}), and "
                                f"{fmt(geo, [c for c in geo if c not in ('US', 'IN') and not any(c in v for v in REGION.values())])}. "
                                f"The firm's offices are Palo Alto (principal) and New York (Form ADV). Core US, other Europe and "
                                f"Latin America "
                                f"(two-label cap); India is next."},
    "investment_scope": {"value": inv["investment_scope"], "source": "companies/classification.json",
                         "flags": ["derived"],
                         "basis": f"Derived: the site carries no sector tags, so the build's site-tag recompute does not "
                                  f"apply. The grind's focus column over the {M} members: "
                                  f"{fmt(focus, [f for f, _ in focus.most_common()])}; published above "
                                  f"profile.focus_min_companies ({FOCUS_MIN}). Specialist: {fintech_share:.0%} of the "
                                  f"members are fintech or crypto companies; the homepage now also names AI, commerce, "
                                  f"infrastructure, wealth management, identity, data and energy."},
    "investment_range": {"value": rng, "source": "scratch/entry-rounds.json", "flags": ["derived"],
                         "basis": f"MEDIAN: ${er['median'] / 1e6:.1f}M, the median entry round over the {er['n']} of "
                                  f"{er['of_members']} members whose first round with the firm is on record with an amount "
                                  f"({er['via'].get('judged round', 0)} from the judged rounds, each cited on its row; "
                                  f"{er['via'].get('Form D entry offering', 0)} from the entry Form D where the entry rests "
                                  f"on the filing): p10 ${er['p10'] / 1e6:.1f}M, p25 ${er['p25'] / 1e6:.1f}M, p75 "
                                  f"${er['p75'] / 1e6:.1f}M, p90 ${er['p90'] / 1e6:.1f}M. By entry stage: "
                                  + ", ".join(f"{k} ${v / 1e6:.1f}M" for k, v in sorted(er['by_stage'].items()))
                                  + ". LOWER and UPPER are the p10 and p90, since the firm publishes no cheque range. It is "
                                    "a round size, not a cheque size: the firm joins large growth rounds (Checkout.com's "
                                    "$1B round), which sets the upper end. Form D covers few entries because two in five "
                                    "members are outside the US."},
    "notable_investments": {"value": inv["notable_investments"], "source": "companies/base.csv",
                            "basis": "The five best known of the firm's own companies, most recognised first (PRO-152, Erik "
                                     "2026-09-24). Considered next: Credit Karma, Affirm, Brex, Wealthfront, Razorpay.",
                            "slugs": ["coinbase", "robinhood", "stripe", "revolut", "nubank"]},
    "aum": {"value": inv["aum"], "source": IAPD,
            "basis": "Both ends: the sworn regulatory assets under management of Ribbit Management Company, LLC (primary "
                     "business name RIBBIT CAPITAL, CRD 165308), Item 5.F of the Form ADV annual amendment of 2026-03-30: "
                     "$20,775,390,188, all discretionary, 67 accounts (sources/registers/adv-165308.pdf, " + ADV + "). "
                     "Section 7.B lists 67 private funds: the flagship and growth funds, founder side funds, holding "
                     "vehicles and about 40 single-deal vehicles (decisions.md D1). Ribbit Capital Z (first sale "
                     "2026-02-12) postdates the amendment's fiscal year, and Leapfrog Capital, L.P. (first sale "
                     "2025-07-01) is not on the list."},
    "funds": {"value": funds, "source": "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=ribbit&type=D",
              "basis": "The flagship funds (Ribbit Capital, L.P. to Ribbit Capital Z, L.P.; there is no VIII or IX), the "
                       "growth line (Bullfrog Capital, Ribbit Bullfrog II and III) and the opportunistic Leapfrog fund, "
                       "from the firm's own Form D filings (the own-desk CIKs in entities.json, read over the bulk zips "
                       "by build-firm-profile.py). Sizes: the sold amount where an amendment reports the close (II, VII, "
                       "Bullfrog II, X, Leapfrog, Z; each entry carries its accession and is asserted against the filing); "
                       "the total offering amount where the only filing reports $0 sold (III, IV, V, VI, Bullfrog "
                       "Capital, Y, Bullfrog III; press corroborates VI and Y); LAVCA's $100M for Fund I, whose Form D "
                       "offered $90M. Form ADV gross asset values are current values, not sizes (Fund III reports "
                       "$3.58B on a $220M fund), so none is used. NOT LISTED, described here: two hedge-fund-type "
                       "evergreen vehicles at the firm's office, RBT, L.P. (2017, $160,988,933 sold by its 2023 "
                       "amendment) and Ribbit OB1 (2022, US and Cayman feeders on one co-issued Form D, $959,405,827 sold "
                       "by 2025 Q3); the founder side funds (Ribbit Founder Fund I to VII, X, Y, Z; Bullfrog Founder "
                       "Fund; Ribbit Bullfrog Founder Fund II and III); holding vehicles (Ribbit Holdings, Ribbit "
                       "Holdings II, Revolut Ribbit Holdings, Ribbit BTC Holdings, RTZ Ribbit Opportunity); and about 40 "
                       "lettered single-deal vehicles (Ribbit Opportunity I to VII and Bullfrog Opportunity I and II "
                       "series, decoded in sources/registers/spv-decode.json)."},
}

sources = {"slug": "ribbit-capital", "generated_at": now, "run": "PRO-161", "fields": fields}
(INV / "investor/investor.json").write_text(json.dumps(inv, indent=2, ensure_ascii=False) + "\n")
(INV / "investor/sources.json").write_text(json.dumps(sources, indent=1, ensure_ascii=False) + "\n")
print("members", M, "| stage", dict(stage), "| range", rng, "| focus", focus_pub)
print("geo", dict(geo.most_common()), reg)
print("history words", len(history.split()))
