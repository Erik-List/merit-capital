"""Sweep roster for the Form D related-person sweep, rebuilt 2026-10-06.

Sources: the live team CMS (sources/site/team.json, investing bucket), the
capture-year windows of /team/<slug> pages read off the CDX index
(scratch/wb/inventory-foundersfund.com.json), the 2010 portfolio.php team menu,
and dated press for departures. Replaces scratch/bootstrap-roster.py, which
read /tmp files that no longer exist. Tenure is corroboration: every seat is
judged on its own date (COLLECTION.md s1, seat dating)."""
import json, re, sys, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic
p = Paths("founders-fund")
inv = json.loads((p.root / "scratch/wb/inventory-foundersfund.com.json").read_text())
cap = collections.defaultdict(set)
for y0, y1, key, ts, orig, mime, sc, dig in inv:
    m = re.match(r"^/team/([a-z0-9-]+)/?$", re.sub(r"^[^)]*\)", "", key).split("?")[0])
    if m and sc == "200":
        cap[m.group(1)].add(int(ts[:4]))
team = json.loads((p.root / "sources/site/team.json").read_text())
roster = {}
def add(name, first, last, sources, basis, slug=None):
    slug = slug or re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    roster[slug] = {"slug": slug, "name": name, "years_seen": [first, last], "first_seen": first,
                    "last_seen": last, "snapshots": 1, "sources": sources, "basis": basis}
for t in team:
    if "investing" not in (t.get("role_bucket") or []):
        continue
    first = min([int(t["date"][:4])] + sorted(cap.get(t["slug"], [])))
    if t["name"] == "Peter Thiel":
        first = 2005
    add(t["name"], first, 2026, [t["url"], "https://foundersfund.com/wp-json/wp/v2/team?per_page=100"],
        "Current investing title on the live site; start year is the earlier of the CMS post date and the first /team/ capture.", t["slug"])
FORMER = [
    ("Dave McClure", 2008, 2010, "https://wellfound.com/p/davemcclure"),
    ("Ken Howery", 2005, 2019, "https://en.wikipedia.org/wiki/Ken_Howery"),
    ("Luke Nosek", 2005, 2017, "https://www.axios.com/2017/12/15/founders-fund-partner-leaves-to-launch-spacex-focused-fund-1513304489"),
    ("Sean Parker", 2006, 2014, "https://fortune.com/2014/03/06/sean-parker-formally-leaves-founders-fund/"),
    ("Brian Singerman", 2008, 2024, "https://en.wikipedia.org/wiki/Brian_Singerman"),
    ("Geoff Lewis", 2012, 2017, "https://techcrunch.com/2017/08/21/geoff-lewis-left-founders-fund/"),
    ("Cyan Banister", 2016, 2020, "https://techcrunch.com/2020/03/02/cyan-banister-leaves-founders-fund-for-long-journey-ventures/"),
    ("Keith Rabois", 2019, 2024, "https://www.forbes.com/sites/alexkonrad/2024/01/09/keith-rabois-surprise-return-khosla-ventures-from-founders-fund/"),
    ("Kevin Hartz", 2016, 2018, "https://www.axios.com/2018/06/07/kevin-hartz-leaves-founders-fund-1528400235"),
    ("Bruce Gibney", 2005, 2012, "https://en.wikipedia.org/wiki/Founders_Fund"),
    ("Justin Fishner-Wolfson", 2008, 2011, "https://en.wikipedia.org/wiki/Founders_Fund"),
    ("Stephen Oskoui", 2015, 2017, "https://en.wikipedia.org/wiki/Founders_Fund"),
    ("Ryan Petersen", 2022, 2023, "https://en.wikipedia.org/wiki/Founders_Fund"),
    # added 2026-10-06 from the archived team pages (capture years in the basis)
    ("Aaron VanDevender", 2011, 2018, "https://web.archive.org/web/2013/http://www.foundersfund.com/team/aaron-vandevender"),
    ("Zachary Hargreaves", 2016, 2019, "https://web.archive.org/web/2017/http://foundersfund.com/team/zachary-hargreaves/"),
    ("Everett Randle", 2020, 2021, "https://web.archive.org/web/2021/https://foundersfund.com/team/everett-randle/"),
    ("Leigh Marie Braswell", 2021, 2023, "https://web.archive.org/web/2022/https://foundersfund.com/team/leigh/"),
    ("Sam Blond", 2022, 2024, "https://web.archive.org/web/2023/https://foundersfund.com/team/sam-blond/"),
    ("Michael Polansky", 2009, 2010, "https://web.archive.org/web/2010/http://foundersfund.com/portfolio.php"),
    ("Derik Pridmore", 2008, 2011, "https://web.archive.org/web/2010/http://foundersfund.com/portfolio.php"),
    ("Alda Leu Dennis", 2006, 2012, "https://web.archive.org/web/2010/http://foundersfund.com/portfolio.php"),
]
for name, first, last, url in FORMER:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    caps = sorted(cap.get(slug, []) or cap.get(slug.split("-")[0], []) if name == "Leigh Marie Braswell" else cap.get(slug, []))
    add(name, first, last, [url],
        "Former investing team member; search target only. Team-page capture years in the index: "
        f"{caps or 'none (pre-WordPress site or uncaptured)'}. Tenure is corroboration; every seat is judged on its own date, and a retained board proves no new investment.")
out = sorted(roster.values(), key=lambda t: t["slug"])
write_atomic(p.wayback / "partner-roster.json", json.dumps(out, indent=2) + "\n")
print(len(out), "sweep targets:", ", ".join(f"{t['name']} {t['first_seen']}-{t['last_seen']}" for t in out))
