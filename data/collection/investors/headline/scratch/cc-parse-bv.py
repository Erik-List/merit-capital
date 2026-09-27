"""Parse the Common Crawl captures of bvcapital.com (BV Capital, 2008-2012) into
sources/wayback/parsed/<year>.json, the archive layer's shape, one row per
company per capture year, citing the capture (index.commoncrawl.org form).

Surfaces: the /portfolio/ listing (anchor text per company), the per-company
pages /portfolio/show/<slug> (the <title> / <h1> carries the name) and the
2012 WordPress site. An exit carries its acquirer or ticker in parentheses on
the listing ("Fotolog (HIMD.PA)", "Rojo (Six Apart)"): the company is the name
before the parenthesis, and the parenthesis goes to the row's description.
Raw captures: data/filings/commoncrawl/headline/bvcapital.com/ (gitignored),
manifest sources/wayback/cc-manifest-bvcapital.com.json."""
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parents[3] / "scripts"))
from paths import write_atomic  # noqa: E402

RAW = HERE.parents[3] / "data" / "filings" / "commoncrawl" / "headline" / "bvcapital.com"
MAN = json.loads((HERE / "sources" / "wayback" / "cc-manifest-bvcapital.com.json").read_text())
OUT = HERE / "sources" / "wayback" / "parsed"
OUT.mkdir(parents=True, exist_ok=True)


def slug_of(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def clean(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


JUNK = {"portfolio", "application error", "bv capital", "team", "news", ""}
by_year = {}
for key, m in MAN.items():
    if m.get("status") != "ok":
        continue
    body = (RAW / key).read_bytes().decode("utf-8", "replace")
    path = re.sub(r"https?://(www\.)?bvcapital\.com", "", m["url"]).split("?")[0]
    year = int(m["timestamp"][:4])
    rows = []
    if re.match(r"^/portfolio/?$", path):
        for href, inner in re.findall(r'<a[^>]+href="([^"]*portfolio/show/[^"]+)"[^>]*>(.*?)</a>', body, re.S):
            name = clean(inner)
            if not name:
                continue
            site_slug = href.rstrip("/").split("/")[-1]
            rows.append((name, site_slug, "/portfolio"))
    elif path.startswith("/portfolio/show/"):
        site_slug = path.rstrip("/").split("/")[-1]
        t = re.search(r"<title>(.*?)</title>", body, re.S)
        h = re.search(r"<h[12][^>]*>(.*?)</h[12]>", body, re.S)
        name = clean(h.group(1)) if h else ""
        if name.lower() in JUNK:
            name = ""
        if not name and t:
            name = clean(t.group(1)).split("|")[0].replace("BV Capital", "").strip(" -:")
        if name and name.lower() not in JUNK and "error" not in name.lower():
            rows.append((name, site_slug, "/portfolio/show/" + site_slug))
    for name, site_slug, p in rows:
        mm = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", name)
        desc = ""
        if mm:
            name, desc = mm.group(1).strip(), f"exit: {mm.group(2)}"
        by_year.setdefault(year, {})[(slug_of(name), p)] = {
            "name": name, "site_slug": site_slug, "description": desc,
            "slug": slug_of(name), "path": p, "snapshot_ts": m["timestamp"],
            "capture_url": m["capture_url"], "surface": f"commoncrawl:{m['crawl']}"}

for year, rows in sorted(by_year.items()):
    f = OUT / f"{year}.json"
    old = {(r["slug"], r["path"]): r for r in json.loads(f.read_text())} if f.exists() else {}
    old.update(rows)                   # parsed year files merge, keyed slug+path (COLLECTION.md s5)
    write_atomic(f, json.dumps(sorted(old.values(), key=lambda r: (r["slug"], r["path"])), indent=1) + "\n")
    names = sorted({r["name"] for r in rows.values()})
    print(year, len(names), names)
