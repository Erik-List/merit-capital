#!/usr/bin/env python3
"""Per-candidate press evidence from Bing News RSS (PRO-167), a second press surface.

Why: the Google News surface is one machine-wide bucket (1 request/s) and on
2026-09-29 another session's fifteen parallel clients left this run about one slot in
sixteen. Bing News RSS answers scripted queries with relevant results and carries the
PUBLISHER's URL in each item (the `url=` parameter of its click-through link), so an item
is citable without the Google decode step. It has its own bucket in shared_throttle
("bingnews", 0.5 request/s: a new service at a polite rate, not a raised one).
Measured before use: see bing-news-score.json (the layer is scored against the Google
headlines of the same candidates before it may carry a recall addition).

    python3 bing-news.py <candidates.json>      # [{"name": ..., "key": ...}, ...]

Output: scratch/bing-news.json {key: {status, n, items: [{date, title, url, source, desc}], query}}.
A failed request is stored as an error and retried on the next run, never as an empty answer.
"""
import html, json, re, subprocess, sys, urllib.parse
from email.utils import parsedate_to_datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402
from shared_throttle import wait  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
OUT = HERE / "bing-news.json"


def bing(q):
    wait("bingnews", 0.5)
    url = "https://www.bing.com/news/search?q=" + urllib.parse.quote_plus(q) + "&format=rss&count=50"
    try:
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "25", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True, text=True, timeout=40)
    except subprocess.TimeoutExpired:
        return {"status": "error", "query": q, "http": 0}
    body, _, code = r.stdout.rpartition("\n")
    if code.strip() != "200" or "<rss" not in body[:400]:
        return {"status": "error", "query": q, "http": code.strip()}
    items = []
    for it in re.findall(r"<item>(.*?)</item>", body, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it)
        s = re.search(r"<News:Source>(.*?)</News:Source>", it, re.S)
        ds = re.search(r"<description>(.*?)</description>", it, re.S)
        link = html.unescape(l.group(1)) if l else ""
        m = re.search(r"[?&]url=([^&]+)", link)
        pub = urllib.parse.unquote(m.group(1)) if m else link
        try:
            day = parsedate_to_datetime(d.group(1)).date().isoformat() if d else None
        except (TypeError, ValueError):
            day = None
        items.append({"date": day, "title": html.unescape(t.group(1)).strip() if t else "",
                      "url": pub, "source": html.unescape(s.group(1)) if s else None,
                      "desc": html.unescape(ds.group(1)).strip()[:300] if ds else None})
    return {"status": "ok", "query": q, "n": len(items), "items": items}


def main():
    from concurrent.futures import ThreadPoolExecutor
    done = json.loads(OUT.read_text()) if OUT.exists() else {}
    cands = json.loads(Path(sys.argv[1]).read_text())
    todo = [c for c in cands if done.get(c["key"], {}).get("status") != "ok"]
    print(f"{len(cands)} candidates, {len(todo)} to query", flush=True)

    def one(c):
        name = re.sub(r"\s*\(.*?\)", "", c["name"]).strip()
        r = bing(f'"{name}" "Tiger Global"')
        r["name"] = c["name"]
        return c, r

    failed = 0
    # three workers overlap curl latency; the shared bucket still paces them to 0.5 request/s
    with ThreadPoolExecutor(max_workers=3) as ex:
        for i, (c, r) in enumerate(ex.map(one, todo)):
            done[c["key"]] = r
            if r["status"] != "ok":
                failed += 1
            if i % 25 == 0 or i == len(todo) - 1:
                print(f"{i:5d} {r.get('n')} {c['name']}", flush=True)
                write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
    write_atomic(OUT, json.dumps(done, indent=1, ensure_ascii=False) + "\n")
    print(f"done: {len(done)} stored, {failed} failed this pass", flush=True)
    sys.exit(3 if failed else 0)


if __name__ == "__main__":
    main()
