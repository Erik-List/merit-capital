"""D8: score the firm's two stage claims against this book's own judged rows.
(a) live listing, data-backed in {seed, all-seed}  -> claims Seed
(b) 2009-2013 stage filter 'Seed stage' ALONE       -> claims Seed ('Early stage' is an anchor, never scored)
A hit is a row whose independently judged stage (web_verified, or model with a named deal) is Seed / Pre-Seed;
a miss is one judged Series A / Growth. Rows with no independent stage are the rows the label would fill."""
import json, collections, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
w = json.loads((R / "sources/site/companies-wagtail.json").read_text())["rows"]
cl = json.loads((R / "companies/classification.json").read_text())
rows = json.loads((R / "companies/base.json").read_text())
rows = rows["companies"] if isinstance(rows, dict) else rows
site2slug = {(r.get("site_url") or "").rstrip("/").split("/")[-1]: r["slug"] for r in rows if r.get("site_url")}
facts = json.loads((R / "sources/wayback/archive-facts.json").read_text())["cc"]
SEED = ("Seed", "Pre-Seed")
def score(name, slugs):
    out = collections.defaultdict(list)
    for s in slugs:
        c = cl.get(s) or {}
        st, src = c.get("entry_stage"), c.get("entry_stage_source")
        if st in (None, "undetermined"): out["unjudged"].append(s)
        elif st in SEED: out[f"hit:{src}"].append(s)
        else: out[f"miss:{src}"].append((s, st))
    print("==", name, "rows", len(slugs))
    for k in sorted(out): print("  ", k, len(out[k]), out[k] if k.startswith("miss") or "-v" in sys.argv else "")
    for src in ("web_verified",):
        h, m = len(out[f"hit:{src}"]), len(out[f"miss:{src}"])
        print(f"   cited score: {h}/{h+m}")
    h = sum(len(v) for k, v in out.items() if k.startswith("hit")); m = sum(len(v) for k, v in out.items() if k.startswith("miss"))
    print(f"   all judged: {h}/{h+m}")
    return out
live = [site2slug.get(r["slug_site"]) for r in w if any("seed" in b for b in (r.get("backed") or []))]
print("live label rows without a base slug:", [r["slug_site"] for r in w if any("seed" in b for b in (r.get("backed") or [])) and r["slug_site"] not in site2slug])
a = score("(a) live 'backed at Seed'", [s for s in live if s])
seed_only = [k for k, v in facts.items() if {e["value"] for e in v.get("stage_filter", [])} == {"Seed stage"}]
both = [k for k, v in facts.items() if {e["value"] for e in v.get("stage_filter", [])} >= {"Seed stage", "Early stage"}]
b = score("(b) 2009-2013 'Seed stage' alone", [k for k in seed_only if k in {r["slug"] for r in rows}])
c = score("(b2) 'Seed stage' AND 'Early stage'", [k for k in both if k in {r["slug"] for r in rows}])
json.dump({"a": {k: v for k, v in a.items()}, "b": {k: v for k, v in b.items()}, "b2": {k: v for k, v in c.items()}}, open(R / "scratch/label-score.json", "w"), indent=1)
