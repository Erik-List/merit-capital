#!/usr/bin/env python3
"""Enumerate an investor's historical site pages from the Common Crawl index.

A second, independent capture archive for the wayback layer's two jobs —
survivorship correction and roster tenure — used when the Internet Archive
is unreachable (measured twice now: a16z ~100min, Accel a full run) or as
corroboration beside it. CC's per-crawl coverage of a single site is
shallow (tens to hundreds of captures), but ~125 crawls back to 2008
accumulate; IA's own pull remains the deeper source and simply overwrites
the same per-year files when it lands (wayback-pull.py writes parsed/
<year>.json wholesale, so recovery converges over this layer).

Reads config `wayback.cdx_domain` + `commoncrawl.company_paths` /
`commoncrawl.people_paths`; filters through `wayback.non_company_slugs` and
`roster.not_a_person`.

Writes:
  sources/wayback/cc-index-raw.json      resume cache of the CC queries
  sources/wayback/parsed/<year>.json     {slug, path, snapshot_ts} company
                                         rows (same shape wayback-pull
                                         writes; snapshot_ts is the CC
                                         capture timestamp)
  sources/wayback/cc-people.json         {slug: [years]} people evidence,
                                         consumed by partner-roster.py

Usage: python3 scripts/commoncrawl-pull.py <investor-slug>
"""
import argparse
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
INDEX = "https://index.commoncrawl.org"


def curl(url: str, tries: int = 5, backoff: float = 4.0) -> str:
    for attempt in range(tries):
        r = subprocess.run(["curl", "-s", "--max-time", "50",
                            "-H", f"User-Agent: {UA}", url], capture_output=True)
        txt = r.stdout.decode(errors="replace")
        if txt:
            return txt
        time.sleep(backoff * (attempt + 1))
    return ""


def fetch_all(domain: str, cache: Path) -> dict:
    """{crawl-id: [(timestamp, path), ...]} across every CC index, resumable.

    The index server throttles hard; serial pacing with backoff is the only
    reliable client. A crawl with no captures stores [] so resume skips it.
    """
    out = json.loads(cache.read_text()) if cache.exists() else {}
    ids = None
    for a in range(6):
        try:
            ids = [i["id"] for i in json.loads(curl(f"{INDEX}/collinfo.json"))]
            break
        except (json.JSONDecodeError, TypeError):
            time.sleep(5 * (a + 1))
    if ids is None:
        sys.exit("Common Crawl collinfo unreachable")
    todo = [c for c in ids if c not in out]
    print(f"CC indexes: {len(ids)} total, {len(todo)} to fetch")
    # One Common Crawl puller at a time across every session on this machine:
    # the index server answers parallel clients with silent empty result sets.
    with shared_throttle.exclusive("cc"):
        for n, cid in enumerate(todo):
            url = (f"{INDEX}/{cid}-index?url={domain}&matchType=domain"
                   f"&output=json&limit=3000&filter=status:200")
            got = None
            for attempt in range(5):
                txt = curl(url, tries=1)
                if txt.startswith('{"message": "No Captures'):
                    got = []
                    break
                rows = []
                for line in txt.splitlines():
                    try:
                        d = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if d.get("status") == "200":
                        p = re.sub(r"^https?://(www\.)?" + re.escape(domain), "",
                                   d.get("url", "")).split("?")[0]
                        rows.append((d.get("timestamp", ""), p, d.get("digest", "")))
                if rows:
                    got = rows
                    break
                time.sleep(4 * (attempt + 1))
            if got is not None:
                out[cid] = got
                write_atomic(cache, json.dumps(out))
            time.sleep(1.5)
            if n % 15 == 0:
                print(f"  {n}/{len(todo)} {cid}: "
                      f"{len(got) if got is not None else 'FAIL'}", flush=True)
    missing = [c for c in ids if c not in out]
    if missing:
        print(f"  WARNING: {len(missing)} indexes unfetched (rerun resumes): "
              f"{missing[:6]}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    args = ap.parse_args()
    p = Paths(args.investor)
    cfg = p.config()
    cc = cfg.get("commoncrawl") or {}
    company_paths = set(cc.get("company_paths") or [])
    people_paths = set(cc.get("people_paths") or [])
    if not company_paths and not people_paths:
        sys.exit("no commoncrawl.company_paths/people_paths in config")
    non_company = set(cfg["wayback"]["non_company_slugs"])
    not_person = set(cfg["roster"]["not_a_person"])

    p.wayback.mkdir(parents=True, exist_ok=True)
    raw = fetch_all(cfg["wayback"]["cdx_domain"], p.wayback / "cc-index-raw.json")

    slug_re = re.compile(r"^/([a-z0-9-]+)/([a-z0-9][a-z0-9_-]*[a-z0-9])/?$")
    years: dict[int, dict] = defaultdict(dict)
    people: dict[str, set] = defaultdict(set)
    shell_dropped = 0
    for cid, rows in raw.items():
        # Catch-all shell filter: a route that serves the SAME body for any
        # slug answers 200 with one digest for every path (accel.com 2018:
        # 368 "/companies/<anything>" captures, one digest — crawler-followed
        # junk slugs like adobe/amazon, not listings). Within one crawl and
        # namespace, captures sharing the dominant digest are dropped when
        # that digest covers most of the namespace and more than one page.
        from collections import Counter
        ns_digests: dict[str, Counter] = defaultdict(Counter)
        for ts, path, dig in ((r + [""])[:3] if isinstance(r, list) else r
                              for r in rows):
            m = slug_re.match(path)
            if m and dig:
                ns_digests[m.group(1)][dig] += 1
        shell: dict[str, str] = {}
        for ns, c in ns_digests.items():
            dig, n = c.most_common(1)[0]
            if n >= 3 and n / sum(c.values()) > 0.5:
                shell[ns] = dig
        for ts, path, dig in ((r + [""])[:3] if isinstance(r, list) else r
                              for r in rows):
            m = slug_re.match(path)
            if not m or not ts[:4].isdigit():
                continue
            ns, slug = m.group(1), m.group(2)
            if dig and shell.get(ns) == dig:
                shell_dropped += 1
                continue
            y = int(ts[:4])
            if ns in company_paths and slug not in non_company:
                prev = years[y].get(slug)
                if prev is None or ts < prev["snapshot_ts"]:
                    years[y][slug] = {"slug": slug, "path": f"/{ns}/{slug}",
                                      "snapshot_ts": ts}
            elif ns in people_paths and slug not in not_person and "-" in slug:
                people[slug].add(str(y))
    if shell_dropped:
        print(f"catch-all shell captures dropped: {shell_dropped}")

    parsed = p.wayback / "parsed"
    parsed.mkdir(parents=True, exist_ok=True)
    for y, comps in sorted(years.items()):
        dest = parsed / f"{y}.json"
        merged = {r["slug"]: r for r in
                  (json.loads(dest.read_text()) if dest.exists() else [])}
        for slug, r in comps.items():
            merged.setdefault(slug, r)
        write_atomic(dest, json.dumps(
            sorted(merged.values(), key=lambda r: r["slug"]), indent=1) + "\n")
        print(f"  {y}: {len(comps)} company pages ({len(merged)} merged)")
    write_atomic(p.wayback / "cc-people.json", json.dumps(
        {s: sorted(ys) for s, ys in sorted(people.items())}, indent=1) + "\n")
    total = {r["slug"] for c in years.values() for r in c.values()}
    print(f"\ncompany slugs across years: {len(total)}   people slugs: {len(people)}")


if __name__ == "__main__":
    main()
