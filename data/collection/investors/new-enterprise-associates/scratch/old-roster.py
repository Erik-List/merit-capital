#!/usr/bin/env python3
"""NEA's pre-2013 team listings -> scratch/roster-ia.json (the shape build-roster.py reads:
{slug: {"names": [...], "titles": {year: title}, "years": [...], "sources": [url...]}}).

Inputs: any saved team-listing page under scratch/old-team/*.html whose file name starts with
the capture timestamp (YYYYMMDDhhmmss-...). Two markups are read:
  2010-13  ASP.NET /Team/Default.aspx: <table class="TeamListTable"> rows of Name | Title | Office
  2008-10  ColdFusion /NEATeam/All/: name and title pairs (read when present)
A year counts once per person with the first title seen that year.
"""
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

SRC = HERE / "old-team"
OUT = HERE / "roster-ia.json"


def slug_of(name):
    import unicodedata
    name = re.sub(r"\s*['\"(][^'\")]*['\")]", " ", name)          # Krishna 'Kittu' Kolluri
    name = re.sub(r",?\s*\b(MD|PhD|Ph\.D\.|JD|MBA)\b\.?", "", name)
    f = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", f.lower().replace(".", "")).strip("-"), re.sub(r"\s+", " ", name).strip(" ,")


def cells(row):
    return [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip()
            for c in re.findall(r"<td[^>]*>([\s\S]*?)</td>", row, re.I)]


def main():
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    for f in sorted(SRC.glob("*.html")):
        year = f.name[:4]
        body = f.read_text(encoding="utf-8", errors="replace")
        pairs = []
        for tbl in re.findall(r'<table class="TeamListTable">([\s\S]*?)</table>', body, re.I):
            for row in re.findall(r"<tr[^>]*>([\s\S]*?)</tr>", tbl, re.I):
                c = cells(row)
                if len(c) >= 2 and c[0] and c[1]:
                    pairs.append((c[0], c[1]))
        if not pairs:      # 2008-10: <P CLASS="partner-name"><A ...>Name</A></P> <P><STRONG>Title</STRONG>
            for m in re.finditer(r'CLASS="partner-name">\s*<A[^>]*>([^<]{3,60})</A>\s*</P>\s*<P>\s*<STRONG>([^<]{2,90})</STRONG>',
                                 body, re.I):
                pairs.append((html.unescape(m.group(1)).strip(), html.unescape(m.group(2)).strip()))
        for name, title in pairs:
            s, clean = slug_of(name)
            p = out.setdefault(s, {"names": [], "titles": {}, "years": [], "sources": []})
            if clean not in p["names"]:
                p["names"].append(clean)
            p["titles"].setdefault(year, title)
            if year not in p["years"]:
                p["years"].append(year)
            if f.name not in p["sources"]:
                p["sources"].append(f.name)
        print(f.name, len(pairs), "rows")
    write_atomic(OUT, json.dumps(dict(sorted(out.items())), indent=1, ensure_ascii=False) + "\n")
    print(len(out), "people")


if __name__ == "__main__":
    main()
