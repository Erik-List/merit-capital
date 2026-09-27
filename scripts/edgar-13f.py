#!/usr/bin/env python3
"""13F holdings layer: the investor's public book, quarter by quarter (PRO-78).

A crossover manager files Form 13F-HR every quarter for the exchange-traded
securities it holds. COLLECTION.md 1 rules that a position which first appears
as a 13F holding and never entered through a venture round is NOT a member (T3),
so this layer never seeds membership. What it gives the run:

  * a public-status corroboration for a member row: a 13F line is, by
    definition, an exchange-traded security, so a company on it has listed;
  * a first-seen quarter per issuer, which dates when the position became
    public (a member entered privately shows up here only after its IPO);
  * the recall trigger for the crossover blind spot: a 13F issuer whose IPO
    postdates the firm's private activity is CHECKED for a pre-IPO round
    (the judge's question), never admitted on the 13F alone.

Reads every 13F-HR / 13F-HR/A of the CIKs in config `edgar.thirteenf_ciks`
through the submissions API, then each filing's information table (XML from
2013Q2; the earlier text-table filings are parsed loosely and marked
`legacy`). Values are normalised to dollars per filing by an implied price
test: a 13F table reports a value and a share count per line, so the median
value per share of a filing is a share price (tens to hundreds of dollars)
when the table is in dollars and a thousandth of one when it is in thousands.
The rule of the form (thousands before 2023Q1, dollars after) is not safe on
its own: Coatue's five filings of 2001 are in dollars, its 2002 to 2022
filings in thousands. A filing total was tried first as the test and failed
on exactly those five (a $43M book read as $43B).

Output: sources/edgar/13f-holdings.json
  {"_readme", "filers": {cik: {name, filings: [{accession, period, filed, positions}]}},
   "issuers": {norm_name: {name, cusips[], classes[], first_period, last_period,
                           periods, max_value_usd, last_value_usd}}}
Usage: python3 scripts/edgar-13f.py <investor-slug> [--refresh]
"""
from __future__ import annotations
import json, re, subprocess, sys, time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shared_throttle  # noqa: E402
from paths import Paths, ROOT, write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"


def get(url: str, tries: int = 4) -> bytes:
    for attempt in range(tries):
        shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-sS", "--max-time", "120", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code == b"200":
            return body
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url}")


def norm(name: str) -> str:
    n = name.lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = re.sub(r"\b(inc|corp|corporation|co|ltd|plc|llc|lp|sa|nv|ag|holdings?|hldgs?|group|grp|new|com|cl a|class a|adr|ads)\b", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def parse_xml_table(xml: str) -> list[dict]:
    rows = []
    for b in re.findall(r"<(?:\w+:)?infoTable>(.*?)</(?:\w+:)?infoTable>", xml, re.S):
        def tag(t):
            m = re.search(rf"<(?:\w+:)?{t}>(.*?)</(?:\w+:)?{t}>", b, re.S)
            return m.group(1).strip() if m else ""
        try:
            val = float(tag("value") or 0)
        except ValueError:
            val = 0.0
        rows.append({"issuer": tag("nameOfIssuer"), "class": tag("titleOfClass"), "cusip": tag("cusip"),
                     "value": val, "shares": tag("sshPrnamt"), "sh_type": tag("sshPrnamtType"),
                     "put_call": tag("putCall"), "discretion": tag("investmentDiscretion")})
    return rows


def parse_legacy_table(txt: str) -> list[dict]:
    """Pre-2013 13F text tables: NAME OF ISSUER / TITLE OF CLASS / CUSIP / VALUE / SHARES.
    Lines are fixed-width-ish; keep any line with a 9-char CUSIP followed by numbers."""
    rows = []
    for line in txt.splitlines():
        m = re.match(r"^(?P<issuer>.{1,40}?)\s{2,}(?P<cls>.{1,20}?)\s{2,}(?P<cusip>[0-9A-Z]{6}[0-9A-Z]{2}[0-9])\s+(?P<value>[\d,]+)\s+(?P<shares>[\d,]+)", line.strip())
        if not m:
            continue
        rows.append({"issuer": m["issuer"].strip(), "class": m["cls"].strip(), "cusip": m["cusip"],
                     "value": float(m["value"].replace(",", "")), "shares": m["shares"].replace(",", ""),
                     "legacy": True})
    return rows


def main() -> None:
    slug = sys.argv[1]
    P = Paths(slug)
    cfg = P.config()
    ciks = [str(int(c)) for c in cfg.get("edgar", {}).get("thirteenf_ciks", [])]
    if not ciks:
        sys.exit("config edgar.thirteenf_ciks is empty")
    out_path = P.edgar / "13f-holdings.json"
    cache = P.root / "scratch" / "13f-raw"
    cache.mkdir(parents=True, exist_ok=True)
    refresh = "--refresh" in sys.argv
    filers, issuers = {}, {}
    for cik in ciks:
        sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
        f = sub["filings"]["recent"]
        filings = [(f["accessionNumber"][k], f["filingDate"][k], f["reportDate"][k], f["primaryDocument"][k], f["form"][k])
                   for k in range(len(f["form"])) if f["form"][k] in ("13F-HR", "13F-HR/A")]
        # keep the latest filing per period (an amendment supersedes)
        by_period: dict[str, tuple] = {}
        for acc, fd, rd, doc, form in sorted(filings, key=lambda x: x[1]):
            by_period[rd] = (acc, fd, rd, doc, form)
        recs = []
        for rd, (acc, fd, _rd, doc, form) in sorted(by_period.items()):
            raw = cache / f"{acc}.json"
            if raw.exists() and not refresh:
                rows = json.loads(raw.read_text())
            else:
                accn = acc.replace("-", "")
                base = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/"
                idx = get(base).decode("utf-8", "replace")
                xmls = [x for x in re.findall(r'href="([^"]+\.xml)"', idx) if "primary_doc" not in x and "xsl" not in x.lower()]
                if xmls:
                    x = xmls[0]
                    url = "https://www.sec.gov" + x if x.startswith("/") else base + x
                    rows = parse_xml_table(get(url).decode("utf-8", "replace"))
                else:
                    txt = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn}/{acc}.txt").decode("utf-8", "replace")
                    rows = parse_legacy_table(txt)
                raw.write_text(json.dumps(rows))          # raw units as filed
            # per-filing scale by implied price (see the module docstring)
            ratios = []
            for r in rows:
                try:
                    sh = float(str(r.get("shares") or 0).replace(",", ""))
                except ValueError:
                    sh = 0.0
                if sh > 0 and r["value"] > 0:
                    ratios.append(r["value"] / sh)
            ratios.sort()
            median_price = ratios[len(ratios) // 2] if ratios else 0.0
            scale = 1000.0 if (ratios and median_price < 1.0) else 1.0
            rows = [dict(r, value=r["value"] * scale) for r in rows]
            recs.append({"accession": acc, "period": rd, "filed": fd, "form": form, "positions": len(rows),
                         "total_value_usd": round(sum(r["value"] for r in rows)), "scale": scale})
            for r in rows:
                if not r["issuer"]:
                    continue
                # a name made only of suffix words ("INC", a loosely parsed
                # legacy line) normalises to nothing: key it on the raw name
                key = norm(r["issuer"]) or r["issuer"].lower().strip()
                e = issuers.setdefault(key, {"name": r["issuer"], "cusips": [], "classes": [], "periods": [],
                                             "first_period": rd, "last_period": rd, "max_value_usd": 0.0, "last_value_usd": 0.0,
                                             "put_call_only": True})
                if r["cusip"] and r["cusip"] not in e["cusips"]:
                    e["cusips"].append(r["cusip"])
                if r["class"] and r["class"] not in e["classes"]:
                    e["classes"].append(r["class"])
                if rd not in e["periods"]:
                    e["periods"].append(rd)
                e["first_period"] = min(e["first_period"], rd)
                if rd >= e["last_period"]:
                    e["last_period"] = rd
                    e["last_value_usd"] = e.get("_last_acc_value", 0.0) + r["value"] if e.get("_last_period") == rd else r["value"]
                    e["_last_period"] = rd
                    e["_last_acc_value"] = e["last_value_usd"]
                e["max_value_usd"] = max(e["max_value_usd"], r["value"])
                if not r.get("put_call"):
                    e["put_call_only"] = False
            print(f"  {cik} {rd} {form} {len(rows)} positions", file=sys.stderr)
        filers[cik] = {"name": sub.get("name"), "filings": recs}
    for e in issuers.values():
        e.pop("_last_period", None); e.pop("_last_acc_value", None)
        e["periods"].sort()
    write_atomic(out_path, json.dumps({"_readme": __doc__.strip(), "filers": filers,
                                       "issuers": dict(sorted(issuers.items()))}, indent=1))
    print(f"wrote {out_path.relative_to(ROOT)}: {len(issuers)} issuers across "
          f"{sum(len(v['filings']) for v in filers.values())} filings")


if __name__ == "__main__":
    main()
