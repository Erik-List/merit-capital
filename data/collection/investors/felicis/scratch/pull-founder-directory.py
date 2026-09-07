#!/usr/bin/env python3
"""The founder directory, read as a first-party COMPANY list.

felicis.com publishes the founders it backed in their own namespace: 620
`founder` documents in the live Sanity dataset, and 153 archived
/founder/<first-last> pages 2013-2021. COLLECTION.md §5.2 (the First Round
rule) says such a directory must be kept out of the roster Form D sweep --
decisions.md D-T4a does that -- and, read the other way round, pulled
deliberately, because it is a company list the portfolio page may no longer
carry.

This writes the LIVE half now. The archived half needs web.archive.org, which
refused every connection from ~22:25 on 2026-09-06; `--archived` adds it and
is safe to re-run (the two halves union by company name).

A founder whose `company` reference does not resolve is the interesting case:
the founder document outlived the company document, so the row is a company
the CMS once carried and has since dropped.
"""
import argparse
import json
import subprocess
import time
import urllib.parse
from pathlib import Path

PROJECT, DATASET = "ggsokyyr", "production"
API = f"https://{PROJECT}.api.sanity.io/v2021-10-21/data/query/{DATASET}"
OUT = Path(__file__).resolve().parent.parent / "sources" / "site"
UA = "merit-capital research (erik@meritcapit.al)"

FOUNDERS = """*[_type=="founder"]|order(name asc){
  "founder": name, "role_line": role,
  "company_ref": company._ref,
  "name": company->name,
  "company_slug": company->slug.current
}"""


def query(groq: str):
    url = f"{API}?query={urllib.parse.quote(groq)}"
    for attempt in range(4):
        r = subprocess.run(["curl", "-sS", "--max-time", "120",
                            "-H", f"User-Agent: {UA}", url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout:
            try:
                return json.loads(r.stdout)["result"]
            except (json.JSONDecodeError, KeyError):
                pass
        if attempt == 3:
            raise SystemExit("sanity query failed")
        time.sleep(3 * (attempt + 1))
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archived", action="store_true",
                    help="also pull the archived /founder/ pages (needs the IA)")
    args = ap.parse_args()

    rows = query(FOUNDERS) or []
    dangling = [r for r in rows if r.get("company_ref") and not r.get("name")]
    named = [r for r in rows if r.get("name")]
    print(f"founder docs: {len(rows)}")
    print(f"  resolving to a live company doc : {len(named)}")
    print(f"  DANGLING company reference      : {len(dangling)}"
          "  <- founders of companies the CMS has dropped")

    out = []
    for r in named:
        out.append({"name": r["name"], "founder": r["founder"],
                    "founder_slug": None, "role_line": r.get("role_line"),
                    "source_path": "sanity:founder"})
    if args.archived:
        arch = OUT / "founder-directory-archived.json"
        if arch.exists():
            for r in json.loads(arch.read_text()).get("rows", []):
                out.append(r)
            print(f"  archived /founder/ rows added   : "
                  f"{len(json.loads(arch.read_text()).get('rows', []))}")
        else:
            print("  no archived pull on disk yet (sources/site/"
                  "founder-directory-archived.json)")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "founder-directory.json").write_text(json.dumps({
        "_readme":
            "Felicis's founder directory read as a first-party company list "
            "(COLLECTION.md §5.2). NOT roster evidence: decisions.md D-T4a "
            "keeps this namespace out of the Form D sweep, because a founder is "
            "a related person on their own company's Form D and sweeping them "
            "would confirm false members with filing-grade-looking evidence. "
            f"{len(dangling)} founder documents carry a company reference that "
            "no longer resolves; those are companies the CMS has dropped and "
            "are listed under _dangling_refs for the recall probe.",
        "_pulled": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "_dangling_refs": sorted({r["company_ref"] for r in dangling}),
        "_dangling_founders": sorted(r["founder"] for r in dangling if r.get("founder")),
        "_list": "companies-founder-directory",
        "rows": out,
    }, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote founder-directory.json: {len(out)} rows")


if __name__ == "__main__":
    main()
