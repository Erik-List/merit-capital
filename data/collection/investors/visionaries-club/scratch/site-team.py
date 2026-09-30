#!/usr/bin/env python3
"""Parse the live visionaries.vc team section into sources/site/team-cards.json.

Each `div.team__member` carries the person's LinkedIn link (the card's own
anchor), name, position and a bio paragraph. Read 2026-09-30 from
sources/site/home.html. Usage: python3 site-team.py
"""
import html, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
SITE = HERE.parent / "sources" / "site"
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

def txt(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()

h = (SITE / "home.html").read_text(encoding="utf-8", errors="replace")
rows = []
for it in re.split(r'<div class="team__member" ', h)[1:]:
    name = re.search(r'team__member-name[^"]*">(.*?)</div>', it, re.S)
    if not name:
        continue
    pos = re.search(r'team__member-position[^"]*">(.*?)</div>', it, re.S)
    link = re.search(r'<a href="([^"]+)" class="team__member-link"', it)
    bio = re.search(r'team__member-content[^"]*">(.*?)</div>', it, re.S)
    rows.append({"name": txt(name.group(1)), "title": txt(pos.group(1)) if pos else "",
                 "url": "https://www.visionaries.vc/#team",
                 "linkedin_url": link.group(1) if link and "linkedin" in link.group(1) else "",
                 "bio": txt(bio.group(1)) if bio else ""})
write_atomic(SITE / "team-cards.json", json.dumps({"_readme": __doc__, "read": "2026-09-30", "rows": rows}, indent=1, ensure_ascii=False) + "\n")
for r in rows:
    print(r["name"], "|", r["title"], "|", r["linkedin_url"])
