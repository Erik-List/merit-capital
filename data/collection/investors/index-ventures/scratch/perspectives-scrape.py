#!/usr/bin/env python3
"""Read every Perspectives post on indexventures.com (sitemap-perspectives.xml):
title, datePublished (JSON-LD), author, the companies it links (/companies/<slug>/),
and the sentences that name a round. Raw pages under
data/filings/index-ventures/perspectives-raw/ (gitignored). Writes
sources/site/perspectives.json: the firm's own announcement archive, the news
surface of this run (COLLECTION.md s5, s6: an announcement is class 1 for the
round it NAMES; it asserts an entry only where the post says so in words)."""
import html as H
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT.parents[2] / "filings" / "index-ventures" / "perspectives-raw"
RAW.mkdir(parents=True, exist_ok=True)
BASE = "https://www.indexventures.com"
UA = "Mozilla/5.0 (MeritCapitalResearch; erik@meritcapit.al)"
ROUND = re.compile(r"\b(pre-?seed|seed|series [A-K]\b|series-[a-k]\b|growth round|funding round|financing|"
                   r"investment in|invested in|led by|we led|leading|co-led|raised|raises|\$\s?\d[\d.,]*\s?(?:m|million|bn|billion)|"
                   r"€\s?\d[\d.,]*\s?(?:m|million|bn|billion)|£\s?\d[\d.,]*\s?(?:m|million|bn|billion)|first backed|first invested|"
                   r"since (?:the|their|its) seed|acquired by|acquisition|ipo\b|goes public|public offering)", re.I)


def get(url, dest):
    gz = Path(str(dest) + ".gz")      # raw pages were gzipped on 2026-10-01 (disk space)
    if gz.exists() and gz.stat().st_size > 0:
        import gzip
        return gzip.open(gz, "rt", errors="replace").read()
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_text(errors="replace")
    for i in range(3):
        r = subprocess.run(["curl", "-sS", "-L", "--max-time", "40", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
        if r.returncode == 0 and code == "200":
            dest.write_text(body)
            time.sleep(0.2)
            return body
        if code == "404":
            return None
        time.sleep(3 * (i + 1))
    return None


def sentences(text):
    # keep decimals: "$5.1M" must not split (COLLECTION.md s5, evidence-pack mechanics)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“])", text) if s.strip()]


sm = get(f"{BASE}/sitemap-perspectives.xml", RAW / "_sitemap.xml") if "--refresh" not in sys.argv else None
if sm is None:
    (RAW / "_sitemap.xml").unlink(missing_ok=True)
    sm = get(f"{BASE}/sitemap-perspectives.xml", RAW / "_sitemap.xml")
locs = [l for l in re.findall(r"<loc>([^<]+)</loc>", sm) if re.fullmatch(rf"{re.escape(BASE)}/perspectives/[^/]+/", l)
        and not re.fullmatch(r".*/perspectives/\d+/", l)]
print("posts", len(locs), flush=True)


def one(url):
    slug = url.rstrip("/").split("/")[-1]
    h = get(url, RAW / f"{slug[:180]}.html")
    if h is None:
        return {"url": url, "slug": slug, "missing": True}
    d = re.search(r'"datePublished":\s*"([^"]*)"', h)
    main = h[h.find('<article role="main"'):] if '<article role="main"' in h else h
    main = main.split("<footer")[0]
    t = re.search(r"<h1[^>]*>(.*?)</h1>", main, flags=re.S)
    title = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", t.group(1)))).strip() if t else None
    lines = [H.unescape(x.strip()) for x in re.sub(r"<[^>]+>", "\n", re.sub(
        r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>", "", main, flags=re.S)).split("\n") if x.strip()]
    kind = lines[3] if len(lines) > 3 and lines[0] == "Navigate back to" else None
    author = None
    if "by" in lines[:12]:
        author = lines[lines.index("by") + 1]
    # body paragraphs as rendered, joined so inline links do not break sentences
    paras = [re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", p))).strip()
             for p in re.findall(r"<p[^>]*>(.*?)</p>", main, flags=re.S)]
    text = " ".join(p for p in paras if p)
    sents = [s for s in sentences(text) if ROUND.search(s)]
    comp = sorted(set(re.findall(r'href="/companies/([^"/]+)/"', main)))
    ext = sorted(set(u for u in re.findall(r'href="(https?://[^"]+)"', main)
                     if not re.search(r"indexventures\.com|twitter\.com/intent|facebook\.com/sharer|linkedin\.com/share|x\.com/intent", u)))[:12]
    return {"url": url, "slug": slug, "title": title, "date": d.group(1) if d else None, "kind": kind, "author": author,
            "companies": comp, "round_sentences": sents[:14], "lede": text[:600], "words": len(text.split()), "links": ext}


with ThreadPoolExecutor(4) as ex:
    rows = list(ex.map(one, locs))
rows.sort(key=lambda r: (r.get("date") or "", r["slug"]))
out = {"_readme": "indexventures.com Perspectives archive, read by scratch/perspectives-scrape.py on %s: "
                  "one row per post with its JSON-LD datePublished, the companies it links and the sentences "
                  "that name a round. Raw pages under data/filings/index-ventures/perspectives-raw/ (gitignored)."
                  % date.today().isoformat(), "rows": rows}
(ROOT / "sources" / "site" / "perspectives.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(len(rows), "rows;", sum(1 for r in rows if r.get("missing")), "missing;",
      sum(1 for r in rows if r.get("date")), "dated;", sum(1 for r in rows if r.get("companies")), "link a company")
