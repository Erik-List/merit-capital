#!/usr/bin/env python3
"""Archived /team/ and /advisors/ INDEX pages, the WordPress-era roster discriminator.

Between 2015 and ~2021 8vc.com rendered its people on two index pages whose cards
carry the name and, for the team, the title inside a modal; ADVISOR PROFILES lived
under /team/<slug> in the same namespace as the partners, so the CDX roster sweep
picked up Scott Cook, Jerry Yang, John Mack, Ashton Kutcher and Ronnie Lott and the
Form D sweep was seeding on them (COLLECTION.md §5, the First Round rule).

These two index pages separate the sets by the firm's own rendering — `square--team`
versus `square--advisor` — for every archived year, which is what the /advisors/
per-person URLs cannot do (they only exist from 2025).

Writes sources/site/wp-people.json.

Usage: python3 wp-people-pull.py
"""
import html
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
P = Paths("8vc")
RAW = P.root / "scratch" / "wayback-people"


def clean(s: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def curl(url: str, min_bytes: int = 2000) -> str:
    for i in range(3):
        shared_throttle.wait("ia")
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, url],
                           capture_output=True)
        if r.returncode == 0 and len(r.stdout) > min_bytes:
            return r.stdout.decode("utf-8", errors="replace")
        time.sleep(2 * (i + 1))
    return ""


def cdx(path: str) -> list[str]:
    """One capture per year for the index page."""
    out = curl("https://web.archive.org/cdx/search/cdx?url=8vc.com" + path
               + "&output=text&fl=timestamp,statuscode&filter=statuscode:200&collapse=timestamp:4",
               min_bytes=10)
    return [l.split()[0] for l in out.splitlines() if l.strip()]


def parse(t: str, kind: str) -> list[dict]:
    """Cards are `square--team` / `square--advisor`; the team's titles sit in the modal."""
    rows = []
    for m in re.finditer(
            r'class="square square--(team|advisor)[^"]*"(.*?)</(?:a|div)><!-- /\.square -->', t, re.S):
        card = m.group(2)
        nm = re.search(r'class="team-member-name">(.*?)</strong>', card) or \
            re.search(r'<h3><strong>(.*?)</strong></h3>', card)
        if not nm:
            continue
        name = clean(nm.group(1))
        role = ""
        r = re.search(r'<p><p>(.*?)</p>', card, re.S)
        if r:
            role = clean(r.group(1))
        rows.append({"name": name, "kind": m.group(1), "role": role})
    # team titles live in the per-person modal, keyed by the anchor id
    for m in re.finditer(r'data-remodal-id="([a-z0-9-]+)".*?alt="([^"]+)"[^>]*>\s*'
                         r'<h3[^>]*>(.*?)</h3>\s*<h4[^>]*>(.*?)</h4>', t, re.S):
        for row in rows:
            if row["name"] == clean(m.group(3)) and not row["role"]:
                row["role"] = clean(m.group(4))
                row["slug"] = m.group(1)
    return rows


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    people: dict[tuple[str, str], dict] = {}
    for path, kind in (("/team/", "team"), ("/advisors/", "advisor")):
        stamps = cdx(path)
        print(f"{path}: {len(stamps)} yearly captures -> {stamps}")
        for ts in stamps:
            f = RAW / f"{kind}-{ts}.html"
            if f.exists():
                t = f.read_text(encoding="utf-8", errors="replace")
            else:
                t = curl(f"http://web.archive.org/web/{ts}id_/http://8vc.com{path}")
                if t:
                    f.write_text(t, encoding="utf-8")
            if not t:
                print(f"  {ts}: no capture")
                continue
            rows = parse(t, kind)
            print(f"  {ts}: {len(rows)} cards")
            for r in rows:
                k = (r["kind"], r["name"])
                e = people.setdefault(k, {**r, "years": []})
                y = int(ts[:4])
                if y not in e["years"]:
                    e["years"].append(y)
                if r.get("role") and not e.get("role"):
                    e["role"] = r["role"]
    out = sorted(people.values(), key=lambda r: (r["kind"], r["name"]))
    payload = {
        "_readme": ("8vc.com's own /team/ and /advisors/ index pages, one capture per archived "
                    "year, parsed by scratch/wp-people-pull.py. The firm's own card class "
                    "(square--team vs square--advisor) is the discriminator that separates its "
                    "partners from the Advisor Upside network, which shared the /team/<slug> "
                    "namespace in the WordPress era. `advisor` rows are excluded from the Form D "
                    "roster sweep (decisions.md D5); a person appearing as both is a partner."),
        "people": out,
    }
    write_atomic(P.root / "sources" / "site" / "wp-people.json",
                 json.dumps(payload, indent=1, ensure_ascii=False))
    n_t = sum(1 for r in out if r["kind"] == "team")
    print(f"wrote wp-people.json — {n_t} team, {len(out) - n_t} advisors")


if __name__ == "__main__":
    main()
