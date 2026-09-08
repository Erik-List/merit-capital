#!/usr/bin/env python3
"""Pull www.khoslaventures.com's Webflow surfaces into file_list sources.

The sitemap has no per-company pages: the entire portfolio is one
server-rendered /portfolio page whose eight category sections each hold a
swiper carousel of company cards. Each card carries the company's outbound
URL, the firm's own fund label (Seed / Early / Growth), an exchange ticker
where the company is listed, a one-line tagline, an investment thesis and a
milestone. /team/<slug> pages (46 in the sitemap) are the current roster.

Writes: sources/site/webflow-portfolio.json, sources/site/team-webflow.json
Usage:  python3 scratch/site-pull.py
"""
import json, re, subprocess, sys, time
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parents[1] / "sources" / "site"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
BASE = "https://www.khoslaventures.com"


def get(url: str) -> str:
    for attempt in range(4):
        r = subprocess.run(["curl", "-sfL", "--compressed", "--max-time", "60",
                            "-H", f"User-Agent: {UA}", url], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode("utf-8", "replace")
        time.sleep(2 * (attempt + 1))
    print(f"  !! fetch failed: {url}")
    return ""


def clean(s):
    return re.sub(r"\s+", " ", unescape(s or "").replace("\xa0", " ")).strip() or None


CATS = ["consumer-retail", "enterprise", "fintech", "frontier", "sustainability",
        "digital-health", "medtech-diagnostics", "therapeutics"]
CAT_LABEL = {"consumer-retail": "Consumer & Retail", "enterprise": "Enterprise",
             "fintech": "Fintech", "frontier": "Frontier",
             "sustainability": "Sustainability", "digital-health": "Digital Health",
             "medtech-diagnostics": "MedTech & Diagnostics",
             "therapeutics": "Therapeutics"}


def portfolio():
    h = get(f"{BASE}/portfolio")
    bounds = sorted((m.start(), a) for a in CATS
                    for m in re.finditer(rf'id="{a}"', h))
    bounds.append((len(h), None))
    rows, seen = [], {}
    for (start, cat), (end, _) in zip(bounds[:-1], bounds[1:]):
        chunk = h[start:end]
        for blk in re.findall(
                r'class="swiper-slide w-dyn-item">(.{0,4000}?)'
                r'(?:<div role="listitem" class="swiper-slide|</div></div></div>)',
                chunk, re.S):
            alt = re.search(r'alt="([^"]*)"', blk)
            back = re.search(r'back-company-title">([^<]*)<', blk)
            # The card renders the name twice: the logo's alt attribute and the
            # flip side's own title. COLLECTION.md's Lux rule says the row's own
            # rendering wins over the image alt -- but here the alt is the fuller
            # string on multi-word names ("Eight Sleep" vs a truncated back
            # title), so take the LONGER of the two and keep both.
            a, b = clean(alt.group(1)) if alt else None, clean(back.group(1)) if back else None
            name = max([x for x in (a, b) if x], key=len, default=None)
            if not name:
                continue
            url = re.search(r'href="(https?://[^"]+)"', blk)
            fund = re.search(r'fund-round-text">([^<]*)<', blk)
            tick = re.search(r'stock-ticker-text">([^<]*)<', blk)
            tag = re.search(r'company-card-title">([^<]*)<', blk)
            thesis = re.search(r'Investment Thesis</div><div class="back-text">([^<]*)<', blk)
            mile = re.search(r'Milestone</div><div class="back-text">([^<]*)<', blk)
            key = name.lower()
            if key in seen:
                seen[key]["sectors_site"].append(CAT_LABEL[cat])
                continue
            row = {"name": name, "name_alt": a, "name_card": b,
                   "url": clean(url.group(1)) if url else None,
                   "site_fund_label": clean(fund.group(1)) if fund else None,
                   "ticker": clean(tick.group(1)) if tick else None,
                   "tagline": clean(tag.group(1)) if tag else None,
                   "thesis": clean(thesis.group(1)) if thesis else None,
                   "milestone": clean(mile.group(1)) if mile else None,
                   "category": CAT_LABEL[cat], "sectors_site": [CAT_LABEL[cat]]}
            seen[key] = row
            rows.append(row)
    return rows


def team():
    sm = get(f"{BASE}/sitemap.xml")
    slugs = sorted({m.group(1) for m in
                    re.finditer(r"<loc>https://www\.khoslaventures\.com/team/([^<]+)</loc>", sm)})
    out = []
    for s in slugs:
        h = get(f"{BASE}/team/{s}")
        if not h:
            continue
        name = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S)
        title = re.search(r'class="[^"]*team-member-title[^"]*"[^>]*>(.*?)<', h, re.S)
        if not title:
            title = re.search(r'class="[^"]*role[^"]*"[^>]*>(.*?)<', h, re.S)
        li = re.search(r'href="(https?://(?:www\.)?linkedin\.com/[^"]+)"', h)
        x = re.search(r'href="(https?://(?:www\.)?(?:x|twitter)\.com/[^"]+)"', h)
        out.append({"name": clean(re.sub(r"<[^>]+>", " ", name.group(1))) if name else s,
                    "slug": s, "url": f"{BASE}/team/{s}",
                    "title": clean(re.sub(r"<[^>]+>", " ", title.group(1))) if title else None,
                    "group": None,
                    "linkedin_url": li.group(1) if li else None,
                    "x_url": x.group(1) if x else None,
                    "source": "site_team"})
        time.sleep(0.3)
    return out


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    comps = portfolio()
    readme = ("Parsed from the single server-rendered https://www.khoslaventures.com/portfolio "
              "page (Webflow, no CMS API, no per-company pages in the sitemap) by "
              "scratch/site-pull.py. Eight category sections, one swiper carousel each. "
              "site_fund_label is the firm's OWN fund label on the card (Seed / Early / "
              "Growth) and is scored on the golden set before it may label entry_stage.")
    (OUT / "webflow-portfolio.json").write_text(json.dumps(
        {"_readme": readme, "pulled": time.strftime("%Y-%m-%d"),
         "companies-live": comps, "rows": comps}, indent=1))
    # "rows" is the key site-portfolio.py's parse_file_list actually reads;
    # the descriptive key is kept so the file reads on its own.
    print(f"portfolio: {len(comps)} companies -> {OUT/'webflow-portfolio.json'}")
    t = team()
    (OUT / "team-webflow.json").write_text(json.dumps(
        {"_readme": "https://www.khoslaventures.com/team/<slug> pages enumerated from "
                    "the live sitemap by scratch/site-pull.py.",
         "pulled": time.strftime("%Y-%m-%d"), "team": t, "rows": t}, indent=1))
    print(f"team: {len(t)} people -> {OUT/'team-webflow.json'}")
