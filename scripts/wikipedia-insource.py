#!/usr/bin/env python3
"""Wikipedia insource sweep — a company-side recall layer (COLLECTION.md §5).

Searches English Wikipedia for articles whose source mentions the investor
(insource:"<phrase>"), fetches each article's wikitext and keeps the
sentences that mention the phrase, so the judge can see "raised a Series B
led by <investor>" next to the article's own references. Company articles
(an {{Infobox company}} or similar) are separated from people, lists and
other pages; every title is matched against the investor's base and
excluded rows so only new candidates need a verdict.

Usage: python3 scripts/wikipedia-insource.py <slug>
Config: wikipedia.phrases (default: the investor name)
Output: sources/web/wikipedia-insource.json
"""
import csv, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

UA = "merit-capital research (erik@meritcapit.al) python-urllib"
ROOT = Path(__file__).resolve().parent.parent
API = "https://en.wikipedia.org/w/api.php"


def api(**params):
    import subprocess
    params |= {"format": "json"}
    url = API + "?" + urllib.parse.urlencode(params)
    r = subprocess.run(["curl", "-s", "-m", "60", "-A", UA, url], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise RuntimeError(f"curl rc={r.returncode} for {url}")
    data = json.loads(r.stdout)
    time.sleep(0.3)
    return data


def loose(n):
    n = n.lower()
    n = re.sub(r"\(.*?\)", "", n)
    n = re.sub(r"\b(inc|labs|the|company|technologies|corporation|corp|ltd|llc|health|software)\b", "", n)
    return re.sub(r"[^a-z0-9]", "", n)


def sentences(text, phrase_re):
    text = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", text, flags=re.S)
    text = re.sub(r"\[\[([^|\]]*\|)?([^\]]*)\]\]", r"\2", text)
    text = re.sub(r"'{2,}", "", text)
    text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    text = re.sub(r"\s+", " ", text)
    out = []
    for m in phrase_re.finditer(text):
        s = text.rfind(". ", 0, m.start()); e = text.find(". ", m.end())
        out.append(text[(s + 2 if s >= 0 else max(0, m.start() - 240)): (e + 1 if e >= 0 else m.end() + 240)].strip())
    return out[:4]


def main():
    slug = sys.argv[1]
    inv = ROOT / "data/collection/investors" / slug
    cfg = json.load(open(inv / "config.json"))
    phrases = (cfg.get("wikipedia") or {}).get("phrases") or [cfg.get("name") or slug.replace("-", " ").title()]
    phrase_re = re.compile("|".join(re.escape(p) for p in phrases), re.I)

    base = {loose(r["name"]): r["slug"] for r in json.load(open(inv / "base.json"))}
    for r in json.load(open(inv / "base.json")):
        for u in filter(None, [r.get("site_url")]):
            base[loose(re.sub(r"^https?://(www\.)?|\..*$", "", u))] = r["slug"]
    excluded = {}
    if (inv / "excluded.csv").exists():
        for r in csv.DictReader(open(inv / "excluded.csv")):
            excluded[loose(r["name"])] = r["slug"]

    titles = {}
    for phrase in phrases:
        off = 0
        while True:
            j = api(action="query", list="search", srsearch=f'insource:"{phrase}"', srlimit=500, sroffset=off, srnamespace=0)
            hits = j["query"]["search"]
            for h in hits:
                titles[h["title"]] = h["pageid"]
            print(f"{phrase!r}: total {j['query']['searchinfo']['totalhits']}, got {len(hits)} at offset {off}")
            if "continue" not in j or not hits:
                break
            off = j["continue"]["sroffset"]

    rows = []
    for title, pid in sorted(titles.items()):
        j = api(action="query", prop="revisions|categories", rvprop="content", rvslots="main", pageids=pid, cllimit=50)
        page = j["query"]["pages"][str(pid)]
        text = page.get("revisions", [{}])[0].get("slots", {}).get("main", {}).get("*", "")
        cats = [c["title"].replace("Category:", "") for c in page.get("categories", [])]
        infobox = re.search(r"\{\{\s*Infobox\s+([A-Za-z ]+)", text)
        kind = (infobox.group(1).strip().lower() if infobox else "none")
        is_company = kind in ("company", "dot-com company", "website", "organization", "software", "video game company", "airline", "bank", "cryptocurrency")
        k = loose(title)
        rows.append({"title": title, "pageid": pid, "url": "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
                     "infobox": kind, "is_company": is_company, "in_base": base.get(k), "in_excluded": excluded.get(k),
                     "categories": cats[:8], "sentences": sentences(text, phrase_re)})
        tag = "base" if base.get(k) else ("excl" if excluded.get(k) else ("CAND" if is_company else "other"))
        print(f"  {tag:5} {title[:40]:40} [{kind}] {(rows[-1]['sentences'] or [''])[0][:110]}")

    out = inv / "sources/web/wikipedia-insource.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    json.dump({"_readme": "Wikipedia insource sweep (scripts/wikipedia-insource.py): every article whose source "
                          "mentions the configured phrases, with the sentences that mention it; is_company from the "
                          "infobox; in_base/in_excluded resolved against the investor's rows. Candidates = company "
                          "articles not in the base; the judge cites the article and its underlying reference.",
               "phrases": phrases, "swept_at": time.strftime("%Y-%m-%d"), "articles": rows},
              open(out, "w"), indent=2, ensure_ascii=False)
    print(f"wrote {out.relative_to(ROOT)}: {len(rows)} articles, "
          f"{sum(1 for r in rows if r['in_base'])} in base, {sum(1 for r in rows if r['is_company'] and not r['in_base'] and not r['in_excluded'])} company candidates")


if __name__ == "__main__":
    main()
