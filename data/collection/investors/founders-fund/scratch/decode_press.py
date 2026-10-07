"""Decode the Google News ids of the recall probe's chosen headlines to publisher URLs (cached in recall-press-urls.json)."""
import importlib.util, sys, json, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
H = Path(__file__).resolve().parent
items = json.loads((H / "recall-press.json").read_text())
cache_p = H / "recall-press-urls.json"
cache = json.loads(cache_p.read_text()) if cache_p.exists() else {}
PICK = ["Primer raises", "Ondo Raises $20M", "Huspy", "Pulley Raises $40 Million", "Mudafy", "Biometric gunmaker", "Giraffe360", "The Mirror raises", "Maverick Protocol",
        "Opal Camera", "Campus, a community college", "Lagrange Labs", "Layup Parts", "modular blockchain Avail", "AfterHour", "Seed Investment Into Open-Source AI Platform Sentient",
        "Igloo, Inc. Raises", "Caldera", "Magdrive", "Avantis", "Co-Lead Investors in Anthropic", "Founders Fund leads Halter", "Roadrunner raises", "Endurance Energy", "Stark Defence",
        "Gamgee", "leads $5 million token purchase in Anvil", "RigUp Raises $60 Million", "HQ Trivia is raising", "AI factory developer", "Founders Fund Leads $80 Million Bet on Manufacturing"]
for p in PICK:
    hit = next((i for i in items if p.lower() in i["title"].lower()), None)
    if not hit: print("NO HEADLINE", p); continue
    if p not in cache or not cache[p].get("url"):
        try: url = gs.decode(hit["gid"]) or ""
        except Exception as e: url = ""
        cache[p] = {"title": hit["title"], "date": hit["date"], "source": hit["source"], "url": url}
        time.sleep(1.0)
    print(cache[p]["date"], "|", cache[p]["url"][:150] or "(not decoded)", "|", p)
cache_p.write_text(json.dumps(cache, indent=1))
