"""Give each Getro board row the live site's rendering of the same company where
the two share a website domain (identity by domain, not by name), keeping the
board's own spelling as board_name. Rewrites sources/site/jobboard-companies.json
in place (idempotent)."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; INV = HERE.parent
sys.path.insert(0, str(INV.parents[3] / "scripts"))
from paths import write_atomic
dom = lambda u: re.sub(r"^(https?://)?(www\.)?", "", (u or "").lower()).split("/")[0].strip()
site = json.load(open(INV / "sources/site/companies-2026.json"))["rows"]
by_dom = {}
for r in site:
    d = dom(r.get("website"))
    if d:
        by_dom.setdefault(d, r["name"])
p = INV / "sources/site/jobboard-companies.json"
b = json.load(open(p))
n = 0
for r in b["rows"]:
    r.setdefault("board_name", r["name"].strip())
    d = dom(r.get("url"))
    if d in by_dom and by_dom[d] != r["name"]:
        r["name"] = by_dom[d]; n += 1
    else:
        r["name"] = r["board_name"]
b["_readme"] = b["_readme"].split(" Board rows sharing")[0] + " Board rows sharing a website domain with a live-site row carry the site's rendering as name (scratch/board_align.py); board_name keeps the board's own."
write_atomic(p, json.dumps(b, indent=1, ensure_ascii=False))
print(n, "board rows renamed to the site's rendering")
