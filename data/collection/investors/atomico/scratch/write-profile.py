#!/usr/bin/env python3
"""Write Atomico's firm profile (COLLECTION.md §11): investor/investor.json and
investor/sources.json, one provenance entry per field. hq_location and the
recomputed fields (individuals, investment_scope.focus) are then written by
scripts/firm-offices.py and scripts/build-firm-profile.py."""
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent / "investor"
INS = "https://atomico.com/insights/"
ADV = "https://reports.adviserinfo.sec.gov/reports/ADV/{0}/PDF/{0}.pdf"
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

history = ("Atomico was founded in London in 2006 by Skype co-founder Niklas Zennström. "
           "Its early bets included Rovio, Supercell, Klarna and Truecaller, and it later backed "
           "Stripe, Hinge Health and DeepL, investing mostly from Series A onward. "
           "In 2024 it closed $1.24 billion across two funds, Atomico Venture VI and Atomico Growth VI.")
thesis = "“Capital is a commodity. Experience is not.”"

funds = [
    {"name": "Atomico Growth VI SCSp", "size": 754000000, "vintage": 2024,
     "sources": [{"source": INS + "dollar124-billion-as-european-technology-comes-of-age",
                  "note": "The firm's own post, 2024-09-09: 'The new $754 million Atomico Growth VI partners with entrepreneurs from Series B to pre-IPO.'"},
                 {"source": ADV.format(301113),
                  "note": "Form ADV 7.B(1) of Atomico (UK) Partners LLP (filed 2026-06-08): ATOMICO GROWTH VI SCSP, gross asset value $956,485,371."}]},
    {"name": "Atomico Venture VI SCSp", "size": 485000000, "vintage": 2024,
     "sources": [{"source": INS + "dollar124-billion-as-european-technology-comes-of-age",
                  "note": "The firm's own post, 2024-09-09: 'a $485 million early stage fund, Atomico Venture VI ... predominantly at Series A, alongside occasional Seed opportunities.'"},
                 {"source": ADV.format(301113),
                  "note": "Form ADV 7.B(1): ATOMICO VENTURE VI SCSP, gross asset value $649,420,674; a parallel Luxembourg vehicle, Atomico Venture VI (Parallel) S.C.A., SICAV-RAIF, appears on UK registers (decisions.md D1)."}]},
    {"name": "Atomico V SCSp", "size": 820000000, "vintage": 2020,
     "sources": [{"source": INS + "announcing-atomico-v",
                  "note": "The firm's own post, 2020-02-18: 'At $820 million ... Atomico V was oversubscribed, closing above our target of $750m.'"},
                 {"source": ADV.format(301113), "note": "Form ADV 7.B(1): ATOMICO V SCSP, gross asset value $983,101,261."}]},
    {"name": "Atomico IV, L.P.", "size": 765000000, "vintage": 2017,
     "sources": [{"source": INS + "atomico-iv-dollar765m-for-europes-most-ambitious-founders",
                  "note": "The firm's own post, 2017-02-16: 'At $765m Atomico IV is one of the largest venture capital funds ever raised in Europe.'"},
                 {"source": ADV.format(165691), "note": "Form ADV 7.B(1) of Atomico Management, Ltd. (filed 2026-03-12): ATOMICO IV, L.P., gross asset value $1,320,244,306; Atomico IV (Guernsey) L.P. is its parallel vehicle on UK registers."}]},
    {"name": "Atomico III, L.P.", "size": 476000000, "vintage": 2013,
     "sources": [{"source": INS + "great-companies-can-come-from-anywhere-announcing-atomico-iii-our-dollar476m-fund-to-help-them-scale",
                  "note": "The firm's own post, 2013-11-19: 'we have now closed our third and most recent fund, Atomico III, at $476m, three times the size of our previous fund.'"},
                 {"source": ADV.format(165691), "note": "Form ADV 7.B(1): ATOMICO III, L.P., gross asset value $263,374,564."}]},
    {"name": "Atomico Ventures II", "size": 165000000, "vintage": 2010,
     "sources": [{"source": "https://techcrunch.com/2010/03/22/atomico-ventures-raises-165m-fund-targeting-disruptive-early-stage-european-startups/",
                  "note": "TechCrunch, 2010-03-22: Atomico Ventures raises a $165M fund; the firm's 2011 site filed its companies under /portfolios/atomico-ii/."}]},
]

inv = {
    "slug": "atomico",
    "name": "Atomico",
    "investor_type": "Institutional",
    "website": "https://atomico.com",
    "icon_url": None,
    "founding_year": 2006,
    "history": history,
    "investment_concept": thesis,
    "investment_stage": ["Seed", "Series A", "Growth"],
    "investment_geo": {"core": ["Europe"], "other": ["US"]},
    "investment_scope": {"type": "Generalist", "focus": []},
    "investment_range": {"lower_limit": 1000000, "median": 17000000, "upper_limit": 100000000},
    "notable_investments": ["Klarna", "Stripe", "Supercell", "Lime", "DeepL"],
    "aum": {"bottom": 4172626176, "top": 4172626176},
    "funds": {"funds": funds},
    "individuals": [],
    "updated_at": now,
}

fields = {
    "name": {"value": "Atomico", "source": "https://atomico.com",
             "basis": "the firm's brand since 2006; the advisers are Atomico (UK) Partners LLP (CRD 301113) and Atomico Management, Ltd. (CRD 165691), and its 2008 site was operated by Atomico Investment Holdings Ltd (the page footer); decisions.md D1 lists the vehicles"},
    "website": {"value": "https://atomico.com", "source": "https://atomico.com",
                "basis": "firm site (Next.js over a Hygraph CMS; portfolio at /partners). Behind a Vercel bot checkpoint on 2026-09-26, so every page was read from Common Crawl or Internet Archive captures"},
    "icon_url": {"value": None, "source": None,
                 "basis": "not yet published: the icon upload waits for Erik's ingest approval (COLLECTION.md §9); the candidate source is chosen by fetch-investor-icon.ts --discover at that point"},
    "founding_year": {"value": 2006, "source": INS + "great-companies-can-come-from-anywhere-announcing-atomico-iii-our-dollar476m-fund-to-help-them-scale",
                      "basis": "the firm's own posts: 'We founded Atomico in 2006' (2013 Atomico III post); 'Since Atomico was founded in 2006' (2024 fund post)"},
    "history": {"value": history, "source": INS + "dollar124-billion-as-european-technology-comes-of-age",
                "basis": "Founded in London in 2006 by Niklas Zennström (the firm's own posts; Skype co-founder). Early bets per the firm's own 2017 fund post ('we've partnered with ... Klarna, Rovio, Supercell, The Climate Corporation, GoEuro and Skype') and the portfolio rows: Rovio Series A 2011, Klarna 2012, Supercell 2013 secondary, Truecaller Series C 2014; later Stripe (CMS 2015), Hinge Health Series A 2017 (IPO 2025), DeepL (CMS 2023). 'Investing mostly from Series A onward': 'Since inception we've partnered with founders from series A, expanding to include growth investments in 2011' (2024 fund post). Fund VI: $754M Growth VI and $485M Venture VI, $1.24B (2024-09-09). Dropped to fit: the fund ladder ($165M 2010, $476M 2013, $765M 2017, $820M 2020, see funds), the State of European Tech report, offices"},
    "investment_concept": {"value": thesis, "source": "https://index.commoncrawl.org/CC-MAIN-2026-04-index?url=atomico.com/&output=json",
                           "basis": "The firm's own statement, verbatim from the homepage's lead heading (h2), read from the Common Crawl capture of atomico.com of 2026-01-18 (local copy scratch/site-raw/home-cc20260118051330.html) because the live site sits behind a bot checkpoint; published inside quotation marks as the firm's words. Competing lines on the same page: the h1 is a banner for the firm's '2025 State of European Tech' report, and the meta description reads 'Atomico invests in innovative technology companies around the world.'"},
    "investment_stage": {"value": ["Seed", "Series A", "Growth"], "source": "companies/base.json",
                         "basis": "entry stages on the 165-row base after classification: Series A 56, Growth 48, Seed 18, undetermined 41 (2 unnameable); the firm's own framing: 'predominantly at Series A, alongside occasional Seed opportunities' (Venture VI) and 'from Series B to pre-IPO' (Growth VI), 2024 fund post"},
    "investment_geo": {"value": {"core": ["Europe"], "other": ["US"]}, "source": "companies/base.json",
                       "basis": "hq_country on the classified base: 103 of 165 in Europe (GB 45, DE 15, NL 7, SE 6, ES 5, FI 5, FR 4, CH 4, others), US 45, elsewhere 17 (mostly the 2011-2012 Latin America and Asia deals: CN, JP, RU, BR, AR, UY), 2 unnameable; the CMS location filter is Europe by region plus 'USA' and 'Rest of World'",
                       "flags": ["geo_core_from_base_counts"]},
    "investment_scope": {"value": {"type": "Generalist", "focus": []}, "source": "companies/base.json",
                         "basis": "focus recomputed by build-firm-profile.py from the firm's own CMS theme tags (Digital Work, Enterprise AI & Automation, Improving Health, Digital Life & Play, ...) through the crosswalk in config.json profile.focus_crosswalk. Scope type is the curated judgement carried in investor.json: themes across software, consumer, health, climate, mobility and industrial"},
    "investment_range": {"value": {"lower_limit": 1000000, "median": 17000000, "upper_limit": 100000000}, "source": "companies/classification.json",
                         "basis": "Median: the entry round on 122 portfolio rows whose recorded funding_rounds give a size (the first round the firm joined): median $17.25M, p25 $10.0M, p75 $51.5M, p90 $115.5M, published as $17M; the rounds are co-invested, so this is a round-size proxy for check size. | Lower limit: the smallest entry rounds are 2011-era seeds of $0.5M-$1M (Silk EUR 320K, Restorando $500K, Quipper GBP 400K, Siine GBP 550K, EVRYTHNG $1M), published as $1M. | Upper limit: the largest rounds the firm led or co-led at entry are TravelPerk $200M (2025, with EQT), PsiQuantum $150M (2020), CodeRabbit $143M (2026, with Smash) and PhysicsX $135M (2025); a 10-15% single-position concentration of the largest fund ($820M, Atomico V) gives $82M-$123M, so $100M. Rejected: The Exploration Company's $450M (three co-leads, the firm's share unknown)"},
    "notable_investments": {"value": ["Klarna", "Stripe", "Supercell", "Lime", "DeepL"], "source": "companies/base.csv",
                            "basis": "The five best known of the firm's own companies, most recognised first: the names a general reader would recognise first (PRO-152, Erik 2026-09-24); names as a reader knows them (COLLECTION.md §8). Also considered: Rovio (Angry Birds), MasterClass, Truecaller, Hinge Health, Zocdoc.",
                            "slugs": ["klarna", "stripe", "supercell", "lime", "deepl"]},
    "aum": {"value": {"bottom": 4172626176, "top": 4172626176}, "source": "https://adviserinfo.sec.gov/",
            "basis": "Bottom and top: the sworn Form ADV Section 7.B(1) gross asset values of Atomico's five reported funds, both advisers being exempt reporting advisers (no Item 5.F): under Atomico (UK) Partners LLP (CRD 301113, filed 2026-06-08) Atomico Growth VI SCSp $956,485,371, Atomico V SCSp $983,101,261, Atomico Venture VI SCSp $649,420,674 = $2,589,007,306; under Atomico Management, Ltd. (CRD 165691, filed 2026-03-12) Atomico III, L.P. $263,374,564 and Atomico IV, L.P. $1,320,244,306 = $1,583,618,870; total $4,172,626,176 (sources/edgar/adv-7b.json, IAPD PDFs data/filings/adv/). The firm's own 2020 figure ('total AUM to $2.7B', Atomico V post) is older and below it",
            "sources": [{"source": ADV.format(301113)}, {"source": ADV.format(165691)}]},
    "funds": {"value": funds, "source": "https://atomico.com/insights/",
              "basis": "The firm's own fund announcements (2013, 2017, 2020, 2024) and TechCrunch for 2010; the ADV 7.B roster confirms III, IV, V, Venture VI and Growth VI. Atomico Ventures I (2006, the founders' capital) published no size and is left out. Parallel vehicles (Atomico IV (Guernsey) L.P., Atomico Venture VI (Parallel) SICAV-RAIF, Atomico Investment Holdings Ltd) sit beside their flagships (decisions.md D1)"},
}
sources = {"slug": "atomico", "generated_at": now, "run": "PRO-79", "fields": fields}

(INV / "investor.json").write_text(json.dumps(inv, indent=1, ensure_ascii=False) + "\n")
(INV / "sources.json").write_text(json.dumps(sources, indent=1, ensure_ascii=False) + "\n")
print("wrote", INV / "investor.json", "and sources.json")
