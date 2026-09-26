#!/usr/bin/env python3
"""EDGAR full-text sweep — the exit-side disclosure layer (COLLECTION.md §5).

Queries EDGAR full-text search (2001+) for the investor's fund-entity phrases
and aggregates the hits by third-party registrant: IPO S-1s (investors'
rights agreement signatories, principal holders), 424B selling-stockholder
tables, acquirers' S-3/S-4/8-K/merger proxies, Reg A offering circulars.
The investor's own vehicles, its LPs' registered funds (NPORT/N-CSR) and
13F/D/G filers are separated out, not judged. For each third-party
registrant the primary document of the earliest hits is fetched and the
sentences around the phrase are kept as evidence for the judge.

Usage: python3 scripts/edgar-fts-sweep.py <slug> [--no-fetch]
Config: edgar.fts_phrases (list of phrases; default: the investor name),
        edgar.fts_own_pattern (regex of registrant names that are the
        investor's own entities or people; default from desks.us patterns).
Output: sources/edgar/fts-hits.json
"""
import json, re, sys, time, urllib.parse, urllib.request, html
from pathlib import Path

UA = "merit-capital research erik@meritcapit.al"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths  # noqa: E402
LP_FORMS = {"NPORT-P", "NPORT-P/A", "N-CSR", "N-CSRS", "N-CSR/A", "N-2", "N-2/A", "N-PORT", "497", "497K", "N-1A"}
OWN_FORMS = {"D", "D/A", "13F-HR", "13F-HR/A", "13F-NT", "SC 13D", "SC 13D/A", "SC 13G", "SC 13G/A", "3", "4", "4/A", "3/A", "5", "ADV"}


def get(url, tries=3, sleep=0.35):
    """Fetch with curl (the system Python's TLS chain is broken on this Mac; every
    EDGAR script in this repo fetches through curl for the same reason)."""
    import subprocess
    err = None
    for i in range(tries):
        r = subprocess.run(["curl", "-s", "-m", "120", "-A", UA, "-H", "Accept-Encoding: identity", url],
                           capture_output=True)
        if r.returncode == 0 and r.stdout:
            time.sleep(sleep)
            return r.stdout
        err = RuntimeError(f"curl rc={r.returncode} for {url}")
        time.sleep(2 + 3 * i)
    raise err


FTS_FIRST_YEAR = 2001      # full-text search covers 2001 onward
FTS_MAX_FROM = 9900        # the index refuses offsets past 10,000
MIN_WINDOW_DAYS = 90       # a window is not split below a quarter


def fts(phrase, frm, start=None, end=None):
    q = urllib.parse.quote(f'"{phrase}"')
    dates = f"dateRange=custom&startdt={start}&enddt={end}" if start else "dateRange=all"
    return json.loads(get(f"https://efts.sec.gov/LATEST/search-index?q={q}&{dates}&from={frm}"))


def fts_page(phrase, frm, start=None, end=None, tries=3):
    """One results page, or None when the index keeps failing it. A deep
    offset can answer {"message": "Internal server error"} on every retry
    (IVP: from=2100 of 2,196 hits, 2026-09-26), so a page without "hits" is a
    failure to report, never an empty page."""
    for i in range(tries):
        try:
            j = fts(phrase, frm, start, end)
        except (RuntimeError, ValueError):
            j = None
        if isinstance(j, dict) and "hits" in j:
            return j
        time.sleep(3 + 4 * i)
    return None


def sweep_window(phrase, start=None, end=None):
    """Page through one query: (hits by id, total, complete, rows read).
    Incomplete when a page kept failing or the total runs past the index's
    offset limit. Rows can exceed distinct ids: the index counts a few
    documents twice (IVP: 2,196 rows, 2,194 distinct)."""
    got, frm, total = {}, 0, None
    while True:
        j = fts_page(phrase, frm, start, end)
        if j is None:
            return got, total, False, frm
        total = j["hits"]["total"]["value"] if total is None else total
        page = j["hits"]["hits"]
        if not page:
            return got, total, True, frm
        for h in page:
            got[h["_id"]] = h
        frm += len(page)
        if frm >= total:
            return got, total, True, frm
        if frm >= FTS_MAX_FROM:
            return got, total, False, frm


def sweep_phrase(phrase):
    """Every hit for a phrase: (hits by id, coverage record). A query that
    cannot be read to the end is re-run in date windows (five years, halved
    again where a window still fails, down to a quarter), so no window needs
    a deep offset; whatever still cannot be read is reported as partial."""
    from datetime import date, timedelta
    got, total, complete, rows = sweep_window(phrase)
    coverage = {"phrase": phrase, "total": total, "complete": complete, "failed_windows": []}
    if complete or total is None:
        # read to the end, or the index would not serve even the first page:
        # an outage, which splitting would only multiply
        coverage.update(read=rows, distinct=len(got))
        if total is None:
            coverage["failed_windows"].append(["all dates", "first page refused"])
        return got, coverage
    coverage["read"] = 0

    def run(start, end):
        hits, wtotal, ok, n = sweep_window(phrase, start.isoformat(), end.isoformat())
        got.update(hits)
        coverage["read"] += n
        if ok:
            return
        # only a deep page is helped by a narrower window; a refused first
        # page is recorded as it is
        if wtotal is None or (end - start).days <= MIN_WINDOW_DAYS:
            coverage["failed_windows"].append([start.isoformat(), end.isoformat()])
            return
        mid = start + (end - start) / 2
        run(start, mid)
        run(mid + timedelta(days=1), end)

    today = date.today()
    for y in range(FTS_FIRST_YEAR, today.year + 1, 5):
        run(date(y, 1, 1), min(date(y + 4, 12, 31), today))
    coverage["complete"] = not coverage["failed_windows"]
    coverage["distinct"] = len(got)
    coverage["split_by_date"] = True
    return got, coverage


def strip_html(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    return re.sub(r"\s+", " ", t)


def main():
    slug = sys.argv[1]
    no_fetch = "--no-fetch" in sys.argv
    P = Paths(slug)
    cfg = P.config()
    ecfg = cfg.get("edgar", {})
    phrases = ecfg.get("fts_phrases") or [cfg.get("name") or slug.replace("-", " ").title()]
    own_pat = ecfg.get("fts_own_pattern")
    if not own_pat:
        pats = [p for d in (cfg.get("desks") or []) if d.get("desk") == "us" for p in d.get("patterns", [])]
        own_pat = "|".join(pats) or re.escape(phrases[0])
    own_re = re.compile(own_pat, re.I)
    phrase_re = re.compile("|".join(re.escape(p) for p in phrases), re.I)

    hits, coverage = {}, []
    for phrase in phrases:
        got, cov = sweep_phrase(phrase)
        for _id, h in got.items():
            hits.setdefault(_id, h["_source"] | {"_id": _id, "_phrase": phrase})
        coverage.append(cov)
        if cov["complete"]:
            print(f"{phrase!r}: {cov['total']} hits ({cov['distinct']} distinct"
                  f"{', read in date windows' if cov.get('split_by_date') else ''})")
        else:
            print(f"{phrase!r}: partial: {cov['read']} of {cov['total']} hits read; "
                  f"unreadable windows {cov['failed_windows']}")

    by = {}
    for h in hits.values():
        for i, name in enumerate(h.get("display_names") or []):
            clean = re.sub(r"\s+\(CIK.*$", "", name).strip()
            cik = (h.get("ciks") or [None] * (i + 1))[i] if i < len(h.get("ciks") or []) else None
            key = clean
            rec = by.setdefault(key, {"registrant": clean, "cik": cik, "forms": {}, "first_date": h["file_date"],
                                      "last_date": h["file_date"], "filings": []})
            rec["forms"][h["form"]] = rec["forms"].get(h["form"], 0) + 1
            rec["first_date"] = min(rec["first_date"], h["file_date"])
            rec["last_date"] = max(rec["last_date"], h["file_date"])
            acc, fn = h["_id"].split(":", 1)
            rec["filings"].append({"form": h["form"], "date": h["file_date"], "adsh": acc,
                                   "url": f"https://www.sec.gov/Archives/edgar/data/{(cik or '0').lstrip('0') or '0'}/{acc.replace('-', '')}/{fn}",
                                   "index": f"https://www.sec.gov/Archives/edgar/data/{(cik or '0').lstrip('0') or '0'}/{acc.replace('-', '')}/{acc}-index.htm"})

    for rec in by.values():
        forms = set(rec["forms"])
        if own_re.search(rec["registrant"]):
            rec["bucket"] = "own"
        elif forms & LP_FORMS and not (forms - LP_FORMS):
            rec["bucket"] = "lp_side"
        elif forms <= OWN_FORMS:
            rec["bucket"] = "ownership_forms"   # 13D/G, 3/4, D on a third party: judged elsewhere
        else:
            rec["bucket"] = "third_party"
        rec["filings"].sort(key=lambda f: f["date"])

    third = [r for r in by.values() if r["bucket"] == "third_party"]
    print(f"registrants: {len(by)} — third-party {len(third)}, own {sum(r['bucket']=='own' for r in by.values())}, "
          f"lp-side {sum(r['bucket']=='lp_side' for r in by.values())}, ownership-form-only {sum(r['bucket']=='ownership_forms' for r in by.values())}")

    if not no_fetch:
        for rec in third:
            rec["snippets"] = []
            seen = 0
            for f in rec["filings"]:
                if seen >= 2:
                    break
                if f["form"] in OWN_FORMS or f["form"] in LP_FORMS:
                    continue
                try:
                    t = strip_html(get(f["url"]))
                except Exception as e:  # noqa
                    rec["snippets"].append({"url": f["url"], "error": str(e)[:120]})
                    seen += 1
                    continue
                found = [t[max(0, m.start() - 260): m.end() + 260] for m in phrase_re.finditer(t)]
                rec["snippets"].append({"url": f["url"], "form": f["form"], "date": f["date"],
                                        "mentions": len(found), "context": found[:3]})
                seen += 1
            print(f"  {rec['registrant'][:44]:44} {rec['first_date']} {dict(rec['forms'])} "
                  f"snippets={sum(s.get('mentions', 0) for s in rec['snippets'])}")

    out = P.edgar / "fts-hits.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    json.dump({"_readme": "EDGAR full-text sweep (scripts/edgar-fts-sweep.py): hits for the configured phrases "
                          "aggregated by registrant; bucket third_party = exit-side disclosure candidates for the "
                          "judge (S-1 IRA signatories and holder tables, 424B selling stockholders, acquirer "
                          "S-3/S-4/8-K), own = the investor's entities/people, lp_side = registered funds holding "
                          "the investor's vehicles, ownership_forms = 13D/G, 3/4 or D filings handled by the "
                          "entities/ownership layers.",
               "phrases": phrases, "own_pattern": own_pat, "swept_at": time.strftime("%Y-%m-%d"),
               # Per phrase: total hits, how many were read, and any date window
               # the index would not serve. A partial sweep is recorded as one,
               # never as the absence of the unread hits.
               "coverage": coverage,
               "registrants": sorted(by.values(), key=lambda r: (r["bucket"], r["first_date"]))},
              open(out, "w"), indent=2, ensure_ascii=False)
    print("wrote", P.rel(out))


if __name__ == "__main__":
    main()
