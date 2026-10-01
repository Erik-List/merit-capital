#!/usr/bin/env python3
"""UK register status per base row (COLLECTION.md §5: "the registers pay off on
status"; decisions.md D11).

For each base row, search Companies House by the row's name and keep every
company whose name, stripped of legal suffixes, equals the row's name (or the
row's name plus one of a few trading words). Each kept candidate carries its
number, status, incorporation date and dissolution date from the search
result; the judge decides whether a candidate IS the portfolio company (era,
city, website) before using it. A search that could not be read is recorded
as failed, never as "not registered".

Output: sources/registers/companies-house/status.json {slug: {...}}
Usage: python3 ch-status.py [slug ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import companies_house as ch  # noqa: E402

INV = HERE.parent
OUT = INV / "sources" / "registers" / "companies-house" / "status.json"
BASE = INV / "companies" / "base.json"
SUFFIX = re.compile(r"\b(limited|ltd|plc|llp|lp|inc|uk|holdings?|group|technologies|technology|tech|labs?|software|app|apps|io|ai|hq|co|company|services|solutions|international|global|the)\b\.?")


def key(s: str) -> str:
    s = (s or "").lower().replace("&", "and").replace(".", " ")
    s = SUFFIX.sub(" ", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def main() -> int:
    only = set(sys.argv[1:])
    base = json.loads(BASE.read_text())
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    failed = 0
    for n, r in enumerate(base, 1):
        s = r["slug"]
        if only and s not in only:
            continue
        if s in out and out[s].get("status") == "ok":
            continue
        k = key(r["name"])
        if len(k) < 3:
            out[s] = {"status": "skipped", "why": "name too short to search"}
            continue
        try:
            res = ch.search_companies(r["name"])
        except ch.Unavailable as e:
            out[s] = {"status": "failed", "why": str(e)}
            failed += 1
            continue
        cands = []
        for c in res:
            if key(c["name"]) == k:
                meta = c.get("meta", "")
                m_inc = re.search(r"(Incorporated|Registered) on (\d+ \w+ \d{4})", meta)
                m_dis = re.search(r"Dissolved on (\d+ \w+ \d{4})", meta)
                cands.append({"number": c["number"], "name": c["name"], "meta": meta,
                              "address": c.get("address"),
                              "incorporated": ch._date(m_inc.group(2)) if m_inc else None,
                              "dissolved": ch._date(m_dis.group(1)) if m_dis else None,
                              "url": f"{ch.BASE}/company/{c['number']}"})
        out[s] = {"status": "ok", "name": r["name"], "candidates": cands}
        if n % 25 == 0:
            OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
            print(n, flush=True)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    hits = sum(1 for v in out.values() if v.get("candidates"))
    print("done", len(out), "rows,", hits, "with a same-name UK company,", failed, "failed", flush=True)
    return 3 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
