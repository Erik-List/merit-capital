"""Persons with significant control, read from the public Companies House page (used by register-uk-psc.py)."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import companies_house as ch

def pscs(number):
    t = ch.get(f"/company/{number}/persons-with-significant-control")
    res = []
    for b in re.split(r'<div class="appointment-\d+">', t)[1:]:
        name = ch._txt((re.search(r'<span class="heading-medium[^"]*"[^>]*>(.*?)</span>', b, re.S) or re.search(r"<b>(.*?)</b>", b, re.S) or [None, ""])[1])
        status = "ceased" if re.search(r"Ceased", b) else "active"
        notified = ch._txt((re.search(r'Notified on</dt>\s*<dd[^>]*>(.*?)</dd>', b, re.S) or [None, ""])[1])
        ceased = ch._txt((re.search(r'Ceased on</dt>\s*<dd[^>]*>(.*?)</dd>', b, re.S) or [None, ""])[1])
        kind = "corporate" if re.search(r"Legal form|Registration number|Governing law", b) else "person"
        nature = [ch._txt(x) for x in re.findall(r'<dd[^>]*id="psc-noc[^"]*"[^>]*>(.*?)</dd>', b, re.S)][:3]
        res.append({"name": name, "kind": kind, "status": status, "notified": ch._date(notified) if notified else "", "ceased": ch._date(ceased) if ceased else "", "nature": nature})
    return res
