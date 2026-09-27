"""Fetch the captured body of every archive slug that joins no base row, so the
judge reads the firm's own page (name, description) and not only the index row
(COLLECTION.md §5: read the captured body; catch-all shells share one digest).
Writes scratch/wayback-bodies/<slug>.html and scratch/wayback-bodies.json."""
import json, glob, re, html, sys, hashlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
I = Path(__file__).resolve().parents[1]
OUT = I / "scratch" / "wayback-bodies"; OUT.mkdir(exist_ok=True)
new = json.load(open(I / "scratch" / "wayback-newkeys.json"))
rows = {}
for f in sorted(glob.glob(str(I / "sources/wayback/parsed/*.json"))):
    for r in json.load(open(f)):
        rows.setdefault(r["slug"], []).append(r)
res_path = I / "scratch" / "wayback-bodies.json"
res = json.load(open(res_path)) if res_path.exists() else {}
def text_of(b):
    b = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", b)
    b = re.sub(r"(?is)<!--.*?-->", " ", b)
    t = re.sub(r"(?s)<[^>]+>", " ", b)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()
for item in new:
    for slug in item["slugs"]:
        if slug in res and res[slug].get("code") == "200":
            continue
        caps = sorted(rows.get(slug, []), key=lambda r: r["snapshot_ts"])
        if not caps:
            continue
        c = caps[0]
        if c["path"] == "/portfolio_list.asp":
            res[slug] = {"code": "200", "name": c.get("name"), "text": c.get("description"), "ts": c["snapshot_ts"], "list": True}
            continue
        url = f"https://web.archive.org/web/{c['snapshot_ts']}id_/http://www.insightpartners.com{c['path']}"
        body, code = ia_fetch.get(url)
        if code == "200" and body:
            s = body.decode("utf-8", "replace")
            (OUT / f"{slug}.html").write_text(s)
            title = re.search(r"(?is)<title[^>]*>(.*?)</title>", s)
            h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", s)
            md = re.search(r'(?is)<meta[^>]+name="description"[^>]+content="([^"]*)"', s)
            og = re.search(r'(?is)<meta[^>]+property="og:title"[^>]+content="([^"]*)"', s)
            t = text_of(s)
            res[slug] = {"code": code, "ts": c["snapshot_ts"], "path": c["path"], "url": url.replace("id_/", "/"),
                         "title": text_of(title.group(1)) if title else "", "h1": text_of(h1.group(1)) if h1 else "",
                         "og": html.unescape(og.group(1)) if og else "", "meta": html.unescape(md.group(1)) if md else "",
                         "digest": hashlib.sha1(t.encode()).hexdigest()[:12], "len": len(s), "text": t[:3000]}
        else:
            res[slug] = {"code": code, "ts": c["snapshot_ts"], "path": c["path"]}
        print(slug, res[slug]["code"], (res[slug].get("title") or "")[:70], flush=True)
        json.dump(res, open(res_path, "w"), indent=1)
json.dump(res, open(res_path, "w"), indent=1)
print("done", len(res))
