"""Momentum and A/B-B check (PRO-76): one Google News query per row
('"<name>" (valuation OR unicorn OR billion OR acquired OR acquires OR "shuts down")'),
shared throttle; prints headlines naming the company with a valuation/exit word,
dated 2025-01 on. Rows: every $1B+ row (pass B) and every private row with an
entry or a round since 2024 (the momentum slice). Output: scratch/research/momentum.json."""
import importlib.util, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py"); gs = importlib.util.module_from_spec(spec)
_a, sys.argv = sys.argv, sys.argv[:1]; spec.loader.exec_module(gs); sys.argv = _a
c = json.loads((HERE.parent / "companies" / "classification.json").read_text())
base = {r["slug"]: r["name"] for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
ALIAS = {"remote-com": "Remote", "kevin": "kevin.", "11x": "11x.ai", "noh-payments": "Noh", "slay": "Born", "roam": "Roam Research"}
rows = []
for s, r in c.items():
    if r.get("status") not in ("private", "public"): continue
    big = r.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus")
    recent = str(r.get("entry_date") or "") >= "2024" or any(str(x.get("date")) >= "2025" for x in r.get("funding_rounds") or [])
    if big or recent: rows.append(s)
out = {}
WORD = re.compile(r"valuation|valued|unicorn|billion|\$\d+(\.\d+)?\s?b\b|acquir|shuts? down|IPO", re.I)
for s in rows:
    name = ALIAS.get(s, base.get(s, s))
    q = f'"{name}" (valuation OR unicorn OR billion OR acquired OR acquires OR "shuts down" OR IPO)'
    res = gs.googlenews(q, name)
    hits = [i for i in res.get("items", []) if i.get("names") and (i.get("date") or "") >= "2025-01" and WORD.search(i["title"])]
    out[s] = {"query": q, "status": res.get("status"), "hits": [(i["date"], i["source"], i["title"][:170]) for i in hits]}
    print(f"{s}: {res.get('status')} {len(hits)} hits", flush=True)
(HERE / "research" / "momentum.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
