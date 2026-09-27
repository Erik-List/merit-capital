#!/usr/bin/env python3
"""Registered-fund holdings layer: N-PORT and N-CSR of the investor's own
1940-Act vehicles (PRO-78; N-CSR was on the untested-layers list since Thrive).

A firm that runs a registered fund (an interval or tender-offer fund sold to
wealth clients) discloses that fund's WHOLE portfolio: N-PORT lists every
position each quarter with its fair value, a restricted-security flag and the
fair-value level, and N-CSR / N-CSRS carry the audited schedule of investments,
whose restricted-securities note gives the ACQUISITION DATE and cost of each
private position. That is filing-grade evidence that a fund of the firm holds
a private company (T2), dated, and a valuation MARK (a fair value, not a priced
round: it goes to the note under Rule A, never to the band).

Reads the CIKs in config `edgar.registered_fund_ciks` through the submissions
API, fetches every NPORT-P primary_doc.xml and every N-CSR / N-CSRS primary
document, and writes:

  sources/edgar/registered-fund-holdings.json
    {"_readme", "funds": {cik: {name, former_names, nport: [{accession, period,
      filed, total_assets, net_assets, positions: [{name, title, value_usd, pct,
      asset_cat, restricted, fair_value_level, country, cusip, isin}]}],
      ncsr: [{accession, form, period, filed, url, restricted_text}]}},
     "restricted": {norm_name: {name, first_period, last_period, last_value_usd,
                                periods[], ncsr_lines[]}}}

Usage: python3 scripts/edgar-registered-fund.py <investor-slug> [--refresh]
"""
from __future__ import annotations
import html as htmlmod
import json, re, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shared_throttle  # noqa: E402
from paths import Paths, ROOT, write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"


def get(url: str, tries: int = 4) -> bytes:
    for attempt in range(tries):
        shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-sS", "--max-time", "180", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code == b"200":
            return body
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url}")


def norm(name: str) -> str:
    n = re.sub(r"[^a-z0-9 ]+", " ", name.lower())
    n = re.sub(r"\b(inc|corp|corporation|co|ltd|plc|llc|lp|sa|nv|ag|holdings?|group|series [a-z0-9 ]+|preferred stock|preferred|common stock|common|class [a-z]|cl [a-z])\b", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def tag(b: str, t: str) -> str:
    m = re.search(rf"<{t}>(.*?)</{t}>", b, re.S)
    return m.group(1).strip() if m else ""


def parse_nport(xml: str) -> dict:
    positions = []
    for b in re.findall(r"<invstOrSec>(.*?)</invstOrSec>", xml, re.S):
        try:
            val = float(tag(b, "valUSD") or 0)
        except ValueError:
            val = 0.0
        positions.append({"name": tag(b, "name"), "title": tag(b, "title"), "value_usd": val, "pct": tag(b, "pctVal"),
                          "asset_cat": tag(b, "assetCat"), "issuer_cat": tag(b, "issuerCat"), "restricted": tag(b, "isRestrictedSec"),
                          "fair_value_level": tag(b, "fairValLevel"), "country": tag(b, "invCountry"),
                          "cusip": tag(b, "cusip"), "isin": tag(b, "isin"), "lei": tag(b, "lei")})
    return {"period": tag(xml, "repPdDate"), "total_assets": tag(xml, "totAssets"), "net_assets": tag(xml, "netAssets"),
            "positions": positions}


def html_text(h: str) -> str:
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)</(p|div|tr|li|h\d|br)\s*>", "\n", h)
    h = re.sub(r"(?i)</t[dh]\s*>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = htmlmod.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    return re.sub(r"\n\s*\n+", "\n", h)


def restricted_sections(text: str) -> list[str]:
    """Every passage that reads like a restricted-securities schedule: the
    paragraphs around 'restricted' that carry acquisition dates."""
    out = []
    for m in re.finditer(r"(?i)restricted securit", text):
        seg = text[max(0, m.start() - 400): m.start() + 6000]
        if re.search(r"\d{1,2}/\d{1,2}/\d{2,4}|\b(19|20)\d{2}\b", seg):
            out.append(seg)
    # dedupe overlapping windows
    uniq = []
    for s in out:
        if not any(s[:300] in u for u in uniq):
            uniq.append(s)
    return uniq


def main() -> None:
    slug = sys.argv[1]
    P = Paths(slug)
    cfg = P.config()
    ciks = [str(int(c)) for c in cfg.get("edgar", {}).get("registered_fund_ciks", [])]
    if not ciks:
        sys.exit("config edgar.registered_fund_ciks is empty")
    cache = P.root / "scratch" / "registered-fund-raw"
    cache.mkdir(parents=True, exist_ok=True)
    refresh = "--refresh" in sys.argv
    funds, restricted = {}, {}
    for cik in ciks:
        sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
        f = sub["filings"]["recent"]
        rec = {"name": sub.get("name"), "former_names": [n["name"] for n in sub.get("formerNames", [])], "nport": [], "ncsr": []}
        for k in range(len(f["form"])):
            form, acc, fd, rd, doc = f["form"][k], f["accessionNumber"][k], f["filingDate"][k], f["reportDate"][k], f["primaryDocument"][k]
            accn = acc.replace("-", "")
            if form in ("NPORT-P", "NPORT-P/A"):
                raw = cache / f"{acc}.xml"
                if not raw.exists() or refresh:
                    raw.write_bytes(get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/primary_doc.xml"))
                p = parse_nport(raw.read_text("utf-8", "replace"))
                p.update({"accession": acc, "form": form, "filed": fd})
                rec["nport"].append(p)
                for pos in p["positions"]:
                    if pos["restricted"] != "Y":
                        continue
                    key = norm(pos["name"])
                    e = restricted.setdefault(key, {"name": pos["name"], "periods": [], "first_period": p["period"],
                                                    "last_period": p["period"], "last_value_usd": 0.0, "titles": [], "ncsr_lines": []})
                    if p["period"] not in e["periods"]:
                        e["periods"].append(p["period"])
                    if pos["title"] not in e["titles"]:
                        e["titles"].append(pos["title"])
                    e["first_period"] = min(e["first_period"], p["period"])
                    if p["period"] > e["last_period"]:
                        e["last_period"], e["last_value_usd"] = p["period"], 0.0
                    if p["period"] == e["last_period"]:
                        e["last_value_usd"] += pos["value_usd"]
                print(f"  {cik} {form} {p['period']}: {len(p['positions'])} positions, "
                      f"{sum(1 for x in p['positions'] if x['restricted']=='Y')} restricted", file=sys.stderr)
            elif form in ("N-CSR", "N-CSRS", "N-CSR/A", "N-CSRS/A"):
                raw = cache / f"{acc}.htm"
                url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/{doc}"
                if not raw.exists() or refresh:
                    raw.write_bytes(get(url))
                text = html_text(raw.read_text("utf-8", "replace"))
                secs = restricted_sections(text)
                rec["ncsr"].append({"accession": acc, "form": form, "period": rd, "filed": fd, "url": url,
                                    "restricted_text": secs})
                for s in secs:
                    for key, e in restricted.items():
                        for line in s.splitlines():
                            if e["name"].split()[0].lower() in line.lower() and re.search(r"\d{1,2}/\d{1,2}/\d{2,4}", line):
                                if line.strip() not in e["ncsr_lines"]:
                                    e["ncsr_lines"].append(line.strip()[:300])
                print(f"  {cik} {form} {rd}: {len(secs)} restricted-securities passages", file=sys.stderr)
        rec["nport"].sort(key=lambda x: x["period"])
        rec["ncsr"].sort(key=lambda x: x["period"])
        funds[cik] = rec
    for e in restricted.values():
        e["periods"].sort()
    out = P.edgar / "registered-fund-holdings.json"
    write_atomic(out, json.dumps({"_readme": __doc__.strip(), "funds": funds,
                                  "restricted": dict(sorted(restricted.items()))}, indent=1))
    print(f"wrote {out.relative_to(ROOT)}: {len(restricted)} restricted issuers")


if __name__ == "__main__":
    main()
