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
  search_index    a hosted search index (Algolia) standing in for a
                  portfolio API: POST {params} -> {hits, nbHits, nbPages},
                  paged per facet slice so a book larger than the index's
                  deep-pagination cap is still enumerable (YC's directory)
  nuxt_payload    a Nuxt 2 full-static site's per-route payload.js (the
                  __NUXT_JSONP__ call that carries the CMS rows the page was
                  generated from — Contentful entries on creandum.com);
                  decoded through node, entries flattened to their fields

Output: <investor>/sources/site/companies.json, team.json (every team row carries
        cms_title, role_bucket, linkedin_url, x_url, socials_source: the profile
        builder's fields)

Usage: python3 scripts/site-portfolio.py <investor-slug>
       python3 scripts/site-portfolio.py <investor-slug> --socials-only
         re-read the people's social links only (PRO-154): team.json keeps its
         rows, the links land on investor.json, the audit in team-socials.json
"""
import argparse
import json
import re
import subprocess
import sys
import time
from html import unescape
from collections import Counter
from urllib.parse import quote, urljoin
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths, write_atomic  # noqa: E402
from people_common import clean_social, firm_handles, handle_score, social_handle  # noqa: E402

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


def get_page(url: str) -> str:
    """A member's profile page: "" at once on a 4xx (First Round's /team/
    links all 404, and get_text's four retries cost 15s each), one retry on a
    network error or 5xx."""
    for attempt in range(2):
        out = subprocess.run(
            ["curl", "-sL", "--max-time", "60", "-H", f"User-Agent: {UA}",
             "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = out.stdout.decode("utf-8", errors="replace").rpartition("\n")
        if code.startswith("2"):
            return body
        if code.startswith("4"):
            return ""
        time.sleep(2 * (attempt + 1))
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


def parse_search_index(src: dict) -> list[dict]:
    """A hosted search index (Algolia) standing in for a portfolio API.

    Why it is its own strategy: `paginated_json` expects {count, next,
    results[]} and a search index answers {hits[], nbHits, nbPages} to a POST
    carrying its own params; and every such index caps deep pagination
    (Algolia's paginationLimitedTo, 1000 hits by default), so a book larger
    than the cap can never be read by paging the unfiltered query. The fix is
    to slice: page the index once per value of a facet whose buckets all sit
    under the cap (YC: `batch`, 50 values, largest 398 of 6,203), and union.

    Config: {url, app_id, api_key, index, slice_facet, params?, snapshot?}.
    `slice_facet` is optional — without it the plain query is paged, which is
    correct for any index under the cap. `snapshot` is a repo-relative path;
    the raw payload is written there so the run is reproducible without the
    live index, and re-read on a later run when the index is unreachable.
    The credentials are the ones the public page ships to every visitor; this
    reads the same rows an anonymous browser is served, no more.
    """
    from paths import ROOT
    url = src["url"]
    headers = ["-H", f"X-Algolia-Application-Id: {src['app_id']}",
               "-H", f"X-Algolia-API-Key: {src['api_key']}",
               "-H", "Content-Type: application/json",
               "-H", f"User-Agent: {UA}"]

    def query(params: str) -> dict:
        body = json.dumps({"params": params})
        for attempt in range(4):
            try:
                out = subprocess.run(
                    ["curl", "-sf", "--max-time", "60", "-X", "POST", url,
                     *headers, "-d", body],
                    capture_output=True, check=True).stdout
                return json.loads(out)
            except (subprocess.CalledProcessError, json.JSONDecodeError):
                time.sleep(1.5 * (attempt + 1))
        raise SystemExit(f"search index unreachable: {url} ({params[:80]})")

    base = src.get("params", "hitsPerPage=1000")
    facet = src.get("slice_facet")
    slices = [""]
    if facet:
        probe = query(f"query=&hitsPerPage=1&page=0&maxValuesPerFacet=1000"
                      f"&facets=%5B%22{facet}%22%5D")
        buckets = probe.get("facets", {}).get(facet, {})
        total = probe.get("nbHits", 0)
        if not buckets:
            raise SystemExit(f"slice_facet {facet!r} is not a facet of the index")
        over = {k: v for k, v in buckets.items() if v >= 1000}
        if over:
            raise SystemExit(f"slice_facet {facet!r} has buckets at/over the "
                             f"pagination cap: {over} — slice on a finer facet")
        slices = [f"&facetFilters=%5B%22{facet}%3A{quote(k)}%22%5D"
                  for k in sorted(buckets)]
        print(f"  index: {total} hits across {len(slices)} {facet} slices")

    rows, seen = [], set()
    for i, sl in enumerate(slices, 1):
        page = 0
        while True:
            d = query(f"query=&{base}&page={page}{sl}")
            hits = d.get("hits", [])
            for h in hits:
                oid = h.get("objectID") or h.get("id")
                if oid in seen:
                    continue
                seen.add(oid)
                rows.append(h)
            page += 1
            if page >= d.get("nbPages", 1) or not hits:
                break
            time.sleep(0.25)
        if i % 10 == 0 or i == len(slices):
            print(f"  slice {i}/{len(slices)}: {len(rows)} rows")
        time.sleep(0.25)

    if src.get("snapshot"):
        dest = ROOT / src["snapshot"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(dest, json.dumps({
            "_readme": (f"Raw {src['index']} hits, pulled {time.strftime('%Y-%m-%d')} "
                        f"from {url} with the public app id and search-only key the "
                        f"directory page ships to every visitor. Paged per "
                        f"{facet or 'query'} slice to stay under the index's deep-"
                        f"pagination cap. Snapshot so the run is reproducible."),
            "pulled": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "index": src["index"], "count": len(rows), "rows": rows},
            indent=1, ensure_ascii=False))
        print(f"  snapshot -> {src['snapshot']} ({len(rows)} rows)")
    return rows


SCRAPE_PARSERS = {
    "js_array": parse_js_array,
    "li_text_list": parse_li_text_list,
    "paginated_json": parse_paginated_json,
    "regex_list": parse_regex_list,
    "json_list": parse_json_list,
    "file_list": parse_file_list,
    "card_blocks": parse_card_blocks,
    "nuxt_payload": parse_nuxt_payload,
    "search_index": parse_search_index,
}


# ---------------------------------------------------------------------------
# team shaping: the profile builder's fields on every team row (PRO-113)
# ---------------------------------------------------------------------------

BUCKETS = ("investing", "operations", "platform", "finance", "advisor",
           "emeritus", "eir", "founder", "other")
TITLE_KEYS = ("cms_title", "title", "role", "jobPosition", "role_display", "position")
# Title rules, for sites that publish no team group. First match wins; a site
# with groups never reaches these (an unmapped group means: do not publish).
TITLE_RULES = [
    (r"emeritus", "emeritus"),
    (r"entrepreneur.in.residence|\beir\b", "eir"),
    (r"advis", "advisor"),
    (r"\b(cfo|coo|financ|controller|accounting|legal|counsel|compliance|"
     r"investor relations|tax|fund admin)", "finance"),
    (r"platform|talent|community|marketing|communications|comms|brand|content|"
     r"events|people|\bhr\b|recruit|portfolio (support|services)|founder (success|"
     r"experience)|network|editor|media|design|engineer|\bit\b|office|assistant|"
     r"chief of staff|operations|operating", "operations"),
    (r"investment team|general partner|managing (partner|director)|\bpartner\b|"
     r"principal|associate|analyst|investor|venture|scout|fellow|\bvp\b|"
     r"vice president|director|president|founder|ceo|chairman", "investing"),
]
# Every LinkedIn or X profile link on a page, escaped JSON included (Greylock's
# pages carry them as "https:\/\/www.linkedin.com\/in\/chandna\").
PAGE_LINKS = re.compile(
    r"https?://(?:[a-z]{2,3}\.)?linkedin\.com/(?:in|pub)/[^\"'\s<>?#\\]+"
    r"|https?://(?:www\.|mobile\.)?(?:twitter|x)\.com/@?[A-Za-z0-9_]{1,15}(?![A-Za-z0-9_])",
    re.I)
# Keys a CMS row may carry a person's links under.
# Creandum keeps the LinkedIn address in `websiteLink`.
SOCIAL_KEYS = ("linkedin_url", "linkedin", "x_url", "twitter", "twitterLink", "websiteLink",
               "socials")


def norm_name(name: str) -> str:
    return re.sub(r"[^a-z]", "", (name or "").lower())


def title_bucket(title: str | None) -> str | None:
    t = (title or "").lower()
    for rx, bucket in TITLE_RULES:
        if re.search(rx, t):
            return bucket
    return None


def bucket_of(row: dict, api: dict) -> list[str]:
    """The row's role bucket(s): the per-person override by name (an empty list
    means "do not publish"), else nothing if a `team_exclude_keys` key is set on
    the row, else the site group through `team_buckets`, else (only when the
    site has no groups) the title rules. Values outside BUCKETS are dropped."""
    over = {norm_name(k): v for k, v in (api.get("team_bucket_overrides") or {}).items()}
    key = norm_name(row.get("name"))
    if key in over:
        b = over[key]                       # [] is a judgement call: do not publish
    elif any(row.get(k) for k in api.get("team_exclude_keys") or []):
        b = None                            # e.g. a CMS "archived" flag
    elif row.get("group") or row.get("section"):
        b = (api.get("team_buckets") or {}).get(row.get("group") or row.get("section"))
    else:
        b = title_bucket(row.get("cms_title"))
    return [x for x in ([b] if isinstance(b, str) else (b or [])) if x in BUCKETS]


SOCIAL_HOST = re.compile(r"^https?://([a-z]{2,3}\.|www\.|mobile\.)?(linkedin|twitter|x)\.com/", re.I)


def page_url(row: dict, site_base: str) -> str:
    """The member's own profile page: absolute as given, or a site-relative
    path resolved against the site (YC's "/people/garry-tan"). A LinkedIn or
    X address in the url slot is the person's link, not a page to read: a
    LinkedIn page lists other people (Creandum). Anything else there
    (Benchmark keeps a note) is not a page."""
    u = (row.get("url") or "").strip()
    if SOCIAL_HOST.match(u):
        return ""
    if u.startswith("http"):
        return u
    if u.startswith("/") and site_base:
        return urljoin(site_base, u)
    return ""


def read_socials(rows: list[dict], api: dict, fetch: bool, site_base: str = "",
                 firm: tuple[str, str] = ("", "")) -> dict:
    """Set linkedin_url, x_url and socials_source on every row; return the
    audit (each person's candidates and the one chosen), PRO-154.

    Candidates come from the CMS row's own fields, from the member's own page,
    and, for a row carried over from an earlier pull (`_legacy`), from the
    links it already had. The rules (COLLECTION.md §11, People's social links):
      - an account named for the firm (`firm_handles`, plus
        `site_api.team_social_exclude`) is nobody's;
      - a CMS field is the person's, unless the CMS gives the same account to
        two or more people (8VC filled @8vc for everyone);
      - a link read off a page, or carried over, must name the person
        (`handle_score` > 0) and goes to nobody when another member of the
        firm matches it as well or better (a colleague quoted on the page);
      - `site_api.team_social_overrides` ({name: {linkedin_url, x_url}}, null
        for none) records a reviewed answer and wins."""
    exclude = {h.lower().lstrip("@") for h in api.get("team_social_exclude") or []}
    exclude |= firm_handles(*firm)
    overrides = {norm_name(k): v for k, v in (api.get("team_social_overrides") or {}).items()}
    cands = []
    for r in rows:
        c: dict[str, list[tuple[str, str]]] = {"linkedin": [], "x": []}

        def add(url, source):
            """One candidate per account: the first spelling seen is kept (the
            published one is added first, so a page's "www.twitter.com" does
            not churn it), and a CMS sighting makes it a CMS link."""
            u = str(url or "")
            kind = ("linkedin" if "linkedin.com" in u.lower() else
                    "x" if re.search(r"(twitter|x)\.com", u, re.I) else None)
            clean = clean_social(kind, u) if kind else ""
            if not clean:
                return
            h = social_handle(kind, clean)
            for i, (x, s) in enumerate(c[kind]):
                if social_handle(kind, x) == h:
                    if source == "cms":
                        c[kind][i] = (x, "cms")
                    return
            c[kind].append((clean, source))

        legacy = r.pop("_legacy", False)
        for v in r.pop("_legacy_links", None) or []:
            add(v, "legacy")
        for key in SOCIAL_KEYS + ("url",):
            vals = r.get(key)
            vals = list(vals.values()) if isinstance(vals, dict) else \
                vals if isinstance(vals, list) else [vals]
            for v in vals:
                if key == "url" and not SOCIAL_HOST.match(str(v or "")):
                    continue
                add(v, "legacy" if legacy and key in ("linkedin_url", "x_url") else "cms")
        page = page_url(r, site_base) if r.get("role_bucket") else ""
        if fetch and page:                   # unpublished rows need no page read
            html = get_page(page).replace("\\/", "/")
            time.sleep(0.5)
            for m in PAGE_LINKS.finditer(html):
                add(m.group(0), "page")
        cands.append(c)

    def flat(h):
        return re.sub(r"[^a-z0-9]", "", h)

    cms_seen = {k: Counter(h for c in cands for h in {social_handle(k, u) for u, s in c[k]
                                                      if s == "cms"})
                for k in ("linkedin", "x")}
    # (kind, handle) -> [best score among the members whose candidates carry it,
    # how many members reach it]: a link goes to its one best match, or nobody.
    best: dict[tuple, list[int]] = {}
    for r, c in zip(rows, cands):
        for kind in ("linkedin", "x"):
            for u, _ in c[kind]:
                h = social_handle(kind, u)
                sc = handle_score(h, r["name"])
                b = best.setdefault((kind, h), [0, 0])
                if sc > b[0]:
                    best[kind, h] = [sc, 1]
                elif sc == b[0] and sc:
                    b[1] += 1

    audit = {}
    for r, c in zip(rows, cands):
        over = overrides.get(norm_name(r["name"]), {})
        sources, entry = {}, {}
        for kind in ("linkedin", "x"):
            key = f"{kind}_url"
            if key in over:
                value = clean_social(kind, over[key]) if over[key] else ""
                source = "override" if value else None
            else:
                scored = []
                for u, s in c[kind]:
                    h = social_handle(kind, u)
                    if flat(h) in exclude:
                        continue
                    if s == "cms":
                        if cms_seen[kind][h] < 2:
                            scored.append((0, 9, u, s))
                        continue
                    score = handle_score(h, r["name"])
                    if score and best[kind, h] == [score, 1]:
                        # at equal strength the published link stays (Sequoia's
                        # Shaun Maguire has two LinkedIn addresses)
                        scored.append((1, -score if s == "legacy" else -score + 0.5, u, s))
                pick = min(scored) if scored else None
                value, source = (pick[2], pick[3]) if pick else ("", None)
            r[key] = value
            sources[kind] = source
            entry[kind] = {"chosen": value or None, "source": source,
                           "candidates": [f"{s}: {u}" for u, s in c[kind]]}
        r["socials_source"] = sources
        audit[r["name"]] = entry
    return audit


def shape_team(rows: list[dict], api: dict, fetch: bool, site_base: str = "",
               firm: tuple[str, str] = ("", "")) -> list[dict]:
    """Every team row gains cms_title, role_bucket, linkedin_url, x_url and
    socials_source."""
    for r in rows:
        r["cms_title"] = next((str(r[k]).strip() for k in
                               api.get("team_title_keys") or TITLE_KEYS if r.get(k)), "")
        r["role_bucket"] = bucket_of(r, api)
    read_socials(rows, api, fetch, site_base, firm)
    return rows


def scrape_companies(api: dict) -> list[dict]:
    """Run every configured source, merge rows by normalized name.

    Each source entry: {parser, url, list, fields?, extras?, row_url?,
    key_field?}.
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
            # Identity is the source's own id where the source has one. The
            # normalized name is the default because most portfolio pages
            # publish nothing else, but a name is not an identity at scale:
            # YC's directory carries 89 names borne by two different
            # companies in different batches (Parse S11 the Facebook-acquired
            # backend vs Parse F25; Struct W23 vs Struct F24), and keying on
            # the name silently merged 100 real companies into 89 rows.
            # `key_field` names the source key that is the identity instead.
            key = ""
            if src.get("key_field"):
                key = str(r.get(src["key_field"]) or "").strip().lower()
            if not key:
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


def firm_of(p: Paths) -> tuple[str, str]:
    """(published firm name, slug), for telling the firm's own account apart."""
    name = json.loads(p.investor.read_text()).get("name", "") if p.investor.exists() else ""
    return name, p.root.name


def dump_like(path: Path, data) -> None:
    """Write JSON in the file's existing style (indent, escaped or raw
    non-ASCII), so a change of a few values does not rewrite every line."""
    old = path.read_text() if path.exists() else ""
    indent = next((len(l) - len(l.lstrip(" ")) for l in old.splitlines()[1:]
                   if l.startswith(" ")), 2)
    raw = any(ord(ch) > 127 for ch in old)
    write_atomic(path, json.dumps(data, indent=indent, ensure_ascii=not raw)
                 + ("\n" if old.endswith("\n") or not old else ""))


def socials_only(p: Paths, api: dict, fetch: bool, site_base: str) -> None:
    """Re-read the links of the people already in team.json, without adding or
    dropping anyone (PRO-154), then carry them onto the published people in
    investor.json and its sidecar, matched by name. Where the site's CMS lists
    the team, its rows are re-fetched for their own link fields; a row the CMS
    no longer lists, or a team built without a CMS, keeps its old links as
    `legacy` candidates, which must match the name like a page read."""
    team = json.loads(p.team.read_text())
    fresh = {}
    if api.get("team_sources"):
        fresh = {norm_name(t["name"]): t
                 for t in scrape_companies({"sources": api["team_sources"]})}
    for r in team:
        f = fresh.get(norm_name(r["name"]))
        if f is None:
            r["_legacy"] = True
            continue
        # The links this row carried stay in play as `legacy` candidates, so a
        # page that moved (Khosla's /team/ pages now 404) loses nothing that
        # still names the person.
        r["_legacy_links"] = [r.get("linkedin_url"), r.get("x_url")]
        for k in SOCIAL_KEYS:
            r.pop(k, None)
            if k in f:
                r[k] = f[k]
        if f.get("url"):
            r["url"] = f["url"]                # the page as the CMS lists it today
    audit = read_socials(team, api, fetch, site_base, firm_of(p))
    write_atomic(p.team, json.dumps(team, indent=1) + "\n")
    write_atomic(p.site / "team-socials.json", json.dumps(audit, indent=1) + "\n")

    by_name = {norm_name(t["name"]): t for t in team}
    row = json.loads(p.investor.read_text())
    src = json.loads(p.investor_sources.read_text())
    changed = 0
    for person in row.get("individuals") or []:
        t = by_name.get(norm_name(person["name"]))
        if t is None:
            continue
        new = {"linkedin_url": t.get("linkedin_url") or None, "x_url": t.get("x_url") or None}
        changed += (person.get("socials") or {}) != new
        person["socials"] = new
    field = src.get("fields", {}).get("individuals")
    if field is not None:
        field["value"] = row.get("individuals")
        people = row.get("individuals") or []
        note = (f"Social links re-read under PRO-154 ({time.strftime('%Y-%m-%d')}): "
                f"{sum(1 for q in people if q['socials']['linkedin_url'])} LinkedIn, "
                f"{sum(1 for q in people if q['socials']['x_url'])} X; a link read off a "
                f"page counts only when its account matches the person's name, and an "
                f"account on two or more people's pages is the firm's.")
        basis = re.sub(r"\s*Social links re-read under PRO-154 .*$", "", field.get("basis") or "")
        field["basis"] = (basis + " " + note).strip()
    dump_like(p.investor, row)
    dump_like(p.investor_sources, src)
    have = sum(1 for t in team if t.get("role_bucket") and (t.get("linkedin_url") or t.get("x_url")))
    print(f"socials: {have} of {sum(1 for t in team if t.get('role_bucket'))} published "
          f"members carry a link; {changed} published people changed")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    ap.add_argument("--no-fetch-profiles", action="store_true",
                    help="skip the per-member profile-page fetch for socials")
    ap.add_argument("--socials-only", action="store_true",
                    help="re-read the links of the people already recorded, and "
                         "carry them onto investor.json; nobody is added or dropped")
    args = ap.parse_args()
    fetch = not args.no_fetch_profiles

    p = Paths(args.investor)
    cfg = p.config()
    api = cfg["site_api"]
    site_base = api.get("base") or (cfg.get("wayback") or {}).get("site_url_base") or ""
    p.site.mkdir(parents=True, exist_ok=True)
    if args.socials_only:
        socials_only(p, api, fetch, site_base)
        return

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
            team = shape_team(scrape_companies({"sources": api["team_sources"]}), api, fetch,
                              site_base, firm_of(p))
            write_atomic(p.team, json.dumps(team, indent=1) + "\n")
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
    write_atomic(p.team, json.dumps(shape_team(people, api, fetch, site_base, firm_of(p)),
                                        indent=1) + "\n")

    from collections import Counter
    sect = Counter(s for c in companies for s in c["sectors"])
    print(f"companies: {len(companies)}   team members: {len(people)}")
    print("  top sectors:", dict(sect.most_common(8)))
    print("  sample:", [c["name"] for c in companies[:6]])


if __name__ == "__main__":
    main()
