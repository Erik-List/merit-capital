#!/usr/bin/env python3
"""The 1999-2006 partner roster, and the partners' own deal attributions.

partner-roster.py enumerates archived profile pages and requires a hyphen in
the slug ("first-last"), so Redpoint's first two people namespaces are
structurally invisible to it: /team/<lastname>.shtml (2000-2001) and the
index.htm CMS's numeric team pages (2002-2006). Those are exactly the years
the Form D roster sweep needs, because a seat is dated against the person's
firm at filing time (COLLECTION.md 1, T4).

The 2002-2006 bios are also a judge instrument in their own right: each
partner's page names the deals they led, and says which of them were done at
Brentwood or IVP BEFORE Redpoint existed — the evidence behind decisions.md D5.

Writes sources/wayback/partner-roster-early.json and merges the people into
sources/wayback/partner-roster.json (existing entries win, so a re-run of
partner-roster.py can be re-merged by re-running this).

Usage: python3 scratch/build-early-roster.py
"""
import json
import re
import subprocess
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import shared_throttle                              # noqa: E402
from paths import Paths, write_atomic               # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
P = Paths("redpoint-ventures")
OUT = P.wayback / "partner-roster-early.json"
CACHE = P.root / "scratch" / "team-pages"
TAGS = re.compile(r"<[^>]+>")


def text(h: str) -> str:
    return re.sub(r"\s+", " ", unescape(TAGS.sub(" ", h))).strip()


def get(url: str, year: int, key: str) -> tuple[str, str]:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{year}-{key}.html"
    if f.exists():
        return f.read_text(errors="replace"), (CACHE / f"{year}-{key}.ts").read_text().strip() \
            if (CACHE / f"{year}-{key}.ts").exists() else ""
    for probe in ("0615", "0201", "1015", "1101"):
        shared_throttle.wait("ia")
        r = subprocess.run(["curl", "-sL", "--max-time", "120", "-w", "\n%{url_effective}",
                            "-H", f"User-Agent: {UA}",
                            f"https://web.archive.org/web/{year}{probe}id_/{url}"],
                           capture_output=True, text=True, errors="replace")
        body, _, eff = (r.stdout or "").rpartition("\n")
        m = re.search(r"/web/(\d{14})id_/", eff)
        if m and m.group(1)[:4] == str(year) and len(body) > 1500:
            f.write_text(body)
            (CACHE / f"{year}-{key}.ts").write_text(m.group(1))
            return body, m.group(1)
    return "", ""


people: dict[str, dict] = {}


def add(name: str, year: int, slug: str, bio: str = "", role: str = "") -> None:
    name = re.sub(r"\s+", " ", name).strip()
    # the CMS page repeats the given name after the full name ("Tim Haley Tim")
    toks = name.split()
    while len(toks) > 2 and toks[-1] == toks[0]:
        toks.pop()
    name = " ".join(toks)
    if not name or len(name.split()) < 2:
        return
    key = name.lower()
    r = people.setdefault(key, {"slug": slug, "name": name, "years_seen": [],
                                "roles": [], "bio": "", "sources": ["early-era-team-page"]})
    if year not in r["years_seen"]:
        r["years_seen"].append(year)
    if role and role not in r["roles"]:
        r["roles"].append(role)
    if len(bio) > len(r["bio"]):
        r["bio"] = bio


# ---- 2000-2001: /team/default.shtml lists the partners, one page each
for y in (2000, 2001):
    html, ts = get("http://www.redpoint.com/team/default.shtml", y, "team-default")
    if not html:
        continue
    slugs = set(re.findall(r'href="([A-Za-z][A-Za-z0-9_]*)\.s?html?"', html))
    print(f"{y} /team/default.shtml: {len(slugs)} profile links")
    for s in sorted(slugs):
        if s.lower() in ("default", "index", "eir"):
            continue
        page, _ = get(f"http://www.redpoint.com/team/{s}.shtml", y, f"team-{s}")
        if not page:
            continue
        body = text(page)
        m = re.search(r"Redpoint Ventures\s*:?\s*(?:Team Member)?\s*([A-Z][a-z]+(?:\s+[A-Z][A-Za-z.'-]+){1,2})",
                      body)
        nm = m.group(1) if m else ""
        if not nm:
            m = re.search(r"([A-Z][a-z]+\s+[A-Z][A-Za-z.'-]+)\s+is\s+(?:a|the)\s", body)
            nm = m.group(1) if m else ""
        add(nm, y, s, bio=body[:1400])

# ---- 2002-2006: the index.htm CMS team section (oid=150) and its member pages
for y in range(2002, 2007):
    html, ts = get("http://www.redpoint.com/index.htm?action=view&oid=150", y, "team-oid150")
    if not html:
        continue
    oids = sorted({int(o) for o in re.findall(r"action=view&(?:amp;)?oid=(\d+)", html)}
                  - {146, 149, 150, 152, 157, 178, 199, 437})
    print(f"{y} oid=150: {len(oids)} candidate member pages")
    for oid in oids:
        page, _ = get(f"http://www.redpoint.com/index.htm?action=view&oid={oid}", y, f"oid{oid}")
        if not page or "Team Member" not in page:
            continue
        body = text(page)
        m = re.search(r"Team Member\s+([A-Z][a-z]+(?:\s+[A-Z][A-Za-z.'-]+){1,2})", body)
        if not m:
            continue
        add(m.group(1), y, f"oid{oid}", bio=body[:1800])

rows = sorted(people.values(), key=lambda r: r["name"])
for r in rows:
    r["years_seen"].sort()
    r["first_seen"], r["last_seen"] = r["years_seen"][0], r["years_seen"][-1]
write_atomic(OUT, json.dumps(rows, indent=1) + "\n")
print(f"\nearly roster: {len(rows)} people")
for r in rows:
    print(f"  {r['name']:26s} {r['first_seen']}-{r['last_seen']}  {r['slug']}")

# ---- merge into the main roster (existing entries win)
main = P.wayback / "partner-roster.json"
cur = json.loads(main.read_text()) if main.exists() else []
have = {r["name"].lower() for r in cur}
added = 0
for r in rows:
    if r["name"].lower() in have:
        continue
    cur.append({"slug": r["slug"], "name": r["name"], "years_seen": r["years_seen"],
                "first_seen": r["first_seen"], "last_seen": r["last_seen"],
                "snapshots": len(r["years_seen"]), "sources": r["sources"]})
    added += 1
write_atomic(main, json.dumps(sorted(cur, key=lambda r: r["slug"]), indent=1) + "\n")
print(f"merged into partner-roster.json: +{added} (now {len(cur)})")
