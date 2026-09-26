#!/usr/bin/env python3
"""Free, deterministic sources for current-valuation outcomes.

Three layers, each cached on disk so a re-run costs nothing:

  A. SEC `dei:EntityPublicFloat`  -- filing-grade current value for public
     companies. This is the 10-K cover-page figure: the aggregate market value
     of common equity held by non-affiliates. It EXCLUDES affiliate holdings, so
     it understates market cap; that is conservative for threshold assignment,
     producing false negatives rather than false positives.
  B. Wikidata  -- market cap for foreign listings SEC misses, plus dissolution
     and parent-company facts that identify defunct and acquired companies, plus
     country for the attributes run.
  C. Unicorn lists -- still-private $1B+ companies.

Everything here is free and keyless. SEC asks only for a descriptive
User-Agent; Wikidata is CC0.
"""
import json
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import SEC_CACHE as CACHE, UNICORN_DIR, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "Merit Capital research erik@meritcapit.al"

# SEC publishes a 10 req/s ceiling per client, and every collection session on
# this machine is the same client. The bucket therefore lives in
# shared_throttle (one budget across processes and threads, 8 req/s by
# default); a single process paces exactly as it did with the in-process
# bucket this replaced.
def _throttle() -> None:
    shared_throttle.wait("sec")


class SECUnavailable(RuntimeError):
    """SEC refused or failed the request (403 rate block, 429, 5xx, transport).

    Distinct from a 404, which is the genuine "no such data" answer. Callers
    leave the row unanswered and retry on the next run; nothing is cached.
    """


class WikidataUnavailable(RuntimeError):
    """The SPARQL endpoint throttled or failed; the batch stays unanswered."""


def curl_status(url: str, timeout: int = 45) -> tuple[int, str]:
    """GET with the SEC-required User-Agent -> (http status, body).

    Status 0 means the transport failed before any HTTP answer. Unlike `curl`
    below, a non-2xx answer is reported, not collapsed into None, so callers
    can tell "no such resource" (404) from "come back later" (403/429/5xx).
    """
    try:
        out = subprocess.run(
            ["curl", "-s", "--max-time", str(timeout), "-H", f"User-Agent: {UA}",
             "-w", "\n%{http_code}", url],
            capture_output=True, check=False).stdout.decode("utf-8", errors="replace")
    except OSError:
        return 0, ""
    body, _, code = out.rpartition("\n")
    try:
        return int(code), body
    except ValueError:
        return 0, out

THRESHOLDS = (("100b", 100_000_000_000), ("10b", 10_000_000_000), ("1b", 1_000_000_000))
BOUNDARY_PCT = 0.20

STOP_SUFFIX = re.compile(
    r"\b(inc|corp|corporation|co|company|ltd|limited|llc|lp|llp|plc|sa|nv|ag|gmbh|"
    r"holdings?|group|technologies|technology|labs?|systems?|software|networks?)\b\.?",
    re.I)

# Entities that are wrappers around a company rather than the company: pre-IPO
# SPVs, share classes, trusts. "AIRBNB, A SERIES OF THE PRE-IPO MARKETPLACE, LLC"
# is a real EDGAR registrant and is not Airbnb.
WRAPPER_RE = re.compile(
    r"\b(a series of|series of|pre.?ipo|spv|special purpose|trust|fund|partners|"
    r"holdings? (i|ii|iii|iv|v)\b|acquisition corp)\b", re.I)


def norm(name: str) -> str:
    n = name.lower()
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = STOP_SUFFIX.sub(" ", n)
    return re.sub(r"\s+", " ", n).strip()


def curl(url: str, timeout: int = 45) -> str | None:
    """GET with the SEC-required descriptive User-Agent. None on any failure."""
    for attempt in range(3):
        try:
            out = subprocess.run(
                ["curl", "-sf", "--max-time", str(timeout), "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout
            return out.decode("utf-8", errors="replace")
        except subprocess.CalledProcessError:
            if attempt < 2:
                time.sleep(1.0 * (attempt + 1))
    return None


# ---------------------------------------------------------------------------
# CIK resolution
# ---------------------------------------------------------------------------

def load_cik_lookup() -> dict[str, list[tuple[str, str]]]:
    """EDGAR's full registrant list, normalised name -> [(cik, original name)].

    `cik-lookup-data.txt` is used rather than `company_tickers.json` because it
    includes historical registrants. A company that IPO'd and was then acquired
    or delisted is absent from the ticker file but present here, and those are
    precisely the rows whose outcome we need to get right.
    """
    dest = CACHE / "cik-lookup-data.txt"
    if not dest.exists():
        # One downloader at a time across sessions: the file is 38 MB and
        # gitignored, so several fresh sessions would otherwise all fetch it
        # and race their writes onto one path.
        with shared_throttle.exclusive("cik-lookup"):
            if not dest.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                _throttle()
                code, body = curl_status(
                    "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt", timeout=180)
                if code != 200 or not body:
                    raise SystemExit(f"could not fetch cik-lookup-data.txt (HTTP {code})")
                write_atomic(dest, body)

    index: dict[str, list[tuple[str, str]]] = {}
    lines = 0
    with open(dest, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            lines += 1
            line = line.rstrip("\n")
            if not line.endswith(":"):
                continue
            name, _, rest = line.rpartition(":")          # trailing empty field
            name, _, cik = name.rpartition(":")
            if not cik.isdigit() or not name:
                continue
            if WRAPPER_RE.search(name):
                continue
            key = norm(name)
            if key:
                index.setdefault(key, []).append((str(int(cik)), name))
    # The file is ~1.05M lines; a torn download parses without error and
    # silently loses registrants, so the guard is a line count, not a parse.
    if lines < 500_000:
        raise SystemExit(f"{dest} looks truncated ({lines} lines); delete it and re-run")
    return index


def resolve_cik(row: dict, index: dict[str, list[tuple[str, str]]]) -> dict | None:
    """Find the SEC registrant for a base row, conservatively.

    Only exact normalised-name equality is accepted; no fuzzy matching. A base
    row whose name is a single short token ("Flex", "Agile") matches far too
    easily, so those are resolved but marked weak for review rather than trusted.
    """
    if (row.get("edgar_cik") or "").strip():
        return {"cik": str(int(row["edgar_cik"])), "cik_source": "base",
                "cik_name": row["name"], "cik_weak": False}

    key = norm(row["name"])
    if not key:
        return None
    hits = index.get(key)
    if not hits:
        return None
    if len(hits) > 1:
        # Ambiguous: several registrants share the name. Not worth guessing.
        return {"cik": hits[0][0], "cik_source": "lookup_ambiguous",
                "cik_name": hits[0][1], "cik_weak": True}

    cik, matched = hits[0]
    weak = len(key) < 6 or " " not in key
    return {"cik": cik, "cik_source": "lookup_exact", "cik_name": matched,
            "cik_weak": weak}


# ---------------------------------------------------------------------------
# Layer A: SEC public float
# ---------------------------------------------------------------------------

def public_float(cik: str) -> list[dict] | None:
    """Full reported series of dei:EntityPublicFloat, cached. None if never public.

    A company with no EntityPublicFloat has never filed a 10-K cover page, which
    is a useful signal in itself: it did not reach US public markets.
    """
    out = CACHE / "public-float" / f"{cik}.json"
    if out.exists():
        payload = json.loads(out.read_text())
        return payload or None

    url = (f"https://data.sec.gov/api/xbrl/companyconcept/"
           f"CIK{int(cik):010d}/dei/EntityPublicFloat.json")
    # Only two answers may enter the shared cache: a parsed 200, or a 404 (the
    # company never reported a public float). A 403 rate block, 429, 5xx or a
    # transport failure raises after retries and writes NOTHING, because a
    # cached empty list here would read as "never public" for every investor.
    last = 0
    for attempt in range(3):
        _throttle()
        code, body = curl_status(url)
        if code == 200:
            series: list[dict] = []
            try:
                for unit in json.loads(body).get("units", {}).get("USD", []):
                    if unit.get("val") is None or not unit.get("end"):
                        continue
                    series.append({"end": unit["end"], "val": int(unit["val"]),
                                   "form": unit.get("form"), "fy": unit.get("fy")})
            except (json.JSONDecodeError, ValueError, TypeError, AttributeError):
                last = code
                time.sleep(1.0 * (attempt + 1))
                continue                     # a 200 that is not the JSON we asked for
            series.sort(key=lambda x: x["end"])
            write_atomic(out, json.dumps(series))
            return series or None
        if code == 404:
            write_atomic(out, "[]")
            return None
        last = code
        time.sleep(1.0 * (attempt + 1))
    raise SECUnavailable(f"CIK {cik}: HTTP {last or 'transport failure'} after 3 attempts")


def prefetch_public_float(ciks: list[str], workers: int = 8, progress=None) -> set[str]:
    """Warm the disk cache for many CIKs at once, inside the rate limit.

    `public_float` stays the single reader, so callers see identical results
    whether or not this ran; it only removes the wall-clock cost. Returns the
    CIKs SEC would not answer (nothing cached for them), so the caller can
    leave those rows open instead of asking again in this run.
    """
    todo = [c for c in dict.fromkeys(ciks)
            if not (CACHE / "public-float" / f"{c}.json").exists()]
    failed: set[str] = set()
    if not todo:
        return failed
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(public_float, c): c for c in todo}
        for fut in as_completed(futures):
            try:
                fut.result()
            except SECUnavailable:
                failed.add(futures[fut])
            done += 1
            if progress and done % 100 == 0:
                progress(done, len(todo))
    if failed:
        print(f"    {len(failed)} CIK(s) unavailable from SEC; nothing cached, "
              f"re-run prepare to retry", file=sys.stderr)
    return failed


# ---------------------------------------------------------------------------
# Layer C: Wikipedia unicorn list
# ---------------------------------------------------------------------------

def _parse_wikitables(html: str) -> list[list[list[str]]]:
    from html.parser import HTMLParser

    class TableParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.tables = []; self.cur = None; self.row = None; self.cell = None
            self.depth = 0

        def handle_starttag(self, tag, attrs):
            a = dict(attrs)
            if tag == "table":
                self.depth += 1
                if self.depth == 1 and "wikitable" in (a.get("class") or ""):
                    self.cur = []
            elif self.cur is not None and self.depth == 1:
                if tag == "tr":
                    self.row = []
                elif tag in ("td", "th") and self.row is not None:
                    self.cell = []

        def handle_endtag(self, tag):
            if tag == "table":
                if self.depth == 1 and self.cur is not None:
                    self.tables.append(self.cur); self.cur = None
                self.depth -= 1
            elif self.cur is not None and self.depth == 1:
                if tag == "tr" and self.row is not None:
                    if self.row:
                        self.cur.append(self.row)
                    self.row = None
                elif tag in ("td", "th") and self.cell is not None:
                    self.row.append("".join(self.cell).strip()); self.cell = None

        def handle_data(self, data):
            if self.cell is not None:
                self.cell.append(data)

    p = TableParser()
    p.feed(html)
    return p.tables


def _cell_date(text: str) -> str | None:
    """'May\\xa02026\\xa0(2026-05)[20]' -> '2026-05'."""
    m = re.search(r"\((\d{4}-\d{2})\)", text)
    if m:
        return m.group(1)
    m = re.search(r"(\d{4})", text)
    return m.group(1) if m else None


def _cell_billions(text: str) -> int | None:
    m = re.search(r"([\d,]+(?:\.\d+)?)", text.replace(",", ""))
    if not m:
        return None
    try:
        return int(float(m.group(1)) * 1e9)
    except ValueError:
        return None


def load_unicorn_list() -> dict[str, dict[str, dict]]:
    """Wikipedia's unicorn list -> {'current': {...}, 'former': {...}}, keyed by
    normalised name.

    This is the second recall net: a $1B+ company the model fails to recognise is
    still caught by name intersection. The *former* table carries exit reason and
    date (IPO / Acquisition / Business failure...), which independently
    corroborates acquired/public/defunct status.

    Wikipedia's figures are last-round marks, not marks-to-market, and the list
    is community-maintained; both caveats travel with the source label
    `unicorn_list` and the medium confidence it carries.
    """
    dest = UNICORN_DIR / "wikipedia.json"
    if dest.exists():
        return json.loads(dest.read_text())

    html_path = UNICORN_DIR / "wikipedia.html"
    if not html_path.exists():
        UNICORN_DIR.mkdir(parents=True, exist_ok=True)
        body = curl("https://en.wikipedia.org/wiki/List_of_unicorn_startup_companies",
                    timeout=120)
        if not body:
            raise SystemExit("could not fetch the Wikipedia unicorn list")
        write_atomic(html_path, body)

    tables = _parse_wikitables(html_path.read_text(encoding="utf-8"))
    current_t = next(t for t in tables
                     if t and t[0][0].startswith("Company") and "Exit" not in "".join(t[0]))
    former_t = next(t for t in tables
                    if t and t[0][0].startswith("Company") and "Exit" in "".join(t[0]))

    current: dict[str, dict] = {}
    for r in current_t[1:]:
        if len(r) < 5 or not r[0]:
            continue
        current.setdefault(norm(r[0]), {
            "name": r[0], "valuation_usd": _cell_billions(r[1]),
            "asof": _cell_date(r[2]), "industry": r[3], "country": r[4],
        })

    former: dict[str, dict] = {}
    for r in former_t[1:]:
        if len(r) < 5 or not r[0]:
            continue
        former.setdefault(norm(r[0]), {
            "name": r[0], "last_valuation_usd": _cell_billions(r[1]),
            "exit_date": _cell_date(r[3]), "exit_reason": r[4],
            "exit_valuation_usd": _cell_billions(r[5]) if len(r) > 5 else None,
        })

    out = {"current": current, "former": former}
    write_atomic(dest, json.dumps(out, indent=1))
    return out


def threshold_of(valuation_usd: int | None) -> str | None:
    if not valuation_usd:
        return None
    for label, floor in THRESHOLDS:
        if valuation_usd >= floor:
            return label
    return "sub_1b"


def near_boundary(valuation_usd: int | None) -> bool:
    """True when the figure sits within 20% of a threshold.

    Public float understates market cap, so a company just under a line may
    genuinely be over it. These rows are flagged for review rather than trusted.
    """
    if not valuation_usd:
        return False
    return any(floor * (1 - BOUNDARY_PCT) <= valuation_usd <= floor * (1 + BOUNDARY_PCT)
               for _, floor in THRESHOLDS)


def from_public_float(series: list[dict], today: str) -> dict:
    """Latest observation -> current valuation, with a staleness read.

    A company that stopped filing 10-Ks was acquired, taken private or delisted,
    so its last reported float is not a current value and must not be published
    as one.
    """
    latest = series[-1]
    stale = latest["end"] < f"{int(today[:4]) - 2}{today[4:]}"    # ~24 months
    rec = {
        "is_public": True,
        "public_since": int(series[0]["end"][:4]),
        "valuation_asof": latest["end"],
        "valuation_source": "sec_public_float",
        "flags": [],
    }
    if stale:
        # Stopped filing: no current standalone valuation exists.
        rec.update({"status": "acquired", "valuation_usd": None,
                    "valuation_confidence": "medium"})
        rec["flags"].append("stale")
    else:
        rec.update({"status": "public", "valuation_usd": latest["val"],
                    "valuation_confidence": "high"})
        if near_boundary(latest["val"]):
            rec["flags"].append("boundary")
    return rec


# ---------------------------------------------------------------------------
# Layer B: Wikidata
# ---------------------------------------------------------------------------

SPARQL = """
SELECT ?item ?itemLabel ?cap ?capTime ?countryLabel ?dissolved ?parentLabel ?ownerLabel ?successorLabel WHERE {
  VALUES ?name { %s }
  ?item rdfs:label ?name .
  ?item wdt:P31/wdt:P279* wd:Q4830453 .
  OPTIONAL { ?item p:P2226 ?capSt . ?capSt ps:P2226 ?cap . OPTIONAL { ?capSt pq:P585 ?capTime } }
  OPTIONAL { ?item wdt:P17 ?country }
  OPTIONAL { ?item wdt:P576 ?dissolved }
  OPTIONAL { ?item wdt:P749 ?parent }
  OPTIONAL { ?item wdt:P127 ?owner }
  OPTIONAL { ?item wdt:P1366 ?successor }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
"""


def wikidata_batch(names: list[str]) -> dict[str, dict]:
    """Look up a batch of company names. Constrained to business entities (Q4830453).

    Name collisions are this layer's main failure mode, so the P31 constraint is
    not optional and callers should corroborate before trusting a hit.
    """
    values = " ".join('"%s"@en' % n.replace('\\', r'\\').replace('"', r'\"')
                      for n in names)
    query = SPARQL % values
    shared_throttle.wait("wikidata")
    try:
        body = subprocess.run(
            ["curl", "-sf", "--max-time", "120", "-X", "POST",
             "-H", f"User-Agent: {UA}",
             "-H", "Accept: application/sparql-results+json",
             "--data-urlencode", f"query={query}",
             "https://query.wikidata.org/sparql"],
            capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
    except subprocess.CalledProcessError as e:
        # A throttled or failed batch must not read as "no hits": the caller
        # would cache an empty answer for every name in it and never ask again.
        raise WikidataUnavailable(f"SPARQL POST failed (curl rc={e.returncode})") from e
    try:
        rows = json.loads(body)["results"]["bindings"]
    except (json.JSONDecodeError, KeyError) as e:
        raise WikidataUnavailable("SPARQL answer was not a result set") from e

    out: dict[str, dict] = {}
    for r in rows:
        label = r.get("itemLabel", {}).get("value")
        if not label:
            continue
        rec = out.setdefault(norm(label), {"label": label})
        if "cap" in r:
            try:
                cap = int(float(r["cap"]["value"]))
                when = r.get("capTime", {}).get("value", "")[:10]
                if cap > rec.get("market_cap", 0):
                    rec["market_cap"] = cap
                    rec["market_cap_asof"] = when or None
            except (ValueError, TypeError):
                pass
        if "countryLabel" in r:
            rec["country"] = r["countryLabel"]["value"]
        if "dissolved" in r:
            rec["dissolved"] = r["dissolved"]["value"][:10]
        if "parentLabel" in r:
            rec["parent"] = r["parentLabel"]["value"]
        # Owned-by and replaced-by name the acquirer of a DISSOLVED company
        # (Datalogix: owned by Oracle; PRO-157). On a live company owned-by
        # often lists a shareholder, so run.py reads them only with a
        # dissolution date.
        if "ownerLabel" in r:
            rec.setdefault("owner", r["ownerLabel"]["value"])
        if "successorLabel" in r:
            rec.setdefault("successor", r["successorLabel"]["value"])
    return out
