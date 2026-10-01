"""Scrape www.speedinvest.com/portfolio (Webflow CMS list, 50 per page) into
sources/site/companies-2026.json. Each row: name, url (/portfolio/<slug>),
short description, sectors (site tags incl. 'Exits' and region tags),
invest_year ('Year Invested'), full description, country (hidden field),
website/linkedin links from the per-company page."""
import re, json, html, time, subprocess, sys, datetime
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
def get(u):
    for i in range(4):
        r = subprocess.run(["curl", "-sSL", "--max-time", "60", "-A", UA, u], capture_output=True)
        if r.returncode == 0 and len(r.stdout) > 1000:
            return r.stdout.decode("utf-8", "replace")
        time.sleep(3)
    raise SystemExit(f"fetch failed {u}")
def clean(x):
    x = re.sub(r"<[^>]+>", " ", x)
    x = html.unescape(x).replace("‍", " ")
    return re.sub(r"\s+", " ", x).strip()
def parse_items(s):
    rows = []
    for m in re.finditer(r'class="portfolio-list_item w-dyn-item">', s):
        chunk = s[m.end(): m.end() + 30000]
        nxt = chunk.find('class="portfolio-list_item w-dyn-item">')
        if nxt > 0: chunk = chunk[:nxt]
        name = clean(re.search(r'fs-list-field="itemTitle"[^>]*>(.*?)</h6>', chunk, re.S).group(1))
        short = re.search(r'fs-list-field="descript"[^>]*>(.*?)</p>', chunk, re.S)
        top = chunk.split('portfolio-list_answer')[0]
        tags = [clean(t) for t in re.findall(r'fs-list-field="portfolio">(.*?)</div>', top, re.S)]
        year = re.search(r'fs-list-field="date">(.*?)</div>', chunk, re.S)
        full = re.search(r'portfolio-list_full-descript-rtf[^>]*>(.*?)</div>', chunk, re.S)
        hid = [clean(t) for t in re.findall(r'<div class="hide"><div fs-list-field="portfolio">(.*?)</div>', chunk, re.S)]
        links = re.findall(r'data-fullurl="([^"]+)"', chunk) + [l for l in re.findall(r'href="(https?://[^"]+)"', chunk) if 'linkedin.com/company' in l or 'linkedin.com/in' in l]
        page = re.search(r'href="(/portfolio/[^"#?]+)"', chunk)
        rows.append({"name": name, "short": clean(short.group(1)) if short else None,
                     "sectors": tags, "invest_year": clean(year.group(1)) if year else None,
                     "description": clean(full.group(1)) if full else None,
                     "hidden_tags": hid, "links": links,
                     "page": page.group(1) if page else None})
    return rows
all_rows, seen = [], set()
for key in ["84ffd661", "d5ea7f63"]:
    for p in range(1, 40):
        u = "https://www.speedinvest.com/portfolio" + (f"?{key}_page={p}" if p > 1 else "")
        s = get(u)
        rows = parse_items(s)
        new = [r for r in rows if r["name"] not in seen]
        for r in new: seen.add(r["name"]); r["list_page"] = u
        all_rows += new
        print(key, p, len(rows), len(new), file=sys.stderr)
        if not re.search(rf'href="\?{key}_page={p+1}"', s): break
        time.sleep(1)
json.dump({"_readme": "www.speedinvest.com/portfolio (Webflow CMS list, paginated ?<list>_page=N) scraped by scratch/site_scrape.py on " + datetime.date.today().isoformat() + ". Fields as rendered: sector tags (incl. the site's 'Exits' tag and region tags), 'Year Invested', short and full descriptions, the hidden country tag.",
           "rows": all_rows}, open("sources/site/portfolio-list-raw.json", "w"), indent=1, ensure_ascii=False)
print(len(all_rows))
