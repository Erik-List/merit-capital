"""Find citable press for a claim: Google News headlines (via scripts/graduation-surfaces.py,
shared throttle), filtered by required substrings, top N decoded to the publisher URL.
usage: cite.py "<query>" "<must1,must2>" [N]   -- or a TSV file of such lines with --file"""
import importlib.util, sys, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
def run(query, musts, n=2):
    res = gs.googlenews(query, query.split('"')[1] if '"' in query else query)
    if res["status"] != "ok":
        print("  ERR", res.get("status")); return
    items = [i for i in res["items"] if all(m.lower() in i["title"].lower() for m in musts if m)]
    print(f"== {query} -> {res['n']} items, {len(items)} match")
    for i in items[:n]:
        url = gs.decode(i["gid"]) or ""
        print(f"  {i['date']} | {i['source']} | {i['title'][:140]} | {url}")
if argv and argv[0] == "--file":
    for line in Path(argv[1]).read_text().splitlines():
        if not line.strip(): continue
        q, m, *rest = line.split("\t")
        run(q, m.split(","), int(rest[0]) if rest else 2)
else:
    run(argv[0], argv[1].split(",") if len(argv) > 1 else [], int(argv[2]) if len(argv) > 2 else 2)
