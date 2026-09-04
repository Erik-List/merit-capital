#!/usr/bin/env python3
"""Extract the 2017-2023 creandum.com/portfolio data attributes (one snapshot per
year, first capture of the year) into sources/site/portfolio-2017-2023.json."""
import json, re, html, subprocess, sys, time
from pathlib import Path
S = Path(sys.argv[1]); OUT = Path(sys.argv[2])
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
def curl(url):
    for a in range(3):
        r = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA, url], capture_output=True)
        if r.returncode == 0 and r.stdout: return r.stdout.decode("utf-8", "replace")
        time.sleep(3)
    return ""
# CDX refused targeted queries at run time (2026-09-04); the playbook's outage path
# (COLLECTION.md §5) is year-targeted replay. The timestamps below are the captures the
# replay resolved for mid-year probes on the first pass (recorded so a rerun is
# deterministic); a year without one is probed again.
KNOWN = {2017: "20170621150411", 2019: "20190624202311", 2020: "20200524204104",
         2021: "20210116123630", 2022: "20221128045517", 2023: "20230129154423"}
cdx = []
for y in range(2017, 2024):
    ts = KNOWN.get(y)
    if not ts:
        for probe in (f"{y}0615", f"{y}0201", f"{y}1015"):
            r = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA, "-o", "/dev/null", "-w", "%{url_effective}",
                                f"http://web.archive.org/web/{probe}id_/http://www.creandum.com/portfolio"], capture_output=True)
            m = re.search(r"/web/(\d{14})id_/", r.stdout.decode())
            if m and m.group(1)[:4] == str(y): ts = m.group(1); break
            time.sleep(2)
    if ts: cdx.append((ts, "http://www.creandum.com/portfolio"))
# sprite ids that are not names (read off the 2017-2023 sprite; the live CMS rendering wins at build)
NAME_OVERRIDES = {"armada_interactive_black": "Armada Interactive", "kry_logo2": "Kry", "knl-2": "KNL Networks",
                  "ipt": "IPtronics", "resolution": "Resolution Games", "nonstopgames": "Nonstop Games",
                  "xtract": "Xtract", "cornershop": "Cornershop", "kahoot": "Kahoot!", "mitrionics": "Mitrionics",
                  "appear-tv": "Appear TV", "izettle": "iZettle", "justbook": "JustBook", "playraven": "PlayRaven",
                  "neo-technologies": "Neo Technology", "its-learning": "itslearning", "virta": "Virta Health",
                  "soundtrack-your-brand": "Soundtrack Your Brand", "13th-lab": "13th Lab"}
rows = {}
years_seen = []
for ts, orig in cdx:
    y = int(ts[:4]); dest = S / "wb" / f"{y}-portfolio-{ts}.html"
    old = S / "wb" / f"{y}-portfolio.html"
    h = dest.read_text(encoding="utf-8", errors="replace") if dest.exists() else (old.read_text(encoding="utf-8", errors="replace") if old.exists() else curl(f"http://web.archive.org/web/{ts}id_/{orig}"))
    if not dest.exists() and h: dest.write_text(h, encoding="utf-8"); time.sleep(1)
    items = []
    for m in re.finditer(r'<div class="cr-portfolio__item[^"]*"', h):
        end = h.find('<div class="cr-portfolio__logo">', m.end())
        items.append(h[m.end():end if end > 0 else m.end() + 4000])
    if not items: print("  no items in", y); continue
    years_seen.append(y)
    titles = dict(re.findall(r'<symbol[^>]*id="([^"]+)"[^>]*>\s*<title>([^<]*)</title>', h))
    n = 0
    for attrs in items:
        a = {k: (v1 or v2) for k, v1, v2 in re.findall(r'data-([a-z]+)=(?:"([^"]*)"|\'([^\']*)\')', attrs)}
        m = re.search(r'xlink:href="#([^"]+)"', a.get("logo", ""))
        if not m: continue
        slug = m.group(1); n += 1
        story = html.unescape(re.sub(r"<[^>]+>", " ", a.get("story", "")))
        r = rows.setdefault(slug, {"slug": slug, "name": NAME_OVERRIDES.get(slug) or html.unescape(titles.get(slug, "")).strip() or " ".join(w.capitalize() for w in slug.split("-")),
                                   "url": "", "invest_year": None, "founded": None, "partners": [], "status_site": None, "type": None, "ceo": None,
                                   "years_listed": [], "story": ""})
        r["years_listed"].append(y)
        r["url"] = r["url"] or a.get("url", "")
        if a.get("invested") and (r["invest_year"] is None or a["invested"] < r["invest_year"]): r["invest_year"] = a["invested"]
        r["founded"] = r["founded"] or a.get("founded")
        if a.get("partner") and a["partner"] not in r["partners"]: r["partners"].append(a["partner"])
        r["status_site"] = a.get("status") or r["status_site"]      # latest snapshot's status wins
        r["type"] = a.get("type") or r["type"]
        r["ceo"] = r["ceo"] or a.get("ceo")
        r["story"] = r["story"] or re.sub(r"\s+", " ", story)[:300]
    print(f"  {y}: {n} items ({ts})")
out = sorted(rows.values(), key=lambda r: r["slug"])
OUT.write_text(json.dumps({"_readme": f"creandum.com/portfolio (the 2017-2023 static site) read from one Wayback snapshot per year ({', '.join(map(str, years_seen))}; first capture of the year, raw id_ replay) on 2026-09-04: every cr-portfolio__item's data attributes — the sprite id (slug), data-invested (the firm's own investment year), data-partner, data-status (active/inactive at that snapshot; the latest wins), data-type (consumer/enterprise), data-founded, data-ceo, data-url — unioned by slug with the years each company was listed. No name element exists on that page: names come from the logo sprite's <title> where the sprite carried one, else from the slug. Regenerated by the PRO-72 scratch script portfolio-2017-2023.py (copied into scratch/).", "rows": out}, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {OUT}: {len(out)} companies; years {years_seen}")
import collections
print(" invest years:", sorted(collections.Counter(r['invest_year'] for r in out).items()))
print(" status:", collections.Counter(r['status_site'] for r in out), " with url:", sum(1 for r in out if r['url']))
print(" names from sprite titles:", sum(1 for r in out if r['name'] != ' '.join(w.capitalize() for w in r['slug'].split('-'))))

# name normalization of sprite ids lives in scratch/rename-2017-2023.py and runs after this script
