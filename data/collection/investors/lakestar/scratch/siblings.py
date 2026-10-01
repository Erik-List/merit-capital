#!/usr/bin/env python3
"""Sibling rows: what the other investors' published books say about the
companies Lakestar holds. Joins on the loose name key (lowercase, legal suffix
and punctuation stripped), the key verify's rule 10 uses, so a hit here is a
pair the cross-investor check will compare.

Writes scratch/siblings.json {slug: [{investor, name, status, valuation_range,
valuation_usd, valuation_asof, valuation_source, valuation_citation, hq_city,
hq_country, focus, entry_stage, entry_date, seed_to_a_graduation, note}]}.
Usage: python3 siblings.py [name ...]   (no names: every company in
archive-evidence.json, companies-2026.json and base.json if present)
"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
INVESTORS = INV.parent
STOP = re.compile(r"\b(inc|corp|corporation|co|company|ltd|limited|llc|l\.l\.c|lp|l\.p|plc|gmbh|ag|nv|sa|se|"
                  r"holdings?|group|technologies|technology|labs?|health|hq)\b\.?", re.I)
KEEP = ("name", "status", "valuation_range", "valuation_usd", "valuation_asof", "valuation_source",
        "valuation_citation", "hq_city", "hq_country", "focus", "entry_stage", "entry_stage_source",
        "entry_date", "seed_to_a_graduation", "membership_verdict", "note")


def key(name: str) -> str:
    n = re.sub(r"\([^)]*\)", " ", name.lower())
    n = re.sub(r"\.(com|io|ai|de|co|app|earth)\b", " ", n)
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP.sub(" ", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def names() -> dict[str, str]:
    out = {}
    b = INV / "companies" / "base.json"
    if b.exists():
        for r in json.loads(b.read_text()):
            out[r["slug"]] = r["name"]
        return out
    ev = INV / "sources" / "wayback" / "archive-evidence.json"
    if ev.exists():
        for s, e in json.loads(ev.read_text())["companies"].items():
            out[s] = e["name"]
    site = INV / "sources" / "site" / "companies-2026.json"
    if site.exists():
        for r in json.loads(site.read_text())["rows"]:
            out.setdefault(re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-"), r["name"])
    return out


def main() -> None:
    idx: dict[str, list[dict]] = {}
    for d in sorted(INVESTORS.iterdir()):
        f = d / "companies" / "base.csv"
        if d.name == "lakestar" or not f.exists():
            continue
        with open(f, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                k = key(r.get("name") or "")
                if k:
                    rec = {c: r.get(c, "") for c in KEEP}
                    rec["investor"] = d.name
                    idx.setdefault(k, []).append(rec)
    wanted = {re.sub(r"[^a-z0-9]+", "-", a.lower()).strip("-"): a for a in sys.argv[1:]} or names()
    out = {}
    for slug, name in sorted(wanted.items()):
        hits = idx.get(key(name)) or []
        if hits:
            out[slug] = hits
    if not sys.argv[1:]:
        (HERE / "siblings.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(out)} of {len(wanted)} companies sit in at least one sibling book")
    for slug, hits in out.items():
        line = "; ".join(f"{h['investor']}:{h['status']}/{h['valuation_range']}"
                         + (f"/${float(h['valuation_usd'])/1e9:.1f}B" if h['valuation_usd'] else "") for h in hits)
        print(f"  {wanted[slug][:24]:24s} {line[:230]}")


if __name__ == "__main__":
    main()
