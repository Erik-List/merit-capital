#!/usr/bin/env python3
"""Parse the Common Crawl captures of tcv.com (scratch/cc-fetch.py) into the
archive layer (PRO-169).

Listing pages go through the same per-generation parsers as the Internet
Archive pull (scratch/pull-archive-tcv.py), by path and year:
  /portfolio/index.php4  2006-2013  idx2007  (the 2008-2012 ARC crawls and CC-MAIN-2013-20)
  /portfolio/      2013-2016  wp2013
  /all-companies   2017-2026  list2017
  /companies/      2017-2023  grid2017   (the deal type per card)
  /partnerships    2024-2026  part2024
Rows merge into sources/wayback/parsed/<year>.json under surface "cc:<gen>",
keyed (surface, slug), keeping the earliest capture; capture_url is the
index.commoncrawl.org form (COLLECTION.md 1: a CC capture is a valid citation).

Team pages (/team/<slug>, /teams/<slug>) are merged into
sources/wayback/partner-roster.json with their capture years (source
'cc-profile-page'); news posts are written to sources/site/news/ as text for
scratch/news-layer.py to pick up.
"""
import importlib.util
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
RAW = INV / "scratch/cc-raw"
PARSED = INV / "sources/wayback/parsed"
spec = importlib.util.spec_from_file_location("pa", INV / "scratch/pull-archive-tcv.py")
pa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pa)
live = INV / "sources/site/all-companies-2026.json"
if live.exists():
    pa.KNOWN_WHOLE.update(r["legal_name"] for r in json.load(open(live))["rows"])

GEN = [
    (r"/portfolio/index\.php4$", 2006, 2013, "idx2007", pa.p_idx2007),
    (r"/portfolio/all-portfolio\.php4$", 2010, 2013, "all2012", pa.p_all2012),
    (r"/portfolio/?$", 2013, 2016, "wp2013", pa.p_wp2013),
    (r"/all-companies/?$", 2017, 2026, "list2017", pa.p_list2017),
    (r"/companies/?$", 2017, 2023, "grid2017", pa.p_grid2017),
    (r"/partnerships/?$", 2024, 2026, "part2024", pa.p_part2024),
]


def main():
    per_year = {}
    for f in PARSED.glob("*.json"):
        per_year[int(f.stem)] = {(r["surface"], r["slug"]): r for r in json.load(open(f))}
    team = {}
    news = 0
    counts = {}
    for meta_f in sorted(RAW.glob("*/*.json")):
        m = json.load(open(meta_f))
        url, ts, crawl = m["url"], m["timestamp"], m["crawl"]
        path = re.sub(r"^https?://(www\.)?tcv\.com(:\d+)?", "", url).split("?")[0]
        y = int(ts[:4])
        html_f = meta_f.with_suffix(".html")
        if not html_f.exists():
            continue
        h = html_f.read_text(encoding="utf-8", errors="replace")
        cap = f"https://index.commoncrawl.org/{crawl}-index?url={url}&output=json"
        tm = re.match(r"^/teams?/([a-z0-9]+(?:-[a-z0-9]+)+)/?$", path)
        if tm:
            team.setdefault(tm.group(1), set()).add(y)
            continue
        hit = None
        for pat, y0, y1, gen, parser in GEN:
            if re.search(pat, path) and y0 <= y <= y1:
                hit = (gen, parser)
                break
        if hit is None:
            if re.match(r"^/(news/)?[a-z0-9-]{25,}/?$", path):
                slug = path.strip("/").split("/")[-1]
                dest = INV / "sources/site/news" / (slug[:150] + ".txt")
                if not dest.exists():
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    t = re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>", " ", h)
                    t = re.sub(r"<[^>]+>", " ", t)
                    dest.write_text(re.sub(r"\s+", " ", t).strip())
                    news += 1
            continue
        gen, parser = hit
        rows = parser(h)
        counts[(gen, ts)] = len(rows)
        bucket = per_year.setdefault(y, {})
        for r in rows:
            nm = r.get("name") or ""
            slug = pa.slug_of(nm) or r.get("page_slug") or ""
            if not slug:
                continue
            key = ("cc:" + gen, slug)
            if key in bucket and bucket[key]["snapshot_ts"] <= ts:
                continue
            bucket[key] = {"slug": slug, "name": nm, "path": path or "/", "snapshot_ts": ts, "capture_url": cap,
                           "surface": "cc:" + gen, **{k: v for k, v in r.items() if k != "name"}}
    PARSED.mkdir(parents=True, exist_ok=True)
    for y, bucket in sorted(per_year.items()):
        (PARSED / f"{y}.json").write_text(json.dumps(sorted(bucket.values(), key=lambda r: (r["surface"], r["slug"])),
                                                      indent=1, ensure_ascii=False))
    # roster
    rp = INV / "sources/wayback/partner-roster.json"
    roster = {r["slug"]: r for r in (json.load(open(rp)) if rp.exists() else [])}
    for slug, ys in team.items():
        e = roster.setdefault(slug, {"slug": slug, "name": " ".join(w.capitalize() for w in slug.split("-")),
                                     "years_seen": [], "snapshots": 0, "sources": []})
        e["years_seen"] = sorted(set(e["years_seen"]) | ys)
        e["first_seen"], e["last_seen"] = e["years_seen"][0], e["years_seen"][-1]
        e["snapshots"] = e.get("snapshots", 0) + len(ys)
        if "cc-profile-page" not in e["sources"]:
            e["sources"] = sorted(e["sources"] + ["cc-profile-page"])
    rp.parent.mkdir(parents=True, exist_ok=True)
    rp.write_text(json.dumps(sorted(roster.values(), key=lambda r: r["slug"]), indent=1) + "\n")
    for (gen, ts), n in sorted(counts.items(), key=lambda x: x[0][1]):
        print(gen, ts, n)
    print("team pages:", len(team), "| news bodies written:", news)
    print({y: len(b) for y, b in sorted(per_year.items())})


if __name__ == "__main__":
    main()
