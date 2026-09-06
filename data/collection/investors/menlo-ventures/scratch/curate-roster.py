#!/usr/bin/env python3
"""Merge the pre-2012 roster into sources/wayback/partner-roster.json.

partner-roster.py's CDX enumeration requires a "first-last" slug shape (it
drops any slug without a hyphen, which is what keeps a namespace's non-person
pages out). Menlo's two early people namespaces do not have that shape --
/m_<lastname>.html (1997-2001) and /management/<initial><lastname>.html
(2002-2007) -- so the automatic roster starts in 2012 and structurally misses
fifteen years of partners, including everyone who left before the WordPress
site. They are curated here from the firm's own archived index pages, which
name them in full with their titles, exactly as COLLECTION.md 5 prescribes
when a roster layer cannot see a period ("curated from the ADV, Form D related
persons and press with press-dated tenure windows").

Sources, all captures of menloventures.com:
  /management.html      2000-03-02  (11 partners, linked as /m_<name>.html)
  /management/          2003-04-02  (15 names with titles)
  /team_bio.html        2009-03-01  (17 names by group)
plus the CDX index of both namespaces for the capture years per person.

Run after partner-roster.py; it is idempotent and never lowers a tenure
window the automatic pass found.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

# name, slug, first_seen, last_seen, role, board-relevant
EARLY = [
    ("H. DuBose Montgomery", "h-dubose-montgomery", 1997, 2026, "Founder, Managing Director", True),
    ("Douglas C. Carlisle", "douglas-c-carlisle", 1997, 2026, "Managing Director", True),
    ("John W. Jarve", "john-w-jarve", 1997, 2026, "Managing Director", True),
    ("Thomas H. Bredt", "thomas-h-bredt", 1997, 2009, "Managing Director, later Venture Advisor", True),
    ("Sonja L. Hoel", "sonja-l-hoel", 1997, 2011, "Managing Director", True),
    ("Sonja Hoel Perkins", "sonja-h-perkins", 2009, 2011, "Managing Director (married name on the 2009 page)", True),
    ("Mark A. Siegel", "mark-a-siegel", 1997, 2026, "Managing Director", True),
    ("Hal Calhoun", "hal-calhoun", 2000, 2011, "Managing Director", True),
    ("Michael D. Laufer, M.D.", "michael-d-laufer", 1999, 2002, "Managing Director (medical devices)", True),
    ("Christopher W. Kersey", "christopher-w-kersey", 1999, 2002, "Principal", True),
    ("Hilary E. Hoover", "hilary-e-hoover", 1999, 2002, "Associate", True),
    ("Ann M. Carney", "ann-m-carney", 2000, 2005, "Associate", True),
    ("Arvind Purushotham", "arvind-purushotham", 2001, 2011, "Managing Director", True),
    ("Pravin A. Vazirani", "pravin-a-vazirani", 2001, 2015, "Managing Director", True),
    ("Shawn T. Carolan", "shawn-t-carolan", 2002, 2026, "Managing Director", True),
    ("Daniel E. Kacher", "daniel-e-kacher", 2000, 2005, "Investment Analyst", True),
    ("Brent W. Dusing", "brent-w-dusing", 2002, 2005, "Investment Analyst", True),
    ("Adam Marchick", "adam-marchick", 2004, 2007, "Associate", True),
    ("Chris C. Mason", "chris-c-mason", 2007, 2011, "Associate", True),
    ("Vineet Mehta", "vineet-mehta", 2009, 2011, "Analyst", True),
    ("Tyler V. Sosin", "tyler-v-sosin", 2009, 2026, "Analyst, later Partner", True),
    ("E. McCleneghan", "e-mccleneghan", 2006, 2007, "Associate", True),
    ("Catherine C. Shaw", "catherine-c-shaw", 2000, 2011, "Finance (not an investing seat)", False),
    ("Kirsten A. Mello", "kirsten-a-mello", 2002, 2026, "Finance (not an investing seat)", False),
    ("Amy R. Biagini", "amy-r-biagini", 2007, 2015, "Finance (not an investing seat)", False),
]
BASIS = ("Curated from the firm's own archived index pages: /management.html "
         "(2000-03-02), /management/ (2003-04-02) and /team_bio.html (2009-03-01), "
         "plus the CDX index of the /m_<name>.html and /management/<slug>.html "
         "namespaces. partner-roster.py cannot enumerate either namespace because "
         "neither slug carries the first-last hyphen shape its filter requires.")


def main() -> None:
    p = Paths("menlo-ventures")
    f = p.wayback / "partner-roster.json"
    rows = json.loads(f.read_text())
    by_slug = {r["slug"]: r for r in rows}
    rows = [r for r in rows if r["slug"] != "photo-download.html"]
    by_slug.pop("photo-download.html", None)
    added = updated = 0
    for name, slug, y0, y1, role, board in EARLY:
        r = by_slug.get(slug)
        if r is None:
            r = {"slug": slug, "name": name, "years_seen": [y0, y1],
                 "first_seen": y0, "last_seen": y1, "snapshots": 0,
                 "sources": ["site-archive-curated"], "role": role,
                 "board_relevant": board, "basis": BASIS}
            rows.append(r)
            by_slug[slug] = r
            added += 1
        else:
            r["first_seen"] = min(r.get("first_seen") or y0, y0)
            r["last_seen"] = max(r.get("last_seen") or y1, y1)
            r["years_seen"] = sorted(set((r.get("years_seen") or []) + [y0, y1]))
            r.setdefault("role", role)
            r["board_relevant"] = board
            r["basis"] = (r.get("basis", "") + " " + BASIS).strip()
            if "site-archive-curated" not in r["sources"]:
                r["sources"].append("site-archive-curated")
            updated += 1
    rows.sort(key=lambda r: (r.get("first_seen") or 9999, r["slug"]))
    write_atomic(f, json.dumps(rows, indent=1) + "\n")
    print(f"roster: {len(rows)} people   curated added: {added}   merged: {updated}")


if __name__ == "__main__":
    main()
