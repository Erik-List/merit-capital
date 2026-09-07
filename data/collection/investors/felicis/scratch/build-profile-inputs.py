#!/usr/bin/env python3
"""The two inputs build-firm-profile.py refuses to start without (§11).

COLLECTION.md §11: "`build-firm-profile.py` has two required inputs that
nothing else writes ... It refuses to start without
`sources/edgar/fund-formds.json` and `sources/site/team-members.json`."

Both carry traps the playbook names explicitly, and both bite here:

* `fund-formds.json` is a mechanical filter of `formd-sweep.json` by
  `config.profile.own_vehicle_pattern`, keyed by issuer name -- and its
  `_readme` must be a **dict**, because the fund verifier iterates every value
  and calls `.get("filings")` on it. A string `_readme` crashes the build.
* `team-members.json` must be a **flat list**, and `role_bucket` must be a
  **list** (the build does `set(m.get("role_bucket", []))`, so a bare string
  would be read as a set of its characters and never match an investing
  bucket). The same CMS pull also feeds site-portfolio.py, which wants
  `{"rows": [...]}` -- so the two consumers get two files rather than one
  file that satisfies neither.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

# Felicis's own teamCategory values -> the buckets build-firm-profile.py
# treats as investing.
BUCKETS = {
    "Investors": ["investing"],
    "Venture Partners": ["investing"],
    "Finance": [],
    "Operations": [],
    "Founder Success": [],
}


def main() -> None:
    p = Paths("felicis")
    cfg = p.config()
    pat = re.compile(cfg["profile"]["own_vehicle_pattern"], re.I)

    # ---- fund-formds.json
    sweep = json.loads((p.edgar / "formd-sweep.json").read_text())
    funds: dict = {}
    for acc, v in sweep.items():
        issuer = (v.get("issuer") or "").strip()
        if not issuer or not pat.match(issuer.lower()):
            continue
        e = funds.setdefault(issuer, {"cik": v.get("cik"), "filings": []})
        e["filings"].append({
            "form": v.get("form") or "D",
            "accession": acc,
            "quarter": (v.get("persons") or [{}])[0].get("quarter"),
            "offering": v.get("total_offering"),
            "sold": v.get("total_sold"),
            "indefinite": str(v.get("total_offering") or "").lower() == "indefinite",
            "first_sale": v.get("date_of_first_sale"),
            "pooled": True,
            "fund_type": v.get("fund_type"),
            "co_issuers": v.get("co_issuers") or [],
        })
    for e in funds.values():
        e["filings"].sort(key=lambda f: f["accession"])

    out = {"_readme": {
        "what": "Every Form D in this run's roster sweep whose ISSUER is one of "
                "Felicis's own vehicles, matched by config.profile."
                "own_vehicle_pattern and keyed by issuer name.",
        "why_a_dict": "build-firm-profile.py's fund verifier iterates every "
                      "value of this file and calls .get('filings') on it, so "
                      "this _readme has to be a dict rather than a string "
                      "(COLLECTION.md §11).",
        "caveat": "This is the sweep's view, not an exhaustive filer sweep: the "
                  "roster-name sweep only sees a vehicle's Form D where a swept "
                  "person is a related person on it. The fund LADDER in "
                  "investor.json is built from the EDGAR company search over all "
                  "sixteen Felicis filers, which is the superset.",
    }}
    out.update(funds)
    write_atomic(p.edgar / "fund-formds.json", json.dumps(out, indent=1) + "\n")
    print(f"fund-formds.json: {len(funds)} own vehicles, "
          f"{sum(len(v['filings']) for v in funds.values())} filings")
    for n, v in sorted(funds.items()):
        print(f"   {n[:46]:46} {len(v['filings'])} filing(s)")

    # ---- team-members.json (flat list) + team-cms.json (site-portfolio shape)
    src = json.loads((p.site / "team-members.json").read_text())
    rows = src["rows"] if isinstance(src, dict) else src
    write_atomic(p.site / "team-cms.json",
                 json.dumps({"_readme": "Sanity team docs in site-portfolio.py's "
                                        "file_list shape.", "rows": rows},
                            indent=1, ensure_ascii=False) + "\n")
    flat = []
    for r in rows:
        grp = r.get("site_group") or r.get("group")
        flat.append({
            "name": (r.get("name") or "").strip(),
            "cms_title": r.get("cms_title") or r.get("title"),
            "role_bucket": BUCKETS.get(grp, []),
            "site_group": grp,
            "linkedin_url": r.get("linkedin_url"),
            "x_url": r.get("x_url"),
            "source": "sanity:teamMember",
        })
    write_atomic(p.site / "team-members.json",
                 json.dumps(flat, indent=1, ensure_ascii=False) + "\n")
    inv = sum(1 for m in flat if m["role_bucket"])
    print(f"team-members.json: {len(flat)} members ({inv} in investing buckets), "
          f"{sum(1 for m in flat if m['cms_title'])} with a CMS title")


if __name__ == "__main__":
    main()
