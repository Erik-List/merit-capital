#!/usr/bin/env python3
"""Pull Insight Partners' own site (insightpartners.com, WordPress) into file_list sources.

insightpartners.com is a WordPress site whose portfolio and team are Vue
components fed by the theme's own public REST namespace, `insight/v1`, beside
the stock `wp/v2` routes. Everything here is what the site's own pages call,
served without auth:

  wp/v2/sfcompany                       every company post: id, slug, title, link, dates
  insight/v1/get-companies?page=N       the grid rows: location, verticals (12 per page)
  insight/v1/get-company-content?id=    the company panel: description, Investment
                                        Team, Sectors, Initial Investment (month and
                                        year), Status (Current / Prior Investment),
                                        milestones, the case-study text where one exists
  wp/v2/posts                           the Ideas archive (news, press, blog)
  insight/v1/get-users                  the team grid: name, position, departments
  insight/v1/get-user-content?id=       the person panel: bio, socials, companies

Writes, under data/collection/investors/insight-partners/sources/site/:
  company-pages.json  one row per company
  posts.json          one row per post, with body text
  team-pages.json     one row per person

Raw payloads are cached under scratch/site-raw/ so a re-run is offline.
Usage: python3 data/collection/investors/insight-partners/scratch/pull-site-insight.py
           [--refresh] [--only companies|posts|team]
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/insight-partners"
RAW = INV / "scratch/site-raw"
OUT = INV / "sources/site"
BASE = "https://www.insightpartners.com"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")
REFRESH = "--refresh" in sys.argv
ONLY = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], 1)}


def get(url: str, ok_404: bool = False) -> bytes:
    code = b""
    for attempt in range(4):
        r = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA,
                            "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code == b"200":
            time.sleep(0.35)
            return body
        if ok_404 and code in (b"400", b"404"):
            return b""
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url} rc={r.returncode} code={code!r}")


def cached(name: str, url: str, ok_404: bool = False) -> bytes:
    p = RAW / name
    if p.exists() and p.stat().st_size and not REFRESH:
        return p.read_bytes()
    b = get(url, ok_404)
    if b:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b)
    return b


def loads2(b: bytes):
    """insight/v1 returns a JSON string that itself holds JSON."""
    v = json.loads(b)
    return json.loads(v) if isinstance(v, str) else v


def text_of(fragment: str) -> str:
    t = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", fragment, flags=re.S)
    t = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>|</div>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    t = re.sub(r"\s*\n\s*", "\n", t)
    return t.strip()


def wp_all(rest_base: str, fields: str, tag: str) -> list[dict]:
    rows, page = [], 1
    while True:
        # ordered by id: the default order is by date, the import stamped
        # hundreds of posts with one second, and pages ordered on a tie
        # repeat some rows and drop others (47 of 856 companies on the first
        # pull)
        url = (f"{BASE}/wp-json/wp/v2/{rest_base}?per_page=100&page={page}"
               f"&orderby=id&order=asc&_fields={fields}")
        b = cached(f"wpid-{tag}-{page:03d}.json", url, ok_404=True)
        if not b:
            break
        batch = json.loads(b)
        if not isinstance(batch, list) or not batch:
            break
        rows.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    seen, uniq = set(), []
    for r in rows:
        if r["id"] not in seen:
            seen.add(r["id"])
            uniq.append(r)
    if len(uniq) != len(rows):
        print(f"  wp/v2/{rest_base}: {len(rows) - len(uniq)} repeated rows dropped")
    return uniq


def role_blocks(content: str) -> dict[str, list[str]]:
    """The panel's labelled blocks: {label: [values]}."""
    out: dict[str, list[str]] = {}
    m = re.search(r'class="partnership-content__roles[^"]*"[^>]*>(.*?)'
                  r'<div class="partnership-content-sec3"', content, flags=re.S)
    if not m:
        return out
    for blk in re.split(r'<div class="mb-e25 block">', m.group(1)):
        lab = re.search(r'<span class="font-semibold block">(.*?)</span>', blk, flags=re.S)
        if not lab:
            continue
        label = text_of(lab.group(1))
        rest = blk[lab.end():]
        vals = [text_of(v) for v in re.findall(
            r'<(?:span|a)\b[^>]*class="block[^"]*"[^>]*>(.*?)</(?:span|a)>', rest, flags=re.S)]
        out[label] = [v for v in vals if v]
    return out


def pull_companies() -> None:
    posts = wp_all("sfcompany", "id,slug,title,link,date,modified", "sfcompany")
    print(f"wp/v2/sfcompany: {len(posts)} posts")

    # the grid rows carry location and verticals; 12 per page
    grid: dict[int, dict] = {}
    page, mx = 1, None
    while True:
        b = cached(f"grid-{page:03d}.json",
                   f"{BASE}/wp-json/insight/v1/get-companies?page={page}")
        d = loads2(b)
        mx = d.get("max")
        rows = d.get("rows") or []
        if not rows:
            break
        for r in rows:
            grid[int(r["id"])] = r
        if mx and len(grid) >= int(mx):
            break
        page += 1
        if page > 200:
            break
    print(f"insight/v1/get-companies: {len(grid)} grid rows (max {mx})")

    # the status filter is the grid's own Current / Prior split, a cross-check
    # on the panel's Status block
    status_by_id: dict[int, str] = {}
    for label in ("Current Investment", "Prior Investment"):
        page = 1
        n = 0
        while True:
            tag = label.split()[0].lower()
            url = (f"{BASE}/wp-json/insight/v1/get-companies?"
                   f"status%5B%5D={quote(label)}&page={page}")
            d = loads2(cached(f"grid-status-{tag}-{page:03d}.json", url))
            rows = d.get("rows") or []
            if not rows:
                break
            for r in rows:
                status_by_id[int(r["id"])] = label
            n += len(rows)
            if d.get("max") and n >= int(d["max"]):
                break
            page += 1
            if page > 200:
                break
        print(f"  status filter {label}: {n}")

    # the grid is the second enumeration; a company on one and not the other
    # is reported, and a grid-only company is still pulled
    have = {int(p["id"]) for p in posts}
    for cid, g in grid.items():
        if cid not in have:
            print(f"  grid-only company {cid} {g.get('slug')}")
            posts.append({"id": cid, "slug": g.get("slug", ""), "link": f"{BASE}/portfolio/{g.get('slug')}/",
                          "title": {"rendered": g.get("name", "")}, "date": "", "modified": ""})
    missing = have - set(grid)
    if missing:
        print(f"  {len(missing)} posts absent from the grid: {sorted(missing)[:10]}")

    out, failed = [], []
    for i, p in enumerate(sorted(posts, key=lambda x: x["slug"])):
        cid = int(p["id"])
        try:
            b = cached(f"company-{cid}.json",
                       f"{BASE}/wp-json/insight/v1/get-company-content?id={cid}&detail=true")
            content = loads2(b).get("content") or ""
        except Exception as e:                      # a failed fetch is not an absence
            failed.append((cid, p["slug"], str(e)))
            continue
        blocks = role_blocks(content)
        g = grid.get(cid, {})
        name = html.unescape(p["title"]["rendered"]).strip()

        hrefs = re.findall(r'<a href="([^"]+)"[^>]*title="Learn More About', content)
        site = next((h for h in hrefs if not re.search(
            r"twitter\.com|x\.com|linkedin\.com|facebook\.com|instagram\.com", h)), "")
        linkedin = next((h for h in hrefs if "linkedin.com" in h), "")

        desc_m = re.search(r'class="partnership-content-sec1">(.*?)'
                           r'<div class="partnership-content-sec2">', content, flags=re.S)
        body_text = text_of(desc_m.group(1)) if desc_m else ""

        ms_m = re.search(r'class="partnership-content__milestones[^"]*"[^>]*>(.*?)</div>\s*</div>',
                         content, flags=re.S)
        milestones = [l for l in text_of(ms_m.group(1)).split("\n") if l] if ms_m else []

        init = (blocks.get("Initial Investment") or [""])[0]
        init_raw = init
        # "June 1996" is the CMS's placeholder, not a date: 36 panels carry it,
        # among them LivingSocial (founded 2007), Ticketmonster (2010) and
        # Fuze. It is kept raw and dates nothing.
        if init == "June 1996":
            init = ""
        iy = im = ""
        mm = re.match(r"([A-Z][a-z]+)\s+((?:19|20)\d\d)$", init)
        if mm and mm.group(1) in MONTHS:
            iy, im = mm.group(2), f"{mm.group(2)}-{MONTHS[mm.group(1)]:02d}"
        elif re.fullmatch(r"(?:19|20)\d\d", init):
            iy = init

        # a case study names the round in words ("joined the Series C round")
        journey = ""
        jm = re.search(r"Insight.s Investment Journey(.*?)(?:How We Helped|Key Results|$)",
                       body_text, flags=re.S)
        if jm:
            journey = jm.group(1).strip()

        ideas = sorted(set(re.findall(
            r'href="(https://www\.insightpartners\.com/ideas/[^"]+)"', content)))

        status = (blocks.get("Status") or [""])[0]
        row = {
            "id": cid,
            "slug": p["slug"],
            "name": name,
            "url": p["link"],
            "post_date": p.get("date", ""),
            "post_modified": p.get("modified", ""),
            "location": g.get("location", ""),
            "sectors": blocks.get("Sectors") or [],
            "partners": blocks.get("Investment Team") or [],
            "initial_investment": init,
            "initial_investment_raw": init_raw,
            "invest_year": iy,
            "invest_date": im,
            "site_status": status,
            "site_status_filter": status_by_id.get(cid, ""),
            "company_site": site,
            "linkedin": linkedin,
            "description": body_text[:1500],
            "investment_journey": journey[:1500],
            "milestones": milestones,
            "ideas": ideas,
            "in_grid": cid in grid,
            "other_blocks": {k: v for k, v in blocks.items() if k not in (
                "Investment Team", "Sectors", "Initial Investment", "Status")},
        }
        out.append(row)
        if (i + 1) % 100 == 0:
            print(f"  company panels: {i + 1}/{len(posts)}")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "company-pages.json").write_text(json.dumps({
        "_readme": ("Insight Partners' live portfolio, read from the site's own REST routes "
                    "(wp/v2/sfcompany for the post list, insight/v1/get-companies for the "
                    "grid rows, insight/v1/get-company-content for each panel) by "
                    "scratch/pull-site-insight.py. 'initial_investment' is the firm's own "
                    "month and year of first investment; 'site_status' is the FIRM's position "
                    "(Current / Prior Investment), not the company's state; 'partners' is the "
                    "panel's Investment Team. The site publishes no round word per company; "
                    "'investment_journey' is the case-study text on the few panels that carry one."),
        "_source": f"{BASE}/wp-json/insight/v1/",
        "_pulled": date.today().isoformat(),
        "_failed": failed,
        "rows": out,
    }, indent=1, ensure_ascii=False))
    print(f"company-pages.json: {len(out)} rows, {len(failed)} failed")
    if failed:
        for f in failed[:20]:
            print("   FAILED", f)


def pull_posts() -> None:
    posts = wp_all("posts", "id,date,slug,link,title,content,excerpt,categories,tags",
                   "posts")
    out = []
    for p in posts:
        body = text_of(p.get("content", {}).get("rendered", ""))
        out.append({
            "id": p["id"], "date": p.get("date", ""), "slug": p["slug"],
            "url": p["link"],
            "title": html.unescape(re.sub(r"<[^>]+>", "", p["title"]["rendered"])).strip(),
            "categories": p.get("categories", []), "tags": p.get("tags", []),
            "excerpt": text_of(p.get("excerpt", {}).get("rendered", ""))[:600],
            "body": body,
        })
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "posts.json").write_text(json.dumps({
        "_readme": ("The Ideas archive (news, press, blog) from wp/v2/posts, body text "
                    "kept: the firm's own announcements name rounds in words."),
        "_source": f"{BASE}/wp-json/wp/v2/posts",
        "_pulled": date.today().isoformat(),
        "rows": sorted(out, key=lambda r: r["date"]),
    }, indent=1, ensure_ascii=False))
    print(f"posts.json: {len(out)} posts")


def pull_team() -> None:
    d = loads2(cached("users.json", f"{BASE}/wp-json/insight/v1/get-users"))
    rows = d.get("rows") or []
    wp = {int(p["id"]): p for p in wp_all("sfuser", "id,slug,link,date,modified", "sfuser")}
    # the team page's own department filter (term ids from its :filters prop);
    # a person can sit in several
    DEPARTMENTS = {12: "Investors", 13: "Onsite Experts", 14: "Firm Operations",
                   15: "Capital Partnerships", 127: "Advisors", 128: "CIO Council",
                   129: "Government Advisory Board", 102: "Diligence and Growth Strategy",
                   103: "Business Development", 97: "Talent", 99: "Sales & Customer Success",
                   100: "Marketing", 101: "Product and Technology", 147: "Finance"}
    dept_of: dict[int, list[str]] = {}
    for tid, label in DEPARTMENTS.items():
        dd = loads2(cached(f"users-dept-{tid}.json",
                           f"{BASE}/wp-json/insight/v1/get-users?department={tid}"))
        for u in dd.get("rows") or []:
            dept_of.setdefault(int(u["id"]), []).append(label)
        print(f"  department {label}: {len(dd.get('rows') or [])}")
    out, failed = [], []
    for i, u in enumerate(rows):
        uid = int(u["id"])
        try:
            b = cached(f"user-{uid}.json",
                       f"{BASE}/wp-json/insight/v1/get-user-content?id={uid}&detail=true")
            content = loads2(b).get("content") or ""
        except Exception as e:
            failed.append((uid, u.get("full_name"), str(e)))
            content = ""
        hrefs = re.findall(r'href="([^"]+)"', content)
        linkedin = next((h for h in hrefs if re.search(r"linkedin\.com/in/", h)), "")
        x = next((h for h in hrefs if re.search(r"(twitter|x)\.com/(?!insightpartners)", h)), "")
        companies = sorted(set(re.findall(r'href="(?:https://www\.insightpartners\.com)?'
                                          r'/portfolio/([a-z0-9][a-z0-9-]*)/?"', content)))
        p = wp.get(uid, {})
        keep = {k: v for k, v in u.items() if k not in ("image",)}
        out.append({
            "id": uid,
            "slug": p.get("slug", ""),
            "name": (u.get("full_name") or "").strip(),
            "url": p.get("link", ""),
            "title": (u.get("position") or "").strip(),
            "departments": dept_of.get(uid, []),
            "group": (dept_of.get(uid) or [""])[0],
            "grid": keep,
            "linkedin_url": linkedin,
            "x_url": x,
            "companies": companies,
            "bio": text_of(content)[:1500],
        })
        if (i + 1) % 100 == 0:
            print(f"  person panels: {i + 1}/{len(rows)}")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "team-pages.json").write_text(json.dumps({
        "_readme": ("The live team from insight/v1/get-users and get-user-content; "
                    "'grid' is the grid row as served (departments and tags included)."),
        "_source": f"{BASE}/wp-json/insight/v1/get-users",
        "_pulled": date.today().isoformat(),
        "_failed": failed,
        "rows": out,
    }, indent=1, ensure_ascii=False))
    print(f"team-pages.json: {len(out)} people, {len(failed)} failed")


if __name__ == "__main__":
    if ONLY in ("", "companies"):
        pull_companies()
    if ONLY in ("", "posts"):
        pull_posts()
    if ONLY in ("", "team"):
        pull_team()
