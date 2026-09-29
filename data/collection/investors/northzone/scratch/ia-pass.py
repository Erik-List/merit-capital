#!/usr/bin/env python3
"""Internet Archive pass for the company pages Common Crawl never captured (2009-2025) and the firm's
own posts the recall probe needs. One CDX lookup and one replay per URL, through scratch/ia.py
(machine-wide throttle and cooldown). Output scratch/ia-pass.json: url -> {ts, title, h1, text}.
A failed lookup is recorded as failed, never as an absence."""
import json, re, sys, html as H
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ia
OUT = HERE / "ia-pass.json"
res = json.loads(OUT.read_text()) if OUT.exists() else {}
URLS = [f"northzone.com/investments/{s}/" for s in ("mojn", "nuday", "outracks", "mcash", "soundrop")] + \
       [f"northzone.com/portfolio/investments-by-segment/*/{s}/" for s in ("brave-new-world", "nyx-security", "proxilliant")] + \
       [f"northzone.com/portfolio/{s}/" for s in ("gro", "statement", "arfa", "noquo-foods", "one2-1two", "salus", "heygo",
                                                 "jasper-2", "fuse", "fuse-2", "magic", "space-ape", "yonder-2", "wagestream-2")] + \
       ["northzone.com/2013/07/04/northzone-leads-9-5-million-investment-ocapo/",
        "northzone.com/2010/01/11/northzone-invests-in-the-online-backup-company/",
        "northzone.com/2011/02/02/social-recruiting-company-bravenewtalent-com-secures-venture-investment/"]
for u in (sys.argv[1:] or URLS):
    if res.get(u, {}).get("status") == "ok":
        continue
    try:
        rows = ia.cdx(f"url={u}&output=json&fl=timestamp,original,statuscode&limit=50" + ("&matchType=prefix" if "*" in u else ""))
        caps = [r for r in rows[1:] if r[2] == "200"]
        if not caps:
            res[u] = {"status": "ok", "captures": 0}
        else:
            ts, orig, _ = caps[0]
            h = ia.replay(ts, orig)
            t = re.search(r"<title>(.*?)</title>", h, flags=re.S)
            h1 = re.search(r"<h1[^>]*>(.*?)</h1>", h, flags=re.S)
            body = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S))))
            res[u] = {"status": "ok", "captures": len(caps), "ts": ts, "original": orig,
                      "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                      "title": H.unescape(t.group(1)).strip() if t else None,
                      "h1": re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else None, "text": body[:3000]}
    except Exception as e:
        res[u] = {"status": "failed", "error": str(e)[:200]}
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False))
    print(u, res[u].get("status"), res[u].get("captures"), (res[u].get("title") or "")[:60], flush=True)
