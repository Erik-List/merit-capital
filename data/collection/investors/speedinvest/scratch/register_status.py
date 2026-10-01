#!/usr/bin/env python3
"""Austrian and German register layer for the Speedinvest book (decisions.md D8),
read through North Data's free entity pages (the Firmenbuch and the
Handelsregister). Adapted from Visionaries Club's register-status.py.

For each target row: North Data suggest (countries AT,DE), the entity whose
name is the row's name plus a legal suffix (case- and punctuation-insensitive),
then that entity page: the terminated mark, liquidation / insolvency /
dissolution events, the seat, the founding date, the name history, and every
publication line naming a Speedinvest vehicle as shareholder (the Firmenbuch
names the holders of an Austrian GmbH at each change).

A dissolution, liquidation or insolvency entry is filing-grade `defunct`
evidence (or `acquired` where a sale follows); a Speedinvest vehicle on the
shareholder register is filing-grade membership corroboration. A lookup that
fails or matches nothing is recorded as such, never as "active".

Input:  scratch/register-targets.json  [{"slug", "name", "countries"}]
Output: sources/registers/status-at-de.json  {slug: {...}}
"""
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "sources" / "registers" / "status-at-de.json"
RAW = HERE / "nd-raw"
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
SUFFIX = re.compile(r"(?i)\s*,?\s*(gmbh(\s*&\s*co\.?\s*kg)?|ug(\s*\(haftungsbeschränkt\))?|ag|se|kg|og|e\.?\s?u\.?|"
                    r"gesellschaft mbh|holding|technologies|technology|software|solutions|labs|group|international|"
                    r"austria|deutschland|germany)\.?$")


def get(url: str) -> str:
    r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, url], capture_output=True)
    time.sleep(3)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""


def key(s: str) -> str:
    s = html.unescape(s).replace("·", ".")
    for _ in range(3):
        s = SUFFIX.sub("", s).strip()
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def text(b: str) -> str:
    b = re.sub(r"<script.*?</script>", "", b, flags=re.S)
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " | ", b)))
    return re.sub(r"(\|\s*)+", "| ", t)


def main() -> None:
    targets = json.loads((HERE / "register-targets.json").read_text())
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    RAW.mkdir(exist_ok=True)
    for t in targets:
        slug, name = t["slug"], t["name"]
        if out.get(slug, {}).get("status") not in (None, "lookup_failed"):
            continue
        s = get("https://www.northdata.com/suggest.json?query=" + urllib.parse.quote(name) + "&countries=" + t.get("countries", "AT,DE"))
        try:
            res = json.loads(s).get("results", [])
        except ValueError:
            out[slug] = {"name": name, "status": "lookup_failed", "why": "suggest did not answer JSON"}
            print(slug, "lookup failed", flush=True)
            continue
        cands = [r for r in res if r.get("type") == "company"]
        match = [r for r in cands if key(r["name"]) == key(name)]
        if not match:
            out[slug] = {"name": name, "status": "no_exact_match", "candidates": [f"{r['name']} ({r.get('description')})" for r in cands[:6]]}
            print(slug, "no exact match", [r["name"] for r in cands[:3]], flush=True)
            continue
        ent = match[0]
        f = RAW / (re.sub(r"[^A-Za-z0-9]+", "_", ent["url"].split("northdata.com/")[-1])[:120] + ".html")
        page = f.read_text(errors="replace") if f.exists() and f.stat().st_size > 20000 else get(ent["url"])
        if page and not f.exists():
            f.write_text(page)
        t_ = text(page)
        head = t_[t_.find("| Name |"):t_.find("| Name |") + 1500] if "| Name |" in t_ else t_[:1500]
        i = t_.find("| Publications |")
        pubs = t_[i:i + 8000] if i >= 0 else ""
        fd = re.search(r'"foundingDate" : "([^"]+)"', page)
        events = re.findall(r"\| (\d{1,2} \w{3,4} \d{4})(?: as [^|]+)? \| ([^|]*(?:Liquidation|liquidation|Insolvency|insolvency|"
                            r"Termination|terminated|Deletion|dissolv|Merger|Acquisition|Konkurs|Sanierung)[^|]*)", pubs)
        si = re.findall(r"\| (\d{1,2} \w{3,4} \d{4})(?: as [^|]+)? \| ([^|]*(?:Speedinvest|Initial Factor Speed Invest)[^|]*)", pubs)
        names = re.findall(r"\| Name \| (.*?) \| Identification", head)
        out[slug] = {"name": name, "status": "matched", "entity": ent["name"], "url": ent["url"],
                     "where": ent.get("description"), "terminated": "✝" in head or "Terminated" in head[:400],
                     "founded": fd.group(1) if fd else None,
                     "names": names[0].split(" | ") if names else [],
                     "events": [" ".join(e) for e in events[:8]],
                     "speedinvest_shareholder": [" ".join(e) for e in si[:6]],
                     "latest": pubs[18:420]}
        print(slug, "->", ent["name"], "| terminated" if out[slug]["terminated"] else "", out[slug]["events"][:2],
              "| SI:", len(si), flush=True)
        write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    write_atomic(OUT, json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(sum(1 for v in out.values() if v["status"] == "matched"), "matched of", len(out))


if __name__ == "__main__":
    main()
