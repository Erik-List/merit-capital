#!/usr/bin/env python3
"""Pull NEA's Statamic CMS through its public GraphQL endpoint.

nea.com is Next.js over Statamic (statamic.nea.com); /graphql answers without a
token. Writes one raw JSON per collection under sources/site/statamic/, every
entry of every status the API will serve (published and, where the API allows,
unpublished), so the listing layer is reproducible from disk.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import write_atomic  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "sources" / "site" / "statamic"
EP = "https://statamic.nea.com/graphql"

PORTFOLIO_FIELDS = """
  id slug title url uri date published private status
  first_invested external_url short_description description meta_info
  company_stage { label value }
  company_status_value { label value }
  company_status company_status_line_two force_current
  investment_type { label value }
  milestones
  theme { label value }
  additional_theme { label value }
  company_category { id slug title }
  team { id title slug url }
  board_members { id title slug url }
  board_member_observer { id title slug url }
  logo { url permalink }
"""


def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}})
    for attempt in range(4):
        r = subprocess.run(
            ["curl", "-s", "-m", "120", "-A", "Mozilla/5.0", "-X", "POST",
             "-H", "Content-Type: application/json", "--data-binary", "@-", EP],
            input=body, capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip().startswith("{"):
            d = json.loads(r.stdout)
            if "errors" in d and not d.get("data"):
                raise SystemExit(f"GraphQL error: {d['errors']}")
            return d
        time.sleep(3 * (attempt + 1))
    raise SystemExit(f"fetch failed rc={r.returncode}: {r.stderr[:200]}")


def pull(collection, fields, status_filter=None):
    rows, page = [], 1
    while True:
        filt = f', filter: {{status: "{status_filter}"}}' if status_filter else ""
        q = f"""{{ entries(collection: "{collection}", limit: 200, page: {page}{filt}) {{
          current_page last_page total
          data {{ ... on EntryInterface {{ id }} {fields} }} }} }}"""
        d = gql(q)
        e = (d.get("data") or {}).get("entries")
        if e is None:
            raise SystemExit(f"refused: {json.dumps(d.get('errors'))[:300]}")
        rows += e["data"]
        print(f"{collection} status={status_filter} page {page}/{e['last_page']} total {e['total']}", file=sys.stderr)
        if page >= e["last_page"]:
            return rows, d.get("errors")
        page += 1
        time.sleep(0.5)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    port_fields = f"... on Entry_Portfolio_Portfolio {{ {PORTFOLIO_FIELDS} }}"
    result = {}
    for st in (None, "published", "draft", "scheduled", "expired"):
        try:
            rows, errs = pull("portfolio", port_fields, st)
        except SystemExit as e:
            print(f"status {st}: {e}", file=sys.stderr)
            continue
        result[str(st)] = {"n": len(rows), "errors": errs}
        if st is None:
            write_atomic(OUT / "portfolio.json", json.dumps(
                {"_readme": f"Every portfolio entry {EP} served (default filter), pulled {time.strftime('%Y-%m-%d')}.",
                 "rows": rows}, indent=1, ensure_ascii=False))
        elif rows:
            write_atomic(OUT / f"portfolio-{st}.json", json.dumps(
                {"_readme": f"Portfolio entries with status={st}, pulled {time.strftime('%Y-%m-%d')}.",
                 "rows": rows}, indent=1, ensure_ascii=False))
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
