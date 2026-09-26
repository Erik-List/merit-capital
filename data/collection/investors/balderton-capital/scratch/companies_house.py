#!/usr/bin/env python3
"""UK Companies House, read through the public register website.

Built in the Atomico run (PRO-79, 2026-09-26) as the UK register layer the
issue asked for; written to be investor-agnostic so it can move to scripts/
at close (COLLECTION.md §5, "When the evidence is thin, invent the layer").

Why the website and not the REST API: the API needs a registered key, the
website serves the same register to anyone. Every page read here is public:
company profiles, officer lists, officer appointment histories and filing
histories. Pages are cached under the investor's scratch/ (regenerable) and
the parsed results land under sources/registers/companies-house/ (evidence).

What the register can and cannot answer (COLLECTION.md §5 country table):
  - status: free and structured (dissolved, liquidation, administration);
  - forward enumeration: only through the OFFICER graph. A partner appointed
    director of a UK company, with the appointment dated and the service
    address on the appointment, is the register's analogue of a Form D
    related-person seat, and the same seat-dating rule applies (§1 T4);
  - backtrace (who holds this company): only inside filed documents
    (annual returns / confirmation statements list shareholders when shares
    moved), not in structured data. Read per company when a row needs it.

Pacing: one request per PACE seconds, a polite UA, no parallelism.

Usage (library first; the CLI is for spot checks):
  python3 companies_house.py company <number>
  python3 companies_house.py officers <number>
  python3 companies_house.py appointments <officer-id>
  python3 companies_house.py search-officers "<name>"
  python3 companies_house.py search-companies "<name>"
  python3 companies_house.py filings <number> [category]
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus

BASE = "https://find-and-update.company-information.service.gov.uk"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
PACE = 0.8
HERE = Path(__file__).resolve().parent
# Raw pages are re-downloadable register material, so they live beside the
# other bulk filings under data/filings/ (gitignored), not in the investor dir.
CACHE = HERE.parents[4] / "data" / "filings" / "companies-house" / "cache"
_last = [0.0]


class Unavailable(Exception):
    """A page could not be read. Never recorded as an absence."""


def _txt(s: str | None) -> str:
    if not s:
        return ""
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())


def _date(s: str) -> str:
    """'19 December 2008' -> '2008-12-19'; '22 Apr 2026' -> '2026-04-22';
    'February 1966' -> '1966-02'."""
    s = _txt(s)
    for fmt, out in (("%d %B %Y", "%Y-%m-%d"), ("%d %b %Y", "%Y-%m-%d"),
                     ("%B %Y", "%Y-%m"), ("%b %Y", "%Y-%m")):
        try:
            return datetime.strptime(s, fmt).strftime(out)
        except ValueError:
            continue
    return s


def get(path: str, max_age_days: float = 30.0) -> str:
    """One register page, cached. Raises Unavailable on anything but a 200."""
    CACHE.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(path.encode()).hexdigest()[:20]
    f = CACHE / f"{key}.html"
    if f.exists() and time.time() - f.stat().st_mtime < max_age_days * 86400:
        return f.read_text(encoding="utf-8", errors="replace")
    for attempt in range(4):
        wait = PACE - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        r = subprocess.run(["curl", "-sS", "--max-time", "60", "-A", UA,
                            "-w", "\n%{http_code}", BASE + path], capture_output=True)
        body = r.stdout.decode("utf-8", errors="replace")
        body, _, code = body.rpartition("\n")
        if r.returncode == 0 and code == "200":
            f.write_text(body, encoding="utf-8")
            return body
        if code == "404":
            raise Unavailable(f"404 {path}")
        if code == "429":
            time.sleep(30 * (attempt + 1))
            continue
        time.sleep(3 * (attempt + 1))
    raise Unavailable(f"{path}: rc={r.returncode} code={code}")


# ------------------------------------------------------------------ pages

def company(number: str) -> dict:
    t = get(f"/company/{number}")
    def dd(id_):
        m = re.search(rf'id="{id_}"[^>]*>(.*?)</(?:dd|p|span)>', t, re.S)
        return _txt(m.group(1)) if m else ""
    name = _txt((re.search(r'<p class="heading-xlarge">(.*?)</p>', t, re.S)
                 or re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S)).group(1))
    # Previous names sit in a table on the overview page: name, then the
    # period it was used ("21 Jan 2011 - 3 Mar 2015").
    prev = []
    pi = t.find("Previous company names")
    if pi > 0:
        for row in re.findall(r"<tr>(.*?)</tr>", t[pi:pi + 20000], re.S):
            cells = [_txt(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
            if len(cells) >= 2:
                a, _, b = cells[1].partition(" - ")
                prev.append({"name": cells[0], "from": _date(a), "to": _date(b)})
    sic = [_txt(s) for s in re.findall(r'id="sic\d+"[^>]*>(.*?)</span>', t, re.S)]
    detail = re.search(r'Company status</dt>.*?</dd>(.*?)</dl>', t, re.S)
    return {
        "number": number, "name": name,
        "status": dd("company-status"),
        # "Liquidation", "In Administration", "Active - Proposal to Strike off"
        # render as the status text itself; kept verbatim.
        "status_detail": _txt(detail.group(1)) if detail and "<dd" in detail.group(1) else "",
        "type": dd("company-type-value"),
        "incorporated": _date(dd("company-creation-date")),
        "dissolved": _date(dd("cessation-date")),
        "registered_office": dd("roa-address"),
        "sic": sic,
        "previous_names": prev,
        "url": f"{BASE}/company/{number}",
    }


def _blocks(t: str, cls: str) -> list[str]:
    return re.split(rf'<div class="{cls}-\d+">', t)[1:]


def officers(number: str) -> list[dict]:
    out, page = [], 1
    while True:
        t = get(f"/company/{number}/officers?page={page}")
        blocks = _blocks(t, "appointment")
        for b in blocks:
            a = re.search(r'href="/officers/([^/"]+)/appointments"[^>]*>(.*?)</a>', b, re.S)
            def f(id_):
                m = re.search(rf'id="{id_}-\d+"[^>]*>(.*?)</dd>', b, re.S)
                return _txt(m.group(1)) if m else ""
            out.append({
                "officer_id": a.group(1) if a else "", "name": _txt(a.group(2)) if a else "",
                "role": f("officer-role"), "appointed": _date(f("officer-appointed-on")),
                "resigned": _date(f("officer-resigned-on")),
                "born": _date(f("officer-date-of-birth")),
                "address": f("officer-address-value") or _txt((re.search(
                    r'id="officer-address-value-\d+"[^>]*>(.*?)</dd>', b, re.S) or [None, ""])[1]),
            })
        if f"page={page + 1}" not in t or not blocks:
            break
        page += 1
    return out


def appointments(officer_id: str) -> dict:
    """Every appointment of one officer identity, with its service address."""
    rows, page, head = [], 1, {}
    while True:
        t = get(f"/officers/{officer_id}/appointments?page={page}")
        if page == 1:
            head = {
                "officer_id": officer_id,
                "name": _txt((re.search(r'id="officer-name"[^>]*>(.*?)</h1>', t, re.S) or [None, ""])[1]),
                "born": _date((re.search(r'id="officer-date-of-birth-value"[^>]*>(.*?)</dd>', t, re.S)
                               or [None, ""])[1]),
                "total": int((re.search(r"Total number of appointments (\d+)", t) or [None, 0])[1]),
            }
        blocks = _blocks(t, "appointment")
        for b in blocks:
            comp = re.search(r'href="/company/([A-Z0-9]+)"[^>]*>(.*?)</a>', b, re.S)
            def f(pat):
                m = re.search(pat, b, re.S)
                return _txt(m.group(1)) if m else ""
            cname = _txt(comp.group(2)) if comp else ""
            rows.append({
                "company_number": comp.group(1) if comp else "",
                "company_name": re.sub(r"\s*\([A-Z0-9]+\)\s*$", "", cname),
                "company_status": f(r'id="company-status-value-\d+"[^>]*>(.*?)</dd>'),
                "role": f(r'id="appointment-type-value\d+"[^>]*>(.*?)</dd>'),
                "appointed": _date(f(r'id="appointed-value\d+"[^>]*>(.*?)</dd>')),
                "resigned": _date(f(r'id="resigned-value-?\d+"[^>]*>(.*?)</dd>')),
                "address": f(r'id="correspondence-address-value-\d+"[^>]*>(.*?)</dd>'),
            })
        if not blocks or f"page={page + 1}" not in t:
            break
        page += 1
    return {**head, "appointments": rows}


def search_officers(q: str, pages: int = 2) -> list[dict]:
    out = []
    for page in range(1, pages + 1):
        t = get(f"/search/officers?q={quote_plus(q)}&page={page}")
        items = re.findall(r'<li class="type-officer">(.*?)</li>', t, re.S)
        for it in items:
            a = re.search(r'href="/officers/([^/"]+)/appointments"[^>]*>(.*?)</a>', it, re.S)
            meta = _txt((re.search(r'<p class="meta crumbtrail">(.*?)</p>', it, re.S) or [None, ""])[1])
            addr = re.findall(r"<p>(.*?)</p>", it, re.S)
            n = re.search(r"appointments (\d+)", meta)
            b = re.search(r"Born (\w+ \d{4})", meta)
            out.append({"officer_id": a.group(1) if a else "", "name": _txt(a.group(2)) if a else "",
                        "appointments": int(n.group(1)) if n else None,
                        "born": _date(b.group(1)) if b else "",
                        "address": _txt(addr[-1]) if addr else ""})
        if len(items) < 20:
            break
    return out


def search_companies(q: str) -> list[dict]:
    t = get(f"/search/companies?q={quote_plus(q)}")
    out = []
    for m in re.finditer(r'href="/company/([A-Z0-9]+)"[^>]*>(.*?)</a>.*?<p class="meta crumbtrail">(.*?)</p>'
                         r'(?:\s*<p>(.*?)</p>)?', t, re.S):
        out.append({"number": m.group(1), "name": _txt(m.group(2)), "meta": _txt(m.group(3)),
                    "address": _txt(m.group(4))})
    return out


def filings(number: str, category: str = "", pages: int = 10) -> list[dict]:
    out = []
    for page in range(1, pages + 1):
        cat = f"&category={category}" if category else ""
        t = get(f"/company/{number}/filing-history?page={page}{cat}")
        rows = re.findall(r"<tr>\s*(<td.*?)</tr>", t, re.S)
        for r in rows:
            cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
            if len(cells) < 3:
                continue
            link = re.search(r'href="(/company/[^"]+/filing-history/[^"]+/document\?format=pdf[^"]*)"', r)
            out.append({"date": _date(cells[0]), "type": _txt(cells[1]),
                        "description": _txt(cells[2]),
                        "pdf": BASE + html.unescape(link.group(1)) if link else ""})
        if not rows or f"page={page + 1}" not in t:
            break
    return out


if __name__ == "__main__":
    cmd, *args = sys.argv[1:]
    fn = {"company": company, "officers": officers, "appointments": appointments,
          "search-officers": search_officers, "search-companies": search_companies,
          "filings": filings}[cmd]
    print(json.dumps(fn(*args), indent=1, ensure_ascii=False))
