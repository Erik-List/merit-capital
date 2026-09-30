#!/usr/bin/env python3
"""List the Internet Archive's captures of nea.com before 2013 (the years Common
Crawl does not reach), one row per distinct URL, through scripts/ia_fetch.py (the
machine-wide throttle and firewall cooldown). Writes scratch/ia-cdx.json
{url: [timestamps...]} for HTML pages, so the listing eras can be chosen from
what the archive actually holds.
Usage: python3 ia-cdx.py [from_year] [to_year]
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402

OUT = HERE / "ia-cdx.json"


def main():
    fy, ty = (sys.argv[1:3] + ["1996", "2013"])[:2] if len(sys.argv) > 1 else ("1996", "2013")
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for y in range(int(fy), int(ty) + 1):
        key = str(y)
        if data.get("_years", {}).get(key) == "ok":
            continue
        url = ("https://web.archive.org/cdx/search/cdx?url=nea.com/*&matchType=prefix"
               f"&from={y}&to={y}&filter=statuscode:200&filter=mimetype:text/html"
               "&fl=original,timestamp,digest&collapse=digest&limit=20000")
        body, code = ia_fetch.get(url, tries=3)
        if code != "200":
            print(y, "FAILED", code, flush=True)
            data.setdefault("_years", {})[key] = f"failed {code}"
            write_atomic(OUT, json.dumps(data, indent=1) + "\n")
            if ia_fetch.blocked():
                print("IA firewall cooldown set; stopping", flush=True)
                return
            continue
        n = 0
        for line in body.decode("utf-8", "replace").splitlines():
            parts = line.split(" ")
            if len(parts) < 3:
                continue
            u, ts, dg = parts[0], parts[1], parts[2]
            data.setdefault("urls", {}).setdefault(u, []).append([ts, dg])
            n += 1
        data.setdefault("_years", {})[key] = "ok"
        print(y, n, "captures", flush=True)
        write_atomic(OUT, json.dumps(data, indent=1) + "\n")


if __name__ == "__main__":
    main()
