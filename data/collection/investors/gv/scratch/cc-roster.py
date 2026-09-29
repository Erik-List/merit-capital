#!/usr/bin/env python3
"""GV's historical people, with per-year titles and capture-year windows, from Common Crawl
(scratch/cc-index-raw.json + the bodies cc-fetch.py saved under data/filings/commoncrawl/gv/).

  2012-13  googleventures.com/team/<slug>: "<Name> | <Title> | @handle | Companies | a | , | b |
           <bio> | <First> is part of the | Investing Team | ..."  (the partner's own company list)
  2013-15  gv.com/team/<slug>: "<Name> | <Title> | <bio> | Investments | <description> | Partner | <Name>"
  2016-18  gv.com/team/<slug>/: "GV / <Name>" page title, "<Name> | <Title> | <bio>"
  later    whatever the capture carries; the title after the name, else none.

The title is read per capture, because it moves: Kevin Rose is "General Partner" to 2015 and
"GV Advisor" from 2016 ("Previously, he was a general partner at GV"), so a window is the
years a person held an investing title, never the years the page existed.
Output scratch/roster-cc.json: {slug: {names, years, titles {year: title}, groups, companies,
former_years, capture_urls}}.
Usage: python3 cc-roster.py
"""
import collections
import html as H
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "gv"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
OUT = HERE / "roster-cc.json"
TITLE_WORD = re.compile(r"partner|principal|associate|advisor|adviser|director|fellow|officer|counsel|manager|"
                        r"analyst|head|chief|founder|entrepreneur|\beir\b|venture|investor|controller|engineer|"
                        r"designer|research|recruit|marketing|operations|coordinator|assistant|\blead\b|cfo|coo|"
                        r"ceo|talent|portfolio|scientist|chair|president|specialist|editor|writer|producer", re.I)
PAGE_TITLE = [re.compile(r"^Google Ventures\s*[—–-]\s*(.+)$"), re.compile(r"^GV\s*/\s*(.+)$"),
              re.compile(r"^GV\s*[—–-]\s*(.+)$"),
              re.compile(r"^(.+?)\s*\|\s*(?:Google Ventures|GV)\b"), re.compile(r"^(?:Google Ventures|GV)\s*\|\s*(.+)$")]
FORMER = re.compile(r"\b(previously|formerly),?\s+(?:he|she|they)?\s*(?:was|were|served as)\s+(?:a\s+)?"
                    r"(?:general |managing |venture )?partner at (?:GV|Google Ventures)", re.I)
JOINED = re.compile(r"\bjoined (?:GV|Google Ventures)(?: as [^.,]{3,40})? in ((?:19|20)\d\d)", re.I)


def text_of(t):
    b = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S | re.I)
    x = H.unescape(re.sub(r"<[^>]+>", " | ", b))
    return [s.strip() for s in re.split(r"\s*\|\s*", re.sub(r"\s+", " ", x)) if s.strip()]


def main():
    man = json.loads(MAN.read_text())
    people = collections.defaultdict(lambda: {"names": set(), "years": set(), "titles": {}, "groups": {},
                                              "companies": {}, "former_years": set(), "joined": set(),
                                              "capture_urls": {}})
    unread = []
    for k, v in sorted(man.items(), key=lambda kv: kv[1].get("timestamp", "")):
        if v.get("status") != "ok":
            continue
        m = re.match(r"^/team/([a-z][a-z0-9-]+)/?$", v.get("path", ""))
        if not m:
            continue
        slug, year = m.group(1), int(v["timestamp"][:4])
        t = (RAW / k).read_text(encoding="utf-8", errors="replace")
        pt = re.search(r"<title>(.*?)</title>", t, re.S)
        pt = re.sub(r"\s+", " ", H.unescape(pt.group(1))).strip() if pt else ""
        name = ""
        for rx in PAGE_TITLE:
            mm = rx.match(pt)
            if mm:
                name = mm.group(1).strip()
                break
        toks = text_of(t)
        title = ""
        idx = [i for i, s in enumerate(toks) if name and s == name]
        for i in idx[1:] + idx[:1]:            # skip the page-title echo first
            if i + 1 < len(toks) and len(toks[i + 1]) <= 60 and TITLE_WORD.search(toks[i + 1]) \
                    and not toks[i + 1].startswith("@"):
                title = toks[i + 1]
                break
        if not name or not title:
            unread.append((year, slug, pt[:60]))
        p = people[slug]
        if name:
            p["names"].add(name)
        p["years"].add(year)
        if title:
            p["titles"].setdefault(year, title)
        p["capture_urls"].setdefault(year, v["capture_url"])
        body = " ".join(toks)
        g = re.search(r"is part of the \| ?([A-Za-z &-]+?) \|", " | ".join(toks))
        if g:
            p["groups"][year] = g.group(1).strip()
        if "Investments" in toks and v["domain"] == "gv" and year >= 2022:
            # 2022+ pages: "Investments | A | B * | ... | + 53 more" (the partner's own list, first ~16 shown)
            i = toks.index("Investments")
            comps = []
            for x in toks[i + 1:]:
                if x.startswith("+ ") or len(x) > 45:
                    break
                comps.append(x.replace("*", "").strip())
            if comps:
                p["companies"][year] = comps
        if "Companies" in toks and v["domain"] == "gve":
            i = max(i for i, s in enumerate(toks) if s == "Companies")
            comps = []
            for s in toks[i + 1:]:
                if s == ",":
                    continue
                if len(s) > 45 or s.startswith(name.split()[0] + " "):
                    break
                comps.append(s)
            if comps:
                p["companies"][year] = comps
        if FORMER.search(body):
            p["former_years"].add(year)
        for jy in JOINED.findall(body):
            p["joined"].add(int(jy))
    out = {}
    for s, p in sorted(people.items()):
        out[s] = {"slug": s, "names": sorted(p["names"]), "years": sorted(p["years"]),
                  "titles": {str(y): t for y, t in sorted(p["titles"].items())},
                  "groups": {str(y): g for y, g in sorted(p["groups"].items())},
                  "companies": {str(y): c for y, c in sorted(p["companies"].items())},
                  "former_years": sorted(p["former_years"]), "joined": sorted(p["joined"]),
                  "capture_urls": {str(y): u for y, u in sorted(p["capture_urls"].items())}}
    write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(len(out), "people;", len(unread), "captures without a readable name or title:", unread[:30])


if __name__ == "__main__":
    main()
