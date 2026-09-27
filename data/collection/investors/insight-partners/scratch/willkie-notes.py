#!/usr/bin/env python3
"""Deal notes of the firm's counsel (Willkie Farr & Gallagher), a layer found
during the control pass of 2026-09-27: the counsel publishes a short note for
most of the firm's transactions and states in words what the firm's own posts
often leave out (control investment, acquisition, majority, minority, the
round's name). Input: the counsel's sitemap. A note is pulled when its URL
names the firm, or names a company of the base (slug match, 5+ characters).
Output: sources/web/willkie-notes.json, one row per note with the base slugs
it matches, its title, date, first paragraphs and the control words found.
Usage: python3 .../scratch/willkie-notes.py <sitemap.xml>"""
import json, re, html, subprocess, sys, time
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
sm = open(sys.argv[1], errors="replace").read()
urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if "/news/" in u]
base = json.load(open(INV / "companies/base.json"))
rows = base["rows"] if isinstance(base, dict) and "rows" in base else base
GENERIC = {"insight", "partners", "capital", "software", "group", "health", "systems", "global", "network", "digital", "energy",
           "solutions", "technologies", "security", "analytics", "education", "financial", "american", "first", "united", "general",
           "class", "coast", "glass", "sweep", "spike", "unit", "slice", "turing", "valence", "genesis", "modus", "agora", "esper"}
keys = {}
for r in rows:
    nm = re.sub(r"\(.*?\)", "", r["name"]).strip().lower()
    k = re.sub(r"[^a-z0-9]+", "-", nm).strip("-")
    k = re.sub(r"-(inc|llc|ltd|corp|corporation|co|com|io|ai|holdings|group|software|technologies)$", "", k)
    if len(k) >= 5 and k not in GENERIC:
        keys.setdefault(k, []).append(r["slug"])
want = {}
for u in urls:
    slug = u.rstrip("/").split("/")[-1].lower()
    hit = [s for k, ss in keys.items() if re.search(rf"(^|-){re.escape(k)}(-|s-|$)", slug) for s in ss]
    if "insight" in slug or hit:
        want[u] = sorted(set(hit))
print(len(want), "notes to pull", file=sys.stderr)
out_p = INV / "sources/web/willkie-notes.json"
out = json.load(open(out_p))["rows"] if out_p.exists() else {}
CTRL = re.compile(r"control investment|controlling (?:stake|interest)|majority (?:stake|investment|interest|owner|share)|acquisition of|acquires?\b|acquired\b|"
                  r"take[- ]private|recapitali[sz]ation|buyout|leveraged", re.I)
MINO = re.compile(r"minority|growth equity|growth investment|series [a-k]\b|financing round|funding round|led the|lead investor", re.I)
n = 0
for u, hit in want.items():
    if u in out and out[u].get("http") == "200":
        out[u]["slugs"] = hit
        continue
    r = subprocess.run(["curl", "-sL", "-m", "30", "-A", UA, "-w", "\n%{http_code}", u], capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    t = re.sub(r"(?s)<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<footer.*?</footer>|<header.*?</header>", " ", body)
    title = re.search(r"(?s)<h1[^>]*>(.*?)</h1>", t)
    title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", title.group(1)))).strip() if title else ""
    paras = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", p))).strip() for p in re.findall(r"(?s)<p[^>]*>(.*?)</p>", t)]
    paras = [p for p in paras if len(p) > 60 and "cookie" not in p.lower()][:4]
    text = " ".join(paras)
    m = re.search(r"/news/(\d{4})/(\d{2})/", u)
    out[u] = {"url": u, "http": code, "date": f"{m.group(1)}-{m.group(2)}" if m else None, "title": title, "text": text[:1500],
              "slugs": hit, "names_firm": bool(re.search(r"insight (venture )?partners", title + " " + text, re.I)),
              "control_words": sorted({x.group(0).lower() for x in CTRL.finditer(title + " " + text)}),
              "minority_words": sorted({x.group(0).lower() for x in MINO.finditer(title + " " + text)})}
    n += 1
    if n % 25 == 0:
        print(n, file=sys.stderr, flush=True)
        json.dump({"_readme": __doc__, "rows": out}, open(out_p, "w"), indent=1, ensure_ascii=False)
    time.sleep(0.7)
json.dump({"_readme": __doc__, "rows": out}, open(out_p, "w"), indent=1, ensure_ascii=False)
print(len(out), "notes on file;", sum(1 for x in out.values() if x.get("names_firm")), "name the firm")
