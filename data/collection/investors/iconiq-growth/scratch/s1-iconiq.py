#!/usr/bin/env python3
"""What each registration statement says about ICONIQ's position, sentence by
sentence: for every third-party registrant in sources/edgar/fts-hits.json whose
hits include a prospectus-type form (S-1, S-1/A, DRS, DRS/A, 424B4, F-1, S-4,
10-12G), fetch the hit documents (SEC, paced through shared_throttle) and keep
the sentences that name ICONIQ together with a series of preferred stock, a
purchase, a price, a date or a board seat. Filing-grade evidence of which round
the growth funds entered (COLLECTION.md 6: for a company that went public, the
prospectus lists every preferred series with dates and holders).
Output: sources/edgar/s1-iconiq.json {registrant: [{form, date, url, sentences}]}
Usage: python3 data/collection/investors/iconiq-growth/scratch/s1-iconiq.py [--only REGEX]
"""
import html as H, json, re, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import shared_throttle  # noqa: E402
from paths import write_atomic  # noqa: E402
INV = HERE.parent
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
CACHE = HERE / "s1-raw"
FORMS = re.compile(r"^(S-1|S-1/A|DRS|DRS/A|424B\d|F-1|F-1/A|S-4|S-4/A|10-12G|10-12G/A)$")
KEEP = re.compile(r"(Series [A-Z0-9-]+|preferred stock|purchased|aggregate purchase price|per share|board of directors|director since|since [A-Z][a-z]+ 20\d\d|in (?:January|February|March|April|May|June|July|August|September|October|November|December) 20\d\d|tender offer|secondary)", re.I)


def get(url: str) -> str:
    f = CACHE / re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("/Archives/edgar/data/")[-1])
    if f.exists():
        return f.read_text(errors="replace")
    for attempt in range(4):
        shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-sS", "--max-time", "120", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code == b"200":
            CACHE.mkdir(exist_ok=True)
            f.write_bytes(body)
            return body.decode("utf-8", "replace")
        time.sleep(3 * (attempt + 1))
    return ""


def main():
    only = re.compile(sys.argv[sys.argv.index("--only") + 1], re.I) if "--only" in sys.argv else None
    fts = json.load(open(INV / "sources/edgar/fts-hits.json"))
    out = {}
    for r in fts["registrants"]:
        if r.get("bucket") != "third_party":
            continue
        name = r["registrant"]
        if only and not only.search(name):
            continue
        docs = [f for f in r.get("filings", []) if FORMS.match(f.get("form", ""))]
        if not docs:
            continue
        seen_urls, rows, seen_s = set(), [], set()
        for f in docs[:6]:
            if f["url"] in seen_urls:
                continue
            seen_urls.add(f["url"])
            t = get(f["url"])
            if not t:
                continue
            t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
            t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", t)))
            sents = re.split(r"(?<=[.;])\s+(?=[A-Z(])", t)
            keep = []
            for s in sents:
                if re.search(r"iconiq", s, re.I) and KEEP.search(s) and len(s) < 1500:
                    k = re.sub(r"\W+", "", s.lower())[:150]
                    if k not in seen_s:
                        seen_s.add(k)
                        keep.append(s.strip())
            if keep:
                rows.append({"form": f["form"], "date": f["date"], "url": f["url"], "sentences": keep[:25]})
        if rows:
            out[name] = rows
            print(f"{name[:50]:50s} {sum(len(x['sentences']) for x in rows)} sentences", flush=True)
    dest = INV / "sources/edgar/s1-iconiq.json"
    prev = json.loads(dest.read_text()) if dest.exists() else {}
    prev.update(out)
    write_atomic(dest, json.dumps({k: v for k, v in prev.items() if not k.startswith("_")} | {"_readme": __doc__.strip()}, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {dest.relative_to(ROOT)}: {len(prev)} registrants")


if __name__ == "__main__":
    main()
