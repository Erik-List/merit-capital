#!/usr/bin/env python3
"""Ribbit's archived portfolio listings, three site eras, every distinct capture.

  bets      2012-2015  WordPress 3.5 /bets/: <h3 class="company-..."><a title="NAME">
                       per company, plus a one-line description; the 2012-2014
                       homepage slider carries the same names (<dt class="company-...">)
  our-bets  2015-2024  WordPress /our-bets/: one <a href="COMPANY_URL" alt="COUNTRY">
                       <img src=".../uploads/..."> per company. No name in the markup:
                       the firm's own link names the company, the alt is the firm's
                       own country label, the upload filename is the logo
  rebels    2025-2026  Next.js /rebels: the page chunk's array, name + founders +
                       companyUrl per row (the live layer, scratch/pull-site.py, reads
                       the current chunk; this reads the archived ones)

Why not wayback-pull.py: its listing_regex era keeps only a name and a slug, and
the our-bets era has neither in the markup; what identifies a row there is the
company URL, which that parser drops. A capture is fetched once into
sources/wayback/raw/ and never re-fetched.

Step 1 (network): python3 scratch/wayback-ribbit.py fetch
   -> sources/wayback/raw/<era>-<ts>.html|js, sources/wayback/captures.json
Step 2 (offline): python3 scratch/wayback-ribbit.py parse
   -> sources/wayback/parsed/<year>.json, through the curated identity map
      sources/wayback/identity-map.json (company URL host or era-1 name -> slug, name)

A failed fetch is recorded as failed, never as an empty capture.
"""
import json
import re
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import ia_fetch  # noqa: E402

P = Paths("ribbit-capital")
WB = P.wayback
RAW = WB / "raw"
CAPS = WB / "captures.json"
IDMAP = WB / "identity-map.json"

ERAS = {
    "bets": {"urls": ["http://ribbitcap.com/bets/"], "years": (2012, 2015), "path": "/bets/"},
    "home": {"urls": ["http://ribbitcap.com/"], "years": (2012, 2014), "path": "/"},
    "our-bets": {"urls": ["http://ribbitcap.com/our-bets/"], "years": (2015, 2025), "path": "/our-bets/"},
    # people pages, for the sweep roster's tenure windows (scratch/build-roster.py)
    "about": {"urls": ["http://ribbitcap.com/about/"], "years": (2012, 2015), "path": "/about/"},
    "team": {"urls": ["http://ribbitcap.com/team/"], "years": (2015, 2025), "path": "/team/"},
}
PROBES = ("0201", "0615", "1015")


def cdx_versions(url: str) -> list[tuple[str, str]] | None:
    """Every distinct body (collapse=digest) of one URL, or None when the
    index does not answer (then the caller probes the replay instead)."""
    q = (f"https://web.archive.org/cdx/search/cdx?url={url}&fl=timestamp,original,statuscode"
         f"&collapse=digest&output=json&filter=statuscode:200")
    try:
        body, status = ia_fetch.get(q)
    except Exception as e:  # noqa: BLE001
        print(f"  cdx failed for {url}: {e}")
        return None
    if not status.startswith("2") or not body.strip().startswith(b"["):
        print(f"  cdx {status} for {url}")
        return None
    rows = json.loads(body)
    return [(r[0], r[1]) for r in rows[1:]]


def probe_versions(urls: list[str], y0: int, y1: int) -> list[tuple[str, str]]:
    found: dict[str, str] = {}
    for y in range(y0, y1 + 1):
        for url in urls:
            for d in PROBES:
                eff, code = ia_fetch.probe(url, f"{y}{d}")
                m = re.search(r"/web/(\d{14})id_/(.*)$", eff)
                if code.startswith("2") and m and m.group(1)[:4] == str(y):
                    found.setdefault(m.group(1), m.group(2))
    return sorted(found.items())


def save(caps: dict) -> None:
    """Merge with what is on disk: scratch/cc-fetch.py registers Common Crawl
    captures in the same file while this runs, and neither may drop the other's."""
    if CAPS.exists():
        disk = json.loads(CAPS.read_text())
        mine = {(c["era"], c["ts"]) for c in caps["captures"]}
        caps["captures"] += [c for c in disk["captures"] if (c["era"], c["ts"]) not in mine]
    caps["captures"].sort(key=lambda c: (c["era"], c["ts"]))
    write_atomic(CAPS, json.dumps(caps, indent=1) + "\n")


def fetch() -> None:
    caps = json.loads(CAPS.read_text()) if CAPS.exists() else {"captures": [], "failed": []}
    have = {(c["era"], c["ts"]) for c in caps["captures"]}
    # A raw file already on disk is a capture already fetched (an earlier run
    # stopped before it saved): register it rather than fetch it again.
    for f in sorted(RAW.glob("*-*")):
        m = re.match(r"(bets|home|our-bets|rebels|about|team)-(\d{14})\.(html|js)$", f.name)
        if m and (m.group(1), m.group(2)) not in have:
            era, ts = m.group(1), m.group(2)
            orig = ERAS[era]["urls"][0] if era in ERAS else ""
            caps["captures"].append({"era": era, "ts": ts, "original": orig,
                                     "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                                     "raw": str(f.relative_to(P.root)), "registered_from_disk": True})
            have.add((era, ts))
    save(caps)
    failed = []
    RAW.mkdir(parents=True, exist_ok=True)
    for era, cfg in ERAS.items():
        y0, y1 = cfg["years"]
        versions: dict[str, str] = {}
        url = cfg["urls"][0]
        v = None
        for attempt in range(3):
            v = cdx_versions(url)
            if v is not None:
                break
        if v is None:
            # http and https share one urlkey in the replay, so one URL form
            # per era is enough for the probes
            versions.update(dict(probe_versions([url], y0, y1)))
        else:
            versions.update(dict(v))
        versions = {ts: o for ts, o in versions.items() if y0 <= int(ts[:4]) <= y1}
        print(f"== {era}: {len(versions)} distinct capture(s)")
        for ts, orig in sorted(versions.items()):
            if (era, ts) in have:
                continue
            dest = RAW / f"{era}-{ts}.html"
            url = f"https://web.archive.org/web/{ts}id_/{orig}"
            try:
                body, status = ia_fetch.get(url)
            except Exception as e:  # noqa: BLE001
                failed.append({"era": era, "ts": ts, "url": url, "error": str(e)})
                continue
            if not status.startswith("2") or not body:
                failed.append({"era": era, "ts": ts, "url": url, "error": f"http {status}"})
                continue
            dest.write_bytes(body)
            caps["captures"].append({"era": era, "ts": ts, "original": orig,
                                     "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                                     "raw": str(dest.relative_to(P.root))})
            save(caps)
            print(f"  {ts} {len(body)} bytes", flush=True)
    # rebels: the archived page chunks named in the domain index
    dom = WB / "cdx-domain.json"
    if dom.exists():
        rows = json.loads(dom.read_text())[1:]
        chunks = sorted({(r[0], r[1]) for r in rows
                         if "/app/rebels/page-" in r[1] and r[2] == "200"})
        print(f"== rebels: {len(chunks)} archived page chunk(s)")
        for ts, orig in chunks:
            if ("rebels", ts) in have:
                continue
            url = f"https://web.archive.org/web/{ts}id_/{orig}"
            try:
                body, status = ia_fetch.get(url)
            except Exception as e:  # noqa: BLE001
                failed.append({"era": "rebels", "ts": ts, "url": url, "error": str(e)})
                continue
            if not status.startswith("2") or not body:
                failed.append({"era": "rebels", "ts": ts, "url": url, "error": f"http {status}"})
                continue
            dest = RAW / f"rebels-{ts}.js"
            dest.write_bytes(body)
            caps["captures"].append({"era": "rebels", "ts": ts, "original": orig,
                                     "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                                     "raw": str(dest.relative_to(P.root))})
            save(caps)
            print(f"  {ts} {len(body)} bytes", flush=True)
    caps["failed"] = failed
    save(caps)
    print(f"captures: {len(caps['captures'])}, failed this run: {len(failed)}")


def host(url: str | None) -> str | None:
    if not url:
        return None
    m = re.match(r"(?:https?:)?//([^/?#]+)", url.strip())
    if not m:
        return None
    h = m.group(1).lower()
    return h[4:] if h.startswith("www.") else h


def rows_of(cap: dict) -> list[dict]:
    """The listing rows one capture carries, before identity mapping."""
    text = (P.root / cap["raw"]).read_bytes().decode("utf-8", errors="replace")
    era = cap["era"]
    out = []
    if era in ("team", "about"):
        return []                       # people pages: scratch/build-roster.py reads them
    if era == "bets":
        # the anchor text is the name; only some anchors carry a title attribute
        for m in re.finditer(r'<h3 class="(company-[^"]*)"[^>]*>\s*<a(?:\s+title="[^"]*")?\s+href="([^"]*)"[^>]*>([^<]+)</a>', text):
            nxt = text[m.end():m.end() + 600]
            d = re.search(r'<blockquote[^>]*>\s*<p>(.*?)</p>', nxt, re.S)
            out.append({"name": unescape(m.group(3)).strip(), "css": m.group(1).split()[0],
                        "page": m.group(2), "about": unescape(re.sub(r"<[^>]+>", "", d.group(1))).strip() if d else None})
        # late 2014 to 2015: a logo grid, <div class="company"><a href=COMPANY_URL>
        # <img src=.../company-<slug>-large.png class="company-<slug>"> (no name)
        for m in re.finditer(r'<div class="company">\s*<a href="([^"]*)"[^>]*>\s*<img src="([^"]+)"[^>]*class="([^"]*)"', text):
            out.append({"company_url": unescape(m.group(1)).strip() or None,
                        "logo": m.group(2).rsplit("/", 1)[-1], "css": m.group(3)})
    elif era == "home":
        for m in re.finditer(r'<a href="([^"]*)"><dl><dt class="([^"]*)">([^<]+)</dt><dd>(.*?)</dd>', text):
            out.append({"name": unescape(m.group(3)).strip(), "css": m.group(2), "page": m.group(1),
                        "about": unescape(m.group(4)).strip()})
    elif era == "our-bets":
        for m in re.finditer(r'<a href="([^"]*)"\s+alt="([^"]*)"\s*>\s*<img src="([^"]+)"', text):
            logo = m.group(3).split("/uploads/")[-1] if "/uploads/" in m.group(3) else m.group(3)
            out.append({"company_url": unescape(m.group(1)).strip() or None,
                        "country_label": unescape(m.group(2)).strip() or None, "logo": logo})
    elif era == "rebels-page":
        # the live-era page as captured: one scrollable-list-item per company,
        # "<span class=truncate>NAME</span><span ...>founders</span>"
        for m in re.finditer(r'data-type="scrollable-list-item"[^>]*>(.*?)</div>', text, re.S):
            spans = re.findall(r'<span class="truncate">(.*?)</span>', m.group(1), re.S)
            if spans:
                out.append({"name": unescape(re.sub(r"<[^>]+>", "", spans[0])).strip()})
    elif era == "rebels":
        for m in re.finditer(r'\{name:"((?:[^"\\]|\\.)*)",founderNames:\[(.*?)\],'
                             r'companyUrl:(null|"(?:[^"\\]|\\.)*")', text):
            s = re.sub(r"\\x([0-9a-fA-F]{2})", r"\\u00\1", m.group(1).replace("\\'", "'"))
            cu = None if m.group(3) == "null" else m.group(3)[1:-1]
            out.append({"name": json.loads(f'"{s}"').strip(), "company_url": cu})
    return out


def key_of(era: str, r: dict) -> str:
    """The identity-map key of a row. An era that renders names is keyed by
    the firm's own rendering; the our-bets era renders none, so its rows are
    keyed by the host of the firm's own link (or the logo file where the link
    is empty)."""
    if r.get("name"):
        return "name:" + r["name"].lower()
    h = host(r.get("company_url"))
    return h if h else "logo:" + r["logo"]


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def parse() -> None:
    caps = json.loads(CAPS.read_text())
    idmap = {k: v for k, v in (json.loads(IDMAP.read_text()) if IDMAP.exists() else {}).items() if not k.startswith("_")}
    unmapped: dict[str, dict] = {}
    by_year: dict[int, dict] = {}
    for cap in caps["captures"]:
        era, ts = cap["era"], cap["ts"]
        if era in ("team", "about"):
            continue
        rows = rows_of(cap)
        if not rows:
            print(f"  !! {era} {ts}: 0 rows from {cap['raw']} (parser hypothesis failed, not an absence)")
        for r in rows:
            k = key_of(era, r)
            ident = idmap.get(k)
            if ident is None and r.get("name"):
                # the firm rendered the name: it owns name and slug
                ident = {"slug": slugify(r["name"]), "name": r["name"]}
            if ident is None:
                unmapped.setdefault(k, {"era": era, "first_ts": ts, **r})
                continue
            if ident.get("skip"):
                continue
            y = int(ts[:4])
            row = {"slug": ident["slug"], "name": ident["name"],
                   "path": ERAS.get(era, {}).get("path", "/rebels"),
                   "snapshot_ts": ts, "era": era, "source": "wayback-listing",
                   "capture_url": cap["capture_url"]}
            for f in ("company_url", "country_label", "logo", "about"):
                if r.get(f):
                    row[f] = r[f]
            by_year.setdefault(y, {}).setdefault((row["slug"], row["path"]), row)
    if unmapped:
        write_atomic(WB / "unmapped.json", json.dumps(unmapped, indent=1, ensure_ascii=False) + "\n")
        print(f"!! {len(unmapped)} row key(s) have no identity-map entry; see sources/wayback/unmapped.json")
        return
    (WB / "unmapped.json").unlink(missing_ok=True)
    (WB / "parsed").mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(by_year.items()):
        write_atomic(WB / "parsed" / f"{y}.json", json.dumps(
            sorted(rows.values(), key=lambda r: (r["slug"], r["path"])), indent=1, ensure_ascii=False) + "\n")
        print(f"  {y}: {len(rows)} rows")
    slugs = {s for rows in by_year.values() for (s, _) in rows}
    print(f"distinct companies across the archive: {len(slugs)}")


if __name__ == "__main__":
    {"fetch": fetch, "parse": parse}[sys.argv[1]]()
