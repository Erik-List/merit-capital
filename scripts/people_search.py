"""A checked web search for a person's own LinkedIn or X profile (PRO-177, PRO-178).

The firm's own site stays the first source (`site-portfolio.py`,
`read_socials`). This is the second, for a published member the site gives no
link for: one search names the person and the firm, and a result counts only
when every test below holds (Erik, 2026-09-30, relaxing PRO-154's "the firm's
own site or none"):
  - its address is a profile (`people_common.clean_social`);
  - its title names the person (first and last name; nickname forms count);
  - its title or snippet names the firm (a non-generic word of the firm's name
    or slug, or an alias from `config.json` `profile.search_aliases`);
  - the account id names the person (`people_common.handle_score` > 0) and is
    not the firm's own (`firm_handles`).
What comes back is a candidate, not a decision: `read_socials` still gives an
account to one person only (a colleague whose name fits it better wins) and
ranks it below anything the site itself said. The evidence (engine, query,
title, date) is written beside the chosen link in `sources/site/team-socials.json`.

Engine: Brave Search's HTML results, the one engine that answers a plain fetch
with results from this machine (DuckDuckGo's HTML endpoint returns a bot
check, Mojeek a 403, Bing no profile results; measured 2026-10-08). Paced
machine-wide through `shared_throttle` ("brave", one query per two seconds)
and cached per query in `<investor>/scratch/socials-search.json`, so a re-run
costs nothing and the audit can be re-read without a search.
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shared_throttle  # noqa: E402
from people_common import (_name_forms, clean_social, firm_handles,  # noqa: E402
                           handle_score, social_handle)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
ENGINE = "brave"
RATE = 1 / 30       # queries per second, machine-wide: Brave's page answers 429 to bursts
BACKOFFS = (60.0, 120.0, 240.0)   # waits on a 429 before each retry (Retry-After when sent)
PAUSE_AFTER_FAILURE = 900.0       # seconds this process asks no more after a query fails outright
_down_until = 0.0
# Words of a firm's name that name no firm on their own.
GENERIC = {"capital", "ventures", "venture", "partners", "partner", "management",
           "growth", "fund", "funds", "group", "the", "and", "co", "llc", "lp",
           "inc", "vc", "equity", "investments", "investment", "global", "labs",
           "associates", "company", "of"}
RESULT = re.compile(r'<div class="snippet [^"]*"[^>]*data-type="web"[^>]*>(.*?)'
                    r'(?=<div class="snippet |<div class="result-cluster|</main>)', re.S)
HREF = re.compile(r'<a href="([^"]+)"')
TITLE = re.compile(r'<div class="title[^"]*"[^>]*?(?:title="([^"]*)")?[^>]*>(.*?)</div>', re.S)
CONTENT = re.compile(r'<div class="content [^"]*"[^>]*>(.*?)</div>', re.S)


def _fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()


def _text(fragment: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", " ", fragment or "")).strip()


def firm_tokens(firm_name: str, slug: str, aliases: list[str] | None = None) -> set[str]:
    """The words that name the firm: every non-generic word of its published
    name, its slug and its aliases, plus each whole name ("general catalyst",
    "a16z")."""
    out: set[str] = set()
    for src in [firm_name, (slug or "").replace("-", " ")] + list(aliases or []):
        f = _fold(src)
        words = [w for w in re.findall(r"[a-z0-9]+", f) if w not in GENERIC]
        out |= set(words)
        if f.strip():
            out.add(re.sub(r"\s+", " ", f.strip()))
    return {t for t in out if t}


def names_firm(text: str, tokens: set[str]) -> bool:
    """Does the text name the firm? A whole-name match, or a non-generic word
    of it; words of three letters or fewer must stand alone ("gv", "ivp")."""
    f = _fold(text)
    for t in tokens:
        if " " in t:
            if t in f:
                return True
        elif len(t) <= 3:
            if re.search(rf"(?<![a-z0-9]){re.escape(t)}(?![a-z0-9])", f):
                return True
        elif t in f:
            return True
    return False


def names_person(text: str, name: str) -> bool:
    """Does the text name the person: a last name and a first name (or a
    nickname form of it) among its words."""
    firsts, lasts, fi, _ = _name_forms(name)
    if not firsts:
        return False
    words = set(re.findall(r"[a-z0-9]+", _fold(text)))
    has_last = any(l in words for l in lasts)
    has_first = any(f in words for f in firsts) or any(
        len(f) >= 4 and any(w.startswith(f) for w in words) for f in firsts)
    return has_last and has_first


def brave_api_search(query: str, key: str) -> list[dict] | None:
    """The same results through the Brave Search API (a key in
    BRAVE_SEARCH_API_KEY; the free plan allows one query a second and 2,000 a
    month), which does not throttle a paced pass the way the HTML page does."""
    shared_throttle.wait("brave-api", 1.0)
    out = subprocess.run(["curl", "-s", "--max-time", "40", "-H", "Accept: application/json",
                          "-H", f"X-Subscription-Token: {key}", "-w", "\n%{http_code}",
                          "https://api.search.brave.com/res/v1/web/search?q=" + quote(query)
                          + "&count=20&search_lang=en"], capture_output=True)
    body, _, code = out.stdout.decode("utf-8", errors="replace").rpartition("\n")
    if code != "200":
        print(f"    brave api {code} on {query!r}", flush=True)
        return None
    try:
        results = json.loads(body).get("web", {}).get("results", [])
    except ValueError:
        return None
    return [{"url": r.get("url") or "", "title": _text(r.get("title") or ""),
             "snippet": _text(r.get("description") or "")} for r in results]


def brave_search(query: str) -> list[dict] | None:
    """Brave's web results for the query: [{url, title, snippet}], or None when
    the engine gave no result page after the retries. With an API key in the
    environment the API answers; else the HTML page, where a 429 is waited out
    (Retry-After, else BACKOFFS in turn); when the retries run out the process
    stops asking for PAUSE_AFTER_FAILURE seconds and sets a short machine-wide
    cooldown, so sibling runs stop too. A failed query is never cached: the
    next pass asks again."""
    global _down_until
    key = os.environ.get("BRAVE_SEARCH_API_KEY")
    if key:
        return brave_api_search(query, key)
    if time.time() < _down_until:
        return None
    url = "https://search.brave.com/search?q=" + quote(query) + "&source=web"
    code = ""
    for attempt, backoff in enumerate(BACKOFFS):
        shared_throttle.wait(ENGINE, RATE)
        out = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", UA,
                              "-H", "Accept-Language: en-US,en;q=0.9", "-D", "-",
                              "-w", "\n%{http_code}", url], capture_output=True)
        text = out.stdout.decode("utf-8", errors="replace")
        head, _, rest = text.partition("\r\n\r\n")
        body, _, code = rest.rpartition("\n")
        if code == "200" and 'class="snippet ' in body:
            break
        if code == "429":
            m = re.search(r"(?im)^retry-after:\s*(\d+)", head)
            wait = float(m.group(1)) if m else backoff
            print(f"    brave 429 on {query!r}; waiting {wait:.0f}s", flush=True)
            time.sleep(wait)
            continue
        time.sleep(5)
    else:
        _down_until = time.time() + PAUSE_AFTER_FAILURE
        shared_throttle.cooldown(ENGINE, 180)
        print(f"    brave gave no results for {query!r} (last status {code}); this process "
              f"asks nothing more for {PAUSE_AFTER_FAILURE / 60:.0f} min, the failed queries "
              f"are not cached", flush=True)
        return None
    results = []
    for m in RESULT.finditer(body):
        seg = m.group(1)
        h = HREF.search(seg)
        if not h:
            continue
        t = TITLE.search(seg)
        c = CONTENT.search(seg)
        results.append({"url": html.unescape(h.group(1)),
                        "title": _text(t.group(1) or t.group(2)) if t else "",
                        "snippet": _text(c.group(1)) if c else ""})
    return results


class SearchCache:
    """Per-investor query cache (scratch/socials-search.json)."""

    def __init__(self, path: Path | None):
        self.path = path
        self.data = json.loads(path.read_text()) if path and path.exists() else {}
        self.dirty = False

    def get(self, query: str) -> dict | None:
        e = self.data.get(query)
        return e if e and e.get("results") is not None else None   # a failed query is asked again

    def put(self, query: str, results: list[dict] | None) -> dict:
        entry = {"engine": ENGINE, "fetched": time.strftime("%Y-%m-%d"),
                 "results": results}
        if results is not None:            # only an answer is remembered
            self.data[query] = entry
            self.dirty = True
        return entry

    def save(self) -> None:
        if self.path and self.dirty:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text(json.dumps(self.data, indent=1, ensure_ascii=False) + "\n")
            self.dirty = False


def search_person(name: str, firm_name: str, slug: str, cache: SearchCache,
                  aliases: list[str] | None = None) -> dict:
    """One checked search for the person: {query, engine, fetched, available,
    accepted: [{kind, url, title}], rejected: [reason...]}. `accepted` holds
    every profile address in the results that passes the four tests; the
    caller decides between them (and against the site's own candidates)."""
    query = f'"{name}" {firm_name} linkedin'
    entry = cache.get(query)
    if entry is None:
        entry = cache.put(query, brave_search(query))
    results = entry.get("results")
    out = {"query": query, "engine": ENGINE, "fetched": entry.get("fetched"),
           "available": results is not None, "accepted": [], "rejected": []}
    if results is None:
        return out
    tokens = firm_tokens(firm_name, slug, aliases)
    firm = firm_handles(firm_name, slug)
    seen = set()
    for r in results:
        u = r.get("url") or ""
        kind = ("linkedin" if "linkedin.com" in u.lower() else
                "x" if re.search(r"(twitter|x)\.com/", u, re.I) else None)
        if not kind:
            continue
        clean = clean_social(kind, u)
        if not clean:
            continue
        h = social_handle(kind, clean)
        if (kind, h) in seen:
            continue
        seen.add((kind, h))
        title, snippet = r.get("title") or "", r.get("snippet") or ""
        why = None
        if not names_person(title, name):
            why = "title does not name the person"
        elif not names_firm(title + " " + snippet, tokens):
            why = "neither title nor snippet names the firm"
        elif re.sub(r"[^a-z0-9]", "", h) in firm:
            why = "the firm's own account"
        elif not handle_score(h, name):
            why = "account id does not name the person"
        if why:
            out["rejected"].append(f"{clean}: {why} ({title[:80]})")
            continue
        out["accepted"].append({"kind": kind, "url": clean, "title": title})
    return out
