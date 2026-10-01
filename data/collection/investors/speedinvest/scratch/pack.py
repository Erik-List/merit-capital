#!/usr/bin/env python3
"""Evidence pack for the Speedinvest judge and research agents, one block per row:
the live site card (Year Invested, sectors and team tags, Exits tag, country,
website, the card's own description, which often states an exit), the Getro
board record, the archived 2017-2025 listings and pages (deal partner, invest
year, filter tags incl. Pre-Seed / Acquired, year acquired), the firm's own posts
naming the row, the Austrian/German register reading, the news headlines the
surfaces layer found, the sibling books holding the same company, the Form D
evidence, and the queue item's open needs.

Usage: python3 pack.py slug [slug ...]   |   python3 pack.py --batch N [size]
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402

QUEUE = J.H / "queue" / "queue.json"


def sentences(text, name, n=3):
    out = []
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text or ""):
        if re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", s, re.I):
            out.append(s.strip()[:300])
        if len(out) >= n:
            break
    return out


def block(slug, item=None):
    b = J.row(slug)
    name = b.get("name") or slug
    print(f"\n=== {slug} | {name} | first_seen {b.get('first_seen')} | archive years {b.get('wayback_years')} | tier {b.get('tier')}")
    if item:
        print("  needs:", item.get("need"), "| evidence:", item.get("evidence_class"))
    lv = J.live(slug, name)
    if lv:
        print(f"  SITE {lv['url']} | invested {lv.get('invest_year')} | {lv.get('sectors')} {lv.get('team_tags')} | "
              f"{lv.get('status_site')} | {lv.get('country_site')} | {lv.get('website')}")
        print(f"       {(lv.get('description') or '')[:420]}")
    bo = J.board(slug, name)
    if bo:
        print(f"  BOARD {bo.get('url')} | founded {bo.get('founded_board')} | {bo.get('org_type_board')} | "
              f"board stage (never a label) {bo.get('stage_board')} | {(bo.get('description') or '')[:160]}")
    e = J.ev(slug, name)
    if e:
        caps = e.get("first_capture"), e.get("last_capture")
        print(f"  ARCHIVE {e.get('n_captures')} captures {caps[0]['ts'][:8]}..{caps[1]['ts'][:8]} | names {e.get('names')} | "
              f"partners {e.get('partners')} | invest years {e.get('invest_years')} | tags {e.get('sections')}")
        print(f"          first {caps[0]['capture_url']}")
        for c in [c for c in [caps[0], caps[1]] if c.get("year_acquired")][:1]:
            print(f"          year acquired (firm's field): {c['year_acquired']}")
    ps = sorted(J.posts_for(slug).items(), key=lambda x: (name.lower() not in (x[1]["title"] or "").lower(), x[1]["date"] or "z"))
    for k, p in ps[:6]:
        ss = sentences(p["text"], name) or [p["text"][:200]]
        print(f"  POST {p['date'] or '?':10} {k[:60]} | {(p['title'] or '')[:90]} | {p['capture_url']}")
        for s in ss[:2]:
            print(f"       > {s[:260]}")
    rg = J.REG.get(slug)
    if rg:
        print(f"  REGISTER {json.dumps(rg, ensure_ascii=False)[:400]}")
    g = J.SURF.get(slug) or {}
    heads = []
    for svc, v in (g.get("surfaces") or {}).items():
        for i in v.get("items") or []:
            if i.get("names") or svc == "googlenews_firm":
                heads.append((bool(i.get("rounds") or i.get("amounts")), i.get("date", "")[:10], svc, i))
    heads.sort(key=lambda x: (not x[0], x[1]))
    for has, d, svc, i in heads[:10]:
        gid = (i.get("gid") or i.get("url") or "")[-10:]
        print(f"  NEWS {d} {svc[:10]:10} [{gid}] {i.get('source', '')[:18]:18} {i.get('title', '')[:130]}")
    for s in g.get("siblings") or []:
        print(f"  SIBLING {s.get('investor')}: status {s.get('status')} band {s.get('valuation_range')} stage "
              f"{s.get('entry_stage')} ({s.get('entry_stage_source')}) {s.get('entry_date', '')} grad "
              f"{s.get('seed_to_a_graduation', '')} | {(s.get('note') or '')[:140]}")
    if b.get("formd_accessions") or b.get("partners_formd"):
        print(f"  FORM D {b.get('formd_span')} max {b.get('formd_max_round_usd')} | partners {b.get('partners_formd')} | "
              f"{(b.get('formd_links') or '')[:160]}")
    if item:
        for k in ("formd_graduation", "graduation_evidence", "known", "acquirer", "former_unicorn", "entry_date",
                  "issuer_city", "year_inc"):
            if item.get(k):
                print(f"  item.{k}: {json.dumps(item[k], ensure_ascii=False)[:300]}")


def main():
    args = sys.argv[1:]
    q = json.loads(QUEUE.read_text()) if QUEUE.exists() else []
    items = q.get("items", q) if isinstance(q, dict) else q
    by = {i["slug"]: i for i in items} if isinstance(items, list) else {}
    if args and args[0] == "--batch":
        n = int(args[1])
        size = int(args[2]) if len(args) > 2 else 15
        slugs = [i["slug"] for i in items][n * size:(n + 1) * size]
    else:
        slugs = args
    for s in slugs:
        block(s, by.get(s))


if __name__ == "__main__":
    main()
