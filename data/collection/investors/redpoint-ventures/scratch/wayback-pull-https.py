#!/usr/bin/env python3
"""RUN-LOCAL COPY of scripts/wayback-pull.py with one change: every
web.archive.org URL is https instead of http.

The archive refused plain-HTTP connections intermittently for the whole of
the PRO-90 run (curl rc=7 on 2 of 3 tries, while https answered 3 of 3), and
the upstream script builds every CDX and replay URL as http, so it was
landing partial years and printing them as "0 entries". scripts/ is edited
only by the wave's designated tooling session (COLLECTION.md 12), so the
workaround lives here and the one-line fix is proposed at close.
"""

import argparse
import gzip
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = {"User-Agent": "MeritCapitalResearch/1.0 (erik@meritcapit.al)"}


def curl(url: str) -> bytes:
    for attempt in range(3):
        shared_throttle.wait("ia")
        try:
            # --compressed: the id_ replay of a capture stored gzip-encoded
            # comes back Content-Encoding: gzip, and without it curl saves
            # the compressed bytes as the "page" (Creandum, 2026-09-04).
            out = subprocess.run(
                ["curl", "-sfL", "--compressed", "--max-time", "90",
                 "-H", f"User-Agent: {UA['User-Agent']}", url],
                capture_output=True, check=True).stdout
            if out[:2] == b"\x1f\x8b":
                # the id_ replay hands back captures that were stored gzip-
                # encoded without the header curl --compressed keys on
                out = gzip.decompress(out)
            return out
        except subprocess.CalledProcessError as e:
            print(f"    retry {attempt+1} {url}: rc={e.returncode}", file=sys.stderr, flush=True)
            time.sleep(3)
    return b""


def fetch(url: str, dest: Path) -> str:
    if dest.exists():
        return dest.read_text(encoding="utf-8", errors="replace")
    html = curl(url).decode("utf-8", errors="replace")
    if html:
        write_atomic(dest, html)
    return html


def cdx(url_pattern: str, **params) -> list[list[str]]:
    qs = "&".join([f"url={url_pattern}", "output=json", "filter=statuscode:200",
                   *[f"{k}={v}" for k, v in params.items()]])
    data = json.loads(curl(f"https://web.archive.org/cdx/search/cdx?{qs}") or b"[]")
    if not data:
        # Degraded-CDX fallback (observed in the 2026-08-29 IA outage): the
        # statuscode-filtered query times out while the unfiltered one
        # answers. Replay follows redirects, so the worst case of an
        # unfiltered pick is a snapshot that parses to zero rows.
        qs = "&".join([f"url={url_pattern}", "output=json",
                       *[f"{k}={v}" for k, v in params.items()]])
        data = json.loads(curl(f"https://web.archive.org/cdx/search/cdx?{qs}") or b"[]")
    return data[1:] if data else []


def wb(ts: str, original: str, raw: bool = False) -> str:
    """Replay URL; raw=True asks for the id_ form (the captured bytes, no
    toolbar and no link rewriting) so an era regex can match the page's own
    hrefs — set per era with "raw": true."""
    return f"https://web.archive.org/web/{ts}{'id_' if raw else ''}/{original}"


def yearly(rows, y0, y1):
    """Pick one snapshot per year (first available)."""
    out = {}
    for row in rows:
        ts, orig = row[0], row[1]
        y = int(ts[:4])
        if y0 <= y <= y1 and y not in out:
            out[y] = (ts, orig)
    return out


def seg_of(era: dict) -> str:
    return era["path"].strip("/")


def replay_yearly(urls: list[str], y0: int, y1: int) -> dict:
    """CDX-outage fallback (COLLECTION.md §5, measured 2026-09 on Lightspeed
    and Creandum: connection-refused CDX, working replay): for each year ask
    the replay for the capture nearest three probe dates and keep the first
    whose true timestamp, read off the redirected id_ URL, falls in the year.
    `urls` are the candidate originals (the current site base and the
    http://www. form the early captures were stored under)."""
    out = {}
    for y in range(y0, y1 + 1):
        found = None
        for url in urls:
            for probe in (f"{y}0615", f"{y}0201", f"{y}1015"):
                r = subprocess.run(
                    ["curl", "-sL", "--max-time", "90", "-o", "/dev/null",
                     "-w", "%{url_effective}\n%{http_code}",
                     "-H", f"User-Agent: {UA['User-Agent']}",
                     f"https://web.archive.org/web/{probe}id_/{url}"],
                    capture_output=True)
                eff, code = (r.stdout.decode().split("\n") + ["", ""])[:2]
                m = re.search(r"/web/(\d{14})id_/(.*)$", eff)
                time.sleep(0.8)
                if code in ("429", "503"):          # replay throttling: back off, retry once
                    time.sleep(8)
                    r = subprocess.run(
                        ["curl", "-sL", "--max-time", "90", "-o", "/dev/null",
                         "-w", "%{url_effective}\n%{http_code}",
                         "-H", f"User-Agent: {UA['User-Agent']}",
                         f"https://web.archive.org/web/{probe}id_/{url}"],
                        capture_output=True)
                    eff, code = (r.stdout.decode().split("\n") + ["", ""])[:2]
                    m = re.search(r"/web/(\d{14})id_/(.*)$", eff)
                if m and m.group(1)[:4] == str(y) and code.startswith("2"):
                    found = (m.group(1), m.group(2))
                    break
            if found:
                break
        if found:
            out[y] = found
    return out


def snapshots(cfg: dict, era: dict, y0: int, y1: int, raw_dir: Path) -> dict:
    """One capture per year of the era's listing page: the CDX index when it
    answers, the replay probe when it refuses, and the era's memo
    (raw/<seg>.snapshots.json) for years an earlier run already resolved —
    replay probing is throttled under load, so a rerun keeps what it found."""
    seg = seg_of(era)
    memo = raw_dir / f"{seg.replace('/', '-')}.snapshots.json"
    known = json.loads(memo.read_text()) if memo.exists() else {}
    snaps = yearly(cdx(f"{cfg['cdx_domain']}/{seg}", collapse="timestamp:4",
                       fl="timestamp,original"), y0, y1)
    if not snaps:
        print(f"  CDX empty for {cfg['cdx_domain']}/{seg}; probing the replay per year")
        dom = cfg["cdx_domain"]
        urls = [f"{cfg['site_url_base']}{era['path']}", f"http://www.{dom}{era['path']}",
                f"http://{dom}{era['path']}"]
        missing = [y for y in range(y0, y1 + 1) if str(y) not in known]
        if missing:
            snaps = replay_yearly(list(dict.fromkeys(urls)), min(missing), max(missing))
    for y in range(y0, y1 + 1):
        if y not in snaps and str(y) in known:
            snaps[y] = tuple(known[str(y)])
    known.update({str(y): list(v) for y, v in snaps.items()})
    raw_dir.mkdir(parents=True, exist_ok=True)
    write_atomic(memo, json.dumps(known, indent=1))
    return snaps


def cdx_company_pages(era, cfg, raw_dir):
    """Per-company pages enumerated straight from the CDX index."""
    seg = seg_of(era)
    non_company = set(cfg["non_company_slugs"])
    print(f"== era {era['path']} {era['from']}-{era['to']} (CDX index)")
    rows = cdx(f"{cfg['cdx_domain']}{era['path']}*", collapse="urlkey",
               fl="timestamp,original", to=str(era["to"]), limit="2000")
    results = {}
    # A site whose company slugs are not lowercase (First Round's 2012-2017
    # /company/<Slug> pages: "Warby-Parker", "33Across") carries its own
    # slug pattern in the era; the default is the lowercase namespace every
    # earlier investor had.
    slug_re = era.get("slug_re", "[a-z0-9_-]+")
    for ts, orig in [(r[0], r[1]) for r in rows]:
        m = re.search(rf"/{seg}/({slug_re})/?(?:\?|$)", orig)
        if not m:
            continue
        slug = m.group(1)
        if slug.lower() in non_company:
            continue
        y = int(ts[:4])
        if not era["from"] <= y <= era["to"]:
            continue
        results.setdefault(y, {})[slug] = {
            "slug": slug, "path": f"/{seg}/{slug}", "snapshot_ts": ts}
    out = {}
    for y, comps in sorted(results.items()):
        out[y] = sorted(comps.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(comps)} companies (from CDX index)")
    return out


def sitemap_home_links(era, cfg, raw_dir):
    """Company hrefs on archived sitemap + homepage snapshots."""
    seg = seg_of(era)
    non_company = set(cfg["non_company_slugs"])
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (sitemap + home)")
    site_snaps = yearly(cdx(f"{cfg['cdx_domain']}/sitemap", collapse="timestamp:4",
                            fl="timestamp,original"), y0, y1)
    home_snaps = yearly(cdx(cfg["cdx_domain"], collapse="timestamp:4",
                            fl="timestamp,original"), y0, y1)
    results = {}
    for y in range(y0, y1 + 1):
        found = {}
        for src, snaps in (("sitemap", site_snaps), ("home", home_snaps)):
            if y not in snaps:
                continue
            ts, orig = snaps[y]
            html = fetch(wb(ts, orig), raw_dir / f"{y}-{src}.html")
            # Old CMSes render sector/category pages with an un-interpolated
            # template object in the alt text ('#<Region:0x..> Gaming'), while
            # company links carry the clean name ('Mixpanel'). That
            # distinguishes the two exactly, and hands us a display name too.
            linked = re.findall(
                rf'href="[^"]*?/{seg}/([a-z0-9_-]+)/?"\s+alt="([^"]*)"', html)
            for slug, alt in linked:
                if "#<" in alt or slug in non_company:
                    continue
                found[slug] = {"slug": slug, "name": unescape(alt).strip() or None,
                               "path": f"/{seg}/{slug}", "snapshot_ts": ts}
            if not linked:      # snapshots without alt attributes
                for slug in re.findall(rf'href="[^"]*?/{seg}/([a-z0-9_-]+)/?"', html):
                    if slug not in non_company:
                        found.setdefault(slug, {"slug": slug, "path": f"/{seg}/{slug}",
                                                "snapshot_ts": ts})
        if found:
            results[y] = sorted(found.values(), key=lambda c: c["slug"])
            print(f"  {y}: {len(found)} /{seg}/ paths (companies+people mixed)")
    return results


def companies_listing(era, cfg, raw_dir):
    """Single listing page: `_name` divs + data-filters attributes."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (listing page)")
    snaps = snapshots(cfg, era, y0, y1, raw_dir)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig, era.get("raw", False)), raw_dir / f"{y}-{seg}.html")
        blocks = re.findall(
            r'data-filters="([^"]*)"[^>]*data-id="([^"]+)"[^>]*>\s*<div class="_name">([^<]+)</div>', html)
        if not blocks:  # attribute order variant
            blocks = [(f, i, n) for i, f, n in re.findall(
                r'data-id="([^"]+)"[^>]*data-filters="([^"]*)"[^>]*>\s*<div class="_name">([^<]+)</div>', html)]
        rows = {}
        for filt, cid, name in blocks:
            name = unescape(name).strip()
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            rows[slug] = {"slug": slug, "name": name, "path": f"/{seg}/{cid}",
                          "filters": filt, "snapshot_ts": ts}
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
            print(f"  {y}: {len(rows)} companies")
    return results


def company_cards(era, cfg, raw_dir):
    """JS-era listing page: company-name card markup."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (card listing)")
    snaps = snapshots(cfg, era, y0, y1, raw_dir)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig, era.get("raw", False)), raw_dir / f"{y}-{seg}.html")
        rows = {}
        for name in re.findall(
                r'class="company-listing-card__company-name">\s*([^<\t\n]+)', html):
            name = unescape(name).strip()
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            if slug:
                rows[slug] = {"slug": slug, "name": name, "path": era["path"],
                              "snapshot_ts": ts}
        time.sleep(2.0)
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(rows)} entries")
    return results


def listing_regex(era, cfg, raw_dir):
    """One listing page per year; companies via the era's own markup regex
    (named groups (?P<name>...) and/or (?P<slug>...)). Markup specifics stay
    in config, mirroring site-portfolio.py's regex_list."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    non_company = set(cfg["non_company_slugs"])
    print(f"== era {era['path']} {y0}-{y1} (regex listing)")
    snaps = snapshots(cfg, era, y0, y1, raw_dir)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig, era.get("raw", False)),
                     raw_dir / f"{y}-{seg.replace('/', '-')}.html")
        rows = {}
        for m in re.finditer(era["pattern"], html):
            d = m.groupdict()
            # Collapse internal whitespace: a listing that wraps a company
            # name across source lines ("Approach\n    Software") otherwise
            # publishes the newlines and the indentation as part of the name.
            name = re.sub(r"\s+", " ",
                          unescape((d.get("name") or "")).replace("\xa0", " ")).strip() or None
            slug = d.get("slug") or (
                re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") if name else "")
            if not slug or slug in non_company:
                continue
            rows[slug] = {"slug": slug, "name": name, "path": era["path"],
                          "snapshot_ts": ts}
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(rows)} entries")
    return results


def extract_js_array(html: str, var: str):
    """The array assigned to `var`, via bracket matching (JSON-safe)."""
    m = re.search(re.escape(var) + r"\s*=\s*\[", html)
    if not m:
        return []
    start = m.end() - 1
    depth, i, instr, esc = 0, start, False, False
    while i < len(html):
        c = html[i]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
        else:
            if c == '"':
                instr = True
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    break
        i += 1
    try:
        return json.loads(html[start:i + 1])
    except json.JSONDecodeError:
        return []


def js_array_listing(era, cfg, raw_dir):
    """Listing page embedding the portfolio as a JSON array in a JS
    assignment (era config: var, name_field)."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (embedded JS array)")
    snaps = snapshots(cfg, era, y0, y1, raw_dir)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig, era.get("raw", False)), raw_dir / f"{y}-{seg}.html")
        rows = {}
        for entry in extract_js_array(html, era["var"]):
            name = unescape(str(entry.get(era.get("name_field", "title")) or "")).strip()
            if not name:
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            if slug:
                rows[slug] = {"slug": slug, "name": name, "path": era["path"],
                              "snapshot_ts": ts}
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(rows)} entries")
        time.sleep(1.0)
    return results


def nuxt_payload_listing(era, cfg, raw_dir):
    """Nuxt 2 full-static site: the archived /_nuxt/static/<build>/<route>/
    payload.js, one build per year, decoded to the CMS rows the listing was
    generated from — the server-rendered HTML of such a page carries only
    what the template renders (creandum.com/commitments: six highlight names),
    while the payload carries every row with the fields the CMS holds. The
    decoder and the Contentful flattening live in site-portfolio.py (the live
    surface reads the current build the same way)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "site_portfolio", Path(__file__).with_name("site-portfolio.py"))
    sp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sp)
    route = era["payload_route"].strip("/")
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (nuxt payload builds)")
    rows = cdx(f"{cfg['cdx_domain']}/_nuxt/static/", fl="timestamp,original",
               limit="20000", matchType="prefix")
    want = re.compile(rf"/_nuxt/static/\d+/{re.escape(route)}/payload\.js$")
    snaps = yearly([r for r in rows if want.search(r[1])], y0, y1)
    if not snaps and era.get("builds"):
        # CDX refused: the era pins one build id per year (read off the index
        # while it answered) and the replay resolves the capture.
        print("  CDX empty; using the era's pinned builds through the replay")
        for y, build in sorted(era["builds"].items()):
            url = f"{cfg['site_url_base']}/_nuxt/static/{build}/{route}/payload.js"
            got = replay_yearly([url], int(y), int(y))
            snaps.update(got)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        dest = raw_dir / f"{y}-{route}-payload.js"
        raw = dest.read_bytes() if dest.exists() \
            else curl(f"https://web.archive.org/web/{ts}id_/{orig}")
        if raw[:2] == b"\x1f\x8b":            # stored gzip-encoded (see curl())
            raw = gzip.decompress(raw)
        js = raw.decode("utf-8", "replace")
        if raw and not dest.exists():
            dest.write_bytes(raw)
            time.sleep(1.0)
        if not js.startswith("__NUXT_JSONP__"):
            print(f"  {y}: capture is not a payload ({js[:40]!r})")
            continue
        data = sp.nuxt_decode(js)
        for part in [p for p in (era.get("list_path") or "").split(".") if p]:
            if isinstance(data, list):
                data = data[int(part)] if part.isdigit() and int(part) < len(data) else []
            elif isinstance(data, dict):
                data = data.get(part) or []
        out = {}
        for entry in (data if isinstance(data, list) else []):
            f = sp.contentful_flatten(entry)
            if not isinstance(f, dict):
                continue
            name = unescape(str(f.get(era.get("name_field", "title")) or "")).strip()
            slug = str(f.get(era.get("slug_field", "slug")) or "").strip() or (
                re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") if name else "")
            if not slug:
                continue
            out[slug] = {"slug": slug, "name": name or None,
                         "path": f"/{route}/{slug}", "snapshot_ts": ts}
        if out:
            results[y] = sorted(out.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(out)} entries (build {orig.rsplit('/static/', 1)[-1].split('/')[0]}, {ts})")
    return results


PARSERS = {
    "cdx_company_pages": cdx_company_pages,
    "sitemap_home_links": sitemap_home_links,
    "companies_listing": companies_listing,
    "company_cards": company_cards,
    "listing_regex": listing_regex,
    "js_array_listing": js_array_listing,
    "nuxt_payload_listing": nuxt_payload_listing,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    args = ap.parse_args()

    p = Paths(args.investor)
    cfg = p.config()["wayback"]
    raw, parsed = p.wayback / "raw", p.wayback / "parsed"
    raw.mkdir(parents=True, exist_ok=True)
    parsed.mkdir(parents=True, exist_ok=True)

    all_years = {}
    for era in cfg["eras"]:
        # A firm that changed domains keeps one config: an era may carry its
        # own cdx_domain (Lightspeed: lightspeedvp.com 2000-2012, lsvp.com
        # after), falling back to the investor-level domain.
        era_cfg = {**cfg, "cdx_domain": era.get("cdx_domain", cfg["cdx_domain"]),
                   "site_url_base": era.get("site_url_base", cfg["site_url_base"])}
        for y, rows in PARSERS[era["parser"]](era, era_cfg, raw).items():
            all_years.setdefault(y, []).extend(rows)
    for y, rows in sorted(all_years.items()):
        # Merge with what the year file already holds rather than replacing:
        # the Common Crawl layer (commoncrawl-pull.py) writes the same
        # per-year shape from a different capture universe (per-company
        # pages vs listing snapshots), and each source must survive the
        # other's re-runs. Keyed by (slug, path); existing rows win.
        dest = parsed / f"{y}.json"
        merged = {(r["slug"], r.get("path")): r
                  for r in (json.loads(dest.read_text()) if dest.exists() else [])}
        for r in rows:
            merged.setdefault((r["slug"], r.get("path")), r)
        write_atomic(parsed / f"{y}.json", json.dumps(
            sorted(merged.values(), key=lambda r: (r["slug"], r.get("path") or "")),
            indent=1) + "\n")
    total = {r["slug"] for rows in all_years.values() for r in rows}
    print(f"\nyears: {sorted(all_years)}\ndistinct slugs across all years: {len(total)}")


if __name__ == "__main__":
    main()
