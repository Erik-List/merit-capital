#!/usr/bin/env python3
"""Read NEA's archived people pages (nea.com/team/<slug>, 2013 on) from the
Common Crawl captures cc-fetch.py stored (one per slug per year), into
scratch/roster-cc.json:

  {slug: {"names": [...], "titles": {year: "General Partner, Menlo Park"}, "years": [...]}}

The page states the person's name in <h1> and title (with the office after a
comma) in the first <h2> of the partner header. A year with no fetched capture
still counts as a year the page existed (from the index), with no title.
"""
import collections
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
IDX = HERE / "cc-index-raw.json"
RAW = ROOT / "data" / "filings" / "commoncrawl" / "new-enterprise-associates"
PAGE = re.compile(r"^https?://(?:www\.)?nea\.com(?::\d+)?/team/([a-z][a-z0-9-]*[a-z0-9])/?$")


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def main():
    out = collections.defaultdict(lambda: {"names": [], "titles": {}, "years": set()})
    idx = json.loads(IDX.read_text())
    for cid, slots in idx.items():
        for _k, v in slots.items():
            for r in v.get("records", []):
                m = PAGE.match(r["url"])
                if m and r.get("status") == "200":
                    out[m.group(1)]["years"].add(r["timestamp"][:4])
    man = json.loads(MAN.read_text())
    for k, v in sorted(man.items(), key=lambda kv: kv[1].get("timestamp", "")):
        m = PAGE.match(v.get("url", ""))
        if not m or v.get("status") != "ok":
            continue
        s = m.group(1)
        body = (RAW / k).read_text(encoding="utf-8", errors="replace")
        hdr = body[body.find("partner-header"):][:3000] if "partner-header" in body else body
        h1 = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", hdr)
        h2 = re.search(r"<h2[^>]*>([\s\S]*?)</h2>", hdr)
        name = clean(h1.group(1)) if h1 else ""
        if not name or name.upper() == "NEA":
            t = re.search(r"<title>([\s\S]*?)</title>", body, re.I)
            name = clean(t.group(1)).split("|")[0].strip() if t else ""
        y = v["timestamp"][:4]
        if name and name not in out[s]["names"] and name.upper() != "NEA":
            out[s]["names"].append(name)
        if h2:
            out[s]["titles"].setdefault(y, clean(h2.group(1)))
    res = {s: {"names": p["names"], "titles": dict(sorted(p["titles"].items())), "years": sorted(p["years"])}
           for s, p in sorted(out.items())}
    write_atomic(HERE / "roster-cc.json", json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    print(len(res), "people slugs;", sum(1 for p in res.values() if p["titles"]), "with a title")


if __name__ == "__main__":
    main()
