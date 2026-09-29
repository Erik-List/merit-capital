#!/usr/bin/env python3
"""Compact judge cards for ICONIQ Growth queue items: the queue item's own
evidence plus what the run's other sources say about the row: the live grid's
fields, the archived listing years (Common Crawl), the firm's own posts that
name the company, the EDGAR full-text sentences (S-1 holder tables and
investors' rights agreements name the ICONIQ vehicle and the series it holds),
the co-invest decode, the 13F window, the Form D rounds, the unicorn list and
the sibling books. Read-only. Adapted from the Coatue run's cards.py.
Usage: python3 .../scratch/cards.py <batch-file|all> [slug ...] [--full]
"""
import json, re, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]
FULL = "--full" in sys.argv


def norm(n):
    n = (n or "").lower(); n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"\b(inc|corp|corporation|llc|ltd|co|company|the|holdings?|group|technologies|technology|software|systems)\b\.?", " ", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def load(p, key=None, default=None):
    try:
        d = json.load(open(p))
    except (OSError, ValueError):
        return default if default is not None else {}
    return d.get(key, d) if key and isinstance(d, dict) else d


SITE = {norm(r["name"]): r for r in load(INV / "sources/site/portfolio-2026.json", "rows", [])}
POSTS = load(INV / "sources/site/posts.json", "posts", [])
SIB = load(INV / "scratch/siblings.json")
SURF = load(INV / "scratch/graduation-surfaces.json")
NEWSI = load(INV / "scratch/news-iconiq.json")
F13 = load(INV / "sources/edgar/13f-holdings.json", "issuers")
F13N = {norm(v["name"]): v for v in F13.values()}
DEC = {}
for d in load(INV / "sources/edgar/coinvest-decode.json", "series", []):
    for c in d.get("companies") or []:
        DEC.setdefault(norm(c), []).append(d)
ARCH = {}
for f in sorted((INV / "sources/wayback/parsed").glob("*.json")):
    for r in load(f, default=[]):
        ARCH.setdefault(norm(r["name"]), set()).add(f.stem)
WIKI = {}
for a in load(INV / "sources/web/wikipedia-insource.json", "articles", []):
    if a.get("sentences"):
        WIKI[norm(a["title"])] = (a["url"], a["sentences"][0])
FTS = {}
for r in load(INV / "sources/edgar/fts-hits.json", "registrants", []):
    if r.get("bucket") in ("third_party", "ownership_forms"):
        FTS.setdefault(norm(re.sub(r"\s+\(.*$", "", r["registrant"])), []).append(r)
UNI = load(ROOT / "data/collection/shared/unicorns/wikipedia.json")
S1 = {}
for reg, rows in load(INV / "sources/edgar/s1-iconiq.json").items():
    if reg.startswith("_"):
        continue
    S1.setdefault(norm(re.sub(r"\s+\(.*$", "", reg)), []).extend(rows)


def uni(name):
    k = re.sub(r"[^a-z0-9]+", "", name.lower())
    for sect in ("current", "former"):
        for kk, v in (UNI.get(sect) or {}).items():
            if re.sub(r"[^a-z0-9]+", "", kk) == k:
                return f"{sect}:{v.get('valuation_usd')}@{v.get('asof')}"
    return ""


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
            out.append((i.get("date") or "", i.get("source") or sname, t, i.get("link") or ("gid:" + (i.get("gid") or "")[:12])))
    out.sort()
    firm = [o for o in out if "iconiq" in o[2].lower()]
    rest = [o for o in out if o not in firm]
    pick = firm[:3] + rest[:2] + rest[-1:] if len(rest) > 3 else firm[:3] + rest
    return sorted(set(pick))[:5]


def fts_lines(name, n=3):
    out = []
    for r in FTS.get(norm(name), []):
        forms = ",".join(f"{k}:{v}" for k, v in list(r["forms"].items())[:5])
        out.append(f"   sec {r['registrant'][:40]} {r['first_date']}..{r['last_date']} [{forms}]")
        for sn in (r.get("snippets") or [])[: (6 if FULL else 2)]:
            for ctx in (sn.get("context") or [])[: (3 if FULL else 1)]:
                i = ctx.lower().find("iconiq")
                seg = ctx[max(0, i - 160): i + (420 if FULL else 260)] if i >= 0 else ctx[:300]
                out.append(f"      {sn['form']} {sn['date']} <{sn['url']}> …{re.sub(r'\s+', ' ', seg)}…")
    return out[: (40 if FULL else 7)]


def card(it):
    k = norm(it["name"])
    out = []
    s = SITE.get(k)
    site = (f"{'/'.join(s['categories'])}{' EXIT' if s['exit_site'] else ''} {(s.get('company_site') or '').replace('https://', '').replace('www.', '').strip('/')}"
            if s else "-")
    arch = ",".join(sorted(ARCH.get(k, [])))
    out.append(f"## {it['slug']} | {it['name']} | {it['evidence_class']} | site {site} | arch {arch or '-'} | need {','.join(x[:4] for x in it['need'])}"
               + (f" | pre {json.dumps(it['known'])[:180]}" if it.get("known") else ""))
    if s and s.get("description"):
        out.append(f"   desc {s['description'][:150]}")
    ev = []
    if it.get("edgar_forms"):
        ev.append(f"edgar {it['edgar_forms']} first {it.get('first_seen')} lineage {it.get('lineage')}")
    if it.get("partners_formd"):
        ev.append(f"formd {it['partners_formd']} @{it.get('issuer_city')},{it.get('issuer_state')} inc {it.get('year_inc')} rounds "
                  + ";".join(f"{(r.get('date') or r.get('quarter') or '')[:7]}:{int((r.get('amount') or r.get('offering_usd') or 0)) / 1e6:.0f}M" for r in (it.get('rounds') or [])[:6]))
    f = F13N.get(k)
    if f:
        ev.append(f"13F {f['first_period'][:7]}..{f['last_period'][:7]} max ${f['max_value_usd'] / 1e6:,.0f}M")
    u = uni(it["name"]) or (f"former:{it['former_unicorn']}" if it.get("former_unicorn") else "")
    if u:
        ev.append(f"unicorn {u}")
    if ev:
        out.append("   " + " | ".join(ev))
    for d in DEC.get(k, []):
        out.append(f"   decode {d['vehicle'][:70]} ({d['code']}) first Form D {d.get('first_filed')} sale {d.get('first_sale')} [{d['status']}] {d.get('basis', '')[:120]}")
    if it.get("formd_graduation"):
        out.append(f"   formd_graduation {json.dumps(it['formd_graduation'])[:230]}")
    full = re.escape(it["name"])
    for p in [p for p in POSTS if p.get("title") and re.search(r"\b" + full + r"\b", (p.get("title") or "") + " " + (p.get("text") or "")[:600], re.I)][:3]:
        out.append(f"   post {p.get('date', '')} {p['title'][:70]} <{p['url']}>")
    out += fts_lines(it["name"])
    s1 = S1.get(k) or []
    ranked = sorted({(x["date"], x["form"], x["url"], sen) for x in s1 for sen in x["sentences"]},
                    key=lambda t: (not re.search(r"Series [A-Z]", t[3]), t[0]))
    for d_, f_, u_, sen in ranked[: (12 if FULL else 4)]:
        i = sen.lower().find("iconiq")
        out.append(f"   s1 {f_} {d_} <{u_}> …{sen[max(0, i - 200): i + 330]}…")
    w = WIKI.get(k)
    if w and "iconiq" in w[1].lower():
        out.append(f"   wiki: {w[1][:170]}")
    for d, src, t, link in headlines(it["slug"]):
        out.append(f"   news {d[:7]} {t}" + (f" <{link}>" if link.startswith("http") else ""))
    ni = [i for i in (NEWSI.get(it["slug"]) or {}).get("items") or [] if i.get("names") and re.search(r"iconiq", i.get("title") or "", re.I)]
    ni += [i for i in (NEWSI.get(it["slug"]) or {}).get("items") or [] if i.get("names") and i.get("rounds") and i not in ni]
    for i in ni[: (12 if FULL else 5)]:
        out.append(f"   iq {(i.get('date') or '')[:7]} {re.sub(chr(10), ' ', i['title'])[:120]}")
    sibs = SIB.get(it["slug"]) or []
    if sibs:
        best = sorted(sibs, key=lambda x: (x["valuation_asof"] or "", x["valuation_usd"] or ""), reverse=True)[0]
        names = {x["name"] for x in sibs}
        v = f"${float(best['valuation_usd']) / 1e9:.2f}B@{best['valuation_asof']}" if best['valuation_usd'] else ""
        out.append(f"   sibs[{len(sibs)}] {sorted(names)[0]} | {'/'.join(sorted({x['status'] for x in sibs}))} {best['valuation_range']} {v} {best['investor']} | hq {sorted({(x['hq_city'] or '?') + ',' + x['hq_country'] for x in sibs})[:2]} | {sorted({x['focus'] for x in sibs if x['focus']})[:2]}")
    return "\n".join(out)


if __name__ == "__main__":
    arg = sys.argv[1]
    items = load(INV / "scratch/queue/queue.json", default=[]) if arg == "all" else json.load(open(arg))
    want = {a for a in sys.argv[2:] if not a.startswith("--")}
    for it in items:
        if want and it["slug"] not in want:
            continue
        print(card(it))
