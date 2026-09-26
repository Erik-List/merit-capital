#!/usr/bin/env python3
"""Atomico's team API (/api/teammembers), read from the archive.

The Next.js site serves its team through /api/teammembers (all, and filtered
by ?role=venture|growth|advisers and ?location=). The Internet Archive holds
captures from 2025; each is the CMS's own list of people with their role
group, title and links. The newest capture of each variant is kept raw under
scratch/team-raw/ and the union is written as a file_list source.

Writes sources/site/team-api.json.
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import ia_fetch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402

P = Paths("atomico")
RAW = HERE / "team-raw"


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    body, code = ia_fetch.get("https://web.archive.org/cdx/search/cdx?url=atomico.com/api/teammembers"
                              "&matchType=prefix&output=json&fl=timestamp,original,statuscode"
                              "&filter=statuscode:200&limit=500")
    if code != "200":
        raise SystemExit(f"CDX: {code}")
    caps = json.loads(body or b"[]")[1:]
    newest: dict[str, tuple[str, str]] = {}
    for ts, orig, _ in caps:
        if orig not in newest or ts > newest[orig][0]:
            newest[orig] = (ts, orig)
    print(f"{len(caps)} captures, {len(newest)} variants")
    people: dict[str, dict] = {}
    for orig, (ts, _) in sorted(newest.items()):
        variant = orig.split("?", 1)[1] if "?" in orig else "all"
        f = RAW / f"{re.sub(r'[^a-z0-9]+', '-', variant.lower())}-{ts}.json"
        if f.exists():
            raw = f.read_text()
        else:
            b, c = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
            if c != "200":
                print("  miss", orig, c)
                continue
            raw = b.decode("utf-8", errors="replace")
            write_atomic(f, raw)
        try:
            data = json.loads(raw)
        except ValueError:
            print("  not json", orig)
            continue
        rows = data.get("data") if isinstance(data, dict) else data
        if isinstance(data, dict) and not rows:
            rows = next((v for v in data.values() if isinstance(v, list)), [])
        print(f"  {variant}: {len(rows or [])} rows ({ts})")
        for r in rows or []:
            name = (r.get("name") or r.get("title") or "").strip()
            if not name:
                continue
            e = people.setdefault(name, {"name": name, "variants": [], "capture_ts": ts})
            e["variants"].append(variant)
            for k, v in r.items():
                if k not in e and not isinstance(v, (dict, list)):
                    e[k] = v
                elif k not in e and isinstance(v, dict) and v.get("url"):
                    e[k] = v.get("url")
    write_atomic(P.site / "team-api.json", json.dumps({
        "_readme": ("atomico.com /api/teammembers (the Next.js site's team endpoint), newest archived "
                    "capture of each variant (all, ?role=venture|growth|advisers, ?location=...), "
                    "read by scratch/team-pull.py " + time.strftime("%Y-%m-%d") + ". `variants` records "
                    "which role filters returned the person: the role group is the site's own."),
        "rows": sorted(people.values(), key=lambda r: r["name"])}, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(people)} people")


if __name__ == "__main__":
    main()
