#!/usr/bin/env python3
"""formd.py <cik>/<accession-nodash>... : print key fields of a Form D primary_doc.xml (raw fetch through secget throttle, no cache parse loss)."""
import sys, re, subprocess, importlib.util
from pathlib import Path
H = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(H.parents[4] / "scripts"))
import shared_throttle
for p in sys.argv[1:]:
    shared_throttle.wait("sec")
    r = subprocess.run(["curl", "-sL", "-m", "60", "-H", "User-Agent: Merit Capital research erik@meritcapit.al", f"https://www.sec.gov/Archives/edgar/data/{p}/primary_doc.xml"], capture_output=True, text=True).stdout
    g = lambda tag: re.findall(rf"<{tag}>([^<]*)</{tag}>", r)
    print("==", p, g("entityName")[:1], "| first sale:", g("value")[:1] or g("dateOfFirstSale")[:1], "| yetToOccur:", g("yetToOccur"), "| offered:", g("totalOfferingAmount"), "| sold:", g("totalAmountSold"), "| investors:", g("totalNumberAlreadyInvested"), "| signed:", g("signatureDate"), "| min inv:", g("minimumInvestmentAccepted"))
    print("   persons:", [a + " " + b for a, b in zip(g("firstName"), g("lastName"))])
