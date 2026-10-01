#!/usr/bin/env python3
"""Map the archived URL space of the firm's domains (kpcb.com, kleinerperkins.com,
kpcb.com.cn left out): one CDX query per domain collapsed by urlkey, 200-only,
HTML only. Writes scratch/cdx-map-<domain>.json [[original, first ts, last ts, count]]."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import ia_fetch
OUT = Path(__file__).resolve().parent
for dom in sys.argv[1:]:
    url = ("https://web.archive.org/cdx/search/cdx?url=" + dom + "/*&output=json&fl=original,timestamp,statuscode,mimetype"
           "&filter=statuscode:200&filter=mimetype:text/html&collapse=urlkey&limit=200000")
    body, status = ia_fetch.get(url, tries=4)
    rows = json.loads(body or b"[]")[1:] if body else []
    (OUT / f"cdx-map-{dom}.json").write_text(json.dumps(rows))
    print(dom, status, len(rows), flush=True)
