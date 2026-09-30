#!/usr/bin/env python3
"""Press sweep for Visionaries Club deals (recall layer, COLLECTION.md s3/s5).

Google News RSS through scripts/graduation-surfaces.py (paced by the shared
throttle), one query per phrase per half-year window 2019-2026, so each
window stays under the feed's ~100-item cap. Every headline is kept with its
date, source and Google id; nothing is judged here. Output:
sources/web/press-sweep.json. Usage: python3 press-sweep.py
"""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
sys.argv = sys.argv[:1]
spec.loader.exec_module(gs)
OUT = HERE.parent / "sources" / "web" / "press-sweep.json"
PHRASES = ['"Visionaries Club"', '"Visionaries Tomorrow"', '"Visionaries" venture Berlin raises']
WINDOWS = []
for y in range(2019, 2027):
    WINDOWS += [(f"{y}-01-01", f"{y}-07-01"), (f"{y}-07-01", f"{y+1}-01-01")]
data = json.loads(OUT.read_text()) if OUT.exists() else {"_readme": __doc__, "queries": {}}
for ph in PHRASES:
    for a, b in WINDOWS:
        q = f"{ph} after:{a} before:{b}"
        if data["queries"].get(q, {}).get("status") == "ok":
            continue
        res = gs.googlenews(q, "Visionaries")
        data["queries"][q] = {"status": res["status"], "n": res.get("n"),
                              "items": [{k: i.get(k) for k in ("date", "source", "title", "gid", "rounds", "amounts")} for i in res.get("items", [])]}
        print(q, res["status"], res.get("n"), flush=True)
        write_atomic(OUT, json.dumps(data, indent=1, ensure_ascii=False) + "\n")
