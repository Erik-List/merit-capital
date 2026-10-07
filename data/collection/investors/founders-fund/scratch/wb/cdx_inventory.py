"""URL inventory of a domain from the CDX index, through the shared IA throttle.
Writes scratch/wb/inventory-<domain>.json: [urlkey, first_ts, last_ts, n, original]."""
import importlib.util, json, sys, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("wp", ROOT / "scripts" / "wayback-pull.py")
wp = importlib.util.module_from_spec(spec); spec.loader.exec_module(wp)
domain = sys.argv[1]
out = Path(__file__).parent / f"inventory-{domain}.json"
rows = []
for y0, y1 in [(1998, 2008), (2009, 2011), (2012, 2013), (2014, 2015), (2016, 2017), (2018, 2019), (2020, 2021), (2022, 2023), (2024, 2026)]:
    r = wp.cdx(f"{domain}/*", **{"from": str(y0), "to": str(y1), "collapse": "urlkey", "fl": "urlkey,timestamp,original,mimetype,statuscode,digest", "filter": "mimetype:text/html", "limit": "20000"})
    print(y0, y1, len(r), flush=True)
    for x in r: rows.append([y0, y1] + x)
out.write_text(json.dumps(rows))
print("wrote", out, len(rows))
