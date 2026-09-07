#!/usr/bin/env python3
"""Build sources/wayback/partner-roster.json from the saved CDX dump.

web.archive.org refused every connection from ~22:25 on 2026-09-06 (the
outage pattern of COLLECTION.md §5), which takes out partner-roster.py's
`cdx_people` step. The whole felicis.com CDX index had already been pulled
before the outage and is kept as evidence at
sources/wayback/raw/cdx-felicis.com-domain-20260906.txt, so the same rows
the script would have fetched are derived from that file instead: one entry
per /team/<slug>, with capture years as the tenure window.

This writes partner-roster.py's exact output shape, so re-running the real
script once the archive recovers simply re-derives and converges (it
overwrites rather than merges, which is safe: the live CDX is a superset of
this dump).

The /founder/ namespace is a directory of PORTFOLIO FOUNDERS, not the firm's
roster (§5.2, the First Round trap), and is excluded here deliberately -- it
is pulled separately as a company list.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

DUMP = "cdx-felicis.com-domain-20260906.txt"


def main() -> None:
    p = Paths("felicis")
    cfg = p.config()["roster"]
    slug_re = re.compile(cfg["slug_re"])
    not_a_person = set(cfg["not_a_person"])

    dump = p.wayback / "raw" / DUMP
    years: dict[str, set[int]] = defaultdict(set)
    for line in dump.read_text(errors="replace").splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        ts, url = parts[0], parts[1]
        m = slug_re.search(url.split("?")[0])
        if not m:
            continue
        slug = m.group(1)
        # Next.js build artefacts live in the same namespace (/team/[slug]/
        # page-<hash>.js); they are filtered by the slug pattern's own shape
        # plus the config's not_a_person list.
        if slug in not_a_person or slug.startswith("page-") or len(slug) < 3:
            continue
        years[slug].add(int(ts[:4]))

    # The live CMS team is current-year evidence, exactly as partner-roster.py
    # unions it in.
    site = json.loads((p.root / "sources" / "site" / "team-members.json").read_text())
    # COLLECTION.md §5.2: where the team CMS carries a group taxonomy, only the
    # board-relevant groups are swept. partner-roster.py's own rule keeps rows
    # that carry NO group, and this matches it exactly.
    keep_groups = set(cfg.get("site_team_groups") or [])
    site_names: dict[str, str] = {}
    out_of_group: set = set()
    skipped = []
    for r in site["rows"]:
        if keep_groups and r.get("group") and r["group"] not in keep_groups:
            skipped.append(r.get("name"))
            sl = (r.get("slug") or "").strip().lower()
            if sl:
                out_of_group.add(sl)
            continue
        slug = (r.get("slug") or "").strip().lower()
        if not slug:
            name = (r.get("name") or "").strip().lower()
            slug = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
        if not slug:
            continue
        site_names[slug] = (r.get("name") or "").strip()
        years[slug].add(2026)

    # A person's CMS group is a fact about the PERSON, not about the surface
    # that named them, so it constrains the archived slugs too: Ryan Thompson
    # (Operations, 29 sweep rows), Tyler Wilson (Operations, 6) and Beth
    # Steinberg (Finance, 8 Brightwood Capital rows) had /team/ pages in their
    # own era and contribute homonym noise from every one of them. This is the
    # a16z rule (469 of 572 site people were non-investors) applied to a roster
    # whose archive predates the group taxonomy.
    dropped = [s for s in years if s in out_of_group]
    for slug in dropped:
        years.pop(slug)

    rows = []
    for slug, ys in sorted(years.items()):
        seen = sorted(ys)
        rows.append({
            "slug": slug,
            "name": site_names.get(slug) or " ".join(
                w.capitalize() for w in slug.split("-")),
            "years_seen": seen,
            "first_seen": seen[0],
            "last_seen": seen[-1],
            "snapshots": len(seen),
            "sources": sorted(
                (["cdx-profile-page"] if slug in {s for s in years} and
                 any(True for _ in [1]) else [])
                + (["site-team"] if slug in site_names else [])
            ) or ["cdx-profile-page"],
        })

    p.wayback.mkdir(parents=True, exist_ok=True)
    write_atomic(p.wayback / "partner-roster.json", json.dumps(rows, indent=1) + "\n")
    print(f"wrote partner-roster.json: {len(rows)} people")
    print(f"  from the CDX dump only : {sum(1 for r in rows if r['slug'] not in site_names)}")
    print(f"  on the live CMS team   : {sum(1 for r in rows if r['slug'] in site_names)}")
    cur = [r['slug'] for r in rows if r['last_seen'] >= 2025]
    print(f"  last seen 2025+        : {len(cur)}")
    print(f"  dropped as non-investing: {len(dropped)} ({', '.join(sorted(dropped))})")
    if skipped:
        print(f"  CMS rows outside the swept groups ({len(skipped)}): "
              f"{', '.join(sorted(n for n in skipped if n))}")


if __name__ == "__main__":
    main()
