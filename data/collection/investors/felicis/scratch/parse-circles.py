#!/usr/bin/env python3
"""Recover the firm's own round ladder from the 2011-2019 WordPress listings.

Each card on felicis.com/portfolio/ in that era is

    <div class="span3">
      <a href="<company site>" class="thumbnail">
        <div class="logo-container">
          <img src="/wp-content/themes/felicis/images/logos/<slug>.png" alt="Name" />
        </div>
        <p class="circles"><span>Seed</span><span>a</span></p>
      </a>
    </div>

and the `circles` are the rounds Felicis itself says it joined, in order. The
FIRST circle is therefore the firm's own claim about its entry round, and the
list as a whole is its follow-on record.

wayback-pull.py's `listing_regex` keeps only slug and name (COLLECTION.md's
era parsers are deliberately generic), so this reads the raw captures the
puller already saved under sources/wayback/raw/ and writes the ladder to
sources/site/wayback-circles.json. It fetches nothing: re-running it after the
puller adds a year picks the new capture up automatically.

Per decisions.md R1 this is an UNSCORED candidate layer. It is measured
against golden.json before the grind is allowed to treat it as a label.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

CARD = re.compile(r'(?s)<div class="span3">(.*?)<p class="circles">(.*?)</p>')
IMG = re.compile(r'images/logos/([A-Za-z0-9_.%-]+?)\.(?:png|jpg|jpeg|gif)"\s+alt="([^"]*)"')
SPAN = re.compile(r"<span>([^<]+)</span>")

# The era's own vocabulary. "Seed" is spelt out; later rounds are bare
# letters. Anything else is left verbatim and reported, never mapped
# silently -- a vocabulary this run has not seen is a finding.
LADDER = {"seed": "Seed", "a": "Series A", "b": "Series B", "c": "Series C",
          "d": "Series D", "e": "Series E", "f": "Series F"}


def main() -> None:
    p = Paths("felicis")
    raw = p.wayback / "raw"
    per_company: dict[str, dict] = {}
    unknown: Counter = Counter()
    years_seen: dict[str, set] = defaultdict(set)

    for f in sorted(raw.glob("[0-9][0-9][0-9][0-9]-portfolio.html")):
        year = f.name[:4]
        html = f.read_text(errors="replace")
        n = 0
        for card, circles in CARD.findall(html):
            m = IMG.search(card)
            if not m:
                continue
            slug, name = m.group(1).lower(), unescape(m.group(2)).strip()
            tokens = [t.strip() for t in SPAN.findall(circles) if t.strip()]
            ladder = []
            for t in tokens:
                key = t.strip().lower()
                if key in LADDER:
                    ladder.append(LADDER[key])
                else:
                    unknown[t] += 1
            if not ladder:
                continue
            e = per_company.setdefault(slug, {
                "slug": slug, "name": name or None,
                "ladder": [], "ladder_by_year": {}, "years": []})
            e["name"] = e["name"] or name or None
            e["ladder_by_year"][year] = ladder
            years_seen[slug].add(year)
            n += 1
        print(f"  {f.name}: {n} cards with a ladder")

    # The latest capture is the firm's most complete statement for a row: a
    # company listed in 2014 with "Seed" and in 2019 with "Seed a b" had two
    # follow-ons in between, and the 2019 reading is the fuller record. Entry
    # is the first element, which is stable across captures by construction --
    # any row where it is NOT stable is reported rather than silently resolved.
    unstable = []
    for slug, e in per_company.items():
        by_year = e["ladder_by_year"]
        latest = by_year[max(by_year)]
        e["ladder"] = latest
        e["site_entry_stage"] = latest[0]
        e["years"] = sorted(by_year)
        firsts = {v[0] for v in by_year.values()}
        if len(firsts) > 1:
            e["entry_unstable"] = sorted(firsts)
            unstable.append((slug, sorted(firsts), by_year))

    rows = sorted(per_company.values(), key=lambda r: r["slug"])
    out = p.root / "sources" / "site" / "wayback-circles.json"
    write_atomic(out, json.dumps({
        "_readme":
            "The firm's own round ladder per company, read off the "
            "<p class='circles'> block of the 2011-2019 felicis.com/portfolio/ "
            "captures. `ladder` is the rounds Felicis says it joined, in order, "
            "from the LATEST capture that carries the row; `site_entry_stage` is "
            "the first of them. UNSCORED: decisions.md R1 requires this layer to "
            "be measured on the stage golden set before the grind may label with "
            "it. Derived offline from sources/wayback/raw/*-portfolio.html by "
            "scratch/parse-circles.py; it fetches nothing.",
        "_captures": sorted({y for s in years_seen.values() for y in s}),
        "companies-circles": rows,
    }, indent=1, ensure_ascii=False) + "\n")

    print(f"\nwrote {out.name}: {len(rows)} companies")
    print("  entry distribution:", dict(Counter(r["site_entry_stage"] for r in rows)))
    print("  ladder length     :", dict(Counter(len(r["ladder"]) for r in rows)))
    if unknown:
        print("  UNMAPPED tokens   :", dict(unknown))
    if unstable:
        print(f"  UNSTABLE entry across captures ({len(unstable)}):")
        for slug, firsts, by_year in unstable[:12]:
            print(f"    {slug}: {firsts} {by_year}")


if __name__ == "__main__":
    main()
