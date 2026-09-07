#!/usr/bin/env python3
"""Battery's own post archive, for entry_stage citations.

battery.com does not expose its `company` post type over REST, but it DOES
expose `posts` (243 of them). Investment announcements sit in there among the
thought-leadership, and each names a round ("our investment in X's Series B").

Read under the Menlo rule (COLLECTION.md 6): an announcement is class 1 for
the round it NAMES, and asserts an ENTRY only where the post says so in words
("we first invested in ... seed"). Scored on the calibration gate before it
labels anything.

Output: sources/site/announcements.json
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

UA = "merit-capital-research/1.0 (list.erik.2005@gmail.com)"
P = Paths("battery-ventures")
OUT = P.site / "announcements.json"
ROUND = re.compile(
    r"\b(pre-seed|seed(?:\s+extension)?|series\s+[A-J](?:-\d)?|"
    r"growth\s+round|growth\s+investment|buyout|majority\s+(?:stake|investment|"
    r"recapitalization|recapitalisation)|minority\s+(?:stake|investment)|"
    r"acquisition|take-private|tender\s+offer|round\s+[A-J])\b", re.I)
ENTRY = re.compile(
    r"\b(we first (?:invested|backed|met|partnered)|first invested in|"
    r"our first (?:investment|check)|led (?:the|their|its) [^.]{0,40}?"
    r"(?:seed|series\s+[A-J])|initial investment|when we invested)\b", re.I)


def curl(url: str, tries: int = 4):
    for i in range(tries):
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", "replace")
        except subprocess.CalledProcessError:
            time.sleep(1.5 * (i + 1))
    return ""


def txt(h): return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def main() -> None:
    posts = []
    for page in range(1, 4):
        raw = curl("https://www.battery.com/wp-json/wp/v2/posts"
                   f"?per_page=100&page={page}")
        if not raw:
            continue
        try:
            posts.extend(json.loads(raw))
        except json.JSONDecodeError:
            pass
    print(f"posts: {len(posts)}")
    rows = []
    for p in posts:
        title = txt(p.get("title", {}).get("rendered", ""))
        body = txt(p.get("content", {}).get("rendered", ""))
        rounds = sorted({m.group(0).lower() for m in ROUND.finditer(title + " " + body)})
        rows.append({
            "slug": p.get("slug"), "date": (p.get("date") or "")[:10],
            "title": title, "url": p.get("link"),
            "rounds_named": rounds,
            "asserts_entry": bool(ENTRY.search(body)),
            "entry_phrases": sorted({m.group(0).lower()
                                     for m in ENTRY.finditer(body)})[:4],
            "excerpt": body[:1500],
        })
    rows.sort(key=lambda r: r["date"], reverse=True)
    write_atomic(OUT, json.dumps({
        "_readme": ("Battery's own post archive via /wp-json/wp/v2/posts (the "
                    "`company` type is not REST-exposed but `posts` is). "
                    "`rounds_named` are the round words the post uses; "
                    "`asserts_entry` marks posts that say in words that this was "
                    "the firm's FIRST investment, which is the only case an "
                    "announcement evidences an ENTRY rather than a round "
                    "(COLLECTION.md 6, the Menlo rule)."),
        "_pulled": time.strftime("%Y-%m-%d"),
        "rows": rows}, indent=1))
    withr = [r for r in rows if r["rounds_named"]]
    print(f"wrote {OUT}: {len(rows)} posts, {len(withr)} naming a round, "
          f"{sum(1 for r in rows if r['asserts_entry'])} asserting an entry")
    for r in withr[:12]:
        print(f"   {r['date']}  {','.join(r['rounds_named'])[:28]:28s} {r['title'][:60]}")


if __name__ == "__main__":
    main()
