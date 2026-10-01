#!/usr/bin/env python3
"""Build Kleiner Perkins' roster for the Form D sweep from first-party sources, into
sources/wayback/partner-roster.json in partner-roster.py's shape
({slug, name, years_seen, first_seen, last_seen, snapshots, sources}) plus title and basis.

Sources (all Common Crawl captures of the firm's own site, or the live site):
  team-2008    kpcb.com/team/* and /team/bio_detail.php (2008-2011): every page carries the whole firm as
               sectioned lists (PARTNERS, TEAM MEMBERS, OPERATING PARTNERS, OPERATIONS, AFFILIATED PARTNERS,
               STRATEGIC LIMITED PARTNERS, PARTNERS EMERITI); a person counts in a capture year when listed
               under PARTNERS, TEAM MEMBERS or OPERATING PARTNERS. AFFILIATED PARTNERS are former partners
               running their own firms (Vinod Khosla at Khosla Ventures, Kevin Compton and Doug Mackenzie at
               Radar Partners, William Hearst, Russell Siegelman): their seats in those years are theirs (T4).
  partner-page kpcb.com/partner/<slug> (2012-2018): the page's own title line ("Investment Partner",
               "Operating Partner", "Director", ...) per capture year; investing titles count.
  deal-panel   the partners the archived company pages (2012-2017) name on a deal, dated by the year the page
               BODY was captured (never the index year: an old page keeps crediting a partner who has left).
  people-page  kleinerperkins.com/people/<slug> (2018 on): a person page existed that year; counted when its
               description or the live CMS role says the person invests.
  site-team    the live WordPress team with an investing role (2026).

Left out: operations, finance, legal, talent, marketing and communications staff, strategic limited
partners (Colin Powell, KR Sridhar: LPs, not investors of the firm), and the emeriti (they sat no seats in
the Form D years). A common name among them buys only false Form D matches.
One person, one entry: name variants fold onto one slug with the union window (VARIANTS).
Usage: python3 build-roster.py
"""
from __future__ import annotations

import collections
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("kleiner-perkins")
OUT = P.wayback / "partner-roster.json"
MAN = P.wayback / "cc-manifest.json"
RAW = ROOT / "data" / "filings" / "commoncrawl" / "kleiner-perkins"
THIS_YEAR = 2026
INVESTING = re.compile(r"investment partner|general partner|managing partner|^partner\b|partner$|, partner\b|principal|"
                       r"associate|venture partner|investor|entrepreneur in residence|\beir\b|chairman|founder|"
                       r"^director$|operating partner|affiliated partner|advisor$|partner and advisor|investing partner", re.I)
NOT_INVESTING = re.compile(r"general counsel|chief financial|chief operating|chief information|marketing|communications|"
                           r"talent|business development|experience|content|operations|finance|legal|recruit|emerit|"
                           r"strategic|engineer", re.I)
# The Bond partners (decisions.md D2): their seats locate Bond from 2018-09, so the window stops at 2018 whatever
# the lingering people pages say.
LAST_YEAR = {"mary-meeker": 2018, "mood-rowghani": 2018, "noah-knauf": 2018, "juliet-de-baubigny": 2018,
             "daegwon-chae": 2018, "paul-vronsky": 2018,
             # affiliated (not investing) partner by the 2008 list; the 2018 people page is an alumnus page
             "doug-mackenzie": 2007}
# An alumnus page that describes the person's next firm is not a year at Kleiner Perkins.
ALUMNUS = re.compile(r"emerit|independent investor|(co-?founder|founder|managing partner)( and managing partner)? of (?!kleiner)|"
                     r"kleiner perkins caufield &(amp;)? byers china|principal engineer|\b(CFO|CMO|COO|CIO)\b|fellows program", re.I)
VARIANTS: dict[str, str] = {"joe-lacob": "joseph-lacob", "russ-siegelman": "russell-siegelman",
                            "will-hearst": "william-hearst-iii", "william-hearst": "william-hearst-iii",
                            "tom-monath": "thomas-monath", "trae-vassallo-barnes": "trae-vassallo",
                            "juliet-flint": "juliet-de-baubigny", "ilya-fushman": "ilya-fushman"}
FILED_NAME = {"william-hearst-iii": "William Hearst", "juliet-de-baubigny": "Juliet de Baubigny"}
SUFFIX = re.compile(r",?\s*\b(MD|M\.D\.|PhD|Ph\.D\.|MBA|JD|Jr\.?|Sr\.?)\b\.?", re.I)
SECTIONS_IN = {"PARTNERS", "TEAM MEMBERS", "OPERATING PARTNERS", "INVESTMENT PARTNERS"}
# KPCB China's team: IN under the provisional X1 reading (decisions.md), so kept; the set is here so a reversal
# of X1 is one line (their seats would then locate KPCB China, not the firm).
KPCB_CHINA: set = set()
SECTIONS_ALL = SECTIONS_IN | {"OPERATIONS", "STRATEGIC LIMITED PARTNERS", "PARTNERS EMERITI", "SENIOR ADVISORS",
                              "ADVISORS", "GROWTH", "CHINA"}


def clean_name(name: str) -> str:
    name = re.sub(r"\s*\([^)]*\)", "", name or "")
    name = SUFFIX.sub("", name.split(",")[0])
    return re.sub(r"\s+", " ", name).strip(" ,")


def slug_of(name: str) -> str:
    folded = unicodedata.normalize("NFKD", clean_name(name)).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", folded.lower().replace(".", "")).strip("-")
    return VARIANTS.get(s, s)


def investing(title: str) -> bool:
    return bool(title) and bool(INVESTING.search(title)) and not NOT_INVESTING.search(title)


def text_of(key: str) -> str:
    s = (RAW / key).read_bytes().decode("utf-8", "replace")
    s = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", "", s, flags=re.I)
    t = re.sub(r"<[^>]+>", "\n", s)
    return re.sub(r"[ \t]*\n\s*", "\n", html.unescape(t)).strip()


def main() -> None:
    people: dict[str, dict] = {}

    def add(name, source, years, basis, title=""):
        name = clean_name(name)
        s = slug_of(name)
        if not s or "-" not in s:
            return
        r = people.setdefault(s, {"slug": s, "name": FILED_NAME.get(s, name), "years": set(), "sources": [],
                                  "basis": collections.defaultdict(set), "titles": {}})
        r["years"] |= set(years)
        if source not in r["sources"]:
            r["sources"].append(source)
        r["basis"][source] |= set(years)
        for y in years:
            if title:
                r["titles"].setdefault(y, title)

    man = {}
    for _mf in sorted(MAN.parent.glob("cc-manifest*.json")):
        man.update(json.loads(_mf.read_text()))
    stats = collections.Counter()
    for key, v in sorted(man.items()):
        if v.get("status") != "ok":
            continue
        path, y = v["path"], int(v["timestamp"][:4])
        # 2008-2011 sectioned team lists
        if re.match(r"^/+team(/|$)", path) and v["domain"] == "kpcb":
            t = text_of(key)
            sec = None
            for line in t.split("\n"):
                u = re.sub(r"\s+", " ", line).strip()
                if u.upper() == u and u.strip() in SECTIONS_ALL:
                    sec = u.strip()
                    continue
                if u in ("Companies", "Team", "News", "Offices") and sec:
                    sec = None
                if u.upper() == u and re.search(r"PARTNER|MEMBER|EMERIT|ADVISOR|OPERATIONS", u):
                    sec = u if u in SECTIONS_ALL else "OTHER"
                    continue
                if sec in SECTIONS_IN and re.match(r"^[A-Z][A-Za-z.'\- ]+(, M\.D\.)?$", u) and 2 <= len(u.split()) <= 5 \
                        and u.upper() != u:
                    add(u, "team-2008", [y], "", {"PARTNERS": "Partner", "TEAM MEMBERS": "Team Member",
                                                    "OPERATING PARTNERS": "Operating Partner",
                                                    "AFFILIATED PARTNERS": "Affiliated Partner",
                                                    "INVESTMENT PARTNERS": "Investment Partner"}[sec])
                    stats["team-2008"] += 1
    # 2012-2018 partner pages and 2018+ people pages: the title (or description) from the one fetched body per
    # page; the years from the Common Crawl index, every year that holds a 200 capture of the page (a proxy that
    # over-reports the end date when a departed person's page lingers; partner-roster.py carries the same caveat).
    idx = json.loads((HERE / "cc-index-raw.json").read_text())
    page_years = collections.defaultdict(set)
    PAGE = re.compile(r"^https?://(?:www\.)?(kpcb|kleinerperkins)\.com(?::\d+)?/+(china/)?(partner|people)/([a-z0-9-]+)/?$", re.I)
    for cid, slots in idx.items():
        for _k, vv in slots.items():
            for rec in vv.get("records", []):
                m = PAGE.match(rec["url"].split("?")[0])
                if m and rec.get("status") == "200":
                    page_years[(m.group(1).lower(), bool(m.group(2)), m.group(4))].add(int(rec["timestamp"][:4]))
    bodies = {}
    for key, v in man.items():
        m = PAGE.match(v["url"].split("?")[0]) if v.get("status") == "ok" else None
        if m:
            bodies[(m.group(1).lower(), bool(m.group(2)), m.group(4))] = key
    for (dom, china, pslug), years in sorted(page_years.items()):
        key = bodies.get((dom, china, pslug))
        if china and not key:
            stats["china partner page (no body)"] += 1
            continue
        if dom == "kpcb":
            title, name = "", pslug.replace("-", " ").title()
            if key:
                lines = [x for x in text_of(key).split("\n") if x.strip()]
                nm = next((x for x in lines if slug_of(x) == slug_of(pslug.replace("-", " "))), "")
                if nm:
                    name = nm
                    i = lines.index(nm)
                    title = lines[i + 1] if i + 1 < len(lines) else ""
            if not key or investing(title):
                add(name, "partner-page", sorted(years), "", title or "partner page (title not read)")
                stats["partner-page"] += 1
            else:
                stats["partner-page not investing"] += 1
        else:
            desc, name = "", pslug.replace("-", " ").title()
            if key:
                sb = (RAW / key).read_bytes().decode("utf-8", "replace")
                d = re.search(r'<meta name="description" content="([^"]*)"', sb)
                desc = html.unescape(d.group(1)) if d else ""
                h = re.search(r'<h1 class="fn">\s*([^<]+?)\s*</h1>', sb) or re.search(r"<title>([^|<]+)", sb)
                name = h.group(1).strip() if h else name
            if (not key or re.search(r"invest|partner|principal|associate|chairman|founded|fellow|board|\?", desc, re.I)) and \
                    not ALUMNUS.search(desc) and \
                    not re.search(r"chief financial|chief operating|general counsel|talent|marketing|communications|"
                                  r"operations|recruit|events", desc, re.I):
                add(name, "people-page", sorted(years), "", "people page" + (f": {desc[:80]}" if desc else ""))
                stats["people-page"] += 1
            else:
                stats["people-page not investing"] += 1

    # deal panels on the archived company pages
    for f in sorted(P.wayback.glob("parsed/*.json")):
        for r in json.loads(f.read_text()):
            if not (r.get("content_ts") or "")[:4].isdigit():
                continue
            y = int(r["content_ts"][:4])
            for n, t in (r.get("partner_titles") or {}).items():
                if t and not investing(t):
                    continue
                add(n, "deal-panel", [y], "", t or "Investment Partner")
                stats["deal-panel"] += 1

    team = json.loads((P.site / "team-pages.json").read_text())["rows"]
    for t in team:
        if investing(t.get("title") or ""):
            add(t["name"], "site-team", [THIS_YEAR], "", t.get("title") or "")

    for s in list(people):
        if s in KPCB_CHINA:
            people.pop(s)
            continue
        if set(people[s]["sources"]) == {"deal-panel"}:
            people.pop(s)   # a deal credit alone is not tenure (old pages credit Khosla, Compton, Hearst)
            continue
        if s in LAST_YEAR:
            people[s]["years"] = {y for y in people[s]["years"] if y <= LAST_YEAR[s]}
            if not people[s]["years"]:
                people.pop(s)
    rows = []
    for s, r in sorted(people.items()):
        ys = sorted(r["years"])
        basis = "; ".join(f"{src} {min(yy)}-{max(yy)}" for src, yy in r["basis"].items())
        rows.append({"slug": s, "name": r["name"], "years_seen": ys, "first_seen": ys[0], "last_seen": ys[-1],
                     "snapshots": len(ys), "sources": r["sources"], "title": r["titles"].get(ys[-1], ""),
                     "basis": basis})
    write_atomic(OUT, json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(dict(stats))
    print(len(rows), "people ->", OUT.relative_to(ROOT))
    for r in rows:
        print(f"  {r['name']:28} {r['first_seen']}-{r['last_seen']} ({r['snapshots']}) {','.join(r['sources'])} | {r['title']}")


if __name__ == "__main__":
    main()
