#!/usr/bin/env python3
"""Enumerate the Internet Archive's URL history for Index Ventures's domains
(collapsed by urlkey, first and last capture year per URL) so the listing
eras can be written into config.json. Throttled through scripts/ia_fetch."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import ia_fetch

OUT = Path(__file__).resolve().parents[5] / "data" / "filings" / "index-ventures" / "cdx-enum.json"
DOMAINS = sys.argv[1:] or ["indexventures.com", "indexventures.ch", "index-ventures.com"]
res = json.loads(OUT.read_text()) if OUT.exists() else {}
for d in DOMAINS:
    if d in res and res[d].get("status") == "ok":
        continue
    url = ("https://web.archive.org/cdx/search/cdx?url=" + d + "/*&output=json"
           "&fl=original,timestamp,statuscode,mimetype&collapse=urlkey&limit=60000")
    body, code = ia_fetch.get(url)
    if code != "200":
        res[d] = {"status": f"failed {code}"}
        print(d, "FAILED", code, flush=True)
    else:
        rows = json.loads(body or b"[]")
        res[d] = {"status": "ok", "rows": rows[1:] if rows else []}
        print(d, len(res[d]["rows"]), flush=True)
    OUT.write_text(json.dumps(res, indent=1))
