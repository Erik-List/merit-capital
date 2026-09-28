#!/usr/bin/env python3
"""TechCrunch / Crunchbase News WordPress search per company, reading each
post's own content for sentences naming 20VC or Harry Stebbings. Bypasses the
shared Google News rate (the WordPress APIs are paced separately).

Usage: python3 wp-check.py "Name" ["Name" ...]   -> scratch/recall/wp.json
"""
import html, json, re, subprocess, sys, time, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
OUT = HERE / "recall" / "wp.json"
FIRM = re.compile(r"\b20\s?VC\b|Twenty ?Minute ?VC|Stebbings|20Growth|20Sales|20Product", re.I)
SITES = {"techcrunch": "https://techcrunch.com", "crunchbase_news": "https://news.crunchbase.com"}


def get(url):
    r = subprocess.run(["curl", "-s", "-L", "--max-time", "40", "-w", "\n%{http_code}", url], capture_output=True)
    body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
    return code, body


def sentences(htm):
    t = html.unescape(re.sub(r"<[^>]+>", " ", htm))
    t = re.sub(r"\s+", " ", t)
    out = []
    for s in re.split(r"(?<=[.!?])(?<!\d\.)\s+(?=[A-Z\"'“])", t):
        if FIRM.search(s) and 15 < len(s) < 700 and s not in out:
            out.append(s.strip())
    return out[:8]


data = json.loads(OUT.read_text()) if OUT.exists() else {}
names = sys.argv[1:]
if names and names[0] == "--file":
    names = [l.strip() for l in Path(names[1]).read_text().splitlines() if l.strip()]
for name in names:
    if name in data:
        continue
    rec = {}
    for svc, base in SITES.items():
        code, body = get(f"{base}/wp-json/wp/v2/posts?search={urllib.parse.quote(name)}&per_page=40"
                         f"&_fields=date,link,title,content")
        time.sleep(2)
        if code != "200":
            rec[svc] = {"status": f"http {code}"}
            continue
        try:
            posts = json.loads(body)
        except ValueError:
            rec[svc] = {"status": "not json"}
            continue
        hits = []
        for p in posts:
            content = (p.get("content") or {}).get("rendered", "")
            title = html.unescape(re.sub(r"<[^>]+>", "", (p.get("title") or {}).get("rendered", "")))
            if not re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", title + " " + content, re.I):
                continue
            s = sentences(content)
            if s:
                hits.append({"date": p["date"][:10], "title": title, "link": p["link"], "sentences": s})
        rec[svc] = {"status": f"ok {len(posts)}", "hits": hits}
    data[name] = rec
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    for svc, r in rec.items():
        for h in r.get("hits", []):
            print(f"{name} | {svc} {h['date']} {h['title'][:80]} | {h['link']}")
            for s in h["sentences"][:3]:
                print(f"     > {s[:260]}")
    print(f"{name}: " + ", ".join(f"{k} {v['status']} ({len(v.get('hits', []))} naming the firm)" for k, v in rec.items()), flush=True)
