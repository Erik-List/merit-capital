#!/usr/bin/env python3
"""A press view per base row for the judge: Google News headlines that name
the company, from two queries (the company with round and exit words; the
company with "Seedcamp"), through scripts/graduation-surfaces.py's
googlenews() and its shared throttle. Resumable; a failed query is recorded
as failed, never as "no coverage" (COLLECTION.md §5).

Output: scratch/news-pack.json {slug: {"q1": {...}, "q2": {...}}}
Usage: python3 news-pack.py [slug ...]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

OUT = HERE / "news-pack.json"
BING = "--bing" in argv
if BING:
    argv.remove("--bing")
    spec2 = importlib.util.spec_from_file_location("bn", HERE.parents[0] / ".." / "tiger-global-management" / "scratch" / "bing-news.py")
    bn = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(bn)


def bing_slim(q, name):
    """Bing News RSS (Tiger Global's helper, 0.5 req/s on its own budget): same shape as slim(),
    items carry the publisher URL directly. Used once the shared Google News budget was saturated."""
    r = bn.bing(q)
    if r.get("status") != "ok":
        return {"status": "failed", "http": r.get("http"), "via": "bing"}
    rx = re.compile(r"(?i)\b" + re.escape(name) + r"\b")
    items = []
    for i in r["items"]:
        if not rx.search(i["title"] + " " + (i.get("desc") or "")):
            continue
        rounds, amounts = gs.tags(i["title"])
        items.append({"date": i["date"], "title": i["title"], "source": i.get("source"), "url": i["url"],
                      "rounds": rounds, "amounts": amounts})
    items.sort(key=lambda x: x["date"] or "")
    return {"status": "ok", "n": r["n"], "naming": len(items), "items": items[-30:], "via": "bing"}
BASE = HERE.parent / "companies" / "base.json"
WORDS = "raises OR funding OR seed OR \"Series A\" OR acquired OR acquires OR shuts OR closes OR valuation"


def slim(res, name):
    if res.get("status") != "ok":
        return {"status": "failed", "http": res.get("http")}
    items = [i for i in res["items"] if i["names"]]
    keep = [{k: i[k] for k in ("date", "title", "source", "gid", "rounds", "amounts")} for i in items]
    return {"status": "ok", "n": res["n"], "naming": len(items), "items": keep[-30:]}


def main():
    base = json.loads(BASE.read_text())
    pack = json.loads(OUT.read_text()) if OUT.exists() else {}
    todo = [r for r in base if (not argv or r["slug"] in argv)]
    n = 0
    for r in todo:
        s, name = r["slug"], r["name"]
        cur = pack.get(s, {})
        if cur.get("q1", {}).get("status") == "ok" and cur.get("q2", {}).get("status") == "ok":
            continue
        q = re.sub(r'"', "", name)
        cur["name"] = name
        if cur.get("q1", {}).get("status") != "ok":
            cur["q1"] = bing_slim(f'"{q}" (raises OR funding OR seed OR acquired OR acquires OR shuts)', q) if BING \
                else slim(gs.googlenews(f'"{q}" ({WORDS})', q), q)
        if cur.get("q2", {}).get("status") != "ok":
            cur["q2"] = bing_slim(f'"{q}" Seedcamp', q) if BING else slim(gs.googlenews(f'"{q}" Seedcamp', q), q)
        pack[s] = cur
        n += 1
        if n % 25 == 0:
            write_atomic(OUT, json.dumps(pack, ensure_ascii=False) + "\n")
            print(n, "rows", flush=True)
    write_atomic(OUT, json.dumps(pack, ensure_ascii=False) + "\n")
    failed = sum(1 for v in pack.values() for k in ("q1", "q2") if v.get(k, {}).get("status") != "ok")
    print("done", len(pack), "rows,", failed, "failed queries", flush=True)
    return 3 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
