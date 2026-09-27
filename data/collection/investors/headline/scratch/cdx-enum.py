"""Enumerate archived URLs per domain (CDX, collapsed by urlkey) through the
shared IA throttle; writes scratch/cdx/<domain>.json. Used at kickoff to pick
the Wayback eras for config.json."""
import json, sys, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import ia_fetch
out = Path(__file__).parent / "cdx"; out.mkdir(exist_ok=True)
for dom in sys.argv[1:]:
    q = urllib.parse.urlencode({"url": f"{dom}/*", "output": "json", "fl": "original,timestamp,statuscode,mimetype,digest",
                                "collapse": "urlkey", "filter": "statuscode:200", "limit": "20000"})
    body, st = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?{q}")
    try:
        rows = json.loads(body or b"[]")
    except Exception as e:
        print(dom, "parse error", st, body[:200]); continue
    (out / f"{dom}.json").write_text(json.dumps(rows))
    print(dom, st, len(rows))
