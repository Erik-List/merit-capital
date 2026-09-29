"""Entry-round and later-round candidates per row, verified against the article.

For each row of a queue batch (or --slugs): the surfaces items naming the company
that carry a round word, split into ENTRY candidates (dated within the window of
HV's own entry claim: the Storyblok entry_date, else the export's HV Entry year)
and LATER candidates (dated after it). Each candidate is decoded to the
publisher URL and the article fetched once; the check records whether the body
names HV (HV Capital / Holtzbrinck Ventures / HV Holtzbrinck) and which round
words it carries. Results cache in scratch/cand-cache.json; the view prints per
row. Nothing here decides a row: it is the judge's evidence.

Usage: candidates.py <batch-no> | --slugs a,b   [--no-fetch]
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import judge_lib as J  # noqa: E402

CACHE = H / "cand-cache.json"
C = json.loads(CACHE.read_text()) if CACHE.exists() else {}
FIRM = re.compile(r"\bHV[ -]Capital\b|Holtzbrinck Ventures|HV Holtzbrinck|\bHV Ventures\b", re.I)
ROUND = re.compile(r"\b(pre-?seed|seed|series [a-h]\b|serie [a-h]\b|series-[a-h]|finanzierungsrunde|growth round|"
                   r"extension|bridge|expansion round)", re.I)
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/128.0.0.0 Safari/537.36")


def entry_claim(slug, name):
    e = J.ev(slug)
    ds = [d for d in e.get("invest_dates") or [] if re.match(r"\d{4}-\d{2}", d)]
    if ds:
        return min(ds)[:7]
    r = J.live(slug, name)
    if r and r["HV Entry"].isdigit():
        return r["HV Entry"] + "-06"
    ys = e.get("invest_years") or []
    return (min(ys) + "-06") if ys else None


def months(a, b):
    ya, ma = int(a[:4]), int(a[5:7] or 6)
    yb, mb = int(b[:4]), int(b[5:7] or 6)
    return (yb - ya) * 12 + (mb - ma)


def fetch(url):
    if url in C.get("_pages", {}):
        return C["_pages"][url]
    try:
        out = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url], capture_output=True).stdout
        s = out.decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        s = ""
    s = re.sub(r"(?s)<(script|style|nav|footer|header)[^>]*>.*?</\1>", " ", s)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))
    firm = [t[max(0, m.start() - 160):m.end() + 160] for m in FIRM.finditer(t)][:3]
    rec = {"len": len(t), "firm": firm, "rounds": sorted({m.group(1).lower() for m in ROUND.finditer(t)})[:8]}
    if len(t) < 1500 or not rec["rounds"]:
        rec["unread"] = True
    C.setdefault("_pages", {})[url] = rec
    return rec


def run(slugs, do_fetch=True):
    for slug, name in slugs:
        claim = entry_claim(slug, name)
        rows = []
        for svc, i in J.items(slug):
            firmhit = svc == "googlenews_firm" and i.get("names")
            if not i.get("names") or not (i.get("rounds") or FIRM.search(i.get("title") or "") or firmhit):
                continue
            d = (i.get("date") or "")[:7]
            if not d:
                continue
            kind = None
            if claim and abs(months(claim, d)) <= 9 and (i.get("rounds") or firmhit or FIRM.search(i.get("title") or "")):
                kind = "ENTRY"
            elif claim and months(claim, d) > 9:
                t0 = (i.get("title") or "").lower()
                nm = (name or slug).lower().split(" (")[0]
                if not (t0.startswith(nm) or f" {nm} " in t0[:60] or FIRM.search(t0)):
                    continue
                kind = "LATER"
            elif FIRM.search(i.get("title") or "") or firmhit:
                kind = "FIRM"
            if not kind:
                continue
            rows.append((kind, d, svc, i))
        rows.sort(key=lambda x: x[1])
        print(f"## {slug} | {name} | HV entry claim {claim}")
        seen = set()
        for kind, d, svc, i in rows:
            key = (i.get("gid") or i.get("url"))
            if key in seen:
                continue
            seen.add(key)
            url = i.get("url")
            if not url and do_fetch and kind in ("ENTRY", "FIRM") or (not url and do_fetch and kind == "LATER" and
                                                                      re.search(r"series [a-h]", (i.get("title") or "").lower())):
                try:
                    url = J.gn(slug, i["gid"][-10:])
                except Exception as e:  # noqa: BLE001
                    url = None
            chk = fetch(url) if (url and do_fetch and kind in ("ENTRY", "FIRM")) else None
            tag = ""
            if chk:
                tag = (" HV=? (page unreadable)" if chk.get("unread") and not chk["firm"]
                       else f" HV={'Y' if chk['firm'] else 'n'} rounds={chk['rounds']}")
            print(f"   {kind:5} {d} [{svc[:6]}] {(i.get('title') or '')[:120]} {{{','.join(i.get('rounds') or [])}}} "
                  f"{url or 'gid:' + (i.get('gid') or '')[-10:]}{tag}")
            if chk and chk["firm"]:
                print(f"         > {chk['firm'][0][:300]}")
        CACHE.write_text(json.dumps(C, ensure_ascii=False))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--slugs":
        base = {r["slug"]: r["name"] for r in json.loads((J.INV / "companies/base.json").read_text())}
        sl = [(s, base.get(s, s)) for s in a[1].split(",")]
    else:
        b = json.loads((J.Q / f"batch-{int(a[0]):03d}.json").read_text())
        sl = [(it["slug"], it["name"]) for it in b]
    run(sl, "--no-fetch" not in a)
