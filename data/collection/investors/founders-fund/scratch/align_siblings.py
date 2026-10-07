"""Cross-investor alignment (COLLECTION.md s9): the stale sibling rows this run found, written from its cited evidence.
One classification line per row into each book's scratch/queue/align-from-founders-fund.out.jsonl, recorded, exported."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]; INV = ROOT / "data/collection/investors"
sys.path.insert(0, str(Path(__file__).parent))
from jl import sibling_val
SA = "https://stockanalysis.com/stocks/prch/market-cap/"
enter = sibling_val("ribbit-capital", "enter"); lighter = sibling_val("coatue", "lighter")
ROWS = {
 "tiger-global-management": [{"slug": "calibrate", "status": "acquired", "valuation_usd": None, "note": "Aligned from the Founders Fund run (2026-10-06): sold to Madryn Asset Management in a restructuring, October 2023 (https://insider.fitt.co/calibrate-restructures-sells-to-private-equity-firm/)."}],
 "y-combinator": [{"slug": "eight-sleep", "status": "private", "note": "Aligned from the Founders Fund run (2026-10-06): Eight Sleep is an operating private company (a $100M round in August 2025); no acquisition is on record."}],
 "coatue": [{"slug": "enter", **enter, "note": "Aligned from the Founders Fund run (2026-10-06): $100M Series B of May 2026 at $1.2B (PR Newswire)."}],
 "sequoia-capital": [{"slug": "enter", **enter, "note": "Aligned from the Founders Fund run (2026-10-06): $100M Series B of May 2026 at $1.2B (PR Newswire)."}],
 "first-round-capital": [{"slug": "instacanvas", "status": "acquired", "note": "Aligned from the Founders Fund run (2026-10-06): Instacanvas became Twenty20, which Envato bought in 2019 (https://www.selling-stock.com/Article/envato-acquires-twenty20)."},
                         {"slug": "readyforce", "status": "acquired", "note": "Aligned from the Founders Fund run (2026-10-06): acquired by LookSharp, December 2014 (https://techcrunch.com/2014/12/02/looksharp-readyforce/)."}],
 "a16z": [{"slug": "lighter", **lighter, "note": "Aligned from the Founders Fund run (2026-10-06): $68M round at $1.5B, as the Coatue and Ribbit books carry it."}],
 "lux-capital": [{"slug": "plethora", "status": "unknown", "note": "Aligned from the Founders Fund run (2026-10-06): Plethora Corp filed Forms D for new rounds in 2020 and 2021 (CIK 1738554), so the business was not sold in 2019; its current state is not established."}],
 "battery-ventures": [{"slug": "porch-group", "valuation_usd": 1950000000, "valuation_range": "1b_plus", "valuation_source": "web_verified", "valuation_citation": SA, "valuation_asof": "2026-10-06", "valuation_confidence": "high",
                       "note": "Aligned from the Founders Fund run (2026-10-06): market cap $1.95B replaces the float."}],
 "menlo-ventures": [{"slug": "readyforce", "status": "acquired", "note": "Aligned from the Founders Fund run (2026-10-06): acquired by LookSharp, December 2014 (https://techcrunch.com/2014/12/02/looksharp-readyforce/)."},
                    {"slug": "synthego", "status": "acquired", "valuation_usd": None, "note": "Aligned from the Founders Fund run (2026-10-06): Chapter 11 in May 2025 with a sale to its lenders (https://www.bloomberg.com/news/articles/2025-05-06/gene-editor-synthego-files-bankruptcy-to-sell-itself-to-lenders)."}],
 "8vc": [{"slug": "synthego", "status": "acquired", "valuation_usd": None, "note": "Aligned from the Founders Fund run (2026-10-06): Chapter 11 in May 2025 with a sale to its lenders (https://www.bloomberg.com/news/articles/2025-05-06/gene-editor-synthego-files-bankruptcy-to-sell-itself-to-lenders)."}],
 "greylock": [{"slug": "gowalla", "status": "defunct", "valuation_usd": None, "note": "Aligned from the Founders Fund run (2026-10-06): Facebook hired the team in December 2011 without buying the service, which closed in March 2012 (https://en.wikipedia.org/wiki/Gowalla): defunct under the acqui-hire rule. The 2023 Gowalla is a new company."}],
}
only = sys.argv[1:] 
for inv, lines in ROWS.items():
    if only and inv not in only: continue
    d = INV / inv
    if (d / "scratch/in-flight.json").exists(): print(inv, "SKIP in flight"); continue
    dirty = subprocess.run(["git", "status", "--porcelain", "--", str(d / "companies")], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if dirty: print(inv, "SKIP uncommitted company files:", dirty[:80].replace("\n", " ")); continue
    f = d / "scratch/queue/align-from-founders-fund.out.jsonl"; f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text("".join(json.dumps(l, ensure_ascii=False) + "\n" for l in lines))
    r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(f)], cwd=ROOT, capture_output=True, text=True)
    last = (r.stdout + r.stderr).strip().splitlines()[-3:]
    ok = "recorded" in " ".join(last) and "REJECTED" not in (r.stdout + r.stderr)
    e = subprocess.run([sys.executable, "scripts/run.py", "export", "--investor", inv], cwd=ROOT, capture_output=True, text=True) if ok else None
    print(inv, "OK" if ok else "FAIL", "|", " / ".join(x.strip()[:150] for x in last), "|", (e.stdout.strip().splitlines()[-1][:80] if e and e.stdout.strip() else (e.stderr.strip()[-120:] if e else "")))
