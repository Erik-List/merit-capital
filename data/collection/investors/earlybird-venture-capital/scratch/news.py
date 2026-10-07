#!/usr/bin/env python3
"""News headline search for the row research: Bing News RSS, then Google News.

Bing News RSS carries the PUBLISHER's URL in each item, so a headline is citable
at once (measured on Tiger Global, PRO-167). Google News is tried as well and
skipped quietly when it answers 503 (it did for this machine on 2026-10-06).
Both go through the shared throttle buckets ("bingnews" 0.5/s, "googlenews").

Usage: python3 news.py "query" [--all] [--decode N] [--lang de|fr|...]
  --all       print every headline, not only those naming the first quoted word
  --decode N  resolve the first N Google headlines to publisher URLs
"""
import html
import importlib.util
import re
import subprocess
import sys
import urllib.parse
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from shared_throttle import wait  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")


def bing(q: str, mkt: str | None = None) -> dict:
    wait("bingnews", 0.5)
    url = "https://www.bing.com/news/search?q=" + urllib.parse.quote_plus(q) + "&format=rss&count=50"
    if mkt:
        url += "&mkt=" + mkt
    try:
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "25", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True, text=True, timeout=40)
    except subprocess.TimeoutExpired:
        return {"status": "error", "http": 0, "items": []}
    body, _, code = r.stdout.rpartition("\n")
    if code.strip() != "200" or "<rss" not in body[:400]:
        return {"status": "error", "http": code.strip(), "items": []}
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
                      "desc": html.unescape(ds.group(1)).strip()[:240] if ds else ""})
    return {"status": "ok", "items": items}


def main() -> None:
    argv = sys.argv[1:]
    if not argv:
        sys.exit(__doc__)
    query = argv[0]
    name = query.split('"')[1] if '"' in query else query.split()[0]
    show_all = "--all" in argv
    n_decode = int(argv[argv.index("--decode") + 1]) if "--decode" in argv else 0
    lang = argv[argv.index("--lang") + 1] if "--lang" in argv else None
    mkt = {"de": "de-DE", "fr": "fr-FR", "sv": "sv-SE", "fi": "fi-FI", "it": "it-IT", "es": "es-ES",
           "nl": "nl-NL", "at": "de-AT", "ch": "de-CH", "uk": "en-GB"}.get(lang or "")
    res = bing(query, mkt)
    items = res["items"]
    if not show_all:
        items = [i for i in items if re.search(re.escape(name), i["title"] + " " + i["desc"], re.I)]
    print(f"BING {res['status']} {res.get('http', '')}: {len(res['items'])} items, {len(items)} shown")
    for i in sorted(items, key=lambda x: x["date"] or ""):
        print(f"  {i['date']} | {i['source']} | {i['title'][:140]} | {i['url']}")
        if i["desc"]:
            print(f"      {i['desc'][:200]}")
    # Google News, when it answers
    try:
        spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
        gs = importlib.util.module_from_spec(spec)
        saved, sys.argv = sys.argv, sys.argv[:1]
        spec.loader.exec_module(gs)
        sys.argv = saved
        g = gs.googlenews(query, name) if not lang else gs.googlenews(query, name, hl=lang, gl=lang.upper() if len(lang) == 2 else "US")
    except Exception as e:  # noqa: BLE001
        g = {"status": "error", "http": str(e)[:60]}
    if g.get("status") != "ok":
        print(f"GOOGLE unavailable ({g.get('http')}): use the Bing items above, WebFetch and WebSearch")
        return
    gi = [i for i in g["items"] if show_all or i["names"]]
    print(f"GOOGLE ok: {g['n']} items, {len(gi)} shown")
    done = 0
    for i in gi[-25:]:
        url = ""
        if done < n_decode and (i["rounds"] or i["amounts"] or "acqui" in i["title"].lower()):
            url = gs.decode(i["gid"]) or ""
            done += 1
        print(f"  {i['date']} | {i['source']} | {i['title'][:150]} {url}")


if __name__ == "__main__":
    main()
