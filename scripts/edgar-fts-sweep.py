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
ROOT = Path(__file__).resolve().parent.parent
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


def fts(phrase, frm):
    q = urllib.parse.quote(f'"{phrase}"')
    return json.loads(get(f"https://efts.sec.gov/LATEST/search-index?q={q}&dateRange=all&from={frm}"))


def strip_html(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    return re.sub(r"\s+", " ", t)


def main():
    slug = sys.argv[1]
    no_fetch = "--no-fetch" in sys.argv
    inv = ROOT / "data/collection/investors" / slug
    cfg = json.load(open(inv / "config.json"))
    ecfg = cfg.get("edgar", {})
    phrases = ecfg.get("fts_phrases") or [cfg.get("name") or slug.replace("-", " ").title()]
    own_pat = ecfg.get("fts_own_pattern")
    if not own_pat:
        pats = [p for d in (cfg.get("desks") or []) if d.get("desk") == "us" for p in d.get("patterns", [])]
        own_pat = "|".join(pats) or re.escape(phrases[0])
    own_re = re.compile(own_pat, re.I)
    phrase_re = re.compile("|".join(re.escape(p) for p in phrases), re.I)

    hits = {}
    for phrase in phrases:
        frm, total = 0, None
        while True:
            j = fts(phrase, frm)
            total = j["hits"]["total"]["value"] if total is None else total
            page = j["hits"]["hits"]
            if not page:
                break
            for h in page:
                hits[h["_id"]] = h["_source"] | {"_id": h["_id"], "_phrase": phrase}
            frm += len(page)
            if frm >= total or frm >= 9900:
                break
        print(f"{phrase!r}: {total} hits")

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

    out = inv / "sources/edgar/fts-hits.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    json.dump({"_readme": "EDGAR full-text sweep (scripts/edgar-fts-sweep.py): hits for the configured phrases "
                          "aggregated by registrant; bucket third_party = exit-side disclosure candidates for the "
                          "judge (S-1 IRA signatories and holder tables, 424B selling stockholders, acquirer "
                          "S-3/S-4/8-K), own = the investor's entities/people, lp_side = registered funds holding "
                          "the investor's vehicles, ownership_forms = 13D/G, 3/4 or D filings handled by the "
                          "entities/ownership layers.",
               "phrases": phrases, "own_pattern": own_pat, "swept_at": time.strftime("%Y-%m-%d"),
               "registrants": sorted(by.values(), key=lambda r: (r["bucket"], r["first_date"]))},
              open(out, "w"), indent=2, ensure_ascii=False)
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
