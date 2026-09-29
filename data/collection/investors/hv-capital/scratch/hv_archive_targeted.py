"""One capture per distinct old-domain page (not per year): 338 targets instead of 1,774 (PRO-104).
The per-company pages carry the same text across years; the yearly portfolio lists are already parsed."""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ha", HERE / "hv_archive.py")
ha = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ha)

caps = ha.load_captures()
best = {}
for ts, orig in caps:
    if re.search(r"news|newsdetail|newspage|\.(jpg|png|gif|css|js)$", orig, re.I):
        continue
    q = orig.split("?", 1)[1] if "?" in orig else re.sub(r"^https?://[^/]+", "", orig)
    key = re.sub(r"_(en|de)$", "", q.lower().strip("/"))
    en = q.lower().endswith("_en")
    cur = best.get(key)
    # prefer the English page, then the latest capture
    if cur is None or (en, ts) > (cur[2], cur[0]):
        best[key] = (ts, orig, en)
todo = sorted((ts, orig) for ts, orig, _ in best.values())
print(f"{len(caps)} captures -> {len(todo)} distinct pages", flush=True)
got = 0
for ts, orig in todo:
    dest = ha.OLD / f"{ts}-{ha.slug_of(orig.split('holtzbrinck-ventures.com', 1)[-1])[:80]}.html"
    if dest.exists() and dest.stat().st_size:
        continue
    body, st = ha.ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
    if st.startswith("2") and body:
        dest.write_bytes(body)
        (ha.OLD / (dest.name + ".url")).write_text(f"{ts}\t{orig}\n")
        got += 1
    else:
        print(f"  {st} {ts} {orig}", flush=True)
    if got and got % 25 == 0:
        print(f"  fetched {got}", flush=True)
print(f"fetched {got} new captures", flush=True)
