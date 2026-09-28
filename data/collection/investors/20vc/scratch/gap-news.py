#!/usr/bin/env python3
"""Targeted Google News reads for the batch rows whose 20VC round is not yet
found (PRO-76). Each (slug, name, query) runs one Google News search (shared
throttle in scripts/graduation-surfaces.py); the headlines naming the company
are decoded (up to --decode N) and read for sentences naming 20VC / Harry
Stebbings and the round sentences (rounds-research.read). A failed read is
recorded as failed, never dropped.
Output: scratch/research/gap.json {slug: [{query, status, items, other_titles}]} (merged).
Usage: python3 gap-news.py <spec.json> [--decode 4]
spec.json: [[slug, name, query], ...]"""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rr", HERE / "rounds-research.py")
rr = importlib.util.module_from_spec(spec)
_argv, sys.argv = sys.argv, sys.argv[:1]
spec.loader.exec_module(rr)
sys.argv = _argv
OUT = HERE / "research" / "gap.json"


def main():
    a = sys.argv[1:]
    n = int(a[a.index("--decode") + 1]) if "--decode" in a else 4
    jobs = json.loads(Path(a[0]).read_text())
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for slug, name, q in jobs:
        res = rr.gs.googlenews(q, name)
        rec = {"query": q, "status": res.get("status"), "items": []}
        if res.get("status") == "ok":
            named = [i for i in res["items"] if i["names"]]
            # funding-shaped headlines first, then the rest, newest last
            named.sort(key=lambda i: (not rr.FUND.search(i["title"]), i["date"] or ""))
            for it in named[:n]:
                url = rr.gs.decode(it["gid"]) if it.get("gid") else None
                st, sents = rr.read(url, name) if url else ("decode failed", [])
                rec["items"].append({"date": it["date"], "title": it["title"], "source": it["source"],
                                     "link": url, "read": st, "sentences": sents})
            rec["other_titles"] = [(i["date"], i["source"], i["title"][:150]) for i in res["items"]
                                   if i not in named[:n]][:20]
        data.setdefault(slug, [])
        data[slug] = [r for r in data[slug] if r["query"] != q] + [rec]
        rr.write_atomic(OUT, json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        firm = sum(1 for it in rec["items"] for x in it["sentences"] if rr.FIRM.search(x))
        print(f"{slug} [{q}]: {res.get('status')} {res.get('n')} results, {len(rec['items'])} read, "
              f"{firm} firm sentences", flush=True)


if __name__ == "__main__":
    main()
