"""Ad-hoc CDX query through ia_fetch. Usage: cdx_q.py '<url-pattern>' [k=v ...]"""
import json, sys, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import ia_fetch
params = {"url": sys.argv[1], "output": "json", "fl": "timestamp,original,statuscode,digest,length"}
for kv in sys.argv[2:]:
    k, v = kv.split("=", 1); params[k] = v
body, st = ia_fetch.get("https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(params))
rows = json.loads(body or b"[]") if st.startswith("2") else []
for r in rows[1:]:
    print("\t".join(r))
print(f"# {st} {max(len(rows)-1,0)} rows", file=sys.stderr)
