#!/usr/bin/env python3
"""Common Crawl WITHOUT the query API.

`commoncrawl-pull.py` asks index.commoncrawl.org, and on 2026-09-07 that host
answered nothing for hours (connection refused on every probe) while the
Internet Archive was refusing too -- both capture archives down at once, with
the run's whole archive layer behind them.  data.commoncrawl.org stayed up and
serves HTTP range requests, and the query API is only a front end over files
that live there, so the index can be read directly:

  cc-index/collections/<crawl>/indexes/cluster.idx   sorted SURT -> (shard, offset, length)
  cc-index/collections/<crawl>/indexes/cdx-000NN.gz  the CDXJ blocks themselves

cluster.idx is ~118 MB and sorted, so a binary search over byte offsets finds
the blocks covering a SURT prefix in about two dozen range requests; each block
is one gzip member that inflates on its own.  The WARC bodies come the same
way, by range request against the crawl's own warc path.

Writes wayback-pull's shapes so the two layers converge:
  sources/wayback/raw/cc-<crawl>-<slug>.html   the captured body
  sources/wayback/parsed/<year>.json           merged per-year rows (slug+path keyed)

Usage:
  python3 cc-direct.py index                 # enumerate captures into cc-index.json
  python3 cc-direct.py fetch [--max N]       # pull bodies + write parsed years
"""
import gzip, io, json, os, re, sys, time, urllib.parse, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/greylock"
WB = INV / "sources/wayback"
IDX_OUT = INV / "scratch/cc-index.json"
BASE = "https://data.commoncrawl.org"
UA = "merit-capital-research/1.0 (erik@meritcapit.al)"
SURT = "com,greylock)"


def get(url, rng=None, tries=4):
    """Range GET through curl (the machine's Python has no CA bundle for these
    hosts, and curl is what every other puller in this repo already uses)."""
    cmd = ["curl", "-sS", "--compressed" if rng is None else "-s", "--max-time", "120",
           "-A", UA, url]
    if rng:
        cmd = ["curl", "-sS", "--max-time", "120", "-A", UA, "-r", rng, url]
    for i in range(tries):
        p = subprocess.run(cmd, capture_output=True)
        if p.returncode == 0 and p.stdout:
            return p.stdout
        time.sleep(1.5 * (i + 1))
    return b""


def cluster_blocks(crawl, prefix):
    """Binary-search cluster.idx for every block that can hold `prefix`."""
    url = f"{BASE}/cc-index/collections/{crawl}/indexes/cluster.idx"
    head = subprocess.run(["curl", "-sSI", "--max-time", "60", "-A", UA, url],
                          capture_output=True).stdout.decode("utf-8", "replace")
    m = re.search(r"(?im)^content-length:\s*(\d+)", head)
    if not m:
        return []
    size = int(m.group(1))

    def line_at(pos):
        """The first complete line at or after `pos`, plus its start offset."""
        chunk = get(url, f"{pos}-{min(pos + 65535, size - 1)}")
        if not chunk:
            return None, None
        nl = chunk.find(b"\n")
        if pos and nl >= 0:
            start = pos + nl + 1
            rest = chunk[nl + 1:]
        else:
            start, rest = pos, chunk
        nl2 = rest.find(b"\n")
        return rest[:nl2 if nl2 >= 0 else len(rest)].decode("utf-8", "replace"), start

    lo, hi, found = 0, size, 0
    while lo < hi:                      # last line whose key <= prefix
        mid = (lo + hi) // 2
        line, start = line_at(mid)
        if line is None:
            break
        key = line.split(" ", 1)[0]
        if key <= prefix:
            found = start
            lo = mid + 1
        else:
            hi = mid
    # Read forward from a little before the hit and keep every block whose key
    # sorts below the prefix's upper bound; the block BEFORE the first match
    # can still contain it, which is why the scan starts one line early.
    blocks, pos = [], max(0, found - 4096)
    upper = prefix[:-1] + chr(ord(prefix[-1]) + 1)
    while pos < size:
        chunk = get(url, f"{pos}-{min(pos + 262143, size - 1)}")
        if not chunk:
            break
        text = chunk.decode("utf-8", "replace")
        lines = text.split("\n")
        if pos:
            lines = lines[1:]
        stop = False
        for ln in lines:
            parts = ln.split("\t")
            if len(parts) < 4:
                continue
            key = parts[0].split(" ", 1)[0]
            if key >= upper:
                stop = True
                break
            blocks.append((parts[1], int(parts[2]), int(parts[3]), key))
        if stop:
            break
        pos += 262144
    # Keep the last block whose key < prefix (it can hold the first match) and
    # every block from there to the upper bound.
    keep, prev = [], None
    for b in blocks:
        if b[3] < prefix:
            prev = b
            continue
        if prev:
            keep.append(prev)
            prev = None
        keep.append(b)
    if not keep and prev:
        keep = [prev]
    return keep


def cdx_rows(crawl, blocks, prefix):
    out = []
    for shard, off, length, _ in blocks:
        raw = get(f"{BASE}/cc-index/collections/{crawl}/indexes/{shard}",
                  f"{off}-{off + length - 1}")
        if not raw:
            continue
        try:
            text = gzip.decompress(raw).decode("utf-8", "replace")
        except OSError:
            continue
        for ln in text.split("\n"):
            if not ln.startswith(prefix):
                continue
            try:
                key, ts, blob = ln.split(" ", 2)
                rec = json.loads(blob)
            except ValueError:
                continue
            rec["urlkey"], rec["timestamp"], rec["crawl"] = key, ts, crawl
            out.append(rec)
    return out


def do_index(crawls):
    seen = json.loads(IDX_OUT.read_text()) if IDX_OUT.exists() else {}
    for crawl in crawls:
        if crawl in seen:
            print(f"  {crawl}: cached ({len(seen[crawl])})")
            continue
        blocks = cluster_blocks(crawl, SURT)
        rows = cdx_rows(crawl, blocks, SURT) if blocks else []
        seen[crawl] = rows
        IDX_OUT.parent.mkdir(parents=True, exist_ok=True)
        IDX_OUT.write_text(json.dumps(seen))
        print(f"  {crawl}: {len(blocks)} blocks, {len(rows)} captures")
    return seen


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "index"
    crawls = [c.strip() for c in
              (pathlib.Path(sys.argv[2]).read_text().split()
               if len(sys.argv) > 2 else [])]
    if mode == "index":
        do_index(crawls)


# --------------------------------------------------------------------------
# fetch: pull the bodies of the LIST pages CC captured and parse them with the
# era patterns from config.json, writing wayback-pull's own parsed shape so the
# two capture layers merge per year (keyed slug+path, COLLECTION.md §5).

def warc_body(rec):
    off, ln = int(rec["offset"]), int(rec["length"])
    raw = get(f"{BASE}/{rec['filename']}", f"{off}-{off + ln - 1}")
    if not raw:
        return ""
    try:
        blob = gzip.decompress(raw)
    except OSError:
        return ""
    txt = blob.decode("utf-8", "replace")
    j = txt.find("\r\n\r\n", txt.find("\r\n\r\n") + 4)
    return txt[j + 4:] if j > 0 else ""


def do_fetch(limit=None):
    from html import unescape
    cfg = json.loads((INV / "config.json").read_text())
    eras = [e for e in cfg["wayback"]["eras"] if e["parser"] == "listing_regex"]
    non = set(cfg["wayback"]["non_company_slugs"])
    idx = json.loads(IDX_OUT.read_text())

    # Which captured URL can an era read? Match on the path, ignoring the query
    # for the eras whose query is only a client-side filter (2011-2017: any
    # ?sector= page ships the whole book).
    def eras_for(url):
        """Every era that can read this URL, not the first: two eras read the
        same /portfolio page through different markup (the visually-hidden
        spans and the upload filenames), and returning one of them silently
        drops the other's 80-odd rows."""
        path = re.sub(r"^https?://[^/]+", "", url)
        bare = path.split("?")[0].rstrip("/") or "/"
        out = []
        for e in eras:
            ep = e["path"].split("?")[0].rstrip("/") or "/"
            if bare != ep:
                continue
            if "?" in e["path"] and "?" not in path and ep not in ("/companies",):
                continue
            out.append(e)
        return out

    picked, raw_dir = {}, WB / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    for crawl, rows in idx.items():
        for r in rows:
            if r.get("status") != "200" or "html" not in (r.get("mime") or ""):
                continue
            for e in eras_for(r["url"]):
                y = int(r["timestamp"][:4])
                if not (e["from"] <= y <= e["to"]):
                    continue
                key = (y, e["path"])
                # one capture per year per era, the earliest in the year
                if key not in picked or r["timestamp"] < picked[key]["timestamp"]:
                    picked[key] = r
    print(f"list-page captures to fetch: {len(picked)}")
    parsed_dir = WB / "parsed"
    parsed_dir.mkdir(parents=True, exist_ok=True)
    done = 0
    for (y, path), rec in sorted(picked.items()):
        if limit and done >= limit:
            break
        era = next(e for e in eras if e["path"] == path)
        seg = path.strip("/").replace("/", "-")
        dest = raw_dir / f"{y}-{seg}.cc.html"
        html = dest.read_text(encoding="utf-8", errors="replace") if dest.exists() else warc_body(rec)
        if not html:
            print(f"  {y} {path}: empty body"); continue
        if not dest.exists():
            dest.write_text(html, encoding="utf-8")
        rows = {}
        for m in re.finditer(era["pattern"], html):
            d = m.groupdict()
            name = re.sub(r"\s+", " ", unescape(d.get("name") or "").replace("\xa0", " ")).strip() or None
            slug = d.get("slug") or (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") if name else "")
            if not slug or slug in non:
                continue
            rows[slug] = {"slug": slug, "name": name, "path": path,
                          "snapshot_ts": rec["timestamp"]}
        # merge into the year file, exactly as wayback-pull's own re-runs do
        pf = parsed_dir / f"{y}.json"
        cur = {(c["slug"], c["path"]): c for c in
               (json.loads(pf.read_text()) if pf.exists() else [])}
        for c in rows.values():
            cur[(c["slug"], c["path"])] = c
        pf.write_text(json.dumps(sorted(cur.values(), key=lambda c: c["slug"]), indent=1))
        print(f"  {y} {path}: {len(rows)} rows  (year file now {len(cur)})")
        done += 1


if len(sys.argv) > 1 and sys.argv[1] == "fetch":
    do_fetch(int(sys.argv[2]) if len(sys.argv) > 2 else None)


# --------------------------------------------------------------------------
# cards: the Rails era's per-company partials. /companies/<id> in 2013-2014 is
# a 600-byte fragment carrying the name, the one-line sector, the website, the
# OUTCOME LINE ("Merged with Creative BioMolecules in 2000") and the GREYLOCK
# PARTNER on the deal -- the same four columns the 1999-2010 listings publish,
# for the one stretch of the book where no other surface has them. The Internet
# Archive enumerated this namespace as numeric ids only.

def do_cards():
    idx = json.loads(IDX_OUT.read_text())
    best = {}
    for crawl, rows in idx.items():
        for r in rows:
            if r.get("status") != "200":
                continue
            u = re.sub(r"^https?://[^/]+", "", r["url"]).split("?")[0]
            m = re.match(r"^/(?:greylock-)?companies/(\d+)/?$", u)
            if not m:
                continue
            cid = m.group(1)
            # prefer the earliest capture: the later WordPress wrapper renders
            # the same id as a JS shell with no company in it.
            if cid not in best or r["timestamp"] < best[cid]["timestamp"]:
                best[cid] = r
    print(f"per-company partials: {len(best)}")
    out_path = INV / "sources/site/rails-cards.json"
    have = json.loads(out_path.read_text())["companies"] if out_path.exists() else {}
    for n, (cid, rec) in enumerate(sorted(best.items(), key=lambda kv: int(kv[0])), 1):
        if cid in have:
            continue
        html = warc_body(rec)
        if not html:
            continue
        name = re.search(r"<h2>\s*(.*?)\s*</h2>", html, re.S)
        if not name:
            continue
        desc = re.search(r"<h4>\s*(.*?)\s*</h4>", html, re.S)
        site = re.search(r'class="link">\s*<a href="([^"]+)"', html)
        bottom = re.findall(r"<p>(?!Partner:)\s*(.*?)\s*</p>", html, re.S)
        partner = re.search(r"Partner:\s*<span[^>]*>\s*(.*?)\s*</span>", html, re.S)
        strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip() or None
        have[cid] = {"id": cid, "name": strip(name.group(1)), "desc": strip(desc.group(1) if desc else None),
                     "website": site.group(1) if site else None,
                     "status_line": strip(bottom[0]) if bottom else None,
                     "partners": [strip(partner.group(1))] if partner else [],
                     "snapshot_ts": rec["timestamp"], "url": rec["url"]}
        if n % 25 == 0:
            print(f"  {n}/{len(best)} …")
            out_path.write_text(json.dumps({"_readme": README_CARDS, "companies": have}, indent=1))
    out_path.write_text(json.dumps({"_readme": README_CARDS, "companies": have}, indent=1))
    named = [c for c in have.values() if c.get("name")]
    print(f"wrote {out_path} — {len(named)} named companies, "
          f"{sum(1 for c in named if c.get('status_line'))} with an outcome line, "
          f"{sum(1 for c in named if c.get('partners'))} with a partner")


README_CARDS = (
    "Greylock's 2011-2014 Rails site served each company as a ~600-byte partial at "
    "/companies/<id> carrying the name, a one-line sector, the website, the OUTCOME "
    "('Merged with Creative BioMolecules in 2000', 'Acquired by Cisco') and the Greylock "
    "PARTNER on the deal. The Internet Archive enumerated that namespace as numeric ids "
    "only, so the pages were unreadable as a company list; Common Crawl's index, read "
    "directly off data.commoncrawl.org by scratch/cc-direct.py while index.commoncrawl.org "
    "was down, has 270 of them. This is the status and partner layer for the one stretch of "
    "the book that the 1999-2010 listings and the modern site both miss. Membership still "
    "comes from the wayback layer; the outcome wording is evidence for the judge, never a "
    "label.")

if len(sys.argv) > 1 and sys.argv[1] == "cards":
    do_cards()
