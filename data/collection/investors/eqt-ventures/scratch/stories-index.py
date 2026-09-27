#!/usr/bin/env python3
"""Index the firm's announcement archive (sources/site/stories.json) per
company, for the evidence packs. For each post: the ISO date, the companies it
names (matched against the candidate names of the site and archive layers,
word-bounded), the round words and amounts in the sentences that name each
company, lead language ("led", "co-led", "participat"), and the EQT fund the
post speaks for ("EQT Ventures" / "EQT Growth" / "Scaleup Europe Fund").
A post is class 1 for the round it NAMES; it asserts an entry only where it
says so in words (COLLECTION.md s6, Menlo). Output: ../sources/site/stories-index.json
"""
import json, re, sys, glob
from datetime import datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
S = HERE.parent / "sources" / "site"
rows = json.loads((S / "stories.json").read_text())["rows"]
names = {}
for r in json.loads((S / "companies-eqtgroup.json").read_text())["rows"]:
    names[r["name"]] = r["name"]
for f in glob.glob(str(HERE.parent / "sources/wayback/parsed/*.json")):
    for r in json.loads(Path(f).read_text()):
        if r.get("name"):
            names.setdefault(r["name"], r["name"])
extra = sys.argv[1:]
for n in extra:
    names[n] = n
ROUND = re.compile(r"(?i)\b(pre-?seed|seed(?: extension)?|series [a-h]\+?|series seed|growth round|bridge|extension|follow-on|secondary|crossover|IPO)\b")
AMT = re.compile(r"(?i)(?:[$€£]|USD |EUR |SEK )\s?\d[\d.,]*\s?(?:m|mn|million|bn|b|billion)\b|\d[\d.,]*\s?(?:million|billion) (?:euros|dollars|USD|EUR)")
def iso(d):
    for f in ("%b %d, %Y", "%B %d, %Y", "%b %d %Y"):
        try: return datetime.strptime(d.replace("Sept", "Sep"), f).date().isoformat()
        except (ValueError, AttributeError): pass
    return None
out = []
for r in rows:
    text = r["text"]
    # the article body sits between the header block and the footer ("More to read")
    body = text.split("More to read")[0]
    sents = re.split(r"(?<=[.!?])\s+(?=[A-Z“\"])|\n", body)
    fund = ("scaleup_europe" if re.search(r"Scaleup Europe Fund", body) else
            "growth" if re.search(r"EQT Growth (?:led|co-led|is leading|invest|particip|back)", body) else
            "ventures" if re.search(r"EQT Ventures", body) else None)
    hits = {}
    for n in names:
        if len(n) < 3: continue
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(n) + r"(?![A-Za-z0-9])", re.I if len(n) > 5 else 0)
        ss = [s.strip() for s in sents if pat.search(s)]
        if not ss and not pat.search(r["title"] or ""):
            continue
        rel = [s for s in ss if ROUND.search(s) or AMT.search(s) or re.search(r"(?i)\b(led|co-led|lead|invest|backing|backed|particip|acqui)", s)]
        hits[n] = {"n_mentions": len(ss), "in_title": bool(pat.search(r["title"] or "")),
                   "round_words": sorted({m.group(0) for s in rel for m in ROUND.finditer(s)}),
                   "amounts": sorted({m.group(0) for s in rel for m in AMT.finditer(s)}),
                   "sentences": rel[:6]}
    out.append({"url": r["url"], "title": re.sub(r"\s*\|\s*EQT.*$", "", r["title"] or ""), "date": iso(r["date_text"]),
                "fund_voice": fund, "companies": hits})
write_atomic(S / "stories-index.json", json.dumps({"_readme": __doc__, "posts": out}, indent=1, ensure_ascii=False))
print(len(out), "posts;", sum(1 for p in out if p["companies"]), "name a candidate")
