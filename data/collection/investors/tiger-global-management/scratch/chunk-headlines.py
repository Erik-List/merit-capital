#!/usr/bin/env python3
"""Split the press sweep's unique headlines into chunks for the extraction agents
(PRO-167). Each line: <gid-index>\t<date>\t<source>\t<title>. The index maps back to
the gid through scratch/recall/headline-index.json."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
d = json.loads((HERE.parent / "sources/web/press-sweep.json").read_text())
items = {}
for q, v in d.items():
    if v.get("status") != "ok":
        continue
    for i in v["items"]:
        if i.get("gid") and i["gid"] not in items:
            items[i["gid"]] = {**i, "query": q}
rows = sorted(items.values(), key=lambda i: (i["date"] or "", i["title"]))
idx = {str(n): r["gid"] for n, r in enumerate(rows)}
(HERE / "recall").mkdir(exist_ok=True)
(HERE / "recall/headline-index.json").write_text(json.dumps(idx) + "\n")
(HERE / "recall/headlines-all.json").write_text(json.dumps(rows, ensure_ascii=False) + "\n")
N = 520
for c in range(0, len(rows), N):
    with open(HERE / f"recall/headlines-{c // N:02d}.tsv", "w") as f:
        for n in range(c, min(c + N, len(rows))):
            r = rows[n]
            t = r["title"].replace("\t", " ")
            f.write(f"{n}\t{r['date']}\t{(r.get('source') or '')[:30]}\t{t}\n")
print(len(rows), "headlines ->", (len(rows) + N - 1) // N, "chunks")
