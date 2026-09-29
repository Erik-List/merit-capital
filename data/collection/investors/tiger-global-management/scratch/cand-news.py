#!/usr/bin/env python3
"""Per-candidate press evidence (PRO-167): one Google News query per candidate company,
'"<name>" "Tiger Global"', kept whole so the judge and the recall triage read the same
headlines. A candidate comes from any layer (press sweep headline, parametric recall
list, EDGAR filer, Form D issuer, full-text registrant, Wikipedia article).

    python3 cand-news.py <candidates.json>      # [{"name": ..., "key": ...}, ...]

Output: scratch/cand-news.json  {key: {status, n, items[], query}}; a failed query is
stored as an error and retried on the next run, never as an empty answer.
"""
import importlib.util, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

OUT = HERE / "cand-news.json"
done = json.loads(OUT.read_text()) if OUT.exists() else {}
cands = json.loads(Path(argv[0]).read_text())
todo = [c for c in cands if done.get(c["key"], {}).get("status") != "ok"]
print(f"{len(cands)} candidates, {len(todo)} to query", flush=True)
failed = 0
for i, c in enumerate(todo):
    name = gs.clean_name(re.sub(r"\s*\(.*?\)", "", c["name"]))
    q = f'"{name}" "Tiger Global"'
    r = gs.googlenews(q, name)
    r["name"] = c["name"]
    done[c["key"]] = r
    if r["status"] != "ok":
        failed += 1
    if i % 25 == 0:
        print(f"{i:5d} {r.get('n')} {q}", flush=True)
        write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
print(f"done: {len(done)} stored, {failed} failed this pass", flush=True)
sys.exit(3 if failed else 0)
