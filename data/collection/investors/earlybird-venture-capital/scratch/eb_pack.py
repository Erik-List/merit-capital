#!/usr/bin/env python3
"""Evidence pack, one block per row: everything the run already holds on disk.

  the queue item (open needs, Form D rounds, what the prepared layers filled),
  the firm's live page (invested year, the list's stage label, status, HQ, deal team),
  the firm's archived pages (years listed, the fund tag, Current / Exited /
    Pre-Fund Investments by year, "investment since", exit route and date),
  the archived /team pages (which partner lists it under "Companies I work with"),
  the firm's own posts naming it (perspectives 2024-2026, press releases 2001-2010),
  EDGAR full-text hits naming it, and other investor books holding the company.

Usage: python3 eb_pack.py slug [slug ...] | --batch N [size] | --all-slugs
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

H = Path(__file__).resolve().parent
INV = H.parent
REPO = INV.parents[3]
SITE = INV / "sources/site"


def loose(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\((formerly|ex|former)[^)]*\)", " ", s)
    s = re.sub(r"\b(gmbh|ag|inc|ltd|limited|s\.?a\.?s?|ab|plc|corp|co|kg|se|oy|bv|llc|technologies|technology)\b\.?", " ", s)
    s = re.sub(r"\.(com|de|net|io|ai)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def load(p: Path, default):
    return json.loads(p.read_text()) if p.exists() else default


BASE = {r["slug"]: r for r in load(INV / "companies/base.json", [])}
EXC = load(INV / "companies/excluded.json", [])
RESOLVED = load(INV / "companies/resolved.json", {})
CLASS = load(INV / "companies/classification.json", {})
IDM = load(INV / "companies/identity-merges.json", {}).get("earlybird-venture-capital", {})
LIVE = {}
for f in ("companies-2026.json", "health-2026.json"):
    for r in load(SITE / f, {"rows": []})["rows"]:
        LIVE.setdefault(loose(r["name"]), r)
ARCH = load(INV / "sources/wayback/archive-evidence.json", {"companies": {}})["companies"]
ARCH_BY = collections.defaultdict(list)
for k, c in ARCH.items():
    for nm in c["names"]:
        ARCH_BY[loose(nm)].append(c)
TEAM = load(INV / "sources/wayback/team-years.json", {"detail": {}})["detail"]
PRESS = load(INV / "sources/web/press-archive.json", {"items": []})["items"]
IDX = {}
for raw in ("sources/site/raw/searchIndex.json", "sources/site/raw/health/searchIndex.json"):
    for k, v in load(INV / raw, {}).items():
        k = unquote(k)
        if k.startswith(("/perspectives/", "/insights/")):
            IDX[("health:" if "health" in raw else "") + k] = v
FTS = load(INV / "sources/edgar/fts-hits.json", {})
SURF = load(H / "graduation-surfaces.json", {})


def names_of(slug: str) -> list[str]:
    b = BASE.get(slug) or {}
    out = [b.get("name") or slug.replace("-", " ")]
    for m in IDM.get("merges", []):
        if m["canonical"] == slug:
            out += [d.replace("-", " ") for d in m["duplicates"]] + [m.get("name") or ""]
    for c in ARCH_BY.get(loose(out[0]), []):
        out += c["names"]
    seen, res = set(), []
    for n in out:
        k = loose(n)
        if k and k not in seen and len(k) > 1:
            seen.add(k)
            res.append(n)
    return res


def sentences(text: str, name: str, n: int = 2) -> list[str]:
    out = []
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9“\"])", text):
        if re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", s, re.I):
            out.append(s.strip()[:330])
        if len(out) >= n:
            break
    return out


_SIB = None


def siblings(names: list[str]) -> list[dict]:
    global _SIB
    if _SIB is None:
        _SIB = collections.defaultdict(list)
        for f in sorted((REPO / "data/collection/investors").glob("*/companies/base.csv")):
            inv = f.parts[-3]
            if inv == "earlybird-venture-capital":
                continue
            with open(f, newline="") as fh:
                for r in csv.DictReader(fh):
                    _SIB[loose(r["name"])].append((inv, r))
    out = []
    for n in names:
        for inv, r in _SIB.get(loose(n), []):
            out.append({"investor": inv, **{k: r.get(k) for k in (
                "name", "status", "valuation_range", "valuation_usd", "valuation_asof", "valuation_citation",
                "entry_stage", "entry_stage_source", "entry_stage_citation", "entry_date",
                "seed_to_a_graduation", "graduation_citation", "hq_city", "hq_country", "focus", "note")}})
    return out


def block(slug: str, item: dict | None = None, out=print) -> None:
    b = BASE.get(slug, {})
    nms = names_of(slug)
    name = nms[0]
    out(f"\n=== {slug} | {name} | first_seen {b.get('first_seen')} | tier {b.get('tier')} | also: {', '.join(nms[1:5])}")
    if item:
        out(f"  needs: {item.get('need')} | evidence_class: {item.get('evidence_class')}")
        for k in ("rounds", "formd_graduation", "formd_band_withheld", "partners_formd", "issuer_city",
                  "issuer_state", "year_inc", "former_unicorn", "acquirer", "known", "graduation_evidence"):
            if item.get(k):
                out(f"  item.{k}: {json.dumps(item[k], ensure_ascii=False)[:420]}")
    r = RESOLVED.get(slug) or {}
    pre = {k: v for k, v in r.items() if k not in ("slug", "name")}
    if pre:
        out(f"  PREPARED: {json.dumps(pre, ensure_ascii=False)[:420]}")
    for n in nms:
        lv = LIVE.get(loose(n))
        if lv:
            out(f"  LIVE ({lv.get('surface')}): invested {lv.get('invest_year')} | list stage '{lv.get('stage_site')}' | "
                f"{lv.get('status_site')} | HQ {lv.get('hq_site') or lv.get('location_list')} | founded {lv.get('founded')} | "
                f"deal team {lv.get('partners_site')} | {lv.get('categories')} | marker {lv.get('fund_marker')} | {lv.get('url')}")
            out(f"       {(lv.get('description') or '')[:260]}")
            break
    seen_arch = set()
    for n in nms:
        for c in ARCH_BY.get(loose(n), []):
            if id(c) in seen_arch:
                continue
            seen_arch.add(id(c))
            cl = c["claims"]
            tags = collections.Counter(x["desk_tag"] for x in cl if x.get("desk_tag"))
            stat = collections.OrderedDict()
            for x in cl:
                if x.get("status_tag"):
                    stat.setdefault(x["status_tag"], x["ts"][:4])
            iy = sorted({x["invest_year"] for x in cl if x.get("invest_year")})
            fd = sorted({x["founded"] for x in cl if x.get("founded")})
            hq = collections.Counter(x["hq"] for x in cl if x.get("hq")).most_common(2)
            ys = sorted(c["years"])
            out(f"  ARCHIVE '{c['name']}': listed {ys[0]}-{ys[-1]} | fund tag {dict(tags)} | status first seen {dict(stat)} | "
                f"invested {iy} | founded {fd} | HQ {[h for h, _ in hq]}")
            for x in cl:
                if x.get("exit_route") or x.get("recent_listed"):
                    out(f"       {x['surface']}: exit {x.get('exit_date')} {x.get('exit_kind') or ''} '{x.get('exit_route')}' recent-listed {x.get('recent_listed')} | {x['capture_url']}")
            d = next((x for x in reversed(cl) if x.get("description")), None)
            if d:
                out(f"       '{d['description'][:260]}' ({d['ts'][:8]})")
            m = next((x for x in cl if x.get("milestones")), None)
            if m:
                out(f"       milestones: {m['milestones'][:160]} | website {next((x.get('website') for x in cl if x.get('website')), None)}")
            first = cl[0] if cl else None
            if first:
                out(f"       first capture: {first['capture_url']}")
    who = []
    for person, d in TEAM.items():
        for y, comp in d["companies"].items():
            if any(re.search(rf"(?<![A-Za-z0-9]){re.escape(n)}(?![A-Za-z0-9])", comp, re.I) for n in nms if len(n) > 2):
                who.append(f"{person} ({'/'.join(sorted(set(d['team_tags'].values())))})")
                break
    if who:
        out(f"  TEAM lists it: {', '.join(sorted(set(who)))}")
    hits = 0
    for key, v in IDX.items():
        txt = " ".join(v.get("p", []))
        title = (v.get("h1") or [""])[-1]
        for n in nms:
            if len(n) > 2 and re.search(rf"(?<![A-Za-z0-9]){re.escape(n)}(?![A-Za-z0-9])", title + " " + txt, re.I):
                ss = sentences(txt, n) or [txt[:200]]
                dom = "https://health.earlybird.com" if key.startswith("health:") else "https://earlybird.com"
                out(f"  POST {dom}{key.replace('health:', '')} | {title[:90]}")
                out(f"       > {ss[0][:300]}")
                hits += 1
                break
        if hits >= 4:
            break
    ph = 0
    for p in PRESS:
        for n in nms:
            if len(n) > 3 and re.search(rf"(?<![A-Za-z0-9]){re.escape(n)}(?![A-Za-z0-9])", p["title"] + " " + p["text"], re.I):
                ss = sentences(p["text"], n) or [p["text"][:200]]
                out(f"  PRESS {p['date'] or '?'} [{p['lang']}/{p['kind']}/{p['id']}] {p['title'][:100]} | {p['capture_url']}")
                out(f"       > {ss[0][:300]}")
                ph += 1
                break
        if ph >= 5:
            break
    regs = FTS.get("registrants") or FTS.get("third_party") or []
    if isinstance(regs, dict):
        regs = list(regs.values())
    for reg in regs:
        rn = reg.get("name") or reg.get("registrant") or ""
        if any(loose(n) and loose(n) in loose(rn) for n in nms if len(loose(n)) > 3):
            out(f"  EDGAR-FTS registrant {rn}: forms {reg.get('forms')} first {reg.get('first_date')}")
            for sn in (reg.get("snippets") or reg.get("evidence") or [])[:2]:
                out(f"       > {json.dumps(sn, ensure_ascii=False)[:420]}")
    for s in siblings(nms)[:4]:
        out(f"  SIBLING {s['investor']}: '{s['name']}' status {s['status']} | {s['valuation_range']} {s['valuation_usd'] or ''} {s['valuation_asof'] or ''} | "
            f"stage {s['entry_stage']} ({s['entry_stage_source']}) {s['entry_date'] or ''} | grad {s['seed_to_a_graduation'] or ''} | "
            f"{s['hq_city']}, {s['hq_country']} | {s['focus']}")
        out(f"       note: {(s['note'] or '')[:300]}")
        for k in ("entry_stage_citation", "graduation_citation", "valuation_citation"):
            if s.get(k):
                out(f"       {k}: {s[k][:200]}")
    g = SURF.get(slug) or {}
    heads = []
    for svc, v in (g.get("surfaces") or {}).items():
        for i in v.get("items") or []:
            if i.get("names") or svc == "googlenews_firm":
                heads.append((bool(i.get("rounds") or i.get("amounts")), i.get("date", "")[:10], svc, i))
    heads.sort(key=lambda x: (not x[0], x[1]))
    for _has, d, svc, i in heads[:8]:
        out(f"  NEWS {d} {svc[:10]:10} {i.get('source', '')[:18]:18} {i.get('title', '')[:130]}")
    c = CLASS.get(slug)
    if c:
        out(f"  RECORDED: {json.dumps({k: v for k, v in c.items() if k not in ('funding_rounds',)}, ensure_ascii=False)[:500]}")


def main() -> None:
    args = sys.argv[1:]
    q = load(H / "queue/queue.json", [])
    by = {i["slug"]: i for i in q}
    if args and args[0] == "--batch":
        n = int(args[1])
        size = int(args[2]) if len(args) > 2 else 20
        slugs = [i["slug"] for i in q][n * size:(n + 1) * size]
    elif args and args[0] == "--all-slugs":
        print("\n".join(i["slug"] for i in q))
        return
    else:
        slugs = args
    for s in slugs:
        block(s, by.get(s))


if __name__ == "__main__":
    main()
