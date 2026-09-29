#!/usr/bin/env python3
"""PRO-167 grind, queue batch 6, chunk d (Getir country, missed in chunk a). Judge b6.

Evidence: the judge view (show.py --batch 5), the evidence pack, the Bing and Google candidate caches, Bing
lookups run with NQ_TAG=b6 (bq.py), sibling books' records, and pages fetched and read in this pass (the
literal URLs below). Every citation is read from disk by a helper or is a page fetched and read here."""
import json
import os
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PKD = json.loads((HERE / "evidence-pack.json").read_text())
BND = json.loads((HERE / "bing-news.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def PK(slug, sub, kind="press"):
    """A URL from the row's evidence-pack lines (press '|| URL', sec line tail, wiki or recall parentheses)."""
    p = PKD.get(slug, {})
    if kind == "recall":
        m = re.findall(r"\((https?://[^)\s]+)\)", p.get("recall_basis") or "")
        if not m:
            raise SystemExit(f"PK recall {slug}")
        return m[-1]
    urls = []
    for x in p.get(kind) or []:
        if sub.lower() not in x.lower():
            continue
        if kind == "press":
            m = re.search(r"\|\| URL (\S+)", x)
        elif kind == "sec":
            m = re.search(r"\| (https?://\S+)\s*$", x)
        else:
            m = re.search(r"\((https?://[^)\s]+)\)", x)
        if m:
            urls.append(m.group(1))
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {sub!r}, {kind}) -> {urls}")
    return urls[0]


def BN(key, sub):
    """A publisher URL from the Bing candidate cache (bing-news.json[key]) whose title contains sub."""
    urls = list(dict.fromkeys(i["url"] for i in (BND.get(key) or {}).get("items", [])
                              if sub.lower() in i["title"].lower()))
    if len(urls) != 1:
        raise SystemExit(f"BN({key!r}, {sub!r}) -> {urls}")
    return urls[0]


def SIB(slug, inv):
    """(usd, asof, citation) of a sibling book's mark for the same company, from the evidence pack."""
    for x in PKD.get(slug, {}).get("sib", []):
        if x["investor"] == inv and x.get("val_cite"):
            return int(float(x["usd"])), x["asof"], x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {inv!r}) missing")


L = [cls("getir", country="TR", country_src="web_verified",
         country_cite=PK("getir", "Anadolu Ajansi | Turkish startup Getir becomes"),
         note="Country: Turkey, the Wikidata claim confirmed from the company's own coverage (Anadolu Agency, "
              "2022-03-17, 'Turkish startup Getir'); head office Istanbul.")]

if __name__ == "__main__":
    jl.write("batch-006d", L, record=os.environ.get("DRY") != "1")
