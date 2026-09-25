#!/usr/bin/env python3
"""Where a firm operates: its newest Form ADV, checked against its own site.

The rule (Erik, 2026-09-24; COLLECTION.md §11): a firm's hq_location is the
principal office on its newest Form ADV (Item 1.F), unless the firm's own site
disagrees with that office, in which case the site wins. Where the firm
operates matters more than where it files.

The site disagrees when it
  (a) labels a different office its headquarters,
  (b) lists its offices and the ADV principal office is not among them, or
  (c) says in its own words that the firm operates from another city. That is
      a recorded statement, config.json profile.site_office {place, url,
      quote, basis}: YC's site calls Mountain View "the original YC office"
      and says the batch moves to San Francisco.
A site that lists several offices including the principal office agrees with
it, whatever the order: Creandum lists San Francisco first, and its ADV shows
two advisory staff there. A site that names no office leaves the ADV standing.

Why not the Form D address vote any more: a count over a decade of filings
answers "where has this firm filed from", not "where is it". 8VC moved to
Austin in 2021 and the vote still said San Francisco; a fund administrator's
address can be the only one on file (Greylock: Burlington, MA); and a filing
address can outlive the office (YC has run from San Francisco since 2023).

The record, sources/offices.json, holds what was read and when: the newest
ADV's principal and other offices (with advisory staff per office), the
site's offices in page order with the quoted text, and the decision. A site
that could not be fetched is recorded as unchecked, never as naming no
office (a failed lookup is not an absence), and the decision refuses.

Usage:
  python3 scripts/firm-offices.py <slug>          refresh the record, apply it
  python3 scripts/firm-offices.py --all           every investor not in flight
  python3 scripts/firm-offices.py --all --check   compare, write nothing
The adviser is config.json profile.adv_crd when set, else the first CRD the
profile's aum provenance cites (the adviser whose ADV carries the AUM).
"""
import argparse
import html
import json
import re
import subprocess
import sys
import time
import unicodedata
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import INVESTORS, ROOT, Paths, write_atomic  # noqa: E402

UA = "Merit Capital research erik@meritcapit.al"      # as edgar_common.py
ADV_URL = "https://reports.adviserinfo.sec.gov/reports/ADV/{crd}/PDF/{crd}.pdf"
ADV_CACHE = ROOT / "data" / "filings" / "adv"          # gitignored, like form-d/
SITE_PAGES = ("", "/contact", "/contact-us", "/about", "/about-us", "/offices",
              "/locations")
RULE = ("Rule (Erik 2026-09-24): the newest Form ADV principal office, unless the "
        "firm's own site disagrees, and then the site wins.")

US_STATES = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI",
    "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Puerto Rico": "PR", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX",
    "Utah": "UT", "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
    "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}
STATE_CODES = set(US_STATES.values())

# Cities a site's office list can name outside the US, with the country the
# published place carries ("Berlin, Germany", as the ADV-derived places read).
WORLD_CITIES = {
    "London": "United Kingdom", "Berlin": "Germany", "Munich": "Germany",
    "Hamburg": "Germany", "Stockholm": "Sweden", "Paris": "France",
    "Amsterdam": "Netherlands", "Copenhagen": "Denmark", "Helsinki": "Finland",
    "Oslo": "Norway", "Dublin": "Ireland", "Zurich": "Switzerland",
    "Vienna": "Austria", "Madrid": "Spain", "Barcelona": "Spain",
    "Lisbon": "Portugal", "Milan": "Italy", "Tel Aviv": "Israel",
    "Bangalore": "India", "Bengaluru": "India", "Mumbai": "India",
    "New Delhi": "India", "Gurugram": "India", "Singapore": "Singapore",
    "Hong Kong": "Hong Kong", "Beijing": "China", "Shanghai": "China",
    "Tokyo": "Japan", "Seoul": "South Korea", "Sydney": "Australia",
    "Toronto": "Canada", "Dubai": "United Arab Emirates", "São Paulo": "Brazil",
}
CITY_ALIASES = {"sf": "san francisco", "nyc": "new york", "new york city": "new york",
                "bengaluru": "bangalore"}


class Unavailable(Exception):
    """A source could not be read. Never recorded as an absence."""


def norm_city(place: str | None) -> str:
    city = (place or "").split(",")[0].strip()
    city = unicodedata.normalize("NFKD", city).encode("ascii", "ignore").decode().lower()
    city = re.sub(r"\s+", " ", city)
    return CITY_ALIASES.get(city, city)


def same_city(a: str | None, b: str | None) -> bool:
    return bool(a) and bool(b) and norm_city(a) == norm_city(b)


def titled(text: str) -> str:
    """Title case that keeps ordinals ("560 20th Street", not "20Th")."""
    return re.sub(r"\b(\d+)(St|Nd|Rd|Th)\b", lambda m: m.group(1) + m.group(2).lower(),
                  text.title())


def place_of(city: str, state: str, country: str) -> str:
    """"City, ST" for a US office, "City, Country" elsewhere."""
    city = re.sub(r"\s+-\s+.*$", "", city).strip().title()   # "BERLIN - MITTE"
    if country in ("", "United States") and state:
        return f"{city}, {US_STATES.get(state, state)}"
    return f"{city}, {country or state}"


# ---------------------------------------------------------------- Form ADV

def fetch_adv(crd: int) -> Path:
    """Download the current Form ADV report for one adviser. The report is
    rendered from the newest filing, so it is always the latest office list."""
    ADV_CACHE.mkdir(parents=True, exist_ok=True)
    out = ADV_CACHE / f"{crd}.pdf"
    if out.exists() and time.time() - out.stat().st_mtime < 86400:
        return out                      # fetched today; the report changes per filing
    tmp = out.with_suffix(".part")
    r = subprocess.run(["curl", "-sfL", "--max-time", "120", "-A", UA, "-o", str(tmp),
                        ADV_URL.format(crd=crd)], capture_output=True)
    if r.returncode != 0 or not tmp.exists() or tmp.read_bytes()[:4] != b"%PDF":
        tmp.unlink(missing_ok=True)
        raise Unavailable(f"Form ADV for CRD {crd}: curl rc={r.returncode}")
    tmp.replace(out)
    return out


def adv_text(pdf: Path) -> str:
    import pypdf  # only this step needs it
    reader = pypdf.PdfReader(str(pdf))
    text = ""
    for page in reader.pages:          # Item 1 and Schedule D 1.F come first
        text += "\n" + (page.extract_text() or "")
        if "SECTION 1.I" in text:
            break
    return text


PAGE_HEADER = re.compile(r"\n\s*FORM ADV\nUNIFORM APPLICATION.*?General Instruction 4\.[^\n]*\n",
                         re.S)


def _address(block: str) -> dict:
    """Street, city, state and country from one ADV address block."""
    def between(a, b):
        m = re.search(re.escape(a) + r"(.*?)" + re.escape(b), block, re.S)
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    street = " ".join(filter(None, [between("Number and Street 1:", "Number and Street 2:"),
                                    between("Number and Street 2:", "City:")]))
    city = between("City:", "State:")
    tail = between("State:", "ZIP+4/Postal Code:")
    state, _, country = tail.partition("Country:")
    state, country = state.strip(), country.strip()
    return {"street": street, "city": city.title(), "state": US_STATES.get(state, state),
            "country": country, "place": place_of(city, state, country)}


def parse_adv(text: str, crd: int) -> dict:
    head = re.search(r"Primary Business Name:\s*(.*?)\s*CRD Number:\s*(\d+)\s*\n\s*"
                     r"(.*?)\s*-?\s*(?:All Sections )?Rev\.[^\n]*\n\s*(\d{1,2}/\d{1,2}/\d{4})",
                     text, re.S)
    if not head:
        raise Unavailable(f"Form ADV for CRD {crd}: header not found")
    body = PAGE_HEADER.sub("\n", text)
    i = body.find("F. Principal Office and Place of Business")
    j = body.find("If this address is a private residence", i)
    if i < 0 or j < 0:
        raise Unavailable(f"Form ADV for CRD {crd}: Item 1.F not found")
    principal = _address(body[i:j])
    # A Schedule D 1.F office is the address block that ends in the per-office
    # staff question. The extracted text does not keep the form's order (8VC's
    # Schedule D comes out ahead of Item 1), so each office is anchored on that
    # question and read back to the nearest address before it.
    others, seen = [], {(principal["street"].lower(), principal["place"])}
    staff_q = re.compile(r"How many employees perform investment advisory functions "
                         r"from this office location\?[ \t]*\n?[ \t]*(\d*)")
    for m in staff_q.finditer(body):
        start = body.rfind("Number and Street 1:", 0, m.start())
        if start < 0:
            continue
        office = _address(body[start:m.start()])
        if not office["city"]:
            continue
        office["advisory_staff"] = int(m.group(1)) if m.group(1) else None
        key = (office["street"].lower(), office["place"])
        if key not in seen:
            seen.add(key)
            others.append(office)
    filed = datetime.strptime(head.group(4), "%m/%d/%Y").date().isoformat()
    return {"crd": crd, "firm": head.group(1).strip(),
            "filing": re.sub(r"\s*-\s*$", "", head.group(3).strip()), "filed": filed,
            "url": ADV_URL.format(crd=crd), "principal": principal,
            "others": sorted(others, key=lambda o: -(o["advisory_staff"] or 0))}


def adviser_crd(p: Paths) -> int | None:
    cfg = p.config().get("profile", {})
    if "adv_crd" in cfg:                       # explicit, including null (no ADV)
        return cfg["adv_crd"]
    fields = json.loads(p.investor_sources.read_text()).get("fields", {})
    found = re.findall(r"(?:reports/ADV/|firm/summary/|CRD )(\d{5,7})",
                       json.dumps(fields.get("aum", {})))
    if not found:
        raise SystemExit(f"{p.slug}: no adviser CRD; set config.json profile.adv_crd "
                         f"(null when the firm files no Form ADV)")
    return int(found[0])


# ---------------------------------------------------------------- the site

def page_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw))


def fetch_page(url: str) -> str | None:
    r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A",
                        "Mozilla/5.0 (Macintosh) merit-capital research", "-w",
                        "\n%{http_code}", url], capture_output=True)
    body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
    if r.returncode != 0:
        raise Unavailable(f"{url}: curl rc={r.returncode}")
    return body if code.strip() == "200" and len(body) > 500 else None


US_ANCHOR = re.compile(
    r"\b((?:[A-Z][A-Za-z.'-]+ ){0,2}[A-Z][A-Za-z.'-]+),? (" + "|".join(
        sorted(list(US_STATES) + sorted(STATE_CODES), key=len, reverse=True))
    + r"),? \d{5}\b")
POSTCODE = r"(?:\d{3} ?\d{2}|\d{4,5}|[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2})"
HQ_LABEL = re.compile(r"(?i)\b(?:headquarter(?:s|ed)|\bHQ\b)")


def site_offices(text: str, known: dict[str, str]) -> list[dict]:
    """The offices a page lists, in page order. An office is a place with an
    address: a US city before its state and ZIP, or a known city beside a
    postcode or its country. Prose ("based in the Bay Area") is not one."""
    found = []
    for m in US_ANCHOR.finditer(text):
        words = m.group(1)
        # "St San Francisco" -> the longest known city the words end with
        city = next((c for c in sorted(known, key=len, reverse=True)
                     if norm_city(words).endswith(norm_city(c))), words)
        state = US_STATES.get(m.group(2), m.group(2))
        found.append((m.start(), place_of(city, state, "United States"), m))
    for city, country in WORLD_CITIES.items():
        pat = (rf"(?:{POSTCODE}[ ,]+{re.escape(city)}\b|\b{re.escape(city)}[ ,]+{POSTCODE}\b"
               rf"|\b{re.escape(city)}[-\w]*,? (?:{re.escape(country)}|UK)\b)")
        for m in re.finditer(pat, text):
            found.append((m.start(), place_of(city, "", country), m))
    offices, seen = [], set()
    found.sort(key=lambda f: f[0])
    for n, (pos, place, m) in enumerate(found):
        # An HQ label belongs to this office only: the text before it back to
        # the previous office, and a short "(HQ)" after it up to the next one.
        # The ten characters after an office are its own suffix slot, so they
        # are not also read as a prefix label of the office that follows.
        prev_end = found[n - 1][2].end() + 10 if n else 0
        next_start = found[n + 1][0] if n + 1 < len(found) else len(text)
        window = (text[max(prev_end, pos - 50):pos]
                  + text[m.end():min(next_start, m.end() + 10)])
        if norm_city(place) in seen:
            continue
        seen.add(norm_city(place))
        offices.append({"place": place,
                        "quote": text[max(prev_end, pos - 40):m.end()].strip(),
                        "hq_label": bool(HQ_LABEL.search(window))})
    return offices


def read_site(website: str, known: dict[str, str]) -> dict:
    base = website.rstrip("/")
    pages, offices = [], []
    for path in SITE_PAGES:
        url = base + path + ("/" if not path else "")
        try:
            body = fetch_page(url)
        except Unavailable:
            if not path:
                raise
            continue
        if body is None:
            if not path:
                raise Unavailable(f"{url}: home page did not load")
            continue
        pages.append(url)
        for o in site_offices(page_text(body), known):
            if not any(same_city(o["place"], x["place"]) for x in offices):
                offices.append({**o, "url": url})
        time.sleep(0.5)
    return {"checked": date.today().isoformat(), "pages": pages, "offices": offices}


# ---------------------------------------------------------------- the rule

def decide(record: dict, statement: dict | None) -> dict:
    """Apply the rule to a record. Pure: verify re-runs it offline."""
    adv = record.get("adv")
    site = record.get("site") or {}
    principal = adv["principal"]["place"] if adv else None
    offices = site.get("offices") or []

    def adv_office(place):
        for o in (adv or {}).get("others", []):
            if same_city(o["place"], place):
                staff = o["advisory_staff"]
                return (f" The Form ADV lists that office ({titled(o['street'])}) "
                        f"with {staff} advisory staff." if staff is not None else
                        f" The Form ADV lists that office ({titled(o['street'])}).")
        return " The Form ADV does not list that office."

    where = (f"{titled(adv['principal']['street'])}, {principal} "
             f"({adv['firm']}, CRD {adv['crd']}, {adv['filing']} filed {adv['filed']})"
             if adv else None)
    if statement:
        if not same_city(statement["place"], principal):
            return {"value": statement["place"], "won_by": "site_statement",
                    "basis": f"The firm's own site disagrees with the Form ADV principal "
                             f"office, {where}. {statement['basis']}"
                             f"{adv_office(statement['place']) if adv else ''} {RULE}"}
    if site.get("unchecked") and not statement:
        raise SystemExit(f"site unchecked ({site['unchecked']}): the rule cannot be "
                         f"applied; re-run firm-offices.py, or record the site's "
                         f"statement in config.json profile.site_office")
    listed = "; ".join(o["place"] for o in offices)
    labeled = [o for o in offices if o["hq_label"]]
    if labeled and principal and not same_city(labeled[0]["place"], principal):
        o = labeled[0]
        return {"value": o["place"], "won_by": "site_hq_label",
                "basis": f"The firm's site labels {o['place']} its headquarters "
                         f"(\"{o['quote']}\", {o['url']}); the Form ADV principal "
                         f"office is {where}.{adv_office(o['place'])} {RULE}"}
    if offices and principal and not any(same_city(o["place"], principal) for o in offices):
        o = offices[0]
        return {"value": o["place"], "won_by": "site_list",
                "basis": f"The firm's site lists its offices as {listed} ({o['url']}), "
                         f"without the Form ADV principal office, {where}; the first "
                         f"office it lists is published.{adv_office(o['place'])} {RULE}"}
    if principal:
        agree = (f"The firm's site lists {listed}; the principal office is among "
                 f"them, so the site agrees." if offices else
                 f"The firm's site names no office in its served pages "
                 f"({len(site.get('pages', []))} checked), so the Form ADV stands.")
        if statement:
            agree = f"The firm's recorded site statement names {statement['place']} and agrees."
        return {"value": principal, "won_by": "adv_principal",
                "basis": f"Principal office on the newest Form ADV: {where}. {agree} "
                         f"{RULE}"}
    if offices:
        o = labeled[0] if labeled else offices[0]
        return {"value": o["place"], "won_by": "site_list",
                "basis": f"The firm files no Form ADV; its site lists {listed} "
                         f"({o['url']}), and the {'labeled' if labeled else 'first'} "
                         f"office is published. {RULE}"}
    raise SystemExit("no Form ADV and no office on the site: record the firm's own "
                     "statement in config.json profile.site_office")


def statement_of(p: Paths) -> dict | None:
    s = p.config().get("profile", {}).get("site_office")
    if s and not all(s.get(k) for k in ("place", "url", "quote", "basis")):
        raise SystemExit(f"{p.slug}: config.json profile.site_office needs place, url, "
                         f"quote and basis")
    return s


# ---------------------------------------------------------------- the record

def build_record(p: Paths) -> dict:
    """Read the newest ADV and the site. Raises Unavailable on a failed read."""
    crd = adviser_crd(p)
    adv = parse_adv(adv_text(fetch_adv(crd)), crd) if crd else None
    known = {}
    for o in ([adv["principal"]] + adv["others"]) if adv else []:
        if o["city"]:
            known[o["place"].split(",")[0]] = o["place"]
    website = json.loads(p.investor.read_text())["website"]
    try:
        site = read_site(website, known)
    except Unavailable as e:
        site = {"checked": date.today().isoformat(), "unchecked": str(e)}
    return {"adv": adv, "site": site}


def hq_field(record: dict, hq: dict, statement: dict | None) -> dict:
    cites = []
    if record.get("adv"):
        a = record["adv"]
        cites.append({"source": f"Form ADV Item 1.F and Schedule D 1.F, {a['firm']} "
                                f"({a['filing']} filed {a['filed']})", "url": a["url"]})
    if statement:
        cites.append({"source": "the firm's own site", "url": statement["url"],
                      "quote": statement["quote"]})
    for o in (record.get("site") or {}).get("offices", [])[:1]:
        cites.append({"source": "the firm's own site, office list", "url": o["url"]})
    return {"value": hq["value"], "source": "sources/offices.json",
            "basis": hq["basis"], "sources": cites}


def dump_like(path: Path, obj, like: str | None = None) -> None:
    """Rewrite a JSON file in the style it already has (indent, escaping,
    final newline), so the diff shows the content that changed and nothing else."""
    text = path.read_text() if like is None else like
    m = re.search(r"\n( +)\S", text[:400])     # first indented line, list or object root
    out = json.dumps(obj, indent=len(m.group(1)) if m else 2, ensure_ascii=text.isascii())
    write_atomic(path, out + ("\n" if text.endswith("\n") else ""))


def apply(p: Paths, record: dict, hq: dict, statement: dict | None) -> str | None:
    """Write the decision into investor.json and its provenance. Returns the
    previous value when it changed."""
    row = json.loads(p.investor.read_text())
    sources = json.loads(p.investor_sources.read_text())
    before = row.get("hq_location")
    if before != hq["value"]:
        row["hq_location"] = hq["value"]
        dump_like(p.investor, row)
    sources.setdefault("fields", {})["hq_location"] = hq_field(record, hq, statement)
    dump_like(p.investor_sources, sources)
    return before if before != hq["value"] else None


def refresh(p: Paths) -> dict:
    """The record for the builder: re-read both sources, and fall back to the
    stored record only when a source is unavailable today."""
    try:
        record = build_record(p)
    except Unavailable as e:
        if not p.offices.exists():
            raise SystemExit(f"{p.slug}: {e}; no stored sources/offices.json to fall back on")
        print(f"offices: {e}; using the stored record")
        return json.loads(p.offices.read_text())
    write_atomic(p.offices, json.dumps(record, indent=1, ensure_ascii=False) + "\n")
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("investor", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--check", action="store_true", help="compare only, write nothing")
    args = ap.parse_args()
    if bool(args.investor) == args.all:
        ap.error("give one investor slug or --all")
    slugs = (sorted(d.name for d in INVESTORS.iterdir() if (d / "investor" / "investor.json").exists())
             if args.all else [args.investor])
    drift = 0
    for slug in slugs:
        p = Paths(slug)
        if args.all and p.in_flight.exists() and not args.check:
            print(f"{slug:24} SKIPPED: in flight ({p.rel(p.in_flight)}); its session runs this")
            continue
        try:
            record = build_record(p)
        except Unavailable as e:
            print(f"{slug:24} UNAVAILABLE: {e}")
            drift += 1
            continue
        statement = statement_of(p)
        hq = decide(record, statement)
        published = json.loads(p.investor.read_text()).get("hq_location")
        mark = "ok" if published == hq["value"] else f"DIFFERS (published {published!r})"
        print(f"{slug:24} {hq['value']:22} {hq['won_by']:15} {mark}")
        if args.check:
            drift += published != hq["value"]
            continue
        write_atomic(p.offices, json.dumps(record, indent=1, ensure_ascii=False) + "\n")
        before = apply(p, record, hq, statement)
        if before is not None:
            print(f"{'':24} changed: {before!r} -> {hq['value']!r}")
    if args.check and drift:
        sys.exit(1)


if __name__ == "__main__":
    main()
