#!/usr/bin/env python3
"""The pre-2008 archive leg (Internet Archive): Common Crawl starts in 2008, so bvp.com's 1999-2007 portfolio pages
exist only on the Internet Archive. Reads the URL map (scratch/cdx-map-bvp.com.json, one row per urlkey), asks CDX
for the per-year captures of the listing pages, and fetches raw bodies (id_) through scripts/ia_fetch.py, which
paces every request on the machine-wide throttle and honours the firewall cooldown. Writes
sources/wayback/ia-manifest.json and the raw bodies under data/filings/wayback/bessemer-venture-partners/
(gitignored). A failed fetch is recorded FAILED, never as absent.
Pages: /port/onepage.asp (the whole portfolio on one page, 2002-2008), /people/** (the 1999-2001 portfolio by
sector, and /people/anti: the first anti-portfolio), /port/anti.asp, /port/investor.asp?* and /port/results.asp?*
(per-partner and filtered lists), /port/success.asp, /firm/investors.* (the team), /Portfolio/Default.aspx (2007)."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402
RAW = ROOT / "data" / "filings" / "wayback" / "bessemer-venture-partners"
MAN = HERE.parent / "sources" / "wayback" / "ia-manifest.json"
CDX = HERE / "ia-cdx-pre2008.json"
P = lambda o: re.sub(r"^https?://(www\.)?bvp\.com(:\d+)?", "", o, flags=re.I) or "/"
umap = json.loads((HERE / "cdx-map-bvp.com.json").read_text())
YEARLY = ["bvp.com/port/onepage.asp", "bvp.com/port/anti.asp", "bvp.com/people/index.asp", "bvp.com/people/index.html",
          "bvp.com/people/anti/index.asp", "bvp.com/firm/investors.asp", "bvp.com/Portfolio/Default.aspx",
          "bvp.com/port/success.asp", "bvp.com/"]
cdx = json.loads(CDX.read_text()) if CDX.exists() else {}
for u in YEARLY:
    if u in cdx:
        continue
    url = ("https://web.archive.org/cdx/search/cdx?url=" + u + "&output=json&from=1996&to=2008"
           "&fl=original,timestamp,digest&filter=statuscode:200&collapse=timestamp:6&limit=400")
    body, status = ia_fetch.get(url, tries=4)
    if status != "200":
        print("CDX FAILED", u, status, flush=True)
        continue
    cdx[u] = json.loads(body)[1:] if body.strip() else []
    write_atomic(CDX, json.dumps(cdx))
    print(u, len(cdx[u]), flush=True)
todo, seen = [], set()
for u, rs in cdx.items():
    half = {}
    for orig, ts, dig in sorted(rs, key=lambda r: r[1]):
        k = (ts[:4], "a" if ts[4:6] <= "06" else "b") if "onepage" in u else (ts[:4],)
        if k not in half and dig not in {d for _, _, d in half.values()}:
            half[k] = (orig, ts, dig)
    todo += list(half.values())
for orig, ts, end, n, *_ in umap:
    p = P(orig)
    if ts[:4] >= "2008":
        continue
    if "--people-only" in sys.argv and not re.match(r"(?i)^/people/", p):
        continue
    if re.match(r"(?i)^/people/", p) or re.match(r"(?i)^/port/(investor|results|success)\.asp", p) or re.match(r"(?i)^/firm/(investors|who|what|roots)\.", p):
        todo.append((orig, ts, ""))
plan = []
for orig, ts, dig in todo:
    k = (P(orig).lower(), ts)
    if k not in seen:
        seen.add(k)
        plan.append((orig, ts, dig))
print(len(plan), "captures to fetch", flush=True)
if "--plan-only" in sys.argv:
    sys.exit(0)
man = json.loads(MAN.read_text()) if MAN.exists() else {}
RAW.mkdir(parents=True, exist_ok=True)
for i, (orig, ts, dig) in enumerate(plan):
    path = P(orig)
    key = f"{ts}-" + (re.sub(r"[^A-Za-z0-9._-]+", "_", path.strip("/")) or "root")[:150] + ".html"
    if man.get(key, {}).get("status") == "ok":
        continue
    body, status = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}", tries=3)
    if body and status == "200":
        (RAW / key).write_bytes(body)
        man[key] = {"status": "ok", "url": orig, "path": path, "timestamp": ts, "digest": dig, "bytes": len(body),
                    "capture_url": f"https://web.archive.org/web/{ts}/{orig}"}
    else:
        man[key] = {"status": "FAILED", "url": orig, "path": path, "timestamp": ts, "http": status}
    if i % 20 == 19:
        write_atomic(MAN, json.dumps(man, indent=1) + "\n"); print(i + 1, "done", flush=True)
write_atomic(MAN, json.dumps(man, indent=1) + "\n")
print(sum(1 for v in man.values() if v["status"] == "ok"), "ok;", sum(1 for v in man.values() if v["status"] != "ok"), "failed", flush=True)
