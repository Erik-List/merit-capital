"""Recall check (PRO-76): earlier versions of 20vc.fund's Framer CMS collection
in the Internet Archive. Two CDX queries through scripts/ia_fetch.py (shared
throttle and machine-wide cooldown): every capture under the project's /cms/
prefix and under its /modules/ prefix. Captured .framercms chunks are fetched
(id_ replay) into data/filings/site-raw/20vc/ and decoded with framercms.py;
names not in companies/base.json are printed. A failed lookup prints as failed.
Usage: python3 ia-framer.py"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts")); sys.path.insert(0, str(HERE))
import ia_fetch, framercms  # noqa: E402
RAW = ROOT / "data" / "filings" / "site-raw" / "20vc" / "ia"
RAW.mkdir(parents=True, exist_ok=True)
PROJECT = "framerusercontent.com/{kind}/bERmDTXK8P7cbh9Ly71G/"
if ia_fetch.blocked():
    sys.exit(f"IA cooldown: {ia_fetch.blocked():.0f}s left; not querying")
caps = []
for kind in ("cms", "modules"):
    url = ("https://web.archive.org/cdx/search/cdx?url=" + PROJECT.format(kind=kind)
           + "&matchType=prefix&output=json&fl=timestamp,original,statuscode,mimetype&filter=statuscode:200&limit=500")
    body, code = ia_fetch.get(url)
    print(kind, "CDX", code, len(body))
    if code != "200":
        print("  FAILED (not an absence)"); continue
    rows = json.loads(body or b"[]")[1:]
    print(" ", len(rows), "captures")
    for ts, orig, sc, mt in rows:
        if "YJbM8mTif" in orig:
            print("  ", ts, orig)
            caps.append((ts, orig))
base = {r["name"].lower() for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
for ts, orig in caps:
    if not orig.endswith(".framercms"):
        continue
    body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}", compressed=False)
    print("chunk", ts, code, len(body))
    if code != "200":
        continue
    p = RAW / f"{ts}-YJbM8mTif.framercms"; p.write_bytes(body)
    try:
        items, _ = framercms.decode(body)
    except Exception as e:  # a different schema version
        print("  decode failed:", e); continue
    names = sorted({it.get("TKx4vX3c1") for it in items if isinstance(it.get("TKx4vX3c1"), str)})
    print("  ", len(names), "names;", "not in base:", [n for n in names if n.lower() not in base])
