#!/usr/bin/env python3
"""Company status from the Nordic home registers (COLLECTION.md §5: "the
registers pay off on status"). Filing-grade `defunct` evidence where the
register records a bankruptcy, a liquidation or a deletion; the register's own
page is the citation. Answers cached under data/filings/northzone/registers.

  Norway  data.brreg.no/enhetsregisteret/api/enheter  (search: live entities;
          /enheter/<orgnr> answers 410 with slettedato for a deleted one)
  Finland avoindata.prh.fi/opendata-ytj-api/v3/companies (name history too)
  Denmark cvrapi.dk/api (free, rate-limited; enddate, creditbankrupt)

Sweden has no free structured status endpoint that answers a script
(allabolag.se 403, 2026-09-29), so Swedish status stays with press and the
judge. Usage: python3 nordic_status.py no|fi|dk "<name or number>"
"""
import hashlib
import json
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

CACHE = Path(__file__).resolve().parents[5] / "data" / "filings" / "northzone" / "registers"
CACHE.mkdir(parents=True, exist_ok=True)
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"


def _get(url: str) -> tuple[int, str]:
    f = CACHE / (hashlib.sha1(url.encode()).hexdigest() + ".json")
    if f.exists():
        d = json.loads(f.read_text())
        return d["code"], d["body"]
    r = subprocess.run(["curl", "-sS", "-A", UA, "--max-time", "30", "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    code = int(code or 0)
    if code in (200, 404, 410):
        f.write_text(json.dumps({"url": url, "code": code, "body": body}))
    time.sleep(0.5)
    return code, body


def norway(q: str) -> list[dict]:
    if q.isdigit() and len(q) == 9:
        code, body = _get(f"https://data.brreg.no/enhetsregisteret/api/enheter/{q}")
        d = json.loads(body) if body.strip().startswith("{") else {}
        return [{"register": "brreg", "orgnr": q, "http": code, "name": d.get("navn"),
                 "deleted": d.get("slettedato"), "bankrupt": d.get("konkurs"),
                 "liquidation": d.get("underAvvikling"), "founded": d.get("stiftelsesdato"),
                 "url": f"https://data.brreg.no/enhetsregisteret/oppslag/enheter/{q}"}]
    code, body = _get("https://data.brreg.no/enhetsregisteret/api/enheter?size=20&navn="
                      + urllib.parse.quote(q))
    out = []
    for e in (json.loads(body).get("_embedded", {}).get("enheter", []) if code == 200 else []):
        out.append({"register": "brreg", "orgnr": e["organisasjonsnummer"], "name": e["navn"],
                    "bankrupt": e.get("konkurs"), "liquidation": e.get("underAvvikling"),
                    "founded": e.get("stiftelsesdato"), "city": (e.get("forretningsadresse") or {}).get("poststed"),
                    "url": f"https://data.brreg.no/enhetsregisteret/oppslag/enheter/{e['organisasjonsnummer']}"})
    return out


def finland(q: str) -> list[dict]:
    code, body = _get("https://avoindata.prh.fi/opendata-ytj-api/v3/companies?name=" + urllib.parse.quote(q))
    out = []
    for c in (json.loads(body).get("companies", []) if code == 200 else []):
        names = sorted(c.get("names", []), key=lambda n: n.get("registrationDate", ""))
        bid = c["businessId"]["value"]
        out.append({"register": "prh", "business_id": bid,
                    "names": [(n["name"], n.get("registrationDate"), n.get("endDate")) for n in names],
                    "status": c.get("status"), "trade_register_status": c.get("tradeRegisterStatus"),
                    "situations": c.get("companySituations"), "ended": c.get("endDate"),
                    "url": f"https://tietopalvelu.ytj.fi/yritys/{bid}"})
    return out


def denmark(q: str) -> list[dict]:
    code, body = _get("https://cvrapi.dk/api?country=dk&search=" + urllib.parse.quote(q))
    if code != 200 or not body.strip().startswith("{"):
        return [{"register": "cvr", "http": code, "error": body[:200]}]
    d = json.loads(body)
    return [{"register": "cvr", "cvr": d.get("vat"), "name": d.get("name"), "start": d.get("startdate"),
             "end": d.get("enddate"), "bankrupt": d.get("creditbankrupt"), "credit_status": d.get("creditstatus"),
             "owners": [o.get("name") for o in d.get("owners") or []], "city": d.get("city"),
             "url": f"https://datacvr.virk.dk/enhed/virksomhed/{d.get('vat')}"}]


if __name__ == "__main__":
    fn = {"no": norway, "fi": finland, "dk": denmark}[sys.argv[1]]
    print(json.dumps(fn(sys.argv[2]), indent=1, ensure_ascii=False))
