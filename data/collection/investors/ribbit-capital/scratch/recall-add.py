#!/usr/bin/env python3
"""Recall probe (PRO-161): write the probe's additions into the ledger's
recall_additions (with a member verdict each) under record's own lock, so a
judge recording in parallel never loses an update. The rejections live in
scratch/recall/rejections.json. Additions enter the base at the one rebuild.

Usage: python3 scratch/recall-add.py
"""
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
from shared_throttle import exclusive  # noqa: E402

P = Paths("ribbit-capital")
WHO = "agent-judge-pro161"
DELPHIA = "https://www.prnewswire.com/news-releases/algo-advisor-delphia-closes-60m-series-a-round-led-by-multicoin-capital-301563593.html"

ADDS = [
    {"slug": "delphia", "name": "Delphia", "first_seen": "2022", "on_site_now": False, "sector": "",
     "source": "recall probe, press sweep ('\"led by Ribbit Capital\"' and related Google News queries)",
     "basis": "Delphia's own release: its $60M Series A was 'led by Multicoin Capital with additional participation from "
              "Ribbit Capital, FTX Ventures, Valor Equity Partners, FJ Labs ...' (PR Newswire, 2022-06-08). Never on "
              "the firm's lists (live Rebels, archived Bets and Our Bets).",
     "citation": DELPHIA},
]


def main() -> None:
    with exclusive(f"record-{P.slug}"):
        led = json.loads(P.ledger.read_text())
        bucket = led.setdefault(P.slug, {"verdicts": {}, "recall_additions": []})
        have = {a["slug"] for a in bucket.setdefault("recall_additions", [])}
        for a in ADDS:
            if a["slug"] not in have:
                bucket["recall_additions"].append(a)
            bucket["verdicts"][a["slug"]] = {
                "verdict": "member", "who": WHO, "evidence_class": "web",
                "basis": a["basis"], "citation": a["citation"], "confidence": "high",
                "decided": date.today().isoformat()}
        write_atomic(P.ledger, json.dumps(led, indent=1, sort_keys=True) + "\n")   # run.py record's own form
    print(f"recall additions: {[a['slug'] for a in ADDS]}")


if __name__ == "__main__":
    main()
