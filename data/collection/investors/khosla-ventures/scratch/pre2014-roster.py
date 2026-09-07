#!/usr/bin/env python3
"""Resolve the pre-2014 partner namespaces the CDX roster pattern cannot reach.

COLLECTION.md §5.2 / decisions.md D11: partner-roster.py enumerates
/team/<first-last> and /team-member/<first-last> and so covers 2014-2026 only.
Khosla's first decade used two other shapes -- /people_<initials>.html (and the
same file under /khosla/) in 2010-2013, and /<lastname>.html in 2006-2009 --
and a roster that starts in 2014 structurally misses the partner-anchored Form D
filings of the firm's first decade, which is most of the cleantech book.

Both namespaces name the person in the page <title> ("andrew chung « Khosla
Ventures") or, on the flat 2006-2009 pages which have no per-page title, in the
first proper-name run of the body text. Writes the resolved names with the
capture years that bracket them.

Usage: python3 scratch/pre2014-roster.py
"""
import json, re, subprocess, sys, time
from html import unescape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "sources" / "wayback"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
INITIALS = ['ac','bl','df','dm','dw','et','ft','gy','jk','kr','mh','mn','mt','pl',
            'ra','rb','rk','sk','sm','sp','ss','sven','vk']
LASTNAMES = ['vinod','kaul','weiden','lamond','kim','kinnier','tamer','yu',
             'cameron','white','adeeb']
SKIP = {'Khosla Ventures','Sand Hill','Menlo Park','Business 2','Silicon Valley',
        'All Rights','Rights Reserved','The Designer','Designer Fund'}


def get(u):
    for a in range(3):
        r = subprocess.run(["curl", "-sfL", "--compressed", "--max-time", "60",
                            "-H", f"User-Agent: {UA}", u], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode("utf-8", "replace")
        time.sleep(1.5 * (a + 1))
    return ""


def main():
    out = {}
    for ini in INITIALS:
        hit = None
        for yr in (2012, 2013, 2011, 2010, 2014):
            for base in (f"http://www.khoslaventures.com/people_{ini}.html",
                         f"http://www.khoslaventures.com/khosla/people_{ini}.html"):
                h = get(f"https://web.archive.org/web/{yr}id_/{base}")
                if not h:
                    continue
                t = re.search(r"<title>([^<]*)</title>", h)
                nm = unescape(t.group(1)).split("«")[0].strip() if t else ""
                if nm and nm.lower() != "khosla ventures":
                    hit = {"name": nm.title(), "raw_title": nm, "year": yr,
                           "path": base.split(".com")[1], "source": "wayback_people_initials"}
                    break
            if hit:
                break
        if hit:
            out[f"people_{ini}"] = hit
            print(f"  people_{ini:6s} {hit['year']} {hit['name']}", flush=True)
        else:
            print(f"  people_{ini:6s} UNRESOLVED", flush=True)
        time.sleep(0.4)

    for ln in LASTNAMES:
        hit = None
        for yr in (2008, 2007, 2009, 2006):
            h = get(f"https://web.archive.org/web/{yr}id_/http://www.khoslaventures.com/{ln}.html")
            if not h:
                continue
            t = re.sub(r"(?s)<(script|style).*?</\1>", "", h)
            txt = unescape(re.sub(r"<[^>]+>", " ", t))
            for c in re.findall(r"\b([A-Z][a-z]+(?: [A-Z]\.)? [A-Z][a-zA-Z'-]+)\b", txt):
                if c not in SKIP:
                    hit = {"name": c, "year": yr, "path": f"/{ln}.html",
                           "source": "wayback_flat_pages"}
                    break
            if hit:
                break
        if hit:
            out[f"early_{ln}"] = hit
            print(f"  early_{ln:9s} {hit['year']} {hit['name']}", flush=True)
        else:
            print(f"  early_{ln:9s} UNRESOLVED", flush=True)
        time.sleep(0.4)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "pre2014-people.json").write_text(json.dumps(
        {"_readme": __doc__, "pulled": time.strftime("%Y-%m-%d"), "people": out}, indent=1))
    print(f"resolved {len(out)} -> {OUT/'pre2014-people.json'}")


if __name__ == "__main__":
    main()
