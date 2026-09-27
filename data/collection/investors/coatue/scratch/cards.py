#!/usr/bin/env python3
"""Compact judge cards for one queue batch: the queue item's own evidence plus
what Coatue's other sources say about the row (the site's own fields, the
firm's posts, the 13F and registered-fund layers, Wikipedia, the full-text
sweep, the Form D rounds, the unicorn list and the sibling books). Read-only.
Usage: python3 .../scratch/cards.py <batch-file|all> [slug ...]"""
import json, re, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]
def norm(n):
    n = (n or "").lower(); n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"\b(inc|corp|corporation|llc|ltd|co|company|the|holdings?|group)\b\.?", " ", n)
    return re.sub(r"[^a-z0-9]+", "", n)
def load(p, key=None, default=None):
    try: d = json.load(open(p))
    except (OSError, ValueError): return default if default is not None else {}
    return d.get(key, d) if key and isinstance(d, dict) else d
SITE = {norm(r["name"]): r for r in load(INV / "sources/site/portfolio-2026.json", "rows", [])}
POSTS = load(INV / "sources/site/posts.json", "rows", [])
SIB = load(INV / "scratch/siblings.json")
SURF = load(INV / "scratch/graduation-surfaces.json")
F13 = load(INV / "sources/edgar/13f-holdings.json", "issuers")
F13N = {norm(v["name"]): v for v in F13.values()}
RF = load(INV / "sources/edgar/registered-fund-holdings.json", "restricted")
RFN = {norm(re.sub(r"(series|pfd|preferred|class|global|group holdings).*", "", v["name"], flags=re.I)): v for v in RF.values()}
WIKI = {}
for a in load(INV / "sources/web/wikipedia-insource.json", "articles", []):
    if a.get("sentences"): WIKI[norm(a["title"])] = (a["url"], a["sentences"][0])
FTS = {}
fts = load(INV / "sources/edgar/fts-hits.json")
for r in (fts.get("registrants") or fts.get("third_party") or []) if isinstance(fts, dict) else []:
    FTS[norm(r.get("name") or r.get("registrant") or "")] = r
UNI = load(ROOT / "data/collection/shared/unicorns/wikipedia.json")
def uni(name):
    k = re.sub(r"[^a-z0-9]+", "", name.lower())
    for sect in ("current", "former"):
        for kk, v in (UNI.get(sect) or {}).items():
            if re.sub(r"[^a-z0-9]+", "", kk) == k:
                return f"{sect}:{v.get('valuation_usd')}@{v.get('asof')}"
    return ""
def headlines(slug, k=5):
    e = SURF.get(slug) or {}; seen, out = set(), []
    for sname in ("googlenews_firm", "googlenews", "techcrunch", "crunchbase_news"):
        for i in ((e.get("surfaces") or {}).get(sname) or {}).get("items") or []:
            if not i.get("names") or not i.get("rounds"): continue
            if re.search(r"getlatka|tracxn|crunchbase$|pitchbook|cbinsights|dealroom", (i.get("source") or "").lower().replace(" ", "")): continue
            t = re.sub(r"\s+", " ", i.get("title") or "")
            t = re.sub(r" - [^-]{2,40}$", "", t)[:88]
            key = (i.get("date"), t[:40])
            if key in seen: continue
            seen.add(key); out.append((i.get("date") or "", i.get("source") or sname, t, i.get("link") or ("gid:" + (i.get("gid") or "")[:12])))
    out.sort()
    firm = [o for o in out if "oatue" in o[2]]
    rest = [o for o in out if o not in firm]
    pick = firm[:2] + rest[:2] + rest[-1:] if len(rest) > 3 else firm[:2] + rest
    return sorted(set(pick))[:4]
def card(it):
    k = norm(it["name"]); out = []
    s = SITE.get(k)
    site = f"{s['initial_investment']}/{s['status_site']} {(s.get('company_site') or '').replace('https://','').replace('www.','').strip('/')}" if s else "-"
    out.append(f"## {it['slug']} | {it['name']} | {it['evidence_class']} | site {site} | need {','.join(x[:4] for x in it['need'])}" + (f" | pre {json.dumps(it['known'])[:160]}" if it.get("known") else ""))
    ev = []
    if it.get("edgar_forms"): ev.append(f"edgar {it['edgar_forms']} first {it.get('first_seen')}")
    if it.get("partners_formd"): ev.append(f"formd {it['partners_formd']} @{it.get('issuer_city')},{it.get('issuer_state')} inc {it.get('year_inc')} rounds " + ";".join(f"{(r.get('date') or r.get('quarter') or '')[:7]}:{int((r.get('amount') or r.get('offering_usd') or 0))/1e6:.0f}M" for r in (it.get('rounds') or [])[:6]))
    f = F13N.get(k)
    if f: ev.append(f"13F {f['first_period'][:7]}..{f['last_period'][:7]} max ${f['max_value_usd']/1e6:,.0f}M")
    r = RFN.get(k)
    if r: ev.append(f"N-PORT restricted {r['first_period'][:7]}.. fair ${r['last_value_usd']/1e6:,.0f}M")
    u = uni(it["name"]) or (f"former:{it['former_unicorn']}" if it.get("former_unicorn") else "")
    if u: ev.append(f"unicorn {u}")
    if ev: out.append("   " + " | ".join(ev))
    if it.get("formd_graduation"): out.append(f"   formd_graduation {json.dumps(it['formd_graduation'])[:230]}")
    full = re.escape(it["name"])
    for p in [p for p in POSTS if p.get("title") and re.search(r"\b" + full + r"\b", p["title"] or "")][:2]:
        out.append(f"   post {str(p['date'])[:10]} {p['title'][:60]} <{p['url'].replace('https://www.coatue.com','')}>")
    w = WIKI.get(k)
    if w and "oatue" in w[1]: out.append(f"   wiki: {w[1][:170]}")
    for d, src, t, link in headlines(it["slug"]):
        out.append(f"   news {d[:7]} {t}" + (f" <{link}>" if link.startswith("http") else ""))
    sibs = SIB.get(it["slug"]) or []
    if sibs:
        best = sorted(sibs, key=lambda x: (x["valuation_asof"] or "", x["valuation_usd"] or ""), reverse=True)[0]
        names = {x["name"] for x in sibs}
        v = f"${float(best['valuation_usd'])/1e9:.2f}B@{best['valuation_asof']}" if best['valuation_usd'] else ""
        out.append(f"   sibs[{len(sibs)}] {sorted(names)[0]} | {'/'.join(sorted({x['status'] for x in sibs}))} {best['valuation_range']} {v} {best['investor']} | hq {sorted({(x['hq_city'] or '?') + ',' + x['hq_country'] for x in sibs})[:2]} | {sorted({x['focus'] for x in sibs if x['focus']})[:2]}")
    return "\n".join(out)
if __name__ == "__main__":
    arg = sys.argv[1]
    items = load(INV / "scratch/queue/queue.json", default=[]) if arg == "all" else json.load(open(arg))
    want = set(sys.argv[2:])
    for it in items:
        if want and it["slug"] not in want: continue
        print(card(it))
