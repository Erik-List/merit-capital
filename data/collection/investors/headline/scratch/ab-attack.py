"""A/B pass B (COLLECTION.md s7): one Google News query per visible row for events after
its mark date. Writes scratch/ab-attack.json."""
import importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
ROWS = {"acorns": ("Acorns", "2022-03"), "icertis": ("Icertis", "2021-03"), "lightricks": ("Lightricks", "2021-09"),
        "staffbase": ("Staffbase", "2022-03"), "swile": ("Swile", "2021-10"), "sorare": ("Sorare", "2021-09"),
        "fetch": ("Fetch Rewards", "2022-04"), "black-forest-labs": ("Black Forest Labs", "2025-12"), "gopuff": ("Gopuff", "2025-11"),
        "flutterwave": ("Flutterwave", "2026-06"), "creditas": ("Creditas", "2025-12"), "the-realreal": ("The RealReal", "2026-01"),
        "sonos": ("Sonos", "2026-01"), "appfolio": ("AppFolio", "2026-01"), "bumble": ("Bumble", "2026-01"), "mistral": ("Mistral AI", "2026-09"),
        "ami-labs": ("AMI Labs", "2026-03"), "recursive": ("Recursive Superintelligence", "2026-05"), "fundamental": ("Fundamental", "2026-02"),
        "owner": ("Owner.com", "2026-08"), "exein": ("Exein", "2026-09"), "yeahka": ("Yeahka", "2026-01"), "sonim-technologies": ("Sonim", "2026-01")}
out = {}
for slug, (name, since) in ROWS.items():
    q = f'"{name}" (acquires OR acquired OR acquisition OR IPO OR valuation OR raises OR bankruptcy OR layoffs OR "takes private")'
    r = gs.googlenews(q, name)
    items = [{"date": i["date"], "title": i["title"], "source": i["source"], "gid": i.get("gid")} for i in r.get("items", [])
             if i.get("names") and i["date"] >= since]
    out[slug] = {"query": q, "since": since, "status": r["status"], "items": items}
    print(slug, r["status"], len(items), flush=True)
Path(__file__).with_name("ab-attack.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
