#!/usr/bin/env python3
"""Pull luxcapital.com/news as the firm's own announcement archive.

COLLECTION.md §6: the strongest entry_stage evidence is a URL naming the round
and the firm's participation, and the firm's own announcement archive is where
that lives (scored class 1 on Creandum). Lux's sitemap carries 195 /news posts;
each is fetched once and scanned for round words so the gate can score the
layer before the grind trusts it.

Writes sources/site/news-archive.json: one row per post with its title, date,
body text and every (company, round, amount) triple the body states.
"""
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
ROUND = re.compile(
    r"\b(pre-seed|seed(?:\s+extension)?|series\s+[A-K](?:-\d)?|angel|"
    r"bridge|growth\s+round|IPO|SPAC|tender|secondary)\b", re.I)
AMOUNT = re.compile(r"\$\s?(\d+(?:\.\d+)?)\s*(million|billion|M\b|B\b)", re.I)


def get(url: str, dest: Path) -> str:
    if dest.exists():
        return dest.read_text(encoding="utf-8", errors="replace")
    for _ in range(3):
        try:
            out = subprocess.run(["curl", "-sfL", "--compressed", "--max-time", "60",
                                  "-H", f"User-Agent: {UA}", url],
                                 capture_output=True, check=True).stdout.decode(
                                     "utf-8", errors="replace")
            write_atomic(dest, out)
            time.sleep(0.2)
            return out
        except subprocess.CalledProcessError:
            time.sleep(2)
    return ""


def visible(html: str) -> str:
    cut = html.find('class="section_related"')
    main = html[:cut] if cut > 0 else html
    t = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", main)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", unescape(t)).strip()


def main():
    p = Paths("lux-capital")
    raw = p.scratch / "news-raw"
    raw.mkdir(parents=True, exist_ok=True)
    sm = (p.scratch / "site-raw" / "sitemap.xml").read_text(encoding="utf-8", errors="replace")
    urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if "/news/" in u]
    print(f"news posts: {len(urls)}")
    rows = []
    for i, u in enumerate(urls, 1):
        slug = u.rstrip("/").rsplit("/", 1)[-1]
        html = get(u, raw / f"{slug}.html")
        if not html:
            continue
        title = re.search(r"<h1[^>]*>([^<]*)</h1>", html)
        # Webflow renders the post date as plain text ("December 17, 2019");
        # there is no <time> element and no JSON-LD datePublished.
        date = re.search(r'>([A-Z][a-z]+ \d{1,2}, 20\d\d)<', html)
        body = visible(html)
        rounds = sorted({m.group(0).lower() for m in ROUND.finditer(body)})
        amts = [f"${m.group(1)}{m.group(2)[0].upper()}" for m in AMOUNT.finditer(body)][:6]
        rows.append({"slug": slug, "title": unescape(title.group(1)).strip() if title else None,
                     "date": date.group(1) if date else None,
                     "rounds_mentioned": rounds, "amounts_mentioned": amts,
                     "url": u, "body": body[:2500]})
        if i % 50 == 0:
            print(f"  {i}/{len(urls)}")
    write_atomic(p.site / "news-archive.json", json.dumps(
        {"_readme": "luxcapital.com/news posts from the sitemap, parsed by "
                    "scratch/news-pull.py. The firm's own announcement archive: "
                    "class-1 entry_stage evidence where a post names the round and "
                    "Lux's participation (COLLECTION.md §6 evidence order 1).",
         "rows": rows}, indent=1))
    with_round = sum(1 for r in rows if r["rounds_mentioned"])
    print(f"news: {len(rows)} posts, {with_round} naming a round")


if __name__ == "__main__":
    main()
