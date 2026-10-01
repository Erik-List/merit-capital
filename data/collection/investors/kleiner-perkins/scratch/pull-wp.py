#!/usr/bin/env python3
"""Pull kleinerperkins.com's WordPress REST collections (company, person, deck,
posts, and the stage/sector taxonomies) into sources/site/raw/. Read-only GETs,
paginated at 100."""
import json, sys, time, urllib.request
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "sources" / "site" / "raw"
OUT.mkdir(parents=True, exist_ok=True)
BASE = "https://www.kleinerperkins.com/wp-json/wp/v2/"
UA = {"User-Agent": "Mozilla/5.0 (merit-capital research)"}

import subprocess, tempfile
def get(url):
    for attempt in range(4):
        with tempfile.NamedTemporaryFile() as hf:
            r = subprocess.run(["curl", "-sfL", "--max-time", "90", "-D", hf.name, "-H",
                                "User-Agent: " + UA["User-Agent"], url], capture_output=True)
            if r.returncode == 0:
                hdr = {}
                for line in open(hf.name, errors="replace"):
                    if ":" in line:
                        k, v = line.split(":", 1); hdr[k.strip()] = v.strip()
                return json.loads(r.stdout), hdr
        print("retry", url, r.returncode, file=sys.stderr); time.sleep(3 * (attempt + 1))
    raise SystemExit(f"failed {url}")

def pull(rest_base, extra=""):
    rows, page = [], 1
    while True:
        d, h = get(f"{BASE}{rest_base}?per_page=100&page={page}{extra}")
        rows += d
        total_pages = int(h.get("X-WP-TotalPages") or h.get("x-wp-totalpages") or h.get("X-Wp-Totalpages") or 1)
        if page >= total_pages: break
        page += 1; time.sleep(0.5)
    for r in rows:
        r.pop("yoast_head", None); r.pop("yoast_head_json", None); r.pop("_links", None)
    (OUT / f"{rest_base.replace('/', '_')}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(rest_base, len(rows))

for rb in sys.argv[1:] or ["company", "person", "deck", "stage", "sector", "posts", "categories", "tags"]:
    pull(rb)
