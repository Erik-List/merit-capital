#!/usr/bin/env python3
"""BCV's historical people, with titles and capture-year windows, from Common Crawl
(scratch/cc-index-raw.json + the fetched bodies in data/filings/commoncrawl/bain-capital-ventures/).

  2009-10  /OurTeam/TeamMember.aspx?id=N: every page's left nav lists the whole "Senior
           Professionals" roster; the body gives the member's name and title
  2012-15  /your-team/member/<slug>: title and office ("| Your Team | Associate, | Boston |"); the
           nav of every 2012-13 page lists the whole team
  2015-26  /team/<slug>/: "Name | TITLE | Office"
Years seen = the capture years of the person's own page in every crawl, unioned with the years a
nav list named them. Output scratch/roster-cc.json in partner-roster.py's shape plus `title`.
Usage: python3 cc-roster.py
"""
import html, json, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "bain-capital-ventures"
man = json.loads((HERE.parent / "sources" / "wayback" / "cc-manifest.json").read_text())
idx = json.loads((HERE / "cc-index-raw.json").read_text())
DOM = re.compile(r"https?://(www\.)?baincapitalventures\.com(:\d+)?", re.I)
NOT_PEOPLE = {"team", "member", "all", "category", "location", "6772", "ai-fellows", "discover-fellows",
              "labs-fellows", "research-fellows"}


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def slug_of(name):
    s = re.sub(r"\b(j\.|mr\.|ms\.)\s*", "", name.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def text(t):
    x = html.unescape(re.sub(r"<[^>]+>", " | ", re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S | re.I)))
    return re.sub(r"(\s*\|\s*)+", " | ", x)


people = defaultdict(lambda: {"names": set(), "years": set(), "titles": {}, "sources": set(), "joined": set()})
JOINED = re.compile(r"(?:joined|joining)\s+(?:Bain Capital Ventures|Bain Capital|BCV|the firm)[^.]{0,40}?\bin\s+((?:19|20)\d\d)", re.I)


def add(name, year, source, title=None, bio=""):
    name = re.sub(r"\s+", " ", name).strip()
    if not name or len(name) > 40 or not re.search(r"[a-z]", name):
        return
    s = slug_of(name)
    if s in NOT_PEOPLE or "-" not in s:
        return
    p = people[s]
    p["names"].add(name)
    p["years"].add(int(year))
    p["sources"].add(source)
    if title:
        p["titles"][int(year)] = title
    for y in JOINED.findall(bio or ""):
        p["joined"].add(int(y))


for k, v in man.items():
    if v["status"] != "ok":
        continue
    path, year = v["path"], v["timestamp"][:4]
    t = (RAW / k).read_bytes().decode("utf-8", "replace")
    x = text(t)
    if re.match(r"(?i)^/ourteam/teammember\.aspx", path):
        m = re.search(r"Senior Professionals \|(.*?)\| (?:Experience|Education)", x)
        if m:
            seg = [s.strip() for s in m.group(1).split("|") if s.strip()]
            # nav names, then the member's own name and title just before "Experience"
            name, title = (seg[-2], seg[-1]) if len(seg) >= 2 else (None, None)
            for n in seg[:-2]:
                add(n, year, "nav2010")
            if name:
                add(name, year, "page2010", title, bio=x)
    elif re.match(r"(?i)^/your-team/member/", path):
        slug = path.rstrip("/").rsplit("/", 1)[-1]
        m = re.search(r'<section id="bYourTeamDetail".*?<h2>\s*([^<]{3,60}?),?\s*<', t, re.S)
        h1 = re.search(r'<section id="bYourTeamDetail".*?<h1>(.*?)</h1>', t, re.S)
        name = clean(h1.group(1)) if h1 and clean(h1.group(1)).lower() not in ("your team",) else slug.replace("-", " ").title()
        add(name, year, "page2012", m.group(1).strip().rstrip(",") if m else None, bio=x)
    elif re.match(r"(?i)^/team/[^/]+/?$", path):
        ti = re.search(r"<title>(.*?)</title>", t, re.S)
        nm = re.sub(r"\s*[-–|].*$", "", clean(ti.group(1))) if ti else ""
        # three layouts: 2016-17 "Name | TITLE | Office"; 2018-21 <div class="row-one"><h2>Name</h2>
        # <ul><li>Title</li><li>Office</li>; 2022+ <div class="positions"> Title </div>
        m = (re.search(r'<div class="row-one">\s*<h2>[^<]*</h2>\s*<ul>\s*<li>([^<]{2,60})</li>', t)
             or re.search(r'<div class="positions">\s*([^<]{2,60}?)\s*</div>', t))
        m2 = re.search(r"\| ([A-Z][^|]{2,40}) \| ([A-Z][A-Z ,&'\-]{3,60}) \| ", x)
        title = clean(m.group(1)) if m else (m2.group(2).strip().title() if m2 and m2.group(1).strip() == nm else None)
        if nm and nm.lower() not in ("team", "page not found"):
            add(nm, year, "pagewp", title, bio=x)
    # every 2012-13 page's nav lists the team ("Your Team | A | B | ... | Pressroom")
    if year in ("2012", "2013"):
        m = re.search(r"\| Your Team \|(.*?)\| Pressroom \|", x)
        if m and m.group(1).count("|") > 10:
            for n in m.group(1).split("|"):
                add(n.strip(), year, "nav2012")

# capture years of each person's own page, all crawls
for cid, v in idx.items():
    for r in v.get("records", []):
        p = DOM.sub("", r["url"]).split("?")[0].rstrip("/")
        m = re.match(r"(?i)^/(?:your-team/member|team)/([a-z][a-z0-9_-]*)$", p)
        if m and m.group(1).lower() in people:
            people[m.group(1).lower()]["years"].add(int(r["timestamp"][:4]))
            people[m.group(1).lower()]["sources"].add("cc-index")

out = []
for s, p in sorted(people.items()):
    if p["joined"]:
        # the person's own bio dates the start; the capture years only bound it from below
        p["years"] |= set(range(min(p["joined"]), min(p["years"]) + 1))
    yrs = sorted(p["years"])
    titles = [p["titles"][y] for y in sorted(p["titles"])]
    out.append({"slug": s, "name": sorted(p["names"], key=len)[-1], "site_name": sorted(p["names"], key=len)[-1],
                "years_seen": yrs, "first_seen": yrs[0], "last_seen": yrs[-1], "snapshots": len(yrs),
                "title": titles[-1] if titles else "", "titles": sorted(set(titles)), "sources": sorted(p["sources"]),
                "joined_bio": min(p["joined"]) if p["joined"] else None})
write_atomic(HERE / "roster-cc.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(len(out), "people;", sum(1 for r in out if r["title"]), "with a title")
for r in out:
    print(f"  {r['name']:28s} {r['first_seen']}-{r['last_seen']}  {r['title'][:40]:40s} {','.join(r['sources'])}")
