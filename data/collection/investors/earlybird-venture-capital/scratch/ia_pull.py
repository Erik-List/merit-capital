#!/usr/bin/env python3
"""Pull the Internet Archive captures Common Crawl does not hold (2001-2007 and
the per-company pages), through the shared, status-aware fetcher only.

Every request goes through scripts/ia_fetch.py (one machine-wide bucket, 429
and 503 honoured, a refused connection sets the machine-wide cooldown and this
script then stops: a failed fetch is recorded FAILED in the manifest, never as
an empty page). Targets come from the one CDX listing already on disk
(scratch/cdx/earlybird-com-urlkeys.json), so no further index queries are made.

Raw bodies: sources/wayback/raw/ia/<ts>-<stem>.html
Manifest:   sources/wayback/raw/ia/manifest.json  {key: {status, original, timestamp}}
Usage: python3 scratch/ia_pull.py [--dry]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]
sys.path.insert(0, str(REPO / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402

RAW = ROOT / "sources/wayback/raw/ia"
MAN = RAW / "manifest.json"
BASE = "http://www.earlybird.com"

YEARLY = {
    "/en/portfolio/a_z/": range(2002, 2008),          # 2008-2010 are in Common Crawl
    "/en/portfolio/recent/": range(2002, 2011),
    "/en/portfolio/healthcare/": range(2002, 2008),
    "/en/portfolio/communication/": range(2002, 2004),
    "/en/exits/ipos/": range(2008, 2011),
    "/en/exits/trade_sales/": range(2009, 2011),
}


def stem_of(path: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", path.strip("/"))[:110] or "root"


def targets() -> list[tuple[str, str | None, str]]:
    """(original url, exact timestamp or None for a yearly probe, year-or-'')."""
    rows = json.loads((ROOT / "scratch/cdx/earlybird-com-urlkeys.json").read_text())[1:]
    out: list[tuple[str, str | None, str]] = []
    for original, ts, ets, _gc, _sc, _mt in rows:
        path = re.sub(r"^https?://(www\.)?earlybird\.com(:80)?", "", original)
        p = path.split("?")[0]
        if re.search(r"\.(gif|jpg|png|css|js)$", p) or "document." in p or "%22" in p:
            continue
        exact = (
            re.fullmatch(r"/en/portfolio/(a_z|it_tele|healthcare|about)/index\.html", p)
            or re.fullmatch(r"/en/portfolio/index\.html", p)
            or re.fullmatch(r"/en/portfolio/investment/[a-z0-9_]+\.html", p)
            or re.fullmatch(r"/en/portfolio/recent/[a-z0-9_]+/", p)
            or re.fullmatch(r"/en/portfolio/case_studies/", p)
            or re.fullmatch(r"/en/companies/(tech|health-tech)/(portfolio|exited)/[^/]+\.html", p)
            or re.fullmatch(r"/en/press/release/\d+/", p)
            or re.fullmatch(r"/en/companies/(tech|health-tech)(/portfolio)?\.html", p)
        )
        if exact:
            out.append((original, ts, ""))
    for path, years in YEARLY.items():
        for y in years:
            out.append((BASE + path, None, str(y)))
    # Framer pages the live site no longer carries and Common Crawl did not name
    ev = ROOT / "sources/wayback/archive-evidence.json"
    if ev.exists():
        for slug in json.loads(ev.read_text()).get("index_only_slugs", []):
            for original, ts, _e, _g, _s, _m in rows:
                if original.rstrip("/").endswith("/companies/" + slug):
                    out.append((original, ts, ""))
                    break
    return out


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    todo = targets()
    print(f"{len(todo)} targets", flush=True)
    if "--dry" in sys.argv:
        for t in todo[:400]:
            print(" ", t)
        return
    done = fail = 0
    for original, ts, year in todo:
        path = re.sub(r"^https?://(www\.)?earlybird\.com(:80)?", "", original)
        if ts is None:
            pk = f"probe:{year}:{path}"
            if man.get(pk, {}).get("status") in ("ok", "none"):
                ts = man[pk].get("timestamp")
                if not ts:
                    continue
            else:
                eff, code = ia_fetch.probe(original, f"{year}0601")
                if code.startswith("rc"):
                    man[pk] = {"status": "FAILED", "code": code}
                    write_atomic(MAN, json.dumps(man, indent=1) + "\n")
                    print(f"  probe {year} {path}: {code} -- stopping (archive not answering)", flush=True)
                    break
                m = re.search(r"/web/(\d{14})", eff)
                if not m or m.group(1)[:4] != year:
                    man[pk] = {"status": "none", "nearest": m.group(1) if m else None}
                    continue          # no capture in that year: an absence, recorded as such
                ts = m.group(1)
                man[pk] = {"status": "ok", "timestamp": ts}
        key = f"{ts}-{stem_of(path)}.html"
        if man.get(key, {}).get("status") == "ok" and (RAW / key).exists():
            continue
        body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{original}")
        if code.startswith("rc"):
            man[key] = {"status": "FAILED", "code": code, "original": original, "timestamp": ts}
            write_atomic(MAN, json.dumps(man, indent=1) + "\n")
            print(f"  {key}: {code} -- stopping (archive not answering)", flush=True)
            fail += 1
            break
        if code != "200" or len(body) < 200:
            man[key] = {"status": "FAILED", "code": code, "original": original, "timestamp": ts}
            fail += 1
        else:
            (RAW / key).write_bytes(body)
            man[key] = {"status": "ok", "original": original, "timestamp": ts, "bytes": len(body)}
            done += 1
        if (done + fail) % 10 == 0:
            write_atomic(MAN, json.dumps(man, indent=1) + "\n")
            print(f"  {done} fetched, {fail} failed", flush=True)
    write_atomic(MAN, json.dumps(man, indent=1) + "\n")
    print(f"done: {done} fetched, {fail} failed, manifest {len(man)}", flush=True)


if __name__ == "__main__":
    main()
