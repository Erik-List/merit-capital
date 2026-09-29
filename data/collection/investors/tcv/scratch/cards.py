#!/usr/bin/env python3
"""Compact judge cards for TCV queue items (PRO-169; adapted from ICONIQ's and
Coatue's cards.py): the queue item's own evidence plus what the run's other
sources say about the row: the live surfaces (compliance list legal name,
partnerships grid status, location, sectors, deal team), the archived list
years and surfaces, the 2018-2023 grid's DEAL TYPE (minority / majority /
public), the firm's own news titles, the EDGAR full-text sentences, the 13F
window, the Form D rounds, the unicorn list and the sibling books. Read-only.
Usage: python3 .../scratch/cards.py <batch-file|all> [slug ...] [--full]
"""
import json
import re
import sys
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]
FULL = "--full" in sys.argv


def norm(n):
    n = (n or "").lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"\b(inc|corp|corporation|llc|ltd|limited|co|company|the|holdings?|group|technologies|technology|"
               r"software|systems|plc|sa|se|ag|gmbh|bv|oy)\b\.?", " ", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def load(p, key=None, default=None):
    try:
        d = json.load(open(p))
    except (OSError, ValueError):
        return default if default is not None else {}
    return d.get(key, d) if key and isinstance(d, dict) else d


SITE = {}
for r in load(INV / "sources/site/portfolio-2026.json", "rows", []):
    for n in [r["name"], r.get("legal_name") or ""] + (r.get("aliases") or []):
        if n:
            SITE.setdefault(norm(n), r)
ARCH, GRID = {}, {}
for f in sorted((INV / "sources/wayback/parsed").glob("*.json")):
    for r in load(f, default=[]):
        for n in {r.get("name") or "", r.get("name_listed") or ""}:
            if not n:
                continue
            ARCH.setdefault(norm(n), {}).setdefault(r["surface"], set()).add(f.stem)
            if r.get("surface") == "grid2017" and r.get("deal_type"):
                GRID.setdefault(norm(n), set()).add(r["deal_type"])
            if r.get("note") and r["surface"] in ("idx2007", "wp2013"):
                ARCH[norm(n)].setdefault("_note", set()).add(r["note"][:80])
NEWS = load(INV / "sources/site/news-archive.json", "rows", [])
SIB = load(INV / "scratch/siblings.json")
SURF = load(INV / "scratch/graduation-surfaces.json")
NEWST = load(INV / "scratch/news-tcv.json")
F13 = load(INV / "sources/edgar/13f-holdings.json", "issuers")
F13N = {norm(v["name"]): v for v in F13.values()}
WIKI = {}
for a in load(INV / "sources/web/wikipedia-insource.json", "articles", []):
    if a.get("sentences"):
        WIKI[norm(a["title"])] = (a["url"], a["sentences"][0])
FTS = {}
for r in load(INV / "sources/edgar/fts-hits.json", "registrants", []):
    if r.get("bucket") in ("third_party", "ownership_forms"):
        FTS.setdefault(norm(re.sub(r"\s+\(.*$", "", r["registrant"])), []).append(r)
UNI = load(ROOT / "data/collection/shared/unicorns/wikipedia.json")


def uni(name):
    k = re.sub(r"[^a-z0-9]+", "", name.lower())
    for sect in ("current", "former"):
        for kk, v in (UNI.get(sect) or {}).items():
            if re.sub(r"[^a-z0-9]+", "", kk) == k:
                return f"{sect}:{v.get('valuation_usd')}@{v.get('asof')}"
    return ""


def news_for(name, aliases):
    toks = {re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-") for n in [name] + list(aliases) if n}
    toks = {t for t in toks if len(t) >= 3}
    out = []
    for r in NEWS:
        s = "-" + r["slug"].lower() + "-"
        if any(f"-{t}-" in s or s.startswith(f"-{t}") for t in toks):
            out.append(r)
    return out


def headlines(slug, k=5):
    e = SURF.get(slug) or {}
    seen, out = set(), []
    for sname in ("googlenews_firm", "googlenews", "techcrunch", "crunchbase_news"):
        for i in ((e.get("surfaces") or {}).get(sname) or {}).get("items") or []:
            if not i.get("names") or not i.get("rounds"):
                continue
            if re.search(r"getlatka|tracxn|crunchbase$|pitchbook|cbinsights|dealroom", (i.get("source") or "").lower().replace(" ", "")):
                continue
            t = re.sub(r"\s+", " ", i.get("title") or "")
            t = re.sub(r" - [^-]{2,40}$", "", t)[:88]
            key = (i.get("date"), t[:40])
            if key in seen:
                continue
            seen.add(key)
            out.append((i.get("date") or "", i.get("source") or sname, t, i.get("link") or ""))
    out.sort()
    firm = [o for o in out if re.search(r"\btcv\b|technology crossover", o[2].lower())]
    rest = [o for o in out if o not in firm]
    return sorted(set(firm[:3] + rest[:2] + rest[-1:]))[:k]


def fts_lines(name, n=3):
    out = []
    for r in FTS.get(norm(name), []):
        forms = ",".join(f"{k}:{v}" for k, v in list(r["forms"].items())[:5])
        out.append(f"   sec {r['registrant'][:40]} {r['first_date']}..{r['last_date']} [{forms}]")
        for sn in (r.get("snippets") or [])[: (6 if FULL else 2)]:
            for ctx in (sn.get("context") or [])[: (3 if FULL else 1)]:
                m = re.search(r"(?i)technology crossover|\bTCV\b", ctx)
                i = m.start() if m else -1
                seg = ctx[max(0, i - 160): i + (420 if FULL else 240)] if i >= 0 else ctx[:280]
                out.append(f"      {sn['form']} {sn['date']} <{sn['url']}> …{re.sub(r'\s+', ' ', seg)}…")
    return out[: (40 if FULL else 6)]


def card(it):
    k = norm(it["name"])
    out = []
    s = SITE.get(k)
    lists = "/".join(s["lists"]) if s else "-"
    arch = ARCH.get(k, {})
    arch_s = " ".join(f"{sf}:{min(ys)}-{max(ys)}" for sf, ys in sorted(arch.items()) if not sf.startswith("_"))
    gd = "/".join(sorted(GRID.get(k, []))) or "-"
    out.append(f"## {it['slug']} | {it['name']} | {it['evidence_class']} | lists {lists} | grid-deal {gd} | need {','.join(x[:4] for x in it['need'])}"
               + (f" | pre {json.dumps(it['known'])[:160]}" if it.get("known") else ""))
    if s:
        bits = [f"legal '{s.get('legal_name') or '-'}'"]
        if s.get("list_note"):
            bits.append(s["list_note"])
        if s.get("status_site"):
            bits.append(f"grid {s['status_site']}")
        if s.get("location"):
            bits.append(s["location"].strip())
        if s.get("sectors"):
            bits.append("/".join(s["sectors"]))
        if s.get("year_founded"):
            bits.append(f"founded {s['year_founded']}")
        if s.get("partners"):
            bits.append("team " + ", ".join(s["partners"][:4]))
        if s.get("domain") or s.get("company_site"):
            bits.append((s.get("domain") or s.get("company_site") or "").replace("https://", "").replace("www.", "").strip("/"))
        out.append("   " + " | ".join(bits))
        if s.get("description"):
            out.append(f"   desc {s['description'][:150]}")
    if arch_s:
        out.append(f"   arch {arch_s}" + (f" | {'; '.join(sorted(arch.get('_note', [])))[:120]}" if arch.get("_note") else ""))
    ev = []
    if it.get("edgar_forms"):
        ev.append(f"edgar {it['edgar_forms']} first {it.get('first_seen')} lineage {it.get('lineage')}")
    if it.get("partners_formd"):
        ev.append(f"formd {it['partners_formd']} @{it.get('issuer_city')},{it.get('issuer_state')} inc {it.get('year_inc')} rounds "
                  + ";".join(f"{(r.get('date') or r.get('quarter') or '')[:7]}:{int((r.get('amount') or r.get('offering_usd') or 0)) / 1e6:.0f}M" for r in (it.get('rounds') or [])[:6]))
    f = F13N.get(k)
    if f:
        ev.append(f"13F {f['first_period'][:7]}..{f['last_period'][:7]} max ${(f.get('max_value_usd') or 0) / 1e6:,.0f}M")
    u = uni(it["name"]) or (f"former:{it['former_unicorn']}" if it.get("former_unicorn") else "")
    if u:
        ev.append(f"unicorn {u}")
    if ev:
        out.append("   " + " | ".join(ev))
    if it.get("formd_graduation"):
        out.append(f"   formd_graduation {json.dumps(it['formd_graduation'])[:230]}")
    for r in news_for(it["name"], (s or {}).get("aliases") or [])[: (8 if FULL else 3)]:
        out.append(f"   tcvnews {r['first_capture'][:8]} {r['slug'][:110]}" + (f" | {r['body_text'][:260]}" if FULL and r.get("body_text") else ""))
    out += fts_lines(it["name"])
    w = WIKI.get(k)
    if w and re.search(r"(?i)technology crossover|\bTCV\b", w[1]):
        out.append(f"   wiki: {w[1][:170]}")
    for d, src, t, link in headlines(it["slug"]):
        out.append(f"   news {d[:7]} {t}" + (f" <{link}>" if link.startswith("http") else ""))
    nt = [i for i in (NEWST.get(it["slug"]) or {}).get("items") or [] if i.get("names")]
    nt.sort(key=lambda i: (not re.search(r"(?i)\btcv\b|technology crossover", i.get("title") or ""), i.get("date") or ""))
    for i in nt[: (10 if FULL else 4)]:
        out.append(f"   tq {(i.get('date') or '')[:7]} {re.sub(chr(10), ' ', i.get('title') or '')[:125]}")
    sibs = SIB.get(it["slug"]) or []
    if sibs:
        best = sorted(sibs, key=lambda x: (x["valuation_asof"] or "", x["valuation_usd"] or ""), reverse=True)[0]
        names = {x["name"] for x in sibs}
        v = f"${float(best['valuation_usd']) / 1e9:.2f}B@{best['valuation_asof']}" if best['valuation_usd'] else ""
        out.append(f"   sibs[{len(sibs)}] {sorted(names)[0]} | {'/'.join(sorted({x['status'] for x in sibs}))} {best['valuation_range']} {v} {best['investor']} | hq {sorted({(x['hq_city'] or '?') + ',' + x['hq_country'] for x in sibs})[:2]} | {sorted({x['focus'] for x in sibs if x['focus']})[:2]} | es {sorted({x.get('entry_stage') or '' for x in sibs})[:3]}")
    return "\n".join(out)


if __name__ == "__main__":
    arg = sys.argv[1]
    items = load(INV / "scratch/queue/queue.json", default=[]) if arg == "all" else json.load(open(arg))
    want = {a for a in sys.argv[2:] if not a.startswith("--")}
    for it in items:
        if want and it["slug"] not in want:
            continue
        print(card(it))
