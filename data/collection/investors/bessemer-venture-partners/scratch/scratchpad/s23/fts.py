import sys, json, hashlib, subprocess, urllib.parse
from pathlib import Path
HERE = Path("/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch")
for q in sys.argv[1:]:
    u = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(q) + "&dateRange=custom&startdt=2001-01-01&enddt=2012-12-31"
    subprocess.run(["python3", str(HERE / "secget.py"), u, "--grep", "zzzz"], capture_output=True, cwd=HERE)
    f = HERE / "sec-cache" / (hashlib.sha1(u.encode()).hexdigest() + ".txt")
    try:
        d = json.loads(f.read_text())
    except Exception as e:
        print("##", q, "ERR", e); continue
    if "hits" not in d:
        print("##", q, "NOHITS", str(d)[:200]); continue
    print("##", q, d["hits"]["total"]["value"])
    for h in d["hits"]["hits"][:6]:
        s = h["_source"]
        print("   ", h["_id"], s.get("file_type"), s.get("file_date"), (s.get("display_names") or [""])[0][:40], "|", (s.get("file_description") or "")[:50])
