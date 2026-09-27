"""Recall probe, press layer (COLLECTION.md s3): Google News headlines naming the firm as a
round's lead or participant, per year window and per name era, for a diff against the
base. Writes scratch/recall-press.json {query: {status, items}}; failures are recorded,
never read as absence."""
import importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
Q = []
for y in range(2008, 2013):
    Q.append((f'"BV Capital" (raises OR funding OR led OR round) after:{y}-01-01 before:{y+1}-01-01', "BV Capital"))
for y in range(2012, 2022):
    Q.append((f'("e.ventures" OR eventures) (raises OR funding OR led OR round) after:{y}-01-01 before:{y+1}-01-01', "e.ventures"))
for y in range(2021, 2027):
    for h in (1, 7):
        a, b = f"{y}-{h:02d}-01", (f"{y}-07-01" if h == 1 else f"{y+1}-01-01")
        Q.append((f'("led by Headline" OR "Headline led" OR "co-led by Headline" OR "from Headline" OR "Headline and") (raises OR funding OR round) after:{a} before:{b}', "Headline"))
out_p = Path(__file__).with_name("recall-press.json")
out = json.loads(out_p.read_text()) if out_p.exists() else {}
for q, name in Q:
    if out.get(q, {}).get("status") == "ok":
        continue
    r = gs.googlenews(q, name)
    out[q] = {"status": r["status"], "items": [{"date": i["date"], "title": i["title"], "source": i["source"], "gid": i.get("gid")} for i in r.get("items", [])]}
    out_p.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(q[:70], r["status"], len(out[q]["items"]), flush=True)
