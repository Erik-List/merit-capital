#!/usr/bin/env python3
"""Choose the evidence for each recall candidate that is not yet a base row (PRO-167).

Reads recall/candidates.json (assemble-candidates.py), cand-news.json (the per-company
'"<name>" "Tiger Global"' query), news-decoded*.json and snippets.json, and writes
recall/additions-plan.json:

  {key: {"name", "grade", "kind", "gid"|"url", "title", "date", "source", "basis", "first_seen",
         "sentences", "sources": [...]}}

Grades, strongest first (the evidence classes of COLLECTION.md 1):
  A  fund_filing: a full-text triage line naming a Tiger vehicle as a holder while the
     company was private (prospectus holder table, IRA signatory, merger filing)
  B  web: a headline that names Tiger Global AND the company with an investment word
  C  web: a Wikipedia sentence naming Tiger's investment in the company
  D  web: a funding headline for the company whose article (the publisher page, fetched)
     has a sentence naming Tiger Global
  X  rejected: only a parametric (model-memory) line, or only a public-trade headline,
     or a funding headline whose article does not name Tiger (reason recorded)

A candidate needing a network step prints it under TODO: gids to decode (for B and D)
and URLs to fetch (for D). Re-run after decode_batch.py / fetch-snippets.py.
"""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
INV = HERE.parent


def J(p, d):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else d


cands = J(HERE / "recall/candidates.json", {})
cnews = J(HERE / "cand-news.json", {})
bnews = J(HERE / "bing-news.json", {})
snips = J(HERE / "snippets.json", {})
decoded = {}
for f in sorted(HERE.glob("news-decoded*.json")):
    decoded.update(J(f, {}))
manual = J(HERE / "recall/manual-decisions.json", {})   # key -> {"reject": reason} | {"alias_of": key}

INVEST = re.compile(r"(?i)\b(rais|lead|led|co-led|backs?|backed|invest|funding|fund\b|round|stake|series|seed|valu|"
                    r"unicorn|bets?|pumps?|pours?|injects?|infus|secures?|bags?|lands?|nabs?|gets?|closes?|picks? up|"
                    r"snaps? up|buys? into|financing|capital from|from tiger|tiger global[- ]backed)")
PUBLIC = re.compile(r"(?i)\b(shares? (fall|rise|jump|drop|slump)|13f|stock picks?|hedge fund (returns?|performance)|"
                    r"sells? (its )?(entire )?stake in (?:[A-Z]\w+ )?(?:inc|corp)|trims? stake|dumps? shares|buys? shares of)")


def mentions(title, name):
    """The company's name as a word in the title. Case-sensitive on the first letter, so a
    common-word brand (Glitch, Slice, Jar) does not match the lowercase word."""
    n = re.sub(r"\s*\(.*?\)", "", name).split(",")[0].strip()
    if not n:
        return False
    pat = r"(?<![\w])" + re.escape(n[0]) + "(?i:" + re.escape(n[1:]) + r")(?![\w])"
    return bool(re.search(pat, title))


def year(d):
    return (d or "")[:4] or None


plan, todo_gids, todo_urls = {}, set(), set()
for k, c in cands.items():
    if c.get("in_base") or k in manual and manual[k].get("alias_of"):
        continue
    name = c["name"]
    names = list(c.get("names", {}).keys()) or [name]
    srcs = [s for s in ("press_T", "press_F", "press_P", "param", "fts", "wiki") if c.get(s)]
    rej = (manual.get(k) or {}).get("reject")
    if rej:
        plan[k] = {"name": name, "grade": "X", "reason": rej, "sources": srcs}
        continue
    # A: filing
    fts = [x for x in c.get("fts", []) if x.get("url")]
    if fts:
        x = sorted(fts, key=lambda x: x.get("first_private_evidence_date") or "9999")[0]
        plan[k] = {"name": name, "grade": "A", "kind": "fund_filing", "url": x["url"],
                   "basis": f"{x.get('basis')} (SEC {x.get('class')} filing; vehicles: {', '.join(x.get('vehicles') or []) or 'not named'}; desk {x.get('desk')})",
                   "first_seen": year(x.get("first_private_evidence_date")), "desk": x.get("desk"), "sources": srcs}
        continue
    # headlines naming Tiger and the company: the sweep's T class plus the per-company query
    heads = [h for h in c.get("press_T", [])]
    for it in (cnews.get(k) or {}).get("items", []):
        if "tiger" in it["title"].lower() and any(mentions(it["title"], n) for n in names):
            heads.append({"gid": it["gid"], "date": it["date"], "source": it.get("source"), "title": it["title"]})
    for it in (bnews.get(k) or {}).get("items", []):
        if "tiger" in it["title"].lower() and any(mentions(it["title"], n) for n in names):
            heads.append({"gid": None, "url": it["url"], "date": it["date"], "source": it.get("source"), "title": it["title"]})
    heads = [h for h in heads if INVEST.search(h["title"]) and not PUBLIC.search(h["title"])]
    if heads:
        def score(h):
            t = h["title"]
            return (bool(re.search(r"(?i)series|seed|round|led by|leads|co-led", t)), bool(re.search(r"\$|₹|rs\.? ?\d|crore|million|billion", t, re.I)), bool(h.get("url") or decoded.get(h.get("gid"))), -(int(year(h["date"]) or 2100)))
        with_url = [x for x in heads if x.get("url") or decoded.get(x.get("gid"))]
        h = sorted(with_url or heads, key=score, reverse=True)[0]
        first = min((year(x["date"]) for x in heads if year(x["date"])), default=None)
        e = {"name": name, "grade": "B", "kind": "web", "gid": h["gid"], "title": h["title"], "date": h["date"],
             "source": h.get("source"), "first_seen": first, "sources": srcs, "n_heads": len(heads)}
        u = h.get("url") or decoded.get(h.get("gid"))
        if u:
            e["url"] = u
            e["sentences"] = (snips.get(u) or {}).get("sentences")
        else:
            todo_gids.add(h["gid"])
        plan[k] = e
        continue
    # C: Wikipedia
    if c.get("wiki"):
        w = c["wiki"][0]
        plan[k] = {"name": name, "grade": "C", "kind": "web", "url": w["url"], "title": w["title"],
                   "sentences": w["sentences"][:2], "basis": " / ".join(w["sentences"][:2])[:400],
                   "first_seen": None, "sources": srcs}
        continue
    # D: a funding headline whose article names Tiger
    fh = [h for h in c.get("press_F", []) if any(mentions(h["title"], n) for n in names)]
    fh += [{"gid": None, "url": it["url"], "date": it["date"], "source": it.get("source"), "title": it["title"]}
           for it in (bnews.get(k) or {}).get("items", []) if any(mentions(it["title"], n) for n in names)]
    if fh:
        got = None
        for h in sorted(fh, key=lambda h: (not h.get("url"), h["date"] or "")):
            u = h.get("url") or decoded.get(h.get("gid"))
            if not u:
                todo_gids.add(h["gid"])
                continue
            s = snips.get(u)
            if not s or s.get("status") != "ok":
                todo_urls.add(u)
                continue
            own = [x for x in (s.get("sentences") or []) if any(mentions(x, n) for n in names)]
            if own:
                got = (h, u, own)
                break
        if got:
            h, u, ss = got
            plan[k] = {"name": name, "grade": "D", "kind": "web", "gid": h["gid"], "url": u, "title": h["title"],
                       "date": h["date"], "source": h.get("source"), "sentences": ss[:3],
                       "first_seen": year(h["date"]), "sources": srcs}
        else:
            def _u(h):
                return h.get("url") or decoded.get(h.get("gid"))
            pending = any(_u(h) is None or (snips.get(_u(h)) or {}).get("status") not in ("ok", "blocked") for h in fh)
            plan[k] = {"name": name, "grade": "pending" if pending else "X",
                       "reason": None if pending else "no fetched article has a sentence naming both Tiger Global and the company",
                       "sources": srcs, "titles": [h["title"] for h in fh[:3]]}
        continue
    if c.get("param"):
        asked = k in cnews and cnews[k].get("status") == "ok"
        plan[k] = {"name": name, "grade": "X" if asked else "pending",
                   "reason": "model-memory lead only; the per-company press query found no headline tying Tiger Global to a round" if asked else None,
                   "sources": srcs, "param": [p.get("basis") for p in c["param"]][:2]}
        continue
    plan[k] = {"name": name, "grade": "X", "reason": "public-market trade headline only (T3)", "sources": srcs}

(HERE / "recall/additions-plan.json").write_text(json.dumps(plan, indent=1, ensure_ascii=False) + "\n")
(HERE / "recall/todo-gids.txt").write_text("\n".join(sorted(todo_gids)) + "\n")
(HERE / "recall/todo-urls.json").write_text(json.dumps({u: u for u in sorted(todo_urls)}, indent=0) + "\n")
from collections import Counter
print("grades:", dict(Counter(v["grade"] for v in plan.values())))
print(f"TODO: {len(todo_gids)} gids to decode, {len(todo_urls)} pages to fetch")
need_q = [k for k, v in plan.items() if v["grade"] == "pending" and "param" in v]
print(f"param-only candidates still to query: {len(need_q)}")
