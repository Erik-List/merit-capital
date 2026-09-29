#!/usr/bin/env python3
"""Pull TCV's live first-party surfaces into sources/site/ (PRO-169).

tcv.com is a Next.js App Router site over Contentful (space ue5a638q2a2b);
the pages ship their data inside the RSC flight payload (self.__next_f), so
each surface is read from its own page with no API key:

  /all-companies            the marketing-rule compliance list, "All
                            investments, listed alphabetically", a plain-text
                            block of legal names dated "*as of 7.15.26"
                            -> all-companies-2026.json
  /partnerships             the featured grid (name, slug, status, location,
                            continent, sector, description)
  /partnerships/<slug>      per company: investmentTeam (the deal partners),
                            yearFounded, websiteUrl, linked articles
                            -> partnerships-2026.json
  /team, /team/<slug>       the team (name, title, role, location, flags,
                            LinkedIn / X where the page carries them)
                            -> team-2026.json
  portfoliojobs.tcv.com     the Getro job board, from sitemap_companies.xml and
                            each company page's __NEXT_DATA__
                            -> jobboard-2026.json

Every file carries a _readme. Re-running refetches everything (the pages are
small); raw pages land in scratch/site-raw/ for audit.

Brand derivation from a legal name (all-companies only): "X (dba Y)" and
"X dba Y" publish as Y; "(fka Y)" is kept as an alias; "acquired by Z" is kept
as a note; legal suffixes are dropped. The legal name is kept verbatim.
"""
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
RAW = INV / "scratch/site-raw"
OUT = INV / "sources/site"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
TODAY = time.strftime("%Y-%m-%d")


def get(url: str, dest: Path | None = None, tries: int = 3) -> str:
    # detail pages are cached (a re-run retries only what failed); the three list
    # pages and the sitemap are always refetched
    if dest and dest.exists() and dest.stat().st_size > 0 and dest.parent != RAW:
        return dest.read_text()
    for a in range(tries):
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "40", "-A", UA,
                            "-w", "\n%{http_code}", url], capture_output=True)
        body = r.stdout.decode("utf-8", "replace")
        body, _, code = body.rpartition("\n")
        if code == "200" and body:
            if dest:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body)
            time.sleep(0.4)
            return body
        time.sleep(2 * (a + 1))
    print(f"  FAILED {url} ({code})", file=sys.stderr)
    return ""


def rsc(html: str) -> str:
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, flags=re.S)
    return "".join(json.loads('"' + c + '"') for c in chunks)


def balanced(s: str, start: int) -> str:
    """The JSON value (object or array) that opens at s[start]."""
    open_c = s[start]
    close_c = {"{": "}", "[": "]"}[open_c]
    depth, i, instr, esc = 0, start, False, False
    while i < len(s):
        ch = s[i]
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
        elif ch == '"':
            instr = True
        elif ch == open_c:
            depth += 1
        elif ch == close_c:
            depth -= 1
            if depth == 0:
                return s[start:i + 1]
        i += 1
    raise ValueError("unbalanced")


SUFFIX = re.compile(
    r"(,?\s+(inc\.?|incorporated|corp\.?|corporation|co\.?|company|llc|l\.l\.c\.?|ltd\.?|limited|"
    r"l\.p\.?|lp|plc|s\.a\.s\.?|sas|s\.a\.?|sa|se|b\.v\.?|bv|n\.v\.?|gmbh|ag|oy|a/s|pty\.?\s+ltd\.?|pty\s+limited|"
    r"private\s+limited|pbc|holdings?|holdco|topco|parent|group))+\s*[.,]?\s*$", re.I)


def brand_of(legal: str) -> dict:
    s = re.sub(r"\s+", " ", legal).strip().rstrip(",")
    out = {"legal_name": s, "aliases": [], "note": ""}
    m = re.search(r",?\s*acquired by (.+)$", s, re.I)
    if m:
        out["note"] = "acquired by " + m.group(1).strip()
        s = s[:m.start()].strip().rstrip(",")
    for fm in re.finditer(r"\(fka ([^)]+)\)", s, re.I):
        out["aliases"].append(fm.group(1).strip())
    s = re.sub(r"\s*\(fka [^)]+\)", "", s, flags=re.I).strip()
    m = re.search(r"\(dba ([^)]+)\)", s, re.I) or re.search(r"\bdba (.+)$", s, re.I)
    if m:
        out["aliases"].append(SUFFIX.sub("", s[:m.start()]).strip() or s[:m.start()].strip())
        s = m.group(1).strip()
    brand = SUFFIX.sub("", s).strip().rstrip(",").strip()
    out["name"] = brand or s
    return out


def all_companies() -> list[dict]:
    html = get("https://www.tcv.com/all-companies", RAW / "all-companies.html")
    s = rsc(html)
    m = re.search(r"\n[0-9a-f]+:T([0-9a-f]+),(\*as of [^\n]*)\n", s)
    size = int(m.group(1), 16)
    # the T-row length counts UTF-8 bytes, not characters ("O’Brien")
    block = s[m.start(2):].encode("utf-8")[:size].decode("utf-8", "ignore")
    asof = m.group(2).strip()
    rows = []
    for line in block.split("\n")[1:]:
        line = line.strip()
        if not line:
            continue
        b = brand_of(line)
        b["url"] = "https://www.tcv.com/all-companies"
        b["list_asof"] = asof
        rows.append(b)
    print(f"all-companies: {len(rows)} rows ({asof})")
    return rows, asof


def partnerships() -> list[dict]:
    html = get("https://www.tcv.com/partnerships", RAW / "partnerships.html")
    s = rsc(html)
    i = s.find('"companies":[')
    arr = json.loads(balanced(s, i + len('"companies":')))
    rows = []
    for c in arr:
        slug = c["slug"]
        d = get(f"https://www.tcv.com/partnerships/{slug}", RAW / f"partnerships/{slug}.html")
        ds = rsc(d)
        team, founded, website, articles, tagline = [], None, None, [], None
        j = ds.find('"company":{')
        if j >= 0:
            try:
                comp = json.loads(balanced(ds, j + len('"company":')))
            except ValueError:
                comp = {}
            founded = comp.get("yearFounded")
            website = comp.get("websiteUrl")
            tagline = comp.get("tagline")
            it = comp.get("investmentTeam") or {}
            for p in (it.get("items") if isinstance(it, dict) else it) or []:
                if isinstance(p, dict) and p.get("name"):
                    team.append(p["name"])
            ar = comp.get("articles") or {}
            for a in (ar.get("items") if isinstance(ar, dict) else ar) or []:
                if isinstance(a, dict):
                    articles.append({k: a.get(k) for k in ("title", "slug", "date", "publishDate", "url") if a.get(k)})
        rows.append({
            "name": c["name"], "slug": slug, "status_site": c.get("status"),
            "location": c.get("location"), "continent": c.get("continent"),
            "sectors": [x["name"] for x in ((c.get("sectors2") or {}).get("items") or [])],
            "description": c.get("description"), "tagline": tagline,
            "year_founded": founded, "company_site": website,
            "partners": team, "articles": articles,
            "url": f"https://www.tcv.com/partnerships/{slug}",
        })
    print(f"partnerships: {len(rows)} rows, {sum(1 for r in rows if r['partners'])} with a deal team")
    return rows


def team() -> list[dict]:
    html = get("https://www.tcv.com/team", RAW / "team.html")
    s = rsc(html)
    people = {}
    for m in re.finditer(r'\{"leadership":(?:true|false)', s):
        try:
            p = json.loads(balanced(s, m.start()))
        except ValueError:
            continue
        if p.get("name") and p.get("slug"):
            people[p["slug"]] = p
    rows = []
    for slug, p in people.items():
        d = rsc(get(f"https://www.tcv.com/team/{slug}", RAW / f"team/{slug}.html"))
        li = re.search(r'"linkedInUrl":"([^"]+)"', d)
        tw = re.search(r'"twitterUrl":"([^"]+)"', d)
        rows.append({
            "name": p["name"], "slug": slug, "title": p.get("title"), "role": p.get("role"),
            "location": (p.get("location") or {}).get("name"),
            "leadership": p.get("leadership"), "executive_committee": p.get("executiveCommittee"),
            "sectors": [x["name"] for x in ((p.get("sectors2") or {}).get("items") or [])],
            "linkedin_url": li.group(1) if li else None, "x_url": tw.group(1) if tw else None,
            "url": f"https://www.tcv.com/team/{slug}",
        })
    print(f"team: {len(rows)} people")
    return rows


def jobboard() -> list[dict]:
    sm = get("https://portfoliojobs.tcv.com/sitemap_companies.xml", RAW / "jobboard-sitemap.xml")
    locs = re.findall(r"<loc>([^<]+/companies/[^<]+)</loc>", sm)
    rows = []
    for u in locs:
        slug = u.rstrip("/").split("/companies/")[1].split("/")[0]
        h = get(u, RAW / f"jobboard/{slug}.html")
        m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
        if not m:
            continue
        d = json.loads(m.group(1))
        c = (((d.get("props") or {}).get("pageProps") or {}).get("company")
             or ((d.get("props") or {}).get("pageProps") or {}).get("initialState", {}).get("company", {}).get("data") or {})
        if not c:
            # the page's company object sits under different keys per Getro build
            txt = m.group(1)
            nm = re.search(r'"name":"([^"]+)","slug":"' + re.escape(slug), txt)
            c = {"name": unescape(nm.group(1))} if nm else {}
        rows.append({"name": c.get("name"), "slug": slug, "domain": c.get("domain"),
                     "stage_board": c.get("stage"), "locations": c.get("locations"),
                     "industry_tags": c.get("industryTags"), "url": u})
    print(f"jobboard: {len(rows)} companies from {len(locs)} sitemap entries")
    return rows


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows, asof = all_companies()
    (OUT / "all-companies-2026.json").write_text(json.dumps({
        "_readme": f"tcv.com/all-companies read {TODAY}: TCV's marketing-rule list, 'All investments, listed "
                   f"alphabetically', {asof.strip('*')}. Declared exclusion (the page's own note): 'Does not include "
                   "investments that were made solely in IPOs or open market public securities in TCV I-III as they "
                   "represent a different strategy than currently employed.' The same note defines deal types: "
                   "'majority' = TCV, singly or together with a consortium of other investors, owns or controls 50% or "
                   "greater after the closing; 'minority' = less than 50%. legal_name is the page's text verbatim; "
                   "name is the brand derived by scratch/pull-site-tcv.py (dba wins, fka kept as an alias, legal "
                   "suffixes dropped).",
        "rows": rows}, indent=1, ensure_ascii=False))
    p = partnerships()
    (OUT / "partnerships-2026.json").write_text(json.dumps({
        "_readme": f"tcv.com/partnerships and every /partnerships/<slug> page, read {TODAY} from the RSC payload "
                   "(Contentful space ue5a638q2a2b). status_site is the grid's Active/Exited field (the FIRM's position, "
                   "not the company's state). partners is the page's investmentTeam: the TCV people on the deal.",
        "rows": p}, indent=1, ensure_ascii=False))
    t = team()
    (OUT / "team-2026.json").write_text(json.dumps({
        "_readme": f"tcv.com/team and every /team/<slug> page, read {TODAY} from the RSC payload.",
        "rows": t}, indent=1, ensure_ascii=False))
    j = jobboard()
    (OUT / "jobboard-2026.json").write_text(json.dumps({
        "_readme": f"portfoliojobs.tcv.com (Getro), read {TODAY} from sitemap_companies.xml and each company page's "
                   "__NEXT_DATA__. stage_board is the board's own field and is NOT a stage label (COLLECTION.md 5: "
                   "a job board's stage is the company's current stage).",
        "rows": j}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
