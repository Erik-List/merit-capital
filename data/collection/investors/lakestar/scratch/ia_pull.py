#!/usr/bin/env python3
"""Internet Archive pull for lakestar.com (PRO-108).

Targets, read off scratch/cdx/*.tsv (CDX enumerations made through ia_fetch):
  - listing pages: the homepage, /portfolio, /team, /about and /news, first and
    last distinct capture per year;
  - every per-page capture once: /company/<slug> (2022-2026 site),
    /portfolio/<slug> and /about-us/* (2013 site), /team/<slug>, /news/<slug>,
    /thesis/<slug>, /media/<slug>.

Bodies -> sources/wayback/raw/ia/<ts>-<path>.html (raw replay, the id_ flavour);
manifest -> sources/wayback/ia-manifest.json {key: {status, url, timestamp,
capture_url, bytes}}. A fetch that fails is recorded FAILED, never as an empty
page, and is retried on the next run. Idempotent.

Usage: python3 ia_pull.py [--listings-only] [--only <path-prefix>]
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402

RAW = INV / "sources" / "wayback" / "raw" / "ia"
MAN = INV / "sources" / "wayback" / "ia-manifest.json"
CDX = HERE / "cdx"

PER_PAGE = ("/company/", "/portfolio/", "/team/", "/news/", "/thesis/", "/media/", "/about-us")
LISTINGS = {
    "exact-lakestar_com_.tsv": lambda y: y == "2013" or "2017" <= y,
    "exact-lakestar_com_portfolio.tsv": lambda y: True,
    "exact-lakestar_com_team.tsv": lambda y: True,
    "exact-lakestar_com_about.tsv": lambda y: True,
    "exact-lakestar_com_news.tsv": lambda y: True,
}


def path_of(orig: str) -> str:
    return re.sub(r"^https?://(www\.)?lakestar\.com(:\d+)?", "", orig)


def key_of(ts: str, orig: str) -> str:
    p = path_of(orig).split("?")[0].strip("/") or "home"
    q = ""
    m = re.search(r"page_num=(\d+)", orig)
    if m:
        q = f"-page{m.group(1)}"
    return f"{ts}-{re.sub(r'[^A-Za-z0-9._%-]+', '_', p)}{q}"


def targets(listings_only: bool, only: str | None) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for fn, keep in LISTINGS.items():
        by = defaultdict(list)
        for line in (CDX / fn).read_text().splitlines():
            r = line.split("\t")
            if len(r) < 6 or "html" not in r[5]:
                continue
            if keep(r[0][:4]):
                by[r[0][:4]].append((r[0], r[1]))
        for y in sorted(by):
            caps = sorted(by[y])
            out.append(caps[0])
            if caps[-1] != caps[0]:
                out.append(caps[-1])
            if len(caps) > 6:                      # a mid-year capture for busy years
                out.append(caps[len(caps) // 2])
    if not listings_only:
        seen = set()
        for line in (CDX / "all-urlkeys.tsv").read_text().splitlines():
            r = line.split("\t")
            if len(r) < 6 or "html" not in r[5]:
                continue
            p = path_of(r[1])
            if "_rsc=" in p or "ref=" in p:
                continue
            bare = p.split("?")[0].rstrip("/").lower()
            if "page_num" in p:
                bare = p
            if not (p.startswith(PER_PAGE)) or bare in seen:
                continue
            seen.add(bare)
            out.append((r[0], r[1]))
    if only:
        out = [t for t in out if path_of(t[1]).startswith(only)]
    if "--max-year" in sys.argv:
        my = sys.argv[sys.argv.index("--max-year") + 1]
        out = [t for t in out if t[0][:4] <= my]
    if "--have-cc" in sys.argv:              # skip pages Common Crawl already holds
        cm = INV / "sources" / "wayback" / "cc-manifest.json"
        have = set()
        if cm.exists():
            for v in json.loads(cm.read_text()).values():
                if v.get("status") == "ok":
                    have.add(path_of(v["url"]).split("?")[0].rstrip("/").lower())
        out = [t for t in out if path_of(t[1]).split("?")[0].rstrip("/").lower() not in have]
    return out


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    tg = targets("--listings-only" in sys.argv, only)
    print(f"{len(tg)} captures targeted", flush=True)
    done = failed = 0
    for i, (ts, orig) in enumerate(tg):
        key = key_of(ts, orig)
        if man.get(key, {}).get("status") == "ok" and (RAW / f"{key}.html").exists():
            continue
        if ia_fetch.blocked() > 0:
            print("IA cooldown active; stopping, re-run later", flush=True)
            break
        url = f"https://web.archive.org/web/{ts}id_/{orig}"
        body, st = ia_fetch.get(url)
        if st.startswith("2") and body:
            (RAW / f"{key}.html").write_bytes(body)
            man[key] = {"status": "ok", "url": orig, "timestamp": ts,
                        "capture_url": f"https://web.archive.org/web/{ts}/{orig}", "bytes": len(body)}
            done += 1
        else:
            man[key] = {"status": f"FAILED {st}", "url": orig, "timestamp": ts,
                        "capture_url": f"https://web.archive.org/web/{ts}/{orig}"}
            failed += 1
        if (done + failed) % 20 == 0:
            write_atomic(MAN, json.dumps(man, indent=1, sort_keys=True) + "\n")
            print(f"  {i + 1}/{len(tg)} fetched {done} failed {failed}", flush=True)
    write_atomic(MAN, json.dumps(man, indent=1, sort_keys=True) + "\n")
    ok = sum(1 for v in man.values() if v["status"] == "ok")
    bad = sum(1 for v in man.values() if v["status"] != "ok")
    print(f"manifest: {ok} ok, {bad} failed (this run: {done} fetched, {failed} failed)")
    sys.exit(3 if bad else 0)


if __name__ == "__main__":
    main()
