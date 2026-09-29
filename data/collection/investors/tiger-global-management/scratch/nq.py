#!/usr/bin/env python3
"""Ad-hoc Google News query for one row: python3 nq.py <slug> "<query>" [--all]
Items are appended to scratch/news-extra.json[slug] (so judge_lib.NEWS can cite them) and printed."""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gs", HERE.parents[4] / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
slug, q = argv[0], argv[1]
name = q.split('"')[1] if '"' in q else q
import fcntl as _f, time as _t
from pathlib import Path as _P
_d = _P.home() / "Library/Caches/merit-capital/locks"
_fh = None
while _fh is None:
    for _i in (0, 1):
        _h = open(_d / f"tiger-googlenews-slot-{_i}.lock", "a+")
        try:
            _f.flock(_h.fileno(), _f.LOCK_EX | _f.LOCK_NB); _fh = _h; break
        except OSError:
            _h.close()
    if _fh is None:
        _t.sleep(0.5)
res = gs.googlenews(q, name)
import os
P = HERE / (f"news-extra-{os.environ['NQ_TAG']}.json" if os.environ.get("NQ_TAG") else "news-extra.json")
d = json.loads(P.read_text()) if P.exists() else {}
have = {i["gid"] for i in d.get(slug, [])}
for it in res.get("items", []):
    if it.get("gid") not in have:
        d.setdefault(slug, []).append({k: it[k] for k in ("date", "title", "source", "gid", "names", "rounds", "amounts")} | {"query": q})
P.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
items = res.get("items", [])
if "--all" not in argv:
    items = [i for i in items if i["names"]]
print(res["status"], res.get("n"), "items")
for i in items[-15:]:
    print(f"  {i['date']} | {i['source']} | {i['title'][:160]}")
