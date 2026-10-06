#!/usr/bin/env python3
"""Parse the Internet Archive captures of indexventures.com 1999-2002 (fetched by ia-pass.py, cached under
data/filings/index-ventures/ia-cache) into sources/wayback/parsed/<year>.json rows of era `ia`, and the firm's own
claims on those pages into sources/wayback/archive-facts.json under the key `ia`.

Three static pages (portfolio.html, portf_sect.html, portf_geo.html, 1999-2002): one table row per company with the
name (logo ALT text, or bold text in 1999-2000), city and country, listing status and, on portfolio.html, a one-line
description. portfolio.html has two groups, headed by images: team_index.gif / team-iv.jpg (the funds' portfolio)
and team_prior.gif (prior investments of the team, made before the first fund). portf_sect.html groups by sector.
The Nov 2002 database pages (/cgi-local/ivw_port_detail.cgi?spgid=N) carry the sector's company list in a side
menu, where '*' "Denotes prior investments of Index Partners" (a partner's deals from an earlier firm).

Names are emitted as the firm rendered them, cleaned of legal suffixes; ALIAS maps the few whose later rendering on
the firm's own lists differs, so one company stays one row (renames proper are in companies/identity-merges.json)."""
import html as H, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CACHE = HERE.parents[4] / "data" / "filings" / "index-ventures" / "ia-cache"
PARSED = ROOT / "sources" / "wayback" / "parsed"
FACTS = ROOT / "sources" / "wayback" / "archive-facts.json"
MANIFEST = ROOT / "sources" / "wayback" / "manifest.json"
res = json.loads((HERE / "ia-pass.json").read_text())
ALIAS = {"Ciao.com": "Ciao", "MediaSurface": "Mediasurface", "Neo Vista Software": "Neovista", "7TM Pharma": "7TM",
         "The Fantastic Corporation": "Fantastic", "CommQuest Technologies": "CommQuest", "Ingenium Pharmaceuticals": "Ingenium",
         "ParAllele BioScience": "ParAllele Bioscience", "DirectMedica": "Directmedica", "MediCentrix": "Medicentrix",
         "digiquant": "Digiquant", "Evolve": "Evolve Software", "Listen": "Listen.com", "Structural Genomix": "Structural GenomiX",
         "Pulsent Corp.": "Pulsent", "Addex Pharmaceuticals": "Addex Pharma", "Respond": "Respond.com"}
# the same company under the name the firm's later lists carry (the old name is kept as the fact `formerly`)
RENAMED = {"Belle systems": "Digiquant", "ControlMed": "Medicentrix", "Structural GenomiX": "SGX Pharma", "GlobeSpanVirata": "Virata",
           "Flutter": "Betfair"}
SUFFIX = re.compile(r",?\s+(Inc\.?|Ltd\.?|AG|A/S|Corp\.?)$")
slug_of = lambda n: re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")
clean = lambda s: re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()
def canon(name):
    n = clean(name).strip(" /")
    while SUFFIX.search(n): n = SUFFIX.sub("", n).strip()
    return ALIAS.get(n, n)

def tokens(body):
    b = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    out = []
    for m in re.finditer(r'<img[^>]*src="images/(team_index\.gif|team-iv\.jpg|team_prior\.gif)"|<img[^>]*ALT="([^"]+)"[^>]*>|'
                         r'<font size=2 face=arial>(.*?)</font>', b, flags=re.S | re.I):
        g, alt, f2 = m.groups()
        if g: out.append(("G", "team_prior" if "prior" in g else "fund"))
        elif alt: out.append(("ALT", alt.strip()))
        else:
            t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " / ", f2))).strip()
            if t: out.append(("F", t))
    return out

rows_by_year, facts = {}, {}
STARRED = {}
def fact(slug, field, value, cap, ts):
    if value in (None, "", []): return
    slot = facts.setdefault(slug, {}).setdefault(field, {})
    v = json.dumps(value, ensure_ascii=False, sort_keys=True)
    if v not in slot or ts < slot[v]["ts"]:
        slot[v] = {"value": value, "ts": ts, "capture_url": cap}
def emit(name, ts, url, path, **f):
    name = canon(name)
    if name in RENAMED:
        f["formerly"] = name; name = RENAMED[name]
    slug = slug_of(name)
    if not slug or slug in ("index-ventures",): return
    cap = f"https://web.archive.org/web/{ts}/{url}"
    rows_by_year.setdefault(int(ts[:4]), {}).setdefault((slug, path), {"name": name, "slug": slug, "path": path, "snapshot_ts": ts,
        "capture_url": cap, "surface": "wayback", "era": "ia", **({"group": f["group"]} if f.get("group") else {})})
    fact(slug, "name", name, cap, ts)
    for k, v in f.items(): fact(slug, k, v, cap, ts)

STATUS = re.compile(r"^(Private|Acquired by|Merged with|Nasdaq|Neuer Markt|Oslo|Copenhagen|Milan|Frankfurt|LSE|Zurich|SWX)", re.I)
for key, v in sorted(res.items()):
    if key.startswith("cdx:") or v.get("status") != "ok": continue
    ts, url = key.split(" ", 1)
    body = (CACHE / v["cache"]).read_text(errors="replace")
    path = re.sub(r"https?://(www\.)?indexventures\.com(:80)?", "", url)
    if re.search(r"/(portfolio|portf_sect|portf_geo)\.html$", path):
        toks = tokens(body)
        heads_are_names = not any(t == "ALT" for t, _ in toks)        # 1999-2000: names are bold text, not logos
        group = sector = None; cur = None; items = []
        for kind, t in toks:
            if kind == "G": group = t; cur = None; continue
            wrapped = kind == "F" and t.startswith("/") and t.endswith("/")
            if kind == "ALT" or (wrapped and heads_are_names):
                if cur and cur["cells"] and cur["cells"][-1].lower().startswith("acquired by") and kind == "ALT":
                    continue                                          # the acquirer's logo beside 'Acquired by X'
                cur = {"name": t.strip(" /"), "group": group, "sector": sector, "cells": []}; items.append(cur)
            elif wrapped:
                sector = t.strip(" /") or sector; cur = None
            elif cur is not None:
                cur["cells"].append(t)
        for it in items:
            cells = it["cells"]
            if not cells: continue
            loc = cells[0]; rest = cells[1:]
            desc = rest[-1] if path.endswith("portfolio.html") and len(rest) >= 2 and not STATUS.match(rest[-1]) else None
            status = [c for c in rest if c != desc]
            main = path.endswith("portfolio.html")           # cell order is only fixed on the main list
            emit(it["name"], ts, url, path.split("?")[0], group=it["group"], sector_1999_2002=it["sector"] if "portf_sect" in path else None,
                 hq=loc.replace(" / ", ", ") if main else None, status_site="; ".join(status) if main else None, description=desc)
    elif "ivw_port_detail.cgi?spgid=" in path:
        b = re.sub(r"<!--.*?-->|<script.*?</script>", "", body, flags=re.S)
        lines = [l.strip() for l in H.unescape(re.sub(r"<[^>]+>", "\n", b)).split("\n") if l.strip()]
        if "Life Sciences" not in lines: continue
        rest = lines[lines.index("Life Sciences") + 1:]
        SUB = {"Drug Discovery & Enabling Platforms", "Healthcare Infrastructure", "Information Technology"}
        life = bool(SUB & set(rest[:3]))
        lst = []
        for l in rest:
            if l in SUB: continue
            if l.rstrip("*") in [x.rstrip("*") for x in lst] or l.startswith("Index Ventures Contact"): break
            lst.append(l)
        detail = rest[len([x for x in rest[:3] if x in SUB]) + len(lst):]
        tab = [a for a in ("Applications & Services", "Communications", "Components & EDA", "Enterprise Infrastructure") if a in lines]
        for l in lst:
            star = l.endswith("*"); disp = l.rstrip("*").strip()
            if star:                  # '* Denotes prior investments of Index Partners': partner-carried (Erik, 2026-09-17), a trap in config, never a row
                STARRED.setdefault(disp, f"https://web.archive.org/web/{ts}/{url}"); continue
            tags = re.findall(r"\(([^()]*)\)", disp); nm = re.sub(r"\s*\([^()]*\)", "", disp).strip()
            if nm == "Flutter" and tags: nm, tags = "Betfair", ["formerly Flutter"]
            emit(nm, ts, url, "/cgi-local/ivw_port_detail.cgi", desk="life" if life else "tech", list_tag="; ".join(tags) or None,
                 prior_partner=True if star else None)
        if detail and not detail[0].endswith("*"):
            nm = re.sub(r"\s*\([^()]*\)", "", detail[0].rstrip("*")).strip()
            if nm == "Flutter": nm = "Betfair"
            contacts = []
            if "Index Ventures Contact(s):" in detail:
                i = detail.index("Index Ventures Contact(s):")
                for c in detail[i + 1:i + 4]:
                    if re.fullmatch(r"[A-Z][a-zé�]+(?: [A-Z][a-z]+)* [A-Z][A-Za-z]+", c) and not re.search(r"\d", c): contacts.append(c.replace("�", "e"))
                    else: break
            emit(nm, ts, url, "/cgi-local/ivw_port_detail.cgi", description=detail[1] if len(detail) > 1 else None, partners=contacts or None)

PARSED.mkdir(parents=True, exist_ok=True)
for year, rows in rows_by_year.items():
    f = PARSED / f"{year}.json"
    cur = json.loads(f.read_text()) if f.exists() else []
    keep = {(r["slug"], r["path"]): r for r in cur if r.get("era") != "ia"}
    for k, r in rows.items(): keep.setdefault(k, r)
    f.write_text(json.dumps(sorted(keep.values(), key=lambda r: (r["path"], r["slug"])), indent=1, ensure_ascii=False) + "\n")
man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
man["ia"] = {str(y): len(r) for y, r in sorted(rows_by_year.items())}
MANIFEST.write_text(json.dumps(man, indent=1) + "\n")
allf = json.loads(FACTS.read_text())
allf["ia"] = {s: {k: sorted(v.values(), key=lambda e: e["ts"]) for k, v in fl.items()} for s, fl in sorted(facts.items())}
FACTS.write_text(json.dumps(allf, indent=1, ensure_ascii=False) + "\n")
print({y: len(r) for y, r in sorted(rows_by_year.items())}, "starred, not emitted:", STARRED)
allf["ia_starred"] = STARRED; FACTS.write_text(json.dumps(allf, indent=1, ensure_ascii=False) + "\n")
for s, fl in sorted(allf["ia"].items()):
    g = lambda k: "; ".join(str(e["value"]) for e in fl.get(k, []))
    print(f"  {s:26s} grp={g('group'):16s} sec={g('sector_1999_2002')[:34]:34s} desk={g('desk'):5s} star={g('prior_partner'):5s} hq={g('hq')[:26]:26s} st={g('status_site')[:40]} | {g('partners')}")
