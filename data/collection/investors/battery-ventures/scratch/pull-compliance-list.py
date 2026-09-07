#!/usr/bin/env python3
"""Battery's marketing-rule compliance list, parsed rather than regexed raw.

/list-of-all-companies/ is the highest-recall surface Battery publishes: 679
entries headed "All investments as of Q1 2026", with no declared exclusions,
covering the whole 1983-2026 book including companies no portfolio page has
carried for twenty years (@Stake, Concord Data Systems, CONXUS, Fore Systems).

It publishes FULL LEGAL names with four annotations that a raw regex would
carry into the join key and break it -- "Coinbase Global, Inc. (NASDAQ: COIN) *"
must key as "coinbase", not "coinbaseglobalnasdaqcoin". So each entry is split
into its parts here and the cleaned name is what the union merges on:

  trailing " *"    the page's own legend: "Denotes an exited investment."
  "(NASDAQ: X)"    ticker and exchange -- filing-grade for status=public
  "(dba X)"        the trading name, usually the name every other layer uses
  "(X Inc.)"       a successor or acquirer entity, which is an identity merge

Output: sources/site/compliance-list.json (a file_list source).
"""
import json
import re
import subprocess
import sys
import time
from collections import Counter
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = "merit-capital-research/1.0 (list.erik.2005@gmail.com)"
URL = "https://www.battery.com/list-of-all-companies/"
P = Paths("battery-ventures")
OUT = P.site / "compliance-list.json"

ROW = re.compile(r'<p>\s*<span style="font-weight: 400;">(.*?)</span>\s*</p>', re.S)
ROW_BR = re.compile(r"([^<>\n]{2,140}?)\s*<br\s*/?>")
TICKER = re.compile(r"\((NASDAQ|NYSE|NYSE American|AMEX|LSE|TSX|OTC|ASX|TASE|"
                    r"Euronext|SIX|XETRA)[:\s]+\s*([A-Z0-9.\-]+)\)", re.I)
DBA = re.compile(r"\(\s*(?:dba|d/b/a|formerly|f/k/a|now)\s+([^)]+)\)", re.I)
PAREN = re.compile(r"\(([^)]*)\)")
LEGAL = re.compile(
    r",?\s*\b(inc|inc\.|incorporated|corp|corp\.|corporation|co|co\.|company|"
    r"ltd|ltd\.|limited|llc|l\.l\.c\.?|lp|l\.p\.?|llp|plc|gmbh|ag|a\.g\.|nv|n\.v\.|"
    r"bv|b\.v\.|sa|s\.a\.|sas|ab|oy|as|a/s|aps|kk|k\.k\.|pte|pty|srl|s\.r\.l\.|"
    r"spa|s\.p\.a\.|oyj|se)\b\.?\s*$", re.I)


def fetch(url: str, tries: int = 4) -> str:
    for i in range(tries):
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", "replace")
        except subprocess.CalledProcessError:
            if i == tries - 1:
                return ""
            time.sleep(1.5 * (i + 1))
    return ""


def strip_legal(n: str) -> str:
    prev = None
    while prev != n:                      # "Cohesity Global, Inc." -> "Cohesity"
        prev = n
        n = LEGAL.sub("", n).strip(" ,.")
    return n


def parse_entry(raw: str) -> dict | None:
    s = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", raw))).strip()
    if len(s) < 2:
        return None
    row = {"legal_name": s}
    if s.rstrip().endswith("*"):
        row["exited"] = True
        s = s.rstrip().rstrip("*").strip()
        row["legal_name"] = s
    m = TICKER.search(s)
    if m:
        row["exchange"], row["ticker"] = m.group(1).upper(), m.group(2).upper()
        s = TICKER.sub("", s).strip()
    m = DBA.search(s)
    if m:
        row["alias"] = m.group(1).strip()
        s = DBA.sub("", s).strip()
    for p in PAREN.findall(s):            # a bare parenthetical is a successor
        p = p.strip()
        if p and not row.get("alias"):
            row["successor"] = p
    s = PAREN.sub("", s).strip(" ,.")
    row["name"] = strip_legal(s) or s
    # A dba is the name every other layer uses; prefer it for the join.
    if row.get("alias"):
        row["name"], row["registered_name"] = row["alias"], row["name"]
    return row if row["name"] else None


STOP = re.compile(r"\b(inc|corp|corporation|co|company|ltd|limited|llc|l\.l\.c|"
                  r"lp|l\.p|plc|gmbh|ag|nv|sa|holdings?|group)\b\.?", re.I)


def norm(name: str) -> str:
    """build-company-base.py's join key, mirrored so this layer lands on the
    SAME key the base will use -- otherwise 'Cohesity Global, Inc.' and the
    portfolio page's 'Cohesity' publish as two rows."""
    n = unescape(name).lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP.sub(" ", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def norm_words(name: str) -> str:
    """norm() keeping word boundaries, for the prefix compare."""
    n = unescape(name).lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP.sub(" ", n)
    return re.sub(r"\s+", " ", n).strip()


def main() -> None:
    html = fetch(URL)
    entries = ROW.findall(html) or ROW_BR.findall(html)
    rows, seen = [], set()
    for e in entries:
        r = parse_entry(e)
        if not r:
            continue
        k = re.sub(r"[^a-z0-9]+", "", r["name"].lower())
        if not k or k in seen:
            continue
        seen.add(k)
        r["slug"] = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
        rows.append(r)
    # The portfolio surface owns the display name where both carry the row:
    # the compliance list publishes registered names ("Cohesity Global, Inc."),
    # the company pages publish the name the firm actually renders ("Cohesity"),
    # and the union keys on the string. Adopt the site's rendering on a norm()
    # match so the two surfaces corroborate one row instead of publishing two.
    detail = P.site / "company-pages.json"
    adopted = 0
    if detail.exists():
        by_norm = {}
        for c in json.load(open(detail))["rows"]:
            by_norm.setdefault(norm(c["name"]), c["name"])
        by_words = {}
        for c in json.load(open(detail))["rows"]:
            by_words.setdefault(norm_words(c["name"]), []).append(c["name"])
        for r in rows:
            site_name = by_norm.get(norm(r["name"]))
            if not site_name:
                # The compliance list publishes the REGISTERED name and the
                # portfolio page the rendered one ("Coinbase Global, Inc." vs
                # "Coinbase"), and norm() does not join them because "Global"
                # is not a legal suffix. build-company-base.py would merge them
                # on its own norm_words prefix rule -- except that rule treats
                # two names co-listed in ONE surface as proof of distinctness,
                # and unioning both here is exactly that. So the prefix match
                # happens at the source instead. Unique matches only.
                kw = norm_words(r["name"])
                cands = [nm for w, names in by_words.items()
                         if w and kw.startswith(w + " ") and len(names) == 1
                         for nm in names]
                site_name = cands[0] if len(cands) == 1 else None
            if site_name and site_name != r["name"]:
                r["registered_name"] = r.get("registered_name") or r["name"]
                r["name"] = site_name
                r["slug"] = re.sub(r"[^a-z0-9]+", "-", site_name.lower()).strip("-")
                adopted += 1
    print(f"  adopted the portfolio page's rendering for {adopted} rows")

    rows.sort(key=lambda r: r["name"].lower())
    write_atomic(OUT, json.dumps({
        "_readme": (
            "Battery's marketing-rule compliance list at " + URL + ", parsed by "
            "scratch/pull-compliance-list.py. Page header: 'All investments as of "
            "Q1 2026'; page legend: '* Denotes an exited investment.' No exclusions "
            "are declared on the page, unlike a16z's permission-limited list. "
            "`name` is the cleaned join name (legal suffix, ticker and parenthetical "
            "removed, a dba preferred); `legal_name` keeps the page's own string."),
        "_source": URL,
        "_pulled": time.strftime("%Y-%m-%d"),
        "_as_of": "Q1 2026",
        "rows": rows}, indent=1))
    print(f"wrote {OUT}: {len(rows)} rows (from {len(entries)} entries)")
    print("  exited(*):", sum(1 for r in rows if r.get("exited")))
    print("  ticker:", sum(1 for r in rows if r.get("ticker")),
          " alias:", sum(1 for r in rows if r.get("alias")),
          " successor:", sum(1 for r in rows if r.get("successor")))
    print("  sample:", [r["name"] for r in rows[:8]])


if __name__ == "__main__":
    main()
