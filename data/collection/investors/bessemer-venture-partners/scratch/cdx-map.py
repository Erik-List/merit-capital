"""Enumerate every archived bvp.com URL (CDX, one row per urlkey with first/last capture and count) into
scratch/cdx-map.json, so the listing eras can be read off the path structure. Paced through ia_fetch (the shared
1/s IA budget). Usage: python3 cdx-map.py [domain]"""
import json, sys, time
from pathlib import Path
from urllib.parse import quote
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch
dom = sys.argv[1] if len(sys.argv) > 1 else "bvp.com"
out = Path(__file__).resolve().parent / f"cdx-map-{dom}.json"
rows, resume, page = [], None, 0
while True:
    url = (f"https://web.archive.org/cdx/search/cdx?url={dom}/*&output=json&collapse=urlkey"
           f"&fl=original,timestamp,endtimestamp,groupcount,statuscode,mimetype&showResumeKey=true&limit=15000"
           f"&filter=statuscode:200&filter=mimetype:text/html")
    if resume:
        url += "&resumeKey=" + quote(resume, safe="")
    body, code = ia_fetch.get(url, tries=4)
    if code != "200":
        print("FAILED", code, "page", page, flush=True)
        time.sleep(30)
        page += 1
        if page > 60: break
        continue
    batch = json.loads(body or b"[]")
    if batch and batch[0] and batch[0][0] == "original":
        batch = batch[1:]
    resume = None
    while batch and not batch[-1]:
        batch.pop()
    if batch and len(batch[-1]) == 1:
        resume = batch.pop()[0]
        while batch and not batch[-1]:
            batch.pop()
    rows.extend(batch)
    page += 1
    print(f"page {page}: +{len(batch)} ({len(rows)} total) resume={bool(resume)}", flush=True)
    out.write_text(json.dumps(rows))
    if not resume:
        break
print("done", len(rows))
