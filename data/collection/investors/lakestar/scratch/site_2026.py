#!/usr/bin/env python3
"""The live lakestar.com (July 2026 relaunch) as a file_list source.

Reads sources/site/raw/wp-pages-2026-10-01.json (the open wp-json pages
endpoint, ACF blocks included) and writes sources/site/companies-2026.json:
one row per company shown on any of the three logo blocks (home, /funds,
/resilience) or named in the Resilience I press release (/resiliencepress).
The logo blocks carry an image and an optional link, never a name, so the
name comes from NAMES below, keyed on the logo file stem; a logo this map does
not know stops the script rather than landing under its file name.
"""
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parent.parent
RAW = INV / "sources" / "site" / "raw" / "wp-pages-2026-10-01.json"
OUT = INV / "sources" / "site" / "companies-2026.json"

# logo file stem (digits and trailing "-N" stripped, lowercased) -> the company
NAMES = {
    "airbnb": "Airbnb", "coinbase": "Coinbase", "facebook": "Facebook", "fuse": "Fuse Energy",
    "helsing": "Helsing", "isar": "Isar Aerospace", "klarna": "Klarna", "neko": "Neko Health",
    "revolut": "Revolut", "spotify": "Spotify", "sumup": "SumUp", "auterion": "Auterion",
    "constellr": "Constellr", "dexory": "Dexory", "exein": "Exein", "harrys": "Harry's",
    "htg": "HomeToGo", "poolside": "Poolside", "public": "Public", "sennder": "Sennder",
    "vertice": "Vertice", "24": "Twentyfour Industries", "agon": "Agon", "arx": "ARX Robotics",
    "cambridge": "Cambridge Aerospace", "dominion-dynamics": "Dominion Dynamics",
    "frankenburg": "Frankenburg Technologies", "kela": "Kela", "kraken": "Kraken Technology",
    "lateration": "Lateration", "onodrim": "Onodrim", "se3": "SE3 Labs",
    "swarm": "SWARM Biotactics", "tekever": "Tekever", "hackinggames": "The Hacking Games",
    "tiberius": "Tiberius", "tytan": "Tytan Technologies", "uforce": "UFORCE",
}
# the Resilience I press release (17 July 2026) names its portfolio in prose
PRESS = ["ARX Robotics", "Auterion", "Cambridge Aerospace", "Constellr", "Dominion Dynamics",
         "Frankenburg Technologies", "Helsing", "Isar Aerospace", "Kela", "Kraken Technology",
         "Lateration", "Onodrim", "SE3 Labs", "SWARM Biotactics", "Tekever", "The Hacking Games",
         "Tiberius", "Twentyfour Industries", "Tytan Technologies", "UFORCE"]
PAGE_URL = {"home": "https://www.lakestar.com/", "funds": "https://www.lakestar.com/funds",
            "resilience": "https://www.lakestar.com/resilience",
            "resiliencepress": "https://www.lakestar.com/resiliencepress"}


def stem(url: str) -> str:
    s = url.rsplit("/", 1)[-1].rsplit(".", 1)[0].lower()
    return re.sub(r"-\d+$", "", s)


def main() -> None:
    pages = {p["slug"]: p for p in json.loads(RAW.read_text())}
    rows: dict[str, dict] = {}
    for slug in ("home", "funds", "resilience"):
        for b in pages[slug]["acf"]["blocks"]:
            if b.get("acf_fc_layout") != "logos":
                continue
            for lg in b["logos"]:
                st = stem(lg["logo"]["url"])
                if st not in NAMES:
                    raise SystemExit(f"unknown logo {lg['logo']['url']} on /{slug}")
                name = NAMES[st]
                link = lg.get("link") if isinstance(lg.get("link"), dict) else {}
                r = rows.setdefault(name, {"name": name, "url": PAGE_URL[slug], "website": "",
                                           "surfaces": [], "logo": lg["logo"]["url"]})
                r["surfaces"].append(slug)
                if link.get("url") and not r["website"]:
                    r["website"] = link["url"]
    press_text = json.dumps(pages["resiliencepress"]["acf"])
    for name in PRESS:
        probe = name.split()[0] if name not in ("The Hacking Games",) else "Hacking Games"
        if probe.lower() not in press_text.lower():
            raise SystemExit(f"{name} not found in the press release text")
        r = rows.setdefault(name, {"name": name, "url": PAGE_URL["resiliencepress"], "website": "",
                                   "surfaces": [], "logo": ""})
        r["surfaces"].append("resiliencepress")
    out = {
        "_readme": "Lakestar's own live site, read 2026-10-01 from the open wp-json pages endpoint "
                   "(sources/site/raw/wp-pages-2026-10-01.json). One row per company on the three logo "
                   "blocks (home 11, /funds 15, /resilience 21) or named in the Resilience I press "
                   "release of 17 July 2026 (20 names). The blocks carry a logo image and an optional "
                   "link, no name, date or round: the name is mapped from the logo file stem in "
                   "scratch/site_2026.py. url is the first page that shows the company; surfaces lists all.",
        "rows": sorted(rows.values(), key=lambda r: r["name"].lower()),
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(rows)} companies -> {OUT.relative_to(INV)}")
    for r in out["rows"]:
        print(f"  {r['name']:28s} {','.join(r['surfaces'])}")


if __name__ == "__main__":
    main()
