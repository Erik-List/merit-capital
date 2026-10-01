#!/usr/bin/env python3
"""One evidence view per queued row, for the judge (the Cherry / Atomico /
Balderton pattern), joined by slug and name from every layer this run built:

  site      the live list (website, the firm's investment year, description,
            sectors) and the curated cohorts (post, date, entry kind, location)
  archive   the parsed Common Crawl / Wayback years, the 2018-2024 exit flag,
            the /acquirer/ label, the logo upload month
  posts     Views posts whose title names the company (and body mentions)
  web       the company's own website as read today
  register  Companies House same-name candidates with status and dates
  press     Google News headlines naming the company (scratch/news-pack.json)
  queue     what prepare pre-filled and what it still asks

Usage: python3 evidence-pack.py [batch-NNN ...]   (prints a compact digest)
       python3 evidence-pack.py --slugs a,b,c
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent


def load(p, default):
    p = INV / p
    return json.loads(p.read_text()) if p.exists() else default


def norm(s: str) -> str:
    s = (s or "").lower().replace("&", "and")
    s = re.sub(r"\b(inc|ltd|limited|gmbh|ab|oy|sa|sas|bv|plc|llc|corp|labs|hq|app|io|ai|the)\b\.?", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def build():
    site = {}
    for r in load("sources/site/companies.json", []):
        site[norm(r["name"])] = r
    cohorts = defaultdict(list)
    for r in load("sources/site/views-cohorts.json", {"rows": []})["rows"]:
        cohorts[norm(r["name"])].append(r)
    arch = defaultdict(list)
    for f in sorted((INV / "sources" / "wayback" / "parsed").glob("*.json")):
        for r in json.loads(f.read_text()):
            arch[r["slug"]].append((f.stem, r))
            if r.get("name"):
                arch[norm(r["name"])].append((f.stem, r))
    posts = load("sources/site/views-posts.json", {"rows": []})["rows"]
    web = load("sources/web/website-check.json", {})
    ch = load("sources/registers/companies-house/status.json", {})
    news = load("scratch/news-pack.json", {})
    return site, cohorts, arch, posts, web, ch, news


def digest(item, ctx) -> str:
    site, cohorts, arch, posts, web, ch, news = ctx
    s, name = item["slug"], item["name"]
    k = norm(name)
    out = [f"## {s} | {name} | need={','.join(item.get('need', []))} | known={json.dumps(item.get('known', {}))}"]
    r = site.get(k)
    if r:
        out.append(f"  site: yr={r.get('invest_year')} web={r.get('website')} lists={r.get('lists')} sect={r.get('sectors')} :: {(r.get('description') or '')[:110]}")
    for c in cohorts.get(k, []):
        out.append(f"  cohort: {c['post_date']} {c['entry_kind']} loc={c.get('location')} :: {c['cohort'][:60]} {c['url']}")
    a = arch.get(s, []) or arch.get(k, [])
    if a:
        yrs = sorted({y for y, _ in a})
        extra = [f"{y}:{x.get('surface')}" + (f" EXIT" if x.get("exit") else "") + (f" acq={x.get('acquirer')}" if x.get("acquirer") else "")
                 + (f" logo={x.get('logo_upload')}" if x.get("logo_upload") else "") for y, x in a
                 if x.get("exit") or x.get("acquirer") or x.get("surface") in ("winners",)]
        desc = next((x.get("description") for _, x in a if x.get("description")), "")
        out.append(f"  archive: {yrs[0]}-{yrs[-1]} ({len(yrs)}y) {' '.join(sorted(set(extra))[:4])} :: {desc[:90]}")
    if len(k) >= 4:
        rx = re.compile(r"(?i)\b" + re.escape(name.split(" (")[0]) + r"\b")
        hits = [p for p in posts if rx.search(p["title"])]
        for p in hits[:5]:
            out.append(f"  post: {p['date'][:10]} {p['title'][:100]} | {p['link']}")
            t = (p.get("text") or "").split("Keep up to date")[0]
            m = re.search(r"(?i)[^.]{0,160}\b(pre-seed|seed|series [a-e]|round|invest(ed|ment|ing)|led by|co-led|participat)\b[^.]{0,200}", t[len(p['title']) + 20:])
            if m:
                out.append(f"      > {' '.join(m.group(0).split())[:330]}")
        nbody = sum(1 for p in posts if rx.search(p.get("text") or "") and p not in hits)
        if nbody:
            out.append(f"  post-body mentions: {nbody}")
    w = web.get(s)
    if w:
        if w.get("status") == "ok":
            fin = re.sub(r"^https?://(www\.)?", "", w.get("final") or "")[:60]
            out.append(f"  web: {w.get('http')} -> {fin} (c){w.get('copyright')} parked={w.get('parked')} :: {(w.get('title') or '')[:70]}")
        else:
            out.append(f"  web: FAILED {w.get('url')}")
    c = ch.get(s)
    if c and c.get("candidates"):
        for x in c["candidates"][:3]:
            out.append(f"  CH: {x['number']} {x['name'][:40]} inc={x.get('incorporated')} diss={x.get('dissolved')} :: {x['meta'][-40:]} | {(x.get('address') or '')[:45]}")
    n = news.get(s)
    if n:
        seen = set()
        for q in ("q2", "q1"):
            for i in (n.get(q, {}).get("items") or [])[::-1]:
                t = i["title"]
                if t in seen:
                    continue
                if i.get("rounds") or i.get("amounts") or re.search(r"(?i)acqui|shut|closes|collapse|administration|insolv|ipo|valuation|seedcamp", t):
                    seen.add(t)
                    out.append(f"  news: {i['date']} {(i.get('source') or '')[:18]} :: {t[:120]}" + (f" <{i['url']}>" if i.get('url') else ""))
                if len(seen) >= 6:
                    break
        if not seen:
            out.append(f"  news: q1={n.get('q1',{}).get('status')}/{n.get('q1',{}).get('naming')} q2={n.get('q2',{}).get('status')}/{n.get('q2',{}).get('naming')} (no round/exit headline)")
    if item.get("formd_graduation"):
        out.append(f"  formd_grad: {json.dumps(item['formd_graduation'])[:200]}")
    for f in ("rounds", "hq_country_claim", "former_unicorn", "acquirer", "issuer_city", "year_inc"):
        if item.get(f):
            out.append(f"  {f}: {json.dumps(item[f])[:200]}")
    return "\n".join(out)


def main():
    args = sys.argv[1:]
    ctx = build()
    q = {x["slug"]: x for x in json.loads((HERE / "queue" / "queue.json").read_text())}
    if args and args[0] == "--slugs":
        items = [q[s] for s in args[1].split(",") if s in q]
    else:
        items = []
        for b in args:
            items += json.loads((HERE / "queue" / f"{b}.json").read_text())
            items = [q.get(i["slug"], i) if isinstance(i, dict) else q[i] for i in items]
    for it in items:
        print(digest(it, ctx))


if __name__ == "__main__":
    main()
