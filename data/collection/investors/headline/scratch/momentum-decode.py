import importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
x = json.loads(Path(__file__).with_name("momentum.json").read_text())
PICK = {"helcim": "valuation hits", "finom": "Series C", "deepip": "Tech.eu", "didero": "Series A to Bring", "mithrl": "Business Wire",
        "netbox-labs": "crn.com", "payflows": "EU-Startups", "first-aml": "Series B", "skalar": "Pulse 2.0", "vox-ai": "Tech.eu",
        "aiprise": "Biometric", "defacto": "Finextra", "braavo": "Series B", "fonoa": "EU-Startups"}
out = {}
for slug, sub in PICK.items():
    it = [i for i in x[slug]["items"] if sub.lower() in (i["title"] + " " + i["source"]).lower()]
    if not it:
        print(slug, "NO ITEM"); continue
    i = it[-1]
    url = gs.decode(i["gid"]) if i.get("gid") else None
    out[slug] = {"date": i["date"], "title": i["title"], "url": url}
    print(slug, i["date"], url)
Path(__file__).with_name("momentum-urls.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
