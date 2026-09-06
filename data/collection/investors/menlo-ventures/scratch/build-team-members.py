#!/usr/bin/env python3
"""menlovc.com team pages -> sources/site/team-members.json.

The live CMS `teams` collection gives names and URLs; the title and the socials
live on each person's own page. role_bucket separates the investing seats from
platform, finance and operations, which is what the profile publishes and what
the Form D roster sweep should be read against.
"""
import json, re, subprocess, sys, time
from html import unescape
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")
INVEST = re.compile(r"partner|managing director|principal|investor|venture|chief investment", re.I)


def curl(url: str) -> str:
    r = subprocess.run(["curl", "-sL", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                       capture_output=True)
    return r.stdout.decode("utf-8", "replace")


def main() -> None:
    p = Paths("menlo-ventures")
    cache = Path(__file__).resolve().parent / "team-pages"
    cache.mkdir(exist_ok=True)
    team = json.loads((p.site / "team.json").read_text())
    cards = json.loads((p.site / "portfolio-cards.json").read_text())["rows"]
    deal_partners = {q["name"] for r in cards for q in (r.get("partners") or []) if q.get("name")}
    out = []
    for t in team:
        slug = t.get("slug") or (t.get("url") or "").rstrip("/").rsplit("/", 1)[-1]
        f = cache / f"{slug}.html"
        if not f.exists():
            write_atomic(f, curl(t.get("url") or f"https://menlovc.com/team/{slug}/"))
            time.sleep(0.5)
        h = f.read_text(encoding="utf-8", errors="replace")
        h = re.sub(r"<svg.*?</svg>", " ", h, flags=re.S)
        title = None
        # The team page renders the person's name and their sector tags but no
        # job title; the firm states the role in its own meta description
        # ("Matt Murphy is a partner at Menlo Ventures and invests ..."), which
        # is the firm's own text and the only title source the site publishes.
        desc = re.search(r'<meta name="description" content="([^"]*)"', h)
        blurb = unescape(desc.group(1)) if desc else ""
        mm = re.search(r"\bis (?:a|an|the) ([^.,;]{3,60}?) (?:at|of|with) Menlo", blurb, re.I)
        for rx in (r"\b(?:serves as|joined Menlo Ventures as) (?:a|an|the) ([^.,;]{3,60})",
                   r"^As (?:a|an|the) ([^.,;]{3,60}?) (?:at|of|with) Menlo",
                   r"^As ([A-Z][^.,;]{3,60}?) (?:at|of|with) Menlo",
                   r"\bwas (?:a|the) (founder) of Menlo Ventures"):
            if mm:
                break
            mm = re.search(rx, blurb, re.I)
        if mm:
            title = mm.group(1).strip()
        sectors = re.search(r"<h1[^>]*>.*?</h1>(.{0,400}?)</span", h, re.S)
        tags = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", sectors.group(1))).strip() if sectors else ""
        li = re.search(r'href="(https://(?:www\.)?linkedin\.com/in/[^"]+)"', h)
        xx = re.search(r'href="(https://(?:x|twitter)\.com/[^"]+)"', h)
        out.append({"name": t["name"], "cms_title": title,
                    # An investing seat is one the firm itself attributes a deal to on
                    # its own portfolio cards, or one whose stated title says so.
                    "role_bucket": ["investing"] if (t["name"] in deal_partners
                                                     or (title and INVEST.search(title)))
                                   else ["platform"],
                    "linkedin_url": li.group(1) if li else None,
                    "x_url": xx.group(1) if xx else None,
                    "sectors": tags or None, "blurb": blurb[:280] or None,
                    "source": f"menlovc.com/team/{slug}/ (live CMS team collection, pulled 2026-09-06; "
                              f"title taken from the firm's own meta description, the only place the site states one)"})
    write_atomic(p.site / "team-members.json", json.dumps(out, indent=1) + "\n")
    from collections import Counter
    print(f"team members: {len(out)}  with titles: {sum(1 for x in out if x['cms_title'])}  "
          f"buckets: {dict(Counter(x['role_bucket'][0] for x in out))}")
    for x in out:
        print(f"   {x['name']:<24} {x['cms_title']}")


if __name__ == "__main__":
    main()
