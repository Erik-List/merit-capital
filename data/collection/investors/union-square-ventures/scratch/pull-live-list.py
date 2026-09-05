#!/usr/bin/env python3
"""Read usv.com/companies/ (the firm's one live list surface, a WordPress `company` post type
with no REST route) into sources/site/live-companies.json: every row's name, website, first
investment ("<round>, <year>" or a bare year), exit detail, excerpt, 'Read the Post' link and
logo, plus the firm's own per-company Sector, Status and Entry Point taxonomy terms read off the
filtered list pages (?industry-cat=, ?status-cat=, ?entry-point-cat=). Paced ~1 request/s."""
import json, re, html, subprocess, time, sys
from pathlib import Path
OUT = Path("data/collection/investors/union-square-ventures/sources/site/live-companies.json")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 MeritCapitalResearch/1.0 (erik@meritcapit.al)"
BASE = "https://www.usv.com/companies/"
def get(url):
    for a in range(4):
        r = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA, url], capture_output=True, text=True)
        if r.returncode == 0 and "m__list-row" in r.stdout: return r.stdout
        time.sleep(4 * (a + 1))
    print("FAILED", url, file=sys.stderr); return ""
def rows_of(h):
    out = []
    for b in re.split(r'<div class="m__list-row ">', h)[1:]:
        b = b.split('<div class="m__list-row m__list-row--mobile')[0]
        def g(p):
            m = re.search(p, b, re.S); return html.unescape(m.group(1)).strip() if m else None
        name = g(r'<div class="m__list-row__col">\s*<a href="[^"]*"[^>]*>([^<]+)</a>') \
            or g(r'<div class="m__list-row__col">\s*([^<]+?)\s*<span class="exit-detail">')
        url = g(r'<div class="m__list-row__col">\s*<a href="([^"]*)"[^>]*>[^<]+</a>\s*<span class="exit-detail">')
        fi = g(r'<span class="exit-detail">[^<]*</span>\s*</div>\s*<div class="m__list-row__col">\s*([^<]*?)\s*</div>')
        out.append({"name": name, "url": url, "first_investment": fi,
                    "exit_detail": g(r'<span class="exit-detail">([^<]*)</span>') or "",
                    "excerpt": g(r'<div class="m__list-row__excerpt">\s*(.*?)\s*</div>'),
                    "post": g(r'class="m__list-row__link"\s*href="([^"]+)"'),
                    "logo": g(r'<img[^>]*src="([^"]+)"')})
    return out
main = rows_of(get(BASE + "?sortby=date_invested&order=desc"))
print("main rows", len(main), "unnamed", sum(1 for r in main if not r["name"]))
key = lambda r: (r["name"] or "").lower()
idx = {key(r): r for r in main}
for r in main: r["sectors"], r["status_site"], r["entry_point_site"] = [], None, None
facets = {"industry-cat": ["adtech","ai","climate","commerce","community","consumer","creator-platform","crypto","data","developer-tools","education","enterprise","environment","fintech","food","gaming","hardware","health","hr","infrastructure","insurance","machine-learning","marketplace","media","music","privacy-security","publishing","real-estate","retail","social","transportation","workforce"],
          "status-cat": ["acquired","current","exited","inactive","public"],
          "entry-point-cat": ["seed","series-a","series-b","series-c","series-d","series-e","common","token","pre-seed","growth","secondary","other"]}
counts = {}
for facet, terms in facets.items():
    for term in terms:
        time.sleep(1.0)
        h = get(f"{BASE}?{facet}={term}")
        rs = rows_of(h) if h else []
        counts[f"{facet}={term}"] = len(rs)
        for r in rs:
            t = idx.get(key(r))
            if t is None:
                print("facet row not in main list:", facet, term, r["name"], file=sys.stderr); continue
            if facet == "industry-cat": t["sectors"].append(term)
            elif facet == "status-cat": t["status_site"] = term if not t["status_site"] else t["status_site"] + "," + term
            else: t["entry_point_site"] = term if not t["entry_point_site"] else t["entry_point_site"] + "," + term
        print(f"{facet}={term}: {len(rs)}", flush=True)
for r in main:
    m = re.match(r'^(.*?),\s*(\d{4})$', r["first_investment"] or "")
    r["round_site"], r["invest_year"] = (m.group(1).strip(), int(m.group(2))) if m else (None, int(r["first_investment"]) if (r["first_investment"] or "").strip().isdigit() else None)
OUT.write_text(json.dumps({"_readme": "usv.com/companies/ read " + time.strftime("%Y-%m-%d") + " (scratch/pull-live-list.py): the server-rendered m__list-row table sorted by date_invested desc, one row per company (name, website, 'FIRST INVESTMENT' label split into round_site + invest_year, exit_detail, excerpt, Read-the-Post link, logo), plus the firm's own Sector / Status / Entry Point taxonomy terms per company read off the filtered list pages. The company post type has no REST route (wp-json types omit it); the taxonomies do (Sector 32 terms, Status 5, Entry Point none).", "pulled": time.strftime("%Y-%m-%dT%H:%M"), "facet_counts": counts, "count": len(main), "rows": main}, ensure_ascii=False, indent=1))
print("wrote", OUT, len(main))
