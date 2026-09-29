#!/usr/bin/env python3
"""Assemble GV's researched profile fields into investor/investor.json and investor/sources.json (COLLECTION.md s11).
Re-runnable: the base-dependent fields (stage, geo, scope, range, notables) are read from scratch/profile-derived.json
when it exists (written after the grind by scratch/derive-profile.py), else left as they are.

The fields a Form ADV would anchor (aum; hq_location's principal office) follow decisions.md Delta 1: GV files no
ADV, so `aum` is the explicit null range with the flag `no_sworn_source` and the firm's own "$13B Under Management" in
the basis, and hq_location comes from the firm's own site statement through firm-offices.py (config profile.site_office).
Usage: python3 write-profile.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("gv")
inv = json.loads(P.investor.read_text()) if P.investor.exists() else {"slug": "gv"}
src = json.loads(P.investor_sources.read_text()) if P.investor_sources.exists() else {"slug": "gv", "fields": {}}
F = src.setdefault("fields", {})


def put(key, value, source, basis, **extra):
    inv[key] = value
    F[key] = {"value": value, "source": source, "basis": basis, **extra}


EDGAR = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}"
STATS = "https://www.gv.com/portfolio"

HISTORY = ("GV was founded in 2009 as Google Ventures by Bill Maris to invest Google's capital, and took the name GV in "
           "2015 under Alphabet. Its bets include Uber, Nest, Slack and Flatiron Health. Led by David Krane, it invests "
           "from San Francisco, New York, Cambridge and London, and says it manages $13 billion.")
put("history", HISTORY, "https://en.wikipedia.org/wiki/GV_(company)",
    "Founded as Google Ventures on March 31, 2009 by Bill Maris with an initial $100 million commitment from Google, "
    "renamed GV in December 2015 (Wikipedia, 'GV (company)', read 2026-09-29; the firm's own homepage caption 'EST. "
    "2009'). Uber, Nest, Slack and Flatiron Health are on the firm's own list (gv.com/portfolio, with the firm's exit "
    "lines 'NYSE: UBER', 'Acquired by Google, 2014', 'NYSE: WORK', 'Acquired by Roche, 2018'). David Krane is 'CEO & "
    "Managing Partner' on the firm's team page (gv.com/team/david-krane). Offices: the firm's own offices document "
    "(San Francisco Bay Area as headquarters, New York, Cambridge, London). '$13B Under Management' is the firm's own "
    "stats box on gv.com (read 2026-09-29), stated as the firm's claim because no sworn figure exists (aum field). "
    "Moved to this sidecar, not the page: the vehicles by vintage (funds field), CapitalG and Gradient as separate "
    "Alphabet units, the $125 million European allocation of 2014 led by Tom Hulme, and Bill Maris's departure in 2016.")

put("aum", {"bottom": None, "top": None}, STATS,
    "EXPLICITLY NULL, flagged no_sworn_source (decisions.md Delta 1, open for Erik). GV is a corporate venture arm and "
    "files no Form ADV: IAPD returns no firm under GV, GV Management, Google Ventures, Google or Alphabet (2026-09-29), "
    "so neither Item 5.F nor Section 7.B exists, and the vehicles raise no outside money (no fund Form D; the one Form "
    "D is GV 2025 GP, L.P., the team's own vehicle, $0 sold). The firm's own statement is '$13B Under Management' "
    "(gv.com stats box, read 2026-09-29); Wikipedia's infobox says 'approximately $10 billion'. Neither is sworn, and "
    "every other profile's range is anchored on a sworn figure, so the firm's number stays here. Alternative for "
    "Erik: publish the firm-stated $13B as both ends, flagged firm_stated. GV Management Company, L.L.C. (CIK 1940173) "
    "files 13F notices; its listed holdings are reported inside Alphabet Inc.'s 13F, which covers public equities "
    "only and is no AUM figure.", flags=["no_sworn_source"])

VEHICLES = [("GV 2023, L.P.", 1961979, 2023), ("GV 2021, L.P.", 1861202, 2021), ("GV 2019, L.P.", 1845041, 2019),
            ("GV 2017, L.P.", 1733340, 2017), ("GV 2016, L.P.", 1721789, 2016), ("GV 2015, L.P.", 1719755, 2015),
            ("GV 2014, L.P.", 1728797, 2014), ("GV 2013, L.P.", 1634261, 2013), ("Google Ventures 2011, L.P.", 1586699, 2011)]
GV2012 = {"name": "Google Ventures 2012, L.P.", "size": None, "vintage": 2012,
          "sources": [{"source": "https://www.sec.gov/Archives/edgar/data/1647639/000119312520309971/d867925ds1a.htm",
                       "note": "Named as a selling stockholder in Upstart's S-1/A (2020-12-04, holder table) and in DocuSign's "
                               "2018 draft registration (notice address 1600 Amphitheatre Parkway); Nextdoor's merger 8-K lists a "
                               "management rights letter with it dated 2012-10-05. It never filed on EDGAR under its own name."}]}
funds = [{"name": n, "size": None, "vintage": v,
          "sources": [{"source": EDGAR.format(cik=f"{c:010d}"),
                       "note": f"The vehicle's own EDGAR filer page (CIK {c}): 13D/G and Forms 3/4 as a holder, filed from "
                               "1600 Amphitheatre Parkway, Mountain View. No size: Alphabet funds it and it files no "
                               "Form D."}]} for n, c, v in VEHICLES]
funds.insert(len(funds) - 1, GV2012)
put("funds", funds, "https://www.sec.gov/cgi-bin/browse-edgar?company=gv+20&type=&dateb=&owner=include&count=40",
    "The GV vehicles on EDGAR (company search 'GV 20' and 'Google Ventures', 2026-09-29), newest first, vintage from "
    "the name, plus Google Ventures 2012, L.P., which filed nothing under its own name but is named in portfolio companies' filings (Upstart's 2020 S-1/A holder table, DocuSign's 2018 registration, Nextdoor's 2012 management rights letter). Sizes are null: Alphabet is the only limited partner, so no vehicle files a Form D or a Section 7.B "
    "gross asset value, and the firm publishes none. GV 2013, L.P. filed first as Google Ventures 2013, L.P. Not "
    "listed: GV 2025 GP, L.P. (CIK 2036706; its Form D reports 84 investors and $0 sold, the team's own general "
    "partner vehicle, evidence of a 2025 vintage whose fund entity is not on EDGAR), the GV 20xx GP entities, GV "
    "Management Company, L.L.C. (the manager), and CapitalG's vehicles (a separate firm). Press allocations: Google's "
    "commitment was $100 million in 2009 and $300 million a year from 2012 (Wikipedia); a $125 million European "
    "allocation was announced in 2014.")

put("icon_url", "data/collection/investors/gv/sources/site/gv-logo.svg", "data/collection/investors/gv/sources/site/gv-logo.svg",
    "Source chosen by measurement: --discover on https://www.gv.com offers a 512x512 favicon.png, a 1280x720 og:image "
    "and two inline SVG logo elements; the vector wins (COLLECTION.md s11). The source is the header's own inline <svg> "
    "(viewBox 0 0 49 31, the black 'GV' mark), saved as sources/site/gv-logo.svg. Dry run 2026-09-29: vector, a "
    "synthesized #ffffff plate behind the bare glyph, artwork scaled 0.682 into the keyline (box 68%, radius 79%), "
    "contrast 18.8:1, ramp 0.86 px. Uploaded at ingest, after Erik's approval.")

derived = HERE / "profile-derived.json"
if derived.exists():
    for k, v in json.loads(derived.read_text()).items():
        put(k, v["value"], v["source"], v["basis"], **{x: y for x, y in v.items() if x not in ("value", "source", "basis")})

write_atomic(P.investor, json.dumps(inv, indent=2, ensure_ascii=False) + "\n")
write_atomic(P.investor_sources, json.dumps(src, indent=2, ensure_ascii=False) + "\n")
print("wrote", sorted(inv))
