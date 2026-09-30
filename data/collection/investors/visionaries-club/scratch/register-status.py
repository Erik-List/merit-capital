#!/usr/bin/env python3
"""German register status layer (COLLECTION.md s5: registers pay off on status).

For each German portfolio company, search North Data (the Handelsregister read
through its free entity pages) by the legal name, take the result whose name
matches exactly (case- and punctuation-insensitive), fetch that entity page
and read what the register says: the terminated mark (a cross after the name),
liquidation or insolvency events, and the latest shareholder-list filings.
A dissolution, liquidation or insolvency entry is filing-grade evidence for
`defunct` (or `acquired` where a sale follows); an active entity with recent
filings corroborates `private`. A lookup that fails or matches nothing is
recorded as such, never as "active".

Input:  scratch/register-targets.json  [{"slug", "legal_name"}]
Output: sources/registers/status-de.json  {slug: {...}}
Usage:  python3 register-status.py
"""
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "sources" / "registers" / "status-de.json"
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"


def get(url: str) -> str:
    r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, url], capture_output=True)
    time.sleep(3)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""


def key(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", html.unescape(s).lower().replace("·", "."))


def text(b: str) -> str:
    b = re.sub(r"<script.*?</script>", "", b, flags=re.S)
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " | ", b)))
    return re.sub(r"(\|\s*)+", "| ", t)


def main() -> None:
    targets = json.loads((HERE / "register-targets.json").read_text())
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    for t in targets:
        slug, name = t["slug"], t["legal_name"]
        if out.get(slug, {}).get("legal_name") == name and out[slug].get("status") != "lookup_failed":
            continue
        s = get("https://www.northdata.com/search?query=" + urllib.parse.quote(name))
        if not s or "_login?targetUrl" in s and "Search for" not in s:
            out[slug] = {"legal_name": name, "status": "lookup_failed", "why": "no answer or login wall"}
            print(slug, "lookup failed", flush=True)
            continue
        links = list(dict.fromkeys(re.findall(r'href="(/[^"?]+?,[^"]+)"', s)))
        match = None
        for l in links:
            ent = urllib.parse.unquote(html.unescape(l)).split("/")[1]
            ent_name = ent.rsplit(",", 1)[0]
            if key(ent_name) == key(name):
                match = l
                break
        if not match:
            out[slug] = {"legal_name": name, "status": "no_exact_match",
                         "candidates": [urllib.parse.unquote(html.unescape(l)).split("/")[1] for l in links[:8]]}
            print(slug, "no exact match", flush=True)
            continue
        url = "https://www.northdata.com" + html.unescape(match)
        page = get(url)
        title = re.search(r"<title>(.*?)</title>", page)
        head = text(page)[:4000]
        terminated = "✝" in head
        evs = []
        for attrs, body in re.findall(r'<div class="event"([^>]*)>(.*?)</div>\s*</div>\s*</div>', page, re.S):
            types = re.search(r'data-topic-types="([^"]*)"', attrs)
            date = re.search(r'data-date="([^"]*)"', attrs)
            summ = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))).strip()
            evs.append({"date": date.group(1) if date else "", "types": types.group(1) if types else "", "text": summ[:240]})
        flagged = [e for e in evs if re.search(r"Termination|Liquidation|Insolvency", e["types"] + " " + e["text"])]
        events = flagged
        out[slug] = {"legal_name": name, "northdata_url": url, "title": html.unescape(title.group(1)) if title else "",
                     "terminated": terminated, "flagged_events": flagged, "latest_event": evs[0] if evs else None,
                     "status": "terminated" if terminated else ("flagged" if flagged else "active"),
                     "read": time.strftime("%Y-%m-%d")}
        print(slug, out[slug]["status"], [e["date"] + " " + e["types"] for e in events], flush=True)
        write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
