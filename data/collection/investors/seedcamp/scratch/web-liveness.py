#!/usr/bin/env python3
"""The company's own website, read once per base row: a status signal for a
book of small, quiet companies (decisions.md D11; COLLECTION.md §3 rule-outs:
"unrecognized with recent evidence of life -> private; unrecognized and dark ->
unknown").

For each row with a website (the firm's list gives one), fetch it and record:
HTTP code, the final URL after redirects (a redirect to another company's
domain is an exit lead, never a verdict), the page <title>, the newest
copyright year on the page, and whether the domain looks parked or for sale.
A fetch that fails is recorded as failed: a dark site is a signal the judge
weighs with the register and the press, never a status by itself.

Output: sources/web/website-check.json {slug: {...}}
Usage: python3 web-liveness.py
"""
from __future__ import annotations

import concurrent.futures as cf
import html
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
OUT = INV / "sources" / "web" / "website-check.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
PARKED = re.compile(r"(?i)(domain (is|may be) for sale|buy this domain|this domain is parked|parkingcrew|sedo|hugedomains|dan\.com|afternic|godaddy.*parked|domain has expired|account suspended)")


def websites() -> dict[str, str]:
    base = json.loads((INV / "companies" / "base.json").read_text())
    site = {re.sub(r"[^a-z0-9]", "", r["name"].lower()): r.get("website")
            for r in json.loads((INV / "sources" / "site" / "companies-2026.json").read_text())["rows"]}
    arch = {}
    for f in sorted((INV / "sources" / "wayback" / "parsed").glob("*.json")):
        for r in json.loads(f.read_text()):
            if r.get("website"):
                arch[r["slug"]] = r["website"]
    out = {}
    for r in base:
        k = re.sub(r"[^a-z0-9]", "", r["name"].lower())
        w = site.get(k) or arch.get(r["slug"])
        if w:
            out[r["slug"]] = w
    return out


def check(url: str) -> dict:
    if not url.startswith("http"):
        url = "http://" + url
    p = subprocess.run(["curl", "-sL", "--max-time", "25", "--max-redirs", "8", "-A", UA,
                        "-o", "-", "-w", "\n__META__%{http_code} %{url_effective}", url],
                       capture_output=True)
    body, _, meta = p.stdout.decode("utf-8", "replace").rpartition("\n__META__")
    code, _, final = meta.partition(" ")
    if p.returncode != 0 and not body:
        return {"url": url, "status": "failed", "rc": p.returncode}
    t = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
    years = [int(y) for y in re.findall(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?(20\d\d)", body, re.I)]
    return {"url": url, "status": "ok", "http": code, "final": final,
            "title": " ".join(html.unescape(t.group(1)).split())[:160] if t else None,
            "copyright": max(years) if years else None,
            "parked": bool(PARKED.search(body[:20000])), "bytes": len(body)}


def main() -> int:
    ws = websites()
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    todo = {s: u for s, u in ws.items() if out.get(s, {}).get("status") != "ok"}
    with cf.ThreadPoolExecutor(8) as ex:
        for s, res in zip(todo, ex.map(check, todo.values())):
            out[s] = res
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({k: out[k] for k in sorted(out)}, indent=1, ensure_ascii=False) + "\n")
    ok = sum(1 for v in out.values() if v.get("status") == "ok")
    print(len(ws), "rows with a website;", ok, "answered;", len(out) - ok, "failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
