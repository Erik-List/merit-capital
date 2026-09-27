#!/usr/bin/env python3
"""The press surface behind the control test (decisions.md D3), a layer this
run invented because the firm's own site publishes no strategy label and its
posts almost never say "majority" in words.

For every site-listed company it asks Google News (the shared, throttled
surface graduation-surfaces.py uses) one question: the company's name, the
firm's name, and the words a control transaction is reported with. It keeps
the headlines that name the company, and marks the ones whose wording is a
control transaction BY the firm:

    "Insight (Venture) Partners acquires / to acquire / buys / takes X private"
    "X acquired by Insight", "majority stake/investment ... Insight"

A headline is a lead with a date and a publisher, not a verdict: the judge
reads it against the row and cites the article (decoded from the Google News
id by graduation-surfaces.py decode). Three outcomes per row, never two: ok
with items, ok with none, error (retried on the next run).

Output: sources/web/control-surfaces.json
Usage:  python3 .../scratch/control-surfaces.py [--slugs a,b] [--refresh]
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from datetime import date
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts/graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gs)
from paths import write_atomic  # noqa: E402

OUT = INV / "sources/web/control-surfaces.json"
FIRM = '("Insight Partners" OR "Insight Venture Partners")'
WORDS = '(acquires OR acquired OR acquisition OR majority OR "take private" OR buyout OR recapitalization)'
BY_FIRM = re.compile(
    r"insight (?:venture )?partners[^.]{0,40}?\b(acquires?|to acquire|acquiring|buys|to buy|takes? (?:a )?majority|"
    r"completes? acquisition|completes? recapitali[sz]ation|takes? .{0,30}private|snaps up|purchases?)\b|"
    r"\b(acquired|bought|taken private|snapped up|purchased) by insight|"
    r"\bmajority (?:stake|investment|interest)\b.{0,60}insight|insight.{0,60}\bmajority (?:stake|investment|interest|owner)|"
    r"\bsells? (?:itself )?to insight|\bsold to insight|\bgoes private.{0,40}insight|insight.{0,40}\btake[- ]private", re.I)
MINORITY = re.compile(r"\bminority\b", re.I)


def main() -> None:
    comps = json.load(open(INV / "sources/site/company-pages.json"))["rows"]
    want = None
    if "--slugs" in sys.argv:
        want = set(sys.argv[sys.argv.index("--slugs") + 1].split(","))
    refresh = "--refresh" in sys.argv
    try:
        store = json.load(open(OUT))
    except (OSError, ValueError):
        store = {"_readme": __doc__.strip(), "rows": {}}
    rows = store["rows"]
    todo = [c for c in comps if (not want or c["slug"] in want)
            and (refresh or rows.get(c["slug"], {}).get("status") != "ok")]
    print(f"{len(todo)} rows to ask", flush=True)
    for i, c in enumerate(todo, 1):
        name = gs.clean_name(re.sub(r"\s*\(.*?\)\s*", " ", c["name"]).strip())
        if len(name) < 2:
            continue
        q = f'"{name}" {FIRM} {WORDS}'
        r = gs.googlenews(q, name)
        rec = {"status": r["status"], "query": q, "asof": date.today().isoformat(), "name": name}
        if r["status"] == "ok":
            items = [it for it in r["items"] if it["names"]]
            for it in items:
                it["control_by_firm"] = bool(BY_FIRM.search(it["title"]))
                it["minority"] = bool(MINORITY.search(it["title"]))
                it.pop("names", None)
            rec["n"] = len(items)
            rec["items"] = items[:25]
            rec["control_headlines"] = sum(1 for it in items if it["control_by_firm"])
        else:
            rec["http"] = r.get("http")
        # the second question is the company's own news: rounds and exits,
        # whoever the counterparty (status, marks, the acquirer's name)
        q2 = f'"{name}" (raises OR funding OR valuation OR acquired OR acquires OR IPO OR "shuts down")'
        r2 = gs.googlenews(q2, name)
        rec["news_status"] = r2["status"]
        if r2["status"] == "ok":
            its = [it for it in r2["items"] if it["names"] and (it["rounds"] or it["amounts"])]
            rec["news"] = [{"date": it["date"], "title": it["title"], "source": it["source"],
                            "gid": it["gid"]} for it in its[-14:]]
        if r2["status"] != "ok":
            rec["status"] = "error"
        rows[c["slug"]] = rec
        if i % 25 == 0 or i == len(todo):
            write_atomic(OUT, json.dumps(store, indent=1, ensure_ascii=False) + "\n")
            ok = sum(1 for v in rows.values() if v["status"] == "ok")
            ctl = sum(1 for v in rows.values() if v.get("control_headlines"))
            print(f"  {i}/{len(todo)}  ok {ok}  rows with a control headline {ctl}", flush=True)
    err = [s for s, v in rows.items() if v["status"] != "ok"]
    print(f"done: {len(rows)} rows, {len(err)} errors")
    if err:
        sys.exit(3)


if __name__ == "__main__":
    main()
