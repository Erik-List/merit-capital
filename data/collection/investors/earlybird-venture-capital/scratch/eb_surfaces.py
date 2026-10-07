#!/usr/bin/env python3
"""Publisher surfaces for the absence test (COLLECTION.md s6), for the Seed rows
whose research found no later round.

scripts/graduation-surfaces.py leans on Google News, which answered 503 for this
machine on 2026-10-06, and it exits 3 while any lookup fails. This runs the
surfaces that did answer, each a place that would have reported a later round:

  techcrunch         techcrunch.com's own post search (WordPress REST)
  crunchbase_news    news.crunchbase.com's own post search (press, not the vendor database)
  deutsche_startups  deutsche-startups.de's own post search (its DealMonitor names every German round)
  bingnews           Bing News, '"<name>" funding OR "Series A" OR raises OR Finanzierungsrunde'

A failed lookup is stored as an error and retried on the next run, never as an
empty answer.  python3 eb_surfaces.py slug [slug ...] | --open
Output: scratch/eb-surfaces.json {slug: {surface: {status, query, n, named, later: [...]}}}
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

H = Path(__file__).resolve().parent
ROOT = H.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(H))
from shared_throttle import wait  # noqa: E402
import news as N  # noqa: E402

OUT = H / "eb-surfaces.json"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
ROUND = re.compile(r"(?i)series [a-f]\b|serie [a-f]\b|\braises?\b|\braised\b|funding|financing|finanzierung|"
                   r"sammelt|erhält|million|mio\b|investment|levée|runde\b|round\b")
WP = {"techcrunch": "https://techcrunch.com", "crunchbase_news": "https://news.crunchbase.com",
      "deutsche_startups": "https://www.deutsche-startups.de"}


def wp(service: str, name: str) -> dict:
    wait(service if service in ("techcrunch", "crunchbase_news") else "bingnews", 1.0)
    url = f"{WP[service]}/wp-json/wp/v2/posts?search={urllib.parse.quote(name)}&per_page=30&_fields=date,link,title,excerpt"
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-A", UA, "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    if code.strip() != "200":
        return {"status": "error", "http": code.strip(), "query": name}
    try:
        posts = json.loads(body)
    except ValueError:
        return {"status": "error", "http": "not json", "query": name}
    items = []
    for p in posts if isinstance(posts, list) else []:
        title = html.unescape(re.sub(r"<[^>]+>", "", (p.get("title") or {}).get("rendered", "")))
        ex = html.unescape(re.sub(r"<[^>]+>", "", (p.get("excerpt") or {}).get("rendered", "")))
        items.append({"date": (p.get("date") or "")[:10], "title": title, "url": p.get("link"), "desc": ex[:300]})
    return {"status": "ok", "query": name, "items": items}


def run(slug: str, name: str, entry: str, country: str | None) -> dict:
    pat = re.compile(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", re.I)
    out = {}
    services = ["techcrunch", "crunchbase_news"] + (["deutsche_startups"] if country in ("DE", "AT", "CH") else [])
    for svc in services:
        res = wp(svc, name)
        if res["status"] == "ok":
            named = [i for i in res["items"] if pat.search(i["title"] + " " + i["desc"])]
            later = [i for i in named if i["date"] > entry and ROUND.search(i["title"] + " " + i["desc"])]
            res = {"status": "ok", "query": name, "n": len(res["items"]), "named": len(named),
                   "later": [{k: i[k] for k in ("date", "title", "url")} for i in later][:8]}
        out[svc] = res
    q = f'"{name}" funding OR "Series A" OR raises OR Finanzierungsrunde'
    res = N.bing(q)
    if res["status"] == "ok":
        named = [i for i in res["items"] if pat.search(i["title"] + " " + i["desc"])]
        later = [i for i in named if (i["date"] or "") > entry and ROUND.search(i["title"] + " " + i["desc"])]
        res = {"status": "ok", "query": q, "n": len(res["items"]), "named": len(named),
               "later": [{k: i[k] for k in ("date", "title", "url")} for i in later][:8]}
    else:
        res = {"status": "error", "http": res.get("http"), "query": q}
    out["bingnews"] = res
    return out


def lines(slug: str, firm_line: str, finding: str = "none names a later round") -> list[str]:
    """The absence test's surface lines for a row, in the recorded form."""
    d = json.loads(OUT.read_text()).get(slug) or {}
    out = [firm_line]
    for svc, v in d.items():
        if v.get("status") != "ok":
            raise RuntimeError(f"{slug}: surface {svc} not ok; re-run eb_surfaces.py before a no")
        if v.get("later"):
            raise RuntimeError(f"{slug}: surface {svc} shows later-round headlines; read them first: {v['later'][:2]}")
        out.append(f"{svc}: {v['query']} -> {v['n']} results, {v['named']} naming the company; {finding}")
    return out


def main() -> None:
    done = json.loads(OUT.read_text()) if OUT.exists() else {}
    cls = json.loads((H.parent / "companies/classification.json").read_text())
    base = {r["slug"]: r for r in json.loads((H.parent / "companies/base.json").read_text())}
    args = sys.argv[1:]
    if args == ["--open"]:
        slugs = [s for s, c in cls.items() if c.get("entry_stage") == "Seed" and s in base
                 and c.get("seed_to_a_graduation") not in ("graduated", "not_graduated", "censored")]
    else:
        slugs = args
    for s in slugs:
        if s in done and all(v.get("status") == "ok" for v in done[s].values()):
            continue
        c = cls.get(s) or {}
        name = (c.get("search_name") or base[s]["name"])
        name = re.sub(r"\s*\(.*\)$|,? (GmbH|AG|Inc\.?|Ltd\.?|S\.A\.S\.?|SA|AB)$", "", name).strip()
        done[s] = run(s, name, str(c.get("entry_date") or "0000"), c.get("hq_country"))
        OUT.write_text(json.dumps(done, indent=1, ensure_ascii=False) + "\n")
        bad = [k for k, v in done[s].items() if v.get("status") != "ok"]
        later = sum(len(v.get("later") or []) for v in done[s].values())
        print(f"{s} ({name}): {'FAILED ' + ','.join(bad) if bad else 'ok'}; later-round headlines: {later}", flush=True)


if __name__ == "__main__":
    main()
