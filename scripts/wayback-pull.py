#!/usr/bin/env python3
"""Pull annual Wayback snapshots of an investor's portfolio pages and parse
them into per-year company lists.

Everything investor-specific — the domain, the era map (which path pattern the
site used in which years, and which parser understands that era's markup), and
the non-company slug list — lives in the investor's config.json under
"wayback". The parsers themselves are named strategies in code; an investor's
era entry picks one:

  cdx_company_pages   per-company pages enumerated straight from the CDX index
  sitemap_home_links  hrefs on archived sitemap + homepage snapshots
  companies_listing   single listing page, `_name` divs + data-filters
  company_cards       JS-era listing page, company-name card markup
  listing_regex       one listing page per year; era config carries the
                      markup regex (named groups name and/or slug)
  js_array_listing    listing page embedding a JSON array in a JS
                      assignment (era config: var, name_field)
  nuxt_payload_listing a Nuxt full-static site's archived per-route
                      payload.js, one build per year, decoded to the CMS rows
                      the listing was generated from (era config:
                      payload_route, list_path, name_field, slug_field)

Raw HTML -> <investor>/sources/wayback/raw/
Parsed   -> <investor>/sources/wayback/parsed/<year>.json
            rows: {slug, name?, path, filters?, snapshot_ts}

Usage: python3 scripts/wayback-pull.py <investor-slug>
"""
import argparse
import gzip
import json
import re
from urllib.parse import quote
import sys
import time
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths, write_atomic  # noqa: E402
import ia_fetch  # noqa: E402

UA = {"User-Agent": "MeritCapitalResearch/1.0 (erik@meritcapit.al)"}


def curl(url: str) -> bytes:
    """Body of `url`, or b"" if IA would not give us one.

    Thin wrapper over the shared status-aware fetch. b"" now means ONLY
    "no body"; callers that must distinguish an empty answer from a failed
    request use `curl_status` instead.
    """
    return curl_status(url)[0]


def curl_status(url: str) -> tuple[bytes, str]:
    """(body, code) — "200", "404", "rc7" for the firewall block, ...

    Replaces `curl -sfL ... check=True`, which collapsed 429, 503 and 404
    into one generic failure and retried a rate-limit warning after 3 s.
    That retry loop is what earned the hour-long IA block (PRO-128).
    """
    body, code = ia_fetch.get(url)
    if body[:2] == b"\x1f\x8b":
        # the id_ replay hands back captures that were stored gzip-encoded
        # without the header curl --compressed keys on (Creandum, 2026-09-04)
        try:
            body = gzip.decompress(body)
        except OSError:
            pass
    return body, code


def fetch(url: str, dest: Path) -> str:
    if dest.exists():
        return dest.read_text(encoding="utf-8", errors="replace")
    html = curl(url).decode("utf-8", errors="replace")
    if html:
        write_atomic(dest, html)
    return html


def cdx(url_pattern: str, **params) -> list[list[str]]:
    """CDX rows for `url_pattern`, [] when the index genuinely holds none."""
    def query(**extra) -> tuple[list, str]:
        qs = "&".join([f"url={url_pattern}", "output=json",
                       *[f"{k}={v}" for k, v in {**params, **extra}.items()]])
        body, code = curl_status(f"https://web.archive.org/cdx/search/cdx?{qs}")
        try:
            return json.loads(body or b"[]"), code
        except ValueError:
            return [], code

    data, code = query(**{"filter": "statuscode:200"})
    if not data and code == "200":
        # Degraded-CDX fallback (the 2026-08-29 outage): the statuscode-
        # filtered query can answer empty while the unfiltered one has rows.
        # Gated on a GENUINE empty 200 — before PRO-128 this fired on any
        # falsy result, including a failed request, so every failure doubled
        # our traffic exactly when IA was least able to take it.
        data, code = query()
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


def ia_replay_probe(url: str, probe: str) -> tuple[str, str]:
    """One replay probe, paced and status-aware -> (effective_url, code).

    Pacing, the 429 Retry-After honour, the 503 backoff and the firewall
    cooldown all live in `ia_fetch`; this is here so `replay_yearly` reads
    the same way it always did.
    """
    return ia_fetch.probe(url, probe)


def replay_yearly(urls: list[str], y0: int, y1: int) -> dict:
    """CDX-outage fallback (COLLECTION.md §5, measured 2026-09 on Lightspeed
    and Creandum: connection-refused CDX, working replay): for each year ask
    the replay for the capture nearest three probe dates and keep the first
    whose true timestamp, read off the redirected id_ URL, falls in the year.
    `urls` are the candidate originals (the current site base and the
    http://www. form the early captures were stored under).

    The search stops at the first hit, so a year that resolves on the current
    base costs ONE probe and only a year that resolves nowhere costs the full
    grid (len(urls) x 3). PRO-127 briefly added a two-pass "cap" on top of
    this; measured against the same synthetic archives it issued exactly the
    same number of probes in every case, because this short-circuit was
    already doing the work. What was actually wrong was that the probes
    bypassed the rate bucket — see `ia_replay_probe`.
    """
    if not urls:
        return {}
    out: dict = {}
    unreachable: list = []
    probes = 0
    years = list(range(y0, y1 + 1))
    for y in years:
        found = None
        for url in urls:
            for probe in (f"{y}0615", f"{y}0201", f"{y}1015"):
                probes += 1
                eff, code = ia_replay_probe(url, probe)
                if code.startswith("rc"):
                    # A refused connection and a year with genuinely no
                    # capture must not look alike: record it as unreachable
                    # and say so below, never as an empty year (12402a7).
                    unreachable.append(f"{y}/{probe}")
                    continue
                m = re.search(r"/web/(\d{14})id_/(.*)$", eff)
                if m and m.group(1)[:4] == str(y) and code.startswith("2"):
                    found = (m.group(1), m.group(2))
                    break
            if found:
                break
        if found:
            out[y] = found

    print(f"  replay probes: {probes} for {len(years)} era-year(s), "
          f"{len(out)} resolved (worst case would be {len(years) * len(urls) * 3})")
    if unreachable:
        print(f"  !! replay probe could not connect on {len(unreachable)} "
              f"probe(s): {', '.join(unreachable[:8])}"
              f"{' ...' if len(unreachable) > 8 else ''}")
        print("     Those years are UNKNOWN, not empty — re-run this era "
              "before reading any absence off it.")
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
    # CDX answers at most `limit` rows per query, and 2000 is the whole
    # namespace for a curated portfolio page. A directory is not: YC's
    # /companies/* namespace is larger than the cap, and a single query
    # returns one alphabetical slice ("0" through "A") while silently
    # dropping the rest — the layer then reports survivorship over 4% of
    # the site and looks like it worked. `cdx_pages` opts an era into
    # paging the index through CDX's own resumption key; its absence keeps
    # the single capped query every earlier investor ran.
    pages = int(era.get("cdx_pages") or 0)
    lim = str(era.get("cdx_limit") or 2000)
    if pages:
        rows, resume, seen_pages = [], None, 0
        while seen_pages < pages:
            kw = {"showResumeKey": "true", "limit": lim}
            if resume:
                kw["resumeKey"] = quote(resume, safe="")
            batch = cdx(f"{cfg['cdx_domain']}{era['path']}*", collapse="urlkey",
                        fl="timestamp,original", to=str(era["to"]), **kw)
            # The resume key is returned as the last row after a blank row.
            resume = None
            while batch and (not batch[-1] or not batch[-1][0]):
                batch.pop()
            if batch and len(batch[-1]) == 1:
                resume = batch.pop()[0]
                while batch and (not batch[-1] or not batch[-1][0]):
                    batch.pop()
            rows.extend(batch)
            seen_pages += 1
            print(f"  cdx page {seen_pages}: +{len(batch)} rows "
                  f"({len(rows)} total){'' if resume else ' — end of index'}")
            if not resume:
                break
    else:
        rows = cdx(f"{cfg['cdx_domain']}{era['path']}*", collapse="urlkey",
                   fl="timestamp,original", to=str(era["to"]), limit=lim)
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
        # Merge with what the year file already holds rather than replacing.
        # Do NOT "simplify" this to a write: a retired second archive wrote
        # the same per-year shape from a different capture universe
        # (per-company pages vs listing snapshots) and those rows are no
        # longer reproducible, so replacing would silently delete them.
        # Keyed by (slug, path); existing rows win.
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
