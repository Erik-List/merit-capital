#!/usr/bin/env python3
"""Pull the investor's current portfolio and team from their own site's API.

Why this layer exists: the three SEC/archive layers all structurally miss recent
private companies. The modern portfolio page is JS-rendered with no per-company
URLs, so the Wayback CDX trick cannot enumerate it; and many current startups
raise under Section 4(a)(2) rather than Reg D, so they file no Form D at all.
Neither has IPO'd, so EDGAR is silent too.

The site's own CMS is the authoritative answer. The endpoint lives in the
investor's config.json under "site_api"; currently implemented: WordPress REST
(`type: "wordpress"`). The escalation ladder for any investor site, in order of
preference:
  1. WordPress REST   /wp-json/wp/v2/types -> find the post type -> paginate it
  2. Next.js          __NEXT_DATA__ script tag, or /_next/data/<build>/*.json
  3. Any SPA          watch XHR in the browser pane, then call that endpoint
  4. Last resort      render the page headless and parse the DOM

When every REST door is closed (a16z: /wp-json 404s and ?rest_route= returns
the homepage), the ladder ends at scraping the site's own rendered surfaces:
`type: "scrape"` with a "sources" list, each naming a parser strategy — the
same named-strategy-in-code, constants-in-config pattern wayback-pull.py uses:

  js_array        JSON array assigned to a JS variable in the page HTML
  li_text_list    plain <li>Name</li> entries (compliance-list page)
  paginated_json  JSON API with {count, next, results[]} pagination
  nuxt_payload    a Nuxt 2 full-static site's per-route payload.js (the
                  __NUXT_JSONP__ call that carries the CMS rows the page was
                  generated from — Contentful entries on creandum.com);
                  decoded through node, entries flattened to their fields

Output: <investor>/sources/site/companies.json, team.json

Usage: python3 scripts/site-portfolio.py <investor-slug>
"""
import argparse
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths, write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
PER_PAGE = 100


def get(url: str) -> list:
    for attempt in range(4):
        try:
            out = subprocess.run(
                ["curl", "-sf", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout
            return json.loads(out)
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            time.sleep(1.5 * (attempt + 1))
    return []


def get_text(url: str) -> str:
    for attempt in range(4):
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "90", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
        except subprocess.CalledProcessError:
            time.sleep(1.5 * (attempt + 1))
    return ""


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


# ---------------------------------------------------------------------------
# scrape parsers: one row dict per company, at minimum {"name": ...}
# ---------------------------------------------------------------------------

def parse_js_array(src: dict) -> list[dict]:
    """JSON array assigned to a JS variable inside the page HTML."""
    html = get_text(src["url"])
    m = re.search(re.escape(src["var"]) + r"\s*=\s*\[", html)
    if not m:
        sys.exit(f"js_array: variable {src['var']!r} not found at {src['url']}")
    start = m.end() - 1
    depth, i, instr, esc = 0, start, False, False
    while i < len(html):
        c = html[i]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
        else:
            if c == '"':
                instr = True
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    break
        i += 1
    return json.loads(html[start:i + 1])


def parse_li_text_list(src: dict) -> list[dict]:
    """Plain <li>Name</li> entries on a listing page."""
    html = get_text(src["url"])
    return [{"name": unescape(m).strip()}
            for m in re.findall(r"<li>([^<]+)</li>", html)
            if unescape(m).strip()]


def parse_paginated_json(src: dict) -> list[dict]:
    """JSON API paginated as {count, next, results[]}."""
    rows, url = [], src["url"]
    while url:
        d = get(url)
        if not isinstance(d, dict) or "results" not in d:
            break
        rows.extend(d["results"])
        url = d.get("next")
        time.sleep(0.4)
    return rows


def parse_regex_list(src: dict) -> list[dict]:
    """Config-supplied regex with named groups over the raw page HTML;
    every group dict becomes a row (at minimum (?P<name>...))."""
    html = get_text(src["url"])
    return [m.groupdict() for m in re.finditer(src["pattern"], html)]


def parse_file_list(src: dict) -> list[dict]:
    """Rows from a local JSON file (bare list, or {"rows": [...]}): the saved
    output of a browser-pane extraction (escalation ladder step 3) that no
    direct fetch reproduces — the file's _readme records how it was made."""
    from paths import ROOT
    data = json.loads((ROOT / src["path"]).read_text())
    return data["rows"] if isinstance(data, dict) else data


def parse_json_list(src: dict) -> list[dict]:
    """Any JSON endpoint returning the rows as an array — a headless CMS's
    own query API (Sanity GROQ, Contentful...). The query, with whatever
    projection flattens the rows, lives in the config URL; src["list_path"]
    is the dot path from the response root to the array ("result")."""
    data = get(src["url"])
    for part in [p for p in (src.get("list_path") or "").split(".") if p]:
        if not isinstance(data, dict):
            return []
        data = data.get(part) or []
    return data if isinstance(data, list) else []


def parse_card_blocks(src: dict) -> list[dict]:
    """Server-rendered listing whose cards carry an OPTIONAL field list (a
    card missing one field must not bleed a match into the next card, which
    rules out one page-wide regex). The page splits into blocks at
    src["block_start"] (regex); each named pattern in src["field_patterns"]
    is searched within its block only, missing fields stay absent. Optional:
    src["section_split"] (regex, one capture group) splits the page into
    labeled sections first, the label landing in src["section_field"];
    src["require"] ({field: [allowed values]}) drops rows failing it —
    listing pages that render another firm's rows alongside their own
    (shared-brand sites) filter on the page's own attribution attribute."""
    html = get_text(src["url"])
    sections = [(None, html)]
    if src.get("section_split"):
        parts = re.split(src["section_split"], html)
        sections = [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
    rows = []
    for label, body in sections:
        for block in re.split(src["block_start"], body)[1:]:
            row = {}
            for key, pat in src["field_patterns"].items():
                m = re.search(pat, block, re.S)
                if m:
                    row[key] = unescape(re.sub(r"\s+", " ", m.group(1))).strip()
            if not row:
                continue
            if label is not None and src.get("section_field"):
                row[src["section_field"]] = unescape(
                    re.sub(r"\s+", " ", label)).strip()
            if any(row.get(f) not in allowed
                   for f, allowed in (src.get("require") or {}).items()):
                continue
            rows.append(row)
    return rows


# A Nuxt 2 site generated with `nuxt generate` (full static mode) ships every
# route's data as /_nuxt/static/<build>/<route>/payload.js — a JSONP call
# `__NUXT_JSONP__("/route", (function(a,b,...){...}(args)))` whose argument
# table dedupes shared objects, so the graph is cyclic and needs a JS engine
# to evaluate. The homepage's window.__NUXT__ literal names the current build
# (staticAssetsBase). This is escalation-ladder step 3 for Nuxt what
# __NEXT_DATA__ is for Next.js, and it hands over the CMS rows (Contentful
# on creandum.com) with every field the page never renders.
NUXT_DECODER = r"""
const fs = require("fs");
const [,, inPath] = process.argv;
const src = fs.readFileSync(inPath, "utf8");
let captured = null;
new Function("__NUXT_JSONP__", src)((route, data) => { captured = { route, data }; });
function strip(o, path) {
  if (o === null || typeof o !== "object") return o;
  if (path.has(o)) return { $ref: (o.sys && o.sys.id) || "cycle" };
  path.add(o);
  let out;
  if (Array.isArray(o)) out = o.map((v) => strip(v, path));
  else { out = {}; for (const k of Object.keys(o)) out[k] = strip(o[k], path); }
  path.delete(o);
  return out;
}
process.stdout.write(JSON.stringify(strip(captured, new Set())));
"""


def nuxt_static_base(site_url: str) -> str:
    """The current build's static asset base (/_nuxt/static/<build>) from the
    homepage's window.__NUXT__ literal."""
    html = get_text(site_url)
    m = re.search(r'staticAssetsBase:"([^"]+)"', html)
    if m:
        return m.group(1).encode().decode("unicode_escape")
    # the SSR homepage may carry the build only in its preload links
    m = re.search(r'(/_nuxt/static/\d+)/', html)
    if not m:
        sys.exit(f"nuxt_payload: no Nuxt static build id in {site_url} (not a "
                 f"Nuxt full-static site, or the build id moved)")
    return m.group(1)


def nuxt_decode(js_text: str) -> dict:
    """{route, data} of one payload.js, via node (the only JS engine needed)."""
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "payload.js").write_text(js_text, encoding="utf-8")
        (Path(td) / "decode.js").write_text(NUXT_DECODER, encoding="utf-8")
        out = subprocess.run(["node", str(Path(td) / "decode.js"),
                              str(Path(td) / "payload.js")],
                             capture_output=True, check=True).stdout
    return json.loads(out)


def contentful_flatten(v, depth: int = 0):
    """A Contentful entry becomes its fields; nested entries beyond one level
    collapse to their name/title; assets to their file URL; rich text to
    plain text; lists map element-wise."""
    if isinstance(v, list):
        return [contentful_flatten(x, depth) for x in v]
    if not isinstance(v, dict):
        return v
    if "$ref" in v:
        return None
    if v.get("nodeType") == "document":
        return rich_text(v)
    f = v.get("fields")
    if isinstance(f, dict):
        if "file" in f and isinstance(f["file"], dict):      # asset
            url = f["file"].get("url") or ""
            return ("https:" + url) if url.startswith("//") else url
        if depth >= 1:
            return f.get("name") or f.get("title") or f.get("slug")
        return {k: contentful_flatten(x, depth + 1) for k, x in f.items()}
    return {k: contentful_flatten(x, depth + 1) for k, x in v.items()
            if k not in ("sys", "metadata")}


def rich_text(node) -> str:
    if isinstance(node, dict):
        if node.get("nodeType") == "text":
            return node.get("value", "")
        return "".join(rich_text(c) for c in node.get("content", []))
    if isinstance(node, list):
        return "".join(rich_text(c) for c in node)
    return ""


def parse_nuxt_payload(src: dict) -> list[dict]:
    """Rows of one route's payload: src["url"] is the site, src["route"] the
    page ("/commitments"), src["list_path"] the dot path from the decoded
    {route, data} to the list ("data.0.portfolios"); src["static_base"]
    pins a build instead of reading the homepage's current one."""
    site = src["url"].rstrip("/")
    base = src.get("static_base") or nuxt_static_base(site)
    route = src["route"].strip("/")
    url = f"{site}{base}/{route + '/' if route else ''}payload.js"
    js = get_text(url)
    if not js.startswith("__NUXT_JSONP__"):
        sys.exit(f"nuxt_payload: {url} is not a payload ({js[:60]!r})")
    data = nuxt_decode(js)
    for part in [p for p in (src.get("list_path") or "").split(".") if p]:
        if isinstance(data, list):
            data = data[int(part)] if part.isdigit() and int(part) < len(data) else []
        elif isinstance(data, dict):
            data = data.get(part) or []
        else:
            return []
    rows = [contentful_flatten(r) for r in (data if isinstance(data, list) else [])]
    return [r for r in rows if isinstance(r, dict)]


SCRAPE_PARSERS = {
    "js_array": parse_js_array,
    "li_text_list": parse_li_text_list,
    "paginated_json": parse_paginated_json,
    "regex_list": parse_regex_list,
    "json_list": parse_json_list,
    "file_list": parse_file_list,
    "card_blocks": parse_card_blocks,
    "nuxt_payload": parse_nuxt_payload,
}


def scrape_companies(api: dict) -> list[dict]:
    """Run every configured source, merge rows by normalized name.

    Each source entry: {parser, url, list, fields?, extras?, row_url?}.
    `fields` maps the unified keys (name, url) to the source's own key names;
    `extras` lists source keys carried through verbatim (evidence for the
    judge: outcome tags, tickers, acquirers, cohorts); `sectors` maps a source
    key whose list values union into the row's sectors. `row_url` is a
    template applied when the mapped url is empty ({slug}/{name} substituted).
    """
    def dig(rec: dict, path: str):
        """'announcement.permalink' walks nested dicts; missing -> ''."""
        cur = rec
        for part in path.split("."):
            if not isinstance(cur, dict):
                return ""
            cur = cur.get(part)
        return cur or ""

    def first_of(rec: dict, paths) -> str:
        """fields values may be a single path or a preference-ordered list."""
        for p in ([paths] if isinstance(paths, str) else paths):
            v = dig(rec, p)
            if v:
                return str(v)
        return ""

    merged: dict[str, dict] = {}
    for src in api["sources"]:
        raw = SCRAPE_PARSERS[src["parser"]](src)
        fields = src.get("fields", {})
        n = 0
        for r in raw:
            # Shape adapters, all optional and parser-agnostic: `pluck` keeps
            # one key of each dict in a list-valued field ({"leads": "name"}
            # -> ["A", "B"]); `first` replaces a list by its first element;
            # `rename` maps source keys to the unified names the build reads
            # (invest_year, partners) so no parser hard-codes a CMS schema.
            for k, sub in (src.get("pluck") or {}).items():
                if isinstance(r.get(k), list):
                    r[k] = [x.get(sub) if isinstance(x, dict) else x for x in r[k]]
                    r[k] = [x for x in r[k] if x]
            for k in src.get("first") or []:
                if isinstance(r.get(k), list):
                    r[k] = r[k][0] if r[k] else None
            for k, new in (src.get("rename") or {}).items():
                if k in r:
                    r[new] = r[k] if new not in r else r[new]
            name = unescape(first_of(r, fields.get("name", "name"))).strip()
            if not name:
                continue
            key = re.sub(r"[^a-z0-9]+", "", name.lower())
            if not key:
                continue
            row = merged.setdefault(key, {
                "name": name, "slug": slug_of(name), "sectors": [],
                "url": "", "published": "", "modified": "", "lists": []})
            url = first_of(r, fields.get("url", "url"))
            if not url and src.get("row_url"):
                url = src["row_url"].format(slug=r.get("slug", slug_of(name)),
                                            name=name)
            row["url"] = row["url"] or url
            if src.get("sectors"):
                vals = r.get(src["sectors"]) or []
                if isinstance(vals, str):
                    vals = [vals]
                row["sectors"] = sorted(set(row["sectors"]) | {
                    str(v) for v in vals if v})
            for k in src.get("extras", []):
                if r.get(k) not in (None, "", [], {}):
                    row.setdefault(k, r[k])
            if src["list"] not in row["lists"]:
                row["lists"].append(src["list"])
            n += 1
        print(f"  source {src['list']}: {n} rows")
    return sorted(merged.values(), key=lambda c: c["name"].lower())


def fetch_type(base: str, rest_base: str) -> list[dict]:
    rows, page = [], 1
    while True:
        batch = get(f"{base}/{rest_base}?per_page={PER_PAGE}&page={page}")
        if not batch:
            break
        rows.extend(batch)
        if len(batch) < PER_PAGE:
            break
        page += 1
        time.sleep(0.3)
    return rows


def categories_from(class_list) -> list[str]:
    return sorted({c[len("category-"):] for c in (class_list or [])
                   if c.startswith("category-")})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    args = ap.parse_args()

    p = Paths(args.investor)
    api = p.config()["site_api"]
    p.site.mkdir(parents=True, exist_ok=True)

    if api.get("type") == "scrape":
        companies = scrape_companies(api)
        write_atomic(p.site / "companies.json", json.dumps(companies, indent=1) + "\n")
        from collections import Counter
        lists = Counter(li for c in companies for li in c["lists"])
        print(f"companies: {len(companies)} (union)   per list: {dict(lists)}")
        print("  sample:", [c["name"] for c in companies[:6]])
        # Team through the same machinery, when the CMS carries people too
        # (roster.site_team_groups then filters on each row's "group" extra).
        if api.get("team_sources"):
            team = scrape_companies({"sources": api["team_sources"]})
            write_atomic(p.site / "team.json", json.dumps(team, indent=1) + "\n")
            groups = Counter(t.get("group") or "?" for t in team)
            print(f"team members: {len(team)}   groups: {dict(groups)}")
        return

    if api.get("type") != "wordpress":
        sys.exit(f"site_api type {api.get('type')!r} not implemented; see the "
                 f"escalation ladder in this script's docstring")

    raw = fetch_type(api["base"], api["company_type"])
    companies = [{
        "name": unescape(c["title"]["rendered"]).strip(),
        "slug": c["slug"],
        "sectors": categories_from(c.get("class_list")),
        "url": c.get("link"),
        "published": (c.get("date") or "")[:10],
        "modified": (c.get("modified") or "")[:10],
    } for c in raw if c.get("title", {}).get("rendered")]
    companies.sort(key=lambda c: c["name"].lower())
    write_atomic(p.site / "companies.json", json.dumps(companies, indent=1) + "\n")

    team = fetch_type(api["base"], api["team_type"])
    people = [{
        "name": unescape(t["title"]["rendered"]).strip(),
        "slug": t["slug"],
        "url": t.get("link"),
    } for t in team if t.get("title", {}).get("rendered")]
    people.sort(key=lambda p_: p_["name"].lower())
    write_atomic(p.site / "team.json", json.dumps(people, indent=1) + "\n")

    from collections import Counter
    sect = Counter(s for c in companies for s in c["sectors"])
    print(f"companies: {len(companies)}   team members: {len(people)}")
    print("  top sectors:", dict(sect.most_common(8)))
    print("  sample:", [c["name"] for c in companies[:6]])


if __name__ == "__main__":
    main()
