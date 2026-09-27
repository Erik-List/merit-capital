#!/usr/bin/env python3
"""Build Insight Partners' roster for the Form D sweep from first-party sources.

Sources, unioned into sources/wayback/partner-roster.json in partner-roster.py's
shape ({slug, name, years_seen, first_seen, last_seen, snapshots, sources}):

  site-team   the live Investors department, at the titles that hold board
              seats (Managing Director, Principal, the Vice President grades,
              Director, Senior Advisor, Operating Partner). Associates and
              analysts are left out unless a company panel names them: they
              sit on no board, and 50 more common names buy only false
              matches. first_seen is the year the person's own bio gives
              ("joined Insight in 2018") where it gives one.
  site-panel  every name on a company panel's Investment Team (the firm's own
              attribution map), whatever the title, including the few people
              the live team page no longer lists.
  cdx         archived people pages with capture-year windows, when
              scratch/roster-cdx.json exists (partner-roster.py's output,
              copied there after the archive cooldown). This is the only
              source that dates a departure.
  founders    Jeff Horing and Jerry Murdock founded the firm in 1995.

One person, one entry: name variants fold onto one slug with the union window
(the First Round rule), via VARIANTS.

Usage: python3 data/collection/investors/insight-partners/scratch/build-roster.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("insight-partners")
OUT = P.wayback / "partner-roster.json"
CDX = P.scratch / "roster-cdx.json"
THIS_YEAR = 2026

SEAT_TITLES = re.compile(
    r"managing director|principal|vice president|^director|senior advisor|"
    r"operating partner|co-founder", re.I)
# not investing seats even inside the Investors department
NOT_SEATS = re.compile(r"trading|investor relations|compliance|counsel|financial officer|"
                       r"operating officer|human capital|marketing|partnerships", re.I)

# variant slug -> canonical slug
VARIANTS = {
    "jeffrey-horing": "jeff-horing",
    "jeffrey-lieberman": "jeff-lieberman",
    "eugenia-bejar-lustgarten": "eugenia-lustgarten",
    "emmet-b-keeffe-iii": "emmet-keeffe",
    "emmet-b-keeffe": "emmet-keeffe",
    "aj-malhotra": "aj-malhotra",
}
# the name the sweep should match on, where the site's rendering would not
FILED_NAME = {
    "jeff-horing": "Jeffrey Horing",
    "jeff-lieberman": "Jeffrey Lieberman",
    "eugenia-lustgarten": "Eugenia Lustgarten",
    "emmet-keeffe": "Emmet Keeffe",
}
FOUNDED = {"jeff-horing": 1995, "jerry-murdock": 1995, "deven-parekh": 2000,
           "peter-sobiloff": 1998}


def slug_of(name: str) -> str:
    s = re.sub(r"\(.*?\)", " ", name.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return VARIANTS.get(s, s)


def main() -> None:
    team = json.load(open(P.site / "team-pages.json"))["rows"]
    comps = json.load(open(P.site / "company-pages.json"))["rows"]
    people: dict[str, dict] = {}

    def add(name: str, source: str, years: set[int], basis: str, title: str = "") -> None:
        s = slug_of(name)
        if not s or "-" not in s:
            return
        r = people.setdefault(s, {"slug": s, "name": FILED_NAME.get(s, re.sub(r"\s*\(.*?\)\s*", " ", name).strip()),
                                  "site_name": name, "years": set(), "sources": [],
                                  "basis": [], "title": ""})
        r["years"] |= years
        if source not in r["sources"]:
            r["sources"].append(source)
        if basis:
            r["basis"].append(basis)
        r["title"] = r["title"] or title

    live_names = set()
    for t in team:
        live_names.add(slug_of(t["name"]))
        if "Investors" not in (t.get("departments") or []):
            continue
        title = t.get("title") or ""
        if not SEAT_TITLES.search(title) or NOT_SEATS.search(title):
            continue
        m = re.search(r"joined\s+Insight[^.]{0,60}?((?:19|20)\d\d)", t.get("bio") or "", flags=re.I)
        start = int(m.group(1)) if m else None
        yrs = set(range(start, THIS_YEAR + 1)) if start else {THIS_YEAR}
        add(t["name"], "site-team", yrs,
            f"{title} on the live team (Investors)" + (f"; bio: joined Insight in {start}" if start else "; start year not stated"),
            title)

    titles = {slug_of(t["name"]): t.get("title") or "" for t in team}
    bios = {slug_of(t["name"]): t.get("bio") or "" for t in team}
    by_person: dict[str, list[int]] = {}
    for c in comps:
        for n in c.get("partners") or []:
            by_person.setdefault(n, []).append(int(c["invest_year"]) if c.get("invest_year") else 0)
    for n, ys in by_person.items():
        s = slug_of(n)
        m = re.search(r"joined\s+Insight[^.]{0,60}?((?:19|20)\d\d)", bios.get(s, ""), flags=re.I)
        start = int(m.group(1)) if m else None
        yrs = set(range(start, THIS_YEAR + 1)) if start else {THIS_YEAR}
        listed = "on the live team" if s in live_names else "NOT on the live team page (departed or unlisted; departure undated)"
        add(n, "site-panel", yrs,
            f"named on the Investment Team of {len(ys)} company panels; {listed}", titles.get(s, ""))

    # people the firm's own history names whom neither list carries as an
    # investor today
    add("Jerry Murdock", "site-team", set(range(1995, THIS_YEAR + 1)),
        "co-founder (1995); the live team lists him as 'Advisor, Co-Founder, Prior Managing Director'",
        "Advisor, Co-Founder, Prior Managing Director")

    for s, y in FOUNDED.items():
        if s in people:
            people[s]["years"] |= set(range(y, THIS_YEAR + 1))
            people[s]["basis"].append(f"at the firm since {y} (firm history)")

    if CDX.exists():
        for r in json.load(open(CDX)):
            yrs = set(r.get("years_seen") or [])
            if not yrs:
                continue
            add(r.get("site_name") or r["name"], "cdx", yrs,
                f"archived people pages {min(yrs)}-{max(yrs)} ({r.get('snapshots')} capture years)")

    out = []
    for s, r in sorted(people.items()):
        yrs = sorted(r["years"])
        out.append({
            "slug": s, "name": r["name"], "site_name": r["site_name"],
            "years_seen": yrs, "first_seen": yrs[0], "last_seen": yrs[-1],
            "snapshots": len(yrs), "sources": r["sources"], "title": r["title"],
            "basis": "; ".join(dict.fromkeys(r["basis"])),
        })
    write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"roster: {len(out)} people -> {OUT.relative_to(ROOT)}")
    print("  sources:", {k: sum(1 for r in out if k in r["sources"]) for k in ("site-team", "site-panel", "cdx")})
    print("  departed (last_seen < 2026):", sum(1 for r in out if r["last_seen"] < THIS_YEAR))


if __name__ == "__main__":
    main()
