#!/usr/bin/env python3
"""The title and meta description of every listed company's own homepage
(sources/web/company-sites.json): what the company says it is, for the rows
the judge cannot place from memory. One request per company, cached.
A failed fetch is recorded as failed, never as an empty description."""
import json, re, subprocess, html, time
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
rows = json.load(open(INV / "sources/site/portfolio-2026.json"))["rows"]
out_p = INV / "sources/web/company-sites.json"
out = json.load(open(out_p)) if out_p.exists() else {}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
for r in rows:
    u = r.get("company_site")
    if not u or (r["name"] in out and out[r["name"]].get("status") == "ok"): continue
    p = subprocess.run(["curl", "-sL", "-m", "20", "-A", UA, "-w", "\n%{http_code}", u], capture_output=True)
    body, _, code = p.stdout.rpartition(b"\n")
    t = body.decode("utf-8", "replace")
    if p.returncode != 0 or code != b"200":
        out[r["name"]] = {"url": u, "status": f"failed rc={p.returncode} http={code.decode()}"}
    else:
        title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
        desc = re.search(r'<meta[^>]+(?:name|property)=["\'](?:description|og:description)["\'][^>]+content=["\'](.*?)["\']', t, re.S | re.I)
        out[r["name"]] = {"url": u, "status": "ok", "title": html.unescape(re.sub(r"\s+", " ", title.group(1)).strip())[:200] if title else None,
                          "description": html.unescape(re.sub(r"\s+", " ", desc.group(1)).strip())[:400] if desc else None, "pulled": time.strftime("%Y-%m-%d")}
    out_p.write_text(json.dumps(out, indent=1, ensure_ascii=False)); time.sleep(0.3)
print(len(out), "sites;", sum(1 for v in out.values() if v["status"] == "ok"), "ok")
