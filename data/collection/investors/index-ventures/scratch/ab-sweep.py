"""A/B pass, attack leg (COLLECTION.md s7): for every visible private row ($1B+), one Google News query for 2026 news
of a newer round, a sale, a listing or a down round. Headlines land in scratch/ab-news.json; the judge reads them."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
spec = importlib.util.spec_from_file_location("merged", H / "merged.py"); mg = importlib.util.module_from_spec(spec); spec.loader.exec_module(mg)
QUAL = {"scale": '"Scale AI"', "remote": '"Remote" HR payroll', "built": '"Built Technologies"', "pave": '"Pave" compensation', "gong": '"Gong" revenue AI',
        "persona": '"Persona" identity verification', "coalition": '"Coalition" cyber insurance', "notion": '"Notion" productivity', "pilot": '"Pilot" bookkeeping startup',
        "glow": '"Glow" endpoint security', "linear": '"Linear" issue tracking', "wonderful": '"Wonderful" AI agents', "alan": '"Alan" health insurance France',
        "goat": '"GOAT" sneaker', "expel": '"Expel" security', "temporal": '"Temporal Technologies"', "fireworks": '"Fireworks AI"', "cohere": '"Cohere" AI',
        "mistral": '"Mistral AI"', "simile": '"Simile" AI', "nourish": '"Nourish" dietitians', "decagon": '"Decagon" AI', "granola": '"Granola" AI notes',
        "thatch": '"Thatch" health benefits', "motive": '"Motive" fleet', "multiverse": '"Multiverse" apprenticeships', "harmonic": '"Harmonic" AI math',
        "cowboy-space": '"Aetherflux" OR "Cowboy Space"', "kry-livi": '"Kry" OR "Livi" digital health', "applyboard-inc": '"ApplyBoard"', "parallel-web-systems": '"Parallel Web Systems"',
        "ineffable": '"Ineffable Intelligence"', "chai-discovery": '"Chai Discovery"', "rohlik": '"Rohlik"', "discord": '"Discord" IPO OR valuation'}
V = mg.view()
vis = {s: r for s, r in V.items() if r["verdict"] == "member" and r.get("status") == "private" and r.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus")}
OUT = H / "ab-news.json"; db = json.loads(OUT.read_text()) if OUT.exists() else {}
for s, r in sorted(vis.items()):
    if s in db and db[s]["status"] == "ok": continue
    q = f'{QUAL.get(s, chr(34) + r["name"] + chr(34))} (valuation OR raises OR acquired OR acquires OR IPO) after:2026-01-01'
    x = gs.googlenews(q, r["name"])
    db[s] = {"status": x["status"], "query": q, "items": [{"date": i["date"], "source": i["source"], "title": i["title"][:220], "gid": i["gid"]} for i in x.get("items", [])]}
    OUT.write_text(json.dumps(db, indent=1, ensure_ascii=False))
print(len(db), "rows;", sum(1 for v in db.values() if v["status"] != "ok"), "failed")
