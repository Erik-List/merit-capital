"""Curate sources/wayback/partner-roster.json (decisions.md D6): the investing
people only, with capture-year tenure windows. Sources: the live team page's
investment teams and Management Team (2026), the archived 2017-2019 team pages
(Common Crawl captures), the three 2023 Form D filings' related persons, the ADV
Schedule A. Operations, legal, finance, people, communications and
portfolio-success staff are left out."""
import glob, html as H, json, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; INV = HERE.parent; ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic
INVEST = {"AI & Infra","Climate Tech & Industrial Tech","Deep Tech","Fintech & DeFi","Growth","Health & Bio",
          "Marketplaces & Consumer","Middle East, Africa & Beyond","Management Team"}
INVEST_TITLE = re.compile(r"Partner|Investor|Principal|Associate|Analyst|CEO|Founder|Managing|Venture|Investment", re.I)
NOT_INVEST_TITLE = re.compile(r"Office Manager|^COO$|^Chairman$|Legal|Counsel|Account|Finance|People|Talent|Communication|Brand|Event|Compliance|Controll|Engineer|Assistant|Operations|Reporting|Capital Formation|Chief of Staff|Portfolio Success", re.I)
people = defaultdict(lambda: {"years": set(), "sources": set(), "titles": set()})
def slug(n): return re.sub(r"[^a-z0-9]+", "-", H.unescape(n).lower().replace("ü","u").replace("ö","o").replace("ä","a").replace("é","e").replace("ß","ss")).strip("-")
for r in json.load(open(INV / "sources/site/team-cards-raw.json"))["rows"]:
    if set(r["tags"]) & INVEST and not NOT_INVEST_TITLE.search(r["title"]):
        p = people[slug(r["name"])]; p["name"] = r["name"]; p["years"].add(2026); p["titles"].add(r["title"])
        p["sources"].add("www.speedinvest.com/team, investment team '" + "/".join(sorted(set(r['tags']) & INVEST)) + "' (read 2026-09-30)")
# archived team pages
raw = ROOT / "data/filings/commoncrawl/speedinvest"
for f in sorted(glob.glob(str(raw / "*/*-team.html"))):
    ts = Path(f).name[:8]; yr = int(ts[:4])
    s = open(f, errors="replace").read()
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    lines = [l.strip() for l in H.unescape(re.sub(r"<[^>]+>", "\n", body)).split("\n") if l.strip()]
    for i in range(len(lines) - 2):
        # card shape: Name / Initials / Name / Title
        if lines[i] == lines[i + 2] and re.fullmatch(r"[A-ZÄÖÜ][a-z]{1,3}", lines[i + 1]) and i + 3 < len(lines):
            name, title = lines[i], lines[i + 3]
            if not re.fullmatch(r"[A-ZÄÖÜ][\w\-äöüßéü'. ]+ [A-ZÄÖÜ][\w\-äöüßéü'. ]+", name):
                continue
            if INVEST_TITLE.search(title) and not NOT_INVEST_TITLE.search(title):
                p = people[slug(name)]; p.setdefault("name", name); p["years"].add(yr); p["titles"].add(title)
                p["sources"].add(f"archived speedinvest.com/team ({ts[:4]}, Common Crawl)")
FORMD = ["Daniel Keiper-Knorr","Oliver Holle","Mathias Ockenfels","Werner Zahnt","Michael Sieghart","Jorg Flock",
         "Marie-Helene Ametsreiter","Andrea Zitna","Olga Shikhantsova","Jeroen Arts","Markus Lang","Andreas Schwarzenbrunner","Rick Hao"]
for n in FORMD:
    k = slug(n).replace("jorg", "jorg")
    if k == "jorg-flock" and "joerg-flock" in people: k = "joerg-flock"
    p = people[k]; p.setdefault("name", n); p["years"].add(2023)
    p["sources"].add("Form D related person, Speedinvest IV / Opportunity I / Industry & Climate Opportunity EuVECA (filed 2023-02-03)")
for n in ["Oliver Holle", "Daniel Keiper-Knorr"]:
    p = people[slug(n)]; p["years"].update(range(2011, 2027))
    p["sources"].add("Form ADV Schedule A, CRD 316774: Manager, Founding Partner since 05/2011 (annual amendment 2026-04-01)")
out = []
for k, p in sorted(people.items()):
    ys = sorted(p["years"])
    out.append({"slug": k, "name": p["name"], "years_seen": ys, "first_seen": ys[0], "last_seen": ys[-1],
                "snapshots": len(p["sources"]), "sources": sorted(p["sources"]), "basis": "; ".join(sorted(p["titles"])) or "Form D related person"})
write_atomic(INV / "sources/wayback/partner-roster.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(len(out)); [print(r["name"], r["first_seen"], r["last_seen"], r["basis"][:60]) for r in out]
