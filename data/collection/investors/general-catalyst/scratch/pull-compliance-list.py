#!/usr/bin/env python3
"""General Catalyst's marketing-rule investment list, parsed for the union.

/list ("All companies") is the highest-recall surface the firm publishes:
"a list of investments made by General Catalyst ... Certain investments were
excluded from this list due to confidentiality provisions ... This list is as
of June 30th, 2026." About 1,900 entries of LEGAL names, against about 600 on
the portfolio grid. Unlike Battery's list it declares exclusions, so absence
from it is strong evidence against a Form D name-match but not proof
(recorded as a coverage caveat).

The entries carry annotations that a raw join key would swallow, so each is
split into its parts and the cleaned name is what the union merges on:

  "(NYSE: HUBS)"                      ticker and exchange
  "(FKA Clvrly Learning, Inc.)"       a former name: an identity-merge lead
  "(Fig)", "(Sail)"                   the trading name, which every other layer uses
  "(Arc Token)"                       a token position beside the company
  "(Stealth Mode)"                    no public name yet
  " - RDV", "(RDV III)"               a vehicle tag on the firm's own side
  "(General Catalyst Holdings II, LLC)"  the firm's holding vehicle for the position
  "(USA)", "(Jersey)", "(Cayman)", "(2016)"  part of the legal name, dropped

Reads scratch/site-raw/list.html (pull-site-gc.py caches it). Output:
sources/site/compliance-list.json (a file_list source); the portfolio grid's
rendering is adopted as the name wherever the two surfaces name one company.
"""
import json
import re
import sys
import time
from html import unescape
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("general-catalyst")
URL = "https://www.generalcatalyst.com/list"
OUT = P.site / "compliance-list.json"

TICKER = re.compile(r"\((NASDAQ|NYSE|NYSE American|AMEX|LSE|TSX|OTC|ASX|TASE|Euronext|SIX|XETRA)[:\s]+\s*([A-Z0-9.\-]+)\)", re.I)
FKA = re.compile(r"\(\s*(?:FKA|f/k/a|formerly)\s+([^)]+)\)", re.I)
DBA = re.compile(r"\(\s*(?:dba|d/b/a)\s+([^)]+)\)", re.I)
TOKEN = re.compile(r"\(([^)]*\bToken)\)", re.I)
STEALTH = re.compile(r"\(\s*Stealth Mode\s*\)", re.I)
RDV = re.compile(r"\s*-\s*RDV\b.*$|\(\s*RDV[^)]*\)", re.I)
JURIS = re.compile(r"\(\s*(USA|US|Jersey|Cayman|Delaware|UK|Singapore|India|BVI|\d{4})\s*\)", re.I)
VEHICLE = re.compile(r"\(([^)]*General Catalyst[^)]*)\)", re.I)
PAREN = re.compile(r"\(([^)]*)\)")
LEGAL = re.compile(
    r",?\s*\b(inc|inc\.|incorporated|corp|corp\.|corporation|co|co\.|company|"
    r"ltd|ltd\.|limited|llc|l\.l\.c\.?|lp|l\.p\.?|llp|plc|gmbh|ag|a\.g\.|nv|n\.v\.|"
    r"bv|b\.v\.|sa|s\.a\.|sas|ab|oy|as|a/s|aps|kk|k\.k\.|pte|pty|srl|s\.r\.l\.|"
    r"spa|s\.p\.a\.|oyj|se|sezc|pbc|p\.b\.c\.|private limited|pvt|pte\. ltd)\b\.?\s*$", re.I)


def strip_legal(n: str) -> str:
    prev = None
    while prev != n:
        prev = n
        n = LEGAL.sub("", n).strip(" ,.")
    return n


def parse_entry(s: str) -> dict | None:
    s = re.sub(r"\s+", " ", s.replace("‍", "")).strip()
    if len(s) < 2:
        return None
    row = {"legal_name": s}
    m = TICKER.search(s)
    if m:
        row["exchange"], row["ticker"] = m.group(1).upper(), m.group(2).upper()
        s = TICKER.sub("", s)
    m = FKA.search(s)
    if m:
        row["former_name"] = strip_legal(m.group(1).strip())
        s = FKA.sub("", s)
    m = DBA.search(s)
    if m:
        row["alias"] = m.group(1).strip()
        s = DBA.sub("", s)
    m = TOKEN.search(s)
    if m:
        row["token"] = m.group(1).strip()
        s = TOKEN.sub("", s)
    if STEALTH.search(s):
        row["stealth"] = True
        s = STEALTH.sub("", s)
    if RDV.search(s):
        row["vehicle_tag"] = RDV.search(s).group(0).strip(" -()")
        s = RDV.sub("", s)
    m = VEHICLE.search(s)
    if m:
        row["held_via"] = m.group(1).strip()
        s = VEHICLE.sub("", s)
    s = JURIS.sub("", s)
    # "Physical Intelligence (Pi), Inc." keeps the full name; "Hercules Labs
    # Inc. (Fig)" is the trading name after a legal suffix.
    for p in PAREN.findall(s):
        p = p.strip()
        if not p:
            continue
        before = s[: s.find("(" + p)].strip()
        if LEGAL.search(before + " ") or re.search(r"\b(inc|llc|ltd|corp)\.?,?$", before, re.I):
            row.setdefault("alias", p)
        else:
            row.setdefault("abbrev", p)
    s = PAREN.sub("", s)
    s = re.sub(r"\s+", " ", s).strip(" ,.-")
    row["registered_name"] = strip_legal(s) or s
    row["name"] = row.get("alias") or row["registered_name"]
    return row if row["name"] else None


STOP = re.compile(r"\b(inc|corp|corporation|co|company|ltd|limited|llc|l\.l\.c|"
                  r"lp|l\.p|plc|gmbh|ag|nv|sa|holdings?|group)\b\.?", re.I)


def norm(name: str) -> str:
    """build-company-base.py's join key, mirrored."""
    n = unescape(name).lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP.sub(" ", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def norm_words(name: str) -> str:
    n = unescape(name).lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP.sub(" ", n)
    return re.sub(r"\s+", " ", n).strip()


# Words a registered name carries that the brand drops ("Abacus Labs, Inc."
# is the grid's "Abacus"; "Airbnb, Inc." is "Airbnb"). Only used for a
# unique match against the grid, never to invent a name.
TAIL = re.compile(r"\s+(labs?|technologies|technology|tech|health|ai|software|systems|"
                  r"inc|global|international|platforms?|networks?|solutions|app|hq|io|"
                  r"financial|holdings?|group|corporation|company)$", re.I)


def main() -> None:
    raw = HERE / "site-raw" / "list.html"
    h = raw.read_text(errors="replace")
    head = re.search(r'c-page-header__subheading">(.*?)</div>', h, re.S)
    caveat = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", head.group(1)))).strip() if head else ""
    i = h.find("c-all-companies__list")
    e = h.find("</div>", i)
    entries = [unescape(re.sub(r"<[^>]+>", "", x)) for x in re.findall(r"<p>(.*?)</p>", h[i:e], re.S)]
    rows, seen = [], set()
    for ent in entries:
        r = parse_entry(ent)
        if not r:
            continue
        k = re.sub(r"[^a-z0-9]+", "", r["legal_name"].lower())
        if not k or k in seen:
            continue
        seen.add(k)
        rows.append(r)

    grid = json.load(open(P.site / "company-pages.json"))["rows"]
    by_norm, by_words = {}, {}
    for c in grid:
        by_norm.setdefault(norm(c["name"]), []).append(c)
        by_words.setdefault(norm_words(c["name"]), []).append(c)
    adopted = 0
    for r in rows:
        cands = []
        for key in (r["name"], r["registered_name"], r.get("alias") or "", r.get("former_name") or ""):
            if key and not cands:
                cands = by_norm.get(norm(key), [])
        if len(cands) == 1:
            c = cands[0]
            r["grid_slug"] = c["slug"]
            if c["name"] != r["name"]:
                r["name"] = c["name"]
                adopted += 1
        r["slug"] = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
    # Second pass, grid side first: a grid name the registered name extends
    # ("Anduril" / "Anduril Industries, Inc."; "Honest Company" / "The Honest
    # Company, Inc."), joined only where exactly one unjoined list row fits and
    # that list row fits no other grid name.
    taken = {r.get("grid_slug") for r in rows if r.get("grid_slug")}
    free = [r for r in rows if not r.get("grid_slug")]
    def words(n: str) -> str:
        return re.sub(r"^the ", "", norm_words(n))
    fits: dict[int, list] = {}
    for c in grid:
        if c["slug"] in taken:
            continue
        gw = words(c["name"])
        if not gw:
            continue
        cands = [r for r in free if words(r["registered_name"]) == gw
                 or words(r["registered_name"]).startswith(gw + " ")]
        if len(cands) == 1:
            fits.setdefault(id(cands[0]), []).append((c, cands[0]))
    for pairs in fits.values():
        if len(pairs) != 1:
            continue
        c, r = pairs[0]
        r["grid_slug"] = c["slug"]
        if c["name"] != r["name"]:
            r["name"] = c["name"]
            adopted += 1
        r["slug"] = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
    # Third pass: the judged pairs (scratch/list-grid-map.json), for a
    # registered name that does not contain the brand (Maplebear is Instacart).
    judged = json.load(open(HERE / "list-grid-map.json"))["pairs"]
    by_slug = {c["slug"]: c for c in grid}
    taken = {r.get("grid_slug") for r in rows if r.get("grid_slug")}
    for r in rows:
        gs = judged.get(r["legal_name"])
        if gs and not r.get("grid_slug") and gs not in taken and gs in by_slug:
            r["grid_slug"], r["name"], r["join"] = gs, by_slug[gs]["name"], "judged"
            r["slug"] = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
            taken.add(gs)
            adopted += 1
    rows.sort(key=lambda r: r["name"].lower())
    write_atomic(OUT, json.dumps({
        "_readme": ("General Catalyst's marketing-rule list at " + URL + " ('All companies'), parsed by "
                    "scratch/pull-compliance-list.py from the page cached by pull-site-gc.py. The list's own "
                    "caveat is kept verbatim in 'caveat': it declares exclusions for confidentiality, so "
                    "absence from it is strong evidence, not proof. `legal_name` is the page's string; "
                    "`registered_name` drops legal suffixes and annotations; `name` is the portfolio grid's "
                    "rendering where the two surfaces name one company (grid_slug), else the trading name "
                    "(alias) or the registered name."),
        "_source": URL,
        "_pulled": time.strftime("%Y-%m-%d"),
        "_as_of": "2026-06-30",
        "caveat": caveat,
        "rows": rows}, indent=1, ensure_ascii=False) + "\n")
    joined = sum(1 for r in rows if r.get("grid_slug"))
    print(f"wrote {OUT}: {len(rows)} rows (from {len(entries)} entries); joined to the grid {joined}, "
          f"renamed to the grid's rendering {adopted}")
    grid_slugs = {r.get("grid_slug") for r in rows}
    print(f"grid rows not on the list: {sum(1 for c in grid if c['slug'] not in grid_slugs)}")
    for k in ("ticker", "former_name", "alias", "token", "stealth", "vehicle_tag", "held_via", "abbrev"):
        print(f"  {k}: {sum(1 for r in rows if r.get(k))}")


if __name__ == "__main__":
    main()
