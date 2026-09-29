#!/usr/bin/env python3
"""Ad-hoc Bing News query for one row (PRO-167): python3 bq.py <slug> "<query>" [--all]

The judge's second press surface beside nq.py (Google News): its own throttle bucket
("bingnews", 0.5 request/s), and every item carries the publisher's URL, so a headline is
citable at once through judge_lib.NEWS(slug, substring) without a decode. Items are appended
to scratch/news-extra-bing[-$NQ_TAG].json[slug] and printed (only headlines naming the
company unless --all)."""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bn", HERE / "bing-news.py")
bn = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(bn)
slug, q = argv[0], argv[1]
name = q.split('"')[1] if '"' in q else q
res = bn.bing(q)
tag = os.environ.get("NQ_TAG")
P = HERE / (f"news-extra-bing-{tag}.json" if tag else "news-extra-bing.json")
d = json.loads(P.read_text()) if P.exists() else {}
have = {i["url"] for i in d.get(slug, [])}
for it in res.get("items", []):
    if it["url"] not in have:
        d.setdefault(slug, []).append({"date": it["date"], "title": it["title"], "source": it.get("source"),
                                       "url": it["url"], "desc": it.get("desc"), "query": q})
P.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
items = res.get("items", [])
if "--all" not in argv:
    items = [i for i in items if re.search(re.escape(name), i["title"] + " " + (i.get("desc") or ""), re.I)]
print(res["status"], res.get("n"), "items")
for i in items[:15]:
    print(f"  {i['date']} | {i.get('source')} | {i['title'][:150]}")
    if i.get("desc"):
        print(f"      {i['desc'][:220]}")
