"""Restore cc-manifest.json entries for bodies already on disk (two cc-fetch.py processes ran at once on
2026-10-01 and the later writer dropped the other's entries; the bodies were never lost). Reads cc-index-raw.json,
recomputes each record's file key exactly as cc-fetch.py does, and adds an 'ok' entry where the file exists."""
import importlib.util, json
from pathlib import Path
from urllib.parse import quote
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ccf", HERE / "cc-fetch.py"); ccf = importlib.util.module_from_spec(spec); spec.loader.exec_module(ccf)
man = json.loads(ccf.MAN.read_text()) if ccf.MAN.exists() else {}
idx = json.loads(ccf.IDX.read_text())
n = 0
for cid, slots in idx.items():
    for v in slots.values():
        for r in v.get("records", []):
            key = ccf.key_of(cid, r)
            f = ccf.RAW / key
            if f.exists() and man.get(key, {}).get("status") != "ok":
                man[key] = {"status": "ok", "url": r["url"], "domain": "bvp", "path": ccf.path_of(r["url"]), "timestamp": r["timestamp"],
                            "crawl": cid, "bytes": f.stat().st_size, "digest": r.get("digest"),
                            "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json"}
                n += 1
ccf.write_atomic(ccf.MAN, json.dumps(man, indent=1) + "\n")
print("restored", n, "| total", len(man), "| failed", [k for k, v in man.items() if v["status"] != "ok"])
