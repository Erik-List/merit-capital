#!/usr/bin/env python3
"""Fetch the pre-2008 portfolio pages of indexventures.com from the Internet Archive (the Common Crawl
floor is 2008): /portfolio.html and /portf_sect.html 1999-2002, every captured /cgi-local/ivw_port_detail.cgi
listing 2002-2007 (typ=it / typ=ls, by section), the PHP site's first captures of late 2007 and its Life
Sciences listings (industry_id/2) through 2013. One request per second through scripts/ia_fetch (shared
throttle); bodies cached under data/filings/index-ventures/ia-cache. Writes scratch/ia-pass.json
(url, timestamp, status, cache key). A fetch that fails is recorded as failed, never as an empty page."""
import gzip, hashlib, json, re, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import ia, ia_fetch  # noqa: E402
OUT = HERE / "ia-pass.json"
res = json.loads(OUT.read_text()) if OUT.exists() else {}
enum = json.load(gzip.open(HERE.parents[4] / "data" / "filings" / "index-ventures" / "cdx-enum.json.gz", "rt"))["indexventures.com"]["rows"]
targets = []
for o, ts, sc, mt in enum:
    low = o.lower()
    if sc != "200":
        continue
    if re.search(r"/(portfolio|portf_sect|portf_geo)\.html$", low) or "ivw_port_detail" in low or "ivw_port_detail_all" in low \
            or re.search(r"/portfolio/index/industry_id/2(/|$)", low) or re.search(r"indexventures\.com(:80)?/portfolio$", low) \
            or re.search(r"/index\.php/portfolio$", low):
        targets.append((ts, o.replace("&amp;", "&")))
# later captures of the static pages and the life list, by CDX (one query each)
for pat, frm, to in (("indexventures.com/portfolio.html", "1999", "2002"), ("indexventures.com/portf_sect.html", "2001", "2002"),
                     ("indexventures.com/portfolio/index/industry_id/2", "2009", "2013"),
                     ("indexventures.com/portfolio/index/industry_id/2/company_status/exited", "2009", "2013"),
                     ("indexventures.com/portfolio/index/industry_id/2/company_status/current", "2009", "2013")):
    key = f"cdx:{pat}"
    if key not in res:
        try:
            rows = ia.cdx(f"url={pat}&output=json&fl=timestamp,original,statuscode&filter=statuscode:200&collapse=timestamp:4&from={frm}&to={to}")
            res[key] = rows[1:] if rows else []
        except Exception as e:
            res[key] = f"failed {e}"
        OUT.write_text(json.dumps(res, indent=1))
    if isinstance(res[key], list):
        targets += [(r[0], r[1]) for r in res[key]]
print(len(targets), "targets", flush=True)
for ts, url in sorted(set(targets)):
    k = f"{ts} {url}"
    if res.get(k, {}).get("status") == "ok":
        continue
    if ia_fetch.blocked() > 0:
        print("IA cooldown, stopping", flush=True)
        break
    try:
        body = ia.replay(ts, url)
        res[k] = {"status": "ok", "bytes": len(body), "cache": hashlib.sha1(f"{ts} {url}".encode()).hexdigest() + ".html"}
    except Exception as e:
        res[k] = {"status": f"failed {str(e)[:80]}"}
    OUT.write_text(json.dumps(res, indent=1))
    time.sleep(2)      # well under the shared 1/s bucket: two refusals on 2026-10-01 came after ~15 quick replays
print(sum(1 for v in res.values() if isinstance(v, dict) and v.get("status") == "ok"), "ok;",
      sum(1 for v in res.values() if isinstance(v, dict) and str(v.get("status")).startswith("failed")), "failed")
