#!/usr/bin/env python3
"""Build sources/wayback/partner-roster.json for Index Ventures from the firm's
own team pages, one entry per person with the years seen and a dated basis.

Sources, all the firm's own site:
  - Common Crawl captures of /team (listing) and /team/<slug> (person page),
    2008-2025 (sources/wayback/cc-manifest.json):
      2008-2013 PHP    the listing groups people as Technology / Life Sciences /
                       Operations, by office;
      2014-2019 Drupal a flat listing (name per card);
      2020-2025 Wagtail cards with data-role (investor / operator / strategist).
  - the live team page 2026 (sources/site/team-cards.json).
  - the firm's own "Index Team" attributions on archived and live company pages
    (sources/wayback/archive-facts.json, sources/site/companies-wagtail.json):
    a person the firm names as the Index Team member of a company is an
    investor in that year, whatever the listing says.

`investing` is true when any source classes the person as an investor (PHP
Technology group; data-role investor; an Index Team attribution). The PHP Life
Sciences group is `desk: life` (decisions.md D3): kept in the roster for seat
dating, not swept (investing false). Operations staff are kept with investing
false. Only investing entries are written to the roster the Form D sweep reads;
everyone else goes to sources/wayback/staff.json.
"""
import html as H
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

def read_raw(f):
    """Raw captures are gzipped on disk (2026-10-01: the machine ran out of space mid-run)."""
    import gzip
    g = Path(str(f) + ".gz")
    if g.exists():
        return gzip.open(g, "rt", errors="replace").read()
    return f.read_text(errors="replace") if f.exists() else None


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]
CCRAW = REPO / "data" / "filings" / "commoncrawl" / "index-ventures"
WB = ROOT / "sources" / "wayback"


def slug_of(name):
    n = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")


def clean(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s)).replace("\xa0", " ")).strip()


people = defaultdict(lambda: {"years": set(), "groups": defaultdict(set), "caps": {}, "names": set(), "titles": {}})


def see(name, year, group, cap, title=None):
    name = clean(name)
    if not name or len(name.split()) < 2 or len(name) > 40:
        return
    k = slug_of(name)
    p = people[k]
    p["names"].add(name)
    p["years"].add(year)
    if group:
        p["groups"][group].add(year)
    p["caps"].setdefault(year, cap)
    if title:
        p["titles"][year] = title


man = json.loads((WB / "cc-manifest.json").read_text())
for key, v in sorted(man.items()):
    if v.get("status") != "ok":
        continue
    path = re.sub(r"https?://(www\.)?indexventures\.com(:80|:443)?", "", v["url"], flags=re.I).split("?")[0]
    path = re.sub(r"^/index\.php", "", path)
    if not path.startswith("/team"):
        continue
    f = CCRAW / key
    body = read_raw(f)
    if body is None:
        continue
    year = int(v["timestamp"][:4]); cap = v["capture_url"]
    if 'class="profile"' in body:                                  # PHP 2008-2013: grouped listing on every team page
        group = None
        for m in re.finditer(r'class="industry"[^>]*>(.*?)</a>|class="(profiletype)"[^>]*>\s*Operations|class="profile">(.*?)</a>|<h3[^>]*>\s*(Operations)\s*</h3>', body, flags=re.S):
            if m.group(1):
                g = clean(m.group(1)).lower()
                group = "tech" if g.startswith("tech") else "life" if g.startswith("life") else "operations" if g.startswith("oper") else g
            elif m.group(2) or m.group(4):
                group = "operations"
            elif m.group(3) and group:
                see(m.group(3), year, group, cap)
        continue
    if re.fullmatch(r"/team/?", path):
        # Wagtail 2020-: cards with data-role
        cards = re.findall(r'<a\s+class="team-member js-team-member[^"]*"\s+href="/team/([^"/]+)/?"\s+data-name="[^"]*"\s+data-sectors="[^"]*"\s+data-location="([^"]*)"\s+data-role="([^"]*)"\s*>(.*?)</a>', body, flags=re.S)
        for slug, loc, role, inner in cards:
            see(clean(inner), year, {"investor": "investor"}.get(role, role), cap)
        # Drupal 2014-2019
        for slug, inner in re.findall(r'<a href="/team/([^"]+)"[^>]*>(.*?)</a>', body, flags=re.S):
            nm = re.search(r'<div class="field-content name">(.*?)</div>', inner, flags=re.S) or \
                 re.search(r'<span itemprop="name">(.*?)</span>', inner, flags=re.S)
            if nm:
                see(nm.group(1), year, None, cap)
        continue
    m = re.fullmatch(r"/team/([^/]+)/?", path)
    if m and m.group(1) not in ("index",):
        t = re.search(r"<title>(.*?)</title>", body, flags=re.S)
        title = clean(t.group(1)) if t else ""
        name = re.split(r"\s+\|\s+", title)[0].strip()
        name = re.sub(r"^Index Ventures\s*[|:]\s*", "", name)
        if not name or re.search(r"not found|^team$|index ventures", name, flags=re.I):
            continue
        jt = re.search(r'class="[^"]*job-title[^"]*">(.*?)</', body, flags=re.S)
        see(name, year, None, cap, clean(jt.group(1)) if jt and clean(jt.group(1)) else None)

# the firm's own Index Team attributions
KNOWN = None
facts = json.loads((WB / "archive-facts.json").read_text()).get("cc", {})
attributions = defaultdict(set)       # slug -> years named as Index Team
raw_attr = []
for k, v in facts.items():
    for e in v.get("partners", []):
        for nm in e["value"]:
            raw_attr.append((nm, int(e["ts"][:4]), e["capture_url"]))
live = json.loads((ROOT / "sources" / "site" / "companies-wagtail.json").read_text())["rows"]
for r in live:
    for nm in r.get("partners", []):
        raw_attr.append((nm, 2026, r["url"]))
names_by_len = None
# a Wagtail capture can run two names together ("Damir Becirovic Danny Rimer"): split on the names already known
all_names = sorted({n for p in people.values() for n in p["names"]}, key=len, reverse=True)
for nm, year, cap in raw_attr:
    nm = clean(nm)
    parts = []
    rest = nm
    for n in all_names:
        if n in rest:
            parts.append(n); rest = rest.replace(n, " ")
    if rest.strip() and len(rest.split()) >= 2:
        parts.append(rest.strip())
    for p in parts or [nm]:
        k = slug_of(p)
        attributions[k].add(year)
        if k not in people:
            see(p, year, None, cap)
        people[k]["groups"]["index_team"].add(year)
        people[k]["years"].add(year)
        people[k]["caps"].setdefault(year, cap)

# live team 2026
for r in json.loads((ROOT / "sources" / "site" / "team-cards.json").read_text())["rows"]:
    see(r["name"], 2026, r["group"], r["url"])

# Life Sciences team members the 2014-2015 flat listing does not group (decisions.md D3): named by the firm
# as the Index Team only on Life Sciences companies; David Grainger joined the life sciences practice in 2012.
LIFE_TEAM = {"david-grainger"}
roster, staff = [], []
for k, p in sorted(people.items()):
    years = sorted(p["years"])
    g = {a: sorted(b) for a, b in p["groups"].items()}
    investing = bool(g.get("tech") or g.get("investor") or g.get("index_team"))
    life = (bool(g.get("life")) and not (g.get("tech") or g.get("investor"))) or k in LIFE_TEAM
    name = sorted(p["names"], key=lambda n: (-len(n), n))[0]
    basis = []
    for label, key in (("Technology group on the team page", "tech"), ("Life Sciences group on the team page", "life"),
                       ("Operations group on the team page", "operations"), ("data-role investor on the team page", "investor"),
                       ("data-role operator", "operator"), ("data-role strategist", "strategist"),
                       ("named as Index Team on a company page", "index_team")):
        if g.get(key):
            basis.append(f"{label} {g[key][0]}-{g[key][-1]}" if g[key][0] != g[key][-1] else f"{label} {g[key][0]}")
    e = {"slug": k, "name": name, "years_seen": years, "first_seen": years[0], "last_seen": years[-1],
         "snapshots": len(years), "sources": ["commoncrawl-team-pages"] + (["site-team"] if 2026 in years else []),
         "basis": "; ".join(basis) or "team page captured " + f"{years[0]}-{years[-1]}",
         "first_capture": p["caps"][years[0]], "investing": investing and not life}
    if life:
        e["desk"] = "life"
    if p["titles"]:
        e["titles"] = {str(y): t for y, t in sorted(p["titles"].items())}
    (roster if e["investing"] else staff).append(e)

(WB / "partner-roster.json").write_text(json.dumps(roster, indent=1, ensure_ascii=False) + "\n")
(WB / "staff.json").write_text(json.dumps(staff, indent=1, ensure_ascii=False) + "\n")
print(len(roster), "investing;", len(staff), "life desk / operations / unclassified")
for e in roster:
    print(f"  {e['first_seen']}-{e['last_seen']} {e['name']:28s} {e['basis'][:110]}")
print("-- not swept")
for e in staff:
    print(f"  {e['first_seen']}-{e['last_seen']} {e['name']:28s} {e.get('desk','')} {e['basis'][:90]}")
