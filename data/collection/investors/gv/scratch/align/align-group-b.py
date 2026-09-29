"""Rule-10 alignment from the GV run (PRO-75), group B books, approved by Erik
2026-09-29 ("ingest GV and align the stale/misaligned sibling rows"). One
classification line per stale sibling row in the accepted pairs of
gv/companies/cross-rulings.json, plus 8VC's Lyell (ALIGN-BRIEF item 2),
written to scratch/align/<investor>.jsonl for `run.py record --investor
<investor>`. Every URL cited here was read with curl on 2026-09-29 and states
the event. No gv.com page is cited to another investor's book.

Rows already aligned by the ICONIQ run (PRO-168, 3c039960) and matching GV's
status and band are not rewritten: battery-ventures:headspin,
eqt-ventures:headspin, redpoint-ventures:omni, thrive-capital:robinhood.

Usage: python3 align-group-b.py [--record]   (default writes the jsonl files only)
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro75"
TAG = "Aligned 2026-09-29 from the GV run (PRO-75, rule 10)"

BASIS = "https://fintech.global/2026/02/25/basis-raises-100m-series-b-at-1-15bn-valuation/"
MOTIVE = "https://en.wikipedia.org/wiki/Motive_%28company%29"
MULTIVERSE = ("https://pulse2.com/multiverse-70-million-raised-at-2-1-billion-valuation-to-expand-"
              "ai-upskilling-platform-across-europe/")
THATCH = ("https://www.prnewswire.com/news-releases/thatch-raises-108m-at-1b-valuation-as-employers-"
          "shift-away-from-traditional-health-plans-302879015.html")
OBSIDIAN = "https://www.unite.ai/obsidian-security-raises-85-million-series-d-at-unicorn-valuation/"
LYELL = "https://stockanalysis.com/stocks/lyel/market-cap/"


def value(slug, st, rng, usd, asof, cite, note):
    return {"slug": slug, "who": WHO, "status": st, "valuation_range": rng, "valuation_usd": usd,
            "valuation_source": "web_verified", "valuation_range_source": "web_verified",
            "valuation_asof": asof, "valuation_citation": cite, "valuation_confidence": "high",
            "note": f"{TAG}: {note}"}


def status(slug, st, note, **extra):
    return {"slug": slug, "who": WHO, "status": st, "valuation_range": "below_1b", **extra,
            "note": f"{TAG}: {note}"}


CLARIFAI = ("acquired, as Erik ruled on 2026-09-29: Nebius took Clarifai's core engineering team, "
            "bought its patent portfolio and licensed its inference and compute orchestration "
            "technology (SiliconANGLE, 2026-05-12, https://siliconangle.com/2026/05/12/nebius-snaps-"
            "clarifais-compute-orchestration-tech-talent-enhance-ai-inference/), as the GV row reads.")
POLAR = ("acquired: Dash0 announced its acquisition of Polar Signals on 2026-08-17 (Business Insider, "
         "https://www.businessinsider.com/dash0-polar-signals-acquisition-ai-agents-continuous-"
         "profiling-2026-8), as the GV row reads.")
VOLTRON = ("defunct: Andy Pavlo's 2025 databases retrospective (CMU, https://www.cs.cmu.edu/~pavlo/blog/"
           "2026/01/2025-databases-retrospective.html) records the death of Voltron Data among the "
           "year's database company closings, as the GV and Coatue rows read.")
OBSIDIAN_NOTE = ("the $85M Series D at a $1.1B valuation, led by Crescent Cove with all existing "
                 "investors participating (Unite.AI, 2026-08-04), as in the GV row.")

LINES = {
    "khosla-ventures": [
        value("basis", "private", "1b_plus", 1150000000, "2026-02", BASIS,
              "the $100M Series B at a $1.15B valuation, led by Accel with GV and existing backer "
              "Khosla Ventures (FinTech Global, 2026-02-25), as in the GV row."),
        status("everyone-medicines", "defunct",
               "defunct: EveryONE Medicines will close, Endpoints News reported on 2026-03-03 "
               "(https://endpoints.news/everyone-medicines-shuts-down-ending-custom-cure-venture-that-"
               "banked-on-new-fda-pathway/), as the GV row reads."),
        value("keep-truckin-inc", "private", "1b_plus", 2850000000, "2022-05", MOTIVE,
              "KeepTruckin, renamed Motive, reached a $2.85B valuation after its $150M Series F of "
              "2022, co-led by Insight Partners and Kleiner Perkins (Wikipedia, citing Bloomberg of "
              "2022-05-25), as in the GV row."),
        status("miso", "acquired",
               "acquired: 'Dijit Acquires Second Screen App Miso' (BetaKit, 2013-02-01, "
               "https://betakit.com/dijit-acquires-second-screen-app-miso-looks-to-provide-hyper-"
               "personalized-discovery/), the sale this row's own note already cites."),
    ],
    "lux-capital": [
        status("clarifai", "acquired", CLARIFAI),
        value("thatch", "private", "1b_plus", 1000000000, "2026-09-15", THATCH,
              "the $108M Series C at a $1B valuation (Thatch's release on PR Newswire, 2026-09-15), "
              "as in the GV row."),
        status("transphorm", "acquired",
               "acquired: Renesas Electronics agreed to buy Transphorm for $339M in January 2024 and "
               "completed the purchase on 2024-06-20 (Wikipedia, https://en.wikipedia.org/wiki/"
               "Transphorm), as the GV row reads."),
    ],
    "lightspeed": [
        value("multiverse", "private", "1b_plus", 2100000000, "2026-05", MULTIVERSE,
              "the $70M round at a $2.1B valuation led by Schroders Capital, with Lightspeed "
              "participating (Pulse 2.0, 2026-05-15), as in the GV row."),
        status("polar-signals", "acquired", POLAR),
        status("voltron-data", "defunct", VOLTRON),
        # The $1B+ band makes the row subject to rule 6: its unchanged GB country needs a
        # citation, or the book's country debt grows past its ratchet (30).
        {"slug": "multiverse", "who": WHO, "hq_country": "GB", "hq_country_source": "web_verified",
         "hq_country_citation": "https://en.wikipedia.org/wiki/Multiverse_(company)",
         "note": f"{TAG}: the country stays GB and now carries its citation, which a $1B+ non-US "
                 "row needs (rule 6): Wikipedia gives the headquarters as London, United Kingdom."},
    ],
    "union-square-ventures": [
        status("circleup", "acquired",
               "acquired: 'CircleUp Acquired by Brightflow AI' (PR Newswire, 2023-06-02, "
               "https://www.prnewswire.com/news-releases/circleup-acquired-by-brightflow-ai-"
               "301841217.html), as the GV row reads."),
        status("clarifai", "acquired", CLARIFAI),
    ],
    "menlo-ventures": [
        status("clarifai", "acquired", CLARIFAI),
        value("obsidian-security", "private", "1b_plus", 1100000000, "2026-08-04", OBSIDIAN,
              OBSIDIAN_NOTE),
    ],
    "battery-ventures": [
        status("voltron-data", "defunct", VOLTRON),
    ],
    "ivp": [
        value("obsidian-security", "private", "1b_plus", 1100000000, "2026-08-04", OBSIDIAN,
              OBSIDIAN_NOTE),
        status("tunein", "acquired",
               "acquired: Stingray Group announced a $175M purchase of TuneIn in November 2025 and "
               "completed it in December 2025 (Wikipedia, https://en.wikipedia.org/wiki/TuneIn), as "
               "the GV row reads."),
    ],
    "spark-capital": [
        status("polar-signals", "acquired", POLAR),
        status("signpost", "acquired",
               "acquired: Hibu, an H.I.G. Capital portfolio company, bought Signpost's marketing "
               "technology platform, announced 2023-09-11 (Corridor Business Journal, 2023-09-12, "
               "https://corridorbusiness.com/hibu-acquires-signposts-marketing-technology-platform/), "
               "a sale of the business, as the GV row reads."),
    ],
    "insight-partners": [
        # The defunct status, its 2010 as-of and its wikidata source came from a one-word
        # Wikidata join to a different Hustle (dissolved 2010); GV's row carries no as-of.
        status("hustle", "acquired",
               "acquired: Social Capital acquired Hustle in 2020 and its employees bought the "
               "company from Social Capital in May 2026 (Campaigns & Elections, "
               "https://campaignsandelections.com/industry-news/employees-buy-out-political-"
               "texting-platform-hustle/); the defunct status and its 2010 date came from a "
               "Wikidata join to a different Hustle, as the GV row reads.",
               valuation_asof=None, valuation_source=None),
    ],
    "greylock": [
        value("obsidian-security", "private", "1b_plus", 1100000000, "2026-08-04", OBSIDIAN,
              OBSIDIAN_NOTE),
    ],
    "redpoint-ventures": [
        status("brandless", "acquired",
               "acquired under the asset-sale rule: Brandless ceased operations in February 2020 "
               "and its assets were bought in June 2020 by Clarke Capital Partners and Ikonifi, who "
               "relaunched the brand (Wikipedia, https://en.wikipedia.org/wiki/Brandless), as the "
               "GV row reads."),
    ],
    "8vc": [
        value("lyell", "public", "below_1b", 231820000, "2026-09-29", LYELL,
              "public: Lyell Immunopharma still trades on NASDAQ (LYEL), market cap $231.82M on "
              "2026-09-29 (StockAnalysis), so the row is not acquired (ALIGN-BRIEF item 2)."),
    ],
}

if __name__ == "__main__":
    rec = "--record" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    for inv, lines in LINES.items():
        if only and inv not in only:
            continue
        p = HERE / f"{inv}.jsonl"
        p.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
        print(f"== {inv}: {len(lines)} line(s) -> {p.name}")
        if not rec:
            continue
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-1500:])
        if r.returncode:
            sys.exit(f"record failed for {inv}; stopping")
