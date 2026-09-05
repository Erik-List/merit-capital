#!/usr/bin/env python3
"""Curate the 2006-2011 investing staff into partner-roster.json (decisions.md D8).

partner-roster.py enumerates dash-separated profile slugs (2012+ WordPress and
Webflow namespaces). The earlier eras used /team/<first>_<last>.html (2006-07,
static), /team/bio/<firstlast> and /index.php/team/bio/<firstlast> (2008-2011,
ExpressionEngine), which the slug rule cannot read. This script asks the CDX
index for those namespaces, maps each early slug to its canonical dash slug and
merges the capture years in (extending first_seen / years_seen / snapshots), so
the tenure filter in build-company-base.py sees the whole window. Re-run after
every partner-roster.py run (that script rewrites the file wholesale).
"""
import json, re, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic
import shared_throttle

P = Paths("spark-capital")
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
EARLY = {  # early-era slug -> (canonical slug, display name)
    "paul_conway": ("paul-conway", "Paul Conway"), "paulconway": ("paul-conway", "Paul Conway"),
    "bijan_sabet": ("bijan-sabet", "Bijan Sabet"), "bijansabet": ("bijan-sabet", "Bijan Sabet"),
    "alex_finkelstein": ("alex-finkelstein", "Alex Finkelstein"), "alexfinkelstein": ("alex-finkelstein", "Alex Finkelstein"),
    "dennis_a_miller": ("dennis-miller", "Dennis Miller"), "dennismiller": ("dennis-miller", "Dennis Miller"),
    "todd_dagres": ("todd-dagres", "Todd Dagres"), "todddagres": ("todd-dagres", "Todd Dagres"),
    "santo_politi": ("santo-politi", "Santo Politi"), "santopoliti": ("santo-politi", "Santo Politi"),
    "scott_borenstein": ("scott-borenstein", "Scott Borenstein"),
    "moshekoyfman": ("mo-koyfman", "Mo Koyfman"), "mokoyfman": ("mo-koyfman", "Mo Koyfman"),
    "robertgo": ("robert-go", "Robert Go"),
    "andrew_parker": ("andrew-parker", "Andrew Parker"),
    "charles_huang": ("charles-huang", "Charles Huang"),
    "david_haber": ("david-haber", "David Haber"),
    "nabeel_hyatt": ("nabeel-hyatt", "Nabeel Hyatt"),
}
def cdx(pattern):
    # the CDX endpoint refuses connections under load (rc 7); retry with backoff
    for attempt in range(5):
        shared_throttle.wait("ia")
        r = subprocess.run(["curl", "-sfL", "--max-time", "120", "-H", f"User-Agent: {UA}",
            f"http://web.archive.org/cdx/search/cdx?url={pattern}&output=text&filter=statuscode:200&fl=original,timestamp&limit=20000"],
            capture_output=True)
        rows = [l.split() for l in r.stdout.decode("utf-8", "replace").splitlines() if len(l.split()) == 2]
        if r.returncode == 0 and rows:
            return rows
        print(f"  cdx {pattern}: rc={r.returncode}, {len(rows)} rows; retry {attempt+1}", file=sys.stderr)
        time.sleep(8 * (attempt + 1))
    return []
years = defaultdict(set); hits = defaultdict(int)
for pat in ("sparkcapital.com/team/bio/*", "sparkcapital.com/index.php/team/bio/*", "sparkcapital.com/team/*"):
    for orig, ts in cdx(pat):
        path = orig.split("?")[0]
        m = re.search(r"/team/(?:bio/)?([a-z][a-z0-9_]*[a-z0-9])(?:\.(?:html|php))?/?$", path)
        if not m or m.group(1).endswith(("_text", "_print", "_pic")):
            continue
        slug = m.group(1)
        if slug in EARLY:
            canon, _ = EARLY[slug]
            years[canon].add(ts[:4]); hits[canon] += 1
    time.sleep(0.5)
rows = json.load(open(P.wayback / "partner-roster.json"))
by = {r["slug"]: r for r in rows}
added = extended = 0
for canon, ys in sorted(years.items()):
    name = next(n for s, (c, n) in EARLY.items() if c == canon)
    if canon in by:
        r = by[canon]; before = r["first_seen"]
        r["years_seen"] = sorted(set(r["years_seen"]) | {int(y) for y in ys})
        r["first_seen"], r["last_seen"] = r["years_seen"][0], r["years_seen"][-1]
        r["snapshots"] += hits[canon]
        if "cdx-early-era-curated" not in r["sources"]: r["sources"].append("cdx-early-era-curated")
        extended += 1
    else:
        yl = sorted(int(y) for y in ys)
        rows.append({"slug": canon, "name": name, "years_seen": yl, "first_seen": yl[0], "last_seen": yl[-1],
                     "snapshots": hits[canon], "sources": ["cdx-early-era-curated"]})
        added += 1
rows.sort(key=lambda r: r["slug"])
write_atomic(P.wayback / "partner-roster.json", json.dumps(rows, indent=1) + "\n")
print(f"early eras: {len(years)} people seen ({added} added, {extended} extended)")
for canon in sorted(years): print(f"  {canon}: {sorted(years[canon])} ({hits[canon]} captures)")
