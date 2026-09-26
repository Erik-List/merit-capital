#!/usr/bin/env python3
"""Check the research agents' citations before the judge uses them: fetch every
{url, quote} pair in the given research JSON files and report whether the page
answers and whether the quote's words appear in it. A page that refuses plain
HTTP (403/429, bot walls) is reported as `blocked`, for WebFetch to settle.

Usage: python3 verify-urls.py research-A.json [...]
"""
import html
import json
import re
import subprocess
import sys
import time

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
SKIP = ("atomico.com",)  # behind a bot checkpoint: archives only


def pairs(obj, path=""):
    if isinstance(obj, dict):
        if isinstance(obj.get("url"), str) and obj["url"].startswith("http"):
            yield path, obj["url"], obj.get("quote") or ""
        for k, v in obj.items():
            yield from pairs(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from pairs(v, f"{path}[{i}]")


def words(s):
    s = html.unescape(s).lower()
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.findall(r"[a-z0-9$£€.%']+", s)


cache = {}
for f in sys.argv[1:]:
    for row in json.load(open(f)):
        for path, url, quote in pairs(row):
            if any(d in url for d in SKIP):
                print(f"skip    {row['slug']:22} {url}")
                continue
            if url not in cache:
                r = subprocess.run(["curl", "-sL", "-m", "30", "-A", UA, "-w", "\n%{http_code}", url],
                                   capture_output=True)
                body = r.stdout.decode("utf-8", "replace")
                code = body.rsplit("\n", 1)[-1] if body else "000"
                cache[url] = (code, " ".join(words(body)))
                time.sleep(0.5)
            code, text = cache[url]
            qw = words(quote)
            if code in ("403", "429", "401", "000", "202", "503"):
                verdict = "blocked"
            elif code != "200":
                verdict = f"http{code}"
            elif not qw:
                verdict = "ok-noquote"
            else:
                # the longest run of quote words found contiguously in the page
                best = 0
                for i in range(len(qw)):
                    for j in range(len(qw), i + best, -1):
                        if " ".join(qw[i:j]) in text:
                            best = max(best, j - i)
                            break
                verdict = "ok" if best >= min(6, len(qw)) else f"weak({best}/{len(qw)})"
            print(f"{verdict:10} {row['slug']:22} {path[:40]:40} {url[:110]}")
