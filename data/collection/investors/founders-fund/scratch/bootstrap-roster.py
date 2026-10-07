"""Build a conservative sweep roster, retaining explicit tenure provenance.

Current CMS publication is a latest-known join bound, not a hire date. The
sweep collects across all years; each resulting seat is judged on its date.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic

p = Paths("founders-fund")
raw = json.loads(Path("/tmp/founders-fund-inspect/team-page1.json").read_text())
roster = []
for t in raw:
    title = t["subtitle"]
    if title not in ("Partner", "Associate"):
        continue
    name = t["title"]["rendered"]
    first = 2005 if name == "Peter Thiel" else int(t["date"][:4])
    roster.append({"slug": t["slug"], "name": name,
                   "years_seen": [first, 2026], "first_seen": first,
                   "last_seen": 2026, "snapshots": 1,
                   "sources": [t["link"], "https://foundersfund.com/wp-json/wp/v2/team?per_page=100"],
                   "basis": "Current investing title. CMS publication year is only a latest-known start bound; earlier filings require individual tenure verification."})

former = [
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
    ("Ryan Petersen", 2023, 2023, "https://en.wikipedia.org/wiki/Founders_Fund"),
]
for name, first, last, url in former:
    roster.append({"slug": name.lower().replace(" ", "-"), "name": name,
                   "years_seen": [first, last], "first_seen": first,
                   "last_seen": last, "snapshots": 1, "sources": [url],
                   "basis": "Former partner search target. Tenure is corroboration only; one snapshot deliberately prevents automatic ex-partner deletion before a judge inspects the seat. Retained boards do not prove a new investment."})
roster.sort(key=lambda t: t["slug"])
write_atomic(p.wayback / "partner-roster.json", json.dumps(roster, indent=2) + "\n")
print(f"{len(roster)} sweep targets written")
