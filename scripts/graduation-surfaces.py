#!/usr/bin/env python3
"""The publisher surfaces behind a graduation verdict (COLLECTION.md §6, PRO-132).

A Seed row past the censoring window with no evidence of a later round did not
graduate (Erik, 2026-09-17), and the column says so rather than abstaining. That
turns absence into a finding, and a finding needs a record: which surfaces were
searched, for what, on what date, and what they showed. This layer makes that
record mechanical, so every judge searches the same surfaces the same way and a
"no" can name them.

    python3 scripts/graduation-surfaces.py <investor>            # open Seed rows
    python3 scripts/graduation-surfaces.py <investor> --all-seed # every Seed row
    python3 scripts/graduation-surfaces.py <investor> --slugs a,b
    python3 scripts/graduation-surfaces.py decode <google-news-id-or-url>

Per row it queries four surfaces (five outside the US) and writes the investor's
scratch/graduation-surfaces.json:

  googlenews       Google News search: the company's name with round and exit
                   words. The widest press index that answers scripted queries.
  googlenews_firm  Google News search: the company's name with the firm's name,
                   which finds the seed announcement and any post of the firm's.
  techcrunch       TechCrunch's own search (its WordPress API), 2005 on.
  crunchbase_news  Crunchbase News's own search (its WordPress API), 2017 on.
                   The vendor's NEWS arm reporting a round is press (Rule A);
                   its database pages are not, and are never a surface here.
  googlenews_local For a company outside the US, Google News in the company's
                   own edition and language (sv-SE, de-DE, fr-FR, ...) with the
                   round words its home press uses. A round reported only at
                   home is invisible to the English searches above.

Recorded nos stay targets on every run, so a re-run is also a re-check.

It also carries what sibling investors already established for the same
company (a decided graduation with its citation, a cited entry stage), because
a row two books share should not be searched twice or decided two ways.

Three outcomes per surface, never two (the absence-vs-failure class, five
instances in this pipeline): `ok` with the items found, `ok` with none (a
2xx that genuinely held nothing), and `error` (anything else). An error is
never stored as an empty result; a re-run retries it. General web engines were
measured and refused for bulk use on 2026-09-20: DuckDuckGo serves a captcha,
Brave answers five queries and then 429s for minutes, and Bing serves
unrelated results to a scripted client. The judge's own web search remains
available for the rows these surfaces leave open.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import threading
import urllib.parse
from datetime import date
from email.utils import parsedate_to_datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import INVESTORS, Paths, write_atomic          # noqa: E402
from shared_throttle import wait                          # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
# Machine-wide request rates per service. Google News took twelve queries at
# one per second without a refusal; the WordPress APIs are lighter still.
RATES = {"googlenews": 1.0, "techcrunch": 2.0, "crunchbase_news": 2.0}

# The firm's name as the press writes it, for the second Google News query.
# A book missing here falls back to investor.json's name.
FIRM_TERMS = {
    "a16z": '("Andreessen Horowitz" OR a16z)',
    "accel": '"Accel"',
    "8vc": '"8VC"',
    "battery-ventures": '"Battery Ventures"',
    "benchmark": '"Benchmark Capital" OR "Benchmark"',
    "cherry": '"Cherry Ventures"',
    "creandum": '"Creandum"',
    "felicis": '"Felicis"',
    "first-round-capital": '"First Round"',
    "greylock": '"Greylock"',
    "khosla-ventures": '"Khosla"',
    "lightspeed": '"Lightspeed"',
    "lux-capital": '"Lux Capital"',
    "menlo-ventures": '"Menlo Ventures"',
    "redpoint-ventures": '"Redpoint"',
    "sequoia-capital": '"Sequoia"',
    "spark-capital": '"Spark Capital"',
    "thrive-capital": '"Thrive Capital"',
    "union-square-ventures": '("Union Square Ventures" OR USV)',
}

ROUND_WORDS = ('raises OR raised OR funding OR seed OR "series a" OR "series b" '
               'OR acquired OR acquires OR "shuts down"')
# Legal suffixes that never appear in a headline about the company.
SUFFIX_RE = re.compile(r"[,\s]+(inc|inc\.|incorporated|llc|l\.l\.c\.|ltd|ltd\.|limited|"
                       r"corp|corp\.|corporation|co\.|gmbh|ag|ab|as|a/s|bv|b\.v\.|sa|"
                       r"s\.a\.|sas|srl|plc|pte|oy)\s*$", re.I)
ROUND_RE = re.compile(
    r"\b(pre-?seed|seed(?:\s+(?:round|funding|extension))?|series\s+[a-h]\b(?:\+|-\d)?|"
    r"growth round|bridge|ipo|goes public|acqui(?:red|res|sition)|buys|merges?|"
    r"shut(?:s|ting)? down|shutters|closes? (?:its )?doors|bankrupt\w*|insolven\w*|"
    # the home-market press's round words (googlenews_local)
    r"finanzierungsrunde|finanzierung|finansiering|investering|rahoitus|levée|lève|"
    r"financiering|financiación|finanziamento|s[ée]rie [a-h]\b|übernahme|übernimmt|"
    r"förvärv|opkøb|konkurs|insolvenz)", re.I)
AMOUNT_RE = re.compile(r"(?:US)?\$\s?\d+(?:[.,]\d+)?\s?(?:m|mn|million|b|bn|billion|k)\b"
                       r"|€\s?\d+(?:[.,]\d+)?\s?(?:m|mn|million|b|bn|billion)\b"
                       r"|\b\d+(?:[.,]\d+)?\s?(?:million|billion|mio\.?|millionen|miljoner|"
                       r"millioner|miljoonaa|millions|miljoen|millones|milioni|milhões|mrd\.?|"
                       r"milliarden)\b", re.I)


def clean_name(name: str) -> str:
    # Typographic quotes and dashes break TechCrunch's search outright (it
    # answers "It’s Good" with an empty non-JSON body) and match nothing a
    # headline would spell with the plain ones.
    n = (name or "").translate(str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"',
                                              "–": "-", "—": "-"}))
    n = re.sub(r"\s*\((?:formerly|fka|f/k/a|now)[^)]*\)", "", n, flags=re.I)
    prev = None
    while prev != n:
        prev, n = n, SUFFIX_RE.sub("", n).strip()
    return n.strip(" .,")


def curl(url: str, data: str | None = None, headers: tuple = ()) -> tuple[int, str]:
    """(http status, body). Status 0 is a transport failure: unknown, never empty."""
    cmd = ["curl", "-s", "-L", "--max-time", "25", "-A", UA,
           "-H", "Accept-Language: en-US,en;q=0.9", "-w", "\n%{http_code}"]
    for h in headers:
        cmd += ["-H", h]
    if data is not None:
        cmd += ["--data-binary", data]
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=40)
    except subprocess.TimeoutExpired:
        return 0, ""
    body, _, code = r.stdout.rpartition("\n")
    return (int(code) if code.isdigit() else 0), body


def tags(text: str) -> tuple[list[str], list[str]]:
    rounds = sorted({m.group(1).lower() for m in ROUND_RE.finditer(text or "")})
    amounts = sorted({m.group(0) for m in AMOUNT_RE.finditer(text or "")})
    return rounds, amounts


def names_company(text: str, name: str) -> bool:
    return bool(re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", text or "", re.I))


def googlenews(query: str, name: str, hl: str = "en-US", gl: str = "US") -> dict:
    wait("googlenews", RATES["googlenews"])
    lang = hl.split("-")[0]
    url = ("https://news.google.com/rss/search?q=" + urllib.parse.quote(query)
           + f"&hl={hl}&gl={gl}&ceid={gl}:{lang}")
    code, body = curl(url)
    if code != 200 or "<rss" not in body[:500]:
        return {"status": "error", "query": query, "http": code}
    items = []
    for it in re.findall(r"<item>(.*?)</item>", body, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        g = re.search(r"articles/([^?<]+)", it)
        title = html.unescape(t.group(1)) if t else ""
        try:
            day = parsedate_to_datetime(d.group(1)).date().isoformat() if d else None
        except (TypeError, ValueError):
            day = None
        rounds, amounts = tags(title)
        items.append({"date": day, "title": title,
                      "source": html.unescape(s.group(1)) if s else None,
                      "gid": g.group(1) if g else None,
                      "names": names_company(title, name),
                      "rounds": rounds, "amounts": amounts})
    items.sort(key=lambda i: i["date"] or "")
    return {"status": "ok", "query": query, "n": len(items), "items": items}


def wordpress(service: str, base: str, name: str) -> dict:
    wait(service, RATES[service])
    url = (f"{base}/wp-json/wp/v2/posts?search={urllib.parse.quote(name)}"
           f"&per_page=30&_fields=date,link,title,excerpt")
    code, body = curl(url)
    if code != 200:
        return {"status": "error", "query": name, "http": code}
    try:
        posts = json.loads(body)
    except ValueError:
        return {"status": "error", "query": name, "http": code, "why": "not json"}
    if not isinstance(posts, list):
        return {"status": "error", "query": name, "http": code, "why": "not a list"}
    items = []
    for p in posts:
        title = html.unescape(re.sub(r"<[^>]+>", "", (p.get("title") or {}).get("rendered", "")))
        exc = html.unescape(re.sub(r"<[^>]+>", " ", (p.get("excerpt") or {}).get("rendered", "")))
        exc = re.sub(r"\s+", " ", exc).strip()[:300]
        rounds, amounts = tags(f"{title} {exc}")
        items.append({"date": (p.get("date") or "")[:10] or None, "title": title,
                      "link": p.get("link"), "excerpt": exc,
                      "names": names_company(f"{title} {exc}", name),
                      "rounds": rounds, "amounts": amounts})
    items.sort(key=lambda i: i["date"] or "")
    return {"status": "ok", "query": name, "n": len(items), "items": items}


# The company's home-market press, for a company outside the US. Google News
# searched in English misses a Nordic or German round reported only at home
# (the first PRO-132 pass on Creandum found a quarter of its nos resting on
# English surfaces alone), so a non-US row is also searched in its own
# edition, with the round words its press uses.
LOCAL_EDITIONS = {
    "SE": ("sv", "SE", 'finansiering OR investering OR miljoner OR "Series A" OR "Series B"'),
    "DK": ("da", "DK", 'investering OR kapital OR millioner OR "Series A" OR "Series B"'),
    "FI": ("fi", "FI", 'rahoitus OR sijoitus OR miljoonaa OR "Series A" OR "Series B"'),
    "NO": ("no", "NO", 'finansiering OR investering OR millioner OR "Series A" OR "Series B"'),
    "DE": ("de", "DE", 'Finanzierung OR Finanzierungsrunde OR Millionen OR "Series A" OR "Series B"'),
    "AT": ("de", "AT", 'Finanzierung OR Finanzierungsrunde OR Millionen OR "Series A" OR "Series B"'),
    "CH": ("de", "CH", 'Finanzierung OR Finanzierungsrunde OR Millionen OR "Series A" OR "Series B"'),
    "FR": ("fr", "FR", 'levée OR lève OR millions OR "série A" OR "Series A" OR "série B"'),
    "NL": ("nl", "NL", 'investering OR financiering OR miljoen OR "Series A" OR "Series B"'),
    "BE": ("fr", "BE", 'levée OR lève OR millions OR "série A" OR "Series A" OR "série B"'),
    "ES": ("es", "ES", 'ronda OR financiación OR millones OR "serie A" OR "Series A"'),
    "IT": ("it", "IT", 'round OR finanziamento OR milioni OR "serie A" OR "Series A"'),
    "PT": ("pt-PT", "PT", 'ronda OR investimento OR milhões OR "série A" OR "Series A"'),
    "BR": ("pt-BR", "BR", 'rodada OR investimento OR milhões OR "série A" OR "Series A"'),
    "GB": ("en", "GB", ROUND_WORDS),
    "IE": ("en", "IE", ROUND_WORDS),
    "IN": ("en", "IN", ROUND_WORDS),
    "IL": ("en", "IL", ROUND_WORDS),
    "CA": ("en", "CA", ROUND_WORDS),
    "AU": ("en", "AU", ROUND_WORDS),
    "SG": ("en", "SG", ROUND_WORDS),
}


def googlenews_local(name: str, country: str | None) -> dict | None:
    ed = LOCAL_EDITIONS.get((country or "").upper())
    if not ed:
        return None
    hl, gl, words = ed
    return googlenews(f'"{name}" ({words})', name, hl=hl, gl=gl)


SURFACES = {
    "googlenews": lambda n, firm: googlenews(f'"{n}" ({ROUND_WORDS})', n),
    "googlenews_firm": lambda n, firm: googlenews(f'"{n}" {firm}', n),
    "techcrunch": lambda n, firm: wordpress("techcrunch", "https://techcrunch.com", n),
    "crunchbase_news": lambda n, firm: wordpress("crunchbase_news",
                                                 "https://news.crunchbase.com", n),
}


def decode(gid: str) -> str | None:
    """A Google News article id -> the publisher's own URL (the citation)."""
    gid = re.sub(r"^.*/articles/", "", gid).split("?")[0]
    wait("googlenews", RATES["googlenews"])
    code, page = curl(f"https://news.google.com/rss/articles/{gid}?oc=5&hl=en-US&gl=US&ceid=US:en")
    sg = re.search(r'data-n-a-sg="([^"]+)"', page)
    ts = re.search(r'data-n-a-ts="([^"]+)"', page)
    if code != 200 or not (sg and ts):
        return None
    inner = ["garturlreq", [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1,
                             None, None, None, None, None, 0, 1],
                            "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
             gid, int(ts.group(1)), sg.group(1)]
    body = urllib.parse.urlencode(
        {"f.req": json.dumps([[["Fbv4je", json.dumps(inner), None, "generic"]]])})
    wait("googlenews", RATES["googlenews"])
    code, resp = curl("https://news.google.com/_/DotsSplashUi/data/batchexecute", data=body,
                      headers=("Content-Type: application/x-www-form-urlencoded;charset=UTF-8",))
    m = re.search(r'\[\\"garturlres\\",\\"(.*?)\\"', resp)
    return m.group(1).encode().decode("unicode_escape") if m else None


def siblings(targets: dict[str, dict], investor: str) -> dict[str, list[dict]]:
    """What the other books already established for the same company: a decided
    graduation with its evidence, or a cited entry stage. Joined on the loose
    name key or a shared Form D issuer CIK, the same identity verify's
    cross-investor invariant uses."""
    import run as R
    want = {s: (R.cross_key(t["name"]), R.cross_ciks(t)) for s, t in targets.items()}
    by_key: dict[str, list[str]] = {}
    for s, (k, _) in want.items():
        by_key.setdefault(k, []).append(s)
    out: dict[str, list[dict]] = {}
    for d in sorted(INVESTORS.iterdir()):
        if d.name == investor or not (d / "companies" / "base.json").exists():
            continue
        p = Paths(d.name)
        try:
            base = json.loads(p.base_json.read_text())
            cls = json.loads(p.classification.read_text()) if p.classification.exists() else {}
            res = json.loads(p.resolved.read_text()) if p.resolved.exists() else {}
        except (ValueError, OSError):
            continue
        for b in base:
            k = R.cross_key(b["name"])
            ciks = R.cross_ciks(b)
            hits = set(by_key.get(k, []))
            if ciks:
                hits |= {s for s, (_, c) in want.items() if c & ciks}
            if not hits:
                continue
            rec = {**res.get(b["slug"], {}), **cls.get(b["slug"], {})}
            if rec.get("valuation_range") == "undetermined":
                continue                     # unnameable there: no identity to share
            keep = {k2: rec.get(k2) for k2 in (
                "entry_stage", "entry_stage_source", "entry_stage_citation", "entry_date",
                "seed_to_a_graduation", "graduation_source", "graduation_citation",
                "graduation_asof", "status", "valuation_range") if rec.get(k2)}
            if not (keep.get("graduation_citation") or keep.get("entry_stage_citation")
                    or keep.get("seed_to_a_graduation") in ("graduated", "not_graduated")):
                continue
            keep["investor"], keep["slug"], keep["name"] = d.name, b["slug"], b["name"]
            note = (rec.get("note") or "")[:300]
            if note:
                keep["note"] = note
            for s in hits:
                out.setdefault(s, []).append(keep)
    return out


def targets_for(investor: str, all_seed: bool, slugs: set[str] | None) -> dict[str, dict]:
    import run as R
    R.P = Paths(investor)
    R.CFG = R.P.config()
    rows = R.load_base(investor)
    merged = R.merge_rows(rows, R.load(R.P.resolved, {}), R.load(R.P.classification, {}))
    by_slug = {r["slug"]: r for r in rows}
    out = {}
    for slug, rec in merged.items():
        row = {**by_slug[slug], "_country": rec.get("hq_country")}
        if slugs is not None:
            if slug in slugs:
                out[slug] = row
            continue
        if rec.get("entry_stage") != "Seed":
            continue
        # a recorded no stays a target: its absence record names these
        # surfaces, and a re-run is how a later round gets caught
        if all_seed or R.graduation_open(rec) or rec.get("seed_to_a_graduation") == "not_graduated":
            out[slug] = row
    return out


def run(investor: str, all_seed: bool, slugs: set[str] | None, refresh: bool) -> None:
    p = Paths(investor)
    dest = p.scratch / "graduation-surfaces.json"
    cache = json.loads(dest.read_text()) if dest.exists() else {}
    targets = targets_for(investor, all_seed, slugs)
    if investor in FIRM_TERMS:
        firm = FIRM_TERMS[investor]
    else:
        inv = json.loads((p.root / "investor" / "investor.json").read_text())
        firm = f'"{inv["name"]}"'
    sib = siblings(targets, investor)
    todo = []
    for slug, row in targets.items():
        entry = cache.get(slug) or {}
        entry["name"], entry["query_name"] = row["name"], clean_name(row["name"])
        entry["country"] = row.get("_country")
        entry["siblings"] = sib.get(slug, [])
        cache[slug] = entry
        svcs = list(SURFACES)
        if (row.get("_country") or "").upper() in LOCAL_EDITIONS:
            svcs.append("googlenews_local")
        for svc in svcs:
            prior = (entry.get("surfaces") or {}).get(svc) or {}
            if refresh or prior.get("status") != "ok" \
                    or prior.get("query_name") != entry["query_name"]:
                todo.append((slug, svc))
    print(f"graduation surfaces {investor}: {len(targets)} rows, {len(todo)} lookups to run")
    lock = threading.Lock()
    done = [0]

    def worker(svc: str, jobs: list[str]) -> None:
        for slug in jobs:
            entry = cache[slug]
            if svc == "googlenews_local":
                res = googlenews_local(entry["query_name"], entry.get("country"))
            else:
                res = SURFACES[svc](entry["query_name"], firm)
            res["query_name"] = entry["query_name"]
            res["asof"] = date.today().isoformat()
            with lock:
                entry.setdefault("surfaces", {})[svc] = res
                done[0] += 1
                if done[0] % 50 == 0:
                    write_atomic(dest, json.dumps(cache, indent=1, sort_keys=True))
                    print(f"    {done[0]}/{len(todo)}", flush=True)

    by_svc: dict[str, list[str]] = {}
    for slug, svc in todo:
        by_svc.setdefault(svc, []).append(slug)
    threads = [threading.Thread(target=worker, args=(svc, jobs)) for svc, jobs in by_svc.items()]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    for entry in cache.values():
        svcs = (entry.get("surfaces") or {}).values()
        entry["asof"] = max((s.get("asof") or "" for s in svcs), default=None)
    write_atomic(dest, json.dumps(cache, indent=1, sort_keys=True))
    errors = sum(1 for s in targets for v in (cache[s].get("surfaces") or {}).values()
                 if v.get("status") != "ok")
    named = sum(1 for s in targets
                if any(i.get("names") for v in (cache[s].get("surfaces") or {}).values()
                       for i in v.get("items", [])))
    print(f"wrote {p.rel(dest)}: {len(targets)} rows, {named} with a headline naming the "
          f"company, {sum(1 for s in targets if cache[s]['siblings'])} with sibling evidence, "
          f"{errors} surface lookups failed (re-run to retry; a failure is never an absence)")
    if errors:
        sys.exit(3)


def main() -> None:
    if len(sys.argv) >= 3 and sys.argv[1] == "decode":
        url = decode(sys.argv[2])
        print(url or "UNRESOLVED")
        sys.exit(0 if url else 1)
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("investor")
    ap.add_argument("--all-seed", action="store_true",
                    help="every Seed row, not only those whose graduation is open")
    ap.add_argument("--slugs", help="comma-separated slugs (overrides the Seed selection)")
    ap.add_argument("--refresh", action="store_true", help="re-run lookups already cached")
    a = ap.parse_args()
    run(a.investor, a.all_seed, set(a.slugs.split(",")) if a.slugs else None, a.refresh)


if __name__ == "__main__":
    main()
