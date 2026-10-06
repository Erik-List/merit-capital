"""Form D sequence by name for the absence test's `formd:` line (COLLECTION.md s6): EDGAR full-text search restricted to
forms D and D/A. Writes scratch/formd-lookup.json {query: {n, filings:[{name, date, form, adsh}]}}. Uses the shared throttle."""
import json, subprocess, sys, time, urllib.parse
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from shared_throttle import wait
UA = "Merit Capital Research erik@meritcapit.al"
out_p = Path(__file__).with_name("formd-lookup.json")
out = json.loads(out_p.read_text()) if out_p.exists() else {}
for q in sys.argv[1:]:
    if q in out and out[q].get("status") == "ok":
        continue
    url = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(f'"{q}"') + "&forms=D,D%2FA"
    wait("sec")
    r = subprocess.run(["curl", "-s", "-m", "60", "-A", UA, "-H", "Accept-Encoding: identity", url], capture_output=True)
    try:
        d = json.loads(r.stdout)
        hits = d["hits"]["hits"]
        out[q] = {"status": "ok", "url": url, "n": d["hits"]["total"]["value"],
                  "filings": sorted([{"name": "; ".join(h["_source"].get("display_names") or []), "date": h["_source"].get("file_date"),
                               "form": h["_source"].get("form"), "adsh": h["_source"].get("adsh")} for h in hits], key=lambda x: x["date"] or "")}
    except Exception as e:
        out[q] = {"status": "error", "url": url, "error": f"rc={r.returncode} {e}"}
    time.sleep(0.3)
out_p.write_text(json.dumps(out, indent=1) + "\n")
for q in sys.argv[1:]:
    v = out[q]; print("##", q, v.get("status"), v.get("n"))
    for f in (v.get("filings") or [])[:8]: print("   ", f["date"], f["form"], f["name"][:90])
