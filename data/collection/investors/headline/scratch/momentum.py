"""Momentum slice (COLLECTION.md s6 valuation, s7): one dated Google News check per
private hot-sector row first seen since 2021, for a mark at or above $1B the base lacks.
Writes scratch/momentum.json {slug: {query, asof, status, items}}; a failed lookup is
recorded as failed, never as empty."""
import importlib.util, json, sys
from datetime import date
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
NAMES = json.loads(Path(__file__).with_name("momentum-names.json").read_text())
out_p = Path(__file__).with_name("momentum.json")
out = json.loads(out_p.read_text()) if out_p.exists() else {}
for slug, name in NAMES.items():
    if out.get(slug, {}).get("status") == "ok":
        continue
    q = f'"{name}" (valuation OR valued OR unicorn OR billion OR raises OR "series b" OR "series c")'
    res = gs.googlenews(q, name)
    out[slug] = {"query": q, "asof": date.today().isoformat(), "status": res["status"],
                 "items": [{"date": i["date"], "title": i["title"], "source": i["source"], "gid": i.get("gid")}
                           for i in res.get("items", []) if i.get("names")]}
    out_p.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(slug, res["status"], len(out[slug]["items"]), flush=True)
