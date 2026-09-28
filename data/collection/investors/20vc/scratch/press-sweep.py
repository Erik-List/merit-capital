#!/usr/bin/env python3
"""Press sweep: every funding article that names 20VC, 2020 onward.

20VC files nothing per company (Delaware fund L.P.s and platform series funds,
European portfolio, no board seats to speak of), so the firm's own list and the
press are the two first-party-adjacent layers. The live list carries 79 cards;
the firm reports 31 companies in Fund I alone. This layer is the recall probe's
primary structural source (COLLECTION.md s5, the Thrive precedent: "press
sweeps run as a primary layer").

Three stages, each resumable (results cached in scratch/press/):
  1. search  Google News RSS (scripts/graduation-surfaces.py googlenews, paced by
             the shared throttle) over quarterly windows 2020-Q1..2026-Q3 and a
             set of phrasings; WordPress search on the news sites that expose it.
  2. decode  a Google News id to the publisher's URL (graduation-surfaces decode).
  3. read    the article, keeping every sentence that names the firm or its
             founder, and the round words and amounts in the title and those
             sentences.

A fetch that fails is recorded as failed, never as "no mention" (the absence vs
failure rule). Output: sources/press/articles.json, one record per article.

Usage: python3 press-sweep.py [search|decode|read|all] [--max N]
"""
import html
import importlib.util
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
I = HERE.parent
CACHE = HERE / "press"
OUT = I / "sources" / "press" / "articles.json"
CACHE.mkdir(parents=True, exist_ok=True)
OUT.parent.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
_argv, sys.argv = sys.argv, sys.argv[:1]
spec.loader.exec_module(gs)
sys.argv = _argv

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
FIRM_RE = re.compile(r"\b20\s?VC\b|Twenty ?Minute ?VC|\bTwenty VC\b|Stebbings|20Growth|20Sales|20Product",
                     re.I)
ROUND_RE = re.compile(r"\b(pre-?seed|seed|series [a-h]|growth round|bridge|extension|"
                      r"angel round|funding round|round)\b", re.I)
AMOUNT_RE = re.compile(r"(?:[$€£]\s?\d[\d.,]*\s?(?:m|mn|million|bn|billion|k)\b|"
                       r"\b\d[\d.,]*\s?(?:million|billion|m|bn)\s?(?:dollars|euros|pounds|usd|eur|gbp)?\b)",
                       re.I)


def quarters():
    for y in range(2020, 2027):
        for q, (a, b) in enumerate((("01-01", "03-31"), ("04-01", "06-30"),
                                    ("07-01", "09-30"), ("10-01", "12-31")), 1):
            if (y, q) > (2026, 3):
                return
            yield f"{y}-{a}", f"{y}-{b}"


PHRASES = [
    '"20VC" (raises OR raised OR seed OR "pre-seed" OR "series a" OR "series b" OR funding OR round)',
    '"Harry Stebbings" (raises OR raised OR seed OR "series a" OR funding OR round OR backed)',
]
GLOBAL = [
    '"led by 20VC"', '"20VC led"', '"20VC Fund"', '"from 20VC"', '"including 20VC"',
    '"and 20VC"', '"20VC and"', '"20VC," seed', '"20VC" "pre-seed"', '"20VC" "Series A"',
    '"20VC" "Series B"', '"Twenty Minute VC" raises', '"20VC" backed startup',
    '"Harry Stebbings" angel', '"Harry Stebbings" "20VC" invests', '"20Growth"',
    '"20Sales" fund', '"20Product" fund', '"20VC" funding', '"20VC" participation',
    '"20VC" investors', '"20VC" "led the round"', '"20VC" "co-led"',
]
# Home-market editions: 20VC's book is European first (the live list: London,
# Berlin, Paris, Munich, Dublin, Amsterdam, Sydney, Sao Paulo).
LOCAL = [("de", "DE", '"20VC" (Finanzierung OR Millionen OR Seed OR "Series A")'),
         ("fr", "FR", '"20VC" (lève OR levée OR millions OR seed OR "série A")'),
         ("en", "GB", '"20VC" (raises OR seed OR "Series A" OR funding)'),
         ("en", "IE", '"20VC" (raises OR seed OR "Series A" OR funding)'),
         ("en", "AU", '"20VC" (raises OR seed OR "Series A" OR funding)'),
         ("nl", "NL", '"20VC" (investering OR financiering OR miljoen OR seed)'),
         ("es", "ES", '"20VC" (ronda OR financiación OR millones OR seed)'),
         ("pt-BR", "BR", '"20VC" (rodada OR investimento OR milhões OR seed)'),
         ("sv", "SE", '"20VC" (finansiering OR investering OR miljoner OR seed)'),
         ("it", "IT", '"20VC" (round OR finanziamento OR milioni OR seed)')]
WORDPRESS = ["https://techcrunch.com", "https://news.crunchbase.com", "https://www.deutsche-startups.de",
             "https://www.businesscloud.co.uk", "https://www.siliconrepublic.com", "https://www.startupdaily.net"]


def load(name, default):
    f = CACHE / name
    return json.loads(f.read_text()) if f.exists() else default


def save(name, data):
    write_atomic(CACHE / name, json.dumps(data, indent=1, ensure_ascii=False) + "\n")


def search():
    done = load("queries.json", {})
    items = load("items.json", {})

    def run(key, fn):
        if done.get(key, {}).get("status") == "ok":
            return
        res = fn()
        if res.get("status") != "ok":
            done[key] = {"status": "failed", "http": res.get("http")}
            print("  FAILED", key, res.get("http"))
            return
        n_new = 0
        for it in res["items"]:
            gid = it.get("gid") or it.get("link")
            if not gid:
                continue
            rec = items.setdefault(gid, {"gid": it.get("gid"), "link": it.get("link"),
                                         "title": it["title"], "date": it["date"],
                                         "source": it.get("source"), "queries": [],
                                         "excerpt": it.get("excerpt")})
            if key not in rec["queries"]:
                rec["queries"].append(key)
                n_new += 1
        done[key] = {"status": "ok", "n": res.get("n", len(res["items"]))}
        print(f"  {key[:110]}: {res.get('n', len(res['items']))} items ({n_new} new)")
        save("queries.json", done)
        save("items.json", items)

    for a, b in quarters():
        for ph in PHRASES:
            q = f"{ph} after:{a} before:{b}"
            run("gn|" + q, lambda q=q: gs.googlenews(q, "20VC"))
    for q in GLOBAL:
        run("gn|" + q, lambda q=q: gs.googlenews(q, "20VC"))
    for hl, gl, q in LOCAL:
        run(f"gn-{gl}|" + q, lambda q=q, hl=hl, gl=gl: gs.googlenews(q, "20VC", hl=hl, gl=gl))
    for base in WORDPRESS:
        for term in ("20VC", "Harry Stebbings"):
            def wp(base=base, term=term):
                out = {"status": "ok", "items": [], "n": 0}
                for page in range(1, 6):
                    code, body = gs.curl(f"{base}/wp-json/wp/v2/posts?search={term.replace(' ', '%20')}"
                                         f"&per_page=100&page={page}&_fields=date,link,title")
                    if code == 400:          # past the last page
                        break
                    if code != 200:
                        return {"status": "error", "http": code}
                    try:
                        posts = json.loads(body)
                    except ValueError:
                        return {"status": "error", "http": code}
                    for p in posts:
                        t = html.unescape(re.sub(r"<[^>]+>", "", (p.get("title") or {}).get("rendered", "")))
                        out["items"].append({"gid": None, "link": p.get("link"), "title": t,
                                             "date": (p.get("date") or "")[:10], "source": base.split("//")[1]})
                    if len(posts) < 100:
                        break
                    time.sleep(1.0)
                out["n"] = len(out["items"])
                return out
            run(f"wp|{base}|{term}", wp)
    print(f"search: {len(items)} unique items; failed queries: "
          f"{sum(1 for v in done.values() if v.get('status') != 'ok')}")


FUNDING_RE = re.compile(r"\b(rais|secur|bag|land|nab|funding|financ|round|seed|series|backs|backed|"
                        r"invest|led by|co-led|million|\$\d|€\d|£\d|\d+m\b|acquir|sammelt|erhält|bekommt|"
                        r"lève|levée|millions|miljoner|miljoen|rodada|ronda)", re.I)
PODCAST_RE = re.compile(r"^20VC\b|20VC x SaaStr|\bpodcast\b|\binterview\b|\bepisode\b", re.I)


def priority(rec):
    t = rec.get("title") or ""
    return (0 if FUNDING_RE.search(t) and not PODCAST_RE.search(t) else 1, rec.get("date") or "")


def decode(max_n):
    items = load("items.json", {})
    n = 0
    order = sorted(items.items(), key=lambda kv: priority(kv[1]))
    for gid, rec in order:
        if rec.get("link") or not rec.get("gid"):
            continue
        if rec.get("decode_status") == "failed" and rec.get("decode_tries", 0) >= 2:
            continue
        url = gs.decode(rec["gid"])
        rec["decode_tries"] = rec.get("decode_tries", 0) + 1
        if url:
            rec["link"] = url
            rec["decode_status"] = "ok"
        else:
            rec["decode_status"] = "failed"
        n += 1
        if n % 25 == 0:
            save("items.json", items)
            print(f"  decoded {n}")
        if max_n and n >= max_n:
            break
    save("items.json", items)
    print(f"decode: {n} this pass; linked {sum(1 for r in items.values() if r.get('link'))} of {len(items)}")


def text_of(page: str) -> str:
    page = re.sub(r"<(script|style|noscript|svg|nav|footer|header)\b.*?</\1>", " ", page, flags=re.S | re.I)
    page = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>|</div>", "\n", page, flags=re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", page))
    return re.sub(r"[ \t\r\f\v]+", " ", t)


def sentences(text: str) -> list[str]:
    out = []
    # split on sentence ends that are not a decimal point ("$5.1M pre-seed": the Cherry lesson)
    for para in text.split("\n"):
        for s in re.split(r"(?<=[.!?])(?<!\d\.)\s+(?=[A-Z\"'“])", para):
            s = s.strip()
            if 20 <= len(s) <= 700 and FIRM_RE.search(s):
                out.append(s)
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq[:12]


def read(max_n):
    items = load("items.json", {})
    n = 0
    for key, rec in sorted(items.items(), key=lambda kv: priority(kv[1])):
        url = rec.get("link")
        if not url or rec.get("read_status") == "ok" or rec.get("read_tries", 0) >= 2:
            continue
        rec["read_tries"] = rec.get("read_tries", 0) + 1
        try:
            r = subprocess.run(["curl", "-s", "-L", "--max-time", "30", "-A", UA,
                                "-H", "Accept-Language: en-US,en;q=0.9", "-w", "\n%{http_code}", url],
                               capture_output=True, timeout=45)
            body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
        except subprocess.TimeoutExpired:
            body, code = "", "000"
        rec["http"] = code
        if code != "200" or len(body) < 500:
            rec["read_status"] = "failed"
        else:
            sents = sentences(text_of(body))
            rec["sentences"] = sents
            rec["read_status"] = "ok"
            rec["names_firm"] = bool(sents)
        n += 1
        if n % 25 == 0:
            save("items.json", items)
            print(f"  read {n}")
        if max_n and n >= max_n:
            break
        time.sleep(0.4)
    save("items.json", items)
    ok = sum(1 for r in items.values() if r.get("read_status") == "ok")
    print(f"read: {n} this pass; ok {ok}, failed {sum(1 for r in items.values() if r.get('read_status') == 'failed')}, "
          f"naming the firm {sum(1 for r in items.values() if r.get('names_firm'))}")


def publish():
    items = load("items.json", {})
    rows = []
    for rec in items.values():
        title = rec.get("title") or ""
        blob = title + " " + " ".join(rec.get("sentences") or [])
        rows.append({**{k: rec.get(k) for k in ("title", "date", "source", "link", "queries",
                                               "read_status", "http", "names_firm", "sentences")},
                     "rounds": sorted({m.group(1).lower() for m in ROUND_RE.finditer(blob)}),
                     "amounts": sorted({m.group(0) for m in AMOUNT_RE.finditer(blob)})[:6]})
    rows.sort(key=lambda r: (r.get("date") or "", r.get("title") or ""))
    write_atomic(OUT, json.dumps({
        "_readme": ("Press articles naming 20VC or its founder, 2020-2026 (scratch/press-sweep.py): "
                    "Google News RSS over quarterly windows and fixed phrasings, plus the WordPress "
                    "search of TechCrunch, Crunchbase News, deutsche-startups.de, BusinessCloud, "
                    "Silicon Republic and Startup Daily. `sentences` are the article's own sentences "
                    "naming the firm; read_status 'failed' means the page could not be read, never "
                    "that it does not name the firm."),
        "rows": rows}, indent=1, ensure_ascii=False) + "\n")
    print(f"published {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 0
    if what in ("search", "all"):
        search()
    if what in ("decode", "all"):
        decode(mx)
    if what in ("read", "all"):
        read(mx)
    publish()
