"""Citation helpers for the PRO-167 verify-gap fixes (fixa.py .. fixd.py), 2026-09-29.

Every URL comes from a file on disk, never typed:
  BURL  a Bing News item this pass stored (news-extra-bing-fx.json, written by bq.py with NQ_TAG=fx)
  SRC   a page this pass fetched and quoted (fx-sources.json: URL, how it was found, the sentence read)
  PR    the URL printed on a press line of the row's evidence view (evidence-pack.json)
  V     a sibling book's recorded, non-vendor mark for the same company (siblings.json, rule 10)
  NEWS  (judge_lib) a Google News headline decoded to the publisher's URL
Each helper refuses a missing or ambiguous match.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

PK = json.loads((HERE / "evidence-pack.json").read_text())
SIBS = json.loads((HERE / "siblings.json").read_text())
SRCS = json.loads((HERE / "fx-sources.json").read_text())
BING = json.loads((HERE / "news-extra-bing-fx.json").read_text())
WV = {"valuation_range_source": "web_verified"}
_VENDOR = re.compile(r"sacra\.com|pitchbook|cbinsights|tracxn|crunchbase\.com/organization|dealroom|getlatka|"
                     r"forgeglobal|caplight")


def SRC(key):
    r = SRCS.get(key) or {}
    if not r.get("url"):
        raise SystemExit(f"SRC({key!r}): not in fx-sources.json")
    return r["url"]


def BURL(slug, title_sub, url_sub=""):
    m = {i["url"] for i in BING.get(slug, [])
         if title_sub.lower() in i["title"].lower() and url_sub in i["url"]}
    if len(m) != 1:
        raise SystemExit(f"BURL({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(m)}")
    return m.pop()


def PR(slug, sub):
    out = []
    for x in PK.get(slug, {}).get("press") or []:
        if sub.lower() in x.lower() and "|| URL " in x:
            out.append(x.split("|| URL ", 1)[1].split(" || ")[0].strip())
    out = list(dict.fromkeys(out))
    if len(out) != 1:
        raise SystemExit(f"PR({slug!r}, {sub!r}) matched {len(out)}")
    return out[0]


def band(usd):
    return "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"


def V(slug, inv):
    """cls() keywords pinning a sibling book's cited mark for the same company (rule 10)."""
    for x in SIBS.get(slug, []):
        if x["investor"] == inv:
            if not x.get("val_cite") or _VENDOR.search(x["val_cite"]) or not x.get("usd"):
                raise SystemExit(f"V({slug!r}, {inv!r}): no usable citation")
            usd = float(x["usd"])
            return dict(rng=band(usd), usd=usd, val_src="web_verified", val_cite=x["val_cite"],
                        asof=x["asof"], extra=dict(WV))
    raise SystemExit(f"V({slug!r}, {inv!r}): no sibling row")


def OLD(slug, round_sub):
    """A funding_rounds entry already recorded on the row (companies/classification.json), found by its round
    label or source, so a list this pass re-emits keeps the earlier entries exactly."""
    cls = json.loads((HERE.parent / "companies" / "classification.json").read_text())
    m = [r for r in (cls.get(slug) or {}).get("funding_rounds") or []
         if round_sub.lower() in f"{r.get('round')} {r.get('source')} {r.get('date')}".lower()]
    if len(m) != 1:
        raise SystemExit(f"OLD({slug!r}, {round_sub!r}) matched {len(m)}")
    return dict(m[0])


def MARK(url, usd, asof):
    """cls() keywords for a mark this pass read itself."""
    return dict(rng=band(usd), usd=usd, val_src="web_verified", val_cite=url, asof=asof, extra=dict(WV))
