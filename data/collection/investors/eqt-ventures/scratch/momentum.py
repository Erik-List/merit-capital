"""Momentum slice (COLLECTION.md s6): one Google News check per private hot-sector row first seen
2021 or later. Writes scratch/momentum.json: per slug the query, the headlines naming the company that
report money (rounds, amounts, valuation, unicorn, acquisition), newest first, with decoded URLs."""
import importlib.util, json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
W = '(raises OR raised OR funding OR valuation OR valued OR unicorn OR acquired OR acquires OR "series")'
Q = {
 "argil": ('"Argil" AI video', "Argil"), "depict-ai": ('"Depict.ai" OR "Depict AI"', "Depict"),
 "dottxt": ('"dottxt"', "dottxt"), "evroc": ('"evroc"', "evroc"), "fly-io": ('"Fly.io"', "Fly.io"),
 "hume-ai": ('"Hume AI"', "Hume"), "juni": ('"Juni" fintech OR "e-commerce"', "Juni"), "kaiber": ('"Kaiber" AI', "Kaiber"),
 "kota": ('"Kota" benefits OR insurance', "Kota"), "moonscale": ('"Moonscale" OR "VidLab7"', "Moonscale"),
 "payrails": ('"Payrails"', "Payrails"), "pruna-ai": ('"Pruna AI"', "Pruna"), "sifflet": ('"Sifflet"', "Sifflet"),
 "talentium": ('"Talentium"', "Talentium"), "timeless": ('"Timeless" collectibles OR investing', "Timeless"),
 "volt": ('"Volt" "open banking" OR payments Volt.io', "Volt"), "wildhero": ('"TreeCard" OR "Wildhero"', "TreeCard"),
 "beside": ('"Beside" AI phone OR receptionist', "Beside"), "billhop": ('"Billhop"', "Billhop"),
 "clarifeye": ('"Clarifeye"', "Clarifeye"), "infinit": ('"Infinit" banking OR SME OR fintech', "Infinit"),
 "marvelx": ('"MarvelX"', "MarvelX"), "meridian": ('"Meridian" payments stablecoin OR "Will Haering"', "Meridian"),
 "pactio": ('"Pactio"', "Pactio"), "paid": ('"Paid" "Manny Medina" OR "Paid.ai"', "Paid"),
 "stacks": ('"Stacks" "financial close" OR "Albert Malikov" OR accounting AI', "Stacks"),
 "strawberry": ('"Strawberry" AI browser', "Strawberry"), "ylookup": ('"Ylookup"', "Ylookup"),
 "bluebook": ('"Bluebook" AI accountants OR accounting', "Bluebook"), "instabee": ('"Instabee" OR "Budbee" OR "Instabox"', "Instabee"),
}
MONEY = re.compile(r"rais|fund|valu|unicorn|acqui|series|seed|round|\$|€|£|million|billion|miljon|millionen|investment|backs|secures|lands|bags", re.I)
out = {}
for slug, (q, name) in Q.items():
    res = gs.googlenews(f"{q} {W}" if "OR" not in q.split('"')[-1] else f"({q}) {W}", name)
    if res["status"] != "ok":
        out[slug] = {"query": q, "status": "error"}; print(slug, "ERROR"); continue
    items = [i for i in res["items"] if i["names"] and MONEY.search(i["title"])]
    items.sort(key=lambda i: i.get("date") or "", reverse=True)
    top = []
    for i in items[:4]:
        top.append({"date": i["date"], "title": i["title"], "url": gs.decode(i["gid"]) or ""})
    out[slug] = {"query": q, "status": "ok", "n": len(items), "top": top}
    print(slug, len(items))
    for t in top: print("    ", t["date"], t["title"][:120], t["url"][:110])
(Path(__file__).parent / "momentum.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
