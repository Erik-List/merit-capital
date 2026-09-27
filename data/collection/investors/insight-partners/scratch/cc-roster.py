#!/usr/bin/env python3
"""The firm's archived INVESTMENT TEAM, per year, from Common Crawl captures of its own team pages,
written in partner-roster.py's shape to scratch/roster-cdx.json (read by scratch/build-roster.py).

Only the investing department feeds the Form D sweep (config roster._note), so a person enters
only from a surface that marks the department:
  2010-09, 2012-02  /team/view/investment (the Investment Team list, one link per person)
  2012-05, 2014-03  /team.asp, /team/ (div.item.teamMember with class investment-team)
  2017-01, 2018-01  /team/ (li.staff-member with class investment-team)
  2018-12 .. 2022   /team/departments/investment-team (li.staff-member)
A person so marked also takes the years of their own /team/<slug> page captures (2017 on), which is
what dates a departure. Titles are kept; build-roster.py filters to seat-holding titles.
Usage: python3 cc-roster.py"""
import html, json, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
I = HERE.parent
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "insight-partners"
man = json.loads((I / "sources" / "wayback" / "cc-manifest.json").read_text())
idx = json.loads((HERE / "cc-index-raw.json").read_text())
DOM = re.compile(r"https?://(www\.)?insightpartners\.com(:\d+)?", re.I)


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


VARIANTS = {"brad-twohig": "bradley-twohig"}
# titles that hold board seats (build-roster.py's rule for the live team); people whose every
# archived title is junior (analyst, associate) stay out of the Form D sweep, where their common
# names buy only false matches; a person listed with no title at all is kept.
SEAT = re.compile(r"managing director|principal|vice president|^director|senior advisor|operating partner|co-founder|partner", re.I)


def slug_of(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return VARIANTS.get(s, s)


people = defaultdict(lambda: {"years": set(), "names": set(), "titles": {}, "sources": set()})
for k, v in man.items():
    b = (RAW / k).read_bytes().decode("utf-8", "replace")
    y = int(v["timestamp"][:4])
    p = v["path"].rstrip("/")
    found = []
    if p == "/team/view/investment":
        found = [(slug_of(clean(t)), clean(t), "") for _, t in re.findall(r'<a[^>]+href="[^"]*/team/view/investment/(\d+)"[^>]*>(.*?)</a>', b, re.S) if clean(t)]
    elif p in ("/team.asp", "/team") and "teamMember" in b:
        for sl, dept, rest in re.findall(r'<div id="([^"]+)" class="item teamMember clickable ([^"]*)"[^>]*>(.*?)(?=<div id="[^"]+" class="item teamMember|$)', b, re.S):
            if "investment-team" in dept.split():
                nm = re.search(r'<div class="name">(.*?)</div>', rest, re.S)
                ti = re.search(r'<div class="position">(.*?)</div>', rest, re.S)
                if nm:
                    found.append((sl, clean(nm.group(1)), clean(ti.group(1)) if ti else ""))
    elif p == "/team" and "staff-member" in b and "grid-item" in b:
        for cls, sl, rest in re.findall(r'<li class="grid-item filter-grid-item staff-member columns ([^"]*)">\s*<a href="[^"]*/team/([a-z0-9\-]+)/?">(.*?)</li>', b, re.S):
            if "investment-team" in cls.split():
                nm = re.search(r"<h6>(.*?)</h6>", rest, re.S)
                ti = re.search(r"<p class='small'>(.*?)</p>", rest, re.S)
                if nm:
                    found.append((sl, clean(nm.group(1)), clean(ti.group(1)) if ti else ""))
    elif p == "/team/departments/investment-team":
        for sl, rest in re.findall(r'<li class="staff-member[^"]*">\s*<a href="[^"]*/team/([a-z0-9\-]+)/?">(.*?)</li>', b, re.S):
            nm = re.search(r"<h2[^>]*>(.*?)</h2>", rest, re.S)
            ti = re.search(r'<p class="position[^"]*">(.*?)</p>', rest, re.S)
            if nm:
                found.append((sl, clean(nm.group(1)), clean(ti.group(1)) if ti else ""))
    if found:
        print(v["timestamp"][:8], p, len(found))
    for sl, nm, ti in found:
        key = slug_of(nm)
        e = people[key]
        e["years"].add(y); e["names"].add(nm); e["sources"].add(p)
        e["page_slugs"] = e.get("page_slugs", set()) | {sl}
        if ti:
            e["titles"][y] = ti

# own profile pages date the window (2017 on, /team/<slug>)
page_years = defaultdict(set)
for cid, v in idx.items():
    for r in v.get("records", []):
        m = re.match(r"^/team/([a-z0-9\-]+)/?$", DOM.sub("", r["url"]).split("?")[0])
        if m:
            page_years[m.group(1)].add(int(r["timestamp"][:4]))
for key, e in people.items():
    for sl in e.get("page_slugs", set()) | {key}:
        e["years"] |= page_years.get(sl, set())

out = []
dropped = []
for key, e in sorted(people.items()):
    if e["titles"] and not any(SEAT.search(t) for t in e["titles"].values()):
        dropped.append(key)
        continue
    yrs = sorted(e["years"])
    last_title = e["titles"][max(e["titles"])] if e["titles"] else ""
    out.append({"slug": key, "name": sorted(e["names"], key=len)[-1], "site_name": sorted(e["names"], key=len)[-1],
                "years_seen": yrs, "first_seen": yrs[0], "last_seen": yrs[-1], "snapshots": len(yrs),
                "titles": {str(y): t for y, t in sorted(e["titles"].items())}, "title": last_title,
                "sources": ["commoncrawl-team-pages"]})
write_atomic(HERE / "roster-cdx.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(len(out), "investment-team people with a seat title ->", HERE / "roster-cdx.json")
print(len(dropped), "left out (junior titles only):", ", ".join(dropped))
