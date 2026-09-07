#!/usr/bin/env python3
"""Read the BODY of the archived per-company pages, not only the CDX index.

`cdx_company_pages` enumerates /portfolio/<slug> from the index and stops there,
so 175 of Khosla's 429 archived slugs land unnamed -- and they are the modern,
high-value half of the book (openai, gitlab, rubrik, commonwealth-fusion-systems,
hermeus, varda-space-industries, sword-health, ultima-genomics, waabi, synchron).
COLLECTION.md §5's Common Crawl rule already says the body is the evidence; the
same is true of the IA replay, and on this site the body carries four fields the
index cannot:

  name          <title> "Anchorage | Khosla Ventures"; the FIRST <h1> is the
                company and wraps its own outbound URL. (The SECOND <h1> is the
                footer's "About Khosla Ventures" -- an <h1>-first parser
                publishes that as the company name on every row. Measured here.)
  abstract      the firm's own description
  categories    the firm's own sector tags, /portfolio/<sector> links
  founded /     <table class=dates> -- the firm's own founding year and its own
  invested      INVESTMENT year. Read `invested` as a CLOSE year, never an
                announcement date (COLLECTION.md §6, the Menlo rule), and score
                it on the golden set before it is allowed to label anything.

A slug never names a row (COLLECTION.md §5.1a), so this exists precisely so the
one-word slugs (block, rocket, go, fresh, even, plum, swift, castle) reach the
judge as the firm's own rendering rather than as a guess.

Writes: sources/wayback/company-pages.json
Usage:  python3 scratch/company-pages.py [slugs.json]
"""
import json, re, subprocess, sys, time
from html import unescape
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "sources" / "wayback" / "company-pages.json"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
# Capped at four probes: the <table class=dates> block belongs to the 2017-2023
# theme, so a slug that has no invested year in 2019 or 2022 does not have one,
# and burning ten replay fetches per slug on that costs the whole IA budget.
YEARS = (2019, 2022, 2017, 2023)


def get(u):
    for a in range(3):
        r = subprocess.run(["curl", "-sfL", "--compressed", "--max-time", "60",
                            "-H", f"User-Agent: {UA}", u], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode("utf-8", "replace")
        time.sleep(1.2 * (a + 1))
    return ""


def txt(s):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).replace("\xa0", " ").strip() or None


def parse(h):
    t = re.sub(r"(?s)<(script|style).*?</\1>", "", h)
    name = url = None
    m = re.search(r"<title>([^<]*)</title>", t)
    if m:
        cand = unescape(m.group(1)).split("|")[0].strip()
        if cand and cand.lower() not in ("khosla ventures", "portfolios", "portfolio",
                                         "all companies", "page not found", "nothing found"):
            name = cand
    for m in re.finditer(r"<h1[^>]*>(.*?)</h1>", t, re.S):
        inner = m.group(1)
        label = txt(inner)
        if not label or label.lower().startswith("about khosla"):
            continue
        a = re.search(r"""href=["']?(https?://[^"'\s>]+)""", inner)
        if a and "khoslaventures.com" not in a.group(1) and "web.archive.org" not in a.group(1):
            url = a.group(1)
        name = name or label
        break
    abstract = None
    m = re.search(r"""<div class=["']?abstract["']?[^>]*>(.*?)(?=<div class=["']?categories|<table|</div>)""", t, re.S)
    if m:
        abstract = txt(m.group(1))
    cats = [txt(c) for c in re.findall(r"""<span class=["']?category-name["']?[^>]*>(.*?)</span>""", t, re.S)]
    founded = invested = None
    m = re.search(r"""<table class=["']?dates["']?.*?<tbody>(.*?)</tbody>""", t, re.S)
    if m:
        tds = [txt(x) for x in re.findall(r"<td[^>]*>(.*?)</td>", m.group(1), re.S)]
        ys = [re.search(r"(19|20)\d{2}", d).group(0) if d and re.search(r"(19|20)\d{2}", d) else None
              for d in tds]
        founded = ys[0] if len(ys) > 0 else None
        invested = ys[1] if len(ys) > 1 else None
    return {"name": name, "company_url": url, "description": abstract[:600] if abstract else None,
            "categories_site": [c for c in cats if c] or None,
            "site_founded_year": founded, "site_invest_year": invested,
            "alumni": bool(re.search(r"""class=["']?alumni""", t)),
            "case_study": bool(re.search(r"""class=["']?case-study""", t))}


def main():
    slugs = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else json.load(open("/tmp/kv-unnamed.json"))
    out = json.load(open(OUT)).get("companies", {}) if OUT.exists() else {}
    for i, s in enumerate(slugs, 1):
        cur = out.get(s) or {}
        if cur.get("name") and (cur.get("site_invest_year") or cur.get("_exhausted")):
            continue
        rec = None
        for yr in YEARS:
            h = get(f"https://web.archive.org/web/{yr}id_/http://www.khoslaventures.com/portfolio/{s}")
            if not h or len(h) < 1500:
                continue
            p = parse(h)
            if p["name"]:
                p["snapshot_year"] = yr
                rec = p
                if p["site_invest_year"]:
                    break
        out[s] = rec or dict(cur, name=cur.get("name"), _exhausted=True)
        if rec and not rec.get("site_invest_year"):
            out[s]["_exhausted"] = True
        r = out[s]
        print(f"  [{i}/{len(slugs)}] {s:42s} {str(r.get('name'))[:28]:28s} "
              f"inv={r.get('site_invest_year')} cats={r.get('categories_site')}", flush=True)
        OUT.write_text(json.dumps({"_readme": __doc__, "pulled": time.strftime("%Y-%m-%d"),
                                   "companies": out}, indent=1))
        time.sleep(0.25)
    named = sum(1 for v in out.values() if v.get("name"))
    dated = sum(1 for v in out.values() if v.get("site_invest_year"))
    print(f"named {named}/{len(out)}, invest-year {dated}/{len(out)} -> {OUT}")


if __name__ == "__main__":
    main()
