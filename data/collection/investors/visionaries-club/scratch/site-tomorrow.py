#!/usr/bin/env python3
"""Parse the live tomorrow.vc portfolio ("The Change Makers" carousel) into
sources/site/companies-tomorrow-2026.json.

tomorrow.vc is VISIONARIES TOMORROW, the firm's industrial deep-tech fund
(Visionaries Club Tomorrow Fund I GmbH & Co. KG, a private fund on Visionaries
Club GmbH's own Form ADV, CRD 317147; decisions.md D1). The page is a Svelte
build whose first carousel lists the fund's companies: one `carousel-slide`
per company with the company's domain, name, a one-line claim and (mostly) a
link to its site. Read 2026-09-30 from sources/site/tomorrow-home.html.
Usage: python3 site-tomorrow.py
"""
import html, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
SITE = HERE.parent / "sources" / "site"
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

def txt(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()

h = (SITE / "tomorrow-home.html").read_text(encoding="utf-8", errors="replace")
start = h.find("THE CHANGE MAKERS")
end = h.find("UNPACKING THE FUTURE", start)
seg = h[start:end]
rows = []
for sl in re.split(r'<div class="carousel-slide [^>]*>', seg)[1:]:
    t = txt(sl)
    links = [u for u in re.findall(r'href="(https?://[^"]+)"', sl)]
    parts = [p.strip() for p in re.split(r"\s{2,}|\|", re.sub(r"<[^>]+>", "|", sl)) if p.strip()]
    parts = [html.unescape(p) for p in parts if not p.startswith("<!") and p not in ("visit",)]
    parts = [p for p in parts if re.search(r"[A-Za-z]", p) and not re.match(r"^[\w\-]+\.(com|ai|inc|io|energy)$", p)]
    if not parts:
        continue
    name, claim = parts[0], (parts[1] if len(parts) > 1 else "")
    rows.append({"name": name, "claim": claim, "website": links[0] if links else "",
                 "url": "https://tomorrow.vc/", "fund_site": "Visionaries Tomorrow"})
write_atomic(SITE / "companies-tomorrow-2026.json",
             json.dumps({"_readme": __doc__, "source_url": "https://tomorrow.vc/", "read": "2026-09-30", "rows": rows},
                        indent=1, ensure_ascii=False) + "\n")
for r in rows:
    print(r)
