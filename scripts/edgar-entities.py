#!/usr/bin/env python3
"""Build the investor's EDGAR entity registry: their own legal vehicles.

One canonical table answering "is this CIK theirs, and which desk?" — used by
role resolution, fund exclusion and lineage partitioning alike.

Sources (union; measured to be non-overlapping):
  1. EDGAR company-name search (seed queries from the investor's config.json)
  2. Co-filer closure: CIKs appearing in a filer role alongside a seed entity
  3. The investor's own pooled-investment-fund Form D issuers

Output: <investor>/entities.json
  {cik, name, desk, vehicle_role, sources[], confirmed}

`desk` is a reviewable lookup table: defaulted from the entity name via the
config's desk patterns, then human-confirmable via the `confirmed` flag.
Judged once and stored, rather than re-derived by regex on every build.

Usage: python3 scripts/edgar-entities.py <investor-slug>
"""
import argparse
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from edgar_common import fetch_header, parse_header_roles  # noqa: E402
from paths import ROOT, Paths  # noqa: E402
from people_common import same_person_any_order  # noqa: E402

UA = "Merit Capital research erik@meritcapit.al"

# Set in main() from the investor's config.json ("desks" block).
DESK_RULES: list[tuple[str, list[re.Pattern]]] = []


def curl(url: str, extra: list[str] | None = None) -> str:
    for attempt in range(4):
        try:
            cmd = ["curl", "-sf", "--max-time", "60", "-H", f"User-Agent: {UA}"]
            cmd += extra or []
            cmd.append(url)
            return subprocess.run(cmd, capture_output=True, check=True).stdout.decode(
                "utf-8", errors="replace")
        except subprocess.CalledProcessError:
            time.sleep(1.5 * (attempt + 1))
    return ""


def classify_desk(name: str) -> str:
    """Default desk from entity name — a starting point for human review.

    The patterns are the investor's, from config.json; rule order decides
    precedence (a split-off desk pattern must come before the parent firm's).
    """
    n = name.lower()
    for desk, pats in DESK_RULES:
        if any(p.search(n) for p in pats):
            return desk
    return "unknown"


def classify_role(name: str) -> str:
    n = name.lower()
    if "principals" in n:
        return "principals-fund"
    if "management" in n or re.search(r"\bgp\b", n):
        return "management"
    if "scout" in n:
        return "scout-fund"
    if "fund" in n or re.search(r"\bl\.?\s?p\.?$", n.strip()):
        return "fund"
    return "unknown"


def seed_from_company_search(seed_queries: list[str]) -> dict[str, dict]:
    """EDGAR company-name search (HTML endpoint; the atom feed mangles names)."""
    found: dict[str, dict] = {}
    for q in seed_queries:
        for start in (0, 100, 200):
            html = curl(f"https://www.sec.gov/cgi-bin/browse-edgar?company={q}"
                        f"&type=&dateb=&owner=include&count=100&start={start}&action=getcompany")
            rows = re.findall(r'CIK=(\d{10})[^"]*"[^>]*>[^<]*</a></td>\s*<td[^>]*>([^<]+)', html)
            if not rows:
                rows = re.findall(r'CIK=(\d{10})[^"]*"[^>]*>\s*\d+\s*</a></td><td[^>]*>([^<]+)', html)
            if not rows:
                break
            for cik, name in rows:
                c = str(int(cik))
                found.setdefault(c, {"cik": c, "name": name.strip(), "sources": []})
                if "company-search" not in found[c]["sources"]:
                    found[c]["sources"].append("company-search")
            time.sleep(0.3)
    return found


def from_existing_filings(edgar_dir: Path) -> dict[str, dict]:
    """Harvest entity names/CIKs already present in collected EDGAR filings."""
    found: dict[str, dict] = {}
    p = edgar_dir / "winner-filings.json"
    if not p.exists():
        return found
    for rec in json.load(open(p)).values():
        for n in rec.get("issuers", []) + rec.get("filers", []):
            m = re.search(r"\(CIK (\d+)\)", n)
            if not m:
                continue
            name = re.sub(r"\s*\(CIK \d+\)\s*$", "", n).strip()
            name = re.sub(r"\s*\([A-Z., ]{1,20}\)\s*$", "", name).strip()
            if classify_desk(name) == "unknown":
                continue  # not one of theirs
            c = str(int(m.group(1)))
            found.setdefault(c, {"cik": c, "name": name, "sources": []})
            if "prior-filings" not in found[c]["sources"]:
                found[c]["sources"].append("prior-filings")
    return found


def from_formd_pooled(edgar_dir: Path) -> dict[str, dict]:
    """The investor's own pooled-investment-fund Form D issuers."""
    found: dict[str, dict] = {}
    p = edgar_dir / "formd-sweep.json"
    if not p.exists():
        return found
    for rec in json.load(open(p)).values():
        if rec.get("industry_group") != "Pooled Investment Fund":
            continue
        name, cik = rec.get("issuer"), rec.get("cik")
        if not name or not cik or classify_desk(name) == "unknown":
            continue
        c = str(int(cik))
        found.setdefault(c, {"cik": c, "name": name.strip(), "sources": []})
        if "formd-pooled" not in found[c]["sources"]:
            found[c]["sources"].append("formd-pooled")
    return found


def cofiler_closure(seed_ciks: set[str], sample_per_entity: int = 15) -> dict[str, dict]:
    """CIKs co-appearing in a filer role with a seed entity are affiliates.

    Discovers vehicles whose names contain no investor keyword at all
    (SC US (TTGP), SCGGF MANAGEMENT, SC IX.I MANAGEMENT).
    """
    found: dict[str, dict] = {}
    seen_acc: set[str] = set()
    for cik in sorted(seed_ciks):
        subs = curl(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
        if not subs:
            continue
        try:
            recent = json.loads(subs)["filings"]["recent"]
        except (json.JSONDecodeError, KeyError):
            continue
        accs = [a for a, f in zip(recent["accessionNumber"], recent["form"])
                if f in ("3", "4", "5", "SC 13D", "SC 13G", "SC 13D/A", "SC 13G/A")]
        for acc in accs[:sample_per_entity]:
            if acc in seen_acc:
                continue
            seen_acc.add(acc)
            hdr = fetch_header(cik, acc)
            if not hdr:
                continue
            _subject, filers = parse_header_roles(hdr)
            for name, fcik in filers:
                c = str(int(fcik))
                if c in seed_ciks or c in found:
                    continue
                found[c] = {"cik": c, "name": name, "sources": ["cofiler-closure"]}
        time.sleep(0.12)
    return found


def resolve_unknowns(registry: dict[str, dict], p: Paths, desks_cfg: dict) -> None:
    """Split the unclassified remainder into the investor's own people vs outsiders.

    Co-filer closure necessarily picks up unrelated institutions that merely
    appear on the same filing (Ameriprise, GIC, SINA). Crawling their
    submissions would import their entire portfolio, so they must be marked
    `external` and excluded. The investor's partners, meanwhile, file as
    individual reporting owners and are genuine board-seat evidence — they are
    identified against the partner roster, not by name shape.
    """
    roster_path = p.wayback / "partner-roster.json"
    roster = [r["name"] for r in json.load(open(roster_path))] if roster_path.exists() else []
    own_desks = {desk for desk, _ in DESK_RULES}
    home_desk = desks_cfg["home"]

    # a person's desk follows the desks of the entities they co-file with
    cofiler_desks: dict[str, Counter] = {}
    for hdr_file in (ROOT / "data" / "filings" / "edgar-headers").glob("*.txt"):
        _subject, filers = parse_header_roles(
            hdr_file.read_text(encoding="utf-8", errors="replace"))
        ciks = [c for _, c in filers]
        known = [registry[c] for c in ciks if c in registry]
        desks = Counter(e["_desk"] for e in known
                        if e.get("_desk") in own_desks)
        if not desks:
            continue
        for c in ciks:
            if c in registry and registry[c].get("_desk") == "unknown":
                cofiler_desks.setdefault(c, Counter()).update(desks)

    people = external = 0
    for e in registry.values():
        if e.get("_desk") != "unknown":
            continue
        if any(same_person_any_order(e["name"], r) for r in roster):
            e["_desk"] = (cofiler_desks.get(e["cik"], Counter()).most_common(1) or
                          [(home_desk, 0)])[0][0]
            e["_role"] = "person"
            people += 1
        else:
            e["_desk"] = "external"
            e["_role"] = "outside-cofiler"
            external += 1
    print(f"   unclassified resolved: {people} partners (people), "
          f"{external} external co-filers excluded from crawling")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    args = ap.parse_args()

    p = Paths(args.investor)
    cfg = p.config()
    global DESK_RULES
    DESK_RULES = [(r["desk"], [re.compile(pat) for pat in r["patterns"]])
                  for r in cfg["desks"]["classify"]]

    registry: dict[str, dict] = {}

    def merge(batch: dict[str, dict]) -> None:
        for c, e in batch.items():
            if c in registry:
                for s in e["sources"]:
                    if s not in registry[c]["sources"]:
                        registry[c]["sources"].append(s)
                if len(e["name"]) > len(registry[c]["name"]):
                    registry[c]["name"] = e["name"]
            else:
                registry[c] = dict(e)

    print("== seeding from EDGAR company search")
    merge(seed_from_company_search(cfg["edgar"]["seed_queries"]))
    print(f"   {len(registry)} entities")

    print("== harvesting from previously collected filings")
    merge(from_existing_filings(p.edgar))
    print(f"   {len(registry)} entities")

    print("== folding in own pooled Form D vehicles")
    before = len(registry)
    merge(from_formd_pooled(p.edgar))
    print(f"   +{len(registry)-before} (total {len(registry)})")

    print("== co-filer closure (sampling filings of seed entities)")
    merge(cofiler_closure(set(registry)))
    print(f"   {len(registry)} entities")

    # preserve human desk confirmations across rebuilds
    prior = {}
    dest = p.entities
    if dest.exists():
        prior = {e["cik"]: e for e in json.load(open(dest))}

    for c, e in registry.items():
        e["cik"] = c
        e["_desk"] = classify_desk(e["name"])
        e["_role"] = classify_role(e["name"])
    resolve_unknowns(registry, p, cfg["desks"])

    rows = []
    for c, e in registry.items():
        pr = prior.get(c, {})
        rows.append({
            "cik": c,
            "name": e["name"],
            "desk": pr["desk"] if pr.get("confirmed") else e["_desk"],
            "vehicle_role": e["_role"],
            "sources": sorted(e["sources"]),
            "confirmed": bool(pr.get("confirmed", False)),
        })
    rows.sort(key=lambda r: (r["desk"], r["name"].lower()))
    dest.write_text(json.dumps(rows, indent=1) + "\n")

    print(f"\nwrote {dest.relative_to(ROOT)} — {len(rows)} entities")
    print("  by desk:", dict(Counter(r["desk"] for r in rows)))
    print(f"  crawlable (desk != external): "
          f"{sum(1 for r in rows if r['desk'] != 'external')}")


if __name__ == "__main__":
    main()
