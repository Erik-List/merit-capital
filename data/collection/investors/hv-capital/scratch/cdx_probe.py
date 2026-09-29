"""CDX probe for HV's domains: per-domain URL inventory, collapsed by urlkey.
Writes scratch/cdx/<domain>.json. Uses ia_fetch (machine-wide IA throttle)."""
import json, sys, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import ia_fetch
out = Path(__file__).resolve().parent / "cdx"
for dom in sys.argv[1:]:
    q = urllib.parse.urlencode({"url": dom + "/*", "output": "json", "fl": "timestamp,original,statuscode,mimetype,digest",
                                "collapse": "urlkey", "limit": "20000"})
    body, st = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?{q}")
    try:
        rows = json.loads(body or b"[]")
    except Exception:
        rows = []
    (out / f"{dom}.json").write_text(json.dumps(rows))
    print(dom, st, len(rows))
