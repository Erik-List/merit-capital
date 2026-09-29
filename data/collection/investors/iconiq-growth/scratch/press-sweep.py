#!/usr/bin/env python3
"""Recall probe, press side: sweep deal headlines naming ICONIQ as an investor and list the
companies the base does not hold. Google News RSS year by year (graduation-surfaces.py's
googlenews(), paced machine-wide, no WebSearch budget) and the TechCrunch WordPress search,
paged. Writes scratch/press-sweep.json {items: [...], unmatched: [...]}; prints the unmatched
headlines for the judge. A headline is a lead, never membership: the growth desk's own list
and filings decide (decisions.md D2, D3).
Usage: python3 .../scratch/press-sweep.py
"""
import html, importlib.util, json, re, sys, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts/graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gs)
DEST = HERE / "press-sweep.json"
QUERIES = ['"led by ICONIQ"', '"led by Iconiq Capital"', '"ICONIQ Growth" raises', '"Iconiq Capital" raises', '"co-led by ICONIQ"']
VERB = re.compile(r"^(.{2,60}?)\s+(?:raises|secures|lands|closes|nabs|gets|bags|announces|scores|hauls|rakes|snags|pulls in|collects|valued|hits|reaches|becomes|receives)\b", re.I)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", re.sub(r"\b(inc|corp|ltd|llc|labs|technologies|the)\b", "", s.lower()))


def main():
    base = json.load(open(HERE.parent / "companies/base.json"))
    rows = base if isinstance(base, list) else list(base.values())
    names = {norm(r["name"]) for r in rows} | {norm(r["slug"].replace("-", " ")) for r in rows}
    items = []
    for year in range(2013, 2027):
        for q in QUERIES:
            query = f"{q} after:{year}-01-01 before:{year}-12-31"
            res = gs.googlenews(query, "ICONIQ")
            if res.get("status") != "ok":
                print(f"  {query}: FAILED {res.get('http')}", flush=True)
                continue
            for it in res["items"]:
                it["query"] = query
                items.append(it)
        print(f"  {year}: {len(items)} items so far", flush=True)
    # TechCrunch search, paged
    for page in range(1, 11):
        gs.wait("techcrunch", gs.RATES["techcrunch"])
        url = f"https://techcrunch.com/wp-json/wp/v2/posts?search=iconiq&per_page=100&page={page}&_fields=date,link,title"
        code, body = gs.curl(url)
        if code != 200:
            print(f"  techcrunch page {page}: http {code}", flush=True)
            break
        try:
            posts = json.loads(body)
        except ValueError:
            break
        if not posts:
            break
        for p in posts:
            items.append({"date": (p.get("date") or "")[:10], "title": html.unescape(re.sub(r"<[^>]+>", "", p["title"]["rendered"])),
                          "source": "TechCrunch", "link": p.get("link"), "query": "techcrunch:iconiq"})
        print(f"  techcrunch page {page}: {len(posts)}", flush=True)
    seen, unmatched = set(), []
    for it in items:
        t = it["title"]
        m = VERB.match(t)
        subj = m.group(1) if m else ""
        subj = re.split(r",| - | – ", subj)[-1].strip() if subj else ""
        key = norm(subj)
        it["subject"] = subj
        if not key or key in seen:
            continue
        seen.add(key)
        if not any(key == n or (len(n) > 4 and (n in key or key in n)) for n in names):
            unmatched.append({"subject": subj, "date": it.get("date"), "title": t, "source": it.get("source"),
                              "gid": it.get("gid"), "link": it.get("link")})
    DEST.write_text(json.dumps({"items": items, "unmatched": unmatched}, indent=1, ensure_ascii=False))
    print(f"{len(items)} items, {len(seen)} subjects, {len(unmatched)} not in the base")
    for u in sorted(unmatched, key=lambda x: x["date"] or ""):
        print(f"  {u['date']} {u['subject'][:30]:30s} | {u['title'][:120]}")


if __name__ == "__main__":
    main()
