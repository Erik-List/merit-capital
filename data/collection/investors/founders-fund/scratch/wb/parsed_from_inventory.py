"""Write sources/wayback/parsed/<year>.json from what is already on disk, so the
base does not wait on an Internet Archive block (2026-10-06: CDX answered the
inventory, then the replay host refused connections and the shared cooldown
doubled to two hours).

Reads: scratch/wb/inventory-*.json (CDX rows: urlkey, first timestamp per period)
       scratch/wb/raw/tff-portfolio-2009.html   thefoundersfund.com/portfolio.html
       scratch/wb/raw/ff-portfolio-php-2011.html foundersfund.com/portfolio.php
       scratch/wb/raw/ff-company-knewton-2013.html  any 2012-13 page: its menu lists
                                                    every company by category
Rows are keyed (slug, path) exactly as wayback-pull.py's eras write them, and the
year files MERGE with existing rows winning on everything but a missing name, so
the config-driven pull converges on the same files when the archive answers."""
import json, re, sys, collections
from html import unescape
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic
p = Paths("founders-fund")
W = p.root / "scratch/wb"
cfg = p.config()["wayback"]
NON = set(cfg["non_company_slugs"])
rows = collections.defaultdict(dict)   # year -> (slug, path) -> row
def put(year, slug, path, ts, name=None, capture_url=None):
    r = {"slug": slug, "path": path, "snapshot_ts": ts}
    if name: r["name"] = name
    if capture_url: r["capture_url"] = capture_url
    rows[year].setdefault((slug, path), r)

# --- the 2012-13 menu: names and categories for every listed company
menu = {}
h = (W / "raw/ff-company-knewton-2013.html").read_text(encoding="utf-8", errors="replace")
for blk in re.finditer(r'<li id="term-\d+" class="term[^"]*">\s*<a title="([^"]+)"(.*?)(?=<li id="term-\d+" class="term|</nav|$)', h, re.S):
    for s2, n2 in re.findall(r'/company/([a-z0-9_-]+)/?" title="([^"]*)"', blk.group(2)):
        menu.setdefault(s2, {"name": unescape(n2), "category": unescape(blk.group(1))})
inv = json.loads((W / "inventory-foundersfund.com.json").read_text())
knew = [(ts, orig) for y0, y1, key, ts, orig, mime, sc, dig in inv if re.search(r"\)/company/knewton/?$", key) and sc == "200" and ts.startswith(("2012", "2013"))]
menu_ts = sorted(knew)[0][0] if knew else "2013"
write_atomic(p.wayback / "site-menu-2013.json", json.dumps({
    "_readme": "The company menu every page of the 2012-2013 site carried, read off the capture of /company/knewton nearest 2013-06-01 (scratch/wb/raw/ff-company-knewton-2013.html). slug -> the site's own name and its menu group. 'FF Angel' is the firm's own label for a position of its angel vehicle; the judge reads it as corroboration for a seed-stage entry until it is scored (COLLECTION.md s5).",
    "capture": f"https://web.archive.org/web/20130601000000/http://www.foundersfund.com/company/knewton", "companies": menu}, indent=1) + "\n")

# --- /company/<slug> pages straight from the CDX inventory (one row per period captured)
for y0, y1, key, ts, orig, mime, sc, dig in inv:
    m = re.match(r"^/company/([a-z0-9_-]+)/?$", re.sub(r"^[^)]*\)", "", key).split("?")[0])
    if not m or sc != "200" or m.group(1) in NON:
        continue
    slug = m.group(1)
    put(int(ts[:4]), slug, f"/company/{slug}", ts, name=(menu.get(slug) or {}).get("name"))

# --- portfolio.php, 2009-2011: <li><a href="slug.php" class="red">Name</a></li>
php = [(ts, orig) for y0, y1, key, ts, orig, mime, sc, dig in inv if re.search(r"\)/portfolio\.php$", key) and sc == "200"]
php_ts = sorted(php)[0][0] if php else "20110101000000"
h = (W / "raw/ff-portfolio-php-2011.html").read_text(encoding="utf-8", errors="replace")
for slug, name in re.findall(cfg["eras"][1]["pattern"], h):
    put(int(php_ts[:4]), slug, "/portfolio.php", php_ts, name=unescape(name).strip(),
        capture_url=f"https://web.archive.org/web/{php_ts}/http://foundersfund.com/portfolio.php")

# --- thefoundersfund.com/portfolio.html, capture of 2009-01-26: the page's own
# paragraph names each company; the slug is the company's domain, as the era regex reads it
NAMES = {"collaborativedrug": "CDD", "engage": "Engage.com", "facebook": "Facebook", "geni": "Geni",
         "ironport": "IronPort", "jaxtr": "Jaxtr", "koders": "Koders", "ooma": "Ooma", "powerset": "Powerset",
         "quantcast": "Quantcast", "slide": "Slide", "smartdrive": "SmartDrive"}
h = (W / "raw/tff-portfolio-2009.html").read_text(encoding="utf-8", errors="replace")
found = [m.group("slug") for m in re.finditer(cfg["eras"][0]["pattern"], h)]
for slug in found:
    put(2009, slug, "/portfolio.html", "20090126000000", name=NAMES.get(slug),
        capture_url="https://web.archive.org/web/20090126000000/http://thefoundersfund.com/portfolio.html")
print("2009 portfolio.html:", found)

parsed = p.wayback / "parsed"; parsed.mkdir(parents=True, exist_ok=True)
total = set()
for y, rs in sorted(rows.items()):
    dest = parsed / f"{y}.json"
    merged = {(r["slug"], r.get("path")): r for r in (json.loads(dest.read_text()) if dest.exists() else [])}
    for k, r in rs.items():
        if k in merged:
            if r.get("name") and not merged[k].get("name"):
                merged[k]["name"] = r["name"]
        else:
            merged[k] = r
    write_atomic(dest, json.dumps(sorted(merged.values(), key=lambda r: (r["slug"], r.get("path") or "")), indent=1) + "\n")
    total |= {r["slug"] for r in merged.values()}
    print(y, len(merged), "rows,", sum(1 for r in merged.values() if r.get("name")), "named")
print("menu companies:", len(menu), collections.Counter(v["category"] for v in menu.values()))
print("distinct slugs in parsed files:", len(total))
