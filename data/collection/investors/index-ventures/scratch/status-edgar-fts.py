#!/usr/bin/env python3
"""Acquirer filings as a status source for rows that read private or unknown: EDGAR full-text search (2021 on, forms
8-K, 10-Q, 10-K and their exhibits) for 'acquisition of <Name>' / 'acquired <Name>' / '<Name>, Inc.'. A public buyer
states a closed purchase in its own filing ('we acquired 100% of ... Common Room, Inc.', Zoom's 10-Q of 2026-08-26),
which no headline has to carry. Writes scratch/status-edgar-fts.json: per row the hit count and the first filers.
A hit is a lead for the judge: a common name matches other companies."""
import csv, json, subprocess, sys, time, urllib.parse
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent; ROOT = H.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from shared_throttle import wait
UA = "Merit Capital Research erik@meritcapit.al"
OUT = H / "status-edgar-fts.json"; out = json.loads(OUT.read_text()) if OUT.exists() else {}
rows = [r for r in csv.DictReader(open(R / "companies/base.csv")) if r["status"] in ("private", "unknown")]
only = set(sys.argv[1:])
for r in rows:
    s = r["slug"]; n = r["name"]
    if only and s not in only: continue
    if s in out and not only: continue
    q = f'"acquisition of {n}" OR "acquired {n}" OR "acquire {n}"'
    u = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(q) + "&forms=8-K,10-Q,10-K&dateRange=custom&startdt=2021-01-01&enddt=2026-10-06"
    wait("sec")
    p = subprocess.run(["curl", "-s", "-m", "40", "-H", f"User-Agent: {UA}", u], capture_output=True, text=True)
    try:
        d = json.loads(p.stdout); hits = d["hits"]["hits"]; total = d["hits"]["total"]["value"]
    except Exception as e:
        print("FAILED", s, str(e)[:60], p.stdout[:80]); time.sleep(3); continue
    out[s] = {"name": n, "country": r["hq_country"], "status": r["status"], "query": q, "total": total,
              "filers": [{"date": h["_source"].get("file_date"), "form": h["_source"].get("form"), "filer": (h["_source"].get("display_names") or [""])[0][:60], "id": h["_id"]} for h in hits[:6]]}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    if total: print(f"{s:22s} {r['hq_country']} {total:4d} | " + " || ".join(f"{f['date']} {f['form']} {f['filer'][:34]}" for f in out[s]["filers"][:4]), flush=True)
print("done", len(out))
