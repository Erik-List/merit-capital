#!/usr/bin/env python3
"""One evidence view per base row for the Tiger Global judges (PRO-167), adapted from
the Sutter Hill / BCV evidence packs to this firm's sources:

  press   the recall addition's own basis (headline, the publisher's sentence naming Tiger,
          citation), every headline naming the company with Tiger (press sweep and the
          per-company query in cand-news.json), with gids so judge_lib.NEWS can cite them
  sec     full-text triage lines (prospectus holder tables, IRA signatories, merger filings):
          class, named Tiger vehicles, desk, URL
  edgar   Tiger's own 13D/G and Form 3/4 on the company (base row fields)
  13f     the first and last quarter the adviser's 13F lists the company (dates a listing)
  formd   roster persons on the company's Form Ds, with role and quarter
  wiki    Wikipedia sentences naming Tiger
  param   model-memory recall lines (a LEAD, never evidence)
  sib     sibling books' rows for the same company (scratch/siblings.json)

Output: scratch/evidence-pack.json {slug: {...}} and scratch/news-extra-pack.json
{slug: [headline items]} so judge_lib.NEWS(slug, substring) resolves the pack's headlines.
"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
INV = HERE.parent
sys.path.insert(0, str(HERE.parents[3].parent / "scripts"))
from paths import write_atomic  # noqa: E402

GENERIC = r"\b(inc|incorporated|ltd|limited|pvt|private|gmbh|ab|sa|s\.a|plc|llc|l\.l\.c|corp|corporation|co|company|group|holdings?|technologies|technology|tech|labs|the|app|com|ai|india|global|international|pte|bv|nv|ag|oy|as)\b\.?"


def loose(s):
    s = (s or "").lower().replace("&", " and ")
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\.(com|io|ai|co|in|app|net|org)\b", " ", s)
    s = re.sub(GENERIC, " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def J(p, default):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else default


base = J(INV / "companies/base.json", [])
cands = J(HERE / "recall/candidates.json", {})
cnews = J(HERE / "cand-news.json", {})
bnews = J(HERE / "bing-news.json", {})
snips = J(HERE / "snippets.json", {})
decoded = {}
for f in sorted(HERE.glob("news-decoded*.json")):
    decoded.update(J(f, {}))
f13 = J(INV / "sources/edgar/13f-holdings.json", {}).get("issuers", {})
f13k = {}
for k, v in f13.items():
    f13k.setdefault(loose(v["name"]), v)
fsweep = J(INV / "sources/edgar/formd-sweep.json", {})
sib = J(HERE / "siblings.json", {})
extra = J(HERE / "recall/cand-extra.json", {})   # key -> alias keys merged by hand

pack, news_pack = {}, {}
for r in base:
    s = r["slug"]
    keys = {loose(r["name"])} | set(extra.get(loose(r["name"]), []))
    e = {}
    c = {}
    for k in keys:
        if k in cands:
            c = cands[k]
            break
    # press: recall basis first
    notes = r.get("notes") or ""
    if "recall addition:" in notes:
        e["recall_basis"] = notes[notes.index("recall addition:"):][:700]
    items = []
    nm = re.sub(r"\s*\(.*?\)", "", r["name"]).split(",")[0].strip()
    nm = re.sub(r"(?i)\s+(inc|corp|corporation|ltd|limited|llc|plc|n\.v|s\.a|holdings?|group)\.?$", "", nm).strip()
    alias = [nm] + [cands[k]["name"] for k in keys if k in cands] + list((c.get("names") or {}).keys())
    def names_row(t):
        return any(a and len(a) > 2 and re.search(r"(?<![\w])" + re.escape(a) + r"(?![\w])", t, re.I) for a in alias)
    for k in keys:
        for it in (cnews.get(k) or {}).get("items", []):
            if "tiger" in it["title"].lower() and names_row(it["title"]):
                items.append({**it, "via": "cand-news"})
    for k in keys:
        for it in (bnews.get(k) or {}).get("items", []):
            if names_row(it["title"]) or "tiger" in (it.get("desc") or "").lower():
                items.append({"date": it["date"], "title": it["title"], "source": it.get("source"),
                              "gid": None, "url": it["url"], "via": "bing"})
    for it in c.get("press_T", []) + c.get("press_F", []):
        items.append({"date": it["date"], "title": it["title"], "source": it.get("source"), "gid": it["gid"],
                      "via": "press-sweep"})
    seen, uniq = set(), []
    for it in sorted(items, key=lambda i: i.get("date") or ""):
        ident = it.get("gid") or it.get("url")
        if ident in seen:
            continue
        seen.add(ident)
        uniq.append(it)
    if uniq:
        news_pack[s] = [{k: it.get(k) for k in ("date", "title", "source", "gid", "url")} for it in uniq]
        lines = []
        for it in uniq[:10]:
            u = it.get("url") or decoded.get(it.get("gid"))
            sn = (snips.get(u) or {}).get("sentences") if u else None
            lines.append(f"{it.get('date')} | {(it.get('source') or '')[:22]} | {it['title'][:150]}"
                         + (f" || URL {u}" if u else "") + (f" || SAYS: {' / '.join(sn)[:400]}" if sn else ""))
        e["press"] = lines
    if c.get("fts"):
        e["sec"] = [f"{x['class']} | {x.get('company')} | vehicles={x.get('vehicles')} desk={x.get('desk')} | "
                    f"{x.get('first_private_evidence_date')} | {x.get('basis')[:250]} | {x.get('url')}" for x in c["fts"]][:4]
    if r.get("edgar_forms"):
        e["edgar"] = f"{r.get('edgar_forms')} {r.get('edgar_span')} cik={r.get('edgar_cik')} links={(r.get('edgar_links') or '')[:200]}"
    for k in keys:
        if k in f13k:
            v = f13k[k]
            e["13f"] = f"{v['name']}: 13F {v['first_period']} to {v['last_period']}, max ${v['max_value_usd']/1e6:,.0f}M"
            break
    accs = [x.strip() for x in (r.get("formd_accessions") or "").split(";") if x.strip()]
    ppl = []
    for acc in accs:
        rec = fsweep.get(acc) or {}
        for p in rec.get("persons", []):
            ppl.append(f"{p['person']} ({p['relationship']}, {p['quarter'][:6]}) on {rec.get('issuer')} "
                       f"[{rec.get('city')}, {rec.get('state')}; sold ${rec.get('total_sold') or '?'}]")
    if ppl:
        e["formd"] = sorted(set(ppl))[:6]
    if c.get("wiki"):
        e["wiki"] = [f"{w['title']} ({w['url']}): " + " / ".join(w["sentences"])[:500] for w in c["wiki"]][:2]
    if c.get("param"):
        e["param"] = [f"{p.get('year')} {p.get('round') or ''} {p.get('country') or ''} {p.get('confidence')}: {p.get('basis')}"
                      for p in c["param"]][:3]
    if s in sib:
        e["sib"] = sib[s]
    pack[s] = e
write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
write_atomic(HERE / "news-extra-pack.json", json.dumps(news_pack, indent=1, ensure_ascii=False) + "\n")
cnt = {k: sum(1 for v in pack.values() if k in v) for k in
       ("recall_basis", "press", "sec", "edgar", "13f", "formd", "wiki", "param", "sib")}
print(f"{len(pack)} rows;", cnt)
