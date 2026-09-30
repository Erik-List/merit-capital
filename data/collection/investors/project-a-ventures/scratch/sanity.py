"""Pull a GROQ query from Project A's public Sanity dataset (project nykgtoh6,
dataset production) into a file_list-shaped JSON under sources/site/.
COLLECTION.md s5 escalation ladder step 2 (headless-CMS query API)."""
import json, subprocess, sys, urllib.parse
q, out = sys.argv[1], sys.argv[2]
u = "https://nykgtoh6.api.sanity.io/v2021-10-21/data/query/production?query=" + urllib.parse.quote(q)
raw = subprocess.run(["curl", "-sf", "--max-time", "120", u], capture_output=True, check=True).stdout
d = json.loads(raw)
json.dump({"_readme": f"Sanity public query API, project nykgtoh6, dataset production, read 2026-09-30. GROQ: {q}",
           "query_url": u, "rows": d["result"]}, open(out, "w"), indent=1, ensure_ascii=False)
print(out, len(d["result"]))
