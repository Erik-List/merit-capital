#!/usr/bin/env python3
"""Index Speedinvest's own posts by the base rows they name (adapted from
Project A PRO-102): the live /knowledge/<slug> posts (2019-2026,
sources/site/knowledge-posts.json) plus the old WordPress blog and pages
(2012-2020, /blog/<slug>/ and root-level posts captured by Common Crawl, and by
the Internet Archive once pulled).

Writes sources/site/press-archive.json: {post_key: {title, date, capture_url,
original_url, text, companies: [base slugs]}}. The judge reads it as the firm's
own announcement layer: class 1 for the round a post NAMES (COLLECTION.md s6:
an announcement asserts an entry only where the post says so in words).
"""
import html as H
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

CC_RAW = ROOT / "data" / "filings" / "commoncrawl" / "speedinvest"
IA_RAW = ROOT / "data" / "filings" / "wayback" / "speedinvest"
MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                      "september", "october", "november", "december"], 1)}
MONTHS.update({m[:3]: i for m, i in list(MONTHS.items())})
MONTHS.update({"sept": 9, "januar": 1, "februar": 2, "märz": 3, "mai": 5, "juni": 6, "juli": 7, "oktober": 10,
               "dezember": 12})
NOT_POST = re.compile(r"^/(team|portfolio|jobs?|job_[a-z]+|jobs_us|contact|imprint|privacy|site-notice|newsletter|idea|approach|"
                      r"offices?(-[a-z-]+)?|office-[a-z-]+|apply|press|platform|remember|fintech|deeptech|industrial-tech|"
                      r"network-effects|digitalhealth-consumertech|esports|internship|team-2|blog|robots\.txt)/?$")


def text_of(body: str) -> str:
    m = re.search(r"<main.*?</main>|<article.*?</article>", body, re.S)
    s = m.group(0) if m else body
    s = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|<footer.*?</footer>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", H.unescape(s)).strip()


def date_of(t: str) -> str:
    m = re.search(r"\b([A-Za-z]+) (\d{1,2}),? (20\d\d)\b", t)
    if m and m.group(1).lower() in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(1).lower()]:02d}-{int(m.group(2)):02d}"
    m = re.search(r"\b(\d{1,2})\.(\d{1,2})\.(20\d\d)\b", t)
    if m:
        return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
    m = re.search(r"\b(\d{1,2})\.? ([A-Za-zä]+) (20\d\d)\b", t)
    if m and m.group(2).lower() in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    return ""


# One-word names that are ordinary words: never auto-indexed (the judge searches
# the posts for them by hand, with the product or city).
COMMON = {"open", "ahead", "blocks", "due", "well", "june", "drop", "fuse", "grace", "genie", "ray", "tower",
          "ultimate", "paradox", "primer", "rainbow", "juno", "juli", "nook", "rive", "haz", "opus", "pace",
          "speedinvest", "facility", "crate", "grin", "loot", "katch", "keyper", "kema", "flank", "fasset",
          "anda", "agon", "ambio", "colorful", "conundrum", "diligent", "eunice", "impala", "jumba", "kwest",
          "mundi", "nomos", "onepot", "onit", "orbital", "platypus", "polaron", "precium", "ralph", "riverse",
          "rivia", "rollee", "seafair", "second nature", "smiler", "sota", "spice labs", "the lowdown",
          "unweave", "vitt", "revio", "kevin", "medicus", "morgana", "pikd", "koin", "juno", "gustav", "sunlight",
          "stateless", "ultimate", "tulyp", "rival", "raus"}


def names_of(base):
    out = {}
    for r in base:
        if r["name"].lower() in COMMON:
            continue
        n = r["name"]
        alts = {n, re.sub(r"(?i)\s*(gmbh|inc\.?|ltd\.?|ag|llc)$", "", n).strip()}
        out[r["slug"]] = [a for a in alts if len(a) >= 3]
    return out


def find(names, t):
    return sorted({s for s, alts in names.items()
                   if any(re.search(rf"(?<![A-Za-z0-9]){re.escape(a)}(?![A-Za-z0-9])", t,
                                    0 if (len(a) <= 4 or a.lower() == a) else re.I) for a in alts)})


def main():
    base = json.loads((INV / "companies/base.json").read_text())
    names = names_of(base)
    posts = {}
    for a in json.loads((INV / "sources/site/knowledge-posts.json").read_text())["rows"]:
        if a.get("status") == "FAILED":
            continue
        t = (a.get("title") or "") + " " + (a.get("body") or "")
        posts["k:" + a["slug"]] = {"title": a.get("title"), "date": a.get("date") or "", "capture_url": a["url"],
                                    "original_url": a["url"], "text": (a.get("body") or "")[:8000],
                                    "companies": find(names, t)}
    for raw, man in ((CC_RAW, INV / "sources/wayback/cc-manifest.json"), (IA_RAW, INV / "sources/wayback/ia-manifest.json")):
        if not man.exists():
            continue
        for key, m in sorted(json.loads(man.read_text()).items()):
            if m.get("status") != "ok":
                continue
            path = re.sub(r"^https?://(www\.)?speedinvest\.com(:\d+)?", "", m["url"]).split("?")[0]
            if not (re.fullmatch(r"/blog/[^/]+/?", path) or re.fullmatch(r"/[a-z0-9_-]+/?", path)) or NOT_POST.match(path):
                continue
            if int(m["timestamp"][:4]) > 2020 and not re.fullmatch(r"/blog/[^/]+/?", path):
                continue   # after 2020 only the firm's /blog/<post> pages are posts (the 2021-2023 site)
            f = raw / key
            if not f.exists():
                continue
            body = f.read_text(errors="replace")
            if re.search(r'class="[^"]*team-member|/team/', path):
                continue
            t = text_of(body)
            title = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S) or re.search(r"<title>(.*?)</title>", body, re.S)
            title = text_of(title.group(1)) if title else path
            post = path.strip("/").split("/")[-1]
            if ("wp:" + post) in posts:
                continue
            posts["wp:" + post] = {"title": title, "date": date_of(t[:1500]) or date_of(t), "capture_url": m.get("capture_url"),
                                   "original_url": m["url"], "capture_ts": m["timestamp"], "text": t[:8000],
                                   "companies": find(names, title + " " + t[:8000])}
    write_atomic(INV / "sources/site/press-archive.json", json.dumps(
        {"_readme": __doc__.strip().splitlines()[0], "posts": posts}, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for p in posts.values() if p["companies"])
    print(f"{len(posts)} posts, {n} naming a base row")


if __name__ == "__main__":
    main()
