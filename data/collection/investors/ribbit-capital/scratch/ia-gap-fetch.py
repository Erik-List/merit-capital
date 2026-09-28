#!/usr/bin/env python3
"""The 2019-2020 gap in Ribbit's archived listing, fetched with the fewest
possible Internet Archive requests (the bulk fetcher tripped the IA firewall
twice on 2026-09-28; Common Crawl has no ribbitcap.com capture between
2018-01 and 2021-01). One replay request per target date: the replay
redirects to the nearest capture, curl follows it, and the true timestamp is
read off the final URL. No CDX query, no probes. Registers each capture in
sources/wayback/captures.json like the other fetchers.

Usage: python3 scratch/ia-gap-fetch.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

WB = HERE.parent / "sources" / "wayback"
RAW = WB / "raw"
CAPS = WB / "captures.json"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
TARGETS = [("our-bets", "20190604141714", "http://ribbitcap.com/our-bets/"),   # a known capture
           ("our-bets", "20191201", "http://ribbitcap.com/our-bets/"),
           ("our-bets", "20200615", "http://ribbitcap.com/our-bets/"),
           ("our-bets", "20201115", "http://ribbitcap.com/our-bets/")]


def main() -> None:
    left = shared_throttle.cooldown_remaining("ia")
    if left > 0:
        sys.exit(f"IA cooldown active for {left / 60:.0f} more minutes; not fetching")
    caps = json.loads(CAPS.read_text())
    have = {(c["era"], c["ts"]) for c in caps["captures"]}
    for era, when, orig in TARGETS:
        shared_throttle.wait("ia")
        url = f"https://web.archive.org/web/{when}id_/{orig}"
        p = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, "-o", "-", "-w", "\n%{url_effective} %{http_code}", url],
                           capture_output=True)
        body, _, tail = p.stdout.rpartition(b"\n")
        eff, _, code = tail.decode().partition(" ")
        if p.returncode != 0:
            print(f"{when}: curl rc={p.returncode}; stopping (a refused connection is the firewall; do not retry)")
            if p.returncode == 7:
                shared_throttle.cooldown("ia")
            break
        m = re.search(r"/web/(\d{14})id_/", eff)
        if not code.startswith("2") or not m:
            print(f"{when}: http {code} ({eff}); recorded as failed, not as an empty year")
            caps.setdefault("failed", []).append({"era": era, "ts": when, "url": url, "error": f"http {code}"})
            continue
        ts = m.group(1)
        if (era, ts) in have:
            print(f"{when}: nearest capture {ts} already on disk")
            continue
        dest = RAW / f"{era}-{ts}.html"
        dest.write_bytes(body)
        caps["captures"].append({"era": era, "ts": ts, "original": orig, "source": "ia-replay",
                                 "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                                 "raw": str(dest.relative_to(HERE.parent))})
        have.add((era, ts))
        print(f"{when}: captured {ts}, {len(body)} bytes")
    caps["captures"].sort(key=lambda c: (c["era"], c["ts"]))
    write_atomic(CAPS, json.dumps(caps, indent=1) + "\n")


if __name__ == "__main__":
    main()
