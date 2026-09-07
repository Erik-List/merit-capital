#!/usr/bin/env python3
"""Greylock's archived listings carry more than names.

Three of the six archive eras render, per company, the firm's own YEAR FUNDED
and STATUS, and the 2005-2010 era adds the Greylock partner on the deal and a
region.  `wayback-pull.py`'s listing_regex keeps only slug and name, so those
columns would be thrown away by the layer that is best placed to supply them:
`status` for a book whose dead rows never reached English-language press, and
`first_seen` for the pre-window slice where no Form D exists.

This reads the raw captures `wayback-pull.py` already stored and writes one
`file_list` source, sources/site/archive-cards.json, keyed by company name with
the era's own fields and the capture it came from.  It is additive: the
wayback layer still owns membership, this owns the columns.

Usage: python3 build-archive-cards.py            (from anywhere)
"""
import json, re, sys, pathlib
from html import unescape

ROOT = pathlib.Path(__file__).resolve().parents[5]
RAW = ROOT / "data/collection/investors/greylock/sources/wayback/raw"
OUT = ROOT / "data/collection/investors/greylock/sources/site/archive-cards.json"


def clean(s):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def era1(html, ts):
    """1999-2001 frameset: <TR> of logo | year | name | product | status."""
    out = []
    for tr in re.findall(r"(?is)<TR[^>]*>(.*?)</TR>", html):
        cells = [clean(c) for c in re.findall(r"(?is)<TD[^>]*>(.*?)</TD>", tr)]
        cells = [c for c in cells if c != ""]
        if len(cells) < 3:
            continue
        if not re.fullmatch(r"(?:19|20)\d{2}", cells[0]):
            continue
        year, name = cells[0], cells[1]
        if not name or len(name) > 70:
            continue
        out.append({"name": name, "invest_year": int(year),
                    "desc": cells[2] if len(cells) > 2 else None,
                    "status_line": cells[3] if len(cells) > 3 else None,
                    "era": "1999-2001 frameset", "snapshot_ts": ts})
    return out


def era2(html, ts):
    """2001-2003 ASP: company anchor, then focus / status / year cells."""
    out = []
    # The rows alternate two bgColors and some carry none at all, so the block
    # is any <TR> holding a company anchor -- keying on one colour read 21 of
    # the capture's 44 rows.
    for m in re.finditer(r"(?is)<TR[^>]*>(.*?)</TR>", html):
        blk = m.group(1)
        if 'class="companylink"' not in blk:
            continue
        a = re.search(r'(?is)<A class="companylink"[^>]*>(?:<IMG[^>]*>)?(?:<BR>)?\s*'
                      r'([^<>]{1,60}?)\s*</A>', blk)
        if not a:
            continue
        cells = [clean(c) for c in re.findall(r"(?is)<TD[^>]*>(.*?)</TD>", blk)]
        cells = [c for c in cells if c and not c.startswith(a.group(1))]
        row = {"name": clean(a.group(1)), "era": "2001-2003 asp", "snapshot_ts": ts}
        if cells:
            row["desc"] = cells[0]
        for c in cells:
            if c.lower() in ("private", "public", "acquired", "merged", "acquired/merged"):
                row["status_line"] = c
            elif re.fullmatch(r"(?:19|20)\d{2}", c):
                row["invest_year"] = int(c)
        out.append(row)
    return out


def era3(html, ts):
    """2005-2010 ColdFusion: <div class="data"> cards."""
    out = []
    for m in re.finditer(r'(?is)<div class="data">(.*?)</div>\s*</td>', html):
        blk = m.group(1)
        n = re.search(r'(?is)<div class="dataHead">\s*(.*?)\s*</div>', blk)
        if not n:
            continue
        text = clean(blk)
        row = {"name": clean(n.group(1)), "era": "2005-2010 coldfusion",
               "snapshot_ts": ts}
        w = re.search(r'href="(https?://[^"]+)"', blk)
        if w:
            row["website"] = w.group(1)
        for key, pat in (("status_line", r"Status:\s*([A-Za-z/ ]{3,40}?)\s*(?:Year Funded|Region|Greylock|$)"),
                         ("invest_year", r"Year Funded:\s*((?:19|20)\d{2})"),
                         ("region", r"Region:\s*([A-Za-z ]{2,30}?)\s*$")):
            mm = re.search(pat, text)
            if mm:
                row[key] = int(mm.group(1)) if key == "invest_year" else mm.group(1).strip()
        row["partners"] = [clean(p) for p in
                           re.findall(r'href="\.\./team/bio\.cfm\?Id=\d+"[^>]*>([^<]{2,40})</a>', blk)]
        out.append(row)
    return out


ERAS = [("company-", era1), ("companies-ByName", era2), ("companies-OtherInvest", era2),
        ("portfolio-portfolio.cfm", era3)]


def main():
    if not RAW.exists():
        sys.exit(f"no raw captures at {RAW}")
    cards, files = {}, []
    for f in sorted(RAW.glob("*.html")):
        for prefix, fn in ERAS:
            if prefix not in f.name:
                continue
            ts = re.match(r"(\d{4})-", f.name)
            html = f.read_text(encoding="utf-8", errors="replace")
            rows = fn(html, f.name)
            files.append(f"{f.name}: {len(rows)}")
            for r in rows:
                key = re.sub(r"[^a-z0-9]+", "", r["name"].lower())
                if not key:
                    continue
                cur = cards.setdefault(key, {"name": r["name"], "sources": []})
                # Newer captures win a field; older ones fill what is still empty,
                # so the 1999 year survives while the 2005 status supersedes it.
                for k, v in r.items():
                    if k in ("name", "era", "snapshot_ts") or v in (None, "", []):
                        continue
                    if k not in cur or f.name > (cur.get("_from", {}).get(k, "")):
                        cur[k] = v
                        cur.setdefault("_from", {})[k] = f.name
                cur["sources"].append(f"{r['era']} ({r['snapshot_ts']})")
            break
    for c in cards.values():
        c.pop("_from", None)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "_readme": ("Greylock's own listing fields, read out of the archived captures in "
                    "sources/wayback/raw by scratch/build-archive-cards.py. Three eras publish "
                    "more than a name: the 1999-2001 frameset (year funded, product, status "
                    "line), the 2001-2003 ASP site (focus, status, year) and the 2005-2010 "
                    "ColdFusion site (website, status, year funded, the Greylock partner on the "
                    "deal, region). wayback-pull's listing_regex keeps slug and name only, so "
                    "these columns would otherwise be discarded by the layer best placed to "
                    "supply them -- status for a book whose dead rows never reached the press, "
                    "and first_seen for the pre-window slice that has no Form D. Membership "
                    "still comes from the wayback layer; this is a classification input, and "
                    "the site's status wording is evidence for the judge, never a label."),
        "_files": files,
        "companies": sorted(cards.values(), key=lambda c: c["name"].lower()),
    }, indent=1) + "\n")
    print(f"wrote {OUT} — {len(cards)} companies from {len(files)} captures")
    for f in files:
        print("  ", f)


if __name__ == "__main__":
    main()
