#!/usr/bin/env python3
"""Look for an address on a company's own website (homepage, /contact, /about): lines naming a
known city or a postcode. Evidence for hq_city, cited to the page. Usage: site-city.py slug..."""
import json, re, subprocess, sys, html
from pathlib import Path
H = Path(__file__).resolve().parent
site = {r["url"].rsplit("/", 1)[1]: r for r in json.load(open(H.parent / "sources" / "site" / "companies-list.json"))["rows"]}
CITIES = r"(Stockholm|Gothenburg|Göteborg|Malmö|Uppsala|Oslo|Bergen|Trondheim|Copenhagen|København|Aarhus|Aalborg|Helsinki|Espoo|Tallinn|London|Cambridge|Oxford|Manchester|Edinburgh|Bristol|Berlin|Munich|München|Hamburg|Cologne|Frankfurt|Freiburg|Amsterdam|Rotterdam|Utrecht|Paris|Lyon|Madrid|Barcelona|Valencia|Lisbon|Milan|Prague|Praha|Zurich|Zürich|Dublin|Warsaw|Istanbul|Dubai|New York|Brooklyn|San Francisco|Palo Alto|Oakland|Los Angeles|Boston|Cambridge, MA|Austin|Seattle|Chicago|Miami|Denver|Toronto|Richmond)"
for slug in sys.argv[1:]:
    w = (site.get(slug) or {}).get("website")
    if not w:
        print(slug, "no website"); continue
    base = re.match(r"https?://[^/]+", w).group(0)
    found = []
    for path in ("", "/contact", "/about", "/imprint", "/impressum", "/legal"):
        r = subprocess.run(["curl", "-sL", "--max-time", "20", "-A", "Mozilla/5.0", base + path], capture_output=True)
        t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", r.stdout.decode("utf-8", "replace"), flags=re.S)))
        t = re.sub(r"\s+", " ", t)
        for m in re.finditer(r"[^.|•]{0,80}\b" + CITIES + r"\b[^.|•]{0,60}", t):
            s = m.group(0).strip()
            if re.search(r"\d", s) and s not in found:
                found.append((path or "/", s[:150]))
        if len(found) >= 3:
            break
    print(slug, base, found[:3])
