#!/usr/bin/env python3
"""The pre-2008 archive leg (Internet Archive): Common Crawl starts in 2008, so kpcb.com's 1996-2007 portfolio pages
exist only on the Internet Archive. One CDX query per path prefix (200, text/html, 1996-2008, collapsed by digest),
then the first capture per path per year, fetched raw (id_) through scripts/ia_fetch.py, which paces every request
on the machine-wide throttle and honours the firewall cooldown. Writes sources/wayback/ia-manifest.json and the raw
bodies under data/filings/wayback/kleiner-perkins/ (gitignored). A failed fetch is recorded FAILED, never as absent.
Usage: python3 ia-pre2008.py [--cdx-only]"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402
RAW = ROOT / "data" / "filings" / "wayback" / "kleiner-perkins"
MAN = HERE.parent / "sources" / "wayback" / "ia-manifest.json"
CDX = HERE / "ia-cdx-pre2008.json"
PREFIXES = ["kpcb.com/portfolio*", "kpcb.com/companies*", "kpcb.com/ventures*", "kpcb.com/keiretsu*",
            "kpcb.com/team*", "kpcb.com/partners*", "kpcb.com/about*", "kpcb.com/initiatives*", "kpcb.com/index*", "kpcb.com/"]
rows = json.loads(CDX.read_text()) if CDX.exists() else {}
for p in PREFIXES:
    if p in rows:
        continue
    url = ("https://web.archive.org/cdx/search/cdx?url=" + p + "&output=json&from=1996&to=2008"
           "&fl=original,timestamp,digest,statuscode,mimetype&filter=statuscode:200&filter=mimetype:text/html&collapse=digest&limit=20000")
    body, status = ia_fetch.get(url, tries=4)
    if not body:
        print("CDX FAILED", p, status, flush=True)
        continue
    rows[p] = json.loads(body)[1:] if body.strip() else []
    write_atomic(CDX, json.dumps(rows))
    print(p, len(rows[p]), flush=True)
if "--cdx-only" in sys.argv:
    sys.exit(0)
man = json.loads(MAN.read_text()) if MAN.exists() else {}
todo, seen = [], set()
for p, rs in rows.items():
    for orig, ts, dig, *_ in sorted(rs, key=lambda r: r[1]):
        path = re.sub(r"^https?://(www\.)?kpcb\.com(:\d+)?", "", orig, flags=re.I) or "/"
        if re.search(r"\.(gif|jpe?g|png|css|js|pdf|swf)(\?|$)", path, re.I):
            continue
        k = (path.lower().rstrip("/"), ts[:4])
        if k in seen:
            continue
        seen.add(k)
        todo.append((orig, ts, dig, path))
print(len(todo), "captures to fetch", flush=True)
RAW.mkdir(parents=True, exist_ok=True)
for i, (orig, ts, dig, path) in enumerate(todo):
    key = f"{ts}-" + (re.sub(r"[^A-Za-z0-9._-]+", "_", path.strip("/")) or "root")[:150] + ".html"
    if man.get(key, {}).get("status") == "ok":
        continue
    body, status = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}", tries=3)
    if body:
        (RAW / key).write_bytes(body)
        man[key] = {"status": "ok", "url": orig, "path": path, "timestamp": ts, "digest": dig, "bytes": len(body),
                    "capture_url": f"https://web.archive.org/web/{ts}/{orig}"}
    else:
        man[key] = {"status": "FAILED", "url": orig, "path": path, "timestamp": ts, "http": status}
    if i % 25 == 24:
        write_atomic(MAN, json.dumps(man, indent=1) + "\n"); print(i + 1, "done", flush=True)
write_atomic(MAN, json.dumps(man, indent=1) + "\n")
print(sum(1 for v in man.values() if v["status"] == "ok"), "ok;", sum(1 for v in man.values() if v["status"] != "ok"), "failed")
