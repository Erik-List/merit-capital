#!/usr/bin/env python3
"""Recall layer: the firm's own NETWORK directory, 2012-2016.

First Round's /team/ namespace holds two populations (config roster._note).
The capitalised half — /team/<First_Last>, 220+ slugs — is not the firm's
roster at all: it is a directory of the FOUNDERS AND CEOs of its portfolio
companies, each page headed "<Role> at <Company>". That makes it a
first-party company list the portfolio pages never carried, and the right
use for a namespace that would otherwise poison the Form D sweep.

Writes sources/web/network-directory.json: {person: {company, role, url}}.
Consumed by the recall probe.
"""
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import shared_throttle  # noqa: E402

INV = Path(__file__).resolve().parents[1]
OUT = INV / "sources/web/network-directory.json"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"


def curl(url: str) -> str:
    for _ in range(3):
        shared_throttle.wait("ia")
        r = subprocess.run(["curl", "-sfL", "--compressed", "--max-time", "60",
                            "-H", f"User-Agent: {UA}", url], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode("utf-8", errors="replace")
        time.sleep(2)
    return ""


def main() -> None:
    rows = json.loads(curl(
        "http://web.archive.org/cdx/search/cdx?url=firstround.com/team*&output=json"
        "&filter=statuscode:200&collapse=urlkey&fl=original,timestamp&limit=900") or "[]")[1:]
    people = {}
    for orig, ts in rows:
        m = re.search(r"/team/([A-Z][A-Za-z]+_[A-Za-z.'-]+)$", orig.split("?")[0])
        if m:
            people.setdefault(m.group(1), (ts, orig))
    print(f"{len(people)} network profile slugs")
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    for i, (slug, (ts, orig)) in enumerate(sorted(people.items()), 1):
        if slug in out:
            continue
        html = curl(f"https://web.archive.org/web/{ts}id_/{orig}")
        if not html:
            out[slug] = {"company": None, "role": None, "url": orig}
            continue
        body = re.sub(r"(?s)<script.*?</script>", "", html)
        text = re.sub(r"\s+", " ", unescape(re.sub(r"(?s)<[^>]+>", " ", body))).strip()
        name = slug.replace("_", " ")
        m = re.search(re.escape(name) + r"\s+(?P<role>[A-Z][^|]{2,60}?)\s+at\s+(?P<co>[A-Z][\w&.'’ -]{1,40})",
                      text)
        out[slug] = {"company": m.group("co").strip() if m else None,
                     "role": m.group("role").strip() if m else None,
                     "url": orig}
        if i % 25 == 0:
            OUT.parent.mkdir(parents=True, exist_ok=True)
            OUT.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
            print(f"  {i}/{len(people)}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    named = sum(1 for v in out.values() if v["company"])
    print(f"wrote {OUT.name} — {len(out)} people, {named} with a named company")


main()
