#!/usr/bin/env python3
"""The firm's 2017-2020 announcement posts on eqtventures.com/article/<slug>,
read from Common Crawl captures (the live site redirects to eqtgroup.com; the
posts that moved to Medium and then to stories.eqtventures.com are in
stories.json). One row per article: the earliest capture, its title, body text
and the capture URL as the citation (COLLECTION.md s1). Also the team pages'
own words for roster dating. Output: ../sources/site/articles-2017-2020.json
"""
import html as H, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "eqt-ventures"
man = json.loads((HERE.parent / "sources" / "wayback" / "cc-manifest.json").read_text())
arts = {}
for k, v in man.items():
    m = re.search(r"eqtventures\.com/article/([^/?#]+)", v["url"])
    if m and v["status"] == "ok":
        arts.setdefault(m.group(1), []).append((v["timestamp"], k, v))
rows = []
for slug, lst in sorted(arts.items()):
    ts, k, v = sorted(lst)[0]
    h = (RAW / k).read_bytes().decode("utf-8", "replace")
    t = re.search(r"<title>([^<]*)</title>", h)
    body = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<footer.*?</footer>", "", h, flags=re.S)
    L = [x.strip() for x in H.unescape(re.sub(r"<[^>]+>", "\n", body)).split("\n") if x.strip()]
    dt = re.search(r'datetime="(\d{4}-\d{2}-\d{2})', h)
    date = dt.group(1) if dt else None
    for x in ([] if date else L[:120]):
        m = re.search(r"\b(\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.? \d{1,2},? \d{4}|\d{4}-\d{2}-\d{2})\b", x)
        if m:
            date = m.group(1); break
    rows.append({"slug": slug, "url": v["url"], "capture_url": v["capture_url"], "snapshot_ts": ts,
                 "title": re.sub(r"\s*\|\s*EQT Ventures\s*$", "", H.unescape(t.group(1)) if t else ""),
                 "date_text": date, "text": "\n".join(L)[:15000]})
write_atomic(HERE.parent / "sources" / "site" / "articles-2017-2020.json",
             json.dumps({"_readme": __doc__, "rows": rows}, indent=1, ensure_ascii=False))
print(len(rows), "articles;", sum(1 for r in rows if r["date_text"]), "dated")
