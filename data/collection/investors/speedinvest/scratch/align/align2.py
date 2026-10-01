"""Second alignment pass from the Speedinvest run (PRO-84), 2026-10-01, after Erik's instruction that cross-investor
alignments need no approval from him and that open questions are settled by rule or research.

- seedcamp:wefox city. Both books now read Zurich, CH: the group's own imprint names wefox Holding AG, Zurich, and its
  About page gives Austria, the Netherlands and Switzerland as its markets (Germany is no longer one), so Berlin is
  the former operating base.
- y-combinator:diligent and y-combinator:june, skipped on 2026-09-30 because the readback showed one row missing and
  one extra. The cause is a leading space in the CSV name " Metadata" (the ingest trims it, the readback tool does
  not): the database equals the committed base. reingest2.py treats a missing/extra pair that is equal after
  trimming as exact and says so.
- a16z:june. Neither june.so's own investor list (Point Nine, Speedinvest, Y Combinator, eFounders, Kima and named
  angels) nor the June oven's names a16z, and a16z's list prints only the bare name. The company cannot be named, so
  the row reads as the playbook's unnameable row (identity_unresolved; status unknown, band and stage undetermined)
  and leaves every metric; the listing keeps it a member.

Each line is recorded ONCE (the record note-join bug). Usage: python3 align2.py [--dry] [book ...]
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro84"
TAG = "Aligned 2026-10-01 from the Speedinvest run (PRO-84)"

LINES = {
    "seedcamp": [{
        "slug": "wefox", "who": WHO, "hq_city": "Zurich", "hq_city_source": "web_verified",
        "hq_country": "CH", "hq_country_source": "web_verified", "hq_country_citation": "https://www.wefox.com/imprint",
        "note": f"{TAG}: headquarters Zurich. The group's own imprint names wefox Holding AG, Räffelstrasse 26, Zürich, "
                "and its About page gives Austria, the Netherlands and Switzerland as its markets; Germany is no "
                "longer one, so Berlin is the former operating base. Read on 2026-10-01.",
    }],
    "y-combinator": [
        {"slug": "diligent", "who": WHO, "status": "private",
         "status_citation": "https://tech.eu/2026/03/04/diligent-ai-raises-25m-to-support-kyc-and-aml-teams-with-ai-agents/",
         "note": f"{TAG}, rule 10: Diligent (godiligent.ai, London, S23) is operating and raised a seed in March 2026 "
                 "(tech.eu, 2026-03-04). The `acquired` reading and the 2015 as-of came from a weak CIK join with an "
                 "unrelated registrant and are not this company's."},
        {"slug": "june", "who": WHO, "status": "defunct", "status_citation": "https://www.june.so/blog/a-new-chapter",
         "note": f"{TAG}, rule 10: June (june.so, W21) wound down in 2025. The company's own post of 2025-07-08 says "
                 "operations end and the founding team joins Amplitude, an acqui-hire of the team only, so defunct "
                 "under the acqui-hire rule (Erik, 2026-09-20). The `acquired` status was carried from namesake rows "
                 "(First Round's June is the June oven)."},
    ],
    "a16z": [{
        "slug": "june", "who": WHO, "status": "unknown", "valuation_range": "undetermined", "valuation_usd": None,
        "seed_to_a_graduation": "undetermined", "focus": None,
        "flags": ["identity_unresolved", "city_unknown", "country_prior"], "clear_flags": ["stage_uncited"],
        "note": f"{TAG}: the company cannot be named. a16z's investment list prints the bare name June and nothing "
                "else. The row was read as june.so, the product-analytics company, but june.so's own funding post "
                "names Point Nine, Speedinvest, Y Combinator, eFounders, Kima and its angels and no a16z fund; the "
                "June oven's investors (Foundry, First Round, Lerer, Founders Fund, Eclipse) do not include a16z "
                "either. So the `acquired` status had no company behind it: status unknown, band, stage and "
                "graduation undetermined, and the row leaves every metric; the listing keeps it a member.",
    }],
}

DISTINCT = {
    "y-combinator": [
        {"rows": ["y-combinator:june", "first-round-capital:june"],
         "note": "YC's June is june.so, the product-analytics company (W21, wound down 2025); First Round's is June, "
                 "the smart oven Weber bought in 2021. Different companies (ruled at the Speedinvest alignment, "
                 "PRO-84, 2026-10-01)."},
        {"rows": ["y-combinator:diligent", "battery-ventures:diligent-software"],
         "note": "YC's Diligent is Diligent AI (godiligent.ai, London, S23); Battery's is Diligent Software, an older "
                 "exited holding. Different companies (ruled at the Speedinvest alignment, PRO-84, 2026-10-01)."},
    ],
}


def rule_distinct(inv):
    p = ROOT / f"data/collection/investors/{inv}/companies/cross-rulings.json"
    d = json.loads(p.read_text()) if p.exists() else {}
    have = {frozenset(e["rows"]) for e in d.get("distinct", [])}
    add = [e for e in DISTINCT.get(inv, []) if frozenset(e["rows"]) not in have]
    if add:
        d.setdefault("distinct", []).extend(add)
        p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
    print(f"   {inv}: {len(add)} distinct pair(s) ruled")


if __name__ == "__main__":
    dry = "--dry" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    for inv, lines in sorted(LINES.items()):
        if only and inv not in only:
            continue
        p = HERE / f"{inv}-2.jsonl"
        p.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines))
        print(f"== {inv}: {len(lines)} line(s) -> {p.name}")
        if dry:
            continue
        rule_distinct(inv)
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(p)], cwd=ROOT,
                           capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-800:])
        if r.returncode:
            sys.exit(f"record failed for {inv}; stopping")
