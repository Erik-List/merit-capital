#!/usr/bin/env python3
"""Rebuild sources/site/companies-framer.json and team-cards.json from the
20vc.fund Framer site (escalation ladder step 4: the rendered page carries 16
cards behind a client-side "Load More"; the whole collection ships as a Framer
CMS chunk).

The portfolio collection is the module
  https://framerusercontent.com/modules/bERmDTXK8P7cbh9Ly71G/hImXCJmFngL74mbqY5oj/YJbM8mTif.js
whose data chunk is the same path under /cms/ with -chunk-default-0.framercms.
The chunk is decoded by scratch/framercms.py; field ids are mapped to the
titles the module declares (Companies, Slug, One Liner, Sector, Sector 2,
URL, Exit Status, #). The team page renders every card server-side.

Usage: python3 data/collection/investors/20vc/scratch/site-from-framer.py [--fetch]
"""
import json, re, sys, html, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
import framercms  # noqa: E402

I = HERE.parent
RAW = I / "sources" / "site" / "raw"
CHUNK = RAW / "portfolio-YJbM8mTif-chunk-default-0.framercms"
MODULE_URL = "https://framerusercontent.com/modules/bERmDTXK8P7cbh9Ly71G/hImXCJmFngL74mbqY5oj/YJbM8mTif.js"
TEAM_HTML = ROOT / "data" / "filings" / "site-raw" / "20vc" / "team-2026-09-28.html"
SECTORS = {"U12FpddaG": "Artificial Intelligence", "oYtgVWPzW": "Fintech",
           "t3iIS2FiO": "Consumer", "vQD95ulpa": "Deep-tech", "sXMeIDar_": "Deep-tech",
           "DxAyK2grY": None}
FIELDS = {"TKx4vX3c1": "name", "GcgCCechW": "cms_slug", "L4P02KUYE": "one_liner",
          "uXmLpgANg": "sector_1", "ArFbVUqSa": "sector_2", "B3x6FmtlM": "website",
          "ySEkzFtEM": "exit_site", "nOZo7hoBK": "order", "createdAt": "cms_created",
          "updatedAt": "cms_updated", "id": "cms_id"}

if "--fetch" in sys.argv:
    url = MODULE_URL.replace("/modules/", "/cms/").replace(".js", "-chunk-default-0.framercms")
    subprocess.run(["curl", "-s", "--max-time", "60", "-o", str(CHUNK), url], check=True)

items, end = framercms.decode(CHUNK.read_bytes())
rows = []
for it in items:
    r = {FIELDS[k]: v for k, v in it.items() if k in FIELDS}
    secs = [SECTORS.get(it.get("uXmLpgANg")), SECTORS.get(it.get("ArFbVUqSa"))]
    r["sectors"] = sorted({s for s in secs if s})
    r["sector_1"] = SECTORS.get(r.get("sector_1"))
    r["sector_2"] = SECTORS.get(r.get("sector_2"))
    r["url"] = "https://20vc.fund/portfolio"
    w = r.get("website")
    r["website"] = w if isinstance(w, str) else ""
    r["exit_site"] = bool(r.get("exit_site"))
    rows.append(r)
rows.sort(key=lambda r: r["name"].lower())
out = {
    "_readme": ("20vc.fund/portfolio, the firm's live list (Framer CMS collection 'Portfolio', "
                f"{len(rows)} items), decoded from the collection's data chunk by "
                "scratch/site-from-framer.py on 2026-09-28. The page server-renders 16 cards "
                "behind a client-side Load More; the chunk is the whole collection. Fields: "
                "name, the firm's one-liner, its two sector enums (Artificial Intelligence, "
                "Fintech, Consumer, Deep-tech), the company URL, the firm's Exit flag, the "
                "CMS order number and the CMS record dates (cms_created is when the card was "
                "added to the site, NOT an investment date: 52 cards share 2024-09-12, the "
                "day the Framer site was built). No round word, no investment year."),
    "rows": rows,
}
(I / "sources" / "site" / "companies-framer.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(f"portfolio: {len(rows)} rows (chunk {end} bytes)")

# ---- team
t = TEAM_HTML.read_text(encoding="utf-8")
body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t.split("<body", 1)[1], flags=re.S)
toks = []
for m in re.finditer(r'<a [^>]*href="([^"]+)"|>([^<>]+)<', body):
    if m.group(1):
        toks.append(("L", m.group(1)))
    else:
        s = html.unescape(m.group(2)).strip()
        if s:
            toks.append(("T", s))
GROUPS = ("20GROWTH Partners", "20SALES Partners", "20Product Partners")
NOISE = {"✨", "Connect to Content", "Add layers or components to swipe between."}
team, group, i = [], "team", 0
start = next(k for k, (_, v) in enumerate(toks) if v == "Harry Stebbings")
k = start
while k < len(toks):
    kind, v = toks[k]
    if kind == "T" and v in GROUPS:
        group = v; k += 1; continue
    if kind == "T" and v in NOISE:
        k += 1; continue
    if kind == "T" and v.startswith("Contact us"):
        break
    if kind == "T":
        name = v
        org = toks[k + 1][1] if k + 1 < len(toks) and toks[k + 1][0] == "T" else ""
        title = toks[k + 2][1] if k + 2 < len(toks) and toks[k + 2][0] == "T" else ""
        links = []
        j = k + 3
        while j < len(toks) and toks[j][0] == "L":
            links.append(toks[j][1]); j += 1
        team.append({"name": name, "org": org, "title": title, "group": group,
                     "linkedin_url": next((l for l in links if "linkedin.com" in l), ""),
                     "x_url": next((l for l in links if "x.com/" in l or "twitter.com/" in l), ""),
                     "url": "https://20vc.fund/team"})
        k = j
        continue
    k += 1
(I / "sources" / "site" / "team-cards.json").write_text(json.dumps({
    "_readme": ("20vc.fund/team as served 2026-09-28 (raw page under data/filings/site-raw/20vc/). "
                "Group 'team' is the firm's own people; the 20GROWTH / 20SALES / 20Product groups "
                "are the operator partners of the AngelList-administered 20Growth, 20Sales and "
                "20Product funds, each shown with their OWN employer (Dropbox, Vanta, Ramp...), "
                "never swept as the firm's roster (decisions.md)."),
    "rows": team}, indent=1, ensure_ascii=False) + "\n")
print(f"team: {len(team)} cards:", {g: sum(1 for p in team if p['group'] == g) for g in {p['group'] for p in team}})
