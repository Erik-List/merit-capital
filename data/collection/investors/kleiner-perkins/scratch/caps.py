#!/usr/bin/env python3
"""A/B pass A for the public rows (COLLECTION.md s6/s7): every public member carries a market cap, web-cited, with an
as-of date, from stockanalysis.com (the aggregator the landed runs cite). Ticker from SEC's company_tickers.json by
the row's own CIK, else from the firm's exit line ("NASDAQ: NET"), else from the ticker map below. Writes
scratch/caps.json {slug: {ticker, url, usd, asof, status}} and prints rows it could not price. A failed fetch is an
error, never a zero.
Usage: python3 caps.py [--emit]   (--emit writes judgments-caps.py lines through judge_lib and records them)
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import shared_throttle  # noqa: E402

INV = HERE.parent
TODAY = time.strftime("%Y-%m-%d")
UA = "Merit Capital research erik@meritcapit.al"
BROWSER = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/128.0 Safari/537.36")
MANUAL = {}


def get(url, sec=False):
    for attempt in range(3):
        if sec:
            shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA if sec else BROWSER, url], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode("utf-8", "replace")
        time.sleep(2 * (attempt + 1))
    return ""


def cap_of(page):
    """The page's own sentence: "... has a market cap or net worth of $124.47 billion as of September 30, 2026." """
    import datetime
    m = re.search(r"market cap or net worth of \$([\d.,]+) (trillion|billion|million) as of ([A-Z][a-z]+ \d{1,2}, \d{4})",
                  page)
    if not m:
        return None, None
    v = float(m.group(1).replace(",", "")) * {"trillion": 1e12, "billion": 1e9, "million": 1e6}[m.group(2)]
    d = datetime.datetime.strptime(m.group(3), "%B %d, %Y").strftime("%Y-%m-%d")
    return v, d


def main():
    led = json.loads((INV / "companies/membership-ledger.json").read_text())["kleiner-perkins"]["verdicts"]
    C = json.loads((INV / "companies/classification.json").read_text())
    C = C.get("kleiner-perkins", C)
    R = json.loads((INV / "companies/resolved.json").read_text())
    R = R.get("kleiner-perkins", R)
    base = {r["slug"]: r for r in json.loads((INV / "companies/base.json").read_text())}
    site = {r["url"]: r for r in json.loads((INV / "sources/site/company-list.json").read_text())["rows"]}
    tick = json.loads(get("https://www.sec.gov/files/company_tickers.json", sec=True))
    by_cik = {str(v["cik_str"]): v["ticker"] for v in tick.values()}
    out_p = HERE / "caps.json"
    out = json.loads(out_p.read_text()) if out_p.exists() else {}
    for s, v in led.items():
        if v.get("verdict") != "member" or s not in base:
            continue
        m = {**R.get(s, {}), **C.get(s, {})}
        if m.get("status") != "public":
            continue
        if (out.get(s) or {}).get("status") == "ok":
            continue
        row = base[s]
        path = MANUAL.get(s)
        t = None
        if not path:
            cik = str(int(row["edgar_cik"])) if row.get("edgar_cik") else ""
            t = by_cik.get(cik)
            if not t:
                # the firm's CMS puts the ticker in since_caption on IPO rows ("TWTR", "ABNB")
                ex = (site.get(row.get("site_url")) or {}).get("acquirer") or ""
                t = ex if re.fullmatch(r"[A-Z]{1,5}", ex) else None
            path = f"stocks/{t.lower()}" if t else None
        if not path:
            out[s] = {"status": "no_ticker"}
            continue
        url = f"https://stockanalysis.com/{path}/market-cap/"
        page = get(url)
        time.sleep(0.8)
        usd, asof = cap_of(page)
        out[s] = {"ticker": t or path, "url": url, "usd": usd, "asof": asof or TODAY,
                  "status": "ok" if usd else "unparsed", "stored_usd": m.get("valuation_usd"),
                  "stored_src": m.get("valuation_source")}
        print(s, t, usd, flush=True)
    out_p.write_text(json.dumps(out, indent=1) + "\n")
    bad = {s: v for s, v in out.items() if v.get("status") != "ok"}
    print(len(out), "public rows;", len(bad), "unpriced:", sorted(bad))


if __name__ == "__main__":
    main()
