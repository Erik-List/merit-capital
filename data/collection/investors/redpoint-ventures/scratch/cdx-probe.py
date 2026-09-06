#!/usr/bin/env python3
"""One-off: enumerate redpoint.com's captured URL space to find the site eras."""
import subprocess, sys, json, pathlib
sys.path.insert(0, "scripts")
import shared_throttle

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
OUT = pathlib.Path("data/collection/investors/redpoint-ventures/scratch")

def cdx(pattern, **params):
    shared_throttle.wait("ia")
    q = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"https://web.archive.org/cdx/search/cdx?url={pattern}&output=json&{q}"
    r = subprocess.run(["curl", "-sS", "--max-time", "300", "-H", f"User-Agent: {UA}", url],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        print("FAIL", pattern, r.returncode, r.stderr[:200], flush=True)
        return []
    try:
        rows = json.loads(r.stdout)
    except Exception as e:
        print("PARSE FAIL", pattern, e, r.stdout[:200], flush=True)
        return []
    return rows[1:] if rows else []

for host in ("redpoint.com", "www.redpoint.com", "redpointventures.com"):
    rows = cdx(f"{host}/*", collapse="urlkey", fl="timestamp,original,statuscode,mimetype",
               filter="statuscode:200", limit="50000")
    print(f"{host}: {len(rows)} distinct urls", flush=True)
    (OUT / f"cdx-{host}.json").write_text(json.dumps(rows))
