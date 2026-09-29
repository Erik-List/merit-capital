"""One compact view per batch: pack line + firm-name hits + round/exit headlines + siblings."""
import json, sys, re, subprocess
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import judge_lib as J
import candidates as C
b = json.loads((H / f"queue/batch-{int(sys.argv[1]):03d}.json").read_text())
only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
g = json.loads((H / "graduation-surfaces.json").read_text())
pack = subprocess.run(["python3", str(H / "pack.py"), sys.argv[1]], capture_output=True, text=True).stdout
blocks = {}
cur = None
for line in pack.splitlines():
    m = re.match(r"## (\S+) \|", line)
    if m: cur = m.group(1); blocks[cur] = []
    if cur: blocks[cur].append(line)
for it in b:
    s = it["slug"]
    if only and s not in only: continue
    print("\n".join(blocks.get(s, [f"## {s}"])))
    claim = C.entry_claim(s, it["name"])
    sv = g.get(s, {}).get("surfaces") or {}
    firm = [i for i in (sv.get("googlenews_firm") or {}).get("items", []) if i.get("names")]
    for i in firm[:9]:
        print(f"   F {i.get('date','')[:10]} {(i.get('title') or '')[:120]} |{(i.get('gid') or i.get('url') or '')[-10:]}")
    other = []
    nm = (it["name"] or s).lower().split(" (")[0]
    for svc in ("googlenews", "techcrunch", "crunchbase_news", "googlenews_local"):
        for i in (sv.get(svc) or {}).get("items", []):
            t = (i.get("title") or "")
            if i.get("names") and i.get("rounds") and (t.lower().startswith(nm) or f" {nm} " in t.lower()[:70] or f"{nm}'" in t.lower()[:70]):
                other.append(i)
    seen = set()
    for i in sorted(other, key=lambda x: x.get("date", "")):
        k = (i.get("title") or "")[:60]
        if k in seen: continue
        seen.add(k)
        print(f"   R {i.get('date','')[:10]} {(i.get('title') or '')[:120]} {{{','.join(i.get('rounds') or [])}}} |{(i.get('gid') or i.get('url') or '')[-10:]}")
    for sb in (g.get(s, {}).get("siblings") or [])[:3]:
        print(f"   SIB {sb.get('investor')}: {sb.get('entry_stage')} {sb.get('entry_stage_source')} {sb.get('entry_stage_citation') or ''} | st={sb.get('status')} band={sb.get('valuation_range')} {sb.get('valuation_usd') or ''} | grad={sb.get('seed_to_a_graduation')} {sb.get('graduation_citation') or ''} | {(sb.get('note') or '')[:140]}")
