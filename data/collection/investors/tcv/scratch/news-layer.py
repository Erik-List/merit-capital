#!/usr/bin/env python3
"""TCV's own news and press-release archive, from the Wayback CDX (PRO-169).

tcv.com published its press releases at the site root (2013-2019 WordPress:
/<title-slug>/), under /news/<slug> (2019 on) and as /<company>_ipo.html or
.pdf (2002-2006). The slug is the post's own title, so it names the company,
often the round and the amount ("nubank-raises-usd-400-million-in-a-new-
investment-round-led-by-tcv"); COLLECTION.md 5 accepts a title-only archived
post as naming its round. This lists every such post with its first capture,
and with --bodies fetches each post's archived body (first 200 capture, id_
replay, through scripts/ia_fetch.py) into sources/site/news/ and keeps the
first 1,500 characters of text.

Output: sources/site/news-archive.json
  rows: {slug, title_words, url, first_capture, capture_url, round_words[], body_text?}
A post is class 1 for the round it NAMES and asserts an entry only where it
says so in words (COLLECTION.md 6); this layer labels nothing by itself.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402

INV = Path(__file__).resolve().parents[1]
OUT = INV / "sources/site/news-archive.json"
BODIES = INV / "sources/site/news"
ROUND = re.compile(r"\b(pre-seed|seed|series-[a-k](?:-\d)?|growth(?:-equity)?|minority|majority|recapitali[sz]ation|"
                   r"ipo|acquir\w*|strategic-investment|significant-investment|investment|financing|funding)\b")
DEAL = re.compile(r"(series|seed|round|financing|funding|invest|raises|secures|closes|led-by|growth|acquir|ipo|"
                  r"minority|majority|stake|recapital|partner)")


def cdx(url):
    body, code = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?url={url}&output=json"
                              f"&fl=timestamp,original&filter=statuscode:200&collapse=urlkey&limit=20000")
    if code != "200":
        sys.exit(f"CDX failed {url}: {code}")
    return json.loads(body or b"[]")[1:]


def text_of(html: str) -> str:
    h = re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>", " ", html)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", h).strip()


def main():
    rows = {}
    for pat in ("tcv.com/*", "tcv.com/news/*"):
        for ts, orig in cdx(pat):
            path = orig.split("tcv.com", 1)[-1].split("?")[0].lstrip(":80").rstrip("/")
            segs = [s for s in path.split("/") if s]
            if not segs:
                continue
            if segs[0] == "news" and len(segs) == 2 and segs[1] not in ("category", "tag", "page"):
                slug = segs[1]
            elif len(segs) == 1 and (segs[0].count("-") >= 4 or re.search(r"_ipo\.(html|pdf)$|funding\.html$", segs[0])):
                slug = segs[0]
            else:
                continue
            if not DEAL.search(slug):
                continue
            if slug in rows and rows[slug]["first_capture"] <= ts:
                continue
            rows[slug] = {"slug": slug, "url": orig, "first_capture": ts,
                          "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                          "round_words": sorted(set(ROUND.findall(slug)))}
    if "--bodies" in sys.argv:
        BODIES.mkdir(parents=True, exist_ok=True)
        for r in rows.values():
            if r["slug"].endswith(".pdf"):
                continue
            dest = BODIES / (re.sub(r"[^a-z0-9-]+", "-", r["slug"].lower())[:150] + ".txt")
            if not dest.exists():
                body, code = ia_fetch.get(f"https://web.archive.org/web/{r['first_capture']}id_/{r['url']}")
                if code != "200" or not body:
                    print("  body failed", r["slug"], code)
                    continue
                dest.write_text(text_of(body.decode("utf-8", "replace")))
            t = dest.read_text()
            m = re.search(r"(?i)(?:\(|\b)(?:PRNewswire|Business Wire|GLOBE NEWSWIRE|MARKETWIRE|/PRNewswire/)", t)
            r["body_text"] = t[max(0, (m.start() - 200) if m else 0):][:1500]
    OUT.write_text(json.dumps({
        "_readme": __doc__.strip(),
        "rows": sorted(rows.values(), key=lambda r: r["first_capture"])}, indent=1, ensure_ascii=False))
    print(len(rows), "deal posts;", sum(1 for r in rows.values() if r.get("body_text")), "with a body")


if __name__ == "__main__":
    main()
