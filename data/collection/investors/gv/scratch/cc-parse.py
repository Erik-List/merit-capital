#!/usr/bin/env python3
"""Parse the archived portfolio listings of googleventures.com and gv.com (Common Crawl
captures fetched by cc-fetch.py) into sources/wayback/parsed/<year>.json, the shape
build-company-base.py reads: {slug, name, path, snapshot_ts, capture_url, filters, ...}.

Markups, one parser each (a zero-row capture that returned bytes is a failed parser, never
an empty year: every capture's count is printed, COLLECTION.md s5):
  A  2012 googleventures.com /portfolio: `<a pivot=".." href="/portfolio/<slug>"
     class="portfolio-company"><div class="company-summary" company="<Name>">` + description.
  B  2012-05 to 2013 googleventures.com /companies: `<a href="<site>" class="has-hovercard
     <tags>" class="company" hover_title="<Name>" hover_description="..">`, plus the
     spotlight logos (`<img .. alt="<Name>">`).
  C  2013-12 to 2015 gv.com /portfolio (WordPress): featured `<a href="<site>"
     class="link-block"><img .. alt="<Name>">` and listed `<a href="<site>" class="has-tooltip">
     Name`, each with a tooltip naming the deal partner (`<span class="names">`).
  D  2016 to 2019 gv.com /portfolio/: `<a class=".. js-companyModalLink" href="<site>"
     data-name=".." data-about=".." data-exit=".." data-investors="<a href='/team/<slug>'>..">`.
  E  2020 on: read by parse_e (the Contentful/Nuxt generations), added once seen.

Partners go into `filters` as the team slug, which the base build maps to partners_site when
the slug is on the roster (sources/wayback/partner-roster.json).
Usage: python3 cc-parse.py
"""
import collections
import html as H
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "gv"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
OUT = HERE.parent / "sources" / "wayback" / "parsed"
REPORT = HERE / "cc-parse-report.json"


def un(s):
    return re.sub(r"\s+", " ", H.unescape(H.unescape(s or ""))).strip()


def slug_of(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def team_slugs(s):
    s = H.unescape(s or "")
    return re.findall(r"/team/([a-z0-9-]+)", s)


def name_slug(n):
    return slug_of(n)


def parse_a(t):
    rows = []
    for m in re.finditer(r'<a pivot="([^"]*)" href="/portfolio/([^"]+)" class="portfolio-company">\s*'
                         r'<div class="company-summary" company="([^"]+)">(.*?)</a>', t, re.S):
        desc = re.search(r'class="company-description"[^>]*>(.*?)</div>', m.group(4), re.S)
        rows.append({"name": un(m.group(3)), "tags": m.group(1), "path": f"/portfolio/{m.group(2)}",
                     "about": un(desc.group(1)) if desc else ""})
    return rows


def parse_b(t):
    rows = []
    for m in re.finditer(r'<a href="([^"]*)" class="has-hovercard([^"]*)"[^>]*?hover_title="([^"]+)"'
                         r'[^>]*?hover_description="([^"]*)"', t, re.S):
        rows.append({"name": un(m.group(3)), "website": m.group(1), "tags": " ".join(m.group(2).split()),
                     "about": un(m.group(4))})
    spot = t.split('class="spotlight"', 1)
    if len(spot) == 2:
        blk = spot[1].split('class="company-filter"', 1)[0]
        for m in re.finditer(r'<a href="([^"]+)"><img src="[^"]*" alt="([^"]+)"', blk):
            rows.append({"name": un(m.group(2)), "website": m.group(1), "tags": "spotlight"})
    return rows


def parse_c(t):
    rows = []
    # featured logo cards: <li class="has-tooltip"><a href=".." class="link-block"><img .. alt="Name"> + tooltip
    for m in re.finditer(r'<a href="([^"]*)" class="link-block">\s*<img [^>]*alt="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
        p = re.findall(r'<span class="names">(.*?)</span>', m.group(3), re.S)
        d = re.search(r'company-tooltip">(.*?)<p class="partners">', m.group(3), re.S)
        rows.append({"name": un(m.group(2)), "website": m.group(1), "partners": [un(x) for x in p],
                     "about": un(d.group(1)) if d else ""})
    # listed names: <a href=".." class="has-tooltip"> Name <div class="tooltip-content company-tooltip">
    for m in re.finditer(r'<a href="([^"]*)" class="has-tooltip">\s*([^<]+?)\s*<div class="tooltip-content'
                         r' company-tooltip">(.*?)</div>', t, re.S):
        p = re.findall(r'<span class="names">(.*?)</span>', m.group(3), re.S)
        d = re.search(r'^(.*?)<p class="partners">', m.group(3), re.S)
        rows.append({"name": un(m.group(2)), "website": m.group(1), "partners": [un(x) for x in p],
                     "about": un(d.group(1)) if d else ""})
    return rows


def parse_d(t):
    rows = []
    for m in re.finditer(r'<a class="[^"]*js-companyModalLink"(.*?)>', t, re.S):
        a = m.group(1)

        def attr(k):
            x = re.search(rf'{k}="([^"]*)"', a, re.S)
            return x.group(1) if x else ""
        name = un(attr("data-name"))
        if not name:
            continue
        inv = attr("data-investors")
        rows.append({"name": name, "website": attr("href"), "about": un(attr("data-about")),
                     "exit": un(attr("data-exit")), "partner_slugs": team_slugs(inv),
                     "partners": [un(x) for x in re.findall(r">([^<]+)</a>", H.unescape(inv))]})
    return rows


NODE_JS = HERE / "js" / "nuxt2-companies.js"


def revive_nuxt_data(arr):
    """Nuxt 3's __NUXT_DATA__ (devalue): a flat array whose objects and arrays hold indices into it."""
    memo = {}

    def rv(i, depth=0):
        if not isinstance(i, int) or i < 0 or i >= len(arr) or depth > 60:
            return None
        if i in memo:
            return memo[i]
        v = arr[i]
        if isinstance(v, list):
            if v and isinstance(v[0], str) and v[0] in ("ShallowReactive", "Reactive", "Ref", "ShallowRef",
                                                         "EmptyRef", "EmptyShallowRef", "NuxtError"):
                out = rv(v[1], depth + 1) if len(v) > 1 else None
            elif v and isinstance(v[0], str) and v[0] in ("Set", "Map", "Date", "RegExp", "BigInt", "null"):
                out = None
            else:
                out = []
                memo[i] = out
                out.extend(rv(j, depth + 1) for j in v)
                return out
        elif isinstance(v, dict):
            out = {}
            memo[i] = out
            for k, j in v.items():
                out[k] = rv(j, depth + 1)
            return out
        else:
            out = v
        memo[i] = out
        return out
    return rv(0)


def parse_e(t, path=None):
    """2022-09 on: the Nuxt payload. Nuxt 2 over Contentful (window.__NUXT__, a minified function whose
    result is a cyclic graph) is evaluated by js/nuxt2-companies.js; Nuxt 3 (__NUXT_DATA__) is revived here.
    Both yield the CMS company entries the page was rendered from: name, exit line, deal partners."""
    import subprocess
    rows = []
    if path is not None and "window.__NUXT__" in t:
        r = subprocess.run(["node", str(NODE_JS), str(path)], capture_output=True, text=True)
        try:
            for c in json.loads(r.stdout or "[]"):
                rows.append({"name": un(c["name"]).replace("*", "").strip(), "website": c.get("website", ""),
                             "exit": un(c.get("acquiredBy", "")), "partners": c.get("investors") or [],
                             "tags": c.get("sector", "")})
        except ValueError:
            pass
    if not rows:
        m = re.search(r'<script[^>]*id="__NUXT_DATA__"[^>]*>(.*?)</script>', t, re.S)
        if m:
            data = revive_nuxt_data(json.loads(m.group(1)))
            seen = set()

            def walk(o, depth=0):
                if depth > 40 or id(o) in seen:
                    return
                seen.add(id(o))
                if isinstance(o, dict):
                    f = o.get("fields") if isinstance(o.get("fields"), dict) else o
                    if isinstance(f.get("name"), str) and ("acquiredBy" in f or "sector" in f):
                        inv = [x.get("fields", x).get("fullName") or x.get("fields", x).get("name") or ""
                               for x in (f.get("investors") or []) if isinstance(x, dict)]
                        rows.append({"name": un(f["name"]).replace("*", "").strip(), "website": f.get("website") or "",
                                     "exit": un(f.get("acquiredBy") or "") if isinstance(f.get("acquiredBy"), str) else "",
                                     "partners": [x for x in inv if x], "tags": ""})
                    for v in o.values():
                        walk(v, depth + 1)
                elif isinstance(o, list):
                    for v in o:
                        walk(v, depth + 1)
            walk(data)
    return rows


def which(dom, path, t):
    if dom == "gve" and path.rstrip("/") == "/portfolio" and 'class="company-summary"' in t:
        return "A", parse_a
    if dom == "gve" and 'hover_title=' in t:
        return "B", parse_b
    if 'company-tooltip' in t:
        return "C", parse_c
    if 'js-companyModalLink' in t:
        return "D", parse_d
    return "E", parse_e


# Curated renames in the parsed source (COLLECTION.md s5): two companies the firm listed under one display name in
# different eras. Keyed on (name, website domain); the second company takes its domain in brackets (the
# shared-names rule, Erik 2026-09-24), so the builder keeps them as two rows.
# "Sense" is NOT split: its 2016-19 entry linked sense.com (the home energy monitor) and the same CMS entry (same
# slot, same colour #F9461C) was re-linked to sensehq.com in May 2019; sense.com's own investor list has no GV and
# the firm's /ai list has SenseHQ re-investments from 2017-03, so it is one company mislinked (judge j12).
SAME_NAME_SPLIT = {("Bowery", "bowery.io"): "Bowery (bowery.io)", ("Basis", "basis.io"): "Basis (basis.io)"}


def dom(u):
    u = (u or "").lower()
    u = re.sub(r"^https?://", "", u).split("/")[0]
    return u.removeprefix("www.")


def main():
    man = json.loads(MAN.read_text())
    caps = sorted(((v["timestamp"], k, v) for k, v in man.items()
                   if v.get("status") == "ok" and re.match(r"^/(portfolio|companies|ai)/?$", v.get("path", ""))),
                  key=lambda x: x[0])
    years = collections.defaultdict(dict)   # year -> slug -> row (first capture in the year that lists it)
    report = []
    for ts, k, v in caps:
        t = (RAW / k).read_text(encoding="utf-8", errors="replace")
        era, fn = which(v["domain"], v["path"], t)
        rows = fn(t, RAW / k) if era == "E" else fn(t)
        report.append({"timestamp": ts, "domain": v["domain"], "path": v["path"], "bytes": v.get("bytes"),
                       "era": era, "rows": len(rows)})
        y = int(ts[:4])
        for r in rows:
            name = SAME_NAME_SPLIT.get((r["name"], dom(r.get("website"))), r["name"])
            if not name or len(name) > 80:
                continue
            s = slug_of(name)
            if not s or s in years[y]:
                continue
            filt = sorted(set(r.get("partner_slugs") or []) | {slug_of(p) for p in r.get("partners") or [] if p})
            years[y][s] = {"slug": s, "name": name, "path": r.get("path") or v["path"], "snapshot_ts": ts,
                           "capture_url": v["capture_url"], "filters": ",".join(filt), "era": era,
                           "website": r.get("website", ""), "about": r.get("about", ""),
                           "exit": r.get("exit", ""), "tags": r.get("tags", ""),
                           "partners": r.get("partners") or []}
    OUT.mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(years.items()):
        # merge rather than replace (COLLECTION.md s5: parsed year files merge; a pull must never delete rows)
        f = OUT / f"{y}.json"
        old = {}
        for r in rows.values():
            old[(r["slug"], r["path"])] = r
        write_atomic(f, json.dumps(sorted(old.values(), key=lambda r: r["slug"]), indent=1, ensure_ascii=False) + "\n")
        print(y, len(rows), "companies (", collections.Counter(r["era"] for r in rows.values()), ")")
    write_atomic(REPORT, json.dumps(report, indent=1) + "\n")
    zero = [r for r in report if r["rows"] == 0]
    print(len(report), "captures parsed;", len(zero), "with zero rows:",
          [(r["timestamp"][:8], r["domain"], r["path"], r["era"], r["bytes"]) for r in zero][:20])


if __name__ == "__main__":
    main()
