#!/usr/bin/env python3
"""Parse Redpoint's two earliest site eras into the pipeline's own shapes.

Why this is not a `wayback.eras` entry: both eras render the portfolio as ONE
page carrying TWO labelled sections — the firm's own "(All) Current
Investments" and "Previous Investments by Redpoint Partners", the founding
partners' Brentwood and IVP book (decisions.md D5) — and a single listing
regex cannot separate them. Era 2 (2002-2006) is additionally logo-only: the
company cell holds an image with no alt text, so the name is derived from the
company's own URL and the firm's own logo filename and then corrected by
joining to the eras that do render names.

Outputs (all idempotent, all merged rather than replaced):
  sources/wayback/raw/<year>-<seg>.html       the captures, as wayback-pull stores them
  sources/wayback/parsed/<year>.json          {slug,name,path,snapshot_ts} rows,
                                              path marks which section the row came from
  sources/site/companies-2000-2006.json       the rich columns the eras publish
  sources/web/previous-by-partners.json       the predecessor-book list, with years

Usage: python3 scratch/build-early-eras.py [--no-fetch]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import shared_throttle                                    # noqa: E402
from paths import Paths, write_atomic                     # noqa: E402
import parse_eras as PE                                   # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
P = Paths("redpoint-ventures")

# era key -> (path, url, years, section wanted)
ERAS = [
    ("portfolio-default.shtml", "/portfolio/default.shtml",
     "http://www.redpoint.com/portfolio/default.shtml", range(2000, 2003)),
    ("index-oid152", "/index.htm?oid=152",
     "http://www.redpoint.com/index.htm?action=view&oid=152", range(2002, 2007)),
    ("index-oid157", "/index.htm?oid=157",
     "http://www.redpoint.com/index.htm?action=view&oid=157", range(2002, 2007)),
]
PROBES = ("0615", "0201", "1015", "1101", "0301")


def replay(url: str, year: int) -> tuple[str, str]:
    """(html, true_timestamp) for the capture nearest a probe date inside `year`.

    https only: the archive's port 80 was refusing connections intermittently
    for the whole of this run while https answered (reported at close)."""
    for probe in PROBES:
        shared_throttle.wait("ia")
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "150", "-w", "\n%{url_effective}",
             "-H", f"User-Agent: {UA}",
             f"https://web.archive.org/web/{year}{probe}id_/{url}"],
            capture_output=True, text=True, errors="replace")
        body, _, eff = (r.stdout or "").rpartition("\n")
        m = re.search(r"/web/(\d{14})id_/", eff)
        if m and m.group(1)[:4] == str(year) and len(body) > 2000:
            return body, m.group(1)
    return "", ""


def derive_name(row: dict) -> tuple[str, str]:
    """(name, basis). The firm's own rendering wins; a logo-only row is named
    from its own domain, with the logo filename as the tie-break."""
    if row.get("name_alt"):
        return row["name_alt"], "site_alt"
    if row.get("name_text"):
        return row["name_text"], "site_text"
    host = urlparse(row.get("url") or "").netloc.lower()
    host = re.sub(r"^(www|corp|home)\.", "", host)
    stem = re.sub(r"\.(jpg|jpeg|gif|png)$", "", row.get("logo_file") or "", flags=re.I)
    stem = re.sub(r"[_-]?(logo|final|new|web|sm|lrg|home)[_ -]?", " ", stem, flags=re.I)
    stem = re.sub(r"\s+", " ", stem).strip(" _-")
    if host:
        base = host.rsplit(".", 1)[0] if host.count(".") >= 1 else host
        base = re.sub(r"\.(co|com)$", "", base)
        return base, "derived_from_url"
    return stem or "", "derived_from_logo"


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def host_of(url: str) -> str:
    """The company's own domain, normalized — the identity key that survives
    a logo-only era. redpoint.com's own host and the acquirers' are excluded
    by the caller (an acquired row's logo link points at the acquirer)."""
    h = urlparse(url or "").netloc.lower().split(":")[0]
    h = re.sub(r"^(www|www2|corp|home|us)\.", "", h)
    return h


def name_map() -> dict[str, str]:
    """host -> the firm's own rendering of the name, from every surface that
    renders one: the live Sanity CMS, and the 2007-2012 captures' logo alt
    text. This is what names the 2002-2006 logo-only rows."""
    out: dict[str, str] = {}

    def put(host: str, name: str) -> None:
        host, name = host.strip(), (name or "").strip()
        if host and name and host not in out:
            out[host] = name

    live = P.site / "sanity-companies.json"
    if live.exists():
        for r in json.loads(live.read_text()).get("result", []):
            put(host_of(r.get("url") or ""), r.get("name") or "")
    for f in sorted((P.wayback / "raw").glob("*-portfolio-current-investments.html")):
        html = f.read_text(errors="replace")
        for m in re.finditer(r'<a[^>]+href="(https?://[^"]+)"[^>]*>\s*<img[^>]+'
                             r'alt="([^"]+)"', html, re.I):
            put(host_of(m.group(1)), m.group(2))
        for m in re.finditer(r'<img[^>]+src="[^"]*(?:customer_logos|uploads)[^"]*"'
                             r'[^>]*alt="([^"]+)"', html, re.I):
            pass
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-fetch", action="store_true")
    args = ap.parse_args()

    raw_dir, parsed_dir = P.wayback / "raw", P.wayback / "parsed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    parsed_dir.mkdir(parents=True, exist_ok=True)
    (P.root / "sources" / "web").mkdir(parents=True, exist_ok=True)

    rich: dict[str, dict] = {}       # key -> rich row (current sections)
    prev: dict[str, dict] = {}       # key -> predecessor-book row
    per_year: dict[int, list] = {}
    names = name_map()
    print(f"name map: {len(names)} hosts named by a rendering surface")
    # site_alt/site_text beat a name derived from the row's own domain, and a
    # name rendered on ANY era's surface beats both when it is the same company
    RANK = {"site_alt": 0, "site_text": 1, "name_map": 2,
            "derived_from_url": 3, "derived_from_logo": 4}

    for seg, path_label, url, years in ERAS:
        for y in years:
            f = raw_dir / f"{y}-{seg}.html"
            html = f.read_text(errors="replace") if f.exists() else ""
            ts = ""
            if not html and not args.no_fetch:
                html, ts = replay(url, y)
                if html:
                    f.write_text(html)
                    (raw_dir / f"{y}-{seg}.ts").write_text(ts)
            elif f.exists() and (raw_dir / f"{y}-{seg}.ts").exists():
                ts = (raw_dir / f"{y}-{seg}.ts").read_text().strip()
            if not html:
                print(f"  {seg} {y}: no capture")
                continue
            sections = PE.split_sections(html)
            counts = {}
            for section, body in sections.items():
                rows = PE.parse_rows(body)
                if section == "previous" and not rows:
                    rows = [{**r, "site_status": "", "logo_file": "", "name_alt": ""}
                            for r in PE.parse_previous_text(body)]
                counts[section] = len(rows)
                for r in rows:
                    name, basis = derive_name(r)
                    host = "" if r.get("acquirer") else host_of(r.get("url") or "")
                    if host in names and basis.startswith("derived"):
                        name, basis = names[host], "name_map"
                    if not name:
                        continue
                    # identity key: the company's own domain where the row has
                    # one, so a logo-only row and a named row are ONE company
                    key = host or slug_of(name)
                    slug = slug_of(name)
                    p_label = (path_label if section == "current"
                               else f"{path_label}#previous-by-partners")
                    per_year.setdefault(y, []).append(
                        {"slug": slug, "name": name, "path": p_label,
                         "snapshot_ts": ts})
                    tgt = rich if section == "current" else prev
                    row = tgt.setdefault(key, {
                        "slug": slug, "name": name, "_name_basis": basis,
                        "url": "", "description": "", "site_location": "",
                        "site_status": "", "ticker": "", "acquirer": "",
                        "logo_file": "", "listing_years": [], "era": seg,
                        "section": section})
                    if RANK[basis] < RANK[row["_name_basis"]]:
                        row["name"], row["_name_basis"] = name, basis
                    for k in ("url", "description", "site_location", "site_status",
                              "ticker", "acquirer", "logo_file"):
                        if r.get(k) and not row[k]:
                            row[k] = r[k]
                    if y not in row["listing_years"]:
                        row["listing_years"].append(y)
            print(f"  {seg} {y} ({ts or 'cached'}): {counts}")

    # ---- merge into the per-year parsed files (keyed slug+path, existing wins)
    for y, rows in sorted(per_year.items()):
        dest = parsed_dir / f"{y}.json"
        merged = {(r["slug"], r.get("path")): r
                  for r in (json.loads(dest.read_text()) if dest.exists() else [])}
        for r in rows:
            merged.setdefault((r["slug"], r.get("path")), r)
        write_atomic(dest, json.dumps(sorted(merged.values(),
                     key=lambda r: (r["slug"], r.get("path") or "")), indent=1) + "\n")

    readme = ("Built by scratch/build-early-eras.py from the archived captures of "
              "redpoint.com's first two site eras. Era 1 (2000-2002) is "
              "/portfolio/default.shtml; era 2 (2002-2006) is the index.htm CMS, "
              "oid=152 'All Current Investments' and oid=157 'Previous Investments by "
              "Redpoint Partners'. Both eras publish four columns (company logo, "
              "description, location, status) and era 2 renders no alt text, so a "
              "logo-only row is named from its own domain (_name_basis records which). "
              "'previous' rows are the founding partners' Brentwood and IVP book, "
              "not_member by decisions.md D5 unless the company also appears in a "
              "current-investments section or carries independent Redpoint evidence.")
    write_atomic(P.site / "companies-2000-2006.json", json.dumps(
        {"_readme": readme, "rows": sorted(rich.values(), key=lambda r: r["slug"])},
        indent=1) + "\n")
    write_atomic(P.root / "sources" / "web" / "previous-by-partners.json", json.dumps(
        {"_readme": readme, "rows": sorted(prev.values(), key=lambda r: r["slug"])},
        indent=1) + "\n")
    print(f"\ncurrent-section companies: {len(rich)}   "
          f"previous-by-partners: {len(prev)}   years: {sorted(per_year)}")


if __name__ == "__main__":
    main()
