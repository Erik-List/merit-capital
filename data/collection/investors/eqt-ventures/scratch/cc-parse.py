#!/usr/bin/env python3
"""Parse Common Crawl captures of eqtventures.com into the archive layer
(sources/wayback/parsed/<year>.json), one row per company per capture year.

Generations read (the markup of each was checked by hand 2026-09-27):
  /companies/           2020-2021  cards: Company name / Description / Stage /
                                   Geography / Industry / Announcement date
  /portfolio            2021-2024  anchors /company/<slug>: name + date
  /company/<slug>       2021-2025  Company Name / Industry / Website /
                                   Description / Geography / Announcement
                                   date / Status (Exit)
  / (home)              2020-2025  anchors to /company/<slug> or #company-<slug>
Older generations (2016-2019) are added as their captures arrive.

The "Announcement date" (2020-2025; "Signing/Closing Date" on the 2017-2018
cards, the firm's own deal-close date) is the firm's own publication date of the deal, an
anchor for first_seen (invest_year), never a round. A date shared by many
pages in one capture set is a build placeholder ("Jul. 21 2021" on the
2021-08 per-company pages) and is dropped. The card "Stage" field (Start-up,
Scale-up) describes the company, not a round, and is kept as evidence only.
Every row cites its own capture (capture_url, the index.commoncrawl.org form).
"""
import html as H, json, re, sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "eqt-ventures"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
OUT = HERE.parent / "sources" / "wayback" / "parsed"
man = json.loads(MAN.read_text())

def text_lines(h):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    return [l.strip() for l in t.split("\n") if l.strip()]

def pdate(s):
    s = (s or "").replace("Sept.", "Sep.").replace(".", "").strip()
    for f in ("%b %d %Y", "%B %d %Y"):
        try:
            return datetime.strptime(s, f).date().isoformat()
        except ValueError:
            pass
    return None

def slug_norm(s):
    from urllib.parse import unquote
    import unicodedata
    s = unicodedata.normalize("NFKD", unquote(H.unescape(s))).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def field(L, label):
    for i, l in enumerate(L):
        if re.fullmatch(rf"{label}\s*:", l, re.I) and i + 1 < len(L):
            return L[i + 1]
    return None

rows = defaultdict(list)          # year -> rows
def add(v, **r):
    y = v["timestamp"][:4]
    r.update(snapshot_ts=v["timestamp"], capture_url=v["capture_url"], surface=f"commoncrawl:{v['crawl']}")
    rows[y].append(r)

for k, v in sorted(man.items()):
    if v["status"] != "ok":
        continue
    u = re.sub(r"^https?://(www\.)?", "", v["url"]).rstrip("/")
    try:
        h = (RAW / k).read_bytes().decode("utf-8", "replace")
    except FileNotFoundError:
        continue
    m = re.fullmatch(r"eqtventures\.com/company/([^/?#]+)", u)
    if m:
        L = text_lines(h)
        name = field(L, "Company Name")
        if not name:
            continue
        add(v, name=name, slug=slug_norm(m.group(1)), path=f"/company/{m.group(1)}",
            website=field(L, "Website"), description=field(L, "Description"),
            industry=field(L, "Industry"), geography=field(L, "Geography"),
            announced_text=field(L, "Announcement date"),
            status_site=(field(L, "Status") or "").lower() or None, kind="company_page")
        continue
    if u == "eqtventures.com/portfolio":
        for a in re.finditer(r'<a[^>]+href="/company/([^"#?]+)"[^>]*>(.*?)</a>', h, re.S):
            L = text_lines(a.group(2))
            if not L:
                continue
            ds = [x for x in L if pdate(x)]
            nm = [x for x in L if not pdate(x) and x != "•"]
            if not nm:
                continue
            add(v, name=nm[0], slug=slug_norm(a.group(1)), path="/portfolio",
                announced_text=ds[0] if ds else None, kind="portfolio_listing")
        continue
    if u == "eqtventures.com/companies":
        for blk in re.split(r'(?=<[^>]+id="company-)', h)[1:]:
            sm = re.match(r'<[^>]+id="company-([^"]+)"', blk)
            L = text_lines(blk[:20000])
            name = field(L, "Company name")
            if not (sm and name):
                continue
            add(v, name=name, slug=slug_norm(sm.group(1)), path="/companies",
                description=field(L, "Description"), stage_site=field(L, "Stage"),
                geography=field(L, "Geography"), industry=field(L, "Industry"),
                announced_text=field(L, "Announcement date") or field(L, "Signing/Closing Date"),
                closing_date=bool(field(L, "Signing/Closing Date")), kind="companies_cards")
        continue
    if u == "eqtventures.com":
        for s in sorted(set(re.findall(r'href="/(?:company/|companies/#company-)([^"#?]+)"', h))):
            add(v, name=None, slug=slug_norm(s), path="/", kind="home_link")

# placeholder dates: one date on many rows of one capture set
for y, rs in rows.items():
    per_ts = defaultdict(Counter)
    for r in rs:
        if r.get("announced_text"):
            per_ts[(r["surface"], r["kind"])][r["announced_text"]] += 1
    for r in rs:
        at = r.get("announced_text")
        if not at:
            continue
        n = per_ts[(r["surface"], r["kind"])][at]
        if r["kind"] == "company_page" and n >= 8:
            r["announced_placeholder"] = True
            continue
        d = pdate(at)
        if d:
            r["announced"] = d
            r["invest_year"] = d[:4]

OUT.mkdir(parents=True, exist_ok=True)
for y, rs in sorted(rows.items()):
    # one row per slug+path per year: keep the latest capture
    best = {}
    for r in sorted(rs, key=lambda r: r["snapshot_ts"]):
        best[(r["slug"], r["path"])] = r
    write_atomic(OUT / f"{y}.json", json.dumps(sorted(best.values(), key=lambda r: (r["slug"], r["path"])),
                                                indent=1, ensure_ascii=False))
    print(y, len(best), "rows", len({r["slug"] for r in best.values()}), "slugs",
          Counter(r["kind"] for r in best.values()))
