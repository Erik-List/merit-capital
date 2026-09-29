"""Once IA answers: CDX captures for each era's listing URLs (all years) and
one sample capture per era, for writing the era parsers. Output
scratch/listing-cdx.json; samples land in the IA cache (data/filings)."""
import json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ia
OUT = HERE / "listing-cdx.json"
res = json.loads(OUT.read_text()) if OUT.exists() else {}
URLS = [
 "northzone.com/portfolio", "northzone.com/team", "northzone.com/about", "northzone.com/",
 "northzone.com/web/folder.asp?folderID=189", "northzone.com/web/folder.asp?folderID=190",
 "northzone.com/web/folder.asp?folderID=191", "northzone.com/web/folder.asp?folderID=192",
 "northzone.com/web/folder.asp?folderID=216", "northzone.com/default.asp",
 "northzone.com/portfolio/active-investments/", "northzone.com/portfolio/exits/",
 "northzone.com/portfolio/investments-by-segment/",
 "northzone.com/investments", "northzone.com/investments/", "northzone.com/people",
 "northzone.com/portfolio/", "northzone.com/team/", "northzone.com/pressreleases",
]
for u in URLS:
    if u in res and res[u].get("ok"):
        continue
    for k in range(4):
        try:
            rows = ia.cdx(f"url={u}&output=json&fl=timestamp,original,statuscode,digest,length&limit=3000")
            res[u] = {"ok": True, "rows": rows[1:]}
            break
        except Exception as e:
            res[u] = {"ok": False, "err": str(e)}
            time.sleep(15)
    print(u, len(res[u].get("rows", [])), res[u].get("err", ""), flush=True)
    OUT.write_text(json.dumps(res, indent=0))
try:
    rows = ia.cdx("url=northzone.com/wp-json/wp/v2/posts*&output=json&fl=timestamp,original,statuscode,length&collapse=urlkey&limit=5000")
    lists = [r for r in rows[1:] if "/posts?" in r[1] or r[1].rstrip("/").endswith("/posts")]
    res["wp-posts-lists"] = {"ok": True, "rows": lists, "total": len(rows) - 1}
    print("wp posts urls", len(rows) - 1, "list pages", len(lists), flush=True)
except Exception as e:
    print("wp posts", e)
OUT.write_text(json.dumps(res, indent=0))
